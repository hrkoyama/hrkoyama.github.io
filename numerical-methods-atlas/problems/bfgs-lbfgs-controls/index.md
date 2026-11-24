# 既知最小点でのBFGSと3組L-BFGS / BFGS and three-pair L-BFGS at known minima

https://hrkoyama.github.io/numerical-methods-atlas/problems/bfgs-lbfgs-controls/

## 日本語

[実際のRosenbrock反復点と解析目的関数の等高線。3つの固定初期値・4手法を示し、全問題での収束保証ではありません。 図の座標は有限次元の変数・反復・診断で、物理空間の次元やPDE境界を表しません。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/results/bfgs-lbfgs-controls-preview.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-inverse-optimization/#bfgs-lbfgs-controls) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#bfgs-lbfgs-controls)

### 方程式・問題の定義

無次元の非有界代数的最適化。既知の解析最小点を持ち、物理PDEの境界条件はありません。

#### [有限次元代数最適化と既知最小点](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#finite-dimensional-optimization-ja)

$$
\min_{x\in\mathbb R^n} f(x)
$$

$$
\nabla f(x_*)=0\quad\text{(necessary for a smooth unconstrained local minimum)}
$$

$$
f_Q(x)=\tfrac12(x-x_*)^TA(x-x_*),\quad A=A^T>0
$$

$$
f_R(x,y)=100(y-x^2)^2+(1-x)^2
$$

8次元SPD二次関数と2変数Rosenbrockの無次元代数最適化です。物理空間・PDE境界を持たず、既知最小点と局所反復作用を比較します。

#### 既知最小点でのBFGSと3組L-BFGS

補助実行例 · 実行例の定義・検証式

$$
H_+=(I-\rho s y^T)H(I-\rho y s^T)+\rho s s^T
$$

$$
\rho=(y^Ts)^{-1},\quad\gamma_0=(s^Ty)/(y^Ty)
$$

$$
f(x,y)=100(y-x^2)^2+(1-x)^2
$$

8次元SPD二次関数と3初期値のRosenbrockを用い、曲率・strong Wolfe・現在の有限記憶作用を検査します。

### 厳密解・参照解

16固定fit、解析的な最小点・勾配、各受理stepのstrong Wolfeと解像された正曲率、BFGSの対称SPD、L-BFGS作用差を判定。保持組とoracle稠密行列の記憶を分離。

#### [既知最小点と現在の有限記憶作用に対する解析参照](https://hrkoyama.github.io/numerical-methods-atlas/validation/bfgs-lbfgs-controls/?lang=ja#bfgs-lbfgs-controls-ja-measurements)

解析解 · 同じ問題の参照

f_Q=\tfrac12(x-x_*)^TA(x-x_*),\quad x_*=(1,-1,\ldots)^T;\quad f_R=100(y-x^2)^2+(1-x)^2,\quad (x_*,y_*)=(1,1);\quad H_+=(I-\rho sy^T)H(I-\rho ys^T)+\rho ss^T.

無次元・非有界の代数最適化。8次元SPD二次関数とRosenbrockの3初期値を用い、L-BFGSは現在の最大3組だけを保持します。物理PDE境界条件はありません。

厳密線形探索ではないためn反復終了や一般的Rosenbrock大域収束を主張しません。原著選択箇所は弱Wolfeであり、本例のstrong Wolfeと区別。Fletcher1970本文は未読です。

#### 既知最小点でのBFGSと3組L-BFGS

16固定fit、解析的な最小点・勾配、各受理stepのstrong Wolfeと解像された正曲率、BFGSの対称SPD、L-BFGS作用差を判定。保持組とoracle稠密行列の記憶を分離。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/bfgs-lbfgs-controls/?lang=ja)

### 計算法

独自逆BFGSとベクトルだけの2-loop L-BFGS（3組）。独立な小稠密oracleは現在γ₀Iから現在保持する組だけを古い順に再生。SciPy BFGS/L-BFGS-B（bounds=None）を別実装として比較。

- [勾配法・準Newton法](https://hrkoyama.github.io/numerical-methods-atlas/methods/optimization/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [既知最小点でのBFGSと3組L-BFGS](https://hrkoyama.github.io/numerical-methods-atlas/validation/bfgs-lbfgs-controls/?lang=ja)

補助実行例

8次元SPD二次関数と3初期値のRosenbrockを用い、曲率・strong Wolfe・現在の有限記憶作用を検査します。

無次元の非有界代数的最適化。既知の解析最小点を持ち、物理PDEの境界条件はありません。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/atlas-inverse-optimization-2026-11-24.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

厳密線形探索ではないためn反復終了や一般的Rosenbrock大域収束を主張しません。原著選択箇所は弱Wolfeであり、本例のstrong Wolfeと区別。Fletcher1970本文は未読です。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-24/inverse-optimization/quasi_newton.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/quasi_newton.py)
- [/code/validated-examples/2026-11-24/inverse-optimization/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/run.py)
- [/code/validated-examples/2026-11-24/inverse-optimization/test_inverse_optimization.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/test_inverse_optimization.py)

## English

[Actual Rosenbrock iterates on analytic objective contours for three fixed starts and four methods; this is not a general convergence guarantee. Plot axes describe finite-dimensional variables, iterations or diagnostics, not a physical spatial dimension or PDE boundary.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/results/bfgs-lbfgs-controls-preview.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-inverse-optimization/#bfgs-lbfgs-controls) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#bfgs-lbfgs-controls-en)

### Equations and problem definitions

Dimensionless unconstrained algebraic optimization with known analytic minima; there is no physical PDE boundary condition.

#### [Finite-dimensional algebraic optimization and known minima](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#finite-dimensional-optimization-en)

$$
\min_{x\in\mathbb R^n} f(x)
$$

$$
\nabla f(x_*)=0\quad\text{(necessary for a smooth unconstrained local minimum)}
$$

$$
f_Q(x)=\tfrac12(x-x_*)^TA(x-x_*),\quad A=A^T>0
$$

$$
f_R(x,y)=100(y-x^2)^2+(1-x)^2
$$

Dimensionless algebraic optimization of an eight-dimensional SPD quadratic and a two-variable Rosenbrock function. There is no physical spatial domain or PDE boundary; compare known minima and local iterative actions.

#### BFGS and three-pair L-BFGS at known minima

Supplementary execution example · Example definition or validation formula

$$
H_+=(I-\rho s y^T)H(I-\rho y s^T)+\rho s s^T
$$

$$
\rho=(y^Ts)^{-1},\quad\gamma_0=(s^Ty)/(y^Ty)
$$

$$
f(x,y)=100(y-x^2)^2+(1-x)^2
$$

An eight-dimensional SPD quadratic and three Rosenbrock starts test curvature, strong Wolfe conditions and the current finite-memory action.

### Exact and reference solutions

Sixteen fixed fits check analytic minima/gradients, strong Wolfe and resolved positive curvature at every accepted step, symmetric SPD BFGS matrices and L-BFGS action defects. Retained-pair and dense-oracle storage are reported separately.

#### [Analytic known minima and the current limited-memory action](https://hrkoyama.github.io/numerical-methods-atlas/validation/bfgs-lbfgs-controls/?lang=en#bfgs-lbfgs-controls-en-measurements)

Analytic reference · Reference for the same problem

f_Q=\tfrac12(x-x_*)^TA(x-x_*),\quad x_*=(1,-1,\ldots)^T;\quad f_R=100(y-x^2)^2+(1-x)^2,\quad (x_*,y_*)=(1,1);\quad H_+=(I-\rho sy^T)H(I-\rho ys^T)+\rho ss^T.

Dimensionless unconstrained algebraic optimization uses an eight-dimensional SPD quadratic and three Rosenbrock starts. L-BFGS retains only the current last three pairs. There is no physical PDE boundary condition.

No exact n-step termination or general global convergence on Rosenbrock is claimed. The selected original text uses weak Wolfe, distinct from this study’s strong Wolfe policy. Fletcher’s 1970 original article remains unread.

#### BFGS and three-pair L-BFGS at known minima

Sixteen fixed fits check analytic minima/gradients, strong Wolfe and resolved positive curvature at every accepted step, symmetric SPD BFGS matrices and L-BFGS action defects. Retained-pair and dense-oracle storage are reported separately.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/bfgs-lbfgs-controls/?lang=en)

### Numerical methods

Original inverse-BFGS and vector-only two-loop L-BFGS with three pairs. A separate small dense oracle replays only currently retained pairs from the current gamma0 I. SciPy BFGS and unbounded L-BFGS-B are distinct software companions.

- [Gradient and quasi-Newton optimization](https://hrkoyama.github.io/numerical-methods-atlas/methods/optimization/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [BFGS and three-pair L-BFGS at known minima](https://hrkoyama.github.io/numerical-methods-atlas/validation/bfgs-lbfgs-controls/?lang=en)

Supplementary execution example

An eight-dimensional SPD quadratic and three Rosenbrock starts test curvature, strong Wolfe conditions and the current finite-memory action.

Dimensionless unconstrained algebraic optimization with known analytic minima; there is no physical PDE boundary condition.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/atlas-inverse-optimization-2026-11-24.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

No exact n-step termination or general global convergence on Rosenbrock is claimed. The selected original text uses weak Wolfe, distinct from this study’s strong Wolfe policy. Fletcher’s 1970 original article remains unread.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-24/inverse-optimization/quasi_newton.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/quasi_newton.py)
- [/code/validated-examples/2026-11-24/inverse-optimization/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/run.py)
- [/code/validated-examples/2026-11-24/inverse-optimization/test_inverse_optimization.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/test_inverse_optimization.py)
