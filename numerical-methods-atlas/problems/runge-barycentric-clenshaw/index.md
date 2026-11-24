# 節点・表現・丸めを分けるRunge補間 / Runge interpolation: nodes, representation and rounding

https://hrkoyama.github.io/numerical-methods-atlas/problems/runge-barycentric-clenshaw/

## 日本語

[Runge関数と絶対値関数を等間隔・Lobatto型の固定節点で補間し、Clenshaw評価と比較します。 保存配列から作図。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/runge-barycentric-clenshaw-preview.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-approximation-controls/#runge-barycentric-clenshaw) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#runge-barycentric-clenshaw)

### 方程式・問題の定義

無次元区間[-1,1]、次数8・16・32、固定2048中点。節点・データ・重みは実際のbinary64値を対象にします。

#### [格納節点の多項式補間](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#polynomial-interpolation-ja)

$$
P_n(x_j)=y_j,\quad P_n\in\mathcal P_n
$$

$$
R(x)=\frac{\sum_jw_jy_j/(x-x_j)}{\sum_jw_j/(x-x_j)}
$$

閉形式重みと丸め節点の表現差、補間誤差と演算丸めを分けます。

#### 節点・表現・丸めを分けるRunge補間

補助実行例 · 実行例の定義・検証式

$$
p(x)=sum_j y_j*prod_(k!=j)((x-x_k)/(x_j-x_k))
$$

$$
R(x)=(sum_j w_j*y_j/(x-x_j))/(sum_j w_j/(x-x_j))
$$

$$
C(x)=sum_(k=0)^n a_k*T_k(x); b_k=a_k+2*x*b_(k+1)-b_(k+2)
$$

Runge関数と絶対値関数を等間隔・Lobatto型の固定節点で補間し、Clenshaw評価と比較します。

### 厳密解・参照解

格納値の補間多項式P、閉重み有理式R、格納係数級数C、目標関数fを区別。17点の正確な有理参照・演算別誤差上界・節点一致・固定Runge傾向を照合します。

#### [節点・表現・丸めを分けるRunge補間](https://hrkoyama.github.io/numerical-methods-atlas/validation/runge-barycentric-clenshaw/?lang=ja#runge-barycentric-clenshaw-ja-measurements)

解析解 · 同じ問題の参照

P_{\rm stored}(x)=\sum_j y_j\prod_{k\ne j}\frac{x-x_k}{x_j-x_k},\quad R_{\rm closed}(x)=\frac{\sum_jw_jy_j/(x-x_j)}{\sum_jw_j/(x-x_j)},\quad C_{\rm stored}(x)=\sum_{k=0}^na_kT_k(x),\quad f(x)\in\{(1+25x^2)^{-1},|x|\}

無次元区間[-1,1]、次数8・16・32、固定2048中点。節点・データ・重みは実際のbinary64値を対象にします。

標本最大誤差は連続一様ノルムの証明ではありません。丸め節点の閉重み・離散直交性は厳密と見なしません。任意次数・任意点の安定性は保証しません。

#### 節点・表現・丸めを分けるRunge補間

格納値の補間多項式P、閉重み有理式R、格納係数級数C、目標関数fを区別。17点の正確な有理参照・演算別誤差上界・節点一致・固定Runge傾向を照合します。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/runge-barycentric-clenshaw/?lang=ja)

### 計算法

第2重心公式と全係数Clenshaw漸化式を自作。丸め済み節点上の閉形式重みと有限Chebyshev変換をそのまま保存します。

- [Chebyshev近似](https://hrkoyama.github.io/numerical-methods-atlas/methods/chebyshev/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [節点・表現・丸めを分けるRunge補間](https://hrkoyama.github.io/numerical-methods-atlas/validation/runge-barycentric-clenshaw/?lang=ja)

補助実行例

Runge関数と絶対値関数を等間隔・Lobatto型の固定節点で補間し、Clenshaw評価と比較します。

無次元区間[-1,1]、次数8・16・32、固定2048中点。節点・データ・重みは実際のbinary64値を対象にします。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/atlas-approximation-controls-2026-11-25.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

標本最大誤差は連続一様ノルムの証明ではありません。丸め節点の閉重み・離散直交性は厳密と見なしません。任意次数・任意点の安定性は保証しません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-25/approximation-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/run.py)
- [/code/validated-examples/2026-11-25/approximation-controls/interpolation.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/interpolation.py)
- [/code/validated-examples/2026-11-25/approximation-controls/test_approximation.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/test_approximation.py)

## English

[Interpolate the Runge and absolute-value functions on fixed equispaced and Lobatto-like nodes, and compare with Clenshaw evaluation. Drawn from saved arrays.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/runge-barycentric-clenshaw-preview.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-approximation-controls/#runge-barycentric-clenshaw) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#runge-barycentric-clenshaw-en)

### Equations and problem definitions

Dimensionless interval [-1,1], degrees 8, 16 and 32, and 2048 fixed midpoints. Actual binary64 nodes, data and weights define the discrete problem.

#### [Polynomial interpolation on stored nodes](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#polynomial-interpolation-en)

$$
P_n(x_j)=y_j,\quad P_n\in\mathcal P_n
$$

$$
R(x)=\frac{\sum_jw_jy_j/(x-x_j)}{\sum_jw_j/(x-x_j)}
$$

Separate closed-weight representation on rounded nodes, interpolation error and evaluation rounding.

#### Runge interpolation: nodes, representation and rounding

Supplementary execution example · Example definition or validation formula

$$
p(x)=sum_j y_j*prod_(k!=j)((x-x_k)/(x_j-x_k))
$$

$$
R(x)=(sum_j w_j*y_j/(x-x_j))/(sum_j w_j/(x-x_j))
$$

$$
C(x)=sum_(k=0)^n a_k*T_k(x); b_k=a_k+2*x*b_(k+1)-b_(k+2)
$$

Interpolate the Runge and absolute-value functions on fixed equispaced and Lobatto-like nodes, and compare with Clenshaw evaluation.

### Exact and reference solutions

Separate the stored-data polynomial P, closed-weight rational expression R, stored-coefficient series C and target f. Check exact rational references at 17 probes, operation-based error bounds, node identities and fixed Runge trends.

#### [Runge interpolation: nodes, representation and rounding](https://hrkoyama.github.io/numerical-methods-atlas/validation/runge-barycentric-clenshaw/?lang=en#runge-barycentric-clenshaw-en-measurements)

Analytic reference · Reference for the same problem

P_{\rm stored}(x)=\sum_j y_j\prod_{k\ne j}\frac{x-x_k}{x_j-x_k},\quad R_{\rm closed}(x)=\frac{\sum_jw_jy_j/(x-x_j)}{\sum_jw_j/(x-x_j)},\quad C_{\rm stored}(x)=\sum_{k=0}^na_kT_k(x),\quad f(x)\in\{(1+25x^2)^{-1},|x|\}

Dimensionless interval [-1,1], degrees 8, 16 and 32, and 2048 fixed midpoints. Actual binary64 nodes, data and weights define the discrete problem.

A sampled maximum error is not a proof of a continuous uniform norm. Closed weights and discrete orthogonality on rounded nodes are not treated as exact. No arbitrary-degree or all-point stability guarantee is made.

#### Runge interpolation: nodes, representation and rounding

Separate the stored-data polynomial P, closed-weight rational expression R, stored-coefficient series C and target f. Check exact rational references at 17 probes, operation-based error bounds, node identities and fixed Runge trends.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/runge-barycentric-clenshaw/?lang=en)

### Numerical methods

Implement the second barycentric formula and a full-coefficient Clenshaw recurrence. Retain the closed weights and finite Chebyshev transform on rounded nodes.

- [Chebyshev approximation](https://hrkoyama.github.io/numerical-methods-atlas/methods/chebyshev/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Runge interpolation: nodes, representation and rounding](https://hrkoyama.github.io/numerical-methods-atlas/validation/runge-barycentric-clenshaw/?lang=en)

Supplementary execution example

Interpolate the Runge and absolute-value functions on fixed equispaced and Lobatto-like nodes, and compare with Clenshaw evaluation.

Dimensionless interval [-1,1], degrees 8, 16 and 32, and 2048 fixed midpoints. Actual binary64 nodes, data and weights define the discrete problem.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/atlas-approximation-controls-2026-11-25.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

A sampled maximum error is not a proof of a continuous uniform norm. Closed weights and discrete orthogonality on rounded nodes are not treated as exact. No arbitrary-degree or all-point stability guarantee is made.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-25/approximation-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/run.py)
- [/code/validated-examples/2026-11-25/approximation-controls/interpolation.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/interpolation.py)
- [/code/validated-examples/2026-11-25/approximation-controls/test_approximation.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/test_approximation.py)
