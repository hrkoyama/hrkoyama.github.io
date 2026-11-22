# Particle Mesh Ewald（PME）

PMEはEwald法の逆空間項を粒子から格子へ移し、FFTを使う方法です。原PMEのLagrange補間と、後のSPMEのB-spline補間を区別して読みます。

## 対象と代表式

中性・3次元周期のCoulomb系で、格子点xₘに割り当てた電荷Qₘを考えます。Wₘは割当重み、ĜₕはEwaldのGaussian因子、格子規約、補間補正を含む逆空間作用素です。この模式式は逆空間部分だけで、実空間・自己項を置き換えません。

$$
Q_{\mathbf m}=\sum_iq_iW_{\mathbf m}(\mathbf r_i),\qquad\phi_h=\mathcal F_h^{-1}\!\left[\widehat G_h\,\mathcal F_h Q\right].
$$

## 計算の流れ

原法では局所Lagrange補間で電荷を格子へ割り当て、離散Fourier変換、格子上の畳み込み、逆変換を行います。力の微分方法と粒子への補間を一組として定義します。格子上で得た電場とエネルギー微分の力が、選んだ離散化で一致するとは限りません。

## 適用条件と落とし穴

格子を細かくする誤差、補間次数、Ewaldの打切り、力の微分規約を混ぜずに比較します。FFTの正規化とk=0、単位を明記します。O(N log N)は通常の格子増大の仮定を伴う計算量の説明で、精度の保証ではありません。

ここで結ぶ公開コードの採用形はB-splineの解析的エネルギー勾配を使うsmooth PMEです。1993年のLagrange補間PMEを実装・検証したという意味ではなく、元のPMEの式・文献・適用条件を保って別の採用変種へ案内します。

## 検証するときに見る量

同一の小さい中性セルについて、十分収束した直接Ewald和を参照にします。格子数・補間次数・分割定数を変え、エネルギーと力のRMS/最大誤差、平行移動依存性を調べます。重力PMの成功をPMEの検証に流用しません。

追加版では同じ中性周期電荷に対し格子数・B-spline order・共通平行移動を変え、収束した直接Ewaldと別実装theta積分に比較します。直接Ewaldとの共有実空間・自己項があるため、その一致だけを独立な全エネルギー検証とはしません。

## 固定入力の実行例と診断対照

受入条件が示す検証範囲と数学的な一般保証を区別します。旧版の入力・測定・公差は保持します。

### Bスプラインsmooth PMEの格子・次数収束

固定標的の計算例

電荷をBスプラインで格子へ割り当て、FFTでEwald逆空間項を評価するsmooth PME（SPME）の小規模例です。

有限格子のaliasingにより、エネルギー勾配型の合力は厳密にはゼロでなく、その診断量を保存します。運動量保存・長時間MD・原法PME・最適化P³M・スラブ補正の検証ではありません。

[入力・結果・受入条件](/numerical-methods-atlas/validation/spme/?lang=ja) · [手法・一次文献](/numerical-methods-atlas/ja/read/validation-particles/#spme) · [コード run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/run.py) · [コード electrostatics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/electrostatics.py) · [コード fmm.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/fmm.py) · [コード transport.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/transport.py) · [テスト test_particles.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/test_particles.py) · [ZIP](/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip) · [結果](/code/validated-examples/2026-11-22/particles/results/result.json) · [追試記録](/code/validated-examples/2026-11-22/particles/verification.json)

### SPME：格子・補間次数・格子位相と保存則

固定標的の計算例

BスプラインSPMEを同じ独立theta参照へ照合し、格子・次数・位相への依存、電荷の保持、エネルギー勾配と合力を測ります。

エネルギー勾配型では有限格子のaliasingにより合力は一般にゼロではありません。厳密な運動量保存や任意配置での同じ誤差、長時間MD、原法PME、SPME全変種の検証とはしません。

[入力・結果・受入条件](/numerical-methods-atlas/validation/spme-convergence/?lang=ja) · [手法・一次文献](/numerical-methods-atlas/ja/read/validation-particle-transport/#spme-convergence) · [コード run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/run.py) · [コード longrange_experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/longrange_experiments.py) · [コード electrostatics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/electrostatics.py) · [コード fmm.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/fmm.py) · [コード kinetic_experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/kinetic_experiments.py) · [コード kinetics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/kinetics.py) · [テスト test_kinetics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/test_kinetics.py) · [テスト test_longrange.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/test_longrange.py) · [テスト test_runner.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/test_runner.py) · [ZIP](/code/validated-examples/2026-11-22/particle-transport/atlas-particle-transport-2026-11-22.zip) · [結果](/code/validated-examples/2026-11-22/particle-transport/results/result.json) · [追試記録](/code/validated-examples/2026-11-22/particle-transport/verification.json)

## 公開範囲

従来の解説・式・文献と旧配布版を保持し、条件を固定した追加検証を別配布版として案内します。上の一般的な検証案すべてを実施したという意味ではありません。各版の入力・参照・合否・制約は専用ページと保存記録で確認してください。

## 文献

- Darden, Tom and York, Darrin and Pedersen, Lee (1993). Particle mesh Ewald: An N log(N) method for Ewald sums in large systems. https://doi.org/10.1063/1.464397
- Ewald, P. P. (1921). Die Berechnung optischer und elektrostatischer Gitterpotentiale. https://doi.org/10.1002/andp.19213690304
