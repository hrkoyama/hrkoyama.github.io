# Oblique s/p incidence on a Lorentz-dispersive slab

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-maxwell-lorentz/

Resources explicitly registered to the methods, problems and executions of this chapter. Measure complex r/t, power fractions and direct dissipation from actual finite-pulse evolutions and compare them with complex Fresnel slab references.

## Methods

- [Yee finite-difference time-domain method](<https://hrkoyama.github.io/numerical-methods-atlas/methods/fdtd/?lang=en>)

  Use the single-ky Yee spatial operator and local implicit-midpoint Lorentz ADE. Couple both p-polarized electric components to polarization, and remove incident propagation with a matched vacuum pulse on the same grid. Accumulate direct Ohmic and material-damping work separately from modified energy.
- [Two-step leapfrog](<https://hrkoyama.github.io/numerical-methods-atlas/methods/leapfrog/?lang=en>)

  Use the single-ky Yee spatial operator and local implicit-midpoint Lorentz ADE. Couple both p-polarized electric components to polarization, and remove incident propagation with a matched vacuum pulse on the same grid. Accumulate direct Ohmic and material-damping work separately from modified energy.
- [Implicit midpoint](<https://hrkoyama.github.io/numerical-methods-atlas/methods/implicit-midpoint/?lang=en>)

  Use the single-ky Yee spatial operator and local implicit-midpoint Lorentz ADE. Couple both p-polarized electric components to polarization, and remove incident propagation with a matched vacuum pulse on the same grid. Accumulate direct Ohmic and material-damping work separately from modified energy.
- [Yee finite-difference time-domain method](<https://hrkoyama.github.io/numerical-methods-atlas/methods/fdtd/?lang=en>)
- [Two-step leapfrog](<https://hrkoyama.github.io/numerical-methods-atlas/methods/leapfrog/?lang=en>)
- [Implicit midpoint](<https://hrkoyama.github.io/numerical-methods-atlas/methods/implicit-midpoint/?lang=en>)

## Equations

- [Passive Lorentz–Ohmic Maxwell fields](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#maxwell-lorentz-en>)

  A single passive Lorentz pole with positive material energy and direct Ohmic/gamma work. The representative equations are three-dimensional; the implemented solver is the two-dimensional s/p component restriction at one periodic ky. Numerical PML work is not identified with physical dissipation. Use a two-dimensional field restricted to periodic transverse wave number ky = 4 and c = 1. The slab [4, 5] has epsilon_inf = 1.5, delta_epsilon = 0.75, omega_0 = 9, gamma = 0.5 and sigma = 0.04. Outer vacuum ends at PEC caps [-24, 36]; T = 60.
- [Passive Lorentz–Ohmic Maxwell fields](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#maxwell-lorentz-en>)

  A single passive Lorentz pole with positive material energy and direct Ohmic/gamma work. The representative equations are three-dimensional; the implemented solver is the two-dimensional s/p component restriction at one periodic ky. Numerical PML work is not identified with physical dissipation.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/lorentz-oblique-sp/?lang=en#lorentz-oblique-sp-en-algorithm>)

  Use the single-ky Yee spatial operator and local implicit-midpoint Lorentz ADE. Couple both p-polarized electric components to polarization, and remove incident propagation with a matched vacuum pulse on the same grid. Accumulate direct Ohmic and material-damping work separately from modified energy.

## Problem figures

- [Oblique s/p incidence on a Lorentz-dispersive slab](<https://hrkoyama.github.io/numerical-methods-atlas/problems/lorentz-oblique-sp/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/results/lorentz-oblique-sp-preview.png
- [Oblique s/p incidence on a Lorentz-dispersive slab](<https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/results/lorentz-oblique-sp.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/results/lorentz-oblique-sp.png

## Exact / reference solutions

- [Oblique s/p incidence on a Lorentz-dispersive slab — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/lorentz-oblique-sp/?lang=en#references-en>)

  Measure omega = 5.1/6/6.9 from 12 actual material/vacuum evolutions across three resolutions and both polarizations. Check an independent finite-window vacuum geometric sum, complex Fresnel coefficients, direct volume dissipation, all-step PEC budgets and final monitor tails.
- [Complex oblique Fresnel coefficients and direct Lorentz-slab loss](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-lorentz-oblique-sp-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference Vacuum surroundings, ky = 4, slab [4, 5], epsilon_inf = 1.5, delta_epsilon = 0.75, omega_0 = 9, gamma = 0.5 and sigma = 0.04. Compare omega = 5.1/6/6.9 for both s = Ez and p = Hz. This is a genuine single-ky restriction rather than arbitrary transverse data. It covers one passive Lorentz pole and a fixed finite band/window. Gaussian tails are nonzero; window diagnostics and reference errors are reported separately. No strict all-frequency no-return proof is claimed.
- [Complex oblique Fresnel coefficients and direct Lorentz-slab loss](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-lorentz-oblique-sp-en>)
  reference_kind: analytic

  Analytic reference Vacuum surroundings, ky = 4, slab [4, 5], epsilon_inf = 1.5, delta_epsilon = 0.75, omega_0 = 9, gamma = 0.5 and sigma = 0.04. Compare omega = 5.1/6/6.9 for both s = Ez and p = Hz.
- [Oblique s/p incidence on a Lorentz-dispersive slab — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/lorentz-oblique-sp/?lang=en#lorentz-oblique-sp-en-validation>)

  Measure omega = 5.1/6/6.9 from 12 actual material/vacuum evolutions across three resolutions and both polarizations. Check an independent finite-window vacuum geometric sum, complex Fresnel coefficients, direct volume dissipation, all-step PEC budgets and final monitor tails.
- [Complex oblique Fresnel coefficients and direct Lorentz-slab loss](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-lorentz-oblique-sp-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference Vacuum surroundings, ky = 4, slab [4, 5], epsilon_inf = 1.5, delta_epsilon = 0.75, omega_0 = 9, gamma = 0.5 and sigma = 0.04. Compare omega = 5.1/6/6.9 for both s = Ez and p = Hz. This is a genuine single-ky restriction rather than arbitrary transverse data. It covers one passive Lorentz pole and a fixed finite band/window. Gaussian tails are nonzero; window diagnostics and reference errors are reported separately. No strict all-frequency no-return proof is claimed.

## Code and validation

- [Oblique s/p incidence on a Lorentz-dispersive slab](<https://hrkoyama.github.io/numerical-methods-atlas/validation/lorentz-oblique-sp/?lang=en>)
  availability: run

  Measure complex r/t, power fractions and direct dissipation from actual finite-pulse evolutions and compare them with complex Fresnel slab references.
