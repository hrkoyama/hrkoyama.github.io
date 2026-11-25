# Fisher–KPP：特殊波速の厳密前線

波形・位置・格子誤差・時間誤差・有限領域の影響を分けます。

**使用手法**

- [SSPRK(3,3)](https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk33/?lang=ja) (`ssprk33`)
- [Dormand–Prince RK45](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk45/?lang=ja) (`rk45`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/fisher-kpp-special-front/?lang=ja#fisher-kpp-special-front-ja-algorithm)

2次中心差分とSSPRK3で計算し、厳密Dirichlet値を各段の時刻で与えます。時間誤差は同じ95未知数の半離散ODE参照と比較します。

$$
u_t=u_{xx}+u(1-u)
$$

$$
u(x,t)=[1+\exp((x-5t/\sqrt6)/\sqrt6)]^{-2}
$$

- [Fisher–KPP侵入前線](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-fisher-kpp-ja) (`bio-fisher-kpp`)

D=r=1、T=1。Ablowitz–Zeppetella型の特殊波速5/√6、L=12の空間・時間系列、定数端点L=6/12/24の境界比較を固定します。


**問題の図**

![Fisher–KPP：特殊波速の厳密前線：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/fisher-kpp-special-front.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Fisher–KPP：特殊波速の厳密前線](https://hrkoyama.github.io/numerical-methods-atlas/problems/fisher-kpp-special-front/?lang=ja) (`fisher-kpp-special-front`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/fisher-kpp-special-front/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/fisher-kpp-special-front/?lang=ja#fisher-kpp-special-front-ja-validation)

厳密波形と1/4等値線、同一格子の時間収束、全域と中央領域の境界誤差を別保存します。実数算術の離散障壁と、実測した浮動小数点の余裕を区別します。

- [Fisher–KPP：特殊波速の厳密前線](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-fisher-kpp-special-front-ja) (`fisher-kpp-special-front`; 同じ問題の参照 · 解析参照)

特殊前線を一般の最小速度2の前線と同一視しません。急減衰初期値からの速度選択、長時間伝播、機械誤差込みの厳密障壁証明は対象外です。
## 前提・単位・境界

D=r=1、T=1。Ablowitz–Zeppetella型の特殊波速5/√6、L=12の空間・時間系列、定数端点L=6/12/24の境界比較を固定します。

**編集上の補足**

特殊前線を一般の最小速度2の前線と同一視しません。急減衰初期値からの速度選択、長時間伝播、機械誤差込みの厳密障壁証明は対象外です。

## 採用した計算法

2次中心差分とSSPRK3で計算し、厳密Dirichlet値を各段の時刻で与えます。時間誤差は同じ95未知数の半離散ODE参照と比較します。

$$
u_t=u_{xx}+u(1-u)
$$

$$
u(x,t)=[1+\exp((x-5t/\sqrt6)/\sqrt6)]^{-2}
$$

## 比較・検証

厳密波形と1/4等値線、同一格子の時間収束、全域と中央領域の境界誤差を別保存します。実数算術の離散障壁と、実測した浮動小数点の余裕を区別します。

## 確認の限界

特殊前線を一般の最小速度2の前線と同一視しません。急減衰初期値からの速度選択、長時間伝播、機械誤差込みの厳密障壁証明は対象外です。

## 調査した目標：達成6・未達0・未確定0（全6）

必須の検証合格と元の調査目標の達成は別です。達成・未達は保存された比較結果を示し、統計的な認定ではありません。未確定と別の不確かさ区分を保持し、nullをfalseや0に置き換えません。

[元の保存結果 / JSON](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/result.json)

<details><summary>全目標の記録を読む</summary>

```json
{
  "schema_version": 1,
  "counts": {
    "met": 6,
    "unmet": 0,
    "unresolved": 0,
    "total": 6
  },
  "goals": [
    {
      "name": "Fisher/space-finest",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 9.239320837961529e-06,
        "target": 0.001
      }
    },
    {
      "name": "Fisher/space-order",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 1.9958436278085308,
        "target": 1.7
      }
    },
    {
      "name": "Fisher/phase",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.0002657675674280213,
        "target": 0.02
      }
    },
    {
      "name": "Fisher/time-order",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 3.0607173908690903,
        "target": 2.7,
        "reference_spread": 2.886579864025407e-15
      }
    },
    {
      "name": "Fisher/time-finest",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 1.8780066390888805e-10,
        "target": 1e-05
      }
    },
    {
      "name": "Fisher/observed-boundary-margin",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "observed_margin": 9.999999795441408e-05,
        "scope": "Observed binary64 margin; analyticreal-arithmetic barrier is not a machine-error certificate"
      }
    }
  ],
  "classification_basis": "stored observed comparison; separate uncertainty classifications retained",
  "source": {
    "collection": "study_goals",
    "json_pointer": "/study_goals",
    "prefix": "Fisher/",
    "result_sha256": "090c187f89db9d05a2eb437eaf5e73b2dcf1e7600ef0163efd94bae4119cb6eb",
    "acceptance_sha256": "b2f1727f9f4e70c139af7d38c218608b369625ab8f5896d762b060f88432a117",
    "result_url": "https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/result.json",
    "acceptance_url": "https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/acceptance.json"
  }
}
```

</details>

## 保存実測値と判定

```json
{
  "metrics": {
    "fixed_records": 11,
    "Fisher/space-finest/actual": 9.239320837961529e-06,
    "Fisher/space-order/actual": 1.9958436278085308,
    "Fisher/phase/actual": 0.0002657675674280213,
    "Fisher/time-order/actual": 3.0607173908690903,
    "Fisher/time-finest/actual": 1.8780066390888805e-10,
    "Fisher/observed-boundary-margin/observed_margin": 9.999999795441408e-05
  },
  "checks": {
    "Fisher/exact-PDE": true,
    "Fisher/wrong-special-speed-detected": true,
    "Fisher/finite-space/0.5": true,
    "Fisher/finite-space/0.25": true,
    "Fisher/finite-space/0.125": true,
    "Fisher/semidiscrete-reference": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/fisher-kpp-special-front/index.json

![精度・参照・統計の実測値と未達目標を分けて表示します。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/fisher-kpp-special-front-diagnostics.png)

精度・参照・統計の実測値と未達目標を分けて表示します。

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/atlas-biology-space-controls-2026-11-25.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

## 出典と確認範囲

- Ablowitz–Zeppetella(1979), Explicit solutions of Fisher’s equation for a special wave speed. https://doi.org/10.1007/BF02462380; review_level=selected-primary-or-bibliographic-see-provenance
source-reading.jsonに実際の読取範囲と未読部分を記録。原著の全式・全図の再現とは主張しません。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Fisher–KPP: a special-speed exact front

Separate profile, phase, grid, time and finite-boundary errors.

**Methods used**

- [SSPRK(3,3)](https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk33/?lang=en) (`ssprk33`)
- [Dormand–Prince RK45](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk45/?lang=en) (`rk45`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/fisher-kpp-special-front/?lang=en#fisher-kpp-special-front-en-algorithm)

Use centered second-order differences and SSPRK3 with exact Dirichlet values at every stage. Compare time errors to an independent reference for the same95-unknown semidiscreteODE.

$$
u_t=u_{xx}+u(1-u)
$$

$$
u(x,t)=[1+\exp((x-5t/\sqrt6)/\sqrt6)]^{-2}
$$

- [Fisher–KPP invasion front](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-fisher-kpp-en) (`bio-fisher-kpp`)

Use D=r=1,T=1 and the special speed5/√6. Fix spatial/time series on L12 and constant-endpoint boundary rows at L6/12/24.


**Problem figure**

![Fisher–KPP: a special-speed exact front: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/fisher-kpp-special-front.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Fisher–KPP: a special-speed exact front](https://hrkoyama.github.io/numerical-methods-atlas/problems/fisher-kpp-special-front/?lang=en) (`fisher-kpp-special-front`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/fisher-kpp-special-front/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/fisher-kpp-special-front/?lang=en#fisher-kpp-special-front-en-validation)

Save exact-profile and quarter-contour errors, same-grid time convergence and full/core boundary errors. Distinguish a real-arithmetic discrete barrier from the observed floating-point margin.

- [Fisher–KPP: a special-speed exact front](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-fisher-kpp-special-front-en) (`fisher-kpp-special-front`; Same-problem reference · Analytic reference)

The special front is distinct from the minimum linear speed2. This is not a steep-data speed-selection study, long-time propagation result or certified machine-error barrier proof.
## Assumptions, units and boundaries

Use D=r=1,T=1 and the special speed5/√6. Fix spatial/time series on L12 and constant-endpoint boundary rows at L6/12/24.

**Editorial clarification**

The special front is distinct from the minimum linear speed2. This is not a steep-data speed-selection study, long-time propagation result or certified machine-error barrier proof.

## Adopted numerical method

Use centered second-order differences and SSPRK3 with exact Dirichlet values at every stage. Compare time errors to an independent reference for the same95-unknown semidiscreteODE.

$$
u_t=u_{xx}+u(1-u)
$$

$$
u(x,t)=[1+\exp((x-5t/\sqrt6)/\sqrt6)]^{-2}
$$

## References and validation

Save exact-profile and quarter-contour errors, same-grid time convergence and full/core boundary errors. Distinguish a real-arithmetic discrete barrier from the observed floating-point margin.

## Limits

The special front is distinct from the minimum linear speed2. This is not a steep-data speed-selection study, long-time propagation result or certified machine-error barrier proof.

## Study goals: 6 met, 0 unmet, 0 unresolved (6 total)

Mandatory qualification is separate from study-goal attainment. Met/unmet follow stored comparisons, not statistical certification. Unresolved and separate uncertainty classifications are retained; null is not replaced by false or zero.

[Original saved results / JSON](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/result.json)

<details><summary>Read every study-goal record</summary>

```json
{
  "schema_version": 1,
  "counts": {
    "met": 6,
    "unmet": 0,
    "unresolved": 0,
    "total": 6
  },
  "goals": [
    {
      "name": "Fisher/space-finest",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 9.239320837961529e-06,
        "target": 0.001
      }
    },
    {
      "name": "Fisher/space-order",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 1.9958436278085308,
        "target": 1.7
      }
    },
    {
      "name": "Fisher/phase",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.0002657675674280213,
        "target": 0.02
      }
    },
    {
      "name": "Fisher/time-order",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 3.0607173908690903,
        "target": 2.7,
        "reference_spread": 2.886579864025407e-15
      }
    },
    {
      "name": "Fisher/time-finest",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 1.8780066390888805e-10,
        "target": 1e-05
      }
    },
    {
      "name": "Fisher/observed-boundary-margin",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "observed_margin": 9.999999795441408e-05,
        "scope": "Observed binary64 margin; analyticreal-arithmetic barrier is not a machine-error certificate"
      }
    }
  ],
  "classification_basis": "stored observed comparison; separate uncertainty classifications retained",
  "source": {
    "collection": "study_goals",
    "json_pointer": "/study_goals",
    "prefix": "Fisher/",
    "result_sha256": "090c187f89db9d05a2eb437eaf5e73b2dcf1e7600ef0163efd94bae4119cb6eb",
    "acceptance_sha256": "b2f1727f9f4e70c139af7d38c218608b369625ab8f5896d762b060f88432a117",
    "result_url": "https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/result.json",
    "acceptance_url": "https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/acceptance.json"
  }
}
```

</details>

## Stored measurements and decisions

```json
{
  "metrics": {
    "fixed_records": 11,
    "Fisher/space-finest/actual": 9.239320837961529e-06,
    "Fisher/space-order/actual": 1.9958436278085308,
    "Fisher/phase/actual": 0.0002657675674280213,
    "Fisher/time-order/actual": 3.0607173908690903,
    "Fisher/time-finest/actual": 1.8780066390888805e-10,
    "Fisher/observed-boundary-margin/observed_margin": 9.999999795441408e-05
  },
  "checks": {
    "Fisher/exact-PDE": true,
    "Fisher/wrong-special-speed-detected": true,
    "Fisher/finite-space/0.5": true,
    "Fisher/finite-space/0.25": true,
    "Fisher/finite-space/0.125": true,
    "Fisher/semidiscrete-reference": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/fisher-kpp-special-front/index.json

![Separate actual accuracy,reference and statistical measurements,including unmet targets.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/fisher-kpp-special-front-diagnostics.png)

Separate actual accuracy,reference and statistical measurements,including unmet targets.

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/atlas-biology-space-controls-2026-11-25.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

## Sources and review scope

- Ablowitz–Zeppetella(1979), Explicit solutions of Fisher’s equation for a special wave speed. https://doi.org/10.1007/BF02462380; review_level=selected-primary-or-bibliographic-see-provenance
Actual selected read scopes and unread limits are recorded in source-reading.json; no full original-paper equation/figure reproduction claim.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
