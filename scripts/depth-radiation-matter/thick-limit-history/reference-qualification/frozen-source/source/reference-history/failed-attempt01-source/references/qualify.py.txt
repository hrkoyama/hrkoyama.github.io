"""Serial official1996integral sensitivity and pinned1997data qualification."""
import argparse,json,hashlib,importlib.util,importlib.machinery
from pathlib import Path
import numpy as np
from analytic import closed_step
HERE=Path(__file__).resolve().parent

def load(name,path):
    loader=importlib.machinery.SourceFileLoader(name,str(path));spec=importlib.util.spec_from_loader(name,loader);m=importlib.util.module_from_spec(spec);loader.exec_module(m);return m

def main():
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    if a.output.exists() and any(a.output.iterdir()):raise ValueError('Fresh reference output required')
    a.output.mkdir(parents=True,exist_ok=True);checks={};details=[]
    def add(key,value,bound):checks[key]=bool(value<=bound);details.append(dict(name=key,value=float(value),bound=bound,passed=checks[key]))
    original=load('official_exactpack_175',HERE/'exactpack-timmes.py.txt');tight=load('tight_exactpack_175',HERE/'exactpack-timmes-tight.py.txt')
    x=np.array([.125,.25,.5,1.,2.,4.,6.]);times=np.array([.1,1.,3.]);data=np.zeros((3,7,2))
    def evaluate(module,position,time):
        u=module.usolution(float(position),float(time),1.);v=module.vsolution(float(position),float(time),1.,u);return np.array([u,v])
    for it,t in enumerate(times):
        for ix,z in enumerate(x):
            base=evaluate(original,z,t);fine=evaluate(tight,z,t);data[it,ix]=fine
            add(f'diffusion/{it}/{ix}/finite-positive',0. if np.isfinite(fine).all() and fine.min()>=-2e-8 else 1.,0.)
            add(f'diffusion/{it}/{ix}/independent-tolerance-sensitivity',np.max(abs(fine-base)),2e-5)
            np.savez(a.output/'diffusion-partial.npz',x=x,times=times,values=data)
    # Independent finite-difference PDE/Robin residuals of the tightened integral.
    for z,t in [(.5,1.),(1.5,1.),(.5,3.)]:
        h=.02;k=.01;center=evaluate(tight,z,t);xm=evaluate(tight,z-h,t);xp=evaluate(tight,z+h,t);xmm=evaluate(tight,z-2*h,t);xpp=evaluate(tight,z+2*h,t)
        tm=evaluate(tight,z,t-k);tp=evaluate(tight,z,t+k);tmm=evaluate(tight,z,t-2*k);tpp=evaluate(tight,z,t+2*k)
        temporal=(tmm-8*tm+8*tp-tpp)/(12*k);second=(-xpp[0]+16*xp[0]-30*center[0]+16*xm[0]-xmm[0])/(12*h*h)
        add('diffusion/PDE/'+str((z,t)),max(abs(temporal[0]-second-center[1]+center[0]),abs(temporal[1]-center[0]+center[1])),1e-3)
    for t in [1.,3.]:
        h=.02;u=np.array([evaluate(tight,j*h,t)[0] for j in range(5)]);gradient=(-25*u[0]+48*u[1]-36*u[2]+16*u[3]-3*u[4])/(12*h)
        add('diffusion/Robin/'+str(t),abs(u[0]-2/np.sqrt(3)*gradient-1),1e-3)
    W=np.loadtxt(HERE/'SuOlson_W_transport.dat.txt');V=np.loadtxt(HERE/'SuOlson_V_transport.dat.txt');tx=np.loadtxt(HERE/'SuOlsonx.dat.txt');tt=np.loadtxt(HERE/'SuOlsont.dat.txt')
    add('transport/shape',0. if W.shape==V.shape==(15,7) and tx.shape==(15,) and tt.shape==(7,) else 1.,0.)
    add('transport/finite-positive',0. if np.isfinite(W).all() and np.isfinite(V).all() and min(W.min(),V.min())>=0 else 1.,0.)
    add('transport/unique-ordered-coordinates',0. if np.all(np.diff(tx)>0) and np.all(np.diff(tt)>0) else 1.,0.)
    add('transport/distinct-radiation-material',0. if np.max(abs(W-V))>.01 else 1.,0.)
    for j,t in enumerate(tt[:2]):
        mask=tx+t<.49;u,v=closed_step(0.,0.,float(t),1.,1.)
        add('transport/closed-homogeneous-normalization/'+str(j),max(np.max(abs(W[mask,j]-u)),np.max(abs(V[mask,j]-v))),2e-4)
    causal=tx[:,None]>.5+tt[None,:]
    add('transport/causal-zero',max(np.max(abs(W[causal])),np.max(abs(V[causal]))),5e-5)
    selected_times=np.array([0,2,3]);selected_x=tx<6
    np.savez(a.output/'diffusion-reference.npz',x=x,times=times,values=data)
    np.savez(a.output/'transport-reference.npz',x=tx[selected_x],times=tt[selected_times],values=np.stack([W[selected_x][:,selected_times].T,V[selected_x][:,selected_times].T],axis=-1))
    result=dict(passed=all(checks.values()),checks=checks,check_count=len(checks),details=details,scope='1996official pinned integral sensitivity/PDE and1997author-provided analytical benchmark table. Original1997table not directly inspected; no primary S_Nreference generation.',PDE_primary_runs=0)
    (a.output/'qualification.json').write_text(json.dumps(result,indent=2,allow_nan=False)+'\n');print(json.dumps({'passed':result['passed'],'checks':len(checks)}))
    if not result['passed']:raise SystemExit(1)
if __name__=='__main__':main()
