# Sod衝撃波管 / Sod shock tube

https://hrkoyama.github.io/numerical-methods-atlas/problems/sod/

## 日本語

[保存した最終時刻の数値波形と参照解。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/sod.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/benchmarks/) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#sod)

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

#### Sod衝撃波管：Godunov型更新と自己相似解

共通実行例 · 問題の式

$$
U_t+F(U)_x=0,\quad U=(\rho,\rho v,E)^{\mathsf T},\quad p=(\gamma-1)\left(E-\frac{\rho v^2}{2}\right)
$$

$$
(\rho,v,p)_L=(1,0,1),\quad(\rho,v,p)_R=(0.125,0,0.1),\quad\gamma=1.4
$$

x=0.5の不連続、[0,1]の流出境界、t=0.2。Godunov型有限体積更新の数値流束は近似HLLC。参照は別の自己相似Riemann式で、星領域圧力には数値求根を使う。

### 厳密解・参照解

理想気体γ=1.4の標準Sod初期値に対する半解析的Riemann解が基準です。同じ問題でも点値・保存変数のセル平均・格子と誤差ノルムは同一とは限りません。

#### [Euler／Sod問題](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=euler-sod)

半解析解 · 関連モデルの参照

U(x,t) = R((x−x0)/t)

比熱比gamma>1の理想気体、平面1次元波。真空の保存変数はゼロ、速度は未定義です。

γ=1.4、左右(ρ,u,p)=(1,0,1)/(0.125,0,0.1)、x0=0.5、[0,1]、t=0.2が一致します。点値・保存セル平均・誤差ノルムは別に確認します。 物理的な入力は一致しますが、参照カードの点値標本と保存計算の有限体積セル平均・離散格子は別表現です。

#### Sod衝撃波管：Godunov型更新と自己相似解

細格子160セルの各中心でρ,u,pと同位置・同時刻の参照値を併記。初期値も点サンプルをセル値として与える既存solverを使う。解析的な波構造を使うが、圧力根の数値評価を含み、別コードベースとの独立照合ではない。

- [細格子160セルの各中心でρ,u,pと同位置・同時刻の参照値を併記。初期値も点サンプルをセル値として与える既存solverを使う。解析的な波構造を使うが、圧力根の数値評価を含み、別コードベースとの独立照合ではない。](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/sod/result.json)
- [保存結果](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/sod/result.json)
- [保存結果](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/sod/solution.csv)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/sod/?lang=ja)

### 計算法

この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。

- [Godunov型有限体積法](https://hrkoyama.github.io/numerical-methods-atlas/methods/godunov/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [HLLC](https://hrkoyama.github.io/numerical-methods-atlas/methods/hllc/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [Sod衝撃波管：Godunov型更新と自己相似解](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/sod/?lang=ja)

共通実行例

γ=1.4、左右(ρ,u,p)=(1,0,1)/(0.125,0,0.1)、初期不連続x=0.5、t=0.2の標準問題。80/160セルの区分一定Godunov型＋HLLC＋SSPRK3を自己相似Euler解と比較する。

理想気体、1次元一様格子、正の密度・圧力、CFL=0.3。名付き標準問題の物理定義はJSONに明示し、異なる定義は拒否する。参照の圧力は既存exact_eulerの区間二分法で評価する。Godunov原報の厳密Riemann一段更新そのものではない。

[コード / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip) · [検証記録](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

[固定入力](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/recipes/sod.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python run_recipe.py --input recipes/sod.json --output output-sod
python -m pytest -q tests/test_recipes.py
```

密度誤差0.035と誤差比0.85は既存Sodテストの80/160セル基準を引き継ぐ。CSVの参照はセル中心で評価した自己相似解との標本比較で、厳密セル平均との誤差ではない。全問題での正値性・エントロピー保証、真空、非理想気体や原報の全計算再現は含まない。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/numerical-methods-atlas/2026-11-22/run_recipe.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/run_recipe.py)
- [/code/numerical-methods-atlas/2026-11-22/tests/test_recipes.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/tests/test_recipes.py)

## English

[Stored final-time numerical profile and reference.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/sod.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/benchmarks/) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#sod-en)

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

#### Sod shock tube: Godunov-type update and self-similar reference

Common execution example · Problem definition

$$
U_t+F(U)_x=0,\quad U=(\rho,\rho v,E)^{\mathsf T},\quad p=(\gamma-1)\left(E-\frac{\rho v^2}{2}\right)
$$

$$
(\rho,v,p)_L=(1,0,1),\quad(\rho,v,p)_R=(0.125,0,0.1),\quad\gamma=1.4
$$

Jump at x=0.5, outflow boundaries on [0,1], t=0.2. Godunov-type finite volumes use approximate HLLC fluxes. The separate self-similar Riemann reference uses numerical root finding for star pressure.

### Exact and reference solutions

Use the semi-analytic Riemann solution for standard Sod data with γ=1.4. A matching problem does not imply identical point/cell-average sampling, grid or error norm.

#### [Euler / Sod](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=euler-sod)

Semi-analytic reference · Related-model reference

U(x,t) = R((x−x0)/t)

Ideal gas; gamma>1; planar 1D waves; vacuum has zero conserved state and undefined velocity.

γ=1.4, primitive states (1,0,1)/(0.125,0,0.1), x0=0.5, [0,1] and t=0.2 match. Inspect point/conserved-cell-average sampling and error norms separately. Physical inputs match, but the card’s point samples and the saved computation’s finite-volume cell averages/discrete grid are different representations.

#### Sod shock tube: Godunov-type update and self-similar reference

Each of the 160 fine-grid centers carries ρ,u,p and reference values at the same time/location. The existing solver also initializes its cell values from point samples. Wave structure is analytic but reference pressure requires a numerical root; this is not a cross-check against an independent codebase.

- [Each of the 160 fine-grid centers carries ρ,u,p and reference values at the same time/location. The existing solver also initializes its cell values from point samples. Wave structure is analytic but reference pressure requires a numerical root; this is not a cross-check against an independent codebase.](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/sod/result.json)
- [Saved result](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/sod/result.json)
- [Saved result](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/sod/solution.csv)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/sod/?lang=en)

### Numerical methods

Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions.

- [Godunov-type finite volumes](https://hrkoyama.github.io/numerical-methods-atlas/methods/godunov/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [HLLC](https://hrkoyama.github.io/numerical-methods-atlas/methods/hllc/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Sod shock tube: Godunov-type update and self-similar reference](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/sod/?lang=en)

Common execution example

Standard γ=1.4 Sod tube with left/right (ρ,u,p)=(1,0,1)/(0.125,0,0.1), initial jump x=0.5 and t=0.2. Compare 80/160-cell piecewise-constant Godunov-type/HLLC/SSPRK3 updates with a self-similar Euler solution.

Perfect gas, one-dimensional uniform grid, positive density/pressure and CFL=0.3. The named benchmark's physical definition is explicit in JSON; incompatible definitions are rejected. Reference pressure is evaluated by the existing exact_euler bracketed bisection. This is not the original exact-Riemann one-step Godunov algorithm.

[Code / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip) · [Verification receipt](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

[Fixed input](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/recipes/sod.json)

[File manifest and hashes](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python run_recipe.py --input recipes/sod.json --output output-sod
python -m pytest -q tests/test_recipes.py
```

Density-error 0.035 and error-ratio 0.85 thresholds follow the existing 80/160-cell Sod test. CSV comparisons use the self-similar reference sampled at cell centers, not exact cell-average errors. No all-problem positivity/entropy guarantee, vacuum/nonideal-gas support or reproduction of all original experiments is claimed.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/numerical-methods-atlas/2026-11-22/run_recipe.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/run_recipe.py)
- [/code/numerical-methods-atlas/2026-11-22/tests/test_recipes.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/tests/test_recipes.py)
