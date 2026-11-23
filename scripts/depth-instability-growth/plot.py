#!/usr/bin/env python3
"""Render only retained nonlinear fields and independent growth curves."""
import argparse,json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
p=argparse.ArgumentParser(description=__doc__);p.add_argument('--results',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args();result=json.loads(a.results.read_text());a.output.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False,'savefig.facecolor':'white'})
def save(fig,name):
 for ext in ['png','svg','pdf']:fig.savefig(a.output/(name+'.'+ext),dpi=150,bbox_inches='tight')
 plt.close(fig)
for c in result['cases']:
 row=next(x for x in c['records'] if x['id']=='n128');d=np.load(a.results.parent/row['file'],allow_pickle=False);eps=row['epsilon'];kh=c['id'].startswith('kh');q=d['omega'][-1]/eps if kh else d['theta'][-1]/eps;ref=d['reference_omega']/eps if kh else d['reference_theta']/eps;vmax=max(abs(q).max(),abs(ref).max());label=r'$\omega^\prime/\epsilon$' if kh else r'$b^\prime/\epsilon$';title='Smooth KH initial growth' if kh else 'Boussinesq RT initial growth'
 fig,axes=plt.subplots(1,3,figsize=(12,3.4),layout='constrained')
 for ax,data,name in zip(axes,[q,ref,q-ref],['Nonlinear PDE, 128 × 128','Independent linear Galerkin','Nonlinear − linear reference']):
  lim=vmax if ax is not axes[-1] else max(abs(q-ref).max(),1e-15);im=ax.imshow(data.T,origin='lower',extent=[0,2*np.pi,0,2*np.pi],cmap='RdBu_r',vmin=-lim,vmax=lim);ax.set(title=name,xlabel='x',ylabel='y');fig.colorbar(im,ax=ax,shrink=.78,label=label)
 fig.suptitle(title+' · small perturbation, not a nonlinear roll-up');save(fig,c['id'])
 fig,axes=plt.subplots(1,2,figsize=(8.2,3.3),layout='constrained');ax=axes[0];im=ax.imshow(q.T,origin='lower',extent=[0,2*np.pi,0,2*np.pi],cmap='RdBu_r',vmin=-vmax,vmax=vmax);ax.set(xlabel='x',ylabel='y',title=title);fig.colorbar(im,ax=ax,shrink=.8,label=label)
 for rr in c['records'][:3]:
  amps=np.array(rr['amplitudes']);axes[1].plot(np.linspace(0,float(d['times'][-1]),len(amps)),amps/amps[0],label=str(rr['n'])+'²',lw=1.2)
 amps=np.array(row['reference_amplitudes']);axes[1].plot(np.linspace(0,float(d['times'][-1]),len(amps)),amps/amps[0],'k--',label='Linear reference');axes[1].set(xlabel='Time',ylabel='Amplitude / initial',title='Finite-time growth');axes[1].legend(fontsize=8);save(fig,c['id']+'-preview')
