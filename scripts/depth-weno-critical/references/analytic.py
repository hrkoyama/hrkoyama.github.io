"""Independent analytic cell averages; no WENO functions are imported."""
import numpy as np
from numpy.polynomial.legendre import leggauss

PROFILES = {'regular': [0, 1, 1, 1, 1, 1],
            'first-critical': [0, 0, 1, 1, 1, 1],
            'second-critical': [0, 0, 0, 1, 1, 1]}


def polynomial_value(x, coefficients):
    return sum(c*np.asarray(x)**k for k, c in enumerate(coefficients))


def polynomial_means(centers, h, coefficients):
    left, right = np.asarray(centers)-h/2, np.asarray(centers)+h/2
    return sum(c*(right**(k+1)-left**(k+1))/((k+1)*h)
               for k, c in enumerate(coefficients))


def periodic_value(x, time=0.):
    phase = 2*np.pi*(np.asarray(x)-time)
    return np.cos(phase)+.1*np.sin(phase)**3


def periodic_means(n, time=0.):
    h = 1/n
    phase = 2*np.pi*((np.arange(n)+.5)*h-time)
    return (np.sinc(h)*np.cos(phase)+.075*np.sinc(h)*np.sin(phase)
            -.025*np.sinc(3*h)*np.sin(3*phase))


def quadrature_means(n, time=0., order=12):
    """Separate point-function Gauss quadrature, not the Fourier antiderivative."""
    nodes, weights = leggauss(order)
    x = (np.arange(n)[:, None]+.5+.5*nodes[None, :])/n
    return .5*(periodic_value(x, time)*weights).sum(axis=1)
