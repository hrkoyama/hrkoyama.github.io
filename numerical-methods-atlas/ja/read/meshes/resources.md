# 構造格子、非構造格子、三角形格子

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/meshes/

構造・非構造・三角形格子の幾何と接続を確認する展示です。公開ソースと対象を絞った検査を案内し、別章のFEM・ALE・SPHや流体実行例を、この格子展示の方程式・厳密解・PDE検証として継承しません。

## 手法

章固有の対応は未登録です。全体一覧：[手法・コードの対応表](https://hrkoyama.github.io/numerical-methods-atlas/methods/?lang=ja)

## 方程式

章固有の対応は未登録です。全体一覧：[方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja)

## 問題の図

章固有の対応は未登録です。全体一覧：[テスト問題の名前と図](https://hrkoyama.github.io/numerical-methods-atlas/gallery/?lang=ja)

## 厳密解・参照解

章固有の対応は未登録です。全体一覧：[厳密解・参照解](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja)

## コード・検証

- [格子の幾何・接続情報を作るソース](<https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/geometry.py>)
  availability: source

  対応箇所はexample_meshes、mesh_topology、polygon_areaです。構造四角形格子、構造格子を分割した三角形、決定的な不規則点群の三角形分割について、面積と面共有の隣接関係を作ります。共有モジュールにはSPH・移動体積の関数も含まれますが、この対応は格子の幾何と接続に限ります。
- [単位正方形の格子面積・位相・隣接関係の検査](<https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_time_geometry.py>)
  availability: source

  配布版を展開したディレクトリでpython -m pytest -q tests/test_time_geometry.py -k test_mesh_areas_topology_and_neighbors_cover_unit_square。正のセル面積、総面積1、相互の面共有隣接、連結性、V−E+F_cells=1を検査します。同じファイルの時間積分・SPH・ALE検査や、有限要素・非構造流体ソルバーの検証をこの格子検査へ読み替えません。
- [対応する既存の共通配布版 / ZIP](<https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip>)
  availability: source

  上記のソースと検査を含む既存の共通配布版です。展開した配布フォルダで、上記の対象を絞った検査コマンドを実行できます。配布版全体には他章のコードも含まれるため、この章で確認する範囲は各リンクの注記に従います。
