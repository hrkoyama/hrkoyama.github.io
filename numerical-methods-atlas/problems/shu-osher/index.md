# Shu–Osher衝撃波・エントロピー波干渉 / Shu–Osher shock/entropy interaction

https://hrkoyama.github.io/numerical-methods-atlas/problems/shu-osher/

## 日本語

[保存したEuler密度波形（1つの手法を代表表示）。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/shu-osher.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/reconstruction/) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#shu-osher)

### 方程式・問題の定義

この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。

#### [圧縮性Euler方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#euler-ja)

$$
\partial_tU+\partial_xF(U)=0
$$

$$
U=(\rho,\rho u,E)^{\mathsf T}
$$

$$
F=(\rho u,\rho u^2+p,u(E+p))^{\mathsf T}
$$

1次元の保存形。状態方程式と初期・境界条件は各テストの定義を参照する。

#### Shu–Osher：特性WENO-Zと高解像度参照

共通実行例 · 問題の式

$$
U_t+F(U)_x=0,\qquad \gamma=1.4,\qquad -5\leq x\leq5
$$

$$
\rho_R(x,0)=1+0.2\sin(5x),\quad v_R=0,\quad p_R=1,\qquad t_{\rm final}=1.8
$$

初期不連続x=−4、左状態は固定入力を参照。特性有限差分WENO5-Zの点値を比較する。800点参照は同一方式の数値解であり、厳密解・独立ソルバーではない。

#### Shu–Osher：独立参照と格子収束

補助実行例 · 実行例の定義・検証式

$$
\rho(x,0)=1+0.2\sin(5x)\quad(x\geq-4)
$$

衝撃波と密度正弦波の相互作用を、同じPython実装の細格子ではなく、別に実行したAthena++の参照と照合します。

### 厳密解・参照解

保存された高解像度WENO-Z数値参照と、別配布の独立Athena++参照を区別します。どちらもこの衝撃波・密度波相互作用の厳密解という主張ではありません。

#### Shu–Osher：特性WENO-Zと高解像度参照

高解像度の保存変数の点値を各100/200点の格子中心へ線形補間する。誤差はそれぞれ同じ場所・t=1.8で平均する。CSVは200点の計算・参照を並べる。近似収支の許容値0.2%は固定境界の離散化誤差を許すためであり、密度誤差0.15の判定とは別。

- [高解像度の保存変数の点値を各100/200点の格子中心へ線形補間する。誤差はそれぞれ同じ場所・t=1.8で平均する。CSVは200点の計算・参照を並べる。近似収支の許容値0.2%は固定境界の離散化誤差を許すためであり、密度誤差0.15の判定とは別。](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/shu-osher/result.json)
- [保存結果](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/shu-osher/result.json)
- [保存結果](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/shu-osher/solution.csv)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/shu-osher/?lang=ja)

#### Shu–Osher：独立参照と格子収束

100/200/400セルの密度L1誤差と改善率、正値性を測り、参照2048/4096/8192セルの差も事前幅と比較します。境界へ衝撃波が届かない固定時刻で比較します。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/shu-independent/?lang=ja)

### 計算法

この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。

- [有限差分WENO5-Z](https://hrkoyama.github.io/numerical-methods-atlas/methods/weno-z/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [MUSCL再構成](https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [Shu–Osher：特性WENO-Zと高解像度参照](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/shu-osher/?lang=ja)

共通実行例

[-5,5]で衝撃波と密度正弦波の干渉をt=1.8まで計算。100/200点の特性FD WENO-Zを800点の同じ実装と比較し、参照との差と近似境界収支を別々に記録する。

γ=1.4、初期不連続x=−4、左(ρ,u,p)=(3.857143,2.629369,10.33333)、右ρ=1+0.2sin(5x),u=0,p=1。初期不連続を各格子の界面へ合わせる。点値FD、大域LF分割、界面固定Roe特性基底、WENO-Z指数2、ε=10^-6、SSPRK3、CFL=0.3。

[コード / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip) · [検証記録](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

[固定入力](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/recipes/shu-osher.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python run_recipe.py --input recipes/shu-osher.json --output output-shu-osher
python -m pytest -q tests/test_recipes.py
```

800点は同一手法の数値参照で、厳密解や独立solverではない。0.15の平均密度差は構造の再現を見る教材用の解像度基準であり、高精度認証ではない。格子倍増で差が減ることだけを判定し、形式次数は付与しない。正の出力と棄却回数を記録しても、全入力の正値性定理にはならない。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/numerical-methods-atlas/2026-11-22/run_recipe.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/run_recipe.py)
- [/code/numerical-methods-atlas/2026-11-22/tests/test_recipes.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/tests/test_recipes.py)

#### [Shu–Osher：独立参照と格子収束](https://hrkoyama.github.io/numerical-methods-atlas/validation/shu-independent/?lang=ja)

補助実行例

衝撃波と密度正弦波の相互作用を、同じPython実装の細格子ではなく、別に実行したAthena++の参照と照合します。

γ=1.4、[-5,5]、t=1.8。x<-4は(rho,u,p)=(3.857143,2.629369,10.33333)、右はrho=1+0.2sin5x,u=0,p=1。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/atlas-mhd-2026-11-22.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

参照は厳密解ではなく独立した有限格子数値解です。異なる流束系列すべての優劣、WENOの一般的高次数、負圧防止の保証には広げません。 参照2048→4096のL1差0.005346は事前幅0.005を満たさず、8192へ細分しました。途中の未達記録も残します。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-22/mhd/legacy/solvers.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/legacy/solvers.py)
- [/code/validated-examples/2026-11-22/mhd/legacy/riemann.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/legacy/riemann.py)
- [/code/validated-examples/2026-11-22/mhd/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/run.py)
- [/code/validated-examples/2026-11-22/mhd/test_validation.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/test_validation.py)

## English

[Stored Euler density profile, showing one representative method.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/shu-osher.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/reconstruction/) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#shu-osher-en)

### Equations and problem definitions

Representative equations related to this problem. See the image/problem conditions and each execution example for initial conditions, boundary conditions and parameters.

#### [Compressible Euler equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#euler-en)

$$
\partial_tU+\partial_xF(U)=0
$$

$$
U=(\rho,\rho u,E)^{\mathsf T}
$$

$$
F=(\rho u,\rho u^2+p,u(E+p))^{\mathsf T}
$$

The one-dimensional conservative form. Consult each test for its equation of state, initial data and boundaries.

#### Shu–Osher: characteristic WENO-Z and a numerical reference

Common execution example · Problem definition

$$
U_t+F(U)_x=0,\qquad \gamma=1.4,\qquad -5\leq x\leq5
$$

$$
\rho_R(x,0)=1+0.2\sin(5x),\quad v_R=0,\quad p_R=1,\qquad t_{\rm final}=1.8
$$

Initial jump at x=−4; see the fixed input for the left state. Compares characteristic finite-difference WENO5-Z point values. The 800-point reference is neither exact nor an independent solver.

#### Shu–Osher: independent reference and mesh refinement

Supplementary execution example · Example definition or validation formula

$$
\rho(x,0)=1+0.2\sin(5x)\quad(x\geq-4)
$$

Compare shock–density-wave interaction against separately executed Athena++ reference data rather than a finer grid of the same Python code.

### Exact and reference solutions

Distinguish the stored high-resolution WENO-Z numerical reference from the separately distributed independent Athena++ reference. Neither is claimed as an exact solution of this shock–density-wave interaction.

#### Shu–Osher: characteristic WENO-Z and a numerical reference

Higher-resolution conserved point values are linearly interpolated to each 100/200-point grid's centers. Errors are averaged at matching locations and t=1.8; CSV pairs the 200-point solution and reference. The 0.2% approximate-balance allowance accommodates fixed-boundary discretization and is separate from the density-error bound of 0.15.

- [Higher-resolution conserved point values are linearly interpolated to each 100/200-point grid's centers. Errors are averaged at matching locations and t=1.8; CSV pairs the 200-point solution and reference. The 0.2% approximate-balance allowance accommodates fixed-boundary discretization and is separate from the density-error bound of 0.15.](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/shu-osher/result.json)
- [Saved result](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/shu-osher/result.json)
- [Saved result](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/shu-osher/solution.csv)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/shu-osher/?lang=en)

#### Shu–Osher: independent reference and mesh refinement

Measure density L1 error, refinement and positivity on 100/200/400 cells; also compare 2048/4096/8192 reference differences with a predeclared bound. The shock has not reached the boundaries at the fixed comparison time.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/shu-independent/?lang=en)

### Numerical methods

Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.

- [FD WENO5-Z](https://hrkoyama.github.io/numerical-methods-atlas/methods/weno-z/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [MUSCL reconstruction](https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Shu–Osher: characteristic WENO-Z and a numerical reference](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/shu-osher/?lang=en)

Common execution example

Evolve shock/entropy-wave interaction on [-5,5] to t=1.8. Compare characteristic FD WENO-Z at 100/200 points with the same implementation at 800 points, separately recording reference disagreement and approximate boundary balance.

γ=1.4, initial jump x=−4, left (ρ,u,p)=(3.857143,2.629369,10.33333), and right ρ=1+0.2sin(5x), u=0, p=1. The initial jump aligns with a face on every grid. Pointwise FD, global LF splitting, face-frozen Roe characteristics, WENO-Z exponent 2, ε=10^-6, SSPRK3 and CFL=0.3 are used.

[Code / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip) · [Verification receipt](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

[Fixed input](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/recipes/shu-osher.json)

[File manifest and hashes](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python run_recipe.py --input recipes/shu-osher.json --output output-shu-osher
python -m pytest -q tests/test_recipes.py
```

The 800-point solution is a same-method numerical reference, not an exact solution or independent solver. The mean-density difference bound of 0.15 is an educational structure-resolution criterion, not a high-accuracy certification. Only decreasing discrepancy under grid doubling is tested; no formal order is assigned. Positive outputs and counted rejections do not establish positivity for every input.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/numerical-methods-atlas/2026-11-22/run_recipe.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/run_recipe.py)
- [/code/numerical-methods-atlas/2026-11-22/tests/test_recipes.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/tests/test_recipes.py)

#### [Shu–Osher: independent reference and mesh refinement](https://hrkoyama.github.io/numerical-methods-atlas/validation/shu-independent/?lang=en)

Supplementary execution example

Compare shock–density-wave interaction against separately executed Athena++ reference data rather than a finer grid of the same Python code.

gamma=1.4, [-5,5], t=1.8. For x<-4, (rho,u,p)=(3.857143,2.629369,10.33333); to the right rho=1+0.2sin5x,u=0,p=1.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/atlas-mhd-2026-11-22.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

The reference is an independent finite-grid numerical solution, not an exact solution. No universal flux ranking, WENO-order claim or positivity guarantee is inferred. The 2048-to-4096 reference L1 increment0.005346 missed the predeclared0.005 bound, so8192 cells were added. The earlier miss remains recorded.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-22/mhd/legacy/solvers.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/legacy/solvers.py)
- [/code/validated-examples/2026-11-22/mhd/legacy/riemann.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/legacy/riemann.py)
- [/code/validated-examples/2026-11-22/mhd/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/run.py)
- [/code/validated-examples/2026-11-22/mhd/test_validation.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/test_validation.py)
