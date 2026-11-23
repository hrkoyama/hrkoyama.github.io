# ALE uniform-state / geometric-conservation model / ALE一様状態・幾何保存モデル

Status: educational-example

Read about ALE uniform-state / geometric-conservation model, follow the original references and inspect related educational code and checks.

「ALE一様状態・幾何保存モデル」の考え方と適用範囲を、解説章・一次文献・関連する教育用コードからたどります。

See the chapter and implementation for equations, boundaries and checked scope. Educational examples are not complete general-purpose solvers.

Other names: ALE法, 任意ラグランジュ・オイラー法, 任意ラグランジュオイラー法, Arbitrary Lagrangian Eulerian, arbitrary Lagrangian Eulerian method

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/ale/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/ale/

- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/geometry.py

- Reference: https://doi.org/10.1016/0021-9991(74)90051-5 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.

## Small fixed-input validation supplements

Additional nonuniform1D prescribed moving-grid scalar advances face positions and masses with shared Heun stages. Check actual relative upwind flux,GCL,analytic moving-cell integrals and temporal error.

追加は非一様な1D指定移動格子上のスカラー輸送。面位置とセル質量を同じHeun段で更新し、実際の相対上流流束、GCL、解析的移動セル積分と時間誤差を検査します。

- ALE scalar transport on genuinely nonuniform moving cells: https://hrkoyama.github.io/numerical-methods-atlas/validation/ale-nonuniform-transport/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/atlas-moving-waves-2026-11-23.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/results/result.json

Common execution records: [{"id": "ale-nonuniform-transport", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/ale-nonuniform-transport/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/ale-nonuniform-transport/?lang=en"}, "kind": "dedicated-supplement"}]

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/ale/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [移動セル上のALEスカラー保存式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#ale-scalar-transport-ja) (`ale-scalar-transport`; ale-nonuniform-transport)

#### 問題の図 (`method-problems-ja`)

##### [非一様移動格子で実際に運ぶALEスカラー](https://hrkoyama.github.io/numerical-methods-atlas/problems/ale-nonuniform-transport/?lang=ja) (`ale-nonuniform-transport`)

![実際に保存した計算配列と固定入力の収束指標から描いた検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/results/ale-nonuniform-transport-preview.png)

実セル質量の上流相対流束(a−w)qと実面位置を同じHeun predictor/correctorで進め、各段体積・面Courant数を記録。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/ale-nonuniform-transport/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/ale-nonuniform-transport/?lang=ja#code-ja)

- [非一様移動格子で実際に運ぶALEスカラー](https://hrkoyama.github.io/numerical-methods-atlas/validation/ale-nonuniform-transport/?lang=ja) (`ale-nonuniform-transport`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/atlas-moving-waves-2026-11-23.zip)

質量と格子面位置を同じHeun段で更新し、一様GCLだけでなく非一様な解析波を運びます。


#### 厳密解・参照解 (`method-references-ja`)

##### [非一様移動格子で実際に運ぶALEスカラー](https://hrkoyama.github.io/numerical-methods-atlas/problems/ale-nonuniform-transport/?lang=ja#references-ja) (`ale-nonuniform-transport`)

- [ALE：実際の移動セル上の解析積分と時間参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-ale-nonuniform-transport-ja) (`ale-nonuniform-transport`; 同じ問題の参照; 解析参照)

1D指定格子運動の第一段階です。図のx–tは2D物理計算ではなく、Euler Lagrange/remapやSaltzmanピストンは未実装の後続課題。

[既存の参照図](/numerical-methods-atlas/validation/ale-nonuniform-transport/?lang=ja#ale-nonuniform-transport-ja-measurements)

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/ale/)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

##### 非一様移動格子で実際に運ぶALEスカラー (`ale-nonuniform-transport`)

[非一様移動格子で実際に運ぶALEスカラー](https://hrkoyama.github.io/numerical-methods-atlas/problems/ale-nonuniform-transport/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/ale-nonuniform-transport/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/atlas-moving-waves-2026-11-23.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/verification.json)

質量と格子面位置を同じHeun段で更新し、一様GCLだけでなく非一様な解析波を運びます。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

追加は非一様な1D指定移動格子上のスカラー輸送。面位置とセル質量を同じHeun段で更新し、実際の相対上流流束、GCL、解析的移動セル積分と時間誤差を検査します。

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### 関連ソース

- [/code/numerical-methods-atlas/2026-11-21/numart/geometry.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/geometry.py)
- [/code/validated-examples/2026-11-23/moving-waves/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/run.py)
- [/code/validated-examples/2026-11-23/moving-waves/transport.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/transport.py)
- [/code/validated-examples/2026-11-23/moving-waves/references/exact.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/references/exact.py)
- [/code/validated-examples/2026-11-23/moving-waves/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/experiments.py)

###### 配布版のテスト

- [/code/numerical-methods-atlas/2026-11-21/tests/test_time_geometry.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_time_geometry.py)
- [/code/validated-examples/2026-11-23/moving-waves/test_moving.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/test_moving.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q tests/test_time_geometry.py
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [ALE scalar conservation on moving cells](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#ale-scalar-transport-en) (`ale-scalar-transport`; ale-nonuniform-transport)

#### Problem figures (`method-problems-en`)

##### [ALE scalar transport on genuinely nonuniform moving cells](https://hrkoyama.github.io/numerical-methods-atlas/problems/ale-nonuniform-transport/?lang=en) (`ale-nonuniform-transport`)

![Validation preview from actual saved PDE arrays and fixed-input refinement measurements.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/results/ale-nonuniform-transport-preview.png)

Upwind relative flux(a-w)q advances actual masses with identical predictor/corrector face geometry; record stage volumes and Courant numbers.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/ale-nonuniform-transport/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/ale-nonuniform-transport/?lang=en#code-en)

- [ALE scalar transport on genuinely nonuniform moving cells](https://hrkoyama.github.io/numerical-methods-atlas/validation/ale-nonuniform-transport/?lang=en) (`ale-nonuniform-transport`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/atlas-moving-waves-2026-11-23.zip)

Advance cell integrals and face positions with identical Heun stages, transporting a nonuniform analytic wave beyond a uniform GCL check.


#### Exact / reference solutions (`method-references-en`)

##### [ALE scalar transport on genuinely nonuniform moving cells](https://hrkoyama.github.io/numerical-methods-atlas/problems/ale-nonuniform-transport/?lang=en#references-en) (`ale-nonuniform-transport`)

- [ALE: analytic moving-cell integrals and separate time reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-ale-nonuniform-transport-en) (`ale-nonuniform-transport`; Same-problem reference; Analytic reference)

First-stage1D prescribed mesh motion. The x–t image is not2D physics; Euler Lagrange/remap and Saltzman piston remain future work.

[Existing reference profile](/numerical-methods-atlas/validation/ale-nonuniform-transport/?lang=en#ale-nonuniform-transport-en-measurements)

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/ale/)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

##### ALE scalar transport on genuinely nonuniform moving cells (`ale-nonuniform-transport`)

[ALE scalar transport on genuinely nonuniform moving cells](https://hrkoyama.github.io/numerical-methods-atlas/problems/ale-nonuniform-transport/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/ale-nonuniform-transport/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/atlas-moving-waves-2026-11-23.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/verification.json)

Advance cell integrals and face positions with identical Heun stages, transporting a nonuniform analytic wave beyond a uniform GCL check.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Additional nonuniform1D prescribed moving-grid scalar advances face positions and masses with shared Heun stages. Check actual relative upwind flux,GCL,analytic moving-cell integrals and temporal error.

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[Related code edition / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### Related source

- [/code/numerical-methods-atlas/2026-11-21/numart/geometry.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/geometry.py)
- [/code/validated-examples/2026-11-23/moving-waves/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/run.py)
- [/code/validated-examples/2026-11-23/moving-waves/transport.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/transport.py)
- [/code/validated-examples/2026-11-23/moving-waves/references/exact.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/references/exact.py)
- [/code/validated-examples/2026-11-23/moving-waves/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/experiments.py)

###### Package tests

- [/code/numerical-methods-atlas/2026-11-21/tests/test_time_geometry.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_time_geometry.py)
- [/code/validated-examples/2026-11-23/moving-waves/test_moving.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/test_moving.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q tests/test_time_geometry.py
```
