# Haar多重解像度の境界・シフト・閾値

長さ17・32の小信号に3段Haar分解を適用。1標本シフトと奇数長の境界処理を分けて比較します。

**使用手法**

- [ウェーブレット](https://hrkoyama.github.io/numerical-methods-atlas/methods/wavelets/?lang=ja) (`wavelets`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/haar-mallat-boundary-threshold/?lang=ja#haar-mallat-boundary-threshold-ja-algorithm)

和差フィルタ・間引き・逆ピラミッドを自作。閾値なし・hard・softの3条件を同じ解析係数から再構成します。

$$
a_(l+1,k)=(a_(l,2k)+a_(l,2k+1))/sqrt(2)
$$

$$
d_(l+1,k)=(a_(l,2k)-a_(l,2k+1))/sqrt(2)
$$

$$
E_after=E_before+padding^2; ||e||_2^2=||delta_coeff||_2^2 only for square orthogonal transform
$$

- [有限長信号の離散Haar変換](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#discrete-haar-transform-ja) (`discrete-haar-transform`)

奇数長の各段で周期型は先頭、対称型は末尾を1点追加し、再構成時に切り戻します。詳細係数のみ閾値0.2を使用。


**問題の図**

![Haar多重解像度の境界・シフト・閾値：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/haar-mallat-boundary-threshold.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Haar多重解像度の境界・シフト・閾値](https://hrkoyama.github.io/numerical-methods-atlas/problems/haar-mallat-boundary-threshold/?lang=ja) (`haar-mallat-boundary-threshold`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/haar-mallat-boundary-threshold/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/haar-mallat-boundary-threshold/?lang=ja#haar-mallat-boundary-threshold-ja-validation)

12解析・36再構成。独立行列・Fraction/Decimal係数、完全再構成、二乗L2誤差を照合。長さ32のみ直交誤差恒等式を要求し、17点では追加エネルギーを段別保存します。

- [Haar多重解像度の境界・シフト・閾値](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-haar-mallat-boundary-threshold-ja) (`haar-mallat-boundary-threshold`; 同じ問題の参照 · 解析参照)

Haarに限定し長いフィルタや画像圧縮は対象外。一般の対称拡張に正規直交性を仮定しません。シフト不変性は要求せず、シフト別差を保存します。
## 前提・単位・境界

奇数長の各段で周期型は先頭、対称型は末尾を1点追加し、再構成時に切り戻します。詳細係数のみ閾値0.2を使用。

**編集上の補足**

Haarに限定し長いフィルタや画像圧縮は対象外。一般の対称拡張に正規直交性を仮定しません。シフト不変性は要求せず、シフト別差を保存します。 標本添字は物理空間の座標ではありません。境界処理を含む有限長信号の写像です。

## 採用した計算法

和差フィルタ・間引き・逆ピラミッドを自作。閾値なし・hard・softの3条件を同じ解析係数から再構成します。

$$
a_(l+1,k)=(a_(l,2k)+a_(l,2k+1))/sqrt(2)
$$

$$
d_(l+1,k)=(a_(l,2k)-a_(l,2k+1))/sqrt(2)
$$

$$
E_after=E_before+padding^2; ||e||_2^2=||delta_coeff||_2^2 only for square orthogonal transform
$$

## 比較・検証

12解析・36再構成。独立行列・Fraction/Decimal係数、完全再構成、二乗L2誤差を照合。長さ32のみ直交誤差恒等式を要求し、17点では追加エネルギーを段別保存します。

## 確認の限界

Haarに限定し長いフィルタや画像圧縮は対象外。一般の対称拡張に正規直交性を仮定しません。シフト不変性は要求せず、シフト別差を保存します。

## 保存実測値と判定

```json
{
  "metrics": {
    "analysis_records": 12,
    "maximum_reconstruction_l2_squared": 0.6095394266271633,
    "maximum_shift_back_equivariance_l2_squared": 0.23999999999999966
  },
  "checks": {
    "reference:golden-0": true,
    "reference:golden-1": true,
    "periodic-smooth32-periodic:independent-analysis": true,
    "periodic-smooth32-periodic:left-inverse": true,
    "periodic-smooth32-periodic:coefficient-count": true,
    "periodic-smooth32-periodic:padding-energy-ledger": true,
    "periodic-smooth32-periodic-none:finite-and-owned-shape": true,
    "periodic-smooth32-periodic-none:independent-synthesis": true,
    "periodic-smooth32-periodic-none:perfect-reconstruction": true,
    "periodic-smooth32-periodic-none:critical-squared-error-identity": true,
    "periodic-smooth32-periodic-hard:finite-and-owned-shape": true,
    "periodic-smooth32-periodic-hard:independent-synthesis": true,
    "periodic-smooth32-periodic-hard:critical-squared-error-identity": true,
    "periodic-smooth32-periodic-soft:finite-and-owned-shape": true,
    "periodic-smooth32-periodic-soft:independent-synthesis": true,
    "periodic-smooth32-periodic-soft:critical-squared-error-identity": true,
    "periodic-smooth32-symmetric:independent-analysis": true,
    "periodic-smooth32-symmetric:left-inverse": true,
    "periodic-smooth32-symmetric:coefficient-count": true,
    "periodic-smooth32-symmetric:padding-energy-ledger": true,
    "periodic-smooth32-symmetric-none:finite-and-owned-shape": true,
    "periodic-smooth32-symmetric-none:independent-synthesis": true,
    "periodic-smooth32-symmetric-none:perfect-reconstruction": true,
    "periodic-smooth32-symmetric-none:critical-squared-error-identity": true,
    "periodic-smooth32-symmetric-hard:finite-and-owned-shape": true,
    "periodic-smooth32-symmetric-hard:independent-synthesis": true,
    "periodic-smooth32-symmetric-hard:critical-squared-error-identity": true,
    "periodic-smooth32-symmetric-soft:finite-and-owned-shape": true,
    "periodic-smooth32-symmetric-soft:independent-synthesis": true,
    "periodic-smooth32-symmetric-soft:critical-squared-error-identity": true,
    "step32-periodic:independent-analysis": true,
    "step32-periodic:left-inverse": true,
    "step32-periodic:coefficient-count": true,
    "step32-periodic:padding-energy-ledger": true,
    "step32-periodic-none:finite-and-owned-shape": true,
    "step32-periodic-none:independent-synthesis": true,
    "step32-periodic-none:perfect-reconstruction": true,
    "step32-periodic-none:critical-squared-error-identity": true,
    "step32-periodic-hard:finite-and-owned-shape": true,
    "step32-periodic-hard:independent-synthesis": true,
    "step32-periodic-hard:critical-squared-error-identity": true,
    "step32-periodic-soft:finite-and-owned-shape": true,
    "step32-periodic-soft:independent-synthesis": true,
    "step32-periodic-soft:critical-squared-error-identity": true,
    "step32-symmetric:independent-analysis": true,
    "step32-symmetric:left-inverse": true,
    "step32-symmetric:coefficient-count": true,
    "step32-symmetric:padding-energy-ledger": true,
    "step32-symmetric-none:finite-and-owned-shape": true,
    "step32-symmetric-none:independent-synthesis": true,
    "step32-symmetric-none:perfect-reconstruction": true,
    "step32-symmetric-none:critical-squared-error-identity": true,
    "step32-symmetric-hard:finite-and-owned-shape": true,
    "step32-symmetric-hard:independent-synthesis": true,
    "step32-symmetric-hard:critical-squared-error-identity": true,
    "step32-symmetric-soft:finite-and-owned-shape": true,
    "step32-symmetric-soft:independent-synthesis": true,
    "step32-symmetric-soft:critical-squared-error-identity": true,
    "ramp17-periodic:independent-analysis": true,
    "ramp17-periodic:left-inverse": true,
    "ramp17-periodic:coefficient-count": true,
    "ramp17-periodic:padding-energy-ledger": true,
    "ramp17-periodic-none:finite-and-owned-shape": true,
    "ramp17-periodic-none:independent-synthesis": true,
    "ramp17-periodic-none:perfect-reconstruction": true,
    "ramp17-periodic-hard:finite-and-owned-shape": true,
    "ramp17-periodic-hard:independent-synthesis": true,
    "ramp17-periodic-soft:finite-and-owned-shape": true,
    "ramp17-periodic-soft:independent-synthesis": true,
    "ramp17-symmetric:independent-analysis": true,
    "ramp17-symmetric:left-inverse": true,
    "ramp17-symmetric:coefficient-count": true,
    "ramp17-symmetric:padding-energy-ledger": true,
    "ramp17-symmetric-none:finite-and-owned-shape": true,
    "ramp17-symmetric-none:independent-synthesis": true,
    "ramp17-symmetric-none:perfect-reconstruction": true,
    "ramp17-symmetric-hard:finite-and-owned-shape": true,
    "ramp17-symmetric-hard:independent-synthesis": true,
    "ramp17-symmetric-soft:finite-and-owned-shape": true,
    "ramp17-symmetric-soft:independent-synthesis": true,
    "step17-periodic:independent-analysis": true,
    "step17-periodic:left-inverse": true,
    "step17-periodic:coefficient-count": true,
    "step17-periodic:padding-energy-ledger": true,
    "step17-periodic-none:finite-and-owned-shape": true,
    "step17-periodic-none:independent-synthesis": true,
    "step17-periodic-none:perfect-reconstruction": true,
    "step17-periodic-hard:finite-and-owned-shape": true,
    "step17-periodic-hard:independent-synthesis": true,
    "step17-periodic-soft:finite-and-owned-shape": true,
    "step17-periodic-soft:independent-synthesis": true,
    "step17-symmetric:independent-analysis": true,
    "step17-symmetric:left-inverse": true,
    "step17-symmetric:coefficient-count": true,
    "step17-symmetric:padding-energy-ledger": true,
    "step17-symmetric-none:finite-and-owned-shape": true,
    "step17-symmetric-none:independent-synthesis": true,
    "step17-symmetric-none:perfect-reconstruction": true,
    "step17-symmetric-hard:finite-and-owned-shape": true,
    "step17-symmetric-hard:independent-synthesis": true,
    "step17-symmetric-soft:finite-and-owned-shape": true,
    "step17-symmetric-soft:independent-synthesis": true,
    "step32-shift1-periodic:independent-analysis": true,
    "step32-shift1-periodic:left-inverse": true,
    "step32-shift1-periodic:coefficient-count": true,
    "step32-shift1-periodic:padding-energy-ledger": true,
    "step32-shift1-periodic-none:finite-and-owned-shape": true,
    "step32-shift1-periodic-none:independent-synthesis": true,
    "step32-shift1-periodic-none:perfect-reconstruction": true,
    "step32-shift1-periodic-none:critical-squared-error-identity": true,
    "step32-shift1-periodic-hard:finite-and-owned-shape": true,
    "step32-shift1-periodic-hard:independent-synthesis": true,
    "step32-shift1-periodic-hard:critical-squared-error-identity": true,
    "step32-shift1-periodic-soft:finite-and-owned-shape": true,
    "step32-shift1-periodic-soft:independent-synthesis": true,
    "step32-shift1-periodic-soft:critical-squared-error-identity": true,
    "step32-shift1-symmetric:independent-analysis": true,
    "step32-shift1-symmetric:left-inverse": true,
    "step32-shift1-symmetric:coefficient-count": true,
    "step32-shift1-symmetric:padding-energy-ledger": true,
    "step32-shift1-symmetric-none:finite-and-owned-shape": true,
    "step32-shift1-symmetric-none:independent-synthesis": true,
    "step32-shift1-symmetric-none:perfect-reconstruction": true,
    "step32-shift1-symmetric-none:critical-squared-error-identity": true,
    "step32-shift1-symmetric-hard:finite-and-owned-shape": true,
    "step32-shift1-symmetric-hard:independent-synthesis": true,
    "step32-shift1-symmetric-hard:critical-squared-error-identity": true,
    "step32-shift1-symmetric-soft:finite-and-owned-shape": true,
    "step32-shift1-symmetric-soft:independent-synthesis": true,
    "step32-shift1-symmetric-soft:critical-squared-error-identity": true,
    "step17-shift1-periodic:independent-analysis": true,
    "step17-shift1-periodic:left-inverse": true,
    "step17-shift1-periodic:coefficient-count": true,
    "step17-shift1-periodic:padding-energy-ledger": true,
    "step17-shift1-periodic-none:finite-and-owned-shape": true,
    "step17-shift1-periodic-none:independent-synthesis": true,
    "step17-shift1-periodic-none:perfect-reconstruction": true,
    "step17-shift1-periodic-hard:finite-and-owned-shape": true,
    "step17-shift1-periodic-hard:independent-synthesis": true,
    "step17-shift1-periodic-soft:finite-and-owned-shape": true,
    "step17-shift1-periodic-soft:independent-synthesis": true,
    "step17-shift1-symmetric:independent-analysis": true,
    "step17-shift1-symmetric:left-inverse": true,
    "step17-shift1-symmetric:coefficient-count": true,
    "step17-shift1-symmetric:padding-energy-ledger": true,
    "step17-shift1-symmetric-none:finite-and-owned-shape": true,
    "step17-shift1-symmetric-none:independent-synthesis": true,
    "step17-shift1-symmetric-none:perfect-reconstruction": true,
    "step17-shift1-symmetric-hard:finite-and-owned-shape": true,
    "step17-shift1-symmetric-hard:independent-synthesis": true,
    "step17-shift1-symmetric-soft:finite-and-owned-shape": true,
    "step17-shift1-symmetric-soft:independent-synthesis": true,
    "fixed-analysis-and-reconstruction-count": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/haar-mallat-boundary-threshold/index.json

![長さ17・32の小信号に3段Haar分解を適用。1標本シフトと奇数長の境界処理を分けて比較します。 保存配列から作図。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/haar-mallat-boundary-threshold-preview.png)

長さ17・32の小信号に3段Haar分解を適用。1標本シフトと奇数長の境界処理を分けて比較します。 保存配列から作図。

![保存済み誤差・導関数または二乗ノルムを別表示。各境界・表現の適用範囲は本文を参照。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/haar-mallat-boundary-threshold-diagnostics.png)

保存済み誤差・導関数または二乗ノルムを別表示。各境界・表現の適用範囲は本文を参照。

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/atlas-approximation-controls-2026-11-25.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

## 出典と確認範囲

- S. Mallat, A Theory for Multiresolution Signal Decomposition: The Wavelet Representation [accessed 2026-11-24]. https://www.di.ens.fr/~mallat/papiers/MallatTheory89.pdf; review_level=primary-paper-selected-body
During preparation: title/abstract, Haar example on printed p. 679, selected §III-B/C filter/downsample/inverse-pyramid and border-symmetry prose on p. 681. Extracted formula glyphs were imperfect; no complete proof or numerical-table audit is claimed.

- PyWavelets documentation: Signal extension modes [accessed 2026-11-25]. https://pywavelets.readthedocs.io/en/latest/ref/signal-extension-modes.html; review_level=official-documentation-selected-terminology
Periodic and half-sample symmetric extension and the redundancy caveat. This example defines its own append-at-each-odd-level/crop convention; it does not claim PyWavelets coefficient-layout equivalence or require PyWavelets.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Haar multiresolution: boundaries, shifts and thresholds

Apply three-level Haar analysis to short signals of lengths 17 and 32, separating one-sample shifts from odd-length boundary handling.

**Methods used**

- [Wavelets](https://hrkoyama.github.io/numerical-methods-atlas/methods/wavelets/?lang=en) (`wavelets`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/haar-mallat-boundary-threshold/?lang=en#haar-mallat-boundary-threshold-en-algorithm)

Implement pair-sum and pair-difference filters, downsampling and inverse pyramids. Reconstruct with no threshold, hard thresholding and soft thresholding from the same analysis coefficients.

$$
a_(l+1,k)=(a_(l,2k)+a_(l,2k+1))/sqrt(2)
$$

$$
d_(l+1,k)=(a_(l,2k)-a_(l,2k+1))/sqrt(2)
$$

$$
E_after=E_before+padding^2; ||e||_2^2=||delta_coeff||_2^2 only for square orthogonal transform
$$

- [Discrete Haar transforms of finite signals](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#discrete-haar-transform-en) (`discrete-haar-transform`)

At each odd-length level append the first sample for periodic extension or the last for symmetric extension, then crop during synthesis. Apply threshold 0.2 only to detail coefficients.


**Problem figure**

![Haar multiresolution: boundaries, shifts and thresholds: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/haar-mallat-boundary-threshold.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Haar multiresolution: boundaries, shifts and thresholds](https://hrkoyama.github.io/numerical-methods-atlas/problems/haar-mallat-boundary-threshold/?lang=en) (`haar-mallat-boundary-threshold`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/haar-mallat-boundary-threshold/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/haar-mallat-boundary-threshold/?lang=en#haar-mallat-boundary-threshold-en-validation)

Use twelve analyses and thirty-six reconstructions. Check independent matrices, Fraction/Decimal coefficients, perfect reconstruction and squared L2 errors. Require the orthogonal error identity only at length 32; retain level-by-level padding energy at length 17.

- [Haar multiresolution: boundaries, shifts and thresholds](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-haar-mallat-boundary-threshold-en) (`haar-mallat-boundary-threshold`; Same-problem reference · Analytic reference)

Limited to Haar, without longer filters or image compression. General symmetric extension is not assumed orthonormal. Shift invariance is not required; shift-dependent differences are retained.
## Assumptions, units and boundaries

At each odd-length level append the first sample for periodic extension or the last for symmetric extension, then crop during synthesis. Apply threshold 0.2 only to detail coefficients.

**Editorial clarification**

Limited to Haar, without longer filters or image compression. General symmetric extension is not assumed orthonormal. Shift invariance is not required; shift-dependent differences are retained. Sample indices are not physical spatial coordinates. This is a finite-signal map with declared boundary handling.

## Adopted numerical method

Implement pair-sum and pair-difference filters, downsampling and inverse pyramids. Reconstruct with no threshold, hard thresholding and soft thresholding from the same analysis coefficients.

$$
a_(l+1,k)=(a_(l,2k)+a_(l,2k+1))/sqrt(2)
$$

$$
d_(l+1,k)=(a_(l,2k)-a_(l,2k+1))/sqrt(2)
$$

$$
E_after=E_before+padding^2; ||e||_2^2=||delta_coeff||_2^2 only for square orthogonal transform
$$

## References and validation

Use twelve analyses and thirty-six reconstructions. Check independent matrices, Fraction/Decimal coefficients, perfect reconstruction and squared L2 errors. Require the orthogonal error identity only at length 32; retain level-by-level padding energy at length 17.

## Limits

Limited to Haar, without longer filters or image compression. General symmetric extension is not assumed orthonormal. Shift invariance is not required; shift-dependent differences are retained.

## Stored measurements and decisions

```json
{
  "metrics": {
    "analysis_records": 12,
    "maximum_reconstruction_l2_squared": 0.6095394266271633,
    "maximum_shift_back_equivariance_l2_squared": 0.23999999999999966
  },
  "checks": {
    "reference:golden-0": true,
    "reference:golden-1": true,
    "periodic-smooth32-periodic:independent-analysis": true,
    "periodic-smooth32-periodic:left-inverse": true,
    "periodic-smooth32-periodic:coefficient-count": true,
    "periodic-smooth32-periodic:padding-energy-ledger": true,
    "periodic-smooth32-periodic-none:finite-and-owned-shape": true,
    "periodic-smooth32-periodic-none:independent-synthesis": true,
    "periodic-smooth32-periodic-none:perfect-reconstruction": true,
    "periodic-smooth32-periodic-none:critical-squared-error-identity": true,
    "periodic-smooth32-periodic-hard:finite-and-owned-shape": true,
    "periodic-smooth32-periodic-hard:independent-synthesis": true,
    "periodic-smooth32-periodic-hard:critical-squared-error-identity": true,
    "periodic-smooth32-periodic-soft:finite-and-owned-shape": true,
    "periodic-smooth32-periodic-soft:independent-synthesis": true,
    "periodic-smooth32-periodic-soft:critical-squared-error-identity": true,
    "periodic-smooth32-symmetric:independent-analysis": true,
    "periodic-smooth32-symmetric:left-inverse": true,
    "periodic-smooth32-symmetric:coefficient-count": true,
    "periodic-smooth32-symmetric:padding-energy-ledger": true,
    "periodic-smooth32-symmetric-none:finite-and-owned-shape": true,
    "periodic-smooth32-symmetric-none:independent-synthesis": true,
    "periodic-smooth32-symmetric-none:perfect-reconstruction": true,
    "periodic-smooth32-symmetric-none:critical-squared-error-identity": true,
    "periodic-smooth32-symmetric-hard:finite-and-owned-shape": true,
    "periodic-smooth32-symmetric-hard:independent-synthesis": true,
    "periodic-smooth32-symmetric-hard:critical-squared-error-identity": true,
    "periodic-smooth32-symmetric-soft:finite-and-owned-shape": true,
    "periodic-smooth32-symmetric-soft:independent-synthesis": true,
    "periodic-smooth32-symmetric-soft:critical-squared-error-identity": true,
    "step32-periodic:independent-analysis": true,
    "step32-periodic:left-inverse": true,
    "step32-periodic:coefficient-count": true,
    "step32-periodic:padding-energy-ledger": true,
    "step32-periodic-none:finite-and-owned-shape": true,
    "step32-periodic-none:independent-synthesis": true,
    "step32-periodic-none:perfect-reconstruction": true,
    "step32-periodic-none:critical-squared-error-identity": true,
    "step32-periodic-hard:finite-and-owned-shape": true,
    "step32-periodic-hard:independent-synthesis": true,
    "step32-periodic-hard:critical-squared-error-identity": true,
    "step32-periodic-soft:finite-and-owned-shape": true,
    "step32-periodic-soft:independent-synthesis": true,
    "step32-periodic-soft:critical-squared-error-identity": true,
    "step32-symmetric:independent-analysis": true,
    "step32-symmetric:left-inverse": true,
    "step32-symmetric:coefficient-count": true,
    "step32-symmetric:padding-energy-ledger": true,
    "step32-symmetric-none:finite-and-owned-shape": true,
    "step32-symmetric-none:independent-synthesis": true,
    "step32-symmetric-none:perfect-reconstruction": true,
    "step32-symmetric-none:critical-squared-error-identity": true,
    "step32-symmetric-hard:finite-and-owned-shape": true,
    "step32-symmetric-hard:independent-synthesis": true,
    "step32-symmetric-hard:critical-squared-error-identity": true,
    "step32-symmetric-soft:finite-and-owned-shape": true,
    "step32-symmetric-soft:independent-synthesis": true,
    "step32-symmetric-soft:critical-squared-error-identity": true,
    "ramp17-periodic:independent-analysis": true,
    "ramp17-periodic:left-inverse": true,
    "ramp17-periodic:coefficient-count": true,
    "ramp17-periodic:padding-energy-ledger": true,
    "ramp17-periodic-none:finite-and-owned-shape": true,
    "ramp17-periodic-none:independent-synthesis": true,
    "ramp17-periodic-none:perfect-reconstruction": true,
    "ramp17-periodic-hard:finite-and-owned-shape": true,
    "ramp17-periodic-hard:independent-synthesis": true,
    "ramp17-periodic-soft:finite-and-owned-shape": true,
    "ramp17-periodic-soft:independent-synthesis": true,
    "ramp17-symmetric:independent-analysis": true,
    "ramp17-symmetric:left-inverse": true,
    "ramp17-symmetric:coefficient-count": true,
    "ramp17-symmetric:padding-energy-ledger": true,
    "ramp17-symmetric-none:finite-and-owned-shape": true,
    "ramp17-symmetric-none:independent-synthesis": true,
    "ramp17-symmetric-none:perfect-reconstruction": true,
    "ramp17-symmetric-hard:finite-and-owned-shape": true,
    "ramp17-symmetric-hard:independent-synthesis": true,
    "ramp17-symmetric-soft:finite-and-owned-shape": true,
    "ramp17-symmetric-soft:independent-synthesis": true,
    "step17-periodic:independent-analysis": true,
    "step17-periodic:left-inverse": true,
    "step17-periodic:coefficient-count": true,
    "step17-periodic:padding-energy-ledger": true,
    "step17-periodic-none:finite-and-owned-shape": true,
    "step17-periodic-none:independent-synthesis": true,
    "step17-periodic-none:perfect-reconstruction": true,
    "step17-periodic-hard:finite-and-owned-shape": true,
    "step17-periodic-hard:independent-synthesis": true,
    "step17-periodic-soft:finite-and-owned-shape": true,
    "step17-periodic-soft:independent-synthesis": true,
    "step17-symmetric:independent-analysis": true,
    "step17-symmetric:left-inverse": true,
    "step17-symmetric:coefficient-count": true,
    "step17-symmetric:padding-energy-ledger": true,
    "step17-symmetric-none:finite-and-owned-shape": true,
    "step17-symmetric-none:independent-synthesis": true,
    "step17-symmetric-none:perfect-reconstruction": true,
    "step17-symmetric-hard:finite-and-owned-shape": true,
    "step17-symmetric-hard:independent-synthesis": true,
    "step17-symmetric-soft:finite-and-owned-shape": true,
    "step17-symmetric-soft:independent-synthesis": true,
    "step32-shift1-periodic:independent-analysis": true,
    "step32-shift1-periodic:left-inverse": true,
    "step32-shift1-periodic:coefficient-count": true,
    "step32-shift1-periodic:padding-energy-ledger": true,
    "step32-shift1-periodic-none:finite-and-owned-shape": true,
    "step32-shift1-periodic-none:independent-synthesis": true,
    "step32-shift1-periodic-none:perfect-reconstruction": true,
    "step32-shift1-periodic-none:critical-squared-error-identity": true,
    "step32-shift1-periodic-hard:finite-and-owned-shape": true,
    "step32-shift1-periodic-hard:independent-synthesis": true,
    "step32-shift1-periodic-hard:critical-squared-error-identity": true,
    "step32-shift1-periodic-soft:finite-and-owned-shape": true,
    "step32-shift1-periodic-soft:independent-synthesis": true,
    "step32-shift1-periodic-soft:critical-squared-error-identity": true,
    "step32-shift1-symmetric:independent-analysis": true,
    "step32-shift1-symmetric:left-inverse": true,
    "step32-shift1-symmetric:coefficient-count": true,
    "step32-shift1-symmetric:padding-energy-ledger": true,
    "step32-shift1-symmetric-none:finite-and-owned-shape": true,
    "step32-shift1-symmetric-none:independent-synthesis": true,
    "step32-shift1-symmetric-none:perfect-reconstruction": true,
    "step32-shift1-symmetric-none:critical-squared-error-identity": true,
    "step32-shift1-symmetric-hard:finite-and-owned-shape": true,
    "step32-shift1-symmetric-hard:independent-synthesis": true,
    "step32-shift1-symmetric-hard:critical-squared-error-identity": true,
    "step32-shift1-symmetric-soft:finite-and-owned-shape": true,
    "step32-shift1-symmetric-soft:independent-synthesis": true,
    "step32-shift1-symmetric-soft:critical-squared-error-identity": true,
    "step17-shift1-periodic:independent-analysis": true,
    "step17-shift1-periodic:left-inverse": true,
    "step17-shift1-periodic:coefficient-count": true,
    "step17-shift1-periodic:padding-energy-ledger": true,
    "step17-shift1-periodic-none:finite-and-owned-shape": true,
    "step17-shift1-periodic-none:independent-synthesis": true,
    "step17-shift1-periodic-none:perfect-reconstruction": true,
    "step17-shift1-periodic-hard:finite-and-owned-shape": true,
    "step17-shift1-periodic-hard:independent-synthesis": true,
    "step17-shift1-periodic-soft:finite-and-owned-shape": true,
    "step17-shift1-periodic-soft:independent-synthesis": true,
    "step17-shift1-symmetric:independent-analysis": true,
    "step17-shift1-symmetric:left-inverse": true,
    "step17-shift1-symmetric:coefficient-count": true,
    "step17-shift1-symmetric:padding-energy-ledger": true,
    "step17-shift1-symmetric-none:finite-and-owned-shape": true,
    "step17-shift1-symmetric-none:independent-synthesis": true,
    "step17-shift1-symmetric-none:perfect-reconstruction": true,
    "step17-shift1-symmetric-hard:finite-and-owned-shape": true,
    "step17-shift1-symmetric-hard:independent-synthesis": true,
    "step17-shift1-symmetric-soft:finite-and-owned-shape": true,
    "step17-shift1-symmetric-soft:independent-synthesis": true,
    "fixed-analysis-and-reconstruction-count": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/haar-mallat-boundary-threshold/index.json

![Apply three-level Haar analysis to short signals of lengths 17 and 32, separating one-sample shifts from odd-length boundary handling. Drawn from saved arrays.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/haar-mallat-boundary-threshold-preview.png)

Apply three-level Haar analysis to short signals of lengths 17 and 32, separating one-sample shifts from odd-length boundary handling. Drawn from saved arrays.

![Saved errors, derivatives or squared norms shown separately. The text states the scope of each boundary and representation.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/haar-mallat-boundary-threshold-diagnostics.png)

Saved errors, derivatives or squared norms shown separately. The text states the scope of each boundary and representation.

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/atlas-approximation-controls-2026-11-25.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

## Sources and review scope

- S. Mallat, A Theory for Multiresolution Signal Decomposition: The Wavelet Representation [accessed 2026-11-24]. https://www.di.ens.fr/~mallat/papiers/MallatTheory89.pdf; review_level=primary-paper-selected-body
During preparation: title/abstract, Haar example on printed p. 679, selected §III-B/C filter/downsample/inverse-pyramid and border-symmetry prose on p. 681. Extracted formula glyphs were imperfect; no complete proof or numerical-table audit is claimed.

- PyWavelets documentation: Signal extension modes [accessed 2026-11-25]. https://pywavelets.readthedocs.io/en/latest/ref/signal-extension-modes.html; review_level=official-documentation-selected-terminology
Periodic and half-sample symmetric extension and the redundancy caveat. This example defines its own append-at-each-odd-level/crop convention; it does not claim PyWavelets coefficient-layout equivalence or require PyWavelets.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
