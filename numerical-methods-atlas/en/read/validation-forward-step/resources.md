# Mach-3 forward-facing step: lightweight 2D verification

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-forward-step/

Resources explicitly registered to the methods, problems and executions of this chapter.

## Methods

- [HLL](<https://hrkoyama.github.io/numerical-methods-atlas/methods/hll/?lang=en>)

  Retain the earlier HLL/MUSCL and slope-limiter comparisons; the additional lightweight example uses piecewise-constant HLL plus Heun. Methods belonging to the reference implementation are identified separately with its source and conditions.
- [MUSCL reconstruction](<https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=en>)

  Retain the earlier HLL/MUSCL and slope-limiter comparisons; the additional lightweight example uses piecewise-constant HLL plus Heun. Methods belonging to the reference implementation are identified separately with its source and conditions.
- [Minmod](<https://hrkoyama.github.io/numerical-methods-atlas/methods/minmod/?lang=en>)

  Retain the earlier HLL/MUSCL and slope-limiter comparisons; the additional lightweight example uses piecewise-constant HLL plus Heun. Methods belonging to the reference implementation are identified separately with its source and conditions.
- [Monotonized central / MC](<https://hrkoyama.github.io/numerical-methods-atlas/methods/mc/?lang=en>)

  Retain the earlier HLL/MUSCL and slope-limiter comparisons; the additional lightweight example uses piecewise-constant HLL plus Heun. Methods belonging to the reference implementation are identified separately with its source and conditions.
- [Heun / SSPRK(2,2)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en>)

  Retain the earlier HLL/MUSCL and slope-limiter comparisons; the additional lightweight example uses piecewise-constant HLL plus Heun. Methods belonging to the reference implementation are identified separately with its source and conditions.
- [HLL](<https://hrkoyama.github.io/numerical-methods-atlas/methods/hll/?lang=en>)
- [Heun / SSPRK(2,2)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en>)

## Equations

- [Compressible Euler equations](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#euler-en>)

  The one-dimensional conservative form. Consult each test for its equation of state, initial data and boundaries. Two-dimensional Euler flow with gamma=1.4 and inflow rho=1.4,u=3,v=0,p=1 evolves to T=4 in [0,3]×[0,1] minus a step of height .2 starting at x=.6.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/forward-step-m3/?lang=en#forward-step-m3-en-algorithm>)

  Published Numart piecewise-constant HLL, unsplit x/y divergence and Heun/SSPRK(2,2) become a standalone package. Six boundary categories integrate the actual fluxes at both RK stages with identical weights. CFL.4, at most20000steps per grid. Every predictor/update checks positive density and pressure. No state floor, repair or hidden retry; invalid stages retain raw arrays/completed history and fail.
- [Compressible Euler equations](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#euler-en>)

  The one-dimensional conservative form. Consult each test for its equation of state, initial data and boundaries.

## Problem figures

- [Mach-3 forward-facing step](<https://hrkoyama.github.io/numerical-methods-atlas/problems/forward-step/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/results/forward-step-m3-preview.png
- [Mach3 forward step: wall budgets and grid verification](<https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/results/forward-step-m3.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/results/forward-step-m3.png

## Exact / reference solutions

- [Mach-3 forward-facing step — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/forward-step/?lang=en#references-en>)

  No exact full-field solution is attached. A newly executed separate C++ finite-volume reference and its two-grid increment are shown, with the shared flux family/time integration,uncorrected corner and finite-grid limits made explicit.
- [Mach-3 forward-facing step: independent C++ finite-grid numerical reference](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-forward-step-en>)
  relation: same-problem
  reference_kind: numerical-reference

  Finite-grid numerical reference Two-dimensional ideal-gas Euler flow with gamma=1.4 in [0,3]×[0,1] excluding the solid step x>=.6,y<.2. Uniform initial/inflow primitive state (rho,u,v,p)=(1.4,3,0,1), reflecting slip channel/step walls, right zero-gradient outflow and T=4. The reference is a separately written C++17 unsplit finite-volume implementation with primitive MUSCL generalized minmod(theta=1.5), Davis HLL flux and Heun/SSPRK2 at CFL=.3 on 240×80 and480×160 cells. Normal slopes touching walls/exterior boundaries are zero; reconstructed primitive slopes may be rescaled without altering cell means. The primary Python calculation uses piecewise-constant HLL plus Heun; flux family/time equations are shared, while implementation and spatial reconstruction are separate. No Woodward–Colella corner entropy/enthalpy reset, state floors or time-step retries are used. The uncorrected corner can produce an entropy layer that affects the downstream reflected shock/Mach stem. This is a finite-grid numerical reference, not an exact solution, rigorous error bound, replication of corner-corrected original PPM figures, or proof that fine slip lines/vortices are resolved. Conservatively restrict newly independently executed C++17 MUSCL/HLL/Heun reference data. The finite-grid numerical reference shares the HLL family,Heun and the uncorrected corner; it is not an exact full-field solution or error bound.
- [Mach-3 forward-facing step: independent C++ finite-grid numerical reference](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-forward-step-en>)
  reference_kind: numerical-reference

  Finite-grid numerical reference Two-dimensional ideal-gas Euler flow with gamma=1.4 in [0,3]×[0,1] excluding the solid step x>=.6,y<.2. Uniform initial/inflow primitive state (rho,u,v,p)=(1.4,3,0,1), reflecting slip channel/step walls, right zero-gradient outflow and T=4. The reference is a separately written C++17 unsplit finite-volume implementation with primitive MUSCL generalized minmod(theta=1.5), Davis HLL flux and Heun/SSPRK2 at CFL=.3 on 240×80 and480×160 cells. Normal slopes touching walls/exterior boundaries are zero; reconstructed primitive slopes may be rescaled without altering cell means. The primary Python calculation uses piecewise-constant HLL plus Heun; flux family/time equations are shared, while implementation and spatial reconstruction are separate. No Woodward–Colella corner entropy/enthalpy reset, state floors or time-step retries are used. The uncorrected corner can produce an entropy layer that affects the downstream reflected shock/Mach stem. This is a finite-grid numerical reference, not an exact solution, rigorous error bound, replication of corner-corrected original PPM figures, or proof that fine slip lines/vortices are resolved.
- [Mach3 forward step: wall budgets and grid verification — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/forward-step-m3/?lang=en#forward-step-m3-en-validation>)

  Inputs, acceptance,24 unit checks and numerical source were frozen before the first primary test/PDE execution. Checks cover analytic Mach3 normal-shock Rankine-Hugoniot identities, uniform parallel-channel flow, zero stationary-wall mass/energy flux, step-pressure force orientation, actual four-component budgets and raw failure retention. Newly executed separate C++17 MUSCL/generalized-minmod theta1.5/HLL/Heun references atNy80/160 are conservatively restricted for whole-fluid density/pressure L1 comparison. Ordinary public-ZIP verification reads saved reference data; reference source, contracts and execution records are bundled. The first referenceNy160 exhausted its preregistered120second budget; that actual timeout is preserved. A reference revision removed only unnecessary diagnostic-string allocation and was repinned before first primary execution; physical inputs,arithmetic,CFL and acceptance values did not change. All24 tests, three final-time runs and45 gates passed with-W error. Primary density L1=.14754/.12878/.10265, pressure L1=.19373/.16015/.12242 and last-pair density slope=.327. Reference80/160 increments=.02636/.03063, about.257/.250 of the finest primary differences. Maximum four-component relative boundary-budget residual=2.99e-13; all integrated wall mass/energy fluxes are zero. The three primary grids took about46seconds on the original Mac; revised reference80/160 took about8/65seconds.
- [Mach-3 forward-facing step: independent C++ finite-grid numerical reference](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-forward-step-en>)
  relation: same-problem
  reference_kind: numerical-reference

  Finite-grid numerical reference Two-dimensional ideal-gas Euler flow with gamma=1.4 in [0,3]×[0,1] excluding the solid step x>=.6,y<.2. Uniform initial/inflow primitive state (rho,u,v,p)=(1.4,3,0,1), reflecting slip channel/step walls, right zero-gradient outflow and T=4. The reference is a separately written C++17 unsplit finite-volume implementation with primitive MUSCL generalized minmod(theta=1.5), Davis HLL flux and Heun/SSPRK2 at CFL=.3 on 240×80 and480×160 cells. Normal slopes touching walls/exterior boundaries are zero; reconstructed primitive slopes may be rescaled without altering cell means. The primary Python calculation uses piecewise-constant HLL plus Heun; flux family/time equations are shared, while implementation and spatial reconstruction are separate. No Woodward–Colella corner entropy/enthalpy reset, state floors or time-step retries are used. The uncorrected corner can produce an entropy layer that affects the downstream reflected shock/Mach stem. This is a finite-grid numerical reference, not an exact solution, rigorous error bound, replication of corner-corrected original PPM figures, or proof that fine slip lines/vortices are resolved. Conservatively restrict newly independently executed C++17 MUSCL/HLL/Heun reference data. The finite-grid numerical reference shares the HLL family,Heun and the uncorrected corner; it is not an exact full-field solution or error bound.

## Code and validation

- [Mach3 forward step: wall budgets and grid verification](<https://hrkoyama.github.io/numerical-methods-atlas/validation/forward-step-m3/?lang=en>)
  availability: run

  Actual2D Euler finite volumes evolve60x20,120x40 and240x80 meshes toT4, comparing separately implemented MUSCL finite-grid references. Actual numerical wall fluxes, including the vertical and horizontal step faces, close all four conserved budgets. Figures and code explicitly use the variant without corner entropy correction.
