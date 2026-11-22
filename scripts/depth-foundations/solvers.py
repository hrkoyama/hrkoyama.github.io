"""Small educational matrix algorithms; NumPy/SciPy references live in run.py.

The AMG construction consumes an SPD matrix, not grid coordinates. The SVD is
one-sided Jacobi; the dense eigensolves below are only small Ritz/Jacobi cores.
"""
from dataclasses import dataclass
import math

import numpy as np
from scipy import sparse


def matrix_product(a, b):
    """Explicit small dense contraction (avoids platform-specific BLAS FP flags)."""
    return np.einsum('ik,kj->ij', a, b, optimize=False)


def matrix_vector(a, b):
    return np.einsum('ij,j->i', a, b, optimize=False)


def real_matrix(value, square=False):
    a = np.array(value, dtype=float, copy=True)
    if a.ndim != 2 or min(a.shape) == 0 or not np.isfinite(a).all():
        raise ValueError('Expected a finite nonempty real matrix')
    if square and a.shape[0] != a.shape[1]:
        raise ValueError('Expected a square matrix')
    return a


def householder_qr(value):
    """Reduced QR for real m >= n; no column pivoting/rank-revealing claim."""
    r = real_matrix(value)
    m, n = r.shape
    if m < n:
        raise ValueError('Reduced implementation requires rows >= columns')
    q = np.eye(m)
    for k in range(n):
        v = r[k:, k].copy()
        length = np.linalg.norm(v)
        if length == 0:
            continue
        v[0] += math.copysign(length, v[0])
        v /= np.linalg.norm(v)
        r[k:, k:] -= 2 * np.outer(v, v @ r[k:, k:])
        q[:, k:] -= 2 * np.outer(q[:, k:] @ v, v)
        r[k + 1:, k] = 0.0
    return q[:, :n], r[:n, :]


def back_substitute(r, b):
    r = real_matrix(r, square=True)
    b = np.asarray(b, dtype=float)
    if b.shape != (r.shape[0],) or not np.isfinite(b).all():
        raise ValueError('Incompatible right-hand side')
    scale = max(1.0, np.linalg.norm(r, np.inf))
    if np.min(np.abs(np.diag(r))) <= np.finfo(float).eps * scale:
        raise ValueError('Singular triangular system; use a rank-aware solver')
    x = np.zeros_like(b)
    for i in range(len(b) - 1, -1, -1):
        x[i] = (b[i] - r[i, i + 1:] @ x[i + 1:]) / r[i, i]
    return x


def column_correlation(b):
    norms = np.linalg.norm(b, axis=0)
    largest = 0.0
    for p in range(b.shape[1]):
        for q in range(p + 1, b.shape[1]):
            product = norms[p] * norms[q]
            if product > np.finfo(float).tiny:
                largest = max(largest, abs(float(b[:, p] @ b[:, q])) / product)
    return largest


def jacobi_svd(value, tolerance=1e-13, max_sweeps=60, rank_rtol=1e-12):
    """One-sided cyclic Jacobi SVD, returning compact numerical-rank factors.

    Zero singular directions are omitted, so U is orthonormal even for deficient
    rank. This is a finite educational implementation, not LAPACK-grade scaling.
    """
    b = real_matrix(value)
    m, n = b.shape
    if m < n or not 0 < tolerance < 1 or max_sweeps < 0 or not 0 < rank_rtol < 1:
        raise ValueError('Invalid SVD shape or controls')
    v = np.eye(n)
    converged = column_correlation(b) <= tolerance
    sweeps = 0
    for sweeps in range(1, max_sweeps + 1):
        if converged:
            sweeps -= 1
            break
        for p in range(n):
            for q in range(p + 1, n):
                bp, bq = b[:, p].copy(), b[:, q].copy()
                alpha, beta, gamma = bp @ bp, bq @ bq, bp @ bq
                if alpha * beta <= np.finfo(float).tiny:
                    continue
                if abs(gamma) <= tolerance * math.sqrt(alpha * beta):
                    continue
                zeta = (beta - alpha) / (2 * gamma)
                t = math.copysign(1.0, zeta) / (abs(zeta) + math.hypot(1.0, zeta))
                c = 1 / math.sqrt(1 + t * t)
                s = c * t
                b[:, p], b[:, q] = c * bp - s * bq, s * bp + c * bq
                vp, vq = v[:, p].copy(), v[:, q].copy()
                v[:, p], v[:, q] = c * vp - s * vq, s * vp + c * vq
        # Tiny numerical-null columns do not define a meaningful correlation.
        singular = np.linalg.norm(b, axis=0)
        active = singular > rank_rtol * max(float(singular.max()), np.finfo(float).tiny)
        converged = column_correlation(b[:, active]) <= tolerance
        if converged:
            break
    singular = np.linalg.norm(b, axis=0)
    order = np.argsort(singular)[::-1]
    singular, b, v = singular[order], b[:, order], v[:, order]
    cutoff = rank_rtol * max(float(singular[0]), np.finfo(float).tiny)
    rank = int(np.count_nonzero(singular > cutoff))
    u = b[:, :rank] / singular[:rank] if rank else np.zeros((m, 0))
    info = {'converged': bool(converged), 'sweeps': sweeps, 'rank': rank,
            'column_correlation': column_correlation(b[:, :rank]),
            'termination': 'column_orthogonality' if converged else 'sweep_budget'}
    return u, singular[:rank], v[:, :rank].T, info


def _start(a, start, dimensions):
    a = real_matrix(a, square=True)
    v = np.asarray(start, dtype=float).copy()
    if not 1 <= dimensions <= len(a) or v.shape != (len(a),) or not np.isfinite(v).all():
        raise ValueError('Invalid Krylov controls')
    length = np.linalg.norm(v)
    if length == 0:
        raise ValueError('Zero starting vector')
    return a, v / length


def arnoldi(a, start, dimensions, breakdown_rtol=1e-13):
    """Two-pass modified Gram–Schmidt Arnoldi; unrestarted real basis."""
    a, v = _start(a, start, dimensions)
    q = np.zeros((len(a), dimensions + 1)); q[:, 0] = v
    h = np.zeros((dimensions + 1, dimensions))
    scale = max(1.0, np.linalg.norm(a, np.inf))
    terminated = False
    for k in range(dimensions):
        w = matrix_vector(a, q[:, k])
        for _ in range(2):
            for j in range(k + 1):
                correction = q[:, j] @ w
                h[j, k] += correction
                w -= correction * q[:, j]
        h[k + 1, k] = np.linalg.norm(w)
        if h[k + 1, k] <= breakdown_rtol * scale:
            terminated = True
            break
        q[:, k + 1] = w / h[k + 1, k]
    count = k + 1
    return q[:, :count], h[:count, :count], {'dimensions': count, 'happy_breakdown': terminated}


def lanczos(a, start, dimensions, breakdown_rtol=1e-13):
    """Symmetric three-term Lanczos with two passes of full reorthogonalization."""
    a, v = _start(a, start, dimensions)
    if not np.allclose(a, a.T, rtol=0, atol=1e-13 * max(1, np.linalg.norm(a, np.inf))):
        raise ValueError('Lanczos requires a real symmetric matrix')
    q = np.zeros((len(a), dimensions + 1)); q[:, 0] = v
    diagonal, off = [], []
    scale = max(1.0, np.linalg.norm(a, np.inf)); terminated = False
    for k in range(dimensions):
        w = matrix_vector(a, q[:, k])
        if k:
            w -= off[-1] * q[:, k - 1]
        alpha = float(q[:, k] @ w); diagonal.append(alpha)
        w -= alpha * q[:, k]
        for _ in range(2):
            w -= matrix_vector(q[:, :k + 1], matrix_vector(q[:, :k + 1].T, w))
        beta = float(np.linalg.norm(w))
        if beta <= breakdown_rtol * scale:
            terminated = True
            break
        if k + 1 < dimensions:
            off.append(beta)
        q[:, k + 1] = w / beta
    count = k + 1
    t = np.diag(diagonal) + np.diag(off, 1) + np.diag(off, -1)
    return q[:, :count], t, {'dimensions': count, 'happy_breakdown': terminated}


def dominant_ritz(a, start, dimensions, method='lanczos', residual_tolerance=1e-9):
    if method not in ('lanczos', 'arnoldi') or residual_tolerance <= 0:
        raise ValueError('Invalid Ritz controls')
    q, h, info = (lanczos if method == 'lanczos' else arnoldi)(a, start, dimensions)
    values, vectors = np.linalg.eigh(h) if method == 'lanczos' else np.linalg.eig(h)
    index = int(np.argmax(values.real))
    value = values[index]
    vector = matrix_vector(q, vectors[:, index]); vector /= np.linalg.norm(vector)
    residual = float(np.linalg.norm(matrix_vector(a, vector) - value * vector))
    info.update(residual=residual, converged=residual <= residual_tolerance,
                orthogonality=float(np.linalg.norm(matrix_product(q.T, q) - np.eye(q.shape[1]), 2)))
    info['termination'] = 'residual_tolerance' if info['converged'] else 'dimension_budget'
    return value, vector, info


def gauss_legendre(order):
    """Golub–Welsch Legendre nodes/weights from a symmetric Jacobi matrix."""
    if not isinstance(order, int) or not 1 <= order <= 128:
        raise ValueError('Quadrature order must be an integer in [1,128]')
    j = np.arange(1, order, dtype=float)
    beta = j / np.sqrt(4 * j * j - 1)
    matrix = np.diag(beta, 1) + np.diag(beta, -1)
    nodes, vectors = np.linalg.eigh(matrix)
    return nodes, 2 * vectors[0, :] ** 2


def adaptive_simpson(function, a, b, absolute_tolerance=1e-9, max_evaluations=20001, max_depth=30):
    """Adaptive Simpson with a heuristic local /15 estimator and explicit budgets.

    The returned estimate is not a rigorous error bound for arbitrary functions.
    """
    if not (math.isfinite(a) and math.isfinite(b) and a < b and
            math.isfinite(absolute_tolerance) and absolute_tolerance > 0):
        raise ValueError('Invalid interval or absolute tolerance')
    if max_evaluations < 3 or max_depth < 0:
        raise ValueError('Invalid evaluation/depth budget')
    evaluations = 0

    def evaluate(x):
        nonlocal evaluations
        result = float(function(x))
        if not math.isfinite(result):
            raise ValueError('Nonfinite integrand')
        evaluations += 1
        return result

    middle = (a + b) / 2
    fa, fm, fb = evaluate(a), evaluate(middle), evaluate(b)
    initial = (b - a) * (fa + 4 * fm + fb) / 6

    def split(left, right, fl, fc, fr, whole, tolerance, depth):
        if evaluations + 2 > max_evaluations:
            return whole, None, False, 'evaluation_budget'
        center = (left + right) / 2
        f1, f2 = evaluate((left + center) / 2), evaluate((center + right) / 2)
        s1 = (center - left) * (fl + 4 * f1 + fc) / 6
        s2 = (right - center) * (fc + 4 * f2 + fr) / 6
        change = s1 + s2 - whole
        estimate = abs(change) / 15
        if estimate <= tolerance:
            return s1 + s2 + change / 15, estimate, True, 'estimated_tolerance'
        if depth == max_depth:
            return s1 + s2, estimate, False, 'depth_budget'
        x1, e1, ok1, reason1 = split(left, center, fl, f1, fc, s1, tolerance / 2, depth + 1)
        x2, e2, ok2, reason2 = split(center, right, fc, f2, fr, s2, tolerance / 2, depth + 1)
        error = e1 + e2 if e1 is not None and e2 is not None else None
        return x1 + x2, error, ok1 and ok2, 'estimated_tolerance' if ok1 and ok2 else (reason1 if not ok1 else reason2)

    value, error, converged, reason = split(a, b, fa, fm, fb, initial, absolute_tolerance, 0)
    return {'value': value, 'estimated_error': error, 'converged': bool(converged),
            'evaluations': evaluations, 'termination': reason}


@dataclass
class SALevel:
    matrix: object
    omega: float
    prolongation: object = None
    coarse: object = None


def aggregate_matrix(a, strength=0.08):
    """Greedy graph-star aggregates; no mesh coordinates or geometric coarsening."""
    a = sparse.csr_matrix(a, dtype=float)
    diagonal = a.diagonal()
    labels = np.full(a.shape[0], -1, dtype=int)
    neighbors = []
    for i in range(len(diagonal)):
        js = a.indices[a.indptr[i]:a.indptr[i + 1]]
        values = a.data[a.indptr[i]:a.indptr[i + 1]]
        off_diagonal = np.abs(values[js != i])
        maximum = float(off_diagonal.max()) if len(off_diagonal) else 0.0
        mask = (js != i) & (np.abs(values) >= strength * maximum)
        neighbors.append(js[mask])
    aggregate = 0
    for i in sorted(range(len(diagonal)), key=lambda k: (-len(neighbors[k]), k)):
        if labels[i] != -1:
            continue
        available = neighbors[i][labels[neighbors[i]] == -1]
        if len(available) == 0 and len(neighbors[i]):
            # Attach a leftover node to an existing neighboring aggregate.
            strongest = max(neighbors[i], key=lambda j: abs(a[i, j]))
            labels[i] = labels[strongest]
            continue
        labels[i] = aggregate
        for j in available:
            labels[j] = aggregate
        aggregate += 1
    return sparse.csr_matrix((np.ones(len(labels)), (np.arange(len(labels)), labels)),
                             shape=(len(labels), aggregate))


def smoothed_aggregation(a, strength=0.08, coarse_size=10, max_levels=12):
    """Scalar SPD smoothed-aggregation hierarchy with a constant candidate."""
    a = sparse.csr_matrix(a, dtype=float)
    if a.shape[0] != a.shape[1] or a.shape[0] == 0 or not np.isfinite(a.data).all():
        raise ValueError('Expected a finite square sparse matrix')
    if not 0 < strength < 1 or coarse_size < 1 or max_levels < 1:
        raise ValueError('Invalid hierarchy controls')
    norm = max(1.0, float(abs(a).sum(axis=1).max()))
    difference = a - a.T
    if np.any(a.diagonal() <= 0) or (difference.nnz and abs(difference).max() > 1e-12 * norm):
        raise ValueError('Expected a symmetric positive-diagonal SPD matrix')
    d_inverse = 1 / a.diagonal()
    rho_bound = float(np.max(np.asarray(abs(a).sum(axis=1)).ravel() * d_inverse))
    omega = 4 / (3 * rho_bound)
    level = SALevel(a, omega)
    if len(d_inverse) <= coarse_size or max_levels == 1:
        # Detect loss of definiteness on the small terminal problem.
        np.linalg.cholesky(a.toarray())
        return level
    tentative = aggregate_matrix(a, strength)
    if tentative.shape[1] >= a.shape[0]:
        np.linalg.cholesky(a.toarray())
        return level
    p = tentative - omega * sparse.diags(d_inverse) @ a @ tentative
    coarse_a = (p.T @ a @ p).tocsr()
    # Roundoff symmetry is restored without changing the Galerkin definition.
    coarse_a = (coarse_a + coarse_a.T) * 0.5
    level.prolongation = p.tocsr()
    level.coarse = smoothed_aggregation(coarse_a, strength, coarse_size, max_levels - 1)
    return level


def v_cycle(level, rhs, pre=2, post=2):
    if level.coarse is None:
        return np.linalg.solve(level.matrix.toarray(), rhs)
    a, p = level.matrix, level.prolongation
    inverse_diagonal = 1 / a.diagonal()
    x = np.zeros_like(rhs, dtype=float)
    for _ in range(pre):
        x += level.omega * inverse_diagonal * (rhs - a @ x)
    x += p @ v_cycle(level.coarse, p.T @ (rhs - a @ x), pre, post)
    for _ in range(post):
        x += level.omega * inverse_diagonal * (rhs - a @ x)
    return x


def solve_amg(level, rhs, relative_tolerance=1e-10, max_cycles=100):
    rhs = np.asarray(rhs, dtype=float)
    if rhs.shape != (level.matrix.shape[0],) or not np.isfinite(rhs).all():
        raise ValueError('Incompatible right-hand side')
    if not 0 < relative_tolerance < 1 or max_cycles < 0:
        raise ValueError('Invalid AMG iteration controls')
    x = np.zeros_like(rhs)
    scale = max(float(np.linalg.norm(rhs)), np.finfo(float).tiny)
    history = [float(np.linalg.norm(rhs - level.matrix @ x) / scale)]
    for _ in range(max_cycles):
        if history[-1] <= relative_tolerance:
            break
        x += v_cycle(level, rhs - level.matrix @ x)
        history.append(float(np.linalg.norm(rhs - level.matrix @ x) / scale))
    converged = history[-1] <= relative_tolerance
    return x, {'converged': bool(converged), 'cycles': len(history) - 1,
               'relative_residual': history[-1], 'history': history,
               'termination': 'residual_tolerance' if converged else 'cycle_budget'}
