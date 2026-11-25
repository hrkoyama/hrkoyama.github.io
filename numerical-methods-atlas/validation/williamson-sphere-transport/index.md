# Williamson型の球面固体回転輸送：傾いた軸と極通過

所与の固体回転速度で球面上のcosine bellを輸送し、傾いた軸・極通過・1周後の誤差を調べる限定例。

**使用手法**

- [セミラグランジュ法：所与球面回転の限定例](https://hrkoyama.github.io/numerical-methods-atlas/methods/semi-lagrangian/?lang=ja) (`semi-lagrangian`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/williamson-sphere-transport/?lang=ja#williamson-sphere-transport-ja-algorithm)

固定入力・宣言したアルゴリズム・補正しない停止条件を用います。

- [球面上の所与速度スカラー移流](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#sphere-scalar-advection-ja) (`sphere-scalar-advection`)

単位球の所与の剛体回転によるスカラー輸送だけです。原W92全文の式は未閲読で、Nairらの選択した著者資料との規約照合に限ります。両格子とも11回の非整合なremap。非保存の双線形補間で質量ずれを報告し、時間収束とは呼びません。


**問題の図**

![Williamson型の球面固体回転輸送：傾いた軸と極通過：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/williamson-sphere-transport.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Williamson型の球面固体回転輸送：傾いた軸と極通過](https://hrkoyama.github.io/numerical-methods-atlas/problems/williamson-sphere-transport/?lang=ja) (`williamson-sphere-transport`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/williamson-sphere-transport/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/williamson-sphere-transport/?lang=ja#williamson-sphere-transport-ja-validation)

解析参照、保存量、細分化、独立成分検査と意図した誤式の負例を区別して保存します。

- [Williamson型の球面固体回転輸送：傾いた軸と極通過](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-williamson-sphere-transport-ja) (`williamson-sphere-transport`; 同じ問題の参照 · 解析参照)

固定入力の式・参照・図と実行コードを対応付けます。 単位球の所与の剛体回転によるスカラー輸送だけです。原W92全文の式は未閲読で、Nairらの選択した著者資料との規約照合に限ります。両格子とも11回の非整合なremap。非保存の双線形補間で質量ずれを報告し、時間収束とは呼びません。
## 前提・単位・境界

所与の固体回転速度で球面上のcosine bellを輸送し、傾いた軸・極通過・1周後の誤差を調べる限定例。 固定入力の条件・境界・参照の範囲はinputs.jsonを参照。

**編集上の補足**

単位球の所与の剛体回転によるスカラー輸送だけです。原W92全文の式は未閲読で、Nairらの選択した著者資料との規約照合に限ります。両格子とも11回の非整合なremap。非保存の双線形補間で質量ずれを報告し、時間収束とは呼びません。

## 採用した計算法

固定入力・宣言したアルゴリズム・補正しない停止条件を用います。

## 比較・検証

解析参照、保存量、細分化、独立成分検査と意図した誤式の負例を区別して保存します。

## 確認の限界

限定した教育用モデルです。元論文の全条件・全アルゴリズムや一般的な性能の再現ではありません。

## 保存実測値と判定

```json
{
  "metrics": {
    "fine_L1": [
      0.17228372801445835,
      0.1983012829411487
    ]
  },
  "checks": {
    "error": true,
    "refinement": true,
    "mass": true,
    "bounds": true,
    "sphere_area": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/williamson-sphere-transport/index.json

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/atlas-continuum-particle-controls-2026-11-25.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

## 出典と確認範囲

- Reformulation of Smoothed Particle Hydrodynamics with Riemann Solver. https://arxiv.org/pdf/astro-ph/0206401; review_level=selected-original-author-paper-sections-and-equations
- New Third-Order Finite Volume Unequal-Sized WENO Lagrangian Schemes for Solving Euler Equations. https://www.mdpi.com/2227-7390/11/23/4842; review_level=selected-publisher-fulltext-example-8
- Second Order Corner Coupled Upwind Transport Methods for Lagrangian Hydrodynamics. https://www.osti.gov/servlets/purl/15005665; review_level=secondary-bibliographic-identity-original-report-unread
- A standard test set for numerical approximations to the shallow water equations in spherical geometry. https://digital.library.unt.edu/ark:/67531/metadc1069483/; review_level=author-report-bibliography-and-abstract-original-formulas-unread
- Cascade interpolation for semi-Lagrangian advection over the sphere. https://www.image.ucar.edu/staff/rnair/qj99_sph.pdf; review_level=selected-author-hosted-formulas-and-publisher-bibliography

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Williamson-type spherical rotation: tilted axes and pole crossing

Limitedprescribedscalartransport, radius1/3 nondimensionalvariant; not nonlinearSWE or exact1992fullpaperreproduction. Nair1999 selectedformulascrosscheck; bilinear method isAtlasoriginal.

**Methods used**

- [Semi-Lagrangian transport: a limited prescribed sphere rotation](https://hrkoyama.github.io/numerical-methods-atlas/methods/semi-lagrangian/?lang=en) (`semi-lagrangian`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/williamson-sphere-transport/?lang=en#williamson-sphere-transport-en-algorithm)

Limitedprescribedscalartransport, radius1/3 nondimensionalvariant; not nonlinearSWE or exact1992fullpaperreproduction. Nair1999 selectedformulascrosscheck; bilinear method isAtlasoriginal.

- [Prescribed scalar advection on a sphere](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#sphere-scalar-advection-en) (`sphere-scalar-advection`)

Only prescribed scalar solid-body rotation on a unit sphere. Original W92 equations remain unread; selected Nair author formulas cross-check conventions. Both grids use eleven noncommensurate remaps. Bilinear interpolation is nonconservative; report mass drift and do not claim temporal convergence or a nonlinear global SWE core.


**Problem figure**

![Williamson-type spherical rotation: tilted axes and pole crossing: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/williamson-sphere-transport.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Williamson-type spherical rotation: tilted axes and pole crossing](https://hrkoyama.github.io/numerical-methods-atlas/problems/williamson-sphere-transport/?lang=en) (`williamson-sphere-transport`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/williamson-sphere-transport/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/williamson-sphere-transport/?lang=en#williamson-sphere-transport-en-validation)

Separate analytic/reference errors, conservation, refinement, independent component qualification and deliberately wrong-formula controls.

- [Williamson-type spherical rotation: tilted axes and pole crossing](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-williamson-sphere-transport-en) (`williamson-sphere-transport`; Same-problem reference · Analytic reference)

Bind the fixed-input formula, reference, figure and executable code. Only prescribed scalar solid-body rotation on a unit sphere. Original W92 equations remain unread; selected Nair author formulas cross-check conventions. Both grids use eleven noncommensurate remaps. Bilinear interpolation is nonconservative; report mass drift and do not claim temporal convergence or a nonlinear global SWE core.
## Assumptions, units and boundaries

Limitedprescribedscalartransport, radius1/3 nondimensionalvariant; not nonlinearSWE or exact1992fullpaperreproduction. Nair1999 selectedformulascrosscheck; bilinear method isAtlasoriginal.

**Editorial clarification**

Only prescribed scalar solid-body rotation on a unit sphere. Original W92 equations remain unread; selected Nair author formulas cross-check conventions. Both grids use eleven noncommensurate remaps. Bilinear interpolation is nonconservative; report mass drift and do not claim temporal convergence or a nonlinear global SWE core.

## Adopted numerical method

Limitedprescribedscalartransport, radius1/3 nondimensionalvariant; not nonlinearSWE or exact1992fullpaperreproduction. Nair1999 selectedformulascrosscheck; bilinear method isAtlasoriginal.

## References and validation

Separate analytic/reference errors, conservation, refinement, independent component qualification and deliberately wrong-formula controls.

## Limits

Limitedprescribedscalartransport, radius1/3 nondimensionalvariant; not nonlinearSWE or exact1992fullpaperreproduction. Nair1999 selectedformulascrosscheck; bilinear method isAtlasoriginal.

## Stored measurements and decisions

```json
{
  "metrics": {
    "fine_L1": [
      0.17228372801445835,
      0.1983012829411487
    ]
  },
  "checks": {
    "error": true,
    "refinement": true,
    "mass": true,
    "bounds": true,
    "sphere_area": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/williamson-sphere-transport/index.json

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/atlas-continuum-particle-controls-2026-11-25.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

## Sources and review scope

- Reformulation of Smoothed Particle Hydrodynamics with Riemann Solver. https://arxiv.org/pdf/astro-ph/0206401; review_level=selected-original-author-paper-sections-and-equations
- New Third-Order Finite Volume Unequal-Sized WENO Lagrangian Schemes for Solving Euler Equations. https://www.mdpi.com/2227-7390/11/23/4842; review_level=selected-publisher-fulltext-example-8
- Second Order Corner Coupled Upwind Transport Methods for Lagrangian Hydrodynamics. https://www.osti.gov/servlets/purl/15005665; review_level=secondary-bibliographic-identity-original-report-unread
- A standard test set for numerical approximations to the shallow water equations in spherical geometry. https://digital.library.unt.edu/ark:/67531/metadc1069483/; review_level=author-report-bibliography-and-abstract-original-formulas-unread
- Cascade interpolation for semi-Lagrangian advection over the sphere. https://www.image.ucar.edu/staff/rnair/qj99_sph.pdf; review_level=selected-author-hosted-formulas-and-publisher-bibliography

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
