"""Small original inverse-BFGS and vector-only L-BFGS control solvers."""
import numpy as np
from scipy.optimize import minimize

from support import classify_library, relative_error


def quadratic(x):
    x = np.asarray(x, dtype=float)
    star = np.array([1., -1., 1., -1., 1., -1., 1., -1.])
    a = np.diag([1., 2., 4., 8., 16., 32., 64., 128.]) + np.ones((8, 8)) / 16.
    error = x - star
    gradient = np.einsum('ij,j->i', a, error)
    return float(.5 * np.dot(error, gradient)), gradient


def rosenbrock(x):
    x, y = np.asarray(x, dtype=float)
    return float(100. * (y - x*x)**2 + (1. - x)**2), np.array([
        -400.*x*(y - x*x) + 2.*(x - 1.), 200.*(y - x*x)])


def positive_curvature(s, y):
    sy = float(np.dot(s, y))
    guard = 64. * np.finfo(float).eps * float(np.linalg.norm(s)) * float(np.linalg.norm(y))
    return sy > guard, sy, guard


def inverse_bfgs(h, s, y, retainer=None):
    okay, sy, _ = positive_curvature(s, y)
    if not okay:
        raise ValueError('Nonpositive or unresolved curvature')
    rho = 1. / sy
    v = np.eye(len(s)) - rho * np.outer(s, y)
    raw = np.einsum('ij,jk,lk->il', v, h, v) + rho * np.outer(s, s)
    if retainer:
        retainer.raw('raw-inverse-bfgs-before-symmetry-diagnostic', inverse_hessian=raw)
    antisymmetry = float(np.linalg.norm(raw - raw.T) / max(np.linalg.norm(raw), 1e-300))
    return .5 * (raw + raw.T), antisymmetry


def current_scaling(pairs):
    if not pairs:
        return 1.
    s, y = pairs[-1]
    okay, sy, _ = positive_curvature(s, y)
    if not okay:
        raise ValueError('Invalid newest pair')
    return float(sy / np.dot(y, y))


def lbfgs_action(gradient, pairs):
    """Vector-only two loops; no dense primary inverse matrix is formed."""
    if len(pairs) > 3:
        raise ValueError('At most three retained pairs')
    q = np.asarray(gradient, dtype=float).copy()
    alphas = []
    for s, y in reversed(pairs):
        okay, sy, _ = positive_curvature(s, y)
        if not okay:
            raise ValueError('Invalid retained curvature')
        alpha = float(np.dot(s, q) / sy)
        alphas.append(alpha)
        q -= alpha * y
    r = current_scaling(pairs) * q
    for (s, y), alpha in zip(pairs, reversed(alphas)):
        beta = float(np.dot(y, r) / np.dot(y, s))
        r += s * (alpha - beta)
    return -r


def dense_retained_action(gradient, pairs):
    """Independent expanded updates, CURRENT scaling and retained pairs only."""
    if len(pairs) > 3:
        raise ValueError('Dense oracle receives only the currently retained pairs')
    h = current_scaling(pairs) * np.eye(len(gradient))
    for s, y in pairs:
        sy = float(np.dot(s, y))
        hy = np.einsum('ij,j->i', h, y)
        yhy = float(np.dot(y, hy))
        h = (h - (np.outer(hy, s) + np.outer(s, hy)) / sy
             + (1. + yhy / sy) * np.outer(s, s) / sy)
    return -np.einsum('ij,j->i', h, gradient)


class Objective:
    def __init__(self, function, retainer):
        self.function, self.retainer = function, retainer
        self.calls = 0
        self.last_x = self.last = None

    def at(self, x):
        x = np.asarray(x, dtype=float)
        if self.last_x is not None and np.array_equal(x, self.last_x):
            return self.last
        self.retainer.raw('objective-requested', x=x)
        self.calls += 1
        value, gradient = self.function(x)
        self.retainer.raw('objective-completed-before-further-work', x=x,
                          objective=value, gradient=gradient, objective_calls=self.calls)
        if not np.isfinite(value) or not np.all(np.isfinite(gradient)):
            raise ValueError('Nonfinite objective or gradient')
        self.last_x, self.last = x.copy(), (float(value), np.asarray(gradient, dtype=float).copy())
        return self.last


def strong_wolfe(objective, x, f0, g0, direction, controls):
    """Bracketing and bisection zoom, no Armijo-only fallback."""
    c1, c2 = controls['strong_wolfe_c1'], controls['strong_wolfe_c2']
    slope0 = float(np.dot(g0, direction))
    if not slope0 < 0:
        raise ValueError('A descent direction is required')
    trials = []

    def evaluate(alpha):
        f, g = objective.at(x + alpha * direction)
        slope = float(np.dot(g, direction))
        trials.append(dict(alpha=alpha, objective=f, slope=slope))
        objective.retainer.raw('line-search-completed-before-decision',
                                alpha=alpha, objective=f, slope=slope)
        return f, g, slope

    def zoom(low, high, flow):
        for _ in range(int(controls['max_zoom_iterations'])):
            alpha = .5 * (low + high)
            if alpha == low or alpha == high:
                break
            f, g, slope = evaluate(alpha)
            if f > f0 + c1 * alpha * slope0 or f >= flow:
                high = alpha
            else:
                if abs(slope) <= -c2 * slope0:
                    return alpha, f, g, trials
                if slope * (high - low) >= 0:
                    high = low
                low, flow = alpha, f
        raise RuntimeError('STRONG_WOLFE_ZOOM_BUDGET_EXHAUSTED')

    previous, fprevious, alpha = 0., f0, float(controls['first_trial'])
    for iteration in range(int(controls['max_bracket_iterations'])):
        f, g, slope = evaluate(alpha)
        if f > f0 + c1 * alpha * slope0 or (iteration > 0 and f >= fprevious):
            return zoom(previous, alpha, fprevious)
        if abs(slope) <= -c2 * slope0:
            return alpha, f, g, trials
        if slope >= 0:
            return zoom(alpha, previous, f)
        previous, fprevious, alpha = alpha, f, 2. * alpha
    raise RuntimeError('STRONG_WOLFE_BRACKET_BUDGET_EXHAUSTED')


def own_quasi_newton(function, initial, method, controls, retainer):
    if method not in ('bfgs', 'lbfgs-m3'):
        raise ValueError('Original BFGS or L-BFGS required')
    obj = Objective(function, retainer)
    x = np.asarray(initial, dtype=float).copy()
    h = np.eye(len(x)) if method == 'bfgs' else None
    pairs, history, steps, oracle_actions = [], [], [], 0
    maxiter = controls['bfgs_maxiter'] if method == 'bfgs' else controls['lbfgs_maxiter']
    reason = 'BUDGET_EXHAUSTED'
    for iteration in range(int(maxiter) + 1):
        f, g = obj.at(x)
        row = dict(iteration=iteration, parameters=x.copy(), objective=f,
                   gradient_inf=float(np.linalg.norm(g, ord=np.inf)),
                   objective_calls=obj.calls, stored_pairs=len(pairs), scaling=current_scaling(pairs))
        row.update(primary_inverse_matrix_scalars=len(x)**2 if method=='bfgs' else 0,
                   primary_retained_pair_scalars=2*len(x)*len(pairs),
                   reference_dense_matrix_scalars=len(x)**2 if method=='lbfgs-m3' else 0)
        history.append(row)
        retainer.raw('quasi-newton-current-before-step', **row)
        if row['gradient_inf'] <= controls['gradient_stop_inf']:
            reason = 'PHYSICAL_GRADIENT_TOLERANCE'
            break
        if iteration == int(maxiter):
            break
        if method == 'bfgs':
            direction = -np.einsum('ij,j->i', h, g)
            defect = 0.
        else:
            direction = lbfgs_action(g, pairs)
            oracle = dense_retained_action(g, pairs)
            oracle_actions += 1
            retainer.raw('lbfgs-directions-before-comparison', direction=direction,
                          oracle_direction=oracle, retained_s=[s for s, _ in pairs],
                          retained_y=[y for _, y in pairs], current_scaling=current_scaling(pairs))
            defect = relative_error(direction, oracle)
        alpha, new_f, new_g, trials = strong_wolfe(obj, x, f, g, direction, controls)
        new_x = x + alpha * direction
        s, y = new_x - x, new_g - g
        retainer.raw('quasi-newton-completed-step-before-update', parameters=new_x,
                      objective=new_f, gradient=new_g, step=s, gradient_change=y,
                      line_trials=trials)
        okay, sy, guard = positive_curvature(s, y)
        if not okay:
            reason = 'CURVATURE_FAILURE'
            # Keep the completed candidate while retaining the last updated iterate.
            break
        antisymmetry = 0.
        minimum_eigenvalue = 1.
        if method == 'bfgs':
            h, antisymmetry = inverse_bfgs(h, s, y, retainer)
            retainer.raw('inverse-bfgs-completed-before-eigenvalue', inverse_hessian=h)
            minimum_eigenvalue = float(np.linalg.eigvalsh(h)[0])
        else:
            pairs = (pairs + [(s.copy(), y.copy())])[-3:]
        slope0 = float(np.dot(g, direction))
        slope1 = float(np.dot(new_g, direction))
        steps.append(dict(alpha=alpha, wolfe_armijo=bool(new_f <= f + controls['strong_wolfe_c1'] * alpha * slope0),
                          wolfe_curvature=bool(abs(slope1) <= -controls['strong_wolfe_c2'] * slope0),
                          curvature=sy, curvature_guard=guard, inverse_antisymmetry=antisymmetry,
                          minimum_eigenvalue=minimum_eigenvalue, dense_direction_relative=defect,
                          retained_pairs=len(pairs), line_trials=len(trials)))
        x = new_x
    f, g = obj.at(x)
    return dict(parameters=x, objective=f, gradient=g, history=history,
                steps=steps, reason=reason, converged=reason == 'PHYSICAL_GRADIENT_TOLERANCE',
                objective_calls=obj.calls, library_success=None, library_status=None,
                library_message=None, nfev=None, njev=None, dense_oracle_actions=oracle_actions,
                primary_inverse_matrix_scalars=len(x)**2 if method=='bfgs' else 0,
                maximum_retained_pair_scalars=max((r['primary_retained_pair_scalars'] for r in history),default=0),
                reference_dense_matrix_scalars=len(x)**2 if method=='lbfgs-m3' else 0)


def library_quasi_newton(function, initial, method, controls, retainer):
    if method not in ('scipy-bfgs', 'scipy-lbfgsb-unbounded'):
        raise ValueError('Explicit library companion required')
    objective, history = Objective(function, retainer), []
    initial_f, initial_g = objective.at(initial)
    history.append(dict(parameters=np.asarray(initial).copy(), objective=initial_f,
                        gradient_inf=float(np.linalg.norm(initial_g, ord=np.inf)),
                        objective_calls=objective.calls, stored_pairs=0))

    def callback(x):
        f, g = objective.at(x)
        history.append(dict(parameters=np.asarray(x).copy(), objective=f,
                            gradient_inf=float(np.linalg.norm(g, ord=np.inf)),
                            objective_calls=objective.calls, stored_pairs=0))
        retainer.raw('library-completed-iterate', **history[-1])

    if method == 'scipy-bfgs':
        answer = minimize(objective.at, initial, method='BFGS', jac=True, callback=callback,
                          options=dict(gtol=1e-8, norm=np.inf, maxiter=200, c1=1e-4, c2=.9))
    else:
        answer = minimize(objective.at, initial, method='L-BFGS-B', jac=True, bounds=None,
                          callback=callback, options=dict(maxcor=3, maxls=30, maxiter=500,
                                                         maxfun=20000, gtol=1e-8, ftol=1e-15))
    retainer.raw('library-answer-before-final-diagnostics', parameters=answer.x,
                  objective=answer.fun, gradient=answer.jac, success=answer.success,
                  status=answer.status, message=answer.message, nfev=answer.nfev, njev=answer.njev)
    f, g = objective.at(answer.x)
    return dict(parameters=np.asarray(answer.x), objective=f, gradient=g,
                history=history, steps=[], reason=classify_library(answer, np.linalg.norm(g, ord=np.inf) <= 1e-6),
                converged=bool(answer.success), objective_calls=objective.calls,
                library_success=bool(answer.success), library_status=int(answer.status),
                library_message=str(answer.message), nfev=int(answer.nfev), njev=int(answer.njev),
                dense_oracle_actions=0, primary_inverse_matrix_scalars=None,
                maximum_retained_pair_scalars=None, reference_dense_matrix_scalars=0)
