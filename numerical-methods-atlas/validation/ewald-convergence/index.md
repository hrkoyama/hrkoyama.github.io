# Ewald：非対称周期セルのエネルギー・力と独立theta積分

中性8電荷の全エネルギーと24力成分を、別実装のGaussian/theta積分と比較。分割・実空間・逆空間の打切り、保存則と不変性を分けて測定します。

**使用手法**

- [Ewald法](https://hrkoyama.github.io/numerical-methods-atlas/methods/ewald/?lang=ja) (`ewald`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/ewald-convergence/?lang=ja#ewald-convergence-ja-algorithm)

erfcと逆空間和による主計算とは別に、1/rのGaussian積分と1次元theta関数の積を数値積分します。小さい積分変数ではPoisson変換と中性条件、大きい側では自己項を引いた像和を使い、力はthetaの解析微分から積分します。

$$
E=\frac{1}{\sqrt\pi}\int_0^\infty\left[\sum_{ij}q_iq_j\Theta(\mathbf r_i-\mathbf r_j,u)-\sum_iq_i^2\right]du
$$

$$
\mathbf F_i=-\nabla_iE
$$

方程式一覧の対応項目は未登録です。個別の式・近似・診断は上の定義に示します。

**問題の図**

![Ewald：非対称周期セルのエネルギー・力と独立theta積分：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/results/ewald-convergence.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[中性周期点電荷：Ewald・smooth PME](https://hrkoyama.github.io/numerical-methods-atlas/problems/neutral-periodic-charges/?lang=ja) (`neutral-periodic-charges`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/neutral-periodic-charges/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/ewald-convergence/?lang=ja#ewald-convergence-ja-validation)

参照の求積・theta/像の打切り・切替点をまとめて精密化し、上限32→40の感度を別に記録します。alpha3点、実空間4点・逆空間5点、平行移動・並べ替え、合力、エネルギー差分の3成分を比較。粗い打切りの不正確さを検出する対照も残します。

参照解一覧の対応カードは未登録です。この実行例の参照値・判定方法は上の検証資料で確認できます。
## 前提・単位・境界

Coulomb定数1、単位立方体の3次元周期、全電荷0、tin-foil境界。旧版と同じ非対称配置です。独立参照も同じ零モードと自己項の規約を使います。

**編集上の補足**

非対称な中性立方セルの全エネルギー・全24力成分を、別実装のGaussian/theta積分と比較します。積分・打切り・上限の感度は、この固定配置での確認です。

## 採用した計算法

erfcと逆空間和による主計算とは別に、1/rのGaussian積分と1次元theta関数の積を数値積分します。小さい積分変数ではPoisson変換と中性条件、大きい側では自己項を引いた像和を使い、力はthetaの解析微分から積分します。

$$
E=\frac{1}{\sqrt\pi}\int_0^\infty\left[\sum_{ij}q_iq_j\Theta(\mathbf r_i-\mathbf r_j,u)-\sum_iq_i^2\right]du
$$

$$
\mathbf F_i=-\nabla_iE
$$

## 比較・検証

参照の求積・theta/像の打切り・切替点をまとめて精密化し、上限32→40の感度を別に記録します。alpha3点、実空間4点・逆空間5点、平行移動・並べ替え、合力、エネルギー差分の3成分を比較。粗い打切りの不正確さを検出する対照も残します。

## 確認の限界

固定した中性立方セルだけです。上限感度は厳密な全配置の裾誤差保証ではありません。theta参照は別定式化の自作実装であり、第三者計算パッケージや公表された参照数表ではありません。非中性・非直交・スラブ・応力・長時間MDは対象外です。

## 保存実測値と判定

```json
{
  "metrics": {
    "reference_energy": -8.407406514350587,
    "reference_energy_refinement": 0.0,
    "reference_force_refinement": 1.7763568394002505e-15,
    "reference_tail_energy": 0.0,
    "reference_tail_force": 1.7763568394002505e-15,
    "reference_quadrature_estimate": 9.6957684120808e-13,
    "energy_error": 3.552713678800501e-15,
    "force_error": 1.2434497875801753e-14,
    "splitting_energy_spread": 3.552713678800501e-15,
    "splitting_force_spread": 7.105427357601002e-14,
    "real_refinement_ratio": 1.520413841404234e-14,
    "reciprocal_refinement_ratio": 4.647403985774097e-13,
    "translation_energy": 3.552713678800501e-15,
    "translation_force": 4.440892098500626e-15,
    "permutation_force": 1.7763568394002505e-15,
    "net_force": 2.842170943040401e-14,
    "gradient_error": 6.119158513229195e-10,
    "control_force_error": 0.8224115526909029
  },
  "checks": {
    "reference_energy_refinement": true,
    "reference_force_refinement": true,
    "reference_tail_energy": true,
    "reference_tail_force": true,
    "reference_quadrature_estimate": true,
    "energy_error": true,
    "force_error": true,
    "splitting_energy_spread": true,
    "splitting_force_spread": true,
    "translation_energy": true,
    "translation_force": true,
    "permutation_force": true,
    "net_force": true,
    "gradient_error": true,
    "real_refinement_ratio": true,
    "reciprocal_refinement_ratio": true,
    "truncation_control_detected": true,
    "asymmetric_forces_nonzero": true,
    "reference_quadrature_converged": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/ewald-convergence/index.json

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/atlas-particle-transport-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。

入力・検証手順の履歴：https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/protocol-history.json

https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/inputs.json

## 出典と確認範囲

- P. P. Ewald (1921). Die Berechnung optischer und elektrostatischer Gitterpotentiale. https://doi.org/10.1002/andp.19213690304; review_level=abstract-and-metadata
  出版社が返した書誌と原著の節見出しを確認。原著全文の監査はしていません。
- NIST Digital Library of Mathematical Functions (2026). §20.7(viii) Transformations of Lattice Parameter. https://dlmf.nist.gov/20.7#viii; review_level=official-documentation
  Jacobi thetaの格子パラメータ変換式を公式資料で確認。年は確認年。

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Ewald: asymmetric-cell energies and forces versus independent theta integration

Compare a neutral eight-charge cell energy and all 24 force components with a separately coded Gaussian/theta integral. Separate splitting and real/reciprocal truncation from invariants and conservation.

**Methods used**

- [Ewald summation](https://hrkoyama.github.io/numerical-methods-atlas/methods/ewald/?lang=en) (`ewald`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/ewald-convergence/?lang=en#ewald-convergence-en-algorithm)

Independently integrate the Gaussian representation of 1/r and products of one-dimensional theta sums. Use a Poisson transform and analytic neutrality cancellation at small integration arguments, and self-subtracted image sums at large arguments. Integrate analytic theta derivatives for forces.

$$
E=\frac{1}{\sqrt\pi}\int_0^\infty\left[\sum_{ij}q_iq_j\Theta(\mathbf r_i-\mathbf r_j,u)-\sum_iq_i^2\right]du
$$

$$
\mathbf F_i=-\nabla_iE
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![Ewald: asymmetric-cell energies and forces versus independent theta integration: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/results/ewald-convergence.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Neutral periodic charges: Ewald and smooth PME](https://hrkoyama.github.io/numerical-methods-atlas/problems/neutral-periodic-charges/?lang=en) (`neutral-periodic-charges`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/neutral-periodic-charges/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/ewald-convergence/?lang=en#ewald-convergence-en-validation)

Record combined refinement of reference quadrature/theta/image/switch controls and a separate upper-limit 32-to-40 sensitivity. Compare three alpha values, four real and five reciprocal cutoffs, translation/permutation, net force and three energy-difference derivatives. Retain an intentionally inaccurate coarse-cutoff control.

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.
## Assumptions, units and boundaries

Coulomb constant one; unit cubic 3D periodic neutral cell with tin-foil boundary. The asymmetric configuration matches the earlier example; reference zero-mode and self conventions match the model.

**Editorial clarification**

Compare the asymmetric neutral cubic-cell energy and all 24 force components with a separately coded Gaussian/theta integral. Quadrature, truncation and upper-tail sensitivity apply to this fixed configuration.

## Adopted numerical method

Independently integrate the Gaussian representation of 1/r and products of one-dimensional theta sums. Use a Poisson transform and analytic neutrality cancellation at small integration arguments, and self-subtracted image sums at large arguments. Integrate analytic theta derivatives for forces.

$$
E=\frac{1}{\sqrt\pi}\int_0^\infty\left[\sum_{ij}q_iq_j\Theta(\mathbf r_i-\mathbf r_j,u)-\sum_iq_i^2\right]du
$$

$$
\mathbf F_i=-\nabla_iE
$$

## References and validation

Record combined refinement of reference quadrature/theta/image/switch controls and a separate upper-limit 32-to-40 sensitivity. Compare three alpha values, four real and five reciprocal cutoffs, translation/permutation, net force and three energy-difference derivatives. Retain an intentionally inaccurate coarse-cutoff control.

## Limits

One fixed neutral cubic cell. Upper-limit sensitivity is not a rigorous tail bound for arbitrary configurations. The theta reference is an independently formulated original implementation, not an external package or published numerical table. Charged/triclinic/slab cells, stress and long MD are outside scope.

## Stored measurements and decisions

```json
{
  "metrics": {
    "reference_energy": -8.407406514350587,
    "reference_energy_refinement": 0.0,
    "reference_force_refinement": 1.7763568394002505e-15,
    "reference_tail_energy": 0.0,
    "reference_tail_force": 1.7763568394002505e-15,
    "reference_quadrature_estimate": 9.6957684120808e-13,
    "energy_error": 3.552713678800501e-15,
    "force_error": 1.2434497875801753e-14,
    "splitting_energy_spread": 3.552713678800501e-15,
    "splitting_force_spread": 7.105427357601002e-14,
    "real_refinement_ratio": 1.520413841404234e-14,
    "reciprocal_refinement_ratio": 4.647403985774097e-13,
    "translation_energy": 3.552713678800501e-15,
    "translation_force": 4.440892098500626e-15,
    "permutation_force": 1.7763568394002505e-15,
    "net_force": 2.842170943040401e-14,
    "gradient_error": 6.119158513229195e-10,
    "control_force_error": 0.8224115526909029
  },
  "checks": {
    "reference_energy_refinement": true,
    "reference_force_refinement": true,
    "reference_tail_energy": true,
    "reference_tail_force": true,
    "reference_quadrature_estimate": true,
    "energy_error": true,
    "force_error": true,
    "splitting_energy_spread": true,
    "splitting_force_spread": true,
    "translation_energy": true,
    "translation_force": true,
    "permutation_force": true,
    "net_force": true,
    "gradient_error": true,
    "real_refinement_ratio": true,
    "reciprocal_refinement_ratio": true,
    "truncation_control_detected": true,
    "asymmetric_forces_nonzero": true,
    "reference_quadrature_converged": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/ewald-convergence/index.json

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/atlas-particle-transport-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group.

Input and validation protocol history: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/protocol-history.json

https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/inputs.json

## Sources and review scope

- P. P. Ewald (1921). Die Berechnung optischer und elektrostatischer Gitterpotentiale. https://doi.org/10.1002/andp.19213690304; review_level=abstract-and-metadata
  Publisher metadata and original section headings checked; no full-text audit claimed.
- NIST Digital Library of Mathematical Functions (2026). §20.7(viii) Transformations of Lattice Parameter. https://dlmf.nist.gov/20.7#viii; review_level=official-documentation
  Official Jacobi-theta lattice-parameter transformations checked; year denotes access year.

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
