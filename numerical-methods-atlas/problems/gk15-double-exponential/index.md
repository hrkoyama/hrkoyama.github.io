# G7/K15と有限区間tanh-sinh / G7/K15 and finite-interval tanh-sinh

https://hrkoyama.github.io/numerical-methods-atlas/problems/gk15-double-exponential/

## 日本語

[保存された変換関数と有限窓誤差（連続tailは別量） 数学的な積分領域と次元は式・入力に示します。パラメータや誤差の図軸に物理空間の次元を割り当てません。 再現確認の合格は精度目標の全達成を意味しません。元の目標判定は達成26件・未達7件・計算不能0件です。FALSE/NAと失敗rawを保持します。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/results/gk15-double-exponential-preview.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-quadrature-controls/#gk15-double-exponential) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#gk15-double-exponential)

### 方程式・問題の定義

exp(x)、x^(-1/3)、−log(x)を[0,1]で積分。h=1/2〜1/16、切断T=3/4。

#### [有限・無限・多変数の定積分](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#definite-integrals-ja)

$$
I_D(f)=\int_D f(\mathbf x)\,d\mathbf x
$$

領域・重み・特異性と有限変換和の定義を確認する数学的求積問題です。

### 厳密解・参照解

解析区間参照で全誤差、連続tail、有限窓誤差を分離します。

#### [G7/K15と有限区間tanh-sinh](https://hrkoyama.github.io/numerical-methods-atlas/validation/gk15-double-exponential/?lang=ja#gk15-double-exponential-ja-measurements)

解析解 · 同じ問題の参照

Q_h^T=h\sum_{k=-T/h}^{T/h}f(\phi(kh))\phi^{\prime}(kh),\quad\phi(t)=\tfrac12[1+\tanh(\tfrac\pi2\sinh t)];\quad\int_0^1(e^x,x^{-1/3},-\log x)\,dx=(e-1,3/2,1)

exp(x)、x^(-1/3)、−log(x)を[0,1]で積分。h=1/2〜1/16、切断T=3/4。

半無限exp-sinh/全実線sinh-sinhは未実装。無限台形SUMの省略項のboundは提供しません。

#### G7/K15と有限区間tanh-sinh

解析区間参照で全誤差、連続tail、有限窓誤差を分離します。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/gk15-double-exponential/?lang=ja)

### 計算法

共有15節点、G7次数13/K15次数23。DEは安定log式と全端点重みです。

- [Gauss求積・適応積分](https://hrkoyama.github.io/numerical-methods-atlas/methods/quadrature/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [Gauss–Kronrod G7/K15](https://hrkoyama.github.io/numerical-methods-atlas/methods/gauss-kronrod/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [tanh–sinh二重指数求積](https://hrkoyama.github.io/numerical-methods-atlas/methods/tanh-sinh/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [G7/K15と有限区間tanh-sinh](https://hrkoyama.github.io/numerical-methods-atlas/validation/gk15-double-exponential/?lang=ja)

補助実行例

9本の適応GKと24本の固定DE和を比較します。

exp(x)、x^(-1/3)、−log(x)を[0,1]で積分。h=1/2〜1/16、切断T=3/4。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/atlas-quadrature-controls-2026-11-25.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

半無限exp-sinh/全実線sinh-sinhは未実装。無限台形SUMの省略項のboundは提供しません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-25/quadrature-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/run.py)
- [/code/validated-examples/2026-11-25/quadrature-controls/gk15.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/gk15.py)
- [/code/validated-examples/2026-11-25/quadrature-controls/double_exponential.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/double_exponential.py)
- [/code/validated-examples/2026-11-25/quadrature-controls/test_quadrature.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/test_quadrature.py)

## English

[Saved transformed integrands and finite-window defects; continuous tails are distinct The formulas and inputs specify mathematical integration domains and dimensions. Parameter and error axes are not physical spatial coordinates. Passing reproduction checks does not mean that every accuracy goal was met. Original row outcomes: 26 met, 7 unmet and 0 not computable. False/NA outcomes and raw failures are retained.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/results/gk15-double-exponential-preview.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-quadrature-controls/#gk15-double-exponential) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#gk15-double-exponential-en)

### Equations and problem definitions

Integrate exp(x), x^(-1/3) and -log(x) on[0,1], with h from1/2 to1/16 and cutoffs3/4.

#### [Finite, improper and multivariate definite integrals](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#definite-integrals-en)

$$
I_D(f)=\int_D f(\mathbf x)\,d\mathbf x
$$

Mathematical quadrature problems with explicit domains, weights, singularities and finite transformed-sum conventions.

### Exact and reference solutions

Analytic interval references separate total error, continuous tail and finite-window defect.

#### [G7/K15 and finite-interval tanh-sinh](https://hrkoyama.github.io/numerical-methods-atlas/validation/gk15-double-exponential/?lang=en#gk15-double-exponential-en-measurements)

Analytic reference · Reference for the same problem

Q_h^T=h\sum_{k=-T/h}^{T/h}f(\phi(kh))\phi^{\prime}(kh),\quad\phi(t)=\tfrac12[1+\tanh(\tfrac\pi2\sinh t)];\quad\int_0^1(e^x,x^{-1/3},-\log x)\,dx=(e-1,3/2,1)

Integrate exp(x), x^(-1/3) and -log(x) on[0,1], with h from1/2 to1/16 and cutoffs3/4.

Half-line exp-sinh and whole-line sinh-sinh are unimplemented; no omitted infinite-grid sum bound is provided.

#### G7/K15 and finite-interval tanh-sinh

Analytic interval references separate total error, continuous tail and finite-window defect.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/gk15-double-exponential/?lang=en)

### Numerical methods

Shared15-node G7 degree13/K15 degree23; DE uses stable logarithmic products and full endpoint weights.

- [Gaussian and adaptive quadrature](https://hrkoyama.github.io/numerical-methods-atlas/methods/quadrature/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Gauss–Kronrod G7/K15](https://hrkoyama.github.io/numerical-methods-atlas/methods/gauss-kronrod/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Tanh–sinh double-exponential quadrature](https://hrkoyama.github.io/numerical-methods-atlas/methods/tanh-sinh/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [G7/K15 and finite-interval tanh-sinh](https://hrkoyama.github.io/numerical-methods-atlas/validation/gk15-double-exponential/?lang=en)

Supplementary execution example

Nine adaptive GK rows and twenty-four fixed DE sums are compared.

Integrate exp(x), x^(-1/3) and -log(x) on[0,1], with h from1/2 to1/16 and cutoffs3/4.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/atlas-quadrature-controls-2026-11-25.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

Half-line exp-sinh and whole-line sinh-sinh are unimplemented; no omitted infinite-grid sum bound is provided.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-25/quadrature-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/run.py)
- [/code/validated-examples/2026-11-25/quadrature-controls/gk15.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/gk15.py)
- [/code/validated-examples/2026-11-25/quadrature-controls/double_exponential.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/double_exponential.py)
- [/code/validated-examples/2026-11-25/quadrature-controls/test_quadrature.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/test_quadrature.py)
