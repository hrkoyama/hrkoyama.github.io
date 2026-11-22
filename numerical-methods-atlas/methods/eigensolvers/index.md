# Krylov eigenvalue solvers / Krylov固有値解法

Status: educational-example

Lanczos and Arnoldi: convergence of Ritz values and eigenpair residuals: Original Lanczos and Arnoldi on symmetric/nonsymmetric 32×32 and 48×48 matrices measure convergence of the largest-real-part eigenpair over Krylov dimensions 4, 8 and 16, against independent full-matrix LAPACK references. Krylov eigenvalues: cluster subspaces and nonnormal sensitivity: Measure Lanczos and Arnoldi with dimensions4/8/16/32 on 48-dimensional clustered symmetric and strongly nonnormal triangular matrices. Distinguish residual, forward error, eigenvalue condition number and invariant subspace.

Lanczos・Arnoldi：Ritz値と固有対残差の収束: 32・48次の対称／非対称行列でLanczosとArnoldiを自作し、Krylov次元4・8・16による最大実部の固有対の収束を測ります。行列全体を解く独立LAPACK参照と照合します。 Krylov固有値：クラスター部分空間と非正規感度: 48次のクラスター固有値と強い非正規上三角行列で、次元4/8/16/32のLanczos・Arnoldiを測ります。残差・前進誤差・固有値条件数・不変部分空間を分けます。

Lanczos and Arnoldi: convergence of Ritz values and eigenpair residuals: Unrestarted small-matrix educational examples with separated extreme eigenpairs. Interior/clustered eigenvalues, very large sparse matrices, strong nonnormality, shift-invert and implicitly restarted Arnoldi are outside scope. A small eigenpair residual alone is not treated as a rigorous eigenvalue-error bound for nonnormal matrices. Krylov eigenvalues: cluster subspaces and nonnormal sensitivity: NumPy projected solves and SciPy dense references may share LAPACK infrastructure and are not claimed fully independent backends. Analytic eigenvalues and constructed controls provide additional checks. Restarting, interior eigenvalues, large sparse systems and universal monotonic convergence are outside scope.

Other names: 固有値解法, eigenvalue solver, Krylov eigensolver, クリロフ固有値法

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/eigensolvers/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/eigensolvers/



- Reference: https://doi.org/10.1090/qam/42792 — Method-specific source; see the detailed reading for source role and actual review depth.
- Reference: https://doi.org/10.6028/jres.045.026 — Method-specific source; see the detailed reading for source role and actual review depth.

## Small fixed-input validation supplements

Lanczos and Arnoldi: convergence of Ritz values and eigenpair residuals: Original Lanczos and Arnoldi on symmetric/nonsymmetric 32×32 and 48×48 matrices measure convergence of the largest-real-part eigenpair over Krylov dimensions 4, 8 and 16, against independent full-matrix LAPACK references. Krylov eigenvalues: cluster subspaces and nonnormal sensitivity: Measure Lanczos and Arnoldi with dimensions4/8/16/32 on 48-dimensional clustered symmetric and strongly nonnormal triangular matrices. Distinguish residual, forward error, eigenvalue condition number and invariant subspace.

Lanczos・Arnoldi：Ritz値と固有対残差の収束: 32・48次の対称／非対称行列でLanczosとArnoldiを自作し、Krylov次元4・8・16による最大実部の固有対の収束を測ります。行列全体を解く独立LAPACK参照と照合します。 Krylov固有値：クラスター部分空間と非正規感度: 48次のクラスター固有値と強い非正規上三角行列で、次元4/8/16/32のLanczos・Arnoldiを測ります。残差・前進誤差・固有値条件数・不変部分空間を分けます。

- Lanczos and Arnoldi: convergence of Ritz values and eigenpair residuals: https://hrkoyama.github.io/numerical-methods-atlas/validation/krylov-eigenvalues/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/atlas-foundations-2026-11-22.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/results/result.json

- Krylov eigenvalues: cluster subspaces and nonnormal sensitivity: https://hrkoyama.github.io/numerical-methods-atlas/validation/krylov-eigen-conditioning/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/atlas-foundations-conditioning-2026-11-22.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/results/result.json

Common execution records: [{"id": "krylov-eigenvalues", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/krylov-eigenvalues/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/krylov-eigenvalues/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "krylov-eigen-conditioning", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/krylov-eigen-conditioning/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/krylov-eigen-conditioning/?lang=en"}, "kind": "dedicated-supplement"}]

Next: Preserve the published fixed-input scope; validate conditions, references and criteria separately for extensions.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/eigensolvers/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/
