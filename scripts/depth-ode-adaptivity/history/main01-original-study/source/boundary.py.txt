"""Actual nonperiodic nodal FD diffusion/reaction subflows; no reference import."""
import math
import numpy as np
from scipy.fft import dst, idst


def continuum(x, t):
    return np.cos(x-0.5)/math.cos(0.5)+0.1*math.exp((1-math.pi**2)*t)*np.sin(math.pi*x)


def semigroup_setup(n, htime, source):
    dx = 1/(n+1)
    eigen = -4*np.sin(math.pi*np.arange(1, n+1)/(2*(n+1)))**2/dx**2
    damping = np.exp(htime*eigen)
    forcing = np.expm1(htime*eigen)/eigen*dst(np.full(n, source), type=1, norm='ortho')
    def flow(w):
        return idst(damping*dst(w, type=1, norm='ortho')+forcing, type=1, norm='ortho')
    return flow


def integrate(row, observe=None):
    n, steps, final = row['n_interior'], row['steps'], row['final_time']
    if type(n) is not int or n < 2 or type(steps) is not int or steps < 4 or steps % 4:
        raise ValueError('Valid interior grid and quarter-observation step count required')
    x = np.arange(1, n+1)/(n+1)
    w = continuum(x, 0.)-1
    dt = final/steps
    corrected = row['method'] == 'strang-boundary-corrected'
    lie = row['method'] == 'lie-unmodified'
    if row['method'] not in ('strang-unmodified', 'strang-boundary-corrected', 'lie-unmodified'):
        raise ValueError('Unknown boundary composition')
    diffusion = semigroup_setup(n, dt if lie else dt/2, 1. if corrected else 0.)
    reaction_scale = math.exp(dt)
    reaction_source = 0. if corrected else math.expm1(dt)
    snapshots, saved_times = [w.copy()+1], [0.]
    for k in range(1, steps+1):
        w = diffusion(w)
        if observe:
            observe('boundary-after-diffusion', time=float(k*dt), state=w.copy(), step=k)
        w = reaction_scale*w+reaction_source
        if observe:
            observe('boundary-after-reaction', time=float(k*dt), state=w.copy(), step=k)
        if not lie:
            w = diffusion(w)
        if observe:
            observe('completed-step', time=float(k*dt), state=w.copy(), step=k)
        if not np.isfinite(w).all():
            raise FloatingPointError('Nonfinite split field')
        if k % (steps//4) == 0:
            snapshots.append(w.copy()+1)
            saved_times.append(final*k/steps)
    return {'x': x, 'times': np.array(saved_times), 'states': np.array(snapshots),
            'work': {'diffusion_calls': steps if lie else 2*steps, 'reaction_calls': steps},
            'boundary': {'prescribed_value': 1., 'reaction_trace_defect': 0. if corrected else math.expm1(dt),
                         'last_subflow_trace_defect': math.expm1(dt) if lie else 0.,
                         'trace_scope': 'Continuous subflow boundary trace; physical nodal interior unknowns are never reset/projected.'}}
