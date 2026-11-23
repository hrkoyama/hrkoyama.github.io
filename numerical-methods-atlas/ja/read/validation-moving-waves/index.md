# 非一様ALE輸送・2次元回転浅水波

非一様に動くセルの保存的ALE輸送とGCL、および2次元C格子の線形回転浅水波を時間発展させます。SaltzmanピストンとWilliamson球面問題は次段階の未実装項目です。

共通22実行例の台帳とは別に管理する追加検証集です。配布ZIPを独立展開し、各グループの全固定入力と検査を実行した記録を示します。設定・手法・刻み幅の違いを独立した物理問題の数には加算しません。

## 非一様移動格子で実際に運ぶALEスカラー

質量と格子面位置を同じHeun段で更新し、一様GCLだけでなく非一様な解析波を運びます。

**使用手法**

- [ALE一様状態・幾何保存モデル](https://hrkoyama.github.io/numerical-methods-atlas/methods/ale/?lang=ja) (`ale`)
- [風上差分（upwind）](https://hrkoyama.github.io/numerical-methods-atlas/methods/upwind/?lang=ja) (`upwind`)
- [Heun法／SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=ja) (`heun`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/ale-nonuniform-transport/?lang=ja#ale-nonuniform-transport-ja-algorithm)

実セル質量の上流相対流束(a−w)qと実面位置を同じHeun predictor/correctorで進め、各段体積・面Courant数を記録。

$$
\dot m_i=-[(a-w)q]_{i+1/2}+[(a-w)q]_{i-1/2},\quad V_i=x_{i+1/2}-x_{i-1/2}
$$

$$
x(\xi,t)=\xi+0.2\sin(2\pi\xi)\sin(2\pi t)/(2\pi)
$$

- [移動セル上のALEスカラー保存式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#ale-scalar-transport-ja) (`ale-scalar-transport`)

周期[0,1]、速度.7、q0=1+.2sin(2pi x)、面速度w=.2sin(2pi xi)cos(2pi t)、N40/80/160、T1。時間比較N40,T.25,32/64/128step。


**問題の図**

![非一様移動格子で実際に運ぶALEスカラー：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/results/ale-nonuniform-transport.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[非一様移動格子で実際に運ぶALEスカラー](https://hrkoyama.github.io/numerical-methods-atlas/problems/ale-nonuniform-transport/?lang=ja) (`ale-nonuniform-transport`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/ale-nonuniform-transport/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/ale-nonuniform-transport/?lang=ja#ale-nonuniform-transport-ja-validation)

解析的移動セル積分、全体/段の質量、GCLconstant、格子幾何誤差を分離。独立DOP853による同じFV ODEの時間参照を二公差で確認。

- [ALE：実際の移動セル上の解析積分と時間参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-ale-nonuniform-transport-ja) (`ale-nonuniform-transport`; 同じ問題の参照 · 解析参照)

1D指定格子運動の第一段階です。図のx–tは2D物理計算ではなく、Euler Lagrange/remapやSaltzmanピストンは未実装の後続課題。
### 前提・単位・境界

周期[0,1]、速度.7、q0=1+.2sin(2pi x)、面速度w=.2sin(2pi xi)cos(2pi t)、N40/80/160、T1。時間比較N40,T.25,32/64/128step。

**編集上の補足**

1D指定格子運動の第一段階です。図のx–tは2D物理計算ではなく、Euler Lagrange/remapやSaltzmanピストンは未実装の後続課題。

### 採用した計算法

実セル質量の上流相対流束(a−w)qと実面位置を同じHeun predictor/correctorで進め、各段体積・面Courant数を記録。

$$
\dot m_i=-[(a-w)q]_{i+1/2}+[(a-w)q]_{i-1/2},\quad V_i=x_{i+1/2}-x_{i-1/2}
$$

$$
x(\xi,t)=\xi+0.2\sin(2\pi\xi)\sin(2\pi t)/(2\pi)
$$

### 比較・検証

解析的移動セル積分、全体/段の質量、GCLconstant、格子幾何誤差を分離。独立DOP853による同じFV ODEの時間参照を二公差で確認。

### 確認の限界

1D指定格子運動の第一段階です。図のx–tは2D物理計算ではなく、Euler Lagrange/remapやSaltzmanピストンは未実装の後続課題。

### 保存実測値と判定

```json
{
  "metrics": {
    "n": 40,
    "steps": 128,
    "time": 0.25,
    "error": 0.01079017856620466,
    "minimum_volume": 0.02002059881546564,
    "minimum_value": 0.8008335429751757,
    "maximum_cfl": 0.07049500497645084,
    "mass_defect": 0.0,
    "step_mass_defect": 2.220446049250313e-16,
    "gcl_defect": 1.9786689647860456e-16,
    "geometry_error": 3.9947516627947266e-07,
    "temporal_error": 2.0565741803957238e-07
  },
  "checks": {
    "adaptive-time reference qualification": true,
    "space-n40 mass_defect": true,
    "space-n40 step_mass_defect": true,
    "space-n40 gcl_defect": true,
    "space-n40 maximum_cfl": true,
    "space-n40 positive volumes and values": true,
    "space-n40 five saved times": true,
    "space-n80 mass_defect": true,
    "space-n80 step_mass_defect": true,
    "space-n80 gcl_defect": true,
    "space-n80 maximum_cfl": true,
    "space-n80 positive volumes and values": true,
    "space-n80 five saved times": true,
    "space-n160 mass_defect": true,
    "space-n160 step_mass_defect": true,
    "space-n160 gcl_defect": true,
    "space-n160 maximum_cfl": true,
    "space-n160 positive volumes and values": true,
    "space-n160 five saved times": true,
    "gcl-n40 mass_defect": true,
    "gcl-n40 step_mass_defect": true,
    "gcl-n40 gcl_defect": true,
    "gcl-n40 maximum_cfl": true,
    "gcl-n40 positive volumes and values": true,
    "gcl-n40 five saved times": true,
    "time-n40-s32 mass_defect": true,
    "time-n40-s32 step_mass_defect": true,
    "time-n40-s32 gcl_defect": true,
    "time-n40-s32 maximum_cfl": true,
    "time-n40-s32 positive volumes and values": true,
    "time-n40-s32 five saved times": true,
    "time-n40-s64 mass_defect": true,
    "time-n40-s64 step_mass_defect": true,
    "time-n40-s64 gcl_defect": true,
    "time-n40-s64 maximum_cfl": true,
    "time-n40-s64 positive volumes and values": true,
    "time-n40-s64 five saved times": true,
    "time-n40-s128 mass_defect": true,
    "time-n40-s128 step_mass_defect": true,
    "time-n40-s128 gcl_defect": true,
    "time-n40-s128 maximum_cfl": true,
    "time-n40-s128 positive volumes and values": true,
    "time-n40-s128 five saved times": true,
    "space refinement 1": true,
    "space refinement 2": true,
    "time refinement 1": true,
    "time refinement 2": true,
    "finest transport error": true,
    "constant-state GCL preservation": true,
    "finest time error": true,
    "reference analytic moving-face velocity": true,
    "reference periodic analytic mass": true,
    "reference skew-Hermitian discrete symbol": true,
    "reference continuous wave frequency": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/ale-nonuniform-transport/index.json

![実際に保存した計算配列と固定入力の収束指標から描いた検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/results/ale-nonuniform-transport-preview.png)

実際に保存した計算配列と固定入力の収束指標から描いた検証図。

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/atlas-moving-waves-2026-11-23.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

### 出典と確認範囲

- Dennis L. Huff (1987). Numerical Simulations of Unsteady, Viscous, Transonic Flow Over Isolated and Cascaded Airfoils Using a Deforming Grid. https://ntrs.nasa.gov/api/citations/19870015002/downloads/19870015002.pdf; review_level=selected-primary-report-grid-treatment
NASA TM89890 grid-velocity and GCL discussion around equation11/printedp5 inspected. It attributes GCL to Thomas/Lombard. Original1979 paper not read; no airfoil algorithm or code reproduced. Our 1D scalar moving-volume/Heun derivation is independent.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## 2D C-grid回転浅水波の実時間発展

実際の2D staggered場を時間積分し、連続波と離散symbolの参照を分けて比較します。

**使用手法**

- [空間中心差分](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=ja) (`centered-difference`)
- [古典的RK4](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=ja) (`rk4`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/cgrid-rotating-wave/?lang=ja#cgrid-rotating-wave-ja-algorithm)

セルeta・法線face u/vの差分と4点Coriolis補間を2Dで評価しRK4更新。3×3行列指数は参照だけで、PDE場の更新には使いません。

$$
\eta_t+u_x+v_y=0,\quad u_t=v-\eta_x,\quad v_t=-u-\eta_y
$$

$$
\tilde k=2\sin(kh/2)/h,\quad C=\cos(kh/2)\cos(lh/2),\quad U_h(t)=e^{tL_h}U_h(0)
$$

- [線形回転浅水方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#linear-rotating-shallow-water-ja) (`linear-rotating-shallow-water`)

線形f-plane、g=H=f=1、周期単位正方形、(k,l)=(1,2)、eta振幅.01、N16/32/64,T.5。別の固定N16時間系列、zero-modeと離散geostrophic診断。


**問題の図**

![2D C-grid回転浅水波の実時間発展：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/results/cgrid-rotating-wave.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[2D C-grid回転浅水波の実時間発展](https://hrkoyama.github.io/numerical-methods-atlas/problems/cgrid-rotating-wave/?lang=ja) (`cgrid-rotating-wave`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/cgrid-rotating-wave/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/cgrid-rotating-wave/?lang=ja#cgrid-rotating-wave-ja-validation)

連続PDE空間誤差と離散symbol時間誤差、mass/energy、stencil-symbol一致、zero-mode慣性振動と離散定常釣合いを保存。

- [C-grid：連続Fourier解と離散記号の行列指数](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-cgrid-rotating-wave-ja) (`cgrid-rotating-wave`; 同じ問題の参照 · 解析参照)

線形・平面・周期squareの限定例。非線形浅水、PV・球面格子・全球dynamical coreやWilliamsonは未実装の後続課題。
### 前提・単位・境界

線形f-plane、g=H=f=1、周期単位正方形、(k,l)=(1,2)、eta振幅.01、N16/32/64,T.5。別の固定N16時間系列、zero-modeと離散geostrophic診断。

**編集上の補足**

線形・平面・周期squareの限定例。非線形浅水、PV・球面格子・全球dynamical coreやWilliamsonは未実装の後続課題。

### 採用した計算法

セルeta・法線face u/vの差分と4点Coriolis補間を2Dで評価しRK4更新。3×3行列指数は参照だけで、PDE場の更新には使いません。

$$
\eta_t+u_x+v_y=0,\quad u_t=v-\eta_x,\quad v_t=-u-\eta_y
$$

$$
\tilde k=2\sin(kh/2)/h,\quad C=\cos(kh/2)\cos(lh/2),\quad U_h(t)=e^{tL_h}U_h(0)
$$

### 比較・検証

連続PDE空間誤差と離散symbol時間誤差、mass/energy、stencil-symbol一致、zero-mode慣性振動と離散定常釣合いを保存。

### 確認の限界

線形・平面・周期squareの限定例。非線形浅水、PV・球面格子・全球dynamical coreやWilliamsonは未実装の後続課題。

### 保存実測値と判定

```json
{
  "metrics": {
    "n": 16,
    "steps": 64,
    "time": 0.5,
    "semidiscrete_error": 6.989513057798398e-16,
    "continuous_error": 0.0069533426306616995,
    "mean_height_change": 1.2705494208814505e-20,
    "relative_energy_change": 2.220446049250313e-16,
    "energy_rhs_defect": 2.1352767681718556e-19,
    "steady_change": 1.8041124150158794e-16
  },
  "checks": {
    "space-n16-s64 mean_height_change": true,
    "space-n16-s64 relative_energy_change": true,
    "space-n16-s64 energy_rhs_defect": true,
    "space-n16-s64 finite actual 2D RK arrays": true,
    "space-n32-s128 mean_height_change": true,
    "space-n32-s128 relative_energy_change": true,
    "space-n32-s128 energy_rhs_defect": true,
    "space-n32-s128 finite actual 2D RK arrays": true,
    "space-n64-s256 mean_height_change": true,
    "space-n64-s256 relative_energy_change": true,
    "space-n64-s256 energy_rhs_defect": true,
    "space-n64-s256 finite actual 2D RK arrays": true,
    "time-n16-s16 mean_height_change": true,
    "time-n16-s16 relative_energy_change": true,
    "time-n16-s16 energy_rhs_defect": true,
    "time-n16-s16 finite actual 2D RK arrays": true,
    "time-n16-s32 mean_height_change": true,
    "time-n16-s32 relative_energy_change": true,
    "time-n16-s32 energy_rhs_defect": true,
    "time-n16-s32 finite actual 2D RK arrays": true,
    "time-n16-s64 mean_height_change": true,
    "time-n16-s64 relative_energy_change": true,
    "time-n16-s64 energy_rhs_defect": true,
    "time-n16-s64 finite actual 2D RK arrays": true,
    "zero-n8-s64 mean_height_change": true,
    "zero-n8-s64 relative_energy_change": true,
    "zero-n8-s64 energy_rhs_defect": true,
    "zero-n8-s64 finite actual 2D RK arrays": true,
    "balance-n16-s64 mean_height_change": true,
    "balance-n16-s64 relative_energy_change": true,
    "balance-n16-s64 energy_rhs_defect": true,
    "balance-n16-s64 finite actual 2D RK arrays": true,
    "continuous spatial refinement 1": true,
    "continuous spatial refinement 2": true,
    "semidiscrete temporal refinement 1": true,
    "semidiscrete temporal refinement 2": true,
    "finest continuous error": true,
    "finest semidiscrete error": true,
    "zero-mode temporal accuracy": true,
    "discrete geostrophic stationarity": true,
    "reference analytic moving-face velocity": true,
    "reference periodic analytic mass": true,
    "reference skew-Hermitian discrete symbol": true,
    "reference continuous wave frequency": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/cgrid-rotating-wave/index.json

![実際に保存した計算配列と固定入力の収束指標から描いた検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/results/cgrid-rotating-wave-preview.png)

実際に保存した計算配列と固定入力の収束指標から描いた検証図。

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/atlas-moving-waves-2026-11-23.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

### 出典と確認範囲

- P. Korn and S. Danilov (n.d.). Elementary dispersion analysis of some mimetic discretizations on triangular C-grids. https://epic.awi.de/id/eprint/42760/1/c-grid_jcp_v5-1.pdf; review_level=selected-primary-author-manuscript
Governing linear equations, energy adjoints and AppendixB quadrilateral standard-C symbols/eq19–21 inspected. Use standard square C-grid only, not the paper triangular mimetic schemes. No global Williamson test or original code run.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
