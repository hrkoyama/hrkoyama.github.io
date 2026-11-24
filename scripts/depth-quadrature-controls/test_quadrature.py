"""Small component/causal controls; the105 primary rows run separately."""
from pathlib import Path
import ast
import hashlib
import json
import math
import sys
import numpy as np
import pytest
import cubature
import double_exponential as de
import experiments
import gk15
import io_contract
import quadpack_adapter as qa
import reference_cache
from simpson_baseline import adaptive_simpson

SOURCE = Path(__file__).resolve().parent


def config():
    return json.loads((SOURCE/"inputs.json").read_text())


def test_fixed_input_inventory():
    rows = config()["primary_rows"]
    assert len(rows) == len({r["row_id"] for r in rows}) == 105
    assert [sum(r["sequence"] == i for r in rows) for i in (78, 79, 80)] == [30, 33, 42]
    assert all(set(r) == set(rows[0]) for r in rows)
    assert all(r["relative_tolerance"] == 0 for r in rows if r["sequence"] == 78)


def test_kronrod_degree23():
    for degree in range(24):
        exact = 0 if degree % 2 else 2/(degree+1)
        assert abs(gk15.panel(lambda x: x**degree, -1, 1)["value"]-exact) <= 2e-13


def test_gauss_degree13():
    for degree in range(14):
        value = gk15.WG[3]*0.0**degree+math.fsum(gk15.WG[j]*((-gk15.X[i])**degree+gk15.X[i]**degree)
                                                        for j, i in enumerate((1, 3, 5)))
        assert abs(value-(0 if degree % 2 else 2/(degree+1))) <= 2e-13


def test_shared15_callback_inventory():
    calls = []
    gk15.panel(lambda x: calls.append(x) or math.exp(x), -1, 1)
    assert len(calls) == len(set(calls)) == 15


def test_reversed_panel_orientation():
    forward = gk15.panel(math.exp, 0, 1)
    reverse = gk15.panel(math.exp, 1, 0)
    assert abs(forward["value"]+reverse["value"]) < 1e-14
    assert reverse["estimated_error"] >= 0


def test_gk_cannot_start14_evaluations():
    with pytest.raises(ValueError):
        gk15.adaptive(math.exp, 0, 1, 1e-9, 14, 128, 24)


def test_gk_explicit_budget_unmet():
    result = gk15.adaptive(lambda x: abs(x-13/100), 0, 1, 1e-16, 15, 128, 24)
    assert result["evaluations"] == 15
    assert result["converged"] is False and result["termination"] == "evaluation_budget"


def test_gk_nonfinite_rejected():
    with pytest.raises(ValueError):
        gk15.panel(lambda x: float("nan"), 0, 1)


def test_adaptive_call_identity():
    result = gk15.adaptive(math.exp, 0, 1, 1e-8, 4095, 128, 24)
    assert result["evaluations"] == 15+30*(len(result["panels"])-1)
    assert abs(result["value"]-math.expm1(1)) < 1e-12


def test_de_center_jacobian():
    for kind, value in [("smooth-exponential", math.exp(.5)),
                        ("algebraic-inverse-cuberoot", 2**(1/3)),
                        ("log-endpoint", math.log(2))]:
        x, transformed, _, _ = de.transformed(kind, 0)
        assert x == .5 and abs(transformed-value*math.pi/4) < 2e-14


def test_stable_de_endpoints_without_clipping():
    for kind in ("smooth-exponential", "algebraic-inverse-cuberoot", "log-endpoint"):
        for t in (-4, 4):
            x, value, logx, logone = de.transformed(kind, t)
            assert 0 <= x <= 1 and value > 0 and all(math.isfinite(v) for v in (x, value, logx, logone))
            assert logx < 0 and logone < 0


def test_de_full_endpoint_sum_and_count():
    result = de.integrate("smooth-exponential", 1/16, 4)
    assert result["evaluations"] == len(result["rows"]) == 129
    assert result["value"] == (1/16)*math.fsum(r[2] for r in result["rows"])
    assert result["half_endpoint_correction"] > 0


def test_de_noninteger_cutoff_rejected(tmp_path, monkeypatch):
    with pytest.raises(ValueError):
        de.integrate("smooth-exponential", .3, 4)
    row = next(r for r in config()["primary_rows"] if r["method_id"] == "finite-tanh-sinh")
    monkeypatch.setattr(de, "transformed", lambda *a: (_ for _ in ()).throw(RuntimeError("transform failure")))
    with pytest.raises(RuntimeError, match="transform failure"):
        experiments.run_row(row, tmp_path, {}, {})
    stem = row["row_id"].replace(":", "__")
    status = json.loads((tmp_path/"raw"/(stem+"-callback-status.json")).read_text())
    assert status["last_attempt"] == {"point": -3.0, "completed": False}
    with np.load(tmp_path/"raw"/(stem+"-callbacks.npz")) as raw:
        assert len(raw["values"]) == 0


def test_nested_rational_angle_keys():
    for level in range(1, 5):
        keys = {k for k, _ in cubature.cc_items(level)}
        assert {k for k, _ in cubature.cc_items(level-1)} <= keys
        assert (0, 1) in keys and (1, 1) in keys and (1, 2) in keys
    assert cubature.coordinate((1, 2)) == .5


def test_noncanonical_angle_inputs_rejected():
    with pytest.raises(ValueError):
        cubature.angle_key(1, 3)
    with pytest.raises(ValueError):
        cubature.coordinate((2, 4))


def test_clenshaw_curtis_moments():
    for level in range(1, 5):
        for degree in range(2**level+1):
            actual = math.fsum(w*cubature.coordinate(k)**degree for k, w in cubature.cc_items(level))
            assert abs(actual-1/(degree+1)) <= 2e-13


def test_delta_combination_independent_assembly():
    for dimension in (2, 3):
        for level in (0, 1, 2):
            a, b = [cubature.assemble(dimension, level, method) for method in ("delta", "combination")]
            wa, wb = dict(zip(a["keys"], a["weights"])), dict(zip(b["keys"], b["weights"]))
            assert set(wa) == set(wb)
            assert max(abs(wa[k]-wb[k]) for k in wa) <= 1e-12*max(1, a["sum_absolute_weights"])


def test_unresolved_interaction_identity():
    for dimension in (2, 3, 4):
        for level in range(1, dimension):
            result = cubature.integrate("interaction-product", dimension, level, "delta", 10000)
            assert result["value"] == 0 and (1/12)**dimension > 0


def test_tensor_interaction_exact_moment():
    for dimension in (2, 3, 4):
        result = cubature.integrate("interaction-product", dimension, 1, "tensor", 10000)
        assert abs(result["value"]-(1/12)**dimension) <= 2e-13


def test_cubature_cap_before_callbacks(tmp_path, monkeypatch):
    calls = []
    with pytest.raises(ValueError):
        cubature.integrate("smooth-product", 2, 1, "tensor", 1, lambda x, y: calls.append(x))
    assert calls == []
    row = next(r for r in config()["primary_rows"] if r["method_id"] == "tensor-clenshaw-curtis"
               and r["dimension"] == 2)
    monkeypatch.setattr(cubature, "integrand", lambda *a: (_ for _ in ()).throw(RuntimeError("integrand failure")))
    with pytest.raises(RuntimeError, match="integrand failure"):
        experiments.run_row(row, tmp_path, {}, {})
    stem = row["row_id"].replace(":", "__")
    status = json.loads((tmp_path/"raw"/(stem+"-callback-status.json")).read_text())
    assert status["last_attempt"] == {"point": [0.0, 0.0], "completed": False}
    with np.load(tmp_path/"raw"/(stem+"-callbacks.npz")) as raw:
        assert len(raw["values"]) == 0


def test_canonical_unique_evaluation_ledger():
    calls = []
    result = cubature.integrate("smooth-product", 2, 2, "delta", 10000, lambda x, y: calls.append(x))
    assert result["evaluations"] == result["unique_nodes"] == len(calls) == len(set(calls))
    assert result["assembly_duplicates"] == result["assembly_contributions"]-len(calls)


def test_quadpack_dispatch_is_explicit():
    for row in config()["primary_rows"]:
        if row["method_id"] == "specialized-quadpack":
            _, _, _, options, routine = qa.dispatch(row)
            assert options["epsrel"] == 0 and options["epsabs"] == row["absolute_tolerance"]
            assert routine in ("qagie", "qawfe", "qawoe", "qagpe")
            assert not ("weight" in options and "points" in options)


def test_weight_breakpoint_conflict_rejected():
    with pytest.raises(ValueError):
        qa.validate_options({"weight": "sin", "points": [.5], "epsabs": 1e-9, "epsrel": 0})


def test_baseline_function_source_unchanged():
    tree = ast.parse((SOURCE/"simpson_baseline.py").read_text())
    node = next(n for n in tree.body if isinstance(n, ast.FunctionDef))
    lines = (SOURCE/"simpson_baseline.py").read_text().splitlines(keepends=True)
    text = "".join(lines[node.lineno-1:node.end_lineno])
    assert hashlib.sha256(text.encode()).hexdigest() == "0e3cb4e0f9705868986edcf1d9aaa01004b1e639b37aeeed77f4666af8f5c258"


def test_existing_simpson_cubic_control():
    result = adaptive_simpson(lambda x: x**3, 0, 1, 1e-10, 129, 8)
    assert result["converged"] and abs(result["value"]-.25) <= 1e-14


def test_singular_baseline_preserves_attempt_and_prefix(tmp_path):
    row = next(r for r in config()["primary_rows"] if r["integrand_id"] == "internal-root"
               and r["method_id"] == "simpson-companion")
    record, checks = experiments.run_row(row, tmp_path, {}, {})
    assert record["termination"] == "singular_node_control" and record["accuracy_goal_met"] is None
    stem = row["row_id"].replace(":", "__")
    status = json.loads((tmp_path/"raw"/(stem+"-callback-status.json")).read_text())
    assert status["last_attempt"] == {"point": .375, "completed": False}
    with np.load(tmp_path/"raw"/(stem+"-callbacks.npz")) as raw:
        assert len(raw["values"]) == status["completed_callbacks"] > 0
    assert checks and all(checks.values())


def test_completed_candidate_saved_before_diagnostic_failure(tmp_path, monkeypatch):
    row = next(r for r in config()["primary_rows"] if r["integrand_id"] == "gaussian-whole-line"
               and r["method_id"] == "simpson-companion")
    monkeypatch.setattr(experiments, "error_interval", lambda *a: (_ for _ in ()).throw(RuntimeError("diagnostic failure")))
    with pytest.raises(RuntimeError, match="diagnostic failure"):
        experiments.run_row(row, tmp_path, {"q78:gaussian-finite": {}},
                            {"q78": {"specialized_absolute_error_factor": 20}})
    stem = row["row_id"].replace(":", "__")
    assert (tmp_path/"raw"/(stem+".npz")).exists()
    candidate = json.loads((tmp_path/"raw"/(stem+".json")).read_text())
    assert math.isfinite(candidate["value"]) and candidate["evaluations"] > 0


def test_cache_refuses_stale_input(monkeypatch):
    original = reference_cache.digest
    monkeypatch.setattr(reference_cache, "digest",
                        lambda path: "0"*64 if Path(path).name == "inputs.json" else original(path))
    with pytest.raises(ValueError, match="stale"):
        reference_cache.load(SOURCE)


def test_raw_nonfinite_is_saved_before_finite_metadata(tmp_path):
    io_contract.save_candidate(tmp_path, "invalid", {"ratio": math.inf, "array": np.array([math.nan])})
    metadata = json.loads((tmp_path/"invalid.json").read_text())
    assert metadata["ratio"]["raw_nonfinite_scalar"]
    with np.load(tmp_path/"invalid.npz") as raw:
        assert math.isinf(raw["candidate__ratio"]) and math.isnan(raw["candidate__array"][0])


def test_numeric_csv_has_no_nonfinite_cells(tmp_path):
    path = tmp_path/"numeric.csv"
    io_contract.write_csv(path, [{"sequence": 78, "value": 1, "converged": False, "accuracy_goal_met": None}])
    assert "False" not in path.read_text()
    with pytest.raises(ValueError):
        io_contract.write_csv(path, [{"value": math.inf}])
