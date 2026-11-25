# DFTから原子間力へ：有限差分・独立参照・力の収束とBOMDへの接続

多原子の周期Heセルで、全エネルギーの位置微分から原子間力を求めます。解析勾配、エネルギーの有限差分、独立した平面波計算を比較し、基底・k点・補助格子・SCFが力に与える影響を分けて確かめます。BOMDへ渡す力の条件と、軌道の検証で追加すべき条件もつなぎます。

固定セル・局所He GTH・スピン非分極LDAの教育用検証です。PySCFの解析核勾配を利用する実行・検証ドライバーであり、自作の電子状態エンジンではありません。この配置の力の一致は、他元素・非局所擬ポテンシャル・応力・長時間BOMDや温度制御の検証を意味しません。

## 全エネルギーの負の勾配を力にする

固定した格子、電子数、汎関数、擬ポテンシャルのもとで、各原子配置における電子基底状態を求めます。Born–Oppenheimerエネルギーは電子項と周期イオン間項を含むセル全体のエネルギーです。原子IのCartesian成分αに働く力は、その座標についての全微分に負号を付けた値です。勾配と力の符号を区別し、座標をbohr、エネルギーをhartreeで扱うと力の単位はhartree/bohrになります。

入力は一辺5 bohrの立方セルで、Heの位置は(0.37, 0.61, 0.83)と(2.13, 2.27, 2.41) bohrです。価電子4・閉殻の固定配置で、対称性だけですべての力がゼロになる検査を避けます。力の大きさだけでなく、各原子のx・y・z成分と方向を照合します。この人工配置の数値的一致を、実在するヘリウム結晶の平衡構造や化学精度の予測と読み替えません。セルを変形する応力・圧力の微分は、固定セルでの原子位置微分とは別の検証です。

$$
E_{\mathrm{BO}}(\mathbf R;A)=\min_{\langle\psi_i|\psi_j\rangle=\delta_{ij}}E_{\mathrm{KS}}[\{\psi_i\};\mathbf R,A]
$$

$$
F_{I\alpha}=-\left.\frac{d E_{\mathrm{BO}}}{dR_{I\alpha}}\right|_{A,N_e},\qquad [F_{I\alpha}]=E_h/a_0
$$

## Hellmann–Feynmanの定理と、移動する基底のPulay項

規格化された厳密な固有状態では、エネルギーのパラメータ微分をHamiltonianの微分の期待値として表せます。これがHellmann–Feynmanの関係です。Feynmanの1939年論文は分子の力を直接評価する歴史的な一次文献です。この定理だけで、有限の原子中心基底で求めた電子状態のすべての力が正しく得られるわけではありません。下のHとΨは定理の一般形を表し、Kohn–Shamの全エネルギーを軌道固有値の和だけに置き換える式ではありません。

原子に追随するGaussian基底では、核を動かすと基底関数と重なり行列も変わります。変分計算で軌道係数を十分に最適化していても、この基底の位置依存に由来する項を含めて、離散化したエネルギーを微分する必要があります。これらをPulay項と呼びます。一般化固有値問題に現れるエネルギー重み付き密度と重なり微分の項はその一部です。今回のドライバーはPySCFの解析核勾配を利用し、単純な裸のイオン–電子Coulomb力へ置き換えません。

固定セルと固定カットオフで用いる平面波は原子位置に追随する基底ではありません。それでも有限カットオフによる力の誤差は残り、SCFや密度格子も収束させる必要があります。「Pulay項が不要」という理由だけで平面波の力が厳密になるわけではありません。セル変形に伴う基底変化とPulay応力の議論も、この固定セル検査の対象から分けます。

$$
H(\lambda)\Psi=E(\lambda)\Psi,\quad\langle\Psi|\Psi\rangle=1\quad\Longrightarrow\quad\frac{dE}{d\lambda}=\left\langle\Psi\left|\frac{\partial H}{\partial\lambda}\right|\Psi\right\rangle
$$

$$
F_{\mathbf k}C_{\mathbf k}=S_{\mathbf k}C_{\mathbf k}\varepsilon_{\mathbf k},\quad W_{\mathbf k}=C_{\mathbf k}f_{\mathbf k}\varepsilon_{\mathbf k}C_{\mathbf k}^{\dagger},\quad \left.\frac{dE}{dR_{I\alpha}}\right|_{\text{overlap term}}=-\sum_qw_q\operatorname{Tr}\!\left(W_{\mathbf k_q}\frac{\partial S_{\mathbf k_q}}{\partial R_{I\alpha}}\right)
$$

## 有限差分照合：変位幅を小さくするだけでは足りない

基準配置から1つの原子の1成分だけを±h動かし、それぞれの配置でSCFを独立に収束させた全エネルギーを用いて中心差分の力を求めます。格子、k点と重み、基底名、FFT格子、汎関数、擬ポテンシャル、電子数をそろえます。原子中心基底も移動させるため、差分は基底の位置依存を含む同じ離散化エネルギーの微分を検査します。

滑らかなエネルギー面では中心差分の切断誤差はO(h²)です。一方で、エネルギーにSCFの解き残しや丸め誤差があれば、その差を2hで割るため小さすぎる変位で誤差が増えることがあります。複数のhを記録し、解析力との差が安定する範囲を確認します。実測の系列が必ずきれいなU字を描くとは仮定しません。入力したSCFのエネルギー公差そのものを、各エネルギーの厳密な誤差上界とは扱いません。

解析力と同一エンジンの有限差分の一致は、符号・成分・基底微分を含む内部整合性の検査です。両者が共通の汎関数や擬ポテンシャルの実装を使うため、これだけを独立した物理参照との一致とは呼びません。今回の独立照合には別実装の平面波DFTKも用います。

$$
F^{\mathrm{FD}}_{I\alpha}(h)=-\frac{E(\mathbf R+h\mathbf e_{I\alpha})-E(\mathbf R-h\mathbf e_{I\alpha})}{2h}
$$

$$
F^{\mathrm{FD}}(h)-F=\mathcal O(h^2)+\mathcal O(\delta E/h)
$$

## 力について基底・k点・補助格子・SCFを別々に収束させる

エネルギー差が小さくなったという理由だけで、力も十分に収束したと判断しません。Gaussian軌道基底、Brillouinゾーンのk点メッシュ、FFTの補助格子、SCF停止条件を1つずつ変え、同じ原子・成分の力の差を測ります。基準と比べるときは原子の順序とCartesian軸を固定します。今回の要約は全成分の絶対値最大を用いるL∞型のノルムで、原子ごとのベクトル長や成分平均とは区別します。

基底名のzeta数を増やす系列は、必ずしも入れ子の空間や単調な力の変化を与えません。k点メッシュもすべてが入れ子ではありません。最後の2設定の力の差を公開した目安と比較しますが、それを完全基底や無限k点での厳密な誤差上界とは呼びません。密度や局所ポテンシャルを載せる補助FFT格子は、Gaussianの軌道空間と独立の収束軸です。

SCFの未収束は力にも現れます。終了フラグと反復回数だけでなく、電子数、軌道・SCF残差など、保存した状態の診断量を併せて読みます。厳しい停止条件に対して力が変わらないことを直接測り、未収束の電子状態をBOMDへ正常な力として返さないようにします。

各走査は1つの制御値だけを変え、その他の制御値は公開入力で指定した有限の設定に固定します。Γ点と2³では基底系列もそれぞれ確認しますが、4³・最大Gaussian基底・最細FFTを同時に組み合わせた完全な収束計算は行っていません。独立参照との一致もΓ点と2³の指定ケースに限られます。

$$
\|\Delta\mathbf F\|_{\infty}=\max_{I,\alpha\in\{x,y,z\}}|F^{(a)}_{I\alpha}-F^{(b)}_{I\alpha}|
$$

$$
\Delta_{\mathrm{basis}}\mathbf F,\quad\Delta_{\mathbf k}\mathbf F,\quad\Delta_{\mathrm{FFT}}\mathbf F,\quad\mathbf F_{\tau}-\mathbf F_{\mathrm{tight}}
$$

## 独立参照：同じモデルを異なる離散化で比較する

PySCF側は周期Gaussian基底とFFTDFを用い、参照側はDFTKの平面波Hamiltonian、SCF、周期イオン間計算と解析力を用います。両側で格子と全原子位置、価電子数、非偏極・整数占有、局所GTHの全係数、LibxcのLDA_XとLDA_C_VWN（VWN5）、分率k点と重みを一致させます。エネルギーの原点を後から合わせる定数や、力を合わせる補正は加えません。

DFTK側でも平面波の打切りを上げ、力の末尾の差を確かめます。比較は同じ有限行列の丸め誤差を測るものではありません。有限のGaussian空間と平面波空間の差を含むため、公開した受入幅と両側の収束診断を併せて評価します。両エンジンがLibxcを共有することも独立性の限界として明示します。

DFTKのcompute_forcesは分率座標に対応する表現を返し、Cartesian力を得るAPIはcompute_forces_cartです。座標と力の変換は同じではありません。今回の照合はCartesian成分・hartree/bohrで統一します。参照の生成スクリプト、Juliaの固定環境、擬ポテンシャル、入力と結果のハッシュを保存し、通常のPython実行による保存参照との比較と、Juliaで参照そのものを再生成する操作を区別します。

$$
\mathbf R=A\boldsymbol\xi,\qquad \mathbf F_{\mathrm{cart}}=-A^{-\mathsf T}\nabla_{\boldsymbol\xi}E
$$

## 成分・並進・非零の力を確認する

力がすべてほぼゼロの配置では、符号が逆でも検査が通ってしまうことがあります。非零の力を持つ多原子配置を用い、成分ごとの解析力、有限差分力、独立参照を比較します。成分の並べ替え、原子番号の取り違え、単位の誤りを、力のノルム1つだけで検査しないようにします。

外場がない理想的な周期系では、全原子の一様並進に対して全エネルギーが不変で、全力の和はゼロです。有限の実空間格子などはこの性質を数値的に破ることがあり、残った全力を記録すると格子や微分の診断になります。並進に関する検査だけでは相対配置に働く力の精度は保証できないため、エネルギー差分と独立参照を併用します。

$$
E(\{\mathbf R_I+\mathbf t\})=E(\{\mathbf R_I\})\quad\Longrightarrow\quad\sum_I\mathbf F_I=\mathbf 0
$$

## BOMDへ渡すものと、軌道で追加検証するもの

BOMDの力供給部energy_and_forcesは、原子位置（positions_bohr）を受け取り、同じエネルギー面の全エネルギー（energy_per_cell）と力（forces_cartesian）、SCFの収束状態・残差を返します。電子状態が未収束なら計算を失敗として扱います。質量は核運動の時間積分で使い、DFTから求めるポテンシャルエネルギーや力へ掛けません。周期セル内での位置の折り返しは表示と連続した軌道の記録を区別します。

速度Verletなら、力で速度を半刻み進め、位置を更新し、新しい配置で電子状態を再び解いて力を得た後、残り半刻みの速度更新を行います。電子の初期推定を前のステップから引き継ぐことは高速化ですが、SCF収束の要件を置き換えるものではありません。今回の検証は原子間力とBOMDへ渡す接続を中心にし、単発の力評価や短い接続試験を長時間のMD検証として数えません。

実用的な軌道の受入には、時間刻みを細分化した比較、SCF公差を厳しくした比較、温度制御を使わないNVEでの全エネルギーと運動量、必要なら時間反転の検査を追加します。温度制御でエネルギーのずれを吸収させると力や積分器の誤差が見えにくくなるため、まず無温度制御で検査します。短時間のドリフトが小さいことを、長時間の安定性や正しい統計分布の保証とはしません。

Car–Parrinello法は仮想電子自由度を核と同時に進める別の定式化です。ここで用意するBorn–Oppenheimer面の力供給をCPMDの実装として扱いません。DFTから力、核の時間積分、温度制御のどこまでが実行済みかは、分野間をつなぐ入口でも段階ごとに示します。

手法台帳には別の2準位BO/CP型教育模型の実行例があります。本章のHe₂の力・局所Verlet接続とは別の固定入力で、一般のKohn–Sham軌道計算・実材料・長時間MDの検証としてまとめて数えません。

$$
\mathbf v_{n+1/2}=\mathbf v_n+\frac{\Delta t}{2M}\mathbf F(\mathbf R_n),\quad\mathbf R_{n+1}=\mathbf R_n+\Delta t\,\mathbf v_{n+1/2},\quad\mathbf v_{n+1}=\mathbf v_{n+1/2}+\frac{\Delta t}{2M}\mathbf F(\mathbf R_{n+1})
$$

$$
\mathcal E_n=E_{\mathrm{BO}}(\mathbf R_n)+\sum_I\frac{M_I}{2}|\mathbf v_{I,n}|^2,\qquad \Delta\mathcal E_n=\mathcal E_n-\mathcal E_0
$$

2準位模型のBO/CP型連成と短い核熱浴: https://hrkoyama.github.io/numerical-methods-atlas/validation/two-state-bo-cp-ou/?lang=ja

https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/source-manifest.json

## 保存した実測値

- max_reference_force_error: 7.53824989575e-05
- max_reference_energy_error: 0.000171684168107
- finite_difference_max_error: 2.32234127207e-08
- finite_difference_scan_max_error: 1.8023756336e-07
- max_tight_scf_commutator: 3.04623403924e-09
- max_scf_commutator: 2.94441763031e-06
- max_electron_count_error: 2.6645352591e-15
- max_orthogonality_error: 4.93782792432e-11
- max_energy_reconstruction_error: 0
- min_sampled_ks_gap: 0.559054051286
- max_overlap_condition: 413148.516377
- finest_net_force: 3.18720265458e-09
- bomd_position_step_difference: 9.60193803634e-07
- bomd_full_step_energy_defect: 3.78557850844e-07
- bomd_two_half_steps_energy_defect: 9.46016402992e-08
- reference_cutoff_force_change: 1.69522172031e-06
- reference_finite_difference_max_error: 2.43217217838e-07
- kpoint_last_change: 2.84334958952e-05
- basis_last_change: 2.65239291374e-06
- basis-k2_last_change: 3.55179947748e-05
- auxiliary_last_change: 1.30328608255e-06
- scf_last_change: 5.64949656501e-10

https://hrkoyama.github.io/code/periodic-forces/2026-11-22/results/result.json

## 実行

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/periodic-he-forces/?lang=ja

## 文献

- S. Goedecker, M. Teter and J. Hutter (1996). Separable dual-space Gaussian pseudopotentials. https://journals.aps.org/prb/abstract/10.1103/PhysRevB.54.1703 — 出版社の書誌・抄録を確認。実際のHe係数は同梱データと両ライブラリで照合し、原論文の表からの全桁の直接転記とは扱いません。
- S. H. Vosko, L. Wilk and M. Nusair (1980). Accurate spin-dependent electron liquid correlation energies for local spin density calculations: a critical analysis. https://doi.org/10.1139/p80-159 — 公式Libxc資料のLDA_C_VWN（VWN5）の原著DOIと書誌を確認。出版社本文へはアクセスできず、全文や表の監査は行っていません。
- Qiming Sun et al. (2020). Recent developments in the PySCF program package. https://doi.org/10.1063/5.0006074 — 出版社の書誌・抄録と既存アトラスの登録を確認。今回使用する周期APIは下記の公式資料と固定版コードでも確認します。
- M. F. Herbst, A. Levitt and E. Cancès (2021). DFTK: A Julian approach for simulating electrons in solids. https://proceedings.juliacon.org/papers/10.21105/jcon.00069 — 出版社の書誌と公開論文の導入部を確認。今回の参照計算は独立した数値検査であり、論文中の全例の再現ではありません。
- DFTK developers (2026). DFTK API and pseudopotentials. https://docs.dftk.org/stable/api/ — compute_forcesとcompute_forces_cartの座標・単位・離散化エネルギー微分の説明を参照。実際の参照生成は配布物のDFTK固定版で実行し、その版のソースも確認します。
- M. Born and R. Oppenheimer (1927). Zur Quantentheorie der Molekeln. https://onlinelibrary.wiley.com/doi/10.1002/andp.19273892002 — 出版社の書誌・DOIを確認。Born–Oppenheimer分離の歴史的基礎として引用し、原文全文の監査や現代のMD実装の再現は主張しません。
- R. Car and M. Parrinello (1985). Unified Approach for Molecular Dynamics and Density-Functional Theory. https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.55.2471 — 出版社の書誌・抄録と公開原文の式(3)–(5)、BO面近傍の仮想電子運動の議論を参照。論文のSi動力学の数値再現は行っていません。
- R. P. Feynman (1939). Forces in Molecules. https://journals.aps.org/pr/abstract/10.1103/PhysRev.56.340 — 出版社の書誌と抄録を確認。Hellmann–Feynmanの力の関係の歴史的な一次文献として引用し、有限基底や擬ポテンシャルの勾配実装をこの原著だけで検証したとは主張しません。
- P. Pulay (1969). Ab initio calculation of force constants and equilibrium geometries in polyatomic molecules. I. Theory. https://www.tandfonline.com/doi/abs/10.1080/00268976900100941 — 検索ツールが返した出版社ページの書誌と抄録を確認。通常のページ取得は403でした。原子位置に依存する有限基底でのエネルギー微分を論じる力の原著として引用し、SCF加速DIISのPulay(1980)とは区別します。原著全文の監査は行っていません。
- PySCF developers (2026). pyscf.pbc.grad.krks: analytic nuclear gradients with k-point sampling. https://pyscf.org/_modules/pyscf/pbc/grad/krks.html — 周期KRKSの解析核勾配、LDAの交換相関微分、対応していない設定を公式ソースで確認。配布版のPySCF 2.11.0でも使用箇所を照合します。
- PySCF developers (2026). pyscf.pbc.grad.krhf: electronic, overlap, pseudopotential and nuclear gradient terms. https://pyscf.org/_modules/pyscf/pbc/grad/krhf.html — grad_elecの密度・エネルギー重み付き密度と重なり微分、擬ポテンシャルの微分、周期イオン項の該当箇所を確認。第三者ソースコードを教材へ複製しません。
- PySCF developers (2026). Guidelines for PBC DFT Parameter Settings. https://pyscf.org/user/pbc/dft-settings.html — FFTDFの補助平面波と実空間格子、核勾配への適用範囲の説明を参照。Gaussian軌道基底とFFT格子の収束を分けるための実装資料です。
- J. M. Herbert and M. Head-Gordon (2005). Accelerated, energy-conserving Born–Oppenheimer molecular dynamics via Fock matrix extrapolation. https://pubs.rsc.org/en/content/articlelanding/2005/cp/b509494a — 検索ツールが返した出版社ページの書誌と抄録を確認。通常のページ取得は403でした。SCFの解き残し・初期推定と力・NVEドリフトを区別する根拠として参照し、論文の外挿法や分子軌道を今回実装・再現したとは主張しません。
