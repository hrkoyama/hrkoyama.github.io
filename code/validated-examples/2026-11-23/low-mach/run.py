#!/usr/bin/env python3
"""Compare ordinary and spatially preconditioned Roe on fixed low-Mach vortices."""
import argparse,csv,hashlib,json,time
from pathlib import Path
import numpy as np
import lm_solver as solver
from linear_stability import stability_scan
from references import analytic_vortex as analytic

ROOT=Path(__file__).resolve().parent
CASE='low-mach-vortex'
U=np.array([1.,.5]);SPEED=float(np.linalg.norm(U));DYNAMIC_PRESSURE=SPEED*SPEED
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def save(path,data):Path(path).write_text(json.dumps(data,ensure_ascii=False,indent=2,allow_nan=False)+'\n')


def diagnostics(out,qr,mach,n,cfg,initial_residual):
    q=out['q'];w=solver.primitive(q);wr=solver.primitive(qr);rho=w[...,0];rr=wr[...,0]
    dv=w[...,1:3]-wr[...,1:3];pert=wr[...,1:3]-U
    norm=np.linalg.norm(pert,axis=-1);den=norm.sum()
    if not den>0:raise ValueError('Nonzero vortex perturbation required')
    velocity_error=np.linalg.norm(dv,axis=-1);pressure_error=abs(w[...,3]-wr[...,3])
    x=analytic.coordinates(n);xx,yy=np.meshgrid(x-U[0]*cfg['final_time'],x-U[1]*cfg['final_time'],indexing='ij')
    core=xx*xx+yy*yy<=cfg['core_radius']**2
    if not np.any(core):raise ValueError('Empty fixed vortex core')
    final=out['final_integral'];initial=out['initial_integral'];balance=abs(final-initial)/np.maximum(1,abs(initial))
    ke=.5*np.sum(rho*np.sum((w[...,1:3]-U)**2,axis=-1))*(cfg['length']/n)**2
    kr=.5*np.sum(rr*np.sum(pert**2,axis=-1))*(cfg['length']/n)**2
    sound=np.sqrt(solver.GAMMA*w[...,3]/rho);h=cfg['length']/n
    acoustic=cfg['cfl']*h/(np.max(abs(w[...,1])+sound)+np.max(abs(w[...,2])+sound))
    convective=cfg['cfl']*h/(np.max(abs(w[...,1]))+np.max(abs(w[...,2])))
    return {'n':n,'mach_far':mach,'time':out['time'],'steps':out['steps'],
        'velocity_relative_l1':float(velocity_error.sum()/den),
        'velocity_relative_l2':float(np.sqrt(np.sum(velocity_error**2)/np.sum(norm**2))),
        'pressure_dynamic_l1':float(pressure_error.mean()/DYNAMIC_PRESSURE),
        'core_pressure_dynamic_l1':float(pressure_error[core].mean()/DYNAMIC_PRESSURE),
        'pressure_dynamic_linf':float(pressure_error.max()/DYNAMIC_PRESSURE),
        'density_l1':float(abs(rho-rr).mean()),
        'perturbation_kinetic_energy':float(ke),'reference_perturbation_kinetic_energy':float(kr),
        'perturbation_kinetic_energy_ratio':float(ke/kr),
        'maximum_local_mach':float(np.max(np.linalg.norm(w[...,1:3],axis=-1)/sound)),
        'acoustic_dt_diagnostic':float(acoustic),'convective_dt_diagnostic':float(convective),
        'convective_to_acoustic_dt_ratio':float(convective/acoustic),
        'minimum_density_all_stages':out['minimum_density_all_stages'],'minimum_pressure_all_stages':out['minimum_pressure_all_stages'],
        'minimum_dt':out['minimum_dt'],'maximum_dt':out['maximum_dt'],
        'state_floor_count':out['state_floor_count'],'rejected_steps':out['rejected_steps'],
        'initial_integral':initial.tolist(),'final_integral':final.tolist(),'conservation_relative':balance.tolist(),
        'initial_translation_corrected_residual_l1':initial_residual,
        'scope':'Velocity normalized by analytic vortex perturbation, pressure by rho_infinity*|U_infinity|^2, not large thermodynamic background.'}


def decisions(rows,scan,reference,cfg,limits):
    checks=[]
    def add(name,value,bound,passed):checks.append({'name':name,'value':value,'bound':bound,'passed':bool(passed)})
    expected=[(m,v,n) for m in cfg['mach_far_values'] for v in cfg['variants'] for n in cfg['grids']]
    add('all twelve fixed nonlinear runs completed',[(r['mach_far'],r['variant'],r['n']) for r in rows],expected,[(r['mach_far'],r['variant'],r['n']) for r in rows]==expected)
    for r in rows:
        key=f"M{r['mach_far']}/{r['variant']}/N{r['n']}: "
        add(key+'final time',r['time'],cfg['final_time'],r['time']==cfg['final_time'])
        for k in ['minimum_density_all_stages','minimum_pressure_all_stages']:add(key+k,r[k],0,r[k]>0)
        for k in ['state_floor_count','rejected_steps']:add(key+k,r[k],0,r[k]==0)
        for k,label in enumerate(['mass','x momentum','y momentum','total energy']):add(key+label+' periodic balance',r['conservation_relative'][k],limits['balance'],r['conservation_relative'][k]<=limits['balance'])
        fields=['velocity_relative_l1','pressure_dynamic_l1','core_pressure_dynamic_l1','perturbation_kinetic_energy_ratio','maximum_local_mach','convective_to_acoustic_dt_ratio']
        finite=all(np.isfinite(r[k]) for k in fields)
        add(key+'finite physical diagnostics',finite,True,finite)
    for mach in cfg['mach_far_values']:
        pc=[r for r in rows if r['mach_far']==mach and r['variant']=='miczek'];plain=[r for r in rows if r['mach_far']==mach and r['variant']=='roe']
        if len(pc)!=3 or len(plain)!=3:continue
        stem='M'+str(mach)+': ';f=pc[-1]
        decreasing=all(a['velocity_relative_l1']>b['velocity_relative_l1'] for a,b in zip(pc,pc[1:]))
        add(stem+'preconditioned velocity error decreases across grids',decreasing,True,decreasing)
        for key,bound in [('velocity_relative_l1','finest_velocity_relative_l1'),('pressure_dynamic_l1','finest_pressure_dynamic_l1'),('core_pressure_dynamic_l1','finest_core_pressure_dynamic_l1')]:add(stem+'finest preconditioned '+key,f[key],limits[bound],f[key]<=limits[bound])
        ratio=f['velocity_relative_l1']/plain[-1]['velocity_relative_l1']
        add(stem+'finest preconditioned / Roe velocity error',ratio,limits['finest_preconditioned_to_Roe_velocity_error'],ratio<=limits['finest_preconditioned_to_Roe_velocity_error'])
    for r in scan:
        stem=f"Fourier M{r['mach_far']}/{r['variant']}: "
        for key,bound in [('maximum_SSPRK3_spectral_radius','fourier_spectral_radius'),('maximum_energy_scaled_power_norm','energy_scaled_power_norm')]:add(stem+key,r[key],limits[bound],r[key]<=limits[bound])
    fe=next(r['maximum_forward_Euler_spectral_radius'] for r in scan if r['mach_far']==.01 and r['variant']=='miczek')
    add('forward Euler counterexample at the chosen acoustic step',fe,1+limits['forward_Euler_instability_excess'],fe>1+limits['forward_Euler_instability_excess'])
    for key,bound in [('maximum_point_Euler_residual','analytic_point_Euler_residual'),('maximum_quadrature_dynamic_difference','cell_quadrature_dynamic_max'),('periodic_seam_velocity_bound','periodic_seam_velocity_bound')]:add('analytic qualification: '+key,reference[key],limits[bound],reference[key]<=limits[bound])
    return checks


def main():
    p=argparse.ArgumentParser();p.add_argument('--input',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    cfg=json.loads(a.input.read_text())['cases'][CASE];limits=json.loads((ROOT/'acceptance.json').read_text())['limits']
    if (cfg['grids'],cfg['mach_far_values'],cfg['variants'],cfg['final_time'],cfg['length'],cfg['beta'],cfg['gamma'],cfg['background_velocity'],cfg['time_integrator'])!=([16,32,64],[.1,.01],['roe','miczek'],.1,20.,3.,1.4,[1.,.5],'SSPRK33'):raise ValueError('Use the fixed qualified input family')
    if a.output.exists() and any(a.output.iterdir()):raise ValueError('Use a new empty output directory')
    a.output.mkdir(parents=True,exist_ok=True);start=time.monotonic();files={};cache={};quad=0.;point=0.;rows=[];failure=None
    for mach in cfg['mach_far_values']:
        pts=np.array([-.91,-.31,.27,.73,1.31]);res,scale=analytic.analytic_euler_residual(pts,pts[::-1],.037,mach);point=max(point,float(np.max(abs(res)/scale)))
        for n in cfg['grids']:
            q0=analytic.cell_means(n,0,mach,cfg['quadrature_order']);qt=analytic.cell_means(n,cfg['final_time'],mach,cfg['quadrature_order'])
            for t,q8 in [(0,q0),(cfg['final_time'],qt)]:
                q16=analytic.cell_means(n,t,mach,cfg['quadrature_check_order'])
                scales=np.array([1.,SPEED,SPEED,DYNAMIC_PRESSURE]);quad=max(quad,float(np.max(abs(q8-q16)/scales)),float(np.max(abs(solver.primitive(q8)[...,3]-solver.primitive(q16)[...,3]))/DYNAMIC_PRESSURE))
            cache[mach,n]=(q0,qt,analytic.cell_means_time_derivative(n,0,mach,cfg['quadrature_order']))
    reference={'maximum_point_Euler_residual':point,'maximum_quadrature_dynamic_difference':quad,
        'periodic_seam_velocity_bound':float(analytic.BETA/(2*np.pi)*cfg['length']*np.exp(.5*(1-(cfg['length']/2-SPEED*cfg['final_time'])**2))),
        'scope':'Whole-plane analytic solution in a finite periodic box; Gauss8 means qualified against Gauss16, not closed-form exact cell averages.'}
    scan=stability_scan(tuple(cfg['mach_far_values']),cfg['cfl'],cfg['fourier_wavenumbers_per_axis'],tuple(cfg['fourier_power_indices']))
    for mach in cfg['mach_far_values']:
        for variant in cfg['variants']:
            for n in cfg['grids']:
                try:
                    q0,qr,qdot=cache[mach,n];res=solver.rhs(q0,cfg['length'],variant,mach)-qdot
                    residual=[float(v) for v in np.mean(abs(res),axis=(0,1))/np.array([1.,SPEED,SPEED,DYNAMIC_PRESSURE])]
                    out=solver.solve(q0,cfg['final_time'],cfg['cfl'],cfg['length'],variant,mach,cfg['max_steps_per_run'])
                    row=diagnostics(out,qr,mach,n,cfg,residual);row['variant']=variant
                    stem=f"M{mach:g}-{variant}-n{n}";field=a.output/('field-'+stem+'.npz');hist=a.output/('history-'+stem+'.json')
                    np.savez_compressed(field,q=out['q'],q_reference=qr,x=analytic.coordinates(n),y=analytic.coordinates(n),time=out['time'])
                    save(hist,out['history']);row.update(field=field.name,history=hist.name);rows.append(row);files[field.name]=sha(field);files[hist.name]=sha(hist)
                except Exception as error:
                    failure={'mach':mach,'variant':variant,'n':n,'type':type(error).__name__,'message':str(error)}
                    if hasattr(error,'failed_state'):
                        np.savez_compressed(a.output/'failed-stage.npz',q=error.failed_state,**getattr(error,'failed_faces',{}));save(a.output/'failed-completed-history.json',error.completed_history);failure['context']=error.failed_context
                    break
            if failure:break
        if failure:break
    checks=decisions(rows,scan,reference,cfg,limits);passed=failure is None and len(rows)==12 and all(c['passed'] for c in checks)
    with (a.output/(CASE+'.csv')).open('w',newline='') as handle:
        writer=csv.DictWriter(handle,fieldnames=['mach_far','variant','n','steps','velocity_relative_l1','pressure_dynamic_l1','core_pressure_dynamic_l1','perturbation_kinetic_energy_ratio'],extrasaction='ignore');writer.writeheader();writer.writerows(rows)
    sources={name:sha(ROOT/name) for name in ['lm_solver.py','linear_stability.py','run.py','inputs.json','acceptance.json','pre-run-contract.json','references/analytic_vortex.py','references/miczek_matrix.py']}
    case={'id':CASE,'passed':passed,'records':rows,'metrics':{'fixed_runs_completed':len(rows),'maximum_quadrature_dynamic_difference':quad,'maximum_point_Euler_residual':point},'checks':{c['name']:c['passed'] for c in checks},'check_details':checks,'linear_stability':scan,'reference_qualification':reference}
    result={'schema_version':1,'passed':passed,'termination':'calculation_failed' if failure else 'fixed_budget_completed','input_sha256':sha(a.input),'checks':{CASE:passed},'cases':[case],'files_sha256':files,'source_sha256':sources,'duration_seconds':time.monotonic()-start,'failure':failure}
    save(a.output/'result.json',result);print(json.dumps({'passed':passed,'runs':len(rows),'gates':len(checks),'failed':[c for c in checks if not c['passed']],'failure':failure}),flush=True)
    return 0 if passed else 1


if __name__=='__main__':raise SystemExit(main())
