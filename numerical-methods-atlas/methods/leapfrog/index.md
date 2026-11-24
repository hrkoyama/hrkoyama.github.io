# Two-step leapfrog / 2ステップleapfrog法

Status: educational-example

Read about Two-step leapfrog, follow the original references and inspect related educational code and checks. Additional fixed examples: Mie scattering width of a two-dimensional dielectric cylinder. See each release for assumptions and checked scope. Additional fixed examples: Oblique s/p incidence on a Lorentz-dispersive slab. See each release for assumptions and checked scope. Additional fixed examples: Long-time grazing PML in a dispersive medium. See each release for assumptions and checked scope.

「2ステップleapfrog法」の考え方と適用範囲を、解説章・一次文献・関連する教育用コードからたどります。 追加固定例：2D誘電体円柱のMie散乱幅。条件と検証範囲は各配布版で確認してください。 追加固定例：Lorentz分散板へのs/p斜め入射。条件と検証範囲は各配布版で確認してください。 追加固定例：分散媒質の浅い入射角と長時間PML。条件と検証範囲は各配布版で確認してください。

See the chapter and implementation for equations, boundaries and checked scope. Educational examples are not complete general-purpose solvers. Additional fixed examples: This is a lossless two-dimensional Ez cylinder, not a three-dimensional sphere. Report staircase geometry error without claiming general second-order curved-boundary accuracy or precision scattering for arbitrary frequencies and materials. Additional fixed examples: This is a genuine single-ky restriction rather than arbitrary transverse data. It covers one passive Lorentz pole and a fixed finite band/window. Gaussian tails are nonzero; window diagnostics and reference errors are reported separately. No strict all-frequency no-return proof is claimed. Additional fixed examples: The central angle is 80 degrees; finite kx bandwidth gives neighboring angles. The no-PML reference shares the discretization and initialization to isolate boundary error from bulk dispersion. Small operator and finite-trajectory checks do not prove global stability for arbitrary angles and materials. The joint family does not measure fixed-PML spatial order; the older 100 checks alone do not prove peak-12 global stability.

Other names: leapfrog法, リープフロッグ法, two step leapfrog

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/time-integration/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/time-integration/

- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/time_integration.py
- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/runge_kutta.py
- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/hamiltonian.py

- Reference: https://doi.org/10.1175/2009MWR2724.1 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.

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

Common execution records: [{"id": "cylinder-mie2d", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/cylinder-mie2d/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/cylinder-mie2d/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "lorentz-oblique-sp", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/lorentz-oblique-sp/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/lorentz-oblique-sp/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "dispersive-grazing-pml", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/dispersive-grazing-pml/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/dispersive-grazing-pml/?lang=en"}, "kind": "dedicated-supplement"}]

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/leapfrog/
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

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/time-integration/)


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

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### 関連ソース

- [/code/numerical-methods-atlas/2026-11-21/numart/time_integration.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/time_integration.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/runge_kutta.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/runge_kutta.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/hamiltonian.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/hamiltonian.py)
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

- [/code/numerical-methods-atlas/2026-11-21/tests/test_time_geometry.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_time_geometry.py)
- [/code/numerical-methods-atlas/2026-11-21/tests/test_runge_kutta.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_runge_kutta.py)
- [/code/numerical-methods-atlas/2026-11-21/tests/test_hamiltonian.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_hamiltonian.py)
- [/code/validated-examples/2026-11-24-r2/maxwell-cylinder/test_cylinder.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-cylinder/test_cylinder.py)
- [/code/validated-examples/2026-11-24-r2/maxwell-lorentz/test_lorentz.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/test_lorentz.py)
- [/code/validated-examples/2026-11-24-r2/maxwell-grazing/test_grazing.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/test_grazing.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q tests/test_time_geometry.py tests/test_runge_kutta.py tests/test_hamiltonian.py
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

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/time-integration/)


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

[Related code edition / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### Related source

- [/code/numerical-methods-atlas/2026-11-21/numart/time_integration.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/time_integration.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/runge_kutta.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/runge_kutta.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/hamiltonian.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/hamiltonian.py)
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

- [/code/numerical-methods-atlas/2026-11-21/tests/test_time_geometry.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_time_geometry.py)
- [/code/numerical-methods-atlas/2026-11-21/tests/test_runge_kutta.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_runge_kutta.py)
- [/code/numerical-methods-atlas/2026-11-21/tests/test_hamiltonian.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_hamiltonian.py)
- [/code/validated-examples/2026-11-24-r2/maxwell-cylinder/test_cylinder.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-cylinder/test_cylinder.py)
- [/code/validated-examples/2026-11-24-r2/maxwell-lorentz/test_lorentz.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/test_lorentz.py)
- [/code/validated-examples/2026-11-24-r2/maxwell-grazing/test_grazing.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/test_grazing.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q tests/test_time_geometry.py tests/test_runge_kutta.py tests/test_hamiltonian.py
```
