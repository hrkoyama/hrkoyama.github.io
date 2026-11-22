# 孤立FFTと非周期直接畳み込み / Isolated FFT versus direct nonperiodic convolution

https://hrkoyama.github.io/numerical-methods-atlas/problems/isolated-convolution/

## 日本語

[境界核の共有図。このカードは「孤立畳み込み」の問題を案内します。](https://hrkoyama.github.io/numerical-methods-atlas/assets/gravity-boundaries.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/gravity-boundaries/) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#isolated-convolution)

### 方程式・問題の定義

重力Poisson方程式の孤立境界に対応する密度場の畳み込み問題です。粒子の軟化二体力や全方向周期Poissonの例とは区別し、この図ではゼロ埋めFFTと同じ離散核の非周期直接畳み込みを照合します。

#### [Poisson・Laplace方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#poisson-laplace-ja)

$$
-\nabla^2u=f
$$

$$
f=0\quad\Longrightarrow\quad\nabla^2u=0
$$

楕円型境界値問題。符号規約を確認し、反復解法・疎行列・境界条件をたどる。

### 厳密解・参照解

同じ離散核・セル体積・自己項を使う非周期直接畳み込みと、ゼロ埋めFFTの一致を確認します。連続核の離散化誤差とは別です。

### 計算法

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

- [孤立境界の倍格子FFT畳み込み](https://hrkoyama.github.io/numerical-methods-atlas/methods/hockney/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

この問題の固定入力実行例は未登録です。保存結果と解説は上のリンクから確認できます。

#### [code/numerical-methods-atlas/2026-11-21/tests/test_gravity_boundaries.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_gravity_boundaries.py)

関連する既存のソース・検査。固定入力実行例とは別です。

`test_isolated_doubling_equals_direct_nonperiodic_discrete_convolution`

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

作業フォルダ：atlas-code-2026-11-21/

```sh
python -m pytest -q tests/test_gravity_boundaries.py -k test_isolated_doubling_equals_direct_nonperiodic_discrete_convolution
```

## English

[Shared boundary-kernel figure; this card links specifically to isolated-convolution.](https://hrkoyama.github.io/numerical-methods-atlas/assets/gravity-boundaries.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/gravity-boundaries/) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#isolated-convolution-en)

### Equations and problem definitions

A density-field convolution for the gravitational Poisson equation with isolated boundaries, distinct from softened particle-pair forces or fully periodic Poisson examples. This visual compares zero-padded FFT with nonperiodic direct convolution using the same discrete kernel.

#### [Poisson / Laplace equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#poisson-laplace-en)

$$
-\nabla^2u=f
$$

$$
f=0\quad\Longrightarrow\quad\nabla^2u=0
$$

Elliptic boundary-value problems: check sign conventions, iterative solvers, sparse matrices and boundaries.

### Exact and reference solutions

Check zero-padded FFT against nonperiodic direct convolution using the same discrete kernel, cell volumes and self term. This is separate from continuum-kernel discretization error.

### Numerical methods

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

- [Isolated doubled-grid FFT convolution](https://hrkoyama.github.io/numerical-methods-atlas/methods/hockney/?lang=en) — Related explanation; Method-registry status: Educational example / related code

### Code and execution

No fixed-input execution example is registered for this problem. The saved visual and reading remain available above.

#### [code/numerical-methods-atlas/2026-11-21/tests/test_gravity_boundaries.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_gravity_boundaries.py)

Existing related source/check, separate from a registered fixed-input execution example.

`test_isolated_doubling_equals_direct_nonperiodic_discrete_convolution`

[Corresponding code edition / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

Working directory: atlas-code-2026-11-21/

```sh
python -m pytest -q tests/test_gravity_boundaries.py -k test_isolated_doubling_equals_direct_nonperiodic_discrete_convolution
```
