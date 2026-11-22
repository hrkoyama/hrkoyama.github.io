# シンプレクティック積分：正準写像とエネルギーを分ける

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/symplectic/

この章に登録された手法・問題・実行例の関連資料です。

## 手法

- [シンプレクティックEuler法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/symplectic-euler/?lang=ja>)
- [速度Verlet／粒子leapfrog法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/verlet/?lang=ja>)
- [吉田の4次合成法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/yoshida4/?lang=ja>)
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
- [シンプレクティックEuler法：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/symplectic-euler/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [速度Verlet／粒子leapfrog法：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/verlet/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [吉田の4次合成法：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/yoshida4/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
