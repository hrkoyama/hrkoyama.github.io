"""Bounded conservative 2D scalar FV rotation; not Zalesak's FCT algorithm.

For P1 reconstruction the average of four face midpoint values is the cell
mean. Each outgoing face Courant <=1/4 makes the upwind FE update a convex
combination of these values and incoming neighbor faces, because the discrete
velocity divergence is zero. SSPRK33 preserves that conditional bound.
"""
import numpy as np

STAGE_COLUMNS = ('step', 'stage', 'input_time', 'dt', 'courant',
                 'face_min', 'face_max', 'fe_min', 'fe_max',
                 'rk_min', 'rk_max', 'mean_preservation_defect',
                 'fe_mass_defect', 'rk_mass_defect')


class StageFailure(ArithmeticError):
    def __init__(self, message, state, context=None):
        super().__init__(message)
        self.state = np.array(state, copy=True)
        self.context = context or {}
        self.history = []


def minmod(a, b):
    """The smaller same-sign difference; this limits slopes, not cell means."""
    return np.where(a*b > 0, np.sign(a)*np.minimum(abs(a), abs(b)), 0.)


def flow(n, center=(.5, .5), omega=1.):
    if not isinstance(n, int) or n < 4:
        raise ValueError('Require integer n>=4')
    center = np.asarray(center, dtype=float)
    if center.shape != (2,) or not np.all(np.isfinite(center)):
        raise ValueError('Require a finite 2D rotation center')
    if not np.isfinite(omega) or omega == 0:
        raise ValueError('Require nonzero finite angular velocity')
    h = 1./n
    x = (np.arange(n)+.5)*h
    # These are exact normal face averages: u does not depend on x, v on y.
    u = np.broadcast_to(-omega*(x[:, None]-center[1]), (n, n))
    v = np.broadcast_to(omega*(x[None, :]-center[0]), (n, n))
    divergence = (u-np.roll(u, 1, axis=1)+v-np.roll(v, 1, axis=0))/h
    return dict(n=n, h=h, u=u, v=v, up=np.maximum(u, 0.),
                um=np.minimum(u, 0.), vp=np.maximum(v, 0.),
                vm=np.minimum(v, 0.), speed=float(max(abs(u).max(), abs(v).max())),
                divergence_max=float(abs(divergence).max()),
                center=center.copy(), omega=float(omega))


def check_state(q, bounds_tolerance, label):
    if not np.all(np.isfinite(q)):
        raise StageFailure(label+' contains nonfinite values', q)
    minimum, maximum = float(q.min()), float(q.max())
    if minimum < -bounds_tolerance or maximum > 1+bounds_tolerance:
        raise StageFailure(label+' exceeds the fixed [0,1] roundoff band', q,
                           {'minimum': minimum, 'maximum': maximum})
    return minimum, maximum


def reconstruct(q, method):
    if method == 'donor-cell':
        return q, q, q, q
    if method != 'muscl-minmod':
        raise ValueError('Unknown fixed reconstruction')
    sx = minmod(q-np.roll(q, 1, axis=1), np.roll(q, -1, axis=1)-q)
    sy = minmod(q-np.roll(q, 1, axis=0), np.roll(q, -1, axis=0)-q)
    return q-.5*sx, q+.5*sx, q-.5*sy, q+.5*sy


def forward_euler(q, f, dt, method='muscl-minmod', bounds_tolerance=5e-13):
    q = np.asarray(q, dtype=float)
    if q.shape != (f['n'], f['n']) or not np.isfinite(dt) or dt <= 0:
        raise ValueError('Require square means matching the flow and positive dt')
    if f['divergence_max'] != 0:
        raise ValueError('This fixed convexity proof requires zero discrete divergence')
    courant = dt*f['speed']/f['h']
    if courant > .25:
        raise ValueError('Individual-face sufficient Courant <=1/4 exceeded')
    check_state(q, bounds_tolerance, 'Stage input mean')
    left, right, down, up = reconstruct(q, method)
    face_min = min(float(x.min()) for x in (left, right, down, up))
    face_max = max(float(x.max()) for x in (left, right, down, up))
    if face_min < -bounds_tolerance or face_max > 1+bounds_tolerance:
        raise StageFailure('A reconstructed face exceeds the [0,1] band',
                           np.stack((left, right, down, up)))
    mean_defect = float(abs(.25*(left+right+down+up)-q).max())
    # Each interface has exactly one stored flux shared by its two cells.
    fx = f['up']*right+f['um']*np.roll(left, -1, axis=1)
    fy = f['vp']*up+f['vm']*np.roll(down, -1, axis=0)
    updated = q+dt/f['h']*(np.roll(fx, 1, axis=1)-fx
                              +np.roll(fy, 1, axis=0)-fy)
    minimum, maximum = check_state(updated, bounds_tolerance, 'FE candidate mean')
    mass_defect = float(abs(f['h']**2*(updated.sum()-q.sum())))
    return updated, dict(courant=float(courant), face_min=face_min, face_max=face_max,
                         fe_min=minimum, fe_max=maximum,
                         mean_preservation_defect=mean_defect,
                         fe_mass_defect=mass_defect)


def solve(initial, method='muscl-minmod', center=(.5, .5), final_time=2*np.pi,
          omega=1., face_courant=.2, bounds_tolerance=5e-13, max_steps=5000):
    initial = np.asarray(initial, dtype=float)
    if initial.ndim != 2 or initial.shape[0] != initial.shape[1]:
        raise ValueError('Require a square array of initial cell means')
    if not 0 < face_courant <= .25 or not np.isfinite(final_time) or final_time <= 0:
        raise ValueError('Require positive time and individual-face Courant<=1/4')
    f = flow(len(initial), center, omega)
    check_state(initial, bounds_tolerance, 'Initial mean')
    q = initial.copy()
    initial_mass = float(f['h']**2*q.sum())
    time, steps = 0., 0
    stage_rows = []
    snapshots, snapshot_times = [q.copy()], [0.]
    targets = np.linspace(0., final_time, 5)[1:]
    dt_nominal = face_courant*f['h']/f['speed']
    try:
        for target in targets:
            while time < target:
                if steps >= max_steps:
                    raise StageFailure('Fixed step budget exhausted', q)
                dt = min(dt_nominal, target-time)
                old = q.copy()
                one, a = forward_euler(old, f, dt, method, bounds_tolerance)
                candidate, b = forward_euler(one, f, dt, method, bounds_tolerance)
                two = .75*old+.25*candidate
                check_state(two, bounds_tolerance, 'Second SSP convex mean')
                candidate, c = forward_euler(two, f, dt, method, bounds_tolerance)
                q = old/3+(2./3)*candidate
                check_state(q, bounds_tolerance, 'Third SSP convex mean')
                for stage, stats, combined, fraction in zip(
                        (1, 2, 3), (a, b, c), (one, two, q), (0., 1., .5)):
                    row = dict(step=steps+1, stage=stage, input_time=time+fraction*dt,
                               dt=dt, rk_min=float(combined.min()),
                               rk_max=float(combined.max()),
                               rk_mass_defect=float(abs(f['h']**2*combined.sum()-initial_mass)),
                               **stats)
                    stage_rows.append([row[key] for key in STAGE_COLUMNS])
                steps += 1
                time = float(target) if dt == target-time else time+dt
            snapshots.append(q.copy());snapshot_times.append(time)
    except StageFailure as error:
        error.history = stage_rows
        raise
    return dict(q=q, initial=initial.copy(), snapshots=np.array(snapshots),
                snapshot_times=np.array(snapshot_times), time=time, steps=steps,
                stage_data=np.array(stage_rows), stage_columns=STAGE_COLUMNS,
                initial_mass=initial_mass, final_mass=float(f['h']**2*q.sum()),
                divergence_max=f['divergence_max'],
                state_clip_count=0, retries=0, rejected_steps=0)
