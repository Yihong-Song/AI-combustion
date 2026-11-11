import concurrent.futures
import argparse
import datetime
import json
import pathlib

from search_paper_code import github_session


ROOT = pathlib.Path(__file__).resolve().parents[1]


def enrich(path):
    data = json.loads(path.read_text(encoding="utf-8"))
    session = github_session()
    base = "https://api.github.com/repos/" + data["repository"]
    try:
        if not data.get("commit"):
            response = session.get(base + "/commits", params={"per_page": 1}, timeout=25)
            response.raise_for_status()
            data["commit"] = response.json()[0]["sha"]
            data.pop("error", None)
        parameters = {"ref": data["commit"]}
        for kind, endpoint in [("readme", "/readme"), ("license", "/license")]:
            if data.get(kind + "_path") and (ROOT / data[kind + "_path"]).is_file():
                continue
            response = session.get(base + endpoint, params=parameters, timeout=25)
            if response.status_code == 404:
                if kind != "license":
                    data[kind + "_status"] = "not_found_via_api"
                    continue
                tree_response = session.get(base + "/git/trees/" + data["commit"], timeout=25)
                tree_response.raise_for_status()
                license_items = [item for item in tree_response.json().get("tree", []) if item["type"] == "blob" and item["path"].upper() in {"LICENSE", "LICENSE.TXT", "LICENSE.MD", "COPYING"}]
                if not license_items:
                    data[kind + "_status"] = "not_found_via_api_or_root_tree"
                    continue
                item = license_items[0]
                response = session.get(base + "/git/blobs/" + item["sha"], timeout=25)
                response.raise_for_status()
                result = response.json()
                result["html_url"] = data["url"] + "/blob/" + data["commit"] + "/" + item["path"]
            else:
                response.raise_for_status()
                result = response.json()
            import base64
            content = base64.b64decode(result["content"])
            target = path.with_suffix("." + kind + ".txt")
            target.write_bytes(content)
            data[kind + "_path"] = target.relative_to(ROOT).as_posix()
            data[kind + "_url"] = result["html_url"]
            data[kind + "_status"] = "retrieved_at_pinned_commit"
            if kind == "license":
                data["license_spdx"] = result.get("license", {}).get("spdx_id")
        data["api_checked_at"] = datetime.datetime.now(datetime.timezone.utc).isoformat()
    except Exception as error:
        data["api_error"] = str(error)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    return data["repository"], bool(data.get("readme_path")), data.get("license_spdx"), data.get("api_error", "")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", action="append")
    arguments = parser.parse_args()
    if arguments.repo:
        paths = []
        for repository in arguments.repo:
            path = ROOT / "evidence/upstream" / (repository.replace("/", "__") + ".json")
            if not path.exists():
                path.write_text(json.dumps({"repository": repository, "url": "https://github.com/" + repository, "retrieved_at": datetime.datetime.now(datetime.timezone.utc).isoformat()}), encoding="utf-8")
            paths.append(path)
    else:
        paths = list((ROOT / "evidence/upstream").glob("*.json"))
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        for result in pool.map(enrich, paths):
            print(result, flush=True)
