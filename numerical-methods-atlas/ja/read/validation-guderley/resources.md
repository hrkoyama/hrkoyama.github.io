# Guderley収束衝撃波：球対称の軽量検証

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-guderley/

この章に登録された手法・問題・実行例の関連資料です。

## 手法

- [HLL](<https://hrkoyama.github.io/numerical-methods-atlas/methods/hll/?lang=ja>)

  球殻の面積・体積と幾何学的な圧力源を使う区分定数HLL有限体積流束、物理時間のHeun更新による限定例です。
- [Heun法／SSPRK(2,2)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=ja>)

  球殻の面積・体積と幾何学的な圧力源を使う区分定数HLL有限体積流束、物理時間のHeun更新による限定例です。
- [HLL](<https://hrkoyama.github.io/numerical-methods-atlas/methods/hll/?lang=ja>)
- [Heun法／SSPRK(2,2)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=ja>)

## 方程式

- [圧縮性Euler方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#euler-ja>)

  1次元の保存形。状態方程式と初期・境界条件は各テストの定義を参照する。 理想気体Eulerの球半径対称系。球殻体積を重みとして密度・半径運動量・全エネルギーを発展させ、半径運動量の幾何源を分けて積算します。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/guderley-implosion/?lang=ja#guderley-implosion-ja-algorithm>)

  面積4πr²と球殻体積4πΔ(r³)/3を用いた第一次数の球対称有限体積法です。共有HLL面流束の発散に、半径方向運動量の圧力幾何項p_iΔA/Vを加え、Heun法・CFL=.4で更新します。中心は面積ゼロの反射条件、外側は各RK段の実時刻に評価した相似場です。全3保存量について実際の境界面流束と幾何ソースを同じHeun重みで積分します。状態floor、圧力修復、時間刻みの隠れた再試行はありません。
- [圧縮性Euler方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#euler-ja>)

  1次元の保存形。状態方程式と初期・境界条件は各テストの定義を参照する。

## 問題の図

- [Guderleyの収束衝撃波](<https://hrkoyama.github.io/numerical-methods-atlas/problems/guderley/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/guderley/results/guderley-implosion-preview.png
- [Guderley収束衝撃波：球対称の軽量検証](<https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/guderley/results/guderley-implosion.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/guderley/results/guderley-implosion.png

## 厳密解・参照解

- [Guderleyの収束衝撃波：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/guderley/?lang=ja#references-ja>)

  γ=1.4・冷たい一様な上流を持つ球対称Guderley相似解の収束前分岐です。相似指数の固有値探索・相似ODE積分・衝撃位置で分割した球殻求積を含む半解析参照で、閉形式の厳密セル平均ではありません。ExactPackに基づく参照実装と有限体積PDE計算の役割を分け、独立した相似解実装どうしの照合とは扱いません。原点での収束、反射後の衝撃波、一般のEOSは今回の範囲外です。
- [Guderley収束衝撃波：固有値と球対称の半解析参照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-guderley-ja>)
  relation: same-problem
  reference_kind: semi-analytic

  半解析解 理想気体Eulerの球半径対称、γ=1.4、未衝撃の上流はρ0=1,u=p=0。Lazarus時間t∈[-1,-.85]、原点での収束はt=0で今回の区間外、r∈[0,.75]、R_s(t)=.6(-t)^α、α=1/λです。初期場も衝撃を含む相似場であり、領域全体が圧力ゼロの初期値ではありません。λは固定ExactPackの固有値計算で求め、同じ固定ソースの相似ODEを収束前だけ積分します。球殻は衝撃位置で分割し、保存量をGauss16で体積平均してGauss32と比較し、その平均保存量からpを計算します。閉形式の厳密セル平均ではありません。ExactPackの高密度出力アダプターであり、独立した半解析実装との照合とは扱いません。図は1D半径計算の2D中心断面表示で、2D Cartesianや原点反射後の計算ではありません。 γ=1.4・冷たい一様な上流を持つ球対称Guderley相似解の収束前分岐です。相似指数の固有値探索・相似ODE積分・衝撃位置で分割した球殻求積を含む半解析参照で、閉形式の厳密セル平均ではありません。ExactPackに基づく参照実装と有限体積PDE計算の役割を分け、独立した相似解実装どうしの照合とは扱いません。原点での収束、反射後の衝撃波、一般のEOSは今回の範囲外です。
- [Guderley収束衝撃波：固有値と球対称の半解析参照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-guderley-ja>)
  reference_kind: semi-analytic

  半解析解 理想気体Eulerの球半径対称、γ=1.4、未衝撃の上流はρ0=1,u=p=0。Lazarus時間t∈[-1,-.85]、原点での収束はt=0で今回の区間外、r∈[0,.75]、R_s(t)=.6(-t)^α、α=1/λです。初期場も衝撃を含む相似場であり、領域全体が圧力ゼロの初期値ではありません。λは固定ExactPackの固有値計算で求め、同じ固定ソースの相似ODEを収束前だけ積分します。球殻は衝撃位置で分割し、保存量をGauss16で体積平均してGauss32と比較し、その平均保存量からpを計算します。閉形式の厳密セル平均ではありません。ExactPackの高密度出力アダプターであり、独立した半解析実装との照合とは扱いません。図は1D半径計算の2D中心断面表示で、2D Cartesianや原点反射後の計算ではありません。
- [Guderley収束衝撃波：球対称の軽量検証：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/guderley-implosion/?lang=ja#guderley-implosion-ja-validation>)

  33単体検査と3格子55判定を実行前に固定し、警告をエラーにする設定で合格しました。冷たい上流でのゼロ音速HLL分岐、幾何的な静止圧力釣合い、共有流束の収支、実際の2段の境界時刻、不正段の生配列保持を確認します。全体積L1と、あらかじめr≥.8Rsとした衝撃・非零流れ領域のL1を並べ、冷たい内側で誤差を薄めないようにします。密度・圧力の最大差と保存した時系列からの衝撃軌道も残します。半解析参照は固定LANL ExactPackの相似指数固有値ルーチンとODEを使い、反射後分岐を計算しないキャッシュ付きアダプターです。独自に再実装した相似ODEとは表示しません。別に実装したEuler有限体積計算と参照を比較します。 全体積の密度L1は.02345/.01339/.007722、圧力L1は.03277/.01743/.009477でした。r≥.8Rsの密度L1も.02414/.01378/.007948と減少します。最細の衝撃位置は.530273、相似参照は.533989で、差は約2.54セルです。最大の全3成分収支残差は8.85e-16、全段の最小内部エネルギーと音速専用丸めガード回数はともに0でした。参照のEuler差分代入残差は8.24e-9、有限オフセットの移動衝撃ジャンプ残差は4.40e-8。固有値計算を含む全3計算は元のMacで約44.6秒でした。
- [Guderley収束衝撃波：固有値と球対称の半解析参照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-guderley-ja>)
  relation: same-problem
  reference_kind: semi-analytic

  半解析解 理想気体Eulerの球半径対称、γ=1.4、未衝撃の上流はρ0=1,u=p=0。Lazarus時間t∈[-1,-.85]、原点での収束はt=0で今回の区間外、r∈[0,.75]、R_s(t)=.6(-t)^α、α=1/λです。初期場も衝撃を含む相似場であり、領域全体が圧力ゼロの初期値ではありません。λは固定ExactPackの固有値計算で求め、同じ固定ソースの相似ODEを収束前だけ積分します。球殻は衝撃位置で分割し、保存量をGauss16で体積平均してGauss32と比較し、その平均保存量からpを計算します。閉形式の厳密セル平均ではありません。ExactPackの高密度出力アダプターであり、独立した半解析実装との照合とは扱いません。図は1D半径計算の2D中心断面表示で、2D Cartesianや原点反射後の計算ではありません。 γ=1.4・冷たい一様な上流を持つ球対称Guderley相似解の収束前分岐です。相似指数の固有値探索・相似ODE積分・衝撃位置で分割した球殻求積を含む半解析参照で、閉形式の厳密セル平均ではありません。ExactPackに基づく参照実装と有限体積PDE計算の役割を分け、独立した相似解実装どうしの照合とは扱いません。原点での収束、反射後の衝撃波、一般のEOSは今回の範囲外です。

## コード・検証

- [Guderley収束衝撃波：球対称の軽量検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/guderley-implosion/?lang=ja>)
  availability: run

  冷たい静止気体へ内向きに進む球対称Guderley衝撃波を、128/256/512個の球殻でt=−1から−.85まで計算します。HLL流束とHeun法を、相似指数の固有値・半解析場・衝撃位置・保存収支と照合する軽量例です。
