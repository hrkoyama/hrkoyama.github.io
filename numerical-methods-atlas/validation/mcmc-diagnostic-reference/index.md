# MCMC診断の独立照合：rank Rhat・bulk/tail ESS・退化条件

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
## 前提・単位・境界

無次元1D標的p=.5N(−6,1)+.5N(6,1)、平均0/分散37/正側占有.5。3固定seed・4鎖、burn1024、保持16384標本/鎖。prefix1024/4096/16384は入れ子で独立再試行ではありません。棄却と自己遷移を保持します。

**編集上の補足**

独立ライブラリとの一致は診断値の計算の照合であり、目標分布を十分探索した証明ではありません。定数や峰指示関数の変動不足は数値のESSへ置き換えず、状態と理由を併記します。負の自己相関ではESSが標本数を超える場合があり、旧Gaussian例の保守的な下限規約とは区別します。

## 採用した計算法

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

## 比較・検証

実鎖9組×3prefix×x/indicator＋8小fixtureの62組。同じbytesを再生成して照合し、通常の有限値Rhat/ESS/ACFと、定数・鎖内ゼロ分散・odd・ties・shift・scaleを検査。別の直接lag和、定常AR(1)の無限列tau=(1+rho)/(1−rho)で有限推定の誤差も測定します。routineは保存参照との照合で、ArviZのその場再実行は任意の別手順です。

## 確認の限界

固定seed・有限予算の教育用実験です。局所Gaussian RWも理論上は既約なMHであり、有限時間のtrappingを非エルゴードなアルゴリズムとは呼びません。小さいRhat・大きいESS・プールCDFの一致は未発見の峰を除外せず、既知対称性のreflection提案も一般多峰ソルバーではありません。量子計算は追加しません。 定数observableのESS=NというArviZ raw規約を混合の証拠にしません。全同値はnull＋status、鎖ごとに異なる定数のRhatはnull＋infinite-separationとして、ライブラリの巨大finite/infを残し通常有限値の一致点から除外します。bulk ESSは原スケール平均のMCSEへ流用しません。

## 保存実測値と判定

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

## 取得・実行

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

## 出典と確認範囲

- A. Vehtari, A. Gelman, D. Simpson, B. Carpenter and P.-C. Bürkner (2021). Rank-Normalization, Folding, and Localization: An Improved R-hat for Assessing Convergence of MCMC (with Discussion). https://paulbuerkner.com/publications/pdf/2021__Vehtari_et_al__Bayesian_Analysis.pdf; review_level=corrected-author-paper-selected-sections
訂正済み著者公開PDFの第3–4節、式4.1の分母S+1/4への2021-06-22訂正、定数indicatorの注意を確認。原著の全数値実験を再現したものではありません。

- C. J. Geyer (1992). Practical Markov Chain Monte Carlo. https://www2.stat.duke.edu/~scs/Courses/Stat376/Papers/GeyerStatSci1992.pdf; review_level=original-selected-paired-sequence-theory
原著第3.3節・定理3.1/3.2で可逆性等の条件とinitial-positive/monotone列を確認。本論文473–483頁と合本の討論頁を区別。有限鎖から真のESSが厳密に分かる保証とは扱いません。

- A. Gelman and D. B. Rubin (1992). Inference from Iterative Simulation Using Multiple Sequences. https://www2.stat.duke.edu/~scs/Courses/Stat376/Papers/ConvergeDiagnostics/GelmanRubinStatSci1992.pdf; review_level=original-selected-multiple-chain-starting-points
原著の序論・第2節で複数鎖と分散した初期値を確認。現代のrank/folded Rhatの原典とは区別し、1992年版の全有限標本補正の再現とも呼びません。

- The ArviZ developers (2024). ArviZ0.20.0 public diagnostics API and tagged source. https://python.arviz.org/en/v0.20.0/api/generated/arviz.rhat.html; review_level=official-versioned-source-and-actual-independent-execution
公式v0.20.0のrhat/ess API、diagnostics.py/stats_utils.pyでsplit・rank・Type7 quantile・端点・定数規約を確認。commit94113176cae99a05ba41d1e93739ee2d5bdbe9b1と導入ソースSHAを照合し、atlas診断をimportしない別環境で同じ62datasetを実計算。元コード本文は転載せず、参照値・版・hash・再生成コードを同梱します。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Independent MCMC diagnostic checks: rank Rhat, bulk/tail ESS and degeneracies

Actually process62 byte-identical datasets with separately installed ArviZ0.20.0, bound by recipe/input/chain/official-source hashes. Separate finite-value agreement from explicit degeneracy-policy differences.

**Methods used**

- [Markov-chain Monte Carlo / MCMC](https://hrkoyama.github.io/numerical-methods-atlas/methods/mcmc/?lang=en) (`mcmc`)

**Equations**

[This example’s diagnostic and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/mcmc-diagnostic-reference/?lang=en#mcmc-diagnostic-reference-en-algorithm)

Original equation-based implementation: split with the odd center dropped, average-tie Blom ranks using corrected S+1/4, re-rank folded deviations, and take the larger Rhat. Bulk ESS uses rank-split draws; tail ESS first determines Type7 quantiles on original full draws, then splits <= indicators. Use initial-positive/monotone pairs, declared endpoint handling and tau>=1/log10(total), without clipping antithetic ESS to N.

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

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![Independent MCMC diagnostic checks: rank Rhat, bulk/tail ESS and degeneracies: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/results/mcmc-diagnostic-reference.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

No separate physical test problem is assigned to this check or diagnostic. Its own diagnostic figure and validation material are provided.

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/mcmc-diagnostic-reference/?lang=en#mcmc-diagnostic-reference-en-validation)

62 datasets: nine actual chains times three prefixes times x/indicator plus eight small fixtures. Regenerate and hash identical bytes; compare ordinary finite Rhat/ESS/ACF and test constants, zero within-chain variance, odd lengths, ties, shift and scale. Direct lag sums and infinite-series stationary-AR(1) tau=(1+rho)/(1−rho) provide separate checks of finite estimates. Routine runs compare stored references; live ArviZ regeneration is a separate optional procedure.

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.
## Assumptions, units and boundaries

Dimensionless1D target p=.5N(−6,1)+.5N(6,1), mean0/variance37/positive occupancy.5. Three fixed seeds, four chains,1024 warmup and16384 retained draws/chain. Prefixes1024/4096/16384 are nested, not independent replications. Rejections/self-transitions are retained.

**Editorial clarification**

Agreement with an independent library checks diagnostic computation; it does not prove adequate target exploration. Constants and insufficiently varying mode indicators carry explicit states and reasons rather than a reassuring numeric ESS. Negative autocorrelation can yield ESS above the draw count; this is distinct from the conservative floor used in the earlier Gaussian example.

## Adopted numerical method

Original equation-based implementation: split with the odd center dropped, average-tie Blom ranks using corrected S+1/4, re-rank folded deviations, and take the larger Rhat. Bulk ESS uses rank-split draws; tail ESS first determines Type7 quantiles on original full draws, then splits <= indicators. Use initial-positive/monotone pairs, declared endpoint handling and tau>=1/log10(total), without clipping antithetic ESS to N.

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

## References and validation

62 datasets: nine actual chains times three prefixes times x/indicator plus eight small fixtures. Regenerate and hash identical bytes; compare ordinary finite Rhat/ESS/ACF and test constants, zero within-chain variance, odd lengths, ties, shift and scale. Direct lag sums and infinite-series stationary-AR(1) tau=(1+rho)/(1−rho) provide separate checks of finite estimates. Routine runs compare stored references; live ArviZ regeneration is a separate optional procedure.

## Limits

An educational fixed-seed, finite-budget experiment. The local Gaussian RW is theoretically irreducible MH; finite-time trapping is not called a nonergodic algorithm. Small Rhat, large ESS and pooled-CDF agreement cannot rule out undiscovered modes. Symmetry-informed reflection is not a generic multimodal solver. No quantum calculations. ArviZ raw constant-ESS=N is not evidence of mixing. Globally identical values yield null/status; differing per-chain constants yield null/infinite-separation Rhat while retaining raw huge-finite/infinite library values outside ordinary finite comparisons. Bulk ESS is not a raw-mean MCSE estimator.

## Stored measurements and decisions

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

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/mcmc-diagnostic-reference/index.json

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/atlas-mcmc-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

## Sources and review scope

- A. Vehtari, A. Gelman, D. Simpson, B. Carpenter and P.-C. Bürkner (2021). Rank-Normalization, Folding, and Localization: An Improved R-hat for Assessing Convergence of MCMC (with Discussion). https://paulbuerkner.com/publications/pdf/2021__Vehtari_et_al__Bayesian_Analysis.pdf; review_level=corrected-author-paper-selected-sections
Checked original sections3–4, the2021-06-22 correction of Eq4.1 to denominator S+1/4, and the constant-indicator warning. This does not reproduce every original numerical experiment.

- C. J. Geyer (1992). Practical Markov Chain Monte Carlo. https://www2.stat.duke.edu/~scs/Courses/Stat376/Papers/GeyerStatSci1992.pdf; review_level=original-selected-paired-sequence-theory
Checked section3.3 and Theorems3.1/3.2 for reversibility assumptions and initial-positive/monotone sequences. Main article pp473–483 are distinguished from combined discussion pagination; no claim gives exact true ESS from finite chains.

- A. Gelman and D. B. Rubin (1992). Inference from Iterative Simulation Using Multiple Sequences. https://www2.stat.duke.edu/~scs/Courses/Stat376/Papers/ConvergeDiagnostics/GelmanRubinStatSci1992.pdf; review_level=original-selected-multiple-chain-starting-points
Checked the original introduction/section2 on multiple sequences and overdispersed starts. Distinct from the later rank/folded method, and not a reproduction of every1992 finite-sample correction.

- The ArviZ developers (2024). ArviZ0.20.0 public diagnostics API and tagged source. https://python.arviz.org/en/v0.20.0/api/generated/arviz.rhat.html; review_level=official-versioned-source-and-actual-independent-execution
Checked the official0.20.0 rhat/ess API and tagged source for splitting, ranks, Type7 quantiles, endpoints and constant conventions. Installed source hashes match commit94113176cae99a05ba41d1e93739ee2d5bdbe9b1;62 byte-identical datasets were actually processed in a separate environment without importing Atlas diagnostics. No upstream implementation is reproduced; values, versions, hashes and regeneration code are supplied.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
