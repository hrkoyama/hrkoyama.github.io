# KHの初期成長：滑らかな周期せん断層 / KH initial growth in a smooth periodic shear layer

https://hrkoyama.github.io/numerical-methods-atlas/problems/kh-initial-growth/

## 日本語

[保存した2D摂動渦度をεで規格化。色の尺度を明記し、線形参照と成長を比較します。](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/results/kh-initial-growth-preview.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-instability-growth/#kh-initial-growth) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#kh-initial-growth)

### 方程式・問題の定義

[0,2π]²周期、層厚δ=.25、ν=κ=.005、摂動ε=1e−5。32²/64²/128²格子。基底層は明示した外力で定常維持します。U=tanh(sin y/δ)、T=1。

#### [維持されたせん断層の強制渦度系](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#forced-vorticity-ja)

$$
-\Delta\psi=\omega,\qquad (u,v)=(\psi_y,-\psi_x)
$$

$$
\omega_t+U(y)\omega_x+U^{\prime\prime}(y)\psi_x+u\omega_x+v\omega_y=\nu\Delta\omega
$$

$$
U(y)=\tanh(\sin y/\delta),\qquad \Omega_{\mathrm{total}}=-U^{\prime}(y)+\omega
$$

解析的な基底せん断を明示的外力で維持し、微小摂動を実際の非線形2D渦度系で進めます。圧力は消去され、鋭い界面・無限領域・可圧縮KHの分散式とは区別します。

#### KHの初期成長：滑らかな周期せん断層

補助実行例 · 実行例の定義・検証式

$$
-\Delta\psi=\omega,\qquad (u,v)=(\partial_y\psi,-\partial_x\psi)
$$

$$
U(y)=\tanh(\sin y/\delta),\quad \omega_t+U\omega_x+U^{\prime\prime}\psi_x+\mathbf{u}\cdot\nabla\omega=\nu\Delta\omega
$$

$$
\sigma_T=\frac{1}{T}\log\frac{A(T)}{A(0)},\qquad \dot{\widehat{\mathbf{q}}}=L_K\widehat{\mathbf{q}}
$$

実際の非線形2D渦度方程式を解き、独立Fourier–Galerkin線形初期値問題と有限時間の成長・格子誤差を比較します。

### 厳密解・参照解

群全体22単体検査・74固定判定、10回の非線形計算を事前固定。参照K24/40/56、3格子の場誤差と次数、5保存時刻の成長、64²で刻み半減・振幅半減、Poisson残差・発散・平均値を別々に検査します。

#### [KH初期成長：独立した線形Fourier–Galerkin参照](https://hrkoyama.github.io/numerical-methods-atlas/validation/kh-initial-growth/?lang=ja#kh-initial-growth-ja-measurements)

有限格子の数値参照 · 同じ問題の参照

U=tanh(sin(y)/delta); omega_t=-U*omega_x-Uyy*psi_x+nu*Delta(omega); -Delta(psi)=omega; qhat(t)=exp(t*L_K)qhat(0).

[0,2π]²周期、層厚δ=.25、ν=κ=.005、摂動ε=1e−5。32²/64²/128²格子。基底層は明示した外力で定常維持します。U=tanh(sin y/δ)、T=1。主計算は非線形2次元の点サンプルで、参照はkx=1の連続線形化IVPです。K24/40/56の切断を比較し、基底の微分は独立Fourier係数から評価します。鋭い界面の分散式を流用しません。

線形範囲の教育用固定入力です。線形参照は独立した空間表現であり、独立非線形PDEエンジンではありません。鋭い無限領域界面の分散式、McNallyの可圧縮入力、非線形後期の巻上がりやRT乱流を再現したとは表示しません。図の摂動はεで規格化した実計算値です。

#### KHの初期成長：滑らかな周期せん断層

群全体22単体検査・74固定判定、10回の非線形計算を事前固定。参照K24/40/56、3格子の場誤差と次数、5保存時刻の成長、64²で刻み半減・振幅半減、Poisson残差・発散・平均値を別々に検査します。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/kh-initial-growth/?lang=ja)

### 計算法

点値の渦度・浮力摂動を共有面の中央流束とHeun法で進め、5点差分PoissonをFFTで解きます。u=ψy,v=−ψxなので中央差分発散は整合します。基底場を解析的に差し引き、層そのものの離散ドリフトと微小摂動を分離します。

- [空間中心差分](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [Heun法／SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [KHの初期成長：滑らかな周期せん断層](https://hrkoyama.github.io/numerical-methods-atlas/validation/kh-initial-growth/?lang=ja)

補助実行例

実際の非線形2D渦度方程式を解き、独立Fourier–Galerkin線形初期値問題と有限時間の成長・格子誤差を比較します。

[0,2π]²周期、層厚δ=.25、ν=κ=.005、摂動ε=1e−5。32²/64²/128²格子。基底層は明示した外力で定常維持します。U=tanh(sin y/δ)、T=1。

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

[Saved actual2D perturbation vorticity normalized by epsilon; color scale and linear-reference growth are explicit.](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/results/kh-initial-growth-preview.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-instability-growth/#kh-initial-growth) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#kh-initial-growth-en)

### Equations and problem definitions

Periodic[0,2pi]², layer width.25, nu=kappa=.005, epsilon1e-5 and32²/64²/128² grids. Explicit forcing maintains the base. U=tanh(sin y/delta),T1.

#### [Forced vorticity about a maintained shear layer](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#forced-vorticity-en)

$$
-\Delta\psi=\omega,\qquad (u,v)=(\psi_y,-\psi_x)
$$

$$
\omega_t+U(y)\omega_x+U^{\prime\prime}(y)\psi_x+u\omega_x+v\omega_y=\nu\Delta\omega
$$

$$
U(y)=\tanh(\sin y/\delta),\qquad \Omega_{\mathrm{total}}=-U^{\prime}(y)+\omega
$$

Explicit forcing maintains the analytic base shear; actual nonlinear2D dynamics evolve its perturbations. Pressure is eliminated. Distinguish this from sharp-interface infinite-domain or compressible KH dispersion.

#### KH initial growth in a smooth periodic shear layer

Supplementary execution example · Example definition or validation formula

$$
-\Delta\psi=\omega,\qquad (u,v)=(\partial_y\psi,-\partial_x\psi)
$$

$$
U(y)=\tanh(\sin y/\delta),\quad \omega_t+U\omega_x+U^{\prime\prime}\psi_x+\mathbf{u}\cdot\nabla\omega=\nu\Delta\omega
$$

$$
\sigma_T=\frac{1}{T}\log\frac{A(T)}{A(0)},\qquad \dot{\widehat{\mathbf{q}}}=L_K\widehat{\mathbf{q}}
$$

Evolve the actual nonlinear2D vorticity PDE and compare finite-time growth and spatial errors with an independent continuous Fourier–Galerkin linear IVP.

### Exact and reference solutions

Freeze22pytest tests,74case gates and10nonlinear evolutions. QualifyK24/40/56references; separately check three-grid field errors/orders, five-time growth,64²halved-step/halved-amplitude probes, Poisson residual, divergence and means.

#### [KH initial growth: independent linear Fourier-Galerkin reference](https://hrkoyama.github.io/numerical-methods-atlas/validation/kh-initial-growth/?lang=en#kh-initial-growth-en-measurements)

Finite-grid numerical reference · Reference for the same problem

U=tanh(sin(y)/delta); omega_t=-U*omega_x-Uyy*psi_x+nu*Delta(omega); -Delta(psi)=omega; qhat(t)=exp(t*L_K)qhat(0).

Periodic[0,2pi]², layer width.25, nu=kappa=.005, epsilon1e-5 and32²/64²/128² grids. Explicit forcing maintains the base. U=tanh(sin y/delta),T1. The nonlinear primary evolves actual2D point samples. The reference solves the continuous linearized IVP at kx1 with truncationsK24/40/56 and independently Fourier-differentiated base profiles; it does not substitute a sharp-interface dispersion formula.

Small-amplitude fixed educational cases. The independent reference changes spatial representation but linearizes the PDE; it is not a second nonlinear engine. No sharp-interface infinite-domain dispersion, original compressible McNally inputs, late roll-up or RT turbulence claim. Figures explicitly normalize computed perturbations by epsilon.

#### KH initial growth in a smooth periodic shear layer

Freeze22pytest tests,74case gates and10nonlinear evolutions. QualifyK24/40/56references; separately check three-grid field errors/orders, five-time growth,64²halved-step/halved-amplitude probes, Poisson residual, divergence and means.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/instability-growth/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/kh-initial-growth/?lang=en)

### Numerical methods

Advance point-sampled perturbations using centered shared-face conservative fluxes and Heun; invert the five-point Poisson symbol by FFT. Centered derivatives define divergence-free velocity. Analytic base subtraction avoids a discretization imbalance larger than the small perturbation.

- [Centered spatial difference](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Heun / SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [KH initial growth in a smooth periodic shear layer](https://hrkoyama.github.io/numerical-methods-atlas/validation/kh-initial-growth/?lang=en)

Supplementary execution example

Evolve the actual nonlinear2D vorticity PDE and compare finite-time growth and spatial errors with an independent continuous Fourier–Galerkin linear IVP.

Periodic[0,2pi]², layer width.25, nu=kappa=.005, epsilon1e-5 and32²/64²/128² grids. Explicit forcing maintains the base. U=tanh(sin y/delta),T1.

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
