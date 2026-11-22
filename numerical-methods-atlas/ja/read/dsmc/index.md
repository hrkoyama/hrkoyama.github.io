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

## 検証するときに見る量

一様気体の速度緩和、Maxwell分布、壁面Couette流や希薄衝撃波で試します。衝突ごとの運動量・エネルギー保存、セル/刻み/粒子数依存、標本相関を含む不確かさを確認します。

## 公開範囲

解説・代表式・文献を公開しています。専用コードと数値検証結果は実装予定です。上記の検証案は未実施で、他の手法のコードや計算結果をこの手法の検証として流用しません。

## 文献

- G. A. Bird (1963). Approach to Translational Equilibrium in a Rigid Sphere Gas. https://doi.org/10.1063/1.1710976
- G. A. Bird (1994). Molecular Gas Dynamics and the Direct Simulation of Gas Flows. https://global.oup.com/academic/product/molecular-gas-dynamics-and-the-direct-simulation-of-gas-flows-9780198561958
