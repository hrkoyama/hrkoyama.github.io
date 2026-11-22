# 周期せん断波の粘性減衰 / Viscous decay of a periodic shear wave

https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-shear/

## 日本語

[保存済みせん断波振幅と粘性減衰の参照値。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/lbm-shear.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/lattice-boltzmann/) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#lbm-shear)

### 方程式・問題の定義

格子BGKが計算モデル、非圧縮Navier–Stokesは低Mach数で比較する巨視的な減衰モデルです。

#### [等温格子BGK](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bgk-ja)

$$
f_q(\boldsymbol x+\boldsymbol c_q,t+1)=f_q(\boldsymbol x,t)-\frac{f_q-f_q^{\rm eq}}{\tau}+S_q
$$

格子単位Δx=Δt=1の衝突・並進更新。D2Q9等温・低Mach数のせん断波とPoiseuille流を扱います。

#### [非圧縮Navier–Stokes](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#navier-stokes-ja)

$$
\partial_t\boldsymbol u+(\boldsymbol u\cdot\nabla)\boldsymbol u=-\rho^{-1}\nabla p+\nu\nabla^2\boldsymbol u
$$

$$
\nabla\cdot\boldsymbol u=0
$$

一定密度・粘性の代表形。公開例は周期2次元MAC格子の射影法とTaylor–Green渦です。

### 厳密解・参照解

低Mach数の周期せん断波について、粘性Fourier減衰から測定した粘性と収束を確認します。熱方程式の参照カードは同型の減衰の関連例です。

#### [熱拡散／Fourierモードの減衰](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=sine-heat)

解析解 · 関連モデルの参照

u = 1 + 0.25 sin(2πx) exp[−0.02(2π)²t]

単位区間の周期境界、拡散係数0.02。

周期せん断速度の線形粘性減衰とスカラー熱モードは同型ですが、LBMの格子単位・波数・粘性と参照カードのν=0.02は異なります。

### 計算法

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

- [D2Q9–BGK衝突・並進](https://hrkoyama.github.io/numerical-methods-atlas/methods/d2q9-bgk/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

この問題の固定入力実行例は未登録です。保存結果と解説は上のリンクから確認できます。

#### [code/numerical-methods-atlas/2026-11-21/tests/test_new_models.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_new_models.py)

関連する既存のソース・検査。固定入力実行例とは別です。

`test_lbm_shear_viscosity_refines`

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

作業フォルダ：atlas-code-2026-11-21/

```sh
python -m pytest -q tests/test_new_models.py -k test_lbm_shear_viscosity_refines
```

## English

[Stored shear amplitudes and viscous-decay reference.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/lbm-shear.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/lattice-boltzmann/) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#lbm-shear-en)

### Equations and problem definitions

Lattice BGK is the computed model; incompressible Navier–Stokes supplies the low-Mach macroscopic decay comparison.

#### [Isothermal lattice BGK](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bgk-en)

$$
f_q(\boldsymbol x+\boldsymbol c_q,t+1)=f_q(\boldsymbol x,t)-\frac{f_q-f_q^{\rm eq}}{\tau}+S_q
$$

Collision/streaming in lattice units Δx=Δt=1. Examples cover D2Q9 isothermal low-Mach shear waves and Poiseuille flow.

#### [Incompressible Navier–Stokes](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#navier-stokes-en)

$$
\partial_t\boldsymbol u+(\boldsymbol u\cdot\nabla)\boldsymbol u=-\rho^{-1}\nabla p+\nu\nabla^2\boldsymbol u
$$

$$
\nabla\cdot\boldsymbol u=0
$$

A representative constant-density, constant-viscosity form. Public examples use periodic 2D MAC projection and a Taylor–Green vortex.

### Exact and reference solutions

For a low-Mach periodic shear wave, infer viscosity from Fourier decay and check refinement. The heat reference card is a related scalar decay model.

#### [Heat / Fourier-mode decay](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=sine-heat)

Analytic reference · Related-model reference

u = 1 + 0.25 sin(2πx) exp[−0.02(2π)²t]

Periodic unit interval; viscosity 0.02.

Linear viscous shear decay and scalar heat modes have the same form, but LBM lattice units, wavenumber and viscosity differ from the card’s ν=0.02.

### Numerical methods

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

- [D2Q9–BGK collision and streaming](https://hrkoyama.github.io/numerical-methods-atlas/methods/d2q9-bgk/?lang=en) — Related explanation; Method-registry status: Educational example / related code

### Code and execution

No fixed-input execution example is registered for this problem. The saved visual and reading remain available above.

#### [code/numerical-methods-atlas/2026-11-21/tests/test_new_models.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_new_models.py)

Existing related source/check, separate from a registered fixed-input execution example.

`test_lbm_shear_viscosity_refines`

[Corresponding code edition / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

Working directory: atlas-code-2026-11-21/

```sh
python -m pytest -q tests/test_new_models.py -k test_lbm_shear_viscosity_refines
```
