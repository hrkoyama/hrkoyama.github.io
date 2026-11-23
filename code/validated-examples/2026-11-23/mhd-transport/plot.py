#!/usr/bin/env python3
"""Render only saved finite-volume fields; never evolve MHD or regenerate references."""
import argparse,json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
from references.qualify import pressure


def image(fig,ax,q,extent,title,cmap='viridis',symmetric=False):
    opts={}
    if symmetric:bound=float(np.max(abs(q)));opts={'vmin':-bound,'vmax':bound}
    im=ax.imshow(q.T,origin='lower',extent=extent,aspect='equal',cmap=cmap,**opts);fig.colorbar(im,cax=make_axes_locatable(ax).append_axes('right',size='4%',pad=.06));ax.set(title=title,xlabel='x',ylabel='y')


def render(results,output):
    results=Path(results);output=Path(output);output.mkdir(parents=True,exist_ok=True);payload=json.loads(results.read_text())
    for case in payload['cases']:
        ident=case['id'];rows=[r for r in case['records'] if r['family']=='refinement'];fine=rows[-1]
        with np.load(results.parent/fine['field'],allow_pickle=False) as f:d={k:f[k] for k in f.files}
        q=d['q'];ref=d['q_reference'];hist=d['history'];times=d['times'];qh=d['q_history']
        fig,axes=plt.subplots(2,3,figsize=(13,7.5),constrained_layout=True)
        if ident=='circular-alfven-refinement':
            n=len(q);x=(np.arange(n)+.5)/n
            axes[0,0].pcolormesh(np.linspace(0,1,n+1),np.arange(6),qh[...,6],shading='flat',cmap='RdBu_r',rasterized=True);axes[0,0].set(title='Computed By: five saved times',xlabel='x',ylabel='Saved time');axes[0,0].set_yticks(np.arange(5)+.5,[f'{t:g}' for t in times])
            for component,label in [(6,'By'),(7,'Bz')]:axes[0,1].plot(x,q[:,component],label=label+' computed');axes[0,1].plot(x,ref[:,component],'--',lw=1,label=label+' analytic mean')
            axes[0,1].set(title='Final full transverse polarization',xlabel='x',ylabel='Magnetic cell mean');axes[0,1].legend(fontsize=7)
            axes[0,2].plot(x,q[:,6]-ref[:,6],label='By');axes[0,2].plot(x,q[:,7]-ref[:,7],label='Bz');axes[0,2].set(title='Final cell-mean error',xlabel='x',ylabel='Numerical minus exact');axes[0,2].legend(fontsize=8)
            title='1D circularly polarized Alfven wave: full eight-state HLLD / MC / Heun'
        elif ident=='magnetic-loop-independent':
            extent=[-1,1,-.5,.5];energy=lambda a:.5*np.sum(a[...,5:7]**2,axis=-1)
            image(fig,axes[0,0],energy(q),extent,'Computed magnetic energy')
            image(fig,axes[0,1],energy(ref),extent,'Athena++ final energy')
            image(fig,axes[0,2],q[...,6]-ref[...,6],extent,'By difference','RdBu_r',True)
            title='Genuine 2D magnetic-loop transport, T=1; official 2.5D variant v=(2,1,2)'
        else:
            extent=[-.5,.5,-.5,.5]
            image(fig,axes[0,0],q[...,0],extent,'Computed density at T=0.2')
            image(fig,axes[0,1],ref[...,0],extent,'Athena++ final / restricted')
            image(fig,axes[0,2],q[...,0]-ref[...,0],extent,'Density difference','RdBu_r',True)
            title='Late compressible ideal-MHD Orszag-Tang: interacting compression / shock structure'
        for key in fine['errors']:
            measure='relative_l2' if ident=='circular-alfven-refinement' else 'relative_l1'
            axes[1,0].loglog([r['n'] for r in rows],[r['errors'][key][measure] for r in rows],'o-',label=key)
        axes[1,0].set(title='Fixed-dt spatial refinement',xlabel='Ny' if ident=='magnetic-loop-independent' else 'N',ylabel='Relative error');axes[1,0].legend(fontsize=8);axes[1,0].grid(alpha=.2)
        axes[1,1].semilogy(hist[:,1],np.maximum(hist[:,8],1e-18),label='Fluid integral defect')
        axes[1,1].semilogy(hist[:,1],np.maximum(hist[:,6],1e-18),label='Primary native div B')
        axes[1,1].set(title='Stage constraint budgets',xlabel='t',ylabel='Stage defect (display floor 1e-18)');axes[1,1].legend(fontsize=7);axes[1,1].grid(alpha=.2)
        if ident=='postshock-orszag-tang':image(fig,axes[1,2],pressure(q),[-.5,.5,-.5,.5],'Computed pressure')
        elif ident=='circular-alfven-refinement':
            axes[1,2].plot(q[:,6],q[:,7],label='Computed');axes[1,2].plot(ref[:,6],ref[:,7],'--',label='Exact means');axes[1,2].set(title='Final transverse polarization',xlabel='By',ylabel='Bz',aspect='equal');axes[1,2].legend(fontsize=8);axes[1,2].grid(alpha=.2)
        else:
            axes[1,2].plot(hist[:,1],hist[:,7],label='Primary common-cell max div B')
            axes[1,2].axhline(fine['reference_common_cell_divergence'],color='tab:orange',ls='--',label='Reference common-cell div B at final')
            axes[1,2].set(title='Common-cell divergence',xlabel='t',ylabel='max |Dcell B|');axes[1,2].legend(fontsize=7);axes[1,2].grid(alpha=.2)
        subtitle='Analytic conserved cell means; five actual saved times' if ident=='circular-alfven-refinement' else 'Independent numerical comparisons are final-only; finite-grid references are not exact solutions'
        fig.suptitle(title+'\n'+subtitle,fontsize=11)
        for suffix in ['png','svg','pdf']:fig.savefig(output/(ident+'.'+suffix),dpi=145,bbox_inches='tight')
        plt.close(fig)
        fig,ax=plt.subplots(figsize=(7.6,4.4),constrained_layout=True)
        if ident=='circular-alfven-refinement':
            ax.pcolormesh(np.linspace(0,1,len(q)+1),np.arange(6),qh[...,6],shading='flat',cmap='RdBu_r',rasterized=True);ax.set(title='Circular Alfven wave: saved By(x,t)',xlabel='x',ylabel='Saved time');ax.set_yticks(np.arange(5)+.5,[f'{t:g}' for t in times])
        elif ident=='magnetic-loop-independent':image(fig,ax,.5*np.sum(q[...,5:7]**2,axis=-1),[-1,1,-.5,.5],'Computed magnetic loop, T=1; v=(2,1,2)')
        else:image(fig,ax,q[...,0],[-.5,.5,-.5,.5],'Computed late Orszag-Tang density, T=0.2')
        fig.savefig(output/(ident+'-preview.png'),dpi=150,bbox_inches='tight');plt.close(fig)

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--results',required=True);p.add_argument('--output',required=True);a=p.parse_args();render(a.results,a.output)
