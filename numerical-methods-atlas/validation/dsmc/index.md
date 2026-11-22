# 等質DSMC衝突成分の保存則・Maxwell分布

等質なMaxwell分子のランダム二体衝突で、保存則と平衡分布への緩和を検証します。

**使用手法**

- [DSMC・運動論輸送](https://hrkoyama.github.io/numerical-methods-atlas/methods/dsmc/?lang=ja) (`dsmc`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc/?lang=ja#dsmc-ja-algorithm)

対の重心速度と相対速度の大きさを保持し、相対速度の方向を球面上で一様に選びます。roundは物理時刻ではなく衝突演算の回数です。 D=<vx²−(vy²+vz²)/2>と置くと、ランダムな相方の平均で重心の異方性が(N−2)/(2(N−1))倍になり、散乱後の相対方向の異方性期待値はゼロになるため、保存した期待減衰率が得られます。

$$
\mathbf v_{1,2}^{\prime}=\mathbf V\pm\frac{|\mathbf g|}{2}\mathbf n,\qquad|\mathbf n|=1
$$

$$
\mathbb E[D_{r+1}]=\frac{N-2}{2(N-1)}\mathbb E[D_r]
$$

方程式一覧の対応項目は未登録です。個別の式・近似・診断は上の定義に示します。

**問題の図**

![等質DSMC衝突成分の保存則・Maxwell分布：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/dsmc.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[等質DSMC衝突成分の保存則・Maxwell分布](https://hrkoyama.github.io/numerical-methods-atlas/problems/maxwell-collisions/?lang=ja) (`maxwell-collisions`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/maxwell-collisions/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc/?lang=ja#dsmc-ja-validation)

粒子512・2048・8192、16 seedで、運動量・運動エネルギー、Maxwellの2次/4次モーメント、Gamma(3/2,1)のエネルギーCDFを比較。異方性の期待減衰率(N−2)/(2(N−1))も独立に照合します。 有限Nの成分4次モーメントは3−6/(3N−1)であり、Maxwell値3との有限N偏りとseed間の標本誤差を区別します。

参照解一覧の対応カードは未登録です。この実行例の参照値・判定方法は上の検証資料で確認できます。
## 前提・単位・境界

等質・等質量・等方散乱・一定衝突率。各roundで全粒子を一度ずつランダムに組み合わせます。初期は±sqrt(3)の二つのビームで、温度の目標は1です。 各seedは総運動量0・総エネルギー固定のmicrocanonical系で、Maxwell/Gammaは大粒子数極限の参照です。

## 採用した計算法

対の重心速度と相対速度の大きさを保持し、相対速度の方向を球面上で一様に選びます。roundは物理時刻ではなく衝突演算の回数です。 D=<vx²−(vy²+vz²)/2>と置くと、ランダムな相方の平均で重心の異方性が(N−2)/(2(N−1))倍になり、散乱後の相対方向の異方性期待値はゼロになるため、保存した期待減衰率が得られます。

$$
\mathbf v_{1,2}^{\prime}=\mathbf V\pm\frac{|\mathbf g|}{2}\mathbf n,\qquad|\mathbf n|=1
$$

$$
\mathbb E[D_{r+1}]=\frac{N-2}{2(N-1)}\mathbb E[D_r]
$$

## 比較・検証

粒子512・2048・8192、16 seedで、運動量・運動エネルギー、Maxwellの2次/4次モーメント、Gamma(3/2,1)のエネルギーCDFを比較。異方性の期待減衰率(N−2)/(2(N−1))も独立に照合します。 有限Nの成分4次モーメントは3−6/(3N−1)であり、Maxwell値3との有限N偏りとseed間の標本誤差を区別します。

## 確認の限界

DSMCの衝突部分の教育例です。空間輸送、衝突セル、剛体球の速度依存の衝突選択、実際の輸送係数・流れ場・全seedでの保証は含みません。Bird原著の剛体球条件を再現したとは主張しません。

## 保存実測値と判定

```json
{
  "metrics": {
    "momentum_error": 1.2923689896027213e-16,
    "energy_error": 2.9605947323337516e-16,
    "variance_error": 0.008371767231336591,
    "fourth_moment_error": 0.06631754023150327,
    "energy_cdf_ks": 0.0017215082600027798,
    "anisotropy_error": 0.011017100788060268,
    "finest_particle_count": 8192,
    "seeds": 16
  },
  "checks": {
    "momentum_error": true,
    "energy_error": true,
    "variance_error": true,
    "fourth_moment_error": true,
    "energy_cdf_ks": true,
    "anisotropy_error": true,
    "sampling_uncertainty_decreases": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc/index.json

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

- G. A. Bird (1963). Approach to Translational Equilibrium in a Rigid Sphere Gas. https://doi.org/10.1063/1.1710976; review_level=metadata-only
  Sandiaの公式DSMC記念文書とDOI書誌を確認。出版社本文は取得できず、原著の剛体球モデルを再現したとは主張しません。

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Conservation and Maxwell relaxation in a homogeneous DSMC collision component

Test conservation and relaxation toward equilibrium through randomized pair collisions of homogeneous Maxwell molecules.

**Methods used**

- [DSMC and kinetic transport](https://hrkoyama.github.io/numerical-methods-atlas/methods/dsmc/?lang=en) (`dsmc`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc/?lang=en#dsmc-en-algorithm)

Preserve pair center-of-mass velocity and relative speed, then choose the new relative direction uniformly on the sphere. Rounds count collision operations and are not calibrated physical time. For D=<vx²−(vy²+vz²)/2>, averaging a random partner multiplies the center-of-mass anisotropy by (N−2)/(2(N−1)); isotropic postcollision relative directions contribute zero expected anisotropy.

$$
\mathbf v_{1,2}^{\prime}=\mathbf V\pm\frac{|\mathbf g|}{2}\mathbf n,\qquad|\mathbf n|=1
$$

$$
\mathbb E[D_{r+1}]=\frac{N-2}{2(N-1)}\mathbb E[D_r]
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![Conservation and Maxwell relaxation in a homogeneous DSMC collision component: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/dsmc.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Conservation and Maxwell relaxation in a homogeneous DSMC collision component](https://hrkoyama.github.io/numerical-methods-atlas/problems/maxwell-collisions/?lang=en) (`maxwell-collisions`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/maxwell-collisions/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc/?lang=en#dsmc-en-validation)

Use 512/2048/8192 particles and sixteen seeds to check momentum/energy, Maxwell second/fourth moments and the Gamma(3/2,1) energy CDF. Independently check the expected per-round anisotropy factor (N−2)/(2(N−1)). The finite-N component fourth moment is 3−6/(3N−1); distinguish that finite-particle offset from the across-seed sampling uncertainty.

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.
## Assumptions, units and boundaries

Homogeneous, equal masses, isotropic scattering and constant collision rate. Each round randomly matches every particle once. Two initial beams at ±sqrt(3) give target temperature one. Each seed has zero total momentum and fixed total energy: its finite-N equilibrium is microcanonical, while Maxwell/Gamma are large-N references.

## Adopted numerical method

Preserve pair center-of-mass velocity and relative speed, then choose the new relative direction uniformly on the sphere. Rounds count collision operations and are not calibrated physical time. For D=<vx²−(vy²+vz²)/2>, averaging a random partner multiplies the center-of-mass anisotropy by (N−2)/(2(N−1)); isotropic postcollision relative directions contribute zero expected anisotropy.

$$
\mathbf v_{1,2}^{\prime}=\mathbf V\pm\frac{|\mathbf g|}{2}\mathbf n,\qquad|\mathbf n|=1
$$

$$
\mathbb E[D_{r+1}]=\frac{N-2}{2(N-1)}\mathbb E[D_r]
$$

## References and validation

Use 512/2048/8192 particles and sixteen seeds to check momentum/energy, Maxwell second/fourth moments and the Gamma(3/2,1) energy CDF. Independently check the expected per-round anisotropy factor (N−2)/(2(N−1)). The finite-N component fourth moment is 3−6/(3N−1); distinguish that finite-particle offset from the across-seed sampling uncertainty.

## Limits

This is an educational DSMC collision component. No spatial streaming, collision cells, speed-dependent hard-sphere selection, measured transport coefficients/flow fields or every-seed guarantee. Bird’s original hard-sphere conditions are not reproduced.

## Stored measurements and decisions

```json
{
  "metrics": {
    "momentum_error": 1.2923689896027213e-16,
    "energy_error": 2.9605947323337516e-16,
    "variance_error": 0.008371767231336591,
    "fourth_moment_error": 0.06631754023150327,
    "energy_cdf_ks": 0.0017215082600027798,
    "anisotropy_error": 0.011017100788060268,
    "finest_particle_count": 8192,
    "seeds": 16
  },
  "checks": {
    "momentum_error": true,
    "energy_error": true,
    "variance_error": true,
    "fourth_moment_error": true,
    "energy_cdf_ks": true,
    "anisotropy_error": true,
    "sampling_uncertainty_decreases": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc/index.json

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

- G. A. Bird (1963). Approach to Translational Equilibrium in a Rigid Sphere Gas. https://doi.org/10.1063/1.1710976; review_level=metadata-only
  Official Sandia DSMC commemorative document and DOI metadata checked; publisher text unavailable and the original hard-sphere model is not claimed as reproduced.

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
