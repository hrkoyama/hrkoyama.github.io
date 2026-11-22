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

### 厳密解・参照解

周期正弦波の解析的な平行移動が基準です。問題台帳には振幅や離散表現の異なる比較を統合しており、参照解一覧の振幅0.25を全実行例に流用しません。

#### [移流／正弦波の平行移動](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=sine-advection)

解析解 · 関連モデルの参照

u = 1 + 0.25 sin[2π(x−t)]

単位区間の周期境界、一定移流速度1。

同じ周期・速度1の正弦移流モデルです。参照一覧は振幅0.25、共通固定入力は0.2で、DG・CIP等の表現や時間も異なります。

#### 周期正弦波の線形移流：風上法と解析解

CSVは128点の格子中心に1行ずつ配置し、同じ時刻・位置で解析値を評価する。平均の保存と最大値原理には丸め誤差許容値10^-12を用いる。

- [CSVは128点の格子中心に1行ずつ配置し、同じ時刻・位置で解析値を評価する。平均の保存と最大値原理には丸め誤差許容値10^-12を用いる。](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/advection-sine/result.json)
- [保存結果](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/advection-sine/result.json)
- [保存結果](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/advection-sine/solution.csv)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/advection-sine/?lang=ja)

### 計算法

この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。

- [風上差分（upwind）](https://hrkoyama.github.io/numerical-methods-atlas/methods/upwind/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

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

### Exact and reference solutions

Analytic translation of a periodic sine is the standard. The problem merges different amplitudes and representations; the reference-library amplitude 0.25 is not the input for every execution example.

#### [Advection / sine translation](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=sine-advection)

Analytic reference · Related-model reference

u = 1 + 0.25 sin[2π(x−t)]

Periodic unit interval; constant advection speed 1.

Same periodic sine-transport model at speed one. The library amplitude is 0.25 versus 0.2 in the common fixed input; DG/CIP representations and output times also differ.

#### Periodic sine advection: upwind and analytic transport

CSV contains one row per fine-grid center, with the analytic reference evaluated at exactly the same time and location. Periodic-mean and maximum-principle checks allow 10^-12 for roundoff.

- [CSV contains one row per fine-grid center, with the analytic reference evaluated at exactly the same time and location. Periodic-mean and maximum-principle checks allow 10^-12 for roundoff.](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/advection-sine/result.json)
- [Saved result](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/advection-sine/result.json)
- [Saved result](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/advection-sine/solution.csv)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/advection-sine/?lang=en)

### Numerical methods

Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions.

- [Upwind finite differences](https://hrkoyama.github.io/numerical-methods-atlas/methods/upwind/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

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
