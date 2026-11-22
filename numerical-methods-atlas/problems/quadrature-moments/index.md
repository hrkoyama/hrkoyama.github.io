# Gauss–Legendreと適応求積：厳密次数・推定誤差・予算切れ / Gauss–Legendre and adaptive quadrature: exactness, error estimates and budgets

https://hrkoyama.github.io/numerical-methods-atlas/problems/quadrature-moments/

## 日本語

[Gauss–Legendreの次数と適応Simpsonの要求公差を走査した保存誤差。指数・Lorentz型積分の解析値を参照し、推定誤差を厳密上界とは扱わない。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/results/gauss-adaptive-quadrature.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-foundations/#gauss-adaptive-quadrature) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#quadrature-moments)

### 方程式・問題の定義

定積分と多項式モーメントの求積問題です。支配PDEの求解ではありません。

#### Gauss–Legendreと適応求積：厳密次数・推定誤差・予算切れ

補助実行例 · 実行例の定義・検証式

$$
\int_{-1}^{1}f(x)\,dx\simeq\sum_{j=1}^{n}w_jf(x_j)
$$

$$
E_{\mathrm{est}}=|S_{\mathrm{left}}+S_{\mathrm{right}}-S_{\mathrm{whole}}|/15
$$

Legendreの3項漸化式からGauss節点と重みを構成し、2n−1次までの多項式モーメントと指数関数を検査します。適応Simpsonは指数関数とLorentz型ピークを積分し、解析積分・独立QUADPACKと比較します。

### 厳密解・参照解

多項式モーメントの既知積分値と独立求積参照を使い、厳密性・推定誤差・評価回数制限を確認します。

#### Gauss–Legendreと適応求積：厳密次数・推定誤差・予算切れ

全指定次数の多項式モーメント、SciPy roots_legendreの節点・重みとの差、解析exp積分の次数収束、解析atan積分とSciPy quadへの一致を測ります。公差を厳しくしたときの評価数と誤差を示し、5評価の強制予算切れ、非有限関数値も検査します。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/gauss-adaptive-quadrature/?lang=ja)

### 計算法

この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。

- [Gauss求積・適応積分](https://hrkoyama.github.io/numerical-methods-atlas/methods/quadrature/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [Gauss–Legendreと適応求積：厳密次数・推定誤差・予算切れ](https://hrkoyama.github.io/numerical-methods-atlas/validation/gauss-adaptive-quadrature/?lang=ja)

補助実行例

Legendreの3項漸化式からGauss節点と重みを構成し、2n−1次までの多項式モーメントと指数関数を検査します。適応Simpsonは指数関数とLorentz型ピークを積分し、解析積分・独立QUADPACKと比較します。

有限区間上の滑らかな実関数、無次元の積分です。固定Gauss次数2・4・8・16と、適応絶対公差10⁻⁵・10⁻⁷・10⁻⁹を別々に走査します。両端特異点・不連続・無限区間は今回の入力では扱いません。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/atlas-foundations-2026-11-22.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

Simpsonの局所推定は任意の関数に対する厳密な誤差上界ではありません。高周波の見落とし、特異点、丸め誤差の停滞を一般に解決する実装ではなく、Gauss–KronrodやQUADPACK全体の再実装でもありません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-22/foundations/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/run.py)
- [/code/validated-examples/2026-11-22/foundations/test_foundations.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/test_foundations.py)

## English

[Saved Gauss–Legendre order and adaptive-Simpson tolerance sweeps against analytic exponential/Lorentzian integrals; estimated errors are not rigorous bounds.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/results/gauss-adaptive-quadrature.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-foundations/#gauss-adaptive-quadrature) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#quadrature-moments-en)

### Equations and problem definitions

Definite-integral and polynomial-moment quadrature, rather than a governing-PDE solve.

#### Gauss–Legendre and adaptive quadrature: exactness, error estimates and budgets

Supplementary execution example · Example definition or validation formula

$$
\int_{-1}^{1}f(x)\,dx\simeq\sum_{j=1}^{n}w_jf(x_j)
$$

$$
E_{\mathrm{est}}=|S_{\mathrm{left}}+S_{\mathrm{right}}-S_{\mathrm{whole}}|/15
$$

Construct Gaussian nodes/weights from the Legendre recurrence and test polynomial moments through degree 2n−1 and an exponential. Adaptive Simpson integrates exponential and Lorentzian peaks, against analytic integrals and independent QUADPACK.

### Exact and reference solutions

Use known polynomial integrals and independent quadrature references to check exactness, estimated errors and evaluation budgets.

#### Gauss–Legendre and adaptive quadrature: exactness, error estimates and budgets

Measure polynomial moments for every chosen order, node/weight differences from SciPy roots_legendre, order refinement for the analytic exponential integral, and agreement with analytic arctangent and SciPy quad references. Store evaluation counts/errors as tolerance tightens; test forced exhaustion after five evaluations and nonfinite integrands.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/gauss-adaptive-quadrature/?lang=en)

### Numerical methods

Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.

- [Gaussian and adaptive quadrature](https://hrkoyama.github.io/numerical-methods-atlas/methods/quadrature/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Gauss–Legendre and adaptive quadrature: exactness, error estimates and budgets](https://hrkoyama.github.io/numerical-methods-atlas/validation/gauss-adaptive-quadrature/?lang=en)

Supplementary execution example

Construct Gaussian nodes/weights from the Legendre recurrence and test polynomial moments through degree 2n−1 and an exponential. Adaptive Simpson integrates exponential and Lorentzian peaks, against analytic integrals and independent QUADPACK.

Dimensionless smooth real functions on finite intervals. Fixed Gauss orders 2/4/8/16 and adaptive absolute tolerances 10⁻⁵/10⁻⁷/10⁻⁹ are swept separately. Endpoint singularities, discontinuities and infinite intervals are not covered by these inputs.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/atlas-foundations-2026-11-22.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

The local Simpson estimate is not a rigorous error bound for arbitrary functions. The implementation does not generally solve missed high frequencies, singularities or roundoff stagnation, and it is not a reimplementation of Gauss–Kronrod or all of QUADPACK.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-22/foundations/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/run.py)
- [/code/validated-examples/2026-11-22/foundations/test_foundations.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/test_foundations.py)
