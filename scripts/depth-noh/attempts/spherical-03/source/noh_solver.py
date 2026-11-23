"""Radial Euler finite volumes with true cold inflow.

Piecewise-constant default or conservative MUSCL-minmod reconstruction,
local Lax-Friedrichs flux and SSPRK2 time integration.
The geometric pressure source uses the same Rusanov interfacial normal
stress as the flux (arithmetic face quadrature by default, or exact radial
integration of its face-linear interpolant). This includes numerical
viscosity consistently at the cold origin; see the retained failed attempt.
No reference-profile function is imported: the analytic inflow follows the
pressureless continuity equation and is implemented locally at r=R.
"""
import math
import time as walltime

import numpy as np


def primitive(q, gamma):
    q = np.asarray(q, dtype=float)
    rho = q[..., 0]
    if not np.all(np.isfinite(q)) or np.any(rho <= 0):
        raise FloatingPointError("Nonfinite state or nonpositive density")
    velocity = q[..., 1] / rho
    internal = q[..., 2] - 0.5 * q[..., 1] * velocity
    scale = np.maximum(np.abs(q[..., 2]), np.finfo(float).tiny)
    if np.any(internal < -64.0 * np.finfo(float).eps * scale):
        raise FloatingPointError("Negative internal energy beyond roundoff")
    pressure = (gamma - 1.0) * internal
    # This does not change q, E, or pressure; only a square-root argument.
    sound = np.sqrt(np.maximum(gamma * pressure / rho, 0.0))
    return rho, velocity, pressure, internal / rho, sound


def conservative(rho, velocity, pressure, gamma):
    return np.column_stack((rho, rho * velocity,
                            pressure / (gamma - 1.0) + 0.5 * rho * velocity**2))


def physical_flux(q, gamma):
    rho, velocity, pressure, _, sound = primitive(q, gamma)
    flux = np.column_stack((q[:, 1], q[:, 1] * velocity + pressure,
                            (q[:, 2] + pressure) * velocity))
    return flux, np.abs(velocity) + sound


def inflow(time, radius, dimension, gamma, rho0, u0):
    density = rho0 * (1.0 - u0 * time / radius)**(dimension - 1)
    return np.array([density, density * u0, 0.5 * density * u0**2])


def volume_centroids(edges, dimension):
    """Centroids for the measure r**(dimension-1) dr, not face midpoints."""
    edges = np.asarray(edges, dtype=float)
    if dimension not in (1, 2, 3) or edges.ndim != 1 or len(edges) < 2:
        raise ValueError("Require radial dimension 1/2/3 and increasing faces")
    if not np.all(np.isfinite(edges)) or edges[0] < 0 or np.any(np.diff(edges) <= 0):
        raise ValueError("Require finite increasing nonnegative faces")
    centers = dimension / (dimension + 1.0) * np.diff(edges**(dimension + 1)) / np.diff(edges**dimension)
    if not np.all(np.isfinite(centers)):
        raise ValueError("Nonfinite radial centroids")
    return centers


def minmod(left, right):
    same_sign = ((left > 0) & (right > 0)) | ((left < 0) & (right < 0))
    return np.where(same_sign, np.sign(left) * np.minimum(np.abs(left), np.abs(right)), 0.0)


def admissible_conserved(states):
    """The primitive routine's density/internal-energy domain, per state."""
    states = np.asarray(states, dtype=float)
    finite = np.all(np.isfinite(states), axis=-1)
    density = states[..., 0]
    positive = finite & (density > 0)
    # No state is changed. A harmless denominator is used only for the
    # predicate's arithmetic on already-rejected nonpositive-density entries.
    denominator = np.where(positive, density, 1.0)
    internal = states[..., 2] - 0.5 * states[..., 1] * (states[..., 1] / denominator)
    scale = np.maximum(np.abs(states[..., 2]), np.finfo(float).tiny)
    return positive & np.isfinite(internal) & (internal >= -64.0 * np.finfo(float).eps * scale)


def reconstruct_conserved(q, edges, dimension, gamma):
    """Face states with one common slope factor per conservative cell mean.

    Interior slopes are minmod of the two centroid-distance differences.
    Boundary cells have zero slope. Bisection reduces a single theta for all
    three components and both faces; it never modifies a cell average.
    """
    q = np.asarray(q, dtype=float)
    edges = np.asarray(edges, dtype=float)
    primitive(q, gamma)
    if q.ndim != 2 or q.shape[1] != 3 or len(edges) != len(q) + 1:
        raise ValueError("Require three conserved means per radial cell")
    centers = volume_centroids(edges, dimension)
    slopes = np.zeros_like(q)
    if len(q) > 2:
        left = (q[1:-1] - q[:-2]) / (centers[1:-1] - centers[:-2])[:, None]
        right = (q[2:] - q[1:-1]) / (centers[2:] - centers[1:-1])[:, None]
        slopes[1:-1] = minmod(left, right)
    delta_left = slopes * (edges[:-1] - centers)[:, None]
    delta_right = slopes * (edges[1:] - centers)[:, None]
    theta = np.ones(len(q))
    full_ok = admissible_conserved(q + delta_left) & admissible_conserved(q + delta_right)
    limited = np.flatnonzero(~full_ok)
    if len(limited):
        means, dl, dr = q[limited], delta_left[limited], delta_right[limited]
        low, high = np.zeros(len(limited)), np.ones(len(limited))
        for _ in range(52):
            middle = 0.5 * (low + high)
            ok = admissible_conserved(means + middle[:, None] * dl)
            ok &= admissible_conserved(means + middle[:, None] * dr)
            low = np.where(ok, middle, low)
            high = np.where(ok, high, middle)
        # Step slightly into the accepted interval before recomputing faces.
        # This scales slopes only, not the conservative mean or its energy.
        theta[limited] = np.nextafter(low, np.zeros_like(low))
    left_faces = q + theta[:, None] * delta_left
    right_faces = q + theta[:, None] * delta_right
    accepted = admissible_conserved(left_faces) & admissible_conserved(right_faces)
    if not np.all(accepted):
        # Rounding at an admissibility boundary may require zero slope. The
        # same theta=0 is applied to ALL components of that cell at BOTH faces.
        theta[~accepted] = 0.0
        left_faces = q + theta[:, None] * delta_left
        right_faces = q + theta[:, None] * delta_right
    primitive(left_faces, gamma)
    primitive(right_faces, gamma)
    return left_faces, right_faces, theta


def linear_radial_stress_integral(edges, face_stress, dimension):
    """Integrate a face-linear stress against d(r**(dimension-1)).

    This integrates the numerical stress interpolant, not the unknown exact
    physical pressure. In spherical symmetry its radial weight is 2*r.
    """
    edges = np.asarray(edges, dtype=float)
    face_stress = np.asarray(face_stress, dtype=float)
    if dimension not in (1, 2, 3) or edges.ndim != 1 or len(edges) < 2:
        raise ValueError("Require radial dimension 1/2/3 and at least two faces")
    if face_stress.shape != edges.shape or not np.all(np.isfinite(face_stress)):
        raise ValueError("Require one finite stress per face")
    if not np.all(np.isfinite(edges)) or edges[0] < 0 or np.any(np.diff(edges) <= 0):
        raise ValueError("Require finite increasing nonnegative radial faces")
    if dimension == 1:
        return np.zeros(len(edges) - 1)
    if dimension == 2:
        return 0.5 * (face_stress[:-1] + face_stress[1:]) * np.diff(edges)
    # Equivalent to dr*((b+2*a)*Pleft+(2*b+a)*Pright)/3, but this
    # constant-preserving form keeps Pleft==Pright bitwise identical to the
    # original arithmetic integral before division by the cell volume.
    arithmetic = 0.5 * (face_stress[:-1] + face_stress[1:]) * np.diff(edges**2)
    correction = np.diff(edges)**2 * (face_stress[1:] - face_stress[:-1]) / 6.0
    return arithmetic + correction


def operator(q, time, edges, dimension, gamma, rho0, u0, stress_quadrature="arithmetic-face",
             reconstruction="piecewise-constant", diagnostics=None):
    if stress_quadrature not in ("arithmetic-face", "linear-radial-stress"):
        raise ValueError("Unknown stress quadrature: " + str(stress_quadrature))
    if reconstruction not in ("piecewise-constant", "muscl-minmod"):
        raise ValueError("Unknown reconstruction: " + str(reconstruction))
    volume = np.diff(edges**dimension) / dimension
    area = np.ones_like(edges) if dimension == 1 else edges**(dimension - 1)
    left_ghost = q[0].copy()
    left_ghost[1] *= -1
    right_ghost = inflow(time, edges[-1], dimension, gamma, rho0, u0)
    if reconstruction == "piecewise-constant":
        # Preserve the complete original path, including operation order.
        padded = np.vstack((left_ghost, q, right_ghost))
        flux, speed = physical_flux(padded, gamma)
        wavespeed = np.maximum(speed[:-1], speed[1:])
        faces = 0.5 * (flux[:-1] + flux[1:]) - 0.5 * wavespeed[:, None] * np.diff(padded, axis=0)
        theta = None
    else:
        cell_left, cell_right, theta = reconstruct_conserved(q, edges, dimension, gamma)
        reflecting_face = cell_left[0].copy()
        reflecting_face[1] *= -1
        left_states = np.vstack((reflecting_face, cell_right))
        right_states = np.vstack((cell_left, right_ghost))
        left_flux, left_speed = physical_flux(left_states, gamma)
        right_flux, right_speed = physical_flux(right_states, gamma)
        wavespeed = np.maximum(left_speed, right_speed)
        faces = 0.5 * (left_flux + right_flux) - 0.5 * wavespeed[:, None] * (right_states - left_states)
    if diagnostics is not None:
        diagnostics.update({"theta_reduced_cells": 0 if theta is None else int(np.count_nonzero(theta < 1)),
                            "theta_zero_cells": 0 if theta is None else int(np.count_nonzero(theta == 0)),
                            "theta_min": 1.0 if theta is None else float(np.min(theta))})
    # The outer boundary is prescribed supersonic, cold, inward flow. Using
    # the physical boundary flux avoids numerically diffusing cell averages
    # against a boundary-face point state. All characteristics enter there.
    faces[-1] = np.array([right_ghost[1], right_ghost[1] * u0,
                          right_ghost[2] * u0])
    weighted = area[:, None] * faces
    rhs = -np.diff(weighted, axis=0) / volume[:, None]
    source = np.zeros_like(q)
    # Use the interface normal stress already present in the momentum flux.
    # For a reflecting face this equals its Riemann wall stress; for constant
    # velocity cold flow it is zero; for static constant pressure it is p.
    # A cell-pressure quadrature at an area-zero origin otherwise leaves the
    # singular cold inflow in an unphysical zero-pressure accumulation state.
    if reconstruction == "piecewise-constant":
        velocity = primitive(padded, gamma)[1]
        face_velocity = 0.5 * (velocity[:-1] + velocity[1:])
    else:
        face_velocity = 0.5 * (primitive(left_states, gamma)[1] + primitive(right_states, gamma)[1])
    normal_stress = faces[:, 1] - face_velocity * faces[:, 0]
    pressure_quadrature = 0.5 * (normal_stress[:-1] + normal_stress[1:])
    if stress_quadrature == "linear-radial-stress" and dimension == 3:
        source[:, 1] = linear_radial_stress_integral(edges, normal_stress, dimension) / volume
    else:
        # Keep the original arithmetic path and operation order, including
        # d=1/2 where this is already exact for a face-linear stress.
        source[:, 1] = pressure_quadrature * np.diff(area) / volume
    rhs += source
    net = weighted[0] - weighted[-1]
    source_integral = np.sum(source * volume[:, None], axis=0)
    return rhs, net, source_integral, wavespeed


def solve(n, dimension, final_time=0.6, r_max=1.0, gamma=5.0 / 3.0,
          rho0=1.0, u0=-1.0, cfl=0.35, max_steps=100000, maximum_seconds=60.0,
          stress_quadrature="arithmetic-face", reconstruction="piecewise-constant"):
    if stress_quadrature not in ("arithmetic-face", "linear-radial-stress"):
        raise ValueError("Unknown stress quadrature: " + str(stress_quadrature))
    if reconstruction not in ("piecewise-constant", "muscl-minmod"):
        raise ValueError("Unknown reconstruction: " + str(reconstruction))
    if not all(math.isfinite(float(x)) for x in (final_time, r_max, gamma, rho0, u0, cfl, maximum_seconds)):
        raise ValueError("Finite input values required")
    if isinstance(n, bool) or int(n) != n or isinstance(dimension, bool):
        raise ValueError("Integer grid and dimension required")
    if n < 8 or dimension not in (1, 2, 3) or final_time <= 0 or r_max <= 0:
        raise ValueError("Invalid grid, geometry, domain or time")
    if gamma <= 1 or rho0 <= 0 or u0 >= 0 or not 0 < cfl < 0.5:
        raise ValueError("Invalid gas, inflow or CFL")
    if maximum_seconds <= 0:
        raise ValueError("Positive wall-time budget required")
    if -u0 * (gamma - 1.0) / 2.0 * final_time >= r_max:
        raise ValueError("The fixed cold inflow requires the shock inside the domain")
    edges = np.linspace(0.0, r_max, n + 1)
    volume = np.diff(edges**dimension) / dimension
    area = np.ones_like(edges) if dimension == 1 else edges**(dimension - 1)
    q = conservative(np.full(n, rho0), np.full(n, u0), np.zeros(n), gamma)
    initial = np.sum(q * volume[:, None], axis=0)
    boundary, source = np.zeros(3), np.zeros(3)
    time, steps = 0.0, 0
    dt_cubed_sum = 0.0
    min_pressure, min_density = 0.0, rho0
    min_roundoff_units, negative_pressure_evaluations = 0.0, 0
    history = []
    minimum_dt, maximum_dt = float("inf"), 0.0
    theta_reduced_stage_cells, theta_zero_stage_cells, theta_min = 0, 0, 1.0

    def observe(state):
        nonlocal min_pressure, min_density, min_roundoff_units, negative_pressure_evaluations
        density, _, pressure, _, _ = primitive(state, gamma)
        scale = np.maximum(abs(state[:, 2]), np.finfo(float).tiny)
        units = pressure / ((gamma - 1) * np.finfo(float).eps * scale)
        min_pressure = min(min_pressure, float(pressure.min()))
        min_density = min(min_density, float(density.min()))
        min_roundoff_units = min(min_roundoff_units, float(units.min()))
        negative_pressure_evaluations += int(np.count_nonzero(pressure < 0))

    def checked_observe(state, stage_name, stage_time, stage_diagnostics):
        try:
            observe(state)
        except FloatingPointError as error:
            # Preserve the failed conservative update; never retry its time
            # step, replace selected cells, clip pressure or repair energy.
            error.failed_state = state.copy()
            error.failed_edges = edges.copy()
            error.failed_history = list(history)
            error.failed_context = {"stage": stage_name, "stage_time": stage_time,
                                    "step": steps + 1, "reconstruction": reconstruction,
                                    "stress_quadrature": stress_quadrature,
                                    "reconstruction_diagnostics_used": stage_diagnostics,
                                    "completed_theta_reduced_stage_cells": theta_reduced_stage_cells,
                                    "completed_theta_zero_stage_cells": theta_zero_stage_cells,
                                    "completed_theta_min": theta_min}
            raise

    started = walltime.perf_counter()
    while time < final_time:
        if steps >= max_steps:
            raise RuntimeError("Maximum step count reached")
        if walltime.perf_counter() - started > maximum_seconds:
            raise RuntimeError("Wall-time budget exhausted")
        diagnostics0 = {}
        rhs0, net0, source0, speed = operator(q, time, edges, dimension, gamma, rho0, u0,
                                             stress_quadrature=stress_quadrature,
                                             reconstruction=reconstruction, diagnostics=diagnostics0)
        rate = (area[:-1] * speed[:-1] + area[1:] * speed[1:]) / volume
        dt = min(cfl / float(np.max(rate)), final_time - time)
        stage = q + dt * rhs0
        checked_observe(stage, "forward-euler-stage", time + dt, [diagnostics0])
        diagnostics1 = {}
        rhs1, net1, source1, _ = operator(stage, time + dt, edges, dimension, gamma, rho0, u0,
                                         stress_quadrature=stress_quadrature,
                                         reconstruction=reconstruction, diagnostics=diagnostics1)
        q = 0.5 * (q + stage + dt * rhs1)
        checked_observe(q, "heun-combination", time + dt, [diagnostics0, diagnostics1])
        for diagnostic in [diagnostics0, diagnostics1]:
            theta_reduced_stage_cells += diagnostic["theta_reduced_cells"]
            theta_zero_stage_cells += diagnostic["theta_zero_cells"]
            theta_min = min(theta_min, diagnostic["theta_min"])
        boundary += dt * 0.5 * (net0 + net1)
        source += dt * 0.5 * (source0 + source1)
        dt_cubed_sum += dt**3
        time += dt
        steps += 1
        minimum_dt, maximum_dt = min(minimum_dt, dt), max(maximum_dt, dt)
        if steps == 1 or steps % 100 == 0 or time == final_time:
            integral = np.sum(q * volume[:, None], axis=0)
            history.append({"step": steps, "time": time, "dt": dt,
                            "dt_cubed_sum": dt_cubed_sum,
                            "reconstruction_theta_reduced_stage_cells": theta_reduced_stage_cells,
                            "reconstruction_theta_zero_stage_cells": theta_zero_stage_cells,
                            "reconstruction_theta_min": theta_min,
                            "integral": integral.tolist(),
                            "boundary_net_integral": boundary.tolist(),
                            "source_integral": source.tolist(),
                            "balance_residual": (integral - initial - boundary - source).tolist()})
    integral = np.sum(q * volume[:, None], axis=0)
    return {"q": q, "edges": edges, "volume": volume, "time": time,
            "stress_quadrature": stress_quadrature,
            "reconstruction": reconstruction,
            "reconstruction_theta_reduced_stage_cells": theta_reduced_stage_cells,
            "reconstruction_theta_zero_stage_cells": theta_zero_stage_cells,
            "reconstruction_theta_min": theta_min,
            "steps": steps, "initial_integral": initial,
            "final_integral": integral, "boundary_net_integral": boundary,
            "source_integral": source, "history": history,
            "dt_cubed_sum": dt_cubed_sum,
            "min_pressure": min_pressure, "min_density": min_density,
            "min_internal_energy_roundoff_units": min_roundoff_units,
            "negative_pressure_evaluations": negative_pressure_evaluations,
            "state_floor_corrections": 0, "minimum_dt": minimum_dt,
            "maximum_dt": maximum_dt}
