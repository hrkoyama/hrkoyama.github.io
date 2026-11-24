# Domain-aware, double-exponential and sparse-grid quadrature

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-quadrature-controls/

Resources explicitly registered to the methods, problems and executions of this chapter. Compare fixed integrals with domain-aware methods, separating estimated errors, actual errors, budget exits and underresolution controls.

## Methods

- [Gaussian and adaptive quadrature](<https://hrkoyama.github.io/numerical-methods-atlas/methods/quadrature/?lang=en>)

  Explicit domain/weight dispatch retains active full_output prefixes. The existing Simpson function is unchanged.
- [Gaussian and adaptive quadrature](<https://hrkoyama.github.io/numerical-methods-atlas/methods/quadrature/?lang=en>)

  Shared15-node G7 degree13/K15 degree23; DE uses stable logarithmic products and full endpoint weights.
- [Gauss–Kronrod G7/K15](<https://hrkoyama.github.io/numerical-methods-atlas/methods/gauss-kronrod/?lang=en>)

  Shared15-node G7 degree13/K15 degree23; DE uses stable logarithmic products and full endpoint weights.
- [Tanh–sinh double-exponential quadrature](<https://hrkoyama.github.io/numerical-methods-atlas/methods/tanh-sinh/?lang=en>)

  Shared15-node G7 degree13/K15 degree23; DE uses stable logarithmic products and full endpoint weights.
- [Gaussian and adaptive quadrature](<https://hrkoyama.github.io/numerical-methods-atlas/methods/quadrature/?lang=en>)

  Canonical dyadic angle keys own shared nodes; signed weights and call ledgers are retained.
- [Smolyak sparse-grid quadrature](<https://hrkoyama.github.io/numerical-methods-atlas/methods/smolyak-sparse-grid/?lang=en>)

  Canonical dyadic angle keys own shared nodes; signed weights and call ledgers are retained.
- [Gaussian and adaptive quadrature](<https://hrkoyama.github.io/numerical-methods-atlas/methods/quadrature/?lang=en>)
- [Gauss–Kronrod G7/K15](<https://hrkoyama.github.io/numerical-methods-atlas/methods/gauss-kronrod/?lang=en>)
- [Tanh–sinh double-exponential quadrature](<https://hrkoyama.github.io/numerical-methods-atlas/methods/tanh-sinh/?lang=en>)
- [Smolyak sparse-grid quadrature](<https://hrkoyama.github.io/numerical-methods-atlas/methods/smolyak-sparse-grid/?lang=en>)

## Equations

- [Finite, improper and multivariate definite integrals](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#definite-integrals-en>)

  Mathematical quadrature problems with explicit domains, weights, singularities and finite transformed-sum conventions. Whole-line Gaussian, two finite frequencies, half-line Fourier and an internal singularity; absolute tolerances1e-6/1e-8/1e-10 and epsrel0.
- [Finite, improper and multivariate definite integrals](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#definite-integrals-en>)

  Mathematical quadrature problems with explicit domains, weights, singularities and finite transformed-sum conventions. Integrate exp(x), x^(-1/3) and -log(x) on[0,1], with h from1/2 to1/16 and cutoffs3/4.
- [Finite, improper and multivariate definite integrals](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#definite-integrals-en>)

  Mathematical quadrature problems with explicit domains, weights, singularities and finite transformed-sum conventions. The integration domain is[0,1]^d for d2/3/4; tensor levels1/2/3 and sparse levels1/2/3/4.
- [Finite, improper and multivariate definite integrals](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#definite-integrals-en>)

  Mathematical quadrature problems with explicit domains, weights, singularities and finite transformed-sum conventions.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/quadpack-domain-selection/?lang=en#quadpack-domain-selection-en-algorithm>)

  Explicit domain/weight dispatch retains active full_output prefixes. The existing Simpson function is unchanged.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/gk15-double-exponential/?lang=en#gk15-double-exponential-en-algorithm>)

  Shared15-node G7 degree13/K15 degree23; DE uses stable logarithmic products and full endpoint weights.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/tensor-smolyak-dimensions/?lang=en#tensor-smolyak-dimensions-en-algorithm>)

  Canonical dyadic angle keys own shared nodes; signed weights and call ledgers are retained.

## Problem figures

- [QUADPACK dispatch and finite Simpson companions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/quadpack-domain-selection/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/results/quadpack-domain-selection-preview.png
- [G7/K15 and finite-interval tanh-sinh](<https://hrkoyama.github.io/numerical-methods-atlas/problems/gk15-double-exponential/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/results/gk15-double-exponential-preview.png
- [Tensor and Smolyak controls in two to four dimensions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/tensor-smolyak-dimensions/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/results/tensor-smolyak-dimensions-preview.png
- [QUADPACK dispatch and finite Simpson companions](<https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/results/quadpack-domain-selection.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/results/quadpack-domain-selection.png
- [G7/K15 and finite-interval tanh-sinh](<https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/results/gk15-double-exponential.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/results/gk15-double-exponential.png
- [Tensor and Smolyak controls in two to four dimensions](<https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/results/tensor-smolyak-dimensions.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/results/tensor-smolyak-dimensions.png

## Exact / reference solutions

- [QUADPACK dispatch and finite Simpson companions — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/quadpack-domain-selection/?lang=en#references-en>)

  Independent analytic interval references and actual callback counts are checked. The finite Gaussian target is an interval, not an invented erf value.
- [QUADPACK dispatch and finite Simpson companions](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-quadpack-domain-selection-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference Whole-line Gaussian, two finite frequencies, half-line Fourier and an internal singularity; absolute tolerances1e-6/1e-8/1e-10 and epsrel0. Singular-node failures and unmet Simpson goals remain visible; error estimates are not general guarantees.
- [G7/K15 and finite-interval tanh-sinh — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/gk15-double-exponential/?lang=en#references-en>)

  Analytic interval references separate total error, continuous tail and finite-window defect.
- [G7/K15 and finite-interval tanh-sinh](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-gk15-double-exponential-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference Integrate exp(x), x^(-1/3) and -log(x) on[0,1], with h from1/2 to1/16 and cutoffs3/4. Half-line exp-sinh and whole-line sinh-sinh are unimplemented; no omitted infinite-grid sum bound is provided.
- [Tensor and Smolyak controls in two to four dimensions — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/tensor-smolyak-dimensions/?lang=en#references-en>)

  Analytic integrals are distinct from companion Delta/combination assembly; interaction underresolution at L<d remains visible.
- [Tensor and Smolyak controls in two to four dimensions](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-tensor-smolyak-dimensions-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference The integration domain is[0,1]^d for d2/3/4; tensor levels1/2/3 and sparse levels1/2/3/4. No general error monotonicity, positive-weight or cost-superiority claim; these are integration coordinates, not a physical PDE space.
- [QUADPACK dispatch and finite Simpson companions](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-quadpack-domain-selection-en>)
  reference_kind: analytic

  Analytic reference Whole-line Gaussian, two finite frequencies, half-line Fourier and an internal singularity; absolute tolerances1e-6/1e-8/1e-10 and epsrel0.
- [G7/K15 and finite-interval tanh-sinh](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-gk15-double-exponential-en>)
  reference_kind: analytic

  Analytic reference Integrate exp(x), x^(-1/3) and -log(x) on[0,1], with h from1/2 to1/16 and cutoffs3/4.
- [Tensor and Smolyak controls in two to four dimensions](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-tensor-smolyak-dimensions-en>)
  reference_kind: analytic

  Analytic reference The integration domain is[0,1]^d for d2/3/4; tensor levels1/2/3 and sparse levels1/2/3/4.
- [QUADPACK dispatch and finite Simpson companions — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/quadpack-domain-selection/?lang=en#quadpack-domain-selection-en-validation>)

  Independent analytic interval references and actual callback counts are checked. The finite Gaussian target is an interval, not an invented erf value.
- [QUADPACK dispatch and finite Simpson companions](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-quadpack-domain-selection-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference Whole-line Gaussian, two finite frequencies, half-line Fourier and an internal singularity; absolute tolerances1e-6/1e-8/1e-10 and epsrel0. Singular-node failures and unmet Simpson goals remain visible; error estimates are not general guarantees.
- [G7/K15 and finite-interval tanh-sinh — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/gk15-double-exponential/?lang=en#gk15-double-exponential-en-validation>)

  Analytic interval references separate total error, continuous tail and finite-window defect.
- [G7/K15 and finite-interval tanh-sinh](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-gk15-double-exponential-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference Integrate exp(x), x^(-1/3) and -log(x) on[0,1], with h from1/2 to1/16 and cutoffs3/4. Half-line exp-sinh and whole-line sinh-sinh are unimplemented; no omitted infinite-grid sum bound is provided.
- [Tensor and Smolyak controls in two to four dimensions — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/tensor-smolyak-dimensions/?lang=en#tensor-smolyak-dimensions-en-validation>)

  Analytic integrals are distinct from companion Delta/combination assembly; interaction underresolution at L<d remains visible.
- [Tensor and Smolyak controls in two to four dimensions](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-tensor-smolyak-dimensions-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference The integration domain is[0,1]^d for d2/3/4; tensor levels1/2/3 and sparse levels1/2/3/4. No general error monotonicity, positive-weight or cost-superiority claim; these are integration coordinates, not a physical PDE space.

## Code and validation

- [QUADPACK dispatch and finite Simpson companions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/quadpack-domain-selection/?lang=en>)
  availability: run

  Fifteen specialized quadratures and fifteen Simpson companions use fixed inputs.
- [G7/K15 and finite-interval tanh-sinh](<https://hrkoyama.github.io/numerical-methods-atlas/validation/gk15-double-exponential/?lang=en>)
  availability: run

  Nine adaptive GK rows and twenty-four fixed DE sums are compared.
- [Tensor and Smolyak controls in two to four dimensions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/tensor-smolyak-dimensions/?lang=en>)
  availability: run

  Forty-two fixed cubatures compare a smooth product and an interaction product.
