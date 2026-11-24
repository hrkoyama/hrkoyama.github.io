# 独自逆モードVJPとJVP/VJP双対性 / Original reverse-mode VJP and JVP/VJP duality

https://hrkoyama.github.io/numerical-methods-atlas/problems/reverse-vjp-duality/

## 日本語

[独立矩形Jacobianと実際の逆微分誤差、固定wide写像の実測sweep数。 図の座標は有限次元の変数・反復・診断で、物理空間の次元やPDE境界を表しません。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/results/reverse-vjp-duality-preview.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-reverse-higher-ad/#reverse-vjp-duality) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#reverse-vjp-duality)

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

#### 独自逆モードVJPとJVP/VJP双対性

補助実行例 · 実行例の定義・検証式

$$
Jv=Df(x)v, VJP=J^T w
$$

$$
<Jv,w>_Gy=<v,Gx^-1 J^T Gy w>_Gx
$$

重複gatherとbroadcastを含む真の逆tapeを独立Jacobianと照合します。

### 厳密解・参照解

固定入力・独立参照・保存候補・全判定を同じ120秒予算内で検証します。数値合格と診断用非収束を区別します。

#### [離散非線形写像の独立Jacobian・JVP・VJP](https://hrkoyama.github.io/numerical-methods-atlas/validation/reverse-vjp-duality/?lang=ja#reverse-vjp-duality-ja-measurements)

解析解 · 同じ問題の参照

Jv=Df(x)v,\quad \operatorname{VJP}(w)=J^\top w,\quad (Jv)^\top G_yw=v^\top G_x(G_x^{-1}J^\top G_yw).

固定R4→R3写像は重複gather[0,0,2]とscalar broadcastを含みます。wide写像と固定Bratu状態はサイズ7/31。Euclidean pullbackと指定SPD計量の随伴を区別します。

一般のNumPy/JAX置換や複素数ADではありません。

#### 独自逆モードVJPとJVP/VJP双対性

固定入力・独立参照・保存候補・全判定を同じ120秒予算内で検証します。数値合格と診断用非収束を区別します。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/reverse-vjp-duality/?lang=ja)

### 計算法

逆topological順のcotangent加算と独立の前向き方向計算です。

- [自動微分](https://hrkoyama.github.io/numerical-methods-atlas/methods/automatic-differentiation/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [独自逆モードVJPとJVP/VJP双対性](https://hrkoyama.github.io/numerical-methods-atlas/validation/reverse-vjp-duality/?lang=ja)

補助実行例

重複gatherとbroadcastを含む真の逆tapeを独立Jacobianと照合します。

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

一般のNumPy/JAX置換や複素数ADではありません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-24/reverse-higher-ad/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/run.py)
- [/code/validated-examples/2026-11-24/reverse-higher-ad/test_ad.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/test_ad.py)

## English

[Independent rectangular Jacobian, actual reverse differentiation error and measured sweep counts for fixed wide maps. Plot axes describe finite-dimensional variables, iterations or diagnostics, not a physical spatial dimension or PDE boundary.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/results/reverse-vjp-duality-preview.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-reverse-higher-ad/#reverse-vjp-duality) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#reverse-vjp-duality-en)

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

#### Original reverse-mode VJP and JVP/VJP duality

Supplementary execution example · Example definition or validation formula

$$
Jv=Df(x)v, VJP=J^T w
$$

$$
<Jv,w>_Gy=<v,Gx^-1 J^T Gy w>_Gx
$$

Check a genuine reverse tape, including repeated-index gather and broadcast, against independent Jacobians.

### Exact and reference solutions

Check fixed inputs, independent references, retained candidates and every gate within the same120-second budget. Numerical success and diagnostic nonconvergence are distinct.

#### [Independent Jacobians, JVPs and VJPs of discrete nonlinear maps](https://hrkoyama.github.io/numerical-methods-atlas/validation/reverse-vjp-duality/?lang=en#reverse-vjp-duality-en-measurements)

Analytic reference · Reference for the same problem

Jv=Df(x)v,\quad \operatorname{VJP}(w)=J^\top w,\quad (Jv)^\top G_yw=v^\top G_x(G_x^{-1}J^\top G_yw).

The fixed R4-to-R3 map includes repeated-index gather[0,0,2] and scalar broadcast. Wide maps and fixed Bratu states have sizes 7 and 31. Euclidean pullbacks and adjoints under specified SPD metrics are distinct.

Not a general NumPy/JAX replacement or complex AD system.

#### Original reverse-mode VJP and JVP/VJP duality

Check fixed inputs, independent references, retained candidates and every gate within the same120-second budget. Numerical success and diagnostic nonconvergence are distinct.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/reverse-vjp-duality/?lang=en)

### Numerical methods

Accumulate cotangents in reverse topological order with a separate forward directional path.

- [Automatic differentiation](https://hrkoyama.github.io/numerical-methods-atlas/methods/automatic-differentiation/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Original reverse-mode VJP and JVP/VJP duality](https://hrkoyama.github.io/numerical-methods-atlas/validation/reverse-vjp-duality/?lang=en)

Supplementary execution example

Check a genuine reverse tape, including repeated-index gather and broadcast, against independent Jacobians.

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

Not a general NumPy/JAX replacement or complex AD system.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-24/reverse-higher-ad/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/run.py)
- [/code/validated-examples/2026-11-24/reverse-higher-ad/test_ad.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/reverse-higher-ad/test_ad.py)
