# Ewald summation

Ewald summation evaluates periodic Coulomb interactions through complementary real- and reciprocal-space sums. It defines a different boundary-value problem from simply truncating 1/r at a finite radius.

## Problem and representative equations

Consider point charges qᵢ in a neutral, triply periodic cell. Set rᵢⱼₙ=rᵢ−rⱼ+n, cell volume V, splitting parameter α>0 and reciprocal vector k. S(k) is the charge structure factor. The energy below uses unit Coulomb prefactor, omits k=0 and assumes a conducting macroscopic boundary. The prime excludes only i=j,n=0.

$$
\begin{aligned}S(\mathbf k)&=\sum_jq_j e^{i\mathbf k\cdot\mathbf r_j},\\E&=\frac12\sum_{i,j,\mathbf n}^{\prime}q_iq_j\frac{\operatorname{erfc}(\alpha r_{ij\mathbf n})}{r_{ij\mathbf n}}+\frac{2\pi}{V}\sum_{\mathbf k\ne0}\frac{e^{-k^2/(4\alpha^2)}}{k^2}|S(\mathbf k)|^2-\frac{\alpha}{\sqrt\pi}\sum_iq_i^2.\end{aligned}
$$

## Algorithm

Accumulate screened real-space pairs and Gaussian-damped reciprocal modes, then subtract the self energy. Restore the same Coulomb prefactor to every term in dimensional units. Changing α redistributes work between sums but cannot change their converged total. Derive forces from the same energy convention.

## Conditions and pitfalls

A net-charged cell requires an additional convention such as a compensating background. Specify potential gauge, surface term, periodic self images and molecular exclusions separately. A periodic gravitational Poisson solve changes the kernel/sign and mean-density treatment; it is not the same calculation.

The companion release keeps an asymmetric neutral eight-charge cubic cell, triply periodic with tin-foil boundaries. It separates the direct-Ewald splitting parameter, real-image and reciprocal-cube cutoffs, using a separately implemented heat-kernel theta integral as a reference. It does not extend to charged backgrounds or slabs.

## What to check

For a small neutral configuration, increase both cutoffs independently and test α independence. Compare forces with finite differences of energy, and check translation invariance and net force. Agreement between two unconverged sums is not independent validation.

Historical and companion inputs, criteria and results are retained separately. The companion checks energy and every particle force, refinement of the reference integral itself, translations, particle ordering, net force and energy differences individually; a deliberately truncated control is distinct from a converged reference.

## Fixed-input examples and diagnostic controls

Distinguish the scope established by acceptance checks from a general mathematical guarantee; preserve historical inputs, measurements and criteria.

### Neutral-cell Ewald sums and an independent theta integral

Fixed-target computation

Implement real-space, reciprocal-space and self Ewald terms for neutral 3D periodic Coulomb charges; vary splitting and cutoffs.

No charged-cell/background correction, triclinic cell, finite-dielectric surface term, slab correction, stress or material-specific force field.

[Input, results and acceptance](/numerical-methods-atlas/validation/ewald/?lang=en) · [Method and sources](/numerical-methods-atlas/en/read/validation-particles/#ewald) · [Code run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/run.py) · [Code electrostatics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/electrostatics.py) · [Code fmm.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/fmm.py) · [Code transport.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/transport.py) · [Tests test_particles.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/test_particles.py) · [ZIP](/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip) · [Results](/code/validated-examples/2026-11-22/particles/results/result.json) · [Rerun receipt](/code/validated-examples/2026-11-22/particles/verification.json)

### Ewald: asymmetric-cell energies and forces versus independent theta integration

Fixed-target computation

Compare a neutral eight-charge cell energy and all 24 force components with a separately coded Gaussian/theta integral. Separate splitting and real/reciprocal truncation from invariants and conservation.

One fixed neutral cubic cell. Upper-limit sensitivity is not a rigorous tail bound for arbitrary configurations. The theta reference is an independently formulated original implementation, not an external package or published numerical table. Charged/triclinic/slab cells, stress and long MD are outside scope.

[Input, results and acceptance](/numerical-methods-atlas/validation/ewald-convergence/?lang=en) · [Method and sources](/numerical-methods-atlas/en/read/validation-particle-transport/#ewald-convergence) · [Code run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/run.py) · [Code longrange_experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/longrange_experiments.py) · [Code electrostatics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/electrostatics.py) · [Code fmm.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/fmm.py) · [Code kinetic_experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/kinetic_experiments.py) · [Code kinetics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/kinetics.py) · [Tests test_kinetics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/test_kinetics.py) · [Tests test_longrange.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/test_longrange.py) · [Tests test_runner.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/test_runner.py) · [ZIP](/code/validated-examples/2026-11-22/particle-transport/atlas-particle-transport-2026-11-22.zip) · [Results](/code/validated-examples/2026-11-22/particle-transport/results/result.json) · [Rerun receipt](/code/validated-examples/2026-11-22/particle-transport/verification.json)

## Publication scope

The historical reading, equations, sources and release are preserved; a separate companion release supplies bounded checks for fixed conditions. This does not mean every general verification suggestion above has been executed. Consult each release’s dedicated page and saved record for inputs, references, checks and limits.

## Sources

- Ewald, P. P. (1921). Die Berechnung optischer und elektrostatischer Gitterpotentiale. https://doi.org/10.1002/andp.19213690304
- Hockney, R. W. and Eastwood, J. W. (1981). Computer Simulation Using Particles. https://doi.org/10.1201/9780367806934
