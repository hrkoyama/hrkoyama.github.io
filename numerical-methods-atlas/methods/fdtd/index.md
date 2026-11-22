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

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

対応する方程式一覧の項目は未登録です。

#### 問題の図 (`method-problems-ja`)

この手法に対応付けられたテスト問題の図は未登録です。

#### 厳密解・参照解 (`method-references-ja`)

この手法の問題図に結び付く参照資料は未登録です。
##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/fdtd/)
- 保存結果: [periodic-wave の保存結果](https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/results/periodic-wave/result.json)
- 保存結果: [pec-cavity の保存結果](https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/results/pec-cavity/result.json)
- 保存結果: [dielectric-interface の保存結果](https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/results/dielectric-interface/result.json)
- 保存結果: [pml-pulse の保存結果](https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/results/pml-pulse/result.json)
- 保存結果: [pml-corners の保存結果](https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/results/pml-corners/result.json)
- 保存結果: [dielectric-oblique の保存結果](https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/results/dielectric-oblique/result.json)
- 保存結果: [p-polarization の保存結果](https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/results/p-polarization/result.json)
- 保存結果: [loss-dispersion の保存結果](https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/results/loss-dispersion/result.json)
- 検証記録: [配布版の検証記録](https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/verification.json)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

この手法と問題図を対応付けた固定入力実行例は未登録です。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/fdtd-2026-11-22-r6.zip)

[配布版の検証記録](https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/verification.json)

###### 関連ソース

- [/code/fdtd/2026-11-22-r6/solver.py](https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/solver.py)
- [/code/fdtd/2026-11-22-r6/run.py](https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/run.py)
- [/code/fdtd/2026-11-22-r6/scattering.py](https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/scattering.py)
- [/code/fdtd/2026-11-22-r6/run_scattering.py](https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/run_scattering.py)
- [/code/fdtd/2026-11-22-r6/corner.py](https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/corner.py)
- [/code/fdtd/2026-11-22-r6/run_corner.py](https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/run_corner.py)
- [/code/fdtd/2026-11-22-r6/oblique.py](https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/oblique.py)
- [/code/fdtd/2026-11-22-r6/run_oblique.py](https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/run_oblique.py)
- [/code/fdtd/2026-11-22-r6/polarization.py](https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/polarization.py)
- [/code/fdtd/2026-11-22-r6/run_polarization.py](https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/run_polarization.py)
- [/code/fdtd/2026-11-22-r6/dispersive.py](https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/dispersive.py)
- [/code/fdtd/2026-11-22-r6/run_dispersive.py](https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/run_dispersive.py)

###### 配布版のテスト

- [/code/fdtd/2026-11-22-r6/test_fdtd.py](https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/test_fdtd.py)
- [/code/fdtd/2026-11-22-r6/test_scattering.py](https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/test_scattering.py)
- [/code/fdtd/2026-11-22-r6/test_corner.py](https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/test_corner.py)
- [/code/fdtd/2026-11-22-r6/test_oblique.py](https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/test_oblique.py)
- [/code/fdtd/2026-11-22-r6/test_polarization.py](https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/test_polarization.py)
- [/code/fdtd/2026-11-22-r6/test_dispersive.py](https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/test_dispersive.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
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


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

No corresponding equation-registry entry is registered.

#### Problem figures (`method-problems-en`)

No test-problem figure is registered for this method.

#### Exact / reference solutions (`method-references-en`)

No reference context is registered for this method’s problem figures.
##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/fdtd/)
- Saved result: [Saved results: periodic-wave](https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/results/periodic-wave/result.json)
- Saved result: [Saved results: pec-cavity](https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/results/pec-cavity/result.json)
- Saved result: [Saved results: dielectric-interface](https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/results/dielectric-interface/result.json)
- Saved result: [Saved results: pml-pulse](https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/results/pml-pulse/result.json)
- Saved result: [Saved results: pml-corners](https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/results/pml-corners/result.json)
- Saved result: [Saved results: dielectric-oblique](https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/results/dielectric-oblique/result.json)
- Saved result: [Saved results: p-polarization](https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/results/p-polarization/result.json)
- Saved result: [Saved results: loss-dispersion](https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/results/loss-dispersion/result.json)
- Verification receipt: [Edition verification receipt](https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/verification.json)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

No fixed-input execution example is linked between this method and a problem figure.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

[Related code edition / ZIP](https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/fdtd-2026-11-22-r6.zip)

[Edition verification receipt](https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/verification.json)

###### Related source

- [/code/fdtd/2026-11-22-r6/solver.py](https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/solver.py)
- [/code/fdtd/2026-11-22-r6/run.py](https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/run.py)
- [/code/fdtd/2026-11-22-r6/scattering.py](https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/scattering.py)
- [/code/fdtd/2026-11-22-r6/run_scattering.py](https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/run_scattering.py)
- [/code/fdtd/2026-11-22-r6/corner.py](https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/corner.py)
- [/code/fdtd/2026-11-22-r6/run_corner.py](https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/run_corner.py)
- [/code/fdtd/2026-11-22-r6/oblique.py](https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/oblique.py)
- [/code/fdtd/2026-11-22-r6/run_oblique.py](https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/run_oblique.py)
- [/code/fdtd/2026-11-22-r6/polarization.py](https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/polarization.py)
- [/code/fdtd/2026-11-22-r6/run_polarization.py](https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/run_polarization.py)
- [/code/fdtd/2026-11-22-r6/dispersive.py](https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/dispersive.py)
- [/code/fdtd/2026-11-22-r6/run_dispersive.py](https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/run_dispersive.py)

###### Package tests

- [/code/fdtd/2026-11-22-r6/test_fdtd.py](https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/test_fdtd.py)
- [/code/fdtd/2026-11-22-r6/test_scattering.py](https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/test_scattering.py)
- [/code/fdtd/2026-11-22-r6/test_corner.py](https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/test_corner.py)
- [/code/fdtd/2026-11-22-r6/test_oblique.py](https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/test_oblique.py)
- [/code/fdtd/2026-11-22-r6/test_polarization.py](https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/test_polarization.py)
- [/code/fdtd/2026-11-22-r6/test_dispersive.py](https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/test_dispersive.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
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
