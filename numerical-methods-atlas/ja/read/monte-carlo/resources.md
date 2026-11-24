# Monte Carlo積分

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/monte-carlo/

この章に登録された手法・問題・実行例の関連資料です。

## 手法

- [Monte Carlo積分](<https://hrkoyama.github.io/numerical-methods-atlas/methods/monte-carlo/?lang=ja>)
- [Monte Carlo積分](<https://hrkoyama.github.io/numerical-methods-atlas/methods/monte-carlo/?lang=ja>)

  この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。

## 方程式

- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#execution-mc-integral-ja>)

  U[0,1]でx²を積分。256の独立seedで解析積分・分散と比較し、Nの平方根に反比例するRMS誤差と区間被覆を確認。MCMC・希少事象は対象外。

## 問題の図

- [Monte Carlo：256 seedの積分誤差と区間被覆](<https://hrkoyama.github.io/numerical-methods-atlas/problems/mc-integral/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/results/mc-integral/preview.png

## 厳密解・参照解

- [Monte Carlo：256 seedの積分誤差と区間被覆：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/mc-integral/?lang=ja#references-ja>)

  既知の積分値を基準に256 seedの誤差・標準誤差・区間被覆を確認します。個々の乱数軌道の決定論的な解との比較ではありません。
- [Monte Carlo：256 seedの積分誤差と区間被覆：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/mc-integral/?lang=ja#mc-integral-ja-validation>)

  U[0,1]でx²を積分。256の独立seedで解析積分・分散と比較し、Nの平方根に反比例するRMS誤差と区間被覆を確認。MCMC・希少事象は対象外。

## コード・検証

- [Monte Carlo：256 seedの積分誤差と区間被覆](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/mc-integral/?lang=ja>)
  availability: run

  U[0,1]でx²を積分。256の独立seedで解析積分・分散と比較し、Nの平方根に反比例するRMS誤差と区間被覆を確認。MCMC・希少事象は対象外。
- [正規稀少尾の通常importance sampling](<https://hrkoyama.github.io/numerical-methods-atlas/validation/normal-tail-importance/?lang=ja>)
  availability: run

  通常の尤度比平均を解析モーメント・独立seed分散・有限被覆診断で確認。
- [Monte Carlo積分：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/monte-carlo/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [Monte Carlo：256 seedの積分誤差と区間被覆：コード・検証状況](<https://hrkoyama.github.io/numerical-methods-atlas/problems/mc-integral/?lang=ja#code-ja>)
  availability: source

  対応する公開検査と配布版の条件を確認できます。
