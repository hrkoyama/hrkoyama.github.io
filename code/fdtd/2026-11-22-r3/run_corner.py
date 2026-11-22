"""Run the fixed four-side/corner PML experiment (0 pass,1 fail,2 input error)."""
import argparse
import csv
import hashlib
import json
import math
import platform
from pathlib import Path
import sys
import numpy as np
import corner as c


def validate(p):
    if p['case']!='pml-corners':raise ValueError('unknown case')
    required=['length','width','axis_carrier','diagonal_carrier','reference_period','spectral_cutoff','probe_offset','pml_thickness','pml_strength','courant','end_time','accuracy_time','gate_start']
    if not all(math.isfinite(p[k]) and p[k]>0 for k in required):raise ValueError('positive finite parameters required')
    if p['families']!=['axis','diagonal']:raise ValueError('both directional families required')
    if p['center']!=p['length']/2:raise ValueError('fixed symmetric central packet required')
    if p['reference_period']<3*p['length']:raise ValueError('reference period must exceed propagation box')
    if isinstance(p['pml_order'],bool) or not isinstance(p['pml_order'],int) or p['pml_order']<1:raise ValueError('positive integer PML profile order required')
    if not 0<p['courant']<1 or not 0<p['accuracy_time']<p['gate_start']<p['end_time']:raise ValueError('invalid clock/CFL')
    if not 0<p['probe_offset']<p['length']/2-p['pml_thickness']:raise ValueError('probes must be inside physical box')
    if len(p['meshes'])!=3 or not all(isinstance(n,int) and not isinstance(n,bool) and 32<=n<=1024 for n in p['meshes']):raise ValueError('three integer grids required')
    if p['meshes'][1:]!=[2*p['meshes'][0],4*p['meshes'][0]]:raise ValueError('double both dimensions')
    for n in p['meshes']:
        dx=p['length']/n
        if any(abs(v/dx-round(v/dx))>1e-10 for v in [p['pml_thickness'],p['center']-p['probe_offset'],p['center']+p['probe_offset']]):raise ValueError('faces/probes must align')
    dk=2*np.pi/p['reference_period']
    if round(p['spectral_cutoff']/dk)*dk>=np.pi*p['meshes'][0]/p['length']:raise ValueError('actual rounded spectrum below every Nyquist required')
    if not all(math.isfinite(v) and v>0 for v in p['acceptance'].values()):raise ValueError('positive finite thresholds required')


def evaluate(path):
    path=Path(path);p=json.loads(path.read_text());validate(p)
    base_steps=int(np.ceil(p['end_time']/(p['courant']*p['length']/p['meshes'][0]/np.sqrt(2))))
    rows=[];histories=[];waves=[];series=[];snapshot=None
    for family in p['families']:
        values=[];traces=[]
        for factor,n in zip([1,2,4],p['meshes']):
            row,trace,snapshot,wave,g=c.run_mesh(p,family,n,base_steps*factor)
            rows.append(row);values.append(row);histories+=trace;traces.append(wave)
            waves.extend([family,n,*w] for w in wave)
        def orders(key):return [float(np.log(a[key]/b[key])/np.log(2)) for a,b in zip(values,values[1:])]
        differences=[]
        for coarse,fine in zip(traces,traces[1:]):
            assert np.allclose(coarse[:,0],fine[::2,0],rtol=0,atol=1e-12)
            gate=coarse[:,0]>=p['gate_start']
            differences.append(float(np.max(np.sqrt(np.mean((coarse[gate,1:]-fine[::2][gate,1:])**2,axis=1)))))
        # A genuinely enlarged finite Fourier period controls periodic-image
        # and quadrature effects, rather than comparing identical padded modes.
        times=np.arange(base_steps+1)*p['end_time']/base_steps
        small=c.modal_trace(g,p,family,times,True)
        large=c.modal_trace(g,p,family,times,True,2*p['reference_period'])
        reference_error=float(np.max(np.sqrt(np.mean((small-large)**2,axis=1)))/values[-1]['incident_probe_reference_peak'])
        _,_,_,perturbed,_=c.run_mesh(p,family,p['meshes'][-1],4*base_steps,zero_initial_layer=True)
        gate=perturbed[:,0]>=p['gate_start']
        tail_sensitivity=float(np.max(np.sqrt(np.mean((perturbed[gate,1:]-traces[-1][gate,1:])**2,axis=1))))
        series.append(dict(family=family,field_orders=orders('early_field_relative_l2'),flux_orders=orders('physical_flux_budget_relative_residual'),
            return_waveform_differences=differences,return_order=float(np.log(differences[0]/differences[1])/np.log(2)),
            reference_period_doubling_error_ratio=reference_error,initial_layer_zeroing_sensitivity_ratio=tail_sensitivity,
            initial_layer_sensitivity_to_return_fraction=tail_sensitivity/values[-1]['reflection_amplitude_ratio']))
    a=p['acceptance'];fine=[r for r in rows if r['nx']==p['meshes'][-1]]
    checks=dict(continuum_accuracy=all(r['early_field_relative_l2']<=a['max_field_error'] for r in fine),
        continuum_refinement=all(min(s['field_orders'])>=a['min_field_order'] for s in series),
        reflection_amplitude=all(r['reflection_amplitude_ratio']<=a['max_reflection_amplitude'] for r in fine),
        reflected_waveform_refinement=all(s['return_order']>=a['min_return_order'] for s in series),
        independent_work_balance=all(r['modified_energy_budget_relative_residual']<=a['max_work_residual'] for r in rows),
        physical_flux_balance=all(r['physical_flux_budget_relative_residual']<=a['max_flux_residual'] for r in fine),
        physical_flux_refinement=all(min(s['flux_orders'])>=a['min_flux_order'] for s in series),
        late_energy=all(r['remaining_physical_energy_fraction']<=a['max_final_energy_fraction'] for r in fine),
        reference_period_control=all(s['reference_period_doubling_error_ratio']<=a['max_reference_period_error'] for s in series),
        reference_below_return_signal=all(s['reference_period_doubling_error_ratio']<=a['max_reference_to_return_fraction']*next(r for r in fine if r['family']==s['family'])['reflection_amplitude_ratio'] for s in series),
        initial_layer_tail=all(r['initial_layer_energy_fraction']<=a['max_initial_layer_energy_fraction'] for r in rows),
        initial_layer_sensitivity_below_return=all(s['initial_layer_sensitivity_to_return_fraction']<=a['max_initial_layer_sensitivity_to_return_fraction'] for s in series),
        gate_contains_global_peak=all(r['global_return_peak_time']>=p['gate_start'] for r in fine),
        all_four_sides=all(min(r['side_flux_fractions'].values())>=a['min_side_flux_fraction'] for r in fine),
        all_four_corners=min(next(r for r in fine if r['family']=='diagonal')['corner_abs_work_fractions'].values())>=a['min_corner_abs_work_fraction'])
    result=dict(schema_version=1,case=p['case'],input_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
        environment=dict(python=platform.python_version(),numpy=np.__version__),termination='fixed_budget_completed',
        normalization='Probe RMS of returned E / peak continuum incident probe RMS; exact discrete baseline shares the finite standing Fourier packet.',
        reflection_scope='Boundary-induced probe error including finite layer and initial PML/auxiliary tails; not pure ideal-PML reflection.',
        metrics=dict(meshes=rows,series=series),checks={k:bool(v) for k,v in checks.items()},passed=bool(all(checks.values())))
    return result,histories,snapshot,waves


def save(out,result,history,snapshot,waves):
    out.mkdir(parents=True,exist_ok=True)
    (out/'result.json').write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    with (out/'convergence.csv').open('w',newline='') as f:
        fields=list(result['metrics']['meshes'][0]);w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
        for row in result['metrics']['meshes']:w.writerow({k:json.dumps(v,sort_keys=True) if isinstance(v,dict) else v for k,v in row.items()})
    with (out/'energy.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['nx','family','time','modified_energy','physical_energy','electric_PML_work','magnetic_PML_work','interior_energy','flux_left','flux_right','flux_bottom','flux_top']);w.writerows(history)
    with (out/'waveforms.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['family','nx','time','return_SW_or_left','return_SE_or_right','return_NW_or_bottom','return_NE_or_top']);w.writerows(waves)
    e,ref,g=snapshot
    with (out/'solution.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['x','y','Ez','continuum_Ez','error'])
        for i,x in enumerate(g['x']):
            w.writerows([x,y,e[i,j],ref[i,j],e[i,j]-ref[i,j]] for j,y in enumerate(g['x']))
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    fig,axs=plt.subplots(1,3,figsize=(13,3.8),constrained_layout=True)
    for family in ['axis','diagonal']:
        rows=[r for r in result['metrics']['meshes'] if r['family']==family]
        axs[0].loglog([r['dx'] for r in rows],[r['early_field_relative_l2'] for r in rows],'o-',label=family)
        axs[1].loglog([r['dx'] for r in rows],[r['reflection_amplitude_ratio'] for r in rows],'o-',label=family)
    axs[0].set(xlabel='Grid spacing (normalized)',ylabel='Relative L2 field error',title='Continuum packet refinement');axs[0].legend()
    axs[1].set(xlabel='Grid spacing (normalized)',ylabel='Boundary-induced error / incident RMS',title='PML boundary + initialization');axs[1].legend()
    z=np.array([r[2:7] for r in history if r[0]==g['n'] and r[1]=='diagonal']);initial=z[0,1]
    axs[2].plot(z[:,0],z[:,1]/initial,label='Modified energy')
    axs[2].plot(z[:,0],(z[:,3]+z[:,4])/initial,label='Signed PML work')
    axs[2].plot(z[:,0],(z[:,1]+z[:,3]+z[:,4])/initial,label='Sum')
    axs[2].set(xlabel='Time (normalized)',ylabel='Fraction of initial energy',title='Independent two-axis work balance');axs[2].legend(fontsize=8)
    fig.savefig(out/'summary.png',dpi=150);plt.close(fig)


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--input',type=Path,required=True);parser.add_argument('--output',type=Path,required=True);a=parser.parse_args()
    try:
        if a.output.exists() and (not a.output.is_dir() or any(a.output.iterdir())):raise ValueError('new or empty output required')
        r,h,s,w=evaluate(a.input);save(a.output,r,h,s,w);print(json.dumps(dict(case=r['case'],passed=r['passed'],checks=r['checks'])));return 0 if r['passed'] else 1
    except Exception as error:print(str(error),file=sys.stderr);return 2

if __name__=='__main__':sys.exit(main())
