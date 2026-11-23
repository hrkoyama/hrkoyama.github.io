# KHの初期成長：滑らかな周期せん断層

実際の非線形2D渦度方程式を解き、独立Fourier–Galerkin線形初期値問題と有限時間の成長・格子誤差を比較します。

**使用手法**

- [空間中心差分](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=ja) (`centered-difference`)
- [Heun法／SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=ja) (`heun`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/kh-initial-growth/?lang=ja#kh-initial-growth-ja-algorithm)

点値の渦度・浮力摂動を共有面の中央流束とHeun法で進め、5点差分PoissonをFFTで解きます。u=ψy,v=−ψxなので中央差分発散は整合します。基底場を解析的に差し引き、層そのものの離散ドリフトと微小摂動を分離します。

$$
-\Delta\psi=\omega,\qquad (u,v)=(\partial_y\psi,-\partial_x\psi)
$$

$$
U(y)=\tanh(\sin y/\delta),\quad \omega_t+U\omega_x+U^{\prime\prime}\psi_x+\mathbf{u}\cdot\nabla\omega=\nu\Delta\omega
$$

$$
\sigma_T=\frac{1}{T}\log\frac{A(T)}{A(0)},\qquad \dot{\widehat{\mathbf{q}}}=L_K\widehat{\mathbf{q}}
$$

- [維持されたせん断層の強制渦度系](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#forced-vorticity-ja) (`forced-vorticity`)

[0,2π]²周期、層厚δ=.25、ν=κ=.005、摂動ε=1e−5。32²/64²/128²格子。基底層は明示した外力で定常維持します。U=tanh(sin y/δ)、T=1。


**問題の図**

![KHの初期成長：滑らかな周期せん断層：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/results/kh-initial-growth.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[KHの初期成長：滑らかな周期せん断層](https://hrkoyama.github.io/numerical-methods-atlas/problems/kh-initial-growth/?lang=ja) (`kh-initial-growth`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/kh-initial-growth/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/kh-initial-growth/?lang=ja#kh-initial-growth-ja-validation)

群全体22単体検査・74固定判定、10回の非線形計算を事前固定。参照K24/40/56、3格子の場誤差と次数、5保存時刻の成長、64²で刻み半減・振幅半減、Poisson残差・発散・平均値を別々に検査します。

- [KH初期成長：独立した線形Fourier–Galerkin参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-kh-initial-growth-ja) (`kh-initial-growth`; 同じ問題の参照 · 有限格子の数値参照)

線形範囲の教育用固定入力です。線形参照は独立した空間表現であり、独立非線形PDEエンジンではありません。鋭い無限領域界面の分散式、McNallyの可圧縮入力、非線形後期の巻上がりやRT乱流を再現したとは表示しません。図の摂動はεで規格化した実計算値です。
## 前提・単位・境界

[0,2π]²周期、層厚δ=.25、ν=κ=.005、摂動ε=1e−5。32²/64²/128²格子。基底層は明示した外力で定常維持します。U=tanh(sin y/δ)、T=1。

**編集上の補足**

線形範囲の教育用固定入力です。線形参照は独立した空間表現であり、独立非線形PDEエンジンではありません。鋭い無限領域界面の分散式、McNallyの可圧縮入力、非線形後期の巻上がりやRT乱流を再現したとは表示しません。図の摂動はεで規格化した実計算値です。

## 採用した計算法

点値の渦度・浮力摂動を共有面の中央流束とHeun法で進め、5点差分PoissonをFFTで解きます。u=ψy,v=−ψxなので中央差分発散は整合します。基底場を解析的に差し引き、層そのものの離散ドリフトと微小摂動を分離します。

$$
-\Delta\psi=\omega,\qquad (u,v)=(\partial_y\psi,-\partial_x\psi)
$$

$$
U(y)=\tanh(\sin y/\delta),\quad \omega_t+U\omega_x+U^{\prime\prime}\psi_x+\mathbf{u}\cdot\nabla\omega=\nu\Delta\omega
$$

$$
\sigma_T=\frac{1}{T}\log\frac{A(T)}{A(0)},\qquad \dot{\widehat{\mathbf{q}}}=L_K\widehat{\mathbf{q}}
$$

## 比較・検証

群全体22単体検査・74固定判定、10回の非線形計算を事前固定。参照K24/40/56、3格子の場誤差と次数、5保存時刻の成長、64²で刻み半減・振幅半減、Poisson残差・発散・平均値を別々に検査します。

## 確認の限界

線形範囲の教育用固定入力です。線形参照は独立した空間表現であり、独立非線形PDEエンジンではありません。鋭い無限領域界面の分散式、McNallyの可圧縮入力、非線形後期の巻上がりやRT乱流を再現したとは表示しません。図の摂動はεで規格化した実計算値です。

## 保存実測値と判定

```json
{
  "metrics": {
    "spatial_orders": [
      2.2589498509059927,
      2.031111897437912
    ],
    "finest_relative_field_error": 0.00425645160443949,
    "finite_window_growth_rate": 0.39492545403491336,
    "reference_finite_window_growth_rate": 0.3978101440217111,
    "finest_growth_factor": 1.4842735401931764,
    "maximum_growth_curve_error": 0.0028805332665482204,
    "time_contamination_fraction": 0.00045118656465393327,
    "amplitude_scaled_difference": 6.588689979924076e-06,
    "linear_operator_maximum_real_eigenvalue": 0.5858641640461411
  },
  "checks": {
    "reference_state_sensitivity": true,
    "reference_growth_sensitivity": true,
    "reference_positive_eigen_growth": true,
    "n32_finite": true,
    "n32_divergence": true,
    "n32_poisson": true,
    "n32_mean_omega": true,
    "n32_mean_theta": true,
    "n64_finite": true,
    "n64_divergence": true,
    "n64_poisson": true,
    "n64_mean_omega": true,
    "n64_mean_theta": true,
    "n128_finite": true,
    "n128_divergence": true,
    "n128_poisson": true,
    "n128_mean_omega": true,
    "n128_mean_theta": true,
    "time-half_finite": true,
    "time-half_divergence": true,
    "time-half_poisson": true,
    "time-half_mean_omega": true,
    "time-half_mean_theta": true,
    "epsilon-half_finite": true,
    "epsilon-half_divergence": true,
    "epsilon-half_poisson": true,
    "epsilon-half_mean_omega": true,
    "epsilon-half_mean_theta": true,
    "spatial_decrease_1": true,
    "spatial_decrease_2": true,
    "minimum_spatial_order": true,
    "finest_field_error": true,
    "growth_curve": true,
    "finite_window_growth_rate": true,
    "observable_growth": true,
    "time_contamination": true,
    "amplitude_linearity": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/kh-initial-growth/index.json

![保存した2D摂動渦度をεで規格化。色の尺度を明記し、線形参照と成長を比較します。](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/results/kh-initial-growth-preview.png)

保存した2D摂動渦度をεで規格化。色の尺度を明記し、線形参照と成長を比較します。

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/atlas-instability-growth-2026-11-23-r2.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

## 出典と確認範囲

- Colin P. McNally, Wladimir Lyra and Jean-Claude Passy (2012). A Well-Posed Kelvin-Helmholtz Instability Test and Comparison. https://arxiv.org/abs/1111.1764; review_level=primary-selected-original-pdf-text
原著の滑らかな層・有限領域・成長測定の議論を確認。本例は独自の強制非圧縮系です。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# KH initial growth in a smooth periodic shear layer

Evolve the actual nonlinear2D vorticity PDE and compare finite-time growth and spatial errors with an independent continuous Fourier–Galerkin linear IVP.

**Methods used**

- [Centered spatial difference](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en) (`centered-difference`)
- [Heun / SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en) (`heun`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/kh-initial-growth/?lang=en#kh-initial-growth-en-algorithm)

Advance point-sampled perturbations using centered shared-face conservative fluxes and Heun; invert the five-point Poisson symbol by FFT. Centered derivatives define divergence-free velocity. Analytic base subtraction avoids a discretization imbalance larger than the small perturbation.

$$
-\Delta\psi=\omega,\qquad (u,v)=(\partial_y\psi,-\partial_x\psi)
$$

$$
U(y)=\tanh(\sin y/\delta),\quad \omega_t+U\omega_x+U^{\prime\prime}\psi_x+\mathbf{u}\cdot\nabla\omega=\nu\Delta\omega
$$

$$
\sigma_T=\frac{1}{T}\log\frac{A(T)}{A(0)},\qquad \dot{\widehat{\mathbf{q}}}=L_K\widehat{\mathbf{q}}
$$

- [Forced vorticity about a maintained shear layer](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#forced-vorticity-en) (`forced-vorticity`)

Periodic[0,2pi]², layer width.25, nu=kappa=.005, epsilon1e-5 and32²/64²/128² grids. Explicit forcing maintains the base. U=tanh(sin y/delta),T1.


**Problem figure**

![KH initial growth in a smooth periodic shear layer: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/results/kh-initial-growth.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[KH initial growth in a smooth periodic shear layer](https://hrkoyama.github.io/numerical-methods-atlas/problems/kh-initial-growth/?lang=en) (`kh-initial-growth`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/kh-initial-growth/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/kh-initial-growth/?lang=en#kh-initial-growth-en-validation)

Freeze22pytest tests,74case gates and10nonlinear evolutions. QualifyK24/40/56references; separately check three-grid field errors/orders, five-time growth,64²halved-step/halved-amplitude probes, Poisson residual, divergence and means.

- [KH initial growth: independent linear Fourier-Galerkin reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-kh-initial-growth-en) (`kh-initial-growth`; Same-problem reference · Finite-grid numerical reference)

Small-amplitude fixed educational cases. The independent reference changes spatial representation but linearizes the PDE; it is not a second nonlinear engine. No sharp-interface infinite-domain dispersion, original compressible McNally inputs, late roll-up or RT turbulence claim. Figures explicitly normalize computed perturbations by epsilon.
## Assumptions, units and boundaries

Periodic[0,2pi]², layer width.25, nu=kappa=.005, epsilon1e-5 and32²/64²/128² grids. Explicit forcing maintains the base. U=tanh(sin y/delta),T1.

**Editorial clarification**

Small-amplitude fixed educational cases. The independent reference changes spatial representation but linearizes the PDE; it is not a second nonlinear engine. No sharp-interface infinite-domain dispersion, original compressible McNally inputs, late roll-up or RT turbulence claim. Figures explicitly normalize computed perturbations by epsilon.

## Adopted numerical method

Advance point-sampled perturbations using centered shared-face conservative fluxes and Heun; invert the five-point Poisson symbol by FFT. Centered derivatives define divergence-free velocity. Analytic base subtraction avoids a discretization imbalance larger than the small perturbation.

$$
-\Delta\psi=\omega,\qquad (u,v)=(\partial_y\psi,-\partial_x\psi)
$$

$$
U(y)=\tanh(\sin y/\delta),\quad \omega_t+U\omega_x+U^{\prime\prime}\psi_x+\mathbf{u}\cdot\nabla\omega=\nu\Delta\omega
$$

$$
\sigma_T=\frac{1}{T}\log\frac{A(T)}{A(0)},\qquad \dot{\widehat{\mathbf{q}}}=L_K\widehat{\mathbf{q}}
$$

## References and validation

Freeze22pytest tests,74case gates and10nonlinear evolutions. QualifyK24/40/56references; separately check three-grid field errors/orders, five-time growth,64²halved-step/halved-amplitude probes, Poisson residual, divergence and means.

## Limits

Small-amplitude fixed educational cases. The independent reference changes spatial representation but linearizes the PDE; it is not a second nonlinear engine. No sharp-interface infinite-domain dispersion, original compressible McNally inputs, late roll-up or RT turbulence claim. Figures explicitly normalize computed perturbations by epsilon.

## Stored measurements and decisions

```json
{
  "metrics": {
    "spatial_orders": [
      2.2589498509059927,
      2.031111897437912
    ],
    "finest_relative_field_error": 0.00425645160443949,
    "finite_window_growth_rate": 0.39492545403491336,
    "reference_finite_window_growth_rate": 0.3978101440217111,
    "finest_growth_factor": 1.4842735401931764,
    "maximum_growth_curve_error": 0.0028805332665482204,
    "time_contamination_fraction": 0.00045118656465393327,
    "amplitude_scaled_difference": 6.588689979924076e-06,
    "linear_operator_maximum_real_eigenvalue": 0.5858641640461411
  },
  "checks": {
    "reference_state_sensitivity": true,
    "reference_growth_sensitivity": true,
    "reference_positive_eigen_growth": true,
    "n32_finite": true,
    "n32_divergence": true,
    "n32_poisson": true,
    "n32_mean_omega": true,
    "n32_mean_theta": true,
    "n64_finite": true,
    "n64_divergence": true,
    "n64_poisson": true,
    "n64_mean_omega": true,
    "n64_mean_theta": true,
    "n128_finite": true,
    "n128_divergence": true,
    "n128_poisson": true,
    "n128_mean_omega": true,
    "n128_mean_theta": true,
    "time-half_finite": true,
    "time-half_divergence": true,
    "time-half_poisson": true,
    "time-half_mean_omega": true,
    "time-half_mean_theta": true,
    "epsilon-half_finite": true,
    "epsilon-half_divergence": true,
    "epsilon-half_poisson": true,
    "epsilon-half_mean_omega": true,
    "epsilon-half_mean_theta": true,
    "spatial_decrease_1": true,
    "spatial_decrease_2": true,
    "minimum_spatial_order": true,
    "finest_field_error": true,
    "growth_curve": true,
    "finite_window_growth_rate": true,
    "observable_growth": true,
    "time_contamination": true,
    "amplitude_linearity": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/kh-initial-growth/index.json

![Saved actual2D perturbation vorticity normalized by epsilon; color scale and linear-reference growth are explicit.](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/results/kh-initial-growth-preview.png)

Saved actual2D perturbation vorticity normalized by epsilon; color scale and linear-reference growth are explicit.

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/atlas-instability-growth-2026-11-23-r2.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

## Sources and review scope

- Colin P. McNally, Wladimir Lyra and Jean-Claude Passy (2012). A Well-Posed Kelvin-Helmholtz Instability Test and Comparison. https://arxiv.org/abs/1111.1764; review_level=primary-selected-original-pdf-text
Selected original methodology read; our incompressible forced inputs differ from its compressible benchmark.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
