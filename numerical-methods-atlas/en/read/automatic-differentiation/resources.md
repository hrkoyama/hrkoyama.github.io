# Automatic differentiation: derivatives for numerical solvers

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/automatic-differentiation/

Resources explicitly registered to the methods, problems and executions of this chapter.

## Methods

- [Automatic differentiation](<https://hrkoyama.github.io/numerical-methods-atlas/methods/automatic-differentiation/?lang=en>)

## Equations

No chapter-specific association is registered. Atlas-wide index: [Equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en)

## Problem figures

No chapter-specific association is registered. Atlas-wide index: [Test problems by name and figure](https://hrkoyama.github.io/numerical-methods-atlas/gallery/?lang=en)

## Exact / reference solutions

No chapter-specific association is registered. Atlas-wide index: [Exact and reference solutions](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en)

## Code and validation

- [Jacobian-free Newton–Krylov with analytic, central-FD and directional-AD products](<https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-matrix-free-jfnk/?lang=en>)
  availability: run

  Solve both Bratu branches with three Jv choices without assembling the nonlinear Jacobian; retain forcing, actual residuals and evaluation counts.
- [Original reverse-mode VJP and JVP/VJP duality](<https://hrkoyama.github.io/numerical-methods-atlas/validation/reverse-vjp-duality/?lang=en>)
  availability: run

  Check a genuine reverse tape, including repeated-index gather and broadcast, against independent Jacobians.
- [Hessian-vector products and fixed-state versus implicit derivatives](<https://hrkoyama.github.io/numerical-methods-atlas/validation/hessian-vector-products/?lang=en>)
  availability: run

  Check forward-over-reverse HVPs and second-order implicit rules against separate independent references.
- [Derivative scope at kinks, branches and stopping decisions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/kink-branch-derivatives/?lang=en>)
  availability: run

  Distinguish classical, one-sided directional and executed-trace derivatives at fixed kinks and stopping switches.
- [Automatic differentiation — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/automatic-differentiation/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
