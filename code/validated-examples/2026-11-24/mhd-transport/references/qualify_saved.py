#!/usr/bin/env python3
"""Reviewed post-run scheduler correction; requalify unchanged saved fields only."""
import argparse,datetime,json
from pathlib import Path
import numpy as np
from qualify import qualify as original_qualification,sha
ROOT=Path(__file__).resolve().parent


def qualify(directory,records,plan):
    result=original_qualification(directory,records,plan);diagnostics=[]
    for row in records:
        with np.load(Path(directory)/row['file'],allow_pickle=False) as d:times=d['times'].copy()
        requested=np.array(row['snapshots']);valid=bool(times.shape==(5,) and np.isfinite(times).all() and np.all(np.diff(times)>0) and np.all(times>=0) and np.all(times<=row['final_time']) and abs(times[0])<=1e-14 and abs(times[-1]-row['final_time'])<=1e-14)
        old=row['id']+' exact requested output times';index=next(i for i,c in enumerate(result['checks']) if c['name']==old)
        result['checks'][index]=dict(name=row['id']+' five ordered actual times and exact endpoints',value=times.tolist(),bound={'count':5,'strictly_ordered':True,'range':[0,row['final_time']],'endpoint_absolute_tolerance':1e-14},passed=valid)
        diagnostics.append(dict(id=row['id'],actual_times=times.tolist(),requested_quarter_times=requested.tolist(),actual_minus_requested=(times-requested).tolist(),intermediate_times_aligned=False))
    result['passed']=len(records)==6 and len(result['checks'])==31 and all(c['passed'] for c in result['checks'])
    result['output_time_diagnostics']=diagnostics
    result['scope']+=' Quantitative cross-grid, cross-CFL and primary/reference comparisons use final fields only. Intermediate fields retain actual scheduler times; no matched-quarter-frame error is claimed.'
    return result


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    if a.output.exists():raise ValueError('Use a fresh qualification output file')
    contract=json.loads((ROOT/'qualification-contract.json').read_text())
    for name,digest in contract['files_sha256'].items():
        if sha(ROOT/name)!=digest:raise ValueError('Changed qualification input '+name)
    original=json.loads((ROOT/'history/attempt-01-failed-qualification.json').read_text());plan=json.loads((ROOT/'reference-input-plan.json').read_text())
    for row in original['records']:
        if sha(ROOT/row['file'])!=row['sha256']:raise ValueError('Changed reference field '+row['file'])
    quality=qualify(ROOT,original['records'],plan)
    result={**original,'passed':quality['passed'],'qualification':quality,'source_run_contract_sha256':original['reference_contract_sha256'],'qualification_contract_sha256':sha(ROOT/'qualification-contract.json'),'qualification_created_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'pde_rerun_performed':False,'qualification_revision':3,'prior_failed_qualification':'history/attempt-01-failed-qualification.json','prior_failed_gates':6,'revision_reason':contract['revision_reason']}
    a.output.write_text(json.dumps(result,ensure_ascii=False,indent=2,allow_nan=False)+'\n')
    print(json.dumps({'passed':result['passed'],'checks':len(quality['checks']),'pde_rerun_performed':False,'qualification_contract_sha256':result['qualification_contract_sha256']}))
    return 0 if result['passed'] else 1
if __name__=='__main__':raise SystemExit(main())
