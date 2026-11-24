# 無軟化Kepler二体の時間誤差

非等質量二体をKDKで1周し、独立Kepler方程式の位置・速度とエネルギー/角運動量を照合。

**使用手法**

- [速度Verlet／粒子leapfrog法](https://hrkoyama.github.io/numerical-methods-atlas/methods/verlet/?lang=ja) (`verlet`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-kepler/?lang=ja#gravity-kepler-ja-algorithm)

位置のみの力でkick半分→drift→kick半分。独立のbracketed Kepler rootと解析速度を使用。

$$
E-e\sin E=nt
$$

$$
r=a(\cos E-e,\sqrt{1-e^2}\sin E,0)
$$

$$
v^{n+1/2}=v^n+\tfrac12\Delta t\,a(x^n)
$$

- [重力粒子モデル](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#particle-gravity-ja) (`particle-gravity`)

G=M=a1,e.4,masses.6/.4、epsilon0、128/256/512steps、初期COM/P0。


**問題の図**

![無軟化Kepler二体の時間誤差：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/results/gravity-kepler.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[無軟化Kepler二体の時間誤差](https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-kepler/?lang=ja) (`gravity-kepler`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-kepler/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-kepler/?lang=ja#gravity-kepler-ja-validation)

位相/時間次数、全同期stepエネルギー、P/L/COM、独立pair力とroot残差。

- [無軟化Kepler二体の時間誤差](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-gravity-kepler-ja) (`gravity-kepler`; 同じ問題の参照 · 解析参照)

1周期・固定離心率のみ。軟化軌道や長時間安定性はこの参照の範囲外。

- [離心率を変えたKepler軌道と時間刻み](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-kepler-eccentricity-ja) (`kepler-eccentricity`; 同じ問題の参照 · 半解析参照)

保存量の小さい誤差から位相精度を推論しません。変動刻み写像の正準symplectic defectは測定せず、固定hの性質をそのまま移しません。初期解像度R1は数値実行前の漸近解析でR2へ改訂。
## 前提・単位・境界

G=M=a1,e.4,masses.6/.4、epsilon0、128/256/512steps、初期COM/P0。

**編集上の補足**

1周期・固定離心率のみ。軟化軌道や長時間安定性はこの参照の範囲外。

## 採用した計算法

位置のみの力でkick半分→drift→kick半分。独立のbracketed Kepler rootと解析速度を使用。

$$
E-e\sin E=nt
$$

$$
r=a(\cos E-e,\sqrt{1-e^2}\sin E,0)
$$

$$
v^{n+1/2}=v^n+\tfrac12\Delta t\,a(x^n)
$$

## 比較・検証

位相/時間次数、全同期stepエネルギー、P/L/COM、独立pair力とroot残差。

## 確認の限界

1周期・固定離心率のみ。軟化軌道や長時間安定性はこの参照の範囲外。

## 保存実測値と判定

```json
{
  "metrics": {
    "finest_position_error": 0.0016120499258598436,
    "finest_energy_drift": 0.00017450491925918854,
    "period": 6.283185307179586
  },
  "checks": {
    "s128 finite synchronized fields": true,
    "s128 fixed final time": true,
    "s128 positive pair separation": true,
    "s128 momentum_drift": true,
    "s128 angular_drift": true,
    "s128 com_drift": true,
    "s128 Kepler root residual": true,
    "s128 independent final pair force": true,
    "s256 finite synchronized fields": true,
    "s256 fixed final time": true,
    "s256 positive pair separation": true,
    "s256 momentum_drift": true,
    "s256 angular_drift": true,
    "s256 com_drift": true,
    "s256 Kepler root residual": true,
    "s256 independent final pair force": true,
    "s512 finite synchronized fields": true,
    "s512 fixed final time": true,
    "s512 positive pair separation": true,
    "s512 momentum_drift": true,
    "s512 angular_drift": true,
    "s512 com_drift": true,
    "s512 Kepler root residual": true,
    "s512 independent final pair force": true,
    "analytic reference energy identity": true,
    "analytic reference angular identity": true,
    "analytic reference COM identity": true,
    "time refinement 1": true,
    "time refinement 2": true,
    "finest Kepler position": true,
    "finest Kepler energy": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-kepler/index.json

![固定入力を実際に計算した保存配列からの検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/results/gravity-kepler-preview.png)

固定入力を実際に計算した保存配列からの検証図。

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/atlas-gravity-dynamics-2026-11-23.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

## 出典と確認範囲

- JPL Keplerian-element formulas. https://ssd.jpl.nasa.gov/planets/approx_pos.html; review_level=official-selected-kepler-equation
Kepler equation and orbital-plane Cartesian conversion inspected only. No planetary fitting coefficients or approximate planetary ephemeris used. Fixed two-body positions/velocities are independently derived.

- Geometric numerical integration illustrated by the Störmer–Verlet method. https://doi.org/10.1017/S0962492902000144; review_level=bibliography-and-failed-author-pdf
Author/publisher metadata only; author PDF unavailable. KDK composition and reversibility are independently derived here; no original full-text audit or BH symplecticity claim.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Unsoftened Kepler two-body time error

Advance an unequal-mass binary for one orbit with KDK and compare independent Kepler positions/velocities and conservation.

**Methods used**

- [Velocity Verlet / particle leapfrog](https://hrkoyama.github.io/numerical-methods-atlas/methods/verlet/?lang=en) (`verlet`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-kepler/?lang=en#gravity-kepler-en-algorithm)

Position-only kick-half/drift/kick-half; separate bracketed Kepler root and analytic velocities.

$$
E-e\sin E=nt
$$

$$
r=a(\cos E-e,\sqrt{1-e^2}\sin E,0)
$$

$$
v^{n+1/2}=v^n+\tfrac12\Delta t\,a(x^n)
$$

- [Gravitational particle model](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#particle-gravity-en) (`particle-gravity`)

G=M=a1,e.4,masses.6/.4,epsilon0,128/256/512steps,initialCOM/P0.


**Problem figure**

![Unsoftened Kepler two-body time error: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/results/gravity-kepler.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Unsoftened Kepler two-body time error](https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-kepler/?lang=en) (`gravity-kepler`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-kepler/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-kepler/?lang=en#gravity-kepler-en-validation)

Time refinement/phase, synchronized all-step energy,P/L/COM,independent pair force and root residuals.

- [Unsoftened Kepler two-body time error](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-gravity-kepler-en) (`gravity-kepler`; Same-problem reference · Analytic reference)

One orbit at fixed eccentricity only; softened binaries and long-time behavior are outside this exact reference.

- [Kepler eccentricity and time-step controls](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-kepler-eccentricity-en) (`kepler-eccentricity`; Same-problem reference · Semi-analytic reference)

Small invariant errors do not establish phase accuracy. No canonical symplectic-defect measurement is claimed for the variable-step map, and fixed-h properties are not transferred automatically. R1 resolution was revised to R2 using pre-execution asymptotic planning, not measured calibration.
## Assumptions, units and boundaries

G=M=a1,e.4,masses.6/.4,epsilon0,128/256/512steps,initialCOM/P0.

**Editorial clarification**

One orbit at fixed eccentricity only; softened binaries and long-time behavior are outside this exact reference.

## Adopted numerical method

Position-only kick-half/drift/kick-half; separate bracketed Kepler root and analytic velocities.

$$
E-e\sin E=nt
$$

$$
r=a(\cos E-e,\sqrt{1-e^2}\sin E,0)
$$

$$
v^{n+1/2}=v^n+\tfrac12\Delta t\,a(x^n)
$$

## References and validation

Time refinement/phase, synchronized all-step energy,P/L/COM,independent pair force and root residuals.

## Limits

One orbit at fixed eccentricity only; softened binaries and long-time behavior are outside this exact reference.

## Stored measurements and decisions

```json
{
  "metrics": {
    "finest_position_error": 0.0016120499258598436,
    "finest_energy_drift": 0.00017450491925918854,
    "period": 6.283185307179586
  },
  "checks": {
    "s128 finite synchronized fields": true,
    "s128 fixed final time": true,
    "s128 positive pair separation": true,
    "s128 momentum_drift": true,
    "s128 angular_drift": true,
    "s128 com_drift": true,
    "s128 Kepler root residual": true,
    "s128 independent final pair force": true,
    "s256 finite synchronized fields": true,
    "s256 fixed final time": true,
    "s256 positive pair separation": true,
    "s256 momentum_drift": true,
    "s256 angular_drift": true,
    "s256 com_drift": true,
    "s256 Kepler root residual": true,
    "s256 independent final pair force": true,
    "s512 finite synchronized fields": true,
    "s512 fixed final time": true,
    "s512 positive pair separation": true,
    "s512 momentum_drift": true,
    "s512 angular_drift": true,
    "s512 com_drift": true,
    "s512 Kepler root residual": true,
    "s512 independent final pair force": true,
    "analytic reference energy identity": true,
    "analytic reference angular identity": true,
    "analytic reference COM identity": true,
    "time refinement 1": true,
    "time refinement 2": true,
    "finest Kepler position": true,
    "finest Kepler energy": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-kepler/index.json

![Validation figure from actual saved fixed-input calculation arrays.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/results/gravity-kepler-preview.png)

Validation figure from actual saved fixed-input calculation arrays.

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/atlas-gravity-dynamics-2026-11-23.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

## Sources and review scope

- JPL Keplerian-element formulas. https://ssd.jpl.nasa.gov/planets/approx_pos.html; review_level=official-selected-kepler-equation
Kepler equation and orbital-plane Cartesian conversion inspected only. No planetary fitting coefficients or approximate planetary ephemeris used. Fixed two-body positions/velocities are independently derived.

- Geometric numerical integration illustrated by the Störmer–Verlet method. https://doi.org/10.1017/S0962492902000144; review_level=bibliography-and-failed-author-pdf
Author/publisher metadata only; author PDF unavailable. KDK composition and reversibility are independently derived here; no original full-text audit or BH symplecticity claim.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
