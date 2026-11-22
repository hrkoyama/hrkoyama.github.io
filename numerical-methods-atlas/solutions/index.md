# 厳密解・参照解 / Exact and reference solutions

Source: https://hrkoyama.github.io/numerical-methods-atlas/assets/reference-solutions.json

SHA-256: `c33118198faa7b35b4f66d7aad6353206f6d90c848f12e0a059874b91f897edc`

## 日本語

### 移流／正弦波の平行移動

解析解 · 1次元

`u = 1 + 0.25 sin[2π(x−t)]`

単位区間の周期境界、一定移流速度1。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=sine-advection) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/reference-solutions/)

### 熱拡散／Fourierモードの減衰

解析解 · 1次元

`u = 1 + 0.25 sin(2πx) exp[−0.02(2π)²t]`

単位区間の周期境界、拡散係数0.02。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=sine-heat) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/reference-solutions/)

### Burgers／衝撃波

解析解 · 1次元

`u_t + (u²/2)_x = 0`

全直線上のスカラーRiemann問題のエントロピー解。端点の外側は一定値で継続します。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=burgers-shock) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/reference-solutions/)

### Burgers／膨張波

解析解 · 1次元

`u_t + (u²/2)_x = 0`

全直線上のスカラーRiemann問題のエントロピー解。端点の外側は一定値で継続します。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=burgers-fan) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/reference-solutions/)

### 交通流／上流へ進む衝撃波

解析解 · 1次元

`rho_t + [rho(1−rho)]_x = 0`

全直線上のスカラーRiemann問題のエントロピー解。端点の外側は一定値で継続します。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=traffic-jam) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/reference-solutions/)

### 交通流／渋滞解消の膨張波

解析解 · 1次元

`rho_t + [rho(1−rho)]_x = 0`

全直線上のスカラーRiemann問題のエントロピー解。端点の外側は一定値で継続します。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=traffic-fan) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/reference-solutions/)

### Euler／Sod問題

半解析解 · 1次元

`U(x,t) = R((x−x0)/t)`

比熱比gamma>1の理想気体、平面1次元波。真空の保存変数はゼロ、速度は未定義です。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=euler-sod) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/reference-solutions/)

### Euler／Lax問題

半解析解 · 1次元

`U(x,t) = R((x−x0)/t)`

比熱比gamma>1の理想気体、平面1次元波。真空の保存変数はゼロ、速度は未定義です。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=euler-lax) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/reference-solutions/)

### Euler／二重膨張波

半解析解 · 1次元

`U(x,t) = R((x−x0)/t)`

比熱比gamma>1の理想気体、平面1次元波。真空の保存変数はゼロ、速度は未定義です。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=euler-double-rarefaction) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/reference-solutions/)

### Euler／生成される真空

解析解 · 1次元

`U(x,t) = R((x−x0)/t)`

比熱比gamma>1の理想気体、平面1次元波。真空の保存変数はゼロ、速度は未定義です。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=euler-vacuum) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/reference-solutions/)

### 浅水流／水深が正のダム崩壊

半解析解 · 1次元

`U(x,t) = R((x−x0)/t)`

平坦な底面と一定の重力g。乾床は参照解のみの対応で、既存の有限体積ソルバーでは扱えません。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=swe-dam-break) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/reference-solutions/)

### 浅水／乾床への膨張波

解析解 · 1次元

`U(x,t) = R((x−x0)/t)`

平坦な底面と一定の重力g。乾床は参照解のみの対応で、既存の有限体積ソルバーでは扱えません。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=swe-dry-bed) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/reference-solutions/)

### 浅水／中央の乾燥領域

解析解 · 1次元

`U(x,t) = R((x−x0)/t)`

平坦な底面と一定の重力g。乾床は参照解のみの対応で、既存の有限体積ソルバーでは扱えません。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=swe-vacuum) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/reference-solutions/)

### 等温流／密度跳躍

半解析解 · 1次元

`U(x,t) = R((x−x0)/t)`

p = c_s² rho、一定の音速c_s。初期密度は厳密に正とし、真空状態とエネルギー方程式はありません。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=isothermal-jump) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/reference-solutions/)

### Poisson／正弦波の製造解

製造解 · 1次元

`u = sin(πx); −u_xx = f = π² sin(πx)`

両端はゼロDirichlet条件。目標解から外力を選ぶ製造解であり、任意の外力のPoisson解ではありません。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=poisson-manufactured) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/reference-solutions/)

### 粘性チャネル／Couette流

解析解 · 1次元

`u(y) = y`

十分に発達した平面定常チャネル。壁速度u(0)=0、u(1)=1、圧力勾配ゼロ。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=couette) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/reference-solutions/)

### 粘性チャネル／Poiseuille流

解析解 · 1次元

`u(y) = G y(1−y)/(2ν); G=1, ν=0.1`

十分に発達した平面定常チャネル、no-slip、単位密度。−dp/dx=G、または体積力加速度G。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=poiseuille) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/reference-solutions/)

### 粘性流／2次元Taylor–Green渦

解析解 · 2次元

`(u,v)=(sin x cos y,−cos x sin y)e^(−2νt); p=(cos 2x+cos 2y)e^(−4νt)/4`

周期領域[0,2π]²、単位密度、動粘性係数0.1、圧力平均ゼロ。Webではy=π/4のx方向断面を表示します。

Taylor–Green：y = π/4のx方向断面です。2次元セル平均ではなく点値を表示します。

[保存済みの解を表示](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=taylor-green) · [定義・条件を読む](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/reference-solutions/)

## English

### Advection / sine translation

Analytic reference · 1D

`u = 1 + 0.25 sin[2π(x−t)]`

Periodic unit interval; constant advection speed 1.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=sine-advection) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/reference-solutions/)

### Heat / Fourier-mode decay

Analytic reference · 1D

`u = 1 + 0.25 sin(2πx) exp[−0.02(2π)²t]`

Periodic unit interval; viscosity 0.02.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=sine-heat) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/reference-solutions/)

### Burgers / shock

Analytic reference · 1D

`u_t + (u²/2)_x = 0`

Entropy solution of a scalar whole-line Riemann problem; constant endpoint continuation.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=burgers-shock) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/reference-solutions/)

### Burgers / rarefaction

Analytic reference · 1D

`u_t + (u²/2)_x = 0`

Entropy solution of a scalar whole-line Riemann problem; constant endpoint continuation.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=burgers-fan) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/reference-solutions/)

### Traffic / upstream shock

Analytic reference · 1D

`rho_t + [rho(1−rho)]_x = 0`

Entropy solution of a scalar whole-line Riemann problem; constant endpoint continuation.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=traffic-jam) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/reference-solutions/)

### Traffic / clearing fan

Analytic reference · 1D

`rho_t + [rho(1−rho)]_x = 0`

Entropy solution of a scalar whole-line Riemann problem; constant endpoint continuation.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=traffic-fan) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/reference-solutions/)

### Euler / Sod

Semi-analytic reference · 1D

`U(x,t) = R((x−x0)/t)`

Ideal gas; gamma>1; planar 1D waves; vacuum has zero conserved state and undefined velocity.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=euler-sod) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/reference-solutions/)

### Euler / Lax

Semi-analytic reference · 1D

`U(x,t) = R((x−x0)/t)`

Ideal gas; gamma>1; planar 1D waves; vacuum has zero conserved state and undefined velocity.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=euler-lax) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/reference-solutions/)

### Euler / double rarefaction

Semi-analytic reference · 1D

`U(x,t) = R((x−x0)/t)`

Ideal gas; gamma>1; planar 1D waves; vacuum has zero conserved state and undefined velocity.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=euler-double-rarefaction) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/reference-solutions/)

### Euler / generated vacuum

Analytic reference · 1D

`U(x,t) = R((x−x0)/t)`

Ideal gas; gamma>1; planar 1D waves; vacuum has zero conserved state and undefined velocity.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=euler-vacuum) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/reference-solutions/)

### Shallow water / wet dam break

Semi-analytic reference · 1D

`U(x,t) = R((x−x0)/t)`

Flat bottom; constant g; dry states allowed in the reference only, not the existing FV solver.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=swe-dam-break) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/reference-solutions/)

### Shallow water / dry-bed fan

Analytic reference · 1D

`U(x,t) = R((x−x0)/t)`

Flat bottom; constant g; dry states allowed in the reference only, not the existing FV solver.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=swe-dry-bed) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/reference-solutions/)

### Shallow water / dry middle state

Analytic reference · 1D

`U(x,t) = R((x−x0)/t)`

Flat bottom; constant g; dry states allowed in the reference only, not the existing FV solver.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=swe-vacuum) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/reference-solutions/)

### Isothermal / density jump

Semi-analytic reference · 1D

`U(x,t) = R((x−x0)/t)`

p = c_s² rho; constant c_s; strictly positive initial density; no vacuum state or energy equation.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=isothermal-jump) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/reference-solutions/)

### Poisson / manufactured sine

Manufactured solution · 1D

`u = sin(πx); −u_xx = f = π² sin(πx)`

Zero Dirichlet endpoints. The forcing is chosen from the target solution; this is not an arbitrary-source Poisson solution.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=poisson-manufactured) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/reference-solutions/)

### Viscous channel / Couette

Analytic reference · 1D

`u(y) = y`

Fully developed planar steady channel; walls u(0)=0,u(1)=1; zero pressure gradient.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=couette) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/reference-solutions/)

### Viscous channel / Poiseuille

Analytic reference · 1D

`u(y) = G y(1−y)/(2ν); G=1, ν=0.1`

Fully developed planar steady channel, no slip, unit density; −dp/dx=G or body acceleration G.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=poiseuille) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/reference-solutions/)

### Viscous flow / 2D Taylor–Green

Analytic reference · 2D

`(u,v)=(sin x cos y,−cos x sin y)e^(−2νt); p=(cos 2x+cos 2y)e^(−4νt)/4`

Periodic [0,2π]²; unit density; viscosity 0.1; zero mean pressure. Web profile is an x-slice at y=π/4.

Taylor–Green: x-slice at y = π/4. These are point values, not two-dimensional cell averages.

[View the saved profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=taylor-green) · [Read definitions and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/reference-solutions/)
