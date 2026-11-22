# 作用素分割：Lie–Trotter と Strang の比較

作用素分割：Lie–Trotter と Strang の比較


作用素分割（演算子分割）は、足し合わせた右辺を別々の発展問題として解き、その解の写像を合成する時間積分の考え方です。Lie–Trotterは順番に全刻み、Strangは対称な半刻み・全刻み・半刻みに分けます。部分問題を厳密に解いても、順序が交換できなければ合成には誤差が残ります。


同じ反応拡散で実行して比べる：32格子・T=1のSchnakenberg系で、初期場・部分ソルバー・出力時刻をそろえ、4つの時間刻みでLie–Trotterの1次とStrangの2次を測ります。参照は同じFD半離散系の非分割Radau／DOP853で、空間収束や連続PDEの厳密解とは区別します。

[固定入力・結果・コード・16検査の追試記録](/numerical-methods-atlas/validation/reaction-diffusion-splitting/?lang=ja)

何を分割し、何を1刻みと数えるか



$$
\dot u=F(u)+G(u),\qquad \dot v=F(v)\ \Rightarrow\ \varphi_F^h,\qquad \dot w=G(w)\ \Rightarrow\ \varphi_G^h.
$$

ここでは自律的で十分滑らかな有限次元の初期値問題を考えます。φは部分方程式を指定時間だけ進める厳密な流、hは元の和の方程式に対する1刻みです。合成は右端から適用します。Fをh進めてからGをh進めても、元の問題の時間はhだけ進めた近似であり、2hではありません。各部分をh/2ずつ進めるだけでは元の右辺を半分にしてしまいます。


反応と拡散、移流と生成項、分離可能なHamiltonianの運動と力などで、部分問題を簡単に解ける構造を利用できます。分割は空間離散化や物理モデルの変更とは別の選択です。線形の場合だけF(u)=Au、G(u)=Buと置いて行列指数で表します。


Lie–Trotter splitting：順に全刻み進める



$$
u^{n+1}=L_h(u^n)=(\varphi_G^h\circ\varphi_F^h)(u^n),\qquad L_h=e^{hB}e^{hA}\quad(\dot u=(A+B)u).
$$

この章の規約は「Fを先に、更新後の状態にGを適用」です。逆順のG→Fも1次法ですが、非可換なら異なる値になります。元のuⁿからFとGをそれぞれ計算して足す更新ではありません。



$$
e^{hB}e^{hA}-e^{h(A+B)}=\frac{h^2}{2}(BA-AB)+O(h^3),\qquad [A,B]=AB-BA.
$$

両辺をh²までTaylor展開すると、正確な和の流との違いに交換子が残ります。上式の符号は採用した積の順序に対応し、逆順では先頭の交換子項の符号が反転します。局所欠損は厳密な初期値からの1ステップ差でO(h²)、安定性と滑らかさを仮定して固定終時刻まで積み重ねた誤差はO(h)です。積公式の極限と、有限刻みでの誤差評価を区別してください。


Strang splitting：対称化して2次にする



$$
u^{n+1}=S_h(u^n)=(\varphi_F^{h/2}\circ\varphi_G^h\circ\varphi_F^{h/2})(u^n),\qquad S_h=e^{hA/2}e^{hB}e^{hA/2}.
$$

Fの半刻み、Gの全刻み、Fの半刻みを、毎回更新された状態に適用します。G/2→F→G/2も別の有効なStrang型です。両者は一般に同じ数値解ではなく、誤差定数も異なります。



$$
S_{-h}=S_h^{-1},\qquad S_h-e^{h(A+B)}=O(h^3),\qquad [A,B]=0\ \Rightarrow\ L_h=S_h=e^{h(A+B)}.
$$

逆向きの流が存在すれば、対称合成は刻みhを−hにすると元へ戻ります。2次項までの展開ではLie–Trotterの先頭誤差が打ち消され、局所欠損O(h³)、大域誤差O(h²)になります。次の誤差項には入れ子の交換子が現れます。有限行列のAとBが可換なら、厳密な部分流の両方式は和の厳密流と一致します。非有界PDE作用素へこの結論を移すには定義域・正則性の確認が必要です。


次数・対称性・計算量を比較する




| 比較する量 | Lie–Trotter | Strang |
| --- | --- | --- |
| 実際に適用する順序 | F(h), G(h) | F(h/2), G(h), F(h/2) |
| 1ステップの局所欠損 | O(h²) | O(h³) |
| 固定終時刻での大域誤差 | O(h) | O(h²) |
| 厳密な部分流での時間対称性 | 一般にはなし | あり（可逆な流の場合） |
| 1ステップの部分流呼出し数 | 2 | 3 |
| 刻み半減時の誤差比の目安 | 約2 | 約4 |



$$
E(h)=\|u_N-u(T)\|_2,\quad h=T/N,\qquad p_{\rm obs}=\log_2\frac{E(h)}{E(h/2)},\qquad E_L(h)=O(h),\ E_S(h)=O(h^2).
$$

同じhならStrangは部分流を1回多く呼びます。ただし一定刻みを連続適用し、Fの厳密流の群性（拡散では正時間の半群性）を使えると、隣接するFの半刻みを全刻みにまとめられます。NステップならLie–Trotterは2N回、Strangは結合後2N+1回の部分流呼出しです。部分流ごとの費用、出力や境界処理、数値流が結合できるかで実費用は変わり、呼出し数を実測速度とみなしません。


小さな非可換例：同じ厳密流で次数を測る



$$
u=\begin{pmatrix}q\\p\end{pmatrix},\quad A=\begin{pmatrix}0&1\\0&0\end{pmatrix},\quad B=\begin{pmatrix}0&0\\-1&0\end{pmatrix},\quad u(0)=\begin{pmatrix}1\\0\end{pmatrix},\quad u(t)=\begin{pmatrix}\cos t\\-\sin t\end{pmatrix}.
$$


$$
\varphi_A^h(q,p)=(q+hp,p),\qquad\varphi_B^h(q,p)=(q,p-hq),\qquad [A,B]=\begin{pmatrix}-1&0\\0&1\end{pmatrix}.
$$


$$
L_hu_0=\begin{pmatrix}1\\-h\end{pmatrix},\quad S_hu_0=\begin{pmatrix}1-h^2/2\\-h\end{pmatrix},\quad u(h)=\begin{pmatrix}1-h^2/2+O(h^4)\\-h+h^3/6+O(h^5)\end{pmatrix}.
$$

q、p、時間はすべて無次元とした2成分の調和振動子です。部分流は足し算と掛け算だけで厳密に適用でき、参照はcosとsinによる解析解です。初回の式だけでも局所欠損の次数を確認できます。q成分だけでは特別な打消しを見落とすので、2成分のノルムを使います。空間格子・独立PDE実装・量子化学計算を用いない軽量な教材例です。




| N | h | Lie–Trotter E(h) | p | Strang E(h) | p |
| --- | --- | --- | --- | --- | --- |
| 8 | 0.125 | 5.220647e-02 | — | 2.075134e-03 | — |
| 16 | 0.0625 | 2.617930e-02 | 0.9958 | 5.176511e-04 | 2.0032 |
| 32 | 0.03125 | 1.311628e-02 | 0.9971 | 1.293422e-04 | 2.0008 |
| 64 | 0.015625 | 6.565750e-03 | 0.9983 | 3.233115e-05 | 2.0002 |


固定したu₀=(1,0)、T=1、N=8,16,32,64を実際に再計算した保存値です。最後の刻み半減で大域の観測次数はLie–Trotterが0.9983、Strangが2.0002。別に厳密な初期値から1刻みだけ比較すると局所の次数は約2と3です。逆順のLie–Trotterも大域1次で異なる解となること、可換なA=−I、B=−2Iでは解析解exp(−3T)との差が浮動小数点の丸め程度となることを対照にしています。


適用条件：2次精度や安定性が崩れる場合


表示した次数は、滑らかな解、十分小さい刻み、固定した有限区間、適切な安定性を仮定します。衝撃波・硬い緩和・非滑らかな初期値では同じ次数を期待できるとは限りません。PDEでは境界値を部分問題と各段階に整合させます。非同次・時間依存境界による次数低下や、空間誤差・非線形反復誤差の支配は別々に点検します。


部分流を近似する場合、単に対称な並べ方にしただけでは2次は保証されません。通常のStrang構成で2次を保つには、各部分ソルバーにも少なくとも2次の整合性と十分厳しい反復公差が必要です。時間対称性も必要なら、厳密流または対称な部分ソルバーを使います。前進Eulerや後退Eulerをそのまま代入すると一般に1次へ落ちます。非自律問題では時刻も含めた拡大系または整合した部分問題の時刻を設計し、すべてを同じ時刻に凍結しないでください。



$$
\det L_h=\det S_h=1,\quad\operatorname{tr}L_h=\operatorname{tr}S_h=2-h^2,\quad 0この振動子では両方式の行列の行列式は1、トレースは2−h²で、安定な振動モードの範囲は0<|h|<2です。部分流を厳密に解くこと自体は無条件安定性を保証しません。また部分流が保つ量だけが合成にも引き継がれるので、Hamiltonian系のシンプレクティック性を、任意の反応系の正値性・全エネルギーの厳密保存へ読み替えません。


既存のStrang実行例とIMEXとの違い


既存の反応拡散の[Schnakenberg有限振幅過渡](/numerical-methods-atlas/validation/schnakenberg-nonlinear/?lang=ja)と[飽和パターン](/numerical-methods-atlas/validation/schnakenberg-pattern/?lang=ja)は、中心差分の拡散を厳密に半刻み進め、反応を陰的中点則で全刻み解くStrang合成です。その固定条件での空間・時間収束は既存の公開記録を参照します。本章の振動子による次数確認と区別し、過去の配布物・公差・結果を変更しません。


IMEXも右辺を複数の部分に分けますが、[IMEX時間積分](/numerical-methods-atlas/ja/read/stiff-integration/)は陽・陰の段階式を組み合わせる方式です。ここでの部分流を順に合成する分割法とは同じ更新式ではありません。分離Hamiltonianでの関係は[シンプレクティック積分](/numerical-methods-atlas/ja/read/symplectic/)も参照してください。


軽量な再計算と公開範囲


上の表・局所欠損・逆順・可換対照はPython 3の標準ライブラリだけで再計算できます。スクリプトは結果をJSONで標準出力に書き、--checkでは保存値と照合します。これは解説用の固定2成分例で、汎用分割ソルバーの配布版や共通実行例台帳への新規登録ではありません。この振動子のスクリプトは解説例として保持します。別の軽量な反応拡散の専用配布版で両手法を実行でき、その固定入力の範囲で「教育用例・関連コードあり」と表示します。


[教材例の再計算スクリプト](/scripts/verify-operator-splitting.py) · [固定入力・保存数値 / JSON](/numerical-methods-atlas/assets/operator-splitting.json)




```text
python3 verify-operator-splitting.py
python3 verify-operator-splitting.py --check operator-splitting.json
```

## 固定入力の実行例と診断対照

受入条件が示す検証範囲と数学的な一般保証を区別します。旧版の入力・測定・公差は保持します。

### 同じ非線形反応拡散でLie–TrotterとStrangを比較する

固定標的の計算例

32格子・終了時刻1のSchnakenberg反応拡散を、同じ入力・部分ソルバーでLie–TrotterとStrangにより進めます。4段階の時間刻みで1次／2次の収束、参照の感度、反応収支と未収束時の失敗を確かめる軽量な比較例です。

固定格子での採用合成法の時間誤差であり、分割誤差と反応中点則の離散誤差を含みます。連続PDEの厳密解・空間収束・独立PDE実装の照合とは呼びません。u+vは反応で保存せず、正濃度は固定入力での観測です。計算費は実際の部分流呼出し数で示し、速度の順位やStrangの一般的優越を主張しません。既存Schnakenberg問題の追加比較で、物理問題数・共通22例・旧配布版の公差や成功履歴を増減・変更しません。長時間パターン・2D・一般境界は対象外です。

[入力・結果・受入条件](/numerical-methods-atlas/validation/reaction-diffusion-splitting/?lang=ja) · [手法・一次文献](/numerical-methods-atlas/ja/read/validation-splitting/#reaction-diffusion-splitting) · [コード run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/splitting/run.py) · [コード splitting.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/splitting/splitting.py) · [コード reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/splitting/reference.py) · [テスト test_splitting.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/splitting/test_splitting.py) · [ZIP](/code/validated-examples/2026-11-22/splitting/atlas-splitting-2026-11-22.zip) · [結果](/code/validated-examples/2026-11-22/splitting/results/result.json) · [追試記録](/code/validated-examples/2026-11-22/splitting/verification.json)

## 公開範囲

2成分振動子の解説例を保持し、同じSchnakenberg反応拡散で両手法を比較する専用の軽量配布版を追加しました。教育用実装の確認範囲は32格子・T=1の固定入力です。既存の物理問題数・共通22例・旧配布版・公差・検証履歴を保持します。

## 文献

- H. F. Trotter (1959). On the product of semi-groups of operators. https://doi.org/10.1090/S0002-9939-1959-0108732-6
- G. Strang (1968). On the Construction and Comparison of Difference Schemes. https://doi.org/10.1137/0705041
- E. Hairer (2010). Geometric Numerical Integration, Lecture2. https://www.unige.ch/~hairer/poly_geoint/week2.pdf
