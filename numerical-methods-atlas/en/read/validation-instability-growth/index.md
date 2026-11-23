# KH/RT initial growth and independent linear references

Compare actual small-amplitude nonlinear2D runs with separately derived continuous Fourier–Galerkin linear IVPs. Separate finite-time growth, spatial, temporal and amplitude effects.

These additional validation supplements are managed separately from the common 22-example registry. Receipts cover independent ZIP extraction, tests and every fixed input within each group. Changes of settings, methods or step sizes do not add independent physical problems.

## KH initial growth in a smooth periodic shear layer

Evolve the actual nonlinear2D vorticity PDE and compare finite-time growth and spatial errors with an independent continuous Fourier–Galerkin linear IVP.

**Methods used**

- [Centered spatial difference](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en) (`centered-difference`)
- [Heun / SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en) (`heun`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/kh-initial-growth/?lang=en#kh-initial-growth-en-algorithm)

Advance point-sampled perturbations using centered shared-face conservative fluxes and Heun; invert the five-point Poisson symbol by FFT. Centered derivatives define divergence-free velocity. Analytic base subtraction avoids a discretization imbalance larger than the small perturbation.

$$
-\Delta\psi=\omega,\qquad (u,v)=(\partial_y\psi,-\partial_x\psi)
$$

$$
U(y)=\tanh(\sin y/\delta),\quad \omega_t+U\omega_x+U^{\prime\prime}\psi_x+\mathbf{u}\cdot\nabla\omega=\nu\Delta\omega
$$

$$
\sigma_T=\frac{1}{T}\log\frac{A(T)}{A(0)},\qquad \dot{\widehat{\mathbf{q}}}=L_K\widehat{\mathbf{q}}
$$

- [Forced vorticity about a maintained shear layer](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#forced-vorticity-en) (`forced-vorticity`)

Periodic[0,2pi]², layer width.25, nu=kappa=.005, epsilon1e-5 and32²/64²/128² grids. Explicit forcing maintains the base. U=tanh(sin y/delta),T1.


**Problem figure**

![KH initial growth in a smooth periodic shear layer: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/results/kh-initial-growth.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[KH initial growth in a smooth periodic shear layer](https://hrkoyama.github.io/numerical-methods-atlas/problems/kh-initial-growth/?lang=en) (`kh-initial-growth`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/kh-initial-growth/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/kh-initial-growth/?lang=en#kh-initial-growth-en-validation)

Freeze22pytest tests,74case gates and10nonlinear evolutions. QualifyK24/40/56references; separately check three-grid field errors/orders, five-time growth,64²halved-step/halved-amplitude probes, Poisson residual, divergence and means.

- [KH initial growth: independent linear Fourier-Galerkin reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-kh-initial-growth-en) (`kh-initial-growth`; Same-problem reference · Finite-grid numerical reference)

Small-amplitude fixed educational cases. The independent reference changes spatial representation but linearizes the PDE; it is not a second nonlinear engine. No sharp-interface infinite-domain dispersion, original compressible McNally inputs, late roll-up or RT turbulence claim. Figures explicitly normalize computed perturbations by epsilon.
### Assumptions, units and boundaries

Periodic[0,2pi]², layer width.25, nu=kappa=.005, epsilon1e-5 and32²/64²/128² grids. Explicit forcing maintains the base. U=tanh(sin y/delta),T1.

**Editorial clarification**

Small-amplitude fixed educational cases. The independent reference changes spatial representation but linearizes the PDE; it is not a second nonlinear engine. No sharp-interface infinite-domain dispersion, original compressible McNally inputs, late roll-up or RT turbulence claim. Figures explicitly normalize computed perturbations by epsilon.

### Adopted numerical method

Advance point-sampled perturbations using centered shared-face conservative fluxes and Heun; invert the five-point Poisson symbol by FFT. Centered derivatives define divergence-free velocity. Analytic base subtraction avoids a discretization imbalance larger than the small perturbation.

$$
-\Delta\psi=\omega,\qquad (u,v)=(\partial_y\psi,-\partial_x\psi)
$$

$$
U(y)=\tanh(\sin y/\delta),\quad \omega_t+U\omega_x+U^{\prime\prime}\psi_x+\mathbf{u}\cdot\nabla\omega=\nu\Delta\omega
$$

$$
\sigma_T=\frac{1}{T}\log\frac{A(T)}{A(0)},\qquad \dot{\widehat{\mathbf{q}}}=L_K\widehat{\mathbf{q}}
$$

### References and validation

Freeze22pytest tests,74case gates and10nonlinear evolutions. QualifyK24/40/56references; separately check three-grid field errors/orders, five-time growth,64²halved-step/halved-amplitude probes, Poisson residual, divergence and means.

### Limits

Small-amplitude fixed educational cases. The independent reference changes spatial representation but linearizes the PDE; it is not a second nonlinear engine. No sharp-interface infinite-domain dispersion, original compressible McNally inputs, late roll-up or RT turbulence claim. Figures explicitly normalize computed perturbations by epsilon.

### Stored measurements and decisions

```json
{
  "metrics": {
    "spatial_orders": [
      2.2589498509059927,
      2.031111897437912
    ],
    "finest_relative_field_error": 0.00425645160443949,
    "finite_window_growth_rate": 0.39492545403491336,
    "reference_finite_window_growth_rate": 0.3978101440217111,
    "finest_growth_factor": 1.4842735401931764,
    "maximum_growth_curve_error": 0.0028805332665482204,
    "time_contamination_fraction": 0.00045118656465393327,
    "amplitude_scaled_difference": 6.588689979924076e-06,
    "linear_operator_maximum_real_eigenvalue": 0.5858641640461411
  },
  "checks": {
    "reference_state_sensitivity": true,
    "reference_growth_sensitivity": true,
    "reference_positive_eigen_growth": true,
    "n32_finite": true,
    "n32_divergence": true,
    "n32_poisson": true,
    "n32_mean_omega": true,
    "n32_mean_theta": true,
    "n64_finite": true,
    "n64_divergence": true,
    "n64_poisson": true,
    "n64_mean_omega": true,
    "n64_mean_theta": true,
    "n128_finite": true,
    "n128_divergence": true,
    "n128_poisson": true,
    "n128_mean_omega": true,
    "n128_mean_theta": true,
    "time-half_finite": true,
    "time-half_divergence": true,
    "time-half_poisson": true,
    "time-half_mean_omega": true,
    "time-half_mean_theta": true,
    "epsilon-half_finite": true,
    "epsilon-half_divergence": true,
    "epsilon-half_poisson": true,
    "epsilon-half_mean_omega": true,
    "epsilon-half_mean_theta": true,
    "spatial_decrease_1": true,
    "spatial_decrease_2": true,
    "minimum_spatial_order": true,
    "finest_field_error": true,
    "growth_curve": true,
    "finite_window_growth_rate": true,
    "observable_growth": true,
    "time_contamination": true,
    "amplitude_linearity": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/kh-initial-growth/index.json

![Saved actual2D perturbation vorticity normalized by epsilon; color scale and linear-reference growth are explicit.](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/results/kh-initial-growth-preview.png)

Saved actual2D perturbation vorticity normalized by epsilon; color scale and linear-reference growth are explicit.

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/atlas-instability-growth-2026-11-23-r2.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group.

### Sources and review scope

- Colin P. McNally, Wladimir Lyra and Jean-Claude Passy (2012). A Well-Posed Kelvin-Helmholtz Instability Test and Comparison. https://arxiv.org/abs/1111.1764; review_level=primary-selected-original-pdf-text
  Selected original methodology read; our incompressible forced inputs differ from its compressible benchmark.

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## RT initial growth in smooth Boussinesq double layers

Advance the actual2D Boussinesq vorticity/active-buoyancy system and compare smooth unstable-layer growth with a separately derived linear IVP.

**Methods used**

- [Centered spatial difference](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en) (`centered-difference`)
- [Heun / SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en) (`heun`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/rt-initial-growth/?lang=en#rt-initial-growth-en-algorithm)

Advance point-sampled perturbations using centered shared-face conservative fluxes and Heun; invert the five-point Poisson symbol by FFT. Centered derivatives define divergence-free velocity. Analytic base subtraction avoids a discretization imbalance larger than the small perturbation.

$$
-\Delta\psi=\omega,\qquad (u,v)=(\partial_y\psi,-\partial_x\psi)
$$

$$
b=b_0(y)+\theta,\quad \omega_t+\mathbf{u}\cdot\nabla\omega=\nu\Delta\omega+\theta_x,\quad \theta_t+\mathbf{u}\cdot\nabla\theta+v b_0^{\prime}=\kappa\Delta\theta
$$

$$
\sigma_T=\frac{1}{T}\log\frac{A(T)}{A(0)},\qquad \dot{\widehat{\mathbf{q}}}=L_K\widehat{\mathbf{q}}
$$

- [Boussinesq vorticity with active buoyancy](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#boussinesq-buoyancy-en) (`boussinesq-buoyancy`)

Periodic[0,2pi]², layer width.25, nu=kappa=.005, epsilon1e-5 and32²/64²/128² grids. Explicit forcing maintains the base. g1,b0=.02tanh(sin y/delta),rho/rho0=1-b/g,T2. Density enters buoyancy only; this is not variable-density Euler.


**Problem figure**

![RT initial growth in smooth Boussinesq double layers: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/results/rt-initial-growth.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[RT initial growth in smooth Boussinesq double layers](https://hrkoyama.github.io/numerical-methods-atlas/problems/rt-initial-growth/?lang=en) (`rt-initial-growth`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/rt-initial-growth/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/rt-initial-growth/?lang=en#rt-initial-growth-en-validation)

Freeze22pytest tests,74case gates and10nonlinear evolutions. QualifyK24/40/56references; separately check three-grid field errors/orders, five-time growth,64²halved-step/halved-amplitude probes, Poisson residual, divergence and means.

- [RT initial growth: linear Boussinesq double-layer IVP reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-rt-initial-growth-en) (`rt-initial-growth`; Same-problem reference · Finite-grid numerical reference)

Small-amplitude fixed educational cases. The independent reference changes spatial representation but linearizes the PDE; it is not a second nonlinear engine. No sharp-interface infinite-domain dispersion, original compressible McNally inputs, late roll-up or RT turbulence claim. Figures explicitly normalize computed perturbations by epsilon.
### Assumptions, units and boundaries

Periodic[0,2pi]², layer width.25, nu=kappa=.005, epsilon1e-5 and32²/64²/128² grids. Explicit forcing maintains the base. g1,b0=.02tanh(sin y/delta),rho/rho0=1-b/g,T2. Density enters buoyancy only; this is not variable-density Euler.

**Editorial clarification**

Small-amplitude fixed educational cases. The independent reference changes spatial representation but linearizes the PDE; it is not a second nonlinear engine. No sharp-interface infinite-domain dispersion, original compressible McNally inputs, late roll-up or RT turbulence claim. Figures explicitly normalize computed perturbations by epsilon.

### Adopted numerical method

Advance point-sampled perturbations using centered shared-face conservative fluxes and Heun; invert the five-point Poisson symbol by FFT. Centered derivatives define divergence-free velocity. Analytic base subtraction avoids a discretization imbalance larger than the small perturbation.

$$
-\Delta\psi=\omega,\qquad (u,v)=(\partial_y\psi,-\partial_x\psi)
$$

$$
b=b_0(y)+\theta,\quad \omega_t+\mathbf{u}\cdot\nabla\omega=\nu\Delta\omega+\theta_x,\quad \theta_t+\mathbf{u}\cdot\nabla\theta+v b_0^{\prime}=\kappa\Delta\theta
$$

$$
\sigma_T=\frac{1}{T}\log\frac{A(T)}{A(0)},\qquad \dot{\widehat{\mathbf{q}}}=L_K\widehat{\mathbf{q}}
$$

### References and validation

Freeze22pytest tests,74case gates and10nonlinear evolutions. QualifyK24/40/56references; separately check three-grid field errors/orders, five-time growth,64²halved-step/halved-amplitude probes, Poisson residual, divergence and means.

### Limits

Small-amplitude fixed educational cases. The independent reference changes spatial representation but linearizes the PDE; it is not a second nonlinear engine. No sharp-interface infinite-domain dispersion, original compressible McNally inputs, late roll-up or RT turbulence claim. Figures explicitly normalize computed perturbations by epsilon.

### Stored measurements and decisions

```json
{
  "metrics": {
    "spatial_orders": [
      1.9961801582972816,
      2.001279583653318
    ],
    "finest_relative_field_error": 0.0006046946397847546,
    "finite_window_growth_rate": 0.005928114552970485,
    "reference_finite_window_growth_rate": 0.005934243782555812,
    "finest_growth_factor": 1.0119267927875564,
    "maximum_growth_curve_error": 1.2258384036050356e-05,
    "time_contamination_fraction": 0.0026807715949025237,
    "amplitude_scaled_difference": 6.607861425190432e-06,
    "linear_operator_maximum_real_eigenvalue": 0.11294010706315265
  },
  "checks": {
    "reference_state_sensitivity": true,
    "reference_growth_sensitivity": true,
    "reference_positive_eigen_growth": true,
    "n32_finite": true,
    "n32_divergence": true,
    "n32_poisson": true,
    "n32_mean_omega": true,
    "n32_mean_theta": true,
    "n64_finite": true,
    "n64_divergence": true,
    "n64_poisson": true,
    "n64_mean_omega": true,
    "n64_mean_theta": true,
    "n128_finite": true,
    "n128_divergence": true,
    "n128_poisson": true,
    "n128_mean_omega": true,
    "n128_mean_theta": true,
    "time-half_finite": true,
    "time-half_divergence": true,
    "time-half_poisson": true,
    "time-half_mean_omega": true,
    "time-half_mean_theta": true,
    "epsilon-half_finite": true,
    "epsilon-half_divergence": true,
    "epsilon-half_poisson": true,
    "epsilon-half_mean_omega": true,
    "epsilon-half_mean_theta": true,
    "spatial_decrease_1": true,
    "spatial_decrease_2": true,
    "minimum_spatial_order": true,
    "finest_field_error": true,
    "growth_curve": true,
    "finite_window_growth_rate": true,
    "observable_growth": true,
    "time_contamination": true,
    "amplitude_linearity": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/rt-initial-growth/index.json

![Saved actual2D buoyancy perturbation normalized by epsilon; an early smooth-layer displacement, not turbulent mixing.](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/results/rt-initial-growth-preview.png)

Saved actual2D buoyancy perturbation normalized by epsilon; an early smooth-layer displacement, not turbulent mixing.

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/atlas-instability-growth-2026-11-23-r2.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group.

### Sources and review scope

- Antonio Celani, Andrea Mazzino and Lara Vozella (2006). Rayleigh–Taylor turbulence in two dimensions. https://arxiv.org/abs/nlin/0510067; review_level=primary-selected-original-pdf-text
  Original Boussinesq equations and periodic setup read; our smooth maintained layers and linear reference are constructed here.

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
