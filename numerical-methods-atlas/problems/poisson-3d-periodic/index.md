# 3次元周期Poisson・Fourier製造解 / 3D periodic Poisson / Fourier manufactured solution

https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-3d-periodic/

## 日本語

[保存済み3次元周期Poisson解の3断面。3次元流体計算ではありません。](https://hrkoyama.github.io/numerical-methods-atlas/assets/field-poisson-3d.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/particle-gravity/) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#poisson-3d-periodic)

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

#### [重力粒子モデル](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#particle-gravity-ja)

$$
\boldsymbol a_i=-G\sum_{j\ne i}m_j\frac{\boldsymbol x_i-\boldsymbol x_j}{(|\boldsymbol x_i-\boldsymbol x_j|^2+\epsilon^2)^{3/2}}
$$

$$
\nabla^2\phi=4\pi G(\rho-\overline\rho)\quad\text{(periodic)}
$$

孤立系のPlummer軟化力と、周期・平均密度除去のPoisson式は異なる境界問題です。公開例は静的な力と境界核の検証で、自己重力流体の時間発展ではありません。

### 厳密解・参照解

平均密度を除いた周期Poissonの単一Fourier製造モードと比較します。格子場の検証であり、周期粒子の直接和の検証とは別です。

### 計算法

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

- [Fourier微分と時間発展](https://hrkoyama.github.io/numerical-methods-atlas/methods/fourier/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり
- [FFT粒子格子力](https://hrkoyama.github.io/numerical-methods-atlas/methods/pm/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

この問題の固定入力実行例は未登録です。保存結果と解説は上のリンクから確認できます。

## English

[Three stored slices of a 3D periodic Poisson solution, not 3D fluid evolution.](https://hrkoyama.github.io/numerical-methods-atlas/assets/field-poisson-3d.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/particle-gravity/) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#poisson-3d-periodic-en)

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

#### [Gravitational particle model](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#particle-gravity-en)

$$
\boldsymbol a_i=-G\sum_{j\ne i}m_j\frac{\boldsymbol x_i-\boldsymbol x_j}{(|\boldsymbol x_i-\boldsymbol x_j|^2+\epsilon^2)^{3/2}}
$$

$$
\nabla^2\phi=4\pi G(\rho-\overline\rho)\quad\text{(periodic)}
$$

Isolated Plummer-softened forces and periodic mean-subtracted Poisson are distinct boundary problems. Public examples check static forces and kernels, not coupled self-gravitating flow evolution.

### Exact and reference solutions

Compare against a single manufactured Fourier mode for periodic Poisson with mean density removed. This validates the mesh field rather than a periodic particle direct sum.

### Numerical methods

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

- [Fourier differentiation and evolution](https://hrkoyama.github.io/numerical-methods-atlas/methods/fourier/?lang=en) — Related explanation; Method-registry status: Educational example / related code
- [FFT particle–mesh forces](https://hrkoyama.github.io/numerical-methods-atlas/methods/pm/?lang=en) — Related explanation; Method-registry status: Educational example / related code

### Code and execution

No fixed-input execution example is registered for this problem. The saved visual and reading remain available above.
