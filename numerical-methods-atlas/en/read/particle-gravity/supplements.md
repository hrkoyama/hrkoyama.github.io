# A separate model: 2D logarithmic FMM

The gravity, PM and tree article and its boundary conventions above are preserved. The following FMM is a separate educational model: a negative-logarithmic kernel in 2D free space evaluated with a uniform quadtree. Its accuracy does not transfer to 3D Coulomb or softened-gravity 1/r kernels.

The historical release is retained. The companion separates expansion order from tree depth and compares Cartesian direct sums, analytic configurations and conservation diagnostics. No monotonic error with depth, empirical complexity scaling, adaptive-tree or periodic-FMM validation is claimed.

## 2D logarithmic FMM with M2M, M2L and L2L

Evaluate a free-space log potential with uniform-quadtree multipole and local expansions and compare with direct sums.

No 3D 1/r kernel, adaptive tree, periodic FMM, singular quadrature or empirical complexity/scaling study. Evidence applies to this 2D free-space educational implementation.

- [Inputs, results and checks](/numerical-methods-atlas/validation/fmm/?lang=en)
- [Reading, equations and primary sources](/numerical-methods-atlas/en/read/validation-particles/#fmm)
- [Code: run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/run.py)
- [Code: electrostatics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/electrostatics.py)
- [Code: fmm.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/fmm.py)
- [Code: transport.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/transport.py)
- [Tests: test_particles.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/test_particles.py)
- [Release ZIP](/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip)
- [Saved results](/code/validated-examples/2026-11-22/particles/results/result.json)
- [Independent-extraction receipt](/code/validated-examples/2026-11-22/particles/verification.json)

## FMM: direct and analytic references, order and tree depth

Compare a 96-particle 2D logarithmic kernel with independent all-pairs sums; measure order/depth, rotation/translation and approximate net-force errors.

Interaction repartition changes with depth, so fixed-order depth refinement is not assumed monotone. Target-wise expansions need not preserve exact action/reaction. No 3D, adaptive/periodic FMM or complexity-scaling claim.

- [Inputs, results and checks](/numerical-methods-atlas/validation/fmm-convergence/?lang=en)
- [Reading, equations and primary sources](/numerical-methods-atlas/en/read/validation-particle-transport/#fmm-convergence)
- [Code: run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/run.py)
- [Code: longrange_experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/longrange_experiments.py)
- [Code: fmm.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/fmm.py)
- [Code: electrostatics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/electrostatics.py)
- [Code: kinetic_experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/kinetic_experiments.py)
- [Code: kinetics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/kinetics.py)
- [Tests: test_kinetics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/test_kinetics.py)
- [Tests: test_longrange.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/test_longrange.py)
- [Tests: test_runner.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/test_runner.py)
- [Release ZIP](/code/validated-examples/2026-11-22/particle-transport/atlas-particle-transport-2026-11-22.zip)
- [Saved results](/code/validated-examples/2026-11-22/particle-transport/results/result.json)
- [Independent-extraction receipt](/code/validated-examples/2026-11-22/particle-transport/verification.json)
