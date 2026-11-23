# レベルセット法：動く界面とVOFとの比較

レベルセット法：動く界面とVOFとの比較

レベルセット法は、曲線や曲面を関数のゼロ等値面として格子上に表し、その関数を発展させる方法です。移流方程式、Hamilton–Jacobi方程式、界面幾何を結び、合体や分裂を表現しやすい構造を持ちます。本章では基本式から、再現できる小さな2Dの円の運動へ進みます。

界面をφ=0として表す


$$
\Gamma(t)=\{\mathbf{x}:\phi(\mathbf{x},t)=0\},\qquad\phi0\;\text{outside}
$$
本章は内部を負、外部を正とします。関数値そのものは流体の密度や体積率ではありません。同じゼロ集合を持つ単調な変換でも界面は同じですが、勾配と数値誤差は変わります。原著・実装によって内部を正とする規約もあるため、法線と速度の符号をそろえてください。

流れに運ばれる界面


$$
\frac{D\phi}{Dt}=0\quad\Longrightarrow\quad\phi_t+\mathbf{u}\cdot\nabla\phi=0
$$
界面上の粒子が速度uで動き、その軌道上でφが変わらない条件を微分すると移流式が得られます。既知速度による界面の移流と、速度・圧力まで解く二相流の連成は区別します。風上差分・ENO/WENO・時間積分はこの式を離散化する選択肢であり、界面表現そのものとは別です。

法線・曲率と法線方向への運動


$$
\phi_t+V_n\|\nabla\phi\|=0,\qquad\mathbf{n}=\frac{\nabla\phi}{\|\nabla\phi\|},\quad\kappa=\nabla\cdot\mathbf{n}
$$

$$
\phi(\mathbf{x})=\operatorname{sgn}(\phi)\operatorname{dist}(\mathbf{x},\Gamma),\qquad\|\nabla\phi\|=1\quad\text{where differentiable}
$$
内部が負ならnは外向きです。2Dの円ではこの規約のκは1/r。法線方向へVnで進む場合は一般のHamilton–Jacobi型になります。符号付き距離関数は微分可能な場所で|∇φ|=1ですが、中心や最近点が一意でない場所では滑らかさを仮定できません。今回の誤差評価は円の界面近傍で行い、曲率で駆動する運動は解説の範囲に留めます。

再初期化は何を直し、何を動かし得るか


$$
\psi_\tau+S_\epsilon(\phi_0)(\|\nabla\psi\|-1)=0,\quad\psi(\mathbf{x},0)=\phi_0(\mathbf{x}),\quad S_\epsilon(z)=\frac{z}{\sqrt{z^2+\epsilon^2}}
$$
一般の速度場では移流したφが距離関数でなくなり、擬似時間τの補助方程式で距離性を回復することがあります。物理時間tはこの操作では進めません。理想的なゼロ集合の保持と、格子上で補間した界面の保持は同じ保証ではありません。実装例は平滑符号を各呼出しで固定する1次Godunov反復です。Sussman–Fatemiの制約付き高次法とは異なり、位置・面積の改善を仮定しません。

VOFとの比較：幾何と体積収支


$$
F_K=\frac1{|K|}\int_K H(-\phi)\,d\mathbf{x},\quad0\le F_K\le1,\qquad\nabla\cdot\mathbf{u}=0:\quad F_t+\nabla\cdot(F\mathbf{u})=0
$$

$$
F_K^{n+1}=F_K^n-\frac{\Delta t}{|K|}\sum_{f\subset\partial K}|f|\widehat{\mathcal F}_{K,f},\quad\sum_K|K|F_K^{n+1}=\sum_K|K|F_K^n-\text{boundary flux}
$$
定式化・保存・今回の実装範囲の比較比較点レベルセットVOF保持する量符号付き関数φ、界面はφ=0セル内の体積率F界面幾何φの勾配から法線・曲率を計算体積率から界面の再構築・幾何評価が必要保存通常の移流・再初期化だけでは囲まれた体積を保証しない共有面流束の保存的更新で体積収支を構成できる数値上の課題距離関数の劣化、界面位置と体積のずれ有界性、界面再構築、曲率精度を別に確認組合せCLSVOFなどで距離型幾何と保存的体積率を結ぶ結合の具体式と誤差・整合性を別途確認本サイトの今回の範囲円の移流・剛体回転の実行例と22検査比較解説のみ。VOFの数値実験は未実施非圧縮の指定速度では、体積率は保存形で運べます。共有面の流束が対向セルで打ち消し合えば、全体の体積変化は境界流束と整合します。有界性0≤F≤1はさらに流束・再構築・CFL条件を必要とし、保存性だけでは決まりません。φを保存形で更新しても、ゼロ界面が囲む面積の保存は別の問題です。今回の区分線形φから測る面積を、保存的に移流したVOFの体積率と呼びません。

軽量2D例：平行移動と偏心円の剛体回転


$$
\phi_{\rm ref}(\mathbf{x},t)=\|\mathbf{x}-\mathbf{c}(t)\|-r,\quad \mathbf{c}_{\rm tr}(t)=\mathbf{c}_0+t\mathbf{v},\quad\mathbf{c}_{\rm rot}(t)=\mathbf{x}_c+R(\omega t)(\mathbf{c}_0-\mathbf{x}_c)
$$
半径.15、単位正方形、T=1。平行移動は中心(.3,.35)、速度(.2,.1)。回転は中心(.68,.5)の円を(.5,.5)周りに角速度2πで1周させます。32²/64²/128²のENO2片側差分とHeun RK2を使い、Courant数は.35以下。外側ゴースト値は各段階の解析解を指定し、内部は毎回数値更新します。これは指定境界を持つ問題で、周期条件ではありません。

両方で移流単独と、時刻.1ごとに5擬似ステップの再初期化を加えたモードを比較します。0/.25/.5/.75/1で観測し、回転の終了時だけでなく円が途中で実際に移動したことも照合します。

[](/code/validated-examples/2026-11-23/level-set/results/level-set-overview.png)保存した2D場からの最細格子の比較。黒は解析的な最終界面、橙は移流単独、緑破線は再初期化あり、灰点線は初期界面です。何を誤差と呼ぶか


$$
E_\Gamma=\max_{t\in\{.25,.5,.75,1\}}\max_{\mathbf{z}\in Z_h(t)}\big|\|\mathbf{z}-\mathbf{c}(t)\|-r\big|,\quad p_{\rm obs}=\log_2\!\left(E_\Gamma(h)/E_\Gamma(h/2)\right)
$$
Z_hは格子辺の線形補間によるゼロ交差点で、EΓはその点での最大半径誤差です。連続な2界面間のHausdorff距離とは区別します。面積は三角形上の線形φを切り取りπr²と比較し、初期からの幾何学的な偏りも表示します。格子と物理刻みを同時に細分化した移流単独の観測次数は平行移動約1.90、回転約2.02。N64での刻み半減の感度を別に記録し、純粋な空間次数の証明とは呼びません。

最細格子の最大相対面積誤差は平行移動で約0.22%→0.93%、回転で約1.06%→2.02%（移流単独→再初期化あり）。この設定では単純な再初期化で誤差が増える事実を残します。距離勾配の改善、ゼロ界面の精度、体積収支は別々の評価項目です。

適用範囲と次に読む資料

この配布版は与えた速度による円の移流です。合体分裂・曲率流・表面張力・二相流の検証、VOFとの性能比較は行っていません。幾何学的な参照式、全2D最終配列、途中の界面標本、CSV、入力ハッシュ、全判定、各再初期化の面積変化を公開します。既存のZalesak型切り欠き円盤は保存的スカラー輸送の別資料として読むことができ、そのコードをVOF実装と読み替えません。

[Zalesak型の保存的な2D回転輸送](/numerical-methods-atlas/ja/read/validation-zalesak/) · [ENO/WENO](/numerical-methods-atlas/ja/read/benchmarks/)

## 固定入力の実行例と診断対照

受入条件が示す検証範囲と数学的な一般保証を区別します。旧版の入力・測定・公差は保持します。

### レベルセット円の2D平行移動：界面・面積・再初期化

固定標的の計算例

中心(.3,.35)の半径.15の円を速度(.2,.1)でT=1まで平行移動します。32²/64²/128²のENO2＋Heunを用い、再初期化の有無、途中の界面位置、面積誤差と格子・刻みの細分化を比べます。

辺上の半径誤差はHausdorff距離ではなく、ΔxとΔtを同時に細分化した観測次数は純粋な空間次数と区別します。再初期化で面積や位置が改善するとは限らず、本例では最細格子でも誤差が増えます。VOFとの数値的な優劣比較、独立PDEエンジン、界面の合体分裂、曲率流・表面張力・二相Navier–Stokesは検証していません。2モードは同じ円の移流問題の追加条件です。

[入力・結果・受入条件](/numerical-methods-atlas/validation/level-set-translation/?lang=ja) · [手法・一次文献](/numerical-methods-atlas/ja/read/validation-level-set/#level-set-translation) · [コード run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/run.py) · [コード level_set.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/level_set.py) · [コード geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/geometry.py) · [テスト test_level_set.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/test_level_set.py) · [ZIP](/code/validated-examples/2026-11-23/level-set/atlas-level-set-2026-11-23.zip) · [結果](/code/validated-examples/2026-11-23/level-set/results/result.json) · [追試記録](/code/validated-examples/2026-11-23/level-set/verification.json)

### 偏心したレベルセット円の2D剛体回転

固定標的の計算例

中心(.68,.5)の半径.15の円を(.5,.5)周りに角速度2πで1周回転させます。32²/64²/128²のENO2＋Heunを用い、再初期化の有無、途中の界面位置、面積誤差と格子・刻みの細分化を比べます。

辺上の半径誤差はHausdorff距離ではなく、ΔxとΔtを同時に細分化した観測次数は純粋な空間次数と区別します。再初期化で面積や位置が改善するとは限らず、本例では最細格子でも誤差が増えます。VOFとの数値的な優劣比較、独立PDEエンジン、界面の合体分裂、曲率流・表面張力・二相Navier–Stokesは検証していません。2モードは同じ円の移流問題の追加条件です。

[入力・結果・受入条件](/numerical-methods-atlas/validation/level-set-rotation/?lang=ja) · [手法・一次文献](/numerical-methods-atlas/ja/read/validation-level-set/#level-set-rotation) · [コード run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/run.py) · [コード level_set.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/level_set.py) · [コード geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/geometry.py) · [テスト test_level_set.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/test_level_set.py) · [ZIP](/code/validated-examples/2026-11-23/level-set/atlas-level-set-2026-11-23.zip) · [結果](/code/validated-examples/2026-11-23/level-set/results/result.json) · [追試記録](/code/validated-examples/2026-11-23/level-set/verification.json)

## 公開範囲

レベルセット法は2D円の移流・剛体回転に限定した教育用実装、VOFは比較解説のみです。専用配布版の22検査と全固定入力を独立展開から再実行。共通22例と旧配布版・既存問題の成功履歴は保持します。

## 文献

- S. Osher and J. A. Sethian (1988). Fronts propagating with curvature-dependent speed: Algorithms based on Hamilton-Jacobi formulations. https://doi.org/10.1016/0021-9991(88)90002-2
- C. W. Hirt and B. D. Nichols (1981). Volume of fluid (VOF) method for the dynamics of free boundaries. https://doi.org/10.1016/0021-9991(81)90145-5
- M. Sussman and E. Fatemi (1999). An Efficient, Interface-Preserving Level Set Redistancing Algorithm and Its Application to Interfacial Incompressible Fluid Flow. https://doi.org/10.1137/S1064827596298245
- M. Sussman and E. G. Puckett (2000). A Coupled Level Set and Volume-of-Fluid Method for Computing 3D and Axisymmetric Incompressible Two-Phase Flows. https://doi.org/10.1006/jcph.2000.6537
