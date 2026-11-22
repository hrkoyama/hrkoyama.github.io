# Algebraic multigrid / AMG / 代数的マルチグリッド（AMG）

Status: educational-example

Matrix-based AMG: distinguish residual and solution error: Build a smoothed-aggregation hierarchy from an SPD matrix alone and run V-cycles. Problems with 7², 15² and 31² unknowns distinguish independent sparse direct solutions, analytic discrete sine modes and second-order convergence to the continuum solution. AMG: conditioning, anisotropy, residual and forward error: Separate condition number from anisotropy on SPD systems of 49, 225 and 961 unknowns. Compare analytic spectra, independent sparse direct solutions and DST diagonalization, and measure how residual translates to forward error.

行列から粗視化するAMG：残差と解誤差を分ける: 正方形Poisson問題から得たSPD行列だけを階層構築へ渡し、平滑化集約AMGのV-cycleを実行します。7²・15²・31²未知数で独立疎行列直接解、解析的な離散正弦モード、連続解への2次収束を分けて検査します。 AMGの条件数・異方性・残差と前進誤差: 49・225・961未知数のSPD行列で、条件数と異方性を別々に変えます。解析スペクトル、独立疎行列直接解、DST対角化を比較し、同じ残差でも解誤差が条件数に依存することを確かめます。

Matrix-based AMG: distinguish residual and solution error: Only three fixed scalar grids are checked. Large coefficient jumps, strong anisotropy, elasticity, arbitrary unstructured meshes, optimal complexity and mesh-independent convergence are not certified. A small residual alone does not prove a small solution error. AMG: conditioning, anisotropy, residual and forward error: Only a small constant-coefficient family is checked. Arbitrary coefficient jumps, unstructured grids, indefinite systems, optimal complexity and uniform convergence are outside scope. No claim that anisotropy necessarily increases κ₂ or monotonically worsens convergence.

Other names: AMG法, algebraic multigrid, 代数マルチグリッド, 代数的多重格子法

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/amg/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/amg/



- Reference: https://doi.org/10.1137/1.9781611971057.ch4 — Method-specific source; see the detailed reading for source role and actual review depth.

## Small fixed-input validation supplements

Matrix-based AMG: distinguish residual and solution error: Build a smoothed-aggregation hierarchy from an SPD matrix alone and run V-cycles. Problems with 7², 15² and 31² unknowns distinguish independent sparse direct solutions, analytic discrete sine modes and second-order convergence to the continuum solution. AMG: conditioning, anisotropy, residual and forward error: Separate condition number from anisotropy on SPD systems of 49, 225 and 961 unknowns. Compare analytic spectra, independent sparse direct solutions and DST diagonalization, and measure how residual translates to forward error.

行列から粗視化するAMG：残差と解誤差を分ける: 正方形Poisson問題から得たSPD行列だけを階層構築へ渡し、平滑化集約AMGのV-cycleを実行します。7²・15²・31²未知数で独立疎行列直接解、解析的な離散正弦モード、連続解への2次収束を分けて検査します。 AMGの条件数・異方性・残差と前進誤差: 49・225・961未知数のSPD行列で、条件数と異方性を別々に変えます。解析スペクトル、独立疎行列直接解、DST対角化を比較し、同じ残差でも解誤差が条件数に依存することを確かめます。

- Matrix-based AMG: distinguish residual and solution error: https://hrkoyama.github.io/numerical-methods-atlas/validation/sa-amg/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/atlas-foundations-2026-11-22.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/results/result.json

- AMG: conditioning, anisotropy, residual and forward error: https://hrkoyama.github.io/numerical-methods-atlas/validation/amg-conditioning/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/atlas-foundations-conditioning-2026-11-22.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/results/result.json

Common execution records: [{"id": "sa-amg", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/sa-amg/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/sa-amg/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "amg-conditioning", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/amg-conditioning/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/amg-conditioning/?lang=en"}, "kind": "dedicated-supplement"}]

Next: Preserve the published fixed-input scope; validate conditions, references and criteria separately for extensions.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/amg/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/
