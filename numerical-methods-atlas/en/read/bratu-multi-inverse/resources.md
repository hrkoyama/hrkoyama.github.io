# Multi-parameter Bratu inversion: regularization and identifiability

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/bratu-multi-inverse/

Resources explicitly registered to the methods, problems and executions of this chapter.

## Methods

- [Gradient and quasi-Newton optimization](<https://hrkoyama.github.io/numerical-methods-atlas/methods/optimization/?lang=en>)
- [Implicit differentiation and adjoint methods](<https://hrkoyama.github.io/numerical-methods-atlas/methods/adjoint/?lang=en>)
- [Automatic differentiation](<https://hrkoyama.github.io/numerical-methods-atlas/methods/automatic-differentiation/?lang=en>)
- [QR, SVD and least squares](<https://hrkoyama.github.io/numerical-methods-atlas/methods/qr-svd/?lang=en>)
- [Armijo-damped Newton](<https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=en>)

## Equations

No chapter-specific association is registered. Atlas-wide index: [Equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en)

## Problem figures

No chapter-specific association is registered. Atlas-wide index: [Test problems by name and figure](https://hrkoyama.github.io/numerical-methods-atlas/gallery/?lang=en)

## Exact / reference solutions

No chapter-specific association is registered. Atlas-wide index: [Exact and reference solutions](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en)

## Code and validation

- [Bratu comparisons of GN, LM and bounded least squares](<https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-gn-lm-bounds/?lang=en>)
  availability: run

  Seventeen fixed fits separate parameter scaling, weights, bounds and physical-coordinate stopping conditions.
- [BFGS and three-pair L-BFGS at known minima](<https://hrkoyama.github.io/numerical-methods-atlas/validation/bfgs-lbfgs-controls/?lang=en>)
  availability: run

  An eight-dimensional SPD quadratic and three Rosenbrock starts test curvature, strong Wolfe conditions and the current finite-memory action.
- [Noise, model discrepancy and finite gamma paths](<https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-noise-regularization/?lang=en>)
  availability: run

  Two independent noise vectors are reused across scales and data contexts. Forty-two fixed fits separate finite-list gamma selection from fixed-gamma local covariance.
- [Discrete diffusion adjoint and checkpoint replay](<https://hrkoyama.github.io/numerical-methods-atlas/validation/diffusion-discrete-adjoint/?lang=en>)
  availability: run

  Reverse the actual backward-Euler map and compare tangent derivatives, independent high-precision modes and block replay.
- [Bratu sensitivity near the discrete fold](<https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-sensitivity/?lang=en>)
  availability: run

  At six fixed points approaching the discrete Bratu fold, separate state error from linear-solve tolerance and compare against independent shooting gradients.
- [Matrix-free VJP for distributed Bratu coefficients](<https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-distributed-vjp/?lang=en>)
  availability: run

  Represent8/16/32 spatial controls with two local hat weights per node; compare objective-wise adjoint VJPs with a separate full-sensitivity reference.
- [Gradient and quasi-Newton optimization — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/optimization/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [Implicit differentiation and adjoint methods — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/adjoint/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
