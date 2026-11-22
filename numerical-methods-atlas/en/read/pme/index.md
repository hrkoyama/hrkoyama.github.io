# Particle mesh Ewald / PME

PME transfers the reciprocal Ewald calculation to a mesh and uses FFTs. Distinguish the original Lagrange-interpolation PME from the later B-spline construction of SPME.

## Problem and representative equations

For a neutral triply periodic Coulomb system, Qₘ is charge assigned to mesh point xₘ using weights Wₘ. The reciprocal operator Ĝₕ includes Ewald screening, mesh conventions and interpolation corrections. This schematic describes only the reciprocal contribution; real-space and self terms remain necessary.

$$
Q_{\mathbf m}=\sum_iq_iW_{\mathbf m}(\mathbf r_i),\qquad\phi_h=\mathcal F_h^{-1}\!\left[\widehat G_h\,\mathcal F_h Q\right].
$$

## Algorithm

Assign charges with local Lagrange polynomials, transform the mesh, apply the reciprocal convolution and transform back. Specify the differentiation and particle-gather rules together. A mesh-interpolated field and the derivative of the discrete energy need not give identical forces.

## Conditions and pitfalls

Separate mesh resolution, interpolation order, Ewald cutoffs and force differentiation in error studies. State FFT normalization, k=0 treatment and units. The usual O(N log N) description assumes an appropriate mesh-growth regime and is not an accuracy guarantee.

The linked implementation adopts smooth PME with B-spline analytical energy gradients. It does not implement or validate the original 1993 Lagrange-interpolation PME; the original PME equations, sources and applicability remain distinct from this implemented variant.

## What to check

Use a converged direct Ewald calculation for the identical neutral cell. Vary mesh size, interpolation order and screening; measure RMS/maximum energy and force errors and sensitivity to common translations. A gravity-PM test does not validate PME.

The companion varies mesh size, B-spline order and common translation for the same neutral periodic charges, comparing against converged direct Ewald and a separately implemented theta integral. The direct-Ewald comparison shares real-space/self terms, so agreement there alone is not independent validation of the entire energy.

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

- Darden, Tom and York, Darrin and Pedersen, Lee (1993). Particle mesh Ewald: An N log(N) method for Ewald sums in large systems. https://doi.org/10.1063/1.464397
- Ewald, P. P. (1921). Die Berechnung optischer und elektrostatischer Gitterpotentiale. https://doi.org/10.1002/andp.19213690304
