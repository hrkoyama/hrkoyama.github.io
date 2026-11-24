# 酵素反応の保存と準定常近似 / Enzyme conservation and QSSA

https://hrkoyama.github.io/numerical-methods-atlas/problems/enzyme-qssa/

## 日本語

[全4状態と準定常近似を比較し、初期層と積分誤差を分けます。 保存値だけを描画します。 時間・濃度・個体数の軸は空間次元ではありません。率は教育用で疾病・実験予測ではありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/enzyme-qssa-preview.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-small-models/#enzyme-qssa) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#enzyme-qssa)

### 方程式・問題の定義

閉鎖反応E+S⇌C→E+Pを無次元化し、k₁=10、k₋₁=k₂=1、S₀=1、C₀=P₀=0、E₀=0.01/0.002。Kₘ=0.2、ε=E₀/(Kₘ+S₀)=1/120,1/600、θ=E₀t∈[0,0.5]です。

#### [Michaelis–Mentenと完全酵素反応系](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-enzyme-ja)

$$
E+S\mathrel{\mathop{\rightleftharpoons}^{k_1}_{k_{-1}}}C\mathrel{\mathop{\longrightarrow}^{k_2}}E+P
$$

$$
v=V_{\max}S/(K_M+S)
$$

酵素・基質・複合体の反応と飽和速度則。完全反応系、迅速平衡近似、準定常近似の違いは解説先へ。 限定した実行例：2つの小εと固定反応定数だけの教育例です。εは尺度比であり、その値だけを厳密なQSSA誤差上界とはしません。θ≥0.02を初期層終了の証明とは呼ばず、生体内の反応・観測値へ外挿しません。

#### 酵素反応の保存と準定常近似

補助実行例 · 実行例の定義・検証式

$$
\begin{aligned}\dot S&=-10ES+C,&\dot C&=10ES-2C,\\\dot E&=-10ES+2C,&\dot P&=C.\end{aligned}
$$

$$
E+C=E_0,\quad S+C+P=1,\quad K_m=\frac{k_{-1}+k_2}{k_1}=0.2
$$

$$
\theta=E_0t,\quad \varepsilon=\frac{E_0}{K_m+S_0}\in\left\{\frac1{120},\frac1{600}\right\}
$$

$$
\frac{dS_{\rm MM}}{d\theta}=-\frac{S_{\rm MM}}{0.2+S_{\rm MM}},\quad S_{\rm MM}+0.2\log S_{\rm MM}=1-\theta
$$

全4状態と準定常近似を比較し、初期層と積分誤差を分けます。

### 厳密解・参照解

独立な全系Radau/BDF参照、縮約式の陰的スカラー恒等式、E+C=E₀とS+C+P=1、正値性、実際の採用・棄却・Newton作業を照合。初期層を含む全時間と、事前指定θ≥0.02の近似誤差を別保存します。

#### [酵素反応の保存と準定常近似](https://hrkoyama.github.io/numerical-methods-atlas/validation/enzyme-qssa/?lang=ja#enzyme-qssa-ja-measurements)

有限格子の数値参照 · 同じ問題の参照

\begin{aligned}\dot S&=-10ES+C,&\dot C&=10ES-2C,\\\dot E&=-10ES+2C,&\dot P&=C.\end{aligned};\quad E+C=E_0,\quad S+C+P=1,\quad K_m=\frac{k_{-1}+k_2}{k_1}=0.2;\quad \theta=E_0t,\quad \varepsilon=\frac{E_0}{K_m+S_0}\in\left\{\frac1{120},\frac1{600}\right\};\quad \frac{dS_{\rm MM}}{d\theta}=-\frac{S_{\rm MM}}{0.2+S_{\rm MM}},\quad S_{\rm MM}+0.2\log S_{\rm MM}=1-\theta

閉鎖反応E+S⇌C→E+Pを無次元化し、k₁=10、k₋₁=k₂=1、S₀=1、C₀=P₀=0、E₀=0.01/0.002。Kₘ=0.2、ε=E₀/(Kₘ+S₀)=1/120,1/600、θ=E₀t∈[0,0.5]です。

2つの小εと固定反応定数だけの教育例です。εは尺度比であり、その値だけを厳密なQSSA誤差上界とはしません。θ≥0.02を初期層終了の証明とは呼ばず、生体内の反応・観測値へ外挿しません。

#### 酵素反応の保存と準定常近似

独立な全系Radau/BDF参照、縮約式の陰的スカラー恒等式、E+C=E₀とS+C+P=1、正値性、実際の採用・棄却・Newton作業を照合。初期層を含む全時間と、事前指定θ≥0.02の近似誤差を別保存します。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/enzyme-qssa/?lang=ja)

### 計算法

全4状態をSDIRK2のstep doublingで積分し、各段のNewton法では同じ重み付きL∞残差とArmijo条件を使います。縮約Michaelis–Menten式はθ上の別RK4計算で求め、全系の積分誤差と近似モデル誤差を混同しません。

- [L安定なSDIRK2](https://hrkoyama.github.io/numerical-methods-atlas/methods/sdirk2/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [適応SDIRK2／ステップ倍分割](https://hrkoyama.github.io/numerical-methods-atlas/methods/step-doubling/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [Armijo減衰Newton法](https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [古典的RK4](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [酵素反応の保存と準定常近似](https://hrkoyama.github.io/numerical-methods-atlas/validation/enzyme-qssa/?lang=ja)

補助実行例

全4状態と準定常近似を比較し、初期層と積分誤差を分けます。

閉鎖反応E+S⇌C→E+Pを無次元化し、k₁=10、k₋₁=k₂=1、S₀=1、C₀=P₀=0、E₀=0.01/0.002。Kₘ=0.2、ε=E₀/(Kₘ+S₀)=1/120,1/600、θ=E₀t∈[0,0.5]です。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/atlas-small-models-2026-11-25.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

2つの小εと固定反応定数だけの教育例です。εは尺度比であり、その値だけを厳密なQSSA誤差上界とはしません。θ≥0.02を初期層終了の証明とは呼ばず、生体内の反応・観測値へ外挿しません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-25/small-models/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/run.py)
- [/code/validated-examples/2026-11-25/small-models/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/experiments.py)
- [/code/validated-examples/2026-11-25/small-models/io_utils.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/io_utils.py)
- [/code/validated-examples/2026-11-25/small-models/biology.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/biology.py)
- [/code/validated-examples/2026-11-25/small-models/test_models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/test_models.py)

## English

[Separate the initial layer, integration error and QSSA modeling error in a four-state enzyme mechanism. This figure reads saved data only. Time, concentrations and populations do not define a spatial dimension. The rates are educational, not disease or experimental predictions.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/enzyme-qssa-preview.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-small-models/#enzyme-qssa) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#enzyme-qssa-en)

### Equations and problem definitions

Use the closed dimensionless reaction E+S⇌C→E+P with k₁=10, k₋₁=k₂=1, S₀=1, C₀=P₀=0 and E₀=0.01 or 0.002. Then Kₘ=0.2, ε=E₀/(Kₘ+S₀)=1/120 or 1/600, and θ=E₀t ranges from 0 to 0.5.

#### [Michaelis–Menten and full enzyme kinetics](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-enzyme-en)

$$
E+S\mathrel{\mathop{\rightleftharpoons}^{k_1}_{k_{-1}}}C\mathrel{\mathop{\longrightarrow}^{k_2}}E+P
$$

$$
v=V_{\max}S/(K_M+S)
$$

Enzyme saturation; the full mass-action system resolves the transient complex C, while the rate law eliminates a fast variable. The 1913 rapid-equilibrium interpretation and the 1925 quasi-steady-state derivation must remain distinct. Scoped executed example: These two small-ε fixed-rate examples are educational. ε is a scale ratio, not itself a certified QSSA error bound. The θ≥0.02 window is not a proof that the initial layer has ended, and the calculation is not an in-vivo prediction.

#### Enzyme conservation and QSSA

Supplementary execution example · Example definition or validation formula

$$
\begin{aligned}\dot S&=-10ES+C,&\dot C&=10ES-2C,\\\dot E&=-10ES+2C,&\dot P&=C.\end{aligned}
$$

$$
E+C=E_0,\quad S+C+P=1,\quad K_m=\frac{k_{-1}+k_2}{k_1}=0.2
$$

$$
\theta=E_0t,\quad \varepsilon=\frac{E_0}{K_m+S_0}\in\left\{\frac1{120},\frac1{600}\right\}
$$

$$
\frac{dS_{\rm MM}}{d\theta}=-\frac{S_{\rm MM}}{0.2+S_{\rm MM}},\quad S_{\rm MM}+0.2\log S_{\rm MM}=1-\theta
$$

Separate the initial layer, integration error and QSSA modeling error in a four-state enzyme mechanism.

### Exact and reference solutions

Compare with independent full-system Radau/BDF references and an implicit scalar identity for the reduced equation. Check E+C=E₀, S+C+P=1, positivity and actual acceptance, rejection and Newton work. Retain both all-time errors including the initial layer and errors on the declared θ≥0.02 window.

#### [Enzyme conservation and QSSA](https://hrkoyama.github.io/numerical-methods-atlas/validation/enzyme-qssa/?lang=en#enzyme-qssa-en-measurements)

Finite-grid numerical reference · Reference for the same problem

\begin{aligned}\dot S&=-10ES+C,&\dot C&=10ES-2C,\\\dot E&=-10ES+2C,&\dot P&=C.\end{aligned};\quad E+C=E_0,\quad S+C+P=1,\quad K_m=\frac{k_{-1}+k_2}{k_1}=0.2;\quad \theta=E_0t,\quad \varepsilon=\frac{E_0}{K_m+S_0}\in\left\{\frac1{120},\frac1{600}\right\};\quad \frac{dS_{\rm MM}}{d\theta}=-\frac{S_{\rm MM}}{0.2+S_{\rm MM}},\quad S_{\rm MM}+0.2\log S_{\rm MM}=1-\theta

Use the closed dimensionless reaction E+S⇌C→E+P with k₁=10, k₋₁=k₂=1, S₀=1, C₀=P₀=0 and E₀=0.01 or 0.002. Then Kₘ=0.2, ε=E₀/(Kₘ+S₀)=1/120 or 1/600, and θ=E₀t ranges from 0 to 0.5.

These two small-ε fixed-rate examples are educational. ε is a scale ratio, not itself a certified QSSA error bound. The θ≥0.02 window is not a proof that the initial layer has ended, and the calculation is not an in-vivo prediction.

#### Enzyme conservation and QSSA

Compare with independent full-system Radau/BDF references and an implicit scalar identity for the reduced equation. Check E+C=E₀, S+C+P=1, positivity and actual acceptance, rejection and Newton work. Retain both all-time errors including the initial layer and errors on the declared θ≥0.02 window.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/enzyme-qssa/?lang=en)

### Numerical methods

Integrate all four states with SDIRK2 step doubling, using the same weighted L∞ residual for Newton convergence and Armijo backtracking. Evolve the reduced Michaelis–Menten equation separately with RK4 in θ, keeping integration error distinct from model-reduction error.

- [L-stable SDIRK2](https://hrkoyama.github.io/numerical-methods-atlas/methods/sdirk2/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Adaptive SDIRK2 / step doubling](https://hrkoyama.github.io/numerical-methods-atlas/methods/step-doubling/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Armijo-damped Newton](https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Classical RK4](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Enzyme conservation and QSSA](https://hrkoyama.github.io/numerical-methods-atlas/validation/enzyme-qssa/?lang=en)

Supplementary execution example

Separate the initial layer, integration error and QSSA modeling error in a four-state enzyme mechanism.

Use the closed dimensionless reaction E+S⇌C→E+P with k₁=10, k₋₁=k₂=1, S₀=1, C₀=P₀=0 and E₀=0.01 or 0.002. Then Kₘ=0.2, ε=E₀/(Kₘ+S₀)=1/120 or 1/600, and θ=E₀t ranges from 0 to 0.5.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/atlas-small-models-2026-11-25.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

These two small-ε fixed-rate examples are educational. ε is a scale ratio, not itself a certified QSSA error bound. The θ≥0.02 window is not a proof that the initial layer has ended, and the calculation is not an in-vivo prediction.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-25/small-models/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/run.py)
- [/code/validated-examples/2026-11-25/small-models/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/experiments.py)
- [/code/validated-examples/2026-11-25/small-models/io_utils.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/io_utils.py)
- [/code/validated-examples/2026-11-25/small-models/biology.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/biology.py)
- [/code/validated-examples/2026-11-25/small-models/test_models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/test_models.py)
