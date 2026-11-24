"""Independent scaled tridiagonal Bratu state and sensitivity oracle, n31."""
import numpy as np


def solve_tridiagonal(diagonal, rhs):
    diagonal, work = np.asarray(diagonal, dtype=float).copy(), np.asarray(rhs, dtype=float).copy()
    vector = work.ndim == 1
    if vector:
        work = work[:, None]
    if diagonal.ndim != 1 or work.shape[0] != len(diagonal):
        raise ValueError('Tridiagonal dimensions differ')
    for i in range(1, len(diagonal)):
        if diagonal[i-1] == 0:
            raise ValueError('Zero Thomas pivot')
        multiplier = -1. / diagonal[i-1]
        diagonal[i] -= -multiplier
        work[i] -= multiplier * work[i-1]
    if diagonal[-1] == 0:
        raise ValueError('Zero Thomas pivot')
    answer = np.empty_like(work)
    answer[-1] = work[-1] / diagonal[-1]
    for i in range(len(diagonal)-2, -1, -1):
        answer[i] = (work[i] + answer[i+1]) / diagonal[i]
    return answer[:, 0] if vector else answer


def state_and_sensitivity(n, theta, positions, retainer=None):
    if retainer:
        retainer.raw('thomas-parameters-before-validation', parameters=theta)
    theta = np.asarray(theta, dtype=float)
    if (theta.shape != (2,) or not np.all(np.isfinite(theta)) or
            theta[0] - abs(theta[1]) <= 0 or theta[0] + abs(theta[1]) > 3.3+1e-14):
        raise ValueError('Independent forward domain violated')
    h = 1. / (int(n)+1)
    x = np.arange(1, int(n)+1)*h
    coefficient = theta[0] + theta[1]*(2.*x-1.)
    u = np.zeros(int(n))
    last_correction = None
    for iteration in range(41):
        if retainer:
            retainer.raw('thomas-current-before-equation', parameters=theta, state=u,
                          iteration=iteration)
        exponential = np.exp(u)
        residual = 2.*u - np.pad(u, (1, 1))[:-2] - np.pad(u, (1, 1))[2:] - h*h*coefficient*exponential
        diagonal = 2. - h*h*coefficient*exponential
        if retainer:
            retainer.raw('thomas-equation-before-linear-solve', state=u, residual=residual,
                          diagonal=diagonal, last_correction=last_correction)
        residual_inf = float(np.linalg.norm(residual, ord=np.inf))
        if last_correction is not None and last_correction <= 2e-13 and residual_inf <= 2e-14:
            break
        if iteration == 40:
            raise RuntimeError('Independent Thomas Newton budget exhausted')
        correction = solve_tridiagonal(diagonal, -residual)
        u = u + correction
        last_correction = float(np.linalg.norm(correction, ord=np.inf))
        if retainer:
            retainer.raw('thomas-completed-newton-state', state=u, correction=correction,
                          parameters=theta)
    positions = np.asarray(positions, dtype=float)
    scaled_positions = positions / h
    nodes = np.rint(scaled_positions).astype(int)
    if np.any(np.abs(scaled_positions-nodes) > 1e-12) or np.any(nodes < 1) or np.any(nodes > n):
        raise ValueError('The fixed oracle observations must coincide with interior nodes')
    parameter_rhs = h*h*np.exp(u)[:, None]*np.column_stack((np.ones(n), 2.*x-1.))
    sensitivity = solve_tridiagonal(diagonal, parameter_rhs)
    result = dict(state=u, predicted=u[nodes-1], data_jacobian=sensitivity[nodes-1],
                  state_sensitivity=sensitivity, scaled_residual_inf=residual_inf,
                  correction_inf=last_correction, newton_updates=iteration)
    if retainer:
        retainer.raw('thomas-complete-before-next-diagnostic', parameters=theta, **result)
    return result
