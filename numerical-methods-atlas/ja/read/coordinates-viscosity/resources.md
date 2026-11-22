# 極・円筒座標：テンソルと粘性

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/coordinates-viscosity/

この章に対応するのは、与えた点での円筒座標のテンソル恒等式と解析場の検査です。管内Poiseuille流と円筒Couette流を、参照解一覧の平行平板ケースへ同一問題として結び付けません。対応する独立した問題図・固定入力PDE実行例は登録されていません。

## 手法

章固有の対応は未登録です。全体一覧：[手法・コードの対応表](https://hrkoyama.github.io/numerical-methods-atlas/methods/?lang=ja)

## 方程式

章固有の対応は未登録です。全体一覧：[方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja)

## 問題の図

章固有の対応は未登録です。全体一覧：[テスト問題の名前と図](https://hrkoyama.github.io/numerical-methods-atlas/gallery/?lang=ja)

## 厳密解・参照解

章固有の対応は未登録です。全体一覧：[厳密解・参照解](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja)

## コード・検証

- [円筒座標のテンソル・粘性応力ルーチン](<https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/coordinates.py>)
  availability: source

  r > 0の正規直交基底の物理成分について、速度勾配・Newton粘性応力・応力発散・基底変換を評価するソースです。円筒座標Navier–StokesのPDEソルバー、軸境界処理、球座標実装ではありません。
- [円筒座標の解析場・テンソル恒等式の検査](<https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_coordinates.py>)
  availability: source

  配布版を展開したディレクトリでpython -m pytest -q tests/test_coordinates.py。剛体回転、管内Poiseuille流、円筒Couette流、Cartesianアフィン場との変換、非負散逸、軸・不正入力の拒否を検査します。平行平板の参照解やPDE時間発展の実行例とは区別します。
- [対応する既存の共通配布版 / ZIP](<https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip>)
  availability: source

  上記のソースと検査を含む既存の共通配布版です。展開した配布フォルダで、上記の対象を絞った検査コマンドを実行できます。配布版全体には他章のコードも含まれるため、この章で確認する範囲は各リンクの注記に従います。
