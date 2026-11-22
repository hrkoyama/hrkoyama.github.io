# Householder QRと片側Jacobi SVD：直交性・階数・最小二乗

実の縦長行列に対するHouseholder QRと片側Jacobi SVDを自作し、通常行列・列スケール差10⁶の行列・階数落ち行列を検査します。独立LAPACKの特異値と最小ノルム最小二乗解を照合します。

## 前提・単位・境界

m≥nの小さな実行列が対象です。SVDの数値階数は最大特異値に対する相対しきい値10⁻¹²で定義し、零特異値方向を除くcompact因子を返します。QRは列ピボットなしで、階数判定には用いません。

## 採用した計算法

Householder反射を左から蓄積してRを上三角化し、Qを構成します。Jacobi SVDは列対の内積を小さくする直交回転を繰り返し、回転した列の長さを特異値とします。AᵀAを作って固有値を求める方法ではありません。最小二乗はQRの後退代入、階数落ちでは打切りSVDで求めます。

$$
A=QR,\quad Q^TQ=I
$$

$$
A\simeq U_r\Sigma_rV_r^T,\quad x_{\min}=V_r\Sigma_r^{-1}U_r^Tb
$$

## 比較・検証

QR/SVDの相対再構成誤差、Q/U/Vの直交性、SciPy LAPACK gesddの特異値、gelsd/gelsyの最小二乗解・階数、正規方程式の停留残差を比較します。特異ベクトルの符号は比較せず、零行列と予算切れも検査します。

## 確認の限界

完全なLAPACK置換、複素行列、横長行列、任意の極端なスケール、最適な相対特異値精度を保証しません。10⁻¹²未満の特異値は入力した数値階数の規約で打ち切るため、数学的な厳密階数と区別します。Demmel–Veselićの精度定理の全条件を実証したとは主張しません。

## 保存実測値と判定

```json
{
  "metrics": {
    "max_qr_reconstruction": 9.197631573723943e-16,
    "max_svd_reconstruction": 1.0519095898403626e-13,
    "max_singular_value_error": 3.399227299681105e-16,
    "max_least_squares_error": 9.164127590036862e-15,
    "max_orthogonality": 1.310421197476067e-15
  },
  "checks": {
    "all_jacobi_converged_and_ranks_match": true,
    "householder_reconstruction": true,
    "householder_orthogonality": true,
    "jacobi_reconstruction": true,
    "jacobi_orthogonality": true,
    "independent_lapack_singular_values": true,
    "independent_minimum_norm_least_squares": true,
    "qr_least_squares": true,
    "least_squares_stationarity": true,
    "sweep_budget_failure_reported": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/qr-svd-factorization/index.json

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/atlas-foundations-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。

## 出典と確認範囲

- A. S. Householder (1958). Unitary Triangularization of a Nonsymmetric Matrix. https://dl.acm.org/doi/10.1145/320941.320947; review_level=publisher-metadata
- J. Demmel and K. Veselić (1992). Jacobi’s Method is More Accurate than QR. https://epubs.siam.org/doi/abs/10.1137/0613074; review_level=publisher-abstract-and-metadata

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Householder QR and one-sided Jacobi SVD: orthogonality, rank and least squares

Original Householder QR and one-sided Jacobi SVD for real tall matrices are checked on ordinary, 10⁶-column-scaled and rank-deficient inputs, against separate LAPACK singular values and minimum-norm least-squares solutions.

## Assumptions, units and boundaries

Small real matrices with m≥n. Numerical rank uses a 10⁻¹² threshold relative to the largest singular value; compact factors omit null directions. QR has no column pivoting and is not used as a rank-revealing method.

## Adopted numerical method

Householder reflectors triangularize R while accumulating Q. The SVD repeatedly rotates column pairs toward orthogonality and uses their resulting lengths as singular values; it does not diagonalize AᵀA. Least squares uses triangular back substitution for QR and truncated compact SVD for deficient rank.

$$
A=QR,\quad Q^TQ=I
$$

$$
A\simeq U_r\Sigma_rV_r^T,\quad x_{\min}=V_r\Sigma_r^{-1}U_r^Tb
$$

## References and validation

Compare QR/SVD relative reconstruction, Q/U/V orthogonality, singular values from SciPy LAPACK gesdd, least-squares solutions/ranks from gelsd/gelsy and normal-equation stationarity residuals. Singular-vector signs are not compared; zero matrices and budget exhaustion are tested.

## Limits

Not a full LAPACK replacement or validation of complex/wide matrices, arbitrary extreme scales or optimal relative singular-value accuracy. The 10⁻¹² cutoff defines numerical rather than exact mathematical rank. The experiment does not establish all hypotheses of the Demmel–Veselić accuracy results.

## Stored measurements and decisions

```json
{
  "metrics": {
    "max_qr_reconstruction": 9.197631573723943e-16,
    "max_svd_reconstruction": 1.0519095898403626e-13,
    "max_singular_value_error": 3.399227299681105e-16,
    "max_least_squares_error": 9.164127590036862e-15,
    "max_orthogonality": 1.310421197476067e-15
  },
  "checks": {
    "all_jacobi_converged_and_ranks_match": true,
    "householder_reconstruction": true,
    "householder_orthogonality": true,
    "jacobi_reconstruction": true,
    "jacobi_orthogonality": true,
    "independent_lapack_singular_values": true,
    "independent_minimum_norm_least_squares": true,
    "qr_least_squares": true,
    "least_squares_stationarity": true,
    "sweep_budget_failure_reported": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/qr-svd-factorization/index.json

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/atlas-foundations-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group.

## Sources and review scope

- A. S. Householder (1958). Unitary Triangularization of a Nonsymmetric Matrix. https://dl.acm.org/doi/10.1145/320941.320947; review_level=publisher-metadata
- J. Demmel and K. Veselić (1992). Jacobi’s Method is More Accurate than QR. https://epubs.siam.org/doi/abs/10.1137/0613074; review_level=publisher-abstract-and-metadata

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
