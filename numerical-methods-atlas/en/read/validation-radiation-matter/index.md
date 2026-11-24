# Non-equilibrium radiation: distinct diffusion and transport

Separate Su-Olson diffusion and transport by normalization,boundaries and sources,with an additional matched periodic Fourier control for the resolved diffusion limit.

These additional validation supplements are managed separately from the common 22-example registry. Receipts cover independent ZIP extraction, tests and every fixed input within each group. Changes of settings, methods or step sizes do not add independent physical problems.

## Su–Olson1996 non-equilibrium diffusion

Advance actual radiation/material fields with the Marshak boundary and compare with independently qualified pinned ExactPack integrals.

**Methods used**

- [Radiation transport and moment methods](https://hrkoyama.github.io/numerical-methods-atlas/methods/radiation-transport/?lang=en) (`radiation-transport`)
- [Backward Euler](https://hrkoyama.github.io/numerical-methods-atlas/methods/backward-euler/?lang=en) (`backward-euler`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-diffusion1996/?lang=en#su-olson-diffusion1996-en-algorithm)

Conservative FV/backwardEuler with opposite exchange sources coupled by a shared Schur complement and Robin half-cell resistance beta+h/2. Analytic nonunitepsilon.25/2controls exercise the same exchange operators.

$$
\epsilon u_\tau-u_{xx}=v-u,\quad v_\tau=u-v
$$

$$
u(0,\tau)-\frac2{\sqrt3}u_x(0,\tau)=1
$$

$$
\epsilon=4a/\alpha,\quad e_m/E_0=v/\epsilon,\quad \mathcal E=\epsilon u+v
$$

- [Su–Olson1996 non-equilibrium diffusion and material exchange](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#non-equilibrium-diffusion-exchange-en) (`non-equilibrium-diffusion-exchange`)

Nondimensionalepsilon1,x0..16,initialu=v0,leftRobin inflow/right0;128/256/512cells plus half-step/domain24probes.


**Problem figure**

![Su–Olson1996 non-equilibrium diffusion: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/results/su-olson-diffusion1996.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Su–Olson1996 non-equilibrium diffusion](https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-diffusion1996/?lang=en) (`su-olson-diffusion1996`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-diffusion1996/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-diffusion1996/?lang=en#su-olson-diffusion1996-en-validation)

The independent54check reference study is shared with transport. Five primary runs separate u/vreferenceerror,all-step capacity-weighted budgets/positivity,time and finite-domain sensitivity.

- [Su–Olson1996 diffusion: pinned independent integral evaluator](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-su-olson-diffusion1996-en) (`su-olson-diffusion1996`; Same-problem reference · Semi-analytic reference)

This1996diffusion model is distinct from1997angular transport. Original paper fulltext unread;officialsoftware selected values qualified. Direct dimensionless functions avoid ambiguous mass-opacity physical-wrapper units.
### Assumptions, units and boundaries

Nondimensionalepsilon1,x0..16,initialu=v0,leftRobin inflow/right0;128/256/512cells plus half-step/domain24probes.

**Editorial clarification**

This1996diffusion model is distinct from1997angular transport. Original paper fulltext unread;officialsoftware selected values qualified. Direct dimensionless functions avoid ambiguous mass-opacity physical-wrapper units.

### Adopted numerical method

Conservative FV/backwardEuler with opposite exchange sources coupled by a shared Schur complement and Robin half-cell resistance beta+h/2. Analytic nonunitepsilon.25/2controls exercise the same exchange operators.

$$
\epsilon u_\tau-u_{xx}=v-u,\quad v_\tau=u-v
$$

$$
u(0,\tau)-\frac2{\sqrt3}u_x(0,\tau)=1
$$

$$
\epsilon=4a/\alpha,\quad e_m/E_0=v/\epsilon,\quad \mathcal E=\epsilon u+v
$$

### References and validation

The independent54check reference study is shared with transport. Five primary runs separate u/vreferenceerror,all-step capacity-weighted budgets/positivity,time and finite-domain sensitivity.

### Limits

This1996diffusion model is distinct from1997angular transport. Original paper fulltext unread;officialsoftware selected values qualified. Direct dimensionless functions avoid ambiguous mass-opacity physical-wrapper units.

### Stored measurements and decisions

```json
{
  "metrics": {
    "completed_primary_runs": 5,
    "reference_scope": "independent official diffusion integrals",
    "capacity_controls": [
      {
        "epsilon": 0.25,
        "method": "diffusion",
        "error": 0.00019032949653130515,
        "budget": 5.984102102729594e-14
      },
      {
        "epsilon": 0.25,
        "method": "transport",
        "error": 3.181825272147165e-07,
        "budget": 3.3306690738754696e-16
      },
      {
        "epsilon": 2.0,
        "method": "diffusion",
        "error": 0.000154177848556869,
        "budget": 7.460698725481052e-14
      },
      {
        "epsilon": 2.0,
        "method": "transport",
        "error": 7.721428540996556e-08,
        "budget": 1.199040866595169e-14
      }
    ]
  },
  "checks": {
    "su-olson-diffusion1996-n128/finite-positive": true,
    "su-olson-diffusion1996-n128/energy-budget": true,
    "su-olson-diffusion1996-n128/fixed-final-time": true,
    "su-olson-diffusion1996-n256/finite-positive": true,
    "su-olson-diffusion1996-n256/energy-budget": true,
    "su-olson-diffusion1996-n256/fixed-final-time": true,
    "su-olson-diffusion1996-n512/finite-positive": true,
    "su-olson-diffusion1996-n512/energy-budget": true,
    "su-olson-diffusion1996-n512/fixed-final-time": true,
    "su-olson-diffusion1996-half-dt/finite-positive": true,
    "su-olson-diffusion1996-half-dt/energy-budget": true,
    "su-olson-diffusion1996-half-dt/fixed-final-time": true,
    "su-olson-diffusion1996-far-domain/finite-positive": true,
    "su-olson-diffusion1996-far-domain/energy-budget": true,
    "su-olson-diffusion1996-far-domain/fixed-final-time": true,
    "refinement/1": true,
    "refinement/2": true,
    "finest-independent-rms": true,
    "finest-independent-linf": true,
    "separate-time-sensitivity": true,
    "finite-domain-sensitivity": true,
    "capacity/0.25/diffusion/error": true,
    "capacity/0.25/diffusion/budget": true,
    "capacity/0.25/transport/error": true,
    "capacity/0.25/transport/budget": true,
    "capacity/2.0/diffusion/error": true,
    "capacity/2.0/diffusion/budget": true,
    "capacity/2.0/transport/error": true,
    "capacity/2.0/transport/budget": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-diffusion1996/index.json

![Scientific preview from the actual saved numerical fields.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/results/su-olson-diffusion1996-preview.png)

Scientific preview from the actual saved numerical fields.

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/atlas-radiation-matter-2026-11-24-r2.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- LANL ExactPack developers;Timmes implementation provenance (2023). ExactPack1.7.5SuOlson pinned independent diffusion solution. https://github.com/lanl/ExactPack/tree/8718b61f281a9744ea7a3820c51800915e4636e9/exactpack/solvers/suolson; review_level=primary-official-software-full-three-module-text-and-qualified-selected-values
Read doc55/wrapper41/Timmes348lines;original1996paper abstract only. Serial original/tight selected integrals and independent PDE/Robin qualifiers passed before main. FullExactPack/base/libraries not audited.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## Su–Olson transport with an independently published analytical table

Evolve actual signed-angle transport/material exchange and compare with pinned analytical benchmark tables provided by the2023primary author.

**Methods used**

- [Radiation transport and moment methods](https://hrkoyama.github.io/numerical-methods-atlas/methods/radiation-transport/?lang=en) (`radiation-transport`)
- [Upwind finite differences](https://hrkoyama.github.io/numerical-methods-atlas/methods/upwind/?lang=en) (`upwind`)
- [Heun / SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en) (`heun`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-transport1997/?lang=en#su-olson-transport1997-en-algorithm)

Full signed-angle upwind FV/SSPRK2 advancesIandV. WithI=2U,E=halfangularintegral,the weightedbudgetisepsilonE+V;nodiffusionsubstitution. Only the thick-limit control constructs the same upwind operator from actual real cos/sin responses and evolves one Fourier mode by an exact-time matrix exponential.

$$
\epsilon I_\tau+\mu I_x+I=V+Q,\quad V_\tau=E-V
$$

$$
E=\frac12\int_{-1}^1I\,d\mu,\quad I=2U,\quad\mathcal E=\epsilon E+V
$$

$$
Q=\mathbf1_{|x|<1/2}\mathbf1_{0<\tau<10}
$$

$$
\epsilon I_t+\mu I_x=\kappa(V-I),\quad V_t=\kappa(E-V),\quad x\in[0,2\pi)
$$

$$
D_{\rm rad}=\frac1{3\kappa},\quad D_{\rm eff}=\frac1{3\kappa(\epsilon+1)},\quad t=\kappa s
$$

$$
E_D=V_D=1+A_N e^{-s/[3(\epsilon+1)]}\cos x,\quad F_D=-\frac1{3\kappa}\partial_x E_D
$$

- [Static grey radiative transfer,scattering and linear exchange](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#static-grey-transfer-en) (`static-grey-transfer`)

The main benchmark uses1997-type radiation/material transport. The heat equation is a limiting companion for separate periodic Fourier controls with E approximately V and diffusivity1/[3kappa(epsilon+1)],not the1996Marshak boundary problem or an exact solution of full transport.

- [Heat / diffusion equation](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#heat-en) (`heat`)

The main benchmark uses1997-type radiation/material transport. The heat equation is a limiting companion for separate periodic Fourier controls with E approximately V and diffusivity1/[3kappa(epsilon+1)],not the1996Marshak boundary problem or an exact solution of full transport.


**Problem figure**

![Su–Olson transport with an independently published analytical table: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/results/su-olson-transport1997.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Su–Olson transport with an independently published analytical table](https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-transport1997/?lang=en) (`su-olson-transport1997`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-transport1997/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-transport1997/?lang=en#su-olson-transport1997-en-validation)

Fiveprimaryrunsseparatespace,32/64angles,timeandindependentW/Verrors. Finite/causalzero/homogeneousanalyticsource normalization oftheprovidedtableswerequalifiedbeforemain. A matched-IC/BC/source control separates FV-space,angular and continuum-limit errors against independent continuum angular matrices and analytic diffusion;141 reference checks use GL64/128,exact nonunit-capacity k0 exchange and independent DOP853 before primary mode evaluation.

- [Su–Olson transport: primary2023author-provided analytical benchmark data](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-su-olson-transport1997-en) (`su-olson-transport1997`; Same-problem reference · Finite-grid numerical reference)

No direct original1997fulltext/tablecomparison claim. TheauthorREADMEdoesnotstate transcriptionversusregeneration. Source-offprofiles,generalscattering,globalcontinuumerrorandangularorderarenotcertified. The addition is a resolved N~kappa^2 semidiscrete periodic control,not fixed-grid AP or an SSPRK2 diffusion-time order certificate. Initial F0 versus nonzero Fick flux is retained;limit gates use final s=.25 only. SciPy sparse expm_multiply is shared;DOP853 qualifies the reference propagator.
### Assumptions, units and boundaries

epsilon1,noelastic scattering,coldIC,Q1inside|x|<.5untiltau10. Symmetricx0..8withreflectingleft/vacuumright;times.1/1/3.16228and13referencepointsx<6. A separate periodic length2pi control uses kappa4/8/16,cells128/512/2048,epsilon1,Q0 and actual cell means of I=V=1+.1cos x.

**Editorial clarification**

No direct original1997fulltext/tablecomparison claim. TheauthorREADMEdoesnotstate transcriptionversusregeneration. Source-offprofiles,generalscattering,globalcontinuumerrorandangularorderarenotcertified. The addition is a resolved N~kappa^2 semidiscrete periodic control,not fixed-grid AP or an SSPRK2 diffusion-time order certificate. Initial F0 versus nonzero Fick flux is retained;limit gates use final s=.25 only. SciPy sparse expm_multiply is shared;DOP853 qualifies the reference propagator.

### Adopted numerical method

Full signed-angle upwind FV/SSPRK2 advancesIandV. WithI=2U,E=halfangularintegral,the weightedbudgetisepsilonE+V;nodiffusionsubstitution. Only the thick-limit control constructs the same upwind operator from actual real cos/sin responses and evolves one Fourier mode by an exact-time matrix exponential.

$$
\epsilon I_\tau+\mu I_x+I=V+Q,\quad V_\tau=E-V
$$

$$
E=\frac12\int_{-1}^1I\,d\mu,\quad I=2U,\quad\mathcal E=\epsilon E+V
$$

$$
Q=\mathbf1_{|x|<1/2}\mathbf1_{0<\tau<10}
$$

$$
\epsilon I_t+\mu I_x=\kappa(V-I),\quad V_t=\kappa(E-V),\quad x\in[0,2\pi)
$$

$$
D_{\rm rad}=\frac1{3\kappa},\quad D_{\rm eff}=\frac1{3\kappa(\epsilon+1)},\quad t=\kappa s
$$

$$
E_D=V_D=1+A_N e^{-s/[3(\epsilon+1)]}\cos x,\quad F_D=-\frac1{3\kappa}\partial_x E_D
$$

### References and validation

Fiveprimaryrunsseparatespace,32/64angles,timeandindependentW/Verrors. Finite/causalzero/homogeneousanalyticsource normalization oftheprovidedtableswerequalifiedbeforemain. A matched-IC/BC/source control separates FV-space,angular and continuum-limit errors against independent continuum angular matrices and analytic diffusion;141 reference checks use GL64/128,exact nonunit-capacity k0 exchange and independent DOP853 before primary mode evaluation.

### Limits

No direct original1997fulltext/tablecomparison claim. TheauthorREADMEdoesnotstate transcriptionversusregeneration. Source-offprofiles,generalscattering,globalcontinuumerrorandangularorderarenotcertified. The addition is a resolved N~kappa^2 semidiscrete periodic control,not fixed-grid AP or an SSPRK2 diffusion-time order certificate. Initial F0 versus nonzero Fick flux is retained;limit gates use final s=.25 only. SciPy sparse expm_multiply is shared;DOP853 qualifies the reference propagator.

### Stored measurements and decisions

```json
{
  "metrics": {
    "completed_primary_runs": 5,
    "reference_scope": "pinned2023author-providedanalyticaltransporttable;original1997table not directly verified",
    "capacity_controls": [
      {
        "epsilon": 0.25,
        "method": "diffusion",
        "error": 0.00019032949653130515,
        "budget": 5.984102102729594e-14
      },
      {
        "epsilon": 0.25,
        "method": "transport",
        "error": 3.181825272147165e-07,
        "budget": 3.3306690738754696e-16
      },
      {
        "epsilon": 2.0,
        "method": "diffusion",
        "error": 0.000154177848556869,
        "budget": 7.460698725481052e-14
      },
      {
        "epsilon": 2.0,
        "method": "transport",
        "error": 7.721428540996556e-08,
        "budget": 1.199040866595169e-14
      }
    ],
    "matched_thick_limit_control": {
      "physical_mode_evolutions": 3,
      "mode_records": [
        {
          "id": "su-olson-transport1997-thick-k4",
          "kind": "matched-thick-semidiscrete-mode-control",
          "fields": "su-olson-transport1997-thick-k4.npz",
          "kappa": 4,
          "cells": 128,
          "ordinates": 32,
          "mean_free_path": 0.25,
          "kappa_h": 0.19634954084936207,
          "times": [
            0.0,
            0.25,
            0.5,
            1.0
          ],
          "scaled_times": [
            0.0,
            0.0625,
            0.125,
            0.25
          ],
          "initial_cellmean_amplitude": 0.09998996042161418,
          "final_FV_space_error": 0.006406191708967511,
          "final_continuum_limit_error": 0.01484981145966009,
          "final_joint_energy_error": 0.009801905835372807,
          "final_joint_scaled_flux_error": 0.008805846751149496,
          "maximum_angular_sensitivity": 2.361755418510908e-15,
          "maximum_budget": 2.8398112908774138e-15,
          "matrix_residual": 1.3877787807814457e-17,
          "semidiscrete_global_RHS_residual": 9.096889908022376e-15
        },
        {
          "id": "su-olson-transport1997-thick-k8",
          "kind": "matched-thick-semidiscrete-mode-control",
          "fields": "su-olson-transport1997-thick-k8.npz",
          "kappa": 8,
          "cells": 512,
          "ordinates": 32,
          "mean_free_path": 0.125,
          "kappa_h": 0.09817477042468103,
          "times": [
            0.0,
            0.5,
            1.0,
            2.0
          ],
          "scaled_times": [
            0.0,
            0.0625,
            0.125,
            0.25
          ],
          "initial_cellmean_amplitude": 0.09999937250863256,
          "final_FV_space_error": 0.0029971556290815586,
          "final_continuum_limit_error": 0.0038430634683478773,
          "final_joint_energy_error": 0.0016548173640567698,
          "final_joint_scaled_flux_error": 0.0012410650258467806,
          "maximum_angular_sensitivity": 2.707688603804596e-15,
          "maximum_budget": 5.698441403484806e-15,
          "matrix_residual": 1.3877787807814457e-17,
          "semidiscrete_global_RHS_residual": 3.609851133290487e-14
        },
        {
          "id": "su-olson-transport1997-thick-k16",
          "kind": "matched-thick-semidiscrete-mode-control",
          "fields": "su-olson-transport1997-thick-k16.npz",
          "kappa": 16,
          "cells": 2048,
          "ordinates": 32,
          "mean_free_path": 0.0625,
          "kappa_h": 0.04908738521234052,
          "times": [
            0.0,
            1.0,
            2.0,
            4.0
          ],
          "scaled_times": [
            0.0,
            0.0625,
            0.125,
            0.25
          ],
          "initial_cellmean_amplitude": 0.09999996078172033,
          "final_FV_space_error": 0.0014774233739939713,
          "final_continuum_limit_error": 0.0009641878482973868,
          "final_joint_energy_error": 0.0011378880853298219,
          "final_joint_scaled_flux_error": 0.0005274719030461596,
          "maximum_angular_sensitivity": 5.828675392681093e-15,
          "maximum_budget": 1.0695349491031034e-14,
          "matrix_residual": 3.469446951953614e-18,
          "semidiscrete_global_RHS_residual": 8.391850078921443e-14
        }
      ],
      "reference_checks": 141,
      "same_operator": "kappa times actualtransport.rhs withkappa*h,bothrates",
      "time_role": "Exact-time semidiscrete Fourier control; originalSSPRK2tests/transientruns separate",
      "reference_role": "Independentcontinuum-space angularmatrixGL64/128plusDOP853qualifiers;sharedSciPysparseexpm_multiplydeclared",
      "diffusion": "D_rad1/(3kappa),D_eff1/[3kappa(epsilon+1)],matchedperiodiccellmeanIC",
      "scope": "ResolvedjointN~kappa^2limit; nofixed-gridAPorSSPRK2temporal-orderclaim. Initiallayerreportedallfourtimes;asymptoticgatesfinals.25only;nojointorderfit."
    }
  },
  "checks": {
    "su-olson-transport1997-n128/finite-positive": true,
    "su-olson-transport1997-n128/energy-budget": true,
    "su-olson-transport1997-n128/fixed-final-time": true,
    "su-olson-transport1997-n128/explicit-courant": true,
    "su-olson-transport1997-n256/finite-positive": true,
    "su-olson-transport1997-n256/energy-budget": true,
    "su-olson-transport1997-n256/fixed-final-time": true,
    "su-olson-transport1997-n256/explicit-courant": true,
    "su-olson-transport1997-n512/finite-positive": true,
    "su-olson-transport1997-n512/energy-budget": true,
    "su-olson-transport1997-n512/fixed-final-time": true,
    "su-olson-transport1997-n512/explicit-courant": true,
    "su-olson-transport1997-angular-64/finite-positive": true,
    "su-olson-transport1997-angular-64/energy-budget": true,
    "su-olson-transport1997-angular-64/fixed-final-time": true,
    "su-olson-transport1997-angular-64/explicit-courant": true,
    "su-olson-transport1997-half-dt/finite-positive": true,
    "su-olson-transport1997-half-dt/energy-budget": true,
    "su-olson-transport1997-half-dt/fixed-final-time": true,
    "su-olson-transport1997-half-dt/explicit-courant": true,
    "refinement/1": true,
    "refinement/2": true,
    "finest-independent-rms": true,
    "finest-independent-linf": true,
    "separate-angular-sensitivity": true,
    "separate-time-sensitivity": true,
    "capacity/0.25/diffusion/error": true,
    "capacity/0.25/diffusion/budget": true,
    "capacity/0.25/transport/error": true,
    "capacity/0.25/transport/budget": true,
    "capacity/2.0/diffusion/error": true,
    "capacity/2.0/diffusion/budget": true,
    "capacity/2.0/transport/error": true,
    "capacity/2.0/transport/budget": true,
    "thick/4/finite-positive-fields": true,
    "thick/4/periodic-weighted-energy": true,
    "thick/4/actual-stencil-and-global-RHS": true,
    "thick/4/separate-FV-space-error": true,
    "thick/4/separate-angular-sensitivity": true,
    "thick/4/physical-initial-layer-retained": true,
    "thick/4/mean-free-path-resolved": true,
    "thick/8/finite-positive-fields": true,
    "thick/8/periodic-weighted-energy": true,
    "thick/8/actual-stencil-and-global-RHS": true,
    "thick/8/separate-FV-space-error": true,
    "thick/8/separate-angular-sensitivity": true,
    "thick/8/physical-initial-layer-retained": true,
    "thick/8/mean-free-path-resolved": true,
    "thick/16/finite-positive-fields": true,
    "thick/16/periodic-weighted-energy": true,
    "thick/16/actual-stencil-and-global-RHS": true,
    "thick/16/separate-FV-space-error": true,
    "thick/16/separate-angular-sensitivity": true,
    "thick/16/physical-initial-layer-retained": true,
    "thick/16/mean-free-path-resolved": true,
    "thick/space/k8": true,
    "thick/continuum-limit/k8": true,
    "thick/space/k16": true,
    "thick/continuum-limit/k16": true,
    "thick/finest-energy-limit": true,
    "thick/finest-scaled-flux-limit": true,
    "thick/wrong-flux-sign-negative-control": true,
    "thick/missing-one-third-negative-control": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-transport1997/index.json

![Scientific preview from the actual saved numerical fields.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/results/su-olson-transport1997-preview.png)

Scientific preview from the actual saved numerical fields.

![Matched thick-limit control: exact-time single Fourier mode of the actual 1D periodic FV/S_N operator;initial layer and spatial/angular/limit errors separated. No fixed-grid AP or SSPRK2 time-integration certification.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/results/su-olson-transport1997-thick-limit.png)

Matched thick-limit control: exact-time single Fourier mode of the actual 1D periodic FV/S_N operator;initial layer and spatial/angular/limit errors separated. No fixed-grid AP or SSPRK2 time-integration certification.

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/atlas-radiation-matter-2026-11-24-r2.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- Aidan Crilly (2023). Learning closure relations using differentiable programming:an example in radiation transport;author-provided analytic benchmark data. https://github.com/aidancrilly/RTClosureJAX/tree/3e4f636299d62bc03f7118cfc884230c756f9d87/SuOlsonData; review_level=primary-author-paper-selected-equations-and-pinned-data-qualification
Read official2023paperpage6Appendix4.1equations7-10,README,pinned W/Vtransport tables andMITlicense. Whether author tables were transcribed or regenerated is unstated. Original1997fulltext/tables not directly checked;not trained-model outputs. Shape,normalization,causal/homogeneous controls qualified.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
