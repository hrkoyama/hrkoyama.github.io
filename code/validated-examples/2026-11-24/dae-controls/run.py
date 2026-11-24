"""Fresh-output fixed-protocol CLI with finite public result envelope."""
import argparse
import hashlib
import json
from pathlib import Path
import sys
import traceback
from io_contract import save_json
import experiments


def main():
    p=argparse.ArgumentParser();p.add_argument('--input',required=True,type=Path);p.add_argument('--output',required=True,type=Path);args=p.parse_args()
    source=Path(__file__).resolve().parent
    raw=args.input.read_bytes()
    expected=hashlib.sha256((source/'inputs.json').read_bytes()).hexdigest()
    contract=json.loads((source/'pre-run-contract.json').read_text())
    if hashlib.sha256(raw).hexdigest()!=expected or expected!=contract['files_sha256']['inputs.json']:raise ValueError('Only frozen input bytes accepted')
    if args.output.exists():raise FileExistsError('Fresh output directory required')
    args.output.mkdir(parents=True)
    cfg=json.loads(raw);accept=json.loads((source/'acceptance.json').read_text())
    ids=['index1-dae-consistent-initialization', 'robertson-conservation-dae', 'high-index-pendulum']
    result={'schema_version':1,'passed':False,'input_sha256':expected,'termination':'incomplete','checks':{k:False for k in ids},'cases':[],
            'source_sha256':{name:hashlib.sha256((source/name).read_bytes()).hexdigest() for name in contract['files_sha256']}}
    save_json(args.output/'result.json',result)
    try:
        for ident in ids:
            case=(experiments.index1_case(args.output,cfg[ident],accept[ident]) if ident==ids[0] else experiments.robertson_case(args.output,cfg[ident],accept[ident],source) if ident==ids[1] else experiments.pendulum_case(args.output,cfg[ident],accept[ident]))
            result['cases'].append(case);result['checks'][ident]=case['passed']
            save_json(args.output/'result.json',result)
        result['passed']=all(result['checks'].values());result['termination']='completed_fixed_protocol'
        targets=[v for case in result['cases'] for v in case['original_target_results'].values()]
        result['original_target_summary']={'met':sum(targets),'total':len(targets),'all_met':all(targets),'acceptance_sha256':hashlib.sha256((source/'acceptance.json').read_bytes()).hexdigest()}
        result['verification_scope']='Retained numerical requirements plus truthful reporting of original accuracy study goals; original_target_summary is separate.'
    except BaseException as exc:
        # Case-owned partial rows are checkpointed before later solvers/diagnostics.
        current=args.output/(ident+'-partial.json')
        if current.exists() and not any(c['id']==ident for c in result['cases']):result['cases'].append(json.loads(current.read_text()))
        result['failure']={'type':type(exc).__name__,'message':str(exc),'traceback':traceback.format_exc()}
    save_json(args.output/'result.json',result)
    return 0 if result['passed'] else 1


if __name__=='__main__':sys.exit(main())
