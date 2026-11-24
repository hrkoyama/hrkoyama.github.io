"""Saved-data DAE figures. No solver or reference-generator imports."""
import argparse
import json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def save(fig,output,stem,preview=False):
    for ext in ('png','svg','pdf'):fig.savefig(output/(stem+'.'+ext),dpi=135,bbox_inches='tight')
    if preview:fig.savefig(output/(stem+'-preview.png'),dpi=90,bbox_inches='tight')
    plt.close(fig)


def index1(root,out):
    ident='index1-dae-consistent-initialization';fig,axes=plt.subplots(1,2,figsize=(12,4.6),layout='constrained')
    d=np.load(root/'index1-BE-64.npz');ref=np.load(root/'index1-BE-64-reference.npz')
    axes[0].plot(d['time'],d['states'][:,0],label='BE y');axes[0].plot(d['time'],d['states'][:,1],label='BE z')
    axes[0].plot(d['time'],ref['reference'][:,0],'k--',label='Authored exact y');axes[0].plot(d['time'],ref['reference'][:,1],'k:',label='Authored exact z')
    axes[0].set(xlabel='Model time',ylabel='Dimensionless state',title='Positive index-one branch');axes[0].legend(fontsize=8)
    for n in (16,32,64):
        a=np.load(root/('index1-BE-'+str(n)+'.npz'));b=np.load(root/('index1-BE-'+str(n)+'-reference.npz'))
        axes[1].plot(a['time'],np.max(np.abs(b['error']),axis=1),label='N = '+str(n))
    axes[1].set(xlabel='Model time',ylabel='Maximum component error',title='Time discretization error');axes[1].legend()
    fig.suptitle('Consistent initialization and a manufactured index-one DAE');save(fig,out,ident,True)
    fig,axes=plt.subplots(1,2,figsize=(12,4.6),layout='constrained')
    for n in (16,32,64):
        a=np.load(root/('index1-BE-'+str(n)+'.npz'))
        axes[0].plot(a['time'],a['step_residuals'][:,0],label='F1, N='+str(n));axes[1].plot(a['time'],a['step_residuals'][:,1],label='F2, N='+str(n))
    axes[0].set(ylabel='Derivative-unit differential residual',xlabel='Model time',yscale='symlog')
    axes[1].set(ylabel='Algebraic residual z³ − y²',xlabel='Model time',yscale='symlog')
    for ax in axes:ax.legend(fontsize=8);ax.grid(alpha=.25)
    fig.suptitle('Separate residual units; zeros retained on symmetric log axes');save(fig,out,ident+'-diagnostics')


def robertson(root,out):
    ident='robertson-conservation-dae';d=np.load(root/'robertson-residual_dae-r4.npz');ref=np.load(root/'robertson-residual_dae-r4-reference.npz')
    official=json.loads((Path(__file__).parent/'ida-printed-values.json').read_text())['printed_rows']
    fig,axes=plt.subplots(1,3,figsize=(13,4.3),layout='constrained')
    for k,ax in enumerate(axes):
        ax.plot(d['time'],d['states'][:,k],label='Own residual DAE / BE')
        ax.plot(d['time'],ref['reference'][:,k],'k--',label='Tight Radau reference')
        ax.plot([float(x['t']) for x in official],[float(x['y'][k]) for x in official],'o',mfc='none',label='Stored official IDA print')
        ax.set(xlabel='Model time',ylabel='Concentration y'+str(k+1),title='Species '+str(k+1));ax.ticklabel_format(axis='y',style='sci',scilimits=(-3,3))
    axes[0].legend(fontsize=7);fig.suptitle('Robertson conservation DAE; no new IDA execution');save(fig,out,ident,True)
    fig,axes=plt.subplots(1,2,figsize=(12,4.6),layout='constrained')
    for form in ('residual_dae','full_ode'):
        for factor in (1,2,4):
            a=np.load(root/('robertson-'+form+'-r'+str(factor)+'.npz'))
            label=form+', refinement '+str(factor)
            axes[0].plot(a['time'],np.sum(a['states'],axis=1)-1,label=label)
            axes[1].plot(a['time'],np.max(np.abs(a['step_residuals'])/np.array([1.,1e-4,1.]),axis=1),label=label)
    axes[0].set(xlabel='Model time',ylabel='Mass defect y1 + y2 + y3 − 1',yscale='symlog')
    axes[1].set(xlabel='Model time',ylabel='Scaled update-residual maximum norm',yscale='symlog')
    for ax in axes:ax.legend(fontsize=7);ax.grid(alpha=.25)
    fig.suptitle('Conservation and nonlinear residuals are separate checks');save(fig,out,ident+'-diagnostics')


def pendulum(root,out):
    ident='high-index-pendulum';n=2000
    a=np.load(root/('pendulum-consistent-underlying-'+str(n)+'.npz'));ref=np.load(root/('pendulum-consistent-underlying-'+str(n)+'-reference.npz'))
    fig,axes=plt.subplots(1,2,figsize=(12,4.6),layout='constrained')
    axes[0].plot(a['states'][:,0],a['states'][:,1],label='Underlying ODE / RK4');axes[0].plot(ref['reference'][:,0],ref['reference'][:,1],'k--',label='Jacobi turning-point reference')
    axes[0].set(xlabel='qx',ylabel='qy',aspect='equal',title='Consistent orbit');axes[0].legend(fontsize=8)
    for kind in ('underlying','stabilized'):
        b=np.load(root/('pendulum-radial-'+kind+'-'+str(n)+'-constraints.npz'));tt=np.linspace(0.,20.,len(b['C']))
        axes[1].plot(tt,b['C'],label=kind+' C');axes[1].plot(tt,b['exact_C'],'k:',linewidth=.9)
    axes[1].set(xlabel='Model time',ylabel='C = (q · q − 1) / 2',title='Explicit off-manifold controls');axes[1].legend(fontsize=8)
    fig.suptitle('Index reduction, constraint drift and explicit stabilization');save(fig,out,ident,True)
    fig,axes=plt.subplots(1,2,figsize=(12,4.6),layout='constrained')
    for kind in ('underlying','stabilized'):
        a=np.load(root/('pendulum-radial-'+kind+'-'+str(n)+'.npz'));b=np.load(root/('pendulum-radial-'+kind+'-'+str(n)+'-constraints.npz'))
        axes[0].plot(a['time'],b['D'],label=kind+' q · v');axes[0].plot(a['time'],b['exact_D'],'k:',linewidth=.9)
        axes[1].plot(a['time'],b['H']-b['H'][0],label=kind+' energy change');axes[1].plot(a['time'],b['H']-b['H'][0]-b['work'],'--',label=kind+' energy minus work')
    axes[0].set(xlabel='Model time',ylabel='Velocity constraint q · v',yscale='symlog');axes[1].set(xlabel='Model time',ylabel='Energy / constraint-work balance',yscale='symlog')
    for ax in axes:ax.legend(fontsize=8);ax.grid(alpha=.25)
    fig.suptitle('Inconsistent controls obey their own constraint and work laws');save(fig,out,ident+'-diagnostics')


def main():
    p=argparse.ArgumentParser();p.add_argument('--results',required=True,type=Path);p.add_argument('--output',required=True,type=Path);args=p.parse_args()
    root=args.results if args.results.is_dir() else args.results.parent
    assert json.loads((root/'result.json').read_text())['passed'] is True
    args.output.mkdir(parents=True,exist_ok=True)
    for fn in (index1,robertson,pendulum):fn(root,args.output)


if __name__=='__main__':main()
