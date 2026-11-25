# Schnakenberg：2D境界と初期モード

2つのNeumann摂動とDirichlet摂動を独立な非線形Galerkin参照と比較します。

**使用手法**

- [Crank–Nicolson法](https://hrkoyama.github.io/numerical-methods-atlas/methods/crank-nicolson/?lang=ja) (`crank-nicolson`)
- [Strang分割](https://hrkoyama.github.io/numerical-methods-atlas/methods/strang-splitting/?lang=ja) (`strang-splitting`)
- [Dormand–Prince RK45](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk45/?lang=ja) (`rk45`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-2d-boundary-modes/?lang=ja#schnakenberg-2d-boundary-modes-ja-algorithm)

セル平均のCN拡散と局所陰的中点反応をStrang分割します。独立参照は正規直交sin/cos Galerkin、K12/18,Q96/192と2許容誤差の4列を全初期値で残します。 元のDirichlet K12/18参照は初回の相対資格基準を満たさなかったため、失敗を残し、D境界だけK24/32・Q128/192の4参照を追加します。

$$
u_t=.01\Delta u+.1-u+u^2v,\qquad v_t=\Delta v+.9-u^2v
$$

- [Schnakenberg反応拡散](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-schnakenberg-ja) (`bio-schnakenberg`)

[0,2π]²、T=2、a=0.1,b=0.9,Du=0.01,Dv=1。平衡(1,0.9)のまわりで3初期値と12/24/48セル、一定の非周期境界を使います。


**問題の図**

![Schnakenberg：2D境界と初期モード：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/schnakenberg-2d-boundary-modes.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Schnakenberg：2D境界と初期モード](https://hrkoyama.github.io/numerical-methods-atlas/problems/schnakenberg-2d-boundary-modes/?lang=ja) (`schnakenberg-2d-boundary-modes`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/schnakenberg-2d-boundary-modes/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-2d-boundary-modes/?lang=ja#schnakenberg-2d-boundary-modes-ja-validation)

線形モードの連続・離散記号、角の面所有、平衡、物質収支を照合。K/Q/時間許容差感度を別に測り、参照が資格条件を満たさなければ精度・次数を未確定にします。 精度目標には、新しい細参照が同じ絶対・相対基準に合格した場合だけその参照を用います。旧参照の不合格を合格へ読み替えません。

- [Schnakenberg：2D境界と初期モード](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-schnakenberg-2d-boundary-modes-ja) (`schnakenberg-2d-boundary-modes`; 同じ問題の参照 · 有限格子の数値参照)

短時間の小振幅・固定初期値です。一般的な模様選択、成長後の成熟パターン、原著図の再現は主張しません。有限の参照差を連続体誤差の厳密上界と呼びません。
## 前提・単位・境界

[0,2π]²、T=2、a=0.1,b=0.9,Du=0.01,Dv=1。平衡(1,0.9)のまわりで3初期値と12/24/48セル、一定の非周期境界を使います。

**編集上の補足**

短時間の小振幅・固定初期値です。一般的な模様選択、成長後の成熟パターン、原著図の再現は主張しません。有限の参照差を連続体誤差の厳密上界と呼びません。

## 採用した計算法

セル平均のCN拡散と局所陰的中点反応をStrang分割します。独立参照は正規直交sin/cos Galerkin、K12/18,Q96/192と2許容誤差の4列を全初期値で残します。 元のDirichlet K12/18参照は初回の相対資格基準を満たさなかったため、失敗を残し、D境界だけK24/32・Q128/192の4参照を追加します。

$$
u_t=.01\Delta u+.1-u+u^2v,\qquad v_t=\Delta v+.9-u^2v
$$

## 比較・検証

線形モードの連続・離散記号、角の面所有、平衡、物質収支を照合。K/Q/時間許容差感度を別に測り、参照が資格条件を満たさなければ精度・次数を未確定にします。 精度目標には、新しい細参照が同じ絶対・相対基準に合格した場合だけその参照を用います。旧参照の不合格を合格へ読み替えません。

## 確認の限界

短時間の小振幅・固定初期値です。一般的な模様選択、成長後の成熟パターン、原著図の再現は主張しません。有限の参照差を連続体誤差の厳密上界と呼びません。

## 調査した目標：達成16・未達0・未確定1（全17）

必須の検証合格と元の調査目標の達成は別です。達成・未達は保存された比較結果を示し、統計的な認定ではありません。未確定と別の不確かさ区分を保持し、nullをfalseや0に置き換えません。

[元の保存結果 / JSON](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/result.json)

<details><summary>全目標の記録を読む</summary>

```json
{
  "schema_version": 1,
  "counts": {
    "met": 16,
    "unmet": 0,
    "unresolved": 1,
    "total": 17
  },
  "goals": [
    {
      "name": "Schnakenberg/positivity/N-mode42/12",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "minimum": 0.8880521241619382
      }
    },
    {
      "name": "Schnakenberg/positivity/N-mode42/24",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "minimum": 0.8860615561401685
      }
    },
    {
      "name": "Schnakenberg/positivity/N-mode42/48",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "minimum": 0.8855372535923153
      }
    },
    {
      "name": "Schnakenberg/space-finest/N-mode42",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 8.250442438972883e-05,
        "target": 0.02
      }
    },
    {
      "name": "Schnakenberg/space-order/N-mode42",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 1.944655350128315,
        "target": 1.6
      }
    },
    {
      "name": "Schnakenberg/positivity/N-mixed/12",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "minimum": 0.8798143344957898
      }
    },
    {
      "name": "Schnakenberg/positivity/N-mixed/24",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "minimum": 0.8771054043233121
      }
    },
    {
      "name": "Schnakenberg/positivity/N-mixed/48",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "minimum": 0.8763952220795853
      }
    },
    {
      "name": "Schnakenberg/space-finest/N-mixed",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.00011769804580841203,
        "target": 0.02
      }
    },
    {
      "name": "Schnakenberg/space-order/N-mixed",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 1.9477700373628166,
        "target": 1.6
      }
    },
    {
      "name": "Schnakenberg/time-order",
      "observed": null,
      "outcome": "unresolved",
      "stored": {
        "observed": null,
        "actual": null,
        "target": 1.7
      }
    },
    {
      "name": "Schnakenberg/time-contamination",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 1.1208580182516432e-07,
        "finest_spatial_discrepancy": 0.00011769804580841203,
        "scope": "Secondorder Richardson indicator,notcertifiederrorbound"
      }
    },
    {
      "name": "Schnakenberg/positivity/D-mode42/12",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "minimum": 0.8862155577223321
      }
    },
    {
      "name": "Schnakenberg/positivity/D-mode42/24",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "minimum": 0.8860670448524426
      }
    },
    {
      "name": "Schnakenberg/positivity/D-mode42/48",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "minimum": 0.8855435379971976
      }
    },
    {
      "name": "Schnakenberg/space-finest/D-mode42",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 8.370124740819662e-05,
        "target": 0.02
      }
    },
    {
      "name": "Schnakenberg/space-order/D-mode42",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 1.9463235349282928,
        "target": 1.6
      }
    }
  ],
  "classification_basis": "stored observed comparison; separate uncertainty classifications retained",
  "source": {
    "collection": "study_goals",
    "json_pointer": "/study_goals",
    "prefix": "Schnakenberg/",
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
    "fixed_records": 33,
    "Schnakenberg/positivity/N-mode42/12/minimum": 0.8880521241619382,
    "Schnakenberg/positivity/N-mode42/24/minimum": 0.8860615561401685,
    "Schnakenberg/positivity/N-mode42/48/minimum": 0.8855372535923153,
    "Schnakenberg/space-finest/N-mode42/actual": 8.250442438972883e-05,
    "Schnakenberg/space-order/N-mode42/actual": 1.944655350128315,
    "Schnakenberg/positivity/N-mixed/12/minimum": 0.8798143344957898,
    "Schnakenberg/positivity/N-mixed/24/minimum": 0.8771054043233121,
    "Schnakenberg/positivity/N-mixed/48/minimum": 0.8763952220795853,
    "Schnakenberg/space-finest/N-mixed/actual": 0.00011769804580841203,
    "Schnakenberg/space-order/N-mixed/actual": 1.9477700373628166,
    "Schnakenberg/time-contamination/actual": 1.1208580182516432e-07,
    "Schnakenberg/positivity/D-mode42/12/minimum": 0.8862155577223321,
    "Schnakenberg/positivity/D-mode42/24/minimum": 0.8860670448524426,
    "Schnakenberg/positivity/D-mode42/48/minimum": 0.8855435379971976,
    "Schnakenberg/space-finest/D-mode42/actual": 8.370124740819662e-05,
    "Schnakenberg/space-order/D-mode42/actual": 1.9463235349282928
  },
  "checks": {
    "Schnakenberg/mode/N/1/1/12": true,
    "Schnakenberg/exp/N/1/1/12/0.1": true,
    "Schnakenberg/exp/N/1/1/12/0.5": true,
    "Schnakenberg/exp/N/1/1/12/1.0": true,
    "Schnakenberg/mode/N/1/1/24": true,
    "Schnakenberg/exp/N/1/1/24/0.1": true,
    "Schnakenberg/exp/N/1/1/24/0.5": true,
    "Schnakenberg/exp/N/1/1/24/1.0": true,
    "Schnakenberg/mode/N/1/1/48": true,
    "Schnakenberg/exp/N/1/1/48/0.1": true,
    "Schnakenberg/exp/N/1/1/48/0.5": true,
    "Schnakenberg/exp/N/1/1/48/1.0": true,
    "Schnakenberg/mode/N/4/2/12": true,
    "Schnakenberg/exp/N/4/2/12/0.1": true,
    "Schnakenberg/exp/N/4/2/12/0.5": true,
    "Schnakenberg/exp/N/4/2/12/1.0": true,
    "Schnakenberg/mode/N/4/2/24": true,
    "Schnakenberg/exp/N/4/2/24/0.1": true,
    "Schnakenberg/exp/N/4/2/24/0.5": true,
    "Schnakenberg/exp/N/4/2/24/1.0": true,
    "Schnakenberg/mode/N/4/2/48": true,
    "Schnakenberg/exp/N/4/2/48/0.1": true,
    "Schnakenberg/exp/N/4/2/48/0.5": true,
    "Schnakenberg/exp/N/4/2/48/1.0": true,
    "Schnakenberg/mode/N/3/1/12": true,
    "Schnakenberg/exp/N/3/1/12/0.1": true,
    "Schnakenberg/exp/N/3/1/12/0.5": true,
    "Schnakenberg/exp/N/3/1/12/1.0": true,
    "Schnakenberg/mode/N/3/1/24": true,
    "Schnakenberg/exp/N/3/1/24/0.1": true,
    "Schnakenberg/exp/N/3/1/24/0.5": true,
    "Schnakenberg/exp/N/3/1/24/1.0": true,
    "Schnakenberg/mode/N/3/1/48": true,
    "Schnakenberg/exp/N/3/1/48/0.1": true,
    "Schnakenberg/exp/N/3/1/48/0.5": true,
    "Schnakenberg/exp/N/3/1/48/1.0": true,
    "Schnakenberg/mode/D/1/1/12": true,
    "Schnakenberg/exp/D/1/1/12/0.1": true,
    "Schnakenberg/exp/D/1/1/12/0.5": true,
    "Schnakenberg/exp/D/1/1/12/1.0": true,
    "Schnakenberg/mode/D/1/1/24": true,
    "Schnakenberg/exp/D/1/1/24/0.1": true,
    "Schnakenberg/exp/D/1/1/24/0.5": true,
    "Schnakenberg/exp/D/1/1/24/1.0": true,
    "Schnakenberg/mode/D/1/1/48": true,
    "Schnakenberg/exp/D/1/1/48/0.1": true,
    "Schnakenberg/exp/D/1/1/48/0.5": true,
    "Schnakenberg/exp/D/1/1/48/1.0": true,
    "Schnakenberg/mode/D/4/2/12": true,
    "Schnakenberg/exp/D/4/2/12/0.1": true,
    "Schnakenberg/exp/D/4/2/12/0.5": true,
    "Schnakenberg/exp/D/4/2/12/1.0": true,
    "Schnakenberg/mode/D/4/2/24": true,
    "Schnakenberg/exp/D/4/2/24/0.1": true,
    "Schnakenberg/exp/D/4/2/24/0.5": true,
    "Schnakenberg/exp/D/4/2/24/1.0": true,
    "Schnakenberg/mode/D/4/2/48": true,
    "Schnakenberg/exp/D/4/2/48/0.1": true,
    "Schnakenberg/exp/D/4/2/48/0.5": true,
    "Schnakenberg/exp/D/4/2/48/1.0": true,
    "Schnakenberg/mode/D/3/1/12": true,
    "Schnakenberg/exp/D/3/1/12/0.1": true,
    "Schnakenberg/exp/D/3/1/12/0.5": true,
    "Schnakenberg/exp/D/3/1/12/1.0": true,
    "Schnakenberg/mode/D/3/1/24": true,
    "Schnakenberg/exp/D/3/1/24/0.1": true,
    "Schnakenberg/exp/D/3/1/24/0.5": true,
    "Schnakenberg/exp/D/3/1/24/1.0": true,
    "Schnakenberg/mode/D/3/1/48": true,
    "Schnakenberg/exp/D/3/1/48/0.1": true,
    "Schnakenberg/exp/D/3/1/48/0.5": true,
    "Schnakenberg/exp/D/3/1/48/1.0": true,
    "Schnakenberg/equilibrium-face-zero": true,
    "Schnakenberg/constant-equilibrium/N": true,
    "Schnakenberg/constant-equilibrium/D": true,
    "Schnakenberg/wrong-boundary-control": true,
    "Schnakenberg/corner-doublecount-control": true,
    "Schnakenberg/linear-action-count": true,
    "Schnakenberg/ledger/N-mode42/12": true,
    "Schnakenberg/ledger/N-mode42/24": true,
    "Schnakenberg/ledger/N-mode42/48": true,
    "Schnakenberg/reference/N-mode42": true,
    "Schnakenberg/ledger/N-mixed/12": true,
    "Schnakenberg/ledger/N-mixed/24": true,
    "Schnakenberg/ledger/N-mixed/48": true,
    "Schnakenberg/reference/N-mixed": true,
    "Schnakenberg/ledger/D-mode42/12": true,
    "Schnakenberg/ledger/D-mode42/24": true,
    "Schnakenberg/ledger/D-mode42/48": true,
    "Schnakenberg/reference/D-mode42": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-2d-boundary-modes/index.json

![精度・参照・統計の実測値と未達目標を分けて表示します。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/schnakenberg-2d-boundary-modes-diagnostics.png)

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

- Schnakenberg(1979), Simple chemical reaction systems with limit cycle behaviour. https://pubmed.ncbi.nlm.nih.gov/537379/; review_level=selected-primary-or-bibliographic-see-provenance
source-reading.jsonに実際の読取範囲と未読部分を記録。原著の全式・全図の再現とは主張しません。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Schnakenberg:2D boundaries and initial modes

Compare two Neumann perturbations and a Dirichlet perturbation against nonlinear Galerkin references.

**Methods used**

- [Crank–Nicolson](https://hrkoyama.github.io/numerical-methods-atlas/methods/crank-nicolson/?lang=en) (`crank-nicolson`)
- [Strang splitting](https://hrkoyama.github.io/numerical-methods-atlas/methods/strang-splitting/?lang=en) (`strang-splitting`)
- [Dormand–Prince RK45](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk45/?lang=en) (`rk45`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-2d-boundary-modes/?lang=en#schnakenberg-2d-boundary-modes-en-algorithm)

Strang-split cell-averageCN diffusion and local implicit-midpoint reactions. Independent orthonormal sine/cosine Galerkin references retain four K12/18,Q96/192,tolerance rows for every initial condition. The original Dirichlet K12/18 reference failed its first relative qualification. Preserve that failure and add four D-only K24/32,Q128/192 reference actions.

$$
u_t=.01\Delta u+.1-u+u^2v,\qquad v_t=\Delta v+.9-u^2v
$$

- [Schnakenberg reaction–diffusion](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-schnakenberg-en) (`bio-schnakenberg`)

On[0,2π]² toT2,use a.1,b.9,Du.01,Dv1. Compare three perturbations of(1,.9),12/24/48cell grids and fixed nonperiodic boundary conditions.


**Problem figure**

![Schnakenberg:2D boundaries and initial modes: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/schnakenberg-2d-boundary-modes.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Schnakenberg:2D boundaries and initial modes](https://hrkoyama.github.io/numerical-methods-atlas/problems/schnakenberg-2d-boundary-modes/?lang=en) (`schnakenberg-2d-boundary-modes`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/schnakenberg-2d-boundary-modes/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-2d-boundary-modes/?lang=en#schnakenberg-2d-boundary-modes-en-validation)

Check continuum/discrete linear symbols, corner-face ownership, equilibrium and mass ledgers. Separate K/Q/tolerance sensitivity; unqualified references leave related accuracy/order unresolved. Use the new finer reference for accuracy goals only after the same absolute/relative criteria pass; the original failed qualification is retained.

- [Schnakenberg:2D boundaries and initial modes](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-schnakenberg-2d-boundary-modes-en) (`schnakenberg-2d-boundary-modes`; Same-problem reference · Finite-grid numerical reference)

This short small-amplitude study does not establish general pattern selection, mature patterns or reproduction of original figures. Finite reference differences are not rigorous continuum error bounds.
## Assumptions, units and boundaries

On[0,2π]² toT2,use a.1,b.9,Du.01,Dv1. Compare three perturbations of(1,.9),12/24/48cell grids and fixed nonperiodic boundary conditions.

**Editorial clarification**

This short small-amplitude study does not establish general pattern selection, mature patterns or reproduction of original figures. Finite reference differences are not rigorous continuum error bounds.

## Adopted numerical method

Strang-split cell-averageCN diffusion and local implicit-midpoint reactions. Independent orthonormal sine/cosine Galerkin references retain four K12/18,Q96/192,tolerance rows for every initial condition. The original Dirichlet K12/18 reference failed its first relative qualification. Preserve that failure and add four D-only K24/32,Q128/192 reference actions.

$$
u_t=.01\Delta u+.1-u+u^2v,\qquad v_t=\Delta v+.9-u^2v
$$

## References and validation

Check continuum/discrete linear symbols, corner-face ownership, equilibrium and mass ledgers. Separate K/Q/tolerance sensitivity; unqualified references leave related accuracy/order unresolved. Use the new finer reference for accuracy goals only after the same absolute/relative criteria pass; the original failed qualification is retained.

## Limits

This short small-amplitude study does not establish general pattern selection, mature patterns or reproduction of original figures. Finite reference differences are not rigorous continuum error bounds.

## Study goals: 16 met, 0 unmet, 1 unresolved (17 total)

Mandatory qualification is separate from study-goal attainment. Met/unmet follow stored comparisons, not statistical certification. Unresolved and separate uncertainty classifications are retained; null is not replaced by false or zero.

[Original saved results / JSON](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/result.json)

<details><summary>Read every study-goal record</summary>

```json
{
  "schema_version": 1,
  "counts": {
    "met": 16,
    "unmet": 0,
    "unresolved": 1,
    "total": 17
  },
  "goals": [
    {
      "name": "Schnakenberg/positivity/N-mode42/12",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "minimum": 0.8880521241619382
      }
    },
    {
      "name": "Schnakenberg/positivity/N-mode42/24",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "minimum": 0.8860615561401685
      }
    },
    {
      "name": "Schnakenberg/positivity/N-mode42/48",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "minimum": 0.8855372535923153
      }
    },
    {
      "name": "Schnakenberg/space-finest/N-mode42",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 8.250442438972883e-05,
        "target": 0.02
      }
    },
    {
      "name": "Schnakenberg/space-order/N-mode42",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 1.944655350128315,
        "target": 1.6
      }
    },
    {
      "name": "Schnakenberg/positivity/N-mixed/12",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "minimum": 0.8798143344957898
      }
    },
    {
      "name": "Schnakenberg/positivity/N-mixed/24",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "minimum": 0.8771054043233121
      }
    },
    {
      "name": "Schnakenberg/positivity/N-mixed/48",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "minimum": 0.8763952220795853
      }
    },
    {
      "name": "Schnakenberg/space-finest/N-mixed",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.00011769804580841203,
        "target": 0.02
      }
    },
    {
      "name": "Schnakenberg/space-order/N-mixed",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 1.9477700373628166,
        "target": 1.6
      }
    },
    {
      "name": "Schnakenberg/time-order",
      "observed": null,
      "outcome": "unresolved",
      "stored": {
        "observed": null,
        "actual": null,
        "target": 1.7
      }
    },
    {
      "name": "Schnakenberg/time-contamination",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 1.1208580182516432e-07,
        "finest_spatial_discrepancy": 0.00011769804580841203,
        "scope": "Secondorder Richardson indicator,notcertifiederrorbound"
      }
    },
    {
      "name": "Schnakenberg/positivity/D-mode42/12",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "minimum": 0.8862155577223321
      }
    },
    {
      "name": "Schnakenberg/positivity/D-mode42/24",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "minimum": 0.8860670448524426
      }
    },
    {
      "name": "Schnakenberg/positivity/D-mode42/48",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "minimum": 0.8855435379971976
      }
    },
    {
      "name": "Schnakenberg/space-finest/D-mode42",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 8.370124740819662e-05,
        "target": 0.02
      }
    },
    {
      "name": "Schnakenberg/space-order/D-mode42",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 1.9463235349282928,
        "target": 1.6
      }
    }
  ],
  "classification_basis": "stored observed comparison; separate uncertainty classifications retained",
  "source": {
    "collection": "study_goals",
    "json_pointer": "/study_goals",
    "prefix": "Schnakenberg/",
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
    "fixed_records": 33,
    "Schnakenberg/positivity/N-mode42/12/minimum": 0.8880521241619382,
    "Schnakenberg/positivity/N-mode42/24/minimum": 0.8860615561401685,
    "Schnakenberg/positivity/N-mode42/48/minimum": 0.8855372535923153,
    "Schnakenberg/space-finest/N-mode42/actual": 8.250442438972883e-05,
    "Schnakenberg/space-order/N-mode42/actual": 1.944655350128315,
    "Schnakenberg/positivity/N-mixed/12/minimum": 0.8798143344957898,
    "Schnakenberg/positivity/N-mixed/24/minimum": 0.8771054043233121,
    "Schnakenberg/positivity/N-mixed/48/minimum": 0.8763952220795853,
    "Schnakenberg/space-finest/N-mixed/actual": 0.00011769804580841203,
    "Schnakenberg/space-order/N-mixed/actual": 1.9477700373628166,
    "Schnakenberg/time-contamination/actual": 1.1208580182516432e-07,
    "Schnakenberg/positivity/D-mode42/12/minimum": 0.8862155577223321,
    "Schnakenberg/positivity/D-mode42/24/minimum": 0.8860670448524426,
    "Schnakenberg/positivity/D-mode42/48/minimum": 0.8855435379971976,
    "Schnakenberg/space-finest/D-mode42/actual": 8.370124740819662e-05,
    "Schnakenberg/space-order/D-mode42/actual": 1.9463235349282928
  },
  "checks": {
    "Schnakenberg/mode/N/1/1/12": true,
    "Schnakenberg/exp/N/1/1/12/0.1": true,
    "Schnakenberg/exp/N/1/1/12/0.5": true,
    "Schnakenberg/exp/N/1/1/12/1.0": true,
    "Schnakenberg/mode/N/1/1/24": true,
    "Schnakenberg/exp/N/1/1/24/0.1": true,
    "Schnakenberg/exp/N/1/1/24/0.5": true,
    "Schnakenberg/exp/N/1/1/24/1.0": true,
    "Schnakenberg/mode/N/1/1/48": true,
    "Schnakenberg/exp/N/1/1/48/0.1": true,
    "Schnakenberg/exp/N/1/1/48/0.5": true,
    "Schnakenberg/exp/N/1/1/48/1.0": true,
    "Schnakenberg/mode/N/4/2/12": true,
    "Schnakenberg/exp/N/4/2/12/0.1": true,
    "Schnakenberg/exp/N/4/2/12/0.5": true,
    "Schnakenberg/exp/N/4/2/12/1.0": true,
    "Schnakenberg/mode/N/4/2/24": true,
    "Schnakenberg/exp/N/4/2/24/0.1": true,
    "Schnakenberg/exp/N/4/2/24/0.5": true,
    "Schnakenberg/exp/N/4/2/24/1.0": true,
    "Schnakenberg/mode/N/4/2/48": true,
    "Schnakenberg/exp/N/4/2/48/0.1": true,
    "Schnakenberg/exp/N/4/2/48/0.5": true,
    "Schnakenberg/exp/N/4/2/48/1.0": true,
    "Schnakenberg/mode/N/3/1/12": true,
    "Schnakenberg/exp/N/3/1/12/0.1": true,
    "Schnakenberg/exp/N/3/1/12/0.5": true,
    "Schnakenberg/exp/N/3/1/12/1.0": true,
    "Schnakenberg/mode/N/3/1/24": true,
    "Schnakenberg/exp/N/3/1/24/0.1": true,
    "Schnakenberg/exp/N/3/1/24/0.5": true,
    "Schnakenberg/exp/N/3/1/24/1.0": true,
    "Schnakenberg/mode/N/3/1/48": true,
    "Schnakenberg/exp/N/3/1/48/0.1": true,
    "Schnakenberg/exp/N/3/1/48/0.5": true,
    "Schnakenberg/exp/N/3/1/48/1.0": true,
    "Schnakenberg/mode/D/1/1/12": true,
    "Schnakenberg/exp/D/1/1/12/0.1": true,
    "Schnakenberg/exp/D/1/1/12/0.5": true,
    "Schnakenberg/exp/D/1/1/12/1.0": true,
    "Schnakenberg/mode/D/1/1/24": true,
    "Schnakenberg/exp/D/1/1/24/0.1": true,
    "Schnakenberg/exp/D/1/1/24/0.5": true,
    "Schnakenberg/exp/D/1/1/24/1.0": true,
    "Schnakenberg/mode/D/1/1/48": true,
    "Schnakenberg/exp/D/1/1/48/0.1": true,
    "Schnakenberg/exp/D/1/1/48/0.5": true,
    "Schnakenberg/exp/D/1/1/48/1.0": true,
    "Schnakenberg/mode/D/4/2/12": true,
    "Schnakenberg/exp/D/4/2/12/0.1": true,
    "Schnakenberg/exp/D/4/2/12/0.5": true,
    "Schnakenberg/exp/D/4/2/12/1.0": true,
    "Schnakenberg/mode/D/4/2/24": true,
    "Schnakenberg/exp/D/4/2/24/0.1": true,
    "Schnakenberg/exp/D/4/2/24/0.5": true,
    "Schnakenberg/exp/D/4/2/24/1.0": true,
    "Schnakenberg/mode/D/4/2/48": true,
    "Schnakenberg/exp/D/4/2/48/0.1": true,
    "Schnakenberg/exp/D/4/2/48/0.5": true,
    "Schnakenberg/exp/D/4/2/48/1.0": true,
    "Schnakenberg/mode/D/3/1/12": true,
    "Schnakenberg/exp/D/3/1/12/0.1": true,
    "Schnakenberg/exp/D/3/1/12/0.5": true,
    "Schnakenberg/exp/D/3/1/12/1.0": true,
    "Schnakenberg/mode/D/3/1/24": true,
    "Schnakenberg/exp/D/3/1/24/0.1": true,
    "Schnakenberg/exp/D/3/1/24/0.5": true,
    "Schnakenberg/exp/D/3/1/24/1.0": true,
    "Schnakenberg/mode/D/3/1/48": true,
    "Schnakenberg/exp/D/3/1/48/0.1": true,
    "Schnakenberg/exp/D/3/1/48/0.5": true,
    "Schnakenberg/exp/D/3/1/48/1.0": true,
    "Schnakenberg/equilibrium-face-zero": true,
    "Schnakenberg/constant-equilibrium/N": true,
    "Schnakenberg/constant-equilibrium/D": true,
    "Schnakenberg/wrong-boundary-control": true,
    "Schnakenberg/corner-doublecount-control": true,
    "Schnakenberg/linear-action-count": true,
    "Schnakenberg/ledger/N-mode42/12": true,
    "Schnakenberg/ledger/N-mode42/24": true,
    "Schnakenberg/ledger/N-mode42/48": true,
    "Schnakenberg/reference/N-mode42": true,
    "Schnakenberg/ledger/N-mixed/12": true,
    "Schnakenberg/ledger/N-mixed/24": true,
    "Schnakenberg/ledger/N-mixed/48": true,
    "Schnakenberg/reference/N-mixed": true,
    "Schnakenberg/ledger/D-mode42/12": true,
    "Schnakenberg/ledger/D-mode42/24": true,
    "Schnakenberg/ledger/D-mode42/48": true,
    "Schnakenberg/reference/D-mode42": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-2d-boundary-modes/index.json

![Separate actual accuracy,reference and statistical measurements,including unmet targets.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/schnakenberg-2d-boundary-modes-diagnostics.png)

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

- Schnakenberg(1979), Simple chemical reaction systems with limit cycle behaviour. https://pubmed.ncbi.nlm.nih.gov/537379/; review_level=selected-primary-or-bibliographic-see-provenance
Actual selected read scopes and unread limits are recorded in source-reading.json; no full original-paper equation/figure reproduction claim.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
