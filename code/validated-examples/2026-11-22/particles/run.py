#!/usr/bin/env python3
"""Run all six small fixed-input particle/transport benchmarks."""
import argparse,csv,hashlib,json,os,time
from pathlib import Path
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
os.environ.setdefault('OMP_NUM_THREADS','1')
import numpy as np
from electrostatics import ewald,spme,nacl_theta_reference
from fmm import fmm,direct
from transport import cold_plasma,dsmc_ensemble,absorption_slab,cic_deposit,cic_gather,poisson


def case(id,checks,metrics,records):
    return dict(id=id,passed=bool(all(checks.values())),checks={k:bool(v) for k,v in checks.items()},metrics=metrics,records=records)


def energy_gradient(function,x,step):
    output=np.zeros_like(x)
    for i in range(len(x)):
        for a in range(3):
            lo=x.copy();hi=x.copy();lo[i,a]-=step;hi[i,a]+=step
            output[i,a]=-(function(hi)-function(lo))/(2*step)
    return output


def ewald_case(c):
    x=np.array(c['positions']);q=np.array(c['charges']);length=c['length'];tol=c['acceptance'];records=[]
    baseline=[]
    for alpha in c['alphas']:
        e,f=ewald(x,q,length,alpha,c['real_images'],c['reciprocal_cutoffs'][-1]);baseline.append((e,f))
        records.append(dict(series='splitting',alpha=alpha,energy=e,max_force=float(abs(f).max())))
    alpha=c['alphas'][1];series=[]
    real_series=[]
    for images in c['real_cutoffs']:
        re,rf=ewald(x,q,length,alpha,images,c['reciprocal_cutoffs'][-1]);real_series.append((re,rf))
        records.append(dict(series='real_cutoff',images=images,energy=re,force_reference_error=float(np.max(abs(rf-baseline[1][1])))))
    for cutoff in c['reciprocal_cutoffs']:
        e,f=ewald(x,q,length,alpha,c['real_images'],cutoff);series.append((e,f))
        records.append(dict(series='reciprocal_cutoff',cutoff=cutoff,energy=e,force_reference_error=float(np.max(abs(f-baseline[1][1])))))
    e,f=baseline[1];fd=energy_gradient(lambda pos:ewald(pos,q,length,alpha,c['real_images'],c['reciprocal_cutoffs'][-1])[0],x,c['finite_difference_step'])
    # Independent scalar NaCl lattice constant (nearest-neighbour distance = 1).
    nacl=np.array([[i,j,k] for i in (0,1) for j in (0,1) for k in (0,1)],float)
    signs=np.array([(-1.)**int(p.sum()) for p in nacl]);nacl_energy,_=ewald(nacl,signs,2.,2.8,3,14)
    measured=-nacl_energy/4;reference,quadrature_error=nacl_theta_reference()
    metrics=dict(madelung_constant=measured,theta_reference=reference,theta_quadrature_error=quadrature_error,real_cutoff_force_last_change=float(np.max(abs(real_series[-1][1]-real_series[-2][1]))),madelung_error=abs(measured-reference),splitting_energy_difference=max(abs(a[0]-e) for a in baseline),splitting_force_difference=max(float(np.max(abs(a[1]-f))) for a in baseline),finite_difference_error=float(np.max(abs(fd-f))),cutoff_force_last_change=float(np.max(abs(series[-1][1]-series[-2][1]))),net_force=float(np.max(abs(f.sum(axis=0)))))
    checks={key:metrics[key]<=value for key,value in tol.items()}
    checks['nonzero_forces']=bool(np.max(abs(f))>.1)
    checks['real_cutoff_refines']=metrics['real_cutoff_force_last_change']<=tol['cutoff_force_last_change']
    checks['theta_reference_error_bound']=quadrature_error<1e-11
    return case('ewald',checks,metrics,records),e,f


def spme_case(c,ec,reference_e,reference_f):
    x=np.array(ec['positions']);q=np.array(ec['charges']);tol=c['acceptance'];records=[];charge_errors=[];outputs={}
    for order in c['orders']:
        for mesh in c['meshes']:
            e,f,charge=spme(x,q,ec['length'],c['alpha'],ec['real_images'],mesh,order);charge_errors.append(charge)
            row=dict(order=order,mesh=mesh,energy=e,energy_error=abs(e-reference_e),force_error=float(np.max(abs(f-reference_f))))
            records.append(row);outputs[order,mesh]=(e,f)
    finest=records[-1];first=next(r for r in records if r['order']==c['orders'][-1]);mesh=c['meshes'][-1];order=c['orders'][-1]
    f=outputs[order,mesh][1]
    fd=energy_gradient(lambda pos:spme(pos,q,ec['length'],c['alpha'],ec['real_images'],mesh,order)[0],x,c['finite_difference_step'])
    metrics=dict(force_error=finest['force_error'],energy_error=finest['energy_error'],finest_to_coarsest_force_ratio=finest['force_error']/first['force_error'],charge_error=max(charge_errors),finite_difference_error=float(np.max(abs(fd-f))),net_force=float(np.max(abs(f.sum(axis=0)))))
    checks={k:metrics[k]<=v for k,v in tol.items()};checks['both_orders_refine']=all(next(r for r in records if r['order']==o and r['mesh']==mesh)['force_error']<next(r for r in records if r['order']==o and r['mesh']==c['meshes'][0])['force_error'] for o in c['orders'])
    return case('spme',checks,metrics,records)


def fmm_case(c):
    rng=np.random.default_rng(c['seed']);n=c['particles'];z=rng.uniform(.01,.99,n)+1j*rng.uniform(.01,.99,n);q=rng.uniform(-1,1,n)
    ref_p,ref_f=direct(z,q);records=[]
    for order in c['orders']:
        p,f,ops=fmm(z,q,order,c['depth']);records.append(dict(order=order,potential_max_error=float(np.max(abs(p-ref_p))),field_max_error=float(np.max(abs(f-ref_f))),**ops))
    final=records[-1];metrics={k:final[k] for k in ['potential_max_error','field_max_error']};metrics['finest_to_coarsest_ratio']=final['field_max_error']/records[0]['field_max_error']
    checks={k:metrics[k]<=v for k,v in c['acceptance'].items()};checks.update(actual_m2l=final['m2l_translations']>0,actual_l2l=final['l2l_translations']>0,near_field_is_subset=final['near_pairs']<final['all_pairs'])
    return case('fmm',checks,metrics,records)


def pic_case(c):
    tol=c['acceptance'];records=[];spatial=[];temporal=[]
    for n in c['spatial_grids']:
        a=cold_plasma(n,c['particles_per_cell'],c['spatial_dt'],c['end_time'],c['amplitude']);spatial.append(a)
        records.append(dict(series='grid',grid=n,dt=a['dt'],particles=a['particles'],error=a['max_mode_error'],energy_defect=a['relative_energy_defect']))
    for dt in c['time_steps']:
        a=cold_plasma(c['time_grid'],c['particles_per_cell'],dt,c['end_time'],c['amplitude']);temporal.append(a)
        records.append(dict(series='time',grid=c['time_grid'],dt=a['dt'],particles=a['particles'],error=a['max_mode_error'],energy_defect=a['relative_energy_defect']))
    length=2*np.pi;x=np.array([.1234]);rho=cic_deposit(x,length,64,length);electric,_=poisson(rho,length)
    self_force=float(abs(cic_gather(electric,x,length)[0]));allruns=spatial+temporal
    metrics=dict(mode_error=spatial[-1]['max_mode_error'],time_mode_error=temporal[-1]['max_mode_error'],charge_error=max(a['charge_error'] for a in allruns),poisson_residual=max(a['poisson_residual'] for a in allruns),self_force=self_force,grid_refinement_ratio=spatial[-1]['max_mode_error']/spatial[0]['max_mode_error'],time_refinement_ratio=temporal[-1]['max_mode_error']/temporal[0]['max_mode_error'])
    checks={k:metrics[k]<=tol[k] for k in ['mode_error','charge_error','poisson_residual','self_force']};checks.update(time_error=metrics['time_mode_error']<=tol['mode_error'],grid_refines=metrics['grid_refinement_ratio']<=tol['refinement_ratio'],time_refines=metrics['time_refinement_ratio']<=tol['refinement_ratio'])
    records += [dict(series='trajectory',**r) for r in temporal[-1]['records']]
    return case('pic',checks,metrics,records)


def dsmc_case(c):
    records=[];allruns=[]
    for particles in c['particle_counts']:
        r=dsmc_ensemble(particles,c['seeds'],c['collision_rounds']);allruns.append(r)
        records.append(dict(particles=particles,variance_error=float(np.max(abs(np.array(r['variance'])-1))),fourth_moment_error=float(np.max(abs(np.array(r['fourth_moment'])-3))),fourth_moment_standard_error=float(max(r['fourth_moment_standard_error'])),energy_cdf_ks=r['energy_cdf_ks'],anisotropy_error=r['anisotropy_max_error']))
    r=allruns[-1];metrics=dict(momentum_error=max(r['momentum_error'] for r in allruns),energy_error=max(r['energy_error'] for r in allruns),variance_error=records[-1]['variance_error'],fourth_moment_error=records[-1]['fourth_moment_error'],energy_cdf_ks=r['energy_cdf_ks'],anisotropy_error=r['anisotropy_max_error'],finest_particle_count=c['particle_counts'][-1],seeds=c['seeds'])
    checks={k:metrics[k]<=v for k,v in c['acceptance'].items()};checks['sampling_uncertainty_decreases']=records[-1]['fourth_moment_standard_error']<records[0]['fourth_moment_standard_error']
    return case('dsmc',checks,metrics,records+[dict(series='anisotropy',**record) for record in r['records']])


def radiation_case(c):
    spatial=[];angular=[];records=[]
    for cells in c['spatial_cells']:
        r=absorption_slab(cells,c['spatial_ordinates'],c['optical_depth'],'upwind');spatial.append(r);records.append(dict(series='spatial',cells=cells,ordinates=c['spatial_ordinates'],**r))
    for ordinates in c['angular_ordinates']:
        r=absorption_slab(8,ordinates,c['optical_depth'],'exponential');angular.append(r);records.append(dict(series='angular',cells=8,ordinates=ordinates,**r))
    metrics=dict(ray_max_error=spatial[-1]['ray_max_error'],spatial_flux_error=spatial[-1]['spatial_flux_error'],angular_flux_error=angular[-1]['angular_flux_error'],balance_error=max(r['balance_error'] for r in spatial),refinement_ratio=spatial[-1]['spatial_flux_error']/spatial[0]['spatial_flux_error'])
    checks={k:metrics[k]<=v for k,v in c['acceptance'].items()};checks['positive_bounded_intensity']=all(0<=r['minimum_intensity']<=r['maximum_intensity']<=1 for r in spatial+angular);checks['angular_refines']=angular[-1]['angular_flux_error']<angular[0]['angular_flux_error']
    return case('radiation-transport',checks,metrics,records)


def validate_config(config):
    if not isinstance(config,dict) or config.get('schema_version')!=1:raise ValueError('Unsupported input schema')
    required={
        'ewald':{'madelung_error','splitting_energy_difference','splitting_force_difference','finite_difference_error','cutoff_force_last_change','net_force'},
        'spme':{'force_error','energy_error','finest_to_coarsest_force_ratio','charge_error','finite_difference_error'},
        'fmm':{'potential_max_error','field_max_error','finest_to_coarsest_ratio'},
        'pic':{'mode_error','charge_error','poisson_residual','self_force','refinement_ratio'},
        'dsmc':{'momentum_error','energy_error','variance_error','fourth_moment_error','energy_cdf_ks','anisotropy_error'},
        'radiation':{'ray_max_error','spatial_flux_error','angular_flux_error','balance_error','refinement_ratio'}}
    def finite(value):
        if isinstance(value,dict):return all(finite(v) for v in value.values())
        if isinstance(value,list):return all(finite(v) for v in value)
        if isinstance(value,(int,float)):return bool(np.isfinite(value))
        return False
    if not finite(config):raise ValueError('Only finite numeric values, arrays and mappings are accepted')
    for name,keys in required.items():
        if not isinstance(config.get(name),dict) or set(config[name].get('acceptance',{}))!=keys:
            raise ValueError('Missing or unknown acceptance conditions for '+name)
        if not all(type(v) in (float,int) and v>0 for v in config[name]['acceptance'].values()):
            raise ValueError('Acceptance values must be positive finite numbers')
    def integers(values,lo,hi):
        if not isinstance(values,list) or not 1<=len(values)<=8 or any(type(v)!=int or not lo<=v<=hi for v in values):
            raise ValueError('Integer refinement array outside this small runner budget')
    e=config['ewald'];integers(e['real_cutoffs'],0,4);integers(e['reciprocal_cutoffs'],1,24)
    if not 2<=len(e['charges'])<=32 or not 0<e['length']<=100 or not 0<e['finite_difference_step']<.01:
        raise ValueError('Ewald input outside this small runner scope')
    if not 1<=len(e['alphas'])<=8 or any(not .1<=a<=20 for a in e['alphas']):raise ValueError('Unsupported alpha sweep')
    if len(e['alphas'])<2 or len(e['reciprocal_cutoffs'])<2 or len(e['real_cutoffs'])<2:raise ValueError('Refinement requires multiple settings')
    p=config['spme'];integers(p['meshes'],16,128)
    if not p['orders'] or any(v not in (4,6,8) for v in p['orders']):raise ValueError('Unsupported spline order')
    f=config['fmm'];integers(f['orders'],1,16)
    if not 2<=f['particles']<=512 or not 1<=f['depth']<=4:raise ValueError('FMM budget exceeded')
    c=config['pic'];integers(c['spatial_grids'],16,512)
    if not 16<=c['time_grid']<=512 or not 2<=c['particles_per_cell']<=16 or not .005<=c['spatial_dt']<=.5 or not 0<c['end_time']<=20:
        raise ValueError('PIC budget exceeded')
    if not 2<=len(c['time_steps'])<=8 or any(not .005<=dt<=.5 for dt in c['time_steps']):raise ValueError('PIC time sweep outside budget')
    d=config['dsmc'];integers(d['particle_counts'],16,8192)
    if not 4<=d['seeds']<=32 or not 1<=d['collision_rounds']<=48:raise ValueError('DSMC budget exceeded')
    r=config['radiation'];integers(r['spatial_cells'],8,1024);integers(r['angular_ordinates'],2,64)
    if not 2<=r['spatial_ordinates']<=64 or not 0<r['optical_depth']<=100:raise ValueError('Absorption input outside scope')


def run(config):
    validate_config(config)
    first,e,f=ewald_case(config['ewald'])
    cases=[first,spme_case(config['spme'],config['ewald'],e,f),fmm_case(config['fmm']),pic_case(config['pic']),dsmc_case(config['dsmc']),radiation_case(config['radiation'])]
    return dict(schema_version=1,passed=all(c['passed'] for c in cases),checks={c['id']:c['passed'] for c in cases},cases=cases,termination='fixed_budget_completed')


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--input',default='inputs.json');parser.add_argument('--output',required=True);args=parser.parse_args()
    path=Path(args.input);output=Path(args.output)
    try:
        config=json.loads(path.read_text());start=time.perf_counter();result=run(config);result['duration_seconds']=time.perf_counter()-start;result['input_sha256']=hashlib.sha256(path.read_bytes()).hexdigest()
        output.mkdir(parents=True,exist_ok=True);(output/'result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2,allow_nan=False)+'\n')
        for c in result['cases']:
            fields=sorted({k for r in c['records'] for k in r})
            with (output/(c['id']+'.csv')).open('w',newline='') as f:
                w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(c['records'])
        print(json.dumps(dict(passed=result['passed'],duration_seconds=result['duration_seconds'],checks=result['checks'])))
        return 0 if result['passed'] else 1
    except (ValueError,KeyError,TypeError,OSError) as exc:
        print(json.dumps(dict(passed=False,error=type(exc).__name__,message=str(exc))));return 2

if __name__=='__main__':raise SystemExit(main())
