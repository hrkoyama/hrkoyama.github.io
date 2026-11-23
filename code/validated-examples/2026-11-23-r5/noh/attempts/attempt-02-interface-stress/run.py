#!/usr/bin/env python3
"""Run the predeclared cold Noh cases, retaining failures and frozen gates."""
import argparse
import csv
import datetime
import hashlib
import json
import math
import platform
import sys
import time
from pathlib import Path

import numpy as np

import noh_reference as reference
import noh_solver as solver


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def relative_norms(error, exact, volume, mask=None):
    if mask is None:
        mask = np.ones(len(volume), dtype=bool)
    if not np.any(mask):
        return {"l1": None, "l2": None, "linf": None, "cells": 0}
    w, e, ref = volume[mask], error[mask], exact[mask]
    tiny = np.finfo(float).tiny
    return {
        "l1": float(np.sum(w * abs(e)) / max(np.sum(w * abs(ref)), tiny)),
        "l2": float(np.sqrt(np.sum(w * e**2) / max(np.sum(w * ref**2), tiny))),
        "linf": float(np.max(abs(e)) / max(np.max(abs(ref)), tiny)),
        "cells": int(np.count_nonzero(mask)),
    }


def save_run(config, geometry, n, output):
    dimension = {"planar": 1, "cylindrical": 2, "spherical": 3}[geometry]
    gamma, rho0, u0 = (config[k] for k in ("gamma", "rho0", "u0"))
    start = time.perf_counter()
    result = solver.solve(n, dimension, config["final_time"], config["r_max"],
                          gamma, rho0, u0, config["cfl"])
    elapsed = time.perf_counter() - start
    q, edges, volume = result["q"], result["edges"], result["volume"]
    centers = 0.5 * (edges[:-1] + edges[1:])
    density, velocity, pressure, sie, _ = solver.primitive(q, gamma)
    exact_q, exact_pressure_average = reference.cell_averages(
        edges, result["time"], dimension, gamma, rho0, u0)
    exact_density, exact_velocity, exact_pressure, exact_sie, _ = solver.primitive(exact_q, gamma)
    parameters = reference.parameters(dimension, gamma, rho0, u0)
    dx = config["r_max"] / n
    shock = parameters["shock_speed"] * result["time"]
    center = edges[1:] <= 0.25 * shock
    shock_mask = (edges[:-1] <= shock + 3 * dx) & (edges[1:] >= shock - 3 * dx)
    plateau = (edges[:-1] >= 0.25 * shock) & (edges[1:] <= 0.70 * shock)
    smooth = ~center & ~shock_mask
    threshold = 0.5 * parameters["pressure_post"]
    crossings = np.flatnonzero((pressure[:-1] >= threshold) & (pressure[1:] < threshold))
    shock_measured = None
    if len(crossings):
        i = int(crossings[-1])
        fraction = (pressure[i] - threshold) / (pressure[i] - pressure[i + 1])
        shock_measured = float(centers[i] + fraction * (centers[i + 1] - centers[i]))
    weighted_mean = lambda data, mask: float(np.sum(data[mask] * volume[mask]) / np.sum(volume[mask]))
    plateau_density = weighted_mean(density, plateau)
    plateau_pressure = weighted_mean(pressure, plateau)
    initial, final = result["initial_integral"], result["final_integral"]
    balance = final - initial - result["boundary_net_integral"] - result["source_integral"]
    exact_mass, exact_energy = reference.exact_integrals(config["r_max"], result["time"], dimension, rho0, u0)
    full = relative_norms(density - exact_density, exact_density, volume)
    numerical_conservation_scale = np.maximum(abs(final), np.finfo(float).tiny)
    center_max_sie = float(np.max(sie[center]))
    metrics = {
        "density_l1": full["l1"], "density_l2": full["l2"], "density_linf": full["linf"],
        "density_errors": {"full": full,
                           "outside_center_and_shock": relative_norms(density - exact_density, exact_density, volume, smooth),
                           "center": relative_norms(density - exact_density, exact_density, volume, center),
                           "shock_band": relative_norms(density - exact_density, exact_density, volume, shock_mask)},
        "shock_exact": shock, "shock_measured_pressure_half_height": shock_measured,
        "shock_error": None if shock_measured is None else abs(shock_measured - shock),
        "shock_error_in_dx": None if shock_measured is None else abs(shock_measured - shock) / dx,
        "plateau_density": plateau_density, "plateau_density_exact": parameters["rho_post"],
        "plateau_density_amplification": plateau_density / rho0,
        "plateau_density_relative_error": abs(plateau_density / parameters["rho_post"] - 1),
        "plateau_pressure": plateau_pressure, "plateau_pressure_exact": parameters["pressure_post"],
        "plateau_pressure_relative_error": abs(plateau_pressure / parameters["pressure_post"] - 1),
        "shock_jump_exact": parameters["shock_density_jump"],
        "initial_density_amplification_exact": parameters["initial_density_amplification"],
        "shock_jump_using_plateau_and_exact_upstream": plateau_density / (rho0 * parameters["shock_density_jump"]**(dimension - 1)),
        "center_max_specific_internal_energy": center_max_sie,
        "center_max_sie_relative_excess": center_max_sie / parameters["specific_internal_energy_post"] - 1,
        "center_min_density": float(np.min(density[center])),
        "center_min_density_ratio": float(np.min(density[center])) / parameters["rho_post"],
        "center_max_pressure": float(np.max(pressure[center])),
        "center_first_cell": {"rho": float(density[0]), "pressure": float(pressure[0]), "specific_internal_energy": float(sie[0])},
        "initial_integral": initial.tolist(), "final_integral": final.tolist(),
        "boundary_net_integral": result["boundary_net_integral"].tolist(),
        "geometric_source_integral": result["source_integral"].tolist(),
        "conservation_residual": balance.tolist(),
        "mass_balance_relative": abs(float(balance[0])) / numerical_conservation_scale[0],
        "energy_balance_relative": abs(float(balance[2])) / numerical_conservation_scale[2],
        "radial_momentum_balance_absolute": abs(float(balance[1])),
        "analytic_total_mass": exact_mass, "analytic_total_energy": exact_energy,
        "mass_vs_analytic_relative": abs(float(final[0]) / exact_mass - 1),
        "energy_vs_analytic_relative": abs(float(final[2]) / exact_energy - 1),
        "min_pressure_all_stages": result["min_pressure"],
        "min_density_all_stages": result["min_density"],
        "min_internal_energy_roundoff_units": result["min_internal_energy_roundoff_units"],
        "negative_pressure_evaluations": result["negative_pressure_evaluations"],
        "state_floor_corrections": result["state_floor_corrections"],
    }
    relative_profile = "profiles/{}-n{}.csv".format(geometry, n)
    profile = output / relative_profile
    profile.parent.mkdir(parents=True, exist_ok=True)
    columns = ["r_left", "r_right", "r_center", "volume", "rho", "momentum", "total_energy",
               "velocity", "pressure", "specific_internal_energy", "exact_rho", "exact_momentum",
               "exact_total_energy", "exact_velocity", "exact_pressure", "exact_specific_internal_energy",
               "exact_pressure_average", "mask_center", "mask_shock", "mask_plateau"]
    data = np.column_stack((edges[:-1], edges[1:], centers, volume, q,
                            velocity, pressure, sie, exact_q, exact_velocity, exact_pressure,
                            exact_sie, exact_pressure_average, center, shock_mask, plateau))
    with profile.open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(columns)
        writer.writerows(data)
    history_path = "histories/{}-n{}.json".format(geometry, n)
    (output / "histories").mkdir(exist_ok=True)
    (output / history_path).write_text(json.dumps(result["history"], indent=2) + "\n")
    return {"geometry": geometry, "dimension": dimension, "n": n,
            "time": result["time"], "status": "completed", "steps": result["steps"],
            "elapsed_seconds": elapsed, "minimum_dt": result["minimum_dt"], "maximum_dt": result["maximum_dt"],
            "profile": relative_profile, "profile_sha256": digest(profile),
            "history": history_path, "history_sha256": digest(output / history_path), "metrics": metrics}


def checks_for_runs(runs, convergence, acceptance, config):
    a = acceptance["checks"]
    completed = [r for r in runs if r["status"] == "completed"]
    checks = []
    def add(name, passed, value=None, bound=None):
        checks.append({"name": name, "passed": bool(passed), "value": value, "bound": bound})
    add("all_runs_reach_final_time", len(completed) == len(config["geometries"]) * len(config["grids"])
        and all(r["time"] == config["final_time"] for r in completed))
    for run in completed:
        m, label = run["metrics"], "{}-n{}".format(run["geometry"], run["n"])
        add(label + ": finite positive density", m["min_density_all_stages"] > 0, m["min_density_all_stages"], 0)
        add(label + ": pressure within roundoff", m["min_internal_energy_roundoff_units"] >= a["pressure_lower_bound_in_energy_roundoff_units"], m["min_internal_energy_roundoff_units"], a["pressure_lower_bound_in_energy_roundoff_units"])
        add(label + ": no state floors", m["state_floor_corrections"] == 0, m["state_floor_corrections"], 0)
        for name, key in [("mass_balance_relative", "conservation_mass_relative_max"), ("energy_balance_relative", "conservation_energy_relative_max")]:
            add(label + ": " + name, m[name] <= a[key], m[name], a[key])
    for geometry in config["geometries"]:
        rows = sorted([r for r in completed if r["geometry"] == geometry], key=lambda r: r["n"])
        if len(rows) != len(config["grids"]):
            add(geometry + ": complete refinement series", False)
            continue
        finest = rows[-1]["metrics"]
        for metric, key in [("density_l1", "density_l1_finest_max"),
                            ("shock_error_in_dx", "shock_position_error_finest_in_dx_max"),
                            ("plateau_density_relative_error", "plateau_density_amplification_relative_error_finest_max"),
                            ("plateau_pressure_relative_error", "plateau_pressure_relative_error_finest_max"),
                            ("mass_vs_analytic_relative", "mass_boundary_quadrature_error_finest_max"),
                            ("energy_vs_analytic_relative", "energy_boundary_quadrature_error_finest_max")]:
            add(geometry + ": finest " + metric, finest[metric] is not None and finest[metric] <= a[key], finest[metric], a[key])
        errors = [r["metrics"]["density_l1"] for r in rows]
        add(geometry + ": density L1 decreases", all(x > y for x, y in zip(errors[:-1], errors[1:])), errors)
        order = convergence[geometry][-1]["density_l1_order"]
        add(geometry + ": last-pair L1 order", order >= a["density_l1_last_pair_order_min"], order, a["density_l1_last_pair_order_min"])
        add(geometry + ": unmasked center heating reported", all("center_first_cell" in r["metrics"] for r in rows))
    return checks


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", default="inputs.json")
    parser.add_argument("--acceptance", default="acceptance.json")
    parser.add_argument("--output", default="results")
    args = parser.parse_args()
    output = Path(args.output)
    if (output / "results.json").exists():
        raise SystemExit("Refusing to overwrite retained results; choose a new --output")
    output.mkdir(parents=True, exist_ok=True)
    config, acceptance = json.loads(Path(args.input).read_text()), json.loads(Path(args.acceptance).read_text())
    if config["p0"] != 0 or config["state_floor"] is not None:
        raise SystemExit("This release implements the true cold state only, without floors")
    source_dir = Path(__file__).resolve().parent
    manifest_paths = [source_dir / name for name in ("run.py", "noh_solver.py", "noh_reference.py", "requirements.txt")]
    document = {"schema_version": 1, "case_id": config["case_id"],
                "started_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
                "metadata": config,
                "environment": {"python": sys.version, "numpy": np.__version__, "platform": platform.platform()},
                "receipts": {"input_sha256": digest(args.input), "acceptance_sha256": digest(args.acceptance),
                             "source_sha256": {p.name: digest(p) for p in manifest_paths}},
                "reference_cell_average_policy": "exact_* conserved columns are volume averages; exact primitive columns use p/velocity evaluated on those conservative averages. exact_pressure_average is the separately averaged physical pressure.",
                "runs": [], "convergence": {}, "checks": []}
    for geometry in config["geometries"]:
        for n in config["grids"]:
            try:
                run = save_run(config, geometry, n, output)
                print(geometry, n, json.dumps(run["metrics"], sort_keys=True), flush=True)
            except Exception as error:
                run = {"geometry": geometry, "n": n, "status": "failed", "error_type": type(error).__name__, "error": str(error)}
                print(json.dumps(run), flush=True)
            document["runs"].append(run)
            # Partial progress survives interruption or a later failed case.
            (output / "results.partial.json").write_text(json.dumps(document, indent=2) + "\n")
    for geometry in config["geometries"]:
        rows = []
        for run in sorted((r for r in document["runs"] if r["geometry"] == geometry and r["status"] == "completed"), key=lambda r: r["n"]):
            row = {"n": run["n"], **{k: run["metrics"][k] for k in ("density_l1", "density_l2", "density_linf", "shock_error", "center_max_sie_relative_excess")}}
            row["density_l1_order"] = None if not rows else math.log(rows[-1]["density_l1"] / row["density_l1"]) / math.log(row["n"] / rows[-1]["n"])
            rows.append(row)
        document["convergence"][geometry] = rows
    document["checks"] = checks_for_runs(document["runs"], document["convergence"], acceptance, config)
    document["passed"] = bool(document["checks"]) and all(c["passed"] for c in document["checks"])
    document["completed_at_utc"] = datetime.datetime.now(datetime.timezone.utc).isoformat()
    (output / "results.json").write_text(json.dumps(document, indent=2, allow_nan=False) + "\n")
    print(json.dumps({"passed": document["passed"], "checks": len(document["checks"]), "failed": [c for c in document["checks"] if not c["passed"]]}, indent=2), flush=True)
    return 0 if document["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
