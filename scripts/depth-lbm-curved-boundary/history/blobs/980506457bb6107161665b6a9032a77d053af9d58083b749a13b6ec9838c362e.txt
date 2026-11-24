"""Fixed scalar/native boundary qualification; no multistep physical evolution."""
import argparse
import hashlib,json
from pathlib import Path
import time,traceback
import numpy as np
from geometry import build,C,W,OPP,equilibrium,moments
from native import Native,NativeFailure
from reference_step import step as scalar_step

ROOT=Path(__file__).resolve().parent
def dump(path,value):Path(path).write_text(json.dumps(value,ensure_ascii=False,indent=2,allow_nan=False)+'\n')
def totals(f):return np.r_[np.sum(f),np.sum(np.einsum('qd,qn->dn',C,f),axis=1)]

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,required=True);args=parser.parse_args()
    protocol=json.loads((ROOT.parent/'protocol.json').read_text())
    for name,value in protocol['files_sha256'].items():
        if hashlib.sha256((ROOT.parent/name).read_bytes()).hexdigest()!=value:raise ValueError('Frozen repair component changed: '+name)
    if args.output.exists():raise ValueError('Fresh output required')
    args.output.mkdir(parents=True);checks={};records=[];native=None;failure=None;start=time.monotonic()
    def gate(name,passed,**record):
        checks[name]=bool(passed);records.append(dict(name=name,passed=bool(passed),**record))
        dump(args.output/'partial-result.json',dict(checks=checks,records=records))
    def initial(g):
        x=np.arange(g['n']);return equilibrium(1+.001*np.sin(.317*x),np.array([.002*np.cos(.193*x),.001*np.sin(.271*x)]))
    def compare(label,g):
        before=initial(g);expected=scalar_step(before,g,.8);actual=before.copy();h=native.advance(actual,g,.8,1)
        defect=(totals(actual)-totals(before)-h[0,3:6])/g['n']
        np.savez_compressed(args.output/(label+'.npz'),before=before,expected=expected,actual=actual,history=h,
                            kind=g['kind'],fraction=g['fraction'],back=g['back'],back2=g['back2'])
        gate(label+' scalar-native',float(np.max(abs(actual-expected)))<=4e-15,error=float(np.max(abs(actual-expected))))
        gate(label+' mass ledger',abs(float(defect[0]))<=3e-14)
        gate(label+' momentum ledger',float(np.max(abs(defect[1:])))<=3e-14)
        return before,actual,h
    def artificial(q,order=2):
        g=build('couette',5,.2,.01,interpolation_order=order)
        wall=g['kind']>0;g['kind'][wall]=2;g['fraction'][wall]=q
        return g
    try:
        native=Native();dump(args.output/'compiler.json',native.compile_receipt)
        gate('strict C++17 compile',native.compile_receipt['returncode']==0)
        for family,n,dx in [('periodic',5,1/5),('cavity',5,.2),('annulus',20,.05)]:
            compare('legacy-'+family,build(family,n,dx,.01))
        g=build('cylinder',0,.01,.001,interpolation_order=2,outlet_mode='nee')
        cylinder_before,cylinder_after,cylinder_h=compare('quadratic-NEE-cylinder',g)
        compare('quadratic-annulus',build('annulus',20,.05,.01,interpolation_order=2))
        for q in protocol['q_probes']:
            fixture=artificial(q);before=initial(fixture);expected=scalar_step(before,fixture,.8);actual=before.copy()
            h=native.advance(actual,fixture,.8,1)
            error=float(np.max(abs(actual-expected)));defect=(totals(actual)-totals(before)-h[0,3:6])/fixture['n']
            gate(f'{q}/scalar-native',error<=4e-15,error=error)
            gate(f'{q}/full ledger',float(np.max(abs(defect)))<=3e-14)
            for degree in [0,1,2]:
                if q<.5:
                    coefficients=np.array([q*(1+2*q),1-4*q*q,-q*(1-2*q)])
                    locations=np.array([0.,-1.,-2.]);target=(2*q-1)**degree
                else:
                    coefficients=np.array([1/(q*(2*q+1)),(2*q-1)/q,-(2*q-1)/(2*q+1)])
                    locations=np.array([2*q-1.,-1.,-2.]);target=1. if degree==0 else 0.
                value=float(np.sum(coefficients*locations**degree))
                gate(f'{q}/polynomial{degree}',abs(value-target)<=2e-14,value=value,target=target)
        for q in [.25,.5,.75]:
            fixture=artificial(q);wall=fixture['kind']>0;translation=np.array([.02,0.])
            for qi,ci in enumerate(C):fixture['wall_dot'][qi,wall[qi]]=float(np.sum(-ci*translation))
            f=equilibrium(np.ones(fixture['n']),np.tile(translation[:,None],(1,fixture['n'])));old=f.copy()
            h=native.advance(f,fixture,.8,1)
            gate(f'{q}/uniform moving-wall equilibrium',float(np.max(abs(f-old)))<=4e-16)
            gate(f'{q}/uniform moving-wall ledger',float(np.max(abs(totals(f)-totals(old)-h[0,3:6])))<=3e-14)
            fixture['wall_dot'][:]=0.;rest=equilibrium(np.ones(fixture['n']),np.zeros((2,fixture['n'])));oldrest=rest.copy()
            native.advance(rest,fixture,.8,1)
            gate(f'{q}/stationary limit',float(np.max(abs(rest-oldrest)))<=4e-16)
        fixture=artificial(.5);f=initial(fixture);quad=f.copy();native.advance(quad,fixture,.8,1)
        fixture['interpolation_order']=1;linear=f.copy();native.advance(linear,fixture,.8,1)
        gate('half-link quadratic equals legacy halfway',float(np.max(abs(quad-linear)))<=3e-15)
        outputs=[]
        for q in [.5-1e-10,.5+1e-10]:
            fixture=artificial(q);f=initial(fixture);native.advance(f,fixture,.8,1);outputs.append(f)
        gate('half-link branch continuity',float(np.max(abs(outputs[0]-outputs[1])))<=1e-10)
        gate('negative quadratic weights explicitly retained',-.25*(1-2*.25)<0 and -(2*.75-1)/(2*.75+1)<0)
        rho,u=moments(cylinder_after);boundary=g['outlet'];interior=g['source'][1,boundary]
        gate('NEE prescribed density all boundary rows',float(np.max(abs(rho[boundary]-1)))<=4e-15)
        gate('NEE adjacent poststream velocity all rows',float(np.max(abs(u[:,boundary]-u[:,interior])))<=4e-15)
        oldg=build('cylinder',0,.01,.001,interpolation_order=2,outlet_mode='zou-he')
        old=cylinder_before.copy();native.advance(old,oldg,.8,1)
        known=np.array([0,1,2,4,5,8]);delta=cylinder_after[known[:,None],boundary]-old[known[:,None],boundary]
        omitted=np.r_[np.sum(delta),np.sum(C[known,0,None]*delta),np.sum(C[known,1,None]*delta)]
        gate('NEE actually replaces known six',float(np.max(abs(delta)))>1e-8)
        actual_defect=totals(cylinder_after)-totals(cylinder_before)-cylinder_h[0,3:6]
        gate('omitting known-six ledger is detected',float(np.max(abs(actual_defect+omitted)))/g['n']>3e-14)
        gate('outlet corner owns full node without wrap',bool(np.all(g['ix'][boundary]-g['ix'][interior]==1) and
             np.all(g['iy'][boundary]==g['iy'][interior]) and g['iy'][boundary[0]]==0 and g['iy'][boundary[-1]]==40))
        for family,n,dx in [('annulus',40,1/40),('annulus',60,1/60),('annulus',80,1/80),('cylinder',0,.01),('cylinder',0,.005)]:
            geom=build(family,n,dx,dx/6,interpolation_order=2,outlet_mode='nee')
            curved=(geom['kind']>=2)&(geom['kind']<=3);short=curved&(geom['fraction']<.5)
            long=curved&(geom['fraction']>.5);support=bool(np.all(geom['back'][short|long]>=0) and np.all(geom['back2'][short]>=0))
            gate(f'{family}-{n}-{dx}/actual fixed stencil support',support,
                 short_links=int(np.count_nonzero(short)),long_links=int(np.count_nonzero(long)))
        fixture=artificial(.25);bad=int(np.flatnonzero(fixture['kind'].ravel()>0)[0]);fixture['back2'].ravel()[bad]=-1
        caught=False
        try:native.advance(initial(fixture),fixture,.8,1)
        except NativeFailure as error:
            caught=True;np.savez_compressed(args.output/'intended-missing-neighbor.npz',**error.payload)
        gate('missing second neighbor rejects without fallback',caught)
        fixture=artificial(.25);broken=initial(fixture);broken[:,0]=-1.;caught=False
        try:native.advance(broken,fixture,.8,1)
        except NativeFailure as error:
            caught=True;np.savez_compressed(args.output/'intended-invalid-density.npz',**error.payload)
        gate('nonpositive density rejects without floor',caught)
        short_linear=.5 # P0=0,P(-1)=1 at q=.25 ->.5, while P(-.5)=.25
        long_linear=.25/(2*.75)+(2*.75-1)/(2*.75) # P(.5)=.25,P(-1)=1 ->.5, while P0=0
        gate('old linear fails quadratic reproduction negative control',abs(short_linear-.25)>.01 and abs(long_linear)>.01)
        timings={}
        for family,n,dx in [('annulus',80,1/80),('cylinder',0,.005)]:
            geom=build(family,n,dx,dx/6,interpolation_order=2,outlet_mode='nee');base=initial(geom);candidate=base.copy()
            begin=time.monotonic()
            for _ in range(16):candidate[:]=base;native.advance(candidate,geom,.8,1)
            timings[family]=(time.monotonic()-begin)/16
        projection=timings['cylinder']*(18000/4+36000)+timings['annulus']*2*(960/4+2160*(60/80)**2+3840)
        gate('fixed curved workload projection <=40s',projection<=40,estimated_seconds=projection)
        dump(args.output/'timing.json',dict(reset_single_step_calls=16,per_call=timings,projected_main_seconds=projection,
             scope='No trajectory; conservative reset-one-step projection,not measured main/Linux runtime.'))
    except Exception as error:
        failure=dict(type=type(error).__name__,message=str(error));(args.output/'traceback.txt').write_text(traceback.format_exc())
        if getattr(error,'receipt',None):dump(args.output/'compiler.json',error.receipt)
        if getattr(error,'payload',None):np.savez_compressed(args.output/'failed-candidate.npz',**error.payload)
    finally:
        if native is not None:native.close()
    expected=protocol['planned_check_names'];passed=failure is None and set(checks)==set(expected) and len(checks)==len(expected) and all(checks.values())
    result=dict(passed=bool(passed),checks=checks,records=records,failure=failure,check_count=len(checks),
                expected_checks=len(expected),protocol_sha256=hashlib.sha256((ROOT.parent/'protocol.json').read_bytes()).hexdigest(),
                missing=sorted(set(expected)-set(checks)),unexpected=sorted(set(checks)-set(expected)),
                elapsed_seconds=time.monotonic()-start,physical_trajectories=0,reference_generations=0)
    dump(args.output/'result.json',result);print(json.dumps(dict(passed=bool(passed),checks=len(checks),failure=failure,missing=result['missing'])))
    return 0 if passed else 1

if __name__=='__main__':raise SystemExit(main())
