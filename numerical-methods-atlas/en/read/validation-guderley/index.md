# Guderley converging shock: lightweight spherical-radial verification

HLL plus Heun follows a Guderley shock into stationary zero-pressure upstream gas at gamma=1.4, r in [0,0.75], t=-1 to -0.85 on 128/256/512 shells. Initialize the similarity field with Rs(-1)=0.6 and compare the pre-collapse trajectory, conserved shell means and budgets with a semi-analytic reference. The figure is a 2D section display of 1D radial results.

These additional validation supplements are managed separately from the common 22-example registry. Receipts cover independent ZIP extraction, tests and every fixed input within each group. Changes of settings, methods or step sizes do not add independent physical problems.

## Guderley converging shock: lightweight spherical-radial verification

An inward spherical Guderley shock in cold stationary gas is evolved from t=-1 to -0.85 on 128/256/512 radial shells. HLL fluxes and Heun steps are checked against a similarity eigenvalue/field, shock trajectory and discrete conservation budgets.

**Methods used**

- [HLL](https://hrkoyama.github.io/numerical-methods-atlas/methods/hll/?lang=en) (`hll`)
- [Heun / SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en) (`heun`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/guderley-implosion/?lang=en#guderley-implosion-en-algorithm)

First-order spherical finite volumes use face area4pi*r^2 and shell volume4pi*delta(r^3)/3. Shared HLL flux divergence plus the radial-momentum pressure source p_i*delta(A)/V is advanced by Heun at CFL0.4. The center is reflecting with zero face area; the outer similarity state is evaluated at both actual RK times. All three conserved budgets integrate the actual boundary flux and geometric source using the same Heun weights. There are no state floors, pressure repairs or hidden step retries.

$$
\partial_t U+\frac{1}{r^2}\partial_r(r^2 F)=\left(0,\frac{2p}{r},0\right)^T,\quad U=(\rho,\rho u,E)^T
$$

$$
R_s(t)=0.6(-t)^\alpha,\quad\alpha=1/\lambda,\quad \lambda\simeq1.3943607844,\quad t<0
$$

$$
\frac{d\bar U_i}{dt}=-\frac{A_{i+1/2}\widehat F_{i+1/2}-A_{i-1/2}\widehat F_{i-1/2}}{V_i}+\left(0,p_i\frac{\Delta A_i}{V_i},0\right)^T
$$

$$
\bar U_i^{\rm ref}=\frac{\int_{r_{i-1/2}}^{r_{i+1/2}}U_{\rm sim}(r,t)r^2\,dr}{(r_{i+1/2}^3-r_{i-1/2}^3)/3},\qquad p_i^{\rm ref}=p(\bar U_i^{\rm ref})
$$

- [Compressible Euler equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#euler-en) (`euler`)

The one-dimensional spherical-radial ideal-gas Euler system with zero upstream pressure and gamma=1.4. The fixed input defines a pre-collapse interval, similarity initial field, boundaries and shell averaging.


**Problem figure**

![Guderley converging shock: lightweight spherical-radial verification: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/guderley/results/guderley-implosion.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Guderley converging shock](https://hrkoyama.github.io/numerical-methods-atlas/problems/guderley/?lang=en) (`guderley`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/guderley/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/guderley-implosion/?lang=en#guderley-implosion-en-validation)

The33 unit checks and55 gates over three refinements were fixed before execution and passed with warnings treated as errors. Checks cover the zero-sound-speed cold HLL branch, geometric static-pressure balance, shared-flux budgets, actual two-stage boundary times and raw failed-stage retention. Full-volume L1 is shown alongside the predetermined r>=0.8*Rs shock/nonzero-flow region, so cold inner gas does not hide active errors. Maximum density/pressure differences and the saved shock trajectory remain visible. The semi-analytic reference uses the pinned LANL ExactPack eigenvalue routine and ODE through a cached pre-collapse-only adapter. It is not an independently reimplemented similarity ODE; the separately implemented finite-volume Euler evolution is compared against that reference. Full-volume density L1 is0.02345/0.01339/0.007722 and pressure L1 is0.03277/0.01743/0.009477. Density L1 in the predetermined r>=0.8*Rs region also decreases:0.02414/0.01378/0.007948. The finest measured shock radius is0.530273 against similarity0.533989, about2.54 cells apart. The maximum scaled three-component budget residual is8.85e-16. Minimum internal energy and sound-speed-only roundoff guard evaluations are both0. The smooth-reference Euler finite-difference residual is8.24e-9 and finite-offset moving-jump residual4.40e-8. The older three-run execution with a newly computed similarity eigenvalue took about44.6 seconds on the original Mac. Public r2 passed all33 Linux tests in96.34 seconds, but its fixed-input runner timed out after the remaining23.31 seconds of the combined120-second test-plus-run budget. That failed replay and its sources are retained. The revision reuses the eigenvalue already obtained by actual ExactPack shooting, bound by SHA to its source and qualification, instead of shooting again in both normal processes. The critical-phase Cdiff residual and similarity ODE are freshly evaluated. Inputs, numerical criteria, Euler solver, fixed-input runner and120-second budget are unchanged. In the revision,33 unit tests and all three fixed inputs with55 gates completed sequentially within one120-second budget in about0.912s on the Mac. Initial,final,reference and saved-history arrays for all three grids were bit-identical to published r2, separately checking that reuse of the eigenvalue preserved the physical results.

- [Guderley converging shock: eigenvalue and spherical semi-analytic reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-guderley-en) (`guderley`; Same-problem reference · Semi-analytic reference)

The pre-collapse branch of the spherical Guderley similarity solution at gamma=1.4 with a cold uniform upstream state. Eigenvalue shooting, similarity-ODE integration and shock-split shell quadrature make it semi-analytic rather than closed-form exact cell means. Routine replay reuses lambda from the retained qualification, freshly integrating the similarity ODE and quadrature; recomputing the eigenvalue and original ExactPack probes is a separate explicit command. This is an adapter to pinned ExactPack, not an independently implemented similarity evaluator. Collapse at the origin, the reflected shock and general equations of state remain outside this example.
### Assumptions, units and boundaries

Fix gamma=1.4, three-dimensional spherical symmetry on r in [0,0.75], Rs(-1)=0.6 and t in [-1,-0.85]. Ahead of the inward shock the inner gas is exactly rho0=1,u0=p0=0. The outer region already contains the shocked similarity field; the entire initial domain is not a uniform cold state. Initial conserved shell means use order16 Gauss integration split at the exact shock, checked against order32. Reference pressure is p(mean conserved state), not mean primitive pressure.

**Editorial clarification**

The pre-collapse branch of the spherical Guderley similarity solution at gamma=1.4 with a cold uniform upstream state. Numerical eigenvalue shooting, similarity-ODE integration and shock-split shell quadrature make this a semi-analytic reference, not closed-form exact cell means. Distinguish the ExactPack-based evaluator from the finite-volume PDE calculation; this is not a comparison between independent similarity implementations. Collapse at the origin, the reflected branch and general equations of state are outside this example. Full-volume density/pressure L1 and the predetermined r>=0.8*Rs active-region L1 decrease across the three grids, but shock-layer density/pressure Linf and shock-location error in cell widths do not decrease monotonically. No collapse or high-order shock-detail convergence is claimed. Minimum raw internal-energy density was 0, including the cold upstream, and the sound-speed square-root guard was used zero times in all three runs. Routine replay reuses lambda qualified by the retained eigenvalue shooting and eight original ExactPack probes, while freshly integrating the similarity ODE, shell quadrature and Euler evolution. Recomputing the eigenvalue/original-source probes is a separate explicit command. The r2 public Linux replay passed 33 tests before reaching the unchanged 120-second group limit; its failure record is retained, with physical inputs and acceptance criteria preserved for the lighter routine replay.

### Adopted numerical method

First-order spherical finite volumes use face area4pi*r^2 and shell volume4pi*delta(r^3)/3. Shared HLL flux divergence plus the radial-momentum pressure source p_i*delta(A)/V is advanced by Heun at CFL0.4. The center is reflecting with zero face area; the outer similarity state is evaluated at both actual RK times. All three conserved budgets integrate the actual boundary flux and geometric source using the same Heun weights. There are no state floors, pressure repairs or hidden step retries.

$$
\partial_t U+\frac{1}{r^2}\partial_r(r^2 F)=\left(0,\frac{2p}{r},0\right)^T,\quad U=(\rho,\rho u,E)^T
$$

$$
R_s(t)=0.6(-t)^\alpha,\quad\alpha=1/\lambda,\quad \lambda\simeq1.3943607844,\quad t<0
$$

$$
\frac{d\bar U_i}{dt}=-\frac{A_{i+1/2}\widehat F_{i+1/2}-A_{i-1/2}\widehat F_{i-1/2}}{V_i}+\left(0,p_i\frac{\Delta A_i}{V_i},0\right)^T
$$

$$
\bar U_i^{\rm ref}=\frac{\int_{r_{i-1/2}}^{r_{i+1/2}}U_{\rm sim}(r,t)r^2\,dr}{(r_{i+1/2}^3-r_{i-1/2}^3)/3},\qquad p_i^{\rm ref}=p(\bar U_i^{\rm ref})
$$

### References and validation

The33 unit checks and55 gates over three refinements were fixed before execution and passed with warnings treated as errors. Checks cover the zero-sound-speed cold HLL branch, geometric static-pressure balance, shared-flux budgets, actual two-stage boundary times and raw failed-stage retention. Full-volume L1 is shown alongside the predetermined r>=0.8*Rs shock/nonzero-flow region, so cold inner gas does not hide active errors. Maximum density/pressure differences and the saved shock trajectory remain visible. The semi-analytic reference uses the pinned LANL ExactPack eigenvalue routine and ODE through a cached pre-collapse-only adapter. It is not an independently reimplemented similarity ODE; the separately implemented finite-volume Euler evolution is compared against that reference. Full-volume density L1 is0.02345/0.01339/0.007722 and pressure L1 is0.03277/0.01743/0.009477. Density L1 in the predetermined r>=0.8*Rs region also decreases:0.02414/0.01378/0.007948. The finest measured shock radius is0.530273 against similarity0.533989, about2.54 cells apart. The maximum scaled three-component budget residual is8.85e-16. Minimum internal energy and sound-speed-only roundoff guard evaluations are both0. The smooth-reference Euler finite-difference residual is8.24e-9 and finite-offset moving-jump residual4.40e-8. The older three-run execution with a newly computed similarity eigenvalue took about44.6 seconds on the original Mac. Public r2 passed all33 Linux tests in96.34 seconds, but its fixed-input runner timed out after the remaining23.31 seconds of the combined120-second test-plus-run budget. That failed replay and its sources are retained. The revision reuses the eigenvalue already obtained by actual ExactPack shooting, bound by SHA to its source and qualification, instead of shooting again in both normal processes. The critical-phase Cdiff residual and similarity ODE are freshly evaluated. Inputs, numerical criteria, Euler solver, fixed-input runner and120-second budget are unchanged. In the revision,33 unit tests and all three fixed inputs with55 gates completed sequentially within one120-second budget in about0.912s on the Mac. Initial,final,reference and saved-history arrays for all three grids were bit-identical to published r2, separately checking that reuse of the eigenvalue preserved the physical results.

### Limits

This is a short one-dimensional spherical verification away from collapse t=0. The singular origin, reflected branch, cylindrical geometry, other gammas and nonspherical perturbation stability are untested. Two-dimensional pictures map saved spherical shell means onto a meridional plane; they are not Cartesian2D evolution. The semi-analytic field is a numerically evaluated ODE/quadrature reference, not a closed-form exact cell average. Zero pressure is allowed in the cold upstream; cancellation-band negative internal energy density down to an absolute64eps is recorded. Sound-speed square-root guards only within that band have separate counts/minimum raw pressure and do not repair the state. No general nonlinear positivity theorem is claimed. Shock-position error in cell units does not decrease monotonically:1.13/2.27/2.54. Absolute radius error is about0.00665 for the first two grids and0.00372 for the finest. Density Linf differences0.258/0.271/0.266 and pressure Linf0.492/0.494/0.466 are also not monotonically decreasing. L1 reduction is not evidence that the discontinuity is pointwise resolved or that the collapse region converges.

### Stored measurements and decisions

```json
{
  "metrics": {
    "n": 512,
    "time": -0.85,
    "steps": 285,
    "density_l1": 0.00772161862650073,
    "pressure_l1": 0.00947688731818041,
    "active_density_l1": 0.007948322269523746,
    "active_pressure_l1": 0.009476887318180412,
    "density_linf": 0.26559799254635363,
    "pressure_linf": 0.4664641041357883,
    "maximum_velocity_error": 0.2918302634973315,
    "active_volume_fraction": 0.8145022392272949,
    "active_inner_radius": 0.4271911929633472,
    "shock_radius": 0.5302734375,
    "reference_shock_radius": 0.533988991204184,
    "shock_error_cells": 2.536484662056258,
    "maximum_history_shock_error_cells": 2.536484662056258,
    "minimum_density_all_stages": 1.0,
    "minimum_pressure_all_stages": 0.0,
    "minimum_internal_energy_all_stages": 0.0,
    "sound_speed_roundoff_guard_evaluations": 0,
    "minimum_pressure_at_sound_speed_guard": 0.0,
    "state_floor_count": 0,
    "rejected_steps": 0,
    "minimum_dt": 0.0004970499254967065,
    "maximum_dt": 0.000537015606799512,
    "reference_quadrature_density_l1": 4.607326285502161e-15,
    "reference_quadrature_pressure_l1": 8.295849629501113e-15,
    "initial_reference_quadrature_density_l1": 1.4522743666682576e-15,
    "initial_reference_quadrature_pressure_l1": 3.208009534299476e-15
  },
  "checks": {
    "all three fixed spherical runs completed": true,
    "N128: final time before collapse": true,
    "N128: strictly positive density all stages": true,
    "N128: minimum_internal_energy_all_stages": true,
    "N128: minimum_pressure_at_sound_speed_guard": true,
    "N128: state_floor_count": true,
    "N128: rejected_steps": true,
    "N128: mass discrete balance": true,
    "N128: radial momentum including geometric source discrete balance": true,
    "N128: energy discrete balance": true,
    "N128: reference_quadrature_density_l1": true,
    "N128: reference_quadrature_pressure_l1": true,
    "N128: initial_reference_quadrature_density_l1": true,
    "N128: initial_reference_quadrature_pressure_l1": true,
    "N128: maximum and trajectory diagnostics retained": true,
    "N256: final time before collapse": true,
    "N256: strictly positive density all stages": true,
    "N256: minimum_internal_energy_all_stages": true,
    "N256: minimum_pressure_at_sound_speed_guard": true,
    "N256: state_floor_count": true,
    "N256: rejected_steps": true,
    "N256: mass discrete balance": true,
    "N256: radial momentum including geometric source discrete balance": true,
    "N256: energy discrete balance": true,
    "N256: reference_quadrature_density_l1": true,
    "N256: reference_quadrature_pressure_l1": true,
    "N256: initial_reference_quadrature_density_l1": true,
    "N256: initial_reference_quadrature_pressure_l1": true,
    "N256: maximum and trajectory diagnostics retained": true,
    "N512: final time before collapse": true,
    "N512: strictly positive density all stages": true,
    "N512: minimum_internal_energy_all_stages": true,
    "N512: minimum_pressure_at_sound_speed_guard": true,
    "N512: state_floor_count": true,
    "N512: rejected_steps": true,
    "N512: mass discrete balance": true,
    "N512: radial momentum including geometric source discrete balance": true,
    "N512: energy discrete balance": true,
    "N512: reference_quadrature_density_l1": true,
    "N512: reference_quadrature_pressure_l1": true,
    "N512: initial_reference_quadrature_density_l1": true,
    "N512: initial_reference_quadrature_pressure_l1": true,
    "N512: maximum and trajectory diagnostics retained": true,
    "similarity qualification: maximum_scaled_euler_residual": true,
    "similarity qualification: maximum_scaled_jump_residual": true,
    "similarity exponent agrees with tabulated lambda": true,
    "finest density_l1": true,
    "finest pressure_l1": true,
    "finest active_density_l1": true,
    "finest active_pressure_l1": true,
    "finest shock_error_cells": true,
    "density_l1 decreases across the three grids": true,
    "active_density_l1 decreases across the three grids": true,
    "pressure_l1 decreases across the three grids": true,
    "last-pair active density L1 slope": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/guderley-implosion/index.json

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/guderley/atlas-guderley-2026-11-23-r3.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/guderley/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/guderley/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/guderley/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group.

### Sources and review scope

- G. Guderley (1942). Starke kugelige und zylindrische Verdichtungsstöße in der Nähe des Kugelmittelpunktes bzw. der Zylinderachse. https://raw.githubusercontent.com/lanl/ExactPack/9bacc477eb791e959c9621e771fc7a725db755fa/doc/source/references.rst; review_level=bibliographic attribution only: year/volume/first page in pinned ExactPack bibliography, title in Lazarus1981 publisher bibliography; original1942 article not inspected
  Historical original-problem attribution. Author/year/volume/first page302 were checked in the pinned ExactPack bibliography and the title in the Lazarus1981 publisher references. The original1942 text was not inspected and is not claimed as the directly transcribed source of the present fields or measurements.
- Scott D. Ramsey, James R. Kamm and John H. Bolstad (2012). The Guderley problem revisited. https://laro.lanl.gov/esploro/outputs/journalArticle/The-Guderley-problem-revisited/9916364702403761; review_level=primary institutional bibliographic record and abstract; actual implementation equations reviewed in pinned ExactPack source, not full original paper
  The LANL record and abstract distinguish the convergence exponent from the reflected trajectory eigenvalue. This is not a claim to have read the entire paper or reproduced its PDE experiment; the present field is constructed using the pinned ExactPack source.
- Roger B. Lazarus (1981). Self-Similar Solutions for Converging Shocks and Collapsing Cavities. https://epubs.siam.org/doi/10.1137/0718022; review_level=publisher bibliographic record/abstract plus equations2.5,2.8,2.9 and sphericalTable6.5 as explicitly transcribed in pinned ExactPack; original full text not inspected
  Checked the publisher record/abstract and the explicitly attributed equations/table in ExactPack. The tabulated lambda1.3943607838 is the value transcribed in that code, not an independent retranscription of the original table.
- R. F. Chisnell (1998). An analytic description of converging shock waves. https://www.cambridge.org/core/journals/journal-of-fluid-mechanics/article/abs/an-analytic-description-of-converging-shock-waves/1D3D7014FF4C6297A5F6DC9BCFDBE0E8; review_level=publisher bibliographic record/abstract and equation3.1 implementation/comments in actual pinned ExactPack eexp source
  Checked the publisher record/abstract and the critical-point phase matching and equation3.1 implementation in ExactPack eexp. The exponent is computed through that eigenvalue routine rather than fixed by dimensional analysis.
- Jasper Thrussell and Jim Michael Ferguson (2023). ExactPack: A python library of exact analytic solutions. https://www.osti.gov/servlets/purl/2204208; review_level=primary OSTI accepted manuscript/search text; software metadata and Guderley registry; selected actual source files pinned separately
  Cites the ExactPack software paper and its Guderley solver listing. The paper version1.7.5 is distinguished from the exact source commit used here, whose source, SHA receipts and BSD license are retained.
- Los Alamos National Laboratory / ExactPack contributors (2025). ExactPack Guderley solver, pinned source. https://github.com/lanl/ExactPack/tree/9bacc477eb791e959c9621e771fc7a725db755fa/exactpack/solvers/guderley; review_level=selected source files and license inspected; eexp,ramsey.state/g,interp_laz and official test fixtures; actual execution recorded separately
  Inspected pinned eexp, the pre-collapse ODE/state, transcribed tables, official regression values and BSD3 terms. This is not a claim to have run the complete ExactPack suite; actual reference execution is recorded separately.

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
