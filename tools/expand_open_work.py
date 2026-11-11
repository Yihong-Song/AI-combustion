import argparse
import datetime
import hashlib
import json
import pathlib
import time

from search_paper_code import github_session


ROOT = pathlib.Path(__file__).resolve().parents[1]
QUERIES = [
    'combustion "neural" in:name,description,readme',
    'flame "operator" in:name,description,readme',
    'thermoacoustic "learning" in:name,description,readme',
    'thermoacoustic "reservoir" in:name,description,readme',
    'combustion "SINDy" in:name,description,readme',
    'combustion "DeepONet" in:name,description,readme',
    'flame "super-resolution" in:name,description,readme',
    'combustion "differentiable" in:name,description,readme',
    'combustion "graph neural" in:name,description,readme',
    'combustion "active learning" in:name,description,readme',
    'combustion "reinforcement" in:name,description,readme',
    'flame "tomography" "neural" in:name,description,readme',
    'soot "machine learning" in:name,description,readme',
    'detonation "machine learning" in:name,description,readme',
    'ignition "neural" "paper" in:name,description,readme',
    'ammonia "PINN" in:name,description,readme',
    'flame "neural network" "Combustion and Flame" in:readme',
    '"chemical kinetics" "learning" in:name,description,readme',
    '"premixed" "learning" in:name,description,readme',
    '"turbulent combustion" "data-driven" in:name,description,readme',
    'combustion "Kolmogorov" in:name,description,readme',
    'combustion "transformer" in:name,description,readme',
    'combustion "uncertainty" "paper" in:readme',
    '"flame transfer" "network" in:name,description,readme',
    '"reaction kinetics" "symbolic" in:name,description,readme',
    '"combustion" "diffusion model" in:readme',
    '"flame" "autoencoder" in:name,description,readme',
    '"chemistry" "neural ODE" "combustion" in:readme',
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=len(QUERIES))
    arguments = parser.parse_args()
    directory = ROOT / "evidence/open_work_search"
    directory.mkdir(exist_ok=True)
    session = github_session()
    for query in QUERIES[:arguments.limit]:
        target = directory / (hashlib.sha256(query.encode()).hexdigest()[:12] + ".json")
        if target.exists():
            continue
        record = {"query": query, "retrieved_at": datetime.datetime.now(datetime.timezone.utc).isoformat(), "purpose": "repository discovery only; hits are not confirmed paper implementations"}
        try:
            response = session.get("https://api.github.com/search/repositories", params={"q": query, "per_page": 30}, timeout=35)
            response.raise_for_status()
            payload = response.json()
            record["total_count"] = payload["total_count"]
            record["url"] = response.url
            record["items"] = [{key: item.get(key) for key in ["full_name", "description", "html_url", "license", "size", "fork", "updated_at"]} for item in payload["items"]]
        except Exception as error:
            record["error"] = str(error)
        target.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(query, record.get("total_count"), [item["full_name"] for item in record.get("items", [])], record.get("error", ""), flush=True)
        time.sleep(6.5)


if __name__ == "__main__":
    main()
