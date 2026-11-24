"""Render saved coupled signed-angle fields and independent flux comparisons."""
import argparse,json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def save(fig,path):
    for suffix in ['png','svg','pdf']:fig.savefig(str(path)+'.'+suffix,dpi=155,bbox_inches='tight')


def main():
    p=argparse.ArgumentParser();p.add_argument('--results',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args();directory=a.results.parent if a.results.is_file() else a.results;result=json.loads((directory/'result.json').read_text());a.output.mkdir(parents=True,exist_ok=True)
    rows=result['cases'][0]['records'];selected=next(r for r in rows if r['id']=='slab3-n256-s64')
    with np.load(directory/selected['fields'],allow_pickle=False) as d:x,mu,intensity,scalar=d['x'],d['mu'],d['intensity'],d['scalar']
    fig,axes=plt.subplots(2,2,figsize=(11,7.5));im=axes[0,0].pcolormesh(x,mu,intensity,shading='nearest',cmap='magma');fig.colorbar(im,ax=axes[0,0],label='Computed intensity')
    axes[0,0].set(xlabel='Optical depth',ylabel='Signed direction cosine',title='Coupled angular-position field (not2Dspace)')
    colors=plt.cm.viridis(np.linspace(.1,.9,4))
    for i,color in enumerate(colors):
        row=next(r for r in rows if r['id']==f'slab{i}-n256-s32')
        with np.load(directory/row['fields'],allow_pickle=False) as d:axes[0,1].plot(d['x'],d['scalar'],color=color,label=f'L={row["depth"]}, omega={row["albedo"]}')
        sequence=[r for r in rows if r.get('parameter_index')==i and r['ordinates']==32]
        axes[1,1].loglog([r['cells'] for r in sequence],[r['maximum_flux_error'] for r in sequence],'o-',color=color)
    axes[0,1].set(xlabel='Optical depth',ylabel='Scalar radiance J',title='Actual coupled source fields');axes[0,1].legend(fontsize=7)
    positions=np.arange(4);bottom=np.zeros(4)
    for j,label in enumerate(['R','T','A']):
        values=np.array([next(r for r in rows if r['id']==f'slab{i}-n256-s32')['fluxes'][j] for i in range(4)])
        axes[1,0].bar(positions,values,bottom=bottom,label=label,alpha=.7);bottom+=values
        reference=np.array([next(r for r in rows if r['id']==f'slab{i}-n256-s32')['reference'][j] for i in range(4)])
        axes[1,0].plot(positions,reference,'kx',markersize=4)
    axes[1,0].set(xlabel='Frozen slab index',ylabel='Fraction of incident flux',title='R/T/A budget; crosses: independent individual fractions');axes[1,0].legend(ncol=3)
    axes[1,1].set(xlabel='Cells',ylabel='Maximum R/T/A error',title='Separate spatial refinement at32signed angles');fig.tight_layout();save(fig,a.output/'isotropic-scattering-slab');plt.close(fig)
    fig,ax=plt.subplots(figsize=(7.2,3.8));im=ax.pcolormesh(x,mu,intensity,shading='nearest',cmap='magma');fig.colorbar(im,ax=ax,label='Intensity');ax.set(xlabel='Optical depth',ylabel='Signed direction cosine',title='Isotropic scattering: reflected negative-angle field');fig.tight_layout();save(fig,a.output/'isotropic-scattering-slab-preview');plt.close(fig)
if __name__=='__main__':main()
