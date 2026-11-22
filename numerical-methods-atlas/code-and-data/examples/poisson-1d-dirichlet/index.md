# 1D Poisson: Dirichlet sine solution and second-order refinement / 1次元Poisson：Dirichlet正弦解と2次収束

Entry: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/poisson-1d-dirichlet/
Registry: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json
Source record: poisson-1d-dirichlet

Public-file rerun: passed
Receipt: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json

## ja

Thomas法の数値解をsin(πx)と比べ、連続解誤差・独立な離散残差・2次格子収束を分けて確認する。

**使用手法**

- [Thomas法／三重対角消去](https://hrkoyama.github.io/numerical-methods-atlas/methods/thomas/?lang=ja) (`thomas`)

**方程式**

[この固定入力の問題式と条件](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#execution-poisson-1d-dirichlet-ja)

一様格子の3点差分を15/31/63内部点で解く。残差が小さいことと連続解に近いことは別々に判定する。

$$
-u''(x)=\pi^2\sin(\pi x),\qquad u(0)=u(1)=0
$$

$$
u_{\rm ref}(x)=\sin(\pi x)
$$

- [Poisson・Laplace方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#poisson-laplace-ja) (`poisson-laplace`)

**問題の図**

![保存済み1次元Dirichlet製造解の誤差と格子数。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/poisson-1d-dirichlet.png)

この問題の代表図です。格子・時刻・初期値などは、この実行例の固定入力と異なる場合があります。

[1次元Poisson・Dirichlet製造解](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-dirichlet/?lang=ja) (`poisson-1d-dirichlet`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-dirichlet/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/poisson-1d-dirichlet/?lang=ja#poisson-1d-dirichlet-ja-validation)

CSVは最細格子でx・数値解・解析解・誤差を整列。全3格子の誤差と残差、隣接格子間の次数はresult.jsonに保存。Thomasの原報告は既存台帳でも直接確認未済のため、未検証の一次文献を新たに掲げない。

- [Poisson／正弦波の製造解](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-poisson-manufactured-ja) (`poisson-manufactured`; 関連モデルの参照 · 製造解)

単一sin(πx)の共通固定入力とは一致しますが、保存比較図は複合正弦製造解も含みます。同じ零Dirichletでも全ソースが同一ではありません。


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

**Methods used**

- [Thomas tridiagonal elimination](https://hrkoyama.github.io/numerical-methods-atlas/methods/thomas/?lang=en) (`thomas`)

**Equations**

[This fixed-input problem and its conditions](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#execution-poisson-1d-dirichlet-en)

Three-point differences on 15/31/63 uniform interior nodes; a small residual and proximity to the continuous solution are separate checks.

$$
-u''(x)=\pi^2\sin(\pi x),\qquad u(0)=u(1)=0
$$

$$
u_{\rm ref}(x)=\sin(\pi x)
$$

- [Poisson / Laplace equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#poisson-laplace-en) (`poisson-laplace`)

**Problem figure**

![Stored error versus resolution for the 1D Dirichlet manufactured solution.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/poisson-1d-dirichlet.png)

A representative figure for the problem. Its grid, time and initial data may differ from this execution’s fixed input.

[1D Poisson / smooth Dirichlet manufactured solutions](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-dirichlet/?lang=en) (`poisson-1d-dirichlet`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-dirichlet/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/poisson-1d-dirichlet/?lang=en#poisson-1d-dirichlet-en-validation)

CSV aligns finest-grid x, numerical/analytic values and error. JSON retains all three errors/residuals and adjacent-level orders. The Thomas original report remains unverified in the existing catalog, so no newly verified primary-source claim is added.

- [Poisson / manufactured sine](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-poisson-manufactured-en) (`poisson-manufactured`; Related-model reference · Manufactured solution)

It matches the single-sine common fixed input, but saved comparisons also contain composite-sine manufactured forcing. Zero Dirichlet boundaries do not make all sources identical.


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
