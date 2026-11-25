# 一様圧力と線形音波：SPH/GSPHの粒子配置依存

規則・摂動粒子の一様圧力と小振幅音波について、初期カーネル誤差と時間発展誤差を区別する。

**使用手法**

- [Godunov SPH／GSPH](https://hrkoyama.github.io/numerical-methods-atlas/methods/gsph/?lang=ja) (`gsph`)
- [SPHカーネル再構成](https://hrkoyama.github.io/numerical-methods-atlas/methods/sph/?lang=ja) (`sph`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/sph-pressure-acoustics/?lang=ja#sph-pressure-acoustics-ja-algorithm)

固定入力・宣言したアルゴリズム・補正しない停止条件を用います。

- [圧縮性Euler方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#euler-ja) (`euler`)

GSPH、摂動した128粒子、t=0.2。初期カーネル再構成誤差は最大0.011834で、音波振幅0.001より大きく、左の密度分布にその影響が残ります。右は初期誤差です。判定は基本Fourierモードの位相・振幅と保存量などの固定条件であり、点ごとの高精度や一般的な優位性を示しません。


**問題の図**

![一様圧力と線形音波：SPH/GSPHの粒子配置依存：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/sph-pressure-acoustics.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[一様圧力と線形音波：SPH/GSPHの粒子配置依存](https://hrkoyama.github.io/numerical-methods-atlas/problems/sph-pressure-acoustics/?lang=ja) (`sph-pressure-acoustics`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/sph-pressure-acoustics/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/sph-pressure-acoustics/?lang=ja#sph-pressure-acoustics-ja-validation)

解析参照、保存量、細分化、独立成分検査と意図した誤式の負例を区別して保存します。

- [一様圧力と線形音波：SPH/GSPHの粒子配置依存](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-sph-pressure-acoustics-ja) (`sph-pressure-acoustics`; 同じ問題の参照 · 解析参照)

固定入力の式・参照・図と実行コードを対応付けます。 GSPH、摂動した128粒子、t=0.2。初期カーネル再構成誤差は最大0.011834で、音波振幅0.001より大きく、左の密度分布にその影響が残ります。右は初期誤差です。判定は基本Fourierモードの位相・振幅と保存量などの固定条件であり、点ごとの高精度や一般的な優位性を示しません。
## 前提・単位・境界

規則・摂動粒子の一様圧力と小振幅音波について、初期カーネル誤差と時間発展誤差を区別する。 固定入力の条件・境界・参照の範囲はinputs.jsonを参照。

**編集上の補足**

GSPH、摂動した128粒子、t=0.2。初期カーネル再構成誤差は最大0.011834で、音波振幅0.001より大きく、左の密度分布にその影響が残ります。右は初期誤差です。判定は基本Fourierモードの位相・振幅と保存量などの固定条件であり、点ごとの高精度や一般的な優位性を示しません。

## 採用した計算法

固定入力・宣言したアルゴリズム・補正しない停止条件を用います。

$$
\partial_tU+\partial_xF(U)=0
$$

$$
U=(\rho,\rho u,E)^{\mathsf T}
$$

$$
F=(\rho u,\rho u^2+p,u(E+p))^{\mathsf T}
$$

数式の編集補足：凍結配布版のコードと登録済み方程式に基づく記述です。配布版・計算・受入条件・保存結果は変更しません。

## 比較・検証

解析参照、保存量、細分化、独立成分検査と意図した誤式の負例を区別して保存します。

## 確認の限界

限定した教育用モデルです。元論文の全条件・全アルゴリズムや一般的な性能の再現ではありません。

## 保存実測値と判定

```json
{
  "metrics": {
    "profiles": 16,
    "linearization_remainder_scale": 1e-06
  },
  "checks": {
    "regular_static_force": true,
    "jittered_static_velocity": true,
    "acoustic_phase": true,
    "acoustic_amplitude": true,
    "conservation": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/sph-pressure-acoustics/index.json

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/atlas-continuum-particle-controls-2026-11-25.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

## 出典と確認範囲

- Reformulation of Smoothed Particle Hydrodynamics with Riemann Solver. https://arxiv.org/pdf/astro-ph/0206401; review_level=selected-original-author-paper-sections-and-equations
- New Third-Order Finite Volume Unequal-Sized WENO Lagrangian Schemes for Solving Euler Equations. https://www.mdpi.com/2227-7390/11/23/4842; review_level=selected-publisher-fulltext-example-8
- Second Order Corner Coupled Upwind Transport Methods for Lagrangian Hydrodynamics. https://www.osti.gov/servlets/purl/15005665; review_level=secondary-bibliographic-identity-original-report-unread
- A standard test set for numerical approximations to the shallow water equations in spherical geometry. https://digital.library.unt.edu/ark:/67531/metadc1069483/; review_level=author-report-bibliography-and-abstract-original-formulas-unread
- Cascade interpolation for semi-Lagrangian advection over the sphere. https://www.image.ucar.edu/staff/rnair/qj99_sph.pdf; review_level=selected-author-hosted-formulas-and-publisher-bibliography

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Uniform pressure and acoustics: particle-layout effects in SPH/GSPH

Regular/deterministicallyjitteredperiodicparticles, fixedhSPHcontrol vs adaptivehGSPH. Separateinitialkernelerror and fluidupdate, finiteamplitudeO(A²)linearizedreference remainder. No universalGSPHsuperiorityclaim.

**Methods used**

- [Godunov SPH / GSPH](https://hrkoyama.github.io/numerical-methods-atlas/methods/gsph/?lang=en) (`gsph`)
- [SPH kernel reconstruction](https://hrkoyama.github.io/numerical-methods-atlas/methods/sph/?lang=en) (`sph`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/sph-pressure-acoustics/?lang=en#sph-pressure-acoustics-en-algorithm)

Regular/deterministicallyjitteredperiodicparticles, fixedhSPHcontrol vs adaptivehGSPH. Separateinitialkernelerror and fluidupdate, finiteamplitudeO(A²)linearizedreference remainder. No universalGSPHsuperiorityclaim.

- [Compressible Euler equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#euler-en) (`euler`)

GSPH with 128 jittered particles at t=0.2. The initial kernel reconstruction error reaches 0.011834, exceeding the acoustic amplitude 0.001 and remaining visible in the left density profile; the right panel shows that initial error. Acceptance concerns the fundamental Fourier mode phase/amplitude and other fixed conservation controls, not pointwise high accuracy or general superiority.


**Problem figure**

![Uniform pressure and acoustics: particle-layout effects in SPH/GSPH: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/sph-pressure-acoustics.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Uniform pressure and acoustics: particle-layout effects in SPH/GSPH](https://hrkoyama.github.io/numerical-methods-atlas/problems/sph-pressure-acoustics/?lang=en) (`sph-pressure-acoustics`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/sph-pressure-acoustics/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/sph-pressure-acoustics/?lang=en#sph-pressure-acoustics-en-validation)

Separate analytic/reference errors, conservation, refinement, independent component qualification and deliberately wrong-formula controls.

- [Uniform pressure and acoustics: particle-layout effects in SPH/GSPH](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-sph-pressure-acoustics-en) (`sph-pressure-acoustics`; Same-problem reference · Analytic reference)

Bind the fixed-input formula, reference, figure and executable code. GSPH with 128 jittered particles at t=0.2. The initial kernel reconstruction error reaches 0.011834, exceeding the acoustic amplitude 0.001 and remaining visible in the left density profile; the right panel shows that initial error. Acceptance concerns the fundamental Fourier mode phase/amplitude and other fixed conservation controls, not pointwise high accuracy or general superiority.
## Assumptions, units and boundaries

Regular/deterministicallyjitteredperiodicparticles, fixedhSPHcontrol vs adaptivehGSPH. Separateinitialkernelerror and fluidupdate, finiteamplitudeO(A²)linearizedreference remainder. No universalGSPHsuperiorityclaim.

**Editorial clarification**

GSPH with 128 jittered particles at t=0.2. The initial kernel reconstruction error reaches 0.011834, exceeding the acoustic amplitude 0.001 and remaining visible in the left density profile; the right panel shows that initial error. Acceptance concerns the fundamental Fourier mode phase/amplitude and other fixed conservation controls, not pointwise high accuracy or general superiority.

## Adopted numerical method

Regular/deterministicallyjitteredperiodicparticles, fixedhSPHcontrol vs adaptivehGSPH. Separateinitialkernelerror and fluidupdate, finiteamplitudeO(A²)linearizedreference remainder. No universalGSPHsuperiorityclaim.

$$
\partial_tU+\partial_xF(U)=0
$$

$$
U=(\rho,\rho u,E)^{\mathsf T}
$$

$$
F=(\rho u,\rho u^2+p,u(E+p))^{\mathsf T}
$$

Editorial equations from the frozen code and registered models. The release, calculations, acceptance conditions and saved results are unchanged.

## References and validation

Separate analytic/reference errors, conservation, refinement, independent component qualification and deliberately wrong-formula controls.

## Limits

Regular/deterministicallyjitteredperiodicparticles, fixedhSPHcontrol vs adaptivehGSPH. Separateinitialkernelerror and fluidupdate, finiteamplitudeO(A²)linearizedreference remainder. No universalGSPHsuperiorityclaim.

## Stored measurements and decisions

```json
{
  "metrics": {
    "profiles": 16,
    "linearization_remainder_scale": 1e-06
  },
  "checks": {
    "regular_static_force": true,
    "jittered_static_velocity": true,
    "acoustic_phase": true,
    "acoustic_amplitude": true,
    "conservation": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/sph-pressure-acoustics/index.json

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/atlas-continuum-particle-controls-2026-11-25.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

## Sources and review scope

- Reformulation of Smoothed Particle Hydrodynamics with Riemann Solver. https://arxiv.org/pdf/astro-ph/0206401; review_level=selected-original-author-paper-sections-and-equations
- New Third-Order Finite Volume Unequal-Sized WENO Lagrangian Schemes for Solving Euler Equations. https://www.mdpi.com/2227-7390/11/23/4842; review_level=selected-publisher-fulltext-example-8
- Second Order Corner Coupled Upwind Transport Methods for Lagrangian Hydrodynamics. https://www.osti.gov/servlets/purl/15005665; review_level=secondary-bibliographic-identity-original-report-unread
- A standard test set for numerical approximations to the shallow water equations in spherical geometry. https://digital.library.unt.edu/ark:/67531/metadc1069483/; review_level=author-report-bibliography-and-abstract-original-formulas-unread
- Cascade interpolation for semi-Lagrangian advection over the sphere. https://www.image.ucar.edu/staff/rnair/qj99_sph.pdf; review_level=selected-author-hosted-formulas-and-publisher-bibliography

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
