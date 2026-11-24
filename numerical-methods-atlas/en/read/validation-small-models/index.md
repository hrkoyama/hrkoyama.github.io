# Small learned models and independently checked biological ODEs

Study a Poisson PINN, periodic-heat FNO and enzyme, predator–prey and SEIR systems under fixed budgets. Original learning and approximation goals remain separate from reproduction checks.

These additional validation supplements are managed separately from the common 22-example registry. Receipts cover independent ZIP extraction, tests and every fixed input within each group. Changes of settings, methods or step sizes do not add independent physical problems.

## Poisson PINN: independent grid error

Compare a 49-parameter PINN for three fixed seeds with analytic and finite-difference solutions.

**Methods used**

- [PINNs and neural operators](https://hrkoyama.github.io/numerical-methods-atlas/methods/pinn-operators/?lang=en) (`pinn-operators`)
- [Thomas tridiagonal elimination](https://hrkoyama.github.io/numerical-methods-atlas/methods/thomas/?lang=en) (`thomas`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/pinn-poisson/?lang=en#pinn-poisson-en-algorithm)

Train a hard-boundary tanh ansatz with trust-region reflective least squares and an analytic parameter Jacobian. Retain every returned model under the fixed budget. Also solve second-order finite differences with 31, 63 and 127 unknowns using the Thomas algorithm.

$$
-u_{xx}=\pi^2\sin(\pi x),\quad 0<x<1,\quad u(0)=u(1)=0
$$

$$
u_\theta(x)=x(1-x)\left[b_0+\sum_{j=1}^{16}a_j\tanh(w_jx+b_j)\right]
$$

$$
r_i=\frac{-u_{\theta,xx}(x_i)-\pi^2\sin(\pi x_i)}{\pi^2},\quad L=\frac1{64}\sum_{i=1}^{64}r_i^2
$$

- [Poisson / Laplace equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#poisson-laplace-en) (`poisson-laplace`)

Solve dimensionless −uₓₓ=π² sin(πx) on [0,1] with zero Dirichlet data. Use sixteen hidden units, 49 real parameters, seeds 8401–8403, 64 training points and 257 separate evaluation points.


**Problem figure**

![Poisson PINN: independent grid error: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/pinn-poisson.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[1D Poisson / smooth Dirichlet manufactured solutions](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-dirichlet/?lang=en) (`poisson-1d-dirichlet`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-dirichlet/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/pinn-poisson/?lang=en#pinn-poisson-en-validation)

Independently qualify all 49 residual-Jacobian columns, loss-gradient coordinates and spatial derivatives. Save off-training solution error against sin(πx), PDE residual, boundary error and finite-difference error separately. Preserve actual convergence and accuracy decisions; a normal budget return is not convergence.

- [Poisson / manufactured sine](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-poisson-manufactured-en) (`poisson-manufactured`; Related-model reference · Manufactured solution)

It matches the single-sine common fixed input, but saved comparisons also contain composite-sine manufactured forcing. Zero Dirichlet boundaries do not make all sources identical.

- [Poisson PINN: independent grid error](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-pinn-poisson-en) (`pinn-poisson`; Related-model reference · Manufactured solution)

This fixed-budget study covers one smooth Poisson problem and three seeds. A small training loss does not establish independent-point accuracy or general PINN training success. Unmet goals remain visible.
### Assumptions, units and boundaries

Solve dimensionless −uₓₓ=π² sin(πx) on [0,1] with zero Dirichlet data. Use sixteen hidden units, 49 real parameters, seeds 8401–8403, 64 training points and 257 separate evaluation points.

**Editorial clarification**

This fixed-budget study covers one smooth Poisson problem and three seeds. A small training loss does not establish independent-point accuracy or general PINN training success. Unmet goals remain visible.

### Adopted numerical method

Train a hard-boundary tanh ansatz with trust-region reflective least squares and an analytic parameter Jacobian. Retain every returned model under the fixed budget. Also solve second-order finite differences with 31, 63 and 127 unknowns using the Thomas algorithm.

$$
-u_{xx}=\pi^2\sin(\pi x),\quad 0<x<1,\quad u(0)=u(1)=0
$$

$$
u_\theta(x)=x(1-x)\left[b_0+\sum_{j=1}^{16}a_j\tanh(w_jx+b_j)\right]
$$

$$
r_i=\frac{-u_{\theta,xx}(x_i)-\pi^2\sin(\pi x_i)}{\pi^2},\quad L=\frac1{64}\sum_{i=1}^{64}r_i^2
$$

### References and validation

Independently qualify all 49 residual-Jacobian columns, loss-gradient coordinates and spatial derivatives. Save off-training solution error against sin(πx), PDE residual, boundary error and finite-difference error separately. Preserve actual convergence and accuracy decisions; a normal budget return is not convergence.

### Limits

This fixed-budget study covers one smooth Poisson problem and three seeds. A small training loss does not establish independent-point accuracy or general PINN training success. Unmet goals remain visible.

### Original numerical targets and unmet outcomes

Passing reproduction/reporting verification does not mean that all original accuracy goals were met. Original decisions are retained.

```json
{
  "original_target_results": {
    "seed-8401:optimizer-converged": false,
    "seed-8401:solution_Linf": true,
    "seed-8401:PDE_normalized_RMS": true,
    "seed-8401:boundary_Linf": true,
    "seed-8402:optimizer-converged": false,
    "seed-8402:solution_Linf": true,
    "seed-8402:PDE_normalized_RMS": true,
    "seed-8402:boundary_Linf": true,
    "seed-8403:optimizer-converged": false,
    "seed-8403:solution_Linf": true,
    "seed-8403:PDE_normalized_RMS": true,
    "seed-8403:boundary_Linf": true,
    "fd-31:solution_Linf": true,
    "fd-63:solution_Linf": true,
    "fd-127:solution_Linf": true
  },
  "original_target_summary": {
    "met": 12,
    "total": 15,
    "all_met": false,
    "acceptance_sha256": "b468e78459cf81bda6a32cade0051f6615b44def256c66308ae7acc82ff516ce"
  }
}
```

### Stored measurements and decisions

```json
{
  "metrics": {
    "training_seeds": 3,
    "parameters": 49,
    "independent_grid_points": 257,
    "FD_runs": 3
  },
  "checks": {
    "seed-8401:finite-shape": true,
    "seed-8401:optimizer-return-status": true,
    "seed-8401:actual-work": true,
    "seed-8402:finite-shape": true,
    "seed-8402:optimizer-return-status": true,
    "seed-8402:actual-work": true,
    "seed-8403:finite-shape": true,
    "seed-8403:optimizer-return-status": true,
    "seed-8403:actual-work": true,
    "fd-31:true-residual": true,
    "fd-63:true-residual": true,
    "fd-127:true-residual": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/pinn-poisson/index.json

![Compare a 49-parameter PINN for three fixed seeds with analytic and finite-difference solutions. This figure reads saved data only.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/pinn-poisson-preview.png)

Compare a 49-parameter PINN for three fixed seeds with analytic and finite-difference solutions. This figure reads saved data only.

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/atlas-small-models-2026-11-25.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- Physics Informed Deep Learning (Part I): Data-driven Solutions of Nonlinear Partial Differential Equations [accessed 2026-11-24]. https://arxiv.org/pdf/1711.10561; review_level=selected-primary-body
Extracted PDF text selected pp.4–6, §2 continuous-time residual, Eq(2)–(4), Burgers setup and loss/optimizer discussion; not all 22 pages and not visual PDF audit.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## Tiny FNO on held-out heat problems

Evaluate the same learned weights on 32/64-point grids, held-out functions and separate OOD inputs.

**Methods used**

- [PINNs and neural operators](https://hrkoyama.github.io/numerical-methods-atlas/methods/pinn-operators/?lang=en) (`pinn-operators`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/fno-periodic-heat/?lang=en#fno-periodic-heat-en-algorithm)

Lift (u₀,ν) to width two and apply two blocks containing a local linear map, real DC and complex Fourier modes 1–4, then tanh. Train with a fixed L-BFGS-B budget and evaluate the same weights at N=32 and 64. Nonlinear terms are evaluated on each native grid without dealiasing.

$$
u_t=\nu u_{xx},\quad x\in[0,2\pi),\quad u(x+2\pi,t)=u(x,t),\quad T=\tfrac14
$$

$$
\widehat u_k(T)=e^{-\nu k^2T}\widehat u_k(0)
$$

$$
v^{\ell+1}=\tanh\!\left(W_\ell v^\ell+b_\ell+\mathcal F_N^{-1}(R_\ell\mathcal F_Nv^\ell)\right),\quad \ell=0,1
$$

$$
\mathrm{relative\ error}=\frac{\operatorname{RMS}(u_\theta-u_{\rm ref})}{\operatorname{RMS}(u_{\rm ref})}\quad\text{only if }\operatorname{RMS}(u_{\rm ref})>10^{-12}
$$

- [Heat / diffusion equation](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#heat-en) (`heat`)

Use periodic heat flow uₜ=νuₓₓ on [0,2π) to T=0.25. Split 46 whole problems into 24 training, 6 validation, 8 held-out ID, 4 viscosity-OOD and 4 spectrum-OOD problems. Use two fixed seeds and 93 real parameters.


**Problem figure**

![Tiny FNO on held-out heat problems: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/fno-periodic-heat.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Periodic Fourier-mode heat decay](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-periodic/?lang=en) (`heat-periodic`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-periodic/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/fno-periodic-heat/?lang=en#fno-periodic-heat-en-validation)

Qualify all 93 real loss-gradient coordinates at two fixed finite-difference widths and compare Fourier blocks with direct DFT sums. Separate analytic heat-mode errors, grid-restriction differences and ID/OOD diagnostics. Relative error is NA when reference RMS≤10⁻¹²; zero and near-zero controls retain absolute errors.

- [Heat / Fourier-mode decay](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-sine-heat-en) (`sine-heat`; Related-model reference · Analytic reference)

The saved gallery matches periodic [0,1], 1+0.25sin(2πx), ν=0.02 and final time one; this does not assert a match to separate-frequency code checks. Physical inputs match, but the card’s point samples and the saved computation’s finite-volume cell averages/discrete grid are different representations.

- [Tiny FNO on held-out heat problems](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-fno-periodic-heat-en) (`fno-periodic-heat`; Related-model reference · Analytic reference)

This comparison concerns a fixed tiny discrete operator, without arbitrary-resolution, distributional or OOD guarantees. The N=64-to-32 discrepancy includes nonlinear aliasing and is not a continuum discretization error. Optimizer convergence is distinct from normal budget termination.
### Assumptions, units and boundaries

Use periodic heat flow uₜ=νuₓₓ on [0,2π) to T=0.25. Split 46 whole problems into 24 training, 6 validation, 8 held-out ID, 4 viscosity-OOD and 4 spectrum-OOD problems. Use two fixed seeds and 93 real parameters.

**Editorial clarification**

This comparison concerns a fixed tiny discrete operator, without arbitrary-resolution, distributional or OOD guarantees. The N=64-to-32 discrepancy includes nonlinear aliasing and is not a continuum discretization error. Optimizer convergence is distinct from normal budget termination. The old heat primary remains. This [0,2pi) whole-problem family, diffusivities and final time are separate fixed inputs.

### Adopted numerical method

Lift (u₀,ν) to width two and apply two blocks containing a local linear map, real DC and complex Fourier modes 1–4, then tanh. Train with a fixed L-BFGS-B budget and evaluate the same weights at N=32 and 64. Nonlinear terms are evaluated on each native grid without dealiasing.

$$
u_t=\nu u_{xx},\quad x\in[0,2\pi),\quad u(x+2\pi,t)=u(x,t),\quad T=\tfrac14
$$

$$
\widehat u_k(T)=e^{-\nu k^2T}\widehat u_k(0)
$$

$$
v^{\ell+1}=\tanh\!\left(W_\ell v^\ell+b_\ell+\mathcal F_N^{-1}(R_\ell\mathcal F_Nv^\ell)\right),\quad \ell=0,1
$$

$$
\mathrm{relative\ error}=\frac{\operatorname{RMS}(u_\theta-u_{\rm ref})}{\operatorname{RMS}(u_{\rm ref})}\quad\text{only if }\operatorname{RMS}(u_{\rm ref})>10^{-12}
$$

### References and validation

Qualify all 93 real loss-gradient coordinates at two fixed finite-difference widths and compare Fourier blocks with direct DFT sums. Separate analytic heat-mode errors, grid-restriction differences and ID/OOD diagnostics. Relative error is NA when reference RMS≤10⁻¹²; zero and near-zero controls retain absolute errors.

### Limits

This comparison concerns a fixed tiny discrete operator, without arbitrary-resolution, distributional or OOD guarantees. The N=64-to-32 discrepancy includes nonlinear aliasing and is not a continuum discretization error. Optimizer convergence is distinct from normal budget termination.

### Original numerical targets and unmet outcomes

Passing reproduction/reporting verification does not mean that all original accuracy goals were met. Original decisions are retained.

```json
{
  "original_target_results": {
    "seed-8501:optimizer-converged": false,
    "seed-8501:ID-N32-relative": true,
    "seed-8501:ID-N64-relative": true,
    "seed-8501:norm-control-absolute": true,
    "seed-8502:optimizer-converged": false,
    "seed-8502:ID-N32-relative": true,
    "seed-8502:ID-N64-relative": true,
    "seed-8502:norm-control-absolute": true
  },
  "original_target_summary": {
    "met": 6,
    "total": 8,
    "all_met": false,
    "acceptance_sha256": "b468e78459cf81bda6a32cade0051f6615b44def256c66308ae7acc82ff516ce"
  }
}
```

### Stored measurements and decisions

```json
{
  "metrics": {
    "models": 2,
    "parameters_per_model": 93,
    "whole_problem_IDs": 46,
    "prediction_rows": 116,
    "nonlinear_dealiasing": "none",
    "restriction_discrepancy_scope": "Native-grid nonlinear/alias sensitivity, not continuum error"
  },
  "checks": {
    "seed-8501:finite-parameters": true,
    "seed-8501:optimizer-return-status": true,
    "seed-8501:actual-work": true,
    "seed-8501:relative-NA": true,
    "seed-8502:finite-parameters": true,
    "seed-8502:optimizer-return-status": true,
    "seed-8502:actual-work": true,
    "seed-8502:relative-NA": true,
    "disjoint-whole-problem-IDs": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/fno-periodic-heat/index.json

![Evaluate the same learned weights on 32/64-point grids, held-out functions and separate OOD inputs. This figure reads saved data only.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/fno-periodic-heat-preview.png)

Evaluate the same learned weights on 32/64-point grids, held-out functions and separate OOD inputs. This figure reads saved data only.

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/atlas-small-models-2026-11-25.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- Fourier Neural Operator for Parametric Partial Differential Equations [accessed 2026-11-24]. https://arxiv.org/html/2010.08895v3; review_level=selected-primary-body
Selected HTML §2 learning operators; §3 Eq(2); §4 Eq(4)–(5), FFT/truncation/reality; §5 setup and §5.1 Burgers. PDF header/edition only; not full paper or appendix audit.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## Enzyme conservation and QSSA

Separate the initial layer, integration error and QSSA modeling error in a four-state enzyme mechanism.

**Methods used**

- [L-stable SDIRK2](https://hrkoyama.github.io/numerical-methods-atlas/methods/sdirk2/?lang=en) (`sdirk2`)
- [Adaptive SDIRK2 / step doubling](https://hrkoyama.github.io/numerical-methods-atlas/methods/step-doubling/?lang=en) (`step-doubling`)
- [Armijo-damped Newton](https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=en) (`newton`)
- [Classical RK4](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=en) (`rk4`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/enzyme-qssa/?lang=en#enzyme-qssa-en-algorithm)

Integrate all four states with SDIRK2 step doubling, using the same weighted L∞ residual for Newton convergence and Armijo backtracking. Evolve the reduced Michaelis–Menten equation separately with RK4 in θ, keeping integration error distinct from model-reduction error.

$$
\begin{aligned}\dot S&=-10ES+C,&\dot C&=10ES-2C,\\\dot E&=-10ES+2C,&\dot P&=C.\end{aligned}
$$

$$
E+C=E_0,\quad S+C+P=1,\quad K_m=\frac{k_{-1}+k_2}{k_1}=0.2
$$

$$
\theta=E_0t,\quad \varepsilon=\frac{E_0}{K_m+S_0}\in\left\{\frac1{120},\frac1{600}\right\}
$$

$$
\frac{dS_{\rm MM}}{d\theta}=-\frac{S_{\rm MM}}{0.2+S_{\rm MM}},\quad S_{\rm MM}+0.2\log S_{\rm MM}=1-\theta
$$

- [Michaelis–Menten and full enzyme kinetics](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-enzyme-en) (`bio-enzyme`)

Use the closed dimensionless reaction E+S⇌C→E+P with k₁=10, k₋₁=k₂=1, S₀=1, C₀=P₀=0 and E₀=0.01 or 0.002. Then Kₘ=0.2, ε=E₀/(Kₘ+S₀)=1/120 or 1/600, and θ=E₀t ranges from 0 to 0.5.


**Problem figure**

![Enzyme conservation and QSSA: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/enzyme-qssa.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Enzyme conservation and QSSA](https://hrkoyama.github.io/numerical-methods-atlas/problems/enzyme-qssa/?lang=en) (`enzyme-qssa`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/enzyme-qssa/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/enzyme-qssa/?lang=en#enzyme-qssa-en-validation)

Compare with independent full-system Radau/BDF references and an implicit scalar identity for the reduced equation. Check E+C=E₀, S+C+P=1, positivity and actual acceptance, rejection and Newton work. Retain both all-time errors including the initial layer and errors on the declared θ≥0.02 window.

- [Enzyme conservation and QSSA](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-enzyme-qssa-en) (`enzyme-qssa`; Same-problem reference · Finite-grid numerical reference)

These two small-ε fixed-rate examples are educational. ε is a scale ratio, not itself a certified QSSA error bound. The θ≥0.02 window is not a proof that the initial layer has ended, and the calculation is not an in-vivo prediction.
### Assumptions, units and boundaries

Use the closed dimensionless reaction E+S⇌C→E+P with k₁=10, k₋₁=k₂=1, S₀=1, C₀=P₀=0 and E₀=0.01 or 0.002. Then Kₘ=0.2, ε=E₀/(Kₘ+S₀)=1/120 or 1/600, and θ=E₀t ranges from 0 to 0.5.

**Editorial clarification**

These two small-ε fixed-rate examples are educational. ε is a scale ratio, not itself a certified QSSA error bound. The θ≥0.02 window is not a proof that the initial layer has ended, and the calculation is not an in-vivo prediction. Time, concentrations and populations do not define a spatial dimension. The rates are educational, not disease or experimental predictions.

### Adopted numerical method

Integrate all four states with SDIRK2 step doubling, using the same weighted L∞ residual for Newton convergence and Armijo backtracking. Evolve the reduced Michaelis–Menten equation separately with RK4 in θ, keeping integration error distinct from model-reduction error.

$$
\begin{aligned}\dot S&=-10ES+C,&\dot C&=10ES-2C,\\\dot E&=-10ES+2C,&\dot P&=C.\end{aligned}
$$

$$
E+C=E_0,\quad S+C+P=1,\quad K_m=\frac{k_{-1}+k_2}{k_1}=0.2
$$

$$
\theta=E_0t,\quad \varepsilon=\frac{E_0}{K_m+S_0}\in\left\{\frac1{120},\frac1{600}\right\}
$$

$$
\frac{dS_{\rm MM}}{d\theta}=-\frac{S_{\rm MM}}{0.2+S_{\rm MM}},\quad S_{\rm MM}+0.2\log S_{\rm MM}=1-\theta
$$

### References and validation

Compare with independent full-system Radau/BDF references and an implicit scalar identity for the reduced equation. Check E+C=E₀, S+C+P=1, positivity and actual acceptance, rejection and Newton work. Retain both all-time errors including the initial layer and errors on the declared θ≥0.02 window.

### Limits

These two small-ε fixed-rate examples are educational. ε is a scale ratio, not itself a certified QSSA error bound. The θ≥0.02 window is not a proof that the initial layer has ended, and the calculation is not an in-vivo prediction.

### Original numerical targets and unmet outcomes

Passing reproduction/reporting verification does not mean that all original accuracy goals were met. Original decisions are retained.

```json
{
  "original_target_results": {
    "enzyme-01-r1e-06:integration": true,
    "enzyme-01-r1e-06:mass": true,
    "enzyme-01-r1e-06:negative-part": true,
    "enzyme-01-r1e-06:QSSA-model": true,
    "enzyme-01-r1e-08:integration": true,
    "enzyme-01-r1e-08:mass": true,
    "enzyme-01-r1e-08:negative-part": true,
    "enzyme-01-r1e-08:QSSA-model": true,
    "enzyme-002-r1e-06:integration": true,
    "enzyme-002-r1e-06:mass": true,
    "enzyme-002-r1e-06:negative-part": true,
    "enzyme-002-r1e-06:QSSA-model": true,
    "enzyme-002-r1e-08:integration": true,
    "enzyme-002-r1e-08:mass": true,
    "enzyme-002-r1e-08:negative-part": true,
    "enzyme-002-r1e-08:QSSA-model": true
  },
  "original_target_summary": {
    "met": 16,
    "total": 16,
    "all_met": true,
    "acceptance_sha256": "b468e78459cf81bda6a32cade0051f6615b44def256c66308ae7acc82ff516ce"
  }
}
```

### Stored measurements and decisions

```json
{
  "metrics": {
    "actual_primary_records": 6,
    "reference_role": "Qualified Radau/BDF full ODE; reduction/linearization errors are distinct modeling diagnostics"
  },
  "checks": {
    "enzyme-01-r1e-06:completed-work": true,
    "enzyme-01-r1e-06:finite": true,
    "enzyme-01-r1e-08:completed-work": true,
    "enzyme-01-r1e-08:finite": true,
    "enzyme-002-r1e-06:completed-work": true,
    "enzyme-002-r1e-06:finite": true,
    "enzyme-002-r1e-08:completed-work": true,
    "enzyme-002-r1e-08:finite": true,
    "mm-200:finite": true,
    "mm-400:finite": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/enzyme-qssa/index.json

![Separate the initial layer, integration error and QSSA modeling error in a four-state enzyme mechanism. This figure reads saved data only.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/enzyme-qssa-preview.png)

Separate the initial layer, integration error and QSSA modeling error in a four-state enzyme mechanism. This figure reads saved data only.

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/atlas-small-models-2026-11-25.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- Rigorous estimates for the quasi-steady state approximation of the Michaelis–Menten reaction mechanism at low enzyme concentrations [accessed 2026-11-24]. https://arxiv.org/html/2305.12602v2; review_level=selected-primary-body
Selected §1 Eq(1)–(8) and selected discussion around transient-time estimates Eq(32); proofs and complete quantitative bounds unread.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## Lotka–Volterra invariant and positivity

Compare a positive orbit against an independently integrated log-coordinate reference.

**Methods used**

- [Classical RK4](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=en) (`rk4`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/lotka-volterra/?lang=en#lotka-volterra-en-algorithm)

Integrate physical populations with classical RK4 at 400, 800 and 1600 fixed steps. Independent Radau/BDF references evolve log x and log y; the primary method uses neither a log-coordinate update nor invariant projection.

$$
\dot x=x(1-y),\quad\dot y=y(x-1),\quad(x(0),y(0))=(1.2,0.8),\quad0\le t\le20
$$

$$
H(x,y)=x-\log x+y-\log y,\quad\frac{dH}{dt}=0\quad(x>0,y>0)
$$

$$
\frac{d\log x}{dt}=1-e^{\log y},\quad\frac{d\log y}{dt}=e^{\log x}-1
$$

- [Lotka–Volterra predator–prey](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-lotka-volterra-en) (`bio-lotka-volterra`)

Use the dimensionless predator–prey equations x′=x(1−y), y′=y(x−1), initial state (1.2,0.8) and 0≤t≤20. Evaluate H=x−log x+y−log y only in the positive quadrant.


**Problem figure**

![Lotka–Volterra invariant and positivity: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/lotka-volterra.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Lotka–Volterra invariant and positivity](https://hrkoyama.github.io/numerical-methods-atlas/problems/lotka-volterra/?lang=en) (`lotka-volterra`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/lotka-volterra/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/lotka-volterra/?lang=en#lotka-volterra-en-validation)

Measure state error against the independent reference, drift of H and the minimum saved population separately. The reference stage qualifies analytic Jacobians, Radau/BDF agreement, tolerance refinement and the identity dH/dt=0.

- [Lotka–Volterra invariant and positivity](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-lotka-volterra-en) (`lotka-volterra`; Same-problem reference · Finite-grid numerical reference)

This is a finite-time comparison for one initial state. The continuum closed orbit is not an attracting limit cycle. RK4 is not claimed to preserve H exactly, maintain positivity at arbitrary steps or guarantee long-time geometric fidelity.
### Assumptions, units and boundaries

Use the dimensionless predator–prey equations x′=x(1−y), y′=y(x−1), initial state (1.2,0.8) and 0≤t≤20. Evaluate H=x−log x+y−log y only in the positive quadrant.

**Editorial clarification**

This is a finite-time comparison for one initial state. The continuum closed orbit is not an attracting limit cycle. RK4 is not claimed to preserve H exactly, maintain positivity at arbitrary steps or guarantee long-time geometric fidelity. Time, concentrations and populations do not define a spatial dimension. The rates are educational, not disease or experimental predictions.

### Adopted numerical method

Integrate physical populations with classical RK4 at 400, 800 and 1600 fixed steps. Independent Radau/BDF references evolve log x and log y; the primary method uses neither a log-coordinate update nor invariant projection.

$$
\dot x=x(1-y),\quad\dot y=y(x-1),\quad(x(0),y(0))=(1.2,0.8),\quad0\le t\le20
$$

$$
H(x,y)=x-\log x+y-\log y,\quad\frac{dH}{dt}=0\quad(x>0,y>0)
$$

$$
\frac{d\log x}{dt}=1-e^{\log y},\quad\frac{d\log y}{dt}=e^{\log x}-1
$$

### References and validation

Measure state error against the independent reference, drift of H and the minimum saved population separately. The reference stage qualifies analytic Jacobians, Radau/BDF agreement, tolerance refinement and the identity dH/dt=0.

### Limits

This is a finite-time comparison for one initial state. The continuum closed orbit is not an attracting limit cycle. RK4 is not claimed to preserve H exactly, maintain positivity at arbitrary steps or guarantee long-time geometric fidelity.

### Original numerical targets and unmet outcomes

Passing reproduction/reporting verification does not mean that all original accuracy goals were met. Original decisions are retained.

```json
{
  "original_target_results": {
    "lv-400:state": true,
    "lv-400:invariant": true,
    "lv-800:state": true,
    "lv-800:invariant": true,
    "lv-1600:state": true,
    "lv-1600:invariant": true
  },
  "original_target_summary": {
    "met": 6,
    "total": 6,
    "all_met": true,
    "acceptance_sha256": "b468e78459cf81bda6a32cade0051f6615b44def256c66308ae7acc82ff516ce"
  }
}
```

### Stored measurements and decisions

```json
{
  "metrics": {
    "actual_primary_records": 3,
    "reference_role": "Qualified Radau/BDF full ODE; reduction/linearization errors are distinct modeling diagnostics"
  },
  "checks": {
    "lv-400:actual-grid-finite": true,
    "lv-800:actual-grid-finite": true,
    "lv-1600:actual-grid-finite": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/lotka-volterra/index.json

![Compare a positive orbit against an independently integrated log-coordinate reference. This figure reads saved data only.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/lotka-volterra-preview.png)

Compare a positive orbit against an independently integrated log-coordinate reference. This figure reads saved data only.

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/atlas-small-models-2026-11-25.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- Experiments in MATLAB, Chapter16: Predator-Prey Model [accessed 2026-11-24]. https://www.mathworks.com/content/dam/mathworks/mathworks-dot-com/moler/exm/chapters/predprey.pdf; review_level=selected-primary-body
Selected extracted text pp3–6: normalized LV equations, equilibrium, periodic-orbit discussion and numerical illustration. No original Lotka/Volterra paper read.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## SEIR conservation and initial linearization

Check population conservation and the full two-mode initial linearization separately.

**Methods used**

- [Classical RK4](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=en) (`rk4`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/seir-linearization/?lang=en#seir-linearization-en-algorithm)

Evolve all four physical states with RK4 at 400, 800 and 1600 fixed steps. Independently compute the nonlinear reference with scaled-deviation Radau/BDF and the early E/I linearization with both modes of the full 2×2 matrix exponential.

$$
\begin{aligned}\dot S&=-\beta SI,&\dot E&=\beta SI-\sigma E,\\\dot I&=\sigma E-\gamma I,&\dot R&=\gamma I.\end{aligned}
$$

$$
\beta=0.6,\quad\sigma=0.3,\quad\gamma=0.2,\quad(S,E,I,R)(0)=(1-2\eta,\eta,\eta,0)
$$

$$
S+E+I+R=1,\quad\eta\in\{10^{-4},5\times10^{-5}\}
$$

$$
\begin{pmatrix}E_{\rm lin}(t)\\ I_{\rm lin}(t)\end{pmatrix}=\exp\!\left[t\begin{pmatrix}-0.3&0.6\\0.3&-0.2\end{pmatrix}\right]\begin{pmatrix}\eta\\\eta\end{pmatrix}
$$

- [Closed SEIR compartment model](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#seir-compartment-en) (`seir-compartment`)

Use a closed population S+E+I+R=1 with β=0.6, σ=0.3 and γ=0.2. For η=10⁻⁴ or 5×10⁻⁵, start from (1−2η,η,η,0) and evolve to t=20. There are no births, deaths or external inflows.


**Problem figure**

![SEIR conservation and initial linearization: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/seir-linearization.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[SEIR conservation and initial linearization](https://hrkoyama.github.io/numerical-methods-atlas/problems/seir-linearization/?lang=en) (`seir-linearization`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/seir-linearization/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/seir-linearization/?lang=en#seir-linearization-en-validation)

Separate full-ODE integration error, population conservation and nonnegativity through t=20 from linearization-model error at 201 reference points on 0≤t≤1. Qualify scaled Jacobians, Radau/BDF agreement with an η² margin and the analytic full matrix exponential independently.

- [SEIR conservation and initial linearization](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-seir-linearization-en) (`seir-linearization`; Same-problem reference · Finite-grid numerical reference)

These fixed-coefficient calculations compare two small initial infection levels. The early linearization is not an exact solution through t=20, and a single dominant mode does not replace the two-mode solution. No epidemic forecast, statistical coverage or arbitrary-population guarantee is claimed.
### Assumptions, units and boundaries

Use a closed population S+E+I+R=1 with β=0.6, σ=0.3 and γ=0.2. For η=10⁻⁴ or 5×10⁻⁵, start from (1−2η,η,η,0) and evolve to t=20. There are no births, deaths or external inflows.

**Editorial clarification**

These fixed-coefficient calculations compare two small initial infection levels. The early linearization is not an exact solution through t=20, and a single dominant mode does not replace the two-mode solution. No epidemic forecast, statistical coverage or arbitrary-population guarantee is claimed. Time, concentrations and populations do not define a spatial dimension. The rates are educational, not disease or experimental predictions.

### Adopted numerical method

Evolve all four physical states with RK4 at 400, 800 and 1600 fixed steps. Independently compute the nonlinear reference with scaled-deviation Radau/BDF and the early E/I linearization with both modes of the full 2×2 matrix exponential.

$$
\begin{aligned}\dot S&=-\beta SI,&\dot E&=\beta SI-\sigma E,\\\dot I&=\sigma E-\gamma I,&\dot R&=\gamma I.\end{aligned}
$$

$$
\beta=0.6,\quad\sigma=0.3,\quad\gamma=0.2,\quad(S,E,I,R)(0)=(1-2\eta,\eta,\eta,0)
$$

$$
S+E+I+R=1,\quad\eta\in\{10^{-4},5\times10^{-5}\}
$$

$$
\begin{pmatrix}E_{\rm lin}(t)\\ I_{\rm lin}(t)\end{pmatrix}=\exp\!\left[t\begin{pmatrix}-0.3&0.6\\0.3&-0.2\end{pmatrix}\right]\begin{pmatrix}\eta\\\eta\end{pmatrix}
$$

### References and validation

Separate full-ODE integration error, population conservation and nonnegativity through t=20 from linearization-model error at 201 reference points on 0≤t≤1. Qualify scaled Jacobians, Radau/BDF agreement with an η² margin and the analytic full matrix exponential independently.

### Limits

These fixed-coefficient calculations compare two small initial infection levels. The early linearization is not an exact solution through t=20, and a single dominant mode does not replace the two-mode solution. No epidemic forecast, statistical coverage or arbitrary-population guarantee is claimed.

### Original numerical targets and unmet outcomes

Passing reproduction/reporting verification does not mean that all original accuracy goals were met. Original decisions are retained.

```json
{
  "original_target_results": {
    "seir-1e-4-400:integration": true,
    "seir-1e-4-400:mass": true,
    "seir-1e-4-400:negative-part": true,
    "seir-1e-4-800:integration": true,
    "seir-1e-4-800:mass": true,
    "seir-1e-4-800:negative-part": true,
    "seir-1e-4-1600:integration": true,
    "seir-1e-4-1600:mass": true,
    "seir-1e-4-1600:negative-part": true,
    "seir-1e-4:early-linearization": true,
    "seir-5e-5-400:integration": true,
    "seir-5e-5-400:mass": true,
    "seir-5e-5-400:negative-part": true,
    "seir-5e-5-800:integration": true,
    "seir-5e-5-800:mass": true,
    "seir-5e-5-800:negative-part": true,
    "seir-5e-5-1600:integration": true,
    "seir-5e-5-1600:mass": true,
    "seir-5e-5-1600:negative-part": true,
    "seir-5e-5:early-linearization": true
  },
  "original_target_summary": {
    "met": 20,
    "total": 20,
    "all_met": true,
    "acceptance_sha256": "b468e78459cf81bda6a32cade0051f6615b44def256c66308ae7acc82ff516ce"
  }
}
```

### Stored measurements and decisions

```json
{
  "metrics": {
    "actual_primary_records": 6,
    "reference_role": "Qualified Radau/BDF full ODE; reduction/linearization errors are distinct modeling diagnostics"
  },
  "checks": {
    "seir-1e-4-400:actual-grid-finite": true,
    "seir-1e-4-800:actual-grid-finite": true,
    "seir-1e-4-1600:actual-grid-finite": true,
    "seir-5e-5-400:actual-grid-finite": true,
    "seir-5e-5-800:actual-grid-finite": true,
    "seir-5e-5-1600:actual-grid-finite": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/seir-linearization/index.json

![Check population conservation and the full two-mode initial linearization separately. This figure reads saved data only.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/seir-linearization-preview.png)

Check population conservation and the full two-mode initial linearization separately. This figure reads saved data only.

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/atlas-small-models-2026-11-25.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- The Mathematics of Infectious Diseases [accessed 2026-11-24]. https://math.uchicago.edu/~shmuel/Modeling/hethcote2000%20Mathematics%20of%20Infectious%20diseases.pdf; review_level=selected-primary-body
Header, selected introduction compartment definitions and §3.1 printedpp618–619, displayed mass-action numbers and Eq(3.1); search around3.2/SEIR limit. Not whole55pages or visual diagram audit.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
