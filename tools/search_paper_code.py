import datetime
import json
import os
import pathlib
import subprocess
import time

import requests


ROOT = pathlib.Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "evidence/code_search"


def github_session():
    session = requests.Session()
    session.headers.update({"Accept": "application/vnd.github+json", "User-Agent": "AI-combustion-academic-catalog"})
    environment = dict(os.environ, GIT_TERMINAL_PROMPT="0", GCM_INTERACTIVE="Never")
    credentials = subprocess.run(["git", "credential", "fill"], input="protocol=https\nhost=github.com\n\n", text=True, capture_output=True, env=environment)
    if credentials.returncode == 0:
        fields = dict(line.split("=", 1) for line in credentials.stdout.splitlines() if "=" in line)
        if fields.get("password"):
            session.headers["Authorization"] = "Bearer " + fields["password"]
    return session


if __name__ == "__main__":
    OUTPUT.mkdir(parents=True, exist_ok=True)
    session = github_session()
    papers = json.loads((ROOT / "literature/screened_candidates.json").read_text(encoding="utf-8"))
    for position, paper in enumerate(papers):
        import hashlib
        target = OUTPUT / (hashlib.sha256(paper["doi"].encode()).hexdigest()[:12] + ".json")
        if target.exists():
            continue
        query = '"' + paper["doi"] + '" in:readme'
        result = {"doi": paper["doi"], "query": query, "search_type": "github_repository_readme_doi_exact", "retrieved_at": datetime.datetime.now(datetime.timezone.utc).isoformat()}
        try:
            response = session.get("https://api.github.com/search/repositories", params={"q": query, "per_page": 10}, timeout=35)
            result["search_url"] = response.url
            response.raise_for_status()
            raw = response.json()
            result["total_count"] = raw["total_count"]
            fields = ["full_name", "html_url", "description", "default_branch", "license", "size", "fork"]
            result["items"] = [{key: item[key] for key in fields if key in item} for item in raw["items"]]
        except Exception as error:
            result["error"] = str(error)
        target.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
        print(position, paper["doi"], result.get("total_count"), [item["full_name"] for item in result.get("items", [])], result.get("error", ""), flush=True)
        time.sleep(2.3)
