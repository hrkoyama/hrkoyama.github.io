# 一様平面スラブの重力 / Uniform plane-slab gravity

https://hrkoyama.github.io/numerical-methods-atlas/problems/uniform-slab/

## 日本語

[境界核の共有図。このカードは「一様平面スラブ」の問題を案内します。](https://hrkoyama.github.io/numerical-methods-atlas/assets/gravity-boundaries.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/gravity-boundaries/) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#uniform-slab)

### 方程式・問題の定義

水平周期・鉛直孤立の重力Poisson問題で、一様平板の零水平モードを扱います。下のPoisson代表式に対し、ここでの右辺は4πGρです。全方向周期境界や軟化粒子系とは区別します。

#### [Poisson・Laplace方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#poisson-laplace-ja)

$$
-\nabla^2u=f
$$

$$
f=0\quad\Longrightarrow\quad\nabla^2u=0
$$

楕円型境界値問題。符号規約を確認し、反復解法・疎行列・境界条件をたどる。

### 厳密解・参照解

一様平板のφ=2πz²を定数ゲージ調整後に比較し、加速度-4πzと零水平モードを確認します。

### 計算法

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

- [水平周期スラブGreen関数FFT](https://hrkoyama.github.io/numerical-methods-atlas/methods/slab/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

この問題の固定入力実行例は未登録です。保存結果と解説は上のリンクから確認できます。

## English

[Shared boundary-kernel figure; this card links specifically to uniform-slab.](https://hrkoyama.github.io/numerical-methods-atlas/assets/gravity-boundaries.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/gravity-boundaries/) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#uniform-slab-en)

### Equations and problem definitions

A gravitational Poisson problem periodic horizontally and isolated vertically, using the zero horizontal mode of a uniform slab. The right-hand side of the representative Poisson equation below is 4πGρ here; fully periodic boundaries and softened particle systems are different cases.

#### [Poisson / Laplace equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#poisson-laplace-en)

$$
-\nabla^2u=f
$$

$$
f=0\quad\Longrightarrow\quad\nabla^2u=0
$$

Elliptic boundary-value problems: check sign conventions, iterative solvers, sparse matrices and boundaries.

### Exact and reference solutions

Compare with φ=2πz² after aligning the additive gauge; check acceleration -4πz and the zero horizontal mode.

### Numerical methods

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

- [Horizontal-periodic slab Green-function FFT](https://hrkoyama.github.io/numerical-methods-atlas/methods/slab/?lang=en) — Related explanation; Method-registry status: Educational example / related code

### Code and execution

No fixed-input execution example is registered for this problem. The saved visual and reading remain available above.
