# Linear algebra: factorizations, saddle systems, restarting and mass eigenpairs

Small fixed matrices compare factorization and refinement, symmetric-indefinite solves, restarted eigenpairs and a consistent-mass string. Independent references distinguish residual from solution error, algebraic from discretization error, and counted operator actions.

These additional validation supplements are managed separately from the common 22-example registry. Receipts cover independent ZIP extraction, tests and every fixed input within each group. Changes of settings, methods or step sizes do not add independent physical problems.

## Pivoted LU, Cholesky and iterative refinement

Exact-rational comparisons separate conditioning, forward and backward error, and pivot growth.

**Methods used**

- [Partial-pivot LU and mixed-precision refinement](https://hrkoyama.github.io/numerical-methods-atlas/methods/lu-partial-pivoting/?lang=en) (`lu-partial-pivoting`)
- [Cholesky factorization and triangular solves](https://hrkoyama.github.io/numerical-methods-atlas/methods/cholesky/?lang=en) (`cholesky`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/pivoted-direct-refinement/?lang=en#pivoted-direct-refinement-en-algorithm)

Original implementations of LU with partial pivoting, lower Cholesky factorization and triangular substitution.

$$
PA=LU
$$

$$
A=LL^T
$$

$$
x_(j+1)=x_j+solve_factor32(b-A*x_j)
$$

- [Finite-dimensional linear systems and factorizations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#finite-dimensional-linear-system-en) (`finite-dimensional-linear-system`)

Fixed SPD matrix of size 12, a nearly singular rank-one matrix of size 8, Hilbert matrix of size 5 and Wilkinson matrix of size 12. Factors and triangular corrections use binary32; residuals use binary64, with five updates.


**Problem figure**

![Pivoted LU, Cholesky and iterative refinement: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/pivoted-direct-refinement.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Pivoted LU, Cholesky and iterative refinement](https://hrkoyama.github.io/numerical-methods-atlas/problems/pivoted-direct-refinement/?lang=en) (`pivoted-direct-refinement`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/pivoted-direct-refinement/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/pivoted-direct-refinement/?lang=en#pivoted-direct-refinement-en-validation)

Exact-rational solutions for the actual binary64 inputs and separate LAPACK DGESV/DPOSV comparisons. Conditioning, forward error and backward error are reported separately. Each saved reference component is the exact Fraction solution rounded to binary64.

- [Pivoted LU and Cholesky: exact-rational references for actual binary input](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-pivoted-direct-refinement-en) (`pivoted-direct-refinement`; Same-problem reference · Analytic reference)

Small fixed examples only; convergence of mixed-precision refinement is not guaranteed for arbitrary matrices.
### Assumptions, units and boundaries

Fixed SPD matrix of size 12, a nearly singular rank-one matrix of size 8, Hilbert matrix of size 5 and Wilkinson matrix of size 12. Factors and triangular corrections use binary32; residuals use binary64, with five updates.

**Editorial clarification**

Small fixed examples only; convergence of mixed-precision refinement is not guaranteed for arbitrary matrices.

### Adopted numerical method

Original implementations of LU with partial pivoting, lower Cholesky factorization and triangular substitution.

$$
PA=LU
$$

$$
A=LL^T
$$

$$
x_(j+1)=x_j+solve_factor32(b-A*x_j)
$$

### References and validation

Exact-rational solutions for the actual binary64 inputs and separate LAPACK DGESV/DPOSV comparisons. Conditioning, forward error and backward error are reported separately. Each saved reference component is the exact Fraction solution rounded to binary64.

### Limits

Small fixed examples only; convergence of mixed-precision refinement is not guaranteed for arbitrary matrices.

### Stored measurements and decisions

```json
{
  "metrics": {
    "max_condition_infinity": 943656.0000016841,
    "max_relative_forward_error": 7.33203121885131e-12,
    "max_normwise_backward_error": 8.07438287144266e-17,
    "max_componentwise_backward_error": 1.2810265668752034e-16,
    "max_relative_LAPACK_difference": 6.180857514425556e-12,
    "max_binary64_pivot_growth": 2048.0
  },
  "checks": {
    "spd-tridiagonal-lu/finite": true,
    "spd-tridiagonal-lu/binary32-factor": true,
    "spd-tridiagonal-lu/binary64-factor": true,
    "spd-tridiagonal-lu/normwise-backward": true,
    "spd-tridiagonal-lu/componentwise-backward": true,
    "spd-tridiagonal-lu/condition-aware-forward": true,
    "spd-tridiagonal-lu/LAPACK-comparison": true,
    "spd-tridiagonal-lu/refinement-gain-or-roundoff": true,
    "spd-tridiagonal-cholesky/finite": true,
    "spd-tridiagonal-cholesky/binary32-factor": true,
    "spd-tridiagonal-cholesky/binary64-factor": true,
    "spd-tridiagonal-cholesky/normwise-backward": true,
    "spd-tridiagonal-cholesky/componentwise-backward": true,
    "spd-tridiagonal-cholesky/condition-aware-forward": true,
    "spd-tridiagonal-cholesky/LAPACK-comparison": true,
    "spd-tridiagonal-cholesky/refinement-gain-or-roundoff": true,
    "near-singular-rank-one-lu/finite": true,
    "near-singular-rank-one-lu/binary32-factor": true,
    "near-singular-rank-one-lu/binary64-factor": true,
    "near-singular-rank-one-lu/normwise-backward": true,
    "near-singular-rank-one-lu/componentwise-backward": true,
    "near-singular-rank-one-lu/condition-aware-forward": true,
    "near-singular-rank-one-lu/LAPACK-comparison": true,
    "near-singular-rank-one-lu/refinement-gain-or-roundoff": true,
    "near-singular-rank-one-cholesky/finite": true,
    "near-singular-rank-one-cholesky/binary32-factor": true,
    "near-singular-rank-one-cholesky/binary64-factor": true,
    "near-singular-rank-one-cholesky/normwise-backward": true,
    "near-singular-rank-one-cholesky/componentwise-backward": true,
    "near-singular-rank-one-cholesky/condition-aware-forward": true,
    "near-singular-rank-one-cholesky/LAPACK-comparison": true,
    "near-singular-rank-one-cholesky/refinement-gain-or-roundoff": true,
    "hilbert5-lu/finite": true,
    "hilbert5-lu/binary32-factor": true,
    "hilbert5-lu/binary64-factor": true,
    "hilbert5-lu/normwise-backward": true,
    "hilbert5-lu/componentwise-backward": true,
    "hilbert5-lu/condition-aware-forward": true,
    "hilbert5-lu/LAPACK-comparison": true,
    "hilbert5-lu/refinement-gain-or-roundoff": true,
    "hilbert5-cholesky/finite": true,
    "hilbert5-cholesky/binary32-factor": true,
    "hilbert5-cholesky/binary64-factor": true,
    "hilbert5-cholesky/normwise-backward": true,
    "hilbert5-cholesky/componentwise-backward": true,
    "hilbert5-cholesky/condition-aware-forward": true,
    "hilbert5-cholesky/LAPACK-comparison": true,
    "hilbert5-cholesky/refinement-gain-or-roundoff": true,
    "wilkinson12-lu/finite": true,
    "wilkinson12-lu/binary32-factor": true,
    "wilkinson12-lu/binary64-factor": true,
    "wilkinson12-lu/normwise-backward": true,
    "wilkinson12-lu/componentwise-backward": true,
    "wilkinson12-lu/condition-aware-forward": true,
    "wilkinson12-lu/LAPACK-comparison": true,
    "wilkinson12-lu/refinement-gain-or-roundoff": true,
    "Wilkinson/exact-growth": true,
    "Hilbert/ill-conditioning-not-residual": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/pivoted-direct-refinement/index.json

![The saved 12 x 12 SPD matrix used in the refinement examples. In the companion full figure, errors are measured against the exact-rational solution rounded to binary64; exact zeros are shown at float64.tiny for logarithmic display only.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/pivoted-direct-refinement-preview.png)

The saved 12 x 12 SPD matrix used in the refinement examples. In the companion full figure, errors are measured against the exact-rational solution rounded to binary64; exact zeros are shown at float64.tiny for logarithmic display only.

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/atlas-linear-algebra-spectral-2026-11-24-r3.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- LAPACK Users Guide: Linear Equations. https://netlib.org/lapack/lug/node38.html; review_level=selected-official-documentation
Selected LU/Cholesky, CON/RFS and same-precision refinement paragraphs were read. This example uses binary32 factors and binary64 residuals; a full LAPACK source audit is not claimed.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## Symmetric saddle systems and Schur preconditioning

MINRES and GMRES use the same original-system residual criterion and are checked against the ideal Schur three-point spectrum.

**Methods used**

- [Educational MINRES for symmetric-indefinite systems](https://hrkoyama.github.io/numerical-methods-atlas/methods/minres/?lang=en) (`minres`)
- [Restarted GMRES](https://hrkoyama.github.io/numerical-methods-atlas/methods/gmres/?lang=en) (`gmres`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/symmetric-saddle-minres/?lang=en#symmetric-saddle-minres-en-algorithm)

Stored-basis Lanczos least squares provides the educational MINRES variant; GMRES uses two-pass modified Gram-Schmidt. An SPD congruence preserves symmetry. The internal target is min(configured rtol, fixed forward-error limit / kappa_infinity), using only the matrix. The independent solution is not a stopping input.

$$
A=[[H,B^T],[B,0]]
$$

$$
P=diag(H,BH^-1B^T)
$$

$$
A_tilde=L^-1 A L^-T
$$

- [Finite-dimensional linear systems and factorizations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#finite-dimensional-linear-system-en) (`finite-dimensional-linear-system`)

Algebraic mixed-Poisson/Stokes-type blocks with velocity sizes 12 and 24 and pressure sizes 5 and 11. The common original-system residual tolerance is 1e-9.


**Problem figure**

![Symmetric saddle systems and Schur preconditioning: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/symmetric-saddle-minres.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Symmetric saddle systems and Schur preconditioning](https://hrkoyama.github.io/numerical-methods-atlas/problems/symmetric-saddle-minres/?lang=en) (`symmetric-saddle-minres`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/symmetric-saddle-minres/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/symmetric-saddle-minres/?lang=en#symmetric-saddle-minres-en-validation)

Global LAPACK solutions, the analytic ideal-Schur spectrum and an explicit negative-curvature control for CG.

- [Symmetric saddles: independent dense solutions and the ideal-Schur spectrum](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-symmetric-saddle-minres-en) (`symmetric-saddle-minres`; Same-problem reference · Finite-grid numerical reference)

A dense, ideal-Schur educational control, not a complete Stokes PDE solver or a scalable approximate preconditioner.
### Assumptions, units and boundaries

Algebraic mixed-Poisson/Stokes-type blocks with velocity sizes 12 and 24 and pressure sizes 5 and 11. The common original-system residual tolerance is 1e-9.

**Editorial clarification**

A dense, ideal-Schur educational control, not a complete Stokes PDE solver or a scalable approximate preconditioner.

### Adopted numerical method

Stored-basis Lanczos least squares provides the educational MINRES variant; GMRES uses two-pass modified Gram-Schmidt. An SPD congruence preserves symmetry. The internal target is min(configured rtol, fixed forward-error limit / kappa_infinity), using only the matrix. The independent solution is not a stopping input.

$$
A=[[H,B^T],[B,0]]
$$

$$
P=diag(H,BH^-1B^T)
$$

$$
A_tilde=L^-1 A L^-T
$$

### References and validation

Global LAPACK solutions, the analytic ideal-Schur spectrum and an explicit negative-curvature control for CG.

### Limits

A dense, ideal-Schur educational control, not a complete Stokes PDE solver or a scalable approximate preconditioner.

### Stored measurements and decisions

```json
{
  "metrics": {
    "max_original_relative_residual": 2.340278567268362e-13,
    "max_relative_reference_error": 4.2310885906326075e-10,
    "max_iterations": 29,
    "max_condition_infinity_estimate": 5682.080194251278
  },
  "checks": {
    "n12/ideal-Schur-three-point-spectrum": true,
    "saddle-12-none-minres/finite": true,
    "saddle-12-none-minres/same-true-residual": true,
    "saddle-12-none-minres/independent-reference": true,
    "saddle-12-none-minres/basis-orthogonality": true,
    "saddle-12-none-minres/symmetric-congruence": true,
    "saddle-12-none-minres/fixed-dimension-budget": true,
    "saddle-12-none-gmres/finite": true,
    "saddle-12-none-gmres/same-true-residual": true,
    "saddle-12-none-gmres/independent-reference": true,
    "saddle-12-none-gmres/basis-orthogonality": true,
    "saddle-12-none-gmres/symmetric-congruence": true,
    "saddle-12-none-gmres/fixed-dimension-budget": true,
    "saddle-12-exact-Schur-minres/finite": true,
    "saddle-12-exact-Schur-minres/same-true-residual": true,
    "saddle-12-exact-Schur-minres/independent-reference": true,
    "saddle-12-exact-Schur-minres/basis-orthogonality": true,
    "saddle-12-exact-Schur-minres/symmetric-congruence": true,
    "saddle-12-exact-Schur-minres/fixed-dimension-budget": true,
    "saddle-12-exact-Schur-minres/ideal-three-step-control": true,
    "saddle-12-exact-Schur-gmres/finite": true,
    "saddle-12-exact-Schur-gmres/same-true-residual": true,
    "saddle-12-exact-Schur-gmres/independent-reference": true,
    "saddle-12-exact-Schur-gmres/basis-orthogonality": true,
    "saddle-12-exact-Schur-gmres/symmetric-congruence": true,
    "saddle-12-exact-Schur-gmres/fixed-dimension-budget": true,
    "saddle-12-exact-Schur-gmres/ideal-three-step-control": true,
    "n24/ideal-Schur-three-point-spectrum": true,
    "saddle-24-none-minres/finite": true,
    "saddle-24-none-minres/same-true-residual": true,
    "saddle-24-none-minres/independent-reference": true,
    "saddle-24-none-minres/basis-orthogonality": true,
    "saddle-24-none-minres/symmetric-congruence": true,
    "saddle-24-none-minres/fixed-dimension-budget": true,
    "saddle-24-none-gmres/finite": true,
    "saddle-24-none-gmres/same-true-residual": true,
    "saddle-24-none-gmres/independent-reference": true,
    "saddle-24-none-gmres/basis-orthogonality": true,
    "saddle-24-none-gmres/symmetric-congruence": true,
    "saddle-24-none-gmres/fixed-dimension-budget": true,
    "saddle-24-exact-Schur-minres/finite": true,
    "saddle-24-exact-Schur-minres/same-true-residual": true,
    "saddle-24-exact-Schur-minres/independent-reference": true,
    "saddle-24-exact-Schur-minres/basis-orthogonality": true,
    "saddle-24-exact-Schur-minres/symmetric-congruence": true,
    "saddle-24-exact-Schur-minres/fixed-dimension-budget": true,
    "saddle-24-exact-Schur-minres/ideal-three-step-control": true,
    "saddle-24-exact-Schur-gmres/finite": true,
    "saddle-24-exact-Schur-gmres/same-true-residual": true,
    "saddle-24-exact-Schur-gmres/independent-reference": true,
    "saddle-24-exact-Schur-gmres/basis-orthogonality": true,
    "saddle-24-exact-Schur-gmres/symmetric-congruence": true,
    "saddle-24-exact-Schur-gmres/fixed-dimension-budget": true,
    "saddle-24-exact-Schur-gmres/ideal-three-step-control": true,
    "CG/explicit-negative-curvature-control": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/symmetric-saddle-minres/index.json

![The saved 35 x 35 saddle matrix for velocity size 24.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/symmetric-saddle-minres-preview.png)

The saved 35 x 35 saddle matrix for velocity size 24.

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/atlas-linear-algebra-spectral-2026-11-24-r3.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- Paige and Saunders: Stanford SOL MINRES. https://web.stanford.edu/group/SOL/software/minres/; review_level=selected-author-official-documentation
Selected discussion of symmetric indefinite systems, SPD preconditioners and the original residual was read. The original 1975 paper was not read. This stored-basis Lanczos least-squares variant is not a copy of the production short recurrence.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## Explicitly restarted Krylov and interior eigenvalues

Explicit restarting and shift-invert are compared using original eigenproblem residuals and counted operator actions.

**Methods used**

- [Krylov eigenvalue solvers](https://hrkoyama.github.io/numerical-methods-atlas/methods/eigensolvers/?lang=en) (`eigensolvers`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/restarted-shift-invert/?lang=en#restarted-shift-invert-en-algorithm)

Two-pass Arnoldi is explicitly restarted from one Ritz vector. Original LU routines perform the shifted solves, and stopping uses the original eigenproblem.

$$
lambda_j=4(n+1)^2 sin^2(j*pi/[2(n+1)])
$$

$$
T=(A-sigma I)^-1
$$

$$
lambda=sigma+1/theta
$$

- [Finite-dimensional matrix eigenproblems](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#finite-dimensional-eigenproblem-en) (`finite-dimensional-eigenproblem`)

A fixed Dirichlet Laplacian of size 31, restart lengths 8 and 16, and at most 40 cycles. Compare the untransformed problem with shifts 0 and 950.


**Problem figure**

![Explicitly restarted Krylov and interior eigenvalues: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/restarted-shift-invert.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Explicitly restarted Krylov and interior eigenvalues](https://hrkoyama.github.io/numerical-methods-atlas/problems/restarted-shift-invert/?lang=en) (`restarted-shift-invert`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/restarted-shift-invert/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/restarted-shift-invert/?lang=en#restarted-shift-invert-en-validation)

The known discrete sine spectrum and an independent global LAPACK comparison. Shift-solve, Krylov and original-residual actions are counted separately.

- [Restarting and shift-invert: the closed spectrum of a fixed discrete matrix](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-restarted-shift-invert-en) (`restarted-shift-invert`; Same-problem reference · Analytic reference)

One eigenpair of a real symmetric matrix only. No implicit restarting, Krylov-Schur, locking, or general nonnormal or clustered-spectrum capability is claimed.
### Assumptions, units and boundaries

A fixed Dirichlet Laplacian of size 31, restart lengths 8 and 16, and at most 40 cycles. Compare the untransformed problem with shifts 0 and 950.

**Editorial clarification**

One eigenpair of a real symmetric matrix only. No implicit restarting, Krylov-Schur, locking, or general nonnormal or clustered-spectrum capability is claimed.

### Adopted numerical method

Two-pass Arnoldi is explicitly restarted from one Ritz vector. Original LU routines perform the shifted solves, and stopping uses the original eigenproblem.

$$
lambda_j=4(n+1)^2 sin^2(j*pi/[2(n+1)])
$$

$$
T=(A-sigma I)^-1
$$

$$
lambda=sigma+1/theta
$$

### References and validation

The known discrete sine spectrum and an independent global LAPACK comparison. Shift-solve, Krylov and original-residual actions are counted separately.

### Limits

One eigenpair of a real symmetric matrix only. No implicit restarting, Krylov-Schur, locking, or general nonnormal or clustered-spectrum capability is claimed.

### Stored measurements and decisions

```json
{
  "metrics": {
    "max_original_eigenpair_residual": 5.774117289151498e-10,
    "max_operator_calls": 216,
    "max_restart_cycles": 27,
    "max_shift_solve_count": 16
  },
  "checks": {
    "restart-8-shift-None/finite": true,
    "restart-8-shift-None/original-problem-residual": true,
    "restart-8-shift-None/known-spectrum": true,
    "restart-8-shift-None/shift-linear-residual": true,
    "restart-8-shift-None/action-budget": true,
    "restart-8-shift-None/basis-orthogonality": true,
    "restart-8-shift-None/inverse-spectral-map": true,
    "restart-16-shift-None/finite": true,
    "restart-16-shift-None/original-problem-residual": true,
    "restart-16-shift-None/known-spectrum": true,
    "restart-16-shift-None/shift-linear-residual": true,
    "restart-16-shift-None/action-budget": true,
    "restart-16-shift-None/basis-orthogonality": true,
    "restart-16-shift-None/inverse-spectral-map": true,
    "restart-8-shift-0.0/finite": true,
    "restart-8-shift-0.0/original-problem-residual": true,
    "restart-8-shift-0.0/known-spectrum": true,
    "restart-8-shift-0.0/shift-linear-residual": true,
    "restart-8-shift-0.0/action-budget": true,
    "restart-8-shift-0.0/basis-orthogonality": true,
    "restart-8-shift-0.0/inverse-spectral-map": true,
    "restart-16-shift-0.0/finite": true,
    "restart-16-shift-0.0/original-problem-residual": true,
    "restart-16-shift-0.0/known-spectrum": true,
    "restart-16-shift-0.0/shift-linear-residual": true,
    "restart-16-shift-0.0/action-budget": true,
    "restart-16-shift-0.0/basis-orthogonality": true,
    "restart-16-shift-0.0/inverse-spectral-map": true,
    "restart-8-shift-950.0/finite": true,
    "restart-8-shift-950.0/original-problem-residual": true,
    "restart-8-shift-950.0/known-spectrum": true,
    "restart-8-shift-950.0/shift-linear-residual": true,
    "restart-8-shift-950.0/action-budget": true,
    "restart-8-shift-950.0/basis-orthogonality": true,
    "restart-8-shift-950.0/inverse-spectral-map": true,
    "restart-16-shift-950.0/finite": true,
    "restart-16-shift-950.0/original-problem-residual": true,
    "restart-16-shift-950.0/known-spectrum": true,
    "restart-16-shift-950.0/shift-linear-residual": true,
    "restart-16-shift-950.0/action-budget": true,
    "restart-16-shift-950.0/basis-orthogonality": true,
    "restart-16-shift-950.0/inverse-spectral-map": true,
    "shift/exact-singularity-failure-retained-as-control": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/restarted-shift-invert/index.json

![The saved 31 x 31 Dirichlet Laplacian used in the eigenvalue comparisons.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/restarted-shift-invert-preview.png)

The saved 31 x 31 Dirichlet Laplacian used in the eigenvalue comparisons.

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/atlas-linear-algebra-spectral-2026-11-24-r3.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- SLEPc EPS: projection, Krylov methods and shift-invert. https://slepc.upv.es/release/documentation/manual/eps.html; review_level=selected-official-documentation
Selected projection, Arnoldi, restarting, shift-invert and generalized-problem paragraphs were read. No SLEPc execution or Krylov-Schur reproduction is claimed.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## Consistent-mass FEM string eigenpairs

Consistent-mass P1 string eigenpairs compare an M-inner-product Krylov method and actual SciPy LOBPCG with an independent discrete spectrum.

**Methods used**

- [Krylov eigenvalue solvers](https://hrkoyama.github.io/numerical-methods-atlas/methods/eigensolvers/?lang=en) (`eigensolvers`)
- [Generalized eigenpairs with SciPy LOBPCG](https://hrkoyama.github.io/numerical-methods-atlas/methods/lobpcg/?lang=en) (`lobpcg`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/fem-mass-eigen/?lang=en#fem-mass-eigen-en-algorithm)

Elementwise K and M assembly, M-inner-product Krylov iteration on K^-1 M, and actual SciPy LOBPCG with a small exact-K-inverse preconditioner. LOBPCG starts from {1, x^3, x^6}; degree-plus-two images avoid the structural rank defect of {1, x, x^2}. The same M is applied through a qualified einsum LinearOperator, avoiding the dense-B adapter. The eigensolver itself remains SciPy LOBPCG.

$$
K x=lambda M x
$$

$$
lambda_j,h=6(1-cos(theta_j))/[h^2(2+cos(theta_j))]
$$

$$
X^T M X=I
$$

- [Fixed-end string eigenvalues and consistent-mass FEM](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#dirichlet-string-eigenproblem-en) (`dirichlet-string-eigenproblem`)

A unit string with unit tension and density and homogeneous Dirichlet endpoints. Use 15, 31 and 63 interior nodes and the lowest three eigenpairs.


**Problem figure**

![Consistent-mass FEM string eigenpairs: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/fem-mass-eigen.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Consistent-mass FEM string eigenpairs](https://hrkoyama.github.io/numerical-methods-atlas/problems/fem-mass-eigen/?lang=en) (`fem-mass-eigen`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/fem-mass-eigen/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/fem-mass-eigen/?lang=en#fem-mass-eigen-en-validation)

Generalized dense eigh, an independent discrete spectrum and refinement toward (j*pi)^2. M-orthogonality and original residuals are distinct quantities.

- [Consistent-mass P1 string: closed discrete and continuum eigenvalues](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-fem-mass-eigen-en) (`fem-mass-eigen`; Same-problem reference · Analytic reference)

A small 1D string only. If SciPy raises before returning, inputs are retained; unreturned internal iterates are not claimed to be saved. The 35 component checks do not replace the four full scientific cases.
### Assumptions, units and boundaries

A unit string with unit tension and density and homogeneous Dirichlet endpoints. Use 15, 31 and 63 interior nodes and the lowest three eigenpairs.

**Editorial clarification**

A small 1D string only. If SciPy raises before returning, inputs are retained; unreturned internal iterates are not claimed to be saved. The 35 component checks do not replace the four full scientific cases.

### Adopted numerical method

Elementwise K and M assembly, M-inner-product Krylov iteration on K^-1 M, and actual SciPy LOBPCG with a small exact-K-inverse preconditioner. LOBPCG starts from {1, x^3, x^6}; degree-plus-two images avoid the structural rank defect of {1, x, x^2}. The same M is applied through a qualified einsum LinearOperator, avoiding the dense-B adapter. The eigensolver itself remains SciPy LOBPCG.

$$
K x=lambda M x
$$

$$
lambda_j,h=6(1-cos(theta_j))/[h^2(2+cos(theta_j))]
$$

$$
X^T M X=I
$$

### References and validation

Generalized dense eigh, an independent discrete spectrum and refinement toward (j*pi)^2. M-orthogonality and original residuals are distinct quantities.

### Limits

A small 1D string only. If SciPy raises before returning, inputs are retained; unreturned internal iterates are not claimed to be saved. The 35 component checks do not replace the four full scientific cases.

### Stored measurements and decisions

```json
{
  "metrics": {
    "max_generalized_residual": 1.94948028233657e-10,
    "max_M_orthogonality_defect": 1.1102230246251565e-15,
    "max_relative_reference_error": 1.5843735459579712e-13,
    "max_operator_vector_actions": 30,
    "max_preconditioner_vector_actions": 24
  },
  "checks": {
    "fem-15-mass-Krylov/finite": true,
    "fem-15-mass-Krylov/original-generalized-residual": true,
    "fem-15-mass-Krylov/M-orthogonality": true,
    "fem-15-mass-Krylov/independent-dense-reference": true,
    "fem-15-mass-Krylov/exact-discrete-spectrum": true,
    "fem-15-mass-Krylov/fixed-action-budget": true,
    "fem-15-SciPy-LOBPCG/finite": true,
    "fem-15-SciPy-LOBPCG/original-generalized-residual": true,
    "fem-15-SciPy-LOBPCG/M-orthogonality": true,
    "fem-15-SciPy-LOBPCG/independent-dense-reference": true,
    "fem-15-SciPy-LOBPCG/exact-discrete-spectrum": true,
    "fem-15-SciPy-LOBPCG/fixed-action-budget": true,
    "fem-31-mass-Krylov/finite": true,
    "fem-31-mass-Krylov/original-generalized-residual": true,
    "fem-31-mass-Krylov/M-orthogonality": true,
    "fem-31-mass-Krylov/independent-dense-reference": true,
    "fem-31-mass-Krylov/exact-discrete-spectrum": true,
    "fem-31-mass-Krylov/fixed-action-budget": true,
    "fem-31-SciPy-LOBPCG/finite": true,
    "fem-31-SciPy-LOBPCG/original-generalized-residual": true,
    "fem-31-SciPy-LOBPCG/M-orthogonality": true,
    "fem-31-SciPy-LOBPCG/independent-dense-reference": true,
    "fem-31-SciPy-LOBPCG/exact-discrete-spectrum": true,
    "fem-31-SciPy-LOBPCG/fixed-action-budget": true,
    "fem-63-mass-Krylov/finite": true,
    "fem-63-mass-Krylov/original-generalized-residual": true,
    "fem-63-mass-Krylov/M-orthogonality": true,
    "fem-63-mass-Krylov/independent-dense-reference": true,
    "fem-63-mass-Krylov/exact-discrete-spectrum": true,
    "fem-63-mass-Krylov/fixed-action-budget": true,
    "fem-63-SciPy-LOBPCG/finite": true,
    "fem-63-SciPy-LOBPCG/original-generalized-residual": true,
    "fem-63-SciPy-LOBPCG/M-orthogonality": true,
    "fem-63-SciPy-LOBPCG/independent-dense-reference": true,
    "fem-63-SciPy-LOBPCG/exact-discrete-spectrum": true,
    "fem-63-SciPy-LOBPCG/fixed-action-budget": true,
    "continuum/second-order-ratio-1": true,
    "continuum/second-order-ratio-2": true,
    "continuum/finest-three-eigenvalues": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/fem-mass-eigen/index.json

![The first three M-normalized modes computed on the 63-node interior grid.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/fem-mass-eigen-preview.png)

The first three M-normalized modes computed on the 63-node interior grid.

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/atlas-linear-algebra-spectral-2026-11-24-r3.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- SLEPc EPS: projection, Krylov methods and shift-invert. https://slepc.upv.es/release/documentation/manual/eps.html; review_level=selected-official-documentation
Selected projection, Arnoldi, restarting, shift-invert and generalized-problem paragraphs were read. No SLEPc execution or Krylov-Schur reproduction is claimed.

- SciPy 1.14.1 LOBPCG API. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.sparse.linalg.lobpcg.html; review_level=selected-official-documentation
Selected discussion of SPD B, preconditioner M, the history tuple, the 3k eigensolve, the 5k > n fallback and the rod example was read. This maintained-library comparison shares reduced LAPACK primitives; LOBPCG is not independently authored here.

- SciPy 1.14.1 LOBPCG adapter and initial B-orthonormalization. https://raw.githubusercontent.com/scipy/scipy/v1.14.1/scipy/sparse/linalg/_eigen/lobpcg/lobpcg.py; review_level=selected-official-source
Selected _makeMatMat, _b_orthonormalize and API lines were read. The installed pinned file is bound separately. No full reading of the original LOBPCG paper or byte equality between wheel and Web source formatting is claimed.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
