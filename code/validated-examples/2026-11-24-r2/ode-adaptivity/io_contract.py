"""Portable finite JSON/CSV and immediately readable failure/checkpoint evidence."""
import csv
import hashlib
import json
import math
from pathlib import Path
import numpy as np


def native(x):
    if isinstance(x, np.ndarray):
        return native(x.tolist())
    if isinstance(x, np.generic):
        return native(x.item())
    if isinstance(x, dict):
        return {str(k): native(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [native(v) for v in x]
    if isinstance(x, float) and not math.isfinite(x):
        raise ValueError('Nonfinite JSON number')
    return x


def save_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    raw = json.dumps(native(value), ensure_ascii=False, indent=2, allow_nan=False)+'\n'
    temp = path.with_name(path.name+'.tmp')
    temp.write_text(raw)
    temp.replace(path)


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def save_csv(path, rows):
    if not rows:
        raise ValueError('Nonempty finite numeric CSV required')
    keys = list(dict.fromkeys(key for row in rows for key in row))
    with Path(path).open('w', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=keys)
        writer.writeheader()
        for row in rows:
            clean = native(row)
            if not any(type(v) in (int, float) for v in clean.values()):
                raise ValueError('Each scientific CSV row needs actual numeric values')
            writer.writerow(clean)


class Trace:
    """Bounded last-role ownership; accepted journal32, snapshot256/failure/close.

    Full successful Newton histories are deliberately not serialized. All event
    counts and last owned candidates survive ordinary exceptions/close; SIGKILL
    can retain only already written accepted blocks and last snapshots.
    """
    def __init__(self, directory, run_id):
        self.directory = Path(directory)
        self.run_id = run_id
        self.stream = (self.directory/(run_id+'-stages.jsonl')).open('w')
        self.lines = 0
        self.event_counts = {}
        self.latest = {}
        self.pending = []
        self.last = None
        self.dirty = False

    @staticmethod
    def owned(values):
        return {key: value.copy() if isinstance(value, np.ndarray) else value for key,value in values.items()}

    def __call__(self, phase, **values):
        # Fixed production phase names; latest snapshots are bounded by roles,
        # not number of Newton/RHS events. Copies never alias solver buffers.
        value = self.owned(values)
        self.latest[phase] = value
        self.last = value
        self.event_counts[phase] = self.event_counts.get(phase, 0)+1
        self.dirty = True
        if phase == 'completed-step':
            state = value.get('state')
            if isinstance(state,np.ndarray) and not np.isfinite(state).all():
                self.flush('nonfinite-completed-candidate-not-an-accepted-journal-row')
                return
            self.pending.append(self.owned(value))
            if len(self.pending) >= 32:
                self.flush_accepted()
            if values.get('step', 0) % 256 == 0:
                self.flush('fixed-256-step-checkpoint')
        elif phase in ('failed-stage', 'failed-data'):
            self.flush(phase)

    @staticmethod
    def nonfinite_scalar(value):
        return isinstance(value, (float, np.floating, complex, np.complexfloating)) and not bool(np.isfinite(value))

    def save_raw(self):
        arrays = {}
        invalid = False
        contexts = dict(self.latest)
        contexts.update({'accepted-'+str(index): value for index,value in enumerate(self.pending)})
        for role, values in contexts.items():
            for key, value in values.items():
                if isinstance(value,np.ndarray):
                    arrays[role+'__'+key] = value
                    if np.issubdtype(value.dtype,np.number) and not np.isfinite(value).all():invalid = True
                elif self.nonfinite_scalar(value):
                    arrays[role+'__'+key] = np.array(value,copy=True)
                    invalid = True
        if self.last:
            for key,value in self.last.items():
                if isinstance(value,np.ndarray) or self.nonfinite_scalar(value):arrays[key] = np.array(value,copy=True)
        snapshot = self.run_id+'-checkpoint-'+str(sum(self.event_counts.values()))+'.npz'
        if arrays:
            np.savez_compressed(self.directory/snapshot, **arrays)
            (self.directory/(self.run_id+'-active.npz')).write_bytes((self.directory/snapshot).read_bytes())
        return snapshot if arrays else None, invalid

    def flush_accepted(self):
        if self.pending:
            try:
                data = native(self.pending)
            except BaseException:
                # A malformed scalar must not prevent raw arrays/pending states
                # from surviving an ordinary exception. Do not forge finite data.
                self.save_raw()
                raise
            row = {'run_id': self.run_id, 'phase': 'completed-accepted-block', 'states': data}
            self.stream.write(json.dumps(row, ensure_ascii=False, allow_nan=False)+'\n')
            self.stream.flush()
            self.pending = []
            self.lines += 1

    def flush(self, reason):
        if not self.dirty:
            return
        # Raw candidates, including nonfinite scalars as0d arrays, precede EVERY
        # metadata conversion and accepted-journal serialization on this path.
        snapshot, invalid = self.save_raw()
        self.flush_accepted()
        descriptions = {}
        for role, values in self.latest.items():
            descriptions[role] = {}
            for key, value in values.items():
                if isinstance(value,np.ndarray) or self.nonfinite_scalar(value):
                    array = np.asarray(value)
                    descriptions[role][key] = {'array': role+'__'+key, 'shape': list(array.shape), 'dtype': str(array.dtype)}
                else:
                    descriptions[role][key] = native(value)
        row = {'run_id': self.run_id, 'phase': 'owned-candidate-checkpoint', 'reason': reason,
               'event_counts': dict(self.event_counts), 'last_roles': descriptions,
               'snapshot': snapshot, 'nonfinite_candidate_saved_to_npz': invalid}
        self.stream.write(json.dumps(row, ensure_ascii=False, allow_nan=False)+'\n')
        self.stream.flush()
        self.lines += 1
        self.dirty = False

    def close(self):
        try:
            self.flush('ordinary-close-final-owned-context')
        finally:
            self.stream.close()
