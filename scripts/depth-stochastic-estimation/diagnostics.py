"""Original equation-based rank/folded Rhat and observable-specific ESS.

Vehtari et al. (2021), sections3–4, supplies the statistical equations. Finite
endpoint, ties, odd splitting and quantile conventions are declared explicitly
and checked against a separately executed ArviZ0.20.0 reference, not imported.
"""
import math
import numpy as np
from scipy.special import ndtri
from scipy.stats import rankdata
from scipy.stats.mstats import mquantiles

METRICS = ['rhat_rank', 'rhat_z', 'rhat_folded', 'rhat_split', 'ess_bulk', 'ess_tail', 'ess_mean']


def split_chains(values):
    half = values.shape[1]//2
    return np.concatenate([values[:, :half], values[:, -half:]], axis=0)


def rank_normalize(values):
    ranks = rankdata(values.ravel(), method='average').reshape(values.shape)
    # Corrected Blom denominator S+1/4, not the early-paper typo S-1/4.
    return ndtri((ranks-3/8)/(values.size+1/4))


def autocovariance(values):
    values = np.asarray(values, float)
    centered = values-values.mean(axis=-1, keepdims=True)
    n = values.shape[-1]
    nfft = 1 << (2*n-1).bit_length()
    spectrum = np.fft.rfft(centered, n=nfft, axis=-1)
    return np.fft.irfft(spectrum*spectrum.conjugate(), n=nfft, axis=-1)[..., :n]/n


def direct_autocovariance(values, lags):
    values = np.asarray(values, float)
    centered = values-values.mean(axis=-1, keepdims=True)
    n = values.shape[-1]
    return np.array([np.sum(centered[..., :n-lag]*centered[..., lag:], axis=-1)/n for lag in lags]).T


def basic_rhat(values):
    n = values.shape[1]
    # A repeated nonexact binary float can have a tiny np.var due to the mean
    # summation. Detect exact constant rows before interpreting such roundoff.
    if np.all(values == values[:, :1]):
        return None, 'infinite_separation' if np.ptp(values[:, 0]) > 0 else 'zero_variance'
    within = float(np.mean(np.var(values, axis=1, ddof=1)))
    between_per_draw = float(np.var(np.mean(values, axis=1), ddof=1))
    if within == 0:
        return None, 'infinite_separation' if between_per_draw > 0 else 'zero_variance'
    return math.sqrt(((n-1)*within/n+between_per_draw)/within), 'ok'


def effective_size(values):
    """Multi-chain variance/ACF estimator with initial-positive monotone pairs.

    The last examined pair contributes its positive even-lag endpoint once;
    complete earlier pairs are monotonized. The finite-sample tau floor is
    1/log10(MN), allowing antithetic ESS above MN instead of flooring tau at1.
    Constant transformed quantile events use the reference library's MN
    convention internally; diagnostics() refuses a constant ORIGINAL observable.
    """
    m, n = values.shape
    total = m*n
    if float(np.ptp(values)) < np.finfo(float).resolution:
        return float(total)
    cov = autocovariance(values).mean(axis=0)
    within = cov[0]*n/(n-1)
    variance = cov[0]+(float(np.var(values.mean(axis=1), ddof=1)) if m > 1 else 0.)
    if variance <= 0:
        raise ArithmeticError('Nonpositive multi-chain variance')
    rho = 1-(within-cov)/variance
    rho[0] = 1.
    pairs = rho[:2*(n//2)].reshape(-1, 2).sum(axis=1)
    last = max(0, n//2-2)
    failed = np.flatnonzero(pairs[1:last+1] <= 0)
    endpoint = int(failed[0]+1) if failed.size else last
    complete = np.minimum.accumulate(pairs[:endpoint])
    tau = -1+2*float(complete.sum())+max(float(rho[2*endpoint]), 0.)
    return total/max(tau, 1/math.log10(total))


def tail_thresholds(values):
    """Declared ArviZ0.20/SciPy1.14.1 floating type7 convention.

    This common quantile primitive is shared with the reference, while the
    rank/ACF/ESS implementation remains independent. Although real-arithmetic
    type7 equals NumPy linear quantiles, weighted interpolation can round a
    repeated order statistic by1ULP and change its <=event mask. No tolerance
    is changed and the historical public diagnostic source is untouched.
    """
    return np.asarray(mquantiles(values,[.05,.95],alphap=1,betap=1),dtype=float)


def diagnose(values):
    values = np.asarray(values, float)
    empty = {key: None for key in METRICS}
    if values.ndim != 2 or values.shape[0] < 2 or values.shape[1] < 8:
        return {**empty, 'status': 'insufficient_chains_or_draws', 'metric_status': {key: 'undefined' for key in METRICS}}
    if values.shape[0] > 32 or values.shape[1] > 65536:
        raise ValueError('Diagnostic array exceeds the bounded workload')
    if not np.isfinite(values).all():
        return {**empty, 'status': 'nonfinite_input', 'metric_status': {key: 'undefined' for key in METRICS}}
    if float(np.ptp(values)) == 0:
        return {**empty, 'status': 'zero_global_variance', 'metric_status': {key: 'undefined' for key in METRICS}}
    halves = split_chains(values)
    z = rank_normalize(halves)
    folded = rank_normalize(np.abs(halves-np.median(halves)))
    rz, zs = basic_rhat(z)
    rf, fs = basic_rhat(folded)
    rs, ss = basic_rhat(halves)
    status = 'infinite_separation' if 'infinite_separation' in [zs, fs] else 'ok'
    valid = [v for v in [rz, rf] if v is not None]
    rhat = max(valid) if status == 'ok' and valid else None
    quantiles = tail_thresholds(values)
    tail_sizes = [effective_size(split_chains((values <= q).astype(float))) for q in quantiles]
    return {'rhat_rank': rhat, 'rhat_z': rz, 'rhat_folded': rf, 'rhat_split': rs,
            'ess_bulk': effective_size(z), 'ess_tail': min(tail_sizes), 'ess_mean': effective_size(halves),
            'status': status,
            'metric_status': {'rhat_rank': status, 'rhat_z': zs, 'rhat_folded': fs, 'rhat_split': ss,
                              'ess_bulk': 'ok', 'ess_tail': 'ok', 'ess_mean': 'ok'}}


def within_chain_summary(values, lags):
    cov = autocovariance(values)
    if np.any(cov[:, 0] == 0):
        return {'acf': None, 'ess_sum': None, 'status': 'zero_within_chain_variance'}
    acf = np.mean(cov[:, lags]/cov[:, :1], axis=0)
    ess_sum = sum(effective_size(split_chains(chain[None, :])) for chain in values)
    return {'acf': acf.tolist(), 'ess_sum': float(ess_sum),
            'status': 'within_chain_only_not_global_mixing'}


def mean_mcse(values):
    """Original-observable sample SD divided by square root of its mean ESS.

    Rank bulk ESS is not substituted here. This addition is separately checked
    against ArviZ0.20.0 on the exact supplied transformed two-dimensional data.
    """
    values=np.asarray(values,float)
    row=diagnose(values)
    if row['status']!='ok' or row['ess_mean'] is None:
        raise ValueError('Mean MCSE requires finite nonconstant chain arrays')
    return float(np.std(values,ddof=1)/np.sqrt(row['ess_mean']))
