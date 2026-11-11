import concurrent.futures
import datetime
import json
import pathlib

import requests


ROOT = pathlib.Path(__file__).resolve().parents[1]
DOIS = ["10.1016/j.cej.2025.160402", "10.1016/j.cpc.2025.109802", "10.1007/s10494-024-00626-3", "10.1063/5.0060697", "10.1021/acs.jpca.0c09316", "10.1021/acs.energyfuels.4c06147", "10.1021/acs.energyfuels.0c03211"]


def retrieve(doi):
    target = ROOT / "evidence/discovery" / ("key_" + doi.replace("/", "_") + ".json")
    if target.exists():
        return doi, "cached"
    response = requests.get("https://api.crossref.org/works/" + doi, timeout=25)
    response.raise_for_status()
    item = response.json()["message"]
    target.write_text(json.dumps({"query": "known DOI from upstream README", "url": response.url, "retrieved_at": datetime.datetime.now(datetime.timezone.utc).isoformat(), "items": [item]}, ensure_ascii=False, indent=2), encoding="utf-8")
    return doi, item["title"][0]


if __name__ == "__main__":
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
        for result in pool.map(retrieve, DOIS):
            print(result, flush=True)
