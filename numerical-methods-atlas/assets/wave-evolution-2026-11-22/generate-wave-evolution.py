#!/usr/bin/env python3
"""Original MIT implementation: matched-time scalar advection diagnostics.

Only the LW curve is a fully discrete Lax-Wendroff update. A is a constructed
amplitude-only diagnostic; B evolves a centered spatial derivative exactly.
"""
import argparse
import hashlib
import json
import platform
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    out = args.output
    if out.exists() and any(out.iterdir()):
        raise SystemExit("Output directory must be absent or empty")
    out.mkdir(parents=True, exist_ok=True)
    p = dict(n=127, domain=[0, 1], advection_speed=1.0, courant=0.8,
             dx=1/127, dt=0.8/127, kappa=60.0, x0=0.25,
             nsteps=160, max_step=160, period=1.0, frame_stride=2, output_decimals=7)
    n, c, dt = p["n"], p["courant"], p["dt"]
    assert n % 2 == 1, "Odd grid avoids the ambiguous real Nyquist translation"
    x = np.arange(n)/n
    theta = 2*np.pi*np.fft.fftfreq(n)
    bump = lambda xx: np.exp(p["kappa"]*(np.cos(2*np.pi*(xx-p["x0"]))-1))
    u0 = bump(x)
    f0 = np.fft.fft(u0)
    upwind = 1-c+c*np.exp(-1j*theta)
    gains = {
        "exact": np.exp(-1j*c*theta),
        "damping_only": abs(upwind)*np.exp(-1j*c*theta),
        "dispersion_only": np.exp(-1j*c*np.sin(theta)),
        "lax_wendroff": 1-1j*c*np.sin(theta)+c*c*(np.cos(theta)-1),
    }
    labels = {"exact": "Exact advection (spectral interpolant)",
              "damping_only": "A: damping only (constructed diagnostic)",
              "dispersion_only": "B: dispersion only (exact semidiscrete evolution)",
              "lax_wendroff": "C: Lax-Wendroff (fully discrete update)"}
    all_steps = np.arange(p["nsteps"]+1)
    complex_values = {k: np.fft.ifft(f0[None, :]*g[None, :]**all_steps[:, None], axis=1)
                      for k, g in gains.items()}
    values = {k: v.real for k, v in complex_values.items()}
    frame_steps = np.arange(0, p["nsteps"]+1, p["frame_stride"])
    decimals = p["output_decimals"]
    data = {"schema_version": 1, "title": "Matched-time wave evolution",
            "parameters": p, "x": np.round(x, 10).tolist(),
            "steps": frame_steps.tolist(), "time": np.round(frame_steps*dt, 10).tolist(),
            "time_in_periods": np.round(frame_steps*dt/p["period"], 10).tolist(),
            "series": {k: np.round(v[frame_steps], decimals).tolist() for k, v in values.items()},
            "labels": labels, "y_limits": [-0.42, 1.08],
            "snapshot_steps": [0, 40, 80, 160]}
    (out/"frames.json").write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":"))+"\n")
    with (out/"snapshots.csv").open("w") as f:
        f.write("step,time,time_in_periods,x,exact,damping_only,dispersion_only,lax_wendroff\n")
        for step in data["snapshot_steps"]:
            for j in range(n):
                nums = [step, step*dt, step*dt/p["period"], x[j]]+[values[k][step,j] for k in gains]
                f.write(",".join(format(v, ".16g") for v in nums)+"\n")

    # Independent real-space LW iteration, not a reuse of its Fourier gain.
    iterate = u0.copy()
    lw_error = 0.0
    for step in all_steps:
        lw_error = max(lw_error, float(np.max(abs(iterate-values["lax_wendroff"][step]))))
        iterate = (iterate-c/2*(np.roll(iterate,-1)-np.roll(iterate,1))
                   +c*c/2*(np.roll(iterate,-1)-2*iterate+np.roll(iterate,1)))
    # Check every discrete Fourier mode against direct stencil applications.
    mode_errors = {"upwind_stencil": 0.0, "centered_derivative": 0.0, "lax_wendroff_stencil": 0.0}
    for j, th in enumerate(theta):
        mode = np.exp(1j*th*np.arange(n))
        up = mode-c*(mode-np.roll(mode,1))
        der = (np.roll(mode,-1)-np.roll(mode,1))/(2*p["dx"])
        lw = mode-c/2*(np.roll(mode,-1)-np.roll(mode,1))+c*c/2*(np.roll(mode,-1)-2*mode+np.roll(mode,1))
        mode_errors["upwind_stencil"] = max(mode_errors["upwind_stencil"], float(np.max(abs(up-upwind[j]*mode))))
        mode_errors["centered_derivative"] = max(mode_errors["centered_derivative"], float(np.max(abs(der-1j*np.sin(th)/p["dx"]*mode))))
        mode_errors["lax_wendroff_stencil"] = max(mode_errors["lax_wendroff_stencil"], float(np.max(abs(lw-gains["lax_wendroff"][j]*mode))))
    physical = bump(x[None,:]-all_steps[:,None]*dt)
    physical_error = float(np.max(abs(values["exact"]-physical)))
    # Numerical tail estimate; this includes floating-point noise, not a bound.
    nfine = 16384
    fine_coeff = np.fft.fft(bump(np.arange(nfine)/nfine))/nfine
    fine_modes = np.fft.fftfreq(nfine)*nfine
    tail = fine_coeff[abs(fine_modes) > (n-1)//2]
    means = {k: np.mean(v,axis=1) for k,v in values.items()}
    l2 = {k: np.sqrt(np.mean(v*v,axis=1)) for k,v in values.items()}
    conservation = {k: {"max_mean_drift":float(np.max(abs(means[k]-means[k][0]))),
                         "max_sum_drift":float(np.max(abs(n*means[k]-n*means[k][0]))),
                         "initial_l2":float(l2[k][0]), "final_l2":float(l2[k][-1]),
                         "final_l2_ratio":float(l2[k][-1]/l2[k][0]),
                         "max_l2_drift":float(np.max(abs(l2[k]-l2[k][0]))),
                         "max_l2_step_increase":float(np.max(np.diff(l2[k])))} for k in gains}
    reality = {k:float(np.max(abs(v.imag))) for k,v in complex_values.items()}
    rounding = {k:float(np.max(abs(v[frame_steps]-np.round(v[frame_steps],decimals)))) for k,v in values.items()}
    fingerprint = hashlib.sha256(json.dumps(p,sort_keys=True,separators=(",", ":")).encode()).hexdigest()
    checks = {
        "all_series_identical_initial_profile": all(np.array_equal(v[0],values["exact"][0]) for v in values.values()),
        "all_values_finite": all(bool(np.all(np.isfinite(v))) for v in values.values()),
        "lw_independent_stencil": lw_error < 2e-13,
        "mode_stencils": max(mode_errors.values()) < 5e-10,
        "real_outputs": max(reality.values()) < 2e-13,
        "physical_reference_matches_interpolant": physical_error < 2e-12,
        "all_means_preserved": max(a["max_mean_drift"] for a in conservation.values()) < 2e-14,
        "damping_only_l2_nonincreasing": conservation["damping_only"]["max_l2_step_increase"] < 2e-14,
        "lax_wendroff_l2_nonincreasing": conservation["lax_wendroff"]["max_l2_step_increase"] < 2e-14,
        "dispersion_only_l2_preserved": conservation["dispersion_only"]["max_l2_drift"] < 2e-13,
        "damping_gain_at_most_one": float(np.max(abs(gains["damping_only"]))) <= 1+2e-15,
        "dispersion_gain_unit": float(np.max(abs(abs(gains["dispersion_only"])-1))) < 5e-16,
        "damping_phase_is_exact": float(np.max(abs(gains["damping_only"]-abs(upwind)*gains["exact"]))) < 1e-15,
        "json_rounding_at_most_5e_minus_8": max(rounding.values()) <= 5.00001e-8,
    }
    assert all(checks.values()), checks
    plt.rcParams.update({"font.size":10,"axes.spines.top":False,"axes.spines.right":False})
    fig, axs = plt.subplots(3,3,figsize=(11.6,7.0),sharex=True,sharey=True)
    colors = ["#a24722", "#326c94", "#67509b"]
    names = list(gains)[1:]
    closed_x = np.r_[x,1]
    for row,(key,color) in enumerate(zip(names,colors)):
        for col,step in enumerate([40,80,160]):
            ax = axs[row,col]
            ax.plot(closed_x,np.r_[values[key][step],values[key][step,0]],color=color,lw=2,label=labels[key].split(": ",1)[1].split(" (")[0])
            ax.plot(closed_x,np.r_[values["exact"][step],values["exact"][step,0]],color="#24282d",ls="--",lw=1.3,label="exact advection")
            ax.axhline(0,color="#b6bcc2",lw=.65)
            ax.set(xlim=(0,1),ylim=(-.42,1.08),xticks=[0,.25,.5,.75,1],yticks=[-.4,0,.5,1])
            ax.grid(alpha=.14)
            if row == 0: ax.set_title(f"step {step}: t = {step*dt:.4f} periods")
            if col == 0: ax.set_ylabel(["A  Damping only\n(constructed diagnostic)","B  Dispersion only\n(exact semidiscrete)","C  Lax–Wendroff\n(actual update)"][row])
            if row == 2: ax.set_xlabel("periodic coordinate x")
            if col == 2: ax.legend(loc="upper right",frameon=False,fontsize=8)
    fig.suptitle("One initial wave, identical times: damping, dispersion, and their combination",fontsize=14,y=.985)
    fig.text(.5,.935,"uₜ + uₓ = 0  ·  N = 127  ·  C = 0.8  ·  positive periodic bump, κ = 60  ·  shared axes",ha="center",fontsize=10)
    fig.text(.5,.012,"A uses upwind gain with exact phase. B evolves the centered spatial derivative exactly in time (no RK4). Dashed: shifted initial interpolant.",ha="center",fontsize=8.6)
    fig.subplots_adjust(top=.87,bottom=.09,left=.105,right=.985,hspace=.14,wspace=.17)
    fig.savefig(out/"overview.png",dpi=170)
    plt.close(fig)
    result = {"schema_version":1,"parameters":p,"parameter_sha256":fingerprint,
              "initial_float64_le_sha256":hashlib.sha256(u0.astype("<f8").tobytes()).hexdigest(),
              "equation":"u_t + a u_x = 0, periodic x in [0,1), a=1",
              "initial_profile":"exp(kappa*(cos(2*pi*(x-x0))-1))",
              "multipliers":{"exact":"exp(-i*C*theta)","damping_only":"abs(1-C+C*exp(-i*theta))*exp(-i*C*theta)",
                             "dispersion_only":"exp(-i*C*sin(theta))","lax_wendroff":"1-i*C*sin(theta)+C^2*(cos(theta)-1)"},
              "scope":"Scalar linear advection only; constructed diagnostic A and exact semidiscrete B are not claimed to be standard fully discrete schemes. No shock data, nonlinear KEEP solver result, or new atlas problem count.",
              "conservation":conservation,
              "final_extrema":{k:{"min":float(v[-1].min()),"max":float(v[-1].max())} for k,v in values.items()},
              "versions":{"python":platform.python_version(),"numpy":np.__version__,"matplotlib":matplotlib.__version__}}
    (out/"result.json").write_text(json.dumps(result,indent=2)+"\n")
    verification = {"passed":True,"checks":checks,"lw_max_abs_error":lw_error,
                    "mode_max_abs_errors":mode_errors,"max_imaginary_residual":reality,
                    "exact_vs_physical_bump_max_abs_error_all_steps":physical_error,
                    "physical_reference_note":"Exact curves translate the N-point trigonometric interpolant. The physical analytic bump differs by negligible spectral sampling/truncation error; measured on all 161 times and 127 grid points.",
                    "dense_fourier_tail_estimate":{"samples":nfine,"cutoff_abs_mode":63,"l1":float(np.sum(abs(tail))),"l2":float(np.sqrt(np.sum(abs(tail)**2))),"note":"Numerical estimate, includes floating-point noise; not an analytic rigorous bound."},
                    "output_quantization_max_abs_error":rounding,
                    "input_parameter_sha256":fingerprint,"generator_sha256":sha(__file__),
                    "files":{p.name:{"bytes":p.stat().st_size,"sha256":sha(p)} for p in sorted(out.iterdir()) if p.is_file()}}
    (out/"verification.json").write_text(json.dumps(verification,indent=2)+"\n")
    print(json.dumps({"output":str(out),"checks_passed":all(checks.values()),"json_bytes":(out/"frames.json").stat().st_size,"physical_reference_error":physical_error,"lw_stencil_error":lw_error}))


if __name__ == "__main__":
    main()
