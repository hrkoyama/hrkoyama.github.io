# Fixed interpolation, spline and Haar controls

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-approximation-controls/

Resources explicitly registered to the methods, problems and executions of this chapter. Small fixed examples separate nodes, representation and rounding; C2 continuity and shape preservation; and boundary extension and shifts.

## Methods

- [Chebyshev approximation](<https://hrkoyama.github.io/numerical-methods-atlas/methods/chebyshev/?lang=en>)

  Implement the second barycentric formula and a full-coefficient Clenshaw recurrence. Retain the closed weights and finite Chebyshev transform on rounded nodes.
- [Spline interpolation](<https://hrkoyama.github.io/numerical-methods-atlas/methods/splines/?lang=en>)

  Solve a cubic B-spline collocation system and evaluate it with de Boor recursion. A separate path implements PCHIP harmonic slopes, endpoint limiting and Hermite evaluation.
- [PCHIP monotone cubic Hermite interpolation](<https://hrkoyama.github.io/numerical-methods-atlas/methods/pchip/?lang=en>)

  Solve a cubic B-spline collocation system and evaluate it with de Boor recursion. A separate path implements PCHIP harmonic slopes, endpoint limiting and Hermite evaluation.
- [Wavelets](<https://hrkoyama.github.io/numerical-methods-atlas/methods/wavelets/?lang=en>)

  Implement pair-sum and pair-difference filters, downsampling and inverse pyramids. Reconstruct with no threshold, hard thresholding and soft thresholding from the same analysis coefficients.
- [Chebyshev approximation](<https://hrkoyama.github.io/numerical-methods-atlas/methods/chebyshev/?lang=en>)
- [Spline interpolation](<https://hrkoyama.github.io/numerical-methods-atlas/methods/splines/?lang=en>)
- [PCHIP monotone cubic Hermite interpolation](<https://hrkoyama.github.io/numerical-methods-atlas/methods/pchip/?lang=en>)
- [Wavelets](<https://hrkoyama.github.io/numerical-methods-atlas/methods/wavelets/?lang=en>)

## Equations

- [Polynomial interpolation on stored nodes](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#polynomial-interpolation-en>)

  Separate closed-weight representation on rounded nodes, interpolation error and evaluation rounding. Dimensionless interval [-1,1], degrees 8, 16 and 32, and 2048 fixed midpoints. Actual binary64 nodes, data and weights define the discrete problem.
- [Cubic splines and shape-preserving interpolation](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#cubic-spline-pchip-en>)

  Distinguish C2 interpolation with endpoint conditions from monotone piecewise Hermite interpolation. Use actual binary64 knots and values. Natural conditions set both endpoint second derivatives to zero; clamped conditions prescribe the first derivatives from the input.
- [Discrete Haar transforms of finite signals](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#discrete-haar-transform-en>)

  A finite map including odd-length padding and cropping; global orthogonality is not assumed for redundant extensions. At each odd-length level append the first sample for periodic extension or the last for symmetric extension, then crop during synthesis. Apply threshold 0.2 only to detail coefficients.
- [Polynomial interpolation on stored nodes](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#polynomial-interpolation-en>)

  Separate closed-weight representation on rounded nodes, interpolation error and evaluation rounding.
- [Cubic splines and shape-preserving interpolation](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#cubic-spline-pchip-en>)

  Distinguish C2 interpolation with endpoint conditions from monotone piecewise Hermite interpolation.
- [Discrete Haar transforms of finite signals](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#discrete-haar-transform-en>)

  A finite map including odd-length padding and cropping; global orthogonality is not assumed for redundant extensions.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/runge-barycentric-clenshaw/?lang=en#runge-barycentric-clenshaw-en-algorithm>)

  Implement the second barycentric formula and a full-coefficient Clenshaw recurrence. Retain the closed weights and finite Chebyshev transform on rounded nodes.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/spline-shape-controls/?lang=en#spline-shape-controls-en-algorithm>)

  Solve a cubic B-spline collocation system and evaluate it with de Boor recursion. A separate path implements PCHIP harmonic slopes, endpoint limiting and Hermite evaluation.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/haar-mallat-boundary-threshold/?lang=en#haar-mallat-boundary-threshold-en-algorithm>)

  Implement pair-sum and pair-difference filters, downsampling and inverse pyramids. Reconstruct with no threshold, hard thresholding and soft thresholding from the same analysis coefficients.

## Problem figures

- [Runge interpolation: nodes, representation and rounding](<https://hrkoyama.github.io/numerical-methods-atlas/problems/runge-barycentric-clenshaw/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/runge-barycentric-clenshaw-preview.png
- [Natural and clamped splines versus PCHIP](<https://hrkoyama.github.io/numerical-methods-atlas/problems/spline-shape-controls/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/spline-shape-controls-preview.png
- [Haar multiresolution: boundaries, shifts and thresholds](<https://hrkoyama.github.io/numerical-methods-atlas/problems/haar-mallat-boundary-threshold/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/haar-mallat-boundary-threshold-preview.png
- [Runge interpolation: nodes, representation and rounding](<https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/runge-barycentric-clenshaw.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/runge-barycentric-clenshaw.png
- [Natural and clamped splines versus PCHIP](<https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/spline-shape-controls.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/spline-shape-controls.png
- [Haar multiresolution: boundaries, shifts and thresholds](<https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/haar-mallat-boundary-threshold.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/haar-mallat-boundary-threshold.png

## Exact / reference solutions

- [Runge interpolation: nodes, representation and rounding — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/runge-barycentric-clenshaw/?lang=en#references-en>)

  Separate the stored-data polynomial P, closed-weight rational expression R, stored-coefficient series C and target f. Check exact rational references at 17 probes, operation-based error bounds, node identities and fixed Runge trends.
- [Runge interpolation: nodes, representation and rounding](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-runge-barycentric-clenshaw-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference Dimensionless interval [-1,1], degrees 8, 16 and 32, and 2048 fixed midpoints. Actual binary64 nodes, data and weights define the discrete problem. A sampled maximum error is not a proof of a continuous uniform norm. Closed weights and discrete orthogonality on rounded nodes are not treated as exact. No arbitrary-degree or all-point stability guarantee is made.
- [Natural and clamped splines versus PCHIP — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/spline-shape-controls/?lang=en#references-en>)

  Compare with exact rational second-derivative systems, rational PCHIP and SciPy 1.14.1. Fifteen endpoint records contain sixteen scalar outputs from thirteen distinct inputs. Independent Fraction formulas show plateau undershoot for the actual binary64 data.
- [Natural and clamped splines versus PCHIP](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-spline-shape-controls-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference Use actual binary64 knots and values. Natural conditions set both endpoint second derivatives to zero; clamped conditions prescribe the first derivatives from the input. PCHIP is generally C1, not necessarily C2. Best approximation, extrapolation and noise smoothing are outside scope. A SciPy comparison does not substitute for reading the original papers.
- [Haar multiresolution: boundaries, shifts and thresholds — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/haar-mallat-boundary-threshold/?lang=en#references-en>)

  Use twelve analyses and thirty-six reconstructions. Check independent matrices, Fraction/Decimal coefficients, perfect reconstruction and squared L2 errors. Require the orthogonal error identity only at length 32; retain level-by-level padding energy at length 17.
- [Haar multiresolution: boundaries, shifts and thresholds](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-haar-mallat-boundary-threshold-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference At each odd-length level append the first sample for periodic extension or the last for symmetric extension, then crop during synthesis. Apply threshold 0.2 only to detail coefficients. Limited to Haar, without longer filters or image compression. General symmetric extension is not assumed orthonormal. Shift invariance is not required; shift-dependent differences are retained.
- [Runge interpolation: nodes, representation and rounding](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-runge-barycentric-clenshaw-en>)
  reference_kind: analytic

  Analytic reference Dimensionless interval [-1,1], degrees 8, 16 and 32, and 2048 fixed midpoints. Actual binary64 nodes, data and weights define the discrete problem.
- [Natural and clamped splines versus PCHIP](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-spline-shape-controls-en>)
  reference_kind: analytic

  Analytic reference Use actual binary64 knots and values. Natural conditions set both endpoint second derivatives to zero; clamped conditions prescribe the first derivatives from the input.
- [Haar multiresolution: boundaries, shifts and thresholds](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-haar-mallat-boundary-threshold-en>)
  reference_kind: analytic

  Analytic reference At each odd-length level append the first sample for periodic extension or the last for symmetric extension, then crop during synthesis. Apply threshold 0.2 only to detail coefficients.
- [Runge interpolation: nodes, representation and rounding — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/runge-barycentric-clenshaw/?lang=en#runge-barycentric-clenshaw-en-validation>)

  Separate the stored-data polynomial P, closed-weight rational expression R, stored-coefficient series C and target f. Check exact rational references at 17 probes, operation-based error bounds, node identities and fixed Runge trends.
- [Runge interpolation: nodes, representation and rounding](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-runge-barycentric-clenshaw-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference Dimensionless interval [-1,1], degrees 8, 16 and 32, and 2048 fixed midpoints. Actual binary64 nodes, data and weights define the discrete problem. A sampled maximum error is not a proof of a continuous uniform norm. Closed weights and discrete orthogonality on rounded nodes are not treated as exact. No arbitrary-degree or all-point stability guarantee is made.
- [Natural and clamped splines versus PCHIP — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/spline-shape-controls/?lang=en#spline-shape-controls-en-validation>)

  Compare with exact rational second-derivative systems, rational PCHIP and SciPy 1.14.1. Fifteen endpoint records contain sixteen scalar outputs from thirteen distinct inputs. Independent Fraction formulas show plateau undershoot for the actual binary64 data.
- [Natural and clamped splines versus PCHIP](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-spline-shape-controls-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference Use actual binary64 knots and values. Natural conditions set both endpoint second derivatives to zero; clamped conditions prescribe the first derivatives from the input. PCHIP is generally C1, not necessarily C2. Best approximation, extrapolation and noise smoothing are outside scope. A SciPy comparison does not substitute for reading the original papers.
- [Haar multiresolution: boundaries, shifts and thresholds — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/haar-mallat-boundary-threshold/?lang=en#haar-mallat-boundary-threshold-en-validation>)

  Use twelve analyses and thirty-six reconstructions. Check independent matrices, Fraction/Decimal coefficients, perfect reconstruction and squared L2 errors. Require the orthogonal error identity only at length 32; retain level-by-level padding energy at length 17.
- [Haar multiresolution: boundaries, shifts and thresholds](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-haar-mallat-boundary-threshold-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference At each odd-length level append the first sample for periodic extension or the last for symmetric extension, then crop during synthesis. Apply threshold 0.2 only to detail coefficients. Limited to Haar, without longer filters or image compression. General symmetric extension is not assumed orthonormal. Shift invariance is not required; shift-dependent differences are retained.

## Code and validation

- [Runge interpolation: nodes, representation and rounding](<https://hrkoyama.github.io/numerical-methods-atlas/validation/runge-barycentric-clenshaw/?lang=en>)
  availability: run

  Interpolate the Runge and absolute-value functions on fixed equispaced and Lobatto-like nodes, and compare with Clenshaw evaluation.
- [Natural and clamped splines versus PCHIP](<https://hrkoyama.github.io/numerical-methods-atlas/validation/spline-shape-controls/?lang=en>)
  availability: run

  Compare C2 continuity and shape preservation on three fixed data sets: a monotone plateau, a cubic and a straight line.
- [Haar multiresolution: boundaries, shifts and thresholds](<https://hrkoyama.github.io/numerical-methods-atlas/validation/haar-mallat-boundary-threshold/?lang=en>)
  availability: run

  Apply three-level Haar analysis to short signals of lengths 17 and 32, separating one-sample shifts from odd-length boundary handling.
