# Fisher–KPP：特殊波速の厳密前線 / Fisher–KPP: a special-speed exact front

https://hrkoyama.github.io/numerical-methods-atlas/problems/fisher-kpp-special-front/

## 日本語

[波形・位置・格子誤差・時間誤差・有限領域の影響を分けます。 特殊前線を一般の最小速度2の前線と同一視しません。急減衰初期値からの速度選択、長時間伝播、機械誤差込みの厳密障壁証明は対象外です。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/fisher-kpp-special-front.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-biology-space-controls/#fisher-kpp-special-front) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#fisher-kpp-special-front)

### 方程式・問題の定義

D=r=1、T=1。Ablowitz–Zeppetella型の特殊波速5/√6、L=12の空間・時間系列、定数端点L=6/12/24の境界比較を固定します。

#### [Fisher–KPP侵入前線](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-fisher-kpp-ja)

$$
u_t=D\Delta u+ru(1-u)
$$

$$
0\leq u\leq1
$$

拡散と増殖を結ぶ侵入前線。表示は規格化した代表形で、波の速度と境界条件は解説先へ。 全モデル族の実装ではありません。今回の固定例：Fisher–KPP：特殊波速の厳密前線

#### Fisher–KPP：特殊波速の厳密前線

補助実行例 · 実行例の定義・検証式

$$
u_t=u_{xx}+u(1-u)
$$

$$
u(x,t)=[1+\exp((x-5t/\sqrt6)/\sqrt6)]^{-2}
$$

波形・位置・格子誤差・時間誤差・有限領域の影響を分けます。

### 厳密解・参照解

厳密波形と1/4等値線、同一格子の時間収束、全域と中央領域の境界誤差を別保存します。実数算術の離散障壁と、実測した浮動小数点の余裕を区別します。

#### [Fisher–KPP：特殊波速の厳密前線](https://hrkoyama.github.io/numerical-methods-atlas/validation/fisher-kpp-special-front/?lang=ja#fisher-kpp-special-front-ja-measurements)

解析解 · 同じ問題の参照

u_t=u_{xx}+u(1-u);\quad u(x,t)=[1+\exp((x-5t/\sqrt6)/\sqrt6)]^{-2}

D=r=1、T=1、特殊速度5/√6を固定。L=12で空間・時間系列を調べ、L=6/12/24で定数端点の境界系列を比較します。無次元で拡散係数と反応率は1。厳密前線の境界値と定数境界を区別し、有限領域の影響を残します。

特殊前線を一般の最小速度2の前線と同一視しません。急減衰初期値からの速度選択、長時間伝播、機械誤差込みの厳密障壁証明は対象外です。

#### Fisher–KPP：特殊波速の厳密前線

厳密波形と1/4等値線、同一格子の時間収束、全域と中央領域の境界誤差を別保存します。実数算術の離散障壁と、実測した浮動小数点の余裕を区別します。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/fisher-kpp-special-front/?lang=ja)

### 計算法

2次中心差分とSSPRK3で計算し、厳密Dirichlet値を各段の時刻で与えます。時間誤差は同じ95未知数の半離散ODE参照と比較します。

- [SSPRK(3,3)](https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk33/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [Dormand–Prince RK45](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk45/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [Fisher–KPP：特殊波速の厳密前線](https://hrkoyama.github.io/numerical-methods-atlas/validation/fisher-kpp-special-front/?lang=ja)

補助実行例

波形・位置・格子誤差・時間誤差・有限領域の影響を分けます。

D=r=1、T=1。Ablowitz–Zeppetella型の特殊波速5/√6、L=12の空間・時間系列、定数端点L=6/12/24の境界比較を固定します。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/atlas-biology-space-controls-2026-11-25.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

特殊前線を一般の最小速度2の前線と同一視しません。急減衰初期値からの速度選択、長時間伝播、機械誤差込みの厳密障壁証明は対象外です。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-25/biology-space-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/run.py)
- [/code/validated-examples/2026-11-25/biology-space-controls/common.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/common.py)
- [/code/validated-examples/2026-11-25/biology-space-controls/fisher.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/fisher.py)
- [/code/validated-examples/2026-11-25/biology-space-controls/test_models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/test_models.py)

## English

[Separate profile, phase, grid, time and finite-boundary errors. The special front is distinct from the minimum linear speed2. This is not a steep-data speed-selection study, long-time propagation result or certified machine-error barrier proof.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/fisher-kpp-special-front.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-biology-space-controls/#fisher-kpp-special-front) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#fisher-kpp-special-front-en)

### Equations and problem definitions

Use D=r=1,T=1 and the special speed5/√6. Fix spatial/time series on L12 and constant-endpoint boundary rows at L6/12/24.

#### [Fisher–KPP invasion front](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-fisher-kpp-en)

$$
u_t=D\Delta u+ru(1-u)
$$

$$
0\leq u\leq1
$$

Spatial spread of an invading population or advantageous allele, represented by a reaction–diffusion front. Fisher–KPP is a conventional family name; the independent KPP 1937 original remains an archival follow-up. The exact special speed is not the minimal speed. Not implementation of the entire model family. Fixed cases: Fisher–KPP: a special-speed exact front

#### Fisher–KPP: a special-speed exact front

Supplementary execution example · Example definition or validation formula

$$
u_t=u_{xx}+u(1-u)
$$

$$
u(x,t)=[1+\exp((x-5t/\sqrt6)/\sqrt6)]^{-2}
$$

Separate profile, phase, grid, time and finite-boundary errors.

### Exact and reference solutions

Save exact-profile and quarter-contour errors, same-grid time convergence and full/core boundary errors. Distinguish a real-arithmetic discrete barrier from the observed floating-point margin.

#### [Fisher–KPP: a special-speed exact front](https://hrkoyama.github.io/numerical-methods-atlas/validation/fisher-kpp-special-front/?lang=en#fisher-kpp-special-front-en-measurements)

Analytic reference · Reference for the same problem

u_t=u_{xx}+u(1-u);\quad u(x,t)=[1+\exp((x-5t/\sqrt6)/\sqrt6)]^{-2}

Use D=r=1,T=1 and the special speed5/√6. Fix spatial/time series on L12 and constant-endpoint boundary rows at L6/12/24. Dimensionless; diffusion coefficient and reaction rate equal 1. Separate exact-front and constant boundary experiments; retain finite-domain effects.

The special front is distinct from the minimum linear speed2. This is not a steep-data speed-selection study, long-time propagation result or certified machine-error barrier proof.

#### Fisher–KPP: a special-speed exact front

Save exact-profile and quarter-contour errors, same-grid time convergence and full/core boundary errors. Distinguish a real-arithmetic discrete barrier from the observed floating-point margin.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/fisher-kpp-special-front/?lang=en)

### Numerical methods

Use centered second-order differences and SSPRK3 with exact Dirichlet values at every stage. Compare time errors to an independent reference for the same95-unknown semidiscreteODE.

- [SSPRK(3,3)](https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk33/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Dormand–Prince RK45](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk45/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Fisher–KPP: a special-speed exact front](https://hrkoyama.github.io/numerical-methods-atlas/validation/fisher-kpp-special-front/?lang=en)

Supplementary execution example

Separate profile, phase, grid, time and finite-boundary errors.

Use D=r=1,T=1 and the special speed5/√6. Fix spatial/time series on L12 and constant-endpoint boundary rows at L6/12/24.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/atlas-biology-space-controls-2026-11-25.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

The special front is distinct from the minimum linear speed2. This is not a steep-data speed-selection study, long-time propagation result or certified machine-error barrier proof.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-25/biology-space-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/run.py)
- [/code/validated-examples/2026-11-25/biology-space-controls/common.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/common.py)
- [/code/validated-examples/2026-11-25/biology-space-controls/fisher.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/fisher.py)
- [/code/validated-examples/2026-11-25/biology-space-controls/test_models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/test_models.py)
