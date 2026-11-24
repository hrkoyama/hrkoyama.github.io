"""Six saved-data-only figures; Matplotlib is not imported by run.py."""
from pathlib import Path
import argparse
import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.ticker import NullLocator


DISPLAY_ERROR_FLOOR = 1e-18


def finish(fig, output, name):
    fig.tight_layout()
    for extension in ("png", "svg", "pdf"):
        fig.savefig(output/(name+"."+extension), dpi=160, bbox_inches="tight")
    plt.close(fig)


def errors(ax, records, title):
    methods = list(dict.fromkeys(r["method_id"] for r in records))
    for method in methods:
        selected = [r for r in records if r["method_id"] == method and r["error_upper"] is not None]
        if not selected:
            continue
        ax.scatter([r["evaluations"] for r in selected],
                   [max(r["error_upper"], DISPLAY_ERROR_FLOOR) for r in selected], label=method, s=24)
        unmet = [r for r in selected if r["accuracy_goal_met"] is False]
        if unmet:
            ax.scatter([r["evaluations"] for r in unmet],
                       [max(r["error_upper"], DISPLAY_ERROR_FLOOR) for r in unmet],
                       marker="x", color="black", s=45)
    ax.set(xscale="log", yscale="log", xlabel="Actual integrand calls",
           ylabel="Analytic absolute-error upper endpoint", title=title)
    ax.grid(alpha=.2)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--results", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    directory = args.results.parent if args.results.is_file() else args.results
    result = json.loads((directory/"result.json").read_text())
    args.output.mkdir(parents=True, exist_ok=True)
    cases = {c["id"]: c for c in result["cases"]}
    rows = cases["quadpack-domain-selection"]["records"]
    fig, axes = plt.subplots(2, 3, figsize=(13, 7))
    for ax, name in zip(axes.flat, dict.fromkeys(r["integrand_id"] for r in rows)):
        errors(ax, [r for r in rows if r["integrand_id"] == name], name)
    axes.flat[-1].axis("off")
    axes.flat[-1].text(.05, .8, "Rows without a numeric return: "+
                       str(sum(r["value"] is None for r in rows))+
                       "\nSee retained singular-node statuses.", va="top")
    axes.flat[0].legend(fontsize=7)
    fig.suptitle("Fixed QUADPACK dispatch and finite Simpson companions; crosses: unmet study goals")
    finish(fig, args.output, "quadpack-domain-selection")
    selected = next(r for r in rows if r["integrand_id"] == "fourier-half-line"
                    and r["method_id"] == "specialized-quadpack")
    cycles = selected["active_partition_or_cycles"]
    fig, axes = plt.subplots(1, 2, figsize=(10, 4))
    axes[0].bar(np.arange(len(cycles["rslst"])), cycles["rslst"])
    axes[0].set(xlabel="Fourier cycle index", ylabel="Saved cycle contribution", title="Actual qawfe active prefix")
    errors(axes[1], [r for r in rows if r["integrand_id"] == "gaussian-whole-line"], "Gaussian: finite vs improper targets")
    axes[1].legend(fontsize=7)
    finish(fig, args.output, "quadpack-domain-selection-preview")
    rows = cases["gk15-double-exponential"]["records"]
    names = list(dict.fromkeys(r["integrand_id"] for r in rows))
    fig, axes = plt.subplots(1, 3, figsize=(13, 4))
    for ax, name in zip(axes, names):
        errors(ax, [r for r in rows if r["integrand_id"] == name], name)
    axes[0].legend(fontsize=7)
    fig.suptitle("G7/K15 and finite-interval tanh-sinh; all fixed rows retained")
    finish(fig, args.output, "gk15-double-exponential")
    fig, axes = plt.subplots(1, 2, figsize=(13, 4.5))
    labels = {"smooth-exponential": "exp(x)",
              "algebraic-inverse-cuberoot": "x^(-1/3)",
              "log-endpoint": "-log(x)"}
    colors = dict(zip(names, ("tab:blue", "tab:orange", "tab:green")))
    for name in names:
        selected = next(r for r in rows if r["integrand_id"] == name
                        and r["method_id"] == "finite-tanh-sinh" and r["step"] == .0625 and r["cutoff"] == 4)
        with np.load(directory/selected["raw_file"]) as raw:
            values = raw["candidate__rows"]
        axes[0].semilogy(values[:, 0], values[:, 2], label=labels[name], color=colors[name])
        family = [r for r in rows if r["integrand_id"] == name and r["method_id"] == "finite-tanh-sinh"]
        axes[1].scatter([r["step"] for r in family],
                        [max(abs(r["signed_finite_window_defect"]), 1e-18) for r in family],
                        color=colors[name], marker="o")
        axes[1].scatter([r["step"] for r in family],
                        [max(abs(r["signed_continuous_tail"]), 1e-18) for r in family],
                        color=colors[name], marker="x")
    axes[0].set(xlabel="Transformed t", ylabel="Saved stable transformed product",
                title="Finite [0,1] tanh-sinh samples")
    axes[1].set(xscale="log", yscale="log", xlabel="Step h",
                ylabel="Absolute saved defect or continuous tail",
                title="Two diagnostics; cutoffs t = 3 and 4")
    axes[1].set_xticks((.0625, .125, .25, .5), ("1/16", "1/8", "1/4", "1/2"))
    axes[1].xaxis.set_minor_locator(NullLocator())
    handles = [Line2D([], [], color=colors[name], lw=2, label=labels[name]) for name in names]
    handles += [Line2D([], [], color="black", marker="o", linestyle="none", label="Finite-window defect"),
                Line2D([], [], color="black", marker="x", linestyle="none", label="Continuous tail")]
    axes[1].legend(handles=handles, fontsize=8, loc="best")
    axes[0].legend(fontsize=8)
    finish(fig, args.output, "gk15-double-exponential-preview")
    rows = cases["tensor-smolyak-dimensions"]["records"]
    fig, axes = plt.subplots(1, 3, figsize=(13, 4))
    for ax, dimension in zip(axes, (2, 3, 4)):
        errors(ax, [r for r in rows if r["dimension"] == dimension], "Dimension "+str(dimension))
    axes[0].legend(fontsize=7)
    fig.suptitle("Tensor and Smolyak controls; unresolved interaction goals remain visible")
    fig.text(.5, -.01, "Log display: max(saved error upper endpoint, 1e-18); stored errors are unchanged.",
             ha="center", fontsize=9)
    finish(fig, args.output, "tensor-smolyak-dimensions")
    fig, axes = plt.subplots(1, 2, figsize=(10, 4))
    for ax, method, level in zip(axes, ("tensor-clenshaw-curtis", "smolyak-delta"), (3, 4)):
        selected = next(r for r in rows if r["dimension"] == 2 and r["integrand_id"] == "smooth-product"
                        and r["method_id"] == method and r["level"] == level)
        with np.load(directory/selected["raw_file"]) as raw:
            x, w = raw["candidate__points"], raw["candidate__weights"]
        picture = ax.scatter(x[:, 0], x[:, 1], c=w, cmap="coolwarm", s=15+250*np.abs(w))
        ax.set(xlabel="x1", ylabel="x2", title=method+" actual 2D nodes", aspect="equal")
        fig.colorbar(picture, ax=ax, label="Signed integration weight")
    finish(fig, args.output, "tensor-smolyak-dimensions-preview")


if __name__ == "__main__":
    main()
