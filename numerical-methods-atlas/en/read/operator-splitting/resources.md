# Operator splitting: Lie–Trotter and Strang

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/operator-splitting/

Resources explicitly registered to the methods, problems and executions of this chapter.

## Methods

- [Lie–Trotter splitting](<https://hrkoyama.github.io/numerical-methods-atlas/methods/lie-trotter/?lang=en>)
- [Strang splitting](<https://hrkoyama.github.io/numerical-methods-atlas/methods/strang-splitting/?lang=en>)
- [Implicit midpoint](<https://hrkoyama.github.io/numerical-methods-atlas/methods/implicit-midpoint/?lang=en>)

## Equations

- [Linear reaction-diffusion with inhomogeneous boundaries](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#inhomogeneous-reaction-diffusion-en>)

  Separate temporal errors relative to the same nonperiodic finite-difference system from spatial errors relative to the continuous exact family.

## Problem figures

No chapter-specific association is registered. Atlas-wide index: [Test problems by name and figure](https://hrkoyama.github.io/numerical-methods-atlas/gallery/?lang=en)

## Exact / reference solutions

No chapter-specific association is registered. Atlas-wide index: [Exact and reference solutions](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en)

## Code and validation

- [Lie–Trotter versus Strang on the same nonlinear reaction–diffusion input](<https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-splitting/?lang=en>)
  availability: run

  Advance a 32-point Schnakenberg reaction–diffusion problem to T=1 with matched inputs and subsolvers. Four step sizes check first-/second-order temporal convergence, reference sensitivity, reaction balance and failure on nonconvergence in a lightweight comparison.
- [Strang splitting: Dirichlet boundary order reduction and correction](<https://hrkoyama.github.io/numerical-methods-atlas/validation/strang-boundary-order-reduction/?lang=en>)
  availability: run

  Evolve actual one-dimensional nonperiodic fields and compare unmodified and boundary-corrected Strang splitting against the same spatial discretization.
- [Coupled frequencies and finite-window resonance](<https://hrkoyama.github.io/numerical-methods-atlas/validation/multifrequency-resonance/?lang=en>)
  availability: run

  A genuinely coupled two-degree-of-freedom system uses twelve 64-step probes and six accuracy trajectories to separate normal modes, coordinate exchange, discrete maps and roundoff.
- [Schnakenberg:2D boundaries and initial modes](<https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-2d-boundary-modes/?lang=en>)
  availability: run

  Compare two Neumann perturbations and a Dirichlet perturbation against nonlinear Galerkin references.
- [Lie–Trotter splitting — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/lie-trotter/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [Strang splitting — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/strang-splitting/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
