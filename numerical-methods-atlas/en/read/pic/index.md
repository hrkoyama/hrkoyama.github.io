# Particle-in-cell / PIC

Plasma PIC represents a distribution by computational particles and self-consistent fields by a mesh. Its smoothing, collisionality and sampling error differ from direct all-pairs Coulomb dynamics.

## Problem and representative equations

Start with nonrelativistic electrostatic Vlasov–Poisson. Computational particle p has weight wₚ, charge qₚ and position xₚ. Dimensionless shape weights Sᵢ sum to one, and Vᵢ is cell volume. Deposit ρ, solve Poisson with the stated boundary conditions, and use E=−∇φ.

$$
\rho_i=\frac1{V_i}\sum_p w_pq_pS_i(\mathbf x_p),\qquad -\nabla_h^2\phi_i=\rho_i/\epsilon_0,\qquad \dot{\mathbf v}_p=(q_p/m_p)\mathbf E_h(\mathbf x_p).
$$

## Algorithm

Repeat charge deposition, field solution, particle gathering and particle pushing; include background ions in ρ. Electromagnetic PIC additionally needs current deposition and Maxwell updates consistent with discrete continuity. Dawson’s sheet model is a historical particle-plasma example, not the definition of every PIC discretization.

## Conditions and pitfalls

Explicit electrostatic PIC must examine plasma-frequency time scales and Debye-length resolution. Exact restrictions depend on the particle pusher, shape and field solver. Separate sampling convergence in particle count from grid/time convergence, and check self-force and finite-grid heating.

The companion is one-dimensional periodic electrostatic cold-electron PIC with a fixed uniform ion background. It is a fixed CIC deposit/gather, Poisson-field and particle-push example; thermal Landau damping, electromagnetic PIC and moving ions are outside its scope.

## What to check

Begin with single-particle self-force, a uniform neutral distribution, and small-amplitude plasma oscillations or Landau damping. Report charge, energy drift, particle-count dependence and independent random realizations. Compare damping rates only within the linear-amplitude regime used by the theory.

Use linear cold-plasma oscillation as a small-amplitude reference and vary mesh, time step and particle count separately. Report charge, field residual, self-force, particle momentum and particle-plus-field energy diagnostics separately. Small conservation diagnostics alone guarantee neither trajectory accuracy nor arbitrary long-time stability.

The companion also integrates the fixed CIC spatial system with DOP853 and tests tolerance/maximum-step sensitivity. This is an alternative time-integration algorithm, not an independent continuum Vlasov–Poisson solver. The random particle-count check concerns the initial power of one Fourier charge mode, compared with its analytic expectation including the finite-grid CIC response. It is distinct from particle-count convergence of arbitrary nonlinear trajectories.

## Fixed-input examples and diagnostic controls

Distinguish the scope established by acceptance checks from a general mathematical guarantee; preserve historical inputs, measurements and criteria.

### Cold-plasma oscillation with electrostatic CIC PIC

Fixed-target computation

Couple electrons to a 1D periodic grid by CIC, solving Poisson and particle motion self-consistently.

Finite amplitude and finite particles leave an error floor. Nonlinear instabilities, Landau damping, collisions, electromagnetic/relativistic PIC and open particle boundaries are unvalidated.

[Input, results and acceptance](/numerical-methods-atlas/validation/pic/?lang=en) · [Method and sources](/numerical-methods-atlas/en/read/validation-particles/#pic) · [Code run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/run.py) · [Code electrostatics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/electrostatics.py) · [Code fmm.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/fmm.py) · [Code transport.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/transport.py) · [Tests test_particles.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/test_particles.py) · [ZIP](/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip) · [Results](/code/validated-examples/2026-11-22/particles/results/result.json) · [Rerun receipt](/code/validated-examples/2026-11-22/particles/verification.json)

### PIC: mesh/time convergence, invariants and particle noise

Fixed-target computation

Separate quiet-start refinement of a cold 1D periodic plasma from independent-seed initial particle noise; record charge, momentum, Gauss diagnostics and energy error.

DOP853 is not an independent PIC spatial implementation. Distinguish charge/momentum preservation from approximate energy conservation. Initial-noise N scaling does not validate evolved warm plasmas. Landau damping, electromagnetic/relativistic PIC and collisions remain unvalidated.

[Input, results and acceptance](/numerical-methods-atlas/validation/pic-conservation/?lang=en) · [Method and sources](/numerical-methods-atlas/en/read/validation-particle-transport/#pic-conservation) · [Code run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/run.py) · [Code kinetic_experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/kinetic_experiments.py) · [Code kinetics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/kinetics.py) · [Code longrange_experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/longrange_experiments.py) · [Code electrostatics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/electrostatics.py) · [Code fmm.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/fmm.py) · [Tests test_kinetics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/test_kinetics.py) · [Tests test_longrange.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/test_longrange.py) · [Tests test_runner.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/test_runner.py) · [ZIP](/code/validated-examples/2026-11-22/particle-transport/atlas-particle-transport-2026-11-22.zip) · [Results](/code/validated-examples/2026-11-22/particle-transport/results/result.json) · [Rerun receipt](/code/validated-examples/2026-11-22/particle-transport/verification.json)

## Publication scope

The historical reading, equations, sources and release are preserved; a separate companion release supplies bounded checks for fixed conditions. This does not mean every general verification suggestion above has been executed. Consult each release’s dedicated page and saved record for inputs, references, checks and limits.

## Sources

- John Dawson (1962). One-Dimensional Plasma Model. https://doi.org/10.1063/1.1706638
- Hockney, R. W. and Eastwood, J. W. (1981). Computer Simulation Using Particles. https://doi.org/10.1201/9780367806934
