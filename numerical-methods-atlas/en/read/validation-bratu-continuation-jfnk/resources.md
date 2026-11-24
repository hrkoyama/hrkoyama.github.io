# Bratu fold continuation and Jacobian-free Newton-Krylov

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-bratu-continuation-jfnk/

Resources explicitly registered to the methods, problems and executions of this chapter. The same one-dimensional Bratu problem compares fold continuation and matrix-free iteration against an independently evaluated analytic family.

## Methods

- [Weighted pseudo-arclength continuation](<https://hrkoyama.github.io/numerical-methods-atlas/methods/pseudo-arclength-continuation/?lang=en>)
- [Jacobian-free Newton-Krylov](<https://hrkoyama.github.io/numerical-methods-atlas/methods/jacobian-free-newton-krylov/?lang=en>)
- [Weighted pseudo-arclength continuation](<https://hrkoyama.github.io/numerical-methods-atlas/methods/pseudo-arclength-continuation/?lang=en>)

  Use a unit tangent in h-sum(du squared)+d-lambda squared, a predictor and a tangent-hyperplane Newton corrector. A separate augmented system locates the fold and a normalized null vector. This case deliberately assembles sparse Jacobians.
- [Armijo-damped Newton](<https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=en>)

  Use a unit tangent in h-sum(du squared)+d-lambda squared, a predictor and a tangent-hyperplane Newton corrector. A separate augmented system locates the fold and a normalized null vector. This case deliberately assembles sparse Jacobians.
- [Centered spatial difference](<https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en>)

  Use a unit tangent in h-sum(du squared)+d-lambda squared, a predictor and a tangent-hyperplane Newton corrector. A separate augmented system locates the fold and a normalized null vector. This case deliberately assembles sparse Jacobians.
- [Jacobian-free Newton-Krylov](<https://hrkoyama.github.io/numerical-methods-atlas/methods/jacobian-free-newton-krylov/?lang=en>)

  Use analytic Jv, a two-residual central difference, or one-direction forward AD. Apply a Poisson Thomas right preconditioner with two-pass reorthogonalized GMRES/Givens. Start eta=.3, then clamp .9*(Fk/Fk-1)^1.5 to [.001,.5]. This is an explicit EW Choice2-style variant, not the paper’s full safeguards or PETSc defaults.
- [Restarted GMRES](<https://hrkoyama.github.io/numerical-methods-atlas/methods/gmres/?lang=en>)

  Use analytic Jv, a two-residual central difference, or one-direction forward AD. Apply a Poisson Thomas right preconditioner with two-pass reorthogonalized GMRES/Givens. Start eta=.3, then clamp .9*(Fk/Fk-1)^1.5 to [.001,.5]. This is an explicit EW Choice2-style variant, not the paper’s full safeguards or PETSc defaults.
- [Thomas tridiagonal elimination](<https://hrkoyama.github.io/numerical-methods-atlas/methods/thomas/?lang=en>)

  Use analytic Jv, a two-residual central difference, or one-direction forward AD. Apply a Poisson Thomas right preconditioner with two-pass reorthogonalized GMRES/Givens. Start eta=.3, then clamp .9*(Fk/Fk-1)^1.5 to [.001,.5]. This is an explicit EW Choice2-style variant, not the paper’s full safeguards or PETSc defaults.
- [Automatic differentiation](<https://hrkoyama.github.io/numerical-methods-atlas/methods/automatic-differentiation/?lang=en>)

  Use analytic Jv, a two-residual central difference, or one-direction forward AD. Apply a Poisson Thomas right preconditioner with two-pass reorthogonalized GMRES/Givens. Start eta=.3, then clamp .9*(Fk/Fk-1)^1.5 to [.001,.5]. This is an explicit EW Choice2-style variant, not the paper’s full safeguards or PETSc defaults.
- [Centered spatial difference](<https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en>)

  Use analytic Jv, a two-residual central difference, or one-direction forward AD. Apply a Poisson Thomas right preconditioner with two-pass reorthogonalized GMRES/Givens. Start eta=.3, then clamp .9*(Fk/Fk-1)^1.5 to [.001,.5]. This is an explicit EW Choice2-style variant, not the paper’s full safeguards or PETSc defaults.
- [Armijo-damped Newton](<https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=en>)
- [Centered spatial difference](<https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en>)
- [Restarted GMRES](<https://hrkoyama.github.io/numerical-methods-atlas/methods/gmres/?lang=en>)
- [Thomas tridiagonal elimination](<https://hrkoyama.github.io/numerical-methods-atlas/methods/thomas/?lang=en>)
- [Automatic differentiation](<https://hrkoyama.github.io/numerical-methods-atlas/methods/automatic-differentiation/?lang=en>)

## Equations

- [Bratu nonlinear boundary-value problem](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bratu-en>)

  The convention here is −u″=λ exp(u). Newton–Krylov checks cover residuals, refinement and inner-solver failures. Dimensionless x in [0,1] with zero Dirichlet endpoints and 31/63/127 interior nodes. Take 80 fixed ds=0.1 steps from the zero solution. Correct both branches at lambda=2; lambda=4 is a deliberate discrete no-solution control. Pseudo-arclength is not physical time.
- [Bratu nonlinear boundary-value problem](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bratu-en>)

  The convention here is −u″=λ exp(u). Newton–Krylov checks cover residuals, refinement and inner-solver failures. The same dimensionless one-dimensional Dirichlet problem at lambda=3, 63/127 interior nodes, starting from zero or 4sin(pi*x). Twelve mode/grid/branch solves plus one analytic-Jv constant-eta=1e-8 control. GMRES restart24/max96, at most 24 Newton steps and nonlinear tolerance1e-9.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-continuation/?lang=en#bratu-fold-continuation-en-algorithm>)

  Use a unit tangent in h-sum(du squared)+d-lambda squared, a predictor and a tangent-hyperplane Newton corrector. A separate augmented system locates the fold and a normalized null vector. This case deliberately assembles sparse Jacobians.
- [Bratu nonlinear boundary-value problem](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bratu-en>)

  The convention here is −u″=λ exp(u). Newton–Krylov checks cover residuals, refinement and inner-solver failures.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-matrix-free-jfnk/?lang=en#bratu-matrix-free-jfnk-en-algorithm>)

  Use analytic Jv, a two-residual central difference, or one-direction forward AD. Apply a Poisson Thomas right preconditioner with two-pass reorthogonalized GMRES/Givens. Start eta=.3, then clamp .9*(Fk/Fk-1)^1.5 to [.001,.5]. This is an explicit EW Choice2-style variant, not the paper’s full safeguards or PETSc defaults.

## Problem figures

- [Crossing the Bratu fold with pseudo-arclength continuation](<https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-continuation/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/results/bratu-fold-continuation-preview.png
- [Jacobian-free Newton–Krylov with analytic, central-FD and directional-AD products](<https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-matrix-free-jfnk/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/results/bratu-matrix-free-jfnk-preview.png
- [Crossing the Bratu fold with pseudo-arclength continuation](<https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/results/bratu-fold-continuation.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/results/bratu-fold-continuation.png
- [Jacobian-free Newton–Krylov with analytic, central-FD and directional-AD products](<https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/results/bratu-matrix-free-jfnk.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/results/bratu-matrix-free-jfnk.png

## Exact / reference solutions

- [Crossing the Bratu fold with pseudo-arclength continuation — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-continuation/?lang=en#references-en>)

  The preserved R3 run passed the shared 27 pytest tests and this case’s 67 fixed gates. Discrete residuals, tangent orientation/normalization, fold/null/transversality conditions, an independent Decimal80 family and fixed three-grid errors are checked separately.
- [Crossing the Bratu fold with pseudo-arclength continuation](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-bratu-fold-continuation-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference Same dimensionless1D Bratu on[0,1] with zero endpoints. The continuous family is evaluated independently in Decimal80;it is not an exact discrete root or Newton/GMRES trajectory. A small one-dimensional simple fold only. The whole-curve family comparison uses the computed midpoint as its family coordinate and is distinct from the independent fixed-lambda profile checks. The continuum fold is not an exact discrete solution. No general bifurcation-tracking or large-scale performance claim.
- [Jacobian-free Newton–Krylov with analytic, central-FD and directional-AD products — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-matrix-free-jfnk/?lang=en#references-en>)

  The preserved R3 run passed the shared27 pytest tests and this case’s129 fixed gates: nonzero analytic Jv qualification, discrete residuals, independent analytic branches, mode agreement, forcing, evaluation ledgers, Krylov storage, Armijo and the constant-eta control. Analytic forcing validation is counted separately and does not steer FD/AD iterations.
- [Jacobian-free Newton–Krylov with analytic, central-FD and directional-AD products](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-bratu-matrix-free-jfnk-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference Same dimensionless1D Bratu on[0,1] with zero endpoints. The continuous family is evaluated independently in Decimal80;it is not an exact discrete root or Newton/GMRES trajectory. An educational small1D BVP. AD covers only elementary arithmetic, exp and linear boundary padding. Small Hessenberg matrices and Krylov bases are stored. The fixed eta floor precludes claiming the unmodified EW asymptotic theorem. No general-AD/PETSc equivalence, speedup or global-convergence guarantee.
- [Crossing the Bratu fold with pseudo-arclength continuation](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-bratu-fold-continuation-en>)
  reference_kind: analytic

  Analytic reference Same dimensionless1D Bratu on[0,1] with zero endpoints. The continuous family is evaluated independently in Decimal80;it is not an exact discrete root or Newton/GMRES trajectory.
- [Jacobian-free Newton–Krylov with analytic, central-FD and directional-AD products](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-bratu-matrix-free-jfnk-en>)
  reference_kind: analytic

  Analytic reference Same dimensionless1D Bratu on[0,1] with zero endpoints. The continuous family is evaluated independently in Decimal80;it is not an exact discrete root or Newton/GMRES trajectory.
- [Crossing the Bratu fold with pseudo-arclength continuation — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-continuation/?lang=en#bratu-fold-continuation-en-validation>)

  The preserved R3 run passed the shared 27 pytest tests and this case’s 67 fixed gates. Discrete residuals, tangent orientation/normalization, fold/null/transversality conditions, an independent Decimal80 family and fixed three-grid errors are checked separately.
- [Crossing the Bratu fold with pseudo-arclength continuation](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-bratu-fold-continuation-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference Same dimensionless1D Bratu on[0,1] with zero endpoints. The continuous family is evaluated independently in Decimal80;it is not an exact discrete root or Newton/GMRES trajectory. A small one-dimensional simple fold only. The whole-curve family comparison uses the computed midpoint as its family coordinate and is distinct from the independent fixed-lambda profile checks. The continuum fold is not an exact discrete solution. No general bifurcation-tracking or large-scale performance claim.
- [Jacobian-free Newton–Krylov with analytic, central-FD and directional-AD products — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-matrix-free-jfnk/?lang=en#bratu-matrix-free-jfnk-en-validation>)

  The preserved R3 run passed the shared27 pytest tests and this case’s129 fixed gates: nonzero analytic Jv qualification, discrete residuals, independent analytic branches, mode agreement, forcing, evaluation ledgers, Krylov storage, Armijo and the constant-eta control. Analytic forcing validation is counted separately and does not steer FD/AD iterations.
- [Jacobian-free Newton–Krylov with analytic, central-FD and directional-AD products](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-bratu-matrix-free-jfnk-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference Same dimensionless1D Bratu on[0,1] with zero endpoints. The continuous family is evaluated independently in Decimal80;it is not an exact discrete root or Newton/GMRES trajectory. An educational small1D BVP. AD covers only elementary arithmetic, exp and linear boundary padding. Small Hessenberg matrices and Krylov bases are stored. The fixed eta floor precludes claiming the unmodified EW asymptotic theorem. No general-AD/PETSc equivalence, speedup or global-convergence guarantee.

## Code and validation

- [Crossing the Bratu fold with pseudo-arclength continuation](<https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-continuation/?lang=en>)
  availability: run

  Follow the lower and upper branches of the same one-dimensional Bratu boundary-value problem; check tangents, the fold and spatial error against an independent analytic family.
- [Jacobian-free Newton–Krylov with analytic, central-FD and directional-AD products](<https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-matrix-free-jfnk/?lang=en>)
  availability: run

  Solve both Bratu branches with three Jv choices without assembling the nonlinear Jacobian; retain forcing, actual residuals and evaluation counts.
- [Weighted pseudo-arclength continuation — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/pseudo-arclength-continuation/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [Jacobian-free Newton-Krylov — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/jacobian-free-newton-krylov/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
