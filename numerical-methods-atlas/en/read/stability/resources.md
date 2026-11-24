# Differences, CFL, von Neumann analysis, and Lax

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/stability/

Resources explicitly registered to the methods, problems and executions of this chapter.

## Methods

- [Forward spatial difference](<https://hrkoyama.github.io/numerical-methods-atlas/methods/forward-difference/?lang=en>)
- [Backward spatial difference](<https://hrkoyama.github.io/numerical-methods-atlas/methods/backward-difference/?lang=en>)
- [Centered spatial difference](<https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en>)
- [Upwind finite differences](<https://hrkoyama.github.io/numerical-methods-atlas/methods/upwind/?lang=en>)
- [Lax–Friedrichs](<https://hrkoyama.github.io/numerical-methods-atlas/methods/lax-friedrichs/?lang=en>)
- [Lax–Wendroff](<https://hrkoyama.github.io/numerical-methods-atlas/methods/lax-wendroff/?lang=en>)
- [Upwind finite differences](<https://hrkoyama.github.io/numerical-methods-atlas/methods/upwind/?lang=en>)

  Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions. Compare critical-point reconstruction from cell means using WENO-JS/Z power-two weights and actual periodic scalar transport. Separate epsilon choices, analytic cell means versus point values, and spatial error versus time-step effects. p+1 Gauss solution points, upwind interface flux, Legendre Radau corrections and SSPRK(3,3). Match initial L2 projection, upwind flux and timestep policy to the unchanged published modal DG. Scaled Courant(2p+1)|a|dt/h<=.15; separately halve the timestep at p2/N32.
- [WENO5-JS](<https://hrkoyama.github.io/numerical-methods-atlas/methods/weno-js/?lang=en>)

  Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions. Compare critical-point reconstruction from cell means using WENO-JS/Z power-two weights and actual periodic scalar transport. Separate epsilon choices, analytic cell means versus point values, and spatial error versus time-step effects. p+1 Gauss solution points, upwind interface flux, Legendre Radau corrections and SSPRK(3,3). Match initial L2 projection, upwind flux and timestep policy to the unchanged published modal DG. Scaled Courant(2p+1)|a|dt/h<=.15; separately halve the timestep at p2/N32.
- [FD WENO5-Z](<https://hrkoyama.github.io/numerical-methods-atlas/methods/weno-z/?lang=en>)

  Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions. Compare critical-point reconstruction from cell means using WENO-JS/Z power-two weights and actual periodic scalar transport. Separate epsilon choices, analytic cell means versus point values, and spatial error versus time-step effects. p+1 Gauss solution points, upwind interface flux, Legendre Radau corrections and SSPRK(3,3). Match initial L2 projection, upwind flux and timestep policy to the unchanged published modal DG. Scaled Courant(2p+1)|a|dt/h<=.15; separately halve the timestep at p2/N32.
- [Classical RK4](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=en>)

  Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions. Compare critical-point reconstruction from cell means using WENO-JS/Z power-two weights and actual periodic scalar transport. Separate epsilon choices, analytic cell means versus point values, and spatial error versus time-step effects. p+1 Gauss solution points, upwind interface flux, Legendre Radau corrections and SSPRK(3,3). Match initial L2 projection, upwind flux and timestep policy to the unchanged published modal DG. Scaled Courant(2p+1)|a|dt/h<=.15; separately halve the timestep at p2/N32.
- [Flux reconstruction (FR)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/flux-reconstruction/?lang=en>)

  Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions. Compare critical-point reconstruction from cell means using WENO-JS/Z power-two weights and actual periodic scalar transport. Separate epsilon choices, analytic cell means versus point values, and spatial error versus time-step effects. p+1 Gauss solution points, upwind interface flux, Legendre Radau corrections and SSPRK(3,3). Match initial L2 projection, upwind flux and timestep policy to the unchanged published modal DG. Scaled Courant(2p+1)|a|dt/h<=.15; separately halve the timestep at p2/N32.
- [Discontinuous Galerkin / Legendre](<https://hrkoyama.github.io/numerical-methods-atlas/methods/dg/?lang=en>)

  Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions. Compare critical-point reconstruction from cell means using WENO-JS/Z power-two weights and actual periodic scalar transport. Separate epsilon choices, analytic cell means versus point values, and spatial error versus time-step effects. p+1 Gauss solution points, upwind interface flux, Legendre Radau corrections and SSPRK(3,3). Match initial L2 projection, upwind flux and timestep policy to the unchanged published modal DG. Scaled Courant(2p+1)|a|dt/h<=.15; separately halve the timestep at p2/N32.

## Equations

- [Linear advection](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#linear-advection-en>)

  Transport at constant speed a: translation, numerical diffusion and stability. Representative equations related to this problem. See the image/problem conditions and each execution example for initial conditions, boundary conditions and parameters.
- [Linear advection](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#linear-advection-en>)

  Transport at constant speed a: translation, numerical diffusion and stability.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#execution-advection-sine-en>)

  First-order upwind plus forward Euler, input CFL=0.5. The reference is continuous-PDE translation, not the discrete amplification factor.

## Problem figures

- [Periodic sine-wave advection](<https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/advection-sine.png

## Exact / reference solutions

- [Periodic sine-wave advection — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=en#references-en>)

  Analytic translation of a periodic sine is the standard. The problem merges different amplitudes and representations; the reference-library amplitude 0.25 is not the input for every execution example. Integrate continuous L2 error at additional Gauss points and compare final polynomials with the actual published DG at common points. Check weighted mass at every RK stage and quadratic energy at each completed step. A matrix exponential of the same FR operator separately measures RK3 time error and its timestep-halving response.
- [Advection / sine translation](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-sine-advection-en>)
  relation: related-model
  reference_kind: analytic

  Analytic reference Periodic unit interval; constant advection speed 1. Same periodic sine-transport model at speed one. The library amplitude is 0.25 versus 0.2 in the common fixed input; DG/CIP representations and output times also differ.
- [WENO critical points: polynomial cell means and analytic periodic transport](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-weno-critical-profile-en>)
  relation: related-model
  reference_kind: analytic

  Analytic reference Local references integrate polynomials over five cells centered around x=0 and evaluate at h/2. Regular, first-critical and second-critical profiles use h=1/64…1/512. The actual periodic-transport reference is the Fourier-integrated cell mean of q₀=cos(2πx)+.1sin³(2πx) on[0,1], speed1,T1, checked independently by Gauss12 point-function quadrature. Local polynomials differ from the evolved profile; neither point samples nor another PDE calculation are substituted for cell means. An additional constant-speed periodic-transport reference. The cos+.1sin³ cell means and local critical polynomials differ from the historical single-sine/CIP display.
- [FR/DG periodic sine advection: analytic reference at mean0.4 andT=.25](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-fr-periodic-advection-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference Dimensionless u_t+u_x=0 on[0,1), periodic boundary, initial0.4+sin(2pi x), analytic0.4+sin(2pi(x-t)). Constant positive speed1 and uniform affine intervals. Dimensionless u_t+u_x=0 on[0,1), periodic boundary, initial0.4+sin(2pi x), analytic0.4+sin(2pi(x-t)). Constant positive speed1 and uniform affine intervals.
- [Periodic sine advection: upwind and analytic transport — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/advection-sine/?lang=en#advection-sine-en-validation>)

  CSV contains one row per fine-grid center, with the analytic reference evaluated at exactly the same time and location. Periodic-mean and maximum-principle checks allow 10^-12 for roundoff.
- [Advection / sine translation](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-sine-advection-en>)
  relation: related-model
  reference_kind: analytic

  Analytic reference Periodic unit interval; constant advection speed 1. Same periodic sine-transport model at speed one. The library amplitude is 0.25 versus 0.2 in the common fixed input; DG/CIP representations and output times also differ.
- [WENO critical points: polynomial cell means and analytic periodic transport](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-weno-critical-profile-en>)
  relation: related-model
  reference_kind: analytic

  Analytic reference Local references integrate polynomials over five cells centered around x=0 and evaluate at h/2. Regular, first-critical and second-critical profiles use h=1/64…1/512. The actual periodic-transport reference is the Fourier-integrated cell mean of q₀=cos(2πx)+.1sin³(2πx) on[0,1], speed1,T1, checked independently by Gauss12 point-function quadrature. Local polynomials differ from the evolved profile; neither point samples nor another PDE calculation are substituted for cell means. An additional constant-speed periodic-transport reference. The cos+.1sin³ cell means and local critical polynomials differ from the historical single-sine/CIP display.
- [FR/DG periodic sine advection: analytic reference at mean0.4 andT=.25](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-fr-periodic-advection-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference Dimensionless u_t+u_x=0 on[0,1), periodic boundary, initial0.4+sin(2pi x), analytic0.4+sin(2pi(x-t)). Constant positive speed1 and uniform affine intervals. Dimensionless u_t+u_x=0 on[0,1), periodic boundary, initial0.4+sin(2pi x), analytic0.4+sin(2pi(x-t)). Constant positive speed1 and uniform affine intervals.

## Code and validation

- [Reaction-diffusion: separate second-order space and fourth-order time](<https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-fourier/?lang=en>)
  availability: run

  Validate a small linear diffusion-reaction operator against continuous and semidiscrete Fourier solutions.
- [Turing instability: linear growth and small-amplitude patterns](<https://hrkoyama.github.io/numerical-methods-atlas/validation/turing-schnakenberg/?lang=en>)
  availability: run

  Use a matrix exponential to validate stable homogeneous kinetics and diffusion-driven growth of a selected Schnakenberg mode.
- [Finite-amplitude Schnakenberg transient: nonlinearity and independent reference](<https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-nonlinear/?lang=en>)
  availability: run

  Validate a finite-amplitude reaction-diffusion transient to t=8 with an independent Fourier–Galerkin reference, grid/time convergence and newly generated harmonics.
- [Near-saturated Schnakenberg pattern: near-stationarity and grid/time convergence](<https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-pattern/?lang=en>)
  availability: run

  Compare the selected1D pattern at t=100 with an independent reference. Separate reference90→100 change/full-PDE residual from the finite-step primary FD residual.
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
- [Pure Neumann compatibility and mean gauge](<https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-neumann/?lang=en>)
  availability: run

  Solve singular2D Poisson with compatibility/gauge and reject incompatible source.
- [2D mixed Robin MMS and boundary flux](<https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-robin/?lang=en>)
  availability: run

  Assemble actual2D Neumann/Robin faces and compare the manufactured field and boundary flux.
- [Actual2D C-grid rotating shallow-water time advance](<https://hrkoyama.github.io/numerical-methods-atlas/validation/cgrid-rotating-wave/?lang=en>)
  availability: run

  Time-advance actual2D staggered fields and distinguish continuous-wave references from semidiscrete symbols.
- [Crossing the Bratu fold with pseudo-arclength continuation](<https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-continuation/?lang=en>)
  availability: run

  Follow the lower and upper branches of the same one-dimensional Bratu boundary-value problem; check tangents, the fold and spatial error against an independent analytic family.
- [Jacobian-free Newton–Krylov with analytic, central-FD and directional-AD products](<https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-matrix-free-jfnk/?lang=en>)
  availability: run

  Solve both Bratu branches with three Jv choices without assembling the nonlinear Jacobian; retain forcing, actual residuals and evaluation counts.
- [Bratu sensitivity near the discrete fold](<https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-sensitivity/?lang=en>)
  availability: run

  At six fixed points approaching the discrete Bratu fold, separate state error from linear-solve tolerance and compare against independent shooting gradients.
- [Matrix-free VJP for distributed Bratu coefficients](<https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-distributed-vjp/?lang=en>)
  availability: run

  Represent8/16/32 spatial controls with two local hat weights per node; compare objective-wise adjoint VJPs with a separate full-sensitivity reference.
- [Periodic sine advection: upwind and analytic transport](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/advection-sine/?lang=en>)
  availability: run

  Advance q_t+a q_x=0 for one period on a unit periodic interval. Compare first-order upwind on 64/128 points with an analytically translated sine, exporting computed, analytic and error values.
- [Zalesak-type 2D rotation: conservation, bounds and shape error](<https://hrkoyama.github.io/numerical-methods-atlas/validation/zalesak-rotation/?lang=en>)
  availability: run

  Rotate a slotted disk through one full turn with an actual 2D finite-volume solver, comparing donor-cell and minmod MUSCL. Eight runs combine three grids with half-cell-center and 45-degree-start probes; measure conservation, bounds at every SSP stage, shape error and slot filling.
- [ALE scalar transport on genuinely nonuniform moving cells](<https://hrkoyama.github.io/numerical-methods-atlas/validation/ale-nonuniform-transport/?lang=en>)
  availability: run

  Advance cell integrals and face positions with identical Heun stages, transporting a nonuniform analytic wave beyond a uniform GCL check.
- [Isotropic scattering in a finite slab](<https://hrkoyama.github.io/numerical-methods-atlas/validation/isotropic-scattering-slab/?lang=en>)
  availability: run

  Solve genuinely coupled signed-angle steady transport and compare R/T/A with an independent continuum-angle Fredholm reference.
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
- [WENO-JS/Z: fixed critical-point and epsilon comparison](<https://hrkoyama.github.io/numerical-methods-atlas/validation/weno-critical-epsilon/?lang=en>)
  availability: run

  Compare WENO5 JS and Z power-two weights from the same cell means, then evolve actual periodic transport. Retain three regularity classes, three epsilon choices, fixed grids and separate halved-time-step diagnostics.
- [1D periodic FR advection: Radau correction and published DG comparison](<https://hrkoyama.github.io/numerical-methods-atlas/validation/fr-periodic-advection/?lang=en>)
  availability: run

  Transport0.4+sin(2pi x) toT=.25. Execute Gauss-node/Radau FR and the existing modal DG for p=1/2 and8/16/32 cells; measure analytic error, mass and time-integration error.
- [Forward spatial difference — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/forward-difference/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [Backward spatial difference — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/backward-difference/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [Centered spatial difference — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [Upwind finite differences — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/upwind/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [Lax–Friedrichs — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/lax-friedrichs/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [Lax–Wendroff — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/lax-wendroff/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
