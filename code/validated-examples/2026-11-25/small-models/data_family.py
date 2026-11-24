"""Fixed whole-function heat problems; direct real-series continuum labels."""
import numpy as np


def problems():
    result = []
    for split, start, count in [('train', 850100, 24), ('validation', 850200, 6),
                              ('test', 850300, 8), ('ood-nu', 850400, 4),
                              ('ood-spectrum', 850500, 4)]:
        for j in range(count):
            ident = start+j
            rng = np.random.Generator(np.random.PCG64(ident))
            # Draw a then b; divide all three coefficients by physical mode k.
            a = rng.uniform(-1, 1, 3)/np.arange(1, 4)
            b = rng.uniform(-1, 1, 3)/np.arange(1, 4)
            nu = .25 if split == 'ood-nu' else (.1 if split == 'ood-spectrum' else [.05, .1, .15][j%3])
            result.append({'id': ident, 'split': split, 'a': a.tolist(), 'b': b.tolist(),
                           'nu': nu, 'sixth_cosine': .25 if split == 'ood-spectrum' else 0.})
    return result


def values(problem, n, time):
    x = 2*np.pi*np.arange(n)/n
    value = np.zeros(n)
    for k, (a, b) in enumerate(zip(problem['a'], problem['b']), 1):
        value += np.exp(-problem['nu']*k*k*time)*(a*np.cos(k*x)+b*np.sin(k*x))
    value += problem['sixth_cosine']*np.exp(-problem['nu']*36*time)*np.cos(6*x)
    return value


def batch(rows, n):
    features = np.array([np.column_stack((values(p, n, 0), np.full(n, p['nu']))) for p in rows])
    target = np.array([values(p, n, .25) for p in rows])
    return features, target

