"""Explicit GN/LM and bounded/unbounded library adapters on fixed residuals."""
import numpy as np
from scipy.optimize import least_squares

from legacy.numart import bratu_multinverse as legacy
from model import canonical_box
from support import classify_library, projected_gradient


def own_least_squares(model, method, initial, scales, controls):
    if method not in ('gn', 'lm'):
        raise ValueError('Own GN or unbounded LM required')
    d = np.asarray(scales, dtype=float)
    if d.shape != (2,) or np.any(d <= 0) or not np.all(np.isfinite(d)):
        raise ValueError('Finite positive parameter scales required')
    z = (np.asarray(initial, dtype=float) - model.prior) / d
    mu = float(controls['lm_initial_mu'])
    history, accepted, attempted, linear_solves = [], [], 0, 0
    reason = 'BUDGET_EXHAUSTED'
    for iteration in range(int(controls['maxiter']) + 1):
        theta = model.prior + d * z
        r, jac, value = model.augmented(theta)
        jz = jac * d[None, :]
        gtheta = value['gradient']
        stationarity = float(np.linalg.norm(gtheta, ord=np.inf))
        history.append(dict(iteration=iteration, parameters=theta.copy(),
                            objective=value['objective'], stationarity=stationarity,
                            damping_mu=mu, forward_calls=model.retainer.forward_calls))
        model.retainer.raw('least-squares-current-before-step', **history[-1])
        if stationarity <= float(controls['physical_gradient_inf_stop']):
            reason = 'PHYSICAL_GRADIENT_TOLERANCE'
            break
        if iteration == int(controls['maxiter']):
            break
        max_trials = int(controls['gn_backtracks'] if method == 'gn' else
                         controls['lm_max_rejected_steps_per_iteration'])
        if method == 'gn':
            # One unchanged GN system per outer iterate; backtracking only scales its step.
            direction = np.linalg.lstsq(jz, -r, rcond=None)[0]
            linear_solves += 1
            model.retainer.raw('gn-direction-before-backtracking', direction=direction)
        for trial in range(max_trials):
            if method == 'gn':
                step = (0.5 ** trial) * direction
            else:
                step = np.linalg.lstsq(np.vstack((jz, np.sqrt(mu) * np.eye(2))),
                                      np.concatenate((-r, np.zeros(2))), rcond=None)[0]
                linear_solves += 1
            trial_theta = model.prior + d * (z + step)
            attempted += 1
            linear_image = np.einsum('ij,j->i', jz, step)
            scaled_gradient = np.einsum('ij,i->j', jz, r)
            predicted = float(-np.dot(scaled_gradient, step) - .5 * np.dot(linear_image, linear_image))
            model.retainer.raw('least-squares-trial-before-forward', method=method,
                              iteration=iteration, trial=trial, parameters=trial_theta,
                              z_step=step, damping_mu=mu, predicted_reduction=predicted)
            try:
                # Validate only the mathematical forward domain, not inference bounds.
                legacy._theta(trial_theta)
            except ValueError as error:
                model.retainer.raw('rejected-forward-domain', error=str(error))
                if method == 'lm':
                    mu *= 2.
                continue
            trial_value = model.at(trial_theta)
            actual = float(value['objective'] - trial_value['objective'])
            gain = actual / predicted if predicted > 0 else None
            if method == 'gn':
                rhs = value['objective'] + float(controls['gn_armijo']) * float(np.dot(gtheta, d * step))
                take = bool(trial_value['objective'] <= rhs)
            else:
                take = bool(predicted > 0 and actual > 0 and gain > float(controls['lm_gain_accept']))
            model.retainer.raw('least-squares-trial-decision', accepted=take,
                              actual_reduction=actual, predicted_reduction=predicted,
                              gain_ratio=gain, damping_mu=mu)
            if take:
                accepted.append(dict(parameters=trial_theta.copy(), objective=trial_value['objective'],
                                     damping_mu=mu, gain_ratio=gain, trial=trial))
                z = z + step
                if method == 'lm':
                    if gain > .75:
                        mu /= 3.
                    elif gain < .25:
                        mu *= 2.
                break
            if method == 'lm':
                mu *= 2.
        else:
            reason = 'LINE_SEARCH_FAILURE' if method == 'gn' else 'DAMPING_TRIAL_BUDGET_EXHAUSTED'
            break
    final = model.at(model.prior + d * z)
    return dict(parameters=final['parameters'], result=final, history=history,
                accepted_steps=accepted, reason=reason,
                converged=reason == 'PHYSICAL_GRADIENT_TOLERANCE',
                attempted_steps=attempted, library_success=None, library_status=None,
                library_message=None, nfev=None, njev=None, linear_subproblem_solves=linear_solves)


def library_least_squares(model, method, initial, scales, box, controls):
    if method not in ('scipy-trf', 'scipy-lm'):
        raise ValueError('Explicit SciPy TRF or unbounded LM required')
    d = np.asarray(scales, dtype=float)
    lo, hi, _ = canonical_box(box)
    z0 = (np.asarray(initial, dtype=float) - model.prior) / d
    history = []

    def fun(z):
        theta = model.prior + d * z
        model.retainer.raw('library-residual-requested', parameters=theta, method=method)
        r, _, value = model.augmented(theta)
        history.append(dict(parameters=theta.copy(), objective=value['objective'],
                            forward_calls=model.retainer.forward_calls))
        return r

    def jac(z):
        return model.augmented(model.prior + d * z)[1] * d[None, :]

    kwargs = dict(jac=jac, ftol=float(controls['least_squares_ftol']),
                  xtol=float(controls['least_squares_xtol']),
                  gtol=float(controls['least_squares_gtol']), max_nfev=int(controls['max_nfev']))
    if method == 'scipy-lm':
        answer = least_squares(fun, z0, method='lm', **kwargs)
    else:
        answer = least_squares(fun, z0, method='trf',
                               bounds=((lo - model.prior) / d, (hi - model.prior) / d),
                               x_scale=1., **kwargs)
    model.retainer.raw('library-answer-before-final-diagnostics', parameters=model.prior + d * answer.x,
                      success=answer.success, status=answer.status, message=answer.message,
                      fun=answer.fun, jac=answer.jac, nfev=answer.nfev, njev=answer.njev)
    value = model.at(model.prior + d * answer.x)
    measure = (float(np.linalg.norm(value['gradient'], ord=np.inf)) if method == 'scipy-lm' else
               projected_gradient(value['parameters'], value['gradient'], lo, hi))
    return dict(parameters=value['parameters'], result=value, history=history,
                accepted_steps=[], converged=bool(answer.success),
                reason=classify_library(answer, measure <= 1e-7),
                attempted_steps=len(history), library_success=bool(answer.success),
                library_status=int(answer.status), library_message=str(answer.message),
                nfev=int(answer.nfev), njev=int(answer.njev) if answer.njev is not None else None)


def legacy_projected(model, initial, box, controls):
    _, _, pairs = canonical_box(box)
    answer = legacy.fit_parameters(model.n, model.data, initial,
                                   positions=model.positions, weights=model.weights,
                                   gamma=model.gamma, prior=model.prior, bounds=pairs,
                                   metric=controls['metric'], primal_tolerance=1e-10,
                                   gradient_tolerance=controls['gradient_tolerance'],
                                   maxiter=controls['maxiter'], initial_step=controls['initial_step'])
    model.retainer.raw('legacy-fit-completed-before-further-work', **answer)
    value = model.at(answer['parameters'])
    history = [{**row, 'stationarity': row['projected_gradient_inf']} for row in answer['history']]
    return dict(parameters=value['parameters'], result=value, history=history,
                accepted_steps=[], converged=bool(answer['converged']), reason=str(answer['reason']),
                attempted_steps=answer['evaluations'], library_success=None, library_status=None,
                library_message=None, nfev=None, njev=None)
