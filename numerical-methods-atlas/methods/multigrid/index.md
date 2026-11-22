# Geometric multigrid V-cycle / 幾何マルチグリッドVサイクル

Status: educational-example

Geometric multigrid combines fine-grid smoothing with coarse-grid correction of smooth error. The public implementation is a fixed-hierarchy V-cycle for zero-Dirichlet Poisson on the unit square.

細格子で平滑化し、粗格子で滑らかな誤差を補正する幾何学的多重格子法。公開実装は単位正方形の零Dirichlet Poisson問題に対する固定階層のV-cycle。

An educational fixed-square, constant-coefficient nested-grid example. It does not implement AMG, irregular meshes, adaptive refinement or specialized smoothing for strong anisotropy/discontinuous coefficients. It does not establish all capabilities of Brandt's paper or optimal work for arbitrary problems.

Other names: マルチグリッド法, 多重格子法, multigrid method, geometric multigrid, GMG, V-cycle, Vサイクル


## 条件と確認範囲 (ja)

problem: 定係数Poisson方程式の五点差分連立系。

variant: 再離散化した粗格子作用素とfull weighting/双線形転送を使う、red-black GSの幾何V-cycle。

use_when:
- 規則的な入れ子正方格子のPoissonを解くとき。
- 緩和だけでは減りにくい滑らかな誤差と粗格子補正を比較して学ぶとき。

avoid_when:
- 非入れ子格子、曲がった領域、係数の強い異方性をそのまま入力する場合。
- この例をそのままAMGや汎用楕円ソルバーとみなす場合。

assumptions [specified]:
- 定係数の −Δu=f、正方形の一様内部格子、各軸 n=2^k−1 の入れ子格子を仮定する。
- 粗格子作用素は五点差分の再離散化。full weighting制限、双線形補間、red-black Gauss–Seidelの前後各3回平滑化を標準とする。
- 最粗格子1未知数は厳密に解く。停止判定は公開入口により絶対値を併用した残差または共通比較用の真の相対残差。
格子条件・転送・平滑化・粗格子解法を関数から確認した。

units [specified]:
公開問題は無次元の [0,1]²、h=1/(n+1)。次元を与える場合 [f]=[u]/[長さ]²、残差ノルムは格子重みなし。
単位正方形とhの規約を確認した。

boundary_conditions [specified]:
[0,1]² の全辺で u=0。誤差補正も零Dirichletで、ゼロ埋め込みにより境界値を入れる。
作用素と転送は零Dirichletのゼロ埋め込みを使う。

limitations [specified]:
固定された正方形・定係数・入れ子格子の教育例。AMG、不規則格子、適応細分化、強い異方性や不連続係数用の特別な平滑化は実装しない。Brandt論文の全機能や任意問題での最適計算量を示すものではない。
実装された幾何V-cycleの範囲に限定した。

Review: multigrid.pyの全関数と、固定点・転送・CG照合・残差・緩和との比較・非入れ子格子拒否の既存検査を読んだ。今回は再実行していない。

Not checked:
- 異方性・不連続係数や一般境界での頑健性。
- 新しい収束率・計算時間測定。

Evidence:
- v_cycle, solve_poisson_multigrid, restrict_full_weighting, prolong_bilinear: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/multigrid.py
- solve(method='multigrid'): https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/poisson_comparison.py
- existing multigrid consistency and convergence tests: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_multigrid.py

References:
- [formulation / primary-research] Brandt, A. (1977). Multi-Level Adaptive Solutions to Boundary-Value Problems. — https://doi.org/10.1090/S0025-5718-1977-0431719-X
  粗密の格子間で情報を交換する多重格子法の一次研究。論文中の適応格子機能を実装済みとはしない。
  abstract-and-metadata (2026-11-22); Abstract on printed p. 333 available in indexed primary-paper text; full PDF fetched but no readable body extracted. Author bibliography separately checked.; https://web.stanford.edu/class/cme324/classics/brandt.pdf

## Conditions and review scope (en)

problem: The five-point discrete system for constant-coefficient Poisson.

variant: Geometric V-cycle with rediscretized coarse operators, full weighting, bilinear transfer and red-black GS.

use_when:
- Solving Poisson on a regular nested square hierarchy.
- Studying smooth-error removal by coarse correction versus relaxation alone.

avoid_when:
- Direct input of non-nested meshes, curved domains or strongly anisotropic coefficients.
- Treating this example as AMG or a general elliptic solver.

assumptions [specified]:
- Constant-coefficient −Δu=f on a uniform square interior grid with n=2^k−1 per axis.
- Coarse operators are rediscretized five-point operators; restriction is full weighting, prolongation bilinear, with three red-black Gauss–Seidel pre/post sweeps by default.
- The one-unknown coarsest problem is solved exactly. Entry points use either mixed absolute/relative residual stopping or the comparison's true relative residual.
Inspected grid restrictions, transfer, smoothing and coarse solve.

units [specified]:
The public problem uses dimensionless [0,1]² and h=1/(n+1). Dimensionally [f]=[u]/[length]²; residual norms have no mesh weights.
Checked unit-square and h conventions.

boundary_conditions [specified]:
u=0 on all sides of [0,1]². Error corrections also have homogeneous Dirichlet boundaries, implemented by zero padding.
Operator and transfer use zero padding for zero Dirichlet boundaries.

limitations [specified]:
An educational fixed-square, constant-coefficient nested-grid example. It does not implement AMG, irregular meshes, adaptive refinement or specialized smoothing for strong anisotropy/discontinuous coefficients. It does not establish all capabilities of Brandt's paper or optimal work for arbitrary problems.
Scoped to the implemented geometric V-cycle.

Review: Inspected multigrid.py and existing fixed-point, transfer, CG-agreement, residual, relaxation-comparison and non-nested-grid rejection tests; no rerun.

Not checked:
- Robustness for anisotropy, discontinuous coefficients or general boundaries.
- New convergence-rate or timing measurements.

Evidence:
- v_cycle, solve_poisson_multigrid, restrict_full_weighting, prolong_bilinear: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/multigrid.py
- solve(method='multigrid'): https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/poisson_comparison.py
- existing multigrid consistency and convergence tests: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_multigrid.py

References:
- [formulation / primary-research] Brandt, A. (1977). Multi-Level Adaptive Solutions to Boundary-Value Problems. — https://doi.org/10.1090/S0025-5718-1977-0431719-X
  Primary multilevel boundary-value research; its adaptive capabilities are not claimed for the fixed-grid atlas example.
  abstract-and-metadata (2026-11-22); Abstract on printed p. 333 available in indexed primary-paper text; full PDF fetched but no readable body extracted. Author bibliography separately checked.; https://web.stanford.edu/class/cme324/classics/brandt.pdf


- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/elliptic/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/elliptic/

- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/linear.py
- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/multigrid.py
- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/poisson_comparison.py

- Reference: https://doi.org/10.1090/S0025-5718-1977-0431719-X — Multilevel interaction for boundary-value solvers; the atlas implements only a fixed nested-grid geometric V-cycle.

Common execution records: [{"id": "poisson-2d-sine", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=ja#poisson-2d-sine-ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=en#poisson-2d-sine-en"}}]

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/multigrid/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [Poisson・Laplace方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#poisson-laplace-ja) (`poisson-laplace`; poisson-2d-broad, poisson-2d-localized, poisson-2d-sine, poisson-2d-uniform)

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

##### [2次元Poisson・一様ソース](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-uniform/?lang=ja) (`poisson-2d-uniform`)

![保存済み一様ソースPoisson問題のマルチグリッド残差。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/poisson-2d-uniform.png)

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-uniform/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-uniform/?lang=ja#code-ja)

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

##### [2次元Poisson・一様ソース](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-uniform/?lang=ja#references-ja) (`poisson-2d-uniform`)

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

- [Poisson / Laplace equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#poisson-laplace-en) (`poisson-laplace`; poisson-2d-broad, poisson-2d-localized, poisson-2d-sine, poisson-2d-uniform)

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

##### [2D Poisson / uniform source](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-uniform/?lang=en) (`poisson-2d-uniform`)

![Stored multigrid residual history for uniform-source Poisson.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/poisson-2d-uniform.png)

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-uniform/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-uniform/?lang=en#code-en)

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

##### [2D Poisson / uniform source](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-uniform/?lang=en#references-en) (`poisson-2d-uniform`)

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
