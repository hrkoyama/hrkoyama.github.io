# Ordinary importance sampling and correlated Gaussian MCMC

日本語: 正規稀少尾の通常ISと、相関2変量Gaussianに対するMetropolis–Hastingsを扱います。banana/funnel/HMC/NUTSは実装しておらず、Gaussianだけでそれらの完了とは数えません。

English: two fixed finite studies distinguish estimator variance/finite interval coverage from per-observable MCMC uncertainty and exact joint-target controls.

## Ordinary IS / 通常IS

The target is standard normal, thresholdsa3/6, proposalN(a,1). Y=1(X>a)exp(-aX+a²/2) is averaged without a random normalizing denominator.64independent seed batches supply nested2048/8192prefixes. Coupled prefixes are not additional independent replications. Raw Gaussian draws and contributions are retained; zero direct-MC hits stay zero.

Analytic rth contribution moments exp(r(r−1)a²/2)*normal_tail(r*a),r1..4, are qualified by independent positive completed-square quadrature and tail identities. Ordinary IS known-variance normal95intervals and direct-MC Clopper-Pearson intervals have separate roles.64trial empirical coverage and its binomial uncertainty are reported separately per threshold/prefix, not turned into general coverage guarantees or weighted Bernoulli exact intervals. Global likelihood-weight ESS and event-contribution ESS are distinct. Owen's author Chapter9 was selectively read during preparation; current refetch403 and absence of a full-book audit are recorded.

## Genuine2D Gaussian MH and independent diagnostics / 2変量MH・独立診断

The invariant target is N((1,−1),[[1,.95],[.95,1]]), not two independently correct marginals. Four chains start at fixed whitened corners. Each of4fixed seed sets has1024burn+8192saved draws, a covariance-preconditioned.9proposal and a fixed isotropic.25comparator. Every rejection stays in the chain.8actual chainset evolutions generated reference input; a separate ArviZ0.20process evaluates the exact same128observable-prefix datasets and640values. This independence qualifies diagnostic arithmetic, not an independent sampler or a nonlinear multimodal target.

The8observables are centered coordinates, squares, product, quadratic form and normalized sum/difference directions. Exact joint moments, whitening and wrong-correlation negative controls are separate from rank/folded split-Rhat, bulk/tail/mean ESS and original-scale meanMCSE. Preconditioned full-prefix gates apply to all8observables for all4seed sets. Short prefixes and isotropic comparisons are descriptive; they are not selected or required to fail. Rhat/ESS/MCSE do not establish global convergence.

An independently pinned ArviZ reference-only environment is excluded from production dependencies. Its original-scale MCSE uses sample standard deviation divided by sqrt(meanESS), not a rank-normalized scale. The packaged immutable diagnostic fixture has the exact raw dataset shape/CbyteSHA used by ArviZ and is guarded before all640comparisons. Main separately evolves8freshchainsets and applies the unchanged physical/mixing gates there. Fresh data SHA/equality is recorded descriptively,never demanded portable bit equality. NumPy2.0compatibilitypolicy only guarantees constrained samebuild/environment/machine reproducibility; this pre-execution correction addresses a potential portability issue,not a measured mismatch. https://numpy.org/doc/2.0/reference/random/compatibility.html Vehtari's selected primary sections and ArviZ0.20official APIs/source roles are recorded; no full-paper claim or copied sampler is made.

## Actual reference history and acceptance scope / 参照履歴・判定範囲

Reference attempt01 passed80analytic SDE checks and22ISmoment checks, and generated8MHchainsets/128datasets; it stopped at an ArviZ import deprecation warning. The reference-only environment was explicitly repinned to compatible pyparsing3.2.1, keeping warnings-as-errors and all raw data/source/input/criteria unchanged. Attempt02 generated640ArviZvalues on the same saved data, then retained a637/640candidate diagnostic disagreement (3tail-ESSvalues). No sampling rerun or tolerance adjustment was used. A separately authorized27check saved-array cause audit explained1ULP interpolation at repeated MH values. The new variant explicitly matches pinned ArviZ0.20/SciPy1.14.1 finite-floating type7 interpolation; Decimal120exactType7 and old NumPy keep those ties,so neither NumPy mathematical error nor ArviZ exact-truth superiority is claimed. The quantile primitive is shared while ACF/ESS arithmetic is independent. Attempt03 then passed3tie regressions and640/640same-data comparisons in2.152150seconds with no sampling or ArviZ regeneration,unchanged tolerances,and allsource/datahashes unchanged. Original637/640failure remains retained. Main itself is still unexecuted.

The main plan has21pytest tests and793case gates:17IS and776MCMC, of which640are same-data diagnostic comparisons. These are arithmetic decisions, not extra physical problems or independent sampled trajectories.22ISreference qualifiers and640external diagnostic values are tracked separately from main pytest. Per-observable moment error is compared with MCSE plus a fixed natural-scale allowance, while analytic target identity remains exact. Finite stochastic checks do not certify arbitrary tails or general-chain convergence.

## 実行と固定契約 / Execution and frozen contract

Production dependencies are exactly NumPy2.0.2, SciPy1.14.1 and pytest8.3.5. The public scientific commands are:

```sh
python -B -W error -m pytest -q -p no:cacheprovider --junitxml=FRESH/tests.xml
python -B -W error run.py --input inputs.json --output FRESH_RESULTS
python plot.py --results FRESH_RESULTS --output FRESH_RESULTS
```

Use one thread for BLAS/OpenMP. Pytest and main share one externally enforced120second deadline per group; there is no automatic retry, tolerance relaxation, window selection or seed replacement. Runtime is unmeasured before the authorized main receipt. Plotting additionally requires Matplotlib3.9.4 and only reads saved accepted arrays. PNG/SVG/PDF and gallery previews show actual state×time or sample/state data, not a claimed two-dimensional physical flow.

`pre-run-contract.json` binds the source, fixed inputs, acceptance, independent reference cache, and planned test/gate inventory. A completed result requires every named case, nonempty high-level run records, exactly the planned gate count, all fixed checks, finite arrays and numeric CSV. No result is inferred from a static source review.

入力・判定基準・seed・固定窓を事前に束縛し、失敗後の基準調整や成功するseedへの差替えを行いません。失敗は独立したattemptとして元ソース、契約、入力、出力、ログとともに保持します。

## 保存と失敗保持 / Saved data and failure retention

Full endpoints/contributions/chains and selected paths are saved as numeric NPZ. Each completed SDE batch and MCMC chainset is saved before fitting/diagnostics, with candidate checkpoints; active driver/state arrays are retained on exceptions. CSV is finite and rectangular. Case-level records summarize actual batches/configurations; detailed diagnostics remain in JSON/cache. No random stream is regenerated to obtain a passing diagnostic.

The public source includes reference/cache provenance and the exact generating code. Full first-attempt and resumed-reference artifacts are retained persistently by the project. Any reference cache is bound to actual input, source and same-data hashes. Setup failures are distinguished from numerical disagreement. Reference-only scientific generation is explicitly counted separately from main.
