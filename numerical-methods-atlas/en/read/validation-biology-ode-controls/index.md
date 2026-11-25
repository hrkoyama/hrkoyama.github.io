# Independent checks of membrane dynamics and reaction SSA

Check Hodgkin–Huxley clamps, rest and firing alongside exact immigration–death SSA transient laws on fixed small inputs.

These additional validation supplements are managed separately from the common 22-example registry. Receipts cover independent ZIP extraction, tests and every fixed input within each group. Changes of settings, methods or step sizes do not add independent physical problems.

## Hodgkin–Huxley: clamps, rest and firing

Compare analytic clamp gates and a four-state system with segment-owned current.

**Methods used**

- [Classical RK4](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=en) (`rk4`)
- [Dormand–Prince RK45](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk45/?lang=en) (`rk45`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/hodgkin-huxley-controls/?lang=en#hodgkin-huxley-controls-en-algorithm)

Use classicalRK4 with all stages owned by each current segment. Separately qualify removable rate singularities, a Decimal rest root and independently written DP5(4)/Cash–Karp references.

$$
C_m\dot V=I-g_{Na}m^3h(V-E_{Na})-g_Kn^4(V-E_K)-g_L(V-E_L)
$$

$$
\dot z=\alpha_z(V)(1-z)-\beta_z(V)z
$$

- [Hodgkin–Huxley membrane dynamics](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-hodgkin-huxley-en) (`bio-hodgkin-huxley`)

Fix6.3°C and the NEURON8.2.6 analytic absolute-voltage convention in ms/mV/µA cm⁻². Use four clamp voltages, three steps, a20ms rest and a10–11ms pulse.


**Problem figure**

![Hodgkin–Huxley: clamps, rest and firing: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/results/hodgkin-huxley-controls.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Hodgkin–Huxley: clamps, rest and firing](https://hrkoyama.github.io/numerical-methods-atlas/problems/hodgkin-huxley-controls/?lang=en) (`hodgkin-huxley-controls`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/hodgkin-huxley-controls/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/hodgkin-huxley-controls/?lang=en#hodgkin-huxley-controls-en-validation)

Retain errors over all accepted times, voltage/gate ranges and Hermite firing events from fresh accepted-endpoint derivatives. Preserve the original1e-8clamp goal even when unmet.

- [Hodgkin–Huxley: clamps, rest and firing](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-hodgkin-huxley-controls-en) (`hodgkin-huxley-controls`; Same-problem reference · Semi-analytic reference)

This educational membrane model does not reproduce the original voltage convention, TABLE/cnexp, cable propagation or measured physiology. Missing/unresolved events remain explicit; rest-root uniqueness and interval-Hurwitz stability are unclaimed.
### Assumptions, units and boundaries

Fix6.3°C and the NEURON8.2.6 analytic absolute-voltage convention in ms/mV/µA cm⁻². Use four clamp voltages, three steps, a20ms rest and a10–11ms pulse.

**Editorial clarification**

This educational membrane model does not reproduce the original voltage convention, TABLE/cnexp, cable propagation or measured physiology. Missing/unresolved events remain explicit; rest-root uniqueness and interval-Hurwitz stability are unclaimed.

### Adopted numerical method

Use classicalRK4 with all stages owned by each current segment. Separately qualify removable rate singularities, a Decimal rest root and independently written DP5(4)/Cash–Karp references.

$$
C_m\dot V=I-g_{Na}m^3h(V-E_{Na})-g_Kn^4(V-E_K)-g_L(V-E_L)
$$

$$
\dot z=\alpha_z(V)(1-z)-\beta_z(V)z
$$

### References and validation

Retain errors over all accepted times, voltage/gate ranges and Hermite firing events from fresh accepted-endpoint derivatives. Preserve the original1e-8clamp goal even when unmet.

### Limits

This educational membrane model does not reproduce the original voltage convention, TABLE/cnexp, cable propagation or measured physiology. Missing/unresolved events remain explicit; rest-root uniqueness and interval-Hurwitz stability are unclaimed.

### Study goals: 9 met, 1 unmet, 0 unresolved (10 total)

Mandatory qualification is separate from study-goal attainment. Met/unmet follow stored comparisons, not statistical certification. Unresolved and separate uncertainty classifications are retained; null is not replaced by false or zero.

[Original saved results / JSON](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/results/result.json)

<details><summary>Read every study-goal record</summary>

```json
{
  "schema_version": 1,
  "counts": {
    "met": 9,
    "unmet": 1,
    "unresolved": 0,
    "total": 10
  },
  "goals": [
    {
      "name": "HH/clamp-original1e-8/-80.0",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 4.711626791498169e-08,
        "target": 1e-08,
        "scope": "Maximum over ALL accepted times and all three gates; unmet outcomes retained"
      }
    },
    {
      "name": "HH/clamp-original1e-8/-55.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 7.262476731106915e-11,
        "target": 1e-08,
        "scope": "Maximum over ALL accepted times and all three gates; unmet outcomes retained"
      }
    },
    {
      "name": "HH/clamp-original1e-8/-40.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 1.4916989865554342e-10,
        "target": 1e-08,
        "scope": "Maximum over ALL accepted times and all three gates; unmet outcomes retained"
      }
    },
    {
      "name": "HH/clamp-original1e-8/0.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 7.521943623522986e-09,
        "target": 1e-08,
        "scope": "Maximum over ALL accepted times and all three gates; unmet outcomes retained"
      }
    },
    {
      "name": "HH/rest/0.04",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "target_mV": 1e-07
      }
    },
    {
      "name": "HH/rest/0.02",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "target_mV": 1e-07
      }
    },
    {
      "name": "HH/rest/0.01",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "target_mV": 1e-07
      }
    },
    {
      "name": "HH/pulse-voltage",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.00010511156826709112,
        "target": 0.05,
        "reference_spread": 1.0302887432089847e-09
      }
    },
    {
      "name": "HH/pulse-gates",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 5.371951350419124e-08,
        "target": 0.0001
      }
    },
    {
      "name": "HH/pulse-event",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual_ms": 3.799796033376879e-08,
        "target_ms": 0.01,
        "reason": null,
        "scope": "ObservedHermiteeventcomparison;exactODEeventcompletenessnotcertified"
      }
    }
  ],
  "classification_basis": "stored observed comparison; separate uncertainty classifications retained",
  "source": {
    "collection": "study_goals",
    "json_pointer": "/study_goals",
    "prefix": "HH/",
    "result_sha256": "104875b041a43542ec5d1500003da8f5986983816e27ce3b88971d11d7b63149",
    "acceptance_sha256": "47bb2050ccf15b2d404c2a3e63047d11d8258dc6feb25dc1e2fc14c3863b72ab",
    "result_url": "https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/results/result.json",
    "acceptance_url": "https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/acceptance.json"
  }
}
```

</details>

### Stored measurements and decisions

```json
{
  "metrics": {
    "fixed_records": 21,
    "HH/clamp-original1e-8/-80.0/actual": 4.711626791498169e-08,
    "HH/clamp-original1e-8/-55.0/actual": 7.262476731106915e-11,
    "HH/clamp-original1e-8/-40.0/actual": 1.4916989865554342e-10,
    "HH/clamp-original1e-8/0.0/actual": 7.521943623522986e-09,
    "HH/pulse-voltage/actual": 0.00010511156826709112,
    "HH/pulse-gates/actual": 5.371951350419124e-08,
    "HH/pulse-event/actual_ms": 3.799796033376879e-08
  },
  "checks": {
    "HH/rates_against_decimal": true,
    "HH/precision_companion": true,
    "HH/removable_singularities": true,
    "HH/rest_bracket_companion": true,
    "HH/owned_stage_edges": true,
    "HH/naive_jump_control_detected": true,
    "HH/clamp-finite-bounds/-80.0/0.04": true,
    "HH/clamp-finite-bounds/-80.0/0.02": true,
    "HH/clamp-finite-bounds/-80.0/0.01": true,
    "HH/clamp-finite-bounds/-55.0/0.04": true,
    "HH/clamp-finite-bounds/-55.0/0.02": true,
    "HH/clamp-finite-bounds/-55.0/0.01": true,
    "HH/clamp-finite-bounds/-40.0/0.04": true,
    "HH/clamp-finite-bounds/-40.0/0.02": true,
    "HH/clamp-finite-bounds/-40.0/0.01": true,
    "HH/clamp-finite-bounds/0.0/0.04": true,
    "HH/clamp-finite-bounds/0.0/0.02": true,
    "HH/clamp-finite-bounds/0.0/0.01": true,
    "HH/reference/rest": true,
    "HH/finite-gates/rest/0.04": true,
    "HH/finite-gates/rest/0.02": true,
    "HH/finite-gates/rest/0.01": true,
    "HH/reference/pulse": true,
    "HH/finite-gates/pulse/0.04": true,
    "HH/finite-gates/pulse/0.02": true,
    "HH/finite-gates/pulse/0.01": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/hodgkin-huxley-controls/index.json

![Separate actual accuracy,reference and statistical measurements,including unmet targets.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/results/hodgkin-huxley-controls-diagnostics.png)

Separate actual accuracy,reference and statistical measurements,including unmet targets.

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/atlas-biology-ode-controls-2026-11-25.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- NEURON8.2.6 analytic hh.mod. https://raw.githubusercontent.com/neuronsimulator/nrn/8.2.6/src/nrnoc/hh.mod; review_level=selected-primary-or-bibliographic-see-provenance
Actual selected read scopes and unread limits are recorded in source-reading.json; no full original-paper equation/figure reproduction claim.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## Immigration–death SSA: exact transient laws

Separate one displayed path from12,288fixed ensemble paths.

**Methods used**

- [Gillespie direct stochastic simulation (SSA)](https://hrkoyama.github.io/numerical-methods-atlas/methods/gillespie-ssa/?lang=en) (`gillespie-ssa`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/immigration-death-ssa/?lang=en#immigration-death-ssa-en-algorithm)

Use direct GillespieSSA with pending event times preserved across observations. Draw open-grid uniforms from rawPCG64; record finite-grid Poisson initialization and all RNG streams.

$$
\varnothing\xrightarrow{6}N,\qquad N\xrightarrow{N} \varnothing
$$

$$
N(t)\overset d=\mathrm{Bin}(n_0,e^{-t})+\mathrm{Pois}(6(1-e^{-t}))
$$

- [Chemical master equation and Gillespie SSA](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-chemical-master-en) (`bio-chemical-master`)

Use immigration6, per-particle death1 and observations0/0.5/2/4. Compare initial0,5 and nominal stationary Poisson(6), two seeds each and2,048paths per record.

- [Immigration–death reaction and exact transient law](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#immigration-death-model-en) (`immigration-death-model`)

Use immigration6, per-particle death1 and observations0/0.5/2/4. Compare initial0,5 and nominal stationary Poisson(6), two seeds each and2,048paths per record.


**Problem figure**

![Immigration–death SSA: exact transient laws: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/results/immigration-death-ssa.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Immigration–death SSA: exact transient laws](https://hrkoyama.github.io/numerical-methods-atlas/problems/immigration-death-ssa/?lang=en) (`immigration-death-ssa`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/immigration-death-ssa/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/immigration-death-ssa/?lang=en#immigration-death-ssa-en-validation)

Qualify exact Binomial-plus-Poisson transients with directed80/120digit intervals and tail bounds. Combine20DKW and20exact-sum mean goals under nominal union bound0.01; retain five-SE variance goals separately.

- [Immigration–death SSA: exact transient laws](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-immigration-death-ssa-en) (`immigration-death-ssa`; Same-problem reference · Analytic reference)

Finite deterministic-start transients are not stationary. Interval qualification concerns the idealIID reference law, without a whole-software PRNG/logarithm coverage guarantee or a claim that one path represents the ensemble.
### Assumptions, units and boundaries

Use immigration6, per-particle death1 and observations0/0.5/2/4. Compare initial0,5 and nominal stationary Poisson(6), two seeds each and2,048paths per record.

**Editorial clarification**

Finite deterministic-start transients are not stationary. Interval qualification concerns the idealIID reference law, without a whole-software PRNG/logarithm coverage guarantee or a claim that one path represents the ensemble.

### Adopted numerical method

Use direct GillespieSSA with pending event times preserved across observations. Draw open-grid uniforms from rawPCG64; record finite-grid Poisson initialization and all RNG streams.

$$
\varnothing\xrightarrow{6}N,\qquad N\xrightarrow{N} \varnothing
$$

$$
N(t)\overset d=\mathrm{Bin}(n_0,e^{-t})+\mathrm{Pois}(6(1-e^{-t}))
$$

### References and validation

Qualify exact Binomial-plus-Poisson transients with directed80/120digit intervals and tail bounds. Combine20DKW and20exact-sum mean goals under nominal union bound0.01; retain five-SE variance goals separately.

### Limits

Finite deterministic-start transients are not stationary. Interval qualification concerns the idealIID reference law, without a whole-software PRNG/logarithm coverage guarantee or a claim that one path represents the ensemble.

### Study goals: 40 met, 0 unmet, 0 unresolved (40 total)

Mandatory qualification is separate from study-goal attainment. Met/unmet follow stored comparisons, not statistical certification. Unresolved and separate uncertainty classifications are retained; null is not replaced by false or zero.

[Original saved results / JSON](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/results/result.json)

<details><summary>Read every study-goal record</summary>

```json
{
  "schema_version": 1,
  "counts": {
    "met": 40,
    "unmet": 0,
    "unresolved": 0,
    "total": 40
  },
  "goals": [
    {
      "name": "SSA/DKW/0/1",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.0044938265744222106,
        "epsilon": 0.046841646520958534
      }
    },
    {
      "name": "SSA/exact-mean/0/1",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "sum": 4830,
        "bounds": [
          4582,
          5092
        ]
      }
    },
    {
      "name": "SSA/DKW/0/2",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.011554936819670791,
        "epsilon": 0.046841646520958534
      }
    },
    {
      "name": "SSA/exact-mean/0/2",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "sum": 10708,
        "bounds": [
          10250,
          11005
        ]
      }
    },
    {
      "name": "SSA/DKW/0/3",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.01814154306809468,
        "epsilon": 0.046841646520958534
      }
    },
    {
      "name": "SSA/exact-mean/0/3",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "sum": 11935,
        "bounds": [
          11663,
          12467
        ]
      }
    },
    {
      "name": "SSA/DKW/1/1",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.0059642975343668775,
        "epsilon": 0.046841646520958534
      }
    },
    {
      "name": "SSA/exact-mean/1/1",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "sum": 4851,
        "bounds": [
          4582,
          5092
        ]
      }
    },
    {
      "name": "SSA/DKW/1/2",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.019536382644266714,
        "epsilon": 0.046841646520958534
      }
    },
    {
      "name": "SSA/exact-mean/1/2",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "sum": 10775,
        "bounds": [
          10250,
          11005
        ]
      }
    },
    {
      "name": "SSA/DKW/1/3",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.01048461957478325,
        "epsilon": 0.046841646520958534
      }
    },
    {
      "name": "SSA/exact-mean/1/3",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "sum": 12142,
        "bounds": [
          11663,
          12467
        ]
      }
    },
    {
      "name": "SSA/DKW/2/1",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.01601739601069163,
        "epsilon": 0.046841646520958534
      }
    },
    {
      "name": "SSA/exact-mean/2/1",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "sum": 10934,
        "bounds": [
          10735,
          11359
        ]
      }
    },
    {
      "name": "SSA/DKW/2/2",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.009983568643240626,
        "epsilon": 0.046841646520958534
      }
    },
    {
      "name": "SSA/exact-mean/2/2",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "sum": 11938,
        "bounds": [
          11615,
          12411
        ]
      }
    },
    {
      "name": "SSA/DKW/2/3",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.00685998885581765,
        "epsilon": 0.046841646520958534
      }
    },
    {
      "name": "SSA/exact-mean/2/3",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "sum": 12211,
        "bounds": [
          11847,
          12658
        ]
      }
    },
    {
      "name": "SSA/DKW/3/1",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.016697788968076333,
        "epsilon": 0.046841646520958534
      }
    },
    {
      "name": "SSA/exact-mean/3/1",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "sum": 10912,
        "bounds": [
          10735,
          11359
        ]
      }
    },
    {
      "name": "SSA/DKW/3/2",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.014638919344433177,
        "epsilon": 0.046841646520958534
      }
    },
    {
      "name": "SSA/exact-mean/3/2",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "sum": 11957,
        "bounds": [
          11615,
          12411
        ]
      }
    },
    {
      "name": "SSA/DKW/3/3",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.01647513015314328,
        "epsilon": 0.046841646520958534
      }
    },
    {
      "name": "SSA/exact-mean/3/3",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "sum": 12256,
        "bounds": [
          11847,
          12658
        ]
      }
    },
    {
      "name": "SSA/DKW/4/0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.027464889885388755,
        "epsilon": 0.046841646520958534
      }
    },
    {
      "name": "SSA/exact-mean/4/0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "sum": 12045,
        "bounds": [
          11884,
          12696
        ]
      }
    },
    {
      "name": "SSA/DKW/4/1",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.016762427046282946,
        "epsilon": 0.046841646520958534
      }
    },
    {
      "name": "SSA/exact-mean/4/1",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "sum": 12243,
        "bounds": [
          11884,
          12696
        ]
      }
    },
    {
      "name": "SSA/DKW/4/2",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.008400530933368788,
        "epsilon": 0.046841646520958534
      }
    },
    {
      "name": "SSA/exact-mean/4/2",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "sum": 12237,
        "bounds": [
          11884,
          12696
        ]
      }
    },
    {
      "name": "SSA/DKW/4/3",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.014281296135388755,
        "epsilon": 0.046841646520958534
      }
    },
    {
      "name": "SSA/exact-mean/4/3",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "sum": 12245,
        "bounds": [
          11884,
          12696
        ]
      }
    },
    {
      "name": "SSA/DKW/5/0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.018227270796282946,
        "epsilon": 0.046841646520958534
      }
    },
    {
      "name": "SSA/exact-mean/5/0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "sum": 12134,
        "bounds": [
          11884,
          12696
        ]
      }
    },
    {
      "name": "SSA/DKW/5/1",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.02549037468336879,
        "epsilon": 0.046841646520958534
      }
    },
    {
      "name": "SSA/exact-mean/5/1",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "sum": 12166,
        "bounds": [
          11884,
          12696
        ]
      }
    },
    {
      "name": "SSA/DKW/5/2",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.018433547614611245,
        "epsilon": 0.046841646520958534
      }
    },
    {
      "name": "SSA/exact-mean/5/2",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "sum": 12379,
        "bounds": [
          11884,
          12696
        ]
      }
    },
    {
      "name": "SSA/DKW/5/3",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.013083844066631212,
        "epsilon": 0.046841646520958534
      }
    },
    {
      "name": "SSA/exact-mean/5/3",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "sum": 12333,
        "bounds": [
          11884,
          12696
        ]
      }
    }
  ],
  "classification_basis": "stored observed comparison; separate uncertainty classifications retained",
  "source": {
    "collection": "study_goals",
    "json_pointer": "/study_goals",
    "prefix": "SSA/",
    "result_sha256": "104875b041a43542ec5d1500003da8f5986983816e27ce3b88971d11d7b63149",
    "acceptance_sha256": "47bb2050ccf15b2d404c2a3e63047d11d8258dc6feb25dc1e2fc14c3863b72ab",
    "result_url": "https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/results/result.json",
    "acceptance_url": "https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/acceptance.json"
  }
}
```

</details>

### Stored measurements and decisions

```json
{
  "metrics": {
    "fixed_records": 9,
    "SSA/DKW/0/1/actual": 0.0044938265744222106,
    "SSA/DKW/0/2/actual": 0.011554936819670791,
    "SSA/DKW/0/3/actual": 0.01814154306809468,
    "SSA/DKW/1/1/actual": 0.0059642975343668775,
    "SSA/DKW/1/2/actual": 0.019536382644266714,
    "SSA/DKW/1/3/actual": 0.01048461957478325,
    "SSA/DKW/2/1/actual": 0.01601739601069163,
    "SSA/DKW/2/2/actual": 0.009983568643240626,
    "SSA/DKW/2/3/actual": 0.00685998885581765,
    "SSA/DKW/3/1/actual": 0.016697788968076333,
    "SSA/DKW/3/2/actual": 0.014638919344433177,
    "SSA/DKW/3/3/actual": 0.01647513015314328,
    "SSA/DKW/4/0/actual": 0.027464889885388755,
    "SSA/DKW/4/1/actual": 0.016762427046282946,
    "SSA/DKW/4/2/actual": 0.008400530933368788,
    "SSA/DKW/4/3/actual": 0.014281296135388755,
    "SSA/DKW/5/0/actual": 0.018227270796282946,
    "SSA/DKW/5/1/actual": 0.02549037468336879,
    "SSA/DKW/5/2/actual": 0.018433547614611245,
    "SSA/DKW/5/3/actual": 0.013083844066631212
  },
  "checks": {
    "SSA/pending_boundary_and_censoring": true,
    "SSA/pending_not_redrawn_at_observations": true,
    "SSA/initial_inverse_monotone": true,
    "SSA/open_grid_limits": true,
    "SSA/reaction_equality_is_death": true,
    "SSA/wrong_stationarity_control": true,
    "SSA/law/0/0.5/1": true,
    "SSA/law/0/2.0/1": true,
    "SSA/law/0/4.0/1": true,
    "SSA/law/5/0.5/1": true,
    "SSA/law/5/2.0/1": true,
    "SSA/law/5/4.0/1": true,
    "SSA/law/stationary/0.0/1": true,
    "SSA/law/0/0.5/2048": true,
    "SSA/law/0/2.0/2048": true,
    "SSA/law/0/4.0/2048": true,
    "SSA/law/5/0.5/2048": true,
    "SSA/law/5/2.0/2048": true,
    "SSA/law/5/4.0/2048": true,
    "SSA/law/stationary/0.0/2048": true,
    "SSA/t0/0": true,
    "SSA/t0/1": true,
    "SSA/t0/2": true,
    "SSA/t0/3": true,
    "SSA/exact-family-count": true,
    "SSA/stream-namespaces-unique": true,
    "SSA/all-24578-initial-PCG-state-inc-pairs-unique": true,
    "SSA/all-24578-stream-labels-unique": true,
    "SSA/all-paths": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/immigration-death-ssa/index.json

![Separate actual accuracy,reference and statistical measurements,including unmet targets.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/results/immigration-death-ssa-diagnostics.png)

Separate actual accuracy,reference and statistical measurements,including unmet targets.

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/atlas-biology-ode-controls-2026-11-25.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- Gillespie(1977), Exact stochastic simulation of coupled chemical reactions. https://doi.org/10.1021/j100540a008; review_level=selected-primary-or-bibliographic-see-provenance
Actual selected read scopes and unread limits are recorded in source-reading.json; no full original-paper equation/figure reproduction claim.

- Massart(1990),The Tight Constant in the Dvoretzky–Kiefer–Wolfowitz Inequality. https://doi.org/10.1214/aop/1176990746; review_level=selected-primary-abstract
Selected original abstract on the author-uploaded page:IID/two-sidedconstant2. Official body access was blocked by an iframe; proof unread.

- Reeve(2024),A short proof of the Dvoretzky–Kiefer–Wolfowitz–Massart inequality. https://arxiv.org/pdf/2403.16651; review_level=selected-primary-theorem
Selected v1pp1–3:IIDsetup,Theorem1,Corollaries1/2. Detailed proofs unread.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
