# KH・RTの初期成長と独立線形参照

小振幅の非線形2D計算を、別に導出した連続Fourier–Galerkin線形初期値問題と比較します。有限時間の成長、格子・時間・振幅の影響を分けます。

共通22実行例の台帳とは別に管理する追加検証集です。配布ZIPを独立展開し、各グループの全固定入力と検査を実行した記録を示します。設定・手法・刻み幅の違いを独立した物理問題の数には加算しません。

## KHの初期成長：滑らかな周期せん断層

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
### 前提・単位・境界

[0,2π]²周期、層厚δ=.25、ν=κ=.005、摂動ε=1e−5。32²/64²/128²格子。基底層は明示した外力で定常維持します。U=tanh(sin y/δ)、T=1。

**編集上の補足**

線形範囲の教育用固定入力です。線形参照は独立した空間表現であり、独立非線形PDEエンジンではありません。鋭い無限領域界面の分散式、McNallyの可圧縮入力、非線形後期の巻上がりやRT乱流を再現したとは表示しません。図の摂動はεで規格化した実計算値です。

### 採用した計算法

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

### 比較・検証

群全体22単体検査・74固定判定、10回の非線形計算を事前固定。参照K24/40/56、3格子の場誤差と次数、5保存時刻の成長、64²で刻み半減・振幅半減、Poisson残差・発散・平均値を別々に検査します。

### 確認の限界

線形範囲の教育用固定入力です。線形参照は独立した空間表現であり、独立非線形PDEエンジンではありません。鋭い無限領域界面の分散式、McNallyの可圧縮入力、非線形後期の巻上がりやRT乱流を再現したとは表示しません。図の摂動はεで規格化した実計算値です。

### 保存実測値と判定

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

### 取得・実行

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

### 出典と確認範囲

- Colin P. McNally, Wladimir Lyra and Jean-Claude Passy (2012). A Well-Posed Kelvin-Helmholtz Instability Test and Comparison. https://arxiv.org/abs/1111.1764; review_level=primary-selected-original-pdf-text
原著の滑らかな層・有限領域・成長測定の議論を確認。本例は独自の強制非圧縮系です。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## RTの初期成長：滑らかなBoussinesq二層

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
### 前提・単位・境界

[0,2π]²周期、層厚δ=.25、ν=κ=.005、摂動ε=1e−5。32²/64²/128²格子。基底層は明示した外力で定常維持します。g=1、b0=.02 tanh(sin y/δ)、ρ/ρ0=1−b/g、T=2。慣性密度は一定で、密度跳躍の可変密度Euler系ではありません。

**編集上の補足**

線形範囲の教育用固定入力です。線形参照は独立した空間表現であり、独立非線形PDEエンジンではありません。鋭い無限領域界面の分散式、McNallyの可圧縮入力、非線形後期の巻上がりやRT乱流を再現したとは表示しません。図の摂動はεで規格化した実計算値です。

### 採用した計算法

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

### 比較・検証

群全体22単体検査・74固定判定、10回の非線形計算を事前固定。参照K24/40/56、3格子の場誤差と次数、5保存時刻の成長、64²で刻み半減・振幅半減、Poisson残差・発散・平均値を別々に検査します。

### 確認の限界

線形範囲の教育用固定入力です。線形参照は独立した空間表現であり、独立非線形PDEエンジンではありません。鋭い無限領域界面の分散式、McNallyの可圧縮入力、非線形後期の巻上がりやRT乱流を再現したとは表示しません。図の摂動はεで規格化した実計算値です。

### 保存実測値と判定

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

### 取得・実行

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

### 出典と確認範囲

- Antonio Celani, Andrea Mazzino and Lara Vozella (2006). Rayleigh–Taylor turbulence in two dimensions. https://arxiv.org/abs/nlin/0510067; review_level=primary-selected-original-pdf-text
原著のBoussinesq方程式と周期設定を確認。本例の滑らかな定常維持二層と線形参照は独自です。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
