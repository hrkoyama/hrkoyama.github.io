# QR, SVD and least squares / QR・SVD・最小二乗

Status: educational-example

Householder QR and one-sided Jacobi SVD: orthogonality, rank and least squares: Original Householder QR and one-sided Jacobi SVD for real tall matrices are checked on ordinary, 10⁶-column-scaled and rank-deficient inputs, against separate LAPACK singular values and minimum-norm least-squares solutions. QR/SVD: prescribed spectra, perturbation gain and numerical rank: Vary condition number from 1 to 2³⁶ for exactly representable 16×4 dyadic matrices, separating reconstruction from forward solution error. Compare LAPACK and separately executed 80/120-digit references for the actual binary64 inputs.

Householder QRと片側Jacobi SVD：直交性・階数・最小二乗: 実の縦長行列に対するHouseholder QRと片側Jacobi SVDを自作し、通常行列・列スケール差10⁶の行列・階数落ち行列を検査します。独立LAPACKの特異値と最小ノルム最小二乗解を照合します。 QR/SVD：既定特異値・摂動増幅・数値階数: 二進で厳密に表現できる16×4行列の条件数を1から2³⁶まで変え、再構成誤差と解誤差を分けます。実際のbinary64入力に対し別環境で実行した80/120桁参照とLAPACKを比較します。

Householder QR and one-sided Jacobi SVD: orthogonality, rank and least squares: Not a full LAPACK replacement or validation of complex/wide matrices, arbitrary extreme scales or optimal relative singular-value accuracy. The 10⁻¹² cutoff defines numerical rather than exact mathematical rank. The experiment does not establish all hypotheses of the Demmel–Veselić accuracy results. QR/SVD: prescribed spectra, perturbation gain and numerical rank: Some LAPACK and projected-core numerical infrastructure is shared. mpmath SVD uses separate bidiagonalization and QR iteration; mpmath least squares is a separate high-precision implementation of the same Householder family. Tiny-singular-value relative accuracy is not guaranteed for arbitrary ill-conditioned matrices.

Other names: QR分解, SVD, 特異値分解, singular value decomposition, least squares, 最小二乗法

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/qr-svd/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/qr-svd/



- Reference: https://doi.org/10.1145/320941.320947 — Method-specific source; see the detailed reading for source role and actual review depth.
- Reference: https://doi.org/10.1007/bf02163027 — Method-specific source; see the detailed reading for source role and actual review depth.

## Small fixed-input validation supplements

Householder QR and one-sided Jacobi SVD: orthogonality, rank and least squares: Original Householder QR and one-sided Jacobi SVD for real tall matrices are checked on ordinary, 10⁶-column-scaled and rank-deficient inputs, against separate LAPACK singular values and minimum-norm least-squares solutions. QR/SVD: prescribed spectra, perturbation gain and numerical rank: Vary condition number from 1 to 2³⁶ for exactly representable 16×4 dyadic matrices, separating reconstruction from forward solution error. Compare LAPACK and separately executed 80/120-digit references for the actual binary64 inputs.

Householder QRと片側Jacobi SVD：直交性・階数・最小二乗: 実の縦長行列に対するHouseholder QRと片側Jacobi SVDを自作し、通常行列・列スケール差10⁶の行列・階数落ち行列を検査します。独立LAPACKの特異値と最小ノルム最小二乗解を照合します。 QR/SVD：既定特異値・摂動増幅・数値階数: 二進で厳密に表現できる16×4行列の条件数を1から2³⁶まで変え、再構成誤差と解誤差を分けます。実際のbinary64入力に対し別環境で実行した80/120桁参照とLAPACKを比較します。

- Householder QR and one-sided Jacobi SVD: orthogonality, rank and least squares: https://hrkoyama.github.io/numerical-methods-atlas/validation/qr-svd-factorization/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/atlas-foundations-2026-11-22.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/results/result.json

- QR/SVD: prescribed spectra, perturbation gain and numerical rank: https://hrkoyama.github.io/numerical-methods-atlas/validation/qr-svd-conditioning/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/atlas-foundations-conditioning-2026-11-22.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/results/result.json

Common execution records: [{"id": "qr-svd-factorization", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/qr-svd-factorization/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/qr-svd-factorization/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "qr-svd-conditioning", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/qr-svd-conditioning/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/qr-svd-conditioning/?lang=en"}, "kind": "dedicated-supplement"}]

Next: Preserve the published fixed-input scope; validate conditions, references and criteria separately for extensions.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/qr-svd/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

対応する方程式一覧の項目は未登録です。

#### 問題の図 (`method-problems-ja`)

##### [Householder QRと片側Jacobi SVD：直交性・階数・最小二乗](https://hrkoyama.github.io/numerical-methods-atlas/problems/matrix-factorization/?lang=ja) (`matrix-factorization`)

![固定した満階数・階数落ち行列で、Householder QR・片側Jacobi SVDの再構成、保持階数の直交性、LAPACKとの差を保存値から図示。丸めゼロは1e−16へ置いて表示。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/results/qr-svd-factorization.png)

この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/matrix-factorization/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/matrix-factorization/?lang=ja#code-ja)

- [Householder QRと片側Jacobi SVD：直交性・階数・最小二乗](https://hrkoyama.github.io/numerical-methods-atlas/validation/qr-svd-factorization/?lang=ja) (`qr-svd-factorization`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/atlas-foundations-2026-11-22.zip)

実の縦長行列に対するHouseholder QRと片側Jacobi SVDを自作し、通常行列・列スケール差10⁶の行列・階数落ち行列を検査します。独立LAPACKの特異値と最小ノルム最小二乗解を照合します。

- [QR/SVD：既定特異値・摂動増幅・数値階数](https://hrkoyama.github.io/numerical-methods-atlas/validation/qr-svd-conditioning/?lang=ja) (`qr-svd-conditioning`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/atlas-foundations-conditioning-2026-11-22.zip)

二進で厳密に表現できる16×4行列の条件数を1から2³⁶まで変え、再構成誤差と解誤差を分けます。実際のbinary64入力に対し別環境で実行した80/120桁参照とLAPACKを比較します。


#### 厳密解・参照解 (`method-references-ja`)

##### [Householder QRと片側Jacobi SVD：直交性・階数・最小二乗](https://hrkoyama.github.io/numerical-methods-atlas/problems/matrix-factorization/?lang=ja#references-ja) (`matrix-factorization`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/qr-svd/)
- 保存結果: [この配布版の保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/results/result.json)
- 検証記録: [配布版の検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/verification.json)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

##### Householder QRと片側Jacobi SVD：直交性・階数・最小二乗 (`qr-svd-factorization`)

[Householder QRと片側Jacobi SVD：直交性・階数・最小二乗](https://hrkoyama.github.io/numerical-methods-atlas/problems/matrix-factorization/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/qr-svd-factorization/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/atlas-foundations-2026-11-22.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/verification.json)

実の縦長行列に対するHouseholder QRと片側Jacobi SVDを自作し、通常行列・列スケール差10⁶の行列・階数落ち行列を検査します。独立LAPACKの特異値と最小ノルム最小二乗解を照合します。

##### QR/SVD：既定特異値・摂動増幅・数値階数 (`qr-svd-conditioning`)

[Householder QRと片側Jacobi SVD：直交性・階数・最小二乗](https://hrkoyama.github.io/numerical-methods-atlas/problems/matrix-factorization/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/qr-svd-conditioning/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/atlas-foundations-conditioning-2026-11-22.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/verification.json)

二進で厳密に表現できる16×4行列の条件数を1から2³⁶まで変え、再構成誤差と解誤差を分けます。実際のbinary64入力に対し別環境で実行した80/120桁参照とLAPACKを比較します。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

Householder QRと片側Jacobi SVD：直交性・階数・最小二乗: 実の縦長行列に対するHouseholder QRと片側Jacobi SVDを自作し、通常行列・列スケール差10⁶の行列・階数落ち行列を検査します。独立LAPACKの特異値と最小ノルム最小二乗解を照合します。 QR/SVD：既定特異値・摂動増幅・数値階数: 二進で厳密に表現できる16×4行列の条件数を1から2³⁶まで変え、再構成誤差と解誤差を分けます。実際のbinary64入力に対し別環境で実行した80/120桁参照とLAPACKを比較します。

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/atlas-foundations-2026-11-22.zip)

[配布版の検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/verification.json)

###### 関連ソース

- [/code/validated-examples/2026-11-22/foundations/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/run.py)
- [/code/validated-examples/2026-11-22/foundations/solvers.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/solvers.py)
- [/code/validated-examples/2026-11-22/foundations-conditioning/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/run.py)
- [/code/validated-examples/2026-11-22/foundations-conditioning/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/experiments.py)
- [/code/validated-examples/2026-11-22/foundations-conditioning/fixtures.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/fixtures.py)
- [/code/validated-examples/2026-11-22/foundations-conditioning/mpmath_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/mpmath_reference.py)
- [/code/validated-examples/2026-11-22/foundations-conditioning/solvers.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/solvers.py)

###### 配布版のテスト

- [/code/validated-examples/2026-11-22/foundations/test_foundations.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/test_foundations.py)
- [/code/validated-examples/2026-11-22/foundations-conditioning/test_conditioning.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/test_conditioning.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q
python run.py --input inputs.json --output output
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

No corresponding equation-registry entry is registered.

#### Problem figures (`method-problems-en`)

##### [Householder QR and one-sided Jacobi SVD: orthogonality, rank and least squares](https://hrkoyama.github.io/numerical-methods-atlas/problems/matrix-factorization/?lang=en) (`matrix-factorization`)

![Saved reconstruction, retained-rank orthogonality and LAPACK differences for fixed full/rank-deficient Householder-QR and one-sided-Jacobi-SVD inputs. Roundoff zeros are displayed at 1e-16.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/results/qr-svd-factorization.png)

Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/matrix-factorization/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/matrix-factorization/?lang=en#code-en)

- [Householder QR and one-sided Jacobi SVD: orthogonality, rank and least squares](https://hrkoyama.github.io/numerical-methods-atlas/validation/qr-svd-factorization/?lang=en) (`qr-svd-factorization`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/atlas-foundations-2026-11-22.zip)

Original Householder QR and one-sided Jacobi SVD for real tall matrices are checked on ordinary, 10⁶-column-scaled and rank-deficient inputs, against separate LAPACK singular values and minimum-norm least-squares solutions.

- [QR/SVD: prescribed spectra, perturbation gain and numerical rank](https://hrkoyama.github.io/numerical-methods-atlas/validation/qr-svd-conditioning/?lang=en) (`qr-svd-conditioning`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/atlas-foundations-conditioning-2026-11-22.zip)

Vary condition number from 1 to 2³⁶ for exactly representable 16×4 dyadic matrices, separating reconstruction from forward solution error. Compare LAPACK and separately executed 80/120-digit references for the actual binary64 inputs.


#### Exact / reference solutions (`method-references-en`)

##### [Householder QR and one-sided Jacobi SVD: orthogonality, rank and least squares](https://hrkoyama.github.io/numerical-methods-atlas/problems/matrix-factorization/?lang=en#references-en) (`matrix-factorization`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/qr-svd/)
- Saved result: [Saved results from this edition](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/results/result.json)
- Verification receipt: [Edition verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/verification.json)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

##### Householder QR and one-sided Jacobi SVD: orthogonality, rank and least squares (`qr-svd-factorization`)

[Householder QR and one-sided Jacobi SVD: orthogonality, rank and least squares](https://hrkoyama.github.io/numerical-methods-atlas/problems/matrix-factorization/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/qr-svd-factorization/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/atlas-foundations-2026-11-22.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/verification.json)

Original Householder QR and one-sided Jacobi SVD for real tall matrices are checked on ordinary, 10⁶-column-scaled and rank-deficient inputs, against separate LAPACK singular values and minimum-norm least-squares solutions.

##### QR/SVD: prescribed spectra, perturbation gain and numerical rank (`qr-svd-conditioning`)

[Householder QR and one-sided Jacobi SVD: orthogonality, rank and least squares](https://hrkoyama.github.io/numerical-methods-atlas/problems/matrix-factorization/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/qr-svd-conditioning/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/atlas-foundations-conditioning-2026-11-22.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/verification.json)

Vary condition number from 1 to 2³⁶ for exactly representable 16×4 dyadic matrices, separating reconstruction from forward solution error. Compare LAPACK and separately executed 80/120-digit references for the actual binary64 inputs.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Householder QR and one-sided Jacobi SVD: orthogonality, rank and least squares: Original Householder QR and one-sided Jacobi SVD for real tall matrices are checked on ordinary, 10⁶-column-scaled and rank-deficient inputs, against separate LAPACK singular values and minimum-norm least-squares solutions. QR/SVD: prescribed spectra, perturbation gain and numerical rank: Vary condition number from 1 to 2³⁶ for exactly representable 16×4 dyadic matrices, separating reconstruction from forward solution error. Compare LAPACK and separately executed 80/120-digit references for the actual binary64 inputs.

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[Related code edition / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/atlas-foundations-2026-11-22.zip)

[Edition verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/verification.json)

###### Related source

- [/code/validated-examples/2026-11-22/foundations/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/run.py)
- [/code/validated-examples/2026-11-22/foundations/solvers.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/solvers.py)
- [/code/validated-examples/2026-11-22/foundations-conditioning/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/run.py)
- [/code/validated-examples/2026-11-22/foundations-conditioning/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/experiments.py)
- [/code/validated-examples/2026-11-22/foundations-conditioning/fixtures.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/fixtures.py)
- [/code/validated-examples/2026-11-22/foundations-conditioning/mpmath_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/mpmath_reference.py)
- [/code/validated-examples/2026-11-22/foundations-conditioning/solvers.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/solvers.py)

###### Package tests

- [/code/validated-examples/2026-11-22/foundations/test_foundations.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/test_foundations.py)
- [/code/validated-examples/2026-11-22/foundations-conditioning/test_conditioning.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/test_conditioning.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q
python run.py --input inputs.json --output output
```
