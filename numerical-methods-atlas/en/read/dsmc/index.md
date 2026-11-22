# DSMC and kinetic transport

DSMC approximates dilute-gas Boltzmann collisions by stochastic collisions between computational particles. It differs from deterministic pair-potential molecular dynamics and from self-consistent plasma PIC fields.

## Problem and representative equations

Consider Boltzmann f with molecular velocity v, acceleration a and collision operator Q. A simulator particle represents F_N physical molecules. In a cell of volume V_c, sample pair collisions according to total cross section σ_T and relative speed g. State the phase-space number-density normalization of f.

$$
\partial_t f+\mathbf v\cdot\nabla_x f+\mathbf a\cdot\nabla_v f=Q(f,f),\qquad P_{\rm pair}\sim \frac{F_N\sigma_T g\,\Delta t}{V_c}.
$$

## Algorithm

Move particles, apply wall/boundary interactions and sample collisions within cells. A representative no-time-counter algorithm uses a bound on gσ_T for candidate selection and acceptance. Specify hard-sphere, VHS or another collision model, distinguishing Bird’s early construction from later algorithms.

## Conditions and pitfalls

DSMC uses dilute-gas and molecular-chaos assumptions. Compare cell size with mean free path and step size with mean collision time; adequate resolution is problem dependent. In low-speed flow, the macroscopic signal can be buried in thermal noise, and longer averaging does not remove discretization bias.

## What to check

Test homogeneous velocity relaxation, Maxwellian equilibrium, wall-driven Couette flow or a rarefied shock. Check collision-level momentum/energy conservation, cell/step/particle-count sensitivity and uncertainty accounting for correlated samples.

## Publication scope

Reading, representative equations and sources are published. Dedicated code and numerical verification remain planned. The suggested checks above are not measured results, and code/results of other methods are not presented as validation of this method.

## Sources

- G. A. Bird (1963). Approach to Translational Equilibrium in a Rigid Sphere Gas. https://doi.org/10.1063/1.1710976
- G. A. Bird (1994). Molecular Gas Dynamics and the Direct Simulation of Gas Flows. https://global.oup.com/academic/product/molecular-gas-dynamics-and-the-direct-simulation-of-gas-flows-9780198561958
