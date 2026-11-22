# QR/SVD：既定特異値・摂動増幅・数値階数

二進で厳密に表現できる16×4行列の条件数を1から2³⁶まで変え、再構成誤差と解誤差を分けます。実際のbinary64入力に対し別環境で実行した80/120桁参照とLAPACKを比較します。

**使用手法**

- [QR・SVD・最小二乗](https://hrkoyama.github.io/numerical-methods-atlas/methods/qr-svd/?lang=ja) (`qr-svd`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/qr-svd-conditioning/?lang=ja#qr-svd-conditioning-ja-algorithm)

Householder QR、片側Jacobi SVD、三角後退代入を実装します。SVDの数値階数閾値を10⁻⁸/10⁻¹²/10⁻¹⁴へ変え、同じ切捨て規約のLAPACK解と比較します。正規方程式の計算例は追加していません。

$$
A=U\operatorname{diag}(2^{-qj})V^T,\quad\kappa_2(A)=2^{3q}
$$

$$
\delta b=\eta u_{\min},\quad\delta x=\eta\sigma_{\min}^{-1}v_{\min}
$$

方程式一覧の対応項目は未登録です。個別の式・近似・診断は上の定義に示します。

**問題の図**

![QR/SVD：既定特異値・摂動増幅・数値階数：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/results/qr-svd-conditioning.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Householder QRと片側Jacobi SVD：直交性・階数・最小二乗](https://hrkoyama.github.io/numerical-methods-atlas/problems/matrix-factorization/?lang=ja) (`matrix-factorization`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/matrix-factorization/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/qr-svd-conditioning/?lang=ja#qr-svd-conditioning-ja-validation)

再構成・直交性・特異値・右辺摂動による解差・最小二乗停留残差・厳密階数2の対照を保存します。高精度参照は実二進入力を整数比へ変換し、mpmath 1.3.0のSVDとQRを独立実行済みです。SHAと全4入力・両精度の完全性を実行時に検査し、不一致を解析解へ置換しません。

参照解一覧の対応カードは未登録です。この実行例の参照値・判定方法は上の検証資料で確認できます。
## 前提・単位・境界

Hadamard直交因子U,Vとsⱼ=2⁻qj、q=0/4/8/12を使います。b=u₀とb+2⁻⁴⁰u_minを固定し、摂動増幅を測ります。q=0の重複特異値では個々の特異ベクトルは一意ではありません。

**編集上の補足**

再構成・直交性・後退誤差が小さくても、悪条件問題の前進誤差は大きくなり得ます。入力した浮動小数点行列と理想的に指定した特異値を区別し、数値階数の閾値も明記します。

## 採用した計算法

Householder QR、片側Jacobi SVD、三角後退代入を実装します。SVDの数値階数閾値を10⁻⁸/10⁻¹²/10⁻¹⁴へ変え、同じ切捨て規約のLAPACK解と比較します。正規方程式の計算例は追加していません。

$$
A=U\operatorname{diag}(2^{-qj})V^T,\quad\kappa_2(A)=2^{3q}
$$

$$
\delta b=\eta u_{\min},\quad\delta x=\eta\sigma_{\min}^{-1}v_{\min}
$$

## 比較・検証

再構成・直交性・特異値・右辺摂動による解差・最小二乗停留残差・厳密階数2の対照を保存します。高精度参照は実二進入力を整数比へ変換し、mpmath 1.3.0のSVDとQRを独立実行済みです。SHAと全4入力・両精度の完全性を実行時に検査し、不一致を解析解へ置換しません。

## 確認の限界

LAPACKと教材の射影コアには共通の数値基盤が含まれます。mpmath SVDは別実装の二重対角化とQR反復、mpmath最小二乗は同じHouseholder群の別高精度実装です。どの高条件数行列にも微小特異値の相対高精度を保証するものではありません。

## 保存実測値と判定

```json
{
  "metrics": {
    "largest_condition_2": 68719476736.0,
    "maximum_backward_reconstruction": 6.074604146362075e-16,
    "maximum_forward_error": 0.0004920953373835635,
    "minimum_numerical_rank": 2,
    "reference_precision_digits": 120
  },
  "checks": {
    "q0-factorization": true,
    "q0-high-precision-spectrum": true,
    "q0-condition-aware-forward": true,
    "q0-lapack-reference": true,
    "q0-perturbation-gain": true,
    "q4-factorization": true,
    "q4-high-precision-spectrum": true,
    "q4-condition-aware-forward": true,
    "q4-lapack-reference": true,
    "q4-perturbation-gain": true,
    "q8-factorization": true,
    "q8-high-precision-spectrum": true,
    "q8-condition-aware-forward": true,
    "q8-lapack-reference": true,
    "q8-perturbation-gain": true,
    "q12-factorization": true,
    "q12-high-precision-spectrum": true,
    "q12-condition-aware-forward": true,
    "q12-lapack-reference": true,
    "q12-perturbation-gain": true,
    "cutoff1e-08-rank-aware": true,
    "cutoff1e-12-rank-aware": true,
    "cutoff1e-14-rank-aware": true,
    "exact-rank-deficiency": true,
    "sweep-budget-failure-explicit": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/qr-svd-conditioning/index.json

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/atlas-foundations-conditioning-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。

## 出典と確認範囲

- A. S. Householder (1958). Unitary Triangularization of a Nonsymmetric Matrix. https://dl.acm.org/doi/10.1145/320941.320947; review_level=publisher-metadata
- J. Demmel, K. Veselić (1992). Jacobi’s Method is More Accurate than QR. https://epubs.siam.org/doi/abs/10.1137/0613074; review_level=primary publisher abstract and bibliographic metadata
  適切な停止規準と行列の成分ごとの条件に依存する相対精度の主張を確認しました。一般の高条件数行列における微小特異値の万能な相対精度とはしません。
- LAPACK authors (1999). Further Details: Error Bounds for Linear Least Squares Problems. https://netlib.org/lapack/lug/node83.html; review_level=official implementation documentation, error-analysis and numerical-rank sections
  小さな後退誤差と前進誤差を区別し、最小二乗では条件数だけでなく残差の角度にも依存すること、RCONDによる切捨ては数値階数の規約であることを確認しました。
- mpmath developers (2023). mpmath 1.3.0 matrix documentation and installed implementation. https://mpmath.org/doc/1.3.0/matrices.html; review_level=official matrix documentation and selected installed mpmath1.3.0 source (svd_r_raw, qr_solve), plus actual 80/120dps fixed-input execution
  SVDはHouseholder二重対角化とQR反復、最小二乗は別実装の高精度Householder QRです。後者は教材のQRと同じ数理的手法群であり、別の手法群とは呼びません。実際の二進浮動小数点入力を整数比で読み込み、生成専用環境で実行しました。

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# QR/SVD: prescribed spectra, perturbation gain and numerical rank

Vary condition number from 1 to 2³⁶ for exactly representable 16×4 dyadic matrices, separating reconstruction from forward solution error. Compare LAPACK and separately executed 80/120-digit references for the actual binary64 inputs.

**Methods used**

- [QR, SVD and least squares](https://hrkoyama.github.io/numerical-methods-atlas/methods/qr-svd/?lang=en) (`qr-svd`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/qr-svd-conditioning/?lang=en#qr-svd-conditioning-en-algorithm)

Implement Householder QR, one-sided Jacobi SVD and triangular back substitution. Vary rank cutoffs 10⁻⁸/10⁻¹²/10⁻¹⁴ and compare with LAPACK solutions using the same truncation convention. No executed normal-equations comparison is added.

$$
A=U\operatorname{diag}(2^{-qj})V^T,\quad\kappa_2(A)=2^{3q}
$$

$$
\delta b=\eta u_{\min},\quad\delta x=\eta\sigma_{\min}^{-1}v_{\min}
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![QR/SVD: prescribed spectra, perturbation gain and numerical rank: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/results/qr-svd-conditioning.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Householder QR and one-sided Jacobi SVD: orthogonality, rank and least squares](https://hrkoyama.github.io/numerical-methods-atlas/problems/matrix-factorization/?lang=en) (`matrix-factorization`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/matrix-factorization/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/qr-svd-conditioning/?lang=en#qr-svd-conditioning-en-validation)

Save reconstruction, orthogonality, singular values, solution perturbations, least-squares stationarity and an exact rank-two control. The mpmath1.3.0 SVD and QR reference was actually executed using integer-ratio conversions of binary inputs. Runtime SHA and completeness guards check all four inputs at both precisions and never substitute analytic truth after a mismatch.

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.
## Assumptions, units and boundaries

Use Hadamard orthogonal factors U,V and sⱼ=2⁻qj for q=0/4/8/12. Fixed b=u₀ and b+2⁻⁴⁰u_min measure perturbation amplification. Individual singular vectors are nonunique for the repeated singular values at q=0.

**Editorial clarification**

Small reconstruction, orthogonality and backward errors do not ensure small forward error for an ill-conditioned problem. Distinguish the actual floating-point matrix from its intended singular values and state the numerical-rank threshold.

## Adopted numerical method

Implement Householder QR, one-sided Jacobi SVD and triangular back substitution. Vary rank cutoffs 10⁻⁸/10⁻¹²/10⁻¹⁴ and compare with LAPACK solutions using the same truncation convention. No executed normal-equations comparison is added.

$$
A=U\operatorname{diag}(2^{-qj})V^T,\quad\kappa_2(A)=2^{3q}
$$

$$
\delta b=\eta u_{\min},\quad\delta x=\eta\sigma_{\min}^{-1}v_{\min}
$$

## References and validation

Save reconstruction, orthogonality, singular values, solution perturbations, least-squares stationarity and an exact rank-two control. The mpmath1.3.0 SVD and QR reference was actually executed using integer-ratio conversions of binary inputs. Runtime SHA and completeness guards check all four inputs at both precisions and never substitute analytic truth after a mismatch.

## Limits

Some LAPACK and projected-core numerical infrastructure is shared. mpmath SVD uses separate bidiagonalization and QR iteration; mpmath least squares is a separate high-precision implementation of the same Householder family. Tiny-singular-value relative accuracy is not guaranteed for arbitrary ill-conditioned matrices.

## Stored measurements and decisions

```json
{
  "metrics": {
    "largest_condition_2": 68719476736.0,
    "maximum_backward_reconstruction": 6.074604146362075e-16,
    "maximum_forward_error": 0.0004920953373835635,
    "minimum_numerical_rank": 2,
    "reference_precision_digits": 120
  },
  "checks": {
    "q0-factorization": true,
    "q0-high-precision-spectrum": true,
    "q0-condition-aware-forward": true,
    "q0-lapack-reference": true,
    "q0-perturbation-gain": true,
    "q4-factorization": true,
    "q4-high-precision-spectrum": true,
    "q4-condition-aware-forward": true,
    "q4-lapack-reference": true,
    "q4-perturbation-gain": true,
    "q8-factorization": true,
    "q8-high-precision-spectrum": true,
    "q8-condition-aware-forward": true,
    "q8-lapack-reference": true,
    "q8-perturbation-gain": true,
    "q12-factorization": true,
    "q12-high-precision-spectrum": true,
    "q12-condition-aware-forward": true,
    "q12-lapack-reference": true,
    "q12-perturbation-gain": true,
    "cutoff1e-08-rank-aware": true,
    "cutoff1e-12-rank-aware": true,
    "cutoff1e-14-rank-aware": true,
    "exact-rank-deficiency": true,
    "sweep-budget-failure-explicit": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/qr-svd-conditioning/index.json

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/atlas-foundations-conditioning-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group.

## Sources and review scope

- A. S. Householder (1958). Unitary Triangularization of a Nonsymmetric Matrix. https://dl.acm.org/doi/10.1145/320941.320947; review_level=publisher-metadata
- J. Demmel, K. Veselić (1992). Jacobi’s Method is More Accurate than QR. https://epubs.siam.org/doi/abs/10.1137/0613074; review_level=primary publisher abstract and bibliographic metadata
  Checked the dependence of relative-accuracy statements on stopping rules and componentwise sensitivity; not a blanket accuracy guarantee for tiny singular values of arbitrary ill-conditioned matrices.
- LAPACK authors (1999). Further Details: Error Bounds for Linear Least Squares Problems. https://netlib.org/lapack/lug/node83.html; review_level=official implementation documentation, error-analysis and numerical-rank sections
  Checked backward versus forward error, the residual-angle dependence of least-squares sensitivity, and numerical-rank truncation controlled by RCOND.
- mpmath developers (2023). mpmath 1.3.0 matrix documentation and installed implementation. https://mpmath.org/doc/1.3.0/matrices.html; review_level=official matrix documentation and selected installed mpmath1.3.0 source (svd_r_raw, qr_solve), plus actual 80/120dps fixed-input execution
  SVD uses Householder bidiagonalization and a QR variant; least squares uses a separate high-precision Householder QR implementation. The latter shares the educational QR mathematical family and is not called a different algorithm family. Actual binary floating-point inputs were loaded by integer ratios and executed in a generation-only environment.

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
