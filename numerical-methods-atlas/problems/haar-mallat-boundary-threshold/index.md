# Haar多重解像度の境界・シフト・閾値 / Haar multiresolution: boundaries, shifts and thresholds

https://hrkoyama.github.io/numerical-methods-atlas/problems/haar-mallat-boundary-threshold/

## 日本語

[長さ17・32の小信号に3段Haar分解を適用。1標本シフトと奇数長の境界処理を分けて比較します。 保存配列から作図。 標本添字は物理空間の座標ではありません。境界処理を含む有限長信号の写像です。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/haar-mallat-boundary-threshold-preview.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-approximation-controls/#haar-mallat-boundary-threshold) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#haar-mallat-boundary-threshold)

### 方程式・問題の定義

奇数長の各段で周期型は先頭、対称型は末尾を1点追加し、再構成時に切り戻します。詳細係数のみ閾値0.2を使用。

#### [有限長信号の離散Haar変換](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#discrete-haar-transform-ja)

$$
\binom{a^{\prime}}d=\frac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}\binom ab
$$

$$
S_NA_N=I_N,\quad\|A_Nx\|_2^2=\|x\|_2^2+\sum_\ell p_\ell^2
$$

奇数長の追加標本と切戻しを含む有限写像です。冗長拡張全体の直交性は仮定しません。

#### Haar多重解像度の境界・シフト・閾値

補助実行例 · 実行例の定義・検証式

$$
a_(l+1,k)=(a_(l,2k)+a_(l,2k+1))/sqrt(2)
$$

$$
d_(l+1,k)=(a_(l,2k)-a_(l,2k+1))/sqrt(2)
$$

$$
E_after=E_before+padding^2; ||e||_2^2=||delta_coeff||_2^2 only for square orthogonal transform
$$

長さ17・32の小信号に3段Haar分解を適用。1標本シフトと奇数長の境界処理を分けて比較します。

### 厳密解・参照解

12解析・36再構成。独立行列・Fraction/Decimal係数、完全再構成、二乗L2誤差を照合。長さ32のみ直交誤差恒等式を要求し、17点では追加エネルギーを段別保存します。

#### [Haar多重解像度の境界・シフト・閾値](https://hrkoyama.github.io/numerical-methods-atlas/validation/haar-mallat-boundary-threshold/?lang=ja#haar-mallat-boundary-threshold-ja-measurements)

解析解 · 同じ問題の参照

a_{\ell+1,k}=\frac{a_{\ell,2k}+a_{\ell,2k+1}}{\sqrt2},\quad d_{\ell+1,k}=\frac{a_{\ell,2k}-a_{\ell,2k+1}}{\sqrt2};\quad E_{\rm after}=E_{\rm before}+p_\ell^2,\quad \|e\|_2^2=\|\Delta c\|_2^2\ \text{for the square orthogonal case only}

奇数長の各段で周期型は先頭、対称型は末尾を1点追加し、再構成時に切り戻します。詳細係数のみ閾値0.2を使用。

Haarに限定し長いフィルタや画像圧縮は対象外。一般の対称拡張に正規直交性を仮定しません。シフト不変性は要求せず、シフト別差を保存します。

#### Haar多重解像度の境界・シフト・閾値

12解析・36再構成。独立行列・Fraction/Decimal係数、完全再構成、二乗L2誤差を照合。長さ32のみ直交誤差恒等式を要求し、17点では追加エネルギーを段別保存します。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/haar-mallat-boundary-threshold/?lang=ja)

### 計算法

和差フィルタ・間引き・逆ピラミッドを自作。閾値なし・hard・softの3条件を同じ解析係数から再構成します。

- [ウェーブレット](https://hrkoyama.github.io/numerical-methods-atlas/methods/wavelets/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [Haar多重解像度の境界・シフト・閾値](https://hrkoyama.github.io/numerical-methods-atlas/validation/haar-mallat-boundary-threshold/?lang=ja)

補助実行例

長さ17・32の小信号に3段Haar分解を適用。1標本シフトと奇数長の境界処理を分けて比較します。

奇数長の各段で周期型は先頭、対称型は末尾を1点追加し、再構成時に切り戻します。詳細係数のみ閾値0.2を使用。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/atlas-approximation-controls-2026-11-25.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

Haarに限定し長いフィルタや画像圧縮は対象外。一般の対称拡張に正規直交性を仮定しません。シフト不変性は要求せず、シフト別差を保存します。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-25/approximation-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/run.py)
- [/code/validated-examples/2026-11-25/approximation-controls/haar.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/haar.py)
- [/code/validated-examples/2026-11-25/approximation-controls/test_approximation.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/test_approximation.py)

## English

[Apply three-level Haar analysis to short signals of lengths 17 and 32, separating one-sample shifts from odd-length boundary handling. Drawn from saved arrays. Sample indices are not physical spatial coordinates. This is a finite-signal map with declared boundary handling.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/haar-mallat-boundary-threshold-preview.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-approximation-controls/#haar-mallat-boundary-threshold) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#haar-mallat-boundary-threshold-en)

### Equations and problem definitions

At each odd-length level append the first sample for periodic extension or the last for symmetric extension, then crop during synthesis. Apply threshold 0.2 only to detail coefficients.

#### [Discrete Haar transforms of finite signals](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#discrete-haar-transform-en)

$$
\binom{a^{\prime}}d=\frac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}\binom ab
$$

$$
S_NA_N=I_N,\quad\|A_Nx\|_2^2=\|x\|_2^2+\sum_\ell p_\ell^2
$$

A finite map including odd-length padding and cropping; global orthogonality is not assumed for redundant extensions.

#### Haar multiresolution: boundaries, shifts and thresholds

Supplementary execution example · Example definition or validation formula

$$
a_(l+1,k)=(a_(l,2k)+a_(l,2k+1))/sqrt(2)
$$

$$
d_(l+1,k)=(a_(l,2k)-a_(l,2k+1))/sqrt(2)
$$

$$
E_after=E_before+padding^2; ||e||_2^2=||delta_coeff||_2^2 only for square orthogonal transform
$$

Apply three-level Haar analysis to short signals of lengths 17 and 32, separating one-sample shifts from odd-length boundary handling.

### Exact and reference solutions

Use twelve analyses and thirty-six reconstructions. Check independent matrices, Fraction/Decimal coefficients, perfect reconstruction and squared L2 errors. Require the orthogonal error identity only at length 32; retain level-by-level padding energy at length 17.

#### [Haar multiresolution: boundaries, shifts and thresholds](https://hrkoyama.github.io/numerical-methods-atlas/validation/haar-mallat-boundary-threshold/?lang=en#haar-mallat-boundary-threshold-en-measurements)

Analytic reference · Reference for the same problem

a_{\ell+1,k}=\frac{a_{\ell,2k}+a_{\ell,2k+1}}{\sqrt2},\quad d_{\ell+1,k}=\frac{a_{\ell,2k}-a_{\ell,2k+1}}{\sqrt2};\quad E_{\rm after}=E_{\rm before}+p_\ell^2,\quad \|e\|_2^2=\|\Delta c\|_2^2\ \text{for the square orthogonal case only}

At each odd-length level append the first sample for periodic extension or the last for symmetric extension, then crop during synthesis. Apply threshold 0.2 only to detail coefficients.

Limited to Haar, without longer filters or image compression. General symmetric extension is not assumed orthonormal. Shift invariance is not required; shift-dependent differences are retained.

#### Haar multiresolution: boundaries, shifts and thresholds

Use twelve analyses and thirty-six reconstructions. Check independent matrices, Fraction/Decimal coefficients, perfect reconstruction and squared L2 errors. Require the orthogonal error identity only at length 32; retain level-by-level padding energy at length 17.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/haar-mallat-boundary-threshold/?lang=en)

### Numerical methods

Implement pair-sum and pair-difference filters, downsampling and inverse pyramids. Reconstruct with no threshold, hard thresholding and soft thresholding from the same analysis coefficients.

- [Wavelets](https://hrkoyama.github.io/numerical-methods-atlas/methods/wavelets/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Haar multiresolution: boundaries, shifts and thresholds](https://hrkoyama.github.io/numerical-methods-atlas/validation/haar-mallat-boundary-threshold/?lang=en)

Supplementary execution example

Apply three-level Haar analysis to short signals of lengths 17 and 32, separating one-sample shifts from odd-length boundary handling.

At each odd-length level append the first sample for periodic extension or the last for symmetric extension, then crop during synthesis. Apply threshold 0.2 only to detail coefficients.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/atlas-approximation-controls-2026-11-25.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

Limited to Haar, without longer filters or image compression. General symmetric extension is not assumed orthonormal. Shift invariance is not required; shift-dependent differences are retained.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-25/approximation-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/run.py)
- [/code/validated-examples/2026-11-25/approximation-controls/haar.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/haar.py)
- [/code/validated-examples/2026-11-25/approximation-controls/test_approximation.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/test_approximation.py)
