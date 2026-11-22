# 中性周期セルのEwald和と独立theta積分

3次元周期Coulomb相互作用の実空間和・逆空間和・自己項を実装し、分割パラメータと打切りを変えて検証します。

## 前提・単位・境界

立方セル・全電荷ゼロ・Coulomb定数1・導体境界（tin foil）。主例は非対称な8点電荷で、NaClの8イオン配置は別の解析照合用です。

## 採用した計算法

erfcで減衰する実空間和、Gaussian係数を持つ構造因子の逆格子和、−alpha/sqrt(pi) sum(q²)を加えます。力は各項の位置微分から求め、24成分を中心エネルギー差分と比較します。

$$
E=\frac12\sum_{ij\mathbf n}^{\prime}q_iq_j\frac{\operatorname{erfc}(\alpha r_{ij\mathbf n})}{r_{ij\mathbf n}}+\frac{2\pi}{V}\sum_{\mathbf k\ne0}\frac{e^{-k^2/(4\alpha^2)}}{k^2}|S(\mathbf k)|^2-\frac{\alpha}{\sqrt\pi}\sum_iq_i^2
$$

$$
M_{\rm NaCl}=\frac2{\sqrt\pi}\int_0^\infty[1-\vartheta_4(0,e^{-u^2})^3]du
$$

## 比較・検証

分割alphaを3点、実空間打切りを3点、逆空間打切りを4点で確認。NaClのMadelung定数は3次元和を呼ばない独立な1次元Jacobi-theta積分と照合し、求積の誤差推定も保存します。

## 確認の限界

非中性セル、背景補正、非直交セル、誘電率が有限の表面項、スラブ補正、応力、物質固有の力場は扱いません。

## 保存実測値と判定

```json
{
  "metrics": {
    "madelung_constant": 1.7475645946331826,
    "theta_reference": 1.7475645946331821,
    "theta_quadrature_error": 1.27151293921409e-13,
    "real_cutoff_force_last_change": 0.0,
    "madelung_error": 4.440892098500626e-16,
    "splitting_energy_difference": 5.329070518200751e-15,
    "splitting_force_difference": 3.8191672047105385e-14,
    "finite_difference_error": 1.7360424209300618e-09,
    "cutoff_force_last_change": 0.0,
    "net_force": 1.1546319456101628e-14
  },
  "checks": {
    "madelung_error": true,
    "splitting_energy_difference": true,
    "splitting_force_difference": true,
    "finite_difference_error": true,
    "cutoff_force_last_change": true,
    "net_force": true,
    "nonzero_forces": true,
    "real_cutoff_refines": true,
    "theta_reference_error_bound": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/ewald/index.json

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。

## 出典と確認範囲

- P. P. Ewald (1921). Die Berechnung optischer und elektrostatischer Gitterpotentiale. https://doi.org/10.1002/andp.19213690304; review_level=abstract-and-metadata
  出版社が返した書誌と原著の節見出しを確認。原著全文の監査はしていません。
- NIST Digital Library of Mathematical Functions (2026). §20.7(viii) Transformations of Lattice Parameter. https://dlmf.nist.gov/20.7#viii; review_level=official-documentation
  Jacobi thetaの格子パラメータ変換式を公式資料で確認。年は確認年。

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Neutral-cell Ewald sums and an independent theta integral

Implement real-space, reciprocal-space and self Ewald terms for neutral 3D periodic Coulomb charges; vary splitting and cutoffs.

## Assumptions, units and boundaries

Cubic cell, zero total charge, Coulomb constant one and conducting/tin-foil boundary. An asymmetric eight-charge case is distinct from the eight-ion NaCl reference cell.

## Adopted numerical method

Combine an erfc-screened image sum, Gaussian-damped reciprocal structure factors and the self correction. Differentiate each term and check all 24 force components against central energy differences.

$$
E=\frac12\sum_{ij\mathbf n}^{\prime}q_iq_j\frac{\operatorname{erfc}(\alpha r_{ij\mathbf n})}{r_{ij\mathbf n}}+\frac{2\pi}{V}\sum_{\mathbf k\ne0}\frac{e^{-k^2/(4\alpha^2)}}{k^2}|S(\mathbf k)|^2-\frac{\alpha}{\sqrt\pi}\sum_iq_i^2
$$

$$
M_{\rm NaCl}=\frac2{\sqrt\pi}\int_0^\infty[1-\vartheta_4(0,e^{-u^2})^3]du
$$

## References and validation

Three splitting parameters, three real cutoffs and four reciprocal cutoffs. Check the NaCl Madelung constant against a separately implemented 1D Jacobi-theta integral, storing its quadrature error estimate.

## Limits

No charged-cell/background correction, triclinic cell, finite-dielectric surface term, slab correction, stress or material-specific force field.

## Stored measurements and decisions

```json
{
  "metrics": {
    "madelung_constant": 1.7475645946331826,
    "theta_reference": 1.7475645946331821,
    "theta_quadrature_error": 1.27151293921409e-13,
    "real_cutoff_force_last_change": 0.0,
    "madelung_error": 4.440892098500626e-16,
    "splitting_energy_difference": 5.329070518200751e-15,
    "splitting_force_difference": 3.8191672047105385e-14,
    "finite_difference_error": 1.7360424209300618e-09,
    "cutoff_force_last_change": 0.0,
    "net_force": 1.1546319456101628e-14
  },
  "checks": {
    "madelung_error": true,
    "splitting_energy_difference": true,
    "splitting_force_difference": true,
    "finite_difference_error": true,
    "cutoff_force_last_change": true,
    "net_force": true,
    "nonzero_forces": true,
    "real_cutoff_refines": true,
    "theta_reference_error_bound": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/ewald/index.json

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group.

## Sources and review scope

- P. P. Ewald (1921). Die Berechnung optischer und elektrostatischer Gitterpotentiale. https://doi.org/10.1002/andp.19213690304; review_level=abstract-and-metadata
  Publisher metadata and original section headings checked; no full-text audit claimed.
- NIST Digital Library of Mathematical Functions (2026). §20.7(viii) Transformations of Lattice Parameter. https://dlmf.nist.gov/20.7#viii; review_level=official-documentation
  Official Jacobi-theta lattice-parameter transformations checked; year denotes access year.

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
