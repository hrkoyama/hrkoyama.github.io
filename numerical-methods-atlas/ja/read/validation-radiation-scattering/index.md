# 等方散乱平板と連続角度参照

等方散乱平板の角度離散法を、連続角度の積分方程式から得た独立参照に照合します。

共通22実行例の台帳とは別に管理する追加検証集です。配布ZIPを独立展開し、各グループの全固定入力と検査を実行した記録を示します。設定・手法・刻み幅の違いを独立した物理問題の数には加算しません。

## 等方散乱平板の反射・透過・吸収

正負の角度を結合した実際の定常輸送を解き、独立な連続角Fredholm参照とR/T/Aを比較します。

**使用手法**

- [放射輸送・モーメント法](https://hrkoyama.github.io/numerical-methods-atlas/methods/radiation-transport/?lang=ja) (`radiation-transport`)
- [風上差分（upwind）](https://hrkoyama.github.io/numerical-methods-atlas/methods/upwind/?lang=ja) (`upwind`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/isotropic-scattering-slab/?lang=ja#isotropic-scattering-slab-ja-algorithm)

保存的風上FVの全方向source結合を離散sweep応答で解きます。半球ごとの正重みGaussにより入射流束πを正規化し、吸収は体積sourceから独立積算します。

$$
\mu\partial_xI+I=\omega J,\quad J=\frac12\int_{-1}^{1}I\,d\mu
$$

$$
J(x)=\frac12E_2(x)+\frac\omega2\int_0^L E_1(|x-s|)J(s)\,ds
$$

$$
R+T+A=1,\qquad A=4(1-\omega)\int_0^LJ\,dx
$$

- [静止媒質の灰色放射輸送・散乱・線形交換](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#static-grey-transfer-ja) (`static-grey-transfer`)

光学厚さ.5/3、単一散乱albedo.5/.9の4入力。左の等方入射I1、右入射0。64/128/256セル、32角と独立64角probe。


**問題の図**

![等方散乱平板の反射・透過・吸収：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/results/isotropic-scattering-slab.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[等方散乱平板の反射・透過・吸収](https://hrkoyama.github.io/numerical-methods-atlas/problems/isotropic-scattering-slab/?lang=ja) (`isotropic-scattering-slab`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/isotropic-scattering-slab/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/isotropic-scattering-slab/?lang=ja#isotropic-scattering-slab-ja-validation)

独立参照78項目はmain前に合格。主18計算では収支・正値・残差と、別々の空間・角度差、純吸収・保存散乱controlを判定します。

- [等方散乱平板：連続角Fredholm流束参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-isotropic-scattering-slab-ja) (`isotropic-scattering-slab`; 同じ問題の参照 · 半解析参照)

有限の4平板に限定。MC、一般角度phase関数、DISORT再現、普遍的次数や厳密連続体誤差境界は認証しません。
### 前提・単位・境界

光学厚さ.5/3、単一散乱albedo.5/.9の4入力。左の等方入射I1、右入射0。64/128/256セル、32角と独立64角probe。

**編集上の補足**

有限の4平板に限定。MC、一般角度phase関数、DISORT再現、普遍的次数や厳密連続体誤差境界は認証しません。

### 採用した計算法

保存的風上FVの全方向source結合を離散sweep応答で解きます。半球ごとの正重みGaussにより入射流束πを正規化し、吸収は体積sourceから独立積算します。

$$
\mu\partial_xI+I=\omega J,\quad J=\frac12\int_{-1}^{1}I\,d\mu
$$

$$
J(x)=\frac12E_2(x)+\frac\omega2\int_0^L E_1(|x-s|)J(s)\,ds
$$

$$
R+T+A=1,\qquad A=4(1-\omega)\int_0^LJ\,dx
$$

### 比較・検証

独立参照78項目はmain前に合格。主18計算では収支・正値・残差と、別々の空間・角度差、純吸収・保存散乱controlを判定します。

### 確認の限界

有限の4平板に限定。MC、一般角度phase関数、DISORT再現、普遍的次数や厳密連続体誤差境界は認証しません。

### 保存実測値と判定

```json
{
  "metrics": {
    "completed_runs": 18,
    "scattering_slabs": 4,
    "continuum_angle_reference": true,
    "separate_space_angle_probes": true,
    "stochastic_runs": 0
  },
  "checks": {
    "slab0-n64-s32/finite-positive": true,
    "slab0-n64-s32/residual": true,
    "slab0-n64-s32/source_residual": true,
    "slab0-n64-s32/balance": true,
    "slab0-n64-s32/physical-fluxes": true,
    "slab0-n128-s32/finite-positive": true,
    "slab0-n128-s32/residual": true,
    "slab0-n128-s32/source_residual": true,
    "slab0-n128-s32/balance": true,
    "slab0-n128-s32/physical-fluxes": true,
    "slab0-n256-s32/finite-positive": true,
    "slab0-n256-s32/residual": true,
    "slab0-n256-s32/source_residual": true,
    "slab0-n256-s32/balance": true,
    "slab0-n256-s32/physical-fluxes": true,
    "slab0-n256-s64/finite-positive": true,
    "slab0-n256-s64/residual": true,
    "slab0-n256-s64/source_residual": true,
    "slab0-n256-s64/balance": true,
    "slab0-n256-s64/physical-fluxes": true,
    "slab0/refinement-n128": true,
    "slab0/refinement-n256": true,
    "slab0/finest-independent-error": true,
    "slab0/space-probe": true,
    "slab0/angle-probe": true,
    "slab1-n64-s32/finite-positive": true,
    "slab1-n64-s32/residual": true,
    "slab1-n64-s32/source_residual": true,
    "slab1-n64-s32/balance": true,
    "slab1-n64-s32/physical-fluxes": true,
    "slab1-n128-s32/finite-positive": true,
    "slab1-n128-s32/residual": true,
    "slab1-n128-s32/source_residual": true,
    "slab1-n128-s32/balance": true,
    "slab1-n128-s32/physical-fluxes": true,
    "slab1-n256-s32/finite-positive": true,
    "slab1-n256-s32/residual": true,
    "slab1-n256-s32/source_residual": true,
    "slab1-n256-s32/balance": true,
    "slab1-n256-s32/physical-fluxes": true,
    "slab1-n256-s64/finite-positive": true,
    "slab1-n256-s64/residual": true,
    "slab1-n256-s64/source_residual": true,
    "slab1-n256-s64/balance": true,
    "slab1-n256-s64/physical-fluxes": true,
    "slab1/refinement-n128": true,
    "slab1/refinement-n256": true,
    "slab1/finest-independent-error": true,
    "slab1/space-probe": true,
    "slab1/angle-probe": true,
    "slab2-n64-s32/finite-positive": true,
    "slab2-n64-s32/residual": true,
    "slab2-n64-s32/source_residual": true,
    "slab2-n64-s32/balance": true,
    "slab2-n64-s32/physical-fluxes": true,
    "slab2-n128-s32/finite-positive": true,
    "slab2-n128-s32/residual": true,
    "slab2-n128-s32/source_residual": true,
    "slab2-n128-s32/balance": true,
    "slab2-n128-s32/physical-fluxes": true,
    "slab2-n256-s32/finite-positive": true,
    "slab2-n256-s32/residual": true,
    "slab2-n256-s32/source_residual": true,
    "slab2-n256-s32/balance": true,
    "slab2-n256-s32/physical-fluxes": true,
    "slab2-n256-s64/finite-positive": true,
    "slab2-n256-s64/residual": true,
    "slab2-n256-s64/source_residual": true,
    "slab2-n256-s64/balance": true,
    "slab2-n256-s64/physical-fluxes": true,
    "slab2/refinement-n128": true,
    "slab2/refinement-n256": true,
    "slab2/finest-independent-error": true,
    "slab2/space-probe": true,
    "slab2/angle-probe": true,
    "slab3-n64-s32/finite-positive": true,
    "slab3-n64-s32/residual": true,
    "slab3-n64-s32/source_residual": true,
    "slab3-n64-s32/balance": true,
    "slab3-n64-s32/physical-fluxes": true,
    "slab3-n128-s32/finite-positive": true,
    "slab3-n128-s32/residual": true,
    "slab3-n128-s32/source_residual": true,
    "slab3-n128-s32/balance": true,
    "slab3-n128-s32/physical-fluxes": true,
    "slab3-n256-s32/finite-positive": true,
    "slab3-n256-s32/residual": true,
    "slab3-n256-s32/source_residual": true,
    "slab3-n256-s32/balance": true,
    "slab3-n256-s32/physical-fluxes": true,
    "slab3-n256-s64/finite-positive": true,
    "slab3-n256-s64/residual": true,
    "slab3-n256-s64/source_residual": true,
    "slab3-n256-s64/balance": true,
    "slab3-n256-s64/physical-fluxes": true,
    "slab3/refinement-n128": true,
    "slab3/refinement-n256": true,
    "slab3/finest-independent-error": true,
    "slab3/space-probe": true,
    "slab3/angle-probe": true,
    "control0/budget": true,
    "control0/pure-absorption": true,
    "control1/budget": true,
    "control1/conservative": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/isotropic-scattering-slab/index.json

![保存した実計算場の科学プレビュー。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/results/isotropic-scattering-slab-preview.png)

保存した実計算場の科学プレビュー。

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/atlas-radiation-scattering-2026-11-24.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

### 出典と確認範囲

- Pharr,Jakob,Humphreys (2023). Physically Based Rendering4e,14.1The Equation of Transfer. https://www.pbr-book.org/4ed/Light_Transport_II_Volume_Rendering/The_Equation_of_Transfer; review_level=primary-author-book-selected-equations
Read14.1transfer/source/finite-ray boundary formulation. Isotropic slab/Fredholm normalization independently derived here;not DISORTpaper/table reproduction.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
