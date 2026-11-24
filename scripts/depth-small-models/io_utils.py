"""Portable finite output, bounded work and owned failure snapshots."""
import hashlib
import json
import math
import time
from pathlib import Path
import numpy as np


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def write_json(path, data):
    path = Path(path)
    temporary = path.with_suffix(path.suffix + '.tmp')
    temporary.write_text(json.dumps(data, ensure_ascii=False, indent=2, allow_nan=False) + '\n')
    temporary.replace(path)


def fresh(path):
    path = Path(path)
    if path.exists() and any(path.iterdir()):
        raise ValueError('Output must be a fresh or empty directory')
    path.mkdir(parents=True, exist_ok=True)
    return path


class Deadline:
    def __init__(self, seconds=120):
        if not 0 < seconds <= 120:
            raise ValueError('Invalid bounded deadline')
        self.end = time.monotonic() + seconds

    def check(self):
        if time.monotonic() > self.end:
            raise TimeoutError('Fixed calculation deadline exhausted')


class Trace:
    """Only latest owned contexts, not full successful optimizer histories.

    Ordinary exceptions flush owned current arrays. SIGKILL preserves only the
    already written checkpoints, not live unwritten library internals.
    """
    def __init__(self, output, stem):
        self.output, self.stem = Path(output), stem
        self.latest = {}
        self.events = 0

    def observe(self, role, **arrays):
        self.latest[role] = {k: np.array(v, copy=True) for k, v in arrays.items()}
        self.events += 1
        if self.events % 32 == 0:
            self.flush()

    def flush(self):
        arrays = {role + '__' + key: value for role, values in self.latest.items()
                  for key, value in values.items()}
        temporary = self.output / (self.stem + '-partial.tmp.npz')
        np.savez_compressed(temporary, **arrays)
        temporary.replace(self.output / (self.stem + '-partial.npz'))


def finite(value):
    array = np.asarray(value)
    if not np.isfinite(array).all():
        raise FloatingPointError('Nonfinite scientific quantity')
    return value


def rms(array):
    array = np.asarray(array)
    return math.sqrt(float(np.mean(array * array)))


def outcome(measured, limit):
    return {'measured': float(measured), 'limit': float(limit),
            'comparison': '<=', 'units': 'dimensionless', 'met': bool(measured <= limit)}


def summarize(case, targets, acceptance_sha):
    case['original_target_results'] = {k: bool(v['met']) for k, v in targets.items()}
    case['original_target_summary'] = {'met': sum(case['original_target_results'].values()),
        'total': len(targets), 'all_met': all(case['original_target_results'].values()),
        'acceptance_sha256': acceptance_sha}
    case['original_study_goal_measurements'] = targets
    case['validation_scope'] = 'predeclared_accuracy_study_with_separate_reproduction_checks'
    case['passed'] = all(case['checks'].values())

