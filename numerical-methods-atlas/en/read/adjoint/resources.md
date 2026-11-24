# Implicit differentiation and adjoints: Bratu parameter sensitivity

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/adjoint/

Resources explicitly registered to the methods, problems and executions of this chapter.

## Methods

- [Implicit differentiation and adjoint methods](<https://hrkoyama.github.io/numerical-methods-atlas/methods/adjoint/?lang=en>)
- [Automatic differentiation](<https://hrkoyama.github.io/numerical-methods-atlas/methods/automatic-differentiation/?lang=en>)
- [Armijo-damped Newton](<https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=en>)

## Equations

No chapter-specific association is registered. Atlas-wide index: [Equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en)

## Problem figures

No chapter-specific association is registered. Atlas-wide index: [Test problems by name and figure](https://hrkoyama.github.io/numerical-methods-atlas/gallery/?lang=en)

## Exact / reference solutions

No chapter-specific association is registered. Atlas-wide index: [Exact and reference solutions](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en)

## Code and validation

- [Discrete diffusion adjoint and checkpoint replay](<https://hrkoyama.github.io/numerical-methods-atlas/validation/diffusion-discrete-adjoint/?lang=en>)
  availability: run

  Reverse the actual backward-Euler map and compare tangent derivatives, independent high-precision modes and block replay.
- [Bratu sensitivity near the discrete fold](<https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-sensitivity/?lang=en>)
  availability: run

  At six fixed points approaching the discrete Bratu fold, separate state error from linear-solve tolerance and compare against independent shooting gradients.
- [Matrix-free VJP for distributed Bratu coefficients](<https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-distributed-vjp/?lang=en>)
  availability: run

  Represent8/16/32 spatial controls with two local hat weights per node; compare objective-wise adjoint VJPs with a separate full-sensitivity reference.
- [Implicit differentiation and adjoint methods — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/adjoint/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
