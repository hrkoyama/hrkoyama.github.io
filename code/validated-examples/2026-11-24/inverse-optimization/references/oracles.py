"""Independent forward implementation with a shared, declared TRF optimizer."""
import numpy as np
from scipy.optimize import least_squares

from references.thomas import state_and_sensitivity
from support import projected_gradient


def context_specification(cfg, index, active_data):
    row = cfg['case65']['contexts'][index]
    if row['id'] == 'same-grid-clean':
        data = cfg['legacy_data']['same_grid_data']
    elif row['id'] == 'weighted-scaled-fine-noisy':
        data = cfg['legacy_data']['old_noisy_data']
    elif row['id'] == 'active-box':
        data = active_data
    elif row['id'] == 'one-center':
        data = [cfg['legacy_data']['same_grid_data'][2]]
    else:
        raise ValueError('Unreviewed least-squares context')
    positions = cfg['bratu']['positions'] if isinstance(row['positions'], str) else row['positions']
    weights = cfg['bratu']['weights'] if isinstance(row['weights'], str) else row['weights']
    return dict(id=row['id'], n=cfg['bratu']['n'], data=np.asarray(data, dtype=float),
                positions=np.asarray(positions, dtype=float), weights=np.asarray(weights, dtype=float),
                gamma=float(row['gamma']), prior=np.asarray(cfg['bratu']['prior'], dtype=float),
                scales=np.asarray(row['scales'], dtype=float), methods=row['methods'])


class ThomasObjective:
    def __init__(self, specification, retainer):
        self.specification, self.retainer = specification, retainer
        self.previous_theta = self.previous = None
        self.history = []

    def at(self, theta):
        theta = np.asarray(theta, dtype=float)
        if self.previous_theta is not None and np.array_equal(theta, self.previous_theta):
            return self.previous
        self.retainer.raw('independent-objective-requested', parameters=theta)
        s = self.specification
        state = state_and_sensitivity(s['n'], theta, s['positions'], self.retainer)
        misfit = state['predicted']-s['data']
        gamma, prior, weights = s['gamma'], s['prior'], s['weights']
        r = np.concatenate((np.sqrt(weights)*misfit, np.sqrt(gamma)*(theta-prior)))
        jac = np.vstack((np.sqrt(weights)[:, None]*state['data_jacobian'], np.sqrt(gamma)*np.eye(2)))
        gradient = np.einsum('ij,i->j', jac, r)
        value = dict(**state, parameters=theta.copy(), augmented_residual=r, augmented_jacobian=jac,
                     gradient=gradient, objective=float(.5*np.dot(r, r)))
        self.retainer.raw('independent-objective-completed-before-next-work', **value)
        self.history.append(dict(parameters=theta.copy(), objective=value['objective'], gradient=gradient))
        self.previous_theta, self.previous = theta.copy(), value
        return value


def fit_context(cfg, index, active_data, retainer):
    specification = context_specification(cfg, index, active_data)
    objective = ThomasObjective(specification, retainer)
    lo, hi = np.asarray(cfg['bratu']['box']['lower']), np.asarray(cfg['bratu']['box']['upper'])
    answer = least_squares(lambda theta: objective.at(theta)['augmented_residual'],
                           cfg['bratu']['initial'],
                           jac=lambda theta: objective.at(theta)['augmented_jacobian'],
                           method='trf', bounds=(lo, hi), ftol=1e-13, xtol=1e-13,
                           gtol=1e-13, max_nfev=200)
    retainer.raw('independent-library-answer-before-diagnostics', parameters=answer.x,
                  fun=answer.fun, jac=answer.jac, success=answer.success, status=answer.status,
                  message=answer.message, nfev=answer.nfev, njev=answer.njev)
    final = objective.at(answer.x)
    retainer.arrays('completed-fit', theta=answer.x, state=final['state'],
                    data_jacobian=final['data_jacobian'], gradient=final['gradient'],
                    raw_parameters=[row['parameters'] for row in objective.history],
                    raw_objectives=[row['objective'] for row in objective.history])
    return dict(**final, projected_gradient_inf=projected_gradient(answer.x, final['gradient'], lo, hi),
                library_success=bool(answer.success), library_status=int(answer.status),
                library_message=str(answer.message), nfev=int(answer.nfev), njev=int(answer.njev),
                initial_objective=objective.history[0]['objective'])
