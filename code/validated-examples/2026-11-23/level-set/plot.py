#!/usr/bin/env python3
"""Plot actual saved contour samples, errors and full two-dimensional fields."""
import argparse,json,math
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter


def contour(ax,points,**kwargs):
    p=np.asarray(points);p=np.vstack((p,p[:1]));ax.plot(p[:,0],p[:,1],**kwargs)


def make(results,output):
    plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False})
    output.mkdir(parents=True,exist_ok=True)
    overview,overview_axes=plt.subplots(1,2,figsize=(10,4.5),layout='constrained')
    for case,overview_ax in zip(results['cases'],overview_axes):
        title='Translation' if case['id'].endswith('translation') else 'Off-center full rotation'
        fine=[r for r in case['records'] if r['n']==128];plain,red=fine
        field=np.load(output/(case['id']+'.npz'))
        fig,axes=plt.subplots(2,2,figsize=(11,8.3),layout='constrained')
        ax=axes[0,0]
        image=ax.pcolormesh(field['x'],field['y'],field['phi_advection'],cmap='RdBu_r',vmin=-.15,vmax=.35,shading='nearest',rasterized=True)
        fig.colorbar(image,ax=ax,label='Numerically advected phi')
        for target in [ax,overview_ax]:
            target.contour(field['x'],field['y'],field['reference_final'],levels=[0],colors=['black'],linewidths=2)
            contour(target,plain['contours'][-1],color='#b45126',label='ENO2 / Heun')
            contour(target,red['contours'][-1],color='#157b78',linestyle='--',label='+ redistancing')
            contour(target,plain['contours'][0],color='gray',linestyle=':',label='Initial circle')
            target.set(xlim=(0,1),ylim=(0,1),xlabel='x',ylabel='y',aspect='equal',title=title+' at T=1 (N=128)')
            target.legend(fontsize=8,loc='upper left')
        ax=axes[0,1]
        for mode,color,label in [('advection-only','#b45126','Advection only'),('redistance','#157b78','With redistancing')]:
            rows=[r for r in case['records'] if r['mode']==mode]
            ax.loglog([1/r['n'] for r in rows],[r['maximum_interface_error'] for r in rows],'o-',color=color,label=label)
        ax.set(xticks=[1/128,1/64,1/32],xticklabels=['1/128','1/64','1/32'],xlabel='Grid spacing (dt also refined)',ylabel='Max sampled radial interface error',title='Worst of four positive observation times')
        ax.xaxis.set_minor_formatter(NullFormatter());ax.legend();ax.grid(alpha=.2)
        for row,color,label in zip(fine,['#b45126','#157b78'],['Advection only','With redistancing']):
            times=[r['time'] for r in row['snapshots']]
            axes[1,0].plot(times,[100*r['relative_area_bias'] for r in row['snapshots']],'o-',color=color,label=label)
            axes[1,1].plot(times,[r['band_distance_gradient_rms'] for r in row['snapshots']],'o-',color=color,label=label)
        axes[1,0].set(xlabel='Time',ylabel='Area bias (%)',title='Measured geometric area; no volume correction')
        axes[1,0].axhline(0,color='gray',linewidth=.7)
        axes[1,1].set(xlabel='Time',ylabel='RMS (|grad phi| - 1)',title='Distance quality in a 2dx analytic-interface band')
        for target in axes[1]:target.legend();target.grid(alpha=.2)
        fig.suptitle('Level-set circle: '+title+' | analytic exterior data; ENO2 + Heun\nOptional first-order redistancing can move the contour and change area',fontsize=13)
        fig.savefig(output/(case['id']+'.png'),dpi=145);plt.close(fig)
    overview.suptitle('Prescribed 2D circle motions: actual numerical zero contours\nBlack: analytic final interface; no VOF or fluid solver',fontsize=12)
    overview.savefig(output/'level-set-overview.png',dpi=145);plt.close(overview)


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--results',required=True,type=Path);p.add_argument('--output',required=True,type=Path);a=p.parse_args();make(json.loads(a.results.read_text()),a.output)
