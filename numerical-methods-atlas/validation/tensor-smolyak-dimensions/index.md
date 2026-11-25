# 2〜4次元テンソル・Smolyak対照

滑らかな積と相互作用積の42本の固定cubatureを比較します。

**使用手法**

- [Gauss求積・適応積分](https://hrkoyama.github.io/numerical-methods-atlas/methods/quadrature/?lang=ja) (`quadrature`)
- [Smolyak疎格子求積](https://hrkoyama.github.io/numerical-methods-atlas/methods/smolyak-sparse-grid/?lang=ja) (`smolyak-sparse-grid`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/tensor-smolyak-dimensions/?lang=ja#tensor-smolyak-dimensions-ja-algorithm)

正規化dyadic角キーで同一節点を所有し、符号付き重みと評価台帳を保持。

- [有限・無限・多変数の定積分](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#definite-integrals-ja) (`definite-integrals`)

[0,1]^d、d=2/3/4。テンソルlevel1/2/3、疎格子level1/2/3/4。


**問題の図**

![2〜4次元テンソル・Smolyak対照：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/results/tensor-smolyak-dimensions.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[2〜4次元テンソル・Smolyak対照](https://hrkoyama.github.io/numerical-methods-atlas/problems/tensor-smolyak-dimensions/?lang=ja) (`tensor-smolyak-dimensions`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/tensor-smolyak-dimensions/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/tensor-smolyak-dimensions/?lang=ja#tensor-smolyak-dimensions-ja-validation)

解析積分と独立Delta/combination組立を区別し、L<dの相互作用未解像を可視化。

- [2〜4次元テンソル・Smolyak対照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-tensor-smolyak-dimensions-ja) (`tensor-smolyak-dimensions`; 同じ問題の参照 · 解析参照)

一般の誤差単調性、常時正重み、疎格子の費用優位は主張しません。物理PDEの空間ではありません。
## 前提・単位・境界

[0,1]^d、d=2/3/4。テンソルlevel1/2/3、疎格子level1/2/3/4。

**編集上の補足**

一般の誤差単調性、常時正重み、疎格子の費用優位は主張しません。物理PDEの空間ではありません。 数学的な積分領域と次元は式・入力に示します。パラメータや誤差の図軸に物理空間の次元を割り当てません。 再現確認の合格は精度目標の全達成を意味しません。元の目標判定は達成24件・未達18件・計算不能0件です。FALSE/NAと失敗rawを保持します。

## 採用した計算法

正規化dyadic角キーで同一節点を所有し、符号付き重みと評価台帳を保持。

$$
I=\int_\Omega f(x)\,dx
$$

## 比較・検証

解析積分と独立Delta/combination組立を区別し、L<dの相互作用未解像を可視化。

## 確認の限界

一般の誤差単調性、常時正重み、疎格子の費用優位は主張しません。物理PDEの空間ではありません。

## 保存実測値と判定

```json
{
  "metrics": {
    "records": 42,
    "integrand_evaluations": 18482,
    "accuracy_goals_met": 24,
    "accuracy_goals_unmet": 18,
    "accuracy_goals_unresolved": 0,
    "estimated_converged_rows": 42
  },
  "checks": {
    "q80:d2:smooth-product:tensor-clenshaw-curtis:L1:callback-ledger": true,
    "q80:d2:smooth-product:tensor-clenshaw-curtis:L1:evaluation-cap": true,
    "q80:d2:smooth-product:tensor-clenshaw-curtis:L1:finite-return": true,
    "q80:d2:smooth-product:tensor-clenshaw-curtis:L1:canonical-inventory": true,
    "q80:d2:smooth-product:tensor-clenshaw-curtis:L1:mass": true,
    "q80:d2:smooth-product:tensor-clenshaw-curtis:L1:low-moments": true,
    "q80:d2:smooth-product:tensor-clenshaw-curtis:L2:callback-ledger": true,
    "q80:d2:smooth-product:tensor-clenshaw-curtis:L2:evaluation-cap": true,
    "q80:d2:smooth-product:tensor-clenshaw-curtis:L2:finite-return": true,
    "q80:d2:smooth-product:tensor-clenshaw-curtis:L2:canonical-inventory": true,
    "q80:d2:smooth-product:tensor-clenshaw-curtis:L2:mass": true,
    "q80:d2:smooth-product:tensor-clenshaw-curtis:L2:low-moments": true,
    "q80:d2:smooth-product:tensor-clenshaw-curtis:L3:callback-ledger": true,
    "q80:d2:smooth-product:tensor-clenshaw-curtis:L3:evaluation-cap": true,
    "q80:d2:smooth-product:tensor-clenshaw-curtis:L3:finite-return": true,
    "q80:d2:smooth-product:tensor-clenshaw-curtis:L3:canonical-inventory": true,
    "q80:d2:smooth-product:tensor-clenshaw-curtis:L3:mass": true,
    "q80:d2:smooth-product:tensor-clenshaw-curtis:L3:low-moments": true,
    "q80:d2:smooth-product:tensor-clenshaw-curtis:L3:required-finest-accuracy": true,
    "q80:d2:smooth-product:smolyak-delta:L1:callback-ledger": true,
    "q80:d2:smooth-product:smolyak-delta:L1:evaluation-cap": true,
    "q80:d2:smooth-product:smolyak-delta:L1:finite-return": true,
    "q80:d2:smooth-product:smolyak-delta:L1:canonical-inventory": true,
    "q80:d2:smooth-product:smolyak-delta:L1:mass": true,
    "q80:d2:smooth-product:smolyak-delta:L1:low-moments": true,
    "q80:d2:smooth-product:smolyak-delta:L1:delta-combination": true,
    "q80:d2:smooth-product:smolyak-delta:L2:callback-ledger": true,
    "q80:d2:smooth-product:smolyak-delta:L2:evaluation-cap": true,
    "q80:d2:smooth-product:smolyak-delta:L2:finite-return": true,
    "q80:d2:smooth-product:smolyak-delta:L2:canonical-inventory": true,
    "q80:d2:smooth-product:smolyak-delta:L2:mass": true,
    "q80:d2:smooth-product:smolyak-delta:L2:low-moments": true,
    "q80:d2:smooth-product:smolyak-delta:L2:delta-combination": true,
    "q80:d2:smooth-product:smolyak-delta:L3:callback-ledger": true,
    "q80:d2:smooth-product:smolyak-delta:L3:evaluation-cap": true,
    "q80:d2:smooth-product:smolyak-delta:L3:finite-return": true,
    "q80:d2:smooth-product:smolyak-delta:L3:canonical-inventory": true,
    "q80:d2:smooth-product:smolyak-delta:L3:mass": true,
    "q80:d2:smooth-product:smolyak-delta:L3:low-moments": true,
    "q80:d2:smooth-product:smolyak-delta:L4:callback-ledger": true,
    "q80:d2:smooth-product:smolyak-delta:L4:evaluation-cap": true,
    "q80:d2:smooth-product:smolyak-delta:L4:finite-return": true,
    "q80:d2:smooth-product:smolyak-delta:L4:canonical-inventory": true,
    "q80:d2:smooth-product:smolyak-delta:L4:mass": true,
    "q80:d2:smooth-product:smolyak-delta:L4:low-moments": true,
    "q80:d2:smooth-product:smolyak-delta:L4:required-finest-accuracy": true,
    "q80:d2:interaction-product:tensor-clenshaw-curtis:L1:callback-ledger": true,
    "q80:d2:interaction-product:tensor-clenshaw-curtis:L1:evaluation-cap": true,
    "q80:d2:interaction-product:tensor-clenshaw-curtis:L1:finite-return": true,
    "q80:d2:interaction-product:tensor-clenshaw-curtis:L1:canonical-inventory": true,
    "q80:d2:interaction-product:tensor-clenshaw-curtis:L1:mass": true,
    "q80:d2:interaction-product:tensor-clenshaw-curtis:L1:low-moments": true,
    "q80:d2:interaction-product:tensor-clenshaw-curtis:L1:required-product-moment": true,
    "q80:d2:interaction-product:tensor-clenshaw-curtis:L2:callback-ledger": true,
    "q80:d2:interaction-product:tensor-clenshaw-curtis:L2:evaluation-cap": true,
    "q80:d2:interaction-product:tensor-clenshaw-curtis:L2:finite-return": true,
    "q80:d2:interaction-product:tensor-clenshaw-curtis:L2:canonical-inventory": true,
    "q80:d2:interaction-product:tensor-clenshaw-curtis:L2:mass": true,
    "q80:d2:interaction-product:tensor-clenshaw-curtis:L2:low-moments": true,
    "q80:d2:interaction-product:tensor-clenshaw-curtis:L2:required-product-moment": true,
    "q80:d2:interaction-product:tensor-clenshaw-curtis:L3:callback-ledger": true,
    "q80:d2:interaction-product:tensor-clenshaw-curtis:L3:evaluation-cap": true,
    "q80:d2:interaction-product:tensor-clenshaw-curtis:L3:finite-return": true,
    "q80:d2:interaction-product:tensor-clenshaw-curtis:L3:canonical-inventory": true,
    "q80:d2:interaction-product:tensor-clenshaw-curtis:L3:mass": true,
    "q80:d2:interaction-product:tensor-clenshaw-curtis:L3:low-moments": true,
    "q80:d2:interaction-product:tensor-clenshaw-curtis:L3:required-product-moment": true,
    "q80:d2:interaction-product:smolyak-delta:L1:callback-ledger": true,
    "q80:d2:interaction-product:smolyak-delta:L1:evaluation-cap": true,
    "q80:d2:interaction-product:smolyak-delta:L1:finite-return": true,
    "q80:d2:interaction-product:smolyak-delta:L1:canonical-inventory": true,
    "q80:d2:interaction-product:smolyak-delta:L1:mass": true,
    "q80:d2:interaction-product:smolyak-delta:L1:low-moments": true,
    "q80:d2:interaction-product:smolyak-delta:L1:delta-combination": true,
    "q80:d2:interaction-product:smolyak-delta:L1:underresolution-identity": true,
    "q80:d2:interaction-product:smolyak-delta:L2:callback-ledger": true,
    "q80:d2:interaction-product:smolyak-delta:L2:evaluation-cap": true,
    "q80:d2:interaction-product:smolyak-delta:L2:finite-return": true,
    "q80:d2:interaction-product:smolyak-delta:L2:canonical-inventory": true,
    "q80:d2:interaction-product:smolyak-delta:L2:mass": true,
    "q80:d2:interaction-product:smolyak-delta:L2:low-moments": true,
    "q80:d2:interaction-product:smolyak-delta:L2:delta-combination": true,
    "q80:d2:interaction-product:smolyak-delta:L2:required-product-moment": true,
    "q80:d2:interaction-product:smolyak-delta:L3:callback-ledger": true,
    "q80:d2:interaction-product:smolyak-delta:L3:evaluation-cap": true,
    "q80:d2:interaction-product:smolyak-delta:L3:finite-return": true,
    "q80:d2:interaction-product:smolyak-delta:L3:canonical-inventory": true,
    "q80:d2:interaction-product:smolyak-delta:L3:mass": true,
    "q80:d2:interaction-product:smolyak-delta:L3:low-moments": true,
    "q80:d2:interaction-product:smolyak-delta:L3:required-product-moment": true,
    "q80:d2:interaction-product:smolyak-delta:L4:callback-ledger": true,
    "q80:d2:interaction-product:smolyak-delta:L4:evaluation-cap": true,
    "q80:d2:interaction-product:smolyak-delta:L4:finite-return": true,
    "q80:d2:interaction-product:smolyak-delta:L4:canonical-inventory": true,
    "q80:d2:interaction-product:smolyak-delta:L4:mass": true,
    "q80:d2:interaction-product:smolyak-delta:L4:low-moments": true,
    "q80:d2:interaction-product:smolyak-delta:L4:required-product-moment": true,
    "q80:d3:smooth-product:tensor-clenshaw-curtis:L1:callback-ledger": true,
    "q80:d3:smooth-product:tensor-clenshaw-curtis:L1:evaluation-cap": true,
    "q80:d3:smooth-product:tensor-clenshaw-curtis:L1:finite-return": true,
    "q80:d3:smooth-product:tensor-clenshaw-curtis:L1:canonical-inventory": true,
    "q80:d3:smooth-product:tensor-clenshaw-curtis:L1:mass": true,
    "q80:d3:smooth-product:tensor-clenshaw-curtis:L1:low-moments": true,
    "q80:d3:smooth-product:tensor-clenshaw-curtis:L2:callback-ledger": true,
    "q80:d3:smooth-product:tensor-clenshaw-curtis:L2:evaluation-cap": true,
    "q80:d3:smooth-product:tensor-clenshaw-curtis:L2:finite-return": true,
    "q80:d3:smooth-product:tensor-clenshaw-curtis:L2:canonical-inventory": true,
    "q80:d3:smooth-product:tensor-clenshaw-curtis:L2:mass": true,
    "q80:d3:smooth-product:tensor-clenshaw-curtis:L2:low-moments": true,
    "q80:d3:smooth-product:tensor-clenshaw-curtis:L3:callback-ledger": true,
    "q80:d3:smooth-product:tensor-clenshaw-curtis:L3:evaluation-cap": true,
    "q80:d3:smooth-product:tensor-clenshaw-curtis:L3:finite-return": true,
    "q80:d3:smooth-product:tensor-clenshaw-curtis:L3:canonical-inventory": true,
    "q80:d3:smooth-product:tensor-clenshaw-curtis:L3:mass": true,
    "q80:d3:smooth-product:tensor-clenshaw-curtis:L3:low-moments": true,
    "q80:d3:smooth-product:tensor-clenshaw-curtis:L3:required-finest-accuracy": true,
    "q80:d3:smooth-product:smolyak-delta:L1:callback-ledger": true,
    "q80:d3:smooth-product:smolyak-delta:L1:evaluation-cap": true,
    "q80:d3:smooth-product:smolyak-delta:L1:finite-return": true,
    "q80:d3:smooth-product:smolyak-delta:L1:canonical-inventory": true,
    "q80:d3:smooth-product:smolyak-delta:L1:mass": true,
    "q80:d3:smooth-product:smolyak-delta:L1:low-moments": true,
    "q80:d3:smooth-product:smolyak-delta:L1:delta-combination": true,
    "q80:d3:smooth-product:smolyak-delta:L2:callback-ledger": true,
    "q80:d3:smooth-product:smolyak-delta:L2:evaluation-cap": true,
    "q80:d3:smooth-product:smolyak-delta:L2:finite-return": true,
    "q80:d3:smooth-product:smolyak-delta:L2:canonical-inventory": true,
    "q80:d3:smooth-product:smolyak-delta:L2:mass": true,
    "q80:d3:smooth-product:smolyak-delta:L2:low-moments": true,
    "q80:d3:smooth-product:smolyak-delta:L2:delta-combination": true,
    "q80:d3:smooth-product:smolyak-delta:L3:callback-ledger": true,
    "q80:d3:smooth-product:smolyak-delta:L3:evaluation-cap": true,
    "q80:d3:smooth-product:smolyak-delta:L3:finite-return": true,
    "q80:d3:smooth-product:smolyak-delta:L3:canonical-inventory": true,
    "q80:d3:smooth-product:smolyak-delta:L3:mass": true,
    "q80:d3:smooth-product:smolyak-delta:L3:low-moments": true,
    "q80:d3:smooth-product:smolyak-delta:L4:callback-ledger": true,
    "q80:d3:smooth-product:smolyak-delta:L4:evaluation-cap": true,
    "q80:d3:smooth-product:smolyak-delta:L4:finite-return": true,
    "q80:d3:smooth-product:smolyak-delta:L4:canonical-inventory": true,
    "q80:d3:smooth-product:smolyak-delta:L4:mass": true,
    "q80:d3:smooth-product:smolyak-delta:L4:low-moments": true,
    "q80:d3:smooth-product:smolyak-delta:L4:required-finest-accuracy": true,
    "q80:d3:interaction-product:tensor-clenshaw-curtis:L1:callback-ledger": true,
    "q80:d3:interaction-product:tensor-clenshaw-curtis:L1:evaluation-cap": true,
    "q80:d3:interaction-product:tensor-clenshaw-curtis:L1:finite-return": true,
    "q80:d3:interaction-product:tensor-clenshaw-curtis:L1:canonical-inventory": true,
    "q80:d3:interaction-product:tensor-clenshaw-curtis:L1:mass": true,
    "q80:d3:interaction-product:tensor-clenshaw-curtis:L1:low-moments": true,
    "q80:d3:interaction-product:tensor-clenshaw-curtis:L1:required-product-moment": true,
    "q80:d3:interaction-product:tensor-clenshaw-curtis:L2:callback-ledger": true,
    "q80:d3:interaction-product:tensor-clenshaw-curtis:L2:evaluation-cap": true,
    "q80:d3:interaction-product:tensor-clenshaw-curtis:L2:finite-return": true,
    "q80:d3:interaction-product:tensor-clenshaw-curtis:L2:canonical-inventory": true,
    "q80:d3:interaction-product:tensor-clenshaw-curtis:L2:mass": true,
    "q80:d3:interaction-product:tensor-clenshaw-curtis:L2:low-moments": true,
    "q80:d3:interaction-product:tensor-clenshaw-curtis:L2:required-product-moment": true,
    "q80:d3:interaction-product:tensor-clenshaw-curtis:L3:callback-ledger": true,
    "q80:d3:interaction-product:tensor-clenshaw-curtis:L3:evaluation-cap": true,
    "q80:d3:interaction-product:tensor-clenshaw-curtis:L3:finite-return": true,
    "q80:d3:interaction-product:tensor-clenshaw-curtis:L3:canonical-inventory": true,
    "q80:d3:interaction-product:tensor-clenshaw-curtis:L3:mass": true,
    "q80:d3:interaction-product:tensor-clenshaw-curtis:L3:low-moments": true,
    "q80:d3:interaction-product:tensor-clenshaw-curtis:L3:required-product-moment": true,
    "q80:d3:interaction-product:smolyak-delta:L1:callback-ledger": true,
    "q80:d3:interaction-product:smolyak-delta:L1:evaluation-cap": true,
    "q80:d3:interaction-product:smolyak-delta:L1:finite-return": true,
    "q80:d3:interaction-product:smolyak-delta:L1:canonical-inventory": true,
    "q80:d3:interaction-product:smolyak-delta:L1:mass": true,
    "q80:d3:interaction-product:smolyak-delta:L1:low-moments": true,
    "q80:d3:interaction-product:smolyak-delta:L1:delta-combination": true,
    "q80:d3:interaction-product:smolyak-delta:L1:underresolution-identity": true,
    "q80:d3:interaction-product:smolyak-delta:L2:callback-ledger": true,
    "q80:d3:interaction-product:smolyak-delta:L2:evaluation-cap": true,
    "q80:d3:interaction-product:smolyak-delta:L2:finite-return": true,
    "q80:d3:interaction-product:smolyak-delta:L2:canonical-inventory": true,
    "q80:d3:interaction-product:smolyak-delta:L2:mass": true,
    "q80:d3:interaction-product:smolyak-delta:L2:low-moments": true,
    "q80:d3:interaction-product:smolyak-delta:L2:delta-combination": true,
    "q80:d3:interaction-product:smolyak-delta:L2:underresolution-identity": true,
    "q80:d3:interaction-product:smolyak-delta:L3:callback-ledger": true,
    "q80:d3:interaction-product:smolyak-delta:L3:evaluation-cap": true,
    "q80:d3:interaction-product:smolyak-delta:L3:finite-return": true,
    "q80:d3:interaction-product:smolyak-delta:L3:canonical-inventory": true,
    "q80:d3:interaction-product:smolyak-delta:L3:mass": true,
    "q80:d3:interaction-product:smolyak-delta:L3:low-moments": true,
    "q80:d3:interaction-product:smolyak-delta:L3:required-product-moment": true,
    "q80:d3:interaction-product:smolyak-delta:L4:callback-ledger": true,
    "q80:d3:interaction-product:smolyak-delta:L4:evaluation-cap": true,
    "q80:d3:interaction-product:smolyak-delta:L4:finite-return": true,
    "q80:d3:interaction-product:smolyak-delta:L4:canonical-inventory": true,
    "q80:d3:interaction-product:smolyak-delta:L4:mass": true,
    "q80:d3:interaction-product:smolyak-delta:L4:low-moments": true,
    "q80:d3:interaction-product:smolyak-delta:L4:required-product-moment": true,
    "q80:d4:smooth-product:tensor-clenshaw-curtis:L1:callback-ledger": true,
    "q80:d4:smooth-product:tensor-clenshaw-curtis:L1:evaluation-cap": true,
    "q80:d4:smooth-product:tensor-clenshaw-curtis:L1:finite-return": true,
    "q80:d4:smooth-product:tensor-clenshaw-curtis:L1:canonical-inventory": true,
    "q80:d4:smooth-product:tensor-clenshaw-curtis:L1:mass": true,
    "q80:d4:smooth-product:tensor-clenshaw-curtis:L1:low-moments": true,
    "q80:d4:smooth-product:tensor-clenshaw-curtis:L2:callback-ledger": true,
    "q80:d4:smooth-product:tensor-clenshaw-curtis:L2:evaluation-cap": true,
    "q80:d4:smooth-product:tensor-clenshaw-curtis:L2:finite-return": true,
    "q80:d4:smooth-product:tensor-clenshaw-curtis:L2:canonical-inventory": true,
    "q80:d4:smooth-product:tensor-clenshaw-curtis:L2:mass": true,
    "q80:d4:smooth-product:tensor-clenshaw-curtis:L2:low-moments": true,
    "q80:d4:smooth-product:tensor-clenshaw-curtis:L3:callback-ledger": true,
    "q80:d4:smooth-product:tensor-clenshaw-curtis:L3:evaluation-cap": true,
    "q80:d4:smooth-product:tensor-clenshaw-curtis:L3:finite-return": true,
    "q80:d4:smooth-product:tensor-clenshaw-curtis:L3:canonical-inventory": true,
    "q80:d4:smooth-product:tensor-clenshaw-curtis:L3:mass": true,
    "q80:d4:smooth-product:tensor-clenshaw-curtis:L3:low-moments": true,
    "q80:d4:smooth-product:tensor-clenshaw-curtis:L3:required-finest-accuracy": true,
    "q80:d4:smooth-product:smolyak-delta:L1:callback-ledger": true,
    "q80:d4:smooth-product:smolyak-delta:L1:evaluation-cap": true,
    "q80:d4:smooth-product:smolyak-delta:L1:finite-return": true,
    "q80:d4:smooth-product:smolyak-delta:L1:canonical-inventory": true,
    "q80:d4:smooth-product:smolyak-delta:L1:mass": true,
    "q80:d4:smooth-product:smolyak-delta:L1:low-moments": true,
    "q80:d4:smooth-product:smolyak-delta:L2:callback-ledger": true,
    "q80:d4:smooth-product:smolyak-delta:L2:evaluation-cap": true,
    "q80:d4:smooth-product:smolyak-delta:L2:finite-return": true,
    "q80:d4:smooth-product:smolyak-delta:L2:canonical-inventory": true,
    "q80:d4:smooth-product:smolyak-delta:L2:mass": true,
    "q80:d4:smooth-product:smolyak-delta:L2:low-moments": true,
    "q80:d4:smooth-product:smolyak-delta:L3:callback-ledger": true,
    "q80:d4:smooth-product:smolyak-delta:L3:evaluation-cap": true,
    "q80:d4:smooth-product:smolyak-delta:L3:finite-return": true,
    "q80:d4:smooth-product:smolyak-delta:L3:canonical-inventory": true,
    "q80:d4:smooth-product:smolyak-delta:L3:mass": true,
    "q80:d4:smooth-product:smolyak-delta:L3:low-moments": true,
    "q80:d4:smooth-product:smolyak-delta:L4:callback-ledger": true,
    "q80:d4:smooth-product:smolyak-delta:L4:evaluation-cap": true,
    "q80:d4:smooth-product:smolyak-delta:L4:finite-return": true,
    "q80:d4:smooth-product:smolyak-delta:L4:canonical-inventory": true,
    "q80:d4:smooth-product:smolyak-delta:L4:mass": true,
    "q80:d4:smooth-product:smolyak-delta:L4:low-moments": true,
    "q80:d4:smooth-product:smolyak-delta:L4:required-finest-accuracy": true,
    "q80:d4:interaction-product:tensor-clenshaw-curtis:L1:callback-ledger": true,
    "q80:d4:interaction-product:tensor-clenshaw-curtis:L1:evaluation-cap": true,
    "q80:d4:interaction-product:tensor-clenshaw-curtis:L1:finite-return": true,
    "q80:d4:interaction-product:tensor-clenshaw-curtis:L1:canonical-inventory": true,
    "q80:d4:interaction-product:tensor-clenshaw-curtis:L1:mass": true,
    "q80:d4:interaction-product:tensor-clenshaw-curtis:L1:low-moments": true,
    "q80:d4:interaction-product:tensor-clenshaw-curtis:L1:required-product-moment": true,
    "q80:d4:interaction-product:tensor-clenshaw-curtis:L2:callback-ledger": true,
    "q80:d4:interaction-product:tensor-clenshaw-curtis:L2:evaluation-cap": true,
    "q80:d4:interaction-product:tensor-clenshaw-curtis:L2:finite-return": true,
    "q80:d4:interaction-product:tensor-clenshaw-curtis:L2:canonical-inventory": true,
    "q80:d4:interaction-product:tensor-clenshaw-curtis:L2:mass": true,
    "q80:d4:interaction-product:tensor-clenshaw-curtis:L2:low-moments": true,
    "q80:d4:interaction-product:tensor-clenshaw-curtis:L2:required-product-moment": true,
    "q80:d4:interaction-product:tensor-clenshaw-curtis:L3:callback-ledger": true,
    "q80:d4:interaction-product:tensor-clenshaw-curtis:L3:evaluation-cap": true,
    "q80:d4:interaction-product:tensor-clenshaw-curtis:L3:finite-return": true,
    "q80:d4:interaction-product:tensor-clenshaw-curtis:L3:canonical-inventory": true,
    "q80:d4:interaction-product:tensor-clenshaw-curtis:L3:mass": true,
    "q80:d4:interaction-product:tensor-clenshaw-curtis:L3:low-moments": true,
    "q80:d4:interaction-product:tensor-clenshaw-curtis:L3:required-product-moment": true,
    "q80:d4:interaction-product:smolyak-delta:L1:callback-ledger": true,
    "q80:d4:interaction-product:smolyak-delta:L1:evaluation-cap": true,
    "q80:d4:interaction-product:smolyak-delta:L1:finite-return": true,
    "q80:d4:interaction-product:smolyak-delta:L1:canonical-inventory": true,
    "q80:d4:interaction-product:smolyak-delta:L1:mass": true,
    "q80:d4:interaction-product:smolyak-delta:L1:low-moments": true,
    "q80:d4:interaction-product:smolyak-delta:L1:underresolution-identity": true,
    "q80:d4:interaction-product:smolyak-delta:L2:callback-ledger": true,
    "q80:d4:interaction-product:smolyak-delta:L2:evaluation-cap": true,
    "q80:d4:interaction-product:smolyak-delta:L2:finite-return": true,
    "q80:d4:interaction-product:smolyak-delta:L2:canonical-inventory": true,
    "q80:d4:interaction-product:smolyak-delta:L2:mass": true,
    "q80:d4:interaction-product:smolyak-delta:L2:low-moments": true,
    "q80:d4:interaction-product:smolyak-delta:L2:underresolution-identity": true,
    "q80:d4:interaction-product:smolyak-delta:L3:callback-ledger": true,
    "q80:d4:interaction-product:smolyak-delta:L3:evaluation-cap": true,
    "q80:d4:interaction-product:smolyak-delta:L3:finite-return": true,
    "q80:d4:interaction-product:smolyak-delta:L3:canonical-inventory": true,
    "q80:d4:interaction-product:smolyak-delta:L3:mass": true,
    "q80:d4:interaction-product:smolyak-delta:L3:low-moments": true,
    "q80:d4:interaction-product:smolyak-delta:L3:underresolution-identity": true,
    "q80:d4:interaction-product:smolyak-delta:L4:callback-ledger": true,
    "q80:d4:interaction-product:smolyak-delta:L4:evaluation-cap": true,
    "q80:d4:interaction-product:smolyak-delta:L4:finite-return": true,
    "q80:d4:interaction-product:smolyak-delta:L4:canonical-inventory": true,
    "q80:d4:interaction-product:smolyak-delta:L4:mass": true,
    "q80:d4:interaction-product:smolyak-delta:L4:low-moments": true,
    "q80:d4:interaction-product:smolyak-delta:L4:required-product-moment": true,
    "tensor-smolyak-dimensions:fixed-record-count": true,
    "tensor-smolyak-dimensions:unique-record-ids": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/tensor-smolyak-dimensions/index.json

![実2次元節点と符号付き積分重み](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/results/tensor-smolyak-dimensions-preview.png)

実2次元節点と符号付き積分重み

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/atlas-quadrature-controls-2026-11-25.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

## 出典と確認範囲

- Fast Construction of the Fejer and Clenshaw-Curtis Quadrature Rules [accessed 2026-11-25]. https://www.sam.math.ethz.ch/sam_reports/reports_final/reports2008/2008-07.pdf; review_level=selected-primary-body-text

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Tensor and Smolyak controls in two to four dimensions

Forty-two fixed cubatures compare a smooth product and an interaction product.

**Methods used**

- [Gaussian and adaptive quadrature](https://hrkoyama.github.io/numerical-methods-atlas/methods/quadrature/?lang=en) (`quadrature`)
- [Smolyak sparse-grid quadrature](https://hrkoyama.github.io/numerical-methods-atlas/methods/smolyak-sparse-grid/?lang=en) (`smolyak-sparse-grid`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/tensor-smolyak-dimensions/?lang=en#tensor-smolyak-dimensions-en-algorithm)

Canonical dyadic angle keys own shared nodes; signed weights and call ledgers are retained.

- [Finite, improper and multivariate definite integrals](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#definite-integrals-en) (`definite-integrals`)

The integration domain is[0,1]^d for d2/3/4; tensor levels1/2/3 and sparse levels1/2/3/4.


**Problem figure**

![Tensor and Smolyak controls in two to four dimensions: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/results/tensor-smolyak-dimensions.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Tensor and Smolyak controls in two to four dimensions](https://hrkoyama.github.io/numerical-methods-atlas/problems/tensor-smolyak-dimensions/?lang=en) (`tensor-smolyak-dimensions`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/tensor-smolyak-dimensions/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/tensor-smolyak-dimensions/?lang=en#tensor-smolyak-dimensions-en-validation)

Analytic integrals are distinct from companion Delta/combination assembly; interaction underresolution at L<d remains visible.

- [Tensor and Smolyak controls in two to four dimensions](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-tensor-smolyak-dimensions-en) (`tensor-smolyak-dimensions`; Same-problem reference · Analytic reference)

No general error monotonicity, positive-weight or cost-superiority claim; these are integration coordinates, not a physical PDE space.
## Assumptions, units and boundaries

The integration domain is[0,1]^d for d2/3/4; tensor levels1/2/3 and sparse levels1/2/3/4.

**Editorial clarification**

No general error monotonicity, positive-weight or cost-superiority claim; these are integration coordinates, not a physical PDE space. The formulas and inputs specify mathematical integration domains and dimensions. Parameter and error axes are not physical spatial coordinates. Passing reproduction checks does not mean that every accuracy goal was met. Original row outcomes: 24 met, 18 unmet and 0 not computable. False/NA outcomes and raw failures are retained.

## Adopted numerical method

Canonical dyadic angle keys own shared nodes; signed weights and call ledgers are retained.

$$
I=\int_\Omega f(x)\,dx
$$

## References and validation

Analytic integrals are distinct from companion Delta/combination assembly; interaction underresolution at L<d remains visible.

## Limits

No general error monotonicity, positive-weight or cost-superiority claim; these are integration coordinates, not a physical PDE space.

## Stored measurements and decisions

```json
{
  "metrics": {
    "records": 42,
    "integrand_evaluations": 18482,
    "accuracy_goals_met": 24,
    "accuracy_goals_unmet": 18,
    "accuracy_goals_unresolved": 0,
    "estimated_converged_rows": 42
  },
  "checks": {
    "q80:d2:smooth-product:tensor-clenshaw-curtis:L1:callback-ledger": true,
    "q80:d2:smooth-product:tensor-clenshaw-curtis:L1:evaluation-cap": true,
    "q80:d2:smooth-product:tensor-clenshaw-curtis:L1:finite-return": true,
    "q80:d2:smooth-product:tensor-clenshaw-curtis:L1:canonical-inventory": true,
    "q80:d2:smooth-product:tensor-clenshaw-curtis:L1:mass": true,
    "q80:d2:smooth-product:tensor-clenshaw-curtis:L1:low-moments": true,
    "q80:d2:smooth-product:tensor-clenshaw-curtis:L2:callback-ledger": true,
    "q80:d2:smooth-product:tensor-clenshaw-curtis:L2:evaluation-cap": true,
    "q80:d2:smooth-product:tensor-clenshaw-curtis:L2:finite-return": true,
    "q80:d2:smooth-product:tensor-clenshaw-curtis:L2:canonical-inventory": true,
    "q80:d2:smooth-product:tensor-clenshaw-curtis:L2:mass": true,
    "q80:d2:smooth-product:tensor-clenshaw-curtis:L2:low-moments": true,
    "q80:d2:smooth-product:tensor-clenshaw-curtis:L3:callback-ledger": true,
    "q80:d2:smooth-product:tensor-clenshaw-curtis:L3:evaluation-cap": true,
    "q80:d2:smooth-product:tensor-clenshaw-curtis:L3:finite-return": true,
    "q80:d2:smooth-product:tensor-clenshaw-curtis:L3:canonical-inventory": true,
    "q80:d2:smooth-product:tensor-clenshaw-curtis:L3:mass": true,
    "q80:d2:smooth-product:tensor-clenshaw-curtis:L3:low-moments": true,
    "q80:d2:smooth-product:tensor-clenshaw-curtis:L3:required-finest-accuracy": true,
    "q80:d2:smooth-product:smolyak-delta:L1:callback-ledger": true,
    "q80:d2:smooth-product:smolyak-delta:L1:evaluation-cap": true,
    "q80:d2:smooth-product:smolyak-delta:L1:finite-return": true,
    "q80:d2:smooth-product:smolyak-delta:L1:canonical-inventory": true,
    "q80:d2:smooth-product:smolyak-delta:L1:mass": true,
    "q80:d2:smooth-product:smolyak-delta:L1:low-moments": true,
    "q80:d2:smooth-product:smolyak-delta:L1:delta-combination": true,
    "q80:d2:smooth-product:smolyak-delta:L2:callback-ledger": true,
    "q80:d2:smooth-product:smolyak-delta:L2:evaluation-cap": true,
    "q80:d2:smooth-product:smolyak-delta:L2:finite-return": true,
    "q80:d2:smooth-product:smolyak-delta:L2:canonical-inventory": true,
    "q80:d2:smooth-product:smolyak-delta:L2:mass": true,
    "q80:d2:smooth-product:smolyak-delta:L2:low-moments": true,
    "q80:d2:smooth-product:smolyak-delta:L2:delta-combination": true,
    "q80:d2:smooth-product:smolyak-delta:L3:callback-ledger": true,
    "q80:d2:smooth-product:smolyak-delta:L3:evaluation-cap": true,
    "q80:d2:smooth-product:smolyak-delta:L3:finite-return": true,
    "q80:d2:smooth-product:smolyak-delta:L3:canonical-inventory": true,
    "q80:d2:smooth-product:smolyak-delta:L3:mass": true,
    "q80:d2:smooth-product:smolyak-delta:L3:low-moments": true,
    "q80:d2:smooth-product:smolyak-delta:L4:callback-ledger": true,
    "q80:d2:smooth-product:smolyak-delta:L4:evaluation-cap": true,
    "q80:d2:smooth-product:smolyak-delta:L4:finite-return": true,
    "q80:d2:smooth-product:smolyak-delta:L4:canonical-inventory": true,
    "q80:d2:smooth-product:smolyak-delta:L4:mass": true,
    "q80:d2:smooth-product:smolyak-delta:L4:low-moments": true,
    "q80:d2:smooth-product:smolyak-delta:L4:required-finest-accuracy": true,
    "q80:d2:interaction-product:tensor-clenshaw-curtis:L1:callback-ledger": true,
    "q80:d2:interaction-product:tensor-clenshaw-curtis:L1:evaluation-cap": true,
    "q80:d2:interaction-product:tensor-clenshaw-curtis:L1:finite-return": true,
    "q80:d2:interaction-product:tensor-clenshaw-curtis:L1:canonical-inventory": true,
    "q80:d2:interaction-product:tensor-clenshaw-curtis:L1:mass": true,
    "q80:d2:interaction-product:tensor-clenshaw-curtis:L1:low-moments": true,
    "q80:d2:interaction-product:tensor-clenshaw-curtis:L1:required-product-moment": true,
    "q80:d2:interaction-product:tensor-clenshaw-curtis:L2:callback-ledger": true,
    "q80:d2:interaction-product:tensor-clenshaw-curtis:L2:evaluation-cap": true,
    "q80:d2:interaction-product:tensor-clenshaw-curtis:L2:finite-return": true,
    "q80:d2:interaction-product:tensor-clenshaw-curtis:L2:canonical-inventory": true,
    "q80:d2:interaction-product:tensor-clenshaw-curtis:L2:mass": true,
    "q80:d2:interaction-product:tensor-clenshaw-curtis:L2:low-moments": true,
    "q80:d2:interaction-product:tensor-clenshaw-curtis:L2:required-product-moment": true,
    "q80:d2:interaction-product:tensor-clenshaw-curtis:L3:callback-ledger": true,
    "q80:d2:interaction-product:tensor-clenshaw-curtis:L3:evaluation-cap": true,
    "q80:d2:interaction-product:tensor-clenshaw-curtis:L3:finite-return": true,
    "q80:d2:interaction-product:tensor-clenshaw-curtis:L3:canonical-inventory": true,
    "q80:d2:interaction-product:tensor-clenshaw-curtis:L3:mass": true,
    "q80:d2:interaction-product:tensor-clenshaw-curtis:L3:low-moments": true,
    "q80:d2:interaction-product:tensor-clenshaw-curtis:L3:required-product-moment": true,
    "q80:d2:interaction-product:smolyak-delta:L1:callback-ledger": true,
    "q80:d2:interaction-product:smolyak-delta:L1:evaluation-cap": true,
    "q80:d2:interaction-product:smolyak-delta:L1:finite-return": true,
    "q80:d2:interaction-product:smolyak-delta:L1:canonical-inventory": true,
    "q80:d2:interaction-product:smolyak-delta:L1:mass": true,
    "q80:d2:interaction-product:smolyak-delta:L1:low-moments": true,
    "q80:d2:interaction-product:smolyak-delta:L1:delta-combination": true,
    "q80:d2:interaction-product:smolyak-delta:L1:underresolution-identity": true,
    "q80:d2:interaction-product:smolyak-delta:L2:callback-ledger": true,
    "q80:d2:interaction-product:smolyak-delta:L2:evaluation-cap": true,
    "q80:d2:interaction-product:smolyak-delta:L2:finite-return": true,
    "q80:d2:interaction-product:smolyak-delta:L2:canonical-inventory": true,
    "q80:d2:interaction-product:smolyak-delta:L2:mass": true,
    "q80:d2:interaction-product:smolyak-delta:L2:low-moments": true,
    "q80:d2:interaction-product:smolyak-delta:L2:delta-combination": true,
    "q80:d2:interaction-product:smolyak-delta:L2:required-product-moment": true,
    "q80:d2:interaction-product:smolyak-delta:L3:callback-ledger": true,
    "q80:d2:interaction-product:smolyak-delta:L3:evaluation-cap": true,
    "q80:d2:interaction-product:smolyak-delta:L3:finite-return": true,
    "q80:d2:interaction-product:smolyak-delta:L3:canonical-inventory": true,
    "q80:d2:interaction-product:smolyak-delta:L3:mass": true,
    "q80:d2:interaction-product:smolyak-delta:L3:low-moments": true,
    "q80:d2:interaction-product:smolyak-delta:L3:required-product-moment": true,
    "q80:d2:interaction-product:smolyak-delta:L4:callback-ledger": true,
    "q80:d2:interaction-product:smolyak-delta:L4:evaluation-cap": true,
    "q80:d2:interaction-product:smolyak-delta:L4:finite-return": true,
    "q80:d2:interaction-product:smolyak-delta:L4:canonical-inventory": true,
    "q80:d2:interaction-product:smolyak-delta:L4:mass": true,
    "q80:d2:interaction-product:smolyak-delta:L4:low-moments": true,
    "q80:d2:interaction-product:smolyak-delta:L4:required-product-moment": true,
    "q80:d3:smooth-product:tensor-clenshaw-curtis:L1:callback-ledger": true,
    "q80:d3:smooth-product:tensor-clenshaw-curtis:L1:evaluation-cap": true,
    "q80:d3:smooth-product:tensor-clenshaw-curtis:L1:finite-return": true,
    "q80:d3:smooth-product:tensor-clenshaw-curtis:L1:canonical-inventory": true,
    "q80:d3:smooth-product:tensor-clenshaw-curtis:L1:mass": true,
    "q80:d3:smooth-product:tensor-clenshaw-curtis:L1:low-moments": true,
    "q80:d3:smooth-product:tensor-clenshaw-curtis:L2:callback-ledger": true,
    "q80:d3:smooth-product:tensor-clenshaw-curtis:L2:evaluation-cap": true,
    "q80:d3:smooth-product:tensor-clenshaw-curtis:L2:finite-return": true,
    "q80:d3:smooth-product:tensor-clenshaw-curtis:L2:canonical-inventory": true,
    "q80:d3:smooth-product:tensor-clenshaw-curtis:L2:mass": true,
    "q80:d3:smooth-product:tensor-clenshaw-curtis:L2:low-moments": true,
    "q80:d3:smooth-product:tensor-clenshaw-curtis:L3:callback-ledger": true,
    "q80:d3:smooth-product:tensor-clenshaw-curtis:L3:evaluation-cap": true,
    "q80:d3:smooth-product:tensor-clenshaw-curtis:L3:finite-return": true,
    "q80:d3:smooth-product:tensor-clenshaw-curtis:L3:canonical-inventory": true,
    "q80:d3:smooth-product:tensor-clenshaw-curtis:L3:mass": true,
    "q80:d3:smooth-product:tensor-clenshaw-curtis:L3:low-moments": true,
    "q80:d3:smooth-product:tensor-clenshaw-curtis:L3:required-finest-accuracy": true,
    "q80:d3:smooth-product:smolyak-delta:L1:callback-ledger": true,
    "q80:d3:smooth-product:smolyak-delta:L1:evaluation-cap": true,
    "q80:d3:smooth-product:smolyak-delta:L1:finite-return": true,
    "q80:d3:smooth-product:smolyak-delta:L1:canonical-inventory": true,
    "q80:d3:smooth-product:smolyak-delta:L1:mass": true,
    "q80:d3:smooth-product:smolyak-delta:L1:low-moments": true,
    "q80:d3:smooth-product:smolyak-delta:L1:delta-combination": true,
    "q80:d3:smooth-product:smolyak-delta:L2:callback-ledger": true,
    "q80:d3:smooth-product:smolyak-delta:L2:evaluation-cap": true,
    "q80:d3:smooth-product:smolyak-delta:L2:finite-return": true,
    "q80:d3:smooth-product:smolyak-delta:L2:canonical-inventory": true,
    "q80:d3:smooth-product:smolyak-delta:L2:mass": true,
    "q80:d3:smooth-product:smolyak-delta:L2:low-moments": true,
    "q80:d3:smooth-product:smolyak-delta:L2:delta-combination": true,
    "q80:d3:smooth-product:smolyak-delta:L3:callback-ledger": true,
    "q80:d3:smooth-product:smolyak-delta:L3:evaluation-cap": true,
    "q80:d3:smooth-product:smolyak-delta:L3:finite-return": true,
    "q80:d3:smooth-product:smolyak-delta:L3:canonical-inventory": true,
    "q80:d3:smooth-product:smolyak-delta:L3:mass": true,
    "q80:d3:smooth-product:smolyak-delta:L3:low-moments": true,
    "q80:d3:smooth-product:smolyak-delta:L4:callback-ledger": true,
    "q80:d3:smooth-product:smolyak-delta:L4:evaluation-cap": true,
    "q80:d3:smooth-product:smolyak-delta:L4:finite-return": true,
    "q80:d3:smooth-product:smolyak-delta:L4:canonical-inventory": true,
    "q80:d3:smooth-product:smolyak-delta:L4:mass": true,
    "q80:d3:smooth-product:smolyak-delta:L4:low-moments": true,
    "q80:d3:smooth-product:smolyak-delta:L4:required-finest-accuracy": true,
    "q80:d3:interaction-product:tensor-clenshaw-curtis:L1:callback-ledger": true,
    "q80:d3:interaction-product:tensor-clenshaw-curtis:L1:evaluation-cap": true,
    "q80:d3:interaction-product:tensor-clenshaw-curtis:L1:finite-return": true,
    "q80:d3:interaction-product:tensor-clenshaw-curtis:L1:canonical-inventory": true,
    "q80:d3:interaction-product:tensor-clenshaw-curtis:L1:mass": true,
    "q80:d3:interaction-product:tensor-clenshaw-curtis:L1:low-moments": true,
    "q80:d3:interaction-product:tensor-clenshaw-curtis:L1:required-product-moment": true,
    "q80:d3:interaction-product:tensor-clenshaw-curtis:L2:callback-ledger": true,
    "q80:d3:interaction-product:tensor-clenshaw-curtis:L2:evaluation-cap": true,
    "q80:d3:interaction-product:tensor-clenshaw-curtis:L2:finite-return": true,
    "q80:d3:interaction-product:tensor-clenshaw-curtis:L2:canonical-inventory": true,
    "q80:d3:interaction-product:tensor-clenshaw-curtis:L2:mass": true,
    "q80:d3:interaction-product:tensor-clenshaw-curtis:L2:low-moments": true,
    "q80:d3:interaction-product:tensor-clenshaw-curtis:L2:required-product-moment": true,
    "q80:d3:interaction-product:tensor-clenshaw-curtis:L3:callback-ledger": true,
    "q80:d3:interaction-product:tensor-clenshaw-curtis:L3:evaluation-cap": true,
    "q80:d3:interaction-product:tensor-clenshaw-curtis:L3:finite-return": true,
    "q80:d3:interaction-product:tensor-clenshaw-curtis:L3:canonical-inventory": true,
    "q80:d3:interaction-product:tensor-clenshaw-curtis:L3:mass": true,
    "q80:d3:interaction-product:tensor-clenshaw-curtis:L3:low-moments": true,
    "q80:d3:interaction-product:tensor-clenshaw-curtis:L3:required-product-moment": true,
    "q80:d3:interaction-product:smolyak-delta:L1:callback-ledger": true,
    "q80:d3:interaction-product:smolyak-delta:L1:evaluation-cap": true,
    "q80:d3:interaction-product:smolyak-delta:L1:finite-return": true,
    "q80:d3:interaction-product:smolyak-delta:L1:canonical-inventory": true,
    "q80:d3:interaction-product:smolyak-delta:L1:mass": true,
    "q80:d3:interaction-product:smolyak-delta:L1:low-moments": true,
    "q80:d3:interaction-product:smolyak-delta:L1:delta-combination": true,
    "q80:d3:interaction-product:smolyak-delta:L1:underresolution-identity": true,
    "q80:d3:interaction-product:smolyak-delta:L2:callback-ledger": true,
    "q80:d3:interaction-product:smolyak-delta:L2:evaluation-cap": true,
    "q80:d3:interaction-product:smolyak-delta:L2:finite-return": true,
    "q80:d3:interaction-product:smolyak-delta:L2:canonical-inventory": true,
    "q80:d3:interaction-product:smolyak-delta:L2:mass": true,
    "q80:d3:interaction-product:smolyak-delta:L2:low-moments": true,
    "q80:d3:interaction-product:smolyak-delta:L2:delta-combination": true,
    "q80:d3:interaction-product:smolyak-delta:L2:underresolution-identity": true,
    "q80:d3:interaction-product:smolyak-delta:L3:callback-ledger": true,
    "q80:d3:interaction-product:smolyak-delta:L3:evaluation-cap": true,
    "q80:d3:interaction-product:smolyak-delta:L3:finite-return": true,
    "q80:d3:interaction-product:smolyak-delta:L3:canonical-inventory": true,
    "q80:d3:interaction-product:smolyak-delta:L3:mass": true,
    "q80:d3:interaction-product:smolyak-delta:L3:low-moments": true,
    "q80:d3:interaction-product:smolyak-delta:L3:required-product-moment": true,
    "q80:d3:interaction-product:smolyak-delta:L4:callback-ledger": true,
    "q80:d3:interaction-product:smolyak-delta:L4:evaluation-cap": true,
    "q80:d3:interaction-product:smolyak-delta:L4:finite-return": true,
    "q80:d3:interaction-product:smolyak-delta:L4:canonical-inventory": true,
    "q80:d3:interaction-product:smolyak-delta:L4:mass": true,
    "q80:d3:interaction-product:smolyak-delta:L4:low-moments": true,
    "q80:d3:interaction-product:smolyak-delta:L4:required-product-moment": true,
    "q80:d4:smooth-product:tensor-clenshaw-curtis:L1:callback-ledger": true,
    "q80:d4:smooth-product:tensor-clenshaw-curtis:L1:evaluation-cap": true,
    "q80:d4:smooth-product:tensor-clenshaw-curtis:L1:finite-return": true,
    "q80:d4:smooth-product:tensor-clenshaw-curtis:L1:canonical-inventory": true,
    "q80:d4:smooth-product:tensor-clenshaw-curtis:L1:mass": true,
    "q80:d4:smooth-product:tensor-clenshaw-curtis:L1:low-moments": true,
    "q80:d4:smooth-product:tensor-clenshaw-curtis:L2:callback-ledger": true,
    "q80:d4:smooth-product:tensor-clenshaw-curtis:L2:evaluation-cap": true,
    "q80:d4:smooth-product:tensor-clenshaw-curtis:L2:finite-return": true,
    "q80:d4:smooth-product:tensor-clenshaw-curtis:L2:canonical-inventory": true,
    "q80:d4:smooth-product:tensor-clenshaw-curtis:L2:mass": true,
    "q80:d4:smooth-product:tensor-clenshaw-curtis:L2:low-moments": true,
    "q80:d4:smooth-product:tensor-clenshaw-curtis:L3:callback-ledger": true,
    "q80:d4:smooth-product:tensor-clenshaw-curtis:L3:evaluation-cap": true,
    "q80:d4:smooth-product:tensor-clenshaw-curtis:L3:finite-return": true,
    "q80:d4:smooth-product:tensor-clenshaw-curtis:L3:canonical-inventory": true,
    "q80:d4:smooth-product:tensor-clenshaw-curtis:L3:mass": true,
    "q80:d4:smooth-product:tensor-clenshaw-curtis:L3:low-moments": true,
    "q80:d4:smooth-product:tensor-clenshaw-curtis:L3:required-finest-accuracy": true,
    "q80:d4:smooth-product:smolyak-delta:L1:callback-ledger": true,
    "q80:d4:smooth-product:smolyak-delta:L1:evaluation-cap": true,
    "q80:d4:smooth-product:smolyak-delta:L1:finite-return": true,
    "q80:d4:smooth-product:smolyak-delta:L1:canonical-inventory": true,
    "q80:d4:smooth-product:smolyak-delta:L1:mass": true,
    "q80:d4:smooth-product:smolyak-delta:L1:low-moments": true,
    "q80:d4:smooth-product:smolyak-delta:L2:callback-ledger": true,
    "q80:d4:smooth-product:smolyak-delta:L2:evaluation-cap": true,
    "q80:d4:smooth-product:smolyak-delta:L2:finite-return": true,
    "q80:d4:smooth-product:smolyak-delta:L2:canonical-inventory": true,
    "q80:d4:smooth-product:smolyak-delta:L2:mass": true,
    "q80:d4:smooth-product:smolyak-delta:L2:low-moments": true,
    "q80:d4:smooth-product:smolyak-delta:L3:callback-ledger": true,
    "q80:d4:smooth-product:smolyak-delta:L3:evaluation-cap": true,
    "q80:d4:smooth-product:smolyak-delta:L3:finite-return": true,
    "q80:d4:smooth-product:smolyak-delta:L3:canonical-inventory": true,
    "q80:d4:smooth-product:smolyak-delta:L3:mass": true,
    "q80:d4:smooth-product:smolyak-delta:L3:low-moments": true,
    "q80:d4:smooth-product:smolyak-delta:L4:callback-ledger": true,
    "q80:d4:smooth-product:smolyak-delta:L4:evaluation-cap": true,
    "q80:d4:smooth-product:smolyak-delta:L4:finite-return": true,
    "q80:d4:smooth-product:smolyak-delta:L4:canonical-inventory": true,
    "q80:d4:smooth-product:smolyak-delta:L4:mass": true,
    "q80:d4:smooth-product:smolyak-delta:L4:low-moments": true,
    "q80:d4:smooth-product:smolyak-delta:L4:required-finest-accuracy": true,
    "q80:d4:interaction-product:tensor-clenshaw-curtis:L1:callback-ledger": true,
    "q80:d4:interaction-product:tensor-clenshaw-curtis:L1:evaluation-cap": true,
    "q80:d4:interaction-product:tensor-clenshaw-curtis:L1:finite-return": true,
    "q80:d4:interaction-product:tensor-clenshaw-curtis:L1:canonical-inventory": true,
    "q80:d4:interaction-product:tensor-clenshaw-curtis:L1:mass": true,
    "q80:d4:interaction-product:tensor-clenshaw-curtis:L1:low-moments": true,
    "q80:d4:interaction-product:tensor-clenshaw-curtis:L1:required-product-moment": true,
    "q80:d4:interaction-product:tensor-clenshaw-curtis:L2:callback-ledger": true,
    "q80:d4:interaction-product:tensor-clenshaw-curtis:L2:evaluation-cap": true,
    "q80:d4:interaction-product:tensor-clenshaw-curtis:L2:finite-return": true,
    "q80:d4:interaction-product:tensor-clenshaw-curtis:L2:canonical-inventory": true,
    "q80:d4:interaction-product:tensor-clenshaw-curtis:L2:mass": true,
    "q80:d4:interaction-product:tensor-clenshaw-curtis:L2:low-moments": true,
    "q80:d4:interaction-product:tensor-clenshaw-curtis:L2:required-product-moment": true,
    "q80:d4:interaction-product:tensor-clenshaw-curtis:L3:callback-ledger": true,
    "q80:d4:interaction-product:tensor-clenshaw-curtis:L3:evaluation-cap": true,
    "q80:d4:interaction-product:tensor-clenshaw-curtis:L3:finite-return": true,
    "q80:d4:interaction-product:tensor-clenshaw-curtis:L3:canonical-inventory": true,
    "q80:d4:interaction-product:tensor-clenshaw-curtis:L3:mass": true,
    "q80:d4:interaction-product:tensor-clenshaw-curtis:L3:low-moments": true,
    "q80:d4:interaction-product:tensor-clenshaw-curtis:L3:required-product-moment": true,
    "q80:d4:interaction-product:smolyak-delta:L1:callback-ledger": true,
    "q80:d4:interaction-product:smolyak-delta:L1:evaluation-cap": true,
    "q80:d4:interaction-product:smolyak-delta:L1:finite-return": true,
    "q80:d4:interaction-product:smolyak-delta:L1:canonical-inventory": true,
    "q80:d4:interaction-product:smolyak-delta:L1:mass": true,
    "q80:d4:interaction-product:smolyak-delta:L1:low-moments": true,
    "q80:d4:interaction-product:smolyak-delta:L1:underresolution-identity": true,
    "q80:d4:interaction-product:smolyak-delta:L2:callback-ledger": true,
    "q80:d4:interaction-product:smolyak-delta:L2:evaluation-cap": true,
    "q80:d4:interaction-product:smolyak-delta:L2:finite-return": true,
    "q80:d4:interaction-product:smolyak-delta:L2:canonical-inventory": true,
    "q80:d4:interaction-product:smolyak-delta:L2:mass": true,
    "q80:d4:interaction-product:smolyak-delta:L2:low-moments": true,
    "q80:d4:interaction-product:smolyak-delta:L2:underresolution-identity": true,
    "q80:d4:interaction-product:smolyak-delta:L3:callback-ledger": true,
    "q80:d4:interaction-product:smolyak-delta:L3:evaluation-cap": true,
    "q80:d4:interaction-product:smolyak-delta:L3:finite-return": true,
    "q80:d4:interaction-product:smolyak-delta:L3:canonical-inventory": true,
    "q80:d4:interaction-product:smolyak-delta:L3:mass": true,
    "q80:d4:interaction-product:smolyak-delta:L3:low-moments": true,
    "q80:d4:interaction-product:smolyak-delta:L3:underresolution-identity": true,
    "q80:d4:interaction-product:smolyak-delta:L4:callback-ledger": true,
    "q80:d4:interaction-product:smolyak-delta:L4:evaluation-cap": true,
    "q80:d4:interaction-product:smolyak-delta:L4:finite-return": true,
    "q80:d4:interaction-product:smolyak-delta:L4:canonical-inventory": true,
    "q80:d4:interaction-product:smolyak-delta:L4:mass": true,
    "q80:d4:interaction-product:smolyak-delta:L4:low-moments": true,
    "q80:d4:interaction-product:smolyak-delta:L4:required-product-moment": true,
    "tensor-smolyak-dimensions:fixed-record-count": true,
    "tensor-smolyak-dimensions:unique-record-ids": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/tensor-smolyak-dimensions/index.json

![Actual two-dimensional nodes and signed integration weights](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/results/tensor-smolyak-dimensions-preview.png)

Actual two-dimensional nodes and signed integration weights

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/atlas-quadrature-controls-2026-11-25.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

## Sources and review scope

- Fast Construction of the Fejer and Clenshaw-Curtis Quadrature Rules [accessed 2026-11-25]. https://www.sam.math.ethz.ch/sam_reports/reports_final/reports2008/2008-07.pdf; review_level=selected-primary-body-text

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
