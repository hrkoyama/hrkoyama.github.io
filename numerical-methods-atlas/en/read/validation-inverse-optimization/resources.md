# Optimization, noise and regularization in the Bratu inverse problem

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-inverse-optimization/

Resources explicitly registered to the methods, problems and executions of this chapter. Retain existing synthetic observations and compare GN/LM, quasi-Newton methods and regularization selection on small fixed controls.

## Methods

- [Gradient and quasi-Newton optimization](<https://hrkoyama.github.io/numerical-methods-atlas/methods/optimization/?lang=en>)

  Original SVD least-squares GN/LM, the retained projected-gradient solver, SciPy TRF and explicitly unbounded SciPy LM. A canonical lower/upper box is explicitly adapted to the legacy per-parameter intervals.
- [Gradient and quasi-Newton optimization](<https://hrkoyama.github.io/numerical-methods-atlas/methods/optimization/?lang=en>)

  Original inverse-BFGS and vector-only two-loop L-BFGS with three pairs. A separate small dense oracle replays only currently retained pairs from the current gamma0 I. SciPy BFGS and unbounded L-BFGS-B are distinct software companions.
- [Gradient and quasi-Newton optimization](<https://hrkoyama.github.io/numerical-methods-atlas/methods/optimization/?lang=en>)

  Select the largest admissible gamma using 1.05 times the realized noise norm only after the full gamma path qualifies. Incomplete paths and complete paths with no admissible gamma are distinct. Four-point L-curves are descriptive diagnostics.
- [Gradient and quasi-Newton optimization](<https://hrkoyama.github.io/numerical-methods-atlas/methods/optimization/?lang=en>)

## Equations

- [Bratu nonlinear boundary-value problem](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bratu-en>)

  The convention here is −u″=λ exp(u). Newton–Krylov checks cover residuals, refinement and inner-solver failures. A dimensionless one-dimensional Bratu problem with 31 interior nodes and zero Dirichlet data. The existing two-coefficient extension and saved observations are reused; objective regularization gamma and LM damping mu are distinct.
- [Finite-dimensional algebraic optimization and known minima](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#finite-dimensional-optimization-en>)

  Dimensionless algebraic optimization of an eight-dimensional SPD quadratic and a two-variable Rosenbrock function. There is no physical spatial domain or PDE boundary; compare known minima and local iterative actions. Dimensionless unconstrained algebraic optimization with known analytic minima; there is no physical PDE boundary condition.
- [Bratu nonlinear boundary-value problem](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bratu-en>)

  The convention here is −u″=λ exp(u). Newton–Krylov checks cover residuals, refinement and inner-solver failures. Bratu inference uses 31 interior nodes, five observations, W=I/5 and Sigma=sigma² I. Existing 1023-grid observations are reused without regeneration. Fixed sigma values are 1e-4/1e-3, seeds are 67001/67002 and the gamma list has five entries.
- [Finite-dimensional algebraic optimization and known minima](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#finite-dimensional-optimization-en>)

  Dimensionless algebraic optimization of an eight-dimensional SPD quadratic and a two-variable Rosenbrock function. There is no physical spatial domain or PDE boundary; compare known minima and local iterative actions.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-gn-lm-bounds/?lang=en#bratu-gn-lm-bounds-en-algorithm>)

  Original SVD least-squares GN/LM, the retained projected-gradient solver, SciPy TRF and explicitly unbounded SciPy LM. A canonical lower/upper box is explicitly adapted to the legacy per-parameter intervals.
- [Bratu nonlinear boundary-value problem](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bratu-en>)

  The convention here is −u″=λ exp(u). Newton–Krylov checks cover residuals, refinement and inner-solver failures.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/bfgs-lbfgs-controls/?lang=en#bfgs-lbfgs-controls-en-algorithm>)

  Original inverse-BFGS and vector-only two-loop L-BFGS with three pairs. A separate small dense oracle replays only currently retained pairs from the current gamma0 I. SciPy BFGS and unbounded L-BFGS-B are distinct software companions.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-noise-regularization/?lang=en#bratu-noise-regularization-en-algorithm>)

  Select the largest admissible gamma using 1.05 times the realized noise norm only after the full gamma path qualifies. Incomplete paths and complete paths with no admissible gamma are distinct. Four-point L-curves are descriptive diagnostics.

## Problem figures

- [Bratu comparisons of GN, LM and bounded least squares](<https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-gn-lm-bounds/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/results/bratu-gn-lm-bounds-preview.png
- [BFGS and three-pair L-BFGS at known minima](<https://hrkoyama.github.io/numerical-methods-atlas/problems/bfgs-lbfgs-controls/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/results/bfgs-lbfgs-controls-preview.png
- [Noise, model discrepancy and finite gamma paths](<https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-noise-regularization/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/results/bratu-noise-regularization-preview.png
- [Bratu comparisons of GN, LM and bounded least squares](<https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/results/bratu-gn-lm-bounds.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/results/bratu-gn-lm-bounds.png
- [BFGS and three-pair L-BFGS at known minima](<https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/results/bfgs-lbfgs-controls.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/results/bfgs-lbfgs-controls.png
- [Noise, model discrepancy and finite gamma paths](<https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/results/bratu-noise-regularization.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/results/bratu-noise-regularization.png

## Exact / reference solutions

- [Bratu comparisons of GN, LM and bounded least squares — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-gn-lm-bounds/?lang=en#references-en>)

  Independent Thomas states/sensitivities and four local reference fits. Gate final state residuals, physical gradient or projected gradient, objective gaps, data-only SVD and active bounds. Common references for unbounded methods must be strictly interior and unbounded-stationary.
- [Independent Thomas-based local references for Bratu inverse least squares](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-bratu-gn-lm-bounds-en>)
  relation: same-problem
  reference_kind: numerical-reference

  Finite-grid numerical reference A two-coefficient inverse problem uses 31 interior nodes and five observations of the one-dimensional zero-Dirichlet Bratu model. Reuse existing synthetic data; the physical box is a in[1,2.8],b in[-.5,.5]. Objective regularization gamma, LM damping mu and variable scaling are distinct. A local comparison on a small smooth branch. The optimizer library is shared by the reference and a companion; no global minimum or uniqueness proof is claimed. LM is not presented as a box-constrained method.
- [BFGS and three-pair L-BFGS at known minima — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/bfgs-lbfgs-controls/?lang=en#references-en>)

  Sixteen fixed fits check analytic minima/gradients, strong Wolfe and resolved positive curvature at every accepted step, symmetric SPD BFGS matrices and L-BFGS action defects. Retained-pair and dense-oracle storage are reported separately.
- [Analytic known minima and the current limited-memory action](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-bfgs-lbfgs-controls-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference Dimensionless unconstrained algebraic optimization uses an eight-dimensional SPD quadratic and three Rosenbrock starts. L-BFGS retains only the current last three pairs. There is no physical PDE boundary condition. No exact n-step termination or general global convergence on Rosenbrock is claimed. The selected original text uses weak Wolfe, distinct from this study’s strong Wolfe policy. Fletcher’s 1970 original article remains unread.
- [Noise, model discrepancy and finite gamma paths — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-noise-regularization/?lang=en#references-en>)

  Gate final residuals, physical KKT conditions and completion for all 42 fits, the selection rule, and covariance/bias/model-shift response against explicit scalar 2x2 algebra, including symmetry and PSD.
- [Bratu references for finite gamma paths and local linear noise propagation](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-bratu-noise-regularization-en>)
  relation: same-problem
  reference_kind: numerical-reference

  Finite-grid numerical reference Use 31 interior nodes, five observations, W=I/5 and Sigma=sigma² I. Reuse existing 31/1023-grid observations. The noise standard deviations sigma are 1e-4 and 1e-3; two seeds provide independent base noises, while scaled/grid-context variants are paired. Gamma has five fixed values. Ellipses are plug-in noise propagation for a local Gauss–Newton linear model with the selected gamma treated as fixed. They omit nonlinear residual Hessians and selection randomness and are not selection-conditional covariance, a posterior or a coverage guarantee. Continuous gamma paths and real data remain unverified.
- [Independent Thomas-based local references for Bratu inverse least squares](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-bratu-gn-lm-bounds-en>)
  reference_kind: numerical-reference

  Finite-grid numerical reference A two-coefficient inverse problem uses 31 interior nodes and five observations of the one-dimensional zero-Dirichlet Bratu model. Reuse existing synthetic data; the physical box is a in[1,2.8],b in[-.5,.5]. Objective regularization gamma, LM damping mu and variable scaling are distinct.
- [Analytic known minima and the current limited-memory action](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-bfgs-lbfgs-controls-en>)
  reference_kind: analytic

  Analytic reference Dimensionless unconstrained algebraic optimization uses an eight-dimensional SPD quadratic and three Rosenbrock starts. L-BFGS retains only the current last three pairs. There is no physical PDE boundary condition.
- [Bratu references for finite gamma paths and local linear noise propagation](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-bratu-noise-regularization-en>)
  reference_kind: numerical-reference

  Finite-grid numerical reference Use 31 interior nodes, five observations, W=I/5 and Sigma=sigma² I. Reuse existing 31/1023-grid observations. The noise standard deviations sigma are 1e-4 and 1e-3; two seeds provide independent base noises, while scaled/grid-context variants are paired. Gamma has five fixed values.
- [Bratu comparisons of GN, LM and bounded least squares — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-gn-lm-bounds/?lang=en#bratu-gn-lm-bounds-en-validation>)

  Independent Thomas states/sensitivities and four local reference fits. Gate final state residuals, physical gradient or projected gradient, objective gaps, data-only SVD and active bounds. Common references for unbounded methods must be strictly interior and unbounded-stationary.
- [Independent Thomas-based local references for Bratu inverse least squares](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-bratu-gn-lm-bounds-en>)
  relation: same-problem
  reference_kind: numerical-reference

  Finite-grid numerical reference A two-coefficient inverse problem uses 31 interior nodes and five observations of the one-dimensional zero-Dirichlet Bratu model. Reuse existing synthetic data; the physical box is a in[1,2.8],b in[-.5,.5]. Objective regularization gamma, LM damping mu and variable scaling are distinct. A local comparison on a small smooth branch. The optimizer library is shared by the reference and a companion; no global minimum or uniqueness proof is claimed. LM is not presented as a box-constrained method.
- [BFGS and three-pair L-BFGS at known minima — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/bfgs-lbfgs-controls/?lang=en#bfgs-lbfgs-controls-en-validation>)

  Sixteen fixed fits check analytic minima/gradients, strong Wolfe and resolved positive curvature at every accepted step, symmetric SPD BFGS matrices and L-BFGS action defects. Retained-pair and dense-oracle storage are reported separately.
- [Analytic known minima and the current limited-memory action](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-bfgs-lbfgs-controls-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference Dimensionless unconstrained algebraic optimization uses an eight-dimensional SPD quadratic and three Rosenbrock starts. L-BFGS retains only the current last three pairs. There is no physical PDE boundary condition. No exact n-step termination or general global convergence on Rosenbrock is claimed. The selected original text uses weak Wolfe, distinct from this study’s strong Wolfe policy. Fletcher’s 1970 original article remains unread.
- [Noise, model discrepancy and finite gamma paths — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-noise-regularization/?lang=en#bratu-noise-regularization-en-validation>)

  Gate final residuals, physical KKT conditions and completion for all 42 fits, the selection rule, and covariance/bias/model-shift response against explicit scalar 2x2 algebra, including symmetry and PSD.
- [Bratu references for finite gamma paths and local linear noise propagation](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-bratu-noise-regularization-en>)
  relation: same-problem
  reference_kind: numerical-reference

  Finite-grid numerical reference Use 31 interior nodes, five observations, W=I/5 and Sigma=sigma² I. Reuse existing 31/1023-grid observations. The noise standard deviations sigma are 1e-4 and 1e-3; two seeds provide independent base noises, while scaled/grid-context variants are paired. Gamma has five fixed values. Ellipses are plug-in noise propagation for a local Gauss–Newton linear model with the selected gamma treated as fixed. They omit nonlinear residual Hessians and selection randomness and are not selection-conditional covariance, a posterior or a coverage guarantee. Continuous gamma paths and real data remain unverified.

## Code and validation

- [Bratu comparisons of GN, LM and bounded least squares](<https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-gn-lm-bounds/?lang=en>)
  availability: run

  Seventeen fixed fits separate parameter scaling, weights, bounds and physical-coordinate stopping conditions.
- [BFGS and three-pair L-BFGS at known minima](<https://hrkoyama.github.io/numerical-methods-atlas/validation/bfgs-lbfgs-controls/?lang=en>)
  availability: run

  An eight-dimensional SPD quadratic and three Rosenbrock starts test curvature, strong Wolfe conditions and the current finite-memory action.
- [Noise, model discrepancy and finite gamma paths](<https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-noise-regularization/?lang=en>)
  availability: run

  Two independent noise vectors are reused across scales and data contexts. Forty-two fixed fits separate finite-list gamma selection from fixed-gamma local covariance.
