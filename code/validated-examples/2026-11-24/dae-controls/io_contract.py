"""Finite, atomic metadata and owned candidate retention."""
import csv
import json
from pathlib import Path
import numpy as np


def json_scalar(value):
    if isinstance(value, np.generic):
        return value.item()
    raise TypeError("Unsupported JSON type: "+type(value).__name__)


def save_json(path, value):
    path = Path(path)
    tmp = path.with_name(path.name+'.tmp')
    tmp.write_text(json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False, default=json_scalar)+'\n')
    tmp.replace(path)


def save_arrays(path, **arrays):
    np.savez_compressed(path, **{key: np.array(value, copy=True) for key, value in arrays.items()})


def csv_rows(path, names, rows):
    with Path(path).open('w', newline='') as stream:
        writer = csv.writer(stream)
        writer.writerow(names)
        writer.writerows(rows)


class Case:
    def __init__(self, ident, output):
        self.output = Path(output)
        self.data = {'id': ident, 'passed': False, 'checks': {}, 'records': [], 'metrics': {}}
        self.checkpoint()

    def checkpoint(self):
        save_json(self.output/(self.data['id']+'-partial.json'), self.data)

    def check(self, key, condition, value=None):
        if key in self.data['checks']:
            raise ValueError('Duplicate gate: '+key)
        self.data['checks'][key] = bool(condition)
        if value is not None:
            self.data['metrics'][key] = value
        self.checkpoint()

    def record(self, value):
        self.data['records'].append(value)
        self.checkpoint()
        return value

    def finish(self):
        import hashlib
        from reporting import verify_study
        source=Path(__file__).resolve().parent
        policy=json.loads((source/'reporting-policy.json').read_text())
        original=dict(self.data['checks'])
        self.data['original_target_results']=original
        self.data['original_target_summary']={'met':sum(original.values()),'total':len(original),'all_met':all(original.values()),'acceptance_sha256':hashlib.sha256((source/'acceptance.json').read_bytes()).hexdigest()}
        self.data['original_scientific_targets_met']=all(original.values())
        if self.data['id'] in policy['study_goal_keys']:
            self.data['checks'],self.data['reporting_verification']=verify_study(self.data,self.output)
            self.data['original_study_goal_measurements']=self.data['reporting_verification']['goal_measurements']
            self.data['validation_scope']='fixed_study_with_separate_original_accuracy_goals'
        else:
            self.data['validation_scope']='all_original_numerical_targets_required'
        self.data['metrics']['original_targets_met']=sum(original.values())
        self.data['metrics']['original_targets_total']=len(original)
        self.data['passed'] = bool(self.data['checks']) and all(self.data['checks'].values())
        self.checkpoint()
        return self.data
