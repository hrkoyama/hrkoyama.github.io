# Gaussian and adaptive quadrature / Gauss求積・適応積分

Status: educational-example

Gauss–Legendre and adaptive quadrature: exactness, error estimates and budgets: Construct Gaussian nodes/weights from the Legendre recurrence and test polynomial moments through degree 2n−1 and an exponential. Adaptive Simpson integrates exponential and Lorentzian peaks, against analytic integrals and independent QUADPACK. Quadrature: narrow peaks, cancellation, endpoints and estimator blind spots: Vary Gauss order and adaptive tolerance on narrow Lorentz peaks, a square-root endpoint, severe cancellation, a zero integral and a deliberately missed compact bump, using analytic integrals and QUADPACK.

Gauss–Legendreと適応求積：厳密次数・推定誤差・予算切れ: Legendreの3項漸化式からGauss節点と重みを構成し、2n−1次までの多項式モーメントと指数関数を検査します。適応Simpsonは指数関数とLorentz型ピークを積分し、解析積分・独立QUADPACKと比較します。 求積：狭いピーク・相殺・端点・誤差推定の盲点: Gauss次数と適応公差を走査し、狭いLorentzピーク、平方根端点、巨大な相殺、零積分、見逃すcompact bumpを解析積分とQUADPACKで検証します。

Gauss–Legendre and adaptive quadrature: exactness, error estimates and budgets: The local Simpson estimate is not a rigorous error bound for arbitrary functions. The implementation does not generally solve missed high frequencies, singularities or roundoff stagnation, and it is not a reimplementation of Gauss–Kronrod or all of QUADPACK. Quadrature: narrow peaks, cancellation, endpoints and estimator blind spots: The Simpson estimate is not a certified error bound. Passing the blind-spot control does not mean accurate integration. Direct square-root integration may honestly terminate at its depth budget. Exhaustive oscillatory/singular exploration and certified quadrature are not claimed.

Other names: 数値求積, 数値積分, Gauss求積, Gaussian quadrature, ガウス求積, 適応積分

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/quadrature/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/quadrature/



- Reference: https://doi.org/10.1090/s0025-5718-69-99647-1 — Method-specific source; see the detailed reading for source role and actual review depth.
- Reference: https://doi.org/10.1007/978-3-642-61786-7 — Method-specific source; see the detailed reading for source role and actual review depth.

## Small fixed-input validation supplements

Gauss–Legendre and adaptive quadrature: exactness, error estimates and budgets: Construct Gaussian nodes/weights from the Legendre recurrence and test polynomial moments through degree 2n−1 and an exponential. Adaptive Simpson integrates exponential and Lorentzian peaks, against analytic integrals and independent QUADPACK. Quadrature: narrow peaks, cancellation, endpoints and estimator blind spots: Vary Gauss order and adaptive tolerance on narrow Lorentz peaks, a square-root endpoint, severe cancellation, a zero integral and a deliberately missed compact bump, using analytic integrals and QUADPACK.

Gauss–Legendreと適応求積：厳密次数・推定誤差・予算切れ: Legendreの3項漸化式からGauss節点と重みを構成し、2n−1次までの多項式モーメントと指数関数を検査します。適応Simpsonは指数関数とLorentz型ピークを積分し、解析積分・独立QUADPACKと比較します。 求積：狭いピーク・相殺・端点・誤差推定の盲点: Gauss次数と適応公差を走査し、狭いLorentzピーク、平方根端点、巨大な相殺、零積分、見逃すcompact bumpを解析積分とQUADPACKで検証します。

- Gauss–Legendre and adaptive quadrature: exactness, error estimates and budgets: https://hrkoyama.github.io/numerical-methods-atlas/validation/gauss-adaptive-quadrature/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/atlas-foundations-2026-11-22.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/results/result.json

- Quadrature: narrow peaks, cancellation, endpoints and estimator blind spots: https://hrkoyama.github.io/numerical-methods-atlas/validation/quadrature-conditioning/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/atlas-foundations-conditioning-2026-11-22.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/results/result.json

Common execution records: [{"id": "gauss-adaptive-quadrature", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/gauss-adaptive-quadrature/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/gauss-adaptive-quadrature/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "quadrature-conditioning", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/quadrature-conditioning/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/quadrature-conditioning/?lang=en"}, "kind": "dedicated-supplement"}]

Next: Preserve the published fixed-input scope; validate conditions, references and criteria separately for extensions.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/quadrature/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/
