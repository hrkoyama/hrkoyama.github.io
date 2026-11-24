# Reverse mode, HVPs and nonsmooth branches

Independent hand-derived references check a small original tape, separating fixed-state partials, implicit total derivatives and executed branches.

These additional validation supplements are managed separately from the common 22-example registry. Receipts cover independent ZIP extraction, tests and every fixed input within each group. Changes of settings, methods or step sizes do not add independent physical problems.

## Original reverse-mode VJP and JVP/VJP duality

Check a genuine reverse tape, including repeated-index gather and broadcast, against independent Jacobians.

**Methods used**

- [Automatic differentiation](https://hrkoyama.github.io/numerical-methods-atlas/methods/automatic-differentiation/?lang=en) (`automatic-differentiation`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/reverse-vjp-duality/?lang=en#reverse-vjp-duality-en-algorithm)

Accumulate cotangents in reverse topological order with a separate forward directional path.

$$
Jv=Df(x)v, VJP=J^T w
$$

$$
<Jv,w>_Gy=<v,Gx^-1 J^T Gy w>_Gx
$$

- [Finite-dimensional nonlinear maps, roots and differential actions](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#finite-dimensional-nonlinear-map-en) (`finite-dimensional-nonlinear-map`)

Small fixed real dimensionless inputs; assumptions and scope are limited to the matching contract.

- [Bratu nonlinear boundary-value problem](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bratu-en) (`bratu`)

Small fixed real dimensionless inputs; assumptions and scope are limited to the matching contract.


**Problem figure**

![Original reverse-mode VJP and JVP/VJP duality: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/results/reverse-vjp-duality.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Original reverse-mode VJP and JVP/VJP duality](https://hrkoyama.github.io/numerical-methods-atlas/problems/reverse-vjp-duality/?lang=en) (`reverse-vjp-duality`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/reverse-vjp-duality/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/reverse-vjp-duality/?lang=en#reverse-vjp-duality-en-validation)

Check fixed inputs, independent references, retained candidates and every gate within the same120-second budget. Numerical success and diagnostic nonconvergence are distinct.

- [Independent Jacobians, JVPs and VJPs of discrete nonlinear maps](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-reverse-vjp-duality-en) (`reverse-vjp-duality`; Same-problem reference · Analytic reference)

Not a general NumPy/JAX replacement or complex AD system.
### Assumptions, units and boundaries

Small fixed real dimensionless inputs; assumptions and scope are limited to the matching contract.

**Editorial clarification**

Not a general NumPy/JAX replacement or complex AD system. Plot axes describe finite-dimensional variables, iterations or diagnostics, not a physical spatial dimension or PDE boundary.

### Adopted numerical method

Accumulate cotangents in reverse topological order with a separate forward directional path.

$$
Jv=Df(x)v, VJP=J^T w
$$

$$
<Jv,w>_Gy=<v,Gx^-1 J^T Gy w>_Gx
$$

### References and validation

Check fixed inputs, independent references, retained candidates and every gate within the same120-second budget. Numerical success and diagnostic nonconvergence are distinct.

### Limits

Not a general NumPy/JAX replacement or complex AD system.

### Stored measurements and decisions

```json
{
  "metrics": {
    "max_JVP_oracle_error": 1.2338534194174146e-13,
    "max_VJP_oracle_error": 5.335730008286552e-13,
    "max_duality_defect": 7.105427357601002e-15,
    "actual_forward_seeds": 80,
    "actual_reverse_pullbacks": 68
  },
  "checks": {
    "rectangular4x3/primal": true,
    "rectangular4x3/independentJVP": true,
    "rectangular4x3/independentVJP": true,
    "rectangular4x3/fullforwardJacobian": true,
    "rectangular4x3/fullreverseJacobian": true,
    "rectangular4x3/duality": true,
    "rectangular4x3/reset_ownership": true,
    "rectangular4x3/measuredsweepcounts": true,
    "metric/product": true,
    "metric/pairing": true,
    "negative/drop-duplicate": true,
    "negative/broadcast-first": true,
    "negative/permuted-output": true,
    "negative/stale-cotangent": true,
    "wide7/primal": true,
    "wide7/independentJVP": true,
    "wide7/independentVJP": true,
    "wide7/fullforwardJacobian": true,
    "wide7/fullreverseJacobian": true,
    "wide7/duality": true,
    "wide7/reset_ownership": true,
    "wide7/measuredsweepcounts": true,
    "wide31/primal": true,
    "wide31/independentJVP": true,
    "wide31/independentVJP": true,
    "wide31/fullforwardJacobian": true,
    "wide31/fullreverseJacobian": true,
    "wide31/duality": true,
    "wide31/reset_ownership": true,
    "wide31/measuredsweepcounts": true,
    "bratu7/primal": true,
    "bratu7/independentJVP": true,
    "bratu7/independentVJP": true,
    "bratu7/fullforwardJacobian": true,
    "bratu7/fullreverseJacobian": true,
    "bratu7/duality": true,
    "bratu7/reset_ownership": true,
    "bratu7/measuredsweepcounts": true,
    "bratu31/primal": true,
    "bratu31/independentJVP": true,
    "bratu31/independentVJP": true,
    "bratu31/fullforwardJacobian": true,
    "bratu31/fullreverseJacobian": true,
    "bratu31/duality": true,
    "bratu31/reset_ownership": true,
    "bratu31/measuredsweepcounts": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/reverse-vjp-duality/index.json

![Independent rectangular Jacobian, actual reverse differentiation error and measured sweep counts for fixed wide maps.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/results/reverse-vjp-duality-preview.png)

Independent rectangular Jacobian, actual reverse differentiation error and measured sweep counts for fixed wide maps.

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/atlas-reverse-higher-ad-2026-11-24.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- The JAX authors (n.d.). The Autodiff Cookbook [accessed 2026-11-24]. https://docs.jax.dev/en/latest/notebooks/autodiff_cookbook.html; review_level=official-documentation-selected-mathematical-sections
Selected definitions and composition formulas only. A new educational tape will implement the stated finite subset. No JAX installation, execution, timing replication or implementation-source audit. Unread: Original reverse-mode/HVP papers, JAX transformation implementation, Unselected cookbook sections. Publication year not established (n.d.).

- The JAX authors (n.d.). Frequently asked questions: undefined branches and ordering [accessed 2026-11-24]. https://docs.jax.dev/en/latest/faq.html; review_level=official-documentation-selected-sections
Read invalid inactive-branch and ordering discussions. We use an explicitly different strict nondifferentiability policy, not a universal JAX tie rule. Unread: Linked issue threads, Generalized derivative original papers. Publication year not established (n.d.).


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## Hessian-vector products and fixed-state versus implicit derivatives

Check forward-over-reverse HVPs and second-order implicit rules against separate independent references.

**Methods used**

- [Automatic differentiation](https://hrkoyama.github.io/numerical-methods-atlas/methods/automatic-differentiation/?lang=en) (`automatic-differentiation`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/hessian-vector-products/?lang=en#hessian-vector-products-en-algorithm)

Transport values, tangents, cotangents and cotangent tangents; solve F/R1/R2 for implicit derivatives.

$$
Hv=D(grad f)(x)v
$$

$$
F=u^2-theta=0, 2u*s=1, 2u*t+2s^2=0
$$

- [Finite-dimensional nonlinear maps, roots and differential actions](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#finite-dimensional-nonlinear-map-en) (`finite-dimensional-nonlinear-map`)

Small fixed real dimensionless inputs; assumptions and scope are limited to the matching contract.

- [Bratu nonlinear boundary-value problem](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bratu-en) (`bratu`)

Small fixed real dimensionless inputs; assumptions and scope are limited to the matching contract.


**Problem figure**

![Hessian-vector products and fixed-state versus implicit derivatives: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/results/hessian-vector-products.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Hessian-vector products and fixed-state versus implicit derivatives](https://hrkoyama.github.io/numerical-methods-atlas/problems/hessian-vector-products/?lang=en) (`hessian-vector-products`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/hessian-vector-products/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/hessian-vector-products/?lang=en#hessian-vector-products-en-validation)

Check fixed inputs, independent references, retained candidates and every gate within the same120-second budget. Numerical success and diagnostic nonconvergence are distinct.

- [Independent references for fixed-state HVPs and second-order implicit rules](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-hessian-vector-products-en) (`hessian-vector-products`; Same-problem reference · Analytic reference)

No general reduced inverse Hessian or identification of finite Newton traces with implicit derivatives.
### Assumptions, units and boundaries

Small fixed real dimensionless inputs; assumptions and scope are limited to the matching contract.

**Editorial clarification**

No general reduced inverse Hessian or identification of finite Newton traces with implicit derivatives. Plot axes describe finite-dimensional variables, iterations or diagnostics, not a physical spatial dimension or PDE boundary.

### Adopted numerical method

Transport values, tangents, cotangents and cotangent tangents; solve F/R1/R2 for implicit derivatives.

$$
Hv=D(grad f)(x)v
$$

$$
F=u^2-theta=0, 2u*s=1, 2u*t+2s^2=0
$$

### References and validation

Check fixed inputs, independent references, retained candidates and every gate within the same120-second budget. Numerical success and diagnostic nonconvergence are distinct.

### Limits

No general reduced inverse Hessian or identification of finite Newton traces with implicit derivatives.

### Stored measurements and decisions

```json
{
  "metrics": {
    "max_HVP_oracle_error": 5.8127826803247354e-15,
    "max_bilinear_symmetry_defect": 0.0,
    "implicit_state_residual": 0.0,
    "implicit_tangent_residual": 0.0,
    "implicit_second_tangent_residual": 0.0,
    "implicit_total_curvature": 0.23125
  },
  "checks": {
    "quadratic4/finite": true,
    "quadratic4/reference_product": true,
    "quadratic4/primary_path_ownership": true,
    "quadratic4/work_counters": true,
    "quadratic4/independent_gradient": true,
    "quadratic4/bilinear_symmetry": true,
    "bratu-energy7/finite": true,
    "bratu-energy7/reference_product": true,
    "bratu-energy7/primary_path_ownership": true,
    "bratu-energy7/work_counters": true,
    "bratu-energy7/independent_gradient": true,
    "bratu-energy7/bilinear_symmetry": true,
    "bratu-energy31/finite": true,
    "bratu-energy31/reference_product": true,
    "bratu-energy31/primary_path_ownership": true,
    "bratu-energy31/work_counters": true,
    "bratu-energy31/independent_gradient": true,
    "bratu-energy31/bilinear_symmetry": true,
    "implicit-scalar4/finite": true,
    "implicit-scalar4/reference_product": true,
    "implicit-scalar4/primary_path_ownership": true,
    "implicit-scalar4/work_counters": true,
    "implicit/state_residual": true,
    "implicit/first_tangent_residual": true,
    "implicit/second_tangent_residual": true,
    "implicit/fixed_partial": true,
    "implicit/total_curvature": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/hessian-vector-products/index.json

![Saved HVPs and independent references, with fixed-state and total implicit second derivatives shown separately.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/results/hessian-vector-products-preview.png)

Saved HVPs and independent references, with fixed-state and total implicit second derivatives shown separately.

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/atlas-reverse-higher-ad-2026-11-24.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- The JAX authors (n.d.). The Autodiff Cookbook [accessed 2026-11-24]. https://docs.jax.dev/en/latest/notebooks/autodiff_cookbook.html; review_level=official-documentation-selected-mathematical-sections
Selected definitions and composition formulas only. A new educational tape will implement the stated finite subset. No JAX installation, execution, timing replication or implementation-source audit. Unread: Original reverse-mode/HVP papers, JAX transformation implementation, Unselected cookbook sections. Publication year not established (n.d.).

- The JAX authors (n.d.). Frequently asked questions: undefined branches and ordering [accessed 2026-11-24]. https://docs.jax.dev/en/latest/faq.html; review_level=official-documentation-selected-sections
Read invalid inactive-branch and ordering discussions. We use an explicitly different strict nondifferentiability policy, not a universal JAX tie rule. Unread: Linked issue threads, Generalized derivative original papers. Publication year not established (n.d.).


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## Derivative scope at kinks, branches and stopping decisions

Distinguish classical, one-sided directional and executed-trace derivatives at fixed kinks and stopping switches.

**Methods used**

- [Automatic differentiation](https://hrkoyama.github.io/numerical-methods-atlas/methods/automatic-differentiation/?lang=en) (`automatic-differentiation`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/kink-branch-derivatives/?lang=en#kink-branch-derivatives-en-algorithm)

Report strict nondifferentiability explicitly and record the literal top-of-loop stopping branch.

$$
x_(k+1)=.5(x_k+theta), |x_k-theta|<=1/8
$$

$$
D max(0,0)[da,db]=max(da,db)
$$

- [Finite-dimensional nonlinear maps, roots and differential actions](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#finite-dimensional-nonlinear-map-en) (`finite-dimensional-nonlinear-map`)

Small fixed real dimensionless inputs; assumptions and scope are limited to the matching contract.


**Problem figure**

![Derivative scope at kinks, branches and stopping decisions: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/results/kink-branch-derivatives.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Derivative scope at kinks, branches and stopping decisions](https://hrkoyama.github.io/numerical-methods-atlas/problems/kink-branch-derivatives/?lang=en) (`kink-branch-derivatives`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/kink-branch-derivatives/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/kink-branch-derivatives/?lang=en#kink-branch-derivatives-en-validation)

Check fixed inputs, independent references, retained candidates and every gate within the same120-second budget. Numerical success and diagnostic nonconvergence are distinct.

- [Nonsmooth discrete maps: directional derivatives and executed traces](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-kink-branch-derivatives-en) (`kink-branch-derivatives`; Same-problem reference · Analytic reference)

An executed-branch derivative is not a universal subgradient or a linear derivative of a nonsmooth map.
### Assumptions, units and boundaries

Small fixed real dimensionless inputs; assumptions and scope are limited to the matching contract.

**Editorial clarification**

An executed-branch derivative is not a universal subgradient or a linear derivative of a nonsmooth map. Plot axes describe finite-dimensional variables, iterations or diagnostics, not a physical spatial dimension or PDE boundary.

### Adopted numerical method

Report strict nondifferentiability explicitly and record the literal top-of-loop stopping branch.

$$
x_(k+1)=.5(x_k+theta), |x_k-theta|<=1/8
$$

$$
D max(0,0)[da,db]=max(da,db)
$$

### References and validation

Check fixed inputs, independent references, retained candidates and every gate within the same120-second budget. Numerical success and diagnostic nonconvergence are distinct.

### Limits

An executed-branch derivative is not a universal subgradient or a linear derivative of a nonsmooth map.

### Stored measurements and decisions

```json
{
  "metrics": {
    "max_smooth_slope_oracle_error": 0.0,
    "max_fixed_trace_slope_error": 0.0,
    "stop_switch_jump": 0.0625,
    "max_jump_quotient_identity_error": 0.0,
    "inactive_invalid_branch_calls": 0
  },
  "checks": {
    "abs-0--1/category": true,
    "abs-0--1/finite_oracle_values": true,
    "abs-0-1/category": true,
    "abs-0-1/finite_oracle_values": true,
    "abs-1--1/category": true,
    "abs-1--1/finite_oracle_values": true,
    "abs-1-1/category": true,
    "abs-1-1/finite_oracle_values": true,
    "abs-2--1/category": true,
    "abs-2--1/finite_oracle_values": true,
    "abs-2-1/category": true,
    "abs-2-1/finite_oracle_values": true,
    "abs-3--1/category": true,
    "abs-3--1/finite_oracle_values": true,
    "abs-3-1/category": true,
    "abs-3-1/finite_oracle_values": true,
    "abs-4--1/category": true,
    "abs-4--1/finite_oracle_values": true,
    "abs-4-1/category": true,
    "abs-4-1/finite_oracle_values": true,
    "abs-5--1/category": true,
    "abs-5--1/finite_oracle_values": true,
    "abs-5-1/category": true,
    "abs-5-1/finite_oracle_values": true,
    "abs-6--1/category": true,
    "abs-6--1/finite_oracle_values": true,
    "abs-6-1/category": true,
    "abs-6-1/finite_oracle_values": true,
    "relu-0--1/category": true,
    "relu-0--1/finite_oracle_values": true,
    "relu-0-1/category": true,
    "relu-0-1/finite_oracle_values": true,
    "relu-1--1/category": true,
    "relu-1--1/finite_oracle_values": true,
    "relu-1-1/category": true,
    "relu-1-1/finite_oracle_values": true,
    "relu-2--1/category": true,
    "relu-2--1/finite_oracle_values": true,
    "relu-2-1/category": true,
    "relu-2-1/finite_oracle_values": true,
    "relu-3--1/category": true,
    "relu-3--1/finite_oracle_values": true,
    "relu-3-1/category": true,
    "relu-3-1/finite_oracle_values": true,
    "relu-4--1/category": true,
    "relu-4--1/finite_oracle_values": true,
    "relu-4-1/category": true,
    "relu-4-1/finite_oracle_values": true,
    "relu-5--1/category": true,
    "relu-5--1/finite_oracle_values": true,
    "relu-5-1/category": true,
    "relu-5-1/finite_oracle_values": true,
    "relu-6--1/category": true,
    "relu-6--1/finite_oracle_values": true,
    "relu-6-1/category": true,
    "relu-6-1/finite_oracle_values": true,
    "clip-0--1/category": true,
    "clip-0--1/finite_oracle_values": true,
    "clip-0-1/category": true,
    "clip-0-1/finite_oracle_values": true,
    "clip-1--1/category": true,
    "clip-1--1/finite_oracle_values": true,
    "clip-1-1/category": true,
    "clip-1-1/finite_oracle_values": true,
    "clip-2--1/category": true,
    "clip-2--1/finite_oracle_values": true,
    "clip-2-1/category": true,
    "clip-2-1/finite_oracle_values": true,
    "clip-3--1/category": true,
    "clip-3--1/finite_oracle_values": true,
    "clip-3-1/category": true,
    "clip-3-1/finite_oracle_values": true,
    "clip-4--1/category": true,
    "clip-4--1/finite_oracle_values": true,
    "clip-4-1/category": true,
    "clip-4-1/finite_oracle_values": true,
    "clip-5--1/category": true,
    "clip-5--1/finite_oracle_values": true,
    "clip-5-1/category": true,
    "clip-5-1/finite_oracle_values": true,
    "clip-6--1/category": true,
    "clip-6--1/finite_oracle_values": true,
    "clip-6-1/category": true,
    "clip-6-1/finite_oracle_values": true,
    "branch-0--1/category": true,
    "branch-0--1/finite_oracle_values": true,
    "branch-0-1/category": true,
    "branch-0-1/finite_oracle_values": true,
    "branch-1--1/category": true,
    "branch-1--1/finite_oracle_values": true,
    "branch-1-1/category": true,
    "branch-1-1/finite_oracle_values": true,
    "branch-2--1/category": true,
    "branch-2--1/finite_oracle_values": true,
    "branch-2-1/category": true,
    "branch-2-1/finite_oracle_values": true,
    "branch-3--1/category": true,
    "branch-3--1/finite_oracle_values": true,
    "branch-3-1/category": true,
    "branch-3-1/finite_oracle_values": true,
    "branch-4--1/category": true,
    "branch-4--1/finite_oracle_values": true,
    "branch-4-1/category": true,
    "branch-4-1/finite_oracle_values": true,
    "branch-5--1/category": true,
    "branch-5--1/finite_oracle_values": true,
    "branch-5-1/category": true,
    "branch-5-1/finite_oracle_values": true,
    "branch-6--1/category": true,
    "branch-6--1/finite_oracle_values": true,
    "branch-6-1/category": true,
    "branch-6-1/finite_oracle_values": true,
    "max-tie-0/category": true,
    "max-tie-0/finite_oracle_values": true,
    "max-tie-1/category": true,
    "max-tie-1/finite_oracle_values": true,
    "max-tie-2/category": true,
    "max-tie-2/finite_oracle_values": true,
    "stop-0/category": true,
    "stop-0/finite_oracle_values": true,
    "stop-0/exactK": true,
    "stop-0/trace_AD_slope": true,
    "stop-1/category": true,
    "stop-1/finite_oracle_values": true,
    "stop-1/exactK": true,
    "stop-1/trace_AD_slope": true,
    "stop-2/category": true,
    "stop-2/finite_oracle_values": true,
    "stop-2/exactK": true,
    "stop-2/trace_AD_slope": true,
    "stop-3/category": true,
    "stop-3/finite_oracle_values": true,
    "stop-3/exactK": true,
    "stop-3/trace_AD_slope": true,
    "stop-4/category": true,
    "stop-4/finite_oracle_values": true,
    "stop-4/exactK": true,
    "stop-4/trace_AD_slope": true,
    "inactive-log/category": true,
    "inactive-log/finite_oracle_values": true,
    "inactive/no_log_evaluation": true,
    "jump/0": true,
    "jump/1": true,
    "jump/2": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/kink-branch-derivatives/index.json

![Saved nonsmooth values and stopped-map samples, distinguishing undefined classical derivatives from trace derivatives.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/results/kink-branch-derivatives-preview.png)

Saved nonsmooth values and stopped-map samples, distinguishing undefined classical derivatives from trace derivatives.

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/atlas-reverse-higher-ad-2026-11-24.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- The JAX authors (n.d.). The Autodiff Cookbook [accessed 2026-11-24]. https://docs.jax.dev/en/latest/notebooks/autodiff_cookbook.html; review_level=official-documentation-selected-mathematical-sections
Selected definitions and composition formulas only. A new educational tape will implement the stated finite subset. No JAX installation, execution, timing replication or implementation-source audit. Unread: Original reverse-mode/HVP papers, JAX transformation implementation, Unselected cookbook sections. Publication year not established (n.d.).

- The JAX authors (n.d.). Frequently asked questions: undefined branches and ordering [accessed 2026-11-24]. https://docs.jax.dev/en/latest/faq.html; review_level=official-documentation-selected-sections
Read invalid inactive-branch and ordering discussions. We use an explicitly different strict nondifferentiability policy, not a universal JAX tie rule. Unread: Linked issue threads, Generalized derivative original papers. Publication year not established (n.d.).


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
