# Turing不安定性：線形成長率と小振幅パターン

Schnakenberg型反応拡散で、一様平衡の安定性と拡散による選択モードの成長を行列指数で検証します。

**使用手法**

- [空間中心差分](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=ja) (`centered-difference`)
- [古典的RK4](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=ja) (`rk4`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/turing-schnakenberg/?lang=ja#turing-schnakenberg-ja-algorithm)

独自の中心差分・RK4で線形化PDEと短い非線形PDEを進めます。3格子でのモード振幅と成長率、非線形の濃度最小値・初期パターン増幅を記録します。

$$
u_t=D_u u_{xx}+a-u+u^2v,\quad v_t=D_v v_{xx}+b-u^2v
$$

$$
\partial_t\widehat{\delta z}=(J-k^2D)\widehat{\delta z},\quad \widehat{\delta z}(t)=e^{(J-k^2D)t}\widehat{\delta z}(0)
$$

方程式一覧の対応項目は未登録です。個別の式・近似・診断は上の定義に示します。

**問題の図**

![Turing不安定性：線形成長率と小振幅パターン：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/turing-schnakenberg.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Turing不安定性：線形成長率と小振幅パターン](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=ja) (`turing-schnakenberg`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/turing-schnakenberg/?lang=ja#turing-schnakenberg-ja-validation)

連続Fourier行列J-k²DのSciPy expmと線形数値解を比較し空間収束を測定。非線形計算は半離散線形行列指数との小振幅差を測り、成熟模様の参照照合とは区別します。

参照解一覧の対応カードは未登録です。この実行例の参照値・判定方法は上の検証資料で確認できます。
## 前提・単位・境界

無次元a=0.1,b=0.9、平衡(1,0.9)、拡散係数(0.01,1)、周期k=2、初期振幅1e-4。線形t=1と非線形t=4の短い計算に限定します。

## 採用した計算法

独自の中心差分・RK4で線形化PDEと短い非線形PDEを進めます。3格子でのモード振幅と成長率、非線形の濃度最小値・初期パターン増幅を記録します。

$$
u_t=D_u u_{xx}+a-u+u^2v,\quad v_t=D_v v_{xx}+b-u^2v
$$

$$
\partial_t\widehat{\delta z}=(J-k^2D)\widehat{\delta z},\quad \widehat{\delta z}(t)=e^{(J-k^2D)t}\widehat{\delta z}(0)
$$

## 比較・検証

連続Fourier行列J-k²DのSciPy expmと線形数値解を比較し空間収束を測定。非線形計算は半離散線形行列指数との小振幅差を測り、成熟模様の参照照合とは区別します。

## 確認の限界

1つの平衡近傍の発生段階です。原著係数や原著実験の再現、成熟模様、ランダム擾乱からの波数選択、実生物の較正は主張しません。

## 保存実測値と判定

```json
{
  "metrics": {
    "homogeneous_max_real_eigenvalue": -0.10000000000000003,
    "continuum_mode_growth_rate": 0.42841126979143596,
    "linear_finest_relative_error": 0.00024726924944451685,
    "linear_minimum_spatial_order": 2.000750498056138,
    "linear_finest_growth_rate_error": 7.301377900481576e-05,
    "nonlinear_minimum_concentration": 0.8998159771334997,
    "nonlinear_early_linear_relative_error": 0.00016918909911058558,
    "pattern_amplitude_growth": 5.535462628423193
  },
  "checks": {
    "homogeneous_stable": true,
    "diffusion_mode_unstable": true,
    "linear_space_error": true,
    "linear_space_order": true,
    "growth_rate": true,
    "nonlinear_finite_positive": true,
    "early_linear_agreement": true,
    "growing_spatial_pattern": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/turing-schnakenberg/index.json

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。

## 出典と確認範囲

- A. M. Turing (1952). The Chemical Basis of Morphogenesis. https://royalsocietypublishing.org/doi/10.1098/rstb.1952.0012; review_level=publisher-archive-and-original-first-page-metadata
  Royal Societyの原稿審査記録と大学公開の原著第1ページの書誌を確認。出版社本文は403でした。拡散誘起不安定性の歴史的原著で、採用したSchnakenberg数値例の出典とは区別します。
- J. Schnakenberg (1979). Simple chemical reaction systems with limit cycle behaviour. https://pubmed.ncbi.nlm.nih.gov/537379/; review_level=official-bibliographic-metadata
  PubMedの書誌・DOIを確認（抄録なし）。反応系の原典として引用し、採用係数a=0.1,b=0.9や今回の空間パターンを原著から転記したとは扱いません。
- The SciPy community (2024). SciPy1.14.1 expm reference. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.linalg.expm.html; review_level=official-api-documentation
  公式の行列指数APIとPadé/scaling-and-squaring法の記載を確認。

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Turing instability: linear growth and small-amplitude patterns

Use a matrix exponential to validate stable homogeneous kinetics and diffusion-driven growth of a selected Schnakenberg mode.

**Methods used**

- [Centered spatial difference](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en) (`centered-difference`)
- [Classical RK4](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=en) (`rk4`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/turing-schnakenberg/?lang=en#turing-schnakenberg-en-algorithm)

Advance the linearized and short nonlinear PDEs using original centered differences/RK4. Record mode amplitudes/growth on three grids, minimum concentrations and early-pattern amplification.

$$
u_t=D_u u_{xx}+a-u+u^2v,\quad v_t=D_v v_{xx}+b-u^2v
$$

$$
\partial_t\widehat{\delta z}=(J-k^2D)\widehat{\delta z},\quad \widehat{\delta z}(t)=e^{(J-k^2D)t}\widehat{\delta z}(0)
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![Turing instability: linear growth and small-amplitude patterns: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/turing-schnakenberg.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Turing instability: linear growth and small-amplitude patterns](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=en) (`turing-schnakenberg`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/turing-schnakenberg/?lang=en#turing-schnakenberg-en-validation)

Compare linear numerical fields with SciPy expm of continuum J-k²D and measure spatial convergence. Quantify the nonlinear run against a semidiscrete linear matrix exponential as a small-amplitude check, not validation of mature morphology.

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.
## Assumptions, units and boundaries

Dimensionless a=0.1,b=0.9, equilibrium(1,0.9), diffusivities(0.01,1), periodic k=2 and initial amplitude1e-4. Restrict runs to linear t=1 and nonlinear t=4.

## Adopted numerical method

Advance the linearized and short nonlinear PDEs using original centered differences/RK4. Record mode amplitudes/growth on three grids, minimum concentrations and early-pattern amplification.

$$
u_t=D_u u_{xx}+a-u+u^2v,\quad v_t=D_v v_{xx}+b-u^2v
$$

$$
\partial_t\widehat{\delta z}=(J-k^2D)\widehat{\delta z},\quad \widehat{\delta z}(t)=e^{(J-k^2D)t}\widehat{\delta z}(0)
$$

## References and validation

Compare linear numerical fields with SciPy expm of continuum J-k²D and measure spatial convergence. Quantify the nonlinear run against a semidiscrete linear matrix exponential as a small-amplitude check, not validation of mature morphology.

## Limits

One near-equilibrium onset experiment. No claim reproduces original-paper parameters/experiments, mature patterns, wavenumber selection from random noise or biological calibration.

## Stored measurements and decisions

```json
{
  "metrics": {
    "homogeneous_max_real_eigenvalue": -0.10000000000000003,
    "continuum_mode_growth_rate": 0.42841126979143596,
    "linear_finest_relative_error": 0.00024726924944451685,
    "linear_minimum_spatial_order": 2.000750498056138,
    "linear_finest_growth_rate_error": 7.301377900481576e-05,
    "nonlinear_minimum_concentration": 0.8998159771334997,
    "nonlinear_early_linear_relative_error": 0.00016918909911058558,
    "pattern_amplitude_growth": 5.535462628423193
  },
  "checks": {
    "homogeneous_stable": true,
    "diffusion_mode_unstable": true,
    "linear_space_error": true,
    "linear_space_order": true,
    "growth_rate": true,
    "nonlinear_finite_positive": true,
    "early_linear_agreement": true,
    "growing_spatial_pattern": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/turing-schnakenberg/index.json

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group.

## Sources and review scope

- A. M. Turing (1952). The Chemical Basis of Morphogenesis. https://royalsocietypublishing.org/doi/10.1098/rstb.1952.0012; review_level=publisher-archive-and-original-first-page-metadata
  Royal Society manuscript-review archive and bibliography on the original first page hosted by a university checked. Publisher text returned 403. Historical source for diffusion-driven instability, distinct from this adopted Schnakenberg example.
- J. Schnakenberg (1979). Simple chemical reaction systems with limit cycle behaviour. https://pubmed.ncbi.nlm.nih.gov/537379/; review_level=official-bibliographic-metadata
  PubMed bibliography and DOI checked (no abstract). Cited for the reaction-system family; a=0.1,b=0.9 and this spatial experiment are adopted educational inputs, not a transcription of the original experiment.
- The SciPy community (2024). SciPy1.14.1 expm reference. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.linalg.expm.html; review_level=official-api-documentation
  Official matrix-exponential API and description of the Pade/scaling-and-squaring method checked.

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
