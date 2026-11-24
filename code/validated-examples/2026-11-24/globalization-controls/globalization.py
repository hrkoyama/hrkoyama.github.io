"""Finite Euclidean dogleg and Armijo controls; retain every attempted step."""
import numpy as np
from scipy.linalg import svd
from problems import DomainError, residual, jacobian, dot, norm, mv


def least_squares(a, f):
    u, s, vh = svd(a, full_matrices=False, check_finite=True)
    active = s > 1e-12*max(a.shape)*(s[0] if len(s) else 0.)
    coef = np.zeros_like(s)
    coef[active] = -np.einsum('ij,i->j', u[:, active], f)/s[active]
    return np.einsum('ij,i->j', vh, coef), s, int(np.sum(active))


def dogleg(a, f, delta):
    g = np.einsum('ij,i->j', a, f)
    if norm(g) == 0:
        return np.zeros(a.shape[1]), {'branch':'stationary', 'rank':None, 'singular_values':[]}
    ag = mv(a, g); denominator = dot(ag, ag)
    if not np.isfinite(denominator) or denominator <= 0:
        raise ArithmeticError('Degenerate Cauchy model')
    pb, s, rank = least_squares(a, f)
    pu = -(dot(g, g)/denominator)*g
    if norm(pu) >= delta:
        step = -delta*g/norm(g); branch = 'cauchy-boundary'
    elif norm(pb) <= delta:
        step = pb; branch = 'gauss-newton'
    else:
        direction = pb-pu; aa = dot(direction, direction)
        bb = 2*dot(pu, direction); cc = dot(pu, pu)-delta*delta
        if aa <= 0 or bb*bb-4*aa*cc < 0: raise ArithmeticError('Invalid dogleg intersection')
        # cc<0: positive quadratic root, stable for either sign of bb.
        disc = np.sqrt(bb*bb-4*aa*cc)
        t = (-2*cc/(bb+disc)) if bb >= 0 else ((-bb+disc)/(2*aa))
        if not 0 <= t <= 1: raise ArithmeticError('Dogleg segment escaped')
        step = pu+t*direction; branch = 'intermediate'
    return step, {'branch':branch, 'rank':rank, 'singular_values':s.tolist()}


def radius_update(delta, rho, pnorm):
    if rho < .25: return .25*delta
    if rho > .75 and pnorm >= .99*delta: return min(2*delta, 100.)
    return delta


def solve(kind, initial, scale, method, checkpoint=lambda *a, **k: None,
          max_iterations=80, max_trials=25):
    x = np.array(initial, dtype=float, copy=True); scale = np.asarray(scale, dtype=float)
    delta = 1.; history = []; counts = {'residual':0, 'jacobian':0, 'linear':0, 'trials':0}
    status = 'MAXITER'; current_f = None; current_j = None
    for iteration in range(max_iterations+1):
        checkpoint('before-current-residual', x=x, f=current_f, jacobian=current_j)
        counts['residual'] += 1
        try: f = residual(kind, x)
        except DomainError:
            status = 'DOMAIN_FAILURE'; break
        current_f = f
        if norm(f)/np.sqrt(len(f)) <= 1e-9:
            status = 'ROOT'; break
        if iteration == max_iterations: break
        checkpoint('before-jacobian', x=x, f=f)
        j = jacobian(kind, x); current_j = j
        counts['jacobian'] += 1
        ff = scale*f; a = scale[:, None]*j
        g = np.einsum('ij,i->j', a, ff); phi = .5*dot(ff, ff)
        checkpoint('before-model-solve', x=x, f=f, jacobian=j, scaled_f=ff, scaled_j=a, g=g)
        if norm(g) == 0:
            status = 'STATIONARY_NONROOT'; break
        if method != 'dogleg-trust-region':
            counts['linear'] += 1
            p, singular, rank = least_squares(a, ff)
            info = {'branch':'newton', 'rank':rank, 'singular_values':singular.tolist()}
            if method == 'armijo-newton' and dot(g, p) >= 0:
                status = 'NONDESCENT_DIRECTION'; break
        accepted = False
        for trial in range(max_trials if method != 'full-newton' else 1):
            old_delta = delta
            if method == 'dogleg-trust-region':
                counts['linear'] += 1; p, info = dogleg(a, ff, delta); alpha = 1.
            else: alpha = 2.**(-trial) if method == 'armijo-newton' else 1.
            step = alpha*p; candidate = x+step; counts['trials'] += 1
            checkpoint('before-trial-residual', x=x, f=f, jacobian=j, p=step, candidate=candidate)
            row = {'iteration':iteration, 'trial':trial, 'x':x.tolist(), 'candidate':candidate.tolist(),
                   'f':f.tolist(), 'phi':phi, 'step':step.tolist(), 'alpha':alpha,
                   'delta':old_delta, 'accepted':False, 'domain_rejected':False, **info}
            try:
                counts['residual'] += 1; candidate_f = residual(kind, candidate)
                trial_phi = .5*dot(scale*candidate_f, scale*candidate_f)
                ap = mv(a, step); pred = -dot(g, step)-.5*dot(ap, ap)
                direct = phi-.5*dot(ff+ap, ff+ap); actual = phi-trial_phi
                row.update(candidate_f=candidate_f.tolist(), trial_phi=trial_phi,
                           pred=pred, pred_direct=direct, actual=actual,
                           gp=dot(g, step), ap_norm=norm(ap), g_norm=norm(g))
                if not all(np.isfinite(row[k]) for k in ['trial_phi','pred','actual']):
                    raise ArithmeticError('Nonfinite finite-domain model')
                if method == 'dogleg-trust-region':
                    if pred <= 0:
                        row['rho'] = None; history.append(row); checkpoint('model-failure', x=x, candidate=candidate, f=f, jacobian=j, record=row)
                        return {'x':x.tolist(), 'f':f.tolist(), 'termination':'MODEL_FAILURE', 'history':history, 'counts':counts}
                    rho = actual/pred; row['rho'] = rho
                    accepted = actual > 0 and rho >= .1
                    delta = radius_update(delta, rho, norm(step))
                elif method == 'armijo-newton':
                    accepted = trial_phi <= phi+1e-4*dot(g, step)
                else: accepted = True
                row['accepted'] = bool(accepted)
            except DomainError:
                row['domain_rejected'] = True
                if method == 'dogleg-trust-region': delta *= .25
            row['delta_after'] = delta
            row['F_evaluations'] = counts['residual']; row['J_evaluations'] = counts['jacobian']
            row['model_solves'] = counts['linear']; history.append(row)
            checkpoint('trial-recorded', x=x, f=f, jacobian=j, candidate=candidate, record=row)
            if accepted:
                x = np.array(candidate, copy=True); break
            if method == 'dogleg-trust-region' and delta < 2.**-40:
                status = 'TRUST_RADIUS_EXHAUSTED'; break
        if not accepted:
            if status != 'TRUST_RADIUS_EXHAUSTED': status = 'TRIALS_EXHAUSTED'
            break
    checkpoint('solver-completed-before-diagnostics', x=x, f=current_f, jacobian=current_j)
    return {'x':x.tolist(), 'f':None if current_f is None else current_f.tolist(),
            'termination':status, 'history':history, 'counts':counts}
