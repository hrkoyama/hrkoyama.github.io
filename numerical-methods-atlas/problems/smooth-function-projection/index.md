# 滑らかな関数の多項式補間・射影 / Polynomial interpolation and projection of a smooth function

https://hrkoyama.github.io/numerical-methods-atlas/problems/smooth-function-projection/

## 日本語

[保存済み8次多項式の射影・補間と元の関数。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/smooth-function-projection.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/basis-functions/) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#smooth-function-projection)

### 方程式・問題の定義

指定関数の多項式射影・補間であり、支配方程式の求解ではありません。

#### 滑らかな関数：Legendre射影とGLL補間

共通実行例 · 近似・離散化の式

$$
\Pi_p f(x)=\sum_{k=0}^{p}c_kP_k(x),\qquad c_k=\frac{2k+1}{2}\int_{-1}^{1}e^\xi P_k(\xi)\,d\xi
$$

$$
I_pf(x)=\sum_{j=0}^{p}e^{x_j}\ell_j(x),\qquad\ell_j(x_i)=\delta_{ij},\qquad p=2,4,6,8
$$

重み1の区間射影とGLL節点補間で、PDEではない。32点求積による射影を、別のLegendre再帰式と64/96点求積で調べる。実行例の式は46モデルの件数に足さない。

### 厳密解・参照解

指定された滑らかな対象関数の既知値を基準に、Legendre射影・節点補間の誤差を比較します。方程式を解いたデータではありません。

#### 滑らかな関数：Legendre射影とGLL補間

CSVは次数ごとに201点、各行で射影値・GLL補間値・exp(x)を整列。次数別L2誤差、係数差、直交性残差、64/96点求積の差はJSONに記録する。

- [CSVは次数ごとに201点、各行で射影値・GLL補間値・exp(x)を整列。次数別L2誤差、係数差、直交性残差、64/96点求積の差はJSONに記録する。](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/smooth-function-projection/result.json)
- [exp(x)を直接評価し、異なる高次求積と独立の三項再帰でモード係数を求め直す。射影自身の求積値の再利用による自明な一致ではない。](https://hrkoyama.github.io/numerical-methods-atlas/en/read/basis-functions/)
- [保存結果](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/smooth-function-projection/result.json)
- [保存結果](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/smooth-function-projection/solution.csv)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/smooth-function-projection/?lang=ja)

### 計算法

この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。

- [Legendreモード基底・正規直交化](https://hrkoyama.github.io/numerical-methods-atlas/methods/legendre-basis/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [Lagrange節点基底・GLL選点法](https://hrkoyama.github.io/numerical-methods-atlas/methods/nodal-basis/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [滑らかな関数：Legendre射影とGLL補間](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/smooth-function-projection/?lang=ja)

共通実行例

exp(x)を次数2/4/6/8でL2射影し、同じ次数のGLL節点補間と比較する。実装の32点Gaussとは別の64/96点求積と独立Legendre再帰式で係数・直交性・誤差を確認する。

参照区間[−1,1]、重み1のLegendre内積。GLLはp+1節点。高次求積の一致を参照精度の補助検査とし、一般関数の厳密積分とは主張しない。出力201点は誤差積分用の求積点とは別。

[コード / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip) · [検証記録](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

[固定入力](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/recipes/smooth-function-projection.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python run_recipe.py --input recipes/smooth-function-projection.json --output output-smooth-function-projection
python -m pytest -q tests/test_recipes.py
```

exp(x)・GLL・次数増加・参照求積を固定し、非有限値や不適切な次数・参照求積数を拒否。不連続関数、高次数での安定性、曲線要素やPDE全体の検証ではない。解説本文は現在英語版。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/numerical-methods-atlas/2026-11-22/run_recipe.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/run_recipe.py)
- [/code/numerical-methods-atlas/2026-11-22/tests/test_recipes.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/tests/test_recipes.py)

## English

[Stored degree-8 projection/interpolation and the original function.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/smooth-function-projection.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/basis-functions/) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#smooth-function-projection-en)

### Equations and problem definitions

Polynomial projection/interpolation of a prescribed function, rather than a governing-equation solve.

#### Smooth function: Legendre projection and GLL interpolation

Common execution example · Approximation or discretization

$$
\Pi_p f(x)=\sum_{k=0}^{p}c_kP_k(x),\qquad c_k=\frac{2k+1}{2}\int_{-1}^{1}e^\xi P_k(\xi)\,d\xi
$$

$$
I_pf(x)=\sum_{j=0}^{p}e^{x_j}\ell_j(x),\qquad\ell_j(x_i)=\delta_{ij},\qquad p=2,4,6,8
$$

Unit-weight interval projection and GLL interpolation, not a PDE. The 32-point projection is checked by a separate Legendre recurrence and 64/96-point rules; example formulas do not add to the 46 model entries.

### Exact and reference solutions

Compare Legendre-projection and nodal-interpolation errors against known values of the specified smooth function. These data do not solve a governing equation.

#### Smooth function: Legendre projection and GLL interpolation

CSV provides 201 aligned projection/interpolation/exp(x) rows per degree. JSON records degree-wise L2 errors, coefficient differences, orthogonality and 64/96-point quadrature agreement.

- [CSV provides 201 aligned projection/interpolation/exp(x) rows per degree. JSON records degree-wise L2 errors, coefficient differences, orthogonality and 64/96-point quadrature agreement.](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/smooth-function-projection/result.json)
- [Direct exp(x) evaluation plus different high-order quadrature and a separate three-term recurrence recompute modal coefficients; the reference does not reuse the projection's own quadrature.](https://hrkoyama.github.io/numerical-methods-atlas/en/read/basis-functions/)
- [Saved result](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/smooth-function-projection/result.json)
- [Saved result](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/smooth-function-projection/solution.csv)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/smooth-function-projection/?lang=en)

### Numerical methods

Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions.

- [Legendre modal basis / orthonormal scaling](https://hrkoyama.github.io/numerical-methods-atlas/methods/legendre-basis/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Lagrange nodal basis / GLL collocation](https://hrkoyama.github.io/numerical-methods-atlas/methods/nodal-basis/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Smooth function: Legendre projection and GLL interpolation](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/smooth-function-projection/?lang=en)

Common execution example

L2-project exp(x) at degrees 2/4/6/8 and compare GLL interpolation at the same degrees. Check coefficients, orthogonality and errors using separate 64/96-point rules and an independent Legendre recurrence, versus 32-point projection quadrature.

Reference interval [−1,1] and unit-weight Legendre inner product; GLL has p+1 nodes. Agreement of higher-order rules supports reference accuracy but is not an exact-integration claim for arbitrary functions. The 201 output points are separate from error quadrature.

[Code / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip) · [Verification receipt](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

[Fixed input](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/recipes/smooth-function-projection.json)

[File manifest and hashes](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python run_recipe.py --input recipes/smooth-function-projection.json --output output-smooth-function-projection
python -m pytest -q tests/test_recipes.py
```

Fix exp(x), GLL, degree refinement and reference quadrature; reject nonfinite/invalid degrees or inadequate reference rules. Not validation for discontinuities, high-degree stability, curved elements or a full PDE. The current reading is English only.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/numerical-methods-atlas/2026-11-22/run_recipe.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/run_recipe.py)
- [/code/numerical-methods-atlas/2026-11-22/tests/test_recipes.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/tests/test_recipes.py)
