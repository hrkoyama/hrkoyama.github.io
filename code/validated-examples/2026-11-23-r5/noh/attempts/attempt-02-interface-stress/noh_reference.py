"""Independent analytic, volume-integrated cold Noh reference.

This module contains no finite-volume solver imports. Angular factors are
omitted consistently: the volume measure is r**(dimension-1) dr.
"""
import math

import numpy as np


def parameters(dimension, gamma=5.0 / 3.0, rho0=1.0, u0=-1.0):
    if dimension not in (1, 2, 3) or gamma <= 1 or rho0 <= 0 or u0 >= 0:
        raise ValueError("Require dimension 1/2/3, gamma>1, rho0>0, u0<0")
    compression = (gamma + 1.0) / (gamma - 1.0)
    rho = rho0 * compression**dimension
    return {
        "shock_speed": -u0 * (gamma - 1.0) / 2.0,
        "rho_post": rho,
        "pressure_post": rho * u0**2 * (gamma - 1.0) / 2.0,
        "specific_internal_energy_post": 0.5 * u0**2,
        "shock_density_jump": compression,
        "initial_density_amplification": compression**dimension,
    }


def point_values(radius, time, dimension, gamma=5.0 / 3.0,
                 rho0=1.0, u0=-1.0):
    """Point primitives, selecting the cold upstream value at the shock."""
    par = parameters(dimension, gamma, rho0, u0)
    radius = np.asarray(radius, dtype=float)
    if np.any(radius < 0) or time < 0:
        raise ValueError("Nonnegative radii and time required")
    shocked = radius < par["shock_speed"] * time
    density = np.empty_like(radius)
    density[shocked] = par["rho_post"]
    outside = ~shocked
    if time == 0:
        density[outside] = rho0
    else:
        density[outside] = rho0 * (
            1.0 - u0 * time / radius[outside]
        )**(dimension - 1)
    velocity = np.where(shocked, 0.0, u0)
    pressure = np.where(shocked, par["pressure_post"], 0.0)
    sie = np.where(shocked, par["specific_internal_energy_post"], 0.0)
    return density, velocity, pressure, sie


def cell_averages(edges, time, dimension, gamma=5.0 / 3.0,
                  rho0=1.0, u0=-1.0):
    """Exact conservative cell averages, splitting a shock-crossing cell.

    Average pressure is also returned separately: evaluating p on averaged
    conserved variables adds the kinetic energy of unresolved velocities.
    """
    par = parameters(dimension, gamma, rho0, u0)
    edges = np.asarray(edges, dtype=float)
    if time < 0 or edges.ndim != 1 or len(edges) < 2:
        raise ValueError("Invalid time or edges")
    if edges[0] < 0 or np.any(np.diff(edges) <= 0):
        raise ValueError("Increasing nonnegative edges required")
    left, right = edges[:-1], edges[1:]
    volume = (right**dimension - left**dimension) / dimension
    shock = par["shock_speed"] * time
    inner_end = np.maximum(left, np.minimum(right, shock))
    inner_volume = (inner_end**dimension - left**dimension) / dimension
    outer_start = np.minimum(right, np.maximum(left, shock))
    # rho*r^(d-1) = rho0*(r+|u0|*t)^(d-1) in the cold inflow.
    outside_mass = rho0 * (
        (right - u0 * time)**dimension
        - (outer_start - u0 * time)**dimension
    ) / dimension
    mass = par["rho_post"] * inner_volume + outside_mass
    q = np.column_stack((mass, u0 * outside_mass, 0.5 * u0**2 * mass))
    q /= volume[:, None]
    pressure_average = par["pressure_post"] * inner_volume / volume
    return q, pressure_average


def exact_integrals(radius, time, dimension, rho0=1.0, u0=-1.0):
    """Total mass/energy while the shock remains inside the outer boundary."""
    mass = rho0 * (radius - u0 * time)**dimension / dimension
    return mass, 0.5 * u0**2 * mass


def integrate_reference_by_gauss(edges, time, dimension, gamma=5.0 / 3.0,
                                 rho0=1.0, u0=-1.0):
    """Separate point formula + split Gauss integration for reference checks."""
    par = parameters(dimension, gamma, rho0, u0)
    nodes, weights = np.polynomial.legendre.leggauss(8)
    result = []
    for left, right in zip(edges[:-1], edges[1:]):
        cuts = [float(left), float(right)]
        shock = par["shock_speed"] * time
        if left < shock < right:
            cuts.insert(1, shock)
        integral = np.zeros(3)
        for start, end in zip(cuts[:-1], cuts[1:]):
            r = (start + end) / 2.0 + (end - start) / 2.0 * nodes
            rho, velocity, pressure, _ = point_values(
                r, time, dimension, gamma, rho0, u0
            )
            energy = pressure / (gamma - 1) + 0.5 * rho * velocity**2
            values = np.column_stack((rho, rho * velocity, energy))
            integral += (end - start) / 2.0 * np.sum(
                weights[:, None] * r[:, None]**(dimension - 1) * values,
                axis=0,
            )
        volume = (right**dimension - left**dimension) / dimension
        result.append(integral / volume)
    return np.asarray(result)
