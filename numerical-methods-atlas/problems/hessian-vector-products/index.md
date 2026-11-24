# HVPと状態固定・陰関数全微分の区別 / Hessian-vector products and fixed-state versus implicit derivatives

https://hrkoyama.github.io/numerical-methods-atlas/problems/hessian-vector-products/

## 日本語

[保存HVPと独立参照、状態固定と陰関数全微分の二階曲率を区別した比較。 図の座標は有限次元の変数・反復・診断で、物理空間の次元やPDE境界を表しません。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/results/hessian-vector-products-preview.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-reverse-higher-ad/#hessian-vector-products) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#hessian-vector-products)

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

#### HVPと状態固定・陰関数全微分の区別

補助実行例 · 実行例の定義・検証式

$$
Hv=D(grad f)(x)v
$$

$$
F=u^2-theta=0, 2u*s=1, 2u*t+2s^2=0
$$

forward-over-reverse HVPと二階陰関数則を別々の独立参照へ照合します。

### 厳密解・参照解

固定入力・独立参照・保存候補・全判定を同じ120秒予算内で検証します。数値合格と診断用非収束を区別します。

#### [固定状態HVPと二階陰関数則の独立参照](https://hrkoyama.github.io/numerical-methods-atlas/validation/hessian-vector-products/?lang=ja#hessian-vector-products-ja-measurements)

解析解 · 同じ問題の参照

Hv=D(\nabla f)(x)v;\quad H_Bv=h(A_hv-\lambda e^u\odot v);\quad 2us=1,\quad 2ut+2s^2=0,\quad j^{\prime\prime}=0.2+s^2+(u-1)t.

4変数のdyadic二次関数とサイズ7/31の固定Bratu energyを用います。別の正枝陰関数u²−θ=0はθ=4、初期値u=3から解き、状態固定偏微分と全微分を分けます。

一般のreduced inverse Hessianや有限Newton traceの数学的陰関数微分とは主張しません。

#### HVPと状態固定・陰関数全微分の区別

固定入力・独立参照・保存候補・全判定を同じ120秒予算内で検証します。数値合格と診断用非収束を区別します。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/hessian-vector-products/?lang=ja)

### 計算法

値と方向接線、cotangentとその方向接線を伝播し、陰関数はF/R1/R2を解きます。

- [自動微分](https://hrkoyama.github.io/numerical-methods-atlas/methods/automatic-differentiation/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [HVPと状態固定・陰関数全微分の区別](https://hrkoyama.github.io/numerical-methods-atlas/validation/hessian-vector-products/?lang=ja)

補助実行例

forward-over-reverse HVPと二階陰関数則を別々の独立参照へ照合します。

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

一般のreduced inverse Hessianや有限Newton traceの数学的陰関数微分とは主張しません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-24/reverse-higher-ad/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/run.py)
- [/code/validated-examples/2026-11-24/reverse-higher-ad/test_ad.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/test_ad.py)

## English

[Saved HVPs and independent references, with fixed-state and total implicit second derivatives shown separately. Plot axes describe finite-dimensional variables, iterations or diagnostics, not a physical spatial dimension or PDE boundary.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/results/hessian-vector-products-preview.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-reverse-higher-ad/#hessian-vector-products) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#hessian-vector-products-en)

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

#### Hessian-vector products and fixed-state versus implicit derivatives

Supplementary execution example · Example definition or validation formula

$$
Hv=D(grad f)(x)v
$$

$$
F=u^2-theta=0, 2u*s=1, 2u*t+2s^2=0
$$

Check forward-over-reverse HVPs and second-order implicit rules against separate independent references.

### Exact and reference solutions

Check fixed inputs, independent references, retained candidates and every gate within the same120-second budget. Numerical success and diagnostic nonconvergence are distinct.

#### [Independent references for fixed-state HVPs and second-order implicit rules](https://hrkoyama.github.io/numerical-methods-atlas/validation/hessian-vector-products/?lang=en#hessian-vector-products-en-measurements)

Analytic reference · Reference for the same problem

Hv=D(\nabla f)(x)v;\quad H_Bv=h(A_hv-\lambda e^u\odot v);\quad 2us=1,\quad 2ut+2s^2=0,\quad j^{\prime\prime}=0.2+s^2+(u-1)t.

Use a four-variable dyadic quadratic and fixed-state Bratu energies of sizes 7 and 31. A separate positive implicit branch u²-theta=0 is solved at theta 4 from initial u 3, distinguishing fixed-state partials from total derivatives.

No general reduced inverse Hessian or identification of finite Newton traces with implicit derivatives.

#### Hessian-vector products and fixed-state versus implicit derivatives

Check fixed inputs, independent references, retained candidates and every gate within the same120-second budget. Numerical success and diagnostic nonconvergence are distinct.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/hessian-vector-products/?lang=en)

### Numerical methods

Transport values, tangents, cotangents and cotangent tangents; solve F/R1/R2 for implicit derivatives.

- [Automatic differentiation](https://hrkoyama.github.io/numerical-methods-atlas/methods/automatic-differentiation/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Hessian-vector products and fixed-state versus implicit derivatives](https://hrkoyama.github.io/numerical-methods-atlas/validation/hessian-vector-products/?lang=en)

Supplementary execution example

Check forward-over-reverse HVPs and second-order implicit rules against separate independent references.

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

No general reduced inverse Hessian or identification of finite Newton traces with implicit derivatives.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-24/reverse-higher-ad/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/run.py)
- [/code/validated-examples/2026-11-24/reverse-higher-ad/test_ad.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/test_ad.py)
