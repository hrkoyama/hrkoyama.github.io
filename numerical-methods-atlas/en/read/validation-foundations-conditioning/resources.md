# Numerical foundations: conditioning, residuals, convergence and independent references

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-foundations-conditioning/

Resources explicitly registered to the methods, problems and executions of this chapter.

## Methods

- [Algebraic multigrid / AMG](<https://hrkoyama.github.io/numerical-methods-atlas/methods/amg/?lang=en>)
- [QR, SVD and least squares](<https://hrkoyama.github.io/numerical-methods-atlas/methods/qr-svd/?lang=en>)
- [Krylov eigenvalue solvers](<https://hrkoyama.github.io/numerical-methods-atlas/methods/eigensolvers/?lang=en>)
- [Gaussian and adaptive quadrature](<https://hrkoyama.github.io/numerical-methods-atlas/methods/quadrature/?lang=en>)

## Equations

- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/amg-conditioning/?lang=en#amg-conditioning-en-algorithm>)

  Reuse the earlier MIT-licensed Atlas educational smoothed-aggregation AMG in a separate source release. Matrix-only hierarchy setup uses strength .08, Jacobi smoothing, fixed relative tolerance 10⁻¹⁰ and at most 180 V-cycles. Sine-transform spectral inversion is reference-side only.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/qr-svd-conditioning/?lang=en#qr-svd-conditioning-en-algorithm>)

  Implement Householder QR, one-sided Jacobi SVD and triangular back substitution. Vary rank cutoffs 10⁻⁸/10⁻¹²/10⁻¹⁴ and compare with LAPACK solutions using the same truncation convention. No executed normal-equations comparison is added.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/krylov-eigen-conditioning/?lang=en#krylov-eigen-conditioning-en-algorithm>)

  Use fully reorthogonalized Lanczos and two-pass MGS Arnoldi; only the small projected matrix is solved densely. Compare QR-spanned top-two subspace projectors, invariant under signs and cluster rotations.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/quadrature-conditioning/?lang=en#quadrature-conditioning-en-algorithm>)

  Implement Golub–Welsch nodes/weights and adaptive Simpson with a local difference/15 estimate. Companion checks use x=t² for the endpoint and a known-support split for the narrow bump; these are not general automatic rescue mechanisms.

## Problem figures

- [AMG: conditioning, anisotropy, residual and forward error](<https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/results/amg-conditioning.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/results/amg-conditioning.png
- [QR/SVD: prescribed spectra, perturbation gain and numerical rank](<https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/results/qr-svd-conditioning.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/results/qr-svd-conditioning.png
- [Krylov eigenvalues: cluster subspaces and nonnormal sensitivity](<https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/results/krylov-eigen-conditioning.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/results/krylov-eigen-conditioning.png
- [Quadrature: narrow peaks, cancellation, endpoints and estimator blind spots](<https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/results/quadrature-conditioning.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/results/quadrature-conditioning.png

## Exact / reference solutions

- [AMG: conditioning, anisotropy, residual and forward error — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/amg-conditioning/?lang=en#amg-conditioning-en-validation>)

  Store true residual, forward error, DST agreement, operator complexity and complete histories. Perturb a maximal-eigenmode RHS in the minimal-eigenmode direction and check the predicted relative amplification κ₂ with direct solves. Isotropic runs must converge; the predeclared anisotropy stress policy permits honestly reported budget exhaustion. A one-cycle control detects nonconvergence.
- [QR/SVD: prescribed spectra, perturbation gain and numerical rank — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/qr-svd-conditioning/?lang=en#qr-svd-conditioning-en-validation>)

  Save reconstruction, orthogonality, singular values, solution perturbations, least-squares stationarity and an exact rank-two control. The mpmath1.3.0 SVD and QR reference was actually executed using integer-ratio conversions of binary inputs. Runtime SHA and completeness guards check all four inputs at both precisions and never substitute analytic truth after a mismatch.
- [Krylov eigenvalues: cluster subspaces and nonnormal sensitivity — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/krylov-eigen-conditioning/?lang=en#krylov-eigen-conditioning-en-validation>)

  Compare analytic triangular eigenvalues, SciPy dense eigenvalues and left/right eigenvector condition numbers. A separately constructed2×2 pseudoeigenpair has residual about2.5×10⁻⁸ but eigenvalue error.005 at K=1000. It is a sensitivity control, not a failure produced by the iterative solver.
- [Quadrature: narrow peaks, cancellation, endpoints and estimator blind spots — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/quadrature-conditioning/?lang=en#quadrature-conditioning-en-validation>)

  Compare roots_legendre, analytic atan integrals,2/3,the bump integral256w/315 and independent QUADPACK. Preserve QUADPACK status, estimated error, evaluation count and warning message. Cancellation uses a roundoff-aware absolute budget. When all initial five bump samples vanish, expose estimated error0 versus actual error about.00813.

## Code and validation

- [AMG: conditioning, anisotropy, residual and forward error](<https://hrkoyama.github.io/numerical-methods-atlas/validation/amg-conditioning/?lang=en>)
  availability: run

  Separate condition number from anisotropy on SPD systems of 49, 225 and 961 unknowns. Compare analytic spectra, independent sparse direct solutions and DST diagonalization, and measure how residual translates to forward error.
- [QR/SVD: prescribed spectra, perturbation gain and numerical rank](<https://hrkoyama.github.io/numerical-methods-atlas/validation/qr-svd-conditioning/?lang=en>)
  availability: run

  Vary condition number from 1 to 2³⁶ for exactly representable 16×4 dyadic matrices, separating reconstruction from forward solution error. Compare LAPACK and separately executed 80/120-digit references for the actual binary64 inputs.
- [Krylov eigenvalues: cluster subspaces and nonnormal sensitivity](<https://hrkoyama.github.io/numerical-methods-atlas/validation/krylov-eigen-conditioning/?lang=en>)
  availability: run

  Measure Lanczos and Arnoldi with dimensions4/8/16/32 on 48-dimensional clustered symmetric and strongly nonnormal triangular matrices. Distinguish residual, forward error, eigenvalue condition number and invariant subspace.
- [Quadrature: narrow peaks, cancellation, endpoints and estimator blind spots](<https://hrkoyama.github.io/numerical-methods-atlas/validation/quadrature-conditioning/?lang=en>)
  availability: run

  Vary Gauss order and adaptive tolerance on narrow Lorentz peaks, a square-root endpoint, severe cancellation, a zero integral and a deliberately missed compact bump, using analytic integrals and QUADPACK.
