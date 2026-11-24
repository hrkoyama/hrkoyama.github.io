"""Finite JSON, scalar-record CSV and exact declared-source provenance."""
import csv
import hashlib
import json
import math
from pathlib import Path


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def portable(value):
    if isinstance(value, dict):
        return {str(k): portable(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [portable(v) for v in value]
    if hasattr(value, 'item'):
        return portable(value.item())
    if isinstance(value, float) and not math.isfinite(value):
        raise ValueError('Nonfinite JSON value')
    if value is None or isinstance(value, (str, int, float, bool)):
        return value
    raise TypeError('Unsupported JSON value '+type(value).__name__)


def write_json(path, value):
    target = Path(path)
    text = json.dumps(portable(value), ensure_ascii=False, indent=2, allow_nan=False)+'\n'
    temporary = target.with_name(target.name+'.tmp')
    temporary.write_text(text)
    temporary.replace(target)


def write_csv(path, rows):
    if not rows:
        raise ValueError('A scientific CSV must have records')
    keys = list(dict.fromkeys(k for row in rows for k in row))
    with Path(path).open('w', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=keys)
        writer.writeheader()
        for row in rows:
            normalized = portable(row)
            if not all(v is None or isinstance(v, (str, int, float, bool)) for v in normalized.values()):
                raise ValueError('CSV contains a nonscalar field')
            writer.writerow({k: '' if v is None else v for k, v in normalized.items()})


def source_hashes(root):
    root = Path(root)
    contract = json.loads((root/'pre-run-contract.json').read_text())
    names = list(contract['files_sha256'])+['pre-run-contract.json']
    result = {name: sha(root/name) for name in names}
    for name, expected in contract['files_sha256'].items():
        if result[name] != expected:
            raise ValueError('Declared source changed: '+name)
    return result
