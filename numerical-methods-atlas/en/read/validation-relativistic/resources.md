# SRHD collision and nonlinear SRMHD Alfven wave

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-relativistic/

Resources explicitly registered to the methods, problems and executions of this chapter. Compare an SRHD head-on collision with a Taub two-shock solution and full7-state finite-amplitude SRMHD wave with independent tensor formulas/conserved means. Space is1D; x–t pictures are not2D flow.

## Methods

- [HLL](<https://hrkoyama.github.io/numerical-methods-atlas/methods/hll/?lang=en>)

  Use the shared seven-component RMHD operator at B=0 with primitive MUSCL/minmod, causal HLL bounds±1 and SSPRK33. Safeguarded Newton recovers the physical Z=rho h W² root; check residual and full conserved-state roundtrip.
- [MUSCL reconstruction](<https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=en>)

  Use the shared seven-component RMHD operator at B=0 with primitive MUSCL/minmod, causal HLL bounds±1 and SSPRK33. Safeguarded Newton recovers the physical Z=rho h W² root; check residual and full conserved-state roundtrip.
- [Minmod](<https://hrkoyama.github.io/numerical-methods-atlas/methods/minmod/?lang=en>)

  Use the shared seven-component RMHD operator at B=0 with primitive MUSCL/minmod, causal HLL bounds±1 and SSPRK33. Safeguarded Newton recovers the physical Z=rho h W² root; check residual and full conserved-state roundtrip.
- [SSPRK(3,3)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk33/?lang=en>)

  Use the shared seven-component RMHD operator at B=0 with primitive MUSCL/minmod, causal HLL bounds±1 and SSPRK33. Safeguarded Newton recovers the physical Z=rho h W² root; check residual and full conserved-state roundtrip.
- [HLL](<https://hrkoyama.github.io/numerical-methods-atlas/methods/hll/?lang=en>)

  Evolve all seven variables D,three momenta,total E and two transverse magnetic fields with the shared MUSCL/minmod–HLL–SSPRK33 operator. Magnetic dynamics are coupled; primitive recovery solves the full RMHD Z root.
- [MUSCL reconstruction](<https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=en>)

  Evolve all seven variables D,three momenta,total E and two transverse magnetic fields with the shared MUSCL/minmod–HLL–SSPRK33 operator. Magnetic dynamics are coupled; primitive recovery solves the full RMHD Z root.
- [Minmod](<https://hrkoyama.github.io/numerical-methods-atlas/methods/minmod/?lang=en>)

  Evolve all seven variables D,three momenta,total E and two transverse magnetic fields with the shared MUSCL/minmod–HLL–SSPRK33 operator. Magnetic dynamics are coupled; primitive recovery solves the full RMHD Z root.
- [SSPRK(3,3)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk33/?lang=en>)

  Evolve all seven variables D,three momenta,total E and two transverse magnetic fields with the shared MUSCL/minmod–HLL–SSPRK33 operator. Magnetic dynamics are coupled; primitive recovery solves the full RMHD Z root.
- [HLL](<https://hrkoyama.github.io/numerical-methods-atlas/methods/hll/?lang=en>)
- [MUSCL reconstruction](<https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=en>)
- [Minmod](<https://hrkoyama.github.io/numerical-methods-atlas/methods/minmod/?lang=en>)
- [SSPRK(3,3)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk33/?lang=en>)

## Equations

- [Special-relativistic hydrodynamics (SRHD)](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#srhd-en>)

  Ideal fluid in flat Cartesian spacetime,c=1. Add a mild fixed symmetric two-shock example with gamma-law EOS and primitive recovery; no general three-wave Riemann,extreme-Lorentz-factor or GR claim. c=1,gamma5/3,rho1,p.1,opposite normal v±.3,B0. Domain[0,1], initial jump .5,t=.3,96/192/384 cells. Constant extrapolation boundaries before shocks reach endpoints.
- [Special-relativistic ideal MHD (SRMHD)](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#srmhd-en>)

  Flat spacetime,ideal conductivity,gamma-law EOS,c=4pi=1; b^mu is the comoving magnetic four-vector. The1D solver evolves seven conserved variables with full magnetic stress and induction, using coupled RMHD Z recovery. Distinguish it from GRMHD. Flat spacetime,c=4pi=1,gamma4/3,rho=p=Bx=eta1, exact-family vx0. Rescale the original2pi period to a unit domain;64/128/256 cells,periodic,t=1/vA. Normal Bx is fixed in1D.
- [Special-relativistic ideal MHD (SRMHD)](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#srmhd-en>)

  Flat spacetime,ideal conductivity,gamma-law EOS,c=4pi=1; b^mu is the comoving magnetic four-vector. The1D solver evolves seven conserved variables with full magnetic stress and induction, using coupled RMHD Z recovery. Distinguish it from GRMHD.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/srhd-collision/?lang=en#srhd-collision-en-algorithm>)

  Use the shared seven-component RMHD operator at B=0 with primitive MUSCL/minmod, causal HLL bounds±1 and SSPRK33. Safeguarded Newton recovers the physical Z=rho h W² root; check residual and full conserved-state roundtrip.
- [Special-relativistic hydrodynamics (SRHD)](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#srhd-en>)

  Ideal fluid in flat Cartesian spacetime,c=1. Add a mild fixed symmetric two-shock example with gamma-law EOS and primitive recovery; no general three-wave Riemann,extreme-Lorentz-factor or GR claim.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/srmhd-alfven/?lang=en#srmhd-alfven-en-algorithm>)

  Evolve all seven variables D,three momenta,total E and two transverse magnetic fields with the shared MUSCL/minmod–HLL–SSPRK33 operator. Magnetic dynamics are coupled; primitive recovery solves the full RMHD Z root.

## Problem figures

- [SRHD symmetric two-shock collision](<https://hrkoyama.github.io/numerical-methods-atlas/problems/srhd-collision/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/results/srhd-collision-preview.png
- [SRMHD finite-amplitude circularly polarized Alfvén wave](<https://hrkoyama.github.io/numerical-methods-atlas/problems/srmhd-alfven/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/results/srmhd-alfven-preview.png
- [SRHD symmetric two-shock collision](<https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/results/srhd-collision.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/results/srhd-collision.png
- [SRMHD finite-amplitude circularly polarized Alfvén wave](<https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/results/srmhd-alfven.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/results/srmhd-alfven.png

## Exact / reference solutions

- [SRHD symmetric two-shock collision — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/srhd-collision/?lang=en#references-en>)

  Predeclare25 pytest tests,six runs,110 group gates and six reference qualifiers. Check all-component boundary budgets, stage/face admissibility,D/E refinement,star pressure,shock positions and reflection. Compare actual final states with independent scalar-pressure SRHD recovery and flux.
- [Relativistic symmetric collision: specialized two-shock Taub reference](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-srhd-collision-en>)
  relation: same-problem
  reference_kind: semi-analytic

  Semi-analytic reference c=1,gamma5/3,rho1,p.1,opposite normal v±.3,B0. Domain[0,1], initial jump .5,t=.3,96/192/384 cells. Constant extrapolation boundaries before shocks reach endpoints. Solve the pressure root from Taub adiabat and relative-velocity relations for the identical resting star states and shock speeds, then integrate the piecewise-constant exact conserved field over cells. The contact degenerates; this is not a general three-wave Riemann solver. Custom mild symmetric input; contact degenerates to identical resting states. No general three-wave Riemann,extreme-Lorentz-factor or original-paper numerical-input reproduction claim. E includes rest mass; compare exact conserved cell means.
- [SRMHD finite-amplitude circularly polarized Alfvén wave — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/srmhd-alfven/?lang=en#references-en>)

  Qualify nonlinear dispersion,independent tensor Gauss means and complex-step PDE residuals. Predeclare all-seven-component conservation,stage admissibility,intermediate errors,finest relative L1≤.04,phase≤.03,amplitude≤.04 and observed order≥1.5.
- [SRMHD circular wave: finite-amplitude exact family and independent tensor integration](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-srmhd-alfven-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference Flat spacetime,c=4pi=1,gamma4/3,rho=p=Bx=eta1, exact-family vx0. Rescale the original2pi period to a unit domain;64/128/256 cells,periodic,t=1/vA. Normal Bx is fixed in1D. Use the closed nonlinear Alfven-speed formula. Independently form conserved quantities/fluxes from point primitives through the stress tensor; qualify Gauss integration and complex-step PDE residuals. Rescale the original2pi period to the unit interval. Use the original exact family with an independent lower-order operator; no ECHO-algorithm or error-table reproduction. Generic RMHD shocks,extreme magnetization/Lorentz factors,GR,resistive MHD and multidimensional divergence control are outside scope. Figures show actual1D x–t fields.
- [Relativistic symmetric collision: specialized two-shock Taub reference](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-srhd-collision-en>)
  reference_kind: semi-analytic

  Semi-analytic reference c=1,gamma5/3,rho1,p.1,opposite normal v±.3,B0. Domain[0,1], initial jump .5,t=.3,96/192/384 cells. Constant extrapolation boundaries before shocks reach endpoints. Solve the pressure root from Taub adiabat and relative-velocity relations for the identical resting star states and shock speeds, then integrate the piecewise-constant exact conserved field over cells. The contact degenerates; this is not a general three-wave Riemann solver.
- [SRMHD circular wave: finite-amplitude exact family and independent tensor integration](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-srmhd-alfven-en>)
  reference_kind: analytic

  Analytic reference Flat spacetime,c=4pi=1,gamma4/3,rho=p=Bx=eta1, exact-family vx0. Rescale the original2pi period to a unit domain;64/128/256 cells,periodic,t=1/vA. Normal Bx is fixed in1D. Use the closed nonlinear Alfven-speed formula. Independently form conserved quantities/fluxes from point primitives through the stress tensor; qualify Gauss integration and complex-step PDE residuals. Rescale the original2pi period to the unit interval.
- [SRHD symmetric two-shock collision — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/srhd-collision/?lang=en#srhd-collision-en-validation>)

  Predeclare25 pytest tests,six runs,110 group gates and six reference qualifiers. Check all-component boundary budgets, stage/face admissibility,D/E refinement,star pressure,shock positions and reflection. Compare actual final states with independent scalar-pressure SRHD recovery and flux.
- [Relativistic symmetric collision: specialized two-shock Taub reference](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-srhd-collision-en>)
  relation: same-problem
  reference_kind: semi-analytic

  Semi-analytic reference c=1,gamma5/3,rho1,p.1,opposite normal v±.3,B0. Domain[0,1], initial jump .5,t=.3,96/192/384 cells. Constant extrapolation boundaries before shocks reach endpoints. Solve the pressure root from Taub adiabat and relative-velocity relations for the identical resting star states and shock speeds, then integrate the piecewise-constant exact conserved field over cells. The contact degenerates; this is not a general three-wave Riemann solver. Custom mild symmetric input; contact degenerates to identical resting states. No general three-wave Riemann,extreme-Lorentz-factor or original-paper numerical-input reproduction claim. E includes rest mass; compare exact conserved cell means.
- [SRMHD finite-amplitude circularly polarized Alfvén wave — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/srmhd-alfven/?lang=en#srmhd-alfven-en-validation>)

  Qualify nonlinear dispersion,independent tensor Gauss means and complex-step PDE residuals. Predeclare all-seven-component conservation,stage admissibility,intermediate errors,finest relative L1≤.04,phase≤.03,amplitude≤.04 and observed order≥1.5.
- [SRMHD circular wave: finite-amplitude exact family and independent tensor integration](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-srmhd-alfven-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference Flat spacetime,c=4pi=1,gamma4/3,rho=p=Bx=eta1, exact-family vx0. Rescale the original2pi period to a unit domain;64/128/256 cells,periodic,t=1/vA. Normal Bx is fixed in1D. Use the closed nonlinear Alfven-speed formula. Independently form conserved quantities/fluxes from point primitives through the stress tensor; qualify Gauss integration and complex-step PDE residuals. Rescale the original2pi period to the unit interval. Use the original exact family with an independent lower-order operator; no ECHO-algorithm or error-table reproduction. Generic RMHD shocks,extreme magnetization/Lorentz factors,GR,resistive MHD and multidimensional divergence control are outside scope. Figures show actual1D x–t fields.

## Code and validation

- [SRHD symmetric two-shock collision](<https://hrkoyama.github.io/numerical-methods-atlas/validation/srhd-collision/?lang=en>)
  availability: run

  Compare a relativistic symmetric collision with independent exact Taub-based conserved cell means; save actual1D x–t fields.
- [SRMHD finite-amplitude circularly polarized Alfvén wave](<https://hrkoyama.github.io/numerical-methods-atlas/validation/srmhd-alfven/?lang=en>)
  availability: run

  Evolve a nonlinear finite-amplitude wave for one period with full SRMHD magnetic stress and induction; check exact cell means,phase,amplitude and refinement.
