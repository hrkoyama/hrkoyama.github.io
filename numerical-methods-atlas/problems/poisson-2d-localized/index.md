# 2次元Poisson・局在ソース / 2D Poisson / localized source

https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-localized/

## 日本語

[保存済み局在ソースと離散Poisson解。](https://hrkoyama.github.io/numerical-methods-atlas/assets/poisson-comparison/localized-63-fields.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/elliptic/) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#poisson-2d-localized)

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

局在ソースに対する離散直接解と真の残差を基準に反復法を比較します。公開資料にこのソースの閉形式連続解は添付されていません。

### 計算法

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

- [Jacobi反復](https://hrkoyama.github.io/numerical-methods-atlas/methods/jacobi-iteration/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり
- [赤黒Gauss–Seidel法](https://hrkoyama.github.io/numerical-methods-atlas/methods/rbgs/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり
- [逐次過緩和法／SOR](https://hrkoyama.github.io/numerical-methods-atlas/methods/sor/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり
- [共役勾配法](https://hrkoyama.github.io/numerical-methods-atlas/methods/cg/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり
- [幾何マルチグリッドVサイクル](https://hrkoyama.github.io/numerical-methods-atlas/methods/multigrid/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり
- [Thomas法／三重対角消去](https://hrkoyama.github.io/numerical-methods-atlas/methods/thomas/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり
- [Fourier微分と時間発展](https://hrkoyama.github.io/numerical-methods-atlas/methods/fourier/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

この問題の固定入力実行例は未登録です。保存結果と解説は上のリンクから確認できます。

## English

[Stored localized forcing and discrete Poisson solution.](https://hrkoyama.github.io/numerical-methods-atlas/assets/poisson-comparison/localized-63-fields.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/elliptic/) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#poisson-2d-localized-en)

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

Compare iterations against a discrete direct solution and true residual for the localized source. This publication attaches no closed-form continuum solution for that source.

### Numerical methods

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

- [Jacobi iteration](https://hrkoyama.github.io/numerical-methods-atlas/methods/jacobi-iteration/?lang=en) — Related explanation; Method-registry status: Educational example / related code
- [Red-black Gauss–Seidel](https://hrkoyama.github.io/numerical-methods-atlas/methods/rbgs/?lang=en) — Related explanation; Method-registry status: Educational example / related code
- [Successive over-relaxation / SOR](https://hrkoyama.github.io/numerical-methods-atlas/methods/sor/?lang=en) — Related explanation; Method-registry status: Educational example / related code
- [Conjugate gradients](https://hrkoyama.github.io/numerical-methods-atlas/methods/cg/?lang=en) — Related explanation; Method-registry status: Educational example / related code
- [Geometric multigrid V-cycle](https://hrkoyama.github.io/numerical-methods-atlas/methods/multigrid/?lang=en) — Related explanation; Method-registry status: Educational example / related code
- [Thomas tridiagonal elimination](https://hrkoyama.github.io/numerical-methods-atlas/methods/thomas/?lang=en) — Related explanation; Method-registry status: Educational example / related code
- [Fourier differentiation and evolution](https://hrkoyama.github.io/numerical-methods-atlas/methods/fourier/?lang=en) — Related explanation; Method-registry status: Educational example / related code

### Code and execution

No fixed-input execution example is registered for this problem. The saved visual and reading remain available above.
