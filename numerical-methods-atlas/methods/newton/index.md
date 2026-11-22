# Armijo-damped Newton / Armijo減衰Newton法

Status: educational-example

Solve F(x)=0 using a Jacobian-based Newton direction and damping that requires sufficient decrease of the residual norm. The example supports a dense or preconditioned GMRES inner solve.

非線形方程式 F(x)=0 を、Jacobianから求めたNewton方向と残差ノルムの十分減少による減衰で解く。公開例は密行列解法または前処理付きGMRESの内部解法を選べる。

Convergence depends on the initial guess, Jacobian nonsingularity and residual scaling; global convergence is not guaranteed. Singular dense solves or preconditioner construction may raise exceptions rather than return a failure reason. No matrix-free Jv, trust region or continuation is provided.

Other names: Newton法, ニュートン法, Newton method, damped Newton, 減衰Newton法, Armijo Newton


## 条件と確認範囲 (ja)

problem: 微分可能な平方の非線形連立方程式 F(x)=0。

variant: 残差ノルムのArmijo型十分減少を用いる減衰Newton。内部線形解法はdenseまたはGMRESで、Jacobianは明示指定。

use_when:
- Jacobianを与えられ、根の候補に近い初期値があるとき。
- 非線形問題で線形解法の誤差と減衰の作用を分けて確認するとき。

avoid_when:
- Jacobianが特異になる点や、解が複数ある問題を初期値依存なしに解きたい場合。
- 制約付き最適化やJacobianなしの巨大問題をこのまま解く場合。

assumptions [specified]:
- FとJacobianを利用者が与える。平方の微分可能な系と、解の近くで非特異なJacobianが基本となる。
- 長さ1から1/2ずつ減らし、||F(x+αs)||₂ ≤ (1−10⁻⁴α)||F(x)||₂ を要求する。α<2⁻²⁰で失敗を返す。
- GMRES経路でもJacobianは明示的に与える。CSRならILU(0)、それ以外ならJacobi前処理を使い、内部残差と外部絶対残差を区別する。
受理不等式、半減、Jacobianと内部解法を確認した。

units [specified]:
固有の物理単位はなく、未知数・残差の尺度は呼び出し側が決める。単位・桁の違う残差成分を自動で無次元化しないため、ノルムと絶対許容誤差を使う前に尺度を揃える。
ソルバーによる尺度変換はなく絶対ノルムを使う。

boundary_conditions [not-applicable]:
Newton法自体に物理境界はない。境界はFとJacobianの組立て側が指定する。既存Bratu検査は [0,1] の両端零Dirichletを内部未知数の残差へ組み込む。
境界は残差とJacobianの定義に属する。

limitations [specified]:
初期値、Jacobianの非特異性、残差の尺度に依存し、大域的収束は保証しない。特異な密行列解法や前処理構築は例外となることがあり、すべてが失敗理由の戻り値に変換されるわけではない。行列なしJv、信頼領域、継続法は備えない。
失敗理由と例外が返る経路を区別した。

Review: krylov.newtonと、立方関数での後退・反復上限、1次元BratuのNewton–GMRES格子細分化を扱う既存検査定義を読んだ。今回は再実行していない。

Not checked:
- 一般初期値からの大域的収束、特異点や分岐への対応。
- 実装固有の内部許容誤差が文献の収束定理を満たすことの証明。

Evidence:
- newton: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/krylov.py
- test_damped_newton_backtracks_and_reports_failure; test_bratu_newton_krylov_refines_to_continuous_reference: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_sparse_fem.py

References:
- [adopted-variant / primary-research] Armijo, L. (1966). Minimization of functions having Lipschitz continuous first partial derivatives. — https://doi.org/10.2140/pjm.1966.16.1
  十分減少と刻みの半減という考え方の根拠。原論文の最小化の収束定理を、この非線形方程式実装の保証とはしない。
  full-text (2026-11-22); Printed pp. 1–3; convergence theorem and Corollary 2, equation (2).; https://msp.org/pjm/1966/16-1/pjm-v16-n1-p01-s.pdf
- [formulation / primary-research] Dembo, R. S., Eisenstat, S. C. & Steihaug, T. (1982). Inexact Newton Methods. — https://doi.org/10.1137/0719025
  Newton方程式を近似的に解く定式化。今回確認したのは抄録であり、実装固有の内部許容誤差の定理適合は未確認。
  abstract-and-metadata (2026-11-22); Publisher abstract and bibliographic metadata, as returned by web search; direct full text not reviewed.; https://epubs.siam.org/doi/abs/10.1137/0719025

## Conditions and review scope (en)

problem: A differentiable square nonlinear system F(x)=0.

variant: Damped Newton with an Armijo-type residual-norm decrease test; explicit Jacobian and dense/GMRES inner solve.

use_when:
- A Jacobian and an initial guess near a candidate root are available.
- Examining the separate effects of inner linear accuracy and damping.

avoid_when:
- Requiring initial-guess-independent results near singular Jacobians or multiple roots.
- Direct use for constrained optimization or very large Jacobian-free problems.

assumptions [specified]:
- The caller supplies F and its Jacobian; the basic setting is a square differentiable system with a nonsingular Jacobian near the root.
- Starting at one, the step is halved until ||F(x+αs)||₂ ≤ (1−10⁻⁴α)||F(x)||₂; failure is returned below α=2⁻²⁰.
- The GMRES path still uses an explicitly supplied Jacobian; CSR uses ILU(0), otherwise Jacobi preconditioning. Inner and outer absolute residual criteria differ.
Inspected the acceptance inequality, halving, Jacobian and inner solvers.

units [specified]:
No intrinsic physical unit; the caller defines unknown and residual scales. Components are not nondimensionalized automatically, so scale them consistently before using the norm and absolute tolerance.
No automatic scaling; the solver uses an absolute norm.

boundary_conditions [not-applicable]:
Newton has no intrinsic physical boundary. F/Jacobian assembly supplies it; the existing Bratu test encodes zero Dirichlet values at both ends of [0,1].
Boundaries belong to the supplied residual/Jacobian.

limitations [specified]:
Convergence depends on the initial guess, Jacobian nonsingularity and residual scaling; global convergence is not guaranteed. Singular dense solves or preconditioner construction may raise exceptions rather than return a failure reason. No matrix-free Jv, trust region or continuation is provided.
Distinguished returned failures from exception paths.

Review: Inspected krylov.newton and existing cubic backtracking/iteration-limit and 1D Bratu Newton–GMRES refinement tests; no rerun.

Not checked:
- Global convergence, singular points and bifurcations.
- Proof that the implemented inner tolerance satisfies a particular literature convergence theorem.

Evidence:
- newton: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/krylov.py
- test_damped_newton_backtracks_and_reports_failure; test_bratu_newton_krylov_refines_to_continuous_reference: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_sparse_fem.py

References:
- [adopted-variant / primary-research] Armijo, L. (1966). Minimization of functions having Lipschitz continuous first partial derivatives. — https://doi.org/10.2140/pjm.1966.16.1
  Supports sufficient decrease and step halving; the minimization theorem is not a convergence certificate for this root solver.
  full-text (2026-11-22); Printed pp. 1–3; convergence theorem and Corollary 2, equation (2).; https://msp.org/pjm/1966/16-1/pjm-v16-n1-p01-s.pdf
- [formulation / primary-research] Dembo, R. S., Eisenstat, S. C. & Steihaug, T. (1982). Inexact Newton Methods. — https://doi.org/10.1137/0719025
  Formulates approximate Newton solves; only the abstract was reviewed, not a theorem audit of the implemented inner tolerance.
  abstract-and-metadata (2026-11-22); Publisher abstract and bibliographic metadata, as returned by web search; direct full text not reviewed.; https://epubs.siam.org/doi/abs/10.1137/0719025


- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/sparse-nonlinear/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/sparse-nonlinear/

- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/krylov.py

- Reference: https://doi.org/10.2140/pjm.1966.16.1 — Source for sufficient-decrease and halving-backtracking ideas; the atlas adapts the test to ||F||, not to the paper's steepest-descent problem.
- Reference: https://doi.org/10.1137/0719025 — Newton equations and approximate inner linear solves; context for the GMRES path, not proof of the atlas's particular forcing rule.

Common execution records: [{"id": "bratu", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=ja#bratu-ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=en#bratu-en"}}]

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/
