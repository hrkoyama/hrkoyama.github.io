# 硬い方程式の積分：段階を解き、時間誤差を制御する

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/stiff-integration/

この章に登録された手法・問題・実行例の関連資料です。

## 手法

- [BDF2](<https://hrkoyama.github.io/numerical-methods-atlas/methods/bdf2/?lang=ja>)
- [L安定なSDIRK2](<https://hrkoyama.github.io/numerical-methods-atlas/methods/sdirk2/?lang=ja>)
- [IMEX Euler](<https://hrkoyama.github.io/numerical-methods-atlas/methods/imex-euler/?lang=ja>)
- [適応SDIRK2／ステップ倍分割](<https://hrkoyama.github.io/numerical-methods-atlas/methods/step-doubling/?lang=ja>)
- [L安定なSDIRK2](<https://hrkoyama.github.io/numerical-methods-atlas/methods/sdirk2/?lang=ja>)

  この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。
- [後退Euler法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/backward-euler/?lang=ja>)

  公開検査に後退Euler・BDF2・SDIRK2・IMEX Eulerがあり、保存プレビューはSDIRK2です。
- [BDF2](<https://hrkoyama.github.io/numerical-methods-atlas/methods/bdf2/?lang=ja>)

  公開検査に後退Euler・BDF2・SDIRK2・IMEX Eulerがあり、保存プレビューはSDIRK2です。
- [L安定なSDIRK2](<https://hrkoyama.github.io/numerical-methods-atlas/methods/sdirk2/?lang=ja>)

  公開検査に後退Euler・BDF2・SDIRK2・IMEX Eulerがあり、保存プレビューはSDIRK2です。
- [IMEX Euler](<https://hrkoyama.github.io/numerical-methods-atlas/methods/imex-euler/?lang=ja>)

  公開検査に後退Euler・BDF2・SDIRK2・IMEX Eulerがあり、保存プレビューはSDIRK2です。

## 方程式

- [Robertson反応系](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#robertson-kinetics-ja>)

  3成分の硬い反応ODEと、保存則を代数式に置き換えたindex-1 DAEを区別して比較します。
- [van der Pol振動子](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#van-der-pol-ja>)

  固定したμと短い時区間で硬さによる仕事量と誤差を比較します。完全な緩和振動周期の検証ではありません。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#execution-stiff-cosine-ja>)

  既存2段SDIRK2を使う時間初期値問題。主問題はt=1、1000/2000/4000刻み。46モデル台帳とは別の実行例の式で、熱PDEや汎用硬い系の新規モデルとして数えない。

## 問題の図

- [硬い余弦追従ODE](<https://hrkoyama.github.io/numerical-methods-atlas/problems/stiff-cosine/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/stiff-cosine.png
- [有理関数を厳密解に持つ非線形・非自律ODE](<https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-rational-ode/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/nonlinear-rational-ode.png

## 厳密解・参照解

- [硬い余弦追従ODE：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/stiff-cosine/?lang=ja#references-ja>)

  y′=-1000(y-cos t)-sin t、y(0)=1の厳密解cos tと、固定刻み・適応刻みの誤差を確認します。
- [有理関数を厳密解に持つ非線形・非自律ODE：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-rational-ode/?lang=ja#references-ja>)

  y′=-y²+sin(t)[y-1/(1+t)]、y(0)=1の製造厳密解1/(1+t)と時間収束を確認します。
- [硬い余弦追従ODE：SDIRK2：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/stiff-cosine/?lang=ja#stiff-cosine-ja-validation>)

  CSVは最細刻みの数値解・解析解・絶対誤差。観測次数は全時刻最大誤差から計算。旧保存例の粗格子で約1台になる挙動と、今回の解像した刻みでの次数を混同しない。

## コード・検証

- [Robertson反応系の初期剛性と実誤差](<https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-stiff-kinetics/?lang=ja>)
  availability: run

  短い固定区間でBDF2・SDIRK2・倍分割適応法を、資格済みRadau/BDF参照と比較します。
- [van der Polの短時間剛性遷移](<https://hrkoyama.github.io/numerical-methods-atlas/validation/van-der-pol-stiff-transition/?lang=ja>)
  availability: run

  局所制御と大域誤差を分離します。初回は元209目標中208達成で、μ=1の厳しい適応設定は大域目標2e-5に未達でした。
- [硬い余弦追従ODE：SDIRK2](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/stiff-cosine/?lang=ja>)
  availability: run

  既存のL安定2段SDIRK2でy′=−1000(y−cos t)−sin t、y(0)=1をt=1まで解く。解析解、固定刻み細分化、別の強減衰1段問題を検査。
- [BDF2：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/bdf2/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [L安定なSDIRK2：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/sdirk2/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [IMEX Euler：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/imex-euler/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [適応SDIRK2／ステップ倍分割：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/step-doubling/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [硬い余弦追従ODE：コード・検証状況](<https://hrkoyama.github.io/numerical-methods-atlas/problems/stiff-cosine/?lang=ja#code-ja>)
  availability: source

  対応する公開検査と配布版の条件を確認できます。
- [有理関数を厳密解に持つ非線形・非自律ODE：コード・検証状況](<https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-rational-ode/?lang=ja#code-ja>)
  availability: source

  対応する公開検査と配布版の条件を確認できます。
