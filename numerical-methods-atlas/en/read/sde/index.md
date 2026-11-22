# Stochastic differential equations

Brownian increments in an SDE scale as √Δt. Adding random numbers to an ODE solver does not by itself specify the stochastic interpretation or convergence order.

## Problem and representative equations

The formula uses a scalar Itô SDE. a is drift, b is diffusion and ΔWₙ are independent Gaussian increments with mean zero and variance Δt. Euler–Maruyama evaluates both coefficients at n. Converting a Stratonovich equation requires the appropriate drift correction.

$$
dX=a(X,t)\,dt+b(X,t)\,dW,\qquad X_{n+1}=X_n+a(X_n,t_n)\Delta t+b(X_n,t_n)\Delta W_n.
$$

## Algorithm

Generate Wiener increments and advance deterministic and stochastic terms. Strong-error refinement must couple paths by summing fine increments into the coarse increment. Weak error concerns expectations of test functions, not the discrepancy of one pair of paths.

## Conditions and pitfalls

Under suitable global Lipschitz, moment and smoothness assumptions, Euler–Maruyama typically has strong order 1/2 and weak order 1. Superlinear growth or positivity constraints can invalidate the method and require specialized treatments. Sampling uncertainty may dominate weak discretization error.

## What to check

Use geometric Brownian exact paths and Ornstein–Uhlenbeck moments to test strong and weak convergence separately. Record step size, random streams, sample count and uncertainty, including negative states or boundary violations.

## Publication scope

Euler–Maruyama for scalar geometric Brownian motion. Coarse/fine steps and analytic endpoints share the same Brownian paths; measure strong RMS error across 4096 paths. Does not validate general SDEs, MCMC or weak convergence order. Inputs, code, measured values and tolerances are linked from the method and execution pages. Not every general verification proposal above has been executed.

## Sources

- Gisiro Maruyama (1955). Continuous Markov processes and stochastic equations. https://doi.org/10.1007/bf02846028
- Desmond J. Higham (2001). An Algorithmic Introduction to Numerical Simulation of Stochastic Differential Equations. https://doi.org/10.1137/s0036144500378302
