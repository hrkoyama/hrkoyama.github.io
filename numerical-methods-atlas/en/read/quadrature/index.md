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

## What to check

Verify degree of exactness on monomials, then test nonpolynomials with known integrals, singularities and narrow peaks. Record estimated versus true error, evaluation count and termination caused by subdivision limits.

## Publication scope

Links lead to existing educational code and dated verification records. This reading/translation update changes no scientific code or historical measurements and does not claim reproduction of an entire paper.

## Sources

- Gene H. Golub and John H. Welsch (1969). Calculation of Gauss quadrature rules. https://doi.org/10.1090/s0025-5718-69-99647-1
- Robert Piessens and Elise de Doncker-Kapenga and Christoph W. Überhuber and David K. Kahaner (1983). QUADPACK: A Subroutine Package for Automatic Integration. https://doi.org/10.1007/978-3-642-61786-7
