# Gaussian and adaptive quadrature

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/quadrature/

Resources explicitly registered to the methods, problems and executions of this chapter.

## Methods

- [Gaussian and adaptive quadrature](<https://hrkoyama.github.io/numerical-methods-atlas/methods/quadrature/?lang=en>)
- [Gauss–Kronrod G7/K15](<https://hrkoyama.github.io/numerical-methods-atlas/methods/gauss-kronrod/?lang=en>)
- [Tanh–sinh double-exponential quadrature](<https://hrkoyama.github.io/numerical-methods-atlas/methods/tanh-sinh/?lang=en>)
- [Smolyak sparse-grid quadrature](<https://hrkoyama.github.io/numerical-methods-atlas/methods/smolyak-sparse-grid/?lang=en>)

## Equations

No chapter-specific association is registered. Atlas-wide index: [Equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en)

## Problem figures

No chapter-specific association is registered. Atlas-wide index: [Test problems by name and figure](https://hrkoyama.github.io/numerical-methods-atlas/gallery/?lang=en)

## Exact / reference solutions

No chapter-specific association is registered. Atlas-wide index: [Exact and reference solutions](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en)

## Code and validation

- [Gauss–Legendre and adaptive quadrature: exactness, error estimates and budgets](<https://hrkoyama.github.io/numerical-methods-atlas/validation/gauss-adaptive-quadrature/?lang=en>)
  availability: run

  Construct Gaussian nodes/weights from the Legendre recurrence and test polynomial moments through degree 2n−1 and an exponential. Adaptive Simpson integrates exponential and Lorentzian peaks, against analytic integrals and independent QUADPACK.
- [Quadrature: narrow peaks, cancellation, endpoints and estimator blind spots](<https://hrkoyama.github.io/numerical-methods-atlas/validation/quadrature-conditioning/?lang=en>)
  availability: run

  Vary Gauss order and adaptive tolerance on narrow Lorentz peaks, a square-root endpoint, severe cancellation, a zero integral and a deliberately missed compact bump, using analytic integrals and QUADPACK.
- [QUADPACK dispatch and finite Simpson companions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/quadpack-domain-selection/?lang=en>)
  availability: run

  Fifteen specialized quadratures and fifteen Simpson companions use fixed inputs.
- [G7/K15 and finite-interval tanh-sinh](<https://hrkoyama.github.io/numerical-methods-atlas/validation/gk15-double-exponential/?lang=en>)
  availability: run

  Nine adaptive GK rows and twenty-four fixed DE sums are compared.
- [Tensor and Smolyak controls in two to four dimensions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/tensor-smolyak-dimensions/?lang=en>)
  availability: run

  Forty-two fixed cubatures compare a smooth product and an interaction product.
- [Gaussian and adaptive quadrature — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/quadrature/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [Gauss–Kronrod G7/K15 — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/gauss-kronrod/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [Tanh–sinh double-exponential quadrature — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/tanh-sinh/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [Smolyak sparse-grid quadrature — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/smolyak-sparse-grid/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
