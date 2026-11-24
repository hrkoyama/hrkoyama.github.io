# LBMのTaylor–Green渦と低Mach誤差

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-lbm-taylor-green/

この章に登録された手法・問題・実行例の関連資料です。 周期渦の解析解を使い、格子・時間刻み・Mach数が結び付く誤差と振幅依存性を調べます。

## 手法

- [D2Q9–BGK衝突・並進](<https://hrkoyama.github.io/numerical-methods-atlas/methods/d2q9-bgk/?lang=ja>)

## 方程式

- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-taylor-green/?lang=ja#lbm-taylor-green-ja-algorithm>)

  標準BGKと完全周期streaming。p=cs²(rho−平均rho)(dx/dt)²で圧力単位とゲージを揃えます。解析場は初期値以外に注入せず、微分を独立Fourier演算で資格確認します。
- [等温格子BGK](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bgk-ja>)

  格子単位Δx=Δt=1の衝突・並進更新。D2Q9等温・低Mach数のせん断波とPoiseuille流を扱います。
- [非圧縮Navier–Stokes](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#navier-stokes-ja>)

  一定密度・粘性の代表形。周期2D MAC射影・Taylor–Green渦に加え、圧力を消去する非周期Re100キャビティを別配布で検証します。

## 問題の図

- [LBM Taylor–Green渦：格子・刻み・Machの結合感度](<https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/results/lbm-taylor-green.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/results/lbm-taylor-green.png
- [周期Taylor–Green渦](<https://hrkoyama.github.io/numerical-methods-atlas/problems/taylor-green/?lang=ja>)

  周期渦の解析解を使い、格子・時間刻み・Mach数が結び付く誤差と振幅依存性を調べます。 テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/numerical-methods-atlas/assets/field-taylor-green.png

## 厳密解・参照解

- [LBMのTaylor–Green渦：格子・時間・Mach数が結び付く感度](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-lbm-taylor-green-ja>)
  reference_kind: analytic

  解析解 [0,2pi)²、ν.1、基本U.2、N24/32/64、dt=.2dx²、tau.56、T=.2pi²、144/256/1024steps。N32/U.4,.8とN32/U.2/dt=.1dx²/tau.53/512stepsを追加。初期圧力整合rhoを使用。
- [LBM Taylor–Green渦：格子・刻み・Machの結合感度：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-taylor-green/?lang=ja#lbm-taylor-green-ja-validation>)

  22pytestと79判定、6固定発展。最細速度相対L2.03、圧力.08、combined速度次数1.5以上、エネルギー.03、発散・周期質量・平均運動量を判定。解析PDE5資格を区別して保存します。 最粗N16の初回エネルギー誤差5.0018%未達を保持し、同じ3%基準へ最粗だけN24へ細分化。次数は最細32/64対だけで評価します。
- [粘性流／2次元Taylor–Green渦](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-taylor-green-ja>)
  relation: related-model
  reference_kind: analytic

  解析解 周期領域[0,2π]²、単位密度、動粘性係数0.1、圧力平均ゼロ。Webではy=π/4のx方向断面を表示します。 Taylor–Green：y = π/4のx方向断面です。2次元セル平均ではなく点値を表示します。 同じν=0.1・周期[0,2π]²の解析モデルですが、参照カードはy=π/4のx断面表示です。2次元速度・圧力場や格子誤差の配列とは一致しません。
- [LBMのTaylor–Green渦：格子・時間・Mach数が結び付く感度](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-lbm-taylor-green-ja>)
  relation: related-model
  reference_kind: analytic

  解析解 [0,2pi)²、ν.1、基本U.2、N24/32/64、dt=.2dx²、tau.56、T=.2pi²、144/256/1024steps。N32/U.4,.8とN32/U.2/dt=.1dx²/tau.53/512stepsを追加。初期圧力整合rhoを使用。 [0,2pi)²、ν.1、基本U.2、N24/32/64、dt=.2dx²、tau.56、T=.2pi²、144/256/1024steps。N32/U.4,.8とN32/U.2/dt=.1dx²/tau.53/512stepsを追加。初期圧力整合rhoを使用。
- [周期Taylor–Green渦：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/taylor-green/?lang=ja#references-ja>)

  周期渦の解析解を使い、格子・時間刻み・Mach数が結び付く誤差と振幅依存性を調べます。 2次元周期Taylor–Green渦の速度・圧力の解析解、粘性減衰と離散発散を確認します。参照解一覧の表示はy=π/4の断面であり、2次元計算全体のデータではありません。
- [粘性流／2次元Taylor–Green渦](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-taylor-green-ja>)
  relation: related-model
  reference_kind: analytic

  周期渦の解析解を使い、格子・時間刻み・Mach数が結び付く誤差と振幅依存性を調べます。 解析解 周期領域[0,2π]²、単位密度、動粘性係数0.1、圧力平均ゼロ。Webではy=π/4のx方向断面を表示します。 Taylor–Green：y = π/4のx方向断面です。2次元セル平均ではなく点値を表示します。 同じν=0.1・周期[0,2π]²の解析モデルですが、参照カードはy=π/4のx断面表示です。2次元速度・圧力場や格子誤差の配列とは一致しません。
- [LBMのTaylor–Green渦：格子・時間・Mach数が結び付く感度](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-lbm-taylor-green-ja>)
  relation: related-model
  reference_kind: analytic

  周期渦の解析解を使い、格子・時間刻み・Mach数が結び付く誤差と振幅依存性を調べます。 解析解 [0,2pi)²、ν.1、基本U.2、N24/32/64、dt=.2dx²、tau.56、T=.2pi²、144/256/1024steps。N32/U.4,.8とN32/U.2/dt=.1dx²/tau.53/512stepsを追加。初期圧力整合rhoを使用。 [0,2pi)²、ν.1、基本U.2、N24/32/64、dt=.2dx²、tau.56、T=.2pi²、144/256/1024steps。N32/U.4,.8とN32/U.2/dt=.1dx²/tau.53/512stepsを追加。初期圧力整合rhoを使用。

## コード・検証

- [LBM Taylor–Green渦：格子・刻み・Machの結合感度](<https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-taylor-green/?lang=ja>)
  availability: run

  周期2Dの非線形渦を実際に時間発展し、連続解析場への速度・圧力・エネルギー誤差を保存します。amplitude感度と同格子のcoupled刻み感度も分けて示します。
