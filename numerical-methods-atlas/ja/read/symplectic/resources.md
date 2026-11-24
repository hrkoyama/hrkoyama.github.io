# シンプレクティック積分：正準写像とエネルギーを分ける

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/symplectic/

この章に登録された手法・問題・実行例の関連資料です。

## 手法

- [シンプレクティックEuler法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/symplectic-euler/?lang=ja>)
- [速度Verlet／粒子leapfrog法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/verlet/?lang=ja>)
- [吉田の4次合成法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/yoshida4/?lang=ja>)
- [SHAKE拘束積分](<https://hrkoyama.github.io/numerical-methods-atlas/methods/shake/?lang=ja>)
- [RATTLE拘束積分](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rattle/?lang=ja>)
- [シンプレクティックEuler法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/symplectic-euler/?lang=ja>)

  この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。
- [速度Verlet／粒子leapfrog法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/verlet/?lang=ja>)

  この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。
- [吉田の4次合成法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/yoshida4/?lang=ja>)

  この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。
- [陰的中点則](<https://hrkoyama.github.io/numerical-methods-atlas/methods/implicit-midpoint/?lang=ja>)

  この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。
- [古典的RK4](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=ja>)

  この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

## 方程式

- [Hamilton系・振動子](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#hamiltonian-ja>)

  正準方程式と分離可能なHamiltonianの代表形。調和・4次ポテンシャルの振動子で、エネルギー誤差とシンプレクティック性を比べます。 この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。
- [Hamilton系・振動子](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#hamiltonian-ja>)

  正準方程式と分離可能なHamiltonianの代表形。調和・4次ポテンシャルの振動子で、エネルギー誤差とシンプレクティック性を比べます。
- [Kepler二体問題](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#kepler-two-body-ja>)

  無次元化した平面楕円軌道で位相、角運動量、エネルギーと刻みの影響を分けます。
- [二周波数の結合調和振動子](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#coupled-harmonic-oscillators-ja>)

  連続正規モード、理想分割写像、保存した浮動小数点係数の写像、実際の反復丸めを区別します。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#execution-harmonic-oscillator-ja>)

  単位質量・単位角振動数、t=20。速度Verletで200/400/800刻み。時間反転の一致やシンプレクティック性は元のエネルギーの厳密保存を意味しない。

## 問題の図

- [4次ポテンシャルの非線形振動子](<https://hrkoyama.github.io/numerical-methods-atlas/problems/quartic-oscillator/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/quartic-oscillator.png
- [調和振動子：Verletの位相誤差とエネルギー](<https://hrkoyama.github.io/numerical-methods-atlas/problems/harmonic-oscillator/?lang=ja>)

  問題の代表図です。固定入力の格子・時刻・初期値とは異なる場合があります。

  https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/harmonic-oscillator.png

## 厳密解・参照解

- [4次ポテンシャルの非線形振動子：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/quartic-oscillator/?lang=ja#references-ja>)

  非線形ポテンシャルの保存エネルギーと長時間の数値軌道・写像の性質を比較します。保存図を閉形式の厳密軌道と呼びません。
- [調和振動子：Verletの位相誤差とエネルギー：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/harmonic-oscillator/?lang=ja#harmonic-oscillator-ja-validation>)

  CSVは最細刻みの時刻ごとに数値・解析のq,pとエネルギーを整列。観測次数は終端状態誤差から、エネルギー偏差は全保存時刻から計算。

## コード・検証

- [調和振動子：Verletの位相誤差とエネルギー](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/harmonic-oscillator/?lang=ja>)
  availability: run

  既存の単位質量・単位角振動数の調和振動子をvelocity Verletで進める。20時間単位、200/400/800刻みの解析解比較、元のエネルギー偏差、時間反転を出力。
- [PIC空間演算の独立実装照合](<https://hrkoyama.github.io/numerical-methods-atlas/validation/pic-independent-spatial/?lang=ja>)
  availability: run

  ベクトル化CIC/FFTと、別に書いた粒子ループCIC・密なDFTを、それぞれが自己無撞着な場を毎kick計算する軌道全体で照合します。
- [無軟化Kepler二体の時間誤差](<https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-kepler/?lang=ja>)
  availability: run

  非等質量二体をKDKで1周し、独立Kepler方程式の位置・速度とエネルギー/角運動量を照合。
- [離心率を変えたKepler軌道と時間刻み](<https://hrkoyama.github.io/numerical-methods-atlas/validation/kepler-eccentricity/?lang=ja>)
  availability: run

  e=0.1/0.7の16固定軌道で、保存量と同時刻の位相誤差、実際の近日点時刻と逆積分を比較します。
- [冷たいPlummer密度由来32粒子の短時間力学](<https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-plummer-short/?lang=ja>)
  availability: run

  同じ軟化有限N ODEで時間誤差と木近似誤差を分け、独立DOP853・直接力と収支を比較。
- [温かいPICの線形Landau減衰](<https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-landau-damping/?lang=ja>)
  availability: run

  熱速度1のMaxwell分布を自己無撞着に動かし、減衰率・周波数・符号付き場の履歴を独立した線形参照で調べます。
- [温かいPICの二流初期成長](<https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-two-stream/?lang=ja>)
  availability: run

  温度を持つ対向Maxwell二流を時間発展し、固定した線形窓の成長率と過渡を分散式・Volterra参照から分けて検査します。
- [結合した2周波数系と共鳴の有限窓](<https://hrkoyama.github.io/numerical-methods-atlas/validation/multifrequency-resonance/?lang=ja>)
  availability: run

  2自由度の実結合系で、12の64刻みprobeと6の精度軌道を使い、真のモード、座標間交換、離散写像と丸めを分けます。
- [SHAKEとRATTLE：拘束と運動量の違い](<https://hrkoyama.github.io/numerical-methods-atlas/validation/shake-rattle-pendulum/?lang=ja>)
  availability: run

  単振り子の10固定軌道で、位置拘束、全時刻の接線運動量と内部点の中心化運動量を区別します。
- [シンプレクティックEuler法：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/symplectic-euler/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [速度Verlet／粒子leapfrog法：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/verlet/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [吉田の4次合成法：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/yoshida4/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [SHAKE拘束積分：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/shake/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [RATTLE拘束積分：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rattle/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
