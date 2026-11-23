# Noh shocks: exact reference, origin heating and refinement

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-noh/

Resources explicitly registered to the methods, problems and executions of this chapter.

## Methods

- [Rusanov / local Lax–Friedrichs flux](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rusanov/?lang=en>)

  All series use Rusanov flux and Heun. Planar/cylindrical reconstruction is piecewise constant; spherical runs use volume-centroid MUSCL/minmod and radial quadrature of face-linear stress, compared with two failed constant-reconstruction baselines under the same 105 gates.
- [Heun / SSPRK(2,2)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en>)

  All series use Rusanov flux and Heun. Planar/cylindrical reconstruction is piecewise constant; spherical runs use volume-centroid MUSCL/minmod and radial quadrature of face-linear stress, compared with two failed constant-reconstruction baselines under the same 105 gates.
- [MUSCL reconstruction](<https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=en>)

  All series use Rusanov flux and Heun. Planar/cylindrical reconstruction is piecewise constant; spherical runs use volume-centroid MUSCL/minmod and radial quadrature of face-linear stress, compared with two failed constant-reconstruction baselines under the same 105 gates.
- [Minmod](<https://hrkoyama.github.io/numerical-methods-atlas/methods/minmod/?lang=en>)

  All series use Rusanov flux and Heun. Planar/cylindrical reconstruction is piecewise constant; spherical runs use volume-centroid MUSCL/minmod and radial quadrature of face-linear stress, compared with two failed constant-reconstruction baselines under the same 105 gates.
- [Rusanov / local Lax–Friedrichs flux](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rusanov/?lang=en>)
- [Heun / SSPRK(2,2)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en>)
- [MUSCL reconstruction](<https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=en>)
- [Minmod](<https://hrkoyama.github.io/numerical-methods-atlas/methods/minmod/?lang=en>)

## Equations

- [Compressible Euler equations](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#euler-en>)

  The one-dimensional conservative form. Consult each test for its equation of state, initial data and boundaries. Planar(d=1), cylindrical-radial(d=2) and spherical-radial(d=3) ideal-gas Euler Noh inflow. The example defines the geometric source, cold inflow, reflecting origin, exactly p0=0 and boundary-time quadrature.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/?lang=en#noh-shock-en-algorithm>)

  Rusanov flux with SSPRK2 (Heun). Planar/cylindrical runs retain piecewise-constant reconstruction. Spherical runs reconstruct conserved variables linearly around volume centroids with minmod slopes based on centroid distances in interior cells and zero slopes in the two boundary cells. A single theta per cell scales all conserved slopes at both faces to check face density/internal energy. Cell means are never corrected and no pressure seed/floor is used. Wave speeds, Rusanov flux and numerical stress P*=F_mom-((u_L+u_R)/2)F_mass use the same face states. The geometric CFL V/(A_La_L+A_Ra_R) uses the prescribed .35. Spherical source quadrature exactly integrates the face-linear numerical stress against 2r dr; planar/cylindrical runs keep the old arithmetic rule. Reconstructed reflection faces use even/odd parity, with physical cold inflow at the outer face. Every RK stage is checked and invalid states cause a retained failure.
- [Compressible Euler equations](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#euler-en>)

  The one-dimensional conservative form. Consult each test for its equation of state, initial data and boundaries.

## Problem figures

- [Noh shocks: zero-pressure planar, cylindrical and spherical flow](<https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/results/noh-shock-preview.png
- [Noh shocks: zero-pressure planar, cylindrical and spherical flow](<https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/results/noh-shock.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/results/noh-shock.png

## Exact / reference solutions

- [Noh shocks: zero-pressure planar, cylindrical and spherical flow — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=en#references-en>)

  The continuous exact solution of this same zero-pressure Noh problem. Distinguish initial-density amplification4^d from the across-shock ratio4. Finite-volume errors use exact conserved-volume averages, with p(mean U) distinct from mean p.
- [Noh cold-inflow shock: planar, cylindrical and spherical symmetry](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-noh-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference Ideal-gas Euler, gamma=5/3, rho0=1, inward speed 1, p0=0; r in [0,1], t=0.6. Planar (d=1), cylindrical-radial (d=2) and spherical-radial (d=3) finite-volume calculations without a pressure floor. The spherical color picture is a central section of one-dimensional radial data, not a Cartesian three-dimensional computation. The continuous exact solution of this same zero-pressure Noh problem. Distinguish initial-density amplification4^d from the across-shock ratio4. Finite-volume errors use exact conserved-volume averages, with p(mean U) distinct from mean p.
- [Noh cold-inflow shock: planar, cylindrical and spherical symmetry](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-noh-en>)
  reference_kind: analytic

  Analytic reference Ideal-gas Euler, gamma=5/3, rho0=1, inward speed 1, p0=0; r in [0,1], t=0.6. Planar (d=1), cylindrical-radial (d=2) and spherical-radial (d=3) finite-volume calculations without a pressure floor. The spherical color picture is a central section of one-dimensional radial data, not a Cartesian three-dimensional computation.
- [Noh shocks: zero-pressure planar, cylindrical and spherical flow — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/?lang=en#noh-shock-en-validation>)

  Retain the planar/cylindrical acceptance file and all 59 original decisions, and save spherical criteria, inputs and source hashes before the first spherical PDE run. The initial cylindrical failure retains its source, all eight diagnostic logs and failed summary; the face-stress revision was tested against the same gates. Analytic conserved means split shock-crossing integrals and distinguish p(mean U) from mean p. The pinned independent LANL ExactPack analytic comparison includes d=1/2/3. New spherical PDE refinements separately measure full-domain r^2-weighted L1/L2/Linf, density L1 in r<=.70rs including the origin, and center/shock/plateau diagnostics. Discrete stage-weighted inflow budgets are distinct from continuous analytic totals; SSPRK2 boundary quadrature is checked through M_h-M_exact=sum(dt^3)/6 and E_h-E_exact=sum(dt^3)/12. The first spherical run retained arithmetic source quadrature and failed two of 105 gates (finest shock-position error 3.923 cells, plateau-density error 11.03%); all results are retained. A second attempt changed only spherical stress quadrature, but still failed the same two gates (3.919 cells and 11.018% density error). A third attempt retains that quadrature and adds MUSCL/minmod reconstruction only for spherical runs, against the same 105 criteria. The third attempt completed 28 tests and all 12 grid runs, passing all 105 gates. At spherical N=512 the whole-domain density L1 is .0114343, shock error 1.98856 cells, plateau-density error 5.2533%, and origin-inclusive core-density L1 .0549503. Maximum center specific-internal-energy excess is 20.59%, worse than the second attempt's 15.52%; not every diagnostic improves.
- [Noh cold-inflow shock: planar, cylindrical and spherical symmetry](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-noh-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference Ideal-gas Euler, gamma=5/3, rho0=1, inward speed 1, p0=0; r in [0,1], t=0.6. Planar (d=1), cylindrical-radial (d=2) and spherical-radial (d=3) finite-volume calculations without a pressure floor. The spherical color picture is a central section of one-dimensional radial data, not a Cartesian three-dimensional computation. The continuous exact solution of this same zero-pressure Noh problem. Distinguish initial-density amplification4^d from the across-shock ratio4. Finite-volume errors use exact conserved-volume averages, with p(mean U) distinct from mean p.

## Code and validation

- [Noh shocks: zero-pressure planar, cylindrical and spherical flow](<https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/?lang=en>)
  availability: run

  An original small 1D finite-volume code solves zero-pressure Noh flow in planar, cylindrical and spherical symmetry. Grids 64/128/256/512 measure full-domain error, origin heating, shock location and budgets, and compare spherical boundary-inflow time-quadrature error with its analytic identity.
