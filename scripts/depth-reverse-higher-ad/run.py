"""Three fixed AD cases with strict result envelope and partial-state retention."""
import argparse
import hashlib
import json
from pathlib import Path
import sys
import traceback
import numpy as np
from experiments import run_reverse,run_hvp,run_kinks,CASE_IDS
from io_contract import save_json


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--input',required=True,type=Path);parser.add_argument('--output',required=True,type=Path);args=parser.parse_args()
    source=Path(__file__).resolve().parent
    if args.output.exists():raise FileExistsError('Fresh output directory required')
    data=args.input.read_bytes()
    if data!=(source/'inputs.json').read_bytes():raise ValueError('Only the exact frozen input bytes are supported')
    if hashlib.sha256(data).hexdigest()!='760e23bd914d37ebab5142bc741a2d443207d7d2c6d0a8630031439ecfedec2e':raise ValueError('Frozen single-input SHA mismatch')
    json.loads(data);args.output.mkdir(parents=True)
    result={'schema_version':1,'passed':False,'input_sha256':hashlib.sha256(data).hexdigest(),
            'termination':'incomplete','checks':dict.fromkeys(CASE_IDS,False),'cases':[],
            'source_sha256':{name:hashlib.sha256((source/name).read_bytes()).hexdigest()
                             for name in json.loads((source/'pre-run-contract.json').read_text())['files_sha256']}}
    try:
        np.seterr(all='raise')
        for function in [run_reverse,run_hvp,run_kinks]:
            case=function(args.output);result['cases'].append(case);result['checks'][case['id']]=case['passed']
            save_json(args.output/'result.json',result)
        result['termination']='completed_fixed_protocol';result['passed']=all(result['checks'].values())
    except BaseException as exc:
        result['failure']={'type':type(exc).__name__,'message':str(exc),'traceback':traceback.format_exc()}
    save_json(args.output/'result.json',result)
    return 0 if result['passed']else 1


if __name__=='__main__':sys.exit(main())
