# Monte Carlo integration / Monte Carlo積分

Status: educational-example

Connect random samples, variance and integration error. Additional fixed examples: Ordinary importance sampling of a normal rare tail. See each release for assumptions and checked scope.

乱数・標本数・分散と積分誤差をつなぐ。 追加固定例：正規稀少尾の通常importance sampling。条件と検証範囲は各配布版で確認してください。

Integrate x² under U[0,1]. Compare 256 independent seeds with analytic integral and variance, checking N^-1/2 RMS scaling and interval coverage. Excludes MCMC and rare events. Additional fixed examples: Bernoulli exact intervals are not applied to weighted IS.64trials do not prove general95%coverage;nested prefixes are not extra independent replicates. Global weightESS and eventESS are distinct.

Other names: モンテカルロ法, モンテカルロ積分, Monte Carlo method, Monte Carlo integration

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/monte-carlo/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/monte-carlo/



- Reference: https://doi.org/10.1080/01621459.1949.10483310 — Method-specific source; see the detailed reading for source role and actual review depth.

Scoped example: Integrate x² under U[0,1]. Compare 256 independent seeds with analytic integral and variance, checking N^-1/2 RMS scaling and interval coverage. Excludes MCMC and rare events.

Code: https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/models.py
Tests: https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/test_models.py
Download: https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/model-benchmarks-2026-11-22.zip
Verification: https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/verification.json

## Small fixed-input validation supplements

Additional fixed examples: Ordinary importance sampling of a normal rare tail. See each release for assumptions and checked scope. Bernoulli exact intervals are not applied to weighted IS.64trials do not prove general95%coverage;nested prefixes are not extra independent replicates. Global weightESS and eventESS are distinct.

追加固定例：正規稀少尾の通常importance sampling。条件と検証範囲は各配布版で確認してください。 重み付きISへBernoulliの厳密区間を転用しません。64反復は一般95%被覆の証明でなく、nestedprefixを独立反復へ水増ししません。global weightESSと事象ESSは別です。

- Ordinary importance sampling of a normal rare tail: https://hrkoyama.github.io/numerical-methods-atlas/validation/normal-tail-importance/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/atlas-stochastic-estimation-2026-11-24.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/results/result.json

Common execution records: [{"id": "mc-integral", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=ja#mc-integral-ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=en#mc-integral-en"}}, {"id": "normal-tail-importance", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/normal-tail-importance/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/normal-tail-importance/?lang=en"}, "kind": "dedicated-supplement"}]

Next: Add validation against another reference problem before extending application scope.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/monte-carlo/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [Gaussian確率測度：尾確率と相関標的](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#gaussian-probability-model-ja) (`gaussian-probability-model`; normal-tail-importance)

#### 問題の図 (`method-problems-ja`)

##### [Monte Carlo：256 seedの積分誤差と区間被覆](https://hrkoyama.github.io/numerical-methods-atlas/problems/mc-integral/?lang=ja) (`mc-integral`)

![公開した固定入力と同じ計算結果。解・解析参照または独立参照・誤差を図示。数値条件とCSVを実行ページに保存。](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/results/mc-integral/preview.png)

この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/mc-integral/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/mc-integral/?lang=ja#code-ja)

- [Monte Carlo：256 seedの積分誤差と区間被覆](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/mc-integral/?lang=ja) (`mc-integral`) · [コードZIP](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/model-benchmarks-2026-11-22.zip)

U[0,1]でx²を積分。256の独立seedで解析積分・分散と比較し、Nの平方根に反比例するRMS誤差と区間被覆を確認。MCMC・希少事象は対象外。

##### [正規稀少尾の通常importance sampling](https://hrkoyama.github.io/numerical-methods-atlas/problems/normal-tail-importance/?lang=ja) (`normal-tail-importance`)

![保存した実データ由来の分布・誤差診断。空間次元と標本/時間軸を区別します。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/results/normal-tail-importance-preview.png)

Y=1(X>a)exp(-aX+a²/2)の通常平均。ランダムな重み総和で割らず、proposal調整なし。直接MCの無hitは0のまま保存しCP区間を付けます。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/normal-tail-importance/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/normal-tail-importance/?lang=ja#code-ja)

- [正規稀少尾の通常importance sampling](https://hrkoyama.github.io/numerical-methods-atlas/validation/normal-tail-importance/?lang=ja) (`normal-tail-importance`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/atlas-stochastic-estimation-2026-11-24.zip)

通常の尤度比平均を解析モーメント・独立seed分散・有限被覆診断で確認。


#### 厳密解・参照解 (`method-references-ja`)

##### [Monte Carlo：256 seedの積分誤差と区間被覆](https://hrkoyama.github.io/numerical-methods-atlas/problems/mc-integral/?lang=ja#references-ja) (`mc-integral`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### [正規稀少尾の通常importance sampling](https://hrkoyama.github.io/numerical-methods-atlas/problems/normal-tail-importance/?lang=ja#references-ja) (`normal-tail-importance`)

- [正規稀少尾の通常importance sampling](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-normal-tail-importance-ja) (`normal-tail-importance`; 同じ問題の参照; 解析参照)

重み付きISへBernoulliの厳密区間を転用しません。64反復は一般95%被覆の証明でなく、nestedprefixを独立反復へ水増ししません。global weightESSと事象ESSは別です。

[既存の参照図](/numerical-methods-atlas/validation/normal-tail-importance/?lang=ja#normal-tail-importance-ja-measurements)

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/monte-carlo/)
- 検証記録: [配布版の検証記録](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/verification.json)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

##### Monte Carlo：256 seedの積分誤差と区間被覆 (`mc-integral`)

[Monte Carlo：256 seedの積分誤差と区間被覆](https://hrkoyama.github.io/numerical-methods-atlas/problems/mc-integral/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/mc-integral/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/model-benchmarks-2026-11-22.zip)

[固定入力](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/inputs/mc-integral.json)

[検証記録](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

U[0,1]でx²を積分。256の独立seedで解析積分・分散と比較し、Nの平方根に反比例するRMS誤差と区間被覆を確認。MCMC・希少事象は対象外。

##### 正規稀少尾の通常importance sampling (`normal-tail-importance`)

[正規稀少尾の通常importance sampling](https://hrkoyama.github.io/numerical-methods-atlas/problems/normal-tail-importance/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/normal-tail-importance/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/atlas-stochastic-estimation-2026-11-24.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/verification.json)

通常の尤度比平均を解析モーメント・独立seed分散・有限被覆診断で確認。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

追加固定例：正規稀少尾の通常importance sampling。条件と検証範囲は各配布版で確認してください。 重み付きISへBernoulliの厳密区間を転用しません。64反復は一般95%被覆の証明でなく、nestedprefixを独立反復へ水増ししません。global weightESSと事象ESSは別です。

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/model-benchmarks-2026-11-22.zip)

[配布版の検証記録](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/verification.json)

###### 関連ソース

- [/code/model-benchmarks/2026-11-22/models.py](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/models.py)
- [/code/model-benchmarks/2026-11-22/run.py](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/run.py)
- [/code/validated-examples/2026-11-24/stochastic-estimation/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/run.py)
- [/code/validated-examples/2026-11-24/stochastic-estimation/importance.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/importance.py)
- [/code/validated-examples/2026-11-24/stochastic-estimation/sampler.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/sampler.py)
- [/code/validated-examples/2026-11-24/stochastic-estimation/diagnostics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/diagnostics.py)
- [/code/validated-examples/2026-11-24/stochastic-estimation/support.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/support.py)
- [/code/validated-examples/2026-11-24/stochastic-estimation/references/generate_arviz.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/references/generate_arviz.py)
- [/code/validated-examples/2026-11-24/stochastic-estimation/references/prepare.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/references/prepare.py)
- [/code/validated-examples/2026-11-24/stochastic-estimation/references/qualify_arviz.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/references/qualify_arviz.py)
- [/code/validated-examples/2026-11-24/stochastic-estimation/references/qualify_is.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/references/qualify_is.py)

###### 配布版のテスト

- [/code/model-benchmarks/2026-11-22/test_models.py](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/test_models.py)
- [/code/validated-examples/2026-11-24/stochastic-estimation/test_driver_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/test_driver_contract.py)
- [/code/validated-examples/2026-11-24/stochastic-estimation/test_estimators.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/test_estimators.py)
- [/code/validated-examples/2026-11-24/stochastic-estimation/test_fixture_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/test_fixture_contract.py)
- [/code/validated-examples/2026-11-24/stochastic-estimation/test_tail_quantiles.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/test_tail_quantiles.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python run.py --input inputs/mc-integral.json --output output
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Gaussian probability measures: tails and correlated targets](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#gaussian-probability-model-en) (`gaussian-probability-model`; normal-tail-importance)

#### Problem figures (`method-problems-en`)

##### [Monte Carlo: integral errors and interval coverage across 256 seeds](https://hrkoyama.github.io/numerical-methods-atlas/problems/mc-integral/?lang=en) (`mc-integral`)

![The same public fixed-input calculation. Shows solutions, analytic/independent references or errors; numerical criteria and CSV are linked in the execution entry.](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/results/mc-integral/preview.png)

Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/mc-integral/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/mc-integral/?lang=en#code-en)

- [Monte Carlo: integral errors and interval coverage across 256 seeds](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/mc-integral/?lang=en) (`mc-integral`) · [Code ZIP](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/model-benchmarks-2026-11-22.zip)

Integrate x² under U[0,1]. Compare 256 independent seeds with analytic integral and variance, checking N^-1/2 RMS scaling and interval coverage. Excludes MCMC and rare events.

##### [Ordinary importance sampling of a normal rare tail](https://hrkoyama.github.io/numerical-methods-atlas/problems/normal-tail-importance/?lang=en) (`normal-tail-importance`)

![Distribution and error diagnostics from actual saved data;sample/time axes are distinguished from spatial dimensions.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/results/normal-tail-importance-preview.png)

Ordinary mean ofY=1(X>a)exp(-aX+a²/2),without random weight normalization or proposal tuning. Retain direct zero-hit counts with Clopper-Pearson intervals.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/normal-tail-importance/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/normal-tail-importance/?lang=en#code-en)

- [Ordinary importance sampling of a normal rare tail](https://hrkoyama.github.io/numerical-methods-atlas/validation/normal-tail-importance/?lang=en) (`normal-tail-importance`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/atlas-stochastic-estimation-2026-11-24.zip)

Check ordinary likelihood-ratio averages with analytic moments,independent batch variance and finite coverage diagnostics.


#### Exact / reference solutions (`method-references-en`)

##### [Monte Carlo: integral errors and interval coverage across 256 seeds](https://hrkoyama.github.io/numerical-methods-atlas/problems/mc-integral/?lang=en#references-en) (`mc-integral`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### [Ordinary importance sampling of a normal rare tail](https://hrkoyama.github.io/numerical-methods-atlas/problems/normal-tail-importance/?lang=en#references-en) (`normal-tail-importance`)

- [Ordinary importance sampling of a normal rare tail](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-normal-tail-importance-en) (`normal-tail-importance`; Same-problem reference; Analytic reference)

Bernoulli exact intervals are not applied to weighted IS.64trials do not prove general95%coverage;nested prefixes are not extra independent replicates. Global weightESS and eventESS are distinct.

[Existing reference profile](/numerical-methods-atlas/validation/normal-tail-importance/?lang=en#normal-tail-importance-en-measurements)

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/monte-carlo/)
- Verification receipt: [Edition verification receipt](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/verification.json)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

##### Monte Carlo: integral errors and interval coverage across 256 seeds (`mc-integral`)

[Monte Carlo: integral errors and interval coverage across 256 seeds](https://hrkoyama.github.io/numerical-methods-atlas/problems/mc-integral/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/mc-integral/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/model-benchmarks-2026-11-22.zip)

[Fixed input](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/inputs/mc-integral.json)

[Verification receipt](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

Integrate x² under U[0,1]. Compare 256 independent seeds with analytic integral and variance, checking N^-1/2 RMS scaling and interval coverage. Excludes MCMC and rare events.

##### Ordinary importance sampling of a normal rare tail (`normal-tail-importance`)

[Ordinary importance sampling of a normal rare tail](https://hrkoyama.github.io/numerical-methods-atlas/problems/normal-tail-importance/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/normal-tail-importance/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/atlas-stochastic-estimation-2026-11-24.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/verification.json)

Check ordinary likelihood-ratio averages with analytic moments,independent batch variance and finite coverage diagnostics.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Additional fixed examples: Ordinary importance sampling of a normal rare tail. See each release for assumptions and checked scope. Bernoulli exact intervals are not applied to weighted IS.64trials do not prove general95%coverage;nested prefixes are not extra independent replicates. Global weightESS and eventESS are distinct.

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[Related code edition / ZIP](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/model-benchmarks-2026-11-22.zip)

[Edition verification receipt](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/verification.json)

###### Related source

- [/code/model-benchmarks/2026-11-22/models.py](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/models.py)
- [/code/model-benchmarks/2026-11-22/run.py](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/run.py)
- [/code/validated-examples/2026-11-24/stochastic-estimation/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/run.py)
- [/code/validated-examples/2026-11-24/stochastic-estimation/importance.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/importance.py)
- [/code/validated-examples/2026-11-24/stochastic-estimation/sampler.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/sampler.py)
- [/code/validated-examples/2026-11-24/stochastic-estimation/diagnostics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/diagnostics.py)
- [/code/validated-examples/2026-11-24/stochastic-estimation/support.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/support.py)
- [/code/validated-examples/2026-11-24/stochastic-estimation/references/generate_arviz.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/references/generate_arviz.py)
- [/code/validated-examples/2026-11-24/stochastic-estimation/references/prepare.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/references/prepare.py)
- [/code/validated-examples/2026-11-24/stochastic-estimation/references/qualify_arviz.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/references/qualify_arviz.py)
- [/code/validated-examples/2026-11-24/stochastic-estimation/references/qualify_is.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/references/qualify_is.py)

###### Package tests

- [/code/model-benchmarks/2026-11-22/test_models.py](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/test_models.py)
- [/code/validated-examples/2026-11-24/stochastic-estimation/test_driver_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/test_driver_contract.py)
- [/code/validated-examples/2026-11-24/stochastic-estimation/test_estimators.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/test_estimators.py)
- [/code/validated-examples/2026-11-24/stochastic-estimation/test_fixture_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/test_fixture_contract.py)
- [/code/validated-examples/2026-11-24/stochastic-estimation/test_tail_quantiles.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/test_tail_quantiles.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python run.py --input inputs/mc-integral.json --output output
```
