# DAE initialization, conservation and constraint drift

Compare consistent initialization, an index-one conservation DAE, and an underlying ODE for an index-three pendulum. Comparisons with stored official IDA output are distinguished from newly executed independent ODE references.

These additional validation supplements are managed separately from the common 22-example registry. Receipts cover independent ZIP extraction, tests and every fixed input within each group. Changes of settings, methods or step sizes do not add independent physical problems.

## Consistent initialization and discrete residuals for an index-one DAE

Separate initialization, backward-Euler error and residuals on a known positive index-one DAE branch.

**Methods used**

- [Differential-algebraic equations / DAE](https://hrkoyama.github.io/numerical-methods-atlas/methods/dae/?lang=en) (`dae`)
- [Backward Euler](https://hrkoyama.github.io/numerical-methods-atlas/methods/backward-euler/?lang=en) (`backward-euler`)
- [Armijo-damped Newton](https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=en) (`newton`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/index1-dae-consistent-initialization/?lang=en#index1-dae-consistent-initialization-en-algorithm)

Use coupled Newton with an Armijo search in the same scaled norm, retaining rather than repairing a singular initial guess.

$$
F1=ydot+y-z+exp(-2t/3), F2=z^3-y^2
$$

$$
y=exp(-t), z=exp(-2t/3)
$$

- [Semi-explicit index-one DAE](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#index-one-dae-en) (`index-one-dae`)

Dimensionless positive branch; differential and algebraic row scales are both one, with the maximum norm.


**Problem figure**

![Consistent initialization and discrete residuals for an index-one DAE: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/index1-dae-consistent-initialization.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Consistent initialization and discrete residuals for an index-one DAE](https://hrkoyama.github.io/numerical-methods-atlas/problems/index1-dae-consistent-initialization/?lang=en) (`index1-dae-consistent-initialization`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/index1-dae-consistent-initialization/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/index1-dae-consistent-initialization/?lang=en#index1-dae-consistent-initialization-en-validation)

Compare independent Decimal manufactured states, three discrete roots and three fixed grids, checking first-order error and the algebraic constraint.

- [Consistent initialization and discrete residuals for an index-one DAE](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-index1-dae-consistent-initialization-en) (`index1-dae-consistent-initialization`; Same-problem reference · Manufactured solution)

One authored positive branch and fixed BE runs; no IDA execution or general DAE-solver qualification.
### Assumptions, units and boundaries

Dimensionless positive branch; differential and algebraic row scales are both one, with the maximum norm.

**Editorial clarification**

One authored positive branch and fixed BE runs; no IDA execution or general DAE-solver qualification. Axes for trajectories, states, time or iterations do not represent physical spatial dimensions.

### Adopted numerical method

Use coupled Newton with an Armijo search in the same scaled norm, retaining rather than repairing a singular initial guess.

$$
F1=ydot+y-z+exp(-2t/3), F2=z^3-y^2
$$

$$
y=exp(-t), z=exp(-2t/3)
$$

### References and validation

Compare independent Decimal manufactured states, three discrete roots and three fixed grids, checking first-order error and the algebraic constraint.

### Limits

One authored positive branch and fixed BE runs; no IDA execution or general DAE-solver qualification.

### Stored measurements and decisions

```json
{
  "metrics": {
    "reference:three-independent-discrete-roots": 3.5860203695392556e-14,
    "initialize-0.5:root": 0.0,
    "initialize-2:root": 2.220446049250313e-16,
    "index1-BE-16:step-residual": 9.536815781530095e-14,
    "index1-BE-16:constraint": 9.536815781530095e-14,
    "index1-BE-16:MMS-bound": 0.017655667991177793,
    "index1-BE-32:step-residual": 1.5543122344752192e-15,
    "index1-BE-32:constraint": 4.440892098500626e-16,
    "index1-BE-32:MMS-bound": 0.00889059915166246,
    "index1-BE-64:step-residual": 3.552713678800501e-15,
    "index1-BE-64:constraint": 3.3306690738754696e-16,
    "index1-BE-64:MMS-bound": 0.0044611112911168704,
    "first-order-refinement": [
      0.989778852631791,
      0.9948775084516599
    ],
    "finest_max_state_error": 0.0044611112911168704,
    "observed_orders": [
      0.989778852631791,
      0.9948775084516599
    ],
    "one_step_reference_errors": [
      3.5860203695392556e-14,
      1.1102230246251565e-16,
      1.1102230246251565e-16
    ],
    "original_targets_met": 30,
    "original_targets_total": 30
  },
  "checks": {
    "reference:MMS-0": true,
    "reference:MMS-1": true,
    "reference:MMS-2": true,
    "reference:nonexpansive-positive-region": true,
    "reference:initial-differentiated-constraint": true,
    "reference:three-positive-branch-brackets": true,
    "reference:three-independent-discrete-roots": true,
    "initialize-0.5:root": true,
    "initialize-0.5:algebraic-residual": true,
    "initialize-2:root": true,
    "initialize-2:algebraic-residual": true,
    "initialize-0:expected-singular-status": true,
    "index1-BE-16:finite": true,
    "index1-BE-16:positive": true,
    "index1-BE-16:step-residual": true,
    "index1-BE-16:constraint": true,
    "index1-BE-16:MMS-bound": true,
    "index1-BE-32:finite": true,
    "index1-BE-32:positive": true,
    "index1-BE-32:step-residual": true,
    "index1-BE-32:constraint": true,
    "index1-BE-32:MMS-bound": true,
    "index1-BE-64:finite": true,
    "index1-BE-64:positive": true,
    "index1-BE-64:step-residual": true,
    "index1-BE-64:constraint": true,
    "index1-BE-64:MMS-bound": true,
    "first-order-refinement": true,
    "initial-F-and-hidden-constraint": true,
    "six-record-identities": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/index1-dae-consistent-initialization/index.json

![Separate initialization, backward-Euler error and residuals on a known positive index-one DAE branch. Drawn from saved arrays.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/index1-dae-consistent-initialization-preview.png)

Separate initialization, backward-Euler error and residuals on a known positive index-one DAE branch. Drawn from saved arrays.

![Saved residuals, constraints and budgets shown separately; symmetric log axes retain zero values.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/index1-dae-consistent-initialization-diagnostics.png)

Saved residuals, constraints and budgets shown separately; symmetric log axes retain zero values.

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/atlas-dae-controls-2026-11-24.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- SUNDIALS v7.1.1 IDA mathematics, section 5.2 [accessed 2026-11-24]. https://sundials.readthedocs.io/en/v7.1.1/ida/Mathematics_link.html; review_level=official-documentation-selected-equations
Residual form, BDF/Newton and consistent initialization sections selected. Section5.2 is not an IDA version. This authored MMS/BE solver is not IDA.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## Robertson conservation DAE and stored official IDA values

Compare the Robertson conservation DAE and full ODE on the same fixed time grids, with a separate check of stored official IDA values. The first retained run missed four original time-accuracy and refinement goals.

**Methods used**

- [Differential-algebraic equations / DAE](https://hrkoyama.github.io/numerical-methods-atlas/methods/dae/?lang=en) (`dae`)
- [Backward Euler](https://hrkoyama.github.io/numerical-methods-atlas/methods/backward-euler/?lang=en) (`backward-euler`)
- [Armijo-damped Newton](https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=en) (`newton`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-conservation-dae/?lang=en#robertson-conservation-dae-en-algorithm)

Use fixed BE/Newton with analytic Jacobians and no mass projection or concentration clipping.

$$
F1=ydot1+0.04*y1-1e4*y2*y3; F2=ydot2-0.04*y1+1e4*y2*y3+3e7*y2^2; F3=y1+y2+y3-1
$$

$$
M=diag(1,1,0)
$$

- [Robertson chemical kinetics](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#robertson-kinetics-en) (`robertson-kinetics`)

Model time zero to four; the intermediate-species state and residual scale is 1e-4. Printing intervals and numerical errors are distinct.

- [Semi-explicit index-one DAE](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#index-one-dae-en) (`index-one-dae`)

Model time zero to four; the intermediate-species state and residual scale is 1e-4. Printing intervals and numerical errors are distinct.


**Problem figure**

![Robertson conservation DAE and stored official IDA values: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/robertson-conservation-dae.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Robertson kinetics: ODE and conservation DAE](https://hrkoyama.github.io/numerical-methods-atlas/problems/robertson-stiff-kinetics/?lang=en) (`robertson-stiff-kinetics`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/robertson-stiff-kinetics/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-conservation-dae/?lang=en#robertson-conservation-dae-en-validation)

Evaluate all 39 original targets, retaining the four unmet accuracy/refinement goals as study outcomes. The other 35 requirements, independent references and faithful saved-array recomputation remain mandatory.

- [Robertson kinetics: initial stiffness and actual error](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-robertson-stiff-kinetics-en) (`robertson-stiff-kinetics`; Same-problem reference · Finite-grid numerical reference)

Conservation and positivity are observations for these inputs, not universal guarantees. Accuracy is sampled on T <= 0.4; this does not validate long-time chemistry or an all-time error bound.

- [Robertson conservation DAE and stored official IDA values](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-robertson-conservation-dae-en) (`robertson-conservation-dae`; Same-problem reference · Finite-grid numerical reference)

Only two official SUNDIALS v7.1.1 printed rows; zero new IDA executions, with no long-time chemistry or general DAE-performance claim. No asymptotic-convergence or all-original-accuracy-goals claim is made for this fixed schedule.
### Assumptions, units and boundaries

Model time zero to four; the intermediate-species state and residual scale is 1e-4. Printing intervals and numerical errors are distinct.

**Editorial clarification**

Only two official SUNDIALS v7.1.1 printed rows; zero new IDA executions, with no long-time chemistry or general DAE-performance claim. No asymptotic-convergence or all-original-accuracy-goals claim is made for this fixed schedule. Axes for trajectories, states, time or iterations do not represent physical spatial dimensions.

### Adopted numerical method

Use fixed BE/Newton with analytic Jacobians and no mass projection or concentration clipping.

$$
F1=ydot1+0.04*y1-1e4*y2*y3; F2=ydot2-0.04*y1+1e4*y2*y3+3e7*y2^2; F3=y1+y2+y3-1
$$

$$
M=diag(1,1,0)
$$

### References and validation

Evaluate all 39 original targets, retaining the four unmet accuracy/refinement goals as study outcomes. The other 35 requirements, independent references and faithful saved-array recomputation remain mandatory.

### Limits

Only two official SUNDIALS v7.1.1 printed rows; zero new IDA executions, with no long-time chemistry or general DAE-performance claim. No asymptotic-convergence or all-original-accuracy-goals claim is made for this fixed schedule.

### Original numerical targets and unmet outcomes

Passing reproduction/reporting verification does not mean that all original accuracy goals were met. Original decisions are retained.

```json
{
  "original_target_results": {
    "reference:all-reference-complete-finite-nonnegative": true,
    "reference:reference-agreement-0": true,
    "reference:reference-agreement-2": true,
    "reference:official-IDA-printed-interval-qualification": true,
    "inconsistent-initial-rejected": true,
    "robertson-residual_dae-r1:finite": true,
    "robertson-residual_dae-r1:nonnegative": true,
    "robertson-residual_dae-r1:nonlinear-residual": true,
    "robertson-residual_dae-r1:mass": true,
    "robertson-residual_dae-r2:finite": true,
    "robertson-residual_dae-r2:nonnegative": true,
    "robertson-residual_dae-r2:nonlinear-residual": true,
    "robertson-residual_dae-r2:mass": true,
    "robertson-residual_dae-r4:finite": true,
    "robertson-residual_dae-r4:nonnegative": true,
    "robertson-residual_dae-r4:nonlinear-residual": true,
    "robertson-residual_dae-r4:mass": true,
    "residual_dae:refinement": false,
    "residual_dae:finest-reference-error": false,
    "residual_dae:official-printed-comparison": true,
    "robertson-full_ode-r1:finite": true,
    "robertson-full_ode-r1:nonnegative": true,
    "robertson-full_ode-r1:nonlinear-residual": true,
    "robertson-full_ode-r1:mass": true,
    "robertson-full_ode-r2:finite": true,
    "robertson-full_ode-r2:nonnegative": true,
    "robertson-full_ode-r2:nonlinear-residual": true,
    "robertson-full_ode-r2:mass": true,
    "robertson-full_ode-r4:finite": true,
    "robertson-full_ode-r4:nonnegative": true,
    "robertson-full_ode-r4:nonlinear-residual": true,
    "robertson-full_ode-r4:mass": true,
    "full_ode:refinement": false,
    "full_ode:finest-reference-error": false,
    "full_ode:official-printed-comparison": true,
    "ODE-DAE-r1": true,
    "ODE-DAE-r2": true,
    "ODE-DAE-r4": true,
    "seven-record-identities": true
  },
  "original_target_summary": {
    "met": 35,
    "total": 39,
    "all_met": false,
    "acceptance_sha256": "de0c9378204b8b08610318f41d98efb95cc2c31048a6b593707197635a0cba96"
  }
}
```

### Stored measurements and decisions

```json
{
  "metrics": {
    "robertson-residual_dae-r1:nonnegative": 0.0,
    "robertson-residual_dae-r1:nonlinear-residual": 1.0710574122841998e-12,
    "robertson-residual_dae-r1:mass": 2.220446049250313e-16,
    "robertson-residual_dae-r2:nonnegative": 0.0,
    "robertson-residual_dae-r2:nonlinear-residual": 1.9804734758359423e-12,
    "robertson-residual_dae-r2:mass": 2.220446049250313e-16,
    "robertson-residual_dae-r4:nonnegative": 0.0,
    "robertson-residual_dae-r4:nonlinear-residual": 9.182101846032633e-13,
    "robertson-residual_dae-r4:mass": 2.220446049250313e-16,
    "residual_dae:refinement": [
      1.0816554513576002,
      1.7211244337110214
    ],
    "residual_dae:finest-reference-error": 0.007755772186054176,
    "residual_dae:official-printed-comparison": [
      [
        0.0,
        0.0,
        1.98496998732485e-06
      ],
      [
        2.8469832178190657e-05,
        3.4259947900275225e-09,
        3.737975817291739e-05
      ]
    ],
    "robertson-full_ode-r1:nonnegative": 0.0,
    "robertson-full_ode-r1:nonlinear-residual": 1.0707354074153451e-12,
    "robertson-full_ode-r1:mass": 4.440892098500626e-16,
    "robertson-full_ode-r2:nonnegative": 0.0,
    "robertson-full_ode-r2:nonlinear-residual": 1.980642882425393e-12,
    "robertson-full_ode-r2:mass": 1.5543122344752192e-15,
    "robertson-full_ode-r4:nonnegative": 0.0,
    "robertson-full_ode-r4:nonlinear-residual": 9.182101846032633e-13,
    "robertson-full_ode-r4:mass": 8.881784197001252e-16,
    "full_ode:refinement": [
      1.0816554513576304,
      1.72112443371103
    ],
    "full_ode:finest-reference-error": 0.007755772186054176,
    "full_ode:official-printed-comparison": [
      [
        0.0,
        0.0,
        1.9849699872138277e-06
      ],
      [
        2.8469832178079635e-05,
        3.4259947900546275e-09,
        3.737975817323658e-05
      ]
    ],
    "ODE-DAE-r1": 8.131516293641283e-16,
    "ODE-DAE-r2": 2.100641709190665e-15,
    "ODE-DAE-r4": 8.809142651444724e-16,
    "finest_scaled_error_DAE": 0.007755772186054176,
    "finest_scaled_error_ODE": 0.007755772186054176,
    "reference_solver_counters": [
      {
        "id": "reference-radau-loose",
        "method": "Radau",
        "nfev": 4291,
        "njev": 43,
        "nlu": 166,
        "status": 0,
        "observations": 1537
      },
      {
        "id": "reference-radau-tight",
        "method": "Radau",
        "nfev": 12141,
        "njev": 9,
        "nlu": 124,
        "status": 0,
        "observations": 1537
      },
      {
        "id": "reference-bdf-tight",
        "method": "BDF",
        "nfev": 1593,
        "njev": 3,
        "nlu": 110,
        "status": 0,
        "observations": 1537
      }
    ],
    "IDA_new_executions": 0,
    "original_targets_met": 35,
    "original_targets_total": 39
  },
  "checks": {
    "reference:all-reference-complete-finite-nonnegative": true,
    "reference:reference-agreement-0": true,
    "reference:reference-agreement-2": true,
    "reference:official-IDA-printed-interval-qualification": true,
    "inconsistent-initial-rejected": true,
    "robertson-residual_dae-r1:finite": true,
    "robertson-residual_dae-r1:nonnegative": true,
    "robertson-residual_dae-r1:nonlinear-residual": true,
    "robertson-residual_dae-r1:mass": true,
    "robertson-residual_dae-r2:finite": true,
    "robertson-residual_dae-r2:nonnegative": true,
    "robertson-residual_dae-r2:nonlinear-residual": true,
    "robertson-residual_dae-r2:mass": true,
    "robertson-residual_dae-r4:finite": true,
    "robertson-residual_dae-r4:nonnegative": true,
    "robertson-residual_dae-r4:nonlinear-residual": true,
    "robertson-residual_dae-r4:mass": true,
    "residual_dae:official-printed-comparison": true,
    "robertson-full_ode-r1:finite": true,
    "robertson-full_ode-r1:nonnegative": true,
    "robertson-full_ode-r1:nonlinear-residual": true,
    "robertson-full_ode-r1:mass": true,
    "robertson-full_ode-r2:finite": true,
    "robertson-full_ode-r2:nonnegative": true,
    "robertson-full_ode-r2:nonlinear-residual": true,
    "robertson-full_ode-r2:mass": true,
    "robertson-full_ode-r4:finite": true,
    "robertson-full_ode-r4:nonnegative": true,
    "robertson-full_ode-r4:nonlinear-residual": true,
    "robertson-full_ode-r4:mass": true,
    "full_ode:official-printed-comparison": true,
    "ODE-DAE-r1": true,
    "ODE-DAE-r2": true,
    "ODE-DAE-r4": true,
    "seven-record-identities": true,
    "verification:original-target-inventory": true,
    "verification:all-original-decisions-recomputed": true,
    "verification:measured-records-match-saved-arrays": true,
    "verification:frozen-original-input-and-acceptance": true,
    "verification:independent-reference-integrity": true,
    "verification:actual-target-summary": true,
    "verification:retained-first-attempt-history": true,
    "verification:only-declared-study-goals-are-nonmandatory": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-conservation-dae/index.json

![Compare the Robertson conservation DAE and full ODE on the same fixed time grids, with a separate check of stored official IDA values. Drawn from saved arrays. The first-run goal shortfall and each rerun’s actual target decisions remain explicit in the saved JSON.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/robertson-conservation-dae-preview.png)

Compare the Robertson conservation DAE and full ODE on the same fixed time grids, with a separate check of stored official IDA values. Drawn from saved arrays. The first-run goal shortfall and each rerun’s actual target decisions remain explicit in the saved JSON.

![Saved residuals, constraints and budgets shown separately; symmetric log axes retain zero values. The first-run goal shortfall and each rerun’s actual target decisions remain explicit in the saved JSON.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/robertson-conservation-dae-diagnostics.png)

Saved residuals, constraints and budgets shown separately; symmetric log axes retain zero values. The first-run goal shortfall and each rerun’s actual target decisions remain explicit in the saved JSON.

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/atlas-dae-controls-2026-11-24.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- SUNDIALS v7.1.1 idaRoberts_dns example [accessed 2026-11-24]. https://github.com/LLNL/sundials/blob/v7.1.1/examples/ida/serial/idaRoberts_dns.c; review_level=official-source-selected-functions
Read residual/Jacobian, initialization, tolerances and print format. Own first two residual rows have opposite sign and the same zero set.

- Stored official v7.1.1 IDA Robertson output [accessed 2026-11-24]. https://github.com/LLNL/sundials/blob/v7.1.1/examples/ida/serial/idaRoberts_dns.out; review_level=official-stored-output-selected-rows
Selected printed t=0.4 and4 values only, with Decimal rounding intervals. These approximate IDA values are not exact truth; no IDA run is performed here.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## Index reduction, constraint drift and explicit stabilization for a pendulum

Derive an explicit ODE from an index-three position constraint and compare drift and stabilization for consistent and inconsistent starts.

**Methods used**

- [Differential-algebraic equations / DAE](https://hrkoyama.github.io/numerical-methods-atlas/methods/dae/?lang=en) (`dae`)
- [Classical RK4](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=en) (`rk4`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/high-index-pendulum/?lang=en#high-index-pendulum-en-algorithm)

Advance the index-reduced ODE and a critical constraint-error extension with fixed RK4, integrating constraint work at the same stages.

$$
C=(q.q-1)/2, D=q.v, lambda=(v.v-q_y+2D+C)/(q.q)
$$

$$
Cddot+2*Cdot+C=0; Wdot=-lambda*(q.v)
$$

- [Constrained planar pendulum](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#constrained-pendulum-en) (`constrained-pendulum`)

m=L=g=1, initial angle 0.7 and zero angular velocity; off-manifold controls explicitly add radial velocity.

- [Hamiltonian systems and oscillators](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#hamiltonian-en) (`hamiltonian`)

m=L=g=1, initial angle 0.7 and zero angular velocity; off-manifold controls explicitly add radial velocity.


**Problem figure**

![Index reduction, constraint drift and explicit stabilization for a pendulum: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/high-index-pendulum.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Constrained planar pendulum](https://hrkoyama.github.io/numerical-methods-atlas/problems/high-index-pendulum/?lang=en) (`high-index-pendulum`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/high-index-pendulum/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/high-index-pendulum/?lang=en#high-index-pendulum-en-validation)

Qualify the Jacobi family against two independent angular ODE runs, then compare states, exact constraint laws and energy/work budgets.

- [Index reduction, constraint drift and explicit stabilization for a pendulum](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-high-index-pendulum-en) (`high-index-pendulum`; Same-problem reference · Semi-analytic reference)

No projection, normalization or SHAKE/RATTLE; no general index-three-solver or symplecticity claim.

- [SHAKE and RATTLE: constraints and momentum ownership](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-shake-rattle-pendulum-en) (`shake-rattle-pendulum`; Same-problem reference · Semi-analytic reference)

Original SHAKE and RATTLE full texts remain unread; selected author lecture notes were inspected. The finite-difference symplectic defect is a local proxy, not a general proof, and centered SHAKE velocity is not assigned RATTLE tangency.
### Assumptions, units and boundaries

m=L=g=1, initial angle 0.7 and zero angular velocity; off-manifold controls explicitly add radial velocity.

**Editorial clarification**

No projection, normalization or SHAKE/RATTLE; no general index-three-solver or symplecticity claim. Axes for trajectories, states, time or iterations do not represent physical spatial dimensions.

### Adopted numerical method

Advance the index-reduced ODE and a critical constraint-error extension with fixed RK4, integrating constraint work at the same stages.

$$
C=(q.q-1)/2, D=q.v, lambda=(v.v-q_y+2D+C)/(q.q)
$$

$$
Cddot+2*Cdot+C=0; Wdot=-lambda*(q.v)
$$

### References and validation

Qualify the Jacobi family against two independent angular ODE runs, then compare states, exact constraint laws and energy/work budgets.

### Limits

No projection, normalization or SHAKE/RATTLE; no general index-three-solver or symplecticity claim.

### Stored measurements and decisions

```json
{
  "metrics": {
    "pendulum-consistent-underlying-2000:state": 1.6288695170452172e-08,
    "pendulum-consistent-underlying-2000:energy": 1.1849681791353817e-08,
    "pendulum-consistent-stabilized-2000:state": 2.182399358452436e-09,
    "pendulum-consistent-stabilized-2000:energy": 1.2245648939313014e-10,
    "pendulum-radial-underlying-2000:C-law": 1.0557027235041927e-08,
    "pendulum-radial-underlying-2000:D-law": 1.037474827401963e-09,
    "pendulum-radial-underlying-2000:work-ledger": 4.06214124837323e-11,
    "pendulum-radial-stabilized-2000:C-law": 1.058986416895176e-10,
    "pendulum-radial-stabilized-2000:D-law": 1.113360997362714e-10,
    "pendulum-radial-stabilized-2000:work-ledger": 1.2632772794691789e-09,
    "underlying-consistent-fourth-order": [
      3.997663875510909,
      3.999093883138539
    ],
    "visible-unstabilized-drift": 0.019999989442972765,
    "stabilized-drift-ratio": 8.89400134498285e-10,
    "finest_consistent_state_error": 1.6288695170452172e-08,
    "observed_orders": [
      3.997663875510909,
      3.999093883138539
    ],
    "stabilized_to_unstabilized_drift_ratio": 8.89400134498285e-10,
    "reference_solver_counters": [
      {
        "id": "angular-reference-0",
        "method": "DOP853",
        "nfev": 1373,
        "njev": 0,
        "nlu": 0,
        "status": 0,
        "observations": 33
      },
      {
        "id": "angular-reference-1",
        "method": "DOP853",
        "nfev": 2273,
        "njev": 0,
        "nlu": 0,
        "status": 0,
        "observations": 33
      }
    ],
    "original_targets_met": 45,
    "original_targets_total": 45
  },
  "checks": {
    "reference:Jacobi-angular-agreement": true,
    "reference:angular-tolerance-agreement": true,
    "reference:Jacobi-initial": true,
    "reference:Jacobi-invariants": true,
    "reference:AGM-K": true,
    "reference:Decimal-remainder-qualification": true,
    "reference:constraint-identity-False": true,
    "reference:constraint-work-False": true,
    "reference:constraint-identity-True": true,
    "reference:constraint-work-True": true,
    "default-consistency-rejection": true,
    "pendulum-consistent-underlying-500:finite": true,
    "pendulum-consistent-underlying-500:radius": true,
    "pendulum-consistent-underlying-1000:finite": true,
    "pendulum-consistent-underlying-1000:radius": true,
    "pendulum-consistent-underlying-2000:finite": true,
    "pendulum-consistent-underlying-2000:radius": true,
    "pendulum-consistent-underlying-2000:state": true,
    "pendulum-consistent-underlying-2000:energy": true,
    "pendulum-consistent-stabilized-2000:finite": true,
    "pendulum-consistent-stabilized-2000:radius": true,
    "pendulum-consistent-stabilized-2000:state": true,
    "pendulum-consistent-stabilized-2000:energy": true,
    "pendulum-radial-underlying-500:finite": true,
    "pendulum-radial-underlying-500:radius": true,
    "pendulum-radial-underlying-1000:finite": true,
    "pendulum-radial-underlying-1000:radius": true,
    "pendulum-radial-underlying-2000:finite": true,
    "pendulum-radial-underlying-2000:radius": true,
    "pendulum-radial-underlying-2000:C-law": true,
    "pendulum-radial-underlying-2000:D-law": true,
    "pendulum-radial-underlying-2000:work-ledger": true,
    "pendulum-radial-stabilized-500:finite": true,
    "pendulum-radial-stabilized-500:radius": true,
    "pendulum-radial-stabilized-1000:finite": true,
    "pendulum-radial-stabilized-1000:radius": true,
    "pendulum-radial-stabilized-2000:finite": true,
    "pendulum-radial-stabilized-2000:radius": true,
    "pendulum-radial-stabilized-2000:C-law": true,
    "pendulum-radial-stabilized-2000:D-law": true,
    "pendulum-radial-stabilized-2000:work-ledger": true,
    "underlying-consistent-fourth-order": true,
    "visible-unstabilized-drift": true,
    "stabilized-drift-ratio": true,
    "eleven-record-identities": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/high-index-pendulum/index.json

![Derive an explicit ODE from an index-three position constraint and compare drift and stabilization for consistent and inconsistent starts. Drawn from saved arrays.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/high-index-pendulum-preview.png)

Derive an explicit ODE from an index-three position constraint and compare drift and stabilization for consistent and inconsistent starts. Drawn from saved arrays.

![Saved residuals, constraints and budgets shown separately; symmetric log axes retain zero values.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/high-index-pendulum-diagnostics.png)

Saved residuals, constraints and budgets shown separately; symmetric log axes retain zero values.

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/atlas-dae-controls-2026-11-24.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- NIST DLMF section22.19(i), pendulum [accessed 2026-11-24]. https://dlmf.nist.gov/22.19; review_level=official-reference-selected-equations
Selected pendulum formulas, phase and modulus convention. Authored Cartesian conversion uses K-t; SciPy takes parameter m=k². No full chapter reading claimed.

- NIST DLMF section19.8(i), arithmetic-geometric mean [accessed 2026-11-24]. https://dlmf.nist.gov/19.8; review_level=official-reference-selected-equations
Selected AGM/K identity; independent Decimal Machin pi and sine with explicit finite remainders qualify a single fixed modulus.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
