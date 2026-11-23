# 2D混合Robinの製造解と境界流束 / 2D mixed Robin MMS and boundary flux

https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-robin/

## 日本語

[実際に保存した計算配列と固定入力の収束指標から描いた検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/poisson-robin-preview.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-mesh-boundary/#poisson-robin) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#poisson-robin)

### 方程式・問題の定義

単位正方形N16/32/64、u=cos(pi x)cos(2pi y)+x+y。x壁Neumann±1、y壁alpha1,beta.5の解析Robin。

#### [Poisson・Laplace方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#poisson-laplace-ja)

$$
-\nabla^2u=f
$$

$$
f=0\quad\Longrightarrow\quad\nabla^2u=0
$$

楕円型境界値問題。符号規約を確認し、反復解法・疎行列・境界条件をたどる。

#### 2D混合Robinの製造解と境界流束

補助実行例 · 実行例の定義・検証式

$$
\alpha u_b+\beta\partial_nu=g,\quad\partial_nu=(g-\alpha u_i)/(\beta+\alpha h/2)
$$

2D PoissonのNeumann/Robin面を実際に組み、連続製造解と境界fluxを照合します。

### 厳密解・参照解

2D解/誤差、真の残差、Robin関係残差と解析法線flux誤差、3格子細分化と積分収支を保存。

#### [混合Robin：2次元解析場と独立な法線流束](https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-robin/?lang=ja#poisson-robin-ja-measurements)

製造解 · 同じ問題の参照

u=cos(pi*x)*cos(2*pi*y)+x+y; -Delta(u)=5*pi^2*cos(pi*x)*cos(2*pi*y); alpha*u+beta*dn(u)=g.

単位正方形N16/32/64、u=cos(pi x)cos(2pi y)+x+y。x壁Neumann±1、y壁alpha1,beta.5の解析Robin。f=5π²cos(πx)cos(2πy)を使い、x壁は外向きNeumann±1、y壁はαu+β∂nu=gの解析値です。境界条件の代数残差と、解析的な物理法線流束の誤差を別々に測ります。

Robin問題は一意なので平均ゲージを重ねません。境界条件の代数残差と物理flux精度を区別します。

#### 2D混合Robinの製造解と境界流束

2D解/誤差、真の残差、Robin関係残差と解析法線flux誤差、3格子細分化と積分収支を保存。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-robin/?lang=ja)

### 計算法

半セル距離を用いてRobin境界値を消去し、外向きgradientの面積積分を離散式と同じ重みで評価。

- [空間中心差分](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [2D混合Robinの製造解と境界流束](https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-robin/?lang=ja)

補助実行例

2D PoissonのNeumann/Robin面を実際に組み、連続製造解と境界fluxを照合します。

単位正方形N16/32/64、u=cos(pi x)cos(2pi y)+x+y。x壁Neumann±1、y壁alpha1,beta.5の解析Robin。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/atlas-mesh-boundary-2026-11-23.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

Robin問題は一意なので平均ゲージを重ねません。境界条件の代数残差と物理flux精度を区別します。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-23/mesh-boundary/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/run.py)
- [/code/validated-examples/2026-11-23/mesh-boundary/boundary.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/boundary.py)
- [/code/validated-examples/2026-11-23/mesh-boundary/test_geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/test_geometry.py)

## English

[Validation preview from actual saved PDE arrays and fixed-input refinement measurements.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/poisson-robin-preview.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-mesh-boundary/#poisson-robin) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#poisson-robin-en)

### Equations and problem definitions

Unit square N16/32/64; cosine-plus-linear exact field. x walls Neumann±1; y walls analytic Robin alpha1,beta.5.

#### [Poisson / Laplace equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#poisson-laplace-en)

$$
-\nabla^2u=f
$$

$$
f=0\quad\Longrightarrow\quad\nabla^2u=0
$$

Elliptic boundary-value problems: check sign conventions, iterative solvers, sparse matrices and boundaries.

#### 2D mixed Robin MMS and boundary flux

Supplementary execution example · Example definition or validation formula

$$
\alpha u_b+\beta\partial_nu=g,\quad\partial_nu=(g-\alpha u_i)/(\beta+\alpha h/2)
$$

Assemble actual2D Neumann/Robin faces and compare the manufactured field and boundary flux.

### Exact and reference solutions

Save2D solution/errors, true residuals, Robin relation and analytic normal-flux errors, three-grid refinement and integral budget.

#### [Mixed Robin: 2D analytic field and independent normal flux](https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-robin/?lang=en#poisson-robin-en-measurements)

Manufactured solution · Reference for the same problem

u=cos(pi*x)*cos(2*pi*y)+x+y; -Delta(u)=5*pi^2*cos(pi*x)*cos(2*pi*y); alpha*u+beta*dn(u)=g.

Unit square N16/32/64; cosine-plus-linear exact field. x walls Neumann±1; y walls analytic Robin alpha1,beta.5. Use f=5pi²cos(pi*x)cos(2pi*y),outward Neumann±1 on x walls and analytic alpha*u+beta*dn(u)=g on y walls. Distinguish algebraic boundary-relation residual from analytic physical-normal-flux error.

The unique Robin problem has no additional mean gauge. Algebraic boundary satisfaction differs from physical flux accuracy.

#### 2D mixed Robin MMS and boundary flux

Save2D solution/errors, true residuals, Robin relation and analytic normal-flux errors, three-grid refinement and integral budget.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-robin/?lang=en)

### Numerical methods

Eliminate Robin trace at half-cell distance, using the same outward-gradient face weights in the discrete PDE and budget.

- [Centered spatial difference](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [2D mixed Robin MMS and boundary flux](https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-robin/?lang=en)

Supplementary execution example

Assemble actual2D Neumann/Robin faces and compare the manufactured field and boundary flux.

Unit square N16/32/64; cosine-plus-linear exact field. x walls Neumann±1; y walls analytic Robin alpha1,beta.5.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/atlas-mesh-boundary-2026-11-23.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

The unique Robin problem has no additional mean gauge. Algebraic boundary satisfaction differs from physical flux accuracy.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-23/mesh-boundary/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/run.py)
- [/code/validated-examples/2026-11-23/mesh-boundary/boundary.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/boundary.py)
- [/code/validated-examples/2026-11-23/mesh-boundary/test_geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/test_geometry.py)
