#!/usr/bin/env python3
"""Execute the preregistered spherical Sedov refinement and source-radius probe."""
import argparse
import csv
import hashlib
import json
from pathlib import Path
import time
import numpy as np
import sedov_solver as solver
import reference_sedov as reference
CASE='sedov-blast'

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def save(path,value):path.write_text(json.dumps(value,ensure_ascii=False,indent=2,allow_nan=False)+'\n')
def norm(value,exact,volumes,mask=None):
    if mask is not None:value,exact,volumes=value[mask],exact[mask],volumes[mask]
    denominator=np.dot(abs(exact),volumes)
    if denominator<=0:raise ValueError('Empty reference norm')
    return float(np.dot(abs(value-exact),volumes)/denominator)

def measure(s,cfg):
    q,edges,vol=s['q'],s['edges'],s['volumes'];rho,u,p,_=solver.primitive(q)
    qref,pref=reference.cell_means(edges,s['time'],order=cfg['reference_order'])
    qcheck,pcheck=reference.cell_means(edges,s['time'],order=cfg['reference_check_order'])
    centers=.5*(edges[:-1]+edges[1:]);rs=reference.shock_radius(s['time']);active=centers<=cfg['active_radius_factor']*rs
    interface=.5*(centers[:-1]+centers[1:]);window=(interface>=cfg['shock_search_factors'][0]*rs)&(interface<=cfg['shock_search_factors'][1]*rs)
    gradient=np.where(window,abs(np.diff(p)),-1.)
    shock=float(interface[np.argmax(gradient)])
    residual=s['final_integral']-s['initial_integral']-s['boundary_net_integral']-s['geometric_source_integral']
    scales=np.array([4*np.pi*cfg['radius']**3/3,1.,cfg['energy']])
    return {'n':len(rho),'deposit_radius':s['deposit_radius'],'time':s['time'],'steps':s['steps'],
      'density_l1':norm(rho,qref[:,0],vol),'active_density_l1':norm(rho,qref[:,0],vol,active),
      'active_pressure_l1':norm(p,pref,vol,active),
      'density_l2':float(np.sqrt(np.dot((rho-qref[:,0])**2,vol)/np.dot(qref[:,0]**2,vol))),
      'density_linf':float(np.max(abs(rho-qref[:,0]))/np.max(qref[:,0])),
      'density_min':float(rho.min()),'density_max':float(rho.max()),'pressure_min':float(p.min()),'pressure_max':float(p.max()),'maximum_speed':float(abs(u).max()),'center_density':float(rho[0]),'center_pressure':float(p[0]),'center_reference_density':float(qref[0,0]),'center_reference_pressure':float(pref[0]),
      'shock_radius':shock,'reference_shock_radius':rs,'shock_error_cells':abs(shock-rs)/(edges[1]-edges[0]),
      'minimum_density_all_stages':s['minimum_density'],'minimum_pressure_all_stages':s['minimum_pressure'],
      'minimum_internal_roundoff_units':s['minimum_internal_roundoff_units'],'state_floor_count':s['state_floor_count'],
      'reference_quadrature_density_l1':norm(qref[:,0],qcheck[:,0],vol,active),
      'reference_quadrature_pressure_l1':norm(pref,pcheck,vol,active),
      'initial_integral':s['initial_integral'].tolist(),'final_integral':s['final_integral'].tolist(),
      'boundary_net_integral':s['boundary_net_integral'].tolist(),'geometric_source_integral':s['geometric_source_integral'].tolist(),
      'conservation_residual':residual.tolist(),'conservation_relative':(abs(residual)/scales).tolist(),
      'initial_energy_error':float(abs(s['initial_integral'][2]/cfg['energy']-1))},qref,pref

def decisions(rows,acceptance,cfg,sensitivity):
    output=[];a=acceptance['limits']
    def add(name,value,bound,passed):output.append({'name':name,'value':value,'bound':bound,'passed':bool(passed)})
    add('three fixed-radius refinements complete',[r['n'] for r in rows],cfg['grids'],[r['n'] for r in rows]==cfg['grids'])
    allrows=rows+([sensitivity] if sensitivity else [])
    add('paired smaller-radius run completes',sensitivity is not None,True,sensitivity is not None)
    for j,r in enumerate(allrows):
        stem=('sensitivity' if j==len(rows) else 'n'+str(r['n']))+': '
        add(stem+'strictly positive density all stages',r['minimum_density_all_stages'],0,r['minimum_density_all_stages']>0)
        add(stem+'internal energy within roundoff',r['minimum_internal_roundoff_units'],-64,r['minimum_internal_roundoff_units']>=-64)
        add(stem+'no state floor or repair',r['state_floor_count'],0,r['state_floor_count']==0)
        add(stem+'unit deposited energy',r['initial_energy_error'],a['energy_deposition'],r['initial_energy_error']<=a['energy_deposition'])
        for i,label in enumerate(['mass','radial momentum including geometric source','energy']):
            add(stem+label+' discrete balance',r['conservation_relative'][i],a['balance'],r['conservation_relative'][i]<=a['balance'])
        for key in ['reference_quadrature_density_l1','reference_quadrature_pressure_l1']:
            add(stem+key,r[key],a['reference_quadrature'],r[key]<=a['reference_quadrature'])
        finite=all(np.isfinite(r[k]) for k in ['density_l2','density_linf','center_density','center_pressure','center_reference_density','center_reference_pressure'])
        add(stem+'origin and maximum diagnostics retained',finite,True,finite)
    if rows:
        fine=rows[-1]
        for key,bound in [('active_density_l1','finest_active_density_l1'),('active_pressure_l1','finest_active_pressure_l1'),('shock_error_cells','finest_shock_cells')]:
            add('finest '+key,fine[key],a[bound],fine[key]<=a[bound])
        monotone=all(left['active_density_l1']>right['active_density_l1'] for left,right in zip(rows[:-1],rows[1:]))
        add('fixed-source active density L1 decreases',monotone,True,monotone)
        order=None if len(rows)<2 else float(np.log2(rows[-2]['active_density_l1']/fine['active_density_l1']))
        add('last fixed-source density L1 order',order,a['minimum_last_pair_density_order'],order is not None and order>=a['minimum_last_pair_density_order'])
    if sensitivity:
        finite=all(np.isfinite(sensitivity[k]) for k in ['paired_density_difference','paired_pressure_difference'])
        add('source-radius effects separately retained',finite,True,finite)
    return output

def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--input',type=Path,required=True);parser.add_argument('--output',type=Path,required=True);args=parser.parse_args()
    root=Path(__file__).resolve().parent;cfg=json.loads(args.input.read_text())['cases'][CASE]
    if cfg['gamma']!=solver.GAMMA or cfg['p0']!=0 or cfg['rho0']!=1 or cfg['energy']!=1:raise ValueError('Fixed strong-blast normalization required')
    acceptance=json.loads((root/'acceptance.json').read_text())
    if args.output.exists() and any(args.output.iterdir()):raise ValueError('Use a new empty output directory')
    args.output.mkdir(parents=True,exist_ok=True)
    start=time.monotonic();rows=[];sensitivity=None;files={};failure=None;fine_q=None
    runs=[(n,cfg['deposit_radius']) for n in cfg['grids']]+[(cfg['grids'][-1],cfg['sensitivity_deposit_radius'])]
    for index,(n,deposit) in enumerate(runs):
        suffix='n'+str(n) if index<len(cfg['grids']) else 'radius-probe'
        try:
            s=solver.solve(n,cfg['radius'],cfg['final_time'],cfg['cfl'],deposit,cfg['energy']);s['deposit_radius']=deposit
            record,qref,pref=measure(s,cfg);field=args.output/('field-'+suffix+'.npz');history=args.output/('history-'+suffix+'.json')
            if index==len(cfg['grids'])-1:fine_q=s['q'].copy()
            if index==len(cfg['grids']):
                rho,u,p,_=solver.primitive(s['q']);rf,uf,pf,_=solver.primitive(fine_q);active=.5*(s['edges'][1:]+s['edges'][:-1])<=cfg['active_radius_factor']*reference.shock_radius(s['time'])
                record['paired_density_difference']=norm(rho,rf,s['volumes'],active);record['paired_pressure_difference']=norm(p,pf,s['volumes'],active)
                sensitivity=record
            else:rows.append(record)
            np.savez_compressed(field,q=s['q'],edges=s['edges'],q_reference=qref,pressure_reference=pref,time=s['time'],deposit_radius=deposit)
            save(history,s['history']);record['field']=field.name;record['history']=history.name;files[field.name]=sha(field);files[history.name]=sha(history)
        except Exception as error:
            failure={'n':n,'deposit_radius':deposit,'type':type(error).__name__,'message':str(error)}
            if hasattr(error,'failed_state'):
                np.savez_compressed(args.output/'failed-stage.npz',q=error.failed_state);failure['stage']=error.failed_context;save(args.output/'failed-completed-history.json',error.completed_history)
            break
    checks=decisions(rows,acceptance,cfg,sensitivity);passed=failure is None and all(x['passed'] for x in checks)
    with (args.output/(CASE+'.csv')).open('w',newline='') as handle:
        writer=csv.DictWriter(handle,fieldnames=['n','deposit_radius','steps','active_density_l1','active_pressure_l1','shock_error_cells','center_density','center_pressure'],extrasaction='ignore');writer.writeheader();writer.writerows(rows+([sensitivity] if sensitivity else []))
    names=['sedov_solver.py','reference_sedov.py','run.py','inputs.json','acceptance.json','pre-run-contract.json']
    source={name:sha(root/name) for name in names}
    case={'id':CASE,'passed':passed,'records':rows,'source_radius_sensitivity':sensitivity,'checks':{r['name']:r['passed'] for r in checks},'check_details':checks,'metrics':{k:v for k,v in rows[-1].items() if isinstance(v,(int,float))} if rows else {},'scope':'One-dimensional spherical radial Euler; fixed finite deposition sphere; not a two-dimensional Cartesian blast.'}
    result={'schema_version':1,'passed':passed,'termination':'calculation_failed' if failure else 'fixed_budget_completed','cases':[case],'checks':{CASE:passed},'input_sha256':sha(args.input),'source_sha256':source,'files_sha256':files,'reference_summary':reference.reference_metadata(),'failure':failure,'duration_seconds':time.monotonic()-start}
    save(args.output/'result.json',result);print(json.dumps({'passed':passed,'runs':len(rows)+(sensitivity is not None),'gates':len(checks),'failed':[r for r in checks if not r['passed']],'failure':failure}),flush=True)
    return 0 if passed else 1
if __name__=='__main__':raise SystemExit(main())
