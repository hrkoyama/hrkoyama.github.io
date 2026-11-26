# 等方散乱平板と連続角度参照

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-radiation-scattering/

この章に登録された手法・問題・実行例の関連資料です。 等方散乱平板の角度離散法を、連続角度の積分方程式から得た独立参照に照合します。

## 手法

- [輻射輸送・モーメント法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/radiation-transport/?lang=ja>)

  保存的風上FVの全方向source結合を離散sweep応答で解きます。半球ごとの正重みGaussにより入射流束πを正規化し、吸収は体積sourceから独立積算します。
- [風上差分（upwind）](<https://hrkoyama.github.io/numerical-methods-atlas/methods/upwind/?lang=ja>)

  保存的風上FVの全方向source結合を離散sweep応答で解きます。半球ごとの正重みGaussにより入射流束πを正規化し、吸収は体積sourceから独立積算します。
- [輻射輸送・モーメント法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/radiation-transport/?lang=ja>)
- [風上差分（upwind）](<https://hrkoyama.github.io/numerical-methods-atlas/methods/upwind/?lang=ja>)

## 方程式

- [静止媒質の灰色輻射輸送・散乱・線形交換](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#static-grey-transfer-ja>)

  正規化した角度平均を使います。物質交換は1997輸送例と周期Fourier比較で進めます。1997の光学座標では係数1、物理座標の比較ではκを輻射・物質の両交換項に掛けます。 光学厚さ.5/3、単一散乱albedo.5/.9の4入力。左の等方入射I1、右入射0。64/128/256セル、32角と独立64角probe。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/isotropic-scattering-slab/?lang=ja#isotropic-scattering-slab-ja-algorithm>)

  保存的風上FVの全方向source結合を離散sweep応答で解きます。半球ごとの正重みGaussにより入射流束πを正規化し、吸収は体積sourceから独立積算します。
- [静止媒質の灰色輻射輸送・散乱・線形交換](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#static-grey-transfer-ja>)

  正規化した角度平均を使います。物質交換は1997輸送例と周期Fourier比較で進めます。1997の光学座標では係数1、物理座標の比較ではκを輻射・物質の両交換項に掛けます。

## 問題の図

- [等方散乱平板の反射・透過・吸収](<https://hrkoyama.github.io/numerical-methods-atlas/problems/isotropic-scattering-slab/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/results/isotropic-scattering-slab-preview.png
- [等方散乱平板の反射・透過・吸収](<https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/results/isotropic-scattering-slab.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/results/isotropic-scattering-slab.png

## 厳密解・参照解

- [等方散乱平板の反射・透過・吸収：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/isotropic-scattering-slab/?lang=ja#references-ja>)

  独立参照78項目はmain前に合格。主18計算では収支・正値・残差と、別々の空間・角度差、純吸収・保存散乱controlを判定します。
- [等方散乱平板：連続角Fredholm流束参照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-isotropic-scattering-slab-ja>)
  relation: same-problem
  reference_kind: semi-analytic

  半解析解 平行平板の定常な光学厚さ座標を用い、左の入射輻射輝度は1、右の入射は真空、等方散乱の単一散乱アルベドを固定します。入射半球流束はπ、符号付き角度の平均はJ=(1/2)∫I dμです。 有限の4平板に限定。MC、一般角度phase関数、DISORT再現、普遍的次数や厳密連続体誤差境界は認証しません。
- [等方散乱平板：連続角Fredholm流束参照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-isotropic-scattering-slab-ja>)
  reference_kind: semi-analytic

  半解析解 平行平板の定常な光学厚さ座標を用い、左の入射輻射輝度は1、右の入射は真空、等方散乱の単一散乱アルベドを固定します。入射半球流束はπ、符号付き角度の平均はJ=(1/2)∫I dμです。
- [等方散乱平板の反射・透過・吸収：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/isotropic-scattering-slab/?lang=ja#isotropic-scattering-slab-ja-validation>)

  独立参照78項目はmain前に合格。主18計算では収支・正値・残差と、別々の空間・角度差、純吸収・保存散乱controlを判定します。
- [等方散乱平板：連続角Fredholm流束参照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-isotropic-scattering-slab-ja>)
  relation: same-problem
  reference_kind: semi-analytic

  半解析解 平行平板の定常な光学厚さ座標を用い、左の入射輻射輝度は1、右の入射は真空、等方散乱の単一散乱アルベドを固定します。入射半球流束はπ、符号付き角度の平均はJ=(1/2)∫I dμです。 有限の4平板に限定。MC、一般角度phase関数、DISORT再現、普遍的次数や厳密連続体誤差境界は認証しません。

## コード・検証

- [等方散乱平板の反射・透過・吸収](<https://hrkoyama.github.io/numerical-methods-atlas/validation/isotropic-scattering-slab/?lang=ja>)
  availability: run

  正負の角度を結合した実際の定常輸送を解き、独立な連続角Fredholm参照とR/T/Aを比較します。
