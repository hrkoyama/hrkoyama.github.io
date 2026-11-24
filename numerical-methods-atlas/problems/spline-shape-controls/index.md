# 自然・端点微分指定スプラインとPCHIP / Natural and clamped splines versus PCHIP

https://hrkoyama.github.io/numerical-methods-atlas/problems/spline-shape-controls/

## 日本語

[平坦部を持つ単調データ・3次式・直線の固定3組で、C2連続性と形状保存を比較します。 保存配列から作図。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/spline-shape-controls-preview.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-approximation-controls/#spline-shape-controls) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#spline-shape-controls)

### 方程式・問題の定義

実binary64の節点と値を使用。自然条件は両端2階微分ゼロ、clamped条件は入力端点1階微分です。

#### [3次スプラインと形状保存補間](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#cubic-spline-pchip-ja)

$$
S_i(x)=a_i+b_i(x-x_i)+c_i(x-x_i)^2+d_i(x-x_i)^3
$$

$$
S\in C^2\ \text{for the natural/clamped spline};\quad P\in C^1\ \text{for PCHIP}
$$

端点条件を持つC2補間と単調な区分Hermite補間を区別します。

#### 自然・端点微分指定スプラインとPCHIP

補助実行例 · 実行例の定義・検証式

$$
S_i(s)=a_i+b_i*s+c_i*s^2+d_i*s^3
$$

$$
d_k=(w_1+w_2)/(w_1/m_(k-1)+w_2/m_k)
$$

$$
S_natural(1.5)=a-9*(b-a)/88; S_clamped(1.5)=a-15*(b-a)/152
$$

平坦部を持つ単調データ・3次式・直線の固定3組で、C2連続性と形状保存を比較します。

### 厳密解・参照解

正確な有理2階微分系・有理PCHIP・SciPy 1.14.1を照合。端点15記録は16スカラー出力・13異なる入力。平坦部の負値は実binary64をFraction化した独立式で示します。

#### [自然・端点微分指定スプラインとPCHIP](https://hrkoyama.github.io/numerical-methods-atlas/validation/spline-shape-controls/?lang=ja#spline-shape-controls-ja-measurements)

解析解 · 同じ問題の参照

S_i(s)=a_i+b_is+c_is^2+d_is^3,\quad d_k=\frac{w_1+w_2}{w_1/m_{k-1}+w_2/m_k};\quad S_{\rm nat}(3/2)=a-\frac9{88}(b-a),\quad S_{\rm clamp}(3/2)=a-\frac{15}{152}(b-a)

実binary64の節点と値を使用。自然条件は両端2階微分ゼロ、clamped条件は入力端点1階微分です。

PCHIPは通常C1でありC2とは限りません。一般データの最良近似・外挿・ノイズ平滑化は対象外。SciPyは原著完全閲読の代用ではありません。

#### 自然・端点微分指定スプラインとPCHIP

正確な有理2階微分系・有理PCHIP・SciPy 1.14.1を照合。端点15記録は16スカラー出力・13異なる入力。平坦部の負値は実binary64をFraction化した独立式で示します。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/spline-shape-controls/?lang=ja)

### 計算法

3次Bスプラインの配置行列を解きde Boor評価。別経路でPCHIPの調和平均・端点制限とHermite評価を実装します。

- [スプライン補間](https://hrkoyama.github.io/numerical-methods-atlas/methods/splines/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [PCHIP単調3次Hermite補間](https://hrkoyama.github.io/numerical-methods-atlas/methods/pchip/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [自然・端点微分指定スプラインとPCHIP](https://hrkoyama.github.io/numerical-methods-atlas/validation/spline-shape-controls/?lang=ja)

補助実行例

平坦部を持つ単調データ・3次式・直線の固定3組で、C2連続性と形状保存を比較します。

実binary64の節点と値を使用。自然条件は両端2階微分ゼロ、clamped条件は入力端点1階微分です。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/atlas-approximation-controls-2026-11-25.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

PCHIPは通常C1でありC2とは限りません。一般データの最良近似・外挿・ノイズ平滑化は対象外。SciPyは原著完全閲読の代用ではありません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-25/approximation-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/run.py)
- [/code/validated-examples/2026-11-25/approximation-controls/splines.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/splines.py)
- [/code/validated-examples/2026-11-25/approximation-controls/test_approximation.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/test_approximation.py)

## English

[Compare C2 continuity and shape preservation on three fixed data sets: a monotone plateau, a cubic and a straight line. Drawn from saved arrays.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/spline-shape-controls-preview.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-approximation-controls/#spline-shape-controls) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#spline-shape-controls-en)

### Equations and problem definitions

Use actual binary64 knots and values. Natural conditions set both endpoint second derivatives to zero; clamped conditions prescribe the first derivatives from the input.

#### [Cubic splines and shape-preserving interpolation](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#cubic-spline-pchip-en)

$$
S_i(x)=a_i+b_i(x-x_i)+c_i(x-x_i)^2+d_i(x-x_i)^3
$$

$$
S\in C^2\ \text{for the natural/clamped spline};\quad P\in C^1\ \text{for PCHIP}
$$

Distinguish C2 interpolation with endpoint conditions from monotone piecewise Hermite interpolation.

#### Natural and clamped splines versus PCHIP

Supplementary execution example · Example definition or validation formula

$$
S_i(s)=a_i+b_i*s+c_i*s^2+d_i*s^3
$$

$$
d_k=(w_1+w_2)/(w_1/m_(k-1)+w_2/m_k)
$$

$$
S_natural(1.5)=a-9*(b-a)/88; S_clamped(1.5)=a-15*(b-a)/152
$$

Compare C2 continuity and shape preservation on three fixed data sets: a monotone plateau, a cubic and a straight line.

### Exact and reference solutions

Compare with exact rational second-derivative systems, rational PCHIP and SciPy 1.14.1. Fifteen endpoint records contain sixteen scalar outputs from thirteen distinct inputs. Independent Fraction formulas show plateau undershoot for the actual binary64 data.

#### [Natural and clamped splines versus PCHIP](https://hrkoyama.github.io/numerical-methods-atlas/validation/spline-shape-controls/?lang=en#spline-shape-controls-en-measurements)

Analytic reference · Reference for the same problem

S_i(s)=a_i+b_is+c_is^2+d_is^3,\quad d_k=\frac{w_1+w_2}{w_1/m_{k-1}+w_2/m_k};\quad S_{\rm nat}(3/2)=a-\frac9{88}(b-a),\quad S_{\rm clamp}(3/2)=a-\frac{15}{152}(b-a)

Use actual binary64 knots and values. Natural conditions set both endpoint second derivatives to zero; clamped conditions prescribe the first derivatives from the input.

PCHIP is generally C1, not necessarily C2. Best approximation, extrapolation and noise smoothing are outside scope. A SciPy comparison does not substitute for reading the original papers.

#### Natural and clamped splines versus PCHIP

Compare with exact rational second-derivative systems, rational PCHIP and SciPy 1.14.1. Fifteen endpoint records contain sixteen scalar outputs from thirteen distinct inputs. Independent Fraction formulas show plateau undershoot for the actual binary64 data.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/spline-shape-controls/?lang=en)

### Numerical methods

Solve a cubic B-spline collocation system and evaluate it with de Boor recursion. A separate path implements PCHIP harmonic slopes, endpoint limiting and Hermite evaluation.

- [Spline interpolation](https://hrkoyama.github.io/numerical-methods-atlas/methods/splines/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [PCHIP monotone cubic Hermite interpolation](https://hrkoyama.github.io/numerical-methods-atlas/methods/pchip/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Natural and clamped splines versus PCHIP](https://hrkoyama.github.io/numerical-methods-atlas/validation/spline-shape-controls/?lang=en)

Supplementary execution example

Compare C2 continuity and shape preservation on three fixed data sets: a monotone plateau, a cubic and a straight line.

Use actual binary64 knots and values. Natural conditions set both endpoint second derivatives to zero; clamped conditions prescribe the first derivatives from the input.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/atlas-approximation-controls-2026-11-25.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

PCHIP is generally C1, not necessarily C2. Best approximation, extrapolation and noise smoothing are outside scope. A SciPy comparison does not substitute for reading the original papers.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-25/approximation-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/run.py)
- [/code/validated-examples/2026-11-25/approximation-controls/splines.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/splines.py)
- [/code/validated-examples/2026-11-25/approximation-controls/test_approximation.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/test_approximation.py)
