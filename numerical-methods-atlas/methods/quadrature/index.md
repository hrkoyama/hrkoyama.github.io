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

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

対応する方程式一覧の項目は未登録です。

#### 問題の図 (`method-problems-ja`)

##### [Gauss–Legendreと適応求積：厳密次数・推定誤差・予算切れ](https://hrkoyama.github.io/numerical-methods-atlas/problems/quadrature-moments/?lang=ja) (`quadrature-moments`)

![Gauss–Legendreの次数と適応Simpsonの要求公差を走査した保存誤差。指数・Lorentz型積分の解析値を参照し、推定誤差を厳密上界とは扱わない。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/results/gauss-adaptive-quadrature.png)

この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/quadrature-moments/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/quadrature-moments/?lang=ja#code-ja)

- [Gauss–Legendreと適応求積：厳密次数・推定誤差・予算切れ](https://hrkoyama.github.io/numerical-methods-atlas/validation/gauss-adaptive-quadrature/?lang=ja) (`gauss-adaptive-quadrature`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/atlas-foundations-2026-11-22.zip)

Legendreの3項漸化式からGauss節点と重みを構成し、2n−1次までの多項式モーメントと指数関数を検査します。適応Simpsonは指数関数とLorentz型ピークを積分し、解析積分・独立QUADPACKと比較します。

- [求積：狭いピーク・相殺・端点・誤差推定の盲点](https://hrkoyama.github.io/numerical-methods-atlas/validation/quadrature-conditioning/?lang=ja) (`quadrature-conditioning`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/atlas-foundations-conditioning-2026-11-22.zip)

Gauss次数と適応公差を走査し、狭いLorentzピーク、平方根端点、巨大な相殺、零積分、見逃すcompact bumpを解析積分とQUADPACKで検証します。


#### 厳密解・参照解 (`method-references-ja`)

##### [Gauss–Legendreと適応求積：厳密次数・推定誤差・予算切れ](https://hrkoyama.github.io/numerical-methods-atlas/problems/quadrature-moments/?lang=ja#references-ja) (`quadrature-moments`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/quadrature/)
- 保存結果: [この配布版の保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/results/result.json)
- 検証記録: [配布版の検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/verification.json)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

##### Gauss–Legendreと適応求積：厳密次数・推定誤差・予算切れ (`gauss-adaptive-quadrature`)

[Gauss–Legendreと適応求積：厳密次数・推定誤差・予算切れ](https://hrkoyama.github.io/numerical-methods-atlas/problems/quadrature-moments/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/gauss-adaptive-quadrature/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/atlas-foundations-2026-11-22.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/verification.json)

Legendreの3項漸化式からGauss節点と重みを構成し、2n−1次までの多項式モーメントと指数関数を検査します。適応Simpsonは指数関数とLorentz型ピークを積分し、解析積分・独立QUADPACKと比較します。

##### 求積：狭いピーク・相殺・端点・誤差推定の盲点 (`quadrature-conditioning`)

[Gauss–Legendreと適応求積：厳密次数・推定誤差・予算切れ](https://hrkoyama.github.io/numerical-methods-atlas/problems/quadrature-moments/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/quadrature-conditioning/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/atlas-foundations-conditioning-2026-11-22.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/verification.json)

Gauss次数と適応公差を走査し、狭いLorentzピーク、平方根端点、巨大な相殺、零積分、見逃すcompact bumpを解析積分とQUADPACKで検証します。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

Gauss–Legendreと適応求積：厳密次数・推定誤差・予算切れ: Legendreの3項漸化式からGauss節点と重みを構成し、2n−1次までの多項式モーメントと指数関数を検査します。適応Simpsonは指数関数とLorentz型ピークを積分し、解析積分・独立QUADPACKと比較します。 求積：狭いピーク・相殺・端点・誤差推定の盲点: Gauss次数と適応公差を走査し、狭いLorentzピーク、平方根端点、巨大な相殺、零積分、見逃すcompact bumpを解析積分とQUADPACKで検証します。

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/atlas-foundations-2026-11-22.zip)

[配布版の検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/verification.json)

###### 関連ソース

- [/code/validated-examples/2026-11-22/foundations/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/run.py)
- [/code/validated-examples/2026-11-22/foundations/solvers.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/solvers.py)
- [/code/validated-examples/2026-11-22/foundations-conditioning/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/run.py)
- [/code/validated-examples/2026-11-22/foundations-conditioning/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/experiments.py)
- [/code/validated-examples/2026-11-22/foundations-conditioning/fixtures.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/fixtures.py)
- [/code/validated-examples/2026-11-22/foundations-conditioning/mpmath_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/mpmath_reference.py)
- [/code/validated-examples/2026-11-22/foundations-conditioning/solvers.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/solvers.py)

###### 配布版のテスト

- [/code/validated-examples/2026-11-22/foundations/test_foundations.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/test_foundations.py)
- [/code/validated-examples/2026-11-22/foundations-conditioning/test_conditioning.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/test_conditioning.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q
python run.py --input inputs.json --output output
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

No corresponding equation-registry entry is registered.

#### Problem figures (`method-problems-en`)

##### [Gauss–Legendre and adaptive quadrature: exactness, error estimates and budgets](https://hrkoyama.github.io/numerical-methods-atlas/problems/quadrature-moments/?lang=en) (`quadrature-moments`)

![Saved Gauss–Legendre order and adaptive-Simpson tolerance sweeps against analytic exponential/Lorentzian integrals; estimated errors are not rigorous bounds.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/results/gauss-adaptive-quadrature.png)

Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/quadrature-moments/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/quadrature-moments/?lang=en#code-en)

- [Gauss–Legendre and adaptive quadrature: exactness, error estimates and budgets](https://hrkoyama.github.io/numerical-methods-atlas/validation/gauss-adaptive-quadrature/?lang=en) (`gauss-adaptive-quadrature`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/atlas-foundations-2026-11-22.zip)

Construct Gaussian nodes/weights from the Legendre recurrence and test polynomial moments through degree 2n−1 and an exponential. Adaptive Simpson integrates exponential and Lorentzian peaks, against analytic integrals and independent QUADPACK.

- [Quadrature: narrow peaks, cancellation, endpoints and estimator blind spots](https://hrkoyama.github.io/numerical-methods-atlas/validation/quadrature-conditioning/?lang=en) (`quadrature-conditioning`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/atlas-foundations-conditioning-2026-11-22.zip)

Vary Gauss order and adaptive tolerance on narrow Lorentz peaks, a square-root endpoint, severe cancellation, a zero integral and a deliberately missed compact bump, using analytic integrals and QUADPACK.


#### Exact / reference solutions (`method-references-en`)

##### [Gauss–Legendre and adaptive quadrature: exactness, error estimates and budgets](https://hrkoyama.github.io/numerical-methods-atlas/problems/quadrature-moments/?lang=en#references-en) (`quadrature-moments`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/quadrature/)
- Saved result: [Saved results from this edition](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/results/result.json)
- Verification receipt: [Edition verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/verification.json)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

##### Gauss–Legendre and adaptive quadrature: exactness, error estimates and budgets (`gauss-adaptive-quadrature`)

[Gauss–Legendre and adaptive quadrature: exactness, error estimates and budgets](https://hrkoyama.github.io/numerical-methods-atlas/problems/quadrature-moments/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/gauss-adaptive-quadrature/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/atlas-foundations-2026-11-22.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/verification.json)

Construct Gaussian nodes/weights from the Legendre recurrence and test polynomial moments through degree 2n−1 and an exponential. Adaptive Simpson integrates exponential and Lorentzian peaks, against analytic integrals and independent QUADPACK.

##### Quadrature: narrow peaks, cancellation, endpoints and estimator blind spots (`quadrature-conditioning`)

[Gauss–Legendre and adaptive quadrature: exactness, error estimates and budgets](https://hrkoyama.github.io/numerical-methods-atlas/problems/quadrature-moments/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/quadrature-conditioning/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/atlas-foundations-conditioning-2026-11-22.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/verification.json)

Vary Gauss order and adaptive tolerance on narrow Lorentz peaks, a square-root endpoint, severe cancellation, a zero integral and a deliberately missed compact bump, using analytic integrals and QUADPACK.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Gauss–Legendre and adaptive quadrature: exactness, error estimates and budgets: Construct Gaussian nodes/weights from the Legendre recurrence and test polynomial moments through degree 2n−1 and an exponential. Adaptive Simpson integrates exponential and Lorentzian peaks, against analytic integrals and independent QUADPACK. Quadrature: narrow peaks, cancellation, endpoints and estimator blind spots: Vary Gauss order and adaptive tolerance on narrow Lorentz peaks, a square-root endpoint, severe cancellation, a zero integral and a deliberately missed compact bump, using analytic integrals and QUADPACK.

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[Related code edition / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/atlas-foundations-2026-11-22.zip)

[Edition verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/verification.json)

###### Related source

- [/code/validated-examples/2026-11-22/foundations/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/run.py)
- [/code/validated-examples/2026-11-22/foundations/solvers.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/solvers.py)
- [/code/validated-examples/2026-11-22/foundations-conditioning/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/run.py)
- [/code/validated-examples/2026-11-22/foundations-conditioning/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/experiments.py)
- [/code/validated-examples/2026-11-22/foundations-conditioning/fixtures.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/fixtures.py)
- [/code/validated-examples/2026-11-22/foundations-conditioning/mpmath_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/mpmath_reference.py)
- [/code/validated-examples/2026-11-22/foundations-conditioning/solvers.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/solvers.py)

###### Package tests

- [/code/validated-examples/2026-11-22/foundations/test_foundations.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/test_foundations.py)
- [/code/validated-examples/2026-11-22/foundations-conditioning/test_conditioning.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/test_conditioning.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q
python run.py --input inputs.json --output output
```
