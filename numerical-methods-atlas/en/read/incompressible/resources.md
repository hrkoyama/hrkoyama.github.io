# Incompressible flow: project with compatible discrete operators

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/incompressible/

Resources explicitly registered to the methods, problems and executions of this chapter.

## Methods

- [MAC pressure projection](<https://hrkoyama.github.io/numerical-methods-atlas/methods/projection/?lang=en>)
- [MAC pressure projection](<https://hrkoyama.github.io/numerical-methods-atlas/methods/projection/?lang=en>)

  Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions.
- [D2Q9–BGK collision and streaming](<https://hrkoyama.github.io/numerical-methods-atlas/methods/d2q9-bgk/?lang=en>)

  Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions.

## Equations

- [Incompressible Navier–Stokes](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#navier-stokes-en>)

  Representative constant-density/viscosity flow. In addition to periodic2D MAC projection/Taylor–Green, a separate release verifies a pressure-eliminated nonperiodic Re100 cavity. Representative equations related to this problem. See the image/problem conditions and each execution example for initial conditions, boundary conditions and parameters.
- [Isothermal lattice BGK](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bgk-en>)

  Collision/streaming in lattice units Δx=Δt=1. Examples cover D2Q9 isothermal low-Mach shear waves and Poiseuille flow. Representative equations related to this problem. See the image/problem conditions and each execution example for initial conditions, boundary conditions and parameters.
- [Incompressible Navier–Stokes](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#navier-stokes-en>)

  Representative constant-density/viscosity flow. In addition to periodic2D MAC projection/Taylor–Green, a separate release verifies a pressure-eliminated nonperiodic Re100 cavity.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#execution-taylor-green-en>)

  Periodic [0,2π)², t=0.5, MAC pressure projection on 16/32/64 grids. Check viscous decay rather than constant energy. Combined space/stable-step refinement is separated from fixed-grid time-step sensitivity.

## Problem figures

- [Periodic Taylor–Green vortex](<https://hrkoyama.github.io/numerical-methods-atlas/problems/taylor-green/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/numerical-methods-atlas/assets/field-taylor-green.png

## Exact / reference solutions

- [Periodic Taylor–Green vortex — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/taylor-green/?lang=en#references-en>)

  Check analytic 2D periodic Taylor–Green velocity/pressure, viscous decay and discrete divergence. The library display is a y=π/4 slice rather than the full 2D computed field.
- [Viscous flow / 2D Taylor–Green](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-taylor-green-en>)
  relation: related-model
  reference_kind: analytic

  Analytic reference Periodic [0,2π]²; unit density; viscosity 0.1; zero mean pressure. Web profile is an x-slice at y=π/4. Taylor–Green: x-slice at y = π/4. These are point values, not two-dimensional cell averages. The analytic model shares ν=0.1 and periodic [0,2π]², but the card displays an x-slice at y=π/4, not full 2D velocity/pressure or mesh-error arrays.
- [LBM Taylor–Green vortex: coupled grid/time/Mach sensitivity](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-lbm-taylor-green-en>)
  relation: related-model
  reference_kind: analytic

  Analytic reference Periodic[0,2pi)²,nu.1,baseU.2,N24/32/64,dt=.2dx²,tau.56,T=.2pi²and144/256/1024steps. Add N32/U.4,.8andN32/U.2/dt=.1dx²/tau.53/512steps. Use pressure-consistent initial density. Periodic[0,2pi)²,nu.1,baseU.2,N24/32/64,dt=.2dx²,tau.56,T=.2pi²and144/256/1024steps. Add N32/U.4,.8andN32/U.2/dt=.1dx²/tau.53/512steps. Use pressure-consistent initial density.
- [Periodic Taylor–Green vortex: velocity, decay and divergence — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/taylor-green/?lang=en#taylor-green-en-validation>)

  CSV uses C-order (i,j) rows with separate coordinates and numerical/analytic values for u faces, v faces and pressure centers; the components are not collocated. JSON includes energy histories and temporal sensitivity.
- [Viscous flow / 2D Taylor–Green](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-taylor-green-en>)
  relation: related-model
  reference_kind: analytic

  Analytic reference Periodic [0,2π]²; unit density; viscosity 0.1; zero mean pressure. Web profile is an x-slice at y=π/4. Taylor–Green: x-slice at y = π/4. These are point values, not two-dimensional cell averages. The analytic model shares ν=0.1 and periodic [0,2π]², but the card displays an x-slice at y=π/4, not full 2D velocity/pressure or mesh-error arrays.
- [LBM Taylor–Green vortex: coupled grid/time/Mach sensitivity](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-lbm-taylor-green-en>)
  relation: related-model
  reference_kind: analytic

  Analytic reference Periodic[0,2pi)²,nu.1,baseU.2,N24/32/64,dt=.2dx²,tau.56,T=.2pi²and144/256/1024steps. Add N32/U.4,.8andN32/U.2/dt=.1dx²/tau.53/512steps. Use pressure-consistent initial density. Periodic[0,2pi)²,nu.1,baseU.2,N24/32/64,dt=.2dx²,tau.56,T=.2pi²and144/256/1024steps. Add N32/U.4,.8andN32/U.2/dt=.1dx²/tau.53/512steps. Use pressure-consistent initial density.

## Code and validation

- [Periodic Taylor–Green vortex: velocity, decay and divergence](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/taylor-green/?lang=en>)
  availability: run

  Use existing two-dimensional MAC projection, centered convection and explicit SSPRK2. Compare analytic decaying vortex on 16²/32²/64² grids and halve CFL on the finest grid.
- [LBM Taylor–Green vortex: coupled grid/time/Mach sensitivity](<https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-taylor-green/?lang=en>)
  availability: run

  Evolve a nonlinear periodic2D vortex and save velocity/pressure/energy errors against the continuous analytic field. Distinguish amplitude probes from a fixed-grid coupled-step probe.
- [MAC pressure projection — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/projection/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
