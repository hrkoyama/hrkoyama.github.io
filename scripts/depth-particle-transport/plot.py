#!/usr/bin/env python3
"""Draw six two-panel figures from saved JSON measurements only.

No solver or experiment module is imported. Aggregation below only selects,
scales and summarizes measurements already present in the result records.
"""
import argparse
import json
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter

COLORS=('#246c9c','#bc5138','#328274','#78569a')
FLOOR=1e-17


def positive(values,floor=FLOOR):
    """A display floor for zero/roundoff diagnostics, never a changed result."""
    return [max(float(value),floor) for value in values]


def figure(title):
    fig,axes=plt.subplots(1,2,figsize=(11.8,4.45))
    fig.suptitle(title,fontsize=13,fontweight='semibold',y=.985)
    return fig,axes


def finish(fig,output,identifier,footer):
    fig.text(.5,.025,footer,ha='center',va='bottom',fontsize=8,color='#4b5563')
    fig.tight_layout(rect=(0,.075,1,.94),w_pad=2.0)
    fig.savefig(output/(identifier+'.png'),dpi=160,facecolor='white')
    plt.close(fig)


def plot_ewald(case,output):
    records=case['records'];metrics=case['metrics']
    fig,ax=figure('Ewald: full asymmetric-cell forces versus independent theta integration')
    for series,xkey,label,color in [('real_cutoff','images','Real-space image cutoff',COLORS[0]),('reciprocal_cutoff','cutoff','Reciprocal cube cutoff',COLORS[1])]:
        rows=[r for r in records if r['series']==series]
        ax[0].semilogy([r[xkey] for r in rows],positive([r['force_error'] for r in rows]),'o-',color=color,label=label)
    ax[0].set(xlabel='Integer cutoff (other controls fixed)',ylabel='Maximum absolute force-component error',title='Separate real and reciprocal truncation')
    ax[0].legend(fontsize=8)
    keys=['net_force','gradient_error','translation_force','permutation_force','reference_force_refinement','reference_tail_force']
    labels=['Net force','Energy\ngradient','Translation','Permutation','Theta\nrefinement','Upper limit\n32 to 40']
    ax[1].bar(labels,positive([metrics[k] for k in keys]),color=[COLORS[0],COLORS[1],COLORS[2],COLORS[2],COLORS[3],COLORS[3]])
    ax[1].set(yscale='log',ylabel='Absolute force-component diagnostic',title='Conservation, identities and reference sensitivity')
    ax[1].tick_params(axis='x',labelsize=8)
    finish(fig,output,case['id'],'Neutral cubic 3D periodic cell; tin-foil boundary. Upper-limit sensitivity is measured, not a rigorous universal tail bound.')


def plot_spme(case,output):
    records=[r for r in case['records'] if r['series']=='mesh_phase'];metrics=case['metrics']
    fig,ax=figure('SPME: mesh/order convergence and translation-phase sensitivity')
    for index,order in enumerate(sorted({r['order'] for r in records})):
        meshes=sorted({r['mesh'] for r in records if r['order']==order})
        groups=[[r for r in records if r['order']==order and r['mesh']==mesh] for mesh in meshes]
        color=COLORS[index]
        ax[0].loglog(meshes,positive([max(r['force_error'] for r in group) for group in groups]),'o-',color=color,label=f'Order {order}: worst of 3 phases')
        ax[1].loglog(meshes,positive([max(r['net_force'] for r in group) for group in groups]),'o-',color=color,label=f'Order {order}: net force')
        # A bound based on each phase's error to the common reference is not
        # substituted for a measured phase difference. The actual fine spread
        # is recorded by the experiment and annotated separately below.
    ax[0].set(xlabel='Mesh points per side',ylabel='Maximum absolute force-component error',title='Against independent theta forces')
    ax[0].set_xticks([16,24,40],labels=['16','24','40']);ax[0].xaxis.set_minor_formatter(NullFormatter());ax[0].legend(fontsize=8)
    ax[1].set(xlabel='Mesh points per side',ylabel='Maximum component of total force',title='Energy-gradient mesh forces: nonzero net force')
    ax[1].set_xticks([16,24,40],labels=['16','24','40']);ax[1].xaxis.set_minor_formatter(NullFormatter());ax[1].legend(fontsize=8,loc='upper right')
    ax[1].text(.04,.06,f"Fine phase force spread: {metrics['phase_force_spread']:.2e}\nFine energy-gradient check: {metrics['gradient_error']:.2e}",transform=ax[1].transAxes,fontsize=8,bbox=dict(facecolor='white',edgecolor='#d1d5db',alpha=.9))
    finish(fig,output,case['id'],'B-spline SPME, orders 4/6; shared Ewald real/self terms checked separately. Energy consistency does not imply exact momentum conservation.')


def plot_fmm(case,output):
    records=[r for r in case['records'] if r['series']=='order_depth'];metrics=case['metrics']
    fig,ax=figure('FMM: independent direct/analytic references for the 2D logarithmic kernel')
    for index,depth in enumerate(sorted({r['depth'] for r in records})):
        rows=sorted([r for r in records if r['depth']==depth],key=lambda r:r['order'])
        color=COLORS[index]
        ax[0].semilogy([r['order'] for r in rows],positive([r['field_error'] for r in rows]),'o-',color=color,label=f'Field, depth {depth}')
        ax[0].semilogy([r['order'] for r in rows],positive([r['potential_error'] for r in rows]),'s--',color=color,label=f'Potential, depth {depth}')
    ax[0].set(xlabel='Expansion order',ylabel='Maximum absolute error versus Cartesian direct',title='Order refinement at each fixed tree depth')
    ax[0].legend(fontsize=8)
    keys=['translation_field_error','rotation_field_error','net_force_absolute','symmetric_field_error','multipole_field_error']
    labels=['Translation\nfield','Rotation\nfield','Net force','Polygon\nfield','Far-ring\nfield']
    ax[1].bar(labels,positive([metrics[k] for k in keys]),color=[COLORS[0],COLORS[0],COLORS[1],COLORS[2],COLORS[3]])
    ax[1].set(yscale='log',ylabel='Absolute diagnostic (dimensionless units)',title='Invariance, force balance and closed-form probes')
    ax[1].tick_params(axis='x',labelsize=8)
    finish(fig,output,case['id'],'Free-space -log(r), not 3D Coulomb. Depth need not improve error monotonically; target-wise expansions need not obey exact action/reaction.')


def plot_pic(case,output):
    records=case['records'];metrics=case['metrics']
    fig,ax=figure('PIC: separate mesh/time errors and measured conservation')
    mesh=[r for r in records if r['series']=='mesh'];time=[r for r in records if r['series']=='time']
    ax[0].loglog([r['grid']/mesh[0]['grid'] for r in mesh],positive([r['mode_error'] for r in mesh]),'o-',color=COLORS[0],label='Mesh vs continuum; 2048 particles')
    ax[0].loglog([time[0]['dt']/r['dt'] for r in time],positive([r['mode_error'] for r in time]),'s-',color=COLORS[1],label='Time vs shared-CIC DOP853')
    ax[0].set(xlabel='Refinement factor (each own coarsest = 1)',ylabel='Absolute normalized displacement-mode error',title='Different references; fixed other discretizations')
    ax[0].set_xticks([1,2,4],labels=['1','2','4']);ax[0].xaxis.set_minor_formatter(NullFormatter());ax[0].legend(fontsize=8)
    ax[0].text(.04,.06,f"Minimum observed time order: {metrics['minimum_time_order']:.3f}",transform=ax[0].transAxes,fontsize=8)
    trajectory=[r for r in records if r['series']=='trajectory']
    for key,label,color in [('relative_energy_drift','Relative energy drift',COLORS[1]),('charge_error','Absolute total charge',COLORS[0]),('momentum_error','Absolute momentum',COLORS[2]),('nyquist_charge','Nyquist charge (separate null mode)',COLORS[3])]:
        values=[];maximum=0.
        for row in trajectory:
            maximum=max(maximum,row[key]);values.append(maximum)
        ax[1].semilogy([r['time'] for r in trajectory],positive(values,1e-30),color=color,label=label)
    ax[1].set(xlabel='Time (finest mesh run)',ylabel='Cumulative maximum diagnostic (normalized units)',title='Energy is approximate; charge/momentum are tighter')
    ax[1].legend(fontsize=7.5,loc='lower left')
    finish(fig,output,case['id'],'Cold 1D periodic plasma. DOP853 shares the CIC RHS. Noise is a separate 64-seed initial diagnostic. Right: cumulative maxima; zeros at 1e-30.')


def plot_dsmc(case,output):
    records=case['records'];metrics=case['metrics']
    fig,ax=figure('DSMC collision component: finite-N equilibrium and seed-level uncertainty')
    counts=sorted({r['particles'] for r in records if r['series']=='cdf'})
    rows=[r for r in records if r['series']=='cdf' and r['particles']==counts[0]]
    energy=[r['energy'] for r in rows]
    ax[0].plot(energy,[r['exact_finite_n'] for r in rows],'-',color=COLORS[0],label=f'Finite-N beta law, N={counts[0]}')
    ax[0].plot(energy,[r['maxwell_limit'] for r in rows],'--',color='#6b7280',label='Maxwell infinite-N limit')
    ax[0].errorbar(energy,[r['mean'] for r in rows],yerr=[r['standard_error'] for r in rows],fmt='o',capsize=3,color=COLORS[1],label='Collisions: mean +/- seed SE')
    ax[0].errorbar(energy,[r['independent_mean'] for r in rows],yerr=[r['independent_standard_error'] for r in rows],fmt='s',capsize=3,color=COLORS[2],label='Projected sphere: mean +/- seed SE')
    ax[0].set(xlabel='Single-particle kinetic energy',ylabel='Energy cumulative probability',title='Finite-particle model bias is distinct from noise')
    ax[0].legend(fontsize=7.5)
    grouped=[[r for r in records if r['series']=='cdf' and r['particles']==count] for count in counts]
    ax[1].loglog(counts,[sum(r['standard_error'] for r in group)/len(group) for group in grouped],'o-',color=COLORS[1],label='Mean CDF seed standard error')
    ax[1].loglog(counts,[max(abs(r['exact_finite_n']-r['maxwell_limit']) for r in group) for group in grouped],'s--',color=COLORS[0],label='Max finite-N CDF bias to Maxwell')
    ax[1].set(xlabel='Particles per replicate (64 independent seeds)',ylabel='Absolute CDF uncertainty or model difference',title='Sampling error and finite-N bias decrease separately')
    ax[1].set_xticks(counts,labels=[str(count) for count in counts]);ax[1].legend(fontsize=7.5)
    finish(fig,output,case['id'],f"Fixed ensemble, correlated particles within each seed; no IID-particle KS claim. Max relative energy defect: {metrics['relative_energy_error']:.1e}; rounds are not physical time.")


def plot_radiation(case,output):
    records=case['records'];metrics=case['metrics']
    fig,ax=figure('Absorbing slab: deterministic refinement and analog-photon uncertainty')
    depths=sorted({r['optical_depth'] for r in records if r['series']=='space'})
    for index,depth in enumerate(depths):
        color=COLORS[index]
        space=[r for r in records if r['series']=='space' and r['optical_depth']==depth]
        angle=[r for r in records if r['series']=='angle' and r['optical_depth']==depth]
        ax[0].loglog([r['cells'] for r in space],positive([r['spatial_flux_error'] for r in space]),'o-',color=color,label=f'tau={depth:g}, space')
        ax[0].loglog([r['ordinates'] for r in angle],positive([r['angular_flux_error'] for r in angle]),'s--',color=color,label=f'tau={depth:g}, angle')
        photons=[r for r in records if r['series']=='photon-statistics' and r['optical_depth']==depth]
        ax[1].loglog([r['histories'] for r in photons],[r['rmse'] for r in photons],'o-',color=color,label=f'tau={depth:g}, measured RMSE')
        ax[1].loglog([r['histories'] for r in photons],[r['binomial_standard_deviation'] for r in photons],'--',color=color,label=f'tau={depth:g}, binomial SD')
    ax[0].set(xlabel='Cells (solid) or angular ordinates (dashed)',ylabel='Absolute outgoing-flux error',title='Space vs fixed rays; angle vs characteristic integral')
    ax[0].legend(fontsize=7.3,ncol=2,loc='lower left')
    ax[1].set(xlabel='Photon histories per replicate',ylabel='Survival-probability error',title='64 independent seeds at each point')
    ax[1].legend(fontsize=7.3)
    finish(fig,output,case['id'],f"Flux-weighted mu=sqrt(U); exact binomial intervals. Minimum observed 95% coverage: {metrics['minimum_measured_coverage']:.4f}; fixed-seed coverage is not guaranteed.")


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--results',required=True,type=Path)
    parser.add_argument('--output',required=True,type=Path)
    args=parser.parse_args()
    data=json.loads(args.results.read_text())
    cases={case['id']:case for case in data['cases']}
    args.output.mkdir(parents=True,exist_ok=True)
    plt.rcParams.update({'font.size':9,'axes.titlesize':10,'axes.labelsize':9,'axes.grid':True,'grid.alpha':.2,'axes.spines.top':False,'axes.spines.right':False,'legend.framealpha':.94})
    for identifier,function in [('ewald-convergence',plot_ewald),('spme-convergence',plot_spme),('fmm-convergence',plot_fmm),('pic-conservation',plot_pic),('dsmc-statistics',plot_dsmc),('radiation-convergence',plot_radiation)]:
        function(cases[identifier],args.output)


if __name__=='__main__':main()
