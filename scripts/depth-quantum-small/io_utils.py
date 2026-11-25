"""DRAFT: owned checkpoints before diagnostics; no computation on import."""
import json
import math
from pathlib import Path
import numpy as np


def mm(a, b):
    """Explicit two-matrix product for these small models; no conjugation."""
    return np.einsum('ij,jk->ik', a, b, optimize=False)


def mv(a, b):
    """Explicit matrix-vector product, including noncontiguous vectors."""
    return np.einsum('ij,j->i', a, b, optimize=False)


def dot(a, b):
    """Explicit bilinear vector contraction; callers supply any conjugation."""
    return np.einsum('i,i->', a, b, optimize=False)


def norm(a, order=None):
    """Scaled Euclidean/Frobenius norm or a matrix infinity norm, no BLAS."""
    absolute = np.abs(np.asarray(a))
    if order == np.inf:
        if absolute.ndim != 2:
            raise ValueError('Only the declared matrix infinity norm is supported')
        return float(np.max(np.sum(absolute, axis=1)))
    if order is not None:
        raise ValueError('Only Euclidean/Frobenius and matrix infinity norms are supported')
    scale = float(np.max(absolute))
    if not math.isfinite(scale):
        raise FloatingPointError('Nonfinite explicit norm input')
    return 0. if scale == 0 else scale*math.sqrt(float(np.sum((absolute/scale)**2)))


def plain(value):
    if isinstance(value, np.ndarray):
        return plain(value.tolist())
    if isinstance(value, np.generic):
        return plain(value.item())
    if isinstance(value, complex):
        return {"real": plain(value.real), "imag": plain(value.imag)}
    if isinstance(value, float) and not math.isfinite(value):
        return {"nonfinite": repr(value)}
    if isinstance(value, dict):
        return {str(k): plain(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [plain(v) for v in value]
    return value


class Checkpoints:
    def __init__(self, directory):
        self.directory = Path(directory)
        if self.directory.exists() and any(self.directory.iterdir()):
            raise FileExistsError('Require a new or empty checkpoint directory')
        self.directory.mkdir(parents=True, exist_ok=True)

    def __call__(self, name, value):
        path = self.directory / (name + '.json')
        if path.exists():
            raise FileExistsError('Refuse to overwrite checkpoint ' + str(path))
        path.write_text(json.dumps(plain(value), ensure_ascii=False, indent=2, allow_nan=False) + '\n')


def eigh_owned(matrix, name, save):
    owned = np.array(matrix, copy=True)
    save(name + '-input', {"matrix": owned})
    try:
        values, vectors = np.linalg.eigh(owned)
    except Exception as error:
        save(name + '-exception', {"type": type(error).__name__, "message": str(error)})
        raise
    save(name + '-native', {"eigenvalues": values.copy(), "eigenvectors": vectors.copy()})
    return values, vectors
