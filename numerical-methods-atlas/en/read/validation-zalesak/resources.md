# Zalesak-type 2D rotation: conservation, bounds and shape error

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-zalesak/

Resources explicitly registered to the methods, problems and executions of this chapter.

## Methods

- [Upwind finite differences](<https://hrkoyama.github.io/numerical-methods-atlas/methods/upwind/?lang=en>)

  Donor-cell upwinding and minmod MUSCL use the same prescribed rotation, periodic finite-volume grid and SSPRK(3,3). This does not claim implementation of Zalesak FCT.
- [MUSCL reconstruction](<https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=en>)

  Donor-cell upwinding and minmod MUSCL use the same prescribed rotation, periodic finite-volume grid and SSPRK(3,3). This does not claim implementation of Zalesak FCT.
- [Minmod](<https://hrkoyama.github.io/numerical-methods-atlas/methods/minmod/?lang=en>)

  Donor-cell upwinding and minmod MUSCL use the same prescribed rotation, periodic finite-volume grid and SSPRK(3,3). This does not claim implementation of Zalesak FCT.
- [SSPRK(3,3)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk33/?lang=en>)

  Donor-cell upwinding and minmod MUSCL use the same prescribed rotation, periodic finite-volume grid and SSPRK(3,3). This does not claim implementation of Zalesak FCT.
- [Upwind finite differences](<https://hrkoyama.github.io/numerical-methods-atlas/methods/upwind/?lang=en>)
- [MUSCL reconstruction](<https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=en>)
- [Minmod](<https://hrkoyama.github.io/numerical-methods-atlas/methods/minmod/?lang=en>)
- [SSPRK(3,3)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk33/?lang=en>)

## Equations

- [Two-dimensional rotational advection](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#rotational-advection-en>)

  A two-dimensional scalar conservation law in a prescribed rigid rotation. The continuum field returns after one turn, enabling mass, bounds and slotted-shape error checks. This is scalar transport in a prescribed divergence-free rotation, not Euler-fluid evolution. It uses a Zalesak-type slotted-disk shape test without claiming implementation of Zalesak’s FCT algorithm. Pointwise indicator values and geometric conserved cell means are distinguished; numerical tails near periodic boundaries are also measured.
- [Two-dimensional rotational advection](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#rotational-advection-en>)

  A two-dimensional scalar conservation law in a prescribed rigid rotation. The continuum field returns after one turn, enabling mass, bounds and slotted-shape error checks.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/zalesak-rotation/?lang=en#zalesak-rotation-en-algorithm>)

  Use analytic divergence-free normal face averages and one shared upwind flux per interface. Both piecewise-constant donor-cell and mean-preserving directional-minmod MUSCL use SSPRK(3,3). The four face-midpoint mean equals the cell mean; individual outgoing-face Courant<=1/4 gives a convex FE update. Check the actual .20 bound at every stage. No transported-state clipping/floors or rejected/retried steps are used.

## Problem figures

- [Zalesak-type slotted-disk rotation](<https://hrkoyama.github.io/numerical-methods-atlas/problems/zalesak/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/results/zalesak-rotation-preview.png
- [Zalesak-type 2D rotation: conservation, bounds and shape error](<https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/results/zalesak-rotation.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/results/zalesak-rotation.png

## Exact / reference solutions

- [Zalesak-type slotted-disk rotation — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/zalesak/?lang=en#references-en>)

  The reference evaluates the initial indicator under inverse rigid rotation. The continuum field returns after one revolution; comparisons use geometric cell means on the same grid.
- [Zalesak-type slotted disk: rigid rotation and geometric cell means](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-zalesak-rotation-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference Unit-square two-dimensional scalar transport with prescribed velocity (0.5-y,x-0.5), angular speed 1 and period2*pi. The baseline indicator is one inside the disk of radius 0.15 centered at (0.5,0.75), excluding 0.475<x<0.525 and y<0.85, and zero outside. This isolates the normalized slotted-cylinder component described in the official Firedrake setup; its bell, cone, background 1, DG discretization and inflow boundary are not copied. Periodic finite-volume normal velocities match on opposite faces; the compact exact body stays away from the boundary, while numerical tails are measured. Exact rigid characteristics and analytic disk/polygon intersection areas define the reference cell means, not rasterized point samples or a second numerical PDE solution. A full turn returns to the initial continuum shape; rotated/shifted variants are separate fixed diagnostics. Fix the disk and slot geometry and compare stored initial/returned cell means. Distinguish indicator point samples and a finer PDE calculation from this geometric reference.
- [Zalesak-type slotted disk: rigid rotation and geometric cell means](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-zalesak-rotation-en>)
  reference_kind: analytic

  Analytic reference Unit-square two-dimensional scalar transport with prescribed velocity (0.5-y,x-0.5), angular speed 1 and period2*pi. The baseline indicator is one inside the disk of radius 0.15 centered at (0.5,0.75), excluding 0.475<x<0.525 and y<0.85, and zero outside. This isolates the normalized slotted-cylinder component described in the official Firedrake setup; its bell, cone, background 1, DG discretization and inflow boundary are not copied. Periodic finite-volume normal velocities match on opposite faces; the compact exact body stays away from the boundary, while numerical tails are measured. Exact rigid characteristics and analytic disk/polygon intersection areas define the reference cell means, not rasterized point samples or a second numerical PDE solution. A full turn returns to the initial continuum shape; rotated/shifted variants are separate fixed diagnostics.
- [Zalesak-type 2D rotation: conservation, bounds and shape error — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/zalesak-rotation/?lang=en#zalesak-rotation-en-validation>)

  Freeze26 unit checks and158 gates across eight fixed runs before execution. Retain min/max of every FE candidate/SSP convex mean, shared-flux mass budgets, reconstruction mean preservation and three-grid L1/Linf/relative-L2 errors. Independent circle/convex-polygon intersection means are qualified against SciPy vertical-slice quadrature, total area and first moments. Also check quarter/half/three-quarter-turn errors and centroids so a wrong direction or speed cannot hide behind a full-turn return.
- [Zalesak-type slotted disk: rigid rotation and geometric cell means](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-zalesak-rotation-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference Unit-square two-dimensional scalar transport with prescribed velocity (0.5-y,x-0.5), angular speed 1 and period2*pi. The baseline indicator is one inside the disk of radius 0.15 centered at (0.5,0.75), excluding 0.475<x<0.525 and y<0.85, and zero outside. This isolates the normalized slotted-cylinder component described in the official Firedrake setup; its bell, cone, background 1, DG discretization and inflow boundary are not copied. Periodic finite-volume normal velocities match on opposite faces; the compact exact body stays away from the boundary, while numerical tails are measured. Exact rigid characteristics and analytic disk/polygon intersection areas define the reference cell means, not rasterized point samples or a second numerical PDE solution. A full turn returns to the initial continuum shape; rotated/shifted variants are separate fixed diagnostics. Fix the disk and slot geometry and compare stored initial/returned cell means. Distinguish indicator point samples and a finer PDE calculation from this geometric reference.

## Code and validation

- [Zalesak-type 2D rotation: conservation, bounds and shape error](<https://hrkoyama.github.io/numerical-methods-atlas/validation/zalesak-rotation/?lang=en>)
  availability: run

  Rotate a slotted disk through one full turn with an actual 2D finite-volume solver, comparing donor-cell and minmod MUSCL. Eight runs combine three grids with half-cell-center and 45-degree-start probes; measure conservation, bounds at every SSP stage, shape error and slot filling.
