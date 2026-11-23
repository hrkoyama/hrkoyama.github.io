"""Independently differentiate tensor polynomial coefficients; never FD solution."""
import csv
from pathlib import Path
import numpy as np
from numpy.polynomial.polynomial import polyder, polyval2d


def ghia():
    with (Path(__file__).parent/'ghia-re100.csv').open() as stream:
        rows = list(csv.DictReader(stream))
    return {c: np.asarray([[float(r['coordinate']), float(r['value'])] for r in rows if r['component'] == c]) for c in ['u', 'v']}


def polynomial_reference(x, y, amplitude, viscosity):
    c = amplitude*np.outer([0., 0., 1., -2., 1.], [0., 0., 1., -2., 1.])
    def derivative(dx, dy):
        return polyval2d(x, y, polyder(polyder(c, dx, axis=0), dy, axis=1))
    p = derivative(0, 0); u = derivative(0, 1); v = -derivative(1, 0)
    w = -derivative(2, 0)-derivative(0, 2)
    wx = -derivative(3, 0)-derivative(1, 2)
    wy = -derivative(2, 1)-derivative(0, 3)
    lw = -derivative(4, 0)-2*derivative(2, 2)-derivative(0, 4)
    return dict(psi=p, u=u, v=v, omega=w, forcing=u*wx+v*wy-viscosity*lw,
                divergence=derivative(1, 1)-derivative(1, 1))


def qualify(implementation, amplitude=8., viscosity=.01):
    # Irrational-looking fixed locations, walls and corners; no solver output used.
    axis = np.array([0., .073, .219, .517, .823, 1.]); X, Y = np.meshgrid(axis, axis)
    expected = polynomial_reference(X, Y, amplitude, viscosity)
    actual = implementation(X, Y, amplitude, viscosity)
    field_error = max(float(np.max(abs(actual[k]-expected[k]))) for k in ['psi', 'u', 'v', 'omega'])
    forcing_error = float(np.max(abs(actual['forcing']-expected['forcing'])))
    mask = (X == 0)|(X == 1)|(Y == 0)|(Y == 1)
    wall_speed = max(float(np.max(abs(expected[k][mask]))) for k in ['u', 'v'])
    tables = ghia()
    checks = {
        'independent tensor-polynomial fields': field_error <= 3e-11,
        'independent tensor-polynomial forcing': forcing_error <= 3e-11,
        'analytic four-wall no slip': wall_speed <= 1e-13,
        'analytic incompressibility': bool(np.max(abs(expected['divergence'])) <= 1e-13),
        'two primary-table columns each 17 points': all(t.shape == (17, 2) and np.all(np.diff(t[:, 0]) < 0) for t in tables.values()) and tables['u'][8, 1] == -.20581 and tables['v'][7, 1] == -.24533,
    }
    return dict(checks=checks, field_maximum=field_error, forcing_maximum=forcing_error,
                exact_wall_speed=wall_speed, passed=all(checks.values()))
