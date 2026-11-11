import collections
import csv
import hashlib
import json
import math
import pathlib
import re
import subprocess
import tarfile
from urllib.parse import unquote, urlsplit


ROOT = pathlib.Path(__file__).resolve().parents[1]


def load(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def file_list():
    result = subprocess.run(["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"], cwd=ROOT, check=True, capture_output=True)
    return sorted({path.decode("utf-8") for path in result.stdout.split(b"\0") if path})


def rows(path):
    with (ROOT / path).open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))


def main():
    failures = []
    checks = collections.Counter()

    def check(condition, message, kind):
        checks[kind] += 1
        if not condition:
            failures.append(message)

    def near(actual, expected, label):
        check(math.isclose(actual, expected, rel_tol=1e-8, abs_tol=1e-12), label, "metrics")

    papers = load("catalog/papers.json")
    packages = load("catalog/code_packages.json")
    stats = load("catalog/stats.json")
    paths = file_list()
    check(not any(path.endswith(".part") for path in paths), "temporary download in publication list", "catalog")
    check(len({paper["doi"] for paper in papers}) == len(papers), "duplicate DOI", "catalog")
    check(len({paper["id"] for paper in papers}) == len(papers), "duplicate paper ID", "catalog")
    check(stats["candidate_papers"] == len(papers), "paper count", "catalog")
    check(stats["code_packages"] == len(packages), "package count", "catalog")
    check(dict(collections.Counter(paper["jcr"]["status"] for paper in papers)) == stats["quartile_status"], "quartile counts", "catalog")
    check(sum(bool(paper["curated_note"]) for paper in papers) == stats["reviewed_paper_code_links"], "curated count", "catalog")
    check(len(rows("catalog/papers.csv")) == len(papers), "CSV count", "catalog")
    package_index = {package["id"]: package for package in packages}
    expected_cards = {paper["path"] + "/paper.json" for paper in papers}
    actual_cards = {path for path in paths if path.endswith("/paper.json")}
    check(actual_cards == expected_cards, "stale or missing paper folders: " + str(sorted(actual_cards ^ expected_cards)), "catalog")
    for paper in papers:
        check((ROOT / paper["path"] / "README.md").is_file(), paper["doi"] + " missing README", "catalog")
        card = load(paper["path"] + "/paper.json")
        check(card["doi"] == paper["doi"] and card["id"] == paper["id"], paper["doi"] + " card mismatch", "catalog")
        check(bool(paper["metadata_source"]) and bool(paper["doi_url"]), paper["doi"] + " missing provenance", "catalog")
        check(not paper["jcr"]["officially_verified"] or bool(paper["jcr"]["edition"]), paper["doi"] + " official JCR without edition", "catalog")
        check((paper["jcr"]["status"] == "adjacent_q3_q4") == paper["path"].startswith("literature/adjacent/"), paper["doi"] + " Q3/Q4 placement", "catalog")
        if paper["code"]["package_id"]:
            check(paper["code"]["package_id"] in package_index, paper["doi"] + " missing package", "catalog")
    for package in packages:
        directory = ROOT / "code_packages" / package["id"]
        check(bool(re.fullmatch(r"[a-f0-9]{40}", package["commit"] or "")), package["id"] + " missing commit", "packages")
        if package.get("license_sha256"):
            digest = hashlib.sha256((directory / "UPSTREAM_LICENSE.txt").read_bytes()).hexdigest()
            check(digest == package["license_sha256"], package["id"] + " license hash", "packages")
        for key, success in [("archive", "downloaded"), ("source_snapshot", "collected")]:
            record = package.get(key, {})
            if record.get("status") != success:
                continue
            check(package["redistribution_enabled"], package["id"] + " redistribution without permission", "packages")
            check(record["commit"] == package["commit"], package["id"] + " archive version", "packages")
            target = ROOT / record["path"]
            check(target.is_file(), record["path"] + " missing", "packages")
            if not target.is_file():
                continue
            check(hashlib.sha256(target.read_bytes()).hexdigest() == record["sha256"], record["path"] + " archive hash", "packages")
            with tarfile.open(target, "r:gz") as bundle:
                members = bundle.getmembers()
                check(all(not pathlib.PurePosixPath(member.name).is_absolute() and ".." not in pathlib.PurePosixPath(member.name).parts for member in members), record["path"] + " unsafe member path", "packages")
                if key == "source_snapshot":
                    expected = {package["id"] + "/" + item["path"]: item for item in record["files"]}
                    check({member.name for member in members} == set(expected), record["path"] + " snapshot members", "packages")
                    for member in members:
                        content = bundle.extractfile(member).read()
                        item = expected[member.name]
                        digest = hashlib.sha256(content).hexdigest()
                        blob = hashlib.sha1(b"blob " + str(len(content)).encode() + b"\0" + content).hexdigest()
                        check(digest == item["sha256"] and blob == item["git_blob_sha"], member.name + " source hash", "packages")
    for path in paths:
        target = ROOT / path
        if not target.is_file():
            continue
        if target.suffix == ".py":
            try:
                compile(target.read_text(encoding="utf-8-sig"), path, "exec")
                checks["python_compile"] += 1
            except SyntaxError as error:
                failures.append(path + ": " + str(error))
        if target.suffix.lower() not in {".md", ".py", ".json", ".txt", ".csv", ".html", ".bib"}:
            continue
        text = target.read_text(encoding="utf-8-sig")
        token_patterns = [r"gh[pousr]_" + r"[A-Za-z0-9]{30,}", r"github_pat_" + r"[A-Za-z0-9_]{30,}", r"-----BEGIN " + r"(?:RSA |EC |OPENSSH )?PRIVATE KEY-----"]
        check(not any(re.search(pattern, text) for pattern in token_patterns), path + " possible secret", "secret_scan")
        if target.suffix != ".md":
            continue
        text = re.sub(r"```.*?```", "", text, flags=re.S)
        for destination in re.findall(r"\]\(([^\n)]+)\)", text):
            destination = destination.strip().split(' "')[0].strip("<>")
            parsed = urlsplit(destination)
            if parsed.scheme or not parsed.path:
                continue
            local = (target.parent / unquote(parsed.path)).resolve()
            check(local.is_relative_to(ROOT) and local.exists(), path + " broken local link: " + destination, "markdown_links")
    baseline = "reproductions/B01_hydrogen_ignition/results/"
    metrics = load(baseline + "metrics.json")
    predictions = rows(baseline + "predictions.csv")
    for model, expected in metrics["models"].items():
        selected = [row for row in predictions if row["model"] == model]
        truth = [float(row["reference_tau_s"]) for row in selected]
        predicted = [float(row["predicted_tau_s"]) for row in selected]
        errors = [math.log10(actual) - math.log10(estimate) for actual, estimate in zip(truth, predicted)]
        near(sum(abs(error) for error in errors) / len(errors), expected["log10_MAE"], model + " log MAE")
        mean = sum(math.log10(value) for value in truth) / len(truth)
        near(1 - sum(error * error for error in errors) / sum((math.log10(value) - mean) ** 2 for value in truth), expected["log10_R2"], model + " R2")
        relative = sorted(abs(actual - estimate) / actual for actual, estimate in zip(truth, predicted))
        near((relative[14] + relative[15]) / 2, expected["median_relative_error"], model + " median relative error")
    check(hashlib.sha256((ROOT / baseline / "dataset.csv").read_bytes()).hexdigest() == metrics["dataset_sha256"], "B01 dataset hash", "metrics")
    solution = rows("reproductions/B02_bratu_pinn/results/solution.csv")
    metrics = load("reproductions/B02_bratu_pinn/results/metrics.json")
    errors = [float(row["pinn"]) - float(row["analytical"]) for row in solution]
    near(max(abs(error) for error in errors), metrics["max_absolute_error"], "B02 max error")
    near(math.sqrt(sum(error * error for error in errors) / sum(float(row["analytical"]) ** 2 for row in solution)), metrics["relative_L2_error"], "B02 relative L2")
    near(max(abs(float(solution[index]["pinn"])) for index in [0, -1]), metrics["boundary_max_absolute_error"], "B02 boundary error")
    predictions = rows("reproductions/C01_wsgg_author_demo/results/predictions.csv")
    metrics = load("reproductions/C01_wsgg_author_demo/results/metrics.json")
    truth = [float(row["LBL_divergence_W_m3"]) for row in predictions]
    errors = [float(row["PINN_WSGG_divergence_W_m3"]) - actual for row, actual in zip(predictions, truth)]
    mae = sum(abs(error) for error in errors) / len(errors)
    near(mae, metrics["mean_absolute_error_W_m3"], "C01 MAE")
    near(mae / (max(truth) - min(truth)), metrics["mae_divided_by_reference_range"], "C01 normalized MAE")
    near(math.sqrt(sum(error * error for error in errors) / sum(value * value for value in truth)), metrics["relative_L2_error"], "C01 relative L2")
    near(max(abs(error) for error in errors), metrics["max_absolute_error_W_m3"], "C01 max error")
    report = {"date": "2026-11-11", "status": "passed" if not failures else "failed", "scope": "Local catalog consistency, relative Markdown file targets, source/archive/license hashes, source compilation, token patterns, independent recomputation of saved prediction metrics. Does not validate external URLs, full-text claims, official JCR, original-paper metrics, or B02 differential residual from saved CSV.", "candidate_papers": len(papers), "packages": len(packages), "files_inspected": len(paths), "checks": dict(checks), "failures": failures}
    (ROOT / "evidence/validation.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
