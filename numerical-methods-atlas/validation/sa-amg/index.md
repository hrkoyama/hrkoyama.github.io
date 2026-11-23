# 行列から粗視化するAMG：残差と解誤差を分ける

正方形Poisson問題から得たSPD行列だけを階層構築へ渡し、平滑化集約AMGのV-cycleを実行します。7²・15²・31²未知数で独立疎行列直接解、解析的な離散正弦モード、連続解への2次収束を分けて検査します。

**使用手法**

- [代数的マルチグリッド（AMG）](https://hrkoyama.github.io/numerical-methods-atlas/methods/amg/?lang=ja) (`amg`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/sa-amg/?lang=ja#sa-amg-ja-algorithm)

各行の最大非対角係数に対する相対強度からグラフを作り、貪欲な星型集約と余剰節点の隣接集約への付着で暫定補間Tを作ります。P=(I−ωD⁻¹A)T、ω=4/(3ρ̄)、ρ̄はD⁻¹Aの絶対行和上界です。粗演算子はPᵀAP。前後2回のJacobi平滑化と最終小行列の直接解を用います。これは採用した小規模SA変種であり、原著の全構築法や収束定理の再現ではありません。

$$
A_c=P^TAP,\quad P=(I-\omega D^{-1}A)T
$$

$$
r_k=b-Ax_k,\quad \eta_k=\|r_k\|_2/\|b\|_2
$$

方程式一覧の対応項目は未登録です。個別の式・近似・診断は上の定義に示します。

**問題の図**

![行列から粗視化するAMG：残差と解誤差を分ける：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/results/sa-amg.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[2次元Poisson・正弦単一モード（FEMを含む）](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=ja) (`poisson-2d-sine`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/sa-amg/?lang=ja#sa-amg-ja-validation)

正規化残差、SciPy spsolveとの相対解差、連続正弦解への離散L²型誤差、観測次数、operator complexityを保存します。節点順を無作為に置き換えた行列も直接解と照合し、幾何学的な粗格子を暗黙に使っていないことを確認します。反復予算0は未収束と報告します。

- [Poisson／正弦波の製造解](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-poisson-manufactured-ja) (`poisson-manufactured`; 関連モデルの参照 · 製造解)

カードは1次元sin(πx)、こちらは2次元sin(πx)sin(πy)です。次元・右辺・FEMの誤差ノルムは異なります。

- [2D Poisson正弦製造解：SEMとP1 FEMの共通参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-sem-poisson-2d-ja) (`sem-poisson-2d`; 同じ問題の参照 · 製造解)

全て無次元。−Δu=2π²sin(πx)sin(πy)、領域[0,1]²、境界u=0。係数は一定、SEMは直交するアフィン正方形、FEMは既存の規則的な三角形分割。
## 前提・単位・境界

無次元の単位正方形、一定正係数の−Δu=f、全周同次Dirichlet境界、5点差分です。階層構築には座標・格子幅・nを渡さず、係数行列と暗黙の定数近似核だけを使います。入力は実対称正定値を前提とし、任意の不定値行列を扱うソルバーではありません。

## 採用した計算法

各行の最大非対角係数に対する相対強度からグラフを作り、貪欲な星型集約と余剰節点の隣接集約への付着で暫定補間Tを作ります。P=(I−ωD⁻¹A)T、ω=4/(3ρ̄)、ρ̄はD⁻¹Aの絶対行和上界です。粗演算子はPᵀAP。前後2回のJacobi平滑化と最終小行列の直接解を用います。これは採用した小規模SA変種であり、原著の全構築法や収束定理の再現ではありません。

$$
A_c=P^TAP,\quad P=(I-\omega D^{-1}A)T
$$

$$
r_k=b-Ax_k,\quad \eta_k=\|r_k\|_2/\|b\|_2
$$

## 比較・検証

正規化残差、SciPy spsolveとの相対解差、連続正弦解への離散L²型誤差、観測次数、operator complexityを保存します。節点順を無作為に置き換えた行列も直接解と照合し、幾何学的な粗格子を暗黙に使っていないことを確認します。反復予算0は未収束と報告します。

## 確認の限界

3格子の固定スカラー問題だけの確認です。係数の大きな不連続、強い異方性、弾性系、任意の非構造格子、最適計算量・格子独立収束を保証しません。小さい残差だけを小さい解誤差の証明としません。

## 保存実測値と判定

```json
{
  "metrics": {
    "max_relative_residual": 7.1395963390776e-11,
    "max_direct_solution_error": 2.0283080847857227e-11,
    "minimum_pde_order": 2.0020872697597354,
    "max_operator_complexity": 3.196752830591754
  },
  "checks": {
    "all_residual_targets": true,
    "independent_sparse_direct": true,
    "second_order_pde_refinement": true,
    "bounded_operator_complexity": true,
    "cycle_budget_failure_reported": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/sa-amg/index.json

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/atlas-foundations-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。

## 出典と確認範囲

- P. Vaněk, J. Mandel and M. Brezina (1996). Algebraic multigrid by smoothed aggregation for second and fourth order elliptic problems. https://link.springer.com/article/10.1007/BF02238511; review_level=publisher-abstract-and-metadata

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Matrix-based AMG: distinguish residual and solution error

Build a smoothed-aggregation hierarchy from an SPD matrix alone and run V-cycles. Problems with 7², 15² and 31² unknowns distinguish independent sparse direct solutions, analytic discrete sine modes and second-order convergence to the continuum solution.

**Methods used**

- [Algebraic multigrid / AMG](https://hrkoyama.github.io/numerical-methods-atlas/methods/amg/?lang=en) (`amg`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/sa-amg/?lang=en#sa-amg-en-algorithm)

A graph based on row-relative off-diagonal strength supplies greedy star aggregates; leftover nodes attach to adjacent aggregates. Smooth tentative T via P=(I−ωD⁻¹A)T with ω=4/(3ρ̄), where ρ̄ bounds the absolute row sums of D⁻¹A. Coarse operators are PᵀAP. V-cycles use two pre/post Jacobi sweeps and a terminal dense direct solve. This is a small adopted SA variant, not every construction or convergence theorem in the original paper.

$$
A_c=P^TAP,\quad P=(I-\omega D^{-1}A)T
$$

$$
r_k=b-Ax_k,\quad \eta_k=\|r_k\|_2/\|b\|_2
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![Matrix-based AMG: distinguish residual and solution error: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/results/sa-amg.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[2D Poisson / single sine mode, including FEM](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=en) (`poisson-2d-sine`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/sa-amg/?lang=en#sa-amg-en-validation)

Store normalized residuals, relative solution differences against SciPy spsolve, discrete-L²-type continuum errors, observed order and operator complexity. A randomly permuted matrix is also checked against a direct solution to expose hidden geometric ordering assumptions. A zero cycle budget reports nonconvergence.

- [Poisson / manufactured sine](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-poisson-manufactured-en) (`poisson-manufactured`; Related-model reference · Manufactured solution)

The card is 1D sin(πx); this test is 2D sin(πx)sin(πy). Dimension, forcing and FEM error norms differ.

- [2D Poisson sine manufactured solution: shared SEM/P1 FEM reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-sem-poisson-2d-en) (`sem-poisson-2d`; Same-problem reference · Manufactured solution)

Dimensionless: -Laplacian u=2pi²sin(pi x)sin(pi y) on[0,1]², u=0 on the boundary. Constant coefficient; affine Cartesian squares for SEM and the existing regular triangle mesh for P1 FEM.
## Assumptions, units and boundaries

Dimensionless unit square, constant-positive-coefficient −Δu=f, homogeneous Dirichlet boundaries and five-point differences. Hierarchy setup receives no coordinates, mesh width or n; it uses the coefficient matrix and an implicit constant near-null candidate. A real SPD input is assumed; arbitrary indefinite problems are outside scope.

## Adopted numerical method

A graph based on row-relative off-diagonal strength supplies greedy star aggregates; leftover nodes attach to adjacent aggregates. Smooth tentative T via P=(I−ωD⁻¹A)T with ω=4/(3ρ̄), where ρ̄ bounds the absolute row sums of D⁻¹A. Coarse operators are PᵀAP. V-cycles use two pre/post Jacobi sweeps and a terminal dense direct solve. This is a small adopted SA variant, not every construction or convergence theorem in the original paper.

$$
A_c=P^TAP,\quad P=(I-\omega D^{-1}A)T
$$

$$
r_k=b-Ax_k,\quad \eta_k=\|r_k\|_2/\|b\|_2
$$

## References and validation

Store normalized residuals, relative solution differences against SciPy spsolve, discrete-L²-type continuum errors, observed order and operator complexity. A randomly permuted matrix is also checked against a direct solution to expose hidden geometric ordering assumptions. A zero cycle budget reports nonconvergence.

## Limits

Only three fixed scalar grids are checked. Large coefficient jumps, strong anisotropy, elasticity, arbitrary unstructured meshes, optimal complexity and mesh-independent convergence are not certified. A small residual alone does not prove a small solution error.

## Stored measurements and decisions

```json
{
  "metrics": {
    "max_relative_residual": 7.1395963390776e-11,
    "max_direct_solution_error": 2.0283080847857227e-11,
    "minimum_pde_order": 2.0020872697597354,
    "max_operator_complexity": 3.196752830591754
  },
  "checks": {
    "all_residual_targets": true,
    "independent_sparse_direct": true,
    "second_order_pde_refinement": true,
    "bounded_operator_complexity": true,
    "cycle_budget_failure_reported": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/sa-amg/index.json

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/atlas-foundations-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group.

## Sources and review scope

- P. Vaněk, J. Mandel and M. Brezina (1996). Algebraic multigrid by smoothed aggregation for second and fourth order elliptic problems. https://link.springer.com/article/10.1007/BF02238511; review_level=publisher-abstract-and-metadata

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
