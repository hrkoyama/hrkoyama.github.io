# Yee finite-difference time-domain method / Yee FDTD

Status: educational-example

Fixed-input Yee FDTD checks for vacuum, Fresnel interfaces, PML and 1D lossy/Lorentz slabs. Additional fixed examples: Mie scattering width of a two-dimensional dielectric cylinder. See each release for assumptions and checked scope. Additional fixed examples: Oblique s/p incidence on a Lorentz-dispersive slab. See each release for assumptions and checked scope. Additional fixed examples: Long-time grazing PML in a dispersive medium. See each release for assumptions and checked scope.

Yee FDTDの真空・Fresnel界面・PMLと一次元の損失・Lorentz分散板を固定入力で検証。 追加固定例：2D誘電体円柱のMie散乱幅。条件と検証範囲は各配布版で確認してください。 追加固定例：Lorentz分散板へのs/p斜め入射。条件と検証範囲は各配布版で確認してください。 追加固定例：分散媒質の浅い入射角と長時間PML。条件と検証範囲は各配布版で確認してください。

Educational Yee FDTD: retained vacuum/Fresnel/s-p/PML examples plus r6 1D normal-incidence Ohmic and passive Lorentz slabs. Spectral references, R/T, direct dissipation, material storage, modified/physical budgets and space/time refinement are separate checks. Not blanket validation of general dispersion, multiple resonances, oblique dispersive incidence, dispersive PML or general 2D/3D. Additional fixed examples: This is a lossless two-dimensional Ez cylinder, not a three-dimensional sphere. Report staircase geometry error without claiming general second-order curved-boundary accuracy or precision scattering for arbitrary frequencies and materials. Additional fixed examples: This is a genuine single-ky restriction rather than arbitrary transverse data. It covers one passive Lorentz pole and a fixed finite band/window. Gaussian tails are nonzero; window diagnostics and reference errors are reported separately. No strict all-frequency no-return proof is claimed. Additional fixed examples: The central angle is 80 degrees; finite kx bandwidth gives neighboring angles. The no-PML reference shares the discretization and initialization to isolate boundary error from bulk dispersion. Small operator and finite-trajectory checks do not prove global stability for arbitrary angles and materials. The joint family does not measure fixed-PML spatial order; the older 100 checks alone do not prove peak-12 global stability.

Other names: FDTD法, finite difference time domain, 有限差分時間領域法, Yee法

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/fdtd/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/fdtd/



- Reference: https://doi.org/10.1109/tap.1966.1138693 — Method-specific source; see the detailed reading for source role and actual review depth.
- Reference: https://arxiv.org/abs/1705.02274v2 — Research preprint v2; energy Eq26 and strict CFL Eq35 consulted. Not a claim to implement its subgridding method.
- Reference: https://doi.org/10.1006/jcph.1994.1159 — Original split-field PML publication: bibliographic identity and abstract checked. Original full text was not available for inspection. The implemented reduction and discrete balance are derived and tested separately; consult Johnson for the matched-layer interpretation.
- Reference: https://arxiv.org/abs/2108.05348v1 — Author notes, selected sections3.4,4.1–4.2 and7.1–7.3: independent x/y coordinate stretches and simultaneous corner damping, matching electric/magnetic rates, anisotropic interpretation, discretization reflections and incidence limitations. Not a complete audit of every PML formulation.
- Reference: https://ocw.mit.edu/courses/res-6-002-electromagnetic-field-theory-a-problem-solving-approach-spring-2008/pages/about-this-book/ — Author textbook, selected sections 7-6-1/7-6-2 (printed pp522–524), 7-9-1 (pp538–540), and 7-9-3/7-9-4 (pp541–544): normal/oblique Fresnel amplitudes, Snell and critical angles, evanescent fields, p-polarized Brewster condition and normal-power weighting. Field/sign conventions are adapted explicitly. Not an original Fresnel publication or a full-book audit. Selected sections 7-2-1 and 7-6-3 additionally consulted for conducting waves, complex wavenumber and conducting-interface context; the finite Lorentz slab and midpoint energy law are derived separately.
- Reference: https://meep.readthedocs.io/en/latest/Materials/ — Official HTML, selected Material Dispersion, Loss and Gain, and Conductivity and Complex ε sections: Lorentz polarization equation and exp(−iωt) convention. Meep uses a D-conductivity convention; this example instead uses conventional σE. Its explicit-ADE resonance stability bound is not attributed to our implicit midpoint update. No Meep numerical comparison or full documentation audit.

## Small fixed-input validation supplements

Additional fixed examples: Mie scattering width of a two-dimensional dielectric cylinder. See each release for assumptions and checked scope. This is a lossless two-dimensional Ez cylinder, not a three-dimensional sphere. Report staircase geometry error without claiming general second-order curved-boundary accuracy or precision scattering for arbitrary frequencies and materials.

追加固定例：2D誘電体円柱のMie散乱幅。条件と検証範囲は各配布版で確認してください。 Ezの無損失2D円柱のみで、3D球ではありません。階段状形状の誤差を記録し、一般の曲面2次精度や任意周波数・材料での精密散乱を保証しません。

- Mie scattering width of a two-dimensional dielectric cylinder: https://hrkoyama.github.io/numerical-methods-atlas/validation/cylinder-mie2d/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-cylinder/atlas-maxwell-cylinder-2026-11-24-r2.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-cylinder/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-cylinder/results/result.json

- Oblique s/p incidence on a Lorentz-dispersive slab: https://hrkoyama.github.io/numerical-methods-atlas/validation/lorentz-oblique-sp/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/atlas-maxwell-lorentz-2026-11-24-r2.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/results/result.json

- Long-time grazing PML in a dispersive medium: https://hrkoyama.github.io/numerical-methods-atlas/validation/dispersive-grazing-pml/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/atlas-maxwell-grazing-2026-11-24-r2.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/results/result.json

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
- Code: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-cylinder/run.py
- Code: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-cylinder/cylinder_draft.py
- Code: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-cylinder/cylinder_evolution.py
- Code: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-cylinder/io_contract.py
- Code: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-cylinder/poynting.py
- Code: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-cylinder/reference_draft.py
- Code: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/run.py
- Code: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/io_contract.py
- Code: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/modal_yee_draft.py
- Code: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/reference_draft.py
- Code: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/slab_evolution.py
- Code: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/slab_reference.py
- Code: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/run.py
- Code: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/references/isolated_reference.py
- Code: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/centered_pml.py
- Code: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/io_contract.py
- Code: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/modal_yee_draft.py
- Code: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/pml_evolution.py
- Code: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/specifications.py

- Tests: https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/test_fdtd.py
- Tests: https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/test_scattering.py
- Tests: https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/test_corner.py
- Tests: https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/test_oblique.py
- Tests: https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/test_polarization.py
- Tests: https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/test_dispersive.py
- Tests: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-cylinder/test_cylinder.py
- Tests: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/test_lorentz.py
- Tests: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/test_grazing.py

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

Common execution records: [{"id": "cylinder-mie2d", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/cylinder-mie2d/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/cylinder-mie2d/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "lorentz-oblique-sp", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/lorentz-oblique-sp/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/lorentz-oblique-sp/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "dispersive-grazing-pml", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/dispersive-grazing-pml/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/dispersive-grazing-pml/?lang=en"}, "kind": "dedicated-supplement"}]

Next: Separately validate multiple resonances, oblique dispersive interfaces and dispersive-media PML.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/fdtd/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [線形Maxwell電磁場（真空・誘電体）](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#maxwell-ja) (`maxwell`; cylinder-mie2d)
- [受動Lorentz・Ohmic分散Maxwell場](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#maxwell-lorentz-ja) (`maxwell-lorentz`; lorentz-oblique-sp, dispersive-grazing-pml)

#### 問題の図 (`method-problems-ja`)

##### [2D誘電体円柱のMie散乱幅](https://hrkoyama.github.io/numerical-methods-atlas/problems/cylinder-mie2d/?lang=ja) (`cylinder-mie2d`)

![保存した最細格子の実2D散乱電場phasorの実部。 図の中央の白抜きは診断用のr<0.4のマスクで、物理円柱の半径0.25とは区別します。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-cylinder/results/cylinder-mie2d-preview.png)

Yeeの散乱場を局所分極contrastの厳密な離散入射差分で励起します。EとHはそれぞれの整数・半時刻でFourier集計し、Hの4点補間後に物理流束を積分します。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/cylinder-mie2d/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/cylinder-mie2d/?lang=ja#code-ja)

- [2D誘電体円柱のMie散乱幅](https://hrkoyama.github.io/numerical-methods-atlas/validation/cylinder-mie2d/?lang=ja) (`cylinder-mie2d`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-cylinder/atlas-maxwell-cylinder-2026-11-24-r2.zip)

実際の2D散乱場を進め、閉曲線Poynting流束と独立な円柱級数を比較します。

##### [Lorentz分散板へのs/p斜め入射](https://hrkoyama.github.io/numerical-methods-atlas/problems/lorentz-oblique-sp/?lang=ja) (`lorentz-oblique-sp`)

![保存したp偏光の実電場をky=4の周期y方向へ再構成した場。 周期y方向の1周期を表示しています。波形を見やすくするため、x軸とy軸の表示縮尺は異なります。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/results/lorentz-oblique-sp-preview.png)

単一ky Yee空間演算と局所の陰的中点Lorentz ADE。p偏光の両電場に分極を結合し、同格子の真空波束で入射・伝播位相を除きます。直接Ohmic・物質減衰仕事と修正エネルギーを別々に集計します。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/lorentz-oblique-sp/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/lorentz-oblique-sp/?lang=ja#code-ja)

- [Lorentz分散板へのs/p斜め入射](https://hrkoyama.github.io/numerical-methods-atlas/validation/lorentz-oblique-sp/?lang=ja) (`lorentz-oblique-sp`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/atlas-maxwell-lorentz-2026-11-24-r2.zip)

有限波束の実進行から複素r/t・R/T・直接散逸を求め、複素Fresnel参照と比較します。

##### [分散媒質の浅い入射角と長時間PML](https://hrkoyama.github.io/numerical-methods-atlas/problems/dispersive-grazing-pml/?lang=ja) (`dispersive-grazing-pml`)

![保存した浅角度の実電場を周期y方向へ再構成。灰色はPML領域です。 周期y方向の1周期を表示しています。波形を見やすくするため、x軸とy軸の表示縮尺は異なります。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/results/dispersive-grazing-pml-preview.png)

Yee・中点ADEに時刻配置を保った台形微分memoryを結合。正の物理散逸と符号付きPML数値仕事を区別し、補助場を含め全状態を保存します。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/dispersive-grazing-pml/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/dispersive-grazing-pml/?lang=ja#code-ja)

- [分散媒質の浅い入射角と長時間PML](https://hrkoyama.github.io/numerical-methods-atlas/validation/dispersive-grazing-pml/?lang=ja) (`dispersive-grazing-pml`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/atlas-maxwell-grazing-2026-11-24-r2.zip)

80度の中心位相角を持つ有限波束をT=700まで進め、境界誤差を同格子の無PML参照から分離します。


#### 厳密解・参照解 (`method-references-ja`)

##### [2D誘電体円柱のMie散乱幅](https://hrkoyama.github.io/numerical-methods-atlas/problems/cylinder-mie2d/?lang=ja#references-ja) (`cylinder-mie2d`)

- [誘電体円柱の外部級数と散乱幅](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-cylinder-mie2d-ja) (`cylinder-mie2d`; 同じ問題の参照; 解析参照)

Ezの無損失2D円柱のみで、3D球ではありません。階段状形状の誤差を記録し、一般の曲面2次精度や任意周波数・材料での精密散乱を保証しません。

[既存の参照図](/numerical-methods-atlas/validation/cylinder-mie2d/?lang=ja#cylinder-mie2d-ja-measurements)

##### [Lorentz分散板へのs/p斜め入射](https://hrkoyama.github.io/numerical-methods-atlas/problems/lorentz-oblique-sp/?lang=ja#references-ja) (`lorentz-oblique-sp`)

- [斜め入射の複素Fresnel係数とLorentz板の直接散逸](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-lorentz-oblique-sp-ja) (`lorentz-oblique-sp`; 同じ問題の参照; 解析参照)

任意の横方向分布ではなく単一kyの実空間制限です。1つの受動Lorentz極と有限帯域・有限窓のみ。Gaussian尾は厳密には非零で、窓診断と参照誤差を別記します。 全周波数で厳密にcap反射が未到達という証明ではありません。

[既存の参照図](/numerical-methods-atlas/validation/lorentz-oblique-sp/?lang=ja#lorentz-oblique-sp-ja-measurements)

##### [分散媒質の浅い入射角と長時間PML](https://hrkoyama.github.io/numerical-methods-atlas/problems/dispersive-grazing-pml/?lang=ja#references-ja) (`dispersive-grazing-pml`)

- [浅角度分散波束の長時間・同格子孤立境界参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-dispersive-grazing-pml-ja) (`dispersive-grazing-pml`; 同じ問題の参照; 有限格子の数値参照)

有限kx帯域の中心角が80度で、全成分が厳密に80度ではありません。無PML参照は同じ離散化・初期場を使い、伝播分散を除いた境界誤差用です。任意角度・材料での大域安定性証明ではありません。 固定PMLの空間次数を測る族ではなく、旧100検査だけでpeak12の大域安定性が証明されたとはしません。

[既存の参照図](/numerical-methods-atlas/validation/dispersive-grazing-pml/?lang=ja#dispersive-grazing-pml-ja-measurements)

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

##### 2D誘電体円柱のMie散乱幅 (`cylinder-mie2d`)

[2D誘電体円柱のMie散乱幅](https://hrkoyama.github.io/numerical-methods-atlas/problems/cylinder-mie2d/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/cylinder-mie2d/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-cylinder/atlas-maxwell-cylinder-2026-11-24-r2.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-cylinder/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-cylinder/verification.json)

実際の2D散乱場を進め、閉曲線Poynting流束と独立な円柱級数を比較します。

##### Lorentz分散板へのs/p斜め入射 (`lorentz-oblique-sp`)

[Lorentz分散板へのs/p斜め入射](https://hrkoyama.github.io/numerical-methods-atlas/problems/lorentz-oblique-sp/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/lorentz-oblique-sp/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/atlas-maxwell-lorentz-2026-11-24-r2.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/verification.json)

有限波束の実進行から複素r/t・R/T・直接散逸を求め、複素Fresnel参照と比較します。

##### 分散媒質の浅い入射角と長時間PML (`dispersive-grazing-pml`)

[分散媒質の浅い入射角と長時間PML](https://hrkoyama.github.io/numerical-methods-atlas/problems/dispersive-grazing-pml/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/dispersive-grazing-pml/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/atlas-maxwell-grazing-2026-11-24-r2.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/verification.json)

80度の中心位相角を持つ有限波束をT=700まで進め、境界誤差を同格子の無PML参照から分離します。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

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
- [/code/validated-examples/2026-11-24-r2/maxwell-cylinder/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-cylinder/run.py)
- [/code/validated-examples/2026-11-24-r2/maxwell-cylinder/cylinder_draft.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-cylinder/cylinder_draft.py)
- [/code/validated-examples/2026-11-24-r2/maxwell-cylinder/cylinder_evolution.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-cylinder/cylinder_evolution.py)
- [/code/validated-examples/2026-11-24-r2/maxwell-cylinder/io_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-cylinder/io_contract.py)
- [/code/validated-examples/2026-11-24-r2/maxwell-cylinder/poynting.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-cylinder/poynting.py)
- [/code/validated-examples/2026-11-24-r2/maxwell-cylinder/reference_draft.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-cylinder/reference_draft.py)
- [/code/validated-examples/2026-11-24-r2/maxwell-lorentz/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/run.py)
- [/code/validated-examples/2026-11-24-r2/maxwell-lorentz/io_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/io_contract.py)
- [/code/validated-examples/2026-11-24-r2/maxwell-lorentz/modal_yee_draft.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/modal_yee_draft.py)
- [/code/validated-examples/2026-11-24-r2/maxwell-lorentz/reference_draft.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/reference_draft.py)
- [/code/validated-examples/2026-11-24-r2/maxwell-lorentz/slab_evolution.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/slab_evolution.py)
- [/code/validated-examples/2026-11-24-r2/maxwell-lorentz/slab_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/slab_reference.py)
- [/code/validated-examples/2026-11-24-r2/maxwell-grazing/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/run.py)
- [/code/validated-examples/2026-11-24-r2/maxwell-grazing/references/isolated_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/references/isolated_reference.py)
- [/code/validated-examples/2026-11-24-r2/maxwell-grazing/centered_pml.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/centered_pml.py)
- [/code/validated-examples/2026-11-24-r2/maxwell-grazing/io_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/io_contract.py)
- [/code/validated-examples/2026-11-24-r2/maxwell-grazing/modal_yee_draft.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/modal_yee_draft.py)
- [/code/validated-examples/2026-11-24-r2/maxwell-grazing/pml_evolution.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/pml_evolution.py)
- [/code/validated-examples/2026-11-24-r2/maxwell-grazing/specifications.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/specifications.py)

###### 配布版のテスト

- [/code/fdtd/2026-11-22-r6/test_fdtd.py](https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/test_fdtd.py)
- [/code/fdtd/2026-11-22-r6/test_scattering.py](https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/test_scattering.py)
- [/code/fdtd/2026-11-22-r6/test_corner.py](https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/test_corner.py)
- [/code/fdtd/2026-11-22-r6/test_oblique.py](https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/test_oblique.py)
- [/code/fdtd/2026-11-22-r6/test_polarization.py](https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/test_polarization.py)
- [/code/fdtd/2026-11-22-r6/test_dispersive.py](https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/test_dispersive.py)
- [/code/validated-examples/2026-11-24-r2/maxwell-cylinder/test_cylinder.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-cylinder/test_cylinder.py)
- [/code/validated-examples/2026-11-24-r2/maxwell-lorentz/test_lorentz.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/test_lorentz.py)
- [/code/validated-examples/2026-11-24-r2/maxwell-grazing/test_grazing.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/test_grazing.py)

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

- [Linear Maxwell fields in vacuum and dielectrics](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#maxwell-en) (`maxwell`; cylinder-mie2d)
- [Passive Lorentz–Ohmic Maxwell fields](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#maxwell-lorentz-en) (`maxwell-lorentz`; lorentz-oblique-sp, dispersive-grazing-pml)

#### Problem figures (`method-problems-en`)

##### [Mie scattering width of a two-dimensional dielectric cylinder](https://hrkoyama.github.io/numerical-methods-atlas/problems/cylinder-mie2d/?lang=en) (`cylinder-mie2d`)

![Real part of the actual saved scattered electric phasor on the finest two-dimensional grid. The central white region is a diagnostic mask at r<0.4, distinct from the physical cylinder radius0.25.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-cylinder/results/cylinder-mie2d-preview.png)

Advance the scattered Yee fields with an exact discrete incident difference on the polarization-contrast support. Accumulate E and H at their own integer and half times, then integrate physical power after four-point native-face collocation.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/cylinder-mie2d/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/cylinder-mie2d/?lang=en#code-en)

- [Mie scattering width of a two-dimensional dielectric cylinder](https://hrkoyama.github.io/numerical-methods-atlas/validation/cylinder-mie2d/?lang=en) (`cylinder-mie2d`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-cylinder/atlas-maxwell-cylinder-2026-11-24-r2.zip)

Evolve the actual two-dimensional scattered fields and compare closed-contour Poynting power with an independent cylindrical series.

##### [Oblique s/p incidence on a Lorentz-dispersive slab](https://hrkoyama.github.io/numerical-methods-atlas/problems/lorentz-oblique-sp/?lang=en) (`lorentz-oblique-sp`)

![Actual saved p-polarized electric field reconstructed over the periodic y direction at ky=4. One transverse y period is shown. The displayed x and y scales differ to make the fields visible.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/results/lorentz-oblique-sp-preview.png)

Use the single-ky Yee spatial operator and local implicit-midpoint Lorentz ADE. Couple both p-polarized electric components to polarization, and remove incident propagation with a matched vacuum pulse on the same grid. Accumulate direct Ohmic and material-damping work separately from modified energy.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/lorentz-oblique-sp/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/lorentz-oblique-sp/?lang=en#code-en)

- [Oblique s/p incidence on a Lorentz-dispersive slab](https://hrkoyama.github.io/numerical-methods-atlas/validation/lorentz-oblique-sp/?lang=en) (`lorentz-oblique-sp`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/atlas-maxwell-lorentz-2026-11-24-r2.zip)

Measure complex r/t, power fractions and direct dissipation from actual finite-pulse evolutions and compare them with complex Fresnel slab references.

##### [Long-time grazing PML in a dispersive medium](https://hrkoyama.github.io/numerical-methods-atlas/problems/dispersive-grazing-pml/?lang=en) (`dispersive-grazing-pml`)

![Actual saved grazing electric field reconstructed over the periodic y direction; gray shading marks the PML. One transverse y period is shown. The displayed x and y scales differ to make the fields visible.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/results/dispersive-grazing-pml-preview.png)

Couple Yee and midpoint ADE updates to a trapezoidal derivative-memory filter at native times. Separate positive physical dissipation from signed numerical PML work, retaining all physical and auxiliary states.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/dispersive-grazing-pml/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/dispersive-grazing-pml/?lang=en#code-en)

- [Long-time grazing PML in a dispersive medium](https://hrkoyama.github.io/numerical-methods-atlas/validation/dispersive-grazing-pml/?lang=en) (`dispersive-grazing-pml`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/atlas-maxwell-grazing-2026-11-24-r2.zip)

Evolve a finite packet with an 80-degree central phase angle to T = 700, isolating boundary error against a no-PML reference on the same grid.


#### Exact / reference solutions (`method-references-en`)

##### [Mie scattering width of a two-dimensional dielectric cylinder](https://hrkoyama.github.io/numerical-methods-atlas/problems/cylinder-mie2d/?lang=en#references-en) (`cylinder-mie2d`)

- [Exterior series and scattering width of a dielectric cylinder](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-cylinder-mie2d-en) (`cylinder-mie2d`; Same-problem reference; Analytic reference)

This is a lossless two-dimensional Ez cylinder, not a three-dimensional sphere. Report staircase geometry error without claiming general second-order curved-boundary accuracy or precision scattering for arbitrary frequencies and materials.

[Existing reference profile](/numerical-methods-atlas/validation/cylinder-mie2d/?lang=en#cylinder-mie2d-en-measurements)

##### [Oblique s/p incidence on a Lorentz-dispersive slab](https://hrkoyama.github.io/numerical-methods-atlas/problems/lorentz-oblique-sp/?lang=en#references-en) (`lorentz-oblique-sp`)

- [Complex oblique Fresnel coefficients and direct Lorentz-slab loss](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-lorentz-oblique-sp-en) (`lorentz-oblique-sp`; Same-problem reference; Analytic reference)

This is a genuine single-ky restriction rather than arbitrary transverse data. It covers one passive Lorentz pole and a fixed finite band/window. Gaussian tails are nonzero; window diagnostics and reference errors are reported separately. No strict all-frequency no-return proof is claimed.

[Existing reference profile](/numerical-methods-atlas/validation/lorentz-oblique-sp/?lang=en#lorentz-oblique-sp-en-measurements)

##### [Long-time grazing PML in a dispersive medium](https://hrkoyama.github.io/numerical-methods-atlas/problems/dispersive-grazing-pml/?lang=en#references-en) (`dispersive-grazing-pml`)

- [Isolated same-grid reference for a long grazing dispersive packet](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-dispersive-grazing-pml-en) (`dispersive-grazing-pml`; Same-problem reference; Finite-grid numerical reference)

The central angle is 80 degrees; finite kx bandwidth gives neighboring angles. The no-PML reference shares the discretization and initialization to isolate boundary error from bulk dispersion. Small operator and finite-trajectory checks do not prove global stability for arbitrary angles and materials. The joint family does not measure fixed-PML spatial order; the older 100 checks alone do not prove peak-12 global stability.

[Existing reference profile](/numerical-methods-atlas/validation/dispersive-grazing-pml/?lang=en#dispersive-grazing-pml-en-measurements)

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

##### Mie scattering width of a two-dimensional dielectric cylinder (`cylinder-mie2d`)

[Mie scattering width of a two-dimensional dielectric cylinder](https://hrkoyama.github.io/numerical-methods-atlas/problems/cylinder-mie2d/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/cylinder-mie2d/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-cylinder/atlas-maxwell-cylinder-2026-11-24-r2.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-cylinder/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-cylinder/verification.json)

Evolve the actual two-dimensional scattered fields and compare closed-contour Poynting power with an independent cylindrical series.

##### Oblique s/p incidence on a Lorentz-dispersive slab (`lorentz-oblique-sp`)

[Oblique s/p incidence on a Lorentz-dispersive slab](https://hrkoyama.github.io/numerical-methods-atlas/problems/lorentz-oblique-sp/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/lorentz-oblique-sp/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/atlas-maxwell-lorentz-2026-11-24-r2.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/verification.json)

Measure complex r/t, power fractions and direct dissipation from actual finite-pulse evolutions and compare them with complex Fresnel slab references.

##### Long-time grazing PML in a dispersive medium (`dispersive-grazing-pml`)

[Long-time grazing PML in a dispersive medium](https://hrkoyama.github.io/numerical-methods-atlas/problems/dispersive-grazing-pml/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/dispersive-grazing-pml/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/atlas-maxwell-grazing-2026-11-24-r2.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/verification.json)

Evolve a finite packet with an 80-degree central phase angle to T = 700, isolating boundary error against a no-PML reference on the same grid.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

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
- [/code/validated-examples/2026-11-24-r2/maxwell-cylinder/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-cylinder/run.py)
- [/code/validated-examples/2026-11-24-r2/maxwell-cylinder/cylinder_draft.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-cylinder/cylinder_draft.py)
- [/code/validated-examples/2026-11-24-r2/maxwell-cylinder/cylinder_evolution.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-cylinder/cylinder_evolution.py)
- [/code/validated-examples/2026-11-24-r2/maxwell-cylinder/io_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-cylinder/io_contract.py)
- [/code/validated-examples/2026-11-24-r2/maxwell-cylinder/poynting.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-cylinder/poynting.py)
- [/code/validated-examples/2026-11-24-r2/maxwell-cylinder/reference_draft.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-cylinder/reference_draft.py)
- [/code/validated-examples/2026-11-24-r2/maxwell-lorentz/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/run.py)
- [/code/validated-examples/2026-11-24-r2/maxwell-lorentz/io_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/io_contract.py)
- [/code/validated-examples/2026-11-24-r2/maxwell-lorentz/modal_yee_draft.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/modal_yee_draft.py)
- [/code/validated-examples/2026-11-24-r2/maxwell-lorentz/reference_draft.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/reference_draft.py)
- [/code/validated-examples/2026-11-24-r2/maxwell-lorentz/slab_evolution.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/slab_evolution.py)
- [/code/validated-examples/2026-11-24-r2/maxwell-lorentz/slab_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/slab_reference.py)
- [/code/validated-examples/2026-11-24-r2/maxwell-grazing/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/run.py)
- [/code/validated-examples/2026-11-24-r2/maxwell-grazing/references/isolated_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/references/isolated_reference.py)
- [/code/validated-examples/2026-11-24-r2/maxwell-grazing/centered_pml.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/centered_pml.py)
- [/code/validated-examples/2026-11-24-r2/maxwell-grazing/io_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/io_contract.py)
- [/code/validated-examples/2026-11-24-r2/maxwell-grazing/modal_yee_draft.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/modal_yee_draft.py)
- [/code/validated-examples/2026-11-24-r2/maxwell-grazing/pml_evolution.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/pml_evolution.py)
- [/code/validated-examples/2026-11-24-r2/maxwell-grazing/specifications.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/specifications.py)

###### Package tests

- [/code/fdtd/2026-11-22-r6/test_fdtd.py](https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/test_fdtd.py)
- [/code/fdtd/2026-11-22-r6/test_scattering.py](https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/test_scattering.py)
- [/code/fdtd/2026-11-22-r6/test_corner.py](https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/test_corner.py)
- [/code/fdtd/2026-11-22-r6/test_oblique.py](https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/test_oblique.py)
- [/code/fdtd/2026-11-22-r6/test_polarization.py](https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/test_polarization.py)
- [/code/fdtd/2026-11-22-r6/test_dispersive.py](https://hrkoyama.github.io/code/fdtd/2026-11-22-r6/test_dispersive.py)
- [/code/validated-examples/2026-11-24-r2/maxwell-cylinder/test_cylinder.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-cylinder/test_cylinder.py)
- [/code/validated-examples/2026-11-24-r2/maxwell-lorentz/test_lorentz.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/test_lorentz.py)
- [/code/validated-examples/2026-11-24-r2/maxwell-grazing/test_grazing.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/test_grazing.py)

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
