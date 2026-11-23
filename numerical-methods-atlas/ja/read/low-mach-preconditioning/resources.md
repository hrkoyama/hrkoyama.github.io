# 前処理行列・低Mach数・音速点とエントロピー修正

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/low-mach-preconditioning/

この章に登録された手法・問題・実行例の関連資料です。

## 手法

- [Roe音響波のエントロピー修正](<https://hrkoyama.github.io/numerical-methods-atlas/methods/entropy-fix/?lang=ja>)
- [低Mach数のPDE前処理](<https://hrkoyama.github.io/numerical-methods-atlas/methods/low-mach-preconditioning/?lang=ja>)

## 方程式

章固有の対応は未登録です。全体一覧：[方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja)

## 問題の図

章固有の対応は未登録です。全体一覧：[テスト問題の名前と図](https://hrkoyama.github.io/numerical-methods-atlas/gallery/?lang=ja)

## 厳密解・参照解

章固有の対応は未登録です。全体一覧：[厳密解・参照解](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja)

## コード・検証

- [低Mach等エントロピー渦：前処理Roe流束の軽量検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/low-mach-vortex/?lang=ja>)
  availability: run

  同じ非線形2次元Euler渦をN=16/32/64、背景Mach数.1/.01でT=.1まで進め、通常RoeとMiczek型の空間流束前処理を比較します。全12計算で、速度・動圧スケールの圧力誤差、保存収支、音響刻み、実段状態を調べます。
- [Roe音響波のエントロピー修正：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/entropy-fix/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [低Mach数のPDE前処理：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/low-mach-preconditioning/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
