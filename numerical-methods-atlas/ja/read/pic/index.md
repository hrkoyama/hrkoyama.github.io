# Particle-in-Cell（PIC）

プラズマPICは速度分布を代表粒子で、自己無撞着な場を格子で表現します。粒子同士のCoulomb力をすべて直接足す方法とは、平滑化・衝突性・統計誤差が異なります。

## 対象と代表式

まず非相対論的・静電的なVlasov–Poisson系を考えます。代表粒子pの重みwₚ、電荷qₚ、位置xₚから格子電荷ρᵢを作ります。Sᵢは粒子形状から得る無次元割当係数でΣᵢSᵢ=1、Vᵢはセル体積です。E=−∇φとし、Poisson方程式を同じ境界条件で解きます。

$$
\rho_i=\frac1{V_i}\sum_p w_pq_pS_i(\mathbf x_p),\qquad -\nabla_h^2\phi_i=\rho_i/\epsilon_0,\qquad \dot{\mathbf v}_p=(q_p/m_p)\mathbf E_h(\mathbf x_p).
$$

## 計算の流れ

電荷の割当、Poisson解法、電場の粒子位置への補間、粒子の押し出しを繰り返します。背景イオンもρに含めます。電磁PICへ進む場合は電流割当とMaxwell更新を加え、離散連続の式との整合を確認します。Dawsonのシート模型は歴史的な粒子プラズマの例であり、全PIC方式の定義ではありません。

## 適用条件と落とし穴

陽的静電PICではプラズマ振動の時間尺度とDebye長の解像を調べます。必要条件は押し出し法・形状・場の解法で変わり、万能なΔtやセル幅はありません。粒子数を増やす統計収束と格子/時間刻みの収束を分け、自己力・有限格子加熱にも注意します。

追加版は静止した一様イオン背景を持つ1次元周期・静電cold-electron PICです。CIC割当・補間、Poisson場と粒子押し出しの固定例であり、熱的Landau減衰、電磁PIC、イオン運動は対象外です。

## 検証するときに見る量

単一粒子の自己力、中性一様分布、微小振幅のプラズマ振動やLandau減衰から始めます。総電荷、エネルギードリフト、粒子数依存と独立乱数系列を報告します。減衰率は理論の線形振幅域に限って比較します。

線形の冷たいプラズマ振動を小振幅の参照とし、格子・時間刻み・粒子数を分けて比較します。総電荷、場の残差、自己力、粒子運動量と粒子・場エネルギーの診断を別々に示します。保存診断の小ささだけで軌道精度や任意の長時間安定性を保証しません。

追加版では固定CIC空間系の運動をDOP853でも積分し、公差と最大刻みの感度を調べます。これは時間積分の別アルゴリズムによる照合であり、独立した連続Vlasov–Poissonソルバーではありません。粒子数の乱数検査は初期時刻の単一Fourier電荷モードのpowerが対象で、CICの有限格子応答を含めて解析期待値と比較します。粒子数増大による任意の非線形軌道の収束とは区別します。

## 固定入力の実行例と診断対照

受入条件が示す検証範囲と数学的な一般保証を区別します。旧版の入力・測定・公差は保持します。

### CIC静電PICの冷たいプラズマ振動

固定標的の計算例

1次元周期セルの電子をCICで格子と結び、Poisson方程式と粒子運動を自洽に進めます。

有限振幅・有限粒子数の誤差床があります。非線形不安定性、Landau減衰、衝突、電磁PIC、相対論粒子、境界流入出の検証ではありません。

[入力・結果・受入条件](/numerical-methods-atlas/validation/pic/?lang=ja) · [手法・一次文献](/numerical-methods-atlas/ja/read/validation-particles/#pic) · [コード run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/run.py) · [コード electrostatics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/electrostatics.py) · [コード fmm.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/fmm.py) · [コード transport.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/transport.py) · [テスト test_particles.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/test_particles.py) · [ZIP](/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip) · [結果](/code/validated-examples/2026-11-22/particles/results/result.json) · [追試記録](/code/validated-examples/2026-11-22/particles/verification.json)

### PIC：格子・時間収束、保存量と粒子雑音

固定標的の計算例

冷たい1次元周期プラズマのquiet-start収束と、独立seedでの初期粒子雑音を分け、電荷・運動量・Gauss則・エネルギー誤差を保存します。

DOP853は独立PIC空間実装ではありません。電荷・運動量の保持とエネルギーの近似保存を区別し、初期雑音のNスケーリングを時間発展した熱プラズマの保証としません。Landau減衰・電磁PIC・相対論・衝突は未検証です。

[入力・結果・受入条件](/numerical-methods-atlas/validation/pic-conservation/?lang=ja) · [手法・一次文献](/numerical-methods-atlas/ja/read/validation-particle-transport/#pic-conservation) · [コード run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/run.py) · [コード kinetic_experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/kinetic_experiments.py) · [コード kinetics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/kinetics.py) · [コード longrange_experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/longrange_experiments.py) · [コード electrostatics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/electrostatics.py) · [コード fmm.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/fmm.py) · [テスト test_kinetics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/test_kinetics.py) · [テスト test_longrange.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/test_longrange.py) · [テスト test_runner.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/test_runner.py) · [ZIP](/code/validated-examples/2026-11-22/particle-transport/atlas-particle-transport-2026-11-22.zip) · [結果](/code/validated-examples/2026-11-22/particle-transport/results/result.json) · [追試記録](/code/validated-examples/2026-11-22/particle-transport/verification.json)

## 公開範囲

従来の解説・式・文献と旧配布版を保持し、条件を固定した追加検証を別配布版として案内します。上の一般的な検証案すべてを実施したという意味ではありません。各版の入力・参照・合否・制約は専用ページと保存記録で確認してください。

## 文献

- John Dawson (1962). One-Dimensional Plasma Model. https://doi.org/10.1063/1.1706638
- Hockney, R. W. and Eastwood, J. W. (1981). Computer Simulation Using Particles. https://doi.org/10.1201/9780367806934
