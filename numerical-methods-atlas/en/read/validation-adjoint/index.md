# Adjoints through time steps, folds and distributed coefficients

Compare tangents and adjoints of discrete maps, separating reference accuracy, requested residuals, owned buffers and recomputation.

These additional validation supplements are managed separately from the common 22-example registry. Receipts cover independent ZIP extraction, tests and every fixed input within each group. Changes of settings, methods or step sizes do not add independent physical problems.

## Discrete diffusion adjoint and checkpoint replay

Reverse the actual backward-Euler map and compare tangent derivatives, independent high-precision modes and block replay.

**Methods used**

- [Implicit differentiation and adjoint methods](https://hrkoyama.github.io/numerical-methods-atlas/methods/adjoint/?lang=en) (`adjoint`)
- [Backward Euler](https://hrkoyama.github.io/numerical-methods-atlas/methods/backward-euler/?lang=en) (`backward-euler`)
- [Thomas tridiagonal elimination](https://hrkoyama.github.io/numerical-methods-atlas/methods/thomas/?lang=en) (`thomas`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/diffusion-discrete-adjoint/?lang=en#diffusion-discrete-adjoint-en-algorithm)

Thomas solves B u_next=u_current+dt theta b; reverse solves use B transpose. Save checkpoints every16steps and replay one block in the original order. Serialize and release the full trajectory before the separate checkpoint ownership window.

$$
B=I+\Delta t\,\kappa A_h,\quad Bu_{k+1}=u_k+\Delta t\,\theta b
$$

$$
p_N=h(u_N-d),\quad z_k=B^{-T}p_{k+1},\quad p_k=z_k
$$

$$
J_\kappa=0.01\kappa-\Delta t\sum_k z_k^TA_hu_{k+1},\quad J_\theta=0.02\theta+\Delta t\sum_kz_k^Tb
$$

- [Heat / diffusion equation](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#heat-en) (`heat`)

Dimensionless x in [0,1], fixed zero Dirichlet endpoints, 7/15 interior nodes and 64/128/256 time steps to T=.1; kappa=.1 and theta=.2. Coordinate transposes include explicit objective h weights.


**Problem figure**

![Discrete diffusion adjoint and checkpoint replay: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/results/diffusion-discrete-adjoint.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Discrete diffusion adjoint and checkpoint replay](https://hrkoyama.github.io/numerical-methods-atlas/problems/diffusion-discrete-adjoint/?lang=en) (`diffusion-discrete-adjoint`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/diffusion-discrete-adjoint/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/diffusion-discrete-adjoint/?lang=en#diffusion-discrete-adjoint-en-validation)

Pre-run freeze:independent67-check reference qualification, then shared32pytest and141fixed group gates. Retain all inputs, tolerances and failures. Actual outcomes are recorded in the bundled result/verification. Initial attempt retained32passing tests and59diffusion/45fold gates before an unmet inner target. R2 general Jv association has separate96component checks; this does not imply primary success. R2 primary failure is also retained. R3 state-onlyhi+lo has separate20component checks;actual three-caseoutcomes are inresult/verification.

- [Backward-Euler discrete modes and time-exact semidiscrete diffusion references](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-diffusion-discrete-adjoint-en) (`diffusion-discrete-adjoint`; Same-problem reference · Analytic reference)

Fixed-step discrete adjoints, not CVODES or an optimal checkpoint schedule. The40n limit counts unique evolving state/adjoint/RHS/solve-scratch elements. Static factors/model arrays are separately listed and included in total bytes. Validation/NPZ assembly follows the ownership windows; this is not RSS.
### Assumptions, units and boundaries

Dimensionless x in [0,1], fixed zero Dirichlet endpoints, 7/15 interior nodes and 64/128/256 time steps to T=.1; kappa=.1 and theta=.2. Coordinate transposes include explicit objective h weights.

**Editorial clarification**

Fixed-step discrete adjoints, not CVODES or an optimal checkpoint schedule. The40n limit counts unique evolving state/adjoint/RHS/solve-scratch elements. Static factors/model arrays are separately listed and included in total bytes. Validation/NPZ assembly follows the ownership windows; this is not RSS.

### Adopted numerical method

Thomas solves B u_next=u_current+dt theta b; reverse solves use B transpose. Save checkpoints every16steps and replay one block in the original order. Serialize and release the full trajectory before the separate checkpoint ownership window.

$$
B=I+\Delta t\,\kappa A_h,\quad Bu_{k+1}=u_k+\Delta t\,\theta b
$$

$$
p_N=h(u_N-d),\quad z_k=B^{-T}p_{k+1},\quad p_k=z_k
$$

$$
J_\kappa=0.01\kappa-\Delta t\sum_k z_k^TA_hu_{k+1},\quad J_\theta=0.02\theta+\Delta t\sum_kz_k^Tb
$$

### References and validation

Pre-run freeze:independent67-check reference qualification, then shared32pytest and141fixed group gates. Retain all inputs, tolerances and failures. Actual outcomes are recorded in the bundled result/verification. Initial attempt retained32passing tests and59diffusion/45fold gates before an unmet inner target. R2 general Jv association has separate96component checks; this does not imply primary success. R2 primary failure is also retained. R3 state-onlyhi+lo has separate20component checks;actual three-caseoutcomes are inresult/verification.

### Limits

Fixed-step discrete adjoints, not CVODES or an optimal checkpoint schedule. The40n limit counts unique evolving state/adjoint/RHS/solve-scratch elements. Static factors/model arrays are separately listed and included in total bytes. Validation/NPZ assembly follows the ownership windows; this is not RSS.

### Stored measurements and decisions

```json
{
  "metrics": {
    "time_ratios": [
      {
        "n": 7,
        "coarse": 64,
        "fine": 128,
        "ratio": 0.5007714700172587,
        "denominator": 0.00011295826203078933
      },
      {
        "n": 7,
        "coarse": 128,
        "fine": 256,
        "ratio": 0.5003862639676856,
        "denominator": 5.6566274927753076e-05
      },
      {
        "n": 15,
        "coarse": 64,
        "fine": 128,
        "ratio": 0.500801018633583,
        "denominator": 0.00011971557684064543
      },
      {
        "n": 15,
        "coarse": 128,
        "fine": 256,
        "ratio": 0.500401075710245,
        "denominator": 5.99536828281022e-05
      }
    ],
    "principal_records": 6,
    "FD_forward_evolutions": 18,
    "ownership_scope": "Unique explicit scientific arrays; validation loaded after the separate ownership windows; serialization internals are not process RSS."
  },
  "checks": {
    "n7-N64-finite-boundary": true,
    "n7-N64-state-modal": true,
    "n7-N64-adjoint-modal": true,
    "n7-N64-tangent-modal": true,
    "n7-N64-adjoint-tangent": true,
    "n7-N64-replay-state": true,
    "n7-N64-replay-gradient": true,
    "n7-N64-exact-work": true,
    "n7-N128-finite-boundary": true,
    "n7-N128-state-modal": true,
    "n7-N128-adjoint-modal": true,
    "n7-N128-tangent-modal": true,
    "n7-N128-adjoint-tangent": true,
    "n7-N128-replay-state": true,
    "n7-N128-replay-gradient": true,
    "n7-N128-exact-work": true,
    "n7-N256-finite-boundary": true,
    "n7-N256-state-modal": true,
    "n7-N256-adjoint-modal": true,
    "n7-N256-tangent-modal": true,
    "n7-N256-adjoint-tangent": true,
    "n7-N256-replay-state": true,
    "n7-N256-replay-gradient": true,
    "n7-N256-exact-work": true,
    "n7-time-ratio-64-128": true,
    "n7-time-ratio-128-256": true,
    "n7-N256-storage": true,
    "n15-N64-finite-boundary": true,
    "n15-N64-state-modal": true,
    "n15-N64-adjoint-modal": true,
    "n15-N64-tangent-modal": true,
    "n15-N64-adjoint-tangent": true,
    "n15-N64-replay-state": true,
    "n15-N64-replay-gradient": true,
    "n15-N64-exact-work": true,
    "n15-N128-finite-boundary": true,
    "n15-N128-state-modal": true,
    "n15-N128-adjoint-modal": true,
    "n15-N128-tangent-modal": true,
    "n15-N128-adjoint-tangent": true,
    "n15-N128-replay-state": true,
    "n15-N128-replay-gradient": true,
    "n15-N128-exact-work": true,
    "n15-N256-finite-boundary": true,
    "n15-N256-state-modal": true,
    "n15-N256-adjoint-modal": true,
    "n15-N256-tangent-modal": true,
    "n15-N256-adjoint-tangent": true,
    "n15-N256-replay-state": true,
    "n15-N256-replay-gradient": true,
    "n15-N256-exact-work": true,
    "n15-time-ratio-64-128": true,
    "n15-time-ratio-128-256": true,
    "n15-N256-storage": true,
    "FD-direction0": true,
    "FD-direction1": true,
    "FD-direction2": true,
    "FD-all-finite": true,
    "qualified-cache": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/diffusion-discrete-adjoint/index.json

![Discrete diffusion adjoint and checkpoint replay. Preview from actual saved numerical data for a one-dimensional problem.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/results/diffusion-discrete-adjoint-preview.png)

Discrete diffusion adjoint and checkpoint replay. Preview from actual saved numerical data for a one-dimensional problem.

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/atlas-adjoint-2026-11-24.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- SUNDIALS CVODES adjoint usage [accessed 2026-11-24]. https://sundials.readthedocs.io/en/latest/cvodes/Usage/ADJ.html; review_level=official-documentation-selected-sections
Selected scope only. Access date is not publication year. Numerical oracle qualification is recorded separately.

- JAX vjp API [accessed 2026-11-24]. https://docs.jax.dev/en/latest/_autosummary/jax.vjp.html; review_level=official-documentation-selected-API
Selected scope only. Access date is not publication year. Numerical oracle qualification is recorded separately.

- Python3.12.16 decimal documentation [accessed 2026-11-24]. https://docs.python.org/3.12/library/decimal.html; review_level=official-documentation-selected-API
Selected scope only. Access date is not publication year. Numerical oracle qualification is recorded separately.

- Dickson,Kelley,Ipsen,Kevrekidis:Condition Estimates for Pseudo-Arclength Continuation [accessed 2026-11-24]. https://ipsen.math.ncsu.edu/ps/sinum65438.pdf; review_level=author-paper-selected-equations
Selected scope only. Access date is not publication year. Numerical oracle qualification is recorded separately.

- Author-hosted INF5620 nonlinear exercises,Problem8,Eq52 [accessed 2026-11-24]. https://hplgit.github.io/INF5620/doc/pub/._main_nonlin005.html; review_level=author-teaching-source-selected-equation
Selected scope only. Access date is not publication year. Numerical oracle qualification is recorded separately.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## Bratu sensitivity near the discrete fold

At six fixed points approaching the discrete Bratu fold, separate state error from linear-solve tolerance and compare against independent shooting gradients.

**Methods used**

- [Implicit differentiation and adjoint methods](https://hrkoyama.github.io/numerical-methods-atlas/methods/adjoint/?lang=en) (`adjoint`)
- [Restarted GMRES](https://hrkoyama.github.io/numerical-methods-atlas/methods/gmres/?lang=en) (`gmres`)
- [Centered spatial difference](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en) (`centered-difference`)
- [Armijo-damped Newton](https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=en) (`newton`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-sensitivity/?lang=en#bratu-fold-sensitivity-en-algorithm)

Analytic Jv, Poisson-Thomas right preconditioning and the preserved GMRES body solve tangents/adjoints. Save every rtol, returned candidate, true residual, termination and roundoff scale. Qualify the discrete oracle through shooting and separate high-precision Thomas-Newton. R2 uses a general near-neighbor-difference association in binary64 Jv; the original nonlinear residual,GMRES and tolerances are unchanged. R3 expands only stateNewtoncorrections ashi+lo,direct9productresidual and3productstateupdate. Physicalstates stayfloat64;derivative/adjointGMRES staysordinary.

$$
G(u,\lambda)=A_hu-\lambda e^u=0,\quad Js=e^u,\quad J^Tp=hu
$$

$$
\mathcal J=\tfrac12h\sum_i u_i^2+0.025\lambda^2,\quad \mathcal J_\lambda=0.05\lambda+p^Te^u
$$

$$
q^T(s_D-\hat s)-p_D^Tr=-p_D^Tr_D+r_{p,D}^T(s_D-\hat s)
$$

- [Bratu nonlinear boundary-value problem](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bratu-en) (`bratu`)

31/63 interior nodes; gaps .1/.01/.001 below the discrete-fold anchor. Every state starts at zero on the lower branch. Parse each lambda string once to binary float; the Decimal oracle evaluates exactly that float.


**Problem figure**

![Bratu sensitivity near the discrete fold: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/results/bratu-fold-sensitivity.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Bratu sensitivity near the discrete fold](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-sensitivity/?lang=en) (`bratu-fold-sensitivity`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-sensitivity/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-sensitivity/?lang=en#bratu-fold-sensitivity-en-validation)

Pre-run freeze:independent67-check reference qualification, then shared32pytest and141fixed group gates. Retain all inputs, tolerances and failures. Actual outcomes are recorded in the bundled result/verification. Initial attempt retained32passing tests and59diffusion/45fold gates before an unmet inner target. R2 general Jv association has separate96component checks; this does not imply primary success. R2 primary failure is also retained. R3 state-onlyhi+lo has separate20component checks;actual three-caseoutcomes are inresult/verification. Fullownership evidence is in the JSONL file/byteoffset/recordSHA referenced by each linear_memory summary;only compact summaries enter case metrics.

- [Discrete Bratu shooting, tangent and adjoint references near a fold](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-bratu-fold-sensitivity-en) (`bratu-fold-sensitivity`; Same-problem reference · Finite-grid numerical reference)

The continuum fold is not the discrete fold. rtol1e-4/1e-8 targets are required; requested1e-12 is observational and unmet is never called converged. Independent accuracy of the returned gradient is a separate gate. Eigenvalue/roundoff scales are floating diagnostics, not certified intervals. Bratu J is symmetric; the nonsymmetric transpose is a separate operator control. The retained /solver/gmres/retention_adaptation text is historicalR1/R2;the newcontract explicitly overrides it for mixed-precisionSTATEsolves. ProjectedUNMET is separatelysaved.
### Assumptions, units and boundaries

31/63 interior nodes; gaps .1/.01/.001 below the discrete-fold anchor. Every state starts at zero on the lower branch. Parse each lambda string once to binary float; the Decimal oracle evaluates exactly that float.

**Editorial clarification**

The continuum fold is not the discrete fold. rtol1e-4/1e-8 targets are required; requested1e-12 is observational and unmet is never called converged. Independent accuracy of the returned gradient is a separate gate. Eigenvalue/roundoff scales are floating diagnostics, not certified intervals. Bratu J is symmetric; the nonsymmetric transpose is a separate operator control. The retained /solver/gmres/retention_adaptation text is historicalR1/R2;the newcontract explicitly overrides it for mixed-precisionSTATEsolves. ProjectedUNMET is separatelysaved.

### Adopted numerical method

Analytic Jv, Poisson-Thomas right preconditioning and the preserved GMRES body solve tangents/adjoints. Save every rtol, returned candidate, true residual, termination and roundoff scale. Qualify the discrete oracle through shooting and separate high-precision Thomas-Newton. R2 uses a general near-neighbor-difference association in binary64 Jv; the original nonlinear residual,GMRES and tolerances are unchanged. R3 expands only stateNewtoncorrections ashi+lo,direct9productresidual and3productstateupdate. Physicalstates stayfloat64;derivative/adjointGMRES staysordinary.

$$
G(u,\lambda)=A_hu-\lambda e^u=0,\quad Js=e^u,\quad J^Tp=hu
$$

$$
\mathcal J=\tfrac12h\sum_i u_i^2+0.025\lambda^2,\quad \mathcal J_\lambda=0.05\lambda+p^Te^u
$$

$$
q^T(s_D-\hat s)-p_D^Tr=-p_D^Tr_D+r_{p,D}^T(s_D-\hat s)
$$

### References and validation

Pre-run freeze:independent67-check reference qualification, then shared32pytest and141fixed group gates. Retain all inputs, tolerances and failures. Actual outcomes are recorded in the bundled result/verification. Initial attempt retained32passing tests and59diffusion/45fold gates before an unmet inner target. R2 general Jv association has separate96component checks; this does not imply primary success. R2 primary failure is also retained. R3 state-onlyhi+lo has separate20component checks;actual three-caseoutcomes are inresult/verification. Fullownership evidence is in the JSONL file/byteoffset/recordSHA referenced by each linear_memory summary;only compact summaries enter case metrics.

### Limits

The continuum fold is not the discrete fold. rtol1e-4/1e-8 targets are required; requested1e-12 is observational and unmet is never called converged. Independent accuracy of the returned gradient is a separate gate. Eigenvalue/roundoff scales are floating diagnostics, not certified intervals. Bratu J is symmetric; the nonsymmetric transpose is a separate operator control. The retained /solver/gmres/retention_adaptation text is historicalR1/R2;the newcontract explicitly overrides it for mixed-precisionSTATEsolves. ProjectedUNMET is separatelysaved.

### Stored measurements and decisions

```json
{
  "metrics": {
    "principal_records": 6,
    "FD_state_solves": 36,
    "tight_target_policy": "1e-12 observational; exact returned candidate retained. Passing case does not imply target attained."
  },
  "checks": {
    "n31-point0-finite-state-branches": true,
    "n31-point0-strict-state-reference": true,
    "n31-point0-state-residuals": true,
    "n31-point0-below-discrete-fold": true,
    "n31-point0-strict-gradient-reference": true,
    "n31-point0-direct-duality": true,
    "n31-point0-GMRES-fixed-targets": true,
    "n31-point0-residual-identities": true,
    "n31-point0-FD-complete": true,
    "n31-point1-finite-state-branches": true,
    "n31-point1-strict-state-reference": true,
    "n31-point1-state-residuals": true,
    "n31-point1-below-discrete-fold": true,
    "n31-point1-strict-gradient-reference": true,
    "n31-point1-direct-duality": true,
    "n31-point1-GMRES-fixed-targets": true,
    "n31-point1-residual-identities": true,
    "n31-point1-FD-complete": true,
    "n31-point2-finite-state-branches": true,
    "n31-point2-strict-state-reference": true,
    "n31-point2-state-residuals": true,
    "n31-point2-below-discrete-fold": true,
    "n31-point2-strict-gradient-reference": true,
    "n31-point2-direct-duality": true,
    "n31-point2-GMRES-fixed-targets": true,
    "n31-point2-residual-identities": true,
    "n31-point2-FD-complete": true,
    "n63-point0-finite-state-branches": true,
    "n63-point0-strict-state-reference": true,
    "n63-point0-state-residuals": true,
    "n63-point0-below-discrete-fold": true,
    "n63-point0-strict-gradient-reference": true,
    "n63-point0-direct-duality": true,
    "n63-point0-GMRES-fixed-targets": true,
    "n63-point0-residual-identities": true,
    "n63-point0-FD-complete": true,
    "n63-point1-finite-state-branches": true,
    "n63-point1-strict-state-reference": true,
    "n63-point1-state-residuals": true,
    "n63-point1-below-discrete-fold": true,
    "n63-point1-strict-gradient-reference": true,
    "n63-point1-direct-duality": true,
    "n63-point1-GMRES-fixed-targets": true,
    "n63-point1-residual-identities": true,
    "n63-point1-FD-complete": true,
    "n63-point2-finite-state-branches": true,
    "n63-point2-strict-state-reference": true,
    "n63-point2-state-residuals": true,
    "n63-point2-below-discrete-fold": true,
    "n63-point2-strict-gradient-reference": true,
    "n63-point2-direct-duality": true,
    "n63-point2-GMRES-fixed-targets": true,
    "n63-point2-residual-identities": true,
    "n63-point2-FD-complete": true,
    "qualified-cache": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-sensitivity/index.json

![Bratu sensitivity near the discrete fold. Preview from actual saved numerical data for a one-dimensional problem.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/results/bratu-fold-sensitivity-preview.png)

Bratu sensitivity near the discrete fold. Preview from actual saved numerical data for a one-dimensional problem.

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/atlas-adjoint-2026-11-24.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- SUNDIALS CVODES adjoint usage [accessed 2026-11-24]. https://sundials.readthedocs.io/en/latest/cvodes/Usage/ADJ.html; review_level=official-documentation-selected-sections
Selected scope only. Access date is not publication year. Numerical oracle qualification is recorded separately.

- JAX vjp API [accessed 2026-11-24]. https://docs.jax.dev/en/latest/_autosummary/jax.vjp.html; review_level=official-documentation-selected-API
Selected scope only. Access date is not publication year. Numerical oracle qualification is recorded separately.

- Python3.12.16 decimal documentation [accessed 2026-11-24]. https://docs.python.org/3.12/library/decimal.html; review_level=official-documentation-selected-API
Selected scope only. Access date is not publication year. Numerical oracle qualification is recorded separately.

- Dickson,Kelley,Ipsen,Kevrekidis:Condition Estimates for Pseudo-Arclength Continuation [accessed 2026-11-24]. https://ipsen.math.ncsu.edu/ps/sinum65438.pdf; review_level=author-paper-selected-equations
Selected scope only. Access date is not publication year. Numerical oracle qualification is recorded separately.

- Author-hosted INF5620 nonlinear exercises,Problem8,Eq52 [accessed 2026-11-24]. https://hplgit.github.io/INF5620/doc/pub/._main_nonlin005.html; review_level=author-teaching-source-selected-equation
Selected scope only. Access date is not publication year. Numerical oracle qualification is recorded separately.

- Python3.12.16 math documentation,math.sumprod [accessed 2026-11-24]. https://docs.python.org/3.12/library/math.html#math.sumprod; review_level=official-selected-API
Selectedofficial math.sumprod API read;accessdate is notpublicationyear,no globalcorrectrounding claim.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## Matrix-free VJP for distributed Bratu coefficients

Represent8/16/32 spatial controls with two local hat weights per node; compare objective-wise adjoint VJPs with a separate full-sensitivity reference.

**Methods used**

- [Implicit differentiation and adjoint methods](https://hrkoyama.github.io/numerical-methods-atlas/methods/adjoint/?lang=en) (`adjoint`)
- [Restarted GMRES](https://hrkoyama.github.io/numerical-methods-atlas/methods/gmres/?lang=en) (`gmres`)
- [Centered spatial difference](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en) (`centered-difference`)
- [Armijo-damped Newton](https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=en) (`newton`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-distributed-vjp/?lang=en#bratu-distributed-vjp-en-algorithm)

Bv uses local gather and B transpose scatter-add. Primary solves use Jv without an n-by-m matrix. One shared Poisson factor serves the one/three-objective runs on the same state. Dense hats and m tangent RHS are allowed only in the separate reference window. R2 uses a general near-neighbor-difference association in binary64 Jv; the original nonlinear residual,GMRES and tolerances are unchanged. R3 expands only stateNewtoncorrections ashi+lo,direct9productresidual and3productstateupdate. Physicalstates stayfloat64;derivative/adjointGMRES staysordinary.

$$
G=A_hu-(2+B\theta)e^u,\quad J^Tp=q,\quad \nabla_\theta\mathcal J=B^T(e^u\odot p)
$$

$$
a_{\rm endpoints}=[a-b,a+b],\quad\theta_{\rm endpoints}=[a-b-2,a+b-2]
$$

- [Bratu nonlinear boundary-value problem](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bratu-en) (`bratu`)

63 interior nodes; a(x)=2+B theta with theta=.2sin(2pi xi)+.1cos(pi xi). State/sensitivity have fixed zero Dirichlet endpoints; endpoint coefficient controls are not fixed zero.


**Problem figure**

![Matrix-free VJP for distributed Bratu coefficients: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/results/bratu-distributed-vjp.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Matrix-free VJP for distributed Bratu coefficients](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-distributed-vjp/?lang=en) (`bratu-distributed-vjp`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-distributed-vjp/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-distributed-vjp/?lang=en#bratu-distributed-vjp-en-validation)

Pre-run freeze:independent67-check reference qualification, then shared32pytest and141fixed group gates. Retain all inputs, tolerances and failures. Actual outcomes are recorded in the bundled result/verification. Initial attempt retained32passing tests and59diffusion/45fold gates before an unmet inner target. R2 general Jv association has separate96component checks; this does not imply primary success. R2 primary failure is also retained. R3 state-onlyhi+lo has separate20component checks;actual three-caseoutcomes are inresult/verification. Fullownership evidence is in the JSONL file/byteoffset/recordSHA referenced by each linear_memory summary;only compact summaries enter case metrics.

- [Independent dense sensitivities and matrix-free VJPs for distributed Bratu coefficients](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-bratu-distributed-vjp-en) (`bratu-distributed-vjp`; Same-problem reference · Finite-grid numerical reference)

Derivative verification at the same discrete state, not independent physical-PDE truth or general AD. Persistent arrays and fixed Krylov workspace inventories are not RSS measurements. For m=2, theta endpoints are[a-b-2,a+b-2], distinct from physical coefficient endpoints[a-b,a+b]. The retained /solver/gmres/retention_adaptation text is historicalR1/R2;the newcontract explicitly overrides it for mixed-precisionSTATEsolves. ProjectedUNMET is separatelysaved.
### Assumptions, units and boundaries

63 interior nodes; a(x)=2+B theta with theta=.2sin(2pi xi)+.1cos(pi xi). State/sensitivity have fixed zero Dirichlet endpoints; endpoint coefficient controls are not fixed zero.

**Editorial clarification**

Derivative verification at the same discrete state, not independent physical-PDE truth or general AD. Persistent arrays and fixed Krylov workspace inventories are not RSS measurements. For m=2, theta endpoints are[a-b-2,a+b-2], distinct from physical coefficient endpoints[a-b,a+b]. The retained /solver/gmres/retention_adaptation text is historicalR1/R2;the newcontract explicitly overrides it for mixed-precisionSTATEsolves. ProjectedUNMET is separatelysaved.

### Adopted numerical method

Bv uses local gather and B transpose scatter-add. Primary solves use Jv without an n-by-m matrix. One shared Poisson factor serves the one/three-objective runs on the same state. Dense hats and m tangent RHS are allowed only in the separate reference window. R2 uses a general near-neighbor-difference association in binary64 Jv; the original nonlinear residual,GMRES and tolerances are unchanged. R3 expands only stateNewtoncorrections ashi+lo,direct9productresidual and3productstateupdate. Physicalstates stayfloat64;derivative/adjointGMRES staysordinary.

$$
G=A_hu-(2+B\theta)e^u,\quad J^Tp=q,\quad \nabla_\theta\mathcal J=B^T(e^u\odot p)
$$

$$
a_{\rm endpoints}=[a-b,a+b],\quad\theta_{\rm endpoints}=[a-b-2,a+b-2]
$$

### References and validation

Pre-run freeze:independent67-check reference qualification, then shared32pytest and141fixed group gates. Retain all inputs, tolerances and failures. Actual outcomes are recorded in the bundled result/verification. Initial attempt retained32passing tests and59diffusion/45fold gates before an unmet inner target. R2 general Jv association has separate96component checks; this does not imply primary success. R2 primary failure is also retained. R3 state-onlyhi+lo has separate20component checks;actual three-caseoutcomes are inresult/verification. Fullownership evidence is in the JSONL file/byteoffset/recordSHA referenced by each linear_memory summary;only compact summaries enter case metrics.

### Limits

Derivative verification at the same discrete state, not independent physical-PDE truth or general AD. Persistent arrays and fixed Krylov workspace inventories are not RSS measurements. For m=2, theta endpoints are[a-b-2,a+b-2], distinct from physical coefficient endpoints[a-b,a+b]. The retained /solver/gmres/retention_adaptation text is historicalR1/R2;the newcontract explicitly overrides it for mixed-precisionSTATEsolves. ProjectedUNMET is separatelysaved.

### Stored measurements and decisions

```json
{
  "metrics": {
    "principal_records": 3,
    "FD_state_solves": 18,
    "affine_error": 4.440892098500626e-16,
    "wrong_offset_error": 2.0000000000000004,
    "primary_scope": "Persistent named-array inventory and declared fixed Krylov workspace; not an RSS/peak-allocation measurement."
  },
  "checks": {
    "m8-state-residual": true,
    "m8-coefficient": true,
    "m8-duality": true,
    "m8-VJP-dense-reference": true,
    "m8-FD-finest": true,
    "m8-objective-count": true,
    "m8-allocation": true,
    "m8-finite-boundary": true,
    "m16-state-residual": true,
    "m16-coefficient": true,
    "m16-duality": true,
    "m16-VJP-dense-reference": true,
    "m16-FD-finest": true,
    "m16-objective-count": true,
    "m16-allocation": true,
    "m16-finite-boundary": true,
    "m32-state-residual": true,
    "m32-coefficient": true,
    "m32-duality": true,
    "m32-VJP-dense-reference": true,
    "m32-FD-finest": true,
    "m32-objective-count": true,
    "m32-allocation": true,
    "m32-finite-boundary": true,
    "nonsymmetric-transpose": true,
    "affine-offset": true,
    "qualified-cache": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-distributed-vjp/index.json

![Matrix-free VJP for distributed Bratu coefficients. Preview from actual saved numerical data for a one-dimensional problem.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/results/bratu-distributed-vjp-preview.png)

Matrix-free VJP for distributed Bratu coefficients. Preview from actual saved numerical data for a one-dimensional problem.

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/atlas-adjoint-2026-11-24.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- SUNDIALS CVODES adjoint usage [accessed 2026-11-24]. https://sundials.readthedocs.io/en/latest/cvodes/Usage/ADJ.html; review_level=official-documentation-selected-sections
Selected scope only. Access date is not publication year. Numerical oracle qualification is recorded separately.

- JAX vjp API [accessed 2026-11-24]. https://docs.jax.dev/en/latest/_autosummary/jax.vjp.html; review_level=official-documentation-selected-API
Selected scope only. Access date is not publication year. Numerical oracle qualification is recorded separately.

- Python3.12.16 decimal documentation [accessed 2026-11-24]. https://docs.python.org/3.12/library/decimal.html; review_level=official-documentation-selected-API
Selected scope only. Access date is not publication year. Numerical oracle qualification is recorded separately.

- Dickson,Kelley,Ipsen,Kevrekidis:Condition Estimates for Pseudo-Arclength Continuation [accessed 2026-11-24]. https://ipsen.math.ncsu.edu/ps/sinum65438.pdf; review_level=author-paper-selected-equations
Selected scope only. Access date is not publication year. Numerical oracle qualification is recorded separately.

- Author-hosted INF5620 nonlinear exercises,Problem8,Eq52 [accessed 2026-11-24]. https://hplgit.github.io/INF5620/doc/pub/._main_nonlin005.html; review_level=author-teaching-source-selected-equation
Selected scope only. Access date is not publication year. Numerical oracle qualification is recorded separately.

- Python3.12.16 math documentation,math.sumprod [accessed 2026-11-24]. https://docs.python.org/3.12/library/math.html#math.sumprod; review_level=official-selected-API
Selectedofficial math.sumprod API read;accessdate is notpublicationyear,no globalcorrectrounding claim.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
