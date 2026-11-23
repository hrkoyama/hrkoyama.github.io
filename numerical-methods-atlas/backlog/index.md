# 未実装・拡充候補：一つずつ検証する / Implementation and verification backlog

全分野サーベイの98候補と共通5項目を作業台帳に登録し、参照・コード・検証・図を一組ずつ揃えます。既存例の拡充や出典整備も含み、103件すべてが未実装の手法という意味ではありません。

2026年11月23日の指示により全候補を順次進めます。Nohから着手し、一つの単位を実装・独立追試・引用・図・公開まで揃えてから次へ進みます。新規実装、既存検証の拡充、出典整理を区別し、未着手や検証中を実装済みと表示しません。既存の年末必達計画とは別の継続台帳で、全項目の完了期限は設定していません。

Source: https://hrkoyama.github.io/catalog/atlas-benchmark-backlog.json

## 共通：参照・引用・再現

### 既存の検証済み解を参照解カードへ登録

ID: common-reference-cards · P0 · 未着手 · 参照・出典の整備

調査時の範囲：整理・登録不足

調査時の現状：

Bratu、調和振動子、stiff-cosine、水素原子等は既存の解析/参照根拠がある。一覧18件にないことを「解がない」と解釈せず、条件・式・図・実行・出典を一組にする。

追加内容・最小の検証：

- Bratu、調和振動子、stiff-cosine、水素原子等は既存の解析/参照根拠がある。一覧18件にないことを「解がない」と解釈せず、条件・式・図・実行・出典を一組にする。

完了条件：

- 対象の本文・台帳と修正した箇所が確認できる。
- 出典・書誌・適用範囲の修正根拠と確認記録を残す。
- 実在する対象と根拠を照合してから完了にする。

調査時の根拠：

- `numerical-methods-atlas/solutions/index.json`
- `numerical-methods-atlas/problems/bratu/index.json`


### 出典を原問題・解の導出・数値手法・参照実装に分ける

ID: common-citation-roles · P0 · 未着手 · 参照・出典の整備

調査時の範囲：出典整備不足

調査時の現状：

URL配列だけの参照解カードに、著者・年・題名・DOI・該当式/節と条件を補う。初等解は信頼できる教科書と代入確認、製造解は自分で選んだ場と導いた外力・境界を示す。存在しない原著を付けない。

追加内容・最小の検証：

- URL配列だけの参照解カードに、著者・年・題名・DOI・該当式/節と条件を補う。初等解は信頼できる教科書と代入確認、製造解は自分で選んだ場と導いた外力・境界を示す。存在しない原著を付けない。

完了条件：

- 対象の本文・台帳と修正した箇所が確認できる。
- 出典・書誌・適用範囲の修正根拠と確認記録を残す。
- 実在する対象と根拠を照合してから完了にする。

調査時の根拠：

- `numerical-methods-atlas/solutions/index.json` · cases[*].sources


### 連続厳密解・半解析解・製造解・離散厳密解・独立数値参照を区別

ID: common-reference-kinds · P0 · 未着手 · 参照・出典の整備

調査時の範囲：共通仕様の拡充

調査時の現状：

半解析解の根探索/求積誤差、独立参照の解像度/公差と版を記録。同一コードの細格子解は独立参照と別に表示し、点値/セル平均・単位・幾何・境界・時刻を合わせる。

追加内容・最小の検証：

- 半解析解の根探索/求積誤差、独立参照の解像度/公差と版を記録。同一コードの細格子解は独立参照と別に表示し、点値/セル平均・単位・幾何・境界・時刻を合わせる。

完了条件：

- 対象の本文・台帳と修正した箇所が確認できる。
- 出典・書誌・適用範囲の修正根拠と確認記録を残す。
- 実在する対象と根拠を照合してから完了にする。

調査時の根拠：

- `catalog/atlas-depth.json`
- `numerical-methods-atlas/solutions/index.json`


### 各テストを入力・誤差・収束・受入条件まで揃える

ID: common-reproducible-package · P0 · 未着手 · 参照・出典の整備

調査時の範囲：共通仕様の拡充

調査時の現状：

図だけで終えず、固定入力・参照評価コード・結果CSV/JSON・誤差ノルム・保存量・失敗/停止理由・再現コマンドを一組にする。空間・時間・反復・標本誤差を分離し、不連続解に滑らかな解の次数を一律要求しない。

追加内容・最小の検証：

- 図だけで終えず、固定入力・参照評価コード・結果CSV/JSON・誤差ノルム・保存量・失敗/停止理由・再現コマンドを一組にする。空間・時間・反復・標本誤差を分離し、不連続解に滑らかな解の次数を一律要求しない。

完了条件：

- 対象の本文・台帳と修正した箇所が確認できる。
- 出典・書誌・適用範囲の修正根拠と確認記録を残す。
- 実在する対象と根拠を照合してから完了にする。

調査時の根拠：

- `catalog/atlas-execution-examples.json`
- `numerical-methods-atlas/validation/index.json`


### FMM原著レコードの古い未実装注記を修正候補にする

ID: common-stale-reference-note · P0 · 未着手 · 参照・出典の整備

調査時の範囲：出典整備不足

調査時の現状：

greengard1987.note はM2LとFMM solver未実装と記すが、現行の2D log FMMと収束検証がある。利用した原著の範囲を保って現在の限定実装と整合させる。今回のサーベイではサイトを変更していない。

追加内容・最小の検証：

- greengard1987.note はM2LとFMM solver未実装と記すが、現行の2D log FMMと収束検証がある。利用した原著の範囲を保って現在の限定実装と整合させる。今回のサーベイではサイトを変更していない。

完了条件：

- 対象の本文・台帳と修正した箇所が確認できる。
- 出典・書誌・適用範囲の修正根拠と確認記録を残す。
- 実在する対象と根拠を照合してから完了にする。

調査時の根拠：

- `numerical-methods-atlas/references.json` · greengard1987
- `catalog/atlas-methods.json` · fmm


## 圧縮性流体・強衝撃波

### Noh問題：収束流と外向き強衝撃波

ID: compressible-fluid-1 · P1 · 作業中 · 新規実装

調査時の範囲：未収録

調査時の現状：

Sod・Shu–Osherの固定入力、独立Athena++追補shu-independent、PPM/AUSM/回転流束の既存実装と2D保存画像がある。Noh/Sedovは本文の将来項目のみ。

追加内容・最小の検証：

- 平面1Dの固定gamma=5/3から開始し、衝撃位置/速度、密度圧縮、保存量、原点・反射壁過熱を測る。
- 円筒・球対称は幾何ソース/原点正則性を別検証し、可能ならCartesian多次元で対称性破れも測る。
- セル平均と点値、体積重み付き誤差、衝撃近傍と原点近傍の誤差を分ける。
- 厳密なcold limit p0=0と正圧近似を区別。既存Eulerはp<=0を拒否するので無言のfloor追加で厳密Nohと称さない。

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

公開した段階と残る範囲：

今回公開する段階は、初期圧力ゼロの平面1Dと円筒対称1D半径方向の実装・厳密体積平均・格子系列・保存収支・原点過熱の検証です。球対称PDEとCartesian多次元は未実行で、候補全体は進行中のまま保持します。図は円筒半径方向の解の回転表示です。

調査時の根拠：

- `catalog/atlas-test-problems.json`
  Noh IDなし。
- `numerical-methods-atlas/en/read/reference-solutions/index.html` · reference-solutions
  Nohはfuture extensionsのみ。
- `code/numerical-methods-atlas/2026-11-21/numart/equations.py` · Euler.primitive
  非正圧を拒否。

- [Noh (1987), Errors for calculations of strong shocks using an artificial viscosity and an artificial heat flux](<https://www.sciencedirect.com/science/article/pii/002199918790074X>)
  出版社検索結果で著者・JCP72,78–120・DOIと過剰なwall heatingを含む抄録を確認。直接openは403、全文未読。
- [LANL ExactPack official Noh solver](<https://github.com/lanl/ExactPack/blob/master/exactpack/solvers/noh/noh1.py>)
  geometry=1/2/3、既定gamma=5/3、shock_locationと密度式を選択確認。一般gammaを受け付けても圧力実装に4**geometry/3があるため、独立照合は既定gammaで始め、API一般性を無検証で信用しない。

公開した段階の根拠：

```json
{
  "verification": "/code/validated-examples/2026-11-23-r3/noh/verification.json",
  "inputs": [
    "/code/validated-examples/2026-11-23-r3/noh/inputs.json",
    "/code/validated-examples/2026-11-23-r3/noh/acceptance.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-23-r3/noh/results/noh-shock-preview.png",
    "/code/validated-examples/2026-11-23-r3/noh/results/noh-shock.png",
    "/code/validated-examples/2026-11-23-r3/noh/results/noh-shock-errors.png"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#noh-ja",
  "execution": "/numerical-methods-atlas/validation/noh-shock/?lang=ja",
  "code": [
    "/code/validated-examples/2026-11-23-r3/noh/noh_solver.py",
    "/code/validated-examples/2026-11-23-r3/noh/noh_reference.py"
  ],
  "references": [
    "/numerical-methods-atlas/solutions/?lang=ja#solution-noh-ja",
    "/code/validated-examples/2026-11-23-r3/noh/exactpack-reference.json",
    "/code/validated-examples/2026-11-23-r3/noh/exactpack-reference-receipt.json"
  ]
}
```

### Sedov–Taylorの点爆発

ID: compressible-fluid-2 · P1 · 未着手 · 新規実装

調査時の範囲：未収録

調査時の現状：

Sod・Shu–Osherの固定入力、独立Athena++追補shu-independent、PPM/AUSM/回転流束の既存実装と2D保存画像がある。Noh/Sedovは本文の将来項目のみ。

追加内容・最小の検証：

- 固定爆発エネルギーの正規化、自己相似の衝撃半径と密度/圧力/速度を比較。
- 有限セルへのエネルギー投入半径の誤差とPDE格子誤差を分け、球対称体積平均で参照を作る。
- 低密度/負圧、総エネルギー、球対称性、中心特異点を報告。

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

調査時の根拠：

- `catalog/atlas-test-problems.json`
  Sedov IDなし。
- `numerical-methods-atlas/en/read/reference-solutions/index.html` · reference-solutions
  Sedovは将来項目としてのみ言及。

- [LANL ExactPack: official benchmark collection and references](<https://github.com/lanl/ExactPack>)
  公式READMEでNoh/Sedov/Guderleyと出典一覧を確認。追加して相互検証する候補であり、現アトラスの依存や照合済み実績ではない。

### Double-Mach/前向きステップの多格子・独立参照

ID: compressible-fluid-3 · P2 · 未着手 · 検証の拡充

調査時の範囲：検証範囲不足

調査時の現状：

Sod・Shu–Osherの固定入力、独立Athena++追補shu-independent、PPM/AUSM/回転流束の既存実装と2D保存画像がある。Noh/Sedovは本文の将来項目のみ。

追加内容・最小の検証：

- 既存初期条件と境界処理を固定し、少数格子で衝撃位置・保存誤差・wall jetを比較。
- 独立コードの有限格子数値参照として保存し厳密2D解とは呼ばない。
- 現時刻まで到達しない計算と成功例を混ぜない。

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

調査時の根拠：

- `catalog/atlas-test-problems.json` · double-mach/forward-step
  計算画像あり、標準runner結び付けはなし。
- `numerical-methods-atlas/en/read/double-mach/index.html` · double-mach
  粗格子HLL像でfull-pattern収束・独立比較は未達と明記。


### 低Mach前処理の限定した渦検証

ID: compressible-fluid-4 · P2 · 未着手 · 新規実装

調査時の範囲：解説のみ

調査時の現状：

Sod・Shu–Osherの固定入力、独立Athena++追補shu-independent、PPM/AUSM/回転流束の既存実装と2D保存画像がある。Noh/Sedovは本文の将来項目のみ。

追加内容・最小の検証：

- 既存等エントロピー渦と同じ解析場を基準に少数Mach値を固定。
- 圧力誤差のMach依存、速度誤差、音響/対流刻み、定常残差を分離。
- 原理説明やRoe entropy-fixの成功をPDE前処理の実装と取り違えない。

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

調査時の根拠：

- `catalog/atlas-methods.json` · low-mach-preconditioning
  status=reading-only、code_modules=[]。
- `catalog/atlas-test-problems.json` · isentropic-vortex
  原KEEPの既存計算はある。


### Guderleyの収束衝撃波

ID: compressible-fluid-additional · P2 · 未着手 · 新規実装

調査時の範囲：未収録

調査時の現状：

Sod・Shu–Osherの固定入力、独立Athena++追補shu-independent、PPM/AUSM/回転流束の既存実装と2D保存画像がある。Noh/Sedovは本文の将来項目のみ。

追加内容・最小の検証：

- Noh/Sedovと区別し、相似指数の固有値問題と半解析的な場の参照を構成する。
- まず収束前の限定時区間・固定EOSで衝撃軌道と体積平均を照合し、原点反射後の分岐は別段階とする。

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

調査時の根拠：

- `catalog/atlas-test-problems.json` · sod/shu-osher/strong-shock/double-mach/cylinder-forebody
  既存登録。strong-shockやdouble-machも計算済みであり未実装ではない。
- `catalog/atlas-execution-examples.json` · sod/shu-osher
  共通固定入力あり。
- `numerical-methods-atlas/validation/index.json` · shu-independent
  独立Athena++参照・格子収束あり。

- [LANL ExactPack: Guderley problem and references](<https://github.com/lanl/ExactPack>)
  公式READMEのGuderley登録とRamsey–Kamm–Bolstad (2012)の参照先を確認。原著の全導出・数値再現は未実施。

## 移流・再構築・正値性

### Eulerの段階ごとの完全離散正値性

ID: advection-reconstruction-1 · P1 · 未着手 · 検証の拡充

調査時の範囲：検証範囲不足

調査時の現状：

MUSCL、WENO-JS/Z、PPM、CIP、DG、特性再構築、各limiterは実装済み。1D滑らか/不連続、2D entropy wave、保存・界面恒等式の検査がある。

追加内容・最小の検証：

- 既存mean-preserving scalingの部品検査から、許容数値流束・SSP段階・CFLを含む一つの限定更新へ接続。
- 密度/圧力最小値とセル平均保存を全段階で測る。
- 強希薄波/near-vacuumで失敗・retry・floorを記録し、結果を理論の保証条件と対応付ける。

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

調査時の根拠：

- `code/numerical-methods-atlas/2026-11-21/numart/limiters.py` · positive_reconstruction
  部品は実装済み。
- `code/numerical-methods-atlas/2026-11-21/tests/test_limiters.py` · test_positive_scaling_conservation_and_pressure
  再構築テストあり。
- `numerical-methods-atlas/en/read/advanced-limiters/index.html` · advanced-limiters
  Euler MUSCL/FD WENOへの未接続を明記。

- [Zhang & Shu (2010), positivity-preserving Euler DG schemes](<https://www.math.purdue.edu/~zhan1966/research/paper/euler.pdf>)
  著者公開原稿をopenし題名・著者・密度圧力正値性の対象を確認。全文監査ではない。

### Zalesak型2D回転輸送・形状保持

ID: advection-reconstruction-2 · P2 · 未着手 · 新規実装

調査時の範囲：未収録

調査時の現状：

MUSCL、WENO-JS/Z、PPM、CIP、DG、特性再構築、各limiterは実装済み。1D滑らか/不連続、2D entropy wave、保存・界面恒等式の検査がある。

追加内容・最小の検証：

- 既存1D矩形波と2D滑らかentropy waveを残し、周期回転後の解析的returnを新たな問題として追加。
- 総量、min/max、形状誤差と回転中心/格子方向依存を比較。
- スロット形状・時刻・境界と点値/セル平均を原著または公式実装から固定する。

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

調査時の根拠：

- `catalog/atlas-test-problems.json` · advection-square/entropy-2d
  既存は1D不連続または2D滑らか。Zalesak固有IDなし。

- [Zalesak (1979), Fully multidimensional flux-corrected transport algorithms for fluids](<https://www.sciencedirect.com/science/article/pii/0021999179900512>)
  出版社書誌・抄録を確認。具体的スロット形状等は実装前に原文のテスト定義を照合する。

### WENO-Zの臨界点・epsilon依存の比較

ID: advection-reconstruction-3 · P2 · 未着手 · 検証の拡充

調査時の範囲：検証範囲不足

調査時の現状：

MUSCL、WENO-JS/Z、PPM、CIP、DG、特性再構築、各limiterは実装済み。1D滑らか/不連続、2D entropy wave、保存・界面恒等式の検査がある。

追加内容・最小の検証：

- 既存p=2・epsilon=1e-6版を凍結し、比較版を追加して極値/高階臨界点の空間誤差を測る。
- 時間誤差を小さくした系列と固定格子の刻み系列を分離する。
- 原著最終版と前稿で異なる重み規約、特性/成分投影、FD点値を明記。

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

調査時の根拠：

- `catalog/atlas-methods.json` · weno-z
  variantとlimited review scope記録済み。
- `numerical-methods-atlas/references.json` · borges2008
  最終版はmetadata/abstract、以前の前稿と区別。
- `code/numerical-methods-atlas/2026-11-21/tests/test_reconstruction.py` · test_weno_constant_and_smooth_spatial_flux_derivative
  滑らか関数の既存検査を基準に拡張。


## 浅水・地形・wet/dry

### SWASHESのlake at rest・地形上の定常解

ID: shallow-water-1 · P1 · 未着手 · 新規実装

調査時の範囲：未収録

調査時の現状：

平坦底・正水深SWEのダム崩壊は実装済み。乾床の参照解カードはあるが既存FV solverは正水深専用。

追加内容・最小の検証：

- 地形圧力ソースとfluxの釣合い、静止水面の保持、質量を測る。
- 一つのsmooth bump定常ケースから始め、境界条件と水頭/流量を固定。
- 平坦底ダム崩壊の成功をwell-balanced性の証拠にしない。

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

調査時の根拠：

- `code/numerical-methods-atlas/2026-11-21/numart/equations.py` · Barotropic(name='shallow-water')
  地形項を含まない基準。
- `catalog/atlas-test-problems.json` · dam-break
  現行問題との差。

- [Delestre et al., SWASHES](<https://arxiv.org/abs/1110.0288v7>)
  著者原稿の書誌・抄録を確認。2013出版、2016修正版v7で出版版の誤りを訂正と明示。参照版を固定すべき。

### dry-bed参照を使うwetting/drying実行

ID: shallow-water-2 · P2 · 未着手 · 検証の拡充

調査時の範囲：検証範囲不足

調査時の現状：

平坦底・正水深SWEのダム崩壊は実装済み。乾床の参照解カードはあるが既存FV solverは正水深専用。

追加内容・最小の検証：

- 既存解析乾床解とfront位置、乾湿遷移、非負水深、質量を照合。
- dry toleranceと運動量処理、dry-cell速度の定義を公開。
- 既存の参照カードを実行済みと数えず、solver拡張後に新規固定入力を登録。

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

調査時の根拠：

- `numerical-methods-atlas/solutions/index.json` · swe-dry-bed/swe-vacuum
  参照は収録済み。
- `code/numerical-methods-atlas/2026-11-21/numart/equations.py` · Barotropic(name='shallow-water')
  現solverは非正水深を拒否。

- [Delestre et al., SWASHES](<https://arxiv.org/abs/1110.0288v7>)
  著者原稿の書誌・抄録を確認。2013出版、2016修正版v7で出版版の誤りを訂正と明示。参照版を固定すべき。

## 非圧縮流・壁境界

### Ghiaのlid-driven cavity低Re比較

ID: incompressible-1 · P2 · 未着手 · 新規実装

調査時の範囲：未収録

調査時の現状：

周期2D MAC射影法とTaylor–Greenの16/32/64格子、圧力・divergence・保存診断、共通固定入力はある。壁境界や境界層の検証はない。

追加内容・最小の検証：

- まずRe=100等の固定した少数条件で壁速度・角点処理・圧力基準を定義。
- 中心線u/v、渦中心、divergenceと定常残差を格子ごとに比較。
- Ghia表は高精度数値参照であり厳密解ではない。原表転記・出典ページと独立参照の差も保存。

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

調査時の根拠：

- `numerical-methods-atlas/en/read/incompressible/index.html` · incompressible
  周期基準のみ、wall boundary未実装を明記。
- `code/numerical-methods-atlas/2026-11-21/numart/incompressible.py` · poisson/project
  周期FFT演算子。

- [Ghia, Ghia & Shin (1982), High-Re solutions for incompressible flow](<https://www.sciencedirect.com/science/article/abs/pii/0021999182900584>)
  出版社検索結果の書誌・抄録で正方形cavityと数値参照を確認。直接openは403、表の値や全文は未照合。

### Blasiusまたは非周期の製造解による壁面検査

ID: incompressible-2 · P2 · 未着手 · 新規実装

調査時の範囲：未収録

調査時の現状：

周期2D MAC射影法とTaylor–Greenの16/32/64格子、圧力・divergence・保存診断、共通固定入力はある。壁境界や境界層の検証はない。

追加内容・最小の検証：

- 軽い非周期MMSで速度/圧力の境界と次数を先に検査。
- Blasius追加時は境界層近似の相似ODE解と、有限Re Navier–Stokes/有限計算領域の差を区別。
- 壁面せん断・排除厚さ・領域依存を測り、全NSの厳密解と表示しない。

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

調査時の根拠：

- `numerical-methods-atlas/en/read/reference-solutions/index.html` · reference-solutions
  Blasiusは将来項目。
- `code/numerical-methods-atlas/2026-11-21/numart/incompressible.py` · taylor_green
  現有は周期解析場。

- [Salari & Knupp, Code Verification by the Method of Manufactured Solutions, SAND2000-1444](<https://www.sandia.gov/research/publications/details/code-verification-by-the-method-of-manufactured-solutions-2000-06-01/>)
  Sandia公式報告の書誌・概要・DOI10.2172/759450を確認。製造解の検証方法の出典で、個別の初等解の発見原著として扱わない。

### Kelvin–Helmholtz／Rayleigh–Taylorの初期成長と独立参照

ID: incompressible-additional · P2 · 未着手 · 新規実装

調査時の範囲：未収録

調査時の現状：

周期2D MAC射影法とTaylor–Greenの16/32/64格子、圧力・divergence・保存診断、共通固定入力はある。壁境界や境界層の検証はない。

追加内容・最小の検証：

- 滑らかなせん断層・明示した摂動・境界・物理散逸を固定し、KHの初期成長率を比較する。
- RTは重力・密度配置・界面厚さと理論の仮定を別に定義する。非線形後期の図を厳密解と扱わず独立数値参照と比較する。

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

調査時の根拠：

- `catalog/atlas-methods.json` · projection
  educational-example。
- `catalog/atlas-execution-examples.json` · taylor-green
  共通実行あり。
- `code/numerical-methods-atlas/2026-11-21/tests/test_new_models.py` · test_taylor_green_refinement_energy_and_pressure
  既存2次収束・圧力検査。

- [McNally–Lyra–Passy: A Well-Posed Kelvin-Helmholtz Instability Test and Comparison](<https://arxiv.org/abs/1111.1764>)
  著者稿の書誌・抄録で初期成長と滑らかな設定の検証目的を確認。この論文はKHの出典でありRT原典ではない。

## 非相対論的MHD・CT/GLM/HLLD

### 円偏波Alfvén波・磁場ループの独立比較と収束

ID: mhd-1 · P1 · 未着手 · 検証の拡充

調査時の範囲：検証範囲不足

調査時の現状：

Brio–Wuは共通実行と独立Athena++追補があり、Orszag–Tangには独立比較と格子/時間感度を分離した追補がある。GLM解析モード・滑らかな移動平衡・非物理制約対照も既に実行済み。

追加内容・最小の検証：

- 既存保存結果を基準に空間/時間系列を分離し、Alfvén位相誤差・偏波・保存量を解析波で測る。
- loopは独立コードと比較し、磁気エネルギー・ループ形状・divergence演算子を揃える。
- 他のOT追補の独立照合を旧loopの検証に流用しない。

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

調査時の根拠：

- `catalog/atlas-test-problems.json` · circular-alfven/magnetic-loop
  問題・計算結果は収録済み、固定入力runner結び付けなし。
- `catalog/atlas-mhd-supplements.json` · historical_replacements
  旧loopの独立照合、強磁場、UCT-HLLDは未検証と明記。

- [Gardiner & Stone (2005), An Unsplit Godunov Method for Ideal MHD via CT](<https://arxiv.org/abs/astro-ph/0501557>)
  著者原稿の抄録・書誌で面平均B、共有corner EMF、CTU/PPM結合を確認。現在の算術flux-CTと同一実装とは呼ばない。

### 衝撃波後OTまたは標準rotorの限定検証

ID: mhd-2 · P2 · 未着手 · 検証の拡充

調査時の範囲：検証範囲不足

調査時の現状：

Brio–Wuは共通実行と独立Athena++追補があり、Orszag–Tangには独立比較と格子/時間感度を分離した追補がある。GLM解析モード・滑らかな移動平衡・非物理制約対照も既に実行済み。

追加内容・最小の検証：

- 現行short smooth OTを残し、衝撃波を伴う別時刻/別入力を区別して追加。
- 熱圧正値性・総エネルギー・native face/common cell divB・参照格子増分を測る。
- rotorを採るなら新規問題として初期回転/磁場/境界を固定し、既存CTU/UCT実装の再現とは呼ばない。

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

調査時の根拠：

- `numerical-methods-atlas/validation/index.json` · ct-glm-ot-convergence
  衝撃波後・3D・一般cleaning認証ではないと明記。
- `catalog/atlas-test-problems.json` · orszag-tang
  現行独立実行はある。rotor固有IDは未登録。

- [Gardiner & Stone (2005), An Unsplit Godunov Method for Ideal MHD via CT](<https://arxiv.org/abs/astro-ph/0501557>)
  著者原稿の抄録・書誌で面平均B、共有corner EMF、CTU/PPM結合を確認。現在の算術flux-CTと同一実装とは呼ばない。

## 格子・座標・非構造FEM

### L字領域Poisson特異解と歪んだ三角形FEM

ID: mesh-coordinate-1 · P2 · 未着手 · 新規実装

調査時の範囲：未収録

調査時の現状：

幾何接続の正面積/閉包/隣接検査、球面格子の面積と被覆、円筒物理成分のテンソル恒等式は実装済み。P1 FEMは単位正方形の製造解を解く。

追加内容・最小の検証：

- r^(2/3)sin(2theta/3)型のreentrant corner解などを境界条件とともに自前定義し、L2/H1誤差を要素積分。
- 一様/局所細分化、要素角度・aspect ratio・条件数の影響を分ける。
- 単位正方形の滑らかな2次L2収束を特異解や不規則格子に一般化しない。

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

調査時の根拠：

- `catalog/atlas-test-problems.json` · poisson-2d-sine
  現基準は滑らかな正弦。
- `numerical-methods-atlas/en/read/meshes/index.html` · meshes
  Matplotlib三角形分割と幾何展示で、Triangle/一般非構造flow solverではない。

- [Shewchuk (1996), Triangle: Engineering a 2D Quality Mesh Generator](<https://www.cs.cmu.edu/~quake/tripaper/triangle0.html>)
  著者公開原著の書誌と算法/品質/robust predicatesの節構成を確認。現コードはMatplotlib triangulationでありTriangle利用ではない。
- [Salari & Knupp, Code Verification by the Method of Manufactured Solutions, SAND2000-1444](<https://www.sandia.gov/research/publications/details/code-verification-by-the-method-of-manufactured-solutions-2000-06-01/>)
  Sandia公式報告の書誌・概要・DOI10.2172/759450を確認。製造解の検証方法の出典で、個別の初等解の発見原著として扱わない。

### 円筒・曲線座標の環状領域PDE製造解

ID: mesh-coordinate-2 · P2 · 未着手 · 検証の拡充

調査時の範囲：検証範囲不足

調査時の現状：

幾何接続の正面積/閉包/隣接検査、球面格子の面積と被覆、円筒物理成分のテンソル恒等式は実装済み。P1 FEMは単位正方形の製造解を解く。

追加内容・最小の検証：

- まずr>0のannulusで粘性応力発散・可変粘性・境界fluxを一組の製造解で離散化検査。
- 座標の物理/共変/反変成分と体積/面積重みを固定し、格子収束を測る。
- 軸を含む場合は正則性とaxis stencilを別テストにする。平面Poiseuille/Couetteを円筒問題の同一参照にしない。

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

調査時の根拠：

- `code/numerical-methods-atlas/2026-11-21/numart/coordinates.py` · cylindrical_velocity_gradient/cylindrical_stress_divergence
  r=0を拒否する点演算子。
- `catalog/atlas-chapter-links.json` · coordinates-viscosity
  現対応はソース/恒等式検査のみ。

- [Salari & Knupp, Code Verification by the Method of Manufactured Solutions, SAND2000-1444](<https://www.sandia.gov/research/publications/details/code-verification-by-the-method-of-manufactured-solutions-2000-06-01/>)
  Sandia公式報告の書誌・概要・DOI10.2172/759450を確認。製造解の検証方法の出典で、個別の初等解の発見原著として扱わない。

## ALE・地球流体・球面格子

### 非一様移動格子輸送、その後Saltzman歪み格子ピストン

ID: ale-geophysical-1 · P2 · 未着手 · 検証の拡充

調査時の範囲：検証範囲不足

調査時の現状：

ALEは一様状態の1D moving-volume/GCL検査。A/B/C-gridはperiodic f-planeの半離散Fourier symbolと独立stencil照合。球面格子の幾何は実装済みで全球SWEの時間発展ではない。

追加内容・最小の検証：

- 最初は既存GCLと同じ移動に非一様scalarの解析輸送を載せ、幾何誤差と輸送誤差を分離。
- Lagrange/remapまで拡張する段階でSaltzmanを新規問題として考慮し、格子反転・歪み・保存・衝撃位置を検査。
- 現在のALE一様状態チェックを完全Euler/remap実装と呼ばない。Saltzman原典/入力は別途照合が必要。

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

調査時の根拠：

- `code/numerical-methods-atlas/2026-11-21/numart/geometry.py` · moving_volume_uniform_test
  一様状態のみ。
- `catalog/atlas-test-problems.json`
  Saltzman登録なし。

- [Salari & Knupp, Code Verification by the Method of Manufactured Solutions, SAND2000-1444](<https://www.sandia.gov/research/publications/details/code-verification-by-the-method-of-manufactured-solutions-2000-06-01/>)
  Sandia公式報告の書誌・概要・DOI10.2172/759450を確認。製造解の検証方法の出典で、個別の初等解の発見原著として扱わない。

### 回転浅水波の時間積分→Williamsonの限定した球面ケース

ID: ale-geophysical-2 · P2 · 未着手 · 検証の拡充

調査時の範囲：検証範囲不足

調査時の現状：

ALEは一様状態の1D moving-volume/GCL検査。A/B/C-gridはperiodic f-planeの半離散Fourier symbolと独立stencil照合。球面格子の幾何は実装済みで全球SWEの時間発展ではない。

追加内容・最小の検証：

- まず既存f-planeの一つの固有modeを実際に時間積分し位相・振幅・geostrophic balanceを解析行列指数と比較。
- 球面拡張時はWilliamsonの固体回転輸送/定常釣合いから段階的に選び、質量/エネルギー/位相と格子向きを比較。
- A/B/C配置だけで時間精度・PV保存・全球dynamical coreの完成を主張しない。

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

調査時の根拠：

- `code/numerical-methods-atlas/2026-11-21/numart/geophysical_grids.py` · symbol/gravity_frequency
  半離散記号。
- `code/numerical-methods-atlas/2026-11-21/tests/test_geophysical_grids.py` · test_fourier_symbol_matches_independent_physical_grid_stencils
  現有の独立空間演算子照合を保持。

- [MITgcm official documentation, C grid staggering of variables](<https://mitgcm.readthedocs.io/en/latest/algorithm/c-grid.html>)
  公式現行ドキュメントのC-grid配置を確認。MITgcm全体の再現ではない。
- [Williamson et al. (1992), A standard test set for spherical shallow water](<https://www.sciencedirect.com/science/article/pii/S0021999105800166>)
  出版社書誌・抄録で七つの段階的テストを確認。全球SWEの実装を現在の球面格子幾何テストから推定しない。

## 相対論的流体・SRMHD

### Martí–Müller型1D相対論衝撃管

ID: relativistic-fluid-1 · P2 · 未着手 · 新規実装

調査時の範囲：解説のみ

調査時の現状：

相対論的流体章とsrhd/grhd/grmhd方程式カードは文献解説のみ。対応する83物理問題、22共通実行、40追補、配布solverは見当たらない。非相対論的HLLD/CT/GLMは代用にならない。

追加内容・最小の検証：

- まずMinkowski・理想気体EOS・法線速度のみの少数固定入力。
- 原始変数回復の残差、rho/p正値、|v|<1、波位置、中間状態をexact Riemann参照と比較。
- 物理/保存変数とセル平均/点値を明示し、GR時空や任意EOSの検証へ拡張解釈しない。

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

調査時の根拠：

- `numerical-methods-atlas/equations/index.json` · srhd
  代表式はあるが実行なし。

- [Martí & Müller (1994), The analytical solution of the Riemann problem in relativistic hydrodynamics](<https://www.cambridge.org/core/journals/journal-of-fluid-mechanics/article/abs/analytical-solution-of-the-riemann-problem-in-relativistic-hydrodynamics/ACFB60CD3557DF2AF8AFF6B72D8B03A4>)
  出版社書誌・抄録でMinkowski時空・polytropic gas・中間圧力の暗黙代数方程式を確認。1994出版と2006電子公開日を区別。

### SRMHDの固定Riemann/Alfvénケース

ID: relativistic-fluid-2 · P3 · 未着手 · 新規実装

調査時の範囲：未収録

調査時の現状：

相対論的流体章とsrhd/grhd/grmhd方程式カードは文献解説のみ。対応する83物理問題、22共通実行、40追補、配布solverは見当たらない。非相対論的HLLD/CT/GLMは代用にならない。

追加内容・最小の検証：

- SRHDの保存・回復が通った後、固定EOSで簡単な磁場配置から開始。
- Bx一定、物理的状態、波位置、磁場/流体相互作用を独立exact RMHD参照と照合。
- B→0極限はSRHDと整合を検査し、非相対論HLLD実装の名前をそのままSRMHD実装扱いしない。

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

調査時の根拠：

- `numerical-methods-atlas/equations/index.json` · grmhd
  文献説明のみ、SRMHD固有カード/runnerなし。
- `catalog/atlas-methods.json` · hlld
  既存はideal nonrelativistic MHD。

- [Giacomazzo & Rezzolla (2006), Exact Riemann solution in relativistic MHD](<https://www.cambridge.org/core/journals/journal-of-fluid-mechanics/article/exact-solution-of-the-riemann-problem-in-relativistic-magnetohydrodynamics/96301C50DDB8E673859CF715B0813F3B>)
  出版社書誌・抄録で三波と一般七波の場合を確認。DOI10.1017/S0022112006001145。著者公式配布ページも確認できるが数値参照は未生成。

## 楕円型・Poisson

### 2Dの純Neumann・混合Robin製造解を、互換条件と平均値ゲージ込みで固定入力化

ID: elliptic-poisson-1 · P1 · 未着手 · 検証の拡充

調査時の範囲：検証範囲不足

調査時の現状：

Thomasの1D Dirichlet固定入力、1D Neumann/Robin/周期境界の既存実装、2D正方形のCG/幾何MG/P1 FEMとsin製造解、SA-AMGがある。amg-conditioningは条件数・残差/前進誤差・定係数異方性ストレス・DST/直接解照合まで実施済み。AMGや異方性検査そのものを未実装扱いしない。

追加内容・最小の検証：

- 既存1D境界実装と区別し、2Dの零空間・不適合右辺の拒否・平均値指定を検査
- 2D CG/MGの現状は零Dirichlet。cos型参照解で境界誤差と残差を分ける

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

調査時の根拠：

- `catalog/atlas-methods.json` · cg.limitations,multigrid.limitations
- `code/numerical-methods-atlas/2026-11-21/numart/linear.py` · poisson_boundary_1d

- [PETSc公式: Singular systems / Neumann nullspace](<https://petsc.org/release/manual/ksp/>)
  一次論文の出版社ページまたは公式資料を検索・確認。全文監査や数値再現ではない。
- [MFEM公式: Example 27 Laplace boundary conditions](<https://mfem.org/examples/>)
  一次論文の出版社ページまたは公式資料を検索・確認。全文監査や数値再現ではない。

### checkerboard係数ジャンプ／回転異方性拡散のMG・AMG比較

ID: elliptic-poisson-3 · P2 · 未着手 · 検証の拡充

調査時の範囲：検証範囲不足

調査時の現状：

Thomasの1D Dirichlet固定入力、1D Neumann/Robin/周期境界の既存実装、2D正方形のCG/幾何MG/P1 FEMとsin製造解、SA-AMGがある。amg-conditioningは条件数・残差/前進誤差・定係数異方性ストレス・DST/直接解照合まで実施済み。AMGや異方性検査そのものを未実装扱いしない。

追加内容・最小の検証：

- 既存amg-conditioningの定係数異方性を再追加しない
- 不連続係数の流束整合、真の残差・前進誤差・収束不達を固定ケースで比較

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

調査時の根拠：

- `code/validated-examples/2026-11-22/foundations-conditioning/cases.json` · amg-conditioning.limits
- `catalog/atlas-methods.json` · multigrid.limitations

- [PETSc公式: Singular systems / Neumann nullspace](<https://petsc.org/release/manual/ksp/>)
  一次論文の出版社ページまたは公式資料を検索・確認。全文監査や数値再現ではない。

### Thomas法の原報と再録・関連章文献の役割整理

ID: elliptic-poisson-4 · P2 · 未着手 · 参照・出典の整備

調査時の範囲：出典整備不足

調査時の現状：

Thomasの1D Dirichlet固定入力、1D Neumann/Robin/周期境界の既存実装、2D正方形のCG/幾何MG/P1 FEMとsin製造解、SA-AMGがある。amg-conditioningは条件数・残差/前進誤差・定係数異方性ストレス・DST/直接解照合まで実施済み。AMGや異方性検査そのものを未実装扱いしない。

追加内容・最小の検証：

- 台帳のThomasリンクはCrank–Nicolson/多重格子文献が中心
- 既存実行記録の『Thomas原報は未確認』を維持し、原報確認ができたときだけアクセス深度を更新

完了条件：

- 対象の本文・台帳と修正した箇所が確認できる。
- 出典・書誌・適用範囲の修正根拠と確認記録を残す。
- 実在する対象と根拠を照合してから完了にする。

調査時の根拠：

- `catalog/atlas-methods.json` · thomas.references
- `catalog/atlas-execution-examples.json` · poisson-1d-dirichlet.reference_notes


## 重力・周期静電場・多重極

### 中性スラブのYeh–Berkowitz補正／2D周期境界ベンチマーク

ID: gravity-electrostatics-multipole-1 · P2 · 未着手 · 新規実装

調査時の範囲：解説のみ

調査時の現状：

孤立3D Plummer軟化Barnes–Hut（単極/完全2次モーメント）と直接和、3D周期CIC–FFT–CIC、Ewald/SPME、2D対数核FMMのM2M/M2L/L2Lが既存。追加粒子検証でEwaldの独立theta参照、SPME格子/次数/位相、FMM次数/木深さ・保存診断まである。 FMMの古い文献注記の整合は共通P0にまとめた。

追加内容・最小の検証：

- slab-ewaldはplannedで詳細解説あり、通常の中性立方Ewald実装とは区別
- 真空層厚依存・双極子補正・力の有限差分・独立2D参照を小ケースで検査

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

調査時の根拠：

- `catalog/atlas-methods.json` · slab-ewald
- `code/validated-examples/2026-11-22/particle-transport/cases.json` · ewald-convergence.limits

- [Yeh & Berkowitz (1999), Ewald summation for systems with slab geometry](<https://pubs.aip.org/jcp/article/111/7/3155/294442/Ewald-summation-for-systems-with-slab-geometry>)
  DOI 10.1063/1.479595と出版社への解決先を確認。本文取得はツールで失敗。既存原著台帳yeh1999にも書誌情報あり。

### 3D 1/r核／適応木のFMM

ID: gravity-electrostatics-multipole-2 · P3 · 未着手 · 検証の拡充

調査時の範囲：検証範囲不足

調査時の現状：

孤立3D Plummer軟化Barnes–Hut（単極/完全2次モーメント）と直接和、3D周期CIC–FFT–CIC、Ewald/SPME、2D対数核FMMのM2M/M2L/L2Lが既存。追加粒子検証でEwaldの独立theta参照、SPME格子/次数/位相、FMM次数/木深さ・保存診断まである。 FMMの古い文献注記の整合は共通P0にまとめた。

追加内容・最小の検証：

- 既存FMMは2D自由空間log核で、3D重力用FMMではない
- 一様球など解析配置・直接和・次数/木深さを分け、必要用途が出た時に範囲拡張

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

調査時の根拠：

- `catalog/atlas-methods.json` · fmm.limitations
- `code/validated-examples/2026-11-22/particle-transport/cases.json` · fmm-convergence


### Plummer球の短時間力学／2体軌道の重力時間積分

ID: gravity-electrostatics-multipole-3 · P2 · 未着手 · 検証の拡充

調査時の範囲：検証範囲不足

調査時の現状：

孤立3D Plummer軟化Barnes–Hut（単極/完全2次モーメント）と直接和、3D周期CIC–FFT–CIC、Ewald/SPME、2D対数核FMMのM2M/M2L/L2Lが既存。追加粒子検証でEwaldの独立theta参照、SPME格子/次数/位相、FMM次数/木深さ・保存診断まである。 FMMの古い文献注記の整合は共通P0にまとめた。

追加内容・最小の検証：

- 現Barnes–Hut固定例は静的力のみ
- 同一軟化核で軌道・エネルギー/運動量の時間誤差と木近似誤差を分ける。長時間・大粒子数走査は後段

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

調査時の根拠：

- `catalog/atlas-execution-examples.json` · barnes-hut.scope
- `catalog/atlas-methods.json` · barnes-hut.limitations

- [Barnes & Hut (1986), A hierarchical O(N log N) force-calculation algorithm](<https://www.nature.com/articles/324446a0>)
  出版社の検索結果・抄録を確認。直接openは認証リダイレクトのため失敗。

## PIC・プラズマ

### 線形Landau減衰

ID: pic-1 · P1 · 未着手 · 新規実装

調査時の範囲：未収録

調査時の現状：

1D周期・静電CIC PICの冷たいプラズマ振動が既存。格子/時間の独立細分化、電荷・運動量・Gauss/Poisson残差、単粒子自己力、64seedの初期粒子雑音まで保存。暖かい分布や不安定性の検証ではない。

追加内容・最小の検証：

- 1D1Vの弱い摂動で電場振幅の減衰率・周波数を解析分散関係と照合
- 粒子雑音・速度分布標本化・格子/刻みの誤差を分離

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

調査時の根拠：

- `catalog/atlas-methods.json` · pic.limitations
- `code/validated-examples/2026-11-22/particle-transport/cases.json` · pic-conservation.limits

- [Kraus et al. (2017), GEMPIC: geometric electromagnetic particle-in-cell methods](<https://www.cambridge.org/core/journals/journal-of-plasma-physics/article/gempic-geometric-electromagnetic-particleincell-methods/C32D97F1B5281878F094B7E5075D291A>)
  出版社本文のLandau damping・Weibel検証節を確認。掲載された大規模設定の再現を推奨する意味ではない。

### two-stream不安定性

ID: pic-2 · P2 · 未着手 · 新規実装

調査時の範囲：未収録

調査時の現状：

1D周期・静電CIC PICの冷たいプラズマ振動が既存。格子/時間の独立細分化、電荷・運動量・Gauss/Poisson残差、単粒子自己力、64seedの初期粒子雑音まで保存。暖かい分布や不安定性の検証ではない。

追加内容・最小の検証：

- 線形成長率と非線形飽和を別指標にし、速度分布・粒子数依存を固定入力化
- 冷たいcos(t)振動への合格を成長問題の検証に流用しない

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

調査時の根拠：

- `code/validated-examples/2026-11-22/particles/cases.json` · pic.limits

- [Kraus et al. (2017), GEMPIC: geometric electromagnetic particle-in-cell methods](<https://www.cambridge.org/core/journals/journal-of-plasma-physics/article/gempic-geometric-electromagnetic-particleincell-methods/C32D97F1B5281878F094B7E5075D291A>)
  出版社本文のLandau damping・Weibel検証節を確認。掲載された大規模設定の再現を推奨する意味ではない。

### PIC空間離散そのものの独立実装照合

ID: pic-3 · P2 · 未着手 · 検証の拡充

調査時の範囲：検証範囲不足

調査時の現状：

1D周期・静電CIC PICの冷たいプラズマ振動が既存。格子/時間の独立細分化、電荷・運動量・Gauss/Poisson残差、単粒子自己力、64seedの初期粒子雑音まで保存。暖かい分布や不安定性の検証ではない。

追加内容・最小の検証：

- 現DOP853は時間参照であり、独立PIC空間実装ではない
- 同じ初期粒子・電荷割当・離散Poisson規約をそろえた小ケースを第三者実装または別実装で照合

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

調査時の根拠：

- `code/validated-examples/2026-11-22/particle-transport/cases.json` · pic-conservation.limits

- [Kraus et al. (2017), GEMPIC: geometric electromagnetic particle-in-cell methods](<https://www.cambridge.org/core/journals/journal-of-plasma-physics/article/gempic-geometric-electromagnetic-particleincell-methods/C32D97F1B5281878F094B7E5075D291A>)
  出版社本文のLandau damping・Weibel検証節を確認。掲載された大規模設定の再現を推奨する意味ではない。

## DSMC・希薄気体

### 平板Couette流／Fourier熱伝導の希薄気体ベンチマーク

ID: dsmc-1 · P1 · 未着手 · 新規実装

調査時の範囲：未収録

調査時の現状：

均質Maxwell分子の衝突成分・平衡緩和が既存。運動量/エネルギー保存、有限Nのmicrocanonical/beta参照、64seed統計、異方性減衰を検査。空間streaming・衝突セル・物理時間の一般DSMCではない。

追加内容・最小の検証：

- まず小さい1D空間・3D速度系で壁散乱、Knudsen層、せん断応力/熱流束を確認
- セル幅/平均自由行程、刻み/衝突時間、粒子数と独立seed誤差を分ける

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

調査時の根拠：

- `code/validated-examples/2026-11-22/particle-transport/cases.json` · dsmc-statistics.limits
- `catalog/atlas-detailed-reading.json` · dsmc.verification

- [SPARTA公式: Validation and Verification](<https://sparta.github.io/pdf/sparta_2015_validation_verification.pdf>)
  Sandia開発者の公式講習資料。Fourier/Couette流による熱流束・せん断応力検証の説明を確認。

### 平面定常衝撃波の構造（hard-sphere/VHS）

ID: dsmc-2 · P2 · 未着手 · 新規実装

調査時の範囲：未収録

調査時の現状：

均質Maxwell分子の衝突成分・平衡緩和が既存。運動量/エネルギー保存、有限Nのmicrocanonical/beta参照、64seed統計、異方性減衰を検査。空間streaming・衝突セル・物理時間の一般DSMCではない。

追加内容・最小の検証：

- 現collision roundsを物理時間と読み替えず、速度依存衝突・streaming・流入出を実装してから検証
- 密度/温度/応力のプロファイルと外部参照を固定し、Maxwell緩和とは別ケースにする

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

調査時の根拠：

- `catalog/atlas-methods.json` · dsmc.limitations
- `code/validated-examples/2026-11-22/particles/cases.json` · dsmc.assumptions

- [SPARTA公式: Validation and Verification](<https://sparta.github.io/pdf/sparta_2015_validation_verification.pdf>)
  Sandia開発者の公式講習資料。Fourier/Couette流による熱流束・せん断応力検証の説明を確認。

## LBM・格子Boltzmann

### Ghia lid-driven cavity（まずRe=100）

ID: lbm-1 · P1 · 未着手 · 新規実装

調査時の範囲：未収録

調査時の現状：

D2Q9等温BGK、Guo外力の半刻み運動量補正、half-way bounce-backが実装済み。周期せん断波粘性の細分化と低Mach平板Poiseuille壁位置/格子細分化テストがある。BGK/Guo/Poiseuille自体を不足扱いしない。

追加内容・最小の検証：

- 移動壁条件・中心線速度・主渦位置と格子細分化を追加
- 壁端の特異性やMach数圧縮性誤差を記録し、既存静止壁Poiseuilleと区別

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

調査時の根拠：

- `code/numerical-methods-atlas/2026-11-21/numart/lattice_boltzmann.py` · step(walls=True)は静止壁
- `code/numerical-methods-atlas/2026-11-21/tests/test_new_models.py` · 既存3件のLBMテスト

- [Ghia, Ghia & Shin (1982), High-Re solutions for incompressible flow ...](<https://www.sciencedirect.com/science/article/abs/pii/0021999182900584>)
  原著出版社の書誌と抄録を確認。cavityベンチマークの原著であり、LBM原著ではない。

### LBM版2D Taylor–Green渦の時間・空間・Mach数誤差

ID: lbm-2 · P1 · 未着手 · 検証の拡充

調査時の範囲：検証範囲不足

調査時の現状：

D2Q9等温BGK、Guo外力の半刻み運動量補正、half-way bounce-backが実装済み。周期せん断波粘性の細分化と低Mach平板Poiseuille壁位置/格子細分化テストがある。BGK/Guo/Poiseuille自体を不足扱いしない。

追加内容・最小の検証：

- せん断単一モードに加え、非線形移流と粘性を含む低Mach渦で速度/圧力誤差を分離
- 別系統の既存Taylor–Green投影法をLBMの検証とみなさない

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

調査時の根拠：

- `code/numerical-methods-atlas/2026-11-21/numart/lattice_boltzmann.py` · shear_wave
- `catalog/atlas-execution-examples.json` · taylor-greenはprojection法


### 円柱後流／曲面境界のSchäfer–Turek型基準問題

ID: lbm-3 · P2 · 未着手 · 新規実装

調査時の範囲：未収録

調査時の現状：

D2Q9等温BGK、Guo外力の半刻み運動量補正、half-way bounce-backが実装済み。周期せん断波粘性の細分化と低Mach平板Poiseuille壁位置/格子細分化テストがある。BGK/Guo/Poiseuille自体を不足扱いしない。

追加内容・最小の検証：

- まず定常低Reで抗力・圧力差を比較し、曲面壁の配置誤差を検査
- 既存half-way平板壁のみの検査から任意曲面精度を主張しない

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

調査時の根拠：

- `code/numerical-methods-atlas/2026-11-21/numart/lattice_boltzmann.py` · step,poiseuille


## 放射輸送

### 等方散乱平板の多重散乱ベンチマーク

ID: radiation-1 · P1 · 未着手 · 検証の拡充

調査時の範囲：検証範囲不足

調査時の現状：

定常・一様・純吸収平板の離散角法があり、Beer–Lambert/E3、空間/角度細分化、正値性・流束収支を検証。追加版は光子生存Monte Carlo、二項参照と有限seedのClopper–Pearson被覆まである。散乱・放射物質連成は別範囲。

追加内容・最小の検証：

- 単一散乱アルベドと光学的厚さを変え、透過・反射・吸収収支を独立輸送解と比較
- 純吸収E3の合格を散乱やDISORT全機能の検証へ広げない

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

調査時の根拠：

- `code/validated-examples/2026-11-22/particles/cases.json` · radiation-transport.limits

- [Su & Olson (1997), An analytical benchmark for non-equilibrium radiative transfer ...](<https://www.sciencedirect.com/science/article/abs/pii/S0306454996001004>)
  原著出版社抄録で等方散乱・非平衡輸送の解析ベンチマークを確認。1996拡散問題と1997輸送問題を区別する。

### Su–Olson非平衡放射輸送／Marshak波

ID: radiation-2 · P2 · 未着手 · 新規実装

調査時の範囲：未収録

調査時の現状：

定常・一様・純吸収平板の離散角法があり、Beer–Lambert/E3、空間/角度細分化、正値性・流束収支を検証。追加版は光子生存Monte Carlo、二項参照と有限seedのClopper–Pearson被覆まである。散乱・放射物質連成は別範囲。

追加内容・最小の検証：

- Su–Olsonの1997輸送解と拡散近似版を区別し、時間依存・物質エネルギー交換を検証
- 熱平衡接近、全エネルギー収支、光学的厚い極限を別指標にする

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

調査時の根拠：

- `catalog/atlas-depth.json` · transport.next
- `catalog/atlas-methods.json` · radiation-transport.limitations

- [Su & Olson (1997), An analytical benchmark for non-equilibrium radiative transfer ...](<https://www.sciencedirect.com/science/article/abs/pii/S0306454996001004>)
  原著出版社抄録で等方散乱・非平衡輸送の解析ベンチマークを確認。1996拡散問題と1997輸送問題を区別する。

### 影形成・交差ビームの多次元輸送（M1の限界も表示）

ID: radiation-3 · P2 · 未着手 · 新規実装

調査時の範囲：未収録

調査時の現状：

定常・一様・純吸収平板の離散角法があり、Beer–Lambert/E3、空間/角度細分化、正値性・流束収支を検証。追加版は光子生存Monte Carlo、二項参照と有限seedのClopper–Pearson被覆まである。散乱・放射物質連成は別範囲。

追加内容・最小の検証：

- 純吸収平板以外の角度構造を持つ2D固定入力を設ける
- 離散角解とmoment closureを混同せず、影の漏れ・交差後の角度情報を比較

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

調査時の根拠：

- `catalog/atlas-methods.json` · radiation-transport
- `catalog/atlas-depth.json` · transport.next


## 確率MC・MCMC・SDE

### GBM/OUのweak誤差と信頼区間を分けた固定入力

ID: stochastic-1 · P1 · 未着手 · 検証の拡充

調査時の範囲：検証範囲不足

調査時の現状：

MCのx²積分は256独立seedでN^-1/2と区間被覆、SDEは共通Brown経路4096本のGBM strong収束が既存。MCMCは正規標的に加え1D二峰標的の混合失敗/偽安心と反射提案、rank/folded Rhat・bulk/tail ESS、ArviZ 0.20.0による62同一データ照合まである。診断や多峰性が全くないという不足扱いは誤り。

追加内容・最小の検証：

- GBM strong収束の既存経路比較とは別に、期待値・分散等のweak収束を反復seedで測る
- OU/Langevinの別章既存例を未実装扱いせず、一般SDE章のweak次数の主張を独立に検査

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

調査時の根拠：

- `catalog/atlas-methods.json` · sde.limitations
- `catalog/atlas-detailed-reading.json` · sde.verification

- [Higham (2001), An Algorithmic Introduction to Numerical Simulation of SDEs](<https://epubs.siam.org/doi/10.1137/S0036144500378302>)
  SIAMの原論文ページでEM・Milstein・strong/weak convergenceの扱いを確認。

### 正規尾確率などのimportance sampling／分散削減

ID: stochastic-2 · P1 · 未着手 · 新規実装

調査時の範囲：未収録

調査時の現状：

MCのx²積分は256独立seedでN^-1/2と区間被覆、SDEは共通Brown経路4096本のGBM strong収束が既存。MCMCは正規標的に加え1D二峰標的の混合失敗/偽安心と反射提案、rank/folded Rhat・bulk/tail ESS、ArviZ 0.20.0による62同一データ照合まである。診断や多峰性が全くないという不足扱いは誤り。

追加内容・最小の検証：

- 既知erfc参照を持つ稀な事象で、推定量の不偏性と重み・実測分散・区間被覆を確認
- 単なる一様x²積分やMCMC診断と区別

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

調査時の根拠：

- `catalog/atlas-execution-examples.json` · mc-integral.scope
- `catalog/atlas-detailed-reading.json` · monte-carlo.verificationは提案、全て実行済みではない


### 相関多変量Gaussian／banana・funnel型標的

ID: stochastic-3 · P2 · 未着手 · 検証の拡充

調査時の範囲：検証範囲不足

調査時の現状：

MCのx²積分は256独立seedでN^-1/2と区間被覆、SDEは共通Brown経路4096本のGBM strong収束が既存。MCMCは正規標的に加え1D二峰標的の混合失敗/偽安心と反射提案、rank/folded Rhat・bulk/tail ESS、ArviZ 0.20.0による62同一データ照合まである。診断や多峰性が全くないという不足扱いは誤り。

追加内容・最小の検証：

- 既存1D対称二峰とは異なる相関・次元・局所スケールで診断の限界を示す
- 標的の既知モーメント/変数変換・量別MCSEを確認。HMC/NUTSの導入そのものを必須にはしない

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

調査時の根拠：

- `catalog/atlas-depth.json` · probability.next
- `code/validated-examples/2026-11-22/mcmc/cases.json` · mcmc-multimodal-mixing.limits

- [Hoffman & Gelman (2014), The No-U-Turn Sampler](<https://www.jmlr.org/papers/v15/hoffman14a.html>)
  JMLR原著ページで高次元・相関のある標的に対する比較の動機を確認。NUTS実装を今回必須とするものではない。

### Milstein法のGBM strong次数比較

ID: stochastic-4 · P2 · 未着手 · 新規実装

調査時の範囲：未収録

調査時の現状：

MCのx²積分は256独立seedでN^-1/2と区間被覆、SDEは共通Brown経路4096本のGBM strong収束が既存。MCMCは正規標的に加え1D二峰標的の混合失敗/偽安心と反射提案、rank/folded Rhat・bulk/tail ESS、ArviZ 0.20.0による62同一データ照合まである。診断や多峰性が全くないという不足扱いは誤り。

追加内容・最小の検証：

- 既存EMと同じBrown経路でstrong 1/2と1を比較
- 正値性や非Lipschitz系へ一般化せず、まず解析解を持つ小例に限定

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

調査時の根拠：

- `catalog/atlas-methods.json` · sde.example_scope
- `catalog/atlas-execution-examples.json` · gbm-sde

- [Higham (2001), An Algorithmic Introduction to Numerical Simulation of SDEs](<https://epubs.siam.org/doi/10.1137/S0036144500378302>)
  SIAMの原論文ページでEM・Milstein・strong/weak convergenceの扱いを確認。

## Maxwell・FDTD

### Mie散乱（まず2D円柱、用途があれば3D球）

ID: maxwell-fdtd-1 · P2 · 未着手 · 新規実装

調査時の範囲：未収録

調査時の現状：

最新r6は108テスト、8固定入力。periodic-wave、pec-cavity、dielectric-interface、pml-pulse、pml-corners、dielectric-oblique、p-polarization（Brewster/TIRを含む）、loss-dispersionがある。真空平面波/空洞固有振動/Fresnel/PMLを不足扱いしない。r6の損失分散は1D垂直入射のOhmic・単一受動Lorentz板。

追加内容・最小の検証：

- 既存平面界面とは異なる曲面・散乱断面積を解析級数と比較
- 2D円柱と3D球の参照式を区別し、格子曲面近似・入射場除去・流束積分を検査

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

調査時の根拠：

- `code/fdtd/2026-11-22-r6/inputs` · 既存8入力に曲面散乱はない

- [Meep公式: Mie Scattering of a Lossless Dielectric Sphere](<https://meep.readthedocs.io/en/latest/Scheme_Tutorials/Basics/>)
  球の散乱効率を解析Mie解と比較する公式例を確認。2D円柱への縮小は提案で、球の式を円柱へ流用しない。

### 損失・Lorentz分散板への斜め入射Fresnel

ID: maxwell-fdtd-2 · P2 · 未着手 · 検証の拡充

調査時の範囲：検証範囲不足

調査時の現状：

最新r6は108テスト、8固定入力。periodic-wave、pec-cavity、dielectric-interface、pml-pulse、pml-corners、dielectric-oblique、p-polarization（Brewster/TIRを含む）、loss-dispersionがある。真空平面波/空洞固有振動/Fresnel/PMLを不足扱いしない。r6の損失分散は1D垂直入射のOhmic・単一受動Lorentz板。

追加内容・最小の検証：

- 既存r5の無損失s/p斜め入射とr6の1D分散垂直入射を単に合体しただけでは検証済みにしない
- 複素角/波数、R/T/直接散逸/物質エネルギーを帯域参照で比較

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

調査時の根拠：

- `code/fdtd/2026-11-22-r6/README.md` · r6 scope
- `code/fdtd/2026-11-22-r6/inputs/loss-dispersion.json`

- [Meep公式: Materials](<https://meep.readthedocs.io/en/latest/Materials/>)
  Lorentz分極・導電率の規約と分散媒質/PML併用時の安定性注意を確認。既存r6はMeepと導電率・更新法の規約が異なる。

### PMLの浅い入射角・長時間・分散媒質との併用

ID: maxwell-fdtd-3 · P2 · 未着手 · 検証の拡充

調査時の範囲：検証範囲不足

調査時の現状：

最新r6は108テスト、8固定入力。periodic-wave、pec-cavity、dielectric-interface、pml-pulse、pml-corners、dielectric-oblique、p-polarization（Brewster/TIRを含む）、loss-dispersionがある。真空平面波/空洞固有振動/Fresnel/PMLを不足扱いしない。r6の損失分散は1D垂直入射のOhmic・単一受動Lorentz板。

追加内容・最小の検証：

- 既存x面・四辺/角PMLは保持し、near-grazingと長時間残留を別固定入力として検査
- 分散媒質との併用で補助変数の安定性・直接仕事/散逸の解釈を確認

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

調査時の根拠：

- `catalog/atlas-methods.json` · fdtd.limitations
- `code/fdtd/2026-11-22-r6/README.md` · no dispersive PML

- [Meep公式: Materials](<https://meep.readthedocs.io/en/latest/Materials/>)
  Lorentz分極・導電率の規約と分散媒質/PML併用時の安定性注意を確認。既存r6はMeepと導電率・更新法の規約が異なる。

## 線形代数・連立一次方程式

### 一般直接法の独立教材：部分ピボット LU・Cholesky と反復改良

ID: linear-algebra-1 · P1 · 未着手 · 新規実装

調査時の範囲：未収録

調査時の現状：

Thomas、定常反復、CG、GMRES/BiCGSTAB、Jacobi/ILU0、幾何 MG、平滑化集約 AMG、QR/SVD がある。AMG の正方 Poisson・異方性・条件数診断と、QR/SVD の独立 LAPACK・80/120桁参照まで保存済み。

追加内容・最小の検証：

- 小さい SPD、ほぼ特異行列、Hilbert 行列、ピボット成長を示す Wilkinson 型行列を固定入力化
- 残差・成分別後退誤差・前進誤差・条件数を分け、LAPACK と比較

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

既存コード内部の numpy/scipy solve 利用はある。独立した手法章・検証例の不足。

調査時の根拠：

- `catalog/atlas-methods.json` · cg/gmres/bicgstab/ilu0/amg/qr-svd
- `code/validated-examples/2026-11-22/foundations/cases.json` · sa-amg/qr-svd-factorization
- `code/validated-examples/2026-11-22/foundations-conditioning/cases.json` · amg-conditioning/qr-svd-conditioning

- [LAPACK Users Guide: Linear Equations](<https://netlib.org/lapack/lug/node38.html>)
  公式資料の該当機能・適用範囲を確認。全文・全証明の監査ではない。
- [PETSc KSP manual](<https://petsc.org/release/manual/ksp/>)
  公式資料の該当機能・適用範囲を確認。全文・全証明の監査ではない。

### 鞍点系・対称不定値系：MINRES とブロック前処理

ID: linear-algebra-2 · P2 · 未着手 · 新規実装

調査時の範囲：未収録

調査時の現状：

Thomas、定常反復、CG、GMRES/BiCGSTAB、Jacobi/ILU0、幾何 MG、平滑化集約 AMG、QR/SVD がある。AMG の正方 Poisson・異方性・条件数診断と、QR/SVD の独立 LAPACK・80/120桁参照まで保存済み。

追加内容・最小の検証：

- 小さい混合 Poisson/Stokes 型ブロック系で、CG の適用外を示す
- MINRES/GMRES と Schur 補前処理を同じ収束基準で比較

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

調査時の根拠：

- `catalog/atlas-methods.json` · cg/gmres/bicgstab/ilu0/amg/qr-svd
- `code/validated-examples/2026-11-22/foundations/cases.json` · sa-amg/qr-svd-factorization
- `code/validated-examples/2026-11-22/foundations-conditioning/cases.json` · amg-conditioning/qr-svd-conditioning

- [LAPACK Users Guide: Linear Equations](<https://netlib.org/lapack/lug/node38.html>)
  公式資料の該当機能・適用範囲を確認。全文・全証明の監査ではない。
- [PETSc KSP manual](<https://petsc.org/release/manual/ksp/>)
  公式資料の該当機能・適用範囲を確認。全文・全証明の監査ではない。

## 固有値・特異値問題

### 再始動 Krylov と shift-invert による内部固有値

ID: eigenvalues-1 · P1 · 未着手 · 検証の拡充

調査時の範囲：検証範囲不足

調査時の現状：

再始動なし Arnoldi/Lanczos、直交性・残差・happy breakdown、ギャップ縮小・非正規性・部分空間診断がある。分子 HF では一般化密行列固有値問題 eigh(F,S) も既に使用。

追加内容・最小の検証：

- 離散 Laplacian の既知スペクトルで端点・内部固有値を比較
- 再始動長、行列作用回数、shift 線形解法の誤差・失敗を記録

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

再始動なしの既存 Arnoldi/Lanczos を未収録扱いしない。

調査時の根拠：

- `catalog/atlas-methods.json` · eigensolvers/qr-svd
- `code/validated-examples/2026-11-22/foundations/cases.json` · krylov-eigenvalues
- `code/validated-examples/2026-11-22/foundations-conditioning/cases.json` · krylov-eigen-conditioning/qr-svd-conditioning
- `code/molecular-hf/2026-11-22/molecular_hf.py` · eigh(F,S)

- [SLEPc: EPS eigensolver manual](<https://slepc.upv.es/release/documentation/manual/eps.html>)
  公式資料の該当機能・適用範囲を確認。全文・全証明の監査ではない。
- [SLEPc: Krylov-Schur](<https://slepc.upv.es/release/manualpages/EPS/EPSKRYLOVSCHUR.html>)
  公式資料の該当機能・適用範囲を確認。全文・全証明の監査ではない。

### 質量行列付き一般化固有値の独立検証例

ID: eigenvalues-2 · P2 · 未着手 · 検証の拡充

調査時の範囲：検証範囲不足

調査時の現状：

再始動なし Arnoldi/Lanczos、直交性・残差・happy breakdown、ギャップ縮小・非正規性・部分空間診断がある。分子 HF では一般化密行列固有値問題 eigh(F,S) も既に使用。

追加内容・最小の検証：

- 1D FEM 弦振動 Kx=λMx で M 直交性・残差と既知固有値への収束を確認
- 小さな dense eigh を参照、一般化 Krylov/LOBPCG を比較

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

一般化固有値の利用自体は分子 HF にある。

調査時の根拠：

- `catalog/atlas-methods.json` · eigensolvers/qr-svd
- `code/validated-examples/2026-11-22/foundations/cases.json` · krylov-eigenvalues
- `code/validated-examples/2026-11-22/foundations-conditioning/cases.json` · krylov-eigen-conditioning/qr-svd-conditioning
- `code/molecular-hf/2026-11-22/molecular_hf.py` · eigh(F,S)

- [SLEPc: EPS eigensolver manual](<https://slepc.upv.es/release/documentation/manual/eps.html>)
  公式資料の該当機能・適用範囲を確認。全文・全証明の監査ではない。
- [SLEPc: Krylov-Schur](<https://slepc.upv.es/release/manualpages/EPS/EPSKRYLOVSCHUR.html>)
  公式資料の該当機能・適用範囲を確認。全文・全証明の監査ではない。

### Arnoldi/Lanczos 原著の参照箇所を明示

ID: eigenvalues-3 · P3 · 未着手 · 参照・出典の整備

調査時の範囲：出典整備不足

調査時の現状：

再始動なし Arnoldi/Lanczos、直交性・残差・happy breakdown、ギャップ縮小・非正規性・部分空間診断がある。分子 HF では一般化密行列固有値問題 eigh(F,S) も既に使用。

追加内容・最小の検証：

- 既存 arnoldi1951/lanczos1950 の metadata レベルを保持し、利用する漸化式・直交化の原文範囲を追加確認

完了条件：

- 対象の本文・台帳と修正した箇所が確認できる。
- 出典・書誌・適用範囲の修正根拠と確認記録を残す。
- 実在する対象と根拠を照合してから完了にする。

数値検証の欠落ではなく、引用台帳の本文確認範囲の不足。

調査時の根拠：

- `catalog/atlas-methods.json` · eigensolvers/qr-svd
- `code/validated-examples/2026-11-22/foundations/cases.json` · krylov-eigenvalues
- `code/validated-examples/2026-11-22/foundations-conditioning/cases.json` · krylov-eigen-conditioning/qr-svd-conditioning
- `code/molecular-hf/2026-11-22/molecular_hf.py` · eigh(F,S)

- [SLEPc: EPS eigensolver manual](<https://slepc.upv.es/release/documentation/manual/eps.html>)
  公式資料の該当機能・適用範囲を確認。全文・全証明の監査ではない。
- [SLEPc: Krylov-Schur](<https://slepc.upv.es/release/manualpages/EPS/EPSKRYLOVSCHUR.html>)
  公式資料の該当機能・適用範囲を確認。全文・全証明の監査ではない。

## 非線形方程式・大域化

### Bratu の折り返し点・上下枝をたどる擬似弧長継続

ID: nonlinear-1 · P1 · 未着手 · 新規実装

調査時の範囲：未収録

調査時の現状：

Bratu の減衰 Newton、十分減少線探索、組み立て Jacobian と GMRES/ILU 内部解法がある。一般の matrix-free Jv・trust region・continuation は atlas-methods の制限に明記。

追加内容・最小の検証：

- 既存解析解族を用いて λ 最大付近の上下枝と折り返しを照合
- 固定 λ Newton の失敗と、継続ステップ・接線・特異値の変化を保存

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

調査時の根拠：

- `catalog/atlas-methods.json` · newton/newton-krylov
- `numerical-methods-atlas/ja/read/sparse-nonlinear/index.html` · Bratu
- `code/numerical-methods-atlas/2026-11-21/numart/krylov.py`

- [PETSc SNES: nonlinear solvers](<https://petsc.org/release/manual/snes/>)
  公式資料の該当機能・適用範囲を確認。全文・全証明の監査ではない。

### 真の matrix-free JFNK と inexact Newton forcing

ID: nonlinear-2 · P2 · 未着手 · 新規実装

調査時の範囲：未収録

調査時の現状：

Bratu の減衰 Newton、十分減少線探索、組み立て Jacobian と GMRES/ILU 内部解法がある。一般の matrix-free Jv・trust region・continuation は atlas-methods の制限に明記。

追加内容・最小の検証：

- 解析 Jv・有限差分 Jv・AD Jv を既存 Bratu で比較
- 線形許容誤差と非線形収束、関数評価回数・停止理由を記録

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

既存 newton-krylov は assembled Jacobian。名称だけで JFNK 実装済みと解釈しない。

調査時の根拠：

- `catalog/atlas-methods.json` · newton/newton-krylov
- `numerical-methods-atlas/ja/read/sparse-nonlinear/index.html` · Bratu
- `code/numerical-methods-atlas/2026-11-21/numart/krylov.py`

- [PETSc SNES: nonlinear solvers](<https://petsc.org/release/manual/snes/>)
  公式資料の該当機能・適用範囲を確認。全文・全証明の監査ではない。

### 信頼領域と線探索の難しい初期値比較

ID: nonlinear-3 · P2 · 未着手 · 新規実装

調査時の範囲：未収録

調査時の現状：

Bratu の減衰 Newton、十分減少線探索、組み立て Jacobian と GMRES/ILU 内部解法がある。一般の matrix-free Jv・trust region・continuation は atlas-methods の制限に明記。

追加内容・最小の検証：

- Bratu と小さいスケール不良の連立系で同じ初期値集合を使用
- 失敗・特異 Jacobian・停滞を区別して保存

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

調査時の根拠：

- `catalog/atlas-methods.json` · newton/newton-krylov
- `numerical-methods-atlas/ja/read/sparse-nonlinear/index.html` · Bratu
- `code/numerical-methods-atlas/2026-11-21/numart/krylov.py`

- [PETSc SNES: nonlinear solvers](<https://petsc.org/release/manual/snes/>)
  公式資料の該当機能・適用範囲を確認。全文・全証明の監査ではない。

## 自動微分

### 逆モード VJP の実装と JVP/VJP 双対性検査

ID: automatic-differentiation-1 · P1 · 未着手 · 新規実装

調査時の範囲：解説のみ

調査時の現状：

独自の forward dual-number、JVP/Jacobian と解析微分・有限差分の Bratu 比較は実装・配布・検証済み。逆モード/VJP/HVP は章内説明がある。

追加内容・最小の検証：

- Bratu 残差で dot(Jv,w)=dot(v,Jᵀw) を解析値・方向差分と比較
- 複数出力/多数入力で評価回数とメモリを比較

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

調査時の根拠：

- `catalog/atlas-methods.json` · automatic-differentiation
- `numerical-methods-atlas/ja/read/automatic-differentiation/index.html`
- `code/autodiff/2026-11-22/numart/autodiff.py`

- [JAX advanced automatic differentiation](<https://docs.jax.dev/en/latest/301/index.html>)
  公式資料の該当機能・適用範囲を確認。全文・全証明の監査ではない。

### Hessian-vector 積・二階微分の検証

ID: automatic-differentiation-2 · P2 · 未着手 · 新規実装

調査時の範囲：解説のみ

調査時の現状：

独自の forward dual-number、JVP/Jacobian と解析微分・有限差分の Bratu 比較は実装・配布・検証済み。逆モード/VJP/HVP は章内説明がある。

追加内容・最小の検証：

- 小さな既知二次関数と Bratu 目的関数で HVP を照合
- 状態を固定した偏微分と陰関数を通る全微分を区別

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

調査時の根拠：

- `catalog/atlas-methods.json` · automatic-differentiation
- `numerical-methods-atlas/ja/read/automatic-differentiation/index.html`
- `code/autodiff/2026-11-22/numart/autodiff.py`

- [JAX advanced automatic differentiation](<https://docs.jax.dev/en/latest/301/index.html>)
  公式資料の該当機能・適用範囲を確認。全文・全証明の監査ではない。

### 分岐・非滑らか演算と微分の適用範囲

ID: automatic-differentiation-3 · P2 · 未着手 · 検証の拡充

調査時の範囲：検証範囲不足

調査時の現状：

独自の forward dual-number、JVP/Jacobian と解析微分・有限差分の Bratu 比較は実装・配布・検証済み。逆モード/VJP/HVP は章内説明がある。

追加内容・最小の検証：

- abs/max、箱制約境界、反復停止条件を含む簡単な例で方向依存・失敗を表示
- 離散化された滑らかな残差の微分と、アルゴリズム分岐の微分を区別

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

調査時の根拠：

- `catalog/atlas-methods.json` · automatic-differentiation
- `numerical-methods-atlas/ja/read/automatic-differentiation/index.html`
- `code/autodiff/2026-11-22/numart/autodiff.py`

- [JAX advanced automatic differentiation](<https://docs.jax.dev/en/latest/301/index.html>)
  公式資料の該当機能・適用範囲を確認。全文・全証明の監査ではない。

## 陰関数微分・感度・随伴法

### 時間依存問題の離散随伴と checkpointing

ID: sensitivity-adjoint-1 · P2 · 未着手 · 新規実装

調査時の範囲：未収録

調査時の現状：

Bratu の陰関数感度と離散随伴、解析パラメータ微分、有限差分、前進/随伴一致がある。現在の実例は定常・小規模密行列で、逆問題も一つ又は二つのパラメータ。

追加内容・最小の検証：

- 小さい拡散 ODE 半離散系又は既知線形 ODE の終端目的関数を使用
- 前進感度・離散随伴・方向差分を照合し、保存全軌道と checkpoint 再計算を比較

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

調査時の根拠：

- `catalog/atlas-methods.json` · adjoint
- `numerical-methods-atlas/ja/read/adjoint/index.html`
- `code/bratu-sensitivity/2026-11-22/numart/bratu_sensitivity.py`
- `code/bratu-multinverse/2026-11-22/numart/bratu_multinverse.py`

- [SUNDIALS CVODES adjoint usage](<https://sundials.readthedocs.io/en/latest/cvodes/Usage/ADJ.html>)
  公式資料の該当機能・適用範囲を確認。全文・全証明の監査ではない。
- [JAX advanced automatic differentiation](<https://docs.jax.dev/en/latest/301/index.html>)
  公式資料の該当機能・適用範囲を確認。全文・全証明の監査ではない。

### 折り返し・悪条件下での感度と解法許容誤差

ID: sensitivity-adjoint-2 · P1 · 未着手 · 検証の拡充

調査時の範囲：検証範囲不足

調査時の現状：

Bratu の陰関数感度と離散随伴、解析パラメータ微分、有限差分、前進/随伴一致がある。現在の実例は定常・小規模密行列で、逆問題も一つ又は二つのパラメータ。

追加内容・最小の検証：

- Bratu 臨界 λ へ近づく列で最小特異値、感度、差分刻み依存を保存
- 状態/随伴線形残差が勾配誤差へ与える影響を分離

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

調査時の根拠：

- `catalog/atlas-methods.json` · adjoint
- `numerical-methods-atlas/ja/read/adjoint/index.html`
- `code/bratu-sensitivity/2026-11-22/numart/bratu_sensitivity.py`
- `code/bratu-multinverse/2026-11-22/numart/bratu_multinverse.py`

- [SUNDIALS CVODES adjoint usage](<https://sundials.readthedocs.io/en/latest/cvodes/Usage/ADJ.html>)
  公式資料の該当機能・適用範囲を確認。全文・全証明の監査ではない。
- [JAX advanced automatic differentiation](<https://docs.jax.dev/en/latest/301/index.html>)
  公式資料の該当機能・適用範囲を確認。全文・全証明の監査ではない。

### 多数の空間パラメータへの行列非形成 VJP 展開

ID: sensitivity-adjoint-3 · P2 · 未着手 · 検証の拡充

調査時の範囲：検証範囲不足

調査時の現状：

Bratu の陰関数感度と離散随伴、解析パラメータ微分、有限差分、前進/随伴一致がある。現在の実例は定常・小規模密行列で、逆問題も一つ又は二つのパラメータ。

追加内容・最小の検証：

- 二つの基底から小さな分布係数へ拡張し、全 Jacobian を作る場合と比較
- 目的関数数とパラメータ数を区別して作業量を測定

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

調査時の根拠：

- `catalog/atlas-methods.json` · adjoint
- `numerical-methods-atlas/ja/read/adjoint/index.html`
- `code/bratu-sensitivity/2026-11-22/numart/bratu_sensitivity.py`
- `code/bratu-multinverse/2026-11-22/numart/bratu_multinverse.py`

- [SUNDIALS CVODES adjoint usage](<https://sundials.readthedocs.io/en/latest/cvodes/Usage/ADJ.html>)
  公式資料の該当機能・適用範囲を確認。全文・全証明の監査ではない。
- [JAX advanced automatic differentiation](<https://docs.jax.dev/en/latest/301/index.html>)
  公式資料の該当機能・適用範囲を確認。全文・全証明の監査ではない。

## 逆問題・最適化・正則化

### Gauss–Newton/Levenberg–Marquardt と境界付き最小二乗

ID: inverse-optimization-1 · P1 · 未着手 · 新規実装

調査時の範囲：未収録

調査時の現状：

Bratu λ 推定、二パラメータ空間係数推定、箱制約投影勾配・Armijo、Tikhonov 正則化とデータのみの感度 SVD による識別可能性を実装済み。BFGS と Rosenbrock の検証案は章にあるが未実行。SVD 診断は統計的 Fisher 情報・厳密 Hessian とは呼んでいない。

追加内容・最小の検証：

- 既存二パラメータ Bratu で投影勾配と同じ観測・誤差基準で比較
- 重み・変数スケーリング・悪条件感度の下で停止理由と線形解法を保存

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

調査時の根拠：

- `catalog/atlas-methods.json` · optimization
- `numerical-methods-atlas/ja/read/optimization/index.html`
- `numerical-methods-atlas/ja/read/bratu-inverse/index.html`
- `numerical-methods-atlas/ja/read/bratu-multi-inverse/index.html`
- `code/bratu-multinverse/2026-11-22/numart/bratu_multinverse.py`
- `numerical-methods-atlas/references.json` · fletcher1970

- [SciPy least_squares official documentation](<https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.least_squares.html>)
  公式資料の該当機能・適用範囲を確認。全文・全証明の監査ではない。

### BFGS/L-BFGS と標準 Rosenbrock 問題の固定検証

ID: inverse-optimization-2 · P2 · 未着手 · 新規実装

調査時の範囲：解説のみ

調査時の現状：

Bratu λ 推定、二パラメータ空間係数推定、箱制約投影勾配・Armijo、Tikhonov 正則化とデータのみの感度 SVD による識別可能性を実装済み。BFGS と Rosenbrock の検証案は章にあるが未実行。SVD 診断は統計的 Fisher 情報・厳密 Hessian とは呼んでいない。

追加内容・最小の検証：

- 既知 SPD 二次関数と Rosenbrock の複数初期値で勾配検査・曲率条件を保存
- 準 Newton と正則化逆問題の役割を区別。Fletcher1970 は現状 metadata のため利用箇所を補足

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

調査時の根拠：

- `catalog/atlas-methods.json` · optimization
- `numerical-methods-atlas/ja/read/optimization/index.html`
- `numerical-methods-atlas/ja/read/bratu-inverse/index.html`
- `numerical-methods-atlas/ja/read/bratu-multi-inverse/index.html`
- `code/bratu-multinverse/2026-11-22/numart/bratu_multinverse.py`
- `numerical-methods-atlas/references.json` · fletcher1970

- [SciPy least_squares official documentation](<https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.least_squares.html>)
  公式資料の該当機能・適用範囲を確認。全文・全証明の監査ではない。

### ノイズ・離散化不一致下の正則化選択と推定不確かさ

ID: inverse-optimization-3 · P1 · 未着手 · 検証の拡充

調査時の範囲：検証範囲不足

調査時の現状：

Bratu λ 推定、二パラメータ空間係数推定、箱制約投影勾配・Armijo、Tikhonov 正則化とデータのみの感度 SVD による識別可能性を実装済み。BFGS と Rosenbrock の検証案は章にあるが未実行。SVD 診断は統計的 Fisher 情報・厳密 Hessian とは呼んでいない。

追加内容・最小の検証：

- 観測を細かい別格子で作り、粗格子で推定して inverse crime を分離
- 固定ノイズの少数反復、discrepancy/L-curve などの γ 選択、推定偏りと安定性を検証
- 局所線形共分散を出すなら仮定を明示し、既存 data-only SVD を統計保証に読み替えない

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

調査時の根拠：

- `catalog/atlas-methods.json` · optimization
- `numerical-methods-atlas/ja/read/optimization/index.html`
- `numerical-methods-atlas/ja/read/bratu-inverse/index.html`
- `numerical-methods-atlas/ja/read/bratu-multi-inverse/index.html`
- `code/bratu-multinverse/2026-11-22/numart/bratu_multinverse.py`
- `numerical-methods-atlas/references.json` · fletcher1970

- [SciPy least_squares official documentation](<https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.least_squares.html>)
  公式資料の該当機能・適用範囲を確認。全文・全証明の監査ではない。

## ODE・時間積分

### 標準 stiff ベンチマーク：Robertson 反応系と van der Pol

ID: ode-time-1 · P1 · 未着手 · 新規実装

調査時の範囲：未収録

調査時の現状：

Euler/Heun/midpoint/Ralston/Kutta3/RK4/SSPRK、BDF2/SDIRK2/IMEX Euler、step doubling と非自律製造解、幾何積分がある。新規 Lie/Strang は有限振幅 Schnakenberg の同一空間離散に対する Radau/DOP853 独立時間参照で検証済み。

追加内容・最小の検証：

- 軽い固定 μ・時区間だけを用い、stiffness 遷移、保存量/正値性、許容誤差と実誤差を比較
- BDF2/SDIRK2 と独立 Radau/BDF を比較し、Jacobian 再利用と失敗記録を残す

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

調査時の根拠：

- `catalog/atlas-methods.json` · bdf2/sdirk2/imex-euler/step-doubling/lie-trotter/strang-splitting
- `code/numerical-methods-atlas/2026-11-21/numart/time_integration.py`
- `code/numerical-methods-atlas/2026-11-21/numart/stiff.py`
- `code/validated-examples/2026-11-22/splitting/cases.json` · reaction-diffusion-splitting

- [SciPy solve_ivp official documentation](<https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html>)
  公式資料の該当機能・適用範囲を確認。全文・全証明の監査ではない。
- [SUNDIALS IDA mathematical considerations](<https://sundials.readthedocs.io/en/latest/ida/Mathematics_link.html>)
  公式資料の該当機能・適用範囲を確認。全文・全証明の監査ではない。

### 埋込み RK45・dense output・イベント位置決め

ID: ode-time-2 · P1 · 未着手 · 新規実装

調査時の範囲：未収録

調査時の現状：

Euler/Heun/midpoint/Ralston/Kutta3/RK4/SSPRK、BDF2/SDIRK2/IMEX Euler、step doubling と非自律製造解、幾何積分がある。新規 Lie/Strang は有限振幅 Schnakenberg の同一空間離散に対する Radau/DOP853 独立時間参照で検証済み。

追加内容・最小の検証：

- 既知交差時刻を持つ減衰振動または落下問題で補間誤差とイベント時刻を照合
- 受理/棄却ステップ、相対/絶対許容誤差、最大刻み依存を保存

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

調査時の根拠：

- `catalog/atlas-methods.json` · bdf2/sdirk2/imex-euler/step-doubling/lie-trotter/strang-splitting
- `code/numerical-methods-atlas/2026-11-21/numart/time_integration.py`
- `code/numerical-methods-atlas/2026-11-21/numart/stiff.py`
- `code/validated-examples/2026-11-22/splitting/cases.json` · reaction-diffusion-splitting

- [SciPy solve_ivp official documentation](<https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html>)
  公式資料の該当機能・適用範囲を確認。全文・全証明の監査ではない。
- [SUNDIALS IDA mathematical considerations](<https://sundials.readthedocs.io/en/latest/ida/Mathematics_link.html>)
  公式資料の該当機能・適用範囲を確認。全文・全証明の監査ではない。

### 分割法の境界・時間依存と order reduction

ID: ode-time-3 · P2 · 未着手 · 検証の拡充

調査時の範囲：検証範囲不足

調査時の現状：

Euler/Heun/midpoint/Ralston/Kutta3/RK4/SSPRK、BDF2/SDIRK2/IMEX Euler、step doubling と非自律製造解、幾何積分がある。新規 Lie/Strang は有限振幅 Schnakenberg の同一空間離散に対する Radau/DOP853 独立時間参照で検証済み。

追加内容・最小の検証：

- 既存周期・固定格子 Schnakenberg の検証を保持し、非同次境界か時間依存係数を一つ追加
- 時間誤差と空間誤差を分離し、理想的な Strang 2次が崩れる条件を記録

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

Lie/Strang 自体は収録済み。

調査時の根拠：

- `catalog/atlas-methods.json` · bdf2/sdirk2/imex-euler/step-doubling/lie-trotter/strang-splitting
- `code/numerical-methods-atlas/2026-11-21/numart/time_integration.py`
- `code/numerical-methods-atlas/2026-11-21/numart/stiff.py`
- `code/validated-examples/2026-11-22/splitting/cases.json` · reaction-diffusion-splitting

- [SciPy solve_ivp official documentation](<https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html>)
  公式資料の該当機能・適用範囲を確認。全文・全証明の監査ではない。
- [SUNDIALS IDA mathematical considerations](<https://sundials.readthedocs.io/en/latest/ida/Mathematics_link.html>)
  公式資料の該当機能・適用範囲を確認。全文・全証明の監査ではない。

### Jameson系の定常多段RKによる線形モード減衰

ID: ode-time-additional · P2 · 未着手 · 新規実装

調査時の範囲：解説のみ

調査時の現状：

Euler/Heun/midpoint/Ralston/Kutta3/RK4/SSPRK、BDF2/SDIRK2/IMEX Euler、step doubling と非自律製造解、幾何積分がある。新規 Lie/Strang は有限振幅 Schnakenberg の同一空間離散に対する Radau/DOP853 独立時間参照で検証済み。

追加内容・最小の検証：

- 既存steady-runge-kutta章の基準状態型多段式と安定性多項式を、小さい線形問題の残差減衰で照合する。
- 古典RK4の非定常4次精度、擬似時間の収束、非線形定常ソルバーの大域収束を区別する。

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

調査時の根拠：

- `catalog/atlas-detailed-reading.json` · steady-runge-kutta
- `numerical-methods-atlas/ja/read/steady-runge-kutta/index.html`


## 微分代数方程式 DAE

### index-1 DAE：整合初期化込みの最小実装

ID: dae-1 · P1 · 未着手 · 新規実装

調査時の範囲：解説のみ

調査時の現状：

dae は planned だが章は存在し、F(t,y,y′)=0、index-1、整合初期値、BDF Newton 行列を説明。専用の実行・保存結果はまだない。Gear の本文確認は導入・定式化範囲に限定。

追加内容・最小の検証：

- 解析解が作れる半陽的 index-1 系で微分・代数残差と全体次数を確認
- 整合/不整合初期値、初期化 Newton の成功/失敗と許容誤差を保存

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

調査時の根拠：

- `catalog/atlas-methods.json` · dae
- `numerical-methods-atlas/ja/read/dae/index.html`
- `numerical-methods-atlas/references.json` · gear1971

- [SUNDIALS IDA mathematical considerations](<https://sundials.readthedocs.io/en/latest/ida/Mathematics_link.html>)
  公式資料の該当機能・適用範囲を確認。全文・全証明の監査ではない。

### 名前付き DAE ベンチマーク：Robertson の保存則 DAE 形式

ID: dae-2 · P2 · 未着手 · 新規実装

調査時の範囲：未収録

調査時の現状：

dae は planned だが章は存在し、F(t,y,y′)=0、index-1、整合初期値、BDF Newton 行列を説明。専用の実行・保存結果はまだない。Gear の本文確認は導入・定式化範囲に限定。

追加内容・最小の検証：

- ODE 形式と一つの保存則を代数式にした index-1 形式を同じ入力で比較
- IDA を独立参照にし、濃度保存・残差・初期値整合性を別々に確認

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

調査時の根拠：

- `catalog/atlas-methods.json` · dae
- `numerical-methods-atlas/ja/read/dae/index.html`
- `numerical-methods-atlas/references.json` · gear1971

- [SUNDIALS IDA mathematical considerations](<https://sundials.readthedocs.io/en/latest/ida/Mathematics_link.html>)
  公式資料の該当機能・適用範囲を確認。全文・全証明の監査ではない。

### 高 index 系の index reduction と拘束ドリフト

ID: dae-3 · P2 · 未着手 · 新規実装

調査時の範囲：解説のみ

調査時の現状：

dae は planned だが章は存在し、F(t,y,y′)=0、index-1、整合初期値、BDF Newton 行列を説明。専用の実行・保存結果はまだない。Gear の本文確認は導入・定式化範囲に限定。

追加内容・最小の検証：

- 小さい拘束振り子で元の拘束・速度拘束・エネルギーのドリフトを表示
- 直接 index-1 と同じ扱いをしない条件を解説し、幾何積分の RATTLE へ接続

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

調査時の根拠：

- `catalog/atlas-methods.json` · dae
- `numerical-methods-atlas/ja/read/dae/index.html`
- `numerical-methods-atlas/references.json` · gear1971

- [SUNDIALS IDA mathematical considerations](<https://sundials.readthedocs.io/en/latest/ida/Mathematics_link.html>)
  公式資料の該当機能・適用範囲を確認。全文・全証明の監査ではない。

## 幾何積分・Hamilton 系

### SHAKE/RATTLE：拘束付き振り子の固定入力比較

ID: geometric-1 · P2 · 未着手 · 新規実装

調査時の範囲：未収録

調査時の現状：

symplectic Euler、Verlet、Yoshida4、implicit midpoint を harmonic/quartic Hamiltonian で比較し、エネルギー・位相・写像の構造を検査済み。単純な振動子がない、という欠落ではない。

追加内容・最小の検証：

- 位置・速度拘束残差、時間反転、エネルギー長期挙動を比較
- 拘束解法の許容誤差と時間刻み誤差を区別

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

調査時の根拠：

- `catalog/atlas-methods.json` · symplectic-euler/verlet/yoshida4
- `numerical-methods-atlas/ja/read/symplectic/index.html`
- `code/numerical-methods-atlas/2026-11-21/tests/test_time_geometry.py`

- [Hairer: Geometric Numerical Integration introductory lecture](<https://unige.ch/~hairer/poly_geoint/intro.pdf>)
  著者公開講義の拘束系・幾何積分の対象を確認。
- [Hairer: Important aspects of geometric numerical integration](<https://www.unige.ch/~hairer/preprints/hairer-pisa.pdf>)
  著者公開原稿の構造・長時間挙動・高振動問題の射程を確認。

### Kepler 問題の離心率依存と近日点誤差

ID: geometric-2 · P2 · 未着手 · 検証の拡充

調査時の範囲：検証範囲不足

調査時の現状：

symplectic Euler、Verlet、Yoshida4、implicit midpoint を harmonic/quartic Hamiltonian で比較し、エネルギー・位相・写像の構造を検査済み。単純な振動子がない、という欠落ではない。

追加内容・最小の検証：

- 既知楕円軌道で位相・角運動量・エネルギー誤差を別々に保存
- 固定刻みと安易な可変刻みで構造がどう変わるかを小規模比較

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

N体重力や軌道積分の既存例を未収録とは呼ばず、幾何積分の体系的比較枠の拡張。

調査時の根拠：

- `catalog/atlas-methods.json` · symplectic-euler/verlet/yoshida4
- `numerical-methods-atlas/ja/read/symplectic/index.html`
- `code/numerical-methods-atlas/2026-11-21/tests/test_time_geometry.py`

- [Hairer: Geometric Numerical Integration introductory lecture](<https://unige.ch/~hairer/poly_geoint/intro.pdf>)
  著者公開講義の拘束系・幾何積分の対象を確認。
- [Hairer: Important aspects of geometric numerical integration](<https://www.unige.ch/~hairer/preprints/hairer-pisa.pdf>)
  著者公開原稿の構造・長時間挙動・高振動問題の射程を確認。

### 多周波数・高振動系での共鳴と安定性限界

ID: geometric-3 · P3 · 未着手 · 検証の拡充

調査時の範囲：検証範囲不足

調査時の現状：

symplectic Euler、Verlet、Yoshida4、implicit midpoint を harmonic/quartic Hamiltonian で比較し、エネルギー・位相・写像の構造を検査済み。単純な振動子がない、という欠落ではない。

追加内容・最小の検証：

- 小さい結合振動子又は短い FPU 鎖で周波数比と刻みを限定走査
- 総エネルギーだけでなくモード間エネルギー交換を検査

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

調査時の根拠：

- `catalog/atlas-methods.json` · symplectic-euler/verlet/yoshida4
- `numerical-methods-atlas/ja/read/symplectic/index.html`
- `code/numerical-methods-atlas/2026-11-21/tests/test_time_geometry.py`

- [Hairer: Geometric Numerical Integration introductory lecture](<https://unige.ch/~hairer/poly_geoint/intro.pdf>)
  著者公開講義の拘束系・幾何積分の対象を確認。
- [Hairer: Important aspects of geometric numerical integration](<https://www.unige.ch/~hairer/preprints/hairer-pisa.pdf>)
  著者公開原稿の構造・長時間挙動・高振動問題の射程を確認。

## 数値求積

### 無限区間・振動重み・既知特異点に応じた求積選択

ID: quadrature-1 · P2 · 未着手 · 検証の拡充

調査時の範囲：検証範囲不足

調査時の現状：

Gauss–Legendre 生成・多項式モーメント、adaptive Simpson、解析 atan/QUADPACK 参照がある。追加 conditioning で狭い Lorentz、相殺、sqrt 端点、零積分、意図的に見逃す bump、推定誤差の過信まで検証済み。

追加内容・最小の検証：

- Gaussian 無限区間、sin(ωx) 型、内部特異点分割の小さな固定例を追加
- 汎用 Simpson と適切な QUADPACK 系ルーチンで評価回数・警告・実誤差を比較

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

端点 sqrt や相殺試験は既存。単に特異関数未検証とは書かない。

調査時の根拠：

- `catalog/atlas-methods.json` · quadrature
- `code/validated-examples/2026-11-22/foundations/cases.json` · gauss-adaptive-quadrature
- `code/validated-examples/2026-11-22/foundations-conditioning/cases.json` · quadrature-conditioning

- [Netlib QUADPACK source index](<https://netlib.org/quadpack/>)
  公式資料の該当機能・適用範囲を確認。全文・全証明の監査ではない。
- [Chebfun guide: Integration and Differentiation](<https://www.chebfun.org/docs/guide/guide02.html>)
  公式資料の該当機能・適用範囲を確認。全文・全証明の監査ではない。

### Gauss–Kronrod と二重指数変換の教材実装比較

ID: quadrature-2 · P2 · 未着手 · 新規実装

調査時の範囲：未収録

調査時の現状：

Gauss–Legendre 生成・多項式モーメント、adaptive Simpson、解析 atan/QUADPACK 参照がある。追加 conditioning で狭い Lorentz、相殺、sqrt 端点、零積分、意図的に見逃す bump、推定誤差の過信まで検証済み。

追加内容・最小の検証：

- 滑らかな関数と可積分端点特異性で、解析積分値・独立参照を照合
- 誤差推定は保証上界ではないことを bump 例と接続

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

調査時の根拠：

- `catalog/atlas-methods.json` · quadrature
- `code/validated-examples/2026-11-22/foundations/cases.json` · gauss-adaptive-quadrature
- `code/validated-examples/2026-11-22/foundations-conditioning/cases.json` · quadrature-conditioning

- [Netlib QUADPACK source index](<https://netlib.org/quadpack/>)
  公式資料の該当機能・適用範囲を確認。全文・全証明の監査ではない。
- [Chebfun guide: Integration and Differentiation](<https://www.chebfun.org/docs/guide/guide02.html>)
  公式資料の該当機能・適用範囲を確認。全文・全証明の監査ではない。

### 多次元求積の次元依存：テンソル積と疎格子

ID: quadrature-3 · P3 · 未着手 · 新規実装

調査時の範囲：未収録

調査時の現状：

Gauss–Legendre 生成・多項式モーメント、adaptive Simpson、解析 atan/QUADPACK 参照がある。追加 conditioning で狭い Lorentz、相殺、sqrt 端点、零積分、意図的に見逃す bump、推定誤差の過信まで検証済み。

追加内容・最小の検証：

- 2〜4次元の分離可能な既知積分値だけで軽量比較
- 標本数・次数・実誤差と相互作用項の影響を保存

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

Monte Carlo/QMC 分野と重複する場合は共同入口にする。

調査時の根拠：

- `catalog/atlas-methods.json` · quadrature
- `code/validated-examples/2026-11-22/foundations/cases.json` · gauss-adaptive-quadrature
- `code/validated-examples/2026-11-22/foundations-conditioning/cases.json` · quadrature-conditioning

- [Netlib QUADPACK source index](<https://netlib.org/quadpack/>)
  公式資料の該当機能・適用範囲を確認。全文・全証明の監査ではない。
- [Chebfun guide: Integration and Differentiation](<https://www.chebfun.org/docs/guide/guide02.html>)
  公式資料の該当機能・適用範囲を確認。全文・全証明の監査ではない。

## 補間・近似・ウェーブレット

### Runge 関数：等間隔・Chebyshev 節点と barycentric/Clenshaw 評価

ID: interpolation-approximation-1 · P1 · 未着手 · 新規実装

調査時の範囲：解説のみ

調査時の現状：

splines/chebyshev/wavelets の章・公式・引用は既存だが各 status は planned。Legendre/nodal basis、GLL と等間隔節点、L² 投影、三角形 P1/P2 と質量行列は別に実装済み。

追加内容・最小の検証：

- 1/(1+25x²) と非滑らかな |x| の独立細密点誤差を保存
- 補間・最小二乗/射影・minimax を区別し、節点上の誤差だけで判定しない

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

調査時の根拠：

- `catalog/atlas-methods.json` · splines/chebyshev/wavelets/legendre-basis/nodal-basis
- `numerical-methods-atlas/ja/read/splines/index.html`
- `numerical-methods-atlas/ja/read/chebyshev/index.html`
- `numerical-methods-atlas/ja/read/wavelets/index.html`
- `code/numerical-methods-atlas/2026-11-21/numart/basis.py`

- [SciPy BarycentricInterpolator](<https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.BarycentricInterpolator.html>)
  公式資料の該当機能・適用範囲を確認。全文・全証明の監査ではない。
- [SciPy PchipInterpolator](<https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.PchipInterpolator.html>)
  公式資料の該当機能・適用範囲を確認。全文・全証明の監査ではない。

### de Boor スプラインと PCHIP の単調データ比較

ID: interpolation-approximation-2 · P1 · 未着手 · 新規実装

調査時の範囲：解説のみ

調査時の現状：

splines/chebyshev/wavelets の章・公式・引用は既存だが各 status は planned。Legendre/nodal basis、GLL と等間隔節点、L² 投影、三角形 P1/P2 と質量行列は別に実装済み。

追加内容・最小の検証：

- 自然/端点微分指定 spline の境界条件、連続性と導関数を照合
- 単調な段差状データで overshoot・正値性・PCHIP の形状保存を検査

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

B-spline/de Boor は章にある。PCHIP は追加手法候補。

調査時の根拠：

- `catalog/atlas-methods.json` · splines/chebyshev/wavelets/legendre-basis/nodal-basis
- `numerical-methods-atlas/ja/read/splines/index.html`
- `numerical-methods-atlas/ja/read/chebyshev/index.html`
- `numerical-methods-atlas/ja/read/wavelets/index.html`
- `code/numerical-methods-atlas/2026-11-21/numart/basis.py`

- [SciPy BarycentricInterpolator](<https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.BarycentricInterpolator.html>)
  公式資料の該当機能・適用範囲を確認。全文・全証明の監査ではない。
- [SciPy PchipInterpolator](<https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.PchipInterpolator.html>)
  公式資料の該当機能・適用範囲を確認。全文・全証明の監査ではない。

### Mallat 変換・閾値化と境界拡張の実行検証

ID: interpolation-approximation-3 · P3 · 未着手 · 新規実装

調査時の範囲：解説のみ

調査時の現状：

splines/chebyshev/wavelets の章・公式・引用は既存だが各 status は planned。Legendre/nodal basis、GLL と等間隔節点、L² 投影、三角形 P1/P2 と質量行列は別に実装済み。

追加内容・最小の検証：

- 短い既知信号で完全再構成・直交系のエネルギーを確認
- 不連続信号の閾値化と周期/対称境界で誤差がどう変わるかを保存

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

調査時の根拠：

- `catalog/atlas-methods.json` · splines/chebyshev/wavelets/legendre-basis/nodal-basis
- `numerical-methods-atlas/ja/read/splines/index.html`
- `numerical-methods-atlas/ja/read/chebyshev/index.html`
- `numerical-methods-atlas/ja/read/wavelets/index.html`
- `code/numerical-methods-atlas/2026-11-21/numart/basis.py`

- [SciPy BarycentricInterpolator](<https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.BarycentricInterpolator.html>)
  公式資料の該当機能・適用範囲を確認。全文・全証明の監査ではない。
- [SciPy PchipInterpolator](<https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.PchipInterpolator.html>)
  公式資料の該当機能・適用範囲を確認。全文・全証明の監査ではない。

## PINN・ニューラル演算子

### 製造解 Poisson PINN と従来法の最小比較

ID: pinn-neural-operators-1 · P2 · 未着手 · 新規実装

調査時の範囲：解説のみ

調査時の現状：

pinn-operators 章は PINN と FNO を区別し、残差・境界・スケーリング・問題単位分割・OOD と複数 seed を説明。status planned で学習コード/保存ベンチマークなし。引用 raissi2019/li2021fno は abstract-and-metadata。

追加内容・最小の検証：

- 小さい固定ネットワークと少数 seed で、独立格子の解誤差・PDE残差・境界誤差を保存
- 学習時間/推論時間と有限差分/FEM 解法の条件を分離し、学習損失だけで合格にしない

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

調査時の根拠：

- `catalog/atlas-methods.json` · pinn-operators
- `numerical-methods-atlas/ja/read/pinn-operators/index.html`
- `numerical-methods-atlas/references.json` · raissi2019/li2021fno

- [Raissi et al.: Physics Informed Deep Learning Part I](<https://arxiv.org/abs/1711.10561>)
  著者投稿の原著 preprint の要旨・対象範囲を確認。既存2019論文そのものの全文監査とは別。
- [Li et al.: Fourier Neural Operator](<https://arxiv.org/abs/2010.08895>)
  著者投稿の原著 preprint の要旨・改訂履歴・問題族学習の対象範囲を確認。OpenReview はブラウザー検証要求のため本文未取得。

### FNO の問題単位 train/test・解像度/OOD 検証

ID: pinn-neural-operators-2 · P3 · 未着手 · 新規実装

調査時の範囲：解説のみ

調査時の現状：

pinn-operators 章は PINN と FNO を区別し、残差・境界・スケーリング・問題単位分割・OOD と複数 seed を説明。status planned で学習コード/保存ベンチマークなし。引用 raissi2019/li2021fno は abstract-and-metadata。

追加内容・最小の検証：

- 小さな周期拡散又は Burgers 族で固定データと計算予算を公開
- 同一軌道の点分割を避け、未学習パラメータ・解像度で誤差を比較

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

大規模 GPU 学習や原著全ベンチマークの再現は不要。

調査時の根拠：

- `catalog/atlas-methods.json` · pinn-operators
- `numerical-methods-atlas/ja/read/pinn-operators/index.html`
- `numerical-methods-atlas/references.json` · raissi2019/li2021fno

- [Raissi et al.: Physics Informed Deep Learning Part I](<https://arxiv.org/abs/1711.10561>)
  著者投稿の原著 preprint の要旨・対象範囲を確認。既存2019論文そのものの全文監査とは別。
- [Li et al.: Fourier Neural Operator](<https://arxiv.org/abs/2010.08895>)
  著者投稿の原著 preprint の要旨・改訂履歴・問題族学習の対象範囲を確認。OpenReview はブラウザー検証要求のため本文未取得。

### PINN/FNO の原著本文で損失・分割・適用条件の出典を補足

ID: pinn-neural-operators-3 · P3 · 未着手 · 参照・出典の整備

調査時の範囲：出典整備不足

調査時の現状：

pinn-operators 章は PINN と FNO を区別し、残差・境界・スケーリング・問題単位分割・OOD と複数 seed を説明。status planned で学習コード/保存ベンチマークなし。引用 raissi2019/li2021fno は abstract-and-metadata。

追加内容・最小の検証：

- 既存の abstract-and-metadata を上書きせず、利用する本文節・式・実験条件を追加確認
- 原著性能値を小規模教材の性能保証へ転用しない

完了条件：

- 対象の本文・台帳と修正した箇所が確認できる。
- 出典・書誌・適用範囲の修正根拠と確認記録を残す。
- 実在する対象と根拠を照合してから完了にする。

調査時の根拠：

- `catalog/atlas-methods.json` · pinn-operators
- `numerical-methods-atlas/ja/read/pinn-operators/index.html`
- `numerical-methods-atlas/references.json` · raissi2019/li2021fno

- [Raissi et al.: Physics Informed Deep Learning Part I](<https://arxiv.org/abs/1711.10561>)
  著者投稿の原著 preprint の要旨・対象範囲を確認。既存2019論文そのものの全文監査とは別。
- [Li et al.: Fourier Neural Operator](<https://arxiv.org/abs/2010.08895>)
  著者投稿の原著 preprint の要旨・改訂履歴・問題族学習の対象範囲を確認。OpenReview はブラウザー検証要求のため本文未取得。

## 生物・化学反応のODE／確率反応

### Michaelis–Menten反応・Lotka–Volterra・SEIRの小規模基準計算

ID: biology-ode-1 · P2 · 未着手 · 新規実装

調査時の範囲：解説のみ

調査時の現状：

ロジスティック増殖、閉鎖SIR、空間なしFitzHugh–Nagumoの限定例は実行済み。生物22モデル族全体の実装ではない。

追加内容・最小の検証：

- 酵素の保存量と準定常近似の誤差を分離する。
- 捕食被食の不変量・正値性、SEIRの総人口保存と早期線形極限を確認する。

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

調査時の根拠：

- `catalog/atlas-depth.json` · biology
- `numerical-methods-atlas/assets/biological-models.json`


### Hodgkin–Huxleyの電位固定・静止平衡・発火時刻の検証

ID: biology-ode-2 · P2 · 未着手 · 新規実装

調査時の範囲：解説のみ

調査時の現状：

ロジスティック増殖、閉鎖SIR、空間なしFitzHugh–Nagumoの限定例は実行済み。生物22モデル族全体の実装ではない。

追加内容・最小の検証：

- 原著とCellML等の符号・温度・単位・速度定数の規約を固定する。
- ゲートの範囲、可除特異点、独立解と時間刻み収束を検査する。

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

調査時の根拠：

- `catalog/atlas-depth.json` · biology
- `numerical-methods-atlas/assets/biological-models.json`

- [Hodgkin–Huxley (1952), A quantitative description of membrane current…](<https://pmc.ncbi.nlm.nih.gov/articles/PMC1392413/>)
  書誌・抄録または公式文書の範囲を確認。新しい数値再現・全式の監査は未実施。

### Gillespie SSAの移入–死亡反応

ID: biology-ode-3 · P2 · 未着手 · 新規実装

調査時の範囲：解説のみ

調査時の現状：

ロジスティック増殖、閉鎖SIR、空間なしFitzHugh–Nagumoの限定例は実行済み。生物22モデル族全体の実装ではない。

追加内容・最小の検証：

- 既知のPoisson定常分布、平均・分散と有限時刻の分布を照合する。
- 単一seedの軌跡とアンサンブルの統計検証を区別する。

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

調査時の根拠：

- `catalog/atlas-depth.json` · biology
- `numerical-methods-atlas/assets/biological-models.json`


## 反応拡散・生物の空間モデル

### Fisher–KPPのAblowitz–Zeppetella厳密進行前線

ID: biology-space-1 · P1 · 未着手 · 新規実装

調査時の範囲：解説のみ

調査時の現状：

1D周期Schnakenbergの線形発現・非線形発展・成長後パターン、反応拡散の分割比較は既存。Fisher–KPPは文献解説のみ。

追加内容・最小の検証：

- 特殊な厳密波速と一般の最小伝播速度を区別する。
- 波形・前線位置・正値性、有限領域境界の影響、空間と時間の収束を分ける。

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

調査時の根拠：

- `catalog/atlas-depth.json` · biology
- `numerical-methods-atlas/assets/biological-models.json` · fisher-kpp

- [Ablowitz–Zeppetella (1979), Explicit solutions of Fisher's equation for a special wave speed](<https://doi.org/10.1007/BF02462380>)
  出版社検索結果の書誌と既存生物台帳の特殊前線条件を確認。全文の導出は今回未精査。

### Schnakenberg等の2D・非周期境界と模様選択

ID: biology-space-2 · P2 · 未着手 · 検証の拡充

調査時の範囲：検証範囲不足

調査時の現状：

1D周期Schnakenbergの線形発現・非線形発展・成長後パターン、反応拡散の分割比較は既存。Fisher–KPPは文献解説のみ。

追加内容・最小の検証：

- 固定対称な1D初期値の結果を一般の模様選択へ拡張しない。
- 空間2Dと境界・初期摂動を変え、独立参照の解像度感度を保存する。

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

調査時の根拠：

- `catalog/atlas-depth.json` · biology.supplemental_examples
- `numerical-methods-atlas/assets/biological-models.json` · schnakenberg

- [Schnakenberg (1979), Simple chemical reaction systems with limit cycle behaviour](<https://pubmed.ncbi.nlm.nih.gov/537379/>)
  原著書誌を確認。既存の1D実行と原著反応則を混同しない。

### Keller–Segel／移流反応拡散の滑らかな製造解

ID: biology-space-3 · P2 · 未着手 · 新規実装

調査時の範囲：解説のみ

調査時の現状：

1D周期Schnakenbergの線形発現・非線形発展・成長後パターン、反応拡散の分割比較は既存。Fisher–KPPは文献解説のみ。

追加内容・最小の検証：

- まず製造解で保存量・正値性・交差流束を確認する。
- ピーク形成・真の発散・数値振動を区別し、連成と分割誤差を測る。

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

調査時の根拠：

- `numerical-methods-atlas/assets/biological-models.json` · keller-segel
- `catalog/atlas-crossovers.json` · reaction-transport


## 古典分子動力学・温度制御

### Nosé–Hoover／chainとBerendsen・速度スケーリングの対照

ID: thermostats-md-1 · P2 · 未着手 · 新規実装

調査時の範囲：解説のみ

調査時の現状：

LangevinとCSVRは、同じOBABO分割の2自由度調和／quartic系とCSVR核まで検証済み。他10手法は専用実装がない。

追加内容・最小の検証：

- 平均温度だけでなく正準分布・温度揺らぎ・非エルゴード性を調べる。
- 既存Langevin/CSVRと同じ小さな系・観測量・分割条件で比較する。

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

調査時の根拠：

- `catalog/atlas-depth.json` · temperature
- `catalog/atlas-methods.json` · nose-hoover

- [LAMMPS公式: Nosé–Hoover nvt/npt](<https://docs.lammps.org/fix_nh.html>)
  書誌・抄録または公式文書の範囲を確認。新しい数値再現・全式の監査は未実施。
- [Bussi–Donadio–Parrinello (2007), Canonical sampling through velocity rescaling](<https://arxiv.org/abs/0803.4060>)
  書誌・抄録または公式文書の範囲を確認。新しい数値再現・全式の監査は未実施。

### 重心除去・拘束・多自由度での正準統計

ID: thermostats-md-2 · P2 · 未着手 · 検証の拡充

調査時の範囲：検証範囲不足

調査時の現状：

LangevinとCSVRは、同じOBABO分割の2自由度調和／quartic系とCSVR核まで検証済み。他10手法は専用実装がない。

追加内容・最小の検証：

- 有効自由度と運動エネルギー分布を一致させる。
- 刻み・結合時間・標本誤差と時間相関を別々に評価する。

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

調査時の根拠：

- `catalog/atlas-depth.json` · temperature
- `catalog/atlas-methods.json` · nose-hoover

- [LAMMPS公式: Nosé–Hoover nvt/npt](<https://docs.lammps.org/fix_nh.html>)
  書誌・抄録または公式文書の範囲を確認。新しい数値再現・全式の監査は未実施。

### BOMD／CPMDと熱浴の連成・長いNVE

ID: thermostats-md-3 · P3 · 未着手 · 検証の拡充

調査時の範囲：検証範囲不足

調査時の現状：

LangevinとCSVRは、同じOBABO分割の2自由度調和／quartic系とCSVR核まで検証済み。他10手法は専用実装がない。

追加内容・最小の検証：

- 既存の短いBOMD局所比較を、長時間のエネルギー保存や連成全体の検証と扱わない。
- 用途が具体化したときに、力誤差・SCF誤差・積分誤差と熱浴の寄与を分離する。

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

調査時の根拠：

- `catalog/atlas-depth.json` · temperature
- `catalog/atlas-methods.json` · nose-hoover


## Schrödinger・孤立原子

### 既存H/Heの式・規格化・出典を独立参照解カードへ収録

ID: quantum-atomic-1 · P1 · 未着手 · 参照・出典の整備

調査時の範囲：出典整備不足

調査時の現状：

水素型原子の解析解、球対称Heの閉殻HF／交換のみLDA、半径格子・SCF・独立PySCF参照は既存。

追加内容・最小の検証：

- 水素の固有値・動径関数・単位・縮退と境界条件をまとめる。
- Heの有限基底HF／LDA参照を相関を含む物理的厳密値と区別する。

完了条件：

- 対象の本文・台帳と修正した箇所が確認できる。
- 出典・書誌・適用範囲の修正根拠と確認記録を残す。
- 実在する対象と根拠を照合してから完了にする。

調査時の根拠：

- `catalog/atlas-depth.json` · quantum-atoms
- `catalog/atlas-quantum.json` · hydrogen

- [PySCF公式: Self-consistent field methods](<https://pyscf.org/user/scf.html>)
  書誌・抄録または公式文書の範囲を確認。新しい数値再現・全式の監査は未実施。

### 箱型井戸・調和振動子等の軽量固有値ベンチマーク

ID: quantum-atomic-2 · P2 · 未着手 · 新規実装

調査時の範囲：未収録

調査時の現状：

水素型原子の解析解、球対称Heの閉殻HF／交換のみLDA、半径格子・SCF・独立PySCF参照は既存。

追加内容・最小の検証：

- 教材と既存コードの詳細照合後に新規登録を確定する。
- 固有値だけでなく規格化・直交性・節・固有対残差、領域と格子誤差を確認する。

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

台帳・配布Pythonの名称と問題登録を概観した候補。全教材本文の数式との重複まで精査した判定ではない。

調査時の根拠：

- `catalog/atlas-depth.json` · quantum-atoms
- `catalog/atlas-quantum.json` · hydrogen


## 分子HF・電子相関

### 最小基底H₂のRHF／UHF／FCI比較

ID: quantum-molecule-1 · P2 · 未着手 · 新規実装

調査時の範囲：解説のみ

調査時の現状：

自作s型Gaussian積分によるH₂ RHFと独立PySCF比較は既存。同一有限基底の比較と、角運動量・完全基底・相関の検証は別。

追加内容・最小の検証：

- 小さな固定基底で解離に伴う対称性の破れと相関誤差を示す。
- 有限基底FCIを連続空間の厳密解と呼ばない。重い基底走査を前提にしない。

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

調査時の根拠：

- `catalog/atlas-depth.json` · quantum-molecular
- `catalog/atlas-quantum.json` · h2-hf-dft

- [PySCF公式: Self-consistent field methods](<https://pyscf.org/user/scf.html>)
  書誌・抄録または公式文書の範囲を確認。新しい数値再現・全式の監査は未実施。

### 一般分子・分子DFT・MP2/CC/多参照の実証

ID: quantum-molecule-2 · P3 · 未着手 · 新規実装

調査時の範囲：解説のみ

調査時の現状：

自作s型Gaussian積分によるH₂ RHFと独立PySCF比較は既存。同一有限基底の比較と、角運動量・完全基底・相関の検証は別。

追加内容・最小の検証：

- 用途と計算予算が決まったものを個別に選ぶ。
- 基底・SCFの数値誤差と、汎関数・電子相関の物理近似誤差を分離する。

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

調査時の根拠：

- `catalog/atlas-depth.json` · quantum-molecular
- `catalog/atlas-quantum.json` · h2-hf-dft

- [PySCF公式: Self-consistent field methods](<https://pyscf.org/user/scf.html>)
  書誌・抄録または公式文書の範囲を確認。新しい数値再現・全式の監査は未実施。

## 周期DFT・力・第一原理MD

### 既存Heのエネルギー／力の参照値と出典の集約

ID: quantum-periodic-1 · P1 · 未着手 · 参照・出典の整備

調査時の範囲：出典整備不足

調査時の現状：

固定Heの静的LDA、非対称He₂の全6座標の力、Gaussian/PW独立比較、短いBOMD局所確認まで既存。

追加内容・最小の検証：

- 幾何・GTH版・Libxc指定・単位・電子数・コード版を参照カードに固定する。
- 解析力、エネルギー差分、独立平面波参照と各残差を対応付ける。

完了条件：

- 対象の本文・台帳と修正した箇所が確認できる。
- 出典・書誌・適用範囲の修正根拠と確認記録を残す。
- 実在する対象と根拠を照合してから完了にする。

調査時の根拠：

- `catalog/atlas-depth.json` · quantum-periodic
- `catalog/atlas-forces-reading.json`

- [DFTK公式: Pseudopotentials](<https://docs.dftk.org/stable/examples/pseudopotentials/>)
  書誌・抄録または公式文書の範囲を確認。新しい数値再現・全式の監査は未実施。

### 一般物質・金属・非局所擬ポテンシャル・長時間MD

ID: quantum-periodic-2 · P3 · 未着手 · 検証の拡充

調査時の範囲：検証範囲不足

調査時の現状：

固定Heの静的LDA、非対称He₂の全6座標の力、Gaussian/PW独立比較、短いBOMD局所確認まで既存。

追加内容・最小の検証：

- 固定Heの成功を一般材料・金属・CPMDの成功へ拡張しない。
- 現行の軽量保守方針を維持し、必要な用途が示された場合に個別計画にする。

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

調査時の根拠：

- `catalog/atlas-depth.json` · quantum-periodic
- `catalog/atlas-forces-reading.json`

- [DFTK公式: Pseudopotentials](<https://docs.dftk.org/stable/examples/pseudopotentials/>)
  書誌・抄録または公式文書の範囲を確認。新しい数値再現・全式の監査は未実施。

## SPH・Godunov SPH

### GSPHの1D Sod衝撃管

ID: sph-gsph-1 · P2 · 未着手 · 新規実装

調査時の範囲：解説のみ

調査時の現状：

SPHはカーネル再構成の実装と検査がある。GSPHの原著に沿う解説はあるが、粒子の流体時間発展は専用実装されていない。

追加内容・最小の検証：

- 既存Sodの厳密Riemann参照を粒子位置・体積重みと整合させる。
- 粒子対の運動量/エネルギー保存、可変平滑化長と時間更新を含めて検証する。

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

調査時の根拠：

- `catalog/atlas-methods.json` · sph/gsph
- `numerical-methods-atlas/references.json` · inutsuka2002

- [Inutsuka (2002), Reformulation of Smoothed Particle Hydrodynamics with Riemann Solver](<https://arxiv.org/abs/astro-ph/0206401>)
  出版社抄録と書誌を確認。既存アトラスには著者稿の節2–4の読書記録がある。今回新しい実装・原著数値再現はしていない。

### 静止一様圧力・線形音波の粒子配置依存

ID: sph-gsph-2 · P2 · 未着手 · 検証の拡充

調査時の範囲：検証範囲不足

調査時の現状：

SPHはカーネル再構成の実装と検査がある。GSPHの原著に沿う解説はあるが、粒子の流体時間発展は専用実装されていない。

追加内容・最小の検証：

- カーネル補間誤差と流体更新誤差を区別する。
- 規則/摂動粒子配置、平滑化長、境界処理と音速/振幅減衰を小規模比較する。

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

調査時の根拠：

- `catalog/atlas-methods.json` · sph/gsph
- `numerical-methods-atlas/references.json` · inutsuka2002
