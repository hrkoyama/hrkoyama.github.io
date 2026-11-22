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

The companion consists of homogeneous Maxwell-molecule elastic pair-collision rounds without positions. It is distinct from physical-time no-time-counter transport with cross sections/relative speeds, spatial hard-sphere motion, walls or inflow boundaries.

## What to check

Test homogeneous velocity relaxation, Maxwellian equilibrium, wall-driven Couette flow or a rarefied shock. Check collision-level momentum/energy conservation, cell/step/particle-count sensitivity and uncertainty accounting for correlated samples.

Derive moments on the finite-particle sphere with fixed momentum/energy here, comparing collision samples with independently projected and normalized Gaussian samples. Scalas et al. provide context for finite microcanonical distributions versus thermodynamic limits; this does not reproduce their complete hard-sphere calculation. Separate between-seed uncertainty and particle-count effects from momentum/energy conservation at each collision.

For the finite system with fixed momentum/energy, a suitably normalized squared velocity component has a Beta distribution. Use this finite-particle reference for 16/64/256 particles and 64 seeds, separating finite-N bias relative to the Maxwell limit from sampling error. The distribution comparison follows 24 collision rounds; rounds are not converted into physical time.

## Fixed-input examples and diagnostic controls

Distinguish the scope established by acceptance checks from a general mathematical guarantee; preserve historical inputs, measurements and criteria.

### Conservation and Maxwell relaxation in a homogeneous DSMC collision component

Fixed-target computation

Test conservation and relaxation toward equilibrium through randomized pair collisions of homogeneous Maxwell molecules.

This is an educational DSMC collision component. No spatial streaming, collision cells, speed-dependent hard-sphere selection, measured transport coefficients/flow fields or every-seed guarantee. Bird’s original hard-sphere conditions are not reproduced.

[Input, results and acceptance](/numerical-methods-atlas/validation/dsmc/?lang=en) · [Method and sources](/numerical-methods-atlas/en/read/validation-particles/#dsmc) · [Code run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/run.py) · [Code electrostatics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/electrostatics.py) · [Code fmm.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/fmm.py) · [Code transport.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/transport.py) · [Tests test_particles.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/test_particles.py) · [ZIP](/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip) · [Results](/code/validated-examples/2026-11-22/particles/results/result.json) · [Rerun receipt](/code/validated-examples/2026-11-22/particles/verification.json)

### DSMC collision component: finite-N equilibrium, invariants and statistical error

Fixed-target computation

Distinguish finite-particle equilibrium from the Maxwell limit; compare independent sphere samples, analytic anisotropy decay and across-seed uncertainty.

Statistical diagnostics cover fixed 64-seed ensembles, not every seed. Conservation correlates particles within a seed; do not use IID KS p-values. No spatial streaming, collision cells, speed-dependent hard-sphere selection or transport coefficients.

[Input, results and acceptance](/numerical-methods-atlas/validation/dsmc-statistics/?lang=en) · [Method and sources](/numerical-methods-atlas/en/read/validation-particle-transport/#dsmc-statistics) · [Code run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/run.py) · [Code kinetic_experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/kinetic_experiments.py) · [Code kinetics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/kinetics.py) · [Code longrange_experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/longrange_experiments.py) · [Code electrostatics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/electrostatics.py) · [Code fmm.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/fmm.py) · [Tests test_kinetics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/test_kinetics.py) · [Tests test_longrange.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/test_longrange.py) · [Tests test_runner.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/test_runner.py) · [ZIP](/code/validated-examples/2026-11-22/particle-transport/atlas-particle-transport-2026-11-22.zip) · [Results](/code/validated-examples/2026-11-22/particle-transport/results/result.json) · [Rerun receipt](/code/validated-examples/2026-11-22/particle-transport/verification.json)

## Publication scope

The historical reading, equations, sources and release are preserved; a separate companion release supplies bounded checks for fixed conditions. This does not mean every general verification suggestion above has been executed. Consult each release’s dedicated page and saved record for inputs, references, checks and limits.

## Sources

- G. A. Bird (1963). Approach to Translational Equilibrium in a Rigid Sphere Gas. https://doi.org/10.1063/1.1710976
- G. A. Bird (1994). Molecular Gas Dynamics and the Direct Simulation of Gas Flows. https://global.oup.com/academic/product/molecular-gas-dynamics-and-the-direct-simulation-of-gas-flows-9780198561958
- Scalas, Enrico; Gabriel, Adrian T.; Martin, Edgar; Germano, Guido (2015). Velocity and energy distributions in microcanonical ensembles of hard spheres. https://doi.org/10.1103/PhysRevE.92.022140
