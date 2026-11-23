# RTの初期成長：滑らかなBoussinesq二層

密度差を浮力だけに残す2D Boussinesq系を時間発展し、不安定な滑らかな層の初期成長を独立線形参照で調べます。

**使用手法**

- [空間中心差分](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=ja) (`centered-difference`)
- [Heun法／SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=ja) (`heun`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/rt-initial-growth/?lang=ja#rt-initial-growth-ja-algorithm)

点値の渦度・浮力摂動を共有面の中央流束とHeun法で進め、5点差分PoissonをFFTで解きます。u=ψy,v=−ψxなので中央差分発散は整合します。基底場を解析的に差し引き、層そのものの離散ドリフトと微小摂動を分離します。

$$
-\Delta\psi=\omega,\qquad (u,v)=(\partial_y\psi,-\partial_x\psi)
$$

$$
b=b_0(y)+\theta,\quad \omega_t+\mathbf{u}\cdot\nabla\omega=\nu\Delta\omega+\theta_x,\quad \theta_t+\mathbf{u}\cdot\nabla\theta+v b_0^{\prime}=\kappa\Delta\theta
$$

$$
\sigma_T=\frac{1}{T}\log\frac{A(T)}{A(0)},\qquad \dot{\widehat{\mathbf{q}}}=L_K\widehat{\mathbf{q}}
$$

- [能動浮力を伴うBoussinesq渦度系](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#boussinesq-buoyancy-ja) (`boussinesq-buoyancy`)

[0,2π]²周期、層厚δ=.25、ν=κ=.005、摂動ε=1e−5。32²/64²/128²格子。基底層は明示した外力で定常維持します。g=1、b0=.02 tanh(sin y/δ)、ρ/ρ0=1−b/g、T=2。慣性密度は一定で、密度跳躍の可変密度Euler系ではありません。


**問題の図**

![RTの初期成長：滑らかなBoussinesq二層：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/results/rt-initial-growth.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[RTの初期成長：滑らかなBoussinesq二層](https://hrkoyama.github.io/numerical-methods-atlas/problems/rt-initial-growth/?lang=ja) (`rt-initial-growth`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/rt-initial-growth/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/rt-initial-growth/?lang=ja#rt-initial-growth-ja-validation)

群全体22単体検査・74固定判定、10回の非線形計算を事前固定。参照K24/40/56、3格子の場誤差と次数、5保存時刻の成長、64²で刻み半減・振幅半減、Poisson残差・発散・平均値を別々に検査します。

- [RT初期成長：Boussinesq二層の線形IVP参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-rt-initial-growth-ja) (`rt-initial-growth`; 同じ問題の参照 · 有限格子の数値参照)

線形範囲の教育用固定入力です。線形参照は独立した空間表現であり、独立非線形PDEエンジンではありません。鋭い無限領域界面の分散式、McNallyの可圧縮入力、非線形後期の巻上がりやRT乱流を再現したとは表示しません。図の摂動はεで規格化した実計算値です。
## 前提・単位・境界

[0,2π]²周期、層厚δ=.25、ν=κ=.005、摂動ε=1e−5。32²/64²/128²格子。基底層は明示した外力で定常維持します。g=1、b0=.02 tanh(sin y/δ)、ρ/ρ0=1−b/g、T=2。慣性密度は一定で、密度跳躍の可変密度Euler系ではありません。

**編集上の補足**

線形範囲の教育用固定入力です。線形参照は独立した空間表現であり、独立非線形PDEエンジンではありません。鋭い無限領域界面の分散式、McNallyの可圧縮入力、非線形後期の巻上がりやRT乱流を再現したとは表示しません。図の摂動はεで規格化した実計算値です。

## 採用した計算法

点値の渦度・浮力摂動を共有面の中央流束とHeun法で進め、5点差分PoissonをFFTで解きます。u=ψy,v=−ψxなので中央差分発散は整合します。基底場を解析的に差し引き、層そのものの離散ドリフトと微小摂動を分離します。

$$
-\Delta\psi=\omega,\qquad (u,v)=(\partial_y\psi,-\partial_x\psi)
$$

$$
b=b_0(y)+\theta,\quad \omega_t+\mathbf{u}\cdot\nabla\omega=\nu\Delta\omega+\theta_x,\quad \theta_t+\mathbf{u}\cdot\nabla\theta+v b_0^{\prime}=\kappa\Delta\theta
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
      1.9961801582972816,
      2.001279583653318
    ],
    "finest_relative_field_error": 0.0006046946397847546,
    "finite_window_growth_rate": 0.005928114552970485,
    "reference_finite_window_growth_rate": 0.005934243782555812,
    "finest_growth_factor": 1.0119267927875564,
    "maximum_growth_curve_error": 1.2258384036050356e-05,
    "time_contamination_fraction": 0.0026807715949025237,
    "amplitude_scaled_difference": 6.607861425190432e-06,
    "linear_operator_maximum_real_eigenvalue": 0.11294010706315265
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

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/rt-initial-growth/index.json

![保存した2D浮力摂動をεで規格化。滑らかな二層の初期変位で、乱流混合の図ではありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/results/rt-initial-growth-preview.png)

保存した2D浮力摂動をεで規格化。滑らかな二層の初期変位で、乱流混合の図ではありません。

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

このコマンドは配布グループの全例を実行します。

## 出典と確認範囲

- Antonio Celani, Andrea Mazzino and Lara Vozella (2006). Rayleigh–Taylor turbulence in two dimensions. https://arxiv.org/abs/nlin/0510067; review_level=primary-selected-original-pdf-text
  原著のBoussinesq方程式と周期設定を確認。本例の滑らかな定常維持二層と線形参照は独自です。

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# RT initial growth in smooth Boussinesq double layers

Advance the actual2D Boussinesq vorticity/active-buoyancy system and compare smooth unstable-layer growth with a separately derived linear IVP.

**Methods used**

- [Centered spatial difference](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en) (`centered-difference`)
- [Heun / SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en) (`heun`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/rt-initial-growth/?lang=en#rt-initial-growth-en-algorithm)

Advance point-sampled perturbations using centered shared-face conservative fluxes and Heun; invert the five-point Poisson symbol by FFT. Centered derivatives define divergence-free velocity. Analytic base subtraction avoids a discretization imbalance larger than the small perturbation.

$$
-\Delta\psi=\omega,\qquad (u,v)=(\partial_y\psi,-\partial_x\psi)
$$

$$
b=b_0(y)+\theta,\quad \omega_t+\mathbf{u}\cdot\nabla\omega=\nu\Delta\omega+\theta_x,\quad \theta_t+\mathbf{u}\cdot\nabla\theta+v b_0^{\prime}=\kappa\Delta\theta
$$

$$
\sigma_T=\frac{1}{T}\log\frac{A(T)}{A(0)},\qquad \dot{\widehat{\mathbf{q}}}=L_K\widehat{\mathbf{q}}
$$

- [Boussinesq vorticity with active buoyancy](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#boussinesq-buoyancy-en) (`boussinesq-buoyancy`)

Periodic[0,2pi]², layer width.25, nu=kappa=.005, epsilon1e-5 and32²/64²/128² grids. Explicit forcing maintains the base. g1,b0=.02tanh(sin y/delta),rho/rho0=1-b/g,T2. Density enters buoyancy only; this is not variable-density Euler.


**Problem figure**

![RT initial growth in smooth Boussinesq double layers: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/results/rt-initial-growth.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[RT initial growth in smooth Boussinesq double layers](https://hrkoyama.github.io/numerical-methods-atlas/problems/rt-initial-growth/?lang=en) (`rt-initial-growth`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/rt-initial-growth/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/rt-initial-growth/?lang=en#rt-initial-growth-en-validation)

Freeze22pytest tests,74case gates and10nonlinear evolutions. QualifyK24/40/56references; separately check three-grid field errors/orders, five-time growth,64²halved-step/halved-amplitude probes, Poisson residual, divergence and means.

- [RT initial growth: linear Boussinesq double-layer IVP reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-rt-initial-growth-en) (`rt-initial-growth`; Same-problem reference · Finite-grid numerical reference)

Small-amplitude fixed educational cases. The independent reference changes spatial representation but linearizes the PDE; it is not a second nonlinear engine. No sharp-interface infinite-domain dispersion, original compressible McNally inputs, late roll-up or RT turbulence claim. Figures explicitly normalize computed perturbations by epsilon.
## Assumptions, units and boundaries

Periodic[0,2pi]², layer width.25, nu=kappa=.005, epsilon1e-5 and32²/64²/128² grids. Explicit forcing maintains the base. g1,b0=.02tanh(sin y/delta),rho/rho0=1-b/g,T2. Density enters buoyancy only; this is not variable-density Euler.

**Editorial clarification**

Small-amplitude fixed educational cases. The independent reference changes spatial representation but linearizes the PDE; it is not a second nonlinear engine. No sharp-interface infinite-domain dispersion, original compressible McNally inputs, late roll-up or RT turbulence claim. Figures explicitly normalize computed perturbations by epsilon.

## Adopted numerical method

Advance point-sampled perturbations using centered shared-face conservative fluxes and Heun; invert the five-point Poisson symbol by FFT. Centered derivatives define divergence-free velocity. Analytic base subtraction avoids a discretization imbalance larger than the small perturbation.

$$
-\Delta\psi=\omega,\qquad (u,v)=(\partial_y\psi,-\partial_x\psi)
$$

$$
b=b_0(y)+\theta,\quad \omega_t+\mathbf{u}\cdot\nabla\omega=\nu\Delta\omega+\theta_x,\quad \theta_t+\mathbf{u}\cdot\nabla\theta+v b_0^{\prime}=\kappa\Delta\theta
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
      1.9961801582972816,
      2.001279583653318
    ],
    "finest_relative_field_error": 0.0006046946397847546,
    "finite_window_growth_rate": 0.005928114552970485,
    "reference_finite_window_growth_rate": 0.005934243782555812,
    "finest_growth_factor": 1.0119267927875564,
    "maximum_growth_curve_error": 1.2258384036050356e-05,
    "time_contamination_fraction": 0.0026807715949025237,
    "amplitude_scaled_difference": 6.607861425190432e-06,
    "linear_operator_maximum_real_eigenvalue": 0.11294010706315265
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

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/rt-initial-growth/index.json

![Saved actual2D buoyancy perturbation normalized by epsilon; an early smooth-layer displacement, not turbulent mixing.](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/results/rt-initial-growth-preview.png)

Saved actual2D buoyancy perturbation normalized by epsilon; an early smooth-layer displacement, not turbulent mixing.

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

This command executes every fixed case in the distribution group.

## Sources and review scope

- Antonio Celani, Andrea Mazzino and Lara Vozella (2006). Rayleigh–Taylor turbulence in two dimensions. https://arxiv.org/abs/nlin/0510067; review_level=primary-selected-original-pdf-text
  Original Boussinesq equations and periodic setup read; our smooth maintained layers and linear reference are constructed here.

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
