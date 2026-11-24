# 酵素反応の保存と準定常近似

全4状態と準定常近似を比較し、初期層と積分誤差を分けます。

**使用手法**

- [L安定なSDIRK2](https://hrkoyama.github.io/numerical-methods-atlas/methods/sdirk2/?lang=ja) (`sdirk2`)
- [適応SDIRK2／ステップ倍分割](https://hrkoyama.github.io/numerical-methods-atlas/methods/step-doubling/?lang=ja) (`step-doubling`)
- [Armijo減衰Newton法](https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=ja) (`newton`)
- [古典的RK4](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=ja) (`rk4`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/enzyme-qssa/?lang=ja#enzyme-qssa-ja-algorithm)

全4状態をSDIRK2のstep doublingで積分し、各段のNewton法では同じ重み付きL∞残差とArmijo条件を使います。縮約Michaelis–Menten式はθ上の別RK4計算で求め、全系の積分誤差と近似モデル誤差を混同しません。

$$
\begin{aligned}\dot S&=-10ES+C,&\dot C&=10ES-2C,\\\dot E&=-10ES+2C,&\dot P&=C.\end{aligned}
$$

$$
E+C=E_0,\quad S+C+P=1,\quad K_m=\frac{k_{-1}+k_2}{k_1}=0.2
$$

$$
\theta=E_0t,\quad \varepsilon=\frac{E_0}{K_m+S_0}\in\left\{\frac1{120},\frac1{600}\right\}
$$

$$
\frac{dS_{\rm MM}}{d\theta}=-\frac{S_{\rm MM}}{0.2+S_{\rm MM}},\quad S_{\rm MM}+0.2\log S_{\rm MM}=1-\theta
$$

- [Michaelis–Mentenと完全酵素反応系](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-enzyme-ja) (`bio-enzyme`)

閉鎖反応E+S⇌C→E+Pを無次元化し、k₁=10、k₋₁=k₂=1、S₀=1、C₀=P₀=0、E₀=0.01/0.002。Kₘ=0.2、ε=E₀/(Kₘ+S₀)=1/120,1/600、θ=E₀t∈[0,0.5]です。


**問題の図**

![酵素反応の保存と準定常近似：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/enzyme-qssa.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[酵素反応の保存と準定常近似](https://hrkoyama.github.io/numerical-methods-atlas/problems/enzyme-qssa/?lang=ja) (`enzyme-qssa`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/enzyme-qssa/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/enzyme-qssa/?lang=ja#enzyme-qssa-ja-validation)

独立な全系Radau/BDF参照、縮約式の陰的スカラー恒等式、E+C=E₀とS+C+P=1、正値性、実際の採用・棄却・Newton作業を照合。初期層を含む全時間と、事前指定θ≥0.02の近似誤差を別保存します。

- [酵素反応の保存と準定常近似](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-enzyme-qssa-ja) (`enzyme-qssa`; 同じ問題の参照 · 有限格子の数値参照)

2つの小εと固定反応定数だけの教育例です。εは尺度比であり、その値だけを厳密なQSSA誤差上界とはしません。θ≥0.02を初期層終了の証明とは呼ばず、生体内の反応・観測値へ外挿しません。
## 前提・単位・境界

閉鎖反応E+S⇌C→E+Pを無次元化し、k₁=10、k₋₁=k₂=1、S₀=1、C₀=P₀=0、E₀=0.01/0.002。Kₘ=0.2、ε=E₀/(Kₘ+S₀)=1/120,1/600、θ=E₀t∈[0,0.5]です。

**編集上の補足**

2つの小εと固定反応定数だけの教育例です。εは尺度比であり、その値だけを厳密なQSSA誤差上界とはしません。θ≥0.02を初期層終了の証明とは呼ばず、生体内の反応・観測値へ外挿しません。 時間・濃度・個体数の軸は空間次元ではありません。率は教育用で疾病・実験予測ではありません。

## 採用した計算法

全4状態をSDIRK2のstep doublingで積分し、各段のNewton法では同じ重み付きL∞残差とArmijo条件を使います。縮約Michaelis–Menten式はθ上の別RK4計算で求め、全系の積分誤差と近似モデル誤差を混同しません。

$$
\begin{aligned}\dot S&=-10ES+C,&\dot C&=10ES-2C,\\\dot E&=-10ES+2C,&\dot P&=C.\end{aligned}
$$

$$
E+C=E_0,\quad S+C+P=1,\quad K_m=\frac{k_{-1}+k_2}{k_1}=0.2
$$

$$
\theta=E_0t,\quad \varepsilon=\frac{E_0}{K_m+S_0}\in\left\{\frac1{120},\frac1{600}\right\}
$$

$$
\frac{dS_{\rm MM}}{d\theta}=-\frac{S_{\rm MM}}{0.2+S_{\rm MM}},\quad S_{\rm MM}+0.2\log S_{\rm MM}=1-\theta
$$

## 比較・検証

独立な全系Radau/BDF参照、縮約式の陰的スカラー恒等式、E+C=E₀とS+C+P=1、正値性、実際の採用・棄却・Newton作業を照合。初期層を含む全時間と、事前指定θ≥0.02の近似誤差を別保存します。

## 確認の限界

2つの小εと固定反応定数だけの教育例です。εは尺度比であり、その値だけを厳密なQSSA誤差上界とはしません。θ≥0.02を初期層終了の証明とは呼ばず、生体内の反応・観測値へ外挿しません。

## 元の数値目標と未達の結果

実行・記録の検証合格は、元の精度目標の全達成を意味しません。元の判定を保持します。

```json
{
  "original_target_results": {
    "enzyme-01-r1e-06:integration": true,
    "enzyme-01-r1e-06:mass": true,
    "enzyme-01-r1e-06:negative-part": true,
    "enzyme-01-r1e-06:QSSA-model": true,
    "enzyme-01-r1e-08:integration": true,
    "enzyme-01-r1e-08:mass": true,
    "enzyme-01-r1e-08:negative-part": true,
    "enzyme-01-r1e-08:QSSA-model": true,
    "enzyme-002-r1e-06:integration": true,
    "enzyme-002-r1e-06:mass": true,
    "enzyme-002-r1e-06:negative-part": true,
    "enzyme-002-r1e-06:QSSA-model": true,
    "enzyme-002-r1e-08:integration": true,
    "enzyme-002-r1e-08:mass": true,
    "enzyme-002-r1e-08:negative-part": true,
    "enzyme-002-r1e-08:QSSA-model": true
  },
  "original_target_summary": {
    "met": 16,
    "total": 16,
    "all_met": true,
    "acceptance_sha256": "b468e78459cf81bda6a32cade0051f6615b44def256c66308ae7acc82ff516ce"
  }
}
```

## 保存実測値と判定

```json
{
  "metrics": {
    "actual_primary_records": 6,
    "reference_role": "Qualified Radau/BDF full ODE; reduction/linearization errors are distinct modeling diagnostics"
  },
  "checks": {
    "enzyme-01-r1e-06:completed-work": true,
    "enzyme-01-r1e-06:finite": true,
    "enzyme-01-r1e-08:completed-work": true,
    "enzyme-01-r1e-08:finite": true,
    "enzyme-002-r1e-06:completed-work": true,
    "enzyme-002-r1e-06:finite": true,
    "enzyme-002-r1e-08:completed-work": true,
    "enzyme-002-r1e-08:finite": true,
    "mm-200:finite": true,
    "mm-400:finite": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/enzyme-qssa/index.json

![全4状態と準定常近似を比較し、初期層と積分誤差を分けます。 保存値だけを描画します。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/enzyme-qssa-preview.png)

全4状態と準定常近似を比較し、初期層と積分誤差を分けます。 保存値だけを描画します。

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/atlas-small-models-2026-11-25.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

## 出典と確認範囲

- Rigorous estimates for the quasi-steady state approximation of the Michaelis–Menten reaction mechanism at low enzyme concentrations [accessed 2026-11-24]. https://arxiv.org/html/2305.12602v2; review_level=selected-primary-body
Selected §1 Eq(1)–(8) and selected discussion around transient-time estimates Eq(32); proofs and complete quantitative bounds unread.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Enzyme conservation and QSSA

Separate the initial layer, integration error and QSSA modeling error in a four-state enzyme mechanism.

**Methods used**

- [L-stable SDIRK2](https://hrkoyama.github.io/numerical-methods-atlas/methods/sdirk2/?lang=en) (`sdirk2`)
- [Adaptive SDIRK2 / step doubling](https://hrkoyama.github.io/numerical-methods-atlas/methods/step-doubling/?lang=en) (`step-doubling`)
- [Armijo-damped Newton](https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=en) (`newton`)
- [Classical RK4](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=en) (`rk4`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/enzyme-qssa/?lang=en#enzyme-qssa-en-algorithm)

Integrate all four states with SDIRK2 step doubling, using the same weighted L∞ residual for Newton convergence and Armijo backtracking. Evolve the reduced Michaelis–Menten equation separately with RK4 in θ, keeping integration error distinct from model-reduction error.

$$
\begin{aligned}\dot S&=-10ES+C,&\dot C&=10ES-2C,\\\dot E&=-10ES+2C,&\dot P&=C.\end{aligned}
$$

$$
E+C=E_0,\quad S+C+P=1,\quad K_m=\frac{k_{-1}+k_2}{k_1}=0.2
$$

$$
\theta=E_0t,\quad \varepsilon=\frac{E_0}{K_m+S_0}\in\left\{\frac1{120},\frac1{600}\right\}
$$

$$
\frac{dS_{\rm MM}}{d\theta}=-\frac{S_{\rm MM}}{0.2+S_{\rm MM}},\quad S_{\rm MM}+0.2\log S_{\rm MM}=1-\theta
$$

- [Michaelis–Menten and full enzyme kinetics](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-enzyme-en) (`bio-enzyme`)

Use the closed dimensionless reaction E+S⇌C→E+P with k₁=10, k₋₁=k₂=1, S₀=1, C₀=P₀=0 and E₀=0.01 or 0.002. Then Kₘ=0.2, ε=E₀/(Kₘ+S₀)=1/120 or 1/600, and θ=E₀t ranges from 0 to 0.5.


**Problem figure**

![Enzyme conservation and QSSA: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/enzyme-qssa.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Enzyme conservation and QSSA](https://hrkoyama.github.io/numerical-methods-atlas/problems/enzyme-qssa/?lang=en) (`enzyme-qssa`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/enzyme-qssa/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/enzyme-qssa/?lang=en#enzyme-qssa-en-validation)

Compare with independent full-system Radau/BDF references and an implicit scalar identity for the reduced equation. Check E+C=E₀, S+C+P=1, positivity and actual acceptance, rejection and Newton work. Retain both all-time errors including the initial layer and errors on the declared θ≥0.02 window.

- [Enzyme conservation and QSSA](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-enzyme-qssa-en) (`enzyme-qssa`; Same-problem reference · Finite-grid numerical reference)

These two small-ε fixed-rate examples are educational. ε is a scale ratio, not itself a certified QSSA error bound. The θ≥0.02 window is not a proof that the initial layer has ended, and the calculation is not an in-vivo prediction.
## Assumptions, units and boundaries

Use the closed dimensionless reaction E+S⇌C→E+P with k₁=10, k₋₁=k₂=1, S₀=1, C₀=P₀=0 and E₀=0.01 or 0.002. Then Kₘ=0.2, ε=E₀/(Kₘ+S₀)=1/120 or 1/600, and θ=E₀t ranges from 0 to 0.5.

**Editorial clarification**

These two small-ε fixed-rate examples are educational. ε is a scale ratio, not itself a certified QSSA error bound. The θ≥0.02 window is not a proof that the initial layer has ended, and the calculation is not an in-vivo prediction. Time, concentrations and populations do not define a spatial dimension. The rates are educational, not disease or experimental predictions.

## Adopted numerical method

Integrate all four states with SDIRK2 step doubling, using the same weighted L∞ residual for Newton convergence and Armijo backtracking. Evolve the reduced Michaelis–Menten equation separately with RK4 in θ, keeping integration error distinct from model-reduction error.

$$
\begin{aligned}\dot S&=-10ES+C,&\dot C&=10ES-2C,\\\dot E&=-10ES+2C,&\dot P&=C.\end{aligned}
$$

$$
E+C=E_0,\quad S+C+P=1,\quad K_m=\frac{k_{-1}+k_2}{k_1}=0.2
$$

$$
\theta=E_0t,\quad \varepsilon=\frac{E_0}{K_m+S_0}\in\left\{\frac1{120},\frac1{600}\right\}
$$

$$
\frac{dS_{\rm MM}}{d\theta}=-\frac{S_{\rm MM}}{0.2+S_{\rm MM}},\quad S_{\rm MM}+0.2\log S_{\rm MM}=1-\theta
$$

## References and validation

Compare with independent full-system Radau/BDF references and an implicit scalar identity for the reduced equation. Check E+C=E₀, S+C+P=1, positivity and actual acceptance, rejection and Newton work. Retain both all-time errors including the initial layer and errors on the declared θ≥0.02 window.

## Limits

These two small-ε fixed-rate examples are educational. ε is a scale ratio, not itself a certified QSSA error bound. The θ≥0.02 window is not a proof that the initial layer has ended, and the calculation is not an in-vivo prediction.

## Original numerical targets and unmet outcomes

Passing reproduction/reporting verification does not mean that all original accuracy goals were met. Original decisions are retained.

```json
{
  "original_target_results": {
    "enzyme-01-r1e-06:integration": true,
    "enzyme-01-r1e-06:mass": true,
    "enzyme-01-r1e-06:negative-part": true,
    "enzyme-01-r1e-06:QSSA-model": true,
    "enzyme-01-r1e-08:integration": true,
    "enzyme-01-r1e-08:mass": true,
    "enzyme-01-r1e-08:negative-part": true,
    "enzyme-01-r1e-08:QSSA-model": true,
    "enzyme-002-r1e-06:integration": true,
    "enzyme-002-r1e-06:mass": true,
    "enzyme-002-r1e-06:negative-part": true,
    "enzyme-002-r1e-06:QSSA-model": true,
    "enzyme-002-r1e-08:integration": true,
    "enzyme-002-r1e-08:mass": true,
    "enzyme-002-r1e-08:negative-part": true,
    "enzyme-002-r1e-08:QSSA-model": true
  },
  "original_target_summary": {
    "met": 16,
    "total": 16,
    "all_met": true,
    "acceptance_sha256": "b468e78459cf81bda6a32cade0051f6615b44def256c66308ae7acc82ff516ce"
  }
}
```

## Stored measurements and decisions

```json
{
  "metrics": {
    "actual_primary_records": 6,
    "reference_role": "Qualified Radau/BDF full ODE; reduction/linearization errors are distinct modeling diagnostics"
  },
  "checks": {
    "enzyme-01-r1e-06:completed-work": true,
    "enzyme-01-r1e-06:finite": true,
    "enzyme-01-r1e-08:completed-work": true,
    "enzyme-01-r1e-08:finite": true,
    "enzyme-002-r1e-06:completed-work": true,
    "enzyme-002-r1e-06:finite": true,
    "enzyme-002-r1e-08:completed-work": true,
    "enzyme-002-r1e-08:finite": true,
    "mm-200:finite": true,
    "mm-400:finite": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/enzyme-qssa/index.json

![Separate the initial layer, integration error and QSSA modeling error in a four-state enzyme mechanism. This figure reads saved data only.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/enzyme-qssa-preview.png)

Separate the initial layer, integration error and QSSA modeling error in a four-state enzyme mechanism. This figure reads saved data only.

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/atlas-small-models-2026-11-25.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

## Sources and review scope

- Rigorous estimates for the quasi-steady state approximation of the Michaelis–Menten reaction mechanism at low enzyme concentrations [accessed 2026-11-24]. https://arxiv.org/html/2305.12602v2; review_level=selected-primary-body
Selected §1 Eq(1)–(8) and selected discussion around transient-time estimates Eq(32); proofs and complete quantitative bounds unread.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
