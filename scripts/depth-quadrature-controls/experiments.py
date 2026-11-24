"""Exactly105 selected fixed rows; no parameter search or result-dependent retries."""
import math
from pathlib import Path
import cubature
import double_exponential
import gk15
from io_contract import Trace, save_candidate
from quadpack_adapter import full_integrand
import quadpack_adapter
from simpson_baseline import adaptive_simpson
from reference_cache import error_interval, goal, midpoint

METHOD_CODES = {"specialized-quadpack": 0, "simpson-companion": 1,
                "adaptive-g7-k15": 2, "finite-tanh-sinh": 3,
                "tensor-clenshaw-curtis": 4, "smolyak-delta": 5}


def run_row(row, output, references, acceptance):
    trace = Trace(Path(output)/"raw", row["row_id"])
    candidate = None
    failed_expected_pole = False
    try:
        method = row["method_id"]
        if method == "specialized-quadpack":
            candidate = quadpack_adapter.integrate(
                row, trace, lambda raw: save_candidate(Path(output)/"raw", row["row_id"]+"-native", raw))
        elif method == "simpson-companion":
            left, right = row["finite_companion_interval"]
            try:
                candidate = adaptive_simpson(trace.wrap(full_integrand(row["integrand_id"])),
                                             left, right, row["absolute_tolerance"],
                                             row["max_evaluations"], row["max_depth"])
            except (ZeroDivisionError, ValueError) as error:
                if not (row["integrand_id"] == "internal-root"
                        and trace.last_attempt is not None
                        and trace.last_attempt["point"] == 3/8
                        and trace.last_attempt["completed"] is False):
                    raise
                failed_expected_pole = True
                candidate = {"value": None, "estimated_error": None,
                             "evaluations": len(trace.values), "converged": False,
                             "termination": "singular_node_control",
                             "failure_type": type(error).__name__}
        elif method == "adaptive-g7-k15":
            function = {"smooth-exponential": math.exp,
                        "algebraic-inverse-cuberoot": lambda x: x**(-1/3),
                        "log-endpoint": lambda x: -math.log(x)}[row["integrand_id"]]
            candidate = gk15.adaptive(trace.wrap(function), 0.0, 1.0,
                                     row["absolute_tolerance"], row["max_evaluations"],
                                     row["max_intervals"], row["max_depth"])
        elif method == "finite-tanh-sinh":
            candidate = double_exponential.integrate(row["integrand_id"], row["step"],
                                                    row["cutoff"], trace.record, trace.begin)
        else:
            level = row["tensor_level"] if method == "tensor-clenshaw-curtis" else row["sparse_total_level"]
            kind = "tensor" if method == "tensor-clenshaw-curtis" else "delta"
            candidate = cubature.integrate(row["integrand_id"], row["dimension"], level,
                                          kind, row["max_evaluations"], trace.record, trace.begin)
        save_candidate(Path(output)/"raw", row["row_id"], candidate)
    finally:
        trace.save()
    # Every completed candidate and trace already exist before reference access.
    checks = {}
    prefix = row["row_id"]+":"

    def gate(name, condition):
        checks[prefix+name] = bool(condition)

    gate("callback-ledger", candidate["evaluations"] == len(trace.values))
    if row["max_evaluations"] is not None:
        gate("evaluation-cap", candidate["evaluations"] <= row["max_evaluations"])
    record = {k: row[k] for k in ("row_id", "sequence", "integrand_id", "method_id",
                                  "dimension", "absolute_tolerance", "step", "cutoff")}
    record.update(method_code=METHOD_CODES[row["method_id"]],
                  level=row["tensor_level"] if row["tensor_level"] is not None else row["sparse_total_level"],
                  value=candidate["value"], evaluations=candidate["evaluations"],
                  estimated_error=candidate.get("estimated_error"),
                  converged=bool(candidate["converged"]), termination=candidate["termination"],
                  accuracy_goal_met=None, error_lower=None, error_upper=None,
                  raw_file="raw/"+row["row_id"].replace(":", "__")+".npz")
    if failed_expected_pole:
        gate("declared-singular-node", trace.last_attempt["point"] == 3/8 and candidate["value"] is None)
        record["accuracy_goal_state"] = "not_computable_at_sampled_singularity"
        return record, checks
    gate("finite-return", math.isfinite(candidate["value"]))
    if row["sequence"] == 78:
        target = "q78:"+row["integrand_id"]
        if row["method_id"] == "simpson-companion":
            if row["integrand_id"] == "gaussian-whole-line":
                target = "q78:gaussian-finite"
            elif row["integrand_id"] == "fourier-half-line":
                target = "q78:fourier-finite"
        tolerance = acceptance["q78"]["specialized_absolute_error_factor"]*row["absolute_tolerance"]
        lower, upper = error_interval(candidate["value"], references[target])
        record.update(error_lower=lower, error_upper=upper, accuracy_goal_met=goal(lower, upper, tolerance))
        if row["method_id"] == "specialized-quadpack":
            gate("native-success", candidate["converged"])
            gate("required-analytic-accuracy", upper <= tolerance)
            gate("absolute-series", row["relative_tolerance"] == 0.0)
            record["routine"] = candidate["routine"]
            record["native_messages"] = candidate["messages"]
            record["active_partition_or_cycles"] = candidate["active"]
        else:
            gate("native-status", candidate["termination"] in ("estimated_tolerance", "evaluation_budget", "depth_budget"))
            record["baseline_accuracy_is_not_mandatory"] = True
            if row["integrand_id"] in ("gaussian-whole-line", "fourier-half-line"):
                record["full_improper_error_interval"] = list(error_interval(candidate["value"], references["q78:"+row["integrand_id"]]))
    elif row["sequence"] == 79:
        target = "q79:"+row["integrand_id"]
        lower, upper = error_interval(candidate["value"], references[target])
        record.update(error_lower=lower, error_upper=upper)
        if row["method_id"] == "adaptive-g7-k15":
            tolerance = acceptance["q79"]["successful_gk_error_factor"]*row["absolute_tolerance"]
            record["accuracy_goal_met"] = goal(lower, upper, tolerance)
            gate("panel-call-identity", candidate["evaluations"] == 15+30*(len(candidate["panels"])-1))
            gate("panel-caps", len(candidate["panels"]) <= row["max_intervals"]
                 and max(p["depth"] for p in candidate["panels"]) <= row["max_depth"])
            gate("success-accuracy-or-explicit-budget",
                 upper <= tolerance if candidate["converged"] else candidate["termination"] in ("evaluation_budget", "interval_budget", "depth_budget"))
        else:
            tolerance = acceptance["q79"]["de_finest_absolute_error"]
            record["accuracy_goal_met"] = goal(lower, upper, tolerance)
            gate("fixed-sample-count", candidate["evaluations"] == 2*int(row["cutoff"]/row["step"])+1)
            window = references[target+":window:"+str(row["cutoff"])]
            tail = references[target+":continuous-tail:"+str(row["cutoff"])]
            record["signed_continuous_tail"] = midpoint(tail)
            record["signed_finite_window_defect"] = midpoint(window)-candidate["value"]
            record["signed_full_integral_defect"] = midpoint(references[target])-candidate["value"]
            record["half_endpoint_correction"] = candidate["half_endpoint_correction"]
            record["omitted_infinite_grid_sum_bound_provided"] = False
            if row["step"] == .0625 and row["cutoff"] == 4:
                gate("required-finest-accuracy", upper <= tolerance)
    else:
        dimension = row["dimension"]
        level = record["level"]
        target = "q80:"+row["integrand_id"]+":"+str(dimension)
        lower, upper = error_interval(candidate["value"], references[target])
        record.update(error_lower=lower, error_upper=upper,
                      sum_weights=candidate["sum_weights"],
                      sum_absolute_weights=candidate["sum_absolute_weights"],
                      assembly_contributions=candidate["assembly_contributions"],
                      assembly_duplicates=candidate["assembly_duplicates"],
                      cache_hits=candidate["cache_hits"], zero_weights_retained=candidate["zero_weights_retained"])
        scale = max(1.0, candidate["sum_absolute_weights"])
        gate("canonical-inventory", len(set(candidate["keys"])) == candidate["unique_nodes"] == candidate["evaluations"])
        gate("mass", abs(candidate["sum_weights"]-1) <= acceptance["q80"]["normalization_scaled_tolerance"]*scale)
        moments = []
        for axis in range(dimension):
            moments.extend([abs(math.fsum(w*x[axis] for w, x in zip(candidate["weights"], candidate["points"]))-.5),
                            abs(math.fsum(w*x[axis]**2 for w, x in zip(candidate["weights"], candidate["points"]))-1/3)])
        for a in range(dimension):
            for b in range(a):
                moments.append(abs(math.fsum(w*x[a]*x[b] for w, x in zip(candidate["weights"], candidate["points"]))-.25))
        record["maximum_low_moment_defect"] = max(moments)
        gate("low-moments", max(moments) <= acceptance["q80"]["normalization_scaled_tolerance"]*scale)
        if row["method_id"] == "smolyak-delta" and dimension <= 3 and level <= 2:
            companion = cubature.assemble(dimension, level, "combination")
            companion_weights = dict(zip(companion["keys"], companion["weights"]))
            defect = max(abs(w-companion_weights.get(k, 0.0)) for k, w in zip(candidate["keys"], candidate["weights"]))
            record["independent_assembly_weight_defect"] = defect
            gate("delta-combination", set(companion_weights) == set(candidate["keys"])
                 and defect <= acceptance["q80"]["assembly_scaled_tolerance"]*scale)
        if row["integrand_id"] == "interaction-product":
            tolerance = acceptance["q80"]["interaction_absolute_error"]
            record["accuracy_goal_met"] = goal(lower, upper, tolerance)
            unresolved = row["method_id"] == "smolyak-delta" and level < dimension
            record["analytic_underresolution_control"] = unresolved
            if unresolved:
                gate("underresolution-identity", candidate["value"] == 0.0 and record["accuracy_goal_met"] is False)
            else:
                gate("required-product-moment", upper <= tolerance)
        else:
            finest = 3 if row["method_id"] == "tensor-clenshaw-curtis" else 4
            tolerance = acceptance["q80"]["smooth_tensor_finest_error" if finest == 3 else "smooth_sparse_finest_error"]
            record["accuracy_goal_met"] = goal(lower, upper, tolerance)
            if level == finest:
                gate("required-finest-accuracy", upper <= tolerance)
    record["accuracy_goal_state"] = ("met" if record["accuracy_goal_met"] is True else
                                     "unmet" if record["accuracy_goal_met"] is False else "unresolved")
    return record, checks
