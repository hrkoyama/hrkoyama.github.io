#!/usr/bin/env python3
"""Run the preregistered lightweight Double Mach reflection comparison."""
import argparse
import csv
import hashlib
import json
from pathlib import Path
import time
import numpy as np
import dm_solver as solver

CASE='double-mach-reflection'
ROOT=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,v):Path(p).write_text(json.dumps(v,ensure_ascii=False,indent=2,allow_nan=False)+'\n')
def restriction(q,ny):
    if q.shape[0]!=4*q.shape[1] or q.shape[-1]!=4 or q.shape[1]%ny:raise ValueError('Reference is not an integer matching mesh')
    f=q.shape[1]//ny
    return q.reshape(4*ny,f,ny,f,4).mean(axis=(1,3))
def l1(a,b,mask=None):
    if mask is not None:a,b=a[mask],b[mask]
    den=np.sum(abs(b))
    if not den>0:raise ValueError('Empty reference norm')
    return float(np.sum(abs(a-b))/den)
def front(q,x,y,cfg):
    j=int(np.argmin(abs(y-cfg['front_y'])))
    positions=.5*(x[1:]+x[:-1]);window=(positions>=cfg['front_x_window'][0])&(positions<=cfg['front_x_window'][1])
    gradient=np.where(window,-np.diff(q[:,j,0]),-np.inf)
    return float(positions[np.argmax(gradient)]),float(y[j])
def measure(out,qfine,cfg):
    q=out['q'];ny=q.shape[1];qr=restriction(qfine,ny)
    w,wr=solver.primitive(q),solver.primitive(qr)
    x,y=out['x'],out['y'];wall=(x[:,None]>=cfg['wall_jet'][0])&(x[:,None]<=cfg['wall_jet'][1])&(y[None,:]<=cfg['wall_jet'][2])
    shock,row=front(q,x,y,cfg);refshock,unused=front(qr,x,y,cfg)
    residual=out['final_integral']-out['initial_integral']-out['boundary_net_integral']
    scale=np.maximum(1.,np.maximum(abs(out['initial_integral']),abs(out['boundary_net_integral'])))
    return {'n':ny,'ny':ny,'nx':4*ny,'time':out['time'],'steps':out['steps'],
      'density_l1':l1(w[...,0],wr[...,0]),'pressure_l1':l1(w[...,3],wr[...,3]),
      'density_l2':float(np.sqrt(np.sum((w[...,0]-wr[...,0])**2)/np.sum(wr[...,0]**2))),
      'density_linf':float(np.max(abs(w[...,0]-wr[...,0]))/np.max(wr[...,0])),
      'minimum_density_all_stages':out['minimum_density'],'minimum_pressure_all_stages':out['minimum_pressure'],
      'density_min':float(w[...,0].min()),'density_max':float(w[...,0].max()),'pressure_min':float(w[...,3].min()),'pressure_max':float(w[...,3].max()),
      'state_floor_count':out['state_floor_count'],'rejected_steps':out['rejected_steps'],
      'initial_integral':out['initial_integral'].tolist(),'final_integral':out['final_integral'].tolist(),
      'boundary_net_integral':out['boundary_net_integral'].tolist(),'conservation_residual':residual.tolist(),'conservation_relative':(abs(residual)/scale).tolist(),
      'incident_front_x':shock,'reference_incident_front_x':refshock,'front_row_y':row,'incident_front_error_cells':abs(shock-refshock)*ny,
      'wall_jet_density_l1':l1(w[...,0],wr[...,0],wall),'wall_jet_mean_density':float(w[...,0][wall].mean()),
      'wall_jet_reference_mean_density':float(wr[...,0][wall].mean()),'wall_jet_mean_u':float(w[...,1][wall].mean()),
      'wall_jet_reference_mean_u':float(wr[...,1][wall].mean()),'wall_jet_max_u':float(w[...,1][wall].max()),
      'wall_jet_reference_max_u':float(wr[...,1][wall].max())},qr
def decisions(rows,reference,cfg,limits):
    details=[]
    def add(name,value,bound,ok):details.append({'name':name,'value':value,'bound':bound,'passed':bool(ok)})
    add('three final-time refinements complete',[r['ny'] for r in rows],cfg['grids'],[r['ny'] for r in rows]==cfg['grids'])
    for r in rows:
        stem='ny'+str(r['ny'])+': '
        add(stem+'requested time reached',r['time'],cfg['final_time'],r['time']==cfg['final_time'])
        for key in ['minimum_density_all_stages','minimum_pressure_all_stages']:add(stem+key,r[key],0,r[key]>0)
        for key in ['state_floor_count','rejected_steps']:add(stem+key,r[key],0,r[key]==0)
        for i,key in enumerate(['mass','x momentum','y momentum','energy']):add(stem+key+' boundary balance',r['conservation_relative'][i],limits['balance'],r['conservation_relative'][i]<=limits['balance'])
        finite=all(np.isfinite(r[k]) for k in ['density_l2','density_linf','wall_jet_density_l1','wall_jet_mean_density','wall_jet_mean_u','wall_jet_reference_mean_u'])
        add(stem+'unmasked maximum and wall-jet diagnostics retained',finite,True,finite)
    if rows:
        fine=rows[-1]
        for key in ['density_l1','pressure_l1']:add('finest '+key,fine[key],limits['finest_'+key],fine[key]<=limits['finest_'+key])
        add('finest upper incident front difference',fine['incident_front_error_cells'],limits['finest_front_cells'],fine['incident_front_error_cells']<=limits['finest_front_cells'])
        monotone=all(a['density_l1']>b['density_l1'] for a,b in zip(rows[:-1],rows[1:]))
        add('density difference decreases across the fixed grids',monotone,True,monotone)
        order=float(np.log2(rows[-2]['density_l1']/fine['density_l1'])) if len(rows)>1 else -1.
        add('last-pair density difference slope',order,limits['minimum_density_slope'],order>=limits['minimum_density_slope'])
        for key in ['density_l1','pressure_l1']:
            value=reference[key]
            add('reference increment '+key,value,limits['reference_increment_l1'],value<=limits['reference_increment_l1'])
            ratio=value/fine[key]
            add('reference increment / primary finest '+key,ratio,limits['reference_to_primary_ratio'],ratio<=limits['reference_to_primary_ratio'])
    return details
def main():
    p=argparse.ArgumentParser();p.add_argument('--input',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    cfg=json.loads(a.input.read_text())['cases'][CASE];acceptance=json.loads((ROOT/'acceptance.json').read_text())
    if cfg['gamma']!=solver.GAMMA or cfg['final_time']!=.2 or cfg['reference_ny']!=128:raise ValueError('Fixed reference parameters required')
    if a.output.exists() and any(a.output.iterdir()):raise ValueError('Use a new empty output directory')
    a.output.mkdir(parents=True,exist_ok=True);start=time.monotonic()
    refs={};reference_hashes={}
    for n in [64,128]:
        path=ROOT/'references'/('double-mach-ny'+str(n)+'.npz');meta=path.with_suffix('.json');m=json.loads(meta.read_text())
        if sha(path)!=m['npz_sha256']:raise ValueError('Changed stored independent reference')
        with np.load(path,allow_pickle=False) as z:
            if float(z['time'])!=cfg['final_time']:raise ValueError('Reference time mismatch')
            refs[n]=z['q'].copy()
        reference_hashes[str(path.relative_to(ROOT))]=sha(path);reference_hashes[str(meta.relative_to(ROOT))]=sha(meta)
    wr64=solver.primitive(refs[64]);wr128=solver.primitive(restriction(refs[128],64))
    increment={'density_l1':l1(wr64[...,0],wr128[...,0]),'pressure_l1':l1(wr64[...,3],wr128[...,3]),'scope':'Ny64 versus conservatively restricted Ny128 independent numerical references; not an exact error bound.'}
    rows=[];files={};failure=None
    for ny in cfg['grids']:
        try:
            out=solver.solve(ny,cfg['final_time'],cfg['cfl']);record,qr=measure(out,refs[128],cfg)
            field=a.output/('field-ny'+str(ny)+'.npz');history=a.output/('history-ny'+str(ny)+'.json')
            np.savez_compressed(field,q=out['q'],q_reference=qr,x=out['x'],y=out['y'],time=out['time'])
            save(history,out['history']);record.update(field=field.name,history=history.name);rows.append(record)
            files[field.name]=sha(field);files[history.name]=sha(history)
        except Exception as error:
            failure={'ny':ny,'type':type(error).__name__,'message':str(error)}
            if hasattr(error,'failed_state'):
                np.savez_compressed(a.output/'failed-stage.npz',q=error.failed_state);save(a.output/'failed-completed-history.json',error.completed_history);failure['context']=error.failed_context
            break
    checks=decisions(rows,increment,cfg,acceptance['limits']);passed=failure is None and len(rows)==len(cfg['grids']) and all(d['passed'] for d in checks)
    with (a.output/(CASE+'.csv')).open('w',newline='') as h:
        writer=csv.DictWriter(h,fieldnames=['ny','nx','steps','density_l1','pressure_l1','incident_front_error_cells','wall_jet_density_l1'],extrasaction='ignore');writer.writeheader();writer.writerows(rows)
    source={f:sha(ROOT/f) for f in ['dm_solver.py','run.py','inputs.json','acceptance.json','pre-run-contract.json']}
    case={'id':CASE,'passed':passed,'records':rows,'reference_increment':increment,'checks':{d['name']:d['passed'] for d in checks},'check_details':checks,'metrics':{k:v for k,v in rows[-1].items() if isinstance(v,(float,int))} if rows else {},'scope':'Full 2D first-order HLL/Heun Double Mach at T=.2; finite-grid independently written MUSCL reference, broad structures only.'}
    result={'schema_version':1,'passed':passed,'termination':'calculation_failed' if failure else 'fixed_budget_completed','input_sha256':sha(a.input),'checks':{CASE:passed},'cases':[case],'files_sha256':files,'source_sha256':source,'reference_sha256':reference_hashes,'failure':failure,'duration_seconds':time.monotonic()-start}
    save(a.output/'result.json',result);print(json.dumps({'passed':passed,'runs':len(rows),'gates':len(checks),'failed':[d for d in checks if not d['passed']],'failure':failure}),flush=True)
    return 0 if passed else 1
if __name__=='__main__':raise SystemExit(main())
