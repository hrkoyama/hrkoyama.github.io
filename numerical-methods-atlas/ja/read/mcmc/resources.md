# Markov連鎖Monte Carlo

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/mcmc/

この章に登録された手法・問題・実行例の関連資料です。

## 手法

- [Markov連鎖Monte Carlo](<https://hrkoyama.github.io/numerical-methods-atlas/methods/mcmc/?lang=ja>)

## 方程式

章固有の対応は未登録です。全体一覧：[方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja)

## 問題の図

章固有の対応は未登録です。全体一覧：[テスト問題の名前と図](https://hrkoyama.github.io/numerical-methods-atlas/gallery/?lang=ja)

## 厳密解・参照解

章固有の対応は未登録です。全体一覧：[厳密解・参照解](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja)

## コード・検証

- [Gaussian標的のMCMC：分布・自己相関・ESS](<https://hrkoyama.github.io/numerical-methods-atlas/validation/gaussian-mcmc/?lang=ja>)
  availability: run

  32本のMetropolis連鎖を既知の標準正規分布へ照合し、平均・分散・CDF、自己相関時間、ESSと標本予算依存を記録します。
- [多峰性MCMC：峰への閉じ込め・偽の安心・大域提案](<https://hrkoyama.github.io/numerical-methods-atlas/validation/mcmc-multimodal-mixing/?lang=ja>)
  availability: run

  同じ2峰密度を、分散初期値の局所MH・同じ峰からの局所MH・対称reflectionを混ぜるMHで比較。期待した混合不良の検出と、実際の峰間移動を分けて検証します。
- [Markov連鎖Monte Carlo：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/mcmc/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
