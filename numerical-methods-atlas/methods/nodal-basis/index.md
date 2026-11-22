# Lagrange nodal basis / GLL collocation / Lagrange節点基底・GLL選点法

Status: educational-example

Interpolate from nodal values with Lagrange cardinal functions. The example covers interval GLL/equispaced nodes, triangle P1/P2, quadrilateral Qₚ products, and exact versus GLL-quadrature-lumped mass.

節点でδᵢⱼとなるLagrange基底により、関数を節点値から補間する。公開実装は区間のGLL/等間隔節点、三角形P1/P2、四角形Qₚの積基底と、GLLの厳密質量・求積集中質量の差を扱う。

High-degree Vandermonde solves face conditioning limits and are not a replacement for stable barycentric tabulation or a general high-order element library. High-degree equispaced interpolation can exhibit Runge behavior. The rank-one exact/lumped GLL mass difference concerns the unweighted affine interval, not arbitrary triangles.

Other names: Lagrange基底, Lagrange interpolation basis, ラグランジュ基底, 節点基底, GLL, Gauss-Lobatto-Legendre


## 条件と確認範囲 (ja)

problem: 節点値からの多項式補間、微分と参照要素行列。

variant: Legendre Vandermondeで構成する区間Lagrange基底、GLL/等間隔節点、明示P1/P2三角形、Qₚ積基底。

use_when:
- 節点自由度、partition of unity、モード表現との同値性を調べるとき。
- GLLで対角化した求積質量と厳密質量の違いを比較するとき。

avoid_when:
- 任意次数の三角形・曲線要素や大規模高次数表作成を求める場合。
- GLLの対角質量を常に厳密だとみなす場合。

assumptions [specified]:
- 区間節点は相異なる有限実数で、中程度の次数を想定する。区間のLagrange多項式はLegendre Vandermonde行列を解いて評価する。
- p≥1のGLL節点は両端±1とPₚ′の根。p+1点GLL求積は2p−1次まで厳密で、次数2pの質量積分は一般には厳密でない。
- 三角形は (0,0),(1,0),(0,1) のP1またはP2のみ。四角形は区間基底のQₚ積で、自由度数は(p+1)²。
節点条件、GLL次数、三角形/積基底の範囲を確認した。

units [specified]:
参照座標と基底は無次元、節点値は表す関数の単位。アフィン区間行列はJ=L/2により M∝J、K∝1/J。
参照座標とアフィン要素の尺度を明示した。

boundary_conditions [not-applicable]:
GLLは端点を含むが、それだけでDirichlet値や要素間の連続性を課すわけではない。境界値・流束・接続は利用側が指定する。
端点節点の存在と物理境界の施行を区別した。

limitations [specified]:
高次数のVandermonde解法は条件数の制約を受け、安定なbarycentric表作成や汎用高次要素の代替ではない。等間隔節点の高次補間にはRunge現象がある。GLL集中質量と厳密質量のrank-1差は重み1・アフィン区間での結果で、三角形全般へ適用しない。
求積精度・条件数・要素族を限定した。

Review: basis.lagrange/lobatto/triangle_lagrange/tensor_basisと、δ補間、導関数・SBP、厳密/集中質量rank-1差、三角形完全性・Q2自由度の既存検査を読んだ。今回は再実行していない。

Not checked:
- 高次数での安定性、任意節点の条件数の新しい測定。
- 曲線要素や一般三角形質量公式への拡張。

Evidence:
- lobatto, lagrange, triangle_lagrange, tensor_basis, element_matrices: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/basis.py
- nodal transform/SBP, mass difference, triangle completeness and Q2 tests: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_basis.py

References:
- [formulation / primary-research] Teukolsky, S. A. (2015). Short note on the mass matrix for Gauss–Lobatto grid points. — https://doi.org/10.1016/j.jcp.2014.12.012
  GLL節点のLagrange基底と、厳密質量行列・対角求積質量行列の差を参照する。三角形一般への公式とはしない。
  full-text (2026-11-22); Author preprint: Section 2, equations (1)–(18), and Section 3.1, equations (19)–(23); journal DOI/year/pages checked against publisher metadata.; https://arxiv.org/html/1412.2276

## Conditions and review scope (en)

problem: Polynomial interpolation/differentiation from nodal values and reference-element matrices.

variant: Interval Lagrange bases via a Legendre Vandermonde solve, GLL/equispaced nodes, explicit triangle P1/P2 and Qₚ products.

use_when:
- Studying nodal degrees of freedom, partition of unity and modal equivalence.
- Comparing quadrature-diagonalized GLL mass with exact mass.

avoid_when:
- Arbitrary-degree triangles, curved elements or large high-degree tabulation.
- Treating GLL diagonal quadrature mass as universally exact.

assumptions [specified]:
- Interval nodes must be distinct finite real values at modest degree; cardinal polynomials are evaluated through a Legendre Vandermonde solve.
- For p≥1, GLL nodes are ±1 and roots of Pₚ′. A p+1-point GLL rule is exact through degree 2p−1, not generally for degree-2p mass products.
- Triangle functions are only P1/P2 on (0,0),(1,0),(0,1). Quadrilaterals use Qₚ tensor products with (p+1)² degrees of freedom.
Checked node conditions, GLL degree and triangle/tensor-product scope.

units [specified]:
Reference coordinates/basis values are dimensionless; nodal values carry the function's units. Affine interval matrices scale as M∝J and K∝1/J with J=L/2.
Specified reference coordinates and affine-element scaling.

boundary_conditions [not-applicable]:
GLL includes endpoints but does not itself enforce Dirichlet values or interelement continuity. The consuming discretization supplies values, fluxes and coupling.
Distinguished endpoint nodes from physical boundary enforcement.

limitations [specified]:
High-degree Vandermonde solves face conditioning limits and are not a replacement for stable barycentric tabulation or a general high-order element library. High-degree equispaced interpolation can exhibit Runge behavior. The rank-one exact/lumped GLL mass difference concerns the unweighted affine interval, not arbitrary triangles.
Scoped quadrature accuracy, conditioning and element families.

Review: Inspected basis.lagrange/lobatto/triangle_lagrange/tensor_basis and existing cardinality, derivative/SBP, exact-versus-lumped mass rank-one, triangle-completeness and Q2-degree-of-freedom tests; no rerun.

Not checked:
- New high-degree stability or arbitrary-node conditioning measurements.
- Extensions to curved elements or general triangle mass formulas.

Evidence:
- lobatto, lagrange, triangle_lagrange, tensor_basis, element_matrices: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/basis.py
- nodal transform/SBP, mass difference, triangle completeness and Q2 tests: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_basis.py

References:
- [formulation / primary-research] Teukolsky, S. A. (2015). Short note on the mass matrix for Gauss–Lobatto grid points. — https://doi.org/10.1016/j.jcp.2014.12.012
  Supports GLL cardinal functions and exact versus quadrature-lumped interval mass; not a universal triangle formula.
  full-text (2026-11-22); Author preprint: Section 2, equations (1)–(18), and Section 3.1, equations (19)–(23); journal DOI/year/pages checked against publisher metadata.; https://arxiv.org/html/1412.2276


- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/basis-functions/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/basis-functions/

- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/basis.py

- Reference: https://doi.org/10.1016/j.jcp.2014.12.012 — GLL nodal cardinal basis and the rank-one difference between exact and quadrature-lumped interval mass matrices; not a universal triangle mass formula.

Common execution records: [{"id": "smooth-function-projection", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=ja#smooth-function-projection-ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=en#smooth-function-projection-en"}}]

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/nodal-basis/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/
