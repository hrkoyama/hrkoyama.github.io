# Continuous P1 Galerkin FEM / 連続P1 Galerkin有限要素法

Status: educational-example

Discretize the weak Poisson problem with continuous piecewise-linear elements. The examples assemble stiffness/consistent-mass matrices on an interval and a triangulated unit square, including nonzero Dirichlet elimination.

Poisson方程式の弱形式を、連続区分線形要素で離散化する。公開例は1次元区間と単位正方形の三角形分割で、剛性・整合質量行列を組み立て、非零Dirichlet値も消去できる。

Not a general mesh generator or implementation of curved elements, variable coefficients or mixed elements. Existing second-order L2 and first-order H1-seminorm tests concern smooth manufactured solutions on these meshes; do not generalize them unconditionally to corner singularities or arbitrary domains.

Other names: FEM, FEM法, 有限要素法, 有限要素, finite element method, P1 FEM, 連続Galerkin法, continuous Galerkin


## 条件と確認範囲 (ja)

problem: Dirichlet境界付きPoisson方程式 −Δu=f の弱解近似。

variant: 連続P1 Galerkin法、区間・アフィン三角形、整合質量行列と疎剛性組立て。

use_when:
- 弱形式・局所要素行列・全体組立てと境界消去を学ぶとき。
- 滑らかな既知解に対するL2/H1誤差を比べるとき。

avoid_when:
- 一般形状・混合境界・不連続係数を追加なしで扱いたい場合。
- 特異な解に対して同じ収束次数を無条件に要求する場合。

assumptions [specified]:
- 定係数の −Δu=f を連続P1 Galerkin空間で近似する。1次元は [0,1] の一様区間、2次元は単位正方形を対角分割したアフィン三角形。
- 剛性・整合質量行列は要素公式を使う。右辺は1次元4点Gauss求積、三角形はDuffy変換の積Gauss求積で評価する。
- Dirichletの行と列を対称に消去し、ILU(0)付きGMRESで解く。滑らかな製造解のL2/H1誤差評価を備える。
要素、求積、組立てと解法を確認した。

units [specified]:
公開例は無次元の長さ1の領域。物理尺度を付けるなら [f]=[u]/L²、次元dの剛性行列はL^(d−2)、質量行列はL^dの幾何学的尺度を持つ。
幾何学的Jacobianと勾配変換による尺度を記述した。

boundary_conditions [specified]:
区間の両端、または単位正方形の全外周にDirichlet値を指定する。標準値は零で、関数により非零値も指定できる。Neumann/Robin境界積分は本例では組み立てない。
全境界Dirichletと対称消去を確認した。

limitations [specified]:
汎用メッシュ生成や曲線要素、可変係数、混合要素の実装ではない。L2で2次・H1半ノルムで1次という既存の検査は滑らかな製造解と本メッシュの範囲であり、角の特異性や任意領域へ無条件に一般化しない。
要素・領域・係数・誤差検査の範囲を限定した。

Review: fem.poisson_1d/2d、triangle_quadrature、eliminate_dirichlet、error_normsと、非零境界の線形パッチ、質量・エネルギー、L2/H1収束の既存検査を読んだ。今回は再実行していない。

Not checked:
- 一般領域・特異解・混合境界の新しい検査。
- 文献の全解析と実装の定理レベルでの対応。

Evidence:
- poisson_1d, poisson_2d, eliminate_dirichlet, triangle_quadrature, error_norms: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/fem.py
- interval/triangle patch, mass, energy and L2/H1 tests: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_sparse_fem.py

References:
- [formulation / primary-research] Courant, R. (1943). Variational methods for the solution of problems of equilibrium and vibrations. — https://doi.org/10.1090/S0002-9904-1943-07818-4
  三角形分割上の区分線形関数による変分近似を根拠付ける。現代的な疎行列・線形解法の出典とは区別する。
  full-text (2026-11-22); Section III, paragraph on linear functions on triangles, PDF p. 15 (reprint printed p. 2179); primary-paper reprint.; https://web.stanford.edu/class/cme324/classics/courant.pdf

## Conditions and review scope (en)

problem: Weak-solution approximation of −Δu=f with Dirichlet data.

variant: Continuous P1 Galerkin on intervals/affine triangles with consistent mass and sparse stiffness assembly.

use_when:
- Studying weak forms, local matrices, assembly and boundary elimination.
- Comparing L2/H1 errors against a smooth known solution.

avoid_when:
- Direct treatment of general geometry, mixed boundaries or discontinuous coefficients.
- Unconditional expectations of the same convergence rates for singular solutions.

assumptions [specified]:
- Approximate constant-coefficient −Δu=f by continuous P1 Galerkin elements: uniform intervals on [0,1] or affine triangles from diagonally split unit-square cells.
- Element formulas assemble stiffness and consistent mass; forcing uses four-point Gauss quadrature in 1D and product Gauss quadrature under a Duffy transform on triangles.
- Dirichlet rows/columns are symmetrically eliminated and the system is solved by ILU(0)-preconditioned GMRES; smooth manufactured solutions support L2/H1 error evaluation.
Inspected elements, quadrature, assembly and linear solve.

units [specified]:
Examples use dimensionless unit-length domains. With physical scaling, [f]=[u]/L²; stiffness and mass have geometric scales L^(d−2) and L^d in dimension d.
Specified geometric Jacobian and gradient-transformation scaling.

boundary_conditions [specified]:
Dirichlet data apply at both interval endpoints or the full unit-square perimeter; defaults are zero and callbacks allow nonzero data. This example does not assemble Neumann/Robin boundary integrals.
Checked full-Dirichlet data and symmetric elimination.

limitations [specified]:
Not a general mesh generator or implementation of curved elements, variable coefficients or mixed elements. Existing second-order L2 and first-order H1-seminorm tests concern smooth manufactured solutions on these meshes; do not generalize them unconditionally to corner singularities or arbitrary domains.
Scoped elements, domains, coefficients and error tests.

Review: Inspected fem.poisson_1d/2d, triangle_quadrature, eliminate_dirichlet, error_norms and existing nonzero-boundary patch, mass/energy and L2/H1-convergence tests; no rerun.

Not checked:
- New checks for general domains, singular solutions or mixed boundaries.
- A theorem-level audit of the full literature analysis against the implementation.

Evidence:
- poisson_1d, poisson_2d, eliminate_dirichlet, triangle_quadrature, error_norms: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/fem.py
- interval/triangle patch, mass, energy and L2/H1 tests: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_sparse_fem.py

References:
- [formulation / primary-research] Courant, R. (1943). Variational methods for the solution of problems of equilibrium and vibrations. — https://doi.org/10.1090/S0002-9904-1943-07818-4
  Supports triangular piecewise-linear variational approximation, separately from the modern sparse solver implementation.
  full-text (2026-11-22); Section III, paragraph on linear functions on triangles, PDF p. 15 (reprint printed p. 2179); primary-paper reprint.; https://web.stanford.edu/class/cme324/classics/courant.pdf


- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/fem/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/fem/

- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/fem.py

- Reference: https://doi.org/10.1090/S0002-9904-1943-07818-4 — Piecewise-linear trial functions on triangular subdivisions in a variational formulation; not a source for the atlas's CSR or GMRES implementation.

Common execution records: [{"id": "poisson-2d-sine", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=ja#poisson-2d-sine-ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=en#poisson-2d-sine-en"}}]

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/p1-fem/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [Poisson・Laplace方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#poisson-laplace-ja) (`poisson-laplace`; poisson-2d-sine)

#### 問題の図 (`method-problems-ja`)

##### [2次元Poisson・正弦単一モード（FEMを含む）](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=ja) (`poisson-2d-sine`)

![同じ正弦製造解を解く、三角形有限要素の保存解と誤差。](https://hrkoyama.github.io/numerical-methods-atlas/assets/field-fem-poisson.png)

この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。 SEMはC0連続なテンソル積Qp Lagrange基底・p+1個のLegendre GLL節点と求積、疎な剛性行列・SciPy直接解法を使用。p=2で各方向2/4/8要素、別に2×2要素でp=1〜6。公開済みNumartのP1 FEM・GMRESをファイルのバイト列を保持して4/8/16分割で実行し、両者の自由未知数9/49/225を一致させます。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=ja#code-ja)

- [2次元Poisson：CG・多重格子とP1 FEM](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/poisson-2d-sine/?lang=ja) (`poisson-2d-sine`) · [コードZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

単位正方形のsin(πx)sin(πy)を参照し、CG/MGは15/31/63内部点、P1 FEMは4/8/16分割で細分化。FDの最大誤差と真の残差、FEMの要素内L2誤差とH1半ノルムを独立に評価する。

- [スペクトル要素法の2D Poisson：P1 FEMとh/p収束を比較](https://hrkoyama.github.io/numerical-methods-atlas/validation/sem-poisson-2d/?lang=ja) (`sem-poisson-2d`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/atlas-sem-fr-2026-11-23.zip)

単位正方形の正弦製造解をGLLスペクトル要素法と既存P1三角形FEMで解きます。自由未知数を揃えたh細分化と、固定要素数でのp=1〜6を分けて測ります。


#### 厳密解・参照解 (`method-references-ja`)

##### [2次元Poisson・正弦単一モード（FEMを含む）](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=ja#references-ja) (`poisson-2d-sine`)

- [Poisson／正弦波の製造解](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-poisson-manufactured-ja) (`poisson-manufactured`; 関連モデルの参照; 製造解)

カードは1次元sin(πx)、こちらは2次元sin(πx)sin(πy)です。次元・右辺・FEMの誤差ノルムは異なります。

[既存の参照図](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=poisson-manufactured)

- [2D Poisson正弦製造解：SEMとP1 FEMの共通参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-sem-poisson-2d-ja) (`sem-poisson-2d`; 同じ問題の参照; 製造解)

全て無次元。−Δu=2π²sin(πx)sin(πy)、領域[0,1]²、境界u=0。係数は一定、SEMは直交するアフィン正方形、FEMは既存の規則的な三角形分割。

[既存の参照図](/numerical-methods-atlas/validation/sem-poisson-2d/?lang=ja)

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/fem/)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

##### 2次元Poisson：CG・多重格子とP1 FEM (`poisson-2d-sine`)

[2次元Poisson・正弦単一モード（FEMを含む）](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/poisson-2d-sine/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

[固定入力](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/recipes/poisson-2d-sine.json)

[検証記録](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

単位正方形のsin(πx)sin(πy)を参照し、CG/MGは15/31/63内部点、P1 FEMは4/8/16分割で細分化。FDの最大誤差と真の残差、FEMの要素内L2誤差とH1半ノルムを独立に評価する。

##### スペクトル要素法の2D Poisson：P1 FEMとh/p収束を比較 (`sem-poisson-2d`)

[2次元Poisson・正弦単一モード（FEMを含む）](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/sem-poisson-2d/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/atlas-sem-fr-2026-11-23.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/verification.json)

単位正方形の正弦製造解をGLLスペクトル要素法と既存P1三角形FEMで解きます。自由未知数を揃えたh細分化と、固定要素数でのp=1〜6を分けて測ります。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

Related chapter modules and test files; not a claim that each test covers every named method.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### 関連ソース

- [/code/numerical-methods-atlas/2026-11-21/numart/fem.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/fem.py)

###### 配布版のテスト

- [/code/numerical-methods-atlas/2026-11-21/tests/test_sparse_fem.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_sparse_fem.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q tests/test_sparse_fem.py
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Poisson / Laplace equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#poisson-laplace-en) (`poisson-laplace`; poisson-2d-sine)

#### Problem figures (`method-problems-en`)

##### [2D Poisson / single sine mode, including FEM](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=en) (`poisson-2d-sine`)

![Stored triangular-FEM solution and error for the same sine manufactured problem.](https://hrkoyama.github.io/numerical-methods-atlas/assets/field-fem-poisson.png)

Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed. C0 tensor Qp Lagrange SEM with p+1 Legendre GLL nodes/quadrature, sparse stiffness assembly and a SciPy direct solve. At p=2 use2/4/8 elements per axis; separately fix2x2 elements and p=1..6. Execute the byte-identical published Numart triangle P1 FEM/GMRES at4/8/16 subdivisions, matching9/49/225 free unknowns.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=en#code-en)

- [2D Poisson: CG, multigrid and P1 FEM](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/poisson-2d-sine/?lang=en) (`poisson-2d-sine`) · [Code ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

Reference sin(πx)sin(πy) on the unit square; refine CG/MG through 15/31/63 interior nodes and P1 FEM through 4/8/16 subdivisions. Independently evaluate FD maximum errors/true residuals and FEM element-interior L2/H1-seminorm errors.

- [2D spectral-element Poisson: P1 FEM comparison and h/p refinement](https://hrkoyama.github.io/numerical-methods-atlas/validation/sem-poisson-2d/?lang=en) (`sem-poisson-2d`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/atlas-sem-fr-2026-11-23.zip)

Solve a sine manufactured solution on the unit square with GLL spectral elements and the existing triangle P1 FEM. Compare matched free-unknown counts under h refinement and p=1..6 at fixed elements.


#### Exact / reference solutions (`method-references-en`)

##### [2D Poisson / single sine mode, including FEM](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=en#references-en) (`poisson-2d-sine`)

- [Poisson / manufactured sine](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-poisson-manufactured-en) (`poisson-manufactured`; Related-model reference; Manufactured solution)

The card is 1D sin(πx); this test is 2D sin(πx)sin(πy). Dimension, forcing and FEM error norms differ.

[Existing reference profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=poisson-manufactured)

- [2D Poisson sine manufactured solution: shared SEM/P1 FEM reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-sem-poisson-2d-en) (`sem-poisson-2d`; Same-problem reference; Manufactured solution)

Dimensionless: -Laplacian u=2pi²sin(pi x)sin(pi y) on[0,1]², u=0 on the boundary. Constant coefficient; affine Cartesian squares for SEM and the existing regular triangle mesh for P1 FEM.

[Existing reference profile](/numerical-methods-atlas/validation/sem-poisson-2d/?lang=en)

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/fem/)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

##### 2D Poisson: CG, multigrid and P1 FEM (`poisson-2d-sine`)

[2D Poisson / single sine mode, including FEM](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/poisson-2d-sine/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

[Fixed input](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/recipes/poisson-2d-sine.json)

[Verification receipt](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

Reference sin(πx)sin(πy) on the unit square; refine CG/MG through 15/31/63 interior nodes and P1 FEM through 4/8/16 subdivisions. Independently evaluate FD maximum errors/true residuals and FEM element-interior L2/H1-seminorm errors.

##### 2D spectral-element Poisson: P1 FEM comparison and h/p refinement (`sem-poisson-2d`)

[2D Poisson / single sine mode, including FEM](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/sem-poisson-2d/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/atlas-sem-fr-2026-11-23.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/verification.json)

Solve a sine manufactured solution on the unit square with GLL spectral elements and the existing triangle P1 FEM. Compare matched free-unknown counts under h refinement and p=1..6 at fixed elements.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Related chapter modules and test files; not a claim that each test covers every named method.

[Related code edition / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### Related source

- [/code/numerical-methods-atlas/2026-11-21/numart/fem.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/fem.py)

###### Package tests

- [/code/numerical-methods-atlas/2026-11-21/tests/test_sparse_fem.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_sparse_fem.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q tests/test_sparse_fem.py
```
