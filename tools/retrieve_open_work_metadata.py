import argparse
import datetime
import difflib
import html
import json
import pathlib
import re
import time

import requests


ROOT = pathlib.Path(__file__).resolve().parents[1]
TITLES = [
    "DFODE-kit: Deep learning package for solving Flame chemical kinetics with high-dimensional stiff Ordinary Differential Equations",
    "Comprehensive deep learning for combustion chemistry integration: Multi-fuel generalization and a posteriori validation in reacting flow",
    "Graphics processing unit/artificial neural network-accelerated large-eddy simulation of swirling premixed flames",
    "DeepFlame: A deep learning empowered open-source platform for reacting flow simulations",
    "Hard-constrained neural networks for modelling nonlinear acoustics",
    "Data-driven computation of adjoint sensitivities without adjoint solvers: An application to thermoacoustics",
    "Real-time thermoacoustic data assimilation",
    "A real-time digital twin of azimuthal thermoacoustic instabilities",
    "Inferring unknown unknowns: Regularized bias-aware ensemble Kalman filter",
    "SAGE: A machine learning model for primary particle segmentation in TEM images of soot aggregates",
    "A machine learning based full-spectrum correlated k-distribution model for nonhomogeneous gas-soot mixtures",
    "A machine learning based efficient and compact full-spectrum correlated k-distribution model",
    "Deep reinforcement learning for dynamic control of fuel injection timing in multi-pulse compression ignition engines",
    "An Active Learning Guided Genetic Algorithm Framework with Surrogate Modeling for Reduced Combustion Mechanism Optimization and Kinetic Analysis of NH3/H2/n-Heptane Combustion",
    "A Priori Uncertainty Quantification of Reacting Turbulence Closure Models using Bayesian Neural Networks",
    "Data-based instantaneous conditional progress variable dissipation rate modeling for turbulent premixed combustion",
    "Data-based filtered dissipation rate modelling for multi-modal turbulent combustion: Evaluating a priori model generalizability",
    "Learning stiff chemical kinetics using extended deep neural operators",
    "Adaptive chemistry via pre-partitioning of composition space and mechanism reduction",
    "Feature extraction and artificial neural networks for the on-the-fly classification of high-dimensional thermochemical spaces in adaptive-chemistry simulations",
    "Chemistry reduction using machine learning trained from non-premixed micro-mixing modeling: Application to DNS of a syngas turbulent oxy-flame with side-wall effects",
    "Learning dominant physical processes with data-driven balance models",
    "ChemKANs for combustion chemistry modeling and acceleration",
    "Integrated Neural Network Approach for Autonomous Sensitivity Analysis and Optimization of Sectional Soot Kinetic Modeling",
    "Deep learning for continuous lead-time prediction of thermoacoustic instabilities in an annular combustor",
    "Physics-informed neural networks and functional interpolation for stiff chemical kinetics",
    "Active learning of hydrogen combustion with neural network potentials",
    "Robust Identification of Flame Frequency Response via Multi-Fidelity Gaussian Process Approach",
]
DOIS = ["10.1016/j.fuel.2026.138904", "10.1016/j.proci.2026.106166", "10.1016/j.proci.2026.106547", "10.1016/j.cej.2024.149863", "10.1016/j.cej.2023.143779"]


def normalize(title):
    return re.sub(r"[^a-z0-9]", "", html.unescape(re.sub(r"<[^>]+>", "", title)).lower())


def retrieve_title(title):
    import hashlib
    target = ROOT / "evidence/open_work_search" / ("title_" + hashlib.sha256(title.encode()).hexdigest()[:12] + ".json")
    if target.exists():
        return json.loads(target.read_text(encoding="utf-8"))
    record = {"title_query": title, "retrieved_at": datetime.datetime.now(datetime.timezone.utc).isoformat()}
    try:
        response = requests.get("https://api.crossref.org/works", params={"query.title": title, "rows": 3, "filter": "type:journal-article"}, timeout=45)
        response.raise_for_status()
        items = response.json()["message"]["items"]
        record["url"] = response.url
        record["candidates"] = [{"doi": item["DOI"], "title": item.get("title", [""])[0], "score": difflib.SequenceMatcher(None, normalize(title), normalize(item.get("title", [""])[0])).ratio()} for item in items]
        matches = [(item, candidate) for item, candidate in zip(items, record["candidates"]) if candidate["score"] >= 0.92]
        if len(matches) == 1:
            item, candidate = matches[0]
            record["matched_doi"] = item["DOI"].lower()
            path = ROOT / "evidence/discovery" / ("key_" + item["DOI"].lower().replace("/", "_") + ".json")
            if not path.exists():
                path.write_text(json.dumps({"query": title, "url": response.url, "retrieved_at": record["retrieved_at"], "items": [item]}, ensure_ascii=False, indent=2), encoding="utf-8")
    except Exception as error:
        record["error"] = str(error)
    target.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return record


if __name__ == "__main__":
    from add_key_papers import retrieve
    parser = argparse.ArgumentParser()
    parser.add_argument("--retry-errors", action="store_true")
    arguments = parser.parse_args()
    if arguments.retry_errors:
        for path in (ROOT / "evidence/open_work_search").glob("title_*.json"):
            record = json.loads(path.read_text(encoding="utf-8"))
            if record.get("error"):
                path.rename(path.with_suffix(".failed.json"))
    for title in TITLES:
        record = retrieve_title(title)
        print(record["title_query"], record.get("matched_doi"), record.get("candidates", []), record.get("error", ""), flush=True)
        time.sleep(3)
    for doi in DOIS:
        try:
            print(retrieve(doi), flush=True)
        except Exception as error:
            print(doi, str(error), flush=True)
        time.sleep(3)
