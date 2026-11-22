#!/usr/bin/env python3
"""Run the predeclared bounded conditioning protocol; retain failure controls."""
import argparse
import csv
import hashlib
import importlib.metadata
import json
import math
from pathlib import Path
import platform
import time

from experiments import amg_case,decomposition_case,krylov_case,quadrature_case

HERE=Path(__file__).resolve().parent
INPUT_SHA256='142f7fdeb264f130c64d402f417eb34e0a64e269431137eba5b821e85484306f'


class Budget:
    def __init__(self,seconds):
        if isinstance(seconds,bool) or not isinstance(seconds,(int,float)) or not math.isfinite(seconds) or not 0<seconds<=110:
            raise ValueError('Runtime budget must be finite and in (0,110] seconds')
        self.start=time.monotonic();self.seconds=seconds
    def check(self):
        if time.monotonic()-self.start>self.seconds:raise TimeoutError('Fixed experiment wall-time budget exhausted')


def validate_input(data):
    """This downloadable recipe is fixed, not an unbounded solver-input service."""
    original=json.loads((HERE/'inputs.json').read_text())
    if hashlib.sha256((HERE/'inputs.json').read_bytes()).hexdigest()!=INPUT_SHA256:
        raise ValueError('Predeclared input SHA mismatch')
    if type(data)!=dict or data!=original:raise ValueError('Only the predeclared bounded input is supported')
    def check(value):
        if isinstance(value,dict):
            for key,child in value.items():
                if key=='acceptance':
                    for bound in child.values():
                        if isinstance(bound,bool) or not isinstance(bound,(int,float)) or not math.isfinite(bound) or bound<=0:
                            raise ValueError('Acceptance widths must be positive finite numbers')
                check(child)
        elif isinstance(value,list):
            for child in value:check(child)
        elif isinstance(value,(float,int)) and not isinstance(value,bool) and not math.isfinite(value):raise ValueError('Nonfinite input')
        elif isinstance(value,bool):raise ValueError('Boolean numerical controls are unsupported')
    check(data)
    return data


def write_csv(path,rows):
    names=list(dict.fromkeys(key for row in rows for key in row))
    with path.open('w',newline='') as stream:
        writer=csv.DictWriter(stream,fieldnames=names);writer.writeheader();writer.writerows(rows)


def execute(config,destination):
    validate_input(config);destination=Path(destination)
    if destination.exists() and any(destination.iterdir()):raise ValueError('Output must be new or empty; previous evidence is retained')
    destination.mkdir(parents=True,exist_ok=True);budget=Budget(config['maximum_seconds']);results=[]
    for name,function in [('amg',amg_case),('decompositions',decomposition_case),('krylov',krylov_case),('quadrature',quadrature_case)]:
        budget.check();result=function(config[name],budget);results.append(result)
        write_csv(destination/(result['id']+'.csv'),result['records'])
        if 'residual_histories' in result:write_csv(destination/'amg-residuals.csv',result['residual_histories'])
        # Each completed case is recoverable even if the next one raises.
        (destination/(result['id']+'.json')).write_text(json.dumps(result,ensure_ascii=False,indent=2,allow_nan=False)+'\n')
        print(result['id']+': '+('PASS' if result['passed'] else 'FAIL'),flush=True)
    summary={'schema_version':1,'passed':all(r['passed'] for r in results),'all_passed':all(r['passed'] for r in results),
             'checks':{r['id']:r['passed'] for r in results},'input_sha256':INPUT_SHA256,
             'elapsed_seconds':time.monotonic()-budget.start,
             'termination':'fixed_inputs_completed','duration_seconds':time.monotonic()-budget.start,
             'environment':{'python':platform.python_version(),**{p:importlib.metadata.version(p) for p in ['numpy','scipy','pytest']}},
             'scope':'Four fixed diagnostics; an expected failure-control pass is not solver convergence. No quantum computations.',
             'cases':results}
    budget.check();(destination/'result.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2,allow_nan=False)+'\n')
    return summary


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--output',required=True,type=Path);parser.add_argument('--input','--inputs',dest='inputs',type=Path,default=HERE/'inputs.json');args=parser.parse_args()
    summary=execute(json.loads(args.inputs.read_text()),args.output)
    return 0 if summary['all_passed'] else 1


if __name__=='__main__':raise SystemExit(main())
