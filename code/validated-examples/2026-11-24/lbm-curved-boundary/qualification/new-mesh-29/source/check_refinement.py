"""Frozen two-new-mesh geometry/one-step qualification, not a physical trajectory."""
import argparse,hashlib,json,time,traceback
from pathlib import Path
import numpy as np
from geometry import build,equilibrium,C,moments
from native import Native
from reference_step import step as scalar_step
D=Path(__file__).resolve().parent.parent
def dump(p,x):Path(p).write_text(json.dumps(x,ensure_ascii=False,indent=2,allow_nan=False)+'\n')
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def totals(f):return np.r_[np.sum(f),np.sum(np.einsum('qd,qn->dn',C,f),axis=1)]
def main():
 parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,required=True);args=parser.parse_args();plan=json.loads((D/'protocol.json').read_text())
 for path,value in plan['files_sha256'].items():
  if sha(D/path)!=value:raise ValueError('Frozen component changed:'+path)
 for r in plan['evidence'].values():
  if sha(r['path'])!=r['sha256']:raise ValueError('Frozen evidence changed:'+r['path'])
 if args.output.exists():raise ValueError('Fresh output required')
 args.output.mkdir(parents=True);checks={};records=[];timings=[];native=None;failure=None;start=time.monotonic()
 def gate(name,passed,**row):
  checks[name]=bool(passed);records.append(dict(name=name,passed=bool(passed),**row));dump(args.output/'partial-result.json',dict(checks=checks,records=records,timings=timings))
 try:
  native=Native();dump(args.output/'compiler.json',native.compile_receipt);gate('strict C++17 compile',native.compile_receipt['returncode']==0)
  for n in plan['new_N']:
   for variant in [0,1]:
    dx=1/n;dt=(.7-.5)/3*dx*dx/.01;label=f'N{n}-variant{variant}'
    g=build('annulus',n,dx,dt,inner_speed=.02,stair=bool(variant),interpolation_order=2)
    curved=(g['kind']>=2)&(g['kind']<=3);short=curved&(g['fraction']<.5);long=curved&(g['fraction']>.5)
    gate(label+' true-circle/stair fractions',bool(np.any(curved) and np.all(g['fraction'][curved]>0) and np.all(g['fraction'][curved]<=1) and (not variant or np.all(g['fraction'][curved]==.5))))
    gate(label+' required stencil support',bool(np.all(g['back'][short|long]>=0) and np.all(g['back2'][short]>=0)),short_links=int(np.count_nonzero(short)),long_links=int(np.count_nonzero(long)))
    x=np.arange(g['n']);f0=equilibrium(1+.001*np.sin(.317*x),np.array([.002*np.cos(.193*x),.001*np.sin(.271*x)]))
    oracle=scalar_step(f0,g,.7);actual=f0.copy();h=native.advance(actual,g,.7,1);rho,u=moments(actual)
    defect=(totals(actual)-totals(f0)-h[0,3:6])/g['n'];error=float(np.max(abs(actual-oracle)))
    np.savez_compressed(args.output/(label+'.npz'),f0=f0,oracle=oracle,actual=actual,history=h,back=g['back'],back2=g['back2'],kind=g['kind'],fraction=g['fraction'],x=g['x'],y=g['y'])
    gate(label+' scalar-native one-step',error<=4e-15,error=error)
    gate(label+' mass ledger',abs(float(defect[0]))<=3e-14)
    gate(label+' momentum ledger',float(np.max(abs(defect[1:])))<=3e-14)
    gate(label+' finite positive one-step density',bool(np.all(np.isfinite(actual)) and np.all(np.isfinite(h)) and np.min(rho)>0))
    candidate=f0.copy();repeats=plan['reset_calls_per_geometry'];zero=[];one=[];same=True
    # Interleaved fixed blocks; zero-step allocation is diagnostic only, never a physics run.
    for block in range(3):
     begin=time.monotonic()
     for _ in range(repeats):candidate[:]=f0;native.advance(candidate,g,.7,0)
     zero.append((time.monotonic()-begin)/repeats)
     begin=time.monotonic()
     for _ in range(repeats):
      candidate[:]=f0;native.advance(candidate,g,.7,1);same=bool(same and np.array_equal(candidate,actual))
     one.append((time.monotonic()-begin)/repeats)
    timings.append(dict(n=n,variant=variant,fluid_nodes=g['n'],main_steps=3*n*n//5,one_step_seconds=one,zero_step_allocation_seconds=zero,median_one_step_seconds=float(np.median(one)),median_zero_step_seconds=float(np.median(zero))))
    gate(label+' every reset reproduces identical single-step',same)
  old=plan['planning_baseline'];small=old['old_N80_reset_one_step_seconds']*3840*2
  raw=small+sum(r['median_one_step_seconds']*r['main_steps'] for r in timings)
  marginal=small+sum(max(0,r['median_one_step_seconds']-r['median_zero_step_seconds'])*r['main_steps'] for r in timings)
  projection=dict(annulus_both_variants_raw_reset_projection_seconds=raw,
   annulus_marginal_step_diagnostic_seconds=marginal,
   full_group_raw_reset_shared_projection_seconds=raw+old['R3_non_annular_main_planning_seconds']+old['R3_pytest_seconds'],
   full_group_marginal_step_diagnostic_seconds=marginal+old['R3_non_annular_main_planning_seconds']+old['R3_pytest_seconds'],
   scope='Planning diagnostics only; raw reset includes per-call allocations unlike chunkedmain,zero-step subtraction is not a rigorous runtime bound; no Linuxmeasurement or mainPASSclaim. Mainauthorization remains separate.')
  dump(args.output/'timing.json',dict(timings=timings,projection=projection))
 except Exception as e:
  failure=dict(type=type(e).__name__,message=str(e));(args.output/'traceback.txt').write_text(traceback.format_exc())
  if getattr(e,'receipt',None):dump(args.output/'compiler.json',e.receipt)
  if getattr(e,'payload',None):np.savez_compressed(args.output/'failed-candidate.npz',**e.payload)
 finally:
  if native is not None:native.close()
 expected=plan['planned_check_names'];passed=failure is None and set(checks)==set(expected) and len(checks)==len(expected) and all(checks.values())
 dump(args.output/'result.json',dict(passed=bool(passed),checks=checks,records=records,timings=timings,failure=failure,check_count=len(checks),expected_checks=len(expected),protocol_sha256=sha(D/'protocol.json'),physical_trajectories=0,reference_generations=0,elapsed_seconds=time.monotonic()-start))
 print(json.dumps(dict(passed=bool(passed),checks=len(checks),failure=failure)));return 0 if passed else 1
if __name__=='__main__':raise SystemExit(main())
