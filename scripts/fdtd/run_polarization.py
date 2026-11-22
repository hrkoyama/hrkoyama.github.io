"""Fixed TEz p-polarization/Brewster/TIR example: 0 pass,1 fail,2 invalid."""
import argparse,csv,hashlib,json,math,platform,sys
from pathlib import Path
import numpy as np
import polarization as o


def validate(p):
    if p['case']!='p-polarization':raise ValueError('unknown case')
    if not all(math.isfinite(p[k]) and p[k]>0 for k in ['reference_period','courant','accuracy_time']):raise ValueError('positive finite parameters required')
    if not 0<p['courant']<1:raise ValueError('strict CFL required')
    if [c['id'] for c in p['subcases']]!=['propagating','brewster','tir']:raise ValueError('three named p-polarized cases required')
    for c in p['subcases']:
        if not all(math.isfinite(c[k]) and c[k]>0 for k in ['center','interface','width','carrier_kx','ky','band_half_width','epsilon_left','epsilon_right','end_time','monitor_offset','accuracy_time']):raise ValueError('finite positive case parameters required')
        if not 0<c['center']<c['interface']<c['lengths'][0]:raise ValueError('ordered packet and interface required')
        if not p['accuracy_time']<c['accuracy_time']<c['end_time']:raise ValueError('ordered field and fluence clocks required')
        if len(c['meshes'])!=3 or not all(len(z)==2 and all(isinstance(n,int) and not isinstance(n,bool) and 4<=n<=32768 for n in z) for z in c['meshes']):raise ValueError('three positive integer grids required')
        if any(b!=[2*a[0],2*a[1]] for a,b in zip(c['meshes'],c['meshes'][1:])):raise ValueError('both spatial dimensions must double')
        if not np.allclose(c['band'],[c['carrier_kx']-c['band_half_width'],c['carrier_kx']+c['band_half_width']],rtol=0,atol=1e-13):raise ValueError('symmetric compact positive-k support required')
        if c['band'][0]<=0 or p['reference_period']<2*c['lengths'][0]:raise ValueError('positive spectrum and sufficient quadrature period required')
        k,_=o.spectrum(p,c);f=o.fresnel(k,c['ky'],c['epsilon_left'],c['epsilon_right'])
        if c['id']=='tir':
            if not np.all(np.imag(f['q'])>0):raise ValueError('every TIR mode must be evanescent')
        elif not np.all(np.real(f['q'])>0):raise ValueError('every non-TIR mode must propagate')
        for nx,ny in c['meshes']:
            dx=c['lengths'][0]/nx
            if max(k[-1],np.max(np.abs(f['q'])))>=np.pi/dx:raise ValueError('normal spectrum exceeds Nyquist')
            for x in [c['interface'],c['interface']-c['monitor_offset'],c['interface']+c['monitor_offset'],c['interface']+2*c['monitor_offset'],*c['flux_region']]:
                if not 0<x<c['lengths'][0] or abs(x/dx-round(x/dx))>1e-9:raise ValueError('interior monitor/flux planes must align')
            o.geometry(nx,ny,c['lengths'],.1*dx,c['epsilon_left'],c['epsilon_right'],c['interface'],c['ky'])
    if not all(math.isfinite(v) and v>0 for v in p['acceptance'].values()):raise ValueError('positive finite tolerances required')


def evaluate(path):
    path=Path(path);p=json.loads(path.read_text());validate(p);rows=[];histories=[];snapshots={};waveforms={};series=[]
    for c in p['subcases']:
        values=[];waves=[]
        for nx,ny in c['meshes']:
            row,h,s,w=o.run_mesh(p,c,nx,ny);rows.append(row);values.append(row);histories.extend(h);snapshots[c['id']]=s;waves.append((nx,ny,w))
        waveforms[c['id']]=waves
        def orders(key):return [float(np.log(a[key]/b[key])/np.log(2)) for a,b in zip(values,values[1:])]
        reference=o.incident_energy(p,c);large=o.incident_energy(p,c,2*p['reference_period'])
        series.append(dict(subcase=c['id'],field_orders=orders('field_relative_l2'),reflection_orders=orders('reflection_error'),transmission_fluence_orders=orders('transmission_error'),transmitted_flux_waveform_orders=orders('transmitted_flux_waveform_relative_l2'),complex_r_orders=orders('complex_r_error'),complex_t_orders=orders('complex_t_error'),flux_orders=orders('physical_flux_budget_max_relative_residual'),decay_orders=orders('decay_rate_error') if c['id']=='tir' else [],reference_energy_period_doubling_error=float(max(abs(large[0]/reference[0]-1),abs(large[1]-reference[1]),abs(large[2]-reference[2])))))
    a=p['acceptance'];fine=[next(r for r in reversed(rows) if r['subcase']==c['id']) for c in p['subcases']];b=next(r for r in fine if r['subcase']=='brewster');tir=next(r for r in fine if r['subcase']=='tir');ts=next(s for s in series if s['subcase']=='tir')
    checks=dict(field_accuracy=all(r['field_relative_l2']<=a['max_field_error'] for r in fine),pre_interface_accuracy=all(r['pre_interface_field_relative_l2']<=a['max_early_field_error'] for r in fine),field_refinement=all(min(s['field_orders'])>=a['min_field_order'] for s in series),
        fresnel_packet_flux=all(max(r['reflection_error'],r['transmission_error'])<=a['max_energy_fraction_error'] for r in fine),packet_reflection_refinement=all(min(s['reflection_orders'])>=a['min_energy_order'] for s in series),packet_transmission_refinement=all(min(s['transmission_fluence_orders'])>=a['min_energy_order'] for s in series if s['subcase']!='tir'),energy_fraction_closure=all(r['energy_fraction_closure']<=a['max_energy_closure'] for r in fine),
        complex_fresnel_amplitudes=all(r['carrier_complex_r_error']<=a['max_complex_r_error'] and r['carrier_complex_t_error']<=a['max_complex_t_error'] for r in fine),complex_reflection_refinement=all(min(s['complex_r_orders'])>=a['min_complex_r_order'] for s in series),
        modified_energy=all(r['modified_energy_max_relative_drift']<=a['max_modified_energy_drift'] for r in rows),independent_physical_flux=all(r['physical_flux_budget_max_relative_residual']<=a['max_flux_residual'] for r in fine),flux_refinement=all(min(s['flux_orders'])>=a['min_flux_order'] for s in series),
        reference_period_control=all(r['reference_period_doubling_relative_l2']<=a['max_reference_period_error'] for r in rows) and all(s['reference_energy_period_doubling_error']<=a['max_reference_period_error'] for s in series),finite_window_fluence_control=all(r['reference_window_energy_gap']<=a['max_reference_window_energy_gap'] for r in rows),finite_window_dft_control=all(max(r['reference_dft_r_error'],r['reference_dft_t_error'])<=a['max_reference_dft_error'] for r in rows),
        initial_secondary_fields=all(r['initial_secondary_field_norm_fraction']<=a['max_initial_secondary_norm_fraction'] for r in rows),distant_pec_caps=all(r['analytic_cap_tangential_electric_max']<=a['max_analytic_cap_field'] for r in rows),incident_fluence_normalization=all(r['incident_fluence_energy_relative_error']<=a['max_incident_fluence_error'] for r in fine),
        brewster_carrier_null=abs(complex(b['numerical_rH_real'],b['numerical_rH_imag']))<=a['max_brewster_carrier_reflection'],brewster_finite_band_residual=0<b['analytic_R'] and b['reflection_flux_fraction']<=a['max_brewster_packet_reflection'],
        tir_flux=abs(tir['reflection_flux_fraction']-1)<=a['max_energy_fraction_error'] and abs(tir['transmission_flux_fraction'])<=a['max_tir_transmission'],tir_nonzero_reactive_storage=tir['max_right_stored_energy_fraction']>=a['min_tir_peak_stored_energy'] and tir['min_transmitted_instantaneous_flux']<0<tir['max_transmitted_instantaneous_flux'],
        tir_decay_accuracy=tir['carrier_decay_rate_error']<=a['max_decay_error'] and tir['reference_decay_rate_error']<=a['max_reference_decay_error'],tir_decay_refinement=min(ts['decay_orders'])>=a['min_decay_order'],tir_stored_energy_reference=tir['peak_right_stored_energy_relative_error']<=a['max_stored_energy_error'],tir_transient_flux_waveform_accuracy=tir['transmitted_flux_waveform_relative_l2']<=a['max_tir_flux_waveform_error'],tir_transient_flux_waveform_refinement=min(ts['transmitted_flux_waveform_orders'])>=a['min_energy_order'])
    return dict(schema_version=1,case=p['case'],input_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),environment=dict(python=platform.python_version(),numpy=np.__version__),termination='fixed_budget_completed',polarization='TEz Hz,Ex,Ey; optical p polarization in xy incidence plane',backend='Exact single-positive-ky reduction of full periodic-y 2D Yee; full 2D equivalence is tested.',amplitude_scope='rH/tH are Hz amplitudes. Temporal DFT ratios use discrete-dispersion phase deembedding; finite-window continuum references and ideal carrier errors are distinct.',energy_scope='R/T are reflected/transmitted time-integrated normal Poynting fluences normalized to a separate homogeneous same-Yee incident run. Evanescent stored energy is not T.',tir_refinement_scope='Near-zero net-T fluence errors/orders remain diagnostics. TIR transmission refinement instead checks the noncancelling time-resolved transmitted-flux L2 error.',field_scope='Field accuracy is measured during interface interaction at per-case accuracy_time. Late field error at the longer fluence end is a separate diagnostic.',metrics=dict(meshes=rows,series=series),checks={k:bool(v) for k,v in checks.items()},passed=all(checks.values())),histories,snapshots,waveforms,p


def save(out,result,history,snapshots,waveforms,p):
    out.mkdir(parents=True,exist_ok=True);(out/'result.json').write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    with (out/'convergence.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(result['metrics']['meshes'][0]));w.writeheader();w.writerows(result['metrics']['meshes'])
    with (out/'energy.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['subcase','nx','ny','time','modified_energy','physical_energy','region_energy','flux_left_integral','flux_right_integral','right_stored_energy']);w.writerows(history)
    with (out/'solution.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['subcase','x','Hz_mode_real','Hz_mode_imag','reference_Hz_mode_real','reference_Hz_mode_imag'])
        for name,(x,h,r) in snapshots.items():w.writerows(zip([name]*len(x),x,h.real,h.imag,r.real,r.imag))
    with (out/'spectrum.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['subcase','kx','ky','epsilon_left','epsilon_right','amplitude','energy_weight','dk','omega','q_real','q_imag','rH_real','rH_imag','tH_real','tH_imag','R','T'])
        for c in p['subcases']:
            k,a=o.spectrum(p,c);z=o.fresnel(k,c['ky'],c['epsilon_left'],c['epsilon_right']);w.writerows(zip([c['id']]*len(k),k,np.full_like(k,c['ky']),np.full_like(k,c['epsilon_left']),np.full_like(k,c['epsilon_right']),a,a*a,np.full_like(k,2*np.pi/p['reference_period']),z['omega'],z['q'].real,z['q'].imag,z['r'].real,z['r'].imag,z['t'].real,z['t'].imag,z['R'],z['T']))
    signal_names=['incident_H','incident_Ey','reflected_H','reflected_Ey','transmitted_H','transmitted_Ey','second_transmitted_H'];header=['subcase','nx','ny','time']+[prefix+name+'_'+part for prefix in ['','analytic_'] for name in signal_names for part in ['real','imag']]+['incident_flux','reflected_flux','transmitted_flux','analytic_incident_flux','analytic_reflected_flux','analytic_transmitted_flux']
    for name,values in waveforms.items():
        with (out/('waveforms-'+name+'.csv')).open('w',newline='') as f:
            w=csv.writer(f);w.writerow(header)
            for nx,ny,arr in values:
                for row in arr:w.writerow([name,nx,ny,float(row[0].real)]+[float(v) for z in row[1:15] for v in [z.real,z.imag]]+[float(v.real) for v in row[15:]])
    import matplotlib;matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    fig,axs=plt.subplots(2,3,figsize=(13,7),constrained_layout=True)
    for name in ['propagating','brewster','tir']:
        r=[r for r in result['metrics']['meshes'] if r['subcase']==name];dx=[x['dx'] for x in r]
        axs[0,0].loglog(dx,[x['field_relative_l2'] for x in r],'o-',label=name);axs[0,1].loglog(dx,[x['complex_r_error'] for x in r],'o-',label=name)
        if name!='tir':axs[0,2].loglog(dx,[x['reflection_error'] for x in r],'o-',label=name+' R');axs[0,2].loglog(dx,[x['transmission_error'] for x in r],'s--',label=name+' T')
    axs[0,0].set(title='Field error during interface interaction',xlabel='dx',ylabel='Relative field L2 error');axs[0,1].set(title='Complex reflected Hz coefficient',xlabel='dx',ylabel='Error vs finite-window Fresnel DFT');axs[0,2].set(title='Integrated reflection / transmission',xlabel='dx',ylabel='Absolute fluence-fraction error')
    for ax in axs[0]:ax.legend(fontsize=8)
    r=[r for r in result['metrics']['meshes'] if r['subcase']=='tir'];axs[1,0].plot([x['dx'] for x in r],[x['numerical_decay_rate'] for x in r],'o-',label='Yee DFT decay');axs[1,0].axhline(r[-1]['carrier_q_imag'],ls='--',label='Continuum carrier kappa');axs[1,0].axhline(r[-1]['reference_window_decay_rate'],ls=':',label='Finite-window DFT reference');axs[1,0].set(title='TIR evanescent decay',xlabel='dx',ylabel='Decay rate');axs[1,0].legend(fontsize=8)
    finest=r[-1]['nx'];hist=np.array([[*row[3:]] for row in history if row[0]=='tir' and row[1]==finest]);u0=hist[0,1];incident=r[-1]['analytic_incident_energy']
    axs[1,1].plot(hist[:,0],hist[:,-1]/incident,label='Right stored energy');axs[1,1].set(title='TIR reactive field stores energy',xlabel='Time',ylabel='Fraction of incident packet energy');axs[1,1].legend(fontsize=8)
    axs[1,2].plot(hist[:,0],(hist[:,1]-u0)/u0,label='Modified-energy drift');axs[1,2].set(title='Closed-domain energy invariant',xlabel='Time',ylabel='Relative drift');axs[1,2].legend(fontsize=8)
    fig.savefig(out/'summary.png',dpi=150);plt.close(fig)


def main():
    q=argparse.ArgumentParser(description=__doc__);q.add_argument('--input',type=Path,required=True);q.add_argument('--output',type=Path,required=True);a=q.parse_args()
    try:
        if a.output.exists() and (not a.output.is_dir() or any(a.output.iterdir())):raise ValueError('new or empty output required')
        r,h,s,w,p=evaluate(a.input);save(a.output,r,h,s,w,p);print(json.dumps(dict(case=r['case'],passed=r['passed'],checks=r['checks'])));return 0 if r['passed'] else 1
    except Exception as e:print(str(e),file=sys.stderr);return 2
if __name__=='__main__':sys.exit(main())
