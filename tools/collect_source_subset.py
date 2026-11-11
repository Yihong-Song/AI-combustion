import argparse
import base64
import concurrent.futures
import hashlib
import io
import json
import pathlib
import tarfile

from search_paper_code import github_session


ROOT = pathlib.Path(__file__).resolve().parents[1]
SUFFIXES = {".py", ".jl", ".toml", ".yaml", ".yml", ".f", ".f90", ".cpp", ".h", ".c", ".md", ".rst"}
PRIORITY = {"CAME-THU/FlamePINN-1D", "ctftamu/SL-GPS", "NatLabRockies/cmlm", "deepflameCFD/deepflame-dev", "DENG-MIT/CRNN", "tianhanz/DNN-Models-for-Chemical-Kinetics", "Seauagain/DeePODE", "burn-research/Cypher-challenge-2025"}


def retrieve_blob(repository, item):
    response = github_session().get("https://api.github.com/repos/" + repository + "/git/blobs/" + item["sha"], timeout=25)
    response.raise_for_status()
    content = base64.b64decode(response.json()["content"])
    object_sha = hashlib.sha1(b"blob " + str(len(content)).encode() + b"\0" + content).hexdigest()
    if object_sha != item["sha"]:
        raise ValueError("Git blob hash mismatch: " + item["path"])
    return item, content


def collect(package):
    directory = ROOT / "code_packages" / package["id"]
    record_path = directory / "source_snapshot.json"
    if record_path.exists():
        record = json.loads(record_path.read_text(encoding="utf-8"))
        target = ROOT / record.get("path", "missing")
        if record.get("status") == "collected" and target.is_file() and hashlib.sha256(target.read_bytes()).hexdigest() == record["sha256"]:
            return package["repository"], "cached", len(record["files"])
    session = github_session()
    response = session.get("https://api.github.com/repos/" + package["repository"] + "/git/trees/" + package["commit"], params={"recursive": "1"}, timeout=30)
    response.raise_for_status()
    tree = response.json()
    if tree.get("truncated"):
        raise ValueError("truncated repository tree")
    chosen = []
    size = 0
    skipped = []
    for item in sorted(tree["tree"], key=lambda entry: entry["path"]):
        path = pathlib.PurePosixPath(item["path"])
        is_license = path.name.upper() in {"LICENSE", "LICENSE.TXT", "LICENSE.MD", "COPYING", "NOTICE", "NOTICE.TXT"}
        wanted = path.suffix.lower() in SUFFIXES or is_license or path.name.startswith("requirements")
        safe = not path.is_absolute() and ".." not in path.parts and all(part not in {"node_modules", ".venv", "__pycache__"} for part in path.parts)
        if item["type"] != "blob" or item.get("mode") == "120000" or not wanted or not safe or item.get("size", 0) > 200000 or size + item.get("size", 0) > 2000000 or len(chosen) >= 160:
            skipped.append(item["path"])
            continue
        chosen.append(item)
        size += item.get("size", 0)
    contents = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        for result in pool.map(lambda item: retrieve_blob(package["repository"], item), chosen):
            contents.append(result)
    if not any(pathlib.PurePosixPath(item["path"]).name.upper().startswith(("LICENSE", "COPYING")) for item, _ in contents):
        raise ValueError("license file missing from source subset")
    target = directory / (package["commit"][:12] + "-source-only.tar.gz")
    temporary = target.with_suffix(".part")
    with tarfile.open(temporary, "w:gz") as bundle:
        for item, content in contents:
            member = tarfile.TarInfo(package["id"] + "/" + item["path"])
            member.size = len(content)
            member.mode = 0o644
            bundle.addfile(member, io.BytesIO(content))
    temporary.replace(target)
    record = {"status": "collected", "collection_type": "partial_source_snapshot", "repository": package["repository"], "commit": package["commit"], "date": "2026-11-11", "path": target.relative_to(ROOT).as_posix(), "bytes": target.stat().st_size, "sha256": hashlib.sha256(target.read_bytes()).hexdigest(), "limitations": "Selected source/config/README/license only; excludes large files, data, images, weights and some unselected file types. Not a complete upstream distribution or execution claim.", "files": [{"path": item["path"], "git_blob_sha": item["sha"], "sha256": hashlib.sha256(content).hexdigest(), "bytes": len(content)} for item, content in contents], "excluded_paths": skipped}
    record_path.write_text(json.dumps(record, ensure_ascii=False, indent=2), encoding="utf-8")
    return package["repository"], "collected", len(contents)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--package")
    arguments = parser.parse_args()
    packages = json.loads((ROOT / "catalog/code_packages.json").read_text(encoding="utf-8"))
    for package in packages:
        if package["redistribution_enabled"] and (package["id"] == arguments.package if arguments.package else package["repository"] in PRIORITY):
            try:
                print(collect(package), flush=True)
            except Exception as error:
                record = {"status": "not_collected", "collection_type": "partial_source_snapshot", "repository": package["repository"], "commit": package["commit"], "date": "2026-11-11", "error": str(error)}
                (ROOT / "code_packages" / package["id"] / "source_snapshot.json").write_text(json.dumps(record, ensure_ascii=False, indent=2), encoding="utf-8")
                print(package["repository"], "failed", str(error), flush=True)
