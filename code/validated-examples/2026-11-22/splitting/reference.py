"""Unsplit time references for the SAME periodic FD semidiscrete equations.

No splitting, FFT diffusion, midpoint reaction or solver RHS is imported here.
Radau and DOP853 are independent time algorithms, not independent PDE engines.
"""
import math
import numpy as np
from scipy.integrate import solve_ivp
from scipy.sparse import bmat, diags


def initial_values(config):
    n = config['grid']
    x = np.arange(n) * config['length'] / n
    field = np.zeros((2, n))
    for species, coefficients in enumerate(config['initial_cosine_coefficients']):
        for mode, value in enumerate(coefficients):
            field[species] += value * np.cos(2 * math.pi * mode * x / config['length'])
    return field


def system(config, budget):
    n = config['grid']
    dx = config['length'] / n
    lap = diags([np.ones(n-1), -2*np.ones(n), np.ones(n-1)], [-1, 0, 1], format='lil')
    lap[0, -1] = lap[-1, 0] = 1
    lap = lap.tocsc() / dx**2
    du, dv = config['diffusion']
    a, b = config['a'], config['b']

    def rhs(t, vector):
        budget.check()
        u, v = vector[:n], vector[n:]
        return np.concatenate((du*(lap @ u)+a-u+u*u*v,
                               dv*(lap @ v)+b-u*u*v))

    def jac(t, vector):
        budget.check()
        u, v = vector[:n], vector[n:]
        return bmat([[du*lap+diags(-1+2*u*v), diags(u*u)],
                     [diags(-2*u*v), dv*lap-diags(u*u)]], format='csc')
    return rhs, jac


def solve(config, budget, method, rtol, atol):
    rhs, jac = system(config, budget)
    options = {'jac': jac} if method == 'Radau' else {}
    solution = solve_ivp(rhs, (0, config['time']), initial_values(config).ravel(),
                         method=method, t_eval=config['snapshot_times'],
                         rtol=rtol, atol=atol, **options)
    if not solution.success or solution.t[-1] != config['time']:
        raise RuntimeError('Unsplit reference failed: ' + solution.message)
    values = solution.y.T.reshape(len(solution.t), 2, config['grid'])
    if not np.isfinite(values).all():
        raise RuntimeError('Nonfinite reference')
    return values, {'method': method, 'rtol': rtol, 'atol': atol,
                    'nfev': int(solution.nfev), 'njev': int(solution.njev),
                    'nlu': int(solution.nlu), 'termination': 'reached_fixed_final_time'}
