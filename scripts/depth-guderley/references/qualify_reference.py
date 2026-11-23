"""Bounded qualification of actual pinned ExactPack and its dense adapter.

No finite-volume PDE evolution, reflected-shock solve or parameter scan occurs.
Run from the distribution root: python -m references.qualify_reference --output ...
"""
import argparse
import json
from pathlib import Path
import time
import traceback
import numpy as np
from scipy.optimize import brentq
from .precollapse import (GuderleyReference, GAMMA, RHO0, SHOCK_SCALE, TIME0,
                         TIME1, OUTER_RADIUS, TABULATED_LAMBDA, TABULATED_ALPHA)
from .exactpack_guderley import eexp as exponent_module
from .exactpack_guderley import ramsey


def qualify():
    ref = GuderleyReference()
    metadata = ref.metadata()
    alpha = ref.alpha
    cdiff = float(exponent_module.Cdiff(alpha, 3, GAMMA))
    rhs_samples = np.linspace(-1, ref.x_end, 513)
    yy = ref.similarity(rhs_samples)
    discriminant = yy[1]**2 - (1+yy[0])**2
    critical = []
    for a, b, fa, fb in zip(rhs_samples[:-1], rhs_samples[1:], discriminant[:-1], discriminant[1:]):
        if fa*fb < 0:
            xx = brentq(lambda x: float(ref.similarity(x)[1]**2-(1+ref.similarity(x)[0])**2), a, b)
            critical.append({"x":float(xx), "r_over_Rs":float((-xx)**(-alpha)),
                             "VCR":ref.similarity(xx).tolist()})
    comparison = []
    maximum_original_difference = 0.
    for t in [TIME0, TIME1]:
        rs = ref.shock_radius(t)
        D = abs(ref.shock_speed(t))
        for ratio in [1.01,1.04,1.08,1.20]:
            r = ratio*rs
            actual = np.array([float(a) for a in ref.point_state(np.array(r), t)])
            # This is the actual unchanged ramsey.state path, without the
            # unnecessary post-reflection B solve of the public wrapper.
            original = ramsey.state(r/SHOCK_SCALE, RHO0, 3, GAMMA,
                                    ref.lambda_, 0., t*(SHOCK_SCALE/r)**ref.lambda_)
            wanted = np.array([original[0], SHOCK_SCALE*original[1], SHOCK_SCALE**2*original[2]])
            error = float(np.max(np.abs(actual-wanted)/np.array([RHO0,D,RHO0*D**2])))
            maximum_original_difference = max(maximum_original_difference,error)
            comparison.append({"t":t,"r":r,"r_over_Rs":ratio,"dense_rho_u_p":actual.tolist(),
                               "original_rho_u_p":wanted.tolist(),"scaled_difference":error})
    maximum_quadrature_difference = 0.
    quadrature = []
    for n in [128,256,512]:
        edges = np.linspace(0,OUTER_RADIUS,n+1)
        for t in [TIME0,TIME1]:
            q16,p16 = ref.cell_means(edges,t,16)
            q32,p32 = ref.cell_means(edges,t,32)
            D=abs(ref.shock_speed(t))
            scale=np.array([RHO0,RHO0*D,RHO0*D**2])
            difference=float(np.max(np.abs(q16-q32)/scale))
            pdiff=float(np.max(np.abs(p16-p32))/(RHO0*D**2))
            maximum_quadrature_difference=max(maximum_quadrature_difference,difference,pdiff)
            quadrature.append({"N":n,"t":t,"scaled_q_difference":difference,"scaled_pressure_difference":pdiff})
    downstream=np.array([float(a) for a in ref.point_state(np.array(ref.shock_radius(TIME0)),TIME0)])
    D=ref.shock_speed(TIME0)
    analytic=np.array([(GAMMA+1)/(GAMMA-1)*RHO0, 2*D/(GAMMA+1),2*RHO0*D*D/(GAMMA+1)])
    jump_error=float(np.max(np.abs(downstream-analytic)/np.array([RHO0,abs(D),RHO0*D**2])))
    cold=ref.point_state(np.linspace(0,.99*ref.shock_radius(TIME1),31),TIME1)
    checks={
        "computed lambda matches archived Lazarus spherical gamma1.4 table within1e-7":abs(ref.lambda_-TABULATED_LAMBDA)<1e-7,
        "computed alpha matches official ExactPack regression within1e-7":abs(alpha-TABULATED_ALPHA)<1e-7,
        "critical-phase matching residual below2e-7":abs(cdiff)<2e-7,
        "dense ODE reached entire fixed branch and is finite":bool(ref.solution.success and np.all(np.isfinite(yy))),
        "cold upstream is rho1 u0 p0 exactly":bool(np.all(cold[0]==RHO0) and np.all(cold[1]==0) and np.all(cold[2]==0)),
        "strong-shock jump scaled error below2e-12":jump_error<2e-12,
        "eight calls to unchanged original state agree within5e-6":maximum_original_difference<5e-6,
        "split-shock Gauss16/32 conserved and pressure averages agree within2e-7":maximum_quadrature_difference<2e-7,
    }
    return {"schema_version":1,"kind":"semi-analytic-reference-qualification",
            "passed":all(checks.values()),"checks":checks,"metadata":metadata,
            "eigenvalue":{"lambda_table":TABULATED_LAMBDA,"alpha_official_test":TABULATED_ALPHA,
                          "Cdiff":cdiff,"critical_points_in_fixed_branch":critical},
            "strong_shock_scaled_error":jump_error,
            "max_original_state_scaled_difference":maximum_original_difference,
            "original_state_calls":comparison,
            "max_Gauss16_32_scaled_difference":maximum_quadrature_difference,
            "quadrature":quadrature,
            "source_scope":"actual pinned eexp and original ramsey.state/RHS; custom dense pre-collapse adapter, not independent implementation",
            "pde_evolution_executed":False,"reflected_branch_executed":False}


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
                "pde_evolution_executed":False,"reflected_branch_executed":False}
    report["duration_seconds"]=time.monotonic()-started
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(report,indent=2,allow_nan=False)+"\n")
    print(json.dumps({k:report[k] for k in ["passed","duration_seconds"]}))
    raise SystemExit(0 if report["passed"] else 1)


if __name__=="__main__":main()
