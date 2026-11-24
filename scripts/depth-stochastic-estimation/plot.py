"""Actual normal-tail batches and two-dimensional target chains; no synthetic fields."""
import argparse,json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def main():
    p=argparse.ArgumentParser();p.add_argument('--results',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args();a.output.mkdir(parents=True,exist_ok=True)
    if a.results.is_file():a.results=a.results.parent
    result=json.loads((a.results/'result.json').read_text())
    if result['passed'] is not True:raise ValueError('Only successful saved results rendered')
    for case in result['cases']:
        ident=case['id'];d=np.load(a.results/(ident+'.npz'),allow_pickle=False);fig,axes=plt.subplots(1,2,figsize=(10,4),constrained_layout=True)
        if ident=='normal-tail-importance':
            contribution=d['contributions'][:,1,:];hist=[];edges=np.linspace(-22,-6,65)
            for row in contribution:
                positive=row[row>0];hist.append(np.histogram(np.log10(positive),bins=edges)[0])
            im=axes[0].pcolormesh(np.arange(65),edges,np.asarray(hist).T,shading='auto',cmap='magma');fig.colorbar(im,ax=axes[0],label='Event contribution count');axes[0].set(xlabel='Independent seed batch',ylabel='log10 contribution Y',title='Actual rare-tail contributions, a=6')
            for z in case['metrics']['records']:
                if z['n']!=8192:continue
                estimates=np.array(z['IS_estimates'])/z['truth'];axes[1].plot(np.arange(len(estimates)),estimates,'.',label=f"IS a={z['a']:g}")
                direct=np.array(z['direct_estimates']);axes[1].annotate(f"a={z['a']:g}: direct zero batches={z['direct_no_hit_batches']}",(.02,.92 if z['a']==3 else .84),xycoords='axes fraction',fontsize=8)
            axes[1].axhline(1,color='black',ls='--');axes[1].set(xlabel='Independent batch',ylabel='IS estimate / analytic truth',title='No zero-hit pseudo-probabilities');axes[1].legend(fontsize=8)
        else:
            chains=d['preconditioned-46001-chains'];x=chains.reshape(-1,2);im=axes[0].hist2d(x[:,0],x[:,1],bins=70,cmap='viridis');fig.colorbar(im[3],ax=axes[0],label='Retained draw count');theta=np.linspace(0,2*np.pi,400);L=np.array([[1,0],[.95,np.sqrt(1-.95**2)]])
            for radius in [1.,2.,3.]:
                curve=radius*np.c_[np.cos(theta),np.sin(theta)]@L.T+np.array([1.,-1.]);axes[0].plot(curve[:,0],curve[:,1],color='white',lw=.8)
            axes[0].set(xlabel='X1',ylabel='X2',title='Actual 2D MH chains and analytic ellipses',aspect='equal')
            values=d['preconditioned-46001'];axes[1].plot(values[0,:1000,6],lw=.6,label='normalized sum');axes[1].plot(values[0,:1000,7],lw=.6,label='normalized difference');axes[1].set(xlabel='Retained iteration',ylabel='Standardized direction',title='Different joint directions, same target variance');axes[1].legend(fontsize=8)
        fig.suptitle(ident+' — saved stochastic data',fontsize=11)
        for ext in ['png','svg','pdf']:fig.savefig(a.output/(ident+'.'+ext),dpi=150)
        for ext in ['png','svg','pdf']:fig.savefig(a.output/(ident+'-preview.'+ext),dpi=110)
        plt.close(fig)

if __name__=='__main__':main()
