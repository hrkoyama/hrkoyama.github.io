"""Small tensor/Smolyak Clenshaw-Curtis rules with exact angle-index keys."""
from fractions import Fraction
from functools import lru_cache
from itertools import product
from math import comb
import math


def angle_key(j, denominator):
    value = Fraction(j, denominator)
    if not 0 <= value <= 1 or denominator < 1:
        raise ValueError("Invalid angle index")
    if denominator & (denominator-1):
        raise ValueError("Dyadic angle denominator required")
    return value.numerator, value.denominator


def key_order(key):
    return Fraction(*key)


@lru_cache(maxsize=64)
def coordinate(key):
    p, q = key
    if angle_key(p, q) != key:
        raise ValueError("Noncanonical angle key")
    if p == 0:
        return 0.0
    if p == q:
        return 1.0
    if 2*p == q:
        return 0.5
    return (1-math.cos(math.pi*(p/q)))/2


@lru_cache(maxsize=5)
def cc_items(level):
    if not isinstance(level, int) or not 0 <= level <= 4:
        raise ValueError("Fixed levels0..4 only")
    if level == 0:
        return (((1, 2), 1.0),)
    count = 2**level
    rows = []
    for j in range(count+1):
        key = angle_key(j, count)
        if j in (0, count):
            weight = 1/(2*(count*count-1))
        else:
            theta = math.pi*j/count
            terms = [1.0, *(-2*math.cos(2*k*theta)/(4*k*k-1)
                            for k in range(1, count//2)),
                     -math.cos(count*theta)/(count*count-1)]
            weight = math.fsum(terms)/count
        rows.append((key, weight))
    return tuple(rows)


def delta_items(level):
    values = {}
    for key, weight in cc_items(level):
        values.setdefault(key, []).append(weight)
    if level:
        for key, weight in cc_items(level-1):
            values.setdefault(key, []).append(-weight)
    return [(key, math.fsum(values[key])) for key in sorted(values, key=key_order)]


def multiindices(dimension, level):
    return sorted((v for v in product(range(level+1), repeat=dimension) if sum(v) <= level),
                  key=lambda v: (sum(v), v))


def tensor_key_order(key):
    return tuple(key_order(k) for k in key)


def assemble(dimension, level, kind):
    if dimension not in (2, 3, 4) or not 0 <= level <= 4:
        raise ValueError("Fixed dimension/level required")
    if kind == "tensor":
        specifications = [((level,)*dimension, 1)]
    elif kind == "delta":
        specifications = [(v, 1) for v in multiindices(dimension, level)]
    elif kind == "combination":
        specifications = [(v, (-1)**(level-sum(v))*comb(dimension-1, level-sum(v)))
                          for v in multiindices(dimension, level)
                          if max(0, level-dimension+1) <= sum(v)]
    else:
        raise ValueError("Unknown assembly")
    gathered = {}
    contributions = 0
    for levels, scale in specifications:
        factors = [delta_items(l) if kind == "delta" else cc_items(l) for l in levels]
        for terms in product(*factors):
            key = tuple(t[0] for t in terms)
            weight = scale*math.prod(t[1] for t in terms)
            gathered.setdefault(key, []).append(weight)
            contributions += 1
    keys = sorted(gathered, key=tensor_key_order)
    weights = [math.fsum(gathered[k]) for k in keys]
    points = [tuple(coordinate(k) for k in key) for key in keys]
    return {"keys": keys, "weights": weights, "points": points,
            "assembly_contributions": contributions, "unique_nodes": len(keys),
            "assembly_duplicates": contributions-len(keys),
            "sum_weights": math.fsum(weights), "sum_absolute_weights": math.fsum(map(abs, weights)),
            "zero_weights_retained": sum(w == 0 for w in weights)}


def integrand(name, point):
    if name == "smooth-product":
        return math.prod(math.exp(a*x) for a, x in zip((1, .5, .25, .125), point))
    if name == "interaction-product":
        return math.prod((x-.5)**2 for x in point)
    raise ValueError("Unknown cubature integrand")


def integrate(name, dimension, level, kind, cap, callback=None, before_evaluation=None):
    rule = assemble(dimension, level, kind)
    if rule["unique_nodes"] > cap:
        raise ValueError("Cubature evaluation budget")
    values = []
    for point in rule["points"]:
        if before_evaluation:
            before_evaluation(point)
        value = integrand(name, point)
        if callback:
            callback(point, value)
        values.append(value)
    return {**rule, "values": values,
            "value": math.fsum(w*v for w, v in zip(rule["weights"], values)),
            "evaluations": len(values), "cache_hits": 0, "converged": True,
            "termination": "fixed_rule_completed", "estimated_error": None}
