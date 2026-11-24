# Reverse mode, HVPs and nonsmooth branches

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-reverse-higher-ad/

Resources explicitly registered to the methods, problems and executions of this chapter. Independent hand-derived references check a small original tape, separating fixed-state partials, implicit total derivatives and executed branches.

## Methods

- [Automatic differentiation](<https://hrkoyama.github.io/numerical-methods-atlas/methods/automatic-differentiation/?lang=en>)

  Accumulate cotangents in reverse topological order with a separate forward directional path.
- [Automatic differentiation](<https://hrkoyama.github.io/numerical-methods-atlas/methods/automatic-differentiation/?lang=en>)

  Transport values, tangents, cotangents and cotangent tangents; solve F/R1/R2 for implicit derivatives.
- [Automatic differentiation](<https://hrkoyama.github.io/numerical-methods-atlas/methods/automatic-differentiation/?lang=en>)

  Report strict nondifferentiability explicitly and record the literal top-of-loop stopping branch.
- [Automatic differentiation](<https://hrkoyama.github.io/numerical-methods-atlas/methods/automatic-differentiation/?lang=en>)

## Equations

- [Finite-dimensional nonlinear maps, roots and differential actions](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#finite-dimensional-nonlinear-map-en>)

  Roots, JVP/VJP, HVP and branch conventions for finite algebraic maps. The variable count n is not a spatial dimension, and a classical derivative is not imposed at nonsmooth points. Small fixed real dimensionless inputs; assumptions and scope are limited to the matching contract.
- [Bratu nonlinear boundary-value problem](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bratu-en>)

  The convention here is −u″=λ exp(u). Newton–Krylov checks cover residuals, refinement and inner-solver failures. Small fixed real dimensionless inputs; assumptions and scope are limited to the matching contract.
- [Finite-dimensional nonlinear maps, roots and differential actions](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#finite-dimensional-nonlinear-map-en>)

  Roots, JVP/VJP, HVP and branch conventions for finite algebraic maps. The variable count n is not a spatial dimension, and a classical derivative is not imposed at nonsmooth points. Small fixed real dimensionless inputs; assumptions and scope are limited to the matching contract.
- [Bratu nonlinear boundary-value problem](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bratu-en>)

  The convention here is −u″=λ exp(u). Newton–Krylov checks cover residuals, refinement and inner-solver failures. Small fixed real dimensionless inputs; assumptions and scope are limited to the matching contract.
- [Finite-dimensional nonlinear maps, roots and differential actions](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#finite-dimensional-nonlinear-map-en>)

  Roots, JVP/VJP, HVP and branch conventions for finite algebraic maps. The variable count n is not a spatial dimension, and a classical derivative is not imposed at nonsmooth points. Small fixed real dimensionless inputs; assumptions and scope are limited to the matching contract.
- [Finite-dimensional nonlinear maps, roots and differential actions](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#finite-dimensional-nonlinear-map-en>)

  Roots, JVP/VJP, HVP and branch conventions for finite algebraic maps. The variable count n is not a spatial dimension, and a classical derivative is not imposed at nonsmooth points.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/reverse-vjp-duality/?lang=en#reverse-vjp-duality-en-algorithm>)

  Accumulate cotangents in reverse topological order with a separate forward directional path.
- [Bratu nonlinear boundary-value problem](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bratu-en>)

  The convention here is −u″=λ exp(u). Newton–Krylov checks cover residuals, refinement and inner-solver failures.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/hessian-vector-products/?lang=en#hessian-vector-products-en-algorithm>)

  Transport values, tangents, cotangents and cotangent tangents; solve F/R1/R2 for implicit derivatives.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/kink-branch-derivatives/?lang=en#kink-branch-derivatives-en-algorithm>)

  Report strict nondifferentiability explicitly and record the literal top-of-loop stopping branch.

## Problem figures

- [Original reverse-mode VJP and JVP/VJP duality](<https://hrkoyama.github.io/numerical-methods-atlas/problems/reverse-vjp-duality/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/results/reverse-vjp-duality-preview.png
- [Hessian-vector products and fixed-state versus implicit derivatives](<https://hrkoyama.github.io/numerical-methods-atlas/problems/hessian-vector-products/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/results/hessian-vector-products-preview.png
- [Derivative scope at kinks, branches and stopping decisions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/kink-branch-derivatives/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/results/kink-branch-derivatives-preview.png
- [Original reverse-mode VJP and JVP/VJP duality](<https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/results/reverse-vjp-duality.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/results/reverse-vjp-duality.png
- [Hessian-vector products and fixed-state versus implicit derivatives](<https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/results/hessian-vector-products.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/results/hessian-vector-products.png
- [Derivative scope at kinks, branches and stopping decisions](<https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/results/kink-branch-derivatives.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/results/kink-branch-derivatives.png

## Exact / reference solutions

- [Original reverse-mode VJP and JVP/VJP duality — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/reverse-vjp-duality/?lang=en#references-en>)

  Check fixed inputs, independent references, retained candidates and every gate within the same120-second budget. Numerical success and diagnostic nonconvergence are distinct.
- [Independent Jacobians, JVPs and VJPs of discrete nonlinear maps](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-reverse-vjp-duality-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference The fixed R4-to-R3 map includes repeated-index gather[0,0,2] and scalar broadcast. Wide maps and fixed Bratu states have sizes 7 and 31. Euclidean pullbacks and adjoints under specified SPD metrics are distinct. Not a general NumPy/JAX replacement or complex AD system.
- [Hessian-vector products and fixed-state versus implicit derivatives — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/hessian-vector-products/?lang=en#references-en>)

  Check fixed inputs, independent references, retained candidates and every gate within the same120-second budget. Numerical success and diagnostic nonconvergence are distinct.
- [Independent references for fixed-state HVPs and second-order implicit rules](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-hessian-vector-products-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference Use a four-variable dyadic quadratic and fixed-state Bratu energies of sizes 7 and 31. A separate positive implicit branch u²-theta=0 is solved at theta 4 from initial u 3, distinguishing fixed-state partials from total derivatives. No general reduced inverse Hessian or identification of finite Newton traces with implicit derivatives.
- [Derivative scope at kinks, branches and stopping decisions — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/kink-branch-derivatives/?lang=en#references-en>)

  Check fixed inputs, independent references, retained candidates and every gate within the same120-second budget. Numerical success and diagnostic nonconvergence are distinct.
- [Nonsmooth discrete maps: directional derivatives and executed traces](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-kink-branch-derivatives-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference Use seven fixed points and directions ±1 for abs, ReLU, clip and a polynomial branch. The stopped iteration starts at x0 = 0, tests |xk - theta| <= 1/8 before updating and allows at mostfive updates. Theta 1/4, 1/2 and 1 are switching points. An executed-branch derivative is not a universal subgradient or a linear derivative of a nonsmooth map.
- [Independent Jacobians, JVPs and VJPs of discrete nonlinear maps](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-reverse-vjp-duality-en>)
  reference_kind: analytic

  Analytic reference The fixed R4-to-R3 map includes repeated-index gather[0,0,2] and scalar broadcast. Wide maps and fixed Bratu states have sizes 7 and 31. Euclidean pullbacks and adjoints under specified SPD metrics are distinct.
- [Independent references for fixed-state HVPs and second-order implicit rules](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-hessian-vector-products-en>)
  reference_kind: analytic

  Analytic reference Use a four-variable dyadic quadratic and fixed-state Bratu energies of sizes 7 and 31. A separate positive implicit branch u²-theta=0 is solved at theta 4 from initial u 3, distinguishing fixed-state partials from total derivatives.
- [Nonsmooth discrete maps: directional derivatives and executed traces](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-kink-branch-derivatives-en>)
  reference_kind: analytic

  Analytic reference Use seven fixed points and directions ±1 for abs, ReLU, clip and a polynomial branch. The stopped iteration starts at x0 = 0, tests |xk - theta| <= 1/8 before updating and allows at mostfive updates. Theta 1/4, 1/2 and 1 are switching points.
- [Original reverse-mode VJP and JVP/VJP duality — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/reverse-vjp-duality/?lang=en#reverse-vjp-duality-en-validation>)

  Check fixed inputs, independent references, retained candidates and every gate within the same120-second budget. Numerical success and diagnostic nonconvergence are distinct.
- [Independent Jacobians, JVPs and VJPs of discrete nonlinear maps](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-reverse-vjp-duality-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference The fixed R4-to-R3 map includes repeated-index gather[0,0,2] and scalar broadcast. Wide maps and fixed Bratu states have sizes 7 and 31. Euclidean pullbacks and adjoints under specified SPD metrics are distinct. Not a general NumPy/JAX replacement or complex AD system.
- [Hessian-vector products and fixed-state versus implicit derivatives — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/hessian-vector-products/?lang=en#hessian-vector-products-en-validation>)

  Check fixed inputs, independent references, retained candidates and every gate within the same120-second budget. Numerical success and diagnostic nonconvergence are distinct.
- [Independent references for fixed-state HVPs and second-order implicit rules](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-hessian-vector-products-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference Use a four-variable dyadic quadratic and fixed-state Bratu energies of sizes 7 and 31. A separate positive implicit branch u²-theta=0 is solved at theta 4 from initial u 3, distinguishing fixed-state partials from total derivatives. No general reduced inverse Hessian or identification of finite Newton traces with implicit derivatives.
- [Derivative scope at kinks, branches and stopping decisions — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/kink-branch-derivatives/?lang=en#kink-branch-derivatives-en-validation>)

  Check fixed inputs, independent references, retained candidates and every gate within the same120-second budget. Numerical success and diagnostic nonconvergence are distinct.
- [Nonsmooth discrete maps: directional derivatives and executed traces](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-kink-branch-derivatives-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference Use seven fixed points and directions ±1 for abs, ReLU, clip and a polynomial branch. The stopped iteration starts at x0 = 0, tests |xk - theta| <= 1/8 before updating and allows at mostfive updates. Theta 1/4, 1/2 and 1 are switching points. An executed-branch derivative is not a universal subgradient or a linear derivative of a nonsmooth map.

## Code and validation

- [Original reverse-mode VJP and JVP/VJP duality](<https://hrkoyama.github.io/numerical-methods-atlas/validation/reverse-vjp-duality/?lang=en>)
  availability: run

  Check a genuine reverse tape, including repeated-index gather and broadcast, against independent Jacobians.
- [Hessian-vector products and fixed-state versus implicit derivatives](<https://hrkoyama.github.io/numerical-methods-atlas/validation/hessian-vector-products/?lang=en>)
  availability: run

  Check forward-over-reverse HVPs and second-order implicit rules against separate independent references.
- [Derivative scope at kinks, branches and stopping decisions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/kink-branch-derivatives/?lang=en>)
  availability: run

  Distinguish classical, one-sided directional and executed-trace derivatives at fixed kinks and stopping switches.
