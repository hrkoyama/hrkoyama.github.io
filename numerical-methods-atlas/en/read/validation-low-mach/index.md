# Low-Mach isentropic vortex: preconditioned Roe flux verification

The same 2D Euler isentropic-vortex family is evolved at background Mach numbers .1 and .01 on 16², 32² and 64² grids to T=.1. Both Roe variants use unlimited central primitive-variable MUSCL reconstruction and SSPRK(3,3); one preconditions numerical dissipation with a Miczek-type matrix. Physical time and acoustic CFL=.2 are retained.

These additional validation supplements are managed separately from the common 22-example registry. Receipts cover independent ZIP extraction, tests and every fixed input within each group. Changes of settings, methods or step sizes do not add independent physical problems.

## Low-Mach isentropic vortex: preconditioned Roe flux verification

The same nonlinear 2D Euler vortex is evolved to T=0.1 on N=16/32/64 at background Mach 0.1/0.01, comparing ordinary Roe with Miczek spatial flux preconditioning. Twelve fixed runs retain velocity and dynamically scaled pressure errors, conserved budgets, acoustic steps and actual stage states.

**Methods used**

- [Roe](https://hrkoyama.github.io/numerical-methods-atlas/methods/roe/?lang=en) (`roe`)
- [Low-Mach PDE preconditioning](https://hrkoyama.github.io/numerical-methods-atlas/methods/low-mach-preconditioning/?lang=en) (`low-mach-preconditioning`)
- [MUSCL reconstruction](https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=en) (`muscl`)
- [SSPRK(3,3)](https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk33/?lang=en) (`ssprk33`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/low-mach-vortex/?lang=en#low-mach-vortex-en-algorithm)

Both finite-volume variants use the same unlimited centered primitive-MUSCL reconstruction,  the physical Euler flux and SSPRK(3,3); only Roe dissipation is replaced by D=P^-1|PA|. At each Roe state use the total-speed Mach with mu=min(1,max(M_local,M_infinity)) and delta=1/mu-1, applying the primitive Miczek matrix through conserved-variable Jacobians. A degree-two characteristic polynomial applies the matrix absolute value; a separate dense eigendecomposition checks it. Physical time and sound speed are unchanged; acoustic CFL=0.2 remains. Reconstructed faces and all three stages check positive density and pressure, without limiters, floors, repair, hidden retries or pseudo-time iteration. A forward-Euler amplification counterexample prevents claiming SSP/TVD or general nonlinear stability from the integrator name.

$$
\partial_tU+\partial_xF(U)+\partial_yG(U)=0,\quad U=(\rho,\rho u,\rho v,E)^T
$$

$$
\widehat F=\tfrac12(F_L+F_R)-\tfrac12J P^{-1}|P A|J^{-1}(U_R-U_L),\quad \mu=\min(1,\max(M_{\rm local},M_\infty)),\quad\delta=\mu^{-1}-1
$$

$$
p_\infty=\frac{|U_\infty|^2}{\gamma M_\infty^2},\qquad \Delta t=\frac{0.2\Delta x}{\max(|u|+c)+\max(|v|+c)}
$$

$$
\chi(k)=\sin k\,(3-\cos k)/2,\quad\psi(k)=(1-\cos k)^2/2,\quad L_h=-i\sum_j\chi(k_j\Delta x)A_j/\Delta x-\sum_j\psi(k_j\Delta x)D_j/\Delta x,\quad R(z)=I+z+z^2/2+z^3/6
$$

- [Compressible Euler equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#euler-en) (`euler`)

Unforced 2D ideal-gas Euler is advanced in the original conservative variables and physical time. Fixed inputs use gamma=1.4, a periodic 20×20 box and a consistently scaled isentropic vortex with Mach-dependent background pressure.


**Problem figure**

![Low-Mach isentropic vortex: preconditioned Roe flux verification: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/low-mach/results/low-mach-vortex.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Periodic moving isentropic vortex](https://hrkoyama.github.io/numerical-methods-atlas/problems/isentropic-vortex/?lang=en) (`isentropic-vortex`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/isentropic-vortex/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/low-mach-vortex/?lang=en#low-mach-vortex-en-validation)

The original 32 unit tests passed, but one of 143 first-order spatial gates failed: finest M_infinity=0.01 whole-domain dynamic pressure error 0.16537 exceeded the fixed 0.1 threshold. Original sources, contract, all twelve fields and the failed global pressure plot are retained. Revision 2 gives both fluxes the same unlimited centered primitive MUSCL and adds three checks for reconstruction, raw face failure and actual-RHS linearization against independent matrices. Inputs, physical time, CFL and acceptance bytes are unchanged; the revised 35-test/143-gate contract was frozen before revision execution.  Checks cover Roe conserved jumps and physical-flux differences, dense-matrix dissipation, the three stages and raw invalid-stage retention. Each background Mach/flux has 17^2 constant-state Fourier modes and powers 1/10/100 in stated physical acoustic-energy variables. Pressure errors divide by rho_infinity*|U_infinity|^2 rather than the large p_infinity; velocity errors divide by analytic vortex perturbations. Initial R_h-q_t for the translating analytic field is retained as truncation error, not converged steady residual. Revision 2 passed all 35 tests, twelve runs and 143 gates with -W error, taking about 4.4 seconds on the original Mac. At finest M_infinity=0.01, relative velocity L1 was 0.07411 for Roe and 0.01847 for preconditioning; fixed-core pressure errors were 0.04871/0.0006325. Whole-domain pressure errors were instead 0.01194/0.01260, slightly worse with preconditioning; M_infinity=0.1 similarly gave 0.0006653/0.0006737. Maximum relative conserved-budget residual was 4.24e-14. Dynamic-scale Gauss8/16 maximum difference was 4.08e-11 and analytic Euler substitution residual 1.09e-16. Sampled SSPRK3 spectral radii and stated energy-scaled matrix powers had maximum 1. Forward Euler exceeded 1 for both MUSCL variants, reaching about 1.03560 for preconditioning at M_infinity=0.01.

- [Isentropic vortex: analytic Euler field for low-Mach comparisons](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-isentropic-vortex-en) (`isentropic-vortex`; Same-problem reference · Analytic reference)

Analytic field for the same translating isentropic-vortex family. Pressure and velocity are evaluated after Gauss integration of conserved variables; finite-periodic Gaussian tails and quadrature error remain explicit.
### Assumptions, units and boundaries

Periodic [-10,10]^2, gamma=1.4, beta=3, background density 1 and velocity (1,0.5). Set p_infinity=|U_infinity|^2/(gamma M_infinity^2), retaining the same flow and vortex strengths. Background Mach is not maximum local Mach. A whole-plane translating isentropic vortex is evaluated with minimum-image coordinates and a separately qualified Gaussian seam. Conserved cell means use eight-point tensor Gauss quadrature, checked against order 16; they are not closed-form exact means or a generic exactly periodic nonlinear vortex.

**Editorial clarification**

The implementation preconditions the numerical-flux dissipation matrix D=P⁻¹|PA|. It does not implement steady pseudo-time or dual-time acceleration, or validate an explicit convective time step. The SSPRK(3,3) name alone does not supply strong-stability or nonlinear positivity guarantees; fixed runs and sampled constant-state Fourier modes have distinct scopes. At the finest M∞=.01 grid, velocity error and vortex kinetic-energy retention improve, but whole-domain dynamically normalized pressure L1 is about .01194 for ordinary Roe and .01260 for preconditioned Roe. Pressure error is not uniformly improved. The vorticity/velocity-perturbation illustration is a central crop; diagnostics distinguish the whole box from a fixed core.

### Adopted numerical method

Both finite-volume variants use the same unlimited centered primitive-MUSCL reconstruction,  the physical Euler flux and SSPRK(3,3); only Roe dissipation is replaced by D=P^-1|PA|. At each Roe state use the total-speed Mach with mu=min(1,max(M_local,M_infinity)) and delta=1/mu-1, applying the primitive Miczek matrix through conserved-variable Jacobians. A degree-two characteristic polynomial applies the matrix absolute value; a separate dense eigendecomposition checks it. Physical time and sound speed are unchanged; acoustic CFL=0.2 remains. Reconstructed faces and all three stages check positive density and pressure, without limiters, floors, repair, hidden retries or pseudo-time iteration. A forward-Euler amplification counterexample prevents claiming SSP/TVD or general nonlinear stability from the integrator name.

$$
\partial_tU+\partial_xF(U)+\partial_yG(U)=0,\quad U=(\rho,\rho u,\rho v,E)^T
$$

$$
\widehat F=\tfrac12(F_L+F_R)-\tfrac12J P^{-1}|P A|J^{-1}(U_R-U_L),\quad \mu=\min(1,\max(M_{\rm local},M_\infty)),\quad\delta=\mu^{-1}-1
$$

$$
p_\infty=\frac{|U_\infty|^2}{\gamma M_\infty^2},\qquad \Delta t=\frac{0.2\Delta x}{\max(|u|+c)+\max(|v|+c)}
$$

$$
\chi(k)=\sin k\,(3-\cos k)/2,\quad\psi(k)=(1-\cos k)^2/2,\quad L_h=-i\sum_j\chi(k_j\Delta x)A_j/\Delta x-\sum_j\psi(k_j\Delta x)D_j/\Delta x,\quad R(z)=I+z+z^2/2+z^3/6
$$

### References and validation

The original 32 unit tests passed, but one of 143 first-order spatial gates failed: finest M_infinity=0.01 whole-domain dynamic pressure error 0.16537 exceeded the fixed 0.1 threshold. Original sources, contract, all twelve fields and the failed global pressure plot are retained. Revision 2 gives both fluxes the same unlimited centered primitive MUSCL and adds three checks for reconstruction, raw face failure and actual-RHS linearization against independent matrices. Inputs, physical time, CFL and acceptance bytes are unchanged; the revised 35-test/143-gate contract was frozen before revision execution.  Checks cover Roe conserved jumps and physical-flux differences, dense-matrix dissipation, the three stages and raw invalid-stage retention. Each background Mach/flux has 17^2 constant-state Fourier modes and powers 1/10/100 in stated physical acoustic-energy variables. Pressure errors divide by rho_infinity*|U_infinity|^2 rather than the large p_infinity; velocity errors divide by analytic vortex perturbations. Initial R_h-q_t for the translating analytic field is retained as truncation error, not converged steady residual. Revision 2 passed all 35 tests, twelve runs and 143 gates with -W error, taking about 4.4 seconds on the original Mac. At finest M_infinity=0.01, relative velocity L1 was 0.07411 for Roe and 0.01847 for preconditioning; fixed-core pressure errors were 0.04871/0.0006325. Whole-domain pressure errors were instead 0.01194/0.01260, slightly worse with preconditioning; M_infinity=0.1 similarly gave 0.0006653/0.0006737. Maximum relative conserved-budget residual was 4.24e-14. Dynamic-scale Gauss8/16 maximum difference was 4.08e-11 and analytic Euler substitution residual 1.09e-16. Sampled SSPRK3 spectral radii and stated energy-scaled matrix powers had maximum 1. Forward Euler exceeded 1 for both MUSCL variants, reaching about 1.03560 for preconditioning at M_infinity=0.01.

### Limits

This is a short T=0.1 fixed-input, few-grid test, not a full circulation or long-time preservation study. The Fourier check covers selected uniform states, wave numbers and powers; it is no proof for all modes, nonlinear variable states or general positivity. Actual integration retains the acoustic CFL and does not use the displayed convective diagnostic step. Steady convergence acceleration, dual time, shock/contact robustness, general meshes and all Mach numbers remain unverified. Finite periodic-box seams, Gauss quadrature and primitive variables evaluated from cell means remain distinct qualifications. Pressure Mach dependence and local errors are retained. Unlimited MUSCL is selected for these smooth inputs, not a limiter, TVD method or general positivity guarantee. The original box-wide pressure waves are shown in a separate full-domain failed-trial figure rather than hidden by the gallery core crop. Velocity/core improvements do not imply globally better pressure: finest whole-domain pressure L1 is slightly larger with preconditioning and grows when background Mach is reduced by ten. No Mach-independent pressure accuracy follows from these measurements. Perturbation kinetic energy is a diagnostic computed from conserved cell means, not exact conservation of continuous kinetic energy.

### Stored measurements and decisions

```json
{
  "metrics": {
    "fixed_runs_completed": 12,
    "maximum_quadrature_dynamic_difference": 4.0745362639427176e-11,
    "maximum_point_Euler_residual": 1.0897087716081738e-16
  },
  "checks": {
    "all twelve fixed nonlinear runs completed": true,
    "M0.1/roe/N16: final time": true,
    "M0.1/roe/N16: minimum_density_all_stages": true,
    "M0.1/roe/N16: minimum_pressure_all_stages": true,
    "M0.1/roe/N16: state_floor_count": true,
    "M0.1/roe/N16: rejected_steps": true,
    "M0.1/roe/N16: mass periodic balance": true,
    "M0.1/roe/N16: x momentum periodic balance": true,
    "M0.1/roe/N16: y momentum periodic balance": true,
    "M0.1/roe/N16: total energy periodic balance": true,
    "M0.1/roe/N16: finite physical diagnostics": true,
    "M0.1/roe/N32: final time": true,
    "M0.1/roe/N32: minimum_density_all_stages": true,
    "M0.1/roe/N32: minimum_pressure_all_stages": true,
    "M0.1/roe/N32: state_floor_count": true,
    "M0.1/roe/N32: rejected_steps": true,
    "M0.1/roe/N32: mass periodic balance": true,
    "M0.1/roe/N32: x momentum periodic balance": true,
    "M0.1/roe/N32: y momentum periodic balance": true,
    "M0.1/roe/N32: total energy periodic balance": true,
    "M0.1/roe/N32: finite physical diagnostics": true,
    "M0.1/roe/N64: final time": true,
    "M0.1/roe/N64: minimum_density_all_stages": true,
    "M0.1/roe/N64: minimum_pressure_all_stages": true,
    "M0.1/roe/N64: state_floor_count": true,
    "M0.1/roe/N64: rejected_steps": true,
    "M0.1/roe/N64: mass periodic balance": true,
    "M0.1/roe/N64: x momentum periodic balance": true,
    "M0.1/roe/N64: y momentum periodic balance": true,
    "M0.1/roe/N64: total energy periodic balance": true,
    "M0.1/roe/N64: finite physical diagnostics": true,
    "M0.1/miczek/N16: final time": true,
    "M0.1/miczek/N16: minimum_density_all_stages": true,
    "M0.1/miczek/N16: minimum_pressure_all_stages": true,
    "M0.1/miczek/N16: state_floor_count": true,
    "M0.1/miczek/N16: rejected_steps": true,
    "M0.1/miczek/N16: mass periodic balance": true,
    "M0.1/miczek/N16: x momentum periodic balance": true,
    "M0.1/miczek/N16: y momentum periodic balance": true,
    "M0.1/miczek/N16: total energy periodic balance": true,
    "M0.1/miczek/N16: finite physical diagnostics": true,
    "M0.1/miczek/N32: final time": true,
    "M0.1/miczek/N32: minimum_density_all_stages": true,
    "M0.1/miczek/N32: minimum_pressure_all_stages": true,
    "M0.1/miczek/N32: state_floor_count": true,
    "M0.1/miczek/N32: rejected_steps": true,
    "M0.1/miczek/N32: mass periodic balance": true,
    "M0.1/miczek/N32: x momentum periodic balance": true,
    "M0.1/miczek/N32: y momentum periodic balance": true,
    "M0.1/miczek/N32: total energy periodic balance": true,
    "M0.1/miczek/N32: finite physical diagnostics": true,
    "M0.1/miczek/N64: final time": true,
    "M0.1/miczek/N64: minimum_density_all_stages": true,
    "M0.1/miczek/N64: minimum_pressure_all_stages": true,
    "M0.1/miczek/N64: state_floor_count": true,
    "M0.1/miczek/N64: rejected_steps": true,
    "M0.1/miczek/N64: mass periodic balance": true,
    "M0.1/miczek/N64: x momentum periodic balance": true,
    "M0.1/miczek/N64: y momentum periodic balance": true,
    "M0.1/miczek/N64: total energy periodic balance": true,
    "M0.1/miczek/N64: finite physical diagnostics": true,
    "M0.01/roe/N16: final time": true,
    "M0.01/roe/N16: minimum_density_all_stages": true,
    "M0.01/roe/N16: minimum_pressure_all_stages": true,
    "M0.01/roe/N16: state_floor_count": true,
    "M0.01/roe/N16: rejected_steps": true,
    "M0.01/roe/N16: mass periodic balance": true,
    "M0.01/roe/N16: x momentum periodic balance": true,
    "M0.01/roe/N16: y momentum periodic balance": true,
    "M0.01/roe/N16: total energy periodic balance": true,
    "M0.01/roe/N16: finite physical diagnostics": true,
    "M0.01/roe/N32: final time": true,
    "M0.01/roe/N32: minimum_density_all_stages": true,
    "M0.01/roe/N32: minimum_pressure_all_stages": true,
    "M0.01/roe/N32: state_floor_count": true,
    "M0.01/roe/N32: rejected_steps": true,
    "M0.01/roe/N32: mass periodic balance": true,
    "M0.01/roe/N32: x momentum periodic balance": true,
    "M0.01/roe/N32: y momentum periodic balance": true,
    "M0.01/roe/N32: total energy periodic balance": true,
    "M0.01/roe/N32: finite physical diagnostics": true,
    "M0.01/roe/N64: final time": true,
    "M0.01/roe/N64: minimum_density_all_stages": true,
    "M0.01/roe/N64: minimum_pressure_all_stages": true,
    "M0.01/roe/N64: state_floor_count": true,
    "M0.01/roe/N64: rejected_steps": true,
    "M0.01/roe/N64: mass periodic balance": true,
    "M0.01/roe/N64: x momentum periodic balance": true,
    "M0.01/roe/N64: y momentum periodic balance": true,
    "M0.01/roe/N64: total energy periodic balance": true,
    "M0.01/roe/N64: finite physical diagnostics": true,
    "M0.01/miczek/N16: final time": true,
    "M0.01/miczek/N16: minimum_density_all_stages": true,
    "M0.01/miczek/N16: minimum_pressure_all_stages": true,
    "M0.01/miczek/N16: state_floor_count": true,
    "M0.01/miczek/N16: rejected_steps": true,
    "M0.01/miczek/N16: mass periodic balance": true,
    "M0.01/miczek/N16: x momentum periodic balance": true,
    "M0.01/miczek/N16: y momentum periodic balance": true,
    "M0.01/miczek/N16: total energy periodic balance": true,
    "M0.01/miczek/N16: finite physical diagnostics": true,
    "M0.01/miczek/N32: final time": true,
    "M0.01/miczek/N32: minimum_density_all_stages": true,
    "M0.01/miczek/N32: minimum_pressure_all_stages": true,
    "M0.01/miczek/N32: state_floor_count": true,
    "M0.01/miczek/N32: rejected_steps": true,
    "M0.01/miczek/N32: mass periodic balance": true,
    "M0.01/miczek/N32: x momentum periodic balance": true,
    "M0.01/miczek/N32: y momentum periodic balance": true,
    "M0.01/miczek/N32: total energy periodic balance": true,
    "M0.01/miczek/N32: finite physical diagnostics": true,
    "M0.01/miczek/N64: final time": true,
    "M0.01/miczek/N64: minimum_density_all_stages": true,
    "M0.01/miczek/N64: minimum_pressure_all_stages": true,
    "M0.01/miczek/N64: state_floor_count": true,
    "M0.01/miczek/N64: rejected_steps": true,
    "M0.01/miczek/N64: mass periodic balance": true,
    "M0.01/miczek/N64: x momentum periodic balance": true,
    "M0.01/miczek/N64: y momentum periodic balance": true,
    "M0.01/miczek/N64: total energy periodic balance": true,
    "M0.01/miczek/N64: finite physical diagnostics": true,
    "M0.1: preconditioned velocity error decreases across grids": true,
    "M0.1: finest preconditioned velocity_relative_l1": true,
    "M0.1: finest preconditioned pressure_dynamic_l1": true,
    "M0.1: finest preconditioned core_pressure_dynamic_l1": true,
    "M0.1: finest preconditioned / Roe velocity error": true,
    "M0.01: preconditioned velocity error decreases across grids": true,
    "M0.01: finest preconditioned velocity_relative_l1": true,
    "M0.01: finest preconditioned pressure_dynamic_l1": true,
    "M0.01: finest preconditioned core_pressure_dynamic_l1": true,
    "M0.01: finest preconditioned / Roe velocity error": true,
    "Fourier M0.1/roe: maximum_SSPRK3_spectral_radius": true,
    "Fourier M0.1/roe: maximum_energy_scaled_power_norm": true,
    "Fourier M0.1/miczek: maximum_SSPRK3_spectral_radius": true,
    "Fourier M0.1/miczek: maximum_energy_scaled_power_norm": true,
    "Fourier M0.01/roe: maximum_SSPRK3_spectral_radius": true,
    "Fourier M0.01/roe: maximum_energy_scaled_power_norm": true,
    "Fourier M0.01/miczek: maximum_SSPRK3_spectral_radius": true,
    "Fourier M0.01/miczek: maximum_energy_scaled_power_norm": true,
    "forward Euler counterexample at the chosen acoustic step": true,
    "analytic qualification: maximum_point_Euler_residual": true,
    "analytic qualification: maximum_quadrature_dynamic_difference": true,
    "analytic qualification: periodic_seam_velocity_bound": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/low-mach-vortex/index.json

![Retained full-domain pressure errors from the original piecewise-constant trial, M_infinity=0.01, N=64, T=0.1. Miczek mean dynamic pressure error 0.16537 failed the unchanged 0.1 criterion. The global failure remains visible; both flux variants were revised to the same smooth MUSCL without changing physical inputs or acceptance. The lower row also shows current full-domain fields on the same color scale, retaining the fact that preconditioning is not uniformly better in global pressure.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/low-mach/results/low-mach-vortex-first-order.png)

Retained full-domain pressure errors from the original piecewise-constant trial, M_infinity=0.01, N=64, T=0.1. Miczek mean dynamic pressure error 0.16537 failed the unchanged 0.1 criterion. The global failure remains visible; both flux variants were revised to the same smooth MUSCL without changing physical inputs or acceptance. The lower row also shows current full-domain fields on the same color scale, retaining the fact that preconditioning is not uniformly better in global pressure.

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23/low-mach/atlas-low-mach-2026-11-23.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23/low-mach/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/low-mach/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23/low-mach/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- Fabian Miczek, Friedrich K. Röpke and Philipp V. F. Edelmann (2015). New numerical solver for flows at various Mach numbers [accessed 2026-11-23]. https://arxiv.org/html/1409.8289; review_level=selected-author-version-full-text: Section8 Eq56; Section4 explicit-RK3 discussion; AppendixA variable transforms; Section6 smooth piecewise-linear reconstruction without a limiter
Selected author-version equations and RK3 discussion were checked. This short isentropic-vortex application does not reproduce the paper’s Gresho or implicit-integration experiments. Section 6 also motivates unlimited piecewise-linear reconstruction for smooth tests; this is independent motivation for the revision.

- Wasilij Barsukow, Philipp V. F. Edelmann, Christian Klingenberg, Fabian Miczek and Friedrich K. Röpke (2017). A Numerical Scheme for the Compressible Low-Mach Number Regime of Ideal Fluid Dynamics [accessed 2026-11-23]. https://arxiv.org/html/1612.03910; review_level=selected-full-text: Section3 Eqs21,31,32; Section5 Eq83 and Fourier-mode stability discussion
Checked the modified dissipation, primitive matrix and restrictive forward-Euler stability result. The present SSPRK33 Fourier/stage checks are separate fixed-input evidence, not a general nonlinear or SSP guarantee.

- Seth C. Spiegel, H. T. Huynh and James R. DeBonis (2015). A Survey of the Isentropic Euler Vortex Problem using High-Order Methods [accessed 2026-11-23]. https://ntrs.nasa.gov/citations/20150018403; review_level=selected-primary-report: parameterized vortex definitions and Sections IV.B/IV.C boundary discussion
Checked the generalized vortex and finite-periodic-boundary qualifications. The selected beta3, mean velocity(1,.5) and background Mach values are explicit adaptations, not NASA/FR execution or figure reuse.

- Sigal Gottlieb and Chi-Wang Shu (1998). Total Variation Diminishing Runge-Kutta Schemes [accessed 2026-11-23]. https://www.cfm.brown.edu/people/sg/SSP1.pdf; review_level=author-bibliography and indexed author-PDF excerpts; direct PDF fetch unavailable
Bibliography and indexed author-PDF excerpts were checked. No direct full-PDF reading is claimed; coefficients are also cross-checked against the author review below.

- Sigal Gottlieb, Chi-Wang Shu and Eitan Tadmor (2001). Strong Stability-Preserving High-Order Time Discretization Methods [accessed 2026-11-23]. https://math.umd.edu/~tadmor/pub/linear-stability/Gottlieb-Shu-Tadmor.SIREV-01.pdf; review_level=selected-full-author-PDF: Section4 Proposition4.1 Eq4.2 printedp100/PDFpage12; Section2.2 Lemma2.1 printedp92/PDFpage4
Checked the three-stage updates and the forward-Euler hypothesis behind SSP. No general SSP/TVD/nonlinear stability guarantee is borrowed for this Miczek flux; the stated Fourier matrices and actual stage states are checked separately.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
