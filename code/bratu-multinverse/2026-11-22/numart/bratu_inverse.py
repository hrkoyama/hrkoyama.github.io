"""Bounded scalar Bratu identification using a discrete adjoint gradient.

Only the smooth lower branch is considered. Observations are at fixed grid
nodes: no interpolation or parameter-dependent observation operator is hidden.
The optimizer uses an adjoint gradient, never a parameter finite difference.
"""
import numpy as np
from .autodiff import bratu_jacobian, bratu_residual
from .bratu_sensitivity import adjoint_gradient, solve_bratu


POSITIONS = np.array([.125, .25, .5, .75, .875])
BOUNDS = (.2, 3.4)
TRUTH_ALPHA = 1.5
TRUTH_LAMBDA = float(2*TRUTH_ALPHA**2/np.cosh(TRUTH_ALPHA/2)**2)
FIXED_NOISE = 1e-3*np.array([1., -.6, .4, -1., .3])


def observation_matrix(n, positions=POSITIONS):
    """Point samples at exact mesh nodes; fixed zero endpoints give zero rows."""
    if not isinstance(n, (int, np.integer)) or n < 1:
        raise ValueError('Positive interior-node count required')
    positions = np.asarray(positions, dtype=float)
    if (positions.ndim != 1 or not len(positions) or not np.all(np.isfinite(positions))
            or np.any(positions < 0) or np.any(positions > 1)):
        raise ValueError('Observation positions must lie in [0,1]')
    nodes = positions*(n+1)
    indices = np.rint(nodes).astype(int)
    if np.max(abs(nodes-indices)) > 1e-12:
        raise ValueError('This example requires observations at exact grid nodes')
    matrix = np.zeros((len(positions), n))
    for row, index in enumerate(indices):
        if 0 < index < n+1:
            matrix[row, index-1] = 1.
    return matrix


def continuous_observations(positions=POSITIONS, alpha=TRUTH_ALPHA):
    """Closed-form continuous family, independent of the inverse grid solve."""
    x = np.asarray(positions, dtype=float)
    return -2*np.log(np.cosh(alpha*(x-.5))/np.cosh(alpha/2))


def _specification(n, data, positions, weights, gamma, prior):
    matrix = observation_matrix(n, positions)
    data = np.asarray(data, dtype=float)
    if data.shape != (len(matrix),) or not np.all(np.isfinite(data)):
        raise ValueError('One finite datum per observation is required')
    weights = np.ones(len(matrix))/len(matrix) if weights is None else np.asarray(weights, dtype=float)
    if weights.shape != data.shape or not np.all(np.isfinite(weights)) or np.any(weights <= 0):
        raise ValueError('Strictly positive finite observation weights required')
    if not np.isfinite(gamma) or gamma < 0 or not np.isfinite(prior):
        raise ValueError('Finite nonnegative regularization and finite prior required')
    return matrix, data, weights


def evaluate(n, lam, data, positions=POSITIONS, weights=None,
             gamma=0., prior=0., primal_tolerance=1e-10, gradient=True):
    """Solve F=0 afresh, then evaluate L and (optionally) its adjoint gradient.

    L=.5 sum(w_j*(H*u-d)_j^2)+.5*gamma*(lambda-prior)^2.
    Each state solve starts at zero. Failed primal solves raise; an optimizer
    cannot silently accept a failed forward evaluation.
    """
    if not np.isfinite(primal_tolerance) or primal_tolerance <= 0:
        raise ValueError('Positive finite primal tolerance required')
    h, data, weights = _specification(n, data, positions, weights, gamma, prior)
    root = solve_bratu(n, lam, primal_tolerance)
    residual_norm = float(np.linalg.norm(bratu_residual(root.x, lam)))
    if not root.converged or residual_norm > primal_tolerance:
        raise RuntimeError('Primal solve failed: '+root.reason)
    predicted = h@root.x
    misfit = predicted-data
    value = float(.5*np.sum(weights*misfit**2)+.5*gamma*(lam-prior)**2)
    result = dict(lambda_value=float(lam), objective=value, state=root.x,
        predicted=predicted, misfit=misfit, primal_residual_l2=residual_norm,
        primal_updates=len(root.step_lengths), primal_residual_history=root.residuals,
        data_rms=float(np.sqrt(np.mean(misfit**2))))
    if gradient:
        matrix = bratu_jacobian(root.x, lam)
        parameter = -np.exp(root.x)
        q = h.T@(weights*misfit)
        explicit = float(gamma*(lam-prior))
        total, p = adjoint_gradient(matrix, parameter, q, explicit)
        adjoint_residual = np.einsum('ji,j->i', matrix, p)-q
        result.update(gradient=total, adjoint=p, objective_state=q,
            explicit_gradient=explicit,
            adjoint_residual_l2=float(np.linalg.norm(adjoint_residual)),
            adjoint_residual_relative_l2=float(np.linalg.norm(adjoint_residual)/max(np.linalg.norm(q),1e-300)))
    return result


def fit_parameter(n, data, initial, positions=POSITIONS, weights=None,
                  bounds=BOUNDS, gamma=0., prior=0., primal_tolerance=1e-10,
                  gradient_tolerance=1e-10, maxiter=300, initial_step=10.):
    """Projected gradient descent with Armijo backtracking on the adjoint gradient.

    Projected-gradient norm uses a unit step. Stopping at an active bound is a
    constrained stationary point, not proof of recovering the generating truth.
    All evaluations, including rejected trial solves, use the same primal controls.
    """
    h, _, _ = _specification(n, data, positions, weights, gamma, prior)
    bounds = np.asarray(bounds, dtype=float)
    if (bounds.shape != (2,) or not np.all(np.isfinite(bounds)) or bounds[0] <= 0
            or bounds[1] >= 3.5 or bounds[0] >= bounds[1]):
        raise ValueError('Use ordered positive bounds below 3.5 on the tested lower branch')
    if not np.isfinite(initial) or not bounds[0] <= initial <= bounds[1]:
        raise ValueError('Initial parameter must lie inside the bounds')
    if (not np.isfinite(gradient_tolerance) or gradient_tolerance <= 0
            or not isinstance(maxiter, (int, np.integer)) or maxiter < 1
            or not np.isfinite(initial_step) or initial_step <= 0):
        raise ValueError('Positive optimization controls required')
    if not np.any(h) and gamma == 0:
        raise ValueError('Boundary-only observations contain no information about lambda')
    lam, evaluations, history = float(initial), 0, []
    current = evaluate(n, lam, data, positions, weights, gamma, prior, primal_tolerance)
    evaluations += 1
    for iteration in range(maxiter+1):
        g = current['gradient']
        projected = float(abs(lam-np.clip(lam-g, *bounds)))
        history.append(dict(iteration=iteration, lambda_value=lam,
            objective=current['objective'], gradient=g, projected_gradient=projected,
            primal_residual_l2=current['primal_residual_l2'],
            adjoint_residual_l2=current['adjoint_residual_l2'],
            adjoint_residual_relative_l2=current['adjoint_residual_relative_l2']))
        if projected <= gradient_tolerance:
            return dict(converged=True, reason='projected adjoint-gradient tolerance',
                lambda_value=lam, history=history, evaluations=evaluations, result=current)
        if iteration == maxiter:
            break
        step = float(initial_step)
        for backtrack in range(50):
            candidate = float(np.clip(lam-step*g, *bounds))
            displacement = candidate-lam
            trial = evaluate(n, candidate, data, positions, weights, gamma, prior, primal_tolerance)
            evaluations += 1
            if trial['objective'] <= current['objective']+1e-4*g*displacement:
                history[-1].update(accepted_step=step, backtracks=backtrack,
                    parameter_step=displacement, armijo_rhs=current['objective']+1e-4*g*displacement)
                lam, current = candidate, trial
                break
            step *= .5
        else:
            return dict(converged=False, reason='Armijo line search failed',
                lambda_value=lam, history=history, evaluations=evaluations, result=current)
    return dict(converged=False, reason='optimization iteration limit',
        lambda_value=lam, history=history, evaluations=evaluations, result=current)


def golden_reference(n, data, positions=POSITIONS, weights=None, bounds=BOUNDS,
                     gamma=0., prior=0., primal_tolerance=1e-10, width_tolerance=1e-8):
    """Independent scalar objective-only reference; no adjoint or state derivative.

    Golden section assumes a unimodal objective on the supplied bracket. The
    exhibit checks its sampled landscape; this is not a global optimality proof.
    """
    a, b = map(float, bounds)
    if not (0 < a < b < 3.5 and np.isfinite(width_tolerance) and width_tolerance > 0):
        raise ValueError('Invalid bounded reference controls')
    ratio = (np.sqrt(5.)-1)/2
    c, d = b-ratio*(b-a), a+ratio*(b-a)
    def value(lam):
        return evaluate(n, lam, data, positions, weights, gamma, prior,
                        primal_tolerance, gradient=False)['objective']
    fc, fd, evaluations = value(c), value(d), 2
    for _ in range(200):
        if b-a <= width_tolerance:
            lam = (a+b)/2
            return dict(lambda_value=lam, objective=value(lam),
                interval_width=b-a, evaluations=evaluations+1)
        if fc < fd:
            b, d, fd = d, c, fc
            c = b-ratio*(b-a); fc = value(c)
        else:
            a, c, fc = c, d, fd
            d = a+ratio*(b-a); fd = value(d)
        evaluations += 1
    raise RuntimeError('Golden-section reference iteration limit')
