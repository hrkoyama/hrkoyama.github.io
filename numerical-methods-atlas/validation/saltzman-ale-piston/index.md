# Saltzman型の歪み格子ピストン：2次元EulerとALE

2023年版の歪み格子と有限初期圧力を明示した、所与の格子移動による2次元Eulerピストン計算。

**使用手法**

- [ALE一様状態・幾何保存モデル](https://hrkoyama.github.io/numerical-methods-atlas/methods/ale/?lang=ja) (`ale`)
- [Rusanov／局所Lax–Friedrichs流束](https://hrkoyama.github.io/numerical-methods-atlas/methods/rusanov/?lang=ja) (`rusanov`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/saltzman-ale-piston/?lang=ja#saltzman-ale-piston-ja-algorithm)

固定入力・宣言したアルゴリズム・補正しない停止条件を用います。

- [圧縮性Euler方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#euler-ja) (`euler`)

Tan–Lv–Zhu (2023) Example 8 の e0=10^-4 を明示した有限圧力版。所与のアフィンALE格子を使う2D Euler/Rusanov例で、物質追従格子、WENO、remapや1985原報の全面再現ではありません。


**問題の図**

![Saltzman型の歪み格子ピストン：2次元EulerとALE：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/saltzman-ale-piston.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Saltzman型の歪み格子ピストン：2次元EulerとALE](https://hrkoyama.github.io/numerical-methods-atlas/problems/saltzman-ale-piston/?lang=ja) (`saltzman-ale-piston`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/saltzman-ale-piston/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/saltzman-ale-piston/?lang=ja#saltzman-ale-piston-ja-validation)

解析参照、保存量、細分化、独立成分検査と意図した誤式の負例を区別して保存します。

- [Saltzman型の歪み格子ピストン：2次元EulerとALE](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-saltzman-ale-piston-ja) (`saltzman-ale-piston`; 同じ問題の参照 · 解析参照)

固定入力の式・参照・図と実行コードを対応付けます。 Tan–Lv–Zhu (2023) Example 8 の e0=10^-4 を明示した有限圧力版。所与のアフィンALE格子を使う2D Euler/Rusanov例で、物質追従格子、WENO、remapや1985原報の全面再現ではありません。
## 前提・単位・境界

2023年版の歪み格子と有限初期圧力を明示した、所与の格子移動による2次元Eulerピストン計算。 固定入力の条件・境界・参照の範囲はinputs.jsonを参照。

**編集上の補足**

Tan–Lv–Zhu (2023) Example 8 の e0=10^-4 を明示した有限圧力版。所与のアフィンALE格子を使う2D Euler/Rusanov例で、物質追従格子、WENO、remapや1985原報の全面再現ではありません。

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
    "finest": {
      "grid": [
        80,
        8
      ],
      "density_error": 0.03966960674770006,
      "shock_error": 0.009071663139626374,
      "plateau_density_error": 0.060142667838002595,
      "plateau_pressure_error": 0.07005129077711092,
      "max_transverse": 0.08502093161153988,
      "mass_defect": 4.1551145858098734e-16,
      "momentum_defect": 1.3877787807814449e-15,
      "energy_defect": 3.5023519269671693e-15,
      "GCL": 3.7705883405261993e-17,
      "steps": 1333,
      "minimum_density": 0.9999999999997568,
      "minimum_pressure": 6.66666666666505e-05
    }
  },
  "checks": {
    "positive": true,
    "conservation": true,
    "GCL": true,
    "density": true,
    "refinement": true,
    "shock": true,
    "plateau": true,
    "transverse": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/saltzman-ale-piston/index.json

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

# Saltzman-type skew-grid piston: 2D Euler and ALE

Tan–Lv–Zhu2023 Example8 e0=1e-4 initialvariant. PrescribedaffineALEmesh, not theirWENO/materialLagrangian/remap scheme. Finitepressure RH cellaverages.

**Methods used**

- [ALE uniform-state / geometric-conservation model](https://hrkoyama.github.io/numerical-methods-atlas/methods/ale/?lang=en) (`ale`)
- [Rusanov / local Lax–Friedrichs flux](https://hrkoyama.github.io/numerical-methods-atlas/methods/rusanov/?lang=en) (`rusanov`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/saltzman-ale-piston/?lang=en#saltzman-ale-piston-en-algorithm)

Tan–Lv–Zhu2023 Example8 e0=1e-4 initialvariant. PrescribedaffineALEmesh, not theirWENO/materialLagrangian/remap scheme. Finitepressure RH cellaverages.

- [Compressible Euler equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#euler-en) (`euler`)

Tan–Lv–Zhu (2023) Example 8 variant with e0=1e-4 and finite initial pressure. Prescribed affine ALE, 2D Euler and Rusanov; not their material Lagrangian mesh, WENO/remap scheme or a full reproduction of the unread 1985 report.


**Problem figure**

![Saltzman-type skew-grid piston: 2D Euler and ALE: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/saltzman-ale-piston.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Saltzman-type skew-grid piston: 2D Euler and ALE](https://hrkoyama.github.io/numerical-methods-atlas/problems/saltzman-ale-piston/?lang=en) (`saltzman-ale-piston`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/saltzman-ale-piston/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/saltzman-ale-piston/?lang=en#saltzman-ale-piston-en-validation)

Separate analytic/reference errors, conservation, refinement, independent component qualification and deliberately wrong-formula controls.

- [Saltzman-type skew-grid piston: 2D Euler and ALE](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-saltzman-ale-piston-en) (`saltzman-ale-piston`; Same-problem reference · Analytic reference)

Bind the fixed-input formula, reference, figure and executable code. Tan–Lv–Zhu (2023) Example 8 variant with e0=1e-4 and finite initial pressure. Prescribed affine ALE, 2D Euler and Rusanov; not their material Lagrangian mesh, WENO/remap scheme or a full reproduction of the unread 1985 report.
## Assumptions, units and boundaries

Tan–Lv–Zhu2023 Example8 e0=1e-4 initialvariant. PrescribedaffineALEmesh, not theirWENO/materialLagrangian/remap scheme. Finitepressure RH cellaverages.

**Editorial clarification**

Tan–Lv–Zhu (2023) Example 8 variant with e0=1e-4 and finite initial pressure. Prescribed affine ALE, 2D Euler and Rusanov; not their material Lagrangian mesh, WENO/remap scheme or a full reproduction of the unread 1985 report.

## Adopted numerical method

Tan–Lv–Zhu2023 Example8 e0=1e-4 initialvariant. PrescribedaffineALEmesh, not theirWENO/materialLagrangian/remap scheme. Finitepressure RH cellaverages.

## References and validation

Separate analytic/reference errors, conservation, refinement, independent component qualification and deliberately wrong-formula controls.

## Limits

Tan–Lv–Zhu2023 Example8 e0=1e-4 initialvariant. PrescribedaffineALEmesh, not theirWENO/materialLagrangian/remap scheme. Finitepressure RH cellaverages.

## Stored measurements and decisions

```json
{
  "metrics": {
    "finest": {
      "grid": [
        80,
        8
      ],
      "density_error": 0.03966960674770006,
      "shock_error": 0.009071663139626374,
      "plateau_density_error": 0.060142667838002595,
      "plateau_pressure_error": 0.07005129077711092,
      "max_transverse": 0.08502093161153988,
      "mass_defect": 4.1551145858098734e-16,
      "momentum_defect": 1.3877787807814449e-15,
      "energy_defect": 3.5023519269671693e-15,
      "GCL": 3.7705883405261993e-17,
      "steps": 1333,
      "minimum_density": 0.9999999999997568,
      "minimum_pressure": 6.66666666666505e-05
    }
  },
  "checks": {
    "positive": true,
    "conservation": true,
    "GCL": true,
    "density": true,
    "refinement": true,
    "shock": true,
    "plateau": true,
    "transverse": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/saltzman-ale-piston/index.json

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
