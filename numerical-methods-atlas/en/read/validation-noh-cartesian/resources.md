# Noh:2D Cartesian flow and grid orientation error

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-noh-cartesian/

Resources explicitly registered to the methods, problems and executions of this chapter.

## Methods

- [Rusanov / local Lax–Friedrichs flux](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rusanov/?lang=en>)

  Rusanov/Heun are used in both radial1D and new Cartesian2D runs. MUSCL/minmod apply only to the earlier spherical series; the new2D reconstruction is piecewise constant.
- [Heun / SSPRK(2,2)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en>)

  Rusanov/Heun are used in both radial1D and new Cartesian2D runs. MUSCL/minmod apply only to the earlier spherical series; the new2D reconstruction is piecewise constant.
- [MUSCL reconstruction](<https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=en>)

  Rusanov/Heun are used in both radial1D and new Cartesian2D runs. MUSCL/minmod apply only to the earlier spherical series; the new2D reconstruction is piecewise constant.
- [Minmod](<https://hrkoyama.github.io/numerical-methods-atlas/methods/minmod/?lang=en>)

  Rusanov/Heun are used in both radial1D and new Cartesian2D runs. MUSCL/minmod apply only to the earlier spherical series; the new2D reconstruction is piecewise constant.
- [Rusanov / local Lax–Friedrichs flux](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rusanov/?lang=en>)
- [Heun / SSPRK(2,2)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en>)

## Equations

- [Compressible Euler equations](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#euler-en>)

  The one-dimensional conservative form. Consult each test for its equation of state, initial data and boundaries. Planar/cylindrical/spherical radial Euler and actual2D Cartesian Euler. The2D edition has no geometric source, radial reduction or symmetry boundary; all four edges prescribe cold inflow.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-cartesian-2d/?lang=en#noh-cartesian-2d-en-algorithm>)

  Unsplit shared-face x/y piecewise-constant Rusanov fluxes and SSPRK2/Heun. CFL .35 uses (max a_x+max a_y)/dx. Cold physical outer fluxes are spatially integrated analytically and their affine time dependence is integrated at both Heun stages. No cell repair, pressure floor/seed or hidden timestep retry; invalid stages retain raw arrays and fail.
- [Compressible Euler equations](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#euler-en>)

  The one-dimensional conservative form. Consult each test for its equation of state, initial data and boundaries.

## Problem figures

- [Noh problem: cold converging flow and outward shock](<https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/noh-cartesian/results/noh-cartesian-2d-preview.png
- [Noh problem: an actual 2D Cartesian Euler calculation](<https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/noh-cartesian/results/noh-cartesian-2d.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/noh-cartesian/results/noh-cartesian-2d.png

## Exact / reference solutions

- [Noh problem: cold converging flow and outward shock — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=en#references-en>)

  Analytic reference for the same Noh problem.1D uses exact conserved-volume means;2D uses density means from shock-split Cartesian cell quadrature. Distinguish points/cell means and p(mean U)/mean p.
- [Noh cold-inflow shock: planar, cylindrical and spherical symmetry](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-noh-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference Ideal-gas Euler, gamma=5/3, rho0=1, inward speed 1, p0=0; r in [0,1], t=0.6. Planar (d=1), cylindrical-radial (d=2) and spherical-radial (d=3) finite-volume calculations without a pressure floor. The spherical color picture is a central section of one-dimensional radial data, not a Cartesian three-dimensional computation. A separate full-square2D Cartesian calculation uses [-.5,.5]^2 with32²/64²/128² cells, both momenta and no radial reduction. Its density-cell reference is shock-split quadrature, checked at orders64/128. Analytic reference for the same Noh problem.1D uses exact conserved-volume means;2D uses density means from shock-split Cartesian cell quadrature. Distinguish points/cell means and p(mean U)/mean p.
- [Noh problem: an actual 2D Cartesian Euler calculation — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-cartesian-2d/?lang=en#noh-cartesian-2d-en-validation>)

  Inputs/source/acceptance hashes are saved before execution. All 19 unit tests and 49 gates on three grids passed at the first attempt. Analytic density is integrated over cells by splitting shock-circle cuts and 64-point Gauss quadrature with x=rs sin(theta), checked against 128 points and analytic total mass; these are quadrature references, not closed-form exact cell means. At 128², full-square density L1=.09981, origin-inclusive core L1=.12231; shock errors are.968 axis cells and1.469 diagonal cells. Maximum relative discrete-budget residual is about 4.6e-15. D4 conserved parity and continuous rotational symmetry are measured separately.
- [Noh cold-inflow shock: planar, cylindrical and spherical symmetry](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-noh-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference Ideal-gas Euler, gamma=5/3, rho0=1, inward speed 1, p0=0; r in [0,1], t=0.6. Planar (d=1), cylindrical-radial (d=2) and spherical-radial (d=3) finite-volume calculations without a pressure floor. The spherical color picture is a central section of one-dimensional radial data, not a Cartesian three-dimensional computation. A separate full-square2D Cartesian calculation uses [-.5,.5]^2 with32²/64²/128² cells, both momenta and no radial reduction. Its density-cell reference is shock-split quadrature, checked at orders64/128. Analytic reference for the same Noh problem.1D uses exact conserved-volume means;2D uses density means from shock-split Cartesian cell quadrature. Distinguish points/cell means and p(mean U)/mean p.

## Code and validation

- [Noh shocks: zero-pressure planar, cylindrical and spherical flow](<https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/?lang=en>)
  availability: run

  An original small 1D finite-volume code solves zero-pressure Noh flow in planar, cylindrical and spherical symmetry. Grids 64/128/256/512 measure full-domain error, origin heating, shock location and budgets, and compare spherical boundary-inflow time-quadrature error with its analytic identity.
- [Noh problem: an actual 2D Cartesian Euler calculation](<https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-cartesian-2d/?lang=en>)
  availability: run

  A small 2D Euler finite-volume calculation evolves density, both momenta and total energy over the full square. Three grids,32²/64²/128², measure Noh-reference errors, budgets and grid orientation effects. The picture shows the actual evolved 2D array.
