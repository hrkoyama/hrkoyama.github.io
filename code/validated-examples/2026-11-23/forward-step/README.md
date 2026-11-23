# Mach-3 forward-facing step: lightweight2D verification

This educational supplement evolves actual two-dimensional ideal-gas Euler
states around a grid-aligned step. It preserves the published Numart
piecewise-constant HLL/Heun method and adds independent finite-grid comparison,
stage admissibility, individual wall impulses and actual numerical face-flux
budgets. Existing published code and figures are not overwritten.

## Run from an extracted ZIP

```sh
python -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -W error -m pytest -q -p no:cacheprovider
.venv/bin/python -W error run.py --input inputs.json --output new-results
```

Use a new empty output directory. The ordinary verification needs only the
three pinned NumPy/SciPy/pytest dependencies. It reads bundled reference arrays;
no C++ compiler, reference download, external CFD engine or private checkout is
required. Reference PDE execution is separate and is not hidden in this runner.
Optional plots use `requirements-plotting.txt` and
`python plot.py --results new-results/result.json --output new-figures`.
That program reads qualified hash-bound arrays only and imports no PDE solver.

## Fixed physical definition and numerical method

The nondimensional domain is [0,3] x [0,1] excluding the solid region
x>=.6,y<.2. Gamma=1.4; initial and left-inflow primitive state is
(rho,u,v,p)=(1.4,3,0,1), with sound speed1 and Mach3. Right outflow is
zero-gradient. Top, bottom and both step faces are stationary reflecting slip
walls: reverse only the normal momentum in the face's mirrored state.

The three square-cell meshes are Nx x Ny=60x20,120x40,240x80, all to T=4.
Ny divisible by5 aligns the x=.6 and y=.2 faces exactly. Solid cells are dummy
storage, excluded from fluid norms and integrals. Their states are not evolved.
There is no cut-cell geometry or geometric error from an approximated step.

Both Cartesian HLL flux divergences are evolved without directional splitting.
Heun/SSPRK(2,2) uses CFL.4 divided by the sum of directional maximum acoustic
rates. Each grid has a declared20000-step cap. Density and pressure must be
finite and strictly positive at every predictor and update. There are no cell
state/pressure floors, repairs, rejected steps or retries. An invalid stage
retains the raw array, completed history and failure context.

`boundary_integrals` separately records inlet, outlet, bottom, top, vertical
step and horizontal step impulses. The same actual face fluxes used by each RK
stage are integrated with its Heun weight. Wall mass/energy fluxes vanish;
normal numerical pressure traction transfers momentum. Global conservation
means the four fluid integral changes equal the total integrated boundary
fluxes including those internal step faces. This is an open inflow/outflow
problem, not a closed-box mass/energy conservation assertion.

## Corner variant and independent reference

This baseline applies **no Woodward--Colella special corner entropy/enthalpy
reset**. The referenced Cockburn--Shu report explicitly compares untreated and
specially treated corners. The uncorrected variant can carry a numerical
corner-generated entropy layer downstream. Do not interpret these coarse fields
as the corrected PPM result or convergence of its thin slip lines and roll-up.

The separately written C++17 reference reconstructs primitive-variable MUSCL
slopes using generalized minmod theta1.5, HLL and Heun at CFL.3 on Ny80/160.
It imports no primary spatial operator and shares only the declared physical
definition and numerical families. Its own pre-run contract, source, license,
execution commands and raw logs/arrays are retained in `references/`.
This is a new independently executed reference, not reused Double Mach data,
and not an AMROC/LAVA/Athena/RKDG execution. Slope admissibility control does
not replace cell means; no cell floors, step rejection or retries are allowed.

Fine reference **conserved** cell means are averaged in integer blocks to each
primary mesh. Pressure is then recovered from the restricted conserved state;
it is not an average of fine primitive pressures. Density/pressure relativeL1
use every active fluid cell. Ny80 versus restricted Ny160 increments diagnose
finite-grid sensitivity, not a rigorous error bound. Primary differences include
its spatial/time errors and reference discretization; the measured slope is
not a pure spatial order or a full-flow-pattern convergence proof.

The fixed diagnostic corner ROI is x=[.4,1],y=[0,.5], intersected with fluid.
It retains density difference, maximum density/pressure and entropy-variable
extrema. Full-fluid Linf/extrema and the first row above the step are also
retained. No feature is removed from the primary L1 norm by this diagnostic ROI.

## Contracts and acceptance

`pre-run-contract.json` freezes primary inputs, criteria, source and24 tests
before any primary unit/PDE execution. It also pins the separately frozen
reference source/contract. Reference arrays did not yet exist when that primary
contract was written; a later data-qualification record binds those arrays
without rewriting the original contract. Every executed trial is retained.

The reference's first Ny80 run completed, while its first Ny160 run exhausted
the declared120second wall-time budget. That original source, contract, raw
completed Ny80 field and actual timeout remain under `references/attempts/01`.
A subsequent reference revision changes only the assertion diagnostic argument
from `const std::string&` to `const char*`, avoiding heap allocation at every
face. It changes no arithmetic, physical input, method, CFL, execution budget
or acceptance value. Before any primary unit/PDE execution, the original
primary contract was retained as `contract-before-reference-performance.json`
and an explained new contract pinned that reference revision. The primary
numerical source,24 tests, input and all45 acceptance gates remain unchanged.

The fixed45 gates require all three final-time runs, positive stages, no floors
or retries, exact aligned fluid area2.52, all four relative boundary-budget
residuals <=3e-12 and integrated wall mass/energy <=2e-13. Finest density and
pressure relativeL1 must be <=.18; density differences must decrease with a
last-pair slope >=.15. Reference density/pressure increments must be <=.08 and
at most.8 of the corresponding finest primary difference. The24 unit tests
include independent analytic Mach3 normal-shock Rankine--Hugoniot identities,
uniform parallel-channel preservation, wall flux invariants, pressure-force
orientation, telescoping budgets, conservative restriction and failure paths.
These criteria are not loosened after observing computed fields.

## Measured results and unresolved structure

All24 unit tests and all three T=4 computations passed with `-W error`; all45
fixed numerical gates passed. At Ny20/40/80, density relativeL1 differences
from the conservatively restricted reference are .147541/.128775/.102651,
and pressure differences are .193727/.160153/.122422. The .18 criterion applies
to the **finest** primary grid. The last-pair density-difference slope is .3271,
which is not a claim of pure spatial order. Reference80/160 density/pressure
increments are .026359/.030633, about .257/.250 of the finest primary differences.
All four conserved budgets close with maximum normalized residual2.99e-13;
integrated mass/energy fluxes on each stationary wall are zero. Primary stage
minima remain positive, with rho>=.5723 and p>=.7623 across this fixed sequence.

The three primary computations took about45.8seconds on the original Mac.
After the diagnostic-argument performance revision, independent reference80/160
runs took about7.8/65.1seconds and used7707/15800steps. Their stage minima remain
positive, with zero state floors, rejected steps or slope rescalings. Ordinary
ZIP verification reruns the primary sequence; it does not rerun the references.

The **normalized maximum density differences do not decrease**:
.5923/.6703/.6649. The corner-ROI densityL1 decreases .10808/.06215/.03512, but
corner entropy-variable minima change -.07841/-.12243/-.35097 and maxima change
.22208/.25179/.30511. These extrema are not stable across the lightweight grids.
The entropy variable log(p/rho^gamma) has an arbitrary additive constant;
more-negative values alone do not mean increasing error. For orientation,
the upstream value is -.47106, and the finest restricted reference corner
minimum is approximately -.47106. No positivity failure or physical entropy
inequality violation is inferred merely from the sign of this diagnostic.

The preserved nonmonotone maximum differences and changing corner extrema
prevent a claim of pointwise/full-pattern convergence. These computations
verify broad structures, coarse-field differences and implementation budgets;
thin slip lines, roll-up and the unresolved uncorrected corner entropy layer
remain explicit limitations. The plot includes the entropy-variable profile
on the first fluid row above the step to make that limitation visible.

## Sources and scope of review

* Woodward and Colella(1984), *The numerical simulation of two-dimensional
  fluid flow with strong shocks*, JCP54,115--173,
  DOI[10.1016/0021-9991(84)90142-6](https://doi.org/10.1016/0021-9991(84)90142-6).
  Original benchmark attribution; direct full-paper review is not claimed.
* Cockburn and Shu(1991), *The P1-RKDG Method for Two-Dimensional Euler
  Equations of Gas Dynamics*, NASA CR187542/ICASE91-32,
  [primary report](https://ntrs.nasa.gov/citations/19910015505).
  Selected Example2 setup and the captions distinguishing corner treatments
  were reviewed. No report figure is redistributed and no RKDG method is run.
* [AMROC official forward-step example](https://amroc.sourceforge.net/examples/euler/2d/html/ffstep_n.htm)
  provides context for the explicitly uncorrected corner variant; no AMROC
  computation, AMR or figure is imported.

Precise review scope and source provenance are in `cases.json`,
`source-provenance.json` and `references/citations.json`. `LICENSE` covers
original implementation code only. Reference code retains its MIT notice.
Prose, figures and data retain the conditions at
https://hrkoyama.github.io/rights/ and https://hrkoyama.github.io/LICENSING.md.
