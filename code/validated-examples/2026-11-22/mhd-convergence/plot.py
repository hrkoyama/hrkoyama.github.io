"""Render stored MHD JSON/NPZ only. Never execute a solver or reference."""
import argparse
import json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import NullLocator


def render(results,output):
    results=Path(results);payload=json.loads(results.read_text());output=Path(output);output.mkdir(parents=True,exist_ok=True)
    for case in payload['cases']:
        ident=case['id']
        with np.load(results.parent/(ident+'-fields.npz'),allow_pickle=False) as f:data={k:f[k] for k in f.files}
        if ident=='ct-glm-constraint-control':
            fig,axes=plt.subplots(2,2,figsize=(11,7.2),constrained_layout=True)
            n=data['initial_q'].shape[0];x=(np.arange(n)+.5)/n
            axes[0,0].plot(x,data['initial_q'][:,0,4],color='.65',label='Initial cell Bx')
            for key,label,color in [('ct','CT: initial defect retained','tab:orange'),('damped','GLM kappa=2','tab:blue'),('undamped','GLM kappa=0','tab:green')]:
                axes[0,0].plot(x,data[key+'_q'][:,0,4],label=label,color=color)
                if key!='ct':
                    axes[0,0].plot(x,data[key+'_reference_B_psi'][:,0,0],'--',color=color,lw=1)
                    axes[0,1].plot(x,data[key+'_q'][:,0,6],label=label,color=color)
                    axes[0,1].plot(x,data[key+'_reference_B_psi'][:,0,1],'--',color=color,lw=1)
                h=data[key+'_history'];axes[1,0].plot(h[:,0],h[:,4],label=label,color=color)
            axes[0,0].set(title='Same initial cell B; solid: MHD, dashed: Fourier FE',xlabel='x',ylabel='Bx')
            axes[0,1].set(title='Active B/psi wave exchange',xlabel='x',ylabel='psi')
            axes[1,0].set(title='Same centered divergence operator',xlabel='Time',ylabel='max |Dcell B|')
            glm=[r for r in case['records'] if r['method']=='glm'];energies=[r['B_psi_wave_energy'] for r in glm]
            axes[1,1].bar(['GLM kappa=2','GLM kappa=0'],energies,color=['tab:blue','tab:green'])
            ratio=case['metrics']['damped_to_undamped_B_psi_wave_energy_ratio']
            axes[1,1].set(title=f'Auxiliary wave norm ratio = {ratio:.6f}',ylabel='mean(Bx^2 + psi^2/ch^2)')
            for ax in axes.flat:
                ax.grid(alpha=.18)
                if ax.get_legend_handles_labels()[0]:ax.legend(fontsize=8)
            fig.suptitle('NONPHYSICAL constraint control: CT initial div B is deliberately nonzero\nCT preserves the initial defect; GLM damping separated from phase and LLF diffusion',fontsize=11)
        else:
            smooth=ident=='ct-glm-smooth-convergence';component=3 if smooth else 0
            target=data['reference'][...,component] if smooth else data['reference'][...,0]
            label='Conserved cell-average E' if smooth else 'Density'
            fig,axes=plt.subplots(2,3,figsize=(13,7.4),constrained_layout=True)
            image=axes[0,0].imshow(target.T,origin='lower',extent=[0,1,0,1],cmap='viridis');fig.colorbar(image,ax=axes[0,0]);axes[0,0].set_title(('Analytic ' if smooth else 'Independent Athena++ ')+label)
            diffs=[data[m+'_q'][...,component]-target for m in ('ct','glm')];bound=max(float(np.max(abs(a))) for a in diffs)
            for ax,method,error in zip(axes[0,1:],('ct','glm'),diffs):
                im=ax.imshow(error.T,origin='lower',extent=[0,1,0,1],cmap='coolwarm',vmin=-bound,vmax=bound);fig.colorbar(im,ax=ax);ax.set_title(method.upper()+' minus reference')
            for method,color in [('ct','tab:orange'),('glm','tab:blue')]:
                space=[r for r in case['records'] if r['method']==method];key='scaled_l2' if smooth else 'combined_relative_l1'
                axes[1,0].loglog([r['n'] for r in space],[r[key] for r in space],'o-',label=method.upper(),color=color)
                temporal=[r for r in case['temporal_records'] if r['method']==method]
                axes[1,1].loglog([r['dt'] for r in temporal],[r['scaled_l2'] for r in temporal],'o-',label=method.upper(),color=color)
                h=data[method+'_history'];axes[1,2].plot(h[:,0],h[:,4],label=method.upper()+' common cell D',color=color)
                if method=='ct':axes[1,2].plot(h[:,0],h[:,3],':',label='CT native face D',color=color)
            axes[1,0].set(title='Grid convergence (fixed dt)',xlabel='N',ylabel='Scaled L2' if smooth else 'Combined relative L1')
            axes[1,1].set(title='Time convergence vs DOP853',xlabel='dt',ylabel='Scaled L2 error')
            axes[1,2].set(title='Native and common divergence',xlabel='Time',ylabel='max |div B|')
            grids=[r['n'] for r in case['records'] if r['method']=='ct']
            dts=sorted(r['dt'] for r in case['temporal_records'] if r['method']=='ct')
            axes[1,0].set_xticks(grids,[str(n) for n in grids]);axes[1,0].xaxis.set_minor_locator(NullLocator())
            axes[1,1].set_xticks(dts,[format(dt,'.1e') for dt in dts]);axes[1,1].xaxis.set_minor_locator(NullLocator())
            for ax in axes[1,:]:ax.grid(alpha=.2);ax.legend(fontsize=8)
            fig.suptitle(('Constructed moving magnetostatic equilibrium' if smooth else 'Short-time periodic Orszag-Tang')+'\nMatched alpha/ch=3, physical kappa=2, first-order Rusanov / forward Euler; solenoidal GLM cleaning is inactive',fontsize=11)
        fig.savefig(output/(ident+'.png'),dpi=155);plt.close(fig)


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--results',required=True);p.add_argument('--output',required=True);a=p.parse_args();render(a.results,a.output)
