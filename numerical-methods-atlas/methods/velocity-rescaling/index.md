# Direct velocity rescaling / 単純な速度スケーリング

Status: planned

Multiply velocities by a common factor to set the kinetic energy at each application. Simple deterministic rescaling does not reproduce canonical kinetic-energy fluctuations.

全粒子の速度に共通係数を掛け、適用時の運動エネルギーを目標値に合わせる。単純な決定論的操作では正準分布の運動エネルギー揺らぎを再現しない。

Comparative reading is available. No dedicated implementation or numerical verification result is provided yet.

Other names: ベロシティースケーリング, ベロシティスケーリング, velocity scaling, simple velocity rescaling

Comparison notes: A comparison case for distinguishing temperature control from canonical sampling. Ratio-based rescaling is undefined at T=0; the application interval also matters.

温度への到達と正準分布の標本化を区別するための比較対象。T=0では比による再スケーリングを定義できず、適用間隔も結果に影響する。

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/thermostats/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/thermostats/



- Reference: https://manual.gromacs.org/current/reference-manual/algorithms/molecular-dynamics.html — Bibliographic entry and introductory comparison; full derivation and numerical reproduction have not been audited.

Next: Add a dedicated formulation and integration recipe, followed by explicit-input distribution and time-correlation checks with stated degrees of freedom, random seeds and step sizes.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/velocity-rescaling/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

対応する方程式一覧の項目は未登録です。

#### 問題の図 (`method-problems-ja`)

この手法に対応付けられたテスト問題の図は未登録です。

#### 厳密解・参照解 (`method-references-ja`)

この手法の問題図に結び付く参照資料は未登録です。
##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/thermostats/)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

この手法と問題図を対応付けた固定入力実行例は未登録です。

この手法に対応するソース・検査・配布版のリンクは未登録です。


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

No corresponding equation-registry entry is registered.

#### Problem figures (`method-problems-en`)

No test-problem figure is registered for this method.

#### Exact / reference solutions (`method-references-en`)

No reference context is registered for this method’s problem figures.
##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/thermostats/)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

No fixed-input execution example is linked between this method and a problem figure.

No related source, tests or code-edition links are registered for this method.
