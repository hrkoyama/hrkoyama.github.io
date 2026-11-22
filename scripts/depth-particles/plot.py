#!/usr/bin/env python3
"""Plot saved records only; no benchmark solver imports or recalculation."""
import argparse,json
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter


def plot(case,output):
    rows=case['records'];name=case['id']
    ncols=3 if name=='pic' else 2
    fig,axes=plt.subplots(1,ncols,figsize=(5*ncols,3.4),layout='constrained')
    a,b=axes[:2]
    if name=='ewald':
        for ax,series,key,label in [(a,'real_cutoff','images','Real-space image cutoff'),(b,'reciprocal_cutoff','cutoff','Reciprocal integer cutoff')]:
            data=[r for r in rows if r['series']==series]
            ax.plot([r[key] for r in data],[r['force_reference_error'] for r in data],'o-');ax.set_yscale('symlog',linthresh=1e-14);ax.set_xlabel(label);ax.set_ylabel('Max force change from converged sum')
        fig.suptitle('Neutral-cell Ewald: real and reciprocal refinement')
    elif name=='spme':
        for order in sorted({r['order'] for r in rows}):
            data=[r for r in rows if r['order']==order]
            for ax,key in [(a,'force_error'),(b,'energy_error')]:ax.loglog([r['mesh'] for r in data],[r[key] for r in data],'o-',label=f'B-spline order {order}')
        a.set_ylabel('Max force error vs direct Ewald');b.set_ylabel('Energy error vs direct Ewald')
        for ax in axes:ax.set_xlabel('Mesh points per dimension');ax.legend(fontsize=8)
        fig.suptitle('Smooth PME: B-spline mesh and order refinement')
    elif name=='fmm':
        a.semilogy([r['order'] for r in rows],[r['potential_max_error'] for r in rows],'o-');a.set_ylabel('Max potential error vs all pairs')
        b.semilogy([r['order'] for r in rows],[r['field_max_error'] for r in rows],'o-');b.set_ylabel('Max field component error vs all pairs')
        for ax in axes:ax.set_xlabel('Multipole/local expansion order')
        fig.suptitle('2D free-space log-kernel FMM: P2M / M2M / M2L / L2L / P2P')
    elif name=='pic':
        data=[r for r in rows if r['series']=='trajectory']
        a.plot([r['time'] for r in data],[r['mode'] for r in data],label='CIC PIC');a.plot([r['time'] for r in data],[r['exact_mode'] for r in data],'--',label='Linear cos(t)');a.set_xlabel('Time / plasma-frequency units');a.set_ylabel('Displacement mode / initial amplitude');a.legend(fontsize=8)
        for ax,series,key,label in [(b,'grid','grid','Grid count'),(axes[2],'time','dt','Timestep')]:
            data=[r for r in rows if r['series']==series];ax.loglog([r[key] for r in data],[r['error'] for r in data],'o-');ax.set_xlabel(label);ax.set_ylabel('Max normalized mode error');ax.set_xticks([r[key] for r in data],labels=[f"{r[key]:.3g}" for r in data])
        fig.suptitle('1D electrostatic cold-plasma PIC: separate grid and time refinements')
    elif name=='dsmc':
        data=[r for r in rows if 'particles' in r]
        for key,label in [('variance_error','Second-moment error'),('fourth_moment_error','Fourth-moment error'),('fourth_moment_standard_error','Fourth-moment SE across seeds')]:a.loglog([r['particles'] for r in data],[r[key] for r in data],'o-',label=label)
        a.set_xlabel('Particles per seed');a.set_ylabel('Moment error or sampling standard error');a.legend(fontsize=8)
        data=[r for r in rows if r.get('series')=='anisotropy'];b.plot([r['round'] for r in data],[r['anisotropy'] for r in data],label='Ensemble mean');b.plot([r['round'] for r in data],[r['expected'] for r in data],'--',label='Exact expected relaxation');b.set_xlabel('Random collision matching round');b.set_ylabel('Velocity anisotropy');b.legend(fontsize=8)
        fig.suptitle('Homogeneous Maxwell-molecule DSMC collision component')
    elif name=='radiation-transport':
        data=[r for r in rows if r['series']=='spatial'];a.loglog([r['cells'] for r in data],[r['spatial_flux_error'] for r in data],'o-',label='Flux error');a.loglog([r['cells'] for r in data],[r['ray_max_error'] for r in data],'s-',label='Max ray intensity error');a.set_xlabel('Upstream finite-volume cells');a.set_ylabel('Error vs analytic rays');a.legend(fontsize=8)
        data=[r for r in rows if r['series']=='angular'];b.semilogy([r['ordinates'] for r in data],[r['angular_flux_error'] for r in data],'o-');b.set_xlabel('Positive hemispheric ordinates');b.set_ylabel('Exit-flux error vs 2 pi E3(tau)')
        fig.suptitle('Pure absorption: separate spatial and angular refinement')
    else:raise ValueError('Unknown saved case '+name)
    for ax in axes:
        ax.grid(True,alpha=.25)
        ax.xaxis.set_minor_formatter(NullFormatter())
    fig.savefig(output/(name+'.png'),dpi=150);plt.close(fig)


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--results',required=True);p.add_argument('--output',required=True);args=p.parse_args()
    data=json.loads(Path(args.results).read_text());out=Path(args.output);out.mkdir(parents=True,exist_ok=True)
    for c in data['cases']:plot(c,out)
    print(json.dumps({'figures':[c['id']+'.png' for c in data['cases']],'source':'saved result records only'}))

if __name__=='__main__':main()
