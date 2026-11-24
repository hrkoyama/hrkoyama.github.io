# SEIR保存則と初期線形化 / SEIR conservation and initial linearization

https://hrkoyama.github.io/numerical-methods-atlas/problems/seir-linearization/

## 日本語

[人口保存と2モードの初期線形化を別々に検査します。 保存値だけを描画します。 時間・濃度・個体数の軸は空間次元ではありません。率は教育用で疾病・実験予測ではありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/seir-linearization-preview.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-small-models/#seir-linearization) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#seir-linearization)

### 方程式・問題の定義

閉鎖人口S+E+I+R=1、β=0.6、σ=0.3、γ=0.2。η=10⁻⁴/5×10⁻⁵に対し(S,E,I,R)(0)=(1−2η,η,η,0)、0≤t≤20。出生・死亡・外部流入はありません。

#### [閉鎖SEIR区画モデル](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#seir-compartment-ja)

$$
\begin{aligned}\dot S&=-\beta SI,&\dot E&=\beta SI-\sigma E,\\\dot I&=\sigma E-\gamma I,&\dot R&=\gamma I.\end{aligned}
$$

$$
S+E+I+R=1
$$

出生死亡なし・全人口一定の教育用率です。初期過渡は2×2行列指数に比較し、感染症予測には使いません。

#### SEIR保存則と初期線形化

補助実行例 · 実行例の定義・検証式

$$
\begin{aligned}\dot S&=-\beta SI,&\dot E&=\beta SI-\sigma E,\\\dot I&=\sigma E-\gamma I,&\dot R&=\gamma I.\end{aligned}
$$

$$
\beta=0.6,\quad\sigma=0.3,\quad\gamma=0.2,\quad(S,E,I,R)(0)=(1-2\eta,\eta,\eta,0)
$$

$$
S+E+I+R=1,\quad\eta\in\{10^{-4},5\times10^{-5}\}
$$

$$
\begin{pmatrix}E_{\rm lin}(t)\\ I_{\rm lin}(t)\end{pmatrix}=\exp\!\left[t\begin{pmatrix}-0.3&0.6\\0.3&-0.2\end{pmatrix}\right]\begin{pmatrix}\eta\\\eta\end{pmatrix}
$$

人口保存と2モードの初期線形化を別々に検査します。

### 厳密解・参照解

t≤20の全ODE積分誤差・人口保存・非負性と、0≤t≤1の201参照点での線形化モデル誤差を分けます。参照では両ηの尺度付きJacobian、Radau/BDF差とη²に対する余裕、解析的な全行列指数を別資格しています。

#### [SEIR保存則と初期線形化](https://hrkoyama.github.io/numerical-methods-atlas/validation/seir-linearization/?lang=ja#seir-linearization-ja-measurements)

有限格子の数値参照 · 同じ問題の参照

\begin{aligned}\dot S&=-\beta SI,&\dot E&=\beta SI-\sigma E,\\\dot I&=\sigma E-\gamma I,&\dot R&=\gamma I.\end{aligned};\quad \beta=0.6,\quad\sigma=0.3,\quad\gamma=0.2,\quad(S,E,I,R)(0)=(1-2\eta,\eta,\eta,0);\quad S+E+I+R=1,\quad\eta\in\{10^{-4},5\times10^{-5}\};\quad \begin{pmatrix}E_{\rm lin}(t)\\ I_{\rm lin}(t)\end{pmatrix}=\exp\!\left[t\begin{pmatrix}-0.3&0.6\\0.3&-0.2\end{pmatrix}\right]\begin{pmatrix}\eta\\\eta\end{pmatrix}

閉鎖人口S+E+I+R=1、β=0.6、σ=0.3、γ=0.2。η=10⁻⁴/5×10⁻⁵に対し(S,E,I,R)(0)=(1−2η,η,η,0)、0≤t≤20。出生・死亡・外部流入はありません。

2つの小初期感染量による固定係数の整合性比較です。早期線形化をt=20全体の厳密解と見なさず、単一の優勢モードで両モードを置き換えません。実流行の予測・統計的被覆・任意人口への一般保証は行いません。

#### SEIR保存則と初期線形化

t≤20の全ODE積分誤差・人口保存・非負性と、0≤t≤1の201参照点での線形化モデル誤差を分けます。参照では両ηの尺度付きJacobian、Radau/BDF差とη²に対する余裕、解析的な全行列指数を別資格しています。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/seir-linearization/?lang=ja)

### 計算法

全4状態を固定400/800/1600ステップのRK4で積分。独立非線形参照は偏差をηで尺度化してRadau/BDFで求め、早期のE・I線形化は2×2行列指数の両モードを使います。

- [古典的RK4](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [SEIR保存則と初期線形化](https://hrkoyama.github.io/numerical-methods-atlas/validation/seir-linearization/?lang=ja)

補助実行例

人口保存と2モードの初期線形化を別々に検査します。

閉鎖人口S+E+I+R=1、β=0.6、σ=0.3、γ=0.2。η=10⁻⁴/5×10⁻⁵に対し(S,E,I,R)(0)=(1−2η,η,η,0)、0≤t≤20。出生・死亡・外部流入はありません。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/atlas-small-models-2026-11-25.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

2つの小初期感染量による固定係数の整合性比較です。早期線形化をt=20全体の厳密解と見なさず、単一の優勢モードで両モードを置き換えません。実流行の予測・統計的被覆・任意人口への一般保証は行いません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-25/small-models/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/run.py)
- [/code/validated-examples/2026-11-25/small-models/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/experiments.py)
- [/code/validated-examples/2026-11-25/small-models/io_utils.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/io_utils.py)
- [/code/validated-examples/2026-11-25/small-models/biology.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/biology.py)
- [/code/validated-examples/2026-11-25/small-models/test_models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/test_models.py)

## English

[Check population conservation and the full two-mode initial linearization separately. This figure reads saved data only. Time, concentrations and populations do not define a spatial dimension. The rates are educational, not disease or experimental predictions.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/seir-linearization-preview.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-small-models/#seir-linearization) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#seir-linearization-en)

### Equations and problem definitions

Use a closed population S+E+I+R=1 with β=0.6, σ=0.3 and γ=0.2. For η=10⁻⁴ or 5×10⁻⁵, start from (1−2η,η,η,0) and evolve to t=20. There are no births, deaths or external inflows.

#### [Closed SEIR compartment model](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#seir-compartment-en)

$$
\begin{aligned}\dot S&=-\beta SI,&\dot E&=\beta SI-\sigma E,\\\dot I&=\sigma E-\gamma I,&\dot R&=\gamma I.\end{aligned}
$$

$$
S+E+I+R=1
$$

Educational rates with no births or deaths and constant population. Compare the early transient with a full two-by-two matrix exponential; no disease forecast is made.

#### SEIR conservation and initial linearization

Supplementary execution example · Example definition or validation formula

$$
\begin{aligned}\dot S&=-\beta SI,&\dot E&=\beta SI-\sigma E,\\\dot I&=\sigma E-\gamma I,&\dot R&=\gamma I.\end{aligned}
$$

$$
\beta=0.6,\quad\sigma=0.3,\quad\gamma=0.2,\quad(S,E,I,R)(0)=(1-2\eta,\eta,\eta,0)
$$

$$
S+E+I+R=1,\quad\eta\in\{10^{-4},5\times10^{-5}\}
$$

$$
\begin{pmatrix}E_{\rm lin}(t)\\ I_{\rm lin}(t)\end{pmatrix}=\exp\!\left[t\begin{pmatrix}-0.3&0.6\\0.3&-0.2\end{pmatrix}\right]\begin{pmatrix}\eta\\\eta\end{pmatrix}
$$

Check population conservation and the full two-mode initial linearization separately.

### Exact and reference solutions

Separate full-ODE integration error, population conservation and nonnegativity through t=20 from linearization-model error at 201 reference points on 0≤t≤1. Qualify scaled Jacobians, Radau/BDF agreement with an η² margin and the analytic full matrix exponential independently.

#### [SEIR conservation and initial linearization](https://hrkoyama.github.io/numerical-methods-atlas/validation/seir-linearization/?lang=en#seir-linearization-en-measurements)

Finite-grid numerical reference · Reference for the same problem

\begin{aligned}\dot S&=-\beta SI,&\dot E&=\beta SI-\sigma E,\\\dot I&=\sigma E-\gamma I,&\dot R&=\gamma I.\end{aligned};\quad \beta=0.6,\quad\sigma=0.3,\quad\gamma=0.2,\quad(S,E,I,R)(0)=(1-2\eta,\eta,\eta,0);\quad S+E+I+R=1,\quad\eta\in\{10^{-4},5\times10^{-5}\};\quad \begin{pmatrix}E_{\rm lin}(t)\\ I_{\rm lin}(t)\end{pmatrix}=\exp\!\left[t\begin{pmatrix}-0.3&0.6\\0.3&-0.2\end{pmatrix}\right]\begin{pmatrix}\eta\\\eta\end{pmatrix}

Use a closed population S+E+I+R=1 with β=0.6, σ=0.3 and γ=0.2. For η=10⁻⁴ or 5×10⁻⁵, start from (1−2η,η,η,0) and evolve to t=20. There are no births, deaths or external inflows.

These fixed-coefficient calculations compare two small initial infection levels. The early linearization is not an exact solution through t=20, and a single dominant mode does not replace the two-mode solution. No epidemic forecast, statistical coverage or arbitrary-population guarantee is claimed.

#### SEIR conservation and initial linearization

Separate full-ODE integration error, population conservation and nonnegativity through t=20 from linearization-model error at 201 reference points on 0≤t≤1. Qualify scaled Jacobians, Radau/BDF agreement with an η² margin and the analytic full matrix exponential independently.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/seir-linearization/?lang=en)

### Numerical methods

Evolve all four physical states with RK4 at 400, 800 and 1600 fixed steps. Independently compute the nonlinear reference with scaled-deviation Radau/BDF and the early E/I linearization with both modes of the full 2×2 matrix exponential.

- [Classical RK4](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [SEIR conservation and initial linearization](https://hrkoyama.github.io/numerical-methods-atlas/validation/seir-linearization/?lang=en)

Supplementary execution example

Check population conservation and the full two-mode initial linearization separately.

Use a closed population S+E+I+R=1 with β=0.6, σ=0.3 and γ=0.2. For η=10⁻⁴ or 5×10⁻⁵, start from (1−2η,η,η,0) and evolve to t=20. There are no births, deaths or external inflows.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/atlas-small-models-2026-11-25.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

These fixed-coefficient calculations compare two small initial infection levels. The early linearization is not an exact solution through t=20, and a single dominant mode does not replace the two-mode solution. No epidemic forecast, statistical coverage or arbitrary-population guarantee is claimed.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-25/small-models/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/run.py)
- [/code/validated-examples/2026-11-25/small-models/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/experiments.py)
- [/code/validated-examples/2026-11-25/small-models/io_utils.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/io_utils.py)
- [/code/validated-examples/2026-11-25/small-models/biology.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/biology.py)
- [/code/validated-examples/2026-11-25/small-models/test_models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/test_models.py)
