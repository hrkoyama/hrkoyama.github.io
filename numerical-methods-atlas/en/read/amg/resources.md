# Algebraic multigrid / AMG

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/amg/

Resources explicitly registered to the methods, problems and executions of this chapter.

## Methods

- [Algebraic multigrid / AMG](<https://hrkoyama.github.io/numerical-methods-atlas/methods/amg/?lang=en>)

## Equations

No chapter-specific association is registered. Atlas-wide index: [Equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en)

## Problem figures

No chapter-specific association is registered. Atlas-wide index: [Test problems by name and figure](https://hrkoyama.github.io/numerical-methods-atlas/gallery/?lang=en)

## Exact / reference solutions

No chapter-specific association is registered. Atlas-wide index: [Exact and reference solutions](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en)

## Code and validation

- [Matrix-based AMG: distinguish residual and solution error](<https://hrkoyama.github.io/numerical-methods-atlas/validation/sa-amg/?lang=en>)
  availability: run

  Build a smoothed-aggregation hierarchy from an SPD matrix alone and run V-cycles. Problems with 7², 15² and 31² unknowns distinguish independent sparse direct solutions, analytic discrete sine modes and second-order convergence to the continuum solution.
- [Checkerboard diffusion: shared flux, MG and AMG](<https://hrkoyama.github.io/numerical-methods-atlas/validation/checkerboard-diffusion/?lang=en>)
  availability: run

  Compare discontinuous-coefficient FV with independent P1 reference fields, separating linear-system residual/forward errors from continuum error.
- [Rotated diffusion: full-tensor Q1, MG and AMG](<https://hrkoyama.github.io/numerical-methods-atlas/validation/rotated-anisotropic-diffusion/?lang=en>)
  availability: run

  Retain nonzero Kxy in the Q1 weak form and compare analytic refinement with MG/AMG convergence for the same matrix.
- [Algebraic multigrid / AMG — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/amg/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
