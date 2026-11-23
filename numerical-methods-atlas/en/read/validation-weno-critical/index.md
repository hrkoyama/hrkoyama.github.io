# WENO critical points and epsilon dependence

Compare critical-point reconstruction from cell means using WENO-JS/Z power-two weights and actual periodic scalar transport. Separate epsilon choices, analytic cell means versus point values, and spatial error versus time-step effects. For the selected first-critical polynomial, both tiny-epsilon JS and Z show local rates about5; Z has a smaller leading error.

These additional validation supplements are managed separately from the common 22-example registry. Receipts cover independent ZIP extraction, tests and every fixed input within each group. Changes of settings, methods or step sizes do not add independent physical problems.

## WENO-JS/Z: fixed critical-point and epsilon comparison

Compare WENO5 JS and Z power-two weights from the same cell means, then evolve actual periodic transport. Retain three regularity classes, three epsilon choices, fixed grids and separate halved-time-step diagnostics.

**Methods used**

- [WENO5-JS](https://hrkoyama.github.io/numerical-methods-atlas/methods/weno-js/?lang=en) (`weno-js`)
- [FD WENO5-Z](https://hrkoyama.github.io/numerical-methods-atlas/methods/weno-z/?lang=en) (`weno-z`)
- [Classical RK4](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=en) (`rk4`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/weno-critical-epsilon/?lang=en#weno-critical-epsilon-en-algorithm)

Share three candidates, linear weights(.1,.6,.3) and JS indicators. Normalize JS d/(beta+epsilon)² or Z d[1+(|beta0−beta2|/(beta+epsilon))²]. Use epsilon10⁻⁴⁰,10⁻⁶,h². Actual transport uses shared upwind face fluxes and classical RK4 at Courant.1 without state clipping/retries.

$$
\bar q_i=h^{-1}\int_{x_i-h/2}^{x_i+h/2}q(x)\,dx,\qquad q^-_{i+1/2}=\sum_{k=0}^2\omega_k p_k
$$

$$
(p_0,p_1,p_2)=\frac16(2\bar q_{i-2}-7\bar q_{i-1}+11\bar q_i,-\bar q_{i-1}+5\bar q_i+2\bar q_{i+1},2\bar q_i+5\bar q_{i+1}-\bar q_{i+2})
$$

$$
\omega_k=\alpha_k/\sum_j\alpha_j,\quad d=(.1,.6,.3),\quad\alpha_k^{JS}=d_k/(\epsilon+\beta_k)^2,\quad\alpha_k^Z=d_k[1+(\tau_5/(\epsilon+\beta_k))^2],\quad\tau_5=|\beta_0-\beta_2|
$$

$$
\partial_tq+\partial_xq=0,\quad q(x,t)=q_0(x-t),\quad\frac{d\bar q_i}{dt}=-\frac{q^-_{i+1/2}-q^-_{i-1/2}}h
$$

$$
\bar q_i(t)=\operatorname{sinc}(h)\cos\theta_i+.075\operatorname{sinc}(h)\sin\theta_i-.025\operatorname{sinc}(3h)\sin(3\theta_i),\quad\theta_i=2\pi(x_i-t),\quad\operatorname{sinc}(z)=\frac{\sin\pi z}{\pi z}
$$

- [Linear advection](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#linear-advection-en) (`linear-advection`)

Local polynomials have center x=0 and target h/2, h=1/64…1/512. Transport uses periodic[0,1], unit speed, q₀=cos(2πx)+.1sin³(2πx), T=1 and32/64/128 cells. All evolved states/references are FV cell means, not point samples.


**Problem figure**

![WENO-JS/Z: fixed critical-point and epsilon comparison: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/weno-critical/results/weno-critical-epsilon.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Periodic sine-wave advection](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=en) (`advection-sine`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/weno-critical-epsilon/?lang=en#weno-critical-epsilon-en-validation)

Pre-run contract fixes72 local reconstructions,24 PDE runs and36 pytest checks. Qualify analytic means against independent Gauss12 quadrature; retain local errors/weights, transport L1/L2/Linf, mass, stage finiteness, intermediate times and shared-flux budgets. Six finest-grid half-dt differences must be at most10% of corresponding continuum errors.

- [Advection / sine translation](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-sine-advection-en) (`sine-advection`; Related-model reference · Analytic reference)

Same periodic sine-transport model at speed one. The library amplitude is 0.25 versus 0.2 in the common fixed input; DG/CIP representations and output times also differ.

- [WENO critical points: polynomial cell means and analytic periodic transport](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-weno-critical-profile-en) (`weno-critical-profile`; Related-model reference · Analytic reference)

An additional constant-speed periodic-transport reference. The cos+.1sin³ cell means and local critical polynomials differ from the historical single-sine/CIP display.

- [FR/DG periodic sine advection: analytic reference at mean0.4 andT=.25](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-fr-periodic-advection-en) (`fr-periodic-advection`; Same-problem reference · Analytic reference)

Dimensionless u_t+u_x=0 on[0,1), periodic boundary, initial0.4+sin(2pi x), analytic0.4+sin(2pi(x-t)). Constant positive speed1 and uniform affine intervals.
### Assumptions, units and boundaries

Local polynomials have center x=0 and target h/2, h=1/64…1/512. Transport uses periodic[0,1], unit speed, q₀=cos(2πx)+.1sin³(2πx), T=1 and32/64/128 cells. All evolved states/references are FV cell means, not point samples.

**Editorial clarification**

Order gates concern the chosen first-critical interface reconstruction; second-critical values remain diagnostic. Fixed epsilon depends on amplitude/units. Distinguish reconstruction order from PDE convergence and this FV implementation from original FD papers. No shock/Euler/MHD, arbitrary higher-critical-point, universal stability/TVD or positivity guarantee is claimed. For the selected first-critical polynomial, BOTH tiny-epsilon JS and Z have local reconstruction rates of about5 on the last grid pair. JS absolute error decreases from about9.77e-9 to2.88e-13 and Z from about2.12e-9 to5.70e-14, with a finest Z/JS ratio about.198. This fixed example demonstrates a smaller leading error; it does not observe JS order loss or establish universal critical-point order recovery by Z. The second-critical class remains a separate diagnostic.

### Adopted numerical method

Share three candidates, linear weights(.1,.6,.3) and JS indicators. Normalize JS d/(beta+epsilon)² or Z d[1+(|beta0−beta2|/(beta+epsilon))²]. Use epsilon10⁻⁴⁰,10⁻⁶,h². Actual transport uses shared upwind face fluxes and classical RK4 at Courant.1 without state clipping/retries.

$$
\bar q_i=h^{-1}\int_{x_i-h/2}^{x_i+h/2}q(x)\,dx,\qquad q^-_{i+1/2}=\sum_{k=0}^2\omega_k p_k
$$

$$
(p_0,p_1,p_2)=\frac16(2\bar q_{i-2}-7\bar q_{i-1}+11\bar q_i,-\bar q_{i-1}+5\bar q_i+2\bar q_{i+1},2\bar q_i+5\bar q_{i+1}-\bar q_{i+2})
$$

$$
\omega_k=\alpha_k/\sum_j\alpha_j,\quad d=(.1,.6,.3),\quad\alpha_k^{JS}=d_k/(\epsilon+\beta_k)^2,\quad\alpha_k^Z=d_k[1+(\tau_5/(\epsilon+\beta_k))^2],\quad\tau_5=|\beta_0-\beta_2|
$$

$$
\partial_tq+\partial_xq=0,\quad q(x,t)=q_0(x-t),\quad\frac{d\bar q_i}{dt}=-\frac{q^-_{i+1/2}-q^-_{i-1/2}}h
$$

$$
\bar q_i(t)=\operatorname{sinc}(h)\cos\theta_i+.075\operatorname{sinc}(h)\sin\theta_i-.025\operatorname{sinc}(3h)\sin(3\theta_i),\quad\theta_i=2\pi(x_i-t),\quad\operatorname{sinc}(z)=\frac{\sin\pi z}{\pi z}
$$

### References and validation

Pre-run contract fixes72 local reconstructions,24 PDE runs and36 pytest checks. Qualify analytic means against independent Gauss12 quadrature; retain local errors/weights, transport L1/L2/Linf, mass, stage finiteness, intermediate times and shared-flux budgets. Six finest-grid half-dt differences must be at most10% of corresponding continuum errors.

### Limits

Order gates concern the chosen first-critical interface reconstruction; second-critical values remain diagnostic. Fixed epsilon depends on amplitude/units. Distinguish reconstruction order from PDE convergence and this FV implementation from original FD papers. No shock/Euler/MHD, arbitrary higher-critical-point, universal stability/TVD or positivity guarantee is claimed.

### Stored measurements and decisions

```json
{
  "metrics": {
    "completed_pde_runs": 24,
    "local_reconstructions": 72,
    "maximum_transport_mass_error": 2.3288662664988635e-16
  },
  "checks": {
    "72 fixed local reconstructions": true,
    "24 fixed PDE runs completed": true,
    "independent analytic-cell quadrature": true,
    "convex normalized local weights": true,
    "first-critical weno-js fixed-1e-40 refinement n128": true,
    "first-critical weno-js fixed-1e-40 refinement n256": true,
    "first-critical weno-js fixed-1e-40 refinement n512": true,
    "first-critical weno-js fixed-1e-6 refinement n128": true,
    "first-critical weno-js fixed-1e-6 refinement n256": true,
    "first-critical weno-js fixed-1e-6 refinement n512": true,
    "first-critical weno-js h-squared refinement n128": true,
    "first-critical weno-js h-squared refinement n256": true,
    "first-critical weno-js h-squared refinement n512": true,
    "first-critical weno-z fixed-1e-40 refinement n128": true,
    "first-critical weno-z fixed-1e-40 refinement n256": true,
    "first-critical weno-z fixed-1e-40 refinement n512": true,
    "first-critical weno-z fixed-1e-6 refinement n128": true,
    "first-critical weno-z fixed-1e-6 refinement n256": true,
    "first-critical weno-z fixed-1e-6 refinement n512": true,
    "first-critical weno-z h-squared refinement n128": true,
    "first-critical weno-z h-squared refinement n256": true,
    "first-critical weno-z h-squared refinement n512": true,
    "first-critical tiny-epsilon Z/JS error": true,
    "first-critical last reconstruction order weno-z fixed-1e-40": true,
    "first-critical last reconstruction order weno-js h-squared": true,
    "weno-js-fixed-1e-40-n32: finite saved arrays": true,
    "weno-js-fixed-1e-40-n32: time reached": true,
    "weno-js-fixed-1e-40-n32: periodic mass": true,
    "weno-js-fixed-1e-40-n32: shared RHS flux balance": true,
    "weno-js-fixed-1e-40-n32: all requested snapshots": true,
    "weno-js-fixed-1e-40-n32: four stage evaluations per step": true,
    "weno-js-fixed-1e-40-n32: no clipping or retries": true,
    "weno-js-fixed-1e-40-n64: finite saved arrays": true,
    "weno-js-fixed-1e-40-n64: time reached": true,
    "weno-js-fixed-1e-40-n64: periodic mass": true,
    "weno-js-fixed-1e-40-n64: shared RHS flux balance": true,
    "weno-js-fixed-1e-40-n64: all requested snapshots": true,
    "weno-js-fixed-1e-40-n64: four stage evaluations per step": true,
    "weno-js-fixed-1e-40-n64: no clipping or retries": true,
    "weno-js-fixed-1e-40-n128: finite saved arrays": true,
    "weno-js-fixed-1e-40-n128: time reached": true,
    "weno-js-fixed-1e-40-n128: periodic mass": true,
    "weno-js-fixed-1e-40-n128: shared RHS flux balance": true,
    "weno-js-fixed-1e-40-n128: all requested snapshots": true,
    "weno-js-fixed-1e-40-n128: four stage evaluations per step": true,
    "weno-js-fixed-1e-40-n128: no clipping or retries": true,
    "weno-js-fixed-1e-6-n32: finite saved arrays": true,
    "weno-js-fixed-1e-6-n32: time reached": true,
    "weno-js-fixed-1e-6-n32: periodic mass": true,
    "weno-js-fixed-1e-6-n32: shared RHS flux balance": true,
    "weno-js-fixed-1e-6-n32: all requested snapshots": true,
    "weno-js-fixed-1e-6-n32: four stage evaluations per step": true,
    "weno-js-fixed-1e-6-n32: no clipping or retries": true,
    "weno-js-fixed-1e-6-n64: finite saved arrays": true,
    "weno-js-fixed-1e-6-n64: time reached": true,
    "weno-js-fixed-1e-6-n64: periodic mass": true,
    "weno-js-fixed-1e-6-n64: shared RHS flux balance": true,
    "weno-js-fixed-1e-6-n64: all requested snapshots": true,
    "weno-js-fixed-1e-6-n64: four stage evaluations per step": true,
    "weno-js-fixed-1e-6-n64: no clipping or retries": true,
    "weno-js-fixed-1e-6-n128: finite saved arrays": true,
    "weno-js-fixed-1e-6-n128: time reached": true,
    "weno-js-fixed-1e-6-n128: periodic mass": true,
    "weno-js-fixed-1e-6-n128: shared RHS flux balance": true,
    "weno-js-fixed-1e-6-n128: all requested snapshots": true,
    "weno-js-fixed-1e-6-n128: four stage evaluations per step": true,
    "weno-js-fixed-1e-6-n128: no clipping or retries": true,
    "weno-js-h-squared-n32: finite saved arrays": true,
    "weno-js-h-squared-n32: time reached": true,
    "weno-js-h-squared-n32: periodic mass": true,
    "weno-js-h-squared-n32: shared RHS flux balance": true,
    "weno-js-h-squared-n32: all requested snapshots": true,
    "weno-js-h-squared-n32: four stage evaluations per step": true,
    "weno-js-h-squared-n32: no clipping or retries": true,
    "weno-js-h-squared-n64: finite saved arrays": true,
    "weno-js-h-squared-n64: time reached": true,
    "weno-js-h-squared-n64: periodic mass": true,
    "weno-js-h-squared-n64: shared RHS flux balance": true,
    "weno-js-h-squared-n64: all requested snapshots": true,
    "weno-js-h-squared-n64: four stage evaluations per step": true,
    "weno-js-h-squared-n64: no clipping or retries": true,
    "weno-js-h-squared-n128: finite saved arrays": true,
    "weno-js-h-squared-n128: time reached": true,
    "weno-js-h-squared-n128: periodic mass": true,
    "weno-js-h-squared-n128: shared RHS flux balance": true,
    "weno-js-h-squared-n128: all requested snapshots": true,
    "weno-js-h-squared-n128: four stage evaluations per step": true,
    "weno-js-h-squared-n128: no clipping or retries": true,
    "weno-z-fixed-1e-40-n32: finite saved arrays": true,
    "weno-z-fixed-1e-40-n32: time reached": true,
    "weno-z-fixed-1e-40-n32: periodic mass": true,
    "weno-z-fixed-1e-40-n32: shared RHS flux balance": true,
    "weno-z-fixed-1e-40-n32: all requested snapshots": true,
    "weno-z-fixed-1e-40-n32: four stage evaluations per step": true,
    "weno-z-fixed-1e-40-n32: no clipping or retries": true,
    "weno-z-fixed-1e-40-n64: finite saved arrays": true,
    "weno-z-fixed-1e-40-n64: time reached": true,
    "weno-z-fixed-1e-40-n64: periodic mass": true,
    "weno-z-fixed-1e-40-n64: shared RHS flux balance": true,
    "weno-z-fixed-1e-40-n64: all requested snapshots": true,
    "weno-z-fixed-1e-40-n64: four stage evaluations per step": true,
    "weno-z-fixed-1e-40-n64: no clipping or retries": true,
    "weno-z-fixed-1e-40-n128: finite saved arrays": true,
    "weno-z-fixed-1e-40-n128: time reached": true,
    "weno-z-fixed-1e-40-n128: periodic mass": true,
    "weno-z-fixed-1e-40-n128: shared RHS flux balance": true,
    "weno-z-fixed-1e-40-n128: all requested snapshots": true,
    "weno-z-fixed-1e-40-n128: four stage evaluations per step": true,
    "weno-z-fixed-1e-40-n128: no clipping or retries": true,
    "weno-z-fixed-1e-6-n32: finite saved arrays": true,
    "weno-z-fixed-1e-6-n32: time reached": true,
    "weno-z-fixed-1e-6-n32: periodic mass": true,
    "weno-z-fixed-1e-6-n32: shared RHS flux balance": true,
    "weno-z-fixed-1e-6-n32: all requested snapshots": true,
    "weno-z-fixed-1e-6-n32: four stage evaluations per step": true,
    "weno-z-fixed-1e-6-n32: no clipping or retries": true,
    "weno-z-fixed-1e-6-n64: finite saved arrays": true,
    "weno-z-fixed-1e-6-n64: time reached": true,
    "weno-z-fixed-1e-6-n64: periodic mass": true,
    "weno-z-fixed-1e-6-n64: shared RHS flux balance": true,
    "weno-z-fixed-1e-6-n64: all requested snapshots": true,
    "weno-z-fixed-1e-6-n64: four stage evaluations per step": true,
    "weno-z-fixed-1e-6-n64: no clipping or retries": true,
    "weno-z-fixed-1e-6-n128: finite saved arrays": true,
    "weno-z-fixed-1e-6-n128: time reached": true,
    "weno-z-fixed-1e-6-n128: periodic mass": true,
    "weno-z-fixed-1e-6-n128: shared RHS flux balance": true,
    "weno-z-fixed-1e-6-n128: all requested snapshots": true,
    "weno-z-fixed-1e-6-n128: four stage evaluations per step": true,
    "weno-z-fixed-1e-6-n128: no clipping or retries": true,
    "weno-z-h-squared-n32: finite saved arrays": true,
    "weno-z-h-squared-n32: time reached": true,
    "weno-z-h-squared-n32: periodic mass": true,
    "weno-z-h-squared-n32: shared RHS flux balance": true,
    "weno-z-h-squared-n32: all requested snapshots": true,
    "weno-z-h-squared-n32: four stage evaluations per step": true,
    "weno-z-h-squared-n32: no clipping or retries": true,
    "weno-z-h-squared-n64: finite saved arrays": true,
    "weno-z-h-squared-n64: time reached": true,
    "weno-z-h-squared-n64: periodic mass": true,
    "weno-z-h-squared-n64: shared RHS flux balance": true,
    "weno-z-h-squared-n64: all requested snapshots": true,
    "weno-z-h-squared-n64: four stage evaluations per step": true,
    "weno-z-h-squared-n64: no clipping or retries": true,
    "weno-z-h-squared-n128: finite saved arrays": true,
    "weno-z-h-squared-n128: time reached": true,
    "weno-z-h-squared-n128: periodic mass": true,
    "weno-z-h-squared-n128: shared RHS flux balance": true,
    "weno-z-h-squared-n128: all requested snapshots": true,
    "weno-z-h-squared-n128: four stage evaluations per step": true,
    "weno-z-h-squared-n128: no clipping or retries": true,
    "weno-js-fixed-1e-40-time-half: finite saved arrays": true,
    "weno-js-fixed-1e-40-time-half: time reached": true,
    "weno-js-fixed-1e-40-time-half: periodic mass": true,
    "weno-js-fixed-1e-40-time-half: shared RHS flux balance": true,
    "weno-js-fixed-1e-40-time-half: all requested snapshots": true,
    "weno-js-fixed-1e-40-time-half: four stage evaluations per step": true,
    "weno-js-fixed-1e-40-time-half: no clipping or retries": true,
    "weno-js-fixed-1e-6-time-half: finite saved arrays": true,
    "weno-js-fixed-1e-6-time-half: time reached": true,
    "weno-js-fixed-1e-6-time-half: periodic mass": true,
    "weno-js-fixed-1e-6-time-half: shared RHS flux balance": true,
    "weno-js-fixed-1e-6-time-half: all requested snapshots": true,
    "weno-js-fixed-1e-6-time-half: four stage evaluations per step": true,
    "weno-js-fixed-1e-6-time-half: no clipping or retries": true,
    "weno-js-h-squared-time-half: finite saved arrays": true,
    "weno-js-h-squared-time-half: time reached": true,
    "weno-js-h-squared-time-half: periodic mass": true,
    "weno-js-h-squared-time-half: shared RHS flux balance": true,
    "weno-js-h-squared-time-half: all requested snapshots": true,
    "weno-js-h-squared-time-half: four stage evaluations per step": true,
    "weno-js-h-squared-time-half: no clipping or retries": true,
    "weno-z-fixed-1e-40-time-half: finite saved arrays": true,
    "weno-z-fixed-1e-40-time-half: time reached": true,
    "weno-z-fixed-1e-40-time-half: periodic mass": true,
    "weno-z-fixed-1e-40-time-half: shared RHS flux balance": true,
    "weno-z-fixed-1e-40-time-half: all requested snapshots": true,
    "weno-z-fixed-1e-40-time-half: four stage evaluations per step": true,
    "weno-z-fixed-1e-40-time-half: no clipping or retries": true,
    "weno-z-fixed-1e-6-time-half: finite saved arrays": true,
    "weno-z-fixed-1e-6-time-half: time reached": true,
    "weno-z-fixed-1e-6-time-half: periodic mass": true,
    "weno-z-fixed-1e-6-time-half: shared RHS flux balance": true,
    "weno-z-fixed-1e-6-time-half: all requested snapshots": true,
    "weno-z-fixed-1e-6-time-half: four stage evaluations per step": true,
    "weno-z-fixed-1e-6-time-half: no clipping or retries": true,
    "weno-z-h-squared-time-half: finite saved arrays": true,
    "weno-z-h-squared-time-half: time reached": true,
    "weno-z-h-squared-time-half: periodic mass": true,
    "weno-z-h-squared-time-half: shared RHS flux balance": true,
    "weno-z-h-squared-time-half: all requested snapshots": true,
    "weno-z-h-squared-time-half: four stage evaluations per step": true,
    "weno-z-h-squared-time-half: no clipping or retries": true,
    "weno-js fixed-1e-40 PDE refinement n64": true,
    "weno-js fixed-1e-40 PDE refinement n128": true,
    "weno-js fixed-1e-40 finest PDE L1": true,
    "weno-js fixed-1e-40 dt contamination fraction": true,
    "weno-js fixed-1e-6 PDE refinement n64": true,
    "weno-js fixed-1e-6 PDE refinement n128": true,
    "weno-js fixed-1e-6 finest PDE L1": true,
    "weno-js fixed-1e-6 dt contamination fraction": true,
    "weno-js h-squared PDE refinement n64": true,
    "weno-js h-squared PDE refinement n128": true,
    "weno-js h-squared finest PDE L1": true,
    "weno-js h-squared dt contamination fraction": true,
    "weno-z fixed-1e-40 PDE refinement n64": true,
    "weno-z fixed-1e-40 PDE refinement n128": true,
    "weno-z fixed-1e-40 finest PDE L1": true,
    "weno-z fixed-1e-40 dt contamination fraction": true,
    "weno-z fixed-1e-6 PDE refinement n64": true,
    "weno-z fixed-1e-6 PDE refinement n128": true,
    "weno-z fixed-1e-6 finest PDE L1": true,
    "weno-z fixed-1e-6 dt contamination fraction": true,
    "weno-z h-squared PDE refinement n64": true,
    "weno-z h-squared PDE refinement n128": true,
    "weno-z h-squared finest PDE L1": true,
    "weno-z h-squared dt contamination fraction": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/weno-critical-epsilon/index.json

![Saved finest-grid actual periodic transport fields and cell-mean errors, alongside a separate local-polynomial first-critical interface reconstruction study.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/weno-critical/results/weno-critical-epsilon-preview.png)

Saved finest-grid actual periodic transport fields and cell-mean errors, alongside a separate local-polynomial first-critical interface reconstruction study.

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23/weno-critical/atlas-weno-critical-2026-11-23.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23/weno-critical/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/weno-critical/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23/weno-critical/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- Guang-Shan Jiang and Chi-Wang Shu (1996). Efficient Implementation of Weighted ENO Schemes. https://ntrs.nasa.gov/api/citations/19960007052/downloads/19960007052.pdf; review_level=NASA-hosted ICASE95-73 preprint selected sections1–3: candidate Table1, optimal Table2, equations2.15–2.16 and3.1–3.9; text layer inspected, not full paper/numerical tables
Inspected selected sections1–3 of the NASA preprint for candidates, weights, indicators and finite-difference point-value conventions. Original experiments/Euler characteristic reconstruction are not reproduced.

- Rafael Borges, Monique Carmona, Bruno Costa and Wai Sun Don (2008). An improved weighted essentially non-oscillatory scheme for hyperbolic conservation laws. https://scholars.hkbu.edu.hk/en/publications/an-improved-weighted-essentially-non-oscillatory-scheme-for-hyper-2/; review_level=Author-institution publication record and abstract inspected; publisher full text returned403; original full paper and numerical experiments not audited
Inspected the author institution bibliography/abstract. Full publisher text was unavailable; no full-paper audit or replication of original power-one experiments is claimed. The implemented power-two formula was checked in another primary research paper.

- Bart S. van Lith, Jan H. M. ten Thije Boonkkamp and Wilbert L. IJzerman (2017). Embedded WENO: A design strategy to improve existing WENO schemes. https://pure.tue.nl/ws/portalfiles/portal/53481949/embedded_WENO.pdf; review_level=Institution-hosted accepted manuscript section2 equations2–15 (PDF pages4–8) and selected section4.2 (PDF page22) text inspected; screenshot requests cache-missed; not a full-paper review
Inspected cell-average equations2–3, candidate/linear weights4–7, JS indicators/weights8–13, Z weights15 and selected power-two discussion in section4.2. The paper’s new embedded schemes are not implemented and its PDF is not redistributed.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
