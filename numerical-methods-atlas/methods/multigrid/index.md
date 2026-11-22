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
