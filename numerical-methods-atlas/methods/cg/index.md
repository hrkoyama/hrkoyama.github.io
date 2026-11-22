# Conjugate gradients / 共役勾配法

Status: educational-example

Solve real SPD linear systems by conjugate directions. The public example is unpreconditioned matrix-free CG for the five-point zero-Dirichlet Poisson operator on a unit square.

実対称正定値な連立一次方程式を共役方向で反復的に解く。公開例は単位正方形・零Dirichlet Poisson方程式の五点差分を、行列を組み立てずに扱う前処理なしCG。

Do not apply this variant directly to nonsymmetric, indefinite or singular systems. This CG example has no preconditioner, general sparse-matrix interface or pure-Neumann nullspace handling. A small residual does not certify discretization accuracy; rapid termination for one eigenmode is not a general performance result.

Other names: CG法, conjugate gradient, conjugate gradient method, 共役勾配, 共役勾配法


## 条件と確認範囲 (ja)

problem: Poisson方程式の離散化などから得られる、実対称正定値系 Ax=b。

variant: 五点差分作用素を直接適用する前処理なしの線形CG。共通比較経路では各反復で真の残差を再計算する。

use_when:
- SPDが分かっている離散系で、行列積だけから解を求めたいとき。
- 同じ格子・右辺・真の残差基準で他のPoisson解法と比較するとき。

avoid_when:
- 移流による非対称系、鞍点系、零空間を残した周期・Neumann系。
- 反復回数だけで計算時間や連続解の精度を保証したい場合。

assumptions [specified]:
- 作用素は実対称正定値で、右辺は有限。ここでは定係数の −Δu=f を一様正方格子で離散化する。
- 内積は配列成分のEuclidean内積。既存実装の初期値は零で、前処理は用いない。
- poisson_comparison.solve は再計算した真の相対残差を停止に使う。linear.poisson_2d は反復残差と tolerance×max(1,初期残差) を使う。
CGの再帰式、前処理の有無、二つの停止条件をコードで区別した。

units [specified]:
CG自体に固有の物理単位はない。公開Poisson例は長さ1の無次元座標で、次元を与えるなら [f]=[u]/[長さ]²。残差は格子体積で重み付けしない配列ノルム。
単位正方形と配列ノルムの規約を明記した。

boundary_conditions [not-applicable]:
代数解法としてのCGは境界を定めない。公開2次元Poisson例は [0,1]² の全辺で u=0 をゼロ埋め込みにより課す。
CGの固有要件ではない。公開例の零Dirichlet条件は別途明記した。

limitations [specified]:
非対称・不定・特異な系にそのまま適用しない。前処理、一般疎行列入力、純Neumannの零空間処理はこのCG例にはない。小さい残差は離散化誤差の保証ではなく、単一固有モードの速い終了を一般的性能と解釈しない。
SPDの要件と既存例の範囲に限定した。

Review: linear.poisson_2d、poisson_comparison.solve、既存の一般右辺の離散残差・共通残差基準・単一モードの検査定義を読んだ。今回は再実行していない。

Not checked:
- 一般SPD行列に対する性能・条件数依存の新しい測定。
- 前処理付きCGや非SPD拡張。

Evidence:
- poisson_2d: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/linear.py
- solve(method='cg'), problem: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/poisson_comparison.py
- test_poisson_cg_for_general_forcing_satisfies_discrete_residual: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_linear.py
- matched true-residual and single-mode tests: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_poisson_comparison.py

References:
- [original-method / primary-research] Hestenes, M. R. & Stiefel, E. (1952). Methods of Conjugate Gradients for Solving Linear Systems. — https://doi.org/10.6028/jres.049.044
  実対称正定値系に対するCGの反復式と、丸め誤差がある場合の有限回終了の限界。
  full-text (2026-11-22); Sections 2–3, especially (3:1) and the discussion of rounding error, pp. 410–411.; https://nvlpubs.nist.gov/nistpubs/jres/049/6/v49.n06.a08.pdf

## Conditions and review scope (en)

problem: Real SPD systems Ax=b, including a discrete Poisson equation.

variant: Unpreconditioned linear CG with a matrix-free five-point operator; the comparison path recomputes the true residual each iteration.

use_when:
- The discretized system is known to be SPD and a matrix-free solve is desired.
- Comparing Poisson solvers on the same grid, forcing and true-residual criterion.

avoid_when:
- Nonsymmetric advection systems, saddle-point systems or periodic/Neumann systems with an untreated nullspace.
- Claims about runtime or continuous-solution accuracy based only on iteration count.

assumptions [specified]:
- The operator must be real SPD and the right-hand side finite; the example discretizes constant-coefficient −Δu=f on a uniform square grid.
- Inner products are Euclidean array products; the current implementation starts from zero and has no preconditioner.
- poisson_comparison.solve stops on a recomputed true relative residual; linear.poisson_2d uses a recurrence residual with tolerance×max(1,initial residual).
Inspected the CG recurrence, absence of preconditioning and two stopping rules.

units [specified]:
CG has no intrinsic physical unit. The public Poisson coordinates have unit dimensionless length; dimensionally [f]=[u]/[length]². Residual norms are unweighted array norms.
Specified the unit-square and array-norm conventions.

boundary_conditions [not-applicable]:
CG itself supplies no physical boundary condition. The public 2D Poisson examples impose u=0 on every side of [0,1]² by zero padding.
Not intrinsic to CG; the examples' zero-Dirichlet condition is separately stated.

limitations [specified]:
Do not apply this variant directly to nonsymmetric, indefinite or singular systems. This CG example has no preconditioner, general sparse-matrix interface or pure-Neumann nullspace handling. A small residual does not certify discretization accuracy; rapid termination for one eigenmode is not a general performance result.
Limited the claim to the SPD requirement and existing examples.

Review: Inspected linear.poisson_2d, poisson_comparison.solve and existing tests for general-forcing discrete residuals, matched stopping criteria and the single-mode case; no rerun.

Not checked:
- New general-SPD performance or condition-number measurements.
- Preconditioned CG or non-SPD extensions.

Evidence:
- poisson_2d: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/linear.py
- solve(method='cg'), problem: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/poisson_comparison.py
- test_poisson_cg_for_general_forcing_satisfies_discrete_residual: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_linear.py
- matched true-residual and single-mode tests: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_poisson_comparison.py

References:
- [original-method / primary-research] Hestenes, M. R. & Stiefel, E. (1952). Methods of Conjugate Gradients for Solving Linear Systems. — https://doi.org/10.6028/jres.049.044
  CG recurrence for real SPD systems and the qualification of finite termination in floating-point arithmetic.
  full-text (2026-11-22); Sections 2–3, especially (3:1) and the discussion of rounding error, pp. 410–411.; https://nvlpubs.nist.gov/nistpubs/jres/049/6/v49.n06.a08.pdf


- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/elliptic/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/elliptic/

- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/linear.py
- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/multigrid.py
- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/poisson_comparison.py

- Reference: https://doi.org/10.6028/jres.049.044 — Real SPD conjugate-gradient recurrence; not the heat time integrator used elsewhere in the chapter.

Common execution records: [{"id": "poisson-2d-sine", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=ja#poisson-2d-sine-ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=en#poisson-2d-sine-en"}}]

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/cg/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/
