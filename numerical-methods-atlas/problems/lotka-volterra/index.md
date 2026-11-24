# Lotka–Volterra不変量と正値性 / Lotka–Volterra invariant and positivity

https://hrkoyama.github.io/numerical-methods-atlas/problems/lotka-volterra/

## 日本語

[正の軌道を独立な対数座標参照と比較します。 保存値だけを描画します。 時間・濃度・個体数の軸は空間次元ではありません。率は教育用で疾病・実験予測ではありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/lotka-volterra-preview.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-small-models/#lotka-volterra) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#lotka-volterra)

### 方程式・問題の定義

無次元の捕食者・被食者系x′=x(1−y)、y′=y(x−1)、初期値(1.2,0.8)、0≤t≤20。正の象限で不変量H=x−log x+y−log yを評価します。

#### [Lotka–Volterra捕食・被食](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-lotka-volterra-ja)

$$
\dot x=\alpha x-\beta xy
$$

$$
\dot y=\delta xy-\gamma y
$$

捕食・被食の結合ODE。位相平面と長時間積分を考えるためのモデルです。 限定した実行例：1初期値・有限時間の固定比較です。連続系の閉軌道を引き込み極限周期とは呼びません。RK4の厳密な不変量保存、任意刻みでの正値性、長時間の構造保存は保証しません。

#### Lotka–Volterra不変量と正値性

補助実行例 · 実行例の定義・検証式

$$
\dot x=x(1-y),\quad\dot y=y(x-1),\quad(x(0),y(0))=(1.2,0.8),\quad0\le t\le20
$$

$$
H(x,y)=x-\log x+y-\log y,\quad\frac{dH}{dt}=0\quad(x>0,y>0)
$$

$$
\frac{d\log x}{dt}=1-e^{\log y},\quad\frac{d\log y}{dt}=e^{\log x}-1
$$

正の軌道を独立な対数座標参照と比較します。

### 厳密解・参照解

独立参照との状態誤差、Hのドリフト、保存された軌道の最小値を別々に測定。参照側では解析Jacobian、Radau/BDF差、刻み精度、Hの時間微分の恒等式を事前資格しています。

#### [Lotka–Volterra不変量と正値性](https://hrkoyama.github.io/numerical-methods-atlas/validation/lotka-volterra/?lang=ja#lotka-volterra-ja-measurements)

有限格子の数値参照 · 同じ問題の参照

\dot x=x(1-y),\quad\dot y=y(x-1),\quad(x(0),y(0))=(1.2,0.8),\quad0\le t\le20;\quad H(x,y)=x-\log x+y-\log y,\quad\frac{dH}{dt}=0\quad(x>0,y>0);\quad \frac{d\log x}{dt}=1-e^{\log y},\quad\frac{d\log y}{dt}=e^{\log x}-1

無次元の捕食者・被食者系x′=x(1−y)、y′=y(x−1)、初期値(1.2,0.8)、0≤t≤20。正の象限で不変量H=x−log x+y−log yを評価します。

1初期値・有限時間の固定比較です。連続系の閉軌道を引き込み極限周期とは呼びません。RK4の厳密な不変量保存、任意刻みでの正値性、長時間の構造保存は保証しません。

#### Lotka–Volterra不変量と正値性

独立参照との状態誤差、Hのドリフト、保存された軌道の最小値を別々に測定。参照側では解析Jacobian、Radau/BDF差、刻み精度、Hの時間微分の恒等式を事前資格しています。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/lotka-volterra/?lang=ja)

### 計算法

固定400/800/1600ステップの古典RK4で物理状態を積分します。独立参照はlog x・log yの変数でRadau/BDFを実行し、主計算には対数変数や保存量の射影を導入しません。

- [古典的RK4](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [Lotka–Volterra不変量と正値性](https://hrkoyama.github.io/numerical-methods-atlas/validation/lotka-volterra/?lang=ja)

補助実行例

正の軌道を独立な対数座標参照と比較します。

無次元の捕食者・被食者系x′=x(1−y)、y′=y(x−1)、初期値(1.2,0.8)、0≤t≤20。正の象限で不変量H=x−log x+y−log yを評価します。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/atlas-small-models-2026-11-25.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

1初期値・有限時間の固定比較です。連続系の閉軌道を引き込み極限周期とは呼びません。RK4の厳密な不変量保存、任意刻みでの正値性、長時間の構造保存は保証しません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-25/small-models/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/run.py)
- [/code/validated-examples/2026-11-25/small-models/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/experiments.py)
- [/code/validated-examples/2026-11-25/small-models/io_utils.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/io_utils.py)
- [/code/validated-examples/2026-11-25/small-models/biology.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/biology.py)
- [/code/validated-examples/2026-11-25/small-models/test_models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/test_models.py)

## English

[Compare a positive orbit against an independently integrated log-coordinate reference. This figure reads saved data only. Time, concentrations and populations do not define a spatial dimension. The rates are educational, not disease or experimental predictions.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/lotka-volterra-preview.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-small-models/#lotka-volterra) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#lotka-volterra-en)

### Equations and problem definitions

Use the dimensionless predator–prey equations x′=x(1−y), y′=y(x−1), initial state (1.2,0.8) and 0≤t≤20. Evaluate H=x−log x+y−log y only in the positive quadrant.

#### [Lotka–Volterra predator–prey](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-lotka-volterra-en)

$$
\dot x=\alpha x-\beta xy
$$

$$
\dot y=\delta xy-\gamma y
$$

Coupled prey growth and predation; a phase-plane and long-time integration test. Scoped executed example: This is a finite-time comparison for one initial state. The continuum closed orbit is not an attracting limit cycle. RK4 is not claimed to preserve H exactly, maintain positivity at arbitrary steps or guarantee long-time geometric fidelity.

#### Lotka–Volterra invariant and positivity

Supplementary execution example · Example definition or validation formula

$$
\dot x=x(1-y),\quad\dot y=y(x-1),\quad(x(0),y(0))=(1.2,0.8),\quad0\le t\le20
$$

$$
H(x,y)=x-\log x+y-\log y,\quad\frac{dH}{dt}=0\quad(x>0,y>0)
$$

$$
\frac{d\log x}{dt}=1-e^{\log y},\quad\frac{d\log y}{dt}=e^{\log x}-1
$$

Compare a positive orbit against an independently integrated log-coordinate reference.

### Exact and reference solutions

Measure state error against the independent reference, drift of H and the minimum saved population separately. The reference stage qualifies analytic Jacobians, Radau/BDF agreement, tolerance refinement and the identity dH/dt=0.

#### [Lotka–Volterra invariant and positivity](https://hrkoyama.github.io/numerical-methods-atlas/validation/lotka-volterra/?lang=en#lotka-volterra-en-measurements)

Finite-grid numerical reference · Reference for the same problem

\dot x=x(1-y),\quad\dot y=y(x-1),\quad(x(0),y(0))=(1.2,0.8),\quad0\le t\le20;\quad H(x,y)=x-\log x+y-\log y,\quad\frac{dH}{dt}=0\quad(x>0,y>0);\quad \frac{d\log x}{dt}=1-e^{\log y},\quad\frac{d\log y}{dt}=e^{\log x}-1

Use the dimensionless predator–prey equations x′=x(1−y), y′=y(x−1), initial state (1.2,0.8) and 0≤t≤20. Evaluate H=x−log x+y−log y only in the positive quadrant.

This is a finite-time comparison for one initial state. The continuum closed orbit is not an attracting limit cycle. RK4 is not claimed to preserve H exactly, maintain positivity at arbitrary steps or guarantee long-time geometric fidelity.

#### Lotka–Volterra invariant and positivity

Measure state error against the independent reference, drift of H and the minimum saved population separately. The reference stage qualifies analytic Jacobians, Radau/BDF agreement, tolerance refinement and the identity dH/dt=0.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/lotka-volterra/?lang=en)

### Numerical methods

Integrate physical populations with classical RK4 at 400, 800 and 1600 fixed steps. Independent Radau/BDF references evolve log x and log y; the primary method uses neither a log-coordinate update nor invariant projection.

- [Classical RK4](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Lotka–Volterra invariant and positivity](https://hrkoyama.github.io/numerical-methods-atlas/validation/lotka-volterra/?lang=en)

Supplementary execution example

Compare a positive orbit against an independently integrated log-coordinate reference.

Use the dimensionless predator–prey equations x′=x(1−y), y′=y(x−1), initial state (1.2,0.8) and 0≤t≤20. Evaluate H=x−log x+y−log y only in the positive quadrant.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/atlas-small-models-2026-11-25.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This is a finite-time comparison for one initial state. The continuum closed orbit is not an attracting limit cycle. RK4 is not claimed to preserve H exactly, maintain positivity at arbitrary steps or guarantee long-time geometric fidelity.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-25/small-models/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/run.py)
- [/code/validated-examples/2026-11-25/small-models/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/experiments.py)
- [/code/validated-examples/2026-11-25/small-models/io_utils.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/io_utils.py)
- [/code/validated-examples/2026-11-25/small-models/biology.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/biology.py)
- [/code/validated-examples/2026-11-25/small-models/test_models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/test_models.py)
