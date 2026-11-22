# Polar and cylindrical coordinates: tensors and viscosity

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/coordinates-viscosity/

The chapter is supported by pointwise cylindrical tensor identities and analytic-field checks. Pipe Poiseuille and cylindrical Couette checks are not identified with the reference library's planar-channel cases. No matching standalone problem figure or fixed-input PDE execution is registered.

## Methods

No chapter-specific association is registered. Atlas-wide index: [Methods and code reference](https://hrkoyama.github.io/numerical-methods-atlas/methods/?lang=en)

## Equations

No chapter-specific association is registered. Atlas-wide index: [Equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en)

## Problem figures

No chapter-specific association is registered. Atlas-wide index: [Test problems by name and figure](https://hrkoyama.github.io/numerical-methods-atlas/gallery/?lang=en)

## Exact / reference solutions

No chapter-specific association is registered. Atlas-wide index: [Exact and reference solutions](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en)

## Code and validation

- [Cylindrical tensor and viscous-stress routines](<https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/coordinates.py>)
  availability: source

  Source routines for velocity gradients, Newtonian viscous stress, stress divergence and basis transformations using physical orthonormal components at r > 0. They do not supply a cylindrical Navier–Stokes PDE solver, an axis boundary scheme or a spherical-coordinate implementation.
- [Analytic-field and tensor-identity checks in cylindrical coordinates](<https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_coordinates.py>)
  availability: source

  From the extracted distribution, run python -m pytest -q tests/test_coordinates.py. Checks cover rigid rotation, pipe Poiseuille flow, cylindrical Couette flow, Cartesian affine transformations, nonnegative dissipation and rejection of axis/invalid inputs. These checks are distinct from planar-channel reference cases and time-dependent PDE executions.
- [Existing shared code distribution / ZIP](<https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip>)
  availability: source

  The existing shared distribution contains the source and tests linked above. Run the focused check commands from the extracted distribution folder. The archive also contains other chapters’ code; the notes on each link identify the scope checked here.
