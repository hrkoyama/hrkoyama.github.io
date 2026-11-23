# WENO critical points and epsilon dependence

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-weno-critical/

Resources explicitly registered to the methods, problems and executions of this chapter.

## Methods

- [WENO5-JS](<https://hrkoyama.github.io/numerical-methods-atlas/methods/weno-js/?lang=en>)
- [FD WENO5-Z](<https://hrkoyama.github.io/numerical-methods-atlas/methods/weno-z/?lang=en>)
- [Classical RK4](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=en>)

## Equations

- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/weno-critical-epsilon/?lang=en#weno-critical-epsilon-en-algorithm>)

  Share three candidates, linear weights(.1,.6,.3) and JS indicators. Normalize JS d/(beta+epsilon)² or Z d[1+(|beta0−beta2|/(beta+epsilon))²]. Use epsilon10⁻⁴⁰,10⁻⁶,h². Actual transport uses shared upwind face fluxes and classical RK4 at Courant.1 without state clipping/retries.
- [Linear advection](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#linear-advection-en>)

  Transport at constant speed a: translation, numerical diffusion and stability.

## Problem figures

- [WENO-JS/Z: fixed critical-point and epsilon comparison](<https://hrkoyama.github.io/code/validated-examples/2026-11-23/weno-critical/results/weno-critical-epsilon.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/weno-critical/results/weno-critical-epsilon.png

## Exact / reference solutions

- [WENO critical points: polynomial cell means and analytic periodic transport](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-weno-critical-profile-en>)
  reference_kind: analytic

  Analytic reference Local references integrate polynomials over five cells centered around x=0 and evaluate at h/2. Regular, first-critical and second-critical profiles use h=1/64…1/512. The actual periodic-transport reference is the Fourier-integrated cell mean of q₀=cos(2πx)+.1sin³(2πx) on[0,1], speed1,T1, checked independently by Gauss12 point-function quadrature. Local polynomials differ from the evolved profile; neither point samples nor another PDE calculation are substituted for cell means.
- [WENO-JS/Z: fixed critical-point and epsilon comparison — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/weno-critical-epsilon/?lang=en#weno-critical-epsilon-en-validation>)

  Pre-run contract fixes72 local reconstructions,24 PDE runs and36 pytest checks. Qualify analytic means against independent Gauss12 quadrature; retain local errors/weights, transport L1/L2/Linf, mass, stage finiteness, intermediate times and shared-flux budgets. Six finest-grid half-dt differences must be at most10% of corresponding continuum errors.
- [Advection / sine translation](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-sine-advection-en>)
  relation: related-model
  reference_kind: analytic

  Analytic reference Periodic unit interval; constant advection speed 1. Same periodic sine-transport model at speed one. The library amplitude is 0.25 versus 0.2 in the common fixed input; DG/CIP representations and output times also differ.
- [WENO critical points: polynomial cell means and analytic periodic transport](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-weno-critical-profile-en>)
  relation: related-model
  reference_kind: analytic

  Analytic reference Local references integrate polynomials over five cells centered around x=0 and evaluate at h/2. Regular, first-critical and second-critical profiles use h=1/64…1/512. The actual periodic-transport reference is the Fourier-integrated cell mean of q₀=cos(2πx)+.1sin³(2πx) on[0,1], speed1,T1, checked independently by Gauss12 point-function quadrature. Local polynomials differ from the evolved profile; neither point samples nor another PDE calculation are substituted for cell means. An additional constant-speed periodic-transport reference. The cos+.1sin³ cell means and local critical polynomials differ from the historical single-sine/CIP display.

## Code and validation

- [WENO-JS/Z: fixed critical-point and epsilon comparison](<https://hrkoyama.github.io/numerical-methods-atlas/validation/weno-critical-epsilon/?lang=en>)
  availability: run

  Compare WENO5 JS and Z power-two weights from the same cell means, then evolve actual periodic transport. Retain three regularity classes, three epsilon choices, fixed grids and separate halved-time-step diagnostics.
