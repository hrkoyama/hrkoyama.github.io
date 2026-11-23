# Mach 3前向きステップ：軽量な2次元検証

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-forward-step/

この章に登録された手法・問題・実行例の関連資料です。

## 手法

- [HLL](<https://hrkoyama.github.io/numerical-methods-atlas/methods/hll/?lang=ja>)

  従来のHLL・MUSCLと勾配制限の比較データを保持し、追加の軽量例は区分定数HLL＋Heunを使います。参照実装の手法は参照の出典と条件で区別します。
- [MUSCL再構成](<https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=ja>)

  従来のHLL・MUSCLと勾配制限の比較データを保持し、追加の軽量例は区分定数HLL＋Heunを使います。参照実装の手法は参照の出典と条件で区別します。
- [Minmod](<https://hrkoyama.github.io/numerical-methods-atlas/methods/minmod/?lang=ja>)

  従来のHLL・MUSCLと勾配制限の比較データを保持し、追加の軽量例は区分定数HLL＋Heunを使います。参照実装の手法は参照の出典と条件で区別します。
- [単調中心勾配制限／MC](<https://hrkoyama.github.io/numerical-methods-atlas/methods/mc/?lang=ja>)

  従来のHLL・MUSCLと勾配制限の比較データを保持し、追加の軽量例は区分定数HLL＋Heunを使います。参照実装の手法は参照の出典と条件で区別します。
- [Heun法／SSPRK(2,2)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=ja>)

  従来のHLL・MUSCLと勾配制限の比較データを保持し、追加の軽量例は区分定数HLL＋Heunを使います。参照実装の手法は参照の出典と条件で区別します。
- [HLL](<https://hrkoyama.github.io/numerical-methods-atlas/methods/hll/?lang=ja>)
- [Heun法／SSPRK(2,2)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=ja>)

## 方程式

- [圧縮性Euler方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#euler-ja>)

  1次元の保存形。状態方程式と初期・境界条件は各テストの定義を参照する。 γ=1.4、ρ=1.4、u=3、v=0、p=1の流入を、[0,3]×[0,1]から高さ.2・開始位置x=.6の段差を除いた2次元Euler系でT=4まで更新します。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/forward-step-m3/?lang=ja#forward-step-m3-ja-algorithm>)

  既存Numartの区分定数HLL・非分割x/y発散・Heun/SSPRK(2,2)を小型配布物にし、6種類の境界ごとに両RK段で実際に使う流束を同じ重みで積算します。CFL=.4、各格子の上限20000刻み。全予測・更新段の正の密度と圧力を確認し、状態floor・修復・隠れた再試行はしません。不正段は生配列と完了履歴を保持して失敗します。
- [圧縮性Euler方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#euler-ja>)

  1次元の保存形。状態方程式と初期・境界条件は各テストの定義を参照する。

## 問題の図

- [Mach 3前向きステップ](<https://hrkoyama.github.io/numerical-methods-atlas/problems/forward-step/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/results/forward-step-m3-preview.png
- [Mach 3前向きステップ：壁面収支と多格子検証](<https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/results/forward-step-m3.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/results/forward-step-m3.png

## 厳密解・参照解

- [Mach 3前向きステップ：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/forward-step/?lang=ja#references-ja>)

  全場の厳密解はありません。新規の別実装C++有限体積参照とその2格子差を示し、主計算との共通の流束族・時間積分、角無補正条件、有限格子の限界を明記します。
- [Mach 3前向きステップ：独立C++有限格子数値参照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-forward-step-ja>)
  relation: same-problem
  reference_kind: numerical-reference

  有限格子の数値参照 γ=1.4の2次元Euler流れ。[0,3]×[0,1]のうちx≥.6,y<.2は固体とし、初期・入口の(ρ,u,v,p)=(1.4,3,0,1)、上下と段差は滑り壁、右端はゼロ勾配、T=4です。参照は独立したC++17実装のprimitive MUSCL（一般化minmod θ1.5）/Davis HLL/HeunをCFL=.3、240×80・480×160で新規実行しました。境界に接する法線方向の傾きはゼロにし、再構築の傾き再調整はセル平均を変えません。Python主計算は区分定数HLL/Heunで、流束族・時間積分式は共有しますが実装と空間再構築は別です。角のエントロピー/エンタルピー補正、状態floor、刻み再試行はありません。角の数値エントロピー層が下流へ移流され得る無補正条件であり、補正付き原著PPM像の再現とは区別します。固体を除いた保存量を保守的に制限してから圧力を算出し、参照格子差・保存収支・局所診断を残します。有限格子の数値参照であり、厳密2次元解、誤差上界、細いすべり線や巻き上がりの収束証明ではありません。 新しく独立実行したC++17のMUSCL/HLL/Heun参照を保存量制限で比較します。同じHLL族・Heunと角無補正条件を共有する有限格子数値参照であり、全場の厳密解や誤差上界ではありません。
- [Mach 3前向きステップ：独立C++有限格子数値参照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-forward-step-ja>)
  reference_kind: numerical-reference

  有限格子の数値参照 γ=1.4の2次元Euler流れ。[0,3]×[0,1]のうちx≥.6,y<.2は固体とし、初期・入口の(ρ,u,v,p)=(1.4,3,0,1)、上下と段差は滑り壁、右端はゼロ勾配、T=4です。参照は独立したC++17実装のprimitive MUSCL（一般化minmod θ1.5）/Davis HLL/HeunをCFL=.3、240×80・480×160で新規実行しました。境界に接する法線方向の傾きはゼロにし、再構築の傾き再調整はセル平均を変えません。Python主計算は区分定数HLL/Heunで、流束族・時間積分式は共有しますが実装と空間再構築は別です。角のエントロピー/エンタルピー補正、状態floor、刻み再試行はありません。角の数値エントロピー層が下流へ移流され得る無補正条件であり、補正付き原著PPM像の再現とは区別します。固体を除いた保存量を保守的に制限してから圧力を算出し、参照格子差・保存収支・局所診断を残します。有限格子の数値参照であり、厳密2次元解、誤差上界、細いすべり線や巻き上がりの収束証明ではありません。
- [Mach 3前向きステップ：壁面収支と多格子検証：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/forward-step-m3/?lang=ja#forward-step-m3-ja-validation>)

  入力・受入基準・24単体検査・数値ソースを主計算の初回検査・PDE実行前に固定しました。解析的なMach3垂直衝撃波のRankine–Hugoniot関係、一様な平行流路、壁の質量・エネルギー流束ゼロ、段差の圧力力の向き、実際の4成分収支、不正段の保持を検査します。別実装のC++17 MUSCL/generalized-minmod θ1.5/HLL/HeunによるNy80/160の参照を新規に実行し、保存量を保守的に制限して密度・圧力の全流体領域L1を比較します。参照の再計算は通常の公開ZIP追試には含めず、保存データ・ソース・契約・実行記録を同梱します。 最初の参照Ny160は事前固定の120秒上限で停止した記録を保持し、診断文字列の不要なメモリ割当てだけを除く参照改訂を、主計算の初回実行前に再固定しました。入力・演算・CFL・判定値は変更していません。 24検査と全3計算・45判定が-W errorで合格。主計算の密度L1は.14754/.12878/.10265、圧力L1は.19373/.16015/.12242、密度の最後の2格子の傾きは.327。参照80/160増分は.02636/.03063で、最細主計算差の約.257/.250。全4成分の境界収支の最大相対残差は2.99e-13、全壁の積分質量・エネルギー流束は0でした。主計算3格子は元のMacで約46秒、性能改訂後の参照80/160は約8/65秒です。
- [Mach 3前向きステップ：独立C++有限格子数値参照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-forward-step-ja>)
  relation: same-problem
  reference_kind: numerical-reference

  有限格子の数値参照 γ=1.4の2次元Euler流れ。[0,3]×[0,1]のうちx≥.6,y<.2は固体とし、初期・入口の(ρ,u,v,p)=(1.4,3,0,1)、上下と段差は滑り壁、右端はゼロ勾配、T=4です。参照は独立したC++17実装のprimitive MUSCL（一般化minmod θ1.5）/Davis HLL/HeunをCFL=.3、240×80・480×160で新規実行しました。境界に接する法線方向の傾きはゼロにし、再構築の傾き再調整はセル平均を変えません。Python主計算は区分定数HLL/Heunで、流束族・時間積分式は共有しますが実装と空間再構築は別です。角のエントロピー/エンタルピー補正、状態floor、刻み再試行はありません。角の数値エントロピー層が下流へ移流され得る無補正条件であり、補正付き原著PPM像の再現とは区別します。固体を除いた保存量を保守的に制限してから圧力を算出し、参照格子差・保存収支・局所診断を残します。有限格子の数値参照であり、厳密2次元解、誤差上界、細いすべり線や巻き上がりの収束証明ではありません。 新しく独立実行したC++17のMUSCL/HLL/Heun参照を保存量制限で比較します。同じHLL族・Heunと角無補正条件を共有する有限格子数値参照であり、全場の厳密解や誤差上界ではありません。

## コード・検証

- [Mach 3前向きステップ：壁面収支と多格子検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/forward-step-m3/?lang=ja>)
  availability: run

  実際の2次元Euler有限体積計算を60×20・120×40・240×80でT=4まで行い、別実装のMUSCL有限格子参照と比較します。段差の垂直面・上面を含む実際の数値流束から4保存量の収支を評価し、角のエントロピー補正を加えない変種として図とコードを公開します。
