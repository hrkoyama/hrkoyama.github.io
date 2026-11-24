# 定常多段RKのモード減衰

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-steady-rk/

この章に登録された手法・問題・実行例の関連資料です。 16成分の周期線形場で擬似時間の残差減衰を測り、安定・非減衰・発散の対照を示します。非線形非定常問題の4次精度とは区別します。

## 手法

- [Jameson型の定常多段Runge–Kutta](<https://hrkoyama.github.io/numerical-methods-atlas/methods/jameson-steady-rk/?lang=ja>)

  全段で同じ基底状態を用い、全場・全段残差・評価回数を保存します。
- [Jameson型の定常多段Runge–Kutta](<https://hrkoyama.github.io/numerical-methods-atlas/methods/jameson-steady-rk/?lang=ja>)

## 方程式

- [有限次元の線形発展系](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#linear-evolution-system-ja>)

  減衰回転の物理時刻と、定常残差を減衰させる擬似時間を例ごとに区別します。 無次元の固定16点・周期・線形残差。疑似時間は反復パラメータです。
- [有限次元線形方程式と行列分解](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#finite-dimensional-linear-system-ja>)

  有限行列Aと右辺bの代数問題です。LU/Cholesky・混合精度改良・対称不定値鞍点系を固定例で検査し、連続PDEの解とは区別します。 無次元の固定16点・周期・線形残差。疑似時間は反復パラメータです。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/jameson-steady-linear-modes/?lang=ja#jameson-steady-linear-modes-ja-algorithm>)

  全段で同じ基底状態を用い、全場・全段残差・評価回数を保存します。
- [有限次元の線形発展系](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#linear-evolution-system-ja>)

  減衰回転の物理時刻と、定常残差を減衰させる擬似時間を例ごとに区別します。
- [有限次元線形方程式と行列分解](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#finite-dimensional-linear-system-ja>)

  有限行列Aと右辺bの代数問題です。LU/Cholesky・混合精度改良・対称不定値鞍点系を固定例で検査し、連続PDEの解とは区別します。

## 問題の図

- [定常多段RKの実空間モード減衰](<https://hrkoyama.github.io/numerical-methods-atlas/problems/jameson-steady-linear-modes/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/steady-rk/results/jameson-steady-linear-modes-preview.png
- [定常多段RKの実空間モード減衰](<https://hrkoyama.github.io/code/validated-examples/2026-11-24/steady-rk/results/jameson-steady-linear-modes.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/steady-rk/results/jameson-steady-linear-modes.png

## 厳密解・参照解

- [定常多段RKの実空間モード減衰：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/jameson-steady-linear-modes/?lang=ja#references-ja>)

  元の41数値目標と実際の真偽を変更せず保存します。増幅制御の絶対残差目標だけを研究結果として分離し、他40条件と保存配列からの判定再計算・正確な表示を必須にします。
- [定常多段RKの実空間モード減衰](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-jameson-steady-linear-modes-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 無次元の固定16点・周期・線形残差。疑似時間は反復パラメータです。 固定線形例に限定。JST圧縮性流束や非線形4次RK、任意初期値の収束は検証しません。 元の全数値目標の合格を意味する公開ではありません。
- [定常多段RKの実空間モード減衰](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-jameson-steady-linear-modes-ja>)
  reference_kind: analytic

  解析解 無次元の固定16点・周期・線形残差。疑似時間は反復パラメータです。
- [定常多段RKの実空間モード減衰：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/jameson-steady-linear-modes/?lang=ja#jameson-steady-linear-modes-ja-validation>)

  元の41数値目標と実際の真偽を変更せず保存します。増幅制御の絶対残差目標だけを研究結果として分離し、他40条件と保存配列からの判定再計算・正確な表示を必須にします。
- [定常多段RKの実空間モード減衰](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-jameson-steady-linear-modes-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 無次元の固定16点・周期・線形残差。疑似時間は反復パラメータです。 固定線形例に限定。JST圧縮性流束や非線形4次RK、任意初期値の収束は検証しません。 元の全数値目標の合格を意味する公開ではありません。

## コード・検証

- [定常多段RKの実空間モード減衰](<https://hrkoyama.github.io/numerical-methods-atlas/validation/jameson-steady-linear-modes/?lang=ja>)
  availability: run

  周期格子の実残差に4段定常反復を適用し、離散モードの減衰・中立・増幅を区別します。 初回の増幅制御では元の絶対残差目標が未達でした。
