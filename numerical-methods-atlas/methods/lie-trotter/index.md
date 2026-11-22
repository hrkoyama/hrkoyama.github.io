# Lie–Trotter splitting / Lie–Trotter分割

Status: reading-only

First-order integration by composing two full subflows. Compare formulas, commutators, local/global errors and a small noncommuting example with Strang splitting.

右辺を2つの部分流に分け、全刻みずつ順に合成する1次の時間積分法。Strangとの公式・交換子・局所と大域の誤差・非可換な小例を比較する。

The smooth finite-dimensional illustration does not validate shocks, stiff PDEs or general boundaries. Exact subflows do not remove composition stability restrictions. The illustration script is not a general solver release.

Other names: Lie-Trotter splitting, Lie Trotter splitting, Lie splitting, Trotter splitting, Lie–Trotter分割法, リー・トロッター分割, リートロッター分割, リー・トロッタ分割, 1次作用素分割

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/operator-splitting/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/operator-splitting/



- Reference: https://doi.org/10.1090/S0002-9939-1959-0108732-6 — AMS bibliographic record checked. Original semigroup product-limit reference; no audit of unbounded-operator hypotheses. Finite-dimensional order calculations are derived in the chapter.
- Reference: https://www.unige.ch/~hairer/poly_geoint/week2.pdf — Author-hosted Lecture 2, section 5, printed pp.12–14, equations (23)–(27), and exact versus numerical subflows: Lie–Trotter, symmetric second-order composition and separable Hamiltonians. Selected passages, not a full-lecture audit.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/lie-trotter/
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

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/operator-splitting/)


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

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/operator-splitting/)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

No fixed-input execution example is linked between this method and a problem figure.

No related source, tests or code-edition links are registered for this method.
