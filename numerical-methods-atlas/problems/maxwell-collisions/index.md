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

### 厳密解・参照解

等質衝突成分の運動量・エネルギー保存、異方性緩和と分布モーメントを確認します。有限粒子数の平衡はmicrocanonicalで、Maxwell/Gamma分布は大粒子数極限の基準です。空間輸送を含むBoltzmann方程式全体の厳密解検証ではありません。

#### 等質DSMC衝突成分の保存則・Maxwell分布

粒子512・2048・8192、16 seedで、運動量・運動エネルギー、Maxwellの2次/4次モーメント、Gamma(3/2,1)のエネルギーCDFを比較。異方性の期待減衰率(N−2)/(2(N−1))も独立に照合します。 有限Nの成分4次モーメントは3−6/(3N−1)であり、Maxwell値3との有限N偏りとseed間の標本誤差を区別します。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc/?lang=ja)

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

### Exact and reference solutions

Check momentum/energy conservation, anisotropy relaxation and distribution moments for the homogeneous collision component. Finite-particle equilibrium is microcanonical; Maxwell/Gamma distributions are large-N standards. This does not validate an exact solution of the full spatial Boltzmann equation.

#### Conservation and Maxwell relaxation in a homogeneous DSMC collision component

Use 512/2048/8192 particles and sixteen seeds to check momentum/energy, Maxwell second/fourth moments and the Gamma(3/2,1) energy CDF. Independently check the expected per-round anisotropy factor (N−2)/(2(N−1)). The finite-N component fourth moment is 3−6/(3N−1); distinguish that finite-particle offset from the across-seed sampling uncertainty.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc/?lang=en)

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
