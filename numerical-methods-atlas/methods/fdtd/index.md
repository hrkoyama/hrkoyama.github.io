# Yee finite-difference time-domain method / Yee FDTD

Status: educational-example

Validate2D TMz vacuum modes, a dielectric interface and left/right x-PML against analytic references.

2次元TMzの真空モード、誘電体界面、左右x方向PMLを解析参照と検証。

Educational2D TMz: original vacuum periodic/PEC modes plus normal incidence at an ε₁=1,ε₂=4 dielectric interface and normal/oblique pulses with x-directed PML in a y-periodic strip. Fresnel solutions, continuum Fourier modes and same-Yee wide-domain references have distinct roles. Four-side/corner PML, oblique material-interface incidence, dispersive matter and3D remain unvalidated.

Other names: FDTD法, finite difference time domain, 有限差分時間領域法, Yee法

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/fdtd/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/fdtd/



- Reference: https://doi.org/10.1109/tap.1966.1138693 — Method-specific source; see the detailed reading for source role and actual review depth.
- Reference: https://arxiv.org/abs/1705.02274v2 — Research preprint v2; energy Eq26 and strict CFL Eq35 consulted. Not a claim to implement its subgridding method.
- Reference: https://doi.org/10.1006/jcph.1994.1159 — Original split-field PML publication: bibliographic identity and abstract checked. Original full text was not available for inspection. The implemented reduction and discrete balance are derived and tested separately; consult Johnson for the matched-layer interpretation.
- Reference: https://arxiv.org/abs/2108.05348v1 — Author notes, selected sections 4.1–4.2 and 7.1–7.3: matching electric and magnetic damping, anisotropic interpretation, discretization reflections and incidence limitations. Not a complete audit of every PML formulation.
- Reference: https://ocw.mit.edu/courses/res-6-002-electromagnetic-field-theory-a-problem-solving-approach-spring-2008/pages/about-this-book/ — Author textbook, selected sections 7-6-1 and 7-6-2, printed pages 522–524 (PDF pages 36–38): tangential E/H continuity, normal-incidence field reflection/transmission and impedance weighting of power. A textbook exposition, not an original Fresnel publication.

2D TMz Yee FDTD supplement: retained vacuum periodic/PEC modes, normal-incidence dielectric Fresnel scattering and matched x-directed PML in a y-periodic strip. Analytic fields, finite-layer return waveforms, grid refinement and independent energy/work/flux budgets are checked separately.

- Code: https://hrkoyama.github.io/code/fdtd/2026-11-22-r2/solver.py
- Code: https://hrkoyama.github.io/code/fdtd/2026-11-22-r2/run.py
- Code: https://hrkoyama.github.io/code/fdtd/2026-11-22-r2/scattering.py
- Code: https://hrkoyama.github.io/code/fdtd/2026-11-22-r2/run_scattering.py

- Tests: https://hrkoyama.github.io/code/fdtd/2026-11-22-r2/test_fdtd.py
- Tests: https://hrkoyama.github.io/code/fdtd/2026-11-22-r2/test_scattering.py

Download: https://hrkoyama.github.io/code/fdtd/2026-11-22-r2/fdtd-2026-11-22-r2.zip
Manifest: https://hrkoyama.github.io/code/fdtd/2026-11-22-r2/source-manifest.json
Verification: https://hrkoyama.github.io/code/fdtd/2026-11-22-r2/verification.json

- periodic-wave: https://hrkoyama.github.io/code/fdtd/2026-11-22-r2/results/periodic-wave/result.json
- pec-cavity: https://hrkoyama.github.io/code/fdtd/2026-11-22-r2/results/pec-cavity/result.json
- dielectric-interface: https://hrkoyama.github.io/code/fdtd/2026-11-22-r2/results/dielectric-interface/result.json
- pml-pulse: https://hrkoyama.github.io/code/fdtd/2026-11-22-r2/results/pml-pulse/result.json

Commands (from extracted supplement):

```sh
python -m pip install -r requirements.txt
python -m pytest -q test_fdtd.py test_scattering.py
python run.py --input inputs/periodic-wave.json --output rerun-periodic-wave
python run.py --input inputs/pec-cavity.json --output rerun-pec-cavity
python run_scattering.py --input inputs/dielectric-interface.json --output rerun-dielectric-interface
python run_scattering.py --input inputs/pml-pulse.json --output rerun-pml-pulse
```

Next: Separately validate oblique material-interface incidence, four-side/corner PML and grazing incidence.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/fdtd/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/
