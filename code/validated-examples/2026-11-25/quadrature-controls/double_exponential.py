"""Finite-[0,1] tanh-sinh with a finite FULL-endpoint trapezoidal sum."""
import math


def transformed(kind, t):
    u = (math.pi/2)*math.sinh(t)
    logx = -math.log1p(math.exp(-2*u)) if u >= 0 else 2*u-math.log1p(math.exp(2*u))
    logone = -2*u-math.log1p(math.exp(-2*u)) if u >= 0 else -math.log1p(math.exp(2*u))
    x = math.exp(logx)
    logjac = math.log(math.pi*math.cosh(t))+logx+logone
    if kind == "smooth-exponential":
        logvalue = x+logjac
    elif kind == "algebraic-inverse-cuberoot":
        logvalue = logjac-logx/3
    elif kind == "log-endpoint":
        logvalue = logjac+math.log(-logx)
    else:
        raise ValueError("Unknown transformed integrand")
    value = math.exp(logvalue)
    if not math.isfinite(value):
        raise ValueError("Nonfinite transformed product")
    return x, value, logx, logone


def integrate(kind, step, cutoff, callback=None, before_evaluation=None):
    if not (step > 0 and cutoff > 0 and cutoff/step == int(cutoff/step)):
        raise ValueError("Fixed integer transformed cutoff required")
    count = int(cutoff/step)
    rows = []
    for k in range(-count, count+1):
        t = k*step
        if before_evaluation:
            before_evaluation(t)
        x, value, logx, logone = transformed(kind, t)
        rows.append([t, x, value, logx, logone])
        if callback:
            callback(t, value)
    result = step*math.fsum(row[2] for row in rows)
    return {"value": result, "evaluations": len(rows), "termination": "fixed_sum_completed",
            "converged": True, "estimated_error": None, "rows": rows,
            "half_endpoint_correction": step*(rows[0][2]+rows[-1][2])/2}
