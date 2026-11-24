# 格子Boltzmann法：衝突、並進、流体運動の回復

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/lattice-boltzmann/

この章に登録された手法・問題・実行例の関連資料です。

## 手法

- [D2Q9–BGK衝突・並進](<https://hrkoyama.github.io/numerical-methods-atlas/methods/d2q9-bgk/?lang=ja>)
- [Guo外力](<https://hrkoyama.github.io/numerical-methods-atlas/methods/guo/?lang=ja>)
- [中間壁バウンスバック](<https://hrkoyama.github.io/numerical-methods-atlas/methods/bounce-back/?lang=ja>)
- [D2Q9–BGK衝突・並進](<https://hrkoyama.github.io/numerical-methods-atlas/methods/d2q9-bgk/?lang=ja>)

  この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。
- [D2Q9–BGK衝突・並進](<https://hrkoyama.github.io/numerical-methods-atlas/methods/d2q9-bgk/?lang=ja>)

  この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。
- [Guo外力](<https://hrkoyama.github.io/numerical-methods-atlas/methods/guo/?lang=ja>)

  この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。
- [中間壁バウンスバック](<https://hrkoyama.github.io/numerical-methods-atlas/methods/bounce-back/?lang=ja>)

  この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

## 方程式

- [等温格子BGK](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bgk-ja>)

  格子単位Δx=Δt=1の衝突・並進更新。D2Q9等温・低Mach数のせん断波とPoiseuille流を扱います。 格子BGKが計算モデル、非圧縮Navier–Stokesは低Mach数で比較する巨視的な減衰モデルです。
- [非圧縮Navier–Stokes](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#navier-stokes-ja>)

  一定密度・粘性の代表形。周期2D MAC射影・Taylor–Green渦に加え、圧力を消去する非周期Re100キャビティを別配布で検証します。 格子BGKが計算モデル、非圧縮Navier–Stokesは低Mach数で比較する巨視的な減衰モデルです。
- [等温格子BGK](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bgk-ja>)

  格子単位Δx=Δt=1の衝突・並進更新。D2Q9等温・低Mach数のせん断波とPoiseuille流を扱います。 格子BGK・体積力・半格子壁を使う計算と、巨視的な定常非圧縮流路解を結びます。
- [非圧縮Navier–Stokes](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#navier-stokes-ja>)

  一定密度・粘性の代表形。周期2D MAC射影・Taylor–Green渦に加え、圧力を消去する非周期Re100キャビティを別配布で検証します。 格子BGK・体積力・半格子壁を使う計算と、巨視的な定常非圧縮流路解を結びます。
- [等温格子BGK](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bgk-ja>)

  格子単位Δx=Δt=1の衝突・並進更新。D2Q9等温・低Mach数のせん断波とPoiseuille流を扱います。

## 問題の図

- [周期せん断波の粘性減衰](<https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-shear/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/lbm-shear.png
- [平行平板Poiseuille流](<https://hrkoyama.github.io/numerical-methods-atlas/problems/channel-poiseuille/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/channel-poiseuille.png

## 厳密解・参照解

- [周期せん断波の粘性減衰：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-shear/?lang=ja#references-ja>)

  低Mach数の周期せん断波について、粘性Fourier減衰から測定した粘性と収束を確認します。熱方程式の参照カードは同型の減衰の関連例です。
- [熱拡散／Fourierモードの減衰](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-sine-heat-ja>)
  relation: related-model
  reference_kind: analytic

  解析解 単位区間の周期境界、拡散係数0.02。 周期せん断速度の線形粘性減衰とスカラー熱モードは同型ですが、LBMの格子単位・波数・粘性と参照カードのν=0.02は異なります。
- [平行平板Poiseuille流：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/channel-poiseuille/?lang=ja#references-ja>)

  半格子bounce-back壁とGuo体積力を使う格子単位の放物線速度が解析基準です。参照解一覧の単位幅・G=1の流路とは駆動力と長さが異なります。
- [粘性チャネル／Poiseuille流](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-poiseuille-ja>)
  relation: related-model
  reference_kind: analytic

  解析解 十分に発達した平面定常チャネル、no-slip、単位密度。−dp/dx=G、または体積力加速度G。 放物線形は共通ですが、計算は格子幅ny・目標最大速度0.01に応じた体積力、カードは単位幅・G=1・ν=0.1です。

## コード・検証

- [LBM Taylor–Green渦：格子・刻み・Machの結合感度](<https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-taylor-green/?lang=ja>)
  availability: run

  周期2Dの非線形渦を実際に時間発展し、連続解析場への速度・圧力・エネルギー誤差を保存します。amplitude感度と同格子のcoupled刻み感度も分けて示します。
- [LBM Re100蓋駆動キャビティ：実2D場とGhia中心線](<https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-cavity-re100/?lang=ja>)
  availability: run

  4壁のBGK更新を3固定格子で実行し、nominal蓋速度で正規化したGhia中心線、主渦、定常性と壁運動量収支を検査します。
- [曲面LBMの環状Couette制御：速度・圧力・torque](<https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-annular-couette-control/?lang=ja>)
  availability: run

  実円弧交点の2次Lagrange補間とstair-halfwayを、回転内壁の解析Navier–Stokes場に比較します。円柱wakeとは別の追加制御です。
- [LBMの実円柱Re20：Schäfer–Turek形状と明示出口](<https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-cylinder-re20/?lang=ja>)
  availability: run

  標準2D-1の全長channelと偏心円柱を実際に発展し、抗力・揚力・表面圧力差・再循環長と定常性を2格子で検査します。
- [D2Q9–BGK衝突・並進：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/d2q9-bgk/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [Guo外力：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/guo/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [中間壁バウンスバック：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/bounce-back/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [周期せん断波の粘性減衰：コード・検証状況](<https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-shear/?lang=ja#code-ja>)
  availability: source

  対応する公開検査と配布版の条件を確認できます。
- [平行平板Poiseuille流：コード・検証状況](<https://hrkoyama.github.io/numerical-methods-atlas/problems/channel-poiseuille/?lang=ja#code-ja>)
  availability: source

  対応する公開検査と配布版の条件を確認できます。
