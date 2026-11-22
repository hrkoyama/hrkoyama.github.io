# Householder QRと片側Jacobi SVD：直交性・階数・最小二乗 / Householder QR and one-sided Jacobi SVD: orthogonality, rank and least squares

https://hrkoyama.github.io/numerical-methods-atlas/problems/matrix-factorization/

## 日本語

[固定した満階数・階数落ち行列で、Householder QR・片側Jacobi SVDの再構成、保持階数の直交性、LAPACKとの差を保存値から図示。丸めゼロは1e−16へ置いて表示。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/results/qr-svd-factorization.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-foundations/#qr-svd-factorization) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#matrix-factorization)

### 方程式・問題の定義

QR・SVDによる行列分解・最小二乗問題です。独立した物理モデル式は割り当てません。

#### Householder QRと片側Jacobi SVD：直交性・階数・最小二乗

補助実行例 · 実行例の定義・検証式

$$
A=QR,\quad Q^TQ=I
$$

$$
A\simeq U_r\Sigma_rV_r^T,\quad x_{\min}=V_r\Sigma_r^{-1}U_r^Tb
$$

実の縦長行列に対するHouseholder QRと片側Jacobi SVDを自作し、通常行列・列スケール差10⁶の行列・階数落ち行列を検査します。独立LAPACKの特異値と最小ノルム最小二乗解を照合します。

#### QR/SVD：既定特異値・摂動増幅・数値階数

補助実行例 · 実行例の定義・検証式

$$
A=U\operatorname{diag}(2^{-qj})V^T,\quad\kappa_2(A)=2^{3q}
$$

$$
\delta b=\eta u_{\min},\quad\delta x=\eta\sigma_{\min}^{-1}v_{\min}
$$

二進で厳密に表現できる16×4行列の条件数を1から2³⁶まで変え、再構成誤差と解誤差を分けます。実際のbinary64入力に対し別環境で実行した80/120桁参照とLAPACKを比較します。

### 厳密解・参照解

独立NumPy/SciPy参照、行列再構成・直交性・特異値・階数・最小二乗残差を確認します。PDEの参照解カードとは別の線形代数検証です。 別版では条件数、右辺摂動、数値階数の閾値を変え、残差と係数の前進誤差を分けます。LAPACKと実際の二進入力から作る高精度参照の役割を区別し、QR／SVD全般や任意の悪条件行列の保証にはしません。

#### Householder QRと片側Jacobi SVD：直交性・階数・最小二乗

QR/SVDの相対再構成誤差、Q/U/Vの直交性、SciPy LAPACK gesddの特異値、gelsd/gelsyの最小二乗解・階数、正規方程式の停留残差を比較します。特異ベクトルの符号は比較せず、零行列と予算切れも検査します。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/qr-svd-factorization/?lang=ja)

#### QR/SVD：既定特異値・摂動増幅・数値階数

再構成・直交性・特異値・右辺摂動による解差・最小二乗停留残差・厳密階数2の対照を保存します。高精度参照は実二進入力を整数比へ変換し、mpmath 1.3.0のSVDとQRを独立実行済みです。SHAと全4入力・両精度の完全性を実行時に検査し、不一致を解析解へ置換しません。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/qr-svd-conditioning/?lang=ja)

### 計算法

この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。

- [QR・SVD・最小二乗](https://hrkoyama.github.io/numerical-methods-atlas/methods/qr-svd/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [Householder QRと片側Jacobi SVD：直交性・階数・最小二乗](https://hrkoyama.github.io/numerical-methods-atlas/validation/qr-svd-factorization/?lang=ja)

補助実行例

実の縦長行列に対するHouseholder QRと片側Jacobi SVDを自作し、通常行列・列スケール差10⁶の行列・階数落ち行列を検査します。独立LAPACKの特異値と最小ノルム最小二乗解を照合します。

m≥nの小さな実行列が対象です。SVDの数値階数は最大特異値に対する相対しきい値10⁻¹²で定義し、零特異値方向を除くcompact因子を返します。QRは列ピボットなしで、階数判定には用いません。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/atlas-foundations-2026-11-22.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

完全なLAPACK置換、複素行列、横長行列、任意の極端なスケール、最適な相対特異値精度を保証しません。10⁻¹²未満の特異値は入力した数値階数の規約で打ち切るため、数学的な厳密階数と区別します。Demmel–Veselićの精度定理の全条件を実証したとは主張しません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-22/foundations/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/run.py)
- [/code/validated-examples/2026-11-22/foundations/test_foundations.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/test_foundations.py)

#### [QR/SVD：既定特異値・摂動増幅・数値階数](https://hrkoyama.github.io/numerical-methods-atlas/validation/qr-svd-conditioning/?lang=ja)

補助実行例

二進で厳密に表現できる16×4行列の条件数を1から2³⁶まで変え、再構成誤差と解誤差を分けます。実際のbinary64入力に対し別環境で実行した80/120桁参照とLAPACKを比較します。

Hadamard直交因子U,Vとsⱼ=2⁻qj、q=0/4/8/12を使います。b=u₀とb+2⁻⁴⁰u_minを固定し、摂動増幅を測ります。q=0の重複特異値では個々の特異ベクトルは一意ではありません。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/atlas-foundations-conditioning-2026-11-22.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

LAPACKと教材の射影コアには共通の数値基盤が含まれます。mpmath SVDは別実装の二重対角化とQR反復、mpmath最小二乗は同じHouseholder群の別高精度実装です。どの高条件数行列にも微小特異値の相対高精度を保証するものではありません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-22/foundations-conditioning/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/run.py)
- [/code/validated-examples/2026-11-22/foundations-conditioning/test_conditioning.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/test_conditioning.py)

## English

[Saved reconstruction, retained-rank orthogonality and LAPACK differences for fixed full/rank-deficient Householder-QR and one-sided-Jacobi-SVD inputs. Roundoff zeros are displayed at 1e-16.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/results/qr-svd-factorization.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-foundations/#qr-svd-factorization) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#matrix-factorization-en)

### Equations and problem definitions

QR/SVD matrix factorization and least squares; no physical-model equation is assigned.

#### Householder QR and one-sided Jacobi SVD: orthogonality, rank and least squares

Supplementary execution example · Example definition or validation formula

$$
A=QR,\quad Q^TQ=I
$$

$$
A\simeq U_r\Sigma_rV_r^T,\quad x_{\min}=V_r\Sigma_r^{-1}U_r^Tb
$$

Original Householder QR and one-sided Jacobi SVD for real tall matrices are checked on ordinary, 10⁶-column-scaled and rank-deficient inputs, against separate LAPACK singular values and minimum-norm least-squares solutions.

#### QR/SVD: prescribed spectra, perturbation gain and numerical rank

Supplementary execution example · Example definition or validation formula

$$
A=U\operatorname{diag}(2^{-qj})V^T,\quad\kappa_2(A)=2^{3q}
$$

$$
\delta b=\eta u_{\min},\quad\delta x=\eta\sigma_{\min}^{-1}v_{\min}
$$

Vary condition number from 1 to 2³⁶ for exactly representable 16×4 dyadic matrices, separating reconstruction from forward solution error. Compare LAPACK and separately executed 80/120-digit references for the actual binary64 inputs.

### Exact and reference solutions

Check independent NumPy/SciPy references, reconstruction, orthogonality, singular values, rank and least-squares residuals. This is linear-algebra validation rather than a PDE reference-solution card. A separate release varies conditioning, right-hand-side perturbations and numerical-rank thresholds while separating residual from coefficient forward error. Distinguish LAPACK from high-precision references built from actual binary input; no general QR/SVD or arbitrary ill-conditioned-matrix guarantee is implied.

#### Householder QR and one-sided Jacobi SVD: orthogonality, rank and least squares

Compare QR/SVD relative reconstruction, Q/U/V orthogonality, singular values from SciPy LAPACK gesdd, least-squares solutions/ranks from gelsd/gelsy and normal-equation stationarity residuals. Singular-vector signs are not compared; zero matrices and budget exhaustion are tested.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/qr-svd-factorization/?lang=en)

#### QR/SVD: prescribed spectra, perturbation gain and numerical rank

Save reconstruction, orthogonality, singular values, solution perturbations, least-squares stationarity and an exact rank-two control. The mpmath1.3.0 SVD and QR reference was actually executed using integer-ratio conversions of binary inputs. Runtime SHA and completeness guards check all four inputs at both precisions and never substitute analytic truth after a mismatch.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/qr-svd-conditioning/?lang=en)

### Numerical methods

Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.

- [QR, SVD and least squares](https://hrkoyama.github.io/numerical-methods-atlas/methods/qr-svd/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Householder QR and one-sided Jacobi SVD: orthogonality, rank and least squares](https://hrkoyama.github.io/numerical-methods-atlas/validation/qr-svd-factorization/?lang=en)

Supplementary execution example

Original Householder QR and one-sided Jacobi SVD for real tall matrices are checked on ordinary, 10⁶-column-scaled and rank-deficient inputs, against separate LAPACK singular values and minimum-norm least-squares solutions.

Small real matrices with m≥n. Numerical rank uses a 10⁻¹² threshold relative to the largest singular value; compact factors omit null directions. QR has no column pivoting and is not used as a rank-revealing method.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/atlas-foundations-2026-11-22.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

Not a full LAPACK replacement or validation of complex/wide matrices, arbitrary extreme scales or optimal relative singular-value accuracy. The 10⁻¹² cutoff defines numerical rather than exact mathematical rank. The experiment does not establish all hypotheses of the Demmel–Veselić accuracy results.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-22/foundations/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/run.py)
- [/code/validated-examples/2026-11-22/foundations/test_foundations.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/test_foundations.py)

#### [QR/SVD: prescribed spectra, perturbation gain and numerical rank](https://hrkoyama.github.io/numerical-methods-atlas/validation/qr-svd-conditioning/?lang=en)

Supplementary execution example

Vary condition number from 1 to 2³⁶ for exactly representable 16×4 dyadic matrices, separating reconstruction from forward solution error. Compare LAPACK and separately executed 80/120-digit references for the actual binary64 inputs.

Use Hadamard orthogonal factors U,V and sⱼ=2⁻qj for q=0/4/8/12. Fixed b=u₀ and b+2⁻⁴⁰u_min measure perturbation amplification. Individual singular vectors are nonunique for the repeated singular values at q=0.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/atlas-foundations-conditioning-2026-11-22.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

Some LAPACK and projected-core numerical infrastructure is shared. mpmath SVD uses separate bidiagonalization and QR iteration; mpmath least squares is a separate high-precision implementation of the same Householder family. Tiny-singular-value relative accuracy is not guaranteed for arbitrary ill-conditioned matrices.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-22/foundations-conditioning/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/run.py)
- [/code/validated-examples/2026-11-22/foundations-conditioning/test_conditioning.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/test_conditioning.py)
