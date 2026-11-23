#!/usr/bin/env python3
"""Plot only stored self-consistent PIC data and qualified linear references."""
import argparse,json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def phase_panel(ax,data,cfg,index=-1):
    nx=cfg['spatial_strata'];nv=len(data['v_initial'])//nx;k=cfg['k'];alpha=cfg['amplitude'];x0=data['x_initial'].reshape(nv,nx);v0=data['v_initial'].reshape(nv,nx);dv=(data['v_history'][index]-data['v_initial']).reshape(nv,nx)/alpha
    # Rows are quadrature velocities, columns quiet spatial strata; every color is
    # an actual evolved full-f particle velocity increment, not an analytic orbit.
    visible=np.max(abs(v0),axis=1)<(6 if cfg['drift']==0 else 8);xp=k*x0[visible];vv=v0[visible];values=dv[visible];limit=float(np.max(abs(values)))
    mesh=ax.scatter(xp.ravel(),vv.ravel(),c=values.ravel(),cmap='RdBu_r',s=6,vmin=-limit,vmax=limit,rasterized=True)
    ax.set(xlabel='initial k x',ylabel='initial velocity',title=f'Actual phase response at t={data["snapshot_times"][index]:g}'+(' (diagnostic)' if cfg['drift'] else ''));ax.set_xlim(0,2*np.pi);return mesh


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--results',type=Path,required=True);p.add_argument('--output',type=Path,required=True);args=p.parse_args();args.results=args.results.parent if args.results.is_file() else args.results;args.output.mkdir(parents=True,exist_ok=True)
    cfg=json.loads((Path(__file__).parent/'inputs.json').read_text());result=json.loads((args.results/'result.json').read_text())
    if not result['passed']:raise ValueError('Figures require a passed saved result')
    for case in result['cases']:
        name=case['id'];controls=cfg['cases'][name];base=next(r for r in case['records'] if r['family']=='ensemble');data=np.load(args.results/base['file']);ref=np.load(args.results/(name+'-linear-reference.npz'));scale=controls['amplitude']/(2*controls['k'])
        fig,axs=plt.subplots(2,2,figsize=(11,7),layout='constrained');ax=axs[0,0]
        for r in case['records']:
            if r['family']=='ensemble':
                d=np.load(args.results/r['file']);show=d['history'][:,1]<=controls['fit_window'][1];ax.plot(d['history'][show,1],d['history'][show,3]/scale,alpha=.65,lw=1,label='PIC seed '+str(r['seed']))
        show=ref['times']<=controls['fit_window'][1];ax.plot(ref['times'][show],ref['normalized_field'][show],'k--',lw=1.3,label='independent linear IVP');ax.axvspan(*controls['fit_window'],alpha=.1,color='orange',label='fixed fit window');ax.set(xlabel='time',ylabel='Im(E mode 1) / [alpha/(2 k)]',title='Signed mode through the fixed fit window');ax.legend(fontsize=7)
        ax=axs[0,1];h=data['history'];ax.semilogy(h[:,1],np.abs(h[:,3]/scale),label='absolute signed mode');ax.semilogy(ref['times'],abs(ref['normalized_field']),'k--',label='linear IVP');ax.axvspan(*controls['fit_window'],alpha=.1,color='orange');ax.set(xlabel='time',ylabel='absolute normalized mode',title='Zeros are retained; no sample selection');ax.legend(fontsize=8)
        mesh=phase_panel(axs[1,0],data,controls);fig.colorbar(mesh,ax=axs[1,0],label='delta v / initial alpha')
        ax=axs[1,1];m=case['metrics'];rates=[r['fit']['gamma'] for r in case['records'] if r['family']=='ensemble'];ax.scatter(range(1,5),rates,label='conditional spatial-shift seeds');ax.axhline(m['dielectric_rate'],color='k',ls='--',label='dielectric pole');ax.axhline(m['volterra_fixed_window_rate'],color='orange',ls=':',label='linear-IVP same-window fit');ax.set(xlabel='fixed seed index',ylabel='amplitude rate gamma',title='Seed spread excludes velocity-quadrature bias');ax.legend(fontsize=7)
        fig.suptitle('Warm Landau damping' if controls['drift']==0 else 'Warm counter-streaming instability')
        for ext in ['png','svg','pdf']:fig.savefig(args.output/(name+'.'+ext),dpi=160)
        plt.close(fig)
        fig,ax=plt.subplots(figsize=(7.2,4.2),layout='constrained');mesh=phase_panel(ax,data,controls);fig.colorbar(mesh,ax=ax,label='delta v / initial alpha');fig.savefig(args.output/(name+'-preview.png'),dpi=160);plt.close(fig)


if __name__=='__main__':main()
