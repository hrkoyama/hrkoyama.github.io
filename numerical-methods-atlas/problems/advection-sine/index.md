# 周期正弦波の線形移流 / Periodic sine-wave advection

https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/

## 日本語

[保存済みのCIP・線形補間・厳密な移流波形。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/advection-sine.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/stability/) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#advection-sine)

### 方程式・問題の定義

この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。

#### [線形移流](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#linear-advection-ja)

$$
\partial_t u+a\,\partial_xu=0
$$

一定速度aによる輸送。波形の移動、数値拡散、安定性へ。

#### 周期正弦波の線形移流：風上法と解析解

共通実行例 · 問題の式

$$
u_t+a\,u_x=0,\qquad a=1,\qquad x\in[0,1)\ \text{periodic}
$$

$$
u(x,0)=1+0.2\sin(2\pi x),\qquad u_{\rm ref}(x,t)=1+0.2\sin[2\pi(x-t)]
$$

一次風上差分＋前進Euler、入力CFL=0.5。連続PDEの平行移動を参照し、離散増幅因子を厳密解として再利用しない。

#### WENO-JS／Z：臨界点とεの固定比較

補助実行例 · 実行例の定義・検証式

$$
\bar q_i=h^{-1}\int_{x_i-h/2}^{x_i+h/2}q(x)\,dx,\qquad q^-_{i+1/2}=\sum_{k=0}^2\omega_k p_k
$$

$$
(p_0,p_1,p_2)=\frac16(2\bar q_{i-2}-7\bar q_{i-1}+11\bar q_i,-\bar q_{i-1}+5\bar q_i+2\bar q_{i+1},2\bar q_i+5\bar q_{i+1}-\bar q_{i+2})
$$

$$
\omega_k=\alpha_k/\sum_j\alpha_j,\quad d=(.1,.6,.3),\quad\alpha_k^{JS}=d_k/(\epsilon+\beta_k)^2,\quad\alpha_k^Z=d_k[1+(\tau_5/(\epsilon+\beta_k))^2],\quad\tau_5=|\beta_0-\beta_2|
$$

$$
\partial_tq+\partial_xq=0,\quad q(x,t)=q_0(x-t),\quad\frac{d\bar q_i}{dt}=-\frac{q^-_{i+1/2}-q^-_{i-1/2}}h
$$

$$
\bar q_i(t)=\operatorname{sinc}(h)\cos\theta_i+.075\operatorname{sinc}(h)\sin\theta_i-.025\operatorname{sinc}(3h)\sin(3\theta_i),\quad\theta_i=2\pi(x_i-t),\quad\operatorname{sinc}(z)=\frac{\sin\pi z}{\pi z}
$$

同じセル平均からのWENO5再構成と実際の周期輸送で、JS重みとZ二乗重みを比較します。3種類の臨界性、3種類のε、固定格子と時間刻み半減を分けて保存します。

### 厳密解・参照解

周期正弦波の解析的な平行移動が基準です。問題台帳には振幅や離散表現の異なる比較を統合しており、参照解一覧の振幅0.25を全実行例に流用しません。

#### [移流／正弦波の平行移動](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=sine-advection)

解析解 · 関連モデルの参照

u = 1 + 0.25 sin[2π(x−t)]

単位区間の周期境界、一定移流速度1。

同じ周期・速度1の正弦移流モデルです。参照一覧は振幅0.25、共通固定入力は0.2で、DG・CIP等の表現や時間も異なります。

#### [WENO臨界点：多項式セル平均と解析的周期輸送](https://hrkoyama.github.io/numerical-methods-atlas/validation/weno-critical-epsilon/?lang=ja#weno-critical-epsilon-ja-measurements)

解析解 · 関連モデルの参照

qbar_i=h^-1 integral_Ci q0(x-t)dx; q0=cos(2pi*x)+.1*sin(2pi*x)^3; local P=x+...+x^5, x²+x³+x⁴+x⁵, or x³+x⁴+x⁵.

局所参照はx=0を中心とする5セルの解析平均からh/2を評価する多項式です。通常・一次・二次臨界の3形、h=1/64…1/512を区別します。実際の周期輸送参照は[0,1]、速度1、T1、q₀=cos(2πx)+.1sin³(2πx)のFourier積分セル平均で、別のGauss12点関数求積と照合します。局所多項式と輸送の初期形は異なり、点値や別PDE計算の参照ではありません。

同じ一定速度の周期移流に対する追加参照ですが、cos+.1sin³のセル平均と局所臨界多項式は、従来の単一正弦・CIP表示と異なります。

#### 周期正弦波の線形移流：風上法と解析解

CSVは128点の格子中心に1行ずつ配置し、同じ時刻・位置で解析値を評価する。平均の保存と最大値原理には丸め誤差許容値10^-12を用いる。

- [CSVは128点の格子中心に1行ずつ配置し、同じ時刻・位置で解析値を評価する。平均の保存と最大値原理には丸め誤差許容値10^-12を用いる。](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/advection-sine/result.json)
- [保存結果](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/advection-sine/result.json)
- [保存結果](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/advection-sine/solution.csv)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/advection-sine/?lang=ja)

#### WENO-JS／Z：臨界点とεの固定比較

実行前契約で72局所再構成・24PDE計算・36pytestを固定します。解析セル平均を独立Gauss12求積と照合し、局所の誤差・重み、輸送のL1/L2/L∞・質量・全段有限性・中間時刻と保存流束を記録します。最細格子で6通りの刻み半減差が対応する連続解誤差の10%以下か確認します。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-23/weno-critical/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/weno-critical-epsilon/?lang=ja)

### 計算法

この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。 セル平均からのWENO-JS／Z二乗重みの臨界点再構成と、実際の周期スカラー輸送を比較します。εの違い、解析セル平均と点値、空間誤差と時間刻みの影響を分けます。

- [風上差分（upwind）](https://hrkoyama.github.io/numerical-methods-atlas/methods/upwind/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [WENO5-JS](https://hrkoyama.github.io/numerical-methods-atlas/methods/weno-js/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [有限差分WENO5-Z](https://hrkoyama.github.io/numerical-methods-atlas/methods/weno-z/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [古典的RK4](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [周期正弦波の線形移流：風上法と解析解](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/advection-sine/?lang=ja)

共通実行例

長さ1の周期区間でq_t+a q_x=0を1周期進め、64/128点の1次風上法を平行移動した正弦波と比較する。計算値、解析値、誤差をCSVへ出す。

一定速度a=1、平均1、振幅0.2、基本モード。既存difference_stepを前進Eulerで呼び、実際の|C|≤0.5になる等間隔時間刻みを使う。入力で速度・正弦波・区間・格子を指定できるが、非ゼロ速度、正振幅、十分なモード解像とCFL条件を検査する。

[コード / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip) · [検証記録](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

[固定入力](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/recipes/advection-sine.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python run_recipe.py --input recipes/advection-sine.json --output output-advection-sine
python -m pytest -q tests/test_recipes.py
```

この滑らかな一定速度・周期問題だけの判定。0.02のL1基準は振幅0.2の10%であり、1次法の拡散を許容する。格子倍増の誤差比は実測指標で、一般の次数・非周期境界・非線形保存則の保証ではない。無効な入力や判定不合格は失敗として返す。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/numerical-methods-atlas/2026-11-22/run_recipe.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/run_recipe.py)
- [/code/numerical-methods-atlas/2026-11-22/tests/test_recipes.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/tests/test_recipes.py)

#### [WENO-JS／Z：臨界点とεの固定比較](https://hrkoyama.github.io/numerical-methods-atlas/validation/weno-critical-epsilon/?lang=ja)

補助実行例

同じセル平均からのWENO5再構成と実際の周期輸送で、JS重みとZ二乗重みを比較します。3種類の臨界性、3種類のε、固定格子と時間刻み半減を分けて保存します。

局所多項式のセル中心x=0、再構成面h/2、h=1/64…1/512を使います。輸送は[0,1]周期・速度1・q₀=cos(2πx)+.1sin³(2πx)、T=1、32/64/128セルです。全て有限体積セル平均であり、点値を誤差の参照にしません。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/weno-critical/atlas-weno-critical-2026-11-23.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/weno-critical/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23/weno-critical/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-23/weno-critical/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

一次臨界点の面再構成だけに次数判定を置き、二次臨界点は診断値として残します。固定εは解の振幅・単位に依存します。局所再構成の次数とPDE全体の次数、有限体積版と原著の有限差分版を区別します。衝撃波、Euler/MHD、一般の高次臨界点、任意入力の安定性・TVD・正値性は今回の保証に含めません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-23/weno-critical/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/weno-critical/run.py)
- [/code/validated-examples/2026-11-23/weno-critical/weno.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/weno-critical/weno.py)
- [/code/validated-examples/2026-11-23/weno-critical/references/analytic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/weno-critical/references/analytic.py)
- [/code/validated-examples/2026-11-23/weno-critical/test_weno.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/weno-critical/test_weno.py)

## English

[Stored CIP, linear-interpolation and exact advection profiles.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/advection-sine.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/stability/) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#advection-sine-en)

### Equations and problem definitions

Representative equations related to this problem. See the image/problem conditions and each execution example for initial conditions, boundary conditions and parameters.

#### [Linear advection](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#linear-advection-en)

$$
\partial_t u+a\,\partial_xu=0
$$

Transport at constant speed a: translation, numerical diffusion and stability.

#### Periodic sine advection: upwind and analytic transport

Common execution example · Problem definition

$$
u_t+a\,u_x=0,\qquad a=1,\qquad x\in[0,1)\ \text{periodic}
$$

$$
u(x,0)=1+0.2\sin(2\pi x),\qquad u_{\rm ref}(x,t)=1+0.2\sin[2\pi(x-t)]
$$

First-order upwind plus forward Euler, input CFL=0.5. The reference is continuous-PDE translation, not the discrete amplification factor.

#### WENO-JS/Z: fixed critical-point and epsilon comparison

Supplementary execution example · Example definition or validation formula

$$
\bar q_i=h^{-1}\int_{x_i-h/2}^{x_i+h/2}q(x)\,dx,\qquad q^-_{i+1/2}=\sum_{k=0}^2\omega_k p_k
$$

$$
(p_0,p_1,p_2)=\frac16(2\bar q_{i-2}-7\bar q_{i-1}+11\bar q_i,-\bar q_{i-1}+5\bar q_i+2\bar q_{i+1},2\bar q_i+5\bar q_{i+1}-\bar q_{i+2})
$$

$$
\omega_k=\alpha_k/\sum_j\alpha_j,\quad d=(.1,.6,.3),\quad\alpha_k^{JS}=d_k/(\epsilon+\beta_k)^2,\quad\alpha_k^Z=d_k[1+(\tau_5/(\epsilon+\beta_k))^2],\quad\tau_5=|\beta_0-\beta_2|
$$

$$
\partial_tq+\partial_xq=0,\quad q(x,t)=q_0(x-t),\quad\frac{d\bar q_i}{dt}=-\frac{q^-_{i+1/2}-q^-_{i-1/2}}h
$$

$$
\bar q_i(t)=\operatorname{sinc}(h)\cos\theta_i+.075\operatorname{sinc}(h)\sin\theta_i-.025\operatorname{sinc}(3h)\sin(3\theta_i),\quad\theta_i=2\pi(x_i-t),\quad\operatorname{sinc}(z)=\frac{\sin\pi z}{\pi z}
$$

Compare WENO5 JS and Z power-two weights from the same cell means, then evolve actual periodic transport. Retain three regularity classes, three epsilon choices, fixed grids and separate halved-time-step diagnostics.

### Exact and reference solutions

Analytic translation of a periodic sine is the standard. The problem merges different amplitudes and representations; the reference-library amplitude 0.25 is not the input for every execution example.

#### [Advection / sine translation](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=sine-advection)

Analytic reference · Related-model reference

u = 1 + 0.25 sin[2π(x−t)]

Periodic unit interval; constant advection speed 1.

Same periodic sine-transport model at speed one. The library amplitude is 0.25 versus 0.2 in the common fixed input; DG/CIP representations and output times also differ.

#### [WENO critical points: polynomial cell means and analytic periodic transport](https://hrkoyama.github.io/numerical-methods-atlas/validation/weno-critical-epsilon/?lang=en#weno-critical-epsilon-en-measurements)

Analytic reference · Related-model reference

qbar_i=h^-1 integral_Ci q0(x-t)dx; q0=cos(2pi*x)+.1*sin(2pi*x)^3; local P=x+...+x^5, x²+x³+x⁴+x⁵, or x³+x⁴+x⁵.

Local references integrate polynomials over five cells centered around x=0 and evaluate at h/2. Regular, first-critical and second-critical profiles use h=1/64…1/512. The actual periodic-transport reference is the Fourier-integrated cell mean of q₀=cos(2πx)+.1sin³(2πx) on[0,1], speed1,T1, checked independently by Gauss12 point-function quadrature. Local polynomials differ from the evolved profile; neither point samples nor another PDE calculation are substituted for cell means.

An additional constant-speed periodic-transport reference. The cos+.1sin³ cell means and local critical polynomials differ from the historical single-sine/CIP display.

#### Periodic sine advection: upwind and analytic transport

CSV contains one row per fine-grid center, with the analytic reference evaluated at exactly the same time and location. Periodic-mean and maximum-principle checks allow 10^-12 for roundoff.

- [CSV contains one row per fine-grid center, with the analytic reference evaluated at exactly the same time and location. Periodic-mean and maximum-principle checks allow 10^-12 for roundoff.](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/advection-sine/result.json)
- [Saved result](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/advection-sine/result.json)
- [Saved result](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/advection-sine/solution.csv)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/advection-sine/?lang=en)

#### WENO-JS/Z: fixed critical-point and epsilon comparison

Pre-run contract fixes72 local reconstructions,24 PDE runs and36 pytest checks. Qualify analytic means against independent Gauss12 quadrature; retain local errors/weights, transport L1/L2/Linf, mass, stage finiteness, intermediate times and shared-flux budgets. Six finest-grid half-dt differences must be at most10% of corresponding continuum errors.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-23/weno-critical/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/weno-critical-epsilon/?lang=en)

### Numerical methods

Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions. Compare critical-point reconstruction from cell means using WENO-JS/Z power-two weights and actual periodic scalar transport. Separate epsilon choices, analytic cell means versus point values, and spatial error versus time-step effects.

- [Upwind finite differences](https://hrkoyama.github.io/numerical-methods-atlas/methods/upwind/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [WENO5-JS](https://hrkoyama.github.io/numerical-methods-atlas/methods/weno-js/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [FD WENO5-Z](https://hrkoyama.github.io/numerical-methods-atlas/methods/weno-z/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Classical RK4](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Periodic sine advection: upwind and analytic transport](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/advection-sine/?lang=en)

Common execution example

Advance q_t+a q_x=0 for one period on a unit periodic interval. Compare first-order upwind on 64/128 points with an analytically translated sine, exporting computed, analytic and error values.

Constant speed a=1, mean 1, amplitude 0.2 and the fundamental mode. Existing difference_step is called with forward Euler and equal time steps with actual |C|≤0.5. Inputs expose the speed, sine, interval and grids, with nonzero speed, positive amplitude, mode resolution and CFL checks.

[Code / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip) · [Verification receipt](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

[Fixed input](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/recipes/advection-sine.json)

[File manifest and hashes](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python run_recipe.py --input recipes/advection-sine.json --output output-advection-sine
python -m pytest -q tests/test_recipes.py
```

Acceptance is limited to this smooth constant-speed periodic problem. The 0.02 L1 threshold is 10% of the 0.2 amplitude and permits first-order diffusion. The grid-doubling ratio is empirical, not a general order, nonperiodic-boundary or nonlinear-conservation-law guarantee. Invalid inputs and failed acceptance are reported as failures.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/numerical-methods-atlas/2026-11-22/run_recipe.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/run_recipe.py)
- [/code/numerical-methods-atlas/2026-11-22/tests/test_recipes.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/tests/test_recipes.py)

#### [WENO-JS/Z: fixed critical-point and epsilon comparison](https://hrkoyama.github.io/numerical-methods-atlas/validation/weno-critical-epsilon/?lang=en)

Supplementary execution example

Compare WENO5 JS and Z power-two weights from the same cell means, then evolve actual periodic transport. Retain three regularity classes, three epsilon choices, fixed grids and separate halved-time-step diagnostics.

Local polynomials have center x=0 and target h/2, h=1/64…1/512. Transport uses periodic[0,1], unit speed, q₀=cos(2πx)+.1sin³(2πx), T=1 and32/64/128 cells. All evolved states/references are FV cell means, not point samples.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/weno-critical/atlas-weno-critical-2026-11-23.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/weno-critical/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23/weno-critical/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-23/weno-critical/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

Order gates concern the chosen first-critical interface reconstruction; second-critical values remain diagnostic. Fixed epsilon depends on amplitude/units. Distinguish reconstruction order from PDE convergence and this FV implementation from original FD papers. No shock/Euler/MHD, arbitrary higher-critical-point, universal stability/TVD or positivity guarantee is claimed.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-23/weno-critical/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/weno-critical/run.py)
- [/code/validated-examples/2026-11-23/weno-critical/weno.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/weno-critical/weno.py)
- [/code/validated-examples/2026-11-23/weno-critical/references/analytic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/weno-critical/references/analytic.py)
- [/code/validated-examples/2026-11-23/weno-critical/test_weno.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/weno-critical/test_weno.py)
