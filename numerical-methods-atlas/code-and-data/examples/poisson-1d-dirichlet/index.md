# 1D Poisson: Dirichlet sine solution and second-order refinement / 1次元Poisson：Dirichlet正弦解と2次収束

Entry: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/poisson-1d-dirichlet/
Registry: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json
Source record: poisson-1d-dirichlet

Public-file rerun: passed
Receipt: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json

## ja

Thomas法の数値解をsin(πx)と比べ、連続解誤差・独立な離散残差・2次格子収束を分けて確認する。

### scope

既存Thomas解法で −u''=π²sin(πx) を15/31/63内部点で解き、解析解sin(πx)、独立な差分残差、格子幅半減の次数を別々に確認する。

### assumptions

定係数・一様格子の3点差分。入力で領域、境界、右辺、格子、解法を固定。ピボットなしThomasに適した正定値三重対角行列で、任意の三重対角行列を検証するものではない。

### units

無次元のx∈[0,1]とu。次元を戻すなら[f]=[u]/L²。離散相対残差は格子体積重みなしのEuclideanノルム比。

### boundaries

u(0)=u(1)=0。CSVには境界2点も含める。

### Input and run

Input: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/recipes/poisson-1d-dirichlet.json
Input SHA-256: 07ae06758f60f77ac198fdad6d056cc0026b32005e76ad7d0f2cc3727be24f51
ZIP: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip
Run from: atlas-code-2026-11-22

```sh
python -m pip install -r requirements.txt
python run_recipe.py --input recipes/poisson-1d-dirichlet.json --output output-poisson-1d-dirichlet
```

### Outputs

- result.json (json): https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/poisson-1d-dirichlet/result.json
- solution.csv (csv): https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/poisson-1d-dirichlet/solution.csv

CSVは最細格子でx・数値解・解析解・誤差を整列。全3格子の誤差と残差、隣接格子間の次数はresult.jsonに保存。Thomasの原報告は既存台帳でも直接確認未済のため、未検証の一次文献を新たに掲げない。

### Numerical acceptance

- continuous-error / 63内部点の連続解最大誤差。2次差分の主要誤差π²h²/12に余裕を持つ上限。: /metrics/finest_linf_error; value ≤ 0.0003
- second-order-refinement / 格子幅を半減したときの最大誤差の次数が1.9以上。: /metrics/minimum_observed_order; value ≥ 1.9
- discrete-residual / 独立な差分式で再計算した離散相対残差。離散化誤差とは別の確認。: /metrics/maximum_true_relative_residual; value ≤ 1e-10
- dirichlet-boundary / 両端の零Dirichlet条件。: /metrics/boundary_maximum_absolute_value; value ≤ 1e-14
- all-criteria / 全数値条件の判定: /checks; all values = true
- input-provenance / 実行した固定入力のSHA-256: /input_sha256; value = 07ae06758f60f77ac198fdad6d056cc0026b32005e76ad7d0f2cc3727be24f51
- case-passed / 入力に記載した条件の合格: /passed; value = true

### Failure and scope

非零境界、別の右辺、異なる領域や不正格子を拒否。有限差分の滑らかな単一解の検査で、Robin/Neumann、可変係数、ピボットの一般的安全性を保証しない。

Reading: https://hrkoyama.github.io/numerical-methods-atlas/ja/read/elliptic/

### References

- CSVは最細格子でx・数値解・解析解・誤差を整列。全3格子の誤差と残差、隣接格子間の次数はresult.jsonに保存。Thomasの原報告は既存台帳でも直接確認未済のため、未検証の一次文献を新たに掲げない。: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/poisson-1d-dirichlet/result.json
- 独立にsin(πx)と右辺を評価する。小残差と連続解誤差は分けて報告する。: https://hrkoyama.github.io/numerical-methods-atlas/en/read/elliptic/

Code license: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/LICENSE
Content/data terms: https://hrkoyama.github.io/rights/
自作コードはMIT。入力・数値データ・図・本文はサイトの個別条件に従います。この台帳は利用許諾を拡大しません。

## en

Compare the Thomas solution with sin(πx), separating continuous error, a recomputed discrete residual and second-order grid refinement.

### scope

Use the existing Thomas kernel for −u''=π²sin(πx) with 15/31/63 interior nodes; separately check analytic sin(πx), a recomputed discrete residual and halving-grid refinement.

### assumptions

Constant-coefficient three-point differences on a uniform mesh. Inputs fix domain, boundaries, forcing, grids and solver. The SPD tridiagonal system suits unpivoted Thomas; this does not validate arbitrary tridiagonal matrices.

### units

Dimensionless x∈[0,1] and u; dimensionally [f]=[u]/L². The relative discrete residual is an unweighted Euclidean norm ratio.

### boundaries

u(0)=u(1)=0; CSV includes both boundary nodes.

### Input and run

Input: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/recipes/poisson-1d-dirichlet.json
Input SHA-256: 07ae06758f60f77ac198fdad6d056cc0026b32005e76ad7d0f2cc3727be24f51
ZIP: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip
Run from: atlas-code-2026-11-22

```sh
python -m pip install -r requirements.txt
python run_recipe.py --input recipes/poisson-1d-dirichlet.json --output output-poisson-1d-dirichlet
```

### Outputs

- result.json (json): https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/poisson-1d-dirichlet/result.json
- solution.csv (csv): https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/poisson-1d-dirichlet/solution.csv

CSV aligns finest-grid x, numerical/analytic values and error. JSON retains all three errors/residuals and adjacent-level orders. The Thomas original report remains unverified in the existing catalog, so no newly verified primary-source claim is added.

### Numerical acceptance

- continuous-error / Continuous-solution maximum error at 63 interior nodes; the bound allows margin above the leading π²h²/12 error.: /metrics/finest_linf_error; value ≤ 0.0003
- second-order-refinement / Maximum-error refinement order is at least 1.9 when spacing halves.: /metrics/minimum_observed_order; value ≥ 1.9
- discrete-residual / Discrete relative residual recomputed with a separate stencil; distinct from discretization error.: /metrics/maximum_true_relative_residual; value ≤ 1e-10
- dirichlet-boundary / Zero Dirichlet values at both endpoints.: /metrics/boundary_maximum_absolute_value; value ≤ 1e-14
- all-criteria / All numerical acceptance flags: /checks; all values = true
- input-provenance / SHA-256 of the executed fixed input: /input_sha256; value = 07ae06758f60f77ac198fdad6d056cc0026b32005e76ad7d0f2cc3727be24f51
- case-passed / Acceptance conditions in the input passed: /passed; value = true

### Failure and scope

Reject different forcing/domain, nonzero boundaries and invalid meshes. This smooth finite-difference case does not validate Robin/Neumann data, variable coefficients or general pivot safety.

Reading: https://hrkoyama.github.io/numerical-methods-atlas/en/read/elliptic/

### References

- CSV aligns finest-grid x, numerical/analytic values and error. JSON retains all three errors/residuals and adjacent-level orders. The Thomas original report remains unverified in the existing catalog, so no newly verified primary-source claim is added.: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/poisson-1d-dirichlet/result.json
- Evaluate sin(πx) and its forcing independently; report continuous-solution error separately from a small discrete residual.: https://hrkoyama.github.io/numerical-methods-atlas/en/read/elliptic/

Code license: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/LICENSE
Content/data terms: https://hrkoyama.github.io/rights/
Original code is MIT. Inputs, numerical data, figures and prose retain the site’s item-specific terms. This registry does not expand reuse permissions.
