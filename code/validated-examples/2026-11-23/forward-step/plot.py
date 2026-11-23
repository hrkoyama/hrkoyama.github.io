#!/usr/bin/env python3
"""Draw qualified saved fluid fields only; never run a PDE/reference solver."""
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

def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def main():
    parser = argparse.ArgumentParser(); parser.add_argument('--results',type=Path,required=True); parser.add_argument('--output',type=Path,required=True); args = parser.parse_args()
    result = json.loads(args.results.read_text()); case = result['cases'][0]; root = args.results.parent; source = Path(__file__).resolve().parent
    if not result['passed'] or not case['passed'] or not all(case['checks'].values()): raise ValueError('Only qualified passed data may be plotted')
    for name,digest in result['files_sha256'].items():
        if Path(name).name != name or sha(root/name) != digest: raise ValueError('Changed saved field/history')
    for name,digest in result['source_sha256'].items():
        if sha(source/name) != digest: raise ValueError('Changed numerical input/source')
    rows = case['records']; fine = rows[-1]
    with np.load(root/fine['field'],allow_pickle=False) as z:
        q = z['q']; qr = z['q_reference']; fluid = z['fluid']; x = z['x']; y = z['y']
    rho,ref = q[...,0],qr[...,0]; error = rho-ref
    if not np.isclose(np.sum(abs(error[fluid]))/np.sum(abs(ref[fluid])),fine['density_l1'],rtol=1e-13): raise ValueError('Saved norm mismatch')
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'axes.spines.top':False,'axes.spines.right':False,'text.color':'#173348','axes.labelcolor':'#173348','axes.titlecolor':'#173348','svg.hashsalt':'atlas-forward-step-2026-11-23'})
    figures = []; args.output.mkdir(parents=True,exist_ok=True)
    def save(fig,stem):
        for ext in ['png','svg','pdf']:
            path = args.output/(stem+'.'+ext)
            if path.exists(): raise ValueError('Use a new figure directory')
            meta = {'Date':None} if ext=='svg' else ({'CreationDate':None,'ModDate':None} if ext=='pdf' else {})
            fig.savefig(path,dpi=160,metadata=meta,facecolor='white')
            if ext=='svg': path.write_text('\n'.join(s.rstrip() for s in path.read_text().splitlines())+'\n')
            figures.append({'path':path.name,'sha256':sha(path)})
        plt.close(fig)
    def step(ax):
        ax.add_patch(Rectangle((.6,0),2.4,.2,facecolor='#ccd5dd',edgecolor='#173348',linewidth=1.))
        ax.set(xlim=(0,3),ylim=(0,1),xlabel='$x$',ylabel='$y$')
    def density(ax,fig):
        field = np.ma.array(rho.T,mask=~fluid.T)
        im = ax.imshow(field,origin='lower',extent=[0,3,0,1],interpolation='nearest',aspect='equal',cmap='magma',vmin=float(rho[fluid].min()),vmax=float(rho[fluid].max()))
        levels = np.linspace(float(rho[fluid].min()),float(rho[fluid].max()),24)[1:-1]
        ax.contour(x,y,field,levels=levels,colors='white',linewidths=.35,alpha=.55)
        step(ax); ax.set_title('Evolved 2D density / aligned solid step')
        fig.colorbar(im,ax=ax,label=r'$\overline{\rho}$',shrink=.85,pad=.025)
    fig = plt.figure(figsize=(8.2,4.65)); ax = fig.add_axes([.075,.30,.84,.47])
    fig.text(.075,.94,'FORWARD STEP  /  MACH 3',fontsize=18,fontweight='bold')
    fig.text(.075,.86,f'2D Euler  |  {q.shape[0]} x {q.shape[1]} cells  |  gamma=1.4  |  t=4',fontsize=10)
    density(ax,fig)
    fig.text(.075,.17,'First-order HLL + Heun; actual fluid-cell evolution with stationary slip walls.',fontsize=8.5)
    fig.text(.075,.10,'No corner entropy reset. Thin slip lines and corner-generated structure remain unresolved.',fontsize=8.5)
    save(fig,'forward-step-m3-preview')
    fig = plt.figure(figsize=(11.2,9.2)); ax = fig.add_axes([.08,.66,.84,.23])
    fig.text(.08,.965,'Mach-3 forward step  |  actual Cartesian evolution',fontsize=18,fontweight='bold')
    fig.text(.08,.925,'Primary Ny=20/40/80; separately implemented MUSCL finite-grid references Ny=80/160.',fontsize=10)
    density(ax,fig); ax.set_xlabel(''); ax.tick_params(axis='x',labelbottom=False)
    ax = fig.add_axes([.08,.385,.84,.23]); bound = float(np.max(abs(error[fluid])))
    im = ax.imshow(np.ma.array(error.T,mask=~fluid.T),origin='lower',extent=[0,3,0,1],aspect='equal',interpolation='nearest',cmap='RdBu_r',vmin=-bound,vmax=bound)
    step(ax); ax.set_title('Signed density difference from conservatively restricted numerical reference')
    fig.colorbar(im,ax=ax,label=r'$\overline{\rho}-\overline{\rho}_{ref}$',shrink=.85,pad=.025)
    ax = fig.add_axes([.08,.115,.37,.19]); ns = [r['ny'] for r in rows]
    ax.loglog(ns,[r['density_l1'] for r in rows],'o-',c='#bd4c27',label='Primary density difference')
    ax.loglog(ns,[r['pressure_l1'] for r in rows],'s-',c='#24879a',label='Primary pressure difference')
    ax.axhline(case['reference_increment']['density_l1'],c='#bd4c27',ls='--',label='Reference density increment')
    ax.axhline(case['reference_increment']['pressure_l1'],c='#24879a',ls='--',label='Reference pressure increment')
    ax.set(xlabel='Cells across height Ny',ylabel='Relative L1 on fluid cells',xticks=ns,xticklabels=[str(n) for n in ns],title='Grid trend, not an exact2D error')
    ax.xaxis.set_minor_locator(NullLocator()); ax.grid(alpha=.2); ax.legend(fontsize=6.5)
    ax = fig.add_axes([.57,.115,.35,.19]); j = int(np.flatnonzero(y>.2)[0])
    def entropy(state):
        r = state[...,0]; p = .4*(state[...,3]-.5*(state[...,1]**2+state[...,2]**2)/r)
        return np.log(p/r**1.4)
    ax.plot(x,entropy(q)[:,j],c='#bd4c27',label='First-order primary')
    ax.plot(x,entropy(qr)[:,j],c='#173348',ls='--',label='Restricted MUSCL reference')
    ax.set(xlim=(.6,3),xlabel='$x$',ylabel=r'$\log(p/\rho^{\gamma})$',title=f'First fluid row above step: y={y[j]:.5f}')
    ax.grid(alpha=.2); ax.legend(fontsize=7)
    fig.text(.08,.055,f"Finest density L1={fine['density_l1']:.4f}; full fluid region retained; {len(case['checks'])} fixed gates passed.",fontsize=9)
    fig.text(.08,.023,'Same no-corner-fix benchmark variant. Finite-grid reference differences are not exact2D solution errors or error bounds.',fontsize=8.4)
    save(fig,'forward-step-m3')
    (args.output/'figure-manifest.json').write_text(json.dumps({'schema_version':1,'validation_passed':True,'result_sha256':sha(args.results),'plot_sha256':sha(Path(__file__)),'files_sha256':result['files_sha256'],
        'actual_cartesian_field':True,'geometry':'Actual2D aligned forward-facing step; solid cells masked, never interpolated as fluid','nx':q.shape[0],'ny':q.shape[1],'figures':figures},indent=2)+'\n')
    print(json.dumps({'figures':len(figures),'passed':True,'nx':q.shape[0],'ny':q.shape[1]}))

if __name__ == '__main__': main()
