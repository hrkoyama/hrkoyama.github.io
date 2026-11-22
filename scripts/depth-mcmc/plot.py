#!/usr/bin/env python3
"""Draw only stored MCMC results; never run the sampler or diagnostic code."""
import argparse
import json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

COLORS = {'dispersed':'#a85b31', 'same_mode':'#a44a6a', 'mixed':'#235b83'}
LABELS = {'dispersed':'Local RW: dispersed starts', 'same_mode':'Local RW: all left starts', 'mixed':'Known-symmetry global proposal'}


def draw(data, output):
    output = Path(output);output.mkdir(parents=True, exist_ok=True)
    plt.rcParams.update({'font.size':9, 'axes.titlesize':10})
    cases = {case['id']:case for case in data['cases']}
    case = cases['mcmc-multimodal-mixing']
    fig, axes = plt.subplots(3, 4, figsize=(16, 9), constrained_layout=True)
    for row, scenario in enumerate(['dispersed','same_mode','mixed']):
        p = case['plot_data'][scenario]
        final = next(r for r in case['records'] if r['scenario']==scenario and r['draws_per_chain']==16384)
        for chain, trace in enumerate(p['trace']):
            axes[row,0].plot(p['trace_draws'], trace, linewidth=.6, alpha=.8, label=f'Chain {chain+1}')
        axes[row,0].set(title=LABELS[scenario], xlabel='Post-warmup draw (first 1024)', ylabel='x')
        axes[row,1].plot(p['cdf_x'], p['exact_cdf'], 'k--', label='Analytic target CDF')
        axes[row,1].plot(p['cdf_x'], p['cdf'], color=COLORS[scenario], label='Pooled empirical CDF')
        axes[row,1].set(title='Pooled CDF can hide trapped chains', xlabel='x', ylabel='P(X <= x)')
        axes[row,2].bar(range(1,5), final['per_chain_occupancy'], color=COLORS[scenario], alpha=.8)
        axes[row,2].axhline(.5, color='k', linestyle='--', label='Target occupancy .5')
        axes[row,2].set(title='Per-chain positive-mode occupancy', xlabel='Chain', ylabel='Fraction x > 0', ylim=(-.03,1.03), xticks=[1,2,3,4])
        axes[row,3].plot(p['acf_lags'], p['within_chain_acf'], 'o-', color=COLORS[scenario])
        diag=final['x_diagnostics'];within=final['within_chain']['ess_sum']
        axes[row,3].set(title=f'Rhat {diag["rhat_rank"]:.4f}; within ESS {within:.0f}; bulk {diag["ess_bulk"]:.0f}', xlabel='Lag (draws)', ylabel='Within-chain centered ACF')
        for ax in axes[row]:
            ax.grid(alpha=.2)
        axes[row,0].legend(fontsize=7);axes[row,1].legend(fontsize=7);axes[row,2].legend(fontsize=7)
    fig.suptitle('Same bimodal target and 16384 draws/chain; three fixed seeds in JSON. Trapped controls are expected failures.', fontsize=12)
    fig.savefig(output/'mcmc-multimodal-mixing.png',dpi=140);plt.close(fig)
    case=cases['mcmc-diagnostic-reference']
    fig, axes=plt.subplots(1,3,figsize=(13,4.3),constrained_layout=True)
    for key,ax,title in [('rhat_rank',axes[0],'Rank/folded split Rhat'),('ess_bulk',axes[1],'Bulk ESS')]:
        rows=[r for r in case['records'] if r['series']=='arviz-comparison' and r.get(key) is not None and r.get('reference_'+key) is not None and 'degeneracy_note' not in r]
        ref=np.array([r['reference_'+key] for r in rows]);own=np.array([r[key] for r in rows])
        ax.scatter(ref,own,s=16,color='#235b83',alpha=.7)
        limits=[min(ref.min(),own.min())*.95,max(ref.max(),own.max())*1.05]
        ax.plot(limits,limits,'k--',label='Identity')
        if key.startswith('ess'):ax.set_xscale('log');ax.set_yscale('log')
        ax.set(xlabel='Independent ArviZ 0.20.0',ylabel='Atlas',title=title+'; finite nondegenerate points')
        ax.legend(fontsize=8)
    rows=[r for r in case['records'] if r['series']=='ar1-calibration']
    exact=np.array([r['exact_stationary_tau'] for r in rows]);estimate=np.array([r['estimated_mean_tau'] for r in rows])
    axes[2].scatter(exact,estimate,s=35,color='#a85b31',label='Finite stationary AR(1) estimates')
    axes[2].plot([.25,10],[.25,10],'k--',label='Infinite-series exact tau')
    axes[2].set(xscale='log',yscale='log',xlabel='Exact (1+rho)/(1-rho)',ylabel='Estimated mean tau',title='Observable-specific ESS; antithetic tau < 1 allowed')
    axes[2].legend(fontsize=7)
    for ax in axes:ax.grid(alpha=.2)
    fig.suptitle('62 same-data reference fixtures; exact degeneracies have explicit null/status, not numerical agreement claims.',fontsize=10)
    fig.savefig(output/'mcmc-diagnostic-reference.png',dpi=140);plt.close(fig)


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--results',required=True);parser.add_argument('--output',required=True)
    args=parser.parse_args();draw(json.loads(Path(args.results).read_text()),args.output)
