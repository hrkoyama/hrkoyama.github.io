# Sedov–Taylor point blast: lightweight spherical-radial validation

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-sedov/

Resources explicitly registered to the methods, problems and executions of this chapter.

## Methods

- [Rusanov / local Lax–Friedrichs flux](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rusanov/?lang=en>)

  A scoped spherical-radial example using piecewise-constant Rusanov finite-volume fluxes and SSPRK2/Heun.
- [Heun / SSPRK(2,2)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en>)

  A scoped spherical-radial example using piecewise-constant Rusanov finite-volume fluxes and SSPRK2/Heun.
- [Rusanov / local Lax–Friedrichs flux](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rusanov/?lang=en>)
- [Heun / SSPRK(2,2)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en>)

## Equations

- [Compressible Euler equations](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#euler-en>)

  The one-dimensional conservative form. Consult each test for its equation of state, initial data and boundaries. Nondimensional spherical-radial Euler flow, evolving radial density, momentum and total energy with volume weighting.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/sedov-blast/?lang=en#sedov-blast-en-algorithm>)

  Piecewise-constant Rusanov fluxes on spherical shells with SSPRK2/Heun. The radial-momentum source p(A_right-A_left)/V is integrated at the same RK stages, with a stationary uniform-pressure balance test. CFL.4 uses the minimum V/(A_left+A_right)/(|u|+c). No pressure seed, floor, cell repair or hidden timestep retry; an invalid stage retains raw conserved values and history and fails.
- [Compressible Euler equations](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#euler-en>)

  The one-dimensional conservative form. Consult each test for its equation of state, initial data and boundaries.

## Problem figures

- [Sedov–Taylor point blast](<https://hrkoyama.github.io/numerical-methods-atlas/problems/sedov/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/sedov/results/sedov-blast-preview.png
- [Sedov–Taylor point blast: lightweight spherical-radial validation](<https://hrkoyama.github.io/code/validated-examples/2026-11-23/sedov/results/sedov-blast.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/sedov/results/sedov-blast.png

## Exact / reference solutions

- [Sedov–Taylor point blast — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/sedov/?lang=en#references-en>)

  An energy-normalized spherical similarity reference. Numerical integration of similarity ODEs and shell quadrature make this semi-analytic, not closed-form exact cell means. Finite-radius deposition is distinct from the singular ideal point-blast initial data. At fixed finite deposition radius, comparison with the point-source similarity reference includes deposition-model discrepancy; its refinement slope is not a pure spatial order. Changing deposition radius on the same finest grid is a sensitivity diagnostic, not a complete separation of continuum deposition and PDE-discretization errors.
- [Sedov–Taylor point blast: energy-normalized spherical similarity solution](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-sedov-en>)
  relation: same-problem
  reference_kind: semi-analytic

  Semi-analytic reference Ideal-gas Euler in spherical radial symmetry, gamma=5/3, ambient rho0=1 and p0=0, explosion energy E0=1, r in [0,1], t=0.05. The similarity reference describes ideal instantaneous point deposition. Finite-volume runs instead deposit energy inside radius 0.03, with a paired radius-0.015 sensitivity calculation. The reference uses a numerical similarity-ODE integration, a tiny-core regular asymptote and split shell quadrature; it is semi-analytic, not closed-form exact cell means. The gallery picture is a central section of one-dimensional spherical-radial data, not a two-dimensional Cartesian computation. Fixed-radius errors include point-source model discrepancy, so their refinement slope is not a pure spatial order; the paired-radius calculation is only a sensitivity diagnostic. An energy-normalized spherical similarity reference. Numerical integration of similarity ODEs and shell quadrature make this semi-analytic, not closed-form exact cell means. Finite-radius deposition is distinct from the singular ideal point-blast initial data. At fixed finite deposition radius, comparison with the point-source similarity reference includes deposition-model discrepancy; its refinement slope is not a pure spatial order. Changing deposition radius on the same finest grid is a sensitivity diagnostic, not a complete separation of continuum deposition and PDE-discretization errors.
- [Sedov–Taylor point blast: energy-normalized spherical similarity solution](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-sedov-en>)
  reference_kind: semi-analytic

  Semi-analytic reference Ideal-gas Euler in spherical radial symmetry, gamma=5/3, ambient rho0=1 and p0=0, explosion energy E0=1, r in [0,1], t=0.05. The similarity reference describes ideal instantaneous point deposition. Finite-volume runs instead deposit energy inside radius 0.03, with a paired radius-0.015 sensitivity calculation. The reference uses a numerical similarity-ODE integration, a tiny-core regular asymptote and split shell quadrature; it is semi-analytic, not closed-form exact cell means. The gallery picture is a central section of one-dimensional spherical-radial data, not a two-dimensional Cartesian computation. Fixed-radius errors include point-source model discrepancy, so their refinement slope is not a pure spatial order; the paired-radius calculation is only a sensitivity diagnostic.
- [Sedov–Taylor point blast: lightweight spherical-radial validation — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/sedov-blast/?lang=en#sedov-blast-en-validation>)

  Inputs, numerical sources, acceptance and22 tests were hash-locked before the first FV execution. All22 unit tests and48 gates on four calculations passed on the first attempt. The independent reference integrates the similarity ODE with DOP853, normalizes energy, uses a regular asymptote for xi<.001 and split shell quadrature at the shock. Orders16/32, core cutoff and ODE tolerance are checked separately. The unmodified pinned ExactPack evaluator was independently run at6001/12001 points and compared away from the center/jump with its preregistered5e-4 criterion. Beta=1.15166641793, Rs(.05)=.34746791233. Origin/shock-inclusive volume-weighted density L1 within r<=1.2Rs is.17257/.12785/.07458 and pressure L1 is.18148/.13939/.07615. Finest shock error is1.096 cells; maximum relative discrete-budget residual is about1.34e-15.
- [Sedov–Taylor point blast: energy-normalized spherical similarity solution](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-sedov-en>)
  relation: same-problem
  reference_kind: semi-analytic

  Semi-analytic reference Ideal-gas Euler in spherical radial symmetry, gamma=5/3, ambient rho0=1 and p0=0, explosion energy E0=1, r in [0,1], t=0.05. The similarity reference describes ideal instantaneous point deposition. Finite-volume runs instead deposit energy inside radius 0.03, with a paired radius-0.015 sensitivity calculation. The reference uses a numerical similarity-ODE integration, a tiny-core regular asymptote and split shell quadrature; it is semi-analytic, not closed-form exact cell means. The gallery picture is a central section of one-dimensional spherical-radial data, not a two-dimensional Cartesian computation. Fixed-radius errors include point-source model discrepancy, so their refinement slope is not a pure spatial order; the paired-radius calculation is only a sensitivity diagnostic. An energy-normalized spherical similarity reference. Numerical integration of similarity ODEs and shell quadrature make this semi-analytic, not closed-form exact cell means. Finite-radius deposition is distinct from the singular ideal point-blast initial data. At fixed finite deposition radius, comparison with the point-source similarity reference includes deposition-model discrepancy; its refinement slope is not a pure spatial order. Changing deposition radius on the same finest grid is a sensitivity diagnostic, not a complete separation of continuum deposition and PDE-discretization errors.

## Code and validation

- [Sedov–Taylor point blast: lightweight spherical-radial validation](<https://hrkoyama.github.io/numerical-methods-atlas/validation/sedov-blast/?lang=en>)
  availability: run

  A lightweight spherical-radial Euler finite-volume example deposits unit energy inside fixed radius0.03. Three grids of128/256/512 radial cells measure differences from a point-blast similarity reference and conservation budgets. The picture is a section display of1D spherical data, not a2D Cartesian calculation.
