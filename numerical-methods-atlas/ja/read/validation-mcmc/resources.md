# 多峰性MCMC：混合不良と収束診断の独立検証

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-mcmc/

この章に登録された手法・問題・実行例の関連資料です。

## 手法

- [Markov連鎖Monte Carlo](<https://hrkoyama.github.io/numerical-methods-atlas/methods/mcmc/?lang=ja>)

  この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。
- [Markov連鎖Monte Carlo](<https://hrkoyama.github.io/numerical-methods-atlas/methods/mcmc/?lang=ja>)

## 方程式

- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/mcmc-multimodal-mixing/?lang=ja#mcmc-multimodal-mixing-ja-algorithm>)

  局所幅.8、mixedのみ確率.1でy=−x+.8Z、それ以外y=x+.8Z。混合率は状態非依存でq(y|x)=q(x|y)のため対数標的比でMH判定。各鎖は独立PCG64 stream、提案の適応・棄却の間引きなし。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/mcmc-diagnostic-reference/?lang=ja#mcmc-diagnostic-reference-ja-algorithm>)

  原著式から独自実装。odd長は中央1標本を落としてsplit、平均順位のBlom式は訂正済みS+1/4、fold後再rank、最大Rhatを採用。bulk ESSはrank split、tail ESSは元の全鎖のType7分位点を先に求めた≤indicatorをsplit。Geyer initial-positive/monotoneと宣言した端点処理・tau≥1/log10(total)を用い、反相関ESSをNへclipしません。

## 問題の図

- [多峰性MCMC：峰への閉じ込め・偽の安心・大域提案](<https://hrkoyama.github.io/numerical-methods-atlas/problems/mcmc-bimodal-mixture/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/results/mcmc-multimodal-mixing.png
- [多峰性MCMC：峰への閉じ込め・偽の安心・大域提案](<https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/results/mcmc-multimodal-mixing.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/results/mcmc-multimodal-mixing.png
- [MCMC診断の独立照合：rank Rhat・bulk/tail ESS・退化条件](<https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/results/mcmc-diagnostic-reference.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/results/mcmc-diagnostic-reference.png

## 厳密解・参照解

- [多峰性MCMC：峰への閉じ込め・偽の安心・大域提案：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/mcmc-bimodal-mixture/?lang=ja#references-ja>)

  既知の2峰Gaussian混合の解析的な密度・モーメント・指定点CDF・正側占有と照合し、診断量は独立ArviZ参照で確認します。峰への閉じ込めと多鎖診断の限界を区別し、局所診断の良さを全体混合の保証にしません。
- [多峰性MCMC：峰への閉じ込め・偽の安心・大域提案：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/mcmc-multimodal-mixing/?lang=ja#mcmc-multimodal-mixing-ja-validation>)

  解析平均・分散・CDFの指定7点・正側占有と照合。各鎖の占有率と峰間遷移、rank/folded split Rhat、bulk/tail/mean・modeindicator ESS、鎖内だけのACF/ESSを記録。分散trapped鎖はpooled分布が良くてもRhat/多鎖ESSで失敗、same-mode鎖はRhatが良くても既知標的に失敗する対照です。scenario passはこの期待失敗を検出できた意味です。CDF差は指定点最大でKS全域距離・IID検定p値ではありません。
- [MCMC診断の独立照合：rank Rhat・bulk/tail ESS・退化条件：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/mcmc-diagnostic-reference/?lang=ja#mcmc-diagnostic-reference-ja-validation>)

  実鎖9組×3prefix×x/indicator＋8小fixtureの62組。同じbytesを再生成して照合し、通常の有限値Rhat/ESS/ACFと、定数・鎖内ゼロ分散・odd・ties・shift・scaleを検査。別の直接lag和、定常AR(1)の無限列tau=(1+rho)/(1−rho)で有限推定の誤差も測定します。routineは保存参照との照合で、ArviZのその場再実行は任意の別手順です。

## コード・検証

- [多峰性MCMC：峰への閉じ込め・偽の安心・大域提案](<https://hrkoyama.github.io/numerical-methods-atlas/validation/mcmc-multimodal-mixing/?lang=ja>)
  availability: run

  同じ2峰密度を、分散初期値の局所MH・同じ峰からの局所MH・対称reflectionを混ぜるMHで比較。期待した混合不良の検出と、実際の峰間移動を分けて検証します。
- [MCMC診断の独立照合：rank Rhat・bulk/tail ESS・退化条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/mcmc-diagnostic-reference/?lang=ja>)
  availability: run

  同一鎖の62datasetを別環境ArviZ0.20.0で実計算し、固定recipe・入力・鎖・公式ソースSHAで結びます。通常の有限値照合と、不定値のpolicy差を分けて検査します。
