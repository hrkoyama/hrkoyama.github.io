# DSMC・運動論輸送

DSMCは希薄気体のBoltzmann衝突を代表粒子の確率的な二体衝突で近似します。分子動力学の決定論的な粒子対ポテンシャル計算とも、場を解くプラズマPICとも異なります。

## 対象と代表式

Boltzmann方程式の分布f、分子速度v、外力加速度a、衝突積分Qを考えます。1代表粒子がF_N個の実分子を表し、体積V_cのセル内で断面積σ_Tと相対速度gに応じて衝突を標本化します。fは位相空間の粒子数密度の規約で定義します。

$$
\partial_t f+\mathbf v\cdot\nabla_x f+\mathbf a\cdot\nabla_v f=Q(f,f),\qquad P_{\rm pair}\sim \frac{F_N\sigma_T g\,\Delta t}{V_c}.
$$

## 計算の流れ

粒子を移動し、境界との相互作用を処理し、セル内で衝突候補を選んで散乱を標本化します。代表的なno-time-counter方式ではgσ_Tの上界に基づく候補数と棄却を使います。衝突モデルはhard sphere、VHSなどを明示し、Birdの初期の提案と後続アルゴリズムを区別します。

## 適用条件と落とし穴

希薄気体と分子混沌の仮定を用い、一般にはセル幅を平均自由行程、時間刻みを平均衝突時間と比較します。必要な解像は問題依存です。低速流では巨視的信号が熱運動の雑音に埋もれやすく、平均化時間を増やしてもバイアスは消えません。

追加版は位置を持たない等質Maxwell分子の弾性二体衝突roundです。断面積と相対速度を用いた物理時間のno-time-counter輸送、hard-sphereの空間運動、壁・流入境界の検証とは区別します。

## 検証するときに見る量

一様気体の速度緩和、Maxwell分布、壁面Couette流や希薄衝撃波で試します。衝突ごとの運動量・エネルギー保存、セル/刻み/粒子数依存、標本相関を含む不確かさを確認します。

有限粒子数で固定運動量・エネルギーを持つ球面のモーメントをここで導出し、独立な正規乱数の射影・正規化標本と衝突標本を比較します。Scalasらの論文は有限系のmicrocanonical分布と熱力学極限の区別の参考であり、そのhard-sphere計算全体の再現ではありません。独立seed間の不確かさと粒子数依存を、各衝突の運動量・エネルギー保存と分けます。

固定運動量・エネルギーの有限系では、単一成分の二乗を適切に規格化するとBeta分布になります。16・64・256粒子と64 seedでこの有限粒子数の基準を使い、Maxwell極限との有限Nバイアスを標本誤差から分けます。24衝突round後の分布比較であり、round数を物理時刻へ換算しません。

## 固定入力の実行例と診断対照

受入条件が示す検証範囲と数学的な一般保証を区別します。旧版の入力・測定・公差は保持します。

### 等質DSMC衝突成分の保存則・Maxwell分布

固定標的の計算例

等質なMaxwell分子のランダム二体衝突で、保存則と平衡分布への緩和を検証します。

DSMCの衝突部分の教育例です。空間輸送、衝突セル、剛体球の速度依存の衝突選択、実際の輸送係数・流れ場・全seedでの保証は含みません。Bird原著の剛体球条件を再現したとは主張しません。

[入力・結果・受入条件](/numerical-methods-atlas/validation/dsmc/?lang=ja) · [手法・一次文献](/numerical-methods-atlas/ja/read/validation-particles/#dsmc) · [コード run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/run.py) · [コード electrostatics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/electrostatics.py) · [コード fmm.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/fmm.py) · [コード transport.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/transport.py) · [テスト test_particles.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/test_particles.py) · [ZIP](/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip) · [結果](/code/validated-examples/2026-11-22/particles/results/result.json) · [追試記録](/code/validated-examples/2026-11-22/particles/verification.json)

### DSMC衝突成分：有限N平衡・保存則・統計誤差

固定標的の計算例

有限粒子数の平衡をMaxwell極限と区別し、独立な球面標本、解析的異方性減衰、seed間誤差と比較します。

固定した64seedの統計的診断であり、全seedの保証ではありません。同一seed内の粒子は保存量で相関し、IIDのKS p値へ読み替えません。空間輸送、衝突セル、剛体球の速度依存衝突選択・輸送係数は含みません。

[入力・結果・受入条件](/numerical-methods-atlas/validation/dsmc-statistics/?lang=ja) · [手法・一次文献](/numerical-methods-atlas/ja/read/validation-particle-transport/#dsmc-statistics) · [コード run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/run.py) · [コード kinetic_experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/kinetic_experiments.py) · [コード kinetics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/kinetics.py) · [コード longrange_experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/longrange_experiments.py) · [コード electrostatics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/electrostatics.py) · [コード fmm.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/fmm.py) · [テスト test_kinetics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/test_kinetics.py) · [テスト test_longrange.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/test_longrange.py) · [テスト test_runner.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/test_runner.py) · [ZIP](/code/validated-examples/2026-11-22/particle-transport/atlas-particle-transport-2026-11-22.zip) · [結果](/code/validated-examples/2026-11-22/particle-transport/results/result.json) · [追試記録](/code/validated-examples/2026-11-22/particle-transport/verification.json)

## 公開範囲

従来の解説・式・文献と旧配布版を保持し、条件を固定した追加検証を別配布版として案内します。上の一般的な検証案すべてを実施したという意味ではありません。各版の入力・参照・合否・制約は専用ページと保存記録で確認してください。

## 文献

- G. A. Bird (1963). Approach to Translational Equilibrium in a Rigid Sphere Gas. https://doi.org/10.1063/1.1710976
- G. A. Bird (1994). Molecular Gas Dynamics and the Direct Simulation of Gas Flows. https://global.oup.com/academic/product/molecular-gas-dynamics-and-the-direct-simulation-of-gas-flows-9780198561958
- Scalas, Enrico; Gabriel, Adrian T.; Martin, Edgar; Germano, Guido (2015). Velocity and energy distributions in microcanonical ensembles of hard spheres. https://doi.org/10.1103/PhysRevE.92.022140
