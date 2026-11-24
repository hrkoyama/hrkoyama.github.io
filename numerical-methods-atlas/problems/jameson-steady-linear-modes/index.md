# 定常多段RKの実空間モード減衰 / Real-space mode damping with steady multistage RK

https://hrkoyama.github.io/numerical-methods-atlas/problems/jameson-steady-linear-modes/

## 日本語

[周期格子の実残差に4段定常反復を適用し、離散モードの減衰・中立・増幅を区別します。 保存配列から作図。 初回の元精度目標未達と再実行の実測判定は保存JSONで区別します。 図の軌道・状態・時刻・反復の軸は、物理空間の次元を表しません。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/steady-rk/results/jameson-steady-linear-modes-preview.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-steady-rk/#jameson-steady-linear-modes) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#jameson-steady-linear-modes)

### 方程式・問題の定義

無次元の固定16点・周期・線形残差。疑似時間は反復パラメータです。

#### [有限次元の線形発展系](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#linear-evolution-system-ja)

$$
\dot y=Ay+b
$$

減衰回転の物理時刻と、定常残差を減衰させる擬似時間を例ごとに区別します。

#### [有限次元線形方程式と行列分解](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#finite-dimensional-linear-system-ja)

$$
A x=b
$$

$$
P A=L U
$$

$$
A=L L^\top\quad(A=A^\top>0)
$$

$$
r=b-Ax
$$

有限行列Aと右辺bの代数問題です。LU/Cholesky・混合精度改良・対称不定値鞍点系を固定例で検査し、連続PDEの解とは区別します。

#### 定常多段RKの実空間モード減衰

補助実行例 · 実行例の定義・検証式

$$
Y_j=u_n-alpha_j*dtau*(A*Y_(j-1)-b)
$$

$$
P(z)=1+z+z^2/2+z^3/6+z^4/24; lambda_4=9+2i, lambda_8=17
$$

周期格子の実残差に4段定常反復を適用し、離散モードの減衰・中立・増幅を区別します。 初回の増幅制御では元の絶対残差目標が未達でした。

### 厳密解・参照解

元の41数値目標と実際の真偽を変更せず保存します。増幅制御の絶対残差目標だけを研究結果として分離し、他40条件と保存配列からの判定再計算・正確な表示を必須にします。

#### [定常多段RKの実空間モード減衰](https://hrkoyama.github.io/numerical-methods-atlas/validation/jameson-steady-linear-modes/?lang=ja#jameson-steady-linear-modes-ja-measurements)

解析解 · 同じ問題の参照

Y_j=u_n-alpha_j*dtau*(A*Y_(j-1)-b);\quad P(z)=1+z+z^2/2+z^3/6+z^4/24; lambda_4=9+2i, lambda_8=17

無次元の固定16点・周期・線形残差。疑似時間は反復パラメータです。

固定線形例に限定。JST圧縮性流束や非線形4次RK、任意初期値の収束は検証しません。 元の全数値目標の合格を意味する公開ではありません。

#### 定常多段RKの実空間モード減衰

元の41数値目標と実際の真偽を変更せず保存します。増幅制御の絶対残差目標だけを研究結果として分離し、他40条件と保存配列からの判定再計算・正確な表示を必須にします。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-24/steady-rk/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/jameson-steady-linear-modes/?lang=ja)

### 計算法

全段で同じ基底状態を用い、全場・全段残差・評価回数を保存します。

- [Jameson型の定常多段Runge–Kutta](https://hrkoyama.github.io/numerical-methods-atlas/methods/jameson-steady-rk/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [定常多段RKの実空間モード減衰](https://hrkoyama.github.io/numerical-methods-atlas/validation/jameson-steady-linear-modes/?lang=ja)

補助実行例

周期格子の実残差に4段定常反復を適用し、離散モードの減衰・中立・増幅を区別します。 初回の増幅制御では元の絶対残差目標が未達でした。

無次元の固定16点・周期・線形残差。疑似時間は反復パラメータです。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/steady-rk/atlas-steady-rk-2026-11-24.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24/steady-rk/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24/steady-rk/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-24/steady-rk/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

固定線形例に限定。JST圧縮性流束や非線形4次RK、任意初期値の収束は検証しません。 元の全数値目標の合格を意味する公開ではありません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-24/steady-rk/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/steady-rk/run.py)
- [/code/validated-examples/2026-11-24/steady-rk/steady.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/steady-rk/steady.py)
- [/code/validated-examples/2026-11-24/steady-rk/test_cases.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/steady-rk/test_cases.py)

## English

[Apply four steady residual stages on a periodic grid, separating damping, neutrality and amplification of discrete modes. Drawn from saved arrays. The first-run goal shortfall and each rerun’s actual target decisions remain explicit in the saved JSON. Axes for trajectories, states, time or iterations do not represent physical spatial dimensions.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/steady-rk/results/jameson-steady-linear-modes-preview.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-steady-rk/#jameson-steady-linear-modes) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#jameson-steady-linear-modes-en)

### Equations and problem definitions

A fixed dimensionless sixteen-node periodic linear residual; pseudo-time is an iteration parameter.

#### [Finite-dimensional linear evolution systems](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#linear-evolution-system-en)

$$
\dot y=Ay+b
$$

Each example distinguishes physical time in damped rotation from pseudo-time used to reduce steady residuals.

#### [Finite-dimensional linear systems and factorizations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#finite-dimensional-linear-system-en)

$$
A x=b
$$

$$
P A=L U
$$

$$
A=L L^\top\quad(A=A^\top>0)
$$

$$
r=b-Ax
$$

Finite matrices A and right-hand sides b define algebraic problems. Fixed LU, Cholesky, refinement and symmetric-indefinite saddle controls are distinct from continuum PDE solutions.

#### Real-space mode damping with steady multistage RK

Supplementary execution example · Example definition or validation formula

$$
Y_j=u_n-alpha_j*dtau*(A*Y_(j-1)-b)
$$

$$
P(z)=1+z+z^2/2+z^3/6+z^4/24; lambda_4=9+2i, lambda_8=17
$$

Apply four steady residual stages on a periodic grid, separating damping, neutrality and amplification of discrete modes. The retained first run missed the original absolute residual goal in the expanding control.

### Exact and reference solutions

Retain all 41 original numerical targets and their actual decisions. Only the expanding-control absolute residual goal is a separate study outcome; the other 40 requirements and faithful recomputation from saved arrays remain mandatory.

#### [Real-space mode damping with steady multistage RK](https://hrkoyama.github.io/numerical-methods-atlas/validation/jameson-steady-linear-modes/?lang=en#jameson-steady-linear-modes-en-measurements)

Analytic reference · Reference for the same problem

Y_j=u_n-alpha_j*dtau*(A*Y_(j-1)-b);\quad P(z)=1+z+z^2/2+z^3/6+z^4/24; lambda_4=9+2i, lambda_8=17

A fixed dimensionless sixteen-node periodic linear residual; pseudo-time is an iteration parameter.

Limited to a fixed linear example; no JST compressible flux, nonlinear fourth-order RK or all-start convergence claim. Verification of this study does not mean that all original numerical targets were met.

#### Real-space mode damping with steady multistage RK

Retain all 41 original numerical targets and their actual decisions. Only the expanding-control absolute residual goal is a separate study outcome; the other 40 requirements and faithful recomputation from saved arrays remain mandatory.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-24/steady-rk/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/jameson-steady-linear-modes/?lang=en)

### Numerical methods

Use the same base state in every stage and retain complete fields, stage residuals and evaluation counts.

- [Jameson-type steady multistage Runge–Kutta](https://hrkoyama.github.io/numerical-methods-atlas/methods/jameson-steady-rk/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Real-space mode damping with steady multistage RK](https://hrkoyama.github.io/numerical-methods-atlas/validation/jameson-steady-linear-modes/?lang=en)

Supplementary execution example

Apply four steady residual stages on a periodic grid, separating damping, neutrality and amplification of discrete modes. The retained first run missed the original absolute residual goal in the expanding control.

A fixed dimensionless sixteen-node periodic linear residual; pseudo-time is an iteration parameter.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/steady-rk/atlas-steady-rk-2026-11-24.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24/steady-rk/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24/steady-rk/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-24/steady-rk/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

Limited to a fixed linear example; no JST compressible flux, nonlinear fourth-order RK or all-start convergence claim. Verification of this study does not mean that all original numerical targets were met.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-24/steady-rk/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/steady-rk/run.py)
- [/code/validated-examples/2026-11-24/steady-rk/steady.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/steady-rk/steady.py)
- [/code/validated-examples/2026-11-24/steady-rk/test_cases.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/steady-rk/test_cases.py)
