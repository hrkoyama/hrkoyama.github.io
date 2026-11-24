# 1次元Poisson・Dirichlet製造解 / 1D Poisson / smooth Dirichlet manufactured solutions

https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-dirichlet/

## 日本語

[保存済み1次元Dirichlet製造解の誤差と格子数。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/poisson-1d-dirichlet.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/elliptic/) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#poisson-1d-dirichlet)

### 方程式・問題の定義

無次元区間[0,1]で −uₓₓ=π²sin(πx)、u(0)=u(1)=0。中間層16素子・49実パラメータ、固定seed 8401–8403、学習64点と独立評価257点を用います。

#### [Poisson・Laplace方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#poisson-laplace-ja)

$$
-\nabla^2u=f
$$

$$
f=0\quad\Longrightarrow\quad\nabla^2u=0
$$

楕円型境界値問題。符号規約を確認し、反復解法・疎行列・境界条件をたどる。

#### 1次元Poisson：Dirichlet正弦解と2次収束

共通実行例 · 問題の式

$$
-u''(x)=\pi^2\sin(\pi x),\qquad u(0)=u(1)=0
$$

$$
u_{\rm ref}(x)=\sin(\pi x)
$$

一様格子の3点差分を15/31/63内部点で解く。残差が小さいことと連続解に近いことは別々に判定する。

#### 1D Poisson PINNと独立格子誤差

補助実行例 · 実行例の定義・検証式

$$
-u_{xx}=\pi^2\sin(\pi x),\quad 0<x<1,\quad u(0)=u(1)=0
$$

$$
u_\theta(x)=x(1-x)\left[b_0+\sum_{j=1}^{16}a_j\tanh(w_jx+b_j)\right]
$$

$$
r_i=\frac{-u_{\theta,xx}(x_i)-\pi^2\sin(\pi x_i)}{\pi^2},\quad L=\frac1{64}\sum_{i=1}^{64}r_i^2
$$

3固定seedの49パラメータPINNを解析解・FDと比較します。

### 厳密解・参照解

零Dirichlet境界の製造正弦解、複合正弦の比較例、および離散残差で確認します。単一sin(πx)の参照カードが全ソース条件を表すわけではありません。 全49列の残差Jacobianと損失勾配、空間微分を別資格段階で独立照合。解析解sin(πx)に対する独立点誤差、PDE残差、境界値、FD誤差を別に保存します。収束・精度目標の実際の真偽を残し、正常な予算終了を収束と呼びません。

#### [Poisson／正弦波の製造解](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=poisson-manufactured)

製造解 · 関連モデルの参照

u = sin(πx); −u_xx = f = π² sin(πx)

両端はゼロDirichlet条件。目標解から外力を選ぶ製造解であり、任意の外力のPoisson解ではありません。

単一sin(πx)の共通固定入力とは一致しますが、保存比較図は複合正弦製造解も含みます。同じ零Dirichletでも全ソースが同一ではありません。

#### [1D Poisson PINNと独立格子誤差](https://hrkoyama.github.io/numerical-methods-atlas/validation/pinn-poisson/?lang=ja#pinn-poisson-ja-measurements)

製造解 · 関連モデルの参照

u_{\rm exact}(x)=\sin(\pi x);\quad -u_{xx}=\pi^2\sin(\pi x),\quad 0<x<1,\quad u(0)=u(1)=0;\quad u_\theta(x)=x(1-x)\left[b_0+\sum_{j=1}^{16}a_j\tanh(w_jx+b_j)\right];\quad r_i=\frac{-u_{\theta,xx}(x_i)-\pi^2\sin(\pi x_i)}{\pi^2},\quad L=\frac1{64}\sum_{i=1}^{64}r_i^2

無次元区間[0,1]で −uₓₓ=π²sin(πx)、u(0)=u(1)=0。中間層16素子・49実パラメータ、固定seed 8401–8403、学習64点と独立評価257点を用います。

1つの滑らかなPoisson問題と3seedの固定予算実験です。小さい学習損失だけで独立点精度の達成や一般的なPINN学習成功を保証しません。未達目標も表示します。

#### 1次元Poisson：Dirichlet正弦解と2次収束

CSVは最細格子でx・数値解・解析解・誤差を整列。全3格子の誤差と残差、隣接格子間の次数はresult.jsonに保存。Thomasの原報告は既存台帳でも直接確認未済のため、未検証の一次文献を新たに掲げない。

- [CSVは最細格子でx・数値解・解析解・誤差を整列。全3格子の誤差と残差、隣接格子間の次数はresult.jsonに保存。Thomasの原報告は既存台帳でも直接確認未済のため、未検証の一次文献を新たに掲げない。](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/poisson-1d-dirichlet/result.json)
- [独立にsin(πx)と右辺を評価する。小残差と連続解誤差は分けて報告する。](https://hrkoyama.github.io/numerical-methods-atlas/en/read/elliptic/)
- [保存結果](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/poisson-1d-dirichlet/result.json)
- [保存結果](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/poisson-1d-dirichlet/solution.csv)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/poisson-1d-dirichlet/?lang=ja)

#### 1D Poisson PINNと独立格子誤差

全49列の残差Jacobianと損失勾配、空間微分を別資格段階で独立照合。解析解sin(πx)に対する独立点誤差、PDE残差、境界値、FD誤差を別に保存します。収束・精度目標の実際の真偽を残し、正常な予算終了を収束と呼びません。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/pinn-poisson/?lang=ja)

### 計算法

この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。 x(1−x)を掛けて境界値を厳密に組み込むtanhネットワークを、解析的な全パラメータJacobian付きTRF最小二乗法で学習します。固定予算後の全モデルを保存し、31/63/127未知数の2次中心差分とThomas法も計算します。

- [Thomas法／三重対角消去](https://hrkoyama.github.io/numerical-methods-atlas/methods/thomas/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [PINN・ニューラル演算子](https://hrkoyama.github.io/numerical-methods-atlas/methods/pinn-operators/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [1次元Poisson：Dirichlet正弦解と2次収束](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/poisson-1d-dirichlet/?lang=ja)

共通実行例

既存Thomas解法で −u''=π²sin(πx) を15/31/63内部点で解き、解析解sin(πx)、独立な差分残差、格子幅半減の次数を別々に確認する。

定係数・一様格子の3点差分。入力で領域、境界、右辺、格子、解法を固定。ピボットなしThomasに適した正定値三重対角行列で、任意の三重対角行列を検証するものではない。

[コード / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip) · [検証記録](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

[固定入力](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/recipes/poisson-1d-dirichlet.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python run_recipe.py --input recipes/poisson-1d-dirichlet.json --output output-poisson-1d-dirichlet
python -m pytest -q tests/test_recipes.py
```

非零境界、別の右辺、異なる領域や不正格子を拒否。有限差分の滑らかな単一解の検査で、Robin/Neumann、可変係数、ピボットの一般的安全性を保証しない。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/numerical-methods-atlas/2026-11-22/run_recipe.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/run_recipe.py)
- [/code/numerical-methods-atlas/2026-11-22/tests/test_recipes.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/tests/test_recipes.py)

#### [1D Poisson PINNと独立格子誤差](https://hrkoyama.github.io/numerical-methods-atlas/validation/pinn-poisson/?lang=ja)

補助実行例

3固定seedの49パラメータPINNを解析解・FDと比較します。

無次元区間[0,1]で −uₓₓ=π²sin(πx)、u(0)=u(1)=0。中間層16素子・49実パラメータ、固定seed 8401–8403、学習64点と独立評価257点を用います。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/atlas-small-models-2026-11-25.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

1つの滑らかなPoisson問題と3seedの固定予算実験です。小さい学習損失だけで独立点精度の達成や一般的なPINN学習成功を保証しません。未達目標も表示します。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-25/small-models/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/run.py)
- [/code/validated-examples/2026-11-25/small-models/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/experiments.py)
- [/code/validated-examples/2026-11-25/small-models/io_utils.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/io_utils.py)
- [/code/validated-examples/2026-11-25/small-models/pinn.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/pinn.py)
- [/code/validated-examples/2026-11-25/small-models/test_models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/test_models.py)

#### [code/numerical-methods-atlas/2026-11-21/tests/test_linear.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_linear.py)

関連する既存のソース・検査。固定入力実行例とは別です。

`test_poisson_second_order`

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

作業フォルダ：atlas-code-2026-11-21/

```sh
python -m pytest -q tests/test_linear.py -k test_poisson_second_order
```

## English

[Stored error versus resolution for the 1D Dirichlet manufactured solution.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/poisson-1d-dirichlet.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/elliptic/) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#poisson-1d-dirichlet-en)

### Equations and problem definitions

Solve dimensionless −uₓₓ=π² sin(πx) on [0,1] with zero Dirichlet data. Use sixteen hidden units, 49 real parameters, seeds 8401–8403, 64 training points and 257 separate evaluation points.

#### [Poisson / Laplace equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#poisson-laplace-en)

$$
-\nabla^2u=f
$$

$$
f=0\quad\Longrightarrow\quad\nabla^2u=0
$$

Elliptic boundary-value problems: check sign conventions, iterative solvers, sparse matrices and boundaries.

#### 1D Poisson: Dirichlet sine solution and second-order refinement

Common execution example · Problem definition

$$
-u''(x)=\pi^2\sin(\pi x),\qquad u(0)=u(1)=0
$$

$$
u_{\rm ref}(x)=\sin(\pi x)
$$

Three-point differences on 15/31/63 uniform interior nodes; a small residual and proximity to the continuous solution are separate checks.

#### Poisson PINN: independent grid error

Supplementary execution example · Example definition or validation formula

$$
-u_{xx}=\pi^2\sin(\pi x),\quad 0<x<1,\quad u(0)=u(1)=0
$$

$$
u_\theta(x)=x(1-x)\left[b_0+\sum_{j=1}^{16}a_j\tanh(w_jx+b_j)\right]
$$

$$
r_i=\frac{-u_{\theta,xx}(x_i)-\pi^2\sin(\pi x_i)}{\pi^2},\quad L=\frac1{64}\sum_{i=1}^{64}r_i^2
$$

Compare a 49-parameter PINN for three fixed seeds with analytic and finite-difference solutions.

### Exact and reference solutions

Use manufactured sine solutions, the composite-sine comparison and discrete residuals with zero Dirichlet endpoints. The single sin(πx) reference does not represent every forcing variant. Independently qualify all 49 residual-Jacobian columns, loss-gradient coordinates and spatial derivatives. Save off-training solution error against sin(πx), PDE residual, boundary error and finite-difference error separately. Preserve actual convergence and accuracy decisions; a normal budget return is not convergence.

#### [Poisson / manufactured sine](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=poisson-manufactured)

Manufactured solution · Related-model reference

u = sin(πx); −u_xx = f = π² sin(πx)

Zero Dirichlet endpoints. The forcing is chosen from the target solution; this is not an arbitrary-source Poisson solution.

It matches the single-sine common fixed input, but saved comparisons also contain composite-sine manufactured forcing. Zero Dirichlet boundaries do not make all sources identical.

#### [Poisson PINN: independent grid error](https://hrkoyama.github.io/numerical-methods-atlas/validation/pinn-poisson/?lang=en#pinn-poisson-en-measurements)

Manufactured solution · Related-model reference

u_{\rm exact}(x)=\sin(\pi x);\quad -u_{xx}=\pi^2\sin(\pi x),\quad 0<x<1,\quad u(0)=u(1)=0;\quad u_\theta(x)=x(1-x)\left[b_0+\sum_{j=1}^{16}a_j\tanh(w_jx+b_j)\right];\quad r_i=\frac{-u_{\theta,xx}(x_i)-\pi^2\sin(\pi x_i)}{\pi^2},\quad L=\frac1{64}\sum_{i=1}^{64}r_i^2

Solve dimensionless −uₓₓ=π² sin(πx) on [0,1] with zero Dirichlet data. Use sixteen hidden units, 49 real parameters, seeds 8401–8403, 64 training points and 257 separate evaluation points.

This fixed-budget study covers one smooth Poisson problem and three seeds. A small training loss does not establish independent-point accuracy or general PINN training success. Unmet goals remain visible.

#### 1D Poisson: Dirichlet sine solution and second-order refinement

CSV aligns finest-grid x, numerical/analytic values and error. JSON retains all three errors/residuals and adjacent-level orders. The Thomas original report remains unverified in the existing catalog, so no newly verified primary-source claim is added.

- [CSV aligns finest-grid x, numerical/analytic values and error. JSON retains all three errors/residuals and adjacent-level orders. The Thomas original report remains unverified in the existing catalog, so no newly verified primary-source claim is added.](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/poisson-1d-dirichlet/result.json)
- [Evaluate sin(πx) and its forcing independently; report continuous-solution error separately from a small discrete residual.](https://hrkoyama.github.io/numerical-methods-atlas/en/read/elliptic/)
- [Saved result](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/poisson-1d-dirichlet/result.json)
- [Saved result](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/poisson-1d-dirichlet/solution.csv)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/poisson-1d-dirichlet/?lang=en)

#### Poisson PINN: independent grid error

Independently qualify all 49 residual-Jacobian columns, loss-gradient coordinates and spatial derivatives. Save off-training solution error against sin(πx), PDE residual, boundary error and finite-difference error separately. Preserve actual convergence and accuracy decisions; a normal budget return is not convergence.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/pinn-poisson/?lang=en)

### Numerical methods

Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions. Train a hard-boundary tanh ansatz with trust-region reflective least squares and an analytic parameter Jacobian. Retain every returned model under the fixed budget. Also solve second-order finite differences with 31, 63 and 127 unknowns using the Thomas algorithm.

- [Thomas tridiagonal elimination](https://hrkoyama.github.io/numerical-methods-atlas/methods/thomas/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [PINNs and neural operators](https://hrkoyama.github.io/numerical-methods-atlas/methods/pinn-operators/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [1D Poisson: Dirichlet sine solution and second-order refinement](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/poisson-1d-dirichlet/?lang=en)

Common execution example

Use the existing Thomas kernel for −u''=π²sin(πx) with 15/31/63 interior nodes; separately check analytic sin(πx), a recomputed discrete residual and halving-grid refinement.

Constant-coefficient three-point differences on a uniform mesh. Inputs fix domain, boundaries, forcing, grids and solver. The SPD tridiagonal system suits unpivoted Thomas; this does not validate arbitrary tridiagonal matrices.

[Code / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip) · [Verification receipt](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

[Fixed input](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/recipes/poisson-1d-dirichlet.json)

[File manifest and hashes](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python run_recipe.py --input recipes/poisson-1d-dirichlet.json --output output-poisson-1d-dirichlet
python -m pytest -q tests/test_recipes.py
```

Reject different forcing/domain, nonzero boundaries and invalid meshes. This smooth finite-difference case does not validate Robin/Neumann data, variable coefficients or general pivot safety.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/numerical-methods-atlas/2026-11-22/run_recipe.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/run_recipe.py)
- [/code/numerical-methods-atlas/2026-11-22/tests/test_recipes.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/tests/test_recipes.py)

#### [Poisson PINN: independent grid error](https://hrkoyama.github.io/numerical-methods-atlas/validation/pinn-poisson/?lang=en)

Supplementary execution example

Compare a 49-parameter PINN for three fixed seeds with analytic and finite-difference solutions.

Solve dimensionless −uₓₓ=π² sin(πx) on [0,1] with zero Dirichlet data. Use sixteen hidden units, 49 real parameters, seeds 8401–8403, 64 training points and 257 separate evaluation points.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/atlas-small-models-2026-11-25.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This fixed-budget study covers one smooth Poisson problem and three seeds. A small training loss does not establish independent-point accuracy or general PINN training success. Unmet goals remain visible.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-25/small-models/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/run.py)
- [/code/validated-examples/2026-11-25/small-models/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/experiments.py)
- [/code/validated-examples/2026-11-25/small-models/io_utils.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/io_utils.py)
- [/code/validated-examples/2026-11-25/small-models/pinn.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/pinn.py)
- [/code/validated-examples/2026-11-25/small-models/test_models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/test_models.py)

#### [code/numerical-methods-atlas/2026-11-21/tests/test_linear.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_linear.py)

Existing related source/check, separate from a registered fixed-input execution example.

`test_poisson_second_order`

[Corresponding code edition / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

Working directory: atlas-code-2026-11-21/

```sh
python -m pytest -q tests/test_linear.py -k test_poisson_second_order
```
