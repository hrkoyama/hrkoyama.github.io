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
