#!/usr/bin/env python3
"""Render only qualified saved 2D states; no PDE or reference solver imports."""
import argparse
import hashlib
import json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.ticker import NullLocator

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
    p=argparse.ArgumentParser();p.add_argument('--results',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    d=json.loads(a.results.read_text());c=d['cases'][0];source=Path(__file__).resolve().parent;root=a.results.parent
    if not d['passed'] or not c['passed'] or not all(c['checks'].values()):raise ValueError('Only qualified passed data may be plotted')
    for name,h in d['files_sha256'].items():
        if Path(name).name!=name or sha(root/name)!=h:raise ValueError('Changed saved field/history')
    for name,h in d['source_sha256'].items():
        if sha(source/name)!=h:raise ValueError('Changed numerical input/source')
    rows=c['records'];fine=rows[-1]
    with np.load(root/fine['field'],allow_pickle=False) as z:q=z['q'];qr=z['q_reference'];x=z['x'];y=z['y']
    rho=q[...,0];ref=qr[...,0];error=rho-ref
    if not np.isclose(np.sum(abs(error))/np.sum(abs(ref)),fine['density_l1'],rtol=1e-13):raise ValueError('Saved norm mismatch')
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'axes.spines.top':False,'axes.spines.right':False,'text.color':'#173348','axes.labelcolor':'#173348','axes.titlecolor':'#173348','svg.hashsalt':'atlas-double-mach-2026-11-23'})
    figures=[];a.output.mkdir(parents=True,exist_ok=True)
    def save(fig,stem):
        for ext in ['png','svg','pdf']:
            path=a.output/(stem+'.'+ext)
            if path.exists():raise ValueError('Use a new figure directory')
            meta={'Date':None} if ext=='svg' else ({'CreationDate':None,'ModDate':None} if ext=='pdf' else {})
            fig.savefig(path,dpi=160,metadata=meta,facecolor='white')
            if ext=='svg':path.write_text('\n'.join(s.rstrip() for s in path.read_text().splitlines())+'\n')
            figures.append({'path':path.name,'sha256':sha(path)})
        plt.close(fig)
    def density(ax,fig):
        im=ax.imshow(rho.T,origin='lower',extent=[0,4,0,1],interpolation='nearest',aspect='equal',cmap='magma',vmin=float(rho.min()),vmax=float(rho.max()))
        levels=np.linspace(float(rho.min()),float(rho.max()),23)[1:-1]
        ax.contour(x,y,rho.T,levels=levels,colors='white',linewidths=.34,alpha=.55)
        ax.add_patch(Rectangle((1,0),1.75,.25,fill=False,edgecolor='#53d6dc',linestyle='--',linewidth=1.1))
        ax.set(xlabel='$x$',ylabel='$y$',title='Evolved 2D density / fixed near-wall ROI')
        fig.colorbar(im,ax=ax,label=r'$\overline{\rho}$',shrink=.85,pad=.025)
    fig=plt.figure(figsize=(8.2,4.55));ax=fig.add_axes([.075,.31,.84,.46])
    fig.text(.075,.94,'DOUBLE MACH  /  FINITE-GRID CHECK',fontsize=17,fontweight='bold')
    fig.text(.075,.86,f'2D Euler  |  {q.shape[0]} x {q.shape[1]} cells  |  Mach 10  |  gamma=1.4  |  t=0.2',fontsize=10)
    density(ax,fig)
    fig.text(.075,.17,'First-order HLL + Heun. A separately written MUSCL/HLL finite-grid reference is compared.',fontsize=8)
    fig.text(.075,.10,'Broad reflection pattern only: the thin wall jet and roll-up remain under-resolved.',fontsize=8)
    save(fig,'double-mach-reflection-preview')
    fig=plt.figure(figsize=(11.2,9));ax=fig.add_axes([.08,.66,.84,.23])
    fig.text(.08,.965,'Double Mach reflection  |  actual Cartesian evolution',fontsize=18,fontweight='bold')
    fig.text(.08,.925,'Fixed inputs/boundaries; Ny=16/32/64, Nx=4 Ny; reference Ny=128 with a separate Ny=64 increment.',fontsize=10)
    density(ax,fig)
    ax.set_xlabel('')
    ax=fig.add_axes([.08,.385,.84,.23]);bound=float(np.max(abs(error)))
    im=ax.imshow(error.T,origin='lower',extent=[0,4,0,1],aspect='equal',interpolation='nearest',cmap='RdBu_r',vmin=-bound,vmax=bound)
    ax.set(xlabel='$x$',ylabel='$y$',title='Signed density difference from conservatively restricted numerical reference')
    fig.colorbar(im,ax=ax,label=r'$\overline{\rho}-\overline{\rho}_{ref}$',shrink=.85,pad=.025)
    ax=fig.add_axes([.08,.115,.37,.19]);ns=[r['ny'] for r in rows]
    ax.loglog(ns,[r['density_l1'] for r in rows],'o-',c='#bd4c27',label='Primary density difference')
    ax.loglog(ns,[r['pressure_l1'] for r in rows],'s-',c='#24879a',label='Primary pressure difference')
    ax.axhline(c['reference_increment']['density_l1'],c='#bd4c27',ls='--',label='Reference density increment')
    ax.axhline(c['reference_increment']['pressure_l1'],c='#24879a',ls='--',label='Reference pressure increment')
    ax.set(xlabel='Cells across height Ny',ylabel='Relative L1',xticks=ns,xticklabels=[str(n) for n in ns],title='Grid trend, not a full-pattern order proof');ax.xaxis.set_minor_locator(NullLocator());ax.grid(alpha=.2);ax.legend(fontsize=6.6)
    ax=fig.add_axes([.57,.115,.35,.19]);j=0
    ax.plot(x,q[:,j,1]/q[:,j,0],c='#bd4c27',label='First-order primary')
    ax.plot(x,qr[:,j,1]/qr[:,j,0],c='#173348',ls='--',label='Restricted MUSCL reference')
    ax.set(xlim=(1,2.75),xlabel='$x$',ylabel='Tangential velocity u',title=f'Near-wall row y={y[j]:.5f}; unresolved jet');ax.grid(alpha=.2);ax.legend(fontsize=7)
    fig.text(.08,.055,f"Finest density L1={fine['density_l1']:.4f}; upper incident-front difference={fine['incident_front_error_cells']:.2f} cells; {len(c['checks'])} fixed gates passed.",fontsize=9)
    fig.text(.08,.023,'Finite-grid reference, cell-center initialization and sampled moving boundary: differences are not exact 2D solution errors.',fontsize=8.5)
    save(fig,'double-mach-reflection')
    (a.output/'figure-manifest.json').write_text(json.dumps({'schema_version':1,'validation_passed':True,'result_sha256':sha(a.results),'plot_sha256':sha(Path(__file__)),'files_sha256':d['files_sha256'],'actual_cartesian_field':True,'geometry':'Full 2D Cartesian Euler evolution, indexed[x,y,conserved]','nx':q.shape[0],'ny':q.shape[1],'figures':figures},indent=2)+'\n')
    print(json.dumps({'figures':len(figures),'passed':True,'nx':q.shape[0],'ny':q.shape[1]}))
if __name__=='__main__':main()
