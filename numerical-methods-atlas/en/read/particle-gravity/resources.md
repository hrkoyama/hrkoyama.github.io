# Particle gravity: PM, P³M, Tree, multipoles, and multigrid

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/particle-gravity/

Resources explicitly registered to the methods, problems and executions of this chapter.

## Methods

- [Cloud-in-cell assignment and interpolation](<https://hrkoyama.github.io/numerical-methods-atlas/methods/cic/?lang=en>)
- [FFT particle–mesh forces](<https://hrkoyama.github.io/numerical-methods-atlas/methods/pm/?lang=en>)
- [Barnes–Hut octree](<https://hrkoyama.github.io/numerical-methods-atlas/methods/barnes-hut/?lang=en>)
- [Monopole and second-moment expansion](<https://hrkoyama.github.io/numerical-methods-atlas/methods/multipole/?lang=en>)
- [P³M short-range correction](<https://hrkoyama.github.io/numerical-methods-atlas/methods/p3m/?lang=en>)
- [TreePM force splitting](<https://hrkoyama.github.io/numerical-methods-atlas/methods/treepm/?lang=en>)
- [Fast multipole translations](<https://hrkoyama.github.io/numerical-methods-atlas/methods/fmm/?lang=en>)
- [Fourier differentiation and evolution](<https://hrkoyama.github.io/numerical-methods-atlas/methods/fourier/?lang=en>)

  Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.
- [FFT particle–mesh forces](<https://hrkoyama.github.io/numerical-methods-atlas/methods/pm/?lang=en>)

  Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.
- [Barnes–Hut octree](<https://hrkoyama.github.io/numerical-methods-atlas/methods/barnes-hut/?lang=en>)

  Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions.
- [Cloud-in-cell assignment and interpolation](<https://hrkoyama.github.io/numerical-methods-atlas/methods/cic/?lang=en>)

  Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions.
- [FFT particle–mesh forces](<https://hrkoyama.github.io/numerical-methods-atlas/methods/pm/?lang=en>)

  Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions.

## Equations

- [Poisson / Laplace equations](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#poisson-laplace-en>)

  Elliptic boundary-value problems: check sign conventions, iterative solvers, sparse matrices and boundaries. Representative equations related to this problem. See the image/problem conditions and each execution example for initial conditions, boundary conditions and parameters.
- [Gravitational particle model](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#particle-gravity-en>)

  Isolated Plummer-softened forces and periodic mean-subtracted Poisson are distinct boundary problems. Public examples check static forces and kernels, not coupled self-gravitating flow evolution. Representative equations related to this problem. See the image/problem conditions and each execution example for initial conditions, boundary conditions and parameters.
- [Gravitational particle model](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#particle-gravity-en>)

  Isolated Plummer-softened forces and periodic mean-subtracted Poisson are distinct boundary problems. Public examples check static forces and kernels, not coupled self-gravitating flow evolution. Representative equations related to this problem. See the image/problem conditions and each execution example for initial conditions, boundary conditions and parameters.
- [Gravitational particle model](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#particle-gravity-en>)

  Isolated Plummer-softened forces and periodic mean-subtracted Poisson are distinct boundary problems. Public examples check static forces and kernels, not coupled self-gravitating flow evolution. Representative equations related to this problem. See the image/problem conditions and each execution example for initial conditions, boundary conditions and parameters.
- [Poisson / Laplace equations](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#poisson-laplace-en>)

  Elliptic boundary-value problems: check sign conventions, iterative solvers, sparse matrices and boundaries. Representative equations related to this problem. See the image/problem conditions and each execution example for initial conditions, boundary conditions and parameters.
- [Gravitational particle model](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#particle-gravity-en>)

  Isolated Plummer-softened forces and periodic mean-subtracted Poisson are distinct boundary problems. Public examples check static forces and kernels, not coupled self-gravitating flow evolution.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#execution-periodic-particles-en>)

  3D periodic L=1 box and 24³ grid, matched CIC and continuum-k² Fourier symbol. Not isolated summation, Ewald, PME or SPME. The analytic sinusoidal mesh check does not certify all close-pair particle forces.
- [Poisson / Laplace equations](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#poisson-laplace-en>)

  Elliptic boundary-value problems: check sign conventions, iterative solvers, sparse matrices and boundaries.

## Problem figures

- [3D periodic Poisson / Fourier manufactured solution](<https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-3d-periodic/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/numerical-methods-atlas/assets/field-poisson-3d.png
- [Isolated softened particle gravity: tree versus direct sum](<https://hrkoyama.github.io/numerical-methods-atlas/problems/isolated-particles/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/isolated-particles.png
- [Periodic PM particle mass and internal force](<https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-particles/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/numerical-methods-atlas/assets/particle-gravity.png

## Exact / reference solutions

- [3D periodic Poisson / Fourier manufactured solution — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-3d-periodic/?lang=en#references-en>)

  Compare against a single manufactured Fourier mode for periodic Poisson with mean density removed. This validates the mesh field rather than a periodic particle direct sum.
- [Isolated softened particle gravity: tree versus direct sum — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/isolated-particles/?lang=en#references-en>)

  Direct pair summation with identical particles and Plummer softening is the numerical standard. Compare force errors by tree opening angle and multipole order.
- [Periodic PM particle mass and internal force — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-particles/?lang=en#references-en>)

  Check mass conservation, mass-weighted internal force and a manufactured Fourier solution of mesh Poisson. This does not establish force accuracy against a general periodic particle direct sum.
- [Periodic PM particles: mass, internal force and mesh field — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/periodic-particles/?lang=en#periodic-particles-en-validation>)

  CSV stores each particle's coordinates, mass, acceleration and force. Independent sinusoidal-field diagnostics are JSON metrics. No mesh refinement is misrepresented as analytic particle-force error.

## Code and validation

- [Periodic PM particles: mass, internal force and mesh field](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/periodic-particles/?lang=en>)
  availability: run

  Periodic CIC–FFT–CIC calculation for 19 particles stored explicitly in input JSON. Check mass, net internal force, single-particle self-force and integer-box translation; separately compare a sinusoidal density with analytic periodic Poisson fields.
- [Barnes–Hut: 192 particles against direct summation](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/barnes-hut/?lang=en>)
  availability: run

  Static isolated softened-gravity force comparison, not orbital integration, periodic gravity or a timing benchmark.
- [2D logarithmic FMM with M2M, M2L and L2L](<https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm/?lang=en>)
  availability: run

  Evaluate a free-space log potential with uniform-quadtree multipole and local expansions and compare with direct sums.
- [FMM: direct and analytic references, order and tree depth](<https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm-convergence/?lang=en>)
  availability: run

  Compare a 96-particle 2D logarithmic kernel with independent all-pairs sums; measure order/depth, rotation/translation and approximate net-force errors.
- [Cloud-in-cell assignment and interpolation — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/cic/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [FFT particle–mesh forces — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/pm/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [Barnes–Hut octree — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/barnes-hut/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [Monopole and second-moment expansion — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/multipole/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [Fast multipole translations — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/fmm/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [Periodic PM particle mass and internal force — code and validation status](<https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-particles/?lang=en#code-en>)
  availability: source

  Inspect the corresponding public checks and distribution conditions.
