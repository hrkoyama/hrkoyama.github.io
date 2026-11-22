"""Small deterministic diagnostic fixtures, independent of the mixture sampler."""
import numpy as np


def ar1_chains(rho, chains, draws, seed):
    if not -1 < rho < 1 or type(chains) is not int or type(draws) is not int or not 1 <= chains <= 32 or not 8 <= draws <= 16384:
        raise ValueError('Invalid bounded stationary AR(1) fixture')
    rng = np.random.Generator(np.random.PCG64(seed))
    values = np.empty((chains, draws))
    # Exact stationary start N(0,1), not a finite burn-in approximation.
    values[:, 0] = rng.standard_normal(chains)
    innovations = rng.standard_normal((chains, draws-1))
    scale = np.sqrt(1-rho*rho)
    for i in range(1, draws):
        values[:, i] = rho*values[:, i-1]+scale*innovations[:, i-1]
    return values


def edge_fixtures():
    rng = np.random.Generator(np.random.PCG64(2026112271))
    iid = rng.standard_normal((4, 2048))
    scale = iid.copy();scale[0] *= 3
    shift = iid.copy();shift[0] += 3
    return {'iid': iid, 'odd': rng.standard_normal((4, 257)),
            'ties': np.round(iid, 1), 'scale': scale, 'shift': shift,
            'antithetic': ar1_chains(-.5, 4, 2048, 2026112272),
            'constant': np.ones((4, 128)),
            'separated_constants': np.repeat(np.array([[-1.], [-1.], [1.], [1.]]), 128, axis=1)}
