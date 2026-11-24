"""Strict output and observation-only raw retention utilities."""
import csv
import hashlib
import json
import math
from pathlib import Path

import numpy as np


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def plain(value, raw=False):
    if isinstance(value, np.ndarray):
        return plain(value.tolist(), raw)
    if isinstance(value, np.generic):
        return plain(value.item(), raw)
    if isinstance(value, dict):
        return {str(k): plain(v, raw) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [plain(v, raw) for v in value]
    if isinstance(value, float) and not math.isfinite(value):
        if raw:
            return {"nonfinite_raw_value": repr(value)}
        raise ValueError("Nonfinite final JSON measurement")
    return value


def write_json(path, value):
    path = Path(path)
    temporary = path.with_suffix(path.suffix + '.tmp')
    temporary.write_text(json.dumps(plain(value), ensure_ascii=False,
                                    indent=2, allow_nan=False) + '\n')
    temporary.replace(path)


def numeric_csv(path, columns, rows):
    with Path(path).open('w', newline='') as handle:
        writer = csv.writer(handle)
        writer.writerow(columns)
        for row in rows:
            if len(row) != len(columns) or not all(math.isfinite(float(v)) for v in row):
                raise ValueError('CSV rows must have finite numeric columns')
            writer.writerow(row)


class Retainer:
    """One append-only raw trace per run, saved before the next computation.

    Nonfinite raw values are tagged, never converted into finite measurements.
    No library-internal temporary arrays are claimed to be observable.
    """
    def __init__(self, directory, name):
        self.directory = Path(directory)
        self.directory.mkdir(parents=True, exist_ok=True)
        self.name = name
        self.path = self.directory / (name + '-raw.jsonl')
        if self.path.exists():
            raise FileExistsError(self.path)
        self.path.touch()
        self.forward_calls = 0
        self.events = 0

    def raw(self, stage, **values):
        record = {'event': self.events, 'stage': stage, **values}
        with self.path.open('a') as handle:
            handle.write(json.dumps(plain(record, raw=True), allow_nan=False) + '\n')
            handle.flush()
        self.events += 1

    def arrays(self, suffix, **values):
        path = self.directory / (self.name + '-' + suffix + '.npz')
        np.savez_compressed(path, **{k: np.asarray(v) for k, v in values.items()})
        return path.name


class DecisionBook:
    def __init__(self):
        self.checks = {}
        self.details = {}

    def add(self, name, passed, actual=None, limit=None):
        if name in self.checks:
            raise ValueError('Repeated decision: ' + name)
        self.checks[name] = bool(passed)
        self.details[name] = plain({'passed': bool(passed), 'actual': actual, 'limit': limit})


def relative_error(actual, expected, order=None):
    actual, expected = np.asarray(actual), np.asarray(expected)
    return float(np.linalg.norm(actual - expected, ord=order) /
                 max(float(np.linalg.norm(expected, ord=order)), 1e-300))


def projected_gradient(theta, gradient, lower, upper):
    theta, gradient = np.asarray(theta), np.asarray(gradient)
    return float(np.linalg.norm(theta - np.clip(theta - gradient, lower, upper), ord=np.inf))


def classify_library(result, externally_stationary):
    status = int(result.status)
    if bool(result.success):
        return 'LIBRARY_SUCCESS'
    if externally_stationary:
        return 'EXTERNALLY_STATIONARY_LIBRARY_FAILURE_RETAINED'
    if status == 0 or 'limit' in str(result.message).lower() or 'exceed' in str(result.message).lower():
        return 'BUDGET_EXHAUSTED'
    return 'LIBRARY_FAILURE'
