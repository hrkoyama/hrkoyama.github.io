# Wall heating: numerical overheating in Noh flow and at reflecting walls

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/wall-heating/

Resources explicitly registered to the methods, problems and executions of this chapter.

## Methods

- [Rusanov / local Lax–Friedrichs flux](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rusanov/?lang=en>)
- [Heun / SSPRK(2,2)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en>)
- [MUSCL reconstruction](<https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=en>)
- [Minmod](<https://hrkoyama.github.io/numerical-methods-atlas/methods/minmod/?lang=en>)

## Equations

No chapter-specific association is registered. Atlas-wide index: [Equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en)

## Problem figures

No chapter-specific association is registered. Atlas-wide index: [Test problems by name and figure](https://hrkoyama.github.io/numerical-methods-atlas/gallery/?lang=en)

## Exact / reference solutions

No chapter-specific association is registered. Atlas-wide index: [Exact and reference solutions](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en)

## Code and validation

- [Noh shocks: zero-pressure planar, cylindrical and spherical flow](<https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/?lang=en>)
  availability: run

  An original small 1D finite-volume code solves zero-pressure Noh flow in planar, cylindrical and spherical symmetry. Grids 64/128/256/512 measure full-domain error, origin heating, shock location and budgets, and compare spherical boundary-inflow time-quadrature error with its analytic identity.
- [Noh problem: an actual 2D Cartesian Euler calculation](<https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-cartesian-2d/?lang=en>)
  availability: run

  A small 2D Euler finite-volume calculation evolves density, both momenta and total energy over the full square. Three grids,32²/64²/128², measure Noh-reference errors, budgets and grid orientation effects. The picture shows the actual evolved 2D array.
- [Sedov–Taylor point blast: lightweight spherical-radial validation](<https://hrkoyama.github.io/numerical-methods-atlas/validation/sedov-blast/?lang=en>)
  availability: run

  A lightweight spherical-radial Euler finite-volume example deposits unit energy inside fixed radius0.03. Three grids of128/256/512 radial cells measure differences from a point-blast similarity reference and conservation budgets. The picture is a section display of1D spherical data, not a2D Cartesian calculation.
- [Two-dimensional absorber shadow and M1 transport](<https://hrkoyama.github.io/numerical-methods-atlas/validation/shadow-absorber2d/?lang=en>)
  availability: run

  Compare the actual evolved circular-absorber shadow with characteristic chord attenuation, signed-angle transport and nonlinear M1.
- [Opposing beams and information loss in the M1 closure](<https://hrkoyama.github.io/numerical-methods-atlas/validation/opposing-beams2d/?lang=en>)
  availability: run

  Show the M1 limitation in actual opposing-packet evolution; validate the same closed M1 solver independently with a manufactured solution.
- [Saltzman-type skew-grid piston: 2D Euler and ALE](<https://hrkoyama.github.io/numerical-methods-atlas/validation/saltzman-ale-piston/?lang=en>)
  availability: run

  Tan–Lv–Zhu2023 Example8 e0=1e-4 initialvariant. PrescribedaffineALEmesh, not theirWENO/materialLagrangian/remap scheme. Finitepressure RH cellaverages.
- [Double Mach reflection: lightweight grid verification](<https://hrkoyama.github.io/numerical-methods-atlas/validation/double-mach-reflection/?lang=en>)
  availability: run

  Full 2D Euler finite volumes evolve the existing Double Mach initial/boundary data to T=.2 on64x16,128x32 and256x64 cells. Compare a separately written finite-grid reference, actual boundary-flux budgets, an upper incident-front position and a fixed near-wall region.
- [Mach3 forward step: wall budgets and grid verification](<https://hrkoyama.github.io/numerical-methods-atlas/validation/forward-step-m3/?lang=en>)
  availability: run

  Actual2D Euler finite volumes evolve60x20,120x40 and240x80 meshes toT4, comparing separately implemented MUSCL finite-grid references. Actual numerical wall fluxes, including the vertical and horizontal step faces, close all four conserved budgets. Figures and code explicitly use the variant without corner entropy correction.
- [Late Orszag-Tang: independent reference and compression structure](<https://hrkoyama.github.io/numerical-methods-atlas/validation/postshock-orszag-tang/?lang=en>)
  availability: run

  Evolve compressible ideal-MHD Orszag-Tang to T.2 and check density/pressure in interacting compression/shock structure against an independent finite-grid reference.
- [Circular Alfven wave: full-state refinement](<https://hrkoyama.github.io/numerical-methods-atlas/validation/circular-alfven-refinement/?lang=en>)
  availability: run

  Evolve all eight conserved variables and compare circular polarization, including nonzero Bz/vz, against analytic cell means.
- [Magnetic loop: independent 2D reference and refinement](<https://hrkoyama.github.io/numerical-methods-atlas/validation/magnetic-loop-independent/?lang=en>)
  availability: run

  Compare genuine 2D magnetic-loop transport with final conserved fields from independent Athena++, qualified in space and time.
- [Guderley converging shock: lightweight spherical-radial verification](<https://hrkoyama.github.io/numerical-methods-atlas/validation/guderley-implosion/?lang=en>)
  availability: run

  An inward spherical Guderley shock in cold stationary gas is evolved from t=-1 to -0.85 on 128/256/512 radial shells. HLL fluxes and Heun steps are checked against a similarity eigenvalue/field, shock trajectory and discrete conservation budgets.
- [Re100 lid-driven cavity: Ghia centerline comparison](<https://hrkoyama.github.io/numerical-methods-atlas/validation/cavity-ghia-re100/?lang=en>)
  availability: run

  March a real nonperiodic 2D viscous incompressible solver to steady state on 17/33/65 node grids and compare against original Ghia centerlines. Retain streamlines, grid vortex center, true PDE residual and discrete divergence.
- [Nonperiodic wall MMS: velocity, shear and pressure operator](<https://hrkoyama.github.io/numerical-methods-atlas/validation/wall-manufactured/?lang=en>)
  availability: run

  Apply analytic forcing to the same wall-bounded2D solver, measuring grid convergence of velocity/streamfunction and actual wall-vorticity/shear errors. A separate nonzero-Dirichlet manufactured pressure verifies Poisson and boundary-gradient operators.
- [KH initial growth in a smooth periodic shear layer](<https://hrkoyama.github.io/numerical-methods-atlas/validation/kh-initial-growth/?lang=en>)
  availability: run

  Evolve the actual nonlinear2D vorticity PDE and compare finite-time growth and spatial errors with an independent continuous Fourier–Galerkin linear IVP.
- [RT initial growth in smooth Boussinesq double layers](<https://hrkoyama.github.io/numerical-methods-atlas/validation/rt-initial-growth/?lang=en>)
  availability: run

  Advance the actual2D Boussinesq vorticity/active-buoyancy system and compare smooth unstable-layer growth with a separately derived linear IVP.
- [ALE scalar transport on genuinely nonuniform moving cells](<https://hrkoyama.github.io/numerical-methods-atlas/validation/ale-nonuniform-transport/?lang=en>)
  availability: run

  Advance cell integrals and face positions with identical Heun stages, transporting a nonuniform analytic wave beyond a uniform GCL check.
- [Su–Olson transport with an independently published analytical table](<https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-transport1997/?lang=en>)
  availability: run

  Evolve actual signed-angle transport/material exchange and compare with pinned analytical benchmark tables provided by the2023primary author.
- [Shu–Osher: independent reference and mesh refinement](<https://hrkoyama.github.io/numerical-methods-atlas/validation/shu-independent/?lang=en>)
  availability: run

  Compare shock–density-wave interaction against separately executed Athena++ reference data rather than a finer grid of the same Python code.
- [Euler double rarefaction: positivity at every stage](<https://hrkoyama.github.io/numerical-methods-atlas/validation/euler-double-rarefaction-positivity/?lang=en>)
  availability: run

  Evolve the existing strong double rarefaction on 128/256/512 cells, connecting mean-preserving positivity scaling to MUSCL, global LF fluxes and SSPRK(3,3). Log density, pressure and boundary budgets for every FE substep and SSP convex combination.
- [Low-Mach isentropic vortex: preconditioned Roe flux verification](<https://hrkoyama.github.io/numerical-methods-atlas/validation/low-mach-vortex/?lang=en>)
  availability: run

  The same nonlinear 2D Euler vortex is evolved to T=0.1 on N=16/32/64 at background Mach 0.1/0.01, comparing ordinary Roe with Miczek spatial flux preconditioning. Twelve fixed runs retain velocity and dynamically scaled pressure errors, conserved budgets, acoustic steps and actual stage states.
- [Brio–Wu: HLLD and a conservatively restricted numerical reference](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/brio-wu/?lang=en>)
  availability: run

  Evolve the one-dimensional γ=2 ideal-MHD shock tube with Bx=0.75 to t=0.1. Compare 64/128-cell HLLD/MC/SSPRK2 with a 512-cell numerical reference, recording density, pressure, longitudinal field, balances and fallback counts.
- [Zalesak-type 2D rotation: conservation, bounds and shape error](<https://hrkoyama.github.io/numerical-methods-atlas/validation/zalesak-rotation/?lang=en>)
  availability: run

  Rotate a slotted disk through one full turn with an actual 2D finite-volume solver, comparing donor-cell and minmod MUSCL. Eight runs combine three grids with half-cell-center and 45-degree-start probes; measure conservation, bounds at every SSP stage, shape error and slot filling.
- [SRHD symmetric two-shock collision](<https://hrkoyama.github.io/numerical-methods-atlas/validation/srhd-collision/?lang=en>)
  availability: run

  Compare a relativistic symmetric collision with independent exact Taub-based conserved cell means; save actual1D x–t fields.
- [SRMHD finite-amplitude circularly polarized Alfvén wave](<https://hrkoyama.github.io/numerical-methods-atlas/validation/srmhd-alfven/?lang=en>)
  availability: run

  Evolve a nonlinear finite-amplitude wave for one period with full SRMHD magnetic stress and induction; check exact cell means,phase,amplitude and refinement.
- [Rusanov / local Lax–Friedrichs flux — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rusanov/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [Heun / SSPRK(2,2) — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [MUSCL reconstruction — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [Minmod — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/minmod/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
