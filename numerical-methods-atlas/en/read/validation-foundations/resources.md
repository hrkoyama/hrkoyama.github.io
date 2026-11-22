# AMG, factorizations, eigenvalues and quadrature

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-foundations/

Resources explicitly registered to the methods, problems and executions of this chapter.

## Methods

- [QR, SVD and least squares](<https://hrkoyama.github.io/numerical-methods-atlas/methods/qr-svd/?lang=en>)

  Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.
- [Krylov eigenvalue solvers](<https://hrkoyama.github.io/numerical-methods-atlas/methods/eigensolvers/?lang=en>)

  Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.
- [Gaussian and adaptive quadrature](<https://hrkoyama.github.io/numerical-methods-atlas/methods/quadrature/?lang=en>)

  Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.
- [Algebraic multigrid / AMG](<https://hrkoyama.github.io/numerical-methods-atlas/methods/amg/?lang=en>)
- [QR, SVD and least squares](<https://hrkoyama.github.io/numerical-methods-atlas/methods/qr-svd/?lang=en>)
- [Krylov eigenvalue solvers](<https://hrkoyama.github.io/numerical-methods-atlas/methods/eigensolvers/?lang=en>)
- [Gaussian and adaptive quadrature](<https://hrkoyama.github.io/numerical-methods-atlas/methods/quadrature/?lang=en>)

## Equations

- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/sa-amg/?lang=en#sa-amg-en-algorithm>)

  A graph based on row-relative off-diagonal strength supplies greedy star aggregates; leftover nodes attach to adjacent aggregates. Smooth tentative T via P=(I−ωD⁻¹A)T with ω=4/(3ρ̄), where ρ̄ bounds the absolute row sums of D⁻¹A. Coarse operators are PᵀAP. V-cycles use two pre/post Jacobi sweeps and a terminal dense direct solve. This is a small adopted SA variant, not every construction or convergence theorem in the original paper.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/qr-svd-factorization/?lang=en#qr-svd-factorization-en-algorithm>)

  Householder reflectors triangularize R while accumulating Q. The SVD repeatedly rotates column pairs toward orthogonality and uses their resulting lengths as singular values; it does not diagonalize AᵀA. Least squares uses triangular back substitution for QR and truncated compact SVD for deficient rank.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/krylov-eigenvalues/?lang=en#krylov-eigenvalues-en-algorithm>)

  Lanczos uses its three-term recurrence plus two passes of full reorthogonalization; Arnoldi uses two-pass modified Gram–Schmidt. Only the small projected T/H is solved by NumPy eigh/eig before lifting Ritz vectors. A full dense solve of the original matrix is used only on the reference side.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/gauss-adaptive-quadrature/?lang=en#gauss-adaptive-quadrature-en-algorithm>)

  Golub–Welsch obtains nodes from a symmetric Jacobi matrix and weights from twice the squared first eigenvector components. Adaptive Simpson bisects intervals and allocates tolerances using |Sleft+Sright−Swhole|/15 as a local estimate. Evaluation and depth limits report unmet targets explicitly.

## Problem figures

- [Householder QR and one-sided Jacobi SVD: orthogonality, rank and least squares](<https://hrkoyama.github.io/numerical-methods-atlas/problems/matrix-factorization/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/results/qr-svd-factorization.png
- [Lanczos and Arnoldi: convergence of Ritz values and eigenpair residuals](<https://hrkoyama.github.io/numerical-methods-atlas/problems/krylov-spectrum/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/results/krylov-eigenvalues.png
- [Gauss–Legendre and adaptive quadrature: exactness, error estimates and budgets](<https://hrkoyama.github.io/numerical-methods-atlas/problems/quadrature-moments/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/results/gauss-adaptive-quadrature.png
- [Matrix-based AMG: distinguish residual and solution error](<https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/results/sa-amg.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/results/sa-amg.png
- [Householder QR and one-sided Jacobi SVD: orthogonality, rank and least squares](<https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/results/qr-svd-factorization.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/results/qr-svd-factorization.png
- [Lanczos and Arnoldi: convergence of Ritz values and eigenpair residuals](<https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/results/krylov-eigenvalues.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/results/krylov-eigenvalues.png
- [Gauss–Legendre and adaptive quadrature: exactness, error estimates and budgets](<https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/results/gauss-adaptive-quadrature.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/results/gauss-adaptive-quadrature.png

## Exact / reference solutions

- [Householder QR and one-sided Jacobi SVD: orthogonality, rank and least squares — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/matrix-factorization/?lang=en#references-en>)

  Check independent NumPy/SciPy references, reconstruction, orthogonality, singular values, rank and least-squares residuals. This is linear-algebra validation rather than a PDE reference-solution card. A separate release varies conditioning, right-hand-side perturbations and numerical-rank thresholds while separating residual from coefficient forward error. Distinguish LAPACK from high-precision references built from actual binary input; no general QR/SVD or arbitrary ill-conditioned-matrix guarantee is implied.
- [Lanczos and Arnoldi: convergence of Ritz values and eigenpair residuals — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/krylov-spectrum/?lang=en#references-en>)

  Check independent eigenvalue references together with Ritz/eigenpair residuals, orthogonality and iterative convergence. A separate release separates spectral spacing, nonnormality and Krylov dimension, distinguishing small residuals from true eigenvalue errors. A clustered-subspace comparison does not certify individual vectors or another physical model.
- [Gauss–Legendre and adaptive quadrature: exactness, error estimates and budgets — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/quadrature-moments/?lang=en#references-en>)

  Use known polynomial integrals and independent quadrature references to check exactness, estimated errors and evaluation budgets. A separate release compares rule order, tolerance and cancellation sensitivity while distinguishing true integration error from the internal estimate. A missed narrow bump is an intended diagnostic; passing that diagnostic does not mean the integral estimate succeeded.
- [Matrix-based AMG: distinguish residual and solution error — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/sa-amg/?lang=en#sa-amg-en-validation>)

  Store normalized residuals, relative solution differences against SciPy spsolve, discrete-L²-type continuum errors, observed order and operator complexity. A randomly permuted matrix is also checked against a direct solution to expose hidden geometric ordering assumptions. A zero cycle budget reports nonconvergence.
- [Poisson / manufactured sine](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-poisson-manufactured-en>)
  relation: related-model
  reference_kind: manufactured

  Manufactured solution Zero Dirichlet endpoints. The forcing is chosen from the target solution; this is not an arbitrary-source Poisson solution. The card is 1D sin(πx); this test is 2D sin(πx)sin(πy). Dimension, forcing and FEM error norms differ.
- [Householder QR and one-sided Jacobi SVD: orthogonality, rank and least squares — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/qr-svd-factorization/?lang=en#qr-svd-factorization-en-validation>)

  Compare QR/SVD relative reconstruction, Q/U/V orthogonality, singular values from SciPy LAPACK gesdd, least-squares solutions/ranks from gelsd/gelsy and normal-equation stationarity residuals. Singular-vector signs are not compared; zero matrices and budget exhaustion are tested.
- [Lanczos and Arnoldi: convergence of Ritz values and eigenpair residuals — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/krylov-eigenvalues/?lang=en#krylov-eigenvalues-en-validation>)

  Store ||Av−λv||₂, differences from independently solved dense eigenvalues and basis orthogonality; verify final improvement as Krylov dimension grows. Nonsymmetric Ritz convergence is not assumed monotone. Tests include identity-matrix happy breakdown, zero-start rejection and insufficient dimension budgets.
- [Gauss–Legendre and adaptive quadrature: exactness, error estimates and budgets — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/gauss-adaptive-quadrature/?lang=en#gauss-adaptive-quadrature-en-validation>)

  Measure polynomial moments for every chosen order, node/weight differences from SciPy roots_legendre, order refinement for the analytic exponential integral, and agreement with analytic arctangent and SciPy quad references. Store evaluation counts/errors as tolerance tightens; test forced exhaustion after five evaluations and nonfinite integrands.

## Code and validation

- [Householder QR and one-sided Jacobi SVD: orthogonality, rank and least squares](<https://hrkoyama.github.io/numerical-methods-atlas/validation/qr-svd-factorization/?lang=en>)
  availability: run

  Original Householder QR and one-sided Jacobi SVD for real tall matrices are checked on ordinary, 10⁶-column-scaled and rank-deficient inputs, against separate LAPACK singular values and minimum-norm least-squares solutions.
- [QR/SVD: prescribed spectra, perturbation gain and numerical rank](<https://hrkoyama.github.io/numerical-methods-atlas/validation/qr-svd-conditioning/?lang=en>)
  availability: run

  Vary condition number from 1 to 2³⁶ for exactly representable 16×4 dyadic matrices, separating reconstruction from forward solution error. Compare LAPACK and separately executed 80/120-digit references for the actual binary64 inputs.
- [Lanczos and Arnoldi: convergence of Ritz values and eigenpair residuals](<https://hrkoyama.github.io/numerical-methods-atlas/validation/krylov-eigenvalues/?lang=en>)
  availability: run

  Original Lanczos and Arnoldi on symmetric/nonsymmetric 32×32 and 48×48 matrices measure convergence of the largest-real-part eigenpair over Krylov dimensions 4, 8 and 16, against independent full-matrix LAPACK references.
- [Krylov eigenvalues: cluster subspaces and nonnormal sensitivity](<https://hrkoyama.github.io/numerical-methods-atlas/validation/krylov-eigen-conditioning/?lang=en>)
  availability: run

  Measure Lanczos and Arnoldi with dimensions4/8/16/32 on 48-dimensional clustered symmetric and strongly nonnormal triangular matrices. Distinguish residual, forward error, eigenvalue condition number and invariant subspace.
- [Gauss–Legendre and adaptive quadrature: exactness, error estimates and budgets](<https://hrkoyama.github.io/numerical-methods-atlas/validation/gauss-adaptive-quadrature/?lang=en>)
  availability: run

  Construct Gaussian nodes/weights from the Legendre recurrence and test polynomial moments through degree 2n−1 and an exponential. Adaptive Simpson integrates exponential and Lorentzian peaks, against analytic integrals and independent QUADPACK.
- [Quadrature: narrow peaks, cancellation, endpoints and estimator blind spots](<https://hrkoyama.github.io/numerical-methods-atlas/validation/quadrature-conditioning/?lang=en>)
  availability: run

  Vary Gauss order and adaptive tolerance on narrow Lorentz peaks, a square-root endpoint, severe cancellation, a zero integral and a deliberately missed compact bump, using analytic integrals and QUADPACK.
- [Matrix-based AMG: distinguish residual and solution error](<https://hrkoyama.github.io/numerical-methods-atlas/validation/sa-amg/?lang=en>)
  availability: run

  Build a smoothed-aggregation hierarchy from an SPD matrix alone and run V-cycles. Problems with 7², 15² and 31² unknowns distinguish independent sparse direct solutions, analytic discrete sine modes and second-order convergence to the continuum solution.
