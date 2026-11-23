# Conjugate gradients / 共役勾配法

Status: educational-example

Existing releases: Solve real SPD linear systems by conjugate directions. The public example is unpreconditioned matrix-free CG for the five-point zero-Dirichlet Poisson operator on a unit square. Additional fixed examples: Checkerboard diffusion: shared flux, MG and AMG, Rotated diffusion: full-tensor Q1, MG and AMG. See each release for assumptions and checked scope.

既存配布版：実対称正定値な連立一次方程式を共役方向で反復的に解く。公開例は単位正方形・零Dirichlet Poisson方程式の五点差分を、行列を組み立てずに扱う前処理なしCG。 追加固定例：係数ジャンプ拡散：共有流束とMG・AMG、回転異方性拡散：完全テンソルQ1とMG・AMG。条件と検証範囲は各配布版で確認してください。

Limits of existing releases: Do not apply this variant directly to nonsymmetric, indefinite or singular systems. This CG example has no preconditioner, general sparse-matrix interface or pure-Neumann nullspace handling. A small residual does not certify discretization accuracy; rapid termination for one eigenmode is not a general performance result. Additional fixed examples: Fixed contrast100 example. P1 differences are not rigorous error bounds; no singular exponent or universal MG/AMG winner is asserted. One angle/anisotropy only. Scalar TPFA is not extended to rotated tensors; arbitrary-tensor robustness is not established.

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
既存配布版の制約：非対称・不定・特異な系にそのまま適用しない。前処理、一般疎行列入力、純Neumannの零空間処理はこのCG例にはない。小さい残差は離散化誤差の保証ではなく、単一固有モードの速い終了を一般的性能と解釈しない。 今回の追加固定例：係数比100の固定例。P1格子差は厳密誤差上界ではなく、特異交点の次数や普遍的なMG/AMG優劣は主張しません。 指定した角度・異方性の限定例。スカラーTPFAを回転テンソルへ転用せず、一般テンソルへの頑健性は保証しません。
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
Limits of existing releases: Do not apply this variant directly to nonsymmetric, indefinite or singular systems. This CG example has no preconditioner, general sparse-matrix interface or pure-Neumann nullspace handling. A small residual does not certify discretization accuracy; rapid termination for one eigenmode is not a general performance result. Additional fixed examples: Fixed contrast100 example. P1 differences are not rigorous error bounds; no singular exponent or universal MG/AMG winner is asserted. One angle/anisotropy only. Scalar TPFA is not extended to rotated tensors; arbitrary-tensor robustness is not established.
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

## Small fixed-input validation supplements

Additional compatible pure-Neumann Poisson uses CG from zero on the same singular operator; align only its constant mean gauge and compare a constrained direct solve. Reject incompatible forcing without source projection.

追加は適合した純Neumann Poisson系。同じ特異作用素で零からCGを実行し、定数分だけ平均ゲージを合わせ、平均拘束付き直接解と比較します。不適合な右辺は射影せず棄却します。

- Pure Neumann compatibility and mean gauge: https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-neumann/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/atlas-mesh-boundary-2026-11-23.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/result.json

- Checkerboard diffusion: shared flux, MG and AMG: https://hrkoyama.github.io/numerical-methods-atlas/validation/checkerboard-diffusion/
- Rotated diffusion: full-tensor Q1, MG and AMG: https://hrkoyama.github.io/numerical-methods-atlas/validation/rotated-anisotropic-diffusion/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/atlas-coefficient-diffusion-2026-11-23.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/results/result.json

Common execution records: [{"id": "poisson-2d-sine", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=ja#poisson-2d-sine-ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=en#poisson-2d-sine-en"}}, {"id": "poisson-neumann", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-neumann/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-neumann/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "checkerboard-diffusion", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/checkerboard-diffusion/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/checkerboard-diffusion/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "rotated-anisotropic-diffusion", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/rotated-anisotropic-diffusion/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/rotated-anisotropic-diffusion/?lang=en"}, "kind": "dedicated-supplement"}]

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/cg/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [Poisson・Laplace方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#poisson-laplace-ja) (`poisson-laplace`; poisson-2d-broad, poisson-2d-localized, poisson-2d-sine, poisson-2d-random, poisson-neumann)
- [不連続係数・完全テンソル拡散の境界値問題](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#tensor-diffusion-ja) (`tensor-diffusion`; checkerboard-diffusion, rotated-anisotropic-diffusion)

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

この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。 SEMはC0連続なテンソル積Qp Lagrange基底・p+1個のLegendre GLL節点と求積、疎な剛性行列・SciPy直接解法を使用。p=2で各方向2/4/8要素、別に2×2要素でp=1〜6。公開済みNumartのP1 FEM・GMRESをファイルのバイト列を保持して4/8/16分割で実行し、両者の自由未知数9/49/225を一致させます。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=ja#code-ja)

- [2次元Poisson：CG・多重格子とP1 FEM](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/poisson-2d-sine/?lang=ja) (`poisson-2d-sine`) · [コードZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

単位正方形のsin(πx)sin(πy)を参照し、CG/MGは15/31/63内部点、P1 FEMは4/8/16分割で細分化。FDの最大誤差と真の残差、FEMの要素内L2誤差とH1半ノルムを独立に評価する。

##### [2次元Poisson・乱数ソースの離散残差](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-random/?lang=ja) (`poisson-2d-random`)

![公開コード版を固定条件で実行して作成した計算結果。条件・値・検査結果を添付。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/poisson-2d-random.png)

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-random/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-random/?lang=ja#code-ja)

この手法でこの問題を解く固定入力実行例は未登録です。

##### [純Neumannの互換条件と平均値ゲージ](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-neumann/?lang=ja) (`poisson-neumann`)

![実際に保存した計算配列と固定入力の収束指標から描いた検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/poisson-neumann-preview.png)

共有面差分で特異行列を組み、体積重み平均のLagrange拘束付き疎直接法とcompatible CGを照合。物理的な不適合外力の平均を勝手に引かない。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-neumann/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-neumann/?lang=ja#code-ja)

- [純Neumannの互換条件と平均値ゲージ](https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-neumann/?lang=ja) (`poisson-neumann`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/atlas-mesh-boundary-2026-11-23.zip)

特異な2D Poissonを互換条件と指定平均込みで解き、不適合な外力を拒否します。

##### [係数ジャンプ拡散：共有流束とMG・AMG](https://hrkoyama.github.io/numerical-methods-atlas/problems/checkerboard-diffusion/?lang=ja) (`checkerboard-diffusion`)

![保存した2D解・誤差・真の残差・格子感度の検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/results/checkerboard-diffusion-preview.png)

直交FVの共有面調和平均。幾何MGと座標を受け取らないSA-AMGの対称Galerkin V-cycleを、同じ行列のPCGへ適用。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/checkerboard-diffusion/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/checkerboard-diffusion/?lang=ja#code-ja)

- [係数ジャンプ拡散：共有流束とMG・AMG](https://hrkoyama.github.io/numerical-methods-atlas/validation/checkerboard-diffusion/?lang=ja) (`checkerboard-diffusion`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/atlas-coefficient-diffusion-2026-11-23.zip)

不連続係数のFV解を独立なP1参照と比較し、線形系の残差・前進誤差と連続問題の誤差を分けます。

##### [回転異方性拡散：完全テンソルQ1とMG・AMG](https://hrkoyama.github.io/numerical-methods-atlas/problems/rotated-anisotropic-diffusion/?lang=ja) (`rotated-anisotropic-diffusion`)

![保存した2D解・誤差・真の残差・格子感度の検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/results/rotated-anisotropic-diffusion-preview.png)

完全2×2テンソルQ1とGauss積分。MG/SA-AMGは対称2/2Jacobi、Galerkin粗行列、粗CholeskyでSPDの固定適用。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/rotated-anisotropic-diffusion/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/rotated-anisotropic-diffusion/?lang=ja#code-ja)

- [回転異方性拡散：完全テンソルQ1とMG・AMG](https://hrkoyama.github.io/numerical-methods-atlas/validation/rotated-anisotropic-diffusion/?lang=ja) (`rotated-anisotropic-diffusion`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/atlas-coefficient-diffusion-2026-11-23.zip)

非零Kxyを保つQ1弱形式で、解析解への収束と同じ行列のMG・AMG収束を比較します。


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

- [2D Poisson正弦製造解：SEMとP1 FEMの共通参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-sem-poisson-2d-ja) (`sem-poisson-2d`; 同じ問題の参照; 製造解)

全て無次元。−Δu=2π²sin(πx)sin(πy)、領域[0,1]²、境界u=0。係数は一定、SEMは直交するアフィン正方形、FEMは既存の規則的な三角形分割。

[既存の参照図](/numerical-methods-atlas/validation/sem-poisson-2d/?lang=ja)

##### [2次元Poisson・乱数ソースの離散残差](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-random/?lang=ja#references-ja) (`poisson-2d-random`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### [純Neumannの互換条件と平均値ゲージ](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-neumann/?lang=ja#references-ja) (`poisson-neumann`)

- [純Neumann：解析場・互換条件・平均値ゲージ](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-poisson-neumann-ja) (`poisson-neumann`; 同じ問題の参照; 製造解)

同じ半離散系の別線形解法は独立PDE参照ではありません。既存Dirichlet MGの成功や2D任意境界へ一般化しません。

[既存の参照図](/numerical-methods-atlas/validation/poisson-neumann/?lang=ja#poisson-neumann-ja-measurements)

##### [係数ジャンプ拡散：共有流束とMG・AMG](https://hrkoyama.github.io/numerical-methods-atlas/problems/checkerboard-diffusion/?lang=ja#references-ja) (`checkerboard-diffusion`)

- [係数ジャンプ拡散：共有流束とMG・AMG](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-checkerboard-diffusion-ja) (`checkerboard-diffusion`; 同じ問題の参照; 有限格子の数値参照)

係数比100の固定例。P1格子差は厳密誤差上界ではなく、特異交点の次数や普遍的なMG/AMG優劣は主張しません。

[既存の参照図](/numerical-methods-atlas/validation/checkerboard-diffusion/?lang=ja#checkerboard-diffusion-ja-measurements)

##### [回転異方性拡散：完全テンソルQ1とMG・AMG](https://hrkoyama.github.io/numerical-methods-atlas/problems/rotated-anisotropic-diffusion/?lang=ja#references-ja) (`rotated-anisotropic-diffusion`)

- [回転異方性拡散：完全テンソルQ1とMG・AMG](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-rotated-anisotropic-diffusion-ja) (`rotated-anisotropic-diffusion`; 同じ問題の参照; 製造解)

指定した角度・異方性の限定例。スカラーTPFAを回転テンソルへ転用せず、一般テンソルへの頑健性は保証しません。

[既存の参照図](/numerical-methods-atlas/validation/rotated-anisotropic-diffusion/?lang=ja#rotated-anisotropic-diffusion-ja-measurements)

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

##### 純Neumannの互換条件と平均値ゲージ (`poisson-neumann`)

[純Neumannの互換条件と平均値ゲージ](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-neumann/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-neumann/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/atlas-mesh-boundary-2026-11-23.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/verification.json)

特異な2D Poissonを互換条件と指定平均込みで解き、不適合な外力を拒否します。

##### 係数ジャンプ拡散：共有流束とMG・AMG (`checkerboard-diffusion`)

[係数ジャンプ拡散：共有流束とMG・AMG](https://hrkoyama.github.io/numerical-methods-atlas/problems/checkerboard-diffusion/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/checkerboard-diffusion/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/atlas-coefficient-diffusion-2026-11-23.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/verification.json)

不連続係数のFV解を独立なP1参照と比較し、線形系の残差・前進誤差と連続問題の誤差を分けます。

##### 回転異方性拡散：完全テンソルQ1とMG・AMG (`rotated-anisotropic-diffusion`)

[回転異方性拡散：完全テンソルQ1とMG・AMG](https://hrkoyama.github.io/numerical-methods-atlas/problems/rotated-anisotropic-diffusion/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/rotated-anisotropic-diffusion/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/atlas-coefficient-diffusion-2026-11-23.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/verification.json)

非零Kxyを保つQ1弱形式で、解析解への収束と同じ行列のMG・AMG収束を比較します。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

追加は適合した純Neumann Poisson系。同じ特異作用素で零からCGを実行し、定数分だけ平均ゲージを合わせ、平均拘束付き直接解と比較します。不適合な右辺は射影せず棄却します。

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### 関連ソース

- [/code/numerical-methods-atlas/2026-11-21/numart/linear.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/linear.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/multigrid.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/multigrid.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/poisson_comparison.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/poisson_comparison.py)
- [/code/validated-examples/2026-11-23/mesh-boundary/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/run.py)
- [/code/validated-examples/2026-11-23/mesh-boundary/boundary.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/boundary.py)
- [/code/validated-examples/2026-11-23/mesh-boundary/fem.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/fem.py)
- [/code/validated-examples/2026-11-23/mesh-boundary/annulus.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/annulus.py)
- [/code/validated-examples/2026-11-23/mesh-boundary/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/experiments.py)
- [/code/validated-examples/2026-11-23/mesh-boundary/references/fields.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/references/fields.py)
- [/code/validated-examples/2026-11-23/coefficient-diffusion/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/run.py)
- [/code/validated-examples/2026-11-23/coefficient-diffusion/operators.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/operators.py)
- [/code/validated-examples/2026-11-23/coefficient-diffusion/multilevel.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/multilevel.py)
- [/code/validated-examples/2026-11-23/coefficient-diffusion/references/p1.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/references/p1.py)
- [/code/validated-examples/2026-11-23/coefficient-diffusion/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/experiments.py)

###### 配布版のテスト

- [/code/numerical-methods-atlas/2026-11-21/tests/test_linear.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_linear.py)
- [/code/numerical-methods-atlas/2026-11-21/tests/test_multigrid.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_multigrid.py)
- [/code/numerical-methods-atlas/2026-11-21/tests/test_poisson_comparison.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_poisson_comparison.py)
- [/code/validated-examples/2026-11-23/mesh-boundary/test_geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/test_geometry.py)
- [/code/validated-examples/2026-11-23/coefficient-diffusion/test_diffusion.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/test_diffusion.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q tests/test_linear.py tests/test_multigrid.py tests/test_poisson_comparison.py
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Poisson / Laplace equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#poisson-laplace-en) (`poisson-laplace`; poisson-2d-broad, poisson-2d-localized, poisson-2d-sine, poisson-2d-random, poisson-neumann)
- [Discontinuous and full-tensor diffusion BVP](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#tensor-diffusion-en) (`tensor-diffusion`; checkerboard-diffusion, rotated-anisotropic-diffusion)

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

Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed. C0 tensor Qp Lagrange SEM with p+1 Legendre GLL nodes/quadrature, sparse stiffness assembly and a SciPy direct solve. At p=2 use2/4/8 elements per axis; separately fix2x2 elements and p=1..6. Execute the byte-identical published Numart triangle P1 FEM/GMRES at4/8/16 subdivisions, matching9/49/225 free unknowns.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=en#code-en)

- [2D Poisson: CG, multigrid and P1 FEM](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/poisson-2d-sine/?lang=en) (`poisson-2d-sine`) · [Code ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

Reference sin(πx)sin(πy) on the unit square; refine CG/MG through 15/31/63 interior nodes and P1 FEM through 4/8/16 subdivisions. Independently evaluate FD maximum errors/true residuals and FEM element-interior L2/H1-seminorm errors.

##### [2D Poisson / random-source discrete residual](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-random/?lang=en) (`poisson-2d-random`)

![Calculated from the public code edition with fixed inputs; inputs, values and checks are linked.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/poisson-2d-random.png)

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-random/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-random/?lang=en#code-en)

No fixed-input execution of this problem is registered for this method.

##### [Pure Neumann compatibility and mean gauge](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-neumann/?lang=en) (`poisson-neumann`)

![Validation preview from actual saved PDE arrays and fixed-input refinement measurements.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/poisson-neumann-preview.png)

Shared-face differences, weighted-mean augmented solve and compatible CG comparison; no physical RHS mean projection.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-neumann/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-neumann/?lang=en#code-en)

- [Pure Neumann compatibility and mean gauge](https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-neumann/?lang=en) (`poisson-neumann`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/atlas-mesh-boundary-2026-11-23.zip)

Solve singular2D Poisson with compatibility/gauge and reject incompatible source.

##### [Checkerboard diffusion: shared flux, MG and AMG](https://hrkoyama.github.io/numerical-methods-atlas/problems/checkerboard-diffusion/?lang=en) (`checkerboard-diffusion`)

![Saved2D solution, error, true residual and refinement/reference sensitivity.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/results/checkerboard-diffusion-preview.png)

Orthogonal FV with shared harmonic transmissibility. Symmetric Galerkin geometric and coordinate-free SA cycles precondition PCG on identical matrices.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/checkerboard-diffusion/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/checkerboard-diffusion/?lang=en#code-en)

- [Checkerboard diffusion: shared flux, MG and AMG](https://hrkoyama.github.io/numerical-methods-atlas/validation/checkerboard-diffusion/?lang=en) (`checkerboard-diffusion`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/atlas-coefficient-diffusion-2026-11-23.zip)

Compare discontinuous-coefficient FV with independent P1 reference fields, separating linear-system residual/forward errors from continuum error.

##### [Rotated diffusion: full-tensor Q1, MG and AMG](https://hrkoyama.github.io/numerical-methods-atlas/problems/rotated-anisotropic-diffusion/?lang=en) (`rotated-anisotropic-diffusion`)

![Saved2D solution, error, true residual and refinement/reference sensitivity.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/results/rotated-anisotropic-diffusion-preview.png)

Full2x2 tensor Q1 and Gauss quadrature. Fixed SPD MG/SA cycles use symmetric2/2Jacobi, Galerkin operators and coarse Cholesky.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/rotated-anisotropic-diffusion/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/rotated-anisotropic-diffusion/?lang=en#code-en)

- [Rotated diffusion: full-tensor Q1, MG and AMG](https://hrkoyama.github.io/numerical-methods-atlas/validation/rotated-anisotropic-diffusion/?lang=en) (`rotated-anisotropic-diffusion`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/atlas-coefficient-diffusion-2026-11-23.zip)

Retain nonzero Kxy in the Q1 weak form and compare analytic refinement with MG/AMG convergence for the same matrix.


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

- [2D Poisson sine manufactured solution: shared SEM/P1 FEM reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-sem-poisson-2d-en) (`sem-poisson-2d`; Same-problem reference; Manufactured solution)

Dimensionless: -Laplacian u=2pi²sin(pi x)sin(pi y) on[0,1]², u=0 on the boundary. Constant coefficient; affine Cartesian squares for SEM and the existing regular triangle mesh for P1 FEM.

[Existing reference profile](/numerical-methods-atlas/validation/sem-poisson-2d/?lang=en)

##### [2D Poisson / random-source discrete residual](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-random/?lang=en#references-en) (`poisson-2d-random`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### [Pure Neumann compatibility and mean gauge](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-neumann/?lang=en#references-en) (`poisson-neumann`)

- [Pure Neumann: analytic field, compatibility and mean gauge](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-poisson-neumann-en) (`poisson-neumann`; Same-problem reference; Manufactured solution)

A different linear solver of the same matrix is not an independent PDE discretization; no general boundary/MG claim.

[Existing reference profile](/numerical-methods-atlas/validation/poisson-neumann/?lang=en#poisson-neumann-en-measurements)

##### [Checkerboard diffusion: shared flux, MG and AMG](https://hrkoyama.github.io/numerical-methods-atlas/problems/checkerboard-diffusion/?lang=en#references-en) (`checkerboard-diffusion`)

- [Checkerboard diffusion: shared flux, MG and AMG](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-checkerboard-diffusion-en) (`checkerboard-diffusion`; Same-problem reference; Finite-grid numerical reference)

Fixed contrast100 example. P1 differences are not rigorous error bounds; no singular exponent or universal MG/AMG winner is asserted.

[Existing reference profile](/numerical-methods-atlas/validation/checkerboard-diffusion/?lang=en#checkerboard-diffusion-en-measurements)

##### [Rotated diffusion: full-tensor Q1, MG and AMG](https://hrkoyama.github.io/numerical-methods-atlas/problems/rotated-anisotropic-diffusion/?lang=en#references-en) (`rotated-anisotropic-diffusion`)

- [Rotated diffusion: full-tensor Q1, MG and AMG](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-rotated-anisotropic-diffusion-en) (`rotated-anisotropic-diffusion`; Same-problem reference; Manufactured solution)

One angle/anisotropy only. Scalar TPFA is not extended to rotated tensors; arbitrary-tensor robustness is not established.

[Existing reference profile](/numerical-methods-atlas/validation/rotated-anisotropic-diffusion/?lang=en#rotated-anisotropic-diffusion-en-measurements)

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

##### Pure Neumann compatibility and mean gauge (`poisson-neumann`)

[Pure Neumann compatibility and mean gauge](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-neumann/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-neumann/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/atlas-mesh-boundary-2026-11-23.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/verification.json)

Solve singular2D Poisson with compatibility/gauge and reject incompatible source.

##### Checkerboard diffusion: shared flux, MG and AMG (`checkerboard-diffusion`)

[Checkerboard diffusion: shared flux, MG and AMG](https://hrkoyama.github.io/numerical-methods-atlas/problems/checkerboard-diffusion/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/checkerboard-diffusion/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/atlas-coefficient-diffusion-2026-11-23.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/verification.json)

Compare discontinuous-coefficient FV with independent P1 reference fields, separating linear-system residual/forward errors from continuum error.

##### Rotated diffusion: full-tensor Q1, MG and AMG (`rotated-anisotropic-diffusion`)

[Rotated diffusion: full-tensor Q1, MG and AMG](https://hrkoyama.github.io/numerical-methods-atlas/problems/rotated-anisotropic-diffusion/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/rotated-anisotropic-diffusion/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/atlas-coefficient-diffusion-2026-11-23.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/verification.json)

Retain nonzero Kxy in the Q1 weak form and compare analytic refinement with MG/AMG convergence for the same matrix.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Additional compatible pure-Neumann Poisson uses CG from zero on the same singular operator; align only its constant mean gauge and compare a constrained direct solve. Reject incompatible forcing without source projection.

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[Related code edition / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### Related source

- [/code/numerical-methods-atlas/2026-11-21/numart/linear.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/linear.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/multigrid.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/multigrid.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/poisson_comparison.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/poisson_comparison.py)
- [/code/validated-examples/2026-11-23/mesh-boundary/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/run.py)
- [/code/validated-examples/2026-11-23/mesh-boundary/boundary.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/boundary.py)
- [/code/validated-examples/2026-11-23/mesh-boundary/fem.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/fem.py)
- [/code/validated-examples/2026-11-23/mesh-boundary/annulus.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/annulus.py)
- [/code/validated-examples/2026-11-23/mesh-boundary/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/experiments.py)
- [/code/validated-examples/2026-11-23/mesh-boundary/references/fields.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/references/fields.py)
- [/code/validated-examples/2026-11-23/coefficient-diffusion/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/run.py)
- [/code/validated-examples/2026-11-23/coefficient-diffusion/operators.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/operators.py)
- [/code/validated-examples/2026-11-23/coefficient-diffusion/multilevel.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/multilevel.py)
- [/code/validated-examples/2026-11-23/coefficient-diffusion/references/p1.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/references/p1.py)
- [/code/validated-examples/2026-11-23/coefficient-diffusion/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/experiments.py)

###### Package tests

- [/code/numerical-methods-atlas/2026-11-21/tests/test_linear.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_linear.py)
- [/code/numerical-methods-atlas/2026-11-21/tests/test_multigrid.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_multigrid.py)
- [/code/numerical-methods-atlas/2026-11-21/tests/test_poisson_comparison.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_poisson_comparison.py)
- [/code/validated-examples/2026-11-23/mesh-boundary/test_geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/test_geometry.py)
- [/code/validated-examples/2026-11-23/coefficient-diffusion/test_diffusion.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/test_diffusion.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q tests/test_linear.py tests/test_multigrid.py tests/test_poisson_comparison.py
```
