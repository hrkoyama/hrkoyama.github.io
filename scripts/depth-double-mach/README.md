# Double Mach reflection: lightweight grid verification

This standalone educational supplement evolves actual two-dimensional Euler
states with piecewise-constant HLL fluxes and Heun/SSPRK(2,2). It extends the
published Numart Double Mach baseline with final-time refinement, independent
finite-grid comparison and actual boundary-flux budgets. Original published
code and figures are not overwritten. This is the Double Mach portion of the
backlog item; the forward-facing-step problem remains separate future work.

## Run from an extracted ZIP

```sh
python -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -W error -m pytest -q -p no:cacheprovider
.venv/bin/python -W error run.py --input inputs.json --output new-results
```

Use a new empty output directory. Runtime dependencies are the three pinned
NumPy/SciPy/pytest versions; no private checkout, reference downloads, C++
compiler, Athena++, LAVA or ExactPack installation is required. The independent
reference PDE is **not rerun** by this command. Optional figure regeneration
uses `requirements-plotting.txt` and
`python plot.py --results new-results/result.json --output new-figures`.
The plot program only reads qualified hash-bound saved fields; it imports no
PDE implementation and performs no hidden simulation.

## Fixed physical definition

Gamma1.4 on [0,4] x [0,1], final time .2, shock Mach10, initial foot x=1/6,
shock angle60degrees to the horizontal. Postshock primitive state is
(rho,u,v,p)=(8,8.25 sqrt(3)/2,-4.125,116.5), upstream=(1.4,0,0,1).
Cell-center side classification sets initial conserved states; these are not
exact cut-cell averages. The left boundary is postshock inflow and right is
zero-gradient outflow. The bottom is postshock for x<1/6 and reflecting slip
wall otherwise. Top data use x<1/6+(1+20t)/sqrt(3) at each actual RK stage time.

The three grids are Nx x Ny=64x16,128x32,256x64 with square cells. CFL.4 uses
the sum of directional maximum acoustic rates. Both x/y flux divergences are
evolved without splitting. Every predictor/update has strictly positive rho
and pressure in these measured runs. There are no state/pressure floors,
cell repairs or hidden timestep retries. Invalid RK stages preserve raw arrays,
completed history and context before failing. Conservation means four global
conserved integrals minus the actual two-stage numerical boundary flux integral;
this is not a closed-box conservation assertion for inflow/outflow data.

## Reference and interpretation

The immutable RKDG2D agent-kit ZIP already contains separately written 2D
primitive-variable MUSCL/generalized-minmod(theta1.5)/HLL/Heun reference runs
on Ny64 and128 at T=.2. Their unmodified source, arrays, metadata and license
are copied into `references/` with ZIP/member hashes and `independent-reuse.json`.
Inherited metadata call the limiter MC; the literal stencil is the theta1.5
MC-type generalized minmod, not canonical theta2 MC. Both saved runs recorded
zero timestep rejections. The reference source supports retries, but none were
used in these stored runs. No new reference PDE was executed for this release.

Both implementations share the HLL flux family. The reference reconstructs
primitive slopes with separately authored spatial operators and imports no
primary operators. It is an independent implementation, **not an external
Athena/LAVA engine, exact reflected-flow solution, or a primary finer-grid run**.
The fine conserved reference is averaged in integer blocks to each primary
mesh before comparison. Pressure is recovered from each conserved cell mean.
Ny64 versus restricted Ny128 reference increments measure finite-grid
sensitivity; they are not guaranteed bounds on true PDE error. The primary
differences include discretization, cell-center initialization/projection,
sampled moving boundaries and finite-reference uncertainty. The measured slope
is not a rigorous spatial order or full-pattern convergence proof.

The fixed upper incident-front diagnostic uses the row nearest y=.75 and the
largest decreasing density gradient in x=[2,3.5]. It compares with the same
restricted reference mesh, not an exact reflected-front position. Empty/flat
search windows are rejected explicitly. The fixed near-wall ROI
x=[1,2.75],y<=.25 contains the high-speed jet region but does not track the jet.
Its density L1, mean density/u and maximum u are retained without a fine-jet
accuracy gate. The whole-domain Linf/extrema are also retained.

## Frozen contract and measured results

`contract-before-front-guard.json` was written before the original20 unit tests
and small unit PDE checks, which all passed. A subsequent read-only review
added only an absent-front diagnostic guard and one regression test before the
three full refinement runs. `pre-run-contract.json` explicitly identifies this
revision and freezes21 tests, revised source, unchanged solver/input/acceptance
and all stored references **before this revision executes**. The old contract,
source, unit log/JUnit and subsequent revision records remain in `attempts/`.
No acceptance value was changed after seeing a primary refinement result.

All21 tests and three full T=.2 runs passed with `-W error`. All40 numerical
gates passed. Density relative L1 differences are .084307/.058022/.035029;
pressure differences are .095560/.067984/.041556. Reference increments are
.009553 and .012502, about .273/.301 of the finest primary differences, below
the preregistered .75 ratio. Maximum normalized boundary-budget residual is
4.60e-13, below2e-12. The full three-grid run took about5seconds on the original
Mac; independently extracted ZIP and public Linux execution are separate checks.

At Ny64 the upper incident front still differs by2cells (physical width shrinks
with refinement). The near-wall maximum tangential velocity is12.644 compared
with16.125 in the restricted reference: the thin wall jet/roll-up remains
under-resolved. These are broad-pattern, modest-grid checks, not recovery of
Woodward--Colella fine-scale PPM structures. Forward step, perturbed data,
alternative wall conditions and high-order/full-pattern convergence are outside
this release.

## Sources and review scope

* Woodward and Colella(1984), *The numerical simulation of two-dimensional
  fluid flow with strong shocks*, JCP54,115--173,
  DOI[10.1016/0021-9991(84)90142-6](https://doi.org/10.1016/0021-9991(84)90142-6).
  Publisher metadata/abstract and official setup cross-check; no original full
  paper review or figure reproduction is claimed.
* [NASA LAVA official Double Mach tutorial](https://www.nas.nasa.gov/LAVA/unst_docs/tutorials/double_mach/double_mach/),
  selected physical setup/boundaries checked; publication undated, page updated
  2026-06-15, accessed2026-11-23. No LAVA execution or NASA figure redistribution.
* The independently executed numerical reference source/data are credited
  separately in `references/independent-reuse.json` and `references/citations.json`.
  The original Numart-derived primary provenance is `source-provenance.json`.

`LICENSE` covers original implementation code only. Reference software retains
its bundled MIT notice. Prose, figures and data retain the site conditions at
https://hrkoyama.github.io/rights/ and https://hrkoyama.github.io/LICENSING.md.
