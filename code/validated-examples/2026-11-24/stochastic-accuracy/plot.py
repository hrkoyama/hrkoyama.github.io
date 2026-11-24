"""Render actual retained path/state arrays and uncertainty diagnostics."""
import argparse,json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm


def main():
    p=argparse.ArgumentParser();p.add_argument('--results',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args();a.output.mkdir(parents=True,exist_ok=True)
    if a.results.is_file():a.results=a.results.parent
    result=json.loads((a.results/'result.json').read_text())
    if result['passed'] is not True:raise ValueError('Only successful saved results are rendered')
    for case in result['cases']:
        ident=case['id'];d=np.load(a.results/(ident+'.npz'),allow_pickle=False);fig,axes=plt.subplots(1,2,figsize=(10,4),constrained_layout=True)
        if ident.endswith('strong'):
            error=abs(d['numerical_examples'][:,1]-d['exact_examples']);heat=error.transpose(0,2,1).reshape(-1,error.shape[1]);positive=heat[heat>0]
            im=axes[0].imshow(np.ma.masked_less_equal(heat,0),origin='lower',aspect='auto',extent=[0,1,0,len(heat)],norm=LogNorm(vmin=max(float(positive.min()),1e-9),vmax=float(positive.max())),cmap='magma');fig.colorbar(im,ax=axes[0],label='Absolute Milstein error')
            axes[0].set(xlabel='Time',ylabel='Saved example path',title=f'{len(heat)} actual coupled examples')
            for z in case['metrics']['methods']:
                rows=z['levels'];h=1/np.array([r['steps'] for r in rows]);y=np.array([r['sample_RMS'] for r in rows]);lo=np.array([r['RMS_nominal95'][0] for r in rows]);hi=np.array([r['RMS_nominal95'][1] for r in rows]);axes[1].errorbar(h,y,yerr=[y-lo,hi-y],marker='o',label=f"{z['method']}: p={z['fixed_last_three_level_order']:.3f}");axes[1].plot(h,[r['analytic_RMS'] for r in rows],ls='--',color='gray')
            axes[1].set(xscale='log',yscale='log',xlabel='Step size h',ylabel='Endpoint L2 RMS',title='Same paths; finite-sample intervals');axes[1].legend(fontsize=8)
        else:
            paths=d['exact_examples'].transpose(0,2,1).reshape(-1,d['exact_examples'].shape[1]);times=np.tile(np.linspace(0,1,paths.shape[1]),len(paths));hist,te,ye=np.histogram2d(times,paths.ravel(),bins=(paths.shape[1],64));im=axes[0].pcolormesh(te,ye,hist.T,shading='auto',cmap='viridis');fig.colorbar(im,ax=axes[0],label='Saved example count');axes[0].set(xlabel='Time',ylabel='State X',title=f'{len(paths)} actual exact-coupled paths')
            for z in case['metrics']['observables']:
                rows=z['levels'];h=1/np.array([r['steps'] for r in rows]);y=abs(np.array([r['paired_mean'] for r in rows]));se=np.array([r['paired_MCSE'] for r in rows]);axes[1].errorbar(h,y,yerr=3*se,marker='o',label=f"X^{z['observable_power']}: paired");axes[1].plot(h,[abs(r['analytic_bias']) for r in rows],ls='--')
            axes[1].set(xscale='log',yscale='log',xlabel='Step size h',ylabel='Absolute weak bias',title='Exact scheme bias and 3 MCSE');axes[1].legend(fontsize=8)
        fig.suptitle(ident+' — fixed-input stochastic study',fontsize=11)
        for ext in ['png','svg','pdf']:fig.savefig(a.output/(ident+'.'+ext),dpi=150)
        for ext in ['png','svg','pdf']:fig.savefig(a.output/(ident+'-preview.'+ext),dpi=110)
        plt.close(fig)

if __name__=='__main__':main()
