# Noh shocks: exact reference, origin heating and refinement

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-noh/

Resources explicitly registered to the methods, problems and executions of this chapter.

## Methods

- [Rusanov / local Lax–Friedrichs flux](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rusanov/?lang=en>)

  The new dedicated edition uses piecewise-constant Rusanov flux with SSPRK2/Heun. It does not alter the older Euler module with a pressure floor; it checks an original consistent first-order radial face-stress source.
- [Heun / SSPRK(2,2)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en>)

  The new dedicated edition uses piecewise-constant Rusanov flux with SSPRK2/Heun. It does not alter the older Euler module with a pressure floor; it checks an original consistent first-order radial face-stress source.
- [Rusanov / local Lax–Friedrichs flux](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rusanov/?lang=en>)
- [Heun / SSPRK(2,2)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en>)

## Equations

- [Compressible Euler equations](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#euler-en>)

  The one-dimensional conservative form. Consult each test for its equation of state, initial data and boundaries. Planar(d=1) and cylindrical-radial(d=2) ideal-gas Euler Noh inflow, with geometric source, cold outer boundary, reflecting origin and exactly p0=0 as specified in the example.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/?lang=en#noh-shock-en-algorithm>)

  Piecewise-constant local Lax–Friedrichs/Rusanov flux and SSPRK2 (Heun), with a geometric CFL based on V/(A_L a_L+A_R a_R). The radial-momentum source uses an original consistent first-order quadrature: average the two interfacial numerical normal stresses P*=F_mom−((u_L+u_R)/2)F_mass and multiply by delta A. This exactly balances static constant pressure and vanishes for d=1. Reflection stress reaches the origin cell rather than allowing singular cold accumulation. No state/pressure floor, clipping or substitution of analytic solution arrays. Negative internal energy within roundoff is logged; only the sound-speed square-root argument uses zero at roundoff.
- [Compressible Euler equations](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#euler-en>)

  The one-dimensional conservative form. Consult each test for its equation of state, initial data and boundaries.

## Problem figures

- [Noh shocks: zero-pressure planar and cylindrical flow](<https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/noh/results/noh-shock-preview.png
- [Noh shocks: zero-pressure planar and cylindrical flow](<https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/noh/results/noh-shock.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/noh/results/noh-shock.png

## Exact / reference solutions

- [Noh shocks: zero-pressure planar and cylindrical flow — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=en#references-en>)

  The continuous exact solution of this same zero-pressure Noh problem. Distinguish initial-density amplification4^d from the across-shock ratio4. Finite-volume errors use exact conserved-volume averages, with p(mean U) distinct from mean p.
- [Noh cold-inflow shock: planar and cylindrical symmetry](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-noh-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference Ideal-gas Euler, gamma=5/3, rho0=1, inward speed 1, p0=0; r in [0,1], t=0.6. Planar (d=1) and cylindrically symmetric radial (d=2) finite-volume calculations; no pressure floor. The radial color image is a revolved one-dimensional solution, not a two-dimensional Cartesian computation. The continuous exact solution of this same zero-pressure Noh problem. Distinguish initial-density amplification4^d from the across-shock ratio4. Finite-volume errors use exact conserved-volume averages, with p(mean U) distinct from mean p.
- [Noh cold-inflow shock: planar and cylindrical symmetry](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-noh-en>)
  reference_kind: analytic

  Analytic reference Ideal-gas Euler, gamma=5/3, rho0=1, inward speed 1, p0=0; r in [0,1], t=0.6. Planar (d=1) and cylindrically symmetric radial (d=2) finite-volume calculations; no pressure floor. The radial color image is a revolved one-dimensional solution, not a two-dimensional Cartesian computation.
- [Noh shocks: zero-pressure planar and cylindrical flow — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/?lang=en#noh-shock-en-validation>)

  Inputs, acceptance criteria and hashes were saved before the first run. The initial cell-pressure p_i delta A source passed planar checks but failed cylindrical shock formation; its source and full refinement results are retained. The interface-stress revision is tested against the SAME thresholds. Analytic conservative cell means split shock-crossing integrals, storing p(mean U) separately from the physical mean pressure. Pinned independent LANL ExactPack was separately executed for points and split-quadrature means. Checks include full-domain volume-weighted relative L1/L2/Linf, explicit center/shock/plateau masks, pressure half-height shock location, initial density amplification 4^d (shock jump 4), and stage-weighted SSPRK2 boundary-inflow budgets.
- [Noh cold-inflow shock: planar and cylindrical symmetry](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-noh-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference Ideal-gas Euler, gamma=5/3, rho0=1, inward speed 1, p0=0; r in [0,1], t=0.6. Planar (d=1) and cylindrically symmetric radial (d=2) finite-volume calculations; no pressure floor. The radial color image is a revolved one-dimensional solution, not a two-dimensional Cartesian computation. The continuous exact solution of this same zero-pressure Noh problem. Distinguish initial-density amplification4^d from the across-shock ratio4. Finite-volume errors use exact conserved-volume averages, with p(mean U) distinct from mean p.

## Code and validation

- [Noh shocks: zero-pressure planar and cylindrical flow](<https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/?lang=en>)
  availability: run

  A small original 1D finite-volume solver advances the Noh problem from exactly zero pressure, in planar and cylindrical-radial symmetry. Grids 64/128/256/512 separately measure volume-weighted errors, shock location, density amplification, origin heating and mass/total-energy budgets including outer inflow.
