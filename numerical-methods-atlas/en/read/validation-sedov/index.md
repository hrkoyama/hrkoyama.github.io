# Sedov–Taylor point blast: lightweight spherical-radial validation

A lightweight spherical-radial Euler finite-volume example deposits unit energy inside fixed radius0.03. Three grids of128/256/512 radial cells measure differences from a point-blast similarity reference and conservation budgets. The picture is a section display of1D spherical data, not a2D Cartesian calculation.

These additional validation supplements are managed separately from the common 22-example registry. Receipts cover independent ZIP extraction, tests and every fixed input within each group. Changes of settings, methods or step sizes do not add independent physical problems.

## Sedov–Taylor point blast: lightweight spherical-radial validation

A lightweight spherical-radial Euler finite-volume example deposits unit energy inside fixed radius0.03. Three grids of128/256/512 radial cells measure differences from a point-blast similarity reference and conservation budgets. The picture is a section display of1D spherical data, not a2D Cartesian calculation.

**Methods used**

- [Rusanov / local Lax–Friedrichs flux](https://hrkoyama.github.io/numerical-methods-atlas/methods/rusanov/?lang=en) (`rusanov`)
- [Heun / SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en) (`heun`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/sedov-blast/?lang=en#sedov-blast-en-algorithm)

Piecewise-constant Rusanov fluxes on spherical shells with SSPRK2/Heun. The radial-momentum source p(A_right-A_left)/V is integrated at the same RK stages, with a stationary uniform-pressure balance test. CFL.4 uses the reciprocal maximum (|u|+c)/(V/(A_left+A_right)), comparing with the remaining interval before division. No pressure seed, floor, cell repair or hidden timestep retry; an invalid stage retains raw conserved values and history and fails.

$$
\partial_t U+\frac{1}{r^2}\partial_r(r^2F)=\left(0,2p/r,0\right)^T,\quad U=(\rho,\rho u,E)^T
$$

$$
R_s(t)=\beta(E_0t^2/\rho_0)^{1/5},\quad\beta\simeq1.15166641793,\quad\dot R_s=2R_s/(5t)
$$

$$
\rho=\rho_0G(\xi),\quad u=\dot R_sV(\xi),\quad p=\rho_0\dot R_s^2P(\xi),\quad\xi=r/R_s
$$

$$
E_0=4\pi\int_0^\infty\left(\frac{p}{\gamma-1}+\frac{\rho u^2}{2}\right)r^2\,dr=1
$$

$$
\bar U_i=\frac{3}{r_{i+1/2}^3-r_{i-1/2}^3}\int_{r_{i-1/2}}^{r_{i+1/2}}U(r)r^2\,dr
$$

- [Compressible Euler equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#euler-en) (`euler`)

The one-dimensional spherical-radial ideal-gas Euler system. This example defines origin reflection, geometric source, finite-radius energy deposition and outer boundary in its fixed input.


**Problem figure**

![Sedov–Taylor point blast: lightweight spherical-radial validation: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/sedov/results/sedov-blast.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Sedov–Taylor point blast](https://hrkoyama.github.io/numerical-methods-atlas/problems/sedov/?lang=en) (`sedov`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/sedov/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/sedov-blast/?lang=en#sedov-blast-en-validation)

Original r1 passed22 tests and48 gates on Mac, but its public-ZIP Linux run failed when warnings-as-errors raised a cold-tail CFL overflow. Revision r2 uses the algebraically equivalent reciprocal maximum-rate evaluation while preserving the original inputs, reference and48 acceptance gates. A new r2-specific pre-execution hash contract precedes23 tests and all four calculations/48 gates passing with warnings as errors. Original sources, contract and actual Linux-failure evidence remain archived. The independent reference integrates the similarity ODE with DOP853, normalizes energy, uses a regular asymptote for xi<.001 and split shell quadrature at the shock. Orders16/32, core cutoff and ODE tolerance are checked separately. The unmodified pinned ExactPack evaluator was independently run at6001/12001 points and compared away from the center/jump with its preregistered5e-4 criterion. Beta=1.15166641793, Rs(.05)=.34746791233. Origin/shock-inclusive volume-weighted density L1 within r<=1.2Rs is.17257/.12785/.07458 and pressure L1 is.18148/.13939/.07615. Finest shock error is1.096 cells; maximum relative discrete-budget residual is about8.89e-16.

- [Sedov–Taylor point blast: energy-normalized spherical similarity solution](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-sedov-en) (`sedov`; Same-problem reference · Semi-analytic reference)

An energy-normalized spherical similarity reference. Numerical integration of similarity ODEs and shell quadrature make this semi-analytic, not closed-form exact cell means. Finite-radius deposition is distinct from the singular ideal point-blast initial data. At fixed finite deposition radius, comparison with the point-source similarity reference includes deposition-model discrepancy; its refinement slope is not a pure spatial order. Changing deposition radius on the same finest grid is a sensitivity diagnostic, not a complete separation of continuum deposition and PDE-discretization errors.
### Assumptions, units and boundaries

Nondimensional gamma=5/3, ambient density1, velocity0, pressure0, radius[0,1], deposited energy1, T=.05. Uniform thermal energy inside a sphere is assigned using exact cut-shell volumes. Deposition radius0.03 is shared by all three grids; a separate512-cell run uses0.015. The origin is reflecting and the outer boundary is outflow; actual boundary fluxes enter measured budgets.

**Editorial clarification**

Revisionr1 passed22 tests and four runs on Mac, but its public-ZIP Linux retry passed22 tests then failed in the -Werror main run when a CFL candidate ratio overflowed at tiny cold-tail wave speeds. Revisionr2 evaluates the same CFL condition as1/max(speed/width), avoiding intermediate overflow. Inputs/acceptance thresholds stay unchanged; retain the old release/failure and independently rerun23 tests and all fixed inputs from a new ZIP. Fixed-radius point-source comparison includes model discrepancy: its refinement slope is not a pure spatial order, and the radius comparison is sensitivity rather than complete deposition/PDE-error separation. Original Linux failure: https://github.com/hrkoyama/hrkoyama.github.io/actions/runs/45109504662 (all22 tests passed; the first128-cell,rdep.03 main calculation raised RuntimeWarning: overflow encountered in divide before completion).

### Adopted numerical method

Piecewise-constant Rusanov fluxes on spherical shells with SSPRK2/Heun. The radial-momentum source p(A_right-A_left)/V is integrated at the same RK stages, with a stationary uniform-pressure balance test. CFL.4 uses the reciprocal maximum (|u|+c)/(V/(A_left+A_right)), comparing with the remaining interval before division. No pressure seed, floor, cell repair or hidden timestep retry; an invalid stage retains raw conserved values and history and fails.

$$
\partial_t U+\frac{1}{r^2}\partial_r(r^2F)=\left(0,2p/r,0\right)^T,\quad U=(\rho,\rho u,E)^T
$$

$$
R_s(t)=\beta(E_0t^2/\rho_0)^{1/5},\quad\beta\simeq1.15166641793,\quad\dot R_s=2R_s/(5t)
$$

$$
\rho=\rho_0G(\xi),\quad u=\dot R_sV(\xi),\quad p=\rho_0\dot R_s^2P(\xi),\quad\xi=r/R_s
$$

$$
E_0=4\pi\int_0^\infty\left(\frac{p}{\gamma-1}+\frac{\rho u^2}{2}\right)r^2\,dr=1
$$

$$
\bar U_i=\frac{3}{r_{i+1/2}^3-r_{i-1/2}^3}\int_{r_{i-1/2}}^{r_{i+1/2}}U(r)r^2\,dr
$$

### References and validation

Original r1 passed22 tests and48 gates on Mac, but its public-ZIP Linux run failed when warnings-as-errors raised a cold-tail CFL overflow. Revision r2 uses the algebraically equivalent reciprocal maximum-rate evaluation while preserving the original inputs, reference and48 acceptance gates. A new r2-specific pre-execution hash contract precedes23 tests and all four calculations/48 gates passing with warnings as errors. Original sources, contract and actual Linux-failure evidence remain archived. The independent reference integrates the similarity ODE with DOP853, normalizes energy, uses a regular asymptote for xi<.001 and split shell quadrature at the shock. Orders16/32, core cutoff and ODE tolerance are checked separately. The unmodified pinned ExactPack evaluator was independently run at6001/12001 points and compared away from the center/jump with its preregistered5e-4 criterion. Beta=1.15166641793, Rs(.05)=.34746791233. Origin/shock-inclusive volume-weighted density L1 within r<=1.2Rs is.17257/.12785/.07458 and pressure L1 is.18148/.13939/.07615. Finest shock error is1.096 cells; maximum relative discrete-budget residual is about8.89e-16.

### Limits

A finite deposition sphere and an ideal point blast have different initial data; reported errors combine deposition-model and discretization effects. The refinement slope is not a pure spatial order. Halving the source radius at the same512 cells changes density by about.000451 and pressure by.000619, but point-reference errors become slightly worse; no improvement or point-source-limit proof is claimed. Pressure compares numerical p(mean conserved U) with reference mean physical pressure, distinct from p(mean reference U). Center values and maximum errors remain reported. The finest density peak is about2.918 versus the exact jump4. The cold-tail local-CFL overflow that caused the r1 Linux failure is avoided in r2 by the equivalent maximum inverse-rate evaluation, without suppressing warnings or adding a physical floor. The regular tiny-core continuation is approximate, and ExactPack point probes exclude xi<.15. Cartesian2D/3D, general perturbations/asymmetry and high-order accuracy are unverified.

### Stored measurements and decisions

```json
{
  "metrics": {
    "n": 512,
    "deposit_radius": 0.03,
    "time": 0.05,
    "steps": 4009,
    "density_l1": 0.0053696340419367985,
    "active_density_l1": 0.07457886347110618,
    "active_pressure_l1": 0.07615237367293778,
    "density_l2": 0.05831370352624319,
    "density_linf": 0.3892475533701634,
    "density_min": 0.01484223174892597,
    "density_max": 2.918215810146801,
    "pressure_min": 0.0,
    "pressure_max": 4.80236959914648,
    "maximum_speed": 2.0075920268793204,
    "center_density": 0.01484223174892597,
    "center_pressure": 1.6417016839131997,
    "center_reference_density": 4.1043889913677827e-11,
    "center_reference_pressure": 1.7744715646691345,
    "shock_radius": 0.349609375,
    "reference_shock_radius": 0.3474679123327071,
    "shock_error_cells": 1.0964288856539781,
    "minimum_density_all_stages": 0.014842231581750347,
    "minimum_pressure_all_stages": 0.0,
    "minimum_internal_roundoff_units": 0.0,
    "state_floor_count": 0,
    "reference_quadrature_density_l1": 1.1766085003791174e-16,
    "reference_quadrature_pressure_l1": 1.1717338251963657e-16,
    "initial_energy_error": 0.0
  },
  "checks": {
    "three fixed-radius refinements complete": true,
    "paired smaller-radius run completes": true,
    "n128: strictly positive density all stages": true,
    "n128: internal energy within roundoff": true,
    "n128: no state floor or repair": true,
    "n128: unit deposited energy": true,
    "n128: mass discrete balance": true,
    "n128: radial momentum including geometric source discrete balance": true,
    "n128: energy discrete balance": true,
    "n128: reference_quadrature_density_l1": true,
    "n128: reference_quadrature_pressure_l1": true,
    "n128: origin and maximum diagnostics retained": true,
    "n256: strictly positive density all stages": true,
    "n256: internal energy within roundoff": true,
    "n256: no state floor or repair": true,
    "n256: unit deposited energy": true,
    "n256: mass discrete balance": true,
    "n256: radial momentum including geometric source discrete balance": true,
    "n256: energy discrete balance": true,
    "n256: reference_quadrature_density_l1": true,
    "n256: reference_quadrature_pressure_l1": true,
    "n256: origin and maximum diagnostics retained": true,
    "n512: strictly positive density all stages": true,
    "n512: internal energy within roundoff": true,
    "n512: no state floor or repair": true,
    "n512: unit deposited energy": true,
    "n512: mass discrete balance": true,
    "n512: radial momentum including geometric source discrete balance": true,
    "n512: energy discrete balance": true,
    "n512: reference_quadrature_density_l1": true,
    "n512: reference_quadrature_pressure_l1": true,
    "n512: origin and maximum diagnostics retained": true,
    "sensitivity: strictly positive density all stages": true,
    "sensitivity: internal energy within roundoff": true,
    "sensitivity: no state floor or repair": true,
    "sensitivity: unit deposited energy": true,
    "sensitivity: mass discrete balance": true,
    "sensitivity: radial momentum including geometric source discrete balance": true,
    "sensitivity: energy discrete balance": true,
    "sensitivity: reference_quadrature_density_l1": true,
    "sensitivity: reference_quadrature_pressure_l1": true,
    "sensitivity: origin and maximum diagnostics retained": true,
    "finest active_density_l1": true,
    "finest active_pressure_l1": true,
    "finest shock_error_cells": true,
    "fixed-source active density L1 decreases": true,
    "last fixed-source density L1 order": true,
    "source-radius effects separately retained": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/sedov-blast/index.json

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/sedov/atlas-sedov-2026-11-23-r2.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/sedov/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/sedov/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/sedov/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- G. I. Taylor (1950). The formation of a blast wave by a very intense explosion I. Theoretical discussion. https://doi.org/10.1098/rspa.1950.0049; review_level=selected-original-pages
Selected original pp159–167 in a university-hosted scan checked for similarity assumptions, Euler reduction, strong-shock jumps, energy normalization and center exponent. Publisher access403; no full-text review or PDF redistribution claimed.

- J. Thrussell and J. M. Ferguson (2023). ExactPack: A python library of exact analytic solutions. https://doi.org/10.1016/j.softx.2023.101560; review_level=official-record-and-selected-pinned-code-execution
Unmodified selected pinned Sedov evaluator actually run at6001/12001 points. Source hashes, parameters, point values, decisions and BSD-3-Clause retained; not another numerical Euler solver or whole-library test.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
