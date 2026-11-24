# Stiff ODEs, RK45 and boundary splitting

Small fixed inputs validate Robertson and van der Pol, RK45 interpolation/events, and splitting with inhomogeneous boundaries. Independent references distinguish local estimates from actual errors and temporal from spatial errors.

These additional validation supplements are managed separately from the common 22-example registry. Receipts cover independent ZIP extraction, tests and every fixed input within each group. Changes of settings, methods or step sizes do not add independent physical problems.

## Robertson kinetics: initial stiffness and actual error

Compare BDF2, SDIRK2 and adaptive step doubling on a short fixed interval against qualified Radau and BDF references.

**Methods used**

- [BDF2](https://hrkoyama.github.io/numerical-methods-atlas/methods/bdf2/?lang=en) (`bdf2`)
- [L-stable SDIRK2](https://hrkoyama.github.io/numerical-methods-atlas/methods/sdirk2/?lang=en) (`sdirk2`)
- [Adaptive SDIRK2 / step doubling](https://hrkoyama.github.io/numerical-methods-atlas/methods/step-doubling/?lang=en) (`step-doubling`)
- [Armijo-damped Newton](https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=en) (`newton`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-stiff-kinetics/?lang=en#robertson-stiff-kinetics-en-algorithm)

BDF2 starts with backward Euler on the same grid. SDIRK2 stages use a weighted maximum residual and reuse Jacobian factors only within one stage. Adaptive steps use an RMS step-doubling estimate and accept the two-half-step result.

$$
\dot y_1=-0.04y_1+10^4y_2y_3,\quad\dot y_2=-\dot y_1-3\!\times\!10^7y_2^2,\quad\dot y_3=3\!\times\!10^7y_2^2
$$

$$
\|r\|_{w,\infty}=\max_i|r_i|/w_i,\quad e_{\rm dbl}=(y_{h/2,h/2}-y_h)/3
$$

- [Robertson chemical kinetics](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#robertson-kinetics-en) (`robertson-kinetics`)

A nondimensional three-species system starts at (1, 0, 0) and ends at T = 0.4. The fixed methods use 512, 1024 and 2048 steps; two adaptive tolerance settings bring the total to eight runs.


**Problem figure**

![Robertson kinetics: initial stiffness and actual error: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/robertson-stiff-kinetics.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Robertson kinetics: ODE and conservation DAE](https://hrkoyama.github.io/numerical-methods-atlas/problems/robertson-stiff-kinetics/?lang=en) (`robertson-stiff-kinetics`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/robertson-stiff-kinetics/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-stiff-kinetics/?lang=en#robertson-stiff-kinetics-en-validation)

Check actual errors at 22 common times, mass and minimum values at every accepted state, true stage residuals, and actual RHS, Jacobian, factorization and linear-solve counts separately.

- [Robertson kinetics: initial stiffness and actual error](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-robertson-stiff-kinetics-en) (`robertson-stiff-kinetics`; Same-problem reference · Finite-grid numerical reference)

Conservation and positivity are observations for these inputs, not universal guarantees. Accuracy is sampled on T <= 0.4; this does not validate long-time chemistry or an all-time error bound.

- [Robertson conservation DAE and stored official IDA values](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-robertson-conservation-dae-en) (`robertson-conservation-dae`; Same-problem reference · Finite-grid numerical reference)

Only two official SUNDIALS v7.1.1 printed rows; zero new IDA executions, with no long-time chemistry or general DAE-performance claim. No asymptotic-convergence or all-original-accuracy-goals claim is made for this fixed schedule.
### Assumptions, units and boundaries

A nondimensional three-species system starts at (1, 0, 0) and ends at T = 0.4. The fixed methods use 512, 1024 and 2048 steps; two adaptive tolerance settings bring the total to eight runs.

**Editorial clarification**

Conservation and positivity are observations for these inputs, not universal guarantees. Accuracy is sampled on T <= 0.4; this does not validate long-time chemistry or an all-time error bound. Axes for trajectories, states, time or iterations do not represent physical spatial dimensions.

### Adopted numerical method

BDF2 starts with backward Euler on the same grid. SDIRK2 stages use a weighted maximum residual and reuse Jacobian factors only within one stage. Adaptive steps use an RMS step-doubling estimate and accept the two-half-step result.

$$
\dot y_1=-0.04y_1+10^4y_2y_3,\quad\dot y_2=-\dot y_1-3\!\times\!10^7y_2^2,\quad\dot y_3=3\!\times\!10^7y_2^2
$$

$$
\|r\|_{w,\infty}=\max_i|r_i|/w_i,\quad e_{\rm dbl}=(y_{h/2,h/2}-y_h)/3
$$

### References and validation

Check actual errors at 22 common times, mass and minimum values at every accepted state, true stage residuals, and actual RHS, Jacobian, factorization and linear-solve counts separately.

### Limits

Conservation and positivity are observations for these inputs, not universal guarantees. Accuracy is sampled on T <= 0.4; this does not validate long-time chemistry or an all-time error bound.

### Stored measurements and decisions

```json
{
  "metrics": {
    "maximum_sampled_weighted_error": 0.04388888512603525,
    "factorizations": 11711,
    "linear_solves": 23896,
    "factor_reuses": 12185,
    "accuracy_scope": "Fixed reference observation times only; all-step positivity/conservation separately tested. Stage residual norm is weightedLinf; adaptive estimator norm is RMS."
  },
  "checks": {
    "robertson-bdf2-512:complete-finite": true,
    "robertson-bdf2-512:true-stage-residual": true,
    "robertson-bdf2-512:mass": true,
    "robertson-bdf2-512:accepted-positivity": true,
    "robertson-bdf2-1024:complete-finite": true,
    "robertson-bdf2-1024:true-stage-residual": true,
    "robertson-bdf2-1024:mass": true,
    "robertson-bdf2-1024:accepted-positivity": true,
    "robertson-bdf2-2048:complete-finite": true,
    "robertson-bdf2-2048:true-stage-residual": true,
    "robertson-bdf2-2048:mass": true,
    "robertson-bdf2-2048:accepted-positivity": true,
    "robertson-sdirk2-512:complete-finite": true,
    "robertson-sdirk2-512:true-stage-residual": true,
    "robertson-sdirk2-512:mass": true,
    "robertson-sdirk2-512:accepted-positivity": true,
    "robertson-sdirk2-1024:complete-finite": true,
    "robertson-sdirk2-1024:true-stage-residual": true,
    "robertson-sdirk2-1024:mass": true,
    "robertson-sdirk2-1024:accepted-positivity": true,
    "robertson-sdirk2-2048:complete-finite": true,
    "robertson-sdirk2-2048:true-stage-residual": true,
    "robertson-sdirk2-2048:mass": true,
    "robertson-sdirk2-2048:accepted-positivity": true,
    "robertson-sdirk-doubling-loose:complete-finite": true,
    "robertson-sdirk-doubling-loose:true-stage-residual": true,
    "robertson-sdirk-doubling-loose:mass": true,
    "robertson-sdirk-doubling-loose:accepted-positivity": true,
    "robertson-sdirk-doubling-tight:complete-finite": true,
    "robertson-sdirk-doubling-tight:true-stage-residual": true,
    "robertson-sdirk-doubling-tight:mass": true,
    "robertson-sdirk-doubling-tight:accepted-positivity": true,
    "robertson-bdf2:finest-accuracy": true,
    "robertson-bdf2:refinement": true,
    "robertson-sdirk2:finest-accuracy": true,
    "robertson-sdirk2:refinement": true,
    "robertson-adaptive-loose:accuracy": true,
    "robertson-adaptive-tight:accuracy": true,
    "robertson-adaptive:actual-tolerance-response": true,
    "actual-within-stage-factor-reuse": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-stiff-kinetics/index.json

![Compare BDF2, SDIRK2 and adaptive step doubling on a short fixed interval against qualified Radau and BDF references. This preview reads saved numerical fields and references only.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/robertson-stiff-kinetics-preview.png)

Compare BDF2, SDIRK2 and adaptive step doubling on a short fixed interval against qualified Radau and BDF references. This preview reads saved numerical fields and references only.

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/atlas-ode-adaptivity-2026-11-24-r2.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- Official SUNDIALS cvRoberts_dns model definition [accessed 2026-11-24]. https://raw.githubusercontent.com/LLNL/sundials/main/examples/cvode/serial/cvRoberts_dns.c; review_level=official-source-selected-functions
Read the model, initial values and Jacobian in selected official source sections. The observed main URL is not an immutable release pin. Our T = 0.4 scope does not reproduce the original paper, the long 4e10 benchmark or its numerical tables.

- SciPy1.14.1 solve_ivp and selected official source [accessed 2026-11-24]. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.integrate.solve_ivp.html; review_level=official-selected-source
Read selected fixed-version method, API, local-tolerance and termination sections. This is not a full audit of the original research papers.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## Van der Pol: an early stiffness transition

Separate local control from global error. The first study met 208 of 209 original targets; the mu = 1 tight adaptive run missed the 2e-5 global goal.

**Methods used**

- [BDF2](https://hrkoyama.github.io/numerical-methods-atlas/methods/bdf2/?lang=en) (`bdf2`)
- [L-stable SDIRK2](https://hrkoyama.github.io/numerical-methods-atlas/methods/sdirk2/?lang=en) (`sdirk2`)
- [Adaptive SDIRK2 / step doubling](https://hrkoyama.github.io/numerical-methods-atlas/methods/step-doubling/?lang=en) (`step-doubling`)
- [Armijo-damped Newton](https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=en) (`newton`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/van-der-pol-stiff-transition/?lang=en#van-der-pol-stiff-transition-en-algorithm)

Use actual BDF2, SDIRK2 and adaptive step doubling, analytic Jacobians, factor reuse within each implicit stage, and retained candidates on failure.

$$
\dot x=v,\qquad \dot v=\mu(1-x^2)v-x,\quad\mu\in\{1,100\}
$$

- [Van der Pol oscillator](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#van-der-pol-en) (`van-der-pol`)

The system is xprime = v and vprime = mu(1 - x squared)v - x, initially (2, 0), over T = 2. Two fixed methods, three step counts and two mu values plus four adaptive runs give 16 runs.


**Problem figure**

![Van der Pol: an early stiffness transition: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/van-der-pol-stiff-transition.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Van der Pol: an early stiffness transition](https://hrkoyama.github.io/numerical-methods-atlas/problems/van-der-pol-stiff-transition/?lang=en) (`van-der-pol-stiff-transition`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/van-der-pol-stiff-transition/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/van-der-pol-stiff-transition/?lang=en#van-der-pol-stiff-transition-en-validation)

Compare 21 sampled times with qualified Radau and BDF references. Preserve every original decision, including false values. Require the other 208 conditions separately from three checks of faithful disclosure, actual local controls and retained original failure evidence.

- [Van der Pol: an early stiffness transition](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-van-der-pol-stiff-transition-en) (`van-der-pol-stiff-transition`; Same-problem reference · Finite-grid numerical reference)

This post-measurement reporting revision is not a numerical repair. The first error, 4.535633779e-5, exceeded the original 2e-5 goal. Local tolerances do not guarantee global accuracy, and reporting PASS does not mean all original goals were met. Full large-mu cycles are outside scope.
### Assumptions, units and boundaries

The system is xprime = v and vprime = mu(1 - x squared)v - x, initially (2, 0), over T = 2. Two fixed methods, three step counts and two mu values plus four adaptive runs give 16 runs.

**Editorial clarification**

This post-measurement reporting revision is not a numerical repair. The first error, 4.535633779e-5, exceeded the original 2e-5 goal. Local tolerances do not guarantee global accuracy, and reporting PASS does not mean all original goals were met. Full large-mu cycles are outside scope. Axes for trajectories, states, time or iterations do not represent physical spatial dimensions.

### Adopted numerical method

Use actual BDF2, SDIRK2 and adaptive step doubling, analytic Jacobians, factor reuse within each implicit stage, and retained candidates on failure.

$$
\dot x=v,\qquad \dot v=\mu(1-x^2)v-x,\quad\mu\in\{1,100\}
$$

### References and validation

Compare 21 sampled times with qualified Radau and BDF references. Preserve every original decision, including false values. Require the other 208 conditions separately from three checks of faithful disclosure, actual local controls and retained original failure evidence.

### Limits

This post-measurement reporting revision is not a numerical repair. The first error, 4.535633779e-5, exceeded the original 2e-5 goal. Local tolerances do not guarantee global accuracy, and reporting PASS does not mean all original goals were met. Full large-mu cycles are outside scope.

### Original numerical targets and unmet outcomes

Passing reproduction/reporting verification does not mean that all original accuracy goals were met. Original decisions are retained.

```json
{
  "original_target_results": {
    "vdp-mu1-bdf2-256:complete-finite": true,
    "vdp-mu1-bdf2-256:true-stage-residual": true,
    "vdp-mu1-bdf2-256:bounded-state": true,
    "vdp-mu1-bdf2-512:complete-finite": true,
    "vdp-mu1-bdf2-512:true-stage-residual": true,
    "vdp-mu1-bdf2-512:bounded-state": true,
    "vdp-mu1-bdf2-1024:complete-finite": true,
    "vdp-mu1-bdf2-1024:true-stage-residual": true,
    "vdp-mu1-bdf2-1024:bounded-state": true,
    "vdp-mu1-sdirk2-256:complete-finite": true,
    "vdp-mu1-sdirk2-256:true-stage-residual": true,
    "vdp-mu1-sdirk2-256:bounded-state": true,
    "vdp-mu1-sdirk2-512:complete-finite": true,
    "vdp-mu1-sdirk2-512:true-stage-residual": true,
    "vdp-mu1-sdirk2-512:bounded-state": true,
    "vdp-mu1-sdirk2-1024:complete-finite": true,
    "vdp-mu1-sdirk2-1024:true-stage-residual": true,
    "vdp-mu1-sdirk2-1024:bounded-state": true,
    "vdp-mu1-sdirk-doubling-loose:complete-finite": true,
    "vdp-mu1-sdirk-doubling-loose:true-stage-residual": true,
    "vdp-mu1-sdirk-doubling-loose:bounded-state": true,
    "vdp-mu1-sdirk-doubling-tight:complete-finite": true,
    "vdp-mu1-sdirk-doubling-tight:true-stage-residual": true,
    "vdp-mu1-sdirk-doubling-tight:bounded-state": true,
    "vdp-mu100-bdf2-256:complete-finite": true,
    "vdp-mu100-bdf2-256:true-stage-residual": true,
    "vdp-mu100-bdf2-256:bounded-state": true,
    "vdp-mu100-bdf2-512:complete-finite": true,
    "vdp-mu100-bdf2-512:true-stage-residual": true,
    "vdp-mu100-bdf2-512:bounded-state": true,
    "vdp-mu100-bdf2-1024:complete-finite": true,
    "vdp-mu100-bdf2-1024:true-stage-residual": true,
    "vdp-mu100-bdf2-1024:bounded-state": true,
    "vdp-mu100-sdirk2-256:complete-finite": true,
    "vdp-mu100-sdirk2-256:true-stage-residual": true,
    "vdp-mu100-sdirk2-256:bounded-state": true,
    "vdp-mu100-sdirk2-512:complete-finite": true,
    "vdp-mu100-sdirk2-512:true-stage-residual": true,
    "vdp-mu100-sdirk2-512:bounded-state": true,
    "vdp-mu100-sdirk2-1024:complete-finite": true,
    "vdp-mu100-sdirk2-1024:true-stage-residual": true,
    "vdp-mu100-sdirk2-1024:bounded-state": true,
    "vdp-mu100-sdirk-doubling-loose:complete-finite": true,
    "vdp-mu100-sdirk-doubling-loose:true-stage-residual": true,
    "vdp-mu100-sdirk-doubling-loose:bounded-state": true,
    "vdp-mu100-sdirk-doubling-tight:complete-finite": true,
    "vdp-mu100-sdirk-doubling-tight:true-stage-residual": true,
    "vdp-mu100-sdirk-doubling-tight:bounded-state": true,
    "vdp-mu1-bdf2:finest-accuracy": true,
    "vdp-mu1-bdf2:refinement": true,
    "vdp-mu1-sdirk2:finest-accuracy": true,
    "vdp-mu1-sdirk2:refinement": true,
    "vdp-mu1-adaptive-loose:accuracy": true,
    "vdp-mu1-adaptive-tight:accuracy": false,
    "vdp-mu1-adaptive:actual-tolerance-response": true,
    "vdp-mu100-bdf2:finest-accuracy": true,
    "vdp-mu100-bdf2:refinement": true,
    "vdp-mu100-sdirk2:finest-accuracy": true,
    "vdp-mu100-sdirk2:refinement": true,
    "vdp-mu100-adaptive-loose:accuracy": true,
    "vdp-mu100-adaptive-tight:accuracy": true,
    "vdp-mu100-adaptive:actual-tolerance-response": true,
    "actual-within-stage-factor-reuse": true
  },
  "original_target_summary": {
    "met": 62,
    "total": 63,
    "all_met": false,
    "acceptance_sha256": "fd7e7cfe528d9844e2992e8ef96d6b33e482e8c5d2bc63a4d6955431168f6051"
  }
}
```

### Stored measurements and decisions

```json
{
  "metrics": {
    "maximum_sampled_weighted_error": 0.0013539838869965851,
    "factorizations": 12376,
    "linear_solves": 20946,
    "factor_reuses": 8570,
    "accuracy_scope": "Fixed reference observation times only; all-step positivity/conservation separately tested. Stage residual norm is weightedLinf; adaptive estimator norm is RMS.",
    "original_mu1_tight_global_goal": 2e-05,
    "actual_mu1_tight_global_error": 4.535633779001458e-05,
    "original_mu1_tight_global_goal_met": false,
    "reporting_scope": "Current protocol verifies faithful reporting; it does not assert this original global accuracy goal was met."
  },
  "checks": {
    "vdp-mu1-bdf2-256:complete-finite": true,
    "vdp-mu1-bdf2-256:true-stage-residual": true,
    "vdp-mu1-bdf2-256:bounded-state": true,
    "vdp-mu1-bdf2-512:complete-finite": true,
    "vdp-mu1-bdf2-512:true-stage-residual": true,
    "vdp-mu1-bdf2-512:bounded-state": true,
    "vdp-mu1-bdf2-1024:complete-finite": true,
    "vdp-mu1-bdf2-1024:true-stage-residual": true,
    "vdp-mu1-bdf2-1024:bounded-state": true,
    "vdp-mu1-sdirk2-256:complete-finite": true,
    "vdp-mu1-sdirk2-256:true-stage-residual": true,
    "vdp-mu1-sdirk2-256:bounded-state": true,
    "vdp-mu1-sdirk2-512:complete-finite": true,
    "vdp-mu1-sdirk2-512:true-stage-residual": true,
    "vdp-mu1-sdirk2-512:bounded-state": true,
    "vdp-mu1-sdirk2-1024:complete-finite": true,
    "vdp-mu1-sdirk2-1024:true-stage-residual": true,
    "vdp-mu1-sdirk2-1024:bounded-state": true,
    "vdp-mu1-sdirk-doubling-loose:complete-finite": true,
    "vdp-mu1-sdirk-doubling-loose:true-stage-residual": true,
    "vdp-mu1-sdirk-doubling-loose:bounded-state": true,
    "vdp-mu1-sdirk-doubling-tight:complete-finite": true,
    "vdp-mu1-sdirk-doubling-tight:true-stage-residual": true,
    "vdp-mu1-sdirk-doubling-tight:bounded-state": true,
    "vdp-mu100-bdf2-256:complete-finite": true,
    "vdp-mu100-bdf2-256:true-stage-residual": true,
    "vdp-mu100-bdf2-256:bounded-state": true,
    "vdp-mu100-bdf2-512:complete-finite": true,
    "vdp-mu100-bdf2-512:true-stage-residual": true,
    "vdp-mu100-bdf2-512:bounded-state": true,
    "vdp-mu100-bdf2-1024:complete-finite": true,
    "vdp-mu100-bdf2-1024:true-stage-residual": true,
    "vdp-mu100-bdf2-1024:bounded-state": true,
    "vdp-mu100-sdirk2-256:complete-finite": true,
    "vdp-mu100-sdirk2-256:true-stage-residual": true,
    "vdp-mu100-sdirk2-256:bounded-state": true,
    "vdp-mu100-sdirk2-512:complete-finite": true,
    "vdp-mu100-sdirk2-512:true-stage-residual": true,
    "vdp-mu100-sdirk2-512:bounded-state": true,
    "vdp-mu100-sdirk2-1024:complete-finite": true,
    "vdp-mu100-sdirk2-1024:true-stage-residual": true,
    "vdp-mu100-sdirk2-1024:bounded-state": true,
    "vdp-mu100-sdirk-doubling-loose:complete-finite": true,
    "vdp-mu100-sdirk-doubling-loose:true-stage-residual": true,
    "vdp-mu100-sdirk-doubling-loose:bounded-state": true,
    "vdp-mu100-sdirk-doubling-tight:complete-finite": true,
    "vdp-mu100-sdirk-doubling-tight:true-stage-residual": true,
    "vdp-mu100-sdirk-doubling-tight:bounded-state": true,
    "vdp-mu1-bdf2:finest-accuracy": true,
    "vdp-mu1-bdf2:refinement": true,
    "vdp-mu1-sdirk2:finest-accuracy": true,
    "vdp-mu1-sdirk2:refinement": true,
    "vdp-mu1-adaptive-loose:accuracy": true,
    "vdp-mu1-adaptive:actual-tolerance-response": true,
    "vdp-mu100-bdf2:finest-accuracy": true,
    "vdp-mu100-bdf2:refinement": true,
    "vdp-mu100-sdirk2:finest-accuracy": true,
    "vdp-mu100-sdirk2:refinement": true,
    "vdp-mu100-adaptive-loose:accuracy": true,
    "vdp-mu100-adaptive-tight:accuracy": true,
    "vdp-mu100-adaptive:actual-tolerance-response": true,
    "actual-within-stage-factor-reuse": true,
    "vdp-mu1-adaptive-tight:original-goal-outcome-faithfully-reported": true,
    "vdp-mu1-adaptive-tight:accepted-local-controls-satisfied": true,
    "vdp-mu1-adaptive-tight:immutable-original-failure-bound": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/van-der-pol-stiff-transition/index.json

![Saved fixed-step comparisons and the local/global error distinction. The first study met 208/209 targets; the unmet mu = 1 adaptive global goal of 2e-5 remains recorded.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/van-der-pol-stiff-transition-preview.png)

Saved fixed-step comparisons and the local/global error distinction. The first study met 208/209 targets; the unmet mu = 1 adaptive global goal of 2e-5 remains recorded.

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/atlas-ode-adaptivity-2026-11-24-r2.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- scikit-sundae official van der Pol example [accessed 2026-11-24]. https://scikit-sundae.readthedocs.io/en/stable/examples/van_der_pol.html; review_level=official-project-example-selected-equations
Read the equations and initial state in the official binding example. Our mu = 1 and 100, T = 2 inputs are an authored early-transient scope, not an original-paper or full mu = 1000 cycle reproduction.

- SciPy1.14.1 solve_ivp and selected official source [accessed 2026-11-24]. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.integrate.solve_ivp.html; review_level=official-selected-source
Read selected fixed-version method, API, local-tolerance and termination sections. This is not a full audit of the original research papers.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## RK45: embedded errors, dense output and events

Use analytic damped rotation to test acceptance, rejection, FSAL ownership, dense interpolation and directed event times separately.

**Methods used**

- [Dormand–Prince RK45](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk45/?lang=en) (`rk45`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/rk45-dense-events/?lang=en#rk45-dense-events-en-algorithm)

Use actual Dormand–Prince 5(4) stages, a quartic continuous extension, an accepted-state derivative cache and bracket bisection on retained interpolants. A rejected endpoint never replaces the accepted starting derivative.

$$
y(t)=e^{-0.2t}(\cos 3t,\sin 3t)^T,\quad t_*=\pi/6,\pi/2
$$

$$
y(t_n+\theta h)=y_n+hQ(\theta,\theta^2,\theta^3,\theta^4)^T
$$

- [Finite-dimensional linear evolution systems](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#linear-evolution-system-en) (`linear-evolution-system`)

Use gamma = 0.2, omega = 3, initial state (1, 0), and T = 2. Three paired relative and absolute tolerances with two maximum steps, plus two terminal runs, give eight runs.


**Problem figure**

![RK45: embedded errors, dense output and events: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/rk45-dense-events.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[RK45: embedded errors, dense output and events](https://hrkoyama.github.io/numerical-methods-atlas/problems/rk45-dense-events/?lang=en) (`rk45-dense-events`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/rk45-dense-events/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/rk45-dense-events/?lang=en#rk45-dense-events-en-validation)

Analytic states and the simple crossings at pi/6 and pi/2 provide independent truth. Check endpoints, 97 off-mesh samples, event times and residuals, and the actual identity nfev = 1 + 6 times the attempted-step count.

- [RK45: embedded errors, dense output and events](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-rk45-dense-events-en) (`rk45-dense-events`; Same-problem reference · Analytic reference)

There is no general guarantee for tangential roots, multiple crossings within a step or systems with resets. Initial-zero and ownership controls are limited component tests; local tolerances and global accuracy remain distinct.
### Assumptions, units and boundaries

Use gamma = 0.2, omega = 3, initial state (1, 0), and T = 2. Three paired relative and absolute tolerances with two maximum steps, plus two terminal runs, give eight runs.

**Editorial clarification**

There is no general guarantee for tangential roots, multiple crossings within a step or systems with resets. Initial-zero and ownership controls are limited component tests; local tolerances and global accuracy remain distinct. Axes for trajectories, states, time or iterations do not represent physical spatial dimensions.

### Adopted numerical method

Use actual Dormand–Prince 5(4) stages, a quartic continuous extension, an accepted-state derivative cache and bracket bisection on retained interpolants. A rejected endpoint never replaces the accepted starting derivative.

$$
y(t)=e^{-0.2t}(\cos 3t,\sin 3t)^T,\quad t_*=\pi/6,\pi/2
$$

$$
y(t_n+\theta h)=y_n+hQ(\theta,\theta^2,\theta^3,\theta^4)^T
$$

### References and validation

Analytic states and the simple crossings at pi/6 and pi/2 provide independent truth. Check endpoints, 97 off-mesh samples, event times and residuals, and the actual identity nfev = 1 + 6 times the attempted-step count.

### Limits

There is no general guarantee for tangential roots, multiple crossings within a step or systems with resets. Initial-zero and ownership controls are limited component tests; local tolerances and global accuracy remain distinct.

### Stored measurements and decisions

```json
{
  "metrics": {
    "maximum_dense_error": 6.136827199998418e-05,
    "maximum_event_time_error": 1.4618863214188593e-05,
    "actual_RHS_evaluations": 2162,
    "rejected_trials": 40,
    "scope": "Analytic state/simple crossings; accepted-full endpoint versus terminal dense-root state distinct. No global guarantee inferred from localtol."
  },
  "checks": {
    "rk45-loose-hmax0.4:completion-and-work": true,
    "rk45-loose-hmax0.4:endpoint-error": true,
    "rk45-loose-hmax0.4:offmesh-error": true,
    "rk45-loose-hmax0.4:event-time-and-set": true,
    "rk45-loose-hmax0.4:event-residual": true,
    "rk45-loose-hmax0.1:completion-and-work": true,
    "rk45-loose-hmax0.1:endpoint-error": true,
    "rk45-loose-hmax0.1:offmesh-error": true,
    "rk45-loose-hmax0.1:event-time-and-set": true,
    "rk45-loose-hmax0.1:event-residual": true,
    "rk45-medium-hmax0.4:completion-and-work": true,
    "rk45-medium-hmax0.4:endpoint-error": true,
    "rk45-medium-hmax0.4:offmesh-error": true,
    "rk45-medium-hmax0.4:event-time-and-set": true,
    "rk45-medium-hmax0.4:event-residual": true,
    "rk45-medium-hmax0.1:completion-and-work": true,
    "rk45-medium-hmax0.1:endpoint-error": true,
    "rk45-medium-hmax0.1:offmesh-error": true,
    "rk45-medium-hmax0.1:event-time-and-set": true,
    "rk45-medium-hmax0.1:event-residual": true,
    "rk45-tight-hmax0.4:completion-and-work": true,
    "rk45-tight-hmax0.4:endpoint-error": true,
    "rk45-tight-hmax0.4:offmesh-error": true,
    "rk45-tight-hmax0.4:event-time-and-set": true,
    "rk45-tight-hmax0.4:event-residual": true,
    "rk45-tight-hmax0.1:completion-and-work": true,
    "rk45-tight-hmax0.1:endpoint-error": true,
    "rk45-tight-hmax0.1:offmesh-error": true,
    "rk45-tight-hmax0.1:event-time-and-set": true,
    "rk45-tight-hmax0.1:event-residual": true,
    "rk45-terminal-direction-1:completion-and-work": true,
    "rk45-terminal-direction-1:endpoint-error": true,
    "rk45-terminal-direction-1:offmesh-error": true,
    "rk45-terminal-direction-1:event-time-and-set": true,
    "rk45-terminal-direction-1:event-residual": true,
    "rk45-terminal-direction1:completion-and-work": true,
    "rk45-terminal-direction1:endpoint-error": true,
    "rk45-terminal-direction1:offmesh-error": true,
    "rk45-terminal-direction1:event-time-and-set": true,
    "rk45-terminal-direction1:event-residual": true,
    "hmax0.4:actual-tolerance-response": true,
    "hmax0.1:actual-tolerance-response": true,
    "rejected-trial-actually-exercised": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/rk45-dense-events/index.json

![Use analytic damped rotation to test acceptance, rejection, FSAL ownership, dense interpolation and directed event times separately. This preview reads saved numerical fields and references only.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/rk45-dense-events-preview.png)

Use analytic damped rotation to test acceptance, rejection, FSAL ownership, dense interpolation and directed event times separately. This preview reads saved numerical fields and references only.

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/atlas-ode-adaptivity-2026-11-24-r2.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- SciPy1.14.1 RK45 coefficient and dense-output source [accessed 2026-11-24]. https://github.com/scipy/scipy/blob/v1.14.1/scipy/integrate/_ivp/rk.py; review_level=official-release-source-selected-functions
Read C, A, B, E, P, stage evaluation, accepted/rejected FSAL updates and quartic evaluation. The original Dormand–Prince 1980 and Shampine 1986 papers remain unread beyond bibliography. The adapted coefficient BSD notice is retained.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## Strang splitting: Dirichlet boundary order reduction and correction

Evolve actual one-dimensional nonperiodic fields and compare unmodified and boundary-corrected Strang splitting against the same spatial discretization.

**Methods used**

- [Strang splitting](https://hrkoyama.github.io/numerical-methods-atlas/methods/strang-splitting/?lang=en) (`strang-splitting`)
- [Lie–Trotter splitting](https://hrkoyama.github.io/numerical-methods-atlas/methods/lie-trotter/?lang=en) (`lie-trotter`)
- [Centered spatial difference](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en) (`centered-difference`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/strang-boundary-order-reduction/?lang=en#strang-boundary-order-reduction-en-algorithm)

For w = u - 1, use the unmodified split (Lw, w + 1) or the corrected split (Lw + 1, w). Compose actual Dirichlet DST-I flows and retain the reaction boundary mismatch.

$$
u_t=u_{xx}+u,\quad u(0,t)=u(1,t)=1,\quad w=u-1
$$

$$
A_{\rm raw}(w)=L_hw,\ B_{\rm raw}(w)=w+1;\quad A_{\rm corr}(w)=L_hw+1,\ B_{\rm corr}(w)=w
$$

- [Linear reaction-diffusion with inhomogeneous boundaries](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#inhomogeneous-reaction-diffusion-en) (`inhomogeneous-reaction-diffusion`)

Solve u_t = u_xx + u on [0, 1] with both boundary values equal to 1, an analytic steady state plus a 0.1 sine perturbation, and T = 0.1. Use 31, 63 and 127 interior nodes with 8, 16, 32 and 64 steps, plus four Lie controls: 28 runs.

- [Heat / diffusion equation](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#heat-en) (`heat`)

Solve u_t = u_xx + u on [0, 1] with both boundary values equal to 1, an analytic steady state plus a 0.1 sine perturbation, and T = 0.1. Use 31, 63 and 127 interior nodes with 8, 16, 32 and 64 steps, plus four Lie controls: 28 runs.


**Problem figure**

![Strang splitting: Dirichlet boundary order reduction and correction: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/strang-boundary-order-reduction.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Strang splitting: Dirichlet boundary order reduction and correction](https://hrkoyama.github.io/numerical-methods-atlas/problems/strang-boundary-order-reduction/?lang=en) (`strang-boundary-order-reduction`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/strang-boundary-order-reduction/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/strang-boundary-order-reduction/?lang=en#strang-boundary-order-reduction-en-validation)

First qualify an independent sparse affine exponential action against separately written sine sums. Then separate temporal error against the same finite-difference system, spatial error against the analytic continuum field, and observed order in the fixed regime.

- [Strang splitting: Dirichlet boundary order reduction and correction](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-strang-boundary-order-reduction-en) (`strang-boundary-order-reduction`; Same-problem reference · Semi-analytic reference)

This is an authored linear specialization, not a reproduction of the original nonlinear tables. It makes no general claim for nonautonomous boundaries or universal order loss. The final reaction-trace mismatch of Lie splitting is disclosed separately.
### Assumptions, units and boundaries

Solve u_t = u_xx + u on [0, 1] with both boundary values equal to 1, an analytic steady state plus a 0.1 sine perturbation, and T = 0.1. Use 31, 63 and 127 interior nodes with 8, 16, 32 and 64 steps, plus four Lie controls: 28 runs.

**Editorial clarification**

This is an authored linear specialization, not a reproduction of the original nonlinear tables. It makes no general claim for nonautonomous boundaries or universal order loss. The final reaction-trace mismatch of Lie splitting is disclosed separately.

### Adopted numerical method

For w = u - 1, use the unmodified split (Lw, w + 1) or the corrected split (Lw + 1, w). Compose actual Dirichlet DST-I flows and retain the reaction boundary mismatch.

$$
u_t=u_{xx}+u,\quad u(0,t)=u(1,t)=1,\quad w=u-1
$$

$$
A_{\rm raw}(w)=L_hw,\ B_{\rm raw}(w)=w+1;\quad A_{\rm corr}(w)=L_hw+1,\ B_{\rm corr}(w)=w
$$

### References and validation

First qualify an independent sparse affine exponential action against separately written sine sums. Then separate temporal error against the same finite-difference system, spatial error against the analytic continuum field, and observed order in the fixed regime.

### Limits

This is an authored linear specialization, not a reproduction of the original nonlinear tables. It makes no general claim for nonautonomous boundaries or universal order loss. The final reaction-trace mismatch of Lie splitting is disclosed separately.

### Stored measurements and decisions

```json
{
  "metrics": {
    "N127_finest_raw_temporal_error": 0.00011072277594093016,
    "N127_finest_corrected_temporal_error": 9.830520841802581e-08,
    "reference_spatial_order": 1.9999950873134633,
    "scope": "Actual1Dnonperiodicfields. TimevsSAME-FDoracle; spacevsanalyticcontinuum. Linearautonomousspecialization, fixed-regime order; no universal reduction/theorem reproduction."
  },
  "checks": {
    "boundary-n31-strang-unmodified-8:actual-field-and-work": true,
    "boundary-n31-strang-unmodified-8:boundary-compatibility-ledger": true,
    "boundary-n31-strang-unmodified-16:actual-field-and-work": true,
    "boundary-n31-strang-unmodified-16:boundary-compatibility-ledger": true,
    "boundary-n31-strang-unmodified-32:actual-field-and-work": true,
    "boundary-n31-strang-unmodified-32:boundary-compatibility-ledger": true,
    "boundary-n31-strang-unmodified-64:actual-field-and-work": true,
    "boundary-n31-strang-unmodified-64:boundary-compatibility-ledger": true,
    "boundary-n31-strang-boundary-corrected-8:actual-field-and-work": true,
    "boundary-n31-strang-boundary-corrected-8:boundary-compatibility-ledger": true,
    "boundary-n31-strang-boundary-corrected-16:actual-field-and-work": true,
    "boundary-n31-strang-boundary-corrected-16:boundary-compatibility-ledger": true,
    "boundary-n31-strang-boundary-corrected-32:actual-field-and-work": true,
    "boundary-n31-strang-boundary-corrected-32:boundary-compatibility-ledger": true,
    "boundary-n31-strang-boundary-corrected-64:actual-field-and-work": true,
    "boundary-n31-strang-boundary-corrected-64:boundary-compatibility-ledger": true,
    "boundary-n63-strang-unmodified-8:actual-field-and-work": true,
    "boundary-n63-strang-unmodified-8:boundary-compatibility-ledger": true,
    "boundary-n63-strang-unmodified-16:actual-field-and-work": true,
    "boundary-n63-strang-unmodified-16:boundary-compatibility-ledger": true,
    "boundary-n63-strang-unmodified-32:actual-field-and-work": true,
    "boundary-n63-strang-unmodified-32:boundary-compatibility-ledger": true,
    "boundary-n63-strang-unmodified-64:actual-field-and-work": true,
    "boundary-n63-strang-unmodified-64:boundary-compatibility-ledger": true,
    "boundary-n63-strang-boundary-corrected-8:actual-field-and-work": true,
    "boundary-n63-strang-boundary-corrected-8:boundary-compatibility-ledger": true,
    "boundary-n63-strang-boundary-corrected-16:actual-field-and-work": true,
    "boundary-n63-strang-boundary-corrected-16:boundary-compatibility-ledger": true,
    "boundary-n63-strang-boundary-corrected-32:actual-field-and-work": true,
    "boundary-n63-strang-boundary-corrected-32:boundary-compatibility-ledger": true,
    "boundary-n63-strang-boundary-corrected-64:actual-field-and-work": true,
    "boundary-n63-strang-boundary-corrected-64:boundary-compatibility-ledger": true,
    "boundary-n127-strang-unmodified-8:actual-field-and-work": true,
    "boundary-n127-strang-unmodified-8:boundary-compatibility-ledger": true,
    "boundary-n127-strang-unmodified-16:actual-field-and-work": true,
    "boundary-n127-strang-unmodified-16:boundary-compatibility-ledger": true,
    "boundary-n127-strang-unmodified-32:actual-field-and-work": true,
    "boundary-n127-strang-unmodified-32:boundary-compatibility-ledger": true,
    "boundary-n127-strang-unmodified-64:actual-field-and-work": true,
    "boundary-n127-strang-unmodified-64:boundary-compatibility-ledger": true,
    "boundary-n127-strang-boundary-corrected-8:actual-field-and-work": true,
    "boundary-n127-strang-boundary-corrected-8:boundary-compatibility-ledger": true,
    "boundary-n127-strang-boundary-corrected-16:actual-field-and-work": true,
    "boundary-n127-strang-boundary-corrected-16:boundary-compatibility-ledger": true,
    "boundary-n127-strang-boundary-corrected-32:actual-field-and-work": true,
    "boundary-n127-strang-boundary-corrected-32:boundary-compatibility-ledger": true,
    "boundary-n127-strang-boundary-corrected-64:actual-field-and-work": true,
    "boundary-n127-strang-boundary-corrected-64:boundary-compatibility-ledger": true,
    "boundary-n127-lie-8:actual-field-and-work": true,
    "boundary-n127-lie-8:boundary-compatibility-ledger": true,
    "boundary-n127-lie-16:actual-field-and-work": true,
    "boundary-n127-lie-16:boundary-compatibility-ledger": true,
    "boundary-n127-lie-32:actual-field-and-work": true,
    "boundary-n127-lie-32:boundary-compatibility-ledger": true,
    "boundary-n127-lie-64:actual-field-and-work": true,
    "boundary-n127-lie-64:boundary-compatibility-ledger": true,
    "n31:corrected-finest-accuracy": true,
    "n63:corrected-finest-accuracy": true,
    "n127:corrected-finest-accuracy": true,
    "strang-unmodified:fixed-regime-temporal-order": true,
    "strang-boundary-corrected:fixed-regime-temporal-order": true,
    "finest:boundary-correction-improves": true,
    "separate-reference-spatial-order": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/strang-boundary-order-reduction/index.json

![Evolve actual one-dimensional nonperiodic fields and compare unmodified and boundary-corrected Strang splitting against the same spatial discretization. This preview reads saved numerical fields and references only.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/strang-boundary-order-reduction-preview.png)

Evolve actual one-dimensional nonperiodic fields and compare unmodified and boundary-corrected Strang splitting against the same spatial discretization. This preview reads saved numerical fields and references only.

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/atlas-ode-adaptivity-2026-11-24-r2.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- L. Einkemmer; A. Ostermann (2014). Overcoming order reduction in diffusion-reaction splitting. Part1: Dirichlet boundary conditions [accessed 2026-11-24]. https://arxiv.org/abs/1411.0465; review_level=primary-preprint-selected-sections
Read selected extracted text from the 2014 v1 preprint: section 2, Algorithm 2, the constant-boundary example, section 3.2 assumptions and result, and the one-dimensional example. This was not a full-proof or whole-PDF visual audit; the present linear specialization does not reproduce the nonlinear tables.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
