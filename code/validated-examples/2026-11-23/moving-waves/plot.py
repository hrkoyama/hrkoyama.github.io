import argparse,json
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

def finish(fig,out,ident):
    for ext in ['png','svg','pdf']:fig.savefig(out/(ident+'.'+ext),dpi=150)
    fig.savefig(out/(ident+'-preview.png'),dpi=80);plt.close(fig)

def main():
    p=argparse.ArgumentParser();p.add_argument('--results',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args();a.output.mkdir(parents=True,exist_ok=True);base=a.results.parent;cases=json.loads(a.results.read_text())['cases'];plt.rcParams.update({'font.size':10})
    for case in cases:
        ident=case['id'];rows=case['records'];seq=[r for r in rows if r['family']=='space'];fine=seq[-1];f=next(n for n in case['data_files'] if 'space-n'+str(fine['n']) in n);d=np.load(base/f);fig,ax=plt.subplots(2,2,figsize=(12,7.6),layout='constrained')
        if ident.startswith('ale'):
            x=.5*(d['x'][:-1]+d['x'][1:]);q=d['m']/np.diff(d['x']);ref=d['reference_mass']/np.diff(d['x']);ax[0,0].plot(x,q,label='moving FV');ax[0,0].plot(x,ref,'k--',label='analytic cell mean');ax[0,0].legend();ax[0,0].set(xlabel='x',ylabel='q',title='Nonuniform moving cells: final transported profile')
            for j in np.linspace(0,len(d['x'])-1,17,dtype=int):ax[0,1].plot(d['geometry'][:,j],d['times'],'o-',ms=3,lw=.9)
            ax[0,1].set(xlabel='physical cell face position',ylabel='saved time',title='Saved moving-face trajectories (1D x–t)')
            ax[1,0].loglog([r['n'] for r in seq],[r['error'] for r in seq],'o-',label='space-series L1');ax[1,0].set(xlabel='cells',ylabel='conservative integral error',title='Analytic moving-cell integral reference');ax[1,0].legend()
            tmp=[r for r in rows if r['family']=='time'];ax[1,1].loglog([r['steps'] for r in tmp],[r['temporal_error'] for r in tmp],'o-');ax[1,1].set(xlabel='Heun steps',ylabel='joint x,m RMS error',title='Fixed-space time error vs independent DOP853')
        else:
            for axes,value,title in [(ax[0,0],d['initial'][0],'Actual 2D C-grid: initial height'),(ax[0,1],d['state'][0],'Numerically time-advanced height'),(ax[1,0],d['state'][0]-d['continuous_reference_history'][-1,0],'Error vs continuous wave reference')]:
                im=axes.imshow(value,origin='lower',extent=[0,1,0,1],cmap='RdBu_r');fig.colorbar(im,ax=axes);axes.set(xlabel='x',ylabel='y',title=title)
            ax[1,1].loglog([r['n'] for r in seq],[r['continuous_error'] for r in seq],'o-',label='continuous PDE');ax[1,1].loglog([r['n'] for r in seq],[r['semidiscrete_error'] for r in seq],'s--',label='discrete symbol/expm');ax[1,1].legend();ax[1,1].set(xlabel='cells per side',ylabel='relative RMS',title='Separate spatial and time-reference errors')
        fig.suptitle(ident+' | fixed lightweight inputs; saved arrays only',fontsize=14);finish(fig,a.output,ident)
if __name__=='__main__':main()
