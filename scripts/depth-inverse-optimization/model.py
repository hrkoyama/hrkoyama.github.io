"""Legacy dense Bratu model with an explicit box adapter and raw observers."""
from contextlib import contextmanager

import numpy as np

from legacy.numart import bratu_multinverse as legacy


def canonical_box(spec):
    lo, hi = np.asarray(spec['lower'], dtype=float), np.asarray(spec['upper'], dtype=float)
    if lo.shape != (2,) or hi.shape != (2,) or not np.all(np.isfinite([lo, hi])) or np.any(lo >= hi):
        raise ValueError('Two finite lower/upper bound vectors required')
    pairs = np.column_stack((lo, hi))
    legacy._bounds(pairs)
    return lo, hi, pairs


@contextmanager
def observe_legacy(retainer):
    """Serial observation only; original functions and arithmetic stay intact."""
    original_residual, original_evaluate = legacy.residual, legacy.evaluate

    def residual(u, theta):
        retainer.raw('newton-residual-input', state=u, parameters=theta)
        return original_residual(u, theta)

    def evaluate(*args, **kwargs):
        theta = args[1] if len(args) > 1 else kwargs['theta']
        retainer.raw('forward-requested', parameters=theta)
        retainer.forward_calls += 1
        result = original_evaluate(*args, **kwargs)
        retainer.raw('forward-completed-before-further-work', **result)
        return result

    legacy.residual, legacy.evaluate = residual, evaluate
    try:
        yield
    finally:
        legacy.residual, legacy.evaluate = original_residual, original_evaluate


class BratuModel:
    def __init__(self, n, data, positions, weights, gamma, prior, retainer):
        self.n = int(n)
        self.data = np.asarray(data, dtype=float)
        self.positions = np.asarray(positions, dtype=float)
        self.weights = np.asarray(weights, dtype=float)
        self.gamma = float(gamma)
        self.prior = np.asarray(prior, dtype=float)
        self.retainer = retainer
        legacy._specification(self.n, self.data, self.positions, self.weights,
                              self.gamma, self.prior)
        self.h = legacy.observation_matrix(self.n, self.positions)
        self.last_theta = self.last = None

    def at(self, theta):
        theta = np.asarray(theta, dtype=float)
        if self.last_theta is not None and np.array_equal(theta, self.last_theta):
            return self.last
        self.retainer.raw('model-parameter-requested', parameters=theta)
        value = legacy.evaluate(self.n, theta, self.data, self.positions,
                                self.weights, self.gamma, self.prior, 1e-10)
        j, ft = legacy.derivatives(value['state'], theta)
        self.retainer.raw('state-and-derivatives-before-sensitivity',
                          parameters=theta, state=value['state'], jacobian=j, parameter_derivative=ft)
        sensitivity = np.linalg.solve(j, -ft)
        k = np.einsum('ij,jk->ik', self.h, sensitivity)
        value.update(data_jacobian=k, state_sensitivity=sensitivity,
                     sensitivity_residual_l2=float(np.linalg.norm(np.einsum('ij,jk->ik', j, sensitivity) + ft)))
        self.retainer.raw('sensitivity-completed-before-diagnostics', **value)
        self.last_theta, self.last = theta.copy(), value
        return value

    def augmented(self, theta):
        value = self.at(theta)
        root_weights = np.sqrt(self.weights)
        r = np.concatenate((root_weights * value['misfit'],
                            np.sqrt(self.gamma) * (np.asarray(theta) - self.prior)))
        jac = np.vstack((root_weights[:, None] * value['data_jacobian'],
                         np.sqrt(self.gamma) * np.eye(2)))
        return r, jac, value

    def rank(self, theta):
        value = self.at(theta)
        matrix = np.sqrt(self.weights)[:, None] * value['data_jacobian']
        singular = np.linalg.svd(matrix, compute_uv=False)
        singular = np.pad(singular, (0, 2 - len(singular)))
        rank = int(np.sum(singular > 1e-10 * singular[0])) if singular[0] else 0
        augmented = np.linalg.svd(np.vstack((matrix, np.sqrt(self.gamma) * np.eye(2))), compute_uv=False)
        return rank, singular, augmented
