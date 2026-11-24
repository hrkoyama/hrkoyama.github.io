# Optimization, noise and regularization in the Bratu inverse problem

Retain existing synthetic observations and compare GN/LM, quasi-Newton methods and regularization selection on small fixed controls.

These additional validation supplements are managed separately from the common 22-example registry. Receipts cover independent ZIP extraction, tests and every fixed input within each group. Changes of settings, methods or step sizes do not add independent physical problems.

## Bratu comparisons of GN, LM and bounded least squares

Seventeen fixed fits separate parameter scaling, weights, bounds and physical-coordinate stopping conditions.

**Methods used**

- [Gradient and quasi-Newton optimization](https://hrkoyama.github.io/numerical-methods-atlas/methods/optimization/?lang=en) (`optimization`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-gn-lm-bounds/?lang=en#bratu-gn-lm-bounds-en-algorithm)

Original SVD least-squares GN/LM, the retained projected-gradient solver, SciPy TRF and explicitly unbounded SciPy LM. A canonical lower/upper box is explicitly adapted to the legacy per-parameter intervals.

$$
F(u,\theta)=A_hu-(a+b(2x-1))e^u=0
$$

$$
\mathcal L=\tfrac12\|H u-d\|_W^2+\tfrac\gamma2\|\theta-\theta_0\|^2
$$

$$
K=-H F_u^{-1}F_\theta,\quad\theta=\theta_0+D z
$$

- [Bratu nonlinear boundary-value problem](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bratu-en) (`bratu`)

A dimensionless one-dimensional Bratu problem with 31 interior nodes and zero Dirichlet data. The existing two-coefficient extension and saved observations are reused; objective regularization gamma and LM damping mu are distinct.


**Problem figure**

![Bratu comparisons of GN, LM and bounded least squares: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/results/bratu-gn-lm-bounds.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Bratu comparisons of GN, LM and bounded least squares](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-gn-lm-bounds/?lang=en) (`bratu-gn-lm-bounds`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-gn-lm-bounds/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-gn-lm-bounds/?lang=en#bratu-gn-lm-bounds-en-validation)

Independent Thomas states/sensitivities and four local reference fits. Gate final state residuals, physical gradient or projected gradient, objective gaps, data-only SVD and active bounds. Common references for unbounded methods must be strictly interior and unbounded-stationary.

- [Independent Thomas-based local references for Bratu inverse least squares](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-bratu-gn-lm-bounds-en) (`bratu-gn-lm-bounds`; Same-problem reference · Finite-grid numerical reference)

A local comparison on a small smooth branch. The optimizer library is shared by the reference and a companion; no global minimum or uniqueness proof is claimed. LM is not presented as a box-constrained method.
### Assumptions, units and boundaries

A dimensionless one-dimensional Bratu problem with 31 interior nodes and zero Dirichlet data. The existing two-coefficient extension and saved observations are reused; objective regularization gamma and LM damping mu are distinct.

**Editorial clarification**

A local comparison on a small smooth branch. The optimizer library is shared by the reference and a companion; no global minimum or uniqueness proof is claimed. LM is not presented as a box-constrained method.

### Adopted numerical method

Original SVD least-squares GN/LM, the retained projected-gradient solver, SciPy TRF and explicitly unbounded SciPy LM. A canonical lower/upper box is explicitly adapted to the legacy per-parameter intervals.

$$
F(u,\theta)=A_hu-(a+b(2x-1))e^u=0
$$

$$
\mathcal L=\tfrac12\|H u-d\|_W^2+\tfrac\gamma2\|\theta-\theta_0\|^2
$$

$$
K=-H F_u^{-1}F_\theta,\quad\theta=\theta_0+D z
$$

### References and validation

Independent Thomas states/sensitivities and four local reference fits. Gate final state residuals, physical gradient or projected gradient, objective gaps, data-only SVD and active bounds. Common references for unbounded methods must be strictly interior and unbounded-stationary.

### Limits

A local comparison on a small smooth branch. The optimizer library is shared by the reference and a companion; no global minimum or uniqueness proof is claimed. LM is not presented as a box-constrained method.

### Stored measurements and decisions

```json
{
  "metrics": {
    "attempted_fits": 17,
    "completed_fits": 17,
    "expected_fits": 17,
    "forward_evaluations": 234,
    "maximum_stationarity_inf": 9.69771818404297e-10,
    "reference_scope": "independent Thomas state/Jacobian; shared local TRF optimizer; no global optimum proof"
  },
  "checks": {
    "fit-0-complete": true,
    "fit-0-final-forward-residual": true,
    "fit-0-stationary": true,
    "fit-0-objective-reference": true,
    "fit-0-data-rank": true,
    "fit-1-complete": true,
    "fit-1-final-forward-residual": true,
    "fit-1-stationary": true,
    "fit-1-objective-reference": true,
    "fit-1-data-rank": true,
    "fit-2-complete": true,
    "fit-2-final-forward-residual": true,
    "fit-2-stationary": true,
    "fit-2-objective-reference": true,
    "fit-2-data-rank": true,
    "fit-2-feasible": true,
    "fit-3-complete": true,
    "fit-3-final-forward-residual": true,
    "fit-3-stationary": true,
    "fit-3-objective-reference": true,
    "fit-3-data-rank": true,
    "fit-3-feasible": true,
    "fit-4-complete": true,
    "fit-4-final-forward-residual": true,
    "fit-4-stationary": true,
    "fit-4-objective-reference": true,
    "fit-4-data-rank": true,
    "fit-5-complete": true,
    "fit-5-final-forward-residual": true,
    "fit-5-stationary": true,
    "fit-5-objective-reference": true,
    "fit-5-data-rank": true,
    "fit-6-complete": true,
    "fit-6-final-forward-residual": true,
    "fit-6-stationary": true,
    "fit-6-objective-reference": true,
    "fit-6-data-rank": true,
    "fit-7-complete": true,
    "fit-7-final-forward-residual": true,
    "fit-7-stationary": true,
    "fit-7-objective-reference": true,
    "fit-7-data-rank": true,
    "fit-7-feasible": true,
    "fit-8-complete": true,
    "fit-8-final-forward-residual": true,
    "fit-8-stationary": true,
    "fit-8-objective-reference": true,
    "fit-8-data-rank": true,
    "fit-8-feasible": true,
    "fit-9-complete": true,
    "fit-9-final-forward-residual": true,
    "fit-9-stationary": true,
    "fit-9-objective-reference": true,
    "fit-9-data-rank": true,
    "fit-10-complete": true,
    "fit-10-final-forward-residual": true,
    "fit-10-stationary": true,
    "fit-10-objective-reference": true,
    "fit-10-data-rank": true,
    "fit-10-feasible": true,
    "fit-10-active-constraint": true,
    "fit-11-complete": true,
    "fit-11-final-forward-residual": true,
    "fit-11-stationary": true,
    "fit-11-objective-reference": true,
    "fit-11-data-rank": true,
    "fit-11-feasible": true,
    "fit-11-active-constraint": true,
    "fit-12-complete": true,
    "fit-12-final-forward-residual": true,
    "fit-12-stationary": true,
    "fit-12-objective-reference": true,
    "fit-12-data-rank": true,
    "fit-13-complete": true,
    "fit-13-final-forward-residual": true,
    "fit-13-stationary": true,
    "fit-13-objective-reference": true,
    "fit-13-data-rank": true,
    "fit-14-complete": true,
    "fit-14-final-forward-residual": true,
    "fit-14-stationary": true,
    "fit-14-objective-reference": true,
    "fit-14-data-rank": true,
    "fit-14-feasible": true,
    "fit-15-complete": true,
    "fit-15-final-forward-residual": true,
    "fit-15-stationary": true,
    "fit-15-objective-reference": true,
    "fit-15-data-rank": true,
    "fit-15-feasible": true,
    "fit-16-complete": true,
    "fit-16-final-forward-residual": true,
    "fit-16-stationary": true,
    "fit-16-objective-reference": true,
    "fit-16-data-rank": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-gn-lm-bounds/index.json

![Saved two-parameter iterates and residual evaluations. SciPy paths include residual evaluations, not only accepted iterates; these are parameter coordinates, not a two-dimensional physical flow.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/results/bratu-gn-lm-bounds-preview.png)

Saved two-parameter iterates and residual evaluations. SciPy paths include residual evaluations, not only accepted iterates; these are parameter coordinates, not a two-dimensional physical flow.

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/atlas-inverse-optimization-2026-11-24.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- SciPy 1.14.1 least_squares documentation [accessed 2026-11-24]. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.optimize.least_squares.html; review_level=selected-primary-scope
Parameters, bounds, callable Jacobian, method-specific ftol/xtol/gtol and x_scale, max_nfev, returned status and Notes on LM and TRF. LM does not handle bounds and requires at least as many residual rows as variables; TRF supports bounds. MINPACK/STIR original papers were not read in this preparation.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## BFGS and three-pair L-BFGS at known minima

An eight-dimensional SPD quadratic and three Rosenbrock starts test curvature, strong Wolfe conditions and the current finite-memory action.

**Methods used**

- [Gradient and quasi-Newton optimization](https://hrkoyama.github.io/numerical-methods-atlas/methods/optimization/?lang=en) (`optimization`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/bfgs-lbfgs-controls/?lang=en#bfgs-lbfgs-controls-en-algorithm)

Original inverse-BFGS and vector-only two-loop L-BFGS with three pairs. A separate small dense oracle replays only currently retained pairs from the current gamma0 I. SciPy BFGS and unbounded L-BFGS-B are distinct software companions.

$$
H_+=(I-\rho s y^T)H(I-\rho y s^T)+\rho s s^T
$$

$$
\rho=(y^Ts)^{-1},\quad\gamma_0=(s^Ty)/(y^Ty)
$$

$$
f(x,y)=100(y-x^2)^2+(1-x)^2
$$

- [Finite-dimensional algebraic optimization and known minima](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#finite-dimensional-optimization-en) (`finite-dimensional-optimization`)

Dimensionless unconstrained algebraic optimization with known analytic minima; there is no physical PDE boundary condition.


**Problem figure**

![BFGS and three-pair L-BFGS at known minima: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/results/bfgs-lbfgs-controls.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[BFGS and three-pair L-BFGS at known minima](https://hrkoyama.github.io/numerical-methods-atlas/problems/bfgs-lbfgs-controls/?lang=en) (`bfgs-lbfgs-controls`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/bfgs-lbfgs-controls/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/bfgs-lbfgs-controls/?lang=en#bfgs-lbfgs-controls-en-validation)

Sixteen fixed fits check analytic minima/gradients, strong Wolfe and resolved positive curvature at every accepted step, symmetric SPD BFGS matrices and L-BFGS action defects. Retained-pair and dense-oracle storage are reported separately.

- [Analytic known minima and the current limited-memory action](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-bfgs-lbfgs-controls-en) (`bfgs-lbfgs-controls`; Same-problem reference · Analytic reference)

No exact n-step termination or general global convergence on Rosenbrock is claimed. The selected original text uses weak Wolfe, distinct from this study’s strong Wolfe policy. Fletcher’s 1970 original article remains unread.
### Assumptions, units and boundaries

Dimensionless unconstrained algebraic optimization with known analytic minima; there is no physical PDE boundary condition.

**Editorial clarification**

No exact n-step termination or general global convergence on Rosenbrock is claimed. The selected original text uses weak Wolfe, distinct from this study’s strong Wolfe policy. Fletcher’s 1970 original article remains unread. Plot axes describe finite-dimensional variables, iterations or diagnostics, not a physical spatial dimension or PDE boundary.

### Adopted numerical method

Original inverse-BFGS and vector-only two-loop L-BFGS with three pairs. A separate small dense oracle replays only currently retained pairs from the current gamma0 I. SciPy BFGS and unbounded L-BFGS-B are distinct software companions.

$$
H_+=(I-\rho s y^T)H(I-\rho y s^T)+\rho s s^T
$$

$$
\rho=(y^Ts)^{-1},\quad\gamma_0=(s^Ty)/(y^Ty)
$$

$$
f(x,y)=100(y-x^2)^2+(1-x)^2
$$

### References and validation

Sixteen fixed fits check analytic minima/gradients, strong Wolfe and resolved positive curvature at every accepted step, symmetric SPD BFGS matrices and L-BFGS action defects. Retained-pair and dense-oracle storage are reported separately.

### Limits

No exact n-step termination or general global convergence on Rosenbrock is claimed. The selected original text uses weak Wolfe, distinct from this study’s strong Wolfe policy. Fletcher’s 1970 original article remains unread.

### Stored measurements and decisions

```json
{
  "metrics": {
    "attempted_fits": 16,
    "completed_fits": 16,
    "expected_fits": 16,
    "objective_evaluations": 722,
    "maximum_gradient_inf": 9.090384658211326e-08,
    "independent_target": "known analytic minima; current-scaling retained-pair dense action"
  },
  "checks": {
    "fit-0-complete": true,
    "fit-0-point": true,
    "fit-0-gradient": true,
    "fit-0-strong-wolfe": true,
    "fit-0-resolved-curvature": true,
    "fit-0-inverse-symmetry": true,
    "fit-0-inverse-spd": true,
    "fit-1-complete": true,
    "fit-1-point": true,
    "fit-1-gradient": true,
    "fit-1-strong-wolfe": true,
    "fit-1-resolved-curvature": true,
    "fit-1-retained-dense-oracle": true,
    "fit-2-complete": true,
    "fit-2-point": true,
    "fit-2-gradient": true,
    "fit-3-complete": true,
    "fit-3-point": true,
    "fit-3-gradient": true,
    "fit-4-complete": true,
    "fit-4-point": true,
    "fit-4-gradient": true,
    "fit-4-objective": true,
    "fit-4-strong-wolfe": true,
    "fit-4-resolved-curvature": true,
    "fit-4-inverse-symmetry": true,
    "fit-4-inverse-spd": true,
    "fit-5-complete": true,
    "fit-5-point": true,
    "fit-5-gradient": true,
    "fit-5-objective": true,
    "fit-5-strong-wolfe": true,
    "fit-5-resolved-curvature": true,
    "fit-5-retained-dense-oracle": true,
    "fit-6-complete": true,
    "fit-6-point": true,
    "fit-6-gradient": true,
    "fit-6-objective": true,
    "fit-7-complete": true,
    "fit-7-point": true,
    "fit-7-gradient": true,
    "fit-7-objective": true,
    "fit-8-complete": true,
    "fit-8-point": true,
    "fit-8-gradient": true,
    "fit-8-objective": true,
    "fit-8-strong-wolfe": true,
    "fit-8-resolved-curvature": true,
    "fit-8-inverse-symmetry": true,
    "fit-8-inverse-spd": true,
    "fit-9-complete": true,
    "fit-9-point": true,
    "fit-9-gradient": true,
    "fit-9-objective": true,
    "fit-9-strong-wolfe": true,
    "fit-9-resolved-curvature": true,
    "fit-9-retained-dense-oracle": true,
    "fit-10-complete": true,
    "fit-10-point": true,
    "fit-10-gradient": true,
    "fit-10-objective": true,
    "fit-11-complete": true,
    "fit-11-point": true,
    "fit-11-gradient": true,
    "fit-11-objective": true,
    "fit-12-complete": true,
    "fit-12-point": true,
    "fit-12-gradient": true,
    "fit-12-objective": true,
    "fit-12-strong-wolfe": true,
    "fit-12-resolved-curvature": true,
    "fit-12-inverse-symmetry": true,
    "fit-12-inverse-spd": true,
    "fit-13-complete": true,
    "fit-13-point": true,
    "fit-13-gradient": true,
    "fit-13-objective": true,
    "fit-13-strong-wolfe": true,
    "fit-13-resolved-curvature": true,
    "fit-13-retained-dense-oracle": true,
    "fit-14-complete": true,
    "fit-14-point": true,
    "fit-14-gradient": true,
    "fit-14-objective": true,
    "fit-15-complete": true,
    "fit-15-point": true,
    "fit-15-gradient": true,
    "fit-15-objective": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/bfgs-lbfgs-controls/index.json

![Actual Rosenbrock iterates on analytic objective contours for three fixed starts and four methods; this is not a general convergence guarantee.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/results/bfgs-lbfgs-controls-preview.png)

Actual Rosenbrock iterates on analytic objective contours for three fixed starts and four methods; this is not a general convergence guarantee.

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/atlas-inverse-optimization-2026-11-24.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- On the limited memory BFGS method for large scale optimization [accessed 2026-11-24]. https://users.iems.northwestern.edu/~nocedal/PDFfiles/limited-memory.pdf; review_level=selected-primary-scope
Author-hosted PDF selected physical pages 3–5 (printed 2–4), rendered locally and visually inspected: limited storage, deletion of oldest correction, Eq. (2.1) inverse-BFGS, Algorithm 2.1 and Eq. (2.6) retained-update construction. No full-paper/proof/experiment or Section 4 scaling review. The selected original uses weak Wolfe; this study deliberately uses a separately specified strong-Wolfe line search. Current-gamma least-squares scaling is independently derived here, not attributed to unread text.

- SciPy 1.14.1 line_search documentation [accessed 2026-11-24]. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.optimize.line_search.html; review_level=selected-primary-scope
Signature, c1/c2, descent-direction requirement, returned failure None and evaluation counts. Cited textbook pages were not read.

- SciPy 1.14.1 BFGS documentation [accessed 2026-11-24]. https://docs.scipy.org/doc/scipy-1.14.1/reference/optimize.minimize-bfgs.html; review_level=selected-primary-scope
Options gtol, norm, c1/c2, hess_inv0 and precision-loss notes; no claim of reading a BFGS original paper.

- SciPy 1.14.1 L-BFGS-B documentation [accessed 2026-11-24]. https://docs.scipy.org/doc/scipy-1.14.1/reference/optimize.minimize-lbfgsb.html; review_level=selected-primary-scope
Options maxcor, ftol, gtol/projected-gradient convention, maxfun, maxiter and maxls.

- A new approach to variable metric algorithms. https://academic.oup.com/comjnl/article-abstract/13/3/317/345520?login=false; review_level=bibliography-only-original-unread
Prior saved publisher metadata/abstract-search record only. Original article full text remains unavailable/unread; no new request was made and no derivation is claimed to have been checked against it.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## Noise, model discrepancy and finite gamma paths

Two independent noise vectors are reused across scales and data contexts. Forty-two fixed fits separate finite-list gamma selection from fixed-gamma local covariance.

**Methods used**

- [Gradient and quasi-Newton optimization](https://hrkoyama.github.io/numerical-methods-atlas/methods/optimization/?lang=en) (`optimization`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-noise-regularization/?lang=en#bratu-noise-regularization-en-algorithm)

Select the largest admissible gamma using 1.05 times the realized noise norm only after the full gamma path qualifies. Incomplete paths and complete paths with no admissible gamma are distinct. Four-point L-curves are descriptive diagnostics.

$$
G=K^TWK+\gamma I
$$

$$
C_\gamma=G^{-1}K^TW\Sigma WKG^{-T}
$$

$$
\operatorname{bias}_\gamma=-\gamma G^{-1}(\theta_* -\theta_0)
$$

- [Bratu nonlinear boundary-value problem](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bratu-en) (`bratu`)

Bratu inference uses 31 interior nodes, five observations, W=I/5 and Sigma=sigma² I. Existing 1023-grid observations are reused without regeneration. Fixed sigma values are 1e-4/1e-3, seeds are 67001/67002 and the gamma list has five entries.


**Problem figure**

![Noise, model discrepancy and finite gamma paths: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/results/bratu-noise-regularization.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Noise, model discrepancy and finite gamma paths](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-noise-regularization/?lang=en) (`bratu-noise-regularization`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-noise-regularization/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-noise-regularization/?lang=en#bratu-noise-regularization-en-validation)

Gate final residuals, physical KKT conditions and completion for all 42 fits, the selection rule, and covariance/bias/model-shift response against explicit scalar 2x2 algebra, including symmetry and PSD.

- [Bratu references for finite gamma paths and local linear noise propagation](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-bratu-noise-regularization-en) (`bratu-noise-regularization`; Same-problem reference · Finite-grid numerical reference)

Ellipses are plug-in noise propagation for a local Gauss–Newton linear model with the selected gamma treated as fixed. They omit nonlinear residual Hessians and selection randomness and are not selection-conditional covariance, a posterior or a coverage guarantee. Continuous gamma paths and real data remain unverified.
### Assumptions, units and boundaries

Bratu inference uses 31 interior nodes, five observations, W=I/5 and Sigma=sigma² I. Existing 1023-grid observations are reused without regeneration. Fixed sigma values are 1e-4/1e-3, seeds are 67001/67002 and the gamma list has five entries.

**Editorial clarification**

Ellipses are plug-in noise propagation for a local Gauss–Newton linear model with the selected gamma treated as fixed. They omit nonlinear residual Hessians and selection randomness and are not selection-conditional covariance, a posterior or a coverage guarantee. Continuous gamma paths and real data remain unverified.

### Adopted numerical method

Select the largest admissible gamma using 1.05 times the realized noise norm only after the full gamma path qualifies. Incomplete paths and complete paths with no admissible gamma are distinct. Four-point L-curves are descriptive diagnostics.

$$
G=K^TWK+\gamma I
$$

$$
C_\gamma=G^{-1}K^TW\Sigma WKG^{-T}
$$

$$
\operatorname{bias}_\gamma=-\gamma G^{-1}(\theta_* -\theta_0)
$$

### References and validation

Gate final residuals, physical KKT conditions and completion for all 42 fits, the selection rule, and covariance/bias/model-shift response against explicit scalar 2x2 algebra, including symmetry and PSD.

### Limits

Ellipses are plug-in noise propagation for a local Gauss–Newton linear model with the selected gamma treated as fixed. They omit nonlinear residual Hessians and selection randomness and are not selection-conditional covariance, a posterior or a coverage guarantee. Continuous gamma paths and real data remain unverified.

### Stored measurements and decisions

```json
{
  "metrics": {
    "attempted_fits": 42,
    "completed_fits": 42,
    "expected_fits": 42,
    "independent_base_noise_vectors": 2,
    "coupled_gamma_paths": 8,
    "forward_evaluations": 339,
    "maximum_stationarity_inf": 2.8491609072034407e-10,
    "covariance_scope": "fixed-gamma Gauss–Newton local-linear-model plug-in; no selection-event covariance or coverage claim",
    "detailed_fit_records": "case67-all-fits.json"
  },
  "checks": {
    "fit-0-complete": true,
    "fit-0-final-forward-residual": true,
    "fit-0-stationary": true,
    "fit-0-feasible": true,
    "fit-1-complete": true,
    "fit-1-final-forward-residual": true,
    "fit-1-stationary": true,
    "fit-1-feasible": true,
    "fit-2-complete": true,
    "fit-2-final-forward-residual": true,
    "fit-2-stationary": true,
    "fit-2-feasible": true,
    "fit-3-complete": true,
    "fit-3-final-forward-residual": true,
    "fit-3-stationary": true,
    "fit-3-feasible": true,
    "fit-4-complete": true,
    "fit-4-final-forward-residual": true,
    "fit-4-stationary": true,
    "fit-4-feasible": true,
    "path-0-complete": true,
    "path-0-selection": true,
    "path-0-covariance-eligibility-and-psd": true,
    "fit-5-complete": true,
    "fit-5-final-forward-residual": true,
    "fit-5-stationary": true,
    "fit-5-feasible": true,
    "fit-6-complete": true,
    "fit-6-final-forward-residual": true,
    "fit-6-stationary": true,
    "fit-6-feasible": true,
    "fit-7-complete": true,
    "fit-7-final-forward-residual": true,
    "fit-7-stationary": true,
    "fit-7-feasible": true,
    "fit-8-complete": true,
    "fit-8-final-forward-residual": true,
    "fit-8-stationary": true,
    "fit-8-feasible": true,
    "fit-9-complete": true,
    "fit-9-final-forward-residual": true,
    "fit-9-stationary": true,
    "fit-9-feasible": true,
    "path-1-complete": true,
    "path-1-selection": true,
    "path-1-covariance-eligibility-and-psd": true,
    "fit-10-complete": true,
    "fit-10-final-forward-residual": true,
    "fit-10-stationary": true,
    "fit-10-feasible": true,
    "fit-11-complete": true,
    "fit-11-final-forward-residual": true,
    "fit-11-stationary": true,
    "fit-11-feasible": true,
    "fit-12-complete": true,
    "fit-12-final-forward-residual": true,
    "fit-12-stationary": true,
    "fit-12-feasible": true,
    "fit-13-complete": true,
    "fit-13-final-forward-residual": true,
    "fit-13-stationary": true,
    "fit-13-feasible": true,
    "fit-14-complete": true,
    "fit-14-final-forward-residual": true,
    "fit-14-stationary": true,
    "fit-14-feasible": true,
    "path-2-complete": true,
    "path-2-selection": true,
    "path-2-covariance-eligibility-and-psd": true,
    "fit-15-complete": true,
    "fit-15-final-forward-residual": true,
    "fit-15-stationary": true,
    "fit-15-feasible": true,
    "fit-16-complete": true,
    "fit-16-final-forward-residual": true,
    "fit-16-stationary": true,
    "fit-16-feasible": true,
    "fit-17-complete": true,
    "fit-17-final-forward-residual": true,
    "fit-17-stationary": true,
    "fit-17-feasible": true,
    "fit-18-complete": true,
    "fit-18-final-forward-residual": true,
    "fit-18-stationary": true,
    "fit-18-feasible": true,
    "fit-19-complete": true,
    "fit-19-final-forward-residual": true,
    "fit-19-stationary": true,
    "fit-19-feasible": true,
    "path-3-complete": true,
    "path-3-selection": true,
    "path-3-covariance-eligibility-and-psd": true,
    "fit-20-complete": true,
    "fit-20-final-forward-residual": true,
    "fit-20-stationary": true,
    "fit-20-feasible": true,
    "fit-21-complete": true,
    "fit-21-final-forward-residual": true,
    "fit-21-stationary": true,
    "fit-21-feasible": true,
    "fit-22-complete": true,
    "fit-22-final-forward-residual": true,
    "fit-22-stationary": true,
    "fit-22-feasible": true,
    "fit-23-complete": true,
    "fit-23-final-forward-residual": true,
    "fit-23-stationary": true,
    "fit-23-feasible": true,
    "fit-24-complete": true,
    "fit-24-final-forward-residual": true,
    "fit-24-stationary": true,
    "fit-24-feasible": true,
    "path-4-complete": true,
    "path-4-selection": true,
    "path-4-covariance-eligibility-and-psd": true,
    "fit-25-complete": true,
    "fit-25-final-forward-residual": true,
    "fit-25-stationary": true,
    "fit-25-feasible": true,
    "fit-26-complete": true,
    "fit-26-final-forward-residual": true,
    "fit-26-stationary": true,
    "fit-26-feasible": true,
    "fit-27-complete": true,
    "fit-27-final-forward-residual": true,
    "fit-27-stationary": true,
    "fit-27-feasible": true,
    "fit-28-complete": true,
    "fit-28-final-forward-residual": true,
    "fit-28-stationary": true,
    "fit-28-feasible": true,
    "fit-29-complete": true,
    "fit-29-final-forward-residual": true,
    "fit-29-stationary": true,
    "fit-29-feasible": true,
    "path-5-complete": true,
    "path-5-selection": true,
    "path-5-covariance-eligibility-and-psd": true,
    "fit-30-complete": true,
    "fit-30-final-forward-residual": true,
    "fit-30-stationary": true,
    "fit-30-feasible": true,
    "fit-31-complete": true,
    "fit-31-final-forward-residual": true,
    "fit-31-stationary": true,
    "fit-31-feasible": true,
    "fit-32-complete": true,
    "fit-32-final-forward-residual": true,
    "fit-32-stationary": true,
    "fit-32-feasible": true,
    "fit-33-complete": true,
    "fit-33-final-forward-residual": true,
    "fit-33-stationary": true,
    "fit-33-feasible": true,
    "fit-34-complete": true,
    "fit-34-final-forward-residual": true,
    "fit-34-stationary": true,
    "fit-34-feasible": true,
    "path-6-complete": true,
    "path-6-selection": true,
    "path-6-covariance-eligibility-and-psd": true,
    "fit-35-complete": true,
    "fit-35-final-forward-residual": true,
    "fit-35-stationary": true,
    "fit-35-feasible": true,
    "fit-36-complete": true,
    "fit-36-final-forward-residual": true,
    "fit-36-stationary": true,
    "fit-36-feasible": true,
    "fit-37-complete": true,
    "fit-37-final-forward-residual": true,
    "fit-37-stationary": true,
    "fit-37-feasible": true,
    "fit-38-complete": true,
    "fit-38-final-forward-residual": true,
    "fit-38-stationary": true,
    "fit-38-feasible": true,
    "fit-39-complete": true,
    "fit-39-final-forward-residual": true,
    "fit-39-stationary": true,
    "fit-39-feasible": true,
    "path-7-complete": true,
    "path-7-selection": true,
    "path-7-covariance-eligibility-and-psd": true,
    "fit-40-complete": true,
    "fit-40-final-forward-residual": true,
    "fit-40-stationary": true,
    "fit-40-feasible": true,
    "fit-41-complete": true,
    "fit-41-final-forward-residual": true,
    "fit-41-stationary": true,
    "fit-41-feasible": true,
    "linear-control-covariance": true,
    "linear-control-bias": true,
    "linear-control-data-shift": true,
    "linear-control-symmetry": true,
    "linear-control-psd": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-noise-regularization/index.json

![Saved two-parameter estimates and fixed-gamma local one-standard-deviation ellipses. These are neither selection-conditional intervals nor confidence regions with coverage established by this small ensemble.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/results/bratu-noise-regularization-preview.png)

Saved two-parameter estimates and fixed-gamma local one-standard-deviation ellipses. These are neither selection-conditional intervals nor confidence regions with coverage established by this small ensemble.

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/atlas-inverse-optimization-2026-11-24.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- Regularization Tools, Version 4.1 for Matlab 7.3 [accessed 2026-11-24]. https://www2.compute.dtu.dk/~pcha/Regutools/RTv4manual.pdf; review_level=selected-primary-scope
Official author manual: selected text around Section 2.5 and Section 2.9; physical pages 20 and 37 (printed 18 and 35) rendered locally and visually inspected. L-curve residual/solution norm tradeoff and discrepancy equation (2.61) were read. Four-point chord curvature here is a finite-list diagnostic, not the manual spline/corner algorithm, a theorem of optimal regularization or coverage. Original software (1994) and later article (2007) are separate bibliographic works and were not read.

- SciPy 1.14.1 curve_fit documentation [accessed 2026-11-24]. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.optimize.curve_fit.html; review_level=selected-primary-scope
sigma/absolute_sigma and covariance interpretation sections. The penalized sandwich covariance in this study is derived independently; it is not presented as curve_fit output.

- SciPy 1.14.1 least_squares documentation [accessed 2026-11-24]. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.optimize.least_squares.html; review_level=selected-primary-scope
Parameters, bounds, callable Jacobian, method-specific ftol/xtol/gtol and x_scale, max_nfev, returned status and Notes on LM and TRF. LM does not handle bounds and requires at least as many residual rows as variables; TRF supports bounds. MINPACK/STIR original papers were not read in this preparation.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
