# 領域別QUADPACKと有限Simpson対照 / QUADPACK dispatch and finite Simpson companions

https://hrkoyama.github.io/numerical-methods-atlas/problems/quadpack-domain-selection/

## 日本語

[活動Fourier周期の保存寄与と誤差・評価数 数学的な積分領域と次元は式・入力に示します。パラメータや誤差の図軸に物理空間の次元を割り当てません。 再現確認の合格は精度目標の全達成を意味しません。元の目標判定は達成25件・未達2件・計算不能3件です。FALSE/NAと失敗rawを保持します。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/results/quadpack-domain-selection-preview.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-quadrature-controls/#quadpack-domain-selection) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#quadpack-domain-selection)

### 方程式・問題の定義

無限Gaussian、有限振動2周波数、半無限Fourier、内部特異点。絶対公差1e-6/1e-8/1e-10、epsrel=0。

#### [有限・無限・多変数の定積分](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#definite-integrals-ja)

$$
I_D(f)=\int_D f(\mathbf x)\,d\mathbf x
$$

領域・重み・特異性と有限変換和の定義を確認する数学的求積問題です。

### 厳密解・参照解

独立の解析区間参照と実callback数を照合します。有限Gaussianは点値でなく厳密区間です。

#### [領域別QUADPACKと有限Simpson対照](https://hrkoyama.github.io/numerical-methods-atlas/validation/quadpack-domain-selection/?lang=ja#quadpack-domain-selection-ja-measurements)

解析解 · 同じ問題の参照

\int_{-\infty}^{\infty}e^{-x^2}\,dx=\sqrt\pi;\quad\int_0^1e^{-x}\sin(\omega x)\,dx=\frac{\omega-e^{-1}(\sin\omega+\omega\cos\omega)}{1+\omega^2};\quad\int_0^\infty e^{-x}\sin(8x)\,dx=\frac8{65};\quad\int_0^1|x-3/8|^{-1/2}\,dx=2(\sqrt{3/8}+\sqrt{5/8})

無限Gaussian、有限振動2周波数、半無限Fourier、内部特異点。絶対公差1e-6/1e-8/1e-10、epsrel=0。

Simpsonの特異節点失敗と未達精度を保存し、推定誤差の一般保証にしません。

#### 領域別QUADPACKと有限Simpson対照

独立の解析区間参照と実callback数を照合します。有限Gaussianは点値でなく厳密区間です。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/quadpack-domain-selection/?lang=ja)

### 計算法

領域と重みを明示しfull_outputの活動prefixを保持。既存Simpson関数は不変。

- [Gauss求積・適応積分](https://hrkoyama.github.io/numerical-methods-atlas/methods/quadrature/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [領域別QUADPACKと有限Simpson対照](https://hrkoyama.github.io/numerical-methods-atlas/validation/quadpack-domain-selection/?lang=ja)

補助実行例

15本の特殊化求積と15本のSimpson対照を固定入力で比較します。

無限Gaussian、有限振動2周波数、半無限Fourier、内部特異点。絶対公差1e-6/1e-8/1e-10、epsrel=0。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/atlas-quadrature-controls-2026-11-25.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

Simpsonの特異節点失敗と未達精度を保存し、推定誤差の一般保証にしません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-25/quadrature-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/run.py)
- [/code/validated-examples/2026-11-25/quadrature-controls/quadpack_adapter.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/quadpack_adapter.py)
- [/code/validated-examples/2026-11-25/quadrature-controls/simpson_baseline.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/simpson_baseline.py)
- [/code/validated-examples/2026-11-25/quadrature-controls/test_quadrature.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/test_quadrature.py)

## English

[Saved active Fourier contributions and actual errors/call counts The formulas and inputs specify mathematical integration domains and dimensions. Parameter and error axes are not physical spatial coordinates. Passing reproduction checks does not mean that every accuracy goal was met. Original row outcomes: 25 met, 2 unmet and 3 not computable. False/NA outcomes and raw failures are retained.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/results/quadpack-domain-selection-preview.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-quadrature-controls/#quadpack-domain-selection) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#quadpack-domain-selection-en)

### Equations and problem definitions

Whole-line Gaussian, two finite frequencies, half-line Fourier and an internal singularity; absolute tolerances1e-6/1e-8/1e-10 and epsrel0.

#### [Finite, improper and multivariate definite integrals](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#definite-integrals-en)

$$
I_D(f)=\int_D f(\mathbf x)\,d\mathbf x
$$

Mathematical quadrature problems with explicit domains, weights, singularities and finite transformed-sum conventions.

### Exact and reference solutions

Independent analytic interval references and actual callback counts are checked. The finite Gaussian target is an interval, not an invented erf value.

#### [QUADPACK dispatch and finite Simpson companions](https://hrkoyama.github.io/numerical-methods-atlas/validation/quadpack-domain-selection/?lang=en#quadpack-domain-selection-en-measurements)

Analytic reference · Reference for the same problem

\int_{-\infty}^{\infty}e^{-x^2}\,dx=\sqrt\pi;\quad\int_0^1e^{-x}\sin(\omega x)\,dx=\frac{\omega-e^{-1}(\sin\omega+\omega\cos\omega)}{1+\omega^2};\quad\int_0^\infty e^{-x}\sin(8x)\,dx=\frac8{65};\quad\int_0^1|x-3/8|^{-1/2}\,dx=2(\sqrt{3/8}+\sqrt{5/8})

Whole-line Gaussian, two finite frequencies, half-line Fourier and an internal singularity; absolute tolerances1e-6/1e-8/1e-10 and epsrel0.

Singular-node failures and unmet Simpson goals remain visible; error estimates are not general guarantees.

#### QUADPACK dispatch and finite Simpson companions

Independent analytic interval references and actual callback counts are checked. The finite Gaussian target is an interval, not an invented erf value.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/quadpack-domain-selection/?lang=en)

### Numerical methods

Explicit domain/weight dispatch retains active full_output prefixes. The existing Simpson function is unchanged.

- [Gaussian and adaptive quadrature](https://hrkoyama.github.io/numerical-methods-atlas/methods/quadrature/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [QUADPACK dispatch and finite Simpson companions](https://hrkoyama.github.io/numerical-methods-atlas/validation/quadpack-domain-selection/?lang=en)

Supplementary execution example

Fifteen specialized quadratures and fifteen Simpson companions use fixed inputs.

Whole-line Gaussian, two finite frequencies, half-line Fourier and an internal singularity; absolute tolerances1e-6/1e-8/1e-10 and epsrel0.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/atlas-quadrature-controls-2026-11-25.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

Singular-node failures and unmet Simpson goals remain visible; error estimates are not general guarantees.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-25/quadrature-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/run.py)
- [/code/validated-examples/2026-11-25/quadrature-controls/quadpack_adapter.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/quadpack_adapter.py)
- [/code/validated-examples/2026-11-25/quadrature-controls/simpson_baseline.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/simpson_baseline.py)
- [/code/validated-examples/2026-11-25/quadrature-controls/test_quadrature.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/test_quadrature.py)
