# Stochastic differential equations / 確率微分方程式

Status: educational-example

Distinguish stochastic-integration conventions and strong/weak errors. Additional fixed examples: GBM weak bias and Monte Carlo error, OU weak moments with joint Brownian coupling, Milstein and EM on identical Brownian paths. See each release for assumptions and checked scope.

確率積分の規約と強・弱誤差を区別する。 追加固定例：GBMのweak誤差とMonte Carlo標準誤差、OUのweakモーメントと同時Brownian結合、同じBrownian経路のMilstein・EM strong比較。条件と検証範囲は各配布版で確認してください。

Euler–Maruyama for scalar geometric Brownian motion. Coarse/fine steps and analytic endpoints share the same Brownian paths; measure strong RMS error across 4096 paths. Does not validate general SDEs, MCMC or weak convergence order. Additional fixed examples: Weak error is a difference of expectations. SE/intervals are not true-error bounds or general coverage guarantees. State×time examples are not2Dphysical flow. Existing GBM/OUbath physical families are reused. Weak error is a difference of expectations. SE/intervals are not true-error bounds or general coverage guarantees. State×time examples are not2Dphysical flow. Existing GBM/OUbath physical families are reused. EndpointL2error is distinct from the selected paper L1definition. No general non-Lipschitz/positivity guarantee. This extends existinggbm-sde rather than adding a physical problem.

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

## Small fixed-input validation supplements

Additional fixed examples: GBM weak bias and Monte Carlo error, OU weak moments with joint Brownian coupling, Milstein and EM on identical Brownian paths. See each release for assumptions and checked scope. Weak error is a difference of expectations. SE/intervals are not true-error bounds or general coverage guarantees. State×time examples are not2Dphysical flow. Existing GBM/OUbath physical families are reused. Weak error is a difference of expectations. SE/intervals are not true-error bounds or general coverage guarantees. State×time examples are not2Dphysical flow. Existing GBM/OUbath physical families are reused. EndpointL2error is distinct from the selected paper L1definition. No general non-Lipschitz/positivity guarantee. This extends existinggbm-sde rather than adding a physical problem.

追加固定例：GBMのweak誤差とMonte Carlo標準誤差、OUのweakモーメントと同時Brownian結合、同じBrownian経路のMilstein・EM strong比較。条件と検証範囲は各配布版で確認してください。 弱誤差は期待値の差です。3SEや区間を真の誤差上界・一般被覆保証としません。1D状態×時間の保存例であり2D物理流れではありません。GBMやOU浴成分を新しい物理問題として重複計数しません。 弱誤差は期待値の差です。3SEや区間を真の誤差上界・一般被覆保証としません。1D状態×時間の保存例であり2D物理流れではありません。GBMやOU浴成分を新しい物理問題として重複計数しません。 L2終端誤差を扱い、原著のL1定義と区別。GBM以外の非Lipschitz系・正値性の一般保証はしません。既存gbm-sdeへの手法追加です。

- GBM weak bias and Monte Carlo error: https://hrkoyama.github.io/numerical-methods-atlas/validation/gbm-weak-moments/
- OU weak moments with joint Brownian coupling: https://hrkoyama.github.io/numerical-methods-atlas/validation/ou-weak-moments/
- Milstein and EM on identical Brownian paths: https://hrkoyama.github.io/numerical-methods-atlas/validation/gbm-milstein-strong/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/atlas-stochastic-accuracy-2026-11-24.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/results/result.json

Common execution records: [{"id": "gbm-sde", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=ja#gbm-sde-ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=en#gbm-sde-en"}}, {"id": "gbm-weak-moments", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/gbm-weak-moments/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/gbm-weak-moments/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "ou-weak-moments", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/ou-weak-moments/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/ou-weak-moments/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "gbm-milstein-strong", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/gbm-milstein-strong/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/gbm-milstein-strong/?lang=en"}, "kind": "dedicated-supplement"}]

Next: Add validation against another reference problem before extending application scope.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/sde/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [スカラーItô拡散：GBMとOU](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#scalar-ito-diffusion-ja) (`scalar-ito-diffusion`; gbm-sde, langevin-harmonic)
- [Hamilton系・振動子](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#hamiltonian-ja) (`hamiltonian`; langevin-harmonic)

#### 問題の図 (`method-problems-ja`)

##### [Itô SDE：共有Brown運動による強収束](https://hrkoyama.github.io/numerical-methods-atlas/problems/gbm-sde/?lang=ja) (`gbm-sde`)

![公開した固定入力と同じ計算結果。解・解析参照または独立参照・誤差を図示。数値条件とCSVを実行ページに保存。](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/results/gbm-sde/preview.png)

この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/gbm-sde/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/gbm-sde/?lang=ja#code-ja)

- [Itô SDE：共有Brown運動による強収束](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/gbm-sde/?lang=ja) (`gbm-sde`) · [コードZIP](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/model-benchmarks-2026-11-22.zip)

スカラー幾何Brown運動のEuler–Maruyama。粗細刻みと解析解で同じBrown運動を共有し、4096経路で強RMS誤差を測定。一般SDE・MCMC・弱収束次数は検証しない。

- [GBMのweak誤差とMonte Carlo標準誤差](https://hrkoyama.github.io/numerical-methods-atlas/validation/gbm-weak-moments/?lang=ja) (`gbm-weak-moments`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/atlas-stochastic-accuracy-2026-11-24.zip)

連続真値、離散EM期待値、同一経路差とMCSEを分離する固定入力です。

- [同じBrownian経路のMilstein・EM strong比較](https://hrkoyama.github.io/numerical-methods-atlas/validation/gbm-milstein-strong/?lang=ja) (`gbm-milstein-strong`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/atlas-stochastic-accuracy-2026-11-24.zip)

補償項を持つMilsteinとEMの終端L2 RMSを、厳密端点と有限モーメントから検査。

##### [Langevin温度制御：正準分布・刻み偏り・時間相関](https://hrkoyama.github.io/numerical-methods-atlas/problems/langevin-harmonic/?lang=ja) (`langevin-harmonic`)

![調和振動子BAOABの刻み0.4/0.2/0.1。離散定常共分散の偏り、有限標本誤差、正準CDF誤差とlag2の位置相関を保存値から分離表示。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/langevin-harmonic.png)

この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/langevin-harmonic/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/langevin-harmonic/?lang=ja#code-ja)

- [OUのweakモーメントと同時Brownian結合](https://hrkoyama.github.io/numerical-methods-atlas/validation/ou-weak-moments/?lang=ja) (`ou-weak-moments`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/atlas-stochastic-accuracy-2026-11-24.zip)

連続真値、離散EM期待値、同一経路差とMCSEを分離する固定入力です。


#### 厳密解・参照解 (`method-references-ja`)

##### [Itô SDE：共有Brown運動による強収束](https://hrkoyama.github.io/numerical-methods-atlas/problems/gbm-sde/?lang=ja#references-ja) (`gbm-sde`)

- [GBMのweak誤差とMonte Carlo標準誤差](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-gbm-weak-moments-ja) (`gbm-weak-moments`; 関連モデルの参照; 解析参照)

dX=.5Xdt+.4XdW,X0=1。無次元T=1、8/16/32/64刻み、独立32seed×1024経路。状態軸に境界・clipなし。

[既存の参照図](/numerical-methods-atlas/validation/gbm-weak-moments/?lang=ja#gbm-weak-moments-ja-measurements)

- [同じBrownian経路のMilstein・EM strong比較](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-gbm-milstein-strong-ja) (`gbm-milstein-strong`; 関連モデルの参照; 解析参照)

既存GBMと同じμ=.15,σ=.4,X0=T=1。4seed×8192経路、16/32/64/128刻み。

[既存の参照図](/numerical-methods-atlas/validation/gbm-milstein-strong/?lang=ja#gbm-milstein-strong-ja-measurements)

##### [Langevin温度制御：正準分布・刻み偏り・時間相関](https://hrkoyama.github.io/numerical-methods-atlas/problems/langevin-harmonic/?lang=ja#references-ja) (`langevin-harmonic`)

- [OUのweakモーメントと同時Brownian結合](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-ou-weak-moments-ja) (`ou-weak-moments`; 関連モデルの参照; 解析参照)

dX=1.5(.2-X)dt+.8dW,X0=.7。無次元T=1、8/16/32/64刻み、独立32seed×1024経路。状態軸に境界・clipなし。

[既存の参照図](/numerical-methods-atlas/validation/ou-weak-moments/?lang=ja#ou-weak-moments-ja-measurements)

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

##### GBMのweak誤差とMonte Carlo標準誤差 (`gbm-weak-moments`)

[Itô SDE：共有Brown運動による強収束](https://hrkoyama.github.io/numerical-methods-atlas/problems/gbm-sde/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/gbm-weak-moments/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/atlas-stochastic-accuracy-2026-11-24.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/verification.json)

連続真値、離散EM期待値、同一経路差とMCSEを分離する固定入力です。

##### 同じBrownian経路のMilstein・EM strong比較 (`gbm-milstein-strong`)

[Itô SDE：共有Brown運動による強収束](https://hrkoyama.github.io/numerical-methods-atlas/problems/gbm-sde/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/gbm-milstein-strong/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/atlas-stochastic-accuracy-2026-11-24.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/verification.json)

補償項を持つMilsteinとEMの終端L2 RMSを、厳密端点と有限モーメントから検査。

##### OUのweakモーメントと同時Brownian結合 (`ou-weak-moments`)

[Langevin温度制御：正準分布・刻み偏り・時間相関](https://hrkoyama.github.io/numerical-methods-atlas/problems/langevin-harmonic/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/ou-weak-moments/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/atlas-stochastic-accuracy-2026-11-24.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/verification.json)

連続真値、離散EM期待値、同一経路差とMCSEを分離する固定入力です。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

追加固定例：GBMのweak誤差とMonte Carlo標準誤差、OUのweakモーメントと同時Brownian結合、同じBrownian経路のMilstein・EM strong比較。条件と検証範囲は各配布版で確認してください。 弱誤差は期待値の差です。3SEや区間を真の誤差上界・一般被覆保証としません。1D状態×時間の保存例であり2D物理流れではありません。GBMやOU浴成分を新しい物理問題として重複計数しません。 弱誤差は期待値の差です。3SEや区間を真の誤差上界・一般被覆保証としません。1D状態×時間の保存例であり2D物理流れではありません。GBMやOU浴成分を新しい物理問題として重複計数しません。 L2終端誤差を扱い、原著のL1定義と区別。GBM以外の非Lipschitz系・正値性の一般保証はしません。既存gbm-sdeへの手法追加です。

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/model-benchmarks-2026-11-22.zip)

[配布版の検証記録](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/verification.json)

###### 関連ソース

- [/code/model-benchmarks/2026-11-22/models.py](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/models.py)
- [/code/model-benchmarks/2026-11-22/run.py](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/run.py)
- [/code/validated-examples/2026-11-24/stochastic-accuracy/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/run.py)
- [/code/validated-examples/2026-11-24/stochastic-accuracy/paths.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/paths.py)
- [/code/validated-examples/2026-11-24/stochastic-accuracy/references/analytic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/references/analytic.py)
- [/code/validated-examples/2026-11-24/stochastic-accuracy/support.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/support.py)
- [/code/validated-examples/2026-11-24/stochastic-accuracy/references/qualify.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/references/qualify.py)

###### 配布版のテスト

- [/code/model-benchmarks/2026-11-22/test_models.py](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/test_models.py)
- [/code/validated-examples/2026-11-24/stochastic-accuracy/test_driver_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/test_driver_contract.py)
- [/code/validated-examples/2026-11-24/stochastic-accuracy/test_paths.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/test_paths.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python run.py --input inputs/gbm-sde.json --output output
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Scalar Ito diffusion: GBM and OU](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#scalar-ito-diffusion-en) (`scalar-ito-diffusion`; gbm-sde, langevin-harmonic)
- [Hamiltonian systems and oscillators](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#hamiltonian-en) (`hamiltonian`; langevin-harmonic)

#### Problem figures (`method-problems-en`)

##### [Itô SDE: strong convergence with coupled Brownian paths](https://hrkoyama.github.io/numerical-methods-atlas/problems/gbm-sde/?lang=en) (`gbm-sde`)

![The same public fixed-input calculation. Shows solutions, analytic/independent references or errors; numerical criteria and CSV are linked in the execution entry.](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/results/gbm-sde/preview.png)

Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/gbm-sde/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/gbm-sde/?lang=en#code-en)

- [Itô SDE: strong convergence with coupled Brownian paths](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/gbm-sde/?lang=en) (`gbm-sde`) · [Code ZIP](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/model-benchmarks-2026-11-22.zip)

Euler–Maruyama for scalar geometric Brownian motion. Coarse/fine steps and analytic endpoints share the same Brownian paths; measure strong RMS error across 4096 paths. Does not validate general SDEs, MCMC or weak convergence order.

- [GBM weak bias and Monte Carlo error](https://hrkoyama.github.io/numerical-methods-atlas/validation/gbm-weak-moments/?lang=en) (`gbm-weak-moments`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/atlas-stochastic-accuracy-2026-11-24.zip)

Separate continuous truth,exact discrete EM expectation,paired-path weak difference and MCSE.

- [Milstein and EM on identical Brownian paths](https://hrkoyama.github.io/numerical-methods-atlas/validation/gbm-milstein-strong/?lang=en) (`gbm-milstein-strong`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/atlas-stochastic-accuracy-2026-11-24.zip)

Compare compensated Milstein and EM endpoint L2RMS against exact endpoints and finite-moment identities.

##### [Langevin thermostat: canonical distributions, timestep bias and correlation](https://hrkoyama.github.io/numerical-methods-atlas/problems/langevin-harmonic/?lang=en) (`langevin-harmonic`)

![Stored harmonic-BAOAB steps 0.4/0.2/0.1 separate discrete stationary-covariance bias, sampling error, canonical-CDF errors and position correlation at lag 2.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/langevin-harmonic.png)

Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/langevin-harmonic/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/langevin-harmonic/?lang=en#code-en)

- [OU weak moments with joint Brownian coupling](https://hrkoyama.github.io/numerical-methods-atlas/validation/ou-weak-moments/?lang=en) (`ou-weak-moments`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/atlas-stochastic-accuracy-2026-11-24.zip)

Separate continuous truth,exact discrete EM expectation,paired-path weak difference and MCSE.


#### Exact / reference solutions (`method-references-en`)

##### [Itô SDE: strong convergence with coupled Brownian paths](https://hrkoyama.github.io/numerical-methods-atlas/problems/gbm-sde/?lang=en#references-en) (`gbm-sde`)

- [GBM weak bias and Monte Carlo error](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-gbm-weak-moments-en) (`gbm-weak-moments`; Related-model reference; Analytic reference)

dX=.5Xdt+.4XdW,X0=1;dimensionlessT1;8/16/32/64steps;32independent seeds×1024paths. Unbounded state,no clipping.

[Existing reference profile](/numerical-methods-atlas/validation/gbm-weak-moments/?lang=en#gbm-weak-moments-en-measurements)

- [Milstein and EM on identical Brownian paths](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-gbm-milstein-strong-en) (`gbm-milstein-strong`; Related-model reference; Analytic reference)

ExistingGBMparametersmu.15,sigma.4,X0=T1;4seeds×8192paths;16/32/64/128steps.

[Existing reference profile](/numerical-methods-atlas/validation/gbm-milstein-strong/?lang=en#gbm-milstein-strong-en-measurements)

##### [Langevin thermostat: canonical distributions, timestep bias and correlation](https://hrkoyama.github.io/numerical-methods-atlas/problems/langevin-harmonic/?lang=en#references-en) (`langevin-harmonic`)

- [OU weak moments with joint Brownian coupling](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-ou-weak-moments-en) (`ou-weak-moments`; Related-model reference; Analytic reference)

dX=1.5(.2-X)dt+.8dW,X0=.7;dimensionlessT1;8/16/32/64steps;32independent seeds×1024paths. Unbounded state,no clipping.

[Existing reference profile](/numerical-methods-atlas/validation/ou-weak-moments/?lang=en#ou-weak-moments-en-measurements)

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

##### GBM weak bias and Monte Carlo error (`gbm-weak-moments`)

[Itô SDE: strong convergence with coupled Brownian paths](https://hrkoyama.github.io/numerical-methods-atlas/problems/gbm-sde/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/gbm-weak-moments/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/atlas-stochastic-accuracy-2026-11-24.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/verification.json)

Separate continuous truth,exact discrete EM expectation,paired-path weak difference and MCSE.

##### Milstein and EM on identical Brownian paths (`gbm-milstein-strong`)

[Itô SDE: strong convergence with coupled Brownian paths](https://hrkoyama.github.io/numerical-methods-atlas/problems/gbm-sde/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/gbm-milstein-strong/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/atlas-stochastic-accuracy-2026-11-24.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/verification.json)

Compare compensated Milstein and EM endpoint L2RMS against exact endpoints and finite-moment identities.

##### OU weak moments with joint Brownian coupling (`ou-weak-moments`)

[Langevin thermostat: canonical distributions, timestep bias and correlation](https://hrkoyama.github.io/numerical-methods-atlas/problems/langevin-harmonic/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/ou-weak-moments/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/atlas-stochastic-accuracy-2026-11-24.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/verification.json)

Separate continuous truth,exact discrete EM expectation,paired-path weak difference and MCSE.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Additional fixed examples: GBM weak bias and Monte Carlo error, OU weak moments with joint Brownian coupling, Milstein and EM on identical Brownian paths. See each release for assumptions and checked scope. Weak error is a difference of expectations. SE/intervals are not true-error bounds or general coverage guarantees. State×time examples are not2Dphysical flow. Existing GBM/OUbath physical families are reused. Weak error is a difference of expectations. SE/intervals are not true-error bounds or general coverage guarantees. State×time examples are not2Dphysical flow. Existing GBM/OUbath physical families are reused. EndpointL2error is distinct from the selected paper L1definition. No general non-Lipschitz/positivity guarantee. This extends existinggbm-sde rather than adding a physical problem.

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[Related code edition / ZIP](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/model-benchmarks-2026-11-22.zip)

[Edition verification receipt](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/verification.json)

###### Related source

- [/code/model-benchmarks/2026-11-22/models.py](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/models.py)
- [/code/model-benchmarks/2026-11-22/run.py](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/run.py)
- [/code/validated-examples/2026-11-24/stochastic-accuracy/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/run.py)
- [/code/validated-examples/2026-11-24/stochastic-accuracy/paths.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/paths.py)
- [/code/validated-examples/2026-11-24/stochastic-accuracy/references/analytic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/references/analytic.py)
- [/code/validated-examples/2026-11-24/stochastic-accuracy/support.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/support.py)
- [/code/validated-examples/2026-11-24/stochastic-accuracy/references/qualify.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/references/qualify.py)

###### Package tests

- [/code/model-benchmarks/2026-11-22/test_models.py](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/test_models.py)
- [/code/validated-examples/2026-11-24/stochastic-accuracy/test_driver_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/test_driver_contract.py)
- [/code/validated-examples/2026-11-24/stochastic-accuracy/test_paths.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/test_paths.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python run.py --input inputs/gbm-sde.json --output output
```
