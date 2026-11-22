# Gaussian and adaptive quadrature

Gaussian quadrature selects nodes and weights for a measure to integrate polynomials efficiently. Adaptive integration separately allocates function evaluations using local error estimates.

## Problem and representative equations

For a positive measure, an n-point Gaussian rule is exact through degree 2n−1 when the required moments exist. The Jacobi matrix J of orthogonal-polynomial recurrence coefficients has quadrature nodes as eigenvalues. Weights are μ₀ times squared first components of normalized eigenvectors, with μ₀=∫w.

$$
\int_a^b f(x)w(x)\,dx\approx\sum_{j=1}^n\omega_jf(x_j),\qquad Jv_j=x_jv_j,\quad\omega_j=\mu_0(v_j)_1^2.
$$

## Algorithm

Golub–Welsch solves this symmetric tridiagonal eigenproblem. Adaptive Gauss–Kronrod-type integration uses differences between nested rules to estimate local errors, subdivides intervals and checks absolute/relative tolerances. The rule difference is not an unconditional error bound.

## Conditions and pitfalls

Singularities, jumps, rapid oscillations and narrow peaks can be missed by sampled nodes. Split at known discontinuities and consider transformations or matched weighted rules. Relative tolerance alone is unsuitable when the integral is close to zero.

When cancellation makes an integral small, a cancellation condition number such as integral(|f|)/|integral(f)| is informative. Absolute/relative true errors differ from a rule’s internal error estimate. If finitely many sample points miss a narrow bump, agreement between two approximations can coexist with a large true integration error. State the input-perturbation norm and perturbation model when comparing condition numbers; if the integral is zero, relative condition and relative error are undefined, so report absolute quantities.

## What to check

Verify degree of exactness on monomials, then test nonpolynomials with known integrals, singularities and narrow peaks. Record estimated versus true error, evaluation count and termination caused by subdivision limits.

The added release varies rule order and tolerance for smooth functions with known integrals, cancellation-sensitive functions and a fixed narrow-bump control. Compare against independent references and record true error, estimated error and function evaluations separately. Distinguish an explicitly split calculation that resolves the bump from a missed-bump diagnostic; neither supplies a universal guarantee for all integrands. Compare an endpoint-derivative singularity before and after a change of variables, and retain evaluation/depth-budget exhaustion as an explicit termination status.

## Fixed-input examples and diagnostic controls

Distinguish the scope established by acceptance checks from a general mathematical guarantee; preserve historical inputs, measurements and criteria.

### Gauss–Legendre and adaptive quadrature: exactness, error estimates and budgets

Fixed-target computation

Construct Gaussian nodes/weights from the Legendre recurrence and test polynomial moments through degree 2n−1 and an exponential. Adaptive Simpson integrates exponential and Lorentzian peaks, against analytic integrals and independent QUADPACK.

The local Simpson estimate is not a rigorous error bound for arbitrary functions. The implementation does not generally solve missed high frequencies, singularities or roundoff stagnation, and it is not a reimplementation of Gauss–Kronrod or all of QUADPACK.

[Input, results and acceptance](/numerical-methods-atlas/validation/gauss-adaptive-quadrature/?lang=en) · [Method and sources](/numerical-methods-atlas/en/read/validation-foundations/#gauss-adaptive-quadrature) · [Code run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/run.py) · [Code solvers.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/solvers.py) · [Tests test_foundations.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/test_foundations.py) · [ZIP](/code/validated-examples/2026-11-22/foundations/atlas-foundations-2026-11-22.zip) · [Results](/code/validated-examples/2026-11-22/foundations/results/result.json) · [Rerun receipt](/code/validated-examples/2026-11-22/foundations/verification.json)

### Quadrature: narrow peaks, cancellation, endpoints and estimator blind spots

Fixed-target computation

Vary Gauss order and adaptive tolerance on narrow Lorentz peaks, a square-root endpoint, severe cancellation, a zero integral and a deliberately missed compact bump, using analytic integrals and QUADPACK.

The Simpson estimate is not a certified error bound. Passing the blind-spot control does not mean accurate integration. Direct square-root integration may honestly terminate at its depth budget. Exhaustive oscillatory/singular exploration and certified quadrature are not claimed.

[Input, results and acceptance](/numerical-methods-atlas/validation/quadrature-conditioning/?lang=en) · [Method and sources](/numerical-methods-atlas/en/read/validation-foundations-conditioning/#quadrature-conditioning) · [Code run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/run.py) · [Code experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/experiments.py) · [Code fixtures.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/fixtures.py) · [Code mpmath_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/mpmath_reference.py) · [Code solvers.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/solvers.py) · [Tests test_conditioning.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/test_conditioning.py) · [ZIP](/code/validated-examples/2026-11-22/foundations-conditioning/atlas-foundations-conditioning-2026-11-22.zip) · [Results](/code/validated-examples/2026-11-22/foundations-conditioning/results/result.json) · [Rerun receipt](/code/validated-examples/2026-11-22/foundations-conditioning/verification.json)

## Publication scope

Historical inputs, measurements and tolerances are preserved. Additional conditioning, residual and convergence checks have a separate scoped release. Passing a diagnostic control can mean that its intended limitation was observed; it does not establish general success or reproduction of an entire paper.

## Sources

- Gene H. Golub and John H. Welsch (1969). Calculation of Gauss quadrature rules. https://doi.org/10.1090/s0025-5718-69-99647-1
- Robert Piessens and Elise de Doncker-Kapenga and Christoph W. Überhuber and David K. Kahaner (1983). QUADPACK: A Subroutine Package for Automatic Integration. https://doi.org/10.1007/978-3-642-61786-7
- P. Gonnet (2010). Increasing the Reliability of Adaptive Quadrature Using Explicit Interpolants. https://doi.org/10.1145/1824801.1824804
