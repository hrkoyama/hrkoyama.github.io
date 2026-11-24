# 領域別・二重指数・疎格子求積

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-quadrature-controls/

この章に登録された手法・問題・実行例の関連資料です。 固定した積分を適用条件に応じて比較し、推定誤差・実誤差・予算終了・未解像対照を区別します。

## 手法

- [Gauss求積・適応積分](<https://hrkoyama.github.io/numerical-methods-atlas/methods/quadrature/?lang=ja>)

  領域と重みを明示しfull_outputの活動prefixを保持。既存Simpson関数は不変。
- [Gauss求積・適応積分](<https://hrkoyama.github.io/numerical-methods-atlas/methods/quadrature/?lang=ja>)

  共有15節点、G7次数13/K15次数23。DEは安定log式と全端点重みです。
- [Gauss–Kronrod G7/K15](<https://hrkoyama.github.io/numerical-methods-atlas/methods/gauss-kronrod/?lang=ja>)

  共有15節点、G7次数13/K15次数23。DEは安定log式と全端点重みです。
- [tanh–sinh二重指数求積](<https://hrkoyama.github.io/numerical-methods-atlas/methods/tanh-sinh/?lang=ja>)

  共有15節点、G7次数13/K15次数23。DEは安定log式と全端点重みです。
- [Gauss求積・適応積分](<https://hrkoyama.github.io/numerical-methods-atlas/methods/quadrature/?lang=ja>)

  正規化dyadic角キーで同一節点を所有し、符号付き重みと評価台帳を保持。
- [Smolyak疎格子求積](<https://hrkoyama.github.io/numerical-methods-atlas/methods/smolyak-sparse-grid/?lang=ja>)

  正規化dyadic角キーで同一節点を所有し、符号付き重みと評価台帳を保持。
- [Gauss求積・適応積分](<https://hrkoyama.github.io/numerical-methods-atlas/methods/quadrature/?lang=ja>)
- [Gauss–Kronrod G7/K15](<https://hrkoyama.github.io/numerical-methods-atlas/methods/gauss-kronrod/?lang=ja>)
- [tanh–sinh二重指数求積](<https://hrkoyama.github.io/numerical-methods-atlas/methods/tanh-sinh/?lang=ja>)
- [Smolyak疎格子求積](<https://hrkoyama.github.io/numerical-methods-atlas/methods/smolyak-sparse-grid/?lang=ja>)

## 方程式

- [有限・無限・多変数の定積分](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#definite-integrals-ja>)

  領域・重み・特異性と有限変換和の定義を確認する数学的求積問題です。 無限Gaussian、有限振動2周波数、半無限Fourier、内部特異点。絶対公差1e-6/1e-8/1e-10、epsrel=0。
- [有限・無限・多変数の定積分](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#definite-integrals-ja>)

  領域・重み・特異性と有限変換和の定義を確認する数学的求積問題です。 exp(x)、x^(-1/3)、−log(x)を[0,1]で積分。h=1/2〜1/16、切断T=3/4。
- [有限・無限・多変数の定積分](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#definite-integrals-ja>)

  領域・重み・特異性と有限変換和の定義を確認する数学的求積問題です。 [0,1]^d、d=2/3/4。テンソルlevel1/2/3、疎格子level1/2/3/4。
- [有限・無限・多変数の定積分](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#definite-integrals-ja>)

  領域・重み・特異性と有限変換和の定義を確認する数学的求積問題です。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/quadpack-domain-selection/?lang=ja#quadpack-domain-selection-ja-algorithm>)

  領域と重みを明示しfull_outputの活動prefixを保持。既存Simpson関数は不変。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/gk15-double-exponential/?lang=ja#gk15-double-exponential-ja-algorithm>)

  共有15節点、G7次数13/K15次数23。DEは安定log式と全端点重みです。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/tensor-smolyak-dimensions/?lang=ja#tensor-smolyak-dimensions-ja-algorithm>)

  正規化dyadic角キーで同一節点を所有し、符号付き重みと評価台帳を保持。

## 問題の図

- [領域別QUADPACKと有限Simpson対照](<https://hrkoyama.github.io/numerical-methods-atlas/problems/quadpack-domain-selection/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/results/quadpack-domain-selection-preview.png
- [G7/K15と有限区間tanh-sinh](<https://hrkoyama.github.io/numerical-methods-atlas/problems/gk15-double-exponential/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/results/gk15-double-exponential-preview.png
- [2〜4次元テンソル・Smolyak対照](<https://hrkoyama.github.io/numerical-methods-atlas/problems/tensor-smolyak-dimensions/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/results/tensor-smolyak-dimensions-preview.png
- [領域別QUADPACKと有限Simpson対照](<https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/results/quadpack-domain-selection.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/results/quadpack-domain-selection.png
- [G7/K15と有限区間tanh-sinh](<https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/results/gk15-double-exponential.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/results/gk15-double-exponential.png
- [2〜4次元テンソル・Smolyak対照](<https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/results/tensor-smolyak-dimensions.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/results/tensor-smolyak-dimensions.png

## 厳密解・参照解

- [領域別QUADPACKと有限Simpson対照：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/quadpack-domain-selection/?lang=ja#references-ja>)

  独立の解析区間参照と実callback数を照合します。有限Gaussianは点値でなく厳密区間です。
- [領域別QUADPACKと有限Simpson対照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-quadpack-domain-selection-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 無限Gaussian、有限振動2周波数、半無限Fourier、内部特異点。絶対公差1e-6/1e-8/1e-10、epsrel=0。 Simpsonの特異節点失敗と未達精度を保存し、推定誤差の一般保証にしません。
- [G7/K15と有限区間tanh-sinh：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/gk15-double-exponential/?lang=ja#references-ja>)

  解析区間参照で全誤差、連続tail、有限窓誤差を分離します。
- [G7/K15と有限区間tanh-sinh](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-gk15-double-exponential-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 exp(x)、x^(-1/3)、−log(x)を[0,1]で積分。h=1/2〜1/16、切断T=3/4。 半無限exp-sinh/全実線sinh-sinhは未実装。無限台形SUMの省略項のboundは提供しません。
- [2〜4次元テンソル・Smolyak対照：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/tensor-smolyak-dimensions/?lang=ja#references-ja>)

  解析積分と独立Delta/combination組立を区別し、L<dの相互作用未解像を可視化。
- [2〜4次元テンソル・Smolyak対照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-tensor-smolyak-dimensions-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 [0,1]^d、d=2/3/4。テンソルlevel1/2/3、疎格子level1/2/3/4。 一般の誤差単調性、常時正重み、疎格子の費用優位は主張しません。物理PDEの空間ではありません。
- [領域別QUADPACKと有限Simpson対照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-quadpack-domain-selection-ja>)
  reference_kind: analytic

  解析解 無限Gaussian、有限振動2周波数、半無限Fourier、内部特異点。絶対公差1e-6/1e-8/1e-10、epsrel=0。
- [G7/K15と有限区間tanh-sinh](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-gk15-double-exponential-ja>)
  reference_kind: analytic

  解析解 exp(x)、x^(-1/3)、−log(x)を[0,1]で積分。h=1/2〜1/16、切断T=3/4。
- [2〜4次元テンソル・Smolyak対照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-tensor-smolyak-dimensions-ja>)
  reference_kind: analytic

  解析解 [0,1]^d、d=2/3/4。テンソルlevel1/2/3、疎格子level1/2/3/4。
- [領域別QUADPACKと有限Simpson対照：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/quadpack-domain-selection/?lang=ja#quadpack-domain-selection-ja-validation>)

  独立の解析区間参照と実callback数を照合します。有限Gaussianは点値でなく厳密区間です。
- [領域別QUADPACKと有限Simpson対照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-quadpack-domain-selection-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 無限Gaussian、有限振動2周波数、半無限Fourier、内部特異点。絶対公差1e-6/1e-8/1e-10、epsrel=0。 Simpsonの特異節点失敗と未達精度を保存し、推定誤差の一般保証にしません。
- [G7/K15と有限区間tanh-sinh：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/gk15-double-exponential/?lang=ja#gk15-double-exponential-ja-validation>)

  解析区間参照で全誤差、連続tail、有限窓誤差を分離します。
- [G7/K15と有限区間tanh-sinh](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-gk15-double-exponential-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 exp(x)、x^(-1/3)、−log(x)を[0,1]で積分。h=1/2〜1/16、切断T=3/4。 半無限exp-sinh/全実線sinh-sinhは未実装。無限台形SUMの省略項のboundは提供しません。
- [2〜4次元テンソル・Smolyak対照：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/tensor-smolyak-dimensions/?lang=ja#tensor-smolyak-dimensions-ja-validation>)

  解析積分と独立Delta/combination組立を区別し、L<dの相互作用未解像を可視化。
- [2〜4次元テンソル・Smolyak対照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-tensor-smolyak-dimensions-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 [0,1]^d、d=2/3/4。テンソルlevel1/2/3、疎格子level1/2/3/4。 一般の誤差単調性、常時正重み、疎格子の費用優位は主張しません。物理PDEの空間ではありません。

## コード・検証

- [領域別QUADPACKと有限Simpson対照](<https://hrkoyama.github.io/numerical-methods-atlas/validation/quadpack-domain-selection/?lang=ja>)
  availability: run

  15本の特殊化求積と15本のSimpson対照を固定入力で比較します。
- [G7/K15と有限区間tanh-sinh](<https://hrkoyama.github.io/numerical-methods-atlas/validation/gk15-double-exponential/?lang=ja>)
  availability: run

  9本の適応GKと24本の固定DE和を比較します。
- [2〜4次元テンソル・Smolyak対照](<https://hrkoyama.github.io/numerical-methods-atlas/validation/tensor-smolyak-dimensions/?lang=ja>)
  availability: run

  滑らかな積と相互作用積の42本の固定cubatureを比較します。
