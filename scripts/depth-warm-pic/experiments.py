"""Frozen study table,scalar records and transparent fixed-ensemble decisions."""
import numpy as np
from scipy.stats import t as student_t
import primary,loading
from references.estimate import fit


def specs(case,cfg):
    base=[dict(spatial_strata=cfg['spatial_strata'],id=f'{case}-seed{seed}',family='ensemble',seed=seed,grid=cfg['grid'],nodes=cfg['velocity_nodes'],dt=cfg['dt'],amplitude=cfg['amplitude']) for seed in cfg['seeds']]
    seed=cfg['seeds'][0];common=dict(spatial_strata=cfg['spatial_strata'],seed=seed,grid=cfg['grid'],nodes=cfg['velocity_nodes'],dt=cfg['dt'],amplitude=cfg['amplitude'])
    rows=base+[dict(common,id=case+'-mesh',family='mesh',grid=64),dict(common,id=case+'-time-half',family='time-half',dt=cfg['dt']/2),dict(common,id=case+'-velocity',family='velocity',nodes=2*cfg['velocity_nodes']),dict(common,id=case+'-amplitude-half',family='amplitude-half',amplitude=cfg['amplitude']/2),dict(common,id=case+'-noise',family='noise',amplitude=0.)]
    if 'spatial_strata_probe' in cfg:rows.append(dict(common,id=case+'-spatial-strata',family='spatial-strata',spatial_strata=cfg['spatial_strata_probe']))
    return rows


def run_one(case,cfg,spec,reference,deadline,retain_completed=None):
    length=2*np.pi/cfg['k'];x,v,weights,vtable,vweights=loading.load(spec.get('spatial_strata',cfg['spatial_strata']),spec['nodes'],length,spec['amplitude'],cfg['drift'],spec['seed'])
    load=loading.qualification(x,v,weights,vtable,vweights,length,spec['amplitude'],cfg['drift'])
    out=primary.advance(x,v,spec['grid'],length,spec['dt'],cfg['final_time'],weights,deadline)
    # Retain the complete evolved candidate before any estimator can fail.
    if retain_completed is not None:retain_completed(out)
    h=out['history'];alpha=cfg['amplitude'] if spec['family']=='noise' else spec['amplitude'];scale=alpha/(2*cfg['k']);signal=h[:,3]/scale
    ref=np.interp(h[:,1],reference['times'],reference['normalized_field']);window=(h[:,1]>=cfg['fit_window'][0]-1e-12)&(h[:,1]<=cfg['fit_window'][1]+1e-12)
    fitted=None if spec['family']=='noise' else fit(case,h[:,1],signal,cfg['fit_window'],complex(reference['omega_real'],reference['gamma']))
    row={**spec,'case':case,'particles':len(x),'steps':int(out['steps']),'time':float(out['final_time']),'snapshot_times':out['snapshot_times'].tolist(),'load':load,'all_finite':bool(all(np.isfinite(out[k]).all() for k in ['x_history','v_history','electric_history','rho_history','history'])),'maximum_charge_error':float(h[:,8].max()),'maximum_momentum_drift':float(h[:,7].max()),'maximum_resolved_gauss':float(h[:,9].max()),'maximum_energy_drift':float(h[:,6].max()),'maximum_nyquist_charge':float(h[:,10].max()),'minimum_weight':float(weights.min()),'state_clip_count':int(out['state_clip_count']),'retries':int(out['retries']),'fit':fitted,'linear_curve_relative_rms':float(np.linalg.norm(signal[window]-ref[window])/np.linalg.norm(ref[window])) if fitted else None,'normalization_field_amplitude':scale,'noise_mode_rms':float(np.sqrt(np.mean((h[window,2]/scale)**2+signal[window]**2))) if fitted is None else None}
    return row,out,signal


def decisions(case,cfg,rows,series,quality,limits):
    checks=[]
    def add(name,value,bound,passed):checks.append(dict(name=name,value=value,bound=bound,passed=bool(passed)))
    add('independent root and fixed-window Volterra qualified',quality['passed'],True,quality['passed'])
    baseline_count=sum(r['family']!='spatial-strata' for r in rows)
    add('nine fixed full-f calculations',baseline_count,9,baseline_count==9)
    if 'spatial_strata_probe' in cfg:add('ten declared Landau full-f calculations',len(rows),10,len(rows)==10)
    for row in rows:
        key=row['id']+' ';q=row['load']
        add(key+'all fields and histories finite',row['all_finite'],True,row['all_finite'])
        exact=row['time']==cfg['final_time'] and np.allclose(row['snapshot_times'],np.linspace(0,cfg['final_time'],5),atol=1e-12,rtol=0)
        add(key+'fixed time and five snapshots',row['snapshot_times'],np.linspace(0,cfg['final_time'],5).tolist(),exact)
        values=[row[k] for k in ['maximum_charge_error','maximum_momentum_drift','maximum_resolved_gauss','maximum_energy_drift']];bounds=[limits[k] for k in ['charge','momentum','resolved_gauss','energy']]
        add(key+'charge momentum resolvedGauss and energy',values,bounds,all(a<=b for a,b in zip(values,bounds)))
        add(key+'positive full-f weights without repair',[row['minimum_weight'],row['state_clip_count'],row['retries']],'weight>0,clips=retries=0',row['minimum_weight']>0 and row['state_clip_count']==row['retries']==0)
        loadok=q['joint_low_mode_factorization_defect']<=limits['load_joint'] and q['density_mode_defect']<=limits['load_density'] and abs(q['thermal_variance']-1)<=limits['load_moment'] and q['fourth_moment_relative_error']<=limits['load_moment'] and abs(q['mean_velocity'])<=limits['load_moment'] and q['gaussian_characteristic_defect']<=limits['load_characteristic']
        add(key+'joint load and Gaussian quadrature qualified',q,'explicit load limits in acceptance.json',loadok)
        if row['fit']:
            f=row['fit'];add(key+'resolved fixed-window rate fit',[f['gamma'],f['relative_fit_residual']],['physical sign',limits['fit_residual']],f['gamma']*quality['gamma']>0 and f['relative_fit_residual']<=limits['fit_residual'])
    metrics={}
    if len(rows)==9+int('spatial_strata_probe' in cfg):
        base=[r for r in rows if r['family']=='ensemble'];rates=np.array([r['fit']['gamma'] for r in base]);mean=float(rates.mean());se=float(rates.std(ddof=1)/np.sqrt(len(rates)));pole=abs(quality['gamma']);ivp=quality['fixed_window_fit']['gamma'];radius=float(student_t.ppf(.975,len(rates)-1)*se)
        metrics=dict(mean_rate=mean,seed_standard_error=se,conditional_t95_lower=mean-radius,conditional_t95_upper=mean+radius,dielectric_rate=quality['gamma'],volterra_fixed_window_rate=ivp,root_window_relative_bias=quality['root_window_relative_bias'],mean_linear_curve_relative_rms=float(np.mean([r['linear_curve_relative_rms'] for r in base])))
        add('conditional rate precision',3*se,limits['rate_three_se_fraction']*pole,3*se<=limits['rate_three_se_fraction']*pole)
        add('mean rate versus dielectric pole',abs(mean-quality['gamma']),limits['rate_pole_relative_error']*pole+3*se,abs(mean-quality['gamma'])<=limits['rate_pole_relative_error']*pole+3*se)
        add('mean rate versus linear IVP fixed-window estimator',abs(mean-ivp),limits['rate_ivp_relative_error']*pole+3*se,abs(mean-ivp)<=limits['rate_ivp_relative_error']*pole+3*se)
        add('mean field curve versus linear continuum',metrics['mean_linear_curve_relative_rms'],limits['mean_field_relative_rms'],metrics['mean_linear_curve_relative_rms']<=limits['mean_field_relative_rms'])
        first=base[0];noise=next(r for r in rows if r['family']=='noise');ratio=3*noise['noise_mode_rms']/min(r['fit']['minimum_envelope'] for r in base);metrics['three_noise_to_minimum_envelope']=ratio
        add('quiet-equilibrium noise versus fitted envelope',ratio,limits['noise_to_envelope'],ratio<=limits['noise_to_envelope'])
        for family,key in [('mesh','mesh_rate_fraction'),('time-half','time_rate_fraction'),('velocity','velocity_rate_fraction'),('amplitude-half','amplitude_rate_fraction')]:
            row=next(r for r in rows if r['family']==family);gap=abs(row['fit']['gamma']-first['fit']['gamma'])/pole;metrics[family+'_rate_fraction']=gap;add(family+' separate rate sensitivity',gap,limits[key],gap<=limits[key])
        half=next(r for r in rows if r['family']=='amplitude-half');t,y=series[first['id']];th,yh=series[half['id']];mask=(t>=cfg['fit_window'][0]-1e-12)&(t<=cfg['fit_window'][1]+1e-12);gap=float(np.linalg.norm(y[mask]-np.interp(t[mask],th,yh))/np.linalg.norm(y[mask]));metrics['amplitude_scaled_curve_gap']=gap
        add('amplitude-halving scaled field linearity',gap,limits['amplitude_curve_fraction'],gap<=limits['amplitude_curve_fraction'])
        if case=='thermal-landau-damping':
            frequency=np.array([r['fit']['omega'] for r in base]);fm=float(frequency.mean());fs=float(frequency.std(ddof=1)/np.sqrt(len(base)));metrics.update(mean_frequency=fm,frequency_seed_se=fs,dielectric_frequency=quality['omega_real']);gap=abs(fm-quality['omega_real']);bound=limits['frequency_relative_error']*quality['omega_real']+3*fs;add('mean frequency versus dielectric pole',gap,bound,gap<=bound)
        if 'spatial_strata_probe' in cfg:
            probe=next(r for r in rows if r['family']=='spatial-strata');rate_gap=abs(probe['fit']['gamma']-first['fit']['gamma'])/pole;metrics['spatial_strata_rate_fraction']=rate_gap
            add('spatial-strata separate rate sensitivity',rate_gap,limits['mesh_rate_fraction'],rate_gap<=limits['mesh_rate_fraction'])
            tp,yp=series[probe['id']];curve_gap=float(np.linalg.norm(y[mask]-np.interp(t[mask],tp,yp))/np.linalg.norm(y[mask]));metrics['spatial_strata_scaled_curve_gap']=curve_gap
            add('spatial-strata scaled field sensitivity',curve_gap,limits['amplitude_curve_fraction'],curve_gap<=limits['amplitude_curve_fraction'])
    return checks,metrics
