"""Fixed-input dielectric and split-field PML checks: exit0 pass,1 fail,2 error."""
import argparse
import csv
import hashlib
import json
import math
from pathlib import Path
import platform
import sys
import numpy as np
from scattering import run_interface,run_pml


def validate(p):
    if p['case'] not in ['dielectric-interface','pml-pulse']:raise ValueError('unknown scattering case')
    for key in ['lengths']:
        if len(p[key])!=2 or not all(math.isfinite(x) and x>0 for x in p[key]):raise ValueError('positive finite lengths required')
    if not all(math.isfinite(p[k]) and p[k]>0 for k in ['width','end_time','courant']):raise ValueError('positive finite inputs required')
    if not 0<p['courant']<1:raise ValueError('strict Courant range required')
    if not 3<=len(p['meshes'])<=6:raise ValueError('3 to6 refinement meshes required')
    if not all(math.isfinite(x) and x>0 for x in p['acceptance'].values()):raise ValueError('finite positive tolerances required')
    if p['case']=='dielectric-interface':
        if not all(isinstance(n,int) and not isinstance(n,bool) and 16<=n<=2048 for n in p['meshes']):raise ValueError('invalid mesh')
        if not all(b==2*a for a,b in zip(p['meshes'],p['meshes'][1:])):raise ValueError('double each mesh')
        if not 0<p['center']<p['interface']<p['lengths'][0]:raise ValueError('invalid interface geometry')
        if min(p['epsilon_left'],p['epsilon_right'])<=0:raise ValueError('positive dielectric permittivity required')
    else:
        if not all(len(n)==2 and all(isinstance(v,int) and not isinstance(v,bool) and 4<=v<=2048 for v in n) for n in p['meshes']):raise ValueError('invalid mesh')
        if not all(b[0]==2*a[0] and b[1]==2*a[1] for a,b in zip(p['meshes'],p['meshes'][1:])):raise ValueError('double both mesh dimensions')
        if not 0<p['accuracy_time']<p['reflection_gate_start']<p['end_time']:raise ValueError('invalid time windows')
        if not 0<p['pml_thickness']<p['center']<p['monitor_x']<p['lengths'][0]-p['pml_thickness']:raise ValueError('invalid PML geometry')
        if not math.isfinite(p['pml_strength']) or p['pml_strength']<=0:raise ValueError('positive PML strength required')
        for nx,ny in p['meshes']:
            if abs(p['pml_thickness']*nx/p['lengths'][0]-round(p['pml_thickness']*nx/p['lengths'][0]))>1e-10:
                raise ValueError('PML interfaces must coincide with electric nodes for flux quadrature')
        for ky in p['transverse_wave_numbers']:
            if ky<0 or not math.isfinite(ky) or abs(ky*p['lengths'][1]/(2*np.pi)-round(ky*p['lengths'][1]/(2*np.pi)))>1e-10:raise ValueError('transverse mode must be periodic')


def evaluate(path):
    path=Path(path);p=json.loads(path.read_text());validate(p)
    rows=[];traces=[];waveforms=[];snapshot=None
    if p['case']=='dielectric-interface':
        for nx in p['meshes']:
            row,trace,snapshot=run_interface(p,nx);rows.append(row);traces+=trace
        def orders(key):return [float(np.log(a[key]/b[key])/np.log(2)) for a,b in zip(rows,rows[1:])]
        a=p['acceptance'];last=rows[-1]
        metrics=dict(meshes=rows,field_orders=orders('field_relative_l2'),reflection_orders=orders('reflection_amplitude_error'),transmission_orders=orders('transmission_amplitude_error'),
                     energy_orders=orders('energy_fraction_closure'))
        checks=dict(field_accuracy=last['field_relative_l2']<=a['max_field_error'],field_refinement=min(metrics['field_orders'])>=a['min_refinement_order'],
                    fresnel_amplitudes=max(last['reflection_amplitude_error'],last['transmission_amplitude_error'])<=a['max_amplitude_error'],
                    reflection_refinement=min(metrics['reflection_orders'])>=a['min_refinement_order'],
                    transmission_error_decreases=all(b['transmission_amplitude_error']<a['transmission_amplitude_error'] for a,b in zip(rows,rows[1:])),
                    physical_energy_refinement=min(metrics['energy_orders'])>=a['min_refinement_order'],
                    fresnel_energy_fractions=max(last['reflected_energy_error'],last['transmitted_energy_error'])<=a['max_energy_fraction_error'],
                    energy_fraction_closure=last['energy_fraction_closure']<=a['max_energy_closure'],
                    modified_energy=all(r['modified_energy_max_relative_drift']<=a['max_modified_energy_drift'] for r in rows))
    else:
        for ky in p['transverse_wave_numbers']:
            for nx,ny in p['meshes']:
                row,trace,snapshot,wave=run_pml(p,nx,ny,ky);rows.append(row);traces+=trace;waveforms+=wave
        series=[]
        for ky in p['transverse_wave_numbers']:
            values=[r for r in rows if r['ky']==ky]
            def orders(key):return [float(np.log(a[key]/b[key])/np.log(2)) for a,b in zip(values,values[1:])]
            series.append(dict(ky=ky,field_orders=orders('field_relative_l2'),reflection_orders=orders('reflected_waveform_max_error_ratio'),flux_budget_orders=orders('physical_region_flux_budget_max_relative_residual')))
        metrics=dict(meshes=rows,series=series)
        a=p['acceptance'];finest=[r for r in rows if r['nx']==p['meshes'][-1][0]]
        checks=dict(field_accuracy=all(r['field_relative_l2']<=a['max_field_error'] for r in finest),
                    field_refinement=all(min(s['field_orders'])>=a['min_field_refinement_order'] for s in series),
                    reflection_amplitude=all(r['reflection_amplitude_ratio']<=a['max_reflection_amplitude'] for r in finest),
                    reflection_refinement=all(min(s['reflection_orders'])>=a['min_reflection_refinement_order'] for s in series),
                    reflected_waveform_accuracy=all(r['reflected_waveform_max_error_ratio']<=a['max_reflection_waveform_error'] for r in finest),
                    pml_work_budget=all(r['modified_energy_budget_relative_residual']<=a['max_work_budget_residual'] for r in rows),
                    physical_flux_budget=all(r['physical_region_flux_budget_max_relative_residual']<=a['max_flux_budget_residual'] for r in finest),
                    physical_flux_refinement=all(min(s['flux_budget_orders'])>=a['min_flux_refinement_order'] for s in series),
                    net_absorption=all(r['total_pml_work_fraction']>.99 and r['remaining_physical_energy_fraction']<=a['max_remaining_energy_fraction'] for r in finest))
    result=dict(schema_version=1,case=p['case'],input_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),environment=dict(python=platform.python_version(),numpy=np.__version__),
                termination='fixed_budget_completed',metrics=metrics,checks={k:bool(v) for k,v in checks.items()},passed=bool(all(checks.values())))
    return result,traces,snapshot,waveforms


def save(out,result,traces,snapshot,waveforms):
    out.mkdir(parents=True,exist_ok=True)
    (out/'result.json').write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    with (out/'convergence.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(result['metrics']['meshes'][0]));w.writeheader();w.writerows(result['metrics']['meshes'])
    with (out/'energy.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['nx','ky','time','modified_energy','physical_energy','electric_PML_work','magnetic_PML_work','interior_physical_energy','outgoing_Poynting_integral'][:len(traces[0])]);w.writerows(traces)
    with (out/'solution.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['x','electric_field','reference_field']);w.writerows(zip(*snapshot))
    if waveforms:
        with (out/'waveforms.csv').open('w',newline='') as f:
            w=csv.writer(f);w.writerow(['nx','ky','time','monitor_E','reference_monitor_E','return_rms','analytic_return_E','measured_return_E']);w.writerows(waveforms)
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    fig,axs=plt.subplots(1,3,figsize=(13,3.8),constrained_layout=True)
    rows=result['metrics']['meshes'];is_pml=result['case']=='pml-pulse'
    for ky in sorted({r.get('ky',0.) for r in rows}):
        r=[v for v in rows if v.get('ky',0.)==ky];dx=[v['dx'] for v in r]
        axs[0].loglog(dx,[v['field_relative_l2'] for v in r],'o-',label='ky='+str(ky))
        key='reflected_waveform_max_error_ratio' if is_pml else 'reflection_amplitude_error'
        axs[1].loglog(dx,[v[key] for v in r],'o-',label='ky='+str(ky))
    axs[0].set(xlabel='Grid spacing dx',ylabel='Relative L2 field error',title='Continuum reference refinement');axs[0].legend()
    axs[1].set(xlabel='Grid spacing dx',ylabel='Return waveform error / incident RMS peak' if is_pml else 'Absolute Fresnel r error',title='Finite-PML analytic reflection error' if is_pml else 'Dielectric reflection amplitude');axs[1].legend()
    if is_pml:
        fine=[v for v in traces if v[0]==rows[-1]['nx'] and v[1]==rows[-1]['ky']];z=np.array(fine);u0=z[0,3]
        axs[2].plot(z[:,2],z[:,3]/u0,label='Modified energy')
        axs[2].plot(z[:,2],(z[:,5]+z[:,6])/u0,label='Integrated signed PML work')
        axs[2].plot(z[:,2],(z[:,3]+z[:,5]+z[:,6])/u0,label='Sum')
        axs[2].set(xlabel='Time',ylabel='Fraction of initial energy',title='Independent PML work balance')
    else:
        axs[2].plot(snapshot[0],snapshot[1],label='Yee Ez');axs[2].plot(snapshot[0],snapshot[2],'--',label='Fresnel analytic Ez')
        axs[2].set(xlabel='x',ylabel='Electric field',title='Reflected and transmitted pulses')
    axs[2].legend(fontsize=8)
    fig.savefig(out/'summary.png',dpi=150);plt.close(fig)


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--input',type=Path,required=True);parser.add_argument('--output',type=Path,required=True);a=parser.parse_args()
    try:
        if a.output.exists() and (not a.output.is_dir() or any(a.output.iterdir())):raise ValueError('new or empty output required')
        result,traces,snapshot,waveforms=evaluate(a.input);save(a.output,result,traces,snapshot,waveforms)
        print(json.dumps(dict(case=result['case'],passed=result['passed'],checks=result['checks'])));return 0 if result['passed'] else 1
    except Exception as e:print(str(e),file=sys.stderr);return 2

if __name__=='__main__':sys.exit(main())
