# SDEの弱誤差・強誤差と標本誤差

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-stochastic-accuracy/

この章に登録された手法・問題・実行例の関連資料です。 解析モーメントと共有Brown運動を使い、SDEの弱誤差・強誤差と有限標本の不確かさを分けます。

## 手法

- [確率微分方程式](<https://hrkoyama.github.io/numerical-methods-atlas/methods/sde/?lang=ja>)

## 方程式

- [スカラーItô拡散：GBMとOU](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#scalar-ito-diffusion-ja>)

  決定論的初期値のスカラーSDE。平均・二次モーメントの弱誤差、共有Brown運動での強誤差、有限標本のMCSEを分けます。OUは調和Langevin系の浴成分に関連する追加検査です。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/gbm-weak-moments/?lang=ja#gbm-weak-moments-ja-algorithm>)

  fine Gaussian増分を固定block和で集約し、厳密端点1配列を全刻みで共有。OUの厳密積分はdWとの共分散を保つ独立bridge正規変数から構成。異なる加算順の和のbit一致は主張しません。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/ou-weak-moments/?lang=ja#ou-weak-moments-ja-algorithm>)

  fine Gaussian増分を固定block和で集約し、厳密端点1配列を全刻みで共有。OUの厳密積分はdWとの共分散を保つ独立bridge正規変数から構成。異なる加算順の和のbit一致は主張しません。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/gbm-milstein-strong/?lang=ja#gbm-milstein-strong-ja-algorithm>)

  Milsteinは.5σ²X(dW²-h)を追加。全法・刻みでfine driverと厳密端点1配列を共有。負状態を修復しません。

## 問題の図

- [GBMのweak誤差とMonte Carlo標準誤差](<https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/results/gbm-weak-moments.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/results/gbm-weak-moments.png
- [OUのweakモーメントと同時Brownian結合](<https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/results/ou-weak-moments.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/results/ou-weak-moments.png
- [同じBrownian経路のMilstein・EM strong比較](<https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/results/gbm-milstein-strong.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/results/gbm-milstein-strong.png
- [Itô SDE：共有Brown運動による強収束](<https://hrkoyama.github.io/numerical-methods-atlas/problems/gbm-sde/?lang=ja>)

  解析モーメントと共有Brown運動を使い、SDEの弱誤差・強誤差と有限標本の不確かさを分けます。 テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/results/gbm-sde/preview.png
- [Langevin温度制御：正準分布・刻み偏り・時間相関](<https://hrkoyama.github.io/numerical-methods-atlas/problems/langevin-harmonic/?lang=ja>)

  解析モーメントと共有Brown運動を使い、SDEの弱誤差・強誤差と有限標本の不確かさを分けます。 テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/langevin-harmonic.png

## 厳密解・参照解

- [GBMのweak誤差とMonte Carlo標準誤差](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-gbm-weak-moments-ja>)
  reference_kind: analytic

  解析解 dX=.5Xdt+.4XdW,X0=1。無次元T=1、8/16/32/64刻み、独立32seed×1024経路。状態軸に境界・clipなし。
- [OUのweakモーメントと同時Brownian結合](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-ou-weak-moments-ja>)
  reference_kind: analytic

  解析解 dX=1.5(.2-X)dt+.8dW,X0=.7。無次元T=1、8/16/32/64刻み、独立32seed×1024経路。状態軸に境界・clipなし。
- [同じBrownian経路のMilstein・EM strong比較](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-gbm-milstein-strong-ja>)
  reference_kind: analytic

  解析解 既存GBMと同じμ=.15,σ=.4,X0=T=1。4seed×8192経路、16/32/64/128刻み。
- [GBMのweak誤差とMonte Carlo標準誤差：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/gbm-weak-moments/?lang=ja#gbm-weak-moments-ja-validation>)

  軌道前にDecimal80/120・独立GH/OU共分散積分とpaired分散による標本解像を資格。各モーメントの5MCSE校正、MCSE精度、固定3段weak率、最後2段の3SE解像を判定。区間の被覆は離散真値に対する有限32反復の記述値。
- [GBMのweak誤差とMonte Carlo標準誤差](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-gbm-weak-moments-ja>)
  relation: related-model
  reference_kind: analytic

  解析解 dX=.5Xdt+.4XdW,X0=1。無次元T=1、8/16/32/64刻み、独立32seed×1024経路。状態軸に境界・clipなし。 dX=.5Xdt+.4XdW,X0=1。無次元T=1、8/16/32/64刻み、独立32seed×1024経路。状態軸に境界・clipなし。
- [同じBrownian経路のMilstein・EM strong比較](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-gbm-milstein-strong-ja>)
  relation: related-model
  reference_kind: analytic

  解析解 既存GBMと同じμ=.15,σ=.4,X0=T=1。4seed×8192経路、16/32/64/128刻み。 既存GBMと同じμ=.15,σ=.4,X0=T=1。4seed×8192経路、16/32/64/128刻み。
- [OUのweakモーメントと同時Brownian結合：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/ou-weak-moments/?lang=ja#ou-weak-moments-ja-validation>)

  軌道前にDecimal80/120・独立GH/OU共分散積分とpaired分散による標本解像を資格。各モーメントの5MCSE校正、MCSE精度、固定3段weak率、最後2段の3SE解像を判定。区間の被覆は離散真値に対する有限32反復の記述値。
- [OUのweakモーメントと同時Brownian結合](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-ou-weak-moments-ja>)
  relation: related-model
  reference_kind: analytic

  解析解 dX=1.5(.2-X)dt+.8dW,X0=.7。無次元T=1、8/16/32/64刻み、独立32seed×1024経路。状態軸に境界・clipなし。 dX=1.5(.2-X)dt+.8dW,X0=.7。無次元T=1、8/16/32/64刻み、独立32seed×1024経路。状態軸に境界・clipなし。
- [同じBrownian経路のMilstein・EM strong比較：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/gbm-milstein-strong/?lang=ja#gbm-milstein-strong-ja-validation>)

  相殺を含む解析MSEをDecimal80/120と独立1step GHで資格。二乗誤差の5SE校正、固定3段RMS率、最細段の優位性を判定。相関を保つ64pathblock jackknifeで率の不確実性を記述。
- [GBMのweak誤差とMonte Carlo標準誤差](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-gbm-weak-moments-ja>)
  relation: related-model
  reference_kind: analytic

  解析解 dX=.5Xdt+.4XdW,X0=1。無次元T=1、8/16/32/64刻み、独立32seed×1024経路。状態軸に境界・clipなし。 dX=.5Xdt+.4XdW,X0=1。無次元T=1、8/16/32/64刻み、独立32seed×1024経路。状態軸に境界・clipなし。
- [同じBrownian経路のMilstein・EM strong比較](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-gbm-milstein-strong-ja>)
  relation: related-model
  reference_kind: analytic

  解析解 既存GBMと同じμ=.15,σ=.4,X0=T=1。4seed×8192経路、16/32/64/128刻み。 既存GBMと同じμ=.15,σ=.4,X0=T=1。4seed×8192経路、16/32/64/128刻み。
- [Itô SDE：共有Brown運動による強収束：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/gbm-sde/?lang=ja#references-ja>)

  解析モーメントと共有Brown運動を使い、SDEの弱誤差・強誤差と有限標本の不確かさを分けます。 幾何Brown運動の解析的なItô解を同じBrown増分で結び、強収束とモーメントを確認します。決定論ODEの厳密解とは区別します。
- [GBMのweak誤差とMonte Carlo標準誤差](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-gbm-weak-moments-ja>)
  relation: related-model
  reference_kind: analytic

  解析モーメントと共有Brown運動を使い、SDEの弱誤差・強誤差と有限標本の不確かさを分けます。 解析解 dX=.5Xdt+.4XdW,X0=1。無次元T=1、8/16/32/64刻み、独立32seed×1024経路。状態軸に境界・clipなし。 dX=.5Xdt+.4XdW,X0=1。無次元T=1、8/16/32/64刻み、独立32seed×1024経路。状態軸に境界・clipなし。
- [同じBrownian経路のMilstein・EM strong比較](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-gbm-milstein-strong-ja>)
  relation: related-model
  reference_kind: analytic

  解析モーメントと共有Brown運動を使い、SDEの弱誤差・強誤差と有限標本の不確かさを分けます。 解析解 既存GBMと同じμ=.15,σ=.4,X0=T=1。4seed×8192経路、16/32/64/128刻み。 既存GBMと同じμ=.15,σ=.4,X0=T=1。4seed×8192経路、16/32/64/128刻み。
- [Langevin温度制御：正準分布・刻み偏り・時間相関：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/langevin-harmonic/?lang=ja#references-ja>)

  解析モーメントと共有Brown運動を使い、SDEの弱誤差・強誤差と有限標本の不確かさを分けます。 調和ポテンシャルの正準分布・モーメントと相関の解析基準を使い、刻み幅バイアスを確認します。摩擦・雑音を持たない調和軌道とは区別します。
- [OUのweakモーメントと同時Brownian結合](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-ou-weak-moments-ja>)
  relation: related-model
  reference_kind: analytic

  解析モーメントと共有Brown運動を使い、SDEの弱誤差・強誤差と有限標本の不確かさを分けます。 解析解 dX=1.5(.2-X)dt+.8dW,X0=.7。無次元T=1、8/16/32/64刻み、独立32seed×1024経路。状態軸に境界・clipなし。 dX=1.5(.2-X)dt+.8dW,X0=.7。無次元T=1、8/16/32/64刻み、独立32seed×1024経路。状態軸に境界・clipなし。

## コード・検証

- [GBMのweak誤差とMonte Carlo標準誤差](<https://hrkoyama.github.io/numerical-methods-atlas/validation/gbm-weak-moments/?lang=ja>)
  availability: run

  連続真値、離散EM期待値、同一経路差とMCSEを分離する固定入力です。
- [OUのweakモーメントと同時Brownian結合](<https://hrkoyama.github.io/numerical-methods-atlas/validation/ou-weak-moments/?lang=ja>)
  availability: run

  連続真値、離散EM期待値、同一経路差とMCSEを分離する固定入力です。
- [同じBrownian経路のMilstein・EM strong比較](<https://hrkoyama.github.io/numerical-methods-atlas/validation/gbm-milstein-strong/?lang=ja>)
  availability: run

  補償項を持つMilsteinとEMの終端L2 RMSを、厳密端点と有限モーメントから検査。
- [Itô SDE：共有Brown運動による強収束：コード・検証状況](<https://hrkoyama.github.io/numerical-methods-atlas/problems/gbm-sde/?lang=ja#code-ja>)
  availability: source

  解析モーメントと共有Brown運動を使い、SDEの弱誤差・強誤差と有限標本の不確かさを分けます。 対応する公開検査と配布版の条件を確認できます。
