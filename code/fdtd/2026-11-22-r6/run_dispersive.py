"""Fixed vacuum/slab/vacuum loss + Lorentz example: 0 pass,1 fail,2 invalid."""
import argparse,csv,hashlib,json,math,platform,sys
from pathlib import Path
import numpy as np
import dispersive as d


def validate(p):
    if p['case']!='loss-dispersion':raise ValueError('unknown case')
    if not math.isfinite(p['reference_period']) or p['reference_period']<=0 or not 0<p['courant']<1:raise ValueError('finite positive period and strict CFL required')
    if [c['id'] for c in p['subcases']]!=['ohmic','lorentz']:raise ValueError('named Ohmic and Lorentz cases required')
    for c in p['subcases']:
        if not all(math.isfinite(c[k]) and c[k]>0 for k in ['length','center','width','carrier','spectrum_max','epsilon_inf','omega0','end_time','accuracy_time','time_quantum']):raise ValueError('positive finite parameters required')
        if not all(math.isfinite(c[k]) and c[k]>=0 for k in ['sigma','delta_epsilon','gamma']):raise ValueError('passive material required')
        if c['id']=='ohmic' and not(c['sigma']>0 and c['delta_epsilon']==0):raise ValueError('Ohmic case required')
        if c['id']=='lorentz' and not(c['sigma']==0 and c['delta_epsilon']>0 and c['gamma']>0):raise ValueError('damped Lorentz case required')
        if not 0<c['center']<c['monitors'][0]<c['slab'][0]<c['slab'][1]<c['monitors'][1]<c['length']:raise ValueError('ordered aligned slab and vacuum monitors required')
        if not 0<c['accuracy_time']<c['end_time'] or p['reference_period']<c['length']:raise ValueError('ordered clocks and long reference period required')
        if len(c['meshes'])!=3 or any(isinstance(n,bool) or not isinstance(n,int) or not 8<=n<=32768 for n in c['meshes']) or c['meshes'][1:]!=[2*c['meshes'][0],4*c['meshes'][0]]:raise ValueError('three doubling integer meshes required')
        for clock in ['accuracy_time','end_time']:
            if abs(c[clock]/c['time_quantum']-round(c[clock]/c['time_quantum']))>1e-10:raise ValueError('all clocks must share time quantum')
        for nx in c['meshes']:
            n,dt=d.clock(p,c,nx);g=d.geometry(nx,c,dt)
            for x in c['monitors']:
                if abs(x/g['dx']-round(x/g['dx']))>1e-9:raise ValueError('aligned vacuum monitors required')
            if c['spectrum_max']>=np.pi/g['dx']:raise ValueError('positive-frequency spectrum must be below Nyquist')
    if not all(math.isfinite(v) and v>0 for v in p['acceptance'].values()):raise ValueError('finite positive tolerances required')


def temporal_series(p,c):
    states=[];clocks=[];nx=c['meshes'][0]
    for factor in [1,2,4]:
        _,dt=d.clock(p,c,nx,factor);g=d.geometry(nx,c,dt);s=d.initial(g,p,c);n=int(round(c['accuracy_time']/dt))
        for _ in range(n):s=d.step(s,g)
        states.append(s[0]);clocks.append(dict(steps=n,dt=dt))
    errors=[float(np.linalg.norm(a-b)/np.linalg.norm(states[-1])) for a,b in zip(states,states[1:])]
    return dict(nx=nx,accuracy_time=c['accuracy_time'],clocks=clocks,relative_field_differences=errors,self_convergence_order=float(np.log2(errors[0]/errors[1])))


def evaluate(path):
    path=Path(path);p=json.loads(path.read_text());validate(p);rows=[];history=[];snapshots={};waves={};series=[]
    for c in p['subcases']:
        values=[];waves[c['id']]=[]
        for nx in c['meshes']:
            row,h,s,w,_=d.run_mesh(p,c,nx);rows.append(row);values.append(row);history.extend(h);snapshots[c['id']]=s;waves[c['id']].append((nx,w))
        keys=['field_relative_l2','reflection_error','transmission_error','absorption_error','complex_r_error','complex_t_error','physical_flux_budget_max_relative_residual','physical_energy_max_relative_balance']
        if c['delta_epsilon']>0:keys+=['polarization_relative_l2','current_relative_l2']
        orders={key:[float(np.log2(a[key]/b[key])) for a,b in zip(values,values[1:])] for key in keys}
        w,amp=d.spectrum(p,c);w2,amp2=d.spectrum(p,c,2*p['reference_period']);z=d.slab(w,c);z2=d.slab(w2,c);q=d.direct_spectral_absorption(w,c);q2=d.direct_spectral_absorption(w,c,256)
        reference_control=max(abs(np.sum(amp*amp*z[key])/np.sum(amp*amp)-np.sum(amp2*amp2*z2[key])/np.sum(amp2*amp2)) for key in ['R','T','A'])
        series.append(dict(subcase=c['id'],orders=orders,temporal=temporal_series(p,c),reference_energy_period_doubling_relative_error=float(abs(2*np.sum(amp2*amp2)/np.sum(amp*amp)-1)),reference_fractions_period_doubling_error=float(reference_control),reference_direct_absorption_closure=float(np.max(abs(q-z['A']))),reference_spatial_quadrature_doubling_error=float(np.max(abs(q-q2))),positive_frequency_omitted_energy_bound=float(math.erfc(c['width']*c['carrier'])/2),upper_frequency_omitted_energy_bound=float(math.erfc(c['width']*(c['spectrum_max']-c['carrier']))/2)))
    fine=[rows[(i+1)*3-1] for i in range(2)];a=p['acceptance']
    checks=dict(field_accuracy=all(r['field_relative_l2']<=a['max_field_error'] for r in fine),field_refinement=all(min(s['orders']['field_relative_l2'])>=a['min_field_order'] for s in series),slab_packet_RTA=all(max(r[k] for k in ['reflection_error','transmission_error','absorption_error'])<=a['max_energy_fraction_error'] for r in fine),RTA_refinement=all(min(s['orders'][k])>=a['min_energy_order'] for s in series for k in ['reflection_error','transmission_error','absorption_error']),complex_slab_amplitudes=all(max(r['carrier_complex_r_error'],r['carrier_complex_t_error'])<=a['max_complex_coefficient_error'] for r in fine),complex_amplitude_refinement=all(min(s['orders'][k])>=a['min_complex_order'] for s in series for k in ['complex_r_error','complex_t_error']),energy_fraction_closure=all(r['energy_fraction_closure']<=a['max_energy_closure'] for r in fine),direct_absorption_nonnegative=all(r['ohmic_absorption_fraction']>=0 and r['lorentz_absorption_fraction']>=0 for r in rows),exact_modified_energy_balance=all(r['modified_energy_max_relative_balance']<=a['max_modified_energy_balance'] for r in rows),independent_physical_flux=all(r['physical_flux_budget_max_relative_residual']<=a['max_physical_flux_residual'] for r in fine),physical_flux_refinement=all(min(s['orders']['physical_flux_budget_max_relative_residual'])>=a['min_flux_order'] for s in series),final_material_tail=all(r['final_material_energy_fraction']<=a['max_final_material_energy'] for r in fine),reference_period_control=all(r['reference_period_doubling_relative_l2']<=a['max_reference_period_error'] for r in rows) and all(max(s['reference_energy_period_doubling_relative_error'],s['reference_fractions_period_doubling_error'])<=a['max_reference_period_error'] for s in series),reference_direct_absorption=all(max(s['reference_direct_absorption_closure'],s['reference_spatial_quadrature_doubling_error'])<=a['max_reference_quadrature_error'] for s in series),finite_window_fluence=all(r['reference_window_fluence_gap']<=a['max_reference_window_gap'] for r in rows),finite_window_DFT=all(max(r['reference_dft_r_error'],r['reference_dft_t_error'])<=a['max_reference_dft_error'] for r in rows),distant_PEC_caps=all(r['analytic_cap_electric_max']<=a['max_analytic_cap_field'] for r in rows),initial_secondary_tails=all(r['initial_secondary_field_norm_fraction']<=a['max_initial_secondary_field_norm'] for r in rows),incident_fluence_normalization=all(r['incident_fluence_energy_relative_error']<=a['max_incident_fluence_error'] for r in fine),fixed_space_time_refinement=all(s['temporal']['self_convergence_order']>=a['min_time_order'] for s in series))
    lorentz=next(s for s in series if s['subcase']=='lorentz')
    checks.update(initial_full_analytic_tails=all(max(r['initial_secondary_E_relative_l2'],r['initial_secondary_H_relative_l2'],np.sqrt(r['initial_omitted_material_energy_fraction']))<=a['max_initial_secondary_field_norm'] for r in rows),material_PJ_accuracy=all(max(r['polarization_relative_l2'],r['current_relative_l2'])<=a['max_field_error'] for r in fine),material_PJ_refinement=all(min(lorentz['orders'][key])>=a['min_field_order'] for key in ['polarization_relative_l2','current_relative_l2']),finite_window_energy_with_storage=all(r['finite_window_energy_fraction_residual']<=a['max_energy_closure'] for r in fine))
    result=dict(schema_version=1,case=p['case'],input_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),environment=dict(python=platform.python_version(),numpy=np.__version__),termination='fixed_budget_completed',backend='Original 1D normal-incidence Yee TMz E_z/H_y with local implicit-midpoint passive Lorentz ADE; complex two-real-quadrature fields.',scope='Finite slab in vacuum; no PML, oblique incidence, anisotropy, Drude pole, nonlinear or negative-strength gain model. PEC caps are distant and measured, never prescribed outgoing fields.',field_scope='field_relative_l2 compares E_z at the interaction clock; Lorentz P and J norms and refinement are also checked independently.',energy_scope='R/T are independent exterior Poynting fluences normalized to a homogeneous same-Yee vacuum run. A is directly integrated sigma|Ebar|²+gamma|Jbar|²/f; oscillator storage is separate. Exact modified balance and approximate physical control-volume balance are distinct.',amplitude_scope='r/t are electric-field coefficients at the front/back slab faces. Finite-window continuum DFT and ideal carrier errors are separate; numerical vacuum phases use the Yee dispersion relation.',refinement_scope='Three joint dx/dt meshes against continuum; fixed-coarse-space time-halving self-convergence at the interaction clock is a separate test.',metrics=dict(meshes=rows,series=series),checks={k:bool(v) for k,v in checks.items()},passed=bool(all(checks.values())))
    return result,history,snapshots,waves,p


def save(out,result,history,snapshots,waves,p):
    out.mkdir(parents=True,exist_ok=True);(out/'result.json').write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    with (out/'convergence.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(result['metrics']['meshes'][0]));w.writeheader();w.writerows(result['metrics']['meshes'])
    with (out/'energy.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['subcase','nx','time','modified_energy','physical_energy','material_energy','region_energy','ohmic_loss','lorentz_loss','ohmic_power_to_next_time','lorentz_power_to_next_time']);w.writerows(history)
    with (out/'solution.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['subcase','x','E_real','E_imag','reference_E_real','reference_E_imag','P_real','P_imag','J_real','J_imag'])
        for name,(x,e,r,pol,j) in snapshots.items():w.writerows(zip([name]*len(x),x,e.real,e.imag,r.real,r.imag,pol.real,pol.imag,j.real,j.imag))
    with (out/'spectrum.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['subcase','omega','amplitude','weight','epsilon_real','epsilon_imag','n_real','n_imag','r_real','r_imag','t_real','t_imag','R','T','A','A_direct'])
        for c in p['subcases']:
            om,a=d.spectrum(p,c);z=d.slab(om,c);w.writerows(zip([c['id']]*len(om),om,a,a*a,z['epsilon'].real,z['epsilon'].imag,z['n'].real,z['n'].imag,z['r'].real,z['r'].imag,z['t'].real,z['t'].imag,z['R'],z['T'],z['A'],d.direct_spectral_absorption(om,c)))
    names=['incident_E','incident_H','reflected_E','reflected_H','transmitted_E','transmitted_H','vacuum_right_E','vacuum_right_H','reference_incident_E','reference_reflected_E','reference_transmitted_E','reference_vacuum_right_E']
    for name,values in waves.items():
        with (out/('waveforms-'+name+'.csv')).open('w',newline='') as f:
            w=csv.writer(f);w.writerow(['subcase','nx','time']+[n+'_'+part for n in names for part in ['real','imag']]+['incident_flux','reflected_flux','transmitted_flux','physical_region_budget_fraction','material_energy_fraction'])
            for nx,arr in values:
                for row in arr:w.writerow([name,nx,float(row[0].real)]+[float(v) for z in row[1:13] for v in [z.real,z.imag]]+[float(v.real) for v in row[13:]])
    import matplotlib;matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    fig,ax=plt.subplots(2,3,figsize=(13,7),constrained_layout=True)
    for name in ['ohmic','lorentz']:
        rows=[r for r in result['metrics']['meshes'] if r['subcase']==name];h=[r['dx'] for r in rows]
        ax[0,0].loglog(h,[r['field_relative_l2'] for r in rows],'o-',label=name)
        for key,style in [('reflection_error','o-'),('transmission_error','s--'),('absorption_error','^:')]:ax[0,1].loglog(h,[r[key] for r in rows],style,label=name+' '+key.split('_')[0])
        ax[0,2].loglog(h,[r['physical_flux_budget_max_relative_residual'] for r in rows],'o-',label=name)
        c=next(c for c in p['subcases'] if c['id']==name);om,a=d.spectrum(p,c);z=d.slab(om,c);ax[1,0].plot(om,z['R'],label=name+' R');ax[1,0].plot(om,z['T'],'--',label=name+' T');ax[1,0].plot(om,z['A'],':',label=name+' A')
        finest=rows[-1]['nx'];hist=np.array([r[2:] for r in history if r[0]==name and r[1]==finest]);u0=hist[0,1]
        ax[1,1].plot(hist[:,0],hist[:,3]/u0,label=name+' stored');ax[1,1].plot(hist[:,0],(hist[:,5]+hist[:,6])/u0,'--',label=name+' direct loss')
        ax[1,2].plot(hist[:,0],(hist[:,1]+hist[:,5]+hist[:,6]-u0)/u0,label=name)
    titles=['Field error at interaction time','Packet R / T / direct A errors','Physical control-volume residual','Continuum slab coefficients','Material storage and direct loss','Exact modified-energy balance']
    for a,title in zip(ax.flat,titles):a.set_title(title,fontsize=10);a.legend(fontsize=7);a.grid(alpha=.2)
    for a in ax[0]:a.set_xlabel('dx')
    ax[1,0].set_xlabel('Angular frequency');ax[1,1].set_xlabel('Time');ax[1,2].set_xlabel('Time');fig.savefig(out/'summary.png',dpi=150);plt.close(fig)


def main():
    q=argparse.ArgumentParser(description=__doc__);q.add_argument('--input',type=Path,required=True);q.add_argument('--output',type=Path,required=True);a=q.parse_args()
    try:
        if a.output.exists() and (not a.output.is_dir() or any(a.output.iterdir())):raise ValueError('new or empty output required')
        r,h,s,w,p=evaluate(a.input);save(a.output,r,h,s,w,p);print(json.dumps(dict(case=r['case'],passed=r['passed'],checks=r['checks'])));return 0 if r['passed'] else 1
    except Exception as e:print(str(e),file=sys.stderr);return 2
if __name__=='__main__':sys.exit(main())
