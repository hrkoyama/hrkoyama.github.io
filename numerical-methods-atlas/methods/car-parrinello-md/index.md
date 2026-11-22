# Car–Parrinello molecular dynamics / CPMD / カー–パリネロ法（CPMD）

Status: reading-only

Assign fictitious inertia to orbitals and propagate an orthonormality-constrained extended system with the nuclei.

電子軌道に仮想質量を与え、直交制約付きの拡張系で核と同時に進める。

Reading only. Adiabatic separation, fictitious-to-nuclear energy transfer and long trajectories are unvalidated.

Other names: CPMD, Car Parrinello, Car–Parrinello, Car Parrinello MD, カー・パリネロ法, カーパリネロ法, 第一原理分子動力学

Comparison notes: Reading only. Adiabatic separation, fictitious-to-nuclear energy transfer and long trajectories are unvalidated.

解説のみ。仮想電子運動の断熱性、エネルギー移動、長時間軌道は未検証です。

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/periodic-dft/#first-principles-md
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/periodic-dft/#first-principles-md



- Reference: https://doi.org/10.1103/PhysRevLett.55.2471 — Publisher bibliography/abstract and original equations (3)–(5) and discussion of fictitious electronic motion near the BO surface consulted. The paper’s silicon dynamics have not been numerically reproduced.

Next: Maintain the reading, primary sources and links to existing small examples. Consider a dedicated implementation only when needed, starting with a small educational case; routine work excludes heavy convergence sweeps, reference regeneration and long MD.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/car-parrinello-md/
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

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/periodic-dft/#first-principles-md)


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

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/periodic-dft/#first-principles-md)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

No fixed-input execution example is linked between this method and a problem figure.

No related source, tests or code-edition links are registered for this method.
