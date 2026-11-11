import argparse
import datetime
import hashlib
import json
import pathlib
import re
import time

from search_paper_code import github_session


ROOT = pathlib.Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=100)
    arguments = parser.parse_args()
    queue = json.loads((ROOT / "reproductions/target_100_q1/queue.json").read_text(encoding="utf-8"))
    output = ROOT / "evidence/title_code_search"
    output.mkdir(exist_ok=True)
    session = github_session()
    attempted = 0
    for paper in queue:
        if paper["repository"] or paper["scope_status"].startswith("excluded"):
            continue
        target = output / (hashlib.sha256(paper["doi"].encode()).hexdigest()[:12] + ".json")
        if target.exists():
            continue
        title = re.sub(r"[^\w\s-]", " ", paper["title"])
        phrase = " ".join(title.split()[:12])
        query = '"' + phrase + '" in:readme'
        result = {"doi": paper["doi"], "title": paper["title"], "query": query, "search_type": "github_readme_title_phrase_candidates_not_implementation_confirmation", "retrieved_at": datetime.datetime.now(datetime.timezone.utc).isoformat()}
        try:
            response = session.get("https://api.github.com/search/repositories", params={"q": query, "per_page": 10}, timeout=30)
            response.raise_for_status()
            payload = response.json()
            result["total_count"] = payload["total_count"]
            result["items"] = [{key: item.get(key) for key in ["full_name", "html_url", "description", "license", "size", "fork"]} for item in payload["items"]]
        except Exception as error:
            result["error"] = str(error)
        target.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(paper["doi"], result.get("total_count"), [item["full_name"] for item in result.get("items", [])], result.get("error", ""), flush=True)
        attempted += 1
        if attempted >= arguments.limit:
            break
        time.sleep(6.5)


if __name__ == "__main__":
    main()
