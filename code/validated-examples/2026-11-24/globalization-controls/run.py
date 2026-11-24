"""Strict fresh-output CLI. Failure leaves raw candidates and completed rows."""
import argparse
import hashlib
import json
from pathlib import Path
import sys
import traceback
import numpy as np
from experiments import run_all, CASE_ID
from io_contract import save_json


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--input',required=True,type=Path);parser.add_argument('--output',required=True,type=Path);args=parser.parse_args()
    source=Path(__file__).resolve().parent
    if args.output.exists():raise FileExistsError('Fresh output directory required')
    data=args.input.read_bytes()
    if data!=(source/'inputs.json').read_bytes():raise ValueError('Only the frozen input bytes are accepted')
    if hashlib.sha256(data).hexdigest()!='04ee3e49e6e2192ee4e58ae20e03905fc56f0c793ce4bbf7d00c13ae3586a9fb':raise ValueError('Frozen single-input SHA mismatch')
    json.loads(data);args.output.mkdir(parents=True)
    result={'schema_version':1,'passed':False,'input_sha256':hashlib.sha256(data).hexdigest(),
            'termination':'incomplete','checks':{CASE_ID:False},'cases':[],
            'source_sha256':{name:hashlib.sha256((source/name).read_bytes()).hexdigest()
                             for name in json.loads((source/'pre-run-contract.json').read_text())['files_sha256']}}
    try:
        np.seterr(all='raise');case=run_all(args.output);result['cases']=[case]
        result['checks']={CASE_ID:case['passed']};result['passed']=case['passed'];result['termination']='completed_fixed_protocol'
    except BaseException as exc:
        result['failure']={'type':type(exc).__name__,'message':str(exc),'traceback':traceback.format_exc()}
    save_json(args.output/'result.json',result)
    return 0 if result['passed'] else 1


if __name__=='__main__':sys.exit(main())
