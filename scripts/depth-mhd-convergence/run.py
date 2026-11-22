"""Run the three bounded, fixed-input matched CT/GLM convergence experiments."""
import argparse
import csv
import hashlib
import json
import math
from pathlib import Path
import time
import numpy as np
from experiments import experiment,constraint_control
from solver import Budget


def validate(config):
    if type(config.get('schema_version')) is not int or config.get('schema_version')!=1:raise ValueError('Unknown input schema')
    model=config['model']
    for key in ('gamma','wave_speed_bound','cleaning_rate','cfl_sum_maximum','maximum_seconds'):
        v=model[key]
        if isinstance(v,bool) or not isinstance(v,(int,float)) or not math.isfinite(v) or v<=0:raise ValueError('Finite positive '+key+' required')
    if model['gamma']!=5/3 or model['cfl_sum_maximum']>.4 or model['maximum_seconds']>110:raise ValueError('Fixed model/budget guard exceeded')
    for case in ('smooth','ot'):
        c=config[case]
        if c['time']!=(.1 if case=='smooth' else .05):raise ValueError('Fixed comparison time required')
        if c['grids']!=[16,32,64] or c['time_steps']!=[16,32,64,128]:raise ValueError('Fixed bounded refinement sequence required')
        if c['time_grid']!=(8 if case=='smooth' else 16):raise ValueError('Fixed temporal grid required')
        steps=c['spatial_steps']
        if isinstance(steps,bool) or not isinstance(steps,int) or not 1<=steps<=2048:raise ValueError('Bounded positive spatial step count required')
        for n,count in [(64,steps),(c['time_grid'],min(c['time_steps']))]:
            if 2*model['wave_speed_bound']*n*c['time']/count>model['cfl_sum_maximum']:raise ValueError('Two-dimensional CFL guard failed')
        if not all(not isinstance(x,bool) and isinstance(x,(int,float)) and math.isfinite(x) and x>0 for x in c['acceptance'].values()):raise ValueError('Finite positive acceptance required')
    if config['ot']['reference_grids']!=[128,256,512]:raise ValueError('Fixed independent reference grids required')
    control=config['constraint_control']
    if control['n']!=32 or control['steps']!=128 or control['time']!=.1 or control['comparison_cleaning_rate']!=0.:raise ValueError('Fixed bounded constraint control required')
    if not all(not isinstance(v,bool) and isinstance(v,(int,float)) and math.isfinite(v) and v>0 for v in control['acceptance'].values()):raise ValueError('Finite positive diagnostic criteria required')
    for key in ('amplitude','density','pressure'):
        if isinstance(control[key],bool) or not isinstance(control[key],(int,float)) or not math.isfinite(control[key]) or control[key]<=0:raise ValueError('Invalid diagnostic physical state')
    c=config['smooth']
    if any(isinstance(c[k],bool) or not math.isfinite(c[k]) or c[k]<=0 for k in ('amplitude','base_pressure','density')):raise ValueError('Invalid smooth equilibrium')
    if len(c['velocity'])!=2 or not all(math.isfinite(v) for v in c['velocity']):raise ValueError('Finite two-dimensional velocity required')
    r=config['time_reference']
    if r['method']!='DOP853' or len(r['rtol'])!=2 or len(r['atol'])!=2 or r['maximum_step_divisors']!=[64,128]:raise ValueError('Fixed double time-reference protocol required')
    for key in ('rtol','atol'):
        if not all(isinstance(v,(int,float)) and not isinstance(v,bool) and 0<v<=1e-8 for v in r[key]) or r[key][1]>=r[key][0]:raise ValueError('Invalid independent time-reference tolerances')


def run(input_path,output):
    start=time.perf_counter();path=Path(input_path);config=json.loads(path.read_text());validate(config)
    output=Path(output)
    if output.exists() and any(output.iterdir()):raise ValueError('Output directory must be new or empty')
    output.mkdir(parents=True,exist_ok=True);budget=Budget(config['model']['maximum_seconds']);cases=[]
    for case in ('smooth','ot','constraint'):
        result,fields=constraint_control(config,budget) if case=='constraint' else experiment(case,config,budget);cases.append(result)
        np.savez_compressed(output/(result['id']+'-fields.npz'),**fields)
        records=result['records']+result.get('temporal_records',[])
        columns=list(dict.fromkeys(k for row in records for k in row if k not in ('l1','l2','linf')))
        with (output/(result['id']+'.csv')).open('w',newline='') as handle:
            writer=csv.DictWriter(handle,fieldnames=['study',*columns]);writer.writeheader()
            for study,rows in [('space',result['records']),('time',result.get('temporal_records',[]))]:
                writer.writerows({'study':study,**{k:v for k,v in row.items() if k in columns}} for row in rows)
    checks={case['id']:case['passed'] for case in cases}
    payload={'schema_version':1,'input_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'passed':all(checks.values()),'checks':checks,'cases':cases,'duration_seconds':time.perf_counter()-start,'termination':'fixed_inputs_completed','scope':'Matched planar CT/GLM finite volumes: exact conserved cell-average moving equilibrium; independent Athena++ OT reference; separately executed DOP853 time references share the spatial RHS. No quantum sweeps.'}
    (output/'result.json').write_text(json.dumps(payload,indent=2,allow_nan=False)+'\n');return payload


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--input',default='inputs.json');parser.add_argument('--output',required=True);args=parser.parse_args()
    result=run(args.input,args.output);print(json.dumps({'passed':result['passed'],'duration_seconds':result['duration_seconds'],'checks':result['checks']}));raise SystemExit(0 if result['passed'] else 1)
