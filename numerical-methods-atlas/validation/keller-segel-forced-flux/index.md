# Keller–Segel：連成流束の製造解

滑らかな2D厳密場で、交差流束・段時刻・収支を検証します。

**使用手法**

- [SSPRK(3,3)](https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk33/?lang=ja) (`ssprk33`)
- [Dormand–Prince RK45](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk45/?lang=ja) (`rk45`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/keller-segel-forced-flux/?lang=ja#keller-segel-forced-flux-ja-algorithm)

セル平均の中心面流束とSSPRK3を使い、n/c/強制項を同じ段に揃えます。展開した三角多項式の積分を、別の未展開積分とスカラー面ループ参照で確認します。

$$
n_t+\nabla\cdot(wn)=D_n\Delta n-\chi\nabla\cdot(n\nabla c)+rn(1-n)+s_n
$$

$$
\tau c_t=D_c\Delta c+\alpha n-\lambda c+s_c
$$

- [Keller–Segel走化性](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-keller-segel-ja) (`bio-keller-segel`)

単位正方形、T=0.25。n=1+0.1e⁻ᵗcosπx cosπy、c=1+0.05e⁻²ᵗcosπx cos2πyに合う強制項と接線方向の発散ゼロ移流を与えます。

- [外力・移流付きKeller–Segel製造問題](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#forced-keller-segel-model-ja) (`forced-keller-segel-model`)

単位正方形、T=0.25。n=1+0.1e⁻ᵗcosπx cosπy、c=1+0.05e⁻²ᵗcosπx cos2πyに合う強制項と接線方向の発散ゼロ移流を与えます。


**問題の図**

![Keller–Segel：連成流束の製造解：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/keller-segel-forced-flux.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Keller–Segel：連成流束の製造解](https://hrkoyama.github.io/numerical-methods-atlas/problems/keller-segel-forced-flux/?lang=ja) (`keller-segel-forced-flux`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/keller-segel-forced-flux/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/keller-segel-forced-flux/?lang=ja#keller-segel-forced-flux-ja-validation)

36点の源項、96セル状態ベクトル、符号・欠落連成・古い段・面重複の負例を検査。空間・同一MOL時間・正値性・実際の段収支を分けて保存します。

- [Keller–Segel：連成流束の製造解](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-keller-segel-forced-flux-ja) (`keller-segel-forced-flux`; 同じ問題の参照 · 製造解)

著者作成の強制2場モデルです。原著の全生物モデル、ピーク形成、真のblow-upやその抑制を実証しません。負値をクリップして正値性を装いません。
## 前提・単位・境界

単位正方形、T=0.25。n=1+0.1e⁻ᵗcosπx cosπy、c=1+0.05e⁻²ᵗcosπx cos2πyに合う強制項と接線方向の発散ゼロ移流を与えます。

**編集上の補足**

著者作成の強制2場モデルです。原著の全生物モデル、ピーク形成、真のblow-upやその抑制を実証しません。負値をクリップして正値性を装いません。

## 採用した計算法

セル平均の中心面流束とSSPRK3を使い、n/c/強制項を同じ段に揃えます。展開した三角多項式の積分を、別の未展開積分とスカラー面ループ参照で確認します。

$$
n_t+\nabla\cdot(wn)=D_n\Delta n-\chi\nabla\cdot(n\nabla c)+rn(1-n)+s_n
$$

$$
\tau c_t=D_c\Delta c+\alpha n-\lambda c+s_c
$$

## 比較・検証

36点の源項、96セル状態ベクトル、符号・欠落連成・古い段・面重複の負例を検査。空間・同一MOL時間・正値性・実際の段収支を分けて保存します。

## 確認の限界

著者作成の強制2場モデルです。原著の全生物モデル、ピーク形成、真のblow-upやその抑制を実証しません。負値をクリップして正値性を装いません。

## 調査した目標：達成9・未達0・未確定0（全9）

必須の検証合格と元の調査目標の達成は別です。達成・未達は保存された比較結果を示し、統計的な認定ではありません。未確定と別の不確かさ区分を保持し、nullをfalseや0に置き換えません。

[元の保存結果 / JSON](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/result.json)

<details><summary>全目標の記録を読む</summary>

```json
{
  "schema_version": 1,
  "counts": {
    "met": 9,
    "unmet": 0,
    "unresolved": 0,
    "total": 9
  },
  "goals": [
    {
      "name": "KS/minimum/12",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "minimum": [
          0.9022638544007324,
          0.9527970664018593
        ]
      }
    },
    {
      "name": "KS/minimum/24",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "minimum": [
          0.9005698543736446,
          0.9507102465265501
        ]
      }
    },
    {
      "name": "KS/minimum/48",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "minimum": [
          0.9001427078852056,
          0.9501782550064043
        ]
      }
    },
    {
      "name": "KS/time-order",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 3.0037445404571113,
        "target": 2.5
      }
    },
    {
      "name": "KS/space-finest/0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.0001221189660198796,
        "target": 0.002
      }
    },
    {
      "name": "KS/space-order/0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 1.9965225132866062,
        "target": 1.7
      }
    },
    {
      "name": "KS/space-finest/1",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 2.9817290057465584e-05,
        "target": 0.002
      }
    },
    {
      "name": "KS/space-order/1",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 1.988907316937278,
        "target": 1.7
      }
    },
    {
      "name": "KS/time-contamination",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 1.893596390800667e-12,
        "finest_spatial_error": 0.0001221189660198796
      }
    }
  ],
  "classification_basis": "stored observed comparison; separate uncertainty classifications retained",
  "source": {
    "collection": "study_goals",
    "json_pointer": "/study_goals",
    "prefix": "KS/",
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
    "fixed_records": 10,
    "KS/time-order/actual": 3.0037445404571113,
    "KS/space-finest/0/actual": 0.0001221189660198796,
    "KS/space-order/0/actual": 1.9965225132866062,
    "KS/space-finest/1/actual": 2.9817290057465584e-05,
    "KS/space-order/1/actual": 1.988907316937278,
    "KS/time-contamination/actual": 1.893596390800667e-12
  },
  "checks": {
    "KS/source_point_pairs36": true,
    "KS/wholegrid_RHS_vectorpairs96": true,
    "KS/divergence_free_faces": true,
    "KS/independent_velocity": true,
    "KS/wrong_chi_detected": true,
    "KS/omitted_coupling_detected": true,
    "KS/stale_source_time_detected": true,
    "KS/duplicated_external_face_detected": true,
    "KS/massledger/12": true,
    "KS/massledger/24": true,
    "KS/massledger/48": true,
    "KS/reference": true,
    "KS/constant-control": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/keller-segel-forced-flux/index.json

![精度・参照・統計の実測値と未達目標を分けて表示します。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/keller-segel-forced-flux-diagnostics.png)

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

- Atlas authored Keller–Segel manufactured fields, forcing and finite-volume balance controls (2026-11-25). https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/keller_segel.py; review_level=authored-formulas-and-actually-executed-component-checks
本アトラス独自の製造解・外力・面流束の導出と実装です。保存された成分検査・独立なスカラー面/RHS参照・セル平均照合の範囲に限ります。原著論文の読了や元の無外力問題の再現を主張しません。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Keller–Segel: a manufactured coupled-flux solution

Use smooth exact2D fields to test cross fluxes, stage timing and mass ledgers.

**Methods used**

- [SSPRK(3,3)](https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk33/?lang=en) (`ssprk33`)
- [Dormand–Prince RK45](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk45/?lang=en) (`rk45`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/keller-segel-forced-flux/?lang=en#keller-segel-forced-flux-en-algorithm)

Use cell-average centered face fluxes and SSPRK3 with n,c and forcing at the same stage. Check expanded trigonometric integrals against independent unexpanded integrals and scalar face-loop references.

$$
n_t+\nabla\cdot(wn)=D_n\Delta n-\chi\nabla\cdot(n\nabla c)+rn(1-n)+s_n
$$

$$
\tau c_t=D_c\Delta c+\alpha n-\lambda c+s_c
$$

- [Keller–Segel chemotaxis](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-keller-segel-en) (`bio-keller-segel`)

On the unit square toT.25,manufacture forcing for n=1+.1e⁻ᵗcosπx cosπy,c=1+.05e⁻²ᵗcosπx cos2πy with divergence-free tangential advection.

- [Forced advective Keller–Segel manufactured problem](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#forced-keller-segel-model-en) (`forced-keller-segel-model`)

On the unit square toT.25,manufacture forcing for n=1+.1e⁻ᵗcosπx cosπy,c=1+.05e⁻²ᵗcosπx cos2πy with divergence-free tangential advection.


**Problem figure**

![Keller–Segel: a manufactured coupled-flux solution: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/keller-segel-forced-flux.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Keller–Segel: a manufactured coupled-flux solution](https://hrkoyama.github.io/numerical-methods-atlas/problems/keller-segel-forced-flux/?lang=en) (`keller-segel-forced-flux`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/keller-segel-forced-flux/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/keller-segel-forced-flux/?lang=en#keller-segel-forced-flux-en-validation)

Qualify36source pairs,96cell-state vectors and wrong-sign,omitted-coupling,stale-stage and face-duplication controls. Separate spatial,same-MOL time,positivity and actual stage-ledger outcomes.

- [Keller–Segel: a manufactured coupled-flux solution](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-keller-segel-forced-flux-en) (`keller-segel-forced-flux`; Same-problem reference · Manufactured solution)

This authored forced two-field model does not reproduce the full original biological model or demonstrate aggregation, true blow-up or suppression. No clipping is used to manufacture positivity.
## Assumptions, units and boundaries

On the unit square toT.25,manufacture forcing for n=1+.1e⁻ᵗcosπx cosπy,c=1+.05e⁻²ᵗcosπx cos2πy with divergence-free tangential advection.

**Editorial clarification**

This authored forced two-field model does not reproduce the full original biological model or demonstrate aggregation, true blow-up or suppression. No clipping is used to manufacture positivity.

## Adopted numerical method

Use cell-average centered face fluxes and SSPRK3 with n,c and forcing at the same stage. Check expanded trigonometric integrals against independent unexpanded integrals and scalar face-loop references.

$$
n_t+\nabla\cdot(wn)=D_n\Delta n-\chi\nabla\cdot(n\nabla c)+rn(1-n)+s_n
$$

$$
\tau c_t=D_c\Delta c+\alpha n-\lambda c+s_c
$$

## References and validation

Qualify36source pairs,96cell-state vectors and wrong-sign,omitted-coupling,stale-stage and face-duplication controls. Separate spatial,same-MOL time,positivity and actual stage-ledger outcomes.

## Limits

This authored forced two-field model does not reproduce the full original biological model or demonstrate aggregation, true blow-up or suppression. No clipping is used to manufacture positivity.

## Study goals: 9 met, 0 unmet, 0 unresolved (9 total)

Mandatory qualification is separate from study-goal attainment. Met/unmet follow stored comparisons, not statistical certification. Unresolved and separate uncertainty classifications are retained; null is not replaced by false or zero.

[Original saved results / JSON](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/result.json)

<details><summary>Read every study-goal record</summary>

```json
{
  "schema_version": 1,
  "counts": {
    "met": 9,
    "unmet": 0,
    "unresolved": 0,
    "total": 9
  },
  "goals": [
    {
      "name": "KS/minimum/12",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "minimum": [
          0.9022638544007324,
          0.9527970664018593
        ]
      }
    },
    {
      "name": "KS/minimum/24",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "minimum": [
          0.9005698543736446,
          0.9507102465265501
        ]
      }
    },
    {
      "name": "KS/minimum/48",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "minimum": [
          0.9001427078852056,
          0.9501782550064043
        ]
      }
    },
    {
      "name": "KS/time-order",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 3.0037445404571113,
        "target": 2.5
      }
    },
    {
      "name": "KS/space-finest/0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.0001221189660198796,
        "target": 0.002
      }
    },
    {
      "name": "KS/space-order/0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 1.9965225132866062,
        "target": 1.7
      }
    },
    {
      "name": "KS/space-finest/1",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 2.9817290057465584e-05,
        "target": 0.002
      }
    },
    {
      "name": "KS/space-order/1",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 1.988907316937278,
        "target": 1.7
      }
    },
    {
      "name": "KS/time-contamination",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 1.893596390800667e-12,
        "finest_spatial_error": 0.0001221189660198796
      }
    }
  ],
  "classification_basis": "stored observed comparison; separate uncertainty classifications retained",
  "source": {
    "collection": "study_goals",
    "json_pointer": "/study_goals",
    "prefix": "KS/",
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
    "fixed_records": 10,
    "KS/time-order/actual": 3.0037445404571113,
    "KS/space-finest/0/actual": 0.0001221189660198796,
    "KS/space-order/0/actual": 1.9965225132866062,
    "KS/space-finest/1/actual": 2.9817290057465584e-05,
    "KS/space-order/1/actual": 1.988907316937278,
    "KS/time-contamination/actual": 1.893596390800667e-12
  },
  "checks": {
    "KS/source_point_pairs36": true,
    "KS/wholegrid_RHS_vectorpairs96": true,
    "KS/divergence_free_faces": true,
    "KS/independent_velocity": true,
    "KS/wrong_chi_detected": true,
    "KS/omitted_coupling_detected": true,
    "KS/stale_source_time_detected": true,
    "KS/duplicated_external_face_detected": true,
    "KS/massledger/12": true,
    "KS/massledger/24": true,
    "KS/massledger/48": true,
    "KS/reference": true,
    "KS/constant-control": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/keller-segel-forced-flux/index.json

![Separate actual accuracy,reference and statistical measurements,including unmet targets.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/keller-segel-forced-flux-diagnostics.png)

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

- Atlas authored Keller–Segel manufactured fields, forcing and finite-volume balance controls (2026-11-25). https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/keller_segel.py; review_level=authored-formulas-and-actually-executed-component-checks
Atlas-authored manufactured fields, forcing and face-flux derivation/implementation. Evidence is limited to saved component checks, independently written scalar-face/RHS references and cell-average comparisons. No original-paper full-text reading or reproduction of the unforced original problem is claimed.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
