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

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

対応する方程式一覧の項目は未登録です。

#### 問題の図 (`method-problems-ja`)

##### [Gaussian標的のMCMC：分布・自己相関・ESS](https://hrkoyama.github.io/numerical-methods-atlas/problems/gaussian-mcmc/?lang=ja) (`gaussian-mcmc`)

![標準正規標的・固定seedの32連鎖。保存したCDF検査点、標本予算ごとの連鎖平均RMSE・平均観測量のESSを表示。全seedの保証ではない。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/gaussian-mcmc.png)

この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/gaussian-mcmc/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/gaussian-mcmc/?lang=ja#code-ja)

- [Gaussian標的のMCMC：分布・自己相関・ESS](https://hrkoyama.github.io/numerical-methods-atlas/validation/gaussian-mcmc/?lang=ja) (`gaussian-mcmc`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip)

32本のMetropolis連鎖を既知の標準正規分布へ照合し、平均・分散・CDF、自己相関時間、ESSと標本予算依存を記録します。

##### [多峰性MCMC：峰への閉じ込め・偽の安心・大域提案](https://hrkoyama.github.io/numerical-methods-atlas/problems/mcmc-bimodal-mixture/?lang=ja) (`mcmc-bimodal-mixture`)

![同じ2峰密度を、分散初期値の局所MH・同じ峰からの局所MH・対称reflectionを混ぜるMHで比較。期待した混合不良の検出と、実際の峰間移動を分けて検証します。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/results/mcmc-multimodal-mixing.png)

この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/mcmc-bimodal-mixture/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/mcmc-bimodal-mixture/?lang=ja#code-ja)

- [多峰性MCMC：峰への閉じ込め・偽の安心・大域提案](https://hrkoyama.github.io/numerical-methods-atlas/validation/mcmc-multimodal-mixing/?lang=ja) (`mcmc-multimodal-mixing`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/atlas-mcmc-2026-11-22.zip)

同じ2峰密度を、分散初期値の局所MH・同じ峰からの局所MH・対称reflectionを混ぜるMHで比較。期待した混合不良の検出と、実際の峰間移動を分けて検証します。


#### 厳密解・参照解 (`method-references-ja`)

##### [Gaussian標的のMCMC：分布・自己相関・ESS](https://hrkoyama.github.io/numerical-methods-atlas/problems/gaussian-mcmc/?lang=ja#references-ja) (`gaussian-mcmc`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### [多峰性MCMC：峰への閉じ込め・偽の安心・大域提案](https://hrkoyama.github.io/numerical-methods-atlas/problems/mcmc-bimodal-mixture/?lang=ja#references-ja) (`mcmc-bimodal-mixture`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/mcmc/)
- 保存結果: [この配布版の保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/result.json)
- 検証記録: [配布版の検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/verification.json)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

##### Gaussian標的のMCMC：分布・自己相関・ESS (`gaussian-mcmc`)

[Gaussian標的のMCMC：分布・自己相関・ESS](https://hrkoyama.github.io/numerical-methods-atlas/problems/gaussian-mcmc/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/gaussian-mcmc/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/verification.json)

32本のMetropolis連鎖を既知の標準正規分布へ照合し、平均・分散・CDF、自己相関時間、ESSと標本予算依存を記録します。

##### 多峰性MCMC：峰への閉じ込め・偽の安心・大域提案 (`mcmc-multimodal-mixing`)

[多峰性MCMC：峰への閉じ込め・偽の安心・大域提案](https://hrkoyama.github.io/numerical-methods-atlas/problems/mcmc-bimodal-mixture/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/mcmc-multimodal-mixing/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/atlas-mcmc-2026-11-22.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/verification.json)

同じ2峰密度を、分散初期値の局所MH・同じ峰からの局所MH・対称reflectionを混ぜるMHで比較。期待した混合不良の検出と、実際の峰間移動を分けて検証します。

##### 問題図との対応付けとは別の登録実行・検査例

- [mcmc-diagnostic-reference](https://hrkoyama.github.io/numerical-methods-atlas/validation/mcmc-diagnostic-reference/?lang=ja) (`mcmc-diagnostic-reference`)

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

Gaussian標的のMCMC：分布・自己相関・ESS: 32本のMetropolis連鎖を既知の標準正規分布へ照合し、平均・分散・CDF、自己相関時間、ESSと標本予算依存を記録します。 多峰性MCMC：峰への閉じ込め・偽の安心・大域提案: 同じ2峰密度を、分散初期値の局所MH・同じ峰からの局所MH・対称reflectionを混ぜるMHで比較。期待した混合不良の検出と、実際の峰間移動を分けて検証します。 MCMC診断の独立照合：rank Rhat・bulk/tail ESS・退化条件: 同一鎖の62datasetを別環境ArviZ0.20.0で実計算し、固定recipe・入力・鎖・公式ソースSHAで結びます。通常の有限値照合と、不定値のpolicy差を分けて検査します。

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip)

[配布版の検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/verification.json)

###### 関連ソース

- [/code/validated-examples/2026-11-22/models/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/run.py)
- [/code/validated-examples/2026-11-22/models/models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/models.py)
- [/code/validated-examples/2026-11-22/mcmc/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/run.py)
- [/code/validated-examples/2026-11-22/mcmc/sampler.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/sampler.py)
- [/code/validated-examples/2026-11-22/mcmc/diagnostics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/diagnostics.py)
- [/code/validated-examples/2026-11-22/mcmc/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/experiments.py)
- [/code/validated-examples/2026-11-22/mcmc/fixtures.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/fixtures.py)
- [/code/validated-examples/2026-11-22/mcmc/generate-arviz-reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/generate-arviz-reference.py)
- [/code/validated-examples/2026-11-22/mcmc/prepare-reference-input.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/prepare-reference-input.py)

###### 配布版のテスト

- [/code/validated-examples/2026-11-22/models/test_models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/test_models.py)
- [/code/validated-examples/2026-11-22/mcmc/test_mcmc.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/test_mcmc.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q
python run.py --input inputs.json --output output
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

No corresponding equation-registry entry is registered.

#### Problem figures (`method-problems-en`)

##### [Gaussian-target MCMC: distribution, autocorrelation and ESS](https://hrkoyama.github.io/numerical-methods-atlas/problems/gaussian-mcmc/?lang=en) (`gaussian-mcmc`)

![Standard-normal target and 32 fixed-seed chains: stored CDF checkpoints, chain-mean RMSE and mean-observable ESS by sample budget. Not an every-seed guarantee.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/gaussian-mcmc.png)

Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/gaussian-mcmc/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/gaussian-mcmc/?lang=en#code-en)

- [Gaussian-target MCMC: distribution, autocorrelation and ESS](https://hrkoyama.github.io/numerical-methods-atlas/validation/gaussian-mcmc/?lang=en) (`gaussian-mcmc`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip)

Check 32 Metropolis chains against a known standard-normal target; record mean, variance, CDF, autocorrelation time, ESS and sample-budget dependence.

##### [Multimodal MCMC: trapping, false reassurance and a global proposal](https://hrkoyama.github.io/numerical-methods-atlas/problems/mcmc-bimodal-mixture/?lang=en) (`mcmc-bimodal-mixture`)

![Compare dispersed local MH, same-mode local MH and symmetry-informed reflection/local MH on the same bimodal target. Separate detecting expected mixing failures from successful finite-budget mode exploration.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/results/mcmc-multimodal-mixing.png)

Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/mcmc-bimodal-mixture/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/mcmc-bimodal-mixture/?lang=en#code-en)

- [Multimodal MCMC: trapping, false reassurance and a global proposal](https://hrkoyama.github.io/numerical-methods-atlas/validation/mcmc-multimodal-mixing/?lang=en) (`mcmc-multimodal-mixing`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/atlas-mcmc-2026-11-22.zip)

Compare dispersed local MH, same-mode local MH and symmetry-informed reflection/local MH on the same bimodal target. Separate detecting expected mixing failures from successful finite-budget mode exploration.


#### Exact / reference solutions (`method-references-en`)

##### [Gaussian-target MCMC: distribution, autocorrelation and ESS](https://hrkoyama.github.io/numerical-methods-atlas/problems/gaussian-mcmc/?lang=en#references-en) (`gaussian-mcmc`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### [Multimodal MCMC: trapping, false reassurance and a global proposal](https://hrkoyama.github.io/numerical-methods-atlas/problems/mcmc-bimodal-mixture/?lang=en#references-en) (`mcmc-bimodal-mixture`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/mcmc/)
- Saved result: [Saved results from this edition](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/result.json)
- Verification receipt: [Edition verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/verification.json)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

##### Gaussian-target MCMC: distribution, autocorrelation and ESS (`gaussian-mcmc`)

[Gaussian-target MCMC: distribution, autocorrelation and ESS](https://hrkoyama.github.io/numerical-methods-atlas/problems/gaussian-mcmc/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/gaussian-mcmc/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/verification.json)

Check 32 Metropolis chains against a known standard-normal target; record mean, variance, CDF, autocorrelation time, ESS and sample-budget dependence.

##### Multimodal MCMC: trapping, false reassurance and a global proposal (`mcmc-multimodal-mixing`)

[Multimodal MCMC: trapping, false reassurance and a global proposal](https://hrkoyama.github.io/numerical-methods-atlas/problems/mcmc-bimodal-mixture/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/mcmc-multimodal-mixing/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/atlas-mcmc-2026-11-22.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/verification.json)

Compare dispersed local MH, same-mode local MH and symmetry-informed reflection/local MH on the same bimodal target. Separate detecting expected mixing failures from successful finite-budget mode exploration.

##### Registered executions and checks separate from problem-figure links

- [mcmc-diagnostic-reference](https://hrkoyama.github.io/numerical-methods-atlas/validation/mcmc-diagnostic-reference/?lang=en) (`mcmc-diagnostic-reference`)

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Gaussian-target MCMC: distribution, autocorrelation and ESS: Check 32 Metropolis chains against a known standard-normal target; record mean, variance, CDF, autocorrelation time, ESS and sample-budget dependence. Multimodal MCMC: trapping, false reassurance and a global proposal: Compare dispersed local MH, same-mode local MH and symmetry-informed reflection/local MH on the same bimodal target. Separate detecting expected mixing failures from successful finite-budget mode exploration. Independent MCMC diagnostic checks: rank Rhat, bulk/tail ESS and degeneracies: Actually process62 byte-identical datasets with separately installed ArviZ0.20.0, bound by recipe/input/chain/official-source hashes. Separate finite-value agreement from explicit degeneracy-policy differences.

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[Related code edition / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip)

[Edition verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/verification.json)

###### Related source

- [/code/validated-examples/2026-11-22/models/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/run.py)
- [/code/validated-examples/2026-11-22/models/models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/models.py)
- [/code/validated-examples/2026-11-22/mcmc/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/run.py)
- [/code/validated-examples/2026-11-22/mcmc/sampler.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/sampler.py)
- [/code/validated-examples/2026-11-22/mcmc/diagnostics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/diagnostics.py)
- [/code/validated-examples/2026-11-22/mcmc/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/experiments.py)
- [/code/validated-examples/2026-11-22/mcmc/fixtures.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/fixtures.py)
- [/code/validated-examples/2026-11-22/mcmc/generate-arviz-reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/generate-arviz-reference.py)
- [/code/validated-examples/2026-11-22/mcmc/prepare-reference-input.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/prepare-reference-input.py)

###### Package tests

- [/code/validated-examples/2026-11-22/models/test_models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/test_models.py)
- [/code/validated-examples/2026-11-22/mcmc/test_mcmc.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/test_mcmc.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q
python run.py --input inputs.json --output output
```
