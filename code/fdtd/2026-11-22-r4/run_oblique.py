"""Fixed spectral Fresnel packet: exit 0 pass, 1 numerical fail, 2 input error."""
import argparse
import csv
import hashlib
import json
import math
from pathlib import Path
import platform
import sys
import numpy as np
import oblique as o


def validate(p):
    if p['case']!='dielectric-oblique':raise ValueError('unknown case')
    if len(p['lengths'])!=2 or not all(math.isfinite(v) and v>0 for v in p['lengths']):raise ValueError('positive finite lengths required')
    if not all(math.isfinite(p[k]) and p[k]>0 for k in ['width','carrier_kx','epsilon_left','epsilon_right','reference_period','spectral_cutoff','end_time','courant']):raise ValueError('positive finite parameters required')
    if not 0<p['courant']<1:raise ValueError('strict CFL required')
    if p['epsilon_right']<p['epsilon_left']:raise ValueError('this benchmark requires propagating low-to-high scattering')
    if not 0<p['center']<p['interface']<p['lengths'][0]:raise ValueError('ordered interior source and interface required')
    if len(p['flux_region'])!=2 or not 0<p['flux_region'][0]<p['interface']<p['flux_region'][1]<p['lengths'][0]:raise ValueError('interior flux region must straddle interface')
    if len(p['meshes'])!=3 or not all(len(v)==2 and all(isinstance(n,int) and not isinstance(n,bool) and 4<=n<=4096 for n in v) for v in p['meshes']):raise ValueError('three integer grids required')
    if not all(b==[2*a[0],2*a[1]] for a,b in zip(p['meshes'],p['meshes'][1:])):raise ValueError('both dimensions must double')
    ks,_=o.spectrum(p)
    for nx,ny in p['meshes']:
        if ks[-1]>=np.pi*nx/p['lengths'][0]:raise ValueError('actual spectrum exceeds Nyquist')
        for x in [p['interface'],*p['flux_region']]:
            if abs(x*nx/p['lengths'][0]-round(x*nx/p['lengths'][0]))>1e-10:raise ValueError('interface/flux planes must align')
    if p['reference_period']<2*p['lengths'][0]:raise ValueError('reference period too small')
    if not p['transverse_wave_numbers'] or not 0. in p['transverse_wave_numbers'] or not any(k>0 for k in p['transverse_wave_numbers']):raise ValueError('normal and oblique controls required')
    for ky in p['transverse_wave_numbers']:
        if not math.isfinite(ky) or ky<0 or ky>=np.pi*p['meshes'][0][1]/p['lengths'][1] or abs(ky*p['lengths'][1]/(2*np.pi)-round(ky*p['lengths'][1]/(2*np.pi)))>1e-10:raise ValueError('resolved periodic transverse mode required')
    if not all(math.isfinite(v) and v>0 for v in p['acceptance'].values()):raise ValueError('finite positive tolerances required')


def evaluate(path):
    path=Path(path);p=json.loads(path.read_text());validate(p)
    rows=[];histories=[];series=[];snapshot=None
    for ky in p['transverse_wave_numbers']:
        values=[]
        for nx,ny in p['meshes']:
            row,history,snapshot=o.run_mesh(p,nx,ny,ky);rows.append(row);values.append(row);histories+=history
        def orders(key):return [float(np.log(a[key]/b[key])/np.log(2)) for a,b in zip(values,values[1:])]
        incident,R,T=o.reference_energy(p,ky);large=o.reference_energy(p,ky,2*p['reference_period'])
        series.append(dict(ky=ky,field_orders=orders('field_relative_l2'),reflection_field_orders=orders('reflected_field_relative_l2'),transmission_field_orders=orders('transmitted_field_relative_l2'),
            reflection_energy_orders=orders('reflected_energy_error'),transmission_energy_orders=orders('transmitted_energy_error'),
            closure_orders=orders('energy_fraction_closure'),flux_orders=orders('physical_flux_budget_max_relative_residual'),
            reference_energy_period_doubling_error=float(max(abs(large[0]/incident-1),abs(large[1]-R),abs(large[2]-T)))))
    a=p['acceptance'];fine=[r for r in rows if r['nx']==p['meshes'][-1][0]]
    checks=dict(field_accuracy=all(r['field_relative_l2']<=a['max_field_error'] for r in fine),
        field_refinement=all(min(s['field_orders'])>=a['min_field_order'] for s in series),
        reflected_field_refinement=all(min(s['reflection_field_orders'])>=a['min_field_order'] for s in series),
        transmitted_field_refinement=all(min(s['transmission_field_orders'])>=a['min_field_order'] for s in series),
        spectral_template_amplitudes=all(max(r['reflection_gain_error'],r['transmission_gain_error'])<=a['max_template_gain_error'] for r in fine),
        fresnel_energy_fractions=all(max(r['reflected_energy_error'],r['transmitted_energy_error'])<=a['max_energy_fraction_error'] for r in fine),
        reflected_energy_refinement=all(min(s['reflection_energy_orders'])>=a['min_energy_order'] for s in series),
        transmitted_energy_refinement=all(min(s['transmission_energy_orders'])>=a['min_energy_order'] for s in series),
        energy_fraction_closure=all(r['energy_fraction_closure']<=a['max_energy_closure'] for r in fine),
        modified_energy=all(r['modified_energy_max_relative_drift']<=a['max_modified_energy_drift'] for r in rows),
        independent_flux_balance=all(r['physical_flux_budget_max_relative_residual']<=a['max_flux_residual'] for r in fine),
        flux_refinement=all(min(s['flux_orders'])>=a['min_flux_order'] for s in series),
        reference_period_control=all(r['reference_period_doubling_relative_l2']<=a['max_reference_period_error'] for r in rows) and all(s['reference_energy_period_doubling_error']<=a['max_reference_period_error'] for s in series),
        finite_window_reference=all(r['reference_window_energy_error']<=a['max_reference_window_error'] for r in rows),
        reference_initial_energy_norm=all(abs(r['reference_initial_energy_ratio']-1)<=a['max_reference_window_error'] for r in rows),
        initial_secondary_fields=all(max(r['initial_secondary_field_energy_fraction'],r['initial_pec_clipping_field_norm_fraction'])<=a['max_initial_secondary_energy_fraction'] for r in rows),
        distant_pec_caps=all(r['analytic_cap_electric_max']<=a['max_analytic_cap_field'] for r in rows))
    result=dict(schema_version=1,case=p['case'],input_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),environment=dict(python=platform.python_version(),numpy=np.__version__),
        termination='fixed_budget_completed',polarization='TMz Ez; optical s/TE for incidence in x-y plane',
        reference_scope='Exact continuum modal Fresnel fields evaluated by finite positive-k spectral quadrature. Parseval packet R/T refer to the underlying continuous spectrum; period doubling and finite-window controls are recorded. No independent external solver or PML comparison.',
        amplitude_scope='Signed least-squares gains of numerical E against exact broadband reflected/transmitted templates; expected gain 1, not a measured monochromatic carrier r or t.',
        energy_normalization='Reflected/transmitted physical energies divided by the continuous incident packet Parseval quadrature. Initial numerical physical energy ratio is recorded separately.',
        initial_secondary_scope='Squared weighted field norms at staggered initial clocks; distinct from same-time physical energy. Initial PEC clipping norm is checked separately with the same bound.',
        metrics=dict(meshes=rows,series=series),checks={k:bool(v) for k,v in checks.items()},passed=bool(all(checks.values())))
    return result,histories,snapshot,p


def save(out,result,history,snapshot,p):
    out.mkdir(parents=True,exist_ok=True)
    (out/'result.json').write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    with (out/'convergence.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(result['metrics']['meshes'][0]));w.writeheader();w.writerows(result['metrics']['meshes'])
    with (out/'energy.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['nx','ny','ky','time','modified_energy','physical_energy','interface_region_energy','flux_left_integral','flux_right_integral']);w.writerows(history)
    with (out/'solution.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['x','Ez_at_y0','continuum_Ez_at_y0']);w.writerows(zip(*snapshot))
    k,a=o.spectrum(p)
    with (out/'spectrum.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['ky','kx','amplitude','energy_weight','omega','kx_transmitted','r_s','t_s','R_s','T_s','dkx2_dkx'])
        for ky in p['transverse_wave_numbers']:
            z=o.fresnel(k,ky,p['epsilon_left'],p['epsilon_right'])
            w.writerows(zip(np.full_like(k,ky),k,a,a*a,z['omega'],z['q'],z['r'],z['t'],z['R'],z['T'],z['qprime']))
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    fig,axs=plt.subplots(1,3,figsize=(13,3.8),constrained_layout=True)
    for ky in p['transverse_wave_numbers']:
        rows=[r for r in result['metrics']['meshes'] if r['ky']==ky];label=f"{rows[0]['incident_angle_degrees']:.2f} deg carrier"
        axs[0].loglog([r['dx'] for r in rows],[r['field_relative_l2'] for r in rows],'o-',label=label)
        axs[1].loglog([r['dx'] for r in rows],[r['reflected_energy_error'] for r in rows],'o-',label='R, '+label)
        axs[1].loglog([r['dx'] for r in rows],[r['transmitted_energy_error'] for r in rows],'s--',label='T, '+label)
    axs[0].set(xlabel='Grid spacing dx',ylabel='Relative L2 field error',title='Spectral Fresnel field refinement');axs[0].legend(fontsize=8)
    axs[1].set(xlabel='Grid spacing dx',ylabel='Absolute packet energy-fraction error',title='Reflection / transmission error');axs[1].legend(fontsize=7)
    axs[2].plot(snapshot[0],snapshot[1],label='Yee Ez');axs[2].plot(snapshot[0],snapshot[2],'--',label='Spectral Fresnel Ez')
    axs[2].axvline(p['interface'],color='grey',ls=':',label='Dielectric interface');axs[2].set(xlabel='x at y=0',ylabel='Electric field',title='Oblique reflected / transmitted packets');axs[2].legend(fontsize=8)
    fig.savefig(out/'summary.png',dpi=150);plt.close(fig)


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--input',type=Path,required=True);parser.add_argument('--output',type=Path,required=True);a=parser.parse_args()
    try:
        if a.output.exists() and (not a.output.is_dir() or any(a.output.iterdir())):raise ValueError('new or empty output required')
        result,history,snapshot,p=evaluate(a.input);save(a.output,result,history,snapshot,p)
        print(json.dumps(dict(case=result['case'],passed=result['passed'],checks=result['checks'])));return 0 if result['passed'] else 1
    except Exception as error:print(str(error),file=sys.stderr);return 2


if __name__=='__main__':sys.exit(main())
