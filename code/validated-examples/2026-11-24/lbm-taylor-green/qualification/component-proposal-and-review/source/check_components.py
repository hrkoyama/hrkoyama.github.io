"""Fixed single-step qualification/timing only; no multistep physical evolution."""
import argparse
import hashlib
import json
from pathlib import Path
import time
import traceback
import numpy as np
from geometry import build,C,W,OPP,equilibrium,moments,circle_fraction
from native import Native,NativeFailure
from reference_step import step as scalar_step

ROOT=Path(__file__).resolve().parent

def dump(path,value):path.write_text(json.dumps(value,ensure_ascii=False,indent=2,allow_nan=False)+'\n')
def total(f):return np.r_[np.sum(f),np.sum(np.einsum('qd,qn->dn',C,f),axis=1)]

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,required=True);args=parser.parse_args()
    if args.output.exists():raise ValueError('Fresh output required')
    protocol=json.loads((ROOT.parent/'protocol.json').read_text())
    for name,digest in protocol['files_sha256'].items():
        if hashlib.sha256((ROOT.parent/name).read_bytes()).hexdigest()!=digest:raise ValueError('Frozen component source changed: '+name)
    args.output.mkdir(parents=True);checks={};records=[];failure=None;started=time.monotonic()
    def gate(name,value,**metrics):
        checks[name]=bool(value);records.append(dict(name=name,passed=bool(value),**metrics))
        dump(args.output/'partial-result.json',dict(passed=False,checks=checks,records=records))
    def state(g):
        i=np.arange(g['n'],dtype=float)
        rho=1+.001*np.sin(.317*i)
        u=np.array([.002*np.cos(.193*i),.001*np.sin(.271*i)])
        return equilibrium(rho,u)
    def compare(label,g,f,native):
        old=f.copy();expected=scalar_step(old,g,.8);actual=f.copy();h=native.advance(actual,g,.8,1)
        np.savez_compressed(args.output/(label+'.npz'),before=old,expected=expected,actual=actual,history=h,
                            source=g['source'],kind=g['kind'],fraction=g['fraction'])
        error=float(np.max(abs(actual-expected)));defect=total(actual)-total(old)-h[0,3:6]
        scale=max(g['n'],1)
        gate(label+' native-scalar',error<=3e-15,error=error)
        gate(label+' mass ledger',abs(float(defect[0]))/scale<=3e-14,scaled_defect=abs(float(defect[0]))/scale)
        gate(label+' momentum ledger',float(np.max(abs(defect[1:])))/scale<=3e-14,
             scaled_defect=float(np.max(abs(defect[1:])))/scale)
        return actual,h
    try:
        native=Native();dump(args.output/'compiler.json',native.compile_receipt)
        gate('strict C++17 compile',native.compile_receipt['returncode']==0)
        for family,n,dx,dt in [('periodic',5,2*np.pi/5,.01),('cavity',5,.2,.01),
                               ('couette',5,.2,.01),('annulus',20,.05,.01),('cylinder',0,.01,.001)]:
            g=build(family,n,dx,dt);compare(family,g,state(g),native)
        for d in [.1,.25,.5,.75,1.]:
            # x-periodic Couette has no corner link lacking its interior point.
            g=build('couette',5,.2,.01);g['fraction'][g['kind']>0]=d
            compare('fraction-'+str(d),g,state(g),native)
        for family,n,dx in [('periodic',5,1/5),('cavity',5,.2),('couette',5,.2),
                            ('annulus',20,.05),('cylinder',0,.01)]:
            g=build(family,n,dx,.001,lid=0.,inner_speed=0.);g['inlet_speed'][:]=0
            f=equilibrium(np.ones(g['n']),np.zeros((2,g['n'])));old=f.copy()
            h=native.advance(f,g,.8,1)
            gate(family+' rest populations',float(np.max(abs(f-old)))<=3e-16)
            gate(family+' rest wall-body impulse',float(np.max(abs(h[0,4:9])))<=2e-12)
        g=build('cavity',5,.2,.001,lid=.02);f=equilibrium(np.ones(g['n']),np.zeros((2,g['n'])))
        h=native.advance(f,g,.8,1)
        gate('rightward lid injects positive x momentum',float(h[0,4])>0)
        gate('moving-corner mass closure',abs(float(h[0,3]))<=2e-15)
        gate('moving-corner actual global mass',abs(float(np.sum(f))-g['n'])<=3e-14)
        g=build('cylinder',0,.01,.001);f0=state(g);f=f0.copy();native.advance(f,g,.8,1);r,u=moments(f)
        gate('inlet nominal horizontal velocity',float(np.max(abs(u[0,g['inlet']]-g['inlet_speed'])))<=3e-15)
        gate('inlet zero vertical velocity',float(np.max(abs(u[1,g['inlet']])))<=3e-15)
        gate('outlet prescribed density',float(np.max(abs(r[g['outlet']]-1)))<=3e-15)
        _,u0=moments(f0)
        gate('outlet tangential old-interior extrapolation',float(np.max(abs(u[1,g['outlet']]-u0[1,g['source'][1,g['outlet']]])))<=3e-15)
        for label,point,direction,expected in [('quarter',[1.1,0],[-.4,0],.25),
                                               ('half-inner',[1.1,0],[-.2,0],.5),
                                               ('half-outer',[.6,0],[.8,0],.5)]:
            q=circle_fraction(point,direction,np.zeros(2),1.)
            gate('analytic circle '+label,abs(q-expected)<=2e-15,actual=float(q))
        for bad in [.5,float('nan')]:
            caught=False
            try:native.advance(f,g,bad,1)
            except ValueError:caught=True
            gate('invalid tau '+('half' if bad==.5 else 'nan'),caught)
        broken=f.copy();broken[:,0]=-1.;caught=False;retained=False
        try:native.advance(broken,g,.8,1)
        except NativeFailure as error:
            caught=True;retained=error.payload['f'].shape==broken.shape
            np.savez_compressed(args.output/'intended-invalid-candidate.npz',**error.payload)
        gate('nonpositive density rejected without floor',caught)
        gate('failed candidate retained',retained)
        timings={}
        # Every timed call resets to the SAME state; these are not PDE trajectories.
        for family,n,dx,dt in [('cavity',32,1/32,.001),('annulus',80,1/80,1/960),
                               ('cylinder',0,.005,.005/6),('periodic',64,2*np.pi/64,.001)]:
            geom=build(family,n,dx,dt);base=state(geom);candidate=base.copy()
            begin=time.monotonic()
            for _ in range(16):
                candidate[:]=base;native.advance(candidate,geom,.8,1)
            elapsed=(time.monotonic()-begin)/16
            timings[family]=dict(nodes=geom['n'],one_step_seconds=elapsed,reset_calls=16,
                                 each_call_steps=1,physical_evolution_performed=False)
        # Conservative one-step cost includes an allocation/reset at every call;
        # actual main keeps its buffers within larger fixed chunks. This is only
        # a frozen workload estimate, not a main-time guarantee or scientific pass.
        cavity=timings['cavity']['one_step_seconds']*(60000*(24/32)**2+80000+120000*(48/32)**2)
        curved=timings['cylinder']['one_step_seconds']*(18000/4+36000)+timings['annulus']['one_step_seconds']*(2*(960/4+2160*(60/80)**2+3840))
        tgv=timings['periodic']['one_step_seconds']*(64/16+256/4+1024+256/4*2+512/4)
        gate('cavity frozen workload estimate <=25s',cavity<=25,estimated_seconds=cavity)
        gate('curved frozen workload estimate <=40s',curved<=40,estimated_seconds=curved)
        gate('TGV frozen workload estimate <=5s',tgv<=5,estimated_seconds=tgv)
        dump(args.output/'timings.json',dict(components=timings,estimates=dict(cavity=cavity,curved=curved,tgv=tgv),
             scope='UNEXECUTED-main projection from reset one-step operations; not a wall-time guarantee.'))
    except Exception as error:
        failure=dict(type=type(error).__name__,message=str(error));(args.output/'traceback.txt').write_text(traceback.format_exc())
        if getattr(error,'receipt',None):dump(args.output/'compiler.json',error.receipt)
        if getattr(error,'payload',None):np.savez_compressed(args.output/'failed-candidate.npz',**error.payload)
    passed=failure is None and len(checks)==protocol['planned_checks'] and all(checks.values())
    report=dict(passed=passed,protocol_sha256=hashlib.sha256((ROOT.parent/'protocol.json').read_bytes()).hexdigest(),
                checks=checks,check_count=len(checks),records=records,failure=failure,
                elapsed_seconds=time.monotonic()-started,main_PDE_executions=0,reference_generations=0)
    dump(args.output/'result.json',report);print(json.dumps(dict(passed=passed,checks=len(checks),failure=failure)))
    return 0 if passed else 1

if __name__=='__main__':raise SystemExit(main())
