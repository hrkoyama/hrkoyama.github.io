# Annular Couette control for curved-wall LBM

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-lbm-annulus/

Resources explicitly registered to the methods, problems and executions of this chapter. Refine the grid at identical physical conditions and compare interpolated/stair walls with analytic velocity,pointwise pressure and torque.

## Methods

- [D2Q9–BGK collision and streaming](<https://hrkoyama.github.io/numerical-methods-atlas/methods/d2q9-bgk/?lang=en>)

  Three-point quadratic interpolation on the reflected characteristic: twointerior outgoing samples forq<.5,oneinterior incoming sample forq>.5,exacthalfway atq=.5. Record movingwall correction,actual force/torque andnonzero wallmass; nofloor ormassrepair.
- [D2Q9–BGK collision and streaming](<https://hrkoyama.github.io/numerical-methods-atlas/methods/d2q9-bgk/?lang=en>)

## Equations

- [Isothermal lattice BGK](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bgk-en>)

  Collision/streaming in lattice units Δx=Δt=1. Examples cover D2Q9 isothermal low-Mach shear waves and Poiseuille flow. Rin.2/Rout.4,center(.5,.5),inner tangential speed.02,stationary outerwall,nu.01. N80/160/240,tau.7,T4,integer3840/15360/34560steps; both boundaries give sixruns. Initialize equilibrium moments of the analytic field.
- [Incompressible Navier–Stokes](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#navier-stokes-en>)

  Representative constant-density/viscosity flow. In addition to periodic2D MAC projection/Taylor–Green, a separate release verifies a pressure-eliminated nonperiodic Re100 cavity. Rin.2/Rout.4,center(.5,.5),inner tangential speed.02,stationary outerwall,nu.01. N80/160/240,tau.7,T4,integer3840/15360/34560steps; both boundaries give sixruns. Initialize equilibrium moments of the analytic field.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-annular-couette-control/?lang=en#lbm-annular-couette-control-en-algorithm>)

  Three-point quadratic interpolation on the reflected characteristic: twointerior outgoing samples forq<.5,oneinterior incoming sample forq>.5,exacthalfway atq=.5. Record movingwall correction,actual force/torque andnonzero wallmass; nofloor ormassrepair.
- [Isothermal lattice BGK](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bgk-en>)

  Collision/streaming in lattice units Δx=Δt=1. Examples cover D2Q9 isothermal low-Mach shear waves and Poiseuille flow.
- [Incompressible Navier–Stokes](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#navier-stokes-en>)

  Representative constant-density/viscosity flow. In addition to periodic2D MAC projection/Taylor–Green, a separate release verifies a pressure-eliminated nonperiodic Re100 cavity.

## Problem figures

- [Curved LBM annular Couette control: velocity,pressure andtorque](<https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-annular-couette-control/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/results/lbm-annular-couette-control-preview.png
- [Curved LBM annular Couette control: velocity,pressure andtorque](<https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/results/lbm-annular-couette-control.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/results/lbm-annular-couette-control.png

## Exact / reference solutions

- [Curved LBM annular Couette control: velocity,pressure andtorque — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-annular-couette-control/?lang=en#references-en>)

  Group28pytest;80annular gates. Sevenindependent radial/Cartesian qualifiers,finest velocity.03,fullpointwise pressure-gauge.08,torque relative.05,stationarity/refinement/stair comparison andwallinclusive budgets. Separate87component qualifiers passed; this doesnot imply main success. Separate29newmeshcomponentqualifierspassed.
- [Curved LBM annular Couette control: velocity,pressure andtorque](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-lbm-annular-couette-control-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference Rin.2/Rout.4,center(.5,.5),inner tangential speed.02,stationary outerwall,nu.01. N80/160/240,tau.7,T4,integer3840/15360/34560steps; both boundaries give sixruns. Initialize equilibrium moments of the analytic field. Fixedcircles andslowrotation only. Negative quadratic coefficients preclude a general positivity/stability guarantee; report actual interpolation massnonconservation. Prior linear attemptfailed pressure.617757>.08 andisretained; no radial-average substitution. No changing-solid topology orsubstitute forcylinderflow. Retain the failedquadraticN80pressure.352758>.08;refinebothboundariesatfixedUi/tau/T.
- [Curved LBM annular Couette control: velocity,pressure andtorque](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-lbm-annular-couette-control-en>)
  reference_kind: analytic

  Analytic reference Rin.2/Rout.4,center(.5,.5),inner tangential speed.02,stationary outerwall,nu.01. N80/160/240,tau.7,T4,integer3840/15360/34560steps; both boundaries give sixruns. Initialize equilibrium moments of the analytic field.
- [Curved LBM annular Couette control: velocity,pressure andtorque — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-annular-couette-control/?lang=en#lbm-annular-couette-control-en-validation>)

  Group28pytest;80annular gates. Sevenindependent radial/Cartesian qualifiers,finest velocity.03,fullpointwise pressure-gauge.08,torque relative.05,stationarity/refinement/stair comparison andwallinclusive budgets. Separate87component qualifiers passed; this doesnot imply main success. Separate29newmeshcomponentqualifierspassed.
- [Curved LBM annular Couette control: velocity,pressure andtorque](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-lbm-annular-couette-control-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference Rin.2/Rout.4,center(.5,.5),inner tangential speed.02,stationary outerwall,nu.01. N80/160/240,tau.7,T4,integer3840/15360/34560steps; both boundaries give sixruns. Initialize equilibrium moments of the analytic field. Fixedcircles andslowrotation only. Negative quadratic coefficients preclude a general positivity/stability guarantee; report actual interpolation massnonconservation. Prior linear attemptfailed pressure.617757>.08 andisretained; no radial-average substitution. No changing-solid topology orsubstitute forcylinderflow. Retain the failedquadraticN80pressure.352758>.08;refinebothboundariesatfixedUi/tau/T.

## Code and validation

- [Curved LBM annular Couette control: velocity,pressure andtorque](<https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-annular-couette-control/?lang=en>)
  availability: run

  Compare true-circle quadratic Lagrange link interpolation andstair halfway against analytic rotating-inner-wall Navier–Stokes flow; anadditional control distinct fromcylinderwake.
