# Line searches and trust regions from identical starts

Original residuals, scaled merit and complete trial ledgers separate roots, stationary nonroots and budget exhaustion.

These additional validation supplements are managed separately from the common 22-example registry. Receipts cover independent ZIP extraction, tests and every fixed input within each group. Changes of settings, methods or step sizes do not add independent physical problems.

## Line search and trust regions from the same difficult starts

Compare Newton, Armijo and dogleg from identical fixed starts, distinguishing roots from stationary nonroots and budget exhaustion.

**Methods used**

- [Armijo-damped Newton](https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=en) (`newton`)
- [Dogleg trust regions for fixed small systems](https://hrkoyama.github.io/numerical-methods-atlas/methods/dogleg-trust-region/?lang=en) (`dogleg-trust-region`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/globalization-difficult-starts/?lang=en#globalization-difficult-starts-en-algorithm)

Separate the original residual from the scaled merit and retain Euclidean dogleg and trial ledgers.

$$
phi(x)=.5||S F(x)||_2^2, g=(S J)^T S F
$$

$$
p_U=-(g^Tg)/(||S J g||_2^2)g, ||p||_2<=Delta
$$

- [Finite-dimensional nonlinear maps, roots and differential actions](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#finite-dimensional-nonlinear-map-en) (`finite-dimensional-nonlinear-map`)

Small fixed real dimensionless inputs; assumptions and scope are limited to the matching contract.

- [Bratu nonlinear boundary-value problem](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bratu-en) (`bratu`)

Small fixed real dimensionless inputs; assumptions and scope are limited to the matching contract.


**Problem figure**

![Line search and trust regions from the same difficult starts: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/results/globalization-difficult-starts.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Line search and trust regions from the same difficult starts](https://hrkoyama.github.io/numerical-methods-atlas/problems/globalization-difficult-starts/?lang=en) (`globalization-difficult-starts`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/globalization-difficult-starts/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/globalization-difficult-starts/?lang=en#globalization-difficult-starts-en-validation)

Check fixed inputs, independent references, retained candidates and every gate within the same120-second budget. Numerical success and diagnostic nonconvergence are distinct.

- [Globalization from identical starts: analytic controls and discrete Bratu corrections](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-globalization-difficult-starts-en) (`globalization-difficult-starts`; Same-problem reference · Finite-grid numerical reference)

No all-start guarantee, universal method ranking or equivalence to PETSc implementation.
### Assumptions, units and boundaries

Small fixed real dimensionless inputs; assumptions and scope are limited to the matching contract.

**Editorial clarification**

No all-start guarantee, universal method ranking or equivalence to PETSc implementation. Plot axes describe finite-dimensional variables, iterations or diagnostics, not a physical spatial dimension or PDE boundary.

### Adopted numerical method

Separate the original residual from the scaled merit and retain Euclidean dogleg and trial ledgers.

$$
phi(x)=.5||S F(x)||_2^2, g=(S J)^T S F
$$

$$
p_U=-(g^Tg)/(||S J g||_2^2)g, ||p||_2<=Delta
$$

### References and validation

Check fixed inputs, independent references, retained candidates and every gate within the same120-second budget. Numerical success and diagnostic nonconvergence are distinct.

### Limits

No all-start guarantee, universal method ranking or equivalence to PETSc implementation.

### Stored measurements and decisions

```json
{
  "metrics": {
    "max_required_unscaled_residual": 9.581336599939344e-11,
    "max_required_state_or_correction_error": 1.1079606960955801e-10,
    "max_model_ledger_defect": 1.1920928955078125e-07,
    "total_residual_evaluations": 322,
    "rejected_trials": 37
  },
  "checks": {
    "rosenbrock-unit-minus-full-newton/finite_saved_history": true,
    "rosenbrock-unit-minus-full-newton/original_residual_recomputed": true,
    "rosenbrock-unit-minus-full-newton/scaled_merit_recomputed": true,
    "rosenbrock-unit-minus-full-newton/method_step_ledger": true,
    "rosenbrock-unit-minus-full-newton/work_caps": true,
    "rosenbrock-unit-minus-full-newton/termination_category": true,
    "rosenbrock-unit-minus-armijo-newton/finite_saved_history": true,
    "rosenbrock-unit-minus-armijo-newton/original_residual_recomputed": true,
    "rosenbrock-unit-minus-armijo-newton/scaled_merit_recomputed": true,
    "rosenbrock-unit-minus-armijo-newton/method_step_ledger": true,
    "rosenbrock-unit-minus-armijo-newton/work_caps": true,
    "rosenbrock-unit-minus-armijo-newton/termination_category": true,
    "rosenbrock-unit-minus-armijo-newton/original_root_residual": true,
    "rosenbrock-unit-minus-armijo-newton/independent_state_or_correction_error": true,
    "rosenbrock-unit-minus-dogleg-trust-region/finite_saved_history": true,
    "rosenbrock-unit-minus-dogleg-trust-region/original_residual_recomputed": true,
    "rosenbrock-unit-minus-dogleg-trust-region/scaled_merit_recomputed": true,
    "rosenbrock-unit-minus-dogleg-trust-region/method_step_ledger": true,
    "rosenbrock-unit-minus-dogleg-trust-region/work_caps": true,
    "rosenbrock-unit-minus-dogleg-trust-region/termination_category": true,
    "rosenbrock-unit-minus-dogleg-trust-region/original_root_residual": true,
    "rosenbrock-unit-minus-dogleg-trust-region/independent_state_or_correction_error": true,
    "rosenbrock-unit-zero-full-newton/finite_saved_history": true,
    "rosenbrock-unit-zero-full-newton/original_residual_recomputed": true,
    "rosenbrock-unit-zero-full-newton/scaled_merit_recomputed": true,
    "rosenbrock-unit-zero-full-newton/method_step_ledger": true,
    "rosenbrock-unit-zero-full-newton/work_caps": true,
    "rosenbrock-unit-zero-full-newton/termination_category": true,
    "rosenbrock-unit-zero-armijo-newton/finite_saved_history": true,
    "rosenbrock-unit-zero-armijo-newton/original_residual_recomputed": true,
    "rosenbrock-unit-zero-armijo-newton/scaled_merit_recomputed": true,
    "rosenbrock-unit-zero-armijo-newton/method_step_ledger": true,
    "rosenbrock-unit-zero-armijo-newton/work_caps": true,
    "rosenbrock-unit-zero-armijo-newton/termination_category": true,
    "rosenbrock-unit-zero-armijo-newton/original_root_residual": true,
    "rosenbrock-unit-zero-armijo-newton/independent_state_or_correction_error": true,
    "rosenbrock-unit-zero-dogleg-trust-region/finite_saved_history": true,
    "rosenbrock-unit-zero-dogleg-trust-region/original_residual_recomputed": true,
    "rosenbrock-unit-zero-dogleg-trust-region/scaled_merit_recomputed": true,
    "rosenbrock-unit-zero-dogleg-trust-region/method_step_ledger": true,
    "rosenbrock-unit-zero-dogleg-trust-region/work_caps": true,
    "rosenbrock-unit-zero-dogleg-trust-region/termination_category": true,
    "rosenbrock-unit-zero-dogleg-trust-region/original_root_residual": true,
    "rosenbrock-unit-zero-dogleg-trust-region/independent_state_or_correction_error": true,
    "rosenbrock-left-scaled-minus-full-newton/finite_saved_history": true,
    "rosenbrock-left-scaled-minus-full-newton/original_residual_recomputed": true,
    "rosenbrock-left-scaled-minus-full-newton/scaled_merit_recomputed": true,
    "rosenbrock-left-scaled-minus-full-newton/method_step_ledger": true,
    "rosenbrock-left-scaled-minus-full-newton/work_caps": true,
    "rosenbrock-left-scaled-minus-full-newton/termination_category": true,
    "rosenbrock-left-scaled-minus-armijo-newton/finite_saved_history": true,
    "rosenbrock-left-scaled-minus-armijo-newton/original_residual_recomputed": true,
    "rosenbrock-left-scaled-minus-armijo-newton/scaled_merit_recomputed": true,
    "rosenbrock-left-scaled-minus-armijo-newton/method_step_ledger": true,
    "rosenbrock-left-scaled-minus-armijo-newton/work_caps": true,
    "rosenbrock-left-scaled-minus-armijo-newton/termination_category": true,
    "rosenbrock-left-scaled-minus-dogleg-trust-region/finite_saved_history": true,
    "rosenbrock-left-scaled-minus-dogleg-trust-region/original_residual_recomputed": true,
    "rosenbrock-left-scaled-minus-dogleg-trust-region/scaled_merit_recomputed": true,
    "rosenbrock-left-scaled-minus-dogleg-trust-region/method_step_ledger": true,
    "rosenbrock-left-scaled-minus-dogleg-trust-region/work_caps": true,
    "rosenbrock-left-scaled-minus-dogleg-trust-region/termination_category": true,
    "rosenbrock-left-scaled-zero-full-newton/finite_saved_history": true,
    "rosenbrock-left-scaled-zero-full-newton/original_residual_recomputed": true,
    "rosenbrock-left-scaled-zero-full-newton/scaled_merit_recomputed": true,
    "rosenbrock-left-scaled-zero-full-newton/method_step_ledger": true,
    "rosenbrock-left-scaled-zero-full-newton/work_caps": true,
    "rosenbrock-left-scaled-zero-full-newton/termination_category": true,
    "rosenbrock-left-scaled-zero-armijo-newton/finite_saved_history": true,
    "rosenbrock-left-scaled-zero-armijo-newton/original_residual_recomputed": true,
    "rosenbrock-left-scaled-zero-armijo-newton/scaled_merit_recomputed": true,
    "rosenbrock-left-scaled-zero-armijo-newton/method_step_ledger": true,
    "rosenbrock-left-scaled-zero-armijo-newton/work_caps": true,
    "rosenbrock-left-scaled-zero-armijo-newton/termination_category": true,
    "rosenbrock-left-scaled-zero-dogleg-trust-region/finite_saved_history": true,
    "rosenbrock-left-scaled-zero-dogleg-trust-region/original_residual_recomputed": true,
    "rosenbrock-left-scaled-zero-dogleg-trust-region/scaled_merit_recomputed": true,
    "rosenbrock-left-scaled-zero-dogleg-trust-region/method_step_ledger": true,
    "rosenbrock-left-scaled-zero-dogleg-trust-region/work_caps": true,
    "rosenbrock-left-scaled-zero-dogleg-trust-region/termination_category": true,
    "bratu-amp0-full-newton/finite_saved_history": true,
    "bratu-amp0-full-newton/original_residual_recomputed": true,
    "bratu-amp0-full-newton/scaled_merit_recomputed": true,
    "bratu-amp0-full-newton/method_step_ledger": true,
    "bratu-amp0-full-newton/work_caps": true,
    "bratu-amp0-full-newton/termination_category": true,
    "bratu-amp0-armijo-newton/finite_saved_history": true,
    "bratu-amp0-armijo-newton/original_residual_recomputed": true,
    "bratu-amp0-armijo-newton/scaled_merit_recomputed": true,
    "bratu-amp0-armijo-newton/method_step_ledger": true,
    "bratu-amp0-armijo-newton/work_caps": true,
    "bratu-amp0-armijo-newton/termination_category": true,
    "bratu-amp0-armijo-newton/original_root_residual": true,
    "bratu-amp0-armijo-newton/independent_state_or_correction_error": true,
    "bratu-amp0-dogleg-trust-region/finite_saved_history": true,
    "bratu-amp0-dogleg-trust-region/original_residual_recomputed": true,
    "bratu-amp0-dogleg-trust-region/scaled_merit_recomputed": true,
    "bratu-amp0-dogleg-trust-region/method_step_ledger": true,
    "bratu-amp0-dogleg-trust-region/work_caps": true,
    "bratu-amp0-dogleg-trust-region/termination_category": true,
    "bratu-amp0-dogleg-trust-region/original_root_residual": true,
    "bratu-amp0-dogleg-trust-region/independent_state_or_correction_error": true,
    "bratu-amp4-full-newton/finite_saved_history": true,
    "bratu-amp4-full-newton/original_residual_recomputed": true,
    "bratu-amp4-full-newton/scaled_merit_recomputed": true,
    "bratu-amp4-full-newton/method_step_ledger": true,
    "bratu-amp4-full-newton/work_caps": true,
    "bratu-amp4-full-newton/termination_category": true,
    "bratu-amp4-armijo-newton/finite_saved_history": true,
    "bratu-amp4-armijo-newton/original_residual_recomputed": true,
    "bratu-amp4-armijo-newton/scaled_merit_recomputed": true,
    "bratu-amp4-armijo-newton/method_step_ledger": true,
    "bratu-amp4-armijo-newton/work_caps": true,
    "bratu-amp4-armijo-newton/termination_category": true,
    "bratu-amp4-dogleg-trust-region/finite_saved_history": true,
    "bratu-amp4-dogleg-trust-region/original_residual_recomputed": true,
    "bratu-amp4-dogleg-trust-region/scaled_merit_recomputed": true,
    "bratu-amp4-dogleg-trust-region/method_step_ledger": true,
    "bratu-amp4-dogleg-trust-region/work_caps": true,
    "bratu-amp4-dogleg-trust-region/termination_category": true,
    "bratu-amp8-full-newton/finite_saved_history": true,
    "bratu-amp8-full-newton/original_residual_recomputed": true,
    "bratu-amp8-full-newton/scaled_merit_recomputed": true,
    "bratu-amp8-full-newton/method_step_ledger": true,
    "bratu-amp8-full-newton/work_caps": true,
    "bratu-amp8-full-newton/termination_category": true,
    "bratu-amp8-armijo-newton/finite_saved_history": true,
    "bratu-amp8-armijo-newton/original_residual_recomputed": true,
    "bratu-amp8-armijo-newton/scaled_merit_recomputed": true,
    "bratu-amp8-armijo-newton/method_step_ledger": true,
    "bratu-amp8-armijo-newton/work_caps": true,
    "bratu-amp8-armijo-newton/termination_category": true,
    "bratu-amp8-dogleg-trust-region/finite_saved_history": true,
    "bratu-amp8-dogleg-trust-region/original_residual_recomputed": true,
    "bratu-amp8-dogleg-trust-region/scaled_merit_recomputed": true,
    "bratu-amp8-dogleg-trust-region/method_step_ledger": true,
    "bratu-amp8-dogleg-trust-region/work_caps": true,
    "bratu-amp8-dogleg-trust-region/termination_category": true,
    "stationary-armijo-newton/stationary_nonroot_status": true,
    "stationary-armijo-newton/not_false_root": true,
    "stationary-dogleg-trust-region/stationary_nonroot_status": true,
    "stationary-dogleg-trust-region/not_false_root": true,
    "domain/rejected_before_exp_evaluation": true,
    "domain/finite_candidate_retained": true,
    "exact24_main_records": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/globalization-difficult-starts/index.json

![Saved paths from identical starts, original residuals, trust radii and measured evaluation counts. Failures and nonconvergence remain explicit.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/results/globalization-difficult-starts-preview.png)

Saved paths from identical starts, original residuals, trust radii and measured evaluation counts. Failures and nonconvergence remain explicit.

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/atlas-globalization-controls-2026-11-24.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- PETSc developers (n.d.). SNES: Nonlinear Solvers [accessed 2026-11-24]. https://petsc.org/release/manual/snes/; review_level=official-documentation-selected-sections
Read nonlinear solver categories, stopping/domain-error distinctions and selected line-search/trust-region descriptions. Our fixed Euclidean dogleg and Delta0=1 are independently specified; not asserted to reproduce PETSc defaults. Unread: MINPACK original report/paper, PETSc solver implementation source, Full manual outside named sections. Publication year not established (n.d.).


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
