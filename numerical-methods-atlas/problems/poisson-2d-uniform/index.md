# 2次元Poisson・一様ソース / 2D Poisson / uniform source

https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-uniform/

## 日本語

[保存済み一様ソースPoisson問題のマルチグリッド残差。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/poisson-2d-uniform.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/elliptic/) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#poisson-2d-uniform)

### 方程式・問題の定義

この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。

#### [Poisson・Laplace方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#poisson-laplace-ja)

$$
-\nabla^2u=f
$$

$$
f=0\quad\Longrightarrow\quad\nabla^2u=0
$$

楕円型境界値問題。符号規約を確認し、反復解法・疎行列・境界条件をたどる。

### 厳密解・参照解

一様右辺・零Dirichletの離散Poisson問題について、保存した多重格子の真の残差と、緩和法との残差低下の違いを確認します。連続厳密解との誤差照合とは区別します。

### 計算法

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

- [幾何マルチグリッドVサイクル](https://hrkoyama.github.io/numerical-methods-atlas/methods/multigrid/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

この問題の固定入力実行例は未登録です。保存結果と解説は上のリンクから確認できます。

#### [code/numerical-methods-atlas/2026-11-21/tests/test_multigrid.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_multigrid.py)

関連する既存のソース・検査。固定入力実行例とは別です。

`test_multigrid_removes_smooth_error_faster_than_relaxation`

一様右辺f=1・零Dirichlet境界の31×31離散Poisson問題で、多重格子の真の残差と、対応する回数の赤黒Gauss–Seidel緩和の残差低下を比較する既存検査です。

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

作業フォルダ：atlas-code-2026-11-21/

```sh
python -m pytest -q tests/test_multigrid.py -k test_multigrid_removes_smooth_error_faster_than_relaxation
```

## English

[Stored multigrid residual history for uniform-source Poisson.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/poisson-2d-uniform.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/elliptic/) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#poisson-2d-uniform-en)

### Equations and problem definitions

Representative equations related to this problem. See the image/problem conditions and each execution example for initial conditions, boundary conditions and parameters.

#### [Poisson / Laplace equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#poisson-laplace-en)

$$
-\nabla^2u=f
$$

$$
f=0\quad\Longrightarrow\quad\nabla^2u=0
$$

Elliptic boundary-value problems: check sign conventions, iterative solvers, sparse matrices and boundaries.

### Exact and reference solutions

For the uniform-source, zero-Dirichlet discrete Poisson problem, check stored true multigrid residuals and compare residual reduction with relaxation. Distinguish this from error against an exact continuum solution.

### Numerical methods

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

- [Geometric multigrid V-cycle](https://hrkoyama.github.io/numerical-methods-atlas/methods/multigrid/?lang=en) — Related explanation; Method-registry status: Educational example / related code

### Code and execution

No fixed-input execution example is registered for this problem. The saved visual and reading remain available above.

#### [code/numerical-methods-atlas/2026-11-21/tests/test_multigrid.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_multigrid.py)

Existing related source/check, separate from a registered fixed-input execution example.

`test_multigrid_removes_smooth_error_faster_than_relaxation`

Existing check for the 31×31 discrete Poisson problem with uniform forcing f=1 and zero Dirichlet boundaries, comparing the true multigrid residual with residual reduction after a corresponding number of red-black Gauss–Seidel sweeps.

[Corresponding code edition / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

Working directory: atlas-code-2026-11-21/

```sh
python -m pytest -q tests/test_multigrid.py -k test_multigrid_removes_smooth_error_faster_than_relaxation
```
