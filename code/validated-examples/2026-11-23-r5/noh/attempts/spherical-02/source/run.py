#!/usr/bin/env python3
"""Run the predeclared cold Noh cases, retaining failures and frozen gates."""
import argparse
import csv
import datetime
import hashlib
import json
import math
import platform
import re
import sys
import time
from pathlib import Path

import numpy as np

import noh_reference as reference
import noh_solver as solver


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def spherical_contract_path(source_dir, filename):
    """Resolve only the local, explicitly named spherical pre-run contract."""
    if not isinstance(filename, str) or not re.fullmatch(
            r"pre-run-contract-spherical(?:-revision[0-9]{2})?\.json", filename):
        raise ValueError("Expected a safe local spherical pre-run contract filename")
    path = Path(source_dir) / filename
    if path.is_symlink():
        raise ValueError("The spherical pre-run contract must not be a symlink")
    return path


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


def spherical_boundary_bias(dt_cubed_sum, rho0=1.0, u0=-1.0):
    """SSPRK2 trapezoidal bias for the cold d=3 boundary inflow.

    The mass influx is rho0*v*(R+v*t)^2, v=|u0|. Its trapezoidal
    excess is rho0*v^3*sum(dt^3)/6, with energy excess v^2/2 times that.
    These are diagnostics; neither the state nor its boundary flux is fixed.
    """
    mass_bias = rho0 * (-u0)**3 * dt_cubed_sum / 6.0
    return mass_bias, 0.5 * u0**2 * mass_bias


def save_run(config, geometry, n, output, maximum_seconds=60.0):
    dimension = {"planar": 1, "cylindrical": 2, "spherical": 3}[geometry]
    gamma, rho0, u0 = (config[k] for k in ("gamma", "rho0", "u0"))
    stress_quadrature = config.get("stress_quadrature_by_geometry", {}).get(
        geometry, config.get("stress_quadrature", "arithmetic-face"))
    start = time.perf_counter()
    result = solver.solve(n, dimension, config["final_time"], config["r_max"],
                          gamma, rho0, u0, config["cfl"], maximum_seconds=maximum_seconds,
                          stress_quadrature=stress_quadrature)
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
    core = edges[1:] <= 0.70 * shock
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
    momentum_scale = max(float(abs(initial[1]) + abs(final[1])
                               + abs(result["boundary_net_integral"][1])
                               + abs(result["source_integral"][1])), np.finfo(float).tiny)
    mass_difference = float(final[0]) - exact_mass
    energy_difference = float(final[2]) - exact_energy
    mass_bias, energy_bias = (spherical_boundary_bias(result["dt_cubed_sum"], rho0, u0)
                              if dimension == 3 else (0.0, 0.0))
    core_errors = relative_norms(density - exact_density, exact_density, volume, core)
    center_first_cell = {
        "rho": float(density[0]), "pressure": float(pressure[0]),
        "specific_internal_energy": float(sie[0]),
        "rho_exact": parameters["rho_post"], "pressure_exact": parameters["pressure_post"],
        "specific_internal_energy_exact": parameters["specific_internal_energy_post"],
        "rho_ratio": float(density[0]) / parameters["rho_post"],
        "pressure_ratio": float(pressure[0]) / parameters["pressure_post"],
        "specific_internal_energy_ratio": float(sie[0]) / parameters["specific_internal_energy_post"],
    }
    metrics = {
        "density_l1": full["l1"], "density_l2": full["l2"], "density_linf": full["linf"],
        "density_errors": {"full": full,
                           "outside_center_and_shock": relative_norms(density - exact_density, exact_density, volume, smooth),
                           "center": relative_norms(density - exact_density, exact_density, volume, center),
                           "shock_band": relative_norms(density - exact_density, exact_density, volume, shock_mask)},
        "core_density_l1": core_errors["l1"], "core_density_errors": core_errors,
        "core_mask": "r_right <= 0.70*r_shock, origin included",
        "shock_exact": shock, "shock_measured_pressure_half_height": shock_measured,
        "shock_error": None if shock_measured is None else abs(shock_measured - shock),
        "shock_error_in_dx": None if shock_measured is None else abs(shock_measured - shock) / dx,
        "shock_position_signed_error": None if shock_measured is None else shock_measured - shock,
        "plateau_density": plateau_density, "plateau_density_exact": parameters["rho_post"],
        "plateau_density_amplification": plateau_density / rho0,
        "plateau_density_relative_error": abs(plateau_density / parameters["rho_post"] - 1),
        "plateau_density_signed_relative_error": plateau_density / parameters["rho_post"] - 1,
        "plateau_pressure": plateau_pressure, "plateau_pressure_exact": parameters["pressure_post"],
        "plateau_pressure_relative_error": abs(plateau_pressure / parameters["pressure_post"] - 1),
        "plateau_pressure_signed_relative_error": plateau_pressure / parameters["pressure_post"] - 1,
        "shock_jump_exact": parameters["shock_density_jump"],
        "initial_density_amplification_exact": parameters["initial_density_amplification"],
        "shock_jump_using_plateau_and_exact_upstream": plateau_density / (rho0 * parameters["shock_density_jump"]**(dimension - 1)),
        "center_max_specific_internal_energy": center_max_sie,
        "center_max_sie_relative_excess": center_max_sie / parameters["specific_internal_energy_post"] - 1,
        "center_max_specific_internal_energy_ratio": center_max_sie / parameters["specific_internal_energy_post"],
        "center_min_density": float(np.min(density[center])),
        "center_min_density_ratio": float(np.min(density[center])) / parameters["rho_post"],
        "center_max_pressure": float(np.max(pressure[center])),
        "center_max_pressure_ratio": float(np.max(pressure[center])) / parameters["pressure_post"],
        "center_first_cell": center_first_cell,
        "initial_integral": initial.tolist(), "final_integral": final.tolist(),
        "boundary_net_integral": result["boundary_net_integral"].tolist(),
        "geometric_source_integral": result["source_integral"].tolist(),
        "conservation_residual": balance.tolist(),
        "mass_balance_relative": abs(float(balance[0])) / numerical_conservation_scale[0],
        "mass_balance_signed": float(balance[0]),
        "mass_balance_signed_relative": float(balance[0]) / numerical_conservation_scale[0],
        "energy_balance_relative": abs(float(balance[2])) / numerical_conservation_scale[2],
        "energy_balance_signed": float(balance[2]),
        "energy_balance_signed_relative": float(balance[2]) / numerical_conservation_scale[2],
        "radial_momentum_balance_absolute": abs(float(balance[1])),
        "radial_momentum_balance_signed": float(balance[1]),
        "radial_momentum_balance_scale": momentum_scale,
        "radial_momentum_balance_relative": abs(float(balance[1])) / momentum_scale,
        "radial_momentum_balance_signed_relative": float(balance[1]) / momentum_scale,
        "analytic_total_mass": exact_mass, "analytic_total_energy": exact_energy,
        "mass_vs_analytic_relative": abs(float(final[0]) / exact_mass - 1),
        "energy_vs_analytic_relative": abs(float(final[2]) / exact_energy - 1),
        "mass_vs_analytic_signed": mass_difference,
        "energy_vs_analytic_signed": energy_difference,
        "mass_vs_analytic_signed_relative": mass_difference / exact_mass,
        "energy_vs_analytic_signed_relative": energy_difference / exact_energy,
        "dt_cubed_sum": result["dt_cubed_sum"],
        "mass_temporal_bias_expected": mass_bias,
        "energy_temporal_bias_expected": energy_bias,
        "mass_temporal_bias_residual_signed": mass_difference - mass_bias,
        "energy_temporal_bias_residual_signed": energy_difference - energy_bias,
        "mass_temporal_bias_residual_relative": abs(mass_difference - mass_bias) / exact_mass,
        "energy_temporal_bias_residual_relative": abs(energy_difference - energy_bias) / exact_energy,
        "mass_temporal_bias_residual_signed_relative": (mass_difference - mass_bias) / exact_mass,
        "energy_temporal_bias_residual_signed_relative": (energy_difference - energy_bias) / exact_energy,
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
    if geometry == "spherical":
        columns.append("mask_core")
        data = np.column_stack((data, core))
    with profile.open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(columns)
        writer.writerows(data)
    history_path = "histories/{}-n{}.json".format(geometry, n)
    (output / "histories").mkdir(exist_ok=True)
    (output / history_path).write_text(json.dumps(result["history"], indent=2) + "\n")
    return {"geometry": geometry, "dimension": dimension, "n": n,
            "stress_quadrature": result["stress_quadrature"],
            "time": result["time"], "status": "completed", "steps": result["steps"],
            "elapsed_seconds": elapsed, "minimum_dt": result["minimum_dt"], "maximum_dt": result["maximum_dt"],
            "profile": relative_profile, "profile_sha256": digest(profile),
            "history": history_path, "history_sha256": digest(output / history_path), "metrics": metrics}


def checks_for_runs(runs, convergence, acceptance, config, spherical_acceptance=None):
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
    if "spherical" in config["geometries"]:
        if spherical_acceptance is None:
            raise ValueError("Spherical executions require the separately frozen spherical acceptance")
        gates = spherical_acceptance["checks"]
        sphere_runs = sorted([r for r in completed if r["geometry"] == "spherical"], key=lambda r: r["n"])
        for run in sphere_runs:
            m, label = run["metrics"], "spherical-n{}".format(run["n"])
            for name, metric, bound_key in [
                ("radial momentum balance relative", "radial_momentum_balance_relative", "radial_momentum_balance_relative_max"),
                ("mass temporal bias identity relative", "mass_temporal_bias_residual_relative", "mass_temporal_bias_identity_relative_max"),
                ("energy temporal bias identity relative", "energy_temporal_bias_residual_relative", "energy_temporal_bias_identity_relative_max"),
            ]:
                add(label + ": " + name, math.isfinite(m[metric]) and m[metric] <= gates[bound_key], m[metric], gates[bound_key])
            center_values = {key: m[key] for key in [
                "center_max_specific_internal_energy", "center_max_specific_internal_energy_ratio",
                "center_min_density", "center_min_density_ratio", "center_max_pressure", "center_max_pressure_ratio",
            ]}
            center_values["center_first_cell"] = m["center_first_cell"]
            finite = all(math.isfinite(value) for key, value in center_values.items() if key != "center_first_cell")
            finite = finite and all(math.isfinite(value) for value in center_values["center_first_cell"].values())
            add(label + ": finite center diagnostics", finite, center_values, "all finite; no maximum-error convergence gate")
        if len(sphere_runs) == len(config["grids"]):
            core_error = sphere_runs[-1]["metrics"]["core_density_l1"]
            add("spherical: finest core density_l1 (origin included)",
                core_error is not None and math.isfinite(core_error) and core_error <= gates["core_density_l1_finest_max"],
                core_error, gates["core_density_l1_finest_max"])
        else:
            add("spherical: finest core density_l1 (origin included)", False, None, gates["core_density_l1_finest_max"])
    return checks


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", default="inputs.json")
    parser.add_argument("--acceptance", default="acceptance.json")
    parser.add_argument("--spherical-acceptance", default="spherical-acceptance.json")
    parser.add_argument("--output", default="results")
    args = parser.parse_args()
    output = Path(args.output)
    if (output / "results.json").exists():
        raise SystemExit("Refusing to overwrite retained results; choose a new --output")
    output.mkdir(parents=True, exist_ok=True)
    payload = Path(args.input).read_bytes()
    config = json.loads(payload)
    maximum_total_seconds = config.get("maximum_total_seconds", 60.0)
    if "cases" in config:
        if config.get("schema_version") != 1 or set(config["cases"]) != {"noh-shock"}:
            raise SystemExit("Expected schema-1 fixed noh-shock input")
        config = config["cases"]["noh-shock"]
    acceptance = json.loads(Path(args.acceptance).read_text())
    spherical_acceptance = (json.loads(Path(args.spherical_acceptance).read_text())
                            if "spherical" in config["geometries"] else None)
    if spherical_acceptance is not None:
        if spherical_acceptance.get("schema_version") != 1:
            raise SystemExit("Expected schema-1 spherical acceptance")
        for key, expected in spherical_acceptance["fixed_input"].items():
            if config.get(key) != expected:
                raise SystemExit("Spherical predeclared input differs: " + key)
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
    if spherical_acceptance is not None:
        document["spherical_acceptance"] = spherical_acceptance
        document["receipts"]["spherical_acceptance_sha256"] = digest(args.spherical_acceptance)
        active_name = config.get("active_spherical_pre_run_contract", "pre-run-contract-spherical.json")
        active_contract = spherical_contract_path(source_dir, active_name)
        document["receipts"]["spherical_pre_run_contract_filename"] = active_name
        document["receipts"]["spherical_pre_run_contract_sha256"] = digest(active_contract)
        document["receipts"]["spherical_original_pre_run_contract_sha256"] = digest(source_dir / "pre-run-contract-spherical.json")
    started = time.perf_counter()
    for geometry in config["geometries"]:
        for n in config["grids"]:
            try:
                remaining = maximum_total_seconds - (time.perf_counter() - started)
                if remaining <= 0:
                    raise RuntimeError("Total wall-time budget exhausted")
                run = save_run(config, geometry, n, output, maximum_seconds=remaining)
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
    document["checks"] = checks_for_runs(document["runs"], document["convergence"], acceptance, config, spherical_acceptance)
    document["passed"] = bool(document["checks"]) and all(c["passed"] for c in document["checks"])
    document["completed_at_utc"] = datetime.datetime.now(datetime.timezone.utc).isoformat()
    document["duration_seconds"] = time.perf_counter() - started
    (output / "results.json").write_text(json.dumps(document, indent=2, allow_nan=False) + "\n")
    # Standard depth-release envelope, alongside the full profile diagnostics.
    metrics, records = {}, []
    for geometry, rows in document["convergence"].items():
        if rows:
            finest = rows[-1]
            for key in ("density_l1", "density_l2", "density_linf", "density_l1_order", "shock_error", "center_max_sie_relative_excess"):
                metrics[geometry + "_" + key + "_finest"] = finest[key]
            finest_run = next(r for r in document["runs"] if r["geometry"] == geometry and r["n"] == finest["n"])
            for key in ("core_density_l1", "radial_momentum_balance_relative", "mass_temporal_bias_residual_relative", "energy_temporal_bias_residual_relative"):
                metrics[geometry + "_" + key + "_finest"] = finest_run["metrics"][key]
    for run in document["runs"]:
        if run["status"] == "completed":
            record = {"geometry": run["geometry"], "n": run["n"], "steps": run["steps"],
                            **{key: run["metrics"][key] for key in ("density_l1", "density_l2", "density_linf", "shock_error_in_dx", "plateau_density_amplification", "plateau_pressure", "center_max_sie_relative_excess", "mass_balance_relative", "energy_balance_relative")}}
            if run["geometry"] == "spherical":
                record.update({key: run["metrics"][key] for key in ("dt_cubed_sum", "core_density_l1", "radial_momentum_balance_relative", "mass_temporal_bias_residual_relative", "energy_temporal_bias_residual_relative")})
            records.append(record)
    case = {"id": "noh-shock", "passed": document["passed"], "metrics": metrics,
            "checks": {c["name"]: c["passed"] for c in document["checks"]},
            "check_details": document["checks"], "records": records,
            "scope": config["spatial_claim"], "detail": "results.json",
            "input_sha256": hashlib.sha256(json.dumps(config, sort_keys=True).encode()).hexdigest()}
    standard = {"schema_version": 1, "passed": document["passed"], "checks": {"noh-shock": document["passed"]},
                "cases": [case], "termination": "fixed_budget_completed",
                "duration_seconds": document["duration_seconds"],
                "input_sha256": hashlib.sha256(payload).hexdigest(),
                "environment": document["environment"], "source_receipts": document["receipts"]}
    (output / "result.json").write_text(json.dumps(standard, indent=2, allow_nan=False) + "\n")
    if records:
        with (output / "noh-shock.csv").open("w", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(dict.fromkeys(key for record in records for key in record)))
            writer.writeheader()
            writer.writerows(records)

    print(json.dumps({"passed": document["passed"], "checks": len(document["checks"]), "failed": [c for c in document["checks"] if not c["passed"]]}, indent=2), flush=True)
    return 0 if document["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
