# 2次元対数核のM2M・M2L・L2Lを持つFMM / 2D logarithmic FMM with M2M, M2L and L2L

https://hrkoyama.github.io/numerical-methods-atlas/problems/logarithmic-particles/

## 日本語

[固定seedの128粒子、2次元自由空間の対数核。FMMの展開次数2/4/8/12を独立した全対直接和と比べたポテンシャル・電場誤差の保存図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/fmm.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-particles/#fmm) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#logarithmic-particles)

### 方程式・問題の定義

2次元Poisson/Laplaceの対数Green核を用いる粒子和です。3次元軟化重力1/rモデルとは区別します。

#### [Poisson・Laplace方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#poisson-laplace-ja)

$$
-\nabla^2u=f
$$

$$
f=0\quad\Longrightarrow\quad\nabla^2u=0
$$

楕円型境界値問題。符号規約を確認し、反復解法・疎行列・境界条件をたどる。

#### 2次元対数核のM2M・M2L・L2Lを持つFMM

補助実行例 · 実行例の定義・検証式

$$
M_k(c)=\sum_jq_j(z_j-c)^k
$$

$$
f(z)=M_0\log(z-c)-\sum_{k=1}^p\frac{M_k}{k(z-c)^k},\qquad\phi=-\Re f
$$

自由空間の対数ポテンシャルを一様四分木の多重極・局所展開で評価し、直接和と比較します。

### 厳密解・参照解

同じ2次元対数核と粒子配置の直接和を数値基準に、多重極の次数・階層変換・力誤差を確認します。3次元1/r核の基準は流用しません。

#### 2次元対数核のM2M・M2L・L2Lを持つFMM

固定seedの128粒子で次数2・4・8・12を走査し、別の全対直接和とポテンシャル・電場の全成分を照合します。2点の符号、順序不変性、ポテンシャル微分も検査します。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm/?lang=ja)

### 計算法

この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。

- [高速多重極法の移動演算](https://hrkoyama.github.io/numerical-methods-atlas/methods/fmm/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [2次元対数核のM2M・M2L・L2Lを持つFMM](https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm/?lang=ja)

補助実行例

自由空間の対数ポテンシャルを一様四分木の多重極・局所展開で評価し、直接和と比較します。

単位正方形内の有限点電荷ですが、境界は壁でなく木を作る包囲領域です。核はphi=−sum(q log r)、電場は−grad(phi)。自己項を除外し、周期像はありません。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

3次元1/r核、適応木、周期FMM、特異積分、実測の計算量スケーリングは未検証です。2次元自由空間の教育用実装として表示します。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-22/particles/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/run.py)
- [/code/validated-examples/2026-11-22/particles/test_particles.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/test_particles.py)

## English

[Stored potential/field errors for 128 fixed-seed particles with a 2D free-space log kernel: FMM orders 2/4/8/12 versus a separate all-pairs sum.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/fmm.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-particles/#fmm) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#logarithmic-particles-en)

### Equations and problem definitions

A particle sum with the logarithmic Green kernel of 2D Poisson/Laplace, distinct from softened 3D 1/r gravity.

#### [Poisson / Laplace equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#poisson-laplace-en)

$$
-\nabla^2u=f
$$

$$
f=0\quad\Longrightarrow\quad\nabla^2u=0
$$

Elliptic boundary-value problems: check sign conventions, iterative solvers, sparse matrices and boundaries.

#### 2D logarithmic FMM with M2M, M2L and L2L

Supplementary execution example · Example definition or validation formula

$$
M_k(c)=\sum_jq_j(z_j-c)^k
$$

$$
f(z)=M_0\log(z-c)-\sum_{k=1}^p\frac{M_k}{k(z-c)^k},\qquad\phi=-\Re f
$$

Evaluate a free-space log potential with uniform-quadtree multipole and local expansions and compare with direct sums.

### Exact and reference solutions

Use direct summation with the same 2D logarithmic kernel and particles to check expansion order, hierarchical translations and force error. Do not reuse a 3D 1/r reference.

#### 2D logarithmic FMM with M2M, M2L and L2L

For 128 fixed-seed particles, sweep orders 2/4/8/12 and compare every potential/field component with a separate all-pairs calculation. Also check two-source signs, permutation invariance and potential derivatives.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm/?lang=en)

### Numerical methods

Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.

- [Fast multipole translations](https://hrkoyama.github.io/numerical-methods-atlas/methods/fmm/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [2D logarithmic FMM with M2M, M2L and L2L](https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm/?lang=en)

Supplementary execution example

Evaluate a free-space log potential with uniform-quadtree multipole and local expansions and compare with direct sums.

Particles lie in a unit-square bounding box, not a physical wall boundary. The kernel is phi=−sum(q log r), with field −grad(phi); self terms are excluded and no periodic images are used.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

No 3D 1/r kernel, adaptive tree, periodic FMM, singular quadrature or empirical complexity/scaling study. Evidence applies to this 2D free-space educational implementation.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-22/particles/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/run.py)
- [/code/validated-examples/2026-11-22/particles/test_particles.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/test_particles.py)
