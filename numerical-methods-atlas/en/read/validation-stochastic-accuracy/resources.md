# Weak/strong SDE errors and sampling uncertainty

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-stochastic-accuracy/

Resources explicitly registered to the methods, problems and executions of this chapter. Use analytic moments and shared Brownian paths to separate weak/strong SDE errors from finite-sample uncertainty.

## Methods

- [Stochastic differential equations](<https://hrkoyama.github.io/numerical-methods-atlas/methods/sde/?lang=en>)

## Equations

- [Scalar Ito diffusion: GBM and OU](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#scalar-ito-diffusion-en>)

  Scalar SDEs with deterministic initial states. Separate weak moment bias,strong errors on shared Brownian paths and finite-sample MCSE. OU is a related bath-component check,not the full harmonic Langevin system.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/gbm-weak-moments/?lang=en#gbm-weak-moments-en-algorithm>)

  Aggregate fixed fine Gaussian blocks;reuse one exact terminal array. OUexact kicks use the correct jointly sampled integral with independent bridge noise. Different floating reduction orders need not be bit identical.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/ou-weak-moments/?lang=en#ou-weak-moments-en-algorithm>)

  Aggregate fixed fine Gaussian blocks;reuse one exact terminal array. OUexact kicks use the correct jointly sampled integral with independent bridge noise. Different floating reduction orders need not be bit identical.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/gbm-milstein-strong/?lang=en#gbm-milstein-strong-en-algorithm>)

  Milstein adds.5sigma²X(dW²-h). All methods/levels share the fine driver and one exact terminal array. No state repair.

## Problem figures

- [GBM weak bias and Monte Carlo error](<https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/results/gbm-weak-moments.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/results/gbm-weak-moments.png
- [OU weak moments with joint Brownian coupling](<https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/results/ou-weak-moments.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/results/ou-weak-moments.png
- [Milstein and EM on identical Brownian paths](<https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/results/gbm-milstein-strong.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/results/gbm-milstein-strong.png
- [Itô SDE: strong convergence with coupled Brownian paths](<https://hrkoyama.github.io/numerical-methods-atlas/problems/gbm-sde/?lang=en>)

  Use analytic moments and shared Brownian paths to separate weak/strong SDE errors from finite-sample uncertainty. Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/results/gbm-sde/preview.png
- [Langevin thermostat: canonical distributions, timestep bias and correlation](<https://hrkoyama.github.io/numerical-methods-atlas/problems/langevin-harmonic/?lang=en>)

  Use analytic moments and shared Brownian paths to separate weak/strong SDE errors from finite-sample uncertainty. Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/langevin-harmonic.png

## Exact / reference solutions

- [GBM weak bias and Monte Carlo error](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-gbm-weak-moments-en>)
  reference_kind: analytic

  Analytic reference dX=.5Xdt+.4XdW,X0=1;dimensionlessT1;8/16/32/64steps;32independent seeds×1024paths. Unbounded state,no clipping.
- [OU weak moments with joint Brownian coupling](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-ou-weak-moments-en>)
  reference_kind: analytic

  Analytic reference dX=1.5(.2-X)dt+.8dW,X0=.7;dimensionlessT1;8/16/32/64steps;32independent seeds×1024paths. Unbounded state,no clipping.
- [Milstein and EM on identical Brownian paths](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-gbm-milstein-strong-en>)
  reference_kind: analytic

  Analytic reference ExistingGBMparametersmu.15,sigma.4,X0=T1;4seeds×8192paths;16/32/64/128steps.
- [GBM weak bias and Monte Carlo error — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/gbm-weak-moments/?lang=en#gbm-weak-moments-en-validation>)

  Before paths qualify Decimal80/120,independent GH/OUcovariance integrals and paired-variance allocation. Gate5MCSE calibration,MCSE precision,fixed three-level weak rate and final-two-level3SE resolution. Coverage is descriptive over32batches against discrete truth.
- [GBM weak bias and Monte Carlo error](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-gbm-weak-moments-en>)
  relation: related-model
  reference_kind: analytic

  Analytic reference dX=.5Xdt+.4XdW,X0=1;dimensionlessT1;8/16/32/64steps;32independent seeds×1024paths. Unbounded state,no clipping. dX=.5Xdt+.4XdW,X0=1;dimensionlessT1;8/16/32/64steps;32independent seeds×1024paths. Unbounded state,no clipping.
- [Milstein and EM on identical Brownian paths](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-gbm-milstein-strong-en>)
  relation: related-model
  reference_kind: analytic

  Analytic reference ExistingGBMparametersmu.15,sigma.4,X0=T1;4seeds×8192paths;16/32/64/128steps. ExistingGBMparametersmu.15,sigma.4,X0=T1;4seeds×8192paths;16/32/64/128steps.
- [OU weak moments with joint Brownian coupling — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/ou-weak-moments/?lang=en#ou-weak-moments-en-validation>)

  Before paths qualify Decimal80/120,independent GH/OUcovariance integrals and paired-variance allocation. Gate5MCSE calibration,MCSE precision,fixed three-level weak rate and final-two-level3SE resolution. Coverage is descriptive over32batches against discrete truth.
- [OU weak moments with joint Brownian coupling](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-ou-weak-moments-en>)
  relation: related-model
  reference_kind: analytic

  Analytic reference dX=1.5(.2-X)dt+.8dW,X0=.7;dimensionlessT1;8/16/32/64steps;32independent seeds×1024paths. Unbounded state,no clipping. dX=1.5(.2-X)dt+.8dW,X0=.7;dimensionlessT1;8/16/32/64steps;32independent seeds×1024paths. Unbounded state,no clipping.
- [Milstein and EM on identical Brownian paths — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/gbm-milstein-strong/?lang=en#gbm-milstein-strong-en-validation>)

  Qualify cancellation-prone analytic MSE by Decimal80/120and independent one-step GH. Gate squared-error5SE calibration,fixed-three-level RMS rates and finest advantage.64paired path-block jackknife describes slope uncertainty.
- [GBM weak bias and Monte Carlo error](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-gbm-weak-moments-en>)
  relation: related-model
  reference_kind: analytic

  Analytic reference dX=.5Xdt+.4XdW,X0=1;dimensionlessT1;8/16/32/64steps;32independent seeds×1024paths. Unbounded state,no clipping. dX=.5Xdt+.4XdW,X0=1;dimensionlessT1;8/16/32/64steps;32independent seeds×1024paths. Unbounded state,no clipping.
- [Milstein and EM on identical Brownian paths](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-gbm-milstein-strong-en>)
  relation: related-model
  reference_kind: analytic

  Analytic reference ExistingGBMparametersmu.15,sigma.4,X0=T1;4seeds×8192paths;16/32/64/128steps. ExistingGBMparametersmu.15,sigma.4,X0=T1;4seeds×8192paths;16/32/64/128steps.
- [Itô SDE: strong convergence with coupled Brownian paths — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/gbm-sde/?lang=en#references-en>)

  Use analytic moments and shared Brownian paths to separate weak/strong SDE errors from finite-sample uncertainty. Couple geometric Brownian motion to its analytic Itô solution using the same Brownian increments to check strong convergence and moments, separately from deterministic ODE exactness.
- [GBM weak bias and Monte Carlo error](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-gbm-weak-moments-en>)
  relation: related-model
  reference_kind: analytic

  Use analytic moments and shared Brownian paths to separate weak/strong SDE errors from finite-sample uncertainty. Analytic reference dX=.5Xdt+.4XdW,X0=1;dimensionlessT1;8/16/32/64steps;32independent seeds×1024paths. Unbounded state,no clipping. dX=.5Xdt+.4XdW,X0=1;dimensionlessT1;8/16/32/64steps;32independent seeds×1024paths. Unbounded state,no clipping.
- [Milstein and EM on identical Brownian paths](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-gbm-milstein-strong-en>)
  relation: related-model
  reference_kind: analytic

  Use analytic moments and shared Brownian paths to separate weak/strong SDE errors from finite-sample uncertainty. Analytic reference ExistingGBMparametersmu.15,sigma.4,X0=T1;4seeds×8192paths;16/32/64/128steps. ExistingGBMparametersmu.15,sigma.4,X0=T1;4seeds×8192paths;16/32/64/128steps.
- [Langevin thermostat: canonical distributions, timestep bias and correlation — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/langevin-harmonic/?lang=en#references-en>)

  Use analytic moments and shared Brownian paths to separate weak/strong SDE errors from finite-sample uncertainty. Use analytic canonical-distribution, moment and correlation standards for the harmonic potential to check timestep bias, separately from frictionless, noiseless harmonic trajectories.
- [OU weak moments with joint Brownian coupling](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-ou-weak-moments-en>)
  relation: related-model
  reference_kind: analytic

  Use analytic moments and shared Brownian paths to separate weak/strong SDE errors from finite-sample uncertainty. Analytic reference dX=1.5(.2-X)dt+.8dW,X0=.7;dimensionlessT1;8/16/32/64steps;32independent seeds×1024paths. Unbounded state,no clipping. dX=1.5(.2-X)dt+.8dW,X0=.7;dimensionlessT1;8/16/32/64steps;32independent seeds×1024paths. Unbounded state,no clipping.

## Code and validation

- [GBM weak bias and Monte Carlo error](<https://hrkoyama.github.io/numerical-methods-atlas/validation/gbm-weak-moments/?lang=en>)
  availability: run

  Separate continuous truth,exact discrete EM expectation,paired-path weak difference and MCSE.
- [OU weak moments with joint Brownian coupling](<https://hrkoyama.github.io/numerical-methods-atlas/validation/ou-weak-moments/?lang=en>)
  availability: run

  Separate continuous truth,exact discrete EM expectation,paired-path weak difference and MCSE.
- [Milstein and EM on identical Brownian paths](<https://hrkoyama.github.io/numerical-methods-atlas/validation/gbm-milstein-strong/?lang=en>)
  availability: run

  Compare compensated Milstein and EM endpoint L2RMS against exact endpoints and finite-moment identities.
- [Itô SDE: strong convergence with coupled Brownian paths — code and validation status](<https://hrkoyama.github.io/numerical-methods-atlas/problems/gbm-sde/?lang=en#code-en>)
  availability: source

  Use analytic moments and shared Brownian paths to separate weak/strong SDE errors from finite-sample uncertainty. Inspect the corresponding public checks and distribution conditions.
