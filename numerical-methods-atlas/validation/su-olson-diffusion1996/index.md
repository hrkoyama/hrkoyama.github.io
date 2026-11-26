# Su–Olson1996非平衡拡散

実際の輻射・物質2場とMarshak境界を進め、固定版ExactPackの独立積分参照と比較します。

**使用手法**

- [輻射輸送・モーメント法](https://hrkoyama.github.io/numerical-methods-atlas/methods/radiation-transport/?lang=ja) (`radiation-transport`)
- [後退Euler法](https://hrkoyama.github.io/numerical-methods-atlas/methods/backward-euler/?lang=ja) (`backward-euler`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-diffusion1996/?lang=ja#su-olson-diffusion1996-ja-algorithm)

保存的FVと後退Euler。輻射物質の反対sourceを同じSchur補元で結合し、Robinのβ+h/2半セル抵抗を用います。ε.25/2の同じ交換operatorも解析検査します。

$$
\epsilon u_\tau-u_{xx}=v-u,\quad v_\tau=u-v
$$

$$
u(0,\tau)-\frac2{\sqrt3}u_x(0,\tau)=1
$$

$$
\epsilon=4a/\alpha,\quad e_m/E_0=v/\epsilon,\quad \mathcal E=\epsilon u+v
$$

- [Su–Olson1996の非平衡拡散・物質交換](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#non-equilibrium-diffusion-exchange-ja) (`non-equilibrium-diffusion-exchange`)

無次元ε1、区間[0,16]、初期u=v0、左Robin入射、右0。128/256/512セルと時間半減・区間24probe。


**問題の図**

![Su–Olson1996非平衡拡散：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/results/su-olson-diffusion1996.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Su–Olson1996非平衡拡散](https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-diffusion1996/?lang=ja) (`su-olson-diffusion1996`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-diffusion1996/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-diffusion1996/?lang=ja#su-olson-diffusion1996-ja-validation)

独立参照54項目を輸送ケースと共有して資格済み。5主計算で独立u/v誤差、全stepの容量重み収支・正値、時間・有限領域差を分離します。

- [Su–Olson1996拡散：固定版の独立積分評価関数](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-su-olson-diffusion1996-ja) (`su-olson-diffusion1996`; 同じ問題の参照 · 半解析参照)

1996拡散であり1997角度輸送とは別です。原典本文は未読、公式ソフトの選択値を資格。物理単位の質量opacity解釈は使わず無次元関数を直接参照します。
## 前提・単位・境界

無次元ε1、区間[0,16]、初期u=v0、左Robin入射、右0。128/256/512セルと時間半減・区間24probe。

**編集上の補足**

1996拡散であり1997角度輸送とは別です。原典本文は未読、公式ソフトの選択値を資格。物理単位の質量opacity解釈は使わず無次元関数を直接参照します。

## 採用した計算法

保存的FVと後退Euler。輻射物質の反対sourceを同じSchur補元で結合し、Robinのβ+h/2半セル抵抗を用います。ε.25/2の同じ交換operatorも解析検査します。

$$
\epsilon u_\tau-u_{xx}=v-u,\quad v_\tau=u-v
$$

$$
u(0,\tau)-\frac2{\sqrt3}u_x(0,\tau)=1
$$

$$
\epsilon=4a/\alpha,\quad e_m/E_0=v/\epsilon,\quad \mathcal E=\epsilon u+v
$$

## 比較・検証

独立参照54項目を輸送ケースと共有して資格済み。5主計算で独立u/v誤差、全stepの容量重み収支・正値、時間・有限領域差を分離します。

## 確認の限界

1996拡散であり1997角度輸送とは別です。原典本文は未読、公式ソフトの選択値を資格。物理単位の質量opacity解釈は使わず無次元関数を直接参照します。

## 保存実測値と判定

```json
{
  "metrics": {
    "completed_primary_runs": 5,
    "reference_scope": "independent official diffusion integrals",
    "capacity_controls": [
      {
        "epsilon": 0.25,
        "method": "diffusion",
        "error": 0.00019032949653130515,
        "budget": 5.984102102729594e-14
      },
      {
        "epsilon": 0.25,
        "method": "transport",
        "error": 3.181825272147165e-07,
        "budget": 3.3306690738754696e-16
      },
      {
        "epsilon": 2.0,
        "method": "diffusion",
        "error": 0.000154177848556869,
        "budget": 7.460698725481052e-14
      },
      {
        "epsilon": 2.0,
        "method": "transport",
        "error": 7.721428540996556e-08,
        "budget": 1.199040866595169e-14
      }
    ]
  },
  "checks": {
    "su-olson-diffusion1996-n128/finite-positive": true,
    "su-olson-diffusion1996-n128/energy-budget": true,
    "su-olson-diffusion1996-n128/fixed-final-time": true,
    "su-olson-diffusion1996-n256/finite-positive": true,
    "su-olson-diffusion1996-n256/energy-budget": true,
    "su-olson-diffusion1996-n256/fixed-final-time": true,
    "su-olson-diffusion1996-n512/finite-positive": true,
    "su-olson-diffusion1996-n512/energy-budget": true,
    "su-olson-diffusion1996-n512/fixed-final-time": true,
    "su-olson-diffusion1996-half-dt/finite-positive": true,
    "su-olson-diffusion1996-half-dt/energy-budget": true,
    "su-olson-diffusion1996-half-dt/fixed-final-time": true,
    "su-olson-diffusion1996-far-domain/finite-positive": true,
    "su-olson-diffusion1996-far-domain/energy-budget": true,
    "su-olson-diffusion1996-far-domain/fixed-final-time": true,
    "refinement/1": true,
    "refinement/2": true,
    "finest-independent-rms": true,
    "finest-independent-linf": true,
    "separate-time-sensitivity": true,
    "finite-domain-sensitivity": true,
    "capacity/0.25/diffusion/error": true,
    "capacity/0.25/diffusion/budget": true,
    "capacity/0.25/transport/error": true,
    "capacity/0.25/transport/budget": true,
    "capacity/2.0/diffusion/error": true,
    "capacity/2.0/diffusion/budget": true,
    "capacity/2.0/transport/error": true,
    "capacity/2.0/transport/budget": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-diffusion1996/index.json

![保存した実計算場の科学プレビュー。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/results/su-olson-diffusion1996-preview.png)

保存した実計算場の科学プレビュー。

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/atlas-radiation-matter-2026-11-24-r2.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

## 出典と確認範囲

- LANL ExactPack developers;Timmes implementation provenance (2023). ExactPack1.7.5SuOlson pinned independent diffusion solution [accessed 2026-11-24]. https://github.com/lanl/ExactPack/tree/8718b61f281a9744ea7a3820c51800915e4636e9/exactpack/solvers/suolson; review_level=primary-official-software-full-three-module-text-and-qualified-selected-values
Read doc55/wrapper41/Timmes348lines;original1996paper abstract only. Serial original/tight selected integrals and independent PDE/Robin qualifiers passed before main. FullExactPack/base/libraries not audited.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Su–Olson1996 non-equilibrium diffusion

Advance actual radiation/material fields with the Marshak boundary and compare with independently qualified pinned ExactPack integrals.

**Methods used**

- [Radiation transport and moment methods](https://hrkoyama.github.io/numerical-methods-atlas/methods/radiation-transport/?lang=en) (`radiation-transport`)
- [Backward Euler](https://hrkoyama.github.io/numerical-methods-atlas/methods/backward-euler/?lang=en) (`backward-euler`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-diffusion1996/?lang=en#su-olson-diffusion1996-en-algorithm)

Conservative FV/backwardEuler with opposite exchange sources coupled by a shared Schur complement and Robin half-cell resistance beta+h/2. Analytic nonunitepsilon.25/2controls exercise the same exchange operators.

$$
\epsilon u_\tau-u_{xx}=v-u,\quad v_\tau=u-v
$$

$$
u(0,\tau)-\frac2{\sqrt3}u_x(0,\tau)=1
$$

$$
\epsilon=4a/\alpha,\quad e_m/E_0=v/\epsilon,\quad \mathcal E=\epsilon u+v
$$

- [Su–Olson1996 non-equilibrium diffusion and material exchange](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#non-equilibrium-diffusion-exchange-en) (`non-equilibrium-diffusion-exchange`)

Nondimensionalepsilon1,x0..16,initialu=v0,leftRobin inflow/right0;128/256/512cells plus half-step/domain24probes.


**Problem figure**

![Su–Olson1996 non-equilibrium diffusion: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/results/su-olson-diffusion1996.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Su–Olson1996 non-equilibrium diffusion](https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-diffusion1996/?lang=en) (`su-olson-diffusion1996`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-diffusion1996/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-diffusion1996/?lang=en#su-olson-diffusion1996-en-validation)

The independent54check reference study is shared with transport. Five primary runs separate u/vreferenceerror,all-step capacity-weighted budgets/positivity,time and finite-domain sensitivity.

- [Su–Olson1996 diffusion: pinned independent integral evaluator](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-su-olson-diffusion1996-en) (`su-olson-diffusion1996`; Same-problem reference · Semi-analytic reference)

This1996diffusion model is distinct from1997angular transport. Original paper fulltext unread;officialsoftware selected values qualified. Direct dimensionless functions avoid ambiguous mass-opacity physical-wrapper units.
## Assumptions, units and boundaries

Nondimensionalepsilon1,x0..16,initialu=v0,leftRobin inflow/right0;128/256/512cells plus half-step/domain24probes.

**Editorial clarification**

This1996diffusion model is distinct from1997angular transport. Original paper fulltext unread;officialsoftware selected values qualified. Direct dimensionless functions avoid ambiguous mass-opacity physical-wrapper units.

## Adopted numerical method

Conservative FV/backwardEuler with opposite exchange sources coupled by a shared Schur complement and Robin half-cell resistance beta+h/2. Analytic nonunitepsilon.25/2controls exercise the same exchange operators.

$$
\epsilon u_\tau-u_{xx}=v-u,\quad v_\tau=u-v
$$

$$
u(0,\tau)-\frac2{\sqrt3}u_x(0,\tau)=1
$$

$$
\epsilon=4a/\alpha,\quad e_m/E_0=v/\epsilon,\quad \mathcal E=\epsilon u+v
$$

## References and validation

The independent54check reference study is shared with transport. Five primary runs separate u/vreferenceerror,all-step capacity-weighted budgets/positivity,time and finite-domain sensitivity.

## Limits

This1996diffusion model is distinct from1997angular transport. Original paper fulltext unread;officialsoftware selected values qualified. Direct dimensionless functions avoid ambiguous mass-opacity physical-wrapper units.

## Stored measurements and decisions

```json
{
  "metrics": {
    "completed_primary_runs": 5,
    "reference_scope": "independent official diffusion integrals",
    "capacity_controls": [
      {
        "epsilon": 0.25,
        "method": "diffusion",
        "error": 0.00019032949653130515,
        "budget": 5.984102102729594e-14
      },
      {
        "epsilon": 0.25,
        "method": "transport",
        "error": 3.181825272147165e-07,
        "budget": 3.3306690738754696e-16
      },
      {
        "epsilon": 2.0,
        "method": "diffusion",
        "error": 0.000154177848556869,
        "budget": 7.460698725481052e-14
      },
      {
        "epsilon": 2.0,
        "method": "transport",
        "error": 7.721428540996556e-08,
        "budget": 1.199040866595169e-14
      }
    ]
  },
  "checks": {
    "su-olson-diffusion1996-n128/finite-positive": true,
    "su-olson-diffusion1996-n128/energy-budget": true,
    "su-olson-diffusion1996-n128/fixed-final-time": true,
    "su-olson-diffusion1996-n256/finite-positive": true,
    "su-olson-diffusion1996-n256/energy-budget": true,
    "su-olson-diffusion1996-n256/fixed-final-time": true,
    "su-olson-diffusion1996-n512/finite-positive": true,
    "su-olson-diffusion1996-n512/energy-budget": true,
    "su-olson-diffusion1996-n512/fixed-final-time": true,
    "su-olson-diffusion1996-half-dt/finite-positive": true,
    "su-olson-diffusion1996-half-dt/energy-budget": true,
    "su-olson-diffusion1996-half-dt/fixed-final-time": true,
    "su-olson-diffusion1996-far-domain/finite-positive": true,
    "su-olson-diffusion1996-far-domain/energy-budget": true,
    "su-olson-diffusion1996-far-domain/fixed-final-time": true,
    "refinement/1": true,
    "refinement/2": true,
    "finest-independent-rms": true,
    "finest-independent-linf": true,
    "separate-time-sensitivity": true,
    "finite-domain-sensitivity": true,
    "capacity/0.25/diffusion/error": true,
    "capacity/0.25/diffusion/budget": true,
    "capacity/0.25/transport/error": true,
    "capacity/0.25/transport/budget": true,
    "capacity/2.0/diffusion/error": true,
    "capacity/2.0/diffusion/budget": true,
    "capacity/2.0/transport/error": true,
    "capacity/2.0/transport/budget": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-diffusion1996/index.json

![Scientific preview from the actual saved numerical fields.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/results/su-olson-diffusion1996-preview.png)

Scientific preview from the actual saved numerical fields.

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/atlas-radiation-matter-2026-11-24-r2.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

## Sources and review scope

- LANL ExactPack developers;Timmes implementation provenance (2023). ExactPack1.7.5SuOlson pinned independent diffusion solution [accessed 2026-11-24]. https://github.com/lanl/ExactPack/tree/8718b61f281a9744ea7a3820c51800915e4636e9/exactpack/solvers/suolson; review_level=primary-official-software-full-three-module-text-and-qualified-selected-values
Read doc55/wrapper41/Timmes348lines;original1996paper abstract only. Serial original/tight selected integrals and independent PDE/Robin qualifiers passed before main. FullExactPack/base/libraries not audited.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
