# Shallow water: topography, lakes and dry beds

Check shallow-water bed sources and hydrostatic reconstruction with wet/emerged lakes and a SWASHES steady Bernoulli flow. A separate flat-bed Ritter dam break tests genuinely dry states, conservation budgets and a fixed-depth front.

These additional validation supplements are managed separately from the common 22-example registry. Receipts cover independent ZIP extraction, tests and every fixed input within each group. Changes of settings, methods or step sizes do not add independent physical problems.

## SWASHES topographic flow: lakes and nonzero steady discharge

Check two lake equilibria separately from nonzero subcritical flow, distinguishing lake preservation from moving-flow discretization error.

**Methods used**

- [Godunov-type finite volumes](https://hrkoyama.github.io/numerical-methods-atlas/methods/godunov/?lang=en) (`godunov`)
- [HLL](https://hrkoyama.github.io/numerical-methods-atlas/methods/hll/?lang=en) (`hll`)
- [Forward Euler](https://hrkoyama.github.io/numerical-methods-atlas/methods/forward-euler/?lang=en) (`forward-euler`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/swashes-topography/?lang=en#swashes-topography-en-algorithm)

Hydrostatic reconstruction, shared HLL flux and left/right pressure corrections discretize the bed source; forward Euler and face CFL .4. Lakes use reflecting walls. Moving subcritical boundaries impose upstream q and downstream h, extrapolating the other datum. No state floors, clipping or retries. Algebraically factor HLL updates into nonnegative water packets; advected momentum uses those same rounded masses, without a small-depth threshold or subsequent repair.

$$
\partial_t h+\partial_x q=0,\qquad \partial_tq+\partial_x(q^2/h+gh^2/2)=-gh\partial_xz
$$

$$
z^*=\max(z_L,z_R),\quad h_K^*=\max(0,h_K+z_K-z^*),\quad q_K^*=h_K^*u_K
$$

$$
F_K=F_{\mathrm{HLL}}(U_L^*,U_R^*)+(0,\tfrac12g(h_K^2-(h_K^*)^2))^T
$$

$$
q=4.42,\quad h+z+q^2/(2gh^2)=2+4.42^2/(8g),\quad h>(q^2/g)^{1/3}
$$

- [Shallow-water equations with bed source](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#shallow-water-bed-en) (`shallow-water-bed`)

1D, g=9.81, L=25m, compact parabolic bed z=.2-.05(x-10)^2 on8<x<12. Lakes at surface .5/.1m use200 cells. Moving flow q=4.42m2/s, downstream h=2m uses100/200/400 cells to2s. Initialize the steady branch, not the published rest-to-steady transient.


**Problem figure**

![SWASHES topographic flow: lakes and nonzero steady discharge: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/results/swashes-topography.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[SWASHES lakes and steady shallow flow over topography](https://hrkoyama.github.io/numerical-methods-atlas/problems/swashes-topography/?lang=en) (`swashes-topography`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/swashes-topography/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/swashes-topography/?lang=en#swashes-topography-en-validation)

Freeze31 unit checks and eight group runs. Record lake drift, every FE minimum depth, shared-flux/bed-impulse budgets, conservative-mean L1 errors and three-grid ratios. Qualify an independent Bernoulli bisection by energy and branch checks.

- [Lake at rest: wet and emerged equilibrium over represented bed](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-lake-at-rest-bed-en) (`lake-at-rest-bed`; Same-problem reference · Analytic reference)

Exact lake balance concerns the represented cell bed. Moving steady states retain finite-time numerical error. Transcritical flows, jumps, friction, rain, infiltration, 2D flow and fully discrete entropy stability are outside scope.

- [SWASHES steady flow: subcritical Bernoulli root](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-swashes-bernoulli-en) (`swashes-bernoulli`; Same-problem reference · Semi-analytic reference)

Exact lake balance concerns the represented cell bed. Moving steady states retain finite-time numerical error. Transcritical flows, jumps, friction, rain, infiltration, 2D flow and fully discrete entropy stability are outside scope.
### Assumptions, units and boundaries

1D, g=9.81, L=25m, compact parabolic bed z=.2-.05(x-10)^2 on8<x<12. Lakes at surface .5/.1m use200 cells. Moving flow q=4.42m2/s, downstream h=2m uses100/200/400 cells to2s. Initialize the steady branch, not the published rest-to-steady transient.

**Editorial clarification**

Exact lake balance concerns the represented cell bed. Moving steady states retain finite-time numerical error. Transcritical flows, jumps, friction, rain, infiltration, 2D flow and fully discrete entropy stability are outside scope. The final revision passed31 unit checks and all109 gates over8 group runs. The finest moving steady case,N400, has depthL1 about.0249108 and relative depthL1 about.000505933. Represented-bed lake balance, finite-time moving steady errors and dry-bed front errors are retained separately.

### Adopted numerical method

Hydrostatic reconstruction, shared HLL flux and left/right pressure corrections discretize the bed source; forward Euler and face CFL .4. Lakes use reflecting walls. Moving subcritical boundaries impose upstream q and downstream h, extrapolating the other datum. No state floors, clipping or retries. Algebraically factor HLL updates into nonnegative water packets; advected momentum uses those same rounded masses, without a small-depth threshold or subsequent repair.

$$
\partial_t h+\partial_x q=0,\qquad \partial_tq+\partial_x(q^2/h+gh^2/2)=-gh\partial_xz
$$

$$
z^*=\max(z_L,z_R),\quad h_K^*=\max(0,h_K+z_K-z^*),\quad q_K^*=h_K^*u_K
$$

$$
F_K=F_{\mathrm{HLL}}(U_L^*,U_R^*)+(0,\tfrac12g(h_K^2-(h_K^*)^2))^T
$$

$$
q=4.42,\quad h+z+q^2/(2gh^2)=2+4.42^2/(8g),\quad h>(q^2/g)^{1/3}
$$

### References and validation

Freeze31 unit checks and eight group runs. Record lake drift, every FE minimum depth, shared-flux/bed-impulse budgets, conservative-mean L1 errors and three-grid ratios. Qualify an independent Bernoulli bisection by energy and branch checks.

### Limits

Exact lake balance concerns the represented cell bed. Moving steady states retain finite-time numerical error. Transcritical flows, jumps, friction, rain, infiltration, 2D flow and fully discrete entropy stability are outside scope.

### Stored measurements and decisions

```json
{
  "metrics": {
    "n": 400,
    "steps": 536,
    "time": 2.0,
    "depth_l1": 0.024910750612742227,
    "momentum_l1": 0.060087246887864654,
    "relative_depth_l1": 0.0005059326932762419,
    "relative_momentum_l1": 0.0005437759899354242,
    "depth_linf": 0.006424726192375774,
    "minimum_depth": 1.7071673523958315,
    "maximum_depth": 2.0053503464023863,
    "maximum_velocity": 2.5885739653660536,
    "maximum_courant": 0.4,
    "maximum_step_mass_defect": 8.624754336295616e-15,
    "maximum_step_momentum_defect": 1.7091399469478224e-14,
    "minimum_staying_coefficient": 0.7344646405854746,
    "maximum_total_mass_defect": 8.038448654658321e-14,
    "maximum_total_momentum_defect": 3.8524326957667387e-13,
    "mass_change": 1.7453826262892047e-05,
    "boundary_mass_change": 1.745382627041232e-05,
    "bed_momentum_impulse": -0.02828240710978647,
    "initial_dry_cells": 0,
    "final_dry_cells": 0,
    "newly_wet_cells": 0,
    "all_saved_values_finite": true,
    "depth_floor_count": 0,
    "state_clip_count": 0,
    "rejected_steps": 0,
    "retries": 0
  },
  "checks": {
    "lake-immersed: maximum_step_mass_defect": true,
    "lake-immersed: maximum_step_momentum_defect": true,
    "lake-immersed: maximum_total_mass_defect": true,
    "lake-immersed: maximum_total_momentum_defect": true,
    "lake-immersed: nonnegative depth": true,
    "lake-immersed: finite arrays": true,
    "lake-immersed: face CFL": true,
    "lake-immersed: no repairs or retries": true,
    "lake-immersed: five exact output times": true,
    "lake-immersed: maximum_equilibrium_depth_drift": true,
    "lake-immersed: maximum_equilibrium_discharge": true,
    "lake-emerged: maximum_step_mass_defect": true,
    "lake-emerged: maximum_step_momentum_defect": true,
    "lake-emerged: maximum_total_mass_defect": true,
    "lake-emerged: maximum_total_momentum_defect": true,
    "lake-emerged: nonnegative depth": true,
    "lake-emerged: finite arrays": true,
    "lake-emerged: face CFL": true,
    "lake-emerged: no repairs or retries": true,
    "lake-emerged: five exact output times": true,
    "lake-emerged: maximum_equilibrium_depth_drift": true,
    "lake-emerged: maximum_equilibrium_discharge": true,
    "subcritical-n100: maximum_step_mass_defect": true,
    "subcritical-n100: maximum_step_momentum_defect": true,
    "subcritical-n100: maximum_total_mass_defect": true,
    "subcritical-n100: maximum_total_momentum_defect": true,
    "subcritical-n100: nonnegative depth": true,
    "subcritical-n100: finite arrays": true,
    "subcritical-n100: face CFL": true,
    "subcritical-n100: no repairs or retries": true,
    "subcritical-n100: five exact output times": true,
    "subcritical-n200: maximum_step_mass_defect": true,
    "subcritical-n200: maximum_step_momentum_defect": true,
    "subcritical-n200: maximum_total_mass_defect": true,
    "subcritical-n200: maximum_total_momentum_defect": true,
    "subcritical-n200: nonnegative depth": true,
    "subcritical-n200: finite arrays": true,
    "subcritical-n200: face CFL": true,
    "subcritical-n200: no repairs or retries": true,
    "subcritical-n200: five exact output times": true,
    "subcritical-n400: maximum_step_mass_defect": true,
    "subcritical-n400: maximum_step_momentum_defect": true,
    "subcritical-n400: maximum_total_mass_defect": true,
    "subcritical-n400: maximum_total_momentum_defect": true,
    "subcritical-n400: nonnegative depth": true,
    "subcritical-n400: finite arrays": true,
    "subcritical-n400: face CFL": true,
    "subcritical-n400: no repairs or retries": true,
    "subcritical-n400: five exact output times": true,
    "subcritical finest relative_depth_l1": true,
    "subcritical relative_depth_l1 refinement 1": true,
    "subcritical relative_depth_l1 refinement 2": true,
    "subcritical finest relative_momentum_l1": true,
    "subcritical relative_momentum_l1 refinement 1": true,
    "subcritical relative_momentum_l1 refinement 2": true,
    "reference: Bernoulli energy constant": true,
    "reference: subcritical branch": true,
    "reference: Gauss8 vs Gauss16 conservative means": true,
    "reference: Ritter total mass": true,
    "reference: Ritter finite difference PDE residual": true,
    "reference: exact dry branch": true,
    "all fixed runs completed": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/swashes-topography/index.json

![Preview of represented bed, saved FV surfaces and moving-steady errors.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/results/swashes-topography-preview.png)

Preview of represented bed, saved FV surfaces and moving-steady errors.

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/atlas-shallow-water-2026-11-23.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group.

Input and validation protocol history: https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/protocol-history.json

https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/attempts/01/source/inputs.json

### Sources and review scope

- O. Delestre et al. (2013). SWASHES: a compilation of shallow water analytic solutions for hydraulic and environmental studies. https://arxiv.org/pdf/1110.0288; review_level=selected-equations-and-fixed-inputs
- E. Audusse, F. Bouchut, M.-O. Bristeau, R. Klein, B. Perthame (2004). A Fast and Stable Well-Balanced Scheme with Hydrostatic Reconstruction for Shallow Water Flows. https://epubs.siam.org/doi/abs/10.1137/S1064827503431090; review_level=bibliography-and-author-follow-up
- E. Audusse, F. Bouchut, M.-O. Bristeau, J. Sainte-Marie (2016). Kinetic entropy inequality and hydrostatic reconstruction scheme for the Saint-Venant system. https://arxiv.org/pdf/1409.3825; review_level=selected-scheme-equations
- Institut Denis Poisson / SWASHES authors (n.d.). SWASHES project page. https://www.idpoisson.fr/en/swashes-es/; review_level=official-project-scope-and-rights

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## Dry-bed dam break: actual wetting and dry states

Start the right half at exactly h=q=0 and compare wetting-front advance, conservation and conservative errors with the Ritter analytic solution.

**Methods used**

- [Godunov-type finite volumes](https://hrkoyama.github.io/numerical-methods-atlas/methods/godunov/?lang=en) (`godunov`)
- [HLL](https://hrkoyama.github.io/numerical-methods-atlas/methods/hll/?lang=en) (`hll`)
- [Forward Euler](https://hrkoyama.github.io/numerical-methods-atlas/methods/forward-euler/?lang=en) (`forward-euler`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/dry-bed-dam-break/?lang=en#dry-bed-dam-break-en-algorithm)

The FV solver supports h=q=0 directly; one-sided dry HLL speeds use u-c/u+2c and their reflection. Forward Euler at face CFL .4 records every minimum and shared-flux budget without raising cell depths. Algebraically factor HLL updates into nonnegative water packets; advected momentum uses those same rounded masses, without a small-depth threshold or subsequent repair.

$$
c_L=\sqrt{gh_L},\quad x_A=x_0-c_Lt,\quad x_B=x_0+2c_Lt
$$

$$
h=(2c_L-(x-x_0)/t)^2/(9g),\quad u=\tfrac23((x-x_0)/t+c_L)\quad (x_A<x<x_B)
$$

$$
\bar U_i^{\mathrm{ref}}=\Delta x^{-1}\int_{C_i}(h,hu)^Tdx,\quad x_{.001}=x_B-3t\sqrt{g(0.001)}
$$

- [Shallow-water equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#shallow-water-en) (`shallow-water`)

Flat frictionless bed on[-10,10]m, dam0, hL=1m/hR=0, initial velocity0, g=9.81, t=.5s,1600/3200/6400 cells. The Ritter formula uses an explicit rescaling distinct from the paper numerical example.


**Problem figure**

![Dry-bed dam break: actual wetting and dry states: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/results/dry-bed-dam-break.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Ritter dam break onto a dry bed](https://hrkoyama.github.io/numerical-methods-atlas/problems/dry-bed-dam-break/?lang=en) (`dry-bed-dam-break`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/dry-bed-dam-break/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/dry-bed-dam-break/?lang=en#dry-bed-dam-break-en-validation)

Record all FE minima, newly wetted and remaining dry cells, boundary-aware mass/momentum budgets, and L1 refinement. Split Gauss8 h/hu references are qualified by Gauss16, mass and PDE identities. Diagnose the rightmost cell center with mean h>=.001m. Depth acceptance uses the original fixed5m2 reference mass, preventing domain extension from weakening the criterion; full-domain relativeL1 remains a separate diagnostic.

- [Ritter dry-bed dam break: dedicated g9.81 cell-mean reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-ritter-dry-bed-en) (`ritter-dry-bed`; Same-problem reference · Analytic reference)

The .001m mean-depth contour differs from the analytic support edge, which is reported separately. These fixed runs test wetting of initially dry cells. Retreating shorelines, re-drying cycles, real floods, friction and moving fronts over topography are outside scope. The initial100/200/400-cell [-5,5]m attempt passed28 tests and105/109 gates; three retained-dry-cell gates and the .3960m>.25m contour error failed. All original records remain archived; revision2 enlarges/refines the input without changing acceptance. Revision2 then stopped on a binary64 subnormal-tail dry-momentum artifact. Revision3 factors the same HLL update into water packets and adds three regression/equivalence tests; the original28 remain unchanged.

- [Shallow water / dry-bed fan](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-swe-dry-bed-en) (`swe-dry-bed`; Related-model reference · Analytic reference)

Retain the historical dry-bed reference gravity/domain/time unchanged. The new g9.81,[-10,10],t.5 computation uses its dedicated Ritter reference.
### Assumptions, units and boundaries

Flat frictionless bed on[-10,10]m, dam0, hL=1m/hR=0, initial velocity0, g=9.81, t=.5s,1600/3200/6400 cells. The Ritter formula uses an explicit rescaling distinct from the paper numerical example.

**Editorial clarification**

The .001m mean-depth contour differs from the analytic support edge, which is reported separately. These fixed runs test wetting of initially dry cells. Retreating shorelines, re-drying cycles, real floods, friction and moving fronts over topography are outside scope. The initial100/200/400-cell [-5,5]m attempt passed28 tests and105/109 gates; three retained-dry-cell gates and the .3960m>.25m contour error failed. All original records remain archived; revision2 enlarges/refines the input without changing acceptance. Revision2 then stopped on a binary64 subnormal-tail dry-momentum artifact. Revision3 factors the same HLL update into water packets and adds three regression/equivalence tests; the original28 remain unchanged. Revision3 passed108/109 gates but failed the .27415m>.25m contour criterion. Revision4 refines only Ritter grids to1600/3200/6400. Relative depth L1 is normalized by domain reference mass; absolute L1 is also retained because the domain changed between revisions1 and2. Final revision4 uses1600/3200/6400cells on[-10,10]m at t.5s and passed31 unit checks and all109 group gates. Acceptance depthL1 retains the original fixed reference mass5m², giving finest.001773819 and absolute depthL1.008869095m². Normalization by the enlarged-domain reference mass10m² gives.000886909 as a separate diagnostic, never an easier acceptance criterion. Relative momentumL1 is.009590172; the depth.001m contour error is.2069613m<.25m and1679 genuinely dry cells remain. All three earlier failures are retained; depth floors,state clips and retries are zero.

### Adopted numerical method

The FV solver supports h=q=0 directly; one-sided dry HLL speeds use u-c/u+2c and their reflection. Forward Euler at face CFL .4 records every minimum and shared-flux budget without raising cell depths. Algebraically factor HLL updates into nonnegative water packets; advected momentum uses those same rounded masses, without a small-depth threshold or subsequent repair.

$$
c_L=\sqrt{gh_L},\quad x_A=x_0-c_Lt,\quad x_B=x_0+2c_Lt
$$

$$
h=(2c_L-(x-x_0)/t)^2/(9g),\quad u=\tfrac23((x-x_0)/t+c_L)\quad (x_A<x<x_B)
$$

$$
\bar U_i^{\mathrm{ref}}=\Delta x^{-1}\int_{C_i}(h,hu)^Tdx,\quad x_{.001}=x_B-3t\sqrt{g(0.001)}
$$

### References and validation

Record all FE minima, newly wetted and remaining dry cells, boundary-aware mass/momentum budgets, and L1 refinement. Split Gauss8 h/hu references are qualified by Gauss16, mass and PDE identities. Diagnose the rightmost cell center with mean h>=.001m. Depth acceptance uses the original fixed5m2 reference mass, preventing domain extension from weakening the criterion; full-domain relativeL1 remains a separate diagnostic.

### Limits

The .001m mean-depth contour differs from the analytic support edge, which is reported separately. These fixed runs test wetting of initially dry cells. Retreating shorelines, re-drying cycles, real floods, friction and moving fronts over topography are outside scope. The initial100/200/400-cell [-5,5]m attempt passed28 tests and105/109 gates; three retained-dry-cell gates and the .3960m>.25m contour error failed. All original records remain archived; revision2 enlarges/refines the input without changing acceptance. Revision2 then stopped on a binary64 subnormal-tail dry-momentum artifact. Revision3 factors the same HLL update into water packets and adds three regression/equivalence tests; the original28 remain unchanged. Revision3 passed108/109 gates but failed the .27415m>.25m contour criterion. Revision4 refines only Ritter grids to1600/3200/6400. Relative depth L1 is normalized by domain reference mass; absolute L1 is also retained because the domain changed between revisions1 and2.

### Stored measurements and decisions

```json
{
  "metrics": {
    "n": 6400,
    "steps": 2263,
    "time": 0.5,
    "depth_l1": 0.00886909478548199,
    "momentum_l1": 0.02351989621706402,
    "relative_depth_l1": 0.0008869094785479971,
    "relative_momentum_l1": 0.009590171750074893,
    "depth_linf": 0.018378452319254834,
    "minimum_depth": 0.0,
    "maximum_depth": 1.0,
    "maximum_velocity": 5.618969641557241,
    "maximum_courant": 0.4000000000000001,
    "maximum_step_mass_defect": 2.175706973437462e-15,
    "maximum_step_momentum_defect": 2.47198095326695e-17,
    "minimum_staying_coefficient": 0.6038337128225417,
    "maximum_total_mass_defect": 4.973799150320701e-14,
    "maximum_total_momentum_defect": 7.549516567451064e-15,
    "mass_change": -7.904787935332912e-15,
    "boundary_mass_change": 0.0,
    "bed_momentum_impulse": 0.0,
    "initial_dry_cells": 3200,
    "final_dry_cells": 1679,
    "newly_wet_cells": 1521,
    "all_saved_values_finite": true,
    "depth_floor_count": 0,
    "state_clip_count": 0,
    "rejected_steps": 0,
    "retries": 0,
    "front_depth_threshold": 0.001,
    "numerical_threshold_front": 2.7765625000000007,
    "analytic_threshold_front": 2.9835237865001925,
    "analytic_support_front": 3.132091952673165,
    "threshold_front_error": 0.20696128650019174,
    "depth_acceptance_reference_mass": 5.0,
    "fixed_reference_relative_depth_l1": 0.001773818957096398
  },
  "checks": {
    "ritter-n1600: maximum_step_mass_defect": true,
    "ritter-n1600: maximum_step_momentum_defect": true,
    "ritter-n1600: maximum_total_mass_defect": true,
    "ritter-n1600: maximum_total_momentum_defect": true,
    "ritter-n1600: nonnegative depth": true,
    "ritter-n1600: finite arrays": true,
    "ritter-n1600: face CFL": true,
    "ritter-n1600: no repairs or retries": true,
    "ritter-n1600: five exact output times": true,
    "ritter-n1600: actual wetting": true,
    "ritter-n1600: dry cells retained": true,
    "ritter-n3200: maximum_step_mass_defect": true,
    "ritter-n3200: maximum_step_momentum_defect": true,
    "ritter-n3200: maximum_total_mass_defect": true,
    "ritter-n3200: maximum_total_momentum_defect": true,
    "ritter-n3200: nonnegative depth": true,
    "ritter-n3200: finite arrays": true,
    "ritter-n3200: face CFL": true,
    "ritter-n3200: no repairs or retries": true,
    "ritter-n3200: five exact output times": true,
    "ritter-n3200: actual wetting": true,
    "ritter-n3200: dry cells retained": true,
    "ritter-n6400: maximum_step_mass_defect": true,
    "ritter-n6400: maximum_step_momentum_defect": true,
    "ritter-n6400: maximum_total_mass_defect": true,
    "ritter-n6400: maximum_total_momentum_defect": true,
    "ritter-n6400: nonnegative depth": true,
    "ritter-n6400: finite arrays": true,
    "ritter-n6400: face CFL": true,
    "ritter-n6400: no repairs or retries": true,
    "ritter-n6400: five exact output times": true,
    "ritter-n6400: actual wetting": true,
    "ritter-n6400: dry cells retained": true,
    "ritter finest relative_depth_l1": true,
    "ritter relative_depth_l1 refinement 1": true,
    "ritter relative_depth_l1 refinement 2": true,
    "ritter finest relative_momentum_l1": true,
    "ritter relative_momentum_l1 refinement 1": true,
    "ritter relative_momentum_l1 refinement 2": true,
    "finest threshold front error": true,
    "reference: Bernoulli energy constant": true,
    "reference: subcritical branch": true,
    "reference: Gauss8 vs Gauss16 conservative means": true,
    "reference: Ritter total mass": true,
    "reference: Ritter finite difference PDE residual": true,
    "reference: exact dry branch": true,
    "all fixed runs completed": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/dry-bed-dam-break/index.json

![Preview from actual saved 1D shallow-water depth/discharge arrays. The space-time panel shows five saved times, not a 2D flow.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/results/dry-bed-dam-break-preview.png)

Preview from actual saved 1D shallow-water depth/discharge arrays. The space-time panel shows five saved times, not a 2D flow.

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/atlas-shallow-water-2026-11-23.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group.

Input and validation protocol history: https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/protocol-history.json

https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/attempts/01/source/inputs.json

### Sources and review scope

- O. Delestre et al. (2013). SWASHES: a compilation of shallow water analytic solutions for hydraulic and environmental studies. https://arxiv.org/pdf/1110.0288; review_level=selected-equations-and-fixed-inputs
- E. Audusse, F. Bouchut, M.-O. Bristeau, R. Klein, B. Perthame (2004). A Fast and Stable Well-Balanced Scheme with Hydrostatic Reconstruction for Shallow Water Flows. https://epubs.siam.org/doi/abs/10.1137/S1064827503431090; review_level=bibliography-and-author-follow-up
- E. Audusse, F. Bouchut, M.-O. Bristeau, J. Sainte-Marie (2016). Kinetic entropy inequality and hydrostatic reconstruction scheme for the Saint-Venant system. https://arxiv.org/pdf/1409.3825; review_level=selected-scheme-equations
- Institut Denis Poisson / SWASHES authors (n.d.). SWASHES project page. https://www.idpoisson.fr/en/swashes-es/; review_level=official-project-scope-and-rights

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
