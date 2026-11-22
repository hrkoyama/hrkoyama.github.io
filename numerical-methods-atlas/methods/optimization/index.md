# Gradient and quasi-Newton optimization / 勾配法・準Newton法

Status: educational-example

Estimate Bratu lambda from synthetic observations and verify discrete-adjoint gradients with bounded projected-gradient optimization.

Bratu方程式の合成観測からλを推定し、離散随伴勾配と区間制約付き勾配法を検証する。

An educational one-parameter inverse problem on the smooth lower branch with fixed synthetic observations, bounded projected gradients and Armijo search. Same-discrete-model recovery, grid bias against continuous analytic observations and shifts under fixed noise are distinguished. Quasi-Newton methods, real data, branch identification and statistical confidence intervals are outside the verified scope.

Other names: 数値最適化, 勾配降下法, 準Newton法, 準ニュートン法, gradient descent, quasi Newton, Bratu, λ推定, パラメータ推定, 逆問題, inverse problem, parameter identification, projected gradient, Armijo

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/bratu-inverse/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/bratu-inverse/



- Reference: https://doi.org/10.1093/comjnl/13.3.317 — Method-specific source; see the detailed reading for source role and actual review depth.
- Reference: https://doi.org/10.2140/pjm.1966.16.1 — Original sufficient-decrease and backtracking construction; the detailed chapter distinguishes the local projected implementation from the original theorem.

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

Next: Independent validation of multiple parameters, regularization selection, real data and quasi-Newton methods.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/optimization/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/
