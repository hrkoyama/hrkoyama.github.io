# MG/AMG for coefficient jumps and rotated anisotropy

Compare geometric MG,SA-AMG and direct solves of identical matrices, separately from analytic or independently discretized continuum references.

These additional validation supplements are managed separately from the common 22-example registry. Receipts cover independent ZIP extraction, tests and every fixed input within each group. Changes of settings, methods or step sizes do not add independent physical problems.

## Checkerboard diffusion: shared flux, MG and AMG

Compare discontinuous-coefficient FV with independent P1 reference fields, separating linear-system residual/forward errors from continuum error.

**Methods used**

- [Geometric multigrid V-cycle](https://hrkoyama.github.io/numerical-methods-atlas/methods/multigrid/?lang=en) (`multigrid`)
- [Algebraic multigrid / AMG](https://hrkoyama.github.io/numerical-methods-atlas/methods/amg/?lang=en) (`amg`)
- [Conjugate gradients](https://hrkoyama.github.io/numerical-methods-atlas/methods/cg/?lang=en) (`cg`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/checkerboard-diffusion/?lang=en#checkerboard-diffusion-en-algorithm)

Orthogonal FV with shared harmonic transmissibility. Symmetric Galerkin geometric and coordinate-free SA cycles precondition PCG on identical matrices.

$$
-\nabla\cdot(a\nabla u)=1,\quad a\in\{1,100\}
$$

$$
T_f=|f|/(d_L/a_L+d_R/a_R)
$$

- [Discontinuous and full-tensor diffusion BVP](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#tensor-diffusion-en) (`tensor-diffusion`)

Unit square, zero Dirichlet, f=1, diagonal quadrants100/others1, N16/32/64; reference P1 meshes128/192.


**Problem figure**

![Checkerboard diffusion: shared flux, MG and AMG: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/results/checkerboard-diffusion.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Checkerboard diffusion: shared flux, MG and AMG](https://hrkoyama.github.io/numerical-methods-atlas/problems/checkerboard-diffusion/?lang=en) (`checkerboard-diffusion`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/checkerboard-diffusion/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/checkerboard-diffusion/?lang=en#checkerboard-diffusion-en-validation)

Nonzero two-material flux patch, residual-aware budget, direct forward/energy errors and independent triangular-P1 grid sensitivity.

- [Checkerboard diffusion: shared flux, MG and AMG](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-checkerboard-diffusion-en) (`checkerboard-diffusion`; Same-problem reference · Finite-grid numerical reference)

Fixed contrast100 example. P1 differences are not rigorous error bounds; no singular exponent or universal MG/AMG winner is asserted.
### Assumptions, units and boundaries

Unit square, zero Dirichlet, f=1, diagonal quadrants100/others1, N16/32/64; reference P1 meshes128/192.

**Editorial clarification**

Fixed contrast100 example. P1 differences are not rigorous error bounds; no singular exponent or universal MG/AMG winner is asserted.

### Adopted numerical method

Orthogonal FV with shared harmonic transmissibility. Symmetric Galerkin geometric and coordinate-free SA cycles precondition PCG on identical matrices.

$$
-\nabla\cdot(a\nabla u)=1,\quad a\in\{1,100\}
$$

$$
T_f=|f|/(d_L/a_L+d_R/a_R)
$$

### References and validation

Nonzero two-material flux patch, residual-aware budget, direct forward/energy errors and independent triangular-P1 grid sensitivity.

### Limits

Fixed contrast100 example. P1 differences are not rigorous error bounds; no singular exponent or universal MG/AMG winner is asserted.

### Stored measurements and decisions

```json
{
  "metrics": {
    "continuous_errors": [
      0.03320269631288309,
      0.008587452847326224,
      0.002547591920168387
    ],
    "reference_sensitivity": [
      0.00010935677943053456,
      0.0001088242415134897,
      0.00034850805399045157
    ]
  },
  "checks": {
    "n16_symmetry": true,
    "n16_geometric_converged": true,
    "n16_geometric_true_residual": true,
    "n16_geometric_forward": true,
    "n16_geometric_energy": true,
    "n16_geometric_history": true,
    "n16_geometric_flux_ledger": true,
    "n16_geometric_budget_residual_bound": true,
    "n16_amg_converged": true,
    "n16_amg_true_residual": true,
    "n16_amg_forward": true,
    "n16_amg_energy": true,
    "n16_amg_history": true,
    "n16_amg_flux_ledger": true,
    "n16_amg_budget_residual_bound": true,
    "n32_symmetry": true,
    "n32_geometric_converged": true,
    "n32_geometric_true_residual": true,
    "n32_geometric_forward": true,
    "n32_geometric_energy": true,
    "n32_geometric_history": true,
    "n32_geometric_flux_ledger": true,
    "n32_geometric_budget_residual_bound": true,
    "n32_amg_converged": true,
    "n32_amg_true_residual": true,
    "n32_amg_forward": true,
    "n32_amg_energy": true,
    "n32_amg_history": true,
    "n32_amg_flux_ledger": true,
    "n32_amg_budget_residual_bound": true,
    "n64_symmetry": true,
    "n64_geometric_converged": true,
    "n64_geometric_true_residual": true,
    "n64_geometric_forward": true,
    "n64_geometric_energy": true,
    "n64_geometric_history": true,
    "n64_geometric_flux_ledger": true,
    "n64_geometric_budget_residual_bound": true,
    "n64_amg_converged": true,
    "n64_amg_true_residual": true,
    "n64_amg_forward": true,
    "n64_amg_energy": true,
    "n64_amg_history": true,
    "n64_amg_flux_ledger": true,
    "n64_amg_budget_residual_bound": true,
    "refinement": true,
    "reference_sensitivity": true,
    "nonzero_harmonic_patch": true,
    "small_operator_spd": true,
    "geometric_small_cycle_spd": true,
    "amg_small_cycle_spd": true,
    "intentional_budget": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/checkerboard-diffusion/index.json

![Saved2D solution, error, true residual and refinement/reference sensitivity.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/results/checkerboard-diffusion-preview.png)

Saved2D solution, error, true residual and refinement/reference sensitivity.

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/atlas-coefficient-diffusion-2026-11-23.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- Two-point flux approximation. https://dumux.org/docs/doxygen/master/group___c_c_tpfa_discretization.html; review_level=selected-official-derivation-read
Scalar harmonic transmissibility, shared flux and K-orthogonality restriction. No DuMux code executed.

- BoomerAMG: smoother options. https://hypre.readthedocs.io/en/latest/solvers-boomeramg.html; review_level=selected-official-documentation-read
CG requires a symmetric smoother. Our educational SA code is not hypre and no hypre code was run.

- Algebraic multigrid by smoothed aggregation for second and fourth order elliptic problems. https://link.springer.com/article/10.1007/BF02238511; review_level=publisher-abstract-only-full-paper-unread
Metadata and abstract only. No general robustness theorem claimed for these fixed jumps/tensors.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## Rotated diffusion: full-tensor Q1, MG and AMG

Retain nonzero Kxy in the Q1 weak form and compare analytic refinement with MG/AMG convergence for the same matrix.

**Methods used**

- [Q1 FEM for scalar diffusion and mapped vector BVPs](https://hrkoyama.github.io/numerical-methods-atlas/methods/q1-fem/?lang=en) (`q1-fem`)
- [Geometric multigrid V-cycle](https://hrkoyama.github.io/numerical-methods-atlas/methods/multigrid/?lang=en) (`multigrid`)
- [Algebraic multigrid / AMG](https://hrkoyama.github.io/numerical-methods-atlas/methods/amg/?lang=en) (`amg`)
- [Conjugate gradients](https://hrkoyama.github.io/numerical-methods-atlas/methods/cg/?lang=en) (`cg`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/rotated-anisotropic-diffusion/?lang=en#rotated-anisotropic-diffusion-en-algorithm)

Full2x2 tensor Q1 and Gauss quadrature. Fixed SPD MG/SA cycles use symmetric2/2Jacobi, Galerkin operators and coarse Cholesky.

$$
-\nabla\cdot(K\nabla u)=f,\quad K=R(\pi/6)\operatorname{diag}(1,.01)R^T
$$

$$
f=\pi^2(K_{xx}+K_{yy})\sin\pi x\sin\pi y-2\pi^2K_{xy}\cos\pi x\cos\pi y
$$

- [Discontinuous and full-tensor diffusion BVP](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#tensor-diffusion-en) (`tensor-diffusion`)

Unit square, zero Dirichlet, K=R(pi/6)diag(1,.01)R^T, exact sin(pi x)sin(pi y), N16/32/64.


**Problem figure**

![Rotated diffusion: full-tensor Q1, MG and AMG: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/results/rotated-anisotropic-diffusion.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Rotated diffusion: full-tensor Q1, MG and AMG](https://hrkoyama.github.io/numerical-methods-atlas/problems/rotated-anisotropic-diffusion/?lang=en) (`rotated-anisotropic-diffusion`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/rotated-anisotropic-diffusion/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/rotated-anisotropic-diffusion/?lang=en#rotated-anisotropic-diffusion-en-validation)

u=xy,f=-2Kxy patch, analytic-flux source, integrated L2/energy error,4/6point quadrature sensitivity and direct-solve comparison.

- [Rotated diffusion: full-tensor Q1, MG and AMG](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-rotated-anisotropic-diffusion-en) (`rotated-anisotropic-diffusion`; Same-problem reference · Manufactured solution)

One angle/anisotropy only. Scalar TPFA is not extended to rotated tensors; arbitrary-tensor robustness is not established.
### Assumptions, units and boundaries

Unit square, zero Dirichlet, K=R(pi/6)diag(1,.01)R^T, exact sin(pi x)sin(pi y), N16/32/64.

**Editorial clarification**

One angle/anisotropy only. Scalar TPFA is not extended to rotated tensors; arbitrary-tensor robustness is not established.

### Adopted numerical method

Full2x2 tensor Q1 and Gauss quadrature. Fixed SPD MG/SA cycles use symmetric2/2Jacobi, Galerkin operators and coarse Cholesky.

$$
-\nabla\cdot(K\nabla u)=f,\quad K=R(\pi/6)\operatorname{diag}(1,.01)R^T
$$

$$
f=\pi^2(K_{xx}+K_{yy})\sin\pi x\sin\pi y-2\pi^2K_{xy}\cos\pi x\cos\pi y
$$

### References and validation

u=xy,f=-2Kxy patch, analytic-flux source, integrated L2/energy error,4/6point quadrature sensitivity and direct-solve comparison.

### Limits

One angle/anisotropy only. Scalar TPFA is not extended to rotated tensors; arbitrary-tensor robustness is not established.

### Stored measurements and decisions

```json
{
  "metrics": {
    "continuous_errors": [
      0.0043094975495807045,
      0.0010835497491345043,
      0.0002713461470266456
    ],
    "reference_sensitivity": []
  },
  "checks": {
    "n16_quadrature": true,
    "n16_symmetry": true,
    "n16_geometric_converged": true,
    "n16_geometric_true_residual": true,
    "n16_geometric_forward": true,
    "n16_geometric_energy": true,
    "n16_geometric_history": true,
    "n16_amg_converged": true,
    "n16_amg_true_residual": true,
    "n16_amg_forward": true,
    "n16_amg_energy": true,
    "n16_amg_history": true,
    "n32_quadrature": true,
    "n32_symmetry": true,
    "n32_geometric_converged": true,
    "n32_geometric_true_residual": true,
    "n32_geometric_forward": true,
    "n32_geometric_energy": true,
    "n32_geometric_history": true,
    "n32_amg_converged": true,
    "n32_amg_true_residual": true,
    "n32_amg_forward": true,
    "n32_amg_energy": true,
    "n32_amg_history": true,
    "n64_quadrature": true,
    "n64_symmetry": true,
    "n64_geometric_converged": true,
    "n64_geometric_true_residual": true,
    "n64_geometric_forward": true,
    "n64_geometric_energy": true,
    "n64_geometric_history": true,
    "n64_amg_converged": true,
    "n64_amg_true_residual": true,
    "n64_amg_forward": true,
    "n64_amg_energy": true,
    "n64_amg_history": true,
    "refinement": true,
    "l2_refinement_ratios": true,
    "finest_l2": true,
    "affine_patch": true,
    "xy_patch": true,
    "small_operator_spd": true,
    "geometric_small_cycle_spd": true,
    "amg_small_cycle_spd": true,
    "intentional_budget": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/rotated-anisotropic-diffusion/index.json

![Saved2D solution, error, true residual and refinement/reference sensitivity.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/results/rotated-anisotropic-diffusion-preview.png)

Saved2D solution, error, true residual and refinement/reference sensitivity.

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/atlas-coefficient-diffusion-2026-11-23.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- Two-point flux approximation. https://dumux.org/docs/doxygen/master/group___c_c_tpfa_discretization.html; review_level=selected-official-derivation-read
Scalar harmonic transmissibility, shared flux and K-orthogonality restriction. No DuMux code executed.

- BoomerAMG: smoother options. https://hypre.readthedocs.io/en/latest/solvers-boomeramg.html; review_level=selected-official-documentation-read
CG requires a symmetric smoother. Our educational SA code is not hypre and no hypre code was run.

- Algebraic multigrid by smoothed aggregation for second and fourth order elliptic problems. https://link.springer.com/article/10.1007/BF02238511; review_level=publisher-abstract-only-full-paper-unread
Metadata and abstract only. No general robustness theorem claimed for these fixed jumps/tensors.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
