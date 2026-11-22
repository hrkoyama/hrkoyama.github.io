# Lie–Trotter / Strang on the same nonlinear reaction–diffusion input

This small teaching example integrates the nondimensional Schnakenberg system

`u_t = 0.01 u_xx + 0.1 − u + u²v`,
`v_t = 1.0 v_xx + 0.9 − u²v`

on the periodic interval `[0,2π)` with 32 grid points, ending at `T=1`.
It reuses the coefficients and finite-amplitude initial field of the earlier
Schnakenberg examples, with a new, shorter final time. It is an additional
comparison of the existing problem, not an additional physical problem family.
The old nonlinear/transient/pattern releases, criteria and results are retained.

The initial field is
`u=1+0.08 cos(2x)+0.01 cos(4x)`,
`v=0.9−0.03 cos(2x)−0.002 cos(4x)`.
It is reflection-even and π-periodic within the declared 2π cell.

## Reproduce

Use Python 3.10+ and a new environment:

```text
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output new-results
```

The three scientific/test requirements are pinned. No network, private source
checkout, plotting or quantum-chemistry library is needed during execution.
Outputs must go into a new or empty directory; existing results are not replaced.
`result.json`, `reaction-diffusion-splitting.csv` and `time-errors.csv` contain
the input hash, complete fixed-time errors, acceptance flags and stopping reason.
The solver budget is capped at 60 seconds; this is a cap, not a performance claim.

To redraw a figure from saved results (without rerunning the solver):

```text
python -m pip install -r requirements-plotting.txt
python plot.py --results new-results/result.json --output new-results
```

## Matched algorithms

Both methods use the SAME grid, initial state, steps, observation times, FD2
diffusion matrix, and implicit-midpoint reaction solver with the same Newton
tolerance/cap. Diffusion is the exact exponential of that FD matrix, applied by
FFT using `−4 sin²(πk/N)/dx²`. FFT is only a diagonalization: this is not continuum
spectral diffusion. There is no clipping, adaptive change of step or fallback.

Lie–Trotter applies a full diffusion step and then a full reaction step.
Strang applies half diffusion, full reaction, half diffusion, always updating
the current state. Each composition advances the original problem by `h`.
The four fixed step counts are 16, 32, 64 and 128. Adjacent diffusion half steps
are deliberately not merged: reported call counts are actual calls in this code.
The reaction step is a second-order approximation, not an exact reaction flow.
Measured temporal errors therefore include both composition error and midpoint
reaction discretization error. Newton sensitivity is checked separately.

## Reference and acceptance scope

`reference.py` independently assembles a REAL-SPACE periodic FD matrix and
implements the unsplit RHS and analytic Jacobian. SciPy Radau integrates the SAME
semidiscrete system. A tighter Radau run and DOP853 provide tolerance and
independent-time-algorithm controls. The reference imports no splitting, FFT or
midpoint implementation. It is a numerical time reference, not an independent
PDE implementation or an exact continuum solution.

All five output times `0,0.25,0.5,0.75,1` are shared by both schemes. For each
species compute mean absolute error, RMS error and maximum error over the grid,
then take the worse species. Refinement uses the maximum of each norm over the
four positive observation times. Observed order is `log2(E(h)/E(h/2))`.
Final profiles and all individual observation errors are also retained.

Acceptance is predeclared in `inputs.json`: first-/second-order windows,
absolute errors, reference and Newton contamination bounds, positive tested
substep concentrations, residuals and source/sink balance. The first fixed
protocol passed without changing any input or acceptance bound. See the
input hashes and first-run record in `protocol-history.json`.

The total concentration is NOT conserved:
`d mean(u+v)/dt = a+b−mean(u)`. The reaction-midpoint discrete balance is checked;
periodic diffusion preserves each species mean. Positive values in this fixed
run do not establish unconditional positivity of implicit midpoint or splitting.
A reversed Lie ordering is a noncommutation control, not a third method claim.
An exact commuting linear-reaction control appears in the tests to show why a
constant scalar reaction with constant diffusion would hide splitting error.

No spatial convergence, general pattern selection, long-time saturation, 2D,
nonperiodic boundary, biological calibration or arbitrary stiff-PDE claim is
made. This short test does not replace the earlier finite-amplitude and
saturated-pattern validations or rerun them. Software is MIT; prose, fixed
inputs, generated numbers and figures retain the site's separate reuse terms.
See `LICENSE`, the public site `LICENSING.md`, and `cases.json` for references.
