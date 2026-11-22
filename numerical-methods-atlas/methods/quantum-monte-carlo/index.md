# Quantum Monte Carlo / 量子Monte Carlo

Status: reading-only

Map stochastic quantum calculations, statistical errors and approximations.

確率的な量子計算と統計誤差・近似を整理する。

Introductory bilingual reading, representative equations and primary references are available. No dedicated implementation or numerical verification result is provided yet. Statistical error bars do not capture fixed-node, time-step or finite-size bias. Quantum Monte Carlo here does not mean computation on a quantum computer.

Other names: VMC, DMC, fixed node, 量子モンテカルロ

Comparison notes: Statistical error bars do not capture fixed-node, time-step or finite-size bias. Quantum Monte Carlo here does not mean computation on a quantum computer.

統計誤差の棒だけでは固定節・時間刻み・有限サイズ等の系統誤差を表せません。量子コンピュータを使う計算という意味でもありません。

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/quantum-chemistry/#quantum-monte-carlo
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/quantum-chemistry/#quantum-monte-carlo



- Reference: https://doi.org/10.1103/PhysRevLett.45.566 — Primary publication entry point for the quantum-chemistry overview. Bibliographic/introductory review only; full-paper equations and numerical results have not been reproduced.

Next: Maintain the reading, primary sources and links to existing small examples. Consider a dedicated implementation only when needed, starting with a small educational case; routine work excludes heavy convergence sweeps, reference regeneration and long MD.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/quantum-monte-carlo/
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

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/quantum-chemistry/#quantum-monte-carlo)


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

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/quantum-chemistry/#quantum-monte-carlo)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

No fixed-input execution example is linked between this method and a problem figure.

No related source, tests or code-edition links are registered for this method.
