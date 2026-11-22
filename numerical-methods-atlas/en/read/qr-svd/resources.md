# QR, SVD and least squares

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/qr-svd/

Resources explicitly registered to the methods, problems and executions of this chapter.

## Methods

- [QR, SVD and least squares](<https://hrkoyama.github.io/numerical-methods-atlas/methods/qr-svd/?lang=en>)

## Equations

No chapter-specific association is registered. Atlas-wide index: [Equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en)

## Problem figures

No chapter-specific association is registered. Atlas-wide index: [Test problems by name and figure](https://hrkoyama.github.io/numerical-methods-atlas/gallery/?lang=en)

## Exact / reference solutions

No chapter-specific association is registered. Atlas-wide index: [Exact and reference solutions](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en)

## Code and validation

- [Householder QR and one-sided Jacobi SVD: orthogonality, rank and least squares](<https://hrkoyama.github.io/numerical-methods-atlas/validation/qr-svd-factorization/?lang=en>)
  availability: run

  Original Householder QR and one-sided Jacobi SVD for real tall matrices are checked on ordinary, 10⁶-column-scaled and rank-deficient inputs, against separate LAPACK singular values and minimum-norm least-squares solutions.
- [QR/SVD: prescribed spectra, perturbation gain and numerical rank](<https://hrkoyama.github.io/numerical-methods-atlas/validation/qr-svd-conditioning/?lang=en>)
  availability: run

  Vary condition number from 1 to 2³⁶ for exactly representable 16×4 dyadic matrices, separating reconstruction from forward solution error. Compare LAPACK and separately executed 80/120-digit references for the actual binary64 inputs.
- [QR, SVD and least squares — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/qr-svd/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
