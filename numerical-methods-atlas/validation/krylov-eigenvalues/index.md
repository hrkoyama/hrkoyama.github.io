# Lanczos・Arnoldi：Ritz値と固有対残差の収束

32・48次の対称／非対称行列でLanczosとArnoldiを自作し、Krylov次元4・8・16による最大実部の固有対の収束を測ります。行列全体を解く独立LAPACK参照と照合します。

## 前提・単位・境界

対称問題では実対称行列、非対称問題では既知の分離した最大固有値5を持つ実行列を使います。初期ベクトルは固定seedです。非対称Ritz値は複素数を許し、最大実部で選びます。

## 採用した計算法

Lanczosの3項漸化式に2回の全再直交化を加え、Arnoldiは修正Gram–Schmidtを2回行います。小さな射影行列T/HだけをNumPyのeigh/eigで解き、元空間へRitzベクトルを戻します。大きな元行列の密固有値計算は参照側だけで使います。

$$
AV_m=V_mH_m+h_{m+1,m}v_{m+1}e_m^T
$$

$$
H_my=\theta y,\quad v=V_my,\quad r=Av-\theta v
$$

## 比較・検証

||Av−λv||₂、独立密行列固有値との差、基底の直交性を保存し、Krylov次元を増やした末尾の改善を確認します。非対称Ritz値の単調収束は仮定しません。恒等行列のhappy breakdown、零初期ベクトル拒否、次元予算不足も検査します。

## 確認の限界

非再始動・小行列・分離した極端固有対の教材です。内部固有値、クラスタ、巨大な疎行列、強い非正規性、shift-invertやimplicitly restarted Arnoldiは対象外です。小さな固有対残差だけで非正規行列の固有値誤差の厳密上界とはしません。

## 保存実測値と判定

```json
{
  "metrics": {
    "max_final_eigenpair_residual": 1.4394924647739691e-12,
    "max_basis_orthogonality": 4.911536314397836e-16
  },
  "checks": {
    "independent_dense_eigenvalues_and_residuals": true,
    "krylov_basis_orthogonality": true,
    "dimension_budget_failure_reported": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/krylov-eigenvalues/index.json

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

- C. Lanczos (1950). An Iteration Method for the Solution of the Eigenvalue Problem of Linear Differential and Integral Operators. https://nvlpubs.nist.gov/nistpubs/jres/045/jresv45n4p255_A1b.pdf; review_level=primary-first-page-and-official-metadata
- W. E. Arnoldi (1951). The principle of minimized iterations in the solution of the matrix eigenvalue problem. https://doi.org/10.1090/qam/42792; review_level=publisher-metadata-and-reference-list
- Y. Saad (1980). Variations on Arnoldi’s method for computing eigenelements of large unsymmetric matrices. https://www.sciencedirect.com/science/article/pii/002437958090169X; review_level=publisher-abstract-and-metadata

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Lanczos and Arnoldi: convergence of Ritz values and eigenpair residuals

Original Lanczos and Arnoldi on symmetric/nonsymmetric 32×32 and 48×48 matrices measure convergence of the largest-real-part eigenpair over Krylov dimensions 4, 8 and 16, against independent full-matrix LAPACK references.

## Assumptions, units and boundaries

The symmetric case is real symmetric; the nonsymmetric case is real with a known separated largest eigenvalue 5. Starting vectors use fixed seeds. Nonsymmetric Ritz values may be complex and are selected by largest real part.

## Adopted numerical method

Lanczos uses its three-term recurrence plus two passes of full reorthogonalization; Arnoldi uses two-pass modified Gram–Schmidt. Only the small projected T/H is solved by NumPy eigh/eig before lifting Ritz vectors. A full dense solve of the original matrix is used only on the reference side.

$$
AV_m=V_mH_m+h_{m+1,m}v_{m+1}e_m^T
$$

$$
H_my=\theta y,\quad v=V_my,\quad r=Av-\theta v
$$

## References and validation

Store ||Av−λv||₂, differences from independently solved dense eigenvalues and basis orthogonality; verify final improvement as Krylov dimension grows. Nonsymmetric Ritz convergence is not assumed monotone. Tests include identity-matrix happy breakdown, zero-start rejection and insufficient dimension budgets.

## Limits

Unrestarted small-matrix educational examples with separated extreme eigenpairs. Interior/clustered eigenvalues, very large sparse matrices, strong nonnormality, shift-invert and implicitly restarted Arnoldi are outside scope. A small eigenpair residual alone is not treated as a rigorous eigenvalue-error bound for nonnormal matrices.

## Stored measurements and decisions

```json
{
  "metrics": {
    "max_final_eigenpair_residual": 1.4394924647739691e-12,
    "max_basis_orthogonality": 4.911536314397836e-16
  },
  "checks": {
    "independent_dense_eigenvalues_and_residuals": true,
    "krylov_basis_orthogonality": true,
    "dimension_budget_failure_reported": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/krylov-eigenvalues/index.json

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

- C. Lanczos (1950). An Iteration Method for the Solution of the Eigenvalue Problem of Linear Differential and Integral Operators. https://nvlpubs.nist.gov/nistpubs/jres/045/jresv45n4p255_A1b.pdf; review_level=primary-first-page-and-official-metadata
- W. E. Arnoldi (1951). The principle of minimized iterations in the solution of the matrix eigenvalue problem. https://doi.org/10.1090/qam/42792; review_level=publisher-metadata-and-reference-list
- Y. Saad (1980). Variations on Arnoldi’s method for computing eigenelements of large unsymmetric matrices. https://www.sciencedirect.com/science/article/pii/002437958090169X; review_level=publisher-abstract-and-metadata

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
