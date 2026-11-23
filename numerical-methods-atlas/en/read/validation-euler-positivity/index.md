# Euler double rarefaction: positivity at every stage

A one-dimensional MUSCL finite-volume Euler double rarefaction combines Lax–Friedrichs fluxes, SSPRK(3,3) and mean-preserving positive-state scaling at each stage. Check the admissible CFL, density/pressure in cell means and face states, and conservation budgets from actual shared boundary fluxes separately.

These additional validation supplements are managed separately from the common 22-example registry. Receipts cover independent ZIP extraction, tests and every fixed input within each group. Changes of settings, methods or step sizes do not add independent physical problems.

## Euler double rarefaction: positivity at every stage

Evolve the existing strong double rarefaction on 128/256/512 cells, connecting mean-preserving positivity scaling to MUSCL, global LF fluxes and SSPRK(3,3). Log density, pressure and boundary budgets for every FE substep and SSP convex combination.

**Methods used**

- [Lax–Friedrichs](https://hrkoyama.github.io/numerical-methods-atlas/methods/lax-friedrichs/?lang=en) (`lax-friedrichs`)
- [MUSCL reconstruction](https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=en) (`muscl`)
- [Mean-preserving positive-state scaling](https://hrkoyama.github.io/numerical-methods-atlas/methods/positive-scaling/?lang=en) (`positive-scaling`)
- [SSPRK(3,3)](https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk33/?lang=en) (`ssprk33`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/euler-double-rarefaction-positivity/?lang=en#euler-double-rarefaction-positivity-en-algorithm)

Unlimited conservative central linear reconstruction is scaled toward its mean with one common theta per cell until both endpoint densities/pressures are positive. The two endpoint mean remains the original conserved mean. Shared LF FE updates are combined by SSPRK(3,3), reconstructing/limiting before every flux stage. Epsilon1e-13 is a reconstruction target, not an injected density/energy floor. No average repair or hidden time-step retries are used.

$$
\partial_t U+\partial_x F(U)=0,\qquad U=(\rho,m,E)^T,\quad F=(m,m^2/\rho+p,(E+p)m/\rho)^T,\quad p=(\gamma-1)(E-m^2/(2\rho))
$$

$$
U_i^{\pm}=\bar U_i\pm\delta U_i,\qquad\widehat U_i^{\pm}=\bar U_i+\theta_i(U_i^{\pm}-\bar U_i),\quad0\le\theta_i\le1,\qquad\tfrac12(\widehat U_i^-+\widehat U_i^+)=\bar U_i
$$

$$
\widehat F_{i+1/2}=\tfrac12\!\left[F(\widehat U_i^+)+F(\widehat U_{i+1}^-)-a(\widehat U_{i+1}^--\widehat U_i^+)\right],\qquad\mathcal E_{\Delta t}(\bar U)_i=\bar U_i-\frac{\Delta t}{\Delta x}(\widehat F_{i+1/2}-\widehat F_{i-1/2})
$$

$$
U^{(1)}=\mathcal E_{\Delta t}(U^n),\qquad U^{(2)}=\tfrac34U^n+\tfrac14\mathcal E_{\Delta t}(U^{(1)}),\qquad U^{n+1}=\tfrac13U^n+\tfrac23\mathcal E_{\Delta t}(U^{(2)})
$$

$$
a\ge\max_{i,\pm}(|u(\widehat U_i^\pm)|+c(\widehat U_i^\pm)),\qquad\frac{a\Delta t}{\Delta x}\le\tfrac12,\qquad\rho(\widehat U_i^\pm)>0,\quad p(\widehat U_i^\pm)>0
$$

- [Compressible Euler equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#euler-en) (`euler`)

Unforced one-dimensional ideal-gas Euler at gamma=1.4 evolves cell means of density, momentum and total energy using linear conservative MUSCL reconstruction and shared Lax–Friedrichs fluxes.


**Problem figure**

![Euler double rarefaction: positivity at every stage: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/results/euler-double-rarefaction-positivity.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Euler double rarefaction](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-rarefaction/?lang=en) (`double-rarefaction`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-rarefaction/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/euler-double-rarefaction-positivity/?lang=en#euler-double-rarefaction-positivity-en-validation)

Freeze 27 unit tests and 73 gates over three grids before execution. Retain negative raw endpoint pressures, then separately measure limited endpoints, FE means, SSP convex means, theta and all three boundary-flux conservation budgets. Cross-check the closed symmetric fan against the prior independent logarithmic-pressure root evaluator; record errors/refinement against conserved Gauss8/16 cell means.

- [Euler / double rarefaction](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-euler-double-rarefaction-en) (`euler-double-rarefaction`; Related-model reference · Semi-analytic reference)

γ=1.4, states (1,-2,0.4)/(1,2,0.4), [0,1], x0=0.5 and t=0.15 match the saved preview. Physical inputs match, but the card’s point samples and the saved computation’s finite-volume cell averages/discrete grid are different representations.
### Assumptions, units and boundaries

Fix gamma1.4, x in [0,1], discontinuity x0=.5, outer primitive states(1,-2,.4)/(1,2,.4) and T=.15. The low-density central state remains strictly positive; this is not a vacuum-generating case. Use fixed global LF splitting speed a4 and dt*a/dx<=.4; assert every actual endpoint satisfies |u|+c<=a and the sufficient dt*a/dx<=1/2 condition.

**Editorial clarification**

The same fixed physical input as the existing double rarefaction uses gamma=1.4, left/right (rho,u,p)=(1,-2,.4)/(1,2,.4), [0,1], x0=.5 and t=.15. Its middle state has small positive density/pressure, unlike separate vacuum-generating data. Stage scaling is connected to sufficient CFL and Lax–Friedrichs wave-speed conditions for this scoped example, without certifying existing WENO, DG, MHD or general equations of state.

### Adopted numerical method

Unlimited conservative central linear reconstruction is scaled toward its mean with one common theta per cell until both endpoint densities/pressures are positive. The two endpoint mean remains the original conserved mean. Shared LF FE updates are combined by SSPRK(3,3), reconstructing/limiting before every flux stage. Epsilon1e-13 is a reconstruction target, not an injected density/energy floor. No average repair or hidden time-step retries are used.

$$
\partial_t U+\partial_x F(U)=0,\qquad U=(\rho,m,E)^T,\quad F=(m,m^2/\rho+p,(E+p)m/\rho)^T,\quad p=(\gamma-1)(E-m^2/(2\rho))
$$

$$
U_i^{\pm}=\bar U_i\pm\delta U_i,\qquad\widehat U_i^{\pm}=\bar U_i+\theta_i(U_i^{\pm}-\bar U_i),\quad0\le\theta_i\le1,\qquad\tfrac12(\widehat U_i^-+\widehat U_i^+)=\bar U_i
$$

$$
\widehat F_{i+1/2}=\tfrac12\!\left[F(\widehat U_i^+)+F(\widehat U_{i+1}^-)-a(\widehat U_{i+1}^--\widehat U_i^+)\right],\qquad\mathcal E_{\Delta t}(\bar U)_i=\bar U_i-\frac{\Delta t}{\Delta x}(\widehat F_{i+1/2}-\widehat F_{i-1/2})
$$

$$
U^{(1)}=\mathcal E_{\Delta t}(U^n),\qquad U^{(2)}=\tfrac34U^n+\tfrac14\mathcal E_{\Delta t}(U^{(1)}),\qquad U^{n+1}=\tfrac13U^n+\tfrac23\mathcal E_{\Delta t}(U^{(2)})
$$

$$
a\ge\max_{i,\pm}(|u(\widehat U_i^\pm)|+c(\widehat U_i^\pm)),\qquad\frac{a\Delta t}{\Delta x}\le\tfrac12,\qquad\rho(\widehat U_i^\pm)>0,\quad p(\widehat U_i^\pm)>0
$$

### References and validation

Freeze 27 unit tests and 73 gates over three grids before execution. Retain negative raw endpoint pressures, then separately measure limited endpoints, FE means, SSP convex means, theta and all three boundary-flux conservation budgets. Cross-check the closed symmetric fan against the prior independent logarithmic-pressure root evaluator; record errors/refinement against conserved Gauss8/16 cell means.

### Limits

Evidence covers this one P1 FV update and fixed input, not general MUSCL/WENO/DG, characteristic reconstruction, reflecting walls, vacuum generation or multidimensional positivity. Unlimited central slopes have no TVD, maximum-principle or nonoscillation guarantee. Raw pressure is evaluated only where raw density is positive; nonpositive raw density has its own count. Reference pressure is p(mean conserved q), not mean pressure. Gallery plots are saved one-dimensional x-t fields, not two-dimensional flow. No ExactPack or separate PDE engine is executed.

### Stored measurements and decisions

```json
{
  "metrics": {
    "n": 512,
    "time": 0.15,
    "steps": 769,
    "stages": 2307,
    "density_l1": 0.013786535690656554,
    "pressure_l1": 0.01435653469629682,
    "density_linf": 0.03601512711847121,
    "pressure_linf": 0.019973924350945027,
    "velocity_linf": 0.027566317367641924,
    "reference_quadrature_maximum": 1.3322676295501878e-15,
    "scaled_cells": 6,
    "maximum_face_spectral_radius": 2.771191823275851,
    "maximum_courant": 0.4,
    "maximum_mean_preservation_defect": 2.220446049250313e-16,
    "maximum_fe_boundary_balance_defect": 1.9081958235744878e-17,
    "maximum_rk_boundary_balance_defect": 8.456776945386935e-17,
    "raw_endpoint_nonpositive_density_count": 0,
    "state_floor_count": 0,
    "rejected_steps": 0,
    "retries": 0,
    "raw_endpoint_min_density": 0.009732631218285564,
    "raw_endpoint_min_pressure": -0.5999999999999999,
    "endpoint_min_density": 0.009732631218285564,
    "endpoint_min_pressure": 1.0640377468007498e-13,
    "fe_mean_min_density": 0.009774320902145379,
    "fe_mean_min_pressure": 0.0016944640635574622,
    "rk_mean_min_density": 0.00977443913337385,
    "rk_mean_min_pressure": 0.0016944926865771217,
    "minimum_theta": 0.4494897427830696
  },
  "checks": {
    "all fixed refinements completed": true,
    "N128: final time": true,
    "N128: three records per full SSP step": true,
    "N128: rk_mean_min_density": true,
    "N128: rk_mean_min_pressure": true,
    "N128: endpoint_min_density": true,
    "N128: endpoint_min_pressure": true,
    "N128: fe_mean_min_density": true,
    "N128: fe_mean_min_pressure": true,
    "N128: maximum_face_spectral_radius": true,
    "N128: maximum_courant": true,
    "N128: maximum_mean_preservation_defect": true,
    "N128: maximum_fe_boundary_balance_defect": true,
    "N128: maximum_rk_boundary_balance_defect": true,
    "N128: zero mass/energy floor injections": true,
    "N128: zero retries or rejected steps": true,
    "N128: scaling actually exercised": true,
    "N128: raw nonadmissible reconstruction retained": true,
    "N128: mass boundary budget": true,
    "N128: momentum boundary budget": true,
    "N128: energy boundary budget": true,
    "N128: split Gauss8/16 reference": true,
    "N256: final time": true,
    "N256: three records per full SSP step": true,
    "N256: rk_mean_min_density": true,
    "N256: rk_mean_min_pressure": true,
    "N256: endpoint_min_density": true,
    "N256: endpoint_min_pressure": true,
    "N256: fe_mean_min_density": true,
    "N256: fe_mean_min_pressure": true,
    "N256: maximum_face_spectral_radius": true,
    "N256: maximum_courant": true,
    "N256: maximum_mean_preservation_defect": true,
    "N256: maximum_fe_boundary_balance_defect": true,
    "N256: maximum_rk_boundary_balance_defect": true,
    "N256: zero mass/energy floor injections": true,
    "N256: zero retries or rejected steps": true,
    "N256: scaling actually exercised": true,
    "N256: raw nonadmissible reconstruction retained": true,
    "N256: mass boundary budget": true,
    "N256: momentum boundary budget": true,
    "N256: energy boundary budget": true,
    "N256: split Gauss8/16 reference": true,
    "N512: final time": true,
    "N512: three records per full SSP step": true,
    "N512: rk_mean_min_density": true,
    "N512: rk_mean_min_pressure": true,
    "N512: endpoint_min_density": true,
    "N512: endpoint_min_pressure": true,
    "N512: fe_mean_min_density": true,
    "N512: fe_mean_min_pressure": true,
    "N512: maximum_face_spectral_radius": true,
    "N512: maximum_courant": true,
    "N512: maximum_mean_preservation_defect": true,
    "N512: maximum_fe_boundary_balance_defect": true,
    "N512: maximum_rk_boundary_balance_defect": true,
    "N512: zero mass/energy floor injections": true,
    "N512: zero retries or rejected steps": true,
    "N512: scaling actually exercised": true,
    "N512: raw nonadmissible reconstruction retained": true,
    "N512: mass boundary budget": true,
    "N512: momentum boundary budget": true,
    "N512: energy boundary budget": true,
    "N512: split Gauss8/16 reference": true,
    "finest density_l1": true,
    "density_l1 refinement ratio 1": true,
    "density_l1 refinement ratio 2": true,
    "finest pressure_l1": true,
    "pressure_l1 refinement ratio 1": true,
    "pressure_l1 refinement ratio 2": true,
    "reference: star_pressure_absolute_difference": true,
    "reference: independent_root_point_maximum_difference": true,
    "reference: maximum_scaled_euler_residual": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/euler-double-rarefaction-positivity/index.json

![Density/pressure of the strong double rarefaction: x-t views of saved one-dimensional evolution, not two-dimensional flow.](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/results/euler-double-rarefaction-positivity-preview.png)

Density/pressure of the strong double rarefaction: x-t views of saved one-dimensional evolution, not two-dimensional flow.

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/atlas-euler-positivity-2026-11-23-r2.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group.

### Sources and review scope

- Xiangxiong Zhang and Chi-Wang Shu (2010). On positivity-preserving high order discontinuous Galerkin schemes for compressible Euler equations on rectangular meshes. https://www.math.purdue.edu/~zhan1966/research/paper/euler.pdf; review_level=author manuscript selected sections actually inspected: §2 Theorem2.1, Remarks2.2/2.4/2.6/2.7; §4.3 distinguishes vacuum input
  Inspected positivity conditions, LF proof, stage limiting and speed-bound caution. This applies the framework to P1 FV; it does not reproduce the paper’s vacuum test or third-order DG scheme.
- David I. Ketcheson, Randall J. LeVeque and Mauricio J. del Razo (2020). Riemann Problems and Jupyter Solutions: The Euler equations of gas dynamics. https://www.clawpack.org/riemann_book/html/Euler.html; review_level=official chapter sections Riemann invariants, exact solution, symmetric expansion and vacuum; official exact_solvers/euler.py integral_curve_1/3 inspected read-only
  Read the official invariants, symmetric expansion and vacuum conditions. The fixed values inherit the existing atlas case and differ from this chapter’s example. No Clawpack software is executed or copied.
- Chi-Wang Shu and Stanley Osher (1988). Efficient implementation of essentially non-oscillatory shock-capturing schemes. https://www.sciencedirect.com/science/article/pii/0021999188901775; review_level=publisher bibliographic record and abstract only; no full-paper audit
  Publisher record and abstract reviewed; the full paper and numerical experiments were not audited. The convex-combination positivity application was also checked in the Zhang–Shu manuscript.
- Eleuterio F. Toro (2009). Riemann Solvers and Numerical Methods for Fluid Dynamics: A Practical Introduction. https://link.springer.com/book/10.1007/b79761; review_level=publisher bibliography and chapter4 title/pages115–162 only; full text not inspected
  Publisher metadata and Euler Riemann chapter listing checked. This inspection alone does not establish the first historical source of the fixed numerical data.
- Hiroshi Koyama (2026). Numerical Methods Atlas: released independent Euler Riemann evaluator. https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/reference_riemann.py; review_level=local immutable source inspected; copied without changes with SHA and MIT license; execution recorded by tests, not presumed
  The prior logarithmic-pressure root and fan evaluator provide a separate algebraic check, with SHA and MIT terms. It is not a different PDE engine; execution is established by test receipts.

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
