# Gravity kernels: isolated FFTs and a periodic slab

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/gravity-boundaries/

Resources explicitly registered to the methods, problems and executions of this chapter.

## Methods

- [Isolated doubled-grid FFT convolution](<https://hrkoyama.github.io/numerical-methods-atlas/methods/hockney/?lang=en>)
- [Horizontal-periodic slab Green-function FFT](<https://hrkoyama.github.io/numerical-methods-atlas/methods/slab/?lang=en>)
- [Isolated doubled-grid FFT convolution](<https://hrkoyama.github.io/numerical-methods-atlas/methods/hockney/?lang=en>)

  Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.
- [Horizontal-periodic slab Green-function FFT](<https://hrkoyama.github.io/numerical-methods-atlas/methods/slab/?lang=en>)

  Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.
- [Horizontal-periodic slab Green-function FFT](<https://hrkoyama.github.io/numerical-methods-atlas/methods/slab/?lang=en>)

  Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

## Equations

- [Poisson / Laplace equations](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#poisson-laplace-en>)

  Elliptic boundary-value problems: check sign conventions, iterative solvers, sparse matrices and boundaries. A density-field convolution for the gravitational Poisson equation with isolated boundaries, distinct from softened particle-pair forces or fully periodic Poisson examples. This visual compares zero-padded FFT with nonperiodic direct convolution using the same discrete kernel.
- [Poisson / Laplace equations](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#poisson-laplace-en>)

  Elliptic boundary-value problems: check sign conventions, iterative solvers, sparse matrices and boundaries. A gravitational Poisson problem periodic horizontally and isolated vertically, using the zero horizontal mode of a uniform slab. The right-hand side of the representative Poisson equation below is 4πGρ here; fully periodic boundaries and softened particle systems are different cases.
- [Poisson / Laplace equations](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#poisson-laplace-en>)

  Elliptic boundary-value problems: check sign conventions, iterative solvers, sparse matrices and boundaries. A gravitational Poisson problem periodic horizontally and isolated vertically, combining nonzero and zero horizontal modes of a sheet density. The Poisson right-hand side is 4πGρ; this differs from fully periodic fields or softened particle-pair forces.

## Problem figures

- [Isolated FFT versus direct nonperiodic convolution](<https://hrkoyama.github.io/numerical-methods-atlas/problems/isolated-convolution/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/numerical-methods-atlas/assets/gravity-boundaries.png
- [Uniform plane-slab gravity](<https://hrkoyama.github.io/numerical-methods-atlas/problems/uniform-slab/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/numerical-methods-atlas/assets/gravity-boundaries.png
- [Sinusoidal sheet gravity](<https://hrkoyama.github.io/numerical-methods-atlas/problems/sinusoidal-sheet/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/numerical-methods-atlas/assets/gravity-boundaries.png

## Exact / reference solutions

- [Isolated FFT versus direct nonperiodic convolution — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/isolated-convolution/?lang=en#references-en>)

  Check zero-padded FFT against nonperiodic direct convolution using the same discrete kernel, cell volumes and self term. This is separate from continuum-kernel discretization error.
- [Uniform plane-slab gravity — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/uniform-slab/?lang=en#references-en>)

  Compare with φ=2πz² after aligning the additive gauge; check acceleration -4πz and the zero horizontal mode.
- [Sinusoidal sheet gravity — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/sinusoidal-sheet/?lang=en#references-en>)

  Check the horizontally periodic, vertically isolated field using the analytic exponential kernel for sinusoidal sheet density plus the absolute-value kernel for its uniform part.

## Code and validation

- [Isolated doubled-grid FFT convolution — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/hockney/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [Horizontal-periodic slab Green-function FFT — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/slab/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [Isolated FFT versus direct nonperiodic convolution — code and validation status](<https://hrkoyama.github.io/numerical-methods-atlas/problems/isolated-convolution/?lang=en#code-en>)
  availability: source

  Inspect the corresponding public checks and distribution conditions.
