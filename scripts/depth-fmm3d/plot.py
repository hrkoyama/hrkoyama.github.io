import argparse,json
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
def main():
    p=argparse.ArgumentParser();p.add_argument('--results',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args();a.output.mkdir(parents=True,exist_ok=True);case=json.loads(a.results.read_text())['cases'][0];rows=[r for r in case['records'] if r['id'].startswith('p')];d=np.load(a.results.parent/'fmm3d-inverse-r-p7-d3.npz');x=d['positions'];error=np.linalg.norm(d['acceleration']-d['reference_acceleration'],axis=1);fig,ax=plt.subplots(2,2,figsize=(11.5,7.4),layout='constrained');im=ax[0,0].scatter(x[:,0],x[:,1],c=error,cmap='magma',s=40);ax[0,0].quiver(x[:,0],x[:,1],d['acceleration'][:,0],d['acceleration'][:,1],alpha=.55);fig.colorbar(im,ax=ax[0,0],label='3D acceleration error norm');ax[0,0].set(aspect='equal',xlabel='x',ylabel='y',title='Actual3D sources/acceleration: x-y projection')
    for depth in [2,3]:
        s=[r for r in rows if r['depth']==depth]
        ax[0,1].semilogy([r['p'] for r in s],[r['potential_error'] for r in s],'o-',label=f'potential level{depth}');ax[0,1].semilogy([r['p'] for r in s],[r['acceleration_error'] for r in s],'s--',label=f'force level{depth}')
    ax[0,1].legend(fontsize=9);ax[0,1].set(xlabel='Chebyshev nodes per axis',ylabel='relative RMS vs direct',title='Separate order and actual leaf-level comparison')
    adaptive=np.load(a.results.parent/'fmm3d-inverse-r-adaptive.npz');boxes=adaptive['boxes'];leaf=boxes[boxes[:,6]==0];im=ax[1,0].scatter(adaptive['positions'][:,0],adaptive['positions'][:,2],c=adaptive['ownership'].sum(axis=1),s=25);ax[1,0].set(xlabel='x',ylabel='z',title='Adaptive3D cloud: x-z projection; all63owners per target')
    for b in leaf:
        from matplotlib.patches import Rectangle
        ax[1,0].add_patch(Rectangle((b[0]-b[3],b[2]-b[3]),2*b[3],2*b[3],fill=False,lw=.5,alpha=.4))
    ax[1,1].imshow(d['ownership'],origin='lower',cmap='viridis',vmin=0,vmax=1);ax[1,1].set(xlabel='source index',ylabel='target index',title='Unique interaction ownership (self diagonal excluded)');fig.suptitle('Uncompressed3D gravitational FMM | actual multilevel fields')
    for ext in ['png','svg','pdf']:fig.savefig(a.output/('fmm3d-inverse-r.'+ext),dpi=150)
    fig.savefig(a.output/'fmm3d-inverse-r-preview.png',dpi=80);plt.close(fig)
if __name__=='__main__':main()
