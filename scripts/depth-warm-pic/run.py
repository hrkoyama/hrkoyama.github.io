#!/usr/bin/env python3
"""Fixed warm full-f PIC calculations; qualify independent linear IVPs first."""
import argparse
import csv
from datetime import datetime,timezone
import hashlib
import json
from pathlib import Path
import time
import numpy as np
from experiments import specs,run_one,decisions
from primary import ParticleFailure,COLUMNS
from references.linear import qualify
ROOT=Path(__file__).resolve().parent


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def save(path,value):Path(path).write_text(json.dumps(value,ensure_ascii=False,indent=2,allow_nan=False)+'\n')

def read_limits(path):return json.loads(Path(path).read_text())['limits']

def write_csv(path,columns,rows):
    with Path(path).open('w',newline='') as handle:
        writer=csv.writer(handle);writer.writerow(columns);writer.writerows(rows)


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--input',type=Path,required=True);parser.add_argument('--output',type=Path,required=True);args=parser.parse_args()
    if args.output.exists():raise ValueError('Fresh output directory required; retain all attempts')
    args.output.mkdir(parents=True);cfg=json.loads(args.input.read_text());limits=read_limits(ROOT/'acceptance.json');contract=json.loads((ROOT/'pre-run-contract.json').read_text())
    for name,digest in contract['files_sha256'].items():
        if sha(ROOT/name)!=digest:raise ValueError('Frozen source changed: '+name)
    if sha(args.input)!=contract['files_sha256']['inputs.json']:raise ValueError('Input differs from the frozen experiment')
    start=time.monotonic();deadline=start+cfg['main_budget_seconds'];results=[];qualification={};references={};completed=[];retained_candidates=[];failure=None;termination='fixed_budget_completed'
    try:
        # Neither qualification nor a PIC state is recycled from an earlier run.
        for case,controls in cfg['cases'].items():
            q,arrays=qualify(case,controls,limits);qualification[case]=q;references[case]=dict(arrays,omega_real=q['omega_real'],gamma=q['gamma']);np.savez_compressed(args.output/(case+'-linear-reference.npz'),**arrays);save(args.output/'reference-qualification.json',qualification)
        if not all(q['passed'] for q in qualification.values()):raise ArithmeticError('Independent linear reference failed; no PIC trajectory launched')
        for case,controls in cfg['cases'].items():
            rows=[];series={}
            for spec in specs(case,controls):
                name=case+'-'+spec['id']
                def retain_completed(arrays):
                    np.savez_compressed(args.output/(name+'.npz'),**arrays)
                    write_csv(args.output/(name+'-history.csv'),COLUMNS,arrays['history'])
                    retained_candidates.append(dict(case=case,run_id=spec['id'],file=name+'.npz',sha256=sha(args.output/(name+'.npz')),retained_before_fit=True))
                    save(args.output/'retained-candidates-before-fit.json',retained_candidates)
                row,arrays,signal=run_one(case,controls,spec,references[case],deadline,retain_completed=retain_completed);row.update(file=name+'.npz',sha256=sha(args.output/(name+'.npz')));rows.append(row);completed.append(dict(row));save(args.output/'completed-runs.json',completed)
                series[spec['id']]=(arrays['history'][:,1],signal)
            checks,metrics=decisions(case,controls,rows,series,qualification[case],limits);check_map={q['name']:q['passed'] for q in checks}
            results.append(dict(id=case,passed=all(check_map.values()),checks=check_map,gates=checks,records=rows,metrics=metrics))
            columns=['id','family','seed','grid','nodes','spatial_strata','amplitude','dt','particles','steps','time','gamma','omega','fit_residual','charge','momentum','resolved_gauss','energy']
            write_csv(args.output/(case+'.csv'),columns,[[r['id'],r['family'],r['seed'],r['grid'],r['nodes'],r.get('spatial_strata',''),r['amplitude'],r['dt'],r['particles'],r['steps'],r['time'],r['fit']['gamma'] if r['fit'] else '',r['fit']['omega'] if r['fit'] else '',r['fit']['relative_fit_residual'] if r['fit'] else '',r['maximum_charge_error'],r['maximum_momentum_drift'],r['maximum_resolved_gauss'],r['maximum_energy_drift']] for r in rows])
    except Exception as error:
        failure=dict(type=type(error).__name__,message=str(error));termination='scientific_failure'
        if isinstance(error,ParticleFailure):np.savez_compressed(args.output/'failed-stage.npz',x=error.x,v=error.v);failure['stage']=error.context
    checks={case:next((r['passed'] for r in results if r['id']==case),False) for case in cfg['cases']}
    result=dict(schema_version=1,group='warm-pic',input_sha256=sha(args.input),passed=failure is None and all(checks.values()),termination=termination,failure=failure,checks=checks,cases=results,reference_qualifications=qualification,completed_run_count=len(completed),retained_complete_candidate_count=len(retained_candidates),duration_seconds=time.monotonic()-start,created_at_utc=datetime.now(timezone.utc).isoformat())
    save(args.output/'result.json',result);print(json.dumps(dict(passed=result['passed'],runs=len(completed),gates=sum(len(c['checks']) for c in results),failed={c['id']:[k for k,v in c['checks'].items() if not v] for c in results},failure=failure)),flush=True);return 0 if result['passed'] else 1


if __name__=='__main__':raise SystemExit(main())
