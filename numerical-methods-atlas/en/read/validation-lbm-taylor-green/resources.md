# LBM Taylor–Green vortex and finite-Mach errors

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-lbm-taylor-green/

Resources explicitly registered to the methods, problems and executions of this chapter. Use the exact periodic vortex to examine coupled grid/time/Mach errors and amplitude effects.

## Methods

- [D2Q9–BGK collision and streaming](<https://hrkoyama.github.io/numerical-methods-atlas/methods/d2q9-bgk/?lang=en>)

## Equations

- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-taylor-green/?lang=en#lbm-taylor-green-en-algorithm>)

  Standard BGK and fully periodic streaming. Convert/gauge pressure ascs²(rho−meanrho)(dx/dt)². No analytic field injection after initialization; independently qualify the continuum field by Fourier differentiation.
- [Isothermal lattice BGK](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bgk-en>)

  Collision/streaming in lattice units Δx=Δt=1. Examples cover D2Q9 isothermal low-Mach shear waves and Poiseuille flow.
- [Incompressible Navier–Stokes](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#navier-stokes-en>)

  Representative constant-density/viscosity flow. In addition to periodic2D MAC projection/Taylor–Green, a separate release verifies a pressure-eliminated nonperiodic Re100 cavity.

## Problem figures

- [LBM Taylor–Green vortex: coupled grid/time/Mach sensitivity](<https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/results/lbm-taylor-green.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/results/lbm-taylor-green.png
- [Periodic Taylor–Green vortex](<https://hrkoyama.github.io/numerical-methods-atlas/problems/taylor-green/?lang=en>)

  Use the exact periodic vortex to examine coupled grid/time/Mach errors and amplitude effects. Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/numerical-methods-atlas/assets/field-taylor-green.png

## Exact / reference solutions

- [LBM Taylor–Green vortex: coupled grid/time/Mach sensitivity](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-lbm-taylor-green-en>)
  reference_kind: analytic

  Analytic reference Periodic[0,2pi)²,nu.1,baseU.2,N24/32/64,dt=.2dx²,tau.56,T=.2pi²and144/256/1024steps. Add N32/U.4,.8andN32/U.2/dt=.1dx²/tau.53/512steps. Use pressure-consistent initial density.
- [LBM Taylor–Green vortex: coupled grid/time/Mach sensitivity — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-taylor-green/?lang=en#lbm-taylor-green-en-validation>)

  22pytest and79gates,sixfixed evolutions. Require finest velocity relativeL2.03,pressure.08,combined velocity order≥1.5,energy.03anddivergence/periodic mass/mean momentum. Save five analyticPDEqualifiers distinctly. Retain the initial N16energy failure5.0018%; refine only thatcoarsegrid to24against the unchanged3%gate. Report order only for thefinest32/64pair.
- [Viscous flow / 2D Taylor–Green](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-taylor-green-en>)
  relation: related-model
  reference_kind: analytic

  Analytic reference Periodic [0,2π]²; unit density; viscosity 0.1; zero mean pressure. Web profile is an x-slice at y=π/4. Taylor–Green: x-slice at y = π/4. These are point values, not two-dimensional cell averages. The analytic model shares ν=0.1 and periodic [0,2π]², but the card displays an x-slice at y=π/4, not full 2D velocity/pressure or mesh-error arrays.
- [LBM Taylor–Green vortex: coupled grid/time/Mach sensitivity](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-lbm-taylor-green-en>)
  relation: related-model
  reference_kind: analytic

  Analytic reference Periodic[0,2pi)²,nu.1,baseU.2,N24/32/64,dt=.2dx²,tau.56,T=.2pi²and144/256/1024steps. Add N32/U.4,.8andN32/U.2/dt=.1dx²/tau.53/512steps. Use pressure-consistent initial density. Periodic[0,2pi)²,nu.1,baseU.2,N24/32/64,dt=.2dx²,tau.56,T=.2pi²and144/256/1024steps. Add N32/U.4,.8andN32/U.2/dt=.1dx²/tau.53/512steps. Use pressure-consistent initial density.
- [Periodic Taylor–Green vortex — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/taylor-green/?lang=en#references-en>)

  Use the exact periodic vortex to examine coupled grid/time/Mach errors and amplitude effects. Check analytic 2D periodic Taylor–Green velocity/pressure, viscous decay and discrete divergence. The library display is a y=π/4 slice rather than the full 2D computed field.
- [Viscous flow / 2D Taylor–Green](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-taylor-green-en>)
  relation: related-model
  reference_kind: analytic

  Use the exact periodic vortex to examine coupled grid/time/Mach errors and amplitude effects. Analytic reference Periodic [0,2π]²; unit density; viscosity 0.1; zero mean pressure. Web profile is an x-slice at y=π/4. Taylor–Green: x-slice at y = π/4. These are point values, not two-dimensional cell averages. The analytic model shares ν=0.1 and periodic [0,2π]², but the card displays an x-slice at y=π/4, not full 2D velocity/pressure or mesh-error arrays.
- [LBM Taylor–Green vortex: coupled grid/time/Mach sensitivity](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-lbm-taylor-green-en>)
  relation: related-model
  reference_kind: analytic

  Use the exact periodic vortex to examine coupled grid/time/Mach errors and amplitude effects. Analytic reference Periodic[0,2pi)²,nu.1,baseU.2,N24/32/64,dt=.2dx²,tau.56,T=.2pi²and144/256/1024steps. Add N32/U.4,.8andN32/U.2/dt=.1dx²/tau.53/512steps. Use pressure-consistent initial density. Periodic[0,2pi)²,nu.1,baseU.2,N24/32/64,dt=.2dx²,tau.56,T=.2pi²and144/256/1024steps. Add N32/U.4,.8andN32/U.2/dt=.1dx²/tau.53/512steps. Use pressure-consistent initial density.

## Code and validation

- [LBM Taylor–Green vortex: coupled grid/time/Mach sensitivity](<https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-taylor-green/?lang=en>)
  availability: run

  Evolve a nonlinear periodic2D vortex and save velocity/pressure/energy errors against the continuous analytic field. Distinguish amplitude probes from a fixed-grid coupled-step probe.
