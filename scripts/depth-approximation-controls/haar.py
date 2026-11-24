"""Explicit three-level Haar pairs with declared odd-length padding/cropping."""
import math
import numpy as np


def analyze(signal, levels, boundary):
    if boundary not in ('periodic', 'symmetric'):
        raise ValueError('Unknown finite-signal boundary rule')
    a = np.array(signal, dtype=float, copy=True)
    if a.ndim != 1 or not np.isfinite(a).all():
        raise ValueError('Finite vector required')
    lengths, details, pads, ledger = [], [], [], []
    for _ in range(levels):
        lengths.append(len(a))
        old_energy = float(np.sum(a*a))
        padded = len(a) % 2 == 1
        extra = float(a[0] if boundary == 'periodic' else a[-1]) if padded else 0.0
        work = np.r_[a, extra] if padded else a.copy()
        nxt = (work[::2]+work[1::2])/math.sqrt(2.0)
        d = (work[::2]-work[1::2])/math.sqrt(2.0)
        ledger.append((old_energy, extra*extra, float(np.sum(nxt*nxt)+np.sum(d*d))))
        details.append(d.copy());pads.append(extra);a = nxt
    return {'coarse': a.copy(), 'details': details, 'lengths': np.array(lengths), 'pads': np.array(pads), 'energy_ledger': np.array(ledger)}


def flatten(model):
    return np.concatenate([model['coarse'], *model['details'][::-1]])


def threshold(model, kind, tau):
    copy = {k: v.copy() if isinstance(v, np.ndarray) else [a.copy() for a in v] for k, v in model.items()}
    if kind not in ('none', 'hard', 'soft'):
        raise ValueError('Unknown threshold')
    for i, d in enumerate(copy['details']):
        if kind == 'hard':copy['details'][i] = np.where(np.abs(d) > tau, d, 0.0)
        elif kind == 'soft':copy['details'][i] = np.sign(d)*np.maximum(np.abs(d)-tau, 0.0)
    return copy


def synthesize(model):
    a = model['coarse'].copy()
    for d, length in zip(model['details'][::-1], model['lengths'][::-1]):
        work = np.empty(2*len(a))
        work[::2] = (a+d)/math.sqrt(2.0)
        work[1::2] = (a-d)/math.sqrt(2.0)
        a = work[:int(length)].copy()
    return a
