# 非滑らか点・分岐・停止条件の微分範囲 / Derivative scope at kinks, branches and stopping decisions

https://hrkoyama.github.io/numerical-methods-atlas/problems/kink-branch-derivatives/

## 日本語

[保存した非滑らか関数値と停止写像、古典微分が未定義な点とtrace微分を分けた表示。 図の座標は有限次元の変数・反復・診断で、物理空間の次元やPDE境界を表しません。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/results/kink-branch-derivatives-preview.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-reverse-higher-ad/#kink-branch-derivatives) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#kink-branch-derivatives)

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

#### 非滑らか点・分岐・停止条件の微分範囲

補助実行例 · 実行例の定義・検証式

$$
x_(k+1)=.5(x_k+theta), |x_k-theta|<=1/8
$$

$$
D max(0,0)[da,db]=max(da,db)
$$

古典微分・一方向微分・実行trace微分を、kinkと停止分岐の固定例で区別します。

### 厳密解・参照解

固定入力・独立参照・保存候補・全判定を同じ120秒予算内で検証します。数値合格と診断用非収束を区別します。

#### [非滑らかな離散写像：一方向微分と実行trace](https://hrkoyama.github.io/numerical-methods-atlas/validation/kink-branch-derivatives/?lang=ja#kink-branch-derivatives-ja-measurements)

解析解 · 同じ問題の参照

x_{k+1}=\tfrac12(x_k+\theta),\quad x_K=(1-2^{-K})\theta;\quad D^+\max(0,0)[a,b]=\max(a,b);\quad q_+(h)=\frac1{16h}+\frac78\ (\theta=1/2).

abs・ReLU・clip・多項式分岐の固定7点と方向±1を用います。停止反復はx0=0、更新前に|xk−θ|≤1/8を検査し最大5更新。θ=1/4,1/2,1は切替点です。

選択した分岐の微分は普遍的なsubgradientや非滑らかな写像の線形微分ではありません。

#### 非滑らか点・分岐・停止条件の微分範囲

固定入力・独立参照・保存候補・全判定を同じ120秒予算内で検証します。数値合格と診断用非収束を区別します。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/kink-branch-derivatives/?lang=ja)

### 計算法

strict nondifferentiableを明示し、停止前<=判定の実行分岐だけを記録します。

- [自動微分](https://hrkoyama.github.io/numerical-methods-atlas/methods/automatic-differentiation/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [非滑らか点・分岐・停止条件の微分範囲](https://hrkoyama.github.io/numerical-methods-atlas/validation/kink-branch-derivatives/?lang=ja)

補助実行例

古典微分・一方向微分・実行trace微分を、kinkと停止分岐の固定例で区別します。

小さな固定入力・実数・無次元。詳しい入力と適用範囲は対応する契約に限定します。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/atlas-reverse-higher-ad-2026-11-24.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

選択した分岐の微分は普遍的なsubgradientや非滑らかな写像の線形微分ではありません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-24/reverse-higher-ad/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/run.py)
- [/code/validated-examples/2026-11-24/reverse-higher-ad/test_ad.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/test_ad.py)

## English

[Saved nonsmooth values and stopped-map samples, distinguishing undefined classical derivatives from trace derivatives. Plot axes describe finite-dimensional variables, iterations or diagnostics, not a physical spatial dimension or PDE boundary.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/results/kink-branch-derivatives-preview.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-reverse-higher-ad/#kink-branch-derivatives) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#kink-branch-derivatives-en)

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

#### Derivative scope at kinks, branches and stopping decisions

Supplementary execution example · Example definition or validation formula

$$
x_(k+1)=.5(x_k+theta), |x_k-theta|<=1/8
$$

$$
D max(0,0)[da,db]=max(da,db)
$$

Distinguish classical, one-sided directional and executed-trace derivatives at fixed kinks and stopping switches.

### Exact and reference solutions

Check fixed inputs, independent references, retained candidates and every gate within the same120-second budget. Numerical success and diagnostic nonconvergence are distinct.

#### [Nonsmooth discrete maps: directional derivatives and executed traces](https://hrkoyama.github.io/numerical-methods-atlas/validation/kink-branch-derivatives/?lang=en#kink-branch-derivatives-en-measurements)

Analytic reference · Reference for the same problem

x_{k+1}=\tfrac12(x_k+\theta),\quad x_K=(1-2^{-K})\theta;\quad D^+\max(0,0)[a,b]=\max(a,b);\quad q_+(h)=\frac1{16h}+\frac78\ (\theta=1/2).

Use seven fixed points and directions ±1 for abs, ReLU, clip and a polynomial branch. The stopped iteration starts at x0 = 0, tests |xk - theta| <= 1/8 before updating and allows at mostfive updates. Theta 1/4, 1/2 and 1 are switching points.

An executed-branch derivative is not a universal subgradient or a linear derivative of a nonsmooth map.

#### Derivative scope at kinks, branches and stopping decisions

Check fixed inputs, independent references, retained candidates and every gate within the same120-second budget. Numerical success and diagnostic nonconvergence are distinct.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/kink-branch-derivatives/?lang=en)

### Numerical methods

Report strict nondifferentiability explicitly and record the literal top-of-loop stopping branch.

- [Automatic differentiation](https://hrkoyama.github.io/numerical-methods-atlas/methods/automatic-differentiation/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Derivative scope at kinks, branches and stopping decisions](https://hrkoyama.github.io/numerical-methods-atlas/validation/kink-branch-derivatives/?lang=en)

Supplementary execution example

Distinguish classical, one-sided directional and executed-trace derivatives at fixed kinks and stopping switches.

Small fixed real dimensionless inputs; assumptions and scope are limited to the matching contract.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/atlas-reverse-higher-ad-2026-11-24.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

An executed-branch derivative is not a universal subgradient or a linear derivative of a nonsmooth map.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-24/reverse-higher-ad/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/run.py)
- [/code/validated-examples/2026-11-24/reverse-higher-ad/test_ad.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/test_ad.py)
