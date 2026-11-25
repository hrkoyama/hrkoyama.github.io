# 神経膜と反応SSAの独立検証

Hodgkin–Huxleyの電位固定・静止・発火と、移入–死亡SSAの厳密過渡分布を、小さな固定入力で照合します。

共通22実行例の台帳とは別に管理する追加検証集です。配布ZIPを独立展開し、各グループの全固定入力と検査を実行した記録を示します。設定・手法・刻み幅の違いを独立した物理問題の数には加算しません。

## Hodgkin–Huxley：電位固定・静止平衡・発火

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
### 前提・単位・境界

6.3°C、ms/mV/µA cm⁻²。NEURON8.2.6の解析的な絶対電位規約を固定し、4電位×3刻み、静止20 ms、10–11 msの電流パルスを扱います。

**編集上の補足**

1細胞膜の教育例です。元論文の電位規約、TABLE/cnexp実装、ケーブル伝播や生体実測の再現とは呼びません。区間内に括れない発火は捏造せず、静止根の一意性・区間Hurwitz安定性は主張しません。

### 採用した計算法

古典RK4を用い、電流の切り替わりでは全段の片側値を区間に帰属させます。ゲートの可除特異点、Decimal静止根、独立なDP5(4)/Cash–Karp参照を別に照合します。

$$
C_m\dot V=I-g_{Na}m^3h(V-E_{Na})-g_Kn^4(V-E_K)-g_L(V-E_L)
$$

$$
\dot z=\alpha_z(V)(1-z)-\beta_z(V)z
$$

### 比較・検証

全採用時刻のゲート誤差、電位・ゲート範囲、採用端点の新しい微分を使うHermite発火時刻を保存。元の1e-8ゲート目標も未達を含めて表示します。

### 確認の限界

1細胞膜の教育例です。元論文の電位規約、TABLE/cnexp実装、ケーブル伝播や生体実測の再現とは呼びません。区間内に括れない発火は捏造せず、静止根の一意性・区間Hurwitz安定性は主張しません。

### 調査した目標：達成9・未達1・未確定0（全10）

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

### 保存実測値と判定

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

### 取得・実行

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

### 出典と確認範囲

- NEURON8.2.6 analytic hh.mod. https://raw.githubusercontent.com/neuronsimulator/nrn/8.2.6/src/nrnoc/hh.mod; review_level=selected-primary-or-bibliographic-see-provenance
source-reading.jsonに実際の読取範囲と未読部分を記録。原著の全式・全図の再現とは主張しません。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## 移入–死亡SSA：有限時刻の厳密分布

1本の軌跡と12,288本の固定アンサンブルを分けて検証します。

**使用手法**

- [Gillespie直接確率シミュレーション（SSA）](https://hrkoyama.github.io/numerical-methods-atlas/methods/gillespie-ssa/?lang=ja) (`gillespie-ssa`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/immigration-death-ssa/?lang=ja#immigration-death-ssa-ja-algorithm)

Gillespie direct SSAで、次の事象時刻を観測点の間で保持します。生のPCG64から開区間一様数を作り、初期Poissonの有限格子逆CDFと全ストリームを記録します。

$$
\varnothing\xrightarrow{6}N,\qquad N\xrightarrow{N} \varnothing
$$

$$
N(t)\overset d=\mathrm{Bin}(n_0,e^{-t})+\mathrm{Pois}(6(1-e^{-t}))
$$

- [化学マスター方程式とGillespie SSA](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-chemical-master-ja) (`bio-chemical-master`)

移入率6、粒子ごとの死亡率1、時刻0/0.5/2/4。初期0・5・名目上のPoisson(6)定常標本を2seedずつ、各2,048本で比較します。

- [移入–死亡反応と厳密過渡法則](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#immigration-death-model-ja) (`immigration-death-model`)

移入率6、粒子ごとの死亡率1、時刻0/0.5/2/4。初期0・5・名目上のPoisson(6)定常標本を2seedずつ、各2,048本で比較します。


**問題の図**

![移入–死亡SSA：有限時刻の厳密分布：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/results/immigration-death-ssa.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[移入–死亡SSA：有限時刻の厳密分布](https://hrkoyama.github.io/numerical-methods-atlas/problems/immigration-death-ssa/?lang=ja) (`immigration-death-ssa`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/immigration-death-ssa/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/immigration-death-ssa/?lang=ja#immigration-death-ssa-ja-validation)

Binomial＋Poissonの厳密過渡法則を、80/120桁の有向区間・尾部上界で照合。20個のDKW目標と20個の厳密和平均目標を名目union bound0.01にまとめ、分散の5SE目標は別に残します。

- [移入–死亡SSA：有限時刻の厳密分布](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-immigration-death-ssa-ja) (`immigration-death-ssa`; 同じ問題の参照 · 解析参照)

有限時間の決定論的初期状態を定常分布とは呼びません。区間の保証は理想IID法則の参照に限り、PRNG・対数演算を含むソフトウェア全体の被覆率保証や単一軌跡の代表性を主張しません。
### 前提・単位・境界

移入率6、粒子ごとの死亡率1、時刻0/0.5/2/4。初期0・5・名目上のPoisson(6)定常標本を2seedずつ、各2,048本で比較します。

**編集上の補足**

有限時間の決定論的初期状態を定常分布とは呼びません。区間の保証は理想IID法則の参照に限り、PRNG・対数演算を含むソフトウェア全体の被覆率保証や単一軌跡の代表性を主張しません。

### 採用した計算法

Gillespie direct SSAで、次の事象時刻を観測点の間で保持します。生のPCG64から開区間一様数を作り、初期Poissonの有限格子逆CDFと全ストリームを記録します。

$$
\varnothing\xrightarrow{6}N,\qquad N\xrightarrow{N} \varnothing
$$

$$
N(t)\overset d=\mathrm{Bin}(n_0,e^{-t})+\mathrm{Pois}(6(1-e^{-t}))
$$

### 比較・検証

Binomial＋Poissonの厳密過渡法則を、80/120桁の有向区間・尾部上界で照合。20個のDKW目標と20個の厳密和平均目標を名目union bound0.01にまとめ、分散の5SE目標は別に残します。

### 確認の限界

有限時間の決定論的初期状態を定常分布とは呼びません。区間の保証は理想IID法則の参照に限り、PRNG・対数演算を含むソフトウェア全体の被覆率保証や単一軌跡の代表性を主張しません。

### 調査した目標：達成40・未達0・未確定0（全40）

必須の検証合格と元の調査目標の達成は別です。達成・未達は保存された比較結果を示し、統計的な認定ではありません。未確定と別の不確かさ区分を保持し、nullをfalseや0に置き換えません。

[元の保存結果 / JSON](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/results/result.json)

<details><summary>全目標の記録を読む</summary>

```json
{
  "schema_version": 1,
  "counts": {
    "met": 40,
    "unmet": 0,
    "unresolved": 0,
    "total": 40
  },
  "goals": [
    {
      "name": "SSA/DKW/0/1",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.0044938265744222106,
        "epsilon": 0.046841646520958534
      }
    },
    {
      "name": "SSA/exact-mean/0/1",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "sum": 4830,
        "bounds": [
          4582,
          5092
        ]
      }
    },
    {
      "name": "SSA/DKW/0/2",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.011554936819670791,
        "epsilon": 0.046841646520958534
      }
    },
    {
      "name": "SSA/exact-mean/0/2",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "sum": 10708,
        "bounds": [
          10250,
          11005
        ]
      }
    },
    {
      "name": "SSA/DKW/0/3",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.01814154306809468,
        "epsilon": 0.046841646520958534
      }
    },
    {
      "name": "SSA/exact-mean/0/3",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "sum": 11935,
        "bounds": [
          11663,
          12467
        ]
      }
    },
    {
      "name": "SSA/DKW/1/1",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.0059642975343668775,
        "epsilon": 0.046841646520958534
      }
    },
    {
      "name": "SSA/exact-mean/1/1",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "sum": 4851,
        "bounds": [
          4582,
          5092
        ]
      }
    },
    {
      "name": "SSA/DKW/1/2",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.019536382644266714,
        "epsilon": 0.046841646520958534
      }
    },
    {
      "name": "SSA/exact-mean/1/2",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "sum": 10775,
        "bounds": [
          10250,
          11005
        ]
      }
    },
    {
      "name": "SSA/DKW/1/3",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.01048461957478325,
        "epsilon": 0.046841646520958534
      }
    },
    {
      "name": "SSA/exact-mean/1/3",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "sum": 12142,
        "bounds": [
          11663,
          12467
        ]
      }
    },
    {
      "name": "SSA/DKW/2/1",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.01601739601069163,
        "epsilon": 0.046841646520958534
      }
    },
    {
      "name": "SSA/exact-mean/2/1",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "sum": 10934,
        "bounds": [
          10735,
          11359
        ]
      }
    },
    {
      "name": "SSA/DKW/2/2",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.009983568643240626,
        "epsilon": 0.046841646520958534
      }
    },
    {
      "name": "SSA/exact-mean/2/2",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "sum": 11938,
        "bounds": [
          11615,
          12411
        ]
      }
    },
    {
      "name": "SSA/DKW/2/3",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.00685998885581765,
        "epsilon": 0.046841646520958534
      }
    },
    {
      "name": "SSA/exact-mean/2/3",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "sum": 12211,
        "bounds": [
          11847,
          12658
        ]
      }
    },
    {
      "name": "SSA/DKW/3/1",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.016697788968076333,
        "epsilon": 0.046841646520958534
      }
    },
    {
      "name": "SSA/exact-mean/3/1",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "sum": 10912,
        "bounds": [
          10735,
          11359
        ]
      }
    },
    {
      "name": "SSA/DKW/3/2",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.014638919344433177,
        "epsilon": 0.046841646520958534
      }
    },
    {
      "name": "SSA/exact-mean/3/2",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "sum": 11957,
        "bounds": [
          11615,
          12411
        ]
      }
    },
    {
      "name": "SSA/DKW/3/3",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.01647513015314328,
        "epsilon": 0.046841646520958534
      }
    },
    {
      "name": "SSA/exact-mean/3/3",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "sum": 12256,
        "bounds": [
          11847,
          12658
        ]
      }
    },
    {
      "name": "SSA/DKW/4/0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.027464889885388755,
        "epsilon": 0.046841646520958534
      }
    },
    {
      "name": "SSA/exact-mean/4/0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "sum": 12045,
        "bounds": [
          11884,
          12696
        ]
      }
    },
    {
      "name": "SSA/DKW/4/1",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.016762427046282946,
        "epsilon": 0.046841646520958534
      }
    },
    {
      "name": "SSA/exact-mean/4/1",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "sum": 12243,
        "bounds": [
          11884,
          12696
        ]
      }
    },
    {
      "name": "SSA/DKW/4/2",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.008400530933368788,
        "epsilon": 0.046841646520958534
      }
    },
    {
      "name": "SSA/exact-mean/4/2",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "sum": 12237,
        "bounds": [
          11884,
          12696
        ]
      }
    },
    {
      "name": "SSA/DKW/4/3",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.014281296135388755,
        "epsilon": 0.046841646520958534
      }
    },
    {
      "name": "SSA/exact-mean/4/3",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "sum": 12245,
        "bounds": [
          11884,
          12696
        ]
      }
    },
    {
      "name": "SSA/DKW/5/0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.018227270796282946,
        "epsilon": 0.046841646520958534
      }
    },
    {
      "name": "SSA/exact-mean/5/0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "sum": 12134,
        "bounds": [
          11884,
          12696
        ]
      }
    },
    {
      "name": "SSA/DKW/5/1",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.02549037468336879,
        "epsilon": 0.046841646520958534
      }
    },
    {
      "name": "SSA/exact-mean/5/1",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "sum": 12166,
        "bounds": [
          11884,
          12696
        ]
      }
    },
    {
      "name": "SSA/DKW/5/2",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.018433547614611245,
        "epsilon": 0.046841646520958534
      }
    },
    {
      "name": "SSA/exact-mean/5/2",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "sum": 12379,
        "bounds": [
          11884,
          12696
        ]
      }
    },
    {
      "name": "SSA/DKW/5/3",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.013083844066631212,
        "epsilon": 0.046841646520958534
      }
    },
    {
      "name": "SSA/exact-mean/5/3",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "sum": 12333,
        "bounds": [
          11884,
          12696
        ]
      }
    }
  ],
  "classification_basis": "stored observed comparison; separate uncertainty classifications retained",
  "source": {
    "collection": "study_goals",
    "json_pointer": "/study_goals",
    "prefix": "SSA/",
    "result_sha256": "104875b041a43542ec5d1500003da8f5986983816e27ce3b88971d11d7b63149",
    "acceptance_sha256": "47bb2050ccf15b2d404c2a3e63047d11d8258dc6feb25dc1e2fc14c3863b72ab",
    "result_url": "https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/results/result.json",
    "acceptance_url": "https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/acceptance.json"
  }
}
```

</details>

### 保存実測値と判定

```json
{
  "metrics": {
    "fixed_records": 9,
    "SSA/DKW/0/1/actual": 0.0044938265744222106,
    "SSA/DKW/0/2/actual": 0.011554936819670791,
    "SSA/DKW/0/3/actual": 0.01814154306809468,
    "SSA/DKW/1/1/actual": 0.0059642975343668775,
    "SSA/DKW/1/2/actual": 0.019536382644266714,
    "SSA/DKW/1/3/actual": 0.01048461957478325,
    "SSA/DKW/2/1/actual": 0.01601739601069163,
    "SSA/DKW/2/2/actual": 0.009983568643240626,
    "SSA/DKW/2/3/actual": 0.00685998885581765,
    "SSA/DKW/3/1/actual": 0.016697788968076333,
    "SSA/DKW/3/2/actual": 0.014638919344433177,
    "SSA/DKW/3/3/actual": 0.01647513015314328,
    "SSA/DKW/4/0/actual": 0.027464889885388755,
    "SSA/DKW/4/1/actual": 0.016762427046282946,
    "SSA/DKW/4/2/actual": 0.008400530933368788,
    "SSA/DKW/4/3/actual": 0.014281296135388755,
    "SSA/DKW/5/0/actual": 0.018227270796282946,
    "SSA/DKW/5/1/actual": 0.02549037468336879,
    "SSA/DKW/5/2/actual": 0.018433547614611245,
    "SSA/DKW/5/3/actual": 0.013083844066631212
  },
  "checks": {
    "SSA/pending_boundary_and_censoring": true,
    "SSA/pending_not_redrawn_at_observations": true,
    "SSA/initial_inverse_monotone": true,
    "SSA/open_grid_limits": true,
    "SSA/reaction_equality_is_death": true,
    "SSA/wrong_stationarity_control": true,
    "SSA/law/0/0.5/1": true,
    "SSA/law/0/2.0/1": true,
    "SSA/law/0/4.0/1": true,
    "SSA/law/5/0.5/1": true,
    "SSA/law/5/2.0/1": true,
    "SSA/law/5/4.0/1": true,
    "SSA/law/stationary/0.0/1": true,
    "SSA/law/0/0.5/2048": true,
    "SSA/law/0/2.0/2048": true,
    "SSA/law/0/4.0/2048": true,
    "SSA/law/5/0.5/2048": true,
    "SSA/law/5/2.0/2048": true,
    "SSA/law/5/4.0/2048": true,
    "SSA/law/stationary/0.0/2048": true,
    "SSA/t0/0": true,
    "SSA/t0/1": true,
    "SSA/t0/2": true,
    "SSA/t0/3": true,
    "SSA/exact-family-count": true,
    "SSA/stream-namespaces-unique": true,
    "SSA/all-24578-initial-PCG-state-inc-pairs-unique": true,
    "SSA/all-24578-stream-labels-unique": true,
    "SSA/all-paths": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/immigration-death-ssa/index.json

![精度・参照・統計の実測値と未達目標を分けて表示します。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/results/immigration-death-ssa-diagnostics.png)

精度・参照・統計の実測値と未達目標を分けて表示します。

### 取得・実行

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

### 出典と確認範囲

- Gillespie(1977), Exact stochastic simulation of coupled chemical reactions. https://doi.org/10.1021/j100540a008; review_level=selected-primary-or-bibliographic-see-provenance
source-reading.jsonに実際の読取範囲と未読部分を記録。原著の全式・全図の再現とは主張しません。

- Massart(1990),The Tight Constant in the Dvoretzky–Kiefer–Wolfowitz Inequality. https://doi.org/10.1214/aop/1176990746; review_level=selected-primary-abstract
著者公開ページの原著抄録でIID・両側定数2を確認。公式本文はiframeで閲覧できず、証明の全読はしていません。

- Reeve(2024),A short proof of the Dvoretzky–Kiefer–Wolfowitz–Massart inequality. https://arxiv.org/pdf/2403.16651; review_level=selected-primary-theorem
v1の1–3頁、IID設定・定理1・系1/2のみ確認。詳細な証明は未読です。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
