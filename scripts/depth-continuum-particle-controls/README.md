# Fixed continuum and particle examples

Five small scientific cases cover a skew-grid ALE piston, prescribed spherical
transport, axisymmetric spherical shallow-water balance, a Gaussian-convolution
GSPH Sod-type problem, and uniform-pressure/acoustic particle controls.
`inputs.json` specifies the fixed protocol; `acceptance.json` declares criteria.
`source-reading.json` gives primary-source read limits and `PROTOCOL.md` explains
sampling, reference independence, deliberate wrong-formula controls and scope.

Use a compatible existing Python runtime. The scientific code uses NumPy and
pytest, with no SciPy import. The common public verifier also pins SciPy for its
other groups. Matplotlib is needed only for plotting saved arrays.

Run `python run.py --input inputs.json --output results` with a fresh results
directory, then `python -m pytest -q test_components.py`. Generate figures and
CSV exports with `python plot.py --results results/result.json --output results`.
The main calculation has a shared cooperative 90-second budget and fixed step,
root and smoothing-length iteration caps. The surrounding verifier retains its
own deadline. No installation or persistent process is started by these scripts.

Measured outcomes belong to `results/result.json`, the source manifest and the
verification receipt. Source recipes do not assert that an execution succeeded.
Failures preserve raw candidate arrays and explicit diagnostic labels. Existing
result directories are never reused by the runner. The accompanying reference
and metadata registrations are separate maintenance work, not extra simulations.
