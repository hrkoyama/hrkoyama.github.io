# Lorentz分散板へのs/p斜め入射 / Oblique s/p incidence on a Lorentz-dispersive slab

https://hrkoyama.github.io/numerical-methods-atlas/problems/lorentz-oblique-sp/

## 日本語

[保存したp偏光の実電場をky=4の周期y方向へ再構成した場。 周期y方向の1周期を表示しています。波形を見やすくするため、x軸とy軸の表示縮尺は異なります。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/results/lorentz-oblique-sp-preview.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-maxwell-lorentz/#lorentz-oblique-sp) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#lorentz-oblique-sp)

### 方程式・問題の定義

周期y方向のky=4に制限した2D場、c=1。板[4,5]のε∞=1.5、Δε=0.75、ω0=9、γ=0.5、σ=0.04。外側は真空、PEC端は[-24,36]、T=60です。

#### [受動Lorentz・Ohmic分散Maxwell場](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#maxwell-lorentz-ja)

$$
\partial_t\mathbf H=-\nabla\times\mathbf E,\quad\varepsilon_\infty\partial_t\mathbf E=\nabla\times\mathbf H-\sigma\mathbf E-\mathbf J
$$

$$
\partial_t\mathbf P=\mathbf J,\quad\partial_t\mathbf J=f\mathbf E-\omega_0^2\mathbf P-\gamma\mathbf J,\quad f=\Delta\varepsilon\omega_0^2
$$

$$
\varepsilon_\infty>0,\quad f,\sigma,\gamma\ge0
$$

正の物質エネルギーと直接Ohmic/γ仕事を持つ単一受動Lorentz極。代表式は3Dですが、実装は周期y単一kyの2D s/p成分制限です。PML数値仕事は物理散逸と同一視しません。

#### Lorentz分散板へのs/p斜め入射

補助実行例 · 実行例の定義・検証式

$$
\varepsilon_\infty\partial_t\mathbf E=\nabla\times\mathbf H-\sigma\mathbf E-\mathbf J,\quad\partial_t\mathbf P=\mathbf J
$$

$$
\partial_t\mathbf J=f\mathbf E-\omega_0^2\mathbf P-\gamma\mathbf J,\quad f=\Delta\varepsilon\omega_0^2
$$

$$
\varepsilon(\omega)=\varepsilon_\infty+\frac{f}{\omega_0^2-\omega^2-i\gamma\omega}+\frac{i\sigma}{\omega}
$$

有限波束の実進行から複素r/t・R/T・直接散逸を求め、複素Fresnel参照と比較します。

### 厳密解・参照解

s/p各3解像度の物質・真空12進行からω=5.1/6/6.9を測定。独立な有限窓の真空幾何級数、複素Fresnel係数、直接体積散逸、全stepのPEC収支と末尾を検査します。

#### [斜め入射の複素Fresnel係数とLorentz板の直接散逸](https://hrkoyama.github.io/numerical-methods-atlas/validation/lorentz-oblique-sp/?lang=ja#lorentz-oblique-sp-ja-measurements)

解析解 · 同じ問題の参照

\varepsilon(\omega)=\varepsilon_\infty+f/(\omega_0^2-\omega^2-i\gamma\omega)+i\sigma/\omega

外側真空、ky=4、板[4,5]、ε∞=1.5、Δε=0.75、ω0=9、γ=0.5、σ=0.04。s=Ezとp=Hzをω=5.1/6/6.9で比較します。

任意の横方向分布ではなく単一kyの実空間制限です。1つの受動Lorentz極と有限帯域・有限窓のみ。Gaussian尾は厳密には非零で、窓診断と参照誤差を別記します。 全周波数で厳密にcap反射が未到達という証明ではありません。

#### Lorentz分散板へのs/p斜め入射

s/p各3解像度の物質・真空12進行からω=5.1/6/6.9を測定。独立な有限窓の真空幾何級数、複素Fresnel係数、直接体積散逸、全stepのPEC収支と末尾を検査します。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/lorentz-oblique-sp/?lang=ja)

### 計算法

単一ky Yee空間演算と局所の陰的中点Lorentz ADE。p偏光の両電場に分極を結合し、同格子の真空波束で入射・伝播位相を除きます。直接Ohmic・物質減衰仕事と修正エネルギーを別々に集計します。

- [Yee FDTD](https://hrkoyama.github.io/numerical-methods-atlas/methods/fdtd/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [2ステップleapfrog法](https://hrkoyama.github.io/numerical-methods-atlas/methods/leapfrog/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [陰的中点則](https://hrkoyama.github.io/numerical-methods-atlas/methods/implicit-midpoint/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [Lorentz分散板へのs/p斜め入射](https://hrkoyama.github.io/numerical-methods-atlas/validation/lorentz-oblique-sp/?lang=ja)

補助実行例

有限波束の実進行から複素r/t・R/T・直接散逸を求め、複素Fresnel参照と比較します。

周期y方向のky=4に制限した2D場、c=1。板[4,5]のε∞=1.5、Δε=0.75、ω0=9、γ=0.5、σ=0.04。外側は真空、PEC端は[-24,36]、T=60です。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/atlas-maxwell-lorentz-2026-11-24-r2.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

任意の横方向分布ではなく単一kyの実空間制限です。1つの受動Lorentz極と有限帯域・有限窓のみ。Gaussian尾は厳密には非零で、窓診断と参照誤差を別記します。 全周波数で厳密にcap反射が未到達という証明ではありません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-24-r2/maxwell-lorentz/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/run.py)
- [/code/validated-examples/2026-11-24-r2/maxwell-lorentz/test_lorentz.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/test_lorentz.py)

## English

[Actual saved p-polarized electric field reconstructed over the periodic y direction at ky=4. One transverse y period is shown. The displayed x and y scales differ to make the fields visible.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/results/lorentz-oblique-sp-preview.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-maxwell-lorentz/#lorentz-oblique-sp) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#lorentz-oblique-sp-en)

### Equations and problem definitions

Use a two-dimensional field restricted to periodic transverse wave number ky = 4 and c = 1. The slab [4, 5] has epsilon_inf = 1.5, delta_epsilon = 0.75, omega_0 = 9, gamma = 0.5 and sigma = 0.04. Outer vacuum ends at PEC caps [-24, 36]; T = 60.

#### [Passive Lorentz–Ohmic Maxwell fields](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#maxwell-lorentz-en)

$$
\partial_t\mathbf H=-\nabla\times\mathbf E,\quad\varepsilon_\infty\partial_t\mathbf E=\nabla\times\mathbf H-\sigma\mathbf E-\mathbf J
$$

$$
\partial_t\mathbf P=\mathbf J,\quad\partial_t\mathbf J=f\mathbf E-\omega_0^2\mathbf P-\gamma\mathbf J,\quad f=\Delta\varepsilon\omega_0^2
$$

$$
\varepsilon_\infty>0,\quad f,\sigma,\gamma\ge0
$$

A single passive Lorentz pole with positive material energy and direct Ohmic/gamma work. The representative equations are three-dimensional; the implemented solver is the two-dimensional s/p component restriction at one periodic ky. Numerical PML work is not identified with physical dissipation.

#### Oblique s/p incidence on a Lorentz-dispersive slab

Supplementary execution example · Example definition or validation formula

$$
\varepsilon_\infty\partial_t\mathbf E=\nabla\times\mathbf H-\sigma\mathbf E-\mathbf J,\quad\partial_t\mathbf P=\mathbf J
$$

$$
\partial_t\mathbf J=f\mathbf E-\omega_0^2\mathbf P-\gamma\mathbf J,\quad f=\Delta\varepsilon\omega_0^2
$$

$$
\varepsilon(\omega)=\varepsilon_\infty+\frac{f}{\omega_0^2-\omega^2-i\gamma\omega}+\frac{i\sigma}{\omega}
$$

Measure complex r/t, power fractions and direct dissipation from actual finite-pulse evolutions and compare them with complex Fresnel slab references.

### Exact and reference solutions

Measure omega = 5.1/6/6.9 from 12 actual material/vacuum evolutions across three resolutions and both polarizations. Check an independent finite-window vacuum geometric sum, complex Fresnel coefficients, direct volume dissipation, all-step PEC budgets and final monitor tails.

#### [Complex oblique Fresnel coefficients and direct Lorentz-slab loss](https://hrkoyama.github.io/numerical-methods-atlas/validation/lorentz-oblique-sp/?lang=en#lorentz-oblique-sp-en-measurements)

Analytic reference · Reference for the same problem

\varepsilon(\omega)=\varepsilon_\infty+f/(\omega_0^2-\omega^2-i\gamma\omega)+i\sigma/\omega

Vacuum surroundings, ky = 4, slab [4, 5], epsilon_inf = 1.5, delta_epsilon = 0.75, omega_0 = 9, gamma = 0.5 and sigma = 0.04. Compare omega = 5.1/6/6.9 for both s = Ez and p = Hz.

This is a genuine single-ky restriction rather than arbitrary transverse data. It covers one passive Lorentz pole and a fixed finite band/window. Gaussian tails are nonzero; window diagnostics and reference errors are reported separately. No strict all-frequency no-return proof is claimed.

#### Oblique s/p incidence on a Lorentz-dispersive slab

Measure omega = 5.1/6/6.9 from 12 actual material/vacuum evolutions across three resolutions and both polarizations. Check an independent finite-window vacuum geometric sum, complex Fresnel coefficients, direct volume dissipation, all-step PEC budgets and final monitor tails.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/lorentz-oblique-sp/?lang=en)

### Numerical methods

Use the single-ky Yee spatial operator and local implicit-midpoint Lorentz ADE. Couple both p-polarized electric components to polarization, and remove incident propagation with a matched vacuum pulse on the same grid. Accumulate direct Ohmic and material-damping work separately from modified energy.

- [Yee finite-difference time-domain method](https://hrkoyama.github.io/numerical-methods-atlas/methods/fdtd/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Two-step leapfrog](https://hrkoyama.github.io/numerical-methods-atlas/methods/leapfrog/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Implicit midpoint](https://hrkoyama.github.io/numerical-methods-atlas/methods/implicit-midpoint/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Oblique s/p incidence on a Lorentz-dispersive slab](https://hrkoyama.github.io/numerical-methods-atlas/validation/lorentz-oblique-sp/?lang=en)

Supplementary execution example

Measure complex r/t, power fractions and direct dissipation from actual finite-pulse evolutions and compare them with complex Fresnel slab references.

Use a two-dimensional field restricted to periodic transverse wave number ky = 4 and c = 1. The slab [4, 5] has epsilon_inf = 1.5, delta_epsilon = 0.75, omega_0 = 9, gamma = 0.5 and sigma = 0.04. Outer vacuum ends at PEC caps [-24, 36]; T = 60.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/atlas-maxwell-lorentz-2026-11-24-r2.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This is a genuine single-ky restriction rather than arbitrary transverse data. It covers one passive Lorentz pole and a fixed finite band/window. Gaussian tails are nonzero; window diagnostics and reference errors are reported separately. No strict all-frequency no-return proof is claimed.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-24-r2/maxwell-lorentz/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/run.py)
- [/code/validated-examples/2026-11-24-r2/maxwell-lorentz/test_lorentz.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/test_lorentz.py)
