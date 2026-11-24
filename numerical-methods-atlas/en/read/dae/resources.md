# Differential-algebraic equations / DAE

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/dae/

Resources explicitly registered to the methods, problems and executions of this chapter.

## Methods

- [Differential-algebraic equations / DAE](<https://hrkoyama.github.io/numerical-methods-atlas/methods/dae/?lang=en>)

## Equations

- [Semi-explicit index-one DAE](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#index-one-dae-en>)

  Small fixed examples expose consistent initialization and separate differential/algebraic residuals; this is not a general-purpose DAE solver.
- [Constrained planar pendulum](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#constrained-pendulum-en>)

  Distinguish the original position-constrained DAE, an underlying ODE based on differentiated constraints, and the SHAKE/RATTLE discrete maps.

## Problem figures

No chapter-specific association is registered. Atlas-wide index: [Test problems by name and figure](https://hrkoyama.github.io/numerical-methods-atlas/gallery/?lang=en)

## Exact / reference solutions

No chapter-specific association is registered. Atlas-wide index: [Exact and reference solutions](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en)

## Code and validation

- [Robertson conservation DAE and stored official IDA values](<https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-conservation-dae/?lang=en>)
  availability: run

  Compare the Robertson conservation DAE and full ODE on the same fixed time grids, with a separate check of stored official IDA values. The first retained run missed four original time-accuracy and refinement goals.
- [Consistent initialization and discrete residuals for an index-one DAE](<https://hrkoyama.github.io/numerical-methods-atlas/validation/index1-dae-consistent-initialization/?lang=en>)
  availability: run

  Separate initialization, backward-Euler error and residuals on a known positive index-one DAE branch.
- [Index reduction, constraint drift and explicit stabilization for a pendulum](<https://hrkoyama.github.io/numerical-methods-atlas/validation/high-index-pendulum/?lang=en>)
  availability: run

  Derive an explicit ODE from an index-three position constraint and compare drift and stabilization for consistent and inconsistent starts.
- [Differential-algebraic equations / DAE — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/dae/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
