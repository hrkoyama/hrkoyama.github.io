# 1次元Bratu非線形境界値問題 / One-dimensional Bratu boundary-value problem

https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu/

## 日本語

[公開コード版を固定条件で実行して作成した計算結果。条件・値・検査結果を添付。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/bratu.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/sparse-nonlinear/) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#bratu)

### 方程式・問題の定義

この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。

#### [Bratu非線形境界値問題](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bratu-ja)

$$
-\frac{d^2u}{dx^2}=\lambda e^u,\qquad 0<x<1
$$

$$
u(0)=u(1)=0
$$

ここでは−u″=λexp(u)の符号規約。Newton–Krylov法で残差・格子収束・内側線形解法の失敗を確認します。

#### 1次元Bratu：小さい枝のNewton–GMRES

共通実行例 · 問題の式

$$
-u''=\lambda e^u,\qquad u(0)=u(1)=0
$$

$$
u_{\rm ref}(x)=2\log\frac{\cosh(\beta/2)}{\cosh[\beta(x-1/2)]},\qquad \lambda=\frac{2\beta^2}{\cosh^2(\beta/2)},\quad\beta=1
$$

31/63/127内部点、零初期値で小さい枝を選ぶ。βtanh(β/2)<2の枝を対象とし、大きい枝や分岐点の追跡を行わない。

### 厳密解・参照解

小さい枝の双曲線関数による連続解と格子収束を確認します。感度・逆問題の追補では微分・目的関数を別に検証し、18件の参照解一覧にBratu専用カードはありません。

#### 1次元Bratu：小さい枝のNewton–GMRES

CSVは最細格子の数値解・解析解・絶対誤差。JSONには各格子の真の非線形残差、Newton反復数と最小減衰長を記録する。

- [CSVは最細格子の数値解・解析解・絶対誤差。JSONには各格子の真の非線形残差、Newton反復数と最小減衰長を記録する。](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/bratu/result.json)
- [λと解析解を同じβから独立に評価し、2β²の係数を落とさない。](https://hrkoyama.github.io/numerical-methods-atlas/en/read/sparse-nonlinear/)
- [保存結果](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/bratu/result.json)
- [保存結果](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/bratu/solution.csv)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/bratu/?lang=ja)

### 計算法

共通実行例では減衰Newton法で前進の境界値問題を解きます。関連する自動微分・感度・随伴・係数推定の検証は各手法の別配布版へ進めます。感度・逆問題（1個または2個の係数）の入力と判定は別であり、共通の前進実行例に合算しません。

- [Armijo減衰Newton法](https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [自動微分](https://hrkoyama.github.io/numerical-methods-atlas/methods/automatic-differentiation/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり
- [陰関数微分・随伴法](https://hrkoyama.github.io/numerical-methods-atlas/methods/adjoint/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり
- [勾配法・準Newton法](https://hrkoyama.github.io/numerical-methods-atlas/methods/optimization/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [1次元Bratu：小さい枝のNewton–GMRES](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/bratu/?lang=ja)

共通実行例

−u''=λexp(u)、β=1・λ=2β²/cosh²(β/2)の小さい枝を零初期値から解く。31/63/127内部点で解析解、独立に再評価した非線形残差、2次格子収束を確認する。

既存の残差十分減少による減衰NewtonとILU(0)付きGMRES。解析解u=2log[cosh(β/2)/cosh(β(x−1/2))]。βtanh(β/2)<2で小さい枝を選び、初期値は全点零。内部Newton制御は非線形許容値1e-10、最大30反復。

[コード / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip) · [検証記録](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

[固定入力](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/recipes/bratu.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python run_recipe.py --input recipes/bratu.json --output output-bratu
python -m pytest -q tests/test_recipes.py
```

小さい枝・零初期値・固定境界の指定を要求する。大きい枝、臨界点近傍の追跡、分岐、任意初期値からの大域収束は保証しない。解の細格子値を解析解とは呼ばない。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/numerical-methods-atlas/2026-11-22/run_recipe.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/run_recipe.py)
- [/code/numerical-methods-atlas/2026-11-22/tests/test_recipes.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/tests/test_recipes.py)

#### [code/numerical-methods-atlas/2026-11-21/tests/test_sparse_fem.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_sparse_fem.py)

関連する既存のソース・検査。固定入力実行例とは別です。

`test_bratu_newton_krylov_refines_to_continuous_reference`

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

作業フォルダ：atlas-code-2026-11-21/

```sh
python -m pytest -q tests/test_sparse_fem.py -k test_bratu_newton_krylov_refines_to_continuous_reference
```

## English

[Calculated from the public code edition with fixed inputs; inputs, values and checks are linked.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/bratu.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/sparse-nonlinear/) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#bratu-en)

### Equations and problem definitions

Representative equations related to this problem. See the image/problem conditions and each execution example for initial conditions, boundary conditions and parameters.

#### [Bratu nonlinear boundary-value problem](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bratu-en)

$$
-\frac{d^2u}{dx^2}=\lambda e^u,\qquad 0<x<1
$$

$$
u(0)=u(1)=0
$$

The convention here is −u″=λ exp(u). Newton–Krylov checks cover residuals, refinement and inner-solver failures.

#### 1D Bratu: Newton–GMRES on the lower branch

Common execution example · Problem definition

$$
-u''=\lambda e^u,\qquad u(0)=u(1)=0
$$

$$
u_{\rm ref}(x)=2\log\frac{\cosh(\beta/2)}{\cosh[\beta(x-1/2)]},\qquad \lambda=\frac{2\beta^2}{\cosh^2(\beta/2)},\quad\beta=1
$$

31/63/127 interior nodes and a zero initial guess select the lower branch with βtanh(β/2)<2; no upper-branch or bifurcation tracking.

### Exact and reference solutions

Check a hyperbolic-function continuum solution on the lower branch and mesh refinement. Follow-on sensitivity/inverse examples validate derivatives and objectives separately; Bratu has no card in the 18-case reference library.

#### 1D Bratu: Newton–GMRES on the lower branch

CSV carries finest-grid numerical/analytic values and absolute error. JSON retains each mesh's nonlinear residual, Newton iteration count and minimum damping length.

- [CSV carries finest-grid numerical/analytic values and absolute error. JSON retains each mesh's nonlinear residual, Newton iteration count and minimum damping length.](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/bratu/result.json)
- [Evaluate λ and the analytic solution independently from β, retaining the factor 2β².](https://hrkoyama.github.io/numerical-methods-atlas/en/read/sparse-nonlinear/)
- [Saved result](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/bratu/result.json)
- [Saved result](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/bratu/solution.csv)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/bratu/?lang=en)

### Numerical methods

The common example solves the forward boundary-value problem with damped Newton. Related method pages lead to separate editions for automatic differentiation, sensitivities, adjoints and coefficient fitting. Sensitivity and inverse problems with one or two coefficients have separate inputs and acceptance checks; they are not added to the common forward execution entry.

- [Armijo-damped Newton](https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Automatic differentiation](https://hrkoyama.github.io/numerical-methods-atlas/methods/automatic-differentiation/?lang=en) — Related explanation; Method-registry status: Educational example / related code
- [Implicit differentiation and adjoint methods](https://hrkoyama.github.io/numerical-methods-atlas/methods/adjoint/?lang=en) — Related explanation; Method-registry status: Educational example / related code
- [Gradient and quasi-Newton optimization](https://hrkoyama.github.io/numerical-methods-atlas/methods/optimization/?lang=en) — Related explanation; Method-registry status: Educational example / related code

### Code and execution

#### [1D Bratu: Newton–GMRES on the lower branch](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/bratu/?lang=en)

Common execution example

Solve the lower branch of −u''=λexp(u), with β=1 and λ=2β²/cosh²(β/2), starting at zero. Check the analytic solution, recomputed nonlinear residual and second-order refinement on 31/63/127 interior nodes.

Existing residual-decrease damped Newton and ILU(0)-GMRES. Analytic u=2log[cosh(β/2)/cosh(β(x−1/2))]. βtanh(β/2)<2 selects the lower branch and all initial unknowns are zero. Nonlinear tolerance is 1e-10 with at most 30 Newton iterations.

[Code / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip) · [Verification receipt](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

[Fixed input](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/recipes/bratu.json)

[File manifest and hashes](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python run_recipe.py --input recipes/bratu.json --output output-bratu
python -m pytest -q tests/test_recipes.py
```

Require the lower-branch declaration, zero initial guess and fixed boundaries. No upper-branch continuation, critical-point tracking, bifurcation or global-convergence guarantee. Fine-grid solutions are not called analytic references.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/numerical-methods-atlas/2026-11-22/run_recipe.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/run_recipe.py)
- [/code/numerical-methods-atlas/2026-11-22/tests/test_recipes.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/tests/test_recipes.py)

#### [code/numerical-methods-atlas/2026-11-21/tests/test_sparse_fem.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_sparse_fem.py)

Existing related source/check, separate from a registered fixed-input execution example.

`test_bratu_newton_krylov_refines_to_continuous_reference`

[Corresponding code edition / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

Working directory: atlas-code-2026-11-21/

```sh
python -m pytest -q tests/test_sparse_fem.py -k test_bratu_newton_krylov_refines_to_continuous_reference
```
