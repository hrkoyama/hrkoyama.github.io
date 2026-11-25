# Runge–Kutta法：段数、次数、安定性、SSP

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/runge-kutta/

この章に登録された手法・問題・実行例の関連資料です。

## 手法

- [Dormand–Prince RK45](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rk45/?lang=ja>)
- [前進Euler法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/forward-euler/?lang=ja>)

  公開の全陽的RK tableauに対する非自律・非線形製造解の検査です。保存プレビューはRK4を使います。
- [Heun法／SSPRK(2,2)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=ja>)

  公開の全陽的RK tableauに対する非自律・非線形製造解の検査です。保存プレビューはRK4を使います。
- [陽的中点RK2](<https://hrkoyama.github.io/numerical-methods-atlas/methods/explicit-midpoint/?lang=ja>)

  公開の全陽的RK tableauに対する非自律・非線形製造解の検査です。保存プレビューはRK4を使います。
- [Ralston RK2](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ralston/?lang=ja>)

  公開の全陽的RK tableauに対する非自律・非線形製造解の検査です。保存プレビューはRK4を使います。
- [Kutta RK3](<https://hrkoyama.github.io/numerical-methods-atlas/methods/kutta3/?lang=ja>)

  公開の全陽的RK tableauに対する非自律・非線形製造解の検査です。保存プレビューはRK4を使います。
- [SSPRK(3,3)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk33/?lang=ja>)

  公開の全陽的RK tableauに対する非自律・非線形製造解の検査です。保存プレビューはRK4を使います。
- [SSPRK(4,3)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk43/?lang=ja>)

  公開の全陽的RK tableauに対する非自律・非線形製造解の検査です。保存プレビューはRK4を使います。
- [古典的RK4](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=ja>)

  公開の全陽的RK tableauに対する非自律・非線形製造解の検査です。保存プレビューはRK4を使います。
- [SSPRK(5,4)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk54/?lang=ja>)

  公開の全陽的RK tableauに対する非自律・非線形製造解の検査です。保存プレビューはRK4を使います。
- [前進Euler法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/forward-euler/?lang=ja>)

  この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。
- [Heun法／SSPRK(2,2)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=ja>)

  この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。
- [陽的中点RK2](<https://hrkoyama.github.io/numerical-methods-atlas/methods/explicit-midpoint/?lang=ja>)

  この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。
- [Ralston RK2](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ralston/?lang=ja>)

  この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。
- [Kutta RK3](<https://hrkoyama.github.io/numerical-methods-atlas/methods/kutta3/?lang=ja>)

  この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。
- [SSPRK(3,3)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk33/?lang=ja>)

  この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。
- [SSPRK(4,3)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk43/?lang=ja>)

  この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。
- [古典的RK4](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=ja>)

  この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。
- [SSPRK(5,4)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk54/?lang=ja>)

  この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

## 方程式

章固有の対応は未登録です。全体一覧：[方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja)

## 問題の図

- [指数関数を厳密解に持つ非線形・非自律ODE](<https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-exp-ode/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/nonlinear-exp-ode.png
- [有理減衰ODE（y′ = −y²）](<https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-rational-decay/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/nonlinear-rational-decay.png

## 厳密解・参照解

- [指数関数を厳密解に持つ非線形・非自律ODE：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-exp-ode/?lang=ja#references-ja>)

  非自律非線形方程式y′=-y²+exp(2t)+exp(t)、y(0)=1の製造厳密解y=exp(t)と時間収束を確認します。
- [有理減衰ODE（y′ = −y²）：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-rational-decay/?lang=ja#references-ja>)

  y′=-y²、y(0)=1の厳密解1/(1+t)を使い、複数の陽的Runge–Kutta法の非線形誤差と次数を確認します。

## コード・検証

- [RK45の埋込み推定・補間・イベント](<https://hrkoyama.github.io/numerical-methods-atlas/validation/rk45-dense-events/?lang=ja>)
  availability: run

  減衰回転の解析解を使い、受理/棄却・FSAL・区間内補間・向き付き交差時刻を分けて検査します。
- [Hodgkin–Huxley：電位固定・静止平衡・発火](<https://hrkoyama.github.io/numerical-methods-atlas/validation/hodgkin-huxley-controls/?lang=ja>)
  availability: run

  固定電位の解析ゲート解と、区分電流下の4状態系を照合します。
- [Fisher–KPP：特殊波速の厳密前線](<https://hrkoyama.github.io/numerical-methods-atlas/validation/fisher-kpp-special-front/?lang=ja>)
  availability: run

  波形・位置・格子誤差・時間誤差・有限領域の影響を分けます。
- [Schnakenberg：2D境界と初期モード](<https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-2d-boundary-modes/?lang=ja>)
  availability: run

  2つのNeumann摂動とDirichlet摂動を独立な非線形Galerkin参照と比較します。
- [Keller–Segel：連成流束の製造解](<https://hrkoyama.github.io/numerical-methods-atlas/validation/keller-segel-forced-flux/?lang=ja>)
  availability: run

  滑らかな2D厳密場で、交差流束・段時刻・収支を検証します。
- [Dormand–Prince RK45：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rk45/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [指数関数を厳密解に持つ非線形・非自律ODE：コード・検証状況](<https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-exp-ode/?lang=ja#code-ja>)
  availability: source

  対応する公開検査と配布版の条件を確認できます。
