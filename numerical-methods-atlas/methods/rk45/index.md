# Dormand–Prince RK45 / Dormand–Prince RK45

Status: educational-example

Explicit time integration combines an embedded 5(4) error estimator, adaptive steps, a quartic continuous extension and directed events.

埋込み5(4)誤差推定と刻み制御、4次の連続拡張、向き付きイベントを組み合わせる陽的時間積分です。

No general guarantee is provided for stiff systems, tangential roots, multiple crossings per step or reset systems. Local tolerances are not global error bounds.

Other names: RK45, Dormand-Prince 5(4), DOPRI5, 埋込みRunge–Kutta

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/runge-kutta/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/runge-kutta/



- Reference: https://github.com/scipy/scipy/blob/v1.14.1/scipy/integrate/_ivp/rk.py — Read C, A, B, E, P, stage evaluation, accepted/rejected FSAL updates and quartic evaluation. The original Dormand–Prince 1980 and Shampine 1986 papers remain unread beyond bibliography. The adapted coefficient BSD notice is retained.

## Small fixed-input validation supplements

Additional fixed examples: RK45: embedded errors, dense output and events. See each release for assumptions and checked scope. There is no general guarantee for tangential roots, multiple crossings within a step or systems with resets. Initial-zero and ownership controls are limited component tests; local tolerances and global accuracy remain distinct.

追加固定例：RK45の埋込み推定・補間・イベント。条件と検証範囲は各配布版で確認してください。 接触根・1刻み内の多重交差・reset付き系の一般性は保証しません。初期零/所有権/resetは限定成分対照で、局所許容誤差と大域精度を同一視しません。

- RK45: embedded errors, dense output and events: https://hrkoyama.github.io/numerical-methods-atlas/validation/rk45-dense-events/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/atlas-ode-adaptivity-2026-11-24-r2.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/result.json

- Hodgkin–Huxley: clamps, rest and firing: https://hrkoyama.github.io/numerical-methods-atlas/validation/hodgkin-huxley-controls/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/atlas-biology-ode-controls-2026-11-25.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/results/result.json

- Fisher–KPP: a special-speed exact front: https://hrkoyama.github.io/numerical-methods-atlas/validation/fisher-kpp-special-front/
- Schnakenberg:2D boundaries and initial modes: https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-2d-boundary-modes/
- Keller–Segel: a manufactured coupled-flux solution: https://hrkoyama.github.io/numerical-methods-atlas/validation/keller-segel-forced-flux/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/atlas-biology-space-controls-2026-11-25.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/result.json

Common execution records: [{"id": "rk45-dense-events", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/rk45-dense-events/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/rk45-dense-events/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "hodgkin-huxley-controls", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/hodgkin-huxley-controls/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/hodgkin-huxley-controls/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "fisher-kpp-special-front", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/fisher-kpp-special-front/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/fisher-kpp-special-front/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "schnakenberg-2d-boundary-modes", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-2d-boundary-modes/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-2d-boundary-modes/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "keller-segel-forced-flux", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/keller-segel-forced-flux/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/keller-segel-forced-flux/?lang=en"}, "kind": "dedicated-supplement"}]

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/rk45/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [有限次元の線形発展系](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#linear-evolution-system-ja) (`linear-evolution-system`; rk45-dense-events)
- [Hodgkin–Huxley膜動態](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-hodgkin-huxley-ja) (`bio-hodgkin-huxley`; hodgkin-huxley-controls)
- [Fisher–KPP侵入前線](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-fisher-kpp-ja) (`bio-fisher-kpp`; fisher-kpp-special-front)
- [Schnakenberg反応拡散](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-schnakenberg-ja) (`bio-schnakenberg`; schnakenberg-2d-boundary-modes)
- [Keller–Segel走化性](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-keller-segel-ja) (`bio-keller-segel`; keller-segel-forced-flux)
- [外力・移流付きKeller–Segel製造問題](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#forced-keller-segel-model-ja) (`forced-keller-segel-model`; keller-segel-forced-flux)

#### 問題の図 (`method-problems-ja`)

##### [RK45の埋込み推定・補間・イベント](https://hrkoyama.github.io/numerical-methods-atlas/problems/rk45-dense-events/?lang=ja) (`rk45-dense-events`)

![減衰回転の解析解を使い、受理/棄却・FSAL・区間内補間・向き付き交差時刻を分けて検査します。 保存済みの数値場と参照を用いた図です。 図の軌道・状態・時刻・反復の軸は、物理空間の次元を表しません。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/rk45-dense-events-preview.png)

実Dormand–Prince5(4)・quartic連続拡張・受理状態が所有するFSAL・保存補間上の符号区間二分法。拒否端点を昇格しません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/rk45-dense-events/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/rk45-dense-events/?lang=ja#code-ja)

- [RK45の埋込み推定・補間・イベント](https://hrkoyama.github.io/numerical-methods-atlas/validation/rk45-dense-events/?lang=ja) (`rk45-dense-events`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/atlas-ode-adaptivity-2026-11-24-r2.zip)

減衰回転の解析解を使い、受理/棄却・FSAL・区間内補間・向き付き交差時刻を分けて検査します。

##### [Hodgkin–Huxley：電位固定・静止平衡・発火](https://hrkoyama.github.io/numerical-methods-atlas/problems/hodgkin-huxley-controls/?lang=ja) (`hodgkin-huxley-controls`)

![固定電位の解析ゲート解と、区分電流下の4状態系を照合します。 1細胞膜の教育例です。元論文の電位規約、TABLE/cnexp実装、ケーブル伝播や生体実測の再現とは呼びません。区間内に括れない発火は捏造せず、静止根の一意性・区間Hurwitz安定性は主張しません。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/results/hodgkin-huxley-controls.png)

古典RK4を用い、電流の切り替わりでは全段の片側値を区間に帰属させます。ゲートの可除特異点、Decimal静止根、独立なDP5(4)/Cash–Karp参照を別に照合します。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/hodgkin-huxley-controls/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/hodgkin-huxley-controls/?lang=ja#code-ja)

- [Hodgkin–Huxley：電位固定・静止平衡・発火](https://hrkoyama.github.io/numerical-methods-atlas/validation/hodgkin-huxley-controls/?lang=ja) (`hodgkin-huxley-controls`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/atlas-biology-ode-controls-2026-11-25.zip)

固定電位の解析ゲート解と、区分電流下の4状態系を照合します。

##### [Fisher–KPP：特殊波速の厳密前線](https://hrkoyama.github.io/numerical-methods-atlas/problems/fisher-kpp-special-front/?lang=ja) (`fisher-kpp-special-front`)

![波形・位置・格子誤差・時間誤差・有限領域の影響を分けます。 特殊前線を一般の最小速度2の前線と同一視しません。急減衰初期値からの速度選択、長時間伝播、機械誤差込みの厳密障壁証明は対象外です。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/fisher-kpp-special-front.png)

2次中心差分とSSPRK3で計算し、厳密Dirichlet値を各段の時刻で与えます。時間誤差は同じ95未知数の半離散ODE参照と比較します。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/fisher-kpp-special-front/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/fisher-kpp-special-front/?lang=ja#code-ja)

- [Fisher–KPP：特殊波速の厳密前線](https://hrkoyama.github.io/numerical-methods-atlas/validation/fisher-kpp-special-front/?lang=ja) (`fisher-kpp-special-front`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/atlas-biology-space-controls-2026-11-25.zip)

波形・位置・格子誤差・時間誤差・有限領域の影響を分けます。

##### [Schnakenberg：2D境界と初期モード](https://hrkoyama.github.io/numerical-methods-atlas/problems/schnakenberg-2d-boundary-modes/?lang=ja) (`schnakenberg-2d-boundary-modes`)

![2つのNeumann摂動とDirichlet摂動を独立な非線形Galerkin参照と比較します。 短時間の小振幅・固定初期値です。一般的な模様選択、成長後の成熟パターン、原著図の再現は主張しません。有限の参照差を連続体誤差の厳密上界と呼びません。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/schnakenberg-2d-boundary-modes.png)

セル平均のCN拡散と局所陰的中点反応をStrang分割します。独立参照は正規直交sin/cos Galerkin、K12/18,Q96/192と2許容誤差の4列を全初期値で残します。 元のDirichlet K12/18参照は初回の相対資格基準を満たさなかったため、失敗を残し、D境界だけK24/32・Q128/192の4参照を追加します。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/schnakenberg-2d-boundary-modes/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/schnakenberg-2d-boundary-modes/?lang=ja#code-ja)

- [Schnakenberg：2D境界と初期モード](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-2d-boundary-modes/?lang=ja) (`schnakenberg-2d-boundary-modes`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/atlas-biology-space-controls-2026-11-25.zip)

2つのNeumann摂動とDirichlet摂動を独立な非線形Galerkin参照と比較します。

##### [Keller–Segel：連成流束の製造解](https://hrkoyama.github.io/numerical-methods-atlas/problems/keller-segel-forced-flux/?lang=ja) (`keller-segel-forced-flux`)

![滑らかな2D厳密場で、交差流束・段時刻・収支を検証します。 著者作成の強制2場モデルです。原著の全生物モデル、ピーク形成、真のblow-upやその抑制を実証しません。負値をクリップして正値性を装いません。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/keller-segel-forced-flux.png)

セル平均の中心面流束とSSPRK3を使い、n/c/強制項を同じ段に揃えます。展開した三角多項式の積分を、別の未展開積分とスカラー面ループ参照で確認します。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/keller-segel-forced-flux/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/keller-segel-forced-flux/?lang=ja#code-ja)

- [Keller–Segel：連成流束の製造解](https://hrkoyama.github.io/numerical-methods-atlas/validation/keller-segel-forced-flux/?lang=ja) (`keller-segel-forced-flux`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/atlas-biology-space-controls-2026-11-25.zip)

滑らかな2D厳密場で、交差流束・段時刻・収支を検証します。


#### 厳密解・参照解 (`method-references-ja`)

##### [RK45の埋込み推定・補間・イベント](https://hrkoyama.github.io/numerical-methods-atlas/problems/rk45-dense-events/?lang=ja#references-ja) (`rk45-dense-events`)

- [RK45の埋込み推定・補間・イベント](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-rk45-dense-events-ja) (`rk45-dense-events`; 同じ問題の参照; 解析参照)

接触根・1刻み内の多重交差・reset付き系の一般性は保証しません。初期零/所有権/resetは限定成分対照で、局所許容誤差と大域精度を同一視しません。

[既存の参照図](/numerical-methods-atlas/validation/rk45-dense-events/?lang=ja#rk45-dense-events-ja-measurements)

##### [Hodgkin–Huxley：電位固定・静止平衡・発火](https://hrkoyama.github.io/numerical-methods-atlas/problems/hodgkin-huxley-controls/?lang=ja#references-ja) (`hodgkin-huxley-controls`)

- [Hodgkin–Huxley：電位固定・静止平衡・発火](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-hodgkin-huxley-controls-ja) (`hodgkin-huxley-controls`; 同じ問題の参照; 半解析参照)

1細胞膜の教育例です。元論文の電位規約、TABLE/cnexp実装、ケーブル伝播や生体実測の再現とは呼びません。区間内に括れない発火は捏造せず、静止根の一意性・区間Hurwitz安定性は主張しません。

[既存の参照図](/numerical-methods-atlas/validation/hodgkin-huxley-controls/?lang=ja#hodgkin-huxley-controls-ja-measurements)

##### [Fisher–KPP：特殊波速の厳密前線](https://hrkoyama.github.io/numerical-methods-atlas/problems/fisher-kpp-special-front/?lang=ja#references-ja) (`fisher-kpp-special-front`)

- [Fisher–KPP：特殊波速の厳密前線](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-fisher-kpp-special-front-ja) (`fisher-kpp-special-front`; 同じ問題の参照; 解析参照)

特殊前線を一般の最小速度2の前線と同一視しません。急減衰初期値からの速度選択、長時間伝播、機械誤差込みの厳密障壁証明は対象外です。

[既存の参照図](/numerical-methods-atlas/validation/fisher-kpp-special-front/?lang=ja#fisher-kpp-special-front-ja-measurements)

##### [Schnakenberg：2D境界と初期モード](https://hrkoyama.github.io/numerical-methods-atlas/problems/schnakenberg-2d-boundary-modes/?lang=ja#references-ja) (`schnakenberg-2d-boundary-modes`)

- [Schnakenberg：2D境界と初期モード](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-schnakenberg-2d-boundary-modes-ja) (`schnakenberg-2d-boundary-modes`; 同じ問題の参照; 有限格子の数値参照)

短時間の小振幅・固定初期値です。一般的な模様選択、成長後の成熟パターン、原著図の再現は主張しません。有限の参照差を連続体誤差の厳密上界と呼びません。

[既存の参照図](/numerical-methods-atlas/validation/schnakenberg-2d-boundary-modes/?lang=ja#schnakenberg-2d-boundary-modes-ja-measurements)

##### [Keller–Segel：連成流束の製造解](https://hrkoyama.github.io/numerical-methods-atlas/problems/keller-segel-forced-flux/?lang=ja#references-ja) (`keller-segel-forced-flux`)

- [Keller–Segel：連成流束の製造解](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-keller-segel-forced-flux-ja) (`keller-segel-forced-flux`; 同じ問題の参照; 製造解)

著者作成の強制2場モデルです。原著の全生物モデル、ピーク形成、真のblow-upやその抑制を実証しません。負値をクリップして正値性を装いません。

[既存の参照図](/numerical-methods-atlas/validation/keller-segel-forced-flux/?lang=ja#keller-segel-forced-flux-ja-measurements)

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/runge-kutta/)
- 保存結果: [この配布版の保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/result.json)
- 検証記録: [配布版の検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/verification.json)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

##### RK45の埋込み推定・補間・イベント (`rk45-dense-events`)

[RK45の埋込み推定・補間・イベント](https://hrkoyama.github.io/numerical-methods-atlas/problems/rk45-dense-events/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/rk45-dense-events/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/atlas-ode-adaptivity-2026-11-24-r2.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/verification.json)

減衰回転の解析解を使い、受理/棄却・FSAL・区間内補間・向き付き交差時刻を分けて検査します。

##### Hodgkin–Huxley：電位固定・静止平衡・発火 (`hodgkin-huxley-controls`)

[Hodgkin–Huxley：電位固定・静止平衡・発火](https://hrkoyama.github.io/numerical-methods-atlas/problems/hodgkin-huxley-controls/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/hodgkin-huxley-controls/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/atlas-biology-ode-controls-2026-11-25.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/verification.json)

固定電位の解析ゲート解と、区分電流下の4状態系を照合します。

##### Fisher–KPP：特殊波速の厳密前線 (`fisher-kpp-special-front`)

[Fisher–KPP：特殊波速の厳密前線](https://hrkoyama.github.io/numerical-methods-atlas/problems/fisher-kpp-special-front/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/fisher-kpp-special-front/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/atlas-biology-space-controls-2026-11-25.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/verification.json)

波形・位置・格子誤差・時間誤差・有限領域の影響を分けます。

##### Schnakenberg：2D境界と初期モード (`schnakenberg-2d-boundary-modes`)

[Schnakenberg：2D境界と初期モード](https://hrkoyama.github.io/numerical-methods-atlas/problems/schnakenberg-2d-boundary-modes/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-2d-boundary-modes/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/atlas-biology-space-controls-2026-11-25.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/verification.json)

2つのNeumann摂動とDirichlet摂動を独立な非線形Galerkin参照と比較します。

##### Keller–Segel：連成流束の製造解 (`keller-segel-forced-flux`)

[Keller–Segel：連成流束の製造解](https://hrkoyama.github.io/numerical-methods-atlas/problems/keller-segel-forced-flux/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/keller-segel-forced-flux/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/atlas-biology-space-controls-2026-11-25.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/verification.json)

滑らかな2D厳密場で、交差流束・段時刻・収支を検証します。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/atlas-ode-adaptivity-2026-11-24-r2.zip)

[配布版の検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/verification.json)

###### 関連ソース

- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/run.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/experiments.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/io_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/io_contract.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/reference_eval.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/reference_eval.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/dopri.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/dopri.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/tableau.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/tableau.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/models.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/stiff.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/stiff.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/reporting_policy.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/reporting_policy.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/boundary.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/boundary.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/boundary_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/boundary_reference.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/coefficient_exact.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/coefficient_exact.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/qualify.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/qualify.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/reference_models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/reference_models.py)
- [/code/validated-examples/2026-11-25/biology-ode-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/run.py)
- [/code/validated-examples/2026-11-25/biology-ode-controls/common.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/common.py)
- [/code/validated-examples/2026-11-25/biology-ode-controls/hh.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/hh.py)
- [/code/validated-examples/2026-11-25/biology-ode-controls/ssa.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/ssa.py)
- [/code/validated-examples/2026-11-25/biology-space-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/run.py)
- [/code/validated-examples/2026-11-25/biology-space-controls/common.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/common.py)
- [/code/validated-examples/2026-11-25/biology-space-controls/fisher.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/fisher.py)
- [/code/validated-examples/2026-11-25/biology-space-controls/schnakenberg.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/schnakenberg.py)
- [/code/validated-examples/2026-11-25/biology-space-controls/keller_segel.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/keller_segel.py)

###### 配布版のテスト

- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_boundary.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_boundary.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_contract.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_dopri.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_dopri.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_reporting.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_reporting.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_stiff.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_stiff.py)
- [/code/validated-examples/2026-11-25/biology-ode-controls/test_models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/test_models.py)
- [/code/validated-examples/2026-11-25/biology-space-controls/test_models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/test_models.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q
python run.py --input inputs.json --output output
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Finite-dimensional linear evolution systems](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#linear-evolution-system-en) (`linear-evolution-system`; rk45-dense-events)
- [Hodgkin–Huxley membrane dynamics](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-hodgkin-huxley-en) (`bio-hodgkin-huxley`; hodgkin-huxley-controls)
- [Fisher–KPP invasion front](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-fisher-kpp-en) (`bio-fisher-kpp`; fisher-kpp-special-front)
- [Schnakenberg reaction–diffusion](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-schnakenberg-en) (`bio-schnakenberg`; schnakenberg-2d-boundary-modes)
- [Keller–Segel chemotaxis](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-keller-segel-en) (`bio-keller-segel`; keller-segel-forced-flux)
- [Forced advective Keller–Segel manufactured problem](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#forced-keller-segel-model-en) (`forced-keller-segel-model`; keller-segel-forced-flux)

#### Problem figures (`method-problems-en`)

##### [RK45: embedded errors, dense output and events](https://hrkoyama.github.io/numerical-methods-atlas/problems/rk45-dense-events/?lang=en) (`rk45-dense-events`)

![Use analytic damped rotation to test acceptance, rejection, FSAL ownership, dense interpolation and directed event times separately. This preview reads saved numerical fields and references only. Axes for trajectories, states, time or iterations do not represent physical spatial dimensions.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/rk45-dense-events-preview.png)

Use actual Dormand–Prince 5(4) stages, a quartic continuous extension, an accepted-state derivative cache and bracket bisection on retained interpolants. A rejected endpoint never replaces the accepted starting derivative.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/rk45-dense-events/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/rk45-dense-events/?lang=en#code-en)

- [RK45: embedded errors, dense output and events](https://hrkoyama.github.io/numerical-methods-atlas/validation/rk45-dense-events/?lang=en) (`rk45-dense-events`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/atlas-ode-adaptivity-2026-11-24-r2.zip)

Use analytic damped rotation to test acceptance, rejection, FSAL ownership, dense interpolation and directed event times separately.

##### [Hodgkin–Huxley: clamps, rest and firing](https://hrkoyama.github.io/numerical-methods-atlas/problems/hodgkin-huxley-controls/?lang=en) (`hodgkin-huxley-controls`)

![Compare analytic clamp gates and a four-state system with segment-owned current. This educational membrane model does not reproduce the original voltage convention, TABLE/cnexp, cable propagation or measured physiology. Missing/unresolved events remain explicit; rest-root uniqueness and interval-Hurwitz stability are unclaimed.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/results/hodgkin-huxley-controls.png)

Use classicalRK4 with all stages owned by each current segment. Separately qualify removable rate singularities, a Decimal rest root and independently written DP5(4)/Cash–Karp references.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/hodgkin-huxley-controls/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/hodgkin-huxley-controls/?lang=en#code-en)

- [Hodgkin–Huxley: clamps, rest and firing](https://hrkoyama.github.io/numerical-methods-atlas/validation/hodgkin-huxley-controls/?lang=en) (`hodgkin-huxley-controls`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/atlas-biology-ode-controls-2026-11-25.zip)

Compare analytic clamp gates and a four-state system with segment-owned current.

##### [Fisher–KPP: a special-speed exact front](https://hrkoyama.github.io/numerical-methods-atlas/problems/fisher-kpp-special-front/?lang=en) (`fisher-kpp-special-front`)

![Separate profile, phase, grid, time and finite-boundary errors. The special front is distinct from the minimum linear speed2. This is not a steep-data speed-selection study, long-time propagation result or certified machine-error barrier proof.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/fisher-kpp-special-front.png)

Use centered second-order differences and SSPRK3 with exact Dirichlet values at every stage. Compare time errors to an independent reference for the same95-unknown semidiscreteODE.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/fisher-kpp-special-front/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/fisher-kpp-special-front/?lang=en#code-en)

- [Fisher–KPP: a special-speed exact front](https://hrkoyama.github.io/numerical-methods-atlas/validation/fisher-kpp-special-front/?lang=en) (`fisher-kpp-special-front`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/atlas-biology-space-controls-2026-11-25.zip)

Separate profile, phase, grid, time and finite-boundary errors.

##### [Schnakenberg:2D boundaries and initial modes](https://hrkoyama.github.io/numerical-methods-atlas/problems/schnakenberg-2d-boundary-modes/?lang=en) (`schnakenberg-2d-boundary-modes`)

![Compare two Neumann perturbations and a Dirichlet perturbation against nonlinear Galerkin references. This short small-amplitude study does not establish general pattern selection, mature patterns or reproduction of original figures. Finite reference differences are not rigorous continuum error bounds.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/schnakenberg-2d-boundary-modes.png)

Strang-split cell-averageCN diffusion and local implicit-midpoint reactions. Independent orthonormal sine/cosine Galerkin references retain four K12/18,Q96/192,tolerance rows for every initial condition. The original Dirichlet K12/18 reference failed its first relative qualification. Preserve that failure and add four D-only K24/32,Q128/192 reference actions.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/schnakenberg-2d-boundary-modes/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/schnakenberg-2d-boundary-modes/?lang=en#code-en)

- [Schnakenberg:2D boundaries and initial modes](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-2d-boundary-modes/?lang=en) (`schnakenberg-2d-boundary-modes`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/atlas-biology-space-controls-2026-11-25.zip)

Compare two Neumann perturbations and a Dirichlet perturbation against nonlinear Galerkin references.

##### [Keller–Segel: a manufactured coupled-flux solution](https://hrkoyama.github.io/numerical-methods-atlas/problems/keller-segel-forced-flux/?lang=en) (`keller-segel-forced-flux`)

![Use smooth exact2D fields to test cross fluxes, stage timing and mass ledgers. This authored forced two-field model does not reproduce the full original biological model or demonstrate aggregation, true blow-up or suppression. No clipping is used to manufacture positivity.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/keller-segel-forced-flux.png)

Use cell-average centered face fluxes and SSPRK3 with n,c and forcing at the same stage. Check expanded trigonometric integrals against independent unexpanded integrals and scalar face-loop references.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/keller-segel-forced-flux/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/keller-segel-forced-flux/?lang=en#code-en)

- [Keller–Segel: a manufactured coupled-flux solution](https://hrkoyama.github.io/numerical-methods-atlas/validation/keller-segel-forced-flux/?lang=en) (`keller-segel-forced-flux`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/atlas-biology-space-controls-2026-11-25.zip)

Use smooth exact2D fields to test cross fluxes, stage timing and mass ledgers.


#### Exact / reference solutions (`method-references-en`)

##### [RK45: embedded errors, dense output and events](https://hrkoyama.github.io/numerical-methods-atlas/problems/rk45-dense-events/?lang=en#references-en) (`rk45-dense-events`)

- [RK45: embedded errors, dense output and events](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-rk45-dense-events-en) (`rk45-dense-events`; Same-problem reference; Analytic reference)

There is no general guarantee for tangential roots, multiple crossings within a step or systems with resets. Initial-zero and ownership controls are limited component tests; local tolerances and global accuracy remain distinct.

[Existing reference profile](/numerical-methods-atlas/validation/rk45-dense-events/?lang=en#rk45-dense-events-en-measurements)

##### [Hodgkin–Huxley: clamps, rest and firing](https://hrkoyama.github.io/numerical-methods-atlas/problems/hodgkin-huxley-controls/?lang=en#references-en) (`hodgkin-huxley-controls`)

- [Hodgkin–Huxley: clamps, rest and firing](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-hodgkin-huxley-controls-en) (`hodgkin-huxley-controls`; Same-problem reference; Semi-analytic reference)

This educational membrane model does not reproduce the original voltage convention, TABLE/cnexp, cable propagation or measured physiology. Missing/unresolved events remain explicit; rest-root uniqueness and interval-Hurwitz stability are unclaimed.

[Existing reference profile](/numerical-methods-atlas/validation/hodgkin-huxley-controls/?lang=en#hodgkin-huxley-controls-en-measurements)

##### [Fisher–KPP: a special-speed exact front](https://hrkoyama.github.io/numerical-methods-atlas/problems/fisher-kpp-special-front/?lang=en#references-en) (`fisher-kpp-special-front`)

- [Fisher–KPP: a special-speed exact front](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-fisher-kpp-special-front-en) (`fisher-kpp-special-front`; Same-problem reference; Analytic reference)

The special front is distinct from the minimum linear speed2. This is not a steep-data speed-selection study, long-time propagation result or certified machine-error barrier proof.

[Existing reference profile](/numerical-methods-atlas/validation/fisher-kpp-special-front/?lang=en#fisher-kpp-special-front-en-measurements)

##### [Schnakenberg:2D boundaries and initial modes](https://hrkoyama.github.io/numerical-methods-atlas/problems/schnakenberg-2d-boundary-modes/?lang=en#references-en) (`schnakenberg-2d-boundary-modes`)

- [Schnakenberg:2D boundaries and initial modes](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-schnakenberg-2d-boundary-modes-en) (`schnakenberg-2d-boundary-modes`; Same-problem reference; Finite-grid numerical reference)

This short small-amplitude study does not establish general pattern selection, mature patterns or reproduction of original figures. Finite reference differences are not rigorous continuum error bounds.

[Existing reference profile](/numerical-methods-atlas/validation/schnakenberg-2d-boundary-modes/?lang=en#schnakenberg-2d-boundary-modes-en-measurements)

##### [Keller–Segel: a manufactured coupled-flux solution](https://hrkoyama.github.io/numerical-methods-atlas/problems/keller-segel-forced-flux/?lang=en#references-en) (`keller-segel-forced-flux`)

- [Keller–Segel: a manufactured coupled-flux solution](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-keller-segel-forced-flux-en) (`keller-segel-forced-flux`; Same-problem reference; Manufactured solution)

This authored forced two-field model does not reproduce the full original biological model or demonstrate aggregation, true blow-up or suppression. No clipping is used to manufacture positivity.

[Existing reference profile](/numerical-methods-atlas/validation/keller-segel-forced-flux/?lang=en#keller-segel-forced-flux-en-measurements)

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/runge-kutta/)
- Saved result: [Saved results from this edition](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/result.json)
- Verification receipt: [Edition verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/verification.json)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

##### RK45: embedded errors, dense output and events (`rk45-dense-events`)

[RK45: embedded errors, dense output and events](https://hrkoyama.github.io/numerical-methods-atlas/problems/rk45-dense-events/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/rk45-dense-events/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/atlas-ode-adaptivity-2026-11-24-r2.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/verification.json)

Use analytic damped rotation to test acceptance, rejection, FSAL ownership, dense interpolation and directed event times separately.

##### Hodgkin–Huxley: clamps, rest and firing (`hodgkin-huxley-controls`)

[Hodgkin–Huxley: clamps, rest and firing](https://hrkoyama.github.io/numerical-methods-atlas/problems/hodgkin-huxley-controls/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/hodgkin-huxley-controls/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/atlas-biology-ode-controls-2026-11-25.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/verification.json)

Compare analytic clamp gates and a four-state system with segment-owned current.

##### Fisher–KPP: a special-speed exact front (`fisher-kpp-special-front`)

[Fisher–KPP: a special-speed exact front](https://hrkoyama.github.io/numerical-methods-atlas/problems/fisher-kpp-special-front/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/fisher-kpp-special-front/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/atlas-biology-space-controls-2026-11-25.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/verification.json)

Separate profile, phase, grid, time and finite-boundary errors.

##### Schnakenberg:2D boundaries and initial modes (`schnakenberg-2d-boundary-modes`)

[Schnakenberg:2D boundaries and initial modes](https://hrkoyama.github.io/numerical-methods-atlas/problems/schnakenberg-2d-boundary-modes/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-2d-boundary-modes/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/atlas-biology-space-controls-2026-11-25.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/verification.json)

Compare two Neumann perturbations and a Dirichlet perturbation against nonlinear Galerkin references.

##### Keller–Segel: a manufactured coupled-flux solution (`keller-segel-forced-flux`)

[Keller–Segel: a manufactured coupled-flux solution](https://hrkoyama.github.io/numerical-methods-atlas/problems/keller-segel-forced-flux/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/keller-segel-forced-flux/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/atlas-biology-space-controls-2026-11-25.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/verification.json)

Use smooth exact2D fields to test cross fluxes, stage timing and mass ledgers.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[Related code edition / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/atlas-ode-adaptivity-2026-11-24-r2.zip)

[Edition verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/verification.json)

###### Related source

- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/run.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/experiments.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/io_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/io_contract.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/reference_eval.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/reference_eval.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/dopri.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/dopri.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/tableau.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/tableau.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/models.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/stiff.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/stiff.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/reporting_policy.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/reporting_policy.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/boundary.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/boundary.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/boundary_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/boundary_reference.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/coefficient_exact.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/coefficient_exact.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/qualify.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/qualify.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/reference_models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/reference_models.py)
- [/code/validated-examples/2026-11-25/biology-ode-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/run.py)
- [/code/validated-examples/2026-11-25/biology-ode-controls/common.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/common.py)
- [/code/validated-examples/2026-11-25/biology-ode-controls/hh.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/hh.py)
- [/code/validated-examples/2026-11-25/biology-ode-controls/ssa.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/ssa.py)
- [/code/validated-examples/2026-11-25/biology-space-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/run.py)
- [/code/validated-examples/2026-11-25/biology-space-controls/common.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/common.py)
- [/code/validated-examples/2026-11-25/biology-space-controls/fisher.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/fisher.py)
- [/code/validated-examples/2026-11-25/biology-space-controls/schnakenberg.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/schnakenberg.py)
- [/code/validated-examples/2026-11-25/biology-space-controls/keller_segel.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/keller_segel.py)

###### Package tests

- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_boundary.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_boundary.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_contract.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_dopri.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_dopri.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_reporting.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_reporting.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_stiff.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_stiff.py)
- [/code/validated-examples/2026-11-25/biology-ode-controls/test_models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/test_models.py)
- [/code/validated-examples/2026-11-25/biology-space-controls/test_models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/test_models.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q
python run.py --input inputs.json --output output
```
