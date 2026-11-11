import concurrent.futures
import datetime
import hashlib
import json
import pathlib
import time
import urllib.parse
import urllib.request


ROOT = pathlib.Path(__file__).resolve().parents[1]
CACHE = ROOT / "evidence" / "discovery"
CACHE.mkdir(parents=True, exist_ok=True)
HEADERS = {"User-Agent": "AI-combustion-literature-catalog/0.1 (public academic metadata collection)"}


def fetch(url):
    request = urllib.request.Request(url, headers=HEADERS)
    for attempt in range(3):
        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                return json.load(response)
        except Exception:
            if attempt == 2:
                raise
            time.sleep(2 + attempt * 3)


def crossref(query, issn=None, rows=40):
    key = hashlib.sha256((query + str(issn) + str(rows)).encode()).hexdigest()[:12]
    target = CACHE / ("crossref_" + key + ".json")
    if target.exists():
        return query, json.loads(target.read_text(encoding="utf-8"))
    filters = "from-pub-date:2018-01-01,until-pub-date:2026-11-11,type:journal-article"
    if issn:
        filters += ",issn:" + issn
    parameters = urllib.parse.urlencode({"query.title": query, "rows": rows, "filter": filters})
    raw = fetch("https://api.crossref.org/works?" + parameters)
    fields = ["DOI", "title", "container-title", "author", "published", "published-online", "published-print", "URL", "link", "license", "abstract", "ISSN", "publisher", "type"]
    result = {"query": query, "issn": issn, "url": "https://api.crossref.org/works?" + parameters, "retrieved_at": datetime.datetime.now(datetime.timezone.utc).isoformat(), "total_results": raw["message"]["total-results"], "items": [{key: item[key] for key in fields if key in item} for item in raw["message"]["items"]]}
    target.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    return query, result


def github(query):
    key = hashlib.sha256(query.encode()).hexdigest()[:12]
    target = CACHE / ("github_" + key + ".json")
    if target.exists():
        return query, json.loads(target.read_text(encoding="utf-8"))
    url = "https://api.github.com/search/repositories?" + urllib.parse.urlencode({"q": query, "per_page": 50})
    raw = fetch(url)
    fields = ["full_name", "html_url", "description", "default_branch", "license", "updated_at", "pushed_at", "size", "fork"]
    result = {"query": query, "url": url, "retrieved_at": datetime.datetime.now(datetime.timezone.utc).isoformat(), "total_results": raw["total_count"], "items": [{key: item[key] for key in fields if key in item} for item in raw["items"]]}
    target.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    return query, result


if __name__ == "__main__":
    scholarly_queries = ["machine learning combustion", "deep learning combustion", "physics informed combustion", "neural operator combustion", "transformer combustion flame", "combustion instability machine learning", "machine learning ammonia hydrogen combustion", "flame tomography deep learning", "reinforcement learning combustion", "chemical kinetics neural network", "machine learning turbulent combustion closure", "deep learning chemical kinetics reduction"]
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        for query, result in pool.map(crossref, scholarly_queries):
            print("Crossref", query, len(result["items"]), flush=True)
    repository_queries = ["combustion machine learning", "combustion deep learning", "combustion PINN", "combustion neural operator", "flame tomography", "combustion instability", "chemical kinetics neural", "ChemNODE", "DeepFlame", "ChemPINN", "FlamePINN"]
    for query in repository_queries:
        try:
            _, result = github(query)
            print("GitHub", query, len(result["items"]), flush=True)
        except Exception as error:
            print("FAILED", query, str(error), flush=True)
        time.sleep(3)
