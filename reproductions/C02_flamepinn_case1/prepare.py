import base64
import concurrent.futures
import hashlib
import json
import pathlib
import sys
import tarfile


ROOT = pathlib.Path(__file__).resolve().parents[2]
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "tools"))
from search_paper_code import github_session


def main():
    record = json.loads((ROOT / "code_packages/CAME-THU__FlamePINN-1D/source_snapshot.json").read_text(encoding="utf-8"))
    archive = ROOT / record["path"]
    if hashlib.sha256(archive.read_bytes()).hexdigest() != record["sha256"]:
        raise ValueError("source archive hash mismatch")
    destination = HERE / "work"
    destination.mkdir(exist_ok=True)
    with tarfile.open(archive) as bundle:
        for member in bundle.getmembers():
            if member.issym() or member.islnk() or not (destination / member.name).resolve().is_relative_to(destination.resolve()):
                raise ValueError("unsafe source member")
        bundle.extractall(destination, filter="data")
    source = destination / "CAME-THU__FlamePINN-1D"
    tree_path = ROOT / "evidence/fulltext_cache/flamepinn_tree.json"
    if tree_path.exists():
        tree = json.loads(tree_path.read_text(encoding="utf-8"))
    else:
        response = github_session().get("https://api.github.com/repos/" + record["repository"] + "/git/trees/" + record["commit"], params={"recursive": "1"}, timeout=30)
        response.raise_for_status()
        tree = response.json()
    if tree.get("truncated"):
        raise ValueError("upstream tree is truncated")
    prefix = "freely_prop_simple/ref_solution/results/p1.00_T298_phi0.40/data/"
    selected = [item for item in tree["tree"] if item["type"] == "blob" and item["path"].startswith(prefix) and item["path"].endswith(".npy")]
    if len(selected) != 9:
        raise ValueError("unexpected reference file count")

    def retrieve(item):
        target = source / item["path"]
        if target.exists():
            content = target.read_bytes()
        else:
            response = github_session().get("https://api.github.com/repos/" + record["repository"] + "/git/blobs/" + item["sha"], timeout=30)
            response.raise_for_status()
            content = base64.b64decode(response.json()["content"])
        digest = hashlib.sha1(b"blob " + str(len(content)).encode() + b"\0" + content).hexdigest()
        if digest != item["sha"]:
            raise ValueError("reference blob hash mismatch")
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(content)
        return {"path": item["path"], "git_blob_sha": digest, "sha256": hashlib.sha256(content).hexdigest(), "bytes": len(content), "source_url": "https://github.com/" + record["repository"] + "/blob/" + record["commit"] + "/" + item["path"]}

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        inputs = list(pool.map(retrieve, selected))
    output = {"repository": record["repository"], "commit": record["commit"], "source_archive_sha256": record["sha256"], "reference": "Author first-order finite-difference/bisection reference, 10000 grid points; not independently regenerated", "input_files": inputs}
    results = HERE / "results"
    results.mkdir(exist_ok=True)
    (results / "inputs.json").write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"source": str(source), "reference_files": len(inputs), "commit": record["commit"]}, indent=2))


if __name__ == "__main__":
    main()
