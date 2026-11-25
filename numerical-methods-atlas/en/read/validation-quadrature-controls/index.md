# Domain-aware, double-exponential and sparse-grid quadrature

Compare fixed integrals with domain-aware methods, separating estimated errors, actual errors, budget exits and underresolution controls.

These additional validation supplements are managed separately from the common 22-example registry. Receipts cover independent ZIP extraction, tests and every fixed input within each group. Changes of settings, methods or step sizes do not add independent physical problems.

## QUADPACK dispatch and finite Simpson companions

Fifteen specialized quadratures and fifteen Simpson companions use fixed inputs.

**Methods used**

- [Gaussian and adaptive quadrature](https://hrkoyama.github.io/numerical-methods-atlas/methods/quadrature/?lang=en) (`quadrature`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/quadpack-domain-selection/?lang=en#quadpack-domain-selection-en-algorithm)

Explicit domain/weight dispatch retains active full_output prefixes. The existing Simpson function is unchanged.

- [Finite, improper and multivariate definite integrals](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#definite-integrals-en) (`definite-integrals`)

Whole-line Gaussian, two finite frequencies, half-line Fourier and an internal singularity; absolute tolerances1e-6/1e-8/1e-10 and epsrel0.


**Problem figure**

![QUADPACK dispatch and finite Simpson companions: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/results/quadpack-domain-selection.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[QUADPACK dispatch and finite Simpson companions](https://hrkoyama.github.io/numerical-methods-atlas/problems/quadpack-domain-selection/?lang=en) (`quadpack-domain-selection`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/quadpack-domain-selection/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/quadpack-domain-selection/?lang=en#quadpack-domain-selection-en-validation)

Independent analytic interval references and actual callback counts are checked. The finite Gaussian target is an interval, not an invented erf value.

- [QUADPACK dispatch and finite Simpson companions](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-quadpack-domain-selection-en) (`quadpack-domain-selection`; Same-problem reference · Analytic reference)

Singular-node failures and unmet Simpson goals remain visible; error estimates are not general guarantees.
### Assumptions, units and boundaries

Whole-line Gaussian, two finite frequencies, half-line Fourier and an internal singularity; absolute tolerances1e-6/1e-8/1e-10 and epsrel0.

**Editorial clarification**

Singular-node failures and unmet Simpson goals remain visible; error estimates are not general guarantees. The formulas and inputs specify mathematical integration domains and dimensions. Parameter and error axes are not physical spatial coordinates. Passing reproduction checks does not mean that every accuracy goal was met. Original row outcomes: 25 met, 2 unmet and 3 not computable. False/NA outcomes and raw failures are retained.

### Adopted numerical method

Explicit domain/weight dispatch retains active full_output prefixes. The existing Simpson function is unchanged.

$$
I=\int_\Omega f(x)\,dx
$$

### References and validation

Independent analytic interval references and actual callback counts are checked. The finite Gaussian target is an interval, not an invented erf value.

### Limits

Singular-node failures and unmet Simpson goals remain visible; error estimates are not general guarantees.

### Stored measurements and decisions

```json
{
  "metrics": {
    "records": 30,
    "integrand_evaluations": 34351,
    "accuracy_goals_met": 25,
    "accuracy_goals_unmet": 2,
    "accuracy_goals_unresolved": 3,
    "estimated_converged_rows": 26
  },
  "checks": {
    "q78:gaussian-whole-line:specialized-quadpack:a0:callback-ledger": true,
    "q78:gaussian-whole-line:specialized-quadpack:a0:finite-return": true,
    "q78:gaussian-whole-line:specialized-quadpack:a0:native-success": true,
    "q78:gaussian-whole-line:specialized-quadpack:a0:required-analytic-accuracy": true,
    "q78:gaussian-whole-line:specialized-quadpack:a0:absolute-series": true,
    "q78:gaussian-whole-line:specialized-quadpack:a1:callback-ledger": true,
    "q78:gaussian-whole-line:specialized-quadpack:a1:finite-return": true,
    "q78:gaussian-whole-line:specialized-quadpack:a1:native-success": true,
    "q78:gaussian-whole-line:specialized-quadpack:a1:required-analytic-accuracy": true,
    "q78:gaussian-whole-line:specialized-quadpack:a1:absolute-series": true,
    "q78:gaussian-whole-line:specialized-quadpack:a2:callback-ledger": true,
    "q78:gaussian-whole-line:specialized-quadpack:a2:finite-return": true,
    "q78:gaussian-whole-line:specialized-quadpack:a2:native-success": true,
    "q78:gaussian-whole-line:specialized-quadpack:a2:required-analytic-accuracy": true,
    "q78:gaussian-whole-line:specialized-quadpack:a2:absolute-series": true,
    "q78:gaussian-whole-line:simpson-companion:a0:callback-ledger": true,
    "q78:gaussian-whole-line:simpson-companion:a0:evaluation-cap": true,
    "q78:gaussian-whole-line:simpson-companion:a0:finite-return": true,
    "q78:gaussian-whole-line:simpson-companion:a0:native-status": true,
    "q78:gaussian-whole-line:simpson-companion:a1:callback-ledger": true,
    "q78:gaussian-whole-line:simpson-companion:a1:evaluation-cap": true,
    "q78:gaussian-whole-line:simpson-companion:a1:finite-return": true,
    "q78:gaussian-whole-line:simpson-companion:a1:native-status": true,
    "q78:gaussian-whole-line:simpson-companion:a2:callback-ledger": true,
    "q78:gaussian-whole-line:simpson-companion:a2:evaluation-cap": true,
    "q78:gaussian-whole-line:simpson-companion:a2:finite-return": true,
    "q78:gaussian-whole-line:simpson-companion:a2:native-status": true,
    "q78:finite-sine-40:specialized-quadpack:a0:callback-ledger": true,
    "q78:finite-sine-40:specialized-quadpack:a0:finite-return": true,
    "q78:finite-sine-40:specialized-quadpack:a0:native-success": true,
    "q78:finite-sine-40:specialized-quadpack:a0:required-analytic-accuracy": true,
    "q78:finite-sine-40:specialized-quadpack:a0:absolute-series": true,
    "q78:finite-sine-40:specialized-quadpack:a1:callback-ledger": true,
    "q78:finite-sine-40:specialized-quadpack:a1:finite-return": true,
    "q78:finite-sine-40:specialized-quadpack:a1:native-success": true,
    "q78:finite-sine-40:specialized-quadpack:a1:required-analytic-accuracy": true,
    "q78:finite-sine-40:specialized-quadpack:a1:absolute-series": true,
    "q78:finite-sine-40:specialized-quadpack:a2:callback-ledger": true,
    "q78:finite-sine-40:specialized-quadpack:a2:finite-return": true,
    "q78:finite-sine-40:specialized-quadpack:a2:native-success": true,
    "q78:finite-sine-40:specialized-quadpack:a2:required-analytic-accuracy": true,
    "q78:finite-sine-40:specialized-quadpack:a2:absolute-series": true,
    "q78:finite-sine-40:simpson-companion:a0:callback-ledger": true,
    "q78:finite-sine-40:simpson-companion:a0:evaluation-cap": true,
    "q78:finite-sine-40:simpson-companion:a0:finite-return": true,
    "q78:finite-sine-40:simpson-companion:a0:native-status": true,
    "q78:finite-sine-40:simpson-companion:a1:callback-ledger": true,
    "q78:finite-sine-40:simpson-companion:a1:evaluation-cap": true,
    "q78:finite-sine-40:simpson-companion:a1:finite-return": true,
    "q78:finite-sine-40:simpson-companion:a1:native-status": true,
    "q78:finite-sine-40:simpson-companion:a2:callback-ledger": true,
    "q78:finite-sine-40:simpson-companion:a2:evaluation-cap": true,
    "q78:finite-sine-40:simpson-companion:a2:finite-return": true,
    "q78:finite-sine-40:simpson-companion:a2:native-status": true,
    "q78:finite-sine-120:specialized-quadpack:a0:callback-ledger": true,
    "q78:finite-sine-120:specialized-quadpack:a0:finite-return": true,
    "q78:finite-sine-120:specialized-quadpack:a0:native-success": true,
    "q78:finite-sine-120:specialized-quadpack:a0:required-analytic-accuracy": true,
    "q78:finite-sine-120:specialized-quadpack:a0:absolute-series": true,
    "q78:finite-sine-120:specialized-quadpack:a1:callback-ledger": true,
    "q78:finite-sine-120:specialized-quadpack:a1:finite-return": true,
    "q78:finite-sine-120:specialized-quadpack:a1:native-success": true,
    "q78:finite-sine-120:specialized-quadpack:a1:required-analytic-accuracy": true,
    "q78:finite-sine-120:specialized-quadpack:a1:absolute-series": true,
    "q78:finite-sine-120:specialized-quadpack:a2:callback-ledger": true,
    "q78:finite-sine-120:specialized-quadpack:a2:finite-return": true,
    "q78:finite-sine-120:specialized-quadpack:a2:native-success": true,
    "q78:finite-sine-120:specialized-quadpack:a2:required-analytic-accuracy": true,
    "q78:finite-sine-120:specialized-quadpack:a2:absolute-series": true,
    "q78:finite-sine-120:simpson-companion:a0:callback-ledger": true,
    "q78:finite-sine-120:simpson-companion:a0:evaluation-cap": true,
    "q78:finite-sine-120:simpson-companion:a0:finite-return": true,
    "q78:finite-sine-120:simpson-companion:a0:native-status": true,
    "q78:finite-sine-120:simpson-companion:a1:callback-ledger": true,
    "q78:finite-sine-120:simpson-companion:a1:evaluation-cap": true,
    "q78:finite-sine-120:simpson-companion:a1:finite-return": true,
    "q78:finite-sine-120:simpson-companion:a1:native-status": true,
    "q78:finite-sine-120:simpson-companion:a2:callback-ledger": true,
    "q78:finite-sine-120:simpson-companion:a2:evaluation-cap": true,
    "q78:finite-sine-120:simpson-companion:a2:finite-return": true,
    "q78:finite-sine-120:simpson-companion:a2:native-status": true,
    "q78:fourier-half-line:specialized-quadpack:a0:callback-ledger": true,
    "q78:fourier-half-line:specialized-quadpack:a0:finite-return": true,
    "q78:fourier-half-line:specialized-quadpack:a0:native-success": true,
    "q78:fourier-half-line:specialized-quadpack:a0:required-analytic-accuracy": true,
    "q78:fourier-half-line:specialized-quadpack:a0:absolute-series": true,
    "q78:fourier-half-line:specialized-quadpack:a1:callback-ledger": true,
    "q78:fourier-half-line:specialized-quadpack:a1:finite-return": true,
    "q78:fourier-half-line:specialized-quadpack:a1:native-success": true,
    "q78:fourier-half-line:specialized-quadpack:a1:required-analytic-accuracy": true,
    "q78:fourier-half-line:specialized-quadpack:a1:absolute-series": true,
    "q78:fourier-half-line:specialized-quadpack:a2:callback-ledger": true,
    "q78:fourier-half-line:specialized-quadpack:a2:finite-return": true,
    "q78:fourier-half-line:specialized-quadpack:a2:native-success": true,
    "q78:fourier-half-line:specialized-quadpack:a2:required-analytic-accuracy": true,
    "q78:fourier-half-line:specialized-quadpack:a2:absolute-series": true,
    "q78:fourier-half-line:simpson-companion:a0:callback-ledger": true,
    "q78:fourier-half-line:simpson-companion:a0:evaluation-cap": true,
    "q78:fourier-half-line:simpson-companion:a0:finite-return": true,
    "q78:fourier-half-line:simpson-companion:a0:native-status": true,
    "q78:fourier-half-line:simpson-companion:a1:callback-ledger": true,
    "q78:fourier-half-line:simpson-companion:a1:evaluation-cap": true,
    "q78:fourier-half-line:simpson-companion:a1:finite-return": true,
    "q78:fourier-half-line:simpson-companion:a1:native-status": true,
    "q78:fourier-half-line:simpson-companion:a2:callback-ledger": true,
    "q78:fourier-half-line:simpson-companion:a2:evaluation-cap": true,
    "q78:fourier-half-line:simpson-companion:a2:finite-return": true,
    "q78:fourier-half-line:simpson-companion:a2:native-status": true,
    "q78:internal-root:specialized-quadpack:a0:callback-ledger": true,
    "q78:internal-root:specialized-quadpack:a0:finite-return": true,
    "q78:internal-root:specialized-quadpack:a0:native-success": true,
    "q78:internal-root:specialized-quadpack:a0:required-analytic-accuracy": true,
    "q78:internal-root:specialized-quadpack:a0:absolute-series": true,
    "q78:internal-root:specialized-quadpack:a1:callback-ledger": true,
    "q78:internal-root:specialized-quadpack:a1:finite-return": true,
    "q78:internal-root:specialized-quadpack:a1:native-success": true,
    "q78:internal-root:specialized-quadpack:a1:required-analytic-accuracy": true,
    "q78:internal-root:specialized-quadpack:a1:absolute-series": true,
    "q78:internal-root:specialized-quadpack:a2:callback-ledger": true,
    "q78:internal-root:specialized-quadpack:a2:finite-return": true,
    "q78:internal-root:specialized-quadpack:a2:native-success": true,
    "q78:internal-root:specialized-quadpack:a2:required-analytic-accuracy": true,
    "q78:internal-root:specialized-quadpack:a2:absolute-series": true,
    "q78:internal-root:simpson-companion:a0:callback-ledger": true,
    "q78:internal-root:simpson-companion:a0:evaluation-cap": true,
    "q78:internal-root:simpson-companion:a0:declared-singular-node": true,
    "q78:internal-root:simpson-companion:a1:callback-ledger": true,
    "q78:internal-root:simpson-companion:a1:evaluation-cap": true,
    "q78:internal-root:simpson-companion:a1:declared-singular-node": true,
    "q78:internal-root:simpson-companion:a2:callback-ledger": true,
    "q78:internal-root:simpson-companion:a2:evaluation-cap": true,
    "q78:internal-root:simpson-companion:a2:declared-singular-node": true,
    "quadpack-domain-selection:fixed-record-count": true,
    "quadpack-domain-selection:unique-record-ids": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/quadpack-domain-selection/index.json

![Saved active Fourier contributions and actual errors/call counts](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/results/quadpack-domain-selection-preview.png)

Saved active Fourier contributions and actual errors/call counts

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/atlas-quadrature-controls-2026-11-25.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- quad: adaptive integration and QUADPACK dispatch [accessed 2026-11-25]. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.integrate.quad.html; review_level=selected-official-documentation

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## G7/K15 and finite-interval tanh-sinh

Nine adaptive GK rows and twenty-four fixed DE sums are compared.

**Methods used**

- [Gaussian and adaptive quadrature](https://hrkoyama.github.io/numerical-methods-atlas/methods/quadrature/?lang=en) (`quadrature`)
- [Gauss–Kronrod G7/K15](https://hrkoyama.github.io/numerical-methods-atlas/methods/gauss-kronrod/?lang=en) (`gauss-kronrod`)
- [Tanh–sinh double-exponential quadrature](https://hrkoyama.github.io/numerical-methods-atlas/methods/tanh-sinh/?lang=en) (`tanh-sinh`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/gk15-double-exponential/?lang=en#gk15-double-exponential-en-algorithm)

Shared15-node G7 degree13/K15 degree23; DE uses stable logarithmic products and full endpoint weights.

- [Finite, improper and multivariate definite integrals](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#definite-integrals-en) (`definite-integrals`)

Integrate exp(x), x^(-1/3) and -log(x) on[0,1], with h from1/2 to1/16 and cutoffs3/4.


**Problem figure**

![G7/K15 and finite-interval tanh-sinh: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/results/gk15-double-exponential.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[G7/K15 and finite-interval tanh-sinh](https://hrkoyama.github.io/numerical-methods-atlas/problems/gk15-double-exponential/?lang=en) (`gk15-double-exponential`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/gk15-double-exponential/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/gk15-double-exponential/?lang=en#gk15-double-exponential-en-validation)

Analytic interval references separate total error, continuous tail and finite-window defect.

- [G7/K15 and finite-interval tanh-sinh](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-gk15-double-exponential-en) (`gk15-double-exponential`; Same-problem reference · Analytic reference)

Half-line exp-sinh and whole-line sinh-sinh are unimplemented; no omitted infinite-grid sum bound is provided.
### Assumptions, units and boundaries

Integrate exp(x), x^(-1/3) and -log(x) on[0,1], with h from1/2 to1/16 and cutoffs3/4.

**Editorial clarification**

Half-line exp-sinh and whole-line sinh-sinh are unimplemented; no omitted infinite-grid sum bound is provided. The formulas and inputs specify mathematical integration domains and dimensions. Parameter and error axes are not physical spatial coordinates. Passing reproduction checks does not mean that every accuracy goal was met. Original row outcomes: 26 met, 7 unmet and 0 not computable. False/NA outcomes and raw failures are retained.

### Adopted numerical method

Shared15-node G7 degree13/K15 degree23; DE uses stable logarithmic products and full endpoint weights.

$$
I=\int_\Omega f(x)\,dx
$$

### References and validation

Analytic interval references separate total error, continuous tail and finite-window defect.

### Limits

Half-line exp-sinh and whole-line sinh-sinh are unimplemented; no omitted infinite-grid sum bound is provided.

### Stored measurements and decisions

```json
{
  "metrics": {
    "records": 33,
    "integrand_evaluations": 5619,
    "accuracy_goals_met": 26,
    "accuracy_goals_unmet": 7,
    "accuracy_goals_unresolved": 0,
    "estimated_converged_rows": 28
  },
  "checks": {
    "q79:smooth-exponential:gk:a0:callback-ledger": true,
    "q79:smooth-exponential:gk:a0:evaluation-cap": true,
    "q79:smooth-exponential:gk:a0:finite-return": true,
    "q79:smooth-exponential:gk:a0:panel-call-identity": true,
    "q79:smooth-exponential:gk:a0:panel-caps": true,
    "q79:smooth-exponential:gk:a0:success-accuracy-or-explicit-budget": true,
    "q79:smooth-exponential:gk:a1:callback-ledger": true,
    "q79:smooth-exponential:gk:a1:evaluation-cap": true,
    "q79:smooth-exponential:gk:a1:finite-return": true,
    "q79:smooth-exponential:gk:a1:panel-call-identity": true,
    "q79:smooth-exponential:gk:a1:panel-caps": true,
    "q79:smooth-exponential:gk:a1:success-accuracy-or-explicit-budget": true,
    "q79:smooth-exponential:gk:a2:callback-ledger": true,
    "q79:smooth-exponential:gk:a2:evaluation-cap": true,
    "q79:smooth-exponential:gk:a2:finite-return": true,
    "q79:smooth-exponential:gk:a2:panel-call-identity": true,
    "q79:smooth-exponential:gk:a2:panel-caps": true,
    "q79:smooth-exponential:gk:a2:success-accuracy-or-explicit-budget": true,
    "q79:smooth-exponential:de:T3:h0:callback-ledger": true,
    "q79:smooth-exponential:de:T3:h0:evaluation-cap": true,
    "q79:smooth-exponential:de:T3:h0:finite-return": true,
    "q79:smooth-exponential:de:T3:h0:fixed-sample-count": true,
    "q79:smooth-exponential:de:T3:h1:callback-ledger": true,
    "q79:smooth-exponential:de:T3:h1:evaluation-cap": true,
    "q79:smooth-exponential:de:T3:h1:finite-return": true,
    "q79:smooth-exponential:de:T3:h1:fixed-sample-count": true,
    "q79:smooth-exponential:de:T3:h2:callback-ledger": true,
    "q79:smooth-exponential:de:T3:h2:evaluation-cap": true,
    "q79:smooth-exponential:de:T3:h2:finite-return": true,
    "q79:smooth-exponential:de:T3:h2:fixed-sample-count": true,
    "q79:smooth-exponential:de:T3:h3:callback-ledger": true,
    "q79:smooth-exponential:de:T3:h3:evaluation-cap": true,
    "q79:smooth-exponential:de:T3:h3:finite-return": true,
    "q79:smooth-exponential:de:T3:h3:fixed-sample-count": true,
    "q79:smooth-exponential:de:T4:h0:callback-ledger": true,
    "q79:smooth-exponential:de:T4:h0:evaluation-cap": true,
    "q79:smooth-exponential:de:T4:h0:finite-return": true,
    "q79:smooth-exponential:de:T4:h0:fixed-sample-count": true,
    "q79:smooth-exponential:de:T4:h1:callback-ledger": true,
    "q79:smooth-exponential:de:T4:h1:evaluation-cap": true,
    "q79:smooth-exponential:de:T4:h1:finite-return": true,
    "q79:smooth-exponential:de:T4:h1:fixed-sample-count": true,
    "q79:smooth-exponential:de:T4:h2:callback-ledger": true,
    "q79:smooth-exponential:de:T4:h2:evaluation-cap": true,
    "q79:smooth-exponential:de:T4:h2:finite-return": true,
    "q79:smooth-exponential:de:T4:h2:fixed-sample-count": true,
    "q79:smooth-exponential:de:T4:h3:callback-ledger": true,
    "q79:smooth-exponential:de:T4:h3:evaluation-cap": true,
    "q79:smooth-exponential:de:T4:h3:finite-return": true,
    "q79:smooth-exponential:de:T4:h3:fixed-sample-count": true,
    "q79:smooth-exponential:de:T4:h3:required-finest-accuracy": true,
    "q79:algebraic-inverse-cuberoot:gk:a0:callback-ledger": true,
    "q79:algebraic-inverse-cuberoot:gk:a0:evaluation-cap": true,
    "q79:algebraic-inverse-cuberoot:gk:a0:finite-return": true,
    "q79:algebraic-inverse-cuberoot:gk:a0:panel-call-identity": true,
    "q79:algebraic-inverse-cuberoot:gk:a0:panel-caps": true,
    "q79:algebraic-inverse-cuberoot:gk:a0:success-accuracy-or-explicit-budget": true,
    "q79:algebraic-inverse-cuberoot:gk:a1:callback-ledger": true,
    "q79:algebraic-inverse-cuberoot:gk:a1:evaluation-cap": true,
    "q79:algebraic-inverse-cuberoot:gk:a1:finite-return": true,
    "q79:algebraic-inverse-cuberoot:gk:a1:panel-call-identity": true,
    "q79:algebraic-inverse-cuberoot:gk:a1:panel-caps": true,
    "q79:algebraic-inverse-cuberoot:gk:a1:success-accuracy-or-explicit-budget": true,
    "q79:algebraic-inverse-cuberoot:gk:a2:callback-ledger": true,
    "q79:algebraic-inverse-cuberoot:gk:a2:evaluation-cap": true,
    "q79:algebraic-inverse-cuberoot:gk:a2:finite-return": true,
    "q79:algebraic-inverse-cuberoot:gk:a2:panel-call-identity": true,
    "q79:algebraic-inverse-cuberoot:gk:a2:panel-caps": true,
    "q79:algebraic-inverse-cuberoot:gk:a2:success-accuracy-or-explicit-budget": true,
    "q79:algebraic-inverse-cuberoot:de:T3:h0:callback-ledger": true,
    "q79:algebraic-inverse-cuberoot:de:T3:h0:evaluation-cap": true,
    "q79:algebraic-inverse-cuberoot:de:T3:h0:finite-return": true,
    "q79:algebraic-inverse-cuberoot:de:T3:h0:fixed-sample-count": true,
    "q79:algebraic-inverse-cuberoot:de:T3:h1:callback-ledger": true,
    "q79:algebraic-inverse-cuberoot:de:T3:h1:evaluation-cap": true,
    "q79:algebraic-inverse-cuberoot:de:T3:h1:finite-return": true,
    "q79:algebraic-inverse-cuberoot:de:T3:h1:fixed-sample-count": true,
    "q79:algebraic-inverse-cuberoot:de:T3:h2:callback-ledger": true,
    "q79:algebraic-inverse-cuberoot:de:T3:h2:evaluation-cap": true,
    "q79:algebraic-inverse-cuberoot:de:T3:h2:finite-return": true,
    "q79:algebraic-inverse-cuberoot:de:T3:h2:fixed-sample-count": true,
    "q79:algebraic-inverse-cuberoot:de:T3:h3:callback-ledger": true,
    "q79:algebraic-inverse-cuberoot:de:T3:h3:evaluation-cap": true,
    "q79:algebraic-inverse-cuberoot:de:T3:h3:finite-return": true,
    "q79:algebraic-inverse-cuberoot:de:T3:h3:fixed-sample-count": true,
    "q79:algebraic-inverse-cuberoot:de:T4:h0:callback-ledger": true,
    "q79:algebraic-inverse-cuberoot:de:T4:h0:evaluation-cap": true,
    "q79:algebraic-inverse-cuberoot:de:T4:h0:finite-return": true,
    "q79:algebraic-inverse-cuberoot:de:T4:h0:fixed-sample-count": true,
    "q79:algebraic-inverse-cuberoot:de:T4:h1:callback-ledger": true,
    "q79:algebraic-inverse-cuberoot:de:T4:h1:evaluation-cap": true,
    "q79:algebraic-inverse-cuberoot:de:T4:h1:finite-return": true,
    "q79:algebraic-inverse-cuberoot:de:T4:h1:fixed-sample-count": true,
    "q79:algebraic-inverse-cuberoot:de:T4:h2:callback-ledger": true,
    "q79:algebraic-inverse-cuberoot:de:T4:h2:evaluation-cap": true,
    "q79:algebraic-inverse-cuberoot:de:T4:h2:finite-return": true,
    "q79:algebraic-inverse-cuberoot:de:T4:h2:fixed-sample-count": true,
    "q79:algebraic-inverse-cuberoot:de:T4:h3:callback-ledger": true,
    "q79:algebraic-inverse-cuberoot:de:T4:h3:evaluation-cap": true,
    "q79:algebraic-inverse-cuberoot:de:T4:h3:finite-return": true,
    "q79:algebraic-inverse-cuberoot:de:T4:h3:fixed-sample-count": true,
    "q79:algebraic-inverse-cuberoot:de:T4:h3:required-finest-accuracy": true,
    "q79:log-endpoint:gk:a0:callback-ledger": true,
    "q79:log-endpoint:gk:a0:evaluation-cap": true,
    "q79:log-endpoint:gk:a0:finite-return": true,
    "q79:log-endpoint:gk:a0:panel-call-identity": true,
    "q79:log-endpoint:gk:a0:panel-caps": true,
    "q79:log-endpoint:gk:a0:success-accuracy-or-explicit-budget": true,
    "q79:log-endpoint:gk:a1:callback-ledger": true,
    "q79:log-endpoint:gk:a1:evaluation-cap": true,
    "q79:log-endpoint:gk:a1:finite-return": true,
    "q79:log-endpoint:gk:a1:panel-call-identity": true,
    "q79:log-endpoint:gk:a1:panel-caps": true,
    "q79:log-endpoint:gk:a1:success-accuracy-or-explicit-budget": true,
    "q79:log-endpoint:gk:a2:callback-ledger": true,
    "q79:log-endpoint:gk:a2:evaluation-cap": true,
    "q79:log-endpoint:gk:a2:finite-return": true,
    "q79:log-endpoint:gk:a2:panel-call-identity": true,
    "q79:log-endpoint:gk:a2:panel-caps": true,
    "q79:log-endpoint:gk:a2:success-accuracy-or-explicit-budget": true,
    "q79:log-endpoint:de:T3:h0:callback-ledger": true,
    "q79:log-endpoint:de:T3:h0:evaluation-cap": true,
    "q79:log-endpoint:de:T3:h0:finite-return": true,
    "q79:log-endpoint:de:T3:h0:fixed-sample-count": true,
    "q79:log-endpoint:de:T3:h1:callback-ledger": true,
    "q79:log-endpoint:de:T3:h1:evaluation-cap": true,
    "q79:log-endpoint:de:T3:h1:finite-return": true,
    "q79:log-endpoint:de:T3:h1:fixed-sample-count": true,
    "q79:log-endpoint:de:T3:h2:callback-ledger": true,
    "q79:log-endpoint:de:T3:h2:evaluation-cap": true,
    "q79:log-endpoint:de:T3:h2:finite-return": true,
    "q79:log-endpoint:de:T3:h2:fixed-sample-count": true,
    "q79:log-endpoint:de:T3:h3:callback-ledger": true,
    "q79:log-endpoint:de:T3:h3:evaluation-cap": true,
    "q79:log-endpoint:de:T3:h3:finite-return": true,
    "q79:log-endpoint:de:T3:h3:fixed-sample-count": true,
    "q79:log-endpoint:de:T4:h0:callback-ledger": true,
    "q79:log-endpoint:de:T4:h0:evaluation-cap": true,
    "q79:log-endpoint:de:T4:h0:finite-return": true,
    "q79:log-endpoint:de:T4:h0:fixed-sample-count": true,
    "q79:log-endpoint:de:T4:h1:callback-ledger": true,
    "q79:log-endpoint:de:T4:h1:evaluation-cap": true,
    "q79:log-endpoint:de:T4:h1:finite-return": true,
    "q79:log-endpoint:de:T4:h1:fixed-sample-count": true,
    "q79:log-endpoint:de:T4:h2:callback-ledger": true,
    "q79:log-endpoint:de:T4:h2:evaluation-cap": true,
    "q79:log-endpoint:de:T4:h2:finite-return": true,
    "q79:log-endpoint:de:T4:h2:fixed-sample-count": true,
    "q79:log-endpoint:de:T4:h3:callback-ledger": true,
    "q79:log-endpoint:de:T4:h3:evaluation-cap": true,
    "q79:log-endpoint:de:T4:h3:finite-return": true,
    "q79:log-endpoint:de:T4:h3:fixed-sample-count": true,
    "q79:log-endpoint:de:T4:h3:required-finest-accuracy": true,
    "gk15-double-exponential:fixed-record-count": true,
    "gk15-double-exponential:unique-record-ids": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/gk15-double-exponential/index.json

![Saved transformed integrands and finite-window defects; continuous tails are distinct](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/results/gk15-double-exponential-preview.png)

Saved transformed integrands and finite-window defects; continuous tails are distinct

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/atlas-quadrature-controls-2026-11-25.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- Pinned SciPy1.14.1 bundled dqk15 [accessed 2026-11-25]. https://raw.githubusercontent.com/scipy/scipy/v1.14.1/scipy/integrate/quadpack/dqk15.f; review_level=primary-software-source
- Double Exponential Formulas for Numerical Integration [accessed 2026-11-25]. https://ems.press/doi/pdf/10.2977/prims/1195192451; review_level=selected-primary-body-text

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## Tensor and Smolyak controls in two to four dimensions

Forty-two fixed cubatures compare a smooth product and an interaction product.

**Methods used**

- [Gaussian and adaptive quadrature](https://hrkoyama.github.io/numerical-methods-atlas/methods/quadrature/?lang=en) (`quadrature`)
- [Smolyak sparse-grid quadrature](https://hrkoyama.github.io/numerical-methods-atlas/methods/smolyak-sparse-grid/?lang=en) (`smolyak-sparse-grid`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/tensor-smolyak-dimensions/?lang=en#tensor-smolyak-dimensions-en-algorithm)

Canonical dyadic angle keys own shared nodes; signed weights and call ledgers are retained.

- [Finite, improper and multivariate definite integrals](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#definite-integrals-en) (`definite-integrals`)

The integration domain is[0,1]^d for d2/3/4; tensor levels1/2/3 and sparse levels1/2/3/4.


**Problem figure**

![Tensor and Smolyak controls in two to four dimensions: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/results/tensor-smolyak-dimensions.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Tensor and Smolyak controls in two to four dimensions](https://hrkoyama.github.io/numerical-methods-atlas/problems/tensor-smolyak-dimensions/?lang=en) (`tensor-smolyak-dimensions`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/tensor-smolyak-dimensions/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/tensor-smolyak-dimensions/?lang=en#tensor-smolyak-dimensions-en-validation)

Analytic integrals are distinct from companion Delta/combination assembly; interaction underresolution at L<d remains visible.

- [Tensor and Smolyak controls in two to four dimensions](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-tensor-smolyak-dimensions-en) (`tensor-smolyak-dimensions`; Same-problem reference · Analytic reference)

No general error monotonicity, positive-weight or cost-superiority claim; these are integration coordinates, not a physical PDE space.
### Assumptions, units and boundaries

The integration domain is[0,1]^d for d2/3/4; tensor levels1/2/3 and sparse levels1/2/3/4.

**Editorial clarification**

No general error monotonicity, positive-weight or cost-superiority claim; these are integration coordinates, not a physical PDE space. The formulas and inputs specify mathematical integration domains and dimensions. Parameter and error axes are not physical spatial coordinates. Passing reproduction checks does not mean that every accuracy goal was met. Original row outcomes: 24 met, 18 unmet and 0 not computable. False/NA outcomes and raw failures are retained.

### Adopted numerical method

Canonical dyadic angle keys own shared nodes; signed weights and call ledgers are retained.

$$
I=\int_\Omega f(x)\,dx
$$

### References and validation

Analytic integrals are distinct from companion Delta/combination assembly; interaction underresolution at L<d remains visible.

### Limits

No general error monotonicity, positive-weight or cost-superiority claim; these are integration coordinates, not a physical PDE space.

### Stored measurements and decisions

```json
{
  "metrics": {
    "records": 42,
    "integrand_evaluations": 18482,
    "accuracy_goals_met": 24,
    "accuracy_goals_unmet": 18,
    "accuracy_goals_unresolved": 0,
    "estimated_converged_rows": 42
  },
  "checks": {
    "q80:d2:smooth-product:tensor-clenshaw-curtis:L1:callback-ledger": true,
    "q80:d2:smooth-product:tensor-clenshaw-curtis:L1:evaluation-cap": true,
    "q80:d2:smooth-product:tensor-clenshaw-curtis:L1:finite-return": true,
    "q80:d2:smooth-product:tensor-clenshaw-curtis:L1:canonical-inventory": true,
    "q80:d2:smooth-product:tensor-clenshaw-curtis:L1:mass": true,
    "q80:d2:smooth-product:tensor-clenshaw-curtis:L1:low-moments": true,
    "q80:d2:smooth-product:tensor-clenshaw-curtis:L2:callback-ledger": true,
    "q80:d2:smooth-product:tensor-clenshaw-curtis:L2:evaluation-cap": true,
    "q80:d2:smooth-product:tensor-clenshaw-curtis:L2:finite-return": true,
    "q80:d2:smooth-product:tensor-clenshaw-curtis:L2:canonical-inventory": true,
    "q80:d2:smooth-product:tensor-clenshaw-curtis:L2:mass": true,
    "q80:d2:smooth-product:tensor-clenshaw-curtis:L2:low-moments": true,
    "q80:d2:smooth-product:tensor-clenshaw-curtis:L3:callback-ledger": true,
    "q80:d2:smooth-product:tensor-clenshaw-curtis:L3:evaluation-cap": true,
    "q80:d2:smooth-product:tensor-clenshaw-curtis:L3:finite-return": true,
    "q80:d2:smooth-product:tensor-clenshaw-curtis:L3:canonical-inventory": true,
    "q80:d2:smooth-product:tensor-clenshaw-curtis:L3:mass": true,
    "q80:d2:smooth-product:tensor-clenshaw-curtis:L3:low-moments": true,
    "q80:d2:smooth-product:tensor-clenshaw-curtis:L3:required-finest-accuracy": true,
    "q80:d2:smooth-product:smolyak-delta:L1:callback-ledger": true,
    "q80:d2:smooth-product:smolyak-delta:L1:evaluation-cap": true,
    "q80:d2:smooth-product:smolyak-delta:L1:finite-return": true,
    "q80:d2:smooth-product:smolyak-delta:L1:canonical-inventory": true,
    "q80:d2:smooth-product:smolyak-delta:L1:mass": true,
    "q80:d2:smooth-product:smolyak-delta:L1:low-moments": true,
    "q80:d2:smooth-product:smolyak-delta:L1:delta-combination": true,
    "q80:d2:smooth-product:smolyak-delta:L2:callback-ledger": true,
    "q80:d2:smooth-product:smolyak-delta:L2:evaluation-cap": true,
    "q80:d2:smooth-product:smolyak-delta:L2:finite-return": true,
    "q80:d2:smooth-product:smolyak-delta:L2:canonical-inventory": true,
    "q80:d2:smooth-product:smolyak-delta:L2:mass": true,
    "q80:d2:smooth-product:smolyak-delta:L2:low-moments": true,
    "q80:d2:smooth-product:smolyak-delta:L2:delta-combination": true,
    "q80:d2:smooth-product:smolyak-delta:L3:callback-ledger": true,
    "q80:d2:smooth-product:smolyak-delta:L3:evaluation-cap": true,
    "q80:d2:smooth-product:smolyak-delta:L3:finite-return": true,
    "q80:d2:smooth-product:smolyak-delta:L3:canonical-inventory": true,
    "q80:d2:smooth-product:smolyak-delta:L3:mass": true,
    "q80:d2:smooth-product:smolyak-delta:L3:low-moments": true,
    "q80:d2:smooth-product:smolyak-delta:L4:callback-ledger": true,
    "q80:d2:smooth-product:smolyak-delta:L4:evaluation-cap": true,
    "q80:d2:smooth-product:smolyak-delta:L4:finite-return": true,
    "q80:d2:smooth-product:smolyak-delta:L4:canonical-inventory": true,
    "q80:d2:smooth-product:smolyak-delta:L4:mass": true,
    "q80:d2:smooth-product:smolyak-delta:L4:low-moments": true,
    "q80:d2:smooth-product:smolyak-delta:L4:required-finest-accuracy": true,
    "q80:d2:interaction-product:tensor-clenshaw-curtis:L1:callback-ledger": true,
    "q80:d2:interaction-product:tensor-clenshaw-curtis:L1:evaluation-cap": true,
    "q80:d2:interaction-product:tensor-clenshaw-curtis:L1:finite-return": true,
    "q80:d2:interaction-product:tensor-clenshaw-curtis:L1:canonical-inventory": true,
    "q80:d2:interaction-product:tensor-clenshaw-curtis:L1:mass": true,
    "q80:d2:interaction-product:tensor-clenshaw-curtis:L1:low-moments": true,
    "q80:d2:interaction-product:tensor-clenshaw-curtis:L1:required-product-moment": true,
    "q80:d2:interaction-product:tensor-clenshaw-curtis:L2:callback-ledger": true,
    "q80:d2:interaction-product:tensor-clenshaw-curtis:L2:evaluation-cap": true,
    "q80:d2:interaction-product:tensor-clenshaw-curtis:L2:finite-return": true,
    "q80:d2:interaction-product:tensor-clenshaw-curtis:L2:canonical-inventory": true,
    "q80:d2:interaction-product:tensor-clenshaw-curtis:L2:mass": true,
    "q80:d2:interaction-product:tensor-clenshaw-curtis:L2:low-moments": true,
    "q80:d2:interaction-product:tensor-clenshaw-curtis:L2:required-product-moment": true,
    "q80:d2:interaction-product:tensor-clenshaw-curtis:L3:callback-ledger": true,
    "q80:d2:interaction-product:tensor-clenshaw-curtis:L3:evaluation-cap": true,
    "q80:d2:interaction-product:tensor-clenshaw-curtis:L3:finite-return": true,
    "q80:d2:interaction-product:tensor-clenshaw-curtis:L3:canonical-inventory": true,
    "q80:d2:interaction-product:tensor-clenshaw-curtis:L3:mass": true,
    "q80:d2:interaction-product:tensor-clenshaw-curtis:L3:low-moments": true,
    "q80:d2:interaction-product:tensor-clenshaw-curtis:L3:required-product-moment": true,
    "q80:d2:interaction-product:smolyak-delta:L1:callback-ledger": true,
    "q80:d2:interaction-product:smolyak-delta:L1:evaluation-cap": true,
    "q80:d2:interaction-product:smolyak-delta:L1:finite-return": true,
    "q80:d2:interaction-product:smolyak-delta:L1:canonical-inventory": true,
    "q80:d2:interaction-product:smolyak-delta:L1:mass": true,
    "q80:d2:interaction-product:smolyak-delta:L1:low-moments": true,
    "q80:d2:interaction-product:smolyak-delta:L1:delta-combination": true,
    "q80:d2:interaction-product:smolyak-delta:L1:underresolution-identity": true,
    "q80:d2:interaction-product:smolyak-delta:L2:callback-ledger": true,
    "q80:d2:interaction-product:smolyak-delta:L2:evaluation-cap": true,
    "q80:d2:interaction-product:smolyak-delta:L2:finite-return": true,
    "q80:d2:interaction-product:smolyak-delta:L2:canonical-inventory": true,
    "q80:d2:interaction-product:smolyak-delta:L2:mass": true,
    "q80:d2:interaction-product:smolyak-delta:L2:low-moments": true,
    "q80:d2:interaction-product:smolyak-delta:L2:delta-combination": true,
    "q80:d2:interaction-product:smolyak-delta:L2:required-product-moment": true,
    "q80:d2:interaction-product:smolyak-delta:L3:callback-ledger": true,
    "q80:d2:interaction-product:smolyak-delta:L3:evaluation-cap": true,
    "q80:d2:interaction-product:smolyak-delta:L3:finite-return": true,
    "q80:d2:interaction-product:smolyak-delta:L3:canonical-inventory": true,
    "q80:d2:interaction-product:smolyak-delta:L3:mass": true,
    "q80:d2:interaction-product:smolyak-delta:L3:low-moments": true,
    "q80:d2:interaction-product:smolyak-delta:L3:required-product-moment": true,
    "q80:d2:interaction-product:smolyak-delta:L4:callback-ledger": true,
    "q80:d2:interaction-product:smolyak-delta:L4:evaluation-cap": true,
    "q80:d2:interaction-product:smolyak-delta:L4:finite-return": true,
    "q80:d2:interaction-product:smolyak-delta:L4:canonical-inventory": true,
    "q80:d2:interaction-product:smolyak-delta:L4:mass": true,
    "q80:d2:interaction-product:smolyak-delta:L4:low-moments": true,
    "q80:d2:interaction-product:smolyak-delta:L4:required-product-moment": true,
    "q80:d3:smooth-product:tensor-clenshaw-curtis:L1:callback-ledger": true,
    "q80:d3:smooth-product:tensor-clenshaw-curtis:L1:evaluation-cap": true,
    "q80:d3:smooth-product:tensor-clenshaw-curtis:L1:finite-return": true,
    "q80:d3:smooth-product:tensor-clenshaw-curtis:L1:canonical-inventory": true,
    "q80:d3:smooth-product:tensor-clenshaw-curtis:L1:mass": true,
    "q80:d3:smooth-product:tensor-clenshaw-curtis:L1:low-moments": true,
    "q80:d3:smooth-product:tensor-clenshaw-curtis:L2:callback-ledger": true,
    "q80:d3:smooth-product:tensor-clenshaw-curtis:L2:evaluation-cap": true,
    "q80:d3:smooth-product:tensor-clenshaw-curtis:L2:finite-return": true,
    "q80:d3:smooth-product:tensor-clenshaw-curtis:L2:canonical-inventory": true,
    "q80:d3:smooth-product:tensor-clenshaw-curtis:L2:mass": true,
    "q80:d3:smooth-product:tensor-clenshaw-curtis:L2:low-moments": true,
    "q80:d3:smooth-product:tensor-clenshaw-curtis:L3:callback-ledger": true,
    "q80:d3:smooth-product:tensor-clenshaw-curtis:L3:evaluation-cap": true,
    "q80:d3:smooth-product:tensor-clenshaw-curtis:L3:finite-return": true,
    "q80:d3:smooth-product:tensor-clenshaw-curtis:L3:canonical-inventory": true,
    "q80:d3:smooth-product:tensor-clenshaw-curtis:L3:mass": true,
    "q80:d3:smooth-product:tensor-clenshaw-curtis:L3:low-moments": true,
    "q80:d3:smooth-product:tensor-clenshaw-curtis:L3:required-finest-accuracy": true,
    "q80:d3:smooth-product:smolyak-delta:L1:callback-ledger": true,
    "q80:d3:smooth-product:smolyak-delta:L1:evaluation-cap": true,
    "q80:d3:smooth-product:smolyak-delta:L1:finite-return": true,
    "q80:d3:smooth-product:smolyak-delta:L1:canonical-inventory": true,
    "q80:d3:smooth-product:smolyak-delta:L1:mass": true,
    "q80:d3:smooth-product:smolyak-delta:L1:low-moments": true,
    "q80:d3:smooth-product:smolyak-delta:L1:delta-combination": true,
    "q80:d3:smooth-product:smolyak-delta:L2:callback-ledger": true,
    "q80:d3:smooth-product:smolyak-delta:L2:evaluation-cap": true,
    "q80:d3:smooth-product:smolyak-delta:L2:finite-return": true,
    "q80:d3:smooth-product:smolyak-delta:L2:canonical-inventory": true,
    "q80:d3:smooth-product:smolyak-delta:L2:mass": true,
    "q80:d3:smooth-product:smolyak-delta:L2:low-moments": true,
    "q80:d3:smooth-product:smolyak-delta:L2:delta-combination": true,
    "q80:d3:smooth-product:smolyak-delta:L3:callback-ledger": true,
    "q80:d3:smooth-product:smolyak-delta:L3:evaluation-cap": true,
    "q80:d3:smooth-product:smolyak-delta:L3:finite-return": true,
    "q80:d3:smooth-product:smolyak-delta:L3:canonical-inventory": true,
    "q80:d3:smooth-product:smolyak-delta:L3:mass": true,
    "q80:d3:smooth-product:smolyak-delta:L3:low-moments": true,
    "q80:d3:smooth-product:smolyak-delta:L4:callback-ledger": true,
    "q80:d3:smooth-product:smolyak-delta:L4:evaluation-cap": true,
    "q80:d3:smooth-product:smolyak-delta:L4:finite-return": true,
    "q80:d3:smooth-product:smolyak-delta:L4:canonical-inventory": true,
    "q80:d3:smooth-product:smolyak-delta:L4:mass": true,
    "q80:d3:smooth-product:smolyak-delta:L4:low-moments": true,
    "q80:d3:smooth-product:smolyak-delta:L4:required-finest-accuracy": true,
    "q80:d3:interaction-product:tensor-clenshaw-curtis:L1:callback-ledger": true,
    "q80:d3:interaction-product:tensor-clenshaw-curtis:L1:evaluation-cap": true,
    "q80:d3:interaction-product:tensor-clenshaw-curtis:L1:finite-return": true,
    "q80:d3:interaction-product:tensor-clenshaw-curtis:L1:canonical-inventory": true,
    "q80:d3:interaction-product:tensor-clenshaw-curtis:L1:mass": true,
    "q80:d3:interaction-product:tensor-clenshaw-curtis:L1:low-moments": true,
    "q80:d3:interaction-product:tensor-clenshaw-curtis:L1:required-product-moment": true,
    "q80:d3:interaction-product:tensor-clenshaw-curtis:L2:callback-ledger": true,
    "q80:d3:interaction-product:tensor-clenshaw-curtis:L2:evaluation-cap": true,
    "q80:d3:interaction-product:tensor-clenshaw-curtis:L2:finite-return": true,
    "q80:d3:interaction-product:tensor-clenshaw-curtis:L2:canonical-inventory": true,
    "q80:d3:interaction-product:tensor-clenshaw-curtis:L2:mass": true,
    "q80:d3:interaction-product:tensor-clenshaw-curtis:L2:low-moments": true,
    "q80:d3:interaction-product:tensor-clenshaw-curtis:L2:required-product-moment": true,
    "q80:d3:interaction-product:tensor-clenshaw-curtis:L3:callback-ledger": true,
    "q80:d3:interaction-product:tensor-clenshaw-curtis:L3:evaluation-cap": true,
    "q80:d3:interaction-product:tensor-clenshaw-curtis:L3:finite-return": true,
    "q80:d3:interaction-product:tensor-clenshaw-curtis:L3:canonical-inventory": true,
    "q80:d3:interaction-product:tensor-clenshaw-curtis:L3:mass": true,
    "q80:d3:interaction-product:tensor-clenshaw-curtis:L3:low-moments": true,
    "q80:d3:interaction-product:tensor-clenshaw-curtis:L3:required-product-moment": true,
    "q80:d3:interaction-product:smolyak-delta:L1:callback-ledger": true,
    "q80:d3:interaction-product:smolyak-delta:L1:evaluation-cap": true,
    "q80:d3:interaction-product:smolyak-delta:L1:finite-return": true,
    "q80:d3:interaction-product:smolyak-delta:L1:canonical-inventory": true,
    "q80:d3:interaction-product:smolyak-delta:L1:mass": true,
    "q80:d3:interaction-product:smolyak-delta:L1:low-moments": true,
    "q80:d3:interaction-product:smolyak-delta:L1:delta-combination": true,
    "q80:d3:interaction-product:smolyak-delta:L1:underresolution-identity": true,
    "q80:d3:interaction-product:smolyak-delta:L2:callback-ledger": true,
    "q80:d3:interaction-product:smolyak-delta:L2:evaluation-cap": true,
    "q80:d3:interaction-product:smolyak-delta:L2:finite-return": true,
    "q80:d3:interaction-product:smolyak-delta:L2:canonical-inventory": true,
    "q80:d3:interaction-product:smolyak-delta:L2:mass": true,
    "q80:d3:interaction-product:smolyak-delta:L2:low-moments": true,
    "q80:d3:interaction-product:smolyak-delta:L2:delta-combination": true,
    "q80:d3:interaction-product:smolyak-delta:L2:underresolution-identity": true,
    "q80:d3:interaction-product:smolyak-delta:L3:callback-ledger": true,
    "q80:d3:interaction-product:smolyak-delta:L3:evaluation-cap": true,
    "q80:d3:interaction-product:smolyak-delta:L3:finite-return": true,
    "q80:d3:interaction-product:smolyak-delta:L3:canonical-inventory": true,
    "q80:d3:interaction-product:smolyak-delta:L3:mass": true,
    "q80:d3:interaction-product:smolyak-delta:L3:low-moments": true,
    "q80:d3:interaction-product:smolyak-delta:L3:required-product-moment": true,
    "q80:d3:interaction-product:smolyak-delta:L4:callback-ledger": true,
    "q80:d3:interaction-product:smolyak-delta:L4:evaluation-cap": true,
    "q80:d3:interaction-product:smolyak-delta:L4:finite-return": true,
    "q80:d3:interaction-product:smolyak-delta:L4:canonical-inventory": true,
    "q80:d3:interaction-product:smolyak-delta:L4:mass": true,
    "q80:d3:interaction-product:smolyak-delta:L4:low-moments": true,
    "q80:d3:interaction-product:smolyak-delta:L4:required-product-moment": true,
    "q80:d4:smooth-product:tensor-clenshaw-curtis:L1:callback-ledger": true,
    "q80:d4:smooth-product:tensor-clenshaw-curtis:L1:evaluation-cap": true,
    "q80:d4:smooth-product:tensor-clenshaw-curtis:L1:finite-return": true,
    "q80:d4:smooth-product:tensor-clenshaw-curtis:L1:canonical-inventory": true,
    "q80:d4:smooth-product:tensor-clenshaw-curtis:L1:mass": true,
    "q80:d4:smooth-product:tensor-clenshaw-curtis:L1:low-moments": true,
    "q80:d4:smooth-product:tensor-clenshaw-curtis:L2:callback-ledger": true,
    "q80:d4:smooth-product:tensor-clenshaw-curtis:L2:evaluation-cap": true,
    "q80:d4:smooth-product:tensor-clenshaw-curtis:L2:finite-return": true,
    "q80:d4:smooth-product:tensor-clenshaw-curtis:L2:canonical-inventory": true,
    "q80:d4:smooth-product:tensor-clenshaw-curtis:L2:mass": true,
    "q80:d4:smooth-product:tensor-clenshaw-curtis:L2:low-moments": true,
    "q80:d4:smooth-product:tensor-clenshaw-curtis:L3:callback-ledger": true,
    "q80:d4:smooth-product:tensor-clenshaw-curtis:L3:evaluation-cap": true,
    "q80:d4:smooth-product:tensor-clenshaw-curtis:L3:finite-return": true,
    "q80:d4:smooth-product:tensor-clenshaw-curtis:L3:canonical-inventory": true,
    "q80:d4:smooth-product:tensor-clenshaw-curtis:L3:mass": true,
    "q80:d4:smooth-product:tensor-clenshaw-curtis:L3:low-moments": true,
    "q80:d4:smooth-product:tensor-clenshaw-curtis:L3:required-finest-accuracy": true,
    "q80:d4:smooth-product:smolyak-delta:L1:callback-ledger": true,
    "q80:d4:smooth-product:smolyak-delta:L1:evaluation-cap": true,
    "q80:d4:smooth-product:smolyak-delta:L1:finite-return": true,
    "q80:d4:smooth-product:smolyak-delta:L1:canonical-inventory": true,
    "q80:d4:smooth-product:smolyak-delta:L1:mass": true,
    "q80:d4:smooth-product:smolyak-delta:L1:low-moments": true,
    "q80:d4:smooth-product:smolyak-delta:L2:callback-ledger": true,
    "q80:d4:smooth-product:smolyak-delta:L2:evaluation-cap": true,
    "q80:d4:smooth-product:smolyak-delta:L2:finite-return": true,
    "q80:d4:smooth-product:smolyak-delta:L2:canonical-inventory": true,
    "q80:d4:smooth-product:smolyak-delta:L2:mass": true,
    "q80:d4:smooth-product:smolyak-delta:L2:low-moments": true,
    "q80:d4:smooth-product:smolyak-delta:L3:callback-ledger": true,
    "q80:d4:smooth-product:smolyak-delta:L3:evaluation-cap": true,
    "q80:d4:smooth-product:smolyak-delta:L3:finite-return": true,
    "q80:d4:smooth-product:smolyak-delta:L3:canonical-inventory": true,
    "q80:d4:smooth-product:smolyak-delta:L3:mass": true,
    "q80:d4:smooth-product:smolyak-delta:L3:low-moments": true,
    "q80:d4:smooth-product:smolyak-delta:L4:callback-ledger": true,
    "q80:d4:smooth-product:smolyak-delta:L4:evaluation-cap": true,
    "q80:d4:smooth-product:smolyak-delta:L4:finite-return": true,
    "q80:d4:smooth-product:smolyak-delta:L4:canonical-inventory": true,
    "q80:d4:smooth-product:smolyak-delta:L4:mass": true,
    "q80:d4:smooth-product:smolyak-delta:L4:low-moments": true,
    "q80:d4:smooth-product:smolyak-delta:L4:required-finest-accuracy": true,
    "q80:d4:interaction-product:tensor-clenshaw-curtis:L1:callback-ledger": true,
    "q80:d4:interaction-product:tensor-clenshaw-curtis:L1:evaluation-cap": true,
    "q80:d4:interaction-product:tensor-clenshaw-curtis:L1:finite-return": true,
    "q80:d4:interaction-product:tensor-clenshaw-curtis:L1:canonical-inventory": true,
    "q80:d4:interaction-product:tensor-clenshaw-curtis:L1:mass": true,
    "q80:d4:interaction-product:tensor-clenshaw-curtis:L1:low-moments": true,
    "q80:d4:interaction-product:tensor-clenshaw-curtis:L1:required-product-moment": true,
    "q80:d4:interaction-product:tensor-clenshaw-curtis:L2:callback-ledger": true,
    "q80:d4:interaction-product:tensor-clenshaw-curtis:L2:evaluation-cap": true,
    "q80:d4:interaction-product:tensor-clenshaw-curtis:L2:finite-return": true,
    "q80:d4:interaction-product:tensor-clenshaw-curtis:L2:canonical-inventory": true,
    "q80:d4:interaction-product:tensor-clenshaw-curtis:L2:mass": true,
    "q80:d4:interaction-product:tensor-clenshaw-curtis:L2:low-moments": true,
    "q80:d4:interaction-product:tensor-clenshaw-curtis:L2:required-product-moment": true,
    "q80:d4:interaction-product:tensor-clenshaw-curtis:L3:callback-ledger": true,
    "q80:d4:interaction-product:tensor-clenshaw-curtis:L3:evaluation-cap": true,
    "q80:d4:interaction-product:tensor-clenshaw-curtis:L3:finite-return": true,
    "q80:d4:interaction-product:tensor-clenshaw-curtis:L3:canonical-inventory": true,
    "q80:d4:interaction-product:tensor-clenshaw-curtis:L3:mass": true,
    "q80:d4:interaction-product:tensor-clenshaw-curtis:L3:low-moments": true,
    "q80:d4:interaction-product:tensor-clenshaw-curtis:L3:required-product-moment": true,
    "q80:d4:interaction-product:smolyak-delta:L1:callback-ledger": true,
    "q80:d4:interaction-product:smolyak-delta:L1:evaluation-cap": true,
    "q80:d4:interaction-product:smolyak-delta:L1:finite-return": true,
    "q80:d4:interaction-product:smolyak-delta:L1:canonical-inventory": true,
    "q80:d4:interaction-product:smolyak-delta:L1:mass": true,
    "q80:d4:interaction-product:smolyak-delta:L1:low-moments": true,
    "q80:d4:interaction-product:smolyak-delta:L1:underresolution-identity": true,
    "q80:d4:interaction-product:smolyak-delta:L2:callback-ledger": true,
    "q80:d4:interaction-product:smolyak-delta:L2:evaluation-cap": true,
    "q80:d4:interaction-product:smolyak-delta:L2:finite-return": true,
    "q80:d4:interaction-product:smolyak-delta:L2:canonical-inventory": true,
    "q80:d4:interaction-product:smolyak-delta:L2:mass": true,
    "q80:d4:interaction-product:smolyak-delta:L2:low-moments": true,
    "q80:d4:interaction-product:smolyak-delta:L2:underresolution-identity": true,
    "q80:d4:interaction-product:smolyak-delta:L3:callback-ledger": true,
    "q80:d4:interaction-product:smolyak-delta:L3:evaluation-cap": true,
    "q80:d4:interaction-product:smolyak-delta:L3:finite-return": true,
    "q80:d4:interaction-product:smolyak-delta:L3:canonical-inventory": true,
    "q80:d4:interaction-product:smolyak-delta:L3:mass": true,
    "q80:d4:interaction-product:smolyak-delta:L3:low-moments": true,
    "q80:d4:interaction-product:smolyak-delta:L3:underresolution-identity": true,
    "q80:d4:interaction-product:smolyak-delta:L4:callback-ledger": true,
    "q80:d4:interaction-product:smolyak-delta:L4:evaluation-cap": true,
    "q80:d4:interaction-product:smolyak-delta:L4:finite-return": true,
    "q80:d4:interaction-product:smolyak-delta:L4:canonical-inventory": true,
    "q80:d4:interaction-product:smolyak-delta:L4:mass": true,
    "q80:d4:interaction-product:smolyak-delta:L4:low-moments": true,
    "q80:d4:interaction-product:smolyak-delta:L4:required-product-moment": true,
    "tensor-smolyak-dimensions:fixed-record-count": true,
    "tensor-smolyak-dimensions:unique-record-ids": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/tensor-smolyak-dimensions/index.json

![Actual two-dimensional nodes and signed integration weights](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/results/tensor-smolyak-dimensions-preview.png)

Actual two-dimensional nodes and signed integration weights

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/atlas-quadrature-controls-2026-11-25.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- Fast Construction of the Fejer and Clenshaw-Curtis Quadrature Rules [accessed 2026-11-25]. https://www.sam.math.ethz.ch/sam_reports/reports_final/reports2008/2008-07.pdf; review_level=selected-primary-body-text

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
