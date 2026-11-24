# Wavelets / ウェーブレット

Status: educational-example

Map multiresolution representations and local structure. Fixed educational executions: Haar multiresolution: boundaries, shifts and thresholds.

多重解像度表現と局所構造の扱いを整理する。 固定した教育用実行例：Haar多重解像度の境界・シフト・閾値。

Limited to Haar, without longer filters or image compression. General symmetric extension is not assumed orthonormal. Shift invariance is not required; shift-dependent differences are retained.

Other names: ウェーブレット変換, wavelet transform, wavelet method

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/wavelets/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/wavelets/



- Reference: https://doi.org/10.1109/34.192463 — Method-specific source; see the detailed reading for source role and actual review depth.
- Reference: https://www.di.ens.fr/~mallat/papiers/MallatTheory89.pdf — During preparation: title/abstract, Haar example on printed p. 679, selected §III-B/C filter/downsample/inverse-pyramid and border-symmetry prose on p. 681. Extracted formula glyphs were imperfect; no complete proof or numerical-table audit is claimed.
- Reference: https://pywavelets.readthedocs.io/en/latest/ref/signal-extension-modes.html — Periodic and half-sample symmetric extension and the redundancy caveat. This example defines its own append-at-each-odd-level/crop convention; it does not claim PyWavelets coefficient-layout equivalence or require PyWavelets.

## Small fixed-input validation supplements

Fixed educational executions: Haar multiresolution: boundaries, shifts and thresholds.

固定した教育用実行例：Haar多重解像度の境界・シフト・閾値。

- Haar multiresolution: boundaries, shifts and thresholds: https://hrkoyama.github.io/numerical-methods-atlas/validation/haar-mallat-boundary-threshold/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/atlas-approximation-controls-2026-11-25.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/result.json

Common execution records: [{"id": "haar-mallat-boundary-threshold", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/haar-mallat-boundary-threshold/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/haar-mallat-boundary-threshold/?lang=en"}, "kind": "dedicated-supplement"}]

Next: Preserve the fixed scope and qualify extensions separately.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/wavelets/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [有限長信号の離散Haar変換](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#discrete-haar-transform-ja) (`discrete-haar-transform`; haar-mallat-boundary-threshold)

#### 問題の図 (`method-problems-ja`)

##### [Haar多重解像度の境界・シフト・閾値](https://hrkoyama.github.io/numerical-methods-atlas/problems/haar-mallat-boundary-threshold/?lang=ja) (`haar-mallat-boundary-threshold`)

![長さ17・32の小信号に3段Haar分解を適用。1標本シフトと奇数長の境界処理を分けて比較します。 保存配列から作図。 標本添字は物理空間の座標ではありません。境界処理を含む有限長信号の写像です。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/haar-mallat-boundary-threshold-preview.png)

和差フィルタ・間引き・逆ピラミッドを自作。閾値なし・hard・softの3条件を同じ解析係数から再構成します。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/haar-mallat-boundary-threshold/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/haar-mallat-boundary-threshold/?lang=ja#code-ja)

- [Haar多重解像度の境界・シフト・閾値](https://hrkoyama.github.io/numerical-methods-atlas/validation/haar-mallat-boundary-threshold/?lang=ja) (`haar-mallat-boundary-threshold`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/atlas-approximation-controls-2026-11-25.zip)

長さ17・32の小信号に3段Haar分解を適用。1標本シフトと奇数長の境界処理を分けて比較します。


#### 厳密解・参照解 (`method-references-ja`)

##### [Haar多重解像度の境界・シフト・閾値](https://hrkoyama.github.io/numerical-methods-atlas/problems/haar-mallat-boundary-threshold/?lang=ja#references-ja) (`haar-mallat-boundary-threshold`)

- [Haar多重解像度の境界・シフト・閾値](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-haar-mallat-boundary-threshold-ja) (`haar-mallat-boundary-threshold`; 同じ問題の参照; 解析参照)

Haarに限定し長いフィルタや画像圧縮は対象外。一般の対称拡張に正規直交性を仮定しません。シフト不変性は要求せず、シフト別差を保存します。

[既存の参照図](/numerical-methods-atlas/validation/haar-mallat-boundary-threshold/?lang=ja#haar-mallat-boundary-threshold-ja-measurements)

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/wavelets/)
- 保存結果: [この配布版の保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/result.json)
- 検証記録: [配布版の検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/verification.json)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

##### Haar多重解像度の境界・シフト・閾値 (`haar-mallat-boundary-threshold`)

[Haar多重解像度の境界・シフト・閾値](https://hrkoyama.github.io/numerical-methods-atlas/problems/haar-mallat-boundary-threshold/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/haar-mallat-boundary-threshold/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/atlas-approximation-controls-2026-11-25.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/verification.json)

長さ17・32の小信号に3段Haar分解を適用。1標本シフトと奇数長の境界処理を分けて比較します。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

固定した教育用実行例：Haar多重解像度の境界・シフト・閾値。

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/atlas-approximation-controls-2026-11-25.zip)

[配布版の検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/verification.json)

###### 関連ソース

- [/code/validated-examples/2026-11-25/approximation-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/run.py)
- [/code/validated-examples/2026-11-25/approximation-controls/haar.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/haar.py)
- [/code/validated-examples/2026-11-25/approximation-controls/interpolation.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/interpolation.py)
- [/code/validated-examples/2026-11-25/approximation-controls/splines.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/splines.py)
- [/code/validated-examples/2026-11-25/approximation-controls/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/experiments.py)
- [/code/validated-examples/2026-11-25/approximation-controls/io_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/io_contract.py)
- [/code/validated-examples/2026-11-25/approximation-controls/references/haar_matrix.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/references/haar_matrix.py)
- [/code/validated-examples/2026-11-25/approximation-controls/references/polynomials.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/references/polynomials.py)
- [/code/validated-examples/2026-11-25/approximation-controls/references/spline_rational.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/references/spline_rational.py)

###### 配布版のテスト

- [/code/validated-examples/2026-11-25/approximation-controls/test_approximation.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/test_approximation.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q
python run.py --input inputs.json --output output
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Discrete Haar transforms of finite signals](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#discrete-haar-transform-en) (`discrete-haar-transform`; haar-mallat-boundary-threshold)

#### Problem figures (`method-problems-en`)

##### [Haar multiresolution: boundaries, shifts and thresholds](https://hrkoyama.github.io/numerical-methods-atlas/problems/haar-mallat-boundary-threshold/?lang=en) (`haar-mallat-boundary-threshold`)

![Apply three-level Haar analysis to short signals of lengths 17 and 32, separating one-sample shifts from odd-length boundary handling. Drawn from saved arrays. Sample indices are not physical spatial coordinates. This is a finite-signal map with declared boundary handling.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/haar-mallat-boundary-threshold-preview.png)

Implement pair-sum and pair-difference filters, downsampling and inverse pyramids. Reconstruct with no threshold, hard thresholding and soft thresholding from the same analysis coefficients.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/haar-mallat-boundary-threshold/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/haar-mallat-boundary-threshold/?lang=en#code-en)

- [Haar multiresolution: boundaries, shifts and thresholds](https://hrkoyama.github.io/numerical-methods-atlas/validation/haar-mallat-boundary-threshold/?lang=en) (`haar-mallat-boundary-threshold`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/atlas-approximation-controls-2026-11-25.zip)

Apply three-level Haar analysis to short signals of lengths 17 and 32, separating one-sample shifts from odd-length boundary handling.


#### Exact / reference solutions (`method-references-en`)

##### [Haar multiresolution: boundaries, shifts and thresholds](https://hrkoyama.github.io/numerical-methods-atlas/problems/haar-mallat-boundary-threshold/?lang=en#references-en) (`haar-mallat-boundary-threshold`)

- [Haar multiresolution: boundaries, shifts and thresholds](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-haar-mallat-boundary-threshold-en) (`haar-mallat-boundary-threshold`; Same-problem reference; Analytic reference)

Limited to Haar, without longer filters or image compression. General symmetric extension is not assumed orthonormal. Shift invariance is not required; shift-dependent differences are retained.

[Existing reference profile](/numerical-methods-atlas/validation/haar-mallat-boundary-threshold/?lang=en#haar-mallat-boundary-threshold-en-measurements)

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/wavelets/)
- Saved result: [Saved results from this edition](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/result.json)
- Verification receipt: [Edition verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/verification.json)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

##### Haar multiresolution: boundaries, shifts and thresholds (`haar-mallat-boundary-threshold`)

[Haar multiresolution: boundaries, shifts and thresholds](https://hrkoyama.github.io/numerical-methods-atlas/problems/haar-mallat-boundary-threshold/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/haar-mallat-boundary-threshold/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/atlas-approximation-controls-2026-11-25.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/verification.json)

Apply three-level Haar analysis to short signals of lengths 17 and 32, separating one-sample shifts from odd-length boundary handling.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Fixed educational executions: Haar multiresolution: boundaries, shifts and thresholds.

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[Related code edition / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/atlas-approximation-controls-2026-11-25.zip)

[Edition verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/verification.json)

###### Related source

- [/code/validated-examples/2026-11-25/approximation-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/run.py)
- [/code/validated-examples/2026-11-25/approximation-controls/haar.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/haar.py)
- [/code/validated-examples/2026-11-25/approximation-controls/interpolation.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/interpolation.py)
- [/code/validated-examples/2026-11-25/approximation-controls/splines.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/splines.py)
- [/code/validated-examples/2026-11-25/approximation-controls/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/experiments.py)
- [/code/validated-examples/2026-11-25/approximation-controls/io_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/io_contract.py)
- [/code/validated-examples/2026-11-25/approximation-controls/references/haar_matrix.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/references/haar_matrix.py)
- [/code/validated-examples/2026-11-25/approximation-controls/references/polynomials.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/references/polynomials.py)
- [/code/validated-examples/2026-11-25/approximation-controls/references/spline_rational.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/references/spline_rational.py)

###### Package tests

- [/code/validated-examples/2026-11-25/approximation-controls/test_approximation.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/test_approximation.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q
python run.py --input inputs.json --output output
```
