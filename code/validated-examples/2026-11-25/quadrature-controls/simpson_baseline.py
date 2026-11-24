import math

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

