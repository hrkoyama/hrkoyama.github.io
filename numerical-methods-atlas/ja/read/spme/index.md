# Smooth PME（SPME）

SPMEは滑らかなcardinal B-splineによってEwald構造因子を格子上で近似します。PMEの同義語としてではなく、補間と力の定義を伴う変種として扱います。

## 対象と代表式

各座標の格子単位での粒子位置をuᵢとし、次数ではなくorderがpのcardinal B-spline Mₚを用います。下式の積は3方向の局所割当を表します。FFTで得る構造因子には、B-splineのFourier応答に応じた補正が必要です。

$$
Q_{m_xm_ym_z}=\sum_iq_i\prod_{d\in\{x,y,z\}}M_p(u_{id}-m_d),\qquad \deg M_p=p-1.
$$

## 計算の流れ

電荷をp個ずつの近傍格子へ割り当て、FFTと補正済み逆空間核から格子エネルギーを求めます。解析的微分ではB-splineの微分を使って粒子の力を計算します。次数・格子と合わせて、解析的微分かFourier空間微分かを記録します。

## 適用条件と落とし穴

滑らかな補間だけで、エネルギー保存と総運動量保存が同時に保証されるわけではありません。境界・中性条件・自己項はEwaldから引き継ぎます。原PMEとの比較では、格子数だけでなく同じ許容誤差になるまで各方式の条件をそろえます。

追加版もB-spline order 4/6の解析的エネルギー勾配型です。離散エネルギーと力の整合性、格子に対する平行移動依存と合力は別の観測量です。有限格子のaliasingにより合力は一般に厳密なゼロにならず、厳密な運動量保存を主張しません。

## 検証するときに見る量

同じ直接Ewald参照に対して力の誤差を測定し、エネルギーの位置差分でも確認します。平行移動に伴う格子誤差と総力を別々に報告します。実空間打切りの誤差が支配していないかも調べます。

16³・24³・40³の格子系列と複数の共通平行移動を、同じ直接Ewaldと独立theta参照に照合する設計です。割当重みの和・電荷、エネルギー差分、力のRMS/最大誤差、実空間打切りを区別し、長時間MDや原法PMEの根拠へ流用しません。

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

- Essmann, Ulrich and Perera, Lalith and Berkowitz, Max L. and Darden, Tom and Lee, Hsing and Pedersen, Lee G. (1995). A smooth particle mesh Ewald method. https://doi.org/10.1063/1.470117
- Darden, Tom and York, Darrin and Pedersen, Lee (1993). Particle mesh Ewald: An N log(N) method for Ewald sums in large systems. https://doi.org/10.1063/1.464397
