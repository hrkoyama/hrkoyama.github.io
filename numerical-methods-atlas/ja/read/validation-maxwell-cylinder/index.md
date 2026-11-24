# 2D誘電体円柱のMie散乱幅

実際の2D散乱場を進め、閉曲線Poynting流束と独立な円柱級数を比較します。

共通22実行例の台帳とは別に管理する追加検証集です。配布ZIPを独立展開し、各グループの全固定入力と検査を実行した記録を示します。設定・手法・刻み幅の違いを独立した物理問題の数には加算しません。

## 2D誘電体円柱のMie散乱幅

実際の2D散乱場を進め、閉曲線Poynting流束と独立な円柱級数を比較します。

**使用手法**

- [Yee FDTD](https://hrkoyama.github.io/numerical-methods-atlas/methods/fdtd/?lang=ja) (`fdtd`)
- [2ステップleapfrog法](https://hrkoyama.github.io/numerical-methods-atlas/methods/leapfrog/?lang=ja) (`leapfrog`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/cylinder-mie2d/?lang=ja#cylinder-mie2d-ja-algorithm)

Yeeの散乱場を局所分極contrastの厳密な離散入射差分で励起します。EとHはそれぞれの整数・半時刻でFourier集計し、Hの4点補間後に物理流束を積分します。

$$
\varepsilon\partial_tE_z=\partial_xH_y-\partial_yH_x,\quad\partial_tH_x=-\partial_yE_z,\quad\partial_tH_y=\partial_xE_z
$$

$$
\Sigma_{\mathrm{sca}}=\frac4k\sum_{n=-\infty}^{\infty}|a_n|^2,\quad\Sigma_{\mathrm{ext}}=-\frac4k\sum_n\operatorname{Re}a_n
$$

- [線形Maxwell電磁場（真空・誘電体）](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#maxwell-ja) (`maxwell`)

c=ε0=μ0=1。無限円柱のEz偏光、半径0.25、比誘電率2.25、真空波長1。6×6領域と4辺PML、明示的な節点階段状形状です。


**問題の図**

![2D誘電体円柱のMie散乱幅：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-cylinder/results/cylinder-mie2d.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[2D誘電体円柱のMie散乱幅](https://hrkoyama.github.io/numerical-methods-atlas/problems/cylinder-mie2d/?lang=ja) (`cylinder-mie2d`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/cylinder-mie2d/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/cylinder-mie2d/?lang=ja#cylinder-mie2d-ja-validation)

12/18/24点/波長、32周期の過渡除去と8周期の計測。2本の閉曲線、前後4周期、同じ全時間を進めた半振幅phasorと5保存時刻の真空対照を検査し、円柱級数の散乱幅と外部場を照合します。

- [誘電体円柱の外部級数と散乱幅](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-cylinder-mie2d-ja) (`cylinder-mie2d`; 同じ問題の参照 · 解析参照)

Ezの無損失2D円柱のみで、3D球ではありません。階段状形状の誤差を記録し、一般の曲面2次精度や任意周波数・材料での精密散乱を保証しません。
### 前提・単位・境界

c=ε0=μ0=1。無限円柱のEz偏光、半径0.25、比誘電率2.25、真空波長1。6×6領域と4辺PML、明示的な節点階段状形状です。

**編集上の補足**

Ezの無損失2D円柱のみで、3D球ではありません。階段状形状の誤差を記録し、一般の曲面2次精度や任意周波数・材料での精密散乱を保証しません。 図の中央の白抜きは診断用のr<0.4のマスクで、物理円柱の半径0.25とは区別します。

### 採用した計算法

Yeeの散乱場を局所分極contrastの厳密な離散入射差分で励起します。EとHはそれぞれの整数・半時刻でFourier集計し、Hの4点補間後に物理流束を積分します。

$$
\varepsilon\partial_tE_z=\partial_xH_y-\partial_yH_x,\quad\partial_tH_x=-\partial_yE_z,\quad\partial_tH_y=\partial_xE_z
$$

$$
\Sigma_{\mathrm{sca}}=\frac4k\sum_{n=-\infty}^{\infty}|a_n|^2,\quad\Sigma_{\mathrm{ext}}=-\frac4k\sum_n\operatorname{Re}a_n
$$

### 比較・検証

12/18/24点/波長、32周期の過渡除去と8周期の計測。2本の閉曲線、前後4周期、同じ全時間を進めた半振幅phasorと5保存時刻の真空対照を検査し、円柱級数の散乱幅と外部場を照合します。

### 確認の限界

Ezの無損失2D円柱のみで、3D球ではありません。階段状形状の誤差を記録し、一般の曲面2次精度や任意周波数・材料での精密散乱を保証しません。

### 保存実測値と判定

```json
{
  "metrics": {
    "completed_primary_and_control_runs": 5,
    "spatial_dimensions": 2,
    "geometry": "Explicitnodalstaircase,noorderclaim",
    "scattering_is_power_integral": true,
    "reference": "IndependentordinarycylindricalJ/H1,notspherical",
    "gallery_source": 145,
    "finest_scattering_width": 0.9571725126288017,
    "independent_scattering_width": 0.9778618212649008,
    "finest_width_relative_error": 0.02115770161610031,
    "finest_exterior_field_relative_error": 0.030278686279997306,
    "complete_run_phasor_linearity": 0.0
  },
  "checks": {
    "reference-and-new-components-qualified": true,
    "cylinder-ppw12/finite": true,
    "cylinder-ppw12/outward-scattering-power": true,
    "cylinder-ppw12/closed-contour-sensitivity": true,
    "cylinder-ppw12/fixed-window-sensitivity": true,
    "cylinder-ppw18/finite": true,
    "cylinder-ppw18/outward-scattering-power": true,
    "cylinder-ppw18/closed-contour-sensitivity": true,
    "cylinder-ppw18/fixed-window-sensitivity": true,
    "cylinder-ppw24/finite": true,
    "cylinder-ppw24/outward-scattering-power": true,
    "cylinder-ppw24/closed-contour-sensitivity": true,
    "cylinder-ppw24/fixed-window-sensitivity": true,
    "finest-scattering-width": true,
    "finest-exterior-scattered-field": true,
    "coarse-to-finest-improvement": true,
    "complete-run-phasor-linearity": true,
    "complete-run-power-quadratic": true,
    "zero-contrast-stored-snapshot-fields": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/cylinder-mie2d/index.json

![保存した最細格子の実2D散乱電場phasorの実部。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-cylinder/results/cylinder-mie2d-preview.png)

保存した最細格子の実2D散乱電場phasorの実部。

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-cylinder/atlas-maxwell-cylinder-2026-11-24-r2.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-cylinder/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-cylinder/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-cylinder/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

### 出典と確認範囲

- Ansys Optics (n.d.). Mie scattering 2D [accessed 2026-11-24]. https://optics.ansys.com/hc/en-us/articles/360042703373-Mie-scattering-2D; review_level=primary-official-documentation-selected-example
Read the complete substantive benchmark description: two-dimensional dielectric cylinder, TFSF, angular far field and lossless cross sections. Did not read the associated simulation files, theory table or cited book; no external numerical data imported. Publication and revision dates have not been verified. Accessed on 2026-11-24; this is a consultation date, not a publication year.

- NIST DLMF. Bessel and Hankel Wronskians, section10.5 (version 1.2.8, released 2026-09-15) [accessed 2026-11-24]. https://dlmf.nist.gov/10.5; review_level=primary-official-mathematical-identity
Read section 10.5, especially equation 10.5.3 for the ordinary J/Hankel1 Wronskian; version 1.2.8. Cylinder boundary algebra is independently derived here. The year 2026 denotes DLMF version 1.2.8, released on 2026-09-15, not its initial publication year. Accessed on 2026-11-24.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
