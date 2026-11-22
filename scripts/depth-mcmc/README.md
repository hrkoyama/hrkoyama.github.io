# Multimodal MCMC / 多峰性MCMC

These two lightweight cases preserve the previous Gaussian-MCMC release. One physical target is added: a symmetric two-component Gaussian mixture. The second case calibrates diagnostic implementations; it is not another physical problem. No quantum computation is performed.

既存のGaussian MCMC凍結版を保持し、対称2峰Gaussian混合という物理問題1件と、問題数へ加算しない診断照合1件を追加します。量子計算は追加しません。

## Three behaviors on one known target / 既知標的の3つの振る舞い

```
pi(x) = .5 Normal(-6,1) + .5 Normal(6,1)
F(x) = .5 Phi(x+6) + .5 Phi(x-6)
E[X]=0, Var(X)=37, P(X>0)=.5.
```

Run four chains at each of three fixed seeds. Retain16384 post-warmup draws per chain after1024 warmup draws, **including rejected states and self-transitions**. The prefix budgets1024/4096/16384 come from the same chains; they are nested observations, not independent repetitions or guaranteed monotone improvements.

- **Dispersed local RW:** start two chains at−6 and two at+6; propose `y=x+.8Z`. All remain in their initial mode over this budget. The pooled moments/CDF/occupancy can look correct, while between-chain rank-Rhat≈1.73 and bulk ESS≈6 expose the poor mixing. Summed within-chain ESS around6000 describes exploration inside the modes and is misleading as a global measure.
- **Same-mode local RW:** start every chain at−6 with the same local kernel. Rhat≈1 and bulk ESS around5600–5900 look reassuring, while positive occupancy is zero and the known target CDF is badly wrong. A small Rhat cannot reveal a mode never visited by any chain. The constant mode indicator has undefined diagnostics, not perfect confidence.
- **Symmetry-informed mixed proposal:** use `y=-x+.8Z` with probability.1 and the local proposal otherwise, starting from dispersed modes. Because `q(y|x)=.9 phi_.8(y-x)+.1 phi_.8(y+x)=q(x|y)`, the MH acceptance ratio uses only the target densities. Every chain crosses modes more than1100 times in the fixed experiment. This deliberately exploits a known symmetry; it is not a generic multimodal sampler.

4鎖×3seedを固定し、warmup後の棄却・自己遷移も標本として保持します。分散した初期値の局所鎖では、pooled分布が良く見えても峰間移動がなく、多鎖診断が失敗を示します。全鎖を同じ峰から始めると、Rhatが良くても既知標的との一致を失います。既知対称性を使うreflection/local混合提案を対照にし、各鎖の占有率と遷移数を明示します。

The local Gaussian RW kernel remains theoretically irreducible and reversible; finite-budget trapping is **poor mixing**, not a claim that the algorithm is nonergodic. Burn-in length and a favorable finite experiment do not prove stationarity or a universal convergence rate. A control scenario **passes when its intended failure is correctly detected**; it is not labelled a successfully converged sampler.

局所Gaussian RWも理論上は既約な可逆MHです。有限予算での閉じ込めを非エルゴードなアルゴリズムとは呼びません。対照のpassは「期待した失敗を正しく検出できた」という意味で、標本化の収束成功とは区別します。

The input file predates the first sampler/diagnostic pilot. SHA256: `b20b594ab2d001426fbc58d1fe86fe4719bd42455f6a10f502966f85fb6eb49a`. No threshold, seed, proposal, or budget was adjusted after inspecting results. An initial implementation check exposed a status bug: variance of an exactly repeated, rank-normalized float could be tiny-positive from summation rounding. Exact constant rows are now detected explicitly; the failed output and correction note are retained in the project evidence directory. This was an implementation correction, with inputs and criteria unchanged.

入力と受入基準は初回計算前に保存し、その後変更していません。初期実装の退化status判定に、定数rank値の丸め由来の微小分散を誤認する問題があり、厳密な同値判定へ修正しました。入力・基準の緩和はなく、失敗した出力と修正理由も保存しています。

## What is measured / 測定量

Compare the analytic mean, variance, positive occupancy and CDF at **seven declared points** `[-8,-6,-4,0,4,6,8]`. Record each signed point error and its maximum. This is not a supremum KS distance, and no IID KS p-value is assigned to correlated draws. Store all fixed seeds and prefix budgets, per-chain occupancies, and per-chain sign-transition counts. The mixed case must pass all final-budget distribution and diagnostic limits in `inputs.json`. No monotonicity of ESS or error across nested prefixes is required.

CDFは指定7点の符号付き差と最大差です。全実数上のKS距離ではなく、相関標本にIID検定のp値を付けません。固定した全seed・全prefix・各鎖の占有率・峰間遷移を記録し、単一鎖の見た目やpooled平均だけで成功にしません。

Within-chain ACF centers **each chain by its own sample mean**, uses autocovariance divisorN rather thanN−lag, and divides by lag-zero covariance. An FFT with padding>=2N is checked by separately coded direct lag sums. The within-only ESS is the sum of separately estimated single-chain mean ESS values; it is explicitly separate from the modern multi-chain ESS that also includes between-chain information.

鎖内ACFは鎖ごとの標本平均を引き、分母Nの自己共分散をゼロlagで正規化します。FFTと別実装の直接lag和を比較します。鎖別ESSの単純合計は鎖内だけの診断で、鎖間情報を用いるmodern多鎖ESSと分けて表示します。

## Exact diagnostic conventions / 診断の定義

The original implementation follows the equations in Vehtari et al.2021, sections3–4, and the Geyer paired-sequence framework, not a copy of the ArviZ implementation. The independent library checks the same estimator and finite-data conventions.

1. Split into the first and last `floor(N/2)` draws, dropping the center draw for oddN. Pool ranks across the split chains; ties get average ranks. Use corrected Blom scores `Phi^-1((rank−3/8)/(S+1/4))`. The author's2021-06-22 correction replaces the earlier printed denominatorS−1/4.
2. Rank-Rhat is the maximum of rank-normalized split-Rhat and folded-rank split-Rhat. Folding uses absolute deviations from the pooled **split** median, followed by a new rank transform. Raw split-Rhat is also reported, without claiming every historical1992 finite-sample correction.
3. Bulk ESS applies the multi-chain variance/ACF formula to rank-normalized split values. Mean ESS applies it on the original scale. Tail ESS is the smaller ESS of the5% and95% `X<=quantile` indicators. Compute R Type7 quantiles from the **original full array before splitting the indicator**, including the center draw in odd-length quantile calculation.
4. The multi-chain correlation estimator combines within-chain biased autocovariance, within varianceW and between-chain means, with `Vplus=(N−1)W/N+B/N`. Truncate using initial-positive paired correlations and monotonize the retained complete pair sums. The last examined pair contributes its positive even-lag endpoint once. This finite endpoint convention matches the independently executed reference. The finite-data safeguard is `tau>=1/log10(total_draws)`. **ESS may exceed the raw draw count for antithetic chains**; it is not clipped toN.

定義はsplit順序・odd長の中央標本・平均順位ties・訂正済みBlom分母・fold後再rank・Type7分位点とindicatorの順序まで固定します。bulk、tail、原スケールmean、峰indicatorのESSは異なる推定対象です。反相関ではESS>Nを許し、旧例のtau≥1という床を持ち込みません。Geyerの構造定理には定常性・既約性・可逆性等の仮定があり、有限鎖の推定量を真のESSそのものとは扱いません。

No MCSE is inferred from bulk ESS for the raw mean: bulk concerns a rank-transformed observable. Raw-mean MCSE would require mean ESS/raw autocovariance; occupancy concerns the indicator's mean ESS. No MCSE=0 is assigned to a trapped constant indicator.

原スケール平均のMCSEへbulk ESSを流用せず、定数indicatorからMCSE=0という偽の確信を作りません。

## Undefined values and policy differences / 不定値とpolicy差

Globally identical input values, insufficient chains/draws, and nonfinite inputs yield JSON`null` with a reason. Global constancy uses **exact equality**, preserving rank diagnostics under transformations such asx→1e−20x for genuinely nonconstant data. Exact zero within-chain variation with distinct chain values yields null/infinite-separation Rhat. ArviZ can produce a huge finite rank-Rhat around1e15 for these exact constants because of variance rounding; its raw result is retained. This is a mathematical-degeneracy policy check, **not** a point of finite numerical agreement.

全標本が同一・短鎖・非有限入力はnullと理由で表します。非定数値を小さくしただけでrank診断を無効化しないよう、全体の退化は厳密な同値判定です。鎖ごとに異なる定数では鎖内分散ゼロを明示し、Rhatをnull/infinite-separationとします。ArviZの丸め由来の巨大finite値も保持し、通常の有限値一致点へ混ぜません。

ArviZ's internal near-constant ESS convention returns the raw count; it is retained for transformed quantile events and raw mean-ESS software agreement, but is not promoted into a claim of perfect mixing. In particular, a globally constant **original** observable is declined by Atlas. Under very small rescalings the library's raw mean-ESS near-constant convention can differ from the scale-invariant rank/bulk/tail diagnostics; the distinction is intentional and tested. Negative or infinite numeric sentinels are not passed off as success. The comparison output reports finite-Rhat/ESS counts and all degeneracy exclusions separately.

Of the434 reference metric slots, **324 are finite numerical comparisons** (168 Rhat and156 ESS). The remaining slots are70 globally constant exclusions across10 datasets,30 exact-row infinite-separation policy checks, and10 nonfinite classification checks. Raw ArviZ reports62 nonfinite metric values. These are different accounting categories; “434 numerical values agree” would be incorrect.

ArviZ内部のnear-constant ESS=Nという数値規約は、変換済み分位indicatorやmean ESSの比較上の規約として限定します。元の観測量自体が定数ならAtlasでは未定義です。極小スケールのmean ESS規約と、rank/bulk/tailの不変性は区別してテストします。有限値照合数と除外数を別々に記録します。

434測定枠のうち数値照合は324点（Rhat168・ESS156）です。残りは定数10datasetの70枠除外、鎖内ゼロ分散の30枠policy検査、10枠の非有限値分類です。ArviZ rawの非有限値62個とは区分が異なり、「434数値が一致」とは表示しません。

## Independent reference and calibration / 独立参照と較正

ArviZ0.20.0 was **actually run** on62 byte-identical datasets in a separate optional environment without importing Atlas diagnostics: nine sampler arrays×three prefixes×two observables plus eight edge fixtures (IID, odd length, ties, shift, scale, antithetic, global constant, separated constants). Public APIs supply rank/z/folded/raw-split Rhat, bulk/tail/mean ESS and per-chain ACF. Each array is bound by little-endian float64 C-order SHA256. `reference.json` also records input and recipe SHA, library version/tag/commit, official-versus-installed source SHA, dependency versions, generator SHA and actual UTC execution time. The referenced ArviZ commit is`94113176cae99a05ba41d1e93739ee2d5bdbe9b1`.

別環境のArviZ0.20.0を同じ62datasetへ実際に適用しました。Atlas診断はimportせず、公開APIを使用します。各鎖のbyte列SHA、入力・生成recipe・generator・公式/導入ソース・依存版・実UTC時刻を保存し、通常実行は実鎖を再生成してSHAと保存参照の両方へ照合します。

Routine execution uses only NumPy/SciPy/pytest and does not rerun ArviZ. The deterministic agreement tolerance is distinct from Monte Carlo uncertainty: Rhat absolute2e−10, ESS relative2e−8, normalized ACF/direct-sum comparison2e−12. Ordinary finite comparison errors are around1e−15 in this run; constants and infinite-separation policies are counted separately. Independently, stationary AR(1) draws at rho=−.5/.8 and two fixed seeds compare finite estimated ACF/tau with exact infinite-series `rho^lag` and `tau=(1+rho)/(1−rho)`; this is calibration of a finite estimator, not an exact finite-sample identity.

保存参照との決定論的一致公差と、MCMC標本誤差を分けます。別の定常AR(1)では、有限鎖から推定したACF・tauを無限級数の解析値と比較し、有限標本誤差として示します。3固定seedや良好なlibrary一致は、任意標的・全seedの混合や所定の偽陽性率を保証しません。

## Reproduce / 再実行

Python3.12 with the pinned routine requirements; no network or private repository is needed after installing them. The complete two cases take about3 seconds on the development machine, with a120-second total failure guard. Tests check equations, actual independent edge fixtures, odd/tied/degenerate data, detailed balance, RNG reproducibility, rejection retention and bounded failure paths. The full cases are executed separately byrun.py and the public verifier.

```
python -m pip install -r requirements.txt
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -W error -m pytest -q -p no:cacheprovider
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -W error run.py --input inputs.json --output NEW_RESULT_DIRECTORY
```

Optional figures are drawn from stored JSON only; no sampler is rerun:

```
python -m pip install -r requirements-plotting.txt
python plot.py --results NEW_RESULT_DIRECTORY/result.json --output FIGURE_DIRECTORY
```

通常追試は3依存だけで、参照ライブラリの再導入を要求しません。図は保存結果から再描画します。全traceをHTML表へ展開せず、全診断は保持16384標本を使い、図には最初の連続1024標本だけを別配列に保存します。これは診断標本の間引きではありません。

Optional **live independent reference regeneration** should use a separate environment. It imports ArviZ rather than Atlas diagnostics. Keep its output separate from the frozen `reference.json`:

```
python prepare-reference-input.py --output NEW_CHAIN_DIRECTORY
python3.12 -m venv NEW_REFERENCE_ENVIRONMENT
NEW_REFERENCE_ENVIRONMENT/bin/python -m pip install -r requirements-arviz-reference.lock.txt --report NEW_INSTALL_REPORT.json
NEW_REFERENCE_ENVIRONMENT/bin/python generate-arviz-reference.py --input NEW_CHAIN_DIRECTORY --sources . --evidence . --output NEW_REFERENCE.json --install-report NEW_INSTALL_REPORT.json
```

The optional lock pins the reference environment separately; it does not enlarge routine dependencies. The regenerator checks the installed upstream source against the recorded official commit and records **its current** environment and UTC time. Its metadata and NPZ-container hash can differ across reruns/platforms even when canonical per-array values and diagnostic results agree. The temporary NPZ is about4MB and is not required in the distribution because fixed recipes and per-array SHA bind the same data. No claim has yet been made about untested platforms merely from matching source code.

その場でのArviZ再生成は別環境・別出力へ行います。公式commitのソースSHAを検査し、過去のMac依存記録を引き継がず、その実行時の環境・UTC時刻を採取します。コンテナNPZのhashや日時は再実行で変わり得ますが、比較の基準は各arrayの正規化byte列と診断値です。入力・基準・凍結参照を上書きしません。

## Sources and rights / 一次資料と権利

Full bibliographic details and exact reading scope appear in `cases.json`: Vehtari et al.2021 (corrected original sections3–4), Geyer1992 (paired-sequence assumptions and IPS/IMS), Gelman–Rubin1992 (multiple dispersed chains), and official ArviZ0.20.0 source/API. Historical foundations, adopted inputs, estimator definitions and actual numerical comparisons are distinct. No article PDF or third-party library implementation is redistributed. `LICENSE` covers original implementation code; prose/translations/inputs/figures/data/results follow the site's separate conditions.

原著の選択節・訂正・仮定と、公式版ソース/APIの実際の確認範囲を日英で記録します。歴史・採用入力・独自実装・今回の数値照合を区別し、論文PDFや第三者ライブラリ本文を転載しません。MITの対象は独自コードで、本文・翻訳・入力・図・データ・結果はサイトの別条件です。
