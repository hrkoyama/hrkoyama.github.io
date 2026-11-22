# Exact and reference solutions

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/reference-solutions/

Resources explicitly registered to the methods, problems and executions of this chapter.

## Methods

No chapter-specific association is registered. Atlas-wide index: [Methods and code reference](https://hrkoyama.github.io/numerical-methods-atlas/methods/?lang=en)

## Equations

No chapter-specific association is registered. Atlas-wide index: [Equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en)

## Problem figures

No chapter-specific association is registered. Atlas-wide index: [Test problems by name and figure](https://hrkoyama.github.io/numerical-methods-atlas/gallery/?lang=en)

## Exact / reference solutions

- [Advection / sine translation](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-sine-advection-en>)
  reference_kind: analytic

  Analytic reference Periodic unit interval; constant advection speed 1.
- [Heat / Fourier-mode decay](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-sine-heat-en>)
  reference_kind: analytic

  Analytic reference Periodic unit interval; viscosity 0.02.
- [Burgers / shock](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-burgers-shock-en>)
  reference_kind: analytic

  Analytic reference Entropy solution of a scalar whole-line Riemann problem; constant endpoint continuation.
- [Burgers / rarefaction](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-burgers-fan-en>)
  reference_kind: analytic

  Analytic reference Entropy solution of a scalar whole-line Riemann problem; constant endpoint continuation.
- [Traffic / upstream shock](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-traffic-jam-en>)
  reference_kind: analytic

  Analytic reference Entropy solution of a scalar whole-line Riemann problem; constant endpoint continuation.
- [Traffic / clearing fan](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-traffic-fan-en>)
  reference_kind: analytic

  Analytic reference Entropy solution of a scalar whole-line Riemann problem; constant endpoint continuation.
- [Euler / Sod](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-euler-sod-en>)
  reference_kind: semi-analytic

  Semi-analytic reference Ideal gas; gamma>1; planar 1D waves; vacuum has zero conserved state and undefined velocity.
- [Euler / Lax](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-euler-lax-en>)
  reference_kind: semi-analytic

  Semi-analytic reference Ideal gas; gamma>1; planar 1D waves; vacuum has zero conserved state and undefined velocity.
- [Euler / double rarefaction](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-euler-double-rarefaction-en>)
  reference_kind: semi-analytic

  Semi-analytic reference Ideal gas; gamma>1; planar 1D waves; vacuum has zero conserved state and undefined velocity.
- [Euler / generated vacuum](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-euler-vacuum-en>)
  reference_kind: analytic

  Analytic reference Ideal gas; gamma>1; planar 1D waves; vacuum has zero conserved state and undefined velocity.
- [Shallow water / wet dam break](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-swe-dam-break-en>)
  reference_kind: semi-analytic

  Semi-analytic reference Flat bottom; constant g; dry states allowed in the reference only, not the existing FV solver.
- [Shallow water / dry-bed fan](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-swe-dry-bed-en>)
  reference_kind: analytic

  Analytic reference Flat bottom; constant g; dry states allowed in the reference only, not the existing FV solver.
- [Shallow water / dry middle state](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-swe-vacuum-en>)
  reference_kind: analytic

  Analytic reference Flat bottom; constant g; dry states allowed in the reference only, not the existing FV solver.
- [Isothermal / density jump](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-isothermal-jump-en>)
  reference_kind: semi-analytic

  Semi-analytic reference p = c_s² rho; constant c_s; strictly positive initial density; no vacuum state or energy equation.
- [Poisson / manufactured sine](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-poisson-manufactured-en>)
  reference_kind: manufactured

  Manufactured solution Zero Dirichlet endpoints. The forcing is chosen from the target solution; this is not an arbitrary-source Poisson solution.
- [Viscous channel / Couette](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-couette-en>)
  reference_kind: analytic

  Analytic reference Fully developed planar steady channel; walls u(0)=0,u(1)=1; zero pressure gradient.
- [Viscous channel / Poiseuille](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-poiseuille-en>)
  reference_kind: analytic

  Analytic reference Fully developed planar steady channel, no slip, unit density; −dp/dx=G or body acceleration G.
- [Viscous flow / 2D Taylor–Green](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-taylor-green-en>)
  reference_kind: analytic

  Analytic reference Periodic [0,2π]²; unit density; viscosity 0.1; zero mean pressure. Web profile is an x-slice at y=π/4. Taylor–Green: x-slice at y = π/4. These are point values, not two-dimensional cell averages.

## Code and validation

No chapter-specific association is registered. Atlas-wide index: [Code, inputs and validation](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=en)
