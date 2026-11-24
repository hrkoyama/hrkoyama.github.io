# Time integration and leapfrog

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/time-integration/

Resources explicitly registered to the methods, problems and executions of this chapter.

## Methods

- [Forward Euler](<https://hrkoyama.github.io/numerical-methods-atlas/methods/forward-euler/?lang=en>)
- [Backward Euler](<https://hrkoyama.github.io/numerical-methods-atlas/methods/backward-euler/?lang=en>)
- [Heun / SSPRK(2,2)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en>)
- [Explicit midpoint RK2](<https://hrkoyama.github.io/numerical-methods-atlas/methods/explicit-midpoint/?lang=en>)
- [Ralston RK2](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ralston/?lang=en>)
- [Kutta RK3](<https://hrkoyama.github.io/numerical-methods-atlas/methods/kutta3/?lang=en>)
- [SSPRK(3,3)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk33/?lang=en>)
- [SSPRK(4,3)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk43/?lang=en>)
- [Classical RK4](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=en>)
- [SSPRK(5,4)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk54/?lang=en>)
- [Implicit midpoint](<https://hrkoyama.github.io/numerical-methods-atlas/methods/implicit-midpoint/?lang=en>)
- [Two-step leapfrog](<https://hrkoyama.github.io/numerical-methods-atlas/methods/leapfrog/?lang=en>)
- [Velocity Verlet / particle leapfrog](<https://hrkoyama.github.io/numerical-methods-atlas/methods/verlet/?lang=en>)

  Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions.

## Equations

- [Hamiltonian systems and oscillators](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#hamiltonian-en>)

  Canonical equations and a representative separable Hamiltonian. Harmonic and quartic oscillators distinguish energy error from symplecticity. Representative equations related to this problem. See the image/problem conditions and each execution example for initial conditions, boundary conditions and parameters.

## Problem figures

- [Harmonic oscillator, including complex-ODE form](<https://hrkoyama.github.io/numerical-methods-atlas/problems/harmonic-oscillator/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/harmonic-oscillator.png

## Exact / reference solutions

- [Harmonic oscillator, including complex-ODE form — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/harmonic-oscillator/?lang=en#references-en>)

  Compare with analytic sine/cosine trajectories, including complex-ODE form, and distinguish phase, energy and geometric map properties. No dedicated reference-library card is included.

## Code and validation

- [SWASHES topographic flow: lakes and nonzero steady discharge](<https://hrkoyama.github.io/numerical-methods-atlas/validation/swashes-topography/?lang=en>)
  availability: run

  Check two lake equilibria separately from nonzero subcritical flow, distinguishing lake preservation from moving-flow discretization error.
- [Dry-bed dam break: actual wetting and dry states](<https://hrkoyama.github.io/numerical-methods-atlas/validation/dry-bed-dam-break/?lang=en>)
  availability: run

  Start the right half at exactly h=q=0 and compare wetting-front advance, conservation and conservative errors with the Ritter analytic solution.
- [Su–Olson1996 non-equilibrium diffusion](<https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-diffusion1996/?lang=en>)
  availability: run

  Advance actual radiation/material fields with the Marshak boundary and compare with independently qualified pinned ExactPack integrals.
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
- [Noh shocks: zero-pressure planar, cylindrical and spherical flow](<https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/?lang=en>)
  availability: run

  An original small 1D finite-volume code solves zero-pressure Noh flow in planar, cylindrical and spherical symmetry. Grids 64/128/256/512 measure full-domain error, origin heating, shock location and budgets, and compare spherical boundary-inflow time-quadrature error with its analytic identity.
- [Noh problem: an actual 2D Cartesian Euler calculation](<https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-cartesian-2d/?lang=en>)
  availability: run

  A small 2D Euler finite-volume calculation evolves density, both momenta and total energy over the full square. Three grids,32²/64²/128², measure Noh-reference errors, budgets and grid orientation effects. The picture shows the actual evolved 2D array.
- [Sedov–Taylor point blast: lightweight spherical-radial validation](<https://hrkoyama.github.io/numerical-methods-atlas/validation/sedov-blast/?lang=en>)
  availability: run

  A lightweight spherical-radial Euler finite-volume example deposits unit energy inside fixed radius0.03. Three grids of128/256/512 radial cells measure differences from a point-blast similarity reference and conservation budgets. The picture is a section display of1D spherical data, not a2D Cartesian calculation.
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
- [Two-dimensional absorber shadow and M1 transport](<https://hrkoyama.github.io/numerical-methods-atlas/validation/shadow-absorber2d/?lang=en>)
  availability: run

  Compare the actual evolved circular-absorber shadow with characteristic chord attenuation, signed-angle transport and nonlinear M1.
- [Opposing beams and information loss in the M1 closure](<https://hrkoyama.github.io/numerical-methods-atlas/validation/opposing-beams2d/?lang=en>)
  availability: run

  Show the M1 limitation in actual opposing-packet evolution; validate the same closed M1 solver independently with a manufactured solution.
- [Euler double rarefaction: positivity at every stage](<https://hrkoyama.github.io/numerical-methods-atlas/validation/euler-double-rarefaction-positivity/?lang=en>)
  availability: run

  Evolve the existing strong double rarefaction on 128/256/512 cells, connecting mean-preserving positivity scaling to MUSCL, global LF fluxes and SSPRK(3,3). Log density, pressure and boundary budgets for every FE substep and SSP convex combination.
- [Low-Mach isentropic vortex: preconditioned Roe flux verification](<https://hrkoyama.github.io/numerical-methods-atlas/validation/low-mach-vortex/?lang=en>)
  availability: run

  The same nonlinear 2D Euler vortex is evolved to T=0.1 on N=16/32/64 at background Mach 0.1/0.01, comparing ordinary Roe with Miczek spatial flux preconditioning. Twelve fixed runs retain velocity and dynamically scaled pressure errors, conserved budgets, acoustic steps and actual stage states.
- [Zalesak-type 2D rotation: conservation, bounds and shape error](<https://hrkoyama.github.io/numerical-methods-atlas/validation/zalesak-rotation/?lang=en>)
  availability: run

  Rotate a slotted disk through one full turn with an actual 2D finite-volume solver, comparing donor-cell and minmod MUSCL. Eight runs combine three grids with half-cell-center and 45-degree-start probes; measure conservation, bounds at every SSP stage, shape error and slot filling.
- [SRHD symmetric two-shock collision](<https://hrkoyama.github.io/numerical-methods-atlas/validation/srhd-collision/?lang=en>)
  availability: run

  Compare a relativistic symmetric collision with independent exact Taub-based conserved cell means; save actual1D x–t fields.
- [SRMHD finite-amplitude circularly polarized Alfvén wave](<https://hrkoyama.github.io/numerical-methods-atlas/validation/srmhd-alfven/?lang=en>)
  availability: run

  Evolve a nonlinear finite-amplitude wave for one period with full SRMHD magnetic stress and induction; check exact cell means,phase,amplitude and refinement.
- [WENO-JS/Z: fixed critical-point and epsilon comparison](<https://hrkoyama.github.io/numerical-methods-atlas/validation/weno-critical-epsilon/?lang=en>)
  availability: run

  Compare WENO5 JS and Z power-two weights from the same cell means, then evolve actual periodic transport. Retain three regularity classes, three epsilon choices, fixed grids and separate halved-time-step diagnostics.
- [Logistic growth: analytic solution and time refinement](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/logistic-growth/?lang=en>)
  availability: run

  One dimensionless population. Compare RK4 with the analytic solution at every output time; check nonnegativity and time refinement. Excludes reaction–diffusion and multispecies models.
- [SIR: independent DOP853 reference, conservation and convergence](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/sir-epidemic/?lang=en>)
  availability: run

  Closed homogeneous population-fraction SIR. Compare RK4 with independently implemented SciPy DOP853; check conservation, nonnegativity and time convergence. Excludes SEIR, spatial spread and calibration to observations.
- [Reaction-diffusion: separate second-order space and fourth-order time](<https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-fourier/?lang=en>)
  availability: run

  Validate a small linear diffusion-reaction operator against continuous and semidiscrete Fourier solutions.
- [Turing instability: linear growth and small-amplitude patterns](<https://hrkoyama.github.io/numerical-methods-atlas/validation/turing-schnakenberg/?lang=en>)
  availability: run

  Use a matrix exponential to validate stable homogeneous kinetics and diffusion-driven growth of a selected Schnakenberg mode.
- [FitzHugh-Nagumo: pulse excitation, recovery and an independent ODE reference](<https://hrkoyama.github.io/numerical-methods-atlas/validation/fitzhugh-nagumo/?lang=en>)
  availability: run

  Excite a two-variable reduced membrane ODE with a current pulse; check all-output-time errors, temporal refinement and recovery against DOP853.
- [Actual2D C-grid rotating shallow-water time advance](<https://hrkoyama.github.io/numerical-methods-atlas/validation/cgrid-rotating-wave/?lang=en>)
  availability: run

  Time-advance actual2D staggered fields and distinguish continuous-wave references from semidiscrete symbols.
- [Finite-amplitude Schnakenberg transient: nonlinearity and independent reference](<https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-nonlinear/?lang=en>)
  availability: run

  Validate a finite-amplitude reaction-diffusion transient to t=8 with an independent Fourier–Galerkin reference, grid/time convergence and newly generated harmonics.
- [Near-saturated Schnakenberg pattern: near-stationarity and grid/time convergence](<https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-pattern/?lang=en>)
  availability: run

  Compare the selected1D pattern at t=100 with an independent reference. Separate reference90→100 change/full-PDE residual from the finite-step primary FD residual.
- [Harmonic oscillator: Verlet phase error and energy](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/harmonic-oscillator/?lang=en>)
  availability: run

  Advance the existing unit-mass, unit-frequency harmonic oscillator with velocity Verlet. Compare analytic states over 20 time units at 200/400/800 steps, original-energy deviation and reversal.
- [Forward Euler — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/forward-euler/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [Backward Euler — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/backward-euler/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [Heun / SSPRK(2,2) — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [Explicit midpoint RK2 — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/explicit-midpoint/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [Ralston RK2 — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ralston/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [Kutta RK3 — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/kutta3/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [SSPRK(3,3) — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk33/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [SSPRK(4,3) — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk43/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [Classical RK4 — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [SSPRK(5,4) — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk54/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [Implicit midpoint — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/implicit-midpoint/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [Two-step leapfrog — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/leapfrog/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
