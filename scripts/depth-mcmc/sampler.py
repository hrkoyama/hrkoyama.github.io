"""Original fixed symmetric-mixture MH sampler; rejected states are retained."""
import hashlib
import math
import time
import numpy as np
from scipy.special import ndtr

SCENARIOS = ['dispersed', 'same_mode', 'mixed']


class Budget:
    def __init__(self, seconds=120.):
        if isinstance(seconds, bool) or not math.isfinite(seconds) or not 0 < seconds <= 120:
            raise ValueError('Budget must be positive and at most 120 seconds')
        self.deadline = time.perf_counter()+seconds

    def check(self):
        if time.perf_counter() > self.deadline:
            raise RuntimeError('Fixed calculation wall-clock budget exhausted')


def array_sha256(array):
    """Digest canonical little-endian float64 C-order values, excluding ZIP headers."""
    return hashlib.sha256(np.asarray(array, dtype='<f8').tobytes(order='C')).hexdigest()


def validate_sampler(config):
    for key in ['mode_distance', 'component_sigma', 'proposal_scale']:
        value = config[key]
        if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value) or not 0 < value <= 100:
            raise ValueError('Invalid positive sampler parameter: '+key)
    p = config['jump_probability']
    if isinstance(p, bool) or not isinstance(p, (int, float)) or not math.isfinite(p) or not 0 < p < 1:
        raise ValueError('Invalid jump probability')
    for key, lo, hi in [('chains', 2, 16), ('samples', 128, 32768), ('burn', 0, 4096)]:
        value = config[key]
        if type(value) is not int or not lo <= value <= hi:
            raise ValueError('Invalid bounded '+key)
    if config['chains'] % 2:
        raise ValueError('Dispersed experiment requires an even number of chains')
    if config['scenarios'] != SCENARIOS or len(config['seeds']) != 3 or len(set(config['seeds'])) != 3 or any(type(s) is not int or not 0 <= s < 2**32 for s in config['seeds']):
        raise ValueError('Expected the three scenarios and three distinct uint32 seeds')
    if config['budgets'] != sorted(set(config['budgets'])) or len(config['budgets']) != 3 or config['budgets'][-1] != config['samples'] or any(type(n) is not int or n < 128 for n in config['budgets']):
        raise ValueError('Invalid fixed prefix budgets')
    for key in ['cdf_points', 'acf_lags']:
        if config[key] != sorted(set(config[key])) or len(config[key]) > 64:
            raise ValueError('Invalid '+key)
    if any(type(lag) is not int or lag < 0 or lag >= min(config['budgets']) for lag in config['acf_lags']):
        raise ValueError('Invalid ACF lag')
    if not np.isfinite(config['cdf_points']).all():
        raise ValueError('Nonfinite CDF point')


def log_target(x, distance=6., sigma=1.):
    left = -.5*((np.asarray(x)+distance)/sigma)**2
    right = -.5*((np.asarray(x)-distance)/sigma)**2
    return np.logaddexp(left, right)-math.log(2*sigma*math.sqrt(2*math.pi))


def target_cdf(x, distance=6., sigma=1.):
    return (ndtr((np.asarray(x)+distance)/sigma)+ndtr((np.asarray(x)-distance)/sigma))/2


def proposal_density(destination, origin, scale=.8, probability=.1):
    """q(y|x)=(1-p)phi_s(y-x)+p phi_s(y+x), exactly symmetric in x,y."""
    delta = np.asarray(destination)-np.asarray(origin)
    total = np.asarray(destination)+np.asarray(origin)
    return ((1-probability)*np.exp(-.5*(delta/scale)**2)+probability*np.exp(-.5*(total/scale)**2))/(scale*math.sqrt(2*math.pi))


def sample_chains(config, scenario, seed, budget=None):
    validate_sampler(config)
    if scenario not in SCENARIOS:
        raise ValueError('Unknown scenario')
    budget = budget or Budget()
    m, n, burn = config['chains'], config['samples'], config['burn']
    total = n+burn
    code = SCENARIOS.index(scenario)
    streams = [np.random.Generator(np.random.PCG64(np.random.SeedSequence([seed, code, chain]))) for chain in range(m)]
    # Draws are independent streams for each chain; no adaptive proposal tuning.
    normal = np.column_stack([rng.standard_normal(total) for rng in streams])
    log_uniform = -np.column_stack([rng.exponential(size=total) for rng in streams])
    selectors = np.column_stack([rng.random(total) for rng in streams])
    x = np.full(m, -config['mode_distance'])
    if scenario != 'same_mode':
        x[m//2:] *= -1
    logp = log_target(x, config['mode_distance'], config['component_sigma'])
    probability = config['jump_probability'] if scenario == 'mixed' else 0.
    samples = np.empty((m, n))
    accepted = np.zeros(m, dtype=int)
    for index in range(total):
        if index % 256 == 0:
            budget.check()
        centers = np.where(selectors[index] < probability, -x, x)
        proposed = centers+config['proposal_scale']*normal[index]
        proposed_logp = log_target(proposed, config['mode_distance'], config['component_sigma'])
        take = log_uniform[index] < proposed_logp-logp
        x = np.where(take, proposed, x)
        logp = np.where(take, proposed_logp, logp)
        if index >= burn:
            accepted += take
            samples[:, index-burn] = x
    return samples, accepted/n
