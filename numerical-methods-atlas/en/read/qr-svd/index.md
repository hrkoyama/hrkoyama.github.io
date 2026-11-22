# QR, SVD and least squares

Least squares, low-rank approximation and conditioning call for different matrix decompositions. QR reduces a problem to orthogonal transformations and a triangular solve; SVD exposes singular values and resolvable directions.

## Problem and representative equations

For a real m×n matrix with m≥n, thin QR has QᵀQ=I and upper triangular R. Full column rank gives the least-squares solve Rx=Qᵀb. SVD has nonnegative singular values σᵢ. Truncating small σᵢ in a pseudoinverse regularizes the problem and can change the solution being sought.

$$
A=QR=U\Sigma V^T,\qquad \min_x\|Ax-b\|_2,\qquad A^+b=\sum_{\sigma_i>\tau}\frac{u_i^Tb}{\sigma_i}v_i\quad\text{(truncated)}.
$$

## Algorithm

Householder QR eliminates subdiagonal entries with reflections and generally maintains orthogonality better than classical Gram–Schmidt. Consider column pivoting or SVD for rank diagnosis. Classical SVD algorithms reduce to bidiagonal form using orthogonal transformations rather than explicitly forming normal equations.

## Conditions and pitfalls

For full column rank, κ₂(AᵀA)=κ₂(A)². A small residual can coexist with uncertain coefficients under ill-conditioning or noise. Choose a numerical-rank threshold relative to scale, rounding and measurement uncertainty, and consider column scaling when variables have different units.

Distinguish residual/backward error from forward errors in coefficients or singular values. At large condition numbers, small changes to the input or right-hand side can cause large coefficient changes. Numerical rank depends on a singular-value threshold and arithmetic precision; a truncated least-squares solution need not solve the original problem exactly.

General least-squares sensitivity also depends on the angle between the right-hand side and the column space, not only on condition number. Published relative-accuracy results for one-sided Jacobi SVD depend on stopping rules and componentwise conditioning. Agreement for small singular values in these small matrices is not a universal relative-accuracy guarantee for arbitrary ill-conditioned matrices.

## What to check

Check relative factorization residuals, orthogonality and Aᵀ(Ax−b). Test prescribed singular values and rank-deficient cases, and compare solution changes under controlled data perturbations.

The added release compares errors across small matrices with prescribed singular values, fixed right-hand-side perturbations and numerical-rank thresholds. Measure QR/SVD reconstruction and orthogonality, least-squares residual, coefficient forward error and numerical rank separately. Distinguish LAPACK references from independent high-precision references constructed from the actual binary floating-point input. Condition-number squaring for normal equations is explained above as theory; it is not an executed control in this added case.

## Fixed-input examples and diagnostic controls

Distinguish the scope established by acceptance checks from a general mathematical guarantee; preserve historical inputs, measurements and criteria.

### Householder QR and one-sided Jacobi SVD: orthogonality, rank and least squares

Fixed-target computation

Original Householder QR and one-sided Jacobi SVD for real tall matrices are checked on ordinary, 10⁶-column-scaled and rank-deficient inputs, against separate LAPACK singular values and minimum-norm least-squares solutions.

Not a full LAPACK replacement or validation of complex/wide matrices, arbitrary extreme scales or optimal relative singular-value accuracy. The 10⁻¹² cutoff defines numerical rather than exact mathematical rank. The experiment does not establish all hypotheses of the Demmel–Veselić accuracy results.

[Input, results and acceptance](/numerical-methods-atlas/validation/qr-svd-factorization/?lang=en) · [Method and sources](/numerical-methods-atlas/en/read/validation-foundations/#qr-svd-factorization) · [Code run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/run.py) · [Code solvers.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/solvers.py) · [Tests test_foundations.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/test_foundations.py) · [ZIP](/code/validated-examples/2026-11-22/foundations/atlas-foundations-2026-11-22.zip) · [Results](/code/validated-examples/2026-11-22/foundations/results/result.json) · [Rerun receipt](/code/validated-examples/2026-11-22/foundations/verification.json)

### QR/SVD: prescribed spectra, perturbation gain and numerical rank

Fixed-target computation

Vary condition number from 1 to 2³⁶ for exactly representable 16×4 dyadic matrices, separating reconstruction from forward solution error. Compare LAPACK and separately executed 80/120-digit references for the actual binary64 inputs.

Some LAPACK and projected-core numerical infrastructure is shared. mpmath SVD uses separate bidiagonalization and QR iteration; mpmath least squares is a separate high-precision implementation of the same Householder family. Tiny-singular-value relative accuracy is not guaranteed for arbitrary ill-conditioned matrices.

[Input, results and acceptance](/numerical-methods-atlas/validation/qr-svd-conditioning/?lang=en) · [Method and sources](/numerical-methods-atlas/en/read/validation-foundations-conditioning/#qr-svd-conditioning) · [Code run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/run.py) · [Code experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/experiments.py) · [Code fixtures.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/fixtures.py) · [Code mpmath_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/mpmath_reference.py) · [Code solvers.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/solvers.py) · [Tests test_conditioning.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/test_conditioning.py) · [ZIP](/code/validated-examples/2026-11-22/foundations-conditioning/atlas-foundations-conditioning-2026-11-22.zip) · [Results](/code/validated-examples/2026-11-22/foundations-conditioning/results/result.json) · [Rerun receipt](/code/validated-examples/2026-11-22/foundations-conditioning/verification.json)

## Publication scope

Historical inputs, measurements and tolerances are preserved. Additional conditioning, residual and convergence checks have a separate scoped release. Passing a diagnostic control can mean that its intended limitation was observed; it does not establish general success or reproduction of an entire paper.

## Sources

- Alston S. Householder (1958). Unitary Triangularization of a Nonsymmetric Matrix. https://doi.org/10.1145/320941.320947
- G. H. Golub and C. Reinsch (1970). Singular value decomposition and least squares solutions. https://doi.org/10.1007/bf02163027
- J. Demmel, K. Veselić (1992). Jacobi’s Method is More Accurate than QR. https://doi.org/10.1137/0613074
- LAPACK authors (1999). Further Details: Error Bounds for Linear Least Squares Problems. https://netlib.org/lapack/lug/node83.html
