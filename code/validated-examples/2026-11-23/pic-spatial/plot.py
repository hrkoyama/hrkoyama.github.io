#!/usr/bin/env python3
"""Render stored independently evolved self-consistent phase-space trajectories."""
import argparse,json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--results',type=Path,required=True);p.add_argument('--output',type=Path,required=True);args=p.parse_args();args.results=args.results.parent if args.results.is_file() else args.results;args.output.mkdir(parents=True,exist_ok=True);result=json.loads((args.results/'result.json').read_text())
    if not result['passed']:raise ValueError('Passed saved data required')
    rows=result['cases'][0]['records'];chosen=next(r for r in rows if r['n']==32);d=np.load(args.results/chosen['file']);t=d['times'];x=d['primary_x'];v=d['primary_v'];xr=d['reference_x'];vr=d['reference_v'];length=2*np.pi
    fig,axs=plt.subplots(2,2,figsize=(10,7),layout='constrained');ax=axs[0,0];ax.scatter(x[-1]%length,v[-1],s=9,label='vectorized / FFT');ax.scatter(xr[-1]%length,vr[-1],s=28,facecolors='none',edgecolors='orange',linewidths=.65,label='scalar / dense DFT');ax.set(xlabel='periodic x',ylabel='velocity',title=f'Actual phase space at t={t[-1]:g}');ax.legend(fontsize=8)
    ax=axs[0,1];ax.plot(np.arange(32)*length/32,d['primary_electric'][-1],label='vectorized');ax.plot(np.arange(32)*length/32,d['reference_electric'][-1],'o',ms=3,label='independent dense DFT');ax.set(xlabel='grid x',ylabel='electric field',title='Each path sourced its own field at every kick');ax.legend(fontsize=8)
    ax=axs[1,0];ax.semilogy(t,np.maximum(np.max(abs(x-xr),axis=1),1e-18),label='position');ax.semilogy(t,np.maximum(np.max(abs(v-vr),axis=1),1e-18),label='velocity');ax.set(xlabel='time',ylabel='maximum absolute difference (display floor 1e-18)',title='All 13 states compared, no temporal interpolation');ax.legend(fontsize=8)
    ax=axs[1,1];ax.scatter([r['n'] for r in rows],[r['field'] for r in rows],label='all-step electric field');ax.set(xlabel='grid nodes',ylabel='maximum absolute discrepancy',title='Six paired comparisons = twelve evolutions');ax.legend(fontsize=8)
    fig.suptitle('Independent PIC spatial implementation: same mathematical time algorithm')
    name='pic-independent-spatial'
    for ext in ['png','svg','pdf']:fig.savefig(args.output/(name+'.'+ext),dpi=160)
    plt.close(fig)
    fig,ax=plt.subplots(figsize=(7.2,4.2),layout='constrained');color=v[-1]-d['v_initial'];sc=ax.scatter(x[-1]%length,v[-1],c=color,cmap='RdBu_r',s=16);ax.set(xlabel='actual final x',ylabel='actual final velocity',title='Self-consistent PIC phase space; color = velocity change');fig.colorbar(sc,ax=ax,label='v(T)-v(0)');fig.savefig(args.output/(name+'-preview.png'),dpi=160);plt.close(fig)


if __name__=='__main__':main()
