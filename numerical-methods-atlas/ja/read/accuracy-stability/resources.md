# A安定性、L安定性、誤差ノルム

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/accuracy-stability/

章で比較する時間積分法と、関連するSDIRK2の硬い余弦追従ODEを案内します。固定入力stiff-cosineの誤差・段階残差・刻み比較は、その条件の実行検証です。A/L安定性の一般的な証明や、列挙した全手法の同一条件での検証を意味しません。誤差ノルムと安定性の役割は分けて読みます。

## 手法

- [前進Euler法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/forward-euler/?lang=ja>)

  章で比較する時間積分法と、関連するSDIRK2の硬い余弦追従ODEを案内します。固定入力stiff-cosineの誤差・段階残差・刻み比較は、その条件の実行検証です。A/L安定性の一般的な証明や、列挙した全手法の同一条件での検証を意味しません。誤差ノルムと安定性の役割は分けて読みます。
- [後退Euler法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/backward-euler/?lang=ja>)

  章で比較する時間積分法と、関連するSDIRK2の硬い余弦追従ODEを案内します。固定入力stiff-cosineの誤差・段階残差・刻み比較は、その条件の実行検証です。A/L安定性の一般的な証明や、列挙した全手法の同一条件での検証を意味しません。誤差ノルムと安定性の役割は分けて読みます。
- [Crank–Nicolson法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/crank-nicolson/?lang=ja>)

  章で比較する時間積分法と、関連するSDIRK2の硬い余弦追従ODEを案内します。固定入力stiff-cosineの誤差・段階残差・刻み比較は、その条件の実行検証です。A/L安定性の一般的な証明や、列挙した全手法の同一条件での検証を意味しません。誤差ノルムと安定性の役割は分けて読みます。
- [陰的中点則](<https://hrkoyama.github.io/numerical-methods-atlas/methods/implicit-midpoint/?lang=ja>)

  章で比較する時間積分法と、関連するSDIRK2の硬い余弦追従ODEを案内します。固定入力stiff-cosineの誤差・段階残差・刻み比較は、その条件の実行検証です。A/L安定性の一般的な証明や、列挙した全手法の同一条件での検証を意味しません。誤差ノルムと安定性の役割は分けて読みます。
- [L安定なSDIRK2](<https://hrkoyama.github.io/numerical-methods-atlas/methods/sdirk2/?lang=ja>)

  章で比較する時間積分法と、関連するSDIRK2の硬い余弦追従ODEを案内します。固定入力stiff-cosineの誤差・段階残差・刻み比較は、その条件の実行検証です。A/L安定性の一般的な証明や、列挙した全手法の同一条件での検証を意味しません。誤差ノルムと安定性の役割は分けて読みます。
- [BDF2](<https://hrkoyama.github.io/numerical-methods-atlas/methods/bdf2/?lang=ja>)

  章で比較する時間積分法と、関連するSDIRK2の硬い余弦追従ODEを案内します。固定入力stiff-cosineの誤差・段階残差・刻み比較は、その条件の実行検証です。A/L安定性の一般的な証明や、列挙した全手法の同一条件での検証を意味しません。誤差ノルムと安定性の役割は分けて読みます。

## 方程式

- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#execution-stiff-cosine-ja>)

  章で比較する時間積分法と、関連するSDIRK2の硬い余弦追従ODEを案内します。固定入力stiff-cosineの誤差・段階残差・刻み比較は、その条件の実行検証です。A/L安定性の一般的な証明や、列挙した全手法の同一条件での検証を意味しません。誤差ノルムと安定性の役割は分けて読みます。 既存2段SDIRK2を使う時間初期値問題。主問題はt=1、1000/2000/4000刻み。46モデル台帳とは別の実行例の式で、熱PDEや汎用硬い系の新規モデルとして数えない。

## 問題の図

- [硬い余弦追従ODE：SDIRK2](<https://hrkoyama.github.io/numerical-methods-atlas/problems/stiff-cosine/?lang=ja>)

  章で比較する時間積分法と、関連するSDIRK2の硬い余弦追従ODEを案内します。固定入力stiff-cosineの誤差・段階残差・刻み比較は、その条件の実行検証です。A/L安定性の一般的な証明や、列挙した全手法の同一条件での検証を意味しません。誤差ノルムと安定性の役割は分けて読みます。 問題の代表図です。固定入力の格子・時刻・初期値とは異なる場合があります。

  https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/stiff-cosine.png

## 厳密解・参照解

- [硬い余弦追従ODE：SDIRK2：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/stiff-cosine/?lang=ja#stiff-cosine-ja-validation>)

  章で比較する時間積分法と、関連するSDIRK2の硬い余弦追従ODEを案内します。固定入力stiff-cosineの誤差・段階残差・刻み比較は、その条件の実行検証です。A/L安定性の一般的な証明や、列挙した全手法の同一条件での検証を意味しません。誤差ノルムと安定性の役割は分けて読みます。 CSVは最細刻みの数値解・解析解・絶対誤差。観測次数は全時刻最大誤差から計算。旧保存例の粗格子で約1台になる挙動と、今回の解像した刻みでの次数を混同しない。

## コード・検証

- [硬い余弦追従ODE：SDIRK2](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/stiff-cosine/?lang=ja>)
  availability: run

  章で比較する時間積分法と、関連するSDIRK2の硬い余弦追従ODEを案内します。固定入力stiff-cosineの誤差・段階残差・刻み比較は、その条件の実行検証です。A/L安定性の一般的な証明や、列挙した全手法の同一条件での検証を意味しません。誤差ノルムと安定性の役割は分けて読みます。 既存のL安定2段SDIRK2でy′=−1000(y−cos t)−sin t、y(0)=1をt=1まで解く。解析解、固定刻み細分化、別の強減衰1段問題を検査。
