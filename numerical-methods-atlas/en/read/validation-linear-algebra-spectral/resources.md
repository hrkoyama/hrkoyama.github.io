# Linear algebra: factorizations, saddle systems, restarting and mass eigenpairs

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-linear-algebra-spectral/

Resources explicitly registered to the methods, problems and executions of this chapter. Small fixed matrices compare factorization and refinement, symmetric-indefinite solves, restarted eigenpairs and a consistent-mass string. Independent references distinguish residual from solution error, algebraic from discretization error, and counted operator actions.

## Methods

- [Partial-pivot LU and mixed-precision refinement](<https://hrkoyama.github.io/numerical-methods-atlas/methods/lu-partial-pivoting/?lang=en>)
- [Cholesky factorization and triangular solves](<https://hrkoyama.github.io/numerical-methods-atlas/methods/cholesky/?lang=en>)
- [Educational MINRES for symmetric-indefinite systems](<https://hrkoyama.github.io/numerical-methods-atlas/methods/minres/?lang=en>)
- [Generalized eigenpairs with SciPy LOBPCG](<https://hrkoyama.github.io/numerical-methods-atlas/methods/lobpcg/?lang=en>)
- [Partial-pivot LU and mixed-precision refinement](<https://hrkoyama.github.io/numerical-methods-atlas/methods/lu-partial-pivoting/?lang=en>)

  Original implementations of LU with partial pivoting, lower Cholesky factorization and triangular substitution.
- [Cholesky factorization and triangular solves](<https://hrkoyama.github.io/numerical-methods-atlas/methods/cholesky/?lang=en>)

  Original implementations of LU with partial pivoting, lower Cholesky factorization and triangular substitution.
- [Educational MINRES for symmetric-indefinite systems](<https://hrkoyama.github.io/numerical-methods-atlas/methods/minres/?lang=en>)

  Stored-basis Lanczos least squares provides the educational MINRES variant; GMRES uses two-pass modified Gram-Schmidt. An SPD congruence preserves symmetry. The internal target is min(configured rtol, fixed forward-error limit / kappa_infinity), using only the matrix. The independent solution is not a stopping input.
- [Restarted GMRES](<https://hrkoyama.github.io/numerical-methods-atlas/methods/gmres/?lang=en>)

  Stored-basis Lanczos least squares provides the educational MINRES variant; GMRES uses two-pass modified Gram-Schmidt. An SPD congruence preserves symmetry. The internal target is min(configured rtol, fixed forward-error limit / kappa_infinity), using only the matrix. The independent solution is not a stopping input.
- [Krylov eigenvalue solvers](<https://hrkoyama.github.io/numerical-methods-atlas/methods/eigensolvers/?lang=en>)

  Two-pass Arnoldi is explicitly restarted from one Ritz vector. Original LU routines perform the shifted solves, and stopping uses the original eigenproblem.
- [Krylov eigenvalue solvers](<https://hrkoyama.github.io/numerical-methods-atlas/methods/eigensolvers/?lang=en>)

  Elementwise K and M assembly, M-inner-product Krylov iteration on K^-1 M, and actual SciPy LOBPCG with a small exact-K-inverse preconditioner. LOBPCG starts from {1, x^3, x^6}; degree-plus-two images avoid the structural rank defect of {1, x, x^2}. The same M is applied through a qualified einsum LinearOperator, avoiding the dense-B adapter. The eigensolver itself remains SciPy LOBPCG.
- [Generalized eigenpairs with SciPy LOBPCG](<https://hrkoyama.github.io/numerical-methods-atlas/methods/lobpcg/?lang=en>)

  Elementwise K and M assembly, M-inner-product Krylov iteration on K^-1 M, and actual SciPy LOBPCG with a small exact-K-inverse preconditioner. LOBPCG starts from {1, x^3, x^6}; degree-plus-two images avoid the structural rank defect of {1, x, x^2}. The same M is applied through a qualified einsum LinearOperator, avoiding the dense-B adapter. The eigensolver itself remains SciPy LOBPCG.
- [Restarted GMRES](<https://hrkoyama.github.io/numerical-methods-atlas/methods/gmres/?lang=en>)
- [Krylov eigenvalue solvers](<https://hrkoyama.github.io/numerical-methods-atlas/methods/eigensolvers/?lang=en>)

## Equations

- [Finite-dimensional linear systems and factorizations](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#finite-dimensional-linear-system-en>)

  Finite matrices A and right-hand sides b define algebraic problems. Fixed LU, Cholesky, refinement and symmetric-indefinite saddle controls are distinct from continuum PDE solutions. Fixed SPD matrix of size 12, a nearly singular rank-one matrix of size 8, Hilbert matrix of size 5 and Wilkinson matrix of size 12. Factors and triangular corrections use binary32; residuals use binary64, with five updates.
- [Finite-dimensional linear systems and factorizations](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#finite-dimensional-linear-system-en>)

  Finite matrices A and right-hand sides b define algebraic problems. Fixed LU, Cholesky, refinement and symmetric-indefinite saddle controls are distinct from continuum PDE solutions. Algebraic mixed-Poisson/Stokes-type blocks with velocity sizes 12 and 24 and pressure sizes 5 and 11. The common original-system residual tolerance is 1e-9.
- [Finite-dimensional matrix eigenproblems](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#finite-dimensional-eigenproblem-en>)

  The primary case is a fixed 31 x 31 symmetric standard eigenproblem. Its discrete spectrum provides the reference; continuum PDE spatial convergence is not claimed. A fixed Dirichlet Laplacian of size 31, restart lengths 8 and 16, and at most 40 cycles. Compare the untransformed problem with shifts 0 and 950.
- [Fixed-end string eigenvalues and consistent-mass FEM](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#dirichlet-string-eigenproblem-en>)

  A unit-string normal-mode eigenproblem separates consistent-mass P1 algebraic error from continuum discretization error. No time evolution is performed. A unit string with unit tension and density and homogeneous Dirichlet endpoints. Use 15, 31 and 63 interior nodes and the lowest three eigenpairs.
- [Finite-dimensional linear systems and factorizations](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#finite-dimensional-linear-system-en>)

  Finite matrices A and right-hand sides b define algebraic problems. Fixed LU, Cholesky, refinement and symmetric-indefinite saddle controls are distinct from continuum PDE solutions.
- [Finite-dimensional matrix eigenproblems](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#finite-dimensional-eigenproblem-en>)

  The primary case is a fixed 31 x 31 symmetric standard eigenproblem. Its discrete spectrum provides the reference; continuum PDE spatial convergence is not claimed.
- [Fixed-end string eigenvalues and consistent-mass FEM](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#dirichlet-string-eigenproblem-en>)

  A unit-string normal-mode eigenproblem separates consistent-mass P1 algebraic error from continuum discretization error. No time evolution is performed.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/pivoted-direct-refinement/?lang=en#pivoted-direct-refinement-en-algorithm>)

  Original implementations of LU with partial pivoting, lower Cholesky factorization and triangular substitution.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/symmetric-saddle-minres/?lang=en#symmetric-saddle-minres-en-algorithm>)

  Stored-basis Lanczos least squares provides the educational MINRES variant; GMRES uses two-pass modified Gram-Schmidt. An SPD congruence preserves symmetry. The internal target is min(configured rtol, fixed forward-error limit / kappa_infinity), using only the matrix. The independent solution is not a stopping input.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/restarted-shift-invert/?lang=en#restarted-shift-invert-en-algorithm>)

  Two-pass Arnoldi is explicitly restarted from one Ritz vector. Original LU routines perform the shifted solves, and stopping uses the original eigenproblem.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/fem-mass-eigen/?lang=en#fem-mass-eigen-en-algorithm>)

  Elementwise K and M assembly, M-inner-product Krylov iteration on K^-1 M, and actual SciPy LOBPCG with a small exact-K-inverse preconditioner. LOBPCG starts from {1, x^3, x^6}; degree-plus-two images avoid the structural rank defect of {1, x, x^2}. The same M is applied through a qualified einsum LinearOperator, avoiding the dense-B adapter. The eigensolver itself remains SciPy LOBPCG.

## Problem figures

- [Pivoted LU, Cholesky and iterative refinement](<https://hrkoyama.github.io/numerical-methods-atlas/problems/pivoted-direct-refinement/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/pivoted-direct-refinement-preview.png
- [Symmetric saddle systems and Schur preconditioning](<https://hrkoyama.github.io/numerical-methods-atlas/problems/symmetric-saddle-minres/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/symmetric-saddle-minres-preview.png
- [Explicitly restarted Krylov and interior eigenvalues](<https://hrkoyama.github.io/numerical-methods-atlas/problems/restarted-shift-invert/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/restarted-shift-invert-preview.png
- [Consistent-mass FEM string eigenpairs](<https://hrkoyama.github.io/numerical-methods-atlas/problems/fem-mass-eigen/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/fem-mass-eigen-preview.png
- [Pivoted LU, Cholesky and iterative refinement](<https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/pivoted-direct-refinement.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/pivoted-direct-refinement.png
- [Symmetric saddle systems and Schur preconditioning](<https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/symmetric-saddle-minres.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/symmetric-saddle-minres.png
- [Explicitly restarted Krylov and interior eigenvalues](<https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/restarted-shift-invert.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/restarted-shift-invert.png
- [Consistent-mass FEM string eigenpairs](<https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/fem-mass-eigen.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/fem-mass-eigen.png

## Exact / reference solutions

- [Pivoted LU, Cholesky and iterative refinement — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/pivoted-direct-refinement/?lang=en#references-en>)

  Exact-rational solutions for the actual binary64 inputs and separate LAPACK DGESV/DPOSV comparisons. Conditioning, forward error and backward error are reported separately. Each saved reference component is the exact Fraction solution rounded to binary64.
- [Pivoted LU and Cholesky: exact-rational references for actual binary input](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-pivoted-direct-refinement-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference The four fixed matrices use the actual binary64 A and b, converted exactly to Fractions. Rational elimination is exact, followed by a final binary64 rounding. Separate LAPACK comparisons share some numerical infrastructure. This is not a forward-accuracy guarantee for arbitrary ill-conditioned matrices. Small fixed examples only; convergence of mixed-precision refinement is not guaranteed for arbitrary matrices.
- [Symmetric saddle systems and Schur preconditioning — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/symmetric-saddle-minres/?lang=en#references-en>)

  Global LAPACK solutions, the analytic ideal-Schur spectrum and an explicit negative-curvature control for CG.
- [Symmetric saddles: independent dense solutions and the ideal-Schur spectrum](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-symmetric-saddle-minres-en>)
  relation: same-problem
  reference_kind: numerical-reference

  Finite-grid numerical reference Algebraic saddles A=[[H,B^T],[B,0]] use velocity sizes 12 and 24 and pressure sizes 5 and 11. Explicit dense SPD ideal-Schur controls compare the original residual separately with dense-solution error. This is not a Stokes boundary-value PDE. A dense, ideal-Schur educational control, not a complete Stokes PDE solver or a scalable approximate preconditioner.
- [Explicitly restarted Krylov and interior eigenvalues — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/restarted-shift-invert/?lang=en#references-en>)

  The known discrete sine spectrum and an independent global LAPACK comparison. Shift-solve, Krylov and original-residual actions are counted separately.
- [Restarting and shift-invert: the closed spectrum of a fixed discrete matrix](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-restarted-shift-invert-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference A fixed 31 x 31 Dirichlet tridiagonal matrix with h=1/32, restart lengths 8 and 16, and shifts none/0/950. The references are eigenvalues of this finite matrix, not a continuum PDE grid-convergence study. One eigenpair of a real symmetric matrix only. No implicit restarting, Krylov-Schur, locking, or general nonnormal or clustered-spectrum capability is claimed.
- [Consistent-mass FEM string eigenpairs — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/fem-mass-eigen/?lang=en#references-en>)

  Generalized dense eigh, an independent discrete spectrum and refinement toward (j*pi)^2. M-orthogonality and original residuals are distinct quantities.
- [Consistent-mass P1 string: closed discrete and continuum eigenvalues](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-fem-mass-eigen-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference Unit length, tension and density, homogeneous Dirichlet endpoints, 15/31/63 interior nodes, and the lowest three eigenpairs. Compare closed discrete eigenvalues with generalized dense LAPACK, then measure error relative to (j*pi)^2 separately. Displayed vectors are saved numerical modes with arbitrary sign. A small 1D string only. If SciPy raises before returning, inputs are retained; unreturned internal iterates are not claimed to be saved. The 35 component checks do not replace the four full scientific cases.
- [Pivoted LU and Cholesky: exact-rational references for actual binary input](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-pivoted-direct-refinement-en>)
  reference_kind: analytic

  Analytic reference The four fixed matrices use the actual binary64 A and b, converted exactly to Fractions. Rational elimination is exact, followed by a final binary64 rounding. Separate LAPACK comparisons share some numerical infrastructure. This is not a forward-accuracy guarantee for arbitrary ill-conditioned matrices.
- [Symmetric saddles: independent dense solutions and the ideal-Schur spectrum](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-symmetric-saddle-minres-en>)
  reference_kind: numerical-reference

  Finite-grid numerical reference Algebraic saddles A=[[H,B^T],[B,0]] use velocity sizes 12 and 24 and pressure sizes 5 and 11. Explicit dense SPD ideal-Schur controls compare the original residual separately with dense-solution error. This is not a Stokes boundary-value PDE.
- [Restarting and shift-invert: the closed spectrum of a fixed discrete matrix](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-restarted-shift-invert-en>)
  reference_kind: analytic

  Analytic reference A fixed 31 x 31 Dirichlet tridiagonal matrix with h=1/32, restart lengths 8 and 16, and shifts none/0/950. The references are eigenvalues of this finite matrix, not a continuum PDE grid-convergence study.
- [Consistent-mass P1 string: closed discrete and continuum eigenvalues](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-fem-mass-eigen-en>)
  reference_kind: analytic

  Analytic reference Unit length, tension and density, homogeneous Dirichlet endpoints, 15/31/63 interior nodes, and the lowest three eigenpairs. Compare closed discrete eigenvalues with generalized dense LAPACK, then measure error relative to (j*pi)^2 separately. Displayed vectors are saved numerical modes with arbitrary sign.
- [Pivoted LU, Cholesky and iterative refinement — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/pivoted-direct-refinement/?lang=en#pivoted-direct-refinement-en-validation>)

  Exact-rational solutions for the actual binary64 inputs and separate LAPACK DGESV/DPOSV comparisons. Conditioning, forward error and backward error are reported separately. Each saved reference component is the exact Fraction solution rounded to binary64.
- [Pivoted LU and Cholesky: exact-rational references for actual binary input](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-pivoted-direct-refinement-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference The four fixed matrices use the actual binary64 A and b, converted exactly to Fractions. Rational elimination is exact, followed by a final binary64 rounding. Separate LAPACK comparisons share some numerical infrastructure. This is not a forward-accuracy guarantee for arbitrary ill-conditioned matrices. Small fixed examples only; convergence of mixed-precision refinement is not guaranteed for arbitrary matrices.
- [Symmetric saddle systems and Schur preconditioning — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/symmetric-saddle-minres/?lang=en#symmetric-saddle-minres-en-validation>)

  Global LAPACK solutions, the analytic ideal-Schur spectrum and an explicit negative-curvature control for CG.
- [Symmetric saddles: independent dense solutions and the ideal-Schur spectrum](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-symmetric-saddle-minres-en>)
  relation: same-problem
  reference_kind: numerical-reference

  Finite-grid numerical reference Algebraic saddles A=[[H,B^T],[B,0]] use velocity sizes 12 and 24 and pressure sizes 5 and 11. Explicit dense SPD ideal-Schur controls compare the original residual separately with dense-solution error. This is not a Stokes boundary-value PDE. A dense, ideal-Schur educational control, not a complete Stokes PDE solver or a scalable approximate preconditioner.
- [Explicitly restarted Krylov and interior eigenvalues — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/restarted-shift-invert/?lang=en#restarted-shift-invert-en-validation>)

  The known discrete sine spectrum and an independent global LAPACK comparison. Shift-solve, Krylov and original-residual actions are counted separately.
- [Restarting and shift-invert: the closed spectrum of a fixed discrete matrix](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-restarted-shift-invert-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference A fixed 31 x 31 Dirichlet tridiagonal matrix with h=1/32, restart lengths 8 and 16, and shifts none/0/950. The references are eigenvalues of this finite matrix, not a continuum PDE grid-convergence study. One eigenpair of a real symmetric matrix only. No implicit restarting, Krylov-Schur, locking, or general nonnormal or clustered-spectrum capability is claimed.
- [Consistent-mass FEM string eigenpairs — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/fem-mass-eigen/?lang=en#fem-mass-eigen-en-validation>)

  Generalized dense eigh, an independent discrete spectrum and refinement toward (j*pi)^2. M-orthogonality and original residuals are distinct quantities.
- [Consistent-mass P1 string: closed discrete and continuum eigenvalues](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-fem-mass-eigen-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference Unit length, tension and density, homogeneous Dirichlet endpoints, 15/31/63 interior nodes, and the lowest three eigenpairs. Compare closed discrete eigenvalues with generalized dense LAPACK, then measure error relative to (j*pi)^2 separately. Displayed vectors are saved numerical modes with arbitrary sign. A small 1D string only. If SciPy raises before returning, inputs are retained; unreturned internal iterates are not claimed to be saved. The 35 component checks do not replace the four full scientific cases.

## Code and validation

- [Pivoted LU, Cholesky and iterative refinement](<https://hrkoyama.github.io/numerical-methods-atlas/validation/pivoted-direct-refinement/?lang=en>)
  availability: run

  Exact-rational comparisons separate conditioning, forward and backward error, and pivot growth.
- [Symmetric saddle systems and Schur preconditioning](<https://hrkoyama.github.io/numerical-methods-atlas/validation/symmetric-saddle-minres/?lang=en>)
  availability: run

  MINRES and GMRES use the same original-system residual criterion and are checked against the ideal Schur three-point spectrum.
- [Consistent-mass FEM string eigenpairs](<https://hrkoyama.github.io/numerical-methods-atlas/validation/fem-mass-eigen/?lang=en>)
  availability: run

  Consistent-mass P1 string eigenpairs compare an M-inner-product Krylov method and actual SciPy LOBPCG with an independent discrete spectrum.
- [Explicitly restarted Krylov and interior eigenvalues](<https://hrkoyama.github.io/numerical-methods-atlas/validation/restarted-shift-invert/?lang=en>)
  availability: run

  Explicit restarting and shift-invert are compared using original eigenproblem residuals and counted operator actions.
- [Partial-pivot LU and mixed-precision refinement — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/lu-partial-pivoting/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [Cholesky factorization and triangular solves — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/cholesky/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [Educational MINRES for symmetric-indefinite systems — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/minres/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [Generalized eigenpairs with SciPy LOBPCG — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/lobpcg/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
