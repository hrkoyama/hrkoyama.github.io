"""Small strict CLI/result/retention helpers; no experiment is selected adaptively."""
import argparse,csv,hashlib,json,time,traceback
from pathlib import Path
import numpy as np


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def write(path,value):Path(path).write_text(json.dumps(value,indent=2,allow_nan=False)+'\n')
def csv_numeric(path,columns,rows):
    with Path(path).open('w',newline='') as handle:
        if not columns or len(set(columns))!=len(columns):raise ValueError('Unique nonempty CSV header required')
        w=csv.writer(handle);w.writerow(columns)
        for row in rows:
            if len(row)!=len(columns) or not all(isinstance(x,(int,float,np.integer,np.floating)) and np.isfinite(x) for x in row):
                raise ArithmeticError('Finite numeric rectangular CSV required')
            w.writerow(row)

def run(experiment,here):
    p=argparse.ArgumentParser();p.add_argument('--input',type=Path,default=here/'inputs.json');p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    if a.output.exists() and (not a.output.is_dir() or any(a.output.iterdir())):p.error('Fresh or empty output required; never overwrite an attempt')
    a.output.mkdir(parents=True,exist_ok=True);start=time.monotonic();cases=[];partial={};failure=None;contract={}
    try:
        contract=json.loads((here/'pre-run-contract.json').read_text())
        if sha(a.input)!=contract['files_sha256']['inputs.json']:raise ValueError('Only fixed input table accepted')
        for name,expected in contract['files_sha256'].items():
            if sha(here/name)!=expected:raise ValueError('Changed frozen file '+name)
        cfg=json.loads(a.input.read_text());limits=json.loads((here/'acceptance.json').read_text())['limits']
        experiment(cfg,limits,a.output,cases,partial)
        expected=set(cfg['cases'])
        if len(cases)!=len(expected) or {c['id'] for c in cases}!=expected:raise ValueError('Fixed case inventory differs')
        if any(not c['records'] for c in cases):raise ValueError('Missing completed case records')
        if sum(len(c['checks']) for c in cases)!=contract['planned_case_gates']:raise ValueError('Fixed numerical gate inventory differs')
        result={'schema_version':1,'passed':bool(cases) and all(c['passed'] for c in cases),'checks':{c['id']:c['passed'] for c in cases},'cases':cases,'termination':'fixed_budget_completed','failure':None,'input_sha256':sha(a.input),'source_sha256':{**contract['files_sha256'],'pre-run-contract.json':sha(here/'pre-run-contract.json')},'numerical_gate_count':sum(len(c['checks']) for c in cases),'wall_seconds':time.monotonic()-start}
    except Exception as error:
        if partial:np.savez(a.output/'failed-candidate-state.npz',**partial)
        failure={'type':type(error).__name__,'message':str(error),'traceback':traceback.format_exc()}
        result={'schema_version':1,'passed':False,'checks':{'completed_without_exception':False},'cases':cases,'termination':'failed','failure':failure,'wall_seconds':time.monotonic()-start}
    write(a.output/'result.json',result);print(json.dumps({'passed':result['passed'],'case_count':len(cases),'gates':result.get('numerical_gate_count',0),'wall_seconds':result['wall_seconds'],'failure':failure}))
    if not result['passed']:raise SystemExit(1)


def case_record(ident,cases):
    row={'id':ident,'passed':False,'checks':{},'metrics':{},'records':[],'termination':'in_progress'};cases.append(row);return row

def finish_case(row,output):
    row.update(passed=bool(row['records']) and bool(row['checks']) and all(row['checks'].values()),termination='fixed_budget_completed');write(output/(row['id']+'-checkpoint.json'),row)
