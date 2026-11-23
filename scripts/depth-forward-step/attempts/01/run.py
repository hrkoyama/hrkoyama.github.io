#!/usr/bin/env python3
"""Preregistered lightweight Mach-3 forward-step, compared on fluid cells only."""
import argparse
import csv
import hashlib
import json
from pathlib import Path
import time
import numpy as np
import fs_solver as solver

CASE = 'forward-step-m3'
ROOT = Path(__file__).resolve().parent

def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,v): Path(p).write_text(json.dumps(v,ensure_ascii=False,indent=2,allow_nan=False)+'\n')

def restriction(q,ny):
    if q.ndim != 3 or q.shape[0] != 3*q.shape[1] or q.shape[-1] != 4 or q.shape[1] % ny or ny % 5:
        raise ValueError('Reference must restrict by an integer factor to the aligned3:1 mesh')
    f = q.shape[1]//ny
    return q.reshape(3*ny,f,ny,f,4).mean(axis=(1,3))

def l1(a,b,mask):
    a,b = a[mask],b[mask]; den = np.sum(abs(b))
    if not len(a) or not den > 0: raise ValueError('Empty/nonpositive reference norm')
    return float(np.sum(abs(a-b))/den)

def measure(out,qfine,cfg):
    q = out['q']; ny = q.shape[1]; qr = restriction(qfine,ny); fluid = out['fluid']
    w,wr = solver.primitive(q),solver.primitive(qr)
    x,y = out['x'],out['y']; a,b,c,d = cfg['corner_roi']
    corner = fluid & (x[:,None]>=a) & (x[:,None]<=b) & (y[None,:]>=c) & (y[None,:]<=d)
    residual = out['final_integral']-out['initial_integral']-out['boundary_net_integral']
    scale = np.maximum(1.,np.maximum(abs(out['initial_integral']),abs(out['boundary_net_integral'])))
    walls = out['boundary_integrals'][2:]
    entropy = np.log(w[...,3]/w[...,0]**solver.GAMMA)
    return {'n':ny,'ny':ny,'nx':3*ny,'time':out['time'],'steps':out['steps'],
        'fluid_cells':int(fluid.sum()),'fluid_area':float(fluid.sum()/ny**2),
        'density_l1':l1(w[...,0],wr[...,0],fluid),'pressure_l1':l1(w[...,3],wr[...,3],fluid),
        'density_l2':float(np.sqrt(np.sum((w[...,0][fluid]-wr[...,0][fluid])**2)/np.sum(wr[...,0][fluid]**2))),
        'density_linf':float(np.max(abs(w[...,0][fluid]-wr[...,0][fluid]))/np.max(wr[...,0][fluid])),
        'minimum_density_all_stages':out['minimum_density'],'minimum_pressure_all_stages':out['minimum_pressure'],
        'density_min':float(w[...,0][fluid].min()),'density_max':float(w[...,0][fluid].max()),
        'pressure_min':float(w[...,3][fluid].min()),'pressure_max':float(w[...,3][fluid].max()),
        'state_floor_count':out['state_floor_count'],'rejected_steps':out['rejected_steps'],
        'initial_integral':out['initial_integral'].tolist(),'final_integral':out['final_integral'].tolist(),
        'boundary_net_integral':out['boundary_net_integral'].tolist(),
        'boundary_integrals':dict(zip(solver.BOUNDARIES,out['boundary_integrals'].tolist())),
        'conservation_residual':residual.tolist(),'conservation_relative':(abs(residual)/scale).tolist(),
        'wall_mass_energy_max_abs':float(np.max(abs(walls[:,[0,3]]))),
        'corner_density_l1':l1(w[...,0],wr[...,0],corner),
        'corner_density_max':float(w[...,0][corner].max()),'corner_pressure_max':float(w[...,3][corner].max()),
        'corner_entropy_min':float(entropy[corner].min()),'corner_entropy_max':float(entropy[corner].max())},qr

def decisions(rows,reference,cfg,limits):
    details = []
    def add(name,value,bound,ok): details.append({'name':name,'value':value,'bound':bound,'passed':bool(ok)})
    add('three final-time refinements complete',[r['ny'] for r in rows],cfg['grids'],[r['ny'] for r in rows]==cfg['grids'])
    for r in rows:
        stem = 'ny'+str(r['ny'])+': '
        add(stem+'requested time reached',r['time'],cfg['final_time'],r['time']==cfg['final_time'])
        for key in ['minimum_density_all_stages','minimum_pressure_all_stages']: add(stem+key,r[key],0,r[key]>0)
        for key in ['state_floor_count','rejected_steps']: add(stem+key,r[key],0,r[key]==0)
        add(stem+'exact aligned fluid area',r['fluid_area'],2.52,abs(r['fluid_area']-2.52)<=1e-14)
        for i,key in enumerate(['mass','x momentum','y momentum','energy']):
            add(stem+key+' including step-wall boundary balance',r['conservation_relative'][i],limits['balance'],r['conservation_relative'][i]<=limits['balance'])
        add(stem+'stationary-wall integrated mass/energy flux',r['wall_mass_energy_max_abs'],limits['wall_mass_energy_flux'],r['wall_mass_energy_max_abs']<=limits['wall_mass_energy_flux'])
        finite = all(np.isfinite(r[k]) for k in ['density_l2','density_linf','corner_density_l1','corner_pressure_max','corner_entropy_min','corner_entropy_max'])
        add(stem+'unmasked full-field/corner diagnostics retained',finite,True,finite)
    if rows:
        fine = rows[-1]
        for key in ['density_l1','pressure_l1']: add('finest '+key,fine[key],limits['finest_'+key],fine[key]<=limits['finest_'+key])
        monotone = all(a['density_l1']>b['density_l1'] for a,b in zip(rows[:-1],rows[1:]))
        add('density difference decreases across the fixed grids',monotone,True,monotone)
        slope = float(np.log2(rows[-2]['density_l1']/fine['density_l1'])) if len(rows)>1 else -1.
        add('last-pair density difference slope',slope,limits['minimum_density_slope'],slope>=limits['minimum_density_slope'])
        for key in ['density_l1','pressure_l1']:
            value = reference[key]
            add('reference increment '+key,value,limits['reference_increment_l1'],value<=limits['reference_increment_l1'])
            ratio = value/fine[key]
            add('reference increment / primary finest '+key,ratio,limits['reference_to_primary_ratio'],ratio<=limits['reference_to_primary_ratio'])
    return details

def main():
    parser = argparse.ArgumentParser(); parser.add_argument('--input',type=Path,required=True); parser.add_argument('--output',type=Path,required=True); args = parser.parse_args()
    cfg = json.loads(args.input.read_text())['cases'][CASE]; acceptance = json.loads((ROOT/'acceptance.json').read_text())
    if (cfg['gamma'],cfg['mach'],cfg['final_time'],cfg['reference_grids'],cfg['step'],cfg['corner_entropy_fix']) != (1.4,3.,4.,[80,160],[.6,.2],False):
        raise ValueError('Fixed independently referenced geometry/state/time required')
    if args.output.exists() and any(args.output.iterdir()): raise ValueError('Use a new empty output directory')
    args.output.mkdir(parents=True,exist_ok=True); start = time.monotonic()
    refs = {}; hashes = {}
    for n in cfg['reference_grids']:
        path = ROOT/'references'/('forward-step-ny'+str(n)+'.npz'); meta = path.with_suffix('.json'); m = json.loads(meta.read_text())
        if sha(path) != m['npz_sha256'] or m['time'] != cfg['final_time']: raise ValueError('Changed independent reference metadata')
        with np.load(path,allow_pickle=False) as z:
            if z['q'].shape != (3*n,n,4) or float(z['time']) != cfg['final_time']: raise ValueError('Reference geometry/time mismatch')
            unused_x,unused_y,fluid = solver.geometry(n)
            if 'fluid' not in z or not np.array_equal(z['fluid'],fluid): raise ValueError('Reference solid geometry mismatch')
            refs[n] = z['q'].copy()
        hashes[str(path.relative_to(ROOT))] = sha(path); hashes[str(meta.relative_to(ROOT))] = sha(meta)
    ref80 = solver.primitive(refs[80]); ref160 = solver.primitive(restriction(refs[160],80)); unused_x,unused_y,mask80 = solver.geometry(80)
    increment = {'density_l1':l1(ref80[...,0],ref160[...,0],mask80),'pressure_l1':l1(ref80[...,3],ref160[...,3],mask80),
        'scope':'Ny80 versus conservatively restricted Ny160 separately implemented numerical references; not an exact error bound.'}
    rows = []; files = {}; failure = None
    for ny in cfg['grids']:
        try:
            out = solver.solve(ny,cfg['final_time'],cfg['cfl'],cfg['max_steps_per_grid']); record,qr = measure(out,refs[160],cfg)
            field = args.output/('field-ny'+str(ny)+'.npz'); history = args.output/('history-ny'+str(ny)+'.json')
            np.savez_compressed(field,q=out['q'],q_reference=qr,fluid=out['fluid'],x=out['x'],y=out['y'],time=out['time'])
            save(history,out['history']); record.update(field=field.name,history=history.name); rows.append(record)
            files[field.name] = sha(field); files[history.name] = sha(history)
        except Exception as error:
            failure = {'ny':ny,'type':type(error).__name__,'message':str(error)}
            if hasattr(error,'failed_state'):
                np.savez_compressed(args.output/'failed-stage.npz',q=error.failed_state); save(args.output/'failed-completed-history.json',error.completed_history); failure['context'] = error.failed_context
            break
    checks = decisions(rows,increment,cfg,acceptance['limits']); passed = failure is None and len(rows)==len(cfg['grids']) and all(d['passed'] for d in checks)
    with (args.output/(CASE+'.csv')).open('w',newline='') as handle:
        writer = csv.DictWriter(handle,fieldnames=['ny','nx','steps','density_l1','pressure_l1','corner_density_l1','wall_mass_energy_max_abs'],extrasaction='ignore'); writer.writeheader(); writer.writerows(rows)
    source = {f:sha(ROOT/f) for f in ['fs_solver.py','run.py','inputs.json','acceptance.json','pre-run-contract.json']}
    case = {'id':CASE,'passed':passed,'records':rows,'reference_increment':increment,'checks':{d['name']:d['passed'] for d in checks},'check_details':checks,
        'metrics':{k:v for k,v in rows[-1].items() if isinstance(v,(float,int))} if rows else {},
        'scope':'Full2D first-order HLL/Heun Mach3 forward-step atT4, same aligned no-corner-fix variant as a separately implemented MUSCL finite-grid reference.'}
    result = {'schema_version':1,'passed':passed,'termination':'calculation_failed' if failure else 'fixed_budget_completed','input_sha256':sha(args.input),'checks':{CASE:passed},'cases':[case],
        'files_sha256':files,'source_sha256':source,'reference_sha256':hashes,'failure':failure,'duration_seconds':time.monotonic()-start}
    save(args.output/'result.json',result); print(json.dumps({'passed':passed,'runs':len(rows),'gates':len(checks),'failed':[d for d in checks if not d['passed']],'failure':failure}),flush=True)
    return 0 if passed else 1

if __name__ == '__main__': raise SystemExit(main())
