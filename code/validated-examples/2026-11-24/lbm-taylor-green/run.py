"""Frozen input runner; partial fields/ledgers survive every numerical failure."""
import argparse
import hashlib
import json
from pathlib import Path
import time
import traceback
import numpy as np
from experiments import execute,IDS
from evolution import dump

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def main():
    root=Path(__file__).resolve().parent;parser=argparse.ArgumentParser()
    parser.add_argument('--input',type=Path,default=root/'inputs.json');parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();start=time.monotonic();contract=json.loads((root/'pre-run-contract.json').read_text())
    for name,value in contract['files_sha256'].items():
        if sha(root/name)!=value:raise ValueError('Frozen scientific source differs: '+name)
    if sha(args.input)!=contract['files_sha256']['inputs.json']:raise ValueError('Only the frozen input is accepted')
    if args.output.exists() and any(args.output.iterdir()):raise ValueError('Fresh result directory required')
    args.output.mkdir(parents=True,exist_ok=True);inputs=json.loads(args.input.read_text());cases=[];failure=None
    try:
        execute(root,args.output,inputs,json.loads((root/'acceptance.json').read_text())['limits'],cases)
    except Exception as error:
        failure=dict(type=type(error).__name__,message=str(error));(args.output/'failure-traceback.txt').write_text(traceback.format_exc())
        if getattr(error,'receipt',None):dump(args.output/'compiler.json',error.receipt)
        if getattr(error,'payload',None):np.savez_compressed(args.output/'failed-candidate.npz',**error.payload)
    ids=IDS[inputs['group']]
    passed=failure is None and {row['id'] for row in cases}==set(ids) and all(row['passed'] for row in cases)
    count=sum(len(row['checks']) for row in cases)
    if passed and count!=contract['planned_case_gates']:
        passed=False;failure=dict(type='GateInventoryError',message=f'Expected{contract["planned_case_gates"]}gates, got{count}')
    result=dict(schema_version=1,passed=bool(passed),termination='fixed_budget_completed' if passed else 'calculation_failed',
                failure=failure,checks={ident:next((row['passed'] for row in cases if row['id']==ident),False) for ident in ids},
                cases=cases,input_sha256=sha(args.input),source_sha256={name:sha(root/name) for name in [*contract['files_sha256'],'pre-run-contract.json']},
                duration_seconds=time.monotonic()-start,numerical_gate_count=count,
                reference_scope='Selected primary benchmark tables and qualified analytic continuum references; fixed finite-Mach/fixed-BC educational LBM, not a general continuum certification.')
    dump(args.output/'result.json',result)
    print(json.dumps(dict(passed=bool(passed),cases=len(cases),gates=count,failure=failure,
                          failed=[key for row in cases for key,value in row['checks'].items() if not value])),flush=True)
    return 0 if passed else 1

if __name__=='__main__':raise SystemExit(main())
