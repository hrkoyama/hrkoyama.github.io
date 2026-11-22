#!/usr/bin/env python3
"""Draw scientific figures from saved measurements only; no solver import."""
import argparse
import json
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--results',required=True,type=Path);parser.add_argument('--output',required=True,type=Path);args=parser.parse_args()
    data=json.loads(args.results.read_text());cases={c['id']:c for c in data['cases']};args.output.mkdir(parents=True,exist_ok=True)
    plt.rcParams.update({'font.size':10,'axes.grid':True,'grid.alpha':.25})
    def finish(fig,identifier):
        fig.tight_layout();fig.savefig(args.output/(identifier+'.png'),dpi=150);plt.close(fig)
    name='amg-conditioning';rows=cases[name]['records'];fig,ax=plt.subplots(1,2,figsize=(10,3.8))
    for eps in sorted({r['epsilon'] for r in rows},reverse=True):
        f=[r for r in rows if r['epsilon']==eps]
        ax[0].semilogx([r['condition_2_analytic'] for r in f],[r['cycles'] for r in f],'o-',label=f'epsilon={eps:g}')
    ax[0].set(xlabel='Analytic 2-norm condition number',ylabel='V-cycles (budget if unresolved)',title='Anisotropy at fixed condition number');ax[0].legend()
    for n in sorted({r['n'] for r in rows}):
        f=[r for r in rows if r['n']==n];ax[1].loglog([r['condition_times_residual'] for r in f],[r['relative_forward_error'] for r in f],'o',label=f'n={n}')
    ax[1].set(xlabel='condition number x true relative residual',ylabel='Relative forward error vs sparse direct',title='Algebraic diagnostic; no PDE order');ax[1].legend();finish(fig,name)
    name='qr-svd-conditioning';rows=cases[name]['records'];f=[r for r in rows if r['kind']=='prescribed-spectrum'];fig,ax=plt.subplots(1,2,figsize=(10,3.8))
    x=[r['condition_2'] for r in f]
    for key,label in [('qr_reconstruction','QR reconstruction'),('svd_reconstruction','SVD reconstruction'),('maximum_relative_forward_error','Forward solution error'),('forward_acceptance_budget','Condition-aware acceptance budget')]:
        ax[0].loglog(x,[max(r[key],1e-18) for r in f],'o-',label=label)
    ax[0].set(xlabel='Prescribed condition number',ylabel='Relative error',title='Backward and forward errors differ');ax[0].legend(fontsize=8)
    f=[r for r in rows if r['kind']=='rank-cutoff'];ax[1].semilogx([r['rank_rtol'] for r in f],[r['bias_to_untruncated_solution'] for r in f],'o-',label='Bias to untruncated solution')
    ax[1].set(xlabel='Numerical-rank cutoff',ylabel='Relative solution difference',title='Rank truncation changes the problem');ax[1].legend(fontsize=8);finish(fig,name)
    name='krylov-eigen-conditioning';rows=cases[name]['records'];fig,ax=plt.subplots(1,2,figsize=(10,3.8))
    for gap in sorted({r['gap'] for r in rows if r['kind']=='symmetric-cluster'}):
        f=[r for r in rows if r['kind']=='symmetric-cluster' and r['gap']==gap]
        ax[0].semilogy([r['dimension'] for r in f],[max(r['top_two_projector_error'],1e-17) for r in f],'o-',label=f'gap={gap:g}')
    ax[0].set(xlabel='Krylov dimension',ylabel='Top-two projector error (2-norm)',title='Cluster invariant subspace');ax[0].legend()
    f=[r for r in rows if r['kind']=='constructed-pseudoeigenpair']
    for key,label in [('absolute_residual','Absolute residual'),('eigenvalue_error','Forward eigenvalue error')]:ax[1].loglog([r['coupling'] for r in f],[r[key] for r in f],'o-',label=label)
    ax[1].set(xlabel='Upper triangular coupling K',ylabel='Absolute error',title='Constructed sensitivity, not solver failure');ax[1].legend(fontsize=8);finish(fig,name)
    name='quadrature-conditioning';rows=cases[name]['records'];fig,ax=plt.subplots(1,2,figsize=(10,3.8))
    for width in sorted({r['width'] for r in rows if r['kind']=='narrow-gauss'}):
        f=[r for r in rows if r['kind']=='narrow-gauss' and r['width']==width]
        ax[0].loglog([r['order'] for r in f],[max(r['absolute_error'],1e-18) for r in f],'o-',label=f'width={width:g}')
    ax[0].set(xlabel='Gauss-Legendre order',ylabel='Absolute error vs analytic integral',title='Narrow peaks require resolution');ax[0].legend()
    f=[r for r in rows if r['kind'].startswith('compact-bump')]
    ax[1].bar(['Unsplit: actual','Unsplit: estimated','Known-support: actual'],[f[0]['absolute_error'],f[0]['estimated_error'],f[1]['absolute_error']],color=['#c24935','#888888','#267f78'])
    ax[1].set_yscale('symlog',linthresh=1e-13)
    ax[1].set(ylabel='Absolute integral error',title='Expected heuristic blind spot');ax[1].tick_params(axis='x',labelsize=8);finish(fig,name)


if __name__=='__main__':main()
