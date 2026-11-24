"""Ordinary normal-tail IS with estimator-specific analytic variance."""
import numpy as np
from scipy.special import log_ndtr,ndtri
from scipy.stats import beta


def log_weight(x,shift):return -shift*np.asarray(x)+.5*shift*shift


def moment(threshold,power):
    return float(np.exp(.5*power*(power-1)*threshold**2+log_ndtr(-power*threshold)))


def variance(threshold):
    lp=log_ndtr(-threshold);log_second=threshold**2+log_ndtr(-2*threshold)
    return float(np.exp(2*lp)*np.expm1(log_second-2*lp))


def count_interval(hits,total,alpha=.05):
    if not (0<=hits<=total and total>0):raise ValueError('Valid Bernoulli hit count required')
    return (0. if hits==0 else float(beta.ppf(alpha/2,hits,total-hits+1)),
            1. if hits==total else float(beta.ppf(1-alpha/2,hits+1,total-hits)))


def simulate(cfg,partial):
    thresholds=cfg['thresholds'];n=max(cfg['samples']);z=[];contributions=[];summaries=[]
    for seed in cfg['seeds']:
        draws=np.random.default_rng(seed).normal(size=n);ys=[]
        partial.update(current_z=draws,seed=np.array(seed))
        for a in thresholds:ys.append(np.where(draws>0,np.exp(log_weight(draws+a,a)),0.))
        z.append(draws);contributions.append(ys)
    z=np.stack(z);y=np.asarray(contributions) # batch,threshold,sample
    partial.update(base_normals=z,contributions=y) # retain ALL completed samples before any statistics
    for j,a in enumerate(thresholds):
        p=float(np.exp(log_ndtr(-a)));var=variance(a)
        for n in cfg['samples']:
            estimates=y[:,j,:n].mean(axis=1);known_se=np.sqrt(var/n);lo=estimates-ndtri(.975)*known_se;hi=estimates+ndtri(.975)*known_se
            hits=(z[:,:n]>a).sum(axis=1);direct=hits/n;intervals=np.array([count_interval(int(k),n) for k in hits]);is_covered=(lo<=p)&(p<=hi);direct_covered=(intervals[:,0]<=p)&(p<=intervals[:,1]);weights=np.exp(log_weight(z[:,:n]+a,a));event=y[:,j,:n]
            summaries.append({'a':a,'n':n,'truth':p,'analytic_variance':var,'estimate_mean':float(estimates.mean()),'batch_variance':float(np.var(estimates,ddof=1)),'aggregate_known_se':float(np.sqrt(var/(n*len(z)))),'IS_coverage':float(is_covered.mean()),'IS_coverage_binomial_CI':count_interval(int(is_covered.sum()),len(z)),'direct_coverage':float(direct_covered.mean()),'direct_coverage_binomial_CI':count_interval(int(direct_covered.sum()),len(z)),'direct_no_hit_batches':int(np.count_nonzero(hits==0)),'IS_estimates':estimates.tolist(),'direct_estimates':direct.tolist(),'direct_CP95_intervals':intervals.tolist(),'weight_ESS':((weights.sum(axis=1))**2/(weights*weights).sum(axis=1)).tolist(),'event_ESS':((event.sum(axis=1))**2/(event*event).sum(axis=1)).tolist(),'unweighted_proposal_event_mean':float((z[:,:n]>0).mean()),'IS_interval_recipe':'Known exact estimator variance normal95; not an exact finite-sample weighted interval.','coverage_scope':'64independent batches for this threshold/prefix only; nested prefixes and thresholds are not pooled.'})
    return {'base_normals':z,'contributions':y},summaries
