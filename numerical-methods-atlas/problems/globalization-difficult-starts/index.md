# 同じ難しい初期値に対する線探索と信頼領域 / Line search and trust regions from the same difficult starts

https://hrkoyama.github.io/numerical-methods-atlas/problems/globalization-difficult-starts/

## 日本語

[同一初期値の保存経路、原残差、trust radiusと実測評価回数。失敗・非収束は別記します。 図の座標は有限次元の変数・反復・診断で、物理空間の次元やPDE境界を表しません。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/results/globalization-difficult-starts-preview.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-globalization-controls/#globalization-difficult-starts) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#globalization-difficult-starts)

### 方程式・問題の定義

小さな固定入力・実数・無次元。詳しい入力と適用範囲は対応する契約に限定します。

#### [有限次元非線形写像・根と微分作用](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#finite-dimensional-nonlinear-map-ja)

$$
F:\mathbb R^n\longrightarrow\mathbb R^m
$$

$$
F(x)=0\quad(m=n\text{ for root controls})
$$

$$
J(x)v=DF(x)[v],\quad J(x)^\top w
$$

$$
H_f(x)v=D(\nabla f)(x)[v]\quad(f\text{ twice differentiable})
$$

有限の代数写像に対する根・JVP/VJP・HVP・分岐規約です。nは空間次元ではなく変数数で、非滑らか点に古典微分を強制しません。

#### [Bratu非線形境界値問題](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bratu-ja)

$$
-\frac{d^2u}{dx^2}=\lambda e^u,\qquad 0<x<1
$$

$$
u(0)=u(1)=0
$$

ここでは−u″=λexp(u)の符号規約。Newton–Krylov法で残差・格子収束・内側線形解法の失敗を確認します。

#### 同じ難しい初期値に対する線探索と信頼領域

補助実行例 · 実行例の定義・検証式

$$
phi(x)=.5||S F(x)||_2^2, g=(S J)^T S F
$$

$$
p_U=-(g^Tg)/(||S J g||_2^2)g, ||p||_2<=Delta
$$

同じ固定初期値からNewton・Armijo・doglegを比較し、真の根と非根停留・予算終了を区別します。

### 厳密解・参照解

固定入力・独立参照・保存候補・全判定を同じ120秒予算内で検証します。数値合格と診断用非収束を区別します。

#### [同一初期値の大域化：解析対照と離散Bratu修正](https://hrkoyama.github.io/numerical-methods-atlas/validation/globalization-difficult-starts/?lang=ja#globalization-difficult-starts-ja-measurements)

有限格子の数値参照 · 同じ問題の参照

F_R(x,y)=(10(y-x^2),1-x)^\top,\quad (x_*,y_*)=(1,1);\quad \phi=\tfrac12\|SF\|_2^2,\quad J_h\delta=-F_h.

実数・無次元の固定系。Rosenbrockの2初期値と2残差スケール、31内点・λ=3の同次Dirichlet Bratuの3初期値を3法で比較します。状態半径はEuclideanで、残差スケールとは別です。

全初期値の成功や手法の普遍的優越、PETSc実装との一致を保証しません。

#### 同じ難しい初期値に対する線探索と信頼領域

固定入力・独立参照・保存候補・全判定を同じ120秒予算内で検証します。数値合格と診断用非収束を区別します。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/globalization-difficult-starts/?lang=ja)

### 計算法

原残差とスケール付きmeritを分離し、Euclidean doglegと全試行ledgerを保存します。

- [Armijo減衰Newton法](https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [小固定系のdogleg信頼領域法](https://hrkoyama.github.io/numerical-methods-atlas/methods/dogleg-trust-region/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [同じ難しい初期値に対する線探索と信頼領域](https://hrkoyama.github.io/numerical-methods-atlas/validation/globalization-difficult-starts/?lang=ja)

補助実行例

同じ固定初期値からNewton・Armijo・doglegを比較し、真の根と非根停留・予算終了を区別します。

小さな固定入力・実数・無次元。詳しい入力と適用範囲は対応する契約に限定します。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/atlas-globalization-controls-2026-11-24.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

全初期値の成功や手法の普遍的優越、PETSc実装との一致を保証しません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-24/globalization-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/run.py)
- [/code/validated-examples/2026-11-24/globalization-controls/test_globalization.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/test_globalization.py)

## English

[Saved paths from identical starts, original residuals, trust radii and measured evaluation counts. Failures and nonconvergence remain explicit. Plot axes describe finite-dimensional variables, iterations or diagnostics, not a physical spatial dimension or PDE boundary.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/results/globalization-difficult-starts-preview.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-globalization-controls/#globalization-difficult-starts) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#globalization-difficult-starts-en)

### Equations and problem definitions

Small fixed real dimensionless inputs; assumptions and scope are limited to the matching contract.

#### [Finite-dimensional nonlinear maps, roots and differential actions](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#finite-dimensional-nonlinear-map-en)

$$
F:\mathbb R^n\longrightarrow\mathbb R^m
$$

$$
F(x)=0\quad(m=n\text{ for root controls})
$$

$$
J(x)v=DF(x)[v],\quad J(x)^\top w
$$

$$
H_f(x)v=D(\nabla f)(x)[v]\quad(f\text{ twice differentiable})
$$

Roots, JVP/VJP, HVP and branch conventions for finite algebraic maps. The variable count n is not a spatial dimension, and a classical derivative is not imposed at nonsmooth points.

#### [Bratu nonlinear boundary-value problem](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bratu-en)

$$
-\frac{d^2u}{dx^2}=\lambda e^u,\qquad 0<x<1
$$

$$
u(0)=u(1)=0
$$

The convention here is −u″=λ exp(u). Newton–Krylov checks cover residuals, refinement and inner-solver failures.

#### Line search and trust regions from the same difficult starts

Supplementary execution example · Example definition or validation formula

$$
phi(x)=.5||S F(x)||_2^2, g=(S J)^T S F
$$

$$
p_U=-(g^Tg)/(||S J g||_2^2)g, ||p||_2<=Delta
$$

Compare Newton, Armijo and dogleg from identical fixed starts, distinguishing roots from stationary nonroots and budget exhaustion.

### Exact and reference solutions

Check fixed inputs, independent references, retained candidates and every gate within the same120-second budget. Numerical success and diagnostic nonconvergence are distinct.

#### [Globalization from identical starts: analytic controls and discrete Bratu corrections](https://hrkoyama.github.io/numerical-methods-atlas/validation/globalization-difficult-starts/?lang=en#globalization-difficult-starts-en-measurements)

Finite-grid numerical reference · Reference for the same problem

F_R(x,y)=(10(y-x^2),1-x)^\top,\quad (x_*,y_*)=(1,1);\quad \phi=\tfrac12\|SF\|_2^2,\quad J_h\delta=-F_h.

Fixed real dimensionless systems: two Rosenbrock starts and two residual scalings, plus three starts for a 31-interior-node Dirichlet Bratu problem at lambda 3, compared by three methods. The Euclidean state radius is distinct from residual scaling.

No all-start guarantee, universal method ranking or equivalence to PETSc implementation.

#### Line search and trust regions from the same difficult starts

Check fixed inputs, independent references, retained candidates and every gate within the same120-second budget. Numerical success and diagnostic nonconvergence are distinct.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/globalization-difficult-starts/?lang=en)

### Numerical methods

Separate the original residual from the scaled merit and retain Euclidean dogleg and trial ledgers.

- [Armijo-damped Newton](https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Dogleg trust regions for fixed small systems](https://hrkoyama.github.io/numerical-methods-atlas/methods/dogleg-trust-region/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Line search and trust regions from the same difficult starts](https://hrkoyama.github.io/numerical-methods-atlas/validation/globalization-difficult-starts/?lang=en)

Supplementary execution example

Compare Newton, Armijo and dogleg from identical fixed starts, distinguishing roots from stationary nonroots and budget exhaustion.

Small fixed real dimensionless inputs; assumptions and scope are limited to the matching contract.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/atlas-globalization-controls-2026-11-24.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

No all-start guarantee, universal method ranking or equivalence to PETSc implementation.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-24/globalization-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/run.py)
- [/code/validated-examples/2026-11-24/globalization-controls/test_globalization.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/globalization-controls/test_globalization.py)
