# 等質DSMC衝突成分の保存則・Maxwell分布 / Conservation and Maxwell relaxation in a homogeneous DSMC collision component

https://hrkoyama.github.io/numerical-methods-atlas/problems/maxwell-collisions/

## 日本語

[等質なMaxwell分子の衝突成分。512/2048/8192粒子・16seedの保存モーメント誤差・標本不確かさと、物理時刻ではない衝突roundごとの異方性緩和。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/dsmc.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-particles/#dsmc) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#maxwell-collisions)

### 方程式・問題の定義

等質Boltzmann衝突演算子をDSMCで標本化する成分検査です。格子BGKとは異なる衝突モデルのため代用リンクを設けません。

#### 等質DSMC衝突成分の保存則・Maxwell分布

補助実行例 · 実行例の定義・検証式

$$
\mathbf v_{1,2}^{\prime}=\mathbf V\pm\frac{|\mathbf g|}{2}\mathbf n,\qquad|\mathbf n|=1
$$

$$
\mathbb E[D_{r+1}]=\frac{N-2}{2(N-1)}\mathbb E[D_r]
$$

等質なMaxwell分子のランダム二体衝突で、保存則と平衡分布への緩和を検証します。

#### DSMC衝突成分：有限N平衡・保存則・統計誤差

補助実行例 · 実行例の定義・検証式

$$
\frac{e_i}{3(N-1)/2}\sim\mathrm{Beta}\!\left(\frac32,\frac{3(N-2)}2\right)
$$

$$
\mathbb E[v_x^4]=\frac{9(N-1)}{3N-1},\qquad\mathbb E[D_r]=3\left[\frac{N-2}{2(N-1)}\right]^r
$$

$$
e_i=|\mathbf v_i|^2/2,\qquad D_r=\langle v_x^2-(v_y^2+v_z^2)/2\rangle_r
$$

有限粒子数の平衡をMaxwell極限と区別し、独立な球面標本、解析的異方性減衰、seed間誤差と比較します。

### 厳密解・参照解

等質衝突成分の運動量・エネルギー保存、異方性緩和と分布モーメントを確認します。有限粒子数の平衡はmicrocanonicalで、Maxwell/Gamma分布は大粒子数極限の基準です。空間輸送を含むBoltzmann方程式全体の厳密解検証ではありません。 追加版は固定運動量・エネルギー球面の有限粒子数モーメントを導出し、独立な射影正規標本と複数seedで比較します。衝突roundは物理時間ではなく、hard-sphere空間輸送へ対応を広げません。

#### 等質DSMC衝突成分の保存則・Maxwell分布

粒子512・2048・8192、16 seedで、運動量・運動エネルギー、Maxwellの2次/4次モーメント、Gamma(3/2,1)のエネルギーCDFを比較。異方性の期待減衰率(N−2)/(2(N−1))も独立に照合します。 有限Nの成分4次モーメントは3−6/(3N−1)であり、Maxwell値3との有限N偏りとseed間の標本誤差を区別します。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc/?lang=ja)

#### DSMC衝突成分：有限N平衡・保存則・統計誤差

全roundの運動量・エネルギーの最大保存誤差は決定論的な許容値で検査します。最初の6roundの異方性、4点のエネルギーCDF、4次モーメントと有限NのBeta参照との差は、独立seed間の標準誤差で測ります。NによるCDF標準誤差の減少と、有限NからMaxwellへの偏りを分けます。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-statistics/?lang=ja)

### 計算法

この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。

- [DSMC・運動論輸送](https://hrkoyama.github.io/numerical-methods-atlas/methods/dsmc/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [等質DSMC衝突成分の保存則・Maxwell分布](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc/?lang=ja)

補助実行例

等質なMaxwell分子のランダム二体衝突で、保存則と平衡分布への緩和を検証します。

等質・等質量・等方散乱・一定衝突率。各roundで全粒子を一度ずつランダムに組み合わせます。初期は±sqrt(3)の二つのビームで、温度の目標は1です。 各seedは総運動量0・総エネルギー固定のmicrocanonical系で、Maxwell/Gammaは大粒子数極限の参照です。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

DSMCの衝突部分の教育例です。空間輸送、衝突セル、剛体球の速度依存の衝突選択、実際の輸送係数・流れ場・全seedでの保証は含みません。Bird原著の剛体球条件を再現したとは主張しません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-22/particles/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/run.py)
- [/code/validated-examples/2026-11-22/particles/test_particles.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/test_particles.py)

#### [DSMC衝突成分：有限N平衡・保存則・統計誤差](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-statistics/?lang=ja)

補助実行例

有限粒子数の平衡をMaxwell極限と区別し、独立な球面標本、解析的異方性減衰、seed間誤差と比較します。

等質・等質量・等方散乱のMaxwell分子、N=16/64/256、独立64seed、運動量0、sum|v|²=3N。二つのビームから24round衝突させ、roundは物理時間へ換算しません。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/atlas-particle-transport-2026-11-22.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

固定した64seedの統計的診断であり、全seedの保証ではありません。同一seed内の粒子は保存量で相関し、IIDのKS p値へ読み替えません。空間輸送、衝突セル、剛体球の速度依存衝突選択・輸送係数は含みません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-22/particle-transport/kinetic_experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/kinetic_experiments.py)
- [/code/validated-examples/2026-11-22/particle-transport/kinetics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/kinetics.py)
- [/code/validated-examples/2026-11-22/particle-transport/test_kinetics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/test_kinetics.py)
- [/code/validated-examples/2026-11-22/particle-transport/test_longrange.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/test_longrange.py)
- [/code/validated-examples/2026-11-22/particle-transport/test_runner.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/test_runner.py)

## English

[Homogeneous Maxwell-molecule collision component: stored moment errors/seed uncertainty for 512/2048/8192 particles over 16 seeds, and anisotropy per collision round, not physical time.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/dsmc.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-particles/#dsmc) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#maxwell-collisions-en)

### Equations and problem definitions

A component test sampling the homogeneous Boltzmann collision operator by DSMC. Lattice BGK uses a different collision model and is not substituted.

#### Conservation and Maxwell relaxation in a homogeneous DSMC collision component

Supplementary execution example · Example definition or validation formula

$$
\mathbf v_{1,2}^{\prime}=\mathbf V\pm\frac{|\mathbf g|}{2}\mathbf n,\qquad|\mathbf n|=1
$$

$$
\mathbb E[D_{r+1}]=\frac{N-2}{2(N-1)}\mathbb E[D_r]
$$

Test conservation and relaxation toward equilibrium through randomized pair collisions of homogeneous Maxwell molecules.

#### DSMC collision component: finite-N equilibrium, invariants and statistical error

Supplementary execution example · Example definition or validation formula

$$
\frac{e_i}{3(N-1)/2}\sim\mathrm{Beta}\!\left(\frac32,\frac{3(N-2)}2\right)
$$

$$
\mathbb E[v_x^4]=\frac{9(N-1)}{3N-1},\qquad\mathbb E[D_r]=3\left[\frac{N-2}{2(N-1)}\right]^r
$$

$$
e_i=|\mathbf v_i|^2/2,\qquad D_r=\langle v_x^2-(v_y^2+v_z^2)/2\rangle_r
$$

Distinguish finite-particle equilibrium from the Maxwell limit; compare independent sphere samples, analytic anisotropy decay and across-seed uncertainty.

### Exact and reference solutions

Check momentum/energy conservation, anisotropy relaxation and distribution moments for the homogeneous collision component. Finite-particle equilibrium is microcanonical; Maxwell/Gamma distributions are large-N standards. This does not validate an exact solution of the full spatial Boltzmann equation. The companion derives finite-particle moments on a fixed-momentum/energy sphere and compares independent projected-Gaussian samples across seeds. Collision rounds are not physical time, and the correspondence does not extend to spatial hard-sphere transport.

#### Conservation and Maxwell relaxation in a homogeneous DSMC collision component

Use 512/2048/8192 particles and sixteen seeds to check momentum/energy, Maxwell second/fourth moments and the Gamma(3/2,1) energy CDF. Independently check the expected per-round anisotropy factor (N−2)/(2(N−1)). The finite-N component fourth moment is 3−6/(3N−1); distinguish that finite-particle offset from the across-seed sampling uncertainty.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc/?lang=en)

#### DSMC collision component: finite-N equilibrium, invariants and statistical error

Check maximum momentum/energy errors over all rounds against deterministic tolerances. Use independent-seed standard errors for six-round anisotropy, four energy-CDF points and fourth moments against the finite-N beta reference. Separate decreasing CDF sampling error with N from finite-N Maxwell bias.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-statistics/?lang=en)

### Numerical methods

Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.

- [DSMC and kinetic transport](https://hrkoyama.github.io/numerical-methods-atlas/methods/dsmc/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Conservation and Maxwell relaxation in a homogeneous DSMC collision component](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc/?lang=en)

Supplementary execution example

Test conservation and relaxation toward equilibrium through randomized pair collisions of homogeneous Maxwell molecules.

Homogeneous, equal masses, isotropic scattering and constant collision rate. Each round randomly matches every particle once. Two initial beams at ±sqrt(3) give target temperature one. Each seed has zero total momentum and fixed total energy: its finite-N equilibrium is microcanonical, while Maxwell/Gamma are large-N references.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This is an educational DSMC collision component. No spatial streaming, collision cells, speed-dependent hard-sphere selection, measured transport coefficients/flow fields or every-seed guarantee. Bird’s original hard-sphere conditions are not reproduced.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-22/particles/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/run.py)
- [/code/validated-examples/2026-11-22/particles/test_particles.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/test_particles.py)

#### [DSMC collision component: finite-N equilibrium, invariants and statistical error](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-statistics/?lang=en)

Supplementary execution example

Distinguish finite-particle equilibrium from the Maxwell limit; compare independent sphere samples, analytic anisotropy decay and across-seed uncertainty.

Homogeneous equal-mass isotropic Maxwell collisions; N=16/64/256, 64 independent seeds, zero momentum and sum|v|²=3N. Start with two beams and run 24 collision rounds; rounds are not calibrated physical time.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/atlas-particle-transport-2026-11-22.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

Statistical diagnostics cover fixed 64-seed ensembles, not every seed. Conservation correlates particles within a seed; do not use IID KS p-values. No spatial streaming, collision cells, speed-dependent hard-sphere selection or transport coefficients.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-22/particle-transport/kinetic_experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/kinetic_experiments.py)
- [/code/validated-examples/2026-11-22/particle-transport/kinetics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/kinetics.py)
- [/code/validated-examples/2026-11-22/particle-transport/test_kinetics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/test_kinetics.py)
- [/code/validated-examples/2026-11-22/particle-transport/test_longrange.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/test_longrange.py)
- [/code/validated-examples/2026-11-22/particle-transport/test_runner.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/test_runner.py)
