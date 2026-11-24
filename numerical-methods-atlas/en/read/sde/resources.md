# Stochastic differential equations

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/sde/

Resources explicitly registered to the methods, problems and executions of this chapter.

## Methods

- [Stochastic differential equations](<https://hrkoyama.github.io/numerical-methods-atlas/methods/sde/?lang=en>)
- [Stochastic differential equations](<https://hrkoyama.github.io/numerical-methods-atlas/methods/sde/?lang=en>)

  Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions.

## Equations

- [Scalar Ito diffusion: GBM and OU](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#scalar-ito-diffusion-en>)

  Scalar SDEs with deterministic initial states. Separate weak moment bias,strong errors on shared Brownian paths and finite-sample MCSE. OU is a related bath-component check,not the full harmonic Langevin system. Geometric-Brownian Itô SDE dX=μXdt+σXdW; no SDE-specific entry exists among the 46 equations.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#execution-gbm-sde-en>)

  Euler–Maruyama for scalar geometric Brownian motion. Coarse/fine steps and analytic endpoints share the same Brownian paths; measure strong RMS error across 4096 paths. Does not validate general SDEs, MCMC or weak convergence order.

## Problem figures

- [Itô SDE: strong convergence with coupled Brownian paths](<https://hrkoyama.github.io/numerical-methods-atlas/problems/gbm-sde/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/results/gbm-sde/preview.png

## Exact / reference solutions

- [Itô SDE: strong convergence with coupled Brownian paths — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/gbm-sde/?lang=en#references-en>)

  Couple geometric Brownian motion to its analytic Itô solution using the same Brownian increments to check strong convergence and moments, separately from deterministic ODE exactness.
- [GBM weak bias and Monte Carlo error](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-gbm-weak-moments-en>)
  relation: related-model
  reference_kind: analytic

  Analytic reference dX=.5Xdt+.4XdW,X0=1;dimensionlessT1;8/16/32/64steps;32independent seeds×1024paths. Unbounded state,no clipping. dX=.5Xdt+.4XdW,X0=1;dimensionlessT1;8/16/32/64steps;32independent seeds×1024paths. Unbounded state,no clipping.
- [Milstein and EM on identical Brownian paths](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-gbm-milstein-strong-en>)
  relation: related-model
  reference_kind: analytic

  Analytic reference ExistingGBMparametersmu.15,sigma.4,X0=T1;4seeds×8192paths;16/32/64/128steps. ExistingGBMparametersmu.15,sigma.4,X0=T1;4seeds×8192paths;16/32/64/128steps.
- [Itô SDE: strong convergence with coupled Brownian paths — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/gbm-sde/?lang=en#gbm-sde-en-validation>)

  Euler–Maruyama for scalar geometric Brownian motion. Coarse/fine steps and analytic endpoints share the same Brownian paths; measure strong RMS error across 4096 paths. Does not validate general SDEs, MCMC or weak convergence order.
- [GBM weak bias and Monte Carlo error](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-gbm-weak-moments-en>)
  relation: related-model
  reference_kind: analytic

  Analytic reference dX=.5Xdt+.4XdW,X0=1;dimensionlessT1;8/16/32/64steps;32independent seeds×1024paths. Unbounded state,no clipping. dX=.5Xdt+.4XdW,X0=1;dimensionlessT1;8/16/32/64steps;32independent seeds×1024paths. Unbounded state,no clipping.
- [Milstein and EM on identical Brownian paths](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-gbm-milstein-strong-en>)
  relation: related-model
  reference_kind: analytic

  Analytic reference ExistingGBMparametersmu.15,sigma.4,X0=T1;4seeds×8192paths;16/32/64/128steps. ExistingGBMparametersmu.15,sigma.4,X0=T1;4seeds×8192paths;16/32/64/128steps.

## Code and validation

- [Itô SDE: strong convergence with coupled Brownian paths](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/gbm-sde/?lang=en>)
  availability: run

  Euler–Maruyama for scalar geometric Brownian motion. Coarse/fine steps and analytic endpoints share the same Brownian paths; measure strong RMS error across 4096 paths. Does not validate general SDEs, MCMC or weak convergence order.
- [GBM weak bias and Monte Carlo error](<https://hrkoyama.github.io/numerical-methods-atlas/validation/gbm-weak-moments/?lang=en>)
  availability: run

  Separate continuous truth,exact discrete EM expectation,paired-path weak difference and MCSE.
- [Milstein and EM on identical Brownian paths](<https://hrkoyama.github.io/numerical-methods-atlas/validation/gbm-milstein-strong/?lang=en>)
  availability: run

  Compare compensated Milstein and EM endpoint L2RMS against exact endpoints and finite-moment identities.
- [OU weak moments with joint Brownian coupling](<https://hrkoyama.github.io/numerical-methods-atlas/validation/ou-weak-moments/?lang=en>)
  availability: run

  Separate continuous truth,exact discrete EM expectation,paired-path weak difference and MCSE.
- [Stochastic differential equations — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/sde/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [Itô SDE: strong convergence with coupled Brownian paths — code and validation status](<https://hrkoyama.github.io/numerical-methods-atlas/problems/gbm-sde/?lang=en#code-en>)
  availability: source

  Inspect the corresponding public checks and distribution conditions.
