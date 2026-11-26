# 可変エディントン因子：周期1D散乱源の固定検証

形式的な角度輸送と独立なモーメント方程式を反復結合し、位置で変わる因子fを閉形式参照と比較します。

**使用手法**

- [可変Eddington因子（1D VEF）](https://hrkoyama.github.io/numerical-methods-atlas/methods/variable-eddington-factor/?lang=ja) (`variable-eddington-factor`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/vef-fourier-scattering1d/?lang=ja#vef-fourier-scattering1d-ja-algorithm)

各反復でq+σs E_LOをFourier形式解へ入れ、f=Kxx/E_HOを抽出し、保存的な面流束を使う有限差分モーメント式を解きます。参照解は主計算の閉包へ渡しません。

$$
\mu\partial_xI+\sigma_tI=\sigma_sE+q,\quad E=\langle I\rangle,\quad f=\langle\mu^2I\rangle/E
$$

$$
\partial_xH+\sigma_aE=q,\quad \partial_x(fE)+\sigma_tH=0
$$

$$
R=\frac{\arctan(k/\sigma_t)}{k},\quad A=\frac{b}{1-\sigma_sR},\quad E_{\rm ref}=1+\Re(ARe^{ikx})
$$

- [静止灰色輻射のVEF・VETモーメント閉包](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#static-grey-variable-eddington-moments-ja) (`static-grey-variable-eddington-moments`)

静止・定常・灰色の単位周期区間。無次元でσt=4、σs=3、σa=1、c=1。q=1+0.3 cos(2πx)、x_i=i/Nの点値です。角度平均は(1/2)∫I dμで規格化します。


**問題の図**

![可変エディントン因子：周期1D散乱源の固定検証：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/results/vef-fourier-scattering1d.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[可変エディントン因子：周期1D散乱源の固定検証](https://hrkoyama.github.io/numerical-methods-atlas/problems/vef-fourier-scattering1d/?lang=ja) (`vef-fourier-scattering1d`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/vef-fourier-scattering1d/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/vef-fourier-scattering1d/?lang=ja#vef-fourier-scattering1d-ja-validation)

N=33/65と固定32点角度則、N=65の64点角度プローブを分けます。解析場・複素モード・保存・実現可能性・反復残差・誤符号等の負制御、別のN=9一定源行を照合します。

- [本例のために導出した周期1D VEFの連続Fourier応答](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-vef-fourier-scattering1d-ja) (`vef-fourier-scattering1d`; 同じ問題の参照 · 解析参照)

正の指定等方輻射源に対する連続角度Fourier応答が、同じ固定問題の解析参照です。点値・面位置・複素位相を区別し、異なるHO/LO離散化の差は保存します。 図の横軸xと角度余弦μは2つの空間次元ではありません。周期・一様係数の教育例で、流入境界、時間発展、物質・流体結合、非線形FLD、一般AP性や速度向上は検証しません。
## 前提・単位・境界

静止・定常・灰色の単位周期区間。無次元でσt=4、σs=3、σa=1、c=1。q=1+0.3 cos(2πx)、x_i=i/Nの点値です。角度平均は(1/2)∫I dμで規格化します。

**編集上の補足**

図の横軸xと角度余弦μは2つの空間次元ではありません。周期・一様係数の教育例で、流入境界、時間発展、物質・流体結合、非線形FLD、一般AP性や速度向上は検証しません。

## 採用した計算法

各反復でq+σs E_LOをFourier形式解へ入れ、f=Kxx/E_HOを抽出し、保存的な面流束を使う有限差分モーメント式を解きます。参照解は主計算の閉包へ渡しません。

$$
\mu\partial_xI+\sigma_tI=\sigma_sE+q,\quad E=\langle I\rangle,\quad f=\langle\mu^2I\rangle/E
$$

$$
\partial_xH+\sigma_aE=q,\quad \partial_x(fE)+\sigma_tH=0
$$

$$
R=\frac{\arctan(k/\sigma_t)}{k},\quad A=\frac{b}{1-\sigma_sR},\quad E_{\rm ref}=1+\Re(ARe^{ikx})
$$

## 比較・検証

N=33/65と固定32点角度則、N=65の64点角度プローブを分けます。解析場・複素モード・保存・実現可能性・反復残差・誤符号等の負制御、別のN=9一定源行を照合します。

## 確認の限界

図の横軸xと角度余弦μは2つの空間次元ではありません。周期・一様係数の教育例で、流入境界、時間発展、物質・流体結合、非線形FLD、一般AP性や速度向上は検証しません。

## 保存実測値と判定

```json
{
  "metrics": {
    "finest_E_relative_rms_error": 3.0084362898696935e-05,
    "finest_face_H_relative_rms_error": 0.0001843336208869165,
    "finest_mode_complex_relative_error": 0.00046313206947184505,
    "finest_D_component_max_abs_error": 2.562663219352057e-06,
    "E_error_refinement_ratio": 0.2575572363841145,
    "face_H_error_refinement_ratio": 0.25786212296040795,
    "HO_LO_gap_refinement_ratio": 0.2575572378802047,
    "angle_probe_E_relative_rms_difference": 7.903639960737542e-15,
    "angle_probe_D_max_abs_difference": 7.216449660063518e-15,
    "finest_nonconstant_f_span": 0.019387902446938998,
    "finest_max_abs_Dxy": 0.0,
    "main_rows": 3,
    "constant_control_rows": 1,
    "outer_iterations_by_row": {
      "space-coarse": 13,
      "space-fine": 13,
      "angle-probe": 13,
      "constant-control": 1
    }
  },
  "checks": {
    "all_row_solver_checks": true,
    "finest_E_accuracy": true,
    "finest_face_H_accuracy": true,
    "complex_source_modes_include_phase": true,
    "tensor_reference_accuracy": true,
    "E_refines": true,
    "face_H_refines": true,
    "HO_LO_gap_refines_not_zero": true,
    "angle_probe_E": true,
    "angle_probe_D": true,
    "variable_closure": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/vef-fourier-scattering1d/index.json

![保存した点値・面流束の誤差、空間細分化、角度プローブと反復履歴。一定源は別制御です。](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/results/vef-fourier-scattering1d-diagnostics.png)

保存した点値・面流束の誤差、空間細分化、角度プローブと反復履歴。一定源は別制御です。

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/atlas-variable-eddington-controls-2026-11-26.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

## 出典と確認範囲

- On the Use of Variable Eddington Factors in Non-LTE Stellar Atmospheres Computations [accessed 2026-11-26]. https://academic.oup.com/mnras/article/149/1/65/2604466; review_level=primary-publisher-abstract-and-bibliography
選択箇所のみの読解です。出版社抄録・書誌のみ。原PDFの式・試験は未読であり、再現の主張はありません。

- High-Order Mixed Finite Element Variable Eddington Factor Methods [accessed 2026-11-26]. https://arxiv.org/pdf/2301.04758; review_level=selected-primary-equations
選択箇所のみの読解です。原論文の全試験・性能や実装全体の再現は主張しません。具体的な読解範囲と未読部分はsource-reading.jsonに記録します。

- A Family of Independent Variable Eddington Factor Methods with Efficient Preconditioned Iterative Solvers [accessed 2026-11-26]. https://arxiv.org/pdf/2111.12255; review_level=selected-primary-method-scope
選択箇所のみの読解です。原論文の全試験・性能や実装全体の再現は主張しません。具体的な読解範囲と未読部分はsource-reading.jsonに記録します。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Variable Eddington factor: a periodic 1D scattering-source control

Iteratively couple formal angular transport to independent moment equations and compare the spatially varying factor f with a closed-form reference.

**Methods used**

- [Variable Eddington factor (1D VEF)](https://hrkoyama.github.io/numerical-methods-atlas/methods/variable-eddington-factor/?lang=en) (`variable-eddington-factor`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/vef-fourier-scattering1d/?lang=en#vef-fourier-scattering1d-en-algorithm)

At each iteration solve formal Fourier transport with q+ss E_LO, extract f=Kxx/E_HO, and solve finite-difference moment equations using shared conservative faces. The primary closure never receives the analytic reference.

$$
\mu\partial_xI+\sigma_tI=\sigma_sE+q,\quad E=\langle I\rangle,\quad f=\langle\mu^2I\rangle/E
$$

$$
\partial_xH+\sigma_aE=q,\quad \partial_x(fE)+\sigma_tH=0
$$

$$
R=\frac{\arctan(k/\sigma_t)}{k},\quad A=\frac{b}{1-\sigma_sR},\quad E_{\rm ref}=1+\Re(ARe^{ikx})
$$

- [Static grey VEF/VET moment closure](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#static-grey-variable-eddington-moments-en) (`static-grey-variable-eddington-moments`)

Static steady grey unit-periodic interval; dimensionless st=4, ss=3, sa=1 and c=1. q=1+0.3 cos(2pi x), sampled as point values at x_i=i/N. Angular averages use (1/2) integral I dmu.


**Problem figure**

![Variable Eddington factor: a periodic 1D scattering-source control: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/results/vef-fourier-scattering1d.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Variable Eddington factor: a periodic 1D scattering-source control](https://hrkoyama.github.io/numerical-methods-atlas/problems/vef-fourier-scattering1d/?lang=en) (`vef-fourier-scattering1d`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/vef-fourier-scattering1d/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/vef-fourier-scattering1d/?lang=en#vef-fourier-scattering1d-en-validation)

Separate N=33/65 refinement at32 angular points from a64-point probe at N=65. Check analytic fields and complex modes, conservation, realizability, iteration residuals, negative controls and a separate N=9 constant-source row.

- [Authored continuum Fourier response for periodic 1D VEF](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-vef-fourier-scattering1d-en) (`vef-fourier-scattering1d`; Same-problem reference · Analytic reference)

The continuum-angle Fourier response to the prescribed positive isotropic source is an analytic reference for this same fixed problem. Keep point/face locations and complex phase distinct, retaining the independent HO/LO discretization gap. Position x and angular cosine mu are not two spatial dimensions. This periodic homogeneous educational control does not validate inflow boundaries, time evolution, material/fluid coupling, nonlinear FLD, general AP properties or speedup.
## Assumptions, units and boundaries

Static steady grey unit-periodic interval; dimensionless st=4, ss=3, sa=1 and c=1. q=1+0.3 cos(2pi x), sampled as point values at x_i=i/N. Angular averages use (1/2) integral I dmu.

**Editorial clarification**

Position x and angular cosine mu are not two spatial dimensions. This periodic homogeneous educational control does not validate inflow boundaries, time evolution, material/fluid coupling, nonlinear FLD, general AP properties or speedup.

## Adopted numerical method

At each iteration solve formal Fourier transport with q+ss E_LO, extract f=Kxx/E_HO, and solve finite-difference moment equations using shared conservative faces. The primary closure never receives the analytic reference.

$$
\mu\partial_xI+\sigma_tI=\sigma_sE+q,\quad E=\langle I\rangle,\quad f=\langle\mu^2I\rangle/E
$$

$$
\partial_xH+\sigma_aE=q,\quad \partial_x(fE)+\sigma_tH=0
$$

$$
R=\frac{\arctan(k/\sigma_t)}{k},\quad A=\frac{b}{1-\sigma_sR},\quad E_{\rm ref}=1+\Re(ARe^{ikx})
$$

## References and validation

Separate N=33/65 refinement at32 angular points from a64-point probe at N=65. Check analytic fields and complex modes, conservation, realizability, iteration residuals, negative controls and a separate N=9 constant-source row.

## Limits

Position x and angular cosine mu are not two spatial dimensions. This periodic homogeneous educational control does not validate inflow boundaries, time evolution, material/fluid coupling, nonlinear FLD, general AP properties or speedup.

## Stored measurements and decisions

```json
{
  "metrics": {
    "finest_E_relative_rms_error": 3.0084362898696935e-05,
    "finest_face_H_relative_rms_error": 0.0001843336208869165,
    "finest_mode_complex_relative_error": 0.00046313206947184505,
    "finest_D_component_max_abs_error": 2.562663219352057e-06,
    "E_error_refinement_ratio": 0.2575572363841145,
    "face_H_error_refinement_ratio": 0.25786212296040795,
    "HO_LO_gap_refinement_ratio": 0.2575572378802047,
    "angle_probe_E_relative_rms_difference": 7.903639960737542e-15,
    "angle_probe_D_max_abs_difference": 7.216449660063518e-15,
    "finest_nonconstant_f_span": 0.019387902446938998,
    "finest_max_abs_Dxy": 0.0,
    "main_rows": 3,
    "constant_control_rows": 1,
    "outer_iterations_by_row": {
      "space-coarse": 13,
      "space-fine": 13,
      "angle-probe": 13,
      "constant-control": 1
    }
  },
  "checks": {
    "all_row_solver_checks": true,
    "finest_E_accuracy": true,
    "finest_face_H_accuracy": true,
    "complex_source_modes_include_phase": true,
    "tensor_reference_accuracy": true,
    "E_refines": true,
    "face_H_refines": true,
    "HO_LO_gap_refines_not_zero": true,
    "angle_probe_E": true,
    "angle_probe_D": true,
    "variable_closure": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/vef-fourier-scattering1d/index.json

![Saved point/face errors, spatial refinement, a separate angular probe and iteration history. The constant source is a separate control.](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/results/vef-fourier-scattering1d-diagnostics.png)

Saved point/face errors, spatial refinement, a separate angular probe and iteration history. The constant source is a separate control.

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/atlas-variable-eddington-controls-2026-11-26.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

## Sources and review scope

- On the Use of Variable Eddington Factors in Non-LTE Stellar Atmospheres Computations [accessed 2026-11-26]. https://academic.oup.com/mnras/article/149/1/65/2604466; review_level=primary-publisher-abstract-and-bibliography
Publisher title/authors/date/DOI and abstract. Establishes historical variable-factor iteration and grey example. Unread limit: Original scannedPDF fetch failed; original equations, full tests and non-LTE calculations are unread and must not be claimed reproduced.

- High-Order Mixed Finite Element Variable Eddington Factor Methods [accessed 2026-11-26]. https://arxiv.org/pdf/2301.04758; review_level=selected-primary-equations
Section2, PDFpp3–4: transport Eq1, moment equations Eq2, angular tensor and boundary factor Eq3, fixed-point steps. Introduction on independent spatial discretizations also read. Unread limit: No claim of full59page reading, high-order mixedFEM reproduction, curved-mesh, multigrid or scalability validation.

- A Family of Independent Variable Eddington Factor Methods with Efficient Preconditioned Iterative Solvers [accessed 2026-11-26]. https://arxiv.org/pdf/2111.12255; review_level=selected-primary-method-scope
Introduction PDFpp1–3 on independent HO/LO discretizations, finite-mesh moment differences and conservation; no numerical tables adopted. Unread limit: No claim of reproducing high-orderDG, preconditioner performance or large-mesh studies.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
