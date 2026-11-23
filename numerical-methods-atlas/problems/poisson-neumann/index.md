# 純Neumannの互換条件と平均値ゲージ / Pure Neumann compatibility and mean gauge

https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-neumann/

## 日本語

[実際に保存した計算配列と固定入力の収束指標から描いた検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/poisson-neumann-preview.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-mesh-boundary/#poisson-neumann) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#poisson-neumann)

### 方程式・問題の定義

単位正方形N16/32/64、セル中心の点DOF。cos(2pi x)cos(2pi y)、全壁Neumann0、平均0とN32の平均.25診断。

#### [Poisson・Laplace方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#poisson-laplace-ja)

$$
-\nabla^2u=f
$$

$$
f=0\quad\Longrightarrow\quad\nabla^2u=0
$$

楕円型境界値問題。符号規約を確認し、反復解法・疎行列・境界条件をたどる。

#### 純Neumannの互換条件と平均値ゲージ

補助実行例 · 実行例の定義・検証式

$$
-\Delta u=f,\quad\partial_nu=g_N,\quad\int f=-\oint g_N
$$

特異な2D Poissonを互換条件と指定平均込みで解き、不適合な外力を拒否します。

### 厳密解・参照解

L2細分化、零空間、平均、CG差、source+1拒否、境界流束/体積源の収支を保存。

#### [純Neumann：解析場・互換条件・平均値ゲージ](https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-neumann/?lang=ja#poisson-neumann-ja-measurements)

製造解 · 同じ問題の参照

u=cos(2*pi*x)*cos(2*pi*y)+mean; f=8*pi^2*cos(2*pi*x)*cos(2*pi*y); dn(u)=0; integral(f)=-integral_boundary(dn(u)).

単位正方形N16/32/64、セル中心の点DOF。cos(2pi x)cos(2pi y)、全壁Neumann0、平均0とN32の平均.25診断。u=cos(2πx)cos(2πy)、f=8π²u、外向き法線流束0を点DOFで比較します。平均0と平均.25を分け、source+1の物理的不適合を投影で隠さず拒否します。

同じ半離散系の別線形解法は独立PDE参照ではありません。既存Dirichlet MGの成功や2D任意境界へ一般化しません。

#### 純Neumannの互換条件と平均値ゲージ

L2細分化、零空間、平均、CG差、source+1拒否、境界流束/体積源の収支を保存。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-neumann/?lang=ja)

### 計算法

共有面差分で特異行列を組み、体積重み平均のLagrange拘束付き疎直接法とcompatible CGを照合。物理的な不適合外力の平均を勝手に引かない。

- [空間中心差分](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [共役勾配法](https://hrkoyama.github.io/numerical-methods-atlas/methods/cg/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [純Neumannの互換条件と平均値ゲージ](https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-neumann/?lang=ja)

補助実行例

特異な2D Poissonを互換条件と指定平均込みで解き、不適合な外力を拒否します。

単位正方形N16/32/64、セル中心の点DOF。cos(2pi x)cos(2pi y)、全壁Neumann0、平均0とN32の平均.25診断。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/atlas-mesh-boundary-2026-11-23.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

同じ半離散系の別線形解法は独立PDE参照ではありません。既存Dirichlet MGの成功や2D任意境界へ一般化しません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-23/mesh-boundary/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/run.py)
- [/code/validated-examples/2026-11-23/mesh-boundary/boundary.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/boundary.py)
- [/code/validated-examples/2026-11-23/mesh-boundary/test_geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/test_geometry.py)

## English

[Validation preview from actual saved PDE arrays and fixed-input refinement measurements.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/poisson-neumann-preview.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-mesh-boundary/#poisson-neumann) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#poisson-neumann-en)

### Equations and problem definitions

Unit square N16/32/64, cell-centred point DOFs, cosine exact field, homogeneous Neumann; mean0 andN32 mean.25 probe.

#### [Poisson / Laplace equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#poisson-laplace-en)

$$
-\nabla^2u=f
$$

$$
f=0\quad\Longrightarrow\quad\nabla^2u=0
$$

Elliptic boundary-value problems: check sign conventions, iterative solvers, sparse matrices and boundaries.

#### Pure Neumann compatibility and mean gauge

Supplementary execution example · Example definition or validation formula

$$
-\Delta u=f,\quad\partial_nu=g_N,\quad\int f=-\oint g_N
$$

Solve singular2D Poisson with compatibility/gauge and reject incompatible source.

### Exact and reference solutions

Retain L2 refinement, nullspace/gauge/CG gap, source+1 rejection and boundary/source budget.

#### [Pure Neumann: analytic field, compatibility and mean gauge](https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-neumann/?lang=en#poisson-neumann-en-measurements)

Manufactured solution · Reference for the same problem

u=cos(2*pi*x)*cos(2*pi*y)+mean; f=8*pi^2*cos(2*pi*x)*cos(2*pi*y); dn(u)=0; integral(f)=-integral_boundary(dn(u)).

Unit square N16/32/64, cell-centred point DOFs, cosine exact field, homogeneous Neumann; mean0 andN32 mean.25 probe. Use point DOFs for u=cos(2pi*x)cos(2pi*y),f=8pi²u and zero outward normal flux. Distinguish means0/.25 and explicitly reject incompatible source+1 rather than projecting it away.

A different linear solver of the same matrix is not an independent PDE discretization; no general boundary/MG claim.

#### Pure Neumann compatibility and mean gauge

Retain L2 refinement, nullspace/gauge/CG gap, source+1 rejection and boundary/source budget.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-neumann/?lang=en)

### Numerical methods

Shared-face differences, weighted-mean augmented solve and compatible CG comparison; no physical RHS mean projection.

- [Centered spatial difference](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Conjugate gradients](https://hrkoyama.github.io/numerical-methods-atlas/methods/cg/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Pure Neumann compatibility and mean gauge](https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-neumann/?lang=en)

Supplementary execution example

Solve singular2D Poisson with compatibility/gauge and reject incompatible source.

Unit square N16/32/64, cell-centred point DOFs, cosine exact field, homogeneous Neumann; mean0 andN32 mean.25 probe.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/atlas-mesh-boundary-2026-11-23.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

A different linear solver of the same matrix is not an independent PDE discretization; no general boundary/MG claim.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-23/mesh-boundary/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/run.py)
- [/code/validated-examples/2026-11-23/mesh-boundary/boundary.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/boundary.py)
- [/code/validated-examples/2026-11-23/mesh-boundary/test_geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/test_geometry.py)
