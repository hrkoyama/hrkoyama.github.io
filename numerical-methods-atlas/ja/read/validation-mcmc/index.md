# 多峰性MCMC：混合不良と収束診断の独立検証

二峰性分布で、局所的な閉じ込めと峰間の移動を比べます。自己相関・有効標本数・収束診断の計算を独立実装と照合し、診断値だけでは見逃す探索不足も示します。

共通22実行例の台帳とは別に管理する追加検証集です。配布ZIPを独立展開し、各グループの全固定入力と検査を実行した記録を示します。設定・手法・刻み幅の違いを独立した物理問題の数には加算しません。

## 多峰性MCMC：峰への閉じ込め・偽の安心・大域提案

同じ2峰密度を、分散初期値の局所MH・同じ峰からの局所MH・対称reflectionを混ぜるMHで比較。期待した混合不良の検出と、実際の峰間移動を分けて検証します。

**使用手法**

- [Markov連鎖Monte Carlo](https://hrkoyama.github.io/numerical-methods-atlas/methods/mcmc/?lang=ja) (`mcmc`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/mcmc-multimodal-mixing/?lang=ja#mcmc-multimodal-mixing-ja-algorithm)

局所幅.8、mixedのみ確率.1でy=−x+.8Z、それ以外y=x+.8Z。混合率は状態非依存でq(y|x)=q(x|y)のため対数標的比でMH判定。各鎖は独立PCG64 stream、提案の適応・棄却の間引きなし。

$$
\pi(x)=\tfrac12\phi(x+6)+\tfrac12\phi(x-6),\quad E[X]=0,\quad\operatorname{Var}X=37
$$

$$
F(x)=\tfrac12\Phi(x+6)+\tfrac12\Phi(x-6),\quad P(X>0)=\tfrac12
$$

$$
q(y\mid x)=(1-p)\phi_s(y-x)+p\phi_s(y+x)=q(x\mid y),\quad s=.8,\ p=.1
$$

$$
\alpha(x,y)=\min\{1,\pi(y)/\pi(x)\},\quad I_n=\mathbf1\{X_n>0\}
$$

方程式一覧の対応項目は未登録です。個別の式・近似・診断は上の定義に示します。

**問題の図**

![多峰性MCMC：峰への閉じ込め・偽の安心・大域提案：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/results/mcmc-multimodal-mixing.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[多峰性MCMC：峰への閉じ込め・偽の安心・大域提案](https://hrkoyama.github.io/numerical-methods-atlas/problems/mcmc-bimodal-mixture/?lang=ja) (`mcmc-bimodal-mixture`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/mcmc-bimodal-mixture/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/mcmc-multimodal-mixing/?lang=ja#mcmc-multimodal-mixing-ja-validation)

解析平均・分散・CDFの指定7点・正側占有と照合。各鎖の占有率と峰間遷移、rank/folded split Rhat、bulk/tail/mean・modeindicator ESS、鎖内だけのACF/ESSを記録。分散trapped鎖はpooled分布が良くてもRhat/多鎖ESSで失敗、same-mode鎖はRhatが良くても既知標的に失敗する対照です。scenario passはこの期待失敗を検出できた意味です。CDF差は指定点最大でKS全域距離・IID検定p値ではありません。

参照解一覧の対応カードは未登録です。この実行例の参照値・判定方法は上の検証資料で確認できます。
### 前提・単位・境界

無次元1D標的p=.5N(−6,1)+.5N(6,1)、平均0/分散37/正側占有.5。3固定seed・4鎖、burn1024、保持16384標本/鎖。prefix1024/4096/16384は入れ子で独立再試行ではありません。棄却と自己遷移を保持します。

**編集上の補足**

この検証の「合格」は、混合する系列の分布確認と、意図的に混合しない系列の失敗・診断の盲点を正しく示したことを表します。全系列が収束したという意味ではありません。RhatやESSは観測量・有限標本・初期値に依存し、同じ峰に閉じ込められた全鎖では良く見えることがあります。反射ジャンプは既知の対称性を利用する比較用の提案であり、一般の未知の多峰性を解く保証ではありません。

### 採用した計算法

局所幅.8、mixedのみ確率.1でy=−x+.8Z、それ以外y=x+.8Z。混合率は状態非依存でq(y|x)=q(x|y)のため対数標的比でMH判定。各鎖は独立PCG64 stream、提案の適応・棄却の間引きなし。

$$
\pi(x)=\tfrac12\phi(x+6)+\tfrac12\phi(x-6),\quad E[X]=0,\quad\operatorname{Var}X=37
$$

$$
F(x)=\tfrac12\Phi(x+6)+\tfrac12\Phi(x-6),\quad P(X>0)=\tfrac12
$$

$$
q(y\mid x)=(1-p)\phi_s(y-x)+p\phi_s(y+x)=q(x\mid y),\quad s=.8,\ p=.1
$$

$$
\alpha(x,y)=\min\{1,\pi(y)/\pi(x)\},\quad I_n=\mathbf1\{X_n>0\}
$$

### 比較・検証

解析平均・分散・CDFの指定7点・正側占有と照合。各鎖の占有率と峰間遷移、rank/folded split Rhat、bulk/tail/mean・modeindicator ESS、鎖内だけのACF/ESSを記録。分散trapped鎖はpooled分布が良くてもRhat/多鎖ESSで失敗、same-mode鎖はRhatが良くても既知標的に失敗する対照です。scenario passはこの期待失敗を検出できた意味です。CDF差は指定点最大でKS全域距離・IID検定p値ではありません。

### 確認の限界

固定seed・有限予算の教育用実験です。局所Gaussian RWも理論上は既約なMHであり、有限時間のtrappingを非エルゴードなアルゴリズムとは呼びません。小さいRhat・大きいESS・プールCDFの一致は未発見の峰を除外せず、既知対称性のreflection提案も一般多峰ソルバーではありません。量子計算は追加しません。

### 保存実測値と判定

```json
{
  "metrics": {
    "maximum_fft_direct_acov_error": 7.105427357601002e-15,
    "mixed_maximum_mean_error": 0.1276413989022717,
    "mixed_maximum_variance_error": 0.15417646942373153,
    "mixed_maximum_cdf_error": 0.011283513239714604,
    "mixed_maximum_occupancy_error": 0.010986328125,
    "mixed_maximum_rank_rhat": 1.000848801908244,
    "mixed_minimum_bulk_ess": 6255.350954061888,
    "mixed_minimum_tail_ess": 9814.323360820285,
    "mixed_minimum_mode_ess": 4932.879232093147,
    "mixed_minimum_transitions_per_chain": 1183,
    "intentionally_trapped_scenarios": 6.0
  },
  "checks": {
    "dispersed-2026112251-acceptance": true,
    "dispersed-2026112251-intentionally_trapped": true,
    "dispersed-2026112251-between_chain_failure_detected": true,
    "dispersed-2026112251-mode_variance_failure_explicit": true,
    "dispersed-2026112252-acceptance": true,
    "dispersed-2026112252-intentionally_trapped": true,
    "dispersed-2026112252-between_chain_failure_detected": true,
    "dispersed-2026112252-mode_variance_failure_explicit": true,
    "dispersed-2026112253-acceptance": true,
    "dispersed-2026112253-intentionally_trapped": true,
    "dispersed-2026112253-between_chain_failure_detected": true,
    "dispersed-2026112253-mode_variance_failure_explicit": true,
    "same_mode-2026112251-acceptance": true,
    "same_mode-2026112251-intentionally_trapped": true,
    "same_mode-2026112251-apparently_benign_diagnostics": true,
    "same_mode-2026112251-wrong_target_cdf": true,
    "same_mode-2026112251-wrong_target_mean": true,
    "same_mode-2026112251-wrong_target_occupancy": true,
    "same_mode-2026112251-constant_mode_indicator_undefined": true,
    "same_mode-2026112252-acceptance": true,
    "same_mode-2026112252-intentionally_trapped": true,
    "same_mode-2026112252-apparently_benign_diagnostics": true,
    "same_mode-2026112252-wrong_target_cdf": true,
    "same_mode-2026112252-wrong_target_mean": true,
    "same_mode-2026112252-wrong_target_occupancy": true,
    "same_mode-2026112252-constant_mode_indicator_undefined": true,
    "same_mode-2026112253-acceptance": true,
    "same_mode-2026112253-intentionally_trapped": true,
    "same_mode-2026112253-apparently_benign_diagnostics": true,
    "same_mode-2026112253-wrong_target_cdf": true,
    "same_mode-2026112253-wrong_target_mean": true,
    "same_mode-2026112253-wrong_target_occupancy": true,
    "same_mode-2026112253-constant_mode_indicator_undefined": true,
    "mixed-2026112251-acceptance": true,
    "mixed-2026112251-mean_absolute_error": true,
    "mixed-2026112251-variance_absolute_error": true,
    "mixed-2026112251-cdf_max_error": true,
    "mixed-2026112251-occupancy_absolute_error": true,
    "mixed-2026112251-rank_rhat": true,
    "mixed-2026112251-bulk_ess": true,
    "mixed-2026112251-tail_ess": true,
    "mixed-2026112251-mode_ess": true,
    "mixed-2026112251-per_chain_mode_transitions": true,
    "mixed-2026112252-acceptance": true,
    "mixed-2026112252-mean_absolute_error": true,
    "mixed-2026112252-variance_absolute_error": true,
    "mixed-2026112252-cdf_max_error": true,
    "mixed-2026112252-occupancy_absolute_error": true,
    "mixed-2026112252-rank_rhat": true,
    "mixed-2026112252-bulk_ess": true,
    "mixed-2026112252-tail_ess": true,
    "mixed-2026112252-mode_ess": true,
    "mixed-2026112252-per_chain_mode_transitions": true,
    "mixed-2026112253-acceptance": true,
    "mixed-2026112253-mean_absolute_error": true,
    "mixed-2026112253-variance_absolute_error": true,
    "mixed-2026112253-cdf_max_error": true,
    "mixed-2026112253-occupancy_absolute_error": true,
    "mixed-2026112253-rank_rhat": true,
    "mixed-2026112253-bulk_ess": true,
    "mixed-2026112253-tail_ess": true,
    "mixed-2026112253-mode_ess": true,
    "mixed-2026112253-per_chain_mode_transitions": true,
    "fft_vs_direct_autocovariance": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/mcmc-multimodal-mixing/index.json

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/atlas-mcmc-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

### 出典と確認範囲

- A. Vehtari, A. Gelman, D. Simpson, B. Carpenter and P.-C. Bürkner (2021). Rank-Normalization, Folding, and Localization: An Improved R-hat for Assessing Convergence of MCMC (with Discussion). https://paulbuerkner.com/publications/pdf/2021__Vehtari_et_al__Bayesian_Analysis.pdf; review_level=corrected-author-paper-selected-sections
訂正済み著者公開PDFの第3–4節、式4.1の分母S+1/4への2021-06-22訂正、定数indicatorの注意を確認。原著の全数値実験を再現したものではありません。

- C. J. Geyer (1992). Practical Markov Chain Monte Carlo. https://www2.stat.duke.edu/~scs/Courses/Stat376/Papers/GeyerStatSci1992.pdf; review_level=original-selected-paired-sequence-theory
原著第3.3節・定理3.1/3.2で可逆性等の条件とinitial-positive/monotone列を確認。本論文473–483頁と合本の討論頁を区別。有限鎖から真のESSが厳密に分かる保証とは扱いません。

- A. Gelman and D. B. Rubin (1992). Inference from Iterative Simulation Using Multiple Sequences. https://www2.stat.duke.edu/~scs/Courses/Stat376/Papers/ConvergeDiagnostics/GelmanRubinStatSci1992.pdf; review_level=original-selected-multiple-chain-starting-points
原著の序論・第2節で複数鎖と分散した初期値を確認。現代のrank/folded Rhatの原典とは区別し、1992年版の全有限標本補正の再現とも呼びません。

- The ArviZ developers (2024). ArviZ0.20.0 public diagnostics API and tagged source. https://python.arviz.org/en/v0.20.0/api/generated/arviz.rhat.html; review_level=official-versioned-source-and-actual-independent-execution
公式v0.20.0のrhat/ess API、diagnostics.py/stats_utils.pyでsplit・rank・Type7 quantile・端点・定数規約を確認。commit94113176cae99a05ba41d1e93739ee2d5bdbe9b1と導入ソースSHAを照合し、atlas診断をimportしない別環境で同じ62datasetを実計算。元コード本文は転載せず、参照値・版・hash・再生成コードを同梱します。

- N. Metropolis, A. W. Rosenbluth, M. N. Rosenbluth, A. H. Teller and E. Teller (1953). Equation of State Calculations by Fast Computing Machines. https://doi.org/10.1063/1.1699114; review_level=publisher-abstract-and-metadata
出版社の書誌・抄録を確認。対称提案のMetropolis受理の原著として引用し、硬い球の原著計算を再現したとは扱いません。

- W. K. Hastings (1970). Monte Carlo sampling methods using Markov chains and their applications. https://probability.ca/hastings/hastings.pdf; review_level=original-paper-excerpt-and-metadata
大学で公開された原著の書誌・要約と冒頭を確認。出版社DOIの通常取得はアクセスできませんでした。今回は対称Gaussian提案なので一般の非対称提案比は実装しません。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## MCMC診断の独立照合：rank Rhat・bulk/tail ESS・退化条件

同一鎖の62datasetを別環境ArviZ0.20.0で実計算し、固定recipe・入力・鎖・公式ソースSHAで結びます。通常の有限値照合と、不定値のpolicy差を分けて検査します。

**使用手法**

- [Markov連鎖Monte Carlo](https://hrkoyama.github.io/numerical-methods-atlas/methods/mcmc/?lang=ja) (`mcmc`)

**方程式**

[この実行例の診断式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/mcmc-diagnostic-reference/?lang=ja#mcmc-diagnostic-reference-ja-algorithm)

原著式から独自実装。odd長は中央1標本を落としてsplit、平均順位のBlom式は訂正済みS+1/4、fold後再rank、最大Rhatを採用。bulk ESSはrank split、tail ESSは元の全鎖のType7分位点を先に求めた≤indicatorをsplit。Geyer initial-positive/monotoneと宣言した端点処理・tau≥1/log10(total)を用い、反相関ESSをNへclipしません。

$$
\widehat R=\sqrt{\widehat V^+/W},\quad\widehat V^+=\tfrac{N-1}{N}W+\tfrac BN
$$

$$
z_s=\Phi^{-1}\!\left(\frac{r_s-3/8}{S+1/4}\right),\quad\widehat R_{\rm rank}=\max(\widehat R_z,\widehat R_{\rm folded})
$$

$$
\widehat N_{\rm eff}=MN/\widehat\tau,\quad\widehat\tau=-1+2\sum_k\widehat P_k,\quad\widehat P_k=\widehat\rho_{2k}+\widehat\rho_{2k+1}
$$

$$
\operatorname{ESS}_{\rm tail}=\min\{\operatorname{ESS}(\mathbf1[X\le q_{.05}]),\operatorname{ESS}(\mathbf1[X\le q_{.95}])\}
$$

方程式一覧の対応項目は未登録です。個別の式・近似・診断は上の定義に示します。

**問題の図**

![MCMC診断の独立照合：rank Rhat・bulk/tail ESS・退化条件：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/results/mcmc-diagnostic-reference.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

この検査・診断例には、別の物理テスト問題を割り当てていません。固有の診断図と検証資料を示しています。

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/mcmc-diagnostic-reference/?lang=ja#mcmc-diagnostic-reference-ja-validation)

実鎖9組×3prefix×x/indicator＋8小fixtureの62組。同じbytesを再生成して照合し、通常の有限値Rhat/ESS/ACFと、定数・鎖内ゼロ分散・odd・ties・shift・scaleを検査。別の直接lag和、定常AR(1)の無限列tau=(1+rho)/(1−rho)で有限推定の誤差も測定します。routineは保存参照との照合で、ArviZのその場再実行は任意の別手順です。

参照解一覧の対応カードは未登録です。この実行例の参照値・判定方法は上の検証資料で確認できます。
### 前提・単位・境界

無次元1D標的p=.5N(−6,1)+.5N(6,1)、平均0/分散37/正側占有.5。3固定seed・4鎖、burn1024、保持16384標本/鎖。prefix1024/4096/16384は入れ子で独立再試行ではありません。棄却と自己遷移を保持します。

**編集上の補足**

独立ライブラリとの一致は診断値の計算の照合であり、目標分布を十分探索した証明ではありません。定数や峰指示関数の変動不足は数値のESSへ置き換えず、状態と理由を併記します。負の自己相関ではESSが標本数を超える場合があり、旧Gaussian例の保守的な下限規約とは区別します。

### 採用した計算法

原著式から独自実装。odd長は中央1標本を落としてsplit、平均順位のBlom式は訂正済みS+1/4、fold後再rank、最大Rhatを採用。bulk ESSはrank split、tail ESSは元の全鎖のType7分位点を先に求めた≤indicatorをsplit。Geyer initial-positive/monotoneと宣言した端点処理・tau≥1/log10(total)を用い、反相関ESSをNへclipしません。

$$
\widehat R=\sqrt{\widehat V^+/W},\quad\widehat V^+=\tfrac{N-1}{N}W+\tfrac BN
$$

$$
z_s=\Phi^{-1}\!\left(\frac{r_s-3/8}{S+1/4}\right),\quad\widehat R_{\rm rank}=\max(\widehat R_z,\widehat R_{\rm folded})
$$

$$
\widehat N_{\rm eff}=MN/\widehat\tau,\quad\widehat\tau=-1+2\sum_k\widehat P_k,\quad\widehat P_k=\widehat\rho_{2k}+\widehat\rho_{2k+1}
$$

$$
\operatorname{ESS}_{\rm tail}=\min\{\operatorname{ESS}(\mathbf1[X\le q_{.05}]),\operatorname{ESS}(\mathbf1[X\le q_{.95}])\}
$$

### 比較・検証

実鎖9組×3prefix×x/indicator＋8小fixtureの62組。同じbytesを再生成して照合し、通常の有限値Rhat/ESS/ACFと、定数・鎖内ゼロ分散・odd・ties・shift・scaleを検査。別の直接lag和、定常AR(1)の無限列tau=(1+rho)/(1−rho)で有限推定の誤差も測定します。routineは保存参照との照合で、ArviZのその場再実行は任意の別手順です。

### 確認の限界

固定seed・有限予算の教育用実験です。局所Gaussian RWも理論上は既約なMHであり、有限時間のtrappingを非エルゴードなアルゴリズムとは呼びません。小さいRhat・大きいESS・プールCDFの一致は未発見の峰を除外せず、既知対称性のreflection提案も一般多峰ソルバーではありません。量子計算は追加しません。 定数observableのESS=NというArviZ raw規約を混合の証拠にしません。全同値はnull＋status、鎖ごとに異なる定数のRhatはnull＋infinite-separationとして、ライブラリの巨大finite/infを残し通常有限値の一致点から除外します。bulk ESSは原スケール平均のMCSEへ流用しません。

### 保存実測値と判定

```json
{
  "metrics": {
    "reference_datasets": 62.0,
    "finite_rhat_comparisons": 168,
    "finite_ess_comparisons": 156,
    "global_constant_datasets": 10,
    "global_constant_metric_exclusions": 70,
    "exact_row_rhat_policy_checks": 30,
    "nonfinite_classification_checks": 10,
    "raw_nonfinite_reference_metrics": 62,
    "maximum_rhat_absolute_error": 8.881784197001252e-16,
    "maximum_ess_relative_error": 3.441382313768295e-15,
    "maximum_fft_direct_acov_error": 2.220446049250313e-16,
    "maximum_independent_acf_error": 1.1102230246251565e-16,
    "maximum_ar1_acf_error": 0.010703862071612946,
    "maximum_ar1_tau_relative_error": 0.03641752244252583
  },
  "checks": {
    "dispersed__2026112251__1024__x-rhat_rank": true,
    "dispersed__2026112251__1024__x-rhat_z": true,
    "dispersed__2026112251__1024__x-rhat_folded": true,
    "dispersed__2026112251__1024__x-rhat_split": true,
    "dispersed__2026112251__1024__x-ess_bulk": true,
    "dispersed__2026112251__1024__x-ess_tail": true,
    "dispersed__2026112251__1024__x-ess_mean": true,
    "dispersed__2026112251__1024__x-independent-acf": true,
    "dispersed__2026112251__1024__positive_indicator-rhat_rank-degeneracy-policy": true,
    "dispersed__2026112251__1024__positive_indicator-rhat_z-degeneracy-policy": true,
    "dispersed__2026112251__1024__positive_indicator-rhat_folded": true,
    "dispersed__2026112251__1024__positive_indicator-rhat_split-degeneracy-policy": true,
    "dispersed__2026112251__1024__positive_indicator-ess_bulk": true,
    "dispersed__2026112251__1024__positive_indicator-ess_tail": true,
    "dispersed__2026112251__1024__positive_indicator-ess_mean": true,
    "dispersed__2026112251__4096__x-rhat_rank": true,
    "dispersed__2026112251__4096__x-rhat_z": true,
    "dispersed__2026112251__4096__x-rhat_folded": true,
    "dispersed__2026112251__4096__x-rhat_split": true,
    "dispersed__2026112251__4096__x-ess_bulk": true,
    "dispersed__2026112251__4096__x-ess_tail": true,
    "dispersed__2026112251__4096__x-ess_mean": true,
    "dispersed__2026112251__4096__x-independent-acf": true,
    "dispersed__2026112251__4096__positive_indicator-rhat_rank-degeneracy-policy": true,
    "dispersed__2026112251__4096__positive_indicator-rhat_z-degeneracy-policy": true,
    "dispersed__2026112251__4096__positive_indicator-rhat_folded": true,
    "dispersed__2026112251__4096__positive_indicator-rhat_split-degeneracy-policy": true,
    "dispersed__2026112251__4096__positive_indicator-ess_bulk": true,
    "dispersed__2026112251__4096__positive_indicator-ess_tail": true,
    "dispersed__2026112251__4096__positive_indicator-ess_mean": true,
    "dispersed__2026112251__16384__x-rhat_rank": true,
    "dispersed__2026112251__16384__x-rhat_z": true,
    "dispersed__2026112251__16384__x-rhat_folded": true,
    "dispersed__2026112251__16384__x-rhat_split": true,
    "dispersed__2026112251__16384__x-ess_bulk": true,
    "dispersed__2026112251__16384__x-ess_tail": true,
    "dispersed__2026112251__16384__x-ess_mean": true,
    "dispersed__2026112251__16384__x-independent-acf": true,
    "dispersed__2026112251__16384__positive_indicator-rhat_rank-degeneracy-policy": true,
    "dispersed__2026112251__16384__positive_indicator-rhat_z-degeneracy-policy": true,
    "dispersed__2026112251__16384__positive_indicator-rhat_folded": true,
    "dispersed__2026112251__16384__positive_indicator-rhat_split-degeneracy-policy": true,
    "dispersed__2026112251__16384__positive_indicator-ess_bulk": true,
    "dispersed__2026112251__16384__positive_indicator-ess_tail": true,
    "dispersed__2026112251__16384__positive_indicator-ess_mean": true,
    "dispersed__2026112252__1024__x-rhat_rank": true,
    "dispersed__2026112252__1024__x-rhat_z": true,
    "dispersed__2026112252__1024__x-rhat_folded": true,
    "dispersed__2026112252__1024__x-rhat_split": true,
    "dispersed__2026112252__1024__x-ess_bulk": true,
    "dispersed__2026112252__1024__x-ess_tail": true,
    "dispersed__2026112252__1024__x-ess_mean": true,
    "dispersed__2026112252__1024__x-independent-acf": true,
    "dispersed__2026112252__1024__positive_indicator-rhat_rank-degeneracy-policy": true,
    "dispersed__2026112252__1024__positive_indicator-rhat_z-degeneracy-policy": true,
    "dispersed__2026112252__1024__positive_indicator-rhat_folded": true,
    "dispersed__2026112252__1024__positive_indicator-rhat_split-degeneracy-policy": true,
    "dispersed__2026112252__1024__positive_indicator-ess_bulk": true,
    "dispersed__2026112252__1024__positive_indicator-ess_tail": true,
    "dispersed__2026112252__1024__positive_indicator-ess_mean": true,
    "dispersed__2026112252__4096__x-rhat_rank": true,
    "dispersed__2026112252__4096__x-rhat_z": true,
    "dispersed__2026112252__4096__x-rhat_folded": true,
    "dispersed__2026112252__4096__x-rhat_split": true,
    "dispersed__2026112252__4096__x-ess_bulk": true,
    "dispersed__2026112252__4096__x-ess_tail": true,
    "dispersed__2026112252__4096__x-ess_mean": true,
    "dispersed__2026112252__4096__x-independent-acf": true,
    "dispersed__2026112252__4096__positive_indicator-rhat_rank-degeneracy-policy": true,
    "dispersed__2026112252__4096__positive_indicator-rhat_z-degeneracy-policy": true,
    "dispersed__2026112252__4096__positive_indicator-rhat_folded": true,
    "dispersed__2026112252__4096__positive_indicator-rhat_split-degeneracy-policy": true,
    "dispersed__2026112252__4096__positive_indicator-ess_bulk": true,
    "dispersed__2026112252__4096__positive_indicator-ess_tail": true,
    "dispersed__2026112252__4096__positive_indicator-ess_mean": true,
    "dispersed__2026112252__16384__x-rhat_rank": true,
    "dispersed__2026112252__16384__x-rhat_z": true,
    "dispersed__2026112252__16384__x-rhat_folded": true,
    "dispersed__2026112252__16384__x-rhat_split": true,
    "dispersed__2026112252__16384__x-ess_bulk": true,
    "dispersed__2026112252__16384__x-ess_tail": true,
    "dispersed__2026112252__16384__x-ess_mean": true,
    "dispersed__2026112252__16384__x-independent-acf": true,
    "dispersed__2026112252__16384__positive_indicator-rhat_rank-degeneracy-policy": true,
    "dispersed__2026112252__16384__positive_indicator-rhat_z-degeneracy-policy": true,
    "dispersed__2026112252__16384__positive_indicator-rhat_folded": true,
    "dispersed__2026112252__16384__positive_indicator-rhat_split-degeneracy-policy": true,
    "dispersed__2026112252__16384__positive_indicator-ess_bulk": true,
    "dispersed__2026112252__16384__positive_indicator-ess_tail": true,
    "dispersed__2026112252__16384__positive_indicator-ess_mean": true,
    "dispersed__2026112253__1024__x-rhat_rank": true,
    "dispersed__2026112253__1024__x-rhat_z": true,
    "dispersed__2026112253__1024__x-rhat_folded": true,
    "dispersed__2026112253__1024__x-rhat_split": true,
    "dispersed__2026112253__1024__x-ess_bulk": true,
    "dispersed__2026112253__1024__x-ess_tail": true,
    "dispersed__2026112253__1024__x-ess_mean": true,
    "dispersed__2026112253__1024__x-independent-acf": true,
    "dispersed__2026112253__1024__positive_indicator-rhat_rank-degeneracy-policy": true,
    "dispersed__2026112253__1024__positive_indicator-rhat_z-degeneracy-policy": true,
    "dispersed__2026112253__1024__positive_indicator-rhat_folded": true,
    "dispersed__2026112253__1024__positive_indicator-rhat_split-degeneracy-policy": true,
    "dispersed__2026112253__1024__positive_indicator-ess_bulk": true,
    "dispersed__2026112253__1024__positive_indicator-ess_tail": true,
    "dispersed__2026112253__1024__positive_indicator-ess_mean": true,
    "dispersed__2026112253__4096__x-rhat_rank": true,
    "dispersed__2026112253__4096__x-rhat_z": true,
    "dispersed__2026112253__4096__x-rhat_folded": true,
    "dispersed__2026112253__4096__x-rhat_split": true,
    "dispersed__2026112253__4096__x-ess_bulk": true,
    "dispersed__2026112253__4096__x-ess_tail": true,
    "dispersed__2026112253__4096__x-ess_mean": true,
    "dispersed__2026112253__4096__x-independent-acf": true,
    "dispersed__2026112253__4096__positive_indicator-rhat_rank-degeneracy-policy": true,
    "dispersed__2026112253__4096__positive_indicator-rhat_z-degeneracy-policy": true,
    "dispersed__2026112253__4096__positive_indicator-rhat_folded": true,
    "dispersed__2026112253__4096__positive_indicator-rhat_split-degeneracy-policy": true,
    "dispersed__2026112253__4096__positive_indicator-ess_bulk": true,
    "dispersed__2026112253__4096__positive_indicator-ess_tail": true,
    "dispersed__2026112253__4096__positive_indicator-ess_mean": true,
    "dispersed__2026112253__16384__x-rhat_rank": true,
    "dispersed__2026112253__16384__x-rhat_z": true,
    "dispersed__2026112253__16384__x-rhat_folded": true,
    "dispersed__2026112253__16384__x-rhat_split": true,
    "dispersed__2026112253__16384__x-ess_bulk": true,
    "dispersed__2026112253__16384__x-ess_tail": true,
    "dispersed__2026112253__16384__x-ess_mean": true,
    "dispersed__2026112253__16384__x-independent-acf": true,
    "dispersed__2026112253__16384__positive_indicator-rhat_rank-degeneracy-policy": true,
    "dispersed__2026112253__16384__positive_indicator-rhat_z-degeneracy-policy": true,
    "dispersed__2026112253__16384__positive_indicator-rhat_folded": true,
    "dispersed__2026112253__16384__positive_indicator-rhat_split-degeneracy-policy": true,
    "dispersed__2026112253__16384__positive_indicator-ess_bulk": true,
    "dispersed__2026112253__16384__positive_indicator-ess_tail": true,
    "dispersed__2026112253__16384__positive_indicator-ess_mean": true,
    "same_mode__2026112251__1024__x-rhat_rank": true,
    "same_mode__2026112251__1024__x-rhat_z": true,
    "same_mode__2026112251__1024__x-rhat_folded": true,
    "same_mode__2026112251__1024__x-rhat_split": true,
    "same_mode__2026112251__1024__x-ess_bulk": true,
    "same_mode__2026112251__1024__x-ess_tail": true,
    "same_mode__2026112251__1024__x-ess_mean": true,
    "same_mode__2026112251__1024__x-independent-acf": true,
    "same_mode__2026112251__1024__positive_indicator-constant-undefined": true,
    "same_mode__2026112251__4096__x-rhat_rank": true,
    "same_mode__2026112251__4096__x-rhat_z": true,
    "same_mode__2026112251__4096__x-rhat_folded": true,
    "same_mode__2026112251__4096__x-rhat_split": true,
    "same_mode__2026112251__4096__x-ess_bulk": true,
    "same_mode__2026112251__4096__x-ess_tail": true,
    "same_mode__2026112251__4096__x-ess_mean": true,
    "same_mode__2026112251__4096__x-independent-acf": true,
    "same_mode__2026112251__4096__positive_indicator-constant-undefined": true,
    "same_mode__2026112251__16384__x-rhat_rank": true,
    "same_mode__2026112251__16384__x-rhat_z": true,
    "same_mode__2026112251__16384__x-rhat_folded": true,
    "same_mode__2026112251__16384__x-rhat_split": true,
    "same_mode__2026112251__16384__x-ess_bulk": true,
    "same_mode__2026112251__16384__x-ess_tail": true,
    "same_mode__2026112251__16384__x-ess_mean": true,
    "same_mode__2026112251__16384__x-independent-acf": true,
    "same_mode__2026112251__16384__positive_indicator-constant-undefined": true,
    "same_mode__2026112252__1024__x-rhat_rank": true,
    "same_mode__2026112252__1024__x-rhat_z": true,
    "same_mode__2026112252__1024__x-rhat_folded": true,
    "same_mode__2026112252__1024__x-rhat_split": true,
    "same_mode__2026112252__1024__x-ess_bulk": true,
    "same_mode__2026112252__1024__x-ess_tail": true,
    "same_mode__2026112252__1024__x-ess_mean": true,
    "same_mode__2026112252__1024__x-independent-acf": true,
    "same_mode__2026112252__1024__positive_indicator-constant-undefined": true,
    "same_mode__2026112252__4096__x-rhat_rank": true,
    "same_mode__2026112252__4096__x-rhat_z": true,
    "same_mode__2026112252__4096__x-rhat_folded": true,
    "same_mode__2026112252__4096__x-rhat_split": true,
    "same_mode__2026112252__4096__x-ess_bulk": true,
    "same_mode__2026112252__4096__x-ess_tail": true,
    "same_mode__2026112252__4096__x-ess_mean": true,
    "same_mode__2026112252__4096__x-independent-acf": true,
    "same_mode__2026112252__4096__positive_indicator-constant-undefined": true,
    "same_mode__2026112252__16384__x-rhat_rank": true,
    "same_mode__2026112252__16384__x-rhat_z": true,
    "same_mode__2026112252__16384__x-rhat_folded": true,
    "same_mode__2026112252__16384__x-rhat_split": true,
    "same_mode__2026112252__16384__x-ess_bulk": true,
    "same_mode__2026112252__16384__x-ess_tail": true,
    "same_mode__2026112252__16384__x-ess_mean": true,
    "same_mode__2026112252__16384__x-independent-acf": true,
    "same_mode__2026112252__16384__positive_indicator-constant-undefined": true,
    "same_mode__2026112253__1024__x-rhat_rank": true,
    "same_mode__2026112253__1024__x-rhat_z": true,
    "same_mode__2026112253__1024__x-rhat_folded": true,
    "same_mode__2026112253__1024__x-rhat_split": true,
    "same_mode__2026112253__1024__x-ess_bulk": true,
    "same_mode__2026112253__1024__x-ess_tail": true,
    "same_mode__2026112253__1024__x-ess_mean": true,
    "same_mode__2026112253__1024__x-independent-acf": true,
    "same_mode__2026112253__1024__positive_indicator-constant-undefined": true,
    "same_mode__2026112253__4096__x-rhat_rank": true,
    "same_mode__2026112253__4096__x-rhat_z": true,
    "same_mode__2026112253__4096__x-rhat_folded": true,
    "same_mode__2026112253__4096__x-rhat_split": true,
    "same_mode__2026112253__4096__x-ess_bulk": true,
    "same_mode__2026112253__4096__x-ess_tail": true,
    "same_mode__2026112253__4096__x-ess_mean": true,
    "same_mode__2026112253__4096__x-independent-acf": true,
    "same_mode__2026112253__4096__positive_indicator-constant-undefined": true,
    "same_mode__2026112253__16384__x-rhat_rank": true,
    "same_mode__2026112253__16384__x-rhat_z": true,
    "same_mode__2026112253__16384__x-rhat_folded": true,
    "same_mode__2026112253__16384__x-rhat_split": true,
    "same_mode__2026112253__16384__x-ess_bulk": true,
    "same_mode__2026112253__16384__x-ess_tail": true,
    "same_mode__2026112253__16384__x-ess_mean": true,
    "same_mode__2026112253__16384__x-independent-acf": true,
    "same_mode__2026112253__16384__positive_indicator-constant-undefined": true,
    "mixed__2026112251__1024__x-rhat_rank": true,
    "mixed__2026112251__1024__x-rhat_z": true,
    "mixed__2026112251__1024__x-rhat_folded": true,
    "mixed__2026112251__1024__x-rhat_split": true,
    "mixed__2026112251__1024__x-ess_bulk": true,
    "mixed__2026112251__1024__x-ess_tail": true,
    "mixed__2026112251__1024__x-ess_mean": true,
    "mixed__2026112251__1024__x-independent-acf": true,
    "mixed__2026112251__1024__positive_indicator-rhat_rank": true,
    "mixed__2026112251__1024__positive_indicator-rhat_z": true,
    "mixed__2026112251__1024__positive_indicator-rhat_folded": true,
    "mixed__2026112251__1024__positive_indicator-rhat_split": true,
    "mixed__2026112251__1024__positive_indicator-ess_bulk": true,
    "mixed__2026112251__1024__positive_indicator-ess_tail": true,
    "mixed__2026112251__1024__positive_indicator-ess_mean": true,
    "mixed__2026112251__1024__positive_indicator-independent-acf": true,
    "mixed__2026112251__4096__x-rhat_rank": true,
    "mixed__2026112251__4096__x-rhat_z": true,
    "mixed__2026112251__4096__x-rhat_folded": true,
    "mixed__2026112251__4096__x-rhat_split": true,
    "mixed__2026112251__4096__x-ess_bulk": true,
    "mixed__2026112251__4096__x-ess_tail": true,
    "mixed__2026112251__4096__x-ess_mean": true,
    "mixed__2026112251__4096__x-independent-acf": true,
    "mixed__2026112251__4096__positive_indicator-rhat_rank": true,
    "mixed__2026112251__4096__positive_indicator-rhat_z": true,
    "mixed__2026112251__4096__positive_indicator-rhat_folded": true,
    "mixed__2026112251__4096__positive_indicator-rhat_split": true,
    "mixed__2026112251__4096__positive_indicator-ess_bulk": true,
    "mixed__2026112251__4096__positive_indicator-ess_tail": true,
    "mixed__2026112251__4096__positive_indicator-ess_mean": true,
    "mixed__2026112251__4096__positive_indicator-independent-acf": true,
    "mixed__2026112251__16384__x-rhat_rank": true,
    "mixed__2026112251__16384__x-rhat_z": true,
    "mixed__2026112251__16384__x-rhat_folded": true,
    "mixed__2026112251__16384__x-rhat_split": true,
    "mixed__2026112251__16384__x-ess_bulk": true,
    "mixed__2026112251__16384__x-ess_tail": true,
    "mixed__2026112251__16384__x-ess_mean": true,
    "mixed__2026112251__16384__x-independent-acf": true,
    "mixed__2026112251__16384__positive_indicator-rhat_rank": true,
    "mixed__2026112251__16384__positive_indicator-rhat_z": true,
    "mixed__2026112251__16384__positive_indicator-rhat_folded": true,
    "mixed__2026112251__16384__positive_indicator-rhat_split": true,
    "mixed__2026112251__16384__positive_indicator-ess_bulk": true,
    "mixed__2026112251__16384__positive_indicator-ess_tail": true,
    "mixed__2026112251__16384__positive_indicator-ess_mean": true,
    "mixed__2026112251__16384__positive_indicator-independent-acf": true,
    "mixed__2026112252__1024__x-rhat_rank": true,
    "mixed__2026112252__1024__x-rhat_z": true,
    "mixed__2026112252__1024__x-rhat_folded": true,
    "mixed__2026112252__1024__x-rhat_split": true,
    "mixed__2026112252__1024__x-ess_bulk": true,
    "mixed__2026112252__1024__x-ess_tail": true,
    "mixed__2026112252__1024__x-ess_mean": true,
    "mixed__2026112252__1024__x-independent-acf": true,
    "mixed__2026112252__1024__positive_indicator-rhat_rank": true,
    "mixed__2026112252__1024__positive_indicator-rhat_z": true,
    "mixed__2026112252__1024__positive_indicator-rhat_folded": true,
    "mixed__2026112252__1024__positive_indicator-rhat_split": true,
    "mixed__2026112252__1024__positive_indicator-ess_bulk": true,
    "mixed__2026112252__1024__positive_indicator-ess_tail": true,
    "mixed__2026112252__1024__positive_indicator-ess_mean": true,
    "mixed__2026112252__1024__positive_indicator-independent-acf": true,
    "mixed__2026112252__4096__x-rhat_rank": true,
    "mixed__2026112252__4096__x-rhat_z": true,
    "mixed__2026112252__4096__x-rhat_folded": true,
    "mixed__2026112252__4096__x-rhat_split": true,
    "mixed__2026112252__4096__x-ess_bulk": true,
    "mixed__2026112252__4096__x-ess_tail": true,
    "mixed__2026112252__4096__x-ess_mean": true,
    "mixed__2026112252__4096__x-independent-acf": true,
    "mixed__2026112252__4096__positive_indicator-rhat_rank": true,
    "mixed__2026112252__4096__positive_indicator-rhat_z": true,
    "mixed__2026112252__4096__positive_indicator-rhat_folded": true,
    "mixed__2026112252__4096__positive_indicator-rhat_split": true,
    "mixed__2026112252__4096__positive_indicator-ess_bulk": true,
    "mixed__2026112252__4096__positive_indicator-ess_tail": true,
    "mixed__2026112252__4096__positive_indicator-ess_mean": true,
    "mixed__2026112252__4096__positive_indicator-independent-acf": true,
    "mixed__2026112252__16384__x-rhat_rank": true,
    "mixed__2026112252__16384__x-rhat_z": true,
    "mixed__2026112252__16384__x-rhat_folded": true,
    "mixed__2026112252__16384__x-rhat_split": true,
    "mixed__2026112252__16384__x-ess_bulk": true,
    "mixed__2026112252__16384__x-ess_tail": true,
    "mixed__2026112252__16384__x-ess_mean": true,
    "mixed__2026112252__16384__x-independent-acf": true,
    "mixed__2026112252__16384__positive_indicator-rhat_rank": true,
    "mixed__2026112252__16384__positive_indicator-rhat_z": true,
    "mixed__2026112252__16384__positive_indicator-rhat_folded": true,
    "mixed__2026112252__16384__positive_indicator-rhat_split": true,
    "mixed__2026112252__16384__positive_indicator-ess_bulk": true,
    "mixed__2026112252__16384__positive_indicator-ess_tail": true,
    "mixed__2026112252__16384__positive_indicator-ess_mean": true,
    "mixed__2026112252__16384__positive_indicator-independent-acf": true,
    "mixed__2026112253__1024__x-rhat_rank": true,
    "mixed__2026112253__1024__x-rhat_z": true,
    "mixed__2026112253__1024__x-rhat_folded": true,
    "mixed__2026112253__1024__x-rhat_split": true,
    "mixed__2026112253__1024__x-ess_bulk": true,
    "mixed__2026112253__1024__x-ess_tail": true,
    "mixed__2026112253__1024__x-ess_mean": true,
    "mixed__2026112253__1024__x-independent-acf": true,
    "mixed__2026112253__1024__positive_indicator-rhat_rank": true,
    "mixed__2026112253__1024__positive_indicator-rhat_z": true,
    "mixed__2026112253__1024__positive_indicator-rhat_folded": true,
    "mixed__2026112253__1024__positive_indicator-rhat_split": true,
    "mixed__2026112253__1024__positive_indicator-ess_bulk": true,
    "mixed__2026112253__1024__positive_indicator-ess_tail": true,
    "mixed__2026112253__1024__positive_indicator-ess_mean": true,
    "mixed__2026112253__1024__positive_indicator-independent-acf": true,
    "mixed__2026112253__4096__x-rhat_rank": true,
    "mixed__2026112253__4096__x-rhat_z": true,
    "mixed__2026112253__4096__x-rhat_folded": true,
    "mixed__2026112253__4096__x-rhat_split": true,
    "mixed__2026112253__4096__x-ess_bulk": true,
    "mixed__2026112253__4096__x-ess_tail": true,
    "mixed__2026112253__4096__x-ess_mean": true,
    "mixed__2026112253__4096__x-independent-acf": true,
    "mixed__2026112253__4096__positive_indicator-rhat_rank": true,
    "mixed__2026112253__4096__positive_indicator-rhat_z": true,
    "mixed__2026112253__4096__positive_indicator-rhat_folded": true,
    "mixed__2026112253__4096__positive_indicator-rhat_split": true,
    "mixed__2026112253__4096__positive_indicator-ess_bulk": true,
    "mixed__2026112253__4096__positive_indicator-ess_tail": true,
    "mixed__2026112253__4096__positive_indicator-ess_mean": true,
    "mixed__2026112253__4096__positive_indicator-independent-acf": true,
    "mixed__2026112253__16384__x-rhat_rank": true,
    "mixed__2026112253__16384__x-rhat_z": true,
    "mixed__2026112253__16384__x-rhat_folded": true,
    "mixed__2026112253__16384__x-rhat_split": true,
    "mixed__2026112253__16384__x-ess_bulk": true,
    "mixed__2026112253__16384__x-ess_tail": true,
    "mixed__2026112253__16384__x-ess_mean": true,
    "mixed__2026112253__16384__x-independent-acf": true,
    "mixed__2026112253__16384__positive_indicator-rhat_rank": true,
    "mixed__2026112253__16384__positive_indicator-rhat_z": true,
    "mixed__2026112253__16384__positive_indicator-rhat_folded": true,
    "mixed__2026112253__16384__positive_indicator-rhat_split": true,
    "mixed__2026112253__16384__positive_indicator-ess_bulk": true,
    "mixed__2026112253__16384__positive_indicator-ess_tail": true,
    "mixed__2026112253__16384__positive_indicator-ess_mean": true,
    "mixed__2026112253__16384__positive_indicator-independent-acf": true,
    "edge__iid-rhat_rank": true,
    "edge__iid-rhat_z": true,
    "edge__iid-rhat_folded": true,
    "edge__iid-rhat_split": true,
    "edge__iid-ess_bulk": true,
    "edge__iid-ess_tail": true,
    "edge__iid-ess_mean": true,
    "edge__iid-independent-acf": true,
    "edge__odd-rhat_rank": true,
    "edge__odd-rhat_z": true,
    "edge__odd-rhat_folded": true,
    "edge__odd-rhat_split": true,
    "edge__odd-ess_bulk": true,
    "edge__odd-ess_tail": true,
    "edge__odd-ess_mean": true,
    "edge__odd-independent-acf": true,
    "edge__ties-rhat_rank": true,
    "edge__ties-rhat_z": true,
    "edge__ties-rhat_folded": true,
    "edge__ties-rhat_split": true,
    "edge__ties-ess_bulk": true,
    "edge__ties-ess_tail": true,
    "edge__ties-ess_mean": true,
    "edge__ties-independent-acf": true,
    "edge__scale-rhat_rank": true,
    "edge__scale-rhat_z": true,
    "edge__scale-rhat_folded": true,
    "edge__scale-rhat_split": true,
    "edge__scale-ess_bulk": true,
    "edge__scale-ess_tail": true,
    "edge__scale-ess_mean": true,
    "edge__scale-independent-acf": true,
    "edge__shift-rhat_rank": true,
    "edge__shift-rhat_z": true,
    "edge__shift-rhat_folded": true,
    "edge__shift-rhat_split": true,
    "edge__shift-ess_bulk": true,
    "edge__shift-ess_tail": true,
    "edge__shift-ess_mean": true,
    "edge__shift-independent-acf": true,
    "edge__antithetic-rhat_rank": true,
    "edge__antithetic-rhat_z": true,
    "edge__antithetic-rhat_folded": true,
    "edge__antithetic-rhat_split": true,
    "edge__antithetic-ess_bulk": true,
    "edge__antithetic-ess_tail": true,
    "edge__antithetic-ess_mean": true,
    "edge__antithetic-independent-acf": true,
    "edge__constant-constant-undefined": true,
    "edge__separated_constants-rhat_rank-degeneracy-policy": true,
    "edge__separated_constants-rhat_z-degeneracy-policy": true,
    "edge__separated_constants-rhat_folded": true,
    "edge__separated_constants-rhat_split-degeneracy-policy": true,
    "edge__separated_constants-ess_bulk": true,
    "edge__separated_constants-ess_tail": true,
    "edge__separated_constants-ess_mean": true,
    "iid_effective_size_scale": true,
    "folding_detects_scale_difference": true,
    "rank_detects_shift": true,
    "antithetic_ess_can_exceed_draws": true,
    "ar1_acf": true,
    "ar1_tau": true,
    "ar1_fft_vs_direct": true,
    "all_reference_metric_slots_accounted_for": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/mcmc-diagnostic-reference/index.json

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/atlas-mcmc-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

### 出典と確認範囲

- A. Vehtari, A. Gelman, D. Simpson, B. Carpenter and P.-C. Bürkner (2021). Rank-Normalization, Folding, and Localization: An Improved R-hat for Assessing Convergence of MCMC (with Discussion). https://paulbuerkner.com/publications/pdf/2021__Vehtari_et_al__Bayesian_Analysis.pdf; review_level=corrected-author-paper-selected-sections
訂正済み著者公開PDFの第3–4節、式4.1の分母S+1/4への2021-06-22訂正、定数indicatorの注意を確認。原著の全数値実験を再現したものではありません。

- C. J. Geyer (1992). Practical Markov Chain Monte Carlo. https://www2.stat.duke.edu/~scs/Courses/Stat376/Papers/GeyerStatSci1992.pdf; review_level=original-selected-paired-sequence-theory
原著第3.3節・定理3.1/3.2で可逆性等の条件とinitial-positive/monotone列を確認。本論文473–483頁と合本の討論頁を区別。有限鎖から真のESSが厳密に分かる保証とは扱いません。

- A. Gelman and D. B. Rubin (1992). Inference from Iterative Simulation Using Multiple Sequences. https://www2.stat.duke.edu/~scs/Courses/Stat376/Papers/ConvergeDiagnostics/GelmanRubinStatSci1992.pdf; review_level=original-selected-multiple-chain-starting-points
原著の序論・第2節で複数鎖と分散した初期値を確認。現代のrank/folded Rhatの原典とは区別し、1992年版の全有限標本補正の再現とも呼びません。

- The ArviZ developers (2024). ArviZ0.20.0 public diagnostics API and tagged source. https://python.arviz.org/en/v0.20.0/api/generated/arviz.rhat.html; review_level=official-versioned-source-and-actual-independent-execution
公式v0.20.0のrhat/ess API、diagnostics.py/stats_utils.pyでsplit・rank・Type7 quantile・端点・定数規約を確認。commit94113176cae99a05ba41d1e93739ee2d5bdbe9b1と導入ソースSHAを照合し、atlas診断をimportしない別環境で同じ62datasetを実計算。元コード本文は転載せず、参照値・版・hash・再生成コードを同梱します。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
