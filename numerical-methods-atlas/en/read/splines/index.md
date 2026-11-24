# Spline interpolation

Splines join piecewise low-degree polynomials with specified continuity. Distinguish them from a single global high-degree polynomial and distinguish exact interpolation from smoothing noisy data.

## Problem and representative equations

Use a nondecreasing knot sequence tᵢ and degree p. Nᵢ,₀ is the indicator of [tᵢ,tᵢ₊₁); zero-denominator terms in the recursion are defined as zero. Degree p means order p+1.

$$
N_{i,p}(x)=\frac{x-t_i}{t_{i+p}-t_i}N_{i,p-1}(x)+\frac{t_{i+p+1}-x}{t_{i+p+1}-t_{i+1}}N_{i+1,p-1}(x),\qquad s(x)=\sum_i c_iN_{i,p}(x).
$$

## Algorithm

Represent s=ΣcᵢNᵢ,ₚ and determine coefficients by interpolation or least squares. A natural cubic spline sets endpoint second derivatives to zero; clamped conditions prescribe endpoint first derivatives. Determining coefficients and evaluating the spline by de Boor’s algorithm are separate stages.

## Conditions and pitfalls

An interior knot of multiplicity r generally gives Cᵖ⁻ʳ continuity. Cubic splines do not automatically preserve monotonicity or positivity and can overshoot. Extrapolation depends on the chosen endpoint convention and is not covered by an in-interval interpolation argument.

## What to check

Check polynomial reproduction, one-sided derivatives at knots and endpoint conditions. For noiseless functions study refinement; for noisy data separately report held-out prediction errors and smoothing-parameter dependence.

## Publication scope

Links lead to existing educational code and dated verification records. This reading/translation update changes no scientific code or historical measurements and does not claim reproduction of an entire paper.

## Sources

- Carl de Boor (1972). On calculating with B-splines. https://doi.org/10.1016/0021-9045(72)90080-9
