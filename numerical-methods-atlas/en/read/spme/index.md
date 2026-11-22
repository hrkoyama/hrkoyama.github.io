# Smooth particle mesh Ewald / SPME

SPME approximates Ewald structure factors using smooth cardinal B-splines. Treat it as a specific interpolation-and-force construction rather than a synonym for every PME implementation.

## Problem and representative equations

Let uᵢ be particle coordinates in mesh units and Mₚ a cardinal B-spline of order p, not degree p. The product below is the local tensor assignment in three dimensions. Fourier structure factors require a correction for the spline response.

$$
Q_{m_xm_ym_z}=\sum_iq_i\prod_{d\in\{x,y,z\}}M_p(u_{id}-m_d),\qquad \deg M_p=p-1.
$$

## Algorithm

Spread charge over p neighboring mesh points in each direction, evaluate a corrected reciprocal mesh energy by FFT, and obtain forces using derivatives of the assignment in analytical differentiation. Record the spline order and mesh together with whether differentiation is analytical or in Fourier space.

## Conditions and pitfalls

Smooth assignment alone does not guarantee both energy consistency and exact net-force cancellation. Ewald neutrality, boundary and self-term conventions still apply. Comparisons with original PME should control error tolerance and differentiation rules, not merely the number of mesh points.

The companion also uses analytical energy gradients with B-spline orders 4/6. Discrete energy–force consistency, common-translation mesh effects and net force are separate observables. Finite-mesh aliasing generally permits nonzero net force; exact momentum conservation is not claimed.

## What to check

Measure force errors against the same converged Ewald reference and check energy finite differences. Report common-translation mesh effects and total force separately. Ensure real-space truncation is not hiding the reciprocal-space convergence trend.

The design compares 16³/24³/40³ meshes and several common translations against matching direct-Ewald and independent theta references. It separates partition of unity/charge, energy differences, RMS/maximum force errors and real-space truncation; it supplies no evidence for long MD or original PME.

## Fixed-input examples and diagnostic controls

Distinguish the scope established by acceptance checks from a general mathematical guarantee; preserve historical inputs, measurements and criteria.

### Mesh/order convergence of B-spline smooth PME

Fixed-target computation

A small smooth-PME example assigns charge with B-splines and evaluates the Ewald reciprocal contribution by FFT.

Finite-mesh aliasing permits nonzero net force for this energy-gradient variant; that diagnostic is reported. No exact momentum conservation, long MD, original PME, optimized P³M or slab validation is claimed.

[Input, results and acceptance](/numerical-methods-atlas/validation/spme/?lang=en) · [Method and sources](/numerical-methods-atlas/en/read/validation-particles/#spme) · [Code run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/run.py) · [Code electrostatics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/electrostatics.py) · [Code fmm.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/fmm.py) · [Code transport.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/transport.py) · [Tests test_particles.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/test_particles.py) · [ZIP](/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip) · [Results](/code/validated-examples/2026-11-22/particles/results/result.json) · [Rerun receipt](/code/validated-examples/2026-11-22/particles/verification.json)

### SPME: mesh, interpolation order, mesh phase and conservation

Fixed-target computation

Compare B-spline SPME with the same independent theta reference; measure mesh/order/phase effects, charge partition, energy gradients and net force.

Finite-mesh aliasing generally gives nonzero net force for this energy-gradient variant. No exact momentum conservation, arbitrary-configuration error bound, long MD, original PME or every SPME variant is certified.

[Input, results and acceptance](/numerical-methods-atlas/validation/spme-convergence/?lang=en) · [Method and sources](/numerical-methods-atlas/en/read/validation-particle-transport/#spme-convergence) · [Code run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/run.py) · [Code longrange_experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/longrange_experiments.py) · [Code electrostatics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/electrostatics.py) · [Code fmm.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/fmm.py) · [Code kinetic_experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/kinetic_experiments.py) · [Code kinetics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/kinetics.py) · [Tests test_kinetics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/test_kinetics.py) · [Tests test_longrange.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/test_longrange.py) · [Tests test_runner.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/test_runner.py) · [ZIP](/code/validated-examples/2026-11-22/particle-transport/atlas-particle-transport-2026-11-22.zip) · [Results](/code/validated-examples/2026-11-22/particle-transport/results/result.json) · [Rerun receipt](/code/validated-examples/2026-11-22/particle-transport/verification.json)

## Publication scope

The historical reading, equations, sources and release are preserved; a separate companion release supplies bounded checks for fixed conditions. This does not mean every general verification suggestion above has been executed. Consult each release’s dedicated page and saved record for inputs, references, checks and limits.

## Sources

- Essmann, Ulrich and Perera, Lalith and Berkowitz, Max L. and Darden, Tom and Lee, Hsing and Pedersen, Lee G. (1995). A smooth particle mesh Ewald method. https://doi.org/10.1063/1.470117
- Darden, Tom and York, Darrin and Pedersen, Lee (1993). Particle mesh Ewald: An N log(N) method for Ewald sums in large systems. https://doi.org/10.1063/1.464397
