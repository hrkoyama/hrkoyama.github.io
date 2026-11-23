# MG/AMG for coefficient jumps and rotated anisotropy

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-coefficient-diffusion/

Resources explicitly registered to the methods, problems and executions of this chapter. Compare geometric MG,SA-AMG and direct solves of identical matrices, separately from analytic or independently discretized continuum references.

## Methods

- [Geometric multigrid V-cycle](<https://hrkoyama.github.io/numerical-methods-atlas/methods/multigrid/?lang=en>)

  Orthogonal FV with shared harmonic transmissibility. Symmetric Galerkin geometric and coordinate-free SA cycles precondition PCG on identical matrices.
- [Algebraic multigrid / AMG](<https://hrkoyama.github.io/numerical-methods-atlas/methods/amg/?lang=en>)

  Orthogonal FV with shared harmonic transmissibility. Symmetric Galerkin geometric and coordinate-free SA cycles precondition PCG on identical matrices.
- [Conjugate gradients](<https://hrkoyama.github.io/numerical-methods-atlas/methods/cg/?lang=en>)

  Orthogonal FV with shared harmonic transmissibility. Symmetric Galerkin geometric and coordinate-free SA cycles precondition PCG on identical matrices.
- [Q1 FEM for scalar diffusion and mapped vector BVPs](<https://hrkoyama.github.io/numerical-methods-atlas/methods/q1-fem/?lang=en>)

  Full2x2 tensor Q1 and Gauss quadrature. Fixed SPD MG/SA cycles use symmetric2/2Jacobi, Galerkin operators and coarse Cholesky.
- [Geometric multigrid V-cycle](<https://hrkoyama.github.io/numerical-methods-atlas/methods/multigrid/?lang=en>)

  Full2x2 tensor Q1 and Gauss quadrature. Fixed SPD MG/SA cycles use symmetric2/2Jacobi, Galerkin operators and coarse Cholesky.
- [Algebraic multigrid / AMG](<https://hrkoyama.github.io/numerical-methods-atlas/methods/amg/?lang=en>)

  Full2x2 tensor Q1 and Gauss quadrature. Fixed SPD MG/SA cycles use symmetric2/2Jacobi, Galerkin operators and coarse Cholesky.
- [Conjugate gradients](<https://hrkoyama.github.io/numerical-methods-atlas/methods/cg/?lang=en>)

  Full2x2 tensor Q1 and Gauss quadrature. Fixed SPD MG/SA cycles use symmetric2/2Jacobi, Galerkin operators and coarse Cholesky.
- [Geometric multigrid V-cycle](<https://hrkoyama.github.io/numerical-methods-atlas/methods/multigrid/?lang=en>)
- [Algebraic multigrid / AMG](<https://hrkoyama.github.io/numerical-methods-atlas/methods/amg/?lang=en>)
- [Conjugate gradients](<https://hrkoyama.github.io/numerical-methods-atlas/methods/cg/?lang=en>)
- [Q1 FEM for scalar diffusion and mapped vector BVPs](<https://hrkoyama.github.io/numerical-methods-atlas/methods/q1-fem/?lang=en>)

## Equations

- [Discontinuous and full-tensor diffusion BVP](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#tensor-diffusion-en>)

  Separate scalar harmonic-flux FV from full-tensor Q1 with nonzero cross terms. MG and AMG solve the same matrix. Unit square, zero Dirichlet, f=1, diagonal quadrants100/others1, N16/32/64; reference P1 meshes128/192.
- [Discontinuous and full-tensor diffusion BVP](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#tensor-diffusion-en>)

  Separate scalar harmonic-flux FV from full-tensor Q1 with nonzero cross terms. MG and AMG solve the same matrix. Unit square, zero Dirichlet, K=R(pi/6)diag(1,.01)R^T, exact sin(pi x)sin(pi y), N16/32/64.
- [Discontinuous and full-tensor diffusion BVP](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#tensor-diffusion-en>)

  Separate scalar harmonic-flux FV from full-tensor Q1 with nonzero cross terms. MG and AMG solve the same matrix.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/checkerboard-diffusion/?lang=en#checkerboard-diffusion-en-algorithm>)

  Orthogonal FV with shared harmonic transmissibility. Symmetric Galerkin geometric and coordinate-free SA cycles precondition PCG on identical matrices.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/rotated-anisotropic-diffusion/?lang=en#rotated-anisotropic-diffusion-en-algorithm>)

  Full2x2 tensor Q1 and Gauss quadrature. Fixed SPD MG/SA cycles use symmetric2/2Jacobi, Galerkin operators and coarse Cholesky.

## Problem figures

- [Checkerboard diffusion: shared flux, MG and AMG](<https://hrkoyama.github.io/numerical-methods-atlas/problems/checkerboard-diffusion/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/results/checkerboard-diffusion-preview.png
- [Rotated diffusion: full-tensor Q1, MG and AMG](<https://hrkoyama.github.io/numerical-methods-atlas/problems/rotated-anisotropic-diffusion/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/results/rotated-anisotropic-diffusion-preview.png
- [Checkerboard diffusion: shared flux, MG and AMG](<https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/results/checkerboard-diffusion.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/results/checkerboard-diffusion.png
- [Rotated diffusion: full-tensor Q1, MG and AMG](<https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/results/rotated-anisotropic-diffusion.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/results/rotated-anisotropic-diffusion.png

## Exact / reference solutions

- [Checkerboard diffusion: shared flux, MG and AMG — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/checkerboard-diffusion/?lang=en#references-en>)

  Nonzero two-material flux patch, residual-aware budget, direct forward/energy errors and independent triangular-P1 grid sensitivity.
- [Checkerboard diffusion: shared flux, MG and AMG](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-checkerboard-diffusion-en>)
  relation: same-problem
  reference_kind: numerical-reference

  Finite-grid numerical reference Unit square, zero Dirichlet, f=1, diagonal quadrants100/others1, N16/32/64; reference P1 meshes128/192. Fixed contrast100 example. P1 differences are not rigorous error bounds; no singular exponent or universal MG/AMG winner is asserted.
- [Rotated diffusion: full-tensor Q1, MG and AMG — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/rotated-anisotropic-diffusion/?lang=en#references-en>)

  u=xy,f=-2Kxy patch, analytic-flux source, integrated L2/energy error,4/6point quadrature sensitivity and direct-solve comparison.
- [Rotated diffusion: full-tensor Q1, MG and AMG](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-rotated-anisotropic-diffusion-en>)
  relation: same-problem
  reference_kind: manufactured

  Manufactured solution Unit square, zero Dirichlet, K=R(pi/6)diag(1,.01)R^T, exact sin(pi x)sin(pi y), N16/32/64. One angle/anisotropy only. Scalar TPFA is not extended to rotated tensors; arbitrary-tensor robustness is not established.
- [Checkerboard diffusion: shared flux, MG and AMG](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-checkerboard-diffusion-en>)
  reference_kind: numerical-reference

  Finite-grid numerical reference Unit square, zero Dirichlet, f=1, diagonal quadrants100/others1, N16/32/64; reference P1 meshes128/192.
- [Rotated diffusion: full-tensor Q1, MG and AMG](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-rotated-anisotropic-diffusion-en>)
  reference_kind: manufactured

  Manufactured solution Unit square, zero Dirichlet, K=R(pi/6)diag(1,.01)R^T, exact sin(pi x)sin(pi y), N16/32/64.
- [Checkerboard diffusion: shared flux, MG and AMG — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/checkerboard-diffusion/?lang=en#checkerboard-diffusion-en-validation>)

  Nonzero two-material flux patch, residual-aware budget, direct forward/energy errors and independent triangular-P1 grid sensitivity.
- [Checkerboard diffusion: shared flux, MG and AMG](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-checkerboard-diffusion-en>)
  relation: same-problem
  reference_kind: numerical-reference

  Finite-grid numerical reference Unit square, zero Dirichlet, f=1, diagonal quadrants100/others1, N16/32/64; reference P1 meshes128/192. Fixed contrast100 example. P1 differences are not rigorous error bounds; no singular exponent or universal MG/AMG winner is asserted.
- [Rotated diffusion: full-tensor Q1, MG and AMG — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/rotated-anisotropic-diffusion/?lang=en#rotated-anisotropic-diffusion-en-validation>)

  u=xy,f=-2Kxy patch, analytic-flux source, integrated L2/energy error,4/6point quadrature sensitivity and direct-solve comparison.
- [Rotated diffusion: full-tensor Q1, MG and AMG](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-rotated-anisotropic-diffusion-en>)
  relation: same-problem
  reference_kind: manufactured

  Manufactured solution Unit square, zero Dirichlet, K=R(pi/6)diag(1,.01)R^T, exact sin(pi x)sin(pi y), N16/32/64. One angle/anisotropy only. Scalar TPFA is not extended to rotated tensors; arbitrary-tensor robustness is not established.

## Code and validation

- [Checkerboard diffusion: shared flux, MG and AMG](<https://hrkoyama.github.io/numerical-methods-atlas/validation/checkerboard-diffusion/?lang=en>)
  availability: run

  Compare discontinuous-coefficient FV with independent P1 reference fields, separating linear-system residual/forward errors from continuum error.
- [Rotated diffusion: full-tensor Q1, MG and AMG](<https://hrkoyama.github.io/numerical-methods-atlas/validation/rotated-anisotropic-diffusion/?lang=en>)
  availability: run

  Retain nonzero Kxy in the Q1 weak form and compare analytic refinement with MG/AMG convergence for the same matrix.
