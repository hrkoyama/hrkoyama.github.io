# 2D C-grid回転浅水波の実時間発展 / Actual2D C-grid rotating shallow-water time advance

https://hrkoyama.github.io/numerical-methods-atlas/problems/cgrid-rotating-wave/

## 日本語

[実際に保存した計算配列と固定入力の収束指標から描いた検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/results/cgrid-rotating-wave-preview.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-moving-waves/#cgrid-rotating-wave) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#cgrid-rotating-wave)

### 方程式・問題の定義

線形f-plane、g=H=f=1、周期単位正方形、(k,l)=(1,2)、eta振幅.01、N16/32/64,T.5。別の固定N16時間系列、zero-modeと離散geostrophic診断。

#### [線形回転浅水方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#linear-rotating-shallow-water-ja)

$$
\eta_t+H(u_x+v_y)=0,\qquad u_t-fv=-g\eta_x,\qquad v_t+fu=-g\eta_y
$$

$$
g=H=f=1,\quad \widetilde k=2\sin(kh/2)/h,\quad C=\cos(kh/2)\cos(lh/2)
$$

$$
\omega_h^2=f^2C^2+gH(\widetilde k^2+\widetilde l^2)
$$

平面f-planeの線形波を実際の2D staggered C-gridでRK4時間発展します。連続分散と離散記号の参照を分け、質量・エネルギー・慣性振動・離散定常釣合いを確認します。

#### 2D C-grid回転浅水波の実時間発展

補助実行例 · 実行例の定義・検証式

$$
\eta_t+u_x+v_y=0,\quad u_t=v-\eta_x,\quad v_t=-u-\eta_y
$$

$$
\tilde k=2\sin(kh/2)/h,\quad C=\cos(kh/2)\cos(lh/2),\quad U_h(t)=e^{tL_h}U_h(0)
$$

実際の2D staggered場を時間積分し、連続波と離散symbolの参照を分けて比較します。

### 厳密解・参照解

連続PDE空間誤差と離散symbol時間誤差、mass/energy、stencil-symbol一致、zero-mode慣性振動と離散定常釣合いを保存。

#### [C-grid：連続Fourier解と離散記号の行列指数](https://hrkoyama.github.io/numerical-methods-atlas/validation/cgrid-rotating-wave/?lang=ja#cgrid-rotating-wave-ja-measurements)

解析解 · 同じ問題の参照

Q(t)=exp(t*L)Q0; ktilde=2*sin(k*h/2)/h; ltilde=2*sin(l*h/2)/h; C=cos(k*h/2)*cos(l*h/2); g=H=f=1.

線形f-plane、g=H=f=1、周期単位正方形、(k,l)=(1,2)、eta振幅.01、N16/32/64,T.5。別の固定N16時間系列、zero-modeと離散geostrophic診断。η₀=.01cos[2π(x+2y)]、u₀=v₀=0を、連続3×3 Fourier作用素と離散3×3記号の行列指数で別々に発展させます。主計算は実際の2次元staggered場を時間更新します。

線形・平面・周期squareの限定例。非線形浅水、PV・球面格子・全球dynamical coreやWilliamsonは未実装の後続課題。

#### 2D C-grid回転浅水波の実時間発展

連続PDE空間誤差と離散symbol時間誤差、mass/energy、stencil-symbol一致、zero-mode慣性振動と離散定常釣合いを保存。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/cgrid-rotating-wave/?lang=ja)

### 計算法

セルeta・法線face u/vの差分と4点Coriolis補間を2Dで評価しRK4更新。3×3行列指数は参照だけで、PDE場の更新には使いません。

- [空間中心差分](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [古典的RK4](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [2D C-grid回転浅水波の実時間発展](https://hrkoyama.github.io/numerical-methods-atlas/validation/cgrid-rotating-wave/?lang=ja)

補助実行例

実際の2D staggered場を時間積分し、連続波と離散symbolの参照を分けて比較します。

線形f-plane、g=H=f=1、周期単位正方形、(k,l)=(1,2)、eta振幅.01、N16/32/64,T.5。別の固定N16時間系列、zero-modeと離散geostrophic診断。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/atlas-moving-waves-2026-11-23.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

線形・平面・周期squareの限定例。非線形浅水、PV・球面格子・全球dynamical coreやWilliamsonは未実装の後続課題。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-23/moving-waves/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/run.py)
- [/code/validated-examples/2026-11-23/moving-waves/transport.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/transport.py)
- [/code/validated-examples/2026-11-23/moving-waves/references/exact.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/references/exact.py)
- [/code/validated-examples/2026-11-23/moving-waves/test_moving.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/test_moving.py)

## English

[Validation preview from actual saved PDE arrays and fixed-input refinement measurements.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/results/cgrid-rotating-wave-preview.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-moving-waves/#cgrid-rotating-wave) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#cgrid-rotating-wave-en)

### Equations and problem definitions

Linear f-plane,g=H=f=1, periodic unit square, mode(1,2),height amplitude.01,N16/32/64,T.5. Separate N16 time refinement, zero-mode and discrete geostrophic probes.

#### [Linear rotating shallow-water equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#linear-rotating-shallow-water-en)

$$
\eta_t+H(u_x+v_y)=0,\qquad u_t-fv=-g\eta_x,\qquad v_t+fu=-g\eta_y
$$

$$
g=H=f=1,\quad \widetilde k=2\sin(kh/2)/h,\quad C=\cos(kh/2)\cos(lh/2)
$$

$$
\omega_h^2=f^2C^2+gH(\widetilde k^2+\widetilde l^2)
$$

Actual2D staggered C-grid fields use RK4 on a planar linear f-plane. Separate continuous and semidiscrete references, checking mass,energy,inertial oscillation and discrete geostrophic balance.

#### Actual2D C-grid rotating shallow-water time advance

Supplementary execution example · Example definition or validation formula

$$
\eta_t+u_x+v_y=0,\quad u_t=v-\eta_x,\quad v_t=-u-\eta_y
$$

$$
\tilde k=2\sin(kh/2)/h,\quad C=\cos(kh/2)\cos(lh/2),\quad U_h(t)=e^{tL_h}U_h(0)
$$

Time-advance actual2D staggered fields and distinguish continuous-wave references from semidiscrete symbols.

### Exact and reference solutions

Retain continuous-PDE spatial and discrete-symbol temporal errors, mass/energy, stencil-symbol identity, zero-mode inertia and discrete steady balance.

#### [C-grid: continuous Fourier solution and discrete-symbol exponential](https://hrkoyama.github.io/numerical-methods-atlas/validation/cgrid-rotating-wave/?lang=en#cgrid-rotating-wave-en-measurements)

Analytic reference · Reference for the same problem

Q(t)=exp(t*L)Q0; ktilde=2*sin(k*h/2)/h; ltilde=2*sin(l*h/2)/h; C=cos(k*h/2)*cos(l*h/2); g=H=f=1.

Linear f-plane,g=H=f=1, periodic unit square, mode(1,2),height amplitude.01,N16/32/64,T.5. Separate N16 time refinement, zero-mode and discrete geostrophic probes. Evolve eta0=.01cos[2pi(x+2y)],u0=v0=0 with separate continuous3x3 Fourier-operator and discrete3x3-symbol exponentials. The primary actually advances2D staggered fields.

Linear planar periodic square only. Nonlinear SWE,PV,spherical dynamics and Williamson tests remain future work.

#### Actual2D C-grid rotating shallow-water time advance

Retain continuous-PDE spatial and discrete-symbol temporal errors, mass/energy, stencil-symbol identity, zero-mode inertia and discrete steady balance.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/cgrid-rotating-wave/?lang=en)

### Numerical methods

Actual2D cell-height/face-velocity differences and four-point Coriolis interpolation use RK4. The3×3 matrix exponential is reference-only, never the PDE update.

- [Centered spatial difference](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Classical RK4](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Actual2D C-grid rotating shallow-water time advance](https://hrkoyama.github.io/numerical-methods-atlas/validation/cgrid-rotating-wave/?lang=en)

Supplementary execution example

Time-advance actual2D staggered fields and distinguish continuous-wave references from semidiscrete symbols.

Linear f-plane,g=H=f=1, periodic unit square, mode(1,2),height amplitude.01,N16/32/64,T.5. Separate N16 time refinement, zero-mode and discrete geostrophic probes.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/atlas-moving-waves-2026-11-23.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

Linear planar periodic square only. Nonlinear SWE,PV,spherical dynamics and Williamson tests remain future work.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-23/moving-waves/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/run.py)
- [/code/validated-examples/2026-11-23/moving-waves/transport.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/transport.py)
- [/code/validated-examples/2026-11-23/moving-waves/references/exact.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/references/exact.py)
- [/code/validated-examples/2026-11-23/moving-waves/test_moving.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/test_moving.py)
