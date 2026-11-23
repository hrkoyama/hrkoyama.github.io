"""Fresh lightweight checks of reused ExactPack eigenvalue evidence.

This does not repeat nonlinear eigenvalue shooting or the original state() calls.
It checks their retained bindings, one critical-phase residual, a fresh dense ODE
and fresh quadrature/field agreement against the recorded original computation.
"""
import argparse
import hashlib
import json
from pathlib import Path
import time
import traceback
import numpy as np
from .precollapse import (REFERENCE_DIR, GuderleyReference, load_eigenvalue_cache,
                         critical_phase_residual, RHO0, OUTER_RADIUS, TIME0, TIME1)


def qualify():
    contract = json.loads((REFERENCE_DIR/"cache-contract.json").read_text())
    for name,digest in contract["files_sha256"].items():
        if hashlib.sha256((REFERENCE_DIR/name).read_bytes()).hexdigest() != digest:
            raise RuntimeError("changed cached-reference contract input: " + name)
    proof = load_eigenvalue_cache()
    reference = GuderleyReference()
    cdiff = critical_phase_residual()
    original = json.loads((REFERENCE_DIR/"attempts/01-eigenvalue-recompute/qualification.json").read_text())
    points = []
    maximum_point_difference = 0.
    for row in original["original_state_calls"]:
        t,r = row["t"],row["r"]
        state = np.array([float(a) for a in reference.point_state(np.array(r),t)])
        wanted = np.array(row["original_rho_u_p"])
        speed = abs(reference.shock_speed(t))
        difference = float(np.max(abs(state-wanted)/np.array([RHO0,speed,RHO0*speed**2])))
        maximum_point_difference=max(maximum_point_difference,difference)
        points.append({"t":t,"r":r,"fresh_dense_rho_u_p":state.tolist(),
                       "archived_original_rho_u_p":wanted.tolist(),"scaled_difference":difference})
    maximum_quadrature_difference = 0.
    quadrature = []
    for n in [128,256,512]:
        edges = np.linspace(0,OUTER_RADIUS,n+1)
        for t in [TIME0,TIME1]:
            q16,p16=reference.cell_means(edges,t,16)
            q32,p32=reference.cell_means(edges,t,32)
            speed=abs(reference.shock_speed(t))
            difference=float(np.max(abs(q16-q32)/np.array([RHO0,RHO0*speed,RHO0*speed**2])))
            pressure_difference=float(np.max(abs(p16-p32))/(RHO0*speed**2))
            maximum_quadrature_difference=max(maximum_quadrature_difference,difference,pressure_difference)
            quadrature.append({"N":n,"t":t,"scaled_q_difference":difference,
                               "scaled_pressure_difference":pressure_difference})
    metadata=reference.metadata()
    checks={
        "cache and original qualification contract/source bindings verified":proof["original_source_files_checked"]==12,
        "default adapter reuses the qualified exponent without full shooting":metadata["eigenvalue_provenance"]["eigenvalue_recomputed"] is False and reference.lambda_==proof["lambda"],
        "one fresh critical-phase residual below unchanged2e-7":abs(cdiff)<2e-7,
        "fresh dense ODE completed the fixed pre-collapse branch":bool(reference.solution.success and np.all(np.isfinite(reference.solution.y))),
        "fresh dense fields match eight archived original states within unchanged5e-6":maximum_point_difference<5e-6,
        "fresh split Gauss16/32 means agree within unchanged2e-7":maximum_quadrature_difference<2e-7,
    }
    return {"schema_version":1,"kind":"cached-eigenvalue-fresh-reference-qualification",
            "passed":all(checks.values()),"checks":checks,"metadata":metadata,
            "eigenvalue_cache_proof":proof,"fresh_Cdiff":cdiff,
            "maximum_archived_point_scaled_difference":maximum_point_difference,
            "archived_point_comparisons":points,
            "maximum_Gauss16_32_scaled_difference":maximum_quadrature_difference,
            "quadrature":quadrature,"full_eigenvalue_shooting_executed":False,
            "original_state_calls_rerun":False,"fresh_original_state_calls":0,
            "fresh_critical_phase_calls":1,"pde_evolution_executed":False,
            "physical_inputs_changed":False,"acceptance_changed":False,
            "scope":"Reuse the computed exponent and historical original-code checks; freshly check the same ODE/quadrature without repeating root shooting."}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output",type=Path,required=True)
    args=parser.parse_args()
    if args.output.exists():parser.error("choose a new output path")
    started=time.monotonic()
    try:
        report=qualify()
    except Exception as error:
        report={"schema_version":1,"passed":False,"exception":type(error).__name__,
                "message":str(error),"traceback":traceback.format_exc(),
                "full_eigenvalue_shooting_executed":False,"pde_evolution_executed":False}
    report["duration_seconds"]=time.monotonic()-started
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(report,indent=2,allow_nan=False)+"\n")
    print(json.dumps({k:report[k] for k in ["passed","duration_seconds"]}))
    raise SystemExit(0 if report["passed"] else 1)


if __name__=="__main__":main()
