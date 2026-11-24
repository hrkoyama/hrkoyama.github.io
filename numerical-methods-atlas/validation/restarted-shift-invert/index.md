# 明示的再始動Krylovと内部固有値

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
## 前提・単位・境界

Dirichlet離散Laplacian31、再始動長8/16、最大40cycle、shiftなし/0/950。

**編集上の補足**

単一対称実固有対だけ。暗黙再始動・Krylov-Schur・ロッキング・一般の非正規やクラスターは未実装。

## 採用した計算法

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

## 比較・検証

既知の正弦スペクトルと独立な全行列LAPACK。shift解・Krylov作用・元残差作用を別計数。

## 確認の限界

単一対称実固有対だけ。暗黙再始動・Krylov-Schur・ロッキング・一般の非正規やクラスターは未実装。

## 保存実測値と判定

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

- SLEPc EPS: projection, Krylov methods and shift-invert. https://slepc.upv.es/release/documentation/manual/eps.html; review_level=selected-official-documentation
Selected projection, Arnoldi, restarting, shift-invert and generalized-problem paragraphs were read. No SLEPc execution or Krylov-Schur reproduction is claimed.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Explicitly restarted Krylov and interior eigenvalues

Explicit restarting and shift-invert are compared using original eigenproblem residuals and counted operator actions.

**Methods used**

- [Krylov eigenvalue solvers](https://hrkoyama.github.io/numerical-methods-atlas/methods/eigensolvers/?lang=en) (`eigensolvers`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/restarted-shift-invert/?lang=en#restarted-shift-invert-en-algorithm)

Two-pass Arnoldi is explicitly restarted from one Ritz vector. Original LU routines perform the shifted solves, and stopping uses the original eigenproblem.

$$
lambda_j=4(n+1)^2 sin^2(j*pi/[2(n+1)])
$$

$$
T=(A-sigma I)^-1
$$

$$
lambda=sigma+1/theta
$$

- [Finite-dimensional matrix eigenproblems](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#finite-dimensional-eigenproblem-en) (`finite-dimensional-eigenproblem`)

A fixed Dirichlet Laplacian of size 31, restart lengths 8 and 16, and at most 40 cycles. Compare the untransformed problem with shifts 0 and 950.


**Problem figure**

![Explicitly restarted Krylov and interior eigenvalues: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/restarted-shift-invert.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Explicitly restarted Krylov and interior eigenvalues](https://hrkoyama.github.io/numerical-methods-atlas/problems/restarted-shift-invert/?lang=en) (`restarted-shift-invert`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/restarted-shift-invert/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/restarted-shift-invert/?lang=en#restarted-shift-invert-en-validation)

The known discrete sine spectrum and an independent global LAPACK comparison. Shift-solve, Krylov and original-residual actions are counted separately.

- [Restarting and shift-invert: the closed spectrum of a fixed discrete matrix](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-restarted-shift-invert-en) (`restarted-shift-invert`; Same-problem reference · Analytic reference)

One eigenpair of a real symmetric matrix only. No implicit restarting, Krylov-Schur, locking, or general nonnormal or clustered-spectrum capability is claimed.
## Assumptions, units and boundaries

A fixed Dirichlet Laplacian of size 31, restart lengths 8 and 16, and at most 40 cycles. Compare the untransformed problem with shifts 0 and 950.

**Editorial clarification**

One eigenpair of a real symmetric matrix only. No implicit restarting, Krylov-Schur, locking, or general nonnormal or clustered-spectrum capability is claimed.

## Adopted numerical method

Two-pass Arnoldi is explicitly restarted from one Ritz vector. Original LU routines perform the shifted solves, and stopping uses the original eigenproblem.

$$
lambda_j=4(n+1)^2 sin^2(j*pi/[2(n+1)])
$$

$$
T=(A-sigma I)^-1
$$

$$
lambda=sigma+1/theta
$$

## References and validation

The known discrete sine spectrum and an independent global LAPACK comparison. Shift-solve, Krylov and original-residual actions are counted separately.

## Limits

One eigenpair of a real symmetric matrix only. No implicit restarting, Krylov-Schur, locking, or general nonnormal or clustered-spectrum capability is claimed.

## Stored measurements and decisions

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

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/restarted-shift-invert/index.json

![The saved 31 x 31 Dirichlet Laplacian used in the eigenvalue comparisons.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/restarted-shift-invert-preview.png)

The saved 31 x 31 Dirichlet Laplacian used in the eigenvalue comparisons.

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

- SLEPc EPS: projection, Krylov methods and shift-invert. https://slepc.upv.es/release/documentation/manual/eps.html; review_level=selected-official-documentation
Selected projection, Arnoldi, restarting, shift-invert and generalized-problem paragraphs were read. No SLEPc execution or Krylov-Schur reproduction is claimed.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
