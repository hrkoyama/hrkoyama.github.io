"""Convert this reference's raw C++ outputs; no PDE execution or primary imports.

Usage: python convert.py --raw-dir TEMP --output-dir references
The output fixtures are independent finite-grid numerical references, not exact.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parent
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,d): p.write_text(json.dumps(d,ensure_ascii=False,indent=2,allow_nan=False)+'\n')
def primitive(q):
    rho=q[...,0]
    return np.stack((rho,q[...,1]/rho,q[...,2]/rho,.4*(q[...,3]-.5*(q[...,1]**2+q[...,2]**2)/rho)),axis=-1)
def restrict(q,n):
    m=q.shape[1]//n
    if q.shape!=(3*n*m,n*m,4) or m<1: raise ValueError('Unaligned reference restriction')
    return q.reshape(3*n,m,n,m,4).mean(axis=(1,3))
def main():
    p=argparse.ArgumentParser();p.add_argument('--raw-dir',type=Path,required=True);p.add_argument('--output-dir',type=Path,required=True);a=p.parse_args()
    a.output_dir.mkdir(parents=True,exist_ok=True)
    contract=json.loads((ROOT/'pre-run-contract.json').read_text())
    for name,digest in contract['files_sha256'].items():
        if sha(ROOT/name)!=digest: raise ValueError('Reference source differs from pre-run contract: '+name)
    arrays={};meta=[]
    for ny in (80,160):
        stem=f'forward-step-ny{ny}'; raw=a.raw_dir/(stem+'.f64');m=json.loads((a.raw_dir/(stem+'.json')).read_text())
        q=np.fromfile(raw,dtype=np.float64).reshape(3*ny,ny,4)
        ii,jj=np.indices((3*ny,ny));fluid=~((ii>=3*ny//5)&(jj<ny//5))
        w=primitive(q)
        if not np.isfinite(w).all() or not (w[...,0][fluid]>0).all() or not (w[...,3][fluid]>0).all():raise ValueError('Inadmissible saved reference')
        if not m['passed'] or m['time']!=4. or m['ny']!=ny or m['rejected_steps']!=0 or m['state_floor_count']!=0:raise ValueError('Unexpected reference execution status')
        if max(m['conservation_relative'])>contract['acceptance']['maximum_relative_conservation_residual']:raise ValueError('Reference conservation gate failed')
        dest=a.output_dir/(stem+'.npz')
        if dest.exists() or dest.with_suffix('.json').exists():raise ValueError('Never overwrite reference fixtures')
        np.savez_compressed(dest,q=q,fluid=fluid,x=np.linspace(0,3,3*ny+1),y=np.linspace(0,1,ny+1),time=4.)
        m.update({'npz_sha256':sha(dest),'raw_state_sha256':sha(raw),'reference_source_sha256':sha(ROOT/'reference.cpp'),'pre_run_contract_sha256':sha(ROOT/'pre-run-contract.json'),'array_interpretation':'q[x,y,4] finite-volume cell averages; dummy solid states excluded from norms','method':'independent C++17 primitive-MUSCL generalized minmod theta1.5 / HLL / Heun','diagnostics':{'rejected_steps':0,'state_floor_count':0,'slope_rescalings':m['slope_rescalings']},'new_reference_pde_executed':True})
        save(dest.with_suffix('.json'),m);arrays[ny]=q;meta.append({'file':dest.name,'sha256':sha(dest),'metadata_sha256':sha(dest.with_suffix('.json')),'steps':m['steps'],'wall_seconds':m['wall_seconds'],'min_density':float(w[...,0][fluid].min()),'min_pressure':float(w[...,3][fluid].min())})
    ii,jj=np.indices((240,80));fluid=~((ii>=48)&(jj<16))
    coarse=primitive(arrays[80]);fine=primitive(restrict(arrays[160],80))
    diffs={k:float(np.sum(np.abs(coarse[...,idx][fluid]-fine[...,idx][fluid]))/np.sum(np.abs(fine[...,idx][fluid]))) for k,idx in [('density_l1',0),('pressure_l1',3)]}
    quality={'schema_version':1,'passed':True,'reference_kind':'independent-finite-grid-numerical','method':'independent C++17 primitive-MUSCL theta1.5/HLL/Heun','comparison':'Ny80 versus conservatively restricted Ny160 q on fluid cells; pressure computed after restriction','reference_increment':diffs,'files':meta,'new_reference_pde_executed':True,'corner_entropy_reset':False,'primary_operator_imports':False,'limitations':['Finite-grid difference is not an error bound or an exact2D solution.','No Woodward--Colella corner entropy/enthalpy reset; corner numerical entropy affects the reflected flow.','Both primary and reference share HLL/Heun families, while source language and reconstruction are independent.']}
    save(a.output_dir/'quality.json',quality)
    print(json.dumps({'converted':2,'reference_increment':diffs,'gate_evaluation':'Primary source evaluates its own predeclared reference criteria; converter checks reference integrity/admissibility/conservation only.'}))
if __name__=='__main__':main()
