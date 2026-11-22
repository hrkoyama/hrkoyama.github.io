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
