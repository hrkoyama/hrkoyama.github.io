import argparse,json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def main():
    p=argparse.ArgumentParser();p.add_argument('--results',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args();result=json.loads(a.results.read_text());a.output.mkdir(exist_ok=True,parents=True)
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'axes.spines.top':False,'axes.spines.right':False})
    for case in result['cases']:
        ident=case['id'];d=np.load(a.results.parent/f'{ident}-n64.npz');fig,ax=plt.subplots(2,2,figsize=(11,8),layout='constrained');fig.set_facecolor('#f7f9fc')
        if ident=='checkerboard-diffusion':
            image=d['direct'].reshape(64,64);err=(d['direct']-d['reference']).reshape(64,64);title='Checkerboard diffusion | scalar FV';subtitle='Shared harmonic face flux | contrast 100:1'
        else:
            image=d['field'].reshape(65,65);xy=d['points'];exact=np.sin(np.pi*xy[:,0])*np.sin(np.pi*xy[:,1]);err=(d['field']-exact).reshape(65,65);title='Rotated anisotropic diffusion | full-tensor Q1';subtitle='Eigenvalues 1, 0.01 | rotation 30 degrees | cross term retained'
        fig.suptitle(title+'\n'+subtitle,fontsize=16,color='#15324e')
        for panel,field,label,cmap in [(ax[0,0],image,'Computed solution','viridis'),(ax[0,1],err,'FV - independent P1 reference' if ident=='checkerboard-diffusion' else 'Q1 - continuous analytic solution','RdBu_r')]:
            im=panel.imshow(field,origin='lower',extent=[0,1,0,1],cmap=cmap,aspect='equal');fig.colorbar(im,ax=panel,shrink=.8);panel.set(xlabel='x',ylabel='y',title=label)
        for kind,color in [('geometric','#087e8b'),('amg','#c45a3b')]:
            for n in [16,32,64]:
                z=np.load(a.results.parent/f'{ident}-n{n}.npz');h=z[kind+'_history'];ax[1,0].semilogy(np.arange(len(h)),h,label=f'{kind} N={n}',alpha=.45+.55*n/64,color=color,linestyle={16:':',32:'--',64:'-'}[n])
        ax[1,0].axhline(1e-8,color='gray',lw=.8);ax[1,0].set(xlabel='PCG iteration',ylabel='True relative residual',title='Same A, b | two SPD V-cycles');ax[1,0].legend(fontsize=8,ncol=2)
        errors=case['metrics']['continuous_errors'];ax[1,1].loglog([16,32,64],errors,'o-',color='#15324e',label='primary/reference discrepancy')
        if case['metrics']['reference_sensitivity']:ax[1,1].loglog([16,32,64],case['metrics']['reference_sensitivity'],'s--',color='#ad7b26',label='P1 128/192 sensitivity')
        ax[1,1].set(xlabel='Intervals per axis',ylabel='Relative field error',title='Continuum accuracy differs from residual');ax[1,1].legend(fontsize=8);ax[1,1].grid(alpha=.2)
        for ext in ['png','svg','pdf']:fig.savefig(a.output/f'{ident}.{ext}',dpi=150)
        fig.savefig(a.output/f'{ident}-preview.png',dpi=90);plt.close(fig)
if __name__=='__main__':main()
