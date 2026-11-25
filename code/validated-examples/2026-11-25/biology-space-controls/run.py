"""Execute the complete frozen fixed protocol; all references and failures retained."""
from __future__ import annotations
import argparse,csv,importlib,json,math,os
from pathlib import Path
from common import Budget,Recorder,assert_frozen,sha
MODULES = [('fisher-kpp-special-front', 'fisher', 'Fisher/'), ('schnakenberg-2d-boundary-modes', 'schnakenberg', 'Schnakenberg/'), ('keller-segel-forced-flux', 'keller_segel', 'KS/')]

def main(input_path,output,seconds=115):
    root=Path(__file__).resolve().parent
    assert_frozen(root)
    if not 0<float(seconds)<=115:raise ValueError('Fixedsharedcap0<seconds<=115required')
    if sha(input_path)!=sha(root/'inputs.json'):raise ValueError('Inputmustmatchreviewedfixedcontract')
    for key in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:
        if os.environ.get(key)!='1':raise ValueError(key+'=1required')
    inputs=json.loads(Path(input_path).read_text());budget=Budget(seconds);rec=Recorder(output,budget,root)
    rec.report['cases']=[]
    try:
        for case_id,module,prefix in MODULES:
            begin=len(rec.report['rows']);importlib.import_module(module).run(rec,budget,inputs)
            checks={k:v for k,v in rec.report['checks'].items() if k.startswith(prefix)}
            records=rec.report['rows'][begin:]
            if not checks or not records:raise ValueError('Emptycasequalification')
            metrics={'fixed_records':len(records)}
            for key,goal in rec.report['study_goals'].items():
                if not key.startswith(prefix):continue
                for label in ['actual','actual_ms','observed_margin','minimum']:
                    value=goal.get(label)
                    if isinstance(value,(int,float)) and not isinstance(value,bool) and math.isfinite(value):
                        metrics[key+'/'+label]=float(value)
            rec.report['cases'].append({'id':case_id,'passed':all(checks.values()),'checks':checks,
                'metrics':metrics,'records':records})
            rec.save()
        rec.check('all_fixed_case_ids', [x['id'] for x in rec.report['cases']]==inputs['case_ids'])
        assert_frozen(root)
        budget.tick('final_completion')
        rec.report['termination']='completed_fixed_protocol'
        rec.report['passed']=all(rec.report['checks'].values()) and all(x['passed'] for x in rec.report['cases'])
        rec.report['qualification_checks']=rec.report['checks']
        rec.report['checks']={c['id']:c['passed'] for c in rec.report['cases']}
        with (rec.output/'measurements.csv').open('w',newline='') as handle:
            writer=csv.writer(handle);writer.writerow(['case_id','measurement','value','mandatory_case_passed'])
            for c in rec.report['cases']:
                for name,value in c['metrics'].items():writer.writerow([c['id'],name,value,int(c['passed'])])
        rec.save()
    except Exception as exc:
        rec.failure(exc);raise
    return rec.report['passed']

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--input',default=str(Path(__file__).with_name('inputs.json')))
    p.add_argument('--output',required=True);p.add_argument('--seconds',type=float,default=115)
    a=p.parse_args();raise SystemExit(0 if main(a.input,a.output,a.seconds) else 1)
