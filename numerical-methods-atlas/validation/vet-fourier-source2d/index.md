# 可変エディントンテンソル：周期2D非平行源の固定検証

非平行な2つの源モードから全S²角度分布と3×3テンソルを求め、Dxyを含む保存的モーメント式と閉形式参照を比較します。

**使用手法**

- [可変Eddingtonテンソル（VET）](https://hrkoyama.github.io/numerical-methods-atlas/methods/variable-eddington-tensor/?lang=ja) (`variable-eddington-tensor`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/vet-fourier-source2d/?lang=ja#vet-fourier-source2d-ja-algorithm)

形式的なFourier角度輸送→D=K_HO/E_HO→独立な有限差分モーメント式を反復します。Dxyの両交差微分を共有面流束へ含め、局所・大域の離散収支を確認します。

$$
\boldsymbol\Omega\cdot\nabla I+\sigma_tI=\sigma_sE+q,\quad D=\frac{\langle\boldsymbol\Omega\boldsymbol\Omega^TI\rangle}{\langle I\rangle}
$$

$$
\sigma_t\sigma_aE-\partial_{xx}(D_{xx}E)-2\partial_{xy}(D_{xy}E)-\partial_{yy}(D_{yy}E)=\sigma_tq
$$

$$
K_k=A\left[T\mathbb I+(C-T)\hat k\hat k^T\right],\quad C=\frac{\sigma_t(1-\sigma_tR)}{k^2},\quad T=\frac{R-C}{2}
$$

- [静止灰色輻射のVEF・VETモーメント閉包](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#static-grey-variable-eddington-moments-ja) (`static-grey-variable-eddington-moments`)

静止・定常・灰色の単位周期正方形。σt=4、σs=3、σa=1、c=1の無次元点値。q=1+0.3 cos(2πx)+0.2 sin(2π(x+y))。空間は2Dでも角度は全S²でDzzも保持します。


**問題の図**

![可変エディントンテンソル：周期2D非平行源の固定検証：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/results/vet-fourier-source2d.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[可変エディントンテンソル：周期2D非平行源の固定検証](https://hrkoyama.github.io/numerical-methods-atlas/problems/vet-fourier-source2d/?lang=ja) (`vet-fourier-source2d`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/vet-fourier-source2d/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/vet-fourier-source2d/?lang=ja#vet-fourier-source2d-ja-validation)

17²/33²と12×48角度則、33²の16×64角度プローブを区別します。解析E/H/K/D、位相を含む複素モード、独立角度積分、テンソル制約、混合項の負制御、N=9²一定源を照合します。

- [本例のために導出した周期2D VETの連続Fourier応答](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-vet-fourier-source2d-ja) (`vet-fourier-source2d`; 同じ問題の参照 · 解析参照)

正の指定等方輻射源に対する連続角度Fourier応答が、同じ固定問題の解析参照です。点値・面位置・複素位相を区別し、異なるHO/LO離散化の差は保存します。 局所M1との比較は閉包の点ごとの診断だけで、M1方程式は解きません。Athena・短い特性線法・影・交差ビーム・RHD・境界閉包の再現でもなく、固定格子でHO/LOの厳密一致や普遍的な収束率を主張しません。
## 前提・単位・境界

静止・定常・灰色の単位周期正方形。σt=4、σs=3、σa=1、c=1の無次元点値。q=1+0.3 cos(2πx)+0.2 sin(2π(x+y))。空間は2Dでも角度は全S²でDzzも保持します。

**編集上の補足**

局所M1との比較は閉包の点ごとの診断だけで、M1方程式は解きません。Athena・短い特性線法・影・交差ビーム・RHD・境界閉包の再現でもなく、固定格子でHO/LOの厳密一致や普遍的な収束率を主張しません。

## 採用した計算法

形式的なFourier角度輸送→D=K_HO/E_HO→独立な有限差分モーメント式を反復します。Dxyの両交差微分を共有面流束へ含め、局所・大域の離散収支を確認します。

$$
\boldsymbol\Omega\cdot\nabla I+\sigma_tI=\sigma_sE+q,\quad D=\frac{\langle\boldsymbol\Omega\boldsymbol\Omega^TI\rangle}{\langle I\rangle}
$$

$$
\sigma_t\sigma_aE-\partial_{xx}(D_{xx}E)-2\partial_{xy}(D_{xy}E)-\partial_{yy}(D_{yy}E)=\sigma_tq
$$

$$
K_k=A\left[T\mathbb I+(C-T)\hat k\hat k^T\right],\quad C=\frac{\sigma_t(1-\sigma_tR)}{k^2},\quad T=\frac{R-C}{2}
$$

## 比較・検証

17²/33²と12×48角度則、33²の16×64角度プローブを区別します。解析E/H/K/D、位相を含む複素モード、独立角度積分、テンソル制約、混合項の負制御、N=9²一定源を照合します。

## 確認の限界

局所M1との比較は閉包の点ごとの診断だけで、M1方程式は解きません。Athena・短い特性線法・影・交差ビーム・RHD・境界閉包の再現でもなく、固定格子でHO/LOの厳密一致や普遍的な収束率を主張しません。

## 保存実測値と判定

```json
{
  "metrics": {
    "finest_E_relative_rms_error": 0.00012228131179061114,
    "finest_face_H_relative_rms_error": 0.0010738390026674726,
    "finest_mode_complex_relative_error": 0.0017983436413314031,
    "finest_D_component_max_abs_error": 1.0250275895629102e-05,
    "E_error_refinement_ratio": 0.2655289724016241,
    "face_H_error_refinement_ratio": 0.26613409578253794,
    "HO_LO_gap_refinement_ratio": 0.2657021024383582,
    "angle_probe_E_relative_rms_difference": 2.3900276798110385e-07,
    "angle_probe_D_max_abs_difference": 2.4197709053153105e-07,
    "finest_nonconstant_f_span": 0.022629325122685784,
    "finest_max_abs_Dxy": 0.0052432003949135775,
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

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/vet-fourier-source2d/index.json

![保存した面流束誤差・Dzz・空間/角度比較と反復残差。全3×3テンソルを保持します。](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/results/vet-fourier-source2d-diagnostics.png)

保存した面流束誤差・Dzz・空間/角度比較と反復残差。全3×3テンソルを保持します。

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

- A Godunov Method for Multidimensional Radiation Magnetohydrodynamics based on a variable Eddington tensor [accessed 2026-11-26]. https://arxiv.org/pdf/1201.2223; review_level=selected-primary-equations-and-test-description
選択箇所のみの読解です。原論文の全試験・性能や実装全体の再現は主張しません。具体的な読解範囲と未読部分はsource-reading.jsonに記録します。

- A Radiation Transfer Solver for Athena using Short Characteristics [accessed 2026-11-26]. https://arxiv.org/pdf/1201.2222; review_level=selected-primary-equations
選択箇所のみの読解です。原論文の全試験・性能や実装全体の再現は主張しません。具体的な読解範囲と未読部分はsource-reading.jsonに記録します。

- High-Order Mixed Finite Element Variable Eddington Factor Methods [accessed 2026-11-26]. https://arxiv.org/pdf/2301.04758; review_level=selected-primary-equations
選択箇所のみの読解です。原論文の全試験・性能や実装全体の再現は主張しません。具体的な読解範囲と未読部分はsource-reading.jsonに記録します。

- A Two-moment Radiation Hydrodynamics Module in Athena Using a Time-explicit Godunov Method [accessed 2026-11-26]. https://arxiv.org/pdf/1306.0010; review_level=selected-primary-equations
選択箇所のみの読解です。原論文の全試験・性能や実装全体の再現は主張しません。具体的な読解範囲と未読部分はsource-reading.jsonに記録します。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Variable Eddington tensor: a periodic 2D nonparallel-source control

Use two nonparallel source modes to compute full-S2 angular moments and a3x3 tensor, then compare conservative moment equations including Dxy with a closed-form reference.

**Methods used**

- [Variable Eddington tensor (VET)](https://hrkoyama.github.io/numerical-methods-atlas/methods/variable-eddington-tensor/?lang=en) (`variable-eddington-tensor`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/vet-fourier-source2d/?lang=en#vet-fourier-source2d-en-algorithm)

Iterate formal Fourier angular transport, D=K_HO/E_HO, and an independent finite-difference moment solve. Include both Dxy cross derivatives in shared face fluxes and check local/global discrete budgets.

$$
\boldsymbol\Omega\cdot\nabla I+\sigma_tI=\sigma_sE+q,\quad D=\frac{\langle\boldsymbol\Omega\boldsymbol\Omega^TI\rangle}{\langle I\rangle}
$$

$$
\sigma_t\sigma_aE-\partial_{xx}(D_{xx}E)-2\partial_{xy}(D_{xy}E)-\partial_{yy}(D_{yy}E)=\sigma_tq
$$

$$
K_k=A\left[T\mathbb I+(C-T)\hat k\hat k^T\right],\quad C=\frac{\sigma_t(1-\sigma_tR)}{k^2},\quad T=\frac{R-C}{2}
$$

- [Static grey VEF/VET moment closure](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#static-grey-variable-eddington-moments-en) (`static-grey-variable-eddington-moments`)

Static steady grey unit-periodic square; dimensionless st=4, ss=3, sa=1 and c=1, using point samples. q=1+0.3 cos(2pi x)+0.2 sin(2pi(x+y)). Space is2D, but directions cover full S2 and Dzz is retained.


**Problem figure**

![Variable Eddington tensor: a periodic 2D nonparallel-source control: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/results/vet-fourier-source2d.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Variable Eddington tensor: a periodic 2D nonparallel-source control](https://hrkoyama.github.io/numerical-methods-atlas/problems/vet-fourier-source2d/?lang=en) (`vet-fourier-source2d`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/vet-fourier-source2d/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/vet-fourier-source2d/?lang=en#vet-fourier-source2d-en-validation)

Separate17x17/33x33 refinement at12x48 angles from the16x64 angular probe on33x33. Check analytic E/H/K/D, complex modes including phase, independent angular integration, tensor constraints, cross-term negative controls and a9x9 constant source.

- [Authored continuum Fourier response for periodic 2D VET](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-vet-fourier-source2d-en) (`vet-fourier-source2d`; Same-problem reference · Analytic reference)

The continuum-angle Fourier response to the prescribed positive isotropic source is an analytic reference for this same fixed problem. Keep point/face locations and complex phase distinct, retaining the independent HO/LO discretization gap. Pointwise M1 comparison is a closure diagnostic; no M1 PDE is solved. This is not a reproduction of Athena, short characteristics, shadows, crossing beams, RHD or boundary closures, and does not claim exact fixed-grid HO/LO agreement or universal convergence rates.
## Assumptions, units and boundaries

Static steady grey unit-periodic square; dimensionless st=4, ss=3, sa=1 and c=1, using point samples. q=1+0.3 cos(2pi x)+0.2 sin(2pi(x+y)). Space is2D, but directions cover full S2 and Dzz is retained.

**Editorial clarification**

Pointwise M1 comparison is a closure diagnostic; no M1 PDE is solved. This is not a reproduction of Athena, short characteristics, shadows, crossing beams, RHD or boundary closures, and does not claim exact fixed-grid HO/LO agreement or universal convergence rates.

## Adopted numerical method

Iterate formal Fourier angular transport, D=K_HO/E_HO, and an independent finite-difference moment solve. Include both Dxy cross derivatives in shared face fluxes and check local/global discrete budgets.

$$
\boldsymbol\Omega\cdot\nabla I+\sigma_tI=\sigma_sE+q,\quad D=\frac{\langle\boldsymbol\Omega\boldsymbol\Omega^TI\rangle}{\langle I\rangle}
$$

$$
\sigma_t\sigma_aE-\partial_{xx}(D_{xx}E)-2\partial_{xy}(D_{xy}E)-\partial_{yy}(D_{yy}E)=\sigma_tq
$$

$$
K_k=A\left[T\mathbb I+(C-T)\hat k\hat k^T\right],\quad C=\frac{\sigma_t(1-\sigma_tR)}{k^2},\quad T=\frac{R-C}{2}
$$

## References and validation

Separate17x17/33x33 refinement at12x48 angles from the16x64 angular probe on33x33. Check analytic E/H/K/D, complex modes including phase, independent angular integration, tensor constraints, cross-term negative controls and a9x9 constant source.

## Limits

Pointwise M1 comparison is a closure diagnostic; no M1 PDE is solved. This is not a reproduction of Athena, short characteristics, shadows, crossing beams, RHD or boundary closures, and does not claim exact fixed-grid HO/LO agreement or universal convergence rates.

## Stored measurements and decisions

```json
{
  "metrics": {
    "finest_E_relative_rms_error": 0.00012228131179061114,
    "finest_face_H_relative_rms_error": 0.0010738390026674726,
    "finest_mode_complex_relative_error": 0.0017983436413314031,
    "finest_D_component_max_abs_error": 1.0250275895629102e-05,
    "E_error_refinement_ratio": 0.2655289724016241,
    "face_H_error_refinement_ratio": 0.26613409578253794,
    "HO_LO_gap_refinement_ratio": 0.2657021024383582,
    "angle_probe_E_relative_rms_difference": 2.3900276798110385e-07,
    "angle_probe_D_max_abs_difference": 2.4197709053153105e-07,
    "finest_nonconstant_f_span": 0.022629325122685784,
    "finest_max_abs_Dxy": 0.0052432003949135775,
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

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/vet-fourier-source2d/index.json

![Saved face-flux errors, Dzz, spatial/angular comparisons and iteration residuals. The full3x3 tensor is retained.](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/results/vet-fourier-source2d-diagnostics.png)

Saved face-flux errors, Dzz, spatial/angular comparisons and iteration residuals. The full3x3 tensor is retained.

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

- A Godunov Method for Multidimensional Radiation Magnetohydrodynamics based on a variable Eddington tensor [accessed 2026-11-26]. https://arxiv.org/pdf/1201.2223; review_level=selected-primary-equations-and-test-description
Section3.1 algorithmStep1; Section3.4 PDFp8, equations22–23 and discussion; Section6.5 shadow-test scope description read. Unread limit: Not a reproduction of Athena, mixed-frameRHD, gas coupling, shocks or the paper shadow/cloud-ablation test.

- A Radiation Transfer Solver for Athena using Short Characteristics [accessed 2026-11-26]. https://arxiv.org/pdf/1201.2222; review_level=selected-primary-equations
Equations8–16 source/opacity/moment conventions, Section3.2 angular quadrature Eq17–19 and two-stream warning; Section3.3 Eq20 formal solution and Section3.5 boundary scope read. Unread limit: Proposed Fourier formal solver is not their short-characteristics/interpolation algorithm. No multifrequency, ALI, stellar atmosphere or timing reproduction claim.

- High-Order Mixed Finite Element Variable Eddington Factor Methods [accessed 2026-11-26]. https://arxiv.org/pdf/2301.04758; review_level=selected-primary-equations
Section2, PDFpp3–4: transport Eq1, moment equations Eq2, angular tensor and boundary factor Eq3, fixed-point steps. Introduction on independent spatial discretizations also read. Unread limit: No claim of full59page reading, high-order mixedFEM reproduction, curved-mesh, multigrid or scalability validation.

- A Two-moment Radiation Hydrodynamics Module in Athena Using a Time-explicit Godunov Method [accessed 2026-11-26]. https://arxiv.org/pdf/1306.0010; review_level=selected-primary-equations
Section2.3 PDFp5, equations11–17: localM1 tensor, trace/covariance constraints and chi(reducedflux). Introduction distinction from formalVET also read. Unread limit: No Hyperion/RHD solver or reduced-light-speed/timing validation. InstitutionalPDF endpoint returned401; arXiv original-author copy was read.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
