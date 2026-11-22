#!/usr/bin/env python3
"""Redraw a scientific figure from saved numbers only; no solver is executed."""
import argparse
import json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter

parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--results',required=True)
parser.add_argument('--output',required=True)
args=parser.parse_args()
case=json.loads(Path(args.results).read_text())['cases'][0]
profiles=case['profiles'];x=np.asarray(profiles['x']);ref=np.asarray(profiles['reference_final'])
rows=case['records'];coarse=min(r['steps'] for r in rows);medium=sorted({r['steps'] for r in rows})[1]
colors={'lie-trotter':'#bd572b','strang':'#1b7971'}
labels={'lie-trotter':'Lie–Trotter','strang':'Strang'}
plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False})
fig,axes=plt.subplots(2,2,figsize=(11.5,8),layout='constrained')
axes[0,0].plot(x,ref[0],color='#202d3b',label='Unsplit FD reference',lw=2)
for method in colors:
    field=np.asarray(profiles['computed_final'][method][str(coarse)])
    axes[0,0].plot(x,field[0],'--' if method=='lie-trotter' else ':',color=colors[method],lw=2,label=labels[method])
axes[0,0].set(title=f'Same final u field (N=32, {coarse} steps)',xlabel='x',ylabel='u(x,1)')
axes[0,0].legend(fontsize=9)
for method in colors:
    selected=[r for r in rows if r['method']==method]
    h=np.array([r['dt'] for r in selected]);err=np.array([r['max_l2'] for r in selected])
    label=labels[method]+f" (last p={selected[-1]['observed_order_l2']:.3f})"
    axes[0,1].loglog(h,err,'o-',color=colors[method],label=label)
counts=sorted({r['steps'] for r in rows},reverse=True)
axes[0,1].set_xticks([1/n for n in counts],labels=['1/'+str(n) for n in counts])
axes[0,1].xaxis.set_minor_formatter(NullFormatter())
axes[0,1].set(title='Time refinement at the SAME fixed grid',xlabel='Time step h',ylabel='Max observed RMS error (worst species)')
axes[0,1].legend(fontsize=9);axes[0,1].grid(alpha=.2,which='both')
for method in colors:
    field=np.asarray(profiles['computed_final'][method][str(coarse)])
    for species,style in [(0,'-'),(1,'--')]:
        axes[1,0].plot(x,field[species]-ref[species],style,color=colors[method],label=labels[method]+(' u' if species==0 else ' v'))
axes[1,0].set(title=f'Final pointwise errors ({coarse} steps)',xlabel='x',ylabel='Computed − unsplit FD reference')
axes[1,0].legend(fontsize=9,ncol=2);axes[1,0].axhline(0,color='#888',lw=.6)
for method in colors:
    observed=[r for r in case['time_records'] if r['method']==method and r['steps']==medium and r['time']>0]
    axes[1,1].semilogy([r['time'] for r in observed],[r['l2'] for r in observed],'o-',color=colors[method],label=labels[method])
axes[1,1].set(title=f'Identical observation times ({medium} steps)',xlabel='t',ylabel='RMS error (worst species)')
axes[1,1].legend(fontsize=9);axes[1,1].grid(alpha=.2)
fig.suptitle('Nonlinear Schnakenberg reaction–diffusion: matched Lie–Trotter / Strang\nPeriodic FD2, N=32, T=1; temporal errors include midpoint reaction discretization',fontsize=13)
out=Path(args.output);out.mkdir(parents=True,exist_ok=True)
fig.savefig(out/(case['id']+'.png'),dpi=160)
plt.close(fig)
