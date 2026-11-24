# Modal damping of steady multistage RK

A 16-component periodic linear field measures pseudo-time residual damping with stable, neutral and expanding controls. This is distinct from fourth-order accuracy for nonlinear physical-time problems.

These additional validation supplements are managed separately from the common 22-example registry. Receipts cover independent ZIP extraction, tests and every fixed input within each group. Changes of settings, methods or step sizes do not add independent physical problems.

## Real-space mode damping with steady multistage RK

Apply four steady residual stages on a periodic grid, separating damping, neutrality and amplification of discrete modes. The retained first run missed the original absolute residual goal in the expanding control.

**Methods used**

- [Jameson-type steady multistage Runge–Kutta](https://hrkoyama.github.io/numerical-methods-atlas/methods/jameson-steady-rk/?lang=en) (`jameson-steady-rk`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/jameson-steady-linear-modes/?lang=en#jameson-steady-linear-modes-en-algorithm)

Use the same base state in every stage and retain complete fields, stage residuals and evaluation counts.

$$
Y_j=u_n-alpha_j*dtau*(A*Y_(j-1)-b)
$$

$$
P(z)=1+z+z^2/2+z^3/6+z^4/24; lambda_4=9+2i, lambda_8=17
$$

- [Finite-dimensional linear evolution systems](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#linear-evolution-system-en) (`linear-evolution-system`)

A fixed dimensionless sixteen-node periodic linear residual; pseudo-time is an iteration parameter.

- [Finite-dimensional linear systems and factorizations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#finite-dimensional-linear-system-en) (`finite-dimensional-linear-system`)

A fixed dimensionless sixteen-node periodic linear residual; pseudo-time is an iteration parameter.


**Problem figure**

![Real-space mode damping with steady multistage RK: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/steady-rk/results/jameson-steady-linear-modes.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Real-space mode damping with steady multistage RK](https://hrkoyama.github.io/numerical-methods-atlas/problems/jameson-steady-linear-modes/?lang=en) (`jameson-steady-linear-modes`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/jameson-steady-linear-modes/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/jameson-steady-linear-modes/?lang=en#jameson-steady-linear-modes-en-validation)

Retain all 41 original numerical targets and their actual decisions. Only the expanding-control absolute residual goal is a separate study outcome; the other 40 requirements and faithful recomputation from saved arrays remain mandatory.

- [Real-space mode damping with steady multistage RK](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-jameson-steady-linear-modes-en) (`jameson-steady-linear-modes`; Same-problem reference · Analytic reference)

Limited to a fixed linear example; no JST compressible flux, nonlinear fourth-order RK or all-start convergence claim. Verification of this study does not mean that all original numerical targets were met.
### Assumptions, units and boundaries

A fixed dimensionless sixteen-node periodic linear residual; pseudo-time is an iteration parameter.

**Editorial clarification**

Limited to a fixed linear example; no JST compressible flux, nonlinear fourth-order RK or all-start convergence claim. Verification of this study does not mean that all original numerical targets were met. Axes for trajectories, states, time or iterations do not represent physical spatial dimensions.

### Adopted numerical method

Use the same base state in every stage and retain complete fields, stage residuals and evaluation counts.

$$
Y_j=u_n-alpha_j*dtau*(A*Y_(j-1)-b)
$$

$$
P(z)=1+z+z^2/2+z^3/6+z^4/24; lambda_4=9+2i, lambda_8=17
$$

### References and validation

Retain all 41 original numerical targets and their actual decisions. Only the expanding-control absolute residual goal is a separate study outcome; the other 40 requirements and faithful recomputation from saved arrays remain mandatory.

### Limits

Limited to a fixed linear example; no JST compressible flux, nonlinear fourth-order RK or all-start convergence claim. Verification of this study does not mean that all original numerical targets were met.

### Original numerical targets and unmet outcomes

Passing reproduction/reporting verification does not mean that all original accuracy goals were met. Original decisions are retained.

```json
{
  "original_target_results": {
    "reference:h32-mode4:expanded-vs-stages": true,
    "reference:h32-mode4:prior-classification": true,
    "reference:h32-mode8:expanded-vs-stages": true,
    "reference:h32-mode8:prior-classification": true,
    "reference:h16-mode4:expanded-vs-stages": true,
    "reference:h16-mode4:prior-classification": true,
    "reference:h16-mode8:expanded-vs-stages": true,
    "reference:h16-mode8:prior-classification": true,
    "reference:neutral:expanded-vs-stages": true,
    "reference:neutral:prior-classification": true,
    "reference:expanding:expanded-vs-stages": true,
    "reference:expanding:prior-classification": true,
    "reference:rational-stencil-mode4": true,
    "reference:rational-stencil-mode8": true,
    "stable-h32:finite": true,
    "stable-h32:stage-count": true,
    "stable-h32:spurious-mode": true,
    "stable-h32:true-residual-reference": true,
    "stable-h32:field-error": true,
    "stable-h32:residual-reduction": true,
    "stable-h32:nonzero-mode4": true,
    "stable-h16:finite": true,
    "stable-h16:stage-count": true,
    "stable-h16:spurious-mode": true,
    "stable-h16:true-residual-reference": true,
    "stable-h16:field-error": true,
    "stable-h16:residual-reduction": true,
    "stable-h16:nonzero-mode4": true,
    "neutral-constant:finite": true,
    "neutral-constant:stage-count": true,
    "neutral-constant:spurious-mode": true,
    "neutral-constant:true-residual-reference": true,
    "neutral-constant:neutrality": true,
    "expanding-nyquist:finite": true,
    "expanding-nyquist:stage-count": true,
    "expanding-nyquist:spurious-mode": true,
    "expanding-nyquist:true-residual-reference": false,
    "expanding-nyquist:expected-expansion": true,
    "expanding-nyquist:normalized-error": true,
    "steady-fixed-point": true,
    "four-record-identities": true
  },
  "original_target_summary": {
    "met": 40,
    "total": 41,
    "all_met": false,
    "acceptance_sha256": "af846323a4e4235d968ecb431eea825fbee40f7a1047e65b18c70b7d4a83fe00"
  }
}
```

### Stored measurements and decisions

```json
{
  "metrics": {
    "stable-h32:field-error": 3.3306690738754696e-16,
    "stable-h32:residual-reduction": 6.446370751486289e-09,
    "stable-h32:nonzero-mode4": 1.5238393618337132e-08,
    "stable-h16:field-error": 2.220446049250313e-16,
    "stable-h16:residual-reduction": 6.6210787709662455e-09,
    "stable-h16:nonzero-mode4": 1.5381125809623605e-08,
    "neutral-constant:neutrality": 0.0,
    "expanding-nyquist:expected-expansion": 1875.5948651814128,
    "expanding-nyquist:normalized-error": 3.634886991251329e-16,
    "max_field_error": 6.821210263296962e-13,
    "original_targets_met": 40,
    "original_targets_total": 41
  },
  "checks": {
    "reference:h32-mode4:expanded-vs-stages": true,
    "reference:h32-mode4:prior-classification": true,
    "reference:h32-mode8:expanded-vs-stages": true,
    "reference:h32-mode8:prior-classification": true,
    "reference:h16-mode4:expanded-vs-stages": true,
    "reference:h16-mode4:prior-classification": true,
    "reference:h16-mode8:expanded-vs-stages": true,
    "reference:h16-mode8:prior-classification": true,
    "reference:neutral:expanded-vs-stages": true,
    "reference:neutral:prior-classification": true,
    "reference:expanding:expanded-vs-stages": true,
    "reference:expanding:prior-classification": true,
    "reference:rational-stencil-mode4": true,
    "reference:rational-stencil-mode8": true,
    "stable-h32:finite": true,
    "stable-h32:stage-count": true,
    "stable-h32:spurious-mode": true,
    "stable-h32:true-residual-reference": true,
    "stable-h32:field-error": true,
    "stable-h32:residual-reduction": true,
    "stable-h32:nonzero-mode4": true,
    "stable-h16:finite": true,
    "stable-h16:stage-count": true,
    "stable-h16:spurious-mode": true,
    "stable-h16:true-residual-reference": true,
    "stable-h16:field-error": true,
    "stable-h16:residual-reduction": true,
    "stable-h16:nonzero-mode4": true,
    "neutral-constant:finite": true,
    "neutral-constant:stage-count": true,
    "neutral-constant:spurious-mode": true,
    "neutral-constant:true-residual-reference": true,
    "neutral-constant:neutrality": true,
    "expanding-nyquist:finite": true,
    "expanding-nyquist:stage-count": true,
    "expanding-nyquist:spurious-mode": true,
    "expanding-nyquist:expected-expansion": true,
    "expanding-nyquist:normalized-error": true,
    "steady-fixed-point": true,
    "four-record-identities": true,
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

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/jameson-steady-linear-modes/index.json

![Apply four steady residual stages on a periodic grid, separating damping, neutrality and amplification of discrete modes. Drawn from saved arrays. The first-run goal shortfall and each rerun’s actual target decisions remain explicit in the saved JSON.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/steady-rk/results/jameson-steady-linear-modes-preview.png)

Apply four steady residual stages on a periodic grid, separating damping, neutrality and amplification of discrete modes. Drawn from saved arrays. The first-run goal shortfall and each rerun’s actual target decisions remain explicit in the saved JSON.

![Saved residuals, constraints and budgets shown separately; symmetric log axes retain zero values. The first-run goal shortfall and each rerun’s actual target decisions remain explicit in the saved JSON.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/steady-rk/results/jameson-steady-linear-modes-diagnostics.png)

Saved residuals, constraints and budgets shown separately; symmetric log axes retain zero values. The first-run goal shortfall and each rerun’s actual target decisions remain explicit in the saved JSON.

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24/steady-rk/atlas-steady-rk-2026-11-24.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24/steady-rk/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/steady-rk/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24/steady-rk/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- PERFORM time integration schemes [accessed 2026-11-24]. https://perform.readthedocs.io/en/latest/solver/timeschemes.html; review_level=official-documentation-selected-equations
Selected four-stage base-state recurrence. No full JST 1981 paper reading or compressible-flow implementation claim.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
