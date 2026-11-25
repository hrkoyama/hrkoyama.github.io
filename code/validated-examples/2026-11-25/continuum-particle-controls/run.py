"""Fixed-input continuum and particle verification recipes.

Packaging interface: run.py --input inputs.json --output fresh-results-directory
"""
import argparse,hashlib,json,traceback,csv,time
from pathlib import Path
import numpy as np
from ale_piston import run_piston,primitive
from sphere import transport,zonal_balance,analytic_zonal_force
from gsph import evolve,sod_initial,smooth_initial,particle_rhs,ContractFailure,pair_swap_residual
from reference_riemann import RiemannSolution
from failure_support import persist_failure
RUN_DEADLINE=None


def scalar(value):
    if isinstance(value,np.ndarray):return value.tolist()
    if isinstance(value,np.generic):return value.item()
    raise TypeError(type(value).__name__)


def dump(path,value):path.write_text(json.dumps(value,default=scalar,ensure_ascii=False,indent=2,allow_nan=False)+'\n')


def atomic_record(ident,metrics,checks,records):
    assert metrics and checks and records
    assert all(type(v) is bool for v in checks.values())
    return dict(id=ident,passed=all(checks.values()),metrics=metrics,checks=checks,records=records)


def continuum_cases(config,accept,out):
    cases=config['groups']['continuum-moving']['cases'];results=[]
    cfg=next(x for x in cases if x['id']=='saltzman-ale-piston');limits=accept[cfg['id']]
    rows=[]
    for nx,ny in cfg['grids']:
        result=run_piston(nx,ny,cfg['final_time'],cfg['gamma'],cfg['rho0'],cfg['specific_internal_energy0'],cfg['CFL'],deadline=RUN_DEADLINE)
        np.savez_compressed(out/('piston-%d-%d.npz'%(nx,ny)),**{k:result[k] for k in ['points','cells','areas','conserved','exact_conserved_average','history']})
        computed,exact=result['conserved'],result['exact_conserved_average'];area=result['areas'];rho,vel,pressure=primitive(computed,cfg['gamma']);ref=result['reference'];error=float(np.sum(area*np.abs(rho-exact[:,0]))/np.sum(area*np.abs(exact[:,0])))
        center=np.mean(result['points'][result['cells']],axis=1);plateau=(center[:,0]>.63)&(center[:,0]<ref['shock_position']-.04)
        if not np.any(plateau):raise ContractFailure('No independently specified plateau sample',{'grid':[nx,ny]})
        mid=(1+ref['rho1'])/2;shock=float(np.max(center[rho>mid,0])) if np.any(rho>mid) else -1.
        defect=result['conservation_defect'];rows.append(dict(grid=[nx,ny],density_error=error,shock_error=abs(shock-ref['shock_position']),plateau_density_error=float(np.max(np.abs(rho[plateau]/ref['rho1']-1))),plateau_pressure_error=float(np.max(np.abs(pressure[plateau]/ref['p1']-1))),max_transverse=float(np.max(np.abs(vel[:,1]))),mass_defect=abs(float(defect[0]))/max(1e-14,abs(float(result['start_integrals'][0]))),momentum_defect=float(np.max(np.abs(defect[1:3])))/max(1e-14,float(np.max(np.abs(result['boundary_integral'][1:3]))),float(result['start_integrals'][0])),energy_defect=abs(float(defect[3]))/max(1e-14,abs(float(result['start_integrals'][3]))+abs(float(result['boundary_integral'][3]))),GCL=result['max_GCL_error'],steps=result['steps'],minimum_density=float(np.min(rho)),minimum_pressure=float(np.min(pressure))))
    fine=rows[-1];checks={key:bool(value) for key,value in dict(positive=all(r['minimum_density']>0 and r['minimum_pressure']>0 for r in rows),conservation=all(r['mass_defect']<=limits['mass_relative_defect_max'] and r['momentum_defect']<=limits['momentum_boundary_impulse_relative_defect_max'] and r['energy_defect']<=limits['energy_boundary_work_relative_defect_max'] for r in rows),GCL=all(r['GCL']<=limits['local_GCL_absolute_max'] for r in rows),density=fine['density_error']<=limits['finest_density_volume_L1_relative_max'],refinement=fine['density_error']<=limits['fine_over_coarse_density_error_max']*rows[0]['density_error'],shock=fine['shock_error']<=limits['finest_shock_position_absolute_max'],plateau=fine['plateau_density_error']<=limits['plateau_density_pressure_relative_max'] and fine['plateau_pressure_error']<=limits['plateau_density_pressure_relative_max'],transverse=fine['max_transverse']<=limits['max_transverse_velocity']).items()};results.append(atomic_record(cfg['id'],{'finest':fine},checks,rows))
    cfg=next(x for x in cases if x['id']=='williamson-sphere-transport');limits=accept[cfg['id']];rows=[]
    for tilt in cfg['tilt_angles']:
        by_grid=[]
        for (nx,ny),steps in zip(cfg['grids'],cfg['steps']):
            result=transport(nx,ny,steps,tilt,cfg['period'],cfg['bell_radius'],deadline=RUN_DEADLINE);tag='sphere-%d-%d-%.6f'%(nx,ny,tilt);np.savez_compressed(out/(tag+'.npz'),**{k:result[k] for k in ['lon','lat','xyz','areas','initial','final','exact']});by_grid.append(dict(grid=[nx,ny],tilt=tilt,relative_L1=result['relative_L1'],mass_drift=result['mass_drift'],analytic_bell_mass=result['analytic_bell_mass'],initial_quadrature_mass_error=result['initial_quadrature_mass_error'],initial_quadrature_mass_relative_error=result['initial_quadrature_mass_relative_error'],minimum=float(np.min(result['final'])),maximum=float(np.max(result['final'])),weight_sum_error=abs(float(np.sum(result['areas']))-4*np.pi)))
        rows.extend(by_grid)
    checks=dict(error=all(rows[i]['relative_L1']<=limits['return_relative_L1_fine_max'] for i in [1,3]),refinement=all(rows[i+1]['relative_L1']<=limits['fine_over_coarse_relative_L1_max']*rows[i]['relative_L1'] for i in [0,2]),mass=all(abs(rows[i]['mass_drift'])<=limits['mass_drift_fraction_fine_max'] for i in [1,3]),bounds=all(r['minimum']>=limits['minimum_q'] and r['maximum']<=limits['maximum_q'] for r in rows),sphere_area=all(r['weight_sum_error']<=limits['weights_sum_error_max'] for r in rows));results.append(atomic_record(cfg['id'],{'fine_L1':[rows[1]['relative_L1'],rows[3]['relative_L1']]},checks,rows))
    cfg=next(x for x in cases if x['id']=='sphere-zonal-balance');limits=accept[cfg['id']];rows=[]
    for n in cfg['grids']:
        result=zonal_balance(n,cfg['final_time'],.1,cfg['a'],cfg['g'],cfg['Omega'],cfg['u0'],cfg['h0'],deadline=RUN_DEADLINE);np.savez_compressed(out/('zonal-%d.npz'%n),**{k:result[k] for k in ['phi','weights','initial','final','initial_rhs']});rows.append(dict(grid=n,h_error=float(np.max(np.abs(result['final'][0]-result['initial'][0]))/cfg['h0']),initial_balance_residual=float(np.max(np.abs(result['initial_rhs'][2]))),analytic_force_residual=float(np.max(np.abs(analytic_zonal_force(result['phi'],cfg['a'],cfg['g'],cfg['Omega'],cfg['u0'])))),mass_defect=abs(result['mass_defect']),minimum_h=float(np.min(result['final'][0])),steps=result['steps']))
    checks=dict(analytic_balance=all(r['analytic_force_residual']<=limits['analytic_force_balance_abs_max'] for r in rows),balance_order=rows[0]['initial_balance_residual']>=limits['finite_difference_balance_refinement_min']*rows[-1]['initial_balance_residual'],height=rows[-1]['h_error']<=limits['finest_h_relative_error_max'],refinement=rows[-1]['h_error']<=limits['fine_over_coarse_h_error_max']*rows[0]['h_error'],mass=all(r['mass_defect']<=limits['mass_relative_defect_max'] for r in rows),positive=all(r['minimum_h']>0 for r in rows));results.append(atomic_record(cfg['id'],{'finest':rows[-1]},checks,rows));return results


def particle_cases(config,accept,out):
    block=config['groups']['particle-gsph'];common=block['common'];results=[]
    # These fixed educational options are not a general arbitrary-parameter API.
    for key,value in [('gamma',1.4),('eta',1.2),('C_smooth',2.),('h_fixed_point_rtol',1e-10),('h_fixed_point_maxiter',100),('CFL',.15),('Riemann_max_pressure_bracket_doublings',32),('Riemann_pressure_bisection_iterations',64)]:
        if common[key]!=value:raise ValueError('Unsupported unreviewed fixed option '+key)
    cfg=next(x for x in block['cases'] if x['id']=='gsph-sod');limits=accept[cfg['id']];oracle=RiemannSolution('euler',cfg['left'],cfg['right'],common['gamma']);rows=[]
    for mode in ['gsph','sph']:
        for count in cfg['right_particle_counts']:
            state,mass,h,initial=sod_initial(count);result=evolve(state,mass,h,2.,cfg['final_time'],mode=mode,cfl=common['CFL'],deadline=RUN_DEADLINE);x=result['state'][0]-1;mask=(x>=cfg['measurement_window'][0])&(x<=cfg['measurement_window'][1]);reference=oracle.point(x,cfg['final_time'],origin=0.);refp=(common['gamma']-1)*(reference[:,2]-.5*reference[:,1]**2/reference[:,0]);weight=mass/result['rho'];rho_error=float(np.sum(weight[mask]*np.abs(result['rho'][mask]-reference[mask,0]))/np.sum(weight[mask]*reference[mask,0]));p_error=float(np.sum(weight[mask]*np.abs(result['pressure'][mask]-refp[mask]))/np.sum(weight[mask]*refp[mask]));shock_ref=max(w['speeds'][0] for w in oracle.waves if w['kind']=='shock')*cfg['final_time'];shock_points=(x>0)&(x<.4)&(result['pressure']>.5*(oracle.star+cfg['right'][2]));shock=float(np.max(x[shock_points])) if np.any(shock_points) else -1.;np.savez_compressed(out/('sod-%s-%d.npz'%(mode,count)),x=x,mass=mass,density=result['rho'],pressure=result['pressure'],velocity=result['state'][1],h=result['h'],reference=reference,history=result['history'],initial_x=state[0]-1,initial_kernel_density=initial['kernel_density'],initial_model_density=initial['model_density']);rows.append(dict(method=mode,right_particles=count,rho_error=rho_error,pressure_error=p_error,shock_error=abs(shock-shock_ref),defect=result['defect'],h_change=float(np.max(np.abs(result['h']/h-1))),steps=result['steps'],h_residual=float(np.max(result['history'][:,6])),Riemann_residual=float(np.max(result['history'][:,7]))))
    gsph=[r for r in rows if r['method']=='gsph'];fine=gsph[-1];swap_force,swap_power=pair_swap_residual();checks=dict(pair_swap_force=swap_force<=limits['pair_swap_force_and_energy_abs_max'],pair_swap_energy=swap_power<=limits['pair_swap_force_and_energy_abs_max'],conservation=all(abs(float(r['defect'][0]))<=limits['closed_periodic_mass_relative_max'] and abs(float(r['defect'][1]))<=limits['closed_periodic_momentum_abs_max'] and abs(float(r['defect'][2]))<=limits['closed_periodic_total_energy_relative_max'] for r in rows),rho=fine['rho_error']<=limits['fine_particle_weighted_rho_L1_relative_max'],pressure=fine['pressure_error']<=limits['fine_particle_weighted_pressure_L1_relative_max'],refinement=fine['rho_error']<=limits['fine_over_coarse_rho_error_max']*gsph[0]['rho_error'],shock=fine['shock_error']<=limits['shock_position_abs_max'],h_solve=all(r['h_residual']<=limits['h_fixed_point_relative_max'] for r in gsph),Riemann=all(r['Riemann_residual']<=limits['Riemann_wave_residual_abs_max'] for r in gsph),adaptive_h=fine['h_change']>1e-4);results.append(atomic_record(cfg['id'],{'finest_GSPH':fine,'pair_swap_force_residual':swap_force,'pair_swap_energy_residual':swap_power,'oracle_pressure_root':oracle.star,'oracle_root_diagnostics':oracle.diagnostics},checks,rows))
    cfg=next(x for x in block['cases'] if x['id']=='sph-pressure-acoustics');limits=accept[cfg['id']];rows=[]
    for mode in ['gsph','sph']:
        for acoustic in [False,True]:
            for jitter in [False,True]:
                for count in cfg['particles']:
                    state,mass,h,initial=smooth_initial(count,acoustic,jitter);_,start=particle_rhs(state,mass,h,1.,mode=mode);T=cfg['final_time_acoustic'] if acoustic else cfg['final_time_pressure'];result=evolve(state,mass,h,1.,T,mode=mode,deadline=RUN_DEADLINE);x=result['state'][0];weight=mass/result['rho'];amplitude=2*np.sum(weight*(result['rho']-1)*np.exp(-2j*np.pi*x))/np.sum(weight);expected=-1j*cfg['acoustic_amplitude']*np.exp(-2j*np.pi*T);phase=abs(float(np.angle(amplitude/expected))) if acoustic else 0.;amp_error=abs(abs(amplitude)/cfg['acoustic_amplitude']-1) if acoustic else 0.;tag='smooth-%s-%s-%s-%d'%(mode,'wave' if acoustic else 'pressure','jitter' if jitter else 'regular',count);np.savez_compressed(out/(tag+'.npz'),x=x,density=result['rho'],pressure=result['pressure'],velocity=result['state'][1],h=result['h'],initial_x=state[0],initial_density=initial['kernel_density'],initial_model_density=initial['model_density'],history=result['history']);rows.append(dict(method=mode,acoustic=acoustic,jitter=jitter,particles=count,initial_force=float(np.max(np.abs(particle_rhs(state,mass,h,1.,mode=mode)[0][1]))),initial_kernel_error=float(np.max(np.abs(initial['kernel_density']-initial['model_density']))),velocity_max=float(np.max(np.abs(result['state'][1]))),phase_error=phase,amplitude_relative_error=amp_error,defect=result['defect'],steps=result['steps']))
    fine=[r for r in rows if r['particles']==max(cfg['particles'])];checks=dict(regular_static_force=all(r['initial_force']<=limits['uniform_regular_force_abs_max'] for r in rows if not r['acoustic'] and not r['jitter']),jittered_static_velocity=all(r['velocity_max']<=limits['jittered_uniform_pressure_velocity_max'] for r in rows if not r['acoustic'] and r['jitter']),acoustic_phase=all(r['phase_error']<=limits['acoustic_relative_phase_error_fine_max'] for r in fine if r['acoustic']),acoustic_amplitude=all(r['amplitude_relative_error']<=limits['acoustic_relative_amplitude_error_fine_max'] for r in fine if r['acoustic']),conservation=all(np.max(np.abs(r['defect']))<=1e-10 for r in rows));results.append(atomic_record(cfg['id'],{'profiles':len(rows),'linearization_remainder_scale':cfg['acoustic_amplitude']**2},checks,rows));return results


def main():
    global RUN_DEADLINE
    p=argparse.ArgumentParser();p.add_argument('--input',type=Path,required=True);p.add_argument('--output',type=Path,required=True);args=p.parse_args();data=args.input.read_bytes();config=json.loads(data);accept=json.loads(args.input.with_name('acceptance.json').read_text());out=args.output;out.mkdir(parents=True,exist_ok=False);RUN_DEADLINE=time.monotonic()+config['cooperative_budget_seconds'];result={'schema_version':1,'input_sha256':hashlib.sha256(data).hexdigest(),'passed':False,'checks':{},'cases':[],'termination':'RUNNING','scientific_scope':'Five fixed new cases for four extension/implementation candidates; fivecommonmaintenancecandidates are separate metadata work.'}
    try:
        result['cases']=continuum_cases(config,accept,out);dump(out/'partial-result.json',result);result['cases'].extend(particle_cases(config,accept,out));assert len(result['cases'])==5 and len({c['id'] for c in result['cases']})==5;result['checks']={c['id']:c['passed'] for c in result['cases']};result['passed']=all(result['checks'].values());result['termination']='completed_fixed_protocol'
    except Exception as error:
        result['termination']='failed_without_repair';result['failure']=persist_failure(out,error,traceback.format_exc());result['checks']={'completed':False}
    with (out/'records.csv').open('w',newline='') as stream:
        writer=csv.writer(stream);writer.writerow(['case','record','metric','value'])
        for case in result['cases']:
            for index,record in enumerate(case['records']):
                for key,value in record.items():
                    if isinstance(value,(int,float,np.number)) and not isinstance(value,(bool,np.bool_)):
                        if not np.isfinite(value):raise FloatingPointError('Nonfinite actualCSVmetric')
                        writer.writerow([case['id'],index,key,float(value)])
    dump(out/'result.json',result);raise SystemExit(0 if result['passed'] else 1)


if __name__=='__main__':main()
