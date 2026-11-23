"""One-shot independent C++ reference build/execution; not ordinary Python CI.

Run only after freezing pre-run-contract.json, under the parent's disk guard.
Binary/raw intermediates go in --scratch, source+selected receipts stay here.
"""
from __future__ import annotations
import argparse
from datetime import datetime,timezone
import hashlib
import json
import platform
from pathlib import Path
import subprocess
import sys
import time

ROOT=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def utc():return datetime.now(timezone.utc).isoformat()
def main():
    p=argparse.ArgumentParser();p.add_argument('--scratch',type=Path,required=True);a=p.parse_args()
    if a.scratch.exists():raise ValueError('Use a new scratch directory for each attempt')
    contract=json.loads((ROOT/'pre-run-contract.json').read_text())
    for n,h in contract['files_sha256'].items():
        if sha(ROOT/n)!=h:raise ValueError('Changed predeclared reference file: '+n)
    a.scratch.mkdir(parents=True)
    dest=ROOT/'independent-execution.json'
    if dest.exists():raise ValueError('Never overwrite execution history')
    receipt={'schema_version':1,'started_at_utc':utc(),'new_reference_pde_executed':True,'primary_operator_imports':False,'source_language':'C++17','source_sha256':sha(ROOT/'reference.cpp'),'pre_run_contract_sha256':sha(ROOT/'pre-run-contract.json'),'python':sys.version,'platform':platform.platform(),'processes':[],'passed':False}
    def save():dest.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
    def call(name,cmd,timeout=120):
        begin=time.monotonic();r={'name':name,'command':list(map(str,cmd)),'timeout_seconds':timeout,'started_at_utc':utc()};receipt['processes'].append(r);save()
        try:
            v=subprocess.run(cmd,cwd=ROOT,text=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=timeout)
            r.update({'exit_code':v.returncode,'duration_seconds':time.monotonic()-begin,'stdout':v.stdout,'stderr':v.stderr})
            save()
            if v.returncode:raise RuntimeError(name+' failed')
            print(name+': '+v.stdout.strip()[-1000:],flush=True)
            return v
        except subprocess.TimeoutExpired as exc:
            r.update({'timed_out':True,'duration_seconds':time.monotonic()-begin,'stdout':(exc.stdout or b'').decode() if isinstance(exc.stdout,bytes) else exc.stdout,'stderr':(exc.stderr or b'').decode() if isinstance(exc.stderr,bytes) else exc.stderr});save();raise
    try:
        call('compiler-version',['/usr/bin/c++','--version'])
        binary=a.scratch/'reference'
        call('compile',['/usr/bin/c++','-std=c++17','-O3','-Wall','-Wextra','-Werror',str(ROOT/'reference.cpp'),'-o',str(binary)])
        receipt['binary_sha256']=sha(binary);save()
        call('self-tests',[str(binary),'--self-test'])
        for ny in (80,160):
            prefix=a.scratch/f'forward-step-ny{ny}'
            call('reference-ny'+str(ny),[str(binary),str(ny),str(prefix)])
        call('convert',[sys.executable,str(ROOT/'convert.py'),'--raw-dir',str(a.scratch),'--output-dir',str(ROOT)])
        receipt['passed']=True;receipt['finished_at_utc']=utc();save()
    except BaseException as exc:
        receipt.update({'passed':False,'failure':repr(exc),'finished_at_utc':utc()});save();raise
if __name__=='__main__':main()
