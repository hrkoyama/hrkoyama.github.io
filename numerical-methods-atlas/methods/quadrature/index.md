# Gaussian and adaptive quadrature / Gauss求積・適応積分

Status: educational-example

Gauss–Legendre and adaptive quadrature: exactness, error estimates and budgets: Construct Gaussian nodes/weights from the Legendre recurrence and test polynomial moments through degree 2n−1 and an exponential. Adaptive Simpson integrates exponential and Lorentzian peaks, against analytic integrals and independent QUADPACK. Quadrature: narrow peaks, cancellation, endpoints and estimator blind spots: Vary Gauss order and adaptive tolerance on narrow Lorentz peaks, a square-root endpoint, severe cancellation, a zero integral and a deliberately missed compact bump, using analytic integrals and QUADPACK. Fixed educational executions: QUADPACK dispatch and finite Simpson companions, G7/K15 and finite-interval tanh-sinh, Tensor and Smolyak controls in two to four dimensions.

Gauss–Legendreと適応求積：厳密次数・推定誤差・予算切れ: Legendreの3項漸化式からGauss節点と重みを構成し、2n−1次までの多項式モーメントと指数関数を検査します。適応Simpsonは指数関数とLorentz型ピークを積分し、解析積分・独立QUADPACKと比較します。 求積：狭いピーク・相殺・端点・誤差推定の盲点: Gauss次数と適応公差を走査し、狭いLorentzピーク、平方根端点、巨大な相殺、零積分、見逃すcompact bumpを解析積分とQUADPACKで検証します。 固定した教育用実行例：領域別QUADPACKと有限Simpson対照、G7/K15と有限区間tanh-sinh、2〜4次元テンソル・Smolyak対照。

Gauss–Legendre and adaptive quadrature: exactness, error estimates and budgets: The local Simpson estimate is not a rigorous error bound for arbitrary functions. The implementation does not generally solve missed high frequencies, singularities or roundoff stagnation, and it is not a reimplementation of Gauss–Kronrod or all of QUADPACK. Quadrature: narrow peaks, cancellation, endpoints and estimator blind spots: The Simpson estimate is not a certified error bound. Passing the blind-spot control does not mean accurate integration. Direct square-root integration may honestly terminate at its depth budget. Exhaustive oscillatory/singular exploration and certified quadrature are not claimed.

Other names: 数値求積, 数値積分, Gauss求積, Gaussian quadrature, ガウス求積, 適応積分

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/quadrature/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/quadrature/



- Reference: https://doi.org/10.1090/s0025-5718-69-99647-1 — Method-specific source; see the detailed reading for source role and actual review depth.
- Reference: https://doi.org/10.1007/978-3-642-61786-7 — Method-specific source; see the detailed reading for source role and actual review depth.
- Reference: https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.integrate.quad.html — Selected parameters/full_output and routine dispatch; no complete QUADPACK book/proof audit.
- Reference: https://raw.githubusercontent.com/scipy/scipy/v1.14.1/scipy/integrate/quadpack/dqk15.f — Displayed table and nesting/resasc safeguards; coefficients are shared-origin, not independently regenerated.
- Reference: https://ems.press/doi/pdf/10.2977/prims/1195192451 — Selected extracted pp722/724/730 equations; rendered equation screenshots failed. No whole-paper proof/optimality audit.
- Reference: https://www.sam.math.ethz.ch/sam_reports/reports_final/reports2008/2008-07.pdf — Selected cover/introduction/sec2 extracted equations2.1–2.6; not the entire DFT proof or performance study. This report supports the Clenshaw-Curtis rule only. The Smolyak Delta/combination assembly is independently derived here; the Smolyak1963 and Gerstner-Griebel1998 original bodies remain unread.

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

- QUADPACK dispatch and finite Simpson companions: https://hrkoyama.github.io/numerical-methods-atlas/validation/quadpack-domain-selection/
- G7/K15 and finite-interval tanh-sinh: https://hrkoyama.github.io/numerical-methods-atlas/validation/gk15-double-exponential/
- Tensor and Smolyak controls in two to four dimensions: https://hrkoyama.github.io/numerical-methods-atlas/validation/tensor-smolyak-dimensions/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/atlas-quadrature-controls-2026-11-25.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/results/result.json

Common execution records: [{"id": "gauss-adaptive-quadrature", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/gauss-adaptive-quadrature/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/gauss-adaptive-quadrature/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "quadrature-conditioning", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/quadrature-conditioning/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/quadrature-conditioning/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "quadpack-domain-selection", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/quadpack-domain-selection/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/quadpack-domain-selection/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "gk15-double-exponential", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/gk15-double-exponential/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/gk15-double-exponential/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "tensor-smolyak-dimensions", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/tensor-smolyak-dimensions/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/tensor-smolyak-dimensions/?lang=en"}, "kind": "dedicated-supplement"}]

Next: Preserve the published fixed-input scope; validate conditions, references and criteria separately for extensions.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/quadrature/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [有限・無限・多変数の定積分](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#definite-integrals-ja) (`definite-integrals`; quadpack-domain-selection, gk15-double-exponential, tensor-smolyak-dimensions)

#### 問題の図 (`method-problems-ja`)

##### [Gauss–Legendreと適応求積：厳密次数・推定誤差・予算切れ](https://hrkoyama.github.io/numerical-methods-atlas/problems/quadrature-moments/?lang=ja) (`quadrature-moments`)

![Gauss–Legendreの次数と適応Simpsonの要求公差を走査した保存誤差。指数・Lorentz型積分の解析値を参照し、推定誤差を厳密上界とは扱わない。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/results/gauss-adaptive-quadrature.png)

この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/quadrature-moments/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/quadrature-moments/?lang=ja#code-ja)

- [Gauss–Legendreと適応求積：厳密次数・推定誤差・予算切れ](https://hrkoyama.github.io/numerical-methods-atlas/validation/gauss-adaptive-quadrature/?lang=ja) (`gauss-adaptive-quadrature`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/atlas-foundations-2026-11-22.zip)

Legendreの3項漸化式からGauss節点と重みを構成し、2n−1次までの多項式モーメントと指数関数を検査します。適応Simpsonは指数関数とLorentz型ピークを積分し、解析積分・独立QUADPACKと比較します。

- [求積：狭いピーク・相殺・端点・誤差推定の盲点](https://hrkoyama.github.io/numerical-methods-atlas/validation/quadrature-conditioning/?lang=ja) (`quadrature-conditioning`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/atlas-foundations-conditioning-2026-11-22.zip)

Gauss次数と適応公差を走査し、狭いLorentzピーク、平方根端点、巨大な相殺、零積分、見逃すcompact bumpを解析積分とQUADPACKで検証します。

##### [領域別QUADPACKと有限Simpson対照](https://hrkoyama.github.io/numerical-methods-atlas/problems/quadpack-domain-selection/?lang=ja) (`quadpack-domain-selection`)

![活動Fourier周期の保存寄与と誤差・評価数 数学的な積分領域と次元は式・入力に示します。パラメータや誤差の図軸に物理空間の次元を割り当てません。 再現確認の合格は精度目標の全達成を意味しません。元の目標判定は達成25件・未達2件・計算不能3件です。FALSE/NAと失敗rawを保持します。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/results/quadpack-domain-selection-preview.png)

領域と重みを明示しfull_outputの活動prefixを保持。既存Simpson関数は不変。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/quadpack-domain-selection/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/quadpack-domain-selection/?lang=ja#code-ja)

- [領域別QUADPACKと有限Simpson対照](https://hrkoyama.github.io/numerical-methods-atlas/validation/quadpack-domain-selection/?lang=ja) (`quadpack-domain-selection`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/atlas-quadrature-controls-2026-11-25.zip)

15本の特殊化求積と15本のSimpson対照を固定入力で比較します。

##### [G7/K15と有限区間tanh-sinh](https://hrkoyama.github.io/numerical-methods-atlas/problems/gk15-double-exponential/?lang=ja) (`gk15-double-exponential`)

![保存された変換関数と有限窓誤差（連続tailは別量） 数学的な積分領域と次元は式・入力に示します。パラメータや誤差の図軸に物理空間の次元を割り当てません。 再現確認の合格は精度目標の全達成を意味しません。元の目標判定は達成26件・未達7件・計算不能0件です。FALSE/NAと失敗rawを保持します。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/results/gk15-double-exponential-preview.png)

共有15節点、G7次数13/K15次数23。DEは安定log式と全端点重みです。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/gk15-double-exponential/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/gk15-double-exponential/?lang=ja#code-ja)

- [G7/K15と有限区間tanh-sinh](https://hrkoyama.github.io/numerical-methods-atlas/validation/gk15-double-exponential/?lang=ja) (`gk15-double-exponential`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/atlas-quadrature-controls-2026-11-25.zip)

9本の適応GKと24本の固定DE和を比較します。

##### [2〜4次元テンソル・Smolyak対照](https://hrkoyama.github.io/numerical-methods-atlas/problems/tensor-smolyak-dimensions/?lang=ja) (`tensor-smolyak-dimensions`)

![実2次元節点と符号付き積分重み 数学的な積分領域と次元は式・入力に示します。パラメータや誤差の図軸に物理空間の次元を割り当てません。 再現確認の合格は精度目標の全達成を意味しません。元の目標判定は達成24件・未達18件・計算不能0件です。FALSE/NAと失敗rawを保持します。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/results/tensor-smolyak-dimensions-preview.png)

正規化dyadic角キーで同一節点を所有し、符号付き重みと評価台帳を保持。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/tensor-smolyak-dimensions/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/tensor-smolyak-dimensions/?lang=ja#code-ja)

- [2〜4次元テンソル・Smolyak対照](https://hrkoyama.github.io/numerical-methods-atlas/validation/tensor-smolyak-dimensions/?lang=ja) (`tensor-smolyak-dimensions`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/atlas-quadrature-controls-2026-11-25.zip)

滑らかな積と相互作用積の42本の固定cubatureを比較します。


#### 厳密解・参照解 (`method-references-ja`)

##### [Gauss–Legendreと適応求積：厳密次数・推定誤差・予算切れ](https://hrkoyama.github.io/numerical-methods-atlas/problems/quadrature-moments/?lang=ja#references-ja) (`quadrature-moments`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### [領域別QUADPACKと有限Simpson対照](https://hrkoyama.github.io/numerical-methods-atlas/problems/quadpack-domain-selection/?lang=ja#references-ja) (`quadpack-domain-selection`)

- [領域別QUADPACKと有限Simpson対照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-quadpack-domain-selection-ja) (`quadpack-domain-selection`; 同じ問題の参照; 解析参照)

Simpsonの特異節点失敗と未達精度を保存し、推定誤差の一般保証にしません。

[既存の参照図](/numerical-methods-atlas/validation/quadpack-domain-selection/?lang=ja#quadpack-domain-selection-ja-measurements)

##### [G7/K15と有限区間tanh-sinh](https://hrkoyama.github.io/numerical-methods-atlas/problems/gk15-double-exponential/?lang=ja#references-ja) (`gk15-double-exponential`)

- [G7/K15と有限区間tanh-sinh](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-gk15-double-exponential-ja) (`gk15-double-exponential`; 同じ問題の参照; 解析参照)

半無限exp-sinh/全実線sinh-sinhは未実装。無限台形SUMの省略項のboundは提供しません。

[既存の参照図](/numerical-methods-atlas/validation/gk15-double-exponential/?lang=ja#gk15-double-exponential-ja-measurements)

##### [2〜4次元テンソル・Smolyak対照](https://hrkoyama.github.io/numerical-methods-atlas/problems/tensor-smolyak-dimensions/?lang=ja#references-ja) (`tensor-smolyak-dimensions`)

- [2〜4次元テンソル・Smolyak対照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-tensor-smolyak-dimensions-ja) (`tensor-smolyak-dimensions`; 同じ問題の参照; 解析参照)

一般の誤差単調性、常時正重み、疎格子の費用優位は主張しません。物理PDEの空間ではありません。

[既存の参照図](/numerical-methods-atlas/validation/tensor-smolyak-dimensions/?lang=ja#tensor-smolyak-dimensions-ja-measurements)

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

##### 領域別QUADPACKと有限Simpson対照 (`quadpack-domain-selection`)

[領域別QUADPACKと有限Simpson対照](https://hrkoyama.github.io/numerical-methods-atlas/problems/quadpack-domain-selection/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/quadpack-domain-selection/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/atlas-quadrature-controls-2026-11-25.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/verification.json)

15本の特殊化求積と15本のSimpson対照を固定入力で比較します。

##### G7/K15と有限区間tanh-sinh (`gk15-double-exponential`)

[G7/K15と有限区間tanh-sinh](https://hrkoyama.github.io/numerical-methods-atlas/problems/gk15-double-exponential/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/gk15-double-exponential/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/atlas-quadrature-controls-2026-11-25.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/verification.json)

9本の適応GKと24本の固定DE和を比較します。

##### 2〜4次元テンソル・Smolyak対照 (`tensor-smolyak-dimensions`)

[2〜4次元テンソル・Smolyak対照](https://hrkoyama.github.io/numerical-methods-atlas/problems/tensor-smolyak-dimensions/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/tensor-smolyak-dimensions/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/atlas-quadrature-controls-2026-11-25.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/verification.json)

滑らかな積と相互作用積の42本の固定cubatureを比較します。

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
- [/code/validated-examples/2026-11-25/quadrature-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/run.py)
- [/code/validated-examples/2026-11-25/quadrature-controls/quadpack_adapter.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/quadpack_adapter.py)
- [/code/validated-examples/2026-11-25/quadrature-controls/simpson_baseline.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/simpson_baseline.py)
- [/code/validated-examples/2026-11-25/quadrature-controls/gk15.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/gk15.py)
- [/code/validated-examples/2026-11-25/quadrature-controls/double_exponential.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/double_exponential.py)
- [/code/validated-examples/2026-11-25/quadrature-controls/cubature.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/cubature.py)
- [/code/validated-examples/2026-11-25/quadrature-controls/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/experiments.py)
- [/code/validated-examples/2026-11-25/quadrature-controls/io_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/io_contract.py)
- [/code/validated-examples/2026-11-25/quadrature-controls/reference_cache.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/reference_cache.py)
- [/code/validated-examples/2026-11-25/quadrature-controls/references/direct_rule.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/references/direct_rule.py)
- [/code/validated-examples/2026-11-25/quadrature-controls/references/formulas.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/references/formulas.py)
- [/code/validated-examples/2026-11-25/quadrature-controls/references/interval.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/references/interval.py)
- [/code/validated-examples/2026-11-25/quadrature-controls/references/qualify.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/references/qualify.py)

###### 配布版のテスト

- [/code/validated-examples/2026-11-22/foundations/test_foundations.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/test_foundations.py)
- [/code/validated-examples/2026-11-22/foundations-conditioning/test_conditioning.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/test_conditioning.py)
- [/code/validated-examples/2026-11-25/quadrature-controls/test_quadrature.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/test_quadrature.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q
python run.py --input inputs.json --output output
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Finite, improper and multivariate definite integrals](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#definite-integrals-en) (`definite-integrals`; quadpack-domain-selection, gk15-double-exponential, tensor-smolyak-dimensions)

#### Problem figures (`method-problems-en`)

##### [Gauss–Legendre and adaptive quadrature: exactness, error estimates and budgets](https://hrkoyama.github.io/numerical-methods-atlas/problems/quadrature-moments/?lang=en) (`quadrature-moments`)

![Saved Gauss–Legendre order and adaptive-Simpson tolerance sweeps against analytic exponential/Lorentzian integrals; estimated errors are not rigorous bounds.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/results/gauss-adaptive-quadrature.png)

Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/quadrature-moments/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/quadrature-moments/?lang=en#code-en)

- [Gauss–Legendre and adaptive quadrature: exactness, error estimates and budgets](https://hrkoyama.github.io/numerical-methods-atlas/validation/gauss-adaptive-quadrature/?lang=en) (`gauss-adaptive-quadrature`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/atlas-foundations-2026-11-22.zip)

Construct Gaussian nodes/weights from the Legendre recurrence and test polynomial moments through degree 2n−1 and an exponential. Adaptive Simpson integrates exponential and Lorentzian peaks, against analytic integrals and independent QUADPACK.

- [Quadrature: narrow peaks, cancellation, endpoints and estimator blind spots](https://hrkoyama.github.io/numerical-methods-atlas/validation/quadrature-conditioning/?lang=en) (`quadrature-conditioning`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/atlas-foundations-conditioning-2026-11-22.zip)

Vary Gauss order and adaptive tolerance on narrow Lorentz peaks, a square-root endpoint, severe cancellation, a zero integral and a deliberately missed compact bump, using analytic integrals and QUADPACK.

##### [QUADPACK dispatch and finite Simpson companions](https://hrkoyama.github.io/numerical-methods-atlas/problems/quadpack-domain-selection/?lang=en) (`quadpack-domain-selection`)

![Saved active Fourier contributions and actual errors/call counts The formulas and inputs specify mathematical integration domains and dimensions. Parameter and error axes are not physical spatial coordinates. Passing reproduction checks does not mean that every accuracy goal was met. Original row outcomes: 25 met, 2 unmet and 3 not computable. False/NA outcomes and raw failures are retained.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/results/quadpack-domain-selection-preview.png)

Explicit domain/weight dispatch retains active full_output prefixes. The existing Simpson function is unchanged.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/quadpack-domain-selection/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/quadpack-domain-selection/?lang=en#code-en)

- [QUADPACK dispatch and finite Simpson companions](https://hrkoyama.github.io/numerical-methods-atlas/validation/quadpack-domain-selection/?lang=en) (`quadpack-domain-selection`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/atlas-quadrature-controls-2026-11-25.zip)

Fifteen specialized quadratures and fifteen Simpson companions use fixed inputs.

##### [G7/K15 and finite-interval tanh-sinh](https://hrkoyama.github.io/numerical-methods-atlas/problems/gk15-double-exponential/?lang=en) (`gk15-double-exponential`)

![Saved transformed integrands and finite-window defects; continuous tails are distinct The formulas and inputs specify mathematical integration domains and dimensions. Parameter and error axes are not physical spatial coordinates. Passing reproduction checks does not mean that every accuracy goal was met. Original row outcomes: 26 met, 7 unmet and 0 not computable. False/NA outcomes and raw failures are retained.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/results/gk15-double-exponential-preview.png)

Shared15-node G7 degree13/K15 degree23; DE uses stable logarithmic products and full endpoint weights.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/gk15-double-exponential/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/gk15-double-exponential/?lang=en#code-en)

- [G7/K15 and finite-interval tanh-sinh](https://hrkoyama.github.io/numerical-methods-atlas/validation/gk15-double-exponential/?lang=en) (`gk15-double-exponential`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/atlas-quadrature-controls-2026-11-25.zip)

Nine adaptive GK rows and twenty-four fixed DE sums are compared.

##### [Tensor and Smolyak controls in two to four dimensions](https://hrkoyama.github.io/numerical-methods-atlas/problems/tensor-smolyak-dimensions/?lang=en) (`tensor-smolyak-dimensions`)

![Actual two-dimensional nodes and signed integration weights The formulas and inputs specify mathematical integration domains and dimensions. Parameter and error axes are not physical spatial coordinates. Passing reproduction checks does not mean that every accuracy goal was met. Original row outcomes: 24 met, 18 unmet and 0 not computable. False/NA outcomes and raw failures are retained.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/results/tensor-smolyak-dimensions-preview.png)

Canonical dyadic angle keys own shared nodes; signed weights and call ledgers are retained.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/tensor-smolyak-dimensions/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/tensor-smolyak-dimensions/?lang=en#code-en)

- [Tensor and Smolyak controls in two to four dimensions](https://hrkoyama.github.io/numerical-methods-atlas/validation/tensor-smolyak-dimensions/?lang=en) (`tensor-smolyak-dimensions`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/atlas-quadrature-controls-2026-11-25.zip)

Forty-two fixed cubatures compare a smooth product and an interaction product.


#### Exact / reference solutions (`method-references-en`)

##### [Gauss–Legendre and adaptive quadrature: exactness, error estimates and budgets](https://hrkoyama.github.io/numerical-methods-atlas/problems/quadrature-moments/?lang=en#references-en) (`quadrature-moments`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### [QUADPACK dispatch and finite Simpson companions](https://hrkoyama.github.io/numerical-methods-atlas/problems/quadpack-domain-selection/?lang=en#references-en) (`quadpack-domain-selection`)

- [QUADPACK dispatch and finite Simpson companions](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-quadpack-domain-selection-en) (`quadpack-domain-selection`; Same-problem reference; Analytic reference)

Singular-node failures and unmet Simpson goals remain visible; error estimates are not general guarantees.

[Existing reference profile](/numerical-methods-atlas/validation/quadpack-domain-selection/?lang=en#quadpack-domain-selection-en-measurements)

##### [G7/K15 and finite-interval tanh-sinh](https://hrkoyama.github.io/numerical-methods-atlas/problems/gk15-double-exponential/?lang=en#references-en) (`gk15-double-exponential`)

- [G7/K15 and finite-interval tanh-sinh](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-gk15-double-exponential-en) (`gk15-double-exponential`; Same-problem reference; Analytic reference)

Half-line exp-sinh and whole-line sinh-sinh are unimplemented; no omitted infinite-grid sum bound is provided.

[Existing reference profile](/numerical-methods-atlas/validation/gk15-double-exponential/?lang=en#gk15-double-exponential-en-measurements)

##### [Tensor and Smolyak controls in two to four dimensions](https://hrkoyama.github.io/numerical-methods-atlas/problems/tensor-smolyak-dimensions/?lang=en#references-en) (`tensor-smolyak-dimensions`)

- [Tensor and Smolyak controls in two to four dimensions](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-tensor-smolyak-dimensions-en) (`tensor-smolyak-dimensions`; Same-problem reference; Analytic reference)

No general error monotonicity, positive-weight or cost-superiority claim; these are integration coordinates, not a physical PDE space.

[Existing reference profile](/numerical-methods-atlas/validation/tensor-smolyak-dimensions/?lang=en#tensor-smolyak-dimensions-en-measurements)

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

##### QUADPACK dispatch and finite Simpson companions (`quadpack-domain-selection`)

[QUADPACK dispatch and finite Simpson companions](https://hrkoyama.github.io/numerical-methods-atlas/problems/quadpack-domain-selection/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/quadpack-domain-selection/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/atlas-quadrature-controls-2026-11-25.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/verification.json)

Fifteen specialized quadratures and fifteen Simpson companions use fixed inputs.

##### G7/K15 and finite-interval tanh-sinh (`gk15-double-exponential`)

[G7/K15 and finite-interval tanh-sinh](https://hrkoyama.github.io/numerical-methods-atlas/problems/gk15-double-exponential/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/gk15-double-exponential/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/atlas-quadrature-controls-2026-11-25.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/verification.json)

Nine adaptive GK rows and twenty-four fixed DE sums are compared.

##### Tensor and Smolyak controls in two to four dimensions (`tensor-smolyak-dimensions`)

[Tensor and Smolyak controls in two to four dimensions](https://hrkoyama.github.io/numerical-methods-atlas/problems/tensor-smolyak-dimensions/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/tensor-smolyak-dimensions/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/atlas-quadrature-controls-2026-11-25.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/verification.json)

Forty-two fixed cubatures compare a smooth product and an interaction product.

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
- [/code/validated-examples/2026-11-25/quadrature-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/run.py)
- [/code/validated-examples/2026-11-25/quadrature-controls/quadpack_adapter.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/quadpack_adapter.py)
- [/code/validated-examples/2026-11-25/quadrature-controls/simpson_baseline.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/simpson_baseline.py)
- [/code/validated-examples/2026-11-25/quadrature-controls/gk15.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/gk15.py)
- [/code/validated-examples/2026-11-25/quadrature-controls/double_exponential.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/double_exponential.py)
- [/code/validated-examples/2026-11-25/quadrature-controls/cubature.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/cubature.py)
- [/code/validated-examples/2026-11-25/quadrature-controls/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/experiments.py)
- [/code/validated-examples/2026-11-25/quadrature-controls/io_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/io_contract.py)
- [/code/validated-examples/2026-11-25/quadrature-controls/reference_cache.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/reference_cache.py)
- [/code/validated-examples/2026-11-25/quadrature-controls/references/direct_rule.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/references/direct_rule.py)
- [/code/validated-examples/2026-11-25/quadrature-controls/references/formulas.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/references/formulas.py)
- [/code/validated-examples/2026-11-25/quadrature-controls/references/interval.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/references/interval.py)
- [/code/validated-examples/2026-11-25/quadrature-controls/references/qualify.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/references/qualify.py)

###### Package tests

- [/code/validated-examples/2026-11-22/foundations/test_foundations.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/test_foundations.py)
- [/code/validated-examples/2026-11-22/foundations-conditioning/test_conditioning.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/test_conditioning.py)
- [/code/validated-examples/2026-11-25/quadrature-controls/test_quadrature.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/test_quadrature.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q
python run.py --input inputs.json --output output
```
