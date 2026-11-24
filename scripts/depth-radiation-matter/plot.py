"""Saved physical radiation/material energies; independent point references."""
import argparse,json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def save(fig,path):
    for ext in ['png','svg','pdf']:fig.savefig(str(path)+'.'+ext,dpi=155,bbox_inches='tight')


def main():
    p=argparse.ArgumentParser();p.add_argument('--results',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args();directory=a.results.parent if a.results.is_file() else a.results;result=json.loads((directory/'result.json').read_text());a.output.mkdir(parents=True,exist_ok=True)
    for c in result['cases']:
        row=next(r for r in c['records'] if r.get('id','').endswith('-n512'))
        with np.load(directory/row['fields'],allow_pickle=False) as d:x=d['x'];states=d['states'];times=d['times'];rx=d['reference_x'];refs=d['reference_values'];history=d['history']
        fig,axes=plt.subplots(2,2,figsize=(10.6,7.3));colors=plt.cm.plasma(np.linspace(.15,.85,len(times)-1))
        for i,color in enumerate(colors,1):
            for j in range(2):axes[0,j].plot(x,states[i,j],color=color,label=f'tau={times[i]:.5g}');axes[0,j].plot(rx,refs[i-1,:,j],'o',mfc='none',color=color,markersize=4)
        for j,label in enumerate(['Radiation energy','Material variable V (energy at epsilon1)']):axes[0,j].set(xlim=(0,6),xlabel='Dimensionless position',ylabel=label,title='Lines: numerical; circles: independent reference');axes[0,j].legend(fontsize=7)
        axes[1,0].plot(history[:,0],history[:,1],label='Weighted total');axes[1,0].plot(history[:,0],history[:,2],'--',label='Source/boundary ledger');axes[1,0].set(xlabel='Dimensionless time',ylabel='Integrated energy');axes[1,0].legend()
        for j,label in enumerate(['Radiation','Material']):
            sequence=[r for r in c['records'] if r.get('family')=='refinement'];axes[1,1].loglog([r['cells'] for r in sequence],[r['reference_rms'][j] for r in sequence],'o-',label=label)
        axes[1,1].set(xlabel='Cells',ylabel='Reference-point RMS',title='Separate from time/angle/domain sensitivity');axes[1,1].legend();fig.suptitle(c['id']+' — diffusion and transport are distinct models');fig.tight_layout();save(fig,a.output/c['id']);plt.close(fig)
        fig,ax=plt.subplots(figsize=(7.2,3.8));ax.plot(x,states[-1,0],label='Radiation');ax.plot(x,states[-1,1],label='Material');ax.plot(rx,refs[-1,:,0],'ko',mfc='none',label='Independent reference');ax.plot(rx,refs[-1,:,1],'ks',mfc='none');ax.set(xlim=(0,6),xlabel='Dimensionless position',ylabel='Energy variable',title=c['id']+f' at tau={times[-1]:.5g}');ax.legend(fontsize=8);fig.tight_layout();save(fig,a.output/(c['id']+'-preview'));plt.close(fig)
    target=next(c for c in result['cases'] if c['id']=='su-olson-transport1997')
    control=target['metrics']['matched_thick_limit_control'];rows=control['mode_records']
    fig,axes=plt.subplots(2,2,figsize=(11.3,7.7))
    for row in rows:
        with np.load(directory/row['fields'],allow_pickle=False) as d:
            x=d['x'];k=float(d['kappa']);amp=float(d['initial_amplitude']);z=d['analytic_diffusion_amplitudes'][-1];energy=d['energy'][-1];material=d['material'][-1];flux=d['flux'][-1]
            curve=1+z[0].real*np.cos(x)-z[0].imag*np.sin(x);fc=z[2].real*np.cos(x)-z[2].imag*np.sin(x)
        axes[0,0].plot(x,(energy-1)/amp,label=f'FV E, kappa={k:g}');axes[0,0].plot(x,(material-1)/amp,':',linewidth=1)
        axes[0,1].plot(x,k*flux/amp,label=f'FV, kappa={k:g}')
    axes[0,0].plot(x,(curve-1)/amp,'k--',label='Matched diffusion (E=V)');axes[0,1].plot(x,k*fc/amp,'k--',label='Fick: -E_x/(3 kappa)')
    axes[0,0].set(xlabel='Physical periodic x',ylabel='Perturbation / initial cell-mean amplitude',title='Final scaled time s=0.25; dotted: material V');axes[0,1].set(xlabel='Physical periodic x',ylabel='kappa F / initial amplitude',title='Final physical flux and sign')
    kappas=[r['kappa'] for r in rows]
    for key,label in [('final_FV_space_error','FV vs same-angle continuum'),('maximum_angular_sensitivity','Same-angle vs GL128 (all times)'),('final_continuum_limit_error','GL128 vs diffusion'),('final_joint_energy_error','FV vs diffusion (E,V)')]:
        axes[1,0].loglog(kappas,[r[key] for r in rows],'o-',label=label)
    axes[1,0].set(xlabel='Physical opacity kappa (N grows as kappa squared)',ylabel='Separate normalized error',title='Separated spatial, angular and continuum-limit errors')
    # log axes omit exact zero values without altering the saved scientific metrics.
    with np.load(directory/rows[-1]['fields'],allow_pickle=False) as d:
        axes[1,1].plot(d['scaled_times'],d['joint_scaled_flux_errors'],'o-',label='FV vs Fick scaled-flux error')
        axes[1,1].plot(d['scaled_times'],d['continuum_limit_errors'],'s-',label='Continuum vs diffusion (E,V)')
    axes[1,1].set(xlabel='Scaled time s=t/kappa',ylabel='Normalized discrepancy',title='Physical initial layer retained, including s=0')
    for ax in axes.flat:ax.legend(fontsize=7);ax.grid(alpha=.2)
    fig.suptitle('Matched thick-limit control: 1D periodic FV/S_N, exact-time single mode\nResolved joint limit; primary SSPRK2 and fixed-grid AP are not certified')
    fig.tight_layout();save(fig,a.output/'su-olson-transport1997-thick-limit');plt.close(fig)
if __name__=='__main__':main()
