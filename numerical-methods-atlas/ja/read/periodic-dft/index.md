# 周期DFT：Γ点・k点積分・基底・SCFと独立参照

Heを1個含む小さな周期セルを例に、Blochの定理からk点積分、周期Gaussian基底、補助FFT格子、SCF反復までをつなぎます。PySCFを用いる実行例と独立した平面波DFTKの参照を比較し、同じモデルを異なる離散化で解くときに必要な整合条件を確かめます。

固定した単純立方Heセルの非相対論・スピン非分極LDAを扱う教育用の周期境界問題です。実装はPySCFを利用するドライバーであり、DFTエンジンを一から自作したものではありません。結晶構造の最適化や実在の固体Heの平衡状態の予測は行いません。

## 固定する物理モデルと、調べる数値誤差

入力は一辺4 bohrの単純立方セルと原点のHe原子1個です。GTH–PADEの局所擬ポテンシャルにより価電子数を2とし、閉殻・スピン非分極のKohn–Sham問題を解きます。このHeポテンシャルには非局所射影子がありません。そのため一般の多元素結晶や非局所擬ポテンシャルの検証をこの1例で代表させません。幾何は収束実験のために固定した教材用の配置です。

交換相関汎関数はLibxcのLDA_XとLDA_C_VWN（VWN5）を明示的に指定します。「LDA」という略称だけでは、VWN、Perdew–Wangなどの相関の選択がそろいません。GTH–PADEは採用した擬ポテンシャルの名称であり、その生成時の近似と今回指定するVWN5が同一であるという意味ではありません。比較する両エンジンには同じ擬ポテンシャルの係数と同じ交換相関を渡します。

原子単位系を用い、格子長はbohr、エネルギーはhartreeで保存します。全エネルギーは単位胞あたりで、電子項と周期イオン間相互作用を含む値を比較します。SCFの解き残し、k点積分、軌道基底、密度・ポテンシャルの補助格子を別々に変えます。これらを小さくしても、LDAや擬ポテンシャルなどの物理近似の誤差を評価したことにはなりません。

$$
\left[-\tfrac12\nabla^2+V_{\mathrm{loc}}+V_H[n]+V_{\mathrm{xc}}[n]\right]\psi_{n\mathbf k}=\varepsilon_{n\mathbf k}\psi_{n\mathbf k}
$$

## Blochの定理と、k点の単位

周期ポテンシャルでは、軌道を平面波因子と格子周期関数の積として表せます。周期関数uと一般のBloch軌道ψを区別します。uは単位胞の端で周期的ですが、ψはk点に応じた位相を伴う境界条件を満たします。Γ点はk=0で、この位相が1となる特別な点です。

ここでは実格子ベクトルを列にもつ行列Aと逆格子ベクトルを列にもつBを用い、AᵀB=2πIと定義します。分率座標κから物理的な波数へはk=Bκで変換します。κは無次元、格子をbohrで定義したkはbohr⁻¹です。PySCFのセル行列は格子ベクトルを行に置き、SCFへ渡すk点は物理的な波数です。DFTKの格子行列の列規約と取り違えないように、入力の格子と分率k点を共通の正本にします。

$$
\psi_{n\mathbf k}(\mathbf r)=e^{i\mathbf k\cdot\mathbf r}u_{n\mathbf k}(\mathbf r),\qquad u_{n\mathbf k}(\mathbf r+\mathbf R)=u_{n\mathbf k}(\mathbf r),\qquad\psi_{n\mathbf k}(\mathbf r+\mathbf R)=e^{i\mathbf k\cdot\mathbf R}\psi_{n\mathbf k}(\mathbf r)
$$

$$
A=(\mathbf a_1,\mathbf a_2,\mathbf a_3),\qquad B=2\pi A^{-\mathsf T},\qquad\mathbf k=B\boldsymbol\kappa,\qquad\Omega=|\det A|
$$

## Γ点とk点メッシュ：積分とバンド経路を分ける

無限結晶の密度やエネルギーにはBrillouinゾーンの積分が現れます。有限のk点と重みでこの積分を近似します。この例では全点と等しい重みを明示したΓを含む一様メッシュを用い、重みの和を1にします。偶数分割でもΓを含む規約であり、ソフトウェアの既定値や、偶数分割で半格子だけずれるMonkhorst–Packの規約と無条件に同一視しません。整数逆格子ベクトルだけ異なる分率k点は同じ点を表します。

Γ点だけの計算はBrillouinゾーン積分の1点近似です。大きな実空間セルや局在した軌道で十分になる場合もありますが、この小さなセルで十分かは実測する必要があります。Γのみと複数のメッシュを同じ基底・補助格子・SCF条件で比較します。異なるメッシュは必ずしも入れ子でなく、エネルギー差の単調な減少は仮定しません。

高対称点を結ぶバンド経路は分散関係の可視化に使う点列です。通常、その点列を等しい重みで平均してもBrillouinゾーン積分にはなりません。本例の目的は全エネルギーと密度の積分を確かめることであり、バンド経路の描画をk点収束の代用にしません。

$$
\frac{1}{|\mathrm{BZ}|}\int_{\mathrm{BZ}}f(\mathbf k)\,d\mathbf k\simeq\sum_{q=1}^{N_k}w_qf(\mathbf k_q),\qquad\sum_qw_q=1,\qquad n(\mathbf r)=2\sum_qw_q\sum_{n\in\mathrm{occ}}|\psi_{n\mathbf k_q}(\mathbf r)|^2
$$

$$
\boldsymbol\kappa_{\mathbf j}=\left(\frac{j_1}{N_1},\frac{j_2}{N_2},\frac{j_3}{N_3}\right)\bmod\mathbb Z^3,\quad j_i=0,\ldots,N_i-1,\quad w_{\mathbf j}=\frac{1}{N_1N_2N_3}
$$

## 軌道基底と補助FFT格子は別の収束軸

PySCF側の軌道は、Gaussian基底の格子和にBlochの位相を付けて展開します。gth-dzvなどの基底名、実際の関数数、重なり行列の条件数を結果に残します。名称のzeta数を増やす操作は完全基底極限の証明ではなく、異なる縮約・偏極関数を含む基底がすべて数学的に入れ子になるとも限りません。基底差は公開した有限系列に対する感度として読みます。

FFT density fitting（FFTDF）は、密度やCoulombポテンシャルなどを扱う補助的な平面波・FFT表現です。FFTメッシュを細かくしてもGaussianの軌道空間は広がりません。逆に軌道基底だけを増やしても、粗い補助格子による誤差は消えません。PySCFの補助格子、DFTKの軌道平面波カットオフ、それに付随する密度格子を混同せず、単位もhartreeとrydbergを区別します。

周期Coulomb相互作用のG=0成分は、電子、局所擬ポテンシャル、周期イオン項を合わせた規約で扱います。平均ポテンシャルの変更は軌道固有値の原点も変えます。同じ計算物理モデルでも、G=0定数や擬ポテンシャル補正、Ewald項、単位胞あたりと原子あたりの違いをそろえなければ全エネルギーを直接比較できません。差を合わせるために結果へ経験的な定数を後付けするのではなく、採用した規約とエネルギー成分を確認します。

$$
\chi_{\mu\mathbf k}(\mathbf r)=\sum_{\mathbf R}e^{i\mathbf k\cdot\mathbf R}\chi_\mu(\mathbf r-\mathbf R),\qquad\psi_{n\mathbf k}=\sum_\mu C_{\mu n}(\mathbf k)\chi_{\mu\mathbf k}
$$

$$
\Delta_kE,\qquad\Delta_{\mathrm{orbital\ basis}}E,\qquad\Delta_{\mathrm{auxiliary\ grid}}E,\qquad E_{\tau}-E_{\mathrm{tight}},\qquad E_{\mathrm{PySCF}}-E_{\mathrm{DFTK}}
$$

## SCF残差、電子数と、標本点上のKSギャップ

Kohn–Sham方程式の有効ポテンシャルは密度に依存するため、固有値問題と密度更新を反復します。エネルギー変化だけでなく、最終密度から再構築した行列による交換子残差、軌道固有方程式の残差、直交性と電子数を検査します。交換子は対称直交化X=S⁻¹ᐟ²を用いたX(FPS−SPF)XのFrobeniusノルムを各k点で求め、その最大値です。軌道残差も同じ最終密度のFを用います。結果には反復履歴、停止理由、許容誤差を残します。反復回数の上限への到達を収束と表示しません。

同じ離散化でSCF許容誤差だけを変え、厳しい設定のエネルギーとの違いを測ります。これは非線形方程式の解き残しの検査です。SCFが収束したことと、基底・補助格子・k点が十分であること、また物理モデルが正確であることは別の判定です。

閉殻の占有と非占有を分け、計算した全k点の占有準位の最大値と非占有準位の最小値から標本点上のKSギャップを求めます。正の値は、このメッシュ上で占有が分離していることを示します。Brillouinゾーン全域の真の最小ギャップを保証するものでも、電子の追加・除去で定義する多体の基本ギャップや実験の光学ギャップでもありません。非占有状態の基底依存性にも注意が必要です。本例ではGaussianと平面波の標本点ギャップに目に見える差が残ります。独立比較で検証する量は全エネルギーであり、ギャップの収束・一致を達成したとは扱いません。

$$
F_{\mathbf k}C_{\mathbf k}=S_{\mathbf k}C_{\mathbf k}\varepsilon_{\mathbf k},\qquad C_{\mathbf k}^{\dagger}S_{\mathbf k}C_{\mathbf k}=I,\qquad\sum_qw_q\operatorname{Tr}(P_{\mathbf k_q}S_{\mathbf k_q})=N_e=2
$$

$$
E_{g,\mathcal K}^{\mathrm{KS}}=\min_{\mathbf k\in\mathcal K,n\in\mathrm{unocc}}\varepsilon_{n\mathbf k}-\max_{\mathbf k\in\mathcal K,n\in\mathrm{occ}}\varepsilon_{n\mathbf k}
$$

## 異なる基底を使う独立DFTK参照と比較する

実行例はPySCFの周期積分・FFTDF・SCFを利用します。参照は独立したJuliaのDFTKで平面波Kohn–Sham問題を解き、教材のPySCFソルバーを呼び出しません。PySCF内で補助表現だけを変更した計算を独立実装の比較と数えません。交換相関の評価には両者でLibxcを使うため、その部分まで完全に独立した検証という意味ではありません。

同一の格子、原子位置、価電子数、スピン、擬ポテンシャル係数、LDA_X＋LDA_C_VWN、分率k点と重みを照合します。DFTK側では平面波カットオフとSCFの収束も確認します。Gaussianと平面波は異なる有限空間なので、有限基底同士の全エネルギーに機械精度の一致を要求しません。公開入力の判定幅の中で、Gaussian基底・補助格子の感度と参照のカットオフ依存性を併記して一致を評価します。判定幅を満たすことは、真の誤差の厳密な上限や化学精度を証明するものではありません。

保存済み参照を使った通常の追試と、Julia環境を用いる参照の再生成を別の工程にします。入力、参照、ソースのハッシュと依存関係の版を固定し、ZIPを別フォルダへ展開した実行も検査します。結果JSONの合否だけでなく、差の実数値、判定条件、収束系列を確かめられる形で配布します。

## 第一原理MD：Born–Oppenheimer法とカー–パリネロ法

周期DFTの次に原子核を動かすのが第一原理分子動力学（AIMD）です。Born–Oppenheimer分子動力学（BOMD）は、各核配置で電子状態を基底状態へ十分に収束させ、そのエネルギー面の力で核の古典運動を積分します。下のE_BOはイオン間項を含む全エネルギーです。1927年のBorn–Oppenheimer論文は電子と核の分離の基礎として引用するもので、現代のBOMDプログラムを発表した論文という意味ではありません。

BOMDではSCFの許容誤差をエネルギーだけでなく力と軌道の再現性でも決めます。原子に追随する有限Gaussian基底を使う場合は、基底の位置依存に由来する力の項（Pulay項）も必要です。力の有限差分照合、時間刻みの細分化、無温度制御のNVEでのエネルギードリフトを別々に検査します。予測した電子状態を次の初期値に使っても、各配置で必要な精度まで最適化するというBOMDの要件は変わりません。

カー–パリネロ分子動力学（CPMD）は、核の座標と電子軌道を拡張ラグランジアンで同時に進めます。μは電子軌道に与える数値的な仮想質量で、実在の電子の質量そのものではありません。直交制約はLagrange乗数Λで課します。表示式は固定セル・固定占有を想定し、軌道の速度項をμ/2と定義する規約です。周期k点を使う一般化では電子項に重みと占有を一貫して含めます。

CPMDで電子軌道を時間発展させることは、TDDFTで実在の電子励起を追うことではありません。電子の仮想運動と核運動の時間尺度を分離し、軌道をBO面の近傍に保つ必要があります。μ・時間刻み・直交性許容誤差を変えて、仮想運動エネルギーと核運動へのエネルギー移動を監視します。温度制御を加えない理想的な拡張系の保存量E_extと、核の運動エネルギー＋BOエネルギーを区別します。狭いギャップや金属への適用をこの説明だけで保証しません。

この節は解説のみです。本章の1原子固定He例が検証するのは静的な全エネルギーとk点・基底・補助格子・SCFの収束です。多原子Heセルの原子間力、エネルギー有限差分と独立参照、BOMDへの力供給は、別章「DFTから原子間力へ」と専用配布版で扱います。BOMD/CPMDの長時間軌道、時間刻み・SCF公差・仮想質量μへの感度、温度制御は段階を分けて検証します。

別の固定入力の教育例では、無次元の2準位電子角と核座標によるBO/CP型連成を短時間だけ実行しています。この模型は本章の周期He計算を動かしたものではなく、一般のKohn–Sham BOMD/CPMD・実材料・長時間MDの検証とは区別します。

$$
E_{\mathrm{BO}}(\mathbf R)=\min_{\langle\psi_i|\psi_j\rangle=\delta_{ij}}E_{\mathrm{KS}}[\{\psi_i\};\mathbf R],\qquad M_I\ddot{\mathbf R}_I=\mathbf F_I=-\nabla_{\mathbf R_I}E_{\mathrm{BO}}(\mathbf R)
$$

$$
L_{\mathrm{CP}}=\frac12\sum_I M_I|\dot{\mathbf R}_I|^2+\frac{\mu}{2}\sum_i\langle\dot\psi_i|\dot\psi_i\rangle-E_{\mathrm{KS}}+\sum_{ij}\Lambda_{ij}\bigl(\langle\psi_i|\psi_j\rangle-\delta_{ij}\bigr)
$$

$$
\langle\psi_i|\psi_j\rangle=\delta_{ij},\qquad K_{\mathrm{fict}}=\frac{\mu}{2}\sum_i\langle\dot\psi_i|\dot\psi_i\rangle,\qquad E_{\mathrm{ext}}=\sum_I\frac{M_I}{2}|\dot{\mathbf R}_I|^2+E_{\mathrm{KS}}+K_{\mathrm{fict}}
$$

2準位模型のBO/CP型連成と短い核熱浴: https://hrkoyama.github.io/numerical-methods-atlas/validation/two-state-bo-cp-ou/?lang=ja

https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/source-manifest.json

## 保存した実測値

- max_reference_energy_error: 4.71162763809e-05
- max_scf_commutator: 3.48433764277e-07
- max_orbital_residual: 7.43065453612e-07
- max_electron_count_error: 4.4408920985e-16
- max_orthogonality_error: 4.86132023525e-10
- max_energy_reconstruction_error: 0
- min_sampled_ks_gap: 0.656519700269
- max_overlap_condition: 508833030.474
- min_overlap_eigenvalue: 4.14810500792e-09
- max_tight_scf_commutator: 1.00490076615e-08
- kpoint_last_change: 0.000525013074401
- basis_last_change: 3.34202303871e-05
- auxiliary_last_change: 2.52654341004e-07
- scf_last_change: 1.86517468137e-14

https://hrkoyama.github.io/code/periodic-dft/2026-11-22/results/result.json

## 実行

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/periodic-he-dft/?lang=ja

## 文献

- Felix Bloch (1929). Über die Quantenmechanik der Elektronen in Kristallgittern. https://link.springer.com/article/10.1007/BF01339455 — 出版社の書誌・抄録を確認。受理年1928と掲載年1929を区別しました。原論文全体の再現・監査ではありません。
- P. Hohenberg and W. Kohn (1964). Inhomogeneous Electron Gas. https://doi.org/10.1103/PhysRev.136.B864 — 既存アトラスの原著書誌・DOIを確認。基礎理論の出典であり、この有限基底計算による定理の証明ではありません。
- W. Kohn and L. J. Sham (1965). Self-Consistent Equations Including Exchange and Correlation Effects. https://doi.org/10.1103/PhysRev.140.A1133 — 既存アトラスの原著書誌・DOIを確認。Kohn–Sham法の原著として引用し、論文全体の数値再現は主張しません。
- H. J. Monkhorst and J. D. Pack (1976). Special points for Brillouin-zone integrations. https://doi.org/10.1103/PhysRevB.13.5188 — 既存アトラスの原著書誌・DOIを確認。本例のΓを含むメッシュ規約は本文と入力に明記し、原論文の全メッシュと同一とは扱いません。
- S. H. Vosko, L. Wilk and M. Nusair (1980). Accurate spin-dependent electron liquid correlation energies for local spin density calculations: a critical analysis. https://doi.org/10.1139/p80-159 — 公式Libxc資料のLDA_C_VWN（VWN5）の原著DOIと書誌を確認。出版社本文へはアクセスできず、全文や表の監査は行っていません。
- S. Goedecker, M. Teter and J. Hutter (1996). Separable dual-space Gaussian pseudopotentials. https://journals.aps.org/prb/abstract/10.1103/PhysRevB.54.1703 — 出版社の書誌・抄録を確認。実際のHe係数は同梱データと両ライブラリで照合し、原論文の表からの全桁の直接転記とは扱いません。
- Qiming Sun et al. (2020). Recent developments in the PySCF program package. https://doi.org/10.1063/5.0006074 — 出版社の書誌・抄録と既存アトラスの登録を確認。今回使用する周期APIは下記の公式資料と固定版コードでも確認します。
- M. F. Herbst, A. Levitt and E. Cancès (2021). DFTK: A Julian approach for simulating electrons in solids. https://proceedings.juliacon.org/papers/10.21105/jcon.00069 — 出版社の書誌と公開論文の導入部を確認。今回の参照計算は独立した数値検査であり、論文中の全例の再現ではありません。
- PySCF developers (2026). Crystal structure. https://pyscf.org/user/pbcgto.html — 格子ベクトル、単位、GTH基底・擬ポテンシャル、k点生成の該当箇所を参照。原法の論文とは区別します。
- PySCF developers (2026). Periodic SCF and density fitting. https://pyscf.org/user/pbc/scf.html — 周期SCF、DFT、FFTDF、カットオフ、Coulomb発散の取り扱いの該当箇所を参照。
- DFTK developers (2026). DFTK API and pseudopotentials. https://docs.dftk.org/stable/api/ — 格子・k点・汎関数・SCFの該当APIと公式擬ポテンシャル解説を参照。配布物には実際に使用した版を別途固定します。
- Libxc developers (2026). Libxc functionals: LDA_X and LDA_C_VWN. https://libxc.gitlab.io/functionals/ — LDA_X（id 1）とLDA_C_VWN（id 7、VWN5）の識別・原著リンクを確認。両エンジンが共用する評価ライブラリとして明記します。
- M. Born and R. Oppenheimer (1927). Zur Quantentheorie der Molekeln. https://onlinelibrary.wiley.com/doi/10.1002/andp.19273892002 — 出版社の書誌・DOIを確認。Born–Oppenheimer分離の歴史的基礎として引用し、原文全文の監査や現代のMD実装の再現は主張しません。
- R. Car and M. Parrinello (1985). Unified Approach for Molecular Dynamics and Density-Functional Theory. https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.55.2471 — 出版社の書誌・抄録と公開原文の式(3)–(5)、BO面近傍の仮想電子運動の議論を参照。論文のSi動力学の数値再現は行っていません。
- Quantum ESPRESSO developers (2026). cp.x input description: electron dynamics, emass and orthogonalization. https://www.quantum-espresso.org/Doc/INPUT_CP.html — 仮想質量、電子と核の運動、時間刻み、直交化と断熱性に関する入力項目を参照。ソフトウェアの実行検証は行っていません。
