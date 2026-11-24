# 重要度サンプリングと相関Gaussian診断

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-stochastic-estimation/

この章に登録された手法・問題・実行例の関連資料です。 重要度重み付き尾確率と2D相関GaussianのMCMCを扱い、解析値・同一データの診断照合・新規標本の検査を区別します。

## 手法

- [Monte Carlo積分](<https://hrkoyama.github.io/numerical-methods-atlas/methods/monte-carlo/?lang=ja>)

  Y=1(X>a)exp(-aX+a²/2)の通常平均。ランダムな重み総和で割らず、proposal調整なし。直接MCの無hitは0のまま保存しCP区間を付けます。
- [Markov連鎖Monte Carlo](<https://hrkoyama.github.io/numerical-methods-atlas/methods/mcmc/?lang=ja>)

  対称random-walk MH、拒否状態も保持。8観測量それぞれのoriginal-scale meanESS/MCSEを計算し、rankbulkESSを流用しません。
- [Monte Carlo積分](<https://hrkoyama.github.io/numerical-methods-atlas/methods/monte-carlo/?lang=ja>)
- [Markov連鎖Monte Carlo](<https://hrkoyama.github.io/numerical-methods-atlas/methods/mcmc/?lang=ja>)

## 方程式

- [Gaussian確率測度：尾確率と相関標的](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#gaussian-probability-model-ja>)

  確率密度と積分のモデル。通常の重要度重みと既知分散の区間、2D相関Gaussianの量別診断を区別し、物理時間発展や一般のMCMC収束保証とは扱いません。 標準正規尾a=3/6、proposal=N(a,1)、64独立seed、N=2048/8192の固定prefix。
- [Gaussian確率測度：尾確率と相関標的](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#gaussian-probability-model-ja>)

  確率密度と積分のモデル。通常の重要度重みと既知分散の区間、2D相関Gaussianの量別診断を区別し、物理時間発展や一般のMCMC収束保証とは扱いません。 平均(1,-1)、相関.95・対角分散1。4独立chainset×4chain、burn1024/draw8192、prefix2048/8192。固定.9Lzと.25z、適応なし。
- [Gaussian確率測度：尾確率と相関標的](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#gaussian-probability-model-ja>)

  確率密度と積分のモデル。通常の重要度重みと既知分散の区間、2D相関Gaussianの量別診断を区別し、物理時間発展や一般のMCMC収束保証とは扱いません。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/normal-tail-importance/?lang=ja#normal-tail-importance-ja-algorithm>)

  Y=1(X>a)exp(-aX+a²/2)の通常平均。ランダムな重み総和で割らず、proposal調整なし。直接MCの無hitは0のまま保存しCP区間を付けます。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/correlated-gaussian-mcmc/?lang=ja#correlated-gaussian-mcmc-ja-algorithm>)

  対称random-walk MH、拒否状態も保持。8観測量それぞれのoriginal-scale meanESS/MCSEを計算し、rankbulkESSを流用しません。

## 問題の図

- [正規稀少尾の通常importance sampling](<https://hrkoyama.github.io/numerical-methods-atlas/problems/normal-tail-importance/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/results/normal-tail-importance-preview.png
- [相関2変量Gaussianのjoint標的とMCSE](<https://hrkoyama.github.io/numerical-methods-atlas/problems/correlated-gaussian-mcmc/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/results/correlated-gaussian-mcmc-preview.png
- [正規稀少尾の通常importance sampling](<https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/results/normal-tail-importance.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/results/normal-tail-importance.png
- [相関2変量Gaussianのjoint標的とMCSE](<https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/results/correlated-gaussian-mcmc.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/results/correlated-gaussian-mcmc.png

## 厳密解・参照解

- [正規稀少尾の通常importance sampling：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/normal-tail-importance/?lang=ja#references-ja>)

  1〜4次モーメントを独立正の積分で資格。既知分散による5SE校正、seed間分散、解析分散低減、重み欠落負例。既知分散normal95%のIS区間の被覆は閾値/prefixごと64反復で別記。
- [正規稀少尾の通常importance sampling](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-normal-tail-importance-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 標準正規尾a=3/6、proposal=N(a,1)、64独立seed、N=2048/8192の固定prefix。 重み付きISへBernoulliの厳密区間を転用しません。64反復は一般95%被覆の証明でなく、nestedprefixを独立反復へ水増ししません。global weightESSと事象ESSは別です。
- [相関2変量Gaussianのjoint標的とMCSE：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/correlated-gaussian-mcmc/?lang=ja#references-ja>)

  4つのpreconditioned最終prefix全観測量にRhat/ESS/MCSE/既知moment条件。同じ128scalararrayを別ArviZ0.20過程へ渡した640値資格と全データSHAで照合。標的は解析Gaussianモーメントで別検査。 640比較は不変な同一データfixture上で行い、別に生成する8組のfresh軌道で物理・混合判定を行います。環境を跨ぐ生成配列のbit一致は要求しません。
- [相関2変量Gaussianのjoint標的とMCSE](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-correlated-gaussian-mcmc-ja>)
  relation: same-problem
  reference_kind: numerical-reference

  有限格子の数値参照 平均(1,-1)、相関.95・対角分散1。4独立chainset×4chain、burn1024/draw8192、prefix2048/8192。固定.9Lzと.25z、適応なし。 診断engineの独立性とsamplerの独立参照を混同しません。Rhat等は大域収束・被覆の証明ではありません。isotropicは固定比較で失敗を要求せず、banana/funnel/HMC/NUTSは未実装です。
- [正規稀少尾の通常importance sampling](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-normal-tail-importance-ja>)
  reference_kind: analytic

  解析解 標準正規尾a=3/6、proposal=N(a,1)、64独立seed、N=2048/8192の固定prefix。
- [相関2変量Gaussianのjoint標的とMCSE](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-correlated-gaussian-mcmc-ja>)
  reference_kind: numerical-reference

  有限格子の数値参照 平均(1,-1)、相関.95・対角分散1。4独立chainset×4chain、burn1024/draw8192、prefix2048/8192。固定.9Lzと.25z、適応なし。
- [正規稀少尾の通常importance sampling：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/normal-tail-importance/?lang=ja#normal-tail-importance-ja-validation>)

  1〜4次モーメントを独立正の積分で資格。既知分散による5SE校正、seed間分散、解析分散低減、重み欠落負例。既知分散normal95%のIS区間の被覆は閾値/prefixごと64反復で別記。
- [正規稀少尾の通常importance sampling](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-normal-tail-importance-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 標準正規尾a=3/6、proposal=N(a,1)、64独立seed、N=2048/8192の固定prefix。 重み付きISへBernoulliの厳密区間を転用しません。64反復は一般95%被覆の証明でなく、nestedprefixを独立反復へ水増ししません。global weightESSと事象ESSは別です。
- [相関2変量Gaussianのjoint標的とMCSE：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/correlated-gaussian-mcmc/?lang=ja#correlated-gaussian-mcmc-ja-validation>)

  4つのpreconditioned最終prefix全観測量にRhat/ESS/MCSE/既知moment条件。同じ128scalararrayを別ArviZ0.20過程へ渡した640値資格と全データSHAで照合。標的は解析Gaussianモーメントで別検査。 640比較は不変な同一データfixture上で行い、別に生成する8組のfresh軌道で物理・混合判定を行います。環境を跨ぐ生成配列のbit一致は要求しません。
- [相関2変量Gaussianのjoint標的とMCSE](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-correlated-gaussian-mcmc-ja>)
  relation: same-problem
  reference_kind: numerical-reference

  有限格子の数値参照 平均(1,-1)、相関.95・対角分散1。4独立chainset×4chain、burn1024/draw8192、prefix2048/8192。固定.9Lzと.25z、適応なし。 診断engineの独立性とsamplerの独立参照を混同しません。Rhat等は大域収束・被覆の証明ではありません。isotropicは固定比較で失敗を要求せず、banana/funnel/HMC/NUTSは未実装です。

## コード・検証

- [正規稀少尾の通常importance sampling](<https://hrkoyama.github.io/numerical-methods-atlas/validation/normal-tail-importance/?lang=ja>)
  availability: run

  通常の尤度比平均を解析モーメント・独立seed分散・有限被覆診断で確認。
- [相関2変量Gaussianのjoint標的とMCSE](<https://hrkoyama.github.io/numerical-methods-atlas/validation/correlated-gaussian-mcmc/?lang=ja>)
  availability: run

  実2D MH軌道を既知のjointモーメントと同一データArviZ診断で検査。
