# Sedov–Taylor point blast: a small spherical-radial verification

This is **one-dimensional spherical-radial Euler**, not a 2D Cartesian blast.
The colored gallery picture is a section display of the saved radial density.
The source, point-blast reference, reference-development record and actual
first numerical attempt are all included. Original implementation code follows
`LICENSE`; figures, prose, inputs and outputs retain the site's separate terms.
The unmodified third-party BSD-3-Clause text is `exactpack-LICENSE.txt`.

## Run the fixed verification

Use Python3.12 and the three pinned public-wheel runtime dependencies:

```sh
python -m venv /path/to/new-env
/path/to/new-env/bin/python -m pip install -r requirements.txt
/path/to/new-env/bin/python -m pytest -q -p no:cacheprovider
/path/to/new-env/bin/python run.py --input inputs.json --output /path/to/new-empty-results
```

No network or private checkout is needed after acquiring the package and
runtime dependencies. A nonempty output directory is rejected. Exit0 means
all frozen scientific gates pass; exit1 retains unmet criteria or a failed
calculation. `result.json` records actual source/input hashes and individual
measurements. A failed RK stage retains raw state and completed history;
there are no pressure seeds, state floors, cell repairs or hidden step retries.
Only plotting additionally needs `requirements-plotting.txt`:

```sh
python -m pip install -r requirements-plotting.txt
python plot.py --results /path/to/results/result.json --output /path/to/new-figures
```

`plot.py` checks saved-result/source hashes and the saved density norm. It does
not import or execute the PDE solver. The release packager independently
extracts the ZIP and actually reruns all22 pytest tests and every fixed input.

## Fixed model and method

- Ideal gas gamma=5/3, ambient density1, zero velocity and **zero** background
  pressure; total injected thermal energy1 with the full4π convention.
- Domain0<=r<=1, final time.05. Uniform heat is deposited inside a **fixed
  physical radius.03** on128,256,512 radial cells. Exact cut-shell volume
  fractions preserve unit initial energy on every mesh.
- A separate512-cell calculation halves the deposition radius to.015. It is
  a source-radius sensitivity probe, not another grid-refinement point.
- Piecewise-constant shared-face Rusanov fluxes and SSPRK2/Heun, CFL.4 using
  V/(A_left+A_right)/(|u|+c). The spherical radial-momentum source
  p(A_right-A_left)/V is integrated in the same RK stages. Origin reflection,
  outer outflow, measured boundary fluxes and geometric-source budgets are
  explicit. Radial momentum is not source-free Cartesian total momentum.
- At extremely small positive cold-tail wave speeds, an unrestrictive local
  timestep ratio overflows to infinity; this warning is retained in the first
  log. The minimum selected global timestep is finite and checked. This does
  not alter conserved states or add a wave-speed/state floor.

## Reference, independent check and error meaning

`reference_sedov.py` independently integrates the continuous similarity ODE
inward from strong-shock jumps with DOP853. It normalizes energy, giving
beta=1.15166641793 and shock radius.34746791233 at time.05. A regular asymptote
for xi<.001 is **approximate**, separately checked at cutoff.0005 and tighter
ODE tolerance. Cell references use split shell quadrature at the shock, with
orders16 and32 checked; these are **semi-analytic quadrature references**, not
closed-form exact cell averages. Reference mass and energy normalizations
are checked separately from the finite-volume solution.

The selected **unmodified** LANL ExactPack Sedov evaluator was independently
executed at commit9bacc477eb791e959c9621e771fc7a725db755fa, npts6001/12001,
gamma5/3, spherical geometry, rho0=E0=1, omega0, t=.05. The probes are
xi=.15,.25,.5,.75,.9,1.05, excluding the small-radius region warned about by
the upstream implementation and the shock jump. `exactpack-snapshot.json`,
`exactpack-receipt.json`, `exactpack-sources.json`, the reproduction script,
license and reference-development evidence preserve hashes, source URLs,
parameters, environment and actual decisions. The comparison criterion5e-4
was declared before that execution; maximum scaled point difference was
.0002737872, and beta differed by1.90e-12 relative. This is an independent
reference **evaluator** comparison, not a second numerical Euler engine,
full ExactPack installation or whole-library validation.

The numerical initial condition is a finite hot sphere; the reference is an
ideal instantaneous point explosion. The reported errors include **both**
finite-source discrepancy and discretization error. Thus the refinement
slope is not a pure spatial order. Active L1 norms use4πr² volume weights
within r<=1.2Rs and include origin and shock; full-domain, L2/Linf and center
values are also retained. Numerical pressure p(mean conserved U) is compared
with the reference **mean physical pressure**, distinct from p(mean reference
conserved U) because of subcell kinetic energy.

## Actual first execution

Before any FV execution (including the small unit-test solve),
`pre-run-contract.json` fixed numerical sources, inputs, acceptance and22 tests.
The earlier independent reference development has its own contract and log.
The exact first numerical source/test copies, JUnit, logs, saved fields,
histories and results remain in `attempts/01/`. The archived test filename
avoids duplicate pytest collection. No thresholds were changed after seeing
results. **22 tests and all48 scientific gates passed on the first attempt.**
The four main calculations took about2.25s in the original local environment;
this is an observation, not a cross-machine performance guarantee.

For fixed deposition radius.03, active density L1 is
.172566/.127846/.074579 on128/256/512 cells; pressure L1 is
.181485/.139395/.076152. Finest shock-location error is1.096 cells. The
maximum relative discrete mass/radial-momentum/energy budget residual is
about1.34e-15. The finest peak density is2.9182 versus the strong-shock
jump4; the center density.014842 and pressure1.64170 remain reported.

Halving the deposition radius at the same512-cell mesh changes density by
.00045072 and pressure by.00061921 in the active relative L1 norms. The
point-blast differences become **slightly worse**, so this is not an
improvement claim or a proof of the point-source continuum limit. The
example does not validate nonspherical perturbations, Cartesian2D/3D,
higher-order methods or a more general equation of state.

## Sources and review scope

1. G.I.Taylor(1950), *The formation of a blast wave by a very intense explosion
   I. Theoretical discussion*, Proceedings of the Royal Society A201(1065),
   159–174, DOI[10.1098/rspa.1950.0049](https://doi.org/10.1098/rspa.1950.0049).
   Selected original pp159–167 were checked via a
   [university-hosted scan](https://homepage.physics.uiowa.edu/~ghowes/teach/phys7729/docs/Taylor50a.pdf)
   for similarity assumptions, Euler reduction, strong-shock conditions,
   energy normalization and the regular-center exponent. Publisher access403;
   no full-text review or redistribution is claimed.
2. J.Thrussell and J.M.Ferguson(2023), *ExactPack: A python library of exact
   analytic solutions*, SoftwareX24,101560,
   DOI[10.1016/j.softx.2023.101560](https://doi.org/10.1016/j.softx.2023.101560).
   Cite this software paper separately from the original similarity theory.
3. [LANL ExactPack selected pinned Sedov code](https://github.com/lanl/ExactPack/tree/9bacc477eb791e959c9621e771fc7a725db755fa/exactpack/solvers/sedov).
   Only the selected unchanged module and its minimal official dependencies
   were executed; the source and execution receipts preserve that scope.
