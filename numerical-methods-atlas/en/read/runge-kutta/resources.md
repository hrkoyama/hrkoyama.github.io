# Runge–Kutta families: stages, order, stability, and SSP

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/runge-kutta/

Resources explicitly registered to the methods, problems and executions of this chapter.

## Methods

- [Dormand–Prince RK45](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rk45/?lang=en>)
- [Forward Euler](<https://hrkoyama.github.io/numerical-methods-atlas/methods/forward-euler/?lang=en>)

  Public nonautonomous/nonlinear manufactured-solution checks exercise every explicit RK tableau; the saved preview uses RK4.
- [Heun / SSPRK(2,2)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en>)

  Public nonautonomous/nonlinear manufactured-solution checks exercise every explicit RK tableau; the saved preview uses RK4.
- [Explicit midpoint RK2](<https://hrkoyama.github.io/numerical-methods-atlas/methods/explicit-midpoint/?lang=en>)

  Public nonautonomous/nonlinear manufactured-solution checks exercise every explicit RK tableau; the saved preview uses RK4.
- [Ralston RK2](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ralston/?lang=en>)

  Public nonautonomous/nonlinear manufactured-solution checks exercise every explicit RK tableau; the saved preview uses RK4.
- [Kutta RK3](<https://hrkoyama.github.io/numerical-methods-atlas/methods/kutta3/?lang=en>)

  Public nonautonomous/nonlinear manufactured-solution checks exercise every explicit RK tableau; the saved preview uses RK4.
- [SSPRK(3,3)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk33/?lang=en>)

  Public nonautonomous/nonlinear manufactured-solution checks exercise every explicit RK tableau; the saved preview uses RK4.
- [SSPRK(4,3)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk43/?lang=en>)

  Public nonautonomous/nonlinear manufactured-solution checks exercise every explicit RK tableau; the saved preview uses RK4.
- [Classical RK4](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=en>)

  Public nonautonomous/nonlinear manufactured-solution checks exercise every explicit RK tableau; the saved preview uses RK4.
- [SSPRK(5,4)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk54/?lang=en>)

  Public nonautonomous/nonlinear manufactured-solution checks exercise every explicit RK tableau; the saved preview uses RK4.
- [Forward Euler](<https://hrkoyama.github.io/numerical-methods-atlas/methods/forward-euler/?lang=en>)

  Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.
- [Heun / SSPRK(2,2)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en>)

  Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.
- [Explicit midpoint RK2](<https://hrkoyama.github.io/numerical-methods-atlas/methods/explicit-midpoint/?lang=en>)

  Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.
- [Ralston RK2](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ralston/?lang=en>)

  Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.
- [Kutta RK3](<https://hrkoyama.github.io/numerical-methods-atlas/methods/kutta3/?lang=en>)

  Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.
- [SSPRK(3,3)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk33/?lang=en>)

  Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.
- [SSPRK(4,3)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk43/?lang=en>)

  Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.
- [Classical RK4](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=en>)

  Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.
- [SSPRK(5,4)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk54/?lang=en>)

  Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

## Equations

No chapter-specific association is registered. Atlas-wide index: [Equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en)

## Problem figures

- [Nonlinear nonautonomous ODE with exponential exact solution](<https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-exp-ode/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/nonlinear-exp-ode.png
- [Rational-decay ODE (y′ = −y²)](<https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-rational-decay/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/nonlinear-rational-decay.png

## Exact / reference solutions

- [Nonlinear nonautonomous ODE with exponential exact solution — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-exp-ode/?lang=en#references-en>)

  Check temporal refinement against the manufactured exact solution y=exp(t) for y′=-y²+exp(2t)+exp(t), y(0)=1.
- [Rational-decay ODE (y′ = −y²) — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-rational-decay/?lang=en#references-en>)

  Use the exact solution 1/(1+t) for y′=-y², y(0)=1, to check nonlinear errors and orders of several explicit Runge–Kutta methods.

## Code and validation

- [RK45: embedded errors, dense output and events](<https://hrkoyama.github.io/numerical-methods-atlas/validation/rk45-dense-events/?lang=en>)
  availability: run

  Use analytic damped rotation to test acceptance, rejection, FSAL ownership, dense interpolation and directed event times separately.
- [Hodgkin–Huxley: clamps, rest and firing](<https://hrkoyama.github.io/numerical-methods-atlas/validation/hodgkin-huxley-controls/?lang=en>)
  availability: run

  Compare analytic clamp gates and a four-state system with segment-owned current.
- [Fisher–KPP: a special-speed exact front](<https://hrkoyama.github.io/numerical-methods-atlas/validation/fisher-kpp-special-front/?lang=en>)
  availability: run

  Separate profile, phase, grid, time and finite-boundary errors.
- [Schnakenberg:2D boundaries and initial modes](<https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-2d-boundary-modes/?lang=en>)
  availability: run

  Compare two Neumann perturbations and a Dirichlet perturbation against nonlinear Galerkin references.
- [Keller–Segel: a manufactured coupled-flux solution](<https://hrkoyama.github.io/numerical-methods-atlas/validation/keller-segel-forced-flux/?lang=en>)
  availability: run

  Use smooth exact2D fields to test cross fluxes, stage timing and mass ledgers.
- [Dormand–Prince RK45 — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rk45/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [Nonlinear nonautonomous ODE with exponential exact solution — code and validation status](<https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-exp-ode/?lang=en#code-en>)
  availability: source

  Inspect the corresponding public checks and distribution conditions.
