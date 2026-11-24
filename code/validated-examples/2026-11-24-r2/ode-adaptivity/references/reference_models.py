"""Independent stiff reference definitions; production models are not imported."""
import numpy as np


def system(key):
    if key == 'robertson':
        def f(t, z):
            return np.array([-0.04*z[0]+10000*z[1]*z[2],
                             0.04*z[0]-10000*z[1]*z[2]-30000000*z[1]**2,
                             30000000*z[1]**2])
        def j(t, z):
            return np.array([[-0.04, 10000*z[2], 10000*z[1]],
                             [0.04, -10000*z[2]-60000000*z[1], -10000*z[1]],
                             [0, 60000000*z[1], 0]])
        return f, j, np.array([1., 0., 0.]), np.array([1., 1e-4, 1.]), 0.4
    if key in ('vdp-mu1', 'vdp-mu100'):
        mu = 1 if key.endswith('mu1') else 100
        def f(t, z):
            return np.array([z[1], mu*z[1]-mu*z[0]**2*z[1]-z[0]])
        def j(t, z):
            return np.array([[0, 1], [-1-2*mu*z[0]*z[1], mu-mu*z[0]**2]])
        return f, j, np.array([2., 0.]), np.ones(2), 2.
    raise ValueError('Unrecognized reference model')


def observation_times(key):
    total = 0.4 if key == 'robertson' else 2.
    divisor, early = (512, (1, 2, 4, 8, 16)) if key == 'robertson' else (256, (1, 2, 4, 8))
    return np.array(sorted(set([total*k/16 for k in range(17)]+[total*k/divisor for k in early])))
