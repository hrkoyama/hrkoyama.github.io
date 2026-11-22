# Chapman–Enskog展開：分布から輸送へ

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/chapman-enskog/

無外力・等温D2Q9格子BGKの低Mach数・近平衡展開と、周期せん断波から粘性を測る既存の検査を結びます。一般形のBGKカードには外力項も表示されますが、この章が導くのは外力をゼロとした場合です。Guo外力や壁境界を導出・検証する対応ではありません。熱方程式のsine-heat参照は同型の減衰を持つ関連モデルで、格子単位・波数・粘性が異なります。

## 手法

- [D2Q9–BGK衝突・並進](<https://hrkoyama.github.io/numerical-methods-atlas/methods/d2q9-bgk/?lang=ja>)

  無外力・等温D2Q9格子BGKの低Mach数・近平衡展開と、周期せん断波から粘性を測る既存の検査を結びます。一般形のBGKカードには外力項も表示されますが、この章が導くのは外力をゼロとした場合です。Guo外力や壁境界を導出・検証する対応ではありません。熱方程式のsine-heat参照は同型の減衰を持つ関連モデルで、格子単位・波数・粘性が異なります。

## 方程式

- [等温格子BGK](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bgk-ja>)

  無外力・等温D2Q9格子BGKの低Mach数・近平衡展開と、周期せん断波から粘性を測る既存の検査を結びます。一般形のBGKカードには外力項も表示されますが、この章が導くのは外力をゼロとした場合です。Guo外力や壁境界を導出・検証する対応ではありません。熱方程式のsine-heat参照は同型の減衰を持つ関連モデルで、格子単位・波数・粘性が異なります。 格子単位Δx=Δt=1の衝突・並進更新。D2Q9等温・低Mach数のせん断波とPoiseuille流を扱います。

## 問題の図

- [周期せん断波の粘性減衰](<https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-shear/?lang=ja>)

  無外力・等温D2Q9格子BGKの低Mach数・近平衡展開と、周期せん断波から粘性を測る既存の検査を結びます。一般形のBGKカードには外力項も表示されますが、この章が導くのは外力をゼロとした場合です。Guo外力や壁境界を導出・検証する対応ではありません。熱方程式のsine-heat参照は同型の減衰を持つ関連モデルで、格子単位・波数・粘性が異なります。 テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/lbm-shear.png

## 厳密解・参照解

- [周期せん断波の粘性減衰：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-shear/?lang=ja#references-ja>)

  無外力・等温D2Q9格子BGKの低Mach数・近平衡展開と、周期せん断波から粘性を測る既存の検査を結びます。一般形のBGKカードには外力項も表示されますが、この章が導くのは外力をゼロとした場合です。Guo外力や壁境界を導出・検証する対応ではありません。熱方程式のsine-heat参照は同型の減衰を持つ関連モデルで、格子単位・波数・粘性が異なります。 低Mach数の周期せん断波について、粘性Fourier減衰から測定した粘性と収束を確認します。熱方程式の参照カードは同型の減衰の関連例です。
- [熱拡散／Fourierモードの減衰](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-sine-heat-ja>)
  relation: related-model
  reference_kind: analytic

  無外力・等温D2Q9格子BGKの低Mach数・近平衡展開と、周期せん断波から粘性を測る既存の検査を結びます。一般形のBGKカードには外力項も表示されますが、この章が導くのは外力をゼロとした場合です。Guo外力や壁境界を導出・検証する対応ではありません。熱方程式のsine-heat参照は同型の減衰を持つ関連モデルで、格子単位・波数・粘性が異なります。 解析解 単位区間の周期境界、拡散係数0.02。 周期せん断速度の線形粘性減衰とスカラー熱モードは同型ですが、LBMの格子単位・波数・粘性と参照カードのν=0.02は異なります。

## コード・検証

- [周期せん断波の粘性減衰：コード・検証状況](<https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-shear/?lang=ja#code-ja>)
  availability: source

  無外力・等温D2Q9格子BGKの低Mach数・近平衡展開と、周期せん断波から粘性を測る既存の検査を結びます。一般形のBGKカードには外力項も表示されますが、この章が導くのは外力をゼロとした場合です。Guo外力や壁境界を導出・検証する対応ではありません。熱方程式のsine-heat参照は同型の減衰を持つ関連モデルで、格子単位・波数・粘性が異なります。 対応する公開検査と配布版の条件を確認できます。
