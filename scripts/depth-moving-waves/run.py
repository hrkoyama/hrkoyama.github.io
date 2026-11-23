#!/usr/bin/env python3
import argparse,csv,hashlib,json,time,traceback
from pathlib import Path
import experiments
ROOT=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def frozen():
    c=json.loads((ROOT/'pre-run-contract.json').read_text())
    for n,h in c['files_sha256'].items():
        if sha(ROOT/n)!=h:raise ValueError('Frozen source changed: '+n)
    return c
def main():
    p=argparse.ArgumentParser();p.add_argument('--input',type=Path,default=ROOT/'inputs.json');p.add_argument('--output',type=Path,required=True);a=p.parse_args();c=frozen()
    if sha(a.input)!=c['files_sha256']['inputs.json']:raise ValueError('Frozen input required')
    if a.output.exists() and any(a.output.iterdir()):raise ValueError('Use new output directory')
    a.output.mkdir(parents=True,exist_ok=True);t=time.monotonic();cases=[];failure=None
    try:experiments.execute(json.loads(a.input.read_text()),a.output,json.loads((ROOT/'acceptance.json').read_text())['limits'],cases)
    except Exception as e:
        failure=dict(type=type(e).__name__,message=str(e));(a.output/'failure-traceback.txt').write_text(traceback.format_exc())
    for case in cases:
        names=list(dict.fromkeys(k for row in case['records'] for k in row))
        with (a.output/(case['id']+'.csv')).open('w',newline='') as f:
            w=csv.DictWriter(f,fieldnames=names);w.writeheader();w.writerows(case['records'])
    passed=failure is None and len(cases)==2 and all(x['passed'] for x in cases)
    result=dict(schema_version=1,passed=passed,termination='fixed_budget_completed' if passed else 'calculation_failed',input_sha256=sha(a.input),checks={ident:next((x['passed'] for x in cases if x['id']==ident),False) for ident in experiments.IDS},cases=cases,failure=failure,duration_seconds=time.monotonic()-t,files_sha256={x.name:sha(x) for x in a.output.iterdir() if x.is_file()},source_sha256={n:sha(ROOT/n) for n in [*c['files_sha256'],'pre-run-contract.json']})
    (a.output/'result.json').write_text(json.dumps(result,indent=2,allow_nan=False)+'\n');print(json.dumps(dict(passed=passed,cases=len(cases),gates=sum(len(x['checks']) for x in cases),failed=[k for x in cases for k,v in x['checks'].items() if not v],failure=failure)));return 0 if passed else 1
if __name__=='__main__':raise SystemExit(main())
