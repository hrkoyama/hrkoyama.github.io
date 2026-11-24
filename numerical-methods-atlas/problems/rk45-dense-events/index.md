# RK45の埋込み推定・補間・イベント / RK45: embedded errors, dense output and events

https://hrkoyama.github.io/numerical-methods-atlas/problems/rk45-dense-events/

## 日本語

[減衰回転の解析解を使い、受理/棄却・FSAL・区間内補間・向き付き交差時刻を分けて検査します。 保存済みの数値場と参照を用いた図です。 図の軌道・状態・時刻・反復の軸は、物理空間の次元を表しません。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/rk45-dense-events-preview.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-ode-adaptivity/#rk45-dense-events) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#rk45-dense-events)

### 方程式・問題の定義

γ=.2,ω=3、初期値(1,0)、T=2。3対のrtol/atol×2最大刻みと終端交差2runで計8run。

#### [有限次元の線形発展系](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#linear-evolution-system-ja)

$$
\dot y=Ay+b
$$

減衰回転の物理時刻と、定常残差を減衰させる擬似時間を例ごとに区別します。

#### RK45の埋込み推定・補間・イベント

補助実行例 · 実行例の定義・検証式

$$
y(t)=e^{-0.2t}(\cos 3t,\sin 3t)^T,\quad t_*=\pi/6,\pi/2
$$

$$
y(t_n+\theta h)=y_n+hQ(\theta,\theta^2,\theta^3,\theta^4)^T
$$

減衰回転の解析解を使い、受理/棄却・FSAL・区間内補間・向き付き交差時刻を分けて検査します。

### 厳密解・参照解

解析状態とπ/6,π/2の単純交差を参照に、端点/97オフメッシュ点/イベント時刻・残差と実nfev=1+6試行数を判定。

#### [RK45の埋込み推定・補間・イベント](https://hrkoyama.github.io/numerical-methods-atlas/validation/rk45-dense-events/?lang=ja#rk45-dense-events-ja-measurements)

解析解 · 同じ問題の参照

y(t)=e^{-0.2t}(\cos 3t,\sin 3t)^T,\quad t_*=\pi/6,\pi/2;\quad y(t_n+\theta h)=y_n+hQ(\theta,\theta^2,\theta^3,\theta^4)^T

γ=.2,ω=3、初期値(1,0)、T=2。3対のrtol/atol×2最大刻みと終端交差2runで計8run。

接触根・1刻み内の多重交差・reset付き系の一般性は保証しません。初期零/所有権/resetは限定成分対照で、局所許容誤差と大域精度を同一視しません。

#### RK45の埋込み推定・補間・イベント

解析状態とπ/6,π/2の単純交差を参照に、端点/97オフメッシュ点/イベント時刻・残差と実nfev=1+6試行数を判定。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/rk45-dense-events/?lang=ja)

### 計算法

実Dormand–Prince5(4)・quartic連続拡張・受理状態が所有するFSAL・保存補間上の符号区間二分法。拒否端点を昇格しません。

- [Dormand–Prince RK45](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk45/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [RK45の埋込み推定・補間・イベント](https://hrkoyama.github.io/numerical-methods-atlas/validation/rk45-dense-events/?lang=ja)

補助実行例

減衰回転の解析解を使い、受理/棄却・FSAL・区間内補間・向き付き交差時刻を分けて検査します。

γ=.2,ω=3、初期値(1,0)、T=2。3対のrtol/atol×2最大刻みと終端交差2runで計8run。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/atlas-ode-adaptivity-2026-11-24-r2.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

接触根・1刻み内の多重交差・reset付き系の一般性は保証しません。初期零/所有権/resetは限定成分対照で、局所許容誤差と大域精度を同一視しません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/run.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/experiments.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/io_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/io_contract.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/reference_eval.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/reference_eval.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/dopri.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/dopri.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/tableau.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/tableau.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_boundary.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_boundary.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_contract.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_dopri.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_dopri.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_reporting.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_reporting.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_stiff.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_stiff.py)

## English

[Use analytic damped rotation to test acceptance, rejection, FSAL ownership, dense interpolation and directed event times separately. This preview reads saved numerical fields and references only. Axes for trajectories, states, time or iterations do not represent physical spatial dimensions.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/rk45-dense-events-preview.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-ode-adaptivity/#rk45-dense-events) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#rk45-dense-events-en)

### Equations and problem definitions

Use gamma = 0.2, omega = 3, initial state (1, 0), and T = 2. Three paired relative and absolute tolerances with two maximum steps, plus two terminal runs, give eight runs.

#### [Finite-dimensional linear evolution systems](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#linear-evolution-system-en)

$$
\dot y=Ay+b
$$

Each example distinguishes physical time in damped rotation from pseudo-time used to reduce steady residuals.

#### RK45: embedded errors, dense output and events

Supplementary execution example · Example definition or validation formula

$$
y(t)=e^{-0.2t}(\cos 3t,\sin 3t)^T,\quad t_*=\pi/6,\pi/2
$$

$$
y(t_n+\theta h)=y_n+hQ(\theta,\theta^2,\theta^3,\theta^4)^T
$$

Use analytic damped rotation to test acceptance, rejection, FSAL ownership, dense interpolation and directed event times separately.

### Exact and reference solutions

Analytic states and the simple crossings at pi/6 and pi/2 provide independent truth. Check endpoints, 97 off-mesh samples, event times and residuals, and the actual identity nfev = 1 + 6 times the attempted-step count.

#### [RK45: embedded errors, dense output and events](https://hrkoyama.github.io/numerical-methods-atlas/validation/rk45-dense-events/?lang=en#rk45-dense-events-en-measurements)

Analytic reference · Reference for the same problem

y(t)=e^{-0.2t}(\cos 3t,\sin 3t)^T,\quad t_*=\pi/6,\pi/2;\quad y(t_n+\theta h)=y_n+hQ(\theta,\theta^2,\theta^3,\theta^4)^T

Use gamma = 0.2, omega = 3, initial state (1, 0), and T = 2. Three paired relative and absolute tolerances with two maximum steps, plus two terminal runs, give eight runs.

There is no general guarantee for tangential roots, multiple crossings within a step or systems with resets. Initial-zero and ownership controls are limited component tests; local tolerances and global accuracy remain distinct.

#### RK45: embedded errors, dense output and events

Analytic states and the simple crossings at pi/6 and pi/2 provide independent truth. Check endpoints, 97 off-mesh samples, event times and residuals, and the actual identity nfev = 1 + 6 times the attempted-step count.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/rk45-dense-events/?lang=en)

### Numerical methods

Use actual Dormand–Prince 5(4) stages, a quartic continuous extension, an accepted-state derivative cache and bracket bisection on retained interpolants. A rejected endpoint never replaces the accepted starting derivative.

- [Dormand–Prince RK45](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk45/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [RK45: embedded errors, dense output and events](https://hrkoyama.github.io/numerical-methods-atlas/validation/rk45-dense-events/?lang=en)

Supplementary execution example

Use analytic damped rotation to test acceptance, rejection, FSAL ownership, dense interpolation and directed event times separately.

Use gamma = 0.2, omega = 3, initial state (1, 0), and T = 2. Three paired relative and absolute tolerances with two maximum steps, plus two terminal runs, give eight runs.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/atlas-ode-adaptivity-2026-11-24-r2.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

There is no general guarantee for tangential roots, multiple crossings within a step or systems with resets. Initial-zero and ownership controls are limited component tests; local tolerances and global accuracy remain distinct.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/run.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/experiments.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/io_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/io_contract.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/reference_eval.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/reference_eval.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/dopri.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/dopri.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/tableau.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/tableau.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_boundary.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_boundary.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_contract.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_dopri.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_dopri.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_reporting.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_reporting.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_stiff.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_stiff.py)
