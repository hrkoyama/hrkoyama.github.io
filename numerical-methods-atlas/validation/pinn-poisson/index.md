# 1D Poisson PINNと独立格子誤差

3固定seedの49パラメータPINNを解析解・FDと比較します。

**使用手法**

- [PINN・ニューラル演算子](https://hrkoyama.github.io/numerical-methods-atlas/methods/pinn-operators/?lang=ja) (`pinn-operators`)
- [Thomas法／三重対角消去](https://hrkoyama.github.io/numerical-methods-atlas/methods/thomas/?lang=ja) (`thomas`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/pinn-poisson/?lang=ja#pinn-poisson-ja-algorithm)

x(1−x)を掛けて境界値を厳密に組み込むtanhネットワークを、解析的な全パラメータJacobian付きTRF最小二乗法で学習します。固定予算後の全モデルを保存し、31/63/127未知数の2次中心差分とThomas法も計算します。

$$
-u_{xx}=\pi^2\sin(\pi x),\quad 0<x<1,\quad u(0)=u(1)=0
$$

$$
u_\theta(x)=x(1-x)\left[b_0+\sum_{j=1}^{16}a_j\tanh(w_jx+b_j)\right]
$$

$$
r_i=\frac{-u_{\theta,xx}(x_i)-\pi^2\sin(\pi x_i)}{\pi^2},\quad L=\frac1{64}\sum_{i=1}^{64}r_i^2
$$

- [Poisson・Laplace方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#poisson-laplace-ja) (`poisson-laplace`)

無次元区間[0,1]で −uₓₓ=π²sin(πx)、u(0)=u(1)=0。中間層16素子・49実パラメータ、固定seed 8401–8403、学習64点と独立評価257点を用います。


**問題の図**

![1D Poisson PINNと独立格子誤差：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/pinn-poisson.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[1次元Poisson・Dirichlet製造解](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-dirichlet/?lang=ja) (`poisson-1d-dirichlet`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-dirichlet/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/pinn-poisson/?lang=ja#pinn-poisson-ja-validation)

全49列の残差Jacobianと損失勾配、空間微分を別資格段階で独立照合。解析解sin(πx)に対する独立点誤差、PDE残差、境界値、FD誤差を別に保存します。収束・精度目標の実際の真偽を残し、正常な予算終了を収束と呼びません。

- [Poisson／正弦波の製造解](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-poisson-manufactured-ja) (`poisson-manufactured`; 関連モデルの参照 · 製造解)

単一sin(πx)の共通固定入力とは一致しますが、保存比較図は複合正弦製造解も含みます。同じ零Dirichletでも全ソースが同一ではありません。

- [1D Poisson PINNと独立格子誤差](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-pinn-poisson-ja) (`pinn-poisson`; 関連モデルの参照 · 製造解)

1つの滑らかなPoisson問題と3seedの固定予算実験です。小さい学習損失だけで独立点精度の達成や一般的なPINN学習成功を保証しません。未達目標も表示します。
## 前提・単位・境界

無次元区間[0,1]で −uₓₓ=π²sin(πx)、u(0)=u(1)=0。中間層16素子・49実パラメータ、固定seed 8401–8403、学習64点と独立評価257点を用います。

**編集上の補足**

1つの滑らかなPoisson問題と3seedの固定予算実験です。小さい学習損失だけで独立点精度の達成や一般的なPINN学習成功を保証しません。未達目標も表示します。

## 採用した計算法

x(1−x)を掛けて境界値を厳密に組み込むtanhネットワークを、解析的な全パラメータJacobian付きTRF最小二乗法で学習します。固定予算後の全モデルを保存し、31/63/127未知数の2次中心差分とThomas法も計算します。

$$
-u_{xx}=\pi^2\sin(\pi x),\quad 0<x<1,\quad u(0)=u(1)=0
$$

$$
u_\theta(x)=x(1-x)\left[b_0+\sum_{j=1}^{16}a_j\tanh(w_jx+b_j)\right]
$$

$$
r_i=\frac{-u_{\theta,xx}(x_i)-\pi^2\sin(\pi x_i)}{\pi^2},\quad L=\frac1{64}\sum_{i=1}^{64}r_i^2
$$

## 比較・検証

全49列の残差Jacobianと損失勾配、空間微分を別資格段階で独立照合。解析解sin(πx)に対する独立点誤差、PDE残差、境界値、FD誤差を別に保存します。収束・精度目標の実際の真偽を残し、正常な予算終了を収束と呼びません。

## 確認の限界

1つの滑らかなPoisson問題と3seedの固定予算実験です。小さい学習損失だけで独立点精度の達成や一般的なPINN学習成功を保証しません。未達目標も表示します。

## 元の数値目標と未達の結果

実行・記録の検証合格は、元の精度目標の全達成を意味しません。元の判定を保持します。

```json
{
  "original_target_results": {
    "seed-8401:optimizer-converged": false,
    "seed-8401:solution_Linf": true,
    "seed-8401:PDE_normalized_RMS": true,
    "seed-8401:boundary_Linf": true,
    "seed-8402:optimizer-converged": false,
    "seed-8402:solution_Linf": true,
    "seed-8402:PDE_normalized_RMS": true,
    "seed-8402:boundary_Linf": true,
    "seed-8403:optimizer-converged": false,
    "seed-8403:solution_Linf": true,
    "seed-8403:PDE_normalized_RMS": true,
    "seed-8403:boundary_Linf": true,
    "fd-31:solution_Linf": true,
    "fd-63:solution_Linf": true,
    "fd-127:solution_Linf": true
  },
  "original_target_summary": {
    "met": 12,
    "total": 15,
    "all_met": false,
    "acceptance_sha256": "b468e78459cf81bda6a32cade0051f6615b44def256c66308ae7acc82ff516ce"
  }
}
```

## 保存実測値と判定

```json
{
  "metrics": {
    "training_seeds": 3,
    "parameters": 49,
    "independent_grid_points": 257,
    "FD_runs": 3
  },
  "checks": {
    "seed-8401:finite-shape": true,
    "seed-8401:optimizer-return-status": true,
    "seed-8401:actual-work": true,
    "seed-8402:finite-shape": true,
    "seed-8402:optimizer-return-status": true,
    "seed-8402:actual-work": true,
    "seed-8403:finite-shape": true,
    "seed-8403:optimizer-return-status": true,
    "seed-8403:actual-work": true,
    "fd-31:true-residual": true,
    "fd-63:true-residual": true,
    "fd-127:true-residual": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/pinn-poisson/index.json

![3固定seedの49パラメータPINNを解析解・FDと比較します。 保存値だけを描画します。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/pinn-poisson-preview.png)

3固定seedの49パラメータPINNを解析解・FDと比較します。 保存値だけを描画します。

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/atlas-small-models-2026-11-25.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

## 出典と確認範囲

- Physics Informed Deep Learning (Part I): Data-driven Solutions of Nonlinear Partial Differential Equations [accessed 2026-11-24]. https://arxiv.org/pdf/1711.10561; review_level=selected-primary-body
Extracted PDF text selected pp.4–6, §2 continuous-time residual, Eq(2)–(4), Burgers setup and loss/optimizer discussion; not all 22 pages and not visual PDF audit.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Poisson PINN: independent grid error

Compare a 49-parameter PINN for three fixed seeds with analytic and finite-difference solutions.

**Methods used**

- [PINNs and neural operators](https://hrkoyama.github.io/numerical-methods-atlas/methods/pinn-operators/?lang=en) (`pinn-operators`)
- [Thomas tridiagonal elimination](https://hrkoyama.github.io/numerical-methods-atlas/methods/thomas/?lang=en) (`thomas`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/pinn-poisson/?lang=en#pinn-poisson-en-algorithm)

Train a hard-boundary tanh ansatz with trust-region reflective least squares and an analytic parameter Jacobian. Retain every returned model under the fixed budget. Also solve second-order finite differences with 31, 63 and 127 unknowns using the Thomas algorithm.

$$
-u_{xx}=\pi^2\sin(\pi x),\quad 0<x<1,\quad u(0)=u(1)=0
$$

$$
u_\theta(x)=x(1-x)\left[b_0+\sum_{j=1}^{16}a_j\tanh(w_jx+b_j)\right]
$$

$$
r_i=\frac{-u_{\theta,xx}(x_i)-\pi^2\sin(\pi x_i)}{\pi^2},\quad L=\frac1{64}\sum_{i=1}^{64}r_i^2
$$

- [Poisson / Laplace equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#poisson-laplace-en) (`poisson-laplace`)

Solve dimensionless −uₓₓ=π² sin(πx) on [0,1] with zero Dirichlet data. Use sixteen hidden units, 49 real parameters, seeds 8401–8403, 64 training points and 257 separate evaluation points.


**Problem figure**

![Poisson PINN: independent grid error: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/pinn-poisson.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[1D Poisson / smooth Dirichlet manufactured solutions](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-dirichlet/?lang=en) (`poisson-1d-dirichlet`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-dirichlet/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/pinn-poisson/?lang=en#pinn-poisson-en-validation)

Independently qualify all 49 residual-Jacobian columns, loss-gradient coordinates and spatial derivatives. Save off-training solution error against sin(πx), PDE residual, boundary error and finite-difference error separately. Preserve actual convergence and accuracy decisions; a normal budget return is not convergence.

- [Poisson / manufactured sine](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-poisson-manufactured-en) (`poisson-manufactured`; Related-model reference · Manufactured solution)

It matches the single-sine common fixed input, but saved comparisons also contain composite-sine manufactured forcing. Zero Dirichlet boundaries do not make all sources identical.

- [Poisson PINN: independent grid error](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-pinn-poisson-en) (`pinn-poisson`; Related-model reference · Manufactured solution)

This fixed-budget study covers one smooth Poisson problem and three seeds. A small training loss does not establish independent-point accuracy or general PINN training success. Unmet goals remain visible.
## Assumptions, units and boundaries

Solve dimensionless −uₓₓ=π² sin(πx) on [0,1] with zero Dirichlet data. Use sixteen hidden units, 49 real parameters, seeds 8401–8403, 64 training points and 257 separate evaluation points.

**Editorial clarification**

This fixed-budget study covers one smooth Poisson problem and three seeds. A small training loss does not establish independent-point accuracy or general PINN training success. Unmet goals remain visible.

## Adopted numerical method

Train a hard-boundary tanh ansatz with trust-region reflective least squares and an analytic parameter Jacobian. Retain every returned model under the fixed budget. Also solve second-order finite differences with 31, 63 and 127 unknowns using the Thomas algorithm.

$$
-u_{xx}=\pi^2\sin(\pi x),\quad 0<x<1,\quad u(0)=u(1)=0
$$

$$
u_\theta(x)=x(1-x)\left[b_0+\sum_{j=1}^{16}a_j\tanh(w_jx+b_j)\right]
$$

$$
r_i=\frac{-u_{\theta,xx}(x_i)-\pi^2\sin(\pi x_i)}{\pi^2},\quad L=\frac1{64}\sum_{i=1}^{64}r_i^2
$$

## References and validation

Independently qualify all 49 residual-Jacobian columns, loss-gradient coordinates and spatial derivatives. Save off-training solution error against sin(πx), PDE residual, boundary error and finite-difference error separately. Preserve actual convergence and accuracy decisions; a normal budget return is not convergence.

## Limits

This fixed-budget study covers one smooth Poisson problem and three seeds. A small training loss does not establish independent-point accuracy or general PINN training success. Unmet goals remain visible.

## Original numerical targets and unmet outcomes

Passing reproduction/reporting verification does not mean that all original accuracy goals were met. Original decisions are retained.

```json
{
  "original_target_results": {
    "seed-8401:optimizer-converged": false,
    "seed-8401:solution_Linf": true,
    "seed-8401:PDE_normalized_RMS": true,
    "seed-8401:boundary_Linf": true,
    "seed-8402:optimizer-converged": false,
    "seed-8402:solution_Linf": true,
    "seed-8402:PDE_normalized_RMS": true,
    "seed-8402:boundary_Linf": true,
    "seed-8403:optimizer-converged": false,
    "seed-8403:solution_Linf": true,
    "seed-8403:PDE_normalized_RMS": true,
    "seed-8403:boundary_Linf": true,
    "fd-31:solution_Linf": true,
    "fd-63:solution_Linf": true,
    "fd-127:solution_Linf": true
  },
  "original_target_summary": {
    "met": 12,
    "total": 15,
    "all_met": false,
    "acceptance_sha256": "b468e78459cf81bda6a32cade0051f6615b44def256c66308ae7acc82ff516ce"
  }
}
```

## Stored measurements and decisions

```json
{
  "metrics": {
    "training_seeds": 3,
    "parameters": 49,
    "independent_grid_points": 257,
    "FD_runs": 3
  },
  "checks": {
    "seed-8401:finite-shape": true,
    "seed-8401:optimizer-return-status": true,
    "seed-8401:actual-work": true,
    "seed-8402:finite-shape": true,
    "seed-8402:optimizer-return-status": true,
    "seed-8402:actual-work": true,
    "seed-8403:finite-shape": true,
    "seed-8403:optimizer-return-status": true,
    "seed-8403:actual-work": true,
    "fd-31:true-residual": true,
    "fd-63:true-residual": true,
    "fd-127:true-residual": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/pinn-poisson/index.json

![Compare a 49-parameter PINN for three fixed seeds with analytic and finite-difference solutions. This figure reads saved data only.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/pinn-poisson-preview.png)

Compare a 49-parameter PINN for three fixed seeds with analytic and finite-difference solutions. This figure reads saved data only.

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/atlas-small-models-2026-11-25.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

## Sources and review scope

- Physics Informed Deep Learning (Part I): Data-driven Solutions of Nonlinear Partial Differential Equations [accessed 2026-11-24]. https://arxiv.org/pdf/1711.10561; review_level=selected-primary-body
Extracted PDF text selected pp.4–6, §2 continuous-time residual, Eq(2)–(4), Burgers setup and loss/optimizer discussion; not all 22 pages and not visual PDF audit.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
