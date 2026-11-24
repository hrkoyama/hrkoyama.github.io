# 2D shadows,beams and M1 closure

Compute absorber shadows and opposing beams with discrete ordinates and M1, separately checking the closed M1 PDE with a manufactured solution.

These additional validation supplements are managed separately from the common 22-example registry. Receipts cover independent ZIP extraction, tests and every fixed input within each group. Changes of settings, methods or step sizes do not add independent physical problems.

## Two-dimensional absorber shadow and M1 transport

Compare the actual evolved circular-absorber shadow with characteristic chord attenuation, signed-angle transport and nonlinear M1.

**Methods used**

- [Radiation transport and moment methods](https://hrkoyama.github.io/numerical-methods-atlas/methods/radiation-transport/?lang=en) (`radiation-transport`)
- [Upwind finite differences](https://hrkoyama.github.io/numerical-methods-atlas/methods/upwind/?lang=en) (`upwind`)
- [Heun / SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en) (`heun`)
- [Rusanov / local Lax–Friedrichs flux](https://hrkoyama.github.io/numerical-methods-atlas/methods/rusanov/?lang=en) (`rusanov`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/shadow-absorber2d/?lang=en#shadow-absorber2d-en-algorithm)

Conservative upwind angular finite volumes or M1 Rusanov fluxes with SSPRK2; exponential absorption with a separate deposited-energy ledger. Six axis directions have weight1/6; a unit beam has nodal intensity6. Retain Pzz and the full3D trace. No positive floor or cone projection. The revised general directional local-LF coefficient is the maximum of endpoint spectral radii,an independently derived cone-splitting bound,and normal reduced flux. Use the same face rule on all ghost boundaries and in the ledger. Explicit speed-only vacuum/allowed-roundoff extension1 is counted; no U/P projection or special beam branch. Preserve the original c1 transverse-diffusion failure.

$$
\partial_tE+\nabla\cdot\mathbf F=-\kappa_aE,\quad\partial_t\mathbf F+\nabla\cdot\mathbf P=-\kappa_a\mathbf F
$$

$$
\mathbf P=E\left[\frac{1-\chi}{2}\mathbf I_3+\frac{3\chi-1}{2}\mathbf n\otimes\mathbf n\right]
$$

$$
\chi=\frac{3+4f^2}{5+2\sqrt{4-3f^2}},\quad f=|\mathbf F|/E,\quad P_{xx}+P_{yy}+P_{zz}=E
$$

- [Static grey radiative transfer,scattering and linear exchange](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#static-grey-transfer-en) (`static-grey-transfer`)

Two spatial dimensions, a three-dimensional angular measure, c=1 and static absorption. Evolve the actual signed-angle and nonlinear M1 equations on24/48/96grids. Same-solver controls retain a varying-direction manufactured solution and crossed x/y packets.

- [Static grey M1 moments in flat spacetime](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#static-grey-m1-en) (`static-grey-m1`)

Two spatial dimensions, a three-dimensional angular measure, c=1 and static absorption. Evolve the actual signed-angle and nonlinear M1 equations on24/48/96grids. Same-solver controls retain a varying-direction manufactured solution and crossed x/y packets.


**Problem figure**

![Two-dimensional absorber shadow and M1 transport: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/results/shadow-absorber2d.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Two-dimensional absorber shadow and M1 transport](https://hrkoyama.github.io/numerical-methods-atlas/problems/shadow-absorber2d/?lang=en) (`shadow-absorber2d`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/shadow-absorber2d/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/shadow-absorber2d/?lang=en#shadow-absorber2d-en-validation)

The independent characteristic cell averages and manufactured M1 forcing passed191reference/component checks before any PDE main. Check all-step budgets, realizability and positivity, spatial refinement, a separate half-step probe, and actual x/y evolution. Opposing-beam closure error is distinguished from numerical error. The new general flux passed762fixed component checks before this revised PDE main. Retain the17old tests and add5directional regressions=22tests; all24fixed runs and166scientific gates remain unchanged under the same120second limit.

- [Circular-absorber characteristic reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-shadow-absorber2d-en) (`shadow-absorber2d`; Same-problem reference · Analytic reference)

Six aligned directions do not demonstrate general angular convergence. The M1 opposing-beam mismatch is expected information loss and is not required to converge to angular transport. No relativistic, gas-dynamical or multifrequency radiation hydrodynamics is implemented.
### Assumptions, units and boundaries

Two spatial dimensions, a three-dimensional angular measure, c=1 and static absorption. Evolve the actual signed-angle and nonlinear M1 equations on24/48/96grids. Same-solver controls retain a varying-direction manufactured solution and crossed x/y packets.

**Editorial clarification**

Six aligned directions do not demonstrate general angular convergence. The M1 opposing-beam mismatch is expected information loss and is not required to converge to angular transport. No relativistic, gas-dynamical or multifrequency radiation hydrodynamics is implemented.

### Adopted numerical method

Conservative upwind angular finite volumes or M1 Rusanov fluxes with SSPRK2; exponential absorption with a separate deposited-energy ledger. Six axis directions have weight1/6; a unit beam has nodal intensity6. Retain Pzz and the full3D trace. No positive floor or cone projection. The revised general directional local-LF coefficient is the maximum of endpoint spectral radii,an independently derived cone-splitting bound,and normal reduced flux. Use the same face rule on all ghost boundaries and in the ledger. Explicit speed-only vacuum/allowed-roundoff extension1 is counted; no U/P projection or special beam branch. Preserve the original c1 transverse-diffusion failure.

$$
\partial_tE+\nabla\cdot\mathbf F=-\kappa_aE,\quad\partial_t\mathbf F+\nabla\cdot\mathbf P=-\kappa_a\mathbf F
$$

$$
\mathbf P=E\left[\frac{1-\chi}{2}\mathbf I_3+\frac{3\chi-1}{2}\mathbf n\otimes\mathbf n\right]
$$

$$
\chi=\frac{3+4f^2}{5+2\sqrt{4-3f^2}},\quad f=|\mathbf F|/E,\quad P_{xx}+P_{yy}+P_{zz}=E
$$

### References and validation

The independent characteristic cell averages and manufactured M1 forcing passed191reference/component checks before any PDE main. Check all-step budgets, realizability and positivity, spatial refinement, a separate half-step probe, and actual x/y evolution. Opposing-beam closure error is distinguished from numerical error. The new general flux passed762fixed component checks before this revised PDE main. Retain the17old tests and add5directional regressions=22tests; all24fixed runs and166scientific gates remain unchanged under the same120second limit.

### Limits

Six aligned directions do not demonstrate general angular convergence. The M1 opposing-beam mismatch is expected information loss and is not required to converge to angular transport. No relativistic, gas-dynamical or multifrequency radiation hydrodynamics is implemented.

### Stored measurements and decisions

```json
{
  "metrics": {
    "M1_numerical_flux": "General directional localLF:max endpoint spectralradius,LFcone-splitting bound and absolute normal reducedflux;not a nonlinearRiemannfan bound",
    "completed_primary_and_control_runs": 8,
    "spatial_dimensions": 2,
    "angular_dimensions": 3,
    "Pzz_retained": true
  },
  "checks": {
    "shadow-sn-n24/all-stages-finite": true,
    "shadow-sn-n24/positive-energy": true,
    "shadow-sn-n24/realizability": true,
    "shadow-sn-n24/energy-budget": true,
    "shadow-sn-n24/full3D-pressure-trace": true,
    "shadow-sn-n24/five-fixed-snapshots": true,
    "shadow-sn-n48/all-stages-finite": true,
    "shadow-sn-n48/positive-energy": true,
    "shadow-sn-n48/realizability": true,
    "shadow-sn-n48/energy-budget": true,
    "shadow-sn-n48/full3D-pressure-trace": true,
    "shadow-sn-n48/five-fixed-snapshots": true,
    "shadow-sn-n96/all-stages-finite": true,
    "shadow-sn-n96/positive-energy": true,
    "shadow-sn-n96/realizability": true,
    "shadow-sn-n96/energy-budget": true,
    "shadow-sn-n96/full3D-pressure-trace": true,
    "shadow-sn-n96/five-fixed-snapshots": true,
    "shadow-m1-n24/all-stages-finite": true,
    "shadow-m1-n24/positive-energy": true,
    "shadow-m1-n24/realizability": true,
    "shadow-m1-n24/energy-budget": true,
    "shadow-m1-n24/full3D-pressure-trace": true,
    "shadow-m1-n24/five-fixed-snapshots": true,
    "shadow-m1-n48/all-stages-finite": true,
    "shadow-m1-n48/positive-energy": true,
    "shadow-m1-n48/realizability": true,
    "shadow-m1-n48/energy-budget": true,
    "shadow-m1-n48/full3D-pressure-trace": true,
    "shadow-m1-n48/five-fixed-snapshots": true,
    "shadow-m1-n96/all-stages-finite": true,
    "shadow-m1-n96/positive-energy": true,
    "shadow-m1-n96/realizability": true,
    "shadow-m1-n96/energy-budget": true,
    "shadow-m1-n96/full3D-pressure-trace": true,
    "shadow-m1-n96/five-fixed-snapshots": true,
    "shadow-sn-n96-half-dt/all-stages-finite": true,
    "shadow-sn-n96-half-dt/positive-energy": true,
    "shadow-sn-n96-half-dt/realizability": true,
    "shadow-sn-n96-half-dt/energy-budget": true,
    "shadow-sn-n96-half-dt/full3D-pressure-trace": true,
    "shadow-sn-n96-half-dt/five-fixed-snapshots": true,
    "shadow-m1-n96-half-dt/all-stages-finite": true,
    "shadow-m1-n96-half-dt/positive-energy": true,
    "shadow-m1-n96-half-dt/realizability": true,
    "shadow-m1-n96-half-dt/energy-budget": true,
    "shadow-m1-n96-half-dt/full3D-pressure-trace": true,
    "shadow-m1-n96-half-dt/five-fixed-snapshots": true,
    "shadow/sn/refinement-n48": true,
    "shadow/sn/refinement-n96": true,
    "shadow/sn/finest-reference": true,
    "shadow/sn/separate-time-sensitivity": true,
    "shadow/m1/refinement-n48": true,
    "shadow/m1/refinement-n96": true,
    "shadow/m1/finest-reference": true,
    "shadow/m1/separate-time-sensitivity": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/shadow-absorber2d/index.json

![Scientific preview from the actual saved numerical fields.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/results/shadow-absorber2d-preview.png)

Scientific preview from the actual saved numerical fields.

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/atlas-radiation-geometry-2026-11-24.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- Rosdahl etal. (2013). RAMSES-RT: Radiation hydrodynamics in the cosmological context [accessed 2026-11-24]. https://arxiv.org/html/1304.7126v2; review_level=primary-paper-selected-M1-equations-and-limitations
ReadSection2equations12-14and two-opposing-beams limitation text. Levermore1984original not read. Educational staticgrey cases/MMS here do not reproduce RAMSESastrophysical runs.

- M. A. Skinner and E. C. Ostriker (2013). A Two-moment Radiation Hydrodynamics Module in Athena Using a Time-Explicit Godunov Method [accessed 2026-11-24]. https://arxiv.org/pdf/1306.0010; review_level=primary-selected-section-by-independent-mathematical-reviewer
Independent reviewer actually read selected extracted Section3.3equations37–41and eigenvalue limits;not a whole-paper/rendered-symbol audit. Directional LF cone root/weighted-CFL algebra is separately authored and independently crosschecked,not a transplanted HLL solver or claimed general Riemann-fan bound.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## Opposing beams and information loss in the M1 closure

Show the M1 limitation in actual opposing-packet evolution; validate the same closed M1 solver independently with a manufactured solution.

**Methods used**

- [Radiation transport and moment methods](https://hrkoyama.github.io/numerical-methods-atlas/methods/radiation-transport/?lang=en) (`radiation-transport`)
- [Upwind finite differences](https://hrkoyama.github.io/numerical-methods-atlas/methods/upwind/?lang=en) (`upwind`)
- [Heun / SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en) (`heun`)
- [Rusanov / local Lax–Friedrichs flux](https://hrkoyama.github.io/numerical-methods-atlas/methods/rusanov/?lang=en) (`rusanov`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/opposing-beams2d/?lang=en#opposing-beams2d-en-algorithm)

Conservative upwind angular finite volumes or M1 Rusanov fluxes with SSPRK2; exponential absorption with a separate deposited-energy ledger. Six axis directions have weight1/6; a unit beam has nodal intensity6. Retain Pzz and the full3D trace. No positive floor or cone projection. The revised general directional local-LF coefficient is the maximum of endpoint spectral radii,an independently derived cone-splitting bound,and normal reduced flux. Use the same face rule on all ghost boundaries and in the ledger. Explicit speed-only vacuum/allowed-roundoff extension1 is counted; no U/P projection or special beam branch. Preserve the original c1 transverse-diffusion failure.

$$
\partial_tE+\nabla\cdot\mathbf F=-\kappa_aE,\quad\partial_t\mathbf F+\nabla\cdot\mathbf P=-\kappa_a\mathbf F
$$

$$
\mathbf P=E\left[\frac{1-\chi}{2}\mathbf I_3+\frac{3\chi-1}{2}\mathbf n\otimes\mathbf n\right]
$$

$$
\chi=\frac{3+4f^2}{5+2\sqrt{4-3f^2}},\quad f=|\mathbf F|/E,\quad P_{xx}+P_{yy}+P_{zz}=E
$$

- [Static grey radiative transfer,scattering and linear exchange](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#static-grey-transfer-en) (`static-grey-transfer`)

Two spatial dimensions, a three-dimensional angular measure, c=1 and static absorption. Evolve the actual signed-angle and nonlinear M1 equations on24/48/96grids. Same-solver controls retain a varying-direction manufactured solution and crossed x/y packets.

- [Static grey M1 moments in flat spacetime](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#static-grey-m1-en) (`static-grey-m1`)

Two spatial dimensions, a three-dimensional angular measure, c=1 and static absorption. Evolve the actual signed-angle and nonlinear M1 equations on24/48/96grids. Same-solver controls retain a varying-direction manufactured solution and crossed x/y packets.


**Problem figure**

![Opposing beams and information loss in the M1 closure: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/results/opposing-beams2d.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Opposing beams and information loss in the M1 closure](https://hrkoyama.github.io/numerical-methods-atlas/problems/opposing-beams2d/?lang=en) (`opposing-beams2d`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/opposing-beams2d/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/opposing-beams2d/?lang=en#opposing-beams2d-en-validation)

The independent characteristic cell averages and manufactured M1 forcing passed191reference/component checks before any PDE main. Check all-step budgets, realizability and positivity, spatial refinement, a separate half-step probe, and actual x/y evolution. Opposing-beam closure error is distinguished from numerical error. The new general flux passed762fixed component checks before this revised PDE main. Retain the17old tests and add5directional regressions=22tests; all24fixed runs and166scientific gates remain unchanged under the same120second limit.

- [Counterpropagating packet characteristic reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-opposing-beams2d-en) (`opposing-beams2d`; Same-problem reference · Analytic reference)

Six aligned directions do not demonstrate general angular convergence. The M1 opposing-beam mismatch is expected information loss and is not required to converge to angular transport. No relativistic, gas-dynamical or multifrequency radiation hydrodynamics is implemented.
### Assumptions, units and boundaries

Two spatial dimensions, a three-dimensional angular measure, c=1 and static absorption. Evolve the actual signed-angle and nonlinear M1 equations on24/48/96grids. Same-solver controls retain a varying-direction manufactured solution and crossed x/y packets.

**Editorial clarification**

Six aligned directions do not demonstrate general angular convergence. The M1 opposing-beam mismatch is expected information loss and is not required to converge to angular transport. No relativistic, gas-dynamical or multifrequency radiation hydrodynamics is implemented.

### Adopted numerical method

Conservative upwind angular finite volumes or M1 Rusanov fluxes with SSPRK2; exponential absorption with a separate deposited-energy ledger. Six axis directions have weight1/6; a unit beam has nodal intensity6. Retain Pzz and the full3D trace. No positive floor or cone projection. The revised general directional local-LF coefficient is the maximum of endpoint spectral radii,an independently derived cone-splitting bound,and normal reduced flux. Use the same face rule on all ghost boundaries and in the ledger. Explicit speed-only vacuum/allowed-roundoff extension1 is counted; no U/P projection or special beam branch. Preserve the original c1 transverse-diffusion failure.

$$
\partial_tE+\nabla\cdot\mathbf F=-\kappa_aE,\quad\partial_t\mathbf F+\nabla\cdot\mathbf P=-\kappa_a\mathbf F
$$

$$
\mathbf P=E\left[\frac{1-\chi}{2}\mathbf I_3+\frac{3\chi-1}{2}\mathbf n\otimes\mathbf n\right]
$$

$$
\chi=\frac{3+4f^2}{5+2\sqrt{4-3f^2}},\quad f=|\mathbf F|/E,\quad P_{xx}+P_{yy}+P_{zz}=E
$$

### References and validation

The independent characteristic cell averages and manufactured M1 forcing passed191reference/component checks before any PDE main. Check all-step budgets, realizability and positivity, spatial refinement, a separate half-step probe, and actual x/y evolution. Opposing-beam closure error is distinguished from numerical error. The new general flux passed762fixed component checks before this revised PDE main. Retain the17old tests and add5directional regressions=22tests; all24fixed runs and166scientific gates remain unchanged under the same120second limit.

### Limits

Six aligned directions do not demonstrate general angular convergence. The M1 opposing-beam mismatch is expected information loss and is not required to converge to angular transport. No relativistic, gas-dynamical or multifrequency radiation hydrodynamics is implemented.

### Stored measurements and decisions

```json
{
  "metrics": {
    "same_solver_controls": [
      "nonlinear-closed-M1-MMS",
      "actual-x-and-y-crossed-angular-packets"
    ],
    "M1_transport_difference_is_model_error": true,
    "M1_numerical_flux": "General directional localLF:max endpoint spectralradius,LFcone-splitting bound and absolute normal reducedflux;not a nonlinearRiemannfan bound",
    "completed_primary_and_control_runs": 16,
    "spatial_dimensions": 2,
    "angular_dimensions": 3,
    "Pzz_retained": true
  },
  "checks": {
    "beams-sn-n24/all-stages-finite": true,
    "beams-sn-n24/positive-energy": true,
    "beams-sn-n24/realizability": true,
    "beams-sn-n24/energy-budget": true,
    "beams-sn-n24/full3D-pressure-trace": true,
    "beams-sn-n24/five-fixed-snapshots": true,
    "beams-sn-n48/all-stages-finite": true,
    "beams-sn-n48/positive-energy": true,
    "beams-sn-n48/realizability": true,
    "beams-sn-n48/energy-budget": true,
    "beams-sn-n48/full3D-pressure-trace": true,
    "beams-sn-n48/five-fixed-snapshots": true,
    "beams-sn-n96/all-stages-finite": true,
    "beams-sn-n96/positive-energy": true,
    "beams-sn-n96/realizability": true,
    "beams-sn-n96/energy-budget": true,
    "beams-sn-n96/full3D-pressure-trace": true,
    "beams-sn-n96/five-fixed-snapshots": true,
    "beams-m1-n24/all-stages-finite": true,
    "beams-m1-n24/positive-energy": true,
    "beams-m1-n24/realizability": true,
    "beams-m1-n24/energy-budget": true,
    "beams-m1-n24/full3D-pressure-trace": true,
    "beams-m1-n24/five-fixed-snapshots": true,
    "beams-m1-n48/all-stages-finite": true,
    "beams-m1-n48/positive-energy": true,
    "beams-m1-n48/realizability": true,
    "beams-m1-n48/energy-budget": true,
    "beams-m1-n48/full3D-pressure-trace": true,
    "beams-m1-n48/five-fixed-snapshots": true,
    "beams-m1-n96/all-stages-finite": true,
    "beams-m1-n96/positive-energy": true,
    "beams-m1-n96/realizability": true,
    "beams-m1-n96/energy-budget": true,
    "beams-m1-n96/full3D-pressure-trace": true,
    "beams-m1-n96/five-fixed-snapshots": true,
    "beams-sn-n96-half-dt/all-stages-finite": true,
    "beams-sn-n96-half-dt/positive-energy": true,
    "beams-sn-n96-half-dt/realizability": true,
    "beams-sn-n96-half-dt/energy-budget": true,
    "beams-sn-n96-half-dt/full3D-pressure-trace": true,
    "beams-sn-n96-half-dt/five-fixed-snapshots": true,
    "beams-m1-n96-half-dt/all-stages-finite": true,
    "beams-m1-n96-half-dt/positive-energy": true,
    "beams-m1-n96-half-dt/realizability": true,
    "beams-m1-n96-half-dt/energy-budget": true,
    "beams-m1-n96-half-dt/full3D-pressure-trace": true,
    "beams-m1-n96-half-dt/five-fixed-snapshots": true,
    "beams/sn/refinement-n48": true,
    "beams/sn/refinement-n96": true,
    "beams/sn/finest-reference": true,
    "beams/sn/separate-time-sensitivity": true,
    "beams/m1/separate-time-sensitivity": true,
    "mms-m1-n16/all-stages-finite": true,
    "mms-m1-n16/positive-energy": true,
    "mms-m1-n16/realizability": true,
    "mms-m1-n16/energy-budget": true,
    "mms-m1-n16/full3D-pressure-trace": true,
    "mms-m1-n16/five-fixed-snapshots": true,
    "mms-m1-n32/all-stages-finite": true,
    "mms-m1-n32/positive-energy": true,
    "mms-m1-n32/realizability": true,
    "mms-m1-n32/energy-budget": true,
    "mms-m1-n32/full3D-pressure-trace": true,
    "mms-m1-n32/five-fixed-snapshots": true,
    "mms-m1-n64/all-stages-finite": true,
    "mms-m1-n64/positive-energy": true,
    "mms-m1-n64/realizability": true,
    "mms-m1-n64/energy-budget": true,
    "mms-m1-n64/full3D-pressure-trace": true,
    "mms-m1-n64/five-fixed-snapshots": true,
    "mms-m1-n64-half-dt/all-stages-finite": true,
    "mms-m1-n64-half-dt/positive-energy": true,
    "mms-m1-n64-half-dt/realizability": true,
    "mms-m1-n64-half-dt/energy-budget": true,
    "mms-m1-n64-half-dt/full3D-pressure-trace": true,
    "mms-m1-n64-half-dt/five-fixed-snapshots": true,
    "crossed-sn-n24/all-stages-finite": true,
    "crossed-sn-n24/positive-energy": true,
    "crossed-sn-n24/realizability": true,
    "crossed-sn-n24/energy-budget": true,
    "crossed-sn-n24/full3D-pressure-trace": true,
    "crossed-sn-n24/five-fixed-snapshots": true,
    "crossed-sn-n48/all-stages-finite": true,
    "crossed-sn-n48/positive-energy": true,
    "crossed-sn-n48/realizability": true,
    "crossed-sn-n48/energy-budget": true,
    "crossed-sn-n48/full3D-pressure-trace": true,
    "crossed-sn-n48/five-fixed-snapshots": true,
    "crossed-sn-n96/all-stages-finite": true,
    "crossed-sn-n96/positive-energy": true,
    "crossed-sn-n96/realizability": true,
    "crossed-sn-n96/energy-budget": true,
    "crossed-sn-n96/full3D-pressure-trace": true,
    "crossed-sn-n96/five-fixed-snapshots": true,
    "crossed-sn-n96-half-dt/all-stages-finite": true,
    "crossed-sn-n96-half-dt/positive-energy": true,
    "crossed-sn-n96-half-dt/realizability": true,
    "crossed-sn-n96-half-dt/energy-budget": true,
    "crossed-sn-n96-half-dt/full3D-pressure-trace": true,
    "crossed-sn-n96-half-dt/five-fixed-snapshots": true,
    "mms/m1/refinement-n32": true,
    "mms/m1/refinement-n64": true,
    "mms/m1/finest-reference": true,
    "mms/m1/separate-time-sensitivity": true,
    "crossed/sn/refinement-n48": true,
    "crossed/sn/refinement-n96": true,
    "crossed/sn/finest-reference": true,
    "crossed/sn/separate-time-sensitivity": true,
    "head-on-closure-information-defect": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/opposing-beams2d/index.json

![Scientific preview from the actual saved numerical fields.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/results/opposing-beams2d-preview.png)

Scientific preview from the actual saved numerical fields.

![Independent manufactured energy,actual evolved energy,and signed error from the same varying-direction M1 solver.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/results/m1-manufactured-control.png)

Independent manufactured energy,actual evolved energy,and signed error from the same varying-direction M1 solver.

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/atlas-radiation-geometry-2026-11-24.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-geometry/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- Rosdahl etal. (2013). RAMSES-RT: Radiation hydrodynamics in the cosmological context [accessed 2026-11-24]. https://arxiv.org/html/1304.7126v2; review_level=primary-paper-selected-M1-equations-and-limitations
ReadSection2equations12-14and two-opposing-beams limitation text. Levermore1984original not read. Educational staticgrey cases/MMS here do not reproduce RAMSESastrophysical runs.

- M. A. Skinner and E. C. Ostriker (2013). A Two-moment Radiation Hydrodynamics Module in Athena Using a Time-Explicit Godunov Method [accessed 2026-11-24]. https://arxiv.org/pdf/1306.0010; review_level=primary-selected-section-by-independent-mathematical-reviewer
Independent reviewer actually read selected extracted Section3.3equations37–41and eigenvalue limits;not a whole-paper/rendered-symbol audit. Directional LF cone root/weighted-CFL algebra is separately authored and independently crosschecked,not a transplanted HLL solver or claimed general Riemann-fan bound.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
