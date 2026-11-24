"""Strict fresh-output/result/checkpoint helpers; no scientific implementation."""
import hashlib,json,traceback,time
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parent
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def write(path,data):Path(path).write_text(json.dumps(data,ensure_ascii=False,indent=2,allow_nan=False)+'\n')
def verify(input_path):
    c=json.loads((ROOT/'pre-run-contract.json').read_text())
    if sha(input_path)!=c['files_sha256']['inputs.json']:raise ValueError('Use exact frozen input bytes')
    for n,h in c['files_sha256'].items():
        if sha(ROOT/n)!=h:raise ValueError('Changed frozen input/source/reference '+n)
    q=json.loads((ROOT/'references/qualification.json').read_text())
    if q['passed'] is not True or not q['checks'] or not all(type(v) is bool and v for v in q['checks'].values()):raise ValueError('Unqualified independent reference')
    return c
def check(case,name,value,bound,passed):
    case['checks'][name]=bool(passed);case['check_details'].append(dict(name=name,value=value,bound=bound,passed=bool(passed)))
def case(ident):return dict(id=ident,passed=False,checks={},check_details=[],records=[],metrics={})
def checkpoint(output,cases):write(output/'completed-cases.json',cases)
def save_fields(output,name,fields):
    np.savez_compressed(output/(name+'.npz'),**fields)
    if 'history' in fields:np.savetxt(output/(name+'-history.csv'),fields['history'],delimiter=',',header=','.join(str(x) for x in fields.get('history_columns',['column_'+str(i) for i in range(fields['history'].shape[1])])),comments='',fmt='%.16e')
def run(main_function):
    import argparse
    p=argparse.ArgumentParser();p.add_argument('--input',type=Path,default=ROOT/'inputs.json');p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    if a.output.exists() and (not a.output.is_dir() or any(a.output.iterdir())):p.error('Use a fresh/empty output;prior evidence is never overwritten')
    a.output.mkdir(parents=True,exist_ok=True);start=time.monotonic();cases=[];failure=None;contract=None
    try:
        contract=verify(a.input);cfg=json.loads(a.input.read_text());limits=json.loads((ROOT/'acceptance.json').read_text())['limits'];main_function(cfg,limits,a.output,cases);passed=bool(cases) and all(c['passed'] for c in cases)
    except Exception as error:
        failure=dict(type=type(error).__name__,message=str(error),traceback=traceback.format_exc());passed=False
    result=dict(schema_version=1,passed=passed,checks={c['id']:c['passed'] for c in cases} or {'completed':False},cases=cases,termination='fixed_budget_completed' if failure is None else 'calculation_failed',failure=failure,input_sha256=sha(a.input),duration_seconds=time.monotonic()-start)
    if contract is not None:result['source_sha256']={**contract['files_sha256'],'pre-run-contract.json':sha(ROOT/'pre-run-contract.json')}
    write(a.output/'result.json',result);print(json.dumps(dict(passed=passed,cases=len(cases),gates=sum(len(c['checks']) for c in cases),seconds=result['duration_seconds'],failure=failure)))
    if not passed:raise SystemExit(1)
