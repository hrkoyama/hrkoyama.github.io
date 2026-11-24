# Mie scattering width of a two-dimensional dielectric cylinder

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-maxwell-cylinder/

Resources explicitly registered to the methods, problems and executions of this chapter. Evolve the actual two-dimensional scattered fields and compare closed-contour Poynting power with an independent cylindrical series.

## Methods

- [Yee finite-difference time-domain method](<https://hrkoyama.github.io/numerical-methods-atlas/methods/fdtd/?lang=en>)

  Advance the scattered Yee fields with an exact discrete incident difference on the polarization-contrast support. Accumulate E and H at their own integer and half times, then integrate physical power after four-point native-face collocation.
- [Two-step leapfrog](<https://hrkoyama.github.io/numerical-methods-atlas/methods/leapfrog/?lang=en>)

  Advance the scattered Yee fields with an exact discrete incident difference on the polarization-contrast support. Accumulate E and H at their own integer and half times, then integrate physical power after four-point native-face collocation.
- [Yee finite-difference time-domain method](<https://hrkoyama.github.io/numerical-methods-atlas/methods/fdtd/?lang=en>)
- [Two-step leapfrog](<https://hrkoyama.github.io/numerical-methods-atlas/methods/leapfrog/?lang=en>)

## Equations

- [Linear Maxwell fields in vacuum and dielectrics](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#maxwell-en>)

  The representative equations describe three-dimensional linear electromagnetics. This implementation is restricted to a z-invariant, genuinely two-dimensional Yee cylinder problem with Ez/Hx/Hy. Use c = epsilon0 = mu0 = 1, an infinite cylinder with Ez polarization, radius 0.25, relative permittivity 2.25 and vacuum wavelength 1. The 6 × 6 domain has four-side PML and an explicitly nodal staircase geometry.
- [Linear Maxwell fields in vacuum and dielectrics](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#maxwell-en>)

  The representative equations describe three-dimensional linear electromagnetics. This implementation is restricted to a z-invariant, genuinely two-dimensional Yee cylinder problem with Ez/Hx/Hy.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/cylinder-mie2d/?lang=en#cylinder-mie2d-en-algorithm>)

  Advance the scattered Yee fields with an exact discrete incident difference on the polarization-contrast support. Accumulate E and H at their own integer and half times, then integrate physical power after four-point native-face collocation.

## Problem figures

- [Mie scattering width of a two-dimensional dielectric cylinder](<https://hrkoyama.github.io/numerical-methods-atlas/problems/cylinder-mie2d/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-cylinder/results/cylinder-mie2d-preview.png
- [Mie scattering width of a two-dimensional dielectric cylinder](<https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-cylinder/results/cylinder-mie2d.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-cylinder/results/cylinder-mie2d.png

## Exact / reference solutions

- [Mie scattering width of a two-dimensional dielectric cylinder — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/cylinder-mie2d/?lang=en#references-en>)

  Use 12/18/24 points per wavelength, 32 burn-in periods and 8 measured periods. Check two contours, consecutive four-period windows, half-amplitude phasors after a complete repeated evolution, and a vacuum control at the five saved times. Compare scattering width and exterior fields with the cylindrical series.
- [Exterior series and scattering width of a dielectric cylinder](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-cylinder-mie2d-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference Lossless infinite cylinder, Ez polarization, c = epsilon0 = mu0 = 1, radius 0.25, epsilon = 2.25 and vacuum wavelength 1. The analytical field is exterior to the exact circle. This is a lossless two-dimensional Ez cylinder, not a three-dimensional sphere. Report staircase geometry error without claiming general second-order curved-boundary accuracy or precision scattering for arbitrary frequencies and materials.
- [Exterior series and scattering width of a dielectric cylinder](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-cylinder-mie2d-en>)
  reference_kind: analytic

  Analytic reference Lossless infinite cylinder, Ez polarization, c = epsilon0 = mu0 = 1, radius 0.25, epsilon = 2.25 and vacuum wavelength 1. The analytical field is exterior to the exact circle.
- [Mie scattering width of a two-dimensional dielectric cylinder — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/cylinder-mie2d/?lang=en#cylinder-mie2d-en-validation>)

  Use 12/18/24 points per wavelength, 32 burn-in periods and 8 measured periods. Check two contours, consecutive four-period windows, half-amplitude phasors after a complete repeated evolution, and a vacuum control at the five saved times. Compare scattering width and exterior fields with the cylindrical series.
- [Exterior series and scattering width of a dielectric cylinder](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-cylinder-mie2d-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference Lossless infinite cylinder, Ez polarization, c = epsilon0 = mu0 = 1, radius 0.25, epsilon = 2.25 and vacuum wavelength 1. The analytical field is exterior to the exact circle. This is a lossless two-dimensional Ez cylinder, not a three-dimensional sphere. Report staircase geometry error without claiming general second-order curved-boundary accuracy or precision scattering for arbitrary frequencies and materials.

## Code and validation

- [Mie scattering width of a two-dimensional dielectric cylinder](<https://hrkoyama.github.io/numerical-methods-atlas/validation/cylinder-mie2d/?lang=en>)
  availability: run

  Evolve the actual two-dimensional scattered fields and compare closed-contour Poynting power with an independent cylindrical series.
