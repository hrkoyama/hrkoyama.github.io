# Stochastic differential equations / 確率微分方程式

Status: educational-example

Distinguish stochastic-integration conventions and strong/weak errors.

確率積分の規約と強・弱誤差を区別する。

Euler–Maruyama for scalar geometric Brownian motion. Coarse/fine steps and analytic endpoints share the same Brownian paths; measure strong RMS error across 4096 paths. Does not validate general SDEs, MCMC or weak convergence order.

Other names: SDE, SDE法, stochastic differential equation, 確率微分方程式法

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/sde/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/sde/



- Reference: https://doi.org/10.1007/bf02846028 — Method-specific source; see the detailed reading for source role and actual review depth.
- Reference: https://doi.org/10.1137/s0036144500378302 — Method-specific source; see the detailed reading for source role and actual review depth.

Scoped example: Euler–Maruyama for scalar geometric Brownian motion. Coarse/fine steps and analytic endpoints share the same Brownian paths; measure strong RMS error across 4096 paths. Does not validate general SDEs, MCMC or weak convergence order.

Code: https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/models.py
Tests: https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/test_models.py
Download: https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/model-benchmarks-2026-11-22.zip
Verification: https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/verification.json

Common execution records: [{"id": "gbm-sde", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=ja#gbm-sde-ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=en#gbm-sde-en"}}]

Next: Add validation against another reference problem before extending application scope.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/sde/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

対応する方程式一覧の項目は未登録です。

#### 問題の図 (`method-problems-ja`)

##### [Itô SDE：共有Brown運動による強収束](https://hrkoyama.github.io/numerical-methods-atlas/problems/gbm-sde/?lang=ja) (`gbm-sde`)

![公開した固定入力と同じ計算結果。解・解析参照または独立参照・誤差を図示。数値条件とCSVを実行ページに保存。](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/results/gbm-sde/preview.png)

この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/gbm-sde/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/gbm-sde/?lang=ja#code-ja)

- [Itô SDE：共有Brown運動による強収束](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/gbm-sde/?lang=ja) (`gbm-sde`) · [コードZIP](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/model-benchmarks-2026-11-22.zip)

スカラー幾何Brown運動のEuler–Maruyama。粗細刻みと解析解で同じBrown運動を共有し、4096経路で強RMS誤差を測定。一般SDE・MCMC・弱収束次数は検証しない。


#### 厳密解・参照解 (`method-references-ja`)

##### [Itô SDE：共有Brown運動による強収束](https://hrkoyama.github.io/numerical-methods-atlas/problems/gbm-sde/?lang=ja#references-ja) (`gbm-sde`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/sde/)
- 検証記録: [配布版の検証記録](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/verification.json)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

##### Itô SDE：共有Brown運動による強収束 (`gbm-sde`)

[Itô SDE：共有Brown運動による強収束](https://hrkoyama.github.io/numerical-methods-atlas/problems/gbm-sde/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/gbm-sde/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/model-benchmarks-2026-11-22.zip)

[固定入力](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/inputs/gbm-sde.json)

[検証記録](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

スカラー幾何Brown運動のEuler–Maruyama。粗細刻みと解析解で同じBrown運動を共有し、4096経路で強RMS誤差を測定。一般SDE・MCMC・弱収束次数は検証しない。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/model-benchmarks-2026-11-22.zip)

[配布版の検証記録](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/verification.json)

###### 関連ソース

- [/code/model-benchmarks/2026-11-22/models.py](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/models.py)
- [/code/model-benchmarks/2026-11-22/run.py](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/run.py)

###### 配布版のテスト

- [/code/model-benchmarks/2026-11-22/test_models.py](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/test_models.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python run.py --input inputs/gbm-sde.json --output output
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

No corresponding equation-registry entry is registered.

#### Problem figures (`method-problems-en`)

##### [Itô SDE: strong convergence with coupled Brownian paths](https://hrkoyama.github.io/numerical-methods-atlas/problems/gbm-sde/?lang=en) (`gbm-sde`)

![The same public fixed-input calculation. Shows solutions, analytic/independent references or errors; numerical criteria and CSV are linked in the execution entry.](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/results/gbm-sde/preview.png)

Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/gbm-sde/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/gbm-sde/?lang=en#code-en)

- [Itô SDE: strong convergence with coupled Brownian paths](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/gbm-sde/?lang=en) (`gbm-sde`) · [Code ZIP](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/model-benchmarks-2026-11-22.zip)

Euler–Maruyama for scalar geometric Brownian motion. Coarse/fine steps and analytic endpoints share the same Brownian paths; measure strong RMS error across 4096 paths. Does not validate general SDEs, MCMC or weak convergence order.


#### Exact / reference solutions (`method-references-en`)

##### [Itô SDE: strong convergence with coupled Brownian paths](https://hrkoyama.github.io/numerical-methods-atlas/problems/gbm-sde/?lang=en#references-en) (`gbm-sde`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/sde/)
- Verification receipt: [Edition verification receipt](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/verification.json)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

##### Itô SDE: strong convergence with coupled Brownian paths (`gbm-sde`)

[Itô SDE: strong convergence with coupled Brownian paths](https://hrkoyama.github.io/numerical-methods-atlas/problems/gbm-sde/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/gbm-sde/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/model-benchmarks-2026-11-22.zip)

[Fixed input](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/inputs/gbm-sde.json)

[Verification receipt](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

Euler–Maruyama for scalar geometric Brownian motion. Coarse/fine steps and analytic endpoints share the same Brownian paths; measure strong RMS error across 4096 paths. Does not validate general SDEs, MCMC or weak convergence order.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

[Related code edition / ZIP](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/model-benchmarks-2026-11-22.zip)

[Edition verification receipt](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/verification.json)

###### Related source

- [/code/model-benchmarks/2026-11-22/models.py](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/models.py)
- [/code/model-benchmarks/2026-11-22/run.py](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/run.py)

###### Package tests

- [/code/model-benchmarks/2026-11-22/test_models.py](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/test_models.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python run.py --input inputs/gbm-sde.json --output output
```
