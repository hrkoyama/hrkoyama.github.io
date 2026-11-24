# Krylov eigenvalue solvers

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/eigensolvers/

Resources explicitly registered to the methods, problems and executions of this chapter.

## Methods

- [Krylov eigenvalue solvers](<https://hrkoyama.github.io/numerical-methods-atlas/methods/eigensolvers/?lang=en>)

## Equations

No chapter-specific association is registered. Atlas-wide index: [Equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en)

## Problem figures

No chapter-specific association is registered. Atlas-wide index: [Test problems by name and figure](https://hrkoyama.github.io/numerical-methods-atlas/gallery/?lang=en)

## Exact / reference solutions

No chapter-specific association is registered. Atlas-wide index: [Exact and reference solutions](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en)

## Code and validation

- [Lanczos and Arnoldi: convergence of Ritz values and eigenpair residuals](<https://hrkoyama.github.io/numerical-methods-atlas/validation/krylov-eigenvalues/?lang=en>)
  availability: run

  Original Lanczos and Arnoldi on symmetric/nonsymmetric 32×32 and 48×48 matrices measure convergence of the largest-real-part eigenpair over Krylov dimensions 4, 8 and 16, against independent full-matrix LAPACK references.
- [Krylov eigenvalues: cluster subspaces and nonnormal sensitivity](<https://hrkoyama.github.io/numerical-methods-atlas/validation/krylov-eigen-conditioning/?lang=en>)
  availability: run

  Measure Lanczos and Arnoldi with dimensions4/8/16/32 on 48-dimensional clustered symmetric and strongly nonnormal triangular matrices. Distinguish residual, forward error, eigenvalue condition number and invariant subspace.
- [Explicitly restarted Krylov and interior eigenvalues](<https://hrkoyama.github.io/numerical-methods-atlas/validation/restarted-shift-invert/?lang=en>)
  availability: run

  Explicit restarting and shift-invert are compared using original eigenproblem residuals and counted operator actions.
- [Consistent-mass FEM string eigenpairs](<https://hrkoyama.github.io/numerical-methods-atlas/validation/fem-mass-eigen/?lang=en>)
  availability: run

  Consistent-mass P1 string eigenpairs compare an M-inner-product Krylov method and actual SciPy LOBPCG with an independent discrete spectrum.
- [Krylov eigenvalue solvers — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/eigensolvers/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
