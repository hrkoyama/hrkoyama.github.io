# 逆モード・HVP・非滑らか分岐の微分

小さい独自tapeを独立手計算と照合し、状態固定の偏微分・陰関数全微分・実行分岐を分けます。

共通22実行例の台帳とは別に管理する追加検証集です。配布ZIPを独立展開し、各グループの全固定入力と検査を実行した記録を示します。設定・手法・刻み幅の違いを独立した物理問題の数には加算しません。

## 独自逆モードVJPとJVP/VJP双対性

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
### 前提・単位・境界

小さな固定入力・実数・無次元。詳しい入力と適用範囲は対応する契約に限定します。

**編集上の補足**

一般のNumPy/JAX置換や複素数ADではありません。 図の座標は有限次元の変数・反復・診断で、物理空間の次元やPDE境界を表しません。

### 採用した計算法

逆topological順のcotangent加算と独立の前向き方向計算です。

$$
Jv=Df(x)v, VJP=J^T w
$$

$$
<Jv,w>_Gy=<v,Gx^-1 J^T Gy w>_Gx
$$

### 比較・検証

固定入力・独立参照・保存候補・全判定を同じ120秒予算内で検証します。数値合格と診断用非収束を区別します。

### 確認の限界

一般のNumPy/JAX置換や複素数ADではありません。

### 保存実測値と判定

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

### 取得・実行

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

### 出典と確認範囲

- The JAX authors (n.d.). The Autodiff Cookbook [accessed 2026-11-24]. https://docs.jax.dev/en/latest/notebooks/autodiff_cookbook.html; review_level=official-documentation-selected-mathematical-sections
Selected definitions and composition formulas only. A new educational tape will implement the stated finite subset. No JAX installation, execution, timing replication or implementation-source audit. Unread: Original reverse-mode/HVP papers, JAX transformation implementation, Unselected cookbook sections. Publication year not established (n.d.).

- The JAX authors (n.d.). Frequently asked questions: undefined branches and ordering [accessed 2026-11-24]. https://docs.jax.dev/en/latest/faq.html; review_level=official-documentation-selected-sections
Read invalid inactive-branch and ordering discussions. We use an explicitly different strict nondifferentiability policy, not a universal JAX tie rule. Unread: Linked issue threads, Generalized derivative original papers. Publication year not established (n.d.).


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## HVPと状態固定・陰関数全微分の区別

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
### 前提・単位・境界

小さな固定入力・実数・無次元。詳しい入力と適用範囲は対応する契約に限定します。

**編集上の補足**

一般のreduced inverse Hessianや有限Newton traceの数学的陰関数微分とは主張しません。 図の座標は有限次元の変数・反復・診断で、物理空間の次元やPDE境界を表しません。

### 採用した計算法

値と方向接線、cotangentとその方向接線を伝播し、陰関数はF/R1/R2を解きます。

$$
Hv=D(grad f)(x)v
$$

$$
F=u^2-theta=0, 2u*s=1, 2u*t+2s^2=0
$$

### 比較・検証

固定入力・独立参照・保存候補・全判定を同じ120秒予算内で検証します。数値合格と診断用非収束を区別します。

### 確認の限界

一般のreduced inverse Hessianや有限Newton traceの数学的陰関数微分とは主張しません。

### 保存実測値と判定

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

### 取得・実行

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

### 出典と確認範囲

- The JAX authors (n.d.). The Autodiff Cookbook [accessed 2026-11-24]. https://docs.jax.dev/en/latest/notebooks/autodiff_cookbook.html; review_level=official-documentation-selected-mathematical-sections
Selected definitions and composition formulas only. A new educational tape will implement the stated finite subset. No JAX installation, execution, timing replication or implementation-source audit. Unread: Original reverse-mode/HVP papers, JAX transformation implementation, Unselected cookbook sections. Publication year not established (n.d.).

- The JAX authors (n.d.). Frequently asked questions: undefined branches and ordering [accessed 2026-11-24]. https://docs.jax.dev/en/latest/faq.html; review_level=official-documentation-selected-sections
Read invalid inactive-branch and ordering discussions. We use an explicitly different strict nondifferentiability policy, not a universal JAX tie rule. Unread: Linked issue threads, Generalized derivative original papers. Publication year not established (n.d.).


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## 非滑らか点・分岐・停止条件の微分範囲

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
### 前提・単位・境界

小さな固定入力・実数・無次元。詳しい入力と適用範囲は対応する契約に限定します。

**編集上の補足**

選択した分岐の微分は普遍的なsubgradientや非滑らかな写像の線形微分ではありません。 図の座標は有限次元の変数・反復・診断で、物理空間の次元やPDE境界を表しません。

### 採用した計算法

strict nondifferentiableを明示し、停止前<=判定の実行分岐だけを記録します。

$$
x_(k+1)=.5(x_k+theta), |x_k-theta|<=1/8
$$

$$
D max(0,0)[da,db]=max(da,db)
$$

### 比較・検証

固定入力・独立参照・保存候補・全判定を同じ120秒予算内で検証します。数値合格と診断用非収束を区別します。

### 確認の限界

選択した分岐の微分は普遍的なsubgradientや非滑らかな写像の線形微分ではありません。

### 保存実測値と判定

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

### 取得・実行

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

### 出典と確認範囲

- The JAX authors (n.d.). The Autodiff Cookbook [accessed 2026-11-24]. https://docs.jax.dev/en/latest/notebooks/autodiff_cookbook.html; review_level=official-documentation-selected-mathematical-sections
Selected definitions and composition formulas only. A new educational tape will implement the stated finite subset. No JAX installation, execution, timing replication or implementation-source audit. Unread: Original reverse-mode/HVP papers, JAX transformation implementation, Unselected cookbook sections. Publication year not established (n.d.).

- The JAX authors (n.d.). Frequently asked questions: undefined branches and ordering [accessed 2026-11-24]. https://docs.jax.dev/en/latest/faq.html; review_level=official-documentation-selected-sections
Read invalid inactive-branch and ordering discussions. We use an explicitly different strict nondifferentiability policy, not a universal JAX tie rule. Unread: Linked issue threads, Generalized derivative original papers. Publication year not established (n.d.).


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
