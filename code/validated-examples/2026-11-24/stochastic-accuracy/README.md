# Scalar stochastic accuracy: weak bias and strong path error

日本語: GBM/OUのweak誤差とMonte Carlo標準誤差、GBMのEM/Milsteinstrong誤差を別々に検証する小規模固定入力です。既存GBMとOU浴成分の物理問題を再利用します。OU浴成分だけで位置を含む全Langevin振動子を検証したとは扱いません。

English: three scalar fixed-input studies separate the difference of expectations, sampling error, and coupled-path endpoint RMS error. No financial calibration or application recommendation is made.

## Models, coupling and independent reference / モデル・結合・独立参照

All parameters are dimensionless; the initial value is a deterministic state and the state line is unbounded, with no imposed boundary or clipping. `inputs.json` gives GBM(mu=.5,sigma=.4,X0=1) weak, OU(kappa1.5,theta.2,sigma.8,X0.7) weak, and GBM(mu=.15,sigma=.4,X0=1) strong atT1.

Weak EM uses8/16/32/64steps and32independent seed batches of1024paths per process. Exact continuous moments, exact discrete EM moments, paired difference and its MCSE are distinct. Exact OU innovations are jointly generated with the same Brownian increments using their analytic covariance plus independent bridge noise; independent exact paths would give the wrong paired precision. Fine increments define every coarse block. One stored exact endpoint is reused by both methods and all levels; different floating reduction associations are reported rather than called bit identical.

The finite discrete/mixed moments are independently derived in `references/analytic.py` and evaluated with Decimal80/120digits. Qualification separately checks an independent positive Gauss-Hermite squared-error integral, OU covariance quadrature and pre-measurement bias-versus-paired-SE allocation. Strong squared-error formulas use A^n+B-2K^n at high precision; no cancellation is hidden by clipping a negative MSE to zero. Qualification ran before the first fixed SDE main batch. It does not replace actual SDE paths.

GBMstrong uses16/32/64/128steps,4seeds×8192paths. RMS uncertainty is computed first on complete-path squared errors. A64block paired jackknife reports the fixed last-three-level rate uncertainty; observations at different levels are not independent. Higham2001selected sections4–6 provide primary definitions and Milstein context. Its L1strong definition and logistic experiment are not falsely claimed to be our L2endpoint experiment.

## Acceptance scope / 判定範囲

The main plan has21pytest tests and65case gates:26each weak case and13strong. Independent analytic qualification80checks is separate. Weak moment calibration uses5MCSE, an independently predicted MCSE ratio, resolved3SEallocation at the final two levels and a fixed three-level rate. The quoted SE and nominal intervals are stochastic diagnostics, not deterministic true-error bounds.32repeated normal intervals target discrete EM truth, and their descriptive coverage does not prove general95%coverage. Strong EM and Milstein RMS rates and finest-level improvement are distinct from weak order.

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
