"""Private Python3.12 sumprod Jv: float64 storage, extended internal dot."""
import math
import numpy as np


def jac_action(u, coefficient, v):
    h2 = float((len(v)+1)**2)
    diagonal = coefficient*np.exp(u)
    out = np.empty_like(v)
    for i in range(len(v)):
        center = float(v[i])
        left = float(v[i-1]) if i else 0.0
        right = float(v[i+1]) if i+1 < len(v) else 0.0
        out[i] = math.sumprod((2.0*h2, -h2, -h2, -float(diagonal[i])),
                              (center, left, right, center))
    return out
