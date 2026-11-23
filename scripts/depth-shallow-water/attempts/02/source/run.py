#!/usr/bin/env python3
"""Execute eight frozen shallow-water runs and retain arrays and budgets."""
import argparse
import csv
import hashlib
import json
from pathlib import Path
import time
import numpy as np
import shallow_water as sw
from references import analytic as ref

ROOT = Path(__file__).resolve().parent


def sha(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def save(path, value):
    Path(path).write_text(json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False)+'\n')


def check_frozen_sources(root=ROOT):
    root=Path(root); contract=json.loads((root/'pre-run-contract.json').read_text())
    for name, expected in contract['files_sha256'].items():
        if sha(root/name) != expected: raise ValueError('Changed frozen scientific file: '+name)
    return contract


def fixed_runs(cfg):
    return ([dict(id='lake-'+label, case='swashes-topography', family='lake', n=cfg['lake_grid'], surface=eta)
             for label,eta in [('immersed',.5),('emerged',.1)]]+
            [dict(id='subcritical-n'+str(n),case='swashes-topography',family='subcritical',n=n)
             for n in cfg['grids']]+
            [dict(id='ritter-n'+str(n),case='dry-bed-dam-break',family='ritter',n=n)
             for n in cfg['ritter']['grids']])


def setup(run,cfg):
    family=run['family']; n=run['n']; g=cfg['g']
    if family=='ritter':
        c=cfg['ritter']; edges=np.linspace(*c['domain'],n+1); z=np.zeros(n)
        initial=ref.ritter_means(edges,0,g,c['left_depth'],c['dam_position'])
        exact=lambda t:ref.ritter_means(edges,t,g,c['left_depth'],c['dam_position'])
        return edges,z,initial,exact,dict(kind='transmissive'),c['final_time']
    edges=np.linspace(0,25,n+1)
    z=ref.means(edges,ref.bump,breaks=[8.,12.])
    if family=='lake':
        # Exact equilibrium for the represented piecewise-constant cell bed.
        h=np.maximum(run['surface']-z,0.)
        initial=np.column_stack((h,np.zeros(n)))
        exact=lambda t:initial.copy()
        boundary=dict(kind='reflecting')
    else:
        initial=ref.means(edges,lambda x:ref.subcritical(x,g),breaks=[8.,12.])
        exact=lambda t:initial.copy()
        boundary=dict(kind='subcritical',discharge=4.42,downstream_depth=2.)
    return edges,z,initial,exact,boundary,cfg['topography_final_time']


def measure(run,out,edges,z,initial,exact,cfg):
    dx=edges[1]-edges[0]; u=out['state']; reference=exact(out['snapshot_times'][-1])
    errors=dx*np.abs(u-reference).sum(axis=0)
    scale=dx*np.abs(reference).sum(axis=0)
    relative=errors/np.where(scale>0,scale,1.)
    stages=out['stages']; history=out['snapshots']
    row=dict(run,steps=out['steps'],time=float(out['snapshot_times'][-1]),
             depth_l1=float(errors[0]),momentum_l1=float(errors[1]),
             relative_depth_l1=float(relative[0]),relative_momentum_l1=float(relative[1]),
             depth_linf=float(np.max(abs(u[:,0]-reference[:,0]))),
             minimum_depth=float(min(initial[:,0].min(),stages[:,2].min())),
             maximum_depth=float(max(initial[:,0].max(),stages[:,3].max())),
             maximum_velocity=float(stages[:,4].max()),maximum_courant=float(stages[:,5].max()),
             maximum_step_mass_defect=float(abs(stages[:,10]).max()),
             maximum_step_momentum_defect=float(abs(stages[:,11]).max()),
             maximum_total_mass_defect=float(abs(stages[:,12]).max()),
             maximum_total_momentum_defect=float(abs(stages[:,13]).max()),
             mass_change=float(dx*(u[:,0]-initial[:,0]).sum()),
             boundary_mass_change=float(stages[:,6].sum()),
             bed_momentum_impulse=float(stages[:,9].sum()),
             initial_dry_cells=int(np.count_nonzero(initial[:,0]==0)),
             final_dry_cells=int(np.count_nonzero(u[:,0]==0)),
             newly_wet_cells=int(np.count_nonzero((initial[:,0]==0)&(u[:,0]>0))),
             all_saved_values_finite=bool(np.isfinite(history).all() and np.isfinite(stages).all()),
             depth_floor_count=out['depth_floor_count'],state_clip_count=out['state_clip_count'],
             rejected_steps=out['rejected_steps'],retries=out['retries'],
             snapshot_times=out['snapshot_times'].tolist())
    if run['family']=='lake':
        row['maximum_equilibrium_depth_drift']=float(abs(history[:,:,0]-initial[None,:,0]).max())
        row['maximum_equilibrium_discharge']=float(abs(history[:,:,1]).max())
    if run['family']=='ritter':
        threshold=cfg['ritter']['front_depth_threshold']; t=row['time']; c=np.sqrt(cfg['g']*cfg['ritter']['left_depth'])
        centers=.5*(edges[:-1]+edges[1:]); active=np.flatnonzero(u[:,0]>=threshold)
        threshold_ref=cfg['ritter']['dam_position']+2*c*t-3*t*np.sqrt(cfg['g']*threshold)
        row.update(front_depth_threshold=threshold,numerical_threshold_front=float(centers[active[-1]]),
                   analytic_threshold_front=float(threshold_ref),analytic_support_front=float(cfg['ritter']['dam_position']+2*c*t),
                   threshold_front_error=float(abs(centers[active[-1]]-threshold_ref)))
    return row


def decisions(rows,qualification,cfg,limits):
    checks=[]
    def add(name,value,bound,passed): checks.append(dict(name=name,value=value,bound=bound,passed=bool(passed)))
    for row in rows:
        p=row['id']+': '
        for key,limit in [('maximum_step_mass_defect','balance'),('maximum_step_momentum_defect','balance'),
                          ('maximum_total_mass_defect','balance'),('maximum_total_momentum_defect','balance')]:
            add(p+key,row[key],limits[limit],row[key]<=limits[limit])
        add(p+'nonnegative depth',row['minimum_depth'],0,row['minimum_depth']>=0)
        add(p+'finite arrays',row['all_saved_values_finite'],True,row['all_saved_values_finite'])
        add(p+'face CFL',row['maximum_courant'],cfg['cfl']+1e-14,row['maximum_courant']<=cfg['cfl']+1e-14)
        add(p+'no repairs or retries',sum(row[k] for k in ['state_clip_count','depth_floor_count','rejected_steps','retries']),0,
            all(row[k]==0 for k in ['state_clip_count','depth_floor_count','rejected_steps','retries']))
        target=cfg['ritter']['final_time'] if row['family']=='ritter' else cfg['topography_final_time']
        add(p+'five exact output times',row['snapshot_times'],np.linspace(0,target,5).tolist(),row['snapshot_times']==np.linspace(0,target,5).tolist())
        if row['family']=='lake':
            for key in ['maximum_equilibrium_depth_drift','maximum_equilibrium_discharge']:
                add(p+key,row[key],limits['lake_equilibrium'],row[key]<=limits['lake_equilibrium'])
        if row['family']=='ritter':
            add(p+'actual wetting',row['newly_wet_cells'],1,row['newly_wet_cells']>0)
            add(p+'dry cells retained',row['final_dry_cells'],1,row['final_dry_cells']>0)
    for family in ['subcritical','ritter']:
        seq=sorted([r for r in rows if r['family']==family],key=lambda r:r['n'])
        if len(seq)!=3: continue
        for key in ['relative_depth_l1','relative_momentum_l1']:
            bound=limits[family+'_finest_'+key]
            add(family+' finest '+key,seq[-1][key],bound,seq[-1][key]<=bound)
            for j in [1,2]:
                ratio=seq[j][key]/seq[j-1][key]
                add(family+' '+key+' refinement '+str(j),ratio,limits['refinement_ratio'],ratio<=limits['refinement_ratio'])
        if family=='ritter':
            add('finest threshold front error',seq[-1]['threshold_front_error'],limits['front_error'],seq[-1]['threshold_front_error']<=limits['front_error'])
    for name,passed in qualification['checks'].items(): add('reference: '+name,passed,True,passed)
    return checks


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input',type=Path,default=ROOT/'inputs.json')
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args(); contract=check_frozen_sources()
    if sha(args.input)!=contract['files_sha256']['inputs.json']: raise ValueError('Frozen input required')
    cfg=json.loads(args.input.read_text()); limits=json.loads((ROOT/'acceptance.json').read_text())['limits']
    if args.output.exists() and any(args.output.iterdir()): raise ValueError('Use new or empty output directory')
    args.output.mkdir(parents=True,exist_ok=True)
    start=time.monotonic(); rows=[]; files={}; failure=None; qualification=ref.qualify()
    try:
        if not all(qualification['checks'].values()): raise ArithmeticError('Reference qualification failed')
        for run in fixed_runs(cfg):
            edges,z,initial,exact,boundary,t=setup(run,cfg)
            out=sw.solve(initial,z,edges[1]-edges[0],t,boundary,cfg['g'],cfg['cfl'],cfg['max_steps'])
            row=measure(run,out,edges,z,initial,exact,cfg); rows.append(row)
            name='field-'+run['id']+'.npz'
            np.savez_compressed(args.output/name,edges=edges,bed=z,initial=initial,state=out['state'],
                                reference=exact(t),history=out['snapshots'],
                                reference_history=np.array([exact(v) for v in out['snapshot_times']]),
                                snapshot_times=out['snapshot_times'],stage_data=out['stages'],
                                stage_columns=np.array(sw.STAGE_COLUMNS))
            files[name]=sha(args.output/name)
    except Exception as error:
        failure=dict(type=type(error).__name__,message=str(error))
        if hasattr(error,'state'):
            np.savez_compressed(args.output/'failed-state.npz',state=error.state,stage_data=error.history)
            files['failed-state.npz']=sha(args.output/'failed-state.npz')
            failure['context']=error.context
    cases=[]
    for ident in ['swashes-topography','dry-bed-dam-break']:
        selected=[r for r in rows if r['case']==ident]
        detail=decisions(selected,qualification,cfg,limits)
        expected=5 if ident=='swashes-topography' else 3
        detail.append(dict(name='all fixed runs completed',value=len(selected),bound=expected,passed=len(selected)==expected))
        passed=failure is None and all(c['passed'] for c in detail)
        finest=selected[-1] if selected else {}
        case=dict(id=ident,passed=passed,records=selected,check_details=detail,
                  checks={c['name']:c['passed'] for c in detail},
                  metrics={k:v for k,v in finest.items() if isinstance(v,(int,float))},reference_qualification=qualification)
        cases.append(case)
        with (args.output/(ident+'.csv')).open('w',newline='') as f:
            fields=['id','n','steps','relative_depth_l1','relative_momentum_l1','minimum_depth','maximum_total_mass_defect','maximum_total_momentum_defect','newly_wet_cells','final_dry_cells','threshold_front_error']
            writer=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore');writer.writeheader();writer.writerows(selected)
        files[ident+'.csv']=sha(args.output/(ident+'.csv'))
    passed=all(c['passed'] for c in cases)
    result=dict(schema_version=1,passed=passed,checks={c['id']:c['passed'] for c in cases},cases=cases,
                input_sha256=sha(args.input),source_sha256={n:sha(ROOT/n) for n in [*contract['files_sha256'],'pre-run-contract.json']},
                files_sha256=files,duration_seconds=time.monotonic()-start,failure=failure,
                termination='calculation_failed' if failure else 'fixed_budget_completed')
    save(args.output/'result.json',result)
    print(json.dumps(dict(passed=passed,runs=len(rows),gates=sum(len(c['check_details']) for c in cases),failure=failure,
                          failed=[d for c in cases for d in c['check_details'] if not d['passed']])),flush=True)
    return 0 if passed else 1


if __name__=='__main__': raise SystemExit(main())
