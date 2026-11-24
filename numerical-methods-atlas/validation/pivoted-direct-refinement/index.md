# 部分ピボットLU・Choleskyと反復改良

独立の厳密有理数解と比較し、条件数・前進誤差・後退誤差・ピボット増大を分けます。

**使用手法**

- [部分ピボットLUと混合精度反復改良](https://hrkoyama.github.io/numerical-methods-atlas/methods/lu-partial-pivoting/?lang=ja) (`lu-partial-pivoting`)
- [Cholesky分解と三角代入](https://hrkoyama.github.io/numerical-methods-atlas/methods/cholesky/?lang=ja) (`cholesky`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/pivoted-direct-refinement/?lang=ja#pivoted-direct-refinement-ja-algorithm)

手書き部分ピボットLU・下三角Cholesky・前後代入。

$$
PA=LU
$$

$$
A=LL^T
$$

$$
x_(j+1)=x_j+solve_factor32(b-A*x_j)
$$

- [有限次元線形方程式と行列分解](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#finite-dimensional-linear-system-ja) (`finite-dimensional-linear-system`)

SPD12、低ランク近特異8、Hilbert5、Wilkinson12を固定。binary32因子・三角解法とbinary64残差・補正の5回です。


**問題の図**

![部分ピボットLU・Choleskyと反復改良：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/pivoted-direct-refinement.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[部分ピボットLU・Choleskyと反復改良](https://hrkoyama.github.io/numerical-methods-atlas/problems/pivoted-direct-refinement/?lang=ja) (`pivoted-direct-refinement`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/pivoted-direct-refinement/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/pivoted-direct-refinement/?lang=ja#pivoted-direct-refinement-ja-validation)

実binary64入力をFraction有理数で厳密に解き、別のLAPACK DGESV/DPOSVへ照合。条件数・前進誤差・後退誤差を分離。 保存する有理数参照ベクトルは、厳密Fraction解の各成分をbinary64へ丸めたものです。

- [部分ピボットLU/Cholesky：実二進入力の厳密有理数参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-pivoted-direct-refinement-ja) (`pivoted-direct-refinement`; 同じ問題の参照 · 解析参照)

小さい固定例のみ。一般の高条件数系で混合精度の収束は保証しません。
## 前提・単位・境界

SPD12、低ランク近特異8、Hilbert5、Wilkinson12を固定。binary32因子・三角解法とbinary64残差・補正の5回です。

**編集上の補足**

小さい固定例のみ。一般の高条件数系で混合精度の収束は保証しません。

## 採用した計算法

手書き部分ピボットLU・下三角Cholesky・前後代入。

$$
PA=LU
$$

$$
A=LL^T
$$

$$
x_(j+1)=x_j+solve_factor32(b-A*x_j)
$$

## 比較・検証

実binary64入力をFraction有理数で厳密に解き、別のLAPACK DGESV/DPOSVへ照合。条件数・前進誤差・後退誤差を分離。 保存する有理数参照ベクトルは、厳密Fraction解の各成分をbinary64へ丸めたものです。

## 確認の限界

小さい固定例のみ。一般の高条件数系で混合精度の収束は保証しません。

## 保存実測値と判定

```json
{
  "metrics": {
    "max_condition_infinity": 943656.0000016841,
    "max_relative_forward_error": 7.33203121885131e-12,
    "max_normwise_backward_error": 8.07438287144266e-17,
    "max_componentwise_backward_error": 1.2810265668752034e-16,
    "max_relative_LAPACK_difference": 6.180857514425556e-12,
    "max_binary64_pivot_growth": 2048.0
  },
  "checks": {
    "spd-tridiagonal-lu/finite": true,
    "spd-tridiagonal-lu/binary32-factor": true,
    "spd-tridiagonal-lu/binary64-factor": true,
    "spd-tridiagonal-lu/normwise-backward": true,
    "spd-tridiagonal-lu/componentwise-backward": true,
    "spd-tridiagonal-lu/condition-aware-forward": true,
    "spd-tridiagonal-lu/LAPACK-comparison": true,
    "spd-tridiagonal-lu/refinement-gain-or-roundoff": true,
    "spd-tridiagonal-cholesky/finite": true,
    "spd-tridiagonal-cholesky/binary32-factor": true,
    "spd-tridiagonal-cholesky/binary64-factor": true,
    "spd-tridiagonal-cholesky/normwise-backward": true,
    "spd-tridiagonal-cholesky/componentwise-backward": true,
    "spd-tridiagonal-cholesky/condition-aware-forward": true,
    "spd-tridiagonal-cholesky/LAPACK-comparison": true,
    "spd-tridiagonal-cholesky/refinement-gain-or-roundoff": true,
    "near-singular-rank-one-lu/finite": true,
    "near-singular-rank-one-lu/binary32-factor": true,
    "near-singular-rank-one-lu/binary64-factor": true,
    "near-singular-rank-one-lu/normwise-backward": true,
    "near-singular-rank-one-lu/componentwise-backward": true,
    "near-singular-rank-one-lu/condition-aware-forward": true,
    "near-singular-rank-one-lu/LAPACK-comparison": true,
    "near-singular-rank-one-lu/refinement-gain-or-roundoff": true,
    "near-singular-rank-one-cholesky/finite": true,
    "near-singular-rank-one-cholesky/binary32-factor": true,
    "near-singular-rank-one-cholesky/binary64-factor": true,
    "near-singular-rank-one-cholesky/normwise-backward": true,
    "near-singular-rank-one-cholesky/componentwise-backward": true,
    "near-singular-rank-one-cholesky/condition-aware-forward": true,
    "near-singular-rank-one-cholesky/LAPACK-comparison": true,
    "near-singular-rank-one-cholesky/refinement-gain-or-roundoff": true,
    "hilbert5-lu/finite": true,
    "hilbert5-lu/binary32-factor": true,
    "hilbert5-lu/binary64-factor": true,
    "hilbert5-lu/normwise-backward": true,
    "hilbert5-lu/componentwise-backward": true,
    "hilbert5-lu/condition-aware-forward": true,
    "hilbert5-lu/LAPACK-comparison": true,
    "hilbert5-lu/refinement-gain-or-roundoff": true,
    "hilbert5-cholesky/finite": true,
    "hilbert5-cholesky/binary32-factor": true,
    "hilbert5-cholesky/binary64-factor": true,
    "hilbert5-cholesky/normwise-backward": true,
    "hilbert5-cholesky/componentwise-backward": true,
    "hilbert5-cholesky/condition-aware-forward": true,
    "hilbert5-cholesky/LAPACK-comparison": true,
    "hilbert5-cholesky/refinement-gain-or-roundoff": true,
    "wilkinson12-lu/finite": true,
    "wilkinson12-lu/binary32-factor": true,
    "wilkinson12-lu/binary64-factor": true,
    "wilkinson12-lu/normwise-backward": true,
    "wilkinson12-lu/componentwise-backward": true,
    "wilkinson12-lu/condition-aware-forward": true,
    "wilkinson12-lu/LAPACK-comparison": true,
    "wilkinson12-lu/refinement-gain-or-roundoff": true,
    "Wilkinson/exact-growth": true,
    "Hilbert/ill-conditioning-not-residual": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/pivoted-direct-refinement/index.json

![保存した12×12 SPD行列。反復改良の固定例に使います。 別の全図に示す誤差は厳密有理数解をbinary64へ丸めた参照との差です。対数表示だけ、厳密なゼロ誤差をfloat64.tinyに置いて表示します。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/pivoted-direct-refinement-preview.png)

保存した12×12 SPD行列。反復改良の固定例に使います。 別の全図に示す誤差は厳密有理数解をbinary64へ丸めた参照との差です。対数表示だけ、厳密なゼロ誤差をfloat64.tinyに置いて表示します。

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/atlas-linear-algebra-spectral-2026-11-24-r3.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

## 出典と確認範囲

- LAPACK Users Guide: Linear Equations. https://netlib.org/lapack/lug/node38.html; review_level=selected-official-documentation
Selected LU/Cholesky, CON/RFS and same-precision refinement paragraphs were read. This example uses binary32 factors and binary64 residuals; a full LAPACK source audit is not claimed.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Pivoted LU, Cholesky and iterative refinement

Exact-rational comparisons separate conditioning, forward and backward error, and pivot growth.

**Methods used**

- [Partial-pivot LU and mixed-precision refinement](https://hrkoyama.github.io/numerical-methods-atlas/methods/lu-partial-pivoting/?lang=en) (`lu-partial-pivoting`)
- [Cholesky factorization and triangular solves](https://hrkoyama.github.io/numerical-methods-atlas/methods/cholesky/?lang=en) (`cholesky`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/pivoted-direct-refinement/?lang=en#pivoted-direct-refinement-en-algorithm)

Original implementations of LU with partial pivoting, lower Cholesky factorization and triangular substitution.

$$
PA=LU
$$

$$
A=LL^T
$$

$$
x_(j+1)=x_j+solve_factor32(b-A*x_j)
$$

- [Finite-dimensional linear systems and factorizations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#finite-dimensional-linear-system-en) (`finite-dimensional-linear-system`)

Fixed SPD matrix of size 12, a nearly singular rank-one matrix of size 8, Hilbert matrix of size 5 and Wilkinson matrix of size 12. Factors and triangular corrections use binary32; residuals use binary64, with five updates.


**Problem figure**

![Pivoted LU, Cholesky and iterative refinement: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/pivoted-direct-refinement.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Pivoted LU, Cholesky and iterative refinement](https://hrkoyama.github.io/numerical-methods-atlas/problems/pivoted-direct-refinement/?lang=en) (`pivoted-direct-refinement`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/pivoted-direct-refinement/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/pivoted-direct-refinement/?lang=en#pivoted-direct-refinement-en-validation)

Exact-rational solutions for the actual binary64 inputs and separate LAPACK DGESV/DPOSV comparisons. Conditioning, forward error and backward error are reported separately. Each saved reference component is the exact Fraction solution rounded to binary64.

- [Pivoted LU and Cholesky: exact-rational references for actual binary input](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-pivoted-direct-refinement-en) (`pivoted-direct-refinement`; Same-problem reference · Analytic reference)

Small fixed examples only; convergence of mixed-precision refinement is not guaranteed for arbitrary matrices.
## Assumptions, units and boundaries

Fixed SPD matrix of size 12, a nearly singular rank-one matrix of size 8, Hilbert matrix of size 5 and Wilkinson matrix of size 12. Factors and triangular corrections use binary32; residuals use binary64, with five updates.

**Editorial clarification**

Small fixed examples only; convergence of mixed-precision refinement is not guaranteed for arbitrary matrices.

## Adopted numerical method

Original implementations of LU with partial pivoting, lower Cholesky factorization and triangular substitution.

$$
PA=LU
$$

$$
A=LL^T
$$

$$
x_(j+1)=x_j+solve_factor32(b-A*x_j)
$$

## References and validation

Exact-rational solutions for the actual binary64 inputs and separate LAPACK DGESV/DPOSV comparisons. Conditioning, forward error and backward error are reported separately. Each saved reference component is the exact Fraction solution rounded to binary64.

## Limits

Small fixed examples only; convergence of mixed-precision refinement is not guaranteed for arbitrary matrices.

## Stored measurements and decisions

```json
{
  "metrics": {
    "max_condition_infinity": 943656.0000016841,
    "max_relative_forward_error": 7.33203121885131e-12,
    "max_normwise_backward_error": 8.07438287144266e-17,
    "max_componentwise_backward_error": 1.2810265668752034e-16,
    "max_relative_LAPACK_difference": 6.180857514425556e-12,
    "max_binary64_pivot_growth": 2048.0
  },
  "checks": {
    "spd-tridiagonal-lu/finite": true,
    "spd-tridiagonal-lu/binary32-factor": true,
    "spd-tridiagonal-lu/binary64-factor": true,
    "spd-tridiagonal-lu/normwise-backward": true,
    "spd-tridiagonal-lu/componentwise-backward": true,
    "spd-tridiagonal-lu/condition-aware-forward": true,
    "spd-tridiagonal-lu/LAPACK-comparison": true,
    "spd-tridiagonal-lu/refinement-gain-or-roundoff": true,
    "spd-tridiagonal-cholesky/finite": true,
    "spd-tridiagonal-cholesky/binary32-factor": true,
    "spd-tridiagonal-cholesky/binary64-factor": true,
    "spd-tridiagonal-cholesky/normwise-backward": true,
    "spd-tridiagonal-cholesky/componentwise-backward": true,
    "spd-tridiagonal-cholesky/condition-aware-forward": true,
    "spd-tridiagonal-cholesky/LAPACK-comparison": true,
    "spd-tridiagonal-cholesky/refinement-gain-or-roundoff": true,
    "near-singular-rank-one-lu/finite": true,
    "near-singular-rank-one-lu/binary32-factor": true,
    "near-singular-rank-one-lu/binary64-factor": true,
    "near-singular-rank-one-lu/normwise-backward": true,
    "near-singular-rank-one-lu/componentwise-backward": true,
    "near-singular-rank-one-lu/condition-aware-forward": true,
    "near-singular-rank-one-lu/LAPACK-comparison": true,
    "near-singular-rank-one-lu/refinement-gain-or-roundoff": true,
    "near-singular-rank-one-cholesky/finite": true,
    "near-singular-rank-one-cholesky/binary32-factor": true,
    "near-singular-rank-one-cholesky/binary64-factor": true,
    "near-singular-rank-one-cholesky/normwise-backward": true,
    "near-singular-rank-one-cholesky/componentwise-backward": true,
    "near-singular-rank-one-cholesky/condition-aware-forward": true,
    "near-singular-rank-one-cholesky/LAPACK-comparison": true,
    "near-singular-rank-one-cholesky/refinement-gain-or-roundoff": true,
    "hilbert5-lu/finite": true,
    "hilbert5-lu/binary32-factor": true,
    "hilbert5-lu/binary64-factor": true,
    "hilbert5-lu/normwise-backward": true,
    "hilbert5-lu/componentwise-backward": true,
    "hilbert5-lu/condition-aware-forward": true,
    "hilbert5-lu/LAPACK-comparison": true,
    "hilbert5-lu/refinement-gain-or-roundoff": true,
    "hilbert5-cholesky/finite": true,
    "hilbert5-cholesky/binary32-factor": true,
    "hilbert5-cholesky/binary64-factor": true,
    "hilbert5-cholesky/normwise-backward": true,
    "hilbert5-cholesky/componentwise-backward": true,
    "hilbert5-cholesky/condition-aware-forward": true,
    "hilbert5-cholesky/LAPACK-comparison": true,
    "hilbert5-cholesky/refinement-gain-or-roundoff": true,
    "wilkinson12-lu/finite": true,
    "wilkinson12-lu/binary32-factor": true,
    "wilkinson12-lu/binary64-factor": true,
    "wilkinson12-lu/normwise-backward": true,
    "wilkinson12-lu/componentwise-backward": true,
    "wilkinson12-lu/condition-aware-forward": true,
    "wilkinson12-lu/LAPACK-comparison": true,
    "wilkinson12-lu/refinement-gain-or-roundoff": true,
    "Wilkinson/exact-growth": true,
    "Hilbert/ill-conditioning-not-residual": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/pivoted-direct-refinement/index.json

![The saved 12 x 12 SPD matrix used in the refinement examples. In the companion full figure, errors are measured against the exact-rational solution rounded to binary64; exact zeros are shown at float64.tiny for logarithmic display only.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/pivoted-direct-refinement-preview.png)

The saved 12 x 12 SPD matrix used in the refinement examples. In the companion full figure, errors are measured against the exact-rational solution rounded to binary64; exact zeros are shown at float64.tiny for logarithmic display only.

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/atlas-linear-algebra-spectral-2026-11-24-r3.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

## Sources and review scope

- LAPACK Users Guide: Linear Equations. https://netlib.org/lapack/lug/node38.html; review_level=selected-official-documentation
Selected LU/Cholesky, CON/RFS and same-precision refinement paragraphs were read. This example uses binary32 factors and binary64 residuals; a full LAPACK source audit is not claimed.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
