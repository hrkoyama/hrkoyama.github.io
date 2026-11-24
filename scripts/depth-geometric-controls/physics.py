"""Small, independently authored scalar geometric maps; no execution on import."""
import math
import numpy as np


class EvolutionFailure(ArithmeticError):
    def __init__(self, message, **payload):
        super().__init__(message)
        self.payload = payload


def dot(a, b):
    return sum(float(x) * float(y) for x, y in zip(a, b))


def finite(*values):
    return all(math.isfinite(float(x)) for value in values for x in value)


def position(a, q, target, cap=8):
    """Solve the continuous eta branch, never project a completed state."""
    a, q = tuple(map(float, a)), tuple(map(float, q))
    eta, history = 0.0, []
    for update in range(cap + 1):
        candidate = (a[0] - eta*q[0], a[1] - eta*q[1])
        residual = (dot(candidate, candidate)-1.0)/2.0
        derivative = -dot(q, candidate)
        history.append((eta, residual, derivative))
        if not finite(candidate, (eta, residual, derivative)):
            raise EvolutionFailure('Nonfinite position solve', candidate=candidate,
                                   eta=eta, history=history)
        if abs(residual) <= target:
            if dot(q, candidate) <= 0:
                raise EvolutionFailure('Wrong constraint branch', candidate=candidate,
                                       eta=eta, history=history)
            return candidate, eta, residual, update, history
        if update == cap or abs(derivative) < 0.25:
            raise EvolutionFailure('Position target unmet or branch unsafe',
                                   candidate=candidate, eta=eta, history=history)
        eta -= residual/derivative
    raise AssertionError('Unreachable scalar solve')


def rattle_step(q, p, h, target, cap=8, omit_final=False):
    a = (q[0]+h*p[0], q[1]+h*p[1]-h*h/2)
    newq, eta, residual, updates, trace = position(a, q, target, cap)
    half = ((newq[0]-q[0])/h, (newq[1]-q[1])/h)
    bar = (half[0], half[1]-h/2)
    mu = 2*dot(newq, bar)/(h*dot(newq, newq))
    newp = bar if omit_final else (bar[0]-h*mu*newq[0]/2,
                                  bar[1]-h*mu*newq[1]/2)
    return newq, newp, (eta, 2*eta/(h*h), mu, residual, updates), trace


def pendulum(method, h, steps, target, theta0=.7, omega0=0.,
             initial=None, pair=None, checkpoint=None, cap=8):
    """SHAKE owns position pairs; RATTLE owns full-time q/p.

    Checkpoints contain current owned states only every256updates. Completed
    arrays are saved by the caller before diagnostics. Exceptions carry the
    accepted prefix and current candidate. SIGKILL can retain only checkpoints.
    """
    if method not in ('rattle', 'shake') or h == 0 or steps < 1:
        raise ValueError('Invalid constrained evolution')
    q0 = (math.sin(theta0), -math.cos(theta0))
    p0 = (omega0*math.cos(theta0), omega0*math.sin(theta0))
    if initial is not None:
        q0, p0 = tuple(initial[0]), tuple(initial[1])
    if pair is not None:
        previous, q0 = tuple(pair[0]), tuple(pair[1])
    q = np.empty((steps+1, 2)); q[0] = q0
    momentum = np.empty((steps+1, 2)) if method == 'rattle' else None
    if momentum is not None:
        momentum[0] = p0
    solves = np.empty((steps, 5 if method == 'rattle' else 4)); completed = 0
    current_q, current_p = tuple(q0), tuple(p0)
    attempted = {}
    def raw():
        result = dict(q=q[:completed+1].copy(), h=float(h),
                      steps_completed=completed, solves=solves[:completed].copy(),
                      times=np.arange(completed+1)*h)
        if momentum is not None:
            result['p'] = momentum[:completed+1].copy()
        return result
    try:
        for i in range(steps):
            attempted = dict(step=i, current_q=np.asarray(current_q))
            if method == 'rattle':
                attempted['current_p'] = np.asarray(current_p)
            if method == 'rattle':
                newq, newp, info, trace = rattle_step(current_q, current_p, h, target, cap)
            else:
                if i == 0 and pair is None:
                    newq, _, info, trace = rattle_step(current_q, current_p, h, target, cap)
                    info = (info[0], info[0]/(h*h), info[3], info[4])
                else:
                    a = (2*current_q[0]-previous[0],
                         2*current_q[1]-previous[1]-h*h)
                    newq, eta, residual, updates, trace = position(a, current_q, target, cap)
                    info = (eta, eta/(h*h), residual, updates)
                newp = current_p  # Not an asserted SHAKE momentum.
            previous = current_q
            current_q, current_p = tuple(newq), tuple(newp)
            q[i+1] = current_q; solves[i] = info
            if momentum is not None:
                momentum[i+1] = current_p
            completed = i+1
            if checkpoint is not None and (completed % 256 == 0 or completed == steps):
                checkpoint(dict(step=completed, q=np.asarray(current_q),
                                p=np.asarray(current_p) if momentum is not None else np.empty(0),
                                previous_q=np.asarray(previous)))
        return raw()
    except BaseException as error:
        payload = raw(); payload.update(attempted)
        if isinstance(error, EvolutionFailure):
            payload.update(error.payload)
        raise EvolutionFailure(str(error), **payload) from error


def acceleration(q):
    x, y = map(float, q); radius = math.hypot(x, y)
    if not math.isfinite(radius) or radius <= 0:
        raise EvolutionFailure('Unsoftened collision or nonfinite force', candidate=q)
    denominator = radius*radius*radius
    return (-x/denominator, -y/denominator)


def kepler_step(q, p, h):
    f = acceleration(q)
    half = (p[0]+h*f[0]/2, p[1]+h*f[1]/2)
    newq = (q[0]+h*half[0], q[1]+h*half[1])
    g = acceleration(newq)
    newp = (half[0]+h*g[0]/2, half[1]+h*g[1]/2)
    if not finite(newq, newp):
        raise EvolutionFailure('Nonfinite Kepler candidate', q=newq, p=newp)
    return newq, newp


def kepler(e, periods=1, steps_per_period=2048, variable=False,
           initial=None, schedule=None, backward=False, cap=50000,
           checkpoint=None):
    q, p = ((1-e, 0.), (0., math.sqrt((1+e)/(1-e)))) if initial is None else initial
    q, p = tuple(q), tuple(p)
    horizon = 2*math.pi*periods; direction = -1. if backward else 1.
    time = horizon if backward else 0.; endpoint = 0. if backward else horizon
    times, qs, ps, hs = [time], [q], [p], []
    n = steps_per_period*periods if not variable and schedule is None else cap
    if schedule is not None:
        n = len(schedule)
    attempted = {}
    def raw():
        return dict(times=np.asarray(times), q=np.asarray(qs), p=np.asarray(ps),
                    actual_h=np.asarray(hs), steps_completed=len(hs),
                    endpoint=float(endpoint))
    try:
        for i in range(n):
            if schedule is not None:
                h = float(schedule[i])
            elif variable:
                magnitude = min(2*math.pi/steps_per_period*math.hypot(*q),
                                abs(endpoint-time))
                h = direction*magnitude
            else:
                h = direction*2*math.pi/steps_per_period
            attempted = dict(step=i, current_q=np.asarray(q), current_p=np.asarray(p),
                             attempted_h=float(h), current_time=float(time))
            if h == 0:
                break
            q, p = kepler_step(q, p, h)
            if variable and schedule is None:
                time += h
            else:
                time = time+h if schedule is not None else times[0]+(i+1)*h
            times.append(time); qs.append(q); ps.append(p); hs.append(h)
            if checkpoint is not None and ((i+1) % 256 == 0):
                checkpoint(dict(step=i+1, q=np.asarray(q), p=np.asarray(p), time=float(time)))
            if variable and schedule is None and abs(endpoint-time) <= 1e-13:
                break
        if abs(endpoint-times[-1]) > 1e-12*(1+horizon):
            raise EvolutionFailure('Kepler endpoint/cap unmet', **attempted)
        return raw()
    except BaseException as error:
        payload = raw(); payload.update(attempted)
        if isinstance(error, EvolutionFailure):
            payload.update(error.payload)
        raise EvolutionFailure(str(error), **payload) from error


def coefficients(method, omega, alpha, h):
    h, omega, alpha = float(h), float(omega), float(alpha)
    theta = h*omega; sine, cosine = math.sin(theta), math.cos(theta)
    return dict(h=h, omega=omega, alpha=alpha, theta_evaluated=theta,
                half=h/2, cross=(h/2)*alpha,
                stiff=((h/2)*(omega*omega) if method == 'verlet' else 0.),
                sine=sine, cosine=cosine, sine_over_omega=sine/omega,
                omega_sine=omega*sine)


def coupled_step(z, method, c):
    q1, q2, p1, p2 = map(float, z); stages = []
    stages.append((q1, q2, p1, p2))
    p1 -= c['half']*q1+c['cross']*q2
    p2 -= c['cross']*q1+c['stiff']*q2
    stages.append((q1, q2, p1, p2))
    if method == 'verlet':
        q1 += c['h']*p1; q2 += c['h']*p2
    else:
        q1 += c['h']*p1
        q2, p2 = (c['cosine']*q2+c['sine_over_omega']*p2,
                  -c['omega_sine']*q2+c['cosine']*p2)
    stages.append((q1, q2, p1, p2))
    p1 -= c['half']*q1+c['cross']*q2
    p2 -= c['cross']*q1+c['stiff']*q2
    result = (q1, q2, p1, p2)
    if not finite(result):
        raise EvolutionFailure('Nonfinite coupled candidate', candidate=result,
                               stage_inputs=np.asarray(stages))
    return result, stages


def coupled(method, c, steps, norm_cap=1e40, checkpoint=None):
    z = (1., 1./c['omega'], 0., 0.)
    states = np.empty((steps+1, 4)); states[0] = z
    stages = np.empty((steps, 3, 4)); completed = 0
    try:
        for i in range(steps):
            z, stage = coupled_step(z, method, c)
            states[i+1] = z; stages[i] = stage; completed = i+1
            if math.sqrt(sum(x*x for x in z)) > norm_cap:
                raise EvolutionFailure('Coupled finite norm cap exceeded', candidate=z)
            if checkpoint is not None and (completed % 256 == 0):
                checkpoint(dict(step=completed, state=np.asarray(z)))
        return dict(states=states, stage_inputs=stages,
                    times=np.arange(steps+1)*c['h'], steps_completed=completed)
    except BaseException as error:
        payload = dict(states=states[:completed+1].copy(),
                       stage_inputs=stages[:completed].copy(),
                       steps_completed=completed, coefficients=c)
        if isinstance(error, EvolutionFailure):
            payload.update(error.payload)
        raise EvolutionFailure(str(error), **payload) from error
