# LBM lid-driven cavity at Re100

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-lbm-cavity/

Resources explicitly registered to the methods, problems and executions of this chapter. Advance a four-wall Re100 LBM flow and compare Ghia centerlines and the primary vortex, recording wall momentum exchange.

## Methods

- [D2Q9–BGK collision and streaming](<https://hrkoyama.github.io/numerical-methods-atlas/methods/d2q9-bgk/?lang=en>)

## Equations

- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-cavity-re100/?lang=en#lbm-cavity-re100-en-algorithm>)

  Standard D2Q9equilibrium/BGK collision, nonperiodic link streaming and moving halfway reflection atq=.5. Sum actual population wall impulses without density repair/interior reset. Compile shipped C++17temporarily and call fromPython.
- [Isothermal lattice BGK](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bgk-en>)

  Collision/streaming in lattice units Δx=Δt=1. Examples cover D2Q9 isothermal low-Mach shear waves and Poiseuille flow.
- [Incompressible Navier–Stokes](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#navier-stokes-en>)

  Representative constant-density/viscosity flow. In addition to periodic2D MAC projection/Taylor–Green, a separate release verifies a pressure-eliminated nonperiodic Re100 cavity.

## Problem figures

- [LBM Re100 cavity: actual2D fields and Ghia centerlines](<https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/results/lbm-cavity-re100.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/results/lbm-cavity-re100.png
- [Re100 lid-driven cavity](<https://hrkoyama.github.io/numerical-methods-atlas/problems/lid-driven-cavity/?lang=en>)

  Advance a four-wall Re100 LBM flow and compare Ghia centerlines and the primary vortex, recording wall momentum exchange. Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/results/cavity-ghia-re100-preview.png

## Exact / reference solutions

- [LBM Re100 cavity: actual2D fields and Ghia centerlines](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-lbm-cavity-re100-en>)
  reference_kind: numerical-reference

  Finite-grid numerical reference Physical unit square, lid1, viscosity.01, Re100; N24/32/48, lattice lid.04, dt=.04/N. Three stationary walls/rightward lid; stationary side owns a simultaneous top/side link. Initialrho1/rest.
- [LBM Re100 cavity: actual2D fields and Ghia centerlines — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-cavity-re100/?lang=en#lbm-cavity-re100-en-validation>)

  22pytest and37case gates. Fixed60k/80k/120ksteps reach t*=100with90/95/100saved. Finest u/v max error.03,vortex distance.06,late relativeL2 change2e-4andmass/wall-inclusive momentum gates are frozen.
- [Ghia Re100: original finite-grid velocity centerlines](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-ghia-re100-en>)
  relation: same-problem
  reference_kind: numerical-reference

  Finite-grid numerical reference Unit square,Re100,unit top lid and stationary other walls. Transcribe17points each of u(.5,y) and v(x,.5) after direct inspection of original TablesI/II Re100 columns, preserving printed four-decimal coordinates. Separately compare the grid primary vortex(.6172,.7344) from TableV. These rounded finite-grid numerical tables are neither continuum exact values nor outputs from the present solver. Educational Re100 checks on three fixed grids. Lid/sidewall corner velocities are discontinuous; stationary corners take precedence. Ghia values are rounded numerical references, not an exact solution, and printed four-decimal coordinates are preserved. No high-Re, turbulence, original-algorithm reproduction or cavity-pressure validation is claimed.
- [LBM Re100 cavity: actual2D fields and Ghia centerlines](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-lbm-cavity-re100-en>)
  relation: related-model
  reference_kind: numerical-reference

  Finite-grid numerical reference Physical unit square, lid1, viscosity.01, Re100; N24/32/48, lattice lid.04, dt=.04/N. Three stationary walls/rightward lid; stationary side owns a simultaneous top/side link. Initialrho1/rest. Physical unit square, lid1, viscosity.01, Re100; N24/32/48, lattice lid.04, dt=.04/N. Three stationary walls/rightward lid; stationary side owns a simultaneous top/side link. Initialrho1/rest.
- [Re100 lid-driven cavity — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/lid-driven-cavity/?lang=en#references-en>)

  Advance a four-wall Re100 LBM flow and compare Ghia centerlines and the primary vortex, recording wall momentum exchange. Freeze21 pytest checks and94group gates. Linearly interpolate to17points per velocity transcribed after direct visual reading of original TablesI/II, printed398–399. Require finest component maximum errors≤.03, refinement decrease and steady residual≤1e−7. Also check primary-vortex grid location from TableV, wall values, Poisson residual and discrete divergence.
- [Ghia Re100: original finite-grid velocity centerlines](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-ghia-re100-en>)
  relation: same-problem
  reference_kind: numerical-reference

  Advance a four-wall Re100 LBM flow and compare Ghia centerlines and the primary vortex, recording wall momentum exchange. Finite-grid numerical reference Unit square,Re100,unit top lid and stationary other walls. Transcribe17points each of u(.5,y) and v(x,.5) after direct inspection of original TablesI/II Re100 columns, preserving printed four-decimal coordinates. Separately compare the grid primary vortex(.6172,.7344) from TableV. These rounded finite-grid numerical tables are neither continuum exact values nor outputs from the present solver. Educational Re100 checks on three fixed grids. Lid/sidewall corner velocities are discontinuous; stationary corners take precedence. Ghia values are rounded numerical references, not an exact solution, and printed four-decimal coordinates are preserved. No high-Re, turbulence, original-algorithm reproduction or cavity-pressure validation is claimed.
- [LBM Re100 cavity: actual2D fields and Ghia centerlines](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-lbm-cavity-re100-en>)
  relation: related-model
  reference_kind: numerical-reference

  Advance a four-wall Re100 LBM flow and compare Ghia centerlines and the primary vortex, recording wall momentum exchange. Finite-grid numerical reference Physical unit square, lid1, viscosity.01, Re100; N24/32/48, lattice lid.04, dt=.04/N. Three stationary walls/rightward lid; stationary side owns a simultaneous top/side link. Initialrho1/rest. Physical unit square, lid1, viscosity.01, Re100; N24/32/48, lattice lid.04, dt=.04/N. Three stationary walls/rightward lid; stationary side owns a simultaneous top/side link. Initialrho1/rest.

## Code and validation

- [LBM Re100 cavity: actual2D fields and Ghia centerlines](<https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-cavity-re100/?lang=en>)
  availability: run

  Advance genuine four-wall BGK flow on three fixed grids, checking nominal-lid Ghia centerlines, primary vortex, stationarity and wall momentum budgets.
