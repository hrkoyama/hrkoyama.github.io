# Nonperiodic walls: cavity and manufactured flow

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-wall-flow/

Resources explicitly registered to the methods, problems and executions of this chapter.

## Methods

- [Centered spatial difference](<https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en>)

  Advance vorticity transport with centered differences and Heun. Each stage solves−Delta_h psi=omega using a nonperiodic Dirichlet DST, then formsu=psi_y,v=−psi_x. Use local first-order Thom wall vorticity; this is an independent method, not Ghia CSI-MG or its higher-order wall formula.
- [Heun / SSPRK(2,2)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en>)

  Advance vorticity transport with centered differences and Heun. Each stage solves−Delta_h psi=omega using a nonperiodic Dirichlet DST, then formsu=psi_y,v=−psi_x. Use local first-order Thom wall vorticity; this is an independent method, not Ghia CSI-MG or its higher-order wall formula.
- [D2Q9–BGK collision and streaming](<https://hrkoyama.github.io/numerical-methods-atlas/methods/d2q9-bgk/?lang=en>)

  Advance vorticity transport with centered differences and Heun. Each stage solves−Delta_h psi=omega using a nonperiodic Dirichlet DST, then formsu=psi_y,v=−psi_x. Use local first-order Thom wall vorticity; this is an independent method, not Ghia CSI-MG or its higher-order wall formula.
- [Centered spatial difference](<https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en>)

  Use the shared centered FD/Heun/nonperiodic Dirichlet DST solver. Qualify explicit analytic derivatives against independently differentiated tensor coefficients. Separately solve nonzero-Dirichlet Poisson forp=x²+y²+sin(pi*x)sin(pi*y), checking central interior and second-order one-sided boundary gradients.
- [Heun / SSPRK(2,2)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en>)

  Use the shared centered FD/Heun/nonperiodic Dirichlet DST solver. Qualify explicit analytic derivatives against independently differentiated tensor coefficients. Separately solve nonzero-Dirichlet Poisson forp=x²+y²+sin(pi*x)sin(pi*y), checking central interior and second-order one-sided boundary gradients.
- [Centered spatial difference](<https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en>)
- [Heun / SSPRK(2,2)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en>)

## Equations

- [Incompressible Navier–Stokes](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#navier-stokes-en>)

  Representative constant-density/viscosity flow. In addition to periodic2D MAC projection/Taylor–Green, a separate release verifies a pressure-eliminated nonperiodic Re100 cavity. Dimensionless unit square, viscosity.01, lid speed1, Re100. Top interior nodes haveu1; other walls and all four corners have zero velocity. Psi0 on every wall; initial interior vorticity0. Reapply Thom wall vorticity at every Heun stage.
- [Isothermal lattice BGK](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bgk-en>)

  Collision/streaming in lattice units Δx=Δt=1. Examples cover D2Q9 isothermal low-Mach shear waves and Poiseuille flow. Dimensionless unit square, viscosity.01, lid speed1, Re100. Top interior nodes haveu1; other walls and all four corners have zero velocity. Psi0 on every wall; initial interior vorticity0. Reapply Thom wall vorticity at every Heun stage.
- [Forced incompressible flow and wall manufactured solutions](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#forced-incompressible-en>)

  Constant-density-one forced incompressible flow. The actual solver uses the curl forcing in a pressure-eliminated vorticity/streamfunction form. p_op is a separate nonzero-Dirichlet Poisson/gradient manufactured operator problem, not a coupled flow pressure or cavity pressure. Unit square, viscosity.01,17/33/65nodes,psi8f(x)f(y), f(z)=z²(1−z)². All walls are impermeable/no-slip. Derive the curl forcing from the continuous PDE and use the same actual Thom closure as the cavity on every wall; never inject exact wall vorticity.
- [Forced incompressible flow and wall manufactured solutions](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#forced-incompressible-en>)

  Constant-density-one forced incompressible flow. The actual solver uses the curl forcing in a pressure-eliminated vorticity/streamfunction form. p_op is a separate nonzero-Dirichlet Poisson/gradient manufactured operator problem, not a coupled flow pressure or cavity pressure.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/cavity-ghia-re100/?lang=en#cavity-ghia-re100-en-algorithm>)

  Advance vorticity transport with centered differences and Heun. Each stage solves−Delta_h psi=omega using a nonperiodic Dirichlet DST, then forms u=psi_y,v=−psi_x. Use local first-order Thom wall vorticity; this is an independent method, not Ghia CSI-MG or its higher-order wall formula.
- [Incompressible Navier–Stokes](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#navier-stokes-en>)

  Representative constant-density/viscosity flow. In addition to periodic2D MAC projection/Taylor–Green, a separate release verifies a pressure-eliminated nonperiodic Re100 cavity.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/wall-manufactured/?lang=en#wall-manufactured-en-algorithm>)

  Use the shared centered FD/Heun/nonperiodic Dirichlet DST solver. Qualify explicit analytic derivatives against independently differentiated tensor coefficients. Separately solve nonzero-Dirichlet Poisson for p=x²+y²+sin(pi*x)sin(pi*y), checking central interior and second-order one-sided boundary gradients.

## Problem figures

- [Re100 lid-driven cavity](<https://hrkoyama.github.io/numerical-methods-atlas/problems/lid-driven-cavity/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/results/cavity-ghia-re100-preview.png
- [Manufactured incompressible flow with nonperiodic walls](<https://hrkoyama.github.io/numerical-methods-atlas/problems/wall-manufactured/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/results/wall-manufactured-preview.png
- [Re100 lid-driven cavity: Ghia centerline comparison](<https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/results/cavity-ghia-re100.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/results/cavity-ghia-re100.png
- [Nonperiodic wall MMS: velocity, shear and pressure operator](<https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/results/wall-manufactured.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/results/wall-manufactured.png

## Exact / reference solutions

- [Re100 lid-driven cavity — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/lid-driven-cavity/?lang=en#references-en>)

  Freeze21 pytest checks and94group gates. Linearly interpolate to17points per velocity transcribed after direct visual reading of original TablesI/II, printed398–399. Require finest component maximum errors≤.03, refinement decrease and steady residual≤1e−7. Also check primary-vortex grid location from TableV, wall values, Poisson residual and discrete divergence.
- [Ghia Re100: original finite-grid velocity centerlines](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-ghia-re100-en>)
  relation: same-problem
  reference_kind: numerical-reference

  Finite-grid numerical reference Unit square,Re100,unit top lid and stationary other walls. Transcribe17points each of u(.5,y) and v(x,.5) after direct inspection of original TablesI/II Re100 columns, preserving printed four-decimal coordinates. Separately compare the grid primary vortex(.6172,.7344) from TableV. These rounded finite-grid numerical tables are neither continuum exact values nor outputs from the present solver. Educational Re100 checks on three fixed grids. Lid/sidewall corner velocities are discontinuous; stationary corners take precedence. Ghia values are rounded numerical references, not an exact solution, and printed four-decimal coordinates are preserved. No high-Re, turbulence, original-algorithm reproduction or cavity-pressure validation is claimed.
- [LBM Re100 cavity: actual2D fields and Ghia centerlines](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-lbm-cavity-re100-en>)
  relation: related-model
  reference_kind: numerical-reference

  Finite-grid numerical reference Physical unit square, lid1, viscosity.01, Re100; N24/32/48, lattice lid.04, dt=.04/N. Three stationary walls/rightward lid; stationary side owns a simultaneous top/side link. Initialrho1/rest. Physical unit square, lid1, viscosity.01, Re100; N24/32/48, lattice lid.04, dt=.04/N. Three stationary walls/rightward lid; stationary side owns a simultaneous top/side link. Initialrho1/rest.
- [Manufactured incompressible flow with nonperiodic walls — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/wall-manufactured/?lang=en#references-en>)

  Require finest-pair psi/velocity orders≥1.7, decreasing and bounded errors, and decreasing actual wall-vorticity/velocity-gradient shear errors. Separate pressure orders must be≥1.8 forp and≥1.7 for full/boundary gradients. Record five independent polynomial-reference checks, four-wall values, true steady residual and nonperiodic Poisson residual.
- [Wall manufactured solution: polynomial velocity and separate pressure operator](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-wall-mms-en>)
  relation: same-problem
  reference_kind: manufactured

  Manufactured solution Unit square,viscosity.01,no-slip,psi*=8x²(1−x)²y²(1−y)²,u*=psi*_y,v*=−psi*_x,omega*=−Delta psi*. Construct s=u*omega*_x+v*omega*_y−nu*Delta omega* from the continuous vorticity PDE, qualified by independent tensor-coefficient differentiation. PDE wall vorticity uses the same Thom closure as the cavity without exact injection. Nonzero-Dirichlet Poisson/gradient for p_op=x²+y²+sin(pi*x)sin(pi*y) is a separate operator problem, not coupled flow or cavity pressure. Thom wall vorticity has first-order local truncation; publish observed shear rates without promising second order. Pressure is eliminated from streamfunction evolution, so a pressure gauge is inapplicable. The separate operator MMS does not verify cavity pressure, traction boundaries or MAC projection. Independent polynomial differentiation is distinct from comparison with an independent flow solver.
- [Ghia Re100: original finite-grid velocity centerlines](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-ghia-re100-en>)
  reference_kind: numerical-reference

  Finite-grid numerical reference Unit square,Re100,unit top lid and stationary other walls. Transcribe17points each of u(.5,y) and v(x,.5) after direct inspection of original TablesI/II Re100 columns, preserving printed four-decimal coordinates. Separately compare the grid primary vortex(.6172,.7344) from TableV. These rounded finite-grid numerical tables are neither continuum exact values nor outputs from the present solver.
- [Wall manufactured solution: polynomial velocity and separate pressure operator](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-wall-mms-en>)
  reference_kind: manufactured

  Manufactured solution Unit square,viscosity.01,no-slip,psi*=8x²(1−x)²y²(1−y)²,u*=psi*_y,v*=−psi*_x,omega*=−Delta psi*. Construct s=u*omega*_x+v*omega*_y−nu*Delta omega* from the continuous vorticity PDE, qualified by independent tensor-coefficient differentiation. PDE wall vorticity uses the same Thom closure as the cavity without exact injection. Nonzero-Dirichlet Poisson/gradient for p_op=x²+y²+sin(pi*x)sin(pi*y) is a separate operator problem, not coupled flow or cavity pressure.
- [Re100 lid-driven cavity: Ghia centerline comparison — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/cavity-ghia-re100/?lang=en#cavity-ghia-re100-en-validation>)

  Freeze 22 pytest checks and 94 group gates. Linearly interpolate to 17 points per velocity transcribed after direct visual reading of original TablesI/II, printed 398–399. Require finest component maximum errors≤.03, refinement decrease and steady residual≤1e−7. Also check primary-vortex grid location from TableV, wall values, Poisson residual and discrete divergence.
- [Ghia Re100: original finite-grid velocity centerlines](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-ghia-re100-en>)
  relation: same-problem
  reference_kind: numerical-reference

  Finite-grid numerical reference Unit square,Re100,unit top lid and stationary other walls. Transcribe17points each of u(.5,y) and v(x,.5) after direct inspection of original TablesI/II Re100 columns, preserving printed four-decimal coordinates. Separately compare the grid primary vortex(.6172,.7344) from TableV. These rounded finite-grid numerical tables are neither continuum exact values nor outputs from the present solver. Educational Re100 checks on three fixed grids. Lid/sidewall corner velocities are discontinuous; stationary corners take precedence. Ghia values are rounded numerical references, not an exact solution, and printed four-decimal coordinates are preserved. No high-Re, turbulence, original-algorithm reproduction or cavity-pressure validation is claimed.
- [LBM Re100 cavity: actual2D fields and Ghia centerlines](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-lbm-cavity-re100-en>)
  relation: related-model
  reference_kind: numerical-reference

  Finite-grid numerical reference Physical unit square, lid1, viscosity.01, Re100; N24/32/48, lattice lid.04, dt=.04/N. Three stationary walls/rightward lid; stationary side owns a simultaneous top/side link. Initialrho1/rest. Physical unit square, lid1, viscosity.01, Re100; N24/32/48, lattice lid.04, dt=.04/N. Three stationary walls/rightward lid; stationary side owns a simultaneous top/side link. Initialrho1/rest.
- [Nonperiodic wall MMS: velocity, shear and pressure operator — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/wall-manufactured/?lang=en#wall-manufactured-en-validation>)

  Require finest-pair psi/velocity orders ≥1.7, decreasing and bounded errors, and decreasing actual wall-vorticity/velocity-gradient shear errors. Separate pressure orders must be≥1.8 for p and≥1.7 for full/boundary gradients. Record five independent polynomial-reference checks, four-wall values, true steady residual and nonperiodic Poisson residual.
- [Wall manufactured solution: polynomial velocity and separate pressure operator](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-wall-mms-en>)
  relation: same-problem
  reference_kind: manufactured

  Manufactured solution Unit square,viscosity.01,no-slip,psi*=8x²(1−x)²y²(1−y)²,u*=psi*_y,v*=−psi*_x,omega*=−Delta psi*. Construct s=u*omega*_x+v*omega*_y−nu*Delta omega* from the continuous vorticity PDE, qualified by independent tensor-coefficient differentiation. PDE wall vorticity uses the same Thom closure as the cavity without exact injection. Nonzero-Dirichlet Poisson/gradient for p_op=x²+y²+sin(pi*x)sin(pi*y) is a separate operator problem, not coupled flow or cavity pressure. Thom wall vorticity has first-order local truncation; publish observed shear rates without promising second order. Pressure is eliminated from streamfunction evolution, so a pressure gauge is inapplicable. The separate operator MMS does not verify cavity pressure, traction boundaries or MAC projection. Independent polynomial differentiation is distinct from comparison with an independent flow solver.

## Code and validation

- [Re100 lid-driven cavity: Ghia centerline comparison](<https://hrkoyama.github.io/numerical-methods-atlas/validation/cavity-ghia-re100/?lang=en>)
  availability: run

  March a real nonperiodic 2D viscous incompressible solver to steady state on 17/33/65 node grids and compare against original Ghia centerlines. Retain streamlines, grid vortex center, true PDE residual and discrete divergence.
- [LBM Re100 cavity: actual2D fields and Ghia centerlines](<https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-cavity-re100/?lang=en>)
  availability: run

  Advance genuine four-wall BGK flow on three fixed grids, checking nominal-lid Ghia centerlines, primary vortex, stationarity and wall momentum budgets.
- [Nonperiodic wall MMS: velocity, shear and pressure operator](<https://hrkoyama.github.io/numerical-methods-atlas/validation/wall-manufactured/?lang=en>)
  availability: run

  Apply analytic forcing to the same wall-bounded2D solver, measuring grid convergence of velocity/streamfunction and actual wall-vorticity/shear errors. A separate nonzero-Dirichlet manufactured pressure verifies Poisson and boundary-gradient operators.
