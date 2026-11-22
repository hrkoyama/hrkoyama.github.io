# Krylov eigenvalue solvers / Krylov固有値解法

Status: educational-example

Original Lanczos and Arnoldi on symmetric/nonsymmetric 32×32 and 48×48 matrices measure convergence of the largest-real-part eigenpair over Krylov dimensions 4, 8 and 16, against independent full-matrix LAPACK references.

32・48次の対称／非対称行列でLanczosとArnoldiを自作し、Krylov次元4・8・16による最大実部の固有対の収束を測ります。行列全体を解く独立LAPACK参照と照合します。

Unrestarted small-matrix educational examples with separated extreme eigenpairs. Interior/clustered eigenvalues, very large sparse matrices, strong nonnormality, shift-invert and implicitly restarted Arnoldi are outside scope. A small eigenpair residual alone is not treated as a rigorous eigenvalue-error bound for nonnormal matrices.

Other names: 固有値解法, eigenvalue solver, Krylov eigensolver, クリロフ固有値法

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/eigensolvers/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/eigensolvers/



- Reference: https://doi.org/10.1090/qam/42792 — Method-specific source; see the detailed reading for source role and actual review depth.
- Reference: https://doi.org/10.6028/jres.045.026 — Method-specific source; see the detailed reading for source role and actual review depth.

## Small fixed-input validation supplement

Original Lanczos and Arnoldi on symmetric/nonsymmetric 32×32 and 48×48 matrices measure convergence of the largest-real-part eigenpair over Krylov dimensions 4, 8 and 16, against independent full-matrix LAPACK references.

32・48次の対称／非対称行列でLanczosとArnoldiを自作し、Krylov次元4・8・16による最大実部の固有対の収束を測ります。行列全体を解く独立LAPACK参照と照合します。

- Lanczos and Arnoldi: convergence of Ritz values and eigenpair residuals: https://hrkoyama.github.io/numerical-methods-atlas/validation/krylov-eigenvalues/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/atlas-foundations-2026-11-22.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/results/result.json

Common execution records: [{"id": "krylov-eigenvalues", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/krylov-eigenvalues/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/krylov-eigenvalues/?lang=en"}, "kind": "dedicated-supplement"}]

Next: Preserve the published fixed-input scope; validate conditions, references and criteria separately for extensions.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/eigensolvers/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/
