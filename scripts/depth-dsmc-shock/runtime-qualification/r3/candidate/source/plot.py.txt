"""Render saved DSMC fields only. Optional matplotlib3.9.4; no simulations."""
import argparse,json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

HERE=Path(__file__).resolve().parent
TITLES={'dsmc-couette':'Hard-sphere Couette flow, Kn0=0.5',
        'dsmc-fourier':'Hard-sphere Fourier heat conduction, Kn0=0.5',
        'dsmc-planar-shock':'Hard-sphere Mach2 planar shock'}


def save(fig,path):
    for extension in ['png','svg','pdf']:fig.savefig(path.with_suffix('.'+extension),dpi=180,bbox_inches='tight')
    plt.close(fig)


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--results',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    results=a.results if a.results.is_dir() else a.results.parent
    result=json.loads((results/'result.json').read_text());inputs=json.loads((HERE/'inputs.json').read_text())
    a.output.mkdir(parents=True,exist_ok=True)
    for case in result['cases']:
        ident=case['id'];cfg=inputs['cases'][ident]['configurations']['base']
        data=np.load(results/(ident+'-ensemble.npz'),allow_pickle=False)
        mean,se=data['mean'],data['seed_se'];reference=data['reference_profiles'];rm=reference.mean(axis=0);rs=reference.std(axis=0,ddof=1)/2
        x=(np.arange(cfg['bins'])+.5)*cfg['length']/cfg['bins']
        first=2 if ident=='dsmc-couette' else 0 if cfg['kind']=='shock' else 4
        second=4 if first!=4 else 0
        names=['Number density','Normal velocity','Tangential velocity','Other velocity','Temperature','Normal molecular stress','Shear molecular stress','Heat flux']
        fig,axes=plt.subplots(2,2,figsize=(10,7),constrained_layout=True)
        for ax,column in zip(axes[0],[first,second]):
            ax.plot(x,rm[:,column],color='black',label='SPARTA independent mean')
            ax.fill_between(x,rm[:,column]-3*rs[:,column],rm[:,column]+3*rs[:,column],color='gray',alpha=.25,label='Reference 3SE')
            ax.errorbar(x,mean[:,column],yerr=3*se[:,column],fmt='o',markersize=3,capsize=2,label='New DSMC mean +/-3SE')
            ax.set(xlabel='Physical normal position x / lambda0',ylabel=names[column]);ax.grid(alpha=.2)
        axes[0,0].legend(fontsize=7)
        blocks=data['primary_block_profiles'];t=cfg['burn_in']+(np.arange(cfg['blocks'])+.5)*cfg['sample_time']/cfg['blocks']
        for seed in range(len(blocks)):axes[1,0].plot(t,blocks[seed,:,:,first].mean(axis=1),'-o',markersize=3,label='Seed '+str(seed+1))
        axes[1,0].set(xlabel='Physical time / tau0',ylabel='Block spatial mean: '+names[first]);axes[1,0].legend(fontsize=6,ncol=3);axes[1,0].grid(alpha=.2)
        labels=[];values=[]
        for row in case['records']:
            labels.append(row['configuration']+' / '+str(row['seed'])[-1]);values.append(row['scaled_budget'])
        axes[1,1].bar(np.arange(len(values)),values,color='#438b91')
        axes[1,1].set_xticks(np.arange(len(values)),labels,rotation=65,ha='right',fontsize=7)
        axes[1,1].set(ylabel='Max reservoir/wall-inclusive scaled budget error')
        fig.suptitle(TITLES[ident]+'\n1D position,3D molecular velocity; fixed inputs and independent whole-run seeds')
        save(fig,a.output/ident)
        record=case['records'][0];field=np.load(results/record['fields'],allow_pickle=False)
        hist=field['histograms'];times=field['snapshot_times'];chosen=[0,len(times)//2,len(times)-1]
        fig,axes=plt.subplots(1,3,figsize=(12,3.8),constrained_layout=True)
        for ax,index in zip(axes,chosen):
            # Counts in actual fixed saved bins; no reconstructed flow field.
            image=ax.imshow(hist[index].T,origin='lower',aspect='auto',extent=(0,cfg['length'],*cfg['hist_velocity']),cmap='magma',vmin=0,vmax=float(np.max(hist)))
            ax.set(xlabel='Physical position x / lambda0',ylabel='v_x' if cfg['kind']=='shock' else 'v_y',title='t / tau0 = '+format(times[index],'.4g'))
        fig.colorbar(image,ax=axes,label='Simulated particle count in fixed phase-space bin',shrink=.8)
        fig.suptitle(TITLES[ident]+'\nSaved particle phase space; not a two-dimensional physical flow')
        save(fig,a.output/(ident+'-preview'))

if __name__=='__main__':main()
