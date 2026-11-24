# 独自逆モードVJPとJVP/VJP双対性

重複gatherとbroadcastを含む真の逆tapeを独立Jacobianと照合します。

**使用手法**

- [自動微分](https://hrkoyama.github.io/numerical-methods-atlas/methods/automatic-differentiation/?lang=ja) (`automatic-differentiation`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/reverse-vjp-duality/?lang=ja#reverse-vjp-duality-ja-algorithm)

逆topological順のcotangent加算と独立の前向き方向計算です。

$$
Jv=Df(x)v, VJP=J^T w
$$

$$
<Jv,w>_Gy=<v,Gx^-1 J^T Gy w>_Gx
$$

- [有限次元非線形写像・根と微分作用](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#finite-dimensional-nonlinear-map-ja) (`finite-dimensional-nonlinear-map`)

小さな固定入力・実数・無次元。詳しい入力と適用範囲は対応する契約に限定します。

- [Bratu非線形境界値問題](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bratu-ja) (`bratu`)

小さな固定入力・実数・無次元。詳しい入力と適用範囲は対応する契約に限定します。


**問題の図**

![独自逆モードVJPとJVP/VJP双対性：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/results/reverse-vjp-duality.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[独自逆モードVJPとJVP/VJP双対性](https://hrkoyama.github.io/numerical-methods-atlas/problems/reverse-vjp-duality/?lang=ja) (`reverse-vjp-duality`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/reverse-vjp-duality/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/reverse-vjp-duality/?lang=ja#reverse-vjp-duality-ja-validation)

固定入力・独立参照・保存候補・全判定を同じ120秒予算内で検証します。数値合格と診断用非収束を区別します。

- [離散非線形写像の独立Jacobian・JVP・VJP](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-reverse-vjp-duality-ja) (`reverse-vjp-duality`; 同じ問題の参照 · 解析参照)

一般のNumPy/JAX置換や複素数ADではありません。
## 前提・単位・境界

小さな固定入力・実数・無次元。詳しい入力と適用範囲は対応する契約に限定します。

**編集上の補足**

一般のNumPy/JAX置換や複素数ADではありません。 図の座標は有限次元の変数・反復・診断で、物理空間の次元やPDE境界を表しません。

## 採用した計算法

逆topological順のcotangent加算と独立の前向き方向計算です。

$$
Jv=Df(x)v, VJP=J^T w
$$

$$
<Jv,w>_Gy=<v,Gx^-1 J^T Gy w>_Gx
$$

## 比較・検証

固定入力・独立参照・保存候補・全判定を同じ120秒予算内で検証します。数値合格と診断用非収束を区別します。

## 確認の限界

一般のNumPy/JAX置換や複素数ADではありません。

## 保存実測値と判定

```json
{
  "metrics": {
    "max_JVP_oracle_error": 1.2338534194174146e-13,
    "max_VJP_oracle_error": 5.335730008286552e-13,
    "max_duality_defect": 7.105427357601002e-15,
    "actual_forward_seeds": 80,
    "actual_reverse_pullbacks": 68
  },
  "checks": {
    "rectangular4x3/primal": true,
    "rectangular4x3/independentJVP": true,
    "rectangular4x3/independentVJP": true,
    "rectangular4x3/fullforwardJacobian": true,
    "rectangular4x3/fullreverseJacobian": true,
    "rectangular4x3/duality": true,
    "rectangular4x3/reset_ownership": true,
    "rectangular4x3/measuredsweepcounts": true,
    "metric/product": true,
    "metric/pairing": true,
    "negative/drop-duplicate": true,
    "negative/broadcast-first": true,
    "negative/permuted-output": true,
    "negative/stale-cotangent": true,
    "wide7/primal": true,
    "wide7/independentJVP": true,
    "wide7/independentVJP": true,
    "wide7/fullforwardJacobian": true,
    "wide7/fullreverseJacobian": true,
    "wide7/duality": true,
    "wide7/reset_ownership": true,
    "wide7/measuredsweepcounts": true,
    "wide31/primal": true,
    "wide31/independentJVP": true,
    "wide31/independentVJP": true,
    "wide31/fullforwardJacobian": true,
    "wide31/fullreverseJacobian": true,
    "wide31/duality": true,
    "wide31/reset_ownership": true,
    "wide31/measuredsweepcounts": true,
    "bratu7/primal": true,
    "bratu7/independentJVP": true,
    "bratu7/independentVJP": true,
    "bratu7/fullforwardJacobian": true,
    "bratu7/fullreverseJacobian": true,
    "bratu7/duality": true,
    "bratu7/reset_ownership": true,
    "bratu7/measuredsweepcounts": true,
    "bratu31/primal": true,
    "bratu31/independentJVP": true,
    "bratu31/independentVJP": true,
    "bratu31/fullforwardJacobian": true,
    "bratu31/fullreverseJacobian": true,
    "bratu31/duality": true,
    "bratu31/reset_ownership": true,
    "bratu31/measuredsweepcounts": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/reverse-vjp-duality/index.json

![独立矩形Jacobianと実際の逆微分誤差、固定wide写像の実測sweep数。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/results/reverse-vjp-duality-preview.png)

独立矩形Jacobianと実際の逆微分誤差、固定wide写像の実測sweep数。

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

# Original reverse-mode VJP and JVP/VJP duality

Check a genuine reverse tape, including repeated-index gather and broadcast, against independent Jacobians.

**Methods used**

- [Automatic differentiation](https://hrkoyama.github.io/numerical-methods-atlas/methods/automatic-differentiation/?lang=en) (`automatic-differentiation`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/reverse-vjp-duality/?lang=en#reverse-vjp-duality-en-algorithm)

Accumulate cotangents in reverse topological order with a separate forward directional path.

$$
Jv=Df(x)v, VJP=J^T w
$$

$$
<Jv,w>_Gy=<v,Gx^-1 J^T Gy w>_Gx
$$

- [Finite-dimensional nonlinear maps, roots and differential actions](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#finite-dimensional-nonlinear-map-en) (`finite-dimensional-nonlinear-map`)

Small fixed real dimensionless inputs; assumptions and scope are limited to the matching contract.

- [Bratu nonlinear boundary-value problem](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bratu-en) (`bratu`)

Small fixed real dimensionless inputs; assumptions and scope are limited to the matching contract.


**Problem figure**

![Original reverse-mode VJP and JVP/VJP duality: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/results/reverse-vjp-duality.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Original reverse-mode VJP and JVP/VJP duality](https://hrkoyama.github.io/numerical-methods-atlas/problems/reverse-vjp-duality/?lang=en) (`reverse-vjp-duality`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/reverse-vjp-duality/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/reverse-vjp-duality/?lang=en#reverse-vjp-duality-en-validation)

Check fixed inputs, independent references, retained candidates and every gate within the same120-second budget. Numerical success and diagnostic nonconvergence are distinct.

- [Independent Jacobians, JVPs and VJPs of discrete nonlinear maps](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-reverse-vjp-duality-en) (`reverse-vjp-duality`; Same-problem reference · Analytic reference)

Not a general NumPy/JAX replacement or complex AD system.
## Assumptions, units and boundaries

Small fixed real dimensionless inputs; assumptions and scope are limited to the matching contract.

**Editorial clarification**

Not a general NumPy/JAX replacement or complex AD system. Plot axes describe finite-dimensional variables, iterations or diagnostics, not a physical spatial dimension or PDE boundary.

## Adopted numerical method

Accumulate cotangents in reverse topological order with a separate forward directional path.

$$
Jv=Df(x)v, VJP=J^T w
$$

$$
<Jv,w>_Gy=<v,Gx^-1 J^T Gy w>_Gx
$$

## References and validation

Check fixed inputs, independent references, retained candidates and every gate within the same120-second budget. Numerical success and diagnostic nonconvergence are distinct.

## Limits

Not a general NumPy/JAX replacement or complex AD system.

## Stored measurements and decisions

```json
{
  "metrics": {
    "max_JVP_oracle_error": 1.2338534194174146e-13,
    "max_VJP_oracle_error": 5.335730008286552e-13,
    "max_duality_defect": 7.105427357601002e-15,
    "actual_forward_seeds": 80,
    "actual_reverse_pullbacks": 68
  },
  "checks": {
    "rectangular4x3/primal": true,
    "rectangular4x3/independentJVP": true,
    "rectangular4x3/independentVJP": true,
    "rectangular4x3/fullforwardJacobian": true,
    "rectangular4x3/fullreverseJacobian": true,
    "rectangular4x3/duality": true,
    "rectangular4x3/reset_ownership": true,
    "rectangular4x3/measuredsweepcounts": true,
    "metric/product": true,
    "metric/pairing": true,
    "negative/drop-duplicate": true,
    "negative/broadcast-first": true,
    "negative/permuted-output": true,
    "negative/stale-cotangent": true,
    "wide7/primal": true,
    "wide7/independentJVP": true,
    "wide7/independentVJP": true,
    "wide7/fullforwardJacobian": true,
    "wide7/fullreverseJacobian": true,
    "wide7/duality": true,
    "wide7/reset_ownership": true,
    "wide7/measuredsweepcounts": true,
    "wide31/primal": true,
    "wide31/independentJVP": true,
    "wide31/independentVJP": true,
    "wide31/fullforwardJacobian": true,
    "wide31/fullreverseJacobian": true,
    "wide31/duality": true,
    "wide31/reset_ownership": true,
    "wide31/measuredsweepcounts": true,
    "bratu7/primal": true,
    "bratu7/independentJVP": true,
    "bratu7/independentVJP": true,
    "bratu7/fullforwardJacobian": true,
    "bratu7/fullreverseJacobian": true,
    "bratu7/duality": true,
    "bratu7/reset_ownership": true,
    "bratu7/measuredsweepcounts": true,
    "bratu31/primal": true,
    "bratu31/independentJVP": true,
    "bratu31/independentVJP": true,
    "bratu31/fullforwardJacobian": true,
    "bratu31/fullreverseJacobian": true,
    "bratu31/duality": true,
    "bratu31/reset_ownership": true,
    "bratu31/measuredsweepcounts": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/reverse-vjp-duality/index.json

![Independent rectangular Jacobian, actual reverse differentiation error and measured sweep counts for fixed wide maps.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/results/reverse-vjp-duality-preview.png)

Independent rectangular Jacobian, actual reverse differentiation error and measured sweep counts for fixed wide maps.

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
