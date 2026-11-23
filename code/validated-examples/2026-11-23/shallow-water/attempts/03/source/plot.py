#!/usr/bin/env python3
"""Render saved numerical arrays only; never execute the solver."""
import argparse
import json
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def finish(fig,out,ident):
    fig.savefig(out/(ident+'.png'),dpi=150)
    fig.savefig(out/(ident+'.svg'))
    fig.savefig(out/(ident+'.pdf'))
    fig.savefig(out/(ident+'-preview.png'),dpi=80)
    plt.close(fig)


def main():
    p=argparse.ArgumentParser();p.add_argument('--results',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    result=json.loads(a.results.read_text());base=a.results.parent;a.output.mkdir(parents=True,exist_ok=True)
    plt.rcParams.update({'font.size':10,'axes.titlesize':11,'axes.spines.top':False,'axes.spines.right':False})
    case={c['id']:c for c in result['cases']}
    fig,axes=plt.subplots(2,2,figsize=(12,7.2),layout='constrained')
    for ax,label,title in zip(axes[0],['immersed','emerged'],['Immersed bump: lake at rest','Emerged bump: stationary wet/dry interface']):
        d=np.load(base/('field-lake-'+label+'.npz'));x=.5*(d['edges'][:-1]+d['edges'][1:]);z=d['bed'];h=d['state'][:,0]
        ax.fill_between(x,0,z,color='#847d70',alpha=.6,label='represented bed')
        ax.plot(x,z+h,color='#197792',lw=2,label='final surface')
        ax.plot(x,z+d['initial'][:,0],'--',color='#e18a33',lw=1,label='initial equilibrium')
        ax.set(xlabel='x [m]',ylabel='z, h+z [m]',xlim=(6,14),title=title);ax.legend(fontsize=8)
    rows=[r for r in case['swashes-topography']['records'] if r['family']=='subcritical']
    for r in rows:
        d=np.load(base/('field-'+r['id']+'.npz'));x=.5*(d['edges'][:-1]+d['edges'][1:])
        axes[1,0].plot(x,d['state'][:,0]+d['bed'],label='FV N='+str(r['n']),lw=1.2)
    axes[1,0].plot(x,d['reference'][:,0]+d['bed'],'k--',lw=1.5,label='Bernoulli reference')
    axes[1,0].set(xlabel='x [m]',ylabel='free surface [m]',xlim=(5,16),title='Nonzero subcritical flow: q=4.42 m²/s');axes[1,0].legend(fontsize=8)
    for key,label in [('relative_depth_l1','depth'),('relative_momentum_l1','discharge')]:
        axes[1,1].loglog([r['n'] for r in rows],[r[key] for r in rows],'o-',label=label)
    axes[1,1].set(xlabel='cells N',ylabel='relative L1 error',title='Moving-steady preservation error at t=2s');axes[1,1].legend()
    fig.suptitle('SWASHES fixed topographic states | hydrostatic reconstruction + HLL',fontsize=14)
    finish(fig,a.output,'swashes-topography')
    fig,axes=plt.subplots(2,2,figsize=(12,7.2),layout='constrained')
    rows=case['dry-bed-dam-break']['records']
    for r in rows:
        d=np.load(base/('field-'+r['id']+'.npz'));x=.5*(d['edges'][:-1]+d['edges'][1:])
        axes[0,0].plot(x,d['state'][:,0],label='FV N='+str(r['n']),lw=1.1)
        axes[0,1].plot(x,d['state'][:,1],lw=1.1)
    axes[0,0].plot(x,d['reference'][:,0],'k--',lw=1.6,label='Ritter cell means');axes[0,0].legend(fontsize=8)
    axes[0,1].plot(x,d['reference'][:,1],'k--',lw=1.6,label='Ritter hu');axes[0,1].legend(fontsize=8)
    axes[0,0].set(xlabel='x [m]',ylabel='water depth h [m]',title='Exactly dry downstream bed: hR=0')
    axes[0,1].set(xlabel='x [m]',ylabel='discharge hu [m²/s]',title='Conservative momentum/discharge')
    mesh=axes[1,0].pcolormesh(x,d['snapshot_times'],d['history'][:,:,0],shading='nearest',cmap='Blues')
    times=d['snapshot_times'];axes[1,0].plot(2*np.sqrt(9.81)*times,times,'--',color='#d57124',label='analytic support front')
    axes[1,0].set(xlabel='x [m]',ylabel='time [s]',title='Five saved numerical depth snapshots');axes[1,0].legend(fontsize=8)
    fig.colorbar(mesh,ax=axes[1,0],label='h [m]')
    for key,label in [('relative_depth_l1','depth'),('relative_momentum_l1','discharge')]:
        axes[1,1].loglog([r['n'] for r in rows],[r[key] for r in rows],'o-',label=label)
    axes[1,1].set(xlabel='cells N',ylabel='relative L1 error',title='Ritter conservative-cell-mean refinement');axes[1,1].legend()
    fig.suptitle('Dry-bed dam break | real wetting, no positive-depth floor | t=0.5s',fontsize=14)
    finish(fig,a.output,'dry-bed-dam-break')


if __name__=='__main__':main()
