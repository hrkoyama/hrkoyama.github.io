# Periodic electronic structure and k-point sampling / 周期電子状態とk点

Status: educational-example

Connect periodic boundaries, Bloch representations and Brillouin-zone integration.

周期境界、Bloch表現、Brillouin領域の積分をつなぐ。

Limited to a selected local GTH and fixed He cell. Nonlocal/PAW/general-element transferability, metals/smearing, a complete-basis limit and agreement with experiment are unvalidated. BZ quadrature meshes are distinct from band paths.

Other names: k点, Monkhorst–Pack, Bloch, Brillouin zone

Comparison notes: Distinguish metallic occupation/smearing dependence, finite-temperature free energy and zero-temperature energy. Whether Γ-only sampling is adequate depends on the system and cell.

金属の占有とsmearing幅の依存、有限温度の自由エネルギーと零温度エネルギーを区別します。Γ点だけで十分かは系とセルに依存します。

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/quantum-chemistry/#k-point
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/quantum-chemistry/#k-point



- Reference: https://doi.org/10.1103/PhysRevB.13.5188 — Primary publication entry point for the quantum-chemistry overview. Bibliographic/introductory review only; full-paper equations and numerical results have not been reproduced.

Periodic scope: Periodic KS-DFT for one fixed simple-cubic He cell. An educational PySCF workflow separately checks Gamma/k sampling, Gaussian orbital basis, auxiliary FFT grid and SCF tolerances against independent DFTK plane waves with identical GTH parameters and LDA exchange plus VWN5 correlation. Does not validate equilibrium helium solids, general materials or metals.

{
  "release": {
    "family": "periodic-dft",
    "version": "2026-11-22",
    "download": "https://hrkoyama.github.io/code/periodic-dft/2026-11-22/periodic-dft-2026-11-22.zip",
    "sha256": "f331515e3ad419b5435dbf851553c6b853b28b2432801fc13c84109faa362df8",
    "manifest": "https://hrkoyama.github.io/code/periodic-dft/2026-11-22/source-manifest.json",
    "manifest_sha256": "1ac7fe2531934a598b7d9b69930c5a8a83f6b5bf2a67ae9f0616f35aa63f34fd",
    "verification": "https://hrkoyama.github.io/code/periodic-dft/2026-11-22/verification.json",
    "archive_directory": "periodic-dft-2026-11-22"
  },
  "code_base": "https://hrkoyama.github.io/code/periodic-dft/2026-11-22/",
  "examples": [
    "periodic-he-dft"
  ],
  "run_commands": [
    "python run.py --input inputs.json --output output"
  ],
  "scope": {
    "ja": "固定した1原子単純立方Heセルの周期KS-DFT。PySCFを使う教育用ワークフローで、Γ点／k点、Gaussian軌道基底、FFT補助格子、SCF公差を別々に検査し、同じGTHパラメータ・LDA交換＋VWN5相関のDFTK平面波計算と比較。平衡He結晶や一般物質・金属の検証ではありません。",
    "en": "Periodic KS-DFT for one fixed simple-cubic He cell. An educational PySCF workflow separately checks Gamma/k sampling, Gaussian orbital basis, auxiliary FFT grid and SCF tolerances against independent DFTK plane waves with identical GTH parameters and LDA exchange plus VWN5 correlation. Does not validate equilibrium helium solids, general materials or metals."
  },
  "implementation": "Original educational workflow using PySCF; independent reference uses DFTK."
}

Common execution records: [{"id": "periodic-he-dft", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=ja#periodic-he-dft-ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=en#periodic-he-dft-en"}}]

Next: Add another insulator, band paths and metallic occupations/smearing with their own independent references and refinement checks.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/k-point/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/
