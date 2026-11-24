# Reverse VJP, HVP and strict branch derivatives

Fixed small real dimensionless educational controls. Scientific dependencies are exactly the three pins in requirements.txt. Python3.12 is used; Matplotlib3.9.4 is needed only for the separate saved-data plot. No JAX/PETSc dependency or speed comparison.

Run from this directory:

```sh
python -B -W error -m pytest -q -p no:cacheprovider
python -B -W error run.py --input inputs.json --output fresh-output
python plot.py --results fresh-output/result.json --output fresh-figures
```

The CLI supports this one frozen input SHA only (760e23bd914d37ebab5142bc741a2d443207d7d2c6d0a8630031439ecfedec2e); edited inputs are rejected. File and directory result arguments are both accepted for plotting. Source-manifest/ZIP receipts are made by the shared canonical packager, not this runner.

The three cases are genuine reverse-tape VJP/duality (5fixed fixtures), forward-over-reverse HVP and a separate implicit second-order rule (4fixtures), and strict kink/branch/stopping controls (65records plus3explicit jump probes). The rectangular R4-to-R3map includes duplicate-index gather[0,0,2] and scalar broadcast. Cotangents accumulate by reverse traversal; VJP is not implemented by transposing an input-seed forward Jacobian. Advanced gather keys, input arrays and returned cotangents have owning snapshots. Real mutated reset/scatter/broadcast/output controls must fail the independent oracle.

HVP transports the tangent of a reverse cotangent; it builds no primary dense Hessian. The Bratu energy is differentiated at a fixed state, not treated as a solved trajectory or reduced inverse Hessian. The separate scalar implicit path solves F,R1,R2 fromu0=3; square-root family formulas occur only in the independent reference. The fixed-state partial and total curvature are distinct.

Strict kinks use an explicit status and null/empty derivative value with validity, never fabricated zero/NaN. One-sided directional maps need not be linear. The stopped loop tests<=before an update; theta1/4,1/2 and1 are all switching points with no classical derivative. Its executed-trace slope and the converged-root derivative1 are separately labelled. The inactive log branch atx=-1 is never evaluated. There are24pytest functions and46+27+144case gates, fixed before numerical execution. Explicit tape-array storage is not process RSS or an unmeasured speedup.

Both runners write strict result.json, nonempty measured case metrics/records, finite rectangular CSV, NPZ values and incremental raw/completed rows BEFORE later diagnostics. The external shared120-second test+main deadline retains stdout/stderr/JUnit and all failure candidates. No automatic retry, threshold relaxation or successful-subset selection. Before this source's first execution, the protocol/source are independently reviewed and frozen; later actual results are authoritative. Prior public algorithms, inputs, accepted goldens and failure histories remain untouched. Selected official-documentation reading is recorded in source-reading.json; original papers and implementation sources were not read in full. Unknown publication years are n.d., separate from access2026-11-24.

## 日本語の範囲

固定入力の小さな教育例です。数学的な微分、反復の実行trace、陰関数の感度、非滑らかな一方向微分を区別します。全判定と失敗候補を保存し、既存の科学データ・公差は変更しません。図は保存配列から別工程で生成します。実行前固定の予定と実際の成功/時間は区別してください。
