"""Exact-rational direct Lagrange integration on tiny stored-node rules."""
from fractions import Fraction


def lagrange_weights(nodes):
    x = [Fraction.from_float(float(v)) for v in nodes]
    weights = []
    for j, point in enumerate(x):
        polynomial, denominator = [Fraction(1)], Fraction(1)
        for k, other in enumerate(x):
            if k == j:
                continue
            grown = [Fraction(0)]*(len(polynomial)+1)
            for degree, coefficient in enumerate(polynomial):
                grown[degree] -= other*coefficient
                grown[degree+1] += coefficient
            polynomial = grown
            denominator *= point-other
        weights.append(sum((coefficient/Fraction(degree+1)
                            for degree, coefficient in enumerate(polynomial)), Fraction(0))/denominator)
    return weights
