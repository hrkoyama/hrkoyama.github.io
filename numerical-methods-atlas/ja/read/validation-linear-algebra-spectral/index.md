# 線形代数：直接法・鞍点系・再始動と整合質量固有値

小さい固定行列で、行列分解と反復改良、対称不定値の反復解法、再始動固有値解法、整合質量の弦を比較します。独立参照へ照合し、残差と解誤差・代数誤差と離散化誤差・作用回数を分けます。

共通22実行例の台帳とは別に管理する追加検証集です。配布ZIPを独立展開し、各グループの全固定入力と検査を実行した記録を示します。設定・手法・刻み幅の違いを独立した物理問題の数には加算しません。

## 部分ピボットLU・Choleskyと反復改良

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
### 前提・単位・境界

SPD12、低ランク近特異8、Hilbert5、Wilkinson12を固定。binary32因子・三角解法とbinary64残差・補正の5回です。

**編集上の補足**

小さい固定例のみ。一般の高条件数系で混合精度の収束は保証しません。

### 採用した計算法

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

### 比較・検証

実binary64入力をFraction有理数で厳密に解き、別のLAPACK DGESV/DPOSVへ照合。条件数・前進誤差・後退誤差を分離。 保存する有理数参照ベクトルは、厳密Fraction解の各成分をbinary64へ丸めたものです。

### 確認の限界

小さい固定例のみ。一般の高条件数系で混合精度の収束は保証しません。

### 保存実測値と判定

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

### 取得・実行

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

### 出典と確認範囲

- LAPACK Users Guide: Linear Equations. https://netlib.org/lapack/lug/node38.html; review_level=selected-official-documentation
Selected LU/Cholesky, CON/RFS and same-precision refinement paragraphs were read. This example uses binary32 factors and binary64 residuals; a full LAPACK source audit is not claimed.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## 対称不定値鞍点系とSchur前処理

同じ元残差の基準でMINRESとGMRESを比較し、理想Schurの三点スペクトルを検査します。

**使用手法**

- [対称不定値系の教育用MINRES](https://hrkoyama.github.io/numerical-methods-atlas/methods/minres/?lang=ja) (`minres`)
- [再始動GMRES](https://hrkoyama.github.io/numerical-methods-atlas/methods/gmres/?lang=ja) (`gmres`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/symmetric-saddle-minres/?lang=ja#symmetric-saddle-minres-ja-algorithm)

全基底保存のLanczos最小残差LSと二重MGS GMRES。SPD合同変換で対称性を保持。 元入力の残差1e-9と固定前進上限2e-8から、行列のみのκ∞推定で内部目標min(rtol,2e-8/κ∞)を導出。独立解を停止に使わない。

$$
A=[[H,B^T],[B,0]]
$$

$$
P=diag(H,BH^-1B^T)
$$

$$
A_tilde=L^-1 A L^-T
$$

- [有限次元線形方程式と行列分解](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#finite-dimensional-linear-system-ja) (`finite-dimensional-linear-system`)

速度12/24、圧力5/11の代数的混合Poisson/Stokes型ブロック。元の真の残差1e-9を共通基準にします。


**問題の図**

![対称不定値鞍点系とSchur前処理：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/symmetric-saddle-minres.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[対称不定値鞍点系とSchur前処理](https://hrkoyama.github.io/numerical-methods-atlas/problems/symmetric-saddle-minres/?lang=ja) (`symmetric-saddle-minres`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/symmetric-saddle-minres/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/symmetric-saddle-minres/?lang=ja#symmetric-saddle-minres-ja-validation)

LAPACK全系解、理想Schurの3点スペクトル、CGの明示的負曲率対照。

- [対称不定値鞍点系：独立dense解と理想Schurスペクトル](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-symmetric-saddle-minres-ja) (`symmetric-saddle-minres`; 同じ問題の参照 · 有限格子の数値参照)

理想Schurは教育用の稠密制御であり、実Stokes PDEやスケーラブルな近似前処理の完成ではありません。
### 前提・単位・境界

速度12/24、圧力5/11の代数的混合Poisson/Stokes型ブロック。元の真の残差1e-9を共通基準にします。

**編集上の補足**

理想Schurは教育用の稠密制御であり、実Stokes PDEやスケーラブルな近似前処理の完成ではありません。

### 採用した計算法

全基底保存のLanczos最小残差LSと二重MGS GMRES。SPD合同変換で対称性を保持。 元入力の残差1e-9と固定前進上限2e-8から、行列のみのκ∞推定で内部目標min(rtol,2e-8/κ∞)を導出。独立解を停止に使わない。

$$
A=[[H,B^T],[B,0]]
$$

$$
P=diag(H,BH^-1B^T)
$$

$$
A_tilde=L^-1 A L^-T
$$

### 比較・検証

LAPACK全系解、理想Schurの3点スペクトル、CGの明示的負曲率対照。

### 確認の限界

理想Schurは教育用の稠密制御であり、実Stokes PDEやスケーラブルな近似前処理の完成ではありません。

### 保存実測値と判定

```json
{
  "metrics": {
    "max_original_relative_residual": 2.340278567268362e-13,
    "max_relative_reference_error": 4.2310885906326075e-10,
    "max_iterations": 29,
    "max_condition_infinity_estimate": 5682.080194251278
  },
  "checks": {
    "n12/ideal-Schur-three-point-spectrum": true,
    "saddle-12-none-minres/finite": true,
    "saddle-12-none-minres/same-true-residual": true,
    "saddle-12-none-minres/independent-reference": true,
    "saddle-12-none-minres/basis-orthogonality": true,
    "saddle-12-none-minres/symmetric-congruence": true,
    "saddle-12-none-minres/fixed-dimension-budget": true,
    "saddle-12-none-gmres/finite": true,
    "saddle-12-none-gmres/same-true-residual": true,
    "saddle-12-none-gmres/independent-reference": true,
    "saddle-12-none-gmres/basis-orthogonality": true,
    "saddle-12-none-gmres/symmetric-congruence": true,
    "saddle-12-none-gmres/fixed-dimension-budget": true,
    "saddle-12-exact-Schur-minres/finite": true,
    "saddle-12-exact-Schur-minres/same-true-residual": true,
    "saddle-12-exact-Schur-minres/independent-reference": true,
    "saddle-12-exact-Schur-minres/basis-orthogonality": true,
    "saddle-12-exact-Schur-minres/symmetric-congruence": true,
    "saddle-12-exact-Schur-minres/fixed-dimension-budget": true,
    "saddle-12-exact-Schur-minres/ideal-three-step-control": true,
    "saddle-12-exact-Schur-gmres/finite": true,
    "saddle-12-exact-Schur-gmres/same-true-residual": true,
    "saddle-12-exact-Schur-gmres/independent-reference": true,
    "saddle-12-exact-Schur-gmres/basis-orthogonality": true,
    "saddle-12-exact-Schur-gmres/symmetric-congruence": true,
    "saddle-12-exact-Schur-gmres/fixed-dimension-budget": true,
    "saddle-12-exact-Schur-gmres/ideal-three-step-control": true,
    "n24/ideal-Schur-three-point-spectrum": true,
    "saddle-24-none-minres/finite": true,
    "saddle-24-none-minres/same-true-residual": true,
    "saddle-24-none-minres/independent-reference": true,
    "saddle-24-none-minres/basis-orthogonality": true,
    "saddle-24-none-minres/symmetric-congruence": true,
    "saddle-24-none-minres/fixed-dimension-budget": true,
    "saddle-24-none-gmres/finite": true,
    "saddle-24-none-gmres/same-true-residual": true,
    "saddle-24-none-gmres/independent-reference": true,
    "saddle-24-none-gmres/basis-orthogonality": true,
    "saddle-24-none-gmres/symmetric-congruence": true,
    "saddle-24-none-gmres/fixed-dimension-budget": true,
    "saddle-24-exact-Schur-minres/finite": true,
    "saddle-24-exact-Schur-minres/same-true-residual": true,
    "saddle-24-exact-Schur-minres/independent-reference": true,
    "saddle-24-exact-Schur-minres/basis-orthogonality": true,
    "saddle-24-exact-Schur-minres/symmetric-congruence": true,
    "saddle-24-exact-Schur-minres/fixed-dimension-budget": true,
    "saddle-24-exact-Schur-minres/ideal-three-step-control": true,
    "saddle-24-exact-Schur-gmres/finite": true,
    "saddle-24-exact-Schur-gmres/same-true-residual": true,
    "saddle-24-exact-Schur-gmres/independent-reference": true,
    "saddle-24-exact-Schur-gmres/basis-orthogonality": true,
    "saddle-24-exact-Schur-gmres/symmetric-congruence": true,
    "saddle-24-exact-Schur-gmres/fixed-dimension-budget": true,
    "saddle-24-exact-Schur-gmres/ideal-three-step-control": true,
    "CG/explicit-negative-curvature-control": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/symmetric-saddle-minres/index.json

![速度サイズ24の固定例で使う、保存した35×35鞍点行列。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/symmetric-saddle-minres-preview.png)

速度サイズ24の固定例で使う、保存した35×35鞍点行列。

### 取得・実行

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

### 出典と確認範囲

- Paige and Saunders: Stanford SOL MINRES. https://web.stanford.edu/group/SOL/software/minres/; review_level=selected-author-official-documentation
Selected discussion of symmetric indefinite systems, SPD preconditioners and the original residual was read. The original 1975 paper was not read. This stored-basis Lanczos least-squares variant is not a copy of the production short recurrence.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## 明示的再始動Krylovと内部固有値

固定長の明示的再始動とshift-invertを、元の固有値問題の残差と作用回数で比較します。

**使用手法**

- [Krylov固有値解法](https://hrkoyama.github.io/numerical-methods-atlas/methods/eigensolvers/?lang=ja) (`eigensolvers`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/restarted-shift-invert/?lang=ja#restarted-shift-invert-ja-algorithm)

二重MGS Arnoldiを単一Ritzベクトルから明示的に再始動。自前LUでshift線形解を求め、元の固有残差で停止。

$$
lambda_j=4(n+1)^2 sin^2(j*pi/[2(n+1)])
$$

$$
T=(A-sigma I)^-1
$$

$$
lambda=sigma+1/theta
$$

- [有限次元の行列固有値問題](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#finite-dimensional-eigenproblem-ja) (`finite-dimensional-eigenproblem`)

Dirichlet離散Laplacian31、再始動長8/16、最大40cycle、shiftなし/0/950。


**問題の図**

![明示的再始動Krylovと内部固有値：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/restarted-shift-invert.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[明示的再始動Krylovと内部固有値](https://hrkoyama.github.io/numerical-methods-atlas/problems/restarted-shift-invert/?lang=ja) (`restarted-shift-invert`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/restarted-shift-invert/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/restarted-shift-invert/?lang=ja#restarted-shift-invert-ja-validation)

既知の正弦スペクトルと独立な全行列LAPACK。shift解・Krylov作用・元残差作用を別計数。

- [再始動/shift-invert：固定離散行列の閉スペクトル](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-restarted-shift-invert-ja) (`restarted-shift-invert`; 同じ問題の参照 · 解析参照)

単一対称実固有対だけ。暗黙再始動・Krylov-Schur・ロッキング・一般の非正規やクラスターは未実装。
### 前提・単位・境界

Dirichlet離散Laplacian31、再始動長8/16、最大40cycle、shiftなし/0/950。

**編集上の補足**

単一対称実固有対だけ。暗黙再始動・Krylov-Schur・ロッキング・一般の非正規やクラスターは未実装。

### 採用した計算法

二重MGS Arnoldiを単一Ritzベクトルから明示的に再始動。自前LUでshift線形解を求め、元の固有残差で停止。

$$
lambda_j=4(n+1)^2 sin^2(j*pi/[2(n+1)])
$$

$$
T=(A-sigma I)^-1
$$

$$
lambda=sigma+1/theta
$$

### 比較・検証

既知の正弦スペクトルと独立な全行列LAPACK。shift解・Krylov作用・元残差作用を別計数。

### 確認の限界

単一対称実固有対だけ。暗黙再始動・Krylov-Schur・ロッキング・一般の非正規やクラスターは未実装。

### 保存実測値と判定

```json
{
  "metrics": {
    "max_original_eigenpair_residual": 5.774117289151498e-10,
    "max_operator_calls": 216,
    "max_restart_cycles": 27,
    "max_shift_solve_count": 16
  },
  "checks": {
    "restart-8-shift-None/finite": true,
    "restart-8-shift-None/original-problem-residual": true,
    "restart-8-shift-None/known-spectrum": true,
    "restart-8-shift-None/shift-linear-residual": true,
    "restart-8-shift-None/action-budget": true,
    "restart-8-shift-None/basis-orthogonality": true,
    "restart-8-shift-None/inverse-spectral-map": true,
    "restart-16-shift-None/finite": true,
    "restart-16-shift-None/original-problem-residual": true,
    "restart-16-shift-None/known-spectrum": true,
    "restart-16-shift-None/shift-linear-residual": true,
    "restart-16-shift-None/action-budget": true,
    "restart-16-shift-None/basis-orthogonality": true,
    "restart-16-shift-None/inverse-spectral-map": true,
    "restart-8-shift-0.0/finite": true,
    "restart-8-shift-0.0/original-problem-residual": true,
    "restart-8-shift-0.0/known-spectrum": true,
    "restart-8-shift-0.0/shift-linear-residual": true,
    "restart-8-shift-0.0/action-budget": true,
    "restart-8-shift-0.0/basis-orthogonality": true,
    "restart-8-shift-0.0/inverse-spectral-map": true,
    "restart-16-shift-0.0/finite": true,
    "restart-16-shift-0.0/original-problem-residual": true,
    "restart-16-shift-0.0/known-spectrum": true,
    "restart-16-shift-0.0/shift-linear-residual": true,
    "restart-16-shift-0.0/action-budget": true,
    "restart-16-shift-0.0/basis-orthogonality": true,
    "restart-16-shift-0.0/inverse-spectral-map": true,
    "restart-8-shift-950.0/finite": true,
    "restart-8-shift-950.0/original-problem-residual": true,
    "restart-8-shift-950.0/known-spectrum": true,
    "restart-8-shift-950.0/shift-linear-residual": true,
    "restart-8-shift-950.0/action-budget": true,
    "restart-8-shift-950.0/basis-orthogonality": true,
    "restart-8-shift-950.0/inverse-spectral-map": true,
    "restart-16-shift-950.0/finite": true,
    "restart-16-shift-950.0/original-problem-residual": true,
    "restart-16-shift-950.0/known-spectrum": true,
    "restart-16-shift-950.0/shift-linear-residual": true,
    "restart-16-shift-950.0/action-budget": true,
    "restart-16-shift-950.0/basis-orthogonality": true,
    "restart-16-shift-950.0/inverse-spectral-map": true,
    "shift/exact-singularity-failure-retained-as-control": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/restarted-shift-invert/index.json

![固有値比較に使う、保存した31×31 Dirichlet Laplacian。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/restarted-shift-invert-preview.png)

固有値比較に使う、保存した31×31 Dirichlet Laplacian。

### 取得・実行

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

### 出典と確認範囲

- SLEPc EPS: projection, Krylov methods and shift-invert. https://slepc.upv.es/release/documentation/manual/eps.html; review_level=selected-official-documentation
Selected projection, Arnoldi, restarting, shift-invert and generalized-problem paragraphs were read. No SLEPc execution or Krylov-Schur reproduction is claimed.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## 整合質量FEM弦の一般化固有値

整合質量のP1弦で、M内積Krylovと実際のSciPy LOBPCGを独立離散スペクトルへ照合します。

**使用手法**

- [Krylov固有値解法](https://hrkoyama.github.io/numerical-methods-atlas/methods/eigensolvers/?lang=ja) (`eigensolvers`)
- [SciPy LOBPCGによる一般化固有値比較](https://hrkoyama.github.io/numerical-methods-atlas/methods/lobpcg/?lang=ja) (`lobpcg`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/fem-mass-eigen/?lang=ja#fem-mass-eigen-ja-algorithm)

要素からK,Mを組み立て、M内積のK^-1M KrylovとSciPy LOBPCGを比較。小規模な厳密K逆前処理。 LOBPCG初期列は{1,x³,x⁶}。K逆Mの次数+2像を初期spanから独立にし、{1,x,x²}の構造的階数欠落を避ける。 同じMの作用を資格済einsumのLinearOperatorで与え、dense-B adapterを通さない。固有値solver自体はSciPy LOBPCG。

$$
K x=lambda M x
$$

$$
lambda_j,h=6(1-cos(theta_j))/[h^2(2+cos(theta_j))]
$$

$$
X^T M X=I
$$

- [固定端弦の固有値と整合質量FEM](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#dirichlet-string-eigenproblem-ja) (`dirichlet-string-eigenproblem`)

単位弦・張力密度1、同次Dirichlet、内部15/31/63点、最低3固有対。


**問題の図**

![整合質量FEM弦の一般化固有値：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/fem-mass-eigen.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[整合質量FEM弦の一般化固有値](https://hrkoyama.github.io/numerical-methods-atlas/problems/fem-mass-eigen/?lang=ja) (`fem-mass-eigen`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/fem-mass-eigen/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/fem-mass-eigen/?lang=ja#fem-mass-eigen-ja-validation)

一般化dense eigh、独立離散スペクトル、連続体(jπ)^2への細分化。M直交性と元残差は別量。

- [P1整合質量弦：閉離散固有値と連続体固有値](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-fem-mass-eigen-ja) (`fem-mass-eigen`; 同じ問題の参照 · 解析参照)

小規模1D弦のみ。SciPyが返す前の例外では入力を保存し、未返却の内部反復を保存したとはしません。 成分資格35判定は4科学例の合格を代用せず、元SciPy内部の未返却反復は保存済みとしません。
### 前提・単位・境界

単位弦・張力密度1、同次Dirichlet、内部15/31/63点、最低3固有対。

**編集上の補足**

小規模1D弦のみ。SciPyが返す前の例外では入力を保存し、未返却の内部反復を保存したとはしません。 成分資格35判定は4科学例の合格を代用せず、元SciPy内部の未返却反復は保存済みとしません。

### 採用した計算法

要素からK,Mを組み立て、M内積のK^-1M KrylovとSciPy LOBPCGを比較。小規模な厳密K逆前処理。 LOBPCG初期列は{1,x³,x⁶}。K逆Mの次数+2像を初期spanから独立にし、{1,x,x²}の構造的階数欠落を避ける。 同じMの作用を資格済einsumのLinearOperatorで与え、dense-B adapterを通さない。固有値solver自体はSciPy LOBPCG。

$$
K x=lambda M x
$$

$$
lambda_j,h=6(1-cos(theta_j))/[h^2(2+cos(theta_j))]
$$

$$
X^T M X=I
$$

### 比較・検証

一般化dense eigh、独立離散スペクトル、連続体(jπ)^2への細分化。M直交性と元残差は別量。

### 確認の限界

小規模1D弦のみ。SciPyが返す前の例外では入力を保存し、未返却の内部反復を保存したとはしません。 成分資格35判定は4科学例の合格を代用せず、元SciPy内部の未返却反復は保存済みとしません。

### 保存実測値と判定

```json
{
  "metrics": {
    "max_generalized_residual": 1.94948028233657e-10,
    "max_M_orthogonality_defect": 1.1102230246251565e-15,
    "max_relative_reference_error": 1.5843735459579712e-13,
    "max_operator_vector_actions": 30,
    "max_preconditioner_vector_actions": 24
  },
  "checks": {
    "fem-15-mass-Krylov/finite": true,
    "fem-15-mass-Krylov/original-generalized-residual": true,
    "fem-15-mass-Krylov/M-orthogonality": true,
    "fem-15-mass-Krylov/independent-dense-reference": true,
    "fem-15-mass-Krylov/exact-discrete-spectrum": true,
    "fem-15-mass-Krylov/fixed-action-budget": true,
    "fem-15-SciPy-LOBPCG/finite": true,
    "fem-15-SciPy-LOBPCG/original-generalized-residual": true,
    "fem-15-SciPy-LOBPCG/M-orthogonality": true,
    "fem-15-SciPy-LOBPCG/independent-dense-reference": true,
    "fem-15-SciPy-LOBPCG/exact-discrete-spectrum": true,
    "fem-15-SciPy-LOBPCG/fixed-action-budget": true,
    "fem-31-mass-Krylov/finite": true,
    "fem-31-mass-Krylov/original-generalized-residual": true,
    "fem-31-mass-Krylov/M-orthogonality": true,
    "fem-31-mass-Krylov/independent-dense-reference": true,
    "fem-31-mass-Krylov/exact-discrete-spectrum": true,
    "fem-31-mass-Krylov/fixed-action-budget": true,
    "fem-31-SciPy-LOBPCG/finite": true,
    "fem-31-SciPy-LOBPCG/original-generalized-residual": true,
    "fem-31-SciPy-LOBPCG/M-orthogonality": true,
    "fem-31-SciPy-LOBPCG/independent-dense-reference": true,
    "fem-31-SciPy-LOBPCG/exact-discrete-spectrum": true,
    "fem-31-SciPy-LOBPCG/fixed-action-budget": true,
    "fem-63-mass-Krylov/finite": true,
    "fem-63-mass-Krylov/original-generalized-residual": true,
    "fem-63-mass-Krylov/M-orthogonality": true,
    "fem-63-mass-Krylov/independent-dense-reference": true,
    "fem-63-mass-Krylov/exact-discrete-spectrum": true,
    "fem-63-mass-Krylov/fixed-action-budget": true,
    "fem-63-SciPy-LOBPCG/finite": true,
    "fem-63-SciPy-LOBPCG/original-generalized-residual": true,
    "fem-63-SciPy-LOBPCG/M-orthogonality": true,
    "fem-63-SciPy-LOBPCG/independent-dense-reference": true,
    "fem-63-SciPy-LOBPCG/exact-discrete-spectrum": true,
    "fem-63-SciPy-LOBPCG/fixed-action-budget": true,
    "continuum/second-order-ratio-1": true,
    "continuum/second-order-ratio-2": true,
    "continuum/finest-three-eigenvalues": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/fem-mass-eigen/index.json

![内部63点で計算した、M正規化された最低3モード。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/fem-mass-eigen-preview.png)

内部63点で計算した、M正規化された最低3モード。

### 取得・実行

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

### 出典と確認範囲

- SLEPc EPS: projection, Krylov methods and shift-invert. https://slepc.upv.es/release/documentation/manual/eps.html; review_level=selected-official-documentation
Selected projection, Arnoldi, restarting, shift-invert and generalized-problem paragraphs were read. No SLEPc execution or Krylov-Schur reproduction is claimed.

- SciPy 1.14.1 LOBPCG API. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.sparse.linalg.lobpcg.html; review_level=selected-official-documentation
Selected discussion of SPD B, preconditioner M, the history tuple, the 3k eigensolve, the 5k > n fallback and the rod example was read. This maintained-library comparison shares reduced LAPACK primitives; LOBPCG is not independently authored here.

- SciPy 1.14.1 LOBPCG adapter and initial B-orthonormalization. https://raw.githubusercontent.com/scipy/scipy/v1.14.1/scipy/sparse/linalg/_eigen/lobpcg/lobpcg.py; review_level=selected-official-source
Selected _makeMatMat, _b_orthonormalize and API lines were read. The installed pinned file is bound separately. No full reading of the original LOBPCG paper or byte equality between wheel and Web source formatting is claimed.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
