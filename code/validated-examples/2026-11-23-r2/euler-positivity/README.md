# Euler double rarefaction: stage-by-stage positivity

This lightweight example connects a mean-preserving reconstruction component
to a complete, limited-scope conservative update. It extends the existing
`double-rarefaction` problem; it is not a new two-dimensional flow solver.

The fixed input is ideal-gas Euler, gamma=1.4, x in [0,1], x0=.5, primitive
states (rho,u,p)=(1,-2,.4)/(1,2,.4), final time .15 and N=128/256/512.
Both exterior states remain fixed at the domain boundaries; the analytic
fan fronts remain inside the interval through final time. Actual numerical
boundary fluxes, rather than presumed analytic zero losses, enter budgets.

## Reconstruction and sufficient condition

Conservative central slopes define two endpoints A=Ubar-delta and
B=Ubar+delta. Their Lobatto quadrature weights are each 1/2. One common
affine theta per cell is used for density and pressure, preserving Ubar.
Density is bounded analytically and pressure by ideal-gas concavity and
bisection. Epsilon=1e-13 is an endpoint reconstruction target. It is not
mass/energy added to a state; an inadmissible mean causes failure.

Let a=4, z=dt*a/dx<=.4, D be the right endpoint of the left neighbor and
C the left endpoint of the right neighbor. The LF forward-Euler mean is

    .5*(1-2*z)*(A+B)
    +.5*z*(A+F(A)/a) + .5*z*(B-F(B)/a)
    +.5*z*(D+F(D)/a) + .5*z*(C-F(C)/a).

For z<=1/2 these weights are nonnegative and sum to one. Ideal-gas Euler
LF split states are positive when a bounds |u|+c at every endpoint. The
program checks that bound on every actual face and fails if it is violated.
SSPRK(3,3) combines these FE updates with nonnegative coefficients; the
reconstruction and endpoint limiting are repeated before each FE flux.
This is a conditional sufficient positivity argument for this P1 FV update,
not a proof for every MUSCL, WENO or DG implementation. The central slopes
are unlimited; positivity does not imply TVD or absence of oscillations.

Every FE result and every SSP convex combination has its own density and
pressure minimum and actual boundary-budget defect. Global boundary flux
weights are 1/6,1/6,2/3. Raw nonpositive endpoint density is counted
separately; raw pressure is evaluated only at positive-density endpoints.
Negative reconstructed endpoint pressure is recorded before scaling; an
invalid raw polynomial is never fed to the Euler flux. There are no hidden
state clipping, floor injections, rejected steps or retries.

## Reference and frozen verification

`references/double_rarefaction.py` evaluates the symmetric rarefactions
from the analytic Riemann invariants. This input is non-vacuum: the center
has positive density and pressure. Conserved cell means split integration
at the four fan boundaries, using Gauss8 and a Gauss16 cross-check. Pressure
is p(mean conserved q), not mean primitive pressure. An unchanged released
Numart logarithmic-root evaluator supplies a separate algebraic check,
not a separate numerical PDE engine. Source roles/review limits and the
vendored MIT notice are preserved under `references/`.

`pre-run-contract.json` binds the inputs, acceptance conditions, numerical
sources and reference sources before the first tests and PDE runs.
The fixed budget is 27 pytest tests and 3 refinements with 73 numerical
gates, sharing a 120-second group budget on public Linux verification.
No tolerance or physical input is adjusted after observing results.

```sh
python -m pip install -r requirements.txt
python -W error -m pytest -q
python -W error run.py --input inputs.json --output new-results
python -m pip install -r requirements-plot.txt
python -W error plot.py --results new-results/result.json --output new-figures
```

Use a fresh empty output directory. `run.py` saves per-stage diagnostics,
full final/reference conserved arrays, sampled time history, errors,
refinement, budgets, source hashes and raw failure arrays if a stage fails.
The gallery preview uses actual saved x-t density/pressure arrays. It is
not a two-dimensional flow computation. Plotting never runs the solver.

This example does not cover vacuum-generating inputs, other EOS, wall
boundaries, multidimensional admissibility, long-time behavior or a general
positivity guarantee for other reconstruction/flux/time-integrator choices.
No ExactPack code is executed in this case; the closed non-vacuum solution
is available directly. See `LICENSE` and the separate third-party notice.
