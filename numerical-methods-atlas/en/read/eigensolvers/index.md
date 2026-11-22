# Krylov eigenvalue solvers

Krylov eigensolvers approximate a few eigenpairs through a small subspace instead of diagonalizing a large matrix in full. Arnoldi, symmetric Lanczos and shift-invert require different assumptions.

## Problem and representative equations

Build Kₘ(A,v)=span{v,Av,…,Aᵐ⁻¹v}. Arnoldi gives an orthonormal Vₘ and upper-Hessenberg Hₘ. Solve Hₘy=θy and set x=Vₘy. The last Arnoldi vector and hₘ₊₁,ₘ give the Ritz residual.

$$
AV_m=V_mH_m+h_{m+1,m}v_{m+1}e_m^T,\qquad \|Ax-\theta x\|_2=|h_{m+1,m}e_m^Ty|\quad(\|y\|_2=1).
$$

## Algorithm

Expand the basis using matrix-vector products and orthogonalization, solve the projected eigenproblem and restart when needed. Hermitian matrices permit a Lanczos three-term recurrence. Shift-invert targets interior eigenvalues but each inverse action requires a linear solve.

## Conditions and pitfalls

Finite-precision loss of orthogonality can create ghost duplicates. For nonnormal matrices, a small residual need not imply a comparably small eigenvalue error. State B and the inner product in generalized problems Ax=λBx, and assess inner-solve tolerances for shift-invert.

A small eigen-residual supplies backward-error information about an eigenpair of a nearby matrix; it need not imply small eigenvalue or eigenvector forward error for a nonnormal matrix. Individual-vector matching can be unstable in a close cluster, where principal angles between invariant subspaces can be more appropriate.

## What to check

Check scaled residuals ∥Ax−θx∥/(∥A∥+|θ|), orthogonality, known eigenpairs and clustered/repeated eigenvalues. For symmetric cases compare Rayleigh quotients, and record restarts and initial-vector sensitivity.

The added release separates eigenvalue spacing from nonnormality on small matrices and compares eigenvalue/subspace errors with independent references as Krylov dimension and residual vary. Passing a residual check alone is not presented as an accurate true eigenvalue. Report conditioning alongside measured errors in clustered and nonnormal controls; no guarantee for arbitrary large nonsymmetric systems is implied. Projected solves and dense references may share LAPACK infrastructure and are not described as fully independent backends. Analytic eigenvalues and constructed pseudoeigenpair controls provide additional checks.

## Fixed-input examples and diagnostic controls

Distinguish the scope established by acceptance checks from a general mathematical guarantee; preserve historical inputs, measurements and criteria.

### Lanczos and Arnoldi: convergence of Ritz values and eigenpair residuals

Fixed-target computation

Original Lanczos and Arnoldi on symmetric/nonsymmetric 32×32 and 48×48 matrices measure convergence of the largest-real-part eigenpair over Krylov dimensions 4, 8 and 16, against independent full-matrix LAPACK references.

Unrestarted small-matrix educational examples with separated extreme eigenpairs. Interior/clustered eigenvalues, very large sparse matrices, strong nonnormality, shift-invert and implicitly restarted Arnoldi are outside scope. A small eigenpair residual alone is not treated as a rigorous eigenvalue-error bound for nonnormal matrices.

[Input, results and acceptance](/numerical-methods-atlas/validation/krylov-eigenvalues/?lang=en) · [Method and sources](/numerical-methods-atlas/en/read/validation-foundations/#krylov-eigenvalues) · [Code run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/run.py) · [Code solvers.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/solvers.py) · [Tests test_foundations.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/test_foundations.py) · [ZIP](/code/validated-examples/2026-11-22/foundations/atlas-foundations-2026-11-22.zip) · [Results](/code/validated-examples/2026-11-22/foundations/results/result.json) · [Rerun receipt](/code/validated-examples/2026-11-22/foundations/verification.json)

### Krylov eigenvalues: cluster subspaces and nonnormal sensitivity

Fixed-target computation

Measure Lanczos and Arnoldi with dimensions4/8/16/32 on 48-dimensional clustered symmetric and strongly nonnormal triangular matrices. Distinguish residual, forward error, eigenvalue condition number and invariant subspace.

NumPy projected solves and SciPy dense references may share LAPACK infrastructure and are not claimed fully independent backends. Analytic eigenvalues and constructed controls provide additional checks. Restarting, interior eigenvalues, large sparse systems and universal monotonic convergence are outside scope.

[Input, results and acceptance](/numerical-methods-atlas/validation/krylov-eigen-conditioning/?lang=en) · [Method and sources](/numerical-methods-atlas/en/read/validation-foundations-conditioning/#krylov-eigen-conditioning) · [Code run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/run.py) · [Code experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/experiments.py) · [Code fixtures.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/fixtures.py) · [Code mpmath_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/mpmath_reference.py) · [Code solvers.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/solvers.py) · [Tests test_conditioning.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/test_conditioning.py) · [ZIP](/code/validated-examples/2026-11-22/foundations-conditioning/atlas-foundations-conditioning-2026-11-22.zip) · [Results](/code/validated-examples/2026-11-22/foundations-conditioning/results/result.json) · [Rerun receipt](/code/validated-examples/2026-11-22/foundations-conditioning/verification.json)

## Publication scope

Historical inputs, measurements and tolerances are preserved. Additional conditioning, residual and convergence checks have a separate scoped release. Passing a diagnostic control can mean that its intended limitation was observed; it does not establish general success or reproduction of an entire paper.

## Sources

- W. E. Arnoldi (1951). The principle of minimized iterations in the solution of the matrix eigenvalue problem. https://doi.org/10.1090/qam/42792
- C. Lanczos (1950). An iteration method for the solution of the eigenvalue problem of linear differential and integral operators. https://doi.org/10.6028/jres.045.026
- LAPACK authors (1999). Error Bounds for the Nonsymmetric Eigenproblem; Overview. https://www.netlib.org/lapack/lug/node91.html
