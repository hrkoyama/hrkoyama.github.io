"""Render only saved arrays/records; never import a solver or generate references."""
import argparse
import json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

TITLES={'robertson-stiff-kinetics':'Robertson: stiff kinetics and actual error',
        'van-der-pol-stiff-transition':'Van der Pol: early stiffness transition',
        'rk45-dense-events':'RK45: dense output and located events',
        'strang-boundary-order-reduction':'Strang splitting: boundary compatibility'}


def load(directory, name):
    with np.load(directory/(name+'.npz'),allow_pickle=False) as p:return {k:p[k].copy() for k in p.files}


def save(fig, output, ident):
    fig.tight_layout(rect=(0,0,1,.96))
    for ext in ('png','svg','pdf'):
        path=output/(ident+'.'+ext)
        if path.exists():raise FileExistsError('Fresh presentation output required: '+str(path))
        fig.savefig(path,dpi=155,bbox_inches='tight')
    plt.close(fig)


def stiff_figures(directory, output, case):
    ident=case['id'];robertson=ident=='robertson-stiff-kinetics'
    fig,axs=plt.subplots(2,2,figsize=(12,8));preview,pax=plt.subplots(1,2,figsize=(9,3.7))
    if robertson:
        data=load(directory,'robertson-sdirk2-2048')
        times,states=data['times'],data['states']
        for ax in (axs[0,0],pax[0]):
            ax.plot(times,states[:,0],label='SDIRK2: y1');ax.plot(times,states[:,2],label='SDIRK2: y3')
            ax.plot(data['observation_times'],data['reference'][:,0],'.',label='qualified Radau: y1')
            ax.set(xlabel='time',ylabel='concentration');ax.set_xscale('symlog',linthresh=1e-4);ax.legend(fontsize=7)
        axs[0,1].plot(times,states[:,1]/1e-4,label='y2 / 1e-4');axs[0,1].plot(data['observation_times'],data['reference'][:,1]/1e-4,'.',label='qualified Radau')
        axs[0,1].set(xlabel='time',ylabel='scaled intermediate species');axs[0,1].set_xscale('symlog',linthresh=1e-4);axs[0,1].legend(fontsize=8)
        for ax in (axs[1,0],pax[1]):
            for method in ('bdf2','sdirk2'):
                rows=[r for r in case['records'] if r['method']==method]
                ax.loglog([.4/r['steps'] for r in rows],[r['sampled_weighted_linf'] for r in rows],'-o',label=method.upper())
            ax.set(xlabel='fixed time step',ylabel='sampled weighted maximum error');ax.legend(fontsize=8);ax.grid(alpha=.25)
        rows=case['records'];xx=np.arange(len(rows));axs[1,1].bar(xx,[r['linear_solves'] for r in rows],label='linear solves');axs[1,1].bar(xx,[r['factorizations'] for r in rows],label='factorizations')
        axs[1,1].set(xlabel='CSV run index (zero based)',ylabel='actual work count');axs[1,1].legend(fontsize=8)
    else:
        for mu,ax in [(1,axs[0,0]),(100,axs[0,1])]:
            data=load(directory,f'vdp-mu{mu}-sdirk2-1024')
            if mu==1:
                ax.plot(data['states'][:,0],data['states'][:,1],label='SDIRK2');ax.plot(data['reference'][:,0],data['reference'][:,1],'.',label='qualified Radau');ax.set(xlabel='x',ylabel='v',title='mu = 1 phase plane')
            else:
                ax.plot(data['times'],data['states'][:,1],label='SDIRK2');ax.plot(data['observation_times'],data['reference'][:,1],'.',label='qualified Radau');ax.set(xlabel='time',ylabel='v',title='mu = 100 initial layer');ax.set_xscale('symlog',linthresh=1e-3)
            ax.legend(fontsize=8)
            pa=pax[0 if mu==1 else 1];pa.plot(data['states'][:,0],data['states'][:,1],label='SDIRK2');pa.plot(data['reference'][:,0],data['reference'][:,1],'.',label='qualified Radau');pa.set(xlabel='x',ylabel='v',title=f'mu = {mu}, 0 <= t <= 2');pa.legend(fontsize=7)
        for mu in (1,100):
            for method in ('bdf2','sdirk2'):
                rows=[r for r in case['records'] if r['mu']==mu and r['method']==method]
                axs[1,0].loglog([2/r['steps'] for r in rows],[r['sampled_weighted_linf'] for r in rows],'-o',label=f'{method.upper()}, mu {mu}')
            rows=[r for r in case['records'] if r['mu']==mu and r['method']=='sdirk2-step-doubling']
            axs[1,1].loglog([r['rtol'] for r in rows],[r['sampled_weighted_linf'] for r in rows],'-o',label=f'mu {mu}')
        axs[1,0].set(xlabel='fixed time step',ylabel='sampled maximum error');axs[1,0].legend(fontsize=7)
        study=case['study_results']['mu1_tight_global_goal']
        axs[1,1].axhline(study['requested_global_bound'],color='black',linestyle=':',label='original mu = 1 global goal')
        status='met' if study['target_met'] else 'NOT met'
        axs[1,1].set(xlabel='requested local rtol',ylabel='actual sampled global error',title='Local control; global goal '+status)
        axs[1,1].legend(fontsize=7)
        note=('First study: 208/209 original targets; mu = 1 global goal was NOT met. '
              'Current goal '+status+'; reporting checks are separate.')
        fig.text(.5,-.015,note,ha='center',fontsize=8)
        preview.text(.5,-.015,'First study: 208/209; mu = 1 global goal 2e-5 NOT met. Current decision: '+status+'.',ha='center',fontsize=8)
    fig.suptitle(TITLES[ident]);preview.suptitle(TITLES[ident]);save(fig,output,ident);save(preview,output,ident+'-preview')


def rk_figures(directory, output, case):
    ident=case['id'];data=load(directory,'rk45-tight-hmax0.4')
    trials=json.loads((directory/'rk45-tight-hmax0.4-trials.json').read_text())
    fig,axs=plt.subplots(2,2,figsize=(12,8));preview,pax=plt.subplots(1,2,figsize=(9,3.7))
    for ax in (axs[0,0],pax[0]):
        ax.plot(data['times'],data['states'][:,0],'o-',markersize=2.5,label='accepted full endpoints')
        ax.plot(data['observation_times'],data['reference'][:,0],'--',label='analytic reference (saved)')
        ax.plot(data['root_times'],np.zeros_like(data['root_times']),'x',markersize=7,label='located roots');ax.set(xlabel='time',ylabel='y1');ax.legend(fontsize=7)
    for ax in (axs[0,1],pax[1]):
        for accepted,label,marker in [(True,'accepted','o'),(False,'rejected','x')]:
            rows=[r for r in trials['attempts'] if r['accepted']==accepted]
            ax.scatter([r['time'] for r in rows],[r['step'] for r in rows],marker=marker,s=21,label=label)
        ax.set(xlabel='trial starting time',ylabel='attempted step');ax.legend(fontsize=8)
    axs[1,0].plot(data['observation_times'],np.max(np.abs(data['observed']-data['reference']),axis=1))
    axs[1,0].set(xlabel='off-mesh time',ylabel='dense-output maximum error');axs[1,0].set_yscale('symlog',linthresh=1e-13)
    for maximum in (.4,.1):
        rows=[r for r in case['records'] if r['max_step']==maximum and not r['terminal']]
        axs[1,1].loglog([r['rtol'] for r in rows],[r['event_time_abs'] for r in rows],'-o',label=f'max step {maximum}')
    axs[1,1].set(xlabel='requested local rtol',ylabel='actual event-time error');axs[1,1].legend(fontsize=8)
    fig.suptitle(TITLES[ident]);preview.suptitle(TITLES[ident]);save(fig,output,ident);save(preview,output,ident+'-preview')


def boundary_figures(directory, output, case):
    ident=case['id'];data=load(directory,'boundary-n127-strang-boundary-corrected-64');raw=load(directory,'boundary-n127-strang-unmodified-64')
    fig,axs=plt.subplots(2,2,figsize=(12,8));preview,pax=plt.subplots(1,2,figsize=(9,3.7))
    mesh=axs[0,0].pcolormesh(data['x'],data['times'],data['states'],shading='nearest');fig.colorbar(mesh,ax=axs[0,0],label='u on interior nodes')
    axs[0,0].set(xlabel='x',ylabel='physical time',title='1D field, five saved time rows')
    for ax in (axs[0,1],pax[0]):
        ax.plot(data['x'],raw['states'][-1],label='unmodified Strang');ax.plot(data['x'],data['states'][-1],label='boundary corrected')
        ax.plot(data['x'],data['reference'][-1],'--',label='same-FD reference');ax.plot(data['x'],data['continuum'][-1],':',label='continuum exact (saved)')
        ax.set(xlabel='x',ylabel='u at t=0.1');ax.legend(fontsize=7)
    for n in (31,63,127):
        for method,linestyle in [('strang-unmodified','--'),('strang-boundary-corrected','-')]:
            rows=[r for r in case['records'] if r['n']==n and r['method']==method]
            axs[1,0].loglog([r['dt'] for r in rows],[r['temporal_linf'] for r in rows],linestyle+'o',label=f'{n}, '+('raw' if method.endswith('unmodified') else 'corrected'))
    axs[1,0].set(xlabel='time step',ylabel='temporal maximum error vs same FD');axs[1,0].legend(fontsize=6)
    rows=[r for r in case['records'] if r['method']=='strang-boundary-corrected' and r['steps']==64]
    axs[1,1].loglog([1/(r['n']+1) for r in rows],[r['reference_spatial_linf'] for r in rows],'-o');axs[1,1].set(xlabel='space step',ylabel='reference spatial error vs continuum')
    for method in ('strang-unmodified','strang-boundary-corrected','lie-unmodified'):
        rows=[r for r in case['records'] if r['n']==127 and r['method']==method]
        pax[1].loglog([r['dt'] for r in rows],[r['temporal_linf'] for r in rows],'-o',label=method.replace('strang-','').replace('lie-unmodified','Lie'))
    pax[1].set(xlabel='time step',ylabel='temporal maximum error');pax[1].legend(fontsize=7)
    saved_steps=sorted({r['dt'] for r in case['records'] if r['n']==127})
    pax[1].set_xticks(saved_steps,[f'{step:.1e}' for step in saved_steps])
    pax[1].tick_params(axis='x',which='minor',labelbottom=False)
    fig.suptitle(TITLES[ident]);preview.suptitle(TITLES[ident]);save(fig,output,ident);save(preview,output,ident+'-preview')


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--results',required=True,type=Path);parser.add_argument('--output',required=True,type=Path);args=parser.parse_args()
    path=args.results/'result.json' if args.results.is_dir() else args.results
    result=json.loads(path.read_text())
    if result.get('passed') is not True:raise ValueError('Plot only actual successful saved science')
    args.output.mkdir(parents=True,exist_ok=True)
    for case in result['cases']:
        if case['id'] in ('robertson-stiff-kinetics','van-der-pol-stiff-transition'):stiff_figures(path.parent,args.output,case)
        elif case['id']=='rk45-dense-events':rk_figures(path.parent,args.output,case)
        else:boundary_figures(path.parent,args.output,case)


if __name__=='__main__':main()
