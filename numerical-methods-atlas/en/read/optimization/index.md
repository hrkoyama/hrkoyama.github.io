# Gradient and quasi-Newton optimization

Gradient and quasi-Newton optimization

Gradient methods use first derivatives; quasi-Newton methods infer curvature from gradient differences. This introduction treats smooth unconstrained minimization, separately from constrained optimality conditions.

Problem and representative equations

Let gₖ=∇f(xₖ), Hₖ approximate the inverse Hessian and pₖ=−Hₖgₖ. In BFGS, s=xₖ₊₁−xₖ, y=gₖ₊₁−gₖ and ρ=1/(yᵀs). Hₖ=I gives steepest descent in the chosen coordinates, so units and scaling matter.


$$
x_{k+1}=x_k-\alpha_kH_kg_k,\qquad H_{k+1}=(I-\rho sy^T)H_k(I-\rho ys^T)+\rho ss^T.
$$
Algorithm

Evaluate gradients, select a step length using a line search and update curvature. BFGS enforces Hₖ₊₁y=s with a symmetric update. Positive-definite Hₖ and yᵀs>0 preserve positive definiteness. Poor curvature requires an explicit policy such as skipping or damping the update.

Conditions and pitfalls

For nonconvex problems, finding a local stationary point is different from finding a global optimum. Noisy gradients, nonsmooth objectives and inaccurate inner PDE solves can corrupt curvature. Do not stop on relative objective change alone: inspect gradient norms, step sizes, limits and termination reasons.

What to check

Vary conditioning on positive-definite quadratics with known minima and check gradients by directional differences. On curved valleys vary initialization, scaling and line searches. Decreasing an objective does not validate physical assumptions or constraints.

[Verified implementation example: adjoint-gradient fitting of the Bratu synthetic inverse problem](/numerical-methods-atlas/en/read/bratu-inverse/)

## Publication scope

This page gives general gradient/quasi-Newton reading. Implemented scope is the separate Bratu synthetic inverse example: a scalar box-constrained projected-gradient method with Armijo backtracking. BFGS, general quasi-Newton methods and the broader checks proposed on this page are not implemented or verified by that example.

## Sources

- R. Fletcher (1970). A new approach to variable metric algorithms. https://doi.org/10.1093/comjnl/13.3.317
