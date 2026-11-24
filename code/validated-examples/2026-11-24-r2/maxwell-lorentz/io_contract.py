"""Fresh-output contract, candidate retention and strict public result envelope."""
import hashlib,json,traceback,time
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write(p,d):Path(p).write_text(json.dumps(d,ensure_ascii=False,indent=2,allow_nan=False)+'\n')
def case(ident):return dict(id=ident,passed=False,checks={},check_details=[],records=[],metrics={})
def check(c,name,value,bound,passed):
    if name in c['checks']:raise ValueError('Duplicate gate '+name)
    c['checks'][name]=bool(passed);c['check_details'].append(dict(name=name,value=value,bound=bound,passed=bool(passed)))
def save(output,name,fields):np.savez_compressed(output/(name+'.npz'),**fields)
def csv(output,name,columns,rows):
    values=np.asarray(rows,dtype=float)
    if values.ndim!=2 or values.shape[1]!=len(columns) or not np.isfinite(values).all():raise ValueError('Finite rectangular CSV required')
    np.savetxt(output/(name+'.csv'),values,delimiter=',',header=','.join(columns),comments='',fmt='%.16e')
def checkpoint(output,cases):write(output/'completed-cases.json',cases)
def verify(p):
    c=json.loads((ROOT/'pre-run-contract.json').read_text())
    if sha(p)!=c['files_sha256']['inputs.json']:raise ValueError('Exact frozen input required')
    for name,expected in c['files_sha256'].items():
        if sha(ROOT/name)!=expected:raise ValueError('Changed fixed source '+name)
    return c
def run(execute):
    import argparse
    p=argparse.ArgumentParser();p.add_argument('--input',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    if a.output.exists() and (not a.output.is_dir() or any(a.output.iterdir())):raise ValueError('Fresh output required')
    a.output.mkdir(parents=True,exist_ok=True);start=time.monotonic();cases=[];failure=None;contract=None
    try:
        contract=verify(a.input);cfg=json.loads(a.input.read_text());limits=json.loads((ROOT/'acceptance.json').read_text())['limits'];execute(cfg,limits,a.output,cases)
        passed=bool(cases) and all(c['passed'] for c in cases)
    except BaseException as e:
        failure=dict(type=type(e).__name__,message=str(e),traceback=traceback.format_exc());passed=False
    result=dict(schema_version=1,passed=passed,cases=cases,checks={c['id']:bool(c['passed']) for c in cases} or {'completed':False},termination='fixed_budget_completed' if failure is None else 'calculation_failed',failure=failure,input_sha256=sha(a.input),duration_seconds=time.monotonic()-start)
    if contract is not None:result['source_sha256']={**contract['files_sha256'],'pre-run-contract.json':sha(ROOT/'pre-run-contract.json')}
    write(a.output/'result.json',result);print(json.dumps(dict(passed=passed,cases=len(cases),gates=sum(len(c['checks']) for c in cases),seconds=result['duration_seconds'],failure=failure)))
    if not passed:raise SystemExit(1)
