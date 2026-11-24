"""Private state-only two-component iterate arithmetic, explicit sumprod."""
import math
import numpy as np


def reconstruct(base_hi, base_lo, Z, y, observe=None):
    hi, lo = np.zeros_like(base_hi), np.zeros_like(base_hi)
    def note(stage):
        if observe is not None: observe(stage, {'reconstruct_new_hi': hi, 'reconstruct_new_lo': lo})
    note('allocated')
    try:
        for i in range(len(hi)):
            coefficients = (1.0, 1.0, *(float(z) for z in Z[i]))
            values = (float(base_hi[i]), float(base_lo[i]), *(float(v) for v in y))
            hi[i] = math.sumprod(coefficients, values)
            lo[i] = math.sumprod((*coefficients, -1.0), (*values, float(hi[i])))
    except BaseException:
        note('exception'); raise
    note('complete')
    return hi, lo


def residual(b, reaction, hi, lo, observe=None):
    h2 = float((len(hi)+1)**2); out = np.zeros_like(hi)
    def note(stage):
        if observe is not None: observe(stage, {'residual9_new': out})
    note('allocated')
    try:
        for i in range(len(hi)):
            c = float(reaction[i])
            out[i] = math.sumprod((1.0, -2*h2, h2, h2, c, -2*h2, h2, h2, c),
                (float(b[i]), float(hi[i]), float(hi[i-1]) if i else 0.0,
                 float(hi[i+1]) if i+1 < len(hi) else 0.0, float(hi[i]),
                 float(lo[i]), float(lo[i-1]) if i else 0.0,
                 float(lo[i+1]) if i+1 < len(lo) else 0.0, float(lo[i])))
    except BaseException:
        note('exception'); raise
    note('complete')
    return out


def newton_update(u, alpha, hi, lo):
    return np.array([math.sumprod((1.0, float(alpha), float(alpha)),
                                 (float(a), float(b), float(c)))
                     for a,b,c in zip(u,hi,lo)], dtype=float)
