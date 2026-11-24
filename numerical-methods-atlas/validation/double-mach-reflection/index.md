# Double Mach反射：多格子の軽量検証

既存のDouble Mach反射と同じ初期値・境界を使い、64×16・128×32・256×64の実2D Euler有限体積計算をT=.2まで実行します。別実装の有限格子参照との差、実際の境界流束収支、上部の入射衝撃位置と壁近傍を比較します。

**使用手法**

- [HLL](https://hrkoyama.github.io/numerical-methods-atlas/methods/hll/?lang=ja) (`hll`)
- [Heun法／SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=ja) (`heun`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/double-mach-reflection/?lang=ja#double-mach-reflection-ja-algorithm)

既存Numartの区分定数HLL流束と非分割x/y発散、Heun/SSPRK(2,2)を独立した小型配布物にし、両段の境界流束・状態確認を追加しました。CFL=.4を各方向の最大音響速度の和に適用し、上辺は各RK段の実時刻で更新します。状態floor、セル修復、隠れた刻み再試行はなく、不正段の生配列と履歴を残して失敗します。

$$
\partial_tU+\partial_xF(U)+\partial_yG(U)=0,\qquad U=(\rho,\rho u,\rho v,E)^T
$$

$$
x_s(y,t)=\frac16+\frac{y+20t}{\sqrt3},\quad \gamma=1.4,\quad M_s=10
$$

$$
\Delta t=0.4\left[\max(|u|+c)/\Delta x+\max(|v|+c)/\Delta y\right]^{-1}
$$

$$
\sum_{ij}|C_{ij}|(\bar U_{ij}^{n+1}-\bar U_{ij}^{n})=\frac{\Delta t}{2}(B(U^n,t_n)+B(U^{(1)},t_n+\Delta t))
$$

- [圧縮性Euler方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#euler-ja) (`euler`)

γ=1.4の2次元圧縮性Euler保存系。Mach10の入射衝撃波、流入・流出・反射壁・移動衝撃波を与える上端境界は、この例の固定入力で定義します。


**問題の図**

![Double Mach反射：多格子の軽量検証：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/double-mach/results/double-mach-reflection.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[二重Mach反射](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-mach/?lang=ja) (`double-mach`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-mach/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/double-mach-reflection/?lang=ja#double-mach-reflection-ja-validation)

初回事前契約の20単体検査は合格。全3格子の実行前の読み取りレビューで、衝撃探索窓に前線が無い場合を拒否する診断ガードと1検査を追加し、旧契約・ソースを保持して改訂契約を固定しました。その21検査と全3計算・40判定が-W errorで合格しました。参照はRKDGキットで既に独立実行済みの、別実装primitive MUSCL/generalized-minmod θ=1.5/HLL/HeunのNy64/128データを再利用し、今回は参照PDEを再実行していません。Ny128保存量を保守的に制限して比較した密度L1は.08431/.05802/.03503、圧力L1は.09556/.06798/.04156。参照64/128増分は.00955/.01250で、最細主計算差の約.273/.301です。4保存量の境界収支の最大相対残差は約4.60e-13でした。

- [Double Mach反射：保存済み独立有限格子数値参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-double-mach-ja) (`double-mach`; 同じ問題の参照 · 有限格子の数値参照)

以前に独立実行した2格子の有限体積参照を保存量制限で比較します。有限格子数値参照であり、厳密2D解や誤差上界ではありません。
## 前提・単位・境界

無次元[0,4]×[0,1]、γ=1.4、Mach10。衝撃脚x=1/6、角度60度、後方状態(ρ,u,v,p)=(8,8.25√3/2,−4.125,116.5)、前方(1.4,0,0,1)。初期セルは衝撃のセル中心側で分類し、切断セルの厳密平均ではありません。左は後方流入、右はゼロ勾配、底はx<1/6で後方状態・他は滑り壁、上はx<1/6+(1+20t)/√3で後方状態を与えます。

**編集上の補足**

独立な有限格子の数値参照と比較する軽量例であり、2次元全場の厳密解ではありません。少数格子で測った衝撃位置・保存収支・wall jetの診断と、細い壁面噴流の収束を区別します。前向きステップは今回の実行対象に含めません。

## 採用した計算法

既存Numartの区分定数HLL流束と非分割x/y発散、Heun/SSPRK(2,2)を独立した小型配布物にし、両段の境界流束・状態確認を追加しました。CFL=.4を各方向の最大音響速度の和に適用し、上辺は各RK段の実時刻で更新します。状態floor、セル修復、隠れた刻み再試行はなく、不正段の生配列と履歴を残して失敗します。

$$
\partial_tU+\partial_xF(U)+\partial_yG(U)=0,\qquad U=(\rho,\rho u,\rho v,E)^T
$$

$$
x_s(y,t)=\frac16+\frac{y+20t}{\sqrt3},\quad \gamma=1.4,\quad M_s=10
$$

$$
\Delta t=0.4\left[\max(|u|+c)/\Delta x+\max(|v|+c)/\Delta y\right]^{-1}
$$

$$
\sum_{ij}|C_{ij}|(\bar U_{ij}^{n+1}-\bar U_{ij}^{n})=\frac{\Delta t}{2}(B(U^n,t_n)+B(U^{(1)},t_n+\Delta t))
$$

## 比較・検証

初回事前契約の20単体検査は合格。全3格子の実行前の読み取りレビューで、衝撃探索窓に前線が無い場合を拒否する診断ガードと1検査を追加し、旧契約・ソースを保持して改訂契約を固定しました。その21検査と全3計算・40判定が-W errorで合格しました。参照はRKDGキットで既に独立実行済みの、別実装primitive MUSCL/generalized-minmod θ=1.5/HLL/HeunのNy64/128データを再利用し、今回は参照PDEを再実行していません。Ny128保存量を保守的に制限して比較した密度L1は.08431/.05802/.03503、圧力L1は.09556/.06798/.04156。参照64/128増分は.00955/.01250で、最細主計算差の約.273/.301です。4保存量の境界収支の最大相対残差は約4.60e-13でした。

## 確認の限界

参照は有限格子の数値解で、厳密2D解でも独立のAthena/LAVA実行でもありません。HLLという流束族は共有しますが、参照は主計算の空間演算をimportしない別実装です。参照増分は不確かさの診断で誤差の上界ではありません。差には初期射影、動く境界の格子標本化、離散化と有限参照の影響が入り、傾きは厳密な空間次数や反射パターン全体の収束証明ではありません。上部前線の2セル差は物理幅では細分化で縮小しますが、セル単位の誤差は下がりません。壁近傍は固定領域x∈[1,2.75],y≤.25の比較で、ジェットを追跡した評価ではありません。最細でも領域最大uは主計算12.644に対し参照16.125で、薄いwall jet・巻き上がりは未解像です。前向きステップ、他の壁条件・一般摂動、高次精度、完全なパターン収束は今回の検証外です。

## 保存実測値と判定

```json
{
  "metrics": {
    "n": 64,
    "ny": 64,
    "nx": 256,
    "time": 0.2,
    "steps": 811,
    "density_l1": 0.035029442558786025,
    "pressure_l1": 0.04155565203322573,
    "density_l2": 0.07511923063820683,
    "density_linf": 0.2503923225552139,
    "minimum_density_all_stages": 1.4,
    "minimum_pressure_all_stages": 1.0,
    "density_min": 1.4,
    "density_max": 20.3156584501302,
    "pressure_min": 1.0,
    "pressure_max": 530.3379565726824,
    "state_floor_count": 0,
    "rejected_steps": 0,
    "incident_front_x": 2.9375,
    "reference_incident_front_x": 2.90625,
    "front_row_y": 0.7421875,
    "incident_front_error_cells": 2.0,
    "wall_jet_density_l1": 0.060165720387909134,
    "wall_jet_mean_density": 13.785652231102395,
    "wall_jet_reference_mean_density": 13.97485965152079,
    "wall_jet_mean_u": 8.343336108943573,
    "wall_jet_reference_mean_u": 8.397760320217083,
    "wall_jet_max_u": 12.644046893512225,
    "wall_jet_reference_max_u": 16.125383198389834
  },
  "checks": {
    "three final-time refinements complete": true,
    "ny16: requested time reached": true,
    "ny16: minimum_density_all_stages": true,
    "ny16: minimum_pressure_all_stages": true,
    "ny16: state_floor_count": true,
    "ny16: rejected_steps": true,
    "ny16: mass boundary balance": true,
    "ny16: x momentum boundary balance": true,
    "ny16: y momentum boundary balance": true,
    "ny16: energy boundary balance": true,
    "ny16: unmasked maximum and wall-jet diagnostics retained": true,
    "ny32: requested time reached": true,
    "ny32: minimum_density_all_stages": true,
    "ny32: minimum_pressure_all_stages": true,
    "ny32: state_floor_count": true,
    "ny32: rejected_steps": true,
    "ny32: mass boundary balance": true,
    "ny32: x momentum boundary balance": true,
    "ny32: y momentum boundary balance": true,
    "ny32: energy boundary balance": true,
    "ny32: unmasked maximum and wall-jet diagnostics retained": true,
    "ny64: requested time reached": true,
    "ny64: minimum_density_all_stages": true,
    "ny64: minimum_pressure_all_stages": true,
    "ny64: state_floor_count": true,
    "ny64: rejected_steps": true,
    "ny64: mass boundary balance": true,
    "ny64: x momentum boundary balance": true,
    "ny64: y momentum boundary balance": true,
    "ny64: energy boundary balance": true,
    "ny64: unmasked maximum and wall-jet diagnostics retained": true,
    "finest density_l1": true,
    "finest pressure_l1": true,
    "finest upper incident front difference": true,
    "density difference decreases across the fixed grids": true,
    "last-pair density difference slope": true,
    "reference increment density_l1": true,
    "reference increment / primary finest density_l1": true,
    "reference increment pressure_l1": true,
    "reference increment / primary finest pressure_l1": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/double-mach-reflection/index.json

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23/double-mach/atlas-double-mach-2026-11-23.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23/double-mach/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/double-mach/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23/double-mach/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

## 出典と確認範囲

- Paul Woodward and Phillip Colella (1984). The numerical simulation of two-dimensional fluid flow with strong shocks. https://www.sciencedirect.com/science/article/pii/0021999184901426; review_level=publisher-metadata-and-abstract; official-NASA-setup-cross-check
出版社の書誌・抄録とNASA公式の設定説明を確認。原著本文を直接読んだという記録ではなく、元の強衝撃波比較と問題設定の出典として引用します。

- NASA Advanced Supercomputing Division, LAVA team (n.d.). Double Mach Reflection — LAVA tutorial [accessed 2026-11-23]. https://www.nas.nasa.gov/LAVA/unst_docs/tutorials/double_mach/double_mach/; review_level=official-tutorial-selected-setup-and-boundaries
公式チュートリアルのMach10・γ=1.4、領域、衝撃脚x=1/6、初期密度/圧力、境界とT=.2を確認。LAVA自体を実行した意味ではなく、図も転載しません。

- Hiroshi Koyama (2026). Independent finite-volume references distributed with the RKDG2D agent kit, 2026-11-23-r2. https://hrkoyama.github.io/code/rkdg2d/2026-11-23-r2/atlas-rkdg-agent-kit.zip; review_level=hash-checked-selected-public-archive-artifacts
保存済みの独立2D FV-MUSCL/HLL/Heun参照のソース・2格子データ・実行記録を不変ZIPから選択取得。今回の参照PDE再実行や別のAthena/LAVA実行ではありません。主計算とHLLという流束族は共有しますが、参照は主計算の空間演算をimportしない別実装です。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Double Mach reflection: lightweight grid verification

Full 2D Euler finite volumes evolve the existing Double Mach initial/boundary data to T=.2 on64x16,128x32 and256x64 cells. Compare a separately written finite-grid reference, actual boundary-flux budgets, an upper incident-front position and a fixed near-wall region.

**Methods used**

- [HLL](https://hrkoyama.github.io/numerical-methods-atlas/methods/hll/?lang=en) (`hll`)
- [Heun / SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en) (`heun`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/double-mach-reflection/?lang=en#double-mach-reflection-en-algorithm)

The published Numart piecewise-constant HLL flux, unsplit x/y divergence and Heun/SSPRK(2,2) form a small standalone package with both-stage boundary accounting and state checks. CFL.4 uses the sum of directional maximum acoustic rates; the top boundary uses each actual RK stage time. No state floor, repair or hidden retry. Invalid stages retain raw arrays/history and fail.

$$
\partial_tU+\partial_xF(U)+\partial_yG(U)=0,\qquad U=(\rho,\rho u,\rho v,E)^T
$$

$$
x_s(y,t)=\frac16+\frac{y+20t}{\sqrt3},\quad \gamma=1.4,\quad M_s=10
$$

$$
\Delta t=0.4\left[\max(|u|+c)/\Delta x+\max(|v|+c)/\Delta y\right]^{-1}
$$

$$
\sum_{ij}|C_{ij}|(\bar U_{ij}^{n+1}-\bar U_{ij}^{n})=\frac{\Delta t}{2}(B(U^n,t_n)+B(U^{(1)},t_n+\Delta t))
$$

- [Compressible Euler equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#euler-en) (`euler`)

Two-dimensional compressible Euler conservation laws with gamma1.4. This example fixes the Mach10 incident shock, inflow/outflow, reflecting wall and moving-shock top boundary.


**Problem figure**

![Double Mach reflection: lightweight grid verification: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/double-mach/results/double-mach-reflection.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Double Mach reflection](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-mach/?lang=en) (`double-mach`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-mach/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/double-mach-reflection/?lang=en#double-mach-reflection-en-validation)

The original preregistered20 unit tests passed. Before the full three-grid run, read-only review added an absent-front diagnostic guard and one test; the old contract/source are preserved and a revision contract was frozen. All21 tests, three final-time runs and40 gates passed with-W error. Previously independently executed Ny64/128 primitive MUSCL/generalized-minmod theta1.5/HLL/Heun data from the RKDG kit are reused; no reference PDE was rerun. Density L1 differences from conservatively restricted Ny128 are.08431/.05802/.03503 and pressure differences.09556/.06798/.04156. Reference64/128 increments are.00955/.01250, about.273/.301 of the finest primary differences. Maximum relative four-component boundary-budget residual is about4.60e-13.

- [Double Mach reflection: saved independent finite-grid numerical reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-double-mach-en) (`double-mach`; Same-problem reference · Finite-grid numerical reference)

Compare against two previously independently executed finite-volume reference grids using conservative restriction. This is a finite-grid numerical reference, not an exact2D solution or error bound.
## Assumptions, units and boundaries

Nondimensional[0,4]x[0,1], gamma1.4, Mach10. Shock footx=1/6, angle60degrees; postshock(rho,u,v,p)=(8,8.25sqrt(3)/2,-4.125,116.5), upstream(1.4,0,0,1). Initial cells are classified by their centers, not exact cut-cell means. Left postshock inflow, right zero-gradient, bottom postshock forx<1/6 and slip wall otherwise; top postshock forx<1/6+(1+20t)/sqrt(3).

**Editorial clarification**

A lightweight comparison with an independent finite-grid numerical reference, not an exact2D full-field solution. Separate measured shock location, conservation budgets and wall-jet diagnostics from convergence of the thin wall jet. Forward-facing step is outside this execution scope.

## Adopted numerical method

The published Numart piecewise-constant HLL flux, unsplit x/y divergence and Heun/SSPRK(2,2) form a small standalone package with both-stage boundary accounting and state checks. CFL.4 uses the sum of directional maximum acoustic rates; the top boundary uses each actual RK stage time. No state floor, repair or hidden retry. Invalid stages retain raw arrays/history and fail.

$$
\partial_tU+\partial_xF(U)+\partial_yG(U)=0,\qquad U=(\rho,\rho u,\rho v,E)^T
$$

$$
x_s(y,t)=\frac16+\frac{y+20t}{\sqrt3},\quad \gamma=1.4,\quad M_s=10
$$

$$
\Delta t=0.4\left[\max(|u|+c)/\Delta x+\max(|v|+c)/\Delta y\right]^{-1}
$$

$$
\sum_{ij}|C_{ij}|(\bar U_{ij}^{n+1}-\bar U_{ij}^{n})=\frac{\Delta t}{2}(B(U^n,t_n)+B(U^{(1)},t_n+\Delta t))
$$

## References and validation

The original preregistered20 unit tests passed. Before the full three-grid run, read-only review added an absent-front diagnostic guard and one test; the old contract/source are preserved and a revision contract was frozen. All21 tests, three final-time runs and40 gates passed with-W error. Previously independently executed Ny64/128 primitive MUSCL/generalized-minmod theta1.5/HLL/Heun data from the RKDG kit are reused; no reference PDE was rerun. Density L1 differences from conservatively restricted Ny128 are.08431/.05802/.03503 and pressure differences.09556/.06798/.04156. Reference64/128 increments are.00955/.01250, about.273/.301 of the finest primary differences. Maximum relative four-component boundary-budget residual is about4.60e-13.

## Limits

The reference is finite-grid numerical data, not an exact2D solution or an Athena/LAVA execution. The HLL family is shared, but reference spatial operators are separately written and not imported by the primary. The reference increment is an uncertainty diagnostic, not an error bound. Initial projection, sampled moving boundaries, discretization and finite-reference effects all enter the difference; the slope is no rigorous order or full reflection-pattern convergence proof. The upper-front discrepancy stays2cells while its physical width shrinks. Fixed near-wall ROIx in[1,2.75],y<=.25 is not feature tracking. Finest ROI maxu12.644 versus reference16.125 shows the thin wall jet/roll-up is unresolved. Forward step, other wall data, general perturbations, higher order and full-pattern convergence are unverified.

## Stored measurements and decisions

```json
{
  "metrics": {
    "n": 64,
    "ny": 64,
    "nx": 256,
    "time": 0.2,
    "steps": 811,
    "density_l1": 0.035029442558786025,
    "pressure_l1": 0.04155565203322573,
    "density_l2": 0.07511923063820683,
    "density_linf": 0.2503923225552139,
    "minimum_density_all_stages": 1.4,
    "minimum_pressure_all_stages": 1.0,
    "density_min": 1.4,
    "density_max": 20.3156584501302,
    "pressure_min": 1.0,
    "pressure_max": 530.3379565726824,
    "state_floor_count": 0,
    "rejected_steps": 0,
    "incident_front_x": 2.9375,
    "reference_incident_front_x": 2.90625,
    "front_row_y": 0.7421875,
    "incident_front_error_cells": 2.0,
    "wall_jet_density_l1": 0.060165720387909134,
    "wall_jet_mean_density": 13.785652231102395,
    "wall_jet_reference_mean_density": 13.97485965152079,
    "wall_jet_mean_u": 8.343336108943573,
    "wall_jet_reference_mean_u": 8.397760320217083,
    "wall_jet_max_u": 12.644046893512225,
    "wall_jet_reference_max_u": 16.125383198389834
  },
  "checks": {
    "three final-time refinements complete": true,
    "ny16: requested time reached": true,
    "ny16: minimum_density_all_stages": true,
    "ny16: minimum_pressure_all_stages": true,
    "ny16: state_floor_count": true,
    "ny16: rejected_steps": true,
    "ny16: mass boundary balance": true,
    "ny16: x momentum boundary balance": true,
    "ny16: y momentum boundary balance": true,
    "ny16: energy boundary balance": true,
    "ny16: unmasked maximum and wall-jet diagnostics retained": true,
    "ny32: requested time reached": true,
    "ny32: minimum_density_all_stages": true,
    "ny32: minimum_pressure_all_stages": true,
    "ny32: state_floor_count": true,
    "ny32: rejected_steps": true,
    "ny32: mass boundary balance": true,
    "ny32: x momentum boundary balance": true,
    "ny32: y momentum boundary balance": true,
    "ny32: energy boundary balance": true,
    "ny32: unmasked maximum and wall-jet diagnostics retained": true,
    "ny64: requested time reached": true,
    "ny64: minimum_density_all_stages": true,
    "ny64: minimum_pressure_all_stages": true,
    "ny64: state_floor_count": true,
    "ny64: rejected_steps": true,
    "ny64: mass boundary balance": true,
    "ny64: x momentum boundary balance": true,
    "ny64: y momentum boundary balance": true,
    "ny64: energy boundary balance": true,
    "ny64: unmasked maximum and wall-jet diagnostics retained": true,
    "finest density_l1": true,
    "finest pressure_l1": true,
    "finest upper incident front difference": true,
    "density difference decreases across the fixed grids": true,
    "last-pair density difference slope": true,
    "reference increment density_l1": true,
    "reference increment / primary finest density_l1": true,
    "reference increment pressure_l1": true,
    "reference increment / primary finest pressure_l1": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/double-mach-reflection/index.json

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23/double-mach/atlas-double-mach-2026-11-23.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23/double-mach/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/double-mach/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23/double-mach/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

## Sources and review scope

- Paul Woodward and Phillip Colella (1984). The numerical simulation of two-dimensional fluid flow with strong shocks. https://www.sciencedirect.com/science/article/pii/0021999184901426; review_level=publisher-metadata-and-abstract; official-NASA-setup-cross-check
Publisher metadata/abstract and the official NASA setup were checked. No direct full-paper review is claimed; cited for the original strong-shock comparison and benchmark.

- NASA Advanced Supercomputing Division, LAVA team (n.d.). Double Mach Reflection — LAVA tutorial [accessed 2026-11-23]. https://www.nas.nasa.gov/LAVA/unst_docs/tutorials/double_mach/double_mach/; review_level=official-tutorial-selected-setup-and-boundaries
Checked Mach10, gamma1.4, domain, shock foot x=1/6, upstream state, boundaries and T=.2. No LAVA execution or figure redistribution.

- Hiroshi Koyama (2026). Independent finite-volume references distributed with the RKDG2D agent kit, 2026-11-23-r2. https://hrkoyama.github.io/code/rkdg2d/2026-11-23-r2/atlas-rkdg-agent-kit.zip; review_level=hash-checked-selected-public-archive-artifacts
Selected source, two-grid data and execution records were copied from the immutable archive. No reference PDE, Athena or LAVA was rerun here. The flux family HLL is shared, while the reference is a separate implementation without imports of primary spatial operators.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
