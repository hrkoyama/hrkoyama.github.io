# Gaussian畳込みGSPHによるSod型粒子衝撃管

Gaussian畳込みの線形比体積近似と対称な可変平滑化長を使う、限定GSPH粒子流体計算。

**使用手法**

- [Godunov SPH／GSPH](https://hrkoyama.github.io/numerical-methods-atlas/methods/gsph/?lang=ja) (`gsph`)
- [SPHカーネル再構成](https://hrkoyama.github.io/numerical-methods-atlas/methods/sph/?lang=ja) (`sph`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/gsph-sod/?lang=ja#gsph-sod-ja-algorithm)

固定入力・宣言したアルゴリズム・補正しない停止条件を用います。

- [圧縮性Euler方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#euler-ja) (`euler`)

Gaussianの線形比体積畳み込み、対称な可変h、独立な対Riemann解と反対称な全エネルギー交換を持つGSPHです。通常SPHへp*を代入する代用ではありません。一次再構成に限定し、論文のcubic/MUSCLや一般精度を主張しません。


**問題の図**

![Gaussian畳込みGSPHによるSod型粒子衝撃管：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/gsph-sod.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Sod衝撃波管](https://hrkoyama.github.io/numerical-methods-atlas/problems/sod/?lang=ja) (`sod`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/sod/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/gsph-sod/?lang=ja#gsph-sod-ja-validation)

解析参照、保存量、細分化、独立成分検査と意図した誤式の負例を区別して保存します。

- [Euler／Sod問題](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-euler-sod-ja) (`euler-sod`; 関連モデルの参照 · 半解析参照)

γ=1.4、左右(ρ,u,p)=(1,0,1)/(0.125,0,0.1)、x0=0.5、[0,1]、t=0.2が一致します。点値・保存セル平均・誤差ノルムは別に確認します。 物理的な入力は一致しますが、参照カードの点値標本と保存計算の有限体積セル平均・離散格子は別表現です。

- [Gaussian畳込みGSPHによるSod型粒子衝撃管](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-gsph-sod-ja) (`gsph-sod`; 同じ問題の参照 · 半解析参照)

固定入力の式・参照・図と実行コードを対応付けます。 Gaussianの線形比体積畳み込み、対称な可変h、独立な対Riemann解と反対称な全エネルギー交換を持つGSPHです。通常SPHへp*を代入する代用ではありません。一次再構成に限定し、論文のcubic/MUSCLや一般精度を主張しません。
## 前提・単位・境界

Gaussian畳込みの線形比体積近似と対称な可変平滑化長を使う、限定GSPH粒子流体計算。 固定入力の条件・境界・参照の範囲はinputs.jsonを参照。

**編集上の補足**

Gaussianの線形比体積畳み込み、対称な可変h、独立な対Riemann解と反対称な全エネルギー交換を持つGSPHです。通常SPHへp*を代入する代用ではありません。一次再構成に限定し、論文のcubic/MUSCLや一般精度を主張しません。

## 採用した計算法

固定入力・宣言したアルゴリズム・補正しない停止条件を用います。

$$
\partial_tU+\partial_xF(U)=0
$$

$$
U=(\rho,\rho u,E)^{\mathsf T}
$$

$$
F=(\rho u,\rho u^2+p,u(E+p))^{\mathsf T}
$$

数式の編集補足：凍結配布版のコードと登録済み方程式に基づく記述です。配布版・計算・受入条件・保存結果は変更しません。

## 比較・検証

解析参照、保存量、細分化、独立成分検査と意図した誤式の負例を区別して保存します。

## 確認の限界

限定した教育用モデルです。元論文の全条件・全アルゴリズムや一般的な性能の再現ではありません。

## 保存実測値と判定

```json
{
  "metrics": {
    "finest_GSPH": {
      "method": "gsph",
      "right_particles": 32,
      "rho_error": 0.03789937718353325,
      "pressure_error": 0.040752681798075875,
      "shock_error": 0.011271366170524794,
      "defect": [
        0.0,
        2.220446049250313e-16,
        0.0
      ],
      "h_change": 1.5560167029698944,
      "steps": 518,
      "h_residual": 9.994160761956033e-11,
      "Riemann_residual": 1.5300261058115439e-15
    },
    "pair_swap_force_residual": 0.0,
    "pair_swap_energy_residual": 1.1102230246251565e-16,
    "oracle_pressure_root": 0.30313017805063625,
    "oracle_root_diagnostics": {
      "iterations": 45,
      "log_bracket_width": 1.3078427230084344e-13,
      "wave_residual": -5.773159728050814e-14
    }
  },
  "checks": {
    "pair_swap_force": true,
    "pair_swap_energy": true,
    "conservation": true,
    "rho": true,
    "pressure": true,
    "refinement": true,
    "shock": true,
    "h_solve": true,
    "Riemann": true,
    "adaptive_h": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/gsph-sod/index.json

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

# Sod-type particle shock tube with Gaussian-convolution GSPH

ActualInutsuka-linear-overlap variablehGSPH approximation withfirstorderpair states, comparedwithdistinctstandardSPHcontrol. Periodictwointerfaces; centralwindowbeforeouterwaves. Not cubic/MUSCLpaperreproduction or plainSPH-pressure-star surrogate.

**Methods used**

- [Godunov SPH / GSPH](https://hrkoyama.github.io/numerical-methods-atlas/methods/gsph/?lang=en) (`gsph`)
- [SPH kernel reconstruction](https://hrkoyama.github.io/numerical-methods-atlas/methods/sph/?lang=en) (`sph`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/gsph-sod/?lang=en#gsph-sod-en-algorithm)

ActualInutsuka-linear-overlap variablehGSPH approximation withfirstorderpair states, comparedwithdistinctstandardSPHcontrol. Periodictwointerfaces; centralwindowbeforeouterwaves. Not cubic/MUSCLpaperreproduction or plainSPH-pressure-star surrogate.

- [Compressible Euler equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#euler-en) (`euler`)

Actual Gaussian linear-specific-volume GSPH overlap with symmetric variable h, independent pair Riemann solves and antisymmetric total-energy exchange; not substitution of star pressure into ordinary SPH. First-order reconstruction only, not the paper cubic/MUSCL implementation or a general accuracy claim.


**Problem figure**

![Sod-type particle shock tube with Gaussian-convolution GSPH: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/gsph-sod.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Sod shock tube](https://hrkoyama.github.io/numerical-methods-atlas/problems/sod/?lang=en) (`sod`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/sod/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/gsph-sod/?lang=en#gsph-sod-en-validation)

Separate analytic/reference errors, conservation, refinement, independent component qualification and deliberately wrong-formula controls.

- [Euler / Sod](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-euler-sod-en) (`euler-sod`; Related-model reference · Semi-analytic reference)

γ=1.4, primitive states (1,0,1)/(0.125,0,0.1), x0=0.5, [0,1] and t=0.2 match. Inspect point/conserved-cell-average sampling and error norms separately. Physical inputs match, but the card’s point samples and the saved computation’s finite-volume cell averages/discrete grid are different representations.

- [Sod-type particle shock tube with Gaussian-convolution GSPH](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-gsph-sod-en) (`gsph-sod`; Same-problem reference · Semi-analytic reference)

Bind the fixed-input formula, reference, figure and executable code. Actual Gaussian linear-specific-volume GSPH overlap with symmetric variable h, independent pair Riemann solves and antisymmetric total-energy exchange; not substitution of star pressure into ordinary SPH. First-order reconstruction only, not the paper cubic/MUSCL implementation or a general accuracy claim.
## Assumptions, units and boundaries

ActualInutsuka-linear-overlap variablehGSPH approximation withfirstorderpair states, comparedwithdistinctstandardSPHcontrol. Periodictwointerfaces; centralwindowbeforeouterwaves. Not cubic/MUSCLpaperreproduction or plainSPH-pressure-star surrogate.

**Editorial clarification**

Actual Gaussian linear-specific-volume GSPH overlap with symmetric variable h, independent pair Riemann solves and antisymmetric total-energy exchange; not substitution of star pressure into ordinary SPH. First-order reconstruction only, not the paper cubic/MUSCL implementation or a general accuracy claim.

## Adopted numerical method

ActualInutsuka-linear-overlap variablehGSPH approximation withfirstorderpair states, comparedwithdistinctstandardSPHcontrol. Periodictwointerfaces; centralwindowbeforeouterwaves. Not cubic/MUSCLpaperreproduction or plainSPH-pressure-star surrogate.

$$
\partial_tU+\partial_xF(U)=0
$$

$$
U=(\rho,\rho u,E)^{\mathsf T}
$$

$$
F=(\rho u,\rho u^2+p,u(E+p))^{\mathsf T}
$$

Editorial equations from the frozen code and registered models. The release, calculations, acceptance conditions and saved results are unchanged.

## References and validation

Separate analytic/reference errors, conservation, refinement, independent component qualification and deliberately wrong-formula controls.

## Limits

ActualInutsuka-linear-overlap variablehGSPH approximation withfirstorderpair states, comparedwithdistinctstandardSPHcontrol. Periodictwointerfaces; centralwindowbeforeouterwaves. Not cubic/MUSCLpaperreproduction or plainSPH-pressure-star surrogate.

## Stored measurements and decisions

```json
{
  "metrics": {
    "finest_GSPH": {
      "method": "gsph",
      "right_particles": 32,
      "rho_error": 0.03789937718353325,
      "pressure_error": 0.040752681798075875,
      "shock_error": 0.011271366170524794,
      "defect": [
        0.0,
        2.220446049250313e-16,
        0.0
      ],
      "h_change": 1.5560167029698944,
      "steps": 518,
      "h_residual": 9.994160761956033e-11,
      "Riemann_residual": 1.5300261058115439e-15
    },
    "pair_swap_force_residual": 0.0,
    "pair_swap_energy_residual": 1.1102230246251565e-16,
    "oracle_pressure_root": 0.30313017805063625,
    "oracle_root_diagnostics": {
      "iterations": 45,
      "log_bracket_width": 1.3078427230084344e-13,
      "wave_residual": -5.773159728050814e-14
    }
  },
  "checks": {
    "pair_swap_force": true,
    "pair_swap_energy": true,
    "conservation": true,
    "rho": true,
    "pressure": true,
    "refinement": true,
    "shock": true,
    "h_solve": true,
    "Riemann": true,
    "adaptive_h": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/gsph-sod/index.json

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
