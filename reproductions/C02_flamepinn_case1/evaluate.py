import argparse
import hashlib
import importlib.metadata
import json
import pathlib
import platform
import re
import shutil

import matplotlib
import numpy as np


matplotlib.use("Agg")
import matplotlib.pyplot as plt


HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--run", type=int, default=1)
    parser.add_argument("--seed", type=int, default=42)
    arguments = parser.parse_args()
    directories = list((HERE / "work").glob("*/freely_prop_simple/results/p1.00_T298_phi0.40/forward/*/" + str(arguments.run)))
    if len(directories) != 1:
        raise ValueError("Expected one completed run directory")
    output = directories[0]
    inputs = json.loads((HERE / "results/inputs.json").read_text(encoding="utf-8"))
    text = (output / "metrics.txt").read_text(encoding="utf-8")
    fields = ["T", "YF", "u", "rho", "omega", "p"]
    values = [np.linspace(0, 0.0015, 5001)]
    columns = ["x_m"]
    metrics = {"status": "trained_preprint_subcase_compared", "strict_q1_accepted": False, "paper_metrics_reproduced": False, "date": "2026-11-12", "paper_doi": "10.1016/j.combustflame.2025.113964", "target": "arXiv:2406.09071v1 Section 3.1.1 / Figure 3 first condition; final journal version not checked", "p_atm": 1.0, "Tin_K": 298.0, "phi": 0.4, "source_commit": inputs["commit"], "source_archive_sha256": inputs["source_archive_sha256"], "seed": arguments.seed, "device": "cpu", "dtype": "float64", "network": [1, 64, 64, 64, 1], "warmup_iterations": 1000, "pde_iterations": 30000, "domain_points": 1001, "evaluation_points": 5001, "sampling": "fixed uniform as preprint Table 3; source default Hammersley changed", "reference": inputs["reference"], "fields": {}, "preprint_reported": {"T_relative_L2": 0.0013, "omega_relative_L2": 0.0108, "maximum_sL_absolute_relative_error_across_12_conditions": 0.0003}, "python": platform.python_version(), "environment": {name: importlib.metadata.version(name) for name in ["torch", "numpy", "scipy", "matplotlib", "scikit-learn"]}, "deepxde_version": "1.15.0 (isolated vendor dependencies)", "deviations_and_limits": ["Preprint v1 rather than verified final published article", "Single stated seed, paper seed unspecified", "Reference arrays supplied by author, not independently regenerated", "Fixed uniform sampling matches preprint but differs from pinned code default", "CPU and dependency versions differ", "First training finished; wrapper initially referenced wrong output filenames and failed in summary export. This evaluator reads actual saved upstream arrays without retraining.", "Only one of 12 forward conditions, no inverse case or full-paper validation", "Official annual JCR Q1 evidence pending"], "output_hashes": {}}
    for field in fields:
        names = [field + "_1D_reference.npy", field + "_1D_predicted.npy"]
        truth, predicted = [np.load(output / "data" / name, allow_pickle=False) for name in names]
        if truth.shape != (5001,) or predicted.shape != truth.shape or not np.isfinite(predicted).all():
            raise ValueError("Invalid prediction array: " + field)
        metrics["fields"][field] = {"relative_L2": float(np.linalg.norm(predicted - truth) / np.linalg.norm(truth)), "mae": float(np.mean(np.abs(predicted - truth))), "max_absolute_error": float(np.max(np.abs(predicted - truth)))}
        values += [truth, predicted]
        columns += [field + "_reference", field + "_pinn"]
        metrics["output_hashes"].update({name: hashlib.sha256((output / "data" / name).read_bytes()).hexdigest() for name in names})
    metrics["sL_relative_error_from_upstream_summary"] = float(re.search(r"^relative error:\s+([-+0-9.eE]+)%", text, re.M).group(1)) / 100
    losses = np.loadtxt(output / "losses_history.csv", delimiter=",", skiprows=1)
    metrics["best_saved_epoch"] = int(losses[np.argmin(np.sum(losses[:, 1:], axis=1)), 0])
    metrics["preprint_value_differences"] = {field: metrics["fields"][field]["relative_L2"] - expected for field, expected in [("T", 0.0013), ("omega", 0.0108)]}
    metrics["meets_preprint_broad_single_condition_field_bounds"] = all(metrics["fields"][field]["relative_L2"] < 0.02 for field in ["T", "YF", "u", "rho", "p"]) and metrics["fields"]["omega"]["relative_L2"] < 0.05
    results = HERE / "results" / ("seed" + str(arguments.seed))
    results.mkdir(exist_ok=True)
    np.savetxt(results / "predictions.csv", np.column_stack(values), delimiter=",", header=",".join(columns), comments="")
    for name in ["metrics.txt", "losses_history.csv", "parameters_history.csv"]:
        shutil.copyfile(output / name, results / name)
    metrics["upstream_training_times_s"] = [float(np.loadtxt(path)) for path in sorted(output.glob("training_time_of_stage*.txt"))]
    figure, axes = plt.subplots(1, 2, figsize=(11, 4))
    for axis, field in zip(axes, ["T", "omega"]):
        reference_index = 1 + 2 * fields.index(field)
        axis.plot(values[0] * 1000, values[reference_index], label="Author FDM reference")
        axis.plot(values[0] * 1000, values[reference_index + 1], "--", label="PINN retrained")
        axis.set_xlabel("x / mm")
        axis.set_ylabel("T / K" if field == "T" else "Reaction rate / kg m^-3 s^-1")
        axis.legend()
    figure.tight_layout()
    figure.savefig(results / "comparison.png", dpi=160)
    plt.close(figure)
    (results / "metrics.json").write_text(json.dumps(metrics, indent=2) + "\n", encoding="utf-8")
    (HERE / "results/metrics.json").write_text(json.dumps(metrics, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(metrics, indent=2))


if __name__ == "__main__":
    main()
