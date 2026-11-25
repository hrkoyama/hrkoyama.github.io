# 生物反応拡散の2次元・境界検証

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-biology-space-controls/

この章に登録された手法・問題・実行例の関連資料です。 Fisherの特殊速度前線、2次元Schnakenbergの境界別過渡、外力付きKeller–Segelのセル平均・流束を独立参照と比べます。

## 手法

- [SSPRK(3,3)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk33/?lang=ja>)

  2次中心差分とSSPRK3で計算し、厳密Dirichlet値を各段の時刻で与えます。時間誤差は同じ95未知数の半離散ODE参照と比較します。
- [Dormand–Prince RK45](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rk45/?lang=ja>)

  2次中心差分とSSPRK3で計算し、厳密Dirichlet値を各段の時刻で与えます。時間誤差は同じ95未知数の半離散ODE参照と比較します。
- [Crank–Nicolson法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/crank-nicolson/?lang=ja>)

  セル平均のCN拡散と局所陰的中点反応をStrang分割します。独立参照は正規直交sin/cos Galerkin、K12/18,Q96/192と2許容誤差の4列を全初期値で残します。 元のDirichlet K12/18参照は初回の相対資格基準を満たさなかったため、失敗を残し、D境界だけK24/32・Q128/192の4参照を追加します。
- [Strang分割](<https://hrkoyama.github.io/numerical-methods-atlas/methods/strang-splitting/?lang=ja>)

  セル平均のCN拡散と局所陰的中点反応をStrang分割します。独立参照は正規直交sin/cos Galerkin、K12/18,Q96/192と2許容誤差の4列を全初期値で残します。 元のDirichlet K12/18参照は初回の相対資格基準を満たさなかったため、失敗を残し、D境界だけK24/32・Q128/192の4参照を追加します。
- [Dormand–Prince RK45](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rk45/?lang=ja>)

  セル平均のCN拡散と局所陰的中点反応をStrang分割します。独立参照は正規直交sin/cos Galerkin、K12/18,Q96/192と2許容誤差の4列を全初期値で残します。 元のDirichlet K12/18参照は初回の相対資格基準を満たさなかったため、失敗を残し、D境界だけK24/32・Q128/192の4参照を追加します。
- [SSPRK(3,3)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk33/?lang=ja>)

  セル平均の中心面流束とSSPRK3を使い、n/c/強制項を同じ段に揃えます。展開した三角多項式の積分を、別の未展開積分とスカラー面ループ参照で確認します。
- [Dormand–Prince RK45](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rk45/?lang=ja>)

  セル平均の中心面流束とSSPRK3を使い、n/c/強制項を同じ段に揃えます。展開した三角多項式の積分を、別の未展開積分とスカラー面ループ参照で確認します。
- [SSPRK(3,3)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk33/?lang=ja>)
- [Dormand–Prince RK45](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rk45/?lang=ja>)
- [Crank–Nicolson法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/crank-nicolson/?lang=ja>)
- [Strang分割](<https://hrkoyama.github.io/numerical-methods-atlas/methods/strang-splitting/?lang=ja>)

## 方程式

- [Fisher–KPP侵入前線](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-fisher-kpp-ja>)

  拡散と増殖を結ぶ侵入前線。表示は規格化した代表形で、波の速度と境界条件は解説先へ。 全モデル族の実装ではありません。今回の固定例：Fisher–KPP：特殊波速の厳密前線 D=r=1、T=1。Ablowitz–Zeppetella型の特殊波速5/√6、L=12の空間・時間系列、定数端点L=6/12/24の境界比較を固定します。
- [Schnakenberg反応拡散](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-schnakenberg-ja>)

  自己触媒反応の空間拡張。反応平衡と分散関係から模様の発生を検証するための数理モデルです。 限定した実行例：a=0.1,b=0.9、拡散係数0.01/1、長さ2πの1次元周期Schnakenberg系。旧線形発現例を保持し、固定した反射対称の有限振幅初期値の非線形発展と成長後パターンを独立Fourier–Galerkin/Radau参照および空間・時間細分化で比較します。この旧1次元例だけから一般の模様選択、生物実験への較正、流体連成へ広げません。 全モデル族の実装ではありません。今回の固定例：Schnakenberg：2D境界と初期モード [0,2π]²、T=2、a=0.1,b=0.9,Du=0.01,Dv=1。平衡(1,0.9)のまわりで3初期値と12/24/48セル、一定の非周期境界を使います。
- [Keller–Segel走化性](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-keller-segel-ja>)

  細胞密度が化学物質の勾配に応答する2場の代表的な縮約系。次元・境界・化学場の動態が重要です。 全モデル族の実装ではありません。今回の固定例：Keller–Segel：連成流束の製造解 単位正方形、T=0.25。n=1+0.1e⁻ᵗcosπx cosπy、c=1+0.05e⁻²ᵗcosπx cos2πyに合う強制項と接線方向の発散ゼロ移流を与えます。
- [外力・移流付きKeller–Segel製造問題](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#forced-keller-segel-model-ja>)

  著者作成の強制2場モデルです。原著の全生物モデル、ピーク形成、真のblow-upやその抑制を実証しません。負値をクリップして正値性を装いません。 単位正方形、T=0.25。n=1+0.1e⁻ᵗcosπx cosπy、c=1+0.05e⁻²ᵗcosπx cos2πyに合う強制項と接線方向の発散ゼロ移流を与えます。
- [外力・移流付きKeller–Segel製造問題](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#forced-keller-segel-model-ja>)

  著者作成の強制2場モデルです。原著の全生物モデル、ピーク形成、真のblow-upやその抑制を実証しません。負値をクリップして正値性を装いません。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/fisher-kpp-special-front/?lang=ja#fisher-kpp-special-front-ja-algorithm>)

  2次中心差分とSSPRK3で計算し、厳密Dirichlet値を各段の時刻で与えます。時間誤差は同じ95未知数の半離散ODE参照と比較します。
- [Fisher–KPP侵入前線](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-fisher-kpp-ja>)

  拡散と増殖を結ぶ侵入前線。表示は規格化した代表形で、波の速度と境界条件は解説先へ。 全モデル族の実装ではありません。今回の固定例：Fisher–KPP：特殊波速の厳密前線
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-2d-boundary-modes/?lang=ja#schnakenberg-2d-boundary-modes-ja-algorithm>)

  セル平均のCN拡散と局所陰的中点反応をStrang分割します。独立参照は正規直交sin/cos Galerkin、K12/18,Q96/192と2許容誤差の4列を全初期値で残します。 元のDirichlet K12/18参照は初回の相対資格基準を満たさなかったため、失敗を残し、D境界だけK24/32・Q128/192の4参照を追加します。
- [Schnakenberg反応拡散](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-schnakenberg-ja>)

  自己触媒反応の空間拡張。反応平衡と分散関係から模様の発生を検証するための数理モデルです。 限定した実行例：a=0.1,b=0.9、拡散係数0.01/1、長さ2πの1次元周期Schnakenberg系。旧線形発現例を保持し、固定した反射対称の有限振幅初期値の非線形発展と成長後パターンを独立Fourier–Galerkin/Radau参照および空間・時間細分化で比較します。この旧1次元例だけから一般の模様選択、生物実験への較正、流体連成へ広げません。 全モデル族の実装ではありません。今回の固定例：Schnakenberg：2D境界と初期モード
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/keller-segel-forced-flux/?lang=ja#keller-segel-forced-flux-ja-algorithm>)

  セル平均の中心面流束とSSPRK3を使い、n/c/強制項を同じ段に揃えます。展開した三角多項式の積分を、別の未展開積分とスカラー面ループ参照で確認します。
- [Keller–Segel走化性](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-keller-segel-ja>)

  細胞密度が化学物質の勾配に応答する2場の代表的な縮約系。次元・境界・化学場の動態が重要です。 全モデル族の実装ではありません。今回の固定例：Keller–Segel：連成流束の製造解

## 問題の図

- [Fisher–KPP：特殊波速の厳密前線](<https://hrkoyama.github.io/numerical-methods-atlas/problems/fisher-kpp-special-front/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/fisher-kpp-special-front.png
- [Schnakenberg：2D境界と初期モード](<https://hrkoyama.github.io/numerical-methods-atlas/problems/schnakenberg-2d-boundary-modes/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/schnakenberg-2d-boundary-modes.png
- [Keller–Segel：連成流束の製造解](<https://hrkoyama.github.io/numerical-methods-atlas/problems/keller-segel-forced-flux/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/keller-segel-forced-flux.png
- [Fisher–KPP：特殊波速の厳密前線](<https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/fisher-kpp-special-front.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/fisher-kpp-special-front.png
- [Schnakenberg：2D境界と初期モード](<https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/schnakenberg-2d-boundary-modes.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/schnakenberg-2d-boundary-modes.png
- [Keller–Segel：連成流束の製造解](<https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/keller-segel-forced-flux.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/keller-segel-forced-flux.png

## 厳密解・参照解

- [Fisher–KPP：特殊波速の厳密前線：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/fisher-kpp-special-front/?lang=ja#references-ja>)

  厳密波形と1/4等値線、同一格子の時間収束、全域と中央領域の境界誤差を別保存します。実数算術の離散障壁と、実測した浮動小数点の余裕を区別します。
- [Fisher–KPP：特殊波速の厳密前線](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-fisher-kpp-special-front-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 D=r=1、T=1、特殊速度5/√6を固定。L=12で空間・時間系列を調べ、L=6/12/24で定数端点の境界系列を比較します。無次元で拡散係数と反応率は1。厳密前線の境界値と定数境界を区別し、有限領域の影響を残します。 特殊前線を一般の最小速度2の前線と同一視しません。急減衰初期値からの速度選択、長時間伝播、機械誤差込みの厳密障壁証明は対象外です。
- [Schnakenberg：2D境界と初期モード：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/schnakenberg-2d-boundary-modes/?lang=ja#references-ja>)

  線形モードの連続・離散記号、角の面所有、平衡、物質収支を照合。K/Q/時間許容差感度を別に測り、参照が資格条件を満たさなければ精度・次数を未確定にします。 精度目標には、新しい細参照が同じ絶対・相対基準に合格した場合だけその参照を用います。旧参照の不合格を合格へ読み替えません。
- [Schnakenberg：2D境界と初期モード](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-schnakenberg-2d-boundary-modes-ja>)
  relation: same-problem
  reference_kind: numerical-reference

  有限格子の数値参照 [0,2π]²、T=2、a=0.1、b=0.9、Du=0.01、Dv=1。(1,0.9)からの3摂動、12/24/48セルと固定非周期境界を比較します。Neumannの単一・混合モードと、平衡Dirichlet境界の単一モードを区別します。 短時間の小振幅・固定初期値です。一般的な模様選択、成長後の成熟パターン、原著図の再現は主張しません。有限の参照差を連続体誤差の厳密上界と呼びません。
- [Keller–Segel：連成流束の製造解：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/keller-segel-forced-flux/?lang=ja#references-ja>)

  36点の源項、96セル状態ベクトル、符号・欠落連成・古い段・面重複の負例を検査。空間・同一MOL時間・正値性・実際の段収支を分けて保存します。
- [Keller–Segel：連成流束の製造解](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-keller-segel-forced-flux-ja>)
  relation: same-problem
  reference_kind: manufactured

  製造解 単位正方形でT=0.25まで、n=1+0.1e⁻ᵗcos(πx)cos(πy)、c=1+0.05e⁻²ᵗcos(πx)cos(2πy)に対応する外力を製造し、発散零で境界に接する移流を用います。無次元の係数と外力をinputs.jsonに固定。内面・角の所有を明示して製造外力と境界流束を扱います。 著者作成の強制2場モデルです。原著の全生物モデル、ピーク形成、真のblow-upやその抑制を実証しません。負値をクリップして正値性を装いません。
- [Fisher–KPP：特殊波速の厳密前線](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-fisher-kpp-special-front-ja>)
  reference_kind: analytic

  解析解 D=r=1、T=1、特殊速度5/√6を固定。L=12で空間・時間系列を調べ、L=6/12/24で定数端点の境界系列を比較します。無次元で拡散係数と反応率は1。厳密前線の境界値と定数境界を区別し、有限領域の影響を残します。
- [Schnakenberg：2D境界と初期モード](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-schnakenberg-2d-boundary-modes-ja>)
  reference_kind: numerical-reference

  有限格子の数値参照 [0,2π]²、T=2、a=0.1、b=0.9、Du=0.01、Dv=1。(1,0.9)からの3摂動、12/24/48セルと固定非周期境界を比較します。Neumannの単一・混合モードと、平衡Dirichlet境界の単一モードを区別します。
- [Keller–Segel：連成流束の製造解](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-keller-segel-forced-flux-ja>)
  reference_kind: manufactured

  製造解 単位正方形でT=0.25まで、n=1+0.1e⁻ᵗcos(πx)cos(πy)、c=1+0.05e⁻²ᵗcos(πx)cos(2πy)に対応する外力を製造し、発散零で境界に接する移流を用います。無次元の係数と外力をinputs.jsonに固定。内面・角の所有を明示して製造外力と境界流束を扱います。
- [Fisher–KPP：特殊波速の厳密前線：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/fisher-kpp-special-front/?lang=ja#fisher-kpp-special-front-ja-validation>)

  厳密波形と1/4等値線、同一格子の時間収束、全域と中央領域の境界誤差を別保存します。実数算術の離散障壁と、実測した浮動小数点の余裕を区別します。
- [Fisher–KPP：特殊波速の厳密前線](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-fisher-kpp-special-front-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 D=r=1、T=1、特殊速度5/√6を固定。L=12で空間・時間系列を調べ、L=6/12/24で定数端点の境界系列を比較します。無次元で拡散係数と反応率は1。厳密前線の境界値と定数境界を区別し、有限領域の影響を残します。 特殊前線を一般の最小速度2の前線と同一視しません。急減衰初期値からの速度選択、長時間伝播、機械誤差込みの厳密障壁証明は対象外です。
- [Schnakenberg：2D境界と初期モード：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-2d-boundary-modes/?lang=ja#schnakenberg-2d-boundary-modes-ja-validation>)

  線形モードの連続・離散記号、角の面所有、平衡、物質収支を照合。K/Q/時間許容差感度を別に測り、参照が資格条件を満たさなければ精度・次数を未確定にします。 精度目標には、新しい細参照が同じ絶対・相対基準に合格した場合だけその参照を用います。旧参照の不合格を合格へ読み替えません。
- [Schnakenberg：2D境界と初期モード](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-schnakenberg-2d-boundary-modes-ja>)
  relation: same-problem
  reference_kind: numerical-reference

  有限格子の数値参照 [0,2π]²、T=2、a=0.1、b=0.9、Du=0.01、Dv=1。(1,0.9)からの3摂動、12/24/48セルと固定非周期境界を比較します。Neumannの単一・混合モードと、平衡Dirichlet境界の単一モードを区別します。 短時間の小振幅・固定初期値です。一般的な模様選択、成長後の成熟パターン、原著図の再現は主張しません。有限の参照差を連続体誤差の厳密上界と呼びません。
- [Keller–Segel：連成流束の製造解：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/keller-segel-forced-flux/?lang=ja#keller-segel-forced-flux-ja-validation>)

  36点の源項、96セル状態ベクトル、符号・欠落連成・古い段・面重複の負例を検査。空間・同一MOL時間・正値性・実際の段収支を分けて保存します。
- [Keller–Segel：連成流束の製造解](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-keller-segel-forced-flux-ja>)
  relation: same-problem
  reference_kind: manufactured

  製造解 単位正方形でT=0.25まで、n=1+0.1e⁻ᵗcos(πx)cos(πy)、c=1+0.05e⁻²ᵗcos(πx)cos(2πy)に対応する外力を製造し、発散零で境界に接する移流を用います。無次元の係数と外力をinputs.jsonに固定。内面・角の所有を明示して製造外力と境界流束を扱います。 著者作成の強制2場モデルです。原著の全生物モデル、ピーク形成、真のblow-upやその抑制を実証しません。負値をクリップして正値性を装いません。

## コード・検証

- [Fisher–KPP：特殊波速の厳密前線](<https://hrkoyama.github.io/numerical-methods-atlas/validation/fisher-kpp-special-front/?lang=ja>)
  availability: run

  波形・位置・格子誤差・時間誤差・有限領域の影響を分けます。
- [Schnakenberg：2D境界と初期モード](<https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-2d-boundary-modes/?lang=ja>)
  availability: run

  2つのNeumann摂動とDirichlet摂動を独立な非線形Galerkin参照と比較します。
- [Keller–Segel：連成流束の製造解](<https://hrkoyama.github.io/numerical-methods-atlas/validation/keller-segel-forced-flux/?lang=ja>)
  availability: run

  滑らかな2D厳密場で、交差流束・段時刻・収支を検証します。
