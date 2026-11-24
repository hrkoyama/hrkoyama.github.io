# Armijo-damped Newton / Armijo減衰Newton法

Status: educational-example

Solve F(x)=0 using a Jacobian-based Newton direction and damping that requires sufficient decrease of the residual norm. The example supports a dense or preconditioned GMRES inner solve. Additional fixed examples: Crossing the Bratu fold with pseudo-arclength continuation. See each release for assumptions and checked scope. Additional fixed examples: Line search and trust regions from the same difficult starts. See each release for assumptions and checked scope. Additional fixed examples: Bratu sensitivity near the discrete fold, Matrix-free VJP for distributed Bratu coefficients. See each release for assumptions and checked scope. Additional fixed examples: Robertson kinetics: initial stiffness and actual error, Van der Pol: an early stiffness transition. See each release for assumptions and checked scope. Additional fixed examples: Consistent initialization and discrete residuals for an index-one DAE, Robertson conservation DAE and stored official IDA values. See each release for assumptions and checked scope. Fixed educational executions: Enzyme conservation and QSSA.

非線形方程式 F(x)=0 を、Jacobianから求めたNewton方向と残差ノルムの十分減少による減衰で解く。公開例は密行列解法または前処理付きGMRESの内部解法を選べる。 追加固定例：擬似弧長継続でBratuのfoldを越える。条件と検証範囲は各配布版で確認してください。 追加固定例：同じ難しい初期値に対する線探索と信頼領域。条件と検証範囲は各配布版で確認してください。 追加固定例：離散fold近傍のBratu感度、分布係数Bratuの行列非形成VJP。条件と検証範囲は各配布版で確認してください。 追加固定例：Robertson反応系の初期剛性と実誤差、van der Polの短時間剛性遷移。条件と検証範囲は各配布版で確認してください。 追加固定例：index-1 DAEの整合初期化と離散残差、Robertson保存制約DAEと公式IDA保存値。条件と検証範囲は各配布版で確認してください。 固定した教育用実行例：酵素反応の保存と準定常近似。

Convergence depends on the initial guess, Jacobian nonsingularity and residual scaling; global convergence is not guaranteed. Singular dense solves or preconditioner construction may raise exceptions rather than return a failure reason. No matrix-free Jv, trust region or continuation is provided. Additional fixed examples: A small one-dimensional simple fold only. The whole-curve family comparison uses the computed midpoint as its family coordinate and is distinct from the independent fixed-lambda profile checks. The continuum fold is not an exact discrete solution. No general bifurcation-tracking or large-scale performance claim. The preceding limitations describe earlier editions. This additional release: No all-start guarantee, universal method ranking or equivalence to PETSc implementation. The preceding limitations describe earlier editions. This additional release: The continuum fold is not the discrete fold. rtol1e-4/1e-8 targets are required; requested1e-12 is observational and unmet is never called converged. Independent accuracy of the returned gradient is a separate gate. Eigenvalue/roundoff scales are floating diagnostics, not certified intervals. Bratu J is symmetric; the nonsymmetric transpose is a separate operator control. The retained /solver/gmres/retention_adaptation text is historicalR1/R2;the newcontract explicitly overrides it for mixed-precisionSTATEsolves. ProjectedUNMET is separatelysaved. Derivative verification at the same discrete state, not independent physical-PDE truth or general AD. Persistent arrays and fixed Krylov workspace inventories are not RSS measurements. For m=2, theta endpoints are[a-b-2,a+b-2], distinct from physical coefficient endpoints[a-b,a+b]. The retained /solver/gmres/retention_adaptation text is historicalR1/R2;the newcontract explicitly overrides it for mixed-precisionSTATEsolves. ProjectedUNMET is separatelysaved. The preceding limitations describe earlier editions. This additional release: Conservation and positivity are observations for these inputs, not universal guarantees. Accuracy is sampled on T <= 0.4; this does not validate long-time chemistry or an all-time error bound. This post-measurement reporting revision is not a numerical repair. The first error, 4.535633779e-5, exceeded the original 2e-5 goal. Local tolerances do not guarantee global accuracy, and reporting PASS does not mean all original goals were met. Full large-mu cycles are outside scope. The preceding limitations describe earlier editions. This additional release: One authored positive branch and fixed BE runs; no IDA execution or general DAE-solver qualification. Only two official SUNDIALS v7.1.1 printed rows; zero new IDA executions, with no long-time chemistry or general DAE-performance claim. No asymptotic-convergence or all-original-accuracy-goals claim is made for this fixed schedule.

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
初期値、Jacobianの非特異性、残差の尺度に依存し、大域的収束は保証しない。特異な密行列解法や前処理構築は例外となることがあり、すべてが失敗理由の戻り値に変換されるわけではない。行列なしJv、信頼領域、継続法は備えない。 追加固定例：小さな1次元の単純foldだけです。分岐曲線の解析族比較では計算した中点値を族の座標に使い、固定λの独立形状比較と区別します。連続foldは離散解そのものではなく、一般の分岐追跡や大規模性能は保証しません。 上記の制限は既存配布版の範囲です。今回の追加配布版：全初期値の成功や手法の普遍的優越、PETSc実装との一致を保証しません。 上記の制限は既存配布版の範囲です。今回の追加配布版：連続foldは離散foldではありません。rtol1e-4/1e-8は達成必須、requested1e-12は観測のみで未達を収束と表示しません。返却候補の独立勾配精度は別判定。最小固有値/丸めscaleは浮動小数点の診断で保証区間ではありません。BratuのJは対称であり、非対称転置は別の演算子対照です。 inputsの/solver/gmres/retention_adaptationはR1/R2の履歴記述で、現状態解法は新契約の明示混合精度が上書きします。射影解の未達は別保存します。 同じ離散状態の微分検証で、独立した物理PDE解の証明や一般ADではありません。保存arrayと固定Krylov workspaceの記録はRSS測定ではありません。m=2のθ端点は[a-b-2,a+b-2]で、物理係数端点[a-b,a+b]と区別します。 inputsの/solver/gmres/retention_adaptationはR1/R2の履歴記述で、現状態解法は新契約の明示混合精度が上書きします。射影解の未達は別保存します。 上記の制限は既存配布版の範囲です。今回の追加配布版：保存/正値性は固定入力の観測で、一般的な保証ではありません。T=.4の短時間・標本時刻での精度であり、長時間化学精度や全時刻誤差上限は主張しません。 測定後の報告範囲変更で、数値的な修復ではありません。初回誤差4.535633779e-5は元目標2e-5を超えます。局所rtolは大域誤差を保証せず、報告検証の合格は全元目標の達成ではありません。大μ全周期は対象外です。 上記の制限は既存配布版の範囲です。今回の追加配布版：単一の製造正枝・固定BE計算です。IDA実行や一般DAEソルバーの検証ではありません。 公式SUNDIALS v7.1.1の2印字行のみ。IDAの新規実行0、長時間の化学精度や一般DAE性能は扱いません。 この固定時間格子の漸近収束や元精度目標の全合格は主張しません。
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
Convergence depends on the initial guess, Jacobian nonsingularity and residual scaling; global convergence is not guaranteed. Singular dense solves or preconditioner construction may raise exceptions rather than return a failure reason. No matrix-free Jv, trust region or continuation is provided. Additional fixed examples: A small one-dimensional simple fold only. The whole-curve family comparison uses the computed midpoint as its family coordinate and is distinct from the independent fixed-lambda profile checks. The continuum fold is not an exact discrete solution. No general bifurcation-tracking or large-scale performance claim. The preceding limitations describe earlier editions. This additional release: No all-start guarantee, universal method ranking or equivalence to PETSc implementation. The preceding limitations describe earlier editions. This additional release: The continuum fold is not the discrete fold. rtol1e-4/1e-8 targets are required; requested1e-12 is observational and unmet is never called converged. Independent accuracy of the returned gradient is a separate gate. Eigenvalue/roundoff scales are floating diagnostics, not certified intervals. Bratu J is symmetric; the nonsymmetric transpose is a separate operator control. The retained /solver/gmres/retention_adaptation text is historicalR1/R2;the newcontract explicitly overrides it for mixed-precisionSTATEsolves. ProjectedUNMET is separatelysaved. Derivative verification at the same discrete state, not independent physical-PDE truth or general AD. Persistent arrays and fixed Krylov workspace inventories are not RSS measurements. For m=2, theta endpoints are[a-b-2,a+b-2], distinct from physical coefficient endpoints[a-b,a+b]. The retained /solver/gmres/retention_adaptation text is historicalR1/R2;the newcontract explicitly overrides it for mixed-precisionSTATEsolves. ProjectedUNMET is separatelysaved. The preceding limitations describe earlier editions. This additional release: Conservation and positivity are observations for these inputs, not universal guarantees. Accuracy is sampled on T <= 0.4; this does not validate long-time chemistry or an all-time error bound. This post-measurement reporting revision is not a numerical repair. The first error, 4.535633779e-5, exceeded the original 2e-5 goal. Local tolerances do not guarantee global accuracy, and reporting PASS does not mean all original goals were met. Full large-mu cycles are outside scope. The preceding limitations describe earlier editions. This additional release: One authored positive branch and fixed BE runs; no IDA execution or general DAE-solver qualification. Only two official SUNDIALS v7.1.1 printed rows; zero new IDA executions, with no long-time chemistry or general DAE-performance claim. No asymptotic-convergence or all-original-accuracy-goals claim is made for this fixed schedule.
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

## Small fixed-input validation supplements

Additional fixed examples: Crossing the Bratu fold with pseudo-arclength continuation. See each release for assumptions and checked scope. A small one-dimensional simple fold only. The whole-curve family comparison uses the computed midpoint as its family coordinate and is distinct from the independent fixed-lambda profile checks. The continuum fold is not an exact discrete solution. No general bifurcation-tracking or large-scale performance claim.

追加固定例：擬似弧長継続でBratuのfoldを越える。条件と検証範囲は各配布版で確認してください。 小さな1次元の単純foldだけです。分岐曲線の解析族比較では計算した中点値を族の座標に使い、固定λの独立形状比較と区別します。連続foldは離散解そのものではなく、一般の分岐追跡や大規模性能は保証しません。

- Crossing the Bratu fold with pseudo-arclength continuation: https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-continuation/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/atlas-bratu-continuation-jfnk-2026-11-24-r2.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/results/result.json

- Line search and trust regions from the same difficult starts: https://hrkoyama.github.io/numerical-methods-atlas/validation/globalization-difficult-starts/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/atlas-globalization-controls-2026-11-24.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/results/result.json

- Bratu sensitivity near the discrete fold: https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-sensitivity/
- Matrix-free VJP for distributed Bratu coefficients: https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-distributed-vjp/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/atlas-adjoint-2026-11-24.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/results/result.json

- Robertson kinetics: initial stiffness and actual error: https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-stiff-kinetics/
- Van der Pol: an early stiffness transition: https://hrkoyama.github.io/numerical-methods-atlas/validation/van-der-pol-stiff-transition/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/atlas-ode-adaptivity-2026-11-24-r2.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/result.json

- Consistent initialization and discrete residuals for an index-one DAE: https://hrkoyama.github.io/numerical-methods-atlas/validation/index1-dae-consistent-initialization/
- Robertson conservation DAE and stored official IDA values: https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-conservation-dae/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/atlas-dae-controls-2026-11-24.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/result.json

- Enzyme conservation and QSSA: https://hrkoyama.github.io/numerical-methods-atlas/validation/enzyme-qssa/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/atlas-small-models-2026-11-25.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/result.json

Common execution records: [{"id": "bratu", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=ja#bratu-ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=en#bratu-en"}}, {"id": "bratu-fold-continuation", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-continuation/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-continuation/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "globalization-difficult-starts", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/globalization-difficult-starts/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/globalization-difficult-starts/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "bratu-fold-sensitivity", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-sensitivity/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-sensitivity/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "bratu-distributed-vjp", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-distributed-vjp/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-distributed-vjp/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "robertson-stiff-kinetics", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-stiff-kinetics/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-stiff-kinetics/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "van-der-pol-stiff-transition", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/van-der-pol-stiff-transition/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/van-der-pol-stiff-transition/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "index1-dae-consistent-initialization", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/index1-dae-consistent-initialization/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/index1-dae-consistent-initialization/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "robertson-conservation-dae", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-conservation-dae/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-conservation-dae/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "enzyme-qssa", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/enzyme-qssa/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/enzyme-qssa/?lang=en"}, "kind": "dedicated-supplement"}]

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [Bratu非線形境界値問題](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bratu-ja) (`bratu`; bratu, bratu-fold-continuation, globalization-difficult-starts, bratu-fold-sensitivity, bratu-distributed-vjp)
- [有限次元非線形写像・根と微分作用](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#finite-dimensional-nonlinear-map-ja) (`finite-dimensional-nonlinear-map`; globalization-difficult-starts)
- [Robertson反応系](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#robertson-kinetics-ja) (`robertson-kinetics`; robertson-stiff-kinetics)
- [半陽的index-1 DAE](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#index-one-dae-ja) (`index-one-dae`; robertson-stiff-kinetics, index1-dae-consistent-initialization)
- [van der Pol振動子](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#van-der-pol-ja) (`van-der-pol`; van-der-pol-stiff-transition)
- [Michaelis–Mentenと完全酵素反応系](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-enzyme-ja) (`bio-enzyme`; enzyme-qssa)

#### 問題の図 (`method-problems-ja`)

##### [1次元Bratu非線形境界値問題](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu/?lang=ja) (`bratu`)

![公開コード版を固定条件で実行して作成した計算結果。条件・値・検査結果を添付。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/bratu.png)

共通実行例では減衰Newton法で前進の境界値問題を解きます。関連する自動微分・感度・随伴・係数推定の検証は各手法の別配布版へ進めます。感度・逆問題（1個または2個の係数）の入力と判定は別であり、共通の前進実行例に合算しません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu/?lang=ja#code-ja)

- [1次元Bratu：小さい枝のNewton–GMRES](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/bratu/?lang=ja) (`bratu`) · [コードZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

−u''=λexp(u)、β=1・λ=2β²/cosh²(β/2)の小さい枝を零初期値から解く。31/63/127内部点で解析解、独立に再評価した非線形残差、2次格子収束を確認する。

##### [減衰Newton法による3次方程式の求根](https://hrkoyama.github.io/numerical-methods-atlas/problems/cubic-root/?lang=ja) (`cubic-root`)

![公開コード版を固定条件で実行して作成した計算結果。条件・値・検査結果を添付。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/cubic-root.png)

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/cubic-root/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/cubic-root/?lang=ja#code-ja)

この手法でこの問題を解く固定入力実行例は未登録です。

##### [擬似弧長継続でBratuのfoldを越える](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-continuation/?lang=ja) (`bratu-fold-continuation`)

![保存した分岐曲線、λ=2の上下枝、Jacobianの最小特異値、3格子のfold誤差を示す縮小図。擬似弧長stepは物理時間ではありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/results/bratu-fold-continuation-preview.png)

hΣdu²+dλ²の重み付き単位接線、予測点と接線超平面によるNewton補正。別の拡大系でfoldと正規化null vectorを解きます。このcaseは疎Jacobianを明示的に組み立てます。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-continuation/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-continuation/?lang=ja#code-ja)

- [擬似弧長継続でBratuのfoldを越える](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-continuation/?lang=ja) (`bratu-fold-continuation`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/atlas-bratu-continuation-jfnk-2026-11-24-r2.zip)

同じ1次元Bratu境界値問題の下枝から上枝までを追跡し、接線・fold・独立解析族との空間誤差を調べます。

##### [同じ難しい初期値に対する線探索と信頼領域](https://hrkoyama.github.io/numerical-methods-atlas/problems/globalization-difficult-starts/?lang=ja) (`globalization-difficult-starts`)

![同一初期値の保存経路、原残差、trust radiusと実測評価回数。失敗・非収束は別記します。 図の座標は有限次元の変数・反復・診断で、物理空間の次元やPDE境界を表しません。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/results/globalization-difficult-starts-preview.png)

原残差とスケール付きmeritを分離し、Euclidean doglegと全試行ledgerを保存します。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/globalization-difficult-starts/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/globalization-difficult-starts/?lang=ja#code-ja)

- [同じ難しい初期値に対する線探索と信頼領域](https://hrkoyama.github.io/numerical-methods-atlas/validation/globalization-difficult-starts/?lang=ja) (`globalization-difficult-starts`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/atlas-globalization-controls-2026-11-24.zip)

同じ固定初期値からNewton・Armijo・doglegを比較し、真の根と非根停留・予算終了を区別します。

##### [離散fold近傍のBratu感度](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-sensitivity/?lang=ja) (`bratu-fold-sensitivity`)

![離散fold近傍のBratu感度。実際の保存数値データの縮小図で、1次元問題です。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/results/bratu-fold-sensitivity-preview.png)

解析Jv、Poisson-Thomas右前処理、固定GMRES本体で接線と随伴を解きます。全rtol・最終候補・true residual・終了状態・丸めscaleを保存します。shootingと別の高精度Thomas-Newtonで離散参照を資格します。 R2は同じfloat64の隣接差を先に取る一般Jvで、元の非線形残差・GMRES・許容差は変更しません。 R3は状態Newton補正だけをhi+loで保持し、直接9積残差と3積状態更新を使います。物理状態はfloat64、感度/随伴GMRESは旧方式です。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-sensitivity/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-sensitivity/?lang=ja#code-ja)

- [離散fold近傍のBratu感度](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-sensitivity/?lang=ja) (`bratu-fold-sensitivity`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/atlas-adjoint-2026-11-24.zip)

離散Bratuのfoldへ近づく6固定点で、状態誤差と線形許容差の影響を分け、独立shooting勾配と照合します。

##### [分布係数Bratuの行列非形成VJP](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-distributed-vjp/?lang=ja) (`bratu-distributed-vjp`)

![分布係数Bratuの行列非形成VJP。実際の保存数値データの縮小図で、1次元問題です。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/results/bratu-distributed-vjp-preview.png)

Bvは局所gather、B転置はscatter-add。一次実装はn×m行列を作らずJvで解き、同一状態の1/3目的関数で実際に1個のPoisson因子を共有します。別の参照期間のみdense hatとm本の接線RHSを許可します。 R2は同じfloat64の隣接差を先に取る一般Jvで、元の非線形残差・GMRES・許容差は変更しません。 R3は状態Newton補正だけをhi+loで保持し、直接9積残差と3積状態更新を使います。物理状態はfloat64、感度/随伴GMRESは旧方式です。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-distributed-vjp/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-distributed-vjp/?lang=ja#code-ja)

- [分布係数Bratuの行列非形成VJP](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-distributed-vjp/?lang=ja) (`bratu-distributed-vjp`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/atlas-adjoint-2026-11-24.zip)

2重みだけの局所hat作用で8/16/32個の空間係数を表し、目的関数ごとの随伴VJPを全感度参照と比較します。

##### [Robertson反応系：ODEと保存則DAE](https://hrkoyama.github.io/numerical-methods-atlas/problems/robertson-stiff-kinetics/?lang=ja) (`robertson-stiff-kinetics`)

![短い固定区間でBDF2・SDIRK2・倍分割適応法を、資格済みRadau/BDF参照と比較します。 保存済みの数値場と参照を用いた図です。 図の軌道・状態・時刻・反復の軸は、物理空間の次元を表しません。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/robertson-stiff-kinetics-preview.png)

BDF2は同格子BE開始。SDIRK2の非線形段階は重み付き最大残差で判定し、同じ段階内だけJacobian因子を再利用。適応法はRMS倍分割誤差と2半刻みを採用。 解析Jacobian付き固定BE/Newtonを使い、質量の投影・濃度クリップはしません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/robertson-stiff-kinetics/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/robertson-stiff-kinetics/?lang=ja#code-ja)

- [Robertson反応系の初期剛性と実誤差](https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-stiff-kinetics/?lang=ja) (`robertson-stiff-kinetics`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/atlas-ode-adaptivity-2026-11-24-r2.zip)

短い固定区間でBDF2・SDIRK2・倍分割適応法を、資格済みRadau/BDF参照と比較します。

- [Robertson保存制約DAEと公式IDA保存値](https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-conservation-dae/?lang=ja) (`robertson-conservation-dae`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/atlas-dae-controls-2026-11-24.zip)

Robertsonの保存制約DAEと全ODEを同じ固定時間格子で比較し、公式IDA保存値を別に照合します。 初回は元の時間精度・細分化目標4件が未達でした。

##### [van der Polの短時間剛性遷移](https://hrkoyama.github.io/numerical-methods-atlas/problems/van-der-pol-stiff-transition/?lang=ja) (`van-der-pol-stiff-transition`)

![保存済みの固定刻み比較と局所/大域誤差の区別。初回208/209で、μ=1適応法の大域目標2e-5は未達のまま保持します。 図の軌道・状態・時刻・反復の軸は、物理空間の次元を表しません。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/van-der-pol-stiff-transition-preview.png)

BDF2/SDIRK2と倍分割適応法。解析Jacobian・段階内だけの因子再利用・失敗時の候補保存を実装します。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/van-der-pol-stiff-transition/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/van-der-pol-stiff-transition/?lang=ja#code-ja)

- [van der Polの短時間剛性遷移](https://hrkoyama.github.io/numerical-methods-atlas/validation/van-der-pol-stiff-transition/?lang=ja) (`van-der-pol-stiff-transition`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/atlas-ode-adaptivity-2026-11-24-r2.zip)

局所制御と大域誤差を分離します。初回は元209目標中208達成で、μ=1の厳しい適応設定は大域目標2e-5に未達でした。

##### [index-1 DAEの整合初期化と離散残差](https://hrkoyama.github.io/numerical-methods-atlas/problems/index1-dae-consistent-initialization/?lang=ja) (`index1-dae-consistent-initialization`)

![既知の正枝を持つindex-1 DAEで初期化と後退Eulerの誤差・残差を分離します。 保存配列から作図。 図の軌道・状態・時刻・反復の軸は、物理空間の次元を表しません。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/index1-dae-consistent-initialization-preview.png)

連立Newtonと同じ尺度のArmijo線探索を用い、特異な初期推測は修復せず記録します。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/index1-dae-consistent-initialization/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/index1-dae-consistent-initialization/?lang=ja#code-ja)

- [index-1 DAEの整合初期化と離散残差](https://hrkoyama.github.io/numerical-methods-atlas/validation/index1-dae-consistent-initialization/?lang=ja) (`index1-dae-consistent-initialization`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/atlas-dae-controls-2026-11-24.zip)

既知の正枝を持つindex-1 DAEで初期化と後退Eulerの誤差・残差を分離します。

##### [酵素反応の保存と準定常近似](https://hrkoyama.github.io/numerical-methods-atlas/problems/enzyme-qssa/?lang=ja) (`enzyme-qssa`)

![全4状態と準定常近似を比較し、初期層と積分誤差を分けます。 保存値だけを描画します。 時間・濃度・個体数の軸は空間次元ではありません。率は教育用で疾病・実験予測ではありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/enzyme-qssa-preview.png)

全4状態をSDIRK2のstep doublingで積分し、各段のNewton法では同じ重み付きL∞残差とArmijo条件を使います。縮約Michaelis–Menten式はθ上の別RK4計算で求め、全系の積分誤差と近似モデル誤差を混同しません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/enzyme-qssa/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/enzyme-qssa/?lang=ja#code-ja)

- [酵素反応の保存と準定常近似](https://hrkoyama.github.io/numerical-methods-atlas/validation/enzyme-qssa/?lang=ja) (`enzyme-qssa`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/atlas-small-models-2026-11-25.zip)

全4状態と準定常近似を比較し、初期層と積分誤差を分けます。


#### 厳密解・参照解 (`method-references-ja`)

##### [1次元Bratu非線形境界値問題](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu/?lang=ja#references-ja) (`bratu`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### [減衰Newton法による3次方程式の求根](https://hrkoyama.github.io/numerical-methods-atlas/problems/cubic-root/?lang=ja#references-ja) (`cubic-root`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### [擬似弧長継続でBratuのfoldを越える](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-continuation/?lang=ja#references-ja) (`bratu-fold-continuation`)

- [擬似弧長継続でBratuのfoldを越える](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-bratu-fold-continuation-ja) (`bratu-fold-continuation`; 同じ問題の参照; 解析参照)

小さな1次元の単純foldだけです。分岐曲線の解析族比較では計算した中点値を族の座標に使い、固定λの独立形状比較と区別します。連続foldは離散解そのものではなく、一般の分岐追跡や大規模性能は保証しません。

[既存の参照図](/numerical-methods-atlas/validation/bratu-fold-continuation/?lang=ja#bratu-fold-continuation-ja-measurements)

##### [同じ難しい初期値に対する線探索と信頼領域](https://hrkoyama.github.io/numerical-methods-atlas/problems/globalization-difficult-starts/?lang=ja#references-ja) (`globalization-difficult-starts`)

- [同一初期値の大域化：解析対照と離散Bratu修正](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-globalization-difficult-starts-ja) (`globalization-difficult-starts`; 同じ問題の参照; 有限格子の数値参照)

全初期値の成功や手法の普遍的優越、PETSc実装との一致を保証しません。

[既存の参照図](/numerical-methods-atlas/validation/globalization-difficult-starts/?lang=ja#globalization-difficult-starts-ja-measurements)

##### [離散fold近傍のBratu感度](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-sensitivity/?lang=ja#references-ja) (`bratu-fold-sensitivity`)

- [離散fold近傍のBratu shooting・接線・随伴参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-bratu-fold-sensitivity-ja) (`bratu-fold-sensitivity`; 同じ問題の参照; 有限格子の数値参照)

連続foldは離散foldではありません。rtol1e-4/1e-8は達成必須、requested1e-12は観測のみで未達を収束と表示しません。返却候補の独立勾配精度は別判定。最小固有値/丸めscaleは浮動小数点の診断で保証区間ではありません。BratuのJは対称であり、非対称転置は別の演算子対照です。 inputsの/solver/gmres/retention_adaptationはR1/R2の履歴記述で、現状態解法は新契約の明示混合精度が上書きします。射影解の未達は別保存します。

[既存の参照図](/numerical-methods-atlas/validation/bratu-fold-sensitivity/?lang=ja#bratu-fold-sensitivity-ja-measurements)

##### [分布係数Bratuの行列非形成VJP](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-distributed-vjp/?lang=ja#references-ja) (`bratu-distributed-vjp`)

- [分布Bratu係数の独立dense感度と行列不要VJP](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-bratu-distributed-vjp-ja) (`bratu-distributed-vjp`; 同じ問題の参照; 有限格子の数値参照)

同じ離散状態の微分検証で、独立した物理PDE解の証明や一般ADではありません。保存arrayと固定Krylov workspaceの記録はRSS測定ではありません。m=2のθ端点は[a-b-2,a+b-2]で、物理係数端点[a-b,a+b]と区別します。 inputsの/solver/gmres/retention_adaptationはR1/R2の履歴記述で、現状態解法は新契約の明示混合精度が上書きします。射影解の未達は別保存します。

[既存の参照図](/numerical-methods-atlas/validation/bratu-distributed-vjp/?lang=ja#bratu-distributed-vjp-ja-measurements)

##### [Robertson反応系：ODEと保存則DAE](https://hrkoyama.github.io/numerical-methods-atlas/problems/robertson-stiff-kinetics/?lang=ja#references-ja) (`robertson-stiff-kinetics`)

- [Robertson反応系の初期剛性と実誤差](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-robertson-stiff-kinetics-ja) (`robertson-stiff-kinetics`; 同じ問題の参照; 有限格子の数値参照)

保存/正値性は固定入力の観測で、一般的な保証ではありません。T=.4の短時間・標本時刻での精度であり、長時間化学精度や全時刻誤差上限は主張しません。

[既存の参照図](/numerical-methods-atlas/validation/robertson-stiff-kinetics/?lang=ja#robertson-stiff-kinetics-ja-measurements)

- [Robertson保存制約DAEと公式IDA保存値](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-robertson-conservation-dae-ja) (`robertson-conservation-dae`; 同じ問題の参照; 有限格子の数値参照)

公式SUNDIALS v7.1.1の2印字行のみ。IDAの新規実行0、長時間の化学精度や一般DAE性能は扱いません。 この固定時間格子の漸近収束や元精度目標の全合格は主張しません。

[既存の参照図](/numerical-methods-atlas/validation/robertson-conservation-dae/?lang=ja#robertson-conservation-dae-ja-measurements)

##### [van der Polの短時間剛性遷移](https://hrkoyama.github.io/numerical-methods-atlas/problems/van-der-pol-stiff-transition/?lang=ja#references-ja) (`van-der-pol-stiff-transition`)

- [van der Polの短時間剛性遷移](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-van-der-pol-stiff-transition-ja) (`van-der-pol-stiff-transition`; 同じ問題の参照; 有限格子の数値参照)

測定後の報告範囲変更で、数値的な修復ではありません。初回誤差4.535633779e-5は元目標2e-5を超えます。局所rtolは大域誤差を保証せず、報告検証の合格は全元目標の達成ではありません。大μ全周期は対象外です。

[既存の参照図](/numerical-methods-atlas/validation/van-der-pol-stiff-transition/?lang=ja#van-der-pol-stiff-transition-ja-measurements)

##### [index-1 DAEの整合初期化と離散残差](https://hrkoyama.github.io/numerical-methods-atlas/problems/index1-dae-consistent-initialization/?lang=ja#references-ja) (`index1-dae-consistent-initialization`)

- [index-1 DAEの整合初期化と離散残差](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-index1-dae-consistent-initialization-ja) (`index1-dae-consistent-initialization`; 同じ問題の参照; 製造解)

単一の製造正枝・固定BE計算です。IDA実行や一般DAEソルバーの検証ではありません。

[既存の参照図](/numerical-methods-atlas/validation/index1-dae-consistent-initialization/?lang=ja#index1-dae-consistent-initialization-ja-measurements)

##### [酵素反応の保存と準定常近似](https://hrkoyama.github.io/numerical-methods-atlas/problems/enzyme-qssa/?lang=ja#references-ja) (`enzyme-qssa`)

- [酵素反応の保存と準定常近似](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-enzyme-qssa-ja) (`enzyme-qssa`; 同じ問題の参照; 有限格子の数値参照)

2つの小εと固定反応定数だけの教育例です。εは尺度比であり、その値だけを厳密なQSSA誤差上界とはしません。θ≥0.02を初期層終了の証明とは呼ばず、生体内の反応・観測値へ外挿しません。

[既存の参照図](/numerical-methods-atlas/validation/enzyme-qssa/?lang=ja#enzyme-qssa-ja-measurements)

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/sparse-nonlinear/)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

##### 1次元Bratu：小さい枝のNewton–GMRES (`bratu`)

[1次元Bratu非線形境界値問題](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/bratu/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

[固定入力](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/recipes/bratu.json)

[検証記録](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

−u''=λexp(u)、β=1・λ=2β²/cosh²(β/2)の小さい枝を零初期値から解く。31/63/127内部点で解析解、独立に再評価した非線形残差、2次格子収束を確認する。

##### 擬似弧長継続でBratuのfoldを越える (`bratu-fold-continuation`)

[擬似弧長継続でBratuのfoldを越える](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-continuation/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-continuation/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/atlas-bratu-continuation-jfnk-2026-11-24-r2.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/verification.json)

同じ1次元Bratu境界値問題の下枝から上枝までを追跡し、接線・fold・独立解析族との空間誤差を調べます。

##### 同じ難しい初期値に対する線探索と信頼領域 (`globalization-difficult-starts`)

[同じ難しい初期値に対する線探索と信頼領域](https://hrkoyama.github.io/numerical-methods-atlas/problems/globalization-difficult-starts/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/globalization-difficult-starts/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/atlas-globalization-controls-2026-11-24.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/verification.json)

同じ固定初期値からNewton・Armijo・doglegを比較し、真の根と非根停留・予算終了を区別します。

##### 離散fold近傍のBratu感度 (`bratu-fold-sensitivity`)

[離散fold近傍のBratu感度](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-sensitivity/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-sensitivity/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/atlas-adjoint-2026-11-24.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/verification.json)

離散Bratuのfoldへ近づく6固定点で、状態誤差と線形許容差の影響を分け、独立shooting勾配と照合します。

##### 分布係数Bratuの行列非形成VJP (`bratu-distributed-vjp`)

[分布係数Bratuの行列非形成VJP](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-distributed-vjp/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-distributed-vjp/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/atlas-adjoint-2026-11-24.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/verification.json)

2重みだけの局所hat作用で8/16/32個の空間係数を表し、目的関数ごとの随伴VJPを全感度参照と比較します。

##### Robertson反応系の初期剛性と実誤差 (`robertson-stiff-kinetics`)

[Robertson反応系：ODEと保存則DAE](https://hrkoyama.github.io/numerical-methods-atlas/problems/robertson-stiff-kinetics/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-stiff-kinetics/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/atlas-ode-adaptivity-2026-11-24-r2.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/verification.json)

短い固定区間でBDF2・SDIRK2・倍分割適応法を、資格済みRadau/BDF参照と比較します。

##### Robertson保存制約DAEと公式IDA保存値 (`robertson-conservation-dae`)

[Robertson反応系：ODEと保存則DAE](https://hrkoyama.github.io/numerical-methods-atlas/problems/robertson-stiff-kinetics/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-conservation-dae/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/atlas-dae-controls-2026-11-24.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/verification.json)

Robertsonの保存制約DAEと全ODEを同じ固定時間格子で比較し、公式IDA保存値を別に照合します。 初回は元の時間精度・細分化目標4件が未達でした。

##### van der Polの短時間剛性遷移 (`van-der-pol-stiff-transition`)

[van der Polの短時間剛性遷移](https://hrkoyama.github.io/numerical-methods-atlas/problems/van-der-pol-stiff-transition/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/van-der-pol-stiff-transition/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/atlas-ode-adaptivity-2026-11-24-r2.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/verification.json)

局所制御と大域誤差を分離します。初回は元209目標中208達成で、μ=1の厳しい適応設定は大域目標2e-5に未達でした。

##### index-1 DAEの整合初期化と離散残差 (`index1-dae-consistent-initialization`)

[index-1 DAEの整合初期化と離散残差](https://hrkoyama.github.io/numerical-methods-atlas/problems/index1-dae-consistent-initialization/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/index1-dae-consistent-initialization/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/atlas-dae-controls-2026-11-24.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/verification.json)

既知の正枝を持つindex-1 DAEで初期化と後退Eulerの誤差・残差を分離します。

##### 酵素反応の保存と準定常近似 (`enzyme-qssa`)

[酵素反応の保存と準定常近似](https://hrkoyama.github.io/numerical-methods-atlas/problems/enzyme-qssa/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/enzyme-qssa/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/atlas-small-models-2026-11-25.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/verification.json)

全4状態と準定常近似を比較し、初期層と積分誤差を分けます。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### 関連ソース

- [/code/numerical-methods-atlas/2026-11-21/numart/krylov.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/krylov.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/run.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/problem.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/problem.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/continuation.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/continuation.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/matrix_free.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/matrix_free.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/dual.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/dual.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/experiments.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/references/analytic_family.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/references/analytic_family.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/io_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/io_contract.py)
- [/code/validated-examples/2026-11-24/globalization-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/run.py)
- [/code/validated-examples/2026-11-24/globalization-controls/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/experiments.py)
- [/code/validated-examples/2026-11-24/globalization-controls/globalization.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/globalization.py)
- [/code/validated-examples/2026-11-24/globalization-controls/io_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/io_contract.py)
- [/code/validated-examples/2026-11-24/globalization-controls/problems.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/problems.py)
- [/code/validated-examples/2026-11-24/globalization-controls/references.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/references.py)
- [/code/validated-examples/2026-11-24/adjoint/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/run.py)
- [/code/validated-examples/2026-11-24/adjoint/operators.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/operators.py)
- [/code/validated-examples/2026-11-24/adjoint/krylov.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/krylov.py)
- [/code/validated-examples/2026-11-24/adjoint/newton.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/newton.py)
- [/code/validated-examples/2026-11-24/adjoint/fold_study.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/fold_study.py)
- [/code/validated-examples/2026-11-24/adjoint/references/modal_decimal.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/references/modal_decimal.py)
- [/code/validated-examples/2026-11-24/adjoint/references/shooting_decimal.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/references/shooting_decimal.py)
- [/code/validated-examples/2026-11-24/adjoint/references/linear_oracle.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/references/linear_oracle.py)
- [/code/validated-examples/2026-11-24/adjoint/balanced_operator.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/balanced_operator.py)
- [/code/validated-examples/2026-11-24/adjoint/state_linear.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/state_linear.py)
- [/code/validated-examples/2026-11-24/adjoint/state_expansion.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/state_expansion.py)
- [/code/validated-examples/2026-11-24/adjoint/state_krylov.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/state_krylov.py)
- [/code/validated-examples/2026-11-24/adjoint/state_jacobian.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/state_jacobian.py)
- [/code/validated-examples/2026-11-24/adjoint/distributed.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/distributed.py)
- [/code/validated-examples/2026-11-24/adjoint/time_adjoint.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/time_adjoint.py)
- [/code/validated-examples/2026-11-24/adjoint/io_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/io_contract.py)
- [/code/validated-examples/2026-11-24/adjoint/qualify_references.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/qualify_references.py)
- [/code/validated-examples/2026-11-24/adjoint/tests/conftest.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/tests/conftest.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/run.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/experiments.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/io_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/io_contract.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/reference_eval.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/reference_eval.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/models.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/stiff.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/stiff.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/reporting_policy.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/reporting_policy.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/dopri.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/dopri.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/tableau.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/tableau.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/boundary.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/boundary.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/boundary_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/boundary_reference.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/coefficient_exact.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/coefficient_exact.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/qualify.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/qualify.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/reference_models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/reference_models.py)
- [/code/validated-examples/2026-11-24/dae-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/run.py)
- [/code/validated-examples/2026-11-24/dae-controls/models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/models.py)
- [/code/validated-examples/2026-11-24/dae-controls/newton.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/newton.py)
- [/code/validated-examples/2026-11-24/dae-controls/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/experiments.py)
- [/code/validated-examples/2026-11-24/dae-controls/io_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/io_contract.py)
- [/code/validated-examples/2026-11-24/dae-controls/references.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/references.py)
- [/code/validated-examples/2026-11-24/dae-controls/reporting.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/reporting.py)
- [/code/validated-examples/2026-11-25/small-models/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/run.py)
- [/code/validated-examples/2026-11-25/small-models/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/experiments.py)
- [/code/validated-examples/2026-11-25/small-models/io_utils.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/io_utils.py)
- [/code/validated-examples/2026-11-25/small-models/biology.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/biology.py)
- [/code/validated-examples/2026-11-25/small-models/pinn.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/pinn.py)
- [/code/validated-examples/2026-11-25/small-models/fno.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/fno.py)
- [/code/validated-examples/2026-11-25/small-models/data_family.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/data_family.py)
- [/code/validated-examples/2026-11-25/small-models/references/oracles.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/references/oracles.py)
- [/code/validated-examples/2026-11-25/small-models/references/qualify.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/references/qualify.py)
- [/code/validated-examples/2026-11-25/small-models/references/reference_models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/references/reference_models.py)

###### 配布版のテスト

- [/code/numerical-methods-atlas/2026-11-21/tests/test_sparse_fem.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_sparse_fem.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/test_bratu.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/test_bratu.py)
- [/code/validated-examples/2026-11-24/globalization-controls/test_globalization.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/test_globalization.py)
- [/code/validated-examples/2026-11-24/adjoint/tests/test_distributed.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/tests/test_distributed.py)
- [/code/validated-examples/2026-11-24/adjoint/tests/test_fold.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/tests/test_fold.py)
- [/code/validated-examples/2026-11-24/adjoint/tests/test_time.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/tests/test_time.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_boundary.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_boundary.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_contract.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_dopri.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_dopri.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_reporting.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_reporting.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_stiff.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_stiff.py)
- [/code/validated-examples/2026-11-24/dae-controls/test_cases.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/test_cases.py)
- [/code/validated-examples/2026-11-24/dae-controls/test_serialization.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/test_serialization.py)
- [/code/validated-examples/2026-11-25/small-models/test_models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/test_models.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q tests/test_sparse_fem.py
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Bratu nonlinear boundary-value problem](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bratu-en) (`bratu`; bratu, bratu-fold-continuation, globalization-difficult-starts, bratu-fold-sensitivity, bratu-distributed-vjp)
- [Finite-dimensional nonlinear maps, roots and differential actions](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#finite-dimensional-nonlinear-map-en) (`finite-dimensional-nonlinear-map`; globalization-difficult-starts)
- [Robertson chemical kinetics](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#robertson-kinetics-en) (`robertson-kinetics`; robertson-stiff-kinetics)
- [Semi-explicit index-one DAE](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#index-one-dae-en) (`index-one-dae`; robertson-stiff-kinetics, index1-dae-consistent-initialization)
- [Van der Pol oscillator](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#van-der-pol-en) (`van-der-pol`; van-der-pol-stiff-transition)
- [Michaelis–Menten and full enzyme kinetics](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-enzyme-en) (`bio-enzyme`; enzyme-qssa)

#### Problem figures (`method-problems-en`)

##### [One-dimensional Bratu boundary-value problem](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu/?lang=en) (`bratu`)

![Calculated from the public code edition with fixed inputs; inputs, values and checks are linked.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/bratu.png)

The common example solves the forward boundary-value problem with damped Newton. Related method pages lead to separate editions for automatic differentiation, sensitivities, adjoints and coefficient fitting. Sensitivity and inverse problems with one or two coefficients have separate inputs and acceptance checks; they are not added to the common forward execution entry.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu/?lang=en#code-en)

- [1D Bratu: Newton–GMRES on the lower branch](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/bratu/?lang=en) (`bratu`) · [Code ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

Solve the lower branch of −u''=λexp(u), with β=1 and λ=2β²/cosh²(β/2), starting at zero. Check the analytic solution, recomputed nonlinear residual and second-order refinement on 31/63/127 interior nodes.

##### [Damped Newton root of a cubic equation](https://hrkoyama.github.io/numerical-methods-atlas/problems/cubic-root/?lang=en) (`cubic-root`)

![Calculated from the public code edition with fixed inputs; inputs, values and checks are linked.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/cubic-root.png)

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/cubic-root/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/cubic-root/?lang=en#code-en)

No fixed-input execution of this problem is registered for this method.

##### [Crossing the Bratu fold with pseudo-arclength continuation](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-continuation/?lang=en) (`bratu-fold-continuation`)

![Preview of the stored branch,lambda=2 profiles,smallest Jacobian singular value and three-grid fold error. Arclength steps are not physical time.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/results/bratu-fold-continuation-preview.png)

Use a unit tangent in h-sum(du squared)+d-lambda squared, a predictor and a tangent-hyperplane Newton corrector. A separate augmented system locates the fold and a normalized null vector. This case deliberately assembles sparse Jacobians.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-continuation/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-continuation/?lang=en#code-en)

- [Crossing the Bratu fold with pseudo-arclength continuation](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-continuation/?lang=en) (`bratu-fold-continuation`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/atlas-bratu-continuation-jfnk-2026-11-24-r2.zip)

Follow the lower and upper branches of the same one-dimensional Bratu boundary-value problem; check tangents, the fold and spatial error against an independent analytic family.

##### [Line search and trust regions from the same difficult starts](https://hrkoyama.github.io/numerical-methods-atlas/problems/globalization-difficult-starts/?lang=en) (`globalization-difficult-starts`)

![Saved paths from identical starts, original residuals, trust radii and measured evaluation counts. Failures and nonconvergence remain explicit. Plot axes describe finite-dimensional variables, iterations or diagnostics, not a physical spatial dimension or PDE boundary.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/results/globalization-difficult-starts-preview.png)

Separate the original residual from the scaled merit and retain Euclidean dogleg and trial ledgers.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/globalization-difficult-starts/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/globalization-difficult-starts/?lang=en#code-en)

- [Line search and trust regions from the same difficult starts](https://hrkoyama.github.io/numerical-methods-atlas/validation/globalization-difficult-starts/?lang=en) (`globalization-difficult-starts`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/atlas-globalization-controls-2026-11-24.zip)

Compare Newton, Armijo and dogleg from identical fixed starts, distinguishing roots from stationary nonroots and budget exhaustion.

##### [Bratu sensitivity near the discrete fold](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-sensitivity/?lang=en) (`bratu-fold-sensitivity`)

![Bratu sensitivity near the discrete fold. Preview from actual saved numerical data for a one-dimensional problem.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/results/bratu-fold-sensitivity-preview.png)

Analytic Jv, Poisson-Thomas right preconditioning and the preserved GMRES body solve tangents/adjoints. Save every rtol, returned candidate, true residual, termination and roundoff scale. Qualify the discrete oracle through shooting and separate high-precision Thomas-Newton. R2 uses a general near-neighbor-difference association in binary64 Jv; the original nonlinear residual,GMRES and tolerances are unchanged. R3 expands only stateNewtoncorrections ashi+lo,direct9productresidual and3productstateupdate. Physicalstates stayfloat64;derivative/adjointGMRES staysordinary.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-sensitivity/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-sensitivity/?lang=en#code-en)

- [Bratu sensitivity near the discrete fold](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-sensitivity/?lang=en) (`bratu-fold-sensitivity`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/atlas-adjoint-2026-11-24.zip)

At six fixed points approaching the discrete Bratu fold, separate state error from linear-solve tolerance and compare against independent shooting gradients.

##### [Matrix-free VJP for distributed Bratu coefficients](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-distributed-vjp/?lang=en) (`bratu-distributed-vjp`)

![Matrix-free VJP for distributed Bratu coefficients. Preview from actual saved numerical data for a one-dimensional problem.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/results/bratu-distributed-vjp-preview.png)

Bv uses local gather and B transpose scatter-add. Primary solves use Jv without an n-by-m matrix. One shared Poisson factor serves the one/three-objective runs on the same state. Dense hats and m tangent RHS are allowed only in the separate reference window. R2 uses a general near-neighbor-difference association in binary64 Jv; the original nonlinear residual,GMRES and tolerances are unchanged. R3 expands only stateNewtoncorrections ashi+lo,direct9productresidual and3productstateupdate. Physicalstates stayfloat64;derivative/adjointGMRES staysordinary.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-distributed-vjp/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-distributed-vjp/?lang=en#code-en)

- [Matrix-free VJP for distributed Bratu coefficients](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-distributed-vjp/?lang=en) (`bratu-distributed-vjp`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/atlas-adjoint-2026-11-24.zip)

Represent8/16/32 spatial controls with two local hat weights per node; compare objective-wise adjoint VJPs with a separate full-sensitivity reference.

##### [Robertson kinetics: ODE and conservation DAE](https://hrkoyama.github.io/numerical-methods-atlas/problems/robertson-stiff-kinetics/?lang=en) (`robertson-stiff-kinetics`)

![Compare BDF2, SDIRK2 and adaptive step doubling on a short fixed interval against qualified Radau and BDF references. This preview reads saved numerical fields and references only. Axes for trajectories, states, time or iterations do not represent physical spatial dimensions.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/robertson-stiff-kinetics-preview.png)

BDF2 starts with backward Euler on the same grid. SDIRK2 stages use a weighted maximum residual and reuse Jacobian factors only within one stage. Adaptive steps use an RMS step-doubling estimate and accept the two-half-step result. Use fixed BE/Newton with analytic Jacobians and no mass projection or concentration clipping.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/robertson-stiff-kinetics/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/robertson-stiff-kinetics/?lang=en#code-en)

- [Robertson kinetics: initial stiffness and actual error](https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-stiff-kinetics/?lang=en) (`robertson-stiff-kinetics`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/atlas-ode-adaptivity-2026-11-24-r2.zip)

Compare BDF2, SDIRK2 and adaptive step doubling on a short fixed interval against qualified Radau and BDF references.

- [Robertson conservation DAE and stored official IDA values](https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-conservation-dae/?lang=en) (`robertson-conservation-dae`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/atlas-dae-controls-2026-11-24.zip)

Compare the Robertson conservation DAE and full ODE on the same fixed time grids, with a separate check of stored official IDA values. The first retained run missed four original time-accuracy and refinement goals.

##### [Van der Pol: an early stiffness transition](https://hrkoyama.github.io/numerical-methods-atlas/problems/van-der-pol-stiff-transition/?lang=en) (`van-der-pol-stiff-transition`)

![Saved fixed-step comparisons and the local/global error distinction. The first study met 208/209 targets; the unmet mu = 1 adaptive global goal of 2e-5 remains recorded. Axes for trajectories, states, time or iterations do not represent physical spatial dimensions.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/van-der-pol-stiff-transition-preview.png)

Use actual BDF2, SDIRK2 and adaptive step doubling, analytic Jacobians, factor reuse within each implicit stage, and retained candidates on failure.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/van-der-pol-stiff-transition/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/van-der-pol-stiff-transition/?lang=en#code-en)

- [Van der Pol: an early stiffness transition](https://hrkoyama.github.io/numerical-methods-atlas/validation/van-der-pol-stiff-transition/?lang=en) (`van-der-pol-stiff-transition`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/atlas-ode-adaptivity-2026-11-24-r2.zip)

Separate local control from global error. The first study met 208 of 209 original targets; the mu = 1 tight adaptive run missed the 2e-5 global goal.

##### [Consistent initialization and discrete residuals for an index-one DAE](https://hrkoyama.github.io/numerical-methods-atlas/problems/index1-dae-consistent-initialization/?lang=en) (`index1-dae-consistent-initialization`)

![Separate initialization, backward-Euler error and residuals on a known positive index-one DAE branch. Drawn from saved arrays. Axes for trajectories, states, time or iterations do not represent physical spatial dimensions.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/index1-dae-consistent-initialization-preview.png)

Use coupled Newton with an Armijo search in the same scaled norm, retaining rather than repairing a singular initial guess.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/index1-dae-consistent-initialization/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/index1-dae-consistent-initialization/?lang=en#code-en)

- [Consistent initialization and discrete residuals for an index-one DAE](https://hrkoyama.github.io/numerical-methods-atlas/validation/index1-dae-consistent-initialization/?lang=en) (`index1-dae-consistent-initialization`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/atlas-dae-controls-2026-11-24.zip)

Separate initialization, backward-Euler error and residuals on a known positive index-one DAE branch.

##### [Enzyme conservation and QSSA](https://hrkoyama.github.io/numerical-methods-atlas/problems/enzyme-qssa/?lang=en) (`enzyme-qssa`)

![Separate the initial layer, integration error and QSSA modeling error in a four-state enzyme mechanism. This figure reads saved data only. Time, concentrations and populations do not define a spatial dimension. The rates are educational, not disease or experimental predictions.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/enzyme-qssa-preview.png)

Integrate all four states with SDIRK2 step doubling, using the same weighted L∞ residual for Newton convergence and Armijo backtracking. Evolve the reduced Michaelis–Menten equation separately with RK4 in θ, keeping integration error distinct from model-reduction error.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/enzyme-qssa/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/enzyme-qssa/?lang=en#code-en)

- [Enzyme conservation and QSSA](https://hrkoyama.github.io/numerical-methods-atlas/validation/enzyme-qssa/?lang=en) (`enzyme-qssa`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/atlas-small-models-2026-11-25.zip)

Separate the initial layer, integration error and QSSA modeling error in a four-state enzyme mechanism.


#### Exact / reference solutions (`method-references-en`)

##### [One-dimensional Bratu boundary-value problem](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu/?lang=en#references-en) (`bratu`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### [Damped Newton root of a cubic equation](https://hrkoyama.github.io/numerical-methods-atlas/problems/cubic-root/?lang=en#references-en) (`cubic-root`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### [Crossing the Bratu fold with pseudo-arclength continuation](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-continuation/?lang=en#references-en) (`bratu-fold-continuation`)

- [Crossing the Bratu fold with pseudo-arclength continuation](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-bratu-fold-continuation-en) (`bratu-fold-continuation`; Same-problem reference; Analytic reference)

A small one-dimensional simple fold only. The whole-curve family comparison uses the computed midpoint as its family coordinate and is distinct from the independent fixed-lambda profile checks. The continuum fold is not an exact discrete solution. No general bifurcation-tracking or large-scale performance claim.

[Existing reference profile](/numerical-methods-atlas/validation/bratu-fold-continuation/?lang=en#bratu-fold-continuation-en-measurements)

##### [Line search and trust regions from the same difficult starts](https://hrkoyama.github.io/numerical-methods-atlas/problems/globalization-difficult-starts/?lang=en#references-en) (`globalization-difficult-starts`)

- [Globalization from identical starts: analytic controls and discrete Bratu corrections](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-globalization-difficult-starts-en) (`globalization-difficult-starts`; Same-problem reference; Finite-grid numerical reference)

No all-start guarantee, universal method ranking or equivalence to PETSc implementation.

[Existing reference profile](/numerical-methods-atlas/validation/globalization-difficult-starts/?lang=en#globalization-difficult-starts-en-measurements)

##### [Bratu sensitivity near the discrete fold](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-sensitivity/?lang=en#references-en) (`bratu-fold-sensitivity`)

- [Discrete Bratu shooting, tangent and adjoint references near a fold](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-bratu-fold-sensitivity-en) (`bratu-fold-sensitivity`; Same-problem reference; Finite-grid numerical reference)

The continuum fold is not the discrete fold. rtol1e-4/1e-8 targets are required; requested1e-12 is observational and unmet is never called converged. Independent accuracy of the returned gradient is a separate gate. Eigenvalue/roundoff scales are floating diagnostics, not certified intervals. Bratu J is symmetric; the nonsymmetric transpose is a separate operator control. The retained /solver/gmres/retention_adaptation text is historicalR1/R2;the newcontract explicitly overrides it for mixed-precisionSTATEsolves. ProjectedUNMET is separatelysaved.

[Existing reference profile](/numerical-methods-atlas/validation/bratu-fold-sensitivity/?lang=en#bratu-fold-sensitivity-en-measurements)

##### [Matrix-free VJP for distributed Bratu coefficients](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-distributed-vjp/?lang=en#references-en) (`bratu-distributed-vjp`)

- [Independent dense sensitivities and matrix-free VJPs for distributed Bratu coefficients](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-bratu-distributed-vjp-en) (`bratu-distributed-vjp`; Same-problem reference; Finite-grid numerical reference)

Derivative verification at the same discrete state, not independent physical-PDE truth or general AD. Persistent arrays and fixed Krylov workspace inventories are not RSS measurements. For m=2, theta endpoints are[a-b-2,a+b-2], distinct from physical coefficient endpoints[a-b,a+b]. The retained /solver/gmres/retention_adaptation text is historicalR1/R2;the newcontract explicitly overrides it for mixed-precisionSTATEsolves. ProjectedUNMET is separatelysaved.

[Existing reference profile](/numerical-methods-atlas/validation/bratu-distributed-vjp/?lang=en#bratu-distributed-vjp-en-measurements)

##### [Robertson kinetics: ODE and conservation DAE](https://hrkoyama.github.io/numerical-methods-atlas/problems/robertson-stiff-kinetics/?lang=en#references-en) (`robertson-stiff-kinetics`)

- [Robertson kinetics: initial stiffness and actual error](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-robertson-stiff-kinetics-en) (`robertson-stiff-kinetics`; Same-problem reference; Finite-grid numerical reference)

Conservation and positivity are observations for these inputs, not universal guarantees. Accuracy is sampled on T <= 0.4; this does not validate long-time chemistry or an all-time error bound.

[Existing reference profile](/numerical-methods-atlas/validation/robertson-stiff-kinetics/?lang=en#robertson-stiff-kinetics-en-measurements)

- [Robertson conservation DAE and stored official IDA values](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-robertson-conservation-dae-en) (`robertson-conservation-dae`; Same-problem reference; Finite-grid numerical reference)

Only two official SUNDIALS v7.1.1 printed rows; zero new IDA executions, with no long-time chemistry or general DAE-performance claim. No asymptotic-convergence or all-original-accuracy-goals claim is made for this fixed schedule.

[Existing reference profile](/numerical-methods-atlas/validation/robertson-conservation-dae/?lang=en#robertson-conservation-dae-en-measurements)

##### [Van der Pol: an early stiffness transition](https://hrkoyama.github.io/numerical-methods-atlas/problems/van-der-pol-stiff-transition/?lang=en#references-en) (`van-der-pol-stiff-transition`)

- [Van der Pol: an early stiffness transition](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-van-der-pol-stiff-transition-en) (`van-der-pol-stiff-transition`; Same-problem reference; Finite-grid numerical reference)

This post-measurement reporting revision is not a numerical repair. The first error, 4.535633779e-5, exceeded the original 2e-5 goal. Local tolerances do not guarantee global accuracy, and reporting PASS does not mean all original goals were met. Full large-mu cycles are outside scope.

[Existing reference profile](/numerical-methods-atlas/validation/van-der-pol-stiff-transition/?lang=en#van-der-pol-stiff-transition-en-measurements)

##### [Consistent initialization and discrete residuals for an index-one DAE](https://hrkoyama.github.io/numerical-methods-atlas/problems/index1-dae-consistent-initialization/?lang=en#references-en) (`index1-dae-consistent-initialization`)

- [Consistent initialization and discrete residuals for an index-one DAE](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-index1-dae-consistent-initialization-en) (`index1-dae-consistent-initialization`; Same-problem reference; Manufactured solution)

One authored positive branch and fixed BE runs; no IDA execution or general DAE-solver qualification.

[Existing reference profile](/numerical-methods-atlas/validation/index1-dae-consistent-initialization/?lang=en#index1-dae-consistent-initialization-en-measurements)

##### [Enzyme conservation and QSSA](https://hrkoyama.github.io/numerical-methods-atlas/problems/enzyme-qssa/?lang=en#references-en) (`enzyme-qssa`)

- [Enzyme conservation and QSSA](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-enzyme-qssa-en) (`enzyme-qssa`; Same-problem reference; Finite-grid numerical reference)

These two small-ε fixed-rate examples are educational. ε is a scale ratio, not itself a certified QSSA error bound. The θ≥0.02 window is not a proof that the initial layer has ended, and the calculation is not an in-vivo prediction.

[Existing reference profile](/numerical-methods-atlas/validation/enzyme-qssa/?lang=en#enzyme-qssa-en-measurements)

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/sparse-nonlinear/)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

##### 1D Bratu: Newton–GMRES on the lower branch (`bratu`)

[One-dimensional Bratu boundary-value problem](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/bratu/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

[Fixed input](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/recipes/bratu.json)

[Verification receipt](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

Solve the lower branch of −u''=λexp(u), with β=1 and λ=2β²/cosh²(β/2), starting at zero. Check the analytic solution, recomputed nonlinear residual and second-order refinement on 31/63/127 interior nodes.

##### Crossing the Bratu fold with pseudo-arclength continuation (`bratu-fold-continuation`)

[Crossing the Bratu fold with pseudo-arclength continuation](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-continuation/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-continuation/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/atlas-bratu-continuation-jfnk-2026-11-24-r2.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/verification.json)

Follow the lower and upper branches of the same one-dimensional Bratu boundary-value problem; check tangents, the fold and spatial error against an independent analytic family.

##### Line search and trust regions from the same difficult starts (`globalization-difficult-starts`)

[Line search and trust regions from the same difficult starts](https://hrkoyama.github.io/numerical-methods-atlas/problems/globalization-difficult-starts/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/globalization-difficult-starts/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/atlas-globalization-controls-2026-11-24.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/verification.json)

Compare Newton, Armijo and dogleg from identical fixed starts, distinguishing roots from stationary nonroots and budget exhaustion.

##### Bratu sensitivity near the discrete fold (`bratu-fold-sensitivity`)

[Bratu sensitivity near the discrete fold](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-sensitivity/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-sensitivity/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/atlas-adjoint-2026-11-24.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/verification.json)

At six fixed points approaching the discrete Bratu fold, separate state error from linear-solve tolerance and compare against independent shooting gradients.

##### Matrix-free VJP for distributed Bratu coefficients (`bratu-distributed-vjp`)

[Matrix-free VJP for distributed Bratu coefficients](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-distributed-vjp/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-distributed-vjp/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/atlas-adjoint-2026-11-24.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/verification.json)

Represent8/16/32 spatial controls with two local hat weights per node; compare objective-wise adjoint VJPs with a separate full-sensitivity reference.

##### Robertson kinetics: initial stiffness and actual error (`robertson-stiff-kinetics`)

[Robertson kinetics: ODE and conservation DAE](https://hrkoyama.github.io/numerical-methods-atlas/problems/robertson-stiff-kinetics/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-stiff-kinetics/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/atlas-ode-adaptivity-2026-11-24-r2.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/verification.json)

Compare BDF2, SDIRK2 and adaptive step doubling on a short fixed interval against qualified Radau and BDF references.

##### Robertson conservation DAE and stored official IDA values (`robertson-conservation-dae`)

[Robertson kinetics: ODE and conservation DAE](https://hrkoyama.github.io/numerical-methods-atlas/problems/robertson-stiff-kinetics/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-conservation-dae/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/atlas-dae-controls-2026-11-24.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/verification.json)

Compare the Robertson conservation DAE and full ODE on the same fixed time grids, with a separate check of stored official IDA values. The first retained run missed four original time-accuracy and refinement goals.

##### Van der Pol: an early stiffness transition (`van-der-pol-stiff-transition`)

[Van der Pol: an early stiffness transition](https://hrkoyama.github.io/numerical-methods-atlas/problems/van-der-pol-stiff-transition/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/van-der-pol-stiff-transition/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/atlas-ode-adaptivity-2026-11-24-r2.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/verification.json)

Separate local control from global error. The first study met 208 of 209 original targets; the mu = 1 tight adaptive run missed the 2e-5 global goal.

##### Consistent initialization and discrete residuals for an index-one DAE (`index1-dae-consistent-initialization`)

[Consistent initialization and discrete residuals for an index-one DAE](https://hrkoyama.github.io/numerical-methods-atlas/problems/index1-dae-consistent-initialization/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/index1-dae-consistent-initialization/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/atlas-dae-controls-2026-11-24.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/verification.json)

Separate initialization, backward-Euler error and residuals on a known positive index-one DAE branch.

##### Enzyme conservation and QSSA (`enzyme-qssa`)

[Enzyme conservation and QSSA](https://hrkoyama.github.io/numerical-methods-atlas/problems/enzyme-qssa/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/enzyme-qssa/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/atlas-small-models-2026-11-25.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/verification.json)

Separate the initial layer, integration error and QSSA modeling error in a four-state enzyme mechanism.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[Related code edition / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### Related source

- [/code/numerical-methods-atlas/2026-11-21/numart/krylov.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/krylov.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/run.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/problem.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/problem.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/continuation.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/continuation.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/matrix_free.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/matrix_free.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/dual.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/dual.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/experiments.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/references/analytic_family.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/references/analytic_family.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/io_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/io_contract.py)
- [/code/validated-examples/2026-11-24/globalization-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/run.py)
- [/code/validated-examples/2026-11-24/globalization-controls/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/experiments.py)
- [/code/validated-examples/2026-11-24/globalization-controls/globalization.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/globalization.py)
- [/code/validated-examples/2026-11-24/globalization-controls/io_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/io_contract.py)
- [/code/validated-examples/2026-11-24/globalization-controls/problems.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/problems.py)
- [/code/validated-examples/2026-11-24/globalization-controls/references.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/references.py)
- [/code/validated-examples/2026-11-24/adjoint/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/run.py)
- [/code/validated-examples/2026-11-24/adjoint/operators.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/operators.py)
- [/code/validated-examples/2026-11-24/adjoint/krylov.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/krylov.py)
- [/code/validated-examples/2026-11-24/adjoint/newton.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/newton.py)
- [/code/validated-examples/2026-11-24/adjoint/fold_study.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/fold_study.py)
- [/code/validated-examples/2026-11-24/adjoint/references/modal_decimal.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/references/modal_decimal.py)
- [/code/validated-examples/2026-11-24/adjoint/references/shooting_decimal.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/references/shooting_decimal.py)
- [/code/validated-examples/2026-11-24/adjoint/references/linear_oracle.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/references/linear_oracle.py)
- [/code/validated-examples/2026-11-24/adjoint/balanced_operator.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/balanced_operator.py)
- [/code/validated-examples/2026-11-24/adjoint/state_linear.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/state_linear.py)
- [/code/validated-examples/2026-11-24/adjoint/state_expansion.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/state_expansion.py)
- [/code/validated-examples/2026-11-24/adjoint/state_krylov.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/state_krylov.py)
- [/code/validated-examples/2026-11-24/adjoint/state_jacobian.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/state_jacobian.py)
- [/code/validated-examples/2026-11-24/adjoint/distributed.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/distributed.py)
- [/code/validated-examples/2026-11-24/adjoint/time_adjoint.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/time_adjoint.py)
- [/code/validated-examples/2026-11-24/adjoint/io_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/io_contract.py)
- [/code/validated-examples/2026-11-24/adjoint/qualify_references.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/qualify_references.py)
- [/code/validated-examples/2026-11-24/adjoint/tests/conftest.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/tests/conftest.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/run.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/experiments.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/io_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/io_contract.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/reference_eval.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/reference_eval.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/models.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/stiff.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/stiff.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/reporting_policy.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/reporting_policy.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/dopri.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/dopri.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/tableau.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/tableau.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/boundary.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/boundary.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/boundary_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/boundary_reference.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/coefficient_exact.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/coefficient_exact.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/qualify.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/qualify.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/reference_models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/reference_models.py)
- [/code/validated-examples/2026-11-24/dae-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/run.py)
- [/code/validated-examples/2026-11-24/dae-controls/models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/models.py)
- [/code/validated-examples/2026-11-24/dae-controls/newton.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/newton.py)
- [/code/validated-examples/2026-11-24/dae-controls/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/experiments.py)
- [/code/validated-examples/2026-11-24/dae-controls/io_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/io_contract.py)
- [/code/validated-examples/2026-11-24/dae-controls/references.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/references.py)
- [/code/validated-examples/2026-11-24/dae-controls/reporting.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/reporting.py)
- [/code/validated-examples/2026-11-25/small-models/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/run.py)
- [/code/validated-examples/2026-11-25/small-models/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/experiments.py)
- [/code/validated-examples/2026-11-25/small-models/io_utils.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/io_utils.py)
- [/code/validated-examples/2026-11-25/small-models/biology.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/biology.py)
- [/code/validated-examples/2026-11-25/small-models/pinn.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/pinn.py)
- [/code/validated-examples/2026-11-25/small-models/fno.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/fno.py)
- [/code/validated-examples/2026-11-25/small-models/data_family.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/data_family.py)
- [/code/validated-examples/2026-11-25/small-models/references/oracles.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/references/oracles.py)
- [/code/validated-examples/2026-11-25/small-models/references/qualify.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/references/qualify.py)
- [/code/validated-examples/2026-11-25/small-models/references/reference_models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/references/reference_models.py)

###### Package tests

- [/code/numerical-methods-atlas/2026-11-21/tests/test_sparse_fem.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_sparse_fem.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/test_bratu.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/test_bratu.py)
- [/code/validated-examples/2026-11-24/globalization-controls/test_globalization.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/test_globalization.py)
- [/code/validated-examples/2026-11-24/adjoint/tests/test_distributed.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/tests/test_distributed.py)
- [/code/validated-examples/2026-11-24/adjoint/tests/test_fold.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/tests/test_fold.py)
- [/code/validated-examples/2026-11-24/adjoint/tests/test_time.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/tests/test_time.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_boundary.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_boundary.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_contract.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_dopri.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_dopri.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_reporting.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_reporting.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_stiff.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_stiff.py)
- [/code/validated-examples/2026-11-24/dae-controls/test_cases.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/test_cases.py)
- [/code/validated-examples/2026-11-24/dae-controls/test_serialization.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/test_serialization.py)
- [/code/validated-examples/2026-11-25/small-models/test_models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/test_models.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q tests/test_sparse_fem.py
```
