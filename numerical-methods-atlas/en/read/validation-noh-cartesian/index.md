# Noh:2D Cartesian flow and grid orientation error

A small 2D Euler finite-volume calculation evolves density, both momenta and total energy over the full square. Three grids,32²/64²/128², measure Noh-reference errors, budgets and grid orientation effects. The picture shows the actual evolved 2D array.

These additional validation supplements are managed separately from the common 22-example registry. Receipts cover independent ZIP extraction, tests and every fixed input within each group. Changes of settings, methods or step sizes do not add independent physical problems.

## Noh problem: an actual 2D Cartesian Euler calculation

A small 2D Euler finite-volume calculation evolves density, both momenta and total energy over the full square. Three grids,32²/64²/128², measure Noh-reference errors, budgets and grid orientation effects. The picture shows the actual evolved 2D array.

**Methods used**

- [Rusanov / local Lax–Friedrichs flux](https://hrkoyama.github.io/numerical-methods-atlas/methods/rusanov/?lang=en) (`rusanov`)
- [Heun / SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en) (`heun`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-cartesian-2d/?lang=en#noh-cartesian-2d-en-algorithm)

Unsplit shared-face x/y piecewise-constant Rusanov fluxes and SSPRK2/Heun. CFL .35 uses (max a_x+max a_y)/dx. Cold physical outer fluxes are spatially integrated analytically and their affine time dependence is integrated at both Heun stages. No cell repair, pressure floor/seed or hidden timestep retry; invalid stages retain raw arrays and fail.

$$
\partial_t U+\partial_xF(U)+\partial_yG(U)=0,\quad U=(\rho,\rho u,\rho v,E)^T
$$

$$
r_s=t/3,\quad(\rho,p,u_r)_2=(16,16/3,0),\quad(\rho,p,u_r)_1=(1+t/r,0,-1)
$$

$$
\bar\rho_i=\frac{1}{\Delta x\Delta y}\int_{C_i}\rho_{\rm exact}(\sqrt{x^2+y^2},t)\,dx\,dy
$$

$$
M(t)=4R^2+8Rt\operatorname{asinh}(1)+\pi t^2,\qquad E_{\rm tot}=M/2,\quad R=0.5
$$

$$
\Delta t=\frac{0.35}{\max a_x/\Delta x+\max a_y/\Delta y}
$$

- [Compressible Euler equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#euler-en) (`euler`)

Two-dimensional Cartesian Euler without a geometric source, evolving density, both momenta and energy over the full square.


**Problem figure**

![Noh problem: an actual 2D Cartesian Euler calculation: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/noh-cartesian/results/noh-cartesian-2d.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Noh problem: cold converging flow and outward shock](https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=en) (`noh`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-cartesian-2d/?lang=en#noh-cartesian-2d-en-validation)

Inputs/source/acceptance hashes are saved before execution. All 19 unit tests and 49 gates on three grids passed at the first attempt. Analytic density is integrated over cells by splitting shock-circle cuts and 64-point Gauss quadrature with x=rs sin(theta), checked against 128 points and analytic total mass; these are quadrature references, not closed-form exact cell means. At 128², full-square density L1=.09981, origin-inclusive core L1=.12231; shock errors are.968 axis cells and1.469 diagonal cells. Maximum relative discrete-budget residual is about 4.6e-15. D4 conserved parity and continuous rotational symmetry are measured separately.

- [Noh cold-inflow shock: planar, cylindrical and spherical symmetry](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-noh-en) (`noh`; Same-problem reference · Analytic reference)

Analytic reference for the same Noh problem.1D uses exact conserved-volume means;2D uses density means from shock-split Cartesian cell quadrature. Distinguish points/cell means and p(mean U)/mean p.
### Assumptions, units and boundaries

Nondimensional [-.5,.5]², gamma=5/3, rho0=1, inward speed 1, p0=0, T=.6, shock radius.2. Initial conserved states are cell-center cold samples, not exact initial momentum means. All four edges prescribe supersonic inflow rho=1+t/r and u=(-x/r,-y/r). No symmetry boundary, radial projection or geometric source.

### Adopted numerical method

Unsplit shared-face x/y piecewise-constant Rusanov fluxes and SSPRK2/Heun. CFL .35 uses (max a_x+max a_y)/dx. Cold physical outer fluxes are spatially integrated analytically and their affine time dependence is integrated at both Heun stages. No cell repair, pressure floor/seed or hidden timestep retry; invalid stages retain raw arrays and fail.

$$
\partial_t U+\partial_xF(U)+\partial_yG(U)=0,\quad U=(\rho,\rho u,\rho v,E)^T
$$

$$
r_s=t/3,\quad(\rho,p,u_r)_2=(16,16/3,0),\quad(\rho,p,u_r)_1=(1+t/r,0,-1)
$$

$$
\bar\rho_i=\frac{1}{\Delta x\Delta y}\int_{C_i}\rho_{\rm exact}(\sqrt{x^2+y^2},t)\,dx\,dy
$$

$$
M(t)=4R^2+8Rt\operatorname{asinh}(1)+\pi t^2,\qquad E_{\rm tot}=M/2,\quad R=0.5
$$

$$
\Delta t=\frac{0.35}{\max a_x/\Delta x+\max a_y/\Delta y}
$$

### References and validation

Inputs/source/acceptance hashes are saved before execution. All 19 unit tests and 49 gates on three grids passed at the first attempt. Analytic density is integrated over cells by splitting shock-circle cuts and 64-point Gauss quadrature with x=rs sin(theta), checked against 128 points and analytic total mass; these are quadrature references, not closed-form exact cell means. At 128², full-square density L1=.09981, origin-inclusive core L1=.12231; shock errors are.968 axis cells and1.469 diagonal cells. Maximum relative discrete-budget residual is about 4.6e-15. D4 conserved parity and continuous rotational symmetry are measured separately.

### Limits

A first-order-space lightweight example retains origin heating and shock errors. Finest maximum center specific internal energy is still about 14% high. Axis/diagonal shock-radius difference is about .501dx and is not monotone over these grids. Roundoff-level D4 parity does not establish exact circular symmetry. General perturbation stability, displaced origins, rotated meshes, 3D Cartesian flow and high-order accuracy are unverified. Earlier planar/cylindrical/spherical 1D editions and gates remain unchanged.

### Stored measurements and decisions

```json
{
  "metrics": {
    "n": 128,
    "steps": 494,
    "time": 0.6,
    "density_l1": 0.09980879898658265,
    "density_l2": 0.19425569047493216,
    "density_linf": 0.5034609713695807,
    "core_density_l1": 0.12230837999864347,
    "plateau_density_relative_error": 0.11211523785241806,
    "plateau_pressure_relative_error": 0.06423624701669228,
    "center_max_internal_energy_excess": 0.13988852566613885,
    "center_min_density": 13.207234408428087,
    "density_min": 1.856867213907176,
    "density_max": 16.460396201777943,
    "minimum_density_all_stages": 1.0,
    "minimum_pressure_all_stages": 0.0,
    "minimum_internal_roundoff_units": 0.0,
    "state_floor_count": 0,
    "d4_conserved_parity_relative": 0.0,
    "reference_order_relative_l1_difference": 3.485261130218118e-18,
    "reference_mass_relative_error": 0.0,
    "mass_vs_analytic_relative": 1.7763568394002505e-15,
    "energy_vs_analytic_relative": 3.3306690738754696e-15,
    "axis_shock_radius": 0.20756435977317667,
    "diagonal_shock_radius": 0.2114756773594714,
    "axis_shock_error_cells": 0.9682380509666153,
    "diagonal_shock_error_cells": 1.468886702012341,
    "shock_axis_diagonal_difference_cells": 0.5006486510457258
  },
  "checks": {
    "all three Cartesian grids complete": true,
    "n32: positive density all stages": true,
    "n32: internal energy within roundoff": true,
    "n32: no floors or cell repair": true,
    "n32: mass discrete balance": true,
    "n32: x momentum discrete balance": true,
    "n32: y momentum discrete balance": true,
    "n32: energy discrete balance": true,
    "n32: mass_vs_analytic_relative": true,
    "n32: energy_vs_analytic_relative": true,
    "n32: d4_conserved_parity_relative": true,
    "n32: reference_order_relative_l1_difference": true,
    "n32: reference_mass_relative_error": true,
    "n32: unmasked center and maximum errors reported": true,
    "n64: positive density all stages": true,
    "n64: internal energy within roundoff": true,
    "n64: no floors or cell repair": true,
    "n64: mass discrete balance": true,
    "n64: x momentum discrete balance": true,
    "n64: y momentum discrete balance": true,
    "n64: energy discrete balance": true,
    "n64: mass_vs_analytic_relative": true,
    "n64: energy_vs_analytic_relative": true,
    "n64: d4_conserved_parity_relative": true,
    "n64: reference_order_relative_l1_difference": true,
    "n64: reference_mass_relative_error": true,
    "n64: unmasked center and maximum errors reported": true,
    "n128: positive density all stages": true,
    "n128: internal energy within roundoff": true,
    "n128: no floors or cell repair": true,
    "n128: mass discrete balance": true,
    "n128: x momentum discrete balance": true,
    "n128: y momentum discrete balance": true,
    "n128: energy discrete balance": true,
    "n128: mass_vs_analytic_relative": true,
    "n128: energy_vs_analytic_relative": true,
    "n128: d4_conserved_parity_relative": true,
    "n128: reference_order_relative_l1_difference": true,
    "n128: reference_mass_relative_error": true,
    "n128: unmasked center and maximum errors reported": true,
    "finest density_l1": true,
    "finest core_density_l1": true,
    "finest plateau_density_relative_error": true,
    "finest plateau_pressure_relative_error": true,
    "finest axis_shock_error_cells": true,
    "finest diagonal_shock_error_cells": true,
    "finest shock_axis_diagonal_difference_cells": true,
    "density L1 decreases": true,
    "last pair density L1 order": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-cartesian-2d/index.json

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/noh-cartesian/atlas-noh-cartesian-2026-11-23-r2.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/noh-cartesian/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/noh-cartesian/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/noh-cartesian/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group.

### Sources and review scope

- W. F. Noh (1987). Errors for calculations of strong shocks using an artificial viscosity and an artificial heat flux. https://www.sciencedirect.com/science/article/pii/002199918790074X; review_level=publisher-metadata-and-abstract
  Publisher metadata and abstract checked; full original text was not accessed (403). Cited for the problem and heating-error analysis, not as the source of this particular finite-volume discretization.
- J. Thrussell and J. M. Ferguson (2023). ExactPack: A python library of exact analytic solutions. https://doi.org/10.1016/j.softx.2023.101560; review_level=official-record-and-unmodified-pinned-code-execution
  Selected pinned official Noh evaluator code checked. Reuse previously independently executed d=2 point values away from the jump; no new ExactPack execution or independent 2D PDE-engine comparison.

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
