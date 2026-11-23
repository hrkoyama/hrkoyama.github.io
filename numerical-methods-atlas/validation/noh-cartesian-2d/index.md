# Noh問題：実際の2次元Cartesian Euler計算

正方形の全域で密度・2成分運動量・全エネルギーを更新する、小型の2次元Euler有限体積計算です。32²・64²・128²の3格子で厳密Noh状態からの誤差・保存収支・格子方向の影響を測ります。図は実際の2次元保存配列で、1D半径解の回転表示ではありません。

**使用手法**

- [Rusanov／局所Lax–Friedrichs流束](https://hrkoyama.github.io/numerical-methods-atlas/methods/rusanov/?lang=ja) (`rusanov`)
- [Heun法／SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=ja) (`heun`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-cartesian-2d/?lang=ja#noh-cartesian-2d-ja-algorithm)

区分定数のRusanov流束をx/y両方向の共有面に置く非分割更新とSSPRK2（Heun）です。CFL=.35を(max a_x+max a_y)/Δxに適用。外辺の冷たい物理流束は面内で解析積分し、時間に一次の流入をHeunの両段で積分します。セル平均の修復・圧力floor・seed・隠れた時間刻み再試行はなく、不正なRK段は配列を保存して失敗にします。

$$
\partial_t U+\partial_xF(U)+\partial_yG(U)=0,\quad U=(\rho,\rho u,\rho v,E)^T
$$

$$
r_s=t/3,\quad(\rho,p,u_r)_2=(16,16/3,0),\quad(\rho,p,u_r)_1=(1+t/r,0,-1)
$$

$$
\bar\rho_i=\frac{1}{\Delta x\Delta y}\int_{C_i}\rho_{\rm exact}(\sqrt{x^2+y^2},t)\,dx\,dy
$$

$$
M(t)=4R^2+8Rt\operatorname{asinh}(1)+\pi t^2,\qquad E_{\rm tot}=M/2,\quad R=0.5
$$

$$
\Delta t=\frac{0.35}{\max a_x/\Delta x+\max a_y/\Delta y}
$$

- [圧縮性Euler方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#euler-ja) (`euler`)

幾何源のない2次元Cartesian Euler系です。密度・2成分運動量・全エネルギーを正方形全域で更新します。


**問題の図**

![Noh問題：実際の2次元Cartesian Euler計算：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/noh-cartesian/results/noh-cartesian-2d.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Noh問題：冷たい収束流と外向き衝撃波](https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=ja) (`noh`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-cartesian-2d/?lang=ja#noh-cartesian-2d-ja-validation)

実行前に入力・ソース・受入基準をhash保存。19単体検査と3格子・49判定が初回から合格しました。解析密度のセル積分は衝撃円の交差で区間を分割し、x=rs sinθによる64点Gauss求積で評価、128点との差と全質量の解析式で確認します。閉形式の厳密セル平均とは区別します。128²で密度全域L1=.09981、原点込みcore L1=.12231、衝撃位置は軸.968セル・対角1.469セルの誤差。離散収支の最大相対残差は約4.6e-15です。D4の鏡映・座標交換の保存量偶奇性と、連続回転対称性を区別して測ります。

- [Nohの冷たい流入衝撃波：平面・円筒・球対称](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-noh-ja) (`noh`; 同じ問題の参照 · 解析参照)

同じNoh問題の解析参照。1Dは保存量の厳密体積平均、2Dは衝撃円で分割した密度の求積セル平均を使用します。点値とセル平均、p(平均U)と平均pを区別します。
## 前提・単位・境界

無次元[-.5,.5]²、γ=5/3、ρ0=1、内向き速度1、p0=0、T=.6、衝撃半径.2。初期保存量はセル中心の冷たい状態の標本で、初期運動量の厳密セル平均ではありません。全4辺へρ=1+t/r、u=(-x/r,-y/r)の超音速流入を与え、対称境界・半径方向への射影・幾何源は使いません。

## 採用した計算法

区分定数のRusanov流束をx/y両方向の共有面に置く非分割更新とSSPRK2（Heun）です。CFL=.35を(max a_x+max a_y)/Δxに適用。外辺の冷たい物理流束は面内で解析積分し、時間に一次の流入をHeunの両段で積分します。セル平均の修復・圧力floor・seed・隠れた時間刻み再試行はなく、不正なRK段は配列を保存して失敗にします。

$$
\partial_t U+\partial_xF(U)+\partial_yG(U)=0,\quad U=(\rho,\rho u,\rho v,E)^T
$$

$$
r_s=t/3,\quad(\rho,p,u_r)_2=(16,16/3,0),\quad(\rho,p,u_r)_1=(1+t/r,0,-1)
$$

$$
\bar\rho_i=\frac{1}{\Delta x\Delta y}\int_{C_i}\rho_{\rm exact}(\sqrt{x^2+y^2},t)\,dx\,dy
$$

$$
M(t)=4R^2+8Rt\operatorname{asinh}(1)+\pi t^2,\qquad E_{\rm tot}=M/2,\quad R=0.5
$$

$$
\Delta t=\frac{0.35}{\max a_x/\Delta x+\max a_y/\Delta y}
$$

## 比較・検証

実行前に入力・ソース・受入基準をhash保存。19単体検査と3格子・49判定が初回から合格しました。解析密度のセル積分は衝撃円の交差で区間を分割し、x=rs sinθによる64点Gauss求積で評価、128点との差と全質量の解析式で確認します。閉形式の厳密セル平均とは区別します。128²で密度全域L1=.09981、原点込みcore L1=.12231、衝撃位置は軸.968セル・対角1.469セルの誤差。離散収支の最大相対残差は約4.6e-15です。D4の鏡映・座標交換の保存量偶奇性と、連続回転対称性を区別して測ります。

## 確認の限界

空間一次の軽量例で、原点過熱と衝撃層の誤差が残ります。最細格子でも中心最大比内部エネルギーは厳密値より約14%高いままです。軸・対角の衝撃半径差は約.501Δxで、3格子間で単調には減りません。D4偶奇性が丸め誤差でも円対称性が厳密という意味ではありません。一般の摂動安定性・原点位置ずらし・回転格子・3D Cartesian・高次精度は未検証です。旧1D平面/円筒/球の配布版と判定は変更しません。

## 保存実測値と判定

```json
{
  "metrics": {
    "n": 128,
    "steps": 494,
    "time": 0.6,
    "density_l1": 0.09980879898658265,
    "density_l2": 0.19425569047493216,
    "density_linf": 0.5034609713695807,
    "core_density_l1": 0.12230837999864347,
    "plateau_density_relative_error": 0.11211523785241806,
    "plateau_pressure_relative_error": 0.06423624701669228,
    "center_max_internal_energy_excess": 0.13988852566613885,
    "center_min_density": 13.207234408428087,
    "density_min": 1.856867213907176,
    "density_max": 16.460396201777943,
    "minimum_density_all_stages": 1.0,
    "minimum_pressure_all_stages": 0.0,
    "minimum_internal_roundoff_units": 0.0,
    "state_floor_count": 0,
    "d4_conserved_parity_relative": 0.0,
    "reference_order_relative_l1_difference": 3.485261130218118e-18,
    "reference_mass_relative_error": 0.0,
    "mass_vs_analytic_relative": 1.7763568394002505e-15,
    "energy_vs_analytic_relative": 3.3306690738754696e-15,
    "axis_shock_radius": 0.20756435977317667,
    "diagonal_shock_radius": 0.2114756773594714,
    "axis_shock_error_cells": 0.9682380509666153,
    "diagonal_shock_error_cells": 1.468886702012341,
    "shock_axis_diagonal_difference_cells": 0.5006486510457258
  },
  "checks": {
    "all three Cartesian grids complete": true,
    "n32: positive density all stages": true,
    "n32: internal energy within roundoff": true,
    "n32: no floors or cell repair": true,
    "n32: mass discrete balance": true,
    "n32: x momentum discrete balance": true,
    "n32: y momentum discrete balance": true,
    "n32: energy discrete balance": true,
    "n32: mass_vs_analytic_relative": true,
    "n32: energy_vs_analytic_relative": true,
    "n32: d4_conserved_parity_relative": true,
    "n32: reference_order_relative_l1_difference": true,
    "n32: reference_mass_relative_error": true,
    "n32: unmasked center and maximum errors reported": true,
    "n64: positive density all stages": true,
    "n64: internal energy within roundoff": true,
    "n64: no floors or cell repair": true,
    "n64: mass discrete balance": true,
    "n64: x momentum discrete balance": true,
    "n64: y momentum discrete balance": true,
    "n64: energy discrete balance": true,
    "n64: mass_vs_analytic_relative": true,
    "n64: energy_vs_analytic_relative": true,
    "n64: d4_conserved_parity_relative": true,
    "n64: reference_order_relative_l1_difference": true,
    "n64: reference_mass_relative_error": true,
    "n64: unmasked center and maximum errors reported": true,
    "n128: positive density all stages": true,
    "n128: internal energy within roundoff": true,
    "n128: no floors or cell repair": true,
    "n128: mass discrete balance": true,
    "n128: x momentum discrete balance": true,
    "n128: y momentum discrete balance": true,
    "n128: energy discrete balance": true,
    "n128: mass_vs_analytic_relative": true,
    "n128: energy_vs_analytic_relative": true,
    "n128: d4_conserved_parity_relative": true,
    "n128: reference_order_relative_l1_difference": true,
    "n128: reference_mass_relative_error": true,
    "n128: unmasked center and maximum errors reported": true,
    "finest density_l1": true,
    "finest core_density_l1": true,
    "finest plateau_density_relative_error": true,
    "finest plateau_pressure_relative_error": true,
    "finest axis_shock_error_cells": true,
    "finest diagonal_shock_error_cells": true,
    "finest shock_axis_diagonal_difference_cells": true,
    "density L1 decreases": true,
    "last pair density L1 order": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-cartesian-2d/index.json

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/noh-cartesian/atlas-noh-cartesian-2026-11-23-r2.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/noh-cartesian/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/noh-cartesian/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/noh-cartesian/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。

## 出典と確認範囲

- W. F. Noh (1987). Errors for calculations of strong shocks using an artificial viscosity and an artificial heat flux. https://www.sciencedirect.com/science/article/pii/002199918790074X; review_level=publisher-metadata-and-abstract
  出版社書誌・抄録を確認。原著本文の直接取得は403のため全文未読。Noh問題・過熱誤差の原著として引用し、今回の有限体積離散化そのものの出典とは呼びません。
- J. Thrussell and J. M. Ferguson (2023). ExactPack: A python library of exact analytic solutions. https://doi.org/10.1016/j.softx.2023.101560; review_level=official-record-and-unmodified-pinned-code-execution
  固定commitの公式Noh解析評価器を選択確認。既存の独立実行済みd=2点値を再利用し、今回もジャンプから離れた点で照合。ExactPackの再実行や独立2D PDEソルバーとの比較ではありません。

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Noh problem: an actual 2D Cartesian Euler calculation

A small 2D Euler finite-volume calculation evolves density, both momenta and total energy over the full square. Three grids,32²/64²/128², measure Noh-reference errors, budgets and grid orientation effects. The picture shows the actual evolved 2D array.

**Methods used**

- [Rusanov / local Lax–Friedrichs flux](https://hrkoyama.github.io/numerical-methods-atlas/methods/rusanov/?lang=en) (`rusanov`)
- [Heun / SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en) (`heun`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-cartesian-2d/?lang=en#noh-cartesian-2d-en-algorithm)

Unsplit shared-face x/y piecewise-constant Rusanov fluxes and SSPRK2/Heun. CFL .35 uses (max a_x+max a_y)/dx. Cold physical outer fluxes are spatially integrated analytically and their affine time dependence is integrated at both Heun stages. No cell repair, pressure floor/seed or hidden timestep retry; invalid stages retain raw arrays and fail.

$$
\partial_t U+\partial_xF(U)+\partial_yG(U)=0,\quad U=(\rho,\rho u,\rho v,E)^T
$$

$$
r_s=t/3,\quad(\rho,p,u_r)_2=(16,16/3,0),\quad(\rho,p,u_r)_1=(1+t/r,0,-1)
$$

$$
\bar\rho_i=\frac{1}{\Delta x\Delta y}\int_{C_i}\rho_{\rm exact}(\sqrt{x^2+y^2},t)\,dx\,dy
$$

$$
M(t)=4R^2+8Rt\operatorname{asinh}(1)+\pi t^2,\qquad E_{\rm tot}=M/2,\quad R=0.5
$$

$$
\Delta t=\frac{0.35}{\max a_x/\Delta x+\max a_y/\Delta y}
$$

- [Compressible Euler equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#euler-en) (`euler`)

Two-dimensional Cartesian Euler without a geometric source, evolving density, both momenta and energy over the full square.


**Problem figure**

![Noh problem: an actual 2D Cartesian Euler calculation: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/noh-cartesian/results/noh-cartesian-2d.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Noh problem: cold converging flow and outward shock](https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=en) (`noh`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-cartesian-2d/?lang=en#noh-cartesian-2d-en-validation)

Inputs/source/acceptance hashes are saved before execution. All 19 unit tests and 49 gates on three grids passed at the first attempt. Analytic density is integrated over cells by splitting shock-circle cuts and 64-point Gauss quadrature with x=rs sin(theta), checked against 128 points and analytic total mass; these are quadrature references, not closed-form exact cell means. At 128², full-square density L1=.09981, origin-inclusive core L1=.12231; shock errors are.968 axis cells and1.469 diagonal cells. Maximum relative discrete-budget residual is about 4.6e-15. D4 conserved parity and continuous rotational symmetry are measured separately.

- [Noh cold-inflow shock: planar, cylindrical and spherical symmetry](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-noh-en) (`noh`; Same-problem reference · Analytic reference)

Analytic reference for the same Noh problem.1D uses exact conserved-volume means;2D uses density means from shock-split Cartesian cell quadrature. Distinguish points/cell means and p(mean U)/mean p.
## Assumptions, units and boundaries

Nondimensional [-.5,.5]², gamma=5/3, rho0=1, inward speed 1, p0=0, T=.6, shock radius.2. Initial conserved states are cell-center cold samples, not exact initial momentum means. All four edges prescribe supersonic inflow rho=1+t/r and u=(-x/r,-y/r). No symmetry boundary, radial projection or geometric source.

## Adopted numerical method

Unsplit shared-face x/y piecewise-constant Rusanov fluxes and SSPRK2/Heun. CFL .35 uses (max a_x+max a_y)/dx. Cold physical outer fluxes are spatially integrated analytically and their affine time dependence is integrated at both Heun stages. No cell repair, pressure floor/seed or hidden timestep retry; invalid stages retain raw arrays and fail.

$$
\partial_t U+\partial_xF(U)+\partial_yG(U)=0,\quad U=(\rho,\rho u,\rho v,E)^T
$$

$$
r_s=t/3,\quad(\rho,p,u_r)_2=(16,16/3,0),\quad(\rho,p,u_r)_1=(1+t/r,0,-1)
$$

$$
\bar\rho_i=\frac{1}{\Delta x\Delta y}\int_{C_i}\rho_{\rm exact}(\sqrt{x^2+y^2},t)\,dx\,dy
$$

$$
M(t)=4R^2+8Rt\operatorname{asinh}(1)+\pi t^2,\qquad E_{\rm tot}=M/2,\quad R=0.5
$$

$$
\Delta t=\frac{0.35}{\max a_x/\Delta x+\max a_y/\Delta y}
$$

## References and validation

Inputs/source/acceptance hashes are saved before execution. All 19 unit tests and 49 gates on three grids passed at the first attempt. Analytic density is integrated over cells by splitting shock-circle cuts and 64-point Gauss quadrature with x=rs sin(theta), checked against 128 points and analytic total mass; these are quadrature references, not closed-form exact cell means. At 128², full-square density L1=.09981, origin-inclusive core L1=.12231; shock errors are.968 axis cells and1.469 diagonal cells. Maximum relative discrete-budget residual is about 4.6e-15. D4 conserved parity and continuous rotational symmetry are measured separately.

## Limits

A first-order-space lightweight example retains origin heating and shock errors. Finest maximum center specific internal energy is still about 14% high. Axis/diagonal shock-radius difference is about .501dx and is not monotone over these grids. Roundoff-level D4 parity does not establish exact circular symmetry. General perturbation stability, displaced origins, rotated meshes, 3D Cartesian flow and high-order accuracy are unverified. Earlier planar/cylindrical/spherical 1D editions and gates remain unchanged.

## Stored measurements and decisions

```json
{
  "metrics": {
    "n": 128,
    "steps": 494,
    "time": 0.6,
    "density_l1": 0.09980879898658265,
    "density_l2": 0.19425569047493216,
    "density_linf": 0.5034609713695807,
    "core_density_l1": 0.12230837999864347,
    "plateau_density_relative_error": 0.11211523785241806,
    "plateau_pressure_relative_error": 0.06423624701669228,
    "center_max_internal_energy_excess": 0.13988852566613885,
    "center_min_density": 13.207234408428087,
    "density_min": 1.856867213907176,
    "density_max": 16.460396201777943,
    "minimum_density_all_stages": 1.0,
    "minimum_pressure_all_stages": 0.0,
    "minimum_internal_roundoff_units": 0.0,
    "state_floor_count": 0,
    "d4_conserved_parity_relative": 0.0,
    "reference_order_relative_l1_difference": 3.485261130218118e-18,
    "reference_mass_relative_error": 0.0,
    "mass_vs_analytic_relative": 1.7763568394002505e-15,
    "energy_vs_analytic_relative": 3.3306690738754696e-15,
    "axis_shock_radius": 0.20756435977317667,
    "diagonal_shock_radius": 0.2114756773594714,
    "axis_shock_error_cells": 0.9682380509666153,
    "diagonal_shock_error_cells": 1.468886702012341,
    "shock_axis_diagonal_difference_cells": 0.5006486510457258
  },
  "checks": {
    "all three Cartesian grids complete": true,
    "n32: positive density all stages": true,
    "n32: internal energy within roundoff": true,
    "n32: no floors or cell repair": true,
    "n32: mass discrete balance": true,
    "n32: x momentum discrete balance": true,
    "n32: y momentum discrete balance": true,
    "n32: energy discrete balance": true,
    "n32: mass_vs_analytic_relative": true,
    "n32: energy_vs_analytic_relative": true,
    "n32: d4_conserved_parity_relative": true,
    "n32: reference_order_relative_l1_difference": true,
    "n32: reference_mass_relative_error": true,
    "n32: unmasked center and maximum errors reported": true,
    "n64: positive density all stages": true,
    "n64: internal energy within roundoff": true,
    "n64: no floors or cell repair": true,
    "n64: mass discrete balance": true,
    "n64: x momentum discrete balance": true,
    "n64: y momentum discrete balance": true,
    "n64: energy discrete balance": true,
    "n64: mass_vs_analytic_relative": true,
    "n64: energy_vs_analytic_relative": true,
    "n64: d4_conserved_parity_relative": true,
    "n64: reference_order_relative_l1_difference": true,
    "n64: reference_mass_relative_error": true,
    "n64: unmasked center and maximum errors reported": true,
    "n128: positive density all stages": true,
    "n128: internal energy within roundoff": true,
    "n128: no floors or cell repair": true,
    "n128: mass discrete balance": true,
    "n128: x momentum discrete balance": true,
    "n128: y momentum discrete balance": true,
    "n128: energy discrete balance": true,
    "n128: mass_vs_analytic_relative": true,
    "n128: energy_vs_analytic_relative": true,
    "n128: d4_conserved_parity_relative": true,
    "n128: reference_order_relative_l1_difference": true,
    "n128: reference_mass_relative_error": true,
    "n128: unmasked center and maximum errors reported": true,
    "finest density_l1": true,
    "finest core_density_l1": true,
    "finest plateau_density_relative_error": true,
    "finest plateau_pressure_relative_error": true,
    "finest axis_shock_error_cells": true,
    "finest diagonal_shock_error_cells": true,
    "finest shock_axis_diagonal_difference_cells": true,
    "density L1 decreases": true,
    "last pair density L1 order": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-cartesian-2d/index.json

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/noh-cartesian/atlas-noh-cartesian-2026-11-23-r2.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/noh-cartesian/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/noh-cartesian/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/noh-cartesian/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group.

## Sources and review scope

- W. F. Noh (1987). Errors for calculations of strong shocks using an artificial viscosity and an artificial heat flux. https://www.sciencedirect.com/science/article/pii/002199918790074X; review_level=publisher-metadata-and-abstract
  Publisher metadata and abstract checked; full original text was not accessed (403). Cited for the problem and heating-error analysis, not as the source of this particular finite-volume discretization.
- J. Thrussell and J. M. Ferguson (2023). ExactPack: A python library of exact analytic solutions. https://doi.org/10.1016/j.softx.2023.101560; review_level=official-record-and-unmodified-pinned-code-execution
  Selected pinned official Noh evaluator code checked. Reuse previously independently executed d=2 point values away from the jump; no new ExactPack execution or independent 2D PDE-engine comparison.

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
