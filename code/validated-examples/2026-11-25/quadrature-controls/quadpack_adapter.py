"""Explicit dispatch and full_output preservation for fixed SciPy1.14.1 calls."""
import math
from scipy.integrate import quad


def full_integrand(name):
    if name == "gaussian-whole-line":
        return lambda x: math.exp(-x*x)
    if name.startswith("finite-sine-"):
        omega = int(name.rsplit("-", 1)[1])
        return lambda x: math.exp(-x)*math.sin(omega*x)
    if name == "fourier-half-line":
        return lambda x: math.exp(-x)*math.sin(8*x)
    if name == "internal-root":
        return lambda x: abs(x-3/8)**(-.5)
    raise ValueError("Unknown integrand")


def dispatch(row):
    name = row["integrand_id"]
    kw = {"epsabs": row["absolute_tolerance"], "epsrel": 0.0,
          "full_output": 1, "limit": row["quad_limit"]}
    if name == "gaussian-whole-line":
        return full_integrand(name), -math.inf, math.inf, kw, "qagie"
    if name.startswith("finite-sine-") or name == "fourier-half-line":
        omega = int(name.rsplit("-", 1)[1]) if name.startswith("finite-sine-") else 8
        kw.update(weight="sin", wvar=omega, maxp1=row["quad_maxp1"])
        if name == "fourier-half-line":
            kw["limlst"] = row["quad_limlst"]
        return lambda x: math.exp(-x), 0.0, math.inf if name == "fourier-half-line" else 1.0, kw, "qawfe" if name == "fourier-half-line" else "qawoe"
    kw["points"] = [3/8]
    return full_integrand(name), 0.0, 1.0, kw, "qagpe"


def validate_options(options):
    if "points" in options and "weight" in options:
        raise ValueError("Breakpoints and oscillatory weights cannot be combined")
    if options.get("epsrel") != 0 or not options.get("epsabs", 0) > 0:
        raise ValueError("This fixed series requires positive epsabs and epsrel0")


def integrate(row, trace, retain_raw):
    function, left, right, options, routine = dispatch(row)
    validate_options(options)
    result = quad(trace.wrap(function), left, right, **options)
    # Persist all native arrays/status before interpreting them.
    raw = {"routine": routine, "value": result[0], "estimated_error": result[1],
           "native_info": result[2], "messages": [str(v) for v in result[3:]]}
    retain_raw(raw)
    info = result[2]
    active = {}
    if "lst" in info:
        count = int(info["lst"])
        active = {k: info[k][:count].tolist() for k in ("ierlst", "rslst", "erlst")}
    else:
        count = int(info["last"])
        active = {k: info[k][:count].tolist() for k in ("alist", "blist", "rlist", "elist")}
    converged = len(result) == 3 and all(v == 0 for v in active.get("ierlst", []))
    return {"value": float(result[0]), "estimated_error": float(result[1]),
            "evaluations": int(info["neval"]), "converged": bool(converged),
            "termination": "library_success" if converged else "library_non_success",
            "routine": routine, "messages": [str(v) for v in result[3:]], "active": active}
