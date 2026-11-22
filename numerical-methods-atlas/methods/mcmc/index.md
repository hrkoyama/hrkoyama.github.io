# Markov-chain Monte Carlo / MCMC / Markov連鎖Monte Carlo

Status: educational-example

Gaussian-target MCMC: distribution, autocorrelation and ESS: Check 32 Metropolis chains against a known standard-normal target; record mean, variance, CDF, autocorrelation time, ESS and sample-budget dependence. Multimodal MCMC: trapping, false reassurance and a global proposal: Compare dispersed local MH, same-mode local MH and symmetry-informed reflection/local MH on the same bimodal target. Separate detecting expected mixing failures from successful finite-budget mode exploration. Independent MCMC diagnostic checks: rank Rhat, bulk/tail ESS and degeneracies: Actually process62 byte-identical datasets with separately installed ArviZ0.20.0, bound by recipe/input/chain/official-source hashes. Separate finite-value agreement from explicit degeneracy-policy differences.

Gaussian標的のMCMC：分布・自己相関・ESS: 32本のMetropolis連鎖を既知の標準正規分布へ照合し、平均・分散・CDF、自己相関時間、ESSと標本予算依存を記録します。 多峰性MCMC：峰への閉じ込め・偽の安心・大域提案: 同じ2峰密度を、分散初期値の局所MH・同じ峰からの局所MH・対称reflectionを混ぜるMHで比較。期待した混合不良の検出と、実際の峰間移動を分けて検証します。 MCMC診断の独立照合：rank Rhat・bulk/tail ESS・退化条件: 同一鎖の62datasetを別環境ArviZ0.20.0で実計算し、固定recipe・入力・鎖・公式ソースSHAで結びます。通常の有限値照合と、不定値のpolicy差を分けて検査します。

Gaussian-target MCMC: distribution, autocorrelation and ESS: Statistical checks apply to fixed seeds and budgets. ESS concerns the mean only; Rhat is not rank-normalized. No guarantee covers multimodality, high dimensions, every seed, mixing or a specified false-positive rate. Multimodal MCMC: trapping, false reassurance and a global proposal: An educational fixed-seed, finite-budget experiment. The local Gaussian RW is theoretically irreducible MH; finite-time trapping is not called a nonergodic algorithm. Small Rhat, large ESS and pooled-CDF agreement cannot rule out undiscovered modes. Symmetry-informed reflection is not a generic multimodal solver. No quantum calculations. Independent MCMC diagnostic checks: rank Rhat, bulk/tail ESS and degeneracies: An educational fixed-seed, finite-budget experiment. The local Gaussian RW is theoretically irreducible MH; finite-time trapping is not called a nonergodic algorithm. Small Rhat, large ESS and pooled-CDF agreement cannot rule out undiscovered modes. Symmetry-informed reflection is not a generic multimodal solver. No quantum calculations. ArviZ raw constant-ESS=N is not evidence of mixing. Globally identical values yield null/status; differing per-chain constants yield null/infinite-separation Rhat while retaining raw huge-finite/infinite library values outside ordinary finite comparisons. Bulk ESS is not a raw-mean MCSE estimator.

Other names: MCMC法, Markov chain Monte Carlo, マルコフ連鎖モンテカルロ, マルコフ連鎖Monte Carlo

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/mcmc/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/mcmc/



- Reference: https://doi.org/10.1063/1.1699114 — Method-specific source; see the detailed reading for source role and actual review depth.
- Reference: https://doi.org/10.1093/biomet/57.1.97 — Method-specific source; see the detailed reading for source role and actual review depth.

## Small fixed-input validation supplements

Gaussian-target MCMC: distribution, autocorrelation and ESS: Check 32 Metropolis chains against a known standard-normal target; record mean, variance, CDF, autocorrelation time, ESS and sample-budget dependence. Multimodal MCMC: trapping, false reassurance and a global proposal: Compare dispersed local MH, same-mode local MH and symmetry-informed reflection/local MH on the same bimodal target. Separate detecting expected mixing failures from successful finite-budget mode exploration. Independent MCMC diagnostic checks: rank Rhat, bulk/tail ESS and degeneracies: Actually process62 byte-identical datasets with separately installed ArviZ0.20.0, bound by recipe/input/chain/official-source hashes. Separate finite-value agreement from explicit degeneracy-policy differences.

Gaussian標的のMCMC：分布・自己相関・ESS: 32本のMetropolis連鎖を既知の標準正規分布へ照合し、平均・分散・CDF、自己相関時間、ESSと標本予算依存を記録します。 多峰性MCMC：峰への閉じ込め・偽の安心・大域提案: 同じ2峰密度を、分散初期値の局所MH・同じ峰からの局所MH・対称reflectionを混ぜるMHで比較。期待した混合不良の検出と、実際の峰間移動を分けて検証します。 MCMC診断の独立照合：rank Rhat・bulk/tail ESS・退化条件: 同一鎖の62datasetを別環境ArviZ0.20.0で実計算し、固定recipe・入力・鎖・公式ソースSHAで結びます。通常の有限値照合と、不定値のpolicy差を分けて検査します。

- Gaussian-target MCMC: distribution, autocorrelation and ESS: https://hrkoyama.github.io/numerical-methods-atlas/validation/gaussian-mcmc/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/result.json

- Multimodal MCMC: trapping, false reassurance and a global proposal: https://hrkoyama.github.io/numerical-methods-atlas/validation/mcmc-multimodal-mixing/
- Independent MCMC diagnostic checks: rank Rhat, bulk/tail ESS and degeneracies: https://hrkoyama.github.io/numerical-methods-atlas/validation/mcmc-diagnostic-reference/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/atlas-mcmc-2026-11-22.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/results/result.json

Common execution records: [{"id": "gaussian-mcmc", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/gaussian-mcmc/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/gaussian-mcmc/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "mcmc-multimodal-mixing", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/mcmc-multimodal-mixing/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/mcmc-multimodal-mixing/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "mcmc-diagnostic-reference", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/mcmc-diagnostic-reference/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/mcmc-diagnostic-reference/?lang=en"}, "kind": "dedicated-supplement"}]

Next: Preserve the published fixed-input scope; validate conditions, references and criteria separately for extensions.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/mcmc/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/
