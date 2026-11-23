# Volume-of-fluid / VOF / VOF法／体積率による界面捕獲

Status: reading-only

Represent an interface through cell fluid-volume fractions. Compare conservation, geometric representation and curvature evaluation with level sets. No dedicated VOF implementation or numerical comparison is included.

セル内の流体体積率で界面を表す方法。レベルセット法との保存性・幾何表現・曲率評価の違いを比較解説する。VOF専用コードと数値比較は未収録。

VOF/CLSVOF comparisons describe formulations and conditions. No VOF implementation, performance ranking, curvature-flow, two-phase-flow or topology-change validation is claimed.

Other names: VOF, volume of fluid, volume-of-fluid method, 体積流体法, 体積率法, VOF法

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/level-set/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/level-set/



- Reference: https://doi.org/10.1016/0021-9991(88)90002-2 — Selected author-hosted original passages: abstract, implicit front representation and Hamilton–Jacobi transport/normal-motion formulation. No full-paper audit or reproduction of its full experiment suite.
- Reference: https://doi.org/10.1016/0021-9991(81)90145-5 — Publisher bibliography and abstract for the original volume-fraction formulation. No full-text algorithm audit or implementation of its donor–acceptor scheme.
- Reference: https://doi.org/10.1137/S1064827596298245 — Official abstract and bibliography: redistancing quality includes retaining the zero interface; its constrained higher-order algorithm is not the simple Godunov auxiliary iteration implemented here.
- Reference: https://doi.org/10.1006/jcph.2000.6537 — Author-hosted pp.302–305, equations(1)–(6),(9),(12),(15): signed-distance geometry, enclosed-mass issue and volume-fraction conservation. Sign is reversed here to make phi negative inside. No CLSVOF or two-phase fluid experiment executed.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/vof/
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

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/level-set/)


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

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/level-set/)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

No fixed-input execution example is linked between this method and a problem figure.

No related source, tests or code-edition links are registered for this method.
