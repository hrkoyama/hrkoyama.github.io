# Fixed inverse and optimization controls / 固定入力の逆問題・最適化

This lightweight supplement contains three scoped cases: 17 Bratu GN/LM/bounded fits, 16 analytic-objective quasi-Newton fits and 42 Bratu noise/regularization fits. All quantities are dimensionless. The Bratu state is one-dimensional with zero Dirichlet data; parameter-plane plots are not two-dimensional physical flows.

本例は17個のBratu最小二乗、16個の解析目的関数、42個の雑音・正則化fitからなります。無次元の小固定例です。Bratu状態は1D・零Dirichletで、2変数の図を2D物理流れとは数えません。

## Reproduction

Install only the three exact pins in requirements.txt. Run `python -B -W error -m pytest -q -p no:cacheprovider` and `python -B -W error run.py --input inputs.json --output FRESH_DIRECTORY`. Each main run requires a new output directory. Plotting is separate: `python plot.py --results FRESH_DIRECTORY/result.json --output FRESH_DIRECTORY` using Matplotlib 3.9.4. Plotting reads saved data; only the analytic Rosenbrock contour is evaluated during rendering. No forward PDE solves are performed by plot.py.

要件は固定3依存のみ。pytestと主計算の合計は外部共有120秒で検査します。参照資格は別の固定30秒枠で、実際の48判定・4状態比較・4局所参照fitが合格したcacheを同梱します。主計算は参照再生成をしません。数値実行前後の入力・受入条件・ソースhash、実時間、成否は各receiptへ保存します。

## Model and interpretation

The exact retained six-module MIT legacy capsule supplies the existing two-coefficient model, dense zero-start Newton state, adjoint gradient and projected-gradient algorithm. Observation-only wrappers save incoming Newton states and completed evaluations without changing their arithmetic. The canonical physical box is converted explicitly to the legacy per-parameter intervals. We do not count the old 30 tests, 17 fits, four-gamma study or the cached 1023-grid observations as new work.

GN and LM use explicit augmented residuals with an SVD least-squares solve. Parameter scales change coordinates, not the reported physical gradient. Objective gamma differs from algorithmic LM mu. SciPy LM is UNBOUNDED; TRF and legacy PG use the physical box. An invalid forward-domain trial is retained: the original line/damping loop can reject it, but a SciPy callback exception aborts the fit. No artificial large residual or method restart hides a failure. Library status/success/message and external stationarity are both saved.

独立Thomas参照は同じ離散モデルの別残差・三重対角消去・感度実装です。参照と主比較の一部はSciPy TRFライブラリを共有し、独立最適化エンジンや大域最小の証明とは説明しません。非有界法の共通参照には厳密な内点性と非有界勾配条件が必要です。

The original L-BFGS primary stores only up to three s/y pairs and work vectors; it has no dense inverse matrix. Each direction is separately compared with a small dense oracle starting from CURRENT gamma0 I and replaying only those currently retained pairs. Oracle storage/actions are separate from primary pair storage; objective-model storage is also distinct. Strong-Wolfe failures and unresolved curvature are retained, with no Armijo-only rescue or eigenvalue clipping.

For noise studies, exactly two independent PCG64 vectors are reused across sigma and data contexts. W is an optimization metric; Sigma is separate noise covariance. A gamma is selected only from a complete, qualified five-point path. A fixed-gamma sandwich is exact for the stated linear control; at a nonlinear Bratu estimate it is a LOCAL LINEAR-MODEL plug-in that ignores residual-weighted Hessians and gamma-selection randomness. It is not covariance conditional on a selection event, a posterior, a confidence interval or a coverage theorem. Bound-active/rank-deficient ellipses are N/A. The finite four-point L-curve diagnostic is not the manual spline/corner algorithm.

## Actual source-reading scope

Selected author-hosted Liu–Nocedal PDF pages printed 2–4 were rendered and visually read: inverse-BFGS, limited retained pairs and oldest-pair deletion. Those pages use weak Wolfe; this example deliberately specifies strong Wolfe. Current scalar scaling is also derived independently. Fletcher 1970 original text remains unread and is bibliography only. Hansen's version 4.1 manual (March 2008), printed 18 and 35, was rendered/read for L-curve and discrepancy roles. SciPy documentation is version 1.14.1, accessed 2026-11-24; the access date is not a publication year. Exact URLs/scopes are in references/source-reading.json and cases.json. Original PDFs are not redistributed.

一次資料の全論文閲読を主張しません。Fletcher原著本文未読、Liu–Nocedalの選択箇所の弱Wolfe、独自に固定したstrong Wolfeを区別します。Hansen manualの版年とWeb文書の閲覧日も区別しています。

## Output and failure retention

The runner exports finite numeric CSV columns, per-fit full-field NPZ files, append-only raw Newton/objective/line-search JSONL, gamma-path JSON and the strict public result envelope with nonempty per-case metrics. Completed candidates are saved before rank/reference/covariance diagnostics. The raw trace cannot expose opaque library-internal temporary arrays and does not claim to. Public-contract functions are exact selected functions from the real public verifier, with the original verifier SHA recorded in public_contract.py.

Runtime and outcomes are taken from the actual result/verification receipts. No accepted thresholds are adjusted after measurement. A failed attempt must be retained under a new revision before any changed rerun. Remaining scope includes many coefficients, real observations, global convergence and selection-aware inference.
