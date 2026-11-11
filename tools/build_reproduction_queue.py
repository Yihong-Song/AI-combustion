import collections
import csv
import json
import pathlib
import re


ROOT = pathlib.Path(__file__).resolve().parents[1]
WILDFIRE = re.compile(r"wildfire|wildland|forest.fire|vegetation.fire|landscape.fire|burned.area|burnt.area|satellite|remote.sens|global.fire", re.I)


def main():
    papers = json.loads((ROOT / "catalog/papers.json").read_text(encoding="utf-8"))
    records = []
    for paper in papers:
        if paper["jcr"]["reported_best_quartile"] != "Q1" or paper["jcr"]["status"] != "provisional_q1_q2":
            continue
        excluded = bool(WILDFIRE.search(paper["title"]))
        relation = paper["code"].get("relationship") or "not_confirmed"
        direct = relation == "author_implementation_readme_explicit"
        record = {"id": paper["id"], "doi": paper["doi"], "title": paper["title"], "year": paper["year"], "journal": paper["journal"], "category": paper["category"], "paper_path": paper["path"], "queue_priority": 1 if direct and paper["code"].get("license") not in {"not_located", None} else 2 if paper["curated_note"] else 3, "scope_status": "excluded_landscape_wildfire_or_remote_sensing" if excluded else "title_level_candidate_fulltext_scope_pending", "q1_evidence_status": "secondary_only_official_year_category_pending", "q1_officially_verified": False, "jcr_year": None, "jcr_category": None, "jcr_evidence_path": None, "repository": paper["code"].get("repository"), "code_relationship": relation, "execution_status": paper["reproduction"]["status"], "exact_paper_target": None, "paper_value": None, "local_value": None, "metric_definition": None, "accepted_q1_reproduction": False, "missing_gates": ["Official JCR Q1 year/category evidence", "Full-text combustion scope and exact figure/table", "Versioned data, code or independent implementation map", "Matching split, model, training budget and metric", "Executed results, comparison and deviations"]}
        if paper["doi"] == "10.1016/j.combustflame.2025.113964":
            record["exact_paper_target"] = "arXiv:2406.09071v1 Section 3.1.1 / Figure 3 first condition, p=1 atm, phi=0.4; final journal correspondence pending"
            record["execution_status"] = "training_started"
            record["experiment_path"] = "reproductions/C02_flamepinn_case1"
            metrics_path = ROOT / record["experiment_path"] / "results/metrics.json"
            if metrics_path.exists():
                metrics = json.loads(metrics_path.read_text(encoding="utf-8"))
                record["execution_status"] = metrics["status"]
                record["local_value"] = metrics.get("fields")
        records.append(record)
    records.sort(key=lambda item: (item["scope_status"].startswith("excluded"), item["queue_priority"], -item["year"], item["doi"]))
    folder = ROOT / "reproductions/target_100_q1"
    folder.mkdir(exist_ok=True)
    (folder / "queue.json").write_text(json.dumps(records, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    fields = ["id", "year", "title", "doi", "journal", "queue_priority", "scope_status", "q1_evidence_status", "repository", "code_relationship", "execution_status", "accepted_q1_reproduction"]
    with (folder / "queue.csv").open("w", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(records)
    summary = {"date": "2026-11-12", "minimum_target": 100, "q1_secondary_candidates": len(records), "scope_excluded": sum(item["scope_status"].startswith("excluded") for item in records), "code_links_reviewed": sum(item["code_relationship"] != "not_confirmed" for item in records), "official_q1_confirmed": 0, "accepted_reproductions": 0, "remaining_to_target": 100, "execution_status_counts": dict(collections.Counter(item["execution_status"] for item in records))}
    (folder / "progress.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
