"""Independent matrix and exact unnormalized-pair representations."""
from fractions import Fraction as F
from decimal import Decimal, localcontext
import math
import numpy as np


def matrices(length, levels, mode):
    current = np.eye(length)
    details, sizes = [], []
    for _ in range(levels):
        n = current.shape[0]
        sizes.append(n)
        low, high = np.zeros(((n+1)//2, n)), np.zeros(((n+1)//2, n))
        for k in range((n+1)//2):
            indices = [2*k, 2*k+1 if 2*k+1 < n else 0 if mode == 'periodic' else n-1]
            for index, sign in zip(indices, [1.0, -1.0]):
                low[k, index] += 1.0/math.sqrt(2.0)
                high[k, index] += sign/math.sqrt(2.0)
        details.append(np.einsum('ij,jk->ik', high, current))
        current = np.einsum('ij,jk->ik', low, current)
    analysis = np.vstack([current, *details[::-1]])
    total = analysis.shape[0]
    synthesis = np.zeros((len(current), total))
    synthesis[:, :len(current)] = np.eye(len(current))
    offset = len(current)
    for n in sizes[::-1]:
        count = (n+1)//2
        select = np.zeros((count, total))
        select[:, offset:offset+count] = np.eye(count)
        out = np.empty((2*count, total))
        out[::2] = (synthesis+select)/math.sqrt(2.0)
        out[1::2] = (synthesis-select)/math.sqrt(2.0)
        synthesis = out[:n].copy()
        offset += count
    return analysis, synthesis


def exact_coefficients(signal, levels, mode):
    """Pair sums/differences are exact Fraction; normalization uses Decimal80."""
    a = [F.from_float(float(v)) for v in signal]
    blocks, padding_energy = [], F(0)
    for level in range(1, levels+1):
        if len(a) % 2:
            extra = a[0] if mode == 'periodic' else a[-1]
            padding_energy += extra*extra/F(2**(level-1))
            a = a+[extra]
        detail = [a[i]-a[i+1] for i in range(0, len(a), 2)]
        a = [a[i]+a[i+1] for i in range(0, len(a), 2)]
        blocks.append((level, detail))
    blocks = [(levels, a), *blocks[::-1]]
    with localcontext() as ctx:
        ctx.prec = 80
        sqrt2 = Decimal(2).sqrt()
        values = [float(Decimal(v.numerator)/Decimal(v.denominator)/(sqrt2**level)) for level, block in blocks for v in block]
    return np.array(values), padding_energy
