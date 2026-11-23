#!/usr/bin/env python3
"""Execute the two complete, bounded level-set examples without a network."""
import argparse,csv,hashlib,json,platform,time
from pathlib import Path
import numpy as np
from geometry import grid,distance
from level_set import Budget,run_case,validate


def run(input_path,output_path):
    payload=Path(input_path).read_bytes()
    def reject(value):raise ValueError('Nonfinite JSON '+value)
    config=json.loads(payload,parse_constant=reject)
    ids=['level-set-translation','level-set-rotation']
    if config.get('schema_version')!=1 or list(config['cases'])!=ids:raise ValueError('Use the complete two-case input')
    for case in config['cases'].values():validate(case)
    output=Path(output_path)
    if output.exists() and (not output.is_dir() or any(output.iterdir())):raise ValueError('Use a new or empty output directory')
    output.mkdir(parents=True,exist_ok=True);started=time.monotonic();budget=Budget(config['maximum_total_seconds'])
    cases=[]
    for ident,case in config['cases'].items():
        result,fields=run_case(case,budget);result['id']=ident
        result['input_sha256']=hashlib.sha256(json.dumps(case,sort_keys=True).encode()).hexdigest()
        x,y=grid(128)
        np.savez_compressed(output/(ident+'.npz'),x=x,y=y,initial=distance(case,x,y,0),
                            reference_final=distance(case,x,y,case['time']),
                            phi_advection=fields['advection-only'],phi_redistance=fields['redistance'])
        summary=[{k:v for k,v in row.items() if k not in ['snapshots','contours','redistance_log']} for row in result['records']]
        columns=list(dict.fromkeys(k for row in summary for k in row))
        with (output/(ident+'.csv')).open('w',newline='') as stream:
            writer=csv.DictWriter(stream,fieldnames=columns);writer.writeheader();writer.writerows(summary)
        cases.append(result)
    answer={'schema_version':1,'passed':all(c['passed'] for c in cases),
            'checks':{c['id']:c['passed'] for c in cases},'cases':cases,
            'input_sha256':hashlib.sha256(payload).hexdigest(),'termination':'fixed_budget_completed',
            'duration_seconds':time.monotonic()-started,'environment':{'python':platform.python_version(),'platform':platform.platform(),'numpy':np.__version__}}
    (output/'result.json').write_text(json.dumps(answer,ensure_ascii=False,indent=2,allow_nan=False)+'\n')
    print(json.dumps({'passed':answer['passed'],'seconds':answer['duration_seconds'],'cases':[{k:c[k] for k in ['id','metrics','checks']} for c in cases]},indent=2))
    return answer


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--input',required=True);parser.add_argument('--output',required=True);args=parser.parse_args()
    try:result=run(args.input,args.output)
    except (OSError,ValueError,ArithmeticError,RuntimeError,KeyError,TypeError) as error:
        print(type(error).__name__+': '+str(error));raise SystemExit(2)
    raise SystemExit(0 if result['passed'] else 1)
