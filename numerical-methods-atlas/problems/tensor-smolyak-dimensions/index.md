# 2〜4次元テンソル・Smolyak対照 / Tensor and Smolyak controls in two to four dimensions

https://hrkoyama.github.io/numerical-methods-atlas/problems/tensor-smolyak-dimensions/

## 日本語

[実2次元節点と符号付き積分重み 数学的な積分領域と次元は式・入力に示します。パラメータや誤差の図軸に物理空間の次元を割り当てません。 再現確認の合格は精度目標の全達成を意味しません。元の目標判定は達成24件・未達18件・計算不能0件です。FALSE/NAと失敗rawを保持します。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/results/tensor-smolyak-dimensions-preview.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-quadrature-controls/#tensor-smolyak-dimensions) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#tensor-smolyak-dimensions)

### 方程式・問題の定義

[0,1]^d、d=2/3/4。テンソルlevel1/2/3、疎格子level1/2/3/4。

#### [有限・無限・多変数の定積分](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#definite-integrals-ja)

$$
I_D(f)=\int_D f(\mathbf x)\,d\mathbf x
$$

領域・重み・特異性と有限変換和の定義を確認する数学的求積問題です。

### 厳密解・参照解

解析積分と独立Delta/combination組立を区別し、L<dの相互作用未解像を可視化。

#### [2〜4次元テンソル・Smolyak対照](https://hrkoyama.github.io/numerical-methods-atlas/validation/tensor-smolyak-dimensions/?lang=ja#tensor-smolyak-dimensions-ja-measurements)

解析解 · 同じ問題の参照

\int_{[0,1]^d}\prod_{j=1}^de^{a_jx_j}\,d\mathbf x=\prod_{j=1}^d\frac{e^{a_j}-1}{a_j},\quad\int_{[0,1]^d}\prod_{j=1}^d(x_j-1/2)^2\,d\mathbf x=12^{-d};\quad A_L=\sum_{|\ell|_1\le L}\bigotimes_{j=1}^d(Q_{\ell_j}-Q_{\ell_j-1}),\quad Q_{-1}=0

[0,1]^d、d=2/3/4。テンソルlevel1/2/3、疎格子level1/2/3/4。

一般の誤差単調性、常時正重み、疎格子の費用優位は主張しません。物理PDEの空間ではありません。

#### 2〜4次元テンソル・Smolyak対照

解析積分と独立Delta/combination組立を区別し、L<dの相互作用未解像を可視化。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/tensor-smolyak-dimensions/?lang=ja)

### 計算法

正規化dyadic角キーで同一節点を所有し、符号付き重みと評価台帳を保持。

- [Gauss求積・適応積分](https://hrkoyama.github.io/numerical-methods-atlas/methods/quadrature/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [Smolyak疎格子求積](https://hrkoyama.github.io/numerical-methods-atlas/methods/smolyak-sparse-grid/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [2〜4次元テンソル・Smolyak対照](https://hrkoyama.github.io/numerical-methods-atlas/validation/tensor-smolyak-dimensions/?lang=ja)

補助実行例

滑らかな積と相互作用積の42本の固定cubatureを比較します。

[0,1]^d、d=2/3/4。テンソルlevel1/2/3、疎格子level1/2/3/4。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/atlas-quadrature-controls-2026-11-25.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

一般の誤差単調性、常時正重み、疎格子の費用優位は主張しません。物理PDEの空間ではありません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-25/quadrature-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/run.py)
- [/code/validated-examples/2026-11-25/quadrature-controls/cubature.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/cubature.py)
- [/code/validated-examples/2026-11-25/quadrature-controls/test_quadrature.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/test_quadrature.py)

## English

[Actual two-dimensional nodes and signed integration weights The formulas and inputs specify mathematical integration domains and dimensions. Parameter and error axes are not physical spatial coordinates. Passing reproduction checks does not mean that every accuracy goal was met. Original row outcomes: 24 met, 18 unmet and 0 not computable. False/NA outcomes and raw failures are retained.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/results/tensor-smolyak-dimensions-preview.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-quadrature-controls/#tensor-smolyak-dimensions) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#tensor-smolyak-dimensions-en)

### Equations and problem definitions

The integration domain is[0,1]^d for d2/3/4; tensor levels1/2/3 and sparse levels1/2/3/4.

#### [Finite, improper and multivariate definite integrals](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#definite-integrals-en)

$$
I_D(f)=\int_D f(\mathbf x)\,d\mathbf x
$$

Mathematical quadrature problems with explicit domains, weights, singularities and finite transformed-sum conventions.

### Exact and reference solutions

Analytic integrals are distinct from companion Delta/combination assembly; interaction underresolution at L<d remains visible.

#### [Tensor and Smolyak controls in two to four dimensions](https://hrkoyama.github.io/numerical-methods-atlas/validation/tensor-smolyak-dimensions/?lang=en#tensor-smolyak-dimensions-en-measurements)

Analytic reference · Reference for the same problem

\int_{[0,1]^d}\prod_{j=1}^de^{a_jx_j}\,d\mathbf x=\prod_{j=1}^d\frac{e^{a_j}-1}{a_j},\quad\int_{[0,1]^d}\prod_{j=1}^d(x_j-1/2)^2\,d\mathbf x=12^{-d};\quad A_L=\sum_{|\ell|_1\le L}\bigotimes_{j=1}^d(Q_{\ell_j}-Q_{\ell_j-1}),\quad Q_{-1}=0

The integration domain is[0,1]^d for d2/3/4; tensor levels1/2/3 and sparse levels1/2/3/4.

No general error monotonicity, positive-weight or cost-superiority claim; these are integration coordinates, not a physical PDE space.

#### Tensor and Smolyak controls in two to four dimensions

Analytic integrals are distinct from companion Delta/combination assembly; interaction underresolution at L<d remains visible.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/tensor-smolyak-dimensions/?lang=en)

### Numerical methods

Canonical dyadic angle keys own shared nodes; signed weights and call ledgers are retained.

- [Gaussian and adaptive quadrature](https://hrkoyama.github.io/numerical-methods-atlas/methods/quadrature/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Smolyak sparse-grid quadrature](https://hrkoyama.github.io/numerical-methods-atlas/methods/smolyak-sparse-grid/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Tensor and Smolyak controls in two to four dimensions](https://hrkoyama.github.io/numerical-methods-atlas/validation/tensor-smolyak-dimensions/?lang=en)

Supplementary execution example

Forty-two fixed cubatures compare a smooth product and an interaction product.

The integration domain is[0,1]^d for d2/3/4; tensor levels1/2/3 and sparse levels1/2/3/4.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/atlas-quadrature-controls-2026-11-25.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

No general error monotonicity, positive-weight or cost-superiority claim; these are integration coordinates, not a physical PDE space.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-25/quadrature-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/run.py)
- [/code/validated-examples/2026-11-25/quadrature-controls/cubature.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/cubature.py)
- [/code/validated-examples/2026-11-25/quadrature-controls/test_quadrature.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quadrature-controls/test_quadrature.py)
