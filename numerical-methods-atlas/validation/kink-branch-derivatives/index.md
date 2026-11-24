# 非滑らか点・分岐・停止条件の微分範囲

古典微分・一方向微分・実行trace微分を、kinkと停止分岐の固定例で区別します。

**使用手法**

- [自動微分](https://hrkoyama.github.io/numerical-methods-atlas/methods/automatic-differentiation/?lang=ja) (`automatic-differentiation`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/kink-branch-derivatives/?lang=ja#kink-branch-derivatives-ja-algorithm)

strict nondifferentiableを明示し、停止前<=判定の実行分岐だけを記録します。

$$
x_(k+1)=.5(x_k+theta), |x_k-theta|<=1/8
$$

$$
D max(0,0)[da,db]=max(da,db)
$$

- [有限次元非線形写像・根と微分作用](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#finite-dimensional-nonlinear-map-ja) (`finite-dimensional-nonlinear-map`)

小さな固定入力・実数・無次元。詳しい入力と適用範囲は対応する契約に限定します。


**問題の図**

![非滑らか点・分岐・停止条件の微分範囲：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/results/kink-branch-derivatives.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[非滑らか点・分岐・停止条件の微分範囲](https://hrkoyama.github.io/numerical-methods-atlas/problems/kink-branch-derivatives/?lang=ja) (`kink-branch-derivatives`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/kink-branch-derivatives/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/kink-branch-derivatives/?lang=ja#kink-branch-derivatives-ja-validation)

固定入力・独立参照・保存候補・全判定を同じ120秒予算内で検証します。数値合格と診断用非収束を区別します。

- [非滑らかな離散写像：一方向微分と実行trace](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-kink-branch-derivatives-ja) (`kink-branch-derivatives`; 同じ問題の参照 · 解析参照)

選択した分岐の微分は普遍的なsubgradientや非滑らかな写像の線形微分ではありません。
## 前提・単位・境界

小さな固定入力・実数・無次元。詳しい入力と適用範囲は対応する契約に限定します。

**編集上の補足**

選択した分岐の微分は普遍的なsubgradientや非滑らかな写像の線形微分ではありません。 図の座標は有限次元の変数・反復・診断で、物理空間の次元やPDE境界を表しません。

## 採用した計算法

strict nondifferentiableを明示し、停止前<=判定の実行分岐だけを記録します。

$$
x_(k+1)=.5(x_k+theta), |x_k-theta|<=1/8
$$

$$
D max(0,0)[da,db]=max(da,db)
$$

## 比較・検証

固定入力・独立参照・保存候補・全判定を同じ120秒予算内で検証します。数値合格と診断用非収束を区別します。

## 確認の限界

選択した分岐の微分は普遍的なsubgradientや非滑らかな写像の線形微分ではありません。

## 保存実測値と判定

```json
{
  "metrics": {
    "max_smooth_slope_oracle_error": 0.0,
    "max_fixed_trace_slope_error": 0.0,
    "stop_switch_jump": 0.0625,
    "max_jump_quotient_identity_error": 0.0,
    "inactive_invalid_branch_calls": 0
  },
  "checks": {
    "abs-0--1/category": true,
    "abs-0--1/finite_oracle_values": true,
    "abs-0-1/category": true,
    "abs-0-1/finite_oracle_values": true,
    "abs-1--1/category": true,
    "abs-1--1/finite_oracle_values": true,
    "abs-1-1/category": true,
    "abs-1-1/finite_oracle_values": true,
    "abs-2--1/category": true,
    "abs-2--1/finite_oracle_values": true,
    "abs-2-1/category": true,
    "abs-2-1/finite_oracle_values": true,
    "abs-3--1/category": true,
    "abs-3--1/finite_oracle_values": true,
    "abs-3-1/category": true,
    "abs-3-1/finite_oracle_values": true,
    "abs-4--1/category": true,
    "abs-4--1/finite_oracle_values": true,
    "abs-4-1/category": true,
    "abs-4-1/finite_oracle_values": true,
    "abs-5--1/category": true,
    "abs-5--1/finite_oracle_values": true,
    "abs-5-1/category": true,
    "abs-5-1/finite_oracle_values": true,
    "abs-6--1/category": true,
    "abs-6--1/finite_oracle_values": true,
    "abs-6-1/category": true,
    "abs-6-1/finite_oracle_values": true,
    "relu-0--1/category": true,
    "relu-0--1/finite_oracle_values": true,
    "relu-0-1/category": true,
    "relu-0-1/finite_oracle_values": true,
    "relu-1--1/category": true,
    "relu-1--1/finite_oracle_values": true,
    "relu-1-1/category": true,
    "relu-1-1/finite_oracle_values": true,
    "relu-2--1/category": true,
    "relu-2--1/finite_oracle_values": true,
    "relu-2-1/category": true,
    "relu-2-1/finite_oracle_values": true,
    "relu-3--1/category": true,
    "relu-3--1/finite_oracle_values": true,
    "relu-3-1/category": true,
    "relu-3-1/finite_oracle_values": true,
    "relu-4--1/category": true,
    "relu-4--1/finite_oracle_values": true,
    "relu-4-1/category": true,
    "relu-4-1/finite_oracle_values": true,
    "relu-5--1/category": true,
    "relu-5--1/finite_oracle_values": true,
    "relu-5-1/category": true,
    "relu-5-1/finite_oracle_values": true,
    "relu-6--1/category": true,
    "relu-6--1/finite_oracle_values": true,
    "relu-6-1/category": true,
    "relu-6-1/finite_oracle_values": true,
    "clip-0--1/category": true,
    "clip-0--1/finite_oracle_values": true,
    "clip-0-1/category": true,
    "clip-0-1/finite_oracle_values": true,
    "clip-1--1/category": true,
    "clip-1--1/finite_oracle_values": true,
    "clip-1-1/category": true,
    "clip-1-1/finite_oracle_values": true,
    "clip-2--1/category": true,
    "clip-2--1/finite_oracle_values": true,
    "clip-2-1/category": true,
    "clip-2-1/finite_oracle_values": true,
    "clip-3--1/category": true,
    "clip-3--1/finite_oracle_values": true,
    "clip-3-1/category": true,
    "clip-3-1/finite_oracle_values": true,
    "clip-4--1/category": true,
    "clip-4--1/finite_oracle_values": true,
    "clip-4-1/category": true,
    "clip-4-1/finite_oracle_values": true,
    "clip-5--1/category": true,
    "clip-5--1/finite_oracle_values": true,
    "clip-5-1/category": true,
    "clip-5-1/finite_oracle_values": true,
    "clip-6--1/category": true,
    "clip-6--1/finite_oracle_values": true,
    "clip-6-1/category": true,
    "clip-6-1/finite_oracle_values": true,
    "branch-0--1/category": true,
    "branch-0--1/finite_oracle_values": true,
    "branch-0-1/category": true,
    "branch-0-1/finite_oracle_values": true,
    "branch-1--1/category": true,
    "branch-1--1/finite_oracle_values": true,
    "branch-1-1/category": true,
    "branch-1-1/finite_oracle_values": true,
    "branch-2--1/category": true,
    "branch-2--1/finite_oracle_values": true,
    "branch-2-1/category": true,
    "branch-2-1/finite_oracle_values": true,
    "branch-3--1/category": true,
    "branch-3--1/finite_oracle_values": true,
    "branch-3-1/category": true,
    "branch-3-1/finite_oracle_values": true,
    "branch-4--1/category": true,
    "branch-4--1/finite_oracle_values": true,
    "branch-4-1/category": true,
    "branch-4-1/finite_oracle_values": true,
    "branch-5--1/category": true,
    "branch-5--1/finite_oracle_values": true,
    "branch-5-1/category": true,
    "branch-5-1/finite_oracle_values": true,
    "branch-6--1/category": true,
    "branch-6--1/finite_oracle_values": true,
    "branch-6-1/category": true,
    "branch-6-1/finite_oracle_values": true,
    "max-tie-0/category": true,
    "max-tie-0/finite_oracle_values": true,
    "max-tie-1/category": true,
    "max-tie-1/finite_oracle_values": true,
    "max-tie-2/category": true,
    "max-tie-2/finite_oracle_values": true,
    "stop-0/category": true,
    "stop-0/finite_oracle_values": true,
    "stop-0/exactK": true,
    "stop-0/trace_AD_slope": true,
    "stop-1/category": true,
    "stop-1/finite_oracle_values": true,
    "stop-1/exactK": true,
    "stop-1/trace_AD_slope": true,
    "stop-2/category": true,
    "stop-2/finite_oracle_values": true,
    "stop-2/exactK": true,
    "stop-2/trace_AD_slope": true,
    "stop-3/category": true,
    "stop-3/finite_oracle_values": true,
    "stop-3/exactK": true,
    "stop-3/trace_AD_slope": true,
    "stop-4/category": true,
    "stop-4/finite_oracle_values": true,
    "stop-4/exactK": true,
    "stop-4/trace_AD_slope": true,
    "inactive-log/category": true,
    "inactive-log/finite_oracle_values": true,
    "inactive/no_log_evaluation": true,
    "jump/0": true,
    "jump/1": true,
    "jump/2": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/kink-branch-derivatives/index.json

![保存した非滑らか関数値と停止写像、古典微分が未定義な点とtrace微分を分けた表示。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/results/kink-branch-derivatives-preview.png)

保存した非滑らか関数値と停止写像、古典微分が未定義な点とtrace微分を分けた表示。

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/atlas-reverse-higher-ad-2026-11-24.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

## 出典と確認範囲

- The JAX authors (n.d.). The Autodiff Cookbook [accessed 2026-11-24]. https://docs.jax.dev/en/latest/notebooks/autodiff_cookbook.html; review_level=official-documentation-selected-mathematical-sections
Selected definitions and composition formulas only. A new educational tape will implement the stated finite subset. No JAX installation, execution, timing replication or implementation-source audit. Unread: Original reverse-mode/HVP papers, JAX transformation implementation, Unselected cookbook sections. Publication year not established (n.d.).

- The JAX authors (n.d.). Frequently asked questions: undefined branches and ordering [accessed 2026-11-24]. https://docs.jax.dev/en/latest/faq.html; review_level=official-documentation-selected-sections
Read invalid inactive-branch and ordering discussions. We use an explicitly different strict nondifferentiability policy, not a universal JAX tie rule. Unread: Linked issue threads, Generalized derivative original papers. Publication year not established (n.d.).


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Derivative scope at kinks, branches and stopping decisions

Distinguish classical, one-sided directional and executed-trace derivatives at fixed kinks and stopping switches.

**Methods used**

- [Automatic differentiation](https://hrkoyama.github.io/numerical-methods-atlas/methods/automatic-differentiation/?lang=en) (`automatic-differentiation`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/kink-branch-derivatives/?lang=en#kink-branch-derivatives-en-algorithm)

Report strict nondifferentiability explicitly and record the literal top-of-loop stopping branch.

$$
x_(k+1)=.5(x_k+theta), |x_k-theta|<=1/8
$$

$$
D max(0,0)[da,db]=max(da,db)
$$

- [Finite-dimensional nonlinear maps, roots and differential actions](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#finite-dimensional-nonlinear-map-en) (`finite-dimensional-nonlinear-map`)

Small fixed real dimensionless inputs; assumptions and scope are limited to the matching contract.


**Problem figure**

![Derivative scope at kinks, branches and stopping decisions: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/results/kink-branch-derivatives.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Derivative scope at kinks, branches and stopping decisions](https://hrkoyama.github.io/numerical-methods-atlas/problems/kink-branch-derivatives/?lang=en) (`kink-branch-derivatives`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/kink-branch-derivatives/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/kink-branch-derivatives/?lang=en#kink-branch-derivatives-en-validation)

Check fixed inputs, independent references, retained candidates and every gate within the same120-second budget. Numerical success and diagnostic nonconvergence are distinct.

- [Nonsmooth discrete maps: directional derivatives and executed traces](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-kink-branch-derivatives-en) (`kink-branch-derivatives`; Same-problem reference · Analytic reference)

An executed-branch derivative is not a universal subgradient or a linear derivative of a nonsmooth map.
## Assumptions, units and boundaries

Small fixed real dimensionless inputs; assumptions and scope are limited to the matching contract.

**Editorial clarification**

An executed-branch derivative is not a universal subgradient or a linear derivative of a nonsmooth map. Plot axes describe finite-dimensional variables, iterations or diagnostics, not a physical spatial dimension or PDE boundary.

## Adopted numerical method

Report strict nondifferentiability explicitly and record the literal top-of-loop stopping branch.

$$
x_(k+1)=.5(x_k+theta), |x_k-theta|<=1/8
$$

$$
D max(0,0)[da,db]=max(da,db)
$$

## References and validation

Check fixed inputs, independent references, retained candidates and every gate within the same120-second budget. Numerical success and diagnostic nonconvergence are distinct.

## Limits

An executed-branch derivative is not a universal subgradient or a linear derivative of a nonsmooth map.

## Stored measurements and decisions

```json
{
  "metrics": {
    "max_smooth_slope_oracle_error": 0.0,
    "max_fixed_trace_slope_error": 0.0,
    "stop_switch_jump": 0.0625,
    "max_jump_quotient_identity_error": 0.0,
    "inactive_invalid_branch_calls": 0
  },
  "checks": {
    "abs-0--1/category": true,
    "abs-0--1/finite_oracle_values": true,
    "abs-0-1/category": true,
    "abs-0-1/finite_oracle_values": true,
    "abs-1--1/category": true,
    "abs-1--1/finite_oracle_values": true,
    "abs-1-1/category": true,
    "abs-1-1/finite_oracle_values": true,
    "abs-2--1/category": true,
    "abs-2--1/finite_oracle_values": true,
    "abs-2-1/category": true,
    "abs-2-1/finite_oracle_values": true,
    "abs-3--1/category": true,
    "abs-3--1/finite_oracle_values": true,
    "abs-3-1/category": true,
    "abs-3-1/finite_oracle_values": true,
    "abs-4--1/category": true,
    "abs-4--1/finite_oracle_values": true,
    "abs-4-1/category": true,
    "abs-4-1/finite_oracle_values": true,
    "abs-5--1/category": true,
    "abs-5--1/finite_oracle_values": true,
    "abs-5-1/category": true,
    "abs-5-1/finite_oracle_values": true,
    "abs-6--1/category": true,
    "abs-6--1/finite_oracle_values": true,
    "abs-6-1/category": true,
    "abs-6-1/finite_oracle_values": true,
    "relu-0--1/category": true,
    "relu-0--1/finite_oracle_values": true,
    "relu-0-1/category": true,
    "relu-0-1/finite_oracle_values": true,
    "relu-1--1/category": true,
    "relu-1--1/finite_oracle_values": true,
    "relu-1-1/category": true,
    "relu-1-1/finite_oracle_values": true,
    "relu-2--1/category": true,
    "relu-2--1/finite_oracle_values": true,
    "relu-2-1/category": true,
    "relu-2-1/finite_oracle_values": true,
    "relu-3--1/category": true,
    "relu-3--1/finite_oracle_values": true,
    "relu-3-1/category": true,
    "relu-3-1/finite_oracle_values": true,
    "relu-4--1/category": true,
    "relu-4--1/finite_oracle_values": true,
    "relu-4-1/category": true,
    "relu-4-1/finite_oracle_values": true,
    "relu-5--1/category": true,
    "relu-5--1/finite_oracle_values": true,
    "relu-5-1/category": true,
    "relu-5-1/finite_oracle_values": true,
    "relu-6--1/category": true,
    "relu-6--1/finite_oracle_values": true,
    "relu-6-1/category": true,
    "relu-6-1/finite_oracle_values": true,
    "clip-0--1/category": true,
    "clip-0--1/finite_oracle_values": true,
    "clip-0-1/category": true,
    "clip-0-1/finite_oracle_values": true,
    "clip-1--1/category": true,
    "clip-1--1/finite_oracle_values": true,
    "clip-1-1/category": true,
    "clip-1-1/finite_oracle_values": true,
    "clip-2--1/category": true,
    "clip-2--1/finite_oracle_values": true,
    "clip-2-1/category": true,
    "clip-2-1/finite_oracle_values": true,
    "clip-3--1/category": true,
    "clip-3--1/finite_oracle_values": true,
    "clip-3-1/category": true,
    "clip-3-1/finite_oracle_values": true,
    "clip-4--1/category": true,
    "clip-4--1/finite_oracle_values": true,
    "clip-4-1/category": true,
    "clip-4-1/finite_oracle_values": true,
    "clip-5--1/category": true,
    "clip-5--1/finite_oracle_values": true,
    "clip-5-1/category": true,
    "clip-5-1/finite_oracle_values": true,
    "clip-6--1/category": true,
    "clip-6--1/finite_oracle_values": true,
    "clip-6-1/category": true,
    "clip-6-1/finite_oracle_values": true,
    "branch-0--1/category": true,
    "branch-0--1/finite_oracle_values": true,
    "branch-0-1/category": true,
    "branch-0-1/finite_oracle_values": true,
    "branch-1--1/category": true,
    "branch-1--1/finite_oracle_values": true,
    "branch-1-1/category": true,
    "branch-1-1/finite_oracle_values": true,
    "branch-2--1/category": true,
    "branch-2--1/finite_oracle_values": true,
    "branch-2-1/category": true,
    "branch-2-1/finite_oracle_values": true,
    "branch-3--1/category": true,
    "branch-3--1/finite_oracle_values": true,
    "branch-3-1/category": true,
    "branch-3-1/finite_oracle_values": true,
    "branch-4--1/category": true,
    "branch-4--1/finite_oracle_values": true,
    "branch-4-1/category": true,
    "branch-4-1/finite_oracle_values": true,
    "branch-5--1/category": true,
    "branch-5--1/finite_oracle_values": true,
    "branch-5-1/category": true,
    "branch-5-1/finite_oracle_values": true,
    "branch-6--1/category": true,
    "branch-6--1/finite_oracle_values": true,
    "branch-6-1/category": true,
    "branch-6-1/finite_oracle_values": true,
    "max-tie-0/category": true,
    "max-tie-0/finite_oracle_values": true,
    "max-tie-1/category": true,
    "max-tie-1/finite_oracle_values": true,
    "max-tie-2/category": true,
    "max-tie-2/finite_oracle_values": true,
    "stop-0/category": true,
    "stop-0/finite_oracle_values": true,
    "stop-0/exactK": true,
    "stop-0/trace_AD_slope": true,
    "stop-1/category": true,
    "stop-1/finite_oracle_values": true,
    "stop-1/exactK": true,
    "stop-1/trace_AD_slope": true,
    "stop-2/category": true,
    "stop-2/finite_oracle_values": true,
    "stop-2/exactK": true,
    "stop-2/trace_AD_slope": true,
    "stop-3/category": true,
    "stop-3/finite_oracle_values": true,
    "stop-3/exactK": true,
    "stop-3/trace_AD_slope": true,
    "stop-4/category": true,
    "stop-4/finite_oracle_values": true,
    "stop-4/exactK": true,
    "stop-4/trace_AD_slope": true,
    "inactive-log/category": true,
    "inactive-log/finite_oracle_values": true,
    "inactive/no_log_evaluation": true,
    "jump/0": true,
    "jump/1": true,
    "jump/2": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/kink-branch-derivatives/index.json

![Saved nonsmooth values and stopped-map samples, distinguishing undefined classical derivatives from trace derivatives.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/results/kink-branch-derivatives-preview.png)

Saved nonsmooth values and stopped-map samples, distinguishing undefined classical derivatives from trace derivatives.

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/atlas-reverse-higher-ad-2026-11-24.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

## Sources and review scope

- The JAX authors (n.d.). The Autodiff Cookbook [accessed 2026-11-24]. https://docs.jax.dev/en/latest/notebooks/autodiff_cookbook.html; review_level=official-documentation-selected-mathematical-sections
Selected definitions and composition formulas only. A new educational tape will implement the stated finite subset. No JAX installation, execution, timing replication or implementation-source audit. Unread: Original reverse-mode/HVP papers, JAX transformation implementation, Unselected cookbook sections. Publication year not established (n.d.).

- The JAX authors (n.d.). Frequently asked questions: undefined branches and ordering [accessed 2026-11-24]. https://docs.jax.dev/en/latest/faq.html; review_level=official-documentation-selected-sections
Read invalid inactive-branch and ordering discussions. We use an explicitly different strict nondifferentiability policy, not a universal JAX tie rule. Unread: Linked issue threads, Generalized derivative original papers. Publication year not established (n.d.).


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
