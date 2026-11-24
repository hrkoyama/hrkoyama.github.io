# Lotka–Volterra不変量と正値性

正の軌道を独立な対数座標参照と比較します。

**使用手法**

- [古典的RK4](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=ja) (`rk4`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/lotka-volterra/?lang=ja#lotka-volterra-ja-algorithm)

固定400/800/1600ステップの古典RK4で物理状態を積分します。独立参照はlog x・log yの変数でRadau/BDFを実行し、主計算には対数変数や保存量の射影を導入しません。

$$
\dot x=x(1-y),\quad\dot y=y(x-1),\quad(x(0),y(0))=(1.2,0.8),\quad0\le t\le20
$$

$$
H(x,y)=x-\log x+y-\log y,\quad\frac{dH}{dt}=0\quad(x>0,y>0)
$$

$$
\frac{d\log x}{dt}=1-e^{\log y},\quad\frac{d\log y}{dt}=e^{\log x}-1
$$

- [Lotka–Volterra捕食・被食](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-lotka-volterra-ja) (`bio-lotka-volterra`)

無次元の捕食者・被食者系x′=x(1−y)、y′=y(x−1)、初期値(1.2,0.8)、0≤t≤20。正の象限で不変量H=x−log x+y−log yを評価します。


**問題の図**

![Lotka–Volterra不変量と正値性：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/lotka-volterra.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Lotka–Volterra不変量と正値性](https://hrkoyama.github.io/numerical-methods-atlas/problems/lotka-volterra/?lang=ja) (`lotka-volterra`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/lotka-volterra/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/lotka-volterra/?lang=ja#lotka-volterra-ja-validation)

独立参照との状態誤差、Hのドリフト、保存された軌道の最小値を別々に測定。参照側では解析Jacobian、Radau/BDF差、刻み精度、Hの時間微分の恒等式を事前資格しています。

- [Lotka–Volterra不変量と正値性](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-lotka-volterra-ja) (`lotka-volterra`; 同じ問題の参照 · 有限格子の数値参照)

1初期値・有限時間の固定比較です。連続系の閉軌道を引き込み極限周期とは呼びません。RK4の厳密な不変量保存、任意刻みでの正値性、長時間の構造保存は保証しません。
## 前提・単位・境界

無次元の捕食者・被食者系x′=x(1−y)、y′=y(x−1)、初期値(1.2,0.8)、0≤t≤20。正の象限で不変量H=x−log x+y−log yを評価します。

**編集上の補足**

1初期値・有限時間の固定比較です。連続系の閉軌道を引き込み極限周期とは呼びません。RK4の厳密な不変量保存、任意刻みでの正値性、長時間の構造保存は保証しません。 時間・濃度・個体数の軸は空間次元ではありません。率は教育用で疾病・実験予測ではありません。

## 採用した計算法

固定400/800/1600ステップの古典RK4で物理状態を積分します。独立参照はlog x・log yの変数でRadau/BDFを実行し、主計算には対数変数や保存量の射影を導入しません。

$$
\dot x=x(1-y),\quad\dot y=y(x-1),\quad(x(0),y(0))=(1.2,0.8),\quad0\le t\le20
$$

$$
H(x,y)=x-\log x+y-\log y,\quad\frac{dH}{dt}=0\quad(x>0,y>0)
$$

$$
\frac{d\log x}{dt}=1-e^{\log y},\quad\frac{d\log y}{dt}=e^{\log x}-1
$$

## 比較・検証

独立参照との状態誤差、Hのドリフト、保存された軌道の最小値を別々に測定。参照側では解析Jacobian、Radau/BDF差、刻み精度、Hの時間微分の恒等式を事前資格しています。

## 確認の限界

1初期値・有限時間の固定比較です。連続系の閉軌道を引き込み極限周期とは呼びません。RK4の厳密な不変量保存、任意刻みでの正値性、長時間の構造保存は保証しません。

## 元の数値目標と未達の結果

実行・記録の検証合格は、元の精度目標の全達成を意味しません。元の判定を保持します。

```json
{
  "original_target_results": {
    "lv-400:state": true,
    "lv-400:invariant": true,
    "lv-800:state": true,
    "lv-800:invariant": true,
    "lv-1600:state": true,
    "lv-1600:invariant": true
  },
  "original_target_summary": {
    "met": 6,
    "total": 6,
    "all_met": true,
    "acceptance_sha256": "b468e78459cf81bda6a32cade0051f6615b44def256c66308ae7acc82ff516ce"
  }
}
```

## 保存実測値と判定

```json
{
  "metrics": {
    "actual_primary_records": 3,
    "reference_role": "Qualified Radau/BDF full ODE; reduction/linearization errors are distinct modeling diagnostics"
  },
  "checks": {
    "lv-400:actual-grid-finite": true,
    "lv-800:actual-grid-finite": true,
    "lv-1600:actual-grid-finite": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/lotka-volterra/index.json

![正の軌道を独立な対数座標参照と比較します。 保存値だけを描画します。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/lotka-volterra-preview.png)

正の軌道を独立な対数座標参照と比較します。 保存値だけを描画します。

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

- Experiments in MATLAB, Chapter16: Predator-Prey Model [accessed 2026-11-24]. https://www.mathworks.com/content/dam/mathworks/mathworks-dot-com/moler/exm/chapters/predprey.pdf; review_level=selected-primary-body
Selected extracted text pp3–6: normalized LV equations, equilibrium, periodic-orbit discussion and numerical illustration. No original Lotka/Volterra paper read.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Lotka–Volterra invariant and positivity

Compare a positive orbit against an independently integrated log-coordinate reference.

**Methods used**

- [Classical RK4](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=en) (`rk4`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/lotka-volterra/?lang=en#lotka-volterra-en-algorithm)

Integrate physical populations with classical RK4 at 400, 800 and 1600 fixed steps. Independent Radau/BDF references evolve log x and log y; the primary method uses neither a log-coordinate update nor invariant projection.

$$
\dot x=x(1-y),\quad\dot y=y(x-1),\quad(x(0),y(0))=(1.2,0.8),\quad0\le t\le20
$$

$$
H(x,y)=x-\log x+y-\log y,\quad\frac{dH}{dt}=0\quad(x>0,y>0)
$$

$$
\frac{d\log x}{dt}=1-e^{\log y},\quad\frac{d\log y}{dt}=e^{\log x}-1
$$

- [Lotka–Volterra predator–prey](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-lotka-volterra-en) (`bio-lotka-volterra`)

Use the dimensionless predator–prey equations x′=x(1−y), y′=y(x−1), initial state (1.2,0.8) and 0≤t≤20. Evaluate H=x−log x+y−log y only in the positive quadrant.


**Problem figure**

![Lotka–Volterra invariant and positivity: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/lotka-volterra.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Lotka–Volterra invariant and positivity](https://hrkoyama.github.io/numerical-methods-atlas/problems/lotka-volterra/?lang=en) (`lotka-volterra`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/lotka-volterra/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/lotka-volterra/?lang=en#lotka-volterra-en-validation)

Measure state error against the independent reference, drift of H and the minimum saved population separately. The reference stage qualifies analytic Jacobians, Radau/BDF agreement, tolerance refinement and the identity dH/dt=0.

- [Lotka–Volterra invariant and positivity](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-lotka-volterra-en) (`lotka-volterra`; Same-problem reference · Finite-grid numerical reference)

This is a finite-time comparison for one initial state. The continuum closed orbit is not an attracting limit cycle. RK4 is not claimed to preserve H exactly, maintain positivity at arbitrary steps or guarantee long-time geometric fidelity.
## Assumptions, units and boundaries

Use the dimensionless predator–prey equations x′=x(1−y), y′=y(x−1), initial state (1.2,0.8) and 0≤t≤20. Evaluate H=x−log x+y−log y only in the positive quadrant.

**Editorial clarification**

This is a finite-time comparison for one initial state. The continuum closed orbit is not an attracting limit cycle. RK4 is not claimed to preserve H exactly, maintain positivity at arbitrary steps or guarantee long-time geometric fidelity. Time, concentrations and populations do not define a spatial dimension. The rates are educational, not disease or experimental predictions.

## Adopted numerical method

Integrate physical populations with classical RK4 at 400, 800 and 1600 fixed steps. Independent Radau/BDF references evolve log x and log y; the primary method uses neither a log-coordinate update nor invariant projection.

$$
\dot x=x(1-y),\quad\dot y=y(x-1),\quad(x(0),y(0))=(1.2,0.8),\quad0\le t\le20
$$

$$
H(x,y)=x-\log x+y-\log y,\quad\frac{dH}{dt}=0\quad(x>0,y>0)
$$

$$
\frac{d\log x}{dt}=1-e^{\log y},\quad\frac{d\log y}{dt}=e^{\log x}-1
$$

## References and validation

Measure state error against the independent reference, drift of H and the minimum saved population separately. The reference stage qualifies analytic Jacobians, Radau/BDF agreement, tolerance refinement and the identity dH/dt=0.

## Limits

This is a finite-time comparison for one initial state. The continuum closed orbit is not an attracting limit cycle. RK4 is not claimed to preserve H exactly, maintain positivity at arbitrary steps or guarantee long-time geometric fidelity.

## Original numerical targets and unmet outcomes

Passing reproduction/reporting verification does not mean that all original accuracy goals were met. Original decisions are retained.

```json
{
  "original_target_results": {
    "lv-400:state": true,
    "lv-400:invariant": true,
    "lv-800:state": true,
    "lv-800:invariant": true,
    "lv-1600:state": true,
    "lv-1600:invariant": true
  },
  "original_target_summary": {
    "met": 6,
    "total": 6,
    "all_met": true,
    "acceptance_sha256": "b468e78459cf81bda6a32cade0051f6615b44def256c66308ae7acc82ff516ce"
  }
}
```

## Stored measurements and decisions

```json
{
  "metrics": {
    "actual_primary_records": 3,
    "reference_role": "Qualified Radau/BDF full ODE; reduction/linearization errors are distinct modeling diagnostics"
  },
  "checks": {
    "lv-400:actual-grid-finite": true,
    "lv-800:actual-grid-finite": true,
    "lv-1600:actual-grid-finite": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/lotka-volterra/index.json

![Compare a positive orbit against an independently integrated log-coordinate reference. This figure reads saved data only.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/lotka-volterra-preview.png)

Compare a positive orbit against an independently integrated log-coordinate reference. This figure reads saved data only.

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

- Experiments in MATLAB, Chapter16: Predator-Prey Model [accessed 2026-11-24]. https://www.mathworks.com/content/dam/mathworks/mathworks-dot-com/moler/exm/chapters/predprey.pdf; review_level=selected-primary-body
Selected extracted text pp3–6: normalized LV equations, equilibrium, periodic-orbit discussion and numerical illustration. No original Lotka/Volterra paper read.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
