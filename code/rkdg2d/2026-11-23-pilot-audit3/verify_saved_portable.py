#!/usr/bin/env python3
"""Supervisor re-evaluation: unchanged frozen evaluators + raw-array metrics.

No solver evolution is launched here. This is additional evidence integrity,
not a replacement or relaxation of the original scientific acceptance rules.
"""
from pathlib import Path
import argparse, hashlib, importlib.util, json, subprocess, sys, datetime
from types import SimpleNamespace
import numpy as np
from numpy.polynomial.legendre import leggauss

EXP=Path(__file__).resolve().parent
TRUST=EXP/'trusted/atlas-rkdg-agent-kit'

def digest(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def js(p):return json.loads(Path(p).read_text())
def protected(kit):
 bad=[];count=0
 for line in (kit/'SHA256SUMS.txt').read_text().splitlines():
  sha,name=line.split(maxsplit=1);p=kit/name.strip().lstrip('*');count+=1
  if not p.is_file() or digest(p)!=sha:bad.append(str(p.relative_to(kit)))
 return {'checked':count,'changed':bad}

def main():
 p=argparse.ArgumentParser();p.add_argument('--bundle',type=Path,required=True);p.add_argument('--trial',choices=['assembly','repair'],required=True);p.add_argument('--base',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args();global TRUST,EXP;TRUST=a.base.resolve();EXP=a.bundle.resolve()
 kit=TRUST;campaign=EXP/'trials'/a.trial;candidate=campaign/'candidate.py';negative=campaign/'negative'
 out=a.output.resolve()/a.trial;out.mkdir(parents=True,exist_ok=False)
 report={'audit_version':3,'comparison_policy':'64eps relative plus 64eps absolute for nonzero dimensionless metrics; recorded zeros must remain exact. Scientific evaluator criteria unchanged.','started_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'trial':a.trial,'candidate_sha256':digest(candidate),'candidate_protected':protected(kit),'trusted_protected':protected(TRUST),'fresh_pde_rerun_by_this_audit':False,'comparisons':[],'raw_arrays':[],'failures':[],'commands':[]}
 if report['candidate_protected']['changed'] or report['trusted_protected']['changed']:raise ValueError('Protected distribution changed')
 for name,args in [('original',[str(campaign/'metrics.json'),'--solver',str(candidate)]),('waveform',['--campaign',str(campaign),'--solver',str(candidate)])]:
  script=TRUST/'validation/rkdg'/('evaluate.py' if name=='original' else 'resolution.py')
  cmd=[sys.executable,str(script),*args,'--output',str(out/(name+'-verdict.json'))]
  r=subprocess.run(cmd,capture_output=True,text=True,cwd=TRUST)
  (out/(name+'.stdout')).write_text(r.stdout);(out/(name+'.stderr')).write_text(r.stderr)
  report['commands'].append({'name':name,'command':cmd,'exit_code':r.returncode})
  if r.returncode:report['failures'].append(name+' frozen evaluator FAIL')
 spec=importlib.util.spec_from_file_location('_trusted_campaign',TRUST/'scripts/run_rkdg_campaign.py');runner=importlib.util.module_from_spec(spec);spec.loader.exec_module(runner)
 m=js(campaign/'metrics.json');eps=64*np.finfo(float).eps
 def compare(label,actual,recorded):
  strict=bool(np.isfinite(actual) and np.isfinite(recorded) and np.isclose(actual,recorded,rtol=eps,atol=0))
  # Metrics are dimensionless in these fixed inputs. Subtraction of O(1)
  # reconstructed fields loses relative precision for near-zero error norms.
  # This integrity check uses an absolute floating-point floor; unchanged
  # frozen evaluators below retain every scientific acceptance threshold.
  ok=bool(np.isfinite(actual) and np.isfinite(recorded) and (actual==0 if recorded==0 else np.isclose(actual,recorded,rtol=eps,atol=eps)))
  report['comparisons'].append({'label':label,'actual':float(actual),'recorded':float(recorded),'matched':ok,'strict_relative_match':strict,'absolute_difference':float(abs(actual-recorded)),'absolute_tolerance':0. if recorded==0 else float(eps)})
  if not ok:report['failures'].append('raw metric mismatch: '+label)
 def load(name):
  path=campaign/'arrays'/(name+'.npz')
  with np.load(path,allow_pickle=False) as z:data={k:np.array(z[k]) for k in z.files}
  c=data['coeff'];cfg=json.loads(str(data['config']));diag=json.loads(str(data['diagnostics']))
  assert c.shape==(cfg['nx'],cfg['ny'],cfg['degree']+1,cfg['degree']+1,4)
  assert np.all(np.isfinite(c)) and np.array_equal(data['q'],c[:,:,0,0,:])
  # The unchanged distributed evolve() closes a remaining interval <=4eps
  # without another callback. Match that declared ledger contract, not bitwise time equality.
  closure_bound=4*np.finfo(float).eps*max(1.,abs(cfg['time']))
  callback_gap=float(data['step_times'][-1])-cfg['time']
  assert diag['final_time']==cfg['time'] and data['step_times'][0]==0
  assert abs(callback_gap)<=closure_bound
  assert np.all(np.diff(data['step_times'])>0)
  report['raw_arrays'].append({'file':name+'.npz','sha256':digest(path),'steps':int(diag['steps']),'wall_seconds':float(diag['wall_seconds']),'final_time':float(diag['final_time']),'cache_key':str(data['cache_key']),'callback_endpoint_gap':callback_gap,'callback_closure_bound':closure_bound})
  return data,c,cfg,diag
 refs=TRUST/'validation/rkdg/references'
 def ref(pattern):
  path=max(refs.glob(pattern),key=lambda f:np.load(f)['q'].size)
  with np.load(path,allow_pickle=False) as z:return {k:np.array(z[k]) for k in z.files}
 shu=ref('shu*.npz');dmr=ref('double-mach*.npz')
 coarse_path=sorted(refs.glob('double-mach*.npz'),key=lambda f:np.load(f)['q'].size)[-2]
 with np.load(coarse_path,allow_pickle=False) as z:coarse={k:np.array(z[k]) for k in z.files}
 uncertainty=runner.density_error(coarse['q'],runner.remap_2d(dmr,coarse['x_edges'],coarse['y_edges']))
 for row in m['smooth']:
  label=f'smooth-p{row["p"]}-n{row["n"]}';data,c,cfg,diag=load(label)
  errors=runner.modal_density_errors(c,runner.exact_entropy,time=row['time'])
  for norm,value in errors.items():compare(label+'/'+norm,value,row['errors'][norm])
  compare(label+'/conservation',runner.normalized_conservation(diag),row['conservation_defect'])
 orient={}
 for row in m['directional']:
  problem,pd,axis,n=[row[k] for k in ['problem','p','axis','n']];label=f'{problem}-p{pd}-a{axis}-n{n}'
  data,c,cfg,diag=load(label);profile=c[:,:,0,0,:].mean(axis=1-axis)
  if axis:profile=profile[:,[0,2,1,3]]
  ed=data['x_edges' if axis==0 else 'y_edges'];expected=runner.sod_average(ed,row['time']) if problem=='sod' else runner.remap_1d(shu,ed)
  compare(label+'/relative_l1',runner.density_error(profile,expected),row['error_l1'])
  transverse=c[:,:,:,1:,:] if axis==0 else c[:,:,1:,:,:]
  compare(label+'/transverse',max(np.max(abs(np.diff(c,axis=1-axis))),np.max(abs(transverse))),row['transverse'])
  compare(label+'/conservation',runner.normalized_conservation(diag),row['conservation_defect'])
  lo=runner.physical_minima(SimpleNamespace(z=np.empty(pd+2)),c)
  compare(label+'/density_min',lo[0],row['min_density']);compare(label+'/pressure_min',lo[1],row['min_pressure'])
  orient.setdefault((problem,pd,n),{})[axis]=(c if not axis else c.transpose(1,0,3,2,4)[...,[0,2,1,3]],row['axis_difference'])
 for key,axes in orient.items():
  delta=np.max(abs(axes[0][0]-axes[1][0]));compare(str(key)+'/axis_difference',delta,axes[0][1]);compare(str(key)+'/axis_difference_y',delta,axes[1][1])
 for row in m['double_mach']:
  label=f'double-mach-p{row["p"]}-ny{row["ny"]}';data,c,cfg,diag=load(label)
  compare(label+'/relative_l1',runner.density_error(data['q'],runner.remap_2d(dmr,data['x_edges'],data['y_edges'])),row['error_l1'])
  compare(label+'/reference_change',uncertainty,row['reference_grid_change_l1']);compare(label+'/conservation',runner.normalized_conservation(diag),row['conservation_defect'])
  lo=runner.physical_minima(SimpleNamespace(z=np.empty(row['p']+2)),c)
  compare(label+'/density_min',lo[0],row['min_density']);compare(label+'/pressure_min',lo[1],row['min_pressure'])
 temporal={}
 for factor in [1,2,4,8]:temporal[factor]=load('temporal-f'+str(factor))[1]
 z,w=leggauss(8);weights=w[:,None]*w[None,:]/4;reference=runner.reconstruct(temporal[8],z)[...,0]
 for row in m['temporal']:
  error=runner.reconstruct(temporal[row['factor']],z)[...,0]-reference
  compare('temporal-f'+str(row['factor'])+'/l2',np.sqrt(np.mean(np.sum(error**2*weights,axis=(-2,-1)))),row['error_l2'])
 evidence=js(negative/'evidence.json');control=js(negative/'control-row.json')
 assert evidence['original_solver_sha256']==digest(candidate)
 assert evidence['mutant_solver_sha256']==digest(negative/'wrong_y_flux.py')
 assert control['evidence_sha256']==digest(negative/'evidence.json')
 assert m['negative_controls']==[control]
 assert evidence['verdict']['valid_evidence'] and evidence['verdict']['rejected'] and control['rejected']
 assert m['solver_sha256']==digest(candidate)==report['candidate_sha256']
 assert {k:len(m[k]) for k in ['smooth','directional','double_mach','temporal','negative_controls']}=={'smooth':12,'directional':24,'double_mach':9,'temporal':3,'negative_controls':1}
 assert len(report['raw_arrays'])==49
 report['passed']=not report['failures'];report['completed_at_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
 (out/'report.json').write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
 print(json.dumps({'trial':a.trial,'passed':report['passed'],'raw_arrays':49,'comparisons':len(report['comparisons']),'failures':report['failures']}))
 return 0 if report['passed'] else 1
if __name__=='__main__':raise SystemExit(main())
