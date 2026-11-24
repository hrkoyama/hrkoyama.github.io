# Discrete adjoints, near-fold sensitivity and distributed VJPs

This educational packet contains three fixed one-dimensional cases, not three new physical equations. All units are dimensionless. The source is implemented and the independent67-check reference qualification passed in its separately recorded authorized attempt. **No primary pytest/main run has occurred at this freeze**. The execution receipt, reference qualification and result files record the actual outcome after authorization; a planned count is not a PASS claim.

## Reproduce

Use Python3.12 and the three exact direct pins in requirements.txt. Matplotlib is needed only to render the saved-data figures.

```sh
python -m pip install -r requirements.txt
python -W error -m pytest -q -p no:cacheprovider
python -W error run.py --input inputs.json --output output
python plot.py --results output/result.json --output output
```

`results/` in a release is the preserved example. Choose a fresh `output/` directory for reproduction. The runner rejects a nonempty output directory to preserve failures. It saves returned states/linear candidates before reference comparisons, updates result.json after every principal record, and retains the current nonlinear/trial state and latest operator input/output on caught exceptions. It does not claim to capture unwritten live arrays after SIGKILL. No network access, private checkout or independent reference regeneration is needed for the primary runner.

## Three scopes

**62 — diffusion-discrete-adjoint.** Actual centered-space backward Euler solves use 7/15 interior nodes and64/128/256 steps to T=.1. The reverse recurrence uses the coordinate transpose, including the terminal h weight. Tangent derivatives, all predetermined finite-difference steps and independent Decimal modes are separate checks. Full-storage and checkpoint/replay ownership windows are separate: the full trajectory is serialized and all its ndarray aliases released before checkpoint evolution. During the checkpoint window, checkpoints plus a16-step replay block and six n-vectors use at most40n evolving elements at N256. Static factors/model arrays are separately listed and included in total owned numeric bytes in both windows. Reference arrays and final validation NPZ assembly are created afterward. Serialization-library buffers are not scientific arrays, and the ledger is not process RSS. Replay states are streamed to disk and then compared byte-for-byte with the full trajectory. This is a fixed-block schedule, not optimal checkpointing or CVODES ASA.

**63 — bratu-fold-sensitivity.** Six lower-branch points use n31/63 and delta=.1/.01/.001 below a separately qualified **discrete** fold. The continuum cosh family/fold is background, not the exact finite-difference solution. Zero-start loose and strict state solves isolate nonlinear-state error from the linear study. The unchanged callable GMRES numerical body comes from the previously qualified Bratu JFNK implementation, including the operator-output alias fix. For both tangent and adjoint, rtol1e-4 and1e-8 must meet the actual true-residual targets. Requested1e-12 is observational: its exact last returned candidate, target_met=false when appropriate, raw termination and history are retained. It is never relabelled converged or replaced by a direct reference. Independent shooting-gradient accuracy is still required. The componentwise roundoff estimate and smallest Jacobian eigenvalue are floating diagnostics, not certified intervals or proof of the cause of stagnation. Finite-reference residual identities retain the direct tangent/adjoint residuals and the approximate-adjoint cross term. All fixed finite-difference curves are saved; no best step is selected for success.

**64 — bratu-distributed-vjp.** At n63, m8/16/32 coefficient controls use a=2+B theta. Bv gathers from two local entries per node; B transpose scatter-adds repeated contributions. Endpoint coefficient controls are not the zero Dirichlet state endpoints. The primary path constructs no n-by-m B or full sensitivity matrix. Named persistent arrays and the fixed GMRES n-by25/n-by24 workspace are reported; this inventory is not a measured peak RSS. One and three objectives on the same solved state actually share one Poisson factor, with its build/solve counts recorded. The state solver has its own separately counted factor. Dense hats and m banded tangent RHS occur only in the post-primary independent-reference window. This verifies derivatives of the same discrete model, not a separate physical forward-PDE oracle or general AD. Actual Bratu J is symmetric; a separate nonsymmetric tridiagonal control tests transpose signs. The m2 affine identity uses theta endpoints[a-b-2,a+b-2], not coefficient endpoints[a-b,a+b].

## References and qualification

The reference-only qualifier imports no primary forward/Newton/VJP operator. Its67 fixed checks cover scalar Decimal50/80 modes and independent geometric formulas; discrete shooting/fold equations, an independent Decimal Thomas-Newton solution and the n1 exact discrete fold; and float banded solves against Decimal elimination including a nonsymmetric matrix. The separate external30s qualification budget is not part of the public primary120s budget. The primary reads only the qualified cache and checks its input/acceptance/source/cache digests. Precision agreement is finite numerical qualification, not interval certification.

source-reading.json records exactly selected official/author-hosted reading and the access date. Unknown publication years remain unspecified; access dates are not publication dates. The new recurrences, identities and local-hat formulas are authored derivations in DERIVATION.md. JAX is terminology only and is not a dependency; SUNDIALS is background for the checkpoint/adjoint distinction and is not executed.

The fixed primary inventory is32 meaningful pytest tests,15 principal records,141 native-boolean gates (59/55/27),18 diffusion finite-difference evolutions,36 fold finite-difference states and18 distributed-control finite-difference states. The actual main plus pytest has one shared120s external deadline; no parameter sweep, hidden retry, seed/window selection or postfailure acceptance relaxation is permitted. Runtime is unmeasured at this source freeze.

## 日本語の範囲説明

本配布は固定入力の教育用3候補です。62は時間離散写像の随伴とcheckpointの所有配列、63は連続foldとは異なる離散fold近傍の感度、64は局所係数作用の行列非形成VJPを扱います。32pytest・141判定・独立67参照判定は計画件数で、実合否と実時間はレシートへ記録します。1e-12の残差未達は未達のまま保存し、独立勾配の精度判定と区別します。失敗時の入力・source・全候補・ログを保存し、公差や固定入力を後から緩めません。図は保存された1次元場・勾配・誤差・実solve回数だけから描き、plot.pyはsolverや参照生成器をimportしません。
