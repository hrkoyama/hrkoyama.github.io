# Noh shocks: exact reference, origin heating and refinement

A small finite-volume code solves zero-pressure planar and cylindrical Noh flow. Cite the original problem and pinned ExactPack, and examine exact volume averages, origin heating, budgets and remaining errors.

These additional validation supplements are managed separately from the common 22-example registry. Receipts cover independent ZIP extraction, tests and every fixed input within each group. Changes of settings, methods or step sizes do not add independent physical problems.

## Noh shocks: zero-pressure planar and cylindrical flow

A small original 1D finite-volume solver advances the Noh problem from exactly zero pressure, in planar and cylindrical-radial symmetry. Grids 64/128/256/512 separately measure volume-weighted errors, shock location, density amplification, origin heating and mass/total-energy budgets including outer inflow.

**Methods used**

- [Rusanov / local Lax–Friedrichs flux](https://hrkoyama.github.io/numerical-methods-atlas/methods/rusanov/?lang=en) (`rusanov`)
- [Heun / SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en) (`heun`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/?lang=en#noh-shock-en-algorithm)

Piecewise-constant local Lax–Friedrichs/Rusanov flux and SSPRK2 (Heun), with a geometric CFL based on V/(A_L a_L+A_R a_R). The radial-momentum source uses an original consistent first-order quadrature: average the two interfacial numerical normal stresses P*=F_mom−((u_L+u_R)/2)F_mass and multiply by delta A. This exactly balances static constant pressure and vanishes for d=1. Reflection stress reaches the origin cell rather than allowing singular cold accumulation. No state/pressure floor, clipping or substitution of analytic solution arrays. Negative internal energy within roundoff is logged; only the sound-speed square-root argument uses zero at roundoff.

$$
\partial_tU+r^{1-d}\partial_r(r^{d-1}F(U))=(0,(d-1)p/r,0)^T,\quad U=(\rho,\rho u,E)^T
$$

$$
C=(\gamma+1)/(\gamma-1),\quad r_s=|u_0|(\gamma-1)t/2,\quad \rho_2=\rho_0C^d,\quad p_2=(\gamma-1)\rho_2u_0^2/2
$$

$$
\rho_1(r,t)=\rho_0(1+|u_0|t/r)^{d-1},\quad u_1=u_0,\quad p_1=0
$$

$$
V_i=(r_{i+1/2}^d-r_{i-1/2}^d)/d,\quad P_f^*=\widehat F_{m,f}-\bar u_f\widehat F_{\rho,f},\quad S_{m,i}V_i=\tfrac12(P_{i-1/2}^*+P_{i+1/2}^*)(A_{i+1/2}-A_{i-1/2})
$$

$$
\mathcal E_1=\frac{\sum_iV_i|\bar\rho_i-\bar\rho_i^{\rm exact}|}{\sum_iV_i\bar\rho_i^{\rm exact}},\quad M(t)=\rho_0(R+|u_0|t)^d/d,\quad E_{\rm tot}(t)=u_0^2M(t)/2
$$

- [Compressible Euler equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#euler-en) (`euler`)

The scoped planar and cylindrical-radial form of ideal-gas Euler. This example defines the geometric source and zero initial pressure in its formulas and fixed input.


**Problem figure**

![Noh shocks: zero-pressure planar and cylindrical flow: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/noh/results/noh-shock.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Noh shocks: zero-pressure planar and cylindrical flow](https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=en) (`noh`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/?lang=en#noh-shock-en-validation)

Inputs, acceptance criteria and hashes were saved before the first run. The initial cell-pressure p_i delta A source passed planar checks but failed cylindrical shock formation; its source and full refinement results are retained. The interface-stress revision is tested against the SAME thresholds. Analytic conservative cell means split shock-crossing integrals, storing p(mean U) separately from the physical mean pressure. Pinned independent LANL ExactPack was separately executed for points and split-quadrature means. Checks include full-domain volume-weighted relative L1/L2/Linf, explicit center/shock/plateau masks, pressure half-height shock location, initial density amplification 4^d (shock jump 4), and stage-weighted SSPRK2 boundary-inflow budgets.

- [Noh cold-inflow shock: planar and cylindrical symmetry](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-noh-en) (`noh`; Same-problem reference · Analytic reference)

The continuous exact solution of this same zero-pressure Noh problem. Distinguish initial-density amplification4^d from the across-shock ratio4. Finite-volume errors use exact conserved-volume averages, with p(mean U) distinct from mean p.
### Assumptions, units and boundaries

Nondimensional r in [0,1], gamma=5/3, rho0=1, u0=-1, p0=0 and T=.6. PDE executions are only planar d=1 and cylindrical-radial d=2, with shock radius .2. Outer cold density is 1+t for cylindrical flow, 1 for planar flow. Reflecting origin, measure r^(d-1)dr, with the same angular factor omitted throughout. Neither geometry-3 analytic-reference checks nor a revolved display are Cartesian 2D Euler simulations.

**Editorial clarification**

The retained failed attempt includes source, inputs, diagnostic logs for all eight runs and its failed summary recovered verbatim from stdout. It does not contain every failed full-field CSV. The successful release separately supplies all profile CSVs, histories, results and an independently extracted ZIP rerun.

### Adopted numerical method

Piecewise-constant local Lax–Friedrichs/Rusanov flux and SSPRK2 (Heun), with a geometric CFL based on V/(A_L a_L+A_R a_R). The radial-momentum source uses an original consistent first-order quadrature: average the two interfacial numerical normal stresses P*=F_mom−((u_L+u_R)/2)F_mass and multiply by delta A. This exactly balances static constant pressure and vanishes for d=1. Reflection stress reaches the origin cell rather than allowing singular cold accumulation. No state/pressure floor, clipping or substitution of analytic solution arrays. Negative internal energy within roundoff is logged; only the sound-speed square-root argument uses zero at roundoff.

$$
\partial_tU+r^{1-d}\partial_r(r^{d-1}F(U))=(0,(d-1)p/r,0)^T,\quad U=(\rho,\rho u,E)^T
$$

$$
C=(\gamma+1)/(\gamma-1),\quad r_s=|u_0|(\gamma-1)t/2,\quad \rho_2=\rho_0C^d,\quad p_2=(\gamma-1)\rho_2u_0^2/2
$$

$$
\rho_1(r,t)=\rho_0(1+|u_0|t/r)^{d-1},\quad u_1=u_0,\quad p_1=0
$$

$$
V_i=(r_{i+1/2}^d-r_{i-1/2}^d)/d,\quad P_f^*=\widehat F_{m,f}-\bar u_f\widehat F_{\rho,f},\quad S_{m,i}V_i=\tfrac12(P_{i-1/2}^*+P_{i+1/2}^*)(A_{i+1/2}-A_{i-1/2})
$$

$$
\mathcal E_1=\frac{\sum_iV_i|\bar\rho_i-\bar\rho_i^{\rm exact}|}{\sum_iV_i\bar\rho_i^{\rm exact}},\quad M(t)=\rho_0(R+|u_0|t)^d/d,\quad E_{\rm tot}(t)=u_0^2M(t)/2
$$

### References and validation

Inputs, acceptance criteria and hashes were saved before the first run. The initial cell-pressure p_i delta A source passed planar checks but failed cylindrical shock formation; its source and full refinement results are retained. The interface-stress revision is tested against the SAME thresholds. Analytic conservative cell means split shock-crossing integrals, storing p(mean U) separately from the physical mean pressure. Pinned independent LANL ExactPack was separately executed for points and split-quadrature means. Checks include full-domain volume-weighted relative L1/L2/Linf, explicit center/shock/plateau masks, pressure half-height shock location, initial density amplification 4^d (shock jump 4), and stage-weighted SSPRK2 boundary-inflow budgets.

### Limits

An educational first-order-space shock-capturing solver. Plateau density error and origin heating remain even on the finest cylindrical grid. No claim of vanishing center maximum error, a general positivity proof, high-order accuracy, Cartesian multidimensional or spherical PDE execution, or independent validation for arbitrary gamma. The center remains in full-domain errors and heating is not hidden to pass. The retained initial failure shows why mass/energy balance alone does not prove the solution correct. ExactPack is an independent implementation of the analytic reference, not an independent PDE engine. Full-domain cylindrical density Linf does not decrease monotonically in this series. The convergence gate uses the predeclared volume-weighted L1; Linf is retained without concealment.

### Stored measurements and decisions

```json
{
  "metrics": {
    "planar_density_l1_finest": 0.006389021550074538,
    "planar_density_l2_finest": 0.035622324219688015,
    "planar_density_linf_finest": 0.2913310649697939,
    "planar_density_l1_order_finest": 1.088972053769089,
    "planar_shock_error_finest": 0.0006243356111319265,
    "planar_center_max_sie_relative_excess_finest": 0.025776017620378955,
    "cylindrical_density_l1_finest": 0.01868269537157265,
    "cylindrical_density_l2_finest": 0.10813806869356997,
    "cylindrical_density_linf_finest": 0.5794791984687887,
    "cylindrical_density_l1_order_finest": 0.9603991144824785,
    "cylindrical_shock_error_finest": 0.004146970746716938,
    "cylindrical_center_max_sie_relative_excess_finest": 0.08161167421978366
  },
  "checks": {
    "all_runs_reach_final_time": true,
    "planar-n64: finite positive density": true,
    "planar-n64: pressure within roundoff": true,
    "planar-n64: no state floors": true,
    "planar-n64: mass_balance_relative": true,
    "planar-n64: energy_balance_relative": true,
    "planar-n128: finite positive density": true,
    "planar-n128: pressure within roundoff": true,
    "planar-n128: no state floors": true,
    "planar-n128: mass_balance_relative": true,
    "planar-n128: energy_balance_relative": true,
    "planar-n256: finite positive density": true,
    "planar-n256: pressure within roundoff": true,
    "planar-n256: no state floors": true,
    "planar-n256: mass_balance_relative": true,
    "planar-n256: energy_balance_relative": true,
    "planar-n512: finite positive density": true,
    "planar-n512: pressure within roundoff": true,
    "planar-n512: no state floors": true,
    "planar-n512: mass_balance_relative": true,
    "planar-n512: energy_balance_relative": true,
    "cylindrical-n64: finite positive density": true,
    "cylindrical-n64: pressure within roundoff": true,
    "cylindrical-n64: no state floors": true,
    "cylindrical-n64: mass_balance_relative": true,
    "cylindrical-n64: energy_balance_relative": true,
    "cylindrical-n128: finite positive density": true,
    "cylindrical-n128: pressure within roundoff": true,
    "cylindrical-n128: no state floors": true,
    "cylindrical-n128: mass_balance_relative": true,
    "cylindrical-n128: energy_balance_relative": true,
    "cylindrical-n256: finite positive density": true,
    "cylindrical-n256: pressure within roundoff": true,
    "cylindrical-n256: no state floors": true,
    "cylindrical-n256: mass_balance_relative": true,
    "cylindrical-n256: energy_balance_relative": true,
    "cylindrical-n512: finite positive density": true,
    "cylindrical-n512: pressure within roundoff": true,
    "cylindrical-n512: no state floors": true,
    "cylindrical-n512: mass_balance_relative": true,
    "cylindrical-n512: energy_balance_relative": true,
    "planar: finest density_l1": true,
    "planar: finest shock_error_in_dx": true,
    "planar: finest plateau_density_relative_error": true,
    "planar: finest plateau_pressure_relative_error": true,
    "planar: finest mass_vs_analytic_relative": true,
    "planar: finest energy_vs_analytic_relative": true,
    "planar: density L1 decreases": true,
    "planar: last-pair L1 order": true,
    "planar: unmasked center heating reported": true,
    "cylindrical: finest density_l1": true,
    "cylindrical: finest shock_error_in_dx": true,
    "cylindrical: finest plateau_density_relative_error": true,
    "cylindrical: finest plateau_pressure_relative_error": true,
    "cylindrical: finest mass_vs_analytic_relative": true,
    "cylindrical: finest energy_vs_analytic_relative": true,
    "cylindrical: density L1 decreases": true,
    "cylindrical: last-pair L1 order": true,
    "cylindrical: unmasked center heating reported": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/index.json

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/noh/atlas-noh-2026-11-23-r3.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/noh/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/noh/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/noh/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group.

### Sources and review scope

- W. F. Noh (1987). Errors for calculations of strong shocks using an artificial viscosity and an artificial heat flux. https://www.sciencedirect.com/science/article/pii/002199918790074X; review_level=publisher-metadata-and-abstract
  Publisher metadata and abstract checked; full original text was not accessed (403). Cited for the problem and heating-error analysis, not as the source of this particular finite-volume discretization.
- J. Thrussell and J. M. Ferguson (2023). ExactPack: A python library of exact analytic solutions. https://doi.org/10.1016/j.softx.2023.101560; review_level=official-record-and-unmodified-pinned-code-execution
  Checked the LANL software record and separately executed unmodified Noh code at commit 9bacc477eb791e959c9621e771fc7a725db755fa. Cross-checks use only gamma=5/3 and rho0=|u0|=1: points and shock-split Gauss integration of conservative means. Geometry-3 reference checks are not a spherical PDE execution.

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
