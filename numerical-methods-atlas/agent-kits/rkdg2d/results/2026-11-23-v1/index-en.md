# Measured RKDG development and repair prompts

One assembly trial and one repair trial used the Japanese templates. Both candidates passed the original 48 scientific cases and four waveform diagnostics, and rejected an actually executed faulty control.

- Assemble from the starter: Original 48 + waveform 4 PASS; fault rejected; 2 repairs; About 49 min (2949.835 s); SHA256 `c8c6b11b688a50a3082a9dedb6b8a663b55a7cd5358aa4ac20166b672299cc2a`.
- Repair an injected defect: Original 48 + waveform 4 PASS; fault rejected; 1 repairs; About 48 min (2866.545 s); SHA256 `4ed984a01c42fe9bb657c09c61361b086682d6aa611e9f478bf996c0b29b81d4`.

Repair counts cover numerical-solver revisions after initial implementation. Environment and auxiliary-script corrections are recorded separately. Reported elapsed time includes setup, development/repair, fresh computation and validation. Trials overlapped on one Mac and are not a model-speed comparison.

Monetary charges, billable tokens and the precise inherited model ID were unavailable. Unavailable cost is not zero. Lower-cost-model comparisons, Atlas-free controls and measured cost savings are outside this pilot.

- Each candidate was selected explicitly with --solver for fresh computation of 12 oblique-wave, 24 x/y Sod/Shu–Osher, 9 Double Mach and 3 temporal-refinement rows. Each campaign produced 49 PDE arrays, including an additional temporal reference.

- Four waveform diagnostics evaluate local error, standard-deviation ratio and correlation from stored p2/p3 x/y outputs; they are not four additional PDE evolutions.

- An independently held distribution supplied the frozen evaluators. The supervisor re-evaluated original 48/waveform 4 and matched 240 reconstructed metrics from each set of 49 arrays. All 295 distributed files, scientific criteria and references remained unchanged. A real faulty-y-flux computation was rejected by the fixed accuracy criteria.

- Both candidates gave finest-pair L2 orders 2.0013 / 2.9747 / 4.0088. No global high-order convergence across shocks is claimed. Double Mach checks broad structure against an independent FV reference; positivity covers the declared quadrature, face and corner points.

The unchanged published Japanese Markdown templates received fixed task context and were run once each by separate agents without inherited conversation history. The supervisor acquired inputs and prepared the environment; subjects implemented/repaired and executed the code.

Assembly started with the unfinished starter and implemented SSPRK(5,4), characteristic TVB and an invariant 1D restriction. A short directional diagnostic prompted two repairs before the full suite. The repair task used one pre-injected SSPRK coefficient defect with its cause withheld. The agent diagnosed a 0.99dt constant-ODE increment and repaired it once.

Reading completed implementations was prohibited by instructions, without OS-enforced read isolation. One trial per task does not measure a general success rate or arbitrary bug-repair ability.

Exactly 1D x/y inputs use an analytic restriction; oblique waves and Double Mach exercise full 2D coupling. The historical reversed-x result remains 5/6, outside this qualification. No MPI, foreign-language PDE or new quantum-chemistry computation was performed.

The 162 distribution-oriented pytest checks passed even with the unfinished candidate; candidate acceptance therefore used explicit --solver fresh runs and frozen evaluators.

NumPy2.0.2 reference-remap matmul warnings were retained and reproduced separately. Inputs/outputs were finite and matched an einsum contraction with zero maximum difference.

Supervisor audit v1 incorrectly required bitwise callback-endpoint equality and failed on the repair data. Audit v2 follows the existing solver closure rule of 4eps×max(1,|T|). Both data sets were rechecked, preserving the first audit failure. Scientific criteria and outputs were unchanged.

## Saved-data reassessment

SHA-verify and extract base kit r2 and the result ZIP separately. Run these commands from the result folder with NumPy2.0.2 and unused output paths. This reassesses saved arrays, not a fresh full PDE campaign.

```sh
python verify_saved.py --trial assembly --base /path/to/atlas-rkdg-agent-kit --output /path/to/new-audit
python verify_saved.py --trial repair --base /path/to/atlas-rkdg-agent-kit --output /path/to/new-audit
```

[ZIP](https://hrkoyama.github.io/code/rkdg2d/2026-11-23-pilot1/atlas-rkdg-agent-pilot.zip) / [SHA256](https://hrkoyama.github.io/code/rkdg2d/2026-11-23-pilot1/atlas-rkdg-agent-pilot.zip.sha256)

[Source kit / primary references](https://hrkoyama.github.io/numerical-methods-atlas/agent-kits/rkdg2d/?lang=en)
