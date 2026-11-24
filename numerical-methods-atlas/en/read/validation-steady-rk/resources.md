# Modal damping of steady multistage RK

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-steady-rk/

Resources explicitly registered to the methods, problems and executions of this chapter. A 16-component periodic linear field measures pseudo-time residual damping with stable, neutral and expanding controls. This is distinct from fourth-order accuracy for nonlinear physical-time problems.

## Methods

- [Jameson-type steady multistage Runge–Kutta](<https://hrkoyama.github.io/numerical-methods-atlas/methods/jameson-steady-rk/?lang=en>)

  Use the same base state in every stage and retain complete fields, stage residuals and evaluation counts.
- [Jameson-type steady multistage Runge–Kutta](<https://hrkoyama.github.io/numerical-methods-atlas/methods/jameson-steady-rk/?lang=en>)

## Equations

- [Finite-dimensional linear evolution systems](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#linear-evolution-system-en>)

  Each example distinguishes physical time in damped rotation from pseudo-time used to reduce steady residuals. A fixed dimensionless sixteen-node periodic linear residual; pseudo-time is an iteration parameter.
- [Finite-dimensional linear systems and factorizations](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#finite-dimensional-linear-system-en>)

  Finite matrices A and right-hand sides b define algebraic problems. Fixed LU, Cholesky, refinement and symmetric-indefinite saddle controls are distinct from continuum PDE solutions. A fixed dimensionless sixteen-node periodic linear residual; pseudo-time is an iteration parameter.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/jameson-steady-linear-modes/?lang=en#jameson-steady-linear-modes-en-algorithm>)

  Use the same base state in every stage and retain complete fields, stage residuals and evaluation counts.
- [Finite-dimensional linear evolution systems](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#linear-evolution-system-en>)

  Each example distinguishes physical time in damped rotation from pseudo-time used to reduce steady residuals.
- [Finite-dimensional linear systems and factorizations](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#finite-dimensional-linear-system-en>)

  Finite matrices A and right-hand sides b define algebraic problems. Fixed LU, Cholesky, refinement and symmetric-indefinite saddle controls are distinct from continuum PDE solutions.

## Problem figures

- [Real-space mode damping with steady multistage RK](<https://hrkoyama.github.io/numerical-methods-atlas/problems/jameson-steady-linear-modes/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/steady-rk/results/jameson-steady-linear-modes-preview.png
- [Real-space mode damping with steady multistage RK](<https://hrkoyama.github.io/code/validated-examples/2026-11-24/steady-rk/results/jameson-steady-linear-modes.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/steady-rk/results/jameson-steady-linear-modes.png

## Exact / reference solutions

- [Real-space mode damping with steady multistage RK — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/jameson-steady-linear-modes/?lang=en#references-en>)

  Retain all 41 original numerical targets and their actual decisions. Only the expanding-control absolute residual goal is a separate study outcome; the other 40 requirements and faithful recomputation from saved arrays remain mandatory.
- [Real-space mode damping with steady multistage RK](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-jameson-steady-linear-modes-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference A fixed dimensionless sixteen-node periodic linear residual; pseudo-time is an iteration parameter. Limited to a fixed linear example; no JST compressible flux, nonlinear fourth-order RK or all-start convergence claim. Verification of this study does not mean that all original numerical targets were met.
- [Real-space mode damping with steady multistage RK](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-jameson-steady-linear-modes-en>)
  reference_kind: analytic

  Analytic reference A fixed dimensionless sixteen-node periodic linear residual; pseudo-time is an iteration parameter.
- [Real-space mode damping with steady multistage RK — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/jameson-steady-linear-modes/?lang=en#jameson-steady-linear-modes-en-validation>)

  Retain all 41 original numerical targets and their actual decisions. Only the expanding-control absolute residual goal is a separate study outcome; the other 40 requirements and faithful recomputation from saved arrays remain mandatory.
- [Real-space mode damping with steady multistage RK](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-jameson-steady-linear-modes-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference A fixed dimensionless sixteen-node periodic linear residual; pseudo-time is an iteration parameter. Limited to a fixed linear example; no JST compressible flux, nonlinear fourth-order RK or all-start convergence claim. Verification of this study does not mean that all original numerical targets were met.

## Code and validation

- [Real-space mode damping with steady multistage RK](<https://hrkoyama.github.io/numerical-methods-atlas/validation/jameson-steady-linear-modes/?lang=en>)
  availability: run

  Apply four steady residual stages on a periodic grid, separating damping, neutrality and amplification of discrete modes. The retained first run missed the original absolute residual goal in the expanding control.
