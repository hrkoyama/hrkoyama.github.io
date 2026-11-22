# Numerical foundations: conditioning, residuals, convergence and independent references

Compare AMG, QR/SVD, Krylov eigenvalue methods and quadrature across fixed conditioning families. Separate residuals from forward error and matrix from integral conditioning; check independent references alongside convergence limits and diagnostic blind spots.

These additional validation supplements are managed separately from the common 22-example registry. Receipts cover independent ZIP extraction, tests and every fixed input within each group. Changes of settings, methods or step sizes do not add independent physical problems.

## AMG: conditioning, anisotropy, residual and forward error

Separate condition number from anisotropy on SPD systems of 49, 225 and 961 unknowns. Compare analytic spectra, independent sparse direct solutions and DST diagonalization, and measure how residual translates to forward error.

**Methods used**

- [Algebraic multigrid / AMG](https://hrkoyama.github.io/numerical-methods-atlas/methods/amg/?lang=en) (`amg`)

**Equations**

[This example’s diagnostic and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/amg-conditioning/?lang=en#amg-conditioning-en-algorithm)

Reuse the earlier MIT-licensed Atlas educational smoothed-aggregation AMG in a separate source release. Matrix-only hierarchy setup uses strength .08, Jacobi smoothing, fixed relative tolerance 10⁻¹⁰ and at most 180 V-cycles. Sine-transform spectral inversion is reference-side only.

$$
\kappa_2(A)=\cot^2\!\left(\frac{\pi}{2(n+1)}\right)
$$

$$
\frac{\|x-\hat x\|_2}{\|x\|_2}\le\kappa_2(A)\frac{\|b-A\hat x\|_2}{\|b\|_2}
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![AMG: conditioning, anisotropy, residual and forward error: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/results/amg-conditioning.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

No separate physical test problem is assigned to this check or diagnostic. Its own diagnostic figure and validation material are provided.

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/amg-conditioning/?lang=en#amg-conditioning-en-validation)

Store true residual, forward error, DST agreement, operator complexity and complete histories. Perturb a maximal-eigenmode RHS in the minimal-eigenmode direction and check the predicted relative amplification κ₂ with direct solves. Isotropic runs must converge; the predeclared anisotropy stress policy permits honestly reported budget exhaustion. A one-cycle control detects nonconvergence.

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.
### Assumptions, units and boundaries

A=T⊗I+εI⊗T with n=7/15/31 and ε=1/.1/.01. This is a known-solution algebraic diagnostic; continuum PDE validation remains in the earlier Poisson example. At fixed square n, κ₂ is independent of ε.

**Editorial clarification**

This diagnoses algebraic matrix conditioning and iteration error, separately from the earlier Poisson manufactured-solution PDE accuracy. Anisotropy and the 2-norm condition number need not vary together on a fixed grid. Distinguish residual, solution error and an exhausted iteration budget.

### Adopted numerical method

Reuse the earlier MIT-licensed Atlas educational smoothed-aggregation AMG in a separate source release. Matrix-only hierarchy setup uses strength .08, Jacobi smoothing, fixed relative tolerance 10⁻¹⁰ and at most 180 V-cycles. Sine-transform spectral inversion is reference-side only.

$$
\kappa_2(A)=\cot^2\!\left(\frac{\pi}{2(n+1)}\right)
$$

$$
\frac{\|x-\hat x\|_2}{\|x\|_2}\le\kappa_2(A)\frac{\|b-A\hat x\|_2}{\|b\|_2}
$$

### References and validation

Store true residual, forward error, DST agreement, operator complexity and complete histories. Perturb a maximal-eigenmode RHS in the minimal-eigenmode direction and check the predicted relative amplification κ₂ with direct solves. Isotropic runs must converge; the predeclared anisotropy stress policy permits honestly reported budget exhaustion. A one-cycle control detects nonconvergence.

### Limits

Only a small constant-coefficient family is checked. Arbitrary coefficient jumps, unstructured grids, indefinite systems, optimal complexity and uniform convergence are outside scope. No claim that anisotropy necessarily increases κ₂ or monotonically worsens convergence.

### Stored measurements and decisions

```json
{
  "metrics": {
    "maximum_condition_2": 414.3450622319016,
    "maximum_actual_relative_residual": 9.213509371626832e-11,
    "maximum_actual_forward_error": 6.249776614864638e-11,
    "stress_budget_exhaustions": 0,
    "maximum_condition_gain_relative_error": 3.2097435820332976e-11
  },
  "checks": {
    "n7-eps1-true-residual": true,
    "n7-eps1-forward-bound": true,
    "n7-eps1-condition-gain": true,
    "n7-eps1-complexity": true,
    "n7-eps1-independent-dst": true,
    "n7-eps1-resolved": true,
    "n7-eps0.1-true-residual": true,
    "n7-eps0.1-forward-bound": true,
    "n7-eps0.1-condition-gain": true,
    "n7-eps0.1-complexity": true,
    "n7-eps0.1-independent-dst": true,
    "n7-eps0.1-stress-honest": true,
    "n7-eps0.01-true-residual": true,
    "n7-eps0.01-forward-bound": true,
    "n7-eps0.01-condition-gain": true,
    "n7-eps0.01-complexity": true,
    "n7-eps0.01-independent-dst": true,
    "n7-eps0.01-stress-honest": true,
    "n7-independent-spectrum": true,
    "n15-eps1-true-residual": true,
    "n15-eps1-forward-bound": true,
    "n15-eps1-condition-gain": true,
    "n15-eps1-complexity": true,
    "n15-eps1-independent-dst": true,
    "n15-eps1-resolved": true,
    "n15-eps0.1-true-residual": true,
    "n15-eps0.1-forward-bound": true,
    "n15-eps0.1-condition-gain": true,
    "n15-eps0.1-complexity": true,
    "n15-eps0.1-independent-dst": true,
    "n15-eps0.1-stress-honest": true,
    "n15-eps0.01-true-residual": true,
    "n15-eps0.01-forward-bound": true,
    "n15-eps0.01-condition-gain": true,
    "n15-eps0.01-complexity": true,
    "n15-eps0.01-independent-dst": true,
    "n15-eps0.01-stress-honest": true,
    "n15-independent-spectrum": true,
    "n31-eps1-true-residual": true,
    "n31-eps1-forward-bound": true,
    "n31-eps1-condition-gain": true,
    "n31-eps1-complexity": true,
    "n31-eps1-independent-dst": true,
    "n31-eps1-resolved": true,
    "n31-eps0.1-true-residual": true,
    "n31-eps0.1-forward-bound": true,
    "n31-eps0.1-condition-gain": true,
    "n31-eps0.1-complexity": true,
    "n31-eps0.1-independent-dst": true,
    "n31-eps0.1-stress-honest": true,
    "n31-eps0.01-true-residual": true,
    "n31-eps0.01-forward-bound": true,
    "n31-eps0.01-condition-gain": true,
    "n31-eps0.01-complexity": true,
    "n31-eps0.01-independent-dst": true,
    "n31-eps0.01-stress-honest": true,
    "n31-independent-spectrum": true,
    "short-budget-failure-explicit": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/amg-conditioning/index.json

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/atlas-foundations-conditioning-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group.

### Sources and review scope

- P. Vaněk, J. Mandel and M. Brezina (1996). Algebraic multigrid by smoothed aggregation for second and fourth order elliptic problems. https://link.springer.com/article/10.1007/BF02238511; review_level=publisher-abstract-and-metadata
- P. Vaněk, M. Brezina, J. Mandel (2001). Convergence of algebraic multigrid based on smoothed aggregation. https://ww3.math.ucla.edu/camreport/cam99-29.pdf; review_level=author-hosted original preprint abstract and opening text via official university search extraction
  Distinguish theory conditional on weak approximation and related assumptions from observations on a small matrix family; no general anisotropy robustness claim.

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## QR/SVD: prescribed spectra, perturbation gain and numerical rank

Vary condition number from 1 to 2³⁶ for exactly representable 16×4 dyadic matrices, separating reconstruction from forward solution error. Compare LAPACK and separately executed 80/120-digit references for the actual binary64 inputs.

**Methods used**

- [QR, SVD and least squares](https://hrkoyama.github.io/numerical-methods-atlas/methods/qr-svd/?lang=en) (`qr-svd`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/qr-svd-conditioning/?lang=en#qr-svd-conditioning-en-algorithm)

Implement Householder QR, one-sided Jacobi SVD and triangular back substitution. Vary rank cutoffs 10⁻⁸/10⁻¹²/10⁻¹⁴ and compare with LAPACK solutions using the same truncation convention. No executed normal-equations comparison is added.

$$
A=U\operatorname{diag}(2^{-qj})V^T,\quad\kappa_2(A)=2^{3q}
$$

$$
\delta b=\eta u_{\min},\quad\delta x=\eta\sigma_{\min}^{-1}v_{\min}
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![QR/SVD: prescribed spectra, perturbation gain and numerical rank: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/results/qr-svd-conditioning.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Householder QR and one-sided Jacobi SVD: orthogonality, rank and least squares](https://hrkoyama.github.io/numerical-methods-atlas/problems/matrix-factorization/?lang=en) (`matrix-factorization`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/matrix-factorization/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/qr-svd-conditioning/?lang=en#qr-svd-conditioning-en-validation)

Save reconstruction, orthogonality, singular values, solution perturbations, least-squares stationarity and an exact rank-two control. The mpmath1.3.0 SVD and QR reference was actually executed using integer-ratio conversions of binary inputs. Runtime SHA and completeness guards check all four inputs at both precisions and never substitute analytic truth after a mismatch.

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.
### Assumptions, units and boundaries

Use Hadamard orthogonal factors U,V and sⱼ=2⁻qj for q=0/4/8/12. Fixed b=u₀ and b+2⁻⁴⁰u_min measure perturbation amplification. Individual singular vectors are nonunique for the repeated singular values at q=0.

**Editorial clarification**

Small reconstruction, orthogonality and backward errors do not ensure small forward error for an ill-conditioned problem. Distinguish the actual floating-point matrix from its intended singular values and state the numerical-rank threshold.

### Adopted numerical method

Implement Householder QR, one-sided Jacobi SVD and triangular back substitution. Vary rank cutoffs 10⁻⁸/10⁻¹²/10⁻¹⁴ and compare with LAPACK solutions using the same truncation convention. No executed normal-equations comparison is added.

$$
A=U\operatorname{diag}(2^{-qj})V^T,\quad\kappa_2(A)=2^{3q}
$$

$$
\delta b=\eta u_{\min},\quad\delta x=\eta\sigma_{\min}^{-1}v_{\min}
$$

### References and validation

Save reconstruction, orthogonality, singular values, solution perturbations, least-squares stationarity and an exact rank-two control. The mpmath1.3.0 SVD and QR reference was actually executed using integer-ratio conversions of binary inputs. Runtime SHA and completeness guards check all four inputs at both precisions and never substitute analytic truth after a mismatch.

### Limits

Some LAPACK and projected-core numerical infrastructure is shared. mpmath SVD uses separate bidiagonalization and QR iteration; mpmath least squares is a separate high-precision implementation of the same Householder family. Tiny-singular-value relative accuracy is not guaranteed for arbitrary ill-conditioned matrices.

### Stored measurements and decisions

```json
{
  "metrics": {
    "largest_condition_2": 68719476736.0,
    "maximum_backward_reconstruction": 6.074604146362075e-16,
    "maximum_forward_error": 0.0004920953373835635,
    "minimum_numerical_rank": 2,
    "reference_precision_digits": 120
  },
  "checks": {
    "q0-factorization": true,
    "q0-high-precision-spectrum": true,
    "q0-condition-aware-forward": true,
    "q0-lapack-reference": true,
    "q0-perturbation-gain": true,
    "q4-factorization": true,
    "q4-high-precision-spectrum": true,
    "q4-condition-aware-forward": true,
    "q4-lapack-reference": true,
    "q4-perturbation-gain": true,
    "q8-factorization": true,
    "q8-high-precision-spectrum": true,
    "q8-condition-aware-forward": true,
    "q8-lapack-reference": true,
    "q8-perturbation-gain": true,
    "q12-factorization": true,
    "q12-high-precision-spectrum": true,
    "q12-condition-aware-forward": true,
    "q12-lapack-reference": true,
    "q12-perturbation-gain": true,
    "cutoff1e-08-rank-aware": true,
    "cutoff1e-12-rank-aware": true,
    "cutoff1e-14-rank-aware": true,
    "exact-rank-deficiency": true,
    "sweep-budget-failure-explicit": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/qr-svd-conditioning/index.json

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/atlas-foundations-conditioning-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group.

### Sources and review scope

- A. S. Householder (1958). Unitary Triangularization of a Nonsymmetric Matrix. https://dl.acm.org/doi/10.1145/320941.320947; review_level=publisher-metadata
- J. Demmel, K. Veselić (1992). Jacobi’s Method is More Accurate than QR. https://epubs.siam.org/doi/abs/10.1137/0613074; review_level=primary publisher abstract and bibliographic metadata
  Checked the dependence of relative-accuracy statements on stopping rules and componentwise sensitivity; not a blanket accuracy guarantee for tiny singular values of arbitrary ill-conditioned matrices.
- LAPACK authors (1999). Further Details: Error Bounds for Linear Least Squares Problems. https://netlib.org/lapack/lug/node83.html; review_level=official implementation documentation, error-analysis and numerical-rank sections
  Checked backward versus forward error, the residual-angle dependence of least-squares sensitivity, and numerical-rank truncation controlled by RCOND.
- mpmath developers (2023). mpmath 1.3.0 matrix documentation and installed implementation. https://mpmath.org/doc/1.3.0/matrices.html; review_level=official matrix documentation and selected installed mpmath1.3.0 source (svd_r_raw, qr_solve), plus actual 80/120dps fixed-input execution
  SVD uses Householder bidiagonalization and a QR variant; least squares uses a separate high-precision Householder QR implementation. The latter shares the educational QR mathematical family and is not called a different algorithm family. Actual binary floating-point inputs were loaded by integer ratios and executed in a generation-only environment.

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## Krylov eigenvalues: cluster subspaces and nonnormal sensitivity

Measure Lanczos and Arnoldi with dimensions4/8/16/32 on 48-dimensional clustered symmetric and strongly nonnormal triangular matrices. Distinguish residual, forward error, eigenvalue condition number and invariant subspace.

**Methods used**

- [Krylov eigenvalue solvers](https://hrkoyama.github.io/numerical-methods-atlas/methods/eigensolvers/?lang=en) (`eigensolvers`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/krylov-eigen-conditioning/?lang=en#krylov-eigen-conditioning-en-algorithm)

Use fully reorthogonalized Lanczos and two-pass MGS Arnoldi; only the small projected matrix is solved densely. Compare QR-spanned top-two subspace projectors, invariant under signs and cluster rotations.

$$
\kappa(\lambda)=\frac{\|y\|_2\|x\|_2}{|y^*x|}
$$

$$
A=\begin{pmatrix}1&K\\0&1+\delta\end{pmatrix},\quad\|A\tilde v-\tilde\lambda\tilde v\|_2=\frac{\delta^2}{4K\sqrt{1+(\delta/(2K))^2}}
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![Krylov eigenvalues: cluster subspaces and nonnormal sensitivity: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/results/krylov-eigen-conditioning.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Lanczos and Arnoldi: convergence of Ritz values and eigenpair residuals](https://hrkoyama.github.io/numerical-methods-atlas/problems/krylov-spectrum/?lang=en) (`krylov-spectrum`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/krylov-spectrum/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/krylov-eigen-conditioning/?lang=en#krylov-eigen-conditioning-en-validation)

Compare analytic triangular eigenvalues, SciPy dense eigenvalues and left/right eigenvector condition numbers. A separately constructed2×2 pseudoeigenpair has residual about2.5×10⁻⁸ but eigenvalue error.005 at K=1000. It is a sensitivity control, not a failure produced by the iterative solver.

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.
### Assumptions, units and boundaries

Top symmetric gaps are1/.1/.01. Nonnormal matrices are actual floating-point upper-triangular inputs with K=10/1000 and known diagonal eigenvalues. Nominal spectra after floating-point similarity construction are not labelled exact truth.

**Editorial clarification**

Separate eigenpair residuals, eigenvalue/invariant-subspace errors, spectral gaps and nonnormality. A constructed sensitivity control is distinct from actual Krylov iteration output or a universal failure example.

### Adopted numerical method

Use fully reorthogonalized Lanczos and two-pass MGS Arnoldi; only the small projected matrix is solved densely. Compare QR-spanned top-two subspace projectors, invariant under signs and cluster rotations.

$$
\kappa(\lambda)=\frac{\|y\|_2\|x\|_2}{|y^*x|}
$$

$$
A=\begin{pmatrix}1&K\\0&1+\delta\end{pmatrix},\quad\|A\tilde v-\tilde\lambda\tilde v\|_2=\frac{\delta^2}{4K\sqrt{1+(\delta/(2K))^2}}
$$

### References and validation

Compare analytic triangular eigenvalues, SciPy dense eigenvalues and left/right eigenvector condition numbers. A separately constructed2×2 pseudoeigenpair has residual about2.5×10⁻⁸ but eigenvalue error.005 at K=1000. It is a sensitivity control, not a failure produced by the iterative solver.

### Limits

NumPy projected solves and SciPy dense references may share LAPACK infrastructure and are not claimed fully independent backends. Analytic eigenvalues and constructed controls provide additional checks. Restarting, interior eigenvalues, large sparse systems and universal monotonic convergence are outside scope.

### Stored measurements and decisions

```json
{
  "metrics": {
    "maximum_basis_orthogonality": 6.813979303412138e-16,
    "largest_eigenvalue_condition": 100000.00000500213,
    "constructed_small_residual": 2.4999999999688053e-08,
    "constructed_forward_error": 0.004999999999999893
  },
  "checks": {
    "gap1-analytic-spectrum": true,
    "gap1-resolved": true,
    "gap1-basis": true,
    "gap0.1-analytic-spectrum": true,
    "gap0.1-resolved": true,
    "gap0.1-basis": true,
    "gap0.01-analytic-spectrum": true,
    "gap0.01-resolved": true,
    "gap0.01-basis": true,
    "K10-condition": true,
    "K10-analytic-spectrum": true,
    "K10-resolved": true,
    "K10-basis": true,
    "K1000-condition": true,
    "K1000-analytic-spectrum": true,
    "K1000-resolved": true,
    "K1000-basis": true,
    "pseudoK1-literal-formula": true,
    "pseudoK10-literal-formula": true,
    "pseudoK1000-literal-formula": true,
    "small-residual-does-not-certify-forward-error": true,
    "short-dimension-has-residual": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/krylov-eigen-conditioning/index.json

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/atlas-foundations-conditioning-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group.

### Sources and review scope

- C. Lanczos (1950). An Iteration Method for the Solution of the Eigenvalue Problem of Linear Differential and Integral Operators. https://nvlpubs.nist.gov/nistpubs/jres/045/jresv45n4p255_A1b.pdf; review_level=primary-first-page-and-official-metadata
- W. E. Arnoldi (1951). The principle of minimized iterations in the solution of the matrix eigenvalue problem. https://doi.org/10.1090/qam/42792; review_level=publisher-metadata-and-reference-list
- Y. Saad (1980). Variations on Arnoldi’s method for computing eigenelements of large unsymmetric matrices. https://www.sciencedirect.com/science/article/pii/002437958090169X; review_level=publisher-abstract-and-metadata
- LAPACK authors (1999). Error Bounds for the Nonsymmetric Eigenproblem; Overview. https://www.netlib.org/lapack/lug/node91.html; review_level=official implementation documentation, error-bound overview and cluster/invariant-subspace distinction
  Do not equate a small eigenpair residual with small forward eigenvalue error for nonnormal matrices; distinguish eigenvalue sensitivity, individual vectors, and clustered invariant subspaces.

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## Quadrature: narrow peaks, cancellation, endpoints and estimator blind spots

Vary Gauss order and adaptive tolerance on narrow Lorentz peaks, a square-root endpoint, severe cancellation, a zero integral and a deliberately missed compact bump, using analytic integrals and QUADPACK.

**Methods used**

- [Gaussian and adaptive quadrature](https://hrkoyama.github.io/numerical-methods-atlas/methods/quadrature/?lang=en) (`quadrature`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/quadrature-conditioning/?lang=en#quadrature-conditioning-en-algorithm)

Implement Golub–Welsch nodes/weights and adaptive Simpson with a local difference/15 estimate. Companion checks use x=t² for the endpoint and a known-support split for the narrow bump; these are not general automatic rescue mechanisms.

$$
\kappa_{\rm cancel}=\frac{\int_a^b|f(x)|\,dx}{|\int_a^bf(x)\,dx|}
$$

$$
\int_{c-w}^{c+w}(1-((x-c)/w)^2)^4\,dx=\frac{256w}{315}
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![Quadrature: narrow peaks, cancellation, endpoints and estimator blind spots: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/results/quadrature-conditioning.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Gauss–Legendre and adaptive quadrature: exactness, error estimates and budgets](https://hrkoyama.github.io/numerical-methods-atlas/problems/quadrature-moments/?lang=en) (`quadrature-moments`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/quadrature-moments/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/quadrature-conditioning/?lang=en#quadrature-conditioning-en-validation)

Compare roots_legendre, analytic atan integrals,2/3,the bump integral256w/315 and independent QUADPACK. Preserve QUADPACK status, estimated error, evaluation count and warning message. Cancellation uses a roundoff-aware absolute budget. When all initial five bump samples vanish, expose estimated error0 versus actual error about.00813.

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.
### Assumptions, units and boundaries

Use[0,1], Gauss orders8/16/32/64/128 and tolerances10⁻⁵/10⁻⁷/10⁻⁹. Lorentz widths are.1/.03/.01; cancellation scales are0/2¹²/2²⁴/2³⁶. A zero integral has undefined relative condition, stored as null.

**Editorial clarification**

An adaptive estimate or agreement between calculations is not a rigorous error bound for arbitrary integrands. Distinguish absolute and relative error under cancellation, unresolved local structure and evaluation budgets.

### Adopted numerical method

Implement Golub–Welsch nodes/weights and adaptive Simpson with a local difference/15 estimate. Companion checks use x=t² for the endpoint and a known-support split for the narrow bump; these are not general automatic rescue mechanisms.

$$
\kappa_{\rm cancel}=\frac{\int_a^b|f(x)|\,dx}{|\int_a^bf(x)\,dx|}
$$

$$
\int_{c-w}^{c+w}(1-((x-c)/w)^2)^4\,dx=\frac{256w}{315}
$$

### References and validation

Compare roots_legendre, analytic atan integrals,2/3,the bump integral256w/315 and independent QUADPACK. Preserve QUADPACK status, estimated error, evaluation count and warning message. Cancellation uses a roundoff-aware absolute budget. When all initial five bump samples vanish, expose estimated error0 versus actual error about.00813.

### Limits

The Simpson estimate is not a certified error bound. Passing the blind-spot control does not mean accurate integration. Direct square-root integration may honestly terminate at its depth budget. Exhaustive oscillatory/singular exploration and certified quadrature are not claimed.

### Stored measurements and decisions

```json
{
  "metrics": {
    "maximum_cancellation_condition": 68719476737.0,
    "blind_bump_actual_error": 0.008126984126984127,
    "blind_bump_reported_error": 0.0,
    "resolved_bump_actual_error": 1.0884418366607918e-12,
    "zero_integral_relative_condition": null
  },
  "checks": {
    "width0.1-reference": true,
    "n8-independent-rule": true,
    "n16-independent-rule": true,
    "n32-independent-rule": true,
    "n64-independent-rule": true,
    "n128-independent-rule": true,
    "width0.1-gauss-refinement": true,
    "width0.1-tol1e-05": true,
    "width0.1-tol1e-07": true,
    "width0.1-tol1e-09": true,
    "width0.03-reference": true,
    "width0.03-gauss-refinement": true,
    "width0.03-tol1e-05": true,
    "width0.03-tol1e-07": true,
    "width0.03-tol1e-09": true,
    "width0.01-reference": true,
    "width0.01-gauss-refinement": true,
    "width0.01-tol1e-05": true,
    "width0.01-tol1e-07": true,
    "width0.01-tol1e-09": true,
    "endpoint-tol1e-05": true,
    "endpoint-tol1e-07": true,
    "endpoint-tol1e-09": true,
    "C0-absolute-error": true,
    "C4096-absolute-error": true,
    "C1.67772e+07-absolute-error": true,
    "C6.87195e+10-absolute-error": true,
    "conditioned-input-perturbation-gain": true,
    "zero-integral-relative-condition-undefined": true,
    "heuristic-blind-spot-explicit": true,
    "known-support-companion-resolves": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/quadrature-conditioning/index.json

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/atlas-foundations-conditioning-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group.

### Sources and review scope

- G. H. Golub and J. H. Welsch (1969). Calculation of Gauss Quadrature Rules. https://www.ams.org/journals/mcom/1969-23-106/S0025-5718-69-99647-1/S0025-5718-69-99647-1.pdf; review_level=publisher-search-first-page-and-metadata
- J. N. Lyness (1969). Notes on the Adaptive Simpson Quadrature Routine. https://dl.acm.org/doi/10.1145/321526.321537; review_level=publisher-metadata
- P. Gonnet (2010). Increasing the Reliability of Adaptive Quadrature Using Explicit Interpolants. https://arxiv.org/abs/1006.3962; review_level=primary author paper, abstract and selected introduction/error-estimation text (§3)
  Checked selected original discussion of accidentally small differences between quadrature estimates. The educational Simpson counterexample is original test design, not an implementation of the paper’s new integrators.

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
