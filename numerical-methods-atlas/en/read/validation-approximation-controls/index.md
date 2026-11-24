# Fixed interpolation, spline and Haar controls

Small fixed examples separate nodes, representation and rounding; C2 continuity and shape preservation; and boundary extension and shifts.

These additional validation supplements are managed separately from the common 22-example registry. Receipts cover independent ZIP extraction, tests and every fixed input within each group. Changes of settings, methods or step sizes do not add independent physical problems.

## Runge interpolation: nodes, representation and rounding

Interpolate the Runge and absolute-value functions on fixed equispaced and Lobatto-like nodes, and compare with Clenshaw evaluation.

**Methods used**

- [Chebyshev approximation](https://hrkoyama.github.io/numerical-methods-atlas/methods/chebyshev/?lang=en) (`chebyshev`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/runge-barycentric-clenshaw/?lang=en#runge-barycentric-clenshaw-en-algorithm)

Implement the second barycentric formula and a full-coefficient Clenshaw recurrence. Retain the closed weights and finite Chebyshev transform on rounded nodes.

$$
p(x)=sum_j y_j*prod_(k!=j)((x-x_k)/(x_j-x_k))
$$

$$
R(x)=(sum_j w_j*y_j/(x-x_j))/(sum_j w_j/(x-x_j))
$$

$$
C(x)=sum_(k=0)^n a_k*T_k(x); b_k=a_k+2*x*b_(k+1)-b_(k+2)
$$

- [Polynomial interpolation on stored nodes](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#polynomial-interpolation-en) (`polynomial-interpolation`)

Dimensionless interval [-1,1], degrees 8, 16 and 32, and 2048 fixed midpoints. Actual binary64 nodes, data and weights define the discrete problem.


**Problem figure**

![Runge interpolation: nodes, representation and rounding: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/runge-barycentric-clenshaw.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Runge interpolation: nodes, representation and rounding](https://hrkoyama.github.io/numerical-methods-atlas/problems/runge-barycentric-clenshaw/?lang=en) (`runge-barycentric-clenshaw`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/runge-barycentric-clenshaw/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/runge-barycentric-clenshaw/?lang=en#runge-barycentric-clenshaw-en-validation)

Separate the stored-data polynomial P, closed-weight rational expression R, stored-coefficient series C and target f. Check exact rational references at 17 probes, operation-based error bounds, node identities and fixed Runge trends.

- [Runge interpolation: nodes, representation and rounding](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-runge-barycentric-clenshaw-en) (`runge-barycentric-clenshaw`; Same-problem reference · Analytic reference)

A sampled maximum error is not a proof of a continuous uniform norm. Closed weights and discrete orthogonality on rounded nodes are not treated as exact. No arbitrary-degree or all-point stability guarantee is made.
### Assumptions, units and boundaries

Dimensionless interval [-1,1], degrees 8, 16 and 32, and 2048 fixed midpoints. Actual binary64 nodes, data and weights define the discrete problem.

**Editorial clarification**

A sampled maximum error is not a proof of a continuous uniform norm. Closed weights and discrete orthogonality on rounded nodes are not treated as exact. No arbitrary-degree or all-point stability guarantee is made.

### Adopted numerical method

Implement the second barycentric formula and a full-coefficient Clenshaw recurrence. Retain the closed weights and finite Chebyshev transform on rounded nodes.

$$
p(x)=sum_j y_j*prod_(k!=j)((x-x_k)/(x_j-x_k))
$$

$$
R(x)=(sum_j w_j*y_j/(x-x_j))/(sum_j w_j/(x-x_j))
$$

$$
C(x)=sum_(k=0)^n a_k*T_k(x); b_k=a_k+2*x*b_(k+1)-b_(k+2)
$$

### References and validation

Separate the stored-data polynomial P, closed-weight rational expression R, stored-coefficient series C and target f. Check exact rational references at 17 probes, operation-based error bounds, node identities and fixed Runge trends.

### Limits

A sampled maximum error is not a proof of a continuous uniform norm. Closed weights and discrete orthogonality on rounded nodes are not treated as exact. No arbitrary-degree or all-point stability guarantee is made.

### Stored measurements and decisions

```json
{
  "metrics": {
    "max_node_table_cosine_defect": 1.6816803605601774e-16,
    "maximum_sampled_function_error": 105718.65676159713,
    "reference_certificate_probes_per_interpolant": 17,
    "coefficient_sets": 6
  },
  "checks": {
    "reference:fixed-cosine-node-table": true,
    "runge-equispaced-8:finite": true,
    "runge-equispaced-8:node-hit-identity": true,
    "runge-equispaced-8:barycentric-operation-certificate": true,
    "runge-lobatto-8:clenshaw-operation-certificate": true,
    "runge-lobatto-8:finite": true,
    "runge-lobatto-8:node-hit-identity": true,
    "runge-lobatto-8:barycentric-operation-certificate": true,
    "runge-equispaced-16:finite": true,
    "runge-equispaced-16:node-hit-identity": true,
    "runge-equispaced-16:barycentric-operation-certificate": true,
    "runge-lobatto-16:clenshaw-operation-certificate": true,
    "runge-lobatto-16:finite": true,
    "runge-lobatto-16:node-hit-identity": true,
    "runge-lobatto-16:barycentric-operation-certificate": true,
    "runge-equispaced-32:finite": true,
    "runge-equispaced-32:node-hit-identity": true,
    "runge-equispaced-32:barycentric-operation-certificate": true,
    "runge-lobatto-32:clenshaw-operation-certificate": true,
    "runge-lobatto-32:finite": true,
    "runge-lobatto-32:node-hit-identity": true,
    "runge-lobatto-32:barycentric-operation-certificate": true,
    "absolute-equispaced-8:finite": true,
    "absolute-equispaced-8:node-hit-identity": true,
    "absolute-equispaced-8:barycentric-operation-certificate": true,
    "absolute-lobatto-8:clenshaw-operation-certificate": true,
    "absolute-lobatto-8:finite": true,
    "absolute-lobatto-8:node-hit-identity": true,
    "absolute-lobatto-8:barycentric-operation-certificate": true,
    "absolute-equispaced-16:finite": true,
    "absolute-equispaced-16:node-hit-identity": true,
    "absolute-equispaced-16:barycentric-operation-certificate": true,
    "absolute-lobatto-16:clenshaw-operation-certificate": true,
    "absolute-lobatto-16:finite": true,
    "absolute-lobatto-16:node-hit-identity": true,
    "absolute-lobatto-16:barycentric-operation-certificate": true,
    "absolute-equispaced-32:finite": true,
    "absolute-equispaced-32:node-hit-identity": true,
    "absolute-equispaced-32:barycentric-operation-certificate": true,
    "absolute-lobatto-32:clenshaw-operation-certificate": true,
    "absolute-lobatto-32:finite": true,
    "absolute-lobatto-32:node-hit-identity": true,
    "absolute-lobatto-32:barycentric-operation-certificate": true,
    "reference:polynomial-control-equispaced": true,
    "reference:polynomial-control-lobatto": true,
    "runge:equispaced-growth": true,
    "runge:lobatto-refinement": true,
    "fixed-record-and-coefficient-count": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/runge-barycentric-clenshaw/index.json

![Interpolate the Runge and absolute-value functions on fixed equispaced and Lobatto-like nodes, and compare with Clenshaw evaluation. Drawn from saved arrays.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/runge-barycentric-clenshaw-preview.png)

Interpolate the Runge and absolute-value functions on fixed equispaced and Lobatto-like nodes, and compare with Clenshaw evaluation. Drawn from saved arrays.

![Saved errors, derivatives or squared norms shown separately. The text states the scope of each boundary and representation.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/runge-barycentric-clenshaw-diagnostics.png)

Saved errors, derivatives or squared norms shown separately. The text states the scope of each boundary and representation.

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/atlas-approximation-controls-2026-11-25.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- NIST DLMF §3.11(ii): Chebyshev series and Clenshaw summation [accessed 2026-11-25]. https://dlmf.nist.gov/3.11; review_level=official-reference-selected-equations
Selected E7, E9, E11 and E15 with endpoint-halving conventions; no original Clenshaw paper reading. The implementation uses full coefficients, so its final combination is derived explicitly.

- SciPy 1.14.1 BarycentricInterpolator documentation [accessed 2026-11-24]. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.interpolate.BarycentricInterpolator.html; review_level=official-documentation-selected-notes
Selected barycentric formula and interpolation-conditioning notes read during the preceding preparation. The Berrut–Trefethen paper is a bibliographic lead, not a full-text reading.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## Natural and clamped splines versus PCHIP

Compare C2 continuity and shape preservation on three fixed data sets: a monotone plateau, a cubic and a straight line.

**Methods used**

- [Spline interpolation](https://hrkoyama.github.io/numerical-methods-atlas/methods/splines/?lang=en) (`splines`)
- [PCHIP monotone cubic Hermite interpolation](https://hrkoyama.github.io/numerical-methods-atlas/methods/pchip/?lang=en) (`pchip`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/spline-shape-controls/?lang=en#spline-shape-controls-en-algorithm)

Solve a cubic B-spline collocation system and evaluate it with de Boor recursion. A separate path implements PCHIP harmonic slopes, endpoint limiting and Hermite evaluation.

$$
S_i(s)=a_i+b_i*s+c_i*s^2+d_i*s^3
$$

$$
d_k=(w_1+w_2)/(w_1/m_(k-1)+w_2/m_k)
$$

$$
S_natural(1.5)=a-9*(b-a)/88; S_clamped(1.5)=a-15*(b-a)/152
$$

- [Cubic splines and shape-preserving interpolation](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#cubic-spline-pchip-en) (`cubic-spline-pchip`)

Use actual binary64 knots and values. Natural conditions set both endpoint second derivatives to zero; clamped conditions prescribe the first derivatives from the input.


**Problem figure**

![Natural and clamped splines versus PCHIP: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/spline-shape-controls.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Natural and clamped splines versus PCHIP](https://hrkoyama.github.io/numerical-methods-atlas/problems/spline-shape-controls/?lang=en) (`spline-shape-controls`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/spline-shape-controls/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/spline-shape-controls/?lang=en#spline-shape-controls-en-validation)

Compare with exact rational second-derivative systems, rational PCHIP and SciPy 1.14.1. Fifteen endpoint records contain sixteen scalar outputs from thirteen distinct inputs. Independent Fraction formulas show plateau undershoot for the actual binary64 data.

- [Natural and clamped splines versus PCHIP](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-spline-shape-controls-en) (`spline-shape-controls`; Same-problem reference · Analytic reference)

PCHIP is generally C1, not necessarily C2. Best approximation, extrapolation and noise smoothing are outside scope. A SciPy comparison does not substitute for reading the original papers.
### Assumptions, units and boundaries

Use actual binary64 knots and values. Natural conditions set both endpoint second derivatives to zero; clamped conditions prescribe the first derivatives from the input.

**Editorial clarification**

PCHIP is generally C1, not necessarily C2. Best approximation, extrapolation and noise smoothing are outside scope. A SciPy comparison does not substitute for reading the original papers.

### Adopted numerical method

Solve a cubic B-spline collocation system and evaluate it with de Boor recursion. A separate path implements PCHIP harmonic slopes, endpoint limiting and Hermite evaluation.

$$
S_i(s)=a_i+b_i*s+c_i*s^2+d_i*s^3
$$

$$
d_k=(w_1+w_2)/(w_1/m_(k-1)+w_2/m_k)
$$

$$
S_natural(1.5)=a-9*(b-a)/88; S_clamped(1.5)=a-15*(b-a)/152
$$

### References and validation

Compare with exact rational second-derivative systems, rational PCHIP and SciPy 1.14.1. Fifteen endpoint records contain sixteen scalar outputs from thirteen distinct inputs. Independent Fraction formulas show plateau undershoot for the actual binary64 data.

### Limits

PCHIP is generally C1, not necessarily C2. Best approximation, extrapolation and noise smoothing are outside scope. A SciPy comparison does not substitute for reading the original papers.

### Stored measurements and decisions

```json
{
  "metrics": {
    "maximum_value_scaled_reference_defect": 2.9409263239818476e-16,
    "maximum_derivative_scaled_reference_defect": 5.2306043094691055e-15,
    "endpoint_fixture_records": 15,
    "endpoint_scalar_outputs": 16,
    "endpoint_distinct_datasets": 13
  },
  "checks": {
    "reference:endpoint-branch-values": true,
    "reference:endpoint-record-count": true,
    "reference:endpoint-output-count": true,
    "reference:endpoint-distinct-datasets": true,
    "reference:negative-natural-witness": true,
    "reference:negative-clamped-witness": true,
    "plateau-natural:finite": true,
    "plateau-natural:value-reference": true,
    "plateau-natural:derivative-reference": true,
    "plateau-natural:nodal": true,
    "plateau-natural:boundary-or-shape": true,
    "plateau-clamped:finite": true,
    "plateau-clamped:value-reference": true,
    "plateau-clamped:derivative-reference": true,
    "plateau-clamped:nodal": true,
    "plateau-clamped:boundary-or-shape": true,
    "reference:pchip-actual-input-plateau": true,
    "plateau-pchip:finite": true,
    "plateau-pchip:value-reference": true,
    "plateau-pchip:derivative-reference": true,
    "plateau-pchip:nodal": true,
    "plateau-pchip:boundary-or-shape": true,
    "cubic-natural:finite": true,
    "cubic-natural:value-reference": true,
    "cubic-natural:derivative-reference": true,
    "cubic-natural:nodal": true,
    "cubic-natural:boundary-or-shape": true,
    "cubic-clamped:finite": true,
    "cubic-clamped:value-reference": true,
    "cubic-clamped:derivative-reference": true,
    "cubic-clamped:nodal": true,
    "cubic-clamped:boundary-or-shape": true,
    "cubic-pchip:finite": true,
    "cubic-pchip:value-reference": true,
    "cubic-pchip:derivative-reference": true,
    "cubic-pchip:nodal": true,
    "cubic-pchip:boundary-or-shape": true,
    "linear-natural:finite": true,
    "linear-natural:value-reference": true,
    "linear-natural:derivative-reference": true,
    "linear-natural:nodal": true,
    "linear-natural:boundary-or-shape": true,
    "linear-clamped:finite": true,
    "linear-clamped:value-reference": true,
    "linear-clamped:derivative-reference": true,
    "linear-clamped:nodal": true,
    "linear-clamped:boundary-or-shape": true,
    "linear-pchip:finite": true,
    "linear-pchip:value-reference": true,
    "linear-pchip:derivative-reference": true,
    "linear-pchip:nodal": true,
    "linear-pchip:boundary-or-shape": true,
    "reference:exact-piece-continuity": true,
    "reference:polynomial-cubic-clamped": true,
    "reference:polynomial-linear-natural": true,
    "reference:polynomial-linear-clamped": true,
    "fixed-fit-count": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/spline-shape-controls/index.json

![Compare C2 continuity and shape preservation on three fixed data sets: a monotone plateau, a cubic and a straight line. Drawn from saved arrays.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/spline-shape-controls-preview.png)

Compare C2 continuity and shape preservation on three fixed data sets: a monotone plateau, a cubic and a straight line. Drawn from saved arrays.

![Saved errors, derivatives or squared norms shown separately. The text states the scope of each boundary and representation.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/spline-shape-controls-diagnostics.png)

Saved errors, derivatives or squared norms shown separately. The text states the scope of each boundary and representation.

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/atlas-approximation-controls-2026-11-25.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- SciPy 1.14.1 PCHIP documentation and selected source [accessed 2026-11-25]. https://raw.githubusercontent.com/scipy/scipy/v1.14.1/scipy/interpolate/_cubic.py; review_level=official-source-selected-lines
Selected lines 202–225, 243–254, 275–298: harmonic interior derivatives, endpoint sign and 3-slope limiter, two-point case. The original Fritsch–Butland paper has not been read in full. Own formulas are independently expressed as scalar Hermite polynomials.

- SciPy 1.14.1 BSpline and CubicSpline documentation [accessed 2026-11-24]. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.interpolate.CubicSpline.html; review_level=official-documentation-selected-definitions
Natural and clamped boundary conditions and the BSpline recurrence were read during preparation. No de Boor original full-text claim. SciPy is a secondary numerical companion; the rational second-derivative system is the independent reference.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## Haar multiresolution: boundaries, shifts and thresholds

Apply three-level Haar analysis to short signals of lengths 17 and 32, separating one-sample shifts from odd-length boundary handling.

**Methods used**

- [Wavelets](https://hrkoyama.github.io/numerical-methods-atlas/methods/wavelets/?lang=en) (`wavelets`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/haar-mallat-boundary-threshold/?lang=en#haar-mallat-boundary-threshold-en-algorithm)

Implement pair-sum and pair-difference filters, downsampling and inverse pyramids. Reconstruct with no threshold, hard thresholding and soft thresholding from the same analysis coefficients.

$$
a_(l+1,k)=(a_(l,2k)+a_(l,2k+1))/sqrt(2)
$$

$$
d_(l+1,k)=(a_(l,2k)-a_(l,2k+1))/sqrt(2)
$$

$$
E_after=E_before+padding^2; ||e||_2^2=||delta_coeff||_2^2 only for square orthogonal transform
$$

- [Discrete Haar transforms of finite signals](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#discrete-haar-transform-en) (`discrete-haar-transform`)

At each odd-length level append the first sample for periodic extension or the last for symmetric extension, then crop during synthesis. Apply threshold 0.2 only to detail coefficients.


**Problem figure**

![Haar multiresolution: boundaries, shifts and thresholds: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/haar-mallat-boundary-threshold.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Haar multiresolution: boundaries, shifts and thresholds](https://hrkoyama.github.io/numerical-methods-atlas/problems/haar-mallat-boundary-threshold/?lang=en) (`haar-mallat-boundary-threshold`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/haar-mallat-boundary-threshold/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/haar-mallat-boundary-threshold/?lang=en#haar-mallat-boundary-threshold-en-validation)

Use twelve analyses and thirty-six reconstructions. Check independent matrices, Fraction/Decimal coefficients, perfect reconstruction and squared L2 errors. Require the orthogonal error identity only at length 32; retain level-by-level padding energy at length 17.

- [Haar multiresolution: boundaries, shifts and thresholds](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-haar-mallat-boundary-threshold-en) (`haar-mallat-boundary-threshold`; Same-problem reference · Analytic reference)

Limited to Haar, without longer filters or image compression. General symmetric extension is not assumed orthonormal. Shift invariance is not required; shift-dependent differences are retained.
### Assumptions, units and boundaries

At each odd-length level append the first sample for periodic extension or the last for symmetric extension, then crop during synthesis. Apply threshold 0.2 only to detail coefficients.

**Editorial clarification**

Limited to Haar, without longer filters or image compression. General symmetric extension is not assumed orthonormal. Shift invariance is not required; shift-dependent differences are retained. Sample indices are not physical spatial coordinates. This is a finite-signal map with declared boundary handling.

### Adopted numerical method

Implement pair-sum and pair-difference filters, downsampling and inverse pyramids. Reconstruct with no threshold, hard thresholding and soft thresholding from the same analysis coefficients.

$$
a_(l+1,k)=(a_(l,2k)+a_(l,2k+1))/sqrt(2)
$$

$$
d_(l+1,k)=(a_(l,2k)-a_(l,2k+1))/sqrt(2)
$$

$$
E_after=E_before+padding^2; ||e||_2^2=||delta_coeff||_2^2 only for square orthogonal transform
$$

### References and validation

Use twelve analyses and thirty-six reconstructions. Check independent matrices, Fraction/Decimal coefficients, perfect reconstruction and squared L2 errors. Require the orthogonal error identity only at length 32; retain level-by-level padding energy at length 17.

### Limits

Limited to Haar, without longer filters or image compression. General symmetric extension is not assumed orthonormal. Shift invariance is not required; shift-dependent differences are retained.

### Stored measurements and decisions

```json
{
  "metrics": {
    "analysis_records": 12,
    "maximum_reconstruction_l2_squared": 0.6095394266271633,
    "maximum_shift_back_equivariance_l2_squared": 0.23999999999999966
  },
  "checks": {
    "reference:golden-0": true,
    "reference:golden-1": true,
    "periodic-smooth32-periodic:independent-analysis": true,
    "periodic-smooth32-periodic:left-inverse": true,
    "periodic-smooth32-periodic:coefficient-count": true,
    "periodic-smooth32-periodic:padding-energy-ledger": true,
    "periodic-smooth32-periodic-none:finite-and-owned-shape": true,
    "periodic-smooth32-periodic-none:independent-synthesis": true,
    "periodic-smooth32-periodic-none:perfect-reconstruction": true,
    "periodic-smooth32-periodic-none:critical-squared-error-identity": true,
    "periodic-smooth32-periodic-hard:finite-and-owned-shape": true,
    "periodic-smooth32-periodic-hard:independent-synthesis": true,
    "periodic-smooth32-periodic-hard:critical-squared-error-identity": true,
    "periodic-smooth32-periodic-soft:finite-and-owned-shape": true,
    "periodic-smooth32-periodic-soft:independent-synthesis": true,
    "periodic-smooth32-periodic-soft:critical-squared-error-identity": true,
    "periodic-smooth32-symmetric:independent-analysis": true,
    "periodic-smooth32-symmetric:left-inverse": true,
    "periodic-smooth32-symmetric:coefficient-count": true,
    "periodic-smooth32-symmetric:padding-energy-ledger": true,
    "periodic-smooth32-symmetric-none:finite-and-owned-shape": true,
    "periodic-smooth32-symmetric-none:independent-synthesis": true,
    "periodic-smooth32-symmetric-none:perfect-reconstruction": true,
    "periodic-smooth32-symmetric-none:critical-squared-error-identity": true,
    "periodic-smooth32-symmetric-hard:finite-and-owned-shape": true,
    "periodic-smooth32-symmetric-hard:independent-synthesis": true,
    "periodic-smooth32-symmetric-hard:critical-squared-error-identity": true,
    "periodic-smooth32-symmetric-soft:finite-and-owned-shape": true,
    "periodic-smooth32-symmetric-soft:independent-synthesis": true,
    "periodic-smooth32-symmetric-soft:critical-squared-error-identity": true,
    "step32-periodic:independent-analysis": true,
    "step32-periodic:left-inverse": true,
    "step32-periodic:coefficient-count": true,
    "step32-periodic:padding-energy-ledger": true,
    "step32-periodic-none:finite-and-owned-shape": true,
    "step32-periodic-none:independent-synthesis": true,
    "step32-periodic-none:perfect-reconstruction": true,
    "step32-periodic-none:critical-squared-error-identity": true,
    "step32-periodic-hard:finite-and-owned-shape": true,
    "step32-periodic-hard:independent-synthesis": true,
    "step32-periodic-hard:critical-squared-error-identity": true,
    "step32-periodic-soft:finite-and-owned-shape": true,
    "step32-periodic-soft:independent-synthesis": true,
    "step32-periodic-soft:critical-squared-error-identity": true,
    "step32-symmetric:independent-analysis": true,
    "step32-symmetric:left-inverse": true,
    "step32-symmetric:coefficient-count": true,
    "step32-symmetric:padding-energy-ledger": true,
    "step32-symmetric-none:finite-and-owned-shape": true,
    "step32-symmetric-none:independent-synthesis": true,
    "step32-symmetric-none:perfect-reconstruction": true,
    "step32-symmetric-none:critical-squared-error-identity": true,
    "step32-symmetric-hard:finite-and-owned-shape": true,
    "step32-symmetric-hard:independent-synthesis": true,
    "step32-symmetric-hard:critical-squared-error-identity": true,
    "step32-symmetric-soft:finite-and-owned-shape": true,
    "step32-symmetric-soft:independent-synthesis": true,
    "step32-symmetric-soft:critical-squared-error-identity": true,
    "ramp17-periodic:independent-analysis": true,
    "ramp17-periodic:left-inverse": true,
    "ramp17-periodic:coefficient-count": true,
    "ramp17-periodic:padding-energy-ledger": true,
    "ramp17-periodic-none:finite-and-owned-shape": true,
    "ramp17-periodic-none:independent-synthesis": true,
    "ramp17-periodic-none:perfect-reconstruction": true,
    "ramp17-periodic-hard:finite-and-owned-shape": true,
    "ramp17-periodic-hard:independent-synthesis": true,
    "ramp17-periodic-soft:finite-and-owned-shape": true,
    "ramp17-periodic-soft:independent-synthesis": true,
    "ramp17-symmetric:independent-analysis": true,
    "ramp17-symmetric:left-inverse": true,
    "ramp17-symmetric:coefficient-count": true,
    "ramp17-symmetric:padding-energy-ledger": true,
    "ramp17-symmetric-none:finite-and-owned-shape": true,
    "ramp17-symmetric-none:independent-synthesis": true,
    "ramp17-symmetric-none:perfect-reconstruction": true,
    "ramp17-symmetric-hard:finite-and-owned-shape": true,
    "ramp17-symmetric-hard:independent-synthesis": true,
    "ramp17-symmetric-soft:finite-and-owned-shape": true,
    "ramp17-symmetric-soft:independent-synthesis": true,
    "step17-periodic:independent-analysis": true,
    "step17-periodic:left-inverse": true,
    "step17-periodic:coefficient-count": true,
    "step17-periodic:padding-energy-ledger": true,
    "step17-periodic-none:finite-and-owned-shape": true,
    "step17-periodic-none:independent-synthesis": true,
    "step17-periodic-none:perfect-reconstruction": true,
    "step17-periodic-hard:finite-and-owned-shape": true,
    "step17-periodic-hard:independent-synthesis": true,
    "step17-periodic-soft:finite-and-owned-shape": true,
    "step17-periodic-soft:independent-synthesis": true,
    "step17-symmetric:independent-analysis": true,
    "step17-symmetric:left-inverse": true,
    "step17-symmetric:coefficient-count": true,
    "step17-symmetric:padding-energy-ledger": true,
    "step17-symmetric-none:finite-and-owned-shape": true,
    "step17-symmetric-none:independent-synthesis": true,
    "step17-symmetric-none:perfect-reconstruction": true,
    "step17-symmetric-hard:finite-and-owned-shape": true,
    "step17-symmetric-hard:independent-synthesis": true,
    "step17-symmetric-soft:finite-and-owned-shape": true,
    "step17-symmetric-soft:independent-synthesis": true,
    "step32-shift1-periodic:independent-analysis": true,
    "step32-shift1-periodic:left-inverse": true,
    "step32-shift1-periodic:coefficient-count": true,
    "step32-shift1-periodic:padding-energy-ledger": true,
    "step32-shift1-periodic-none:finite-and-owned-shape": true,
    "step32-shift1-periodic-none:independent-synthesis": true,
    "step32-shift1-periodic-none:perfect-reconstruction": true,
    "step32-shift1-periodic-none:critical-squared-error-identity": true,
    "step32-shift1-periodic-hard:finite-and-owned-shape": true,
    "step32-shift1-periodic-hard:independent-synthesis": true,
    "step32-shift1-periodic-hard:critical-squared-error-identity": true,
    "step32-shift1-periodic-soft:finite-and-owned-shape": true,
    "step32-shift1-periodic-soft:independent-synthesis": true,
    "step32-shift1-periodic-soft:critical-squared-error-identity": true,
    "step32-shift1-symmetric:independent-analysis": true,
    "step32-shift1-symmetric:left-inverse": true,
    "step32-shift1-symmetric:coefficient-count": true,
    "step32-shift1-symmetric:padding-energy-ledger": true,
    "step32-shift1-symmetric-none:finite-and-owned-shape": true,
    "step32-shift1-symmetric-none:independent-synthesis": true,
    "step32-shift1-symmetric-none:perfect-reconstruction": true,
    "step32-shift1-symmetric-none:critical-squared-error-identity": true,
    "step32-shift1-symmetric-hard:finite-and-owned-shape": true,
    "step32-shift1-symmetric-hard:independent-synthesis": true,
    "step32-shift1-symmetric-hard:critical-squared-error-identity": true,
    "step32-shift1-symmetric-soft:finite-and-owned-shape": true,
    "step32-shift1-symmetric-soft:independent-synthesis": true,
    "step32-shift1-symmetric-soft:critical-squared-error-identity": true,
    "step17-shift1-periodic:independent-analysis": true,
    "step17-shift1-periodic:left-inverse": true,
    "step17-shift1-periodic:coefficient-count": true,
    "step17-shift1-periodic:padding-energy-ledger": true,
    "step17-shift1-periodic-none:finite-and-owned-shape": true,
    "step17-shift1-periodic-none:independent-synthesis": true,
    "step17-shift1-periodic-none:perfect-reconstruction": true,
    "step17-shift1-periodic-hard:finite-and-owned-shape": true,
    "step17-shift1-periodic-hard:independent-synthesis": true,
    "step17-shift1-periodic-soft:finite-and-owned-shape": true,
    "step17-shift1-periodic-soft:independent-synthesis": true,
    "step17-shift1-symmetric:independent-analysis": true,
    "step17-shift1-symmetric:left-inverse": true,
    "step17-shift1-symmetric:coefficient-count": true,
    "step17-shift1-symmetric:padding-energy-ledger": true,
    "step17-shift1-symmetric-none:finite-and-owned-shape": true,
    "step17-shift1-symmetric-none:independent-synthesis": true,
    "step17-shift1-symmetric-none:perfect-reconstruction": true,
    "step17-shift1-symmetric-hard:finite-and-owned-shape": true,
    "step17-shift1-symmetric-hard:independent-synthesis": true,
    "step17-shift1-symmetric-soft:finite-and-owned-shape": true,
    "step17-shift1-symmetric-soft:independent-synthesis": true,
    "fixed-analysis-and-reconstruction-count": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/haar-mallat-boundary-threshold/index.json

![Apply three-level Haar analysis to short signals of lengths 17 and 32, separating one-sample shifts from odd-length boundary handling. Drawn from saved arrays.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/haar-mallat-boundary-threshold-preview.png)

Apply three-level Haar analysis to short signals of lengths 17 and 32, separating one-sample shifts from odd-length boundary handling. Drawn from saved arrays.

![Saved errors, derivatives or squared norms shown separately. The text states the scope of each boundary and representation.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/haar-mallat-boundary-threshold-diagnostics.png)

Saved errors, derivatives or squared norms shown separately. The text states the scope of each boundary and representation.

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/atlas-approximation-controls-2026-11-25.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- S. Mallat, A Theory for Multiresolution Signal Decomposition: The Wavelet Representation [accessed 2026-11-24]. https://www.di.ens.fr/~mallat/papiers/MallatTheory89.pdf; review_level=primary-paper-selected-body
During preparation: title/abstract, Haar example on printed p. 679, selected §III-B/C filter/downsample/inverse-pyramid and border-symmetry prose on p. 681. Extracted formula glyphs were imperfect; no complete proof or numerical-table audit is claimed.

- PyWavelets documentation: Signal extension modes [accessed 2026-11-25]. https://pywavelets.readthedocs.io/en/latest/ref/signal-extension-modes.html; review_level=official-documentation-selected-terminology
Periodic and half-sample symmetric extension and the redundancy caveat. This example defines its own append-at-each-odd-level/crop convention; it does not claim PyWavelets coefficient-layout equivalence or require PyWavelets.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
