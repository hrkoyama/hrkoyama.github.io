"""First-order-space radial Euler finite volumes with true cold inflow.

Piecewise constant local Lax-Friedrichs flux + SSPRK2 time integration.
The geometric pressure source uses the same Rusanov interfacial normal
stress as the flux (arithmetic face quadrature). This includes numerical
viscosity consistently at the cold origin; see the retained failed attempt.
No reference-profile function is imported: the analytic inflow follows the
pressureless continuity equation and is implemented locally at r=R.
"""
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


def operator(q, time, edges, dimension, gamma, rho0, u0):
    volume = np.diff(edges**dimension) / dimension
    area = np.ones_like(edges) if dimension == 1 else edges**(dimension - 1)
    left_ghost = q[0].copy()
    left_ghost[1] *= -1
    right_ghost = inflow(time, edges[-1], dimension, gamma, rho0, u0)
    padded = np.vstack((left_ghost, q, right_ghost))
    flux, speed = physical_flux(padded, gamma)
    wavespeed = np.maximum(speed[:-1], speed[1:])
    faces = 0.5 * (flux[:-1] + flux[1:]) - 0.5 * wavespeed[:, None] * np.diff(padded, axis=0)
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
    velocity = primitive(padded, gamma)[1]
    face_velocity = 0.5 * (velocity[:-1] + velocity[1:])
    normal_stress = faces[:, 1] - face_velocity * faces[:, 0]
    pressure_quadrature = 0.5 * (normal_stress[:-1] + normal_stress[1:])
    source[:, 1] = pressure_quadrature * np.diff(area) / volume
    rhs += source
    net = weighted[0] - weighted[-1]
    source_integral = np.sum(source * volume[:, None], axis=0)
    return rhs, net, source_integral, wavespeed


def solve(n, dimension, final_time=0.6, r_max=1.0, gamma=5.0 / 3.0,
          rho0=1.0, u0=-1.0, cfl=0.35, max_steps=100000):
    if n < 8 or dimension not in (1, 2, 3) or final_time <= 0 or r_max <= 0:
        raise ValueError("Invalid grid, geometry, domain or time")
    if gamma <= 1 or rho0 <= 0 or u0 >= 0 or not 0 < cfl < 0.5:
        raise ValueError("Invalid gas, inflow or CFL")
    edges = np.linspace(0.0, r_max, n + 1)
    volume = np.diff(edges**dimension) / dimension
    area = np.ones_like(edges) if dimension == 1 else edges**(dimension - 1)
    q = conservative(np.full(n, rho0), np.full(n, u0), np.zeros(n), gamma)
    initial = np.sum(q * volume[:, None], axis=0)
    boundary, source = np.zeros(3), np.zeros(3)
    time, steps = 0.0, 0
    min_pressure, min_density = 0.0, rho0
    min_roundoff_units, negative_pressure_evaluations = 0.0, 0
    history = []
    minimum_dt, maximum_dt = float("inf"), 0.0

    def observe(state):
        nonlocal min_pressure, min_density, min_roundoff_units, negative_pressure_evaluations
        density, _, pressure, _, _ = primitive(state, gamma)
        scale = np.maximum(abs(state[:, 2]), np.finfo(float).tiny)
        units = pressure / ((gamma - 1) * np.finfo(float).eps * scale)
        min_pressure = min(min_pressure, float(pressure.min()))
        min_density = min(min_density, float(density.min()))
        min_roundoff_units = min(min_roundoff_units, float(units.min()))
        negative_pressure_evaluations += int(np.count_nonzero(pressure < 0))

    while time < final_time:
        if steps >= max_steps:
            raise RuntimeError("Maximum step count reached")
        rhs0, net0, source0, speed = operator(q, time, edges, dimension, gamma, rho0, u0)
        rate = (area[:-1] * speed[:-1] + area[1:] * speed[1:]) / volume
        dt = min(cfl / float(np.max(rate)), final_time - time)
        stage = q + dt * rhs0
        observe(stage)
        rhs1, net1, source1, _ = operator(stage, time + dt, edges, dimension, gamma, rho0, u0)
        q = 0.5 * (q + stage + dt * rhs1)
        observe(q)
        boundary += dt * 0.5 * (net0 + net1)
        source += dt * 0.5 * (source0 + source1)
        time += dt
        steps += 1
        minimum_dt, maximum_dt = min(minimum_dt, dt), max(maximum_dt, dt)
        if steps == 1 or steps % 100 == 0 or time == final_time:
            integral = np.sum(q * volume[:, None], axis=0)
            history.append({"step": steps, "time": time, "dt": dt,
                            "integral": integral.tolist(),
                            "boundary_net_integral": boundary.tolist(),
                            "source_integral": source.tolist(),
                            "balance_residual": (integral - initial - boundary - source).tolist()})
    integral = np.sum(q * volume[:, None], axis=0)
    return {"q": q, "edges": edges, "volume": volume, "time": time,
            "steps": steps, "initial_integral": initial,
            "final_integral": integral, "boundary_net_integral": boundary,
            "source_integral": source, "history": history,
            "min_pressure": min_pressure, "min_density": min_density,
            "min_internal_energy_roundoff_units": min_roundoff_units,
            "negative_pressure_evaluations": negative_pressure_evaluations,
            "state_floor_corrections": 0, "minimum_dt": minimum_dt,
            "maximum_dt": maximum_dt}
