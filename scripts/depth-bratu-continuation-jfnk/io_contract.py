"""Small public result/finite-CSV envelope, also retaining partial source-independent arrays."""
import csv,json
from pathlib import Path
import numpy as np


def dump(path,value):Path(path).write_text(json.dumps(value,ensure_ascii=False,indent=2,allow_nan=False)+'\n')


def array_progress(out,label):
    """Retain the current candidate before a solver/library/diagnostic can fail."""
    return lambda **arrays:np.savez_compressed(out/(label+'-candidate.npz'),**{k:np.asarray(v) for k,v in arrays.items()})


def save_arc_raw(out,label,arc):
    arrays=dict(states=arc['states'],tangents=arc['tangents'])
    for k,row in enumerate(arc['correctors']):
        arrays['corrector_states_'+str(k)]=row['states'];arrays['corrector_residuals_'+str(k)]=row['residuals']
    np.savez_compressed(out/(label+'-completed-arc.npz'),**arrays)
    dump(out/(label+'-completed-arc.json'),arc['rows'])


def save_root_raw(out,label,ans):
    np.savez_compressed(out/(label+'-completed-root.npz'),u=ans['u'],states=ans['states'],residuals=ans['residuals'])
    dump(out/(label+'-completed-root.json'),dict(passed=bool(ans['passed']),reason=ans['reason']))


def save_jfnk_raw(out,label,ans):
    arrays=dict(u=ans['u'],states=ans['states'])
    for k,history in enumerate(ans['linear_histories']):arrays['inner_'+str(k)]=history
    for k,trial in enumerate(ans['line_trials']):arrays['line_trial_'+str(k)]=trial['state']
    np.savez_compressed(out/(label+'-completed-solve.npz'),**arrays)
    dump(out/(label+'-completed-solve.json'),dict(passed=bool(ans['passed']),reason=ans['reason'],
         final_residual=float(ans['final_residual']),counts=ans['counts'],rows=ans['rows'],
         line_trials=[{k:v for k,v in trial.items() if k!='state'} for trial in ans['line_trials']]))


def numeric_csv(path,rows):
    if not rows:raise ValueError('Numeric CSV cannot be empty')
    fields=list(rows[0])
    with Path(path).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
        for row in rows:
            if set(row)!=set(fields) or not all(isinstance(v,(int,float,np.integer,np.floating)) and np.isfinite(v) for v in row.values()):raise ValueError('Nonfinite/ragged CSV')
            w.writerow(row)


class Case:
    def __init__(self,ident,out,cases):
        self.out=out;self.data=dict(id=ident,passed=False,checks={},metrics={},records=[],data_files=[]);cases.append(self.data)
    def gate(self,name,value):
        if name in self.data['checks']:raise ValueError('Duplicate gate:'+name)
        self.data['checks'][name]=bool(value)
    def row(self,row):
        self.data['records'].append(row);dump(self.out/(self.data['id']+'-partial.json'),self.data)
    def finish(self,metrics):
        self.data['metrics']=metrics;self.data['passed']=bool(self.data['records'] and all(self.data['checks'].values()))
