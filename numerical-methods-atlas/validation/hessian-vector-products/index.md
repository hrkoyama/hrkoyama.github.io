# HVPと状態固定・陰関数全微分の区別

forward-over-reverse HVPと二階陰関数則を別々の独立参照へ照合します。

**使用手法**

- [自動微分](https://hrkoyama.github.io/numerical-methods-atlas/methods/automatic-differentiation/?lang=ja) (`automatic-differentiation`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/hessian-vector-products/?lang=ja#hessian-vector-products-ja-algorithm)

値と方向接線、cotangentとその方向接線を伝播し、陰関数はF/R1/R2を解きます。

$$
Hv=D(grad f)(x)v
$$

$$
F=u^2-theta=0, 2u*s=1, 2u*t+2s^2=0
$$

- [有限次元非線形写像・根と微分作用](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#finite-dimensional-nonlinear-map-ja) (`finite-dimensional-nonlinear-map`)

小さな固定入力・実数・無次元。詳しい入力と適用範囲は対応する契約に限定します。

- [Bratu非線形境界値問題](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bratu-ja) (`bratu`)

小さな固定入力・実数・無次元。詳しい入力と適用範囲は対応する契約に限定します。


**問題の図**

![HVPと状態固定・陰関数全微分の区別：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/results/hessian-vector-products.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[HVPと状態固定・陰関数全微分の区別](https://hrkoyama.github.io/numerical-methods-atlas/problems/hessian-vector-products/?lang=ja) (`hessian-vector-products`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/hessian-vector-products/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/hessian-vector-products/?lang=ja#hessian-vector-products-ja-validation)

固定入力・独立参照・保存候補・全判定を同じ120秒予算内で検証します。数値合格と診断用非収束を区別します。

- [固定状態HVPと二階陰関数則の独立参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-hessian-vector-products-ja) (`hessian-vector-products`; 同じ問題の参照 · 解析参照)

一般のreduced inverse Hessianや有限Newton traceの数学的陰関数微分とは主張しません。
## 前提・単位・境界

小さな固定入力・実数・無次元。詳しい入力と適用範囲は対応する契約に限定します。

**編集上の補足**

一般のreduced inverse Hessianや有限Newton traceの数学的陰関数微分とは主張しません。 図の座標は有限次元の変数・反復・診断で、物理空間の次元やPDE境界を表しません。

## 採用した計算法

値と方向接線、cotangentとその方向接線を伝播し、陰関数はF/R1/R2を解きます。

$$
Hv=D(grad f)(x)v
$$

$$
F=u^2-theta=0, 2u*s=1, 2u*t+2s^2=0
$$

## 比較・検証

固定入力・独立参照・保存候補・全判定を同じ120秒予算内で検証します。数値合格と診断用非収束を区別します。

## 確認の限界

一般のreduced inverse Hessianや有限Newton traceの数学的陰関数微分とは主張しません。

## 保存実測値と判定

```json
{
  "metrics": {
    "max_HVP_oracle_error": 5.8127826803247354e-15,
    "max_bilinear_symmetry_defect": 0.0,
    "implicit_state_residual": 0.0,
    "implicit_tangent_residual": 0.0,
    "implicit_second_tangent_residual": 0.0,
    "implicit_total_curvature": 0.23125
  },
  "checks": {
    "quadratic4/finite": true,
    "quadratic4/reference_product": true,
    "quadratic4/primary_path_ownership": true,
    "quadratic4/work_counters": true,
    "quadratic4/independent_gradient": true,
    "quadratic4/bilinear_symmetry": true,
    "bratu-energy7/finite": true,
    "bratu-energy7/reference_product": true,
    "bratu-energy7/primary_path_ownership": true,
    "bratu-energy7/work_counters": true,
    "bratu-energy7/independent_gradient": true,
    "bratu-energy7/bilinear_symmetry": true,
    "bratu-energy31/finite": true,
    "bratu-energy31/reference_product": true,
    "bratu-energy31/primary_path_ownership": true,
    "bratu-energy31/work_counters": true,
    "bratu-energy31/independent_gradient": true,
    "bratu-energy31/bilinear_symmetry": true,
    "implicit-scalar4/finite": true,
    "implicit-scalar4/reference_product": true,
    "implicit-scalar4/primary_path_ownership": true,
    "implicit-scalar4/work_counters": true,
    "implicit/state_residual": true,
    "implicit/first_tangent_residual": true,
    "implicit/second_tangent_residual": true,
    "implicit/fixed_partial": true,
    "implicit/total_curvature": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/hessian-vector-products/index.json

![保存HVPと独立参照、状態固定と陰関数全微分の二階曲率を区別した比較。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/results/hessian-vector-products-preview.png)

保存HVPと独立参照、状態固定と陰関数全微分の二階曲率を区別した比較。

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

# Hessian-vector products and fixed-state versus implicit derivatives

Check forward-over-reverse HVPs and second-order implicit rules against separate independent references.

**Methods used**

- [Automatic differentiation](https://hrkoyama.github.io/numerical-methods-atlas/methods/automatic-differentiation/?lang=en) (`automatic-differentiation`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/hessian-vector-products/?lang=en#hessian-vector-products-en-algorithm)

Transport values, tangents, cotangents and cotangent tangents; solve F/R1/R2 for implicit derivatives.

$$
Hv=D(grad f)(x)v
$$

$$
F=u^2-theta=0, 2u*s=1, 2u*t+2s^2=0
$$

- [Finite-dimensional nonlinear maps, roots and differential actions](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#finite-dimensional-nonlinear-map-en) (`finite-dimensional-nonlinear-map`)

Small fixed real dimensionless inputs; assumptions and scope are limited to the matching contract.

- [Bratu nonlinear boundary-value problem](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bratu-en) (`bratu`)

Small fixed real dimensionless inputs; assumptions and scope are limited to the matching contract.


**Problem figure**

![Hessian-vector products and fixed-state versus implicit derivatives: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/results/hessian-vector-products.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Hessian-vector products and fixed-state versus implicit derivatives](https://hrkoyama.github.io/numerical-methods-atlas/problems/hessian-vector-products/?lang=en) (`hessian-vector-products`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/hessian-vector-products/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/hessian-vector-products/?lang=en#hessian-vector-products-en-validation)

Check fixed inputs, independent references, retained candidates and every gate within the same120-second budget. Numerical success and diagnostic nonconvergence are distinct.

- [Independent references for fixed-state HVPs and second-order implicit rules](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-hessian-vector-products-en) (`hessian-vector-products`; Same-problem reference · Analytic reference)

No general reduced inverse Hessian or identification of finite Newton traces with implicit derivatives.
## Assumptions, units and boundaries

Small fixed real dimensionless inputs; assumptions and scope are limited to the matching contract.

**Editorial clarification**

No general reduced inverse Hessian or identification of finite Newton traces with implicit derivatives. Plot axes describe finite-dimensional variables, iterations or diagnostics, not a physical spatial dimension or PDE boundary.

## Adopted numerical method

Transport values, tangents, cotangents and cotangent tangents; solve F/R1/R2 for implicit derivatives.

$$
Hv=D(grad f)(x)v
$$

$$
F=u^2-theta=0, 2u*s=1, 2u*t+2s^2=0
$$

## References and validation

Check fixed inputs, independent references, retained candidates and every gate within the same120-second budget. Numerical success and diagnostic nonconvergence are distinct.

## Limits

No general reduced inverse Hessian or identification of finite Newton traces with implicit derivatives.

## Stored measurements and decisions

```json
{
  "metrics": {
    "max_HVP_oracle_error": 5.8127826803247354e-15,
    "max_bilinear_symmetry_defect": 0.0,
    "implicit_state_residual": 0.0,
    "implicit_tangent_residual": 0.0,
    "implicit_second_tangent_residual": 0.0,
    "implicit_total_curvature": 0.23125
  },
  "checks": {
    "quadratic4/finite": true,
    "quadratic4/reference_product": true,
    "quadratic4/primary_path_ownership": true,
    "quadratic4/work_counters": true,
    "quadratic4/independent_gradient": true,
    "quadratic4/bilinear_symmetry": true,
    "bratu-energy7/finite": true,
    "bratu-energy7/reference_product": true,
    "bratu-energy7/primary_path_ownership": true,
    "bratu-energy7/work_counters": true,
    "bratu-energy7/independent_gradient": true,
    "bratu-energy7/bilinear_symmetry": true,
    "bratu-energy31/finite": true,
    "bratu-energy31/reference_product": true,
    "bratu-energy31/primary_path_ownership": true,
    "bratu-energy31/work_counters": true,
    "bratu-energy31/independent_gradient": true,
    "bratu-energy31/bilinear_symmetry": true,
    "implicit-scalar4/finite": true,
    "implicit-scalar4/reference_product": true,
    "implicit-scalar4/primary_path_ownership": true,
    "implicit-scalar4/work_counters": true,
    "implicit/state_residual": true,
    "implicit/first_tangent_residual": true,
    "implicit/second_tangent_residual": true,
    "implicit/fixed_partial": true,
    "implicit/total_curvature": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/hessian-vector-products/index.json

![Saved HVPs and independent references, with fixed-state and total implicit second derivatives shown separately.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/results/hessian-vector-products-preview.png)

Saved HVPs and independent references, with fixed-state and total implicit second derivatives shown separately.

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
