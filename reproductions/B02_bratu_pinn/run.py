import importlib.metadata
import json
import pathlib
import platform
import time

import matplotlib
import numpy as np
import torch
from scipy.optimize import brentq

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def main():
    started = time.perf_counter()
    torch.set_num_threads(1)
    torch.manual_seed(42)
    torch.set_default_dtype(torch.float64)
    output = pathlib.Path(__file__).parent / "results"
    output.mkdir(exist_ok=True)
    model = torch.nn.Sequential(torch.nn.Linear(1, 24), torch.nn.Tanh(), torch.nn.Linear(24, 24), torch.nn.Tanh(), torch.nn.Linear(24, 1))
    points = torch.linspace(0.0, 1.0, 100).reshape(-1, 1).requires_grad_(True)

    def prediction(coordinates):
        return coordinates * (1.0 - coordinates) * model(coordinates)

    def loss():
        values = prediction(points)
        first = torch.autograd.grad(values, points, torch.ones_like(values), create_graph=True)[0]
        second = torch.autograd.grad(first, points, torch.ones_like(first), create_graph=True)[0]
        return ((second + torch.exp(values)) ** 2).mean()

    optimizer = torch.optim.Adam(model.parameters(), lr=0.003)
    history = []
    for epoch in range(1500):
        optimizer.zero_grad()
        objective = loss()
        objective.backward()
        optimizer.step()
        if epoch % 100 == 0:
            history.append({"epoch": epoch, "residual_mse": float(objective.detach())})
    optimizer = torch.optim.LBFGS(model.parameters(), max_iter=300, tolerance_grad=1e-12, tolerance_change=1e-14, line_search_fn="strong_wolfe")

    def closure():
        optimizer.zero_grad()
        objective = loss()
        objective.backward()
        return objective

    optimizer.step(closure)
    coordinates = np.linspace(0.0, 1.0, 501)
    theta = brentq(lambda value: 2.0 * value ** 2 / np.cosh(value / 2.0) ** 2 - 1.0, 0.01, 2.0)
    exact = -2.0 * np.log(np.cosh(theta * (coordinates - 0.5)) / np.cosh(theta / 2.0))
    values = prediction(torch.tensor(coordinates.reshape(-1, 1))).detach().numpy().ravel()
    report = {"status": "executed_independent_equation_benchmark", "paper_result_reproduced": False, "equation": "u_xx + exp(u) = 0; x in [0,1]; u(0)=u(1)=0", "branch": "lower branch, theta in (0.01,2)", "lambda": 1.0, "theta": theta, "network": [1, 24, 24, 1], "activation": "tanh", "hard_boundary_transform": "x*(1-x)*NN(x)", "training_points": 100, "test_points": 501, "adam_steps": 1500, "lbfgs_max_iterations": 300, "seed": 42, "max_absolute_error": float(np.max(np.abs(values - exact))), "relative_L2_error": float(np.linalg.norm(values - exact) / np.linalg.norm(exact)), "residual_mse_training_points": float(loss().detach()), "boundary_max_absolute_error": float(max(abs(values[0]), abs(values[-1]))), "elapsed_seconds": time.perf_counter() - started, "python": platform.python_version(), "environment": {package: importlib.metadata.version(package) for package in ["torch", "numpy", "scipy", "matplotlib"]}}
    np.savetxt(output / "solution.csv", np.column_stack([coordinates, exact, values]), delimiter=",", header="x,analytical,pinn", comments="")
    (output / "metrics.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    (output / "training_history.json").write_text(json.dumps(history, indent=2), encoding="utf-8")
    figure, axis = plt.subplots(figsize=(6, 4))
    axis.plot(coordinates, exact, label="Analytical lower branch")
    axis.plot(coordinates[::10], values[::10], ".", label="PINN")
    axis.set(xlabel="x", ylabel="u(x)")
    axis.legend()
    figure.tight_layout()
    figure.savefig(output / "solution.png", dpi=180)
    plt.close(figure)
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
