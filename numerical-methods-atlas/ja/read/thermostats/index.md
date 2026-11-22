# サーモスタット：温度制御と分布の比較

温度の平均だけでなく、揺らぎ・エルゴード性・時間相関を比べる。Nosé–Hoover、速度スケーリングから確率的・運動量保存型の手法まで。

12手法のうちLangevinとCSVRの2手法に専用実装。旧1自由度Langevin/BAOABの調和例を保持し、別版の同じOBABO分割で、非縮退2自由度の調和系とquartic係数λ=0.2の2自由度非調和系を比較します。CSVR単独の運動エネルギー核も検査。他の10手法は実装予定です。

## 何の温度を制御するか

運動エネルギーをK、有効自由度数をfとすると、運動温度は T = 2 K / (f k_B)。拘束や重心運動の除去に応じてfを数え、流れがある場合は熱運動と平均流を区別する。回転自由度を含むかも明記する。

## 同じ平均温度でも分布は違う

古典的な二次形式の運動エネルギーを持つf個の独立な運動量自由度では、正準平衡で 2 K/(k_B T₀) は自由度fのχ²分布。平均Kはf k_B T₀/2、分散はf(k_B T₀)²/2となる。単純な速度スケーリング v ← √(T₀/T) v は適用直後のKを固定し、この揺らぎを再現しない。CSVRは確率的な係数で揺らぎを生成する別の手法である。

## 分布の標本化と運動の再現を分ける

正しい不変分布を持っていても、有限時間の軌道が十分に探索するとは限らない。また平衡分布が正しくても、摩擦や衝突で速度自己相関や拡散は変わり得る。有限時間刻みの誤差、熱浴の結合時間、乱数依存性まで含めて評価する。

## CSVRとLangevin：正準分布・揺らぎ・相関を比べる

新しい比較は古典的な少自由度系に限定します。CSVRとLangevinに同じOBABO分割、自由度、温度、ポテンシャル、観測時刻を使い、分布・揺らぎ・相関を別々に評価します。従来のBAOAB調和振動子の結果は別の配布版として保持します。

### CSVRの確率的更新と符号

CSVRは各運動量成分へ独立なノイズを加えず、全自由度の運動エネルギーを確率的に進め、同じ係数で運動量を拡大・縮小します。2007年論文の運動エネルギーSDEと厳密伝播式、2008年論文の符号付き係数を採用します。以下のhは熱浴のサブステップです。

同じ正規乱数RをKの更新と符号の判定に使います。少自由度では符号反転を捨てられません。Sは自由度f−1のχ²乱数で、f=1では厳密に0です。原著者は2007年論文のGammaによる二乗和生成の説明に誤植を指摘しているため、採用コードはχ²を直接生成します。

$$
dK=\frac{\bar K-K}{\tau}\,dt+2\sqrt{\frac{K\bar K}{f\tau}}\,dW
$$

$$
c=e^{-h/\tau},\quad a=\frac{(1-c)\bar K}{f},\quad K^+=\left(\sqrt{cK}+\sqrt a\,R\right)^2+aS,\quad R\sim N(0,1),\quad S\sim\chi^2_{f-1}
$$

$$
\alpha=\operatorname{sign}\!\left(\sqrt{cK}+\sqrt a\,R\right)\sqrt{K^+/K},\qquad p_i^+=\alpha p_i
$$

### 同じ分割順序で比べる

今回の2方式は、MD刻みをΔtとしてO(Δt/2)–B(Δt/2)–A(Δt)–B(Δt/2)–O(Δt/2)という同じOBABO順序を使います。Aは座標移動、Bは力による運動量更新、Oは熱浴です。CSVR更新式ではh=Δt/2を使います。OBABOの中央にはvelocity Verletがあり、両端の熱浴だけを入れ替えます。

τ=(2γ)⁻¹として、ポテンシャルのない熱浴の運動エネルギー緩和を揃えます。同じ数字のτを摩擦時間γ⁻¹と同一視しません。f=1では符号付きCSVRとLangevinの熱浴は同じ遷移分布となり、採用実装は与えたノイズを対応させて照合します。

以前のBAOAB例はB–A–O–A–Bという別の分割です。旧結果と独立線形参照は保存したまま、今回のOBABOの離散参照や誤差の結果に置き換えません。

$$
\tau=(2\gamma)^{-1},\qquad p^+=e^{-\gamma h}p+\sqrt{m k_B T_0(1-e^{-2\gamma h})}\,R_{\rm phys}\quad(f=1)
$$

### 分布・揺らぎ・相関の三つの判定

静的な正準分布は両方式で共通です。運動量と運動エネルギー、瞬間温度の分布・平均・分散を確認し、位置の参照は調和系の解析分布、非調和系では別の数値求積から作ります。温度の平均だけが一致しても、揺らぎの再現は確認できません。

動的な相関は熱浴の方式と結合時間に依存します。座標q、運動量p、運動エネルギーK、全エネルギーHを観測し、方法間で一致することを成功条件にはしません。Langevinの調和系は連続行列指数とOBABOの離散定常共分散・伝播を分け、他の全系相関は測定値・不確かさ・刻み依存として示します。

ρK(t)=exp(−t/τ)という厳密参照は、Hamiltonianの力や位置更新を含まない熱浴単独の検査です。調和・非調和の全系ではKとUが交換するので、この式をそのまま当てません。

CDFの誤差は、入力で先に固定した位置・エネルギーの各5点、条件付き熱浴では3分位点などで調べた最大差です。分布全域の上限を取るKolmogorov–Smirnov統計量ではありません。全系の相関は正準参照の平均・分散で中心化・正規化しているため、有限刻みの零時差値が厳密に1とは限りません。

$$
K=\sum_{i=1}^{f}\frac{p_i^2}{2m_i},\quad \bar K=\frac{f k_B T_0}{2},\quad T_{\rm inst}=\frac{2K}{f k_B}
$$

$$
\frac{2K}{k_B T_0}\sim\chi_f^2,\quad \operatorname{Var}K=\frac{f(k_B T_0)^2}{2},\quad \operatorname{Var}T_{\rm inst}=\frac{2T_0^2}{f}
$$

$$
C_X(t)=\langle(X(t)-\langle X\rangle)(X(0)-\langle X\rangle)\rangle,\qquad \rho_X(t)=C_X(t)/C_X(0)
$$

$$
\mathbb E[K^+\mid K]=cK+fa,\quad\operatorname{Var}(K^+\mid K)=2fa^2+4acK,\quad \rho_K(t)=e^{-t/\tau}\ \text{(bath only)}
$$

### 標本化の限界と実装の境界

正準な初期アンサンブルを保つ検査と、温度をずらした初期値から平衡へ近づく検査を区別します。複数の独立レプリカと固定seed、有限の観測窓を使い、標本誤差と刻み誤差・結合時間依存を混ぜません。採用した少自由度の検査は任意の初期値からの一般的な混合保証ではありません。 相関の標準誤差は、各時差で独立レプリカ間の積のばらつきから求めています。単一軌道の時間平均や、有効標本数を評価した誤差ではありません。非調和系の全系相関には独立な動的参照をまだ持たず、誤差ゼロとは表示しません。

全体を同じ係数でスケールする熱浴は、運動量空間の向きを直接ランダム化しません。対称性のある系で全運動量ゼロなどを保つ不変条件や、閉じた不変部分空間、同一周波数の特殊な系などによる探索不足を、正しいK分布だけで否定できません。今回の自由度には拘束や重心除去を追加していません。

正の熱浴刻みでK=0なら元の向きがなく、速度の比によるglobal rescaleは定義できないため、採用コードは明示的に拒否します。そこへ任意の向きを注入する別アルゴリズムとしては扱いません。非有限値、非正の温度・質量、無効な自由度や時間も検査します。

## 検証済みの範囲と次の課題

3つの新例は、熱浴単独の厳密則、少自由度の調和系、弱い非調和系を別々に検査します。各例で固定入力、実測値、誤差と不確かさ、受入条件、コード、テスト、配布ZIP、独立展開からの追試記録へ進めます。旧BAOAB例は別の根拠です。他の10手法は専用の実装・検証をまだ持ちません。

## 出典と確認範囲

CSVRについては2007年原著の著者稿の運動エネルギー式と付録、2008年原著の著者稿の符号付き更新式、原著者の誤植訂正を確認し、採用した小規模な古典例を独立参照・求積・再実行で検証しています。原著のLennard–JonesやTIP4P水の数値実験の再現ではありません。他の10方式は比較解説・一次文献への案内であり、ここで数値検証したと表示しません。Gaussian isokineticの個別原論文の整理も継続課題です。

- G. Bussi, D. Donadio and M. Parrinello (2007). Canonical sampling through velocity rescaling. https://arxiv.org/html/0803.4060v1
- G. Bussi and M. Parrinello (2008). Stochastic thermostats: comparison of local and global schemes. https://arxiv.org/html/0803.4397v1
- Giovanni Bussi (2026). Algorithms: stochastic velocity rescaling, author correction note. https://sites.google.com/site/giovannibussi/Research/algorithms

## 実行・検証例

### Langevin温度制御：正準分布・刻み偏り・時間相関

調和ポテンシャル・固定seedの分布検証です。位置分散が正確でも運動量には有限刻み偏りがあります。他のサーモスタット、一般分子系、長時間の第一原理MDへ検証を移しません。

Entry: https://hrkoyama.github.io/numerical-methods-atlas/validation/langevin-harmonic/?lang=ja
ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/verification.json

### CSVRの厳密浴：条件付き分布・揺らぎ・運動エネルギー相関

浴の診断用ケースで独立した物理問題数へ加算しません。浴がKを正しく分布させてもglobal rescalingだけでは方向を熱化しません。exp(−t/τ)を力付きMDのK相関へ流用しません。固定seedと予算に対する統計判定で、一般の混合保証ではありません。

Entry: https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-kinetic-kernel/?lang=ja
ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/atlas-thermostats-2026-11-22.zip
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/verification.json

### CSVRとLangevin：調和2自由度の分布・揺らぎ・相関

global CSVRとlocal Langevinの運動相関が等しいとは要求しません。CDF差は指定5点の最大であり全実数上のKS距離ではありません。正準初期分布の保存と温度摂動からの有限時間確認は一般のエルゴード性証明ではなく、軸上の励起されない自由度が残る反例もテストします。分子・拘束・BOMDには外挿しません。

Entry: https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-harmonic/?lang=ja
ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/atlas-thermostats-2026-11-22.zip
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/verification.json

### 非調和CSVRとLangevin：Boltzmann求積との分布比較

特定の分離可能な四次2自由度・固定seedだけの小さな例です。Hを調和系のGamma分布と扱いません。全系相関には独立な厳密動力学参照がなく、相関一致や統計誤差に隠れる時間次数を合格主張しません。成熟分子系・輸送係数・量子・第一原理MDの検証ではありません。

Entry: https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-quartic/?lang=ja
ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/atlas-thermostats-2026-11-22.zip
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/verification.json
