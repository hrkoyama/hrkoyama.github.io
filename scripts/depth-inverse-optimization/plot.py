#!/usr/bin/env python3
"""Render actual saved optimizer paths and local-model diagnostics only."""
import argparse
import json
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

COLORS={'gn':'tab:blue','lm':'tab:orange','legacy-pg':'tab:green','scipy-trf':'tab:red',
        'scipy-lm':'tab:purple','bfgs':'tab:blue','lbfgs-m3':'tab:orange',
        'scipy-bfgs':'tab:green','scipy-lbfgsb-unbounded':'tab:red'}


def save(figure,output,name):
    figure.tight_layout()
    for extension in ['png','svg','pdf']:
        figure.savefig(output/(name+'.'+extension),dpi=160)
    plt.close(figure)


def load_arrays(directory,name):
    with np.load(directory/name,allow_pickle=False) as data:
        return {k:data[k].copy() for k in data.files}


def parameter_paths(ax,rows,directory,title,truth=(2.2,.35),truth_label='synthetic truth'):
    for row in rows:
        arrays=load_arrays(directory,row['artifact'])
        path=arrays['path']
        kind='residual evals' if row['method'].startswith('scipy-') else 'iterates'
        ax.plot(path[:,0],path[:,1],'.-',ms=3,lw=1.2,color=COLORS[row['method']],
                label=row['method']+' ('+kind+')')
        ax.plot(row['parameters'][0],row['parameters'][1],'x',color=COLORS[row['method']],ms=7)
    ax.plot([1,2.8,2.8,1,1],[-.5,-.5,.5,.5,-.5],'k--',lw=1,label='inference box')
    ax.plot(truth[0],truth[1],'k*',ms=10,label=truth_label)
    ax.set(xlabel='a',ylabel='b',title=title)
    ax.legend(fontsize=6)
    ax.grid(alpha=.2)


def positive_curve(ax,x,y,label,color=None):
    x,y=np.asarray(x),np.asarray(y)
    mask=y>0
    ax.plot(x[mask],y[mask],'.-',lw=1,ms=2,label=label,color=color)
    if np.any(~mask):
        ax.text(.02,.02+.04*len(ax.texts),'Exact zeros: '+label,transform=ax.transAxes,fontsize=6)
    ax.set_yscale('log')


def plot65(case,directory,output):
    rows=case['records']
    active=[r for r in rows if r['context']=='active-box']
    noisy=[r for r in rows if r['context']=='weighted-scaled-fine-noisy']
    fig,axes=plt.subplots(2,2,figsize=(12,8))
    parameter_paths(axes[0,0],active,directory,'Active-box control; infeasible generating truth',
                    truth=(2.9,.35),truth_label='outside-box generating truth')
    parameter_paths(axes[0,1],noisy,directory,'Weighted, scaled fine-grid noisy data')
    values=np.array([r['stationarity_inf'] for r in rows])
    mask=values>0
    axes[1,0].scatter(np.arange(len(values))[mask],values[mask],c=[COLORS[rows[i]['method']] for i in np.where(mask)[0]])
    axes[1,0].axhline(1e-7,color='k',ls='--',lw=1,label='fixed external limit')
    axes[1,0].set(yscale='log',xlabel='Fixed fit index',ylabel='Physical stationarity infinity norm',
                  title='Unscaled gradient or projected gradient')
    axes[1,0].legend(fontsize=7)
    chosen=[next(r for r in rows if r['context']==name and r['method']=='gn')
            for name in ['same-grid-clean','one-center']]
    x=np.arange(2)
    for i,row in enumerate(chosen):
        axes[1,1].bar(x+(i-.5)*.3,row['data_singular_values'],width=.3,label=row['context'])
    axes[1,1].set(xticks=x,xticklabels=['first','second'],ylabel='Singular value',
                  title='Data-only Jacobian; penalty rows excluded')
    axes[1,1].legend(fontsize=7)
    save(fig,output,case['id'])
    fig,ax=plt.subplots(figsize=(6,4.6))
    parameter_paths(ax,noisy,directory,'Actual parameter paths / evaluations')
    save(fig,output,case['id']+'-preview')


def rosen_paths(ax,rows,directory,legend=True):
    paths=[load_arrays(directory,row['artifact'])['path'] for row in rows]
    points=np.vstack(paths)
    lower=np.min(points,axis=0);upper=np.max(points,axis=0)
    span=np.maximum(upper-lower,.2)
    x=np.linspace(lower[0]-.08*span[0],upper[0]+.08*span[0],201)
    y=np.linspace(lower[1]-.08*span[1],upper[1]+.08*span[1],201)
    xx,yy=np.meshgrid(x,y)
    surface=100.*(yy-xx*xx)**2+(1.-xx)**2
    ax.contour(xx,yy,surface,levels=[.01,.1,1,10,100,1000],colors='.8',linewidths=.7)
    used=set()
    styles=['-','--',':']
    for row,path in zip(rows,paths):
        method=row['method'];start=int(row['problem'].split('-')[-1])
        ax.plot(path[:,0],path[:,1],styles[start],color=COLORS[method],lw=1.1,
                label=method if method not in used else None)
        ax.plot(path[0,0],path[0,1],'o',color=COLORS[method],ms=3)
        used.add(method)
    ax.plot(1.,1.,'k*',ms=11)
    ax.set(xlabel='x',ylabel='y',title='Saved Rosenbrock iterates; three fixed starts')
    if legend:ax.legend(fontsize=7)


def plot66(case,directory,output):
    rows=case['records'];rosen=[r for r in rows if r['problem'].startswith('rosenbrock')]
    fig,axes=plt.subplots(2,2,figsize=(12,8))
    rosen_paths(axes[0,0],rosen,directory)
    for row in [r for r in rosen if r['problem']=='rosenbrock-0']:
        saved=load_arrays(directory,row['artifact'])
        positive_curve(axes[0,1],saved['path_calls'],saved['path_objective'],row['method'],COLORS[row['method']])
        positive_curve(axes[1,0],saved['path_calls'],saved['path_gradient_inf'],row['method'],COLORS[row['method']])
    axes[0,1].set(xlabel='Actual objective/gradient evaluations',ylabel='Objective',title='Start (-1.2, 1)')
    axes[1,0].set(xlabel='Actual objective/gradient evaluations',ylabel='Gradient infinity norm')
    axes[0,1].legend(fontsize=7);axes[1,0].legend(fontsize=7)
    own=[r for r in rows if r['problem']=='quadratic' and r['method'] in ('bfgs','lbfgs-m3')]
    x=np.arange(2)
    axes[1,1].bar(x-.23,[r['primary_inverse_matrix_scalars'] for r in own],width=.23,label='primary inverse matrix')
    axes[1,1].bar(x,[r['maximum_retained_pair_scalars'] for r in own],width=.23,label='primary retained s/y')
    axes[1,1].bar(x+.23,[r['reference_dense_matrix_scalars'] for r in own],width=.23,label='separate dense oracle')
    axes[1,1].set(xticks=x,xticklabels=['BFGS','L-BFGS m=3'],ylabel='Stored scalars (specified components)',
                  title='8D control; excludes objective model and work vectors')
    axes[1,1].legend(fontsize=6)
    save(fig,output,case['id'])
    fig,ax=plt.subplots(figsize=(6,4.6));rosen_paths(ax,rosen,directory)
    save(fig,output,case['id']+'-preview')


def noise_parameter_panel(ax,paths,fits):
    for context in [0,1]:
        for sigma in [0,1]:
            points=[r['parameters'] for r in fits if r['context_index']==context and r['sigma_index']==sigma]
            points=np.asarray(points)
            ax.scatter(points[:,0],points[:,1],s=13,alpha=.55,marker='o' if context==0 else 's',
                       color=['tab:blue','tab:orange'][sigma],
                       label=('same-grid' if context==0 else 'fine-data')+', sigma='+['1e-4','1e-3'][sigma])
    angle=np.linspace(0,2*np.pi,160)
    for row in paths:
        if row.get('covariance') is None:continue
        covariance=np.asarray(row['covariance']);values,vectors=np.linalg.eigh(covariance)
        # Negative eigenvalues are not projected; an unplottable roundoff case is marked N/A.
        if np.any(values<0):continue
        circle=np.vstack((np.cos(angle),np.sin(angle)))
        ellipse=np.asarray(row['selected_parameters'])[:,None]+np.einsum('ij,jk->ik',vectors*np.sqrt(values)[None,:],circle)
        ax.plot(ellipse[0],ellipse[1],color='.25',lw=.7,alpha=.6)
    ax.plot(2.2,.35,'k*',ms=10,label='truth');ax.plot(2.,0.,'kx',label='prior')
    ax.set(xlabel='a',ylabel='b',title='Fits and fixed-gamma local-model 1-SD ellipses')
    ax.legend(fontsize=6)
    ax.grid(alpha=.2)


def plot67(case,directory,output):
    fits=json.loads((directory/'case67-all-fits.json').read_text())
    paths=json.loads((directory/'case67-paths.json').read_text())
    fig,axes=plt.subplots(2,2,figsize=(12,8))
    noise_parameter_panel(axes[0,0],paths,fits)
    for i,row in enumerate(paths[:8]):
        group=[f for f in fits if (f['context_index'],f['sigma_index'],f['seed_index'])==
               (row['context_index'],0 if row['sigma']==1e-4 else 1,0 if row['seed']==67001 else 1)]
        residual=[r['weighted_residual_norm'] for r in group]
        axes[0,1].plot(range(5),residual,'.-',lw=.8,label='path '+str(i))
        positive=[r for r in group if r['gamma']>0 and r['weighted_residual_norm']>0 and r['parameter_deviation_norm']>0]
        axes[1,0].plot([r['weighted_residual_norm'] for r in positive],
                      [r['parameter_deviation_norm'] for r in positive],'.-',lw=.8)
    axes[0,1].set(xticks=range(5),xticklabels=['0','1e-5','1e-4','1e-3','1e-2'],
                  xlabel='Fixed gamma list',ylabel='Weighted residual norm',title='Eight coupled paths, two independent noise vectors')
    axes[0,1].legend(fontsize=6,ncol=2)
    axes[1,0].set(xscale='log',yscale='log',xlabel='Weighted residual norm',ylabel='Parameter deviation norm',
                  title='Four-point L-curve diagnostics; no corner theorem')
    controls=paths[-2:]
    errors=np.asarray([r['parameters'] for r in controls])-np.array([2.2,.35])
    axes[1,1].bar(np.array([0,1])-.15,errors[:,0],width=.3,label='a error')
    axes[1,1].bar(np.array([0,1])+.15,errors[:,1],width=.3,label='b error')
    axes[1,1].set(xticks=[0,1],xticklabels=['same-grid data','fixed fine-grid data'],
                  ylabel='Noiseless gamma0 parameter error',title='Model discrepancy separated from sampled noise')
    axes[1,1].legend(fontsize=7)
    save(fig,output,case['id'])
    fig,ax=plt.subplots(figsize=(6,4.6));noise_parameter_panel(ax,paths,fits)
    ax.text(.02,.02,'Local fixed-gamma plug-in, not confidence coverage',transform=ax.transAxes,fontsize=7)
    save(fig,output,case['id']+'-preview')


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--results',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    source=args.results.parent if args.results.is_file() else args.results
    result=json.loads((source/'result.json').read_text())
    if result.get('passed') is not True:raise ValueError('Figures require a passed saved result')
    output=args.output;output.mkdir(parents=True,exist_ok=True)
    for case,function in zip(result['cases'],[plot65,plot66,plot67]):function(case,source,output)


if __name__=='__main__':main()
