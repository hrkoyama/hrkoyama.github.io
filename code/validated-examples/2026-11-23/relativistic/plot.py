#!/usr/bin/env python3
"""Plot stored numerical fields only; no physics rerun or synthetic 2D flow."""
import argparse
import json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def save(fig,path):
    for extension in ['png','svg','pdf']:
        fig.savefig(path.with_suffix('.'+extension),dpi=165,bbox_inches='tight')
    plt.close(fig)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--results',type=Path,required=True)
    p.add_argument('--output',type=Path)
    args=p.parse_args()
    result_path=args.results if args.results.is_file() else args.results/'result.json'
    directory=result_path.parent;output=args.output or directory;output.mkdir(parents=True,exist_ok=True)
    result=json.loads(result_path.read_text())
    plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False})
    for case in result['cases']:
        ident=case['id'];wave=ident=='srmhd-alfven';rows=case['records'];r=rows[-1]
        with np.load(directory/r['field_file']) as raw:d={k:raw[k] for k in raw.files}
        x=d['x'];times=d['snapshot_times'];field=d['U_history'][:,:,5 if wave else 0]
        title='SRMHD: finite-amplitude CP Alfvén wave' if wave else 'SRHD: symmetric two-shock collision'
        quantity=r'$B_y$' if wave else r'$D=\rho W$'
        def spacetime(fig,ax):
            image=ax.pcolormesh(x,times,field,shading='nearest',cmap='RdBu_r' if wave else 'viridis',rasterized=True)
            fig.colorbar(image,ax=ax,label=quantity)
            ax.set(xlabel='x',ylabel='t',ylim=(times[0],times[-1]),title='1D x–t field · 5 stored times')
        fig,axs=plt.subplots(2,2,figsize=(11.5,7.8),layout='constrained');fig.suptitle(title+' · N='+str(r['n']))
        spacetime(fig,axs[0,0]);ax=axs[0,1]
        for component,label,color in ([(5,r'$B_y$','#2563eb'),(6,r'$B_z$','#c2410c')] if wave else [(0,r'$D$','#2563eb')]):
            ax.plot(x,d['U'][...,component],color=color,label=label+' numerical')
            ax.plot(x,d['U_reference_history'][-1,:,component],'--',color=color,lw=1.2,label=label+' exact cell mean')
        ax.set(xlabel='x',ylabel='conserved cell mean',title='Final profile');ax.legend(fontsize=8)
        ax=axs[1,0];n=np.array([row['n'] for row in rows])
        errors=np.array([row['transverse_relative_l1'] if wave else row['component_l1'][0] for row in rows])
        ax.loglog(n,errors,'o-',label='measured transverse L1' if wave else 'measured D L1')
        ax.loglog(n,errors[0]*(n[0]/n)**(2 if wave else 1),'--',label=r'$N^{-2}$ guide' if wave else r'$N^{-1}$ guide')
        ax.set(xlabel='cells N',ylabel='error',title='All three fixed grids');ax.legend(fontsize=8);ax.grid(alpha=.2)
        ax=axs[1,1];st=d['stages'];t=st[:,2]
        ax.plot(t,st[:,3],label='min density');ax.plot(t,st[:,4],label='min pressure');ax.plot(t,st[:,5],label='max |v|')
        ax.axhline(1.,color='black',ls=':',lw=.8,label='light speed c=1')
        ax.set(xlabel='t',ylabel='stage diagnostic',title='Every SSP stage and completed step');ax.legend(fontsize=8)
        save(fig,output/ident)
        fig,ax=plt.subplots(figsize=(7.6,4.5),layout='constrained');spacetime(fig,ax)
        fig.suptitle(title+' · N='+str(r['n']),fontsize=12)
        save(fig,output/(ident+'-preview'))


if __name__=='__main__':main()
