import concurrent.futures
import json
import pathlib

from inspect_upstream import inspect


ROOT = pathlib.Path(__file__).resolve().parents[1]


if __name__ == "__main__":
    repositories = set()
    for path in (ROOT / "evidence/code_search").glob("*.json"):
        data = json.loads(path.read_text(encoding="utf-8"))
        for item in data.get("items", []):
            if not item.get("fork"):
                repositories.add(item["full_name"])
    repositories.update(["TaoRen-Rad/WSGG-H2O-CO2-NH3", "Weihu22/Neural-Implicit-Reconstruction-for-BOS", "tianhanz/DNN-Models-for-Chemical-Kinetics", "ECRL/ECNet", "LorenzoPiu/aPrioriDNS"])
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        for result in pool.map(inspect, sorted(repositories)):
            print(result["repository"], result.get("commit"), result.get("license_path"), result.get("error"), flush=True)
