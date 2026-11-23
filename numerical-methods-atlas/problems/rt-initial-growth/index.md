# RTの初期成長：滑らかなBoussinesq二層 / RT initial growth in smooth Boussinesq double layers

https://hrkoyama.github.io/numerical-methods-atlas/problems/rt-initial-growth/

## 日本語

[保存した2D浮力摂動をεで規格化。滑らかな二層の初期変位で、乱流混合の図ではありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/results/rt-initial-growth-preview.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-instability-growth/#rt-initial-growth) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#rt-initial-growth)

### 方程式・問題の定義

[0,2π]²周期、層厚δ=.25、ν=κ=.005、摂動ε=1e−5。32²/64²/128²格子。基底層は明示した外力で定常維持します。g=1、b0=.02 tanh(sin y/δ)、ρ/ρ0=1−b/g、T=2。慣性密度は一定で、密度跳躍の可変密度Euler系ではありません。

#### [能動浮力を伴うBoussinesq渦度系](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#boussinesq-buoyancy-ja)

$$
-\Delta\psi=\omega,\quad (u,v)=(\psi_y,-\psi_x),\quad b=b_0(y)+\theta
$$

$$
\omega_t+u\omega_x+v\omega_y=\nu\Delta\omega+\theta_x
$$

$$
\theta_t+u\theta_x+v\theta_y+v b_0^{\prime}=\kappa\Delta\theta,\qquad b_0=.02\tanh(\sin y/\delta)
$$

慣性密度を一定とし、密度差は浮力だけに残します。基底浮力を外力で維持した摂動形です。全浮力bの鉛直力のcurlがθxを与え、可変密度Euler系とは異なります。

#### RTの初期成長：滑らかなBoussinesq二層

補助実行例 · 実行例の定義・検証式

$$
-\Delta\psi=\omega,\qquad (u,v)=(\partial_y\psi,-\partial_x\psi)
$$

$$
b=b_0(y)+\theta,\quad \omega_t+\mathbf{u}\cdot\nabla\omega=\nu\Delta\omega+\theta_x,\quad \theta_t+\mathbf{u}\cdot\nabla\theta+v b_0^{\prime}=\kappa\Delta\theta
$$

$$
\sigma_T=\frac{1}{T}\log\frac{A(T)}{A(0)},\qquad \dot{\widehat{\mathbf{q}}}=L_K\widehat{\mathbf{q}}
$$

密度差を浮力だけに残す2D Boussinesq系を時間発展し、不安定な滑らかな層の初期成長を独立線形参照で調べます。

### 厳密解・参照解

群全体22単体検査・74固定判定、10回の非線形計算を事前固定。参照K24/40/56、3格子の場誤差と次数、5保存時刻の成長、64²で刻み半減・振幅半減、Poisson残差・発散・平均値を別々に検査します。

#### [RT初期成長：Boussinesq二層の線形IVP参照](https://hrkoyama.github.io/numerical-methods-atlas/validation/rt-initial-growth/?lang=ja#rt-initial-growth-ja-measurements)

有限格子の数値参照 · 同じ問題の参照

b0=.02*tanh(sin(y)/delta); omega_t=nu*Delta(omega)+theta_x; theta_t=kappa*Delta(theta)+psi_x*b0prime; -Delta(psi)=omega.

[0,2π]²周期、層厚δ=.25、ν=κ=.005、摂動ε=1e−5。32²/64²/128²格子。基底層は明示した外力で定常維持します。g=1、b0=.02 tanh(sin y/δ)、ρ/ρ0=1−b/g、T=2。慣性密度は一定で、密度跳躍の可変密度Euler系ではありません。参照は同じ滑らかな基底のkx=1連続線形化をFourier–Galerkin K24/40/56で解きます。慣性密度は一定、浮力偏差θだけが鉛直力へ入り、周期二層の一方が不安定です。

線形範囲の教育用固定入力です。線形参照は独立した空間表現であり、独立非線形PDEエンジンではありません。鋭い無限領域界面の分散式、McNallyの可圧縮入力、非線形後期の巻上がりやRT乱流を再現したとは表示しません。図の摂動はεで規格化した実計算値です。

#### RTの初期成長：滑らかなBoussinesq二層

群全体22単体検査・74固定判定、10回の非線形計算を事前固定。参照K24/40/56、3格子の場誤差と次数、5保存時刻の成長、64²で刻み半減・振幅半減、Poisson残差・発散・平均値を別々に検査します。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/rt-initial-growth/?lang=ja)

### 計算法

点値の渦度・浮力摂動を共有面の中央流束とHeun法で進め、5点差分PoissonをFFTで解きます。u=ψy,v=−ψxなので中央差分発散は整合します。基底場を解析的に差し引き、層そのものの離散ドリフトと微小摂動を分離します。

- [空間中心差分](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [Heun法／SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [RTの初期成長：滑らかなBoussinesq二層](https://hrkoyama.github.io/numerical-methods-atlas/validation/rt-initial-growth/?lang=ja)

補助実行例

密度差を浮力だけに残す2D Boussinesq系を時間発展し、不安定な滑らかな層の初期成長を独立線形参照で調べます。

[0,2π]²周期、層厚δ=.25、ν=κ=.005、摂動ε=1e−5。32²/64²/128²格子。基底層は明示した外力で定常維持します。g=1、b0=.02 tanh(sin y/δ)、ρ/ρ0=1−b/g、T=2。慣性密度は一定で、密度跳躍の可変密度Euler系ではありません。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/atlas-instability-growth-2026-11-23-r2.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

線形範囲の教育用固定入力です。線形参照は独立した空間表現であり、独立非線形PDEエンジンではありません。鋭い無限領域界面の分散式、McNallyの可圧縮入力、非線形後期の巻上がりやRT乱流を再現したとは表示しません。図の摂動はεで規格化した実計算値です。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-23-r2/instability-growth/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/run.py)
- [/code/validated-examples/2026-11-23-r2/instability-growth/flow.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/flow.py)
- [/code/validated-examples/2026-11-23-r2/instability-growth/references/linear.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/references/linear.py)
- [/code/validated-examples/2026-11-23-r2/instability-growth/test_instability.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/test_instability.py)

## English

[Saved actual2D buoyancy perturbation normalized by epsilon; an early smooth-layer displacement, not turbulent mixing.](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/results/rt-initial-growth-preview.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-instability-growth/#rt-initial-growth) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#rt-initial-growth-en)

### Equations and problem definitions

Periodic[0,2pi]², layer width.25, nu=kappa=.005, epsilon1e-5 and32²/64²/128² grids. Explicit forcing maintains the base. g1,b0=.02tanh(sin y/delta),rho/rho0=1-b/g,T2. Density enters buoyancy only; this is not variable-density Euler.

#### [Boussinesq vorticity with active buoyancy](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#boussinesq-buoyancy-en)

$$
-\Delta\psi=\omega,\quad (u,v)=(\psi_y,-\psi_x),\quad b=b_0(y)+\theta
$$

$$
\omega_t+u\omega_x+v\omega_y=\nu\Delta\omega+\theta_x
$$

$$
\theta_t+u\theta_x+v\theta_y+v b_0^{\prime}=\kappa\Delta\theta,\qquad b_0=.02\tanh(\sin y/\delta)
$$

Inertial density is constant; density contrast enters buoyancy only. Forcing maintains the base profile. The curl of vertical buoyancy yields theta_x; this is a perturbation Boussinesq system rather than variable-density Euler.

#### RT initial growth in smooth Boussinesq double layers

Supplementary execution example · Example definition or validation formula

$$
-\Delta\psi=\omega,\qquad (u,v)=(\partial_y\psi,-\partial_x\psi)
$$

$$
b=b_0(y)+\theta,\quad \omega_t+\mathbf{u}\cdot\nabla\omega=\nu\Delta\omega+\theta_x,\quad \theta_t+\mathbf{u}\cdot\nabla\theta+v b_0^{\prime}=\kappa\Delta\theta
$$

$$
\sigma_T=\frac{1}{T}\log\frac{A(T)}{A(0)},\qquad \dot{\widehat{\mathbf{q}}}=L_K\widehat{\mathbf{q}}
$$

Advance the actual2D Boussinesq vorticity/active-buoyancy system and compare smooth unstable-layer growth with a separately derived linear IVP.

### Exact and reference solutions

Freeze22pytest tests,74case gates and10nonlinear evolutions. QualifyK24/40/56references; separately check three-grid field errors/orders, five-time growth,64²halved-step/halved-amplitude probes, Poisson residual, divergence and means.

#### [RT initial growth: linear Boussinesq double-layer IVP reference](https://hrkoyama.github.io/numerical-methods-atlas/validation/rt-initial-growth/?lang=en#rt-initial-growth-en-measurements)

Finite-grid numerical reference · Reference for the same problem

b0=.02*tanh(sin(y)/delta); omega_t=nu*Delta(omega)+theta_x; theta_t=kappa*Delta(theta)+psi_x*b0prime; -Delta(psi)=omega.

Periodic[0,2pi]², layer width.25, nu=kappa=.005, epsilon1e-5 and32²/64²/128² grids. Explicit forcing maintains the base. g1,b0=.02tanh(sin y/delta),rho/rho0=1-b/g,T2. Density enters buoyancy only; this is not variable-density Euler. The reference uses the same smooth base, kx1 continuous linearization and Fourier-Galerkin truncationsK24/40/56. Inertial density is constant; buoyancy perturbation theta supplies vertical forcing, with one unstable interface in the periodic double layer.

Small-amplitude fixed educational cases. The independent reference changes spatial representation but linearizes the PDE; it is not a second nonlinear engine. No sharp-interface infinite-domain dispersion, original compressible McNally inputs, late roll-up or RT turbulence claim. Figures explicitly normalize computed perturbations by epsilon.

#### RT initial growth in smooth Boussinesq double layers

Freeze22pytest tests,74case gates and10nonlinear evolutions. QualifyK24/40/56references; separately check three-grid field errors/orders, five-time growth,64²halved-step/halved-amplitude probes, Poisson residual, divergence and means.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/rt-initial-growth/?lang=en)

### Numerical methods

Advance point-sampled perturbations using centered shared-face conservative fluxes and Heun; invert the five-point Poisson symbol by FFT. Centered derivatives define divergence-free velocity. Analytic base subtraction avoids a discretization imbalance larger than the small perturbation.

- [Centered spatial difference](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Heun / SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [RT initial growth in smooth Boussinesq double layers](https://hrkoyama.github.io/numerical-methods-atlas/validation/rt-initial-growth/?lang=en)

Supplementary execution example

Advance the actual2D Boussinesq vorticity/active-buoyancy system and compare smooth unstable-layer growth with a separately derived linear IVP.

Periodic[0,2pi]², layer width.25, nu=kappa=.005, epsilon1e-5 and32²/64²/128² grids. Explicit forcing maintains the base. g1,b0=.02tanh(sin y/delta),rho/rho0=1-b/g,T2. Density enters buoyancy only; this is not variable-density Euler.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/atlas-instability-growth-2026-11-23-r2.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

Small-amplitude fixed educational cases. The independent reference changes spatial representation but linearizes the PDE; it is not a second nonlinear engine. No sharp-interface infinite-domain dispersion, original compressible McNally inputs, late roll-up or RT turbulence claim. Figures explicitly normalize computed perturbations by epsilon.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-23-r2/instability-growth/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/run.py)
- [/code/validated-examples/2026-11-23-r2/instability-growth/flow.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/flow.py)
- [/code/validated-examples/2026-11-23-r2/instability-growth/references/linear.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/references/linear.py)
- [/code/validated-examples/2026-11-23-r2/instability-growth/test_instability.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/test_instability.py)
