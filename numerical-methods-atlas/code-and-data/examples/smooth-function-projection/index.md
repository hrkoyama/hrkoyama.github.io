# Smooth function: Legendre projection and GLL interpolation / 滑らかな関数：Legendre射影とGLL補間

Entry: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/smooth-function-projection/
Registry: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json
Source record: smooth-function-projection

Public-file rerun: passed
Receipt: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-periodic.json

## ja

exp(x)のLegendre射影とGLL補間を比較し、次数による誤差減少・係数・直交性を別の高次求積で確認する。

### scope

exp(x)を次数2/4/6/8でL2射影し、同じ次数のGLL節点補間と比較する。実装の32点Gaussとは別の64/96点求積と独立Legendre再帰式で係数・直交性・誤差を確認する。

### assumptions

参照区間[−1,1]、重み1のLegendre内積。GLLはp+1節点。高次求積の一致を参照精度の補助検査とし、一般関数の厳密積分とは主張しない。出力201点は誤差積分用の求積点とは別。

### units

参照座標ξとexp(ξ)は無次元。L2誤差は重み1の区間積分から計算する。

### boundaries

補間・射影の問題で物理境界条件はない。GLLの端点節点はPDE境界の施行を意味しない。

### Input and run

Input: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/recipes/smooth-function-projection.json
Input SHA-256: 97e6d8f9819e62d2c16e99a7364e05526cbed382d0615f63d73596f512c2b7ea
ZIP: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip
Run from: atlas-code-2026-11-22

```sh
python -m pip install -r requirements.txt
python run_recipe.py --input recipes/smooth-function-projection.json --output output-smooth-function-projection
```

### Outputs

- result.json (json): https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/smooth-function-projection/result.json
- solution.csv (csv): https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/smooth-function-projection/solution.csv

CSVは次数ごとに201点、各行で射影値・GLL補間値・exp(x)を整列。次数別L2誤差、係数差、直交性残差、64/96点求積の差はJSONに記録する。

### Numerical acceptance

- projection-l2-error / exp(x)の8次L2射影の値誤差。高次モードの既知の急減に基づく保守的上限。: /metrics/finest_projection_l2_error; value ≤ 2e-08
- interpolation-l2-error / 同じ8次GLL節点補間を別の高次求積で評価する。: /metrics/finest_gll_interpolation_l2_error; value ≤ 5e-08
- projection-degree-refinement / 次数を2ずつ上げたとき射影誤差が少なくとも10分の1になる。: /metrics/minimum_projection_error_reduction; value ≥ 10
- interpolation-degree-refinement / 次数を2ずつ上げたとき補間誤差が少なくとも10分の1になる。: /metrics/minimum_interpolation_error_reduction; value ≥ 10
- independent-modal-coefficients / 独立のLegendre再帰式と96点求積による係数との一致。射影と同じ求積を繰り返さない。: /metrics/maximum_independent_coefficient_difference; value ≤ 1e-11
- projection-orthogonality / 残差とP0からPpの内積を高次求積で評価し、L2射影の直交性を確認する。: /metrics/maximum_projection_orthogonality_defect; value ≤ 1e-12
- quadrature-reference-agreement / 64点と96点求積でL2誤差の評価が一致し、参照求積の不足を検知する。: /metrics/maximum_reference_quadrature_disagreement; value ≤ 1e-12
- all-criteria / 全数値条件の判定: /checks; all values = true
- input-provenance / 実行した固定入力のSHA-256: /input_sha256; value = 97e6d8f9819e62d2c16e99a7364e05526cbed382d0615f63d73596f512c2b7ea
- case-passed / 入力に記載した条件の合格: /passed; value = true

### Failure and scope

exp(x)・GLL・次数増加・参照求積を固定し、非有限値や不適切な次数・参照求積数を拒否。不連続関数、高次数での安定性、曲線要素やPDE全体の検証ではない。解説本文は現在英語版。

Reading: https://hrkoyama.github.io/numerical-methods-atlas/en/read/basis-functions/

### References

- CSVは次数ごとに201点、各行で射影値・GLL補間値・exp(x)を整列。次数別L2誤差、係数差、直交性残差、64/96点求積の差はJSONに記録する。: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/smooth-function-projection/result.json
- exp(x)を直接評価し、異なる高次求積と独立の三項再帰でモード係数を求め直す。射影自身の求積値の再利用による自明な一致ではない。: https://hrkoyama.github.io/numerical-methods-atlas/en/read/basis-functions/
- 既存基底項目のLegendreモード・GLL節点表現の文献。多項式基底の歴史的起源の主張には用いない。: https://doi.org/10.1016/j.jcp.2014.12.012

Code license: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/LICENSE
Content/data terms: https://hrkoyama.github.io/rights/
自作コードはMIT。入力・数値データ・図・本文はサイトの個別条件に従います。この台帳は利用許諾を拡大しません。

## en

Compare Legendre projection and GLL interpolation of exp(x); use higher-order reference quadrature for p-refinement, coefficients and orthogonality.

### scope

L2-project exp(x) at degrees 2/4/6/8 and compare GLL interpolation at the same degrees. Check coefficients, orthogonality and errors using separate 64/96-point rules and an independent Legendre recurrence, versus 32-point projection quadrature.

### assumptions

Reference interval [−1,1] and unit-weight Legendre inner product; GLL has p+1 nodes. Agreement of higher-order rules supports reference accuracy but is not an exact-integration claim for arbitrary functions. The 201 output points are separate from error quadrature.

### units

Dimensionless reference coordinate ξ and exp(ξ); L2 errors use unit-weight interval integration.

### boundaries

An interpolation/projection problem without physical boundary conditions; GLL endpoint nodes do not enforce a PDE boundary.

### Input and run

Input: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/recipes/smooth-function-projection.json
Input SHA-256: 97e6d8f9819e62d2c16e99a7364e05526cbed382d0615f63d73596f512c2b7ea
ZIP: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip
Run from: atlas-code-2026-11-22

```sh
python -m pip install -r requirements.txt
python run_recipe.py --input recipes/smooth-function-projection.json --output output-smooth-function-projection
```

### Outputs

- result.json (json): https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/smooth-function-projection/result.json
- solution.csv (csv): https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/smooth-function-projection/solution.csv

CSV provides 201 aligned projection/interpolation/exp(x) rows per degree. JSON records degree-wise L2 errors, coefficient differences, orthogonality and 64/96-point quadrature agreement.

### Numerical acceptance

- projection-l2-error / Value error of degree-eight L2 projection of exp(x), with a conservative bound for rapidly decaying smooth-function modes.: /metrics/finest_projection_l2_error; value ≤ 2e-08
- interpolation-l2-error / Degree-eight GLL interpolation evaluated using separate higher-order quadrature.: /metrics/finest_gll_interpolation_l2_error; value ≤ 5e-08
- projection-degree-refinement / Projection error falls by at least a factor ten for each two-degree increase.: /metrics/minimum_projection_error_reduction; value ≥ 10
- interpolation-degree-refinement / Interpolation error falls by at least a factor ten for each two-degree increase.: /metrics/minimum_interpolation_error_reduction; value ≥ 10
- independent-modal-coefficients / Agreement with coefficients from a separate Legendre recurrence and 96-point quadrature, not repeated projection quadrature.: /metrics/maximum_independent_coefficient_difference; value ≤ 1e-11
- projection-orthogonality / Higher-order quadrature checks residual orthogonality against P0 through Pp.: /metrics/maximum_projection_orthogonality_defect; value ≤ 1e-12
- quadrature-reference-agreement / L2-error estimates agree between 64- and 96-point rules, detecting inadequate reference quadrature.: /metrics/maximum_reference_quadrature_disagreement; value ≤ 1e-12
- all-criteria / All numerical acceptance flags: /checks; all values = true
- input-provenance / SHA-256 of the executed fixed input: /input_sha256; value = 97e6d8f9819e62d2c16e99a7364e05526cbed382d0615f63d73596f512c2b7ea
- case-passed / Acceptance conditions in the input passed: /passed; value = true

### Failure and scope

Fix exp(x), GLL, degree refinement and reference quadrature; reject nonfinite/invalid degrees or inadequate reference rules. Not validation for discontinuities, high-degree stability, curved elements or a full PDE. The current reading is English only.

Reading: https://hrkoyama.github.io/numerical-methods-atlas/en/read/basis-functions/

### References

- CSV provides 201 aligned projection/interpolation/exp(x) rows per degree. JSON records degree-wise L2 errors, coefficient differences, orthogonality and 64/96-point quadrature agreement.: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/smooth-function-projection/result.json
- Direct exp(x) evaluation plus different high-order quadrature and a separate three-term recurrence recompute modal coefficients; the reference does not reuse the projection's own quadrature.: https://hrkoyama.github.io/numerical-methods-atlas/en/read/basis-functions/
- Existing basis-method reference for Legendre modal and GLL nodal formulations, without a historical-origin claim.: https://doi.org/10.1016/j.jcp.2014.12.012

Code license: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/LICENSE
Content/data terms: https://hrkoyama.github.io/rights/
Original code is MIT. Inputs, numerical data, figures and prose retain the site’s item-specific terms. This registry does not expand reuse permissions.
