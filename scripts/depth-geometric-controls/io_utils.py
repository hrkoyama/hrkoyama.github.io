"""Portable finite metadata and immediate raw candidate retention."""
import hashlib
import json
import math
from pathlib import Path
import numpy as np


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def plain(value):
    if isinstance(value, np.ndarray):
        return plain(value.tolist())
    if isinstance(value, np.generic):
        return plain(value.item())
    if isinstance(value, dict):
        return {str(k): plain(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [plain(v) for v in value]
    if isinstance(value, float) and not math.isfinite(value):
        raise ValueError('Nonfinite JSON metadata')
    return value


def write_json(path, value):
    path = Path(path)
    temporary = path.with_name(path.name+'.tmp')
    temporary.write_text(json.dumps(plain(value), ensure_ascii=False,
                                    indent=2, allow_nan=False)+'\n')
    temporary.replace(path)


def save_raw(directory, tag, fields):
    """NPZ arrays and JSON labels are separate; no pickle/object arrays."""
    directory = Path(directory); directory.mkdir(parents=True, exist_ok=True)
    arrays, metadata = {}, {}
    for key, value in fields.items():
        if isinstance(value, np.ndarray):
            arrays[key] = value
        elif isinstance(value, (int, float, bool)):
            arrays[key] = np.asarray(value)
        elif isinstance(value, (tuple, list)):
            try:
                array = np.asarray(value)
                if array.dtype.kind in 'biufc':
                    arrays[key] = array
                else:
                    metadata[key] = plain(value)
            except ValueError:
                metadata[key] = plain(value)
        else:
            metadata[key] = plain(value)
    temporary = directory/(tag+'.tmp.npz')
    np.savez(temporary, **arrays)
    temporary.replace(directory/(tag+'.npz'))
    if metadata:
        write_json(directory/(tag+'-labels.json'), metadata)
