# 非圧縮流：整合する離散演算子で射影する

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/incompressible/

この章に登録された手法・問題・実行例の関連資料です。

## 手法

- [MAC圧力射影法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/projection/?lang=ja>)
- [MAC圧力射影法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/projection/?lang=ja>)

  この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。
- [D2Q9–BGK衝突・並進](<https://hrkoyama.github.io/numerical-methods-atlas/methods/d2q9-bgk/?lang=ja>)

  この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。

## 方程式

- [非圧縮Navier–Stokes](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#navier-stokes-ja>)

  一定密度・粘性の代表形。周期2D MAC射影・Taylor–Green渦に加え、圧力を消去する非周期Re100キャビティを別配布で検証します。 この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。
- [等温格子BGK](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bgk-ja>)

  格子単位Δx=Δt=1の衝突・並進更新。D2Q9等温・低Mach数のせん断波とPoiseuille流を扱います。 この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。
- [非圧縮Navier–Stokes](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#navier-stokes-ja>)

  一定密度・粘性の代表形。周期2D MAC射影・Taylor–Green渦に加え、圧力を消去する非周期Re100キャビティを別配布で検証します。
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
- [LBMのTaylor–Green渦：格子・時間・Mach数が結び付く感度](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-lbm-taylor-green-ja>)
  relation: related-model
  reference_kind: analytic

  解析解 [0,2pi)²、ν.1、基本U.2、N24/32/64、dt=.2dx²、tau.56、T=.2pi²、144/256/1024steps。N32/U.4,.8とN32/U.2/dt=.1dx²/tau.53/512stepsを追加。初期圧力整合rhoを使用。 [0,2pi)²、ν.1、基本U.2、N24/32/64、dt=.2dx²、tau.56、T=.2pi²、144/256/1024steps。N32/U.4,.8とN32/U.2/dt=.1dx²/tau.53/512stepsを追加。初期圧力整合rhoを使用。
- [周期Taylor–Green渦：速度・散逸・発散：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/taylor-green/?lang=ja#taylor-green-ja-validation>)

  CSVは(i,j)をC順に並べ、u面・v面・圧力中心それぞれの座標、数値解と解析解を別列に保存。MAC速度を同じ位置の成分と誤解しない。JSONにエネルギー履歴と時間感度を保存。
- [粘性流／2次元Taylor–Green渦](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-taylor-green-ja>)
  relation: related-model
  reference_kind: analytic

  解析解 周期領域[0,2π]²、単位密度、動粘性係数0.1、圧力平均ゼロ。Webではy=π/4のx方向断面を表示します。 Taylor–Green：y = π/4のx方向断面です。2次元セル平均ではなく点値を表示します。 同じν=0.1・周期[0,2π]²の解析モデルですが、参照カードはy=π/4のx断面表示です。2次元速度・圧力場や格子誤差の配列とは一致しません。
- [LBMのTaylor–Green渦：格子・時間・Mach数が結び付く感度](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-lbm-taylor-green-ja>)
  relation: related-model
  reference_kind: analytic

  解析解 [0,2pi)²、ν.1、基本U.2、N24/32/64、dt=.2dx²、tau.56、T=.2pi²、144/256/1024steps。N32/U.4,.8とN32/U.2/dt=.1dx²/tau.53/512stepsを追加。初期圧力整合rhoを使用。 [0,2pi)²、ν.1、基本U.2、N24/32/64、dt=.2dx²、tau.56、T=.2pi²、144/256/1024steps。N32/U.4,.8とN32/U.2/dt=.1dx²/tau.53/512stepsを追加。初期圧力整合rhoを使用。

## コード・検証

- [周期Taylor–Green渦：速度・散逸・発散](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/taylor-green/?lang=ja>)
  availability: run

  既存の2次元MAC投影法・中心対流項・明示SSPRK2を使用。16²/32²/64²で解析的減衰渦と比較し、最細格子はCFL半減でも確認。
- [LBM Taylor–Green渦：格子・刻み・Machの結合感度](<https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-taylor-green/?lang=ja>)
  availability: run

  周期2Dの非線形渦を実際に時間発展し、連続解析場への速度・圧力・エネルギー誤差を保存します。amplitude感度と同格子のcoupled刻み感度も分けて示します。
- [MAC圧力射影法：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/projection/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
