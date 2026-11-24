"""Fresh output, finite envelope and save-before-diagnostic helpers."""
import csv
import hashlib
import json
from pathlib import Path
import numpy as np


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def native(value):
    if isinstance(value, np.ndarray):
        return native(value.tolist())
    if isinstance(value, np.generic):
        return native(value.item())
    if isinstance(value, dict):
        return {str(k): native(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [native(v) for v in value]
    return value


def save_json(path, value):
    path = Path(path)
    tmp = path.with_name(path.name+'.tmp')
    tmp.write_text(json.dumps(native(value), ensure_ascii=False, indent=2, allow_nan=False)+'\n')
    tmp.replace(path)


def save_npz(path, arrays=None, **keywords):
    # Completed candidates are saved BEFORE reference/diagnostic access.
    values = {} if arrays is None else dict(arrays)
    values.update(keywords)
    np.savez_compressed(path, **values)


def finite_csv(path, columns, rows):
    with Path(path).open('w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(columns)
        for row in rows:
            if any(not np.isfinite(float(x)) for x in row):
                raise ValueError('Nonfinite numeric CSV')
            writer.writerow([float(x) for x in row])


def fresh_directory(path):
    path = Path(path)
    if path.exists() and any(path.iterdir()):
        raise ValueError('Output must be fresh/empty; preserve earlier attempts')
    path.mkdir(parents=True, exist_ok=True)
    return path


def checkpoint(path, **arrays):
    save_npz(path, **{k: np.asarray(v) for k, v in arrays.items() if v is not None})


def add(checks, name, passed):
    if name in checks:
        raise ValueError('Repeated gate: '+name)
    checks[name] = bool(passed)


def qualified_cache(source, input_path, acceptance_path):
    source = Path(source)
    q = json.loads((source/'references/qualification.json').read_text())
    if q.get('passed') is not True or len(q.get('checks', {})) != 67 or not all(v is True for v in q['checks'].values()):
        raise ValueError('All67 independent reference checks required')
    if q['input_sha256'] != digest(input_path) or q['acceptance_sha256'] != digest(acceptance_path):
        raise ValueError('Stale reference inputs/criteria')
    for name, expected in q['source_sha256'].items():
        if digest(source/name) != expected:
            raise ValueError('Stale reference source: '+name)
    for name, expected in q['cache_sha256'].items():
        if digest(source/'references'/name) != expected:
            raise ValueError('Changed reference cache: '+name)
    return q
