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

## Small fixed-input validation supplements

AdditionalP1 cases compare an Lshape singularity on uniform/matched-DOF graded meshes and square/warped triangles. Independently increase corner-Duffy quadrature and compare L2/H1 errors and mesh quality.

追加のP1例はL字領域の特異解と同じ未知数数のgraded格子、正方形/warped三角形。角に接するDuffy積分を別次数で確認し、L2/H1誤差と格子品質を比較します。

- L-corner P1 FEM: grading and separate mesh distortion: https://hrkoyama.github.io/numerical-methods-atlas/validation/lshape-fem/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/atlas-mesh-boundary-2026-11-23.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/result.json

Common execution records: [{"id": "poisson-2d-sine", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=ja#poisson-2d-sine-ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=en#poisson-2d-sine-en"}}, {"id": "lshape-fem", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/lshape-fem/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/lshape-fem/?lang=en"}, "kind": "dedicated-supplement"}]

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/p1-fem/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [Poisson・Laplace方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#poisson-laplace-ja) (`poisson-laplace`; poisson-2d-sine, lshape-fem)

#### 問題の図 (`method-problems-ja`)

##### [2次元Poisson・正弦単一モード（FEMを含む）](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=ja) (`poisson-2d-sine`)

![同じ正弦製造解を解く、三角形有限要素の保存解と誤差。](https://hrkoyama.github.io/numerical-methods-atlas/assets/field-fem-poisson.png)

この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。 SEMはC0連続なテンソル積Qp Lagrange基底・p+1個のLegendre GLL節点と求積、疎な剛性行列・SciPy直接解法を使用。p=2で各方向2/4/8要素、別に2×2要素でp=1〜6。公開済みNumartのP1 FEM・GMRESをファイルのバイト列を保持して4/8/16分割で実行し、両者の自由未知数9/49/225を一致させます。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=ja#code-ja)

- [2次元Poisson：CG・多重格子とP1 FEM](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/poisson-2d-sine/?lang=ja) (`poisson-2d-sine`) · [コードZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

単位正方形のsin(πx)sin(πy)を参照し、CG/MGは15/31/63内部点、P1 FEMは4/8/16分割で細分化。FDの最大誤差と真の残差、FEMの要素内L2誤差とH1半ノルムを独立に評価する。

- [スペクトル要素法の2D Poisson：P1 FEMとh/p収束を比較](https://hrkoyama.github.io/numerical-methods-atlas/validation/sem-poisson-2d/?lang=ja) (`sem-poisson-2d`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/atlas-sem-fr-2026-11-23.zip)

単位正方形の正弦製造解をGLLスペクトル要素法と既存P1三角形FEMで解きます。自由未知数を揃えたh細分化と、固定要素数でのp=1〜6を分けて測ります。

##### [L字領域P1特異解：graded格子と歪みの分離](https://hrkoyama.github.io/numerical-methods-atlas/problems/lshape-fem/?lang=ja) (`lshape-fem`)

![実際に保存した計算配列と固定入力の収束指標から描いた検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/lshape-fem-preview.png)

面積と物理勾配からP1剛性を組み、境界を消去して疎直接法で解きます。隅要素は原点をDuffy写像の頂点に移し、Gauss48/96を比較。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/lshape-fem/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/lshape-fem/?lang=ja#code-ja)

- [L字領域P1特異解：graded格子と歪みの分離](https://hrkoyama.github.io/numerical-methods-atlas/validation/lshape-fem/?lang=ja) (`lshape-fem`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/atlas-mesh-boundary-2026-11-23.zip)

再入隅の調和特異解を真の2D P1で解き、同じ未知数の一様/graded格子と、独立した滑らかな正方形の歪みを比較します。


#### 厳密解・参照解 (`method-references-ja`)

##### [2次元Poisson・正弦単一モード（FEMを含む）](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=ja#references-ja) (`poisson-2d-sine`)

- [Poisson／正弦波の製造解](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-poisson-manufactured-ja) (`poisson-manufactured`; 関連モデルの参照; 製造解)

カードは1次元sin(πx)、こちらは2次元sin(πx)sin(πy)です。次元・右辺・FEMの誤差ノルムは異なります。

[既存の参照図](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=poisson-manufactured)

- [2D Poisson正弦製造解：SEMとP1 FEMの共通参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-sem-poisson-2d-ja) (`sem-poisson-2d`; 同じ問題の参照; 製造解)

全て無次元。−Δu=2π²sin(πx)sin(πy)、領域[0,1]²、境界u=0。係数は一定、SEMは直交するアフィン正方形、FEMは既存の規則的な三角形分割。

[既存の参照図](/numerical-methods-atlas/validation/sem-poisson-2d/?lang=ja)

##### [L字領域P1特異解：graded格子と歪みの分離](https://hrkoyama.github.io/numerical-methods-atlas/problems/lshape-fem/?lang=ja#references-ja) (`lshape-fem`)

- [L字角の特異解：調和場と別の滑らかな製造解](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-lshape-fem-ja) (`lshape-fem`; 同じ問題の参照; 解析参照)

特異解に正方形のL2二次を要求しません。固定の事前graded写像でありAMRソフトではありません。条件数は推定で、任意歪みへの保証はしません。

[既存の参照図](/numerical-methods-atlas/validation/lshape-fem/?lang=ja#lshape-fem-ja-measurements)

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

##### L字領域P1特異解：graded格子と歪みの分離 (`lshape-fem`)

[L字領域P1特異解：graded格子と歪みの分離](https://hrkoyama.github.io/numerical-methods-atlas/problems/lshape-fem/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/lshape-fem/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/atlas-mesh-boundary-2026-11-23.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/verification.json)

再入隅の調和特異解を真の2D P1で解き、同じ未知数の一様/graded格子と、独立した滑らかな正方形の歪みを比較します。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

追加のP1例はL字領域の特異解と同じ未知数数のgraded格子、正方形/warped三角形。角に接するDuffy積分を別次数で確認し、L2/H1誤差と格子品質を比較します。

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### 関連ソース

- [/code/numerical-methods-atlas/2026-11-21/numart/fem.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/fem.py)
- [/code/validated-examples/2026-11-23/mesh-boundary/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/run.py)
- [/code/validated-examples/2026-11-23/mesh-boundary/fem.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/fem.py)
- [/code/validated-examples/2026-11-23/mesh-boundary/references/fields.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/references/fields.py)
- [/code/validated-examples/2026-11-23/mesh-boundary/annulus.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/annulus.py)
- [/code/validated-examples/2026-11-23/mesh-boundary/boundary.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/boundary.py)
- [/code/validated-examples/2026-11-23/mesh-boundary/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/experiments.py)

###### 配布版のテスト

- [/code/numerical-methods-atlas/2026-11-21/tests/test_sparse_fem.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_sparse_fem.py)
- [/code/validated-examples/2026-11-23/mesh-boundary/test_geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/test_geometry.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q tests/test_sparse_fem.py
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Poisson / Laplace equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#poisson-laplace-en) (`poisson-laplace`; poisson-2d-sine, lshape-fem)

#### Problem figures (`method-problems-en`)

##### [2D Poisson / single sine mode, including FEM](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=en) (`poisson-2d-sine`)

![Stored triangular-FEM solution and error for the same sine manufactured problem.](https://hrkoyama.github.io/numerical-methods-atlas/assets/field-fem-poisson.png)

Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed. C0 tensor Qp Lagrange SEM with p+1 Legendre GLL nodes/quadrature, sparse stiffness assembly and a SciPy direct solve. At p=2 use2/4/8 elements per axis; separately fix2x2 elements and p=1..6. Execute the byte-identical published Numart triangle P1 FEM/GMRES at4/8/16 subdivisions, matching9/49/225 free unknowns.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=en#code-en)

- [2D Poisson: CG, multigrid and P1 FEM](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/poisson-2d-sine/?lang=en) (`poisson-2d-sine`) · [Code ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

Reference sin(πx)sin(πy) on the unit square; refine CG/MG through 15/31/63 interior nodes and P1 FEM through 4/8/16 subdivisions. Independently evaluate FD maximum errors/true residuals and FEM element-interior L2/H1-seminorm errors.

- [2D spectral-element Poisson: P1 FEM comparison and h/p refinement](https://hrkoyama.github.io/numerical-methods-atlas/validation/sem-poisson-2d/?lang=en) (`sem-poisson-2d`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/atlas-sem-fr-2026-11-23.zip)

Solve a sine manufactured solution on the unit square with GLL spectral elements and the existing triangle P1 FEM. Compare matched free-unknown counts under h refinement and p=1..6 at fixed elements.

##### [L-corner P1 FEM: grading and separate mesh distortion](https://hrkoyama.github.io/numerical-methods-atlas/problems/lshape-fem/?lang=en) (`lshape-fem`)

![Validation preview from actual saved PDE arrays and fixed-input refinement measurements.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/lshape-fem-preview.png)

Assemble physical P1 gradients/areas, eliminate boundary data and solve sparse systems. Corner triangles use origin-based Duffy quadrature48/96.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/lshape-fem/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/lshape-fem/?lang=en#code-en)

- [L-corner P1 FEM: grading and separate mesh distortion](https://hrkoyama.github.io/numerical-methods-atlas/validation/lshape-fem/?lang=en) (`lshape-fem`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/atlas-mesh-boundary-2026-11-23.zip)

Solve a harmonic reentrant-corner field with actual2D P1 FEM; compare matched-DOF uniform/grading and separate smooth-square mesh distortion.


#### Exact / reference solutions (`method-references-en`)

##### [2D Poisson / single sine mode, including FEM](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=en#references-en) (`poisson-2d-sine`)

- [Poisson / manufactured sine](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-poisson-manufactured-en) (`poisson-manufactured`; Related-model reference; Manufactured solution)

The card is 1D sin(πx); this test is 2D sin(πx)sin(πy). Dimension, forcing and FEM error norms differ.

[Existing reference profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=poisson-manufactured)

- [2D Poisson sine manufactured solution: shared SEM/P1 FEM reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-sem-poisson-2d-en) (`sem-poisson-2d`; Same-problem reference; Manufactured solution)

Dimensionless: -Laplacian u=2pi²sin(pi x)sin(pi y) on[0,1]², u=0 on the boundary. Constant coefficient; affine Cartesian squares for SEM and the existing regular triangle mesh for P1 FEM.

[Existing reference profile](/numerical-methods-atlas/validation/sem-poisson-2d/?lang=en)

##### [L-corner P1 FEM: grading and separate mesh distortion](https://hrkoyama.github.io/numerical-methods-atlas/problems/lshape-fem/?lang=en#references-en) (`lshape-fem`)

- [L-corner singularity: harmonic field and separate smooth MMS](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-lshape-fem-en) (`lshape-fem`; Same-problem reference; Analytic reference)

No smooth-square L2 order is imposed on the singular field. Fixed a-priori grading is not an AMR engine. Conditioning is estimated; arbitrary distortion is not certified.

[Existing reference profile](/numerical-methods-atlas/validation/lshape-fem/?lang=en#lshape-fem-en-measurements)

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

##### L-corner P1 FEM: grading and separate mesh distortion (`lshape-fem`)

[L-corner P1 FEM: grading and separate mesh distortion](https://hrkoyama.github.io/numerical-methods-atlas/problems/lshape-fem/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/lshape-fem/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/atlas-mesh-boundary-2026-11-23.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/verification.json)

Solve a harmonic reentrant-corner field with actual2D P1 FEM; compare matched-DOF uniform/grading and separate smooth-square mesh distortion.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

AdditionalP1 cases compare an Lshape singularity on uniform/matched-DOF graded meshes and square/warped triangles. Independently increase corner-Duffy quadrature and compare L2/H1 errors and mesh quality.

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[Related code edition / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### Related source

- [/code/numerical-methods-atlas/2026-11-21/numart/fem.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/fem.py)
- [/code/validated-examples/2026-11-23/mesh-boundary/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/run.py)
- [/code/validated-examples/2026-11-23/mesh-boundary/fem.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/fem.py)
- [/code/validated-examples/2026-11-23/mesh-boundary/references/fields.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/references/fields.py)
- [/code/validated-examples/2026-11-23/mesh-boundary/annulus.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/annulus.py)
- [/code/validated-examples/2026-11-23/mesh-boundary/boundary.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/boundary.py)
- [/code/validated-examples/2026-11-23/mesh-boundary/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/experiments.py)

###### Package tests

- [/code/numerical-methods-atlas/2026-11-21/tests/test_sparse_fem.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_sparse_fem.py)
- [/code/validated-examples/2026-11-23/mesh-boundary/test_geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/test_geometry.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q tests/test_sparse_fem.py
```
