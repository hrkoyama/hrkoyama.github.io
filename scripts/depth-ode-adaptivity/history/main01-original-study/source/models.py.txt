"""Primary vector RHS and analytic Jacobians; no reference-solver imports."""
import numpy as np


def robertson(t, y):
    a, b, c = y
    r1 = -0.04*a+1e4*b*c
    r3 = 3e7*b*b
    return np.array([r1, -r1-r3, r3])


def robertson_jac(t, y):
    a, b, c = y
    return np.array([[-0.04, 1e4*c, 1e4*b],
                     [0.04, -1e4*c-6e7*b, -1e4*b],
                     [0.0, 6e7*b, 0.0]])


def vdp(t, y, mu):
    x, v = y
    return np.array([v, mu*(1-x*x)*v-x])


def vdp_jac(t, y, mu):
    x, v = y
    return np.array([[0.0, 1.0], [-2*mu*x*v-1, mu*(1-x*x)]])


def model(case_id, mu=None):
    if case_id == 'robertson-stiff-kinetics':
        return robertson, robertson_jac, np.array([1., 0., 0.]), np.array([1., 1e-4, 1.])
    if case_id == 'van-der-pol-stiff-transition' and mu in (1, 100):
        return (lambda t, y: vdp(t, y, mu)), (lambda t, y: vdp_jac(t, y, mu)), np.array([2., 0.]), np.ones(2)
    raise ValueError('Unknown frozen model')
