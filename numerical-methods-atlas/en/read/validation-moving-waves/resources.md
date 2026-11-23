# Nonuniform ALE transport and2D rotating shallow-water waves

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-moving-waves/

Resources explicitly registered to the methods, problems and executions of this chapter. Time-advance conservative ALE transport on genuinely nonuniform moving cells with GCL, and2D linear rotating C-grid shallow-water waves. Saltzman pistons and global Williamson problems remain future work.

## Methods

- [ALE uniform-state / geometric-conservation model](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ale/?lang=en>)

  Upwind relative flux(a-w)q advances actual masses with identical predictor/corrector face geometry; record stage volumes and Courant numbers.
- [Upwind finite differences](<https://hrkoyama.github.io/numerical-methods-atlas/methods/upwind/?lang=en>)

  Upwind relative flux(a-w)q advances actual masses with identical predictor/corrector face geometry; record stage volumes and Courant numbers.
- [Heun / SSPRK(2,2)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en>)

  Upwind relative flux(a-w)q advances actual masses with identical predictor/corrector face geometry; record stage volumes and Courant numbers.
- [Centered spatial difference](<https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en>)

  Actual2D cell-height/face-velocity differences and four-point Coriolis interpolation use RK4. The3×3 matrix exponential is reference-only, never the PDE update.
- [Classical RK4](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=en>)

  Actual2D cell-height/face-velocity differences and four-point Coriolis interpolation use RK4. The3×3 matrix exponential is reference-only, never the PDE update.
- [ALE uniform-state / geometric-conservation model](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ale/?lang=en>)
- [Upwind finite differences](<https://hrkoyama.github.io/numerical-methods-atlas/methods/upwind/?lang=en>)
- [Heun / SSPRK(2,2)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en>)
- [Centered spatial difference](<https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en>)
- [Classical RK4](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=en>)

## Equations

- [ALE scalar conservation on moving cells](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#ale-scalar-transport-en>)

  Prescribed nonuniform face positions and cell masses share Heun stages. Evaluate geometric conservation and nonuniform-wave transport separately; this is not an Euler-fluid Lagrange/remap scheme. Periodic unit interval, speed.7,q0=1+.2sin(2pi x), grid speed .2sin(2pi xi)cos(2pi t),N40/80/160,T1. Separate N40,T.25 time series32/64/128steps.
- [Linear rotating shallow-water equations](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#linear-rotating-shallow-water-en>)

  Actual2D staggered C-grid fields use RK4 on a planar linear f-plane. Separate continuous and semidiscrete references, checking mass,energy,inertial oscillation and discrete geostrophic balance. Linear f-plane,g=H=f=1, periodic unit square, mode(1,2),height amplitude.01,N16/32/64,T.5. Separate N16 time refinement, zero-mode and discrete geostrophic probes.
- [ALE scalar conservation on moving cells](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#ale-scalar-transport-en>)

  Prescribed nonuniform face positions and cell masses share Heun stages. Evaluate geometric conservation and nonuniform-wave transport separately; this is not an Euler-fluid Lagrange/remap scheme.
- [Linear rotating shallow-water equations](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#linear-rotating-shallow-water-en>)

  Actual2D staggered C-grid fields use RK4 on a planar linear f-plane. Separate continuous and semidiscrete references, checking mass,energy,inertial oscillation and discrete geostrophic balance.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/ale-nonuniform-transport/?lang=en#ale-nonuniform-transport-en-algorithm>)

  Upwind relative flux(a-w)q advances actual masses with identical predictor/corrector face geometry; record stage volumes and Courant numbers.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/cgrid-rotating-wave/?lang=en#cgrid-rotating-wave-en-algorithm>)

  Actual2D cell-height/face-velocity differences and four-point Coriolis interpolation use RK4. The3×3 matrix exponential is reference-only, never the PDE update.

## Problem figures

- [ALE scalar transport on genuinely nonuniform moving cells](<https://hrkoyama.github.io/numerical-methods-atlas/problems/ale-nonuniform-transport/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/results/ale-nonuniform-transport-preview.png
- [Actual2D C-grid rotating shallow-water time advance](<https://hrkoyama.github.io/numerical-methods-atlas/problems/cgrid-rotating-wave/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/results/cgrid-rotating-wave-preview.png
- [ALE scalar transport on genuinely nonuniform moving cells](<https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/results/ale-nonuniform-transport.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/results/ale-nonuniform-transport.png
- [Actual2D C-grid rotating shallow-water time advance](<https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/results/cgrid-rotating-wave.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/results/cgrid-rotating-wave.png

## Exact / reference solutions

- [ALE scalar transport on genuinely nonuniform moving cells — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/ale-nonuniform-transport/?lang=en#references-en>)

  Separate analytic moving-cell-integral error, global/stage mass, constant GCL and geometry error. Qualify an independent DOP853 integration of the same FV ODE with two tolerances.
- [ALE: analytic moving-cell integrals and separate time reference](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-ale-nonuniform-transport-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference Periodic unit interval, speed.7,q0=1+.2sin(2pi x), grid speed .2sin(2pi xi)cos(2pi t),N40/80/160,T1. Separate N40,T.25 time series32/64/128steps. Integrate q(x,t)=1+.2sin[2pi(x-.7t)] between the actual saved primary faces. Separately record geometry error against analytic face positions. Time checks use independent DOP853 at two tolerances for the same FV ODE. First-stage1D prescribed mesh motion. The x–t image is not2D physics; Euler Lagrange/remap and Saltzman piston remain future work.
- [Actual2D C-grid rotating shallow-water time advance — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/cgrid-rotating-wave/?lang=en#references-en>)

  Retain continuous-PDE spatial and discrete-symbol temporal errors, mass/energy, stencil-symbol identity, zero-mode inertia and discrete steady balance.
- [C-grid: continuous Fourier solution and discrete-symbol exponential](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-cgrid-rotating-wave-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference Linear f-plane,g=H=f=1, periodic unit square, mode(1,2),height amplitude.01,N16/32/64,T.5. Separate N16 time refinement, zero-mode and discrete geostrophic probes. Evolve eta0=.01cos[2pi(x+2y)],u0=v0=0 with separate continuous3x3 Fourier-operator and discrete3x3-symbol exponentials. The primary actually advances2D staggered fields. Linear planar periodic square only. Nonlinear SWE,PV,spherical dynamics and Williamson tests remain future work.
- [ALE: analytic moving-cell integrals and separate time reference](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-ale-nonuniform-transport-en>)
  reference_kind: analytic

  Analytic reference Periodic unit interval, speed.7,q0=1+.2sin(2pi x), grid speed .2sin(2pi xi)cos(2pi t),N40/80/160,T1. Separate N40,T.25 time series32/64/128steps. Integrate q(x,t)=1+.2sin[2pi(x-.7t)] between the actual saved primary faces. Separately record geometry error against analytic face positions. Time checks use independent DOP853 at two tolerances for the same FV ODE.
- [C-grid: continuous Fourier solution and discrete-symbol exponential](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-cgrid-rotating-wave-en>)
  reference_kind: analytic

  Analytic reference Linear f-plane,g=H=f=1, periodic unit square, mode(1,2),height amplitude.01,N16/32/64,T.5. Separate N16 time refinement, zero-mode and discrete geostrophic probes. Evolve eta0=.01cos[2pi(x+2y)],u0=v0=0 with separate continuous3x3 Fourier-operator and discrete3x3-symbol exponentials. The primary actually advances2D staggered fields.
- [ALE scalar transport on genuinely nonuniform moving cells — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/ale-nonuniform-transport/?lang=en#ale-nonuniform-transport-en-validation>)

  Separate analytic moving-cell-integral error, global/stage mass, constant GCL and geometry error. Qualify an independent DOP853 integration of the same FV ODE with two tolerances.
- [ALE: analytic moving-cell integrals and separate time reference](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-ale-nonuniform-transport-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference Periodic unit interval, speed.7,q0=1+.2sin(2pi x), grid speed .2sin(2pi xi)cos(2pi t),N40/80/160,T1. Separate N40,T.25 time series32/64/128steps. Integrate q(x,t)=1+.2sin[2pi(x-.7t)] between the actual saved primary faces. Separately record geometry error against analytic face positions. Time checks use independent DOP853 at two tolerances for the same FV ODE. First-stage1D prescribed mesh motion. The x–t image is not2D physics; Euler Lagrange/remap and Saltzman piston remain future work.
- [Actual2D C-grid rotating shallow-water time advance — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/cgrid-rotating-wave/?lang=en#cgrid-rotating-wave-en-validation>)

  Retain continuous-PDE spatial and discrete-symbol temporal errors, mass/energy, stencil-symbol identity, zero-mode inertia and discrete steady balance.
- [C-grid: continuous Fourier solution and discrete-symbol exponential](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-cgrid-rotating-wave-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference Linear f-plane,g=H=f=1, periodic unit square, mode(1,2),height amplitude.01,N16/32/64,T.5. Separate N16 time refinement, zero-mode and discrete geostrophic probes. Evolve eta0=.01cos[2pi(x+2y)],u0=v0=0 with separate continuous3x3 Fourier-operator and discrete3x3-symbol exponentials. The primary actually advances2D staggered fields. Linear planar periodic square only. Nonlinear SWE,PV,spherical dynamics and Williamson tests remain future work.

## Code and validation

- [ALE scalar transport on genuinely nonuniform moving cells](<https://hrkoyama.github.io/numerical-methods-atlas/validation/ale-nonuniform-transport/?lang=en>)
  availability: run

  Advance cell integrals and face positions with identical Heun stages, transporting a nonuniform analytic wave beyond a uniform GCL check.
- [Actual2D C-grid rotating shallow-water time advance](<https://hrkoyama.github.io/numerical-methods-atlas/validation/cgrid-rotating-wave/?lang=en>)
  availability: run

  Time-advance actual2D staggered fields and distinguish continuous-wave references from semidiscrete symbols.
