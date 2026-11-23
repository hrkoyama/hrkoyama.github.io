# Euler double rarefaction: positivity at every stage

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-euler-positivity/

Resources explicitly registered to the methods, problems and executions of this chapter.

## Methods

- [Lax–Friedrichs](<https://hrkoyama.github.io/numerical-methods-atlas/methods/lax-friedrichs/?lang=en>)
- [MUSCL reconstruction](<https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=en>)
- [Mean-preserving positive-state scaling](<https://hrkoyama.github.io/numerical-methods-atlas/methods/positive-scaling/?lang=en>)
- [SSPRK(3,3)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk33/?lang=en>)

## Equations

- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/euler-double-rarefaction-positivity/?lang=en#euler-double-rarefaction-positivity-en-algorithm>)

  Unlimited conservative central linear reconstruction is scaled toward its mean with one common theta per cell until both endpoint densities/pressures are positive. The two endpoint mean remains the original conserved mean. Shared LF FE updates are combined by SSPRK(3,3), reconstructing/limiting before every flux stage. Epsilon1e-13 is a reconstruction target, not an injected density/energy floor. No average repair or hidden time-step retries are used.
- [Compressible Euler equations](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#euler-en>)

  The one-dimensional conservative form. Consult each test for its equation of state, initial data and boundaries.

## Problem figures

- [Euler double rarefaction: positivity at every stage](<https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/results/euler-double-rarefaction-positivity.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/results/euler-double-rarefaction-positivity.png

## Exact / reference solutions

- [Euler double rarefaction: positivity at every stage — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/euler-double-rarefaction-positivity/?lang=en#euler-double-rarefaction-positivity-en-validation>)

  Freeze 27 unit tests and 73 gates over three grids before execution. Retain negative raw endpoint pressures, then separately measure limited endpoints, FE means, SSP convex means, theta and all three boundary-flux conservation budgets. Cross-check the closed symmetric fan against the prior independent logarithmic-pressure root evaluator; record errors/refinement against conserved Gauss8/16 cell means.
- [Euler / double rarefaction](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-euler-double-rarefaction-en>)
  relation: related-model
  reference_kind: semi-analytic

  Semi-analytic reference Ideal gas; gamma>1; planar 1D waves; vacuum has zero conserved state and undefined velocity. γ=1.4, states (1,-2,0.4)/(1,2,0.4), [0,1], x0=0.5 and t=0.15 match the saved preview. Physical inputs match, but the card’s point samples and the saved computation’s finite-volume cell averages/discrete grid are different representations.

## Code and validation

- [Euler double rarefaction: positivity at every stage](<https://hrkoyama.github.io/numerical-methods-atlas/validation/euler-double-rarefaction-positivity/?lang=en>)
  availability: run

  Evolve the existing strong double rarefaction on 128/256/512 cells, connecting mean-preserving positivity scaling to MUSCL, global LF fluxes and SSPRK(3,3). Log density, pressure and boundary budgets for every FE substep and SSP convex combination.
