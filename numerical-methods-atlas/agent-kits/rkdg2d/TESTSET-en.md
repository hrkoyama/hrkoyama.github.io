# 2D Euler RKDG: code and fixed tests for AI agents

Release **2026-11-23-r1**. [Atlas entry](https://hrkoyama.github.io/numerical-methods-atlas/agent-kits/rkdg2d/) / [日本語](https://hrkoyama.github.io/numerical-methods-atlas/agent-kits/rkdg2d/TESTSET.md) / [public machine-readable manifest](https://hrkoyama.github.io/numerical-methods-atlas/agent-kits/rkdg2d/manifest.json).

Give this Markdown to your AI agent when you want a Cartesian DG solver for two-dimensional compressible Euler flow. Obtain working Atlas code, frozen inputs, independent references and evaluators. Develop a separate candidate, then run the same checks. This is a bounded development workflow using supplied code, not a guarantee that arbitrary AI-generated scientific code succeeds.

## Download, verify and run a first actual calculation

Computation requires Python >=3.9 and NumPy. The checked environment is Python3.9.6 / NumPy2.0.2; this does not establish testing of every supported version. The commands also use curl, unzip and a SHA256 utility. Start in a new working directory.

```bash
mkdir rkdg-atlas-2026-11-23-r1
cd rkdg-atlas-2026-11-23-r1
curl -fL https://hrkoyama.github.io/code/rkdg2d/2026-11-23-r1/atlas-rkdg-agent-kit.zip -o atlas-rkdg-agent-kit.zip
curl -fL https://hrkoyama.github.io/code/rkdg2d/2026-11-23-r1/atlas-rkdg-agent-kit.zip.sha256 -o atlas-rkdg-agent-kit.zip.sha256
sha256sum -c atlas-rkdg-agent-kit.zip.sha256
# On macOS, if sha256sum is absent, replace the previous line with:
# shasum -a 256 -c atlas-rkdg-agent-kit.zip.sha256
unzip -q atlas-rkdg-agent-kit.zip
cd atlas-rkdg-agent-kit
sha256sum -c SHA256SUMS.txt
# macOS: shasum -a 256 -c SHA256SUMS.txt
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-verified.txt
.venv/bin/python scripts/run_rkdg_smoke.py --output outputs/fresh-smoke.json
```

Stop on a checksum mismatch and investigate the downloaded version. Internal SHA256SUMS.txt covers all distributed files except itself. In the remaining commands, replace `python` with `.venv/bin/python`; use the corresponding virtual-environment executable on Windows.

The smoke test performs **six fresh PDE evolutions**: p1/p2/p3, 6² to12² cells, t=0.02. The oblique entropy wave varies in both x and y and exercises the fully2D operator. Density is independently reconstructed from raw modes, without solver.sample, and compared with the exact solution. The test checks coarse-grid L2 order, conservation and positivity at declared sample points. Success means exit0 and `outputs/fresh-smoke.json` containing `passed=true`. **This does not qualify the original48 cases.** Actual elapsed time is recorded as `wall_seconds`, without a runtime guarantee.

## Supplied numerics and fixed identities

- 2D ideal-gas Euler, gamma1.4, uniform Cartesian mesh, tensor Legendre Q1/Q2/Q3 (p=1/2/3); HLL; density-normalized characteristic TVB/minmod M100; cell-average-preserving positivity scaling; SSPRK(5,4).
- Current completed candidate: `agent-kits/rkdg2d/generated/rkdg2d.py`, SHA256 `4ed984a01c42fe9bb657c09c61361b086682d6aa611e9f478bf996c0b29b81d4`.
- Original48 rules: `validation/rkdg/acceptance.json`, SHA256 `7219904b7460efa32f1f1ea03b6cd729e9e3b200e7c60643d0cfa08ec866d4af`.
- Waveform4 rules: `validation/rkdg/resolution-acceptance.json`, SHA256 `275c7ffc386bc4cc791148b498e3872e9a67398f2a175bd3ae9a418559cf63c3`.
- Supplemental reflection6 rules: `validation/rkdg/reflection-acceptance.json`, SHA256 `ab7986e1eaf768f63fb239bf5a8d766d4c4fc5778389bdc42b5eb294594bf18a`.

Current results are under `outputs/rkdg-2026-11-23/accepted-v3/`. **Original48 PASS and waveform4 PASS; the later reverse-x supplement passes5/6 and is FAIL overall.** Shu–Osher p3 has a normalized maximum discrepancy1.4833e-10 against the frozen1e-10 limit. Both the limit and failure record are retained. Do not describe the original48+4 success as a success of every supplemental test.

`accepted/`, `manifest-v2.json` and `generated/assembly-notes.txt` retain historical candidates, failures and repairs. Identify the current source using4ed984… above. The incomplete `starter/rkdg2d.py` belongs to the assembly exercise; use the completed candidate for first execution. Read RELEASE.json and BUILD-STATE.json for release and verification scope.

## Reevaluate saved results without running the PDE

From the extracted root, after the package checksum check:

```bash
python scripts/package_rkdg_agent_release.py --verify-only
python validation/rkdg/evaluate.py outputs/rkdg-2026-11-23/accepted-v3/metrics.json --solver agent-kits/rkdg2d/generated/rkdg2d.py --output outputs/saved-verdict.json
python validation/rkdg/resolution.py --campaign outputs/rkdg-2026-11-23/accepted-v3 --solver agent-kits/rkdg2d/generated/rkdg2d.py --output outputs/saved-resolution-verdict.json
```

`--verify-only` also checks saved source/array bindings and all12 reflection arrays. Exit0 and `integrity_passed=true` mean evidence integrity; `reflection_supplement.qualification_passed=false` (5/6 PASS) is retained. This is not an all-scientific-tests PASS. The two evaluators must then exit0 with `passed=true` and `failures=[]`. The original evaluator checks recorded metrics and source identity; the waveform evaluator reevaluates saved arrays. Report these as saved-result checks, not fresh PDE calculations. To run structural, evaluator and interchange regression checks, install `python -m pip install -r requirements-tests-verified.txt`, then run `python -m pytest -q tests/test_rkdg*.py`. These do not replace a fresh full scientific campaign.

## Create a candidate and run original48 plus waveform4 afresh

Copy the candidate; never modify the frozen criteria, evaluators, references or historical outputs.

```bash
mkdir candidate
cp agent-kits/rkdg2d/generated/rkdg2d.py candidate/rkdg2d.py
python scripts/run_rkdg_smoke.py --solver candidate/rkdg2d.py --output outputs/candidate-smoke.json
# If the candidate changes, rerun smoke into another unused output path.
python scripts/run_rkdg_campaign.py --solver candidate/rkdg2d.py --output outputs/candidate-full
python scripts/run_rkdg_negative_control.py --solver candidate/rkdg2d.py --campaign outputs/candidate-full --output outputs/candidate-negative
python validation/rkdg/evaluate.py outputs/candidate-full/metrics.json --solver candidate/rkdg2d.py --output outputs/candidate-full/verdict.json
python validation/rkdg/resolution.py --campaign outputs/candidate-full --solver candidate/rkdg2d.py --output outputs/candidate-full/resolution-verdict.json
```

The full campaign is an **explicit opt-in fresh scientific calculation**, not the default first action. Fine temporal comparisons and a faulty solver also run, so it is heavier than smoke. End-to-end runtime has not been measured as a single workflow and depends on the machine. Use the same candidate path for all four commands. Keep output paths unused and inside the extracted root. Retain interrupted and failed runs.

The campaign's exit0 means computation finished; subsequent evaluators determine qualification. The original verdict reports `case_counts`: smooth12, directional24, double_mach9, temporal3, negative_controls1 (48 scientific cases plus a fault control). The supplemental `diagnostic_checks=4` reevaluates existing Shu–Osher arrays, not four new PDE runs. Require exit0 / `passed=true` from both evaluators and `rejected=true` in `outputs/candidate-negative/control-row.json`; retain evidence.json.

Fault injection identifies the supplied candidate's y-flux source line. If a refactor prevents injection, report the control as unexecuted and implement an adapter that introduces the equivalent y-flux fault. Do not edit result JSON or the evaluator to manufacture success. Reject missing cases, source/hash mismatch, nonfinite values and threshold violations.

## Six fresh reverse-x runs: historical v3 source only

The recorded verdict is `outputs/rkdg-2026-11-23/x-reflection/verdict.json`; arrays are in its arrays/ directory. Fresh initial states reflect the entire problem, including Shu–Osher phase, x momentum and Legendre x-mode parity. These results are not merely a flipped plot.

```bash
python scripts/run_rkdg_reflection.py --solver agent-kits/rkdg2d/generated/rkdg2d.py --forward outputs/rkdg-2026-11-23/accepted-v3 --output outputs/fresh-reflection --workers 2
```

This runs six fresh PDE evolutions. **The recorded environment gives expected exit1, `passed=false`,5/6 PASS.** Record what the new environment actually measures; floating-point differences can change this borderline result. An expected failure is still a failure. This historical runner pins the candidate to SHA4ed984… and cannot test an edited candidate. A new candidate needs a separately versioned runner, fresh matching forward data and provenance, while preserving the same immutable comparison criteria. Keep --output and --forward under the extracted root.

## Language ports and MPI

`agent-kits/rkdg2d/PORT-AND-MPI-TASK.txt` is the task template. The common output contract is in `docs/rkdg-interchange-en.md` and Japanese `docs/rkdg-interchange.md`. Write a JSON manifest plus owned-cell modal CSV. Conserved variables are rho,rho_u,rho_v,energy; Legendre normalization is P_m(1)=1; mode00 is the cell mean. Emit every Qp mode once, excluding ghost/halo cells.

```text
global_i,global_j,mode_i,mode_j,rho,rho_u,rho_v,energy
```

Examples for outputs actually produced by a port (`port/` is not bundled):

```bash
python validation/rkdg/interchange.py check-reference outputs/rkdg-2026-11-23/accepted-v3/arrays/smooth-p2-n8.npz port/smooth-p2-n8/manifest.json --output port/reference-comparison.json
python validation/rkdg/interchange.py compare port/serial/manifest.json port/mpi4/manifest.json --output port/mpi4-comparison.json
```

Success requires exit0 and `passed=true`. Default coefficient tolerances atol1e-11 / rtol1e-9 apply to I/O equivalence; they do not relax physical accuracy rules. Supply boundary-flux diagnostics and require `conservation_checked=true`; a false value caused by omitted diagnostics does not verify conservation.

The Python campaign imports a Python module exposing DG2D; it does not directly run a foreign-language executable. The port must supply an adapter to launch runs, read its output and produce independently evaluated metrics.json for every fixed case. One matching output is not a48-case qualification. For MPI, actually launch1/2/4 ranks and test x/y and uneven partitions, global CFL, stage-wise halos/boundary times, physical-boundary fluxes and owned-cell-only reductions. Assign `execution_kind="solver-output"` only to actual PDE output.

Bundled executed examples are C++17 analytic-polynomial I/O and1/2/4-partition fixtures. **A foreign-language PDE solver and an actual MPI PDE runtime have not been executed.** Never report fixtures as MPI execution.

## Limits, references and reporting

Exact1D inputs in x/y use an analytic invariant reduction. Oblique waves, Double Mach and smoke exercise fully2D coupling. Do not demand global2/3/4-order convergence across shocks. Double Mach is a broad-structure comparison with an independent FV reference, not a fine-vortex convergence result. Positivity is checked only at specified quadrature, face and corner points. Waveform4 covers p2/p3, x/y,256 cells, ROI[1.2,2.2], requiring relativeL1<=.08, mean-removed standard-deviation ratio>=.5 and correlation>=.8 simultaneously.

Frozen reference arrays, provenance, inputs and hashes are under validation/rkdg/references/. The Shu–Osher reference-grid difference is a global relative-densityL1 uncertainty, not a pointwise exact error bound. Reference regeneration is normally unnecessary.

Separate fresh PDE runs, saved-result reevaluation, I/O fixtures and unexecuted work. Record actual source SHA, commands, exit codes, environment, input/output hashes, errors/orders, conservation residuals, positivity and failures. The bilingual docs/rkdg.md and docs/rkdg-en.md cite nine primary works: Sod(1978), HLL(1983), Woodward–Colella(1984), Shu–Osher(1989), Toro et al.(1994), Jiang–Shu(1996), Cockburn–Shu(1998), Spiteri–Ruuth(2002), Zhang–Shu(2010).

The supplied original code and accompanying documentation use the MIT license in LICENSE. Preserve its copyright and permission text. Algorithm citations and code permission have different roles. No cited paper's full text, private poster or unpublished manuscript is bundled.
