# 生物モデル方程式と数値検証

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/biological-models/

この章に登録された手法・問題・実行例の関連資料です。

## 手法

- [古典的RK4](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=ja>)

  この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。
- [古典的RK4](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=ja>)

  この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。
- [古典的RK4](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=ja>)

## 方程式

- [ロジスティック個体群増殖](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-logistic-ja>)

  収容力Kを持つ密度依存の連続時間増殖モデル。離散ロジスティック写像とは区別します。 限定した実行例：無次元の単一個体群。RK4を全出力時刻で解析解と比較し、非負性と刻み幅の収束を確認。反応拡散・複数種は対象外。 この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。
- [SIR・SEIR区画モデル](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-sir-ja>)

  閉じた一様混合集団の規格化SIR系。SEIRは曝露区画を追加します。人数と割合ではβの定義が異なります。 限定した実行例：閉鎖・均質な人口割合SIR。RK4と別実装のSciPy DOP853を比較。人口保存・非負性・時間収束を確認。SEIR・空間伝播・実データ較正は対象外。 この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。
- [ロジスティック個体群増殖](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-logistic-ja>)

  収容力Kを持つ密度依存の連続時間増殖モデル。離散ロジスティック写像とは区別します。 限定した実行例：無次元の単一個体群。RK4を全出力時刻で解析解と比較し、非負性と刻み幅の収束を確認。反応拡散・複数種は対象外。
- [Michaelis–Mentenと完全酵素反応系](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-enzyme-ja>)

  酵素・基質・複合体の反応と飽和速度則。完全反応系、迅速平衡近似、準定常近似の違いは解説先へ。 限定した実行例：2つの小εと固定反応定数だけの教育例です。εは尺度比であり、その値だけを厳密なQSSA誤差上界とはしません。θ≥0.02を初期層終了の証明とは呼ばず、生体内の反応・観測値へ外挿しません。
- [Lotka–Volterra捕食・被食](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-lotka-volterra-ja>)

  捕食・被食の結合ODE。位相平面と長時間積分を考えるためのモデルです。 限定した実行例：1初期値・有限時間の固定比較です。連続系の閉軌道を引き込み極限周期とは呼びません。RK4の厳密な不変量保存、任意刻みでの正値性、長時間の構造保存は保証しません。
- [McKendrick年齢構造個体群](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-age-structure-ja>)

  年齢aに沿う輸送と死亡、新生個体の非局所な更新境界を持つモデルです。 文献解説のみ。
- [SIR・SEIR区画モデル](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-sir-ja>)

  閉じた一様混合集団の規格化SIR系。SEIRは曝露区画を追加します。人数と割合ではβの定義が異なります。 限定した実行例：閉鎖・均質な人口割合SIR。RK4と別実装のSciPy DOP853を比較。人口保存・非負性・時間収束を確認。SEIR・空間伝播・実データ較正は対象外。
- [Fisher–KPP侵入前線](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-fisher-kpp-ja>)

  拡散と増殖を結ぶ侵入前線。表示は規格化した代表形で、波の速度と境界条件は解説先へ。 全モデル族の実装ではありません。今回の固定例：Fisher–KPP：特殊波速の厳密前線
- [Monod増殖とケモスタット](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-monod-ja>)

  基質S、菌体X、収率Y、希釈率dの代表形。d=0の閉鎖バッチとケモスタットを区別します。 文献解説のみ。
- [Hodgkin–Huxley膜動態](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-hodgkin-huxley-ja>)

  電位とゲート変数z=m,h,nの膜モデル。元のイカ軸索モデルと、人心筋や空間ケーブルへの拡張を区別します。 全モデル族の実装ではありません。今回の固定例：Hodgkin–Huxley：電位固定・静止平衡・発火
- [Turing反応拡散の枠組み](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-turing-ja>)

  2成分反応拡散の枠組み。f・gは個別に指定する必要があり、模様の画像だけでTuring機構とは判定できません。 限定した実行例：a=0.1,b=0.9、拡散係数0.01/1、長さ2πの1次元周期Schnakenberg系。旧線形発現例を保持し、固定した反射対称の有限振幅初期値の非線形発展と成長後パターンを独立Fourier–Galerkin/Radau参照および空間・時間細分化で比較します。一般の模様選択、2次元、生物実験への較正、流体連成には広げません。
- [FitzHugh–Nagumoの興奮と回復](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-fitzhugh-nagumo-ja>)

  高速の興奮と低速の回復を結ぶ規格化した代表形。係数・符号・空間拡張には複数の規約があります。 限定した実行例：公開実行例はD=0の空間なしの縮約ODEです。FHN/BVP型の縮約ODEの限定検証です。HH全イオンチャネル、空間軸索、患者データ、実測電気生理の再現を含みません。
- [Keller–Segel走化性](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-keller-segel-ja>)

  細胞密度が化学物質の勾配に応答する2場の代表的な縮約系。次元・境界・化学場の動態が重要です。 全モデル族の実装ではありません。今回の固定例：Keller–Segel：連成流束の製造解
- [Gierer–Meinhardt活性化・抑制](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-gierer-meinhardt-ja>)

  短距離活性化・長距離抑制の簡略代表形。飽和項や基礎生成項には複数の変種があります。 文献解説のみ。
- [流体・弾性構造と埋め込み境界](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-immersed-boundary-ja>)

  流体と変形構造の結合の入口。構造の力・構成則が別途必要で、既存の非圧縮ソルバーだけで実装済みとはなりません。 文献解説のみ。
- [化学マスター方程式とGillespie SSA](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-chemical-master-ja>)

  整数分子数n、反応ジャンプνj、傾向関数ajの確率モデル。Gillespie SSAは軌道を標本化する解法で、反応網自体とは区別します。 全モデル族の実装ではありません。今回の固定例：移入–死亡SSA：有限時刻の厳密分布
- [Mackey–Glass遅延生理フィードバック](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-mackey-glass-ja>)

  遅延を持つフィードバックODE。初期値1点だけでなく、遅延区間の履歴関数が必要です。 文献解説のみ。
- [レプリケータ進化ゲーム動態](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-replicator-ja>)

  利得行列Aに対する戦略割合の動態。定常点と進化的安定戦略の同一視はしません。 文献解説のみ。
- [Schnakenberg反応拡散](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-schnakenberg-ja>)

  自己触媒反応の空間拡張。反応平衡と分散関係から模様の発生を検証するための数理モデルです。 限定した実行例：a=0.1,b=0.9、拡散係数0.01/1、長さ2πの1次元周期Schnakenberg系。旧線形発現例を保持し、固定した反射対称の有限振幅初期値の非線形発展と成長後パターンを独立Fourier–Galerkin/Radau参照および空間・時間細分化で比較します。この旧1次元例だけから一般の模様選択、生物実験への較正、流体連成へ広げません。 全モデル族の実装ではありません。今回の固定例：Schnakenberg：2D境界と初期モード
- [Shigesada–Kawasaki–Teramoto交差拡散](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-skt-ja>)

  自己拡散・交差拡散と競争を含む系。表示は環境ポテンシャルを省いた一様環境での縮約形です。 文献解説のみ。
- [Gray–Scott空間自己触媒反応](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-gray-scott-ja>)

  流入・除去を持つ自己触媒反応拡散。斑点分裂の画像だけで細胞分裂や線形Turing不安定性とは判定しません。 文献解説のみ。
- [Aliev–Panfilov心筋興奮](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-cardiac-ja>)

  心筋波の興奮・回復を表す現象論的な2変数モデル。単・双領域の組織モデルは追加の構成を要します。 文献解説のみ。
- [Repressilator mRNA・タンパク質回路](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-repressilator-ja>)

  3遺伝子の環状抑制。mRNAとタンパク質を残す6変数形で、振動の有無はパラメータに依存します。 文献解説のみ。
- [遺伝子トグルスイッチ](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-toggle-ja>)

  相互抑制による規格化した2変数遺伝子スイッチ。任意のHill指数・生成率で双安定になるとは限りません。 文献解説のみ。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#execution-logistic-growth-ja>)

  無次元の単一個体群。RK4を全出力時刻で解析解と比較し、非負性と刻み幅の収束を確認。反応拡散・複数種は対象外。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#execution-sir-epidemic-ja>)

  閉鎖・均質な人口割合SIR。RK4と別実装のSciPy DOP853を比較。人口保存・非負性・時間収束を確認。SEIR・空間伝播・実データ較正は対象外。

## 問題の図

- [ロジスティック増殖：解析解と刻み幅の収束](<https://hrkoyama.github.io/numerical-methods-atlas/problems/logistic-growth/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/results/logistic-growth/preview.png
- [SIR：独立DOP853参照・人口保存・収束](<https://hrkoyama.github.io/numerical-methods-atlas/problems/sir-epidemic/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/results/sir-epidemic/preview.png

## 厳密解・参照解

- [ロジスティック増殖：解析解と刻み幅の収束：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/logistic-growth/?lang=ja#references-ja>)

  指定r・K・初期値のロジスティック解析解と時間刻み収束が基準です。18件の参照解一覧とは別の固定入力で検証しています。
- [SIR：独立DOP853参照・人口保存・収束：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/sir-epidemic/?lang=ja#references-ja>)

  同一入力の独立DOP853数値参照、人口保存、非負性と時間収束を確認します。一般的な閉形式SIR解の提供ではありません。
- [ロジスティック増殖：解析解と刻み幅の収束：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/logistic-growth/?lang=ja#logistic-growth-ja-validation>)

  無次元の単一個体群。RK4を全出力時刻で解析解と比較し、非負性と刻み幅の収束を確認。反応拡散・複数種は対象外。
- [SIR：独立DOP853参照・人口保存・収束：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/sir-epidemic/?lang=ja#sir-epidemic-ja-validation>)

  別実装DOP853と2段階許容誤差の比較。解析解ではありません。

## コード・検証

- [ロジスティック増殖：解析解と刻み幅の収束](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/logistic-growth/?lang=ja>)
  availability: run

  無次元の単一個体群。RK4を全出力時刻で解析解と比較し、非負性と刻み幅の収束を確認。反応拡散・複数種は対象外。
- [SIR：独立DOP853参照・人口保存・収束](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/sir-epidemic/?lang=ja>)
  availability: run

  閉鎖・均質な人口割合SIR。RK4と別実装のSciPy DOP853を比較。人口保存・非負性・時間収束を確認。SEIR・空間伝播・実データ較正は対象外。
- [ロジスティック増殖：解析解と刻み幅の収束：コード・検証状況](<https://hrkoyama.github.io/numerical-methods-atlas/problems/logistic-growth/?lang=ja#code-ja>)
  availability: source

  対応する公開検査と配布版の条件を確認できます。
- [SIR：独立DOP853参照・人口保存・収束：コード・検証状況](<https://hrkoyama.github.io/numerical-methods-atlas/problems/sir-epidemic/?lang=ja#code-ja>)
  availability: source

  対応する公開検査と配布版の条件を確認できます。
