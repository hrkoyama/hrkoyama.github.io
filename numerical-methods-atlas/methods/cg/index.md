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

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [Poisson・Laplace方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#poisson-laplace-ja) (`poisson-laplace`; poisson-2d-broad, poisson-2d-localized, poisson-2d-sine, poisson-2d-random)

#### 問題の図 (`method-problems-ja`)

##### [2次元Poisson・広帯域の滑らかな製造解](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-broad/?lang=ja) (`poisson-2d-broad`)

![保存済みの広帯域ソースと離散Poisson解。](https://hrkoyama.github.io/numerical-methods-atlas/assets/poisson-comparison/manufactured-63-fields.png)

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-broad/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-broad/?lang=ja#code-ja)

この手法でこの問題を解く固定入力実行例は未登録です。

##### [2次元Poisson・局在ソース](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-localized/?lang=ja) (`poisson-2d-localized`)

![保存済み局在ソースと離散Poisson解。](https://hrkoyama.github.io/numerical-methods-atlas/assets/poisson-comparison/localized-63-fields.png)

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-localized/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-localized/?lang=ja#code-ja)

この手法でこの問題を解く固定入力実行例は未登録です。

##### [2次元Poisson・正弦単一モード（FEMを含む）](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=ja) (`poisson-2d-sine`)

![同じ正弦製造解を解く、三角形有限要素の保存解と誤差。](https://hrkoyama.github.io/numerical-methods-atlas/assets/field-fem-poisson.png)

この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=ja#code-ja)

- [2次元Poisson：CG・多重格子とP1 FEM](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/poisson-2d-sine/?lang=ja) (`poisson-2d-sine`) · [コードZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

単位正方形のsin(πx)sin(πy)を参照し、CG/MGは15/31/63内部点、P1 FEMは4/8/16分割で細分化。FDの最大誤差と真の残差、FEMの要素内L2誤差とH1半ノルムを独立に評価する。

##### [2次元Poisson・乱数ソースの離散残差](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-random/?lang=ja) (`poisson-2d-random`)

![公開コード版を固定条件で実行して作成した計算結果。条件・値・検査結果を添付。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/poisson-2d-random.png)

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-random/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-random/?lang=ja#code-ja)

この手法でこの問題を解く固定入力実行例は未登録です。


#### 厳密解・参照解 (`method-references-ja`)

##### [2次元Poisson・広帯域の滑らかな製造解](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-broad/?lang=ja#references-ja) (`poisson-2d-broad`)

- [Poisson／正弦波の製造解](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-poisson-manufactured-ja) (`poisson-manufactured`; 関連モデルの参照; 製造解)

同じPoisson製造解の考え方ですが、カードは1次元単一正弦、こちらは2次元の滑らかな複合ソースです。

[既存の参照図](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=poisson-manufactured)

##### [2次元Poisson・局在ソース](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-localized/?lang=ja#references-ja) (`poisson-2d-localized`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### [2次元Poisson・正弦単一モード（FEMを含む）](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=ja#references-ja) (`poisson-2d-sine`)

- [Poisson／正弦波の製造解](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-poisson-manufactured-ja) (`poisson-manufactured`; 関連モデルの参照; 製造解)

カードは1次元sin(πx)、こちらは2次元sin(πx)sin(πy)です。次元・右辺・FEMの誤差ノルムは異なります。

[既存の参照図](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=poisson-manufactured)

##### [2次元Poisson・乱数ソースの離散残差](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-random/?lang=ja#references-ja) (`poisson-2d-random`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/elliptic/)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

##### 2次元Poisson：CG・多重格子とP1 FEM (`poisson-2d-sine`)

[2次元Poisson・正弦単一モード（FEMを含む）](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/poisson-2d-sine/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

[固定入力](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/recipes/poisson-2d-sine.json)

[検証記録](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

単位正方形のsin(πx)sin(πy)を参照し、CG/MGは15/31/63内部点、P1 FEMは4/8/16分割で細分化。FDの最大誤差と真の残差、FEMの要素内L2誤差とH1半ノルムを独立に評価する。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

Related chapter modules and test files; not a claim that each test covers every named method.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### 関連ソース

- [/code/numerical-methods-atlas/2026-11-21/numart/linear.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/linear.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/multigrid.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/multigrid.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/poisson_comparison.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/poisson_comparison.py)

###### 配布版のテスト

- [/code/numerical-methods-atlas/2026-11-21/tests/test_linear.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_linear.py)
- [/code/numerical-methods-atlas/2026-11-21/tests/test_multigrid.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_multigrid.py)
- [/code/numerical-methods-atlas/2026-11-21/tests/test_poisson_comparison.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_poisson_comparison.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q tests/test_linear.py tests/test_multigrid.py tests/test_poisson_comparison.py
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Poisson / Laplace equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#poisson-laplace-en) (`poisson-laplace`; poisson-2d-broad, poisson-2d-localized, poisson-2d-sine, poisson-2d-random)

#### Problem figures (`method-problems-en`)

##### [2D Poisson / broad smooth manufactured forcing](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-broad/?lang=en) (`poisson-2d-broad`)

![Stored broad smooth forcing and discrete Poisson solution.](https://hrkoyama.github.io/numerical-methods-atlas/assets/poisson-comparison/manufactured-63-fields.png)

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-broad/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-broad/?lang=en#code-en)

No fixed-input execution of this problem is registered for this method.

##### [2D Poisson / localized source](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-localized/?lang=en) (`poisson-2d-localized`)

![Stored localized forcing and discrete Poisson solution.](https://hrkoyama.github.io/numerical-methods-atlas/assets/poisson-comparison/localized-63-fields.png)

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-localized/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-localized/?lang=en#code-en)

No fixed-input execution of this problem is registered for this method.

##### [2D Poisson / single sine mode, including FEM](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=en) (`poisson-2d-sine`)

![Stored triangular-FEM solution and error for the same sine manufactured problem.](https://hrkoyama.github.io/numerical-methods-atlas/assets/field-fem-poisson.png)

Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=en#code-en)

- [2D Poisson: CG, multigrid and P1 FEM](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/poisson-2d-sine/?lang=en) (`poisson-2d-sine`) · [Code ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

Reference sin(πx)sin(πy) on the unit square; refine CG/MG through 15/31/63 interior nodes and P1 FEM through 4/8/16 subdivisions. Independently evaluate FD maximum errors/true residuals and FEM element-interior L2/H1-seminorm errors.

##### [2D Poisson / random-source discrete residual](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-random/?lang=en) (`poisson-2d-random`)

![Calculated from the public code edition with fixed inputs; inputs, values and checks are linked.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/poisson-2d-random.png)

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-random/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-random/?lang=en#code-en)

No fixed-input execution of this problem is registered for this method.


#### Exact / reference solutions (`method-references-en`)

##### [2D Poisson / broad smooth manufactured forcing](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-broad/?lang=en#references-en) (`poisson-2d-broad`)

- [Poisson / manufactured sine](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-poisson-manufactured-en) (`poisson-manufactured`; Related-model reference; Manufactured solution)

Both use manufactured Poisson solutions, but the card is a 1D single sine while this test uses a smooth composite 2D source.

[Existing reference profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=poisson-manufactured)

##### [2D Poisson / localized source](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-localized/?lang=en#references-en) (`poisson-2d-localized`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### [2D Poisson / single sine mode, including FEM](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=en#references-en) (`poisson-2d-sine`)

- [Poisson / manufactured sine](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-poisson-manufactured-en) (`poisson-manufactured`; Related-model reference; Manufactured solution)

The card is 1D sin(πx); this test is 2D sin(πx)sin(πy). Dimension, forcing and FEM error norms differ.

[Existing reference profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=poisson-manufactured)

##### [2D Poisson / random-source discrete residual](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-random/?lang=en#references-en) (`poisson-2d-random`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/elliptic/)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

##### 2D Poisson: CG, multigrid and P1 FEM (`poisson-2d-sine`)

[2D Poisson / single sine mode, including FEM](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/poisson-2d-sine/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

[Fixed input](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/recipes/poisson-2d-sine.json)

[Verification receipt](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

Reference sin(πx)sin(πy) on the unit square; refine CG/MG through 15/31/63 interior nodes and P1 FEM through 4/8/16 subdivisions. Independently evaluate FD maximum errors/true residuals and FEM element-interior L2/H1-seminorm errors.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Related chapter modules and test files; not a claim that each test covers every named method.

[Related code edition / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### Related source

- [/code/numerical-methods-atlas/2026-11-21/numart/linear.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/linear.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/multigrid.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/multigrid.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/poisson_comparison.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/poisson_comparison.py)

###### Package tests

- [/code/numerical-methods-atlas/2026-11-21/tests/test_linear.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_linear.py)
- [/code/numerical-methods-atlas/2026-11-21/tests/test_multigrid.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_multigrid.py)
- [/code/numerical-methods-atlas/2026-11-21/tests/test_poisson_comparison.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_poisson_comparison.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q tests/test_linear.py tests/test_multigrid.py tests/test_poisson_comparison.py
```
