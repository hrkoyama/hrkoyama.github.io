#!/usr/bin/env python3
"""Render only hash-qualified saved 2D fields; never execute a solver."""
import argparse,hashlib,json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import NullLocator

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def main():
    p=argparse.ArgumentParser();p.add_argument('--results',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    source=Path(__file__).resolve().parent;root=a.results.parent;result=json.loads(a.results.read_text());case=result['cases'][0]
    if not result['passed'] or not case['passed'] or not all(case['checks'].values()):raise ValueError('Only qualified passed results may be plotted')
    for name,h in result['source_sha256'].items():
        if sha(source/name)!=h:raise ValueError('Changed frozen numerical source: '+name)
    for name,h in result['files_sha256'].items():
        if Path(name).name!=name or sha(root/name)!=h:raise ValueError('Changed field/history: '+name)
    rows=case['records'];n=max(r['n'] for r in rows);mach=min(r['mach_far'] for r in rows);fields={}
    def pressure(q):return .4*(q[...,3]-.5*(q[...,1]**2+q[...,2]**2)/q[...,0])
    for variant in ['roe','miczek']:
        record=next(r for r in rows if r['n']==n and r['mach_far']==mach and r['variant']==variant)
        with np.load(root/record['field'],allow_pickle=False) as data:
            q=data['q'];x=data['x'];rho=q[...,0];u=q[...,1]/rho;v=q[...,2]/rho;h=20/n
            omega=(np.roll(v,-1,axis=0)-np.roll(v,1,axis=0)-np.roll(u,-1,axis=1)+np.roll(u,1,axis=1))/(2*h)
            fields[variant]={'omega':omega,'u':u-1,'v':v-.5,'pressure_error':(pressure(q)-pressure(data['q_reference']))/1.25}
    bound=max(float(np.max(abs(f['omega']))) for f in fields.values());assert bound>0
    plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False,'text.color':'#173348','axes.labelcolor':'#173348','axes.titlecolor':'#173348','savefig.facecolor':'white'})
    a.output.mkdir(parents=True,exist_ok=True);figures=[]
    def save(fig,stem):
        for ext in ['png','svg','pdf']:
            path=a.output/(stem+'.'+ext)
            if path.exists():raise ValueError('Use a fresh figure output directory')
            metadata={'Date':None} if ext=='svg' else ({'CreationDate':None,'ModDate':None} if ext=='pdf' else {})
            fig.savefig(path,dpi=160,metadata=metadata,facecolor='white')
            if ext=='svg':path.write_text('\n'.join(line.rstrip() for line in path.read_text().splitlines())+'\n')
            figures.append({'path':path.name,'sha256':sha(path)})
        plt.close(fig)
    def panel(ax,variant):
        f=fields[variant];im=ax.imshow(f['omega'].T,origin='lower',extent=[-10,10,-10,10],interpolation='nearest',cmap='RdBu_r',vmin=-bound,vmax=bound)
        ax.contour(x,x,f['omega'].T,levels=np.linspace(-bound,bound,13)[1:-1],colors='white',linewidths=.45,alpha=.75)
        idx=np.flatnonzero((x>=-3)&(x<=3))[::2]
        ax.quiver(x[idx],x[idx],f['u'][np.ix_(idx,idx)].T,f['v'][np.ix_(idx,idx)].T,color='#21384b',angles='xy',scale_units='xy',scale=1.3,width=.004)
        ax.set(xlim=(-3,3),ylim=(-3,3),xlabel='$x$',ylabel='$y$',xticks=[-3,0,3],yticks=[-3,0,3],title='Ordinary Roe' if variant=='roe' else 'Miczek spatial preconditioning')
        return im
    fig=plt.figure(figsize=(8.2,5.25));fig.text(.075,.945,'LOW-MACH VORTEX',fontsize=21,fontweight='bold')
    fig.text(.075,.875,f'Actual 2D Euler evolution  |  M infinity={mach:g}  |  {n} x {n} cells  |  t=0.1',fontsize=10)
    for left,variant in [(.075,'roe'),(.50,'miczek')]:im=panel(fig.add_axes([left,.26,.34,.53]),variant)
    fig.colorbar(im,cax=fig.add_axes([.905,.28,.018,.48]),label=r'$\omega_z$ from saved velocities')
    fig.text(.075,.14,'Core view [-3,3] squared; the full periodic computation uses [-10,10] squared.',fontsize=9)
    fig.text(.075,.075,'Unlimited primitive MUSCL; SSPRK(3,3), acoustic CFL=0.2. Arrows: velocity minus mean flow.',fontsize=8.4)
    fig.text(.075,.028,'Short-time fixed-input evidence; no full-period or general nonlinear stability claim.',fontsize=8.3)
    save(fig,'low-mach-vortex-preview')
    fig=plt.figure(figsize=(11.3,10.2));fig.text(.075,.968,'Low-Mach vortex  |  spatial preconditioning and physical time',fontsize=18,fontweight='bold')
    fig.text(.075,.925,'N=16/32/64; background Mach=0.1/0.01; T=0.1; beta=3; mean velocity=(1,0.5).',fontsize=10)
    for left,variant in [(.075,'roe'),(.56,'miczek')]:
        ax=fig.add_axes([left,.64,.365,.245]);im=panel(ax,variant);ax.set_xlabel('');ax.tick_params(axis='x',labelbottom=False)
    fig.colorbar(im,cax=fig.add_axes([.90,.65,.012,.22]),label=r'$\omega_z$')
    colors={.1:'#bc4b2a',.01:'#237e9a'}
    for xpos,key,title,ylabel in [(.075,'velocity_relative_l1','Velocity error: normalize by the vortex','Relative L1 of velocity perturbation'),(.56,'pressure_dynamic_l1','Pressure error: retain dynamic scaling',r'Mean $|p-p_{ref}|/(\rho_\infty |U_\infty|^2)$')]:
        ax=fig.add_axes([xpos,.335,.365,.225])
        for m in [.1,.01]:
            for variant,style in [('roe','--'),('miczek','-')]:
                selected=[r for r in rows if r['mach_far']==m and r['variant']==variant]
                ax.loglog([r['n'] for r in selected],[r[key] for r in selected],style+'o',color=colors[m],label=f'M={m:g}, '+('Roe' if variant=='roe' else 'preconditioned'))
        ax.set(xlabel='Cells per side N',ylabel=ylabel,title=title,xticks=[16,32,64],xticklabels=['16','32','64']);ax.xaxis.set_minor_locator(NullLocator());ax.grid(alpha=.2);ax.legend(fontsize=7)
    ax=fig.add_axes([.075,.115,.365,.12]);scan=next(r for r in case['linear_stability'] if r['mach_far']==.01 and r['variant']=='miczek')
    amplification=[scan['maximum_forward_Euler_spectral_radius'],scan['maximum_SSPRK3_spectral_radius']]
    ax.plot([0,1],amplification,'o',markersize=8,color='#bc4b2a');ax.axhline(1,color='#173348',ls='--',lw=1)
    ax.set(xticks=[0,1],xticklabels=['Forward Euler','SSPRK(3,3)'],xlim=(-.5,1.5),ylabel='Max sampled spectral radius',title='Uniform-state Fourier diagnostic at M=0.01')
    ax.set_ylim(.995,max(amplification)*1.015);ax.grid(alpha=.2)
    ax=fig.add_axes([.56,.115,.365,.12]);selected=[next(r for r in rows if r['mach_far']==m and r['variant']=='miczek' and r['n']==n) for m in [.1,.01]]
    ax.loglog([r['mach_far'] for r in selected],[r['acoustic_dt_diagnostic'] for r in selected],'o-',color='#237e9a',label='Acoustic diagnostic')
    ax.loglog([r['mach_far'] for r in selected],[r['convective_dt_diagnostic'] for r in selected],'s--',color='#bc4b2a',label='Convective diagnostic (not used)')
    ax.set(xlabel='Background Mach number',ylabel='Diagnostic time step',title='The explicit acoustic restriction remains');ax.legend(fontsize=7);ax.grid(alpha=.2)
    balance=max(v for r in rows for v in r['conservation_relative'])
    fig.text(.075,.055,f"{len(case['checks'])} fixed gates passed; max relative four-component periodic balance={balance:.2e}.",fontsize=9)
    fig.text(.075,.026,'Whole-plane analytic field, finite periodic-box seam, Gauss cell means and sampled linear stability have separate stated qualifications.',fontsize=8.3)
    save(fig,'low-mach-vortex')
    # The unsuccessful original spatial discretization remains visible. Read
    # its own arrays/source snapshot; never relabel them as the successful run.
    oldroot=source/'attempts/01';old=json.loads((oldroot/'results/result.json').read_text());oldcase=old['cases'][0]
    if old['passed'] or oldcase['passed']:raise ValueError('The retained original trial must remain marked failed')
    for name,h in old['source_sha256'].items():
        if sha(oldroot/name)!=h:raise ValueError('Changed original numerical source: '+name)
    for name,h in old['files_sha256'].items():
        if sha(oldroot/'results'/name)!=h:raise ValueError('Changed original saved field/history')
    original={};original_rows={}
    for variant in ['roe','miczek']:
        row=next(r for r in oldcase['records'] if r['n']==n and r['mach_far']==mach and r['variant']==variant);original_rows[variant]=row
        with np.load(oldroot/'results'/row['field'],allow_pickle=False) as z:
            original[variant]=(pressure(z['q'])-pressure(z['q_reference']))/1.25
    oldbound=max(float(np.max(abs(z))) for z in [*original.values(),*[f['pressure_error'] for f in fields.values()]]);assert oldbound>0
    fig=plt.figure(figsize=(10.6,10.2));fig.text(.075,.965,'RETAINED FAILURE  /  FULL-DOMAIN PRESSURE',fontsize=18,fontweight='bold',color='#a52b2b')
    fig.text(.075,.925,'Same physical Euler, SSPRK(3,3), CFL, grids and acceptance. Shared color scale; no core crop.',fontsize=10)
    for bottom,kind in [(.56,'original'),(.175,'current')]:
        for left,variant in [(.075,'roe'),(.535,'miczek')]:
            row=original_rows[variant] if kind=='original' else next(r for r in rows if r['variant']==variant and r['mach_far']==mach and r['n']==n)
            error=original[variant] if kind=='original' else fields[variant]['pressure_error']
            ax=fig.add_axes([left,bottom,.34,.31]);im=ax.imshow(error.T,origin='lower',extent=[-10,10,-10,10],interpolation='nearest',cmap='RdBu_r',vmin=-oldbound,vmax=oldbound)
            title=('Original constant / ' if kind=='original' else 'Current MUSCL / ')+('Roe' if variant=='roe' else 'preconditioned Roe')
            ax.set(xlabel='$x$',ylabel='$y$',title=title)
            ax.text(.03,.035,f"Mean dynamic pressure error = {row['pressure_dynamic_l1']:.5f}",transform=ax.transAxes,fontsize=8,bbox={'facecolor':'white','alpha':.9,'edgecolor':'none'})
    fig.colorbar(im,cax=fig.add_axes([.92,.215,.015,.60]),label=r'$(p-p_{ref})/(\rho_\infty |U_\infty|^2)$')
    limit=json.loads((oldroot/'acceptance.json').read_text())['limits']['finest_pressure_dynamic_l1'];failed=original_rows['miczek']['pressure_dynamic_l1']
    if not failed>limit:raise ValueError('Original pressure criterion must retain its actual failure')
    fig.text(.075,.10,f'M infinity={mach:g}, N={n}, T=0.1. Original preconditioned {failed:.5f} > unchanged {limit:g}: FAIL.',fontsize=10,color='#a52b2b')
    fig.text(.075,.055,'Current global pressure error is not always smaller with preconditioning; the full fields and whole-domain norms remain visible.',fontsize=9)
    save(fig,'low-mach-vortex-first-order')
    manifest={'schema_version':1,'validation_passed':True,'actual_cartesian_field':True,'result_sha256':sha(a.results),'plot_sha256':sha(Path(__file__)),'files_sha256':result['files_sha256'],'nx':n,'ny':n,'mach_far':mach,'display_crop':[-3,3,-3,3],'full_domain':[-10,10,-10,10],'displayed_field':'Centered periodic vorticity and velocity perturbation derived from saved actual2D conserved states. No PDE executed by plotting.','figures':figures}
    manifest['retained_failed_trial']={'passed':False,'result_sha256':sha(oldroot/'results/result.json'),'full_domain_shown':True,'file':'low-mach-vortex-first-order.png','original_pressure_dynamic_l1':failed,'unchanged_criterion':limit}
    (a.output/'figure-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n');print(json.dumps({'figures':len(figures),'passed':True,'field_shape':[n,n,4]}))


if __name__=='__main__':main()
