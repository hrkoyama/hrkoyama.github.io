# Double Mach reflection: lightweight grid verification

Full 2D Euler finite volumes evolve the existing Double Mach initial/boundary data to T=.2 on64x16,128x32 and256x64 cells. Compare a separately written finite-grid reference, actual boundary-flux budgets, an upper incident-front position and a fixed near-wall region.

These additional validation supplements are managed separately from the common 22-example registry. Receipts cover independent ZIP extraction, tests and every fixed input within each group. Changes of settings, methods or step sizes do not add independent physical problems.

## Double Mach reflection: lightweight grid verification

Full 2D Euler finite volumes evolve the existing Double Mach initial/boundary data to T=.2 on64x16,128x32 and256x64 cells. Compare a separately written finite-grid reference, actual boundary-flux budgets, an upper incident-front position and a fixed near-wall region.

**Methods used**

- [HLL](https://hrkoyama.github.io/numerical-methods-atlas/methods/hll/?lang=en) (`hll`)
- [Heun / SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en) (`heun`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/double-mach-reflection/?lang=en#double-mach-reflection-en-algorithm)

The published Numart piecewise-constant HLL flux, unsplit x/y divergence and Heun/SSPRK(2,2) form a small standalone package with both-stage boundary accounting and state checks. CFL.4 uses the sum of directional maximum acoustic rates; the top boundary uses each actual RK stage time. No state floor, repair or hidden retry. Invalid stages retain raw arrays/history and fail.

$$
\partial_tU+\partial_xF(U)+\partial_yG(U)=0,\qquad U=(\rho,\rho u,\rho v,E)^T
$$

$$
x_s(y,t)=\frac16+\frac{y+20t}{\sqrt3},\quad \gamma=1.4,\quad M_s=10
$$

$$
\Delta t=0.4\left[\max(|u|+c)/\Delta x+\max(|v|+c)/\Delta y\right]^{-1}
$$

$$
\sum_{ij}|C_{ij}|(\bar U_{ij}^{n+1}-\bar U_{ij}^{n})=\frac{\Delta t}{2}(B(U^n,t_n)+B(U^{(1)},t_n+\Delta t))
$$

- [Compressible Euler equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#euler-en) (`euler`)

Two-dimensional compressible Euler conservation laws with gamma1.4. This example fixes the Mach10 incident shock, inflow/outflow, reflecting wall and moving-shock top boundary.


**Problem figure**

![Double Mach reflection: lightweight grid verification: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/double-mach/results/double-mach-reflection.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Double Mach reflection](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-mach/?lang=en) (`double-mach`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-mach/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/double-mach-reflection/?lang=en#double-mach-reflection-en-validation)

The original preregistered20 unit tests passed. Before the full three-grid run, read-only review added an absent-front diagnostic guard and one test; the old contract/source are preserved and a revision contract was frozen. All21 tests, three final-time runs and40 gates passed with-W error. Previously independently executed Ny64/128 primitive MUSCL/generalized-minmod theta1.5/HLL/Heun data from the RKDG kit are reused; no reference PDE was rerun. Density L1 differences from conservatively restricted Ny128 are.08431/.05802/.03503 and pressure differences.09556/.06798/.04156. Reference64/128 increments are.00955/.01250, about.273/.301 of the finest primary differences. Maximum relative four-component boundary-budget residual is about4.60e-13.

- [Double Mach reflection: saved independent finite-grid numerical reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-double-mach-en) (`double-mach`; Same-problem reference · Finite-grid numerical reference)

Compare against two previously independently executed finite-volume reference grids using conservative restriction. This is a finite-grid numerical reference, not an exact2D solution or error bound.
### Assumptions, units and boundaries

Nondimensional[0,4]x[0,1], gamma1.4, Mach10. Shock footx=1/6, angle60degrees; postshock(rho,u,v,p)=(8,8.25sqrt(3)/2,-4.125,116.5), upstream(1.4,0,0,1). Initial cells are classified by their centers, not exact cut-cell means. Left postshock inflow, right zero-gradient, bottom postshock forx<1/6 and slip wall otherwise; top postshock forx<1/6+(1+20t)/sqrt(3).

**Editorial clarification**

A lightweight comparison with an independent finite-grid numerical reference, not an exact2D full-field solution. Separate measured shock location, conservation budgets and wall-jet diagnostics from convergence of the thin wall jet. Forward-facing step is outside this execution scope.

### Adopted numerical method

The published Numart piecewise-constant HLL flux, unsplit x/y divergence and Heun/SSPRK(2,2) form a small standalone package with both-stage boundary accounting and state checks. CFL.4 uses the sum of directional maximum acoustic rates; the top boundary uses each actual RK stage time. No state floor, repair or hidden retry. Invalid stages retain raw arrays/history and fail.

$$
\partial_tU+\partial_xF(U)+\partial_yG(U)=0,\qquad U=(\rho,\rho u,\rho v,E)^T
$$

$$
x_s(y,t)=\frac16+\frac{y+20t}{\sqrt3},\quad \gamma=1.4,\quad M_s=10
$$

$$
\Delta t=0.4\left[\max(|u|+c)/\Delta x+\max(|v|+c)/\Delta y\right]^{-1}
$$

$$
\sum_{ij}|C_{ij}|(\bar U_{ij}^{n+1}-\bar U_{ij}^{n})=\frac{\Delta t}{2}(B(U^n,t_n)+B(U^{(1)},t_n+\Delta t))
$$

### References and validation

The original preregistered20 unit tests passed. Before the full three-grid run, read-only review added an absent-front diagnostic guard and one test; the old contract/source are preserved and a revision contract was frozen. All21 tests, three final-time runs and40 gates passed with-W error. Previously independently executed Ny64/128 primitive MUSCL/generalized-minmod theta1.5/HLL/Heun data from the RKDG kit are reused; no reference PDE was rerun. Density L1 differences from conservatively restricted Ny128 are.08431/.05802/.03503 and pressure differences.09556/.06798/.04156. Reference64/128 increments are.00955/.01250, about.273/.301 of the finest primary differences. Maximum relative four-component boundary-budget residual is about4.60e-13.

### Limits

The reference is finite-grid numerical data, not an exact2D solution or an Athena/LAVA execution. The HLL family is shared, but reference spatial operators are separately written and not imported by the primary. The reference increment is an uncertainty diagnostic, not an error bound. Initial projection, sampled moving boundaries, discretization and finite-reference effects all enter the difference; the slope is no rigorous order or full reflection-pattern convergence proof. The upper-front discrepancy stays2cells while its physical width shrinks. Fixed near-wall ROIx in[1,2.75],y<=.25 is not feature tracking. Finest ROI maxu12.644 versus reference16.125 shows the thin wall jet/roll-up is unresolved. Forward step, other wall data, general perturbations, higher order and full-pattern convergence are unverified.

### Stored measurements and decisions

```json
{
  "metrics": {
    "n": 64,
    "ny": 64,
    "nx": 256,
    "time": 0.2,
    "steps": 811,
    "density_l1": 0.035029442558786025,
    "pressure_l1": 0.04155565203322573,
    "density_l2": 0.07511923063820683,
    "density_linf": 0.2503923225552139,
    "minimum_density_all_stages": 1.4,
    "minimum_pressure_all_stages": 1.0,
    "density_min": 1.4,
    "density_max": 20.3156584501302,
    "pressure_min": 1.0,
    "pressure_max": 530.3379565726824,
    "state_floor_count": 0,
    "rejected_steps": 0,
    "incident_front_x": 2.9375,
    "reference_incident_front_x": 2.90625,
    "front_row_y": 0.7421875,
    "incident_front_error_cells": 2.0,
    "wall_jet_density_l1": 0.060165720387909134,
    "wall_jet_mean_density": 13.785652231102395,
    "wall_jet_reference_mean_density": 13.97485965152079,
    "wall_jet_mean_u": 8.343336108943573,
    "wall_jet_reference_mean_u": 8.397760320217083,
    "wall_jet_max_u": 12.644046893512225,
    "wall_jet_reference_max_u": 16.125383198389834
  },
  "checks": {
    "three final-time refinements complete": true,
    "ny16: requested time reached": true,
    "ny16: minimum_density_all_stages": true,
    "ny16: minimum_pressure_all_stages": true,
    "ny16: state_floor_count": true,
    "ny16: rejected_steps": true,
    "ny16: mass boundary balance": true,
    "ny16: x momentum boundary balance": true,
    "ny16: y momentum boundary balance": true,
    "ny16: energy boundary balance": true,
    "ny16: unmasked maximum and wall-jet diagnostics retained": true,
    "ny32: requested time reached": true,
    "ny32: minimum_density_all_stages": true,
    "ny32: minimum_pressure_all_stages": true,
    "ny32: state_floor_count": true,
    "ny32: rejected_steps": true,
    "ny32: mass boundary balance": true,
    "ny32: x momentum boundary balance": true,
    "ny32: y momentum boundary balance": true,
    "ny32: energy boundary balance": true,
    "ny32: unmasked maximum and wall-jet diagnostics retained": true,
    "ny64: requested time reached": true,
    "ny64: minimum_density_all_stages": true,
    "ny64: minimum_pressure_all_stages": true,
    "ny64: state_floor_count": true,
    "ny64: rejected_steps": true,
    "ny64: mass boundary balance": true,
    "ny64: x momentum boundary balance": true,
    "ny64: y momentum boundary balance": true,
    "ny64: energy boundary balance": true,
    "ny64: unmasked maximum and wall-jet diagnostics retained": true,
    "finest density_l1": true,
    "finest pressure_l1": true,
    "finest upper incident front difference": true,
    "density difference decreases across the fixed grids": true,
    "last-pair density difference slope": true,
    "reference increment density_l1": true,
    "reference increment / primary finest density_l1": true,
    "reference increment pressure_l1": true,
    "reference increment / primary finest pressure_l1": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/double-mach-reflection/index.json

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23/double-mach/atlas-double-mach-2026-11-23.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23/double-mach/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/double-mach/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23/double-mach/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- Paul Woodward and Phillip Colella (1984). The numerical simulation of two-dimensional fluid flow with strong shocks. https://www.sciencedirect.com/science/article/pii/0021999184901426; review_level=publisher-metadata-and-abstract; official-NASA-setup-cross-check
Publisher metadata/abstract and the official NASA setup were checked. No direct full-paper review is claimed; cited for the original strong-shock comparison and benchmark.

- NASA Advanced Supercomputing Division, LAVA team (n.d.). Double Mach Reflection — LAVA tutorial. https://www.nas.nasa.gov/LAVA/unst_docs/tutorials/double_mach/double_mach/; review_level=official-tutorial-selected-setup-and-boundaries
Checked Mach10, gamma1.4, domain, shock foot x=1/6, upstream state, boundaries and T=.2. No LAVA execution or figure redistribution.

- Hiroshi Koyama (2026). Independent finite-volume references distributed with the RKDG2D agent kit, 2026-11-23-r2. https://hrkoyama.github.io/code/rkdg2d/2026-11-23-r2/atlas-rkdg-agent-kit.zip; review_level=hash-checked-selected-public-archive-artifacts
Selected source, two-grid data and execution records were copied from the immutable archive. No reference PDE, Athena or LAVA was rerun here. The flux family HLL is shared, while the reference is a separate implementation without imports of primary spatial operators.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
