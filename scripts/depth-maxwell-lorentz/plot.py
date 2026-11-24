"""Plot saved actual fields only; accepts a result.json file or its directory."""
from pathlib import Path
import argparse,json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def image(ax,x,y,field,title):
    value=np.max(abs(field));m=ax.pcolormesh(x,y,field.T,cmap='RdBu_r',vmin=-value if value else -1,vmax=value if value else 1,shading='auto',rasterized=True)
    ax.set(xlabel='x',ylabel='y',title=title);plt.colorbar(m,ax=ax,label='Field amplitude',shrink=.8);return m


def save(fig,output,name):
    for extension in ['png','svg','pdf']:fig.savefig(output/(name+'.'+extension),dpi=160,bbox_inches='tight')
    plt.close(fig)


def main():
    p=argparse.ArgumentParser();p.add_argument('--results',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    directory=a.results.parent if a.results.is_file() else a.results;a.output.mkdir(parents=True,exist_ok=True)
    result=json.loads((directory/'result.json').read_text())
    if result['passed'] is not True:raise ValueError('Scientific figures require a passed saved result')
    c=result['cases'][0];ident=c['id'];rows=c['records'];fig,axes=plt.subplots(1,3,figsize=(14,4.2),layout='constrained')
    if ident=='cylinder-mie2d':
        fine=max([r for r in rows if r['id'].startswith('cylinder-ppw')],key=lambda r:r['ppw'])
        with np.load(directory/fine['fields'],allow_pickle=False) as f:d={n:f[n] for n in f.files}
        x=d['x'];field=d['E_phasor'].real;image(axes[0],x,x,field,'Actual scattered electric phasor')
        mask=d['reference_mask'];error=np.ma.array(abs(d['E_phasor']-d['reference_E']),mask=~mask)
        m=axes[1].pcolormesh(x,x,error.T,shading='auto',cmap='magma',rasterized=True);plt.colorbar(m,ax=axes[1],label='Absolute phasor error',shrink=.8);axes[1].set(xlabel='x',ylabel='y',title='Independent cylindrical-series comparison',xlim=(-1.5,1.5),ylim=(-1.5,1.5))
        grid=[r for r in rows if 'reference_width' in r];axes[2].plot([r['ppw'] for r in grid],[r['width'] for r in grid],'o-',label='Actual closed-contour power');axes[2].axhline(fine['reference_width'],color='black',ls='--',label='Independent cylindrical series');axes[2].set(xlabel='Points per vacuum wavelength',ylabel='Scattering width',title='Fixed staircase refinement');axes[2].legend(fontsize=8)
        preview_title='Actual 2D dielectric-cylinder scattering'
    elif ident=='lorentz-oblique-sp':
        selected=[r for r in rows if r['polarization']=='p'];fine=max(selected,key=lambda r:r['cells'])
        with np.load(directory/fine['fields'],allow_pickle=False) as f:d={n:f[n] for n in f.files}
        cfg=json.loads((Path(__file__).parent/'inputs.json').read_text())['slab'];ky=cfg['ky'];y=np.linspace(0,2*np.pi/ky,65);x=d['x'];field=np.real(d['material_state1'][1,:,None]*np.exp(1j*ky*y[None,:]));image(axes[0],x,y,field,'Actual p-polarized field at t='+str(d['times'][1]));axes[0].set_xlim(-4,12)
        for key,label in [('R','Reflectance'),('T','Transmittance'),('A_direct','Direct absorption')]:axes[1].plot(d['omega'],d[key],'o-',label=label)
        for key in ['reference_R','reference_T','reference_A']:axes[1].plot(d['omega'],d[key],'k.',ms=4)
        axes[1].set(xlabel='Angular frequency',ylabel='Power fraction',title='Oblique dispersive slab: dots = reference');axes[1].legend(fontsize=8)
        for pol in ['s','p']:
            line=[r for r in rows if r['polarization']==pol];axes[2].loglog([r['h'] for r in line],[r['complex_rt_error'] for r in line],'o-',label=pol+' polarization')
        axes[2].set(xlabel='x grid spacing',ylabel='Maximum complex r/t error',title='Actual matched pulse refinements');axes[2].legend(fontsize=8);preview_title='Actual oblique Lorentz slab: p electric field'
    else:
        fine=next(r for r in rows if r['id']=='grazing-n1024')
        with np.load(directory/fine['fields'],allow_pickle=False) as f:d={n:f[n] for n in f.files}
        x=d['x'];ky=float(d['ky']);y=np.linspace(0,2*np.pi/ky,65);field=np.real(d['E'][1,:,None]*np.exp(1j*ky*y[None,:]));image(axes[0],x,y,field,'Actual grazing packet at t='+str(d['times'][1]))
        error=np.abs((d['E'][1]-d['reference_E'][1])[:,None]*np.exp(1j*ky*y[None,:]));m=axes[1].pcolormesh(x,y,error.T,cmap='magma',shading='auto',rasterized=True);plt.colorbar(m,ax=axes[1],label='Boundary-isolated error',shrink=.8);axes[1].set(xlabel='x',ylabel='y',title='Independent no-PML same-grid reference')
        for row in rows:
            with np.load(directory/row['fields'],allow_pickle=False) as f:h=f['history'];initial=float(f['initial_energy'])
            axes[2].semilogy(h[:,0],h[:,2]/initial,label=row['id'])
        axes[2].set(xlabel='Time',ylabel='Positive physical energy / initial',title='Actual long-time fields and material energy');axes[2].legend(fontsize=7);preview_title='Actual grazing packet in a Lorentz medium'
    for ax in axes:ax.grid(alpha=.15)
    save(fig,a.output,ident)
    fig,ax=plt.subplots(figsize=(7.4,3.6),layout='constrained');image(ax,x,y if ident!='cylinder-mie2d' else x,field,preview_title)
    if ident=='lorentz-oblique-sp':ax.set_xlim(-4,12);ax.axvline(4.,color='black',lw=.7);ax.axvline(5.,color='black',lw=.7)
    if ident=='dispersive-grazing-pml':ax.axvspan(0,12,color='gray',alpha=.15);ax.axvspan(52,64,color='gray',alpha=.15)
    fig.savefig(a.output/(ident+'-preview.png'),dpi=140,bbox_inches='tight');plt.close(fig)
if __name__=='__main__':main()
