#!/usr/bin/env python3
"""Render actual hash-checked WENO cell averages and critical-point records."""
import argparse
import hashlib
import json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

CASE = 'weno-critical-epsilon'

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--results', type=Path, required=True);p.add_argument('--output', type=Path, required=True)
    a = p.parse_args();result = json.loads(a.results.read_text());saved = a.results.parent
    if not result['passed']:raise ValueError('Passed numerical results required')
    for name, digest in result['source_sha256'].items():
        if sha(Path(__file__).resolve().parent/name) != digest:raise ValueError('Changed scientific source: '+name)
    for name, digest in result['files_sha256'].items():
        if Path(name).name != name or sha(saved/name) != digest:raise ValueError('Changed saved field: '+name)
    case = result['cases'][0];rows = case['records'];local = case['reconstruction_records']
    plt.rcParams.update({'font.family':'DejaVu Sans', 'font.size':10, 'axes.spines.top':False,
                         'axes.spines.right':False, 'svg.hashsalt':CASE, 'text.color':'#18364b',
                         'axes.labelcolor':'#18364b', 'axes.titlecolor':'#18364b'})
    colors = {'weno-js':'#bd5539', 'weno-z':'#20799b'}
    styles = {'fixed-1e-40':'-', 'fixed-1e-6':'--', 'h-squared':':'}
    labels = {'fixed-1e-40':r'$10^{-40}$', 'fixed-1e-6':r'$10^{-6}$', 'h-squared':r'$h^2$'}
    a.output.mkdir(parents=True, exist_ok=True);manifest = []
    def save(fig, name):
        for ext in ['png', 'svg', 'pdf']:
            path = a.output/(name+'.'+ext)
            if path.exists():raise ValueError('Fresh figure paths required')
            meta = {'Date':None} if ext == 'svg' else {'CreationDate':None, 'ModDate':None} if ext == 'pdf' else {}
            fig.savefig(path, dpi=160, metadata=meta, facecolor='white')
            manifest.append({'file':path.name, 'sha256':sha(path)})
        plt.close(fig)
    finest = max(r['n'] for r in rows)
    fields = {}
    for m in colors:
        r = next(r for r in rows if r['method'] == m and r['n'] == finest and r['epsilon_policy'] == 'fixed-1e-40' and r['family'] == 'refinement')
        with np.load(saved/r['field'], allow_pickle=False) as d:fields[m] = {k:d[k].copy() for k in d.files}
    d = fields['weno-z'];x = .5*(d['edges'][1:]+d['edges'][:-1])
    def local_curve(ax, profile, weights=False):
        for m in colors:
            for policy in styles:
                seq = [r for r in local if r['profile'] == profile and r['method'] == m and r['epsilon_policy'] == policy]
                ax.loglog([r['n'] for r in seq], [r['weight_deviation' if weights else 'absolute_error'] for r in seq],
                          'o'+styles[policy], ms=3, color=colors[m], label=m.replace('weno-', '').upper()+', '+labels[policy])
        ax.set(xlabel='Inverse cell width $1/h$', ylabel=r'$\max_k|\omega_k-d_k|$' if weights else 'Interface absolute error')
        ax.grid(alpha=.16);ax.set_xticks([64,128,256,512], labels=['64','128','256','512']);ax.minorticks_off()
    fig, ax = plt.subplots(2, 2, figsize=(11, 8));fig.subplots_adjust(left=.09,right=.97,bottom=.11,top=.83,wspace=.30,hspace=.42)
    fig.text(.09,.945,'WENO5 / CRITICAL POINTS AND EPSILON',fontsize=20,weight='bold')
    fig.text(.09,.887,'Finite-volume cell means; Z power 2. Fixed inputs; reconstruction and PDE errors measured separately.',fontsize=10)
    local_curve(ax[0,0], 'first-critical');ax[0,0].set_title('First critical point: $x^2+x^3+x^4+x^5$');ax[0,0].legend(fontsize=7,ncol=2,frameon=False)
    local_curve(ax[0,1], 'second-critical');ax[0,1].set_title('Second critical point: diagnostic, no order guarantee')
    for m in colors:
        for policy in styles:
            seq = [r for r in rows if r['method']==m and r['epsilon_policy']==policy and r['family']=='refinement']
            ax[1,0].loglog([r['n'] for r in seq],[r['l1'] for r in seq],'o'+styles[policy],color=colors[m],ms=4)
    ax[1,0].set(xlabel='Transport cells $N$',ylabel='Final whole-domain $L^1$',title='Actual periodic transport, RK4, $T=1$');ax[1,0].grid(alpha=.16);ax[1,0].set_xticks([32,64,128], labels=['32','64','128']);ax[1,0].minorticks_off()
    for m in colors:ax[1,1].plot(x,fields[m]['q']-fields[m]['q_reference'],label=m.upper(),color=colors[m])
    ax[1,1].set(xlabel='$x$',ylabel='Numerical minus analytic cell mean',title=f'Saved field error, N={finest}, epsilon $10^{{-40}}$');ax[1,1].legend(fontsize=8,frameon=False);ax[1,1].grid(alpha=.16)
    fig.text(.09,.025,'Dashed / dotted curves change epsilon, not the PDE. Analytic cell means are independently quadrature-checked.',fontsize=9)
    save(fig,CASE)
    fig, ax = plt.subplots(1,3,figsize=(12,4.7));fig.subplots_adjust(left=.07,right=.975,bottom=.22,top=.73,wspace=.34)
    fig.text(.07,.92,'WENO5 / ACTUAL TRANSPORT AND CRITICAL RECONSTRUCTION',fontsize=18,weight='bold')
    fig.text(.07,.82,f'Unit-speed periodic scalar advection | {finest} cells | T = 1 | Z power 2',fontsize=10)
    ax[0].plot(x,d['q_reference'],color='#536a5a',lw=2,label='Analytic cell means')
    for m in colors:ax[0].plot(x,fields[m]['q'],color=colors[m],ls='--',label=m.upper())
    ax[0].set(xlabel='$x$',ylabel='Cell mean $q$',title='Actual evolved full field');ax[0].legend(fontsize=7,frameon=False)
    for m in colors:ax[1].plot(x,fields[m]['q']-d['q_reference'],color=colors[m],label=m.upper())
    ax[1].set(xlabel='$x$',ylabel='Signed cell-mean error',title=r'Transport error, $\epsilon=10^{-40}$');ax[1].ticklabel_format(axis='y',style='sci',scilimits=(0,0));ax[1].grid(alpha=.16)
    for m in colors:
        seq=[r for r in local if r['profile']=='first-critical' and r['method']==m and r['epsilon_policy']=='fixed-1e-40']
        ax[2].loglog([r['n'] for r in seq],[r['absolute_error'] for r in seq],'o-',color=colors[m],label=m.upper())
    ax[2].set(xlabel='Inverse cell width $1/h$',ylabel='Interface absolute error',title='First-critical reconstruction');ax[2].grid(alpha=.16);ax[2].set_xticks([64,128,256,512],labels=['64','128','256','512']);ax[2].minorticks_off();ax[2].legend(fontsize=7,frameon=False)
    fig.text(.07,.055,'The reconstruction study uses analytic polynomial cell means; it is separate from the evolved periodic profile.',fontsize=9)
    save(fig,CASE+'-preview')
    (a.output/'figure-provenance.json').write_text(json.dumps({'source_result_sha256':sha(a.results),'figures':manifest},indent=2)+'\n')

if __name__ == '__main__':main()
