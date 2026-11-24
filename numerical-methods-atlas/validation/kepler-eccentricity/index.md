# 離心率を変えたKepler軌道と時間刻み

e=0.1/0.7の16固定軌道で、保存量と同時刻の位相誤差、実際の近日点時刻と逆積分を比較します。

**使用手法**

- [速度Verlet／粒子leapfrog法](https://hrkoyama.github.io/numerical-methods-atlas/methods/verlet/?lang=ja) (`verlet`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/kepler-eccentricity/?lang=ja#kepler-eccentricity-ja-algorithm)

独自の中心力KDK Verlet。固定・保存刻み再生・再生成刻みを区別し、cubic Hermite軌道の正の放射速度交差をbrentqで局在化。

$$
\ddot q=-q/\|q\|^3
$$

$$
E-e\sin E=t,\quad q=(\cos E-e,\sqrt{1-e^2}\sin E)
$$

$$
H=\tfrac12\|p\|^2-1/\|q\|
$$

- [Kepler二体問題](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#kepler-two-body-ja) (`kepler-two-body`)

a=μ=換算質量=1、軟化なし。1周期は512/1024/2048刻み、10周期は基準2048刻み/周期。変動刻みh=h0|q|を現在状態から定め、最後だけ物理終端へ短縮。

- [重力粒子モデル](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#particle-gravity-ja) (`particle-gravity`)

a=μ=換算質量=1、軟化なし。1周期は512/1024/2048刻み、10周期は基準2048刻み/周期。変動刻みh=h0|q|を現在状態から定め、最後だけ物理終端へ短縮。

- [Hamilton系・振動子](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#hamiltonian-ja) (`hamiltonian`)

a=μ=換算質量=1、軟化なし。1周期は512/1024/2048刻み、10周期は基準2048刻み/周期。変動刻みh=h0|q|を現在状態から定め、最後だけ物理終端へ短縮。


**問題の図**

![離心率を変えたKepler軌道と時間刻み：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/results/kepler-eccentricity.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[無軟化Kepler二体の時間誤差](https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-kepler/?lang=ja) (`gravity-kepler`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-kepler/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/kepler-eccentricity/?lang=ja#kepler-eccentricity-ja-validation)

独立のKepler方程式brentq／二分法解析族、92主判定。全状態誤差とエネルギー・角運動量、8回以上の近日点、有限窓の順序と反転誤差を検査。

- [無軟化Kepler二体の時間誤差](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-gravity-kepler-ja) (`gravity-kepler`; 同じ問題の参照 · 解析参照)

1周期・固定離心率のみ。軟化軌道や長時間安定性はこの参照の範囲外。

- [離心率を変えたKepler軌道と時間刻み](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-kepler-eccentricity-ja) (`kepler-eccentricity`; 同じ問題の参照 · 半解析参照)

保存量の小さい誤差から位相精度を推論しません。変動刻み写像の正準symplectic defectは測定せず、固定hの性質をそのまま移しません。初期解像度R1は数値実行前の漸近解析でR2へ改訂。
## 前提・単位・境界

a=μ=換算質量=1、軟化なし。1周期は512/1024/2048刻み、10周期は基準2048刻み/周期。変動刻みh=h0|q|を現在状態から定め、最後だけ物理終端へ短縮。

**編集上の補足**

保存量の小さい誤差から位相精度を推論しません。変動刻み写像の正準symplectic defectは測定せず、固定hの性質をそのまま移しません。初期解像度R1は数値実行前の漸近解析でR2へ改訂。 図の軌道・状態・時刻・反復の軸は、物理空間の次元を表しません。

## 採用した計算法

独自の中心力KDK Verlet。固定・保存刻み再生・再生成刻みを区別し、cubic Hermite軌道の正の放射速度交差をbrentqで局在化。

$$
\ddot q=-q/\|q\|^3
$$

$$
E-e\sin E=t,\quad q=(\cos E-e,\sqrt{1-e^2}\sin E)
$$

$$
H=\tfrac12\|p\|^2-1/\|q\|
$$

## 比較・検証

独立のKepler方程式brentq／二分法解析族、92主判定。全状態誤差とエネルギー・角運動量、8回以上の近日点、有限窓の順序と反転誤差を検査。

## 確認の限界

保存量の小さい誤差から位相精度を推論しません。変動刻み写像の正準symplectic defectは測定せず、固定hの性質をそのまま移しません。初期解像度R1は数値実行前の漸近解析でR2へ改訂。

## 保存実測値と判定

```json
{
  "metrics": {
    "e0.1_orders": [
      1.9999876782390122,
      1.9999962905452664
    ],
    "e0.7_orders": [
      1.987542094585538,
      2.000215589787777
    ],
    "evolution_count": 16,
    "variable_map_symplecticity_measured": false,
    "max_state_error": 0.39849708597264355
  },
  "checks": {
    "e0p1-fixed-512-finite": true,
    "e0p1-fixed-512-time": true,
    "e0p1-fixed-512-radius": true,
    "e0p1-fixed-512-angular": true,
    "e0p1-fixed-512-energy": true,
    "e0p1-fixed-512-reference": true,
    "e0p1-fixed-1024-finite": true,
    "e0p1-fixed-1024-time": true,
    "e0p1-fixed-1024-radius": true,
    "e0p1-fixed-1024-angular": true,
    "e0p1-fixed-1024-energy": true,
    "e0p1-fixed-1024-reference": true,
    "e0p1-fixed-2048-finite": true,
    "e0p1-fixed-2048-time": true,
    "e0p1-fixed-2048-radius": true,
    "e0p1-fixed-2048-angular": true,
    "e0p1-fixed-2048-energy": true,
    "e0p1-fixed-2048-reference": true,
    "e0p1-fixed-long-finite": true,
    "e0p1-fixed-long-time": true,
    "e0p1-fixed-long-radius": true,
    "e0p1-fixed-long-angular": true,
    "e0p1-fixed-long-energy": true,
    "e0p1-fixed-long-reference": true,
    "e0p1-fixed-long-periapsis-count": true,
    "e0p1-fixed-long-periapsis-time": true,
    "e0p1-variable-long-finite": true,
    "e0p1-variable-long-time": true,
    "e0p1-variable-long-radius": true,
    "e0p1-variable-long-angular": true,
    "e0p1-variable-long-energy": true,
    "e0p1-variable-long-reference": true,
    "e0p1-variable-long-periapsis-count": true,
    "e0p1-variable-long-periapsis-time": true,
    "e0p1-reverse-fixed-finite": true,
    "e0p1-reverse-fixed-schedule": true,
    "e0p1-reverse-fixed-recovery-or-diagnostic-scope": true,
    "e0p1-reverse-variable-replay-finite": true,
    "e0p1-reverse-variable-replay-schedule": true,
    "e0p1-reverse-variable-replay-recovery-or-diagnostic-scope": true,
    "e0p1-reverse-variable-regenerated-finite": true,
    "e0p1-reverse-variable-regenerated-schedule": true,
    "e0p1-reverse-variable-regenerated-recovery-or-diagnostic-scope": true,
    "e0p7-fixed-512-finite": true,
    "e0p7-fixed-512-time": true,
    "e0p7-fixed-512-radius": true,
    "e0p7-fixed-512-angular": true,
    "e0p7-fixed-512-energy": true,
    "e0p7-fixed-512-reference": true,
    "e0p7-fixed-1024-finite": true,
    "e0p7-fixed-1024-time": true,
    "e0p7-fixed-1024-radius": true,
    "e0p7-fixed-1024-angular": true,
    "e0p7-fixed-1024-energy": true,
    "e0p7-fixed-1024-reference": true,
    "e0p7-fixed-2048-finite": true,
    "e0p7-fixed-2048-time": true,
    "e0p7-fixed-2048-radius": true,
    "e0p7-fixed-2048-angular": true,
    "e0p7-fixed-2048-energy": true,
    "e0p7-fixed-2048-reference": true,
    "e0p7-fixed-long-finite": true,
    "e0p7-fixed-long-time": true,
    "e0p7-fixed-long-radius": true,
    "e0p7-fixed-long-angular": true,
    "e0p7-fixed-long-energy": true,
    "e0p7-fixed-long-reference": true,
    "e0p7-fixed-long-periapsis-count": true,
    "e0p7-fixed-long-periapsis-time": true,
    "e0p7-variable-long-finite": true,
    "e0p7-variable-long-time": true,
    "e0p7-variable-long-radius": true,
    "e0p7-variable-long-angular": true,
    "e0p7-variable-long-energy": true,
    "e0p7-variable-long-reference": true,
    "e0p7-variable-long-periapsis-count": true,
    "e0p7-variable-long-periapsis-time": true,
    "e0p7-reverse-fixed-finite": true,
    "e0p7-reverse-fixed-schedule": true,
    "e0p7-reverse-fixed-recovery-or-diagnostic-scope": true,
    "e0p7-reverse-variable-replay-finite": true,
    "e0p7-reverse-variable-replay-schedule": true,
    "e0p7-reverse-variable-replay-recovery-or-diagnostic-scope": true,
    "e0p7-reverse-variable-regenerated-finite": true,
    "e0p7-reverse-variable-regenerated-schedule": true,
    "e0p7-reverse-variable-regenerated-recovery-or-diagnostic-scope": true,
    "e0.1-fine-state": true,
    "e0.1-state-order": true,
    "e0.1-fine-energy": true,
    "e0.7-fine-state": true,
    "e0.7-state-order": true,
    "e0.7-fine-energy": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/kepler-eccentricity/index.json

![保存したe=0.7、10周期の固定刻み／変動刻み軌道。物理座標は等倍率で、中心力は軟化していません。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/results/kepler-eccentricity-preview.png)

保存したe=0.7、10周期の固定刻み／変動刻み軌道。物理座標は等倍率で、中心力は軟化していません。

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/atlas-geometric-controls-2026-11-24.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

## 出典と確認範囲

- Lecture2: Symplectic integrators [accessed 2026-11-24]. https://www.unige.ch/~hairer/poly_geoint/week2.pdf; review_level=selected-primary-scope
Author-hosted course notes, selected rendered printed pages2,12–13: Verlet kick/drift form, symplectic statement, Lie and symmetric Strang compositions. This does not qualify every state-dependent step rule or the authored coupled resonance experiment.

- Approximate Positions of the Planets [accessed 2026-11-24]. https://ssd.jpl.nasa.gov/planets/approx_pos.html; review_level=selected-primary-scope
Official JPL page, selected steps3–4 and Kepler equation. Only the eccentric-anomaly equation and elliptic coordinate transformation are used; no planetary coefficient tables, fitted ephemeris accuracy or Horizons calculation is claimed. Publication date was not verified.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Kepler eccentricity and time-step controls

Sixteen fixed evolutions at e=0.1/0.7 compare invariants, same-time phase error, physical periapsis times and reversal.

**Methods used**

- [Velocity Verlet / particle leapfrog](https://hrkoyama.github.io/numerical-methods-atlas/methods/verlet/?lang=en) (`verlet`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/kepler-eccentricity/?lang=en#kepler-eccentricity-en-algorithm)

Original central-force KDK Verlet. Fixed, replayed and regenerated schedules are distinct. Positive radial crossings of cubic Hermite trajectories are localized by brentq.

$$
\ddot q=-q/\|q\|^3
$$

$$
E-e\sin E=t,\quad q=(\cos E-e,\sqrt{1-e^2}\sin E)
$$

$$
H=\tfrac12\|p\|^2-1/\|q\|
$$

- [Kepler two-body problem](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#kepler-two-body-en) (`kepler-two-body`)

a=mu=reduced mass=1, without softening. One-period runs use 512/1024/2048 steps; ten-period controls use h0=2π/2048. Variable steps use h=h0|q| at the current state, with only the final step shortened to the physical endpoint.

- [Gravitational particle model](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#particle-gravity-en) (`particle-gravity`)

a=mu=reduced mass=1, without softening. One-period runs use 512/1024/2048 steps; ten-period controls use h0=2π/2048. Variable steps use h=h0|q| at the current state, with only the final step shortened to the physical endpoint.

- [Hamiltonian systems and oscillators](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#hamiltonian-en) (`hamiltonian`)

a=mu=reduced mass=1, without softening. One-period runs use 512/1024/2048 steps; ten-period controls use h0=2π/2048. Variable steps use h=h0|q| at the current state, with only the final step shortened to the physical endpoint.


**Problem figure**

![Kepler eccentricity and time-step controls: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/results/kepler-eccentricity.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Unsoftened Kepler two-body time error](https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-kepler/?lang=en) (`gravity-kepler`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-kepler/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/kepler-eccentricity/?lang=en#kepler-eccentricity-en-validation)

An independent Kepler-equation family, qualified with brentq and bisection, supports 92 main decisions: full-state error, energy/angular momentum, at least eight periapses, finite-window order and reversal defects.

- [Unsoftened Kepler two-body time error](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-gravity-kepler-en) (`gravity-kepler`; Same-problem reference · Analytic reference)

One orbit at fixed eccentricity only; softened binaries and long-time behavior are outside this exact reference.

- [Kepler eccentricity and time-step controls](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-kepler-eccentricity-en) (`kepler-eccentricity`; Same-problem reference · Semi-analytic reference)

Small invariant errors do not establish phase accuracy. No canonical symplectic-defect measurement is claimed for the variable-step map, and fixed-h properties are not transferred automatically. R1 resolution was revised to R2 using pre-execution asymptotic planning, not measured calibration.
## Assumptions, units and boundaries

a=mu=reduced mass=1, without softening. One-period runs use 512/1024/2048 steps; ten-period controls use h0=2π/2048. Variable steps use h=h0|q| at the current state, with only the final step shortened to the physical endpoint.

**Editorial clarification**

Small invariant errors do not establish phase accuracy. No canonical symplectic-defect measurement is claimed for the variable-step map, and fixed-h properties are not transferred automatically. R1 resolution was revised to R2 using pre-execution asymptotic planning, not measured calibration. Axes for trajectories, states, time or iterations do not represent physical spatial dimensions.

## Adopted numerical method

Original central-force KDK Verlet. Fixed, replayed and regenerated schedules are distinct. Positive radial crossings of cubic Hermite trajectories are localized by brentq.

$$
\ddot q=-q/\|q\|^3
$$

$$
E-e\sin E=t,\quad q=(\cos E-e,\sqrt{1-e^2}\sin E)
$$

$$
H=\tfrac12\|p\|^2-1/\|q\|
$$

## References and validation

An independent Kepler-equation family, qualified with brentq and bisection, supports 92 main decisions: full-state error, energy/angular momentum, at least eight periapses, finite-window order and reversal defects.

## Limits

Small invariant errors do not establish phase accuracy. No canonical symplectic-defect measurement is claimed for the variable-step map, and fixed-h properties are not transferred automatically. R1 resolution was revised to R2 using pre-execution asymptotic planning, not measured calibration.

## Stored measurements and decisions

```json
{
  "metrics": {
    "e0.1_orders": [
      1.9999876782390122,
      1.9999962905452664
    ],
    "e0.7_orders": [
      1.987542094585538,
      2.000215589787777
    ],
    "evolution_count": 16,
    "variable_map_symplecticity_measured": false,
    "max_state_error": 0.39849708597264355
  },
  "checks": {
    "e0p1-fixed-512-finite": true,
    "e0p1-fixed-512-time": true,
    "e0p1-fixed-512-radius": true,
    "e0p1-fixed-512-angular": true,
    "e0p1-fixed-512-energy": true,
    "e0p1-fixed-512-reference": true,
    "e0p1-fixed-1024-finite": true,
    "e0p1-fixed-1024-time": true,
    "e0p1-fixed-1024-radius": true,
    "e0p1-fixed-1024-angular": true,
    "e0p1-fixed-1024-energy": true,
    "e0p1-fixed-1024-reference": true,
    "e0p1-fixed-2048-finite": true,
    "e0p1-fixed-2048-time": true,
    "e0p1-fixed-2048-radius": true,
    "e0p1-fixed-2048-angular": true,
    "e0p1-fixed-2048-energy": true,
    "e0p1-fixed-2048-reference": true,
    "e0p1-fixed-long-finite": true,
    "e0p1-fixed-long-time": true,
    "e0p1-fixed-long-radius": true,
    "e0p1-fixed-long-angular": true,
    "e0p1-fixed-long-energy": true,
    "e0p1-fixed-long-reference": true,
    "e0p1-fixed-long-periapsis-count": true,
    "e0p1-fixed-long-periapsis-time": true,
    "e0p1-variable-long-finite": true,
    "e0p1-variable-long-time": true,
    "e0p1-variable-long-radius": true,
    "e0p1-variable-long-angular": true,
    "e0p1-variable-long-energy": true,
    "e0p1-variable-long-reference": true,
    "e0p1-variable-long-periapsis-count": true,
    "e0p1-variable-long-periapsis-time": true,
    "e0p1-reverse-fixed-finite": true,
    "e0p1-reverse-fixed-schedule": true,
    "e0p1-reverse-fixed-recovery-or-diagnostic-scope": true,
    "e0p1-reverse-variable-replay-finite": true,
    "e0p1-reverse-variable-replay-schedule": true,
    "e0p1-reverse-variable-replay-recovery-or-diagnostic-scope": true,
    "e0p1-reverse-variable-regenerated-finite": true,
    "e0p1-reverse-variable-regenerated-schedule": true,
    "e0p1-reverse-variable-regenerated-recovery-or-diagnostic-scope": true,
    "e0p7-fixed-512-finite": true,
    "e0p7-fixed-512-time": true,
    "e0p7-fixed-512-radius": true,
    "e0p7-fixed-512-angular": true,
    "e0p7-fixed-512-energy": true,
    "e0p7-fixed-512-reference": true,
    "e0p7-fixed-1024-finite": true,
    "e0p7-fixed-1024-time": true,
    "e0p7-fixed-1024-radius": true,
    "e0p7-fixed-1024-angular": true,
    "e0p7-fixed-1024-energy": true,
    "e0p7-fixed-1024-reference": true,
    "e0p7-fixed-2048-finite": true,
    "e0p7-fixed-2048-time": true,
    "e0p7-fixed-2048-radius": true,
    "e0p7-fixed-2048-angular": true,
    "e0p7-fixed-2048-energy": true,
    "e0p7-fixed-2048-reference": true,
    "e0p7-fixed-long-finite": true,
    "e0p7-fixed-long-time": true,
    "e0p7-fixed-long-radius": true,
    "e0p7-fixed-long-angular": true,
    "e0p7-fixed-long-energy": true,
    "e0p7-fixed-long-reference": true,
    "e0p7-fixed-long-periapsis-count": true,
    "e0p7-fixed-long-periapsis-time": true,
    "e0p7-variable-long-finite": true,
    "e0p7-variable-long-time": true,
    "e0p7-variable-long-radius": true,
    "e0p7-variable-long-angular": true,
    "e0p7-variable-long-energy": true,
    "e0p7-variable-long-reference": true,
    "e0p7-variable-long-periapsis-count": true,
    "e0p7-variable-long-periapsis-time": true,
    "e0p7-reverse-fixed-finite": true,
    "e0p7-reverse-fixed-schedule": true,
    "e0p7-reverse-fixed-recovery-or-diagnostic-scope": true,
    "e0p7-reverse-variable-replay-finite": true,
    "e0p7-reverse-variable-replay-schedule": true,
    "e0p7-reverse-variable-replay-recovery-or-diagnostic-scope": true,
    "e0p7-reverse-variable-regenerated-finite": true,
    "e0p7-reverse-variable-regenerated-schedule": true,
    "e0p7-reverse-variable-regenerated-recovery-or-diagnostic-scope": true,
    "e0.1-fine-state": true,
    "e0.1-state-order": true,
    "e0.1-fine-energy": true,
    "e0.7-fine-state": true,
    "e0.7-state-order": true,
    "e0.7-fine-energy": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/kepler-eccentricity/index.json

![Saved ten-period fixed-step and variable-step orbits at e=0.7, shown with equal physical aspect and an unsoftened central force.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/results/kepler-eccentricity-preview.png)

Saved ten-period fixed-step and variable-step orbits at e=0.7, shown with equal physical aspect and an unsoftened central force.

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/atlas-geometric-controls-2026-11-24.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

## Sources and review scope

- Lecture2: Symplectic integrators [accessed 2026-11-24]. https://www.unige.ch/~hairer/poly_geoint/week2.pdf; review_level=selected-primary-scope
Author-hosted course notes, selected rendered printed pages2,12–13: Verlet kick/drift form, symplectic statement, Lie and symmetric Strang compositions. This does not qualify every state-dependent step rule or the authored coupled resonance experiment.

- Approximate Positions of the Planets [accessed 2026-11-24]. https://ssd.jpl.nasa.gov/planets/approx_pos.html; review_level=selected-primary-scope
Official JPL page, selected steps3–4 and Kepler equation. Only the eccentric-anomaly equation and elliptic coordinate transformation are used; no planetary coefficient tables, fitted ephemeris accuracy or Horizons calculation is claimed. Publication date was not verified.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
