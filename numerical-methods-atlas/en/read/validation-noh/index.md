# Noh shocks: exact reference, origin heating and refinement

Solve zero-pressure planar, cylindrical and spherical Noh flow with 1D finite volumes. Compare exact cell means, origin heating and refinement; separately verify discrete budgets and boundary-time-quadrature error in spherical flow.

These additional validation supplements are managed separately from the common 22-example registry. Receipts cover independent ZIP extraction, tests and every fixed input within each group. Changes of settings, methods or step sizes do not add independent physical problems.

## Noh shocks: zero-pressure planar, cylindrical and spherical flow

An original small 1D finite-volume code solves zero-pressure Noh flow in planar, cylindrical and spherical symmetry. Grids 64/128/256/512 measure full-domain error, origin heating, shock location and budgets, and compare spherical boundary-inflow time-quadrature error with its analytic identity.

**Methods used**

- [Rusanov / local Lax–Friedrichs flux](https://hrkoyama.github.io/numerical-methods-atlas/methods/rusanov/?lang=en) (`rusanov`)
- [Heun / SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en) (`heun`)
- [MUSCL reconstruction](https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=en) (`muscl`)
- [Minmod](https://hrkoyama.github.io/numerical-methods-atlas/methods/minmod/?lang=en) (`minmod`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/?lang=en#noh-shock-en-algorithm)

Rusanov flux with SSPRK2 (Heun). Planar/cylindrical runs retain piecewise-constant reconstruction. Spherical runs reconstruct conserved variables linearly around volume centroids with minmod slopes based on centroid distances in interior cells and zero slopes in the two boundary cells. A single theta per cell scales all conserved slopes at both faces to check face density/internal energy. Cell means are never corrected and no pressure seed/floor is used. Wave speeds, Rusanov flux and numerical stress P*=F_mom-((u_L+u_R)/2)F_mass use the same face states. The geometric CFL V/(A_La_L+A_Ra_R) uses the prescribed .35. Spherical source quadrature exactly integrates the face-linear numerical stress against 2r dr; planar/cylindrical runs keep the old arithmetic rule. Reconstructed reflection faces use even/odd parity, with physical cold inflow at the outer face. Every RK stage is checked and invalid states cause a retained failure.

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
V_i=(r_{i+1/2}^d-r_{i-1/2}^d)/d,\quad P_f^*=\widehat F_{m,f}-\bar u_f\widehat F_{\rho,f},\quad \text{arithmetic-face option: }S_{m,i}V_i=\tfrac12(P_{i-1/2}^*+P_{i+1/2}^*)(A_{i+1/2}-A_{i-1/2})
$$

$$
\mathcal E_1=\frac{\sum_iV_i|\bar\rho_i-\bar\rho_i^{\rm exact}|}{\sum_iV_i\bar\rho_i^{\rm exact}},\quad M(t)=\rho_0(R+|u_0|t)^d/d,\quad E_{\rm tot}(t)=u_0^2M(t)/2
$$

$$
d=3,\ \rho_0=|u_0|=1:\quad M_h-M_{\rm exact}=\frac16\sum_n\Delta t_n^3,\qquad E_h-E_{\rm exact}=\frac1{12}\sum_n\Delta t_n^3
$$

$$
\mathcal E_{\rm core}=\frac{\sum_{r_{i+1/2}\le0.70r_s}V_i|\bar\rho_i-\bar\rho_i^{\rm exact}|}{\sum_{r_{i+1/2}\le0.70r_s}V_i\bar\rho_i^{\rm exact}},\qquad V_i=\frac{r_{i+1/2}^3-r_{i-1/2}^3}{3}
$$

$$
d=3:\quad \int_a^b2rP^*(r)\,dr=\frac{b-a}{3}\big[(b+2a)P_L^*+(2b+a)P_R^*\big]
$$

$$
\bar r_i=\frac{d}{d+1}\frac{r_{i+1/2}^{d+1}-r_{i-1/2}^{d+1}}{r_{i+1/2}^{d}-r_{i-1/2}^{d}},\qquad U_i(r)=\bar U_i+\theta_i\sigma_i(r-\bar r_i)
$$

$$
\sigma_i=\operatorname{minmod}\left(\frac{\bar U_i-\bar U_{i-1}}{\bar r_i-\bar r_{i-1}},\frac{\bar U_{i+1}-\bar U_i}{\bar r_{i+1}-\bar r_i}\right),\quad 0\le\theta_i\le1\quad \text{interior cells; boundary slopes }\sigma_0=\sigma_{N-1}=0
$$

- [Compressible Euler equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#euler-en) (`euler`)

The scoped planar, cylindrical-radial and spherical-radial forms of ideal-gas Euler. This example defines the geometric source, outer inflow and exactly zero initial pressure in its formulas and fixed input.


**Problem figure**

![Noh shocks: zero-pressure planar, cylindrical and spherical flow: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/results/noh-shock.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Noh problem: cold converging flow and outward shock](https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=en) (`noh`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/?lang=en#noh-shock-en-validation)

Retain the planar/cylindrical acceptance file and all 59 original decisions, and save spherical criteria, inputs and source hashes before the first spherical PDE run. The initial cylindrical failure retains its source, all eight diagnostic logs and failed summary; the face-stress revision was tested against the same gates. Analytic conserved means split shock-crossing integrals and distinguish p(mean U) from mean p. The pinned independent LANL ExactPack analytic comparison includes d=1/2/3. New spherical PDE refinements separately measure full-domain r^2-weighted L1/L2/Linf, density L1 in r<=.70rs including the origin, and center/shock/plateau diagnostics. Discrete stage-weighted inflow budgets are distinct from continuous analytic totals; SSPRK2 boundary quadrature is checked through M_h-M_exact=sum(dt^3)/6 and E_h-E_exact=sum(dt^3)/12. The first spherical run retained arithmetic source quadrature and failed two of 105 gates (finest shock-position error 3.923 cells, plateau-density error 11.03%); all results are retained. A second attempt changed only spherical stress quadrature, but still failed the same two gates (3.919 cells and 11.018% density error). A third attempt retains that quadrature and adds MUSCL/minmod reconstruction only for spherical runs, against the same 105 criteria. The third attempt completed 28 tests and all 12 grid runs, passing all 105 gates. At spherical N=512 the whole-domain density L1 is .0114343, shock error 1.98856 cells, plateau-density error 5.2533%, and origin-inclusive core-density L1 .0549503. Maximum center specific-internal-energy excess is 20.59%, worse than the second attempt's 15.52%; not every diagnostic improves.

- [Noh cold-inflow shock: planar, cylindrical and spherical symmetry](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-noh-en) (`noh`; Same-problem reference · Analytic reference)

Analytic reference for the same Noh problem.1D uses exact conserved-volume means;2D uses density means from shock-split Cartesian cell quadrature. Distinguish points/cell means and p(mean U)/mean p.
### Assumptions, units and boundaries

Nondimensional r in [0,1], gamma=5/3, rho0=1, u0=-1, p0=0, T=.6. PDE runs use planar d=1, cylindrical-radial d=2 and spherical-radial d=3, with shock radius .2. Outer density is (1+t)^(d-1), the origin reflects, and the measure is r^(d-1)dr. The same angular factor is omitted throughout; spherical analytic totals are M=512/375 and E=256/375. Its figure is a central section of a 1D radial solution, not a Cartesian 2D/3D calculation or a test of angular symmetry breaking.

**Editorial clarification**

The initial failed attempt retains its source, inputs, diagnostic logs and all eight original full-field profile CSVs. These arrays are distinct from the failed summary recovered verbatim from stdout; their hashes match the same CSVs in the prior r3 edition. The successful release supplies all profiles, histories, results and an independently extracted ZIP rerun.

### Adopted numerical method

Rusanov flux with SSPRK2 (Heun). Planar/cylindrical runs retain piecewise-constant reconstruction. Spherical runs reconstruct conserved variables linearly around volume centroids with minmod slopes based on centroid distances in interior cells and zero slopes in the two boundary cells. A single theta per cell scales all conserved slopes at both faces to check face density/internal energy. Cell means are never corrected and no pressure seed/floor is used. Wave speeds, Rusanov flux and numerical stress P*=F_mom-((u_L+u_R)/2)F_mass use the same face states. The geometric CFL V/(A_La_L+A_Ra_R) uses the prescribed .35. Spherical source quadrature exactly integrates the face-linear numerical stress against 2r dr; planar/cylindrical runs keep the old arithmetic rule. Reconstructed reflection faces use even/odd parity, with physical cold inflow at the outer face. Every RK stage is checked and invalid states cause a retained failure.

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
V_i=(r_{i+1/2}^d-r_{i-1/2}^d)/d,\quad P_f^*=\widehat F_{m,f}-\bar u_f\widehat F_{\rho,f},\quad \text{arithmetic-face option: }S_{m,i}V_i=\tfrac12(P_{i-1/2}^*+P_{i+1/2}^*)(A_{i+1/2}-A_{i-1/2})
$$

$$
\mathcal E_1=\frac{\sum_iV_i|\bar\rho_i-\bar\rho_i^{\rm exact}|}{\sum_iV_i\bar\rho_i^{\rm exact}},\quad M(t)=\rho_0(R+|u_0|t)^d/d,\quad E_{\rm tot}(t)=u_0^2M(t)/2
$$

$$
d=3,\ \rho_0=|u_0|=1:\quad M_h-M_{\rm exact}=\frac16\sum_n\Delta t_n^3,\qquad E_h-E_{\rm exact}=\frac1{12}\sum_n\Delta t_n^3
$$

$$
\mathcal E_{\rm core}=\frac{\sum_{r_{i+1/2}\le0.70r_s}V_i|\bar\rho_i-\bar\rho_i^{\rm exact}|}{\sum_{r_{i+1/2}\le0.70r_s}V_i\bar\rho_i^{\rm exact}},\qquad V_i=\frac{r_{i+1/2}^3-r_{i-1/2}^3}{3}
$$

$$
d=3:\quad \int_a^b2rP^*(r)\,dr=\frac{b-a}{3}\big[(b+2a)P_L^*+(2b+a)P_R^*\big]
$$

$$
\bar r_i=\frac{d}{d+1}\frac{r_{i+1/2}^{d+1}-r_{i-1/2}^{d+1}}{r_{i+1/2}^{d}-r_{i-1/2}^{d}},\qquad U_i(r)=\bar U_i+\theta_i\sigma_i(r-\bar r_i)
$$

$$
\sigma_i=\operatorname{minmod}\left(\frac{\bar U_i-\bar U_{i-1}}{\bar r_i-\bar r_{i-1}},\frac{\bar U_{i+1}-\bar U_i}{\bar r_{i+1}-\bar r_i}\right),\quad 0\le\theta_i\le1\quad \text{interior cells; boundary slopes }\sigma_0=\sigma_{N-1}=0
$$

### References and validation

Retain the planar/cylindrical acceptance file and all 59 original decisions, and save spherical criteria, inputs and source hashes before the first spherical PDE run. The initial cylindrical failure retains its source, all eight diagnostic logs and failed summary; the face-stress revision was tested against the same gates. Analytic conserved means split shock-crossing integrals and distinguish p(mean U) from mean p. The pinned independent LANL ExactPack analytic comparison includes d=1/2/3. New spherical PDE refinements separately measure full-domain r^2-weighted L1/L2/Linf, density L1 in r<=.70rs including the origin, and center/shock/plateau diagnostics. Discrete stage-weighted inflow budgets are distinct from continuous analytic totals; SSPRK2 boundary quadrature is checked through M_h-M_exact=sum(dt^3)/6 and E_h-E_exact=sum(dt^3)/12. The first spherical run retained arithmetic source quadrature and failed two of 105 gates (finest shock-position error 3.923 cells, plateau-density error 11.03%); all results are retained. A second attempt changed only spherical stress quadrature, but still failed the same two gates (3.919 cells and 11.018% density error). A third attempt retains that quadrature and adds MUSCL/minmod reconstruction only for spherical runs, against the same 105 criteria. The third attempt completed 28 tests and all 12 grid runs, passing all 105 gates. At spherical N=512 the whole-domain density L1 is .0114343, shock error 1.98856 cells, plateau-density error 5.2533%, and origin-inclusive core-density L1 .0549503. Maximum center specific-internal-energy excess is 20.59%, worse than the second attempt's 15.52%; not every diagnostic improves.

### Limits

An educational calculation: first-order space in planar/cylindrical flow and MUSCL-type limited linear reconstruction in spherical flow. Origin heating and finite-grid plateau errors remain; the center is never removed from whole-domain error. Because r^2 weighting can make central defects appear small, an origin-inclusive fixed-core norm and enlarged view are also shown. Vanishing Linf/center maximum error, high order for the complete method on smooth spherical problems, general stage positivity with the geometric source, Cartesian multidimensional flow and independent arbitrary-gamma validation are not established. Cylindrical Linf was not monotone in the old series; spherical L2/Linf and heating are retained as diagnostics. Roundoff-scale discrete mass/energy balance coexists with O(dt^2) spherical boundary-time-quadrature error against analytic totals. Radial momentum has a geometric source and is not a conserved Cartesian momentum component. ExactPack independently implements the analytic evaluator, not another numerical PDE engine.

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
    "planar_core_density_l1_finest": 0.006592233446323422,
    "planar_radial_momentum_balance_relative_finest": 1.2490009027033014e-16,
    "planar_mass_temporal_bias_residual_relative_finest": 6.938893903907228e-16,
    "planar_energy_temporal_bias_residual_relative_finest": 6.938893903907228e-16,
    "planar_reconstruction_theta_reduced_stage_cells_finest": 0,
    "planar_reconstruction_theta_zero_stage_cells_finest": 0,
    "planar_reconstruction_theta_min_finest": 1.0,
    "cylindrical_density_l1_finest": 0.01868269537157265,
    "cylindrical_density_l2_finest": 0.10813806869356997,
    "cylindrical_density_linf_finest": 0.5794791984687887,
    "cylindrical_density_l1_order_finest": 0.9603991144824785,
    "cylindrical_shock_error_finest": 0.004146970746716938,
    "cylindrical_center_max_sie_relative_excess_finest": 0.08161167421978366,
    "cylindrical_core_density_l1_finest": 0.04533233801997577,
    "cylindrical_radial_momentum_balance_relative_finest": 4.77048955893622e-16,
    "cylindrical_mass_temporal_bias_residual_relative_finest": 0.0,
    "cylindrical_energy_temporal_bias_residual_relative_finest": 0.0,
    "cylindrical_reconstruction_theta_reduced_stage_cells_finest": 0,
    "cylindrical_reconstruction_theta_zero_stage_cells_finest": 0,
    "cylindrical_reconstruction_theta_min_finest": 1.0,
    "spherical_density_l1_finest": 0.011434288260693065,
    "spherical_density_l2_finest": 0.12865133541762314,
    "spherical_density_linf_finest": 0.6509628676271373,
    "spherical_density_l1_order_finest": 0.9289091507144915,
    "spherical_shock_error_finest": 0.003883913585905091,
    "spherical_center_max_sie_relative_excess_finest": 0.205922730533584,
    "spherical_core_density_l1_finest": 0.05495030379369082,
    "spherical_radial_momentum_balance_relative_finest": 4.3706899842577265e-16,
    "spherical_mass_temporal_bias_residual_relative_finest": 6.154895124725433e-16,
    "spherical_energy_temporal_bias_residual_relative_finest": 6.154895124725433e-16,
    "spherical_reconstruction_theta_reduced_stage_cells_finest": 1968,
    "spherical_reconstruction_theta_zero_stage_cells_finest": 0,
    "spherical_reconstruction_theta_min_finest": 3.415046023746981e-13
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
    "spherical-n64: finite positive density": true,
    "spherical-n64: pressure within roundoff": true,
    "spherical-n64: no state floors": true,
    "spherical-n64: mass_balance_relative": true,
    "spherical-n64: energy_balance_relative": true,
    "spherical-n128: finite positive density": true,
    "spherical-n128: pressure within roundoff": true,
    "spherical-n128: no state floors": true,
    "spherical-n128: mass_balance_relative": true,
    "spherical-n128: energy_balance_relative": true,
    "spherical-n256: finite positive density": true,
    "spherical-n256: pressure within roundoff": true,
    "spherical-n256: no state floors": true,
    "spherical-n256: mass_balance_relative": true,
    "spherical-n256: energy_balance_relative": true,
    "spherical-n512: finite positive density": true,
    "spherical-n512: pressure within roundoff": true,
    "spherical-n512: no state floors": true,
    "spherical-n512: mass_balance_relative": true,
    "spherical-n512: energy_balance_relative": true,
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
    "cylindrical: unmasked center heating reported": true,
    "spherical: finest density_l1": true,
    "spherical: finest shock_error_in_dx": true,
    "spherical: finest plateau_density_relative_error": true,
    "spherical: finest plateau_pressure_relative_error": true,
    "spherical: finest mass_vs_analytic_relative": true,
    "spherical: finest energy_vs_analytic_relative": true,
    "spherical: density L1 decreases": true,
    "spherical: last-pair L1 order": true,
    "spherical: unmasked center heating reported": true,
    "spherical-n64: radial momentum balance relative": true,
    "spherical-n64: mass temporal bias identity relative": true,
    "spherical-n64: energy temporal bias identity relative": true,
    "spherical-n64: finite center diagnostics": true,
    "spherical-n128: radial momentum balance relative": true,
    "spherical-n128: mass temporal bias identity relative": true,
    "spherical-n128: energy temporal bias identity relative": true,
    "spherical-n128: finite center diagnostics": true,
    "spherical-n256: radial momentum balance relative": true,
    "spherical-n256: mass temporal bias identity relative": true,
    "spherical-n256: energy temporal bias identity relative": true,
    "spherical-n256: finite center diagnostics": true,
    "spherical-n512: radial momentum balance relative": true,
    "spherical-n512: mass temporal bias identity relative": true,
    "spherical-n512: energy temporal bias identity relative": true,
    "spherical-n512: finite center diagnostics": true,
    "spherical: finest core density_l1 (origin included)": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/index.json

![Origin heating, signed density error and whole-domain L1/L2/Linf for all three symmetries. Full-domain norms retain the origin and shock.](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/results/noh-shock-errors.png)

Origin heating, signed density error and whole-domain L1/L2/Linf for all three symmetries. Full-domain norms retain the origin and shock.

![Spherical diagnostics separate discrete budgets, differences from analytic totals, the sum(dt^3) boundary-quadrature prediction and origin-inclusive core error.](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/results/noh-spherical-budget.png)

Spherical diagnostics separate discrete budgets, differences from analytic totals, the sum(dt^3) boundary-quadrature prediction and origin-inclusive core error.

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/atlas-noh-2026-11-23-r5.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- W. F. Noh (1987). Errors for calculations of strong shocks using an artificial viscosity and an artificial heat flux. https://www.sciencedirect.com/science/article/pii/002199918790074X; review_level=publisher-metadata-and-abstract
Publisher metadata and abstract checked; full original text was not accessed (403). Cited for the problem and heating-error analysis, not as the source of this particular finite-volume discretization.

- J. Thrussell and J. M. Ferguson (2023). ExactPack: A python library of exact analytic solutions. https://doi.org/10.1016/j.softx.2023.101560; review_level=official-record-and-unmodified-pinned-code-execution
Checked the LANL software record and separately executed unmodified Noh code at commit 9bacc477eb791e959c9621e771fc7a725db755fa. Cross-checks use only gamma=5/3 and rho0=|u0|=1: points and shock-split Gauss integration of conservative means. Retain that d=3 analytic-comparison receipt; this edition separately executes its spherical PDE series.

- van Leer, Bram (1979). Towards the ultimate conservative difference scheme. V. A second-order sequel to Godunov's method. https://www.sciencedirect.com/science/article/pii/0021999179901451; review_level=existing-atlas-publisher-record-and-abstract
Existing Atlas bibliography record. Background for limited linear reconstruction and limiters, not a claim to reproduce the full original algorithm or a general positivity theorem for geometric-source zero-pressure Euler.

- Sweby, P. K. (1984). High Resolution Schemes Using Flux Limiters for Hyperbolic Conservation Laws. https://epubs.siam.org/doi/10.1137/0721062; review_level=existing-atlas-publisher-record-and-abstract
Existing Atlas bibliography record. Background for limited linear reconstruction and limiters, not a claim to reproduce the full original algorithm or a general positivity theorem for geometric-source zero-pressure Euler.

- Mignone, Andrea (2014). High-order conservative reconstruction schemes for finite volume methods in cylindrical and spherical coordinates. https://arxiv.org/abs/1404.0537; review_level=original-arxiv-selected-sections-2.2-3.1-4.2
Selected original arXiv sections 2.2, 3.1 and 4.2 checked for volume centroids, conservative linear reconstruction and source integration. The restricted minmod/Rusanov/Heun and numerical-stress source are Atlas choices, distinct from reproducing the full paper scheme.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
