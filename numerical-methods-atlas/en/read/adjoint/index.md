# Adjoint methods and inverse problems

Adjoints efficiently compute sensitivities when state and parameter dimensions are large but there are few objectives. Obtaining a gradient does not establish uniqueness of an inverse problem.

## Problem and representative equations

For a discrete state equation R(u,m)=0 and scalar objective J, define L=J−λᵀR. With suitable invertibility of R_u, solve R_uᵀλ=J_uᵀ to avoid explicit state sensitivities for every parameter. Subscripts denote partial derivatives; the signs follow this Lagrangian convention.

$$
R_u^T\lambda=J_u^T,\qquad \frac{dJ}{dm}=J_m-\lambda^TR_m.
$$

## Algorithm

Solve the forward state, solve the adjoint using residual/objective derivatives, then assemble the gradient. Transient problems need forward-state history and a storage/recomputation strategy. Discretizing a continuous adjoint and differentiating a discretization need not agree on a finite mesh.

## Conditions and pitfalls

Differentiate boundary conditions, mesh/coordinate dependence, observations and regularization consistently. Nonsmooth limiters and moving shocks challenge ordinary differentiability assumptions. Incomplete forward or adjoint convergence contaminates gradients.

## What to check

Use directional Taylor tests: J(m+hv)−J(m)−h∇J·v should behave as O(h²) in a smooth, sufficiently converged regime. Add adjoint inner-product and finite-difference tests. Assess identifiability, regularization and data error separately for the inverse problem.

## Publication scope

Reading, representative equations and sources are published. Dedicated code and numerical verification remain planned. The suggested checks above are not measured results, and code/results of other methods are not presented as validation of this method.

## Sources

- Antony Jameson (1988). Aerodynamic design via control theory. https://doi.org/10.1007/bf01061285
- Seppo Linnainmaa (1976). Taylor expansion of the accumulated rounding error. https://doi.org/10.1007/bf01931367
