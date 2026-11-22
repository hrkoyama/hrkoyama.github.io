# 1次元Poisson・Robin境界の製造解 / 1D Poisson / Robin manufactured solutions

https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-robin/

## 日本語

[公開コード版を固定条件で実行して作成した計算結果。条件・値・検査結果を添付。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/poisson-1d-robin.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/elliptic/) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#poisson-1d-robin)

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

f=-exp(x)と指定Robin係数を満たすu=exp(x)が製造解です。境界処理を含む2次収束を確認します。

#### [Poisson／正弦波の製造解](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=poisson-manufactured)

製造解 · 関連モデルの参照

u = sin(πx); −u_xx = f = π² sin(πx)

両端はゼロDirichlet条件。目標解から外力を選ぶ製造解であり、任意の外力のPoisson解ではありません。

参照カードは零Dirichletの正弦解、こちらはRobin境界のexp(x)です。

### 計算法

公開のRobin境界Poisson検査で使うThomas消去です。

- [Thomas法／三重対角消去](https://hrkoyama.github.io/numerical-methods-atlas/methods/thomas/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

この問題の固定入力実行例は未登録です。保存結果と解説は上のリンクから確認できます。

#### [code/numerical-methods-atlas/2026-11-21/tests/test_linear.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_linear.py)

関連する既存のソース・検査。固定入力実行例とは別です。

`test_robin_second_order_with_manufactured_exponential`

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

作業フォルダ：atlas-code-2026-11-21/

```sh
python -m pytest -q tests/test_linear.py -k test_robin_second_order_with_manufactured_exponential
```

## English

[Calculated from the public code edition with fixed inputs; inputs, values and checks are linked.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/poisson-1d-robin.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/elliptic/) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#poisson-1d-robin-en)

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

Use the manufactured solution u=exp(x) for f=-exp(x) and the specified Robin coefficients; check second-order convergence including boundary treatment.

#### [Poisson / manufactured sine](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=poisson-manufactured)

Manufactured solution · Related-model reference

u = sin(πx); −u_xx = f = π² sin(πx)

Zero Dirichlet endpoints. The forcing is chosen from the target solution; this is not an arbitrary-source Poisson solution.

The card is a zero-Dirichlet sine solution; this test uses Robin boundaries and exp(x).

### Numerical methods

Thomas elimination used by the public Robin-boundary Poisson check.

- [Thomas tridiagonal elimination](https://hrkoyama.github.io/numerical-methods-atlas/methods/thomas/?lang=en) — Related explanation; Method-registry status: Educational example / related code

### Code and execution

No fixed-input execution example is registered for this problem. The saved visual and reading remain available above.

#### [code/numerical-methods-atlas/2026-11-21/tests/test_linear.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_linear.py)

Existing related source/check, separate from a registered fixed-input execution example.

`test_robin_second_order_with_manufactured_exponential`

[Corresponding code edition / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

Working directory: atlas-code-2026-11-21/

```sh
python -m pytest -q tests/test_linear.py -k test_robin_second_order_with_manufactured_exponential
```
