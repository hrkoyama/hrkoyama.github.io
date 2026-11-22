#!/usr/bin/env python3
"""Execute the preregistered bounded particle/transport validation protocol."""
import argparse
import csv
import hashlib
import importlib.metadata
import json
import math
from pathlib import Path
import platform
import time

from longrange_experiments import build_longrange_cases
from kinetic_experiments import pic_case, dsmc_case, radiation_case

HERE=Path(__file__).resolve().parent
INPUT_SHA256='c90c95405e1622affc84c3feaffc50a7f5599fc868741823e26c7840eeda288b'
CASE_IDS=['ewald-convergence','spme-convergence','fmm-convergence','pic-conservation','dsmc-statistics','radiation-convergence']


def strict_json(payload):
    def pairs(items):
        result={}
        for key,value in items:
            if key in result:raise ValueError('Repeated JSON field: '+key)
            result[key]=value
        return result
    def invalid(value):raise ValueError('Nonfinite JSON constant: '+value)
    return json.loads(payload,object_pairs_hook=pairs,parse_constant=invalid)


def validate_input(config):
    original=(HERE/'inputs.json').read_bytes()
    if hashlib.sha256(original).hexdigest()!=INPUT_SHA256:raise ValueError('Preregistered input SHA mismatch')
    if type(config) is not dict or config!=strict_json(original):raise ValueError('Only the fixed reviewed protocol is supported')
    def finite(value):
        if isinstance(value,dict):
            for child in value.values():finite(child)
        elif isinstance(value,list):
            for child in value:finite(child)
        elif isinstance(value,bool):raise ValueError('Boolean numerical controls are unsupported')
        elif isinstance(value,(float,int)) and not math.isfinite(value):raise ValueError('Nonfinite numerical input')
    finite(config)
    return config


def write_case(destination,case):
    if case['id'] not in CASE_IDS or type(case['passed']) is not bool:raise ValueError('Invalid case identity/decision')
    if not case['checks'] or any(type(v) is not bool for v in case['checks'].values()):raise ValueError('Numerical decisions must be literal booleans')
    text=json.dumps(case,ensure_ascii=False,indent=2,allow_nan=False)+'\n'
    (destination/(case['id']+'.json')).write_text(text)
    rows=case['records']
    fields=list(dict.fromkeys(k for row in rows for k in row))
    with (destination/(case['id']+'.csv')).open('w',newline='') as stream:
        writer=csv.DictWriter(stream,fieldnames=fields);writer.writeheader();writer.writerows(rows)


def execute(config,destination):
    validate_input(config);destination=Path(destination)
    if destination.exists() and any(destination.iterdir()):raise ValueError('Output must be new or empty; earlier evidence is retained')
    destination.mkdir(parents=True,exist_ok=True);start=time.monotonic();cases=[]
    def retain(case):
        if time.monotonic()-start>config['maximum_seconds']:raise TimeoutError('Fixed wall-time budget exhausted')
        write_case(destination,case);cases.append(case)
        print(case['id']+': '+('PASS' if case['passed'] else 'FAIL'),flush=True)
    for case in build_longrange_cases(config):retain(case)
    for name,function in [('pic',pic_case),('dsmc',dsmc_case),('radiation',radiation_case)]:retain(function(config[name]))
    if [c['id'] for c in cases]!=CASE_IDS:raise ValueError('Incomplete or reordered protocol')
    checks={c['id']:c['passed'] for c in cases}
    result={'schema_version':1,'input_sha256':INPUT_SHA256,'passed':all(checks.values()),'checks':checks,'cases':cases,
            'termination':'fixed_inputs_completed','duration_seconds':time.monotonic()-start,
            'environment':{'python':platform.python_version(),**{k:importlib.metadata.version(k) for k in ['numpy','scipy','pytest']}},
            'scope':'Six small extensions of existing physical problems. Independently formulated references, shared spatial/time reference limits, approximate conservation and independent-seed statistical uncertainty are explicit. No quantum calculations.'}
    (destination/'result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2,allow_nan=False)+'\n')
    return result


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--input',type=Path,default=HERE/'inputs.json');parser.add_argument('--output',type=Path,required=True);args=parser.parse_args()
    result=execute(strict_json(args.input.read_bytes()),args.output)
    return 0 if result['passed'] else 1


if __name__=='__main__':raise SystemExit(main())
