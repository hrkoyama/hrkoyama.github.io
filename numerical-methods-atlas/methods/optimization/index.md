# Gradient and quasi-Newton optimization / 勾配法・準Newton法

Status: educational-example

Fit Bratu coefficients from synthetic observations and verify two-parameter adjoint gradients, regularization bias, data-sensitivity singular values and nonidentifiable observations.

Bratuの合成観測から係数を推定し、2パラメータの随伴勾配、正則化の偏り、観測感度の特異値と識別不能例を検証する。

Educational tests use small smooth lower-branch Bratu problems and fixed synthetic observations. They cover two spatial coefficients, Tikhonov regularization, local data-sensitivity SVD, rank loss with central observations and reflection ambiguity. Prior selection through regularization does not add observational information. Real data, high-dimensional function estimation, global uniqueness, statistical confidence intervals and quasi-Newton methods generally are outside scope.

Other names: 数値最適化, 勾配降下法, 準Newton法, 準ニュートン法, gradient descent, quasi Newton, Bratu, λ推定, パラメータ推定, 逆問題, inverse problem, parameter identification, projected gradient, Armijo, 複数パラメータ推定, 正則化, 識別可能性, Tikhonov regularization, identifiability, singular values, multi-parameter inverse problem

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/bratu-multi-inverse/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/bratu-multi-inverse/



- Reference: https://doi.org/10.1093/comjnl/13.3.317 — Method-specific source; see the detailed reading for source role and actual review depth.
- Reference: https://doi.org/10.2140/pjm.1966.16.1 — Original sufficient-decrease and backtracking construction; the detailed chapter distinguishes the local projected implementation from the original theorem.
- Reference: https://www.imm.dtu.dk/~pcha/Regutools/RTv4manual.pdf — Author official manual; the detailed chapter records the selected SVD and standard-form Tikhonov/nonzero-prior passages consulted. The local Bratu implementation is independent of the MATLAB toolbox.

Bratu inverse supplement: bounded projected adjoint-gradient fitting of one scalar parameter from fixed synthetic observations. Same-model consistency, continuous-observation grid bias and fixed-noise shifts are separate checks.

- Code: https://hrkoyama.github.io/code/bratu-inverse/2026-11-22/numart/bratu_inverse.py
- Code: https://hrkoyama.github.io/code/bratu-inverse/2026-11-22/numart/bratu_sensitivity.py
- Code: https://hrkoyama.github.io/code/bratu-inverse/2026-11-22/numart/autodiff.py
- Code: https://hrkoyama.github.io/code/bratu-inverse/2026-11-22/numart/krylov.py
- Code: https://hrkoyama.github.io/code/bratu-inverse/2026-11-22/scripts/build_bratu_inverse.py

- Tests: https://hrkoyama.github.io/code/bratu-inverse/2026-11-22/tests/test_bratu_inverse.py

Download: https://hrkoyama.github.io/code/bratu-inverse/2026-11-22/bratu-inverse-2026-11-22.zip
Manifest: https://hrkoyama.github.io/code/bratu-inverse/2026-11-22/source-manifest.json
Verification: https://hrkoyama.github.io/code/bratu-inverse/2026-11-22/verification.json
Measurements: https://hrkoyama.github.io/code/bratu-inverse/2026-11-22/docs/figures/bratu-inverse.json

Commands (from extracted supplement):

```sh
python -m pip install -r requirements.txt
python -m pytest -q tests/test_bratu_inverse.py
python scripts/build_bratu_inverse.py
```

Multi-parameter Bratu inverse supplement: two spatial coefficients, adjoint fitting, Tikhonov regularization and data-only SVD identifiability diagnostics. Regularization does not add observational information.

- Code: https://hrkoyama.github.io/code/bratu-multinverse/2026-11-22/numart/bratu_multinverse.py
- Code: https://hrkoyama.github.io/code/bratu-multinverse/2026-11-22/numart/bratu_inverse.py
- Code: https://hrkoyama.github.io/code/bratu-multinverse/2026-11-22/numart/bratu_sensitivity.py
- Code: https://hrkoyama.github.io/code/bratu-multinverse/2026-11-22/numart/autodiff.py
- Code: https://hrkoyama.github.io/code/bratu-multinverse/2026-11-22/numart/krylov.py
- Code: https://hrkoyama.github.io/code/bratu-multinverse/2026-11-22/scripts/build_bratu_multinverse.py

- Tests: https://hrkoyama.github.io/code/bratu-multinverse/2026-11-22/tests/test_bratu_multinverse.py

Download: https://hrkoyama.github.io/code/bratu-multinverse/2026-11-22/bratu-multinverse-2026-11-22.zip
Manifest: https://hrkoyama.github.io/code/bratu-multinverse/2026-11-22/source-manifest.json
Verification: https://hrkoyama.github.io/code/bratu-multinverse/2026-11-22/verification.json
Measurements: https://hrkoyama.github.io/code/bratu-multinverse/2026-11-22/docs/figures/bratu-multinverse.json

Commands (from extracted supplement):

```sh
python -m pip install -r requirements.txt
python -m pytest -q tests/test_bratu_multinverse.py
python scripts/build_bratu_multinverse.py
```

Next: Separate validation for data-driven regularization selection, many coefficients, real data and more general optimization methods.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/optimization/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/
