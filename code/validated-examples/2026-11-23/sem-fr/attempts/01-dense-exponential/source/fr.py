"""Gauss-node flux reconstruction with Radau corrections for linear advection.

The tested correction recovers nodal DG for a constant linear flux on affine
intervals. No nonlinear, shock-capturing or arbitrary FR-family claim is made.
"""
import numpy as np
from numpy.polynomial.legendre import Legendre, leggauss, legvander
from scipy.linalg import expm
from polynomials import cardinal, degree


def initial(x):
    return .4+np.sin(2*np.pi*x)


def exact(x, time, speed=1.):
    return initial((x-speed*time) % 1.)


def corrections(p, x, derivative=False):
    p = degree(p, high=2)
    left = (-1.)**p*(Legendre.basis(p)-Legendre.basis(p+1))/2
    right = (Legendre.basis(p)+Legendre.basis(p+1))/2
    if derivative:
        left, right = left.deriv(), right.deriv()
    return left(x), right(x)


class Operator:
    def __init__(self, n, p, speed=1.):
        p = degree(p, high=2)
        if type(n) is not int or not 2 <= n <= 64 or not np.isfinite(speed) or speed == 0 or abs(speed) > 2:
            raise ValueError('Require 2..64 cells and a finite, bounded nonzero speed')
        self.n, self.p, self.speed = n, p, float(speed)
        self.z, self.w = leggauss(p+1)
        self.d = cardinal(self.z, self.z, derivative=True)
        self.left, self.right = cardinal(self.z, np.array([-1., 1.]))
        self.gl, self.gr = corrections(p, self.z, derivative=True)
        self.x = (np.arange(n)[:, None]+(self.z+1)/2)/n

    def __call__(self, u):
        ql, qr = u@self.left, u@self.right
        flux_right = self.speed*(qr if self.speed > 0 else np.roll(ql, -1))
        flux_left = np.roll(flux_right, 1)
        return -2*self.n*(self.speed*u@self.d.T+(flux_left-self.speed*ql)[:, None]*self.gl+(flux_right-self.speed*qr)[:, None]*self.gr)

    def project(self, function=initial):
        # The same L2 projection rule as the unmodified published modal DG.
        q, w = leggauss(max(self.p+2, 4))
        x = (np.arange(self.n)[:, None]+(q+1)/2)/self.n
        coefficients = .5*np.einsum('jq,q,qm->jm', function(x), w, legvander(q, self.p))*(2*np.arange(self.p+1)+1)
        return coefficients@legvander(self.z, self.p).T

    def mass(self, u):
        return float(np.sum(u*self.w)/(2*self.n))

    def energy(self, u):
        return float(np.sum(u*u*self.w)/(4*self.n))

    def exponential(self, u, time):
        # Same spatial operator, a separate time propagator, not another PDE solver.
        size = self.n*(self.p+1)
        matrix = np.column_stack([self(e.reshape(u.shape)).ravel() for e in np.eye(size)])
        return (expm(time*matrix)@u.ravel()).reshape(u.shape)

    def error(self, u, time, quadrature=None):
        q, w = leggauss(quadrature or self.p+5)
        x = (np.arange(self.n)[:, None]+(q+1)/2)/self.n
        reconstructed = u@cardinal(self.z, q).T
        return float(np.sqrt(np.sum((reconstructed-exact(x, time, self.speed))**2*w)/(2*self.n)))


def evolve(operator, final_time, cfl, budget, function=initial):
    if not np.isfinite(final_time) or not 0 < final_time <= 1 or not np.isfinite(cfl) or not 0 < cfl <= .2:
        raise ValueError('Invalid bounded time/CFL')
    u = operator.project(function)
    start = u.copy(); time = 0.; steps = 0
    mass0, energy0 = operator.mass(u), operator.energy(u)
    max_mass_drift, max_energy_increase, max_courant = 0., 0., 0.
    history = [{'time': 0., 'mass': mass0, 'energy': energy0}]
    while time < final_time:
        budget.check()
        dt = min(cfl/(operator.n*(2*operator.p+1)*abs(operator.speed)), final_time-time)
        a = u+dt*operator(u)
        b = .75*u+.25*(a+dt*operator(a))
        unew = u/3+2/3*(b+dt*operator(b))
        if not np.isfinite(unew).all():
            raise ArithmeticError('Nonfinite FR state')
        max_mass_drift = max(max_mass_drift, *(abs(operator.mass(q)-mass0) for q in [a, b, unew]))
        max_energy_increase = max(max_energy_increase, operator.energy(unew)-operator.energy(u))
        max_courant = max(max_courant, abs(operator.speed)*dt*operator.n*(2*operator.p+1))
        u = unew; time += dt; steps += 1
        history.append({'time': float(time), 'mass': operator.mass(u), 'energy': operator.energy(u)})
    return u, start, {'steps': steps, 'final_time': float(time), 'max_mass_drift': max_mass_drift,
                      'max_energy_increase': max_energy_increase, 'max_scaled_courant': max_courant,
                      'initial_energy': energy0, 'final_energy': operator.energy(u), 'history': history}
