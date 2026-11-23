# L字領域P1特異解：graded格子と歪みの分離 / L-corner P1 FEM: grading and separate mesh distortion

https://hrkoyama.github.io/numerical-methods-atlas/problems/lshape-fem/

## 日本語

[実際に保存した計算配列と固定入力の収束指標から描いた検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/lshape-fem-preview.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-mesh-boundary/#lshape-fem) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#lshape-fem)

### 方程式・問題の定義

第4象限を除いた[-1,1]²、theta∈[0,3pi/2]、u=r^(2/3)sin(2theta/3)、解析Dirichlet。N8/16/32、graded map x→x max(|x|,|y|)。正方形sin(pi x)sin(pi y)を同Nのregular/warpedで別検査。

#### [Poisson・Laplace方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#poisson-laplace-ja)

$$
-\nabla^2u=f
$$

$$
f=0\quad\Longrightarrow\quad\nabla^2u=0
$$

楕円型境界値問題。符号規約を確認し、反復解法・疎行列・境界条件をたどる。

#### L字領域P1特異解：graded格子と歪みの分離

補助実行例 · 実行例の定義・検証式

$$
-\Delta u=0,\quad u=r^{2/3}\sin(2\theta/3)
$$

$$
K_{ab}=\sum_T |T|\nabla N_a\cdot\nabla N_b,\quad x_{graded}=x\|x\|_\infty
$$

再入隅の調和特異解を真の2D P1で解き、同じ未知数の一様/graded格子と、独立した滑らかな正方形の歪みを比較します。

### 厳密解・参照解

L2/H1積分誤差・求積差、一様/gradedの同DOF改善、別のsquare/warped系列、最小角・aspect・1ノルム条件数推定・真の線形残差を保存。

#### [L字角の特異解：調和場と別の滑らかな製造解](https://hrkoyama.github.io/numerical-methods-atlas/validation/lshape-fem/?lang=ja#lshape-fem-ja-measurements)

解析解 · 同じ問題の参照

u=r^(2/3)*sin(2*theta/3); -Delta(u)=0; theta in[0,3*pi/2]; separate square MMS u=sin(pi*x)*sin(pi*y).

第4象限を除いた[-1,1]²、theta∈[0,3pi/2]、u=r^(2/3)sin(2theta/3)、解析Dirichlet。N8/16/32、graded map x→x max(|x|,|y|)。正方形sin(pi x)sin(pi y)を同Nのregular/warpedで別検査。角の解析解と勾配を要素求積し、一様格子と事前graded格子を同じ自由度で比べます。別の単位正方形でsin(πx)sin(πy)をregular/warped格子へ置き、特異性と歪みを分けます。

特異解に正方形のL2二次を要求しません。固定の事前graded写像でありAMRソフトではありません。条件数は推定で、任意歪みへの保証はしません。

#### L字領域P1特異解：graded格子と歪みの分離

L2/H1積分誤差・求積差、一様/gradedの同DOF改善、別のsquare/warped系列、最小角・aspect・1ノルム条件数推定・真の線形残差を保存。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/lshape-fem/?lang=ja)

### 計算法

面積と物理勾配からP1剛性を組み、境界を消去して疎直接法で解きます。隅要素は原点をDuffy写像の頂点に移し、Gauss48/96を比較。

- [連続P1 Galerkin有限要素法](https://hrkoyama.github.io/numerical-methods-atlas/methods/p1-fem/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [L字領域P1特異解：graded格子と歪みの分離](https://hrkoyama.github.io/numerical-methods-atlas/validation/lshape-fem/?lang=ja)

補助実行例

再入隅の調和特異解を真の2D P1で解き、同じ未知数の一様/graded格子と、独立した滑らかな正方形の歪みを比較します。

第4象限を除いた[-1,1]²、theta∈[0,3pi/2]、u=r^(2/3)sin(2theta/3)、解析Dirichlet。N8/16/32、graded map x→x max(|x|,|y|)。正方形sin(pi x)sin(pi y)を同Nのregular/warpedで別検査。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/atlas-mesh-boundary-2026-11-23.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

特異解に正方形のL2二次を要求しません。固定の事前graded写像でありAMRソフトではありません。条件数は推定で、任意歪みへの保証はしません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-23/mesh-boundary/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/run.py)
- [/code/validated-examples/2026-11-23/mesh-boundary/fem.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/fem.py)
- [/code/validated-examples/2026-11-23/mesh-boundary/references/fields.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/references/fields.py)
- [/code/validated-examples/2026-11-23/mesh-boundary/test_geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/test_geometry.py)

## English

[Validation preview from actual saved PDE arrays and fixed-input refinement measurements.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/lshape-fem-preview.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-mesh-boundary/#lshape-fem) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#lshape-fem-en)

### Equations and problem definitions

L-shaped[-1,1]² minus quadrantIV, theta0..3pi/2, analytic Dirichlet harmonic corner field. N8/16/32, fixed map x→x max(|x|,|y|). Separate unit-square sine MMS uses regular/warped grids.

#### [Poisson / Laplace equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#poisson-laplace-en)

$$
-\nabla^2u=f
$$

$$
f=0\quad\Longrightarrow\quad\nabla^2u=0
$$

Elliptic boundary-value problems: check sign conventions, iterative solvers, sparse matrices and boundaries.

#### L-corner P1 FEM: grading and separate mesh distortion

Supplementary execution example · Example definition or validation formula

$$
-\Delta u=0,\quad u=r^{2/3}\sin(2\theta/3)
$$

$$
K_{ab}=\sum_T |T|\nabla N_a\cdot\nabla N_b,\quad x_{graded}=x\|x\|_\infty
$$

Solve a harmonic reentrant-corner field with actual2D P1 FEM; compare matched-DOF uniform/grading and separate smooth-square mesh distortion.

### Exact and reference solutions

Retain integrated L2/H1 errors, quadrature gaps, matched-DOF grading improvement, separate square/warp errors, minimum angle/aspect, estimated1-norm conditioning and true residuals.

#### [L-corner singularity: harmonic field and separate smooth MMS](https://hrkoyama.github.io/numerical-methods-atlas/validation/lshape-fem/?lang=en#lshape-fem-en-measurements)

Analytic reference · Reference for the same problem

u=r^(2/3)*sin(2*theta/3); -Delta(u)=0; theta in[0,3*pi/2]; separate square MMS u=sin(pi*x)*sin(pi*y).

L-shaped[-1,1]² minus quadrantIV, theta0..3pi/2, analytic Dirichlet harmonic corner field. N8/16/32, fixed map x→x max(|x|,|y|). Separate unit-square sine MMS uses regular/warped grids. Integrate the analytic corner field and gradient over elements, comparing uniform and a-priori graded meshes at matched DOFs. A separate unit-square sine MMS on regular/warped meshes separates singularity from distortion.

No smooth-square L2 order is imposed on the singular field. Fixed a-priori grading is not an AMR engine. Conditioning is estimated; arbitrary distortion is not certified.

#### L-corner P1 FEM: grading and separate mesh distortion

Retain integrated L2/H1 errors, quadrature gaps, matched-DOF grading improvement, separate square/warp errors, minimum angle/aspect, estimated1-norm conditioning and true residuals.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/lshape-fem/?lang=en)

### Numerical methods

Assemble physical P1 gradients/areas, eliminate boundary data and solve sparse systems. Corner triangles use origin-based Duffy quadrature48/96.

- [Continuous P1 Galerkin FEM](https://hrkoyama.github.io/numerical-methods-atlas/methods/p1-fem/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [L-corner P1 FEM: grading and separate mesh distortion](https://hrkoyama.github.io/numerical-methods-atlas/validation/lshape-fem/?lang=en)

Supplementary execution example

Solve a harmonic reentrant-corner field with actual2D P1 FEM; compare matched-DOF uniform/grading and separate smooth-square mesh distortion.

L-shaped[-1,1]² minus quadrantIV, theta0..3pi/2, analytic Dirichlet harmonic corner field. N8/16/32, fixed map x→x max(|x|,|y|). Separate unit-square sine MMS uses regular/warped grids.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/atlas-mesh-boundary-2026-11-23.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

No smooth-square L2 order is imposed on the singular field. Fixed a-priori grading is not an AMR engine. Conditioning is estimated; arbitrary distortion is not certified.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-23/mesh-boundary/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/run.py)
- [/code/validated-examples/2026-11-23/mesh-boundary/fem.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/fem.py)
- [/code/validated-examples/2026-11-23/mesh-boundary/references/fields.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/references/fields.py)
- [/code/validated-examples/2026-11-23/mesh-boundary/test_geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/test_geometry.py)
