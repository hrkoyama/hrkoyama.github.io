# 移入–死亡SSA：有限時刻の厳密分布

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
## 前提・単位・境界

移入率6、粒子ごとの死亡率1、時刻0/0.5/2/4。初期0・5・名目上のPoisson(6)定常標本を2seedずつ、各2,048本で比較します。

**編集上の補足**

有限時間の決定論的初期状態を定常分布とは呼びません。区間の保証は理想IID法則の参照に限り、PRNG・対数演算を含むソフトウェア全体の被覆率保証や単一軌跡の代表性を主張しません。

## 採用した計算法

Gillespie direct SSAで、次の事象時刻を観測点の間で保持します。生のPCG64から開区間一様数を作り、初期Poissonの有限格子逆CDFと全ストリームを記録します。

$$
\varnothing\xrightarrow{6}N,\qquad N\xrightarrow{N} \varnothing
$$

$$
N(t)\overset d=\mathrm{Bin}(n_0,e^{-t})+\mathrm{Pois}(6(1-e^{-t}))
$$

## 比較・検証

Binomial＋Poissonの厳密過渡法則を、80/120桁の有向区間・尾部上界で照合。20個のDKW目標と20個の厳密和平均目標を名目union bound0.01にまとめ、分散の5SE目標は別に残します。

## 確認の限界

有限時間の決定論的初期状態を定常分布とは呼びません。区間の保証は理想IID法則の参照に限り、PRNG・対数演算を含むソフトウェア全体の被覆率保証や単一軌跡の代表性を主張しません。

## 調査した目標：達成40・未達0・未確定0（全40）

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

## 保存実測値と判定

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

- Gillespie(1977), Exact stochastic simulation of coupled chemical reactions. https://doi.org/10.1021/j100540a008; review_level=selected-primary-or-bibliographic-see-provenance
source-reading.jsonに実際の読取範囲と未読部分を記録。原著の全式・全図の再現とは主張しません。

- Massart(1990),The Tight Constant in the Dvoretzky–Kiefer–Wolfowitz Inequality. https://doi.org/10.1214/aop/1176990746; review_level=selected-primary-abstract
著者公開ページの原著抄録でIID・両側定数2を確認。公式本文はiframeで閲覧できず、証明の全読はしていません。

- Reeve(2024),A short proof of the Dvoretzky–Kiefer–Wolfowitz–Massart inequality. https://arxiv.org/pdf/2403.16651; review_level=selected-primary-theorem
v1の1–3頁、IID設定・定理1・系1/2のみ確認。詳細な証明は未読です。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Immigration–death SSA: exact transient laws

Separate one displayed path from12,288fixed ensemble paths.

**Methods used**

- [Gillespie direct stochastic simulation (SSA)](https://hrkoyama.github.io/numerical-methods-atlas/methods/gillespie-ssa/?lang=en) (`gillespie-ssa`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/immigration-death-ssa/?lang=en#immigration-death-ssa-en-algorithm)

Use direct GillespieSSA with pending event times preserved across observations. Draw open-grid uniforms from rawPCG64; record finite-grid Poisson initialization and all RNG streams.

$$
\varnothing\xrightarrow{6}N,\qquad N\xrightarrow{N} \varnothing
$$

$$
N(t)\overset d=\mathrm{Bin}(n_0,e^{-t})+\mathrm{Pois}(6(1-e^{-t}))
$$

- [Chemical master equation and Gillespie SSA](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-chemical-master-en) (`bio-chemical-master`)

Use immigration6, per-particle death1 and observations0/0.5/2/4. Compare initial0,5 and nominal stationary Poisson(6), two seeds each and2,048paths per record.

- [Immigration–death reaction and exact transient law](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#immigration-death-model-en) (`immigration-death-model`)

Use immigration6, per-particle death1 and observations0/0.5/2/4. Compare initial0,5 and nominal stationary Poisson(6), two seeds each and2,048paths per record.


**Problem figure**

![Immigration–death SSA: exact transient laws: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/results/immigration-death-ssa.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Immigration–death SSA: exact transient laws](https://hrkoyama.github.io/numerical-methods-atlas/problems/immigration-death-ssa/?lang=en) (`immigration-death-ssa`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/immigration-death-ssa/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/immigration-death-ssa/?lang=en#immigration-death-ssa-en-validation)

Qualify exact Binomial-plus-Poisson transients with directed80/120digit intervals and tail bounds. Combine20DKW and20exact-sum mean goals under nominal union bound0.01; retain five-SE variance goals separately.

- [Immigration–death SSA: exact transient laws](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-immigration-death-ssa-en) (`immigration-death-ssa`; Same-problem reference · Analytic reference)

Finite deterministic-start transients are not stationary. Interval qualification concerns the idealIID reference law, without a whole-software PRNG/logarithm coverage guarantee or a claim that one path represents the ensemble.
## Assumptions, units and boundaries

Use immigration6, per-particle death1 and observations0/0.5/2/4. Compare initial0,5 and nominal stationary Poisson(6), two seeds each and2,048paths per record.

**Editorial clarification**

Finite deterministic-start transients are not stationary. Interval qualification concerns the idealIID reference law, without a whole-software PRNG/logarithm coverage guarantee or a claim that one path represents the ensemble.

## Adopted numerical method

Use direct GillespieSSA with pending event times preserved across observations. Draw open-grid uniforms from rawPCG64; record finite-grid Poisson initialization and all RNG streams.

$$
\varnothing\xrightarrow{6}N,\qquad N\xrightarrow{N} \varnothing
$$

$$
N(t)\overset d=\mathrm{Bin}(n_0,e^{-t})+\mathrm{Pois}(6(1-e^{-t}))
$$

## References and validation

Qualify exact Binomial-plus-Poisson transients with directed80/120digit intervals and tail bounds. Combine20DKW and20exact-sum mean goals under nominal union bound0.01; retain five-SE variance goals separately.

## Limits

Finite deterministic-start transients are not stationary. Interval qualification concerns the idealIID reference law, without a whole-software PRNG/logarithm coverage guarantee or a claim that one path represents the ensemble.

## Study goals: 40 met, 0 unmet, 0 unresolved (40 total)

Mandatory qualification is separate from study-goal attainment. Met/unmet follow stored comparisons, not statistical certification. Unresolved and separate uncertainty classifications are retained; null is not replaced by false or zero.

[Original saved results / JSON](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/results/result.json)

<details><summary>Read every study-goal record</summary>

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

## Stored measurements and decisions

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

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/immigration-death-ssa/index.json

![Separate actual accuracy,reference and statistical measurements,including unmet targets.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/results/immigration-death-ssa-diagnostics.png)

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

- Gillespie(1977), Exact stochastic simulation of coupled chemical reactions. https://doi.org/10.1021/j100540a008; review_level=selected-primary-or-bibliographic-see-provenance
Actual selected read scopes and unread limits are recorded in source-reading.json; no full original-paper equation/figure reproduction claim.

- Massart(1990),The Tight Constant in the Dvoretzky–Kiefer–Wolfowitz Inequality. https://doi.org/10.1214/aop/1176990746; review_level=selected-primary-abstract
Selected original abstract on the author-uploaded page:IID/two-sidedconstant2. Official body access was blocked by an iframe; proof unread.

- Reeve(2024),A short proof of the Dvoretzky–Kiefer–Wolfowitz–Massart inequality. https://arxiv.org/pdf/2403.16651; review_level=selected-primary-theorem
Selected v1pp1–3:IIDsetup,Theorem1,Corollaries1/2. Detailed proofs unread.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
