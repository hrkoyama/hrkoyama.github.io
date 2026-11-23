# Low-Mach isentropic vortex: preconditioned Roe flux verification

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-low-mach/

Resources explicitly registered to the methods, problems and executions of this chapter.

## Methods

- [Original Cartesian KEEP split flux](<https://hrkoyama.github.io/numerical-methods-atlas/methods/keep/?lang=en>)

  Retain the historical KEEP/RK4 fixed case and connect Roe, dissipation preconditioning, unlimited central primitive MUSCL and SSPRK(3,3) to the additional low-Mach comparison. Each execution page states its own methods.
- [Classical RK4](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=en>)

  Retain the historical KEEP/RK4 fixed case and connect Roe, dissipation preconditioning, unlimited central primitive MUSCL and SSPRK(3,3) to the additional low-Mach comparison. Each execution page states its own methods.
- [Roe](<https://hrkoyama.github.io/numerical-methods-atlas/methods/roe/?lang=en>)

  Retain the historical KEEP/RK4 fixed case and connect Roe, dissipation preconditioning, unlimited central primitive MUSCL and SSPRK(3,3) to the additional low-Mach comparison. Each execution page states its own methods.
- [Low-Mach PDE preconditioning](<https://hrkoyama.github.io/numerical-methods-atlas/methods/low-mach-preconditioning/?lang=en>)

  Retain the historical KEEP/RK4 fixed case and connect Roe, dissipation preconditioning, unlimited central primitive MUSCL and SSPRK(3,3) to the additional low-Mach comparison. Each execution page states its own methods.
- [SSPRK(3,3)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk33/?lang=en>)

  Retain the historical KEEP/RK4 fixed case and connect Roe, dissipation preconditioning, unlimited central primitive MUSCL and SSPRK(3,3) to the additional low-Mach comparison. Each execution page states its own methods.
- [MUSCL reconstruction](<https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=en>)

  Retain the historical KEEP/RK4 fixed case and connect Roe, dissipation preconditioning, unlimited central primitive MUSCL and SSPRK(3,3) to the additional low-Mach comparison. Each execution page states its own methods.
- [Roe](<https://hrkoyama.github.io/numerical-methods-atlas/methods/roe/?lang=en>)
- [Low-Mach PDE preconditioning](<https://hrkoyama.github.io/numerical-methods-atlas/methods/low-mach-preconditioning/?lang=en>)
- [MUSCL reconstruction](<https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=en>)
- [SSPRK(3,3)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk33/?lang=en>)

## Equations

- [Compressible Euler equations](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#euler-en>)

  The one-dimensional conservative form. Consult each test for its equation of state, initial data and boundaries. Representative equations related to this problem. See the image/problem conditions and each execution example for initial conditions, boundary conditions and parameters.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/low-mach-vortex/?lang=en#low-mach-vortex-en-algorithm>)

  Both finite-volume variants use the same unlimited centered primitive-MUSCL reconstruction,  the physical Euler flux and SSPRK(3,3); only Roe dissipation is replaced by D=P^-1|PA|. At each Roe state use the total-speed Mach with mu=min(1,max(M_local,M_infinity)) and delta=1/mu-1, applying the primitive Miczek matrix through conserved-variable Jacobians. A degree-two characteristic polynomial applies the matrix absolute value; a separate dense eigendecomposition checks it. Physical time and sound speed are unchanged; acoustic CFL=0.2 remains. Reconstructed faces and all three stages check positive density and pressure, without limiters, floors, repair, hidden retries or pseudo-time iteration. A forward-Euler amplification counterexample prevents claiming SSP/TVD or general nonlinear stability from the integrator name.
- [Compressible Euler equations](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#euler-en>)

  The one-dimensional conservative form. Consult each test for its equation of state, initial data and boundaries.

## Problem figures

- [Periodic moving isentropic vortex](<https://hrkoyama.github.io/numerical-methods-atlas/problems/isentropic-vortex/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/low-mach/results/low-mach-vortex-preview.png
- [Low-Mach isentropic vortex: preconditioned Roe flux verification](<https://hrkoyama.github.io/code/validated-examples/2026-11-23/low-mach/results/low-mach-vortex.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/low-mach/results/low-mach-vortex.png

## Exact / reference solutions

- [Periodic moving isentropic vortex — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/isentropic-vortex/?lang=en#references-en>)

  This extends the analytic family used by the historical KEEP vortex with consistently scaled pressure and density at background Mach numbers .1 and .01. The analytic field is a translating whole-plane Euler solution; tiny finite-periodic-box tails and numerical quadrature of conservative cell averages are qualified separately.
- [Isentropic vortex: analytic Euler field for low-Mach comparisons](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-isentropic-vortex-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference The translating whole-plane ideal-gas Euler vortex uses gamma=1.4, beta=3, far-field density1 and background velocity U=(1,.5). For background Mach number M, p_inf=1.25/(1.4*M^2); theta=1-(gamma-1)*beta^2*exp(1-r^2)/(8*gamma*pi^2*p_inf), rho=theta^(1/(gamma-1)), p=p_inf*theta^(gamma/(gamma-1)). Coordinates move with U and are wrapped in [-10,10]^2. The whole-plane field is analytic; the finite minimum-image periodic field retains nonzero Gaussian seam tails and is not a globally exact smooth torus solution. Tensor Gauss8 cell means of all conserved variables are checked against Gauss16, then primitive pressure and velocity are recovered from those means. These are numerical cell quadratures, not closed-form exact cell averages or means of primitive variables. The low-Mach fixed runs use M=.1/.01 and T=.1; the historical KEEP case is recovered by p_inf=1. Analytic field for the same translating isentropic-vortex family. Pressure and velocity are evaluated after Gauss integration of conserved variables; finite-periodic Gaussian tails and quadrature error remain explicit.
- [Isentropic vortex: analytic Euler field for low-Mach comparisons](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-isentropic-vortex-en>)
  reference_kind: analytic

  Analytic reference The translating whole-plane ideal-gas Euler vortex uses gamma=1.4, beta=3, far-field density1 and background velocity U=(1,.5). For background Mach number M, p_inf=1.25/(1.4*M^2); theta=1-(gamma-1)*beta^2*exp(1-r^2)/(8*gamma*pi^2*p_inf), rho=theta^(1/(gamma-1)), p=p_inf*theta^(gamma/(gamma-1)). Coordinates move with U and are wrapped in [-10,10]^2. The whole-plane field is analytic; the finite minimum-image periodic field retains nonzero Gaussian seam tails and is not a globally exact smooth torus solution. Tensor Gauss8 cell means of all conserved variables are checked against Gauss16, then primitive pressure and velocity are recovered from those means. These are numerical cell quadratures, not closed-form exact cell averages or means of primitive variables. The low-Mach fixed runs use M=.1/.01 and T=.1; the historical KEEP case is recovered by p_inf=1.
- [Low-Mach isentropic vortex: preconditioned Roe flux verification — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/low-mach-vortex/?lang=en#low-mach-vortex-en-validation>)

  The original 32 unit tests passed, but one of 143 first-order spatial gates failed: finest M_infinity=0.01 whole-domain dynamic pressure error 0.16537 exceeded the fixed 0.1 threshold. Original sources, contract, all twelve fields and the failed global pressure plot are retained. Revision 2 gives both fluxes the same unlimited centered primitive MUSCL and adds three checks for reconstruction, raw face failure and actual-RHS linearization against independent matrices. Inputs, physical time, CFL and acceptance bytes are unchanged; the revised 35-test/143-gate contract was frozen before revision execution.  Checks cover Roe conserved jumps and physical-flux differences, dense-matrix dissipation, the three stages and raw invalid-stage retention. Each background Mach/flux has 17^2 constant-state Fourier modes and powers 1/10/100 in stated physical acoustic-energy variables. Pressure errors divide by rho_infinity*|U_infinity|^2 rather than the large p_infinity; velocity errors divide by analytic vortex perturbations. Initial R_h-q_t for the translating analytic field is retained as truncation error, not converged steady residual. Revision 2 passed all 35 tests, twelve runs and 143 gates with -W error, taking about 4.4 seconds on the original Mac. At finest M_infinity=0.01, relative velocity L1 was 0.07411 for Roe and 0.01847 for preconditioning; fixed-core pressure errors were 0.04871/0.0006325. Whole-domain pressure errors were instead 0.01194/0.01260, slightly worse with preconditioning; M_infinity=0.1 similarly gave 0.0006653/0.0006737. Maximum relative conserved-budget residual was 4.24e-14. Dynamic-scale Gauss8/16 maximum difference was 4.08e-11 and analytic Euler substitution residual 1.09e-16. Sampled SSPRK3 spectral radii and stated energy-scaled matrix powers had maximum 1. Forward Euler exceeded 1 for both MUSCL variants, reaching about 1.03560 for preconditioning at M_infinity=0.01.
- [Isentropic vortex: analytic Euler field for low-Mach comparisons](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-isentropic-vortex-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference The translating whole-plane ideal-gas Euler vortex uses gamma=1.4, beta=3, far-field density1 and background velocity U=(1,.5). For background Mach number M, p_inf=1.25/(1.4*M^2); theta=1-(gamma-1)*beta^2*exp(1-r^2)/(8*gamma*pi^2*p_inf), rho=theta^(1/(gamma-1)), p=p_inf*theta^(gamma/(gamma-1)). Coordinates move with U and are wrapped in [-10,10]^2. The whole-plane field is analytic; the finite minimum-image periodic field retains nonzero Gaussian seam tails and is not a globally exact smooth torus solution. Tensor Gauss8 cell means of all conserved variables are checked against Gauss16, then primitive pressure and velocity are recovered from those means. These are numerical cell quadratures, not closed-form exact cell averages or means of primitive variables. The low-Mach fixed runs use M=.1/.01 and T=.1; the historical KEEP case is recovered by p_inf=1. Analytic field for the same translating isentropic-vortex family. Pressure and velocity are evaluated after Gauss integration of conserved variables; finite-periodic Gaussian tails and quadrature error remain explicit.

## Code and validation

- [Low-Mach isentropic vortex: preconditioned Roe flux verification](<https://hrkoyama.github.io/numerical-methods-atlas/validation/low-mach-vortex/?lang=en>)
  availability: run

  The same nonlinear 2D Euler vortex is evolved to T=0.1 on N=16/32/64 at background Mach 0.1/0.01, comparing ordinary Roe with Miczek spatial flux preconditioning. Twelve fixed runs retain velocity and dynamically scaled pressure errors, conserved budgets, acoustic steps and actual stage states.
