"""Own explicit DP5(4), accepted-state FSAL, quartic output and event ownership."""
import math
import numpy as np
from tableau import A, B, C, E, P


def rotation(t, y, gamma=0.2, omega=3.):
    return np.array([-gamma*y[0]-omega*y[1], omega*y[0]-gamma*y[1]])


def exact(t, gamma=0.2, omega=3.):
    t = np.asarray(t)
    return np.exp(-gamma*t)[..., None]*np.stack((np.cos(omega*t), np.sin(omega*t)), axis=-1)


class Segment:
    def __init__(self, t0, t1, y0, stages):
        self.t0, self.t1 = float(t0), float(t1)
        self.y0 = y0.copy()
        self.q = np.einsum('si,sj->ij', stages, P, optimize=False)

    def __call__(self, t):
        theta = (float(t)-self.t0)/(self.t1-self.t0)
        if theta < -2e-14 or theta > 1+2e-14:
            raise ValueError('No dense extrapolation outside accepted step')
        powers = np.array([theta, theta**2, theta**3, theta**4])
        return self.y0+(self.t1-self.t0)*np.einsum('ij,j->i', self.q, powers, optimize=False)


def step(rhs, t, y, f0, h, observe=None):
    k = np.zeros((7, len(y)))
    k[0] = f0
    for stage in range(1, 6):
        value = y+h*np.einsum('s,si->i', A[stage, :stage], k[:stage], optimize=False)
        if observe:
            observe('rk-before-rhs', time=float(t+C[stage]*h), candidate=value.copy(), stages=k.copy(), stage=stage)
        k[stage] = rhs(t+C[stage]*h, value)
    out = y+h*np.einsum('s,si->i', B, k[:6], optimize=False)
    if observe:
        observe('rk-before-rhs', time=float(t+h), candidate=out.copy(), stages=k.copy(), stage=6)
    k[6] = rhs(t+h, out)
    if not np.isfinite(k).all() or not np.isfinite(out).all():
        raise FloatingPointError('Nonfinite RK stage or output')
    error = h*np.einsum('s,si->i', E, k, optimize=False)
    return out, k[6].copy(), error, k


def root(segment, lo, hi, config):
    left, right = segment(lo)[0], segment(hi)[0]
    if left == 0:
        return float(lo), float(left), [float(lo), float(lo)], 0
    if right == 0:
        return float(hi), float(right), [float(hi), float(hi)], 0
    if left*right > 0:
        raise ValueError('Event requires an actual sign bracket')
    for count in range(1, config['max_iterations']+1):
        mid = lo+(hi-lo)/2
        value = float(segment(mid)[0])
        if value == 0 or hi-lo <= config['absolute_time_width']:
            return float(mid), value, [float(lo), float(hi)], count
        if (left < 0) == (value < 0):
            lo, left = mid, value
        else:
            hi, right = mid, value
    raise RuntimeError('Fixed event bisection cap reached')


def evaluate(segments, t):
    if not segments:
        raise ValueError('No accepted interpolation interval')
    ends = np.array([s.t1 for s in segments])
    index = int(np.searchsorted(ends, t, side='left'))
    if index == len(segments):
        raise ValueError('Observation beyond final accepted step')
    return segments[index](t)


def integrate(row, config, rhs=rotation, y0=None, observe=None):
    y = np.array(config['initial'] if y0 is None else y0, dtype=float, copy=True)
    final = float(row['final_time'])
    h = float(row['first_step'])
    if final <= 0 or h <= 0 or row['max_step'] <= 0 or not np.isfinite(y).all():
        raise ValueError('Finite initial state, positive interval and steps required')
    tol = config['tolerances'][row['tolerance_id']]
    controls = config['adaptivity']
    atol, rtol = np.array(tol['atol']), tol['rtol']
    t, f = 0., np.asarray(rhs(0., y))
    nfev = 1
    accepted = rejected = 0
    times, states, segments, attempts, roots = [0.], [y.copy()], [], [], []
    output_time, output_state, termination = None, None, None
    if y[0] == 0:
        roots.append({'time': 0., 'residual': 0., 'bracket': [0., 0.], 'iterations': 0, 'initial': True})
    for attempt in range(1, controls['max_trials']+1):
        h = min(h, row['max_step'], final-t)
        if h <= 16*np.finfo(float).eps*max(1., abs(t)):
            raise RuntimeError('RK45 step underflow')
        candidate, fend, error, stages = step(rhs, t, y, f, h, observe)
        nfev += 6
        ratio = error/(atol+rtol*np.maximum(np.abs(y), np.abs(candidate)))
        norm = float(np.sqrt(np.mean(ratio*ratio)))
        good = math.isfinite(norm) and norm < 1
        attempts.append({'time': float(t), 'step': float(h), 'error_ratio': norm,
                         'accepted': bool(good), 'nfev': nfev})
        if observe:
            observe('rk-trial-result', time=float(t), step=float(h), candidate=candidate.copy(),
                    accepted_state=y.copy(), accepted_start_rhs=f.copy(), endpoint_rhs=fend.copy(),
                    accepted=bool(good), error_ratio=norm, attempt=attempt)
        if not good:
            rejected += 1
            h *= max(controls['factor_min'], controls['safety']*norm**(-1/5))
            continue
        tn = min(final, t+h)
        segment = Segment(t, tn, y, stages)
        segments.append(segment)
        accepted += 1
        previous_rejected = attempt > 1 and not attempts[-2]['accepted']
        old_g, new_g = float(y[0]), float(candidate[0])
        direction = row['event_direction']
        crossing = ((old_g > 0 and new_g <= 0 and direction <= 0) or
                    (old_g < 0 and new_g >= 0 and direction >= 0))
        if crossing:
            rt, residual, bracket, count = root(segment, t, tn, config['event_root_solver'])
            if not roots or rt-roots[-1]['time'] > config['event_root_solver']['absolute_time_width']:
                roots.append({'time': rt, 'residual': residual, 'bracket': bracket,
                              'iterations': count, 'initial': False})
                if row['terminal']:
                    output_time, output_state = rt, segment(rt)
                    termination = 'terminal_event'
        t, y, f = tn, candidate, fend
        times.append(t)
        states.append(y.copy())
        if observe:
            observe('completed-step', time=float(t), state=y.copy(), rhs=f.copy(), step=accepted)
        if output_time is not None:
            break
        if t == final:
            output_time, output_state, termination = t, y.copy(), 'reached_fixed_final_time'
            break
        factor = controls['factor_max'] if norm == 0 else min(controls['factor_max'], controls['safety']*norm**(-1/5))
        if previous_rejected:
            factor = min(1., factor)
        h *= factor
    else:
        raise RuntimeError('Fixed RK45 trial cap reached')
    return {'times': np.array(times), 'states': np.array(states), 'segments': segments,
            'attempts': attempts, 'roots': roots, 'output_time': output_time, 'output_state': output_state,
            'termination': termination, 'work': {'nfev': nfev, 'attempted_steps': len(attempts),
            'accepted_steps': accepted, 'rejected_steps': rejected}}
