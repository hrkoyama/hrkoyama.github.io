# 確率微分方程式

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/sde/

この章に登録された手法・問題・実行例の関連資料です。

## 手法

- [確率微分方程式](<https://hrkoyama.github.io/numerical-methods-atlas/methods/sde/?lang=ja>)
- [確率微分方程式](<https://hrkoyama.github.io/numerical-methods-atlas/methods/sde/?lang=ja>)

  この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。

## 方程式

- [スカラーItô拡散：GBMとOU](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#scalar-ito-diffusion-ja>)

  決定論的初期値のスカラーSDE。平均・二次モーメントの弱誤差、共有Brown運動での強誤差、有限標本のMCSEを分けます。OUは調和Langevin系の浴成分に関連する追加検査です。 幾何Brown運動のItô SDE dX=μXdt+σXdW。既存46式にはSDEの専用項目がありません。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#execution-gbm-sde-ja>)

  スカラー幾何Brown運動のEuler–Maruyama。粗細刻みと解析解で同じBrown運動を共有し、4096経路で強RMS誤差を測定。一般SDE・MCMC・弱収束次数は検証しない。

## 問題の図

- [Itô SDE：共有Brown運動による強収束](<https://hrkoyama.github.io/numerical-methods-atlas/problems/gbm-sde/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/results/gbm-sde/preview.png

## 厳密解・参照解

- [Itô SDE：共有Brown運動による強収束：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/gbm-sde/?lang=ja#references-ja>)

  幾何Brown運動の解析的なItô解を同じBrown増分で結び、強収束とモーメントを確認します。決定論ODEの厳密解とは区別します。
- [GBMのweak誤差とMonte Carlo標準誤差](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-gbm-weak-moments-ja>)
  relation: related-model
  reference_kind: analytic

  解析解 dX=.5Xdt+.4XdW,X0=1。無次元T=1、8/16/32/64刻み、独立32seed×1024経路。状態軸に境界・clipなし。 dX=.5Xdt+.4XdW,X0=1。無次元T=1、8/16/32/64刻み、独立32seed×1024経路。状態軸に境界・clipなし。
- [同じBrownian経路のMilstein・EM strong比較](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-gbm-milstein-strong-ja>)
  relation: related-model
  reference_kind: analytic

  解析解 既存GBMと同じμ=.15,σ=.4,X0=T=1。4seed×8192経路、16/32/64/128刻み。 既存GBMと同じμ=.15,σ=.4,X0=T=1。4seed×8192経路、16/32/64/128刻み。
- [Itô SDE：共有Brown運動による強収束：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/gbm-sde/?lang=ja#gbm-sde-ja-validation>)

  スカラー幾何Brown運動のEuler–Maruyama。粗細刻みと解析解で同じBrown運動を共有し、4096経路で強RMS誤差を測定。一般SDE・MCMC・弱収束次数は検証しない。
- [GBMのweak誤差とMonte Carlo標準誤差](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-gbm-weak-moments-ja>)
  relation: related-model
  reference_kind: analytic

  解析解 dX=.5Xdt+.4XdW,X0=1。無次元T=1、8/16/32/64刻み、独立32seed×1024経路。状態軸に境界・clipなし。 dX=.5Xdt+.4XdW,X0=1。無次元T=1、8/16/32/64刻み、独立32seed×1024経路。状態軸に境界・clipなし。
- [同じBrownian経路のMilstein・EM strong比較](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-gbm-milstein-strong-ja>)
  relation: related-model
  reference_kind: analytic

  解析解 既存GBMと同じμ=.15,σ=.4,X0=T=1。4seed×8192経路、16/32/64/128刻み。 既存GBMと同じμ=.15,σ=.4,X0=T=1。4seed×8192経路、16/32/64/128刻み。

## コード・検証

- [Itô SDE：共有Brown運動による強収束](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/gbm-sde/?lang=ja>)
  availability: run

  スカラー幾何Brown運動のEuler–Maruyama。粗細刻みと解析解で同じBrown運動を共有し、4096経路で強RMS誤差を測定。一般SDE・MCMC・弱収束次数は検証しない。
- [GBMのweak誤差とMonte Carlo標準誤差](<https://hrkoyama.github.io/numerical-methods-atlas/validation/gbm-weak-moments/?lang=ja>)
  availability: run

  連続真値、離散EM期待値、同一経路差とMCSEを分離する固定入力です。
- [同じBrownian経路のMilstein・EM strong比較](<https://hrkoyama.github.io/numerical-methods-atlas/validation/gbm-milstein-strong/?lang=ja>)
  availability: run

  補償項を持つMilsteinとEMの終端L2 RMSを、厳密端点と有限モーメントから検査。
- [OUのweakモーメントと同時Brownian結合](<https://hrkoyama.github.io/numerical-methods-atlas/validation/ou-weak-moments/?lang=ja>)
  availability: run

  連続真値、離散EM期待値、同一経路差とMCSEを分離する固定入力です。
- [確率微分方程式：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/sde/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [Itô SDE：共有Brown運動による強収束：コード・検証状況](<https://hrkoyama.github.io/numerical-methods-atlas/problems/gbm-sde/?lang=ja#code-ja>)
  availability: source

  対応する公開検査と配布版の条件を確認できます。
