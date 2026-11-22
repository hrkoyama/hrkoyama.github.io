# 多峰性MCMC：峰への閉じ込め・偽の安心・大域提案

同じ2峰密度を、分散初期値の局所MH・同じ峰からの局所MH・対称reflectionを混ぜるMHで比較。期待した混合不良の検出と、実際の峰間移動を分けて検証します。

## 前提・単位・境界

無次元1D標的p=.5N(−6,1)+.5N(6,1)、平均0/分散37/正側占有.5。3固定seed・4鎖、burn1024、保持16384標本/鎖。prefix1024/4096/16384は入れ子で独立再試行ではありません。棄却と自己遷移を保持します。

**編集上の補足**

この検証の「合格」は、混合する系列の分布確認と、意図的に混合しない系列の失敗・診断の盲点を正しく示したことを表します。全系列が収束したという意味ではありません。RhatやESSは観測量・有限標本・初期値に依存し、同じ峰に閉じ込められた全鎖では良く見えることがあります。反射ジャンプは既知の対称性を利用する比較用の提案であり、一般の未知の多峰性を解く保証ではありません。

## 採用した計算法

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

## 比較・検証

解析平均・分散・CDFの指定7点・正側占有と照合。各鎖の占有率と峰間遷移、rank/folded split Rhat、bulk/tail/mean・modeindicator ESS、鎖内だけのACF/ESSを記録。分散trapped鎖はpooled分布が良くてもRhat/多鎖ESSで失敗、same-mode鎖はRhatが良くても既知標的に失敗する対照です。scenario passはこの期待失敗を検出できた意味です。CDF差は指定点最大でKS全域距離・IID検定p値ではありません。

## 確認の限界

固定seed・有限予算の教育用実験です。局所Gaussian RWも理論上は既約なMHであり、有限時間のtrappingを非エルゴードなアルゴリズムとは呼びません。小さいRhat・大きいESS・プールCDFの一致は未発見の峰を除外せず、既知対称性のreflection提案も一般多峰ソルバーではありません。量子計算は追加しません。

## 保存実測値と判定

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

このコマンドは配布グループの全例を実行します。

## 出典と確認範囲

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

# Multimodal MCMC: trapping, false reassurance and a global proposal

Compare dispersed local MH, same-mode local MH and symmetry-informed reflection/local MH on the same bimodal target. Separate detecting expected mixing failures from successful finite-budget mode exploration.

## Assumptions, units and boundaries

Dimensionless1D target p=.5N(−6,1)+.5N(6,1), mean0/variance37/positive occupancy.5. Three fixed seeds, four chains,1024 warmup and16384 retained draws/chain. Prefixes1024/4096/16384 are nested, not independent replications. Rejections/self-transitions are retained.

**Editorial clarification**

Passing this validation means confirming the well-mixing run and correctly exposing failures and diagnostic blind spots in deliberately trapped runs; it does not mean every run converged. Rhat and ESS depend on the observable, finite sample and initial states, and can look reassuring when all chains miss the same mode. Reflection jumps exploit known target symmetry for this comparison and do not guarantee exploration of arbitrary unknown multimodal targets.

## Adopted numerical method

Local scale.8; mixed uses y=−x+.8Z with probability.1, otherwise y=x+.8Z. The state-independent mixture is symmetric q(y|x)=q(x|y), so MH uses the log-target ratio. Chains use independent PCG64 streams, with no adaptation or removal of rejected states.

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

## References and validation

Compare with analytic moments, seven declared CDF points and positive occupancy. Record per-chain occupancies/transitions, rank/folded split Rhat, bulk/tail/mean and mode-indicator ESS, and within-only ACF/ESS. Dispersed trapped chains can have a good pooled distribution yet fail between-chain diagnostics; same-mode chains can have reassuring Rhat yet fail the known target. A control scenario passes when its intended failure is detected. CDF error is a declared-point maximum, not whole-line KS distance or an IID-test p-value.

## Limits

An educational fixed-seed, finite-budget experiment. The local Gaussian RW is theoretically irreducible MH; finite-time trapping is not called a nonergodic algorithm. Small Rhat, large ESS and pooled-CDF agreement cannot rule out undiscovered modes. Symmetry-informed reflection is not a generic multimodal solver. No quantum calculations.

## Stored measurements and decisions

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

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/mcmc-multimodal-mixing/index.json

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

This command executes every fixed case in the distribution group.

## Sources and review scope

- A. Vehtari, A. Gelman, D. Simpson, B. Carpenter and P.-C. Bürkner (2021). Rank-Normalization, Folding, and Localization: An Improved R-hat for Assessing Convergence of MCMC (with Discussion). https://paulbuerkner.com/publications/pdf/2021__Vehtari_et_al__Bayesian_Analysis.pdf; review_level=corrected-author-paper-selected-sections
  Checked original sections3–4, the2021-06-22 correction of Eq4.1 to denominator S+1/4, and the constant-indicator warning. This does not reproduce every original numerical experiment.
- C. J. Geyer (1992). Practical Markov Chain Monte Carlo. https://www2.stat.duke.edu/~scs/Courses/Stat376/Papers/GeyerStatSci1992.pdf; review_level=original-selected-paired-sequence-theory
  Checked section3.3 and Theorems3.1/3.2 for reversibility assumptions and initial-positive/monotone sequences. Main article pp473–483 are distinguished from combined discussion pagination; no claim gives exact true ESS from finite chains.
- A. Gelman and D. B. Rubin (1992). Inference from Iterative Simulation Using Multiple Sequences. https://www2.stat.duke.edu/~scs/Courses/Stat376/Papers/ConvergeDiagnostics/GelmanRubinStatSci1992.pdf; review_level=original-selected-multiple-chain-starting-points
  Checked the original introduction/section2 on multiple sequences and overdispersed starts. Distinct from the later rank/folded method, and not a reproduction of every1992 finite-sample correction.
- The ArviZ developers (2024). ArviZ0.20.0 public diagnostics API and tagged source. https://python.arviz.org/en/v0.20.0/api/generated/arviz.rhat.html; review_level=official-versioned-source-and-actual-independent-execution
  Checked the official0.20.0 rhat/ess API and tagged source for splitting, ranks, Type7 quantiles, endpoints and constant conventions. Installed source hashes match commit94113176cae99a05ba41d1e93739ee2d5bdbe9b1;62 byte-identical datasets were actually processed in a separate environment without importing Atlas diagnostics. No upstream implementation is reproduced; values, versions, hashes and regeneration code are supplied.
- N. Metropolis, A. W. Rosenbluth, M. N. Rosenbluth, A. H. Teller and E. Teller (1953). Equation of State Calculations by Fast Computing Machines. https://doi.org/10.1063/1.1699114; review_level=publisher-abstract-and-metadata
  Publisher bibliography and abstract checked. Cited for symmetric-proposal Metropolis acceptance; no reproduction of the original hard-sphere experiment is claimed.
- W. K. Hastings (1970). Monte Carlo sampling methods using Markov chains and their applications. https://probability.ca/hastings/hastings.pdf; review_level=original-paper-excerpt-and-metadata
  Bibliography, summary and opening excerpt of the original paper hosted by a university checked; the publisher DOI could not be opened. This example uses symmetric Gaussian proposals and does not implement a general asymmetric proposal ratio.

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
