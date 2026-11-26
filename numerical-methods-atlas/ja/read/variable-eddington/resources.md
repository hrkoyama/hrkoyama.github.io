# 可変Eddington因子・テンソル：角度輸送でモーメントを閉じる

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/variable-eddington/

この章に登録された手法・問題・実行例の関連資料です。

## 手法

- [可変Eddington因子（1D VEF）](<https://hrkoyama.github.io/numerical-methods-atlas/methods/variable-eddington-factor/?lang=ja>)
- [可変Eddingtonテンソル（VET）](<https://hrkoyama.github.io/numerical-methods-atlas/methods/variable-eddington-tensor/?lang=ja>)

## 方程式

- [静止灰色輻射のVEF・VETモーメント閉包](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#static-grey-variable-eddington-moments-ja>)

  c=1、角度平均はdΩ/(4π)。1Dのスカラー因子と、2D空間・3D角度の全テンソルを同じモーメント系の変種として扱います。公開例は正の等方輻射源・一定係数・周期境界に限定します。

## 問題の図

章固有の対応は未登録です。全体一覧：[テスト問題の名前と図](https://hrkoyama.github.io/numerical-methods-atlas/gallery/?lang=ja)

## 厳密解・参照解

章固有の対応は未登録です。全体一覧：[厳密解・参照解](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja)

## コード・検証

- [可変エディントン因子：周期1D散乱源の固定検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/vef-fourier-scattering1d/?lang=ja>)
  availability: run

  形式的な角度輸送と独立なモーメント方程式を反復結合し、位置で変わる因子fを閉形式参照と比較します。
- [可変エディントンテンソル：周期2D非平行源の固定検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/vet-fourier-source2d/?lang=ja>)
  availability: run

  非平行な2つの源モードから全S²角度分布と3×3テンソルを求め、Dxyを含む保存的モーメント式と閉形式参照を比較します。
- [可変Eddington因子（1D VEF）：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/variable-eddington-factor/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [可変Eddingtonテンソル（VET）：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/variable-eddington-tensor/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
