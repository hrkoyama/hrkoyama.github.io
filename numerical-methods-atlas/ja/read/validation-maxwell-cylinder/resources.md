# 2D誘電体円柱のMie散乱幅

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-maxwell-cylinder/

この章に登録された手法・問題・実行例の関連資料です。 実際の2D散乱場を進め、閉曲線Poynting流束と独立な円柱級数を比較します。

## 手法

- [Yee FDTD](<https://hrkoyama.github.io/numerical-methods-atlas/methods/fdtd/?lang=ja>)

  Yeeの散乱場を局所分極contrastの厳密な離散入射差分で励起します。EとHはそれぞれの整数・半時刻でFourier集計し、Hの4点補間後に物理流束を積分します。
- [2ステップleapfrog法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/leapfrog/?lang=ja>)

  Yeeの散乱場を局所分極contrastの厳密な離散入射差分で励起します。EとHはそれぞれの整数・半時刻でFourier集計し、Hの4点補間後に物理流束を積分します。
- [Yee FDTD](<https://hrkoyama.github.io/numerical-methods-atlas/methods/fdtd/?lang=ja>)
- [2ステップleapfrog法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/leapfrog/?lang=ja>)

## 方程式

- [線形Maxwell電磁場（真空・誘電体）](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#maxwell-ja>)

  代表式は3D線形電磁場です。今回の実装はz不変の円柱Ez/Hx/Hyに制限した真2D Yee計算です。 c=ε0=μ0=1。無限円柱のEz偏光、半径0.25、比誘電率2.25、真空波長1。6×6領域と4辺PML、明示的な節点階段状形状です。
- [線形Maxwell電磁場（真空・誘電体）](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#maxwell-ja>)

  代表式は3D線形電磁場です。今回の実装はz不変の円柱Ez/Hx/Hyに制限した真2D Yee計算です。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/cylinder-mie2d/?lang=ja#cylinder-mie2d-ja-algorithm>)

  Yeeの散乱場を局所分極contrastの厳密な離散入射差分で励起します。EとHはそれぞれの整数・半時刻でFourier集計し、Hの4点補間後に物理流束を積分します。

## 問題の図

- [2D誘電体円柱のMie散乱幅](<https://hrkoyama.github.io/numerical-methods-atlas/problems/cylinder-mie2d/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-cylinder/results/cylinder-mie2d-preview.png
- [2D誘電体円柱のMie散乱幅](<https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-cylinder/results/cylinder-mie2d.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-cylinder/results/cylinder-mie2d.png

## 厳密解・参照解

- [2D誘電体円柱のMie散乱幅：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/cylinder-mie2d/?lang=ja#references-ja>)

  12/18/24点/波長、32周期の過渡除去と8周期の計測。2本の閉曲線、前後4周期、同じ全時間を進めた半振幅phasorと5保存時刻の真空対照を検査し、円柱級数の散乱幅と外部場を照合します。
- [誘電体円柱の外部級数と散乱幅](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-cylinder-mie2d-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 無損失無限円柱、Ez偏光、c=ε0=μ0=1、半径0.25、ε=2.25、真空波長1。解析場は厳密な円の外部だけです。 Ezの無損失2D円柱のみで、3D球ではありません。階段状形状の誤差を記録し、一般の曲面2次精度や任意周波数・材料での精密散乱を保証しません。
- [誘電体円柱の外部級数と散乱幅](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-cylinder-mie2d-ja>)
  reference_kind: analytic

  解析解 無損失無限円柱、Ez偏光、c=ε0=μ0=1、半径0.25、ε=2.25、真空波長1。解析場は厳密な円の外部だけです。
- [2D誘電体円柱のMie散乱幅：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/cylinder-mie2d/?lang=ja#cylinder-mie2d-ja-validation>)

  12/18/24点/波長、32周期の過渡除去と8周期の計測。2本の閉曲線、前後4周期、同じ全時間を進めた半振幅phasorと5保存時刻の真空対照を検査し、円柱級数の散乱幅と外部場を照合します。
- [誘電体円柱の外部級数と散乱幅](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-cylinder-mie2d-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 無損失無限円柱、Ez偏光、c=ε0=μ0=1、半径0.25、ε=2.25、真空波長1。解析場は厳密な円の外部だけです。 Ezの無損失2D円柱のみで、3D球ではありません。階段状形状の誤差を記録し、一般の曲面2次精度や任意周波数・材料での精密散乱を保証しません。

## コード・検証

- [2D誘電体円柱のMie散乱幅](<https://hrkoyama.github.io/numerical-methods-atlas/validation/cylinder-mie2d/?lang=ja>)
  availability: run

  実際の2D散乱場を進め、閉曲線Poynting流束と独立な円柱級数を比較します。
