"""Actual saved2Dspace fields, common color limits and M1closure limitations."""
import argparse,json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def save(fig,path):
    for ext in ['png','svg','pdf']:fig.savefig(str(path)+'.'+ext,dpi=155,bbox_inches='tight')


def main():
    p=argparse.ArgumentParser();p.add_argument('--results',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args();directory=a.results.parent if a.results.is_file() else a.results;result=json.loads((directory/'result.json').read_text());a.output.mkdir(parents=True,exist_ok=True)
    for c in result['cases']:
        kind='shadow' if c['id']=='shadow-absorber2d' else 'beams';data={}
        for method in ['sn','m1']:
            row=next(r for r in c['records'] if r['id']==kind+'-'+method+'-n96')
            with np.load(directory/row['fields'],allow_pickle=False) as d:data[method]={k:d[k] for k in ['moments','reference_moments','times','pressure','history']}
        snap=4 if kind=='shadow' else 2;truth=data['sn']['reference_moments'][snap,...,0];vmax=max(float(truth.max()),float(data['sn']['moments'][snap,...,0].max()),float(data['m1']['moments'][snap,...,0].max()))
        fig,axes=plt.subplots(2,3,figsize=(12.3,7.3))
        for ax,label,field in zip(axes[0],['Analytic angular transport','Actual signed-angle FV','Actual nonlinear M1'],[truth,data['sn']['moments'][snap,...,0],data['m1']['moments'][snap,...,0]]):
            im=ax.imshow(field.T,origin='lower',extent=[0,1,0,1],vmin=0,vmax=vmax,cmap='magma');ax.set(xlabel='x',ylabel='y',title=label)
        fig.colorbar(im,ax=list(axes[0]),label='Radiation energy',shrink=.8)
        x=(np.arange(96)+.5)/96
        for method in ['sn','m1']:axes[1,0].plot(x,data[method]['moments'][snap,:,48,0],label=method.upper())
        axes[1,0].plot(x,truth[:,48],'k--',label='Analytic angular');axes[1,0].set(xlabel='x',ylabel='Energy',title='Central lineout');axes[1,0].legend(fontsize=7)
        for method in ['sn','m1']:axes[1,1].semilogy(data[method]['history'][:,0],np.maximum(data[method]['history'][:,5],1e-18),label=method.upper())
        axes[1,1].set(xlabel='Time',ylabel='Absolute energy-budget defect');axes[1,1].legend(fontsize=7)
        if kind=='beams':
            p=data['m1']['pressure'][snap];axes[1,2].plot(x,p[:,48,0],label='M1 Pxx');axes[1,2].plot(x,p[:,48,2],label='M1 Pyy');axes[1,2].plot(x,p[:,48,3],label='M1 Pzz');axes[1,2].plot(x,truth[:,48],'k--',label='Angular Pxx');axes[1,2].set(title='Head-on model information loss',xlabel='x',ylabel='Pressure tensor')
        else:
            for method in ['sn','m1']:
                rows=[r for r in c['records'] if r['method']==method and r['family']=='refinement'];axes[1,2].loglog([r['cells'] for r in rows],[r['independent_moment_l1'] for r in rows],'o-',label=method.upper())
            axes[1,2].set(xlabel='Cells',ylabel='Moment L1 error',title='Separate geometry/numerical error')
        axes[1,2].legend(fontsize=7);fig.suptitle(c['id']+f' at time={data["sn"]["times"][snap]:.3g}; actual2Dspace/3Dangle');fig.subplots_adjust(top=.88,hspace=.35,wspace=.3);save(fig,a.output/c['id']);plt.close(fig)
        fig,axes=plt.subplots(1,3,figsize=(10.5,3.2))
        for ax,label,field in zip(axes,['Analytic angular','Signed-angle FV','M1 moment PDE'],[truth,data['sn']['moments'][snap,...,0],data['m1']['moments'][snap,...,0]]):
            ax.imshow(field.T,origin='lower',extent=[0,1,0,1],vmin=0,vmax=vmax,cmap='magma');ax.set(title=label,xlabel='x',ylabel='y')
        fig.suptitle('Physical2Dfield;common color scale'+(' — M1 opposing-beam difference is model error' if kind=='beams' else ''));fig.tight_layout();save(fig,a.output/(c['id']+'-preview'));plt.close(fig)
    control=next(c for c in result['cases'] if c['id']=='opposing-beams2d')
    row=next(r for r in control['records'] if r['id']=='mms-m1-n64')
    with np.load(directory/row['fields'],allow_pickle=False) as d:
        actual=d['moments'][-1];truth=d['reference_moments'][-1];x=d['x'];time=float(d['times'][-1])
    fig,axes=plt.subplots(1,3,figsize=(12,3.5))
    lo=min(float(actual[...,0].min()),float(truth[...,0].min()));hi=max(float(actual[...,0].max()),float(truth[...,0].max()))
    for ax,title,field in zip(axes[:2],['Independent manufactured energy','Actual evolved nonlinear M1 energy'],[truth[...,0],actual[...,0]]):
        ax.imshow(field.T,origin='lower',extent=[0,1,0,1],vmin=lo,vmax=hi,cmap='viridis');ax.set(title=title,xlabel='x',ylabel='y')
    im=axes[2].imshow((actual[...,0]-truth[...,0]).T,origin='lower',extent=[0,1,0,1],cmap='coolwarm');axes[2].set(title='Actual signed energy error',xlabel='x',ylabel='y');fig.colorbar(im,ax=axes[2],shrink=.75)
    fig.suptitle(f'Same M1 solver: varying flux direction/magnitude, t={time:g}; Pzz retained');fig.tight_layout();save(fig,a.output/'m1-manufactured-control');plt.close(fig)
if __name__=='__main__':main()
