# Scoped ALE piston, sphere transport and SPH/GSPH controls

Fixed prescribed-ALE piston, limited sphere transport and axisymmetric balance, plus actual GSPH and separate SPH controls.

These additional validation supplements are managed separately from the common 22-example registry. Receipts cover independent ZIP extraction, tests and every fixed input within each group. Changes of settings, methods or step sizes do not add independent physical problems.

## Saltzman-type skew-grid piston: 2D Euler and ALE

Tan–Lv–Zhu2023 Example8 e0=1e-4 initialvariant. PrescribedaffineALEmesh, not theirWENO/materialLagrangian/remap scheme. Finitepressure RH cellaverages.

**Methods used**

- [ALE uniform-state / geometric-conservation model](https://hrkoyama.github.io/numerical-methods-atlas/methods/ale/?lang=en) (`ale`)
- [Rusanov / local Lax–Friedrichs flux](https://hrkoyama.github.io/numerical-methods-atlas/methods/rusanov/?lang=en) (`rusanov`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/saltzman-ale-piston/?lang=en#saltzman-ale-piston-en-algorithm)

Tan–Lv–Zhu2023 Example8 e0=1e-4 initialvariant. PrescribedaffineALEmesh, not theirWENO/materialLagrangian/remap scheme. Finitepressure RH cellaverages.

- [Compressible Euler equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#euler-en) (`euler`)

Tan–Lv–Zhu (2023) Example 8 variant with e0=1e-4 and finite initial pressure. Prescribed affine ALE, 2D Euler and Rusanov; not their material Lagrangian mesh, WENO/remap scheme or a full reproduction of the unread 1985 report.


**Problem figure**

![Saltzman-type skew-grid piston: 2D Euler and ALE: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/saltzman-ale-piston.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Saltzman-type skew-grid piston: 2D Euler and ALE](https://hrkoyama.github.io/numerical-methods-atlas/problems/saltzman-ale-piston/?lang=en) (`saltzman-ale-piston`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/saltzman-ale-piston/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/saltzman-ale-piston/?lang=en#saltzman-ale-piston-en-validation)

Separate analytic/reference errors, conservation, refinement, independent component qualification and deliberately wrong-formula controls.

- [Saltzman-type skew-grid piston: 2D Euler and ALE](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-saltzman-ale-piston-en) (`saltzman-ale-piston`; Same-problem reference · Analytic reference)

Bind the fixed-input formula, reference, figure and executable code. Tan–Lv–Zhu (2023) Example 8 variant with e0=1e-4 and finite initial pressure. Prescribed affine ALE, 2D Euler and Rusanov; not their material Lagrangian mesh, WENO/remap scheme or a full reproduction of the unread 1985 report.
### Assumptions, units and boundaries

Tan–Lv–Zhu2023 Example8 e0=1e-4 initialvariant. PrescribedaffineALEmesh, not theirWENO/materialLagrangian/remap scheme. Finitepressure RH cellaverages.

**Editorial clarification**

Tan–Lv–Zhu (2023) Example 8 variant with e0=1e-4 and finite initial pressure. Prescribed affine ALE, 2D Euler and Rusanov; not their material Lagrangian mesh, WENO/remap scheme or a full reproduction of the unread 1985 report.

### Adopted numerical method

Tan–Lv–Zhu2023 Example8 e0=1e-4 initialvariant. PrescribedaffineALEmesh, not theirWENO/materialLagrangian/remap scheme. Finitepressure RH cellaverages.

### References and validation

Separate analytic/reference errors, conservation, refinement, independent component qualification and deliberately wrong-formula controls.

### Limits

Tan–Lv–Zhu2023 Example8 e0=1e-4 initialvariant. PrescribedaffineALEmesh, not theirWENO/materialLagrangian/remap scheme. Finitepressure RH cellaverages.

### Stored measurements and decisions

```json
{
  "metrics": {
    "finest": {
      "grid": [
        80,
        8
      ],
      "density_error": 0.03966960674770006,
      "shock_error": 0.009071663139626374,
      "plateau_density_error": 0.060142667838002595,
      "plateau_pressure_error": 0.07005129077711092,
      "max_transverse": 0.08502093161153988,
      "mass_defect": 4.1551145858098734e-16,
      "momentum_defect": 1.3877787807814449e-15,
      "energy_defect": 3.5023519269671693e-15,
      "GCL": 3.7705883405261993e-17,
      "steps": 1333,
      "minimum_density": 0.9999999999997568,
      "minimum_pressure": 6.66666666666505e-05
    }
  },
  "checks": {
    "positive": true,
    "conservation": true,
    "GCL": true,
    "density": true,
    "refinement": true,
    "shock": true,
    "plateau": true,
    "transverse": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/saltzman-ale-piston/index.json

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/atlas-continuum-particle-controls-2026-11-25.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- Reformulation of Smoothed Particle Hydrodynamics with Riemann Solver. https://arxiv.org/pdf/astro-ph/0206401; review_level=selected-original-author-paper-sections-and-equations
- New Third-Order Finite Volume Unequal-Sized WENO Lagrangian Schemes for Solving Euler Equations. https://www.mdpi.com/2227-7390/11/23/4842; review_level=selected-publisher-fulltext-example-8
- Second Order Corner Coupled Upwind Transport Methods for Lagrangian Hydrodynamics. https://www.osti.gov/servlets/purl/15005665; review_level=secondary-bibliographic-identity-original-report-unread
- A standard test set for numerical approximations to the shallow water equations in spherical geometry. https://digital.library.unt.edu/ark:/67531/metadc1069483/; review_level=author-report-bibliography-and-abstract-original-formulas-unread
- Cascade interpolation for semi-Lagrangian advection over the sphere. https://www.image.ucar.edu/staff/rnair/qj99_sph.pdf; review_level=selected-author-hosted-formulas-and-publisher-bibliography

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## Williamson-type spherical rotation: tilted axes and pole crossing

Limitedprescribedscalartransport, radius1/3 nondimensionalvariant; not nonlinearSWE or exact1992fullpaperreproduction. Nair1999 selectedformulascrosscheck; bilinear method isAtlasoriginal.

**Methods used**

- [Semi-Lagrangian transport: a limited prescribed sphere rotation](https://hrkoyama.github.io/numerical-methods-atlas/methods/semi-lagrangian/?lang=en) (`semi-lagrangian`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/williamson-sphere-transport/?lang=en#williamson-sphere-transport-en-algorithm)

Limitedprescribedscalartransport, radius1/3 nondimensionalvariant; not nonlinearSWE or exact1992fullpaperreproduction. Nair1999 selectedformulascrosscheck; bilinear method isAtlasoriginal.

- [Prescribed scalar advection on a sphere](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#sphere-scalar-advection-en) (`sphere-scalar-advection`)

Only prescribed scalar solid-body rotation on a unit sphere. Original W92 equations remain unread; selected Nair author formulas cross-check conventions. Both grids use eleven noncommensurate remaps. Bilinear interpolation is nonconservative; report mass drift and do not claim temporal convergence or a nonlinear global SWE core.


**Problem figure**

![Williamson-type spherical rotation: tilted axes and pole crossing: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/williamson-sphere-transport.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Williamson-type spherical rotation: tilted axes and pole crossing](https://hrkoyama.github.io/numerical-methods-atlas/problems/williamson-sphere-transport/?lang=en) (`williamson-sphere-transport`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/williamson-sphere-transport/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/williamson-sphere-transport/?lang=en#williamson-sphere-transport-en-validation)

Separate analytic/reference errors, conservation, refinement, independent component qualification and deliberately wrong-formula controls.

- [Williamson-type spherical rotation: tilted axes and pole crossing](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-williamson-sphere-transport-en) (`williamson-sphere-transport`; Same-problem reference · Analytic reference)

Bind the fixed-input formula, reference, figure and executable code. Only prescribed scalar solid-body rotation on a unit sphere. Original W92 equations remain unread; selected Nair author formulas cross-check conventions. Both grids use eleven noncommensurate remaps. Bilinear interpolation is nonconservative; report mass drift and do not claim temporal convergence or a nonlinear global SWE core.
### Assumptions, units and boundaries

Limitedprescribedscalartransport, radius1/3 nondimensionalvariant; not nonlinearSWE or exact1992fullpaperreproduction. Nair1999 selectedformulascrosscheck; bilinear method isAtlasoriginal.

**Editorial clarification**

Only prescribed scalar solid-body rotation on a unit sphere. Original W92 equations remain unread; selected Nair author formulas cross-check conventions. Both grids use eleven noncommensurate remaps. Bilinear interpolation is nonconservative; report mass drift and do not claim temporal convergence or a nonlinear global SWE core.

### Adopted numerical method

Limitedprescribedscalartransport, radius1/3 nondimensionalvariant; not nonlinearSWE or exact1992fullpaperreproduction. Nair1999 selectedformulascrosscheck; bilinear method isAtlasoriginal.

### References and validation

Separate analytic/reference errors, conservation, refinement, independent component qualification and deliberately wrong-formula controls.

### Limits

Limitedprescribedscalartransport, radius1/3 nondimensionalvariant; not nonlinearSWE or exact1992fullpaperreproduction. Nair1999 selectedformulascrosscheck; bilinear method isAtlasoriginal.

### Stored measurements and decisions

```json
{
  "metrics": {
    "fine_L1": [
      0.17228372801445835,
      0.1983012829411487
    ]
  },
  "checks": {
    "error": true,
    "refinement": true,
    "mass": true,
    "bounds": true,
    "sphere_area": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/williamson-sphere-transport/index.json

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/atlas-continuum-particle-controls-2026-11-25.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- Reformulation of Smoothed Particle Hydrodynamics with Riemann Solver. https://arxiv.org/pdf/astro-ph/0206401; review_level=selected-original-author-paper-sections-and-equations
- New Third-Order Finite Volume Unequal-Sized WENO Lagrangian Schemes for Solving Euler Equations. https://www.mdpi.com/2227-7390/11/23/4842; review_level=selected-publisher-fulltext-example-8
- Second Order Corner Coupled Upwind Transport Methods for Lagrangian Hydrodynamics. https://www.osti.gov/servlets/purl/15005665; review_level=secondary-bibliographic-identity-original-report-unread
- A standard test set for numerical approximations to the shallow water equations in spherical geometry. https://digital.library.unt.edu/ark:/67531/metadc1069483/; review_level=author-report-bibliography-and-abstract-original-formulas-unread
- Cascade interpolation for semi-Lagrangian advection over the sphere. https://www.image.ucar.edu/staff/rnair/qj99_sph.pdf; review_level=selected-author-hosted-formulas-and-publisher-bibliography

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## Time evolution of axisymmetric spherical shallow-water balance

NondimensionalWilliamson2-type axisymmetricsubproblem. Analyticstaticstatevsactualtimeintegration; not fullglobaldynamicalcore/PVclaim.

**Methods used**

- [Centered spatial difference](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en) (`centered-difference`)
- [Classical RK4](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=en) (`rk4`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/sphere-zonal-balance/?lang=en#sphere-zonal-balance-en-algorithm)

NondimensionalWilliamson2-type axisymmetricsubproblem. Analyticstaticstatevsactualtimeintegration; not fullglobaldynamicalcore/PVclaim.

- [Axisymmetric spherical shallow-water subproblem](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#spherical-shallow-water-en) (`spherical-shallow-water`)

Axisymmetric nondimensional subproblem with a=g=1, Omega=2, u0=.5 and h0=10. Actual time evolution uses centered primitive momentum, finite-volume mass and RK4. Not standard Earth parameters, a full global multidimensional SWE core, exact discrete balance or a PV-conservation claim.


**Problem figure**

![Time evolution of axisymmetric spherical shallow-water balance: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/sphere-zonal-balance.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Time evolution of axisymmetric spherical shallow-water balance](https://hrkoyama.github.io/numerical-methods-atlas/problems/sphere-zonal-balance/?lang=en) (`sphere-zonal-balance`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/sphere-zonal-balance/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/sphere-zonal-balance/?lang=en#sphere-zonal-balance-en-validation)

Separate analytic/reference errors, conservation, refinement, independent component qualification and deliberately wrong-formula controls.

- [Time evolution of axisymmetric spherical shallow-water balance](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-sphere-zonal-balance-en) (`sphere-zonal-balance`; Same-problem reference · Analytic reference)

Bind the fixed-input formula, reference, figure and executable code. Axisymmetric nondimensional subproblem with a=g=1, Omega=2, u0=.5 and h0=10. Actual time evolution uses centered primitive momentum, finite-volume mass and RK4. Not standard Earth parameters, a full global multidimensional SWE core, exact discrete balance or a PV-conservation claim.
### Assumptions, units and boundaries

Nondimensional axisymmetric spherical SWE subproblem. Hybrid centered meridional differences for primitive momentum and latitude-band finite-volume face fluxes for mass, advanced by RK4. Pole mass flux is zero; no equilibrium residual subtraction or correction. Fixed inputs, boundaries and reference scope are specified in inputs.json.

**Editorial clarification**

Axisymmetric nondimensional subproblem with a=g=1, Omega=2, u0=.5 and h0=10. Actual time evolution uses centered primitive momentum, finite-volume mass and RK4. Not standard Earth parameters, a full global multidimensional SWE core, exact discrete balance or a PV-conservation claim.

### Adopted numerical method

NondimensionalWilliamson2-type axisymmetricsubproblem. Analyticstaticstatevsactualtimeintegration; not fullglobaldynamicalcore/PVclaim.

### References and validation

Separate analytic/reference errors, conservation, refinement, independent component qualification and deliberately wrong-formula controls.

### Limits

NondimensionalWilliamson2-type axisymmetricsubproblem. Analyticstaticstatevsactualtimeintegration; not fullglobaldynamicalcore/PVclaim.

### Stored measurements and decisions

```json
{
  "metrics": {
    "finest": {
      "grid": 64,
      "h_error": 0.00010108962138506427,
      "initial_balance_residual": 0.0018041320580228781,
      "analytic_force_residual": 0.0,
      "mass_defect": 0.0,
      "minimum_h": 8.87466665967074,
      "steps": 129
    }
  },
  "checks": {
    "analytic_balance": true,
    "balance_order": true,
    "height": true,
    "refinement": true,
    "mass": true,
    "positive": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/sphere-zonal-balance/index.json

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/atlas-continuum-particle-controls-2026-11-25.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- Reformulation of Smoothed Particle Hydrodynamics with Riemann Solver. https://arxiv.org/pdf/astro-ph/0206401; review_level=selected-original-author-paper-sections-and-equations
- New Third-Order Finite Volume Unequal-Sized WENO Lagrangian Schemes for Solving Euler Equations. https://www.mdpi.com/2227-7390/11/23/4842; review_level=selected-publisher-fulltext-example-8
- Second Order Corner Coupled Upwind Transport Methods for Lagrangian Hydrodynamics. https://www.osti.gov/servlets/purl/15005665; review_level=secondary-bibliographic-identity-original-report-unread
- A standard test set for numerical approximations to the shallow water equations in spherical geometry. https://digital.library.unt.edu/ark:/67531/metadc1069483/; review_level=author-report-bibliography-and-abstract-original-formulas-unread
- Cascade interpolation for semi-Lagrangian advection over the sphere. https://www.image.ucar.edu/staff/rnair/qj99_sph.pdf; review_level=selected-author-hosted-formulas-and-publisher-bibliography

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## Sod-type particle shock tube with Gaussian-convolution GSPH

ActualInutsuka-linear-overlap variablehGSPH approximation withfirstorderpair states, comparedwithdistinctstandardSPHcontrol. Periodictwointerfaces; centralwindowbeforeouterwaves. Not cubic/MUSCLpaperreproduction or plainSPH-pressure-star surrogate.

**Methods used**

- [Godunov SPH / GSPH](https://hrkoyama.github.io/numerical-methods-atlas/methods/gsph/?lang=en) (`gsph`)
- [SPH kernel reconstruction](https://hrkoyama.github.io/numerical-methods-atlas/methods/sph/?lang=en) (`sph`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/gsph-sod/?lang=en#gsph-sod-en-algorithm)

ActualInutsuka-linear-overlap variablehGSPH approximation withfirstorderpair states, comparedwithdistinctstandardSPHcontrol. Periodictwointerfaces; centralwindowbeforeouterwaves. Not cubic/MUSCLpaperreproduction or plainSPH-pressure-star surrogate.

- [Compressible Euler equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#euler-en) (`euler`)

Actual Gaussian linear-specific-volume GSPH overlap with symmetric variable h, independent pair Riemann solves and antisymmetric total-energy exchange; not substitution of star pressure into ordinary SPH. First-order reconstruction only, not the paper cubic/MUSCL implementation or a general accuracy claim.


**Problem figure**

![Sod-type particle shock tube with Gaussian-convolution GSPH: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/gsph-sod.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Sod shock tube](https://hrkoyama.github.io/numerical-methods-atlas/problems/sod/?lang=en) (`sod`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/sod/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/gsph-sod/?lang=en#gsph-sod-en-validation)

Separate analytic/reference errors, conservation, refinement, independent component qualification and deliberately wrong-formula controls.

- [Euler / Sod](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-euler-sod-en) (`euler-sod`; Related-model reference · Semi-analytic reference)

γ=1.4, primitive states (1,0,1)/(0.125,0,0.1), x0=0.5, [0,1] and t=0.2 match. Inspect point/conserved-cell-average sampling and error norms separately. Physical inputs match, but the card’s point samples and the saved computation’s finite-volume cell averages/discrete grid are different representations.

- [Sod-type particle shock tube with Gaussian-convolution GSPH](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-gsph-sod-en) (`gsph-sod`; Same-problem reference · Semi-analytic reference)

Bind the fixed-input formula, reference, figure and executable code. Actual Gaussian linear-specific-volume GSPH overlap with symmetric variable h, independent pair Riemann solves and antisymmetric total-energy exchange; not substitution of star pressure into ordinary SPH. First-order reconstruction only, not the paper cubic/MUSCL implementation or a general accuracy claim.
### Assumptions, units and boundaries

ActualInutsuka-linear-overlap variablehGSPH approximation withfirstorderpair states, comparedwithdistinctstandardSPHcontrol. Periodictwointerfaces; centralwindowbeforeouterwaves. Not cubic/MUSCLpaperreproduction or plainSPH-pressure-star surrogate.

**Editorial clarification**

Actual Gaussian linear-specific-volume GSPH overlap with symmetric variable h, independent pair Riemann solves and antisymmetric total-energy exchange; not substitution of star pressure into ordinary SPH. First-order reconstruction only, not the paper cubic/MUSCL implementation or a general accuracy claim.

### Adopted numerical method

ActualInutsuka-linear-overlap variablehGSPH approximation withfirstorderpair states, comparedwithdistinctstandardSPHcontrol. Periodictwointerfaces; centralwindowbeforeouterwaves. Not cubic/MUSCLpaperreproduction or plainSPH-pressure-star surrogate.

### References and validation

Separate analytic/reference errors, conservation, refinement, independent component qualification and deliberately wrong-formula controls.

### Limits

ActualInutsuka-linear-overlap variablehGSPH approximation withfirstorderpair states, comparedwithdistinctstandardSPHcontrol. Periodictwointerfaces; centralwindowbeforeouterwaves. Not cubic/MUSCLpaperreproduction or plainSPH-pressure-star surrogate.

### Stored measurements and decisions

```json
{
  "metrics": {
    "finest_GSPH": {
      "method": "gsph",
      "right_particles": 32,
      "rho_error": 0.03789937718353325,
      "pressure_error": 0.040752681798075875,
      "shock_error": 0.011271366170524794,
      "defect": [
        0.0,
        2.220446049250313e-16,
        0.0
      ],
      "h_change": 1.5560167029698944,
      "steps": 518,
      "h_residual": 9.994160761956033e-11,
      "Riemann_residual": 1.5300261058115439e-15
    },
    "pair_swap_force_residual": 0.0,
    "pair_swap_energy_residual": 1.1102230246251565e-16,
    "oracle_pressure_root": 0.30313017805063625,
    "oracle_root_diagnostics": {
      "iterations": 45,
      "log_bracket_width": 1.3078427230084344e-13,
      "wave_residual": -5.773159728050814e-14
    }
  },
  "checks": {
    "pair_swap_force": true,
    "pair_swap_energy": true,
    "conservation": true,
    "rho": true,
    "pressure": true,
    "refinement": true,
    "shock": true,
    "h_solve": true,
    "Riemann": true,
    "adaptive_h": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/gsph-sod/index.json

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/atlas-continuum-particle-controls-2026-11-25.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- Reformulation of Smoothed Particle Hydrodynamics with Riemann Solver. https://arxiv.org/pdf/astro-ph/0206401; review_level=selected-original-author-paper-sections-and-equations
- New Third-Order Finite Volume Unequal-Sized WENO Lagrangian Schemes for Solving Euler Equations. https://www.mdpi.com/2227-7390/11/23/4842; review_level=selected-publisher-fulltext-example-8
- Second Order Corner Coupled Upwind Transport Methods for Lagrangian Hydrodynamics. https://www.osti.gov/servlets/purl/15005665; review_level=secondary-bibliographic-identity-original-report-unread
- A standard test set for numerical approximations to the shallow water equations in spherical geometry. https://digital.library.unt.edu/ark:/67531/metadc1069483/; review_level=author-report-bibliography-and-abstract-original-formulas-unread
- Cascade interpolation for semi-Lagrangian advection over the sphere. https://www.image.ucar.edu/staff/rnair/qj99_sph.pdf; review_level=selected-author-hosted-formulas-and-publisher-bibliography

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## Uniform pressure and acoustics: particle-layout effects in SPH/GSPH

Regular/deterministicallyjitteredperiodicparticles, fixedhSPHcontrol vs adaptivehGSPH. Separateinitialkernelerror and fluidupdate, finiteamplitudeO(A²)linearizedreference remainder. No universalGSPHsuperiorityclaim.

**Methods used**

- [Godunov SPH / GSPH](https://hrkoyama.github.io/numerical-methods-atlas/methods/gsph/?lang=en) (`gsph`)
- [SPH kernel reconstruction](https://hrkoyama.github.io/numerical-methods-atlas/methods/sph/?lang=en) (`sph`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/sph-pressure-acoustics/?lang=en#sph-pressure-acoustics-en-algorithm)

Regular/deterministicallyjitteredperiodicparticles, fixedhSPHcontrol vs adaptivehGSPH. Separateinitialkernelerror and fluidupdate, finiteamplitudeO(A²)linearizedreference remainder. No universalGSPHsuperiorityclaim.

- [Compressible Euler equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#euler-en) (`euler`)

GSPH with 128 jittered particles at t=0.2. The initial kernel reconstruction error reaches 0.011834, exceeding the acoustic amplitude 0.001 and remaining visible in the left density profile; the right panel shows that initial error. Acceptance concerns the fundamental Fourier mode phase/amplitude and other fixed conservation controls, not pointwise high accuracy or general superiority.


**Problem figure**

![Uniform pressure and acoustics: particle-layout effects in SPH/GSPH: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/sph-pressure-acoustics.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Uniform pressure and acoustics: particle-layout effects in SPH/GSPH](https://hrkoyama.github.io/numerical-methods-atlas/problems/sph-pressure-acoustics/?lang=en) (`sph-pressure-acoustics`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/sph-pressure-acoustics/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/sph-pressure-acoustics/?lang=en#sph-pressure-acoustics-en-validation)

Separate analytic/reference errors, conservation, refinement, independent component qualification and deliberately wrong-formula controls.

- [Uniform pressure and acoustics: particle-layout effects in SPH/GSPH](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-sph-pressure-acoustics-en) (`sph-pressure-acoustics`; Same-problem reference · Analytic reference)

Bind the fixed-input formula, reference, figure and executable code. GSPH with 128 jittered particles at t=0.2. The initial kernel reconstruction error reaches 0.011834, exceeding the acoustic amplitude 0.001 and remaining visible in the left density profile; the right panel shows that initial error. Acceptance concerns the fundamental Fourier mode phase/amplitude and other fixed conservation controls, not pointwise high accuracy or general superiority.
### Assumptions, units and boundaries

Regular/deterministicallyjitteredperiodicparticles, fixedhSPHcontrol vs adaptivehGSPH. Separateinitialkernelerror and fluidupdate, finiteamplitudeO(A²)linearizedreference remainder. No universalGSPHsuperiorityclaim.

**Editorial clarification**

GSPH with 128 jittered particles at t=0.2. The initial kernel reconstruction error reaches 0.011834, exceeding the acoustic amplitude 0.001 and remaining visible in the left density profile; the right panel shows that initial error. Acceptance concerns the fundamental Fourier mode phase/amplitude and other fixed conservation controls, not pointwise high accuracy or general superiority.

### Adopted numerical method

Regular/deterministicallyjitteredperiodicparticles, fixedhSPHcontrol vs adaptivehGSPH. Separateinitialkernelerror and fluidupdate, finiteamplitudeO(A²)linearizedreference remainder. No universalGSPHsuperiorityclaim.

### References and validation

Separate analytic/reference errors, conservation, refinement, independent component qualification and deliberately wrong-formula controls.

### Limits

Regular/deterministicallyjitteredperiodicparticles, fixedhSPHcontrol vs adaptivehGSPH. Separateinitialkernelerror and fluidupdate, finiteamplitudeO(A²)linearizedreference remainder. No universalGSPHsuperiorityclaim.

### Stored measurements and decisions

```json
{
  "metrics": {
    "profiles": 16,
    "linearization_remainder_scale": 1e-06
  },
  "checks": {
    "regular_static_force": true,
    "jittered_static_velocity": true,
    "acoustic_phase": true,
    "acoustic_amplitude": true,
    "conservation": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/sph-pressure-acoustics/index.json

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/atlas-continuum-particle-controls-2026-11-25.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- Reformulation of Smoothed Particle Hydrodynamics with Riemann Solver. https://arxiv.org/pdf/astro-ph/0206401; review_level=selected-original-author-paper-sections-and-equations
- New Third-Order Finite Volume Unequal-Sized WENO Lagrangian Schemes for Solving Euler Equations. https://www.mdpi.com/2227-7390/11/23/4842; review_level=selected-publisher-fulltext-example-8
- Second Order Corner Coupled Upwind Transport Methods for Lagrangian Hydrodynamics. https://www.osti.gov/servlets/purl/15005665; review_level=secondary-bibliographic-identity-original-report-unread
- A standard test set for numerical approximations to the shallow water equations in spherical geometry. https://digital.library.unt.edu/ark:/67531/metadc1069483/; review_level=author-report-bibliography-and-abstract-original-formulas-unread
- Cascade interpolation for semi-Lagrangian advection over the sphere. https://www.image.ucar.edu/staff/rnair/qj99_sph.pdf; review_level=selected-author-hosted-formulas-and-publisher-bibliography

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
