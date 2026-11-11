import argparse
import base64
import datetime
import hashlib
import json
import pathlib

from search_paper_code import github_session
from validate import file_list


ROOT = pathlib.Path(__file__).resolve().parents[1]
REPOSITORY = "Yihong-Song/AI-combustion"
BASE = "https://api.github.com/repos/" + REPOSITORY


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--publish", action="store_true")
    arguments = parser.parse_args()
    validation = json.loads((ROOT / "evidence/validation.json").read_text(encoding="utf-8"))
    if validation["status"] != "passed":
        raise ValueError("Run tools/validate.py successfully before publication")
    files = []
    for name in file_list():
        path = ROOT / name
        if not path.is_file() or path.is_symlink() or not path.resolve().is_relative_to(ROOT):
            raise ValueError("Unsupported file: " + name)
        content = path.read_bytes()
        if len(content) > 10 * 1024 * 1024:
            raise ValueError("File too large for this publisher: " + name)
        files.append({"path": name, "bytes": len(content), "sha256": hashlib.sha256(content).hexdigest(), "git_blob_sha": hashlib.sha1(b"blob " + str(len(content)).encode() + b"\0" + content).hexdigest()})
    inventory = {"repository": REPOSITORY, "files": files, "total_bytes": sum(item["bytes"] for item in files), "mode": "publish" if arguments.publish else "preview"}
    (ROOT / "evidence/publication_inventory.json").write_text(json.dumps(inventory, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({key: value for key, value in inventory.items() if key != "files"}, ensure_ascii=False), "files=", len(files), flush=True)
    if not arguments.publish:
        return
    session = github_session()

    def request(method, endpoint, body=None):
        response = session.request(method, BASE + endpoint, json=body, timeout=(15, 90))
        if not response.ok:
            raise RuntimeError(str(response.status_code) + " " + endpoint + ": " + response.text[:500])
        return response.json()

    repository = request("GET", "")
    if repository["full_name"].casefold() != REPOSITORY.casefold() or not repository.get("permissions", {}).get("push"):
        raise ValueError("Repository identity or permission mismatch")
    branch = repository["default_branch"]
    response = session.get(BASE + "/git/ref/heads/" + branch, timeout=25)
    if response.status_code in {404, 409}:
        contents = session.get(BASE + "/contents", timeout=25)
        if contents.status_code not in {200, 404}:
            contents.raise_for_status()
        if contents.status_code == 200 and contents.json():
            raise ValueError("Unexpected files in repository without a default ref")
        initial = request("PUT", "/contents/README.md", {"message": "Initialize AI combustion research collection", "content": base64.b64encode((ROOT / "README.md").read_bytes()).decode(), "branch": branch})
        parent = initial["commit"]["sha"]
    else:
        response.raise_for_status()
        parent = response.json()["object"]["sha"]
    commit = request("GET", "/git/commits/" + parent)
    remote_tree = request("GET", "/git/trees/" + commit["tree"]["sha"] + "?recursive=1")
    if remote_tree.get("truncated"):
        raise ValueError("Remote tree truncated")
    remote_index = {item["path"]: item["sha"] for item in remote_tree["tree"] if item["type"] == "blob"}
    entries = []
    for item in files:
        if remote_index.get(item["path"]) == item["git_blob_sha"]:
            continue
        content = (ROOT / item["path"]).read_bytes()
        if hashlib.sha256(content).hexdigest() != item["sha256"]:
            raise ValueError("File changed during publication: " + item["path"])
        entry = {"path": item["path"], "mode": "100644", "type": "blob"}
        try:
            decoded = content.decode("utf-8")
            if "\0" in decoded:
                raise UnicodeError("binary")
            if len(content) > 500000:
                blob = request("POST", "/git/blobs", {"content": base64.b64encode(content).decode(), "encoding": "base64"})
                if blob["sha"] != item["git_blob_sha"]:
                    raise ValueError("Remote blob mismatch: " + item["path"])
                entry["sha"] = blob["sha"]
                print("Uploaded large text:", item["path"], flush=True)
            else:
                entry["content"] = decoded
        except UnicodeError:
            blob = request("POST", "/git/blobs", {"content": base64.b64encode(content).decode(), "encoding": "base64"})
            if blob["sha"] != item["git_blob_sha"]:
                raise ValueError("Remote blob mismatch: " + item["path"])
            entry["sha"] = blob["sha"]
            print("Uploaded binary:", item["path"], flush=True)
        entries.append(entry)
    if not entries:
        print("Remote files already match local inventory", flush=True)
        return
    tree = {"sha": commit["tree"]["sha"]}
    for start in range(0, len(entries), 100):
        tree = request("POST", "/git/trees", {"base_tree": tree["sha"], "tree": entries[start:start + 100]})
        print("Prepared tree entries:", min(start + 100, len(entries)), "/", len(entries), flush=True)
    new_commit = request("POST", "/git/commits", {"message": "Add documented AI combustion literature, source packages and executed benchmarks", "tree": tree["sha"], "parents": [parent]})
    current = request("GET", "/git/ref/heads/" + branch)["object"]["sha"]
    if current != parent:
        raise ValueError("Remote changed concurrently; ref was not updated. Review and retry.")
    request("PATCH", "/git/refs/heads/" + branch, {"sha": new_commit["sha"], "force": False})
    verified = request("GET", "/git/trees/" + tree["sha"] + "?recursive=1")
    actual = {item["path"]: item["sha"] for item in verified["tree"] if item["type"] == "blob"}
    mismatches = [item["path"] for item in files if actual.get(item["path"]) != item["git_blob_sha"]]
    if verified.get("truncated") or mismatches:
        raise ValueError("Remote verification failed: " + str(mismatches[:10]))
    record = {"repository": REPOSITORY, "url": repository["html_url"], "commit": new_commit["sha"], "branch": branch, "verified_files": len(files), "bytes": inventory["total_bytes"], "checked_at": datetime.datetime.now(datetime.timezone.utc).isoformat(), "method": "GitHub REST Git database API; full local inventory hashes verified; existing unrelated remote paths preserved; no forced ref update"}
    (ROOT / "evidence/publication_result.json").write_text(json.dumps(record, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(record, ensure_ascii=False, indent=2), flush=True)


if __name__ == "__main__":
    main()
