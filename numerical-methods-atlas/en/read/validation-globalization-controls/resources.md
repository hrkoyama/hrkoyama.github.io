# Line searches and trust regions from identical starts

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-globalization-controls/

Resources explicitly registered to the methods, problems and executions of this chapter. Original residuals, scaled merit and complete trial ledgers separate roots, stationary nonroots and budget exhaustion.

## Methods

- [Dogleg trust regions for fixed small systems](<https://hrkoyama.github.io/numerical-methods-atlas/methods/dogleg-trust-region/?lang=en>)
- [Armijo-damped Newton](<https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=en>)

  Separate the original residual from the scaled merit and retain Euclidean dogleg and trial ledgers.
- [Dogleg trust regions for fixed small systems](<https://hrkoyama.github.io/numerical-methods-atlas/methods/dogleg-trust-region/?lang=en>)

  Separate the original residual from the scaled merit and retain Euclidean dogleg and trial ledgers.
- [Armijo-damped Newton](<https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=en>)

## Equations

- [Finite-dimensional nonlinear maps, roots and differential actions](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#finite-dimensional-nonlinear-map-en>)

  Roots, JVP/VJP, HVP and branch conventions for finite algebraic maps. The variable count n is not a spatial dimension, and a classical derivative is not imposed at nonsmooth points. Small fixed real dimensionless inputs; assumptions and scope are limited to the matching contract.
- [Bratu nonlinear boundary-value problem](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bratu-en>)

  The convention here is −u″=λ exp(u). Newton–Krylov checks cover residuals, refinement and inner-solver failures. Small fixed real dimensionless inputs; assumptions and scope are limited to the matching contract.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/globalization-difficult-starts/?lang=en#globalization-difficult-starts-en-algorithm>)

  Separate the original residual from the scaled merit and retain Euclidean dogleg and trial ledgers.
- [Finite-dimensional nonlinear maps, roots and differential actions](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#finite-dimensional-nonlinear-map-en>)

  Roots, JVP/VJP, HVP and branch conventions for finite algebraic maps. The variable count n is not a spatial dimension, and a classical derivative is not imposed at nonsmooth points.
- [Bratu nonlinear boundary-value problem](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bratu-en>)

  The convention here is −u″=λ exp(u). Newton–Krylov checks cover residuals, refinement and inner-solver failures.

## Problem figures

- [Line search and trust regions from the same difficult starts](<https://hrkoyama.github.io/numerical-methods-atlas/problems/globalization-difficult-starts/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/results/globalization-difficult-starts-preview.png
- [Line search and trust regions from the same difficult starts](<https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/results/globalization-difficult-starts.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/results/globalization-difficult-starts.png

## Exact / reference solutions

- [Line search and trust regions from the same difficult starts — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/globalization-difficult-starts/?lang=en#references-en>)

  Check fixed inputs, independent references, retained candidates and every gate within the same120-second budget. Numerical success and diagnostic nonconvergence are distinct.
- [Globalization from identical starts: analytic controls and discrete Bratu corrections](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-globalization-difficult-starts-en>)
  relation: same-problem
  reference_kind: numerical-reference

  Finite-grid numerical reference Fixed real dimensionless systems: two Rosenbrock starts and two residual scalings, plus three starts for a 31-interior-node Dirichlet Bratu problem at lambda 3, compared by three methods. The Euclidean state radius is distinct from residual scaling. No all-start guarantee, universal method ranking or equivalence to PETSc implementation.
- [Globalization from identical starts: analytic controls and discrete Bratu corrections](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-globalization-difficult-starts-en>)
  reference_kind: numerical-reference

  Finite-grid numerical reference Fixed real dimensionless systems: two Rosenbrock starts and two residual scalings, plus three starts for a 31-interior-node Dirichlet Bratu problem at lambda 3, compared by three methods. The Euclidean state radius is distinct from residual scaling.
- [Line search and trust regions from the same difficult starts — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/globalization-difficult-starts/?lang=en#globalization-difficult-starts-en-validation>)

  Check fixed inputs, independent references, retained candidates and every gate within the same120-second budget. Numerical success and diagnostic nonconvergence are distinct.
- [Globalization from identical starts: analytic controls and discrete Bratu corrections](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-globalization-difficult-starts-en>)
  relation: same-problem
  reference_kind: numerical-reference

  Finite-grid numerical reference Fixed real dimensionless systems: two Rosenbrock starts and two residual scalings, plus three starts for a 31-interior-node Dirichlet Bratu problem at lambda 3, compared by three methods. The Euclidean state radius is distinct from residual scaling. No all-start guarantee, universal method ranking or equivalence to PETSc implementation.

## Code and validation

- [Line search and trust regions from the same difficult starts](<https://hrkoyama.github.io/numerical-methods-atlas/validation/globalization-difficult-starts/?lang=en>)
  availability: run

  Compare Newton, Armijo and dogleg from identical fixed starts, distinguishing roots from stationary nonroots and budget exhaustion.
- [Dogleg trust regions for fixed small systems — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/dogleg-trust-region/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
