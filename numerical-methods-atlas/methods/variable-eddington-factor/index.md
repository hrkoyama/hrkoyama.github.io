# Variable Eddington factor (1D VEF) / 可変Eddington因子（1D VEF）

Status: educational-example

Compute f=Kxx/E from angular transport and iterate a separate closed moment solve, checked on a small fixed periodic scattering problem.

角度輸送から因子f=Kxx/Eを求め、別のモーメント方程式を閉じて反復します。周期散乱場の小さな固定例で確認します。

Position x and angular cosine mu are not two spatial dimensions. This periodic homogeneous educational control does not validate inflow boundaries, time evolution, material/fluid coupling, nonlinear FLD, general AP properties or speedup.

Other names: VEF, variable Eddington factor, 可変エディントン因子, quasidiffusion, 準拡散法

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/variable-eddington/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/variable-eddington/



- Reference: https://academic.oup.com/mnras/article/149/1/65/2604466 — Publisher title/authors/date/DOI and abstract. Establishes historical variable-factor iteration and grey example. Limits: Original scannedPDF fetch failed; original equations, full tests and non-LTE calculations are unread and must not be claimed reproduced.
- Reference: https://arxiv.org/pdf/2301.04758 — Section2, PDFpp3–4: transport Eq1, moment equations Eq2, angular tensor and boundary factor Eq3, fixed-point steps. Introduction on independent spatial discretizations also read. Limits: No claim of full59page reading, high-order mixedFEM reproduction, curved-mesh, multigrid or scalability validation.
- Reference: https://arxiv.org/pdf/2111.12255 — Introduction PDFpp1–3 on independent HO/LO discretizations, finite-mesh moment differences and conservation; no numerical tables adopted. Limits: No claim of reproducing high-orderDG, preconditioner performance or large-mesh studies.

## Small fixed-input validation supplements

Iteratively couple formal angular transport to independent moment equations and compare the spatially varying factor f with a closed-form reference.

形式的な角度輸送と独立なモーメント方程式を反復結合し、位置で変わる因子fを閉形式参照と比較します。

- Variable Eddington factor: a periodic 1D scattering-source control: https://hrkoyama.github.io/numerical-methods-atlas/validation/vef-fourier-scattering1d/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/atlas-variable-eddington-controls-2026-11-26.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/results/result.json

Common execution records: [{"id": "vef-fourier-scattering1d", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/vef-fourier-scattering1d/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/vef-fourier-scattering1d/?lang=en"}, "kind": "dedicated-supplement"}]

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/variable-eddington-factor/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [静止灰色輻射のVEF・VETモーメント閉包](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#static-grey-variable-eddington-moments-ja) (`static-grey-variable-eddington-moments`; vef-fourier-scattering1d)

#### 問題の図 (`method-problems-ja`)

##### [可変エディントン因子：周期1D散乱源の固定検証](https://hrkoyama.github.io/numerical-methods-atlas/problems/vef-fourier-scattering1d/?lang=ja) (`vef-fourier-scattering1d`)

![形式的な角度輸送と独立なモーメント方程式を反復結合し、位置で変わる因子fを閉形式参照と比較します。 図の横軸xと角度余弦μは2つの空間次元ではありません。周期・一様係数の教育例で、流入境界、時間発展、物質・流体結合、非線形FLD、一般AP性や速度向上は検証しません。](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/results/vef-fourier-scattering1d.png)

形式的な角度輸送と独立なモーメント方程式を反復結合し、位置で変わる因子fを閉形式参照と比較します。 図の横軸xと角度余弦μは2つの空間次元ではありません。周期・一様係数の教育例で、流入境界、時間発展、物質・流体結合、非線形FLD、一般AP性や速度向上は検証しません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/vef-fourier-scattering1d/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/vef-fourier-scattering1d/?lang=ja#code-ja)

- [可変エディントン因子：周期1D散乱源の固定検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/vef-fourier-scattering1d/?lang=ja) (`vef-fourier-scattering1d`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/atlas-variable-eddington-controls-2026-11-26.zip)

形式的な角度輸送と独立なモーメント方程式を反復結合し、位置で変わる因子fを閉形式参照と比較します。


#### 厳密解・参照解 (`method-references-ja`)

##### [可変エディントン因子：周期1D散乱源の固定検証](https://hrkoyama.github.io/numerical-methods-atlas/problems/vef-fourier-scattering1d/?lang=ja#references-ja) (`vef-fourier-scattering1d`)

- [本例のために導出した周期1D VEFの連続Fourier応答](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-vef-fourier-scattering1d-ja) (`vef-fourier-scattering1d`; 同じ問題の参照; 解析参照)

正の指定等方輻射源に対する連続角度Fourier応答が、同じ固定問題の解析参照です。点値・面位置・複素位相を区別し、異なるHO/LO離散化の差は保存します。 図の横軸xと角度余弦μは2つの空間次元ではありません。周期・一様係数の教育例で、流入境界、時間発展、物質・流体結合、非線形FLD、一般AP性や速度向上は検証しません。

[既存の参照図](/numerical-methods-atlas/validation/vef-fourier-scattering1d/?lang=ja#vef-fourier-scattering1d-ja-measurements)

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/variable-eddington/)
- 保存結果: [この配布版の保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/results/result.json)
- 検証記録: [配布版の検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/verification.json)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

##### 可変エディントン因子：周期1D散乱源の固定検証 (`vef-fourier-scattering1d`)

[可変エディントン因子：周期1D散乱源の固定検証](https://hrkoyama.github.io/numerical-methods-atlas/problems/vef-fourier-scattering1d/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/vef-fourier-scattering1d/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/atlas-variable-eddington-controls-2026-11-26.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/verification.json)

形式的な角度輸送と独立なモーメント方程式を反復結合し、位置で変わる因子fを閉形式参照と比較します。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

形式的な角度輸送と独立なモーメント方程式を反復結合し、位置で変わる因子fを閉形式参照と比較します。

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/atlas-variable-eddington-controls-2026-11-26.zip)

[配布版の検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/verification.json)

###### 関連ソース

- [/code/validated-examples/2026-11-26/variable-eddington-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/run.py)
- [/code/validated-examples/2026-11-26/variable-eddington-controls/primary.py](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/primary.py)
- [/code/validated-examples/2026-11-26/variable-eddington-controls/analytic_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/analytic_reference.py)

###### 配布版のテスト

- [/code/validated-examples/2026-11-26/variable-eddington-controls/test_cases.py](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/test_cases.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q
python run.py --input inputs.json --output output
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Static grey VEF/VET moment closure](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#static-grey-variable-eddington-moments-en) (`static-grey-variable-eddington-moments`; vef-fourier-scattering1d)

#### Problem figures (`method-problems-en`)

##### [Variable Eddington factor: a periodic 1D scattering-source control](https://hrkoyama.github.io/numerical-methods-atlas/problems/vef-fourier-scattering1d/?lang=en) (`vef-fourier-scattering1d`)

![Iteratively couple formal angular transport to independent moment equations and compare the spatially varying factor f with a closed-form reference. Position x and angular cosine mu are not two spatial dimensions. This periodic homogeneous educational control does not validate inflow boundaries, time evolution, material/fluid coupling, nonlinear FLD, general AP properties or speedup.](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/results/vef-fourier-scattering1d.png)

Iteratively couple formal angular transport to independent moment equations and compare the spatially varying factor f with a closed-form reference. Position x and angular cosine mu are not two spatial dimensions. This periodic homogeneous educational control does not validate inflow boundaries, time evolution, material/fluid coupling, nonlinear FLD, general AP properties or speedup.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/vef-fourier-scattering1d/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/vef-fourier-scattering1d/?lang=en#code-en)

- [Variable Eddington factor: a periodic 1D scattering-source control](https://hrkoyama.github.io/numerical-methods-atlas/validation/vef-fourier-scattering1d/?lang=en) (`vef-fourier-scattering1d`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/atlas-variable-eddington-controls-2026-11-26.zip)

Iteratively couple formal angular transport to independent moment equations and compare the spatially varying factor f with a closed-form reference.


#### Exact / reference solutions (`method-references-en`)

##### [Variable Eddington factor: a periodic 1D scattering-source control](https://hrkoyama.github.io/numerical-methods-atlas/problems/vef-fourier-scattering1d/?lang=en#references-en) (`vef-fourier-scattering1d`)

- [Authored continuum Fourier response for periodic 1D VEF](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-vef-fourier-scattering1d-en) (`vef-fourier-scattering1d`; Same-problem reference; Analytic reference)

The continuum-angle Fourier response to the prescribed positive isotropic source is an analytic reference for this same fixed problem. Keep point/face locations and complex phase distinct, retaining the independent HO/LO discretization gap. Position x and angular cosine mu are not two spatial dimensions. This periodic homogeneous educational control does not validate inflow boundaries, time evolution, material/fluid coupling, nonlinear FLD, general AP properties or speedup.

[Existing reference profile](/numerical-methods-atlas/validation/vef-fourier-scattering1d/?lang=en#vef-fourier-scattering1d-en-measurements)

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/variable-eddington/)
- Saved result: [Saved results from this edition](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/results/result.json)
- Verification receipt: [Edition verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/verification.json)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

##### Variable Eddington factor: a periodic 1D scattering-source control (`vef-fourier-scattering1d`)

[Variable Eddington factor: a periodic 1D scattering-source control](https://hrkoyama.github.io/numerical-methods-atlas/problems/vef-fourier-scattering1d/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/vef-fourier-scattering1d/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/atlas-variable-eddington-controls-2026-11-26.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/verification.json)

Iteratively couple formal angular transport to independent moment equations and compare the spatially varying factor f with a closed-form reference.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Iteratively couple formal angular transport to independent moment equations and compare the spatially varying factor f with a closed-form reference.

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[Related code edition / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/atlas-variable-eddington-controls-2026-11-26.zip)

[Edition verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/verification.json)

###### Related source

- [/code/validated-examples/2026-11-26/variable-eddington-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/run.py)
- [/code/validated-examples/2026-11-26/variable-eddington-controls/primary.py](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/primary.py)
- [/code/validated-examples/2026-11-26/variable-eddington-controls/analytic_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/analytic_reference.py)

###### Package tests

- [/code/validated-examples/2026-11-26/variable-eddington-controls/test_cases.py](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/test_cases.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q
python run.py --input inputs.json --output output
```
