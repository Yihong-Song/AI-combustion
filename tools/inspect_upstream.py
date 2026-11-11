import concurrent.futures
import datetime
import json
import pathlib
import subprocess
import urllib.error
import urllib.request

import requests

from discover import CACHE, HEADERS, fetch, github
from search_paper_code import github_session


ROOT = pathlib.Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "evidence" / "upstream"
OUTPUT.mkdir(parents=True, exist_ok=True)
GITHUB = github_session()


def inspect(repository):
    key = repository.replace("/", "__")
    target = OUTPUT / (key + ".json")
    if target.exists():
        cached = json.loads(target.read_text(encoding="utf-8"))
        if not cached.get("error"):
            return cached
    result = {"repository": repository, "url": "https://github.com/" + repository, "retrieved_at": datetime.datetime.now(datetime.timezone.utc).isoformat()}
    try:
        response = GITHUB.get("https://api.github.com/repos/" + repository + "/commits", params={"per_page": 1}, timeout=40)
        response.raise_for_status()
        result["commit"] = response.json()[0]["sha"]
        result["pin_source"] = "GitHub commits API"
    except Exception as error:
        result["error"] = str(error)
    if result.get("commit"):
        for name in ["README.md", "README.rst", "README", "readme.md", "ReadMe.md", "README.MD", "README.txt"]:
            url = "https://raw.githubusercontent.com/" + repository + "/" + result["commit"] + "/" + name
            try:
                response = requests.get(url, headers=HEADERS, timeout=30)
                if response.status_code == 404:
                    continue
                response.raise_for_status()
                content = response.text
                (OUTPUT / (key + ".readme.txt")).write_text(content, encoding="utf-8")
                result["readme_url"] = url
                result["readme_path"] = "evidence/upstream/" + key + ".readme.txt"
                break
            except urllib.error.HTTPError as error:
                if error.code != 404:
                    result["readme_error"] = str(error)
                    break
            except requests.RequestException as error:
                result["readme_error"] = str(error)
                break
        for name in ["LICENSE", "LICENSE.md", "LICENSE.txt", "COPYING"]:
            url = "https://raw.githubusercontent.com/" + repository + "/" + result["commit"] + "/" + name
            try:
                response = requests.get(url, headers=HEADERS, timeout=30)
                if response.status_code == 404:
                    continue
                response.raise_for_status()
                content = response.text
                (OUTPUT / (key + ".license.txt")).write_text(content, encoding="utf-8")
                result["license_url"] = url
                result["license_path"] = "evidence/upstream/" + key + ".license.txt"
                break
            except urllib.error.HTTPError as error:
                if error.code != 404:
                    result["license_error"] = str(error)
                    break
            except requests.RequestException as error:
                result["license_error"] = str(error)
                break
    target.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    return result


if __name__ == "__main__":
    for query in ["FlamePINN", "CRNN chemical reaction", "thermoacoustic machine learning", "flame super resolution", "PINN flame", "combustion neural ODE"]:
        try:
            _, result = github(query)
            print("SEARCH", query, [(item["full_name"], item["description"]) for item in result["items"]], flush=True)
        except Exception as error:
            print("FAILED", query, str(error), flush=True)
    repositories = ["DENG-MIT/Stiff-PINN", "DENG-MIT/CRNN", "deepflameCFD/deepflame-dev", "caic99/deepflame-kit", "NatLabRockies/cmlm", "ctftamu/SL-GPS", "edwardning/ML_RateConstants", "ytg7146/DU_CNN", "HongyuanDIKyotoU/FSCKPINN", "HongyuanDIKyotoU/Ammonia_PINN_Net", "Ushnish-Sengupta/FYR", "ShuaiGuo16/Data-driven-High-dimensional-UQ-Analysis", "ShuaiGuo16/General-Risk-Analysis-Framework", "ryanxhr/DeepThermal", "burn-research/Cypher-challenge-2025", "jiweiqi/CombustionNet", "lmcastellanos/Deep-learning-dynamical-latencies-for-the-analysis-and-reduction-of-combustion-chemistry-kinetics", "maritimebear/CombustionPINN_RxnProgressVariable", "huwenfeng1128/POD-PINO", "mccartney-ge/GT2021-60283"]
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        for result in pool.map(inspect, repositories):
            print("INSPECT", result["repository"], result.get("commit"), result.get("readme_path"), result.get("license_path"), result.get("error"), flush=True)
