import argparse,json
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
def main():
    p=argparse.ArgumentParser();p.add_argument('--results',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args();a.output.mkdir(parents=True,exist_ok=True);case=json.loads(a.results.read_text())['cases'][0];rows=[r for r in case['records'] if r['alpha']==4.];d=np.load(a.results.parent/'neutral-slab-yb-z6-a4.npz');fig,ax=plt.subplots(2,2,figsize=(11.5,7.4),layout='constrained');x=d['positions'];q=d['charges'];force=d['force'];im=ax[0,0].scatter(x[:,0],x[:,2],c=q,cmap='coolwarm',s=100,edgecolors='k');ax[0,0].quiver(x[:,0],x[:,2],force[:,0],force[:,2],alpha=.7);fig.colorbar(im,ax=ax[0,0],label='charge');ax[0,0].set(xlabel='x',ylabel='physical z',title='Four3D charges: x-z projection and corrected force')
    for axes,key,title in [(ax[0,1],'energy','Energy vs genuine2P reference'),(ax[1,0],'force','All-component max force error')]:
        for kind in ['corrected','uncorrected']:axes.semilogy([r['Lz'] for r in rows],[max(r[kind+'_'+key+'_error'],1e-16) for r in rows],'o-',label=kind)
        axes.legend();axes.set(xlabel='extended3P box Lz',ylabel='absolute error',title=title)
    ax[1,1].plot((d['force']-d['reference_force']).ravel(),'o-',label='YB-corrected minus2P');ax[1,1].plot((d['uncorrected_force']-d['reference_force']).ravel(),'s--',label='3P minus2P');ax[1,1].set_yscale('symlog',linthresh=1e-11);ax[1,1].legend(fontsize=9);ax[1,1].set(xlabel='particle/component index',ylabel='signed force error',title='Finest vacuum: every force component retained');fig.suptitle('Neutral rectangular slab | Coulomb1/r, periodic x/y, free z')
    for ext in ['png','svg','pdf']:fig.savefig(a.output/('neutral-slab-yb.'+ext),dpi=150)
    fig.savefig(a.output/'neutral-slab-yb-preview.png',dpi=80);plt.close(fig)
if __name__=='__main__':main()
