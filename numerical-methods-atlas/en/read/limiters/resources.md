# Slope limiters: minmod, Superbee, MC, van Leer, and van Albada

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/limiters/

Resources explicitly registered to the methods, problems and executions of this chapter.

## Methods

- [Minmod](<https://hrkoyama.github.io/numerical-methods-atlas/methods/minmod/?lang=en>)
- [Superbee](<https://hrkoyama.github.io/numerical-methods-atlas/methods/superbee/?lang=en>)
- [Monotonized central / MC](<https://hrkoyama.github.io/numerical-methods-atlas/methods/mc/?lang=en>)
- [Van Leer limiter](<https://hrkoyama.github.io/numerical-methods-atlas/methods/van-leer/?lang=en>)
- [Clipped Van Albada limiter](<https://hrkoyama.github.io/numerical-methods-atlas/methods/van-albada/?lang=en>)
- [Cubic-Hermite CIP](<https://hrkoyama.github.io/numerical-methods-atlas/methods/cip/?lang=en>)

  Methods used by the stored square-wave CIP and limiter comparisons.
- [MUSCL reconstruction](<https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=en>)

  Methods used by the stored square-wave CIP and limiter comparisons.
- [Minmod](<https://hrkoyama.github.io/numerical-methods-atlas/methods/minmod/?lang=en>)

  Methods used by the stored square-wave CIP and limiter comparisons.
- [Superbee](<https://hrkoyama.github.io/numerical-methods-atlas/methods/superbee/?lang=en>)

  Methods used by the stored square-wave CIP and limiter comparisons.
- [Monotonized central / MC](<https://hrkoyama.github.io/numerical-methods-atlas/methods/mc/?lang=en>)

  Methods used by the stored square-wave CIP and limiter comparisons.
- [Van Leer limiter](<https://hrkoyama.github.io/numerical-methods-atlas/methods/van-leer/?lang=en>)

  Methods used by the stored square-wave CIP and limiter comparisons.
- [Clipped Van Albada limiter](<https://hrkoyama.github.io/numerical-methods-atlas/methods/van-albada/?lang=en>)

  Methods used by the stored square-wave CIP and limiter comparisons.
- [Upwind finite differences](<https://hrkoyama.github.io/numerical-methods-atlas/methods/upwind/?lang=en>)

  Methods used by the stored square-wave CIP and limiter comparisons.
- [TVB modified minmod](<https://hrkoyama.github.io/numerical-methods-atlas/methods/tvb/?lang=en>)

  Methods used by the stored square-wave CIP and limiter comparisons.

## Equations

- [Linear advection](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#linear-advection-en>)

  Transport at constant speed a: translation, numerical diffusion and stability. Representative equations related to this problem. See the image/problem conditions and each execution example for initial conditions, boundary conditions and parameters.

## Problem figures

- [Periodic square-wave advection](<https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-square/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/advection-square.png

## Exact / reference solutions

- [Periodic square-wave advection — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-square/?lang=en#references-en>)

  The standard is periodic translation of the discontinuous square profile. The library sine wave uses different initial data for the same transport model.
- [Advection / sine translation](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-sine-advection-en>)
  relation: related-model
  reference_kind: analytic

  Analytic reference Periodic unit interval; constant advection speed 1. The equation and periodic transport are shared, but the reference uses smooth sine initial data and is not a numerical reference for this square profile.

## Code and validation

- [Noh shocks: zero-pressure planar, cylindrical and spherical flow](<https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/?lang=en>)
  availability: run

  An original small 1D finite-volume code solves zero-pressure Noh flow in planar, cylindrical and spherical symmetry. Grids 64/128/256/512 measure full-domain error, origin heating, shock location and budgets, and compare spherical boundary-inflow time-quadrature error with its analytic identity.
- [Zalesak-type 2D rotation: conservation, bounds and shape error](<https://hrkoyama.github.io/numerical-methods-atlas/validation/zalesak-rotation/?lang=en>)
  availability: run

  Rotate a slotted disk through one full turn with an actual 2D finite-volume solver, comparing donor-cell and minmod MUSCL. Eight runs combine three grids with half-cell-center and 45-degree-start probes; measure conservation, bounds at every SSP stage, shape error and slot filling.
- [Minmod — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/minmod/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [Superbee — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/superbee/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [Monotonized central / MC — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/mc/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [Van Leer limiter — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/van-leer/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [Clipped Van Albada limiter — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/van-albada/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
