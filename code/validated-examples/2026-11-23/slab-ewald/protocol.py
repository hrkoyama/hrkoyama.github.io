"""Self-contained fixed-input runner and persistent partial-output protocol."""
import argparse,csv,hashlib,json,time,traceback
from pathlib import Path
import numpy as np

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def dump(p,v):Path(p).write_text(json.dumps(v,indent=2,ensure_ascii=False,allow_nan=False)+'\n')
def finite(v):
    if isinstance(v,(float,np.floating)) and not np.isfinite(v):raise ArithmeticError('Nonfinite measurement')
    if isinstance(v,dict):
        for x in v.values():finite(x)
    if isinstance(v,(list,tuple)):
        for x in v:finite(x)

class Budget:
    def __init__(self,seconds=115):self.end=time.monotonic()+seconds
    def check(self):
        if time.monotonic()>self.end:raise TimeoutError('Fixed scientific runtime budget exhausted')

class Case:
    def __init__(self,ident,out,cases):
        self.out=out;self.data=dict(id=ident,passed=False,checks={},records=[],metrics={},data_files=[]);cases.append(self.data)
    def gate(self,name,passed):self.data['checks'][name]=bool(passed)
    def bound(self,name,value,limit):self.gate(name,np.isfinite(value) and value<=limit)
    def save(self,name,arrays):
        path=self.data['id']+'-'+name+'.npz';np.savez_compressed(self.out/path,**arrays);self.data['data_files'].append(path);return path
    def row(self,record):
        finite(record);self.data['records'].append(record);dump(self.out/(self.data['id']+'-partial.json'),self.data)
    def finish(self,metrics):
        finite(metrics);self.data['metrics']=metrics;self.data['passed']=bool(self.data['records'] and self.data['checks'] and all(self.data['checks'].values()))

def frozen(root):
    contract=json.loads((root/'pre-run-contract.json').read_text())
    for name,h in contract['files_sha256'].items():
        if sha(root/name)!=h:raise ValueError('Frozen scientific source changed: '+name)
    return contract

def main(root,ids,execute):
    parser=argparse.ArgumentParser();parser.add_argument('--input',type=Path,default=root/'inputs.json');parser.add_argument('--output',type=Path,required=True);args=parser.parse_args();contract=frozen(root)
    if sha(args.input)!=contract['files_sha256']['inputs.json']:raise ValueError('Only frozen input accepted')
    if args.output.exists() and any(args.output.iterdir()):raise ValueError('Choose fresh output directory')
    args.output.mkdir(parents=True,exist_ok=True);cases=[];failure=None;start=time.monotonic()
    try:execute(json.loads(args.input.read_text()),json.loads((root/'acceptance.json').read_text())['limits'],args.output,cases,Budget())
    except Exception as error:
        failure=dict(type=type(error).__name__,message=str(error));(args.output/'failure-traceback.txt').write_text(traceback.format_exc())
        if getattr(error,'payload',None):np.savez_compressed(args.output/'failed-candidate.npz',**error.payload)
    for c in cases:
        if not c['records']:continue
        names=list(dict.fromkeys(k for row in c['records'] for k in row))
        with (args.output/(c['id']+'.csv')).open('w',newline='') as f:
            w=csv.DictWriter(f,fieldnames=names);w.writeheader()
            for row in c['records']:w.writerow({k:json.dumps(v,allow_nan=False) if isinstance(v,(dict,list)) else v for k,v in row.items()})
    passed=bool(failure is None and set(ids)=={c['id'] for c in cases} and all(c['passed'] for c in cases))
    result=dict(schema_version=1,passed=passed,termination='fixed_budget_completed' if passed else 'calculation_failed',failure=failure,input_sha256=sha(args.input),checks={i:next((c['passed'] for c in cases if c['id']==i),False) for i in ids},cases=cases,numerical_gate_count=sum(len(c['checks']) for c in cases),duration_seconds=time.monotonic()-start,source_sha256={n:sha(root/n) for n in [*contract['files_sha256'],'pre-run-contract.json']})
    dump(args.output/'result.json',result);print(json.dumps(dict(passed=passed,cases=len(cases),gates=result['numerical_gate_count'],failure=failure,failed=[n for c in cases for n,v in c['checks'].items() if not v])),flush=True)
    return 0 if passed else 1
