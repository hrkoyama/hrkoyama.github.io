# 非圧縮流：整合する離散演算子で射影する

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/incompressible/

この章に登録された手法・問題・実行例の関連資料です。

## 手法

- [MAC圧力射影法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/projection/?lang=ja>)
- [MAC圧力射影法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/projection/?lang=ja>)

  この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。

## 方程式

- [非圧縮Navier–Stokes](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#navier-stokes-ja>)

  一定密度・粘性の代表形。公開例は周期2次元MAC格子の射影法とTaylor–Green渦です。 この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。
- [非圧縮Navier–Stokes](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#navier-stokes-ja>)

  一定密度・粘性の代表形。公開例は周期2次元MAC格子の射影法とTaylor–Green渦です。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#execution-taylor-green-ja>)

  [0,2π)²周期、t=0.5、16/32/64格子のMAC圧力射影。保存すべき定数エネルギーではなく粘性減衰を調べる。空間と安定刻みの同時細分化と、同一格子の刻み感度を区別する。

## 問題の図

- [周期Taylor–Green渦](<https://hrkoyama.github.io/numerical-methods-atlas/problems/taylor-green/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/numerical-methods-atlas/assets/field-taylor-green.png

## 厳密解・参照解

- [周期Taylor–Green渦：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/taylor-green/?lang=ja#references-ja>)

  2次元周期Taylor–Green渦の速度・圧力の解析解、粘性減衰と離散発散を確認します。参照解一覧の表示はy=π/4の断面であり、2次元計算全体のデータではありません。
- [粘性流／2次元Taylor–Green渦](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-taylor-green-ja>)
  relation: related-model
  reference_kind: analytic

  解析解 周期領域[0,2π]²、単位密度、動粘性係数0.1、圧力平均ゼロ。Webではy=π/4のx方向断面を表示します。 Taylor–Green：y = π/4のx方向断面です。2次元セル平均ではなく点値を表示します。 同じν=0.1・周期[0,2π]²の解析モデルですが、参照カードはy=π/4のx断面表示です。2次元速度・圧力場や格子誤差の配列とは一致しません。
- [周期Taylor–Green渦：速度・散逸・発散：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/taylor-green/?lang=ja#taylor-green-ja-validation>)

  CSVは(i,j)をC順に並べ、u面・v面・圧力中心それぞれの座標、数値解と解析解を別列に保存。MAC速度を同じ位置の成分と誤解しない。JSONにエネルギー履歴と時間感度を保存。
- [粘性流／2次元Taylor–Green渦](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-taylor-green-ja>)
  relation: related-model
  reference_kind: analytic

  解析解 周期領域[0,2π]²、単位密度、動粘性係数0.1、圧力平均ゼロ。Webではy=π/4のx方向断面を表示します。 Taylor–Green：y = π/4のx方向断面です。2次元セル平均ではなく点値を表示します。 同じν=0.1・周期[0,2π]²の解析モデルですが、参照カードはy=π/4のx断面表示です。2次元速度・圧力場や格子誤差の配列とは一致しません。

## コード・検証

- [周期Taylor–Green渦：速度・散逸・発散](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/taylor-green/?lang=ja>)
  availability: run

  既存の2次元MAC投影法・中心対流項・明示SSPRK2を使用。16²/32²/64²で解析的減衰渦と比較し、最細格子はCFL半減でも確認。
- [MAC圧力射影法：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/projection/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
