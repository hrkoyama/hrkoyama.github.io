# 非一様移動格子で実際に運ぶALEスカラー

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
## 前提・単位・境界

周期[0,1]、速度.7、q0=1+.2sin(2pi x)、面速度w=.2sin(2pi xi)cos(2pi t)、N40/80/160、T1。時間比較N40,T.25,32/64/128step。

**編集上の補足**

1D指定格子運動の第一段階です。図のx–tは2D物理計算ではなく、Euler Lagrange/remapやSaltzmanピストンは未実装の後続課題。

## 採用した計算法

実セル質量の上流相対流束(a−w)qと実面位置を同じHeun predictor/correctorで進め、各段体積・面Courant数を記録。

$$
\dot m_i=-[(a-w)q]_{i+1/2}+[(a-w)q]_{i-1/2},\quad V_i=x_{i+1/2}-x_{i-1/2}
$$

$$
x(\xi,t)=\xi+0.2\sin(2\pi\xi)\sin(2\pi t)/(2\pi)
$$

## 比較・検証

解析的移動セル積分、全体/段の質量、GCLconstant、格子幾何誤差を分離。独立DOP853による同じFV ODEの時間参照を二公差で確認。

## 確認の限界

1D指定格子運動の第一段階です。図のx–tは2D物理計算ではなく、Euler Lagrange/remapやSaltzmanピストンは未実装の後続課題。

## 保存実測値と判定

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

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

## 出典と確認範囲

- Dennis L. Huff (1987). Numerical Simulations of Unsteady, Viscous, Transonic Flow Over Isolated and Cascaded Airfoils Using a Deforming Grid. https://ntrs.nasa.gov/api/citations/19870015002/downloads/19870015002.pdf; review_level=selected-primary-report-grid-treatment
NASA TM89890 grid-velocity and GCL discussion around equation11/printedp5 inspected. It attributes GCL to Thomas/Lombard. Original1979 paper not read; no airfoil algorithm or code reproduced. Our 1D scalar moving-volume/Heun derivation is independent.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# ALE scalar transport on genuinely nonuniform moving cells

Advance cell integrals and face positions with identical Heun stages, transporting a nonuniform analytic wave beyond a uniform GCL check.

**Methods used**

- [ALE uniform-state / geometric-conservation model](https://hrkoyama.github.io/numerical-methods-atlas/methods/ale/?lang=en) (`ale`)
- [Upwind finite differences](https://hrkoyama.github.io/numerical-methods-atlas/methods/upwind/?lang=en) (`upwind`)
- [Heun / SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en) (`heun`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/ale-nonuniform-transport/?lang=en#ale-nonuniform-transport-en-algorithm)

Upwind relative flux(a-w)q advances actual masses with identical predictor/corrector face geometry; record stage volumes and Courant numbers.

$$
\dot m_i=-[(a-w)q]_{i+1/2}+[(a-w)q]_{i-1/2},\quad V_i=x_{i+1/2}-x_{i-1/2}
$$

$$
x(\xi,t)=\xi+0.2\sin(2\pi\xi)\sin(2\pi t)/(2\pi)
$$

- [ALE scalar conservation on moving cells](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#ale-scalar-transport-en) (`ale-scalar-transport`)

Periodic unit interval, speed.7,q0=1+.2sin(2pi x), grid speed .2sin(2pi xi)cos(2pi t),N40/80/160,T1. Separate N40,T.25 time series32/64/128steps.


**Problem figure**

![ALE scalar transport on genuinely nonuniform moving cells: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/results/ale-nonuniform-transport.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[ALE scalar transport on genuinely nonuniform moving cells](https://hrkoyama.github.io/numerical-methods-atlas/problems/ale-nonuniform-transport/?lang=en) (`ale-nonuniform-transport`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/ale-nonuniform-transport/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/ale-nonuniform-transport/?lang=en#ale-nonuniform-transport-en-validation)

Separate analytic moving-cell-integral error, global/stage mass, constant GCL and geometry error. Qualify an independent DOP853 integration of the same FV ODE with two tolerances.

- [ALE: analytic moving-cell integrals and separate time reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-ale-nonuniform-transport-en) (`ale-nonuniform-transport`; Same-problem reference · Analytic reference)

First-stage1D prescribed mesh motion. The x–t image is not2D physics; Euler Lagrange/remap and Saltzman piston remain future work.
## Assumptions, units and boundaries

Periodic unit interval, speed.7,q0=1+.2sin(2pi x), grid speed .2sin(2pi xi)cos(2pi t),N40/80/160,T1. Separate N40,T.25 time series32/64/128steps.

**Editorial clarification**

First-stage1D prescribed mesh motion. The x–t image is not2D physics; Euler Lagrange/remap and Saltzman piston remain future work.

## Adopted numerical method

Upwind relative flux(a-w)q advances actual masses with identical predictor/corrector face geometry; record stage volumes and Courant numbers.

$$
\dot m_i=-[(a-w)q]_{i+1/2}+[(a-w)q]_{i-1/2},\quad V_i=x_{i+1/2}-x_{i-1/2}
$$

$$
x(\xi,t)=\xi+0.2\sin(2\pi\xi)\sin(2\pi t)/(2\pi)
$$

## References and validation

Separate analytic moving-cell-integral error, global/stage mass, constant GCL and geometry error. Qualify an independent DOP853 integration of the same FV ODE with two tolerances.

## Limits

First-stage1D prescribed mesh motion. The x–t image is not2D physics; Euler Lagrange/remap and Saltzman piston remain future work.

## Stored measurements and decisions

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

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/ale-nonuniform-transport/index.json

![Validation preview from actual saved PDE arrays and fixed-input refinement measurements.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/results/ale-nonuniform-transport-preview.png)

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

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

## Sources and review scope

- Dennis L. Huff (1987). Numerical Simulations of Unsteady, Viscous, Transonic Flow Over Isolated and Cascaded Airfoils Using a Deforming Grid. https://ntrs.nasa.gov/api/citations/19870015002/downloads/19870015002.pdf; review_level=selected-primary-report-grid-treatment
NASA TM89890 grid-velocity and GCL discussion around equation11/printedp5 inspected. It attributes GCL to Thomas/Lombard. Original1979 paper not read; no airfoil algorithm or code reproduced. Our 1D scalar moving-volume/Heun derivation is independent.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
