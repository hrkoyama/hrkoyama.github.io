# PICの独立空間実装との照合

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-pic-spatial/

この章に登録された手法・問題・実行例の関連資料です。 各kickで独立なCICと明示DFTから場を更新し、同じ時間積分の共有範囲を明示します。

## 手法

- [Particle-in-Cell（PIC）](<https://hrkoyama.github.io/numerical-methods-atlas/methods/pic/?lang=ja>)
- [Cloud-in-cellの割当てと補間](<https://hrkoyama.github.io/numerical-methods-atlas/methods/cic/?lang=ja>)
- [速度Verlet／粒子leapfrog法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/verlet/?lang=ja>)

## 方程式

- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/pic-independent-spatial/?lang=ja#pic-independent-spatial-ja-algorithm>)

  独立側はPythonスカラー配置、明示的な複素DFT和、独自の補間ループを所有します。主側のFFT・配置・補間を呼びません。数学上のCIC、Nyquist規約、velocity-Verlet法、初期配列は共通です。
- [静電Vlasov–Poisson方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#vlasov-poisson-ja>)

  1D1V電子と固定中性化背景。重み付き全分布PICの粒子・格子・時間近似と、線形参照の範囲を分けます。

## 問題の図

- [PIC空間演算の独立実装照合](<https://hrkoyama.github.io/code/validated-examples/2026-11-23/pic-spatial/results/pic-independent-spatial.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/pic-spatial/results/pic-independent-spatial.png
- [CIC静電PICの冷たいプラズマ振動](<https://hrkoyama.github.io/numerical-methods-atlas/problems/cold-plasma-pic/?lang=ja>)

  各kickで独立なCICと明示DFTから場を更新し、同じ時間積分の共有範囲を明示します。 テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/pic.png

## 厳密解・参照解

- [PIC空間演算の独立実装照合](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-pic-independent-spatial-ja>)
  reference_kind: numerical-reference

  有限格子の数値参照 周期[0,2π]、256粒子、格子8/16/32、シード35001/35002、dt=.02、T=.24。位置は一様乱数、v=.2 Normal+.1 sin x。6組は別々に進めた12軌道です。 19 pytestと58/58固定判定が合格。6組＝12の自己無撞着軌道を13時刻全てで照合し、最大差は位置8.88e−16・速度3.33e−16・電場8.33e−16・電荷2.89e−15。pytest+mainは0.392秒。最初の小pytestは周期端点の添字不具合で17/18となり、元記録を保持して修正後に全計算を実行しました。 離散演算の独立したコーディング照合です。時間積分法や連続方程式を変えた独立エンジン、連続極限の収束、冷たいプラズマの振動参照の再現を意味しません。既存cold-plasma-picの関連補助検証として扱い、温かい初期速度の軌道を冷たい解と同一視しません。
- [PIC空間演算の独立実装照合：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/pic-independent-spatial/?lang=ja#pic-independent-spatial-ja-validation>)

  19 pytestと58/58固定判定が合格。6組＝12の自己無撞着軌道を13時刻全てで照合し、最大差は位置8.88e−16・速度3.33e−16・電場8.33e−16・電荷2.89e−15。pytest+mainは0.392秒。最初の小pytestは周期端点の添字不具合で17/18となり、元記録を保持して修正後に全計算を実行しました。
- [PIC空間演算の独立実装照合](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-pic-independent-spatial-ja>)
  relation: related-model
  reference_kind: numerical-reference

  有限格子の数値参照 周期[0,2π]、256粒子、格子8/16/32、シード35001/35002、dt=.02、T=.24。位置は一様乱数、v=.2 Normal+.1 sin x。6組は別々に進めた12軌道です。 19 pytestと58/58固定判定が合格。6組＝12の自己無撞着軌道を13時刻全てで照合し、最大差は位置8.88e−16・速度3.33e−16・電場8.33e−16・電荷2.89e−15。pytest+mainは0.392秒。最初の小pytestは周期端点の添字不具合で17/18となり、元記録を保持して修正後に全計算を実行しました。 離散演算の独立したコーディング照合です。時間積分法や連続方程式を変えた独立エンジン、連続極限の収束、冷たいプラズマの振動参照の再現を意味しません。既存cold-plasma-picの関連補助検証として扱い、温かい初期速度の軌道を冷たい解と同一視しません。 周期[0,2π]、256粒子、格子8/16/32、シード35001/35002、dt=.02、T=.24。位置は一様乱数、v=.2 Normal+.1 sin x。6組は別々に進めた12軌道です。
- [CIC静電PICの冷たいプラズマ振動：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/cold-plasma-pic/?lang=ja#references-ja>)

  各kickで独立なCICと明示DFTから場を更新し、同じ時間積分の共有範囲を明示します。 小振幅の冷たいプラズマの線形変位cos(t)と比較し、電荷整合性・Poisson残差・自己力、格子系列と時間刻み系列を確認します。一般の非線形PIC軌道の厳密解という主張ではありません。 追加版は静止イオン背景のまま、電荷・運動量・粒子と場のエネルギーを軌道誤差と分けます。小振幅線形参照であり、熱的Landau減衰や電磁PICの根拠ではありません。
- [PIC空間演算の独立実装照合](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-pic-independent-spatial-ja>)
  relation: related-model
  reference_kind: numerical-reference

  各kickで独立なCICと明示DFTから場を更新し、同じ時間積分の共有範囲を明示します。 有限格子の数値参照 周期[0,2π]、256粒子、格子8/16/32、シード35001/35002、dt=.02、T=.24。位置は一様乱数、v=.2 Normal+.1 sin x。6組は別々に進めた12軌道です。 19 pytestと58/58固定判定が合格。6組＝12の自己無撞着軌道を13時刻全てで照合し、最大差は位置8.88e−16・速度3.33e−16・電場8.33e−16・電荷2.89e−15。pytest+mainは0.392秒。最初の小pytestは周期端点の添字不具合で17/18となり、元記録を保持して修正後に全計算を実行しました。 離散演算の独立したコーディング照合です。時間積分法や連続方程式を変えた独立エンジン、連続極限の収束、冷たいプラズマの振動参照の再現を意味しません。既存cold-plasma-picの関連補助検証として扱い、温かい初期速度の軌道を冷たい解と同一視しません。 周期[0,2π]、256粒子、格子8/16/32、シード35001/35002、dt=.02、T=.24。位置は一様乱数、v=.2 Normal+.1 sin x。6組は別々に進めた12軌道です。

## コード・検証

- [PIC空間演算の独立実装照合](<https://hrkoyama.github.io/numerical-methods-atlas/validation/pic-independent-spatial/?lang=ja>)
  availability: run

  ベクトル化CIC/FFTと、別に書いた粒子ループCIC・密なDFTを、それぞれが自己無撞着な場を毎kick計算する軌道全体で照合します。
