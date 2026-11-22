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

### 厳密解・参照解

独立NumPy/SciPy参照、行列再構成・直交性・特異値・階数・最小二乗残差を確認します。PDEの参照解カードとは別の線形代数検証です。

#### Householder QRと片側Jacobi SVD：直交性・階数・最小二乗

QR/SVDの相対再構成誤差、Q/U/Vの直交性、SciPy LAPACK gesddの特異値、gelsd/gelsyの最小二乗解・階数、正規方程式の停留残差を比較します。特異ベクトルの符号は比較せず、零行列と予算切れも検査します。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/qr-svd-factorization/?lang=ja)

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

### Exact and reference solutions

Check independent NumPy/SciPy references, reconstruction, orthogonality, singular values, rank and least-squares residuals. This is linear-algebra validation rather than a PDE reference-solution card.

#### Householder QR and one-sided Jacobi SVD: orthogonality, rank and least squares

Compare QR/SVD relative reconstruction, Q/U/V orthogonality, singular values from SciPy LAPACK gesdd, least-squares solutions/ranks from gelsd/gelsy and normal-equation stationarity residuals. Singular-vector signs are not compared; zero matrices and budget exhaustion are tested.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/qr-svd-factorization/?lang=en)

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
