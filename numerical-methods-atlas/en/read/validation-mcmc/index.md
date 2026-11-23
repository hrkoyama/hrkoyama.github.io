# Multimodal MCMC: independent checks of poor mixing and convergence diagnostics

Compare local trapping and between-mode movement on a bimodal target. Check autocorrelation, effective sample size and convergence diagnostics against an independent implementation, and expose missed exploration that diagnostics alone cannot detect.

These additional validation supplements are managed separately from the common 22-example registry. Receipts cover independent ZIP extraction, tests and every fixed input within each group. Changes of settings, methods or step sizes do not add independent physical problems.

## Multimodal MCMC: trapping, false reassurance and a global proposal

Compare dispersed local MH, same-mode local MH and symmetry-informed reflection/local MH on the same bimodal target. Separate detecting expected mixing failures from successful finite-budget mode exploration.

**Methods used**

- [Markov-chain Monte Carlo / MCMC](https://hrkoyama.github.io/numerical-methods-atlas/methods/mcmc/?lang=en) (`mcmc`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/mcmc-multimodal-mixing/?lang=en#mcmc-multimodal-mixing-en-algorithm)

Local scale.8; mixed uses y=−x+.8Z with probability.1, otherwise y=x+.8Z. The state-independent mixture is symmetric q(y|x)=q(x|y), so MH uses the log-target ratio. Chains use independent PCG64 streams, with no adaptation or removal of rejected states.

$$
\pi(x)=\tfrac12\phi(x+6)+\tfrac12\phi(x-6),\quad E[X]=0,\quad\operatorname{Var}X=37
$$

$$
F(x)=\tfrac12\Phi(x+6)+\tfrac12\Phi(x-6),\quad P(X>0)=\tfrac12
$$

$$
q(y\mid x)=(1-p)\phi_s(y-x)+p\phi_s(y+x)=q(x\mid y),\quad s=.8,\ p=.1
$$

$$
\alpha(x,y)=\min\{1,\pi(y)/\pi(x)\},\quad I_n=\mathbf1\{X_n>0\}
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![Multimodal MCMC: trapping, false reassurance and a global proposal: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/results/mcmc-multimodal-mixing.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Multimodal MCMC: trapping, false reassurance and a global proposal](https://hrkoyama.github.io/numerical-methods-atlas/problems/mcmc-bimodal-mixture/?lang=en) (`mcmc-bimodal-mixture`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/mcmc-bimodal-mixture/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/mcmc-multimodal-mixing/?lang=en#mcmc-multimodal-mixing-en-validation)

Compare with analytic moments, seven declared CDF points and positive occupancy. Record per-chain occupancies/transitions, rank/folded split Rhat, bulk/tail/mean and mode-indicator ESS, and within-only ACF/ESS. Dispersed trapped chains can have a good pooled distribution yet fail between-chain diagnostics; same-mode chains can have reassuring Rhat yet fail the known target. A control scenario passes when its intended failure is detected. CDF error is a declared-point maximum, not whole-line KS distance or an IID-test p-value.

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.
### Assumptions, units and boundaries

Dimensionless1D target p=.5N(−6,1)+.5N(6,1), mean0/variance37/positive occupancy.5. Three fixed seeds, four chains,1024 warmup and16384 retained draws/chain. Prefixes1024/4096/16384 are nested, not independent replications. Rejections/self-transitions are retained.

**Editorial clarification**

Passing this validation means confirming the well-mixing run and correctly exposing failures and diagnostic blind spots in deliberately trapped runs; it does not mean every run converged. Rhat and ESS depend on the observable, finite sample and initial states, and can look reassuring when all chains miss the same mode. Reflection jumps exploit known target symmetry for this comparison and do not guarantee exploration of arbitrary unknown multimodal targets.

### Adopted numerical method

Local scale.8; mixed uses y=−x+.8Z with probability.1, otherwise y=x+.8Z. The state-independent mixture is symmetric q(y|x)=q(x|y), so MH uses the log-target ratio. Chains use independent PCG64 streams, with no adaptation or removal of rejected states.

$$
\pi(x)=\tfrac12\phi(x+6)+\tfrac12\phi(x-6),\quad E[X]=0,\quad\operatorname{Var}X=37
$$

$$
F(x)=\tfrac12\Phi(x+6)+\tfrac12\Phi(x-6),\quad P(X>0)=\tfrac12
$$

$$
q(y\mid x)=(1-p)\phi_s(y-x)+p\phi_s(y+x)=q(x\mid y),\quad s=.8,\ p=.1
$$

$$
\alpha(x,y)=\min\{1,\pi(y)/\pi(x)\},\quad I_n=\mathbf1\{X_n>0\}
$$

### References and validation

Compare with analytic moments, seven declared CDF points and positive occupancy. Record per-chain occupancies/transitions, rank/folded split Rhat, bulk/tail/mean and mode-indicator ESS, and within-only ACF/ESS. Dispersed trapped chains can have a good pooled distribution yet fail between-chain diagnostics; same-mode chains can have reassuring Rhat yet fail the known target. A control scenario passes when its intended failure is detected. CDF error is a declared-point maximum, not whole-line KS distance or an IID-test p-value.

### Limits

An educational fixed-seed, finite-budget experiment. The local Gaussian RW is theoretically irreducible MH; finite-time trapping is not called a nonergodic algorithm. Small Rhat, large ESS and pooled-CDF agreement cannot rule out undiscovered modes. Symmetry-informed reflection is not a generic multimodal solver. No quantum calculations.

### Stored measurements and decisions

```json
{
  "metrics": {
    "maximum_fft_direct_acov_error": 7.105427357601002e-15,
    "mixed_maximum_mean_error": 0.1276413989022717,
    "mixed_maximum_variance_error": 0.15417646942373153,
    "mixed_maximum_cdf_error": 0.011283513239714604,
    "mixed_maximum_occupancy_error": 0.010986328125,
    "mixed_maximum_rank_rhat": 1.000848801908244,
    "mixed_minimum_bulk_ess": 6255.350954061888,
    "mixed_minimum_tail_ess": 9814.323360820285,
    "mixed_minimum_mode_ess": 4932.879232093147,
    "mixed_minimum_transitions_per_chain": 1183,
    "intentionally_trapped_scenarios": 6.0
  },
  "checks": {
    "dispersed-2026112251-acceptance": true,
    "dispersed-2026112251-intentionally_trapped": true,
    "dispersed-2026112251-between_chain_failure_detected": true,
    "dispersed-2026112251-mode_variance_failure_explicit": true,
    "dispersed-2026112252-acceptance": true,
    "dispersed-2026112252-intentionally_trapped": true,
    "dispersed-2026112252-between_chain_failure_detected": true,
    "dispersed-2026112252-mode_variance_failure_explicit": true,
    "dispersed-2026112253-acceptance": true,
    "dispersed-2026112253-intentionally_trapped": true,
    "dispersed-2026112253-between_chain_failure_detected": true,
    "dispersed-2026112253-mode_variance_failure_explicit": true,
    "same_mode-2026112251-acceptance": true,
    "same_mode-2026112251-intentionally_trapped": true,
    "same_mode-2026112251-apparently_benign_diagnostics": true,
    "same_mode-2026112251-wrong_target_cdf": true,
    "same_mode-2026112251-wrong_target_mean": true,
    "same_mode-2026112251-wrong_target_occupancy": true,
    "same_mode-2026112251-constant_mode_indicator_undefined": true,
    "same_mode-2026112252-acceptance": true,
    "same_mode-2026112252-intentionally_trapped": true,
    "same_mode-2026112252-apparently_benign_diagnostics": true,
    "same_mode-2026112252-wrong_target_cdf": true,
    "same_mode-2026112252-wrong_target_mean": true,
    "same_mode-2026112252-wrong_target_occupancy": true,
    "same_mode-2026112252-constant_mode_indicator_undefined": true,
    "same_mode-2026112253-acceptance": true,
    "same_mode-2026112253-intentionally_trapped": true,
    "same_mode-2026112253-apparently_benign_diagnostics": true,
    "same_mode-2026112253-wrong_target_cdf": true,
    "same_mode-2026112253-wrong_target_mean": true,
    "same_mode-2026112253-wrong_target_occupancy": true,
    "same_mode-2026112253-constant_mode_indicator_undefined": true,
    "mixed-2026112251-acceptance": true,
    "mixed-2026112251-mean_absolute_error": true,
    "mixed-2026112251-variance_absolute_error": true,
    "mixed-2026112251-cdf_max_error": true,
    "mixed-2026112251-occupancy_absolute_error": true,
    "mixed-2026112251-rank_rhat": true,
    "mixed-2026112251-bulk_ess": true,
    "mixed-2026112251-tail_ess": true,
    "mixed-2026112251-mode_ess": true,
    "mixed-2026112251-per_chain_mode_transitions": true,
    "mixed-2026112252-acceptance": true,
    "mixed-2026112252-mean_absolute_error": true,
    "mixed-2026112252-variance_absolute_error": true,
    "mixed-2026112252-cdf_max_error": true,
    "mixed-2026112252-occupancy_absolute_error": true,
    "mixed-2026112252-rank_rhat": true,
    "mixed-2026112252-bulk_ess": true,
    "mixed-2026112252-tail_ess": true,
    "mixed-2026112252-mode_ess": true,
    "mixed-2026112252-per_chain_mode_transitions": true,
    "mixed-2026112253-acceptance": true,
    "mixed-2026112253-mean_absolute_error": true,
    "mixed-2026112253-variance_absolute_error": true,
    "mixed-2026112253-cdf_max_error": true,
    "mixed-2026112253-occupancy_absolute_error": true,
    "mixed-2026112253-rank_rhat": true,
    "mixed-2026112253-bulk_ess": true,
    "mixed-2026112253-tail_ess": true,
    "mixed-2026112253-mode_ess": true,
    "mixed-2026112253-per_chain_mode_transitions": true,
    "fft_vs_direct_autocovariance": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/mcmc-multimodal-mixing/index.json

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/atlas-mcmc-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- A. Vehtari, A. Gelman, D. Simpson, B. Carpenter and P.-C. Bürkner (2021). Rank-Normalization, Folding, and Localization: An Improved R-hat for Assessing Convergence of MCMC (with Discussion). https://paulbuerkner.com/publications/pdf/2021__Vehtari_et_al__Bayesian_Analysis.pdf; review_level=corrected-author-paper-selected-sections
Checked original sections3–4, the2021-06-22 correction of Eq4.1 to denominator S+1/4, and the constant-indicator warning. This does not reproduce every original numerical experiment.

- C. J. Geyer (1992). Practical Markov Chain Monte Carlo. https://www2.stat.duke.edu/~scs/Courses/Stat376/Papers/GeyerStatSci1992.pdf; review_level=original-selected-paired-sequence-theory
Checked section3.3 and Theorems3.1/3.2 for reversibility assumptions and initial-positive/monotone sequences. Main article pp473–483 are distinguished from combined discussion pagination; no claim gives exact true ESS from finite chains.

- A. Gelman and D. B. Rubin (1992). Inference from Iterative Simulation Using Multiple Sequences. https://www2.stat.duke.edu/~scs/Courses/Stat376/Papers/ConvergeDiagnostics/GelmanRubinStatSci1992.pdf; review_level=original-selected-multiple-chain-starting-points
Checked the original introduction/section2 on multiple sequences and overdispersed starts. Distinct from the later rank/folded method, and not a reproduction of every1992 finite-sample correction.

- The ArviZ developers (2024). ArviZ0.20.0 public diagnostics API and tagged source. https://python.arviz.org/en/v0.20.0/api/generated/arviz.rhat.html; review_level=official-versioned-source-and-actual-independent-execution
Checked the official0.20.0 rhat/ess API and tagged source for splitting, ranks, Type7 quantiles, endpoints and constant conventions. Installed source hashes match commit94113176cae99a05ba41d1e93739ee2d5bdbe9b1;62 byte-identical datasets were actually processed in a separate environment without importing Atlas diagnostics. No upstream implementation is reproduced; values, versions, hashes and regeneration code are supplied.

- N. Metropolis, A. W. Rosenbluth, M. N. Rosenbluth, A. H. Teller and E. Teller (1953). Equation of State Calculations by Fast Computing Machines. https://doi.org/10.1063/1.1699114; review_level=publisher-abstract-and-metadata
Publisher bibliography and abstract checked. Cited for symmetric-proposal Metropolis acceptance; no reproduction of the original hard-sphere experiment is claimed.

- W. K. Hastings (1970). Monte Carlo sampling methods using Markov chains and their applications. https://probability.ca/hastings/hastings.pdf; review_level=original-paper-excerpt-and-metadata
Bibliography, summary and opening excerpt of the original paper hosted by a university checked; the publisher DOI could not be opened. This example uses symmetric Gaussian proposals and does not implement a general asymmetric proposal ratio.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## Independent MCMC diagnostic checks: rank Rhat, bulk/tail ESS and degeneracies

Actually process62 byte-identical datasets with separately installed ArviZ0.20.0, bound by recipe/input/chain/official-source hashes. Separate finite-value agreement from explicit degeneracy-policy differences.

**Methods used**

- [Markov-chain Monte Carlo / MCMC](https://hrkoyama.github.io/numerical-methods-atlas/methods/mcmc/?lang=en) (`mcmc`)

**Equations**

[This example’s diagnostic and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/mcmc-diagnostic-reference/?lang=en#mcmc-diagnostic-reference-en-algorithm)

Original equation-based implementation: split with the odd center dropped, average-tie Blom ranks using corrected S+1/4, re-rank folded deviations, and take the larger Rhat. Bulk ESS uses rank-split draws; tail ESS first determines Type7 quantiles on original full draws, then splits <= indicators. Use initial-positive/monotone pairs, declared endpoint handling and tau>=1/log10(total), without clipping antithetic ESS to N.

$$
\widehat R=\sqrt{\widehat V^+/W},\quad\widehat V^+=\tfrac{N-1}{N}W+\tfrac BN
$$

$$
z_s=\Phi^{-1}\!\left(\frac{r_s-3/8}{S+1/4}\right),\quad\widehat R_{\rm rank}=\max(\widehat R_z,\widehat R_{\rm folded})
$$

$$
\widehat N_{\rm eff}=MN/\widehat\tau,\quad\widehat\tau=-1+2\sum_k\widehat P_k,\quad\widehat P_k=\widehat\rho_{2k}+\widehat\rho_{2k+1}
$$

$$
\operatorname{ESS}_{\rm tail}=\min\{\operatorname{ESS}(\mathbf1[X\le q_{.05}]),\operatorname{ESS}(\mathbf1[X\le q_{.95}])\}
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![Independent MCMC diagnostic checks: rank Rhat, bulk/tail ESS and degeneracies: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/results/mcmc-diagnostic-reference.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

No separate physical test problem is assigned to this check or diagnostic. Its own diagnostic figure and validation material are provided.

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/mcmc-diagnostic-reference/?lang=en#mcmc-diagnostic-reference-en-validation)

62 datasets: nine actual chains times three prefixes times x/indicator plus eight small fixtures. Regenerate and hash identical bytes; compare ordinary finite Rhat/ESS/ACF and test constants, zero within-chain variance, odd lengths, ties, shift and scale. Direct lag sums and infinite-series stationary-AR(1) tau=(1+rho)/(1−rho) provide separate checks of finite estimates. Routine runs compare stored references; live ArviZ regeneration is a separate optional procedure.

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.
### Assumptions, units and boundaries

Dimensionless1D target p=.5N(−6,1)+.5N(6,1), mean0/variance37/positive occupancy.5. Three fixed seeds, four chains,1024 warmup and16384 retained draws/chain. Prefixes1024/4096/16384 are nested, not independent replications. Rejections/self-transitions are retained.

**Editorial clarification**

Agreement with an independent library checks diagnostic computation; it does not prove adequate target exploration. Constants and insufficiently varying mode indicators carry explicit states and reasons rather than a reassuring numeric ESS. Negative autocorrelation can yield ESS above the draw count; this is distinct from the conservative floor used in the earlier Gaussian example.

### Adopted numerical method

Original equation-based implementation: split with the odd center dropped, average-tie Blom ranks using corrected S+1/4, re-rank folded deviations, and take the larger Rhat. Bulk ESS uses rank-split draws; tail ESS first determines Type7 quantiles on original full draws, then splits <= indicators. Use initial-positive/monotone pairs, declared endpoint handling and tau>=1/log10(total), without clipping antithetic ESS to N.

$$
\widehat R=\sqrt{\widehat V^+/W},\quad\widehat V^+=\tfrac{N-1}{N}W+\tfrac BN
$$

$$
z_s=\Phi^{-1}\!\left(\frac{r_s-3/8}{S+1/4}\right),\quad\widehat R_{\rm rank}=\max(\widehat R_z,\widehat R_{\rm folded})
$$

$$
\widehat N_{\rm eff}=MN/\widehat\tau,\quad\widehat\tau=-1+2\sum_k\widehat P_k,\quad\widehat P_k=\widehat\rho_{2k}+\widehat\rho_{2k+1}
$$

$$
\operatorname{ESS}_{\rm tail}=\min\{\operatorname{ESS}(\mathbf1[X\le q_{.05}]),\operatorname{ESS}(\mathbf1[X\le q_{.95}])\}
$$

### References and validation

62 datasets: nine actual chains times three prefixes times x/indicator plus eight small fixtures. Regenerate and hash identical bytes; compare ordinary finite Rhat/ESS/ACF and test constants, zero within-chain variance, odd lengths, ties, shift and scale. Direct lag sums and infinite-series stationary-AR(1) tau=(1+rho)/(1−rho) provide separate checks of finite estimates. Routine runs compare stored references; live ArviZ regeneration is a separate optional procedure.

### Limits

An educational fixed-seed, finite-budget experiment. The local Gaussian RW is theoretically irreducible MH; finite-time trapping is not called a nonergodic algorithm. Small Rhat, large ESS and pooled-CDF agreement cannot rule out undiscovered modes. Symmetry-informed reflection is not a generic multimodal solver. No quantum calculations. ArviZ raw constant-ESS=N is not evidence of mixing. Globally identical values yield null/status; differing per-chain constants yield null/infinite-separation Rhat while retaining raw huge-finite/infinite library values outside ordinary finite comparisons. Bulk ESS is not a raw-mean MCSE estimator.

### Stored measurements and decisions

```json
{
  "metrics": {
    "reference_datasets": 62.0,
    "finite_rhat_comparisons": 168,
    "finite_ess_comparisons": 156,
    "global_constant_datasets": 10,
    "global_constant_metric_exclusions": 70,
    "exact_row_rhat_policy_checks": 30,
    "nonfinite_classification_checks": 10,
    "raw_nonfinite_reference_metrics": 62,
    "maximum_rhat_absolute_error": 8.881784197001252e-16,
    "maximum_ess_relative_error": 3.441382313768295e-15,
    "maximum_fft_direct_acov_error": 2.220446049250313e-16,
    "maximum_independent_acf_error": 1.1102230246251565e-16,
    "maximum_ar1_acf_error": 0.010703862071612946,
    "maximum_ar1_tau_relative_error": 0.03641752244252583
  },
  "checks": {
    "dispersed__2026112251__1024__x-rhat_rank": true,
    "dispersed__2026112251__1024__x-rhat_z": true,
    "dispersed__2026112251__1024__x-rhat_folded": true,
    "dispersed__2026112251__1024__x-rhat_split": true,
    "dispersed__2026112251__1024__x-ess_bulk": true,
    "dispersed__2026112251__1024__x-ess_tail": true,
    "dispersed__2026112251__1024__x-ess_mean": true,
    "dispersed__2026112251__1024__x-independent-acf": true,
    "dispersed__2026112251__1024__positive_indicator-rhat_rank-degeneracy-policy": true,
    "dispersed__2026112251__1024__positive_indicator-rhat_z-degeneracy-policy": true,
    "dispersed__2026112251__1024__positive_indicator-rhat_folded": true,
    "dispersed__2026112251__1024__positive_indicator-rhat_split-degeneracy-policy": true,
    "dispersed__2026112251__1024__positive_indicator-ess_bulk": true,
    "dispersed__2026112251__1024__positive_indicator-ess_tail": true,
    "dispersed__2026112251__1024__positive_indicator-ess_mean": true,
    "dispersed__2026112251__4096__x-rhat_rank": true,
    "dispersed__2026112251__4096__x-rhat_z": true,
    "dispersed__2026112251__4096__x-rhat_folded": true,
    "dispersed__2026112251__4096__x-rhat_split": true,
    "dispersed__2026112251__4096__x-ess_bulk": true,
    "dispersed__2026112251__4096__x-ess_tail": true,
    "dispersed__2026112251__4096__x-ess_mean": true,
    "dispersed__2026112251__4096__x-independent-acf": true,
    "dispersed__2026112251__4096__positive_indicator-rhat_rank-degeneracy-policy": true,
    "dispersed__2026112251__4096__positive_indicator-rhat_z-degeneracy-policy": true,
    "dispersed__2026112251__4096__positive_indicator-rhat_folded": true,
    "dispersed__2026112251__4096__positive_indicator-rhat_split-degeneracy-policy": true,
    "dispersed__2026112251__4096__positive_indicator-ess_bulk": true,
    "dispersed__2026112251__4096__positive_indicator-ess_tail": true,
    "dispersed__2026112251__4096__positive_indicator-ess_mean": true,
    "dispersed__2026112251__16384__x-rhat_rank": true,
    "dispersed__2026112251__16384__x-rhat_z": true,
    "dispersed__2026112251__16384__x-rhat_folded": true,
    "dispersed__2026112251__16384__x-rhat_split": true,
    "dispersed__2026112251__16384__x-ess_bulk": true,
    "dispersed__2026112251__16384__x-ess_tail": true,
    "dispersed__2026112251__16384__x-ess_mean": true,
    "dispersed__2026112251__16384__x-independent-acf": true,
    "dispersed__2026112251__16384__positive_indicator-rhat_rank-degeneracy-policy": true,
    "dispersed__2026112251__16384__positive_indicator-rhat_z-degeneracy-policy": true,
    "dispersed__2026112251__16384__positive_indicator-rhat_folded": true,
    "dispersed__2026112251__16384__positive_indicator-rhat_split-degeneracy-policy": true,
    "dispersed__2026112251__16384__positive_indicator-ess_bulk": true,
    "dispersed__2026112251__16384__positive_indicator-ess_tail": true,
    "dispersed__2026112251__16384__positive_indicator-ess_mean": true,
    "dispersed__2026112252__1024__x-rhat_rank": true,
    "dispersed__2026112252__1024__x-rhat_z": true,
    "dispersed__2026112252__1024__x-rhat_folded": true,
    "dispersed__2026112252__1024__x-rhat_split": true,
    "dispersed__2026112252__1024__x-ess_bulk": true,
    "dispersed__2026112252__1024__x-ess_tail": true,
    "dispersed__2026112252__1024__x-ess_mean": true,
    "dispersed__2026112252__1024__x-independent-acf": true,
    "dispersed__2026112252__1024__positive_indicator-rhat_rank-degeneracy-policy": true,
    "dispersed__2026112252__1024__positive_indicator-rhat_z-degeneracy-policy": true,
    "dispersed__2026112252__1024__positive_indicator-rhat_folded": true,
    "dispersed__2026112252__1024__positive_indicator-rhat_split-degeneracy-policy": true,
    "dispersed__2026112252__1024__positive_indicator-ess_bulk": true,
    "dispersed__2026112252__1024__positive_indicator-ess_tail": true,
    "dispersed__2026112252__1024__positive_indicator-ess_mean": true,
    "dispersed__2026112252__4096__x-rhat_rank": true,
    "dispersed__2026112252__4096__x-rhat_z": true,
    "dispersed__2026112252__4096__x-rhat_folded": true,
    "dispersed__2026112252__4096__x-rhat_split": true,
    "dispersed__2026112252__4096__x-ess_bulk": true,
    "dispersed__2026112252__4096__x-ess_tail": true,
    "dispersed__2026112252__4096__x-ess_mean": true,
    "dispersed__2026112252__4096__x-independent-acf": true,
    "dispersed__2026112252__4096__positive_indicator-rhat_rank-degeneracy-policy": true,
    "dispersed__2026112252__4096__positive_indicator-rhat_z-degeneracy-policy": true,
    "dispersed__2026112252__4096__positive_indicator-rhat_folded": true,
    "dispersed__2026112252__4096__positive_indicator-rhat_split-degeneracy-policy": true,
    "dispersed__2026112252__4096__positive_indicator-ess_bulk": true,
    "dispersed__2026112252__4096__positive_indicator-ess_tail": true,
    "dispersed__2026112252__4096__positive_indicator-ess_mean": true,
    "dispersed__2026112252__16384__x-rhat_rank": true,
    "dispersed__2026112252__16384__x-rhat_z": true,
    "dispersed__2026112252__16384__x-rhat_folded": true,
    "dispersed__2026112252__16384__x-rhat_split": true,
    "dispersed__2026112252__16384__x-ess_bulk": true,
    "dispersed__2026112252__16384__x-ess_tail": true,
    "dispersed__2026112252__16384__x-ess_mean": true,
    "dispersed__2026112252__16384__x-independent-acf": true,
    "dispersed__2026112252__16384__positive_indicator-rhat_rank-degeneracy-policy": true,
    "dispersed__2026112252__16384__positive_indicator-rhat_z-degeneracy-policy": true,
    "dispersed__2026112252__16384__positive_indicator-rhat_folded": true,
    "dispersed__2026112252__16384__positive_indicator-rhat_split-degeneracy-policy": true,
    "dispersed__2026112252__16384__positive_indicator-ess_bulk": true,
    "dispersed__2026112252__16384__positive_indicator-ess_tail": true,
    "dispersed__2026112252__16384__positive_indicator-ess_mean": true,
    "dispersed__2026112253__1024__x-rhat_rank": true,
    "dispersed__2026112253__1024__x-rhat_z": true,
    "dispersed__2026112253__1024__x-rhat_folded": true,
    "dispersed__2026112253__1024__x-rhat_split": true,
    "dispersed__2026112253__1024__x-ess_bulk": true,
    "dispersed__2026112253__1024__x-ess_tail": true,
    "dispersed__2026112253__1024__x-ess_mean": true,
    "dispersed__2026112253__1024__x-independent-acf": true,
    "dispersed__2026112253__1024__positive_indicator-rhat_rank-degeneracy-policy": true,
    "dispersed__2026112253__1024__positive_indicator-rhat_z-degeneracy-policy": true,
    "dispersed__2026112253__1024__positive_indicator-rhat_folded": true,
    "dispersed__2026112253__1024__positive_indicator-rhat_split-degeneracy-policy": true,
    "dispersed__2026112253__1024__positive_indicator-ess_bulk": true,
    "dispersed__2026112253__1024__positive_indicator-ess_tail": true,
    "dispersed__2026112253__1024__positive_indicator-ess_mean": true,
    "dispersed__2026112253__4096__x-rhat_rank": true,
    "dispersed__2026112253__4096__x-rhat_z": true,
    "dispersed__2026112253__4096__x-rhat_folded": true,
    "dispersed__2026112253__4096__x-rhat_split": true,
    "dispersed__2026112253__4096__x-ess_bulk": true,
    "dispersed__2026112253__4096__x-ess_tail": true,
    "dispersed__2026112253__4096__x-ess_mean": true,
    "dispersed__2026112253__4096__x-independent-acf": true,
    "dispersed__2026112253__4096__positive_indicator-rhat_rank-degeneracy-policy": true,
    "dispersed__2026112253__4096__positive_indicator-rhat_z-degeneracy-policy": true,
    "dispersed__2026112253__4096__positive_indicator-rhat_folded": true,
    "dispersed__2026112253__4096__positive_indicator-rhat_split-degeneracy-policy": true,
    "dispersed__2026112253__4096__positive_indicator-ess_bulk": true,
    "dispersed__2026112253__4096__positive_indicator-ess_tail": true,
    "dispersed__2026112253__4096__positive_indicator-ess_mean": true,
    "dispersed__2026112253__16384__x-rhat_rank": true,
    "dispersed__2026112253__16384__x-rhat_z": true,
    "dispersed__2026112253__16384__x-rhat_folded": true,
    "dispersed__2026112253__16384__x-rhat_split": true,
    "dispersed__2026112253__16384__x-ess_bulk": true,
    "dispersed__2026112253__16384__x-ess_tail": true,
    "dispersed__2026112253__16384__x-ess_mean": true,
    "dispersed__2026112253__16384__x-independent-acf": true,
    "dispersed__2026112253__16384__positive_indicator-rhat_rank-degeneracy-policy": true,
    "dispersed__2026112253__16384__positive_indicator-rhat_z-degeneracy-policy": true,
    "dispersed__2026112253__16384__positive_indicator-rhat_folded": true,
    "dispersed__2026112253__16384__positive_indicator-rhat_split-degeneracy-policy": true,
    "dispersed__2026112253__16384__positive_indicator-ess_bulk": true,
    "dispersed__2026112253__16384__positive_indicator-ess_tail": true,
    "dispersed__2026112253__16384__positive_indicator-ess_mean": true,
    "same_mode__2026112251__1024__x-rhat_rank": true,
    "same_mode__2026112251__1024__x-rhat_z": true,
    "same_mode__2026112251__1024__x-rhat_folded": true,
    "same_mode__2026112251__1024__x-rhat_split": true,
    "same_mode__2026112251__1024__x-ess_bulk": true,
    "same_mode__2026112251__1024__x-ess_tail": true,
    "same_mode__2026112251__1024__x-ess_mean": true,
    "same_mode__2026112251__1024__x-independent-acf": true,
    "same_mode__2026112251__1024__positive_indicator-constant-undefined": true,
    "same_mode__2026112251__4096__x-rhat_rank": true,
    "same_mode__2026112251__4096__x-rhat_z": true,
    "same_mode__2026112251__4096__x-rhat_folded": true,
    "same_mode__2026112251__4096__x-rhat_split": true,
    "same_mode__2026112251__4096__x-ess_bulk": true,
    "same_mode__2026112251__4096__x-ess_tail": true,
    "same_mode__2026112251__4096__x-ess_mean": true,
    "same_mode__2026112251__4096__x-independent-acf": true,
    "same_mode__2026112251__4096__positive_indicator-constant-undefined": true,
    "same_mode__2026112251__16384__x-rhat_rank": true,
    "same_mode__2026112251__16384__x-rhat_z": true,
    "same_mode__2026112251__16384__x-rhat_folded": true,
    "same_mode__2026112251__16384__x-rhat_split": true,
    "same_mode__2026112251__16384__x-ess_bulk": true,
    "same_mode__2026112251__16384__x-ess_tail": true,
    "same_mode__2026112251__16384__x-ess_mean": true,
    "same_mode__2026112251__16384__x-independent-acf": true,
    "same_mode__2026112251__16384__positive_indicator-constant-undefined": true,
    "same_mode__2026112252__1024__x-rhat_rank": true,
    "same_mode__2026112252__1024__x-rhat_z": true,
    "same_mode__2026112252__1024__x-rhat_folded": true,
    "same_mode__2026112252__1024__x-rhat_split": true,
    "same_mode__2026112252__1024__x-ess_bulk": true,
    "same_mode__2026112252__1024__x-ess_tail": true,
    "same_mode__2026112252__1024__x-ess_mean": true,
    "same_mode__2026112252__1024__x-independent-acf": true,
    "same_mode__2026112252__1024__positive_indicator-constant-undefined": true,
    "same_mode__2026112252__4096__x-rhat_rank": true,
    "same_mode__2026112252__4096__x-rhat_z": true,
    "same_mode__2026112252__4096__x-rhat_folded": true,
    "same_mode__2026112252__4096__x-rhat_split": true,
    "same_mode__2026112252__4096__x-ess_bulk": true,
    "same_mode__2026112252__4096__x-ess_tail": true,
    "same_mode__2026112252__4096__x-ess_mean": true,
    "same_mode__2026112252__4096__x-independent-acf": true,
    "same_mode__2026112252__4096__positive_indicator-constant-undefined": true,
    "same_mode__2026112252__16384__x-rhat_rank": true,
    "same_mode__2026112252__16384__x-rhat_z": true,
    "same_mode__2026112252__16384__x-rhat_folded": true,
    "same_mode__2026112252__16384__x-rhat_split": true,
    "same_mode__2026112252__16384__x-ess_bulk": true,
    "same_mode__2026112252__16384__x-ess_tail": true,
    "same_mode__2026112252__16384__x-ess_mean": true,
    "same_mode__2026112252__16384__x-independent-acf": true,
    "same_mode__2026112252__16384__positive_indicator-constant-undefined": true,
    "same_mode__2026112253__1024__x-rhat_rank": true,
    "same_mode__2026112253__1024__x-rhat_z": true,
    "same_mode__2026112253__1024__x-rhat_folded": true,
    "same_mode__2026112253__1024__x-rhat_split": true,
    "same_mode__2026112253__1024__x-ess_bulk": true,
    "same_mode__2026112253__1024__x-ess_tail": true,
    "same_mode__2026112253__1024__x-ess_mean": true,
    "same_mode__2026112253__1024__x-independent-acf": true,
    "same_mode__2026112253__1024__positive_indicator-constant-undefined": true,
    "same_mode__2026112253__4096__x-rhat_rank": true,
    "same_mode__2026112253__4096__x-rhat_z": true,
    "same_mode__2026112253__4096__x-rhat_folded": true,
    "same_mode__2026112253__4096__x-rhat_split": true,
    "same_mode__2026112253__4096__x-ess_bulk": true,
    "same_mode__2026112253__4096__x-ess_tail": true,
    "same_mode__2026112253__4096__x-ess_mean": true,
    "same_mode__2026112253__4096__x-independent-acf": true,
    "same_mode__2026112253__4096__positive_indicator-constant-undefined": true,
    "same_mode__2026112253__16384__x-rhat_rank": true,
    "same_mode__2026112253__16384__x-rhat_z": true,
    "same_mode__2026112253__16384__x-rhat_folded": true,
    "same_mode__2026112253__16384__x-rhat_split": true,
    "same_mode__2026112253__16384__x-ess_bulk": true,
    "same_mode__2026112253__16384__x-ess_tail": true,
    "same_mode__2026112253__16384__x-ess_mean": true,
    "same_mode__2026112253__16384__x-independent-acf": true,
    "same_mode__2026112253__16384__positive_indicator-constant-undefined": true,
    "mixed__2026112251__1024__x-rhat_rank": true,
    "mixed__2026112251__1024__x-rhat_z": true,
    "mixed__2026112251__1024__x-rhat_folded": true,
    "mixed__2026112251__1024__x-rhat_split": true,
    "mixed__2026112251__1024__x-ess_bulk": true,
    "mixed__2026112251__1024__x-ess_tail": true,
    "mixed__2026112251__1024__x-ess_mean": true,
    "mixed__2026112251__1024__x-independent-acf": true,
    "mixed__2026112251__1024__positive_indicator-rhat_rank": true,
    "mixed__2026112251__1024__positive_indicator-rhat_z": true,
    "mixed__2026112251__1024__positive_indicator-rhat_folded": true,
    "mixed__2026112251__1024__positive_indicator-rhat_split": true,
    "mixed__2026112251__1024__positive_indicator-ess_bulk": true,
    "mixed__2026112251__1024__positive_indicator-ess_tail": true,
    "mixed__2026112251__1024__positive_indicator-ess_mean": true,
    "mixed__2026112251__1024__positive_indicator-independent-acf": true,
    "mixed__2026112251__4096__x-rhat_rank": true,
    "mixed__2026112251__4096__x-rhat_z": true,
    "mixed__2026112251__4096__x-rhat_folded": true,
    "mixed__2026112251__4096__x-rhat_split": true,
    "mixed__2026112251__4096__x-ess_bulk": true,
    "mixed__2026112251__4096__x-ess_tail": true,
    "mixed__2026112251__4096__x-ess_mean": true,
    "mixed__2026112251__4096__x-independent-acf": true,
    "mixed__2026112251__4096__positive_indicator-rhat_rank": true,
    "mixed__2026112251__4096__positive_indicator-rhat_z": true,
    "mixed__2026112251__4096__positive_indicator-rhat_folded": true,
    "mixed__2026112251__4096__positive_indicator-rhat_split": true,
    "mixed__2026112251__4096__positive_indicator-ess_bulk": true,
    "mixed__2026112251__4096__positive_indicator-ess_tail": true,
    "mixed__2026112251__4096__positive_indicator-ess_mean": true,
    "mixed__2026112251__4096__positive_indicator-independent-acf": true,
    "mixed__2026112251__16384__x-rhat_rank": true,
    "mixed__2026112251__16384__x-rhat_z": true,
    "mixed__2026112251__16384__x-rhat_folded": true,
    "mixed__2026112251__16384__x-rhat_split": true,
    "mixed__2026112251__16384__x-ess_bulk": true,
    "mixed__2026112251__16384__x-ess_tail": true,
    "mixed__2026112251__16384__x-ess_mean": true,
    "mixed__2026112251__16384__x-independent-acf": true,
    "mixed__2026112251__16384__positive_indicator-rhat_rank": true,
    "mixed__2026112251__16384__positive_indicator-rhat_z": true,
    "mixed__2026112251__16384__positive_indicator-rhat_folded": true,
    "mixed__2026112251__16384__positive_indicator-rhat_split": true,
    "mixed__2026112251__16384__positive_indicator-ess_bulk": true,
    "mixed__2026112251__16384__positive_indicator-ess_tail": true,
    "mixed__2026112251__16384__positive_indicator-ess_mean": true,
    "mixed__2026112251__16384__positive_indicator-independent-acf": true,
    "mixed__2026112252__1024__x-rhat_rank": true,
    "mixed__2026112252__1024__x-rhat_z": true,
    "mixed__2026112252__1024__x-rhat_folded": true,
    "mixed__2026112252__1024__x-rhat_split": true,
    "mixed__2026112252__1024__x-ess_bulk": true,
    "mixed__2026112252__1024__x-ess_tail": true,
    "mixed__2026112252__1024__x-ess_mean": true,
    "mixed__2026112252__1024__x-independent-acf": true,
    "mixed__2026112252__1024__positive_indicator-rhat_rank": true,
    "mixed__2026112252__1024__positive_indicator-rhat_z": true,
    "mixed__2026112252__1024__positive_indicator-rhat_folded": true,
    "mixed__2026112252__1024__positive_indicator-rhat_split": true,
    "mixed__2026112252__1024__positive_indicator-ess_bulk": true,
    "mixed__2026112252__1024__positive_indicator-ess_tail": true,
    "mixed__2026112252__1024__positive_indicator-ess_mean": true,
    "mixed__2026112252__1024__positive_indicator-independent-acf": true,
    "mixed__2026112252__4096__x-rhat_rank": true,
    "mixed__2026112252__4096__x-rhat_z": true,
    "mixed__2026112252__4096__x-rhat_folded": true,
    "mixed__2026112252__4096__x-rhat_split": true,
    "mixed__2026112252__4096__x-ess_bulk": true,
    "mixed__2026112252__4096__x-ess_tail": true,
    "mixed__2026112252__4096__x-ess_mean": true,
    "mixed__2026112252__4096__x-independent-acf": true,
    "mixed__2026112252__4096__positive_indicator-rhat_rank": true,
    "mixed__2026112252__4096__positive_indicator-rhat_z": true,
    "mixed__2026112252__4096__positive_indicator-rhat_folded": true,
    "mixed__2026112252__4096__positive_indicator-rhat_split": true,
    "mixed__2026112252__4096__positive_indicator-ess_bulk": true,
    "mixed__2026112252__4096__positive_indicator-ess_tail": true,
    "mixed__2026112252__4096__positive_indicator-ess_mean": true,
    "mixed__2026112252__4096__positive_indicator-independent-acf": true,
    "mixed__2026112252__16384__x-rhat_rank": true,
    "mixed__2026112252__16384__x-rhat_z": true,
    "mixed__2026112252__16384__x-rhat_folded": true,
    "mixed__2026112252__16384__x-rhat_split": true,
    "mixed__2026112252__16384__x-ess_bulk": true,
    "mixed__2026112252__16384__x-ess_tail": true,
    "mixed__2026112252__16384__x-ess_mean": true,
    "mixed__2026112252__16384__x-independent-acf": true,
    "mixed__2026112252__16384__positive_indicator-rhat_rank": true,
    "mixed__2026112252__16384__positive_indicator-rhat_z": true,
    "mixed__2026112252__16384__positive_indicator-rhat_folded": true,
    "mixed__2026112252__16384__positive_indicator-rhat_split": true,
    "mixed__2026112252__16384__positive_indicator-ess_bulk": true,
    "mixed__2026112252__16384__positive_indicator-ess_tail": true,
    "mixed__2026112252__16384__positive_indicator-ess_mean": true,
    "mixed__2026112252__16384__positive_indicator-independent-acf": true,
    "mixed__2026112253__1024__x-rhat_rank": true,
    "mixed__2026112253__1024__x-rhat_z": true,
    "mixed__2026112253__1024__x-rhat_folded": true,
    "mixed__2026112253__1024__x-rhat_split": true,
    "mixed__2026112253__1024__x-ess_bulk": true,
    "mixed__2026112253__1024__x-ess_tail": true,
    "mixed__2026112253__1024__x-ess_mean": true,
    "mixed__2026112253__1024__x-independent-acf": true,
    "mixed__2026112253__1024__positive_indicator-rhat_rank": true,
    "mixed__2026112253__1024__positive_indicator-rhat_z": true,
    "mixed__2026112253__1024__positive_indicator-rhat_folded": true,
    "mixed__2026112253__1024__positive_indicator-rhat_split": true,
    "mixed__2026112253__1024__positive_indicator-ess_bulk": true,
    "mixed__2026112253__1024__positive_indicator-ess_tail": true,
    "mixed__2026112253__1024__positive_indicator-ess_mean": true,
    "mixed__2026112253__1024__positive_indicator-independent-acf": true,
    "mixed__2026112253__4096__x-rhat_rank": true,
    "mixed__2026112253__4096__x-rhat_z": true,
    "mixed__2026112253__4096__x-rhat_folded": true,
    "mixed__2026112253__4096__x-rhat_split": true,
    "mixed__2026112253__4096__x-ess_bulk": true,
    "mixed__2026112253__4096__x-ess_tail": true,
    "mixed__2026112253__4096__x-ess_mean": true,
    "mixed__2026112253__4096__x-independent-acf": true,
    "mixed__2026112253__4096__positive_indicator-rhat_rank": true,
    "mixed__2026112253__4096__positive_indicator-rhat_z": true,
    "mixed__2026112253__4096__positive_indicator-rhat_folded": true,
    "mixed__2026112253__4096__positive_indicator-rhat_split": true,
    "mixed__2026112253__4096__positive_indicator-ess_bulk": true,
    "mixed__2026112253__4096__positive_indicator-ess_tail": true,
    "mixed__2026112253__4096__positive_indicator-ess_mean": true,
    "mixed__2026112253__4096__positive_indicator-independent-acf": true,
    "mixed__2026112253__16384__x-rhat_rank": true,
    "mixed__2026112253__16384__x-rhat_z": true,
    "mixed__2026112253__16384__x-rhat_folded": true,
    "mixed__2026112253__16384__x-rhat_split": true,
    "mixed__2026112253__16384__x-ess_bulk": true,
    "mixed__2026112253__16384__x-ess_tail": true,
    "mixed__2026112253__16384__x-ess_mean": true,
    "mixed__2026112253__16384__x-independent-acf": true,
    "mixed__2026112253__16384__positive_indicator-rhat_rank": true,
    "mixed__2026112253__16384__positive_indicator-rhat_z": true,
    "mixed__2026112253__16384__positive_indicator-rhat_folded": true,
    "mixed__2026112253__16384__positive_indicator-rhat_split": true,
    "mixed__2026112253__16384__positive_indicator-ess_bulk": true,
    "mixed__2026112253__16384__positive_indicator-ess_tail": true,
    "mixed__2026112253__16384__positive_indicator-ess_mean": true,
    "mixed__2026112253__16384__positive_indicator-independent-acf": true,
    "edge__iid-rhat_rank": true,
    "edge__iid-rhat_z": true,
    "edge__iid-rhat_folded": true,
    "edge__iid-rhat_split": true,
    "edge__iid-ess_bulk": true,
    "edge__iid-ess_tail": true,
    "edge__iid-ess_mean": true,
    "edge__iid-independent-acf": true,
    "edge__odd-rhat_rank": true,
    "edge__odd-rhat_z": true,
    "edge__odd-rhat_folded": true,
    "edge__odd-rhat_split": true,
    "edge__odd-ess_bulk": true,
    "edge__odd-ess_tail": true,
    "edge__odd-ess_mean": true,
    "edge__odd-independent-acf": true,
    "edge__ties-rhat_rank": true,
    "edge__ties-rhat_z": true,
    "edge__ties-rhat_folded": true,
    "edge__ties-rhat_split": true,
    "edge__ties-ess_bulk": true,
    "edge__ties-ess_tail": true,
    "edge__ties-ess_mean": true,
    "edge__ties-independent-acf": true,
    "edge__scale-rhat_rank": true,
    "edge__scale-rhat_z": true,
    "edge__scale-rhat_folded": true,
    "edge__scale-rhat_split": true,
    "edge__scale-ess_bulk": true,
    "edge__scale-ess_tail": true,
    "edge__scale-ess_mean": true,
    "edge__scale-independent-acf": true,
    "edge__shift-rhat_rank": true,
    "edge__shift-rhat_z": true,
    "edge__shift-rhat_folded": true,
    "edge__shift-rhat_split": true,
    "edge__shift-ess_bulk": true,
    "edge__shift-ess_tail": true,
    "edge__shift-ess_mean": true,
    "edge__shift-independent-acf": true,
    "edge__antithetic-rhat_rank": true,
    "edge__antithetic-rhat_z": true,
    "edge__antithetic-rhat_folded": true,
    "edge__antithetic-rhat_split": true,
    "edge__antithetic-ess_bulk": true,
    "edge__antithetic-ess_tail": true,
    "edge__antithetic-ess_mean": true,
    "edge__antithetic-independent-acf": true,
    "edge__constant-constant-undefined": true,
    "edge__separated_constants-rhat_rank-degeneracy-policy": true,
    "edge__separated_constants-rhat_z-degeneracy-policy": true,
    "edge__separated_constants-rhat_folded": true,
    "edge__separated_constants-rhat_split-degeneracy-policy": true,
    "edge__separated_constants-ess_bulk": true,
    "edge__separated_constants-ess_tail": true,
    "edge__separated_constants-ess_mean": true,
    "iid_effective_size_scale": true,
    "folding_detects_scale_difference": true,
    "rank_detects_shift": true,
    "antithetic_ess_can_exceed_draws": true,
    "ar1_acf": true,
    "ar1_tau": true,
    "ar1_fft_vs_direct": true,
    "all_reference_metric_slots_accounted_for": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/mcmc-diagnostic-reference/index.json

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/atlas-mcmc-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- A. Vehtari, A. Gelman, D. Simpson, B. Carpenter and P.-C. Bürkner (2021). Rank-Normalization, Folding, and Localization: An Improved R-hat for Assessing Convergence of MCMC (with Discussion). https://paulbuerkner.com/publications/pdf/2021__Vehtari_et_al__Bayesian_Analysis.pdf; review_level=corrected-author-paper-selected-sections
Checked original sections3–4, the2021-06-22 correction of Eq4.1 to denominator S+1/4, and the constant-indicator warning. This does not reproduce every original numerical experiment.

- C. J. Geyer (1992). Practical Markov Chain Monte Carlo. https://www2.stat.duke.edu/~scs/Courses/Stat376/Papers/GeyerStatSci1992.pdf; review_level=original-selected-paired-sequence-theory
Checked section3.3 and Theorems3.1/3.2 for reversibility assumptions and initial-positive/monotone sequences. Main article pp473–483 are distinguished from combined discussion pagination; no claim gives exact true ESS from finite chains.

- A. Gelman and D. B. Rubin (1992). Inference from Iterative Simulation Using Multiple Sequences. https://www2.stat.duke.edu/~scs/Courses/Stat376/Papers/ConvergeDiagnostics/GelmanRubinStatSci1992.pdf; review_level=original-selected-multiple-chain-starting-points
Checked the original introduction/section2 on multiple sequences and overdispersed starts. Distinct from the later rank/folded method, and not a reproduction of every1992 finite-sample correction.

- The ArviZ developers (2024). ArviZ0.20.0 public diagnostics API and tagged source. https://python.arviz.org/en/v0.20.0/api/generated/arviz.rhat.html; review_level=official-versioned-source-and-actual-independent-execution
Checked the official0.20.0 rhat/ess API and tagged source for splitting, ranks, Type7 quantiles, endpoints and constant conventions. Installed source hashes match commit94113176cae99a05ba41d1e93739ee2d5bdbe9b1;62 byte-identical datasets were actually processed in a separate environment without importing Atlas diagnostics. No upstream implementation is reproduced; values, versions, hashes and regeneration code are supplied.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
