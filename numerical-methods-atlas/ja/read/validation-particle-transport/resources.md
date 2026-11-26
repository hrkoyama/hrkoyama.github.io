# 粒子・輸送：独立参照・保存則・統計誤差

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-particle-transport/

この章に登録された手法・問題・実行例の関連資料です。

## 手法

- [Ewald法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ewald/?lang=ja>)
- [Particle Mesh Ewald（PME）](<https://hrkoyama.github.io/numerical-methods-atlas/methods/pme/?lang=ja>)
- [Smooth PME（SPME）](<https://hrkoyama.github.io/numerical-methods-atlas/methods/spme/?lang=ja>)
- [高速多重極法の移動演算](<https://hrkoyama.github.io/numerical-methods-atlas/methods/fmm/?lang=ja>)
- [Particle-in-Cell（PIC）](<https://hrkoyama.github.io/numerical-methods-atlas/methods/pic/?lang=ja>)
- [DSMC・運動論輸送](<https://hrkoyama.github.io/numerical-methods-atlas/methods/dsmc/?lang=ja>)
- [輻射輸送・モーメント法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/radiation-transport/?lang=ja>)

## 方程式

- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/ewald-convergence/?lang=ja#ewald-convergence-ja-algorithm>)

  erfcと逆空間和による主計算とは別に、1/rのGaussian積分と1次元theta関数の積を数値積分します。小さい積分変数ではPoisson変換と中性条件、大きい側では自己項を引いた像和を使い、力はthetaの解析微分から積分します。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/spme-convergence/?lang=ja#spme-convergence-ja-algorithm>)

  16³/24³/40³格子と4/6次Bスプライン、3つの平行移動位相を用います。FFT逆空間エネルギーを割当て重みで位置微分し、実空間・自己項はEwald主計算と共有します。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm-convergence/?lang=ja#fmm-convergence-ja-algorithm>)

  P2M/M2M/M2L/L2Lと近接P2Pを保ち、次数2/4/8/12、深さ2/3を比較します。別のCartesian直接和、二点電荷の閉形式、正多角形の中心力と遠方ポテンシャルを参照にします。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/pic-conservation/?lang=ja#pic-conservation-ja-algorithm>)

  CIC割当て・同じ重みの場補間・スペクトルPoisson・速度Verlet。独立な時間積分法DOP853は同じ粒子格子RHSを積分し、参照自身の最大刻み感度を検査します。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-statistics/?lang=ja#dsmc-statistics-ja-algorithm>)

  ランダムな完全対合と球面一様の散乱で、各対の運動量・エネルギーを保持します。別の標本生成ではGaussianを重心ゼロ部分空間へ射影し、半径を固定します。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/radiation-convergence/?lang=ja#radiation-convergence-ja-algorithm>)

  1次風上有限体積の空間更新とGauss–Legendre方向を使い、角度系列は正確な指数伝播で空間誤差を除きます。MCはmu=sqrt(U)と指数光学距離から生存・吸収を独立に判定します。

## 問題の図

- [Ewald：非対称周期セルのエネルギー・力と独立theta積分](<https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/results/ewald-convergence.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/results/ewald-convergence.png
- [SPME：格子・補間次数・格子位相と保存則](<https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/results/spme-convergence.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/results/spme-convergence.png
- [FMM：直接和・解析配置と展開次数・木の深さ](<https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/results/fmm-convergence.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/results/fmm-convergence.png
- [PIC：格子・時間収束、保存量と粒子雑音](<https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/results/pic-conservation.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/results/pic-conservation.png
- [DSMC衝突成分：有限N平衡・保存則・統計誤差](<https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/results/dsmc-statistics.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/results/dsmc-statistics.png
- [輻射輸送：空間・角度収束と光子統計](<https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/results/radiation-convergence.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/results/radiation-convergence.png

## 厳密解・参照解

- [Ewald：非対称周期セルのエネルギー・力と独立theta積分：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/ewald-convergence/?lang=ja#ewald-convergence-ja-validation>)

  参照の求積・theta/像の打切り・切替点をまとめて精密化し、上限32→40の感度を別に記録します。alpha3点、実空間4点・逆空間5点、平行移動・並べ替え、合力、エネルギー差分の3成分を比較。粗い打切りの不正確さを検出する対照も残します。
- [SPME：格子・補間次数・格子位相と保存則：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/spme-convergence/?lang=ja#spme-convergence-ja-validation>)

  独立thetaエネルギー・全力との差と、共有Ewald経路自体の誤差を明記します。分配の総和・導関数総和、電荷、エネルギー差分3成分、位相間の幅、有限格子の合力と粗い格子の対照を保存します。
- [FMM：直接和・解析配置と展開次数・木の深さ：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm-convergence/?lang=ja#fmm-convergence-ja-validation>)

  ポテンシャル・場の最大絶対誤差、実際の遠方移動演算、回転・平行移動誤差、電荷を掛けた力の合計を測ります。粗い展開の失敗対照も確認します。
- [PIC：格子・時間収束、保存量と粒子雑音：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/pic-conservation/?lang=ja#pic-conservation-ja-validation>)

  16/32/64格子とdt=.2/.1/.05を別に精密化し、線形cos(t)と時間参照の誤差を分離します。実数奇微分のNyquist零モードはGauss残差から分けて記録。時刻0の64seed・N=256/1024/4096のCICモード電力を解析期待値と比較します。
- [PIC空間演算の独立実装照合](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-pic-independent-spatial-ja>)
  relation: related-model
  reference_kind: numerical-reference

  有限格子の数値参照 周期[0,2π]、256粒子、格子8/16/32、シード35001/35002、dt=.02、T=.24。位置は一様乱数、v=.2 Normal+.1 sin x。6組は別々に進めた12軌道です。 19 pytestと58/58固定判定が合格。6組＝12の自己無撞着軌道を13時刻全てで照合し、最大差は位置8.88e−16・速度3.33e−16・電場8.33e−16・電荷2.89e−15。pytest+mainは0.392秒。最初の小pytestは周期端点の添字不具合で17/18となり、元記録を保持して修正後に全計算を実行しました。 離散演算の独立したコーディング照合です。時間積分法や連続方程式を変えた独立エンジン、連続極限の収束、冷たいプラズマの振動参照の再現を意味しません。既存cold-plasma-picの関連補助検証として扱い、温かい初期速度の軌道を冷たい解と同一視しません。 周期[0,2π]、256粒子、格子8/16/32、シード35001/35002、dt=.02、T=.24。位置は一様乱数、v=.2 Normal+.1 sin x。6組は別々に進めた12軌道です。
- [DSMC衝突成分：有限N平衡・保存則・統計誤差：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-statistics/?lang=ja#dsmc-statistics-ja-validation>)

  全roundの運動量・エネルギーの最大保存誤差は決定論的な許容値で検査します。最初の6roundの異方性、4点のエネルギーCDF、4次モーメントと有限NのBeta参照との差は、独立seed間の標準誤差で測ります。NによるCDF標準誤差の減少と、有限NからMaxwellへの偏りを分けます。
- [輻射輸送：空間・角度収束と光子統計：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/radiation-convergence/?lang=ja#radiation-convergence-ja-validation>)

  16〜256セル・4〜64方向を別に収束させ、QUADPACK積分とE3を照合。64seed・1024/4096/16384光子で平均誤差、RMSE、二項標準偏差と95% Clopper–Pearson区間の実測被覆を記録します。全光子の出射＋吸収、正値性と離散フラックス収支を確認します。

## コード・検証

- [Ewald：非対称周期セルのエネルギー・力と独立theta積分](<https://hrkoyama.github.io/numerical-methods-atlas/validation/ewald-convergence/?lang=ja>)
  availability: run

  中性8電荷の全エネルギーと24力成分を、別実装のGaussian/theta積分と比較。分割・実空間・逆空間の打切り、保存則と不変性を分けて測定します。
- [SPME：格子・補間次数・格子位相と保存則](<https://hrkoyama.github.io/numerical-methods-atlas/validation/spme-convergence/?lang=ja>)
  availability: run

  BスプラインSPMEを同じ独立theta参照へ照合し、格子・次数・位相への依存、電荷の保持、エネルギー勾配と合力を測ります。
- [FMM：直接和・解析配置と展開次数・木の深さ](<https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm-convergence/?lang=ja>)
  availability: run

  96粒子の2次元対数核を別の全対直接和と照合し、展開次数・木の深さ、回転・平行移動、合力の近似誤差を測ります。
- [PIC：格子・時間収束、保存量と粒子雑音](<https://hrkoyama.github.io/numerical-methods-atlas/validation/pic-conservation/?lang=ja>)
  availability: run

  冷たい1次元周期プラズマのquiet-start収束と、独立seedでの初期粒子雑音を分け、電荷・運動量・Gauss則・エネルギー誤差を保存します。
- [DSMC衝突成分：有限N平衡・保存則・統計誤差](<https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-statistics/?lang=ja>)
  availability: run

  有限粒子数の平衡をMaxwell極限と区別し、独立な球面標本、解析的異方性減衰、seed間誤差と比較します。
- [輻射輸送：空間・角度収束と光子統計](<https://hrkoyama.github.io/numerical-methods-atlas/validation/radiation-convergence/?lang=ja>)
  availability: run

  純吸収平板で特性解・独立適応求積・光子生存率を比較し、離散収支と標本誤差・区間被覆を別々に測ります。
