"""Fixed continuum-angle reference generation/qualification; no primary imports."""
import argparse,json,hashlib
from pathlib import Path
import numpy as np
from scipy.integrate import quad
from scipy.special import expn
from fredholm import solution

PARAMETERS=[(.5,.5),(.5,.9),(3.,.5),(3.,.9)]

def main():
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    if a.output.exists() and any(a.output.iterdir()):raise ValueError('Fresh reference output required')
    a.output.mkdir(parents=True,exist_ok=True);checks={};details=[];cache=[]
    def add(key,value,bound):checks[key]=bool(value<=bound);details.append(dict(name=key,value=float(value),bound=bound,passed=checks[key]))
    # Independent binary-fraction scalar-sum goldens; no BLAS matmul call.
    matrix=np.array([[1.,2.,-1.,.5],[.25,-2.,4.,1.],[-.5,1.,.25,2.]])
    vector=np.array([.25,-.5,2.,1.])
    golden=np.array([sum(float(matrix[i,j])*float(vector[j]) for j in range(4)) for i in range(3)])
    add('safe-contraction/matrix-vector',np.max(abs(np.einsum('ij,j->i',matrix,vector,optimize=False)-golden)),0.)
    for k,row in enumerate([np.array([.25,-.5,2.]),np.array([-1.,.5,.25])]):
        golden=np.array([sum(float(row[i])*float(matrix[i,j]) for i in range(3)) for j in range(4)])
        add('safe-contraction/row-matrix/'+str(k),np.max(abs(np.einsum('i,ij->j',row,matrix,optimize=False)-golden)),0.)
    for depth,albedo in PARAMETERS:
        answers={};label=f'L{depth}-w{albedo}'
        for linear,cells in [(False,256),(False,512),(False,1024),(True,256),(True,512)]:
            name=('linear' if linear else 'constant')+str(cells);r=solution(depth,albedo,cells,linear)
            np.savez(a.output/(label+'-'+name+'.npz'),**r)
            add(label+'/'+name+'/finite-positive',0. if all(np.isfinite(v).all() for v in r.values()) and r['scalar'].min()>=-1e-12 else 1.,0.)
            add(label+'/'+name+'/residual',r['residual'],1e-10);add(label+'/'+name+'/budget',r['balance'],5e-4)
            answers[name]=np.array([r[k] for k in ['R','T','A']])
            (a.output/'completed.json').write_text(json.dumps(details,indent=2)+'\n')
        for key,one,two in [('constant-refinement','constant512','constant1024'),('linear-refinement','linear256','linear512'),('independent-basis','constant1024','linear512')]:add(label+'/'+key,np.max(abs(answers[one]-answers[two])),2e-4)
        cache.append(answers['linear512'])
    for h in [.5/256,3/256,3/1024]:
        direct=2*quad(lambda z:float(expn(1,z)),0,h/2,epsabs=1e-12,epsrel=1e-12)[0]
        add('independent-E1-diagonal-'+str(h),abs(direct-2*(1-expn(2,h/2))),1e-10)
    np.savez(a.output/'reference-cache.npz',parameters=np.array(PARAMETERS),fluxes=np.array(cache))
    result=dict(passed=all(checks.values()),checks=checks,check_count=len(checks),details=details,scope='Continuum Fredholm reference with exact singular-cell weights,two scalar bases and fixed refinements;empirical finite-reference sensitivity,not a rigorous continuum error bound.',PDE_primary_runs=0)
    (a.output/'qualification.json').write_text(json.dumps(result,indent=2,allow_nan=False)+'\n');print(json.dumps({'passed':result['passed'],'checks':len(checks)}))
    if not result['passed']:raise SystemExit(1)
if __name__=='__main__':main()
