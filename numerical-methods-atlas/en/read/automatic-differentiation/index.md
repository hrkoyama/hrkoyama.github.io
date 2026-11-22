# Automatic differentiation

Automatic differentiation applies the chain rule to elementary operations in a program. It is distinct from symbolic manipulation and from finite-difference differentiation with a chosen step.

## Problem and representative equations

For z=φ(x), forward mode propagates ż=φ_x ẋ; reverse mode accumulates φ_xᵀz̄ into x̄. Floating-point rounding remains, so derivatives are not literally error-free, but there is no finite-difference truncation step.

$$
\dot z=\frac{\partial\phi}{\partial x}\dot x,\qquad \bar x\mathrel{+}=\left(\frac{\partial\phi}{\partial x}\right)^T\bar z,\qquad w^T(Jv)=v^T(J^Tw).
$$

## Algorithm

Decompose the computation into elementary operations and store values with tangents or the history needed for reverse accumulation. Few input directions favor forward mode; a scalar output with many inputs favors reverse mode. Distinguish differentiating solver iterations from implicitly differentiating the converged solution.

## Conditions and pitfalls

Branches differentiate the executed path. Check nondifferentiability and conventions for abs, max, limiters, contacts and events. Audit stop-gradient, external primitives and iterative stopping. AD is not a guarantee of a classical derivative of every discontinuous bit-level operation.

## What to check

Test analytic elementary cases, directional Taylor remainders and the duality identity wᵀ(Jv)=vᵀ(Jᵀw). Avoid finite-difference steps so small that rounding dominates. Include boundary and parameter dependence when differentiating PDE residuals.

## Publication scope

Reading, representative equations and sources are published. Dedicated code and numerical verification remain planned. The suggested checks above are not measured results, and code/results of other methods are not presented as validation of this method.

## Sources

- R. E. Wengert (1964). A simple automatic derivative evaluation program. https://doi.org/10.1145/355586.364791
- Seppo Linnainmaa (1976). Taylor expansion of the accumulated rounding error. https://doi.org/10.1007/bf01931367
