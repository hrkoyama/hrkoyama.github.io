# 明示的再始動Krylovと内部固有値 / Explicitly restarted Krylov and interior eigenvalues

https://hrkoyama.github.io/numerical-methods-atlas/problems/restarted-shift-invert/

## 日本語

[固有値比較に使う、保存した31×31 Dirichlet Laplacian。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/restarted-shift-invert-preview.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-linear-algebra-spectral/#restarted-shift-invert) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#restarted-shift-invert)

### 方程式・問題の定義

Dirichlet離散Laplacian31、再始動長8/16、最大40cycle、shiftなし/0/950。

#### [有限次元の行列固有値問題](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#finite-dimensional-eigenproblem-ja)

$$
A x=\lambda x
$$

主対象は31×31の固定対称行列の標準固有値問題です。行列の離散スペクトルを参照し、連続PDEの空間収束を検査したとはしません。

#### 明示的再始動Krylovと内部固有値

補助実行例 · 実行例の定義・検証式

$$
lambda_j=4(n+1)^2 sin^2(j*pi/[2(n+1)])
$$

$$
T=(A-sigma I)^-1
$$

$$
lambda=sigma+1/theta
$$

固定長の明示的再始動とshift-invertを、元の固有値問題の残差と作用回数で比較します。

### 厳密解・参照解

既知の正弦スペクトルと独立な全行列LAPACK。shift解・Krylov作用・元残差作用を別計数。

#### [再始動/shift-invert：固定離散行列の閉スペクトル](https://hrkoyama.github.io/numerical-methods-atlas/validation/restarted-shift-invert/?lang=ja#restarted-shift-invert-ja-measurements)

解析解 · 同じ問題の参照

lambda_j=4/h^2*sin(j*pi/(2*(n+1)))^2,n=31; mu=1/(lambda-sigma); lambda=sigma+1/mu

31×31 Dirichlet三重対角行列、h=1/32、再始動長8/16、shiftなし/0/950。参照はこの有限行列の固有値であり、格子細分化による連続PDE収束を認証しません。

単一対称実固有対だけ。暗黙再始動・Krylov-Schur・ロッキング・一般の非正規やクラスターは未実装。

#### 明示的再始動Krylovと内部固有値

既知の正弦スペクトルと独立な全行列LAPACK。shift解・Krylov作用・元残差作用を別計数。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/restarted-shift-invert/?lang=ja)

### 計算法

二重MGS Arnoldiを単一Ritzベクトルから明示的に再始動。自前LUでshift線形解を求め、元の固有残差で停止。

- [Krylov固有値解法](https://hrkoyama.github.io/numerical-methods-atlas/methods/eigensolvers/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [明示的再始動Krylovと内部固有値](https://hrkoyama.github.io/numerical-methods-atlas/validation/restarted-shift-invert/?lang=ja)

補助実行例

固定長の明示的再始動とshift-invertを、元の固有値問題の残差と作用回数で比較します。

Dirichlet離散Laplacian31、再始動長8/16、最大40cycle、shiftなし/0/950。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/atlas-linear-algebra-spectral-2026-11-24-r3.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

単一対称実固有対だけ。暗黙再始動・Krylov-Schur・ロッキング・一般の非正規やクラスターは未実装。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/run.py)
- [/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/test_algorithms.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/test_algorithms.py)
- [/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/test_mass_action.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/test_mass_action.py)

## English

[The saved 31 x 31 Dirichlet Laplacian used in the eigenvalue comparisons.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/restarted-shift-invert-preview.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-linear-algebra-spectral/#restarted-shift-invert) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#restarted-shift-invert-en)

### Equations and problem definitions

A fixed Dirichlet Laplacian of size 31, restart lengths 8 and 16, and at most 40 cycles. Compare the untransformed problem with shifts 0 and 950.

#### [Finite-dimensional matrix eigenproblems](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#finite-dimensional-eigenproblem-en)

$$
A x=\lambda x
$$

The primary case is a fixed 31 x 31 symmetric standard eigenproblem. Its discrete spectrum provides the reference; continuum PDE spatial convergence is not claimed.

#### Explicitly restarted Krylov and interior eigenvalues

Supplementary execution example · Example definition or validation formula

$$
lambda_j=4(n+1)^2 sin^2(j*pi/[2(n+1)])
$$

$$
T=(A-sigma I)^-1
$$

$$
lambda=sigma+1/theta
$$

Explicit restarting and shift-invert are compared using original eigenproblem residuals and counted operator actions.

### Exact and reference solutions

The known discrete sine spectrum and an independent global LAPACK comparison. Shift-solve, Krylov and original-residual actions are counted separately.

#### [Restarting and shift-invert: the closed spectrum of a fixed discrete matrix](https://hrkoyama.github.io/numerical-methods-atlas/validation/restarted-shift-invert/?lang=en#restarted-shift-invert-en-measurements)

Analytic reference · Reference for the same problem

lambda_j=4/h^2*sin(j*pi/(2*(n+1)))^2,n=31; mu=1/(lambda-sigma); lambda=sigma+1/mu

A fixed 31 x 31 Dirichlet tridiagonal matrix with h=1/32, restart lengths 8 and 16, and shifts none/0/950. The references are eigenvalues of this finite matrix, not a continuum PDE grid-convergence study.

One eigenpair of a real symmetric matrix only. No implicit restarting, Krylov-Schur, locking, or general nonnormal or clustered-spectrum capability is claimed.

#### Explicitly restarted Krylov and interior eigenvalues

The known discrete sine spectrum and an independent global LAPACK comparison. Shift-solve, Krylov and original-residual actions are counted separately.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/restarted-shift-invert/?lang=en)

### Numerical methods

Two-pass Arnoldi is explicitly restarted from one Ritz vector. Original LU routines perform the shifted solves, and stopping uses the original eigenproblem.

- [Krylov eigenvalue solvers](https://hrkoyama.github.io/numerical-methods-atlas/methods/eigensolvers/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Explicitly restarted Krylov and interior eigenvalues](https://hrkoyama.github.io/numerical-methods-atlas/validation/restarted-shift-invert/?lang=en)

Supplementary execution example

Explicit restarting and shift-invert are compared using original eigenproblem residuals and counted operator actions.

A fixed Dirichlet Laplacian of size 31, restart lengths 8 and 16, and at most 40 cycles. Compare the untransformed problem with shifts 0 and 950.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/atlas-linear-algebra-spectral-2026-11-24-r3.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

One eigenpair of a real symmetric matrix only. No implicit restarting, Krylov-Schur, locking, or general nonnormal or clustered-spectrum capability is claimed.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/run.py)
- [/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/test_algorithms.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/test_algorithms.py)
- [/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/test_mass_action.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/test_mass_action.py)
