"""Reference/component qualification only: no 105-row primary run."""
from pathlib import Path
import argparse
import hashlib
import json
import math
from decimal import Decimal, localcontext
import sys

SOURCE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SOURCE))
from references.formulas import all_targets
from references.interval import Interval, pi_interval
from references.direct_rule import lagrange_weights
import gk15
import cubature
import double_exponential

DEPENDENCIES = ["inputs.json", "acceptance.json", "gk15.py", "cubature.py",
                "double_exponential.py", "references/interval.py",
                "references/formulas.py", "references/direct_rule.py",
                "references/qualify.py", "references/__init__.py"]
EXPECTED_CHECKS = 188


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write(path, value):
    path.write_text(json.dumps(value, indent=2, allow_nan=False)+"\n")


def transformed_reference(kind, t, precision):
    t = Interval(t, precision=precision)
    pi = pi_interval(precision)
    sinh, cosh = (t.exp()-(-t).exp())/2, (t.exp()+(-t).exp())/2
    x = 1/(1+(-pi*sinh).exp())
    jac = pi*cosh*x*(1-x)
    if kind == "smooth-exponential":
        return x.exp()*jac
    if kind == "algebraic-inverse-cuberoot":
        return (-x.ln()/3).exp()*jac
    return -x.ln()*jac


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=False)
    before = {name: digest(SOURCE/name) for name in DEPENDENCIES}
    checks, raw, cache = {}, {}, {}
    failure = None

    def retain(precision, partial):
        raw[str(precision)] = dict(partial)
        write(args.output/"partial-targets.json", raw)

    def gate(name, condition):
        checks[name] = bool(condition)
        write(args.output/"partial-checks.json", checks)

    try:
        low = all_targets(80, lambda v: retain(80, v))
        high = all_targets(120, lambda v: retain(120, v))
        if len(low) != 30 or set(low) != set(high):
            raise ValueError("Reference target inventory")
        with localcontext() as context:
            context.prec = 160
            for name in low:
                l, h = low[name], high[name]
                l0, l1, h0, h1 = map(Decimal, (l["lower"], l["upper"], h["lower"], h["upper"]))
                scale = max(Decimal(1), abs((h0+h1)/2))
                gate("interval-overlap:"+name, max(l0, h0) <= min(l1, h1))
                gate("precision-agreement:"+name, abs((l0+l1-h0-h1)/2) <= Decimal("1e-60")*scale)
                allowed = (2*Decimal(high["q78:gaussian-tail-bound"]["upper"])
                           if name == "q78:gaussian-finite" else Decimal("1e-60")*scale)
                gate("interval-width:"+name, h1-h0 <= allowed and l1-l0 <= allowed)
                cache[name] = h
        for degree in range(14):
            result = gk15.panel(lambda x, degree=degree: x**degree, -1, 1)
            # panel's stored K15 does not itself expose G7; integrate its seven nodes directly.
            gauss = gk15.WG[3]*(0.0**degree)+math.fsum(
                gk15.WG[j]*((-gk15.X[i])**degree+gk15.X[i]**degree)
                for j, i in enumerate((1, 3, 5)))
            exact = 0.0 if degree % 2 else 2/(degree+1)
            gate("g7-moment:"+str(degree), abs(gauss-exact) <= 2e-13)
        for degree in range(24):
            result = gk15.panel(lambda x, degree=degree: x**degree, -1, 1)
            exact = 0.0 if degree % 2 else 2/(degree+1)
            gate("k15-moment:"+str(degree), abs(result["value"]-exact) <= 2e-13)
        gate("gk-positive-weights", all(v > 0 for v in (*gk15.WG, *gk15.WK)))
        calls = []
        gk15.panel(lambda x: calls.append(x) or 1.0, -1, 1)
        gate("gk-shared15-calls", len(calls) == len(set(calls)) == 15)
        for level in range(5):
            rule = cubature.cc_items(level)
            nodes = [cubature.coordinate(k) for k, _ in rule]
            weights = [w for _, w in rule]
            max_degree = 1 if level == 0 else 2**level
            for degree in range(max_degree+1):
                gate("cc-moment:"+str(level)+":"+str(degree),
                     abs(math.fsum(w*x**degree for w, x in zip(weights, nodes))-1/(degree+1)) <= 2e-13)
            gate("cc-canonical:"+str(level),
                 len({k for k, _ in rule}) == len(rule)
                 and all(cubature.angle_key(*k) == k for k, _ in rule)
                 and cubature.coordinate((1, 2)) == .5)
            if level in (1, 2):
                direct = lagrange_weights(nodes)
                gate("cc-independent-polynomial:"+str(level),
                     max(abs(float(a)-b) for a, b in zip(direct, weights)) <= 2e-13)
        for kind in ("smooth-exponential", "algebraic-inverse-cuberoot", "log-endpoint"):
            for t in (-4, -1, 0, 1, 4):
                ref = transformed_reference(kind, t, 120)
                _, actual, _, _ = double_exponential.transformed(kind, t)
                with localcontext() as context:
                    context.prec = 160
                    middle = (ref.lo+ref.hi)/2
                    discrepancy = max(abs(Decimal.from_float(actual)-ref.lo),
                                      abs(Decimal.from_float(actual)-ref.hi))
                    gate("de-stable-product:"+kind+":"+str(t),
                         discrepancy <= Decimal("5e-13")*abs(middle))
        if len(checks) != EXPECTED_CHECKS:
            raise ValueError("Qualification check inventory differs")
    except BaseException as error:
        failure = {"type": type(error).__name__, "message": str(error)}
    finally:
        after = {name: digest(SOURCE/name) for name in DEPENDENCIES}
        result = {"schema_version": 1, "passed": failure is None and len(checks) == EXPECTED_CHECKS and all(checks.values()) and before == after,
                  "checks": checks, "check_count": len(checks), "expected_check_count": EXPECTED_CHECKS,
                  "failure": failure, "source_sha256": before, "source_unchanged": before == after,
                  "input_sha256": digest(SOURCE/"inputs.json"), "acceptance_sha256": digest(SOURCE/"acceptance.json"),
                  "primary_rows_executed": 0, "target_count": len(cache)}
        write(args.output/"qualification.json", result)
        write(args.output/"reference-cache.json", {"schema_version": 1, "targets": cache,
              "qualification_sha256": digest(args.output/"qualification.json"),
              "source_sha256": before, "input_sha256": result["input_sha256"],
              "acceptance_sha256": result["acceptance_sha256"], "qualified": result["passed"]})
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
