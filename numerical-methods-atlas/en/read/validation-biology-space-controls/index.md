# Biological reaction–diffusion: two-dimensional and boundary controls

Compare a special-speed Fisher front, boundary-specific two-dimensional Schnakenberg transients and forced Keller–Segel cell averages and fluxes with independent references.

These additional validation supplements are managed separately from the common 22-example registry. Receipts cover independent ZIP extraction, tests and every fixed input within each group. Changes of settings, methods or step sizes do not add independent physical problems.

## Fisher–KPP: a special-speed exact front

Separate profile, phase, grid, time and finite-boundary errors.

**Methods used**

- [SSPRK(3,3)](https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk33/?lang=en) (`ssprk33`)
- [Dormand–Prince RK45](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk45/?lang=en) (`rk45`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/fisher-kpp-special-front/?lang=en#fisher-kpp-special-front-en-algorithm)

Use centered second-order differences and SSPRK3 with exact Dirichlet values at every stage. Compare time errors to an independent reference for the same95-unknown semidiscreteODE.

$$
u_t=u_{xx}+u(1-u)
$$

$$
u(x,t)=[1+\exp((x-5t/\sqrt6)/\sqrt6)]^{-2}
$$

- [Fisher–KPP invasion front](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-fisher-kpp-en) (`bio-fisher-kpp`)

Use D=r=1,T=1 and the special speed5/√6. Fix spatial/time series on L12 and constant-endpoint boundary rows at L6/12/24.


**Problem figure**

![Fisher–KPP: a special-speed exact front: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/fisher-kpp-special-front.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Fisher–KPP: a special-speed exact front](https://hrkoyama.github.io/numerical-methods-atlas/problems/fisher-kpp-special-front/?lang=en) (`fisher-kpp-special-front`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/fisher-kpp-special-front/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/fisher-kpp-special-front/?lang=en#fisher-kpp-special-front-en-validation)

Save exact-profile and quarter-contour errors, same-grid time convergence and full/core boundary errors. Distinguish a real-arithmetic discrete barrier from the observed floating-point margin.

- [Fisher–KPP: a special-speed exact front](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-fisher-kpp-special-front-en) (`fisher-kpp-special-front`; Same-problem reference · Analytic reference)

The special front is distinct from the minimum linear speed2. This is not a steep-data speed-selection study, long-time propagation result or certified machine-error barrier proof.
### Assumptions, units and boundaries

Use D=r=1,T=1 and the special speed5/√6. Fix spatial/time series on L12 and constant-endpoint boundary rows at L6/12/24.

**Editorial clarification**

The special front is distinct from the minimum linear speed2. This is not a steep-data speed-selection study, long-time propagation result or certified machine-error barrier proof.

### Adopted numerical method

Use centered second-order differences and SSPRK3 with exact Dirichlet values at every stage. Compare time errors to an independent reference for the same95-unknown semidiscreteODE.

$$
u_t=u_{xx}+u(1-u)
$$

$$
u(x,t)=[1+\exp((x-5t/\sqrt6)/\sqrt6)]^{-2}
$$

### References and validation

Save exact-profile and quarter-contour errors, same-grid time convergence and full/core boundary errors. Distinguish a real-arithmetic discrete barrier from the observed floating-point margin.

### Limits

The special front is distinct from the minimum linear speed2. This is not a steep-data speed-selection study, long-time propagation result or certified machine-error barrier proof.

### Study goals: 6 met, 0 unmet, 0 unresolved (6 total)

Mandatory qualification is separate from study-goal attainment. Met/unmet follow stored comparisons, not statistical certification. Unresolved and separate uncertainty classifications are retained; null is not replaced by false or zero.

[Original saved results / JSON](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/result.json)

<details><summary>Read every study-goal record</summary>

```json
{
  "schema_version": 1,
  "counts": {
    "met": 6,
    "unmet": 0,
    "unresolved": 0,
    "total": 6
  },
  "goals": [
    {
      "name": "Fisher/space-finest",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 9.239320837961529e-06,
        "target": 0.001
      }
    },
    {
      "name": "Fisher/space-order",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 1.9958436278085308,
        "target": 1.7
      }
    },
    {
      "name": "Fisher/phase",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.0002657675674280213,
        "target": 0.02
      }
    },
    {
      "name": "Fisher/time-order",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 3.0607173908690903,
        "target": 2.7,
        "reference_spread": 2.886579864025407e-15
      }
    },
    {
      "name": "Fisher/time-finest",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 1.8780066390888805e-10,
        "target": 1e-05
      }
    },
    {
      "name": "Fisher/observed-boundary-margin",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "observed_margin": 9.999999795441408e-05,
        "scope": "Observed binary64 margin; analyticreal-arithmetic barrier is not a machine-error certificate"
      }
    }
  ],
  "classification_basis": "stored observed comparison; separate uncertainty classifications retained",
  "source": {
    "collection": "study_goals",
    "json_pointer": "/study_goals",
    "prefix": "Fisher/",
    "result_sha256": "090c187f89db9d05a2eb437eaf5e73b2dcf1e7600ef0163efd94bae4119cb6eb",
    "acceptance_sha256": "b2f1727f9f4e70c139af7d38c218608b369625ab8f5896d762b060f88432a117",
    "result_url": "https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/result.json",
    "acceptance_url": "https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/acceptance.json"
  }
}
```

</details>

### Stored measurements and decisions

```json
{
  "metrics": {
    "fixed_records": 11,
    "Fisher/space-finest/actual": 9.239320837961529e-06,
    "Fisher/space-order/actual": 1.9958436278085308,
    "Fisher/phase/actual": 0.0002657675674280213,
    "Fisher/time-order/actual": 3.0607173908690903,
    "Fisher/time-finest/actual": 1.8780066390888805e-10,
    "Fisher/observed-boundary-margin/observed_margin": 9.999999795441408e-05
  },
  "checks": {
    "Fisher/exact-PDE": true,
    "Fisher/wrong-special-speed-detected": true,
    "Fisher/finite-space/0.5": true,
    "Fisher/finite-space/0.25": true,
    "Fisher/finite-space/0.125": true,
    "Fisher/semidiscrete-reference": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/fisher-kpp-special-front/index.json

![Separate actual accuracy,reference and statistical measurements,including unmet targets.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/fisher-kpp-special-front-diagnostics.png)

Separate actual accuracy,reference and statistical measurements,including unmet targets.

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/atlas-biology-space-controls-2026-11-25.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- Ablowitz–Zeppetella(1979), Explicit solutions of Fisher’s equation for a special wave speed. https://doi.org/10.1007/BF02462380; review_level=selected-primary-or-bibliographic-see-provenance
Actual selected read scopes and unread limits are recorded in source-reading.json; no full original-paper equation/figure reproduction claim.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## Schnakenberg:2D boundaries and initial modes

Compare two Neumann perturbations and a Dirichlet perturbation against nonlinear Galerkin references.

**Methods used**

- [Crank–Nicolson](https://hrkoyama.github.io/numerical-methods-atlas/methods/crank-nicolson/?lang=en) (`crank-nicolson`)
- [Strang splitting](https://hrkoyama.github.io/numerical-methods-atlas/methods/strang-splitting/?lang=en) (`strang-splitting`)
- [Dormand–Prince RK45](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk45/?lang=en) (`rk45`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-2d-boundary-modes/?lang=en#schnakenberg-2d-boundary-modes-en-algorithm)

Strang-split cell-averageCN diffusion and local implicit-midpoint reactions. Independent orthonormal sine/cosine Galerkin references retain four K12/18,Q96/192,tolerance rows for every initial condition. The original Dirichlet K12/18 reference failed its first relative qualification. Preserve that failure and add four D-only K24/32,Q128/192 reference actions.

$$
u_t=.01\Delta u+.1-u+u^2v,\qquad v_t=\Delta v+.9-u^2v
$$

- [Schnakenberg reaction–diffusion](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-schnakenberg-en) (`bio-schnakenberg`)

On[0,2π]² toT2,use a.1,b.9,Du.01,Dv1. Compare three perturbations of(1,.9),12/24/48cell grids and fixed nonperiodic boundary conditions.


**Problem figure**

![Schnakenberg:2D boundaries and initial modes: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/schnakenberg-2d-boundary-modes.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Schnakenberg:2D boundaries and initial modes](https://hrkoyama.github.io/numerical-methods-atlas/problems/schnakenberg-2d-boundary-modes/?lang=en) (`schnakenberg-2d-boundary-modes`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/schnakenberg-2d-boundary-modes/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-2d-boundary-modes/?lang=en#schnakenberg-2d-boundary-modes-en-validation)

Check continuum/discrete linear symbols, corner-face ownership, equilibrium and mass ledgers. Separate K/Q/tolerance sensitivity; unqualified references leave related accuracy/order unresolved. Use the new finer reference for accuracy goals only after the same absolute/relative criteria pass; the original failed qualification is retained.

- [Schnakenberg:2D boundaries and initial modes](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-schnakenberg-2d-boundary-modes-en) (`schnakenberg-2d-boundary-modes`; Same-problem reference · Finite-grid numerical reference)

This short small-amplitude study does not establish general pattern selection, mature patterns or reproduction of original figures. Finite reference differences are not rigorous continuum error bounds.
### Assumptions, units and boundaries

On[0,2π]² toT2,use a.1,b.9,Du.01,Dv1. Compare three perturbations of(1,.9),12/24/48cell grids and fixed nonperiodic boundary conditions.

**Editorial clarification**

This short small-amplitude study does not establish general pattern selection, mature patterns or reproduction of original figures. Finite reference differences are not rigorous continuum error bounds.

### Adopted numerical method

Strang-split cell-averageCN diffusion and local implicit-midpoint reactions. Independent orthonormal sine/cosine Galerkin references retain four K12/18,Q96/192,tolerance rows for every initial condition. The original Dirichlet K12/18 reference failed its first relative qualification. Preserve that failure and add four D-only K24/32,Q128/192 reference actions.

$$
u_t=.01\Delta u+.1-u+u^2v,\qquad v_t=\Delta v+.9-u^2v
$$

### References and validation

Check continuum/discrete linear symbols, corner-face ownership, equilibrium and mass ledgers. Separate K/Q/tolerance sensitivity; unqualified references leave related accuracy/order unresolved. Use the new finer reference for accuracy goals only after the same absolute/relative criteria pass; the original failed qualification is retained.

### Limits

This short small-amplitude study does not establish general pattern selection, mature patterns or reproduction of original figures. Finite reference differences are not rigorous continuum error bounds.

### Study goals: 16 met, 0 unmet, 1 unresolved (17 total)

Mandatory qualification is separate from study-goal attainment. Met/unmet follow stored comparisons, not statistical certification. Unresolved and separate uncertainty classifications are retained; null is not replaced by false or zero.

[Original saved results / JSON](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/result.json)

<details><summary>Read every study-goal record</summary>

```json
{
  "schema_version": 1,
  "counts": {
    "met": 16,
    "unmet": 0,
    "unresolved": 1,
    "total": 17
  },
  "goals": [
    {
      "name": "Schnakenberg/positivity/N-mode42/12",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "minimum": 0.8880521241619382
      }
    },
    {
      "name": "Schnakenberg/positivity/N-mode42/24",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "minimum": 0.8860615561401685
      }
    },
    {
      "name": "Schnakenberg/positivity/N-mode42/48",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "minimum": 0.8855372535923153
      }
    },
    {
      "name": "Schnakenberg/space-finest/N-mode42",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 8.250442438972883e-05,
        "target": 0.02
      }
    },
    {
      "name": "Schnakenberg/space-order/N-mode42",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 1.944655350128315,
        "target": 1.6
      }
    },
    {
      "name": "Schnakenberg/positivity/N-mixed/12",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "minimum": 0.8798143344957898
      }
    },
    {
      "name": "Schnakenberg/positivity/N-mixed/24",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "minimum": 0.8771054043233121
      }
    },
    {
      "name": "Schnakenberg/positivity/N-mixed/48",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "minimum": 0.8763952220795853
      }
    },
    {
      "name": "Schnakenberg/space-finest/N-mixed",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.00011769804580841203,
        "target": 0.02
      }
    },
    {
      "name": "Schnakenberg/space-order/N-mixed",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 1.9477700373628166,
        "target": 1.6
      }
    },
    {
      "name": "Schnakenberg/time-order",
      "observed": null,
      "outcome": "unresolved",
      "stored": {
        "observed": null,
        "actual": null,
        "target": 1.7
      }
    },
    {
      "name": "Schnakenberg/time-contamination",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 1.1208580182516432e-07,
        "finest_spatial_discrepancy": 0.00011769804580841203,
        "scope": "Secondorder Richardson indicator,notcertifiederrorbound"
      }
    },
    {
      "name": "Schnakenberg/positivity/D-mode42/12",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "minimum": 0.8862155577223321
      }
    },
    {
      "name": "Schnakenberg/positivity/D-mode42/24",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "minimum": 0.8860670448524426
      }
    },
    {
      "name": "Schnakenberg/positivity/D-mode42/48",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "minimum": 0.8855435379971976
      }
    },
    {
      "name": "Schnakenberg/space-finest/D-mode42",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 8.370124740819662e-05,
        "target": 0.02
      }
    },
    {
      "name": "Schnakenberg/space-order/D-mode42",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 1.9463235349282928,
        "target": 1.6
      }
    }
  ],
  "classification_basis": "stored observed comparison; separate uncertainty classifications retained",
  "source": {
    "collection": "study_goals",
    "json_pointer": "/study_goals",
    "prefix": "Schnakenberg/",
    "result_sha256": "090c187f89db9d05a2eb437eaf5e73b2dcf1e7600ef0163efd94bae4119cb6eb",
    "acceptance_sha256": "b2f1727f9f4e70c139af7d38c218608b369625ab8f5896d762b060f88432a117",
    "result_url": "https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/result.json",
    "acceptance_url": "https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/acceptance.json"
  }
}
```

</details>

### Stored measurements and decisions

```json
{
  "metrics": {
    "fixed_records": 33,
    "Schnakenberg/positivity/N-mode42/12/minimum": 0.8880521241619382,
    "Schnakenberg/positivity/N-mode42/24/minimum": 0.8860615561401685,
    "Schnakenberg/positivity/N-mode42/48/minimum": 0.8855372535923153,
    "Schnakenberg/space-finest/N-mode42/actual": 8.250442438972883e-05,
    "Schnakenberg/space-order/N-mode42/actual": 1.944655350128315,
    "Schnakenberg/positivity/N-mixed/12/minimum": 0.8798143344957898,
    "Schnakenberg/positivity/N-mixed/24/minimum": 0.8771054043233121,
    "Schnakenberg/positivity/N-mixed/48/minimum": 0.8763952220795853,
    "Schnakenberg/space-finest/N-mixed/actual": 0.00011769804580841203,
    "Schnakenberg/space-order/N-mixed/actual": 1.9477700373628166,
    "Schnakenberg/time-contamination/actual": 1.1208580182516432e-07,
    "Schnakenberg/positivity/D-mode42/12/minimum": 0.8862155577223321,
    "Schnakenberg/positivity/D-mode42/24/minimum": 0.8860670448524426,
    "Schnakenberg/positivity/D-mode42/48/minimum": 0.8855435379971976,
    "Schnakenberg/space-finest/D-mode42/actual": 8.370124740819662e-05,
    "Schnakenberg/space-order/D-mode42/actual": 1.9463235349282928
  },
  "checks": {
    "Schnakenberg/mode/N/1/1/12": true,
    "Schnakenberg/exp/N/1/1/12/0.1": true,
    "Schnakenberg/exp/N/1/1/12/0.5": true,
    "Schnakenberg/exp/N/1/1/12/1.0": true,
    "Schnakenberg/mode/N/1/1/24": true,
    "Schnakenberg/exp/N/1/1/24/0.1": true,
    "Schnakenberg/exp/N/1/1/24/0.5": true,
    "Schnakenberg/exp/N/1/1/24/1.0": true,
    "Schnakenberg/mode/N/1/1/48": true,
    "Schnakenberg/exp/N/1/1/48/0.1": true,
    "Schnakenberg/exp/N/1/1/48/0.5": true,
    "Schnakenberg/exp/N/1/1/48/1.0": true,
    "Schnakenberg/mode/N/4/2/12": true,
    "Schnakenberg/exp/N/4/2/12/0.1": true,
    "Schnakenberg/exp/N/4/2/12/0.5": true,
    "Schnakenberg/exp/N/4/2/12/1.0": true,
    "Schnakenberg/mode/N/4/2/24": true,
    "Schnakenberg/exp/N/4/2/24/0.1": true,
    "Schnakenberg/exp/N/4/2/24/0.5": true,
    "Schnakenberg/exp/N/4/2/24/1.0": true,
    "Schnakenberg/mode/N/4/2/48": true,
    "Schnakenberg/exp/N/4/2/48/0.1": true,
    "Schnakenberg/exp/N/4/2/48/0.5": true,
    "Schnakenberg/exp/N/4/2/48/1.0": true,
    "Schnakenberg/mode/N/3/1/12": true,
    "Schnakenberg/exp/N/3/1/12/0.1": true,
    "Schnakenberg/exp/N/3/1/12/0.5": true,
    "Schnakenberg/exp/N/3/1/12/1.0": true,
    "Schnakenberg/mode/N/3/1/24": true,
    "Schnakenberg/exp/N/3/1/24/0.1": true,
    "Schnakenberg/exp/N/3/1/24/0.5": true,
    "Schnakenberg/exp/N/3/1/24/1.0": true,
    "Schnakenberg/mode/N/3/1/48": true,
    "Schnakenberg/exp/N/3/1/48/0.1": true,
    "Schnakenberg/exp/N/3/1/48/0.5": true,
    "Schnakenberg/exp/N/3/1/48/1.0": true,
    "Schnakenberg/mode/D/1/1/12": true,
    "Schnakenberg/exp/D/1/1/12/0.1": true,
    "Schnakenberg/exp/D/1/1/12/0.5": true,
    "Schnakenberg/exp/D/1/1/12/1.0": true,
    "Schnakenberg/mode/D/1/1/24": true,
    "Schnakenberg/exp/D/1/1/24/0.1": true,
    "Schnakenberg/exp/D/1/1/24/0.5": true,
    "Schnakenberg/exp/D/1/1/24/1.0": true,
    "Schnakenberg/mode/D/1/1/48": true,
    "Schnakenberg/exp/D/1/1/48/0.1": true,
    "Schnakenberg/exp/D/1/1/48/0.5": true,
    "Schnakenberg/exp/D/1/1/48/1.0": true,
    "Schnakenberg/mode/D/4/2/12": true,
    "Schnakenberg/exp/D/4/2/12/0.1": true,
    "Schnakenberg/exp/D/4/2/12/0.5": true,
    "Schnakenberg/exp/D/4/2/12/1.0": true,
    "Schnakenberg/mode/D/4/2/24": true,
    "Schnakenberg/exp/D/4/2/24/0.1": true,
    "Schnakenberg/exp/D/4/2/24/0.5": true,
    "Schnakenberg/exp/D/4/2/24/1.0": true,
    "Schnakenberg/mode/D/4/2/48": true,
    "Schnakenberg/exp/D/4/2/48/0.1": true,
    "Schnakenberg/exp/D/4/2/48/0.5": true,
    "Schnakenberg/exp/D/4/2/48/1.0": true,
    "Schnakenberg/mode/D/3/1/12": true,
    "Schnakenberg/exp/D/3/1/12/0.1": true,
    "Schnakenberg/exp/D/3/1/12/0.5": true,
    "Schnakenberg/exp/D/3/1/12/1.0": true,
    "Schnakenberg/mode/D/3/1/24": true,
    "Schnakenberg/exp/D/3/1/24/0.1": true,
    "Schnakenberg/exp/D/3/1/24/0.5": true,
    "Schnakenberg/exp/D/3/1/24/1.0": true,
    "Schnakenberg/mode/D/3/1/48": true,
    "Schnakenberg/exp/D/3/1/48/0.1": true,
    "Schnakenberg/exp/D/3/1/48/0.5": true,
    "Schnakenberg/exp/D/3/1/48/1.0": true,
    "Schnakenberg/equilibrium-face-zero": true,
    "Schnakenberg/constant-equilibrium/N": true,
    "Schnakenberg/constant-equilibrium/D": true,
    "Schnakenberg/wrong-boundary-control": true,
    "Schnakenberg/corner-doublecount-control": true,
    "Schnakenberg/linear-action-count": true,
    "Schnakenberg/ledger/N-mode42/12": true,
    "Schnakenberg/ledger/N-mode42/24": true,
    "Schnakenberg/ledger/N-mode42/48": true,
    "Schnakenberg/reference/N-mode42": true,
    "Schnakenberg/ledger/N-mixed/12": true,
    "Schnakenberg/ledger/N-mixed/24": true,
    "Schnakenberg/ledger/N-mixed/48": true,
    "Schnakenberg/reference/N-mixed": true,
    "Schnakenberg/ledger/D-mode42/12": true,
    "Schnakenberg/ledger/D-mode42/24": true,
    "Schnakenberg/ledger/D-mode42/48": true,
    "Schnakenberg/reference/D-mode42": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-2d-boundary-modes/index.json

![Separate actual accuracy,reference and statistical measurements,including unmet targets.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/schnakenberg-2d-boundary-modes-diagnostics.png)

Separate actual accuracy,reference and statistical measurements,including unmet targets.

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/atlas-biology-space-controls-2026-11-25.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- Schnakenberg(1979), Simple chemical reaction systems with limit cycle behaviour. https://pubmed.ncbi.nlm.nih.gov/537379/; review_level=selected-primary-or-bibliographic-see-provenance
Actual selected read scopes and unread limits are recorded in source-reading.json; no full original-paper equation/figure reproduction claim.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## Keller–Segel: a manufactured coupled-flux solution

Use smooth exact2D fields to test cross fluxes, stage timing and mass ledgers.

**Methods used**

- [SSPRK(3,3)](https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk33/?lang=en) (`ssprk33`)
- [Dormand–Prince RK45](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk45/?lang=en) (`rk45`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/keller-segel-forced-flux/?lang=en#keller-segel-forced-flux-en-algorithm)

Use cell-average centered face fluxes and SSPRK3 with n,c and forcing at the same stage. Check expanded trigonometric integrals against independent unexpanded integrals and scalar face-loop references.

$$
n_t+\nabla\cdot(wn)=D_n\Delta n-\chi\nabla\cdot(n\nabla c)+rn(1-n)+s_n
$$

$$
\tau c_t=D_c\Delta c+\alpha n-\lambda c+s_c
$$

- [Keller–Segel chemotaxis](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-keller-segel-en) (`bio-keller-segel`)

On the unit square toT.25,manufacture forcing for n=1+.1e⁻ᵗcosπx cosπy,c=1+.05e⁻²ᵗcosπx cos2πy with divergence-free tangential advection.

- [Forced advective Keller–Segel manufactured problem](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#forced-keller-segel-model-en) (`forced-keller-segel-model`)

On the unit square toT.25,manufacture forcing for n=1+.1e⁻ᵗcosπx cosπy,c=1+.05e⁻²ᵗcosπx cos2πy with divergence-free tangential advection.


**Problem figure**

![Keller–Segel: a manufactured coupled-flux solution: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/keller-segel-forced-flux.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Keller–Segel: a manufactured coupled-flux solution](https://hrkoyama.github.io/numerical-methods-atlas/problems/keller-segel-forced-flux/?lang=en) (`keller-segel-forced-flux`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/keller-segel-forced-flux/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/keller-segel-forced-flux/?lang=en#keller-segel-forced-flux-en-validation)

Qualify36source pairs,96cell-state vectors and wrong-sign,omitted-coupling,stale-stage and face-duplication controls. Separate spatial,same-MOL time,positivity and actual stage-ledger outcomes.

- [Keller–Segel: a manufactured coupled-flux solution](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-keller-segel-forced-flux-en) (`keller-segel-forced-flux`; Same-problem reference · Manufactured solution)

This authored forced two-field model does not reproduce the full original biological model or demonstrate aggregation, true blow-up or suppression. No clipping is used to manufacture positivity.
### Assumptions, units and boundaries

On the unit square toT.25,manufacture forcing for n=1+.1e⁻ᵗcosπx cosπy,c=1+.05e⁻²ᵗcosπx cos2πy with divergence-free tangential advection.

**Editorial clarification**

This authored forced two-field model does not reproduce the full original biological model or demonstrate aggregation, true blow-up or suppression. No clipping is used to manufacture positivity.

### Adopted numerical method

Use cell-average centered face fluxes and SSPRK3 with n,c and forcing at the same stage. Check expanded trigonometric integrals against independent unexpanded integrals and scalar face-loop references.

$$
n_t+\nabla\cdot(wn)=D_n\Delta n-\chi\nabla\cdot(n\nabla c)+rn(1-n)+s_n
$$

$$
\tau c_t=D_c\Delta c+\alpha n-\lambda c+s_c
$$

### References and validation

Qualify36source pairs,96cell-state vectors and wrong-sign,omitted-coupling,stale-stage and face-duplication controls. Separate spatial,same-MOL time,positivity and actual stage-ledger outcomes.

### Limits

This authored forced two-field model does not reproduce the full original biological model or demonstrate aggregation, true blow-up or suppression. No clipping is used to manufacture positivity.

### Study goals: 9 met, 0 unmet, 0 unresolved (9 total)

Mandatory qualification is separate from study-goal attainment. Met/unmet follow stored comparisons, not statistical certification. Unresolved and separate uncertainty classifications are retained; null is not replaced by false or zero.

[Original saved results / JSON](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/result.json)

<details><summary>Read every study-goal record</summary>

```json
{
  "schema_version": 1,
  "counts": {
    "met": 9,
    "unmet": 0,
    "unresolved": 0,
    "total": 9
  },
  "goals": [
    {
      "name": "KS/minimum/12",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "minimum": [
          0.9022638544007324,
          0.9527970664018593
        ]
      }
    },
    {
      "name": "KS/minimum/24",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "minimum": [
          0.9005698543736446,
          0.9507102465265501
        ]
      }
    },
    {
      "name": "KS/minimum/48",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "minimum": [
          0.9001427078852056,
          0.9501782550064043
        ]
      }
    },
    {
      "name": "KS/time-order",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 3.0037445404571113,
        "target": 2.5
      }
    },
    {
      "name": "KS/space-finest/0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.0001221189660198796,
        "target": 0.002
      }
    },
    {
      "name": "KS/space-order/0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 1.9965225132866062,
        "target": 1.7
      }
    },
    {
      "name": "KS/space-finest/1",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 2.9817290057465584e-05,
        "target": 0.002
      }
    },
    {
      "name": "KS/space-order/1",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 1.988907316937278,
        "target": 1.7
      }
    },
    {
      "name": "KS/time-contamination",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 1.893596390800667e-12,
        "finest_spatial_error": 0.0001221189660198796
      }
    }
  ],
  "classification_basis": "stored observed comparison; separate uncertainty classifications retained",
  "source": {
    "collection": "study_goals",
    "json_pointer": "/study_goals",
    "prefix": "KS/",
    "result_sha256": "090c187f89db9d05a2eb437eaf5e73b2dcf1e7600ef0163efd94bae4119cb6eb",
    "acceptance_sha256": "b2f1727f9f4e70c139af7d38c218608b369625ab8f5896d762b060f88432a117",
    "result_url": "https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/result.json",
    "acceptance_url": "https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/acceptance.json"
  }
}
```

</details>

### Stored measurements and decisions

```json
{
  "metrics": {
    "fixed_records": 10,
    "KS/time-order/actual": 3.0037445404571113,
    "KS/space-finest/0/actual": 0.0001221189660198796,
    "KS/space-order/0/actual": 1.9965225132866062,
    "KS/space-finest/1/actual": 2.9817290057465584e-05,
    "KS/space-order/1/actual": 1.988907316937278,
    "KS/time-contamination/actual": 1.893596390800667e-12
  },
  "checks": {
    "KS/source_point_pairs36": true,
    "KS/wholegrid_RHS_vectorpairs96": true,
    "KS/divergence_free_faces": true,
    "KS/independent_velocity": true,
    "KS/wrong_chi_detected": true,
    "KS/omitted_coupling_detected": true,
    "KS/stale_source_time_detected": true,
    "KS/duplicated_external_face_detected": true,
    "KS/massledger/12": true,
    "KS/massledger/24": true,
    "KS/massledger/48": true,
    "KS/reference": true,
    "KS/constant-control": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/keller-segel-forced-flux/index.json

![Separate actual accuracy,reference and statistical measurements,including unmet targets.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/keller-segel-forced-flux-diagnostics.png)

Separate actual accuracy,reference and statistical measurements,including unmet targets.

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/atlas-biology-space-controls-2026-11-25.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- Atlas authored Keller–Segel manufactured fields, forcing and finite-volume balance controls (2026-11-25). https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/keller_segel.py; review_level=authored-formulas-and-actually-executed-component-checks
Atlas-authored manufactured fields, forcing and face-flux derivation/implementation. Evidence is limited to saved component checks, independently written scalar-face/RHS references and cell-average comparisons. No original-paper full-text reading or reproduction of the unforced original problem is claimed.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
