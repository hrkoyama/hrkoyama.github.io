# Stochastic differential equations / 確率微分方程式

Status: educational-example

Distinguish stochastic-integration conventions and strong/weak errors.

確率積分の規約と強・弱誤差を区別する。

Euler–Maruyama for scalar geometric Brownian motion. Coarse/fine steps and analytic endpoints share the same Brownian paths; measure strong RMS error across 4096 paths. Does not validate general SDEs, MCMC or weak convergence order.

Other names: SDE, SDE法, stochastic differential equation, 確率微分方程式法

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/sde/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/sde/



- Reference: https://doi.org/10.1007/bf02846028 — Method-specific source; see the detailed reading for source role and actual review depth.
- Reference: https://doi.org/10.1137/s0036144500378302 — Method-specific source; see the detailed reading for source role and actual review depth.

Scoped example: Euler–Maruyama for scalar geometric Brownian motion. Coarse/fine steps and analytic endpoints share the same Brownian paths; measure strong RMS error across 4096 paths. Does not validate general SDEs, MCMC or weak convergence order.

Code: https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/models.py
Tests: https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/test_models.py
Download: https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/model-benchmarks-2026-11-22.zip
Verification: https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/verification.json

Common execution records: [{"id": "gbm-sde", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=ja#gbm-sde-ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=en#gbm-sde-en"}}]

Next: Add validation against another reference problem before extending application scope.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/sde/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/
