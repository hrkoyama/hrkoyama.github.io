# Importance sampling and correlated-Gaussian diagnostics

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-stochastic-estimation/

Resources explicitly registered to the methods, problems and executions of this chapter. Study importance-weighted tails and 2D correlated-Gaussian MCMC, separating analytic targets, same-data diagnostic comparisons and fresh-sample checks.

## Methods

- [Monte Carlo integration](<https://hrkoyama.github.io/numerical-methods-atlas/methods/monte-carlo/?lang=en>)

  Ordinary mean ofY=1(X>a)exp(-aX+a²/2),without random weight normalization or proposal tuning. Retain direct zero-hit counts with Clopper-Pearson intervals.
- [Markov-chain Monte Carlo / MCMC](<https://hrkoyama.github.io/numerical-methods-atlas/methods/mcmc/?lang=en>)

  Symmetric random-walk MH retains rejected states. Compute original-scale meanESS/MCSE separately for8observables;rank bulkESS is not substituted.
- [Monte Carlo integration](<https://hrkoyama.github.io/numerical-methods-atlas/methods/monte-carlo/?lang=en>)
- [Markov-chain Monte Carlo / MCMC](<https://hrkoyama.github.io/numerical-methods-atlas/methods/mcmc/?lang=en>)

## Equations

- [Gaussian probability measures: tails and correlated targets](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#gaussian-probability-model-en>)

  A probability-density/integration model. Separate ordinary importance weights/known-variance intervals and observable-specific2D Gaussian diagnostics; no physical-time or universal MCMC-convergence claim. Standard normal tailsa3/6;proposalN(a,1);64independent seeds;fixedN2048/8192prefixes.
- [Gaussian probability measures: tails and correlated targets](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#gaussian-probability-model-en>)

  A probability-density/integration model. Separate ordinary importance weights/known-variance intervals and observable-specific2D Gaussian diagnostics; no physical-time or universal MCMC-convergence claim. Mean(1,-1),unit marginal variances,rho.95;4independent chainsets×4chains;burn1024/draw8192;prefix2048/8192. Fixed.9Lzand.25z,no adaptation.
- [Gaussian probability measures: tails and correlated targets](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#gaussian-probability-model-en>)

  A probability-density/integration model. Separate ordinary importance weights/known-variance intervals and observable-specific2D Gaussian diagnostics; no physical-time or universal MCMC-convergence claim.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/normal-tail-importance/?lang=en#normal-tail-importance-en-algorithm>)

  Ordinary mean ofY=1(X>a)exp(-aX+a²/2),without random weight normalization or proposal tuning. Retain direct zero-hit counts with Clopper-Pearson intervals.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/correlated-gaussian-mcmc/?lang=en#correlated-gaussian-mcmc-en-algorithm>)

  Symmetric random-walk MH retains rejected states. Compute original-scale meanESS/MCSE separately for8observables;rank bulkESS is not substituted.

## Problem figures

- [Ordinary importance sampling of a normal rare tail](<https://hrkoyama.github.io/numerical-methods-atlas/problems/normal-tail-importance/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/results/normal-tail-importance-preview.png
- [Joint target and MCSE for a correlated bivariate Gaussian](<https://hrkoyama.github.io/numerical-methods-atlas/problems/correlated-gaussian-mcmc/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/results/correlated-gaussian-mcmc-preview.png
- [Ordinary importance sampling of a normal rare tail](<https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/results/normal-tail-importance.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/results/normal-tail-importance.png
- [Joint target and MCSE for a correlated bivariate Gaussian](<https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/results/correlated-gaussian-mcmc.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/results/correlated-gaussian-mcmc.png

## Exact / reference solutions

- [Ordinary importance sampling of a normal rare tail — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/normal-tail-importance/?lang=en#references-en>)

  Qualify moments1..4 by independent positive quadrature. Gate known-variance5SE,batch variance,analytic variance reduction and omitted-weight negative control. Report known-variance normal95IScoverage separately for64trials per threshold/prefix.
- [Ordinary importance sampling of a normal rare tail](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-normal-tail-importance-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference Standard normal tailsa3/6;proposalN(a,1);64independent seeds;fixedN2048/8192prefixes. Bernoulli exact intervals are not applied to weighted IS.64trials do not prove general95%coverage;nested prefixes are not extra independent replicates. Global weightESS and eventESS are distinct.
- [Joint target and MCSE for a correlated bivariate Gaussian — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/correlated-gaussian-mcmc/?lang=en#references-en>)

  Gate all full-prefix observables in4preconditioned chainsets by Rhat/ESS/MCSE/knownmoments. Match exact dataSHAand640values from128scalar arrays in a separateArviZ0.20process. Target law is separately checked by analytic Gaussian moments. All640comparisons use the immutable same-data fixture;8freshchainsets independently receive the unchanged physical/mixing gates. No portable generated-byte-identity claim.
- [Joint target and MCSE for a correlated bivariate Gaussian](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-correlated-gaussian-mcmc-en>)
  relation: same-problem
  reference_kind: numerical-reference

  Finite-grid numerical reference Mean(1,-1),unit marginal variances,rho.95;4independent chainsets×4chains;burn1024/draw8192;prefix2048/8192. Fixed.9Lzand.25z,no adaptation. Diagnostic-engine independence is not an independent sampler. Rhat/ESS/MCSE do not prove global convergence/coverage. Isotropic is descriptive with no required failure;banana/funnel/HMC/NUTSremain unimplemented.
- [Ordinary importance sampling of a normal rare tail](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-normal-tail-importance-en>)
  reference_kind: analytic

  Analytic reference Standard normal tailsa3/6;proposalN(a,1);64independent seeds;fixedN2048/8192prefixes.
- [Joint target and MCSE for a correlated bivariate Gaussian](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-correlated-gaussian-mcmc-en>)
  reference_kind: numerical-reference

  Finite-grid numerical reference Mean(1,-1),unit marginal variances,rho.95;4independent chainsets×4chains;burn1024/draw8192;prefix2048/8192. Fixed.9Lzand.25z,no adaptation.
- [Ordinary importance sampling of a normal rare tail — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/normal-tail-importance/?lang=en#normal-tail-importance-en-validation>)

  Qualify moments1..4 by independent positive quadrature. Gate known-variance5SE,batch variance,analytic variance reduction and omitted-weight negative control. Report known-variance normal95IScoverage separately for64trials per threshold/prefix.
- [Ordinary importance sampling of a normal rare tail](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-normal-tail-importance-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference Standard normal tailsa3/6;proposalN(a,1);64independent seeds;fixedN2048/8192prefixes. Bernoulli exact intervals are not applied to weighted IS.64trials do not prove general95%coverage;nested prefixes are not extra independent replicates. Global weightESS and eventESS are distinct.
- [Joint target and MCSE for a correlated bivariate Gaussian — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/correlated-gaussian-mcmc/?lang=en#correlated-gaussian-mcmc-en-validation>)

  Gate all full-prefix observables in4preconditioned chainsets by Rhat/ESS/MCSE/knownmoments. Match exact dataSHAand640values from128scalar arrays in a separateArviZ0.20process. Target law is separately checked by analytic Gaussian moments. All640comparisons use the immutable same-data fixture;8freshchainsets independently receive the unchanged physical/mixing gates. No portable generated-byte-identity claim.
- [Joint target and MCSE for a correlated bivariate Gaussian](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-correlated-gaussian-mcmc-en>)
  relation: same-problem
  reference_kind: numerical-reference

  Finite-grid numerical reference Mean(1,-1),unit marginal variances,rho.95;4independent chainsets×4chains;burn1024/draw8192;prefix2048/8192. Fixed.9Lzand.25z,no adaptation. Diagnostic-engine independence is not an independent sampler. Rhat/ESS/MCSE do not prove global convergence/coverage. Isotropic is descriptive with no required failure;banana/funnel/HMC/NUTSremain unimplemented.

## Code and validation

- [Ordinary importance sampling of a normal rare tail](<https://hrkoyama.github.io/numerical-methods-atlas/validation/normal-tail-importance/?lang=en>)
  availability: run

  Check ordinary likelihood-ratio averages with analytic moments,independent batch variance and finite coverage diagnostics.
- [Joint target and MCSE for a correlated bivariate Gaussian](<https://hrkoyama.github.io/numerical-methods-atlas/validation/correlated-gaussian-mcmc/?lang=en>)
  availability: run

  Test actual2D MH paths against known joint moments and same-data ArviZ diagnostics.
