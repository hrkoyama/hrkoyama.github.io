# MCMC・温度制御・生物モデル

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-models/

この章に登録された手法・問題・実行例の関連資料です。

## 手法

- [Markov連鎖Monte Carlo](<https://hrkoyama.github.io/numerical-methods-atlas/methods/mcmc/?lang=ja>)

  この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。
- [Langevinサーモスタット](<https://hrkoyama.github.io/numerical-methods-atlas/methods/langevin-thermostat/?lang=ja>)

  この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。
- [確率的速度リスケーリング（CSVR）](<https://hrkoyama.github.io/numerical-methods-atlas/methods/stochastic-velocity-rescaling/?lang=ja>)

  この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。
- [確率微分方程式](<https://hrkoyama.github.io/numerical-methods-atlas/methods/sde/?lang=ja>)

  この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。
- [空間中心差分](<https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=ja>)

  この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。
- [古典的RK4](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=ja>)

  この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。
- [空間中心差分](<https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=ja>)

  この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。
- [古典的RK4](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=ja>)

  この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。
- [陰的中点則](<https://hrkoyama.github.io/numerical-methods-atlas/methods/implicit-midpoint/?lang=ja>)

  この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。
- [Lie–Trotter分割](<https://hrkoyama.github.io/numerical-methods-atlas/methods/lie-trotter/?lang=ja>)

  この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。
- [Strang分割](<https://hrkoyama.github.io/numerical-methods-atlas/methods/strang-splitting/?lang=ja>)

  この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。
- [古典的RK4](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=ja>)

  この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。
- [Markov連鎖Monte Carlo](<https://hrkoyama.github.io/numerical-methods-atlas/methods/mcmc/?lang=ja>)
- [Langevinサーモスタット](<https://hrkoyama.github.io/numerical-methods-atlas/methods/langevin-thermostat/?lang=ja>)
- [空間中心差分](<https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=ja>)
- [古典的RK4](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=ja>)

## 方程式

- [Hamilton系・振動子](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#hamiltonian-ja>)

  正準方程式と分離可能なHamiltonianの代表形。調和・4次ポテンシャルの振動子で、エネルギー誤差とシンプレクティック性を比べます。 Hamilton系へのリンクは調和ポテンシャルの力学部分です。計算には摩擦・雑音またはCSVRの温度浴が追加されます。
- [スカラーItô拡散：GBMとOU](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#scalar-ito-diffusion-ja>)

  決定論的初期値のスカラーSDE。平均・二次モーメントの弱誤差、共有Brown運動での強誤差、有限標本のMCSEを分けます。OUは調和Langevin系の浴成分に関連する追加検査です。 Hamilton系へのリンクは調和ポテンシャルの力学部分です。計算には摩擦・雑音またはCSVRの温度浴が追加されます。
- [熱・拡散方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#heat-ja>)

  一定拡散係数νの代表形。モードの減衰、時間積分、境界条件へ。 線形反応拡散u_t=D u_xx+r u（公開入力はD=0.1、r=0.1）です。熱方程式へのリンクは拡散部分で、反応項を含む固有値r-Dk²で比較します。
- [Schnakenberg反応拡散](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-schnakenberg-ja>)

  自己触媒反応の空間拡張。反応平衡と分散関係から模様の発生を検証するための数理モデルです。 限定した実行例：a=0.1,b=0.9、拡散係数0.01/1、長さ2πの1次元周期Schnakenberg系。旧線形発現例を保持し、固定した反射対称の有限振幅初期値の非線形発展と成長後パターンを独立Fourier–Galerkin/Radau参照および空間・時間細分化で比較します。この旧1次元例だけから一般の模様選択、生物実験への較正、流体連成へ広げません。 全モデル族の実装ではありません。今回の固定例：Schnakenberg：2D境界と初期モード この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。
- [Turing反応拡散の枠組み](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-turing-ja>)

  2成分反応拡散の枠組み。f・gは個別に指定する必要があり、模様の画像だけでTuring機構とは判定できません。 限定した実行例：a=0.1,b=0.9、拡散係数0.01/1、長さ2πの1次元周期Schnakenberg系。旧線形発現例を保持し、固定した反射対称の有限振幅初期値の非線形発展と成長後パターンを独立Fourier–Galerkin/Radau参照および空間・時間細分化で比較します。一般の模様選択、2次元、生物実験への較正、流体連成には広げません。 この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。
- [FitzHugh–Nagumoの興奮と回復](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-fitzhugh-nagumo-ja>)

  高速の興奮と低速の回復を結ぶ規格化した代表形。係数・符号・空間拡張には複数の規約があります。 限定した実行例：公開実行例はD=0の空間なしの縮約ODEです。FHN/BVP型の縮約ODEの限定検証です。HH全イオンチャネル、空間軸索、患者データ、実測電気生理の再現を含みません。 公開固定入力は空間拡散を含まない2変数ODEの極限です。一般の伝播PDEを検証したという意味ではありません。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/gaussian-mcmc/?lang=ja#gaussian-mcmc-ja-algorithm>)

  log受理比でMetropolis更新。FFTによる連鎖内自己共分散を平均し、Geyerのgamma0+gamma1から始まる初期正ペア和から平均観測量のESSを求めます。古典的split-Rhatも併記します。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/langevin-harmonic/?lang=ja#langevin-harmonic-ja-algorithm>)

  力B・ドリフトAの半ステップと厳密OUノイズ更新OをB-A-O-A-Bで合成。サンプルの共分散・3種のCDF・エネルギー平均/分散・位置相関を記録します。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-fourier/?lang=ja#reaction-diffusion-fourier-ja-algorithm>)

  周期中心2階差分と独自RK4で進めます。空間系列は小さな同一時間刻み、時間系列は同じ空間演算子を用います。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/turing-schnakenberg/?lang=ja#turing-schnakenberg-ja-algorithm>)

  独自の中心差分・RK4で線形化PDEと短い非線形PDEを進めます。3格子でのモード振幅と成長率、非線形の濃度最小値・初期パターン増幅を記録します。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/fitzhugh-nagumo/?lang=ja#fitzhugh-nagumo-ja-algorithm>)

  独自RK4を刻み0.1/0.05/0.025で使用し、パルスの不連続点で時間区間を厳密に分割します。出力刻み0.1でピークと休止状態からの距離も測定します。

## 問題の図

- [Gaussian標的のMCMC：分布・自己相関・ESS](<https://hrkoyama.github.io/numerical-methods-atlas/problems/gaussian-mcmc/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/gaussian-mcmc.png
- [Langevin温度制御：正準分布・刻み偏り・時間相関](<https://hrkoyama.github.io/numerical-methods-atlas/problems/langevin-harmonic/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/langevin-harmonic.png
- [反応拡散：空間2次と時間4次を分けて測る](<https://hrkoyama.github.io/numerical-methods-atlas/problems/reaction-diffusion-fourier/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/reaction-diffusion-fourier.png
- [Turing不安定性：線形成長率と小振幅パターン](<https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/turing-schnakenberg.png
- [FitzHugh–Nagumo：パルス興奮・回復と独立ODE参照](<https://hrkoyama.github.io/numerical-methods-atlas/problems/fitzhugh-nagumo/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/fitzhugh-nagumo.png
- [Gaussian標的のMCMC：分布・自己相関・ESS](<https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/gaussian-mcmc.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/gaussian-mcmc.png
- [Langevin温度制御：正準分布・刻み偏り・時間相関](<https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/langevin-harmonic.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/langevin-harmonic.png
- [反応拡散：空間2次と時間4次を分けて測る](<https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/reaction-diffusion-fourier.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/reaction-diffusion-fourier.png
- [Turing不安定性：線形成長率と小振幅パターン](<https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/turing-schnakenberg.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/turing-schnakenberg.png
- [FitzHugh–Nagumo：パルス興奮・回復と独立ODE参照](<https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/fitzhugh-nagumo.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/fitzhugh-nagumo.png

## 厳密解・参照解

- [Gaussian標的のMCMC：分布・自己相関・ESS：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/gaussian-mcmc/?lang=ja#references-ja>)

  既知のGaussian標的分布・モーメントを基準に、標本分布・自己相関・ESSを確認します。18件の参照解一覧にMCMC軌道の厳密解カードはありません。
- [Langevin温度制御：正準分布・刻み偏り・時間相関：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/langevin-harmonic/?lang=ja#references-ja>)

  調和ポテンシャルの正準分布・モーメントと相関の解析基準を使い、刻み幅バイアスを確認します。摩擦・雑音を持たない調和軌道とは区別します。
- [OUのweakモーメントと同時Brownian結合](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-ou-weak-moments-ja>)
  relation: related-model
  reference_kind: analytic

  解析解 dX=1.5(.2-X)dt+.8dW,X0=.7。無次元T=1、8/16/32/64刻み、独立32seed×1024経路。状態軸に境界・clipなし。 dX=1.5(.2-X)dt+.8dW,X0=.7。無次元T=1、8/16/32/64刻み、独立32seed×1024経路。状態軸に境界・clipなし。
- [反応拡散：空間2次と時間4次を分けて測る：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/reaction-diffusion-fourier/?lang=ja#references-ja>)

  線形反応拡散の連続Fourier解と半離散Fourier解を分け、空間2次・時間4次の収束を確認します。純拡散カードの指数率をそのまま使いません。
- [Turing不安定性：線形成長率と小振幅パターン：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=ja#references-ja>)

  小振幅では行列指数の線形成長率を使い、非線形追補では独立Radau参照と正値性・収束を確認します。線形近似を非線形飽和パターンの厳密解と呼びません。
- [FitzHugh–Nagumo：パルス興奮・回復と独立ODE参照：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/fitzhugh-nagumo/?lang=ja#references-ja>)

  電流パルスを与えた2変数縮約ODEを独立DOP853参照と比較し、全出力時刻の誤差・時間収束・回復を確認します。
- [Gaussian標的のMCMC：分布・自己相関・ESS：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/gaussian-mcmc/?lang=ja#gaussian-mcmc-ja-validation>)

  正規CDFを独立参照とし、標本数1024/2048/8192の連鎖平均RMSEを比較。別の定常AR(1)系列と厳密tau=(1+rho)/(1-rho)で診断量を照合します。公差は固定入力で事前指定します。
- [Langevin温度制御：正準分布・刻み偏り・時間相関：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/langevin-harmonic/?lang=ja#langevin-harmonic-ja-validation>)

  SciPy離散Lyapunov解および調和系の明示共分散diag(T/omega²,T(1-h²omega²/4))で照合。運動量の刻み2次偏りと有限標本誤差を分離し、burn過渡を写像で評価。連続相関は別の行列指数で算出します。
- [OUのweakモーメントと同時Brownian結合](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-ou-weak-moments-ja>)
  relation: related-model
  reference_kind: analytic

  解析解 dX=1.5(.2-X)dt+.8dW,X0=.7。無次元T=1、8/16/32/64刻み、独立32seed×1024経路。状態軸に境界・clipなし。 dX=1.5(.2-X)dt+.8dW,X0=.7。無次元T=1、8/16/32/64刻み、独立32seed×1024経路。状態軸に境界・clipなし。
- [反応拡散：空間2次と時間4次を分けて測る：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-fourier/?lang=ja#reaction-diffusion-fourier-ja-validation>)

  連続固有値r-Dk²への最大誤差で空間次数、半離散固有値r-4Dsin²(kdx/2)/dx²への最大誤差で時間次数を測ります。独立した解析参照であり同じ実装の細格子値を参照にしません。
- [Turing不安定性：線形成長率と小振幅パターン：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/turing-schnakenberg/?lang=ja#turing-schnakenberg-ja-validation>)

  連続Fourier行列J-k²DのSciPy expmと線形数値解を比較し空間収束を測定。非線形計算は半離散線形行列指数との小振幅差を測り、成熟模様の参照照合とは区別します。
- [FitzHugh–Nagumo：パルス興奮・回復と独立ODE参照：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/fitzhugh-nagumo/?lang=ja#fitzhugh-nagumo-ja-validation>)

  別実装SciPy DOP853のrtol1e-11と1e-13を比較して参照の感度を確認し、厳しい参照への最大解誤差と時間次数を評価します。ピーク時刻は出力格子上の精度です。

## コード・検証

- [Gaussian標的のMCMC：分布・自己相関・ESS](<https://hrkoyama.github.io/numerical-methods-atlas/validation/gaussian-mcmc/?lang=ja>)
  availability: run

  32本のMetropolis連鎖を既知の標準正規分布へ照合し、平均・分散・CDF、自己相関時間、ESSと標本予算依存を記録します。
- [Langevin温度制御：正準分布・刻み偏り・時間相関](<https://hrkoyama.github.io/numerical-methods-atlas/validation/langevin-harmonic/?lang=ja>)
  availability: run

  調和振動子のBAOABを、正準分布と離散Lyapunov定常分布、連続・離散の時間相関へ照合します。
- [CSVRとLangevin：調和2自由度の分布・揺らぎ・相関](<https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-harmonic/?lang=ja>)
  availability: run

  異なる周波数を持つ2自由度でglobal CSVRとlocal Langevinを同じOBABO分割で比較。位置・運動量・温度・全エネルギーの分布、揺らぎ、相関を記録します。
- [OUのweakモーメントと同時Brownian結合](<https://hrkoyama.github.io/numerical-methods-atlas/validation/ou-weak-moments/?lang=ja>)
  availability: run

  連続真値、離散EM期待値、同一経路差とMCSEを分離する固定入力です。
- [反応拡散：空間2次と時間4次を分けて測る](<https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-fourier/?lang=ja>)
  availability: run

  線形の拡散・反応演算子を、連続と半離散のFourier厳密解を用いて小規模に検証します。
- [Turing不安定性：線形成長率と小振幅パターン](<https://hrkoyama.github.io/numerical-methods-atlas/validation/turing-schnakenberg/?lang=ja>)
  availability: run

  Schnakenberg型反応拡散で、一様平衡の安定性と拡散による選択モードの成長を行列指数で検証します。
- [Schnakenberg有限振幅過渡：非線形性と独立参照](<https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-nonlinear/?lang=ja>)
  availability: run

  t=8までの有限振幅反応拡散を、独立なFourier–Galerkin参照・格子と時間刻み収束・新しい高調波で検証します。
- [Schnakenberg飽和パターン：近定常性と格子・時間収束](<https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-pattern/?lang=ja>)
  availability: run

  t=100の1D選択パターンを独立参照で照合。参照の90→100の変化・全PDE残差と、有限刻みprimaryのFD残差を分けて測ります。
- [同じ非線形反応拡散でLie–TrotterとStrangを比較する](<https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-splitting/?lang=ja>)
  availability: run

  32格子・終了時刻1のSchnakenberg反応拡散を、同じ入力・部分ソルバーでLie–TrotterとStrangにより進めます。4段階の時間刻みで1次／2次の収束、参照の感度、反応収支と未収束時の失敗を確かめる軽量な比較例です。
- [FitzHugh–Nagumo：パルス興奮・回復と独立ODE参照](<https://hrkoyama.github.io/numerical-methods-atlas/validation/fitzhugh-nagumo/?lang=ja>)
  availability: run

  2変数の膜興奮縮約ODEを電流パルスで励起し、DOP853との全出力時刻の誤差・時間収束・回復を確認します。
