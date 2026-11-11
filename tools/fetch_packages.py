import argparse
import concurrent.futures
import datetime
import hashlib
import json
import pathlib

from search_paper_code import github_session


ROOT = pathlib.Path(__file__).resolve().parents[1]
PRIORITY = ["TaoRen-Rad/WSGG-H2O-CO2-NH3", "CAME-THU/FlamePINN-1D", "ctftamu/SL-GPS", "DENG-MIT/Biomass.jl", "DENG-MIT/CRNN", "DENG-MIT/reactorch", "DENG-MIT/Arrhenius.jl", "DENG-MIT/StiffNeuralODE", "NatLabRockies/cmlm", "tianhanz/DNN-Models-for-Chemical-Kinetics", "vanshs1/ML_DetonationCells_SootFoil", "burn-research/Cypher-challenge-2025", "LorenzoPiu/aPrioriDNS", "Seauagain/DeePODE", "DENG-MIT/CoFFe", "ECRL/ECNet", "caic99/deepflame-kit", "deepflameCFD/deepflame-dev"]


def fetch(package, limit):
    directory = ROOT / "code_packages" / package["id"]
    record_path = directory / "archive.json"
    if record_path.exists():
        record = json.loads(record_path.read_text(encoding="utf-8"))
        if record.get("status") == "downloaded":
            target = ROOT / record["path"]
            if target.exists() and hashlib.sha256(target.read_bytes()).hexdigest() == record["sha256"]:
                return package["repository"], "cached", record["bytes"]
    if not package["redistribution_enabled"] or not package.get("commit"):
        return package["repository"], "link_only", 0
    target = directory / (package["commit"][:12] + ".tar.gz")
    temporary = target.with_suffix(".part")
    record = {"repository": package["repository"], "commit": package["commit"], "source_url": package["archive_url"], "retrieved_at": datetime.datetime.now(datetime.timezone.utc).isoformat(), "license": package["license"], "execution": "not_executed"}
    try:
        digest = hashlib.sha256()
        length = 0
        with github_session().get(package["archive_url"], stream=True, timeout=(15, 45)) as response:
            response.raise_for_status()
            record["resolved_source_url"] = response.url
            with temporary.open("wb") as stream:
                for chunk in response.iter_content(65536):
                    length += len(chunk)
                    if length > limit:
                        raise ValueError("archive exceeds configured byte limit; use pinned upstream download")
                    stream.write(chunk)
                    digest.update(chunk)
        temporary.replace(target)
        record.update({"status": "downloaded", "path": target.relative_to(ROOT).as_posix(), "bytes": length, "sha256": digest.hexdigest()})
    except Exception as error:
        temporary.unlink(missing_ok=True)
        record.update({"status": "not_collected", "error": str(error)})
    record_path.write_text(json.dumps(record, ensure_ascii=False, indent=2), encoding="utf-8")
    return package["repository"], record["status"], record.get("bytes", 0)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--package")
    parser.add_argument("--all-licensed", action="store_true")
    parser.add_argument("--max-mb", type=float, default=5)
    arguments = parser.parse_args()
    packages = json.loads((ROOT / "catalog/code_packages.json").read_text(encoding="utf-8"))
    selected = [item for item in packages if item["id"] == arguments.package] if arguments.package else [item for item in packages if arguments.all_licensed or item["repository"] in PRIORITY]
    if not selected:
        parser.error("package not found")
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        for result in pool.map(lambda item: fetch(item, int(arguments.max_mb * 1024 * 1024)), selected):
            print(result, flush=True)
