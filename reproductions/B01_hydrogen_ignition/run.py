import argparse
import csv
import hashlib
import importlib.metadata
import json
import pathlib
import platform
import time

import cantera as ct
import matplotlib
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.neural_network import MLPRegressor
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def ignition(temperature, pressure_atm, equivalence_ratio):
    gas = ct.Solution("h2o2.yaml")
    gas.TP = temperature, pressure_atm * ct.one_atm
    gas.set_equivalence_ratio(equivalence_ratio, "H2", "O2:1,N2:3.76")
    reactor = ct.IdealGasReactor(gas, clone=True)
    network = ct.ReactorNet([reactor])
    network.rtol = 1e-9
    network.atol = 1e-15
    previous_time = 0.0
    previous_temperature = temperature
    threshold = temperature + 400.0
    while network.time < 0.2:
        network.step()
        if reactor.T >= threshold:
            fraction = (threshold - previous_temperature) / (reactor.T - previous_temperature)
            return previous_time + fraction * (network.time - previous_time)
        previous_time = network.time
        previous_temperature = reactor.T
    return None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default=str(pathlib.Path(__file__).parent / "results"))
    arguments = parser.parse_args()
    output = pathlib.Path(arguments.output)
    output.mkdir(parents=True, exist_ok=True)
    started = time.perf_counter()
    rows = []
    for temperature in [950.0, 1000.0, 1050.0, 1100.0, 1150.0, 1200.0, 1250.0, 1300.0]:
        for pressure in [1.0, 3.0, 5.0]:
            for ratio in [0.5, 0.75, 1.0, 1.25, 1.5]:
                delay = ignition(temperature, pressure, ratio)
                split = "test" if temperature in [1050.0, 1200.0] else "train"
                rows.append({"T0_K": temperature, "p0_atm": pressure, "phi": ratio, "tau_s": delay, "split": split, "status": "ignited" if delay is not None else "right_censored_0.2s"})
    with (output / "dataset.csv").open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    valid = [row for row in rows if row["tau_s"] is not None]
    features = np.array([[1000.0 / row["T0_K"], np.log(row["p0_atm"]), row["phi"]] for row in valid])
    targets = np.log10([row["tau_s"] for row in valid])
    test_mask = np.array([row["split"] == "test" for row in valid])
    report = {"status": "executed_independent_baseline", "paper_result_reproduced": False, "date": "2026-11-11", "mechanism": "Cantera bundled h2o2.yaml", "reactor": "closed, adiabatic, constant volume ideal gas", "ignition_definition": "first T=T0+400 K crossing, linear interpolation between accepted solver steps", "censoring_horizon_s": 0.2, "split": "hold out all cases at T0=1050 K and 1200 K; no trajectory or row leakage", "n_total": len(rows), "n_valid": len(valid), "n_censored": len(rows) - len(valid), "n_train": int((~test_mask).sum()), "n_test": int(test_mask.sum()), "models": {}, "environment": {package: importlib.metadata.version(package) for package in ["cantera", "numpy", "scipy", "scikit-learn", "matplotlib"]}, "python": platform.python_version()}
    predictions = []
    figure, axes = plt.subplots(1, 2, figsize=(10, 4))
    for axis, (name, model) in zip(axes, [("MLP", make_pipeline(StandardScaler(), MLPRegressor(hidden_layer_sizes=(32, 32), activation="tanh", solver="lbfgs", max_iter=3000, random_state=42, alpha=1e-3))), ("RandomForest", RandomForestRegressor(n_estimators=200, random_state=42, n_jobs=1))]):
        model.fit(features[~test_mask], targets[~test_mask])
        predicted = model.predict(features[test_mask])
        report["models"][name] = {"log10_MAE": float(mean_absolute_error(targets[test_mask], predicted)), "log10_R2": float(r2_score(targets[test_mask], predicted)), "median_relative_error": float(np.median(np.abs(10.0 ** (predicted - targets[test_mask]) - 1.0)))}
        for row, actual, prediction in zip([row for row in valid if row["split"] == "test"], targets[test_mask], predicted):
            predictions.append({"model": name, "T0_K": row["T0_K"], "p0_atm": row["p0_atm"], "phi": row["phi"], "reference_tau_s": 10.0 ** actual, "predicted_tau_s": 10.0 ** prediction})
        axis.scatter(targets[test_mask], predicted, s=20)
        bounds = [min(targets[test_mask].min(), predicted.min()), max(targets[test_mask].max(), predicted.max())]
        axis.plot(bounds, bounds, "k--")
        axis.set(xlabel="Reference log10(tau / s)", ylabel="Predicted log10(tau / s)", title=name)
    figure.tight_layout()
    figure.savefig(output / "parity.png", dpi=180)
    plt.close(figure)
    with (output / "predictions.csv").open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(predictions[0]))
        writer.writeheader()
        writer.writerows(predictions)
    mechanism_file = next(pathlib.Path(directory) / "h2o2.yaml" for directory in ct.get_data_directories() if (pathlib.Path(directory) / "h2o2.yaml").exists())
    report["mechanism_sha256"] = hashlib.sha256(mechanism_file.read_bytes()).hexdigest()
    report["dataset_sha256"] = hashlib.sha256((output / "dataset.csv").read_bytes()).hexdigest()
    report["elapsed_seconds"] = time.perf_counter() - started
    (output / "metrics.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
