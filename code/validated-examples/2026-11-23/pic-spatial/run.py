#!/usr/bin/env python3
"""Independent scalar CIC/dense-DFT spatial pipeline against vectorized PIC."""
import argparse,csv,hashlib,json,time
from datetime import datetime,timezone
from pathlib import Path
import numpy as np
import primary
from references import scalar_pic
ROOT=Path(__file__).resolve().parent

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def save(path,value):Path(path).write_text(json.dumps(value,ensure_ascii=False,indent=2,allow_nan=False)+'\n')
def maximum(a,b):return float(np.max(abs(a-b)))

def fixture():
    n=8;length=2*np.pi;x=np.repeat(np.arange(n)*length/n,[3,2,1,2,3,2,1,2]);return n,length,x


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--input',type=Path,required=True);p.add_argument('--output',type=Path,required=True);args=p.parse_args()
    if args.output.exists():raise ValueError('Fresh output required')
    args.output.mkdir(parents=True);cfg=json.loads(args.input.read_text());lim=json.loads((ROOT/'acceptance.json').read_text());contract=json.loads((ROOT/'pre-run-contract.json').read_text())
    for name,digest in contract['files_sha256'].items():
        if sha(ROOT/name)!=digest:raise ValueError('Frozen source changed: '+name)
    if sha(args.input)!=contract['files_sha256']['inputs.json']:raise ValueError('Input differs from frozen experiment')
    start=time.monotonic();checks={};gates=[];rows=[];failure=None
    def add(name,value,bound,ok):checks[name]=bool(ok);gates.append(dict(name=name,value=value,bound=bound,passed=bool(ok)))
    try:
        n,length,x=fixture();expected_e=-.25*np.sin(2*np.arange(n)*length/n);expected_a=.25*np.sin(2*x);expected_r=-.5*np.cos(2*np.arange(n)*length/n)
        for name,method in [('primary',primary.field),('independent',scalar_pic.field)]:
            a,e,r,*_=method(x,n,length);errors=[maximum(a,expected_a),maximum(e,expected_e),maximum(r,expected_r)];add(name+' analytic charge field electron-sign fixture',errors,lim['analytic_fixture_absolute'],max(errors)<=lim['analytic_fixture_absolute'])
        wrong,*_=scalar_pic.field(x,n,length,wrong_sign=True);error=maximum(wrong,expected_a);add('deliberate wrong electron sign is detected',error,lim['wrong_sign_minimum_error'],error>=lim['wrong_sign_minimum_error'])
        # Genuine odd-grid and positive unequal-weight operator comparisons.
        rng=np.random.default_rng(35000);xp=rng.uniform(0,cfg['length'],cfg['particles']);weights=rng.uniform(.5,1.5,len(xp));weights*=cfg['length']/weights.sum()
        for n,w,label in [(15,None,'odd-grid'),(16,weights,'positive-weight')]:
            ap,ep,rp,_=primary.field(xp,n,cfg['length'],w);ar,er,rr=scalar_pic.field(xp,n,cfg['length'],w)
            for key,value,bound in [('force',maximum(ap,ar),lim['force_absolute']),('field',maximum(ep,er),lim['field_absolute']),('charge',maximum(rp,rr),lim['charge_absolute'])]:add(label+' '+key,value,bound,value<=bound)
        steps=int(round(cfg['final_time']/cfg['dt']))
        for n in cfg['grids']:
            for seed in cfg['seeds']:
                if time.monotonic()-start>cfg['main_budget_seconds']:raise TimeoutError('Shared fixed budget')
                rng=np.random.default_rng(seed);x=rng.uniform(0,cfg['length'],cfg['particles']);v=.2*rng.normal(size=len(x))+.1*np.sin(x)
                pstate=primary.advance(x.copy(),v.copy(),n,cfg['length'],cfg['dt'],cfg['final_time'],deadline=start+cfg['main_budget_seconds'],save_every_step=True)
                rstate=scalar_pic.advance(x.copy(),v.copy(),n,cfg['length'],cfg['dt'],steps)
                name=f'n{n}-seed{seed}';filename=name+'.npz';arrays=dict(x_initial=x,v_initial=v,primary_x=pstate['x_history'],primary_v=pstate['v_history'],primary_electric=pstate['electric_history'],primary_charge=pstate['rho_history'],reference_x=rstate['x'],reference_v=rstate['v'],reference_electric=rstate['electric'],reference_charge=rstate['charge'],times=rstate['times'],primary_history=pstate['history'],history_columns=pstate['history_columns'])
                np.savez_compressed(args.output/filename,**arrays)
                errors=dict(position=maximum(arrays['primary_x'],arrays['reference_x']),velocity=maximum(arrays['primary_v'],arrays['reference_v']),field=maximum(arrays['primary_electric'],arrays['reference_electric']),charge=maximum(arrays['primary_charge'],arrays['reference_charge']))
                finite=bool(all(np.isfinite(a).all() for key,a in arrays.items() if key!='history_columns'));add(name+' all saved arrays finite',finite,True,finite)
                for key,boundkey in [('position','trajectory_position_absolute'),('velocity','trajectory_velocity_absolute'),('field','trajectory_field_absolute'),('charge','trajectory_charge_absolute')]:add(name+' all-step '+key,errors[key],lim[boundkey],errors[key]<=lim[boundkey])
                q=float(np.max(abs(np.sum(arrays['reference_charge'],axis=1)))*cfg['length']/n);momentum=float(np.max(abs(np.mean(arrays['reference_v'],axis=1)-np.mean(v))));add(name+' independent charge conservation',q,lim['charge_integral_absolute'],q<=lim['charge_integral_absolute']);add(name+' independent momentum conservation',momentum,lim['momentum_absolute'],momentum<=lim['momentum_absolute'])
                same=bool(np.array_equal(pstate['snapshot_times'],rstate['times']) and len(rstate['times'])==steps+1 and rstate['times'][-1]==cfg['final_time']);add(name+' own fields at every fixed kick',len(rstate['times']),steps+1,same)
                row=dict(id=name,n=n,seed=seed,particles=len(x),steps=steps,file=filename,sha256=sha(args.output/filename),**errors,charge_integral=q,momentum=momentum);rows.append(row);save(args.output/'completed-runs.json',rows)
        add('six paired comparisons equal twelve separate trajectories',len(rows)*2,12,len(rows)==6)
        with (args.output/'pic-independent-spatial.csv').open('w',newline='') as handle:
            columns=['id','n','seed','particles','steps','position','velocity','field','charge','charge_integral','momentum'];writer=csv.DictWriter(handle,fieldnames=columns,extrasaction='ignore');writer.writeheader();writer.writerows(rows)
    except Exception as error:
        failure=dict(type=type(error).__name__,message=str(error))
        if isinstance(error,primary.ParticleFailure):np.savez_compressed(args.output/'failed-stage.npz',x=error.x,v=error.v);failure['stage']=error.context
    passed=failure is None and len(rows)==6 and all(checks.values());case=dict(id='pic-independent-spatial',passed=passed,checks=checks,gates=gates,records=rows,metrics=dict(comparison_pairs=len(rows),separate_trajectories=2*len(rows),saved_states_per_trajectory=int(round(cfg['final_time']/cfg['dt']))+1,maximum_position_discrepancy=max((r['position'] for r in rows),default=0.),maximum_velocity_discrepancy=max((r['velocity'] for r in rows),default=0.),maximum_field_discrepancy=max((r['field'] for r in rows),default=0.),maximum_charge_discrepancy=max((r['charge'] for r in rows),default=0.)))
    result=dict(schema_version=1,group='pic-spatial',input_sha256=sha(args.input),passed=passed,termination='fixed_budget_completed' if failure is None else 'scientific_failure',failure=failure,checks={'pic-independent-spatial':passed},cases=[case],duration_seconds=time.monotonic()-start,created_at_utc=datetime.now(timezone.utc).isoformat())
    save(args.output/'result.json',result);print(json.dumps(dict(passed=passed,gates=len(checks),pairs=len(rows),failed=[k for k,v in checks.items() if not v],failure=failure)),flush=True);return 0 if passed else 1


if __name__=='__main__':raise SystemExit(main())
