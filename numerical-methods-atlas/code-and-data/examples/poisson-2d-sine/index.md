# 2D Poisson: CG, multigrid and P1 FEM / 2次元Poisson：CG・多重格子とP1 FEM

Entry: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/poisson-2d-sine/
Registry: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json
Source record: poisson-2d-sine

Public-file rerun: passed
Receipt: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json

## ja

CG・多重格子の同じ差分解とP1有限要素を調べ、FD最大誤差とFEMのL2・H1半ノルム収束を見比べる。

**使用手法**

- [共役勾配法](https://hrkoyama.github.io/numerical-methods-atlas/methods/cg/?lang=ja) (`cg`)
- [幾何マルチグリッドVサイクル](https://hrkoyama.github.io/numerical-methods-atlas/methods/multigrid/?lang=ja) (`multigrid`)
- [連続P1 Galerkin有限要素法](https://hrkoyama.github.io/numerical-methods-atlas/methods/p1-fem/?lang=ja) (`p1-fem`)

**方程式**

[この固定入力の問題式と条件](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#execution-poisson-2d-sine-ja)

CG/MGは15/31/63内部点、P1 FEMは4/8/16分割。FEMの値誤差L2と勾配誤差H1半ノルムは要素内で評価する。単一固有モードのCG反復数は一般的速度比較に用いない。

$$
-\nabla^2u=2\pi^2\sin(\pi x)\sin(\pi y),\qquad u|_{\partial[0,1]^2}=0
$$

$$
u_{\rm ref}(x,y)=\sin(\pi x)\sin(\pi y)
$$

- [Poisson・Laplace方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#poisson-laplace-ja) (`poisson-laplace`)

**問題の図**

![同じ正弦製造解を解く、三角形有限要素の保存解と誤差。](https://hrkoyama.github.io/numerical-methods-atlas/assets/field-fem-poisson.png)

この問題の代表図です。格子・時刻・初期値などは、この実行例の固定入力と異なる場合があります。

[2次元Poisson・正弦単一モード（FEMを含む）](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=ja) (`poisson-2d-sine`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/poisson-2d-sine/?lang=ja#poisson-2d-sine-ja-validation)

CSVのmethod_codeは0=CG、1=多重格子、2=P1 FEM。各方式の最細格子と境界点で、同一行座標の解析解を付す。resolutionはFDで内部点数、FEMで三角形分割前の軸方向分割数。

- [Poisson／正弦波の製造解](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-poisson-manufactured-ja) (`poisson-manufactured`; 関連モデルの参照 · 製造解)

カードは1次元sin(πx)、こちらは2次元sin(πx)sin(πy)です。次元・右辺・FEMの誤差ノルムは異なります。

- [2D Poisson正弦製造解：SEMとP1 FEMの共通参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-sem-poisson-2d-ja) (`sem-poisson-2d`; 同じ問題の参照 · 製造解)

全て無次元。−Δu=2π²sin(πx)sin(πy)、領域[0,1]²、境界u=0。係数は一定、SEMは直交するアフィン正方形、FEMは既存の規則的な三角形分割。


### scope

単位正方形のsin(πx)sin(πy)を参照し、CG/MGは15/31/63内部点、P1 FEMは4/8/16分割で細分化。FDの最大誤差と真の残差、FEMの要素内L2誤差とH1半ノルムを独立に評価する。

### assumptions

定係数 −Δu=2π²sin(πx)sin(πy)。CG/MGは同じ五点SPD系を相対許容値1e-11で解く。FEMは既存の連続P1・対角三角形分割・ILU(0)付きGMRES。FEM誤差は別のDuffy写像と8点積Gauss求積で評価する。

### units

領域長1・uとも無次元。L2は値の面積積分ノルム、H1半ノルムは勾配誤差の面積積分であり、節点最大誤差や単純な配列ノルムと区別する。

### boundaries

正方形[0,1]²の全周でu=0。FEMの組立て残差は内部自由度だけで評価し、境界反力は除く。

### Input and run

Input: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/recipes/poisson-2d-sine.json
Input SHA-256: e4928dda7da5eb43bbb33c8739be6d8cc28e0bd6bed9ba6635899daad4c1c244
ZIP: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip
Run from: atlas-code-2026-11-22

```sh
python -m pip install -r requirements.txt
python run_recipe.py --input recipes/poisson-2d-sine.json --output output-poisson-2d-sine
```

### Outputs

- result.json (json): https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/poisson-2d-sine/result.json
- solution.csv (csv): https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/poisson-2d-sine/solution.csv

CSVのmethod_codeは0=CG、1=多重格子、2=P1 FEM。各方式の最細格子と境界点で、同一行座標の解析解を付す。resolutionはFDで内部点数、FEMで三角形分割前の軸方向分割数。

### Numerical acceptance

- cg-continuous-error / CGの連続解最大誤差。63内部点で正弦モードの2次差分誤差に余裕を持たせる。: /metrics/fd_finest_cg_linf_error; value ≤ 0.0003
- mg-continuous-error / 多重格子の連続解最大誤差。CGと同じ離散問題を使う。: /metrics/fd_finest_multigrid_linf_error; value ≤ 0.0003
- fd-second-order / CGと多重格子の最大誤差がともに2次収束する。: /metrics/fd_minimum_observed_order; value ≥ 1.9
- fd-discrete-residual / 独立な五点差分で再計算した相対残差。内部停止1e-11より緩い再評価上限。: /metrics/fd_maximum_true_relative_residual; value ≤ 1e-09
- matched-fd-solutions / 同じ五点差分解を求めるCGと多重格子の一致。連続解参照とは区別する。: /metrics/fd_maximum_cg_multigrid_difference; value ≤ 1e-09
- fem-l2-error / 16分割P1要素の要素内L2誤差。節点最大誤差ではない。: /metrics/fem_finest_l2_error; value ≤ 0.01
- fem-h1-seminorm-error / 16分割P1要素の勾配誤差のH1半ノルム。L2誤差と分ける。: /metrics/fem_finest_h1_seminorm_error; value ≤ 0.3
- fem-second-order-l2 / 滑らかな解に対するP1のL2誤差の期待次数2を確認する。: /metrics/fem_minimum_l2_order; value ≥ 1.8
- fem-first-order-h1 / 滑らかな解に対するP1のH1半ノルム誤差の期待次数1を確認する。: /metrics/fem_minimum_h1_seminorm_order; value ≥ 0.9
- fem-assembled-residual / 組立て剛性行列の内部自由度残差。境界行の反力を残差に混ぜない。: /metrics/fem_maximum_interior_true_relative_residual; value ≤ 1e-09
- fem-dirichlet-boundary / P1要素の全周零Dirichlet条件。: /metrics/fem_boundary_maximum_absolute_value; value ≤ 1e-12
- all-criteria / 全数値条件の判定: /checks; all values = true
- input-provenance / 実行した固定入力のSHA-256: /input_sha256; value = e4928dda7da5eb43bbb33c8739be6d8cc28e0bd6bed9ba6635899daad4c1c244
- case-passed / 入力に記載した条件の合格: /passed; value = true

### Failure and scope

非入れ子FD格子、異なる境界や方程式を拒否。滑らかな正弦解の次数確認に限定し、一般領域・特異解・異方性を保証しない。単一固有モードなのでCGの速い終了を速度比較に用いない。FD/FEMの異なる誤差ノルムを直接同列に扱わない。

Reading: https://hrkoyama.github.io/numerical-methods-atlas/ja/read/fem/

### References

- CSVのmethod_codeは0=CG、1=多重格子、2=P1 FEM。各方式の最細格子と境界点で、同一行座標の解析解を付す。resolutionはFDで内部点数、FEMで三角形分割前の軸方向分割数。: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/poisson-2d-sine/result.json
- 解析解とその勾配を独立に評価する。FEMのL2/H1は要素内求積であり厳密積分との主張ではない。: https://hrkoyama.github.io/numerical-methods-atlas/en/read/fem/
- 既存CG項目の一次文献。単一モードの反復数を一般性能とは解釈しない。: https://doi.org/10.6028/jres.049.044
- 既存多重格子項目の文献。本例は固定階層V-cycleに限定。: https://doi.org/10.1090/S0025-5718-1977-0431719-X
- 既存P1要素項目の区分線形変分近似の文献。現コードの全アルゴリズムを原論文へ帰属しない。: https://doi.org/10.1090/S0002-9904-1943-07818-4

Code license: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/LICENSE
Content/data terms: https://hrkoyama.github.io/rights/
自作コードはMIT。入力・数値データ・図・本文はサイトの個別条件に従います。この台帳は利用許諾を拡大しません。

## en

Inspect CG/multigrid on the same discrete system and P1 FEM, comparing FD maximum error with separate FEM L2/H1-seminorm refinement.

**Methods used**

- [Conjugate gradients](https://hrkoyama.github.io/numerical-methods-atlas/methods/cg/?lang=en) (`cg`)
- [Geometric multigrid V-cycle](https://hrkoyama.github.io/numerical-methods-atlas/methods/multigrid/?lang=en) (`multigrid`)
- [Continuous P1 Galerkin FEM](https://hrkoyama.github.io/numerical-methods-atlas/methods/p1-fem/?lang=en) (`p1-fem`)

**Equations**

[This fixed-input problem and its conditions](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#execution-poisson-2d-sine-en)

CG/MG use 15/31/63 interior nodes; P1 FEM uses 4/8/16 subdivisions. FEM value L2 and gradient H1-seminorm errors are evaluated inside elements. Single-mode CG iteration counts are not a general speed benchmark.

$$
-\nabla^2u=2\pi^2\sin(\pi x)\sin(\pi y),\qquad u|_{\partial[0,1]^2}=0
$$

$$
u_{\rm ref}(x,y)=\sin(\pi x)\sin(\pi y)
$$

- [Poisson / Laplace equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#poisson-laplace-en) (`poisson-laplace`)

**Problem figure**

![Stored triangular-FEM solution and error for the same sine manufactured problem.](https://hrkoyama.github.io/numerical-methods-atlas/assets/field-fem-poisson.png)

A representative figure for the problem. Its grid, time and initial data may differ from this execution’s fixed input.

[2D Poisson / single sine mode, including FEM](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=en) (`poisson-2d-sine`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/poisson-2d-sine/?lang=en#poisson-2d-sine-en-validation)

CSV method_code: 0=CG, 1=multigrid, 2=P1 FEM. Each finest mesh includes boundaries and a coordinate-aligned analytic value. resolution means FD interior nodes per axis or FEM subdivisions before diagonal splitting.

- [Poisson / manufactured sine](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-poisson-manufactured-en) (`poisson-manufactured`; Related-model reference · Manufactured solution)

The card is 1D sin(πx); this test is 2D sin(πx)sin(πy). Dimension, forcing and FEM error norms differ.

- [2D Poisson sine manufactured solution: shared SEM/P1 FEM reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-sem-poisson-2d-en) (`sem-poisson-2d`; Same-problem reference · Manufactured solution)

Dimensionless: -Laplacian u=2pi²sin(pi x)sin(pi y) on[0,1]², u=0 on the boundary. Constant coefficient; affine Cartesian squares for SEM and the existing regular triangle mesh for P1 FEM.


### scope

Reference sin(πx)sin(πy) on the unit square; refine CG/MG through 15/31/63 interior nodes and P1 FEM through 4/8/16 subdivisions. Independently evaluate FD maximum errors/true residuals and FEM element-interior L2/H1-seminorm errors.

### assumptions

Constant-coefficient −Δu=2π²sin(πx)sin(πy). CG/MG solve the same five-point SPD system to relative tolerance 1e-11. FEM uses existing continuous P1, diagonally split triangles and ILU(0)-GMRES. FEM errors use a separate Duffy map and eight-point product Gauss quadrature.

### units

Dimensionless unit-length domain and u. L2 integrates value error over area; H1 seminorm integrates gradient error, separately from nodal maximum or plain array norms.

### boundaries

u=0 around [0,1]². FEM assembled residuals use interior degrees of freedom, excluding boundary reactions.

### Input and run

Input: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/recipes/poisson-2d-sine.json
Input SHA-256: e4928dda7da5eb43bbb33c8739be6d8cc28e0bd6bed9ba6635899daad4c1c244
ZIP: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip
Run from: atlas-code-2026-11-22

```sh
python -m pip install -r requirements.txt
python run_recipe.py --input recipes/poisson-2d-sine.json --output output-poisson-2d-sine
```

### Outputs

- result.json (json): https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/poisson-2d-sine/result.json
- solution.csv (csv): https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/poisson-2d-sine/solution.csv

CSV method_code: 0=CG, 1=multigrid, 2=P1 FEM. Each finest mesh includes boundaries and a coordinate-aligned analytic value. resolution means FD interior nodes per axis or FEM subdivisions before diagonal splitting.

### Numerical acceptance

- cg-continuous-error / CG continuous-solution maximum error, allowing margin for the second-order sine-mode error on 63 interior nodes.: /metrics/fd_finest_cg_linf_error; value ≤ 0.0003
- mg-continuous-error / Multigrid continuous-solution maximum error for the same discrete problem as CG.: /metrics/fd_finest_multigrid_linf_error; value ≤ 0.0003
- fd-second-order / Both CG and multigrid maximum errors show second-order refinement.: /metrics/fd_minimum_observed_order; value ≥ 1.9
- fd-discrete-residual / Relative residual from a separately evaluated five-point stencil; the check leaves margin above the 1e-11 solver target.: /metrics/fd_maximum_true_relative_residual; value ≤ 1e-09
- matched-fd-solutions / CG/multigrid agreement for the same five-point system; this is a numerical cross-check, separate from the analytic solution.: /metrics/fd_maximum_cg_multigrid_difference; value ≤ 1e-09
- fem-l2-error / Element-interior L2 error for the 16-subdivision P1 mesh, not a nodal maximum norm.: /metrics/fem_finest_l2_error; value ≤ 0.01
- fem-h1-seminorm-error / H1 seminorm of the P1 gradient error on the 16-subdivision mesh, separate from L2 value error.: /metrics/fem_finest_h1_seminorm_error; value ≤ 0.3
- fem-second-order-l2 / Checks the expected order-two P1 L2 refinement for the smooth solution.: /metrics/fem_minimum_l2_order; value ≥ 1.8
- fem-first-order-h1 / Checks the expected order-one P1 H1-seminorm refinement for the smooth solution.: /metrics/fem_minimum_h1_seminorm_order; value ≥ 0.9
- fem-assembled-residual / Assembled stiffness residual on interior degrees of freedom; boundary reactions are excluded.: /metrics/fem_maximum_interior_true_relative_residual; value ≤ 1e-09
- fem-dirichlet-boundary / Zero Dirichlet values around the P1 domain boundary.: /metrics/fem_boundary_maximum_absolute_value; value ≤ 1e-12
- all-criteria / All numerical acceptance flags: /checks; all values = true
- input-provenance / SHA-256 of the executed fixed input: /input_sha256; value = e4928dda7da5eb43bbb33c8739be6d8cc28e0bd6bed9ba6635899daad4c1c244
- case-passed / Acceptance conditions in the input passed: /passed; value = true

### Failure and scope

Reject non-nested FD grids or changed equations/boundaries. Limited to smooth-sine refinement, not general geometry, singular solutions or anisotropy. Rapid one-eigenmode CG termination is not a speed benchmark. Do not equate the distinct FD/FEM error norms.

Reading: https://hrkoyama.github.io/numerical-methods-atlas/en/read/fem/

### References

- CSV method_code: 0=CG, 1=multigrid, 2=P1 FEM. Each finest mesh includes boundaries and a coordinate-aligned analytic value. resolution means FD interior nodes per axis or FEM subdivisions before diagonal splitting.: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/poisson-2d-sine/result.json
- Independently evaluate the analytic solution/gradient; FEM L2/H1 values use element quadrature, not an exact-integration claim.: https://hrkoyama.github.io/numerical-methods-atlas/en/read/fem/
- Existing CG primary reference; one-mode iteration counts are not a general performance benchmark.: https://doi.org/10.6028/jres.049.044
- Existing multigrid reference; this recipe is limited to the fixed-hierarchy V-cycle.: https://doi.org/10.1090/S0025-5718-1977-0431719-X
- Existing P1 reference for piecewise-linear variational approximation; not attribution of every modern code component to the original paper.: https://doi.org/10.1090/S0002-9904-1943-07818-4

Code license: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/LICENSE
Content/data terms: https://hrkoyama.github.io/rights/
Original code is MIT. Inputs, numerical data, figures and prose retain the site’s item-specific terms. This registry does not expand reuse permissions.
