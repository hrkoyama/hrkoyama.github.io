# ODE adaptivity, stiffness and boundary splitting

The preserved first primary study completed 39 pytest tests and all 60 runs, but **only 208 of 209 original targets were met**. The mu = 1 tight adaptive van der Pol run had sampled maximum error **4.535633779e-5**, exceeding the unchanged **2e-5 global goal**, although all accepted local error ratios were at most one. The original result remains FAIL in `history/main01-original-study/original-result.json`.

This is an explicitly **post-measurement reporting-scope revision**, not a numerical repair. All numerical kernels, inputs, local tolerances, controller settings, observation times and original acceptance thresholds are unchanged. The current protocol requires the other 208 original checks plus three clearly named reporting, accepted-local-control and history checks (211 total). A reporting PASS does **not** mean that all 209 original numerical goals were met. Each run retains the complete original decision map, including any false result, as `original_target_results`, with `original_target_summary` and the unchanged acceptance SHA. The current mu = 1 global decision is measured again and may be true or false; no expected-failure mask is imposed.

At this revision's pre-execution freeze, the new reporting protocol and its 41 tests have not yet run. The independent reference qualification previously passed 52 checks. Current execution status belongs in `results/result.json` and the package `verification.json`; neither the reference result nor the old 208/209 study is a current all-targets PASS.

Four runnable cases cover three topics. `inputs.json` enumerates exactly 60 primary runs: eight Robertson, 16 van der Pol, eight RK45 and 28 boundary-splitting runs. Earlier drafts, distributions, inputs, criteria and histories are retained separately.

## Reproduce

Use Python 3.12 and the three exact scientific dependencies in `requirements.txt`. Main reads the bundled qualified reference cache and never regenerates reference trajectories. Saved `results` are examples; rerun into a **new directory**:

```sh
python -m pip install -r requirements.txt
python -B -W error -m pytest -q -p no:cacheprovider
python -B -W error run.py --input inputs.json --output output
python -m pip install -r requirements-plotting.txt
python plot.py --results output/result.json --output output
```

Set `OPENBLAS_NUM_THREADS=1`, `OMP_NUM_THREADS=1`, `MKL_NUM_THREADS=1`, `VECLIB_MAXIMUM_THREADS=1` and `PYTHONDONTWRITEBYTECODE=1`. The group has one shared 120-second pytest-plus-main ceiling. The initial complete attempt took 3.066 seconds including its 39 pytest tests and the failed global goal. The new reporting revision runtime is unmeasured; the 55-second planning target is neither an acceptance allowance nor a runtime guarantee. Reference qualification and plotting have separate budgets and receipts. Retries are never automatic.

## Stiff trajectories

Robertson uses the standard nondimensional three-species model, initially (1, 0, 0), only on 0 <= t <= 0.4. Selected official SUNDIALS model, RHS and Jacobian sections were read. The original Robertson paper remains unread, and this is not a reproduction of its long-time 4e10 benchmark. Van der Pol starts at (2, 0), uses mu = 1 and 100 and ends at T = 2. It covers early stiffness rather than a full large-mu relaxation cycle.

BDF2 has a backward-Euler startup on the same fixed grid. SDIRK2 uses gamma = 1 - 1/sqrt(2). The stage residual is `z - base - c*f(t,z)`. Newton stopping and Armijo use the same weighted maximum norm, `max(abs(residual)/error_weights)`, with the frozen tolerance and caps. Analytic Jacobian factors are refreshed every third correction and reused only within that one implicit stage. They are not shared across stages, timesteps, parameters or independent references. Actual RHS, Jacobian, factorization and solve counters report the work. No clipping, normalization or mass projection is used.

Adaptive SDIRK2 computes one full step and two half steps. It accepts the two-half-step result and estimates local error by their difference divided by three. Its scaled ratio uses an RMS norm, distinct from the Newton norm. Steps stop at the fixed common observation times. Accuracy is sampled at 22 Robertson or 21 van der Pol times, not claimed as an all-time supremum. Every accepted state is retained for conservation, positivity and boundedness checks. Intermediate Newton candidates, completed implicit stages and accepted solution states remain distinct. An L-stable method is not generically positivity preserving.

The independent reference definitions use SciPy 1.14.1 Radau, tighter Radau and variable-order BDF. They do not import the primary RHS or integrators. Reference Jacobians first pass complex-step controls. The algorithms share NumPy, SciPy and LAPACK infrastructure; agreement is a finite numerical qualification, not independent physical truth. Actual error, nonlinear residual, reference discrepancy and local tolerance have separate meanings and criteria.

## RK45, dense output and events

Dormand–Prince 5(4) and quartic coefficient expressions are adapted from the fixed SciPy 1.14.1 source, with BSD notices in `SCIPY-LICENSE.txt`. The primary stage, controller, cache, interpolation and event code is inspectable. SciPy RK45 is not used as both candidate and oracle. The original Dormand–Prince 1980 and Shampine 1986 papers remain unread beyond bibliography; the selected official source and license were read.

Analytic damped rotation supplies independent truth. Accepted endpoints, 97 off-mesh samples and the simple crossings pi/6 downward and pi/2 upward have separate error gates. A prescribed first step avoids hidden initial-step calls: actual RHS work must equal `1 + 6*attempted_steps`, including rejected trials. Rejected endpoints never replace the accepted starting derivative. Dense and event queries make no RHS calls. A terminal interior-root output is distinct from the accepted full-step endpoint, and both are retained. Generic resets, tangential roots and multiple crossings inside one step are outside the claimed scope. Causal component tests check the stated cache, ownership and failure controls.

## Nonperiodic boundary splitting

The authored linear example solves `u_t = u_xx + u` on [0, 1], with both boundary values equal to one. Its continuum solution is

    cos(x - 1/2)/cos(1/2) + 0.1*exp((1 - pi*pi)*t)*sin(pi*x).

Fields are interior node values, not cell means. For `w = u - 1`, both compositions approximate the same finite-difference system, `wprime = L_h*w + w + 1`. The unmodified subflows are `(L_h*w, w + 1)`, while the boundary-compatible subflows are `(L_h*w + 1, w)`. Diffusion uses a nonperiodic Dirichlet DST-I semigroup with the exact affine source integral. It is not periodic Fourier diffusion. Every field is actually stepped through the subflows; an analytic mode answer is never substituted for the primary evolution.

The unmodified reaction trace moves a boundary value of one to exp(dt). This mismatch is recorded without resetting interior states. Strang ends with diffusion and its prescribed trace. Lie ends with reaction in this packet, so its nonzero final reaction-trace mismatch is reported rather than called boundary compatible. Lie accuracy compares interior unknowns. Field plots focus on the two Strang variants.

Independent sparse affine exponential actions in the original u variables are checked against separately coded sine-series solutions. Temporal error uses this same spatial discretization. Spatial error compares the qualified finite-difference reference with the analytic continuum field. The fixed n and timestep regime tests observed order loss and restoration. At a fixed finite n, sufficiently small timesteps can recover ordinary matrix asymptotics; no universal order-loss statement follows. Only selected extracted sections of the Einkemmer–Ostermann 2014 preprint were read. This linear constant-boundary example does not reproduce its nonlinear tables or validate a general time-dependent boundary theorem.

## Saved data and failure scope

Every completed run has finite numeric records and CSV, with full accepted states in NPZ saved before diagnostics. Current tracing keeps bounded, owned latest candidate, base, residual and Jacobian contexts by role. It does not serialize full successful Newton or line-search histories. Accepted states are journaled in blocks of 32 and flushed. Numbered array snapshots are saved every 256 accepted steps and on failure or ordinary close, with a stable latest alias. Ordinary exceptions flush pending accepted states and the last owned contexts. A SIGKILL can retain only data already written.

The earlier retention revision superseded an unexecuted promise of full successful stage histories. This later reporting revision keeps every numerical update, all 60 input rows, tolerances and the original 209 threshold decisions unchanged. It changes only the validation role of the one explicitly named global goal: that goal is still evaluated and preserved, but is not required to be true by the current reporting protocol. A failed candidate's nonfinite array or scalar is saved as raw NPZ data; JSON uses an explicit array descriptor and invalid flag. It is not converted to a finite success value. A later diagnostic failure retains the entered case and completed rows and returns FAIL.

The reference stage has a separate 30-second cap and 52 checks. If a monolithic SciPy solve raises, the last owned RHS or Jacobian callback state is saved. Its unreturned accepted history is unavailable. A returned failed or partial solution is saved before diagnostics. Reference regeneration is explicit and separate from main and plot:

```sh
python -B -W error references/qualify.py --output fresh-reference-check
```

A fresh directory is required. Qualified caches bind input, acceptance and generator hashes, and the main source contract also binds every cached file. The 52 reference checks, primary case gates and pytest counts are separate. Never install a failed or partial qualification as a cache.

`plot.py` reads saved arrays and records only. It accepts a result directory or `result.json`, including the canonical `--results results/result.json --output results` form. It renders a scientific main and a separate gallery preview per case in PNG, SVG and PDF. Figures show actual concentration or phase data, acceptance/rejection and event errors, or a one-dimensional field across saved times with separate time and space errors. A time-space image is not a two-dimensional flow. Zero values are retained with labeled symlog axes where appropriate.

Case metadata carries six bilingual fields, actual method IDs, preview membership and honest reading scope. Detailed inputs, references and limits remain in this distribution. No private authoring path or work queue is included.


## Why the local control did not meet the original global goal

The accepted solution is the two-half-step SDIRK2 value. For an order-two method the local estimate `(two_half_steps - full_step)/3` and controller exponent -1/3 are consistent. A bound on this scaled local RMS estimate is not a theorem bounding the accumulated sampled global maximum error. The preserved mu = 1 tight run accepted 89 steps, rejected two trials, had no failed implicit stages, and had a maximum accepted local ratio of 0.8371802053. Its global error nevertheless exceeded 2e-5. Tighter local tolerances reduced the error relative to the loose run, but did not achieve that separate requested bound.

The source does not increase the threshold, retune safety, add steps or substitute an extrapolated state. `reporting-policy.json` permits a change of reporting role only for `vdp-mu1-adaptive-tight:accuracy`; every other original check remains required. The three new checks validate the actual outcome disclosure, accepted local controls, and the exact original failure evidence. They do not establish the missed global accuracy goal.

The public history contains exact original source files with inert `.py.txt`/`.json.txt` names and a path/hash map, the original failed result, the failed-run trajectory and trial log. Its receipt summary is explicitly curated and cites the original receipt SHA; it is not that byte-identical receipt. Complete logs and raw data for all 60 original runs remain preserved privately. Historical pre-execution statements in those snapshots describe their original freeze, not the current release.

日本語：初回は元の209目標中208件のみ達成し、μ=1の厳しい適応設定で大域誤差4.535633779e-5が目標2e-5を超えました。局所制御の成功と大域目標の未達を別々に示す、測定後の報告範囲変更です。元の偽値・入力・全閾値・数値コードは保持し、新しい報告検証の合格を元209目標すべての達成とは扱いません。
