import concurrent.futures
import datetime
import json
import pathlib
import re
import urllib.parse

import bs4
import requests


ROOT = pathlib.Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "evidence/journals"
OUTPUT.mkdir(parents=True, exist_ok=True)
KNOWN = {"Combustion and Flame": "1901", "Proceedings of the Combustion Institute": "6861", "Progress in Energy and Combustion Science": "6930", "Fuel": "2950", "Chemical Engineering Journal": "1639", "Applied Energy": "729"}


def collect(name):
    target = OUTPUT / (re.sub(r"[^a-z0-9]+", "_", name.lower()).strip("_") + ".json")
    cached = json.loads(target.read_text(encoding="utf-8")) if target.exists() else {}
    if cached.get("reported_best_quartile"):
        return cached
    session = requests.Session()
    result = {"journal": name, "retrieved_at": datetime.datetime.now(datetime.timezone.utc).isoformat(), "source_type": "secondary_crowdsourced_letpub", "jcr_edition": None, "jif_year": None, "edition_note": "Source does not explicitly identify the JCR edition; do not infer it from retrieval date or self-citation year.", "officially_verified": False}
    try:
        journal_id = KNOWN.get(name) or cached.get("journal_id")
        if journal_id is None:
            search_url = "https://www.letpub.com/journal-selector?" + urllib.parse.urlencode({"view": "search", "initsub": 1, "title": name})
            response = session.get(search_url, timeout=40)
            response.raise_for_status()
            soup = bs4.BeautifulSoup(response.content, "html.parser")
            result["search_url"] = search_url
            for anchor in soup.find_all("a"):
                label = anchor.get_text(" ", strip=True)
                if label.casefold() == name.casefold():
                    match = re.search(r"(?:journal/|journalid=)(\d+)", anchor.get("href", ""))
                    if match:
                        journal_id = match.group(1)
                        break
        if journal_id is None:
            raise ValueError("Exact journal match not located in LetPub search")
        url = "https://www.letpub.com/journal-selector/journal/" + journal_id
        response = session.get(url, timeout=40)
        response.raise_for_status()
        soup = bs4.BeautifulSoup(response.content, "html.parser")
        text = soup.get_text(" ", strip=True)
        result["page_title"] = soup.title.get_text(" ", strip=True) if soup.title else ""
        result["source_url"] = url
        result["journal_id"] = journal_id
        result["identity_in_page"] = name.casefold() in result["page_title"].casefold()
        match = re.search(r"Quartiles By JIF(.*?)Quartiles By JCI", text)
        result["jif_evidence_text"] = match.group(1).strip() if match else ""
        result["categories"] = [{"category": category.strip(), "collection": collection, "quartile": quartile, "rank": rank} for category, collection, quartile, rank in re.findall(r"Category:\s*(.*?)\s+(SCIE|SSCI|ESCI)\s+(Q[1-4])\s+(\d+/\d+)", result["jif_evidence_text"])]
        result["reported_best_quartile"] = min((entry["quartile"] for entry in result["categories"]), default=None)
        (OUTPUT / (target.stem + ".txt")).write_text(text, encoding="utf-8")
    except Exception as error:
        result["error"] = str(error)
        result["categories"] = []
        result["reported_best_quartile"] = None
    target.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    return result


if __name__ == "__main__":
    papers = json.loads((ROOT / "literature/screened_candidates.json").read_text(encoding="utf-8"))
    journals = sorted({paper["journal"] for paper in papers})
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        for result in pool.map(collect, journals):
            print(result["journal"], result["reported_best_quartile"], result.get("jif_evidence_text", ""), result.get("error", ""), flush=True)
