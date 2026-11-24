# Adjoints through time steps, folds and distributed coefficients

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-adjoint/

Resources explicitly registered to the methods, problems and executions of this chapter. Compare tangents and adjoints of discrete maps, separating reference accuracy, requested residuals, owned buffers and recomputation.

## Methods

- [Implicit differentiation and adjoint methods](<https://hrkoyama.github.io/numerical-methods-atlas/methods/adjoint/?lang=en>)

  Thomas solves B u_next=u_current+dt theta b; reverse solves use B transpose. Save checkpoints every16steps and replay one block in the original order. Serialize and release the full trajectory before the separate checkpoint ownership window.
- [Backward Euler](<https://hrkoyama.github.io/numerical-methods-atlas/methods/backward-euler/?lang=en>)

  Thomas solves B u_next=u_current+dt theta b; reverse solves use B transpose. Save checkpoints every16steps and replay one block in the original order. Serialize and release the full trajectory before the separate checkpoint ownership window.
- [Thomas tridiagonal elimination](<https://hrkoyama.github.io/numerical-methods-atlas/methods/thomas/?lang=en>)

  Thomas solves B u_next=u_current+dt theta b; reverse solves use B transpose. Save checkpoints every16steps and replay one block in the original order. Serialize and release the full trajectory before the separate checkpoint ownership window.
- [Implicit differentiation and adjoint methods](<https://hrkoyama.github.io/numerical-methods-atlas/methods/adjoint/?lang=en>)

  Analytic Jv, Poisson-Thomas right preconditioning and the preserved GMRES body solve tangents/adjoints. Save every rtol, returned candidate, true residual, termination and roundoff scale. Qualify the discrete oracle through shooting and separate high-precision Thomas-Newton. R2 uses a general near-neighbor-difference association in binary64 Jv; the original nonlinear residual,GMRES and tolerances are unchanged. R3 expands only stateNewtoncorrections ashi+lo,direct9productresidual and3productstateupdate. Physicalstates stayfloat64;derivative/adjointGMRES staysordinary.
- [Restarted GMRES](<https://hrkoyama.github.io/numerical-methods-atlas/methods/gmres/?lang=en>)

  Analytic Jv, Poisson-Thomas right preconditioning and the preserved GMRES body solve tangents/adjoints. Save every rtol, returned candidate, true residual, termination and roundoff scale. Qualify the discrete oracle through shooting and separate high-precision Thomas-Newton. R2 uses a general near-neighbor-difference association in binary64 Jv; the original nonlinear residual,GMRES and tolerances are unchanged. R3 expands only stateNewtoncorrections ashi+lo,direct9productresidual and3productstateupdate. Physicalstates stayfloat64;derivative/adjointGMRES staysordinary.
- [Centered spatial difference](<https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en>)

  Analytic Jv, Poisson-Thomas right preconditioning and the preserved GMRES body solve tangents/adjoints. Save every rtol, returned candidate, true residual, termination and roundoff scale. Qualify the discrete oracle through shooting and separate high-precision Thomas-Newton. R2 uses a general near-neighbor-difference association in binary64 Jv; the original nonlinear residual,GMRES and tolerances are unchanged. R3 expands only stateNewtoncorrections ashi+lo,direct9productresidual and3productstateupdate. Physicalstates stayfloat64;derivative/adjointGMRES staysordinary.
- [Armijo-damped Newton](<https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=en>)

  Analytic Jv, Poisson-Thomas right preconditioning and the preserved GMRES body solve tangents/adjoints. Save every rtol, returned candidate, true residual, termination and roundoff scale. Qualify the discrete oracle through shooting and separate high-precision Thomas-Newton. R2 uses a general near-neighbor-difference association in binary64 Jv; the original nonlinear residual,GMRES and tolerances are unchanged. R3 expands only stateNewtoncorrections ashi+lo,direct9productresidual and3productstateupdate. Physicalstates stayfloat64;derivative/adjointGMRES staysordinary.
- [Implicit differentiation and adjoint methods](<https://hrkoyama.github.io/numerical-methods-atlas/methods/adjoint/?lang=en>)

  Bv uses local gather and B transpose scatter-add. Primary solves use Jv without an n-by-m matrix. One shared Poisson factor serves the one/three-objective runs on the same state. Dense hats and m tangent RHS are allowed only in the separate reference window. R2 uses a general near-neighbor-difference association in binary64 Jv; the original nonlinear residual,GMRES and tolerances are unchanged. R3 expands only stateNewtoncorrections ashi+lo,direct9productresidual and3productstateupdate. Physicalstates stayfloat64;derivative/adjointGMRES staysordinary.
- [Restarted GMRES](<https://hrkoyama.github.io/numerical-methods-atlas/methods/gmres/?lang=en>)

  Bv uses local gather and B transpose scatter-add. Primary solves use Jv without an n-by-m matrix. One shared Poisson factor serves the one/three-objective runs on the same state. Dense hats and m tangent RHS are allowed only in the separate reference window. R2 uses a general near-neighbor-difference association in binary64 Jv; the original nonlinear residual,GMRES and tolerances are unchanged. R3 expands only stateNewtoncorrections ashi+lo,direct9productresidual and3productstateupdate. Physicalstates stayfloat64;derivative/adjointGMRES staysordinary.
- [Centered spatial difference](<https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en>)

  Bv uses local gather and B transpose scatter-add. Primary solves use Jv without an n-by-m matrix. One shared Poisson factor serves the one/three-objective runs on the same state. Dense hats and m tangent RHS are allowed only in the separate reference window. R2 uses a general near-neighbor-difference association in binary64 Jv; the original nonlinear residual,GMRES and tolerances are unchanged. R3 expands only stateNewtoncorrections ashi+lo,direct9productresidual and3productstateupdate. Physicalstates stayfloat64;derivative/adjointGMRES staysordinary.
- [Armijo-damped Newton](<https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=en>)

  Bv uses local gather and B transpose scatter-add. Primary solves use Jv without an n-by-m matrix. One shared Poisson factor serves the one/three-objective runs on the same state. Dense hats and m tangent RHS are allowed only in the separate reference window. R2 uses a general near-neighbor-difference association in binary64 Jv; the original nonlinear residual,GMRES and tolerances are unchanged. R3 expands only stateNewtoncorrections ashi+lo,direct9productresidual and3productstateupdate. Physicalstates stayfloat64;derivative/adjointGMRES staysordinary.
- [Implicit differentiation and adjoint methods](<https://hrkoyama.github.io/numerical-methods-atlas/methods/adjoint/?lang=en>)
- [Backward Euler](<https://hrkoyama.github.io/numerical-methods-atlas/methods/backward-euler/?lang=en>)
- [Thomas tridiagonal elimination](<https://hrkoyama.github.io/numerical-methods-atlas/methods/thomas/?lang=en>)
- [Restarted GMRES](<https://hrkoyama.github.io/numerical-methods-atlas/methods/gmres/?lang=en>)
- [Centered spatial difference](<https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en>)
- [Armijo-damped Newton](<https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=en>)

## Equations

- [Heat / diffusion equation](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#heat-en>)

  A representative constant-diffusivity form: mode decay, time integration and boundaries. Dimensionless x in [0,1], fixed zero Dirichlet endpoints, 7/15 interior nodes and 64/128/256 time steps to T=.1; kappa=.1 and theta=.2. Coordinate transposes include explicit objective h weights.
- [Bratu nonlinear boundary-value problem](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bratu-en>)

  The convention here is −u″=λ exp(u). Newton–Krylov checks cover residuals, refinement and inner-solver failures. 31/63 interior nodes; gaps .1/.01/.001 below the discrete-fold anchor. Every state starts at zero on the lower branch. Parse each lambda string once to binary float; the Decimal oracle evaluates exactly that float.
- [Bratu nonlinear boundary-value problem](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bratu-en>)

  The convention here is −u″=λ exp(u). Newton–Krylov checks cover residuals, refinement and inner-solver failures. 63 interior nodes; a(x)=2+B theta with theta=.2sin(2pi xi)+.1cos(pi xi). State/sensitivity have fixed zero Dirichlet endpoints; endpoint coefficient controls are not fixed zero.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/diffusion-discrete-adjoint/?lang=en#diffusion-discrete-adjoint-en-algorithm>)

  Thomas solves B u_next=u_current+dt theta b; reverse solves use B transpose. Save checkpoints every16steps and replay one block in the original order. Serialize and release the full trajectory before the separate checkpoint ownership window.
- [Heat / diffusion equation](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#heat-en>)

  A representative constant-diffusivity form: mode decay, time integration and boundaries.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-sensitivity/?lang=en#bratu-fold-sensitivity-en-algorithm>)

  Analytic Jv, Poisson-Thomas right preconditioning and the preserved GMRES body solve tangents/adjoints. Save every rtol, returned candidate, true residual, termination and roundoff scale. Qualify the discrete oracle through shooting and separate high-precision Thomas-Newton. R2 uses a general near-neighbor-difference association in binary64 Jv; the original nonlinear residual,GMRES and tolerances are unchanged. R3 expands only stateNewtoncorrections ashi+lo,direct9productresidual and3productstateupdate. Physicalstates stayfloat64;derivative/adjointGMRES staysordinary.
- [Bratu nonlinear boundary-value problem](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bratu-en>)

  The convention here is −u″=λ exp(u). Newton–Krylov checks cover residuals, refinement and inner-solver failures.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-distributed-vjp/?lang=en#bratu-distributed-vjp-en-algorithm>)

  Bv uses local gather and B transpose scatter-add. Primary solves use Jv without an n-by-m matrix. One shared Poisson factor serves the one/three-objective runs on the same state. Dense hats and m tangent RHS are allowed only in the separate reference window. R2 uses a general near-neighbor-difference association in binary64 Jv; the original nonlinear residual,GMRES and tolerances are unchanged. R3 expands only stateNewtoncorrections ashi+lo,direct9productresidual and3productstateupdate. Physicalstates stayfloat64;derivative/adjointGMRES staysordinary.

## Problem figures

- [Discrete diffusion adjoint and checkpoint replay](<https://hrkoyama.github.io/numerical-methods-atlas/problems/diffusion-discrete-adjoint/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/results/diffusion-discrete-adjoint-preview.png
- [Bratu sensitivity near the discrete fold](<https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-sensitivity/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/results/bratu-fold-sensitivity-preview.png
- [Matrix-free VJP for distributed Bratu coefficients](<https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-distributed-vjp/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/results/bratu-distributed-vjp-preview.png
- [Discrete diffusion adjoint and checkpoint replay](<https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/results/diffusion-discrete-adjoint.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/results/diffusion-discrete-adjoint.png
- [Bratu sensitivity near the discrete fold](<https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/results/bratu-fold-sensitivity.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/results/bratu-fold-sensitivity.png
- [Matrix-free VJP for distributed Bratu coefficients](<https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/results/bratu-distributed-vjp.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/results/bratu-distributed-vjp.png

## Exact / reference solutions

- [Discrete diffusion adjoint and checkpoint replay — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/diffusion-discrete-adjoint/?lang=en#references-en>)

  Pre-run freeze:independent67-check reference qualification, then shared32pytest and141fixed group gates. Retain all inputs, tolerances and failures. Actual outcomes are recorded in the bundled result/verification. Initial attempt retained32passing tests and59diffusion/45fold gates before an unmet inner target. R2 general Jv association has separate96component checks; this does not imply primary success. R2 primary failure is also retained. R3 state-onlyhi+lo has separate20component checks;actual three-caseoutcomes are inresult/verification.
- [Backward-Euler discrete modes and time-exact semidiscrete diffusion references](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-diffusion-discrete-adjoint-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference Dimensionless x in [0,1] with zero Dirichlet data, kappa = .1, theta = .2 and T = .1. Use 7/15 interior nodes and 64/128/256 time steps. The objective has an h-weighted terminal error and specified quadratic penalties. Fixed-step discrete adjoints, not CVODES or an optimal checkpoint schedule. The40n limit counts unique evolving state/adjoint/RHS/solve-scratch elements. Static factors/model arrays are separately listed and included in total bytes. Validation/NPZ assembly follows the ownership windows; this is not RSS.
- [Bratu sensitivity near the discrete fold — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-sensitivity/?lang=en#references-en>)

  Pre-run freeze:independent67-check reference qualification, then shared32pytest and141fixed group gates. Retain all inputs, tolerances and failures. Actual outcomes are recorded in the bundled result/verification. Initial attempt retained32passing tests and59diffusion/45fold gates before an unmet inner target. R2 general Jv association has separate96component checks; this does not imply primary success. R2 primary failure is also retained. R3 state-onlyhi+lo has separate20component checks;actual three-caseoutcomes are inresult/verification. Fullownership evidence is in the JSONL file/byteoffset/recordSHA referenced by each linear_memory summary;only compact summaries enter case metrics.
- [Discrete Bratu shooting, tangent and adjoint references near a fold](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-bratu-fold-sensitivity-en>)
  relation: same-problem
  reference_kind: numerical-reference

  Finite-grid numerical reference One-dimensional Dirichlet Bratu with 31/63 interior nodes. Fixed gaps .1/.01/.001 below the discrete-fold anchor use lower-branch states. Each lambda string is converted once to binary64 and that exact value is passed to the high-precision reference. The continuum fold is not the discrete fold. rtol1e-4/1e-8 targets are required; requested1e-12 is observational and unmet is never called converged. Independent accuracy of the returned gradient is a separate gate. Eigenvalue/roundoff scales are floating diagnostics, not certified intervals. Bratu J is symmetric; the nonsymmetric transpose is a separate operator control. The retained /solver/gmres/retention_adaptation text is historicalR1/R2;the newcontract explicitly overrides it for mixed-precisionSTATEsolves. ProjectedUNMET is separatelysaved.
- [Matrix-free VJP for distributed Bratu coefficients — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-distributed-vjp/?lang=en#references-en>)

  Pre-run freeze:independent67-check reference qualification, then shared32pytest and141fixed group gates. Retain all inputs, tolerances and failures. Actual outcomes are recorded in the bundled result/verification. Initial attempt retained32passing tests and59diffusion/45fold gates before an unmet inner target. R2 general Jv association has separate96component checks; this does not imply primary success. R2 primary failure is also retained. R3 state-onlyhi+lo has separate20component checks;actual three-caseoutcomes are inresult/verification. Fullownership evidence is in the JSONL file/byteoffset/recordSHA referenced by each linear_memory summary;only compact summaries enter case metrics.
- [Independent dense sensitivities and matrix-free VJPs for distributed Bratu coefficients](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-bratu-distributed-vjp-en>)
  relation: same-problem
  reference_kind: numerical-reference

  Finite-grid numerical reference A one-dimensional zero-Dirichlet problem with 63 interior nodes. The coefficient a(x)=2+Btheta uses 8/16/32 linear-hat controls and stays between 1.7 and 2.3 in the fixed main cases. Endpoint coefficient controls are not zeroed like state Dirichlet values. Derivative verification at the same discrete state, not independent physical-PDE truth or general AD. Persistent arrays and fixed Krylov workspace inventories are not RSS measurements. For m=2, theta endpoints are[a-b-2,a+b-2], distinct from physical coefficient endpoints[a-b,a+b]. The retained /solver/gmres/retention_adaptation text is historicalR1/R2;the newcontract explicitly overrides it for mixed-precisionSTATEsolves. ProjectedUNMET is separatelysaved.
- [Backward-Euler discrete modes and time-exact semidiscrete diffusion references](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-diffusion-discrete-adjoint-en>)
  reference_kind: analytic

  Analytic reference Dimensionless x in [0,1] with zero Dirichlet data, kappa = .1, theta = .2 and T = .1. Use 7/15 interior nodes and 64/128/256 time steps. The objective has an h-weighted terminal error and specified quadratic penalties.
- [Discrete Bratu shooting, tangent and adjoint references near a fold](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-bratu-fold-sensitivity-en>)
  reference_kind: numerical-reference

  Finite-grid numerical reference One-dimensional Dirichlet Bratu with 31/63 interior nodes. Fixed gaps .1/.01/.001 below the discrete-fold anchor use lower-branch states. Each lambda string is converted once to binary64 and that exact value is passed to the high-precision reference.
- [Independent dense sensitivities and matrix-free VJPs for distributed Bratu coefficients](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-bratu-distributed-vjp-en>)
  reference_kind: numerical-reference

  Finite-grid numerical reference A one-dimensional zero-Dirichlet problem with 63 interior nodes. The coefficient a(x)=2+Btheta uses 8/16/32 linear-hat controls and stays between 1.7 and 2.3 in the fixed main cases. Endpoint coefficient controls are not zeroed like state Dirichlet values.
- [Discrete diffusion adjoint and checkpoint replay — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/diffusion-discrete-adjoint/?lang=en#diffusion-discrete-adjoint-en-validation>)

  Pre-run freeze:independent67-check reference qualification, then shared32pytest and141fixed group gates. Retain all inputs, tolerances and failures. Actual outcomes are recorded in the bundled result/verification. Initial attempt retained32passing tests and59diffusion/45fold gates before an unmet inner target. R2 general Jv association has separate96component checks; this does not imply primary success. R2 primary failure is also retained. R3 state-onlyhi+lo has separate20component checks;actual three-caseoutcomes are inresult/verification.
- [Backward-Euler discrete modes and time-exact semidiscrete diffusion references](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-diffusion-discrete-adjoint-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference Dimensionless x in [0,1] with zero Dirichlet data, kappa = .1, theta = .2 and T = .1. Use 7/15 interior nodes and 64/128/256 time steps. The objective has an h-weighted terminal error and specified quadratic penalties. Fixed-step discrete adjoints, not CVODES or an optimal checkpoint schedule. The40n limit counts unique evolving state/adjoint/RHS/solve-scratch elements. Static factors/model arrays are separately listed and included in total bytes. Validation/NPZ assembly follows the ownership windows; this is not RSS.
- [Bratu sensitivity near the discrete fold — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-sensitivity/?lang=en#bratu-fold-sensitivity-en-validation>)

  Pre-run freeze:independent67-check reference qualification, then shared32pytest and141fixed group gates. Retain all inputs, tolerances and failures. Actual outcomes are recorded in the bundled result/verification. Initial attempt retained32passing tests and59diffusion/45fold gates before an unmet inner target. R2 general Jv association has separate96component checks; this does not imply primary success. R2 primary failure is also retained. R3 state-onlyhi+lo has separate20component checks;actual three-caseoutcomes are inresult/verification. Fullownership evidence is in the JSONL file/byteoffset/recordSHA referenced by each linear_memory summary;only compact summaries enter case metrics.
- [Discrete Bratu shooting, tangent and adjoint references near a fold](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-bratu-fold-sensitivity-en>)
  relation: same-problem
  reference_kind: numerical-reference

  Finite-grid numerical reference One-dimensional Dirichlet Bratu with 31/63 interior nodes. Fixed gaps .1/.01/.001 below the discrete-fold anchor use lower-branch states. Each lambda string is converted once to binary64 and that exact value is passed to the high-precision reference. The continuum fold is not the discrete fold. rtol1e-4/1e-8 targets are required; requested1e-12 is observational and unmet is never called converged. Independent accuracy of the returned gradient is a separate gate. Eigenvalue/roundoff scales are floating diagnostics, not certified intervals. Bratu J is symmetric; the nonsymmetric transpose is a separate operator control. The retained /solver/gmres/retention_adaptation text is historicalR1/R2;the newcontract explicitly overrides it for mixed-precisionSTATEsolves. ProjectedUNMET is separatelysaved.
- [Matrix-free VJP for distributed Bratu coefficients — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-distributed-vjp/?lang=en#bratu-distributed-vjp-en-validation>)

  Pre-run freeze:independent67-check reference qualification, then shared32pytest and141fixed group gates. Retain all inputs, tolerances and failures. Actual outcomes are recorded in the bundled result/verification. Initial attempt retained32passing tests and59diffusion/45fold gates before an unmet inner target. R2 general Jv association has separate96component checks; this does not imply primary success. R2 primary failure is also retained. R3 state-onlyhi+lo has separate20component checks;actual three-caseoutcomes are inresult/verification. Fullownership evidence is in the JSONL file/byteoffset/recordSHA referenced by each linear_memory summary;only compact summaries enter case metrics.
- [Independent dense sensitivities and matrix-free VJPs for distributed Bratu coefficients](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-bratu-distributed-vjp-en>)
  relation: same-problem
  reference_kind: numerical-reference

  Finite-grid numerical reference A one-dimensional zero-Dirichlet problem with 63 interior nodes. The coefficient a(x)=2+Btheta uses 8/16/32 linear-hat controls and stays between 1.7 and 2.3 in the fixed main cases. Endpoint coefficient controls are not zeroed like state Dirichlet values. Derivative verification at the same discrete state, not independent physical-PDE truth or general AD. Persistent arrays and fixed Krylov workspace inventories are not RSS measurements. For m=2, theta endpoints are[a-b-2,a+b-2], distinct from physical coefficient endpoints[a-b,a+b]. The retained /solver/gmres/retention_adaptation text is historicalR1/R2;the newcontract explicitly overrides it for mixed-precisionSTATEsolves. ProjectedUNMET is separatelysaved.

## Code and validation

- [Discrete diffusion adjoint and checkpoint replay](<https://hrkoyama.github.io/numerical-methods-atlas/validation/diffusion-discrete-adjoint/?lang=en>)
  availability: run

  Reverse the actual backward-Euler map and compare tangent derivatives, independent high-precision modes and block replay.
- [Bratu sensitivity near the discrete fold](<https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-sensitivity/?lang=en>)
  availability: run

  At six fixed points approaching the discrete Bratu fold, separate state error from linear-solve tolerance and compare against independent shooting gradients.
- [Matrix-free VJP for distributed Bratu coefficients](<https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-distributed-vjp/?lang=en>)
  availability: run

  Represent8/16/32 spatial controls with two local hat weights per node; compare objective-wise adjoint VJPs with a separate full-sensitivity reference.
