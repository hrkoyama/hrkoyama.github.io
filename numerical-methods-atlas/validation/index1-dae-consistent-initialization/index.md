# index-1 DAEの整合初期化と離散残差

既知の正枝を持つindex-1 DAEで初期化と後退Eulerの誤差・残差を分離します。

**使用手法**

- [微分代数方程式（DAE）](https://hrkoyama.github.io/numerical-methods-atlas/methods/dae/?lang=ja) (`dae`)
- [後退Euler法](https://hrkoyama.github.io/numerical-methods-atlas/methods/backward-euler/?lang=ja) (`backward-euler`)
- [Armijo減衰Newton法](https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=ja) (`newton`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/index1-dae-consistent-initialization/?lang=ja#index1-dae-consistent-initialization-ja-algorithm)

連立Newtonと同じ尺度のArmijo線探索を用い、特異な初期推測は修復せず記録します。

$$
F1=ydot+y-z+exp(-2t/3), F2=z^3-y^2
$$

$$
y=exp(-t), z=exp(-2t/3)
$$

- [半陽的index-1 DAE](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#index-one-dae-ja) (`index-one-dae`)

無次元・正枝。微分行と代数行の尺度はそれぞれ1で、最大ノルムを用います。


**問題の図**

![index-1 DAEの整合初期化と離散残差：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/index1-dae-consistent-initialization.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[index-1 DAEの整合初期化と離散残差](https://hrkoyama.github.io/numerical-methods-atlas/problems/index1-dae-consistent-initialization/?lang=ja) (`index1-dae-consistent-initialization`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/index1-dae-consistent-initialization/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/index1-dae-consistent-initialization/?lang=ja#index1-dae-consistent-initialization-ja-validation)

独立Decimal製造解・3つの離散根と3固定格子を比較し、一次誤差と代数拘束を確認します。

- [index-1 DAEの整合初期化と離散残差](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-index1-dae-consistent-initialization-ja) (`index1-dae-consistent-initialization`; 同じ問題の参照 · 製造解)

単一の製造正枝・固定BE計算です。IDA実行や一般DAEソルバーの検証ではありません。
## 前提・単位・境界

無次元・正枝。微分行と代数行の尺度はそれぞれ1で、最大ノルムを用います。

**編集上の補足**

単一の製造正枝・固定BE計算です。IDA実行や一般DAEソルバーの検証ではありません。 図の軌道・状態・時刻・反復の軸は、物理空間の次元を表しません。

## 採用した計算法

連立Newtonと同じ尺度のArmijo線探索を用い、特異な初期推測は修復せず記録します。

$$
F1=ydot+y-z+exp(-2t/3), F2=z^3-y^2
$$

$$
y=exp(-t), z=exp(-2t/3)
$$

## 比較・検証

独立Decimal製造解・3つの離散根と3固定格子を比較し、一次誤差と代数拘束を確認します。

## 確認の限界

単一の製造正枝・固定BE計算です。IDA実行や一般DAEソルバーの検証ではありません。

## 保存実測値と判定

```json
{
  "metrics": {
    "reference:three-independent-discrete-roots": 3.5860203695392556e-14,
    "initialize-0.5:root": 0.0,
    "initialize-2:root": 2.220446049250313e-16,
    "index1-BE-16:step-residual": 9.536815781530095e-14,
    "index1-BE-16:constraint": 9.536815781530095e-14,
    "index1-BE-16:MMS-bound": 0.017655667991177793,
    "index1-BE-32:step-residual": 1.5543122344752192e-15,
    "index1-BE-32:constraint": 4.440892098500626e-16,
    "index1-BE-32:MMS-bound": 0.00889059915166246,
    "index1-BE-64:step-residual": 3.552713678800501e-15,
    "index1-BE-64:constraint": 3.3306690738754696e-16,
    "index1-BE-64:MMS-bound": 0.0044611112911168704,
    "first-order-refinement": [
      0.989778852631791,
      0.9948775084516599
    ],
    "finest_max_state_error": 0.0044611112911168704,
    "observed_orders": [
      0.989778852631791,
      0.9948775084516599
    ],
    "one_step_reference_errors": [
      3.5860203695392556e-14,
      1.1102230246251565e-16,
      1.1102230246251565e-16
    ],
    "original_targets_met": 30,
    "original_targets_total": 30
  },
  "checks": {
    "reference:MMS-0": true,
    "reference:MMS-1": true,
    "reference:MMS-2": true,
    "reference:nonexpansive-positive-region": true,
    "reference:initial-differentiated-constraint": true,
    "reference:three-positive-branch-brackets": true,
    "reference:three-independent-discrete-roots": true,
    "initialize-0.5:root": true,
    "initialize-0.5:algebraic-residual": true,
    "initialize-2:root": true,
    "initialize-2:algebraic-residual": true,
    "initialize-0:expected-singular-status": true,
    "index1-BE-16:finite": true,
    "index1-BE-16:positive": true,
    "index1-BE-16:step-residual": true,
    "index1-BE-16:constraint": true,
    "index1-BE-16:MMS-bound": true,
    "index1-BE-32:finite": true,
    "index1-BE-32:positive": true,
    "index1-BE-32:step-residual": true,
    "index1-BE-32:constraint": true,
    "index1-BE-32:MMS-bound": true,
    "index1-BE-64:finite": true,
    "index1-BE-64:positive": true,
    "index1-BE-64:step-residual": true,
    "index1-BE-64:constraint": true,
    "index1-BE-64:MMS-bound": true,
    "first-order-refinement": true,
    "initial-F-and-hidden-constraint": true,
    "six-record-identities": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/index1-dae-consistent-initialization/index.json

![既知の正枝を持つindex-1 DAEで初期化と後退Eulerの誤差・残差を分離します。 保存配列から作図。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/index1-dae-consistent-initialization-preview.png)

既知の正枝を持つindex-1 DAEで初期化と後退Eulerの誤差・残差を分離します。 保存配列から作図。

![保存済み残差・拘束・収支を別表示。ゼロ値は対称対数軸で保持します。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/index1-dae-consistent-initialization-diagnostics.png)

保存済み残差・拘束・収支を別表示。ゼロ値は対称対数軸で保持します。

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/atlas-dae-controls-2026-11-24.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

## 出典と確認範囲

- SUNDIALS v7.1.1 IDA mathematics, section 5.2 [accessed 2026-11-24]. https://sundials.readthedocs.io/en/v7.1.1/ida/Mathematics_link.html; review_level=official-documentation-selected-equations
Residual form, BDF/Newton and consistent initialization sections selected. Section5.2 is not an IDA version. This authored MMS/BE solver is not IDA.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Consistent initialization and discrete residuals for an index-one DAE

Separate initialization, backward-Euler error and residuals on a known positive index-one DAE branch.

**Methods used**

- [Differential-algebraic equations / DAE](https://hrkoyama.github.io/numerical-methods-atlas/methods/dae/?lang=en) (`dae`)
- [Backward Euler](https://hrkoyama.github.io/numerical-methods-atlas/methods/backward-euler/?lang=en) (`backward-euler`)
- [Armijo-damped Newton](https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=en) (`newton`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/index1-dae-consistent-initialization/?lang=en#index1-dae-consistent-initialization-en-algorithm)

Use coupled Newton with an Armijo search in the same scaled norm, retaining rather than repairing a singular initial guess.

$$
F1=ydot+y-z+exp(-2t/3), F2=z^3-y^2
$$

$$
y=exp(-t), z=exp(-2t/3)
$$

- [Semi-explicit index-one DAE](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#index-one-dae-en) (`index-one-dae`)

Dimensionless positive branch; differential and algebraic row scales are both one, with the maximum norm.


**Problem figure**

![Consistent initialization and discrete residuals for an index-one DAE: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/index1-dae-consistent-initialization.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Consistent initialization and discrete residuals for an index-one DAE](https://hrkoyama.github.io/numerical-methods-atlas/problems/index1-dae-consistent-initialization/?lang=en) (`index1-dae-consistent-initialization`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/index1-dae-consistent-initialization/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/index1-dae-consistent-initialization/?lang=en#index1-dae-consistent-initialization-en-validation)

Compare independent Decimal manufactured states, three discrete roots and three fixed grids, checking first-order error and the algebraic constraint.

- [Consistent initialization and discrete residuals for an index-one DAE](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-index1-dae-consistent-initialization-en) (`index1-dae-consistent-initialization`; Same-problem reference · Manufactured solution)

One authored positive branch and fixed BE runs; no IDA execution or general DAE-solver qualification.
## Assumptions, units and boundaries

Dimensionless positive branch; differential and algebraic row scales are both one, with the maximum norm.

**Editorial clarification**

One authored positive branch and fixed BE runs; no IDA execution or general DAE-solver qualification. Axes for trajectories, states, time or iterations do not represent physical spatial dimensions.

## Adopted numerical method

Use coupled Newton with an Armijo search in the same scaled norm, retaining rather than repairing a singular initial guess.

$$
F1=ydot+y-z+exp(-2t/3), F2=z^3-y^2
$$

$$
y=exp(-t), z=exp(-2t/3)
$$

## References and validation

Compare independent Decimal manufactured states, three discrete roots and three fixed grids, checking first-order error and the algebraic constraint.

## Limits

One authored positive branch and fixed BE runs; no IDA execution or general DAE-solver qualification.

## Stored measurements and decisions

```json
{
  "metrics": {
    "reference:three-independent-discrete-roots": 3.5860203695392556e-14,
    "initialize-0.5:root": 0.0,
    "initialize-2:root": 2.220446049250313e-16,
    "index1-BE-16:step-residual": 9.536815781530095e-14,
    "index1-BE-16:constraint": 9.536815781530095e-14,
    "index1-BE-16:MMS-bound": 0.017655667991177793,
    "index1-BE-32:step-residual": 1.5543122344752192e-15,
    "index1-BE-32:constraint": 4.440892098500626e-16,
    "index1-BE-32:MMS-bound": 0.00889059915166246,
    "index1-BE-64:step-residual": 3.552713678800501e-15,
    "index1-BE-64:constraint": 3.3306690738754696e-16,
    "index1-BE-64:MMS-bound": 0.0044611112911168704,
    "first-order-refinement": [
      0.989778852631791,
      0.9948775084516599
    ],
    "finest_max_state_error": 0.0044611112911168704,
    "observed_orders": [
      0.989778852631791,
      0.9948775084516599
    ],
    "one_step_reference_errors": [
      3.5860203695392556e-14,
      1.1102230246251565e-16,
      1.1102230246251565e-16
    ],
    "original_targets_met": 30,
    "original_targets_total": 30
  },
  "checks": {
    "reference:MMS-0": true,
    "reference:MMS-1": true,
    "reference:MMS-2": true,
    "reference:nonexpansive-positive-region": true,
    "reference:initial-differentiated-constraint": true,
    "reference:three-positive-branch-brackets": true,
    "reference:three-independent-discrete-roots": true,
    "initialize-0.5:root": true,
    "initialize-0.5:algebraic-residual": true,
    "initialize-2:root": true,
    "initialize-2:algebraic-residual": true,
    "initialize-0:expected-singular-status": true,
    "index1-BE-16:finite": true,
    "index1-BE-16:positive": true,
    "index1-BE-16:step-residual": true,
    "index1-BE-16:constraint": true,
    "index1-BE-16:MMS-bound": true,
    "index1-BE-32:finite": true,
    "index1-BE-32:positive": true,
    "index1-BE-32:step-residual": true,
    "index1-BE-32:constraint": true,
    "index1-BE-32:MMS-bound": true,
    "index1-BE-64:finite": true,
    "index1-BE-64:positive": true,
    "index1-BE-64:step-residual": true,
    "index1-BE-64:constraint": true,
    "index1-BE-64:MMS-bound": true,
    "first-order-refinement": true,
    "initial-F-and-hidden-constraint": true,
    "six-record-identities": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/index1-dae-consistent-initialization/index.json

![Separate initialization, backward-Euler error and residuals on a known positive index-one DAE branch. Drawn from saved arrays.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/index1-dae-consistent-initialization-preview.png)

Separate initialization, backward-Euler error and residuals on a known positive index-one DAE branch. Drawn from saved arrays.

![Saved residuals, constraints and budgets shown separately; symmetric log axes retain zero values.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/index1-dae-consistent-initialization-diagnostics.png)

Saved residuals, constraints and budgets shown separately; symmetric log axes retain zero values.

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/atlas-dae-controls-2026-11-24.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

## Sources and review scope

- SUNDIALS v7.1.1 IDA mathematics, section 5.2 [accessed 2026-11-24]. https://sundials.readthedocs.io/en/v7.1.1/ida/Mathematics_link.html; review_level=official-documentation-selected-equations
Residual form, BDF/Newton and consistent initialization sections selected. Section5.2 is not an IDA version. This authored MMS/BE solver is not IDA.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
