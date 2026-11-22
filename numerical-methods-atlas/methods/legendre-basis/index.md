# Legendre modal basis / orthonormal scaling / Legendreモード基底・正規直交化

Status: educational-example

Represent reference-interval functions in Legendre modes. The implementation tabulates P₀…Pₚ and derivatives, optionally normalizes them, and computes unweighted L2 projection and affine element matrices by Gauss quadrature.

参照区間 [−1,1] の関数をLegendre多項式のモードで表す。公開実装はP₀からPₚ、微分、任意の直交規格化、Gauss求積による重み1のL2射影とアフィン要素行列を扱う。

Educational tabulation for modest degrees, without high-degree stability/performance guarantees. Discontinuities limit single-polynomial approximation and quadrature. Do not confuse Chebyshev weights with the unit Legendre weight, or GLL quadrature's highest-mode mass with exact mass.

Other names: Legendre基底, Legendre polynomials, ルジャンドル基底, ルジャンドル多項式


## 条件と確認範囲 (ja)

problem: 区間上の関数の多項式表現、L2射影、要素積分。

variant: 重み1のLegendreモードと任意のL2直交規格化。NumPyのLegendre評価とGauss求積を使用。

use_when:
- モード係数と節点値の違いや直交性を確かめるとき。
- 滑らかな区間関数の射影や定係数アフィン要素の行列を作るとき。

avoid_when:
- 曲線写像・可変係数でも同じ少数求積点で厳密積分できると期待する場合。
- 不連続点をまたぐGauss求積だけで高精度を保証したい場合。

assumptions [specified]:
- 参照区間 [−1,1]、重み1の内積を採用する。∫PⱼPₖdξ=2δⱼₖ/(2k+1)、orthonormal指定時は√((2k+1)/2)を掛ける。
- degreeは0以上の整数。project_legendreはGauss求積で射影積分を近似するため、一般関数に対して求積誤差も残る。
- element_matricesの厳密求積指定は定係数・アフィン写像下の多項式積を対象とし、p+1点Gaussを使う。
規格化、重み、次数、Gauss求積を確認した。

units [specified]:
ξと基底は無次元。長さLのアフィン区間ではJ=L/2で、質量行列にJ、勾配の剛性行列に1/Jを掛ける。展開係数は表す関数と同じ単位。
参照区間とアフィンJacobianの尺度を明記した。

boundary_conditions [not-applicable]:
基底の評価・射影自体は物理境界を課さない。端点の値や流束、隣接要素の接続は利用する離散化側が指定する。剛性行列の定数モードの零空間も自動で除かない。
基底評価は物理境界の施行ではない。

limitations [specified]:
中程度の次数向けの教育用表作成で、高次数での安定性・最適化を保証しない。不連続関数では単一多項式の収束と求積が制約される。Chebyshev基底の重みをLegendreの重み1と混同せず、GLL求積による最高モードの質量を厳密質量と同一視しない。
次数・不連続性・求積の制約を記述した。

Review: basis.legendre、project_legendre、element_matricesと、規格化・直交性、射影、区分積分、写像尺度を扱う既存検査を読んだ。今回は再実行していない。

Not checked:
- 高次数での条件数や丸め誤差の新しい測定。
- 一般関数の射影誤差の保証や曲線要素への拡張。

Evidence:
- legendre, project_legendre, element_matrices: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/basis.py
- orthogonality/normalization, projection and affine-mapping tests: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_basis.py

References:
- [formulation / primary-research] Teukolsky, S. A. (2015). Short note on the mass matrix for Gauss–Lobatto grid points. — https://doi.org/10.1016/j.jcp.2014.12.012
  重み1のLegendre展開・規格化と節点値との変換を参照する。Legendre多項式の歴史的起源の主張には用いない。
  full-text (2026-11-22); Author preprint: Section 2, equations (1)–(18), and Section 3.1, equations (19)–(23); journal DOI/year/pages checked against publisher metadata.; https://arxiv.org/html/1412.2276

## Conditions and review scope (en)

problem: Polynomial representation, L2 projection and element integration on an interval.

variant: Unweighted Legendre modes with optional unit-L2 normalization, using NumPy Legendre evaluation and Gauss quadrature.

use_when:
- Examining modal coefficients versus nodal values and orthogonality.
- Projecting smooth interval functions or constructing constant-coefficient affine element matrices.

avoid_when:
- Expecting the same low-order quadrature to remain exact with curved maps or variable coefficients.
- Relying on unsplit Gauss quadrature across a jump for guaranteed high accuracy.

assumptions [specified]:
- The reference interval is [−1,1] with weight one: ∫PⱼPₖdξ=2δⱼₖ/(2k+1); orthonormal=True multiplies by √((2k+1)/2).
- Degree is a nonnegative integer. project_legendre approximates projection integrals by Gauss quadrature, leaving quadrature error for general functions.
- Exact element-matrix quadrature means p+1 Gauss points for polynomial products with constant coefficients and an affine map.
Checked normalization, weight, degree and Gauss quadrature.

units [specified]:
ξ and basis values are dimensionless. On an affine interval of length L, J=L/2 scales mass by J and gradient stiffness by 1/J. Expansion coefficients share the represented function's units.
Specified reference coordinates and affine-Jacobian scaling.

boundary_conditions [not-applicable]:
Basis evaluation/projection imposes no physical boundary condition. Endpoint values/fluxes and interelement coupling belong to the consuming discretization; the constant stiffness nullspace is not removed automatically.
Basis evaluation does not impose physical boundaries.

limitations [specified]:
Educational tabulation for modest degrees, without high-degree stability/performance guarantees. Discontinuities limit single-polynomial approximation and quadrature. Do not confuse Chebyshev weights with the unit Legendre weight, or GLL quadrature's highest-mode mass with exact mass.
Specified degree, discontinuity and quadrature limits.

Review: Inspected basis.legendre, project_legendre, element_matrices and existing normalization, orthogonality, projection, split-integration and affine-scaling tests; no rerun.

Not checked:
- New high-degree conditioning or rounding-error measurements.
- Error guarantees for arbitrary function projection or curved-element extensions.

Evidence:
- legendre, project_legendre, element_matrices: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/basis.py
- orthogonality/normalization, projection and affine-mapping tests: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_basis.py

References:
- [formulation / primary-research] Teukolsky, S. A. (2015). Short note on the mass matrix for Gauss–Lobatto grid points. — https://doi.org/10.1016/j.jcp.2014.12.012
  Supports unweighted Legendre normalization and modal/nodal transforms, without claiming historical origin.
  full-text (2026-11-22); Author preprint: Section 2, equations (1)–(18), and Section 3.1, equations (19)–(23); journal DOI/year/pages checked against publisher metadata.; https://arxiv.org/html/1412.2276


- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/basis-functions/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/basis-functions/

- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/basis.py

- Reference: https://doi.org/10.1016/j.jcp.2014.12.012 — Legendre modal expansion, unweighted normalization and modal/nodal transforms; a modern formulation, not a historical-origin attribution.

Common execution records: [{"id": "smooth-function-projection", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=ja#smooth-function-projection-ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=en#smooth-function-projection-en"}}]

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/legendre-basis/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/
