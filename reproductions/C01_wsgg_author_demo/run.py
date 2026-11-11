import hashlib
import importlib.metadata
import json
import os
import pathlib
import platform
import runpy
import shutil
import sys
import tarfile
import time

import matplotlib
import numpy as np
import torch


matplotlib.use("Agg")
ROOT = pathlib.Path(__file__).resolve().parents[2]
OUTPUT = pathlib.Path(__file__).parent / "results"
PACKAGE = ROOT / "code_packages/TaoRen-Rad__WSGG-H2O-CO2-NH3"


def main():
    started = time.perf_counter()
    archive = json.loads((PACKAGE / "archive.json").read_text(encoding="utf-8"))
    source = ROOT / archive["path"]
    if hashlib.sha256(source.read_bytes()).hexdigest() != archive["sha256"]:
        raise ValueError("source archive SHA-256 mismatch")
    directory = ROOT / "vendor/WSGG-H2O-CO2-NH3" / archive["commit"]
    directory.mkdir(parents=True, exist_ok=True)
    with tarfile.open(source) as bundle:
        members = bundle.getmembers()
        if sum(member.size for member in members) > 10 * 1024 * 1024:
            raise ValueError("unexpected extracted archive size")
        for member in members:
            resolved = (directory / member.name).resolve()
            if not resolved.is_relative_to(directory.resolve()) or member.issym() or member.islnk():
                raise ValueError("unsafe archive member")
        bundle.extractall(directory, filter="data")
        top = pathlib.PurePosixPath(members[0].name).parts[0]
    upstream = directory / top
    sys.path.insert(0, str(upstream))
    from PINN_WSGG import plot_setup
    from PINN_WSGG.nn_wsgg import load_wsgg, nn_wsgg_rte

    original_setup = plot_setup.setup

    def portable_setup():
        original_setup()
        matplotlib.rcParams["text.usetex"] = False

    plot_setup.setup = portable_setup
    original_directory = pathlib.Path.cwd()
    torch.set_num_threads(1)
    try:
        os.chdir(upstream)
        with torch.no_grad():
            runpy.run_path(str(upstream / "test.py"), run_name="__main__")
        profiles = np.load(upstream / "data/profiles.npy", allow_pickle=False)
        references = np.load(upstream / "data/results.npy", allow_pickle=False)
        values = torch.tensor(profiles, dtype=torch.float32)
        model = load_wsgg(torch.float32).eval()
        with torch.no_grad():
            incident, heat_flux, divergence = nn_wsgg_rte(model, values[:, 0], values[:, 4], values[:, 1], values[:, 2], values[:, 3], torch.tensor(300.0), torch.tensor(300.0))
        prediction = divergence.numpy().ravel()
        reference = references[:, -1]
        if not np.isfinite(prediction).all() or not np.isfinite(reference).all():
            raise ValueError("nonfinite radiation source")
        scale = float(np.ptp(reference))
        if scale <= 0:
            raise ValueError("zero reference range")
        metrics = {"status": "author_demo_executed", "paper_metrics_reproduced": False, "repository": archive["repository"], "commit": archive["commit"], "source_archive_sha256": archive["sha256"], "date": "2026-11-11", "command": "python reproductions/C01_wsgg_author_demo/run.py", "upstream_entry": "test.py", "adaptations": ["Agg plotting backend", "text.usetex=False to avoid external LaTeX; numerical model and data unchanged", "torch CPU threads=1", "additional evaluation pass using same upstream functions"], "n_points": len(prediction), "reference": "upstream data/results.npy last column, README labels LBL; LBL not independently recomputed", "reference_range_W_m3": scale, "mean_absolute_error_W_m3": float(np.mean(np.abs(prediction - reference))), "mae_divided_by_reference_range": float(np.mean(np.abs(prediction - reference)) / scale), "relative_L2_error": float(np.linalg.norm(prediction - reference) / np.linalg.norm(reference)), "max_absolute_error_W_m3": float(np.max(np.abs(prediction - reference))), "python": platform.python_version(), "environment": {name: importlib.metadata.version(name) for name in ["torch", "numpy", "scipy", "matplotlib", "tqdm"]}, "input_hashes": {name: hashlib.sha256((upstream / name).read_bytes()).hexdigest() for name in ["data/profiles.npy", "data/results.npy", "PINN_WSGG/data/wsgg.json"]}, "elapsed_seconds": time.perf_counter() - started}
        OUTPUT.mkdir(parents=True, exist_ok=True)
        np.savetxt(OUTPUT / "predictions.csv", np.column_stack([profiles[:, 0], reference, prediction, heat_flux.numpy(), incident.numpy()]), delimiter=",", header="x_m,LBL_divergence_W_m3,PINN_WSGG_divergence_W_m3,heat_flux_W_m2,incident_radiation_W_m2", comments="")
        shutil.copyfile(upstream / "test_case.png", OUTPUT / "test_case.png")
        (OUTPUT / "metrics.json").write_text(json.dumps(metrics, ensure_ascii=False, indent=2), encoding="utf-8")
        print(json.dumps(metrics, ensure_ascii=False, indent=2))
    finally:
        os.chdir(original_directory)


if __name__ == "__main__":
    main()
