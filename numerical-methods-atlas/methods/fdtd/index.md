# Yee finite-difference time-domain method / Yee FDTD

Status: educational-example

Fixed-input Yee FDTD checks for vacuum, Fresnel interfaces, PML and 1D lossy/Lorentz slabs.

Yee FDTDの真空・Fresnel界面・PMLと一次元の損失・Lorentz分散板を固定入力で検証。

Educational Yee FDTD: retained vacuum/Fresnel/s-p/PML examples plus r6 1D normal-incidence Ohmic and passive Lorentz slabs. Spectral references, R/T, direct dissipation, material storage, modified/physical budgets and space/time refinement are separate checks. Not blanket validation of general dispersion, multiple resonances, oblique dispersive incidence, dispersive PML or general 2D/3D.

Other names: FDTD法, finite difference time domain, 有限差分時間領域法, Yee法

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/fdtd/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/fdtd/



- Reference: https://doi.org/10.1109/tap.1966.1138693 — Method-specific source; see the detailed reading for source role and actual review depth.
- Reference: https://arxiv.org/abs/1705.02274v2 — Research preprint v2; energy Eq26 and strict CFL Eq35 consulted. Not a claim to implement its subgridding method.
- Reference: https://doi.org/10.1006/jcph.1994.1159 — Original split-field PML publication: bibliographic identity and abstract checked. Original full text was not available for inspection. The implemented reduction and discrete balance are derived and tested separately; consult Johnson for the matched-layer interpretation.
- Reference: https://arxiv.org/abs/2108.05348v1 — Author notes, selected sections3.4,4.1–4.2 and7.1–7.3: independent x/y coordinate stretches and simultaneous corner damping, matching electric/magnetic rates, anisotropic interpretation, discretization reflections and incidence limitations. Not a complete audit of every PML formulation.
- Reference: https://ocw.mit.edu/courses/res-6-002-electromagnetic-field-theory-a-problem-solving-approach-spring-2008/pages/about-this-book/ — Author textbook, selected sections 7-6-1/7-6-2 (printed pp522–524), 7-9-1 (pp538–540), and 7-9-3/7-9-4 (pp541–544): normal/oblique Fresnel amplitudes, Snell and critical angles, evanescent fields, p-polarized Brewster condition and normal-power weighting. Field/sign conventions are adapted explicitly. Not an original Fresnel publication or a full-book audit. Selected sections 7-2-1 and 7-6-3 additionally consulted for conducting waves, complex wavenumber and conducting-interface context; the finite Lorentz slab and midpoint energy law are derived separately.
- Reference: https://meep.readthedocs.io/en/latest/Materials/ — Official HTML, selected Material Dispersion, Loss and Gain, and Conductivity and Complex ε sections: Lorentz polarization equation and exp(−iωt) convention. Meep uses a D-conductivity convention; this example instead uses conventional σE. Its explicit-ADE resonance stability bound is not attributed to our implicit midpoint update. No Meep numerical comparison or full documentation audit.

Yee FDTD supplement: retained 2D TMz vacuum modes, s-polarized dielectric interfaces, matched PML cases and selected TEz p-polarized Fresnel, Brewster and total-internal-reflection cases. The current edition adds normally incident 1D finite Ohmic and Lorentz slabs. Complex-permittivity analytic reflection, transmission and absorption, directly accumulated Ohmic/oscillator damping, material energy storage and grid convergence are checked separately. General 2D dispersive media and dispersive PML remain outside this fixed-input scope.

- Code: https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/solver.py
- Code: https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/run.py
- Code: https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/scattering.py
- Code: https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/run_scattering.py
- Code: https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/corner.py
- Code: https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/run_corner.py
- Code: https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/oblique.py
- Code: https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/run_oblique.py
- Code: https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/polarization.py
- Code: https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/run_polarization.py
- Code: https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/dispersive.py
- Code: https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/run_dispersive.py

- Tests: https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/test_fdtd.py
- Tests: https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/test_scattering.py
- Tests: https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/test_corner.py
- Tests: https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/test_oblique.py
- Tests: https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/test_polarization.py
- Tests: https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/test_dispersive.py

Download: https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/fdtd-2026-11-22-r6.zip
Manifest: https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/source-manifest.json
Verification: https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/verification.json

- periodic-wave: https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/results/periodic-wave/result.json
- pec-cavity: https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/results/pec-cavity/result.json
- dielectric-interface: https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/results/dielectric-interface/result.json
- pml-pulse: https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/results/pml-pulse/result.json
- pml-corners: https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/results/pml-corners/result.json
- dielectric-oblique: https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/results/dielectric-oblique/result.json
- p-polarization: https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/results/p-polarization/result.json
- loss-dispersion: https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/results/loss-dispersion/result.json

Commands (from extracted supplement):

```sh
python -m pip install -r requirements.txt
python -m pytest -q test_fdtd.py test_scattering.py test_corner.py test_oblique.py test_polarization.py test_dispersive.py
python run.py --input inputs/periodic-wave.json --output rerun-periodic-wave
python run.py --input inputs/pec-cavity.json --output rerun-pec-cavity
python run_scattering.py --input inputs/dielectric-interface.json --output rerun-dielectric-interface
python run_scattering.py --input inputs/pml-pulse.json --output rerun-pml-pulse
python run_corner.py --input inputs/pml-corners.json --output rerun-pml-corners
python run_oblique.py --input inputs/dielectric-oblique.json --output rerun-dielectric-oblique
python run_polarization.py --input inputs/p-polarization.json --output rerun-p-polarization
python run_dispersive.py --input inputs/loss-dispersion.json --output rerun-loss-dispersion
```

Next: Separately validate multiple resonances, oblique dispersive interfaces and dispersive-media PML.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/fdtd/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/
