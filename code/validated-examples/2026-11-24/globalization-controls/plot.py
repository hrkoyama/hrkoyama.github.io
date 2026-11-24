"""Saved trajectories only; analytic Rosenbrock contours are labelled context."""
import argparse
import json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--results',required=True,type=Path);parser.add_argument('--output',required=True,type=Path);args=parser.parse_args()
    path=args.results/'result.json'if args.results.is_dir()else args.results
    data=json.loads(path.read_text());case=data['cases'][0];args.output.mkdir(parents=True,exist_ok=True)
    fig,ax=plt.subplots(2,2,figsize=(11,8),layout='constrained')
    xx,yy=np.meshgrid(np.linspace(-2.,2.,160),np.linspace(-5.,4.,180))
    zz=.5*((10*(yy-xx*xx))**2+(1-xx)**2)
    ax[0,0].contour(xx,yy,np.log10(1+zz),levels=12,colors='#ced8df',linewidths=.6)
    colors={'full-newton':'#8a697e','armijo-newton':'#137f92','dogleg-trust-region':'#d78324'}
    for row in case['records']:
        if row.get('kind')not in ['rosenbrock','bratu']:continue
        color=colors[row['method']];label=row['id'].replace('rosenbrock-unit-','').replace('bratu-','')
        if row['kind']=='rosenbrock'and'-unit-'in row['id']:
            accepted=[t['x']for t in row['history']if t['accepted']]+[row['x']]
            points=np.array(accepted);ax[0,0].plot(points[:,0],points[:,1],'.-',color=color,alpha=.8,lw=1,label=label)
        if row['required_root']:
            steps=[t for t in row['history']if not t['domain_rejected']]
            values=[np.sqrt(np.mean(np.asarray(t['candidate_f'])**2))for t in steps]
            ax[0,1].semilogy([t['F_evaluations']for t in steps],np.maximum(values,1e-16),'.-',color=color,alpha=.8,label=label)
        if row['kind']=='bratu'and row['method']=='dogleg-trust-region':
            ax[1,0].plot(range(1,len(row['history'])+1),[t['delta']for t in row['history']],'.-',label=label)
    ax[0,0].plot([1],[1],'*',color='#263a48',ms=12);ax[0,0].set(xlabel='x',ylabel='y',title='Saved Rosenbrock paths; analytic residual contours',xlim=(-2,2),ylim=(-5,4));ax[0,0].legend(fontsize=6)
    ax[0,1].set(xlabel='Actual residual evaluations',ylabel='Original residual RMS',title='Required roots; exact zero displayed at 1e-16');ax[0,1].grid(alpha=.2);ax[0,1].legend(fontsize=6)
    ax[1,0].set(xlabel='Attempted step',ylabel='Euclidean trust radius',title='Bratu dogleg: accepted and rejected trials');ax[1,0].legend(fontsize=7);ax[1,0].grid(alpha=.2)
    names=[];values=[]
    for method in colors:
        rows=[r for r in case['records']if r.get('kind')in ['rosenbrock','bratu']and r.get('method')==method]
        names.append(method.replace('-',' '));values.append(sum(r['counts']['residual']for r in rows))
    ax[1,1].bar(names,values,color=list(colors.values()));ax[1,1].set(ylabel='Measured residual calls',title='All fixed starts, including diagnostic starts');ax[1,1].tick_params(axis='x',labelsize=8)
    fig.suptitle('Line search and trust regions from identical fixed starts',fontsize=14)
    fig.supxlabel('Diagnostic trajectories need not be roots. No universal method ranking is implied.',fontsize=8)
    ident=case['id']
    for suffix in ['png','svg','pdf']:
        target=args.output/(ident+'.'+suffix)
        if target.exists():raise FileExistsError(target)
        fig.savefig(target,dpi=160)
    fig.savefig(args.output/(ident+'-preview.png'),dpi=90);plt.close(fig)


if __name__=='__main__':main()
