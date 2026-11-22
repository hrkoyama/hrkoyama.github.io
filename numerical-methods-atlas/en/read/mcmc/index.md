# Markov-chain Monte Carlo / MCMC

MCMC constructs a chain with a chosen invariant distribution. Invariance, finite-time mixing and accuracy for a particular observable are separate questions. Preserve the earlier unimodal Gaussian example while a separate scoped release examines multimodal mixing failures, diagnostic blind spots and independent implementation comparisons.

## Problem and representative equations

For an unnormalized target π and proposal q(y|x), use the Metropolis–Hastings acceptance probability. Unknown target normalization cancels. Proposal factors cancel only for symmetric proposals; omitting them for an asymmetric proposal changes the target.

The new target is the one-dimensional equal-weight Gaussian mixture π(x)=[N(−6,1)+N(6,1)]/2. Compare moments, CDF and right-mode occupancy with known targets. It is one new test problem, distinct from the existing standard-normal target; different initializations, proposals and seeds do not add problems.

$$
a(x,y)=\min\!\left(1,\frac{\pi(y)q(x\mid y)}{\pi(x)q(y\mid x)}\right),\qquad N_{\rm eff}\approx\frac{N}{1+2\sum_{k\ge1}\rho_k}.
$$

## Algorithm

Propose y, accept or retain x, and keep rejected repetitions as samples. Assess initial transients and use dispersed initial states across chains. Interpret autocorrelation-based effective sample size only when stationarity and autocorrelation estimation are credible.

The new release distinguishes local random walks from dispersed mode-specific starts, local random walks with every chain starting in the same mode, and proposals containing reflection jumps that exploit the known symmetry x→−x. The last is a target-specific control, not a general solution for unknown multimodal distributions.

Evaluate x and the right-mode indicator separately. Preserve the old release’s classical split R-hat and mean-observable ESS; the new release adds rank-normalized split/folded R-hat and bulk/tail ESS as distinct definitions. ACF/ESS depend on the observable, sample budget, stationarity and estimator conventions; no single ESS universally characterizes a chain.

Do not use rank-transformed bulk ESS directly as an estimator of the raw-scale mean’s Monte Carlo standard error (MCSE). A library returning ESS=N for a constant observable is not evidence of good mixing.

## Conditions and pitfalls

Detailed balance alone does not establish irreducibility or aperiodicity. Multimodality, correlations and boundaries can slow mixing. High acceptance can simply reflect tiny moves. Thinning is not a general way to increase information for a fixed computational budget.

Chains trapped in different modes can reveal a between-chain discrepancy, while chains all trapped in one mode can have R-hat near one despite a completely unexplored mode. Check known CDFs, mode occupancy and transitions alongside apparently favorable R-hat/ESS. Reflection-induced mode changes alone do not establish within-mode exploration.

Passing a test that intentionally reproduces poor mixing or a diagnostic blind spot does not mean estimation succeeded in that scenario. Fixed-input thresholds are acceptance criteria for this small comparison, not finite-run guarantees, diagnostic false-positive rates or reliability for every seed and target.

The local Gaussian random-walk MH used here is theoretically irreducible. Failure to leave a mode in a finite run is not described as a permanently nonergodic algorithm.

## What to check

Check means, variances and quantiles for known targets, including asymmetric proposals and rejections. For multimodal cases report between-chain comparisons, autocorrelations, effective sample sizes and uncertainty; visually flat traces alone are not proof of convergence.

The new diagnostic controls compare ACF with direct summation on the same saved chains, and rank-normalized R-hat plus bulk/tail ESS with an independent ArviZ 0.20 execution. Keep IID, known-correlation and boundary controls such as constant series separate from estimation accuracy of the mixture sampler. Dedicated fixed inputs and references specify definitions, centering, splitting, ties, endpoints and the exact metrics compared.

For three scenarios and three fixed seeds, place distribution errors, mode occupancy/transitions and observable-specific diagnostics side by side. The old Gaussian release’s positive-sequence ESS and classical split R-hat remain unchanged and are not borrowed as verification of the new diagnostics.

Degenerate controls such as constant series and policies for nonfinite input are classification checks, separate from numerical agreement of finite diagnostics. The total number of reference-fixture fields is not presented as the number of numerical agreements.

## Fixed-input examples and diagnostic controls

Distinguish the scope established by acceptance checks from a general mathematical guarantee; preserve historical inputs, measurements and criteria.

### Gaussian-target MCMC: distribution, autocorrelation and ESS

Fixed-target computation

Check 32 Metropolis chains against a known standard-normal target; record mean, variance, CDF, autocorrelation time, ESS and sample-budget dependence.

Statistical checks apply to fixed seeds and budgets. ESS concerns the mean only; Rhat is not rank-normalized. No guarantee covers multimodality, high dimensions, every seed, mixing or a specified false-positive rate.

[Input, results and acceptance](/numerical-methods-atlas/validation/gaussian-mcmc/?lang=en) · [Method and sources](/numerical-methods-atlas/en/read/validation-models/#gaussian-mcmc) · [Code run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/run.py) · [Code models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/models.py) · [Tests test_models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/test_models.py) · [ZIP](/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip) · [Results](/code/validated-examples/2026-11-22/models/results/result.json) · [Rerun receipt](/code/validated-examples/2026-11-22/models/verification.json)

### Multimodal MCMC: trapping, false reassurance and a global proposal

Fixed-target computation

Compare dispersed local MH, same-mode local MH and symmetry-informed reflection/local MH on the same bimodal target. Separate detecting expected mixing failures from successful finite-budget mode exploration.

An educational fixed-seed, finite-budget experiment. The local Gaussian RW is theoretically irreducible MH; finite-time trapping is not called a nonergodic algorithm. Small Rhat, large ESS and pooled-CDF agreement cannot rule out undiscovered modes. Symmetry-informed reflection is not a generic multimodal solver. No quantum calculations.

[Input, results and acceptance](/numerical-methods-atlas/validation/mcmc-multimodal-mixing/?lang=en) · [Method and sources](/numerical-methods-atlas/en/read/validation-mcmc/#mcmc-multimodal-mixing) · [Code run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/run.py) · [Code sampler.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/sampler.py) · [Code diagnostics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/diagnostics.py) · [Code experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/experiments.py) · [Code fixtures.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/fixtures.py) · [Code generate-arviz-reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/generate-arviz-reference.py) · [Code prepare-reference-input.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/prepare-reference-input.py) · [Tests test_mcmc.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/test_mcmc.py) · [ZIP](/code/validated-examples/2026-11-22/mcmc/atlas-mcmc-2026-11-22.zip) · [Results](/code/validated-examples/2026-11-22/mcmc/results/result.json) · [Rerun receipt](/code/validated-examples/2026-11-22/mcmc/verification.json)

### Independent MCMC diagnostic checks: rank Rhat, bulk/tail ESS and degeneracies

Diagnostic control; no physical-problem increment

Actually process62 byte-identical datasets with separately installed ArviZ0.20.0, bound by recipe/input/chain/official-source hashes. Separate finite-value agreement from explicit degeneracy-policy differences.

An educational fixed-seed, finite-budget experiment. The local Gaussian RW is theoretically irreducible MH; finite-time trapping is not called a nonergodic algorithm. Small Rhat, large ESS and pooled-CDF agreement cannot rule out undiscovered modes. Symmetry-informed reflection is not a generic multimodal solver. No quantum calculations. ArviZ raw constant-ESS=N is not evidence of mixing. Globally identical values yield null/status; differing per-chain constants yield null/infinite-separation Rhat while retaining raw huge-finite/infinite library values outside ordinary finite comparisons. Bulk ESS is not a raw-mean MCSE estimator.

[Input, results and acceptance](/numerical-methods-atlas/validation/mcmc-diagnostic-reference/?lang=en) · [Method and sources](/numerical-methods-atlas/en/read/validation-mcmc/#mcmc-diagnostic-reference) · [Code run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/run.py) · [Code sampler.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/sampler.py) · [Code diagnostics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/diagnostics.py) · [Code experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/experiments.py) · [Code fixtures.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/fixtures.py) · [Code generate-arviz-reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/generate-arviz-reference.py) · [Code prepare-reference-input.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/prepare-reference-input.py) · [Tests test_mcmc.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/test_mcmc.py) · [ZIP](/code/validated-examples/2026-11-22/mcmc/atlas-mcmc-2026-11-22.zip) · [Results](/code/validated-examples/2026-11-22/mcmc/results/result.json) · [Rerun receipt](/code/validated-examples/2026-11-22/mcmc/verification.json)

## Publication scope

The earlier unimodal Gaussian release remains separate from the new bimodal exploration comparison and diagnostic controls. Reproducing poor mixing is also an intended check. These are low-dimensional, fixed-seed educational examples using a known symmetry, not general MCMC, high-dimensional or scientific-model convergence guarantees.

## Sources

- Nicholas Metropolis and Arianna W. Rosenbluth and Marshall N. Rosenbluth and Augusta H. Teller and Edward Teller (1953). Equation of State Calculations by Fast Computing Machines. https://doi.org/10.1063/1.1699114
- W. K. Hastings (1970). Monte Carlo sampling methods using Markov chains and their applications. https://doi.org/10.1093/biomet/57.1.97
