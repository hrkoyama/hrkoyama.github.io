# index-1 DAEの整合初期化と離散残差 / Consistent initialization and discrete residuals for an index-one DAE

https://hrkoyama.github.io/numerical-methods-atlas/problems/index1-dae-consistent-initialization/

## 日本語

[既知の正枝を持つindex-1 DAEで初期化と後退Eulerの誤差・残差を分離します。 保存配列から作図。 図の軌道・状態・時刻・反復の軸は、物理空間の次元を表しません。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/index1-dae-consistent-initialization-preview.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-dae-controls/#index1-dae-consistent-initialization) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#index1-dae-consistent-initialization)

### 方程式・問題の定義

無次元・正枝。微分行と代数行の尺度はそれぞれ1で、最大ノルムを用います。

#### [半陽的index-1 DAE](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#index-one-dae-ja)

$$
\dot y=f(t,y,z),\qquad0=g(t,y,z),\qquad\det g_z\ne0
$$

整合初期化と微分・代数残差を扱う小規模な固定例です。一般DAEソルバーの完成を意味しません。

#### index-1 DAEの整合初期化と離散残差

補助実行例 · 実行例の定義・検証式

$$
F1=ydot+y-z+exp(-2t/3), F2=z^3-y^2
$$

$$
y=exp(-t), z=exp(-2t/3)
$$

既知の正枝を持つindex-1 DAEで初期化と後退Eulerの誤差・残差を分離します。

### 厳密解・参照解

独立Decimal製造解・3つの離散根と3固定格子を比較し、一次誤差と代数拘束を確認します。

#### [index-1 DAEの整合初期化と離散残差](https://hrkoyama.github.io/numerical-methods-atlas/validation/index1-dae-consistent-initialization/?lang=ja#index1-dae-consistent-initialization-ja-measurements)

製造解 · 同じ問題の参照

F1=ydot+y-z+exp(-2t/3), F2=z^3-y^2;\quad y=exp(-t), z=exp(-2t/3)

無次元・正枝。微分行と代数行の尺度はそれぞれ1で、最大ノルムを用います。

単一の製造正枝・固定BE計算です。IDA実行や一般DAEソルバーの検証ではありません。

#### index-1 DAEの整合初期化と離散残差

独立Decimal製造解・3つの離散根と3固定格子を比較し、一次誤差と代数拘束を確認します。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/index1-dae-consistent-initialization/?lang=ja)

### 計算法

連立Newtonと同じ尺度のArmijo線探索を用い、特異な初期推測は修復せず記録します。

- [微分代数方程式（DAE）](https://hrkoyama.github.io/numerical-methods-atlas/methods/dae/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [後退Euler法](https://hrkoyama.github.io/numerical-methods-atlas/methods/backward-euler/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [Armijo減衰Newton法](https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [index-1 DAEの整合初期化と離散残差](https://hrkoyama.github.io/numerical-methods-atlas/validation/index1-dae-consistent-initialization/?lang=ja)

補助実行例

既知の正枝を持つindex-1 DAEで初期化と後退Eulerの誤差・残差を分離します。

無次元・正枝。微分行と代数行の尺度はそれぞれ1で、最大ノルムを用います。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/atlas-dae-controls-2026-11-24.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

単一の製造正枝・固定BE計算です。IDA実行や一般DAEソルバーの検証ではありません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-24/dae-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/run.py)
- [/code/validated-examples/2026-11-24/dae-controls/models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/models.py)
- [/code/validated-examples/2026-11-24/dae-controls/newton.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/newton.py)
- [/code/validated-examples/2026-11-24/dae-controls/test_cases.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/test_cases.py)
- [/code/validated-examples/2026-11-24/dae-controls/test_serialization.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/test_serialization.py)

## English

[Separate initialization, backward-Euler error and residuals on a known positive index-one DAE branch. Drawn from saved arrays. Axes for trajectories, states, time or iterations do not represent physical spatial dimensions.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/index1-dae-consistent-initialization-preview.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-dae-controls/#index1-dae-consistent-initialization) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#index1-dae-consistent-initialization-en)

### Equations and problem definitions

Dimensionless positive branch; differential and algebraic row scales are both one, with the maximum norm.

#### [Semi-explicit index-one DAE](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#index-one-dae-en)

$$
\dot y=f(t,y,z),\qquad0=g(t,y,z),\qquad\det g_z\ne0
$$

Small fixed examples expose consistent initialization and separate differential/algebraic residuals; this is not a general-purpose DAE solver.

#### Consistent initialization and discrete residuals for an index-one DAE

Supplementary execution example · Example definition or validation formula

$$
F1=ydot+y-z+exp(-2t/3), F2=z^3-y^2
$$

$$
y=exp(-t), z=exp(-2t/3)
$$

Separate initialization, backward-Euler error and residuals on a known positive index-one DAE branch.

### Exact and reference solutions

Compare independent Decimal manufactured states, three discrete roots and three fixed grids, checking first-order error and the algebraic constraint.

#### [Consistent initialization and discrete residuals for an index-one DAE](https://hrkoyama.github.io/numerical-methods-atlas/validation/index1-dae-consistent-initialization/?lang=en#index1-dae-consistent-initialization-en-measurements)

Manufactured solution · Reference for the same problem

F1=ydot+y-z+exp(-2t/3), F2=z^3-y^2;\quad y=exp(-t), z=exp(-2t/3)

Dimensionless positive branch; differential and algebraic row scales are both one, with the maximum norm.

One authored positive branch and fixed BE runs; no IDA execution or general DAE-solver qualification.

#### Consistent initialization and discrete residuals for an index-one DAE

Compare independent Decimal manufactured states, three discrete roots and three fixed grids, checking first-order error and the algebraic constraint.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/index1-dae-consistent-initialization/?lang=en)

### Numerical methods

Use coupled Newton with an Armijo search in the same scaled norm, retaining rather than repairing a singular initial guess.

- [Differential-algebraic equations / DAE](https://hrkoyama.github.io/numerical-methods-atlas/methods/dae/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Backward Euler](https://hrkoyama.github.io/numerical-methods-atlas/methods/backward-euler/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Armijo-damped Newton](https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Consistent initialization and discrete residuals for an index-one DAE](https://hrkoyama.github.io/numerical-methods-atlas/validation/index1-dae-consistent-initialization/?lang=en)

Supplementary execution example

Separate initialization, backward-Euler error and residuals on a known positive index-one DAE branch.

Dimensionless positive branch; differential and algebraic row scales are both one, with the maximum norm.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/atlas-dae-controls-2026-11-24.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

One authored positive branch and fixed BE runs; no IDA execution or general DAE-solver qualification.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-24/dae-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/run.py)
- [/code/validated-examples/2026-11-24/dae-controls/models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/models.py)
- [/code/validated-examples/2026-11-24/dae-controls/newton.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/newton.py)
- [/code/validated-examples/2026-11-24/dae-controls/test_cases.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/test_cases.py)
- [/code/validated-examples/2026-11-24/dae-controls/test_serialization.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/test_serialization.py)
