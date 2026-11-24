"""Render saved fields and residual histories; accepts result JSON or directory."""
import argparse
import json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def save(fig,output,stem,preview=False):
    for extension in ('png','svg','pdf'):fig.savefig(output/(stem+'.'+extension),dpi=135,bbox_inches='tight')
    if preview:fig.savefig(output/(stem+'-preview.png'),dpi=90,bbox_inches='tight')
    plt.close(fig)


def main():
    p=argparse.ArgumentParser();p.add_argument('--results',required=True,type=Path);p.add_argument('--output',required=True,type=Path);args=p.parse_args()
    root=args.results if args.results.is_dir() else args.results.parent
    result=json.loads((root/'result.json').read_text());assert result['passed'] is True
    args.output.mkdir(parents=True,exist_ok=True)
    ident='jameson-steady-linear-modes';data=np.load(root/'stable-h32.npz');comparison=np.load(root/'stable-h32-comparison.npz')
    fig,axes=plt.subplots(1,2,figsize=(12,4.6),layout='constrained')
    im=axes[0].pcolormesh(data['x'],data['tau'],data['states']-data['steady_state'],shading='nearest',cmap='coolwarm',rasterized=True)
    fig.colorbar(im,ax=axes[0],label='Error relative to the prescribed steady grid state')
    axes[0].set(xlabel='Periodic x',ylabel='Iteration parameter (not physical time)',title='Actual 16-node error field')
    axes[1].plot(data['x'],data['states'][0]-data['steady_state'],'o-',label='Initial error')
    axes[1].plot(data['x'],data['states'][1]-data['steady_state'],'s-',label='After one iteration')
    axes[1].plot(data['x'],comparison['reference'][1]-data['steady_state'],'k--',label='Discrete amplification reference')
    axes[1].set(xlabel='Periodic x',ylabel='Error',title='Phase and damping on the actual grid');axes[1].legend(fontsize=8)
    fig.suptitle('Real-space mode damping with steady multistage RK');save(fig,args.output,ident,True)
    fig,axes=plt.subplots(1,2,figsize=(12,4.6),layout='constrained')
    for name in ('stable-h32','stable-h16','neutral-constant','expanding-nyquist'):
        d=np.load(root/(name+'.npz'));c=np.load(root/(name+'-comparison.npz'))
        axes[0].plot(np.arange(len(d['states'])),np.max(np.abs(c['true_residual']),axis=1),label=name)
        axes[1].plot(np.arange(len(d['states'])),np.max(np.abs(c['error']),axis=1),label=name)
    axes[0].set(xlabel='Completed iterations',ylabel='Unsmoothed residual maximum norm',yscale='symlog',title='Neutral and expanding controls are explicit')
    axes[1].set(xlabel='Completed iterations',ylabel='Error to discrete reference',yscale='symlog',title='Zero errors remain zero (symmetric log axis)')
    for ax in axes:ax.legend(fontsize=8);ax.grid(alpha=.25)
    save(fig,args.output,ident+'-diagnostics')


if __name__=='__main__':main()
