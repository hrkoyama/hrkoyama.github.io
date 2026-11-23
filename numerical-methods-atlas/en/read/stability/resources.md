# Differences, CFL, von Neumann analysis, and Lax

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/stability/

Resources explicitly registered to the methods, problems and executions of this chapter.

## Methods

- [Forward spatial difference](<https://hrkoyama.github.io/numerical-methods-atlas/methods/forward-difference/?lang=en>)
- [Backward spatial difference](<https://hrkoyama.github.io/numerical-methods-atlas/methods/backward-difference/?lang=en>)
- [Centered spatial difference](<https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en>)
- [Upwind finite differences](<https://hrkoyama.github.io/numerical-methods-atlas/methods/upwind/?lang=en>)
- [Lax–Friedrichs](<https://hrkoyama.github.io/numerical-methods-atlas/methods/lax-friedrichs/?lang=en>)
- [Lax–Wendroff](<https://hrkoyama.github.io/numerical-methods-atlas/methods/lax-wendroff/?lang=en>)
- [Upwind finite differences](<https://hrkoyama.github.io/numerical-methods-atlas/methods/upwind/?lang=en>)

  Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions.

## Equations

- [Linear advection](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#linear-advection-en>)

  Transport at constant speed a: translation, numerical diffusion and stability. Representative equations related to this problem. See the image/problem conditions and each execution example for initial conditions, boundary conditions and parameters.
- [Linear advection](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#linear-advection-en>)

  Transport at constant speed a: translation, numerical diffusion and stability.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#execution-advection-sine-en>)

  First-order upwind plus forward Euler, input CFL=0.5. The reference is continuous-PDE translation, not the discrete amplification factor.

## Problem figures

- [Periodic sine-wave advection](<https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/advection-sine.png

## Exact / reference solutions

- [Periodic sine-wave advection — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=en#references-en>)

  Analytic translation of a periodic sine is the standard. The problem merges different amplitudes and representations; the reference-library amplitude 0.25 is not the input for every execution example.
- [Advection / sine translation](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-sine-advection-en>)
  relation: related-model
  reference_kind: analytic

  Analytic reference Periodic unit interval; constant advection speed 1. Same periodic sine-transport model at speed one. The library amplitude is 0.25 versus 0.2 in the common fixed input; DG/CIP representations and output times also differ.
- [Periodic sine advection: upwind and analytic transport — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/advection-sine/?lang=en#advection-sine-en-validation>)

  CSV contains one row per fine-grid center, with the analytic reference evaluated at exactly the same time and location. Periodic-mean and maximum-principle checks allow 10^-12 for roundoff.
- [Advection / sine translation](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-sine-advection-en>)
  relation: related-model
  reference_kind: analytic

  Analytic reference Periodic unit interval; constant advection speed 1. Same periodic sine-transport model at speed one. The library amplitude is 0.25 versus 0.2 in the common fixed input; DG/CIP representations and output times also differ.

## Code and validation

- [Reaction-diffusion: separate second-order space and fourth-order time](<https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-fourier/?lang=en>)
  availability: run

  Validate a small linear diffusion-reaction operator against continuous and semidiscrete Fourier solutions.
- [Turing instability: linear growth and small-amplitude patterns](<https://hrkoyama.github.io/numerical-methods-atlas/validation/turing-schnakenberg/?lang=en>)
  availability: run

  Use a matrix exponential to validate stable homogeneous kinetics and diffusion-driven growth of a selected Schnakenberg mode.
- [Finite-amplitude Schnakenberg transient: nonlinearity and independent reference](<https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-nonlinear/?lang=en>)
  availability: run

  Validate a finite-amplitude reaction-diffusion transient to t=8 with an independent Fourier–Galerkin reference, grid/time convergence and newly generated harmonics.
- [Near-saturated Schnakenberg pattern: near-stationarity and grid/time convergence](<https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-pattern/?lang=en>)
  availability: run

  Compare the selected1D pattern at t=100 with an independent reference. Separate reference90→100 change/full-PDE residual from the finite-step primary FD residual.
- [Periodic sine advection: upwind and analytic transport](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/advection-sine/?lang=en>)
  availability: run

  Advance q_t+a q_x=0 for one period on a unit periodic interval. Compare first-order upwind on 64/128 points with an analytically translated sine, exporting computed, analytic and error values.
- [Zalesak-type 2D rotation: conservation, bounds and shape error](<https://hrkoyama.github.io/numerical-methods-atlas/validation/zalesak-rotation/?lang=en>)
  availability: run

  Rotate a slotted disk through one full turn with an actual 2D finite-volume solver, comparing donor-cell and minmod MUSCL. Eight runs combine three grids with half-cell-center and 45-degree-start probes; measure conservation, bounds at every SSP stage, shape error and slot filling.
- [Euler double rarefaction: positivity at every stage](<https://hrkoyama.github.io/numerical-methods-atlas/validation/euler-double-rarefaction-positivity/?lang=en>)
  availability: run

  Evolve the existing strong double rarefaction on 128/256/512 cells, connecting mean-preserving positivity scaling to MUSCL, global LF fluxes and SSPRK(3,3). Log density, pressure and boundary budgets for every FE substep and SSP convex combination.
- [Forward spatial difference — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/forward-difference/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [Backward spatial difference — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/backward-difference/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [Centered spatial difference — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [Upwind finite differences — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/upwind/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [Lax–Friedrichs — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/lax-friedrichs/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [Lax–Wendroff — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/lax-wendroff/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
