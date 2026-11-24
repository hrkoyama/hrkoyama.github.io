"""Vector BE/BDF2/SDIRK2 with real stage residuals and scoped factor reuse."""
import math
import numpy as np
from scipy.linalg import lu_factor, lu_solve

GAMMA = 1-1/math.sqrt(2)


class StageFailure(RuntimeError):
    def __init__(self, reason, context):
        super().__init__(reason)
        self.context = context


def counters():
    return dict(rhs=0, jacobian=0, factorizations=0, linear_solves=0,
                newton_updates=0, line_search_rejections=0, stage_failures=0,
                completed_stages=0, maximum_completed_stage_residual=0.0,
                minimum_completed_stage_value=None, maximum_completed_stage_abs=0.0)


def weighted_linf(value, weights):
    return float(np.max(np.abs(value)/weights))


def stage(rhs, jac, t, base, coefficient, guess, weights, config, work, observe=None):
    z = np.array(guess, dtype=float, copy=True)
    base = np.array(base, dtype=float, copy=True)
    weights = np.asarray(weights, dtype=float)
    if z.ndim != 1 or base.shape != z.shape or weights.shape != z.shape or np.any(weights <= 0):
        raise ValueError('Stage requires matching vectors and positive weights')
    tol = config['newton_scaled_residual_tolerance']
    maximum = config['newton_max_updates']
    lu = None

    def note(phase, **extra):
        if observe:
            observe(phase, time=float(t), coefficient=float(coefficient),
                    candidate=z.copy(), base=base.copy(), **extra)

    def residual(at, phase):
        if observe:
            observe(phase, time=float(t), coefficient=float(coefficient), candidate=at.copy(), base=base.copy())
        work['rhs'] += 1
        f = np.asarray(rhs(t, at))
        if f.shape != at.shape:
            if observe:observe('failed-data', candidate=at.copy(), raw_rhs=f.copy(), time=float(t))
            raise ValueError('Mismatched implicit RHS')
        r = at-base-coefficient*f
        if observe:observe('stage-rhs-evaluated', candidate=at.copy(), raw_rhs=f.copy(), residual=r.copy(), time=float(t), coefficient=float(coefficient), evaluation_role=phase)
        if not np.isfinite(f).all() or not np.isfinite(r).all():
            if observe:observe('failed-data', candidate=at.copy(), raw_rhs=f.copy(), residual=r.copy(), time=float(t))
            raise FloatingPointError('Nonfinite implicit RHS')
        return r, f

    def fail(reason, **context):
        work['stage_failures'] += 1
        note('failed-stage', reason=reason, **context)
        raise StageFailure(reason, {'time': float(t), 'candidate': z.copy(), 'base': base.copy(), **context})

    for update in range(maximum+1):
        try:
            r, fz = residual(z, 'before-rhs')
        except (FloatingPointError, ValueError, OverflowError) as exc:
            fail(type(exc).__name__+': '+str(exc))
        norm = weighted_linf(r, weights)
        note('true-stage-residual', residual=r.copy(), scaled_residual=norm, update=update)
        if not np.isfinite(z).all() or np.max(np.abs(z)) > config['state_bound']:
            fail('nonfinite or unbounded candidate', residual=r.copy())
        if norm <= tol:
            minimum = float(np.min(z))
            old_minimum = work['minimum_completed_stage_value']
            work['minimum_completed_stage_value'] = minimum if old_minimum is None else min(old_minimum, minimum)
            work['maximum_completed_stage_abs'] = max(work['maximum_completed_stage_abs'], float(np.max(np.abs(z))))
            work['completed_stages'] += 1
            work['maximum_completed_stage_residual'] = max(work['maximum_completed_stage_residual'], norm)
            return z, fz, norm
        if update == maximum:
            fail('fixed Newton update cap reached', residual=r.copy(), scaled_residual=norm)
        accepted = False
        for refresh_retry in range(2):
            if lu is None or update % 3 == 0 or refresh_retry:
                work['jacobian'] += 1
                matrix = np.eye(len(z))-coefficient*np.asarray(jac(t, z))
                note('before-factorization', matrix=matrix.copy(), residual=r.copy())
                work['factorizations'] += 1
                lu = lu_factor(matrix, overwrite_a=False, check_finite=True)
            work['linear_solves'] += 1
            correction = lu_solve(lu, -r, check_finite=True)
            note('linear-correction', correction=correction.copy(), residual=r.copy())
            alpha = 1.0
            for halves in range(config['newton_line_search_max_halvings']+1):
                trial = z+alpha*correction
                try:
                    rt, _ = residual(trial, 'line-search-before-rhs')
                    nt = weighted_linf(rt, weights)
                except (FloatingPointError, ValueError, OverflowError):
                    nt = math.inf
                if math.isfinite(nt) and nt <= (1-config['newton_armijo']*alpha)*norm:
                    z = trial
                    work['newton_updates'] += 1
                    accepted = True
                    note('accepted-newton-correction', alpha=alpha, update=update+1)
                    break
                work['line_search_rejections'] += 1
                alpha *= 0.5
            if accepted:
                break
        if not accepted:
            fail('fixed Armijo/refresh cap reached', residual=r.copy(), scaled_residual=norm)
    raise AssertionError('Unreachable stage loop')


def sdirk_step(rhs, jac, t, y, h, weights, config, work, observe=None):
    first, ffirst, _ = stage(rhs, jac, t+GAMMA*h, y, GAMMA*h, y, weights, config, work, observe)
    base = y+h*(1-GAMMA)*ffirst
    second, _, _ = stage(rhs, jac, t+h, base, GAMMA*h, first, weights, config, work, observe)
    return second


def fixed(rhs, jac, y0, weights, total, steps, method, config, observe=None):
    if type(steps) is not int or steps < 1 or method not in ('bdf2', 'sdirk2', 'be'):
        raise ValueError('Invalid fixed method or step count')
    y = np.array(y0, dtype=float, copy=True)
    times = np.arange(steps+1, dtype=float)*(total/steps)
    times[-1] = total
    values = [y.copy()]
    work = counters()
    for k in range(steps):
        h = total/steps
        if method == 'sdirk2':
            new = sdirk_step(rhs, jac, times[k], y, h, weights, config, work, observe)
        else:
            coefficient, base = h, y
            if method == 'bdf2' and k:
                coefficient, base = 2*h/3, (4*y-values[-2])/3
            new, _, _ = stage(rhs, jac, times[k+1], base, coefficient, y, weights, config, work, observe)
        if observe:
            observe('completed-step', time=float(times[k+1]), state=new.copy(), step=k+1)
        y = new
        values.append(y.copy())
    work.update(accepted_steps=steps, rejected_steps=0, attempted_steps=steps,
                factor_reuses=work['linear_solves']-work['factorizations'])
    return {'times': times, 'states': np.asarray(values), 'work': work}


def adaptive(rhs, jac, y0, weights, observations, config, adapt, tolerance_id, first_step, observe=None):
    y = np.array(y0, dtype=float, copy=True)
    observations = np.asarray(observations, dtype=float)
    if observations[0] != 0 or np.any(np.diff(observations) <= 0):
        raise ValueError('Strict fixed observations starting at zero required')
    controls = adapt[tolerance_id]
    rtol = controls['rtol']
    atol = controls['atol_scale']*np.asarray(weights)
    work = counters()
    accepted = rejected = attempts = 0
    times, values, obs_values, trials = [0.], [y.copy()], [y.copy()], []
    t, h = 0., float(first_step)
    for wanted in observations[1:]:
        while t < wanted:
            attempts += 1
            if attempts > adapt['max_trials']:
                raise RuntimeError('Fixed adaptive trial cap reached')
            step = min(h, wanted-t)
            if step <= 16*np.finfo(float).eps*max(1., abs(t)):
                raise RuntimeError('Adaptive step underflow')
            failure = None
            try:
                full = sdirk_step(rhs, jac, t, y, step, weights, config, work, observe)
                half = sdirk_step(rhs, jac, t, y, step/2, weights, config, work, observe)
                half = sdirk_step(rhs, jac, t+step/2, half, step/2, weights, config, work, observe)
                ratio = (half-full)/(3*(atol+rtol*np.maximum(np.abs(y), np.abs(half))))
                # Explicitly frozen RMS aggregate; Newton uses weighted L-infinity.
                error = float(np.sqrt(np.mean(ratio*ratio)))
            except StageFailure as exc:
                error, failure = math.inf, str(exc)
            good = math.isfinite(error) and error <= 1
            trials.append({'time': float(t), 'step': float(step), 'error_ratio': error if math.isfinite(error) else None,
                           'accepted': bool(good), 'stage_failure': failure})
            if good:
                t = float(wanted) if step == wanted-t else t+step
                y = half
                accepted += 1
                times.append(t)
                values.append(y.copy())
                if observe:
                    observe('completed-step', time=t, state=y.copy(), step=accepted)
            else:
                rejected += 1
            factor = adapt['factor_max'] if error == 0 else max(adapt['factor_min'], min(adapt['factor_max'], adapt['safety']*error**(-1/3)))
            h = step*factor
        obs_values.append(y.copy())
    work.update(accepted_steps=accepted, rejected_steps=rejected, attempted_steps=attempts,
                factor_reuses=work['linear_solves']-work['factorizations'])
    return {'times': np.asarray(times), 'states': np.asarray(values),
            'observation_states': np.asarray(obs_values), 'trials': trials, 'work': work}
