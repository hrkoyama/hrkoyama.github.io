# Hodgkin–Huxley：電位固定・静止平衡・発火

固定電位の解析ゲート解と、区分電流下の4状態系を照合します。

**使用手法**

- [古典的RK4](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=ja) (`rk4`)
- [Dormand–Prince RK45](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk45/?lang=ja) (`rk45`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/hodgkin-huxley-controls/?lang=ja#hodgkin-huxley-controls-ja-algorithm)

古典RK4を用い、電流の切り替わりでは全段の片側値を区間に帰属させます。ゲートの可除特異点、Decimal静止根、独立なDP5(4)/Cash–Karp参照を別に照合します。

$$
C_m\dot V=I-g_{Na}m^3h(V-E_{Na})-g_Kn^4(V-E_K)-g_L(V-E_L)
$$

$$
\dot z=\alpha_z(V)(1-z)-\beta_z(V)z
$$

- [Hodgkin–Huxley膜動態](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-hodgkin-huxley-ja) (`bio-hodgkin-huxley`)

6.3°C、ms/mV/µA cm⁻²。NEURON8.2.6の解析的な絶対電位規約を固定し、4電位×3刻み、静止20 ms、10–11 msの電流パルスを扱います。


**問題の図**

![Hodgkin–Huxley：電位固定・静止平衡・発火：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/results/hodgkin-huxley-controls.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Hodgkin–Huxley：電位固定・静止平衡・発火](https://hrkoyama.github.io/numerical-methods-atlas/problems/hodgkin-huxley-controls/?lang=ja) (`hodgkin-huxley-controls`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/hodgkin-huxley-controls/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/hodgkin-huxley-controls/?lang=ja#hodgkin-huxley-controls-ja-validation)

全採用時刻のゲート誤差、電位・ゲート範囲、採用端点の新しい微分を使うHermite発火時刻を保存。元の1e-8ゲート目標も未達を含めて表示します。

- [Hodgkin–Huxley：電位固定・静止平衡・発火](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-hodgkin-huxley-controls-ja) (`hodgkin-huxley-controls`; 同じ問題の参照 · 半解析参照)

1細胞膜の教育例です。元論文の電位規約、TABLE/cnexp実装、ケーブル伝播や生体実測の再現とは呼びません。区間内に括れない発火は捏造せず、静止根の一意性・区間Hurwitz安定性は主張しません。
## 前提・単位・境界

6.3°C、ms/mV/µA cm⁻²。NEURON8.2.6の解析的な絶対電位規約を固定し、4電位×3刻み、静止20 ms、10–11 msの電流パルスを扱います。

**編集上の補足**

1細胞膜の教育例です。元論文の電位規約、TABLE/cnexp実装、ケーブル伝播や生体実測の再現とは呼びません。区間内に括れない発火は捏造せず、静止根の一意性・区間Hurwitz安定性は主張しません。

## 採用した計算法

古典RK4を用い、電流の切り替わりでは全段の片側値を区間に帰属させます。ゲートの可除特異点、Decimal静止根、独立なDP5(4)/Cash–Karp参照を別に照合します。

$$
C_m\dot V=I-g_{Na}m^3h(V-E_{Na})-g_Kn^4(V-E_K)-g_L(V-E_L)
$$

$$
\dot z=\alpha_z(V)(1-z)-\beta_z(V)z
$$

## 比較・検証

全採用時刻のゲート誤差、電位・ゲート範囲、採用端点の新しい微分を使うHermite発火時刻を保存。元の1e-8ゲート目標も未達を含めて表示します。

## 確認の限界

1細胞膜の教育例です。元論文の電位規約、TABLE/cnexp実装、ケーブル伝播や生体実測の再現とは呼びません。区間内に括れない発火は捏造せず、静止根の一意性・区間Hurwitz安定性は主張しません。

## 調査した目標：達成9・未達1・未確定0（全10）

必須の検証合格と元の調査目標の達成は別です。達成・未達は保存された比較結果を示し、統計的な認定ではありません。未確定と別の不確かさ区分を保持し、nullをfalseや0に置き換えません。

[元の保存結果 / JSON](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/results/result.json)

<details><summary>全目標の記録を読む</summary>

```json
{
  "schema_version": 1,
  "counts": {
    "met": 9,
    "unmet": 1,
    "unresolved": 0,
    "total": 10
  },
  "goals": [
    {
      "name": "HH/clamp-original1e-8/-80.0",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 4.711626791498169e-08,
        "target": 1e-08,
        "scope": "Maximum over ALL accepted times and all three gates; unmet outcomes retained"
      }
    },
    {
      "name": "HH/clamp-original1e-8/-55.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 7.262476731106915e-11,
        "target": 1e-08,
        "scope": "Maximum over ALL accepted times and all three gates; unmet outcomes retained"
      }
    },
    {
      "name": "HH/clamp-original1e-8/-40.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 1.4916989865554342e-10,
        "target": 1e-08,
        "scope": "Maximum over ALL accepted times and all three gates; unmet outcomes retained"
      }
    },
    {
      "name": "HH/clamp-original1e-8/0.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 7.521943623522986e-09,
        "target": 1e-08,
        "scope": "Maximum over ALL accepted times and all three gates; unmet outcomes retained"
      }
    },
    {
      "name": "HH/rest/0.04",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "target_mV": 1e-07
      }
    },
    {
      "name": "HH/rest/0.02",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "target_mV": 1e-07
      }
    },
    {
      "name": "HH/rest/0.01",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "target_mV": 1e-07
      }
    },
    {
      "name": "HH/pulse-voltage",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.00010511156826709112,
        "target": 0.05,
        "reference_spread": 1.0302887432089847e-09
      }
    },
    {
      "name": "HH/pulse-gates",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 5.371951350419124e-08,
        "target": 0.0001
      }
    },
    {
      "name": "HH/pulse-event",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual_ms": 3.799796033376879e-08,
        "target_ms": 0.01,
        "reason": null,
        "scope": "ObservedHermiteeventcomparison;exactODEeventcompletenessnotcertified"
      }
    }
  ],
  "classification_basis": "stored observed comparison; separate uncertainty classifications retained",
  "source": {
    "collection": "study_goals",
    "json_pointer": "/study_goals",
    "prefix": "HH/",
    "result_sha256": "104875b041a43542ec5d1500003da8f5986983816e27ce3b88971d11d7b63149",
    "acceptance_sha256": "47bb2050ccf15b2d404c2a3e63047d11d8258dc6feb25dc1e2fc14c3863b72ab",
    "result_url": "https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/results/result.json",
    "acceptance_url": "https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/acceptance.json"
  }
}
```

</details>

## 保存実測値と判定

```json
{
  "metrics": {
    "fixed_records": 21,
    "HH/clamp-original1e-8/-80.0/actual": 4.711626791498169e-08,
    "HH/clamp-original1e-8/-55.0/actual": 7.262476731106915e-11,
    "HH/clamp-original1e-8/-40.0/actual": 1.4916989865554342e-10,
    "HH/clamp-original1e-8/0.0/actual": 7.521943623522986e-09,
    "HH/pulse-voltage/actual": 0.00010511156826709112,
    "HH/pulse-gates/actual": 5.371951350419124e-08,
    "HH/pulse-event/actual_ms": 3.799796033376879e-08
  },
  "checks": {
    "HH/rates_against_decimal": true,
    "HH/precision_companion": true,
    "HH/removable_singularities": true,
    "HH/rest_bracket_companion": true,
    "HH/owned_stage_edges": true,
    "HH/naive_jump_control_detected": true,
    "HH/clamp-finite-bounds/-80.0/0.04": true,
    "HH/clamp-finite-bounds/-80.0/0.02": true,
    "HH/clamp-finite-bounds/-80.0/0.01": true,
    "HH/clamp-finite-bounds/-55.0/0.04": true,
    "HH/clamp-finite-bounds/-55.0/0.02": true,
    "HH/clamp-finite-bounds/-55.0/0.01": true,
    "HH/clamp-finite-bounds/-40.0/0.04": true,
    "HH/clamp-finite-bounds/-40.0/0.02": true,
    "HH/clamp-finite-bounds/-40.0/0.01": true,
    "HH/clamp-finite-bounds/0.0/0.04": true,
    "HH/clamp-finite-bounds/0.0/0.02": true,
    "HH/clamp-finite-bounds/0.0/0.01": true,
    "HH/reference/rest": true,
    "HH/finite-gates/rest/0.04": true,
    "HH/finite-gates/rest/0.02": true,
    "HH/finite-gates/rest/0.01": true,
    "HH/reference/pulse": true,
    "HH/finite-gates/pulse/0.04": true,
    "HH/finite-gates/pulse/0.02": true,
    "HH/finite-gates/pulse/0.01": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/hodgkin-huxley-controls/index.json

![精度・参照・統計の実測値と未達目標を分けて表示します。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/results/hodgkin-huxley-controls-diagnostics.png)

精度・参照・統計の実測値と未達目標を分けて表示します。

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/atlas-biology-ode-controls-2026-11-25.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

## 出典と確認範囲

- NEURON8.2.6 analytic hh.mod. https://raw.githubusercontent.com/neuronsimulator/nrn/8.2.6/src/nrnoc/hh.mod; review_level=selected-primary-or-bibliographic-see-provenance
source-reading.jsonに実際の読取範囲と未読部分を記録。原著の全式・全図の再現とは主張しません。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Hodgkin–Huxley: clamps, rest and firing

Compare analytic clamp gates and a four-state system with segment-owned current.

**Methods used**

- [Classical RK4](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=en) (`rk4`)
- [Dormand–Prince RK45](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk45/?lang=en) (`rk45`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/hodgkin-huxley-controls/?lang=en#hodgkin-huxley-controls-en-algorithm)

Use classicalRK4 with all stages owned by each current segment. Separately qualify removable rate singularities, a Decimal rest root and independently written DP5(4)/Cash–Karp references.

$$
C_m\dot V=I-g_{Na}m^3h(V-E_{Na})-g_Kn^4(V-E_K)-g_L(V-E_L)
$$

$$
\dot z=\alpha_z(V)(1-z)-\beta_z(V)z
$$

- [Hodgkin–Huxley membrane dynamics](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-hodgkin-huxley-en) (`bio-hodgkin-huxley`)

Fix6.3°C and the NEURON8.2.6 analytic absolute-voltage convention in ms/mV/µA cm⁻². Use four clamp voltages, three steps, a20ms rest and a10–11ms pulse.


**Problem figure**

![Hodgkin–Huxley: clamps, rest and firing: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/results/hodgkin-huxley-controls.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Hodgkin–Huxley: clamps, rest and firing](https://hrkoyama.github.io/numerical-methods-atlas/problems/hodgkin-huxley-controls/?lang=en) (`hodgkin-huxley-controls`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/hodgkin-huxley-controls/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/hodgkin-huxley-controls/?lang=en#hodgkin-huxley-controls-en-validation)

Retain errors over all accepted times, voltage/gate ranges and Hermite firing events from fresh accepted-endpoint derivatives. Preserve the original1e-8clamp goal even when unmet.

- [Hodgkin–Huxley: clamps, rest and firing](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-hodgkin-huxley-controls-en) (`hodgkin-huxley-controls`; Same-problem reference · Semi-analytic reference)

This educational membrane model does not reproduce the original voltage convention, TABLE/cnexp, cable propagation or measured physiology. Missing/unresolved events remain explicit; rest-root uniqueness and interval-Hurwitz stability are unclaimed.
## Assumptions, units and boundaries

Fix6.3°C and the NEURON8.2.6 analytic absolute-voltage convention in ms/mV/µA cm⁻². Use four clamp voltages, three steps, a20ms rest and a10–11ms pulse.

**Editorial clarification**

This educational membrane model does not reproduce the original voltage convention, TABLE/cnexp, cable propagation or measured physiology. Missing/unresolved events remain explicit; rest-root uniqueness and interval-Hurwitz stability are unclaimed.

## Adopted numerical method

Use classicalRK4 with all stages owned by each current segment. Separately qualify removable rate singularities, a Decimal rest root and independently written DP5(4)/Cash–Karp references.

$$
C_m\dot V=I-g_{Na}m^3h(V-E_{Na})-g_Kn^4(V-E_K)-g_L(V-E_L)
$$

$$
\dot z=\alpha_z(V)(1-z)-\beta_z(V)z
$$

## References and validation

Retain errors over all accepted times, voltage/gate ranges and Hermite firing events from fresh accepted-endpoint derivatives. Preserve the original1e-8clamp goal even when unmet.

## Limits

This educational membrane model does not reproduce the original voltage convention, TABLE/cnexp, cable propagation or measured physiology. Missing/unresolved events remain explicit; rest-root uniqueness and interval-Hurwitz stability are unclaimed.

## Study goals: 9 met, 1 unmet, 0 unresolved (10 total)

Mandatory qualification is separate from study-goal attainment. Met/unmet follow stored comparisons, not statistical certification. Unresolved and separate uncertainty classifications are retained; null is not replaced by false or zero.

[Original saved results / JSON](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/results/result.json)

<details><summary>Read every study-goal record</summary>

```json
{
  "schema_version": 1,
  "counts": {
    "met": 9,
    "unmet": 1,
    "unresolved": 0,
    "total": 10
  },
  "goals": [
    {
      "name": "HH/clamp-original1e-8/-80.0",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 4.711626791498169e-08,
        "target": 1e-08,
        "scope": "Maximum over ALL accepted times and all three gates; unmet outcomes retained"
      }
    },
    {
      "name": "HH/clamp-original1e-8/-55.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 7.262476731106915e-11,
        "target": 1e-08,
        "scope": "Maximum over ALL accepted times and all three gates; unmet outcomes retained"
      }
    },
    {
      "name": "HH/clamp-original1e-8/-40.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 1.4916989865554342e-10,
        "target": 1e-08,
        "scope": "Maximum over ALL accepted times and all three gates; unmet outcomes retained"
      }
    },
    {
      "name": "HH/clamp-original1e-8/0.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 7.521943623522986e-09,
        "target": 1e-08,
        "scope": "Maximum over ALL accepted times and all three gates; unmet outcomes retained"
      }
    },
    {
      "name": "HH/rest/0.04",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "target_mV": 1e-07
      }
    },
    {
      "name": "HH/rest/0.02",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "target_mV": 1e-07
      }
    },
    {
      "name": "HH/rest/0.01",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "target_mV": 1e-07
      }
    },
    {
      "name": "HH/pulse-voltage",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.00010511156826709112,
        "target": 0.05,
        "reference_spread": 1.0302887432089847e-09
      }
    },
    {
      "name": "HH/pulse-gates",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 5.371951350419124e-08,
        "target": 0.0001
      }
    },
    {
      "name": "HH/pulse-event",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual_ms": 3.799796033376879e-08,
        "target_ms": 0.01,
        "reason": null,
        "scope": "ObservedHermiteeventcomparison;exactODEeventcompletenessnotcertified"
      }
    }
  ],
  "classification_basis": "stored observed comparison; separate uncertainty classifications retained",
  "source": {
    "collection": "study_goals",
    "json_pointer": "/study_goals",
    "prefix": "HH/",
    "result_sha256": "104875b041a43542ec5d1500003da8f5986983816e27ce3b88971d11d7b63149",
    "acceptance_sha256": "47bb2050ccf15b2d404c2a3e63047d11d8258dc6feb25dc1e2fc14c3863b72ab",
    "result_url": "https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/results/result.json",
    "acceptance_url": "https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/acceptance.json"
  }
}
```

</details>

## Stored measurements and decisions

```json
{
  "metrics": {
    "fixed_records": 21,
    "HH/clamp-original1e-8/-80.0/actual": 4.711626791498169e-08,
    "HH/clamp-original1e-8/-55.0/actual": 7.262476731106915e-11,
    "HH/clamp-original1e-8/-40.0/actual": 1.4916989865554342e-10,
    "HH/clamp-original1e-8/0.0/actual": 7.521943623522986e-09,
    "HH/pulse-voltage/actual": 0.00010511156826709112,
    "HH/pulse-gates/actual": 5.371951350419124e-08,
    "HH/pulse-event/actual_ms": 3.799796033376879e-08
  },
  "checks": {
    "HH/rates_against_decimal": true,
    "HH/precision_companion": true,
    "HH/removable_singularities": true,
    "HH/rest_bracket_companion": true,
    "HH/owned_stage_edges": true,
    "HH/naive_jump_control_detected": true,
    "HH/clamp-finite-bounds/-80.0/0.04": true,
    "HH/clamp-finite-bounds/-80.0/0.02": true,
    "HH/clamp-finite-bounds/-80.0/0.01": true,
    "HH/clamp-finite-bounds/-55.0/0.04": true,
    "HH/clamp-finite-bounds/-55.0/0.02": true,
    "HH/clamp-finite-bounds/-55.0/0.01": true,
    "HH/clamp-finite-bounds/-40.0/0.04": true,
    "HH/clamp-finite-bounds/-40.0/0.02": true,
    "HH/clamp-finite-bounds/-40.0/0.01": true,
    "HH/clamp-finite-bounds/0.0/0.04": true,
    "HH/clamp-finite-bounds/0.0/0.02": true,
    "HH/clamp-finite-bounds/0.0/0.01": true,
    "HH/reference/rest": true,
    "HH/finite-gates/rest/0.04": true,
    "HH/finite-gates/rest/0.02": true,
    "HH/finite-gates/rest/0.01": true,
    "HH/reference/pulse": true,
    "HH/finite-gates/pulse/0.04": true,
    "HH/finite-gates/pulse/0.02": true,
    "HH/finite-gates/pulse/0.01": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/hodgkin-huxley-controls/index.json

![Separate actual accuracy,reference and statistical measurements,including unmet targets.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/results/hodgkin-huxley-controls-diagnostics.png)

Separate actual accuracy,reference and statistical measurements,including unmet targets.

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/atlas-biology-ode-controls-2026-11-25.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

## Sources and review scope

- NEURON8.2.6 analytic hh.mod. https://raw.githubusercontent.com/neuronsimulator/nrn/8.2.6/src/nrnoc/hh.mod; review_level=selected-primary-or-bibliographic-see-provenance
Actual selected read scopes and unread limits are recorded in source-reading.json; no full original-paper equation/figure reproduction claim.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
