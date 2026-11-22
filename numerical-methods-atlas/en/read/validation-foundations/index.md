# AMG, factorizations, eigenvalues and quadrature

Small fixed inputs connect numerical methods, references, errors, refinement and explicit failure conditions.

These additional validation supplements are managed separately from the common 22-example registry. Receipts cover independent ZIP extraction, tests and every fixed input within each group. Changes of settings, methods or step sizes do not add independent physical problems.

## Matrix-based AMG: distinguish residual and solution error

Build a smoothed-aggregation hierarchy from an SPD matrix alone and run V-cycles. Problems with 7², 15² and 31² unknowns distinguish independent sparse direct solutions, analytic discrete sine modes and second-order convergence to the continuum solution.

### Assumptions, units and boundaries

Dimensionless unit square, constant-positive-coefficient −Δu=f, homogeneous Dirichlet boundaries and five-point differences. Hierarchy setup receives no coordinates, mesh width or n; it uses the coefficient matrix and an implicit constant near-null candidate. A real SPD input is assumed; arbitrary indefinite problems are outside scope.

### Adopted numerical method

A graph based on row-relative off-diagonal strength supplies greedy star aggregates; leftover nodes attach to adjacent aggregates. Smooth tentative T via P=(I−ωD⁻¹A)T with ω=4/(3ρ̄), where ρ̄ bounds the absolute row sums of D⁻¹A. Coarse operators are PᵀAP. V-cycles use two pre/post Jacobi sweeps and a terminal dense direct solve. This is a small adopted SA variant, not every construction or convergence theorem in the original paper.

$$
A_c=P^TAP,\quad P=(I-\omega D^{-1}A)T
$$

$$
r_k=b-Ax_k,\quad \eta_k=\|r_k\|_2/\|b\|_2
$$

### References and validation

Store normalized residuals, relative solution differences against SciPy spsolve, discrete-L²-type continuum errors, observed order and operator complexity. A randomly permuted matrix is also checked against a direct solution to expose hidden geometric ordering assumptions. A zero cycle budget reports nonconvergence.

### Limits

Only three fixed scalar grids are checked. Large coefficient jumps, strong anisotropy, elasticity, arbitrary unstructured meshes, optimal complexity and mesh-independent convergence are not certified. A small residual alone does not prove a small solution error.

### Stored measurements and decisions

```json
{
  "metrics": {
    "max_relative_residual": 7.1395963390776e-11,
    "max_direct_solution_error": 2.0283080847857227e-11,
    "minimum_pde_order": 2.0020872697597354,
    "max_operator_complexity": 3.196752830591754
  },
  "checks": {
    "all_residual_targets": true,
    "independent_sparse_direct": true,
    "second_order_pde_refinement": true,
    "bounded_operator_complexity": true,
    "cycle_budget_failure_reported": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/sa-amg/index.json

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/atlas-foundations-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group.

### Sources and review scope

- P. Vaněk, J. Mandel and M. Brezina (1996). Algebraic multigrid by smoothed aggregation for second and fourth order elliptic problems. https://link.springer.com/article/10.1007/BF02238511; review_level=publisher-abstract-and-metadata

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## Householder QR and one-sided Jacobi SVD: orthogonality, rank and least squares

Original Householder QR and one-sided Jacobi SVD for real tall matrices are checked on ordinary, 10⁶-column-scaled and rank-deficient inputs, against separate LAPACK singular values and minimum-norm least-squares solutions.

### Assumptions, units and boundaries

Small real matrices with m≥n. Numerical rank uses a 10⁻¹² threshold relative to the largest singular value; compact factors omit null directions. QR has no column pivoting and is not used as a rank-revealing method.

### Adopted numerical method

Householder reflectors triangularize R while accumulating Q. The SVD repeatedly rotates column pairs toward orthogonality and uses their resulting lengths as singular values; it does not diagonalize AᵀA. Least squares uses triangular back substitution for QR and truncated compact SVD for deficient rank.

$$
A=QR,\quad Q^TQ=I
$$

$$
A\simeq U_r\Sigma_rV_r^T,\quad x_{\min}=V_r\Sigma_r^{-1}U_r^Tb
$$

### References and validation

Compare QR/SVD relative reconstruction, Q/U/V orthogonality, singular values from SciPy LAPACK gesdd, least-squares solutions/ranks from gelsd/gelsy and normal-equation stationarity residuals. Singular-vector signs are not compared; zero matrices and budget exhaustion are tested.

### Limits

Not a full LAPACK replacement or validation of complex/wide matrices, arbitrary extreme scales or optimal relative singular-value accuracy. The 10⁻¹² cutoff defines numerical rather than exact mathematical rank. The experiment does not establish all hypotheses of the Demmel–Veselić accuracy results.

### Stored measurements and decisions

```json
{
  "metrics": {
    "max_qr_reconstruction": 9.197631573723943e-16,
    "max_svd_reconstruction": 1.0519095898403626e-13,
    "max_singular_value_error": 3.399227299681105e-16,
    "max_least_squares_error": 9.164127590036862e-15,
    "max_orthogonality": 1.310421197476067e-15
  },
  "checks": {
    "all_jacobi_converged_and_ranks_match": true,
    "householder_reconstruction": true,
    "householder_orthogonality": true,
    "jacobi_reconstruction": true,
    "jacobi_orthogonality": true,
    "independent_lapack_singular_values": true,
    "independent_minimum_norm_least_squares": true,
    "qr_least_squares": true,
    "least_squares_stationarity": true,
    "sweep_budget_failure_reported": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/qr-svd-factorization/index.json

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/atlas-foundations-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group.

### Sources and review scope

- A. S. Householder (1958). Unitary Triangularization of a Nonsymmetric Matrix. https://dl.acm.org/doi/10.1145/320941.320947; review_level=publisher-metadata
- J. Demmel and K. Veselić (1992). Jacobi’s Method is More Accurate than QR. https://epubs.siam.org/doi/abs/10.1137/0613074; review_level=publisher-abstract-and-metadata

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## Lanczos and Arnoldi: convergence of Ritz values and eigenpair residuals

Original Lanczos and Arnoldi on symmetric/nonsymmetric 32×32 and 48×48 matrices measure convergence of the largest-real-part eigenpair over Krylov dimensions 4, 8 and 16, against independent full-matrix LAPACK references.

### Assumptions, units and boundaries

The symmetric case is real symmetric; the nonsymmetric case is real with a known separated largest eigenvalue 5. Starting vectors use fixed seeds. Nonsymmetric Ritz values may be complex and are selected by largest real part.

### Adopted numerical method

Lanczos uses its three-term recurrence plus two passes of full reorthogonalization; Arnoldi uses two-pass modified Gram–Schmidt. Only the small projected T/H is solved by NumPy eigh/eig before lifting Ritz vectors. A full dense solve of the original matrix is used only on the reference side.

$$
AV_m=V_mH_m+h_{m+1,m}v_{m+1}e_m^T
$$

$$
H_my=\theta y,\quad v=V_my,\quad r=Av-\theta v
$$

### References and validation

Store ||Av−λv||₂, differences from independently solved dense eigenvalues and basis orthogonality; verify final improvement as Krylov dimension grows. Nonsymmetric Ritz convergence is not assumed monotone. Tests include identity-matrix happy breakdown, zero-start rejection and insufficient dimension budgets.

### Limits

Unrestarted small-matrix educational examples with separated extreme eigenpairs. Interior/clustered eigenvalues, very large sparse matrices, strong nonnormality, shift-invert and implicitly restarted Arnoldi are outside scope. A small eigenpair residual alone is not treated as a rigorous eigenvalue-error bound for nonnormal matrices.

### Stored measurements and decisions

```json
{
  "metrics": {
    "max_final_eigenpair_residual": 1.4394924647739691e-12,
    "max_basis_orthogonality": 4.911536314397836e-16
  },
  "checks": {
    "independent_dense_eigenvalues_and_residuals": true,
    "krylov_basis_orthogonality": true,
    "dimension_budget_failure_reported": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/krylov-eigenvalues/index.json

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/atlas-foundations-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/verification.json

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

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## Gauss–Legendre and adaptive quadrature: exactness, error estimates and budgets

Construct Gaussian nodes/weights from the Legendre recurrence and test polynomial moments through degree 2n−1 and an exponential. Adaptive Simpson integrates exponential and Lorentzian peaks, against analytic integrals and independent QUADPACK.

### Assumptions, units and boundaries

Dimensionless smooth real functions on finite intervals. Fixed Gauss orders 2/4/8/16 and adaptive absolute tolerances 10⁻⁵/10⁻⁷/10⁻⁹ are swept separately. Endpoint singularities, discontinuities and infinite intervals are not covered by these inputs.

### Adopted numerical method

Golub–Welsch obtains nodes from a symmetric Jacobi matrix and weights from twice the squared first eigenvector components. Adaptive Simpson bisects intervals and allocates tolerances using |Sleft+Sright−Swhole|/15 as a local estimate. Evaluation and depth limits report unmet targets explicitly.

$$
\int_{-1}^{1}f(x)\,dx\simeq\sum_{j=1}^{n}w_jf(x_j)
$$

$$
E_{\mathrm{est}}=|S_{\mathrm{left}}+S_{\mathrm{right}}-S_{\mathrm{whole}}|/15
$$

### References and validation

Measure polynomial moments for every chosen order, node/weight differences from SciPy roots_legendre, order refinement for the analytic exponential integral, and agreement with analytic arctangent and SciPy quad references. Store evaluation counts/errors as tolerance tightens; test forced exhaustion after five evaluations and nonfinite integrands.

### Limits

The local Simpson estimate is not a rigorous error bound for arbitrary functions. The implementation does not generally solve missed high frequencies, singularities or roundoff stagnation, and it is not a reimplementation of Gauss–Kronrod or all of QUADPACK.

### Stored measurements and decisions

```json
{
  "metrics": {
    "max_polynomial_moment_error": 8.881784197001252e-16,
    "max_scipy_rule_error": 1.2490009027033011e-15,
    "gauss_final_exp_error": 0.0,
    "max_adaptive_error_over_tolerance": 0.01729971494390803,
    "budget_failure_evaluations": 5
  },
  "checks": {
    "gauss_polynomial_moments": true,
    "independent_scipy_gauss_rule": true,
    "gauss_nonsingular_refinement": true,
    "adaptive_exact_and_quad_references": true,
    "evaluation_budget_failure_reported": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/gauss-adaptive-quadrature/index.json

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/atlas-foundations-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group.

### Sources and review scope

- G. H. Golub and J. H. Welsch (1969). Calculation of Gauss Quadrature Rules. https://www.ams.org/journals/mcom/1969-23-106/S0025-5718-69-99647-1/S0025-5718-69-99647-1.pdf; review_level=publisher-search-first-page-and-metadata
- J. N. Lyness (1969). Notes on the Adaptive Simpson Quadrature Routine. https://dl.acm.org/doi/10.1145/321526.321537; review_level=publisher-metadata

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
