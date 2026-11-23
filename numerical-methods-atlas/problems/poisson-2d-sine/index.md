# 2次元Poisson・正弦単一モード（FEMを含む） / 2D Poisson / single sine mode, including FEM

https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/

## 日本語

[同じ正弦製造解を解く、三角形有限要素の保存解と誤差。](https://hrkoyama.github.io/numerical-methods-atlas/assets/field-fem-poisson.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/fem/) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#poisson-2d-sine)

### 方程式・問題の定義

この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。

#### [Poisson・Laplace方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#poisson-laplace-ja)

$$
-\nabla^2u=f
$$

$$
f=0\quad\Longrightarrow\quad\nabla^2u=0
$$

楕円型境界値問題。符号規約を確認し、反復解法・疎行列・境界条件をたどる。

#### 2次元Poisson：CG・多重格子とP1 FEM

共通実行例 · 問題の式

$$
-\nabla^2u=2\pi^2\sin(\pi x)\sin(\pi y),\qquad u|_{\partial[0,1]^2}=0
$$

$$
u_{\rm ref}(x,y)=\sin(\pi x)\sin(\pi y)
$$

CG/MGは15/31/63内部点、P1 FEMは4/8/16分割。FEMの値誤差L2と勾配誤差H1半ノルムは要素内で評価する。単一固有モードのCG反復数は一般的速度比較に用いない。

#### 行列から粗視化するAMG：残差と解誤差を分ける

補助実行例 · 実行例の定義・検証式

$$
A_c=P^TAP,\quad P=(I-\omega D^{-1}A)T
$$

$$
r_k=b-Ax_k,\quad \eta_k=\|r_k\|_2/\|b\|_2
$$

正方形Poisson問題から得たSPD行列だけを階層構築へ渡し、平滑化集約AMGのV-cycleを実行します。7²・15²・31²未知数で独立疎行列直接解、解析的な離散正弦モード、連続解への2次収束を分けて検査します。

#### スペクトル要素法の2D Poisson：P1 FEMとh/p収束を比較

補助実行例 · 実行例の定義・検証式

$$
-\Delta u=f,\quad u|_{\partial\Omega}=0,\quad u_*=\sin(\pi x)\sin(\pi y),\quad f=2\pi^2u_*
$$

$$
K^e=S\otimes W+W\otimes S,\quad S=D^TWD,\quad W=\operatorname{diag}(w_i)
$$

$$
E_{L^2}=\left(\int_\Omega(u_h-u_*)^2\,d\Omega\right)^{1/2},\quad E_{H^1}=\left(\int_\Omega|\nabla u_h-\nabla u_*|^2\,d\Omega\right)^{1/2}
$$

単位正方形の正弦製造解をGLLスペクトル要素法と既存P1三角形FEMで解きます。自由未知数を揃えたh細分化と、固定要素数でのp=1〜6を分けて測ります。

### 厳密解・参照解

単位正方形の製造解sin(πx)sin(πy)を使い、差分・連続P1 FEMの格子誤差と、補助AMG例の離散参照を確認します。 追加のamg-conditioningは既知の代数解を使う条件数・残差診断で、物理問題への紐付けはありません。このPoisson問題の格子精度・独立参照の証拠として流用しません。 解析的な正弦製造解と勾配を参照し、GLL節点とは異なる高次Gauss点で連続L2誤差・H1半ノルムを積分。h/p収束・自由未知数を揃えた誤差・境界値・真の残差を検査し、実際の2D場とP1の頂点・三角形・解をNPZに保存。

#### [Poisson／正弦波の製造解](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=poisson-manufactured)

製造解 · 関連モデルの参照

u = sin(πx); −u_xx = f = π² sin(πx)

両端はゼロDirichlet条件。目標解から外力を選ぶ製造解であり、任意の外力のPoisson解ではありません。

カードは1次元sin(πx)、こちらは2次元sin(πx)sin(πy)です。次元・右辺・FEMの誤差ノルムは異なります。

#### [2D Poisson正弦製造解：SEMとP1 FEMの共通参照](https://hrkoyama.github.io/numerical-methods-atlas/validation/sem-poisson-2d/?lang=ja)

製造解 · 同じ問題の参照

u(x,y)=sin(pi*x)*sin(pi*y); f=2*pi^2*u; grad u=(pi*cos(pi*x)*sin(pi*y),pi*sin(pi*x)*cos(pi*y)).

全て無次元。−Δu=2π²sin(πx)sin(πy)、領域[0,1]²、境界u=0。係数は一定、SEMは直交するアフィン正方形、FEMは既存の規則的な三角形分割。

全て無次元。−Δu=2π²sin(πx)sin(πy)、領域[0,1]²、境界u=0。係数は一定、SEMは直交するアフィン正方形、FEMは既存の規則的な三角形分割。

#### 2次元Poisson：CG・多重格子とP1 FEM

CSVのmethod_codeは0=CG、1=多重格子、2=P1 FEM。各方式の最細格子と境界点で、同一行座標の解析解を付す。resolutionはFDで内部点数、FEMで三角形分割前の軸方向分割数。

- [CSVのmethod_codeは0=CG、1=多重格子、2=P1 FEM。各方式の最細格子と境界点で、同一行座標の解析解を付す。resolutionはFDで内部点数、FEMで三角形分割前の軸方向分割数。](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/poisson-2d-sine/result.json)
- [解析解とその勾配を独立に評価する。FEMのL2/H1は要素内求積であり厳密積分との主張ではない。](https://hrkoyama.github.io/numerical-methods-atlas/en/read/fem/)
- [保存結果](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/poisson-2d-sine/result.json)
- [保存結果](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/poisson-2d-sine/solution.csv)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/poisson-2d-sine/?lang=ja)

#### 行列から粗視化するAMG：残差と解誤差を分ける

正規化残差、SciPy spsolveとの相対解差、連続正弦解への離散L²型誤差、観測次数、operator complexityを保存します。節点順を無作為に置き換えた行列も直接解と照合し、幾何学的な粗格子を暗黙に使っていないことを確認します。反復予算0は未収束と報告します。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/sa-amg/?lang=ja)

#### スペクトル要素法の2D Poisson：P1 FEMとh/p収束を比較

解析的な正弦製造解と勾配を参照し、GLL節点とは異なる高次Gauss点で連続L2誤差・H1半ノルムを積分。h/p収束・自由未知数を揃えた誤差・境界値・真の残差を検査し、実際の2D場とP1の頂点・三角形・解をNPZに保存。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/sem-poisson-2d/?lang=ja)

### 計算法

この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。 SEMはC0連続なテンソル積Qp Lagrange基底・p+1個のLegendre GLL節点と求積、疎な剛性行列・SciPy直接解法を使用。p=2で各方向2/4/8要素、別に2×2要素でp=1〜6。公開済みNumartのP1 FEM・GMRESをファイルのバイト列を保持して4/8/16分割で実行し、両者の自由未知数9/49/225を一致させます。

- [共役勾配法](https://hrkoyama.github.io/numerical-methods-atlas/methods/cg/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [幾何マルチグリッドVサイクル](https://hrkoyama.github.io/numerical-methods-atlas/methods/multigrid/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [連続P1 Galerkin有限要素法](https://hrkoyama.github.io/numerical-methods-atlas/methods/p1-fem/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [代数的マルチグリッド（AMG）](https://hrkoyama.github.io/numerical-methods-atlas/methods/amg/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [スペクトル要素法（SEM）](https://hrkoyama.github.io/numerical-methods-atlas/methods/spectral-element/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [2次元Poisson：CG・多重格子とP1 FEM](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/poisson-2d-sine/?lang=ja)

共通実行例

単位正方形のsin(πx)sin(πy)を参照し、CG/MGは15/31/63内部点、P1 FEMは4/8/16分割で細分化。FDの最大誤差と真の残差、FEMの要素内L2誤差とH1半ノルムを独立に評価する。

定係数 −Δu=2π²sin(πx)sin(πy)。CG/MGは同じ五点SPD系を相対許容値1e-11で解く。FEMは既存の連続P1・対角三角形分割・ILU(0)付きGMRES。FEM誤差は別のDuffy写像と8点積Gauss求積で評価する。

[コード / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip) · [検証記録](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

[固定入力](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/recipes/poisson-2d-sine.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python run_recipe.py --input recipes/poisson-2d-sine.json --output output-poisson-2d-sine
python -m pytest -q tests/test_recipes.py
```

非入れ子FD格子、異なる境界や方程式を拒否。滑らかな正弦解の次数確認に限定し、一般領域・特異解・異方性を保証しない。単一固有モードなのでCGの速い終了を速度比較に用いない。FD/FEMの異なる誤差ノルムを直接同列に扱わない。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/numerical-methods-atlas/2026-11-22/run_recipe.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/run_recipe.py)
- [/code/numerical-methods-atlas/2026-11-22/tests/test_recipes.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/tests/test_recipes.py)

#### [行列から粗視化するAMG：残差と解誤差を分ける](https://hrkoyama.github.io/numerical-methods-atlas/validation/sa-amg/?lang=ja)

補助実行例

正方形Poisson問題から得たSPD行列だけを階層構築へ渡し、平滑化集約AMGのV-cycleを実行します。7²・15²・31²未知数で独立疎行列直接解、解析的な離散正弦モード、連続解への2次収束を分けて検査します。

無次元の単位正方形、一定正係数の−Δu=f、全周同次Dirichlet境界、5点差分です。階層構築には座標・格子幅・nを渡さず、係数行列と暗黙の定数近似核だけを使います。入力は実対称正定値を前提とし、任意の不定値行列を扱うソルバーではありません。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/atlas-foundations-2026-11-22.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

3格子の固定スカラー問題だけの確認です。係数の大きな不連続、強い異方性、弾性系、任意の非構造格子、最適計算量・格子独立収束を保証しません。小さい残差だけを小さい解誤差の証明としません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-22/foundations/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/run.py)
- [/code/validated-examples/2026-11-22/foundations/test_foundations.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/test_foundations.py)

#### [スペクトル要素法の2D Poisson：P1 FEMとh/p収束を比較](https://hrkoyama.github.io/numerical-methods-atlas/validation/sem-poisson-2d/?lang=ja)

補助実行例

単位正方形の正弦製造解をGLLスペクトル要素法と既存P1三角形FEMで解きます。自由未知数を揃えたh細分化と、固定要素数でのp=1〜6を分けて測ります。

全て無次元。−Δu=2π²sin(πx)sin(πy)、領域[0,1]²、境界u=0。係数は一定、SEMは直交するアフィン正方形、FEMは既存の規則的な三角形分割。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/atlas-sem-fr-2026-11-23.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

滑らかな固定問題だけの結果。要素・求積・代数ソルバーが異なるので、速度・計算量・汎用的優位性の比較ではありません。GLLの対角求積質量は一般の積の厳密な質量行列ではない。曲線格子・特異解・非圧縮流体・Nek5000/nekRS本体は未実行。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-23/sem-fr/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/run.py)
- [/code/validated-examples/2026-11-23/sem-fr/sem.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/sem.py)
- [/code/validated-examples/2026-11-23/sem-fr/polynomials.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/polynomials.py)
- [/code/validated-examples/2026-11-23/sem-fr/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/experiments.py)
- [/code/validated-examples/2026-11-23/sem-fr/legacy/fem.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/legacy/fem.py)
- [/code/validated-examples/2026-11-23/sem-fr/legacy/krylov.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/legacy/krylov.py)
- [/code/validated-examples/2026-11-23/sem-fr/test_sem_fr.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/test_sem_fr.py)

## English

[Stored triangular-FEM solution and error for the same sine manufactured problem.](https://hrkoyama.github.io/numerical-methods-atlas/assets/field-fem-poisson.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/fem/) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#poisson-2d-sine-en)

### Equations and problem definitions

Representative equations related to this problem. See the image/problem conditions and each execution example for initial conditions, boundary conditions and parameters.

#### [Poisson / Laplace equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#poisson-laplace-en)

$$
-\nabla^2u=f
$$

$$
f=0\quad\Longrightarrow\quad\nabla^2u=0
$$

Elliptic boundary-value problems: check sign conventions, iterative solvers, sparse matrices and boundaries.

#### 2D Poisson: CG, multigrid and P1 FEM

Common execution example · Problem definition

$$
-\nabla^2u=2\pi^2\sin(\pi x)\sin(\pi y),\qquad u|_{\partial[0,1]^2}=0
$$

$$
u_{\rm ref}(x,y)=\sin(\pi x)\sin(\pi y)
$$

CG/MG use 15/31/63 interior nodes; P1 FEM uses 4/8/16 subdivisions. FEM value L2 and gradient H1-seminorm errors are evaluated inside elements. Single-mode CG iteration counts are not a general speed benchmark.

#### Matrix-based AMG: distinguish residual and solution error

Supplementary execution example · Example definition or validation formula

$$
A_c=P^TAP,\quad P=(I-\omega D^{-1}A)T
$$

$$
r_k=b-Ax_k,\quad \eta_k=\|r_k\|_2/\|b\|_2
$$

Build a smoothed-aggregation hierarchy from an SPD matrix alone and run V-cycles. Problems with 7², 15² and 31² unknowns distinguish independent sparse direct solutions, analytic discrete sine modes and second-order convergence to the continuum solution.

#### 2D spectral-element Poisson: P1 FEM comparison and h/p refinement

Supplementary execution example · Example definition or validation formula

$$
-\Delta u=f,\quad u|_{\partial\Omega}=0,\quad u_*=\sin(\pi x)\sin(\pi y),\quad f=2\pi^2u_*
$$

$$
K^e=S\otimes W+W\otimes S,\quad S=D^TWD,\quad W=\operatorname{diag}(w_i)
$$

$$
E_{L^2}=\left(\int_\Omega(u_h-u_*)^2\,d\Omega\right)^{1/2},\quad E_{H^1}=\left(\int_\Omega|\nabla u_h-\nabla u_*|^2\,d\Omega\right)^{1/2}
$$

Solve a sine manufactured solution on the unit square with GLL spectral elements and the existing triangle P1 FEM. Compare matched free-unknown counts under h refinement and p=1..6 at fixed elements.

### Exact and reference solutions

Use sin(πx)sin(πy) on the unit square to check finite-difference and continuous-P1 FEM mesh errors, plus the supplemental AMG example's discrete reference. The added amg-conditioning case uses known algebraic solutions for conditioning/residual diagnostics and has no physical-problem binding. Its results are not borrowed as evidence for this Poisson problem’s mesh accuracy or independent reference. Compare with the analytic manufactured sine solution/gradient. Integrate continuous L2/H1-seminorm errors at independent higher-order Gauss points. Check h/p refinement, matched-unknown errors, boundary data and true residuals; save actual2D SEM fields and P1 vertices/triangles/values in NPZ.

#### [Poisson / manufactured sine](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=poisson-manufactured)

Manufactured solution · Related-model reference

u = sin(πx); −u_xx = f = π² sin(πx)

Zero Dirichlet endpoints. The forcing is chosen from the target solution; this is not an arbitrary-source Poisson solution.

The card is 1D sin(πx); this test is 2D sin(πx)sin(πy). Dimension, forcing and FEM error norms differ.

#### [2D Poisson sine manufactured solution: shared SEM/P1 FEM reference](https://hrkoyama.github.io/numerical-methods-atlas/validation/sem-poisson-2d/?lang=en)

Manufactured solution · Reference for the same problem

u(x,y)=sin(pi*x)*sin(pi*y); f=2*pi^2*u; grad u=(pi*cos(pi*x)*sin(pi*y),pi*sin(pi*x)*cos(pi*y)).

Dimensionless: -Laplacian u=2pi²sin(pi x)sin(pi y) on[0,1]², u=0 on the boundary. Constant coefficient; affine Cartesian squares for SEM and the existing regular triangle mesh for P1 FEM.

Dimensionless: -Laplacian u=2pi²sin(pi x)sin(pi y) on[0,1]², u=0 on the boundary. Constant coefficient; affine Cartesian squares for SEM and the existing regular triangle mesh for P1 FEM.

#### 2D Poisson: CG, multigrid and P1 FEM

CSV method_code: 0=CG, 1=multigrid, 2=P1 FEM. Each finest mesh includes boundaries and a coordinate-aligned analytic value. resolution means FD interior nodes per axis or FEM subdivisions before diagonal splitting.

- [CSV method_code: 0=CG, 1=multigrid, 2=P1 FEM. Each finest mesh includes boundaries and a coordinate-aligned analytic value. resolution means FD interior nodes per axis or FEM subdivisions before diagonal splitting.](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/poisson-2d-sine/result.json)
- [Independently evaluate the analytic solution/gradient; FEM L2/H1 values use element quadrature, not an exact-integration claim.](https://hrkoyama.github.io/numerical-methods-atlas/en/read/fem/)
- [Saved result](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/poisson-2d-sine/result.json)
- [Saved result](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/poisson-2d-sine/solution.csv)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/poisson-2d-sine/?lang=en)

#### Matrix-based AMG: distinguish residual and solution error

Store normalized residuals, relative solution differences against SciPy spsolve, discrete-L²-type continuum errors, observed order and operator complexity. A randomly permuted matrix is also checked against a direct solution to expose hidden geometric ordering assumptions. A zero cycle budget reports nonconvergence.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/sa-amg/?lang=en)

#### 2D spectral-element Poisson: P1 FEM comparison and h/p refinement

Compare with the analytic manufactured sine solution/gradient. Integrate continuous L2/H1-seminorm errors at independent higher-order Gauss points. Check h/p refinement, matched-unknown errors, boundary data and true residuals; save actual2D SEM fields and P1 vertices/triangles/values in NPZ.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/sem-poisson-2d/?lang=en)

### Numerical methods

Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed. C0 tensor Qp Lagrange SEM with p+1 Legendre GLL nodes/quadrature, sparse stiffness assembly and a SciPy direct solve. At p=2 use2/4/8 elements per axis; separately fix2x2 elements and p=1..6. Execute the byte-identical published Numart triangle P1 FEM/GMRES at4/8/16 subdivisions, matching9/49/225 free unknowns.

- [Conjugate gradients](https://hrkoyama.github.io/numerical-methods-atlas/methods/cg/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Geometric multigrid V-cycle](https://hrkoyama.github.io/numerical-methods-atlas/methods/multigrid/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Continuous P1 Galerkin FEM](https://hrkoyama.github.io/numerical-methods-atlas/methods/p1-fem/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Algebraic multigrid / AMG](https://hrkoyama.github.io/numerical-methods-atlas/methods/amg/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Spectral element method (SEM)](https://hrkoyama.github.io/numerical-methods-atlas/methods/spectral-element/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [2D Poisson: CG, multigrid and P1 FEM](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/poisson-2d-sine/?lang=en)

Common execution example

Reference sin(πx)sin(πy) on the unit square; refine CG/MG through 15/31/63 interior nodes and P1 FEM through 4/8/16 subdivisions. Independently evaluate FD maximum errors/true residuals and FEM element-interior L2/H1-seminorm errors.

Constant-coefficient −Δu=2π²sin(πx)sin(πy). CG/MG solve the same five-point SPD system to relative tolerance 1e-11. FEM uses existing continuous P1, diagonally split triangles and ILU(0)-GMRES. FEM errors use a separate Duffy map and eight-point product Gauss quadrature.

[Code / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip) · [Verification receipt](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

[Fixed input](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/recipes/poisson-2d-sine.json)

[File manifest and hashes](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python run_recipe.py --input recipes/poisson-2d-sine.json --output output-poisson-2d-sine
python -m pytest -q tests/test_recipes.py
```

Reject non-nested FD grids or changed equations/boundaries. Limited to smooth-sine refinement, not general geometry, singular solutions or anisotropy. Rapid one-eigenmode CG termination is not a speed benchmark. Do not equate the distinct FD/FEM error norms.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/numerical-methods-atlas/2026-11-22/run_recipe.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/run_recipe.py)
- [/code/numerical-methods-atlas/2026-11-22/tests/test_recipes.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/tests/test_recipes.py)

#### [Matrix-based AMG: distinguish residual and solution error](https://hrkoyama.github.io/numerical-methods-atlas/validation/sa-amg/?lang=en)

Supplementary execution example

Build a smoothed-aggregation hierarchy from an SPD matrix alone and run V-cycles. Problems with 7², 15² and 31² unknowns distinguish independent sparse direct solutions, analytic discrete sine modes and second-order convergence to the continuum solution.

Dimensionless unit square, constant-positive-coefficient −Δu=f, homogeneous Dirichlet boundaries and five-point differences. Hierarchy setup receives no coordinates, mesh width or n; it uses the coefficient matrix and an implicit constant near-null candidate. A real SPD input is assumed; arbitrary indefinite problems are outside scope.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/atlas-foundations-2026-11-22.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

Only three fixed scalar grids are checked. Large coefficient jumps, strong anisotropy, elasticity, arbitrary unstructured meshes, optimal complexity and mesh-independent convergence are not certified. A small residual alone does not prove a small solution error.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-22/foundations/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/run.py)
- [/code/validated-examples/2026-11-22/foundations/test_foundations.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/test_foundations.py)

#### [2D spectral-element Poisson: P1 FEM comparison and h/p refinement](https://hrkoyama.github.io/numerical-methods-atlas/validation/sem-poisson-2d/?lang=en)

Supplementary execution example

Solve a sine manufactured solution on the unit square with GLL spectral elements and the existing triangle P1 FEM. Compare matched free-unknown counts under h refinement and p=1..6 at fixed elements.

Dimensionless: -Laplacian u=2pi²sin(pi x)sin(pi y) on[0,1]², u=0 on the boundary. Constant coefficient; affine Cartesian squares for SEM and the existing regular triangle mesh for P1 FEM.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/atlas-sem-fr-2026-11-23.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

One smooth fixed problem only. Meshes, quadrature and algebraic solvers differ: no speed, complexity or universal-accuracy ranking. The diagonal GLL quadrature mass is not the exactly integrated mass of every product. No curved mesh, singular solution, incompressible flow or Nek5000/nekRS run.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-23/sem-fr/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/run.py)
- [/code/validated-examples/2026-11-23/sem-fr/sem.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/sem.py)
- [/code/validated-examples/2026-11-23/sem-fr/polynomials.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/polynomials.py)
- [/code/validated-examples/2026-11-23/sem-fr/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/experiments.py)
- [/code/validated-examples/2026-11-23/sem-fr/legacy/fem.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/legacy/fem.py)
- [/code/validated-examples/2026-11-23/sem-fr/legacy/krylov.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/legacy/krylov.py)
- [/code/validated-examples/2026-11-23/sem-fr/test_sem_fr.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/test_sem_fr.py)
