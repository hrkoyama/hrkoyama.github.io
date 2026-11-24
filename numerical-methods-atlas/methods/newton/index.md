# Armijo-damped Newton / Armijo減衰Newton法

Status: educational-example

Solve F(x)=0 using a Jacobian-based Newton direction and damping that requires sufficient decrease of the residual norm. The example supports a dense or preconditioned GMRES inner solve. Additional fixed examples: Crossing the Bratu fold with pseudo-arclength continuation. See each release for assumptions and checked scope.

非線形方程式 F(x)=0 を、Jacobianから求めたNewton方向と残差ノルムの十分減少による減衰で解く。公開例は密行列解法または前処理付きGMRESの内部解法を選べる。 追加固定例：擬似弧長継続でBratuのfoldを越える。条件と検証範囲は各配布版で確認してください。

Convergence depends on the initial guess, Jacobian nonsingularity and residual scaling; global convergence is not guaranteed. Singular dense solves or preconditioner construction may raise exceptions rather than return a failure reason. No matrix-free Jv, trust region or continuation is provided. Additional fixed examples: A small one-dimensional simple fold only. The whole-curve family comparison uses the computed midpoint as its family coordinate and is distinct from the independent fixed-lambda profile checks. The continuum fold is not an exact discrete solution. No general bifurcation-tracking or large-scale performance claim.

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
初期値、Jacobianの非特異性、残差の尺度に依存し、大域的収束は保証しない。特異な密行列解法や前処理構築は例外となることがあり、すべてが失敗理由の戻り値に変換されるわけではない。行列なしJv、信頼領域、継続法は備えない。 追加固定例：小さな1次元の単純foldだけです。分岐曲線の解析族比較では計算した中点値を族の座標に使い、固定λの独立形状比較と区別します。連続foldは離散解そのものではなく、一般の分岐追跡や大規模性能は保証しません。
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
Convergence depends on the initial guess, Jacobian nonsingularity and residual scaling; global convergence is not guaranteed. Singular dense solves or preconditioner construction may raise exceptions rather than return a failure reason. No matrix-free Jv, trust region or continuation is provided. Additional fixed examples: A small one-dimensional simple fold only. The whole-curve family comparison uses the computed midpoint as its family coordinate and is distinct from the independent fixed-lambda profile checks. The continuum fold is not an exact discrete solution. No general bifurcation-tracking or large-scale performance claim.
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

Common execution records: [{"id": "bratu", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=ja#bratu-ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=en#bratu-en"}}, {"id": "bratu-fold-continuation", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-continuation/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-continuation/?lang=en"}, "kind": "dedicated-supplement"}]

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [Bratu非線形境界値問題](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bratu-ja) (`bratu`; bratu, bratu-fold-continuation)

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


#### 厳密解・参照解 (`method-references-ja`)

##### [1次元Bratu非線形境界値問題](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu/?lang=ja#references-ja) (`bratu`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### [減衰Newton法による3次方程式の求根](https://hrkoyama.github.io/numerical-methods-atlas/problems/cubic-root/?lang=ja#references-ja) (`cubic-root`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### [擬似弧長継続でBratuのfoldを越える](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-continuation/?lang=ja#references-ja) (`bratu-fold-continuation`)

- [擬似弧長継続でBratuのfoldを越える](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-bratu-fold-continuation-ja) (`bratu-fold-continuation`; 同じ問題の参照; 解析参照)

小さな1次元の単純foldだけです。分岐曲線の解析族比較では計算した中点値を族の座標に使い、固定λの独立形状比較と区別します。連続foldは離散解そのものではなく、一般の分岐追跡や大規模性能は保証しません。

[既存の参照図](/numerical-methods-atlas/validation/bratu-fold-continuation/?lang=ja#bratu-fold-continuation-ja-measurements)

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

###### 配布版のテスト

- [/code/numerical-methods-atlas/2026-11-21/tests/test_sparse_fem.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_sparse_fem.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/test_bratu.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/test_bratu.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q tests/test_sparse_fem.py
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Bratu nonlinear boundary-value problem](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bratu-en) (`bratu`; bratu, bratu-fold-continuation)

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


#### Exact / reference solutions (`method-references-en`)

##### [One-dimensional Bratu boundary-value problem](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu/?lang=en#references-en) (`bratu`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### [Damped Newton root of a cubic equation](https://hrkoyama.github.io/numerical-methods-atlas/problems/cubic-root/?lang=en#references-en) (`cubic-root`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### [Crossing the Bratu fold with pseudo-arclength continuation](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-continuation/?lang=en#references-en) (`bratu-fold-continuation`)

- [Crossing the Bratu fold with pseudo-arclength continuation](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-bratu-fold-continuation-en) (`bratu-fold-continuation`; Same-problem reference; Analytic reference)

A small one-dimensional simple fold only. The whole-curve family comparison uses the computed midpoint as its family coordinate and is distinct from the independent fixed-lambda profile checks. The continuum fold is not an exact discrete solution. No general bifurcation-tracking or large-scale performance claim.

[Existing reference profile](/numerical-methods-atlas/validation/bratu-fold-continuation/?lang=en#bratu-fold-continuation-en-measurements)

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

###### Package tests

- [/code/numerical-methods-atlas/2026-11-21/tests/test_sparse_fem.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_sparse_fem.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/test_bratu.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/test_bratu.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q tests/test_sparse_fem.py
```
