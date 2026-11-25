# Semi-Lagrangian transport: a limited prescribed sphere rotation / セミラグランジュ法：所与球面回転の限定例

Status: educational-example

Trace backward characteristics and interpolate at departure points; this example uses exact rigid-rotation departures and bilinear interpolation only.

逆向き特性から出発点を求めて補間する方法。ここでは厳密な剛体回転の出発点と双線形補間だけを用います。

Only prescribed scalar solid-body rotation on a unit sphere. Original W92 equations remain unread; selected Nair author formulas cross-check conventions. Both grids use eleven noncommensurate remaps. Bilinear interpolation is nonconservative; report mass drift and do not claim temporal convergence or a nonlinear global SWE core.

Other names: semi-Lagrangian, セミラグランジュ法

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-continuum-particle-controls/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-continuum-particle-controls/



- Reference: https://doi.org/10.1002/qj.1999.49712555617 — Selected author-hosted solid-body/bell formulas; this implementation is bilinear, not their cascade algorithm. Original W92 full text remains unread.

## Small fixed-input validation supplements

Only prescribed scalar solid-body rotation on a unit sphere. Original W92 equations remain unread; selected Nair author formulas cross-check conventions. Both grids use eleven noncommensurate remaps. Bilinear interpolation is nonconservative; report mass drift and do not claim temporal convergence or a nonlinear global SWE core.

単位球の所与の剛体回転によるスカラー輸送だけです。原W92全文の式は未閲読で、Nairらの選択した著者資料との規約照合に限ります。両格子とも11回の非整合なremap。非保存の双線形補間で質量ずれを報告し、時間収束とは呼びません。

- Williamson-type spherical rotation: tilted axes and pole crossing: https://hrkoyama.github.io/numerical-methods-atlas/validation/williamson-sphere-transport/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/atlas-continuum-particle-controls-2026-11-25.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/result.json

Common execution records: [{"id": "williamson-sphere-transport", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/williamson-sphere-transport/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/williamson-sphere-transport/?lang=en"}, "kind": "dedicated-supplement"}]

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/semi-lagrangian/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [球面上の所与速度スカラー移流](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#sphere-scalar-advection-ja) (`sphere-scalar-advection`; williamson-sphere-transport)

#### 問題の図 (`method-problems-ja`)

##### [Williamson型の球面固体回転輸送：傾いた軸と極通過](https://hrkoyama.github.io/numerical-methods-atlas/problems/williamson-sphere-transport/?lang=ja) (`williamson-sphere-transport`)

![所与の固体回転速度で球面上のcosine bellを輸送し、傾いた軸・極通過・1周後の誤差を調べる限定例。 単位球の所与の剛体回転によるスカラー輸送だけです。原W92全文の式は未閲読で、Nairらの選択した著者資料との規約照合に限ります。両格子とも11回の非整合なremap。非保存の双線形補間で質量ずれを報告し、時間収束とは呼びません。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/williamson-sphere-transport.png)

単位球の所与の剛体回転によるスカラー輸送だけです。原W92全文の式は未閲読で、Nairらの選択した著者資料との規約照合に限ります。両格子とも11回の非整合なremap。非保存の双線形補間で質量ずれを報告し、時間収束とは呼びません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/williamson-sphere-transport/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/williamson-sphere-transport/?lang=ja#code-ja)

- [Williamson型の球面固体回転輸送：傾いた軸と極通過](https://hrkoyama.github.io/numerical-methods-atlas/validation/williamson-sphere-transport/?lang=ja) (`williamson-sphere-transport`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/atlas-continuum-particle-controls-2026-11-25.zip)

所与の固体回転速度で球面上のcosine bellを輸送し、傾いた軸・極通過・1周後の誤差を調べる限定例。


#### 厳密解・参照解 (`method-references-ja`)

##### [Williamson型の球面固体回転輸送：傾いた軸と極通過](https://hrkoyama.github.io/numerical-methods-atlas/problems/williamson-sphere-transport/?lang=ja#references-ja) (`williamson-sphere-transport`)

- [Williamson型の球面固体回転輸送：傾いた軸と極通過](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-williamson-sphere-transport-ja) (`williamson-sphere-transport`; 同じ問題の参照; 解析参照)

固定入力の式・参照・図と実行コードを対応付けます。 単位球の所与の剛体回転によるスカラー輸送だけです。原W92全文の式は未閲読で、Nairらの選択した著者資料との規約照合に限ります。両格子とも11回の非整合なremap。非保存の双線形補間で質量ずれを報告し、時間収束とは呼びません。

[既存の参照図](/numerical-methods-atlas/validation/williamson-sphere-transport/?lang=ja#williamson-sphere-transport-ja-measurements)

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-continuum-particle-controls/)
- 保存結果: [この配布版の保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/result.json)
- 検証記録: [配布版の検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/verification.json)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

##### Williamson型の球面固体回転輸送：傾いた軸と極通過 (`williamson-sphere-transport`)

[Williamson型の球面固体回転輸送：傾いた軸と極通過](https://hrkoyama.github.io/numerical-methods-atlas/problems/williamson-sphere-transport/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/williamson-sphere-transport/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/atlas-continuum-particle-controls-2026-11-25.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/verification.json)

所与の固体回転速度で球面上のcosine bellを輸送し、傾いた軸・極通過・1周後の誤差を調べる限定例。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

単位球の所与の剛体回転によるスカラー輸送だけです。原W92全文の式は未閲読で、Nairらの選択した著者資料との規約照合に限ります。両格子とも11回の非整合なremap。非保存の双線形補間で質量ずれを報告し、時間収束とは呼びません。

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/atlas-continuum-particle-controls-2026-11-25.zip)

[配布版の検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/verification.json)

###### 関連ソース

- [/code/validated-examples/2026-11-25/continuum-particle-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/run.py)
- [/code/validated-examples/2026-11-25/continuum-particle-controls/ale_piston.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/ale_piston.py)
- [/code/validated-examples/2026-11-25/continuum-particle-controls/failure_support.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/failure_support.py)
- [/code/validated-examples/2026-11-25/continuum-particle-controls/gsph.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/gsph.py)
- [/code/validated-examples/2026-11-25/continuum-particle-controls/sphere.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/sphere.py)
- [/code/validated-examples/2026-11-25/continuum-particle-controls/reference_riemann.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/reference_riemann.py)

###### 配布版のテスト

- [/code/validated-examples/2026-11-25/continuum-particle-controls/test_components.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/test_components.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q
python run.py --input inputs.json --output output
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Prescribed scalar advection on a sphere](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#sphere-scalar-advection-en) (`sphere-scalar-advection`; williamson-sphere-transport)

#### Problem figures (`method-problems-en`)

##### [Williamson-type spherical rotation: tilted axes and pole crossing](https://hrkoyama.github.io/numerical-methods-atlas/problems/williamson-sphere-transport/?lang=en) (`williamson-sphere-transport`)

![Limitedprescribedscalartransport, radius1/3 nondimensionalvariant; not nonlinearSWE or exact1992fullpaperreproduction. Nair1999 selectedformulascrosscheck; bilinear method isAtlasoriginal. Only prescribed scalar solid-body rotation on a unit sphere. Original W92 equations remain unread; selected Nair author formulas cross-check conventions. Both grids use eleven noncommensurate remaps. Bilinear interpolation is nonconservative; report mass drift and do not claim temporal convergence or a nonlinear global SWE core.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/williamson-sphere-transport.png)

Only prescribed scalar solid-body rotation on a unit sphere. Original W92 equations remain unread; selected Nair author formulas cross-check conventions. Both grids use eleven noncommensurate remaps. Bilinear interpolation is nonconservative; report mass drift and do not claim temporal convergence or a nonlinear global SWE core.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/williamson-sphere-transport/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/williamson-sphere-transport/?lang=en#code-en)

- [Williamson-type spherical rotation: tilted axes and pole crossing](https://hrkoyama.github.io/numerical-methods-atlas/validation/williamson-sphere-transport/?lang=en) (`williamson-sphere-transport`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/atlas-continuum-particle-controls-2026-11-25.zip)

Limitedprescribedscalartransport, radius1/3 nondimensionalvariant; not nonlinearSWE or exact1992fullpaperreproduction. Nair1999 selectedformulascrosscheck; bilinear method isAtlasoriginal.


#### Exact / reference solutions (`method-references-en`)

##### [Williamson-type spherical rotation: tilted axes and pole crossing](https://hrkoyama.github.io/numerical-methods-atlas/problems/williamson-sphere-transport/?lang=en#references-en) (`williamson-sphere-transport`)

- [Williamson-type spherical rotation: tilted axes and pole crossing](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-williamson-sphere-transport-en) (`williamson-sphere-transport`; Same-problem reference; Analytic reference)

Bind the fixed-input formula, reference, figure and executable code. Only prescribed scalar solid-body rotation on a unit sphere. Original W92 equations remain unread; selected Nair author formulas cross-check conventions. Both grids use eleven noncommensurate remaps. Bilinear interpolation is nonconservative; report mass drift and do not claim temporal convergence or a nonlinear global SWE core.

[Existing reference profile](/numerical-methods-atlas/validation/williamson-sphere-transport/?lang=en#williamson-sphere-transport-en-measurements)

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-continuum-particle-controls/)
- Saved result: [Saved results from this edition](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/result.json)
- Verification receipt: [Edition verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/verification.json)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

##### Williamson-type spherical rotation: tilted axes and pole crossing (`williamson-sphere-transport`)

[Williamson-type spherical rotation: tilted axes and pole crossing](https://hrkoyama.github.io/numerical-methods-atlas/problems/williamson-sphere-transport/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/williamson-sphere-transport/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/atlas-continuum-particle-controls-2026-11-25.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/verification.json)

Limitedprescribedscalartransport, radius1/3 nondimensionalvariant; not nonlinearSWE or exact1992fullpaperreproduction. Nair1999 selectedformulascrosscheck; bilinear method isAtlasoriginal.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Only prescribed scalar solid-body rotation on a unit sphere. Original W92 equations remain unread; selected Nair author formulas cross-check conventions. Both grids use eleven noncommensurate remaps. Bilinear interpolation is nonconservative; report mass drift and do not claim temporal convergence or a nonlinear global SWE core.

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[Related code edition / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/atlas-continuum-particle-controls-2026-11-25.zip)

[Edition verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/verification.json)

###### Related source

- [/code/validated-examples/2026-11-25/continuum-particle-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/run.py)
- [/code/validated-examples/2026-11-25/continuum-particle-controls/ale_piston.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/ale_piston.py)
- [/code/validated-examples/2026-11-25/continuum-particle-controls/failure_support.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/failure_support.py)
- [/code/validated-examples/2026-11-25/continuum-particle-controls/gsph.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/gsph.py)
- [/code/validated-examples/2026-11-25/continuum-particle-controls/sphere.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/sphere.py)
- [/code/validated-examples/2026-11-25/continuum-particle-controls/reference_riemann.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/reference_riemann.py)

###### Package tests

- [/code/validated-examples/2026-11-25/continuum-particle-controls/test_components.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/test_components.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q
python run.py --input inputs.json --output output
```
