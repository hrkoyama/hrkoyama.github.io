# 2D誘電体円柱のMie散乱幅 / Mie scattering width of a two-dimensional dielectric cylinder

https://hrkoyama.github.io/numerical-methods-atlas/problems/cylinder-mie2d/

## 日本語

[保存した最細格子の実2D散乱電場phasorの実部。 図の中央の白抜きは診断用のr<0.4のマスクで、物理円柱の半径0.25とは区別します。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-cylinder/results/cylinder-mie2d-preview.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-maxwell-cylinder/#cylinder-mie2d) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#cylinder-mie2d)

### 方程式・問題の定義

c=ε0=μ0=1。無限円柱のEz偏光、半径0.25、比誘電率2.25、真空波長1。6×6領域と4辺PML、明示的な節点階段状形状です。

#### [線形Maxwell電磁場（真空・誘電体）](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#maxwell-ja)

$$
\partial_t\mathbf B=-\nabla\times\mathbf E,\quad\partial_t\mathbf D=\nabla\times\mathbf H
$$

$$
\mathbf D=\varepsilon(\mathbf x)\mathbf E,\quad\mathbf B=\mathbf H
$$

代表式は3D線形電磁場です。今回の実装はz不変の円柱Ez/Hx/Hyに制限した真2D Yee計算です。

#### 2D誘電体円柱のMie散乱幅

補助実行例 · 実行例の定義・検証式

$$
\varepsilon\partial_tE_z=\partial_xH_y-\partial_yH_x,\quad\partial_tH_x=-\partial_yE_z,\quad\partial_tH_y=\partial_xE_z
$$

$$
\Sigma_{\mathrm{sca}}=\frac4k\sum_{n=-\infty}^{\infty}|a_n|^2,\quad\Sigma_{\mathrm{ext}}=-\frac4k\sum_n\operatorname{Re}a_n
$$

実際の2D散乱場を進め、閉曲線Poynting流束と独立な円柱級数を比較します。

### 厳密解・参照解

12/18/24点/波長、32周期の過渡除去と8周期の計測。2本の閉曲線、前後4周期、同じ全時間を進めた半振幅phasorと5保存時刻の真空対照を検査し、円柱級数の散乱幅と外部場を照合します。

#### [誘電体円柱の外部級数と散乱幅](https://hrkoyama.github.io/numerical-methods-atlas/validation/cylinder-mie2d/?lang=ja#cylinder-mie2d-ja-measurements)

解析解 · 同じ問題の参照

E_z^{\mathrm{sca}}=\sum_n i^n a_nH_n^{(1)}(kr)e^{in\theta},\quad\Sigma_{\mathrm{sca}}=4\sum_n|a_n|^2/k

無損失無限円柱、Ez偏光、c=ε0=μ0=1、半径0.25、ε=2.25、真空波長1。解析場は厳密な円の外部だけです。

Ezの無損失2D円柱のみで、3D球ではありません。階段状形状の誤差を記録し、一般の曲面2次精度や任意周波数・材料での精密散乱を保証しません。

#### 2D誘電体円柱のMie散乱幅

12/18/24点/波長、32周期の過渡除去と8周期の計測。2本の閉曲線、前後4周期、同じ全時間を進めた半振幅phasorと5保存時刻の真空対照を検査し、円柱級数の散乱幅と外部場を照合します。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-cylinder/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/cylinder-mie2d/?lang=ja)

### 計算法

Yeeの散乱場を局所分極contrastの厳密な離散入射差分で励起します。EとHはそれぞれの整数・半時刻でFourier集計し、Hの4点補間後に物理流束を積分します。

- [Yee FDTD](https://hrkoyama.github.io/numerical-methods-atlas/methods/fdtd/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [2ステップleapfrog法](https://hrkoyama.github.io/numerical-methods-atlas/methods/leapfrog/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [2D誘電体円柱のMie散乱幅](https://hrkoyama.github.io/numerical-methods-atlas/validation/cylinder-mie2d/?lang=ja)

補助実行例

実際の2D散乱場を進め、閉曲線Poynting流束と独立な円柱級数を比較します。

c=ε0=μ0=1。無限円柱のEz偏光、半径0.25、比誘電率2.25、真空波長1。6×6領域と4辺PML、明示的な節点階段状形状です。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-cylinder/atlas-maxwell-cylinder-2026-11-24-r2.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-cylinder/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-cylinder/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-cylinder/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

Ezの無損失2D円柱のみで、3D球ではありません。階段状形状の誤差を記録し、一般の曲面2次精度や任意周波数・材料での精密散乱を保証しません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-24-r2/maxwell-cylinder/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-cylinder/run.py)
- [/code/validated-examples/2026-11-24-r2/maxwell-cylinder/test_cylinder.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-cylinder/test_cylinder.py)

## English

[Real part of the actual saved scattered electric phasor on the finest two-dimensional grid. The central white region is a diagnostic mask at r<0.4, distinct from the physical cylinder radius0.25.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-cylinder/results/cylinder-mie2d-preview.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-maxwell-cylinder/#cylinder-mie2d) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#cylinder-mie2d-en)

### Equations and problem definitions

Use c = epsilon0 = mu0 = 1, an infinite cylinder with Ez polarization, radius 0.25, relative permittivity 2.25 and vacuum wavelength 1. The 6 × 6 domain has four-side PML and an explicitly nodal staircase geometry.

#### [Linear Maxwell fields in vacuum and dielectrics](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#maxwell-en)

$$
\partial_t\mathbf B=-\nabla\times\mathbf E,\quad\partial_t\mathbf D=\nabla\times\mathbf H
$$

$$
\mathbf D=\varepsilon(\mathbf x)\mathbf E,\quad\mathbf B=\mathbf H
$$

The representative equations describe three-dimensional linear electromagnetics. This implementation is restricted to a z-invariant, genuinely two-dimensional Yee cylinder problem with Ez/Hx/Hy.

#### Mie scattering width of a two-dimensional dielectric cylinder

Supplementary execution example · Example definition or validation formula

$$
\varepsilon\partial_tE_z=\partial_xH_y-\partial_yH_x,\quad\partial_tH_x=-\partial_yE_z,\quad\partial_tH_y=\partial_xE_z
$$

$$
\Sigma_{\mathrm{sca}}=\frac4k\sum_{n=-\infty}^{\infty}|a_n|^2,\quad\Sigma_{\mathrm{ext}}=-\frac4k\sum_n\operatorname{Re}a_n
$$

Evolve the actual two-dimensional scattered fields and compare closed-contour Poynting power with an independent cylindrical series.

### Exact and reference solutions

Use 12/18/24 points per wavelength, 32 burn-in periods and 8 measured periods. Check two contours, consecutive four-period windows, half-amplitude phasors after a complete repeated evolution, and a vacuum control at the five saved times. Compare scattering width and exterior fields with the cylindrical series.

#### [Exterior series and scattering width of a dielectric cylinder](https://hrkoyama.github.io/numerical-methods-atlas/validation/cylinder-mie2d/?lang=en#cylinder-mie2d-en-measurements)

Analytic reference · Reference for the same problem

E_z^{\mathrm{sca}}=\sum_n i^n a_nH_n^{(1)}(kr)e^{in\theta},\quad\Sigma_{\mathrm{sca}}=4\sum_n|a_n|^2/k

Lossless infinite cylinder, Ez polarization, c = epsilon0 = mu0 = 1, radius 0.25, epsilon = 2.25 and vacuum wavelength 1. The analytical field is exterior to the exact circle.

This is a lossless two-dimensional Ez cylinder, not a three-dimensional sphere. Report staircase geometry error without claiming general second-order curved-boundary accuracy or precision scattering for arbitrary frequencies and materials.

#### Mie scattering width of a two-dimensional dielectric cylinder

Use 12/18/24 points per wavelength, 32 burn-in periods and 8 measured periods. Check two contours, consecutive four-period windows, half-amplitude phasors after a complete repeated evolution, and a vacuum control at the five saved times. Compare scattering width and exterior fields with the cylindrical series.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-cylinder/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/cylinder-mie2d/?lang=en)

### Numerical methods

Advance the scattered Yee fields with an exact discrete incident difference on the polarization-contrast support. Accumulate E and H at their own integer and half times, then integrate physical power after four-point native-face collocation.

- [Yee finite-difference time-domain method](https://hrkoyama.github.io/numerical-methods-atlas/methods/fdtd/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Two-step leapfrog](https://hrkoyama.github.io/numerical-methods-atlas/methods/leapfrog/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Mie scattering width of a two-dimensional dielectric cylinder](https://hrkoyama.github.io/numerical-methods-atlas/validation/cylinder-mie2d/?lang=en)

Supplementary execution example

Evolve the actual two-dimensional scattered fields and compare closed-contour Poynting power with an independent cylindrical series.

Use c = epsilon0 = mu0 = 1, an infinite cylinder with Ez polarization, radius 0.25, relative permittivity 2.25 and vacuum wavelength 1. The 6 × 6 domain has four-side PML and an explicitly nodal staircase geometry.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-cylinder/atlas-maxwell-cylinder-2026-11-24-r2.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-cylinder/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-cylinder/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-cylinder/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This is a lossless two-dimensional Ez cylinder, not a three-dimensional sphere. Report staircase geometry error without claiming general second-order curved-boundary accuracy or precision scattering for arbitrary frequencies and materials.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-24-r2/maxwell-cylinder/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-cylinder/run.py)
- [/code/validated-examples/2026-11-24-r2/maxwell-cylinder/test_cylinder.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-cylinder/test_cylinder.py)
