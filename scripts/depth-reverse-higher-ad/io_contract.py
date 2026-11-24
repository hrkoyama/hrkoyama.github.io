"""Finite public JSON/CSV and early, owning candidate snapshots."""
import csv
import json
from pathlib import Path
import numpy as np


def plain(x):
    if isinstance(x, np.ndarray): return x.tolist()
    if isinstance(x, np.generic): return x.item()
    if isinstance(x, dict): return {str(k): plain(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)): return [plain(v) for v in x]
    return x


def save_json(path, value):
    path = Path(path); temp = path.with_suffix(path.suffix+'.partial')
    temp.write_text(json.dumps(plain(value), ensure_ascii=False, indent=2, allow_nan=False)+'\n')
    temp.replace(path)


def snapshot(path, stage, **arrays):
    values = {k: np.array(v, copy=True) for k, v in arrays.items() if v is not None}
    values['stage'] = np.array(stage)
    path=Path(path);temporary=path.with_name(path.stem+'.partial.npz')
    np.savez_compressed(temporary, **values);temporary.replace(path)


def csv_rows(path, rows):
    if not rows: raise ValueError('Nonempty CSV required')
    with Path(path).open('w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(plain(rows))
