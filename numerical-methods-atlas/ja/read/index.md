# 分野別に解説を読む

理論・導出・計算例を、分野ごとにまとめた読み物です。基礎から関連する手法と検証例へ進めます。

## 基礎・誤差・時間積分

誤差と安定性から入り、時間積分と拘束を持つ方程式の扱いをたどります。

- [差分、CFL条件、von Neumann解析、Laxの定理](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/stability/)
- [A安定性、L安定性、誤差ノルム](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/accuracy-stability/)
- [時間積分とleapfrog法](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/time-integration/)
- [Runge–Kutta法：段数、次数、安定性、SSP](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/runge-kutta/)
- [硬い方程式の積分：段階を解き、時間誤差を制御する](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/stiff-integration/)
- [作用素分割：Lie–Trotter と Strang の比較](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/operator-splitting/)
- [シンプレクティック積分：正準写像とエネルギーを分ける](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/symplectic/)
- [微分代数方程式（DAE）](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/dae/)

## 楕円型問題・線形代数・近似

境界値問題と疎行列の解法から、固有値・基底・補間・数値積分へ進みます。

- [拡散、楕円型方程式、境界条件、反復法](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/elliptic/)
- [西川の双曲型拡散法：1階系を反復する](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/hyperbolic-diffusion/)
- [疎行列・非線形方程式系：真の残差を測る](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/sparse-nonlinear/)
- [代数的マルチグリッド（AMG）](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/amg/)
- [QR・SVD・最小二乗](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/qr-svd/)
- [Krylov固有値解法](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/eigensolvers/)
- [直交多項式と格子上の基底関数](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/basis-functions/)
- [スプライン補間](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/splines/)
- [Gauss求積・適応積分](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/quadrature/)
- [Chebyshev近似](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/chebyshev/)
- [ウェーブレット](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/wavelets/)
- [AMG・行列分解・固有値・求積](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-foundations/)
- [基盤手法：条件数・残差・収束と独立参照](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-foundations-conditioning/)

## 自動微分・最適化・逆問題

残差と解の微分を区別し、目的関数・観測・正則化へつなぎます。

- [自動微分：数値ソルバーのための微分計算](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/automatic-differentiation/)
- [陰関数微分と随伴法：Bratuのパラメータ感度](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/adjoint/)
- [勾配法・準Newton法](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/optimization/)
- [Bratu逆問題：合成観測からλを随伴勾配で推定する](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/bratu-inverse/)
- [Bratu逆問題の複数パラメータ化：正則化と識別可能性](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/bratu-multi-inverse/)
- [PINN・ニューラル演算子](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/pinn-operators/)

## 流体・衝撃波・定常解法

保存則の再構成、勾配制限、衝撃波の頑健性、低Mach数と定常反復の条件を読みます。

- [Euler再構成：PPM・特性変数・WENO-Z・AUSM](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/reconstruction/)
- [勾配制限：minmod、Superbee、MC、van Leer、van Albada](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/limiters/)
- [発展的な勾配制限：TVBと正値性保存](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/advanced-limiters/)
- [回転ハイブリッド・リーマンソルバー](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/rotated-hybrid/)
- [波追跡PPM、AUSM系と曲面前方の衝撃波](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/shock-expansion/)
- [カーバンクル現象](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/carbuncle/)
- [二重Mach反射](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/double-mach/)
- [KEEP法：滑らかな流れの釣合いと限界を検証する](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/keep/)
- [前処理、二重時間積分、残差分配法](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/advanced/)
- [前処理行列・低Mach数・音速点とエントロピー修正](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/low-mach-preconditioning/)
- [定常解のためのダンピングRunge–Kutta反復](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/steady-runge-kutta/)
- [NASAの2次元検証・妥当性確認問題集](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/nasa-2d/)

## 格子・有限要素・連成方程式

空間離散化と座標を整理し、非圧縮流・MHD・相対論系の条件へ進みます。

- [構造格子、非構造格子、三角形格子](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/meshes/)
- [連続有限要素法：弱形式から疎行列の組立てへ](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/fem/)
- [任意Lagrange–Euler法](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/ale/)
- [極・円筒座標：テンソルと粘性](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/coordinates-viscosity/)
- [球面メッシュとArakawa A・B・C格子](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/geophysical-grids/)
- [CIP：値と勾配を運ぶ](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/cip/)
- [非圧縮流：整合する離散演算子で射影する](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/incompressible/)
- [MHD：制約輸送法と発散クリーニング](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/mhd/)
- [相対論的流体力学：SRHD、GRHD、GRMHD](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/relativistic-hydrodynamics/)
- [流体・MHDの独立照合とCT／GLM](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-mhd/)
- [CTとGLM：同条件の独立照合・格子・時間収束](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-mhd-convergence/)

## 粒子・運動論・輸送

粒子法、分布関数、長距離力と輸送方程式を読みます。

- [粒子法と平滑化粒子流体力学](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/particles-sph/)
- [Godunov平滑化粒子流体力学（GSPH）](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/gsph/)
- [格子Boltzmann法：衝突、並進、流体運動の回復](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/lattice-boltzmann/)
- [Chapman–Enskog展開：分布から輸送へ](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/chapman-enskog/)
- [DSMC・運動論輸送](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/dsmc/)
- [粒子重力：PM、P³M、ツリー、多重極、マルチグリッド](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/particle-gravity/)
- [重力核：孤立FFTと周期スラブ](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/gravity-boundaries/)
- [放射輸送・モーメント法](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/radiation-transport/)
- [粒子・静電場・運動論・放射輸送](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-particles/)

## 電磁場・静電場・電子状態

周期静電場・電磁場と、原子・分子・周期電子状態の近似をたどります。

- [Ewald法](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/ewald/)
- [Particle Mesh Ewald（PME）](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/pme/)
- [Smooth PME（SPME）](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/spme/)
- [スラブ静電場と2次元周期Ewald](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/slab-ewald/)
- [Yee FDTD：基礎と検証例](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/fdtd/)
- [Particle-in-Cell（PIC）](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/pic/)
- [量子化学・DFT：何を近似し、何を解くか](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/quantum-chemistry/)
- [水素型原子とHe：実行・検証例](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/quantum-atoms/)
- [H₂分子の閉殻HF：独立参照・SCF残差・基底の収束](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/h2-hf/)
- [周期DFT：Γ点・k点積分・基底・SCFと独立参照](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/periodic-dft/)
- [DFTから原子間力へ：有限差分・独立参照・力の収束とBOMDへの接続](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/periodic-forces/)

## 確率計算・生物・温度制御

確率誤差、集団モデル、温度制御を、それぞれの検証量とともに比べます。

- [Monte Carlo積分](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/monte-carlo/)
- [Markov連鎖Monte Carlo](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/mcmc/)
- [多峰性MCMC：混合不良と収束診断の独立検証](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-mcmc/)
- [確率微分方程式](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/sde/)
- [生物モデル方程式と数値検証](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/biological-models/)
- [非線形反応拡散・パターン形成の独立検証](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-biology/)
- [サーモスタット：温度制御と分布の比較](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/thermostats/)
- [MCMC・温度制御・生物モデル](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-models/)
- [CSVRとLangevin：分布・揺らぎ・相関](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-thermostats/)

## 検証問題・実験ガイド

計算対象と参照解を選び、展示・保存結果・実行例の役割を確認します。

- [方程式ギャラリー：計算法の前に方程式を選ぶ](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/equation-gallery/)
- [テスト計算ライブラリ](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/benchmarks/)
- [厳密解・参照解ライブラリ](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/reference-solutions/)
- [インタラクティブ実験ガイド](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/experiments/)
- [時間依存テスト：動画と保存状態](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/movies/)

## 歴史・文献・整備記録

数値計算法の系譜と出典、教科書、収録範囲・整備記録を確認します。

- [数値計算法の歴史アトラス](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/history/)
- [原著の出版年順に並べた参考文献](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/references/)
- [教科書案内：次に何を調べるか](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/textbooks/)
- [Philip L. Roeを偲んで](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/roe-memorial/)
- [収録範囲と数え方](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/site-coverage/)
- [実装ロードマップ](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/roadmap/)
- [v0.1.0 初版](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/release-notes-v0.1.0/)

