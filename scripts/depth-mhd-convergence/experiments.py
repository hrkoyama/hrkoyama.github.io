"""Predeclared norm, temporal and independent-solver checks for matched MHD."""
from pathlib import Path
import hashlib
import json
import math
import numpy as np
from scipy.integrate import solve_ivp
from scipy.linalg import expm
from solver import (Budget,common_divergence,divergence,exact_smooth,initial_q,
                    pack,primitive,rhs,solve,unpack)

HERE=Path(__file__).resolve().parent
REFERENCE_MANIFEST_SHA256='bacb294db8b40e50aa814dc6704efebb9eecdbe295e3b957600a9a9d677c928c'
REFERENCE_DATASETS={
    '128':(128,.3,'athena-ot-128.npz','athinput-ot-128-cfl03'),
    '256':(256,.15,'athena-ot-256-cfl015.npz','athinput-ot-256-cfl015'),
    '512':(512,.15,'athena-ot-512-cfl015.npz','athinput-ot-512-cfl015'),
    '512-cfl03':(512,.3,'athena-ot-512-cfl03.npz','athinput-ot-512-cfl03')}
REQUIRED_REFERENCE_FILES={
    'ATHENA-LICENSE.txt','athena-ot-original-provenance.json','athena-ot-new-provenance.json',
    *[v[2] for v in REFERENCE_DATASETS.values()],*[v[3] for v in REFERENCE_DATASETS.values()]}
FIELD_NAMES=['density','momentum_x','momentum_y','total_energy','magnetic_x','magnetic_y']


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def scales(initial):
    return np.maximum(np.sqrt(np.mean(initial[...,:6]**2,axis=(0,1))),1e-12)


def norms(q,target,scale):
    error=q[...,:6]-target[...,:6]
    return {'scaled_l2':float(np.sqrt(np.mean((error/scale)**2))),
            'l1':dict(zip(FIELD_NAMES,map(float,np.mean(abs(error),axis=(0,1))))),
            'l2':dict(zip(FIELD_NAMES,map(float,np.sqrt(np.mean(error*error,axis=(0,1)))))),
            'linf':dict(zip(FIELD_NAMES,map(float,np.max(abs(error),axis=(0,1)))))}


def order(errors):
    if any(not math.isfinite(v) or v<=0 for v in errors):
        raise ValueError('Order estimation requires finite strictly positive resolved errors')
    return [float(np.log2(a/b)) for a,b in zip(errors,errors[1:])]


def conservation(result):
    hist=result['history'];mass=hist[:,1];energy=hist[:,2]
    return {'mass_relative_drift':float(np.max(abs(mass-mass[0]))/abs(mass[0])),
            'energy_relative_drift':float(np.max(abs(energy-energy[0]))/abs(energy[0]))}


def temporal_reference(case,n,cfg,model,time_cfg,budget):
    """An independent time integrator, explicitly sharing the spatial RHS."""
    records=[];answers={}
    for method in ('ct','glm'):
        state=pack(initial_q(case,n,cfg),method);shape=state.shape;outputs=[]
        for tol,atol,divisor in zip(time_cfg['rtol'],time_cfg['atol'],time_cfg['maximum_step_divisors']):
            budget.check()
            def fun(t,flat):return rhs(flat.reshape(shape),method,model,budget).ravel()
            ref=solve_ivp(fun,(0.,cfg['time']),state.ravel(),method='DOP853',rtol=tol,atol=atol,max_step=cfg['time']/divisor)
            if not ref.success or not np.all(np.isfinite(ref.y[:,-1])) or ref.t[-1]!=cfg['time']:
                raise RuntimeError('Independent DOP853 time reference did not reach final time')
            answer=unpack(ref.y[:,-1].reshape(shape),method);primitive(answer,model['gamma']);outputs.append(answer)
            records.append({'method':method,'grid':n,'rtol':tol,'atol':atol,'maximum_step':cfg['time']/divisor,'nfev':int(ref.nfev),'accepted_nodes':len(ref.t),'success':True})
        answers[method]=outputs[-1]
        records[-1]['two_reference_scaled_l2_difference']=norms(outputs[-2],outputs[-1],scales(initial_q(case,n,cfg)))['scaled_l2']
    return answers,records


def temporal_study(case,cfg,model,time_cfg,budget):
    n=cfg['time_grid'];reference,ref_records=temporal_reference(case,n,cfg,model,time_cfg,budget)
    records=[];checks={};t=cfg['acceptance'];saved={}
    scale=scales(initial_q(case,n,cfg))
    for method in ('ct','glm'):
        values=[]
        for count in cfg['time_steps']:
            result=solve(case,n,count,method,cfg,model,budget)
            error=norms(result['q'],reference[method],scale)
            records.append({'method':method,'n':n,'steps':count,'dt':result['dt'],'cfl_sum':result['cfl_sum'],**error})
            values.append(error['scaled_l2'])
        observed=order(values)
        for index,p in enumerate(observed):records[-len(values)+index+1]['order_from_previous']=p
        delta=next(r['two_reference_scaled_l2_difference'] for r in ref_records if r['method']==method and 'two_reference_scaled_l2_difference' in r)
        ratio=delta/values[-1]
        checks[method+'_temporal_order']=min(observed[-2:])>=t['minimum_temporal_order']
        checks[method+'_temporal_error']=values[-1]<=t['finest_time_scaled_l2']
        checks[method+'_temporal_reference_resolved']=ratio<=t['reference_time_ratio']
        saved[method]={'orders':observed,'finest_scaled_l2':values[-1],'reference_scaled_l2_difference':delta,'reference_to_primary_ratio':ratio}
    return records,ref_records,checks,saved


def common_record(result,method,cfg,model):
    q=result['q'];bscale=float(np.sqrt(np.mean(q[...,4]**2+q[...,5]**2)))
    return {'method':method,'n':result['n'],'steps':result['steps'],'dt':result['dt'],'cfl_sum':result['cfl_sum'],
            'maximum_psi_linf':result['maximum_psi_linf'],'minimum_density':result['min_density'],'minimum_derived_pressure':result['min_pressure'],
            'native_divergence_linf':result['maximum_native_divergence_linf'],
            'common_centered_divergence_linf':result['maximum_common_divergence_linf'],
            'common_centered_divergence_final_l2':float(np.sqrt(np.mean(common_divergence(q)**2))),
            'common_divergence_final_dimensionless':float(np.sqrt(np.mean(common_divergence(q)**2)))/(result['n']*bscale),
            **conservation(result)}


def load_reference():
    directory=HERE/'references';manifest_path=directory/'reference-manifest.json'
    if sha(manifest_path)!=REFERENCE_MANIFEST_SHA256:raise ValueError('Independent reference manifest SHA mismatch')
    manifest=json.loads(manifest_path.read_text())
    if type(manifest.get('schema_version')) is not int or manifest.get('schema_version')!=1 or manifest.get('actually_executed') is not True or manifest.get('athena_commit')!='1395e2f543f4368d448cb1a2cf92ba1f910e3416':
        raise ValueError('Independent Athena reference provenance is missing')
    if set(manifest.get('files',{}))!=REQUIRED_REFERENCE_FILES:raise ValueError('Incomplete required reference file bindings')
    if manifest.get('provenance_files')!=['athena-ot-original-provenance.json','athena-ot-new-provenance.json']:raise ValueError('Incomplete reference provenance bindings')
    for name,digest in manifest['files'].items():
        if Path(name).is_absolute() or '..' in Path(name).parts or sha(directory/name)!=digest:
            raise ValueError('Independent reference file SHA mismatch: '+name)
    expected=set(REFERENCE_DATASETS)
    if set(manifest['datasets'])!=expected:raise ValueError('Incomplete independent spatial/time reference datasets')
    arrays={}
    for name,entry in manifest['datasets'].items():
        n,cfl,datafile,inputfile=REFERENCE_DATASETS[name]
        if (entry.get('n'),entry.get('cfl'),entry.get('file'),entry.get('input'))!=(n,cfl,datafile,inputfile):raise ValueError('Independent reference dataset identity mismatch')
        if name=='128' and entry.get('historical_only') is not True:raise ValueError('Historical reference must remain labelled')
        path=directory/entry['file']
        if entry['file'] not in manifest['files']:raise ValueError('Reference dataset not bound by manifest')
        with np.load(path,allow_pickle=False) as data:a=np.asarray(data['table'])
        n=entry['n']
        if a.shape!=(n*n,12) or not np.all(np.isfinite(a)) or n not in (128,256,512):
            raise ValueError('Invalid Athena reference array')
        if entry['time']!=.05:raise ValueError('Independent reference time mismatch')
        arrays[name]=a
    return arrays,manifest


def restrict(table,n,columns=(4,9,10)):
    fine=math.isqrt(len(table))
    if fine*fine!=len(table) or fine%n:raise ValueError('Reference block averaging requires integer grid ratio')
    r=fine//n
    # Official Athena table x1 is fastest. Atlas arrays index x first.
    return np.stack([table[:,c].reshape(fine,fine).T.reshape(n,r,n,r).mean(axis=(1,3)) for c in columns],axis=-1)


def ot_errors(q,target):
    rho=float(np.mean(abs(q[...,0]-target[...,0])))
    magnetic=float(np.mean(abs(q[...,4:6]-target[...,1:3])))
    rho_rel=rho/float(np.mean(abs(target[...,0])))
    mag_rel=magnetic/float(np.mean(abs(target[...,1:3])))
    return {'density_l1':rho,'magnetic_l1':magnetic,'density_relative_l1':rho_rel,'magnetic_relative_l1':mag_rel,'combined_relative_l1':.5*(rho_rel+mag_rel)}


def experiment(case,config,budget):
    cfg=config[case];model=config['model'];t=cfg['acceptance'];records=[];checks={};fields={};space_summary={};reference_records=[]
    q0=initial_q(case,cfg['grids'][0],cfg)
    initial_difference=float(np.max(abs(unpack(pack(q0,'ct'),'ct')-unpack(pack(q0,'glm'),'glm'))))
    checks['identical_initial_cell_states']=initial_difference<=t['initial_cell_state_difference']
    references=None
    if case=='ot':
        references,manifest=load_reference()
        for lo,hi in zip(cfg['reference_grids'],cfg['reference_grids'][1:]):
            a=restrict(references[str(lo)],lo);b=restrict(references[str(hi)],lo)
            delta=np.mean(abs(a-b),axis=(0,1))
            reference_records.append({'coarse_n':lo,'fine_n':hi,'density_increment_l1':float(delta[0]),'magnetic_increment_l1':float(np.mean(delta[1:])),'bx_increment_l1':float(delta[1]),'by_increment_l1':float(delta[2]),'coarse_cfl':.3 if lo==128 else .15,'fine_cfl':.15,'historical_mixed_cfl_only':lo==128})
        a=restrict(references['512'],512);b=restrict(references['512-cfl03'],512)
        d=np.mean(abs(a-b),axis=(0,1));ref_time=max(float(d[0]),float(np.mean(d[1:])))
        checks['independent_reference_density_refinement']=reference_records[-1]['density_increment_l1']<=t['independent_density_increment_l1']
        checks['independent_reference_magnetic_refinement']=reference_records[-1]['magnetic_increment_l1']<=t['independent_magnetic_increment_l1']
        checks['independent_reference_time_refinement']=ref_time<=t['independent_time_increment_l1']
        reference_records.append({'n':512,'cfl_coarse':.3,'cfl_fine':.15,'density_increment_l1':float(d[0]),'magnetic_increment_l1':float(np.mean(d[1:])),'bx_increment_l1':float(d[1]),'by_increment_l1':float(d[2]),'maximum_density_magnetic_l1_increment':ref_time})
    for method in ('ct','glm'):
        errors=[];method_results=[]
        for n in cfg['grids']:
            result=solve(case,n,cfg['spatial_steps'],method,cfg,model,budget);record=common_record(result,method,cfg,model)
            if case=='smooth':
                target=exact_smooth(n,cfg['time'],cfg);error=norms(result['q'],target,scales(result['initial']));criterion=error['scaled_l2']
            else:
                target=restrict(references['512'],n);error=ot_errors(result['q'],target);criterion=error['combined_relative_l1']
            record.update(error);records.append(record);errors.append(criterion);method_results.append(result)
            if method=='ct':checks['ct_native_constraint_n'+str(n)]=result['maximum_native_divergence_linf']<=t['ct_native_divergence_linf']
        orders=order(errors)
        for index,p in enumerate(orders):records[-len(errors)+index+1]['spatial_order_from_previous']=p
        fine=method_results[-1];n=cfg['grids'][-1]
        doubled=solve(case,n,2*cfg['spatial_steps'],method,cfg,model,budget)
        if case=='smooth':
            contamination=norms(fine['q'],doubled['q'],scales(fine['initial']))['scaled_l2']/errors[-1]
            checks[method+'_spatial_order']=min(orders)>=t['minimum_spatial_order']
            checks[method+'_continuum_error']=errors[-1]<=t['finest_scaled_l2']
            checks[method+'_common_divergence_bounded']=records[-1]['common_divergence_final_dimensionless']<=t['finest_common_divergence_dimensionless']
        else:
            comparison=np.stack((doubled['q'][...,0],doubled['q'][...,4],doubled['q'][...,5]),axis=-1)
            contamination=ot_errors(fine['q'],comparison)['combined_relative_l1']/errors[-1]
            checks[method+'_spatial_refinement']=errors[-1]/errors[-2]<=t['last_spatial_error_ratio']
            checks[method+'_density_error']=records[-1]['density_relative_l1']<=t['finest_density_relative_l1']
            checks[method+'_magnetic_error']=records[-1]['magnetic_relative_l1']<=t['finest_magnetic_relative_l1']
            rho_ratio=reference_records[1]['density_increment_l1']/records[-1]['density_l1']
            mag_ratio=reference_records[1]['magnetic_increment_l1']/records[-1]['magnetic_l1']
            time_rho_ratio=reference_records[2]['density_increment_l1']/records[-1]['density_l1']
            time_mag_ratio=reference_records[2]['magnetic_increment_l1']/records[-1]['magnetic_l1']
            records[-1].update({'reference_spatial_density_to_primary_ratio':rho_ratio,'reference_spatial_magnetic_to_primary_ratio':mag_ratio,'reference_time_density_to_primary_ratio':time_rho_ratio,'reference_time_magnetic_to_primary_ratio':time_mag_ratio})
            checks[method+'_independent_reference_resolved']=max(rho_ratio,mag_ratio,time_rho_ratio,time_mag_ratio)<=t['independent_reference_to_primary_ratio']
        checks[method+'_time_contamination_bounded']=contamination<=t['time_contamination_ratio']
        checks[method+'_positive_states']=all(x['min_density']>0 and x['min_pressure']>0 for x in method_results+[doubled])
        checks[method+'_conservative_mass_energy']=all(max(conservation(x).values())<=t['relative_conservation_drift'] for x in method_results+[doubled])
        space_summary[method]={'orders':orders,'finest_error':errors[-1],'time_contamination_ratio':contamination}
        fields[method+'_q']=fine['q'];fields[method+'_history']=fine['history']
        fields[method+'_native_divergence']=divergence(fine['state'],method)
        fields[method+'_common_divergence']=common_divergence(fine['q'])
    fields['reference']=exact_smooth(cfg['grids'][-1],cfg['time'],cfg) if case=='smooth' else restrict(references['512'],cfg['grids'][-1])
    temporal,temporal_refs,time_checks,time_summary=temporal_study(case,cfg,model,config['time_reference'],budget);checks.update(time_checks)
    metrics={'initial_cell_state_linf_difference':initial_difference}
    for method in ('ct','glm'):
        metrics[method+'_finest_spatial_error']=space_summary[method]['finest_error']
        metrics[method+'_minimum_spatial_order']=min(space_summary[method]['orders'])
        metrics[method+'_time_contamination_ratio']=space_summary[method]['time_contamination_ratio']
        metrics[method+'_finest_temporal_scaled_l2']=time_summary[method]['finest_scaled_l2']
        metrics[method+'_minimum_temporal_order']=min(time_summary[method]['orders'][-2:])
        metrics[method+'_time_reference_to_primary_ratio']=time_summary[method]['reference_to_primary_ratio']
    return {'id':cfg['case_id'],'passed':all(checks.values()),'checks':checks,'metrics':metrics,'records':records,'temporal_records':temporal,'temporal_reference_records':temporal_refs,'independent_reference_records':reference_records},fields


def longitudinal_reference(n,steps,end,amplitude,alpha,kappa):
    """Independently constructed 2x2 Fourier symbol and FE matrix power."""
    theta=2*np.pi/n;kd=n*np.sin(theta);nu=alpha*n*(np.cos(theta)-1)
    discrete=np.array([[nu,-1j*kd],[-1j*alpha*alpha*kd,nu-kappa]],dtype=complex)
    continuous=np.array([[0.,-1j*2*np.pi],[-1j*alpha*alpha*2*np.pi,-kappa]],dtype=complex)
    initial=np.array([amplitude*np.cos(np.pi/n),0.],dtype=complex)
    fe=np.linalg.matrix_power(np.eye(2)+end/steps*discrete,steps)@initial
    semi=expm(end*discrete)@initial;cont=expm(end*continuous)@initial
    return fe,semi,cont,nu,kd


def constraint_control(config,budget):
    cfg=config['constraint_control'];model=config['model'];n=cfg['n'];count=cfg['steps'];alpha=model['wave_speed_bound'];t=cfg['acceptance']
    records=[];checks={};fields={};initial=initial_q('constraint',n,cfg)
    common_initial=common_divergence(initial);initial_norm=float(np.sqrt(np.mean(common_initial**2)))
    ct=solve('constraint',n,count,'ct',cfg,model,budget)
    initial_face=np.zeros((n,n,6));initial_face[...,:4]=initial[...,:4]
    initial_face[...,4]=cfg['amplitude']*np.cos(2*np.pi*(np.arange(n)[:,None]+1)/n)
    native_initial=divergence(initial_face,'ct')
    ct_change=float(np.max(abs(divergence(ct['state'],'ct')-native_initial)))
    ct_common_change=float(np.max(abs(common_divergence(ct['q'])-common_initial)))
    checks['ct_preserves_initial_constraint_defect']=ct_change<=t['ct_native_divergence_change_linf']
    checks['ct_does_not_clean_common_initial_defect']=ct_common_change<=t['ct_common_divergence_change_linf']
    checks['ct_initial_constraint_is_deliberately_nonzero']=float(np.max(abs(native_initial)))>1e-3
    records.append({'method':'ct','cleaning_rate':None,'initial_native_divergence_linf':float(np.max(abs(native_initial))),'native_divergence_change_linf':ct_change,'common_divergence_change_linf':ct_common_change,**conservation(ct)})
    fields['ct_q']=ct['q'];fields['ct_history']=ct['history'];fields['initial_q']=initial
    energies={};x=2*np.pi*(np.arange(n)+.5)/n
    for kappa in (model['cleaning_rate'],cfg['comparison_cleaning_rate']):
        local={**model,'cleaning_rate':kappa};result=solve('constraint',n,count,'glm',cfg,local,budget)
        fe,semi,cont,nu,kd=longitudinal_reference(n,count,cfg['time'],cfg['amplitude'],alpha,kappa)
        target=np.real(np.exp(1j*x)[:,None]*fe[None,:])
        measured=np.stack((result['q'][...,4],result['q'][...,6]),axis=-1)
        expected=np.broadcast_to(target[:,None,:],measured.shape)
        error=float(np.max(abs(measured-expected)))
        divergence_ratio=float(np.sqrt(np.mean(common_divergence(result['q'])**2)))/initial_norm
        energy=float(np.mean(result['q'][...,4]**2+result['q'][...,6]**2/alpha**2))
        expected_energy=float((abs(fe[0])**2+abs(fe[1])**2/alpha**2)/2)
        energies[kappa]=energy;label='damped' if kappa else 'undamped'
        checks[label+'_independent_discrete_fourier_agreement']=error<=t['discrete_fourier_reference_linf']
        checks[label+'_positive_states']=result['min_density']>0 and result['min_pressure']>0
        checks[label+'_conservative_mass_energy']=max(conservation(result).values())<=t['relative_conservation_drift']
        checks[label+'_psi_is_activated']=result['maximum_psi_linf']>=t['glm_psi_activation_minimum']
        if kappa:checks['glm_final_B_divergence_reduced']=divergence_ratio<=t['glm_final_divergence_ratio']
        records.append({'method':'glm','cleaning_rate':kappa,'n':n,'steps':count,'dt':result['dt'],'cfl_sum':result['cfl_sum'],'fourier_FE_reference_linf':error,'final_common_divergence_ratio':divergence_ratio,'maximum_psi_linf':result['maximum_psi_linf'],'B_psi_wave_energy':energy,'reference_wave_energy':expected_energy,'LLF_diffusion_eigenvalue':float(nu),'centered_derivative_wavenumber':float(kd),'FE_B_amplitude_real':float(fe[0].real),'FE_psi_amplitude_imaginary':float(fe[1].imag),'semidiscrete_B_amplitude_real':float(semi[0].real),'continuous_B_amplitude_real':float(cont[0].real),'minimum_density':result['min_density'],'minimum_derived_pressure':result['min_pressure'],**conservation(result)})
        fields[label+'_q']=result['q'];fields[label+'_history']=result['history'];fields[label+'_reference_B_psi']=expected
    wave_ratio=energies[model['cleaning_rate']]/energies[cfg['comparison_cleaning_rate']]
    checks['physical_damping_separated_from_phase_and_LLF_viscosity']=wave_ratio<=t['damped_to_undamped_wave_energy_ratio']
    checks['ct_positive_states']=ct['min_density']>0 and ct['min_pressure']>0
    checks['ct_conservative_mass_energy']=max(conservation(ct).values())<=t['relative_conservation_drift']
    metrics={'damped_to_undamped_B_psi_wave_energy_ratio':wave_ratio,'ct_native_divergence_linf_change':ct_change,'ct_common_divergence_linf_change':ct_common_change,'initial_common_divergence_l2':initial_norm,'initial_cell_state_difference':float(np.max(abs(unpack(initial_face,'ct')-initial)))}
    checks['matched_initial_cell_states']=metrics['initial_cell_state_difference']<=2e-14
    return {'id':cfg['case_id'],'passed':all(checks.values()),'checks':checks,'metrics':metrics,'records':records},fields
