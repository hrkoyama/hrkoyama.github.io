# Multimodal MCMC: independent checks of poor mixing and convergence diagnostics

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-mcmc/

Resources explicitly registered to the methods, problems and executions of this chapter.

## Methods

- [Markov-chain Monte Carlo / MCMC](<https://hrkoyama.github.io/numerical-methods-atlas/methods/mcmc/?lang=en>)

  Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.
- [Markov-chain Monte Carlo / MCMC](<https://hrkoyama.github.io/numerical-methods-atlas/methods/mcmc/?lang=en>)

## Equations

- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/mcmc-multimodal-mixing/?lang=en#mcmc-multimodal-mixing-en-algorithm>)

  Local scale.8; mixed uses y=−x+.8Z with probability.1, otherwise y=x+.8Z. The state-independent mixture is symmetric q(y|x)=q(x|y), so MH uses the log-target ratio. Chains use independent PCG64 streams, with no adaptation or removal of rejected states.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/mcmc-diagnostic-reference/?lang=en#mcmc-diagnostic-reference-en-algorithm>)

  Original equation-based implementation: split with the odd center dropped, average-tie Blom ranks using corrected S+1/4, re-rank folded deviations, and take the larger Rhat. Bulk ESS uses rank-split draws; tail ESS first determines Type7 quantiles on original full draws, then splits <= indicators. Use initial-positive/monotone pairs, declared endpoint handling and tau>=1/log10(total), without clipping antithetic ESS to N.

## Problem figures

- [Multimodal MCMC: trapping, false reassurance and a global proposal](<https://hrkoyama.github.io/numerical-methods-atlas/problems/mcmc-bimodal-mixture/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/results/mcmc-multimodal-mixing.png
- [Multimodal MCMC: trapping, false reassurance and a global proposal](<https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/results/mcmc-multimodal-mixing.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/results/mcmc-multimodal-mixing.png
- [Independent MCMC diagnostic checks: rank Rhat, bulk/tail ESS and degeneracies](<https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/results/mcmc-diagnostic-reference.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/results/mcmc-diagnostic-reference.png

## Exact / reference solutions

- [Multimodal MCMC: trapping, false reassurance and a global proposal — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/mcmc-bimodal-mixture/?lang=en#references-en>)

  Compare with the known bimodal Gaussian mixture’s analytic density, moments, declared CDF points and positive occupancy, and check diagnostics against independent ArviZ references. Distinguish trapping from diagnostic limitations; reassuring local diagnostics do not guarantee global mixing.
- [Multimodal MCMC: trapping, false reassurance and a global proposal — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/mcmc-multimodal-mixing/?lang=en#mcmc-multimodal-mixing-en-validation>)

  Compare with analytic moments, seven declared CDF points and positive occupancy. Record per-chain occupancies/transitions, rank/folded split Rhat, bulk/tail/mean and mode-indicator ESS, and within-only ACF/ESS. Dispersed trapped chains can have a good pooled distribution yet fail between-chain diagnostics; same-mode chains can have reassuring Rhat yet fail the known target. A control scenario passes when its intended failure is detected. CDF error is a declared-point maximum, not whole-line KS distance or an IID-test p-value.
- [Independent MCMC diagnostic checks: rank Rhat, bulk/tail ESS and degeneracies — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/mcmc-diagnostic-reference/?lang=en#mcmc-diagnostic-reference-en-validation>)

  62 datasets: nine actual chains times three prefixes times x/indicator plus eight small fixtures. Regenerate and hash identical bytes; compare ordinary finite Rhat/ESS/ACF and test constants, zero within-chain variance, odd lengths, ties, shift and scale. Direct lag sums and infinite-series stationary-AR(1) tau=(1+rho)/(1−rho) provide separate checks of finite estimates. Routine runs compare stored references; live ArviZ regeneration is a separate optional procedure.

## Code and validation

- [Multimodal MCMC: trapping, false reassurance and a global proposal](<https://hrkoyama.github.io/numerical-methods-atlas/validation/mcmc-multimodal-mixing/?lang=en>)
  availability: run

  Compare dispersed local MH, same-mode local MH and symmetry-informed reflection/local MH on the same bimodal target. Separate detecting expected mixing failures from successful finite-budget mode exploration.
- [Independent MCMC diagnostic checks: rank Rhat, bulk/tail ESS and degeneracies](<https://hrkoyama.github.io/numerical-methods-atlas/validation/mcmc-diagnostic-reference/?lang=en>)
  availability: run

  Actually process62 byte-identical datasets with separately installed ArviZ0.20.0, bound by recipe/input/chain/official-source hashes. Separate finite-value agreement from explicit degeneracy-policy differences.
