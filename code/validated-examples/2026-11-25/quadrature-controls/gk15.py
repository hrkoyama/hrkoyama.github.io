"""Authored adaptive G7/K15, shared QUADPACK-origin coefficient table.

G7 degree13, K15 degree23; estimates are heuristics, not error certificates.
"""
import math
import sys

X = (0.991455371120812639206854697526329,
     0.949107912342758524526189684047851,
     0.864864423359769072789712788640926,
     0.741531185599394439863864773280788,
     0.586087235467691130294144838258730,
     0.405845151377397166906606412076961,
     0.207784955007898467600689403773245, 0.0)
WK = (0.022935322010529224963732008058970,
      0.063092092629978553290700663189204,
      0.104790010322250183839876322541518,
      0.140653259715525918745189590510238,
      0.169004726639267902826583426598550,
      0.190350578064785409913256402421014,
      0.204432940075298892414161999234649,
      0.209482141084727828012999174891714)
WG = (0.129484966168869693270611432679082,
      0.279705391489276667901467771423780,
      0.381830050505118944950369775488975,
      0.417959183673469387755102040816327)


def panel(function, left, right):
    if not (math.isfinite(left) and math.isfinite(right) and left != right):
        raise ValueError("Finite nonzero panel required")
    center, half = (left+right)/2, (right-left)/2
    fc = float(function(center))
    pairs = [(float(function(center-half*x)), float(function(center+half*x))) for x in X[:-1]]
    all_values = [fc, *(v for pair in pairs for v in pair)]
    if not all(math.isfinite(v) for v in all_values):
        raise ValueError("Nonfinite integrand")
    kronrod = math.fsum([WK[7]*fc, *(WK[i]*(a+b) for i, (a, b) in enumerate(pairs))])
    gauss = math.fsum([WG[3]*fc, *(WG[j]*(pairs[i][0]+pairs[i][1]) for j, i in enumerate((1, 3, 5)))])
    resabs = abs(half)*math.fsum([WK[7]*abs(fc), *(WK[i]*(abs(a)+abs(b)) for i, (a, b) in enumerate(pairs))])
    mean = kronrod/2
    resasc = abs(half)*math.fsum([WK[7]*abs(fc-mean), *(WK[i]*(abs(a-mean)+abs(b-mean)) for i, (a, b) in enumerate(pairs))])
    raw = abs(half*(kronrod-gauss))
    error = raw
    if resasc > 0 and raw > 0:
        error = resasc*min(1.0, (200*raw/resasc)**1.5)
    if resabs > sys.float_info.min/(50*sys.float_info.epsilon):
        error = max(error, 50*sys.float_info.epsilon*resabs)
    return {"value": half*kronrod, "estimated_error": error, "raw_error": raw,
            "resabs": resabs, "resasc": resasc, "evaluations": 15}


def adaptive(function, left, right, atol, max_evaluations, max_intervals, max_depth, retain=None):
    if not (0 < atol and left < right and max_evaluations >= 15 and max_intervals >= 1 and max_depth >= 0):
        raise ValueError("Invalid G7/K15 controls")
    initial = panel(function, left, right)
    panels = [{**initial, "left": left, "right": right, "depth": 0, "serial": 0}]
    evaluations, serial = 15, 1
    status = "estimated_tolerance"
    while math.fsum(p["estimated_error"] for p in panels) > atol:
        if evaluations+30 > max_evaluations:
            status = "evaluation_budget"
            break
        if len(panels)+1 > max_intervals:
            status = "interval_budget"
            break
        index = min(range(len(panels)), key=lambda i: (-panels[i]["estimated_error"], panels[i]["left"], panels[i]["serial"]))
        parent = panels[index]
        if parent["depth"] == max_depth:
            status = "depth_budget"
            break
        middle = (parent["left"]+parent["right"])/2
        children = []
        for a, b in ((parent["left"], middle), (middle, parent["right"])):
            child = panel(function, a, b)
            evaluations += 15
            children.append({**child, "left": a, "right": b, "depth": parent["depth"]+1, "serial": serial})
            serial += 1
        panels[index:index+1] = children
        if retain:
            retain(panels, evaluations)
    return {"value": math.fsum(p["value"] for p in panels),
            "estimated_error": math.fsum(p["estimated_error"] for p in panels),
            "raw_error": math.fsum(p["raw_error"] for p in panels),
            "converged": status == "estimated_tolerance", "termination": status,
            "evaluations": evaluations, "panels": panels}
