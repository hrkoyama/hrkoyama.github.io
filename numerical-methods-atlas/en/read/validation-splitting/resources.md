# Operator splitting: Lie–Trotter and Strang on the same reaction–diffusion problem

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-splitting/

Resources explicitly registered to the methods, problems and executions of this chapter.

## Methods

- [Lie–Trotter splitting](<https://hrkoyama.github.io/numerical-methods-atlas/methods/lie-trotter/?lang=en>)
- [Strang splitting](<https://hrkoyama.github.io/numerical-methods-atlas/methods/strang-splitting/?lang=en>)

## Equations

- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-splitting/?lang=en#reaction-diffusion-splitting-en-algorithm>)

  Lie–Trotter uses diffusion(h) then reaction(h); Strang uses diffusion(h/2), reaction(h), diffusion(h/2), always passing the updated state. Both apply the exact exponential of the centered-FD diffusion matrix by FFT and the same implicit-midpoint reaction/Newton tolerance 2e−13 with at most 12 residual evaluations. The reaction flow is a second-order approximation, not exact. No clipping, adaptive steps or fallback; nonconvergence is failure.

## Problem figures

- [Lie–Trotter versus Strang on the same nonlinear reaction–diffusion input](<https://hrkoyama.github.io/code/validated-examples/2026-11-22/splitting/results/reaction-diffusion-splitting.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/splitting/results/reaction-diffusion-splitting.png

## Exact / reference solutions

- [Lie–Trotter versus Strang on the same nonlinear reaction–diffusion input — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-splitting/?lang=en#reaction-diffusion-splitting-en-validation>)

  The reference independently assembles the SAME FD semidiscretization with a real-space sparse matrix and separately written reaction RHS, then integrates it unsplit with Radau. Tighter Radau and separate DOP853 runs measure reference sensitivity relative to the finest Strang error. Norms are per-species mean L1, RMS L2 and maximum L∞, then the worse species; refinement uses the maximum across the four common positive observation times. Also record Newton-tolerance sensitivity, positive tested substeps, reaction source/sink balance and reversed-Lie ordering.

## Code and validation

- [Lie–Trotter versus Strang on the same nonlinear reaction–diffusion input](<https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-splitting/?lang=en>)
  availability: run

  Advance a 32-point Schnakenberg reaction–diffusion problem to T=1 with matched inputs and subsolvers. Four step sizes check first-/second-order temporal convergence, reference sensitivity, reaction balance and failure on nonconvergence in a lightweight comparison.
