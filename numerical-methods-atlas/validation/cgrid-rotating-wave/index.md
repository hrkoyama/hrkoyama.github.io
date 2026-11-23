# 2D C-grid回転浅水波の実時間発展

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
## 前提・単位・境界

線形f-plane、g=H=f=1、周期単位正方形、(k,l)=(1,2)、eta振幅.01、N16/32/64,T.5。別の固定N16時間系列、zero-modeと離散geostrophic診断。

**編集上の補足**

線形・平面・周期squareの限定例。非線形浅水、PV・球面格子・全球dynamical coreやWilliamsonは未実装の後続課題。

## 採用した計算法

セルeta・法線face u/vの差分と4点Coriolis補間を2Dで評価しRK4更新。3×3行列指数は参照だけで、PDE場の更新には使いません。

$$
\eta_t+u_x+v_y=0,\quad u_t=v-\eta_x,\quad v_t=-u-\eta_y
$$

$$
\tilde k=2\sin(kh/2)/h,\quad C=\cos(kh/2)\cos(lh/2),\quad U_h(t)=e^{tL_h}U_h(0)
$$

## 比較・検証

連続PDE空間誤差と離散symbol時間誤差、mass/energy、stencil-symbol一致、zero-mode慣性振動と離散定常釣合いを保存。

## 確認の限界

線形・平面・周期squareの限定例。非線形浅水、PV・球面格子・全球dynamical coreやWilliamsonは未実装の後続課題。

## 保存実測値と判定

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

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/atlas-moving-waves-2026-11-23.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。

## 出典と確認範囲

- P. Korn and S. Danilov (n.d.). Elementary dispersion analysis of some mimetic discretizations on triangular C-grids. https://epic.awi.de/id/eprint/42760/1/c-grid_jcp_v5-1.pdf; review_level=selected-primary-author-manuscript

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Actual2D C-grid rotating shallow-water time advance

Time-advance actual2D staggered fields and distinguish continuous-wave references from semidiscrete symbols.

**Methods used**

- [Centered spatial difference](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en) (`centered-difference`)
- [Classical RK4](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=en) (`rk4`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/cgrid-rotating-wave/?lang=en#cgrid-rotating-wave-en-algorithm)

Actual2D cell-height/face-velocity differences and four-point Coriolis interpolation use RK4. The3×3 matrix exponential is reference-only, never the PDE update.

$$
\eta_t+u_x+v_y=0,\quad u_t=v-\eta_x,\quad v_t=-u-\eta_y
$$

$$
\tilde k=2\sin(kh/2)/h,\quad C=\cos(kh/2)\cos(lh/2),\quad U_h(t)=e^{tL_h}U_h(0)
$$

- [Linear rotating shallow-water equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#linear-rotating-shallow-water-en) (`linear-rotating-shallow-water`)

Linear f-plane,g=H=f=1, periodic unit square, mode(1,2),height amplitude.01,N16/32/64,T.5. Separate N16 time refinement, zero-mode and discrete geostrophic probes.


**Problem figure**

![Actual2D C-grid rotating shallow-water time advance: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/results/cgrid-rotating-wave.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Actual2D C-grid rotating shallow-water time advance](https://hrkoyama.github.io/numerical-methods-atlas/problems/cgrid-rotating-wave/?lang=en) (`cgrid-rotating-wave`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/cgrid-rotating-wave/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/cgrid-rotating-wave/?lang=en#cgrid-rotating-wave-en-validation)

Retain continuous-PDE spatial and discrete-symbol temporal errors, mass/energy, stencil-symbol identity, zero-mode inertia and discrete steady balance.

- [C-grid: continuous Fourier solution and discrete-symbol exponential](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-cgrid-rotating-wave-en) (`cgrid-rotating-wave`; Same-problem reference · Analytic reference)

Linear planar periodic square only. Nonlinear SWE,PV,spherical dynamics and Williamson tests remain future work.
## Assumptions, units and boundaries

Linear f-plane,g=H=f=1, periodic unit square, mode(1,2),height amplitude.01,N16/32/64,T.5. Separate N16 time refinement, zero-mode and discrete geostrophic probes.

**Editorial clarification**

Linear planar periodic square only. Nonlinear SWE,PV,spherical dynamics and Williamson tests remain future work.

## Adopted numerical method

Actual2D cell-height/face-velocity differences and four-point Coriolis interpolation use RK4. The3×3 matrix exponential is reference-only, never the PDE update.

$$
\eta_t+u_x+v_y=0,\quad u_t=v-\eta_x,\quad v_t=-u-\eta_y
$$

$$
\tilde k=2\sin(kh/2)/h,\quad C=\cos(kh/2)\cos(lh/2),\quad U_h(t)=e^{tL_h}U_h(0)
$$

## References and validation

Retain continuous-PDE spatial and discrete-symbol temporal errors, mass/energy, stencil-symbol identity, zero-mode inertia and discrete steady balance.

## Limits

Linear planar periodic square only. Nonlinear SWE,PV,spherical dynamics and Williamson tests remain future work.

## Stored measurements and decisions

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

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/cgrid-rotating-wave/index.json

![Validation preview from actual saved PDE arrays and fixed-input refinement measurements.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/results/cgrid-rotating-wave-preview.png)

Validation preview from actual saved PDE arrays and fixed-input refinement measurements.

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/atlas-moving-waves-2026-11-23.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group.

## Sources and review scope

- P. Korn and S. Danilov (n.d.). Elementary dispersion analysis of some mimetic discretizations on triangular C-grids. https://epic.awi.de/id/eprint/42760/1/c-grid_jcp_v5-1.pdf; review_level=selected-primary-author-manuscript

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
