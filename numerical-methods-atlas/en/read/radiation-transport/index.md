# Radiation transport and moment methods

Radiation transport resolves intensity in space, direction and frequency. Moment methods reduce the angular dimension but require closure for information removed by integration.

## Problem and representative equations

Use frequency-integrated grey intensity I in a static medium, with isotropic emissivity η and absorption coefficient κ of inverse-length units; omit scattering here. Define E=(1/c)∫I dΩ, F=∫nI dΩ and P=(1/c)∫nnI dΩ. Moment equations for E and F require a prescription for P.

$$
\frac1c\partial_t I+\mathbf n\cdot\nabla I=\eta-\kappa I,\qquad\partial_t E+\nabla\cdot\mathbf F=4\pi\eta-c\kappa E,\qquad c^{-2}\partial_t\mathbf F+\nabla\cdot\mathbf P=-\kappa\mathbf F/c.
$$

## Algorithm

Discrete ordinates discretizes angle directly; moment methods close P=D E. M1 obtains D locally from E and F, while flux-limited diffusion instead approximates F from the gradient of E. Check optically thick and free-streaming limits and couple matter exchange through a consistent energy balance.

## Conditions and pitfalls

M1 generally cannot propagate crossing beams independently. FLD ties flux to the energy gradient, limiting shadows and strongly anisotropic fields. A reduced light speed changes transport/relaxation scales and must be justified against the physical time scales of interest.

The companion retains a one-dimensional steady purely absorbing slab with specified inflow, solving μ∂xI=−κI. General radiation moment closures, scattering, time dependence, multiple frequencies and fluid coupling are unvalidated.

## What to check

Test exponential absorption, isotropic diffusion, free streaming/shadows and crossing beams separately. Check E≥0, |F|≤cE, matter-plus-radiation energy and angular/spatial/time convergence. Distinguish closure error from discretization error.

Use directional Beer–Lambert solutions and a continuum-angle exponential integral, separating upwind spatial error at fixed ordinates from angular-quadrature error with exact ray propagation. Check inflow–outflow versus volume absorption and positivity separately; a balance check alone does not establish angular-distribution accuracy.

At optical depths 0.1/0.7/3, cross-check the continuum-angle reference using expn and a separate adaptive QUADPACK quadrature. Independent transport sampling draws μ=√U for the incident flux and counts transmission as a Bernoulli variable. Check binomial intervals and RMSE over 64 finite-sample replicates; nominal 95% coverage is not claimed for arbitrary inputs or samples.

## Fixed-input examples and diagnostic controls

Distinguish the scope established by acceptance checks from a general mathematical guarantee; preserve historical inputs, measurements and criteria.

### Discrete-ordinate radiation transport through an absorbing slab

Fixed-target computation

Discretize steady pure-absorption transfer in angle and space, checking Beer–Lambert rays and integrated exit flux.

Multiple scattering, thermal emission, frequency redistribution, moving media and radiation–fluid coupling are unimplemented. This does not reproduce full DISORT functionality/stabilization.

[Input, results and acceptance](/numerical-methods-atlas/validation/radiation-transport/?lang=en) · [Method and sources](/numerical-methods-atlas/en/read/validation-particles/#radiation-transport) · [Code run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/run.py) · [Code electrostatics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/electrostatics.py) · [Code fmm.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/fmm.py) · [Code transport.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/transport.py) · [Tests test_particles.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/test_particles.py) · [ZIP](/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip) · [Results](/code/validated-examples/2026-11-22/particles/results/result.json) · [Rerun receipt](/code/validated-examples/2026-11-22/particles/verification.json)

### Radiation transport: space/angle convergence and photon statistics

Fixed-target computation

Compare characteristics, independent adaptive integration and photon survival in a pure-absorption slab; separate discrete balance, sampling error and interval coverage.

Coverage is observed over finite fixed seeds; neither exactly 95% empirical coverage nor all-seed success is guaranteed. Keep deterministic quadrature error separate from statistical error. Multiple scattering, frequency dependence, thermal emission and radiation hydrodynamics are unvalidated.

[Input, results and acceptance](/numerical-methods-atlas/validation/radiation-convergence/?lang=en) · [Method and sources](/numerical-methods-atlas/en/read/validation-particle-transport/#radiation-convergence) · [Code run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/run.py) · [Code kinetic_experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/kinetic_experiments.py) · [Code kinetics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/kinetics.py) · [Code longrange_experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/longrange_experiments.py) · [Code electrostatics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/electrostatics.py) · [Code fmm.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/fmm.py) · [Tests test_kinetics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/test_kinetics.py) · [Tests test_longrange.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/test_longrange.py) · [Tests test_runner.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/test_runner.py) · [ZIP](/code/validated-examples/2026-11-22/particle-transport/atlas-particle-transport-2026-11-22.zip) · [Results](/code/validated-examples/2026-11-22/particle-transport/results/result.json) · [Rerun receipt](/code/validated-examples/2026-11-22/particle-transport/verification.json)

## Publication scope

The historical reading, equations, sources and release are preserved; a separate companion release supplies bounded checks for fixed conditions. This does not mean every general verification suggestion above has been executed. Consult each release’s dedicated page and saved record for inputs, references, checks and limits.

## Sources

- C.D. Levermore (1984). Relating Eddington factors to flux limiters. https://doi.org/10.1016/0022-4073(84)90112-2
