# 補間・スプライン・Haarの固定対照

節点・表現・丸め、C2連続性と形状保存、境界拡張とシフトをそれぞれ分けた小さな固定例です。

共通22実行例の台帳とは別に管理する追加検証集です。配布ZIPを独立展開し、各グループの全固定入力と検査を実行した記録を示します。設定・手法・刻み幅の違いを独立した物理問題の数には加算しません。

## 節点・表現・丸めを分けるRunge補間

Runge関数と絶対値関数を等間隔・Lobatto型の固定節点で補間し、Clenshaw評価と比較します。

**使用手法**

- [Chebyshev近似](https://hrkoyama.github.io/numerical-methods-atlas/methods/chebyshev/?lang=ja) (`chebyshev`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/runge-barycentric-clenshaw/?lang=ja#runge-barycentric-clenshaw-ja-algorithm)

第2重心公式と全係数Clenshaw漸化式を自作。丸め済み節点上の閉形式重みと有限Chebyshev変換をそのまま保存します。

$$
p(x)=sum_j y_j*prod_(k!=j)((x-x_k)/(x_j-x_k))
$$

$$
R(x)=(sum_j w_j*y_j/(x-x_j))/(sum_j w_j/(x-x_j))
$$

$$
C(x)=sum_(k=0)^n a_k*T_k(x); b_k=a_k+2*x*b_(k+1)-b_(k+2)
$$

- [格納節点の多項式補間](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#polynomial-interpolation-ja) (`polynomial-interpolation`)

無次元区間[-1,1]、次数8・16・32、固定2048中点。節点・データ・重みは実際のbinary64値を対象にします。


**問題の図**

![節点・表現・丸めを分けるRunge補間：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/runge-barycentric-clenshaw.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[節点・表現・丸めを分けるRunge補間](https://hrkoyama.github.io/numerical-methods-atlas/problems/runge-barycentric-clenshaw/?lang=ja) (`runge-barycentric-clenshaw`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/runge-barycentric-clenshaw/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/runge-barycentric-clenshaw/?lang=ja#runge-barycentric-clenshaw-ja-validation)

格納値の補間多項式P、閉重み有理式R、格納係数級数C、目標関数fを区別。17点の正確な有理参照・演算別誤差上界・節点一致・固定Runge傾向を照合します。

- [節点・表現・丸めを分けるRunge補間](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-runge-barycentric-clenshaw-ja) (`runge-barycentric-clenshaw`; 同じ問題の参照 · 解析参照)

標本最大誤差は連続一様ノルムの証明ではありません。丸め節点の閉重み・離散直交性は厳密と見なしません。任意次数・任意点の安定性は保証しません。
### 前提・単位・境界

無次元区間[-1,1]、次数8・16・32、固定2048中点。節点・データ・重みは実際のbinary64値を対象にします。

**編集上の補足**

標本最大誤差は連続一様ノルムの証明ではありません。丸め節点の閉重み・離散直交性は厳密と見なしません。任意次数・任意点の安定性は保証しません。

### 採用した計算法

第2重心公式と全係数Clenshaw漸化式を自作。丸め済み節点上の閉形式重みと有限Chebyshev変換をそのまま保存します。

$$
p(x)=sum_j y_j*prod_(k!=j)((x-x_k)/(x_j-x_k))
$$

$$
R(x)=(sum_j w_j*y_j/(x-x_j))/(sum_j w_j/(x-x_j))
$$

$$
C(x)=sum_(k=0)^n a_k*T_k(x); b_k=a_k+2*x*b_(k+1)-b_(k+2)
$$

### 比較・検証

格納値の補間多項式P、閉重み有理式R、格納係数級数C、目標関数fを区別。17点の正確な有理参照・演算別誤差上界・節点一致・固定Runge傾向を照合します。

### 確認の限界

標本最大誤差は連続一様ノルムの証明ではありません。丸め節点の閉重み・離散直交性は厳密と見なしません。任意次数・任意点の安定性は保証しません。

### 保存実測値と判定

```json
{
  "metrics": {
    "max_node_table_cosine_defect": 1.6816803605601774e-16,
    "maximum_sampled_function_error": 105718.65676159713,
    "reference_certificate_probes_per_interpolant": 17,
    "coefficient_sets": 6
  },
  "checks": {
    "reference:fixed-cosine-node-table": true,
    "runge-equispaced-8:finite": true,
    "runge-equispaced-8:node-hit-identity": true,
    "runge-equispaced-8:barycentric-operation-certificate": true,
    "runge-lobatto-8:clenshaw-operation-certificate": true,
    "runge-lobatto-8:finite": true,
    "runge-lobatto-8:node-hit-identity": true,
    "runge-lobatto-8:barycentric-operation-certificate": true,
    "runge-equispaced-16:finite": true,
    "runge-equispaced-16:node-hit-identity": true,
    "runge-equispaced-16:barycentric-operation-certificate": true,
    "runge-lobatto-16:clenshaw-operation-certificate": true,
    "runge-lobatto-16:finite": true,
    "runge-lobatto-16:node-hit-identity": true,
    "runge-lobatto-16:barycentric-operation-certificate": true,
    "runge-equispaced-32:finite": true,
    "runge-equispaced-32:node-hit-identity": true,
    "runge-equispaced-32:barycentric-operation-certificate": true,
    "runge-lobatto-32:clenshaw-operation-certificate": true,
    "runge-lobatto-32:finite": true,
    "runge-lobatto-32:node-hit-identity": true,
    "runge-lobatto-32:barycentric-operation-certificate": true,
    "absolute-equispaced-8:finite": true,
    "absolute-equispaced-8:node-hit-identity": true,
    "absolute-equispaced-8:barycentric-operation-certificate": true,
    "absolute-lobatto-8:clenshaw-operation-certificate": true,
    "absolute-lobatto-8:finite": true,
    "absolute-lobatto-8:node-hit-identity": true,
    "absolute-lobatto-8:barycentric-operation-certificate": true,
    "absolute-equispaced-16:finite": true,
    "absolute-equispaced-16:node-hit-identity": true,
    "absolute-equispaced-16:barycentric-operation-certificate": true,
    "absolute-lobatto-16:clenshaw-operation-certificate": true,
    "absolute-lobatto-16:finite": true,
    "absolute-lobatto-16:node-hit-identity": true,
    "absolute-lobatto-16:barycentric-operation-certificate": true,
    "absolute-equispaced-32:finite": true,
    "absolute-equispaced-32:node-hit-identity": true,
    "absolute-equispaced-32:barycentric-operation-certificate": true,
    "absolute-lobatto-32:clenshaw-operation-certificate": true,
    "absolute-lobatto-32:finite": true,
    "absolute-lobatto-32:node-hit-identity": true,
    "absolute-lobatto-32:barycentric-operation-certificate": true,
    "reference:polynomial-control-equispaced": true,
    "reference:polynomial-control-lobatto": true,
    "runge:equispaced-growth": true,
    "runge:lobatto-refinement": true,
    "fixed-record-and-coefficient-count": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/runge-barycentric-clenshaw/index.json

![Runge関数と絶対値関数を等間隔・Lobatto型の固定節点で補間し、Clenshaw評価と比較します。 保存配列から作図。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/runge-barycentric-clenshaw-preview.png)

Runge関数と絶対値関数を等間隔・Lobatto型の固定節点で補間し、Clenshaw評価と比較します。 保存配列から作図。

![保存済み誤差・導関数または二乗ノルムを別表示。各境界・表現の適用範囲は本文を参照。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/runge-barycentric-clenshaw-diagnostics.png)

保存済み誤差・導関数または二乗ノルムを別表示。各境界・表現の適用範囲は本文を参照。

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/atlas-approximation-controls-2026-11-25.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

### 出典と確認範囲

- NIST DLMF §3.11(ii): Chebyshev series and Clenshaw summation [accessed 2026-11-25]. https://dlmf.nist.gov/3.11; review_level=official-reference-selected-equations
Selected E7, E9, E11 and E15 with endpoint-halving conventions; no original Clenshaw paper reading. The implementation uses full coefficients, so its final combination is derived explicitly.

- SciPy 1.14.1 BarycentricInterpolator documentation [accessed 2026-11-24]. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.interpolate.BarycentricInterpolator.html; review_level=official-documentation-selected-notes
Selected barycentric formula and interpolation-conditioning notes read during the preceding preparation. The Berrut–Trefethen paper is a bibliographic lead, not a full-text reading.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## 自然・端点微分指定スプラインとPCHIP

平坦部を持つ単調データ・3次式・直線の固定3組で、C2連続性と形状保存を比較します。

**使用手法**

- [スプライン補間](https://hrkoyama.github.io/numerical-methods-atlas/methods/splines/?lang=ja) (`splines`)
- [PCHIP単調3次Hermite補間](https://hrkoyama.github.io/numerical-methods-atlas/methods/pchip/?lang=ja) (`pchip`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/spline-shape-controls/?lang=ja#spline-shape-controls-ja-algorithm)

3次Bスプラインの配置行列を解きde Boor評価。別経路でPCHIPの調和平均・端点制限とHermite評価を実装します。

$$
S_i(s)=a_i+b_i*s+c_i*s^2+d_i*s^3
$$

$$
d_k=(w_1+w_2)/(w_1/m_(k-1)+w_2/m_k)
$$

$$
S_natural(1.5)=a-9*(b-a)/88; S_clamped(1.5)=a-15*(b-a)/152
$$

- [3次スプラインと形状保存補間](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#cubic-spline-pchip-ja) (`cubic-spline-pchip`)

実binary64の節点と値を使用。自然条件は両端2階微分ゼロ、clamped条件は入力端点1階微分です。


**問題の図**

![自然・端点微分指定スプラインとPCHIP：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/spline-shape-controls.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[自然・端点微分指定スプラインとPCHIP](https://hrkoyama.github.io/numerical-methods-atlas/problems/spline-shape-controls/?lang=ja) (`spline-shape-controls`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/spline-shape-controls/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/spline-shape-controls/?lang=ja#spline-shape-controls-ja-validation)

正確な有理2階微分系・有理PCHIP・SciPy 1.14.1を照合。端点15記録は16スカラー出力・13異なる入力。平坦部の負値は実binary64をFraction化した独立式で示します。

- [自然・端点微分指定スプラインとPCHIP](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-spline-shape-controls-ja) (`spline-shape-controls`; 同じ問題の参照 · 解析参照)

PCHIPは通常C1でありC2とは限りません。一般データの最良近似・外挿・ノイズ平滑化は対象外。SciPyは原著完全閲読の代用ではありません。
### 前提・単位・境界

実binary64の節点と値を使用。自然条件は両端2階微分ゼロ、clamped条件は入力端点1階微分です。

**編集上の補足**

PCHIPは通常C1でありC2とは限りません。一般データの最良近似・外挿・ノイズ平滑化は対象外。SciPyは原著完全閲読の代用ではありません。

### 採用した計算法

3次Bスプラインの配置行列を解きde Boor評価。別経路でPCHIPの調和平均・端点制限とHermite評価を実装します。

$$
S_i(s)=a_i+b_i*s+c_i*s^2+d_i*s^3
$$

$$
d_k=(w_1+w_2)/(w_1/m_(k-1)+w_2/m_k)
$$

$$
S_natural(1.5)=a-9*(b-a)/88; S_clamped(1.5)=a-15*(b-a)/152
$$

### 比較・検証

正確な有理2階微分系・有理PCHIP・SciPy 1.14.1を照合。端点15記録は16スカラー出力・13異なる入力。平坦部の負値は実binary64をFraction化した独立式で示します。

### 確認の限界

PCHIPは通常C1でありC2とは限りません。一般データの最良近似・外挿・ノイズ平滑化は対象外。SciPyは原著完全閲読の代用ではありません。

### 保存実測値と判定

```json
{
  "metrics": {
    "maximum_value_scaled_reference_defect": 2.9409263239818476e-16,
    "maximum_derivative_scaled_reference_defect": 5.2306043094691055e-15,
    "endpoint_fixture_records": 15,
    "endpoint_scalar_outputs": 16,
    "endpoint_distinct_datasets": 13
  },
  "checks": {
    "reference:endpoint-branch-values": true,
    "reference:endpoint-record-count": true,
    "reference:endpoint-output-count": true,
    "reference:endpoint-distinct-datasets": true,
    "reference:negative-natural-witness": true,
    "reference:negative-clamped-witness": true,
    "plateau-natural:finite": true,
    "plateau-natural:value-reference": true,
    "plateau-natural:derivative-reference": true,
    "plateau-natural:nodal": true,
    "plateau-natural:boundary-or-shape": true,
    "plateau-clamped:finite": true,
    "plateau-clamped:value-reference": true,
    "plateau-clamped:derivative-reference": true,
    "plateau-clamped:nodal": true,
    "plateau-clamped:boundary-or-shape": true,
    "reference:pchip-actual-input-plateau": true,
    "plateau-pchip:finite": true,
    "plateau-pchip:value-reference": true,
    "plateau-pchip:derivative-reference": true,
    "plateau-pchip:nodal": true,
    "plateau-pchip:boundary-or-shape": true,
    "cubic-natural:finite": true,
    "cubic-natural:value-reference": true,
    "cubic-natural:derivative-reference": true,
    "cubic-natural:nodal": true,
    "cubic-natural:boundary-or-shape": true,
    "cubic-clamped:finite": true,
    "cubic-clamped:value-reference": true,
    "cubic-clamped:derivative-reference": true,
    "cubic-clamped:nodal": true,
    "cubic-clamped:boundary-or-shape": true,
    "cubic-pchip:finite": true,
    "cubic-pchip:value-reference": true,
    "cubic-pchip:derivative-reference": true,
    "cubic-pchip:nodal": true,
    "cubic-pchip:boundary-or-shape": true,
    "linear-natural:finite": true,
    "linear-natural:value-reference": true,
    "linear-natural:derivative-reference": true,
    "linear-natural:nodal": true,
    "linear-natural:boundary-or-shape": true,
    "linear-clamped:finite": true,
    "linear-clamped:value-reference": true,
    "linear-clamped:derivative-reference": true,
    "linear-clamped:nodal": true,
    "linear-clamped:boundary-or-shape": true,
    "linear-pchip:finite": true,
    "linear-pchip:value-reference": true,
    "linear-pchip:derivative-reference": true,
    "linear-pchip:nodal": true,
    "linear-pchip:boundary-or-shape": true,
    "reference:exact-piece-continuity": true,
    "reference:polynomial-cubic-clamped": true,
    "reference:polynomial-linear-natural": true,
    "reference:polynomial-linear-clamped": true,
    "fixed-fit-count": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/spline-shape-controls/index.json

![平坦部を持つ単調データ・3次式・直線の固定3組で、C2連続性と形状保存を比較します。 保存配列から作図。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/spline-shape-controls-preview.png)

平坦部を持つ単調データ・3次式・直線の固定3組で、C2連続性と形状保存を比較します。 保存配列から作図。

![保存済み誤差・導関数または二乗ノルムを別表示。各境界・表現の適用範囲は本文を参照。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/spline-shape-controls-diagnostics.png)

保存済み誤差・導関数または二乗ノルムを別表示。各境界・表現の適用範囲は本文を参照。

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/atlas-approximation-controls-2026-11-25.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

### 出典と確認範囲

- SciPy 1.14.1 PCHIP documentation and selected source [accessed 2026-11-25]. https://raw.githubusercontent.com/scipy/scipy/v1.14.1/scipy/interpolate/_cubic.py; review_level=official-source-selected-lines
Selected lines 202–225, 243–254, 275–298: harmonic interior derivatives, endpoint sign and 3-slope limiter, two-point case. The original Fritsch–Butland paper has not been read in full. Own formulas are independently expressed as scalar Hermite polynomials.

- SciPy 1.14.1 BSpline and CubicSpline documentation [accessed 2026-11-24]. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.interpolate.CubicSpline.html; review_level=official-documentation-selected-definitions
Natural and clamped boundary conditions and the BSpline recurrence were read during preparation. No de Boor original full-text claim. SciPy is a secondary numerical companion; the rational second-derivative system is the independent reference.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## Haar多重解像度の境界・シフト・閾値

長さ17・32の小信号に3段Haar分解を適用。1標本シフトと奇数長の境界処理を分けて比較します。

**使用手法**

- [ウェーブレット](https://hrkoyama.github.io/numerical-methods-atlas/methods/wavelets/?lang=ja) (`wavelets`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/haar-mallat-boundary-threshold/?lang=ja#haar-mallat-boundary-threshold-ja-algorithm)

和差フィルタ・間引き・逆ピラミッドを自作。閾値なし・hard・softの3条件を同じ解析係数から再構成します。

$$
a_(l+1,k)=(a_(l,2k)+a_(l,2k+1))/sqrt(2)
$$

$$
d_(l+1,k)=(a_(l,2k)-a_(l,2k+1))/sqrt(2)
$$

$$
E_after=E_before+padding^2; ||e||_2^2=||delta_coeff||_2^2 only for square orthogonal transform
$$

- [有限長信号の離散Haar変換](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#discrete-haar-transform-ja) (`discrete-haar-transform`)

奇数長の各段で周期型は先頭、対称型は末尾を1点追加し、再構成時に切り戻します。詳細係数のみ閾値0.2を使用。


**問題の図**

![Haar多重解像度の境界・シフト・閾値：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/haar-mallat-boundary-threshold.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Haar多重解像度の境界・シフト・閾値](https://hrkoyama.github.io/numerical-methods-atlas/problems/haar-mallat-boundary-threshold/?lang=ja) (`haar-mallat-boundary-threshold`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/haar-mallat-boundary-threshold/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/haar-mallat-boundary-threshold/?lang=ja#haar-mallat-boundary-threshold-ja-validation)

12解析・36再構成。独立行列・Fraction/Decimal係数、完全再構成、二乗L2誤差を照合。長さ32のみ直交誤差恒等式を要求し、17点では追加エネルギーを段別保存します。

- [Haar多重解像度の境界・シフト・閾値](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-haar-mallat-boundary-threshold-ja) (`haar-mallat-boundary-threshold`; 同じ問題の参照 · 解析参照)

Haarに限定し長いフィルタや画像圧縮は対象外。一般の対称拡張に正規直交性を仮定しません。シフト不変性は要求せず、シフト別差を保存します。
### 前提・単位・境界

奇数長の各段で周期型は先頭、対称型は末尾を1点追加し、再構成時に切り戻します。詳細係数のみ閾値0.2を使用。

**編集上の補足**

Haarに限定し長いフィルタや画像圧縮は対象外。一般の対称拡張に正規直交性を仮定しません。シフト不変性は要求せず、シフト別差を保存します。 標本添字は物理空間の座標ではありません。境界処理を含む有限長信号の写像です。

### 採用した計算法

和差フィルタ・間引き・逆ピラミッドを自作。閾値なし・hard・softの3条件を同じ解析係数から再構成します。

$$
a_(l+1,k)=(a_(l,2k)+a_(l,2k+1))/sqrt(2)
$$

$$
d_(l+1,k)=(a_(l,2k)-a_(l,2k+1))/sqrt(2)
$$

$$
E_after=E_before+padding^2; ||e||_2^2=||delta_coeff||_2^2 only for square orthogonal transform
$$

### 比較・検証

12解析・36再構成。独立行列・Fraction/Decimal係数、完全再構成、二乗L2誤差を照合。長さ32のみ直交誤差恒等式を要求し、17点では追加エネルギーを段別保存します。

### 確認の限界

Haarに限定し長いフィルタや画像圧縮は対象外。一般の対称拡張に正規直交性を仮定しません。シフト不変性は要求せず、シフト別差を保存します。

### 保存実測値と判定

```json
{
  "metrics": {
    "analysis_records": 12,
    "maximum_reconstruction_l2_squared": 0.6095394266271633,
    "maximum_shift_back_equivariance_l2_squared": 0.23999999999999966
  },
  "checks": {
    "reference:golden-0": true,
    "reference:golden-1": true,
    "periodic-smooth32-periodic:independent-analysis": true,
    "periodic-smooth32-periodic:left-inverse": true,
    "periodic-smooth32-periodic:coefficient-count": true,
    "periodic-smooth32-periodic:padding-energy-ledger": true,
    "periodic-smooth32-periodic-none:finite-and-owned-shape": true,
    "periodic-smooth32-periodic-none:independent-synthesis": true,
    "periodic-smooth32-periodic-none:perfect-reconstruction": true,
    "periodic-smooth32-periodic-none:critical-squared-error-identity": true,
    "periodic-smooth32-periodic-hard:finite-and-owned-shape": true,
    "periodic-smooth32-periodic-hard:independent-synthesis": true,
    "periodic-smooth32-periodic-hard:critical-squared-error-identity": true,
    "periodic-smooth32-periodic-soft:finite-and-owned-shape": true,
    "periodic-smooth32-periodic-soft:independent-synthesis": true,
    "periodic-smooth32-periodic-soft:critical-squared-error-identity": true,
    "periodic-smooth32-symmetric:independent-analysis": true,
    "periodic-smooth32-symmetric:left-inverse": true,
    "periodic-smooth32-symmetric:coefficient-count": true,
    "periodic-smooth32-symmetric:padding-energy-ledger": true,
    "periodic-smooth32-symmetric-none:finite-and-owned-shape": true,
    "periodic-smooth32-symmetric-none:independent-synthesis": true,
    "periodic-smooth32-symmetric-none:perfect-reconstruction": true,
    "periodic-smooth32-symmetric-none:critical-squared-error-identity": true,
    "periodic-smooth32-symmetric-hard:finite-and-owned-shape": true,
    "periodic-smooth32-symmetric-hard:independent-synthesis": true,
    "periodic-smooth32-symmetric-hard:critical-squared-error-identity": true,
    "periodic-smooth32-symmetric-soft:finite-and-owned-shape": true,
    "periodic-smooth32-symmetric-soft:independent-synthesis": true,
    "periodic-smooth32-symmetric-soft:critical-squared-error-identity": true,
    "step32-periodic:independent-analysis": true,
    "step32-periodic:left-inverse": true,
    "step32-periodic:coefficient-count": true,
    "step32-periodic:padding-energy-ledger": true,
    "step32-periodic-none:finite-and-owned-shape": true,
    "step32-periodic-none:independent-synthesis": true,
    "step32-periodic-none:perfect-reconstruction": true,
    "step32-periodic-none:critical-squared-error-identity": true,
    "step32-periodic-hard:finite-and-owned-shape": true,
    "step32-periodic-hard:independent-synthesis": true,
    "step32-periodic-hard:critical-squared-error-identity": true,
    "step32-periodic-soft:finite-and-owned-shape": true,
    "step32-periodic-soft:independent-synthesis": true,
    "step32-periodic-soft:critical-squared-error-identity": true,
    "step32-symmetric:independent-analysis": true,
    "step32-symmetric:left-inverse": true,
    "step32-symmetric:coefficient-count": true,
    "step32-symmetric:padding-energy-ledger": true,
    "step32-symmetric-none:finite-and-owned-shape": true,
    "step32-symmetric-none:independent-synthesis": true,
    "step32-symmetric-none:perfect-reconstruction": true,
    "step32-symmetric-none:critical-squared-error-identity": true,
    "step32-symmetric-hard:finite-and-owned-shape": true,
    "step32-symmetric-hard:independent-synthesis": true,
    "step32-symmetric-hard:critical-squared-error-identity": true,
    "step32-symmetric-soft:finite-and-owned-shape": true,
    "step32-symmetric-soft:independent-synthesis": true,
    "step32-symmetric-soft:critical-squared-error-identity": true,
    "ramp17-periodic:independent-analysis": true,
    "ramp17-periodic:left-inverse": true,
    "ramp17-periodic:coefficient-count": true,
    "ramp17-periodic:padding-energy-ledger": true,
    "ramp17-periodic-none:finite-and-owned-shape": true,
    "ramp17-periodic-none:independent-synthesis": true,
    "ramp17-periodic-none:perfect-reconstruction": true,
    "ramp17-periodic-hard:finite-and-owned-shape": true,
    "ramp17-periodic-hard:independent-synthesis": true,
    "ramp17-periodic-soft:finite-and-owned-shape": true,
    "ramp17-periodic-soft:independent-synthesis": true,
    "ramp17-symmetric:independent-analysis": true,
    "ramp17-symmetric:left-inverse": true,
    "ramp17-symmetric:coefficient-count": true,
    "ramp17-symmetric:padding-energy-ledger": true,
    "ramp17-symmetric-none:finite-and-owned-shape": true,
    "ramp17-symmetric-none:independent-synthesis": true,
    "ramp17-symmetric-none:perfect-reconstruction": true,
    "ramp17-symmetric-hard:finite-and-owned-shape": true,
    "ramp17-symmetric-hard:independent-synthesis": true,
    "ramp17-symmetric-soft:finite-and-owned-shape": true,
    "ramp17-symmetric-soft:independent-synthesis": true,
    "step17-periodic:independent-analysis": true,
    "step17-periodic:left-inverse": true,
    "step17-periodic:coefficient-count": true,
    "step17-periodic:padding-energy-ledger": true,
    "step17-periodic-none:finite-and-owned-shape": true,
    "step17-periodic-none:independent-synthesis": true,
    "step17-periodic-none:perfect-reconstruction": true,
    "step17-periodic-hard:finite-and-owned-shape": true,
    "step17-periodic-hard:independent-synthesis": true,
    "step17-periodic-soft:finite-and-owned-shape": true,
    "step17-periodic-soft:independent-synthesis": true,
    "step17-symmetric:independent-analysis": true,
    "step17-symmetric:left-inverse": true,
    "step17-symmetric:coefficient-count": true,
    "step17-symmetric:padding-energy-ledger": true,
    "step17-symmetric-none:finite-and-owned-shape": true,
    "step17-symmetric-none:independent-synthesis": true,
    "step17-symmetric-none:perfect-reconstruction": true,
    "step17-symmetric-hard:finite-and-owned-shape": true,
    "step17-symmetric-hard:independent-synthesis": true,
    "step17-symmetric-soft:finite-and-owned-shape": true,
    "step17-symmetric-soft:independent-synthesis": true,
    "step32-shift1-periodic:independent-analysis": true,
    "step32-shift1-periodic:left-inverse": true,
    "step32-shift1-periodic:coefficient-count": true,
    "step32-shift1-periodic:padding-energy-ledger": true,
    "step32-shift1-periodic-none:finite-and-owned-shape": true,
    "step32-shift1-periodic-none:independent-synthesis": true,
    "step32-shift1-periodic-none:perfect-reconstruction": true,
    "step32-shift1-periodic-none:critical-squared-error-identity": true,
    "step32-shift1-periodic-hard:finite-and-owned-shape": true,
    "step32-shift1-periodic-hard:independent-synthesis": true,
    "step32-shift1-periodic-hard:critical-squared-error-identity": true,
    "step32-shift1-periodic-soft:finite-and-owned-shape": true,
    "step32-shift1-periodic-soft:independent-synthesis": true,
    "step32-shift1-periodic-soft:critical-squared-error-identity": true,
    "step32-shift1-symmetric:independent-analysis": true,
    "step32-shift1-symmetric:left-inverse": true,
    "step32-shift1-symmetric:coefficient-count": true,
    "step32-shift1-symmetric:padding-energy-ledger": true,
    "step32-shift1-symmetric-none:finite-and-owned-shape": true,
    "step32-shift1-symmetric-none:independent-synthesis": true,
    "step32-shift1-symmetric-none:perfect-reconstruction": true,
    "step32-shift1-symmetric-none:critical-squared-error-identity": true,
    "step32-shift1-symmetric-hard:finite-and-owned-shape": true,
    "step32-shift1-symmetric-hard:independent-synthesis": true,
    "step32-shift1-symmetric-hard:critical-squared-error-identity": true,
    "step32-shift1-symmetric-soft:finite-and-owned-shape": true,
    "step32-shift1-symmetric-soft:independent-synthesis": true,
    "step32-shift1-symmetric-soft:critical-squared-error-identity": true,
    "step17-shift1-periodic:independent-analysis": true,
    "step17-shift1-periodic:left-inverse": true,
    "step17-shift1-periodic:coefficient-count": true,
    "step17-shift1-periodic:padding-energy-ledger": true,
    "step17-shift1-periodic-none:finite-and-owned-shape": true,
    "step17-shift1-periodic-none:independent-synthesis": true,
    "step17-shift1-periodic-none:perfect-reconstruction": true,
    "step17-shift1-periodic-hard:finite-and-owned-shape": true,
    "step17-shift1-periodic-hard:independent-synthesis": true,
    "step17-shift1-periodic-soft:finite-and-owned-shape": true,
    "step17-shift1-periodic-soft:independent-synthesis": true,
    "step17-shift1-symmetric:independent-analysis": true,
    "step17-shift1-symmetric:left-inverse": true,
    "step17-shift1-symmetric:coefficient-count": true,
    "step17-shift1-symmetric:padding-energy-ledger": true,
    "step17-shift1-symmetric-none:finite-and-owned-shape": true,
    "step17-shift1-symmetric-none:independent-synthesis": true,
    "step17-shift1-symmetric-none:perfect-reconstruction": true,
    "step17-shift1-symmetric-hard:finite-and-owned-shape": true,
    "step17-shift1-symmetric-hard:independent-synthesis": true,
    "step17-shift1-symmetric-soft:finite-and-owned-shape": true,
    "step17-shift1-symmetric-soft:independent-synthesis": true,
    "fixed-analysis-and-reconstruction-count": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/haar-mallat-boundary-threshold/index.json

![長さ17・32の小信号に3段Haar分解を適用。1標本シフトと奇数長の境界処理を分けて比較します。 保存配列から作図。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/haar-mallat-boundary-threshold-preview.png)

長さ17・32の小信号に3段Haar分解を適用。1標本シフトと奇数長の境界処理を分けて比較します。 保存配列から作図。

![保存済み誤差・導関数または二乗ノルムを別表示。各境界・表現の適用範囲は本文を参照。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/haar-mallat-boundary-threshold-diagnostics.png)

保存済み誤差・導関数または二乗ノルムを別表示。各境界・表現の適用範囲は本文を参照。

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/atlas-approximation-controls-2026-11-25.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

### 出典と確認範囲

- S. Mallat, A Theory for Multiresolution Signal Decomposition: The Wavelet Representation [accessed 2026-11-24]. https://www.di.ens.fr/~mallat/papiers/MallatTheory89.pdf; review_level=primary-paper-selected-body
During preparation: title/abstract, Haar example on printed p. 679, selected §III-B/C filter/downsample/inverse-pyramid and border-symmetry prose on p. 681. Extracted formula glyphs were imperfect; no complete proof or numerical-table audit is claimed.

- PyWavelets documentation: Signal extension modes [accessed 2026-11-25]. https://pywavelets.readthedocs.io/en/latest/ref/signal-extension-modes.html; review_level=official-documentation-selected-terminology
Periodic and half-sample symmetric extension and the redundancy caveat. This example defines its own append-at-each-odd-level/crop convention; it does not claim PyWavelets coefficient-layout equivalence or require PyWavelets.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
