# Globalization from identical fixed starts

Fixed small real dimensionless educational controls. Scientific dependencies are exactly the three pins in requirements.txt. Python3.12 is used; Matplotlib3.9.4 is needed only for the separate saved-data plot. No JAX/PETSc dependency or speed comparison.

Run from this directory:

```sh
python -B -W error -m pytest -q -p no:cacheprovider
python -B -W error run.py --input inputs.json --output fresh-output
python plot.py --results fresh-output/result.json --output fresh-figures
```

The CLI supports this one frozen input SHA only (04ee3e49e6e2192ee4e58ae20e03905fc56f0c793ce4bbf7d00c13ae3586a9fb); edited inputs are rejected. File and directory result arguments are both accepted for plotting. Source-manifest/ZIP receipts are made by the shared canonical packager, not this runner.

The root systems are Rosenbrock F=(10(y-x²),1-x) and the31-interior-node Bratu stencil at lambda3 on[0,1] with zero Dirichlet endpoints. There are21common-start trajectories (7inputs times3methods) plus2stationary nonroot controls and1pre-evaluation exponential-domain control. Six fixed Armijo/dogleg starts must find roots; other trajectories are diagnostic and can end in explicit nonconvergence. The result does not call every diagnostic trajectory a root. Original residual success is invariant under left residual scaling.

Dogleg uses the Euclidean state radius, a minimum-norm SVD Gauss-Newton endpoint with the declared cutoff and a Cauchy-to-GN segment. A zero-gradient nonroot is explicit; uncomputed rank is null. This is not an exact optimal trust-region subproblem or PETSc implementation replica. Stable quadratic predicted decrease and the direct expression are both saved and audited. All rejected steps, domain candidates, counts and radius/alpha histories remain visible. Exponential arguments outside[-700,700] are rejected before evaluation as the declared floating-point domain, including underflow-prone trials.

Rosenbrock has the independent exact root(1,1); Bratu uses a separately assembled discrete correction audit, not continuum1e-8 exactness. Small Fraction/Decimal dogleg components qualify the geometry. There are16pytest functions and145case gates, fixed before numerical execution. Timings and numerical outcomes belong to actual result/verification receipts, not a prediction in this source.

Both runners write strict result.json, nonempty measured case metrics/records, finite rectangular CSV, NPZ values and incremental raw/completed rows BEFORE later diagnostics. The external shared120-second test+main deadline retains stdout/stderr/JUnit and all failure candidates. No automatic retry, threshold relaxation or successful-subset selection. Before this source's first execution, the protocol/source are independently reviewed and frozen; later actual results are authoritative. Prior public algorithms, inputs, accepted goldens and failure histories remain untouched. Selected official-documentation reading is recorded in source-reading.json; original papers and implementation sources were not read in full. Unknown publication years are n.d., separate from access2026-11-24.

## 日本語の範囲

固定入力の小さな教育例です。数学的な微分、反復の実行trace、陰関数の感度、非滑らかな一方向微分を区別します。全判定と失敗候補を保存し、既存の科学データ・公差は変更しません。図は保存配列から別工程で生成します。実行前固定の予定と実際の成功/時間は区別してください。
