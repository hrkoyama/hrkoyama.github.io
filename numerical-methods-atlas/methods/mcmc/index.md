# Markov-chain Monte Carlo / MCMC / Markov連鎖Monte Carlo

Status: educational-example

Check 32 Metropolis chains against a known standard-normal target; record mean, variance, CDF, autocorrelation time, ESS and sample-budget dependence.

32本のMetropolis連鎖を既知の標準正規分布へ照合し、平均・分散・CDF、自己相関時間、ESSと標本予算依存を記録します。

Statistical checks apply to fixed seeds and budgets. ESS concerns the mean only; Rhat is not rank-normalized. No guarantee covers multimodality, high dimensions, every seed, mixing or a specified false-positive rate.

Other names: MCMC法, Markov chain Monte Carlo, マルコフ連鎖モンテカルロ, マルコフ連鎖Monte Carlo

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/mcmc/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/mcmc/



- Reference: https://doi.org/10.1063/1.1699114 — Method-specific source; see the detailed reading for source role and actual review depth.
- Reference: https://doi.org/10.1093/biomet/57.1.97 — Method-specific source; see the detailed reading for source role and actual review depth.

## Small fixed-input validation supplement

Check 32 Metropolis chains against a known standard-normal target; record mean, variance, CDF, autocorrelation time, ESS and sample-budget dependence.

32本のMetropolis連鎖を既知の標準正規分布へ照合し、平均・分散・CDF、自己相関時間、ESSと標本予算依存を記録します。

- Gaussian-target MCMC: distribution, autocorrelation and ESS: https://hrkoyama.github.io/numerical-methods-atlas/validation/gaussian-mcmc/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/result.json

Common execution records: [{"id": "gaussian-mcmc", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/gaussian-mcmc/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/gaussian-mcmc/?lang=en"}, "kind": "dedicated-supplement"}]

Next: Preserve the published fixed-input scope; validate conditions, references and criteria separately for extensions.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/mcmc/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/
