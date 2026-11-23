#!/usr/bin/env python3
"""Render only passed, hash-bound saved fields. Never executes a PDE solver."""
import argparse
import hashlib
import json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import NullLocator


def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--results',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();data=json.loads(args.results.read_text());root=args.results.parent
    if data.get('passed') is not True or data['cases'][0].get('passed') is not True or not all(data['cases'][0]['checks'].values()):raise ValueError('Only passed saved results may be rendered as qualified figures')
    for name,value in data['files_sha256'].items():
        if Path(name).name!=name or sha(root/name)!=value:raise ValueError('Changed/unsafe saved field: '+name)
    source=Path(__file__).resolve().parent
    for name,value in data['source_sha256'].items():
        if sha(source/name)!=value:raise ValueError('Changed numerical source '+name)
    rows=data['cases'][0]['records'];finest=rows[-1]
    with np.load(root/finest['field'],allow_pickle=False) as field:
        q=field['q'];edges=field['edges'];exact=field['density_reference'];time=float(field['time'])
    rho=q[...,0];n=len(rho);dx=edges[1]-edges[0];centers=.5*(edges[:-1]+edges[1:])
    l1=float(np.sum(abs(rho-exact))/np.sum(abs(exact)))
    if not np.isclose(l1,finest['density_l1'],rtol=1e-13,atol=1e-15):raise ValueError('Saved norm/field mismatch')
    args.output.mkdir(parents=True,exist_ok=True)
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'axes.spines.top':False,'axes.spines.right':False,'axes.labelcolor':'#183849','text.color':'#183849','axes.titlecolor':'#183849','svg.hashsalt':'atlas-noh-cartesian-2026-11-23'})
    image_records=[]
    def save(fig,stem):
        for ext in ['png','svg','pdf']:
            target=args.output/(stem+'.'+ext)
            if target.exists():raise ValueError('Use a new figure output directory')
            meta={'Date':None} if ext=='svg' else ({'CreationDate':None,'ModDate':None} if ext=='pdf' else {})
            fig.savefig(target,dpi=160,metadata=meta,facecolor='white')
            if ext=='svg':target.write_text('\n'.join(x.rstrip() for x in target.read_text().splitlines())+'\n')
            image_records.append({'path':target.name,'sha256':sha(target)})
        plt.close(fig)
    def density(ax,fig):
        maximum=max(16.,float(np.max(rho)))
        im=ax.imshow(rho,origin='lower',extent=[edges[0],edges[-1],edges[0],edges[-1]],interpolation='nearest',cmap='viridis',vmin=0,vmax=maximum)
        theta=np.linspace(0,2*np.pi,401);ax.plot(time/3*np.cos(theta),time/3*np.sin(theta),'w--',lw=1.1)
        ax.set(xlabel='$x/L$',ylabel='$y/L$',title='Evolved 2D density; exact shock dashed')
        fig.colorbar(im,ax=ax,label=r'$\overline{\rho}/\rho_0$',shrink=.82)
    def rays(ax):
        radius=np.linspace(0,np.sqrt(2)*edges[-1],800);exact_point=np.where(radius<time/3,16,1+time/np.maximum(radius,1e-100))
        ax.plot(radius,exact_point,'--',c='#183849',label='Analytic radial point profile',lw=1.3)
        ax.plot(centers[n//2:],.5*(rho[n//2]+rho[n//2-1])[n//2:],c='#23788b',label='Axis (interpolated means)')
        ax.plot(np.sqrt(2)*centers[n//2:],np.diag(rho)[n//2:],c='#c35231',label='Diagonal cell means')
        ax.set(xlabel='$r/L$',ylabel=r'$\rho/\rho_0$',xlim=(0,np.sqrt(2)*edges[-1]),title='Grid orientation remains visible')
        ax.grid(alpha=.2);ax.legend(fontsize=7.5,loc='upper right')
    fig,axes=plt.subplots(1,2,figsize=(8.2,4.55));fig.subplots_adjust(left=.075,right=.98,bottom=.29,top=.77,wspace=.32)
    fig.text(.075,.94,'NOH  /  2D CARTESIAN',fontsize=19,fontweight='bold')
    fig.text(.075,.87,f'Full-square Euler FV  ·  {n} × {n} cells  ·  t = {time:g}  ·  initial pressure = 0',fontsize=10)
    density(axes[0],fig);rays(axes[1])
    fig.text(.075,.13,'Both momentum components and x/y fluxes evolve; no radial reduction or symmetry projection.',fontsize=8)
    fig.text(.075,.075,'Rusanov + Heun; first-order space. Origin heating and finite-grid anisotropy are retained.',fontsize=8)
    save(fig,'noh-cartesian-2d-preview')
    fig,axes=plt.subplots(2,2,figsize=(11.2,9));fig.subplots_adjust(left=.09,right=.97,bottom=.16,top=.84,hspace=.43,wspace=.35)
    fig.text(.09,.95,'Noh verification  |  actual 2D Cartesian flow',fontsize=19,fontweight='bold')
    fig.text(.09,.90,f'Gamma=5/3; rho0=1; inward speed=1; p0=0; t={time:g}; N={n}.  All 49 fixed gates passed.',fontsize=10)
    density(axes[0,0],fig)
    err=(rho-exact)/16;limit=float(np.max(abs(err)))
    im=axes[0,1].imshow(err,origin='lower',extent=[edges[0],edges[-1],edges[0],edges[-1]],interpolation='nearest',cmap='RdBu_r',vmin=-limit,vmax=limit)
    axes[0,1].set(xlabel='$x/L$',ylabel='$y/L$',title='Signed density error / downstream density')
    fig.colorbar(im,ax=axes[0,1],shrink=.82)
    rays(axes[1,0]);ns=[r['n'] for r in rows]
    axes[1,1].loglog(ns,[r['density_l1'] for r in rows],'o-',c='#23788b',label='Whole square, origin + shock included')
    axes[1,1].loglog(ns,[r['core_density_l1'] for r in rows],'s-',c='#c35231',label='Core, origin included')
    axes[1,1].set(xlabel='Cartesian cells per side N',ylabel='Relative density L1',title='Three lightweight refinements',xticks=ns,xticklabels=[str(v) for v in ns]);axes[1,1].grid(alpha=.2);axes[1,1].legend(fontsize=8)
    axes[1,1].xaxis.set_minor_locator(NullLocator())
    fig.text(.09,.095,f"Finest: axis/diagonal shock difference = {finest['shock_axis_diagonal_difference_cells']:.3f} dx (not monotone over these grids).",fontsize=9)
    fig.text(.09,.065,f"Maximum center internal-energy excess = {100*finest['center_max_internal_energy_excess']:.2f}%; exact D4 parity is not continuous rotational symmetry.",fontsize=9)
    fig.text(.09,.035,'Error map/norms use split cell quadrature, checked at orders64/128. Ray curve is a point reference; color scales include all field values.',fontsize=8)
    save(fig,'noh-cartesian-2d')
    manifest={'schema_version':1,'validation_passed':True,'result_sha256':sha(args.results),'plot_sha256':sha(Path(__file__)),'files_sha256':data['files_sha256'],'n':n,'actual_cartesian_field':True,'display_interpolation':'nearest','geometry':'full square 2D; not a rotated radial computation','figures':image_records}
    (args.output/'figure-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    print(json.dumps({'figures':len(image_records),'n':n,'passed':True}))


if __name__=='__main__':main()
