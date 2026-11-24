"""Diagnostics only; none of these routines advances a primary trajectory."""
import math
import numpy as np
from scipy.optimize import brentq


EPS = np.finfo(float).eps


def maxnorm(value):
    value = np.asarray(value)
    return float(np.max(np.sqrt(np.sum(value*value, axis=-1))))


def pendulum_fields(raw, method):
    q = raw['q']; h = float(raw['h'])
    constraint = (np.sum(q*q, axis=1)-1)/2
    if method == 'rattle':
        p, times, interior_q = raw['p'], raw['times'], q
    else:
        p = (q[2:]-q[:-2])/(2*h)
        times, interior_q = raw['times'][1:-1], q[1:-1]
    energy = np.sum(p*p, axis=1)/2+interior_q[:, 1]
    tangent = np.sum(interior_q*p, axis=1)
    result = dict(p=p, q=interior_q, times=times, constraint=constraint,
                  energy=energy, tangent=tangent)
    if method == 'shake':
        backward = q[1:-1]-q[:-2]; forward = q[2:]-q[1:-1]
        result['finite_C_identity'] = ((np.sum(backward*backward, axis=1)-
                                      np.sum(forward*forward, axis=1))/(4*h)+
                                     (constraint[2:]-constraint[:-2])/(2*h))
    return result


def reduced_coordinates(q, p):
    return np.array([math.atan2(float(q[0]), -float(q[1])),
                     float(q[0])*float(p[1])-float(q[1])*float(p[0])])


def reduced_map(step, state, h, target):
    theta, momentum = map(float, state)
    q = (math.sin(theta), -math.cos(theta))
    p = (momentum*math.cos(theta), momentum*math.sin(theta))
    newq, newp, _, _ = step(q, p, h, target)
    return reduced_coordinates(newq, newp)


def reduced_jacobian(step, state, h, target, delta):
    columns = []
    for j in range(2):
        plus, minus = np.array(state, float), np.array(state, float)
        plus[j] += delta; minus[j] -= delta
        columns.append((reduced_map(step, plus, h, target)-
                        reduced_map(step, minus, h, target))/(2*delta))
    return np.column_stack(columns)


def kepler_fields(raw):
    q, p = raw['q'], raw['p']
    r = np.sqrt(np.sum(q*q, axis=1))
    L = q[:, 0]*p[:, 1]-q[:, 1]*p[:, 0]
    energy = np.sum(p*p, axis=1)/2-1/r
    evec = np.column_stack((p[:, 1]*L, -p[:, 0]*L))-q/r[:, None]
    return dict(radius=r, angular=L, energy=energy, eccentricity_vector=evec,
                apsidal_angle=np.unwrap(np.arctan2(evec[:, 1], evec[:, 0])) )


def hermite_point(q0, q1, p0, p1, h, s):
    """Position and derivative with respect to local s, not time."""
    q = ((2*s**3-3*s*s+1)*q0+(s**3-2*s*s+s)*h*p0+
         (-2*s**3+3*s*s)*q1+(s**3-s*s)*h*p1)
    derivative = ((6*s*s-6*s)*q0+(3*s*s-4*s+1)*h*p0+
                  (-6*s*s+6*s)*q1+(3*s*s-2*s)*h*p1)
    return q, derivative


def periapses(raw, xtol=1e-14, rtol=1e-14):
    q, p, times = raw['q'], raw['p'], raw['times']
    radial = np.sum(q*p, axis=1); roots, residuals, positions = [], [], []
    for i in range(len(times)-1):
        if radial[i] < 0 <= radial[i+1]:
            h = times[i+1]-times[i]
            def fun(s):
                position, tangent = hermite_point(q[i], q[i+1], p[i], p[i+1], h, s)
                return float(np.sum(position*tangent))
            s = brentq(fun, 0., 1., xtol=xtol, rtol=rtol, maxiter=100)
            time = times[i]+s*h
            if time > 1e-10:
                roots.append(time); residuals.append(fun(s))
                positions.append(hermite_point(q[i], q[i+1], p[i], p[i+1], h, s)[0])
    return dict(times=np.asarray(roots), residuals=np.asarray(residuals),
                positions=np.asarray(positions).reshape((-1, 2)))


def orders(errors, hs):
    if min(errors) <= 0:
        raise ArithmeticError('Observed order requires strictly positive errors')
    return [math.log(errors[i]/errors[i+1])/math.log(hs[i]/hs[i+1])
            for i in range(len(errors)-1)]


def coupled_energy(states, omega, alpha=1.):
    q1, q2, p1, p2 = np.asarray(states).T
    coordinate = np.column_stack(((p1*p1+q1*q1)/2,
                                  (p2*p2+omega*omega*q2*q2)/2))
    coupling = alpha*q1*q2
    return coordinate, coupling, coordinate.sum(axis=1)+coupling


def modal_energy(states, eigenvalues, vectors):
    z = np.asarray(states)
    Q = np.column_stack([z[:, 0]*v[0]+z[:, 1]*v[1] for v in vectors])
    P = np.column_stack([z[:, 2]*v[0]+z[:, 3]*v[1] for v in vectors])
    return (P*P+np.asarray(eigenvalues)*Q*Q)/2


def symplectic_defect(matrix):
    M = np.asarray(matrix, float)
    J = np.array([[0., 0., 1., 0.], [0., 0., 0., 1.],
                  [-1., 0., 0., 0.], [0., -1., 0., 0.]])
    # Explicit sums avoid a BLAS dependency for a fixed4x4 diagnostic.
    residue = np.empty((4, 4))
    for i in range(4):
        for j in range(4):
            residue[i, j] = sum(M[k, i]*J[k, l]*M[l, j]
                                for k in range(4) for l in range(4))-J[i, j]
    return float(np.max(abs(residue))/(1+np.max(abs(M))**2))
