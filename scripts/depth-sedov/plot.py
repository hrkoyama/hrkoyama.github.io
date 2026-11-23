#!/usr/bin/env python3
"""Plot only qualified saved radial fields; does not execute the PDE solver."""
import argparse
import hashlib
import json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import NullLocator

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--results',type=Path,required=True);parser.add_argument('--output',type=Path,required=True);args=parser.parse_args()
    data=json.loads(args.results.read_text());source=Path(__file__).resolve().parent;root=args.results.parent
    if data['passed'] is not True or not data['cases'][0]['passed'] or not all(data['cases'][0]['checks'].values()):raise ValueError('Only passed, saved data can qualify figures')
    for name,value in data['files_sha256'].items():
        if Path(name).name!=name or sha(root/name)!=value:raise ValueError('Changed/unsafe saved field '+name)
    for name,value in data['source_sha256'].items():
        if sha(source/name)!=value:raise ValueError('Changed numerical source '+name)
    case=data['cases'][0];rows=case['records'];finest=rows[-1];probe=case['source_radius_sensitivity']
    with np.load(root/finest['field'],allow_pickle=False) as saved:
        edges=saved['edges'];q=saved['q'];qref=saved['q_reference'];pref=saved['pressure_reference'];t=float(saved['time'])
    centers=.5*(edges[:-1]+edges[1:]);vol=np.diff(edges**3);rs=finest['reference_shock_radius'];active=centers<=1.2*rs
    l1=float(np.dot(abs(q[:,0]-qref[:,0])[active],vol[active])/np.dot(abs(qref[:,0])[active],vol[active]))
    if not np.isclose(l1,finest['active_density_l1'],rtol=1e-13):raise ValueError('Saved field/norm mismatch')
    rho=q[:,0];u=q[:,1]/rho;p=(5/3-1)*(q[:,2]-.5*q[:,1]*u)
    with np.load(root/probe['field'],allow_pickle=False) as saved:probe_q=saved['q']
    probe_rho=probe_q[:,0]
    extent=1.25*rs;pixel=np.linspace(-extent,extent,501);x,y=np.meshgrid(pixel,pixel);r=np.hypot(x,y)
    idx=np.minimum(np.searchsorted(edges,r,side='right')-1,len(rho)-1);idx=np.maximum(idx,0);image=rho[idx]
    args.output.mkdir(parents=True,exist_ok=True)
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'axes.spines.top':False,'axes.spines.right':False,'axes.labelcolor':'#173348','text.color':'#173348','axes.titlecolor':'#173348','svg.hashsalt':'atlas-sedov-2026-11-23'})
    figures=[]
    def save(fig,stem):
        for ext in ['png','svg','pdf']:
            path=args.output/(stem+'.'+ext)
            if path.exists():raise ValueError('Use a new figure output directory')
            meta={'Date':None} if ext=='svg' else ({'CreationDate':None,'ModDate':None} if ext=='pdf' else {})
            fig.savefig(path,dpi=160,metadata=meta,facecolor='white')
            if ext=='svg':path.write_text('\n'.join(row.rstrip() for row in path.read_text().splitlines())+'\n')
            figures.append({'path':path.name,'sha256':sha(path)})
        plt.close(fig)
    def disk(ax,fig):
        im=ax.imshow(image,origin='lower',extent=[-extent/rs,extent/rs,-extent/rs,extent/rs],interpolation='nearest',cmap='magma',vmin=0,vmax=max(4,float(rho.max())))
        theta=np.linspace(0,2*np.pi,401);ax.plot(np.cos(theta),np.sin(theta),'c--',lw=1.05)
        ax.set(xlabel='$x/R_s$',ylabel='$y/R_s$',title='Radial display of evolved spherical density')
        fig.colorbar(im,ax=ax,label=r'$\overline{\rho}/\rho_0$',shrink=.8)
    def profiles(ax):
        ax.plot(centers/rs,qref[:,0],c='#173348',ls='--',label='Point-blast cell-quadrature reference')
        ax.plot(centers/rs,rho,c='#bd4c27',lw=1.4,label='Finite-source radial FV, a=0.03')
        ax.plot(centers/rs,probe_rho,c='#24879a',lw=1,label='Same grid, a=0.015')
        ax.set(xlim=(0,1.25),xlabel='$r/R_s$',ylabel=r'$\overline{\rho}/\rho_0$',title='Shock and origin remain in comparison');ax.grid(alpha=.2);ax.legend(fontsize=7.2)
    fig,axes=plt.subplots(1,2,figsize=(8.2,4.55));fig.subplots_adjust(left=.08,right=.98,bottom=.28,top=.77,wspace=.36)
    fig.text(.08,.94,'SEDOV–TAYLOR  /  POINT BLAST',fontsize=17,fontweight='bold')
    fig.text(.08,.87,f'Spherical radial Euler FV  ·  gamma=5/3  ·  E=1  ·  t={t:g}  ·  N={len(rho)}',fontsize=9.5)
    disk(axes[0],fig);profiles(axes[1])
    fig.text(.08,.135,'Picture: 1D spherical-radial result shown as a section; this is not a 2D Cartesian calculation.',fontsize=8)
    fig.text(.08,.075,'Rusanov + Heun. Finite deposition radius and grid error are distinct; dashed circle is point-blast shock.',fontsize=7.8)
    save(fig,'sedov-blast-preview')
    fig,axes=plt.subplots(2,2,figsize=(11.2,9));fig.subplots_adjust(left=.09,right=.97,bottom=.17,top=.84,wspace=.35,hspace=.43)
    fig.text(.09,.95,'Sedov–Taylor verification  |  spherical radial flow',fontsize=18,fontweight='bold')
    fig.text(.09,.90,f'Fixed physical deposition a=0.03; 128/256/512 radial cells; smaller-source probe a=0.015 at N=512.',fontsize=10)
    disk(axes[0,0],fig);profiles(axes[0,1])
    axes[1,0].plot(centers/rs,pref,'--',c='#173348',label='Point-blast physical pressure mean')
    axes[1,0].plot(centers/rs,p,c='#bd4c27',label='FV pressure from conserved cell mean')
    axes[1,0].set(xlim=(0,1.25),xlabel='$r/R_s$',ylabel='$p$',title='Pressure includes the central region');axes[1,0].grid(alpha=.2);axes[1,0].legend(fontsize=7.5)
    ns=[row['n'] for row in rows]
    axes[1,1].loglog(ns,[row['active_density_l1'] for row in rows],'o-',c='#bd4c27',label='Density, origin + shock included')
    axes[1,1].loglog(ns,[row['active_pressure_l1'] for row in rows],'s-',c='#24879a',label='Pressure, origin + shock included')
    axes[1,1].set(xlabel='Radial cells N',ylabel='Volume-weighted relative L1',xticks=ns,xticklabels=[str(n) for n in ns],title='Point-blast difference within r <= 1.2 Rs')
    axes[1,1].xaxis.set_minor_locator(NullLocator());axes[1,1].grid(alpha=.2);axes[1,1].legend(fontsize=8)
    fig.text(.09,.115,f"Finest density L1={finest['active_density_l1']:.4f}; shock error={finest['shock_error_cells']:.3f} cells; all {len(case['check_details'])} frozen gates passed.",fontsize=9)
    fig.text(.09,.08,f"Halving source radius at the same grid changes density by {probe['paired_density_difference']:.4f} (relative L1); it is a separate sensitivity probe.",fontsize=8.5)
    fig.text(.09,.045,'Semi-analytic similarity ODE + split cell quadrature; tiny-core asymptote and pinned ExactPack checks documented separately.',fontsize=8.3)
    save(fig,'sedov-blast')
    (args.output/'figure-manifest.json').write_text(json.dumps({'schema_version':1,'validation_passed':True,'result_sha256':sha(args.results),'plot_sha256':sha(Path(__file__)),'files_sha256':data['files_sha256'],'geometry':'1D spherical radial section display, not a 2D computation','actual_cartesian_field':False,'n':len(rho),'figures':figures},indent=2)+'\n')
    print(json.dumps({'figures':len(figures),'passed':True,'n':len(rho),'actual_cartesian_field':False}))
if __name__=='__main__':main()
