import argparse,json
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
def save(fig,out,id):
    for ext in ['png','svg','pdf']:fig.savefig(out/(id+'.'+ext),dpi=150)
    fig.savefig(out/(id+'-preview.png'),dpi=80);plt.close(fig)
def main():
    p=argparse.ArgumentParser();p.add_argument('--results',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args();a.output.mkdir(parents=True,exist_ok=True);base=a.results.parent;cases=json.loads(a.results.read_text())['cases']
    for c in cases:
        id=c['id'];rows=c['records'];fig,ax=plt.subplots(2,2,figsize=(11.5,7.4),layout='constrained')
        if id=='gravity-kepler':
            d=np.load(base/(id+'-s512.npz'))
            for j in range(2):ax[0,0].plot(d['positions'][:,j,0],d['positions'][:,j,1],label=f'body{j+1} KDK');ax[0,0].plot(d['reference_positions'][:,j,0],d['reference_positions'][:,j,1],'k--',lw=.7)
            ax[0,0].set(aspect='equal',xlabel='x',ylabel='y',title='One unequal-mass binary orbit and exact ellipse');ax[0,0].legend(fontsize=8)
            error=np.linalg.norm(d['positions']-d['reference_positions'],axis=2).max(axis=1);ax[0,1].plot(d['times'],error);ax[0,1].set(xlabel='time',ylabel='maximum body-position error',title='Actual phase/position error along one orbit')
            ax[1,0].loglog([r['steps'] for r in rows],[r['state_rms_error'] for r in rows],'o-');ax[1,0].set(xlabel='steps per orbit',ylabel='fixed-scale state RMS error',title='KDK time refinement vs analytic ephemeris')
            for r in rows:
                z=np.load(base/(id+'-'+r['id']+'.npz'));E=z['diagnostics'][:,0];ax[1,1].plot(z['times'],(E-E[0])/abs(E[0]),label=str(r['steps'])+'steps')
            ax[1,1].legend(fontsize=8);ax[1,1].set(xlabel='time',ylabel='relative energy change',title='Synchronized all-step Hamiltonian')
        else:
            d=np.load(base/(id+'-direct-s80.npz'));indices=np.linspace(0,len(d['times'])-1,5,dtype=int)
            for j in indices:ax[0,0].scatter(d['positions'][j,:,0],d['positions'][j,:,2],s=13,alpha=.55,label=f't={d["times"][j]:.2f}')
            ax[0,0].set(aspect='equal',xlabel='x',ylabel='z',title='Cold32body3D cloud: saved x-z projections');ax[0,0].legend(fontsize=8)
            direct=[r for r in rows if r['theta']<0];tree=[r for r in rows if r['theta']>=0];ax[0,1].loglog([r['steps'] for r in direct],[r['state_rms_error'] for r in direct],'o-');ax[0,1].set(xlabel='KDK steps to t=.2',ylabel='fixed-scale state RMS error',title='Direct time error vs independent DOP853')
            for r in tree:
                z=np.load(base/(id+'-'+r['id']+'.npz'));ax[1,0].plot(z['times'][indices],z['held_direct_force_errors'],'o-',label='theta'+str(r['theta']))
            ax[1,0].set_yscale('symlog',linthresh=1e-13);ax[1,0].legend(fontsize=8);ax[1,0].set(xlabel='held direct-path time',ylabel='relative force error at SAME positions',title='Separate force-operator comparison')
            for r in [direct[-1],*tree]:
                z=np.load(base/(id+'-'+r['id']+'.npz'));E=z['diagnostics'][:,0];ax[1,1].plot(z['times'],(E-E[0])/abs(E[0]),label=r['id'])
            ax[1,1].legend(fontsize=8);ax[1,1].set(xlabel='time',ylabel='relative exact pair-energy change',title='Same softened Hamiltonian on each trajectory')
        fig.suptitle(id+' | isolated fixed-input dynamics');save(fig,a.output,id)
if __name__=='__main__':main()
