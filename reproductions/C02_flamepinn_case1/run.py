import argparse
import ast
import hashlib
import importlib.metadata
import json
import os
import pathlib
import platform
import sys
import time


ROOT = pathlib.Path(__file__).resolve().parents[2]
HERE = pathlib.Path(__file__).resolve().parent
os.environ["DDE_BACKEND"] = "pytorch"
os.environ["MPLBACKEND"] = "Agg"
sys.path.insert(0, str(ROOT / "vendor/flamepinn_dependencies"))
import deepxde as dde
import numpy as np
import torch


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--threads", type=int, default=2)
    parser.add_argument("--iterations", type=int, default=30000)
    arguments = parser.parse_args()
    torch.set_num_threads(arguments.threads)
    torch.set_default_device("cpu")
    dde.config.set_default_float("float64")
    dde.config.set_random_seed(arguments.seed)
    source = HERE / "work/CAME-THU__FlamePINN-1D"
    inputs = json.loads((HERE / "results/inputs.json").read_text(encoding="utf-8"))
    for item in inputs["input_files"]:
        if hashlib.sha256((source / item["path"]).read_bytes()).hexdigest() != item["sha256"]:
            raise ValueError("input changed: " + item["path"])
    entry = source / "freely_prop_simple/src/main_free_simple.py"
    original = entry.read_text(encoding="utf-8")
    tree = ast.parse(original)
    tree.body = [node for node in tree.body if not isinstance(node, ast.If)]
    selected = ast.unparse(tree)
    selected = selected.replace("train_distribution='Hammersley'", "train_distribution='uniform'")
    namespace = {"__name__": "author_forward_case1", "__file__": str(entry)}
    sys.path.insert(0, str(source))
    sys.path.insert(0, str(entry.parent))
    old_directory = pathlib.Path.cwd()
    started = time.perf_counter()
    try:
        os.chdir(entry.parent)
        exec(compile(selected, str(entry), "exec"), namespace)
        config = argparse.Namespace(case_id=1, problem_type="forward", bc_type="soft", oc_type="none", p_in=101325.0, T_in=298.0, phi=0.40, scales={"x": 10 / 0.0015, "T": 1 / 298.0, "sL": 1.0}, shifts={"x": 0.0}, infer_paras={"sL": 0.4}, n_ob=10, noise_level=0.0, observe_u=True, n_iter=arguments.iterations, i_run=1)
        output = pathlib.Path(namespace["main"](config)).resolve()
        metrics = {"status": "author_training_executed_preprint_subcase", "paper_metrics_reproduced": False, "strict_q1_accepted": False, "date": "2026-11-12", "paper_doi": "10.1016/j.combustflame.2025.113964", "reference_version": "arXiv:2406.09071v1, not verified identical to final journal version", "target": "Section 3.1.1, Figure 3, p=1 atm, phi=0.4; Table 3 training protocol", "repository": inputs["repository"], "commit": inputs["commit"], "source_archive_sha256": inputs["source_archive_sha256"], "entry_sha256": hashlib.sha256(original.encode()).hexdigest(), "seed": arguments.seed, "threads": arguments.threads, "device": "cpu", "dtype": "float64", "warmup_iterations": 1000, "pde_iterations": arguments.iterations, "sampling": "uniform (preprint Table 3), fixed 1001 domain points plus boundary samples", "adaptations": ["AST loads upstream imports and main without executing hard-coded CLI overrides", "Set p=1 atm, Tin=298 K, phi=0.4 to match preprint Figure 3 left column", "Change Hammersley sampling in source to uniform sampling specified by preprint Table 3", "Explicit seed and CPU float64; unspecified paper seed", "PyTorch/DeepXDE version and hardware differ from original"], "upstream_output": output.relative_to(HERE).as_posix(), "elapsed_seconds": time.perf_counter() - started, "python": platform.python_version(), "environment": {name: importlib.metadata.version(name) for name in ["torch", "deepxde", "numpy", "scipy", "matplotlib", "scikit-learn"]}}
        reference = source / "freely_prop_simple/ref_solution/results/p1.00_T298_phi0.40/data"
        for field in ["T", "YF", "u", "rho", "omega", "p"]:
            predicted = np.load(output / "data" / (field + "_1D_predicted.npy"), allow_pickle=False)
            truth = np.load(output / "data" / (field + "_1D_reference.npy"), allow_pickle=False)
            metrics.setdefault("fields", {})[field] = {"relative_L2": float(np.linalg.norm(predicted - truth) / np.linalg.norm(truth)), "mae": float(np.mean(np.abs(predicted - truth))), "n_points": len(truth)}
        data = np.loadtxt(output / "parameters_history.csv", delimiter=",", skiprows=1)
        metrics["sL_reference_m_s"] = float(np.load(reference / "sL.npy", allow_pickle=False))
        metrics["parameter_history_last_row"] = data[-1].tolist()
        (HERE / "results/metrics.json").write_text(json.dumps(metrics, indent=2) + "\n", encoding="utf-8")
        print(json.dumps(metrics, indent=2), flush=True)
    finally:
        os.chdir(old_directory)


if __name__ == "__main__":
    main()
