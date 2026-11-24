# 周期Fourierモードの熱拡散 / Periodic Fourier-mode heat decay

https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-periodic/

## 日本語

[保存した最終時刻の数値波形と参照解。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/heat-periodic.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/elliptic/) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#heat-periodic)

### 方程式・問題の定義

周期区間[0,2π)、uₜ=νuₓₓ、T=0.25。同じ関数の点を分散させず、全46問題を学習24・検証6・未見ID8・νのOOD4・周波数のOOD4に分けます。2固定seed、93実パラメータです。

#### [熱・拡散方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#heat-ja)

$$
\partial_tu=\nu\nabla^2u
$$

一定拡散係数νの代表形。モードの減衰、時間積分、境界条件へ。

#### 小型FNOの問題単位検証

補助実行例 · 実行例の定義・検証式

$$
u_t=\nu u_{xx},\quad x\in[0,2\pi),\quad u(x+2\pi,t)=u(x,t),\quad T=\tfrac14
$$

$$
\widehat u_k(T)=e^{-\nu k^2T}\widehat u_k(0)
$$

$$
v^{\ell+1}=\tanh\!\left(W_\ell v^\ell+b_\ell+\mathcal F_N^{-1}(R_\ell\mathcal F_Nv^\ell)\right),\quad \ell=0,1
$$

$$
\mathrm{relative\ error}=\frac{\operatorname{RMS}(u_\theta-u_{\rm ref})}{\operatorname{RMS}(u_{\rm ref})}\quad\text{only if }\operatorname{RMS}(u_{\rm ref})>10^{-12}
$$

同じ重みで32/64点・未見関数・OODを分けて評価します。

### 厳密解・参照解

周期区間の単一Fourierモードの指数減衰が解析基準です。保存図の振幅0.25・粘性0.02の条件を、別周波数のコード検査と区別します。 全93実座標の損失勾配を2つの固定差分幅で照合し、Fourierブロックを直接DFTと比較。解析的な熱モード減衰に対する絶対・相対誤差、格子制限差、ID/OODを分離します。参照RMS≤10⁻¹²では相対誤差をNAとし、ゼロ・微小振幅では絶対誤差を保存します。

#### [熱拡散／Fourierモードの減衰](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=sine-heat)

解析解 · 関連モデルの参照

u = 1 + 0.25 sin(2πx) exp[−0.02(2π)²t]

単位区間の周期境界、拡散係数0.02。

保存ギャラリーの周期[0,1]、1+0.25sin(2πx)、ν=0.02、最終時刻1が一致します。別周波数のコード検査への一致は意味しません。 物理的な入力は一致しますが、参照カードの点値標本と保存計算の有限体積セル平均・離散格子は別表現です。

#### [小型FNOの問題単位検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/fno-periodic-heat/?lang=ja#fno-periodic-heat-ja-measurements)

解析解 · 関連モデルの参照

u_t=\nu u_{xx},\quad x\in[0,2\pi),\quad u(x+2\pi,t)=u(x,t),\quad T=\tfrac14;\quad \widehat u_k(T)=e^{-\nu k^2T}\widehat u_k(0);\quad v^{\ell+1}=\tanh\!\left(W_\ell v^\ell+b_\ell+\mathcal F_N^{-1}(R_\ell\mathcal F_Nv^\ell)\right),\quad \ell=0,1;\quad \mathrm{relative\ error}=\frac{\operatorname{RMS}(u_\theta-u_{\rm ref})}{\operatorname{RMS}(u_{\rm ref})}\quad\text{only if }\operatorname{RMS}(u_{\rm ref})>10^{-12}

周期区間[0,2π)、uₜ=νuₓₓ、T=0.25。同じ関数の点を分散させず、全46問題を学習24・検証6・未見ID8・νのOOD4・周波数のOOD4に分けます。2固定seed、93実パラメータです。

固定された小型離散作用素の比較で、任意の解像度・分布に対する一般化やOOD精度を保証しません。N=64から32への差には非線形aliasingが含まれ、連続体離散化誤差とは呼びません。最適化収束と固定予算終了は別です。

#### 小型FNOの問題単位検証

全93実座標の損失勾配を2つの固定差分幅で照合し、Fourierブロックを直接DFTと比較。解析的な熱モード減衰に対する絶対・相対誤差、格子制限差、ID/OODを分離します。参照RMS≤10⁻¹²では相対誤差をNAとし、ゼロ・微小振幅では絶対誤差を保存します。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/fno-periodic-heat/?lang=ja)

### 計算法

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。 入力(u₀,ν)を幅2へ写し、局所線形項・DCと1–4モードの複素Fourier項・tanhからなる2ブロックを適用します。L-BFGS-Bの固定予算で学習し、同じ重みをN=32/64へ転送。非線形項は各格子上で評価しdealiasingしません。

- [空間中心差分](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり
- [前進Euler法](https://hrkoyama.github.io/numerical-methods-atlas/methods/forward-euler/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり
- [PINN・ニューラル演算子](https://hrkoyama.github.io/numerical-methods-atlas/methods/pinn-operators/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [小型FNOの問題単位検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/fno-periodic-heat/?lang=ja)

補助実行例

同じ重みで32/64点・未見関数・OODを分けて評価します。

周期区間[0,2π)、uₜ=νuₓₓ、T=0.25。同じ関数の点を分散させず、全46問題を学習24・検証6・未見ID8・νのOOD4・周波数のOOD4に分けます。2固定seed、93実パラメータです。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/atlas-small-models-2026-11-25.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

固定された小型離散作用素の比較で、任意の解像度・分布に対する一般化やOOD精度を保証しません。N=64から32への差には非線形aliasingが含まれ、連続体離散化誤差とは呼びません。最適化収束と固定予算終了は別です。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-25/small-models/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/run.py)
- [/code/validated-examples/2026-11-25/small-models/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/experiments.py)
- [/code/validated-examples/2026-11-25/small-models/io_utils.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/io_utils.py)
- [/code/validated-examples/2026-11-25/small-models/fno.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/fno.py)
- [/code/validated-examples/2026-11-25/small-models/data_family.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/data_family.py)
- [/code/validated-examples/2026-11-25/small-models/test_models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/test_models.py)

#### [code/numerical-methods-atlas/2026-11-21/tests/test_linear.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_linear.py)

関連する既存のソース・検査。固定入力実行例とは別です。

`test_spectral_heat_exact_mode_decay`

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

作業フォルダ：atlas-code-2026-11-21/

```sh
python -m pytest -q tests/test_linear.py -k test_spectral_heat_exact_mode_decay
```

## English

[Stored final-time numerical profile and reference.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/heat-periodic.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/elliptic/) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#heat-periodic-en)

### Equations and problem definitions

Use periodic heat flow uₜ=νuₓₓ on [0,2π) to T=0.25. Split 46 whole problems into 24 training, 6 validation, 8 held-out ID, 4 viscosity-OOD and 4 spectrum-OOD problems. Use two fixed seeds and 93 real parameters.

#### [Heat / diffusion equation](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#heat-en)

$$
\partial_tu=\nu\nabla^2u
$$

A representative constant-diffusivity form: mode decay, time integration and boundaries.

#### Tiny FNO on held-out heat problems

Supplementary execution example · Example definition or validation formula

$$
u_t=\nu u_{xx},\quad x\in[0,2\pi),\quad u(x+2\pi,t)=u(x,t),\quad T=\tfrac14
$$

$$
\widehat u_k(T)=e^{-\nu k^2T}\widehat u_k(0)
$$

$$
v^{\ell+1}=\tanh\!\left(W_\ell v^\ell+b_\ell+\mathcal F_N^{-1}(R_\ell\mathcal F_Nv^\ell)\right),\quad \ell=0,1
$$

$$
\mathrm{relative\ error}=\frac{\operatorname{RMS}(u_\theta-u_{\rm ref})}{\operatorname{RMS}(u_{\rm ref})}\quad\text{only if }\operatorname{RMS}(u_{\rm ref})>10^{-12}
$$

Evaluate the same learned weights on 32/64-point grids, held-out functions and separate OOD inputs.

### Exact and reference solutions

Analytic exponential decay of a periodic Fourier mode is the standard. Distinguish the saved figure's amplitude 0.25 and viscosity 0.02 from code checks using other frequencies. Qualify all 93 real loss-gradient coordinates at two fixed finite-difference widths and compare Fourier blocks with direct DFT sums. Separate analytic heat-mode errors, grid-restriction differences and ID/OOD diagnostics. Relative error is NA when reference RMS≤10⁻¹²; zero and near-zero controls retain absolute errors.

#### [Heat / Fourier-mode decay](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=sine-heat)

Analytic reference · Related-model reference

u = 1 + 0.25 sin(2πx) exp[−0.02(2π)²t]

Periodic unit interval; viscosity 0.02.

The saved gallery matches periodic [0,1], 1+0.25sin(2πx), ν=0.02 and final time one; this does not assert a match to separate-frequency code checks. Physical inputs match, but the card’s point samples and the saved computation’s finite-volume cell averages/discrete grid are different representations.

#### [Tiny FNO on held-out heat problems](https://hrkoyama.github.io/numerical-methods-atlas/validation/fno-periodic-heat/?lang=en#fno-periodic-heat-en-measurements)

Analytic reference · Related-model reference

u_t=\nu u_{xx},\quad x\in[0,2\pi),\quad u(x+2\pi,t)=u(x,t),\quad T=\tfrac14;\quad \widehat u_k(T)=e^{-\nu k^2T}\widehat u_k(0);\quad v^{\ell+1}=\tanh\!\left(W_\ell v^\ell+b_\ell+\mathcal F_N^{-1}(R_\ell\mathcal F_Nv^\ell)\right),\quad \ell=0,1;\quad \mathrm{relative\ error}=\frac{\operatorname{RMS}(u_\theta-u_{\rm ref})}{\operatorname{RMS}(u_{\rm ref})}\quad\text{only if }\operatorname{RMS}(u_{\rm ref})>10^{-12}

Use periodic heat flow uₜ=νuₓₓ on [0,2π) to T=0.25. Split 46 whole problems into 24 training, 6 validation, 8 held-out ID, 4 viscosity-OOD and 4 spectrum-OOD problems. Use two fixed seeds and 93 real parameters.

This comparison concerns a fixed tiny discrete operator, without arbitrary-resolution, distributional or OOD guarantees. The N=64-to-32 discrepancy includes nonlinear aliasing and is not a continuum discretization error. Optimizer convergence is distinct from normal budget termination.

#### Tiny FNO on held-out heat problems

Qualify all 93 real loss-gradient coordinates at two fixed finite-difference widths and compare Fourier blocks with direct DFT sums. Separate analytic heat-mode errors, grid-restriction differences and ID/OOD diagnostics. Relative error is NA when reference RMS≤10⁻¹²; zero and near-zero controls retain absolute errors.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/fno-periodic-heat/?lang=en)

### Numerical methods

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability. Lift (u₀,ν) to width two and apply two blocks containing a local linear map, real DC and complex Fourier modes 1–4, then tanh. Train with a fixed L-BFGS-B budget and evaluate the same weights at N=32 and 64. Nonlinear terms are evaluated on each native grid without dealiasing.

- [Centered spatial difference](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en) — Related explanation; Method-registry status: Educational example / related code
- [Forward Euler](https://hrkoyama.github.io/numerical-methods-atlas/methods/forward-euler/?lang=en) — Related explanation; Method-registry status: Educational example / related code
- [PINNs and neural operators](https://hrkoyama.github.io/numerical-methods-atlas/methods/pinn-operators/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Tiny FNO on held-out heat problems](https://hrkoyama.github.io/numerical-methods-atlas/validation/fno-periodic-heat/?lang=en)

Supplementary execution example

Evaluate the same learned weights on 32/64-point grids, held-out functions and separate OOD inputs.

Use periodic heat flow uₜ=νuₓₓ on [0,2π) to T=0.25. Split 46 whole problems into 24 training, 6 validation, 8 held-out ID, 4 viscosity-OOD and 4 spectrum-OOD problems. Use two fixed seeds and 93 real parameters.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/atlas-small-models-2026-11-25.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This comparison concerns a fixed tiny discrete operator, without arbitrary-resolution, distributional or OOD guarantees. The N=64-to-32 discrepancy includes nonlinear aliasing and is not a continuum discretization error. Optimizer convergence is distinct from normal budget termination.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-25/small-models/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/run.py)
- [/code/validated-examples/2026-11-25/small-models/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/experiments.py)
- [/code/validated-examples/2026-11-25/small-models/io_utils.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/io_utils.py)
- [/code/validated-examples/2026-11-25/small-models/fno.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/fno.py)
- [/code/validated-examples/2026-11-25/small-models/data_family.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/data_family.py)
- [/code/validated-examples/2026-11-25/small-models/test_models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/test_models.py)

#### [code/numerical-methods-atlas/2026-11-21/tests/test_linear.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_linear.py)

Existing related source/check, separate from a registered fixed-input execution example.

`test_spectral_heat_exact_mode_decay`

[Corresponding code edition / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

Working directory: atlas-code-2026-11-21/

```sh
python -m pytest -q tests/test_linear.py -k test_spectral_heat_exact_mode_decay
```
