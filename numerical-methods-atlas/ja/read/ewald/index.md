# Ewald法

Ewald法は、条件付き収束する周期Coulomb相互作用の和を、短距離の実空間和と滑らかな逆空間和に分ける方法です。有限半径で1/rを切ることとは、境界値問題が異なります。

## 対象と代表式

中性の3次元周期セルにある点電荷qᵢを考えます。rᵢⱼₙ=rᵢ−rⱼ+n、セル体積V、分割定数α>0、逆格子ベクトルk、S(k)=Σⱼqⱼexp(ik·rⱼ)とします。下式はCoulomb定数を1にしたエネルギーで、k=0を除き、巨視的境界を導体極限とした場合です。プライムはi=jかつn=0だけを除きます。

$$
\begin{aligned}S(\mathbf k)&=\sum_jq_j e^{i\mathbf k\cdot\mathbf r_j},\\E&=\frac12\sum_{i,j,\mathbf n}^{\prime}q_iq_j\frac{\operatorname{erfc}(\alpha r_{ij\mathbf n})}{r_{ij\mathbf n}}+\frac{2\pi}{V}\sum_{\mathbf k\ne0}\frac{e^{-k^2/(4\alpha^2)}}{k^2}|S(\mathbf k)|^2-\frac{\alpha}{\sqrt\pi}\sum_iq_i^2.\end{aligned}
$$

## 計算の流れ

erfcで減衰する実空間項を近接像まで、Gaussianで減衰する逆空間項を有限波数まで足し、自己エネルギーを引きます。実装単位系では全項に同じCoulomb係数を掛けます。αを変えると両和への仕事の配分が変わりますが、収束した総和は変わりません。力は同じエネルギー規約から微分します。

## 適用条件と落とし穴

正味電荷がある場合は、背景電荷など追加の規約なしにはこの式を使えません。平均電位のゲージ、表面項、自己像、分子内除外は別々に指定します。重力の周期Poisson問題は核・符号・平均密度の扱いが異なるため、そのまま置き換えません。

別配布版の対象も、中性の非対称8点電荷・立方体・3次元周期・tin-foil境界です。直接Ewaldの分割係数と実空間像・逆空間立方打切りを分け、熱核theta積分を別実装の参照にします。非中性背景やslabの検証へ広げません。

## 検証するときに見る量

小さい中性配置で実空間・逆空間の打切りを独立に伸ばし、α依存が消えることを確認します。エネルギーの位置差分と力、全体平行移動に対する不変性、総力を比較します。収束前の和同士の一致は独立検証ではありません。

旧版と追加版の入力・公差・結果は別々に保持します。追加版ではエネルギーと全粒子力、参照積分自身の細分化、平行移動・粒子順序・合力とエネルギー差分を個別に照合し、意図的な低打切り対照を収束済み参照と区別します。

## 固定入力の実行例と診断対照

受入条件が示す検証範囲と数学的な一般保証を区別します。旧版の入力・測定・公差は保持します。

### 中性周期セルのEwald和と独立theta積分

固定標的の計算例

3次元周期Coulomb相互作用の実空間和・逆空間和・自己項を実装し、分割パラメータと打切りを変えて検証します。

非中性セル、背景補正、非直交セル、誘電率が有限の表面項、スラブ補正、応力、物質固有の力場は扱いません。

[入力・結果・受入条件](/numerical-methods-atlas/validation/ewald/?lang=ja) · [手法・一次文献](/numerical-methods-atlas/ja/read/validation-particles/#ewald) · [コード run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/run.py) · [コード electrostatics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/electrostatics.py) · [コード fmm.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/fmm.py) · [コード transport.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/transport.py) · [テスト test_particles.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/test_particles.py) · [ZIP](/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip) · [結果](/code/validated-examples/2026-11-22/particles/results/result.json) · [追試記録](/code/validated-examples/2026-11-22/particles/verification.json)

### Ewald：非対称周期セルのエネルギー・力と独立theta積分

固定標的の計算例

中性8電荷の全エネルギーと24力成分を、別実装のGaussian/theta積分と比較。分割・実空間・逆空間の打切り、保存則と不変性を分けて測定します。

固定した中性立方セルだけです。上限感度は厳密な全配置の裾誤差保証ではありません。theta参照は別定式化の自作実装であり、第三者計算パッケージや公表された参照数表ではありません。非中性・非直交・スラブ・応力・長時間MDは対象外です。

[入力・結果・受入条件](/numerical-methods-atlas/validation/ewald-convergence/?lang=ja) · [手法・一次文献](/numerical-methods-atlas/ja/read/validation-particle-transport/#ewald-convergence) · [コード run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/run.py) · [コード longrange_experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/longrange_experiments.py) · [コード electrostatics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/electrostatics.py) · [コード fmm.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/fmm.py) · [コード kinetic_experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/kinetic_experiments.py) · [コード kinetics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/kinetics.py) · [テスト test_kinetics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/test_kinetics.py) · [テスト test_longrange.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/test_longrange.py) · [テスト test_runner.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/test_runner.py) · [ZIP](/code/validated-examples/2026-11-22/particle-transport/atlas-particle-transport-2026-11-22.zip) · [結果](/code/validated-examples/2026-11-22/particle-transport/results/result.json) · [追試記録](/code/validated-examples/2026-11-22/particle-transport/verification.json)

## 公開範囲

従来の解説・式・文献と旧配布版を保持し、条件を固定した追加検証を別配布版として案内します。上の一般的な検証案すべてを実施したという意味ではありません。各版の入力・参照・合否・制約は専用ページと保存記録で確認してください。

## 文献

- Ewald, P. P. (1921). Die Berechnung optischer und elektrostatischer Gitterpotentiale. https://doi.org/10.1002/andp.19213690304
- Hockney, R. W. and Eastwood, J. W. (1981). Computer Simulation Using Particles. https://doi.org/10.1201/9780367806934
