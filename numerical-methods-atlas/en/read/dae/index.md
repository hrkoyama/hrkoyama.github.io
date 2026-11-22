# Differential-algebraic equations / DAE

A DAE combines differential evolution with algebraic constraints. An implicit ODE is not necessarily a DAE; singular dependence on derivatives is central to the distinction.

## Problem and representative equations

Use F(t,y,ẏ)=0. A semi-explicit system ẋ=f(x,z,t), 0=g(x,z,t) with invertible g_z is a representative locally eliminable index-1 case. Several index definitions exist; differentiation index concerns differentiating constraints to obtain an explicit ODE.

$$
F(t,y,\dot y)=0,\qquad \dot y_{n+1}\approx\frac{\alpha_0y_{n+1}+\sum_{j=1}^k\alpha_jy_{n+1-j}}{\Delta t},\qquad J_N=F_y+\frac{\alpha_0}{\Delta t}F_{\dot y}.
$$

## Algorithm

BDF methods approximate ẏ from the state history and solve F=0 using Newton iterations. The Newton matrix includes F_y+α₀F_ẏ/Δt. Initial values and derivatives must be consistent with both algebraic constraints and F(t₀,y₀,ẏ₀)=0.

## Conditions and pitfalls

Higher-index systems can contain hidden constraints, drift and degraded error control, requiring index reduction or projection formulations. Smaller ODE time steps alone do not fix these issues. Scale tolerances separately for differential and algebraic variables and their units.

## What to check

For an index-1 system with known solution, measure state error, F residual, algebraic-constraint violation and initialization consistency. Vary steps, nonlinear tolerances and initial perturbations; record constraint drift and termination reasons.

## Publication scope

Reading, representative equations and sources are published. Dedicated code and numerical verification remain planned. The suggested checks above are not measured results, and code/results of other methods are not presented as validation of this method.

## Sources

- C. Gear (1971). Simultaneous Numerical Solution of Differential-Algebraic Equations. https://doi.org/10.1109/tct.1971.1083221
