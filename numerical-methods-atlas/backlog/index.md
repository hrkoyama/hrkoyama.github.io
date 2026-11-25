# 未実装・拡充候補：問題ごとに検証し、まとめて公開する / Benchmark backlog: verify each problem, publish in batches

全分野サーベイの98候補と共通5項目を作業台帳に登録し、参照・コード・検証・図を一組ずつ揃えます。既存例の拡充や出典整備も含み、103件すべてが未実装の手法という意味ではありません。

今回はユーザーが明示した残り23項目を一組として扱います。入力・参照・判定・保存図・履歴は各問題で独立させ、索引生成・全体検査・公開確認を集約します。検証済みは記載した固定入力/整理範囲に限り、元の一般的な未実装・未検証範囲まで完了した意味ではありません。

Source: https://hrkoyama.github.io/catalog/atlas-benchmark-backlog.json

## 共通：参照・引用・再現

### 既存の検証済み解を参照解カードへ登録

ID: common-reference-cards · P0 · 検証済み · 参照・出典の整備

調査時の範囲：整理・登録不足

調査時の現状：

Bratu、調和振動子、stiff-cosine、水素原子等は既存の解析/参照根拠がある。一覧18件にないことを「解がない」と解釈せず、条件・式・図・実行・出典を一組にする。

追加内容・最小の検証：

- Bratu、調和振動子、stiff-cosine、水素原子等は既存の解析/参照根拠がある。一覧18件にないことを「解がない」と解釈せず、条件・式・図・実行・出典を一組にする。

完了条件：

- 対象の本文・台帳と修正した箇所が確認できる。
- 出典・書誌・適用範囲の修正根拠と確認記録を残す。
- 実在する対象と根拠を照合してから完了にする。

2026-11-25に追加した限定範囲：既存Bratu・調和振動子・stiff-cosine・水素型原子の4参照カードを、実固定パラメータ・標本化・旧配布版/入力SHA・図・実行へ結びました。新規数値実行ではありません。

調査時の根拠：

- `numerical-methods-atlas/solutions/index.json`
- `numerical-methods-atlas/problems/bratu/index.json`


完了の根拠：

```json
{
  "targets": [
    "/catalog/atlas-reference-supplements.json",
    "/catalog/atlas-problem-links.json"
  ],
  "proof": [
    "/catalog/atlas-reference-metadata.json",
    "/code/numerical-methods-atlas/2026-11-22/verification.json",
    "/code/quantum-atoms/2026-11-21/verification.json"
  ],
  "note": "確認した対象・出典/入力/旧配布版SHAに基づく限定したメタデータ修正。既存Bratu・調和振動子・stiff-cosine・水素型原子の4参照カードを、実固定パラメータ・標本化・旧配布版/入力SHA・図・実行へ結びました。新規数値実行ではありません。"
}
```

### 出典を原問題・解の導出・数値手法・参照実装に分ける

ID: common-citation-roles · P0 · 検証済み · 参照・出典の整備

調査時の範囲：出典整備不足

調査時の現状：

URL配列だけの参照解カードに、著者・年・題名・DOI・該当式/節と条件を補う。初等解は信頼できる教科書と代入確認、製造解は自分で選んだ場と導いた外力・境界を示す。存在しない原著を付けない。

追加内容・最小の検証：

- URL配列だけの参照解カードに、著者・年・題名・DOI・該当式/節と条件を補う。初等解は信頼できる教科書と代入確認、製造解は自分で選んだ場と導いた外力・境界を示す。存在しない原著を付けない。

完了条件：

- 対象の本文・台帳と修正した箇所が確認できる。
- 出典・書誌・適用範囲の修正根拠と確認記録を残す。
- 実在する対象と根拠を照合してから完了にする。

2026-11-25に追加した限定範囲：旧18カードに引用役割と実際の閲読範囲を付記し、旧97カードの引用を保持しました。全原著や原厳密解出典を通読・確定したとは扱いません。

調査時の根拠：

- `numerical-methods-atlas/solutions/index.json` · cases[*].sources


完了の根拠：

```json
{
  "targets": [
    "/catalog/atlas-reference-metadata.json"
  ],
  "proof": [
    "/numerical-methods-atlas/assets/reference-solutions.json",
    "/numerical-methods-atlas/references.json"
  ],
  "note": "確認した対象・出典/入力/旧配布版SHAに基づく限定したメタデータ修正。旧18カードに引用役割と実際の閲読範囲を付記し、旧97カードの引用を保持しました。全原著や原厳密解出典を通読・確定したとは扱いません。"
}
```

### 連続厳密解・半解析解・製造解・離散厳密解・独立数値参照を区別

ID: common-reference-kinds · P0 · 検証済み · 参照・出典の整備

調査時の範囲：共通仕様の拡充

調査時の現状：

半解析解の根探索/求積誤差、独立参照の解像度/公差と版を記録。同一コードの細格子解は独立参照と別に表示し、点値/セル平均・単位・幾何・境界・時刻を合わせる。

追加内容・最小の検証：

- 半解析解の根探索/求積誤差、独立参照の解像度/公差と版を記録。同一コードの細格子解は独立参照と別に表示し、点値/セル平均・単位・幾何・境界・時刻を合わせる。

完了条件：

- 対象の本文・台帳と修正した箇所が確認できる。
- 出典・書誌・適用範囲の修正根拠と確認記録を残す。
- 実在する対象と根拠を照合してから完了にする。

2026-11-25に追加した限定範囲：今回の19ケースを加える前の119カードのうち31を精密な参照種別へ分類し、88は明示的な未分類として残しました。連続厳密解・離散厳密参照・独立数値参照・自己収束を同一視しません。

調査時の根拠：

- `catalog/atlas-depth.json`
- `numerical-methods-atlas/solutions/index.json`


完了の根拠：

```json
{
  "targets": [
    "/catalog/atlas-reference-metadata.json"
  ],
  "proof": [
    "/catalog/atlas-reference-supplements.json"
  ],
  "note": "確認した対象・出典/入力/旧配布版SHAに基づく限定したメタデータ修正。今回の19ケースを加える前の119カードのうち31を精密な参照種別へ分類し、88は明示的な未分類として残しました。連続厳密解・離散厳密参照・独立数値参照・自己収束を同一視しません。"
}
```

### 各テストを入力・誤差・収束・受入条件まで揃える

ID: common-reproducible-package · P0 · 検証済み · 参照・出典の整備

調査時の範囲：共通仕様の拡充

調査時の現状：

図だけで終えず、固定入力・参照評価コード・結果CSV/JSON・誤差ノルム・保存量・失敗/停止理由・再現コマンドを一組にする。空間・時間・反復・標本誤差を分離し、不連続解に滑らかな解の次数を一律要求しない。

追加内容・最小の検証：

- 図だけで終えず、固定入力・参照評価コード・結果CSV/JSON・誤差ノルム・保存量・失敗/停止理由・再現コマンドを一組にする。空間・時間・反復・標本誤差を分離し、不連続解に滑らかな解の次数を一律要求しない。

完了条件：

- 対象の本文・台帳と修正した箇所が確認できる。
- 出典・書誌・適用範囲の修正根拠と確認記録を残す。
- 実在する対象と根拠を照合してから完了にする。

2026-11-25に追加した限定範囲：旧63群138ケースのSHA付き契約台帳を作り、保存判定7819件と元のstudy-goal成否を保持しました。52群はacceptance/pre-run資料あり、11群はembedded-only。acceptance.jsonなし13群のうちlevel-set/sem-frにはpre-run資料があります。後付けの事前凍結や新しい収束検証を作りません。

調査時の根拠：

- `catalog/atlas-execution-examples.json`
- `numerical-methods-atlas/validation/index.json`


完了の根拠：

```json
{
  "targets": [
    "/catalog/atlas-legacy-reference-contracts-2026-11-25.json"
  ],
  "proof": [
    "/catalog/atlas-legacy-reference-registry-2026-11-25.json"
  ],
  "note": "確認した対象・出典/入力/旧配布版SHAに基づく限定したメタデータ修正。旧63群138ケースのSHA付き契約台帳を作り、保存判定7819件と元のstudy-goal成否を保持しました。52群はacceptance/pre-run資料あり、11群はembedded-only。acceptance.jsonなし13群のうちlevel-set/sem-frにはpre-run資料があります。後付けの事前凍結や新しい収束検証を作りません。"
}
```

### FMM原著レコードの古い未実装注記を修正候補にする

ID: common-stale-reference-note · P0 · 検証済み · 参照・出典の整備

調査時の範囲：出典整備不足

調査時の現状：

greengard1987.note はM2LとFMM solver未実装と記すが、現行の2D log FMMと収束検証がある。利用した原著の範囲を保って現在の限定実装と整合させる。今回のサーベイではサイトを変更していない。

追加内容・最小の検証：

- greengard1987.note はM2LとFMM solver未実装と記すが、現行の2D log FMMと収束検証がある。利用した原著の範囲を保って現在の限定実装と整合させる。今回のサーベイではサイトを変更していない。

完了条件：

- 対象の本文・台帳と修正した箇所が確認できる。
- 出典・書誌・適用範囲の修正根拠と確認記録を残す。
- 実在する対象と根拠を照合してから完了にする。

2026-11-25に追加した限定範囲：Greengard–Rokhlin(1987)の現行noteだけを限定した2D log M2L/FMMと3D inverse-r実装の現状に合わせ、原著・旧配布版・その他書誌を保持しました。

調査時の根拠：

- `numerical-methods-atlas/references.json` · greengard1987
- `catalog/atlas-methods.json` · fmm


完了の根拠：

```json
{
  "targets": [
    "/numerical-methods-atlas/references.json"
  ],
  "proof": [
    "/catalog/atlas-execution-examples.json",
    "/numerical-methods-atlas/validation/releases.json"
  ],
  "note": "確認した対象・出典/入力/旧配布版SHAに基づく限定したメタデータ修正。Greengard–Rokhlin(1987)の現行noteだけを限定した2D log M2L/FMMと3D inverse-r実装の現状に合わせ、原著・旧配布版・その他書誌を保持しました。"
}
```

## 圧縮性流体・強衝撃波

### Noh問題：収束流と外向き強衝撃波

ID: compressible-fluid-1 · P1 · 公開済み · 新規実装

調査時の範囲：未収録

調査時の現状：

初期圧力ゼロの1D平面・円筒・球対称と、正方形全域の実2D Cartesianの固定入力を公開済み。旧配布版・基準・失敗履歴を保持し、公開URLの図・ZIP・Linux追試まで確認。

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

公開完了の範囲は初期圧力ゼロの1D平面・円筒・球対称と、正方形全域の実2D Cartesianの固定入力です。各配布物・受入基準・失敗履歴・過熱誤差・方向差を保持しています。原点位置ずらし・一般摂動安定性・3D Cartesian等の将来拡張は今回の完了範囲外で、未検証です。

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

完了の根拠：

```json
{
  "verification": "/code/validated-examples/2026-11-23-r5/noh/verification.json",
  "inputs": [
    "/code/validated-examples/2026-11-23-r5/noh/inputs.json",
    "/code/validated-examples/2026-11-23-r5/noh/acceptance.json",
    "/code/validated-examples/2026-11-23-r5/noh/spherical-acceptance.json",
    "/code/validated-examples/2026-11-23-r5/noh/pre-run-contract-spherical.json",
    "/code/validated-examples/2026-11-23-r5/noh/pre-run-contract-spherical-revision03.json",
    "/code/validated-examples/2026-11-23-r2/noh-cartesian/inputs.json",
    "/code/validated-examples/2026-11-23-r2/noh-cartesian/acceptance.json",
    "/code/validated-examples/2026-11-23-r2/noh-cartesian/pre-run-contract.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-23-r5/noh/results/noh-shock-preview.png",
    "/code/validated-examples/2026-11-23-r5/noh/results/noh-shock.png",
    "/code/validated-examples/2026-11-23-r5/noh/results/noh-shock-errors.png",
    "/code/validated-examples/2026-11-23-r5/noh/results/noh-spherical-budget.png",
    "/code/validated-examples/2026-11-23-r2/noh-cartesian/results/noh-cartesian-2d-preview.png",
    "/code/validated-examples/2026-11-23-r2/noh-cartesian/results/noh-cartesian-2d.png"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#noh-ja",
  "execution": "/numerical-methods-atlas/validation/noh-cartesian-2d/?lang=ja",
  "code": [
    "/code/validated-examples/2026-11-23-r5/noh/noh_solver.py",
    "/code/validated-examples/2026-11-23-r5/noh/noh_reference.py",
    "/code/validated-examples/2026-11-23-r2/noh-cartesian/cartesian_solver.py",
    "/code/validated-examples/2026-11-23-r2/noh-cartesian/cartesian_reference.py"
  ],
  "references": [
    "/numerical-methods-atlas/solutions/?lang=ja#solution-noh-ja",
    "/code/validated-examples/2026-11-23-r5/noh/exactpack-reference.json",
    "/code/validated-examples/2026-11-23-r5/noh/exactpack-reference-receipt.json"
  ]
}
```

### Sedov–Taylorの点爆発

ID: compressible-fluid-2 · P1 · 公開済み · 新規実装

調査時の範囲：未収録

調査時の現状：

1D球対称の固定入力・半解析参照・独立ExactPack点値・図・コードを追加。初版のLinux追試はCFL中間比のoverflow警告で失敗したため、その失敗と旧配布物を保持し、新r2で等価なCFL計算へ修正。入力と受入閾値を保って23検査・全4計算を再実行。 修正版r2は指定HRサイトで公開され、公開ZIPだけのLinux458検査（Sedov23検査・全4計算48判定）と匿名取得の照合まで確認済み。

追加内容・最小の検証：

- 固定爆発エネルギーの正規化、自己相似の衝撃半径と密度/圧力/速度を比較。
- 有限セルへのエネルギー投入半径の誤差とPDE格子誤差を分け、球対称体積平均で参照を作る。
- 低密度/負圧、総エネルギー、球対称性、中心特異点を報告。

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

軽量検証は128/256/512球殻と同じ最細格子での投入半径.03/.015感度に限定します。r1はMacで成功後、公開ZIPのLinux -Werror本計算でoverflow警告を例外扱いし失敗。r2では1/max(波速/幅)という等価なCFL演算で中間overflowを回避し、数値基準を緩めていません。有限投入半径と理想点源のモデル差が残り、傾きは純粋な空間精度次数ではありません。完全な連続極限分離、実2D Cartesian、非対称安定性、他γ・周囲密度勾配は未検証です。 公開済みという状態は、この固定入力で完了した軽量検証に限ります。

調査時の根拠：

- `catalog/atlas-test-problems.json`
  Sedov IDなし。
- `numerical-methods-atlas/en/read/reference-solutions/index.html` · reference-solutions
  Sedovは将来項目としてのみ言及。

- [LANL ExactPack: official benchmark collection and references](<https://github.com/lanl/ExactPack>)
  公式READMEでNoh/Sedov/Guderleyと出典一覧を確認。追加して相互検証する候補であり、現アトラスの依存や照合済み実績ではない。

完了の根拠：

```json
{
  "verification": "/code/validated-examples/2026-11-23-r2/sedov/verification.json",
  "inputs": [
    "/code/validated-examples/2026-11-23-r2/sedov/inputs.json",
    "/code/validated-examples/2026-11-23-r2/sedov/acceptance.json",
    "/code/validated-examples/2026-11-23-r2/sedov/pre-run-contract.json",
    "/code/validated-examples/2026-11-23-r2/sedov/reference-contract.json",
    "/code/validated-examples/2026-11-23-r2/sedov/contract-r1.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-23-r2/sedov/results/sedov-blast-preview.png",
    "/code/validated-examples/2026-11-23-r2/sedov/results/sedov-blast.png"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#sedov-ja",
  "execution": "/numerical-methods-atlas/validation/sedov-blast/?lang=ja",
  "code": [
    "/code/validated-examples/2026-11-23-r2/sedov/run.py",
    "/code/validated-examples/2026-11-23-r2/sedov/sedov_solver.py",
    "/code/validated-examples/2026-11-23-r2/sedov/reference_sedov.py"
  ],
  "references": [
    "/numerical-methods-atlas/solutions/?lang=ja#solution-sedov-ja",
    "/code/validated-examples/2026-11-23-r2/sedov/exactpack-receipt.json",
    "/code/validated-examples/2026-11-23-r2/sedov/exactpack-snapshot.json",
    "https://github.com/hrkoyama/hrkoyama.github.io/actions/runs/45109504662",
    "https://github.com/hrkoyama/hrkoyama.github.io/actions/runs/45111190625"
  ]
}
```

### Double-Mach/前向きステップの多格子・独立参照

ID: compressible-fluid-3 · P2 · 公開済み · 検証の拡充

調査時の範囲：検証範囲不足

調査時の現状：

Double Mach反射と前向きステップの固定入力・3格子比較・独立有限体積参照・保存収支・図と実行コードを公開。前向きステップの参照は新規の独立C++17 MUSCL/HLL/Heun実行で、参照Ny160初回の120秒タイムアウトも保存。診断文字列の不要な確保だけを修正し、旧Ny80と配列がビット一致した。角の特別なエントロピー補正は使わず、局所エントロピー極値の変化と単調には減らない全流体の最大密度差を保持する。

追加内容・最小の検証：

- 既存初期条件と境界処理を固定し、少数格子で衝撃位置・保存誤差・wall jetを比較。
- 独立コードの有限格子数値参照として保存し厳密2D解とは呼ばない。
- 現時刻まで到達しない計算と成功例を混ぜない。

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

今回までの公開段階はDouble Mach反射と前向きステップの軽量な固定入力例です。Double Mach参照は過去実行の再利用、前向きステップ参照は新規の独立C++実行です。前向きステップの角無補正条件と元論文の角補正付きPPM像を区別し、高解像度のwall jet・すべり線・渦やfull-patternの収束、一般条件への保証は未検証として残します。 公開済みという状態は、この固定入力で完了した軽量検証に限ります。

調査時の根拠：

- `catalog/atlas-test-problems.json` · double-mach/forward-step
  計算画像あり、標準runner結び付けはなし。
- `numerical-methods-atlas/en/read/double-mach/index.html` · double-mach
  粗格子HLL像でfull-pattern収束・独立比較は未達と明記。

- [Woodward and Colella (1984), The numerical simulation of two-dimensional fluid flow with strong shocks](<https://doi.org/10.1016/0021-9991(84)90142-6>)
  問題の原著として書誌を引用。原著全文を直接精読したとは表示せず、前向きステップの固定設定と角処理の区別は下記Cockburn–Shuの選択箇所に照合。
- [Cockburn and Shu (1991), The P¹-RKDG Method for Two-Dimensional Euler Equations of Gas Dynamics, NASA CR187542 / ICASE91-32](<https://ntrs.nasa.gov/api/citations/19910015505/downloads/19910015505.pdf>)
  Example2のprintedpage7/PDFpage11とFig3のprintedpage8/PDFpage12の選択本文で、Mach3・形状・初期/流入値・T4と、角の特別処理有無を区別する記述を確認。今回の実装は角無補正。図の転載やRKDG実行は行わない。

完了の根拠：

```json
{
  "verification": "/code/validated-examples/2026-11-23/forward-step/verification.json",
  "inputs": [
    "/code/validated-examples/2026-11-23/double-mach/inputs.json",
    "/code/validated-examples/2026-11-23/double-mach/acceptance.json",
    "/code/validated-examples/2026-11-23/double-mach/pre-run-contract.json",
    "/code/validated-examples/2026-11-23/double-mach/references/independent-reuse.json",
    "/code/validated-examples/2026-11-23/forward-step/inputs.json",
    "/code/validated-examples/2026-11-23/forward-step/acceptance.json",
    "/code/validated-examples/2026-11-23/forward-step/pre-run-contract.json",
    "/code/validated-examples/2026-11-23/forward-step/references/independent-execution.json",
    "/code/validated-examples/2026-11-23/forward-step/contract-before-reference-performance.json",
    "/code/validated-examples/2026-11-23/forward-step/reference-data-qualification.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-23/double-mach/results/double-mach-reflection-preview.png",
    "/code/validated-examples/2026-11-23/double-mach/results/double-mach-reflection.png",
    "/code/validated-examples/2026-11-23/forward-step/results/forward-step-m3-preview.png",
    "/code/validated-examples/2026-11-23/forward-step/results/forward-step-m3.png"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#forward-step-ja",
  "execution": "/numerical-methods-atlas/validation/forward-step-m3/?lang=ja",
  "code": [
    "/code/validated-examples/2026-11-23/double-mach/run.py",
    "/code/validated-examples/2026-11-23/double-mach/dm_solver.py",
    "/code/validated-examples/2026-11-23/forward-step/run.py",
    "/code/validated-examples/2026-11-23/forward-step/fs_solver.py"
  ],
  "references": [
    "/numerical-methods-atlas/solutions/?lang=ja#solution-double-mach-ja",
    "/code/validated-examples/2026-11-23/double-mach/references/independent-reuse.json",
    "/code/validated-examples/2026-11-23/double-mach/references/quality.json",
    "https://doi.org/10.1016/0021-9991(84)90142-6",
    "/code/validated-examples/2026-11-23/double-mach/verification.json",
    "/numerical-methods-atlas/validation/double-mach-reflection/?lang=ja",
    "/numerical-methods-atlas/solutions/?lang=ja#solution-forward-step-ja",
    "/code/validated-examples/2026-11-23/forward-step/references/independent-execution.json",
    "/code/validated-examples/2026-11-23/forward-step/references/quality.json",
    "/code/validated-examples/2026-11-23/forward-step/references/reference.cpp",
    "https://ntrs.nasa.gov/api/citations/19910015505/downloads/19910015505.pdf",
    "/code/validated-examples/2026-11-23/forward-step/references/attempts/01/independent-execution.json",
    "/code/validated-examples/2026-11-23/forward-step/references/performance-revision-comparison.json"
  ]
}
```

### 低Mach前処理の限定した渦検証

ID: compressible-fluid-4 · P2 · 公開済み · 新規実装

調査時の範囲：解説のみ

調査時の現状：

背景Mach数.1/.01・3格子・2流束の12計算を、同じ無制限中心primitive MUSCLとSSPRK(3,3)で比較する軽量例を公開。35単体検査・143判定と配布ZIPの独立展開再実行が合格した。初版の区分定数計算は全143判定中142合格で、M∞=.01の全域動圧規格化圧力L1=.16537が固定閾値.1を超えた失敗を保持。物理入力・判定値を変えず、両流束を同じ再構築へ改訂した。最細のM∞=.01では速度誤差と運動エネルギー保持が改善する一方、全域圧力L1は通常Roe .01194に対し前処理側 .01260で、すべての量が改善する結果ではない。

追加内容・最小の検証：

- 既存等エントロピー渦と同じ解析場を基準に少数Mach値を固定。
- 圧力誤差のMach依存、速度誤差、音響/対流刻み、定常残差を分離。
- 原理説明やRoe entropy-fixの成功をPDE前処理の実装と取り違えない。

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

対象はN16/32/64、M∞=.1/.01、T=.1の12固定実行と定数状態の17²標本Fourierモードです。数値散逸を前処理し、元の物理時間項は保ちます。SSPRK(3,3)の名だけから前進Eulerの強安定性や非線形安定性を導かず、陽的な音響刻み制約も保持します。定常反復・二重時間積分の加速、長時間・全Mach数域・衝撃波の検証は今後の範囲です。 初回の失敗した区分定数計算も全域誤差とともに保持し、改訂版だけを初回成功として扱いません。無制限中心MUSCLは滑らかな固定入力向けで、制限関数やTVD・衝撃波の保証は含みません。 公開済みという状態は、この短い固定入力と標本Fourier診断の範囲に限ります。全域圧力誤差は前処理側が大きい場合もあり、中心部の改善や切り出し図だけで全域の精度を主張しません。

調査時の根拠：

- `catalog/atlas-methods.json` · low-mach-preconditioning
  status=reading-only、code_modules=[]。
- `catalog/atlas-test-problems.json` · isentropic-vortex
  原KEEPの既存計算はある。

- [Fabian Miczek, Friedrich K. Röpke and Philipp V. F. Edelmann (2015). New numerical solver for flows at various Mach numbers](<https://doi.org/10.1051/0004-6361/201425059>)
  著者版の前処理行列・散逸項とRK3への言及を確認。今回は等エントロピー渦の短い時間区間に適用し、原著のGresho実験や暗黙積分を再現したとは扱いません。
- [Wasilij Barsukow, Philipp V. F. Edelmann, Christian Klingenberg, Fabian Miczek and Friedrich K. Röpke (2017). A Numerical Scheme for the Compressible Low-Mach Number Regime of Ideal Fluid Dynamics](<https://doi.org/10.1007/s10915-017-0372-4>)
  前処理散逸P⁻¹|PA|、原始変数行列と前進Eulerの厳しい刻み制限を確認。SSPRK33での本固定入力のFourier診断・実段検査は別に実施し、一般の非線形安定性やSSP保証を借用しません。
- [Seth C. Spiegel, H. T. Huynh and James R. DeBonis (2015). A Survey of the Isentropic Euler Vortex Problem using High-Order Methods](<https://doi.org/10.2514/6.2015-2444>)
  一般化された渦の定義と周期境界の相互作用・せん断層の説明を確認。独自のβ3・流速(1,.5)・M∞.1/.01を明示し、全平面解と有限周期箱の違いを保持します。NASA/FRソルバーや論文図の転載ではありません。
- [Sigal Gottlieb and Chi-Wang Shu (1998). Total Variation Diminishing Runge-Kutta Schemes](<https://doi.org/10.1090/S0025-5718-98-00913-2>)
  著者の書誌と著者PDFの索引抜粋で書誌・3次TVD法の位置付けを確認。PDFを直接通読したとは記録しません。係数は次の著者レビューのSSPRK(3,3)表示とも照合します。
- [Sigal Gottlieb, Chi-Wang Shu and Eitan Tadmor (2001). Strong Stability-Preserving High-Order Time Discretization Methods](<https://doi.org/10.1137/S003614450036757X>)
  3段3次の更新係数と、前進Eulerの強安定性を前提にするSSPの条件を確認。今回のMiczek流束についてSSP・TVD・非線形安定性を一般保証せず、指定したFourier行列と実際の段状態を別途確認します。

完了の根拠：

```json
{
  "verification": "/code/validated-examples/2026-11-23/low-mach/verification.json",
  "inputs": [
    "/code/validated-examples/2026-11-23/low-mach/inputs.json",
    "/code/validated-examples/2026-11-23/low-mach/acceptance.json",
    "/code/validated-examples/2026-11-23/low-mach/pre-run-contract.json",
    "/code/validated-examples/2026-11-23/low-mach/references/definition.json",
    "/code/validated-examples/2026-11-23/low-mach/contract-first-order.json",
    "/code/validated-examples/2026-11-23/low-mach/attempts/01/acceptance.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-23/low-mach/results/low-mach-vortex-preview.png",
    "/code/validated-examples/2026-11-23/low-mach/results/low-mach-vortex.png"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#isentropic-vortex-ja",
  "execution": "/numerical-methods-atlas/validation/low-mach-vortex/?lang=ja",
  "code": [
    "/code/validated-examples/2026-11-23/low-mach/run.py",
    "/code/validated-examples/2026-11-23/low-mach/lm_solver.py",
    "/code/validated-examples/2026-11-23/low-mach/linear_stability.py",
    "/code/validated-examples/2026-11-23/low-mach/references/analytic_vortex.py"
  ],
  "references": [
    "/numerical-methods-atlas/solutions/?lang=ja#solution-isentropic-vortex-ja",
    "/code/validated-examples/2026-11-23/low-mach/references/citations.json",
    "/code/validated-examples/2026-11-23/low-mach/references/README.md",
    "/code/validated-examples/2026-11-23/low-mach/attempts/01/results/result.json",
    "/code/validated-examples/2026-11-23/low-mach/results/low-mach-vortex-first-order.png"
  ]
}
```

### Guderleyの収束衝撃波

ID: compressible-fluid-additional · P2 · 公開済み · 新規実装

調査時の範囲：未収録

調査時の現状：

γ=1.4・未衝撃上流ρ=1,u=p=0、r∈[0,.75]、R_s(-1)=.6、t=-1→-.85、128/256/512球殻でHLL＋Heunを比較するr3を公開。33単体検査・3格子55判定と、ZIP独立展開での再実行が合格した。通常追試は元ExactPackの固有値探索・8点照合で資格確認したλを再利用し、相似ODE・Gauss16/32球殻求積・全3格子Euler計算を新たに実行する。固有値探索と元ソース点照合の再生成は別の明示コマンド。旧r2はMacの33検査・55判定に合格したが、公開Linuxでは33検査96.3396秒の後、本計算が残り23.312秒でグループ全体120秒上限へ達した。旧r2と実際の失敗記録を保持し、物理入力・受入基準・有限体積コア・run.py・120秒上限は不変。全体積・活性領域のL1、衝撃位置、境界流束と幾何源収支を並べ、衝撃層の最大差とセル幅単位の位置差が単調減少しない事実も保持する。原点収束や反射後は今回の範囲外。 Macでは同じ120秒枠で検査と本計算を続けて約.9121秒で完了し、ZIP独立展開での本計算は約.4241秒でした。全3格子の初期場・最終場・参照・履歴の保存配列は旧r2とビット一致しました。

追加内容・最小の検証：

- Noh/Sedovと区別し、相似指数の固有値問題と半解析的な場の参照を構成する。
- まず収束前の限定時区間・固定EOSで衝撃軌道と体積平均を照合し、原点反射後の分岐は別段階とする。

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

対象は球対称・γ=1.4・冷たい一様上流の収束前分岐をt=-1から-.85まで追う短い固定例。初期場は衝撃後の外側を含む相似場で、圧力ゼロは未衝撃の内側上流に限る。相似指数の固有値探索・相似ODE・球殻平均は数値評価を含む半解析参照で、閉形式の厳密セル平均とは区別する。参照は実際の固定ExactPackソースに基づくアダプターであり、独立に実装した相似解や別のPDEエンジンとの比較とは扱わない。圧力は保存量平均から評価し、原始圧力の平均と混同しない。図は1D半径結果の2D子午面表示。原点到達・反射後、円筒対称、一般EOS・非球対称摂動は未検証。冷たい上流の圧力ゼロと、64epsの絶対内部エネルギー許容帯にある丸め負値を記録し、音速平方根だけのガード回数と状態修復を分ける。非線形正値性の一般保証や高次の収束次数は主張しない。 通常追試のλは、固定ExactPackを実際に実行した資格確認記録から再利用します。相似ODEと求積・PDEの再計算、固有値探索の明示再生成、保存された元ソース照合の役割を区別し、キャッシュを固有値探索の再実行と表示しません。

調査時の根拠：

- `catalog/atlas-test-problems.json` · sod/shu-osher/strong-shock/double-mach/cylinder-forebody
  既存登録。strong-shockやdouble-machも計算済みであり未実装ではない。
- `catalog/atlas-execution-examples.json` · sod/shu-osher
  共通固定入力あり。
- `numerical-methods-atlas/validation/index.json` · shu-independent
  独立Athena++参照・格子収束あり。

- [G. Guderley (1942), Starke kugelige und zylindrische Verdichtungsstöße in der Nähe des Kugelmittelpunktes bzw. der Zylinderachse](<https://raw.githubusercontent.com/lanl/ExactPack/9bacc477eb791e959c9621e771fc7a725db755fa/doc/source/references.rst>)
  原問題の歴史的出典。固定ExactPackの書誌で著者・年・巻・開始頁302を、Lazarus1981の出版社参考文献で題名を確認。原著1942本文は未閲覧で、相似場の式や今回の実測を原著から直接再現したとは主張しません。
- [Scott D. Ramsey, James R. Kamm and John H. Bolstad (2012), The Guderley problem revisited](<https://doi.org/10.1080/10618562.2011.647768>)
  LANLの書誌・抄録で収束側の相似指数と反射後の軌道係数が別の固有値問題であることを確認。原論文の全文通読や原著のPDE計算再現とは扱わず、今回の場は固定ExactPackソースを実際に用いて構成します。
- [Roger B. Lazarus (1981), Self-Similar Solutions for Converging Shocks and Collapsing Cavities](<https://doi.org/10.1137/0718022>)
  出版社の書誌・抄録と、ExactPackが明示する式2.5/2.8/2.9・球対称表6.5の転記を確認。λ=1.3943607838の表値はコード内の転記値で、元論文を独立に再転記した値とは区別します。
- [R. F. Chisnell (1998), An analytic description of converging shock waves](<https://doi.org/10.1017/S0022112097007775>)
  出版社の書誌・抄録と、ExactPack eexpが採用する臨界点の位相差・式3.1の実装を確認。相似指数は寸法解析から固定せず、固定コードの固有値計算で求めます。
- [Jasper Thrussell and Jim Michael Ferguson (2023), ExactPack: A python library of exact analytic solutions](<https://doi.org/10.1016/j.softx.2023.101560>)
  ExactPackのソフトウェア論文とGuderley収録を参照。論文記載版1.7.5と今回用いるソースの固定コミットは区別し、配布物内にソース・SHA・BSDライセンスを保存します。
- [Los Alamos National Laboratory / ExactPack contributors (2025), ExactPack Guderley solver, pinned source](<https://github.com/lanl/ExactPack/tree/9bacc477eb791e959c9621e771fc7a725db755fa/exactpack/solvers/guderley>)
  固定版のeexp・ramseyの前収束ODEとstate、表の転記、公式回帰値、BSD3条項を確認。全ExactPackテストを実行したとは扱いません。参照の実行成否はqualification.jsonに別記します。

完了の根拠：

```json
{
  "verification": "/code/validated-examples/2026-11-23-r3/guderley/verification.json",
  "inputs": [
    "/code/validated-examples/2026-11-23-r3/guderley/inputs.json",
    "/code/validated-examples/2026-11-23-r3/guderley/acceptance.json",
    "/code/validated-examples/2026-11-23-r3/guderley/pre-run-contract.json",
    "/code/validated-examples/2026-11-23-r3/guderley/references/definition.json",
    "/code/validated-examples/2026-11-23-r3/guderley/references/pre-reference-contract.json",
    "/code/validated-examples/2026-11-23-r3/guderley/references/cache-contract.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-23-r3/guderley/results/guderley-implosion-preview.png",
    "/code/validated-examples/2026-11-23-r3/guderley/results/guderley-implosion.png"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#guderley-ja",
  "execution": "/numerical-methods-atlas/validation/guderley-implosion/?lang=ja",
  "code": [
    "/code/validated-examples/2026-11-23-r3/guderley/run.py",
    "/code/validated-examples/2026-11-23-r3/guderley/guderley_solver.py",
    "/code/validated-examples/2026-11-23-r3/guderley/references/precollapse.py"
  ],
  "references": [
    "/numerical-methods-atlas/solutions/?lang=ja#solution-guderley-ja",
    "/code/validated-examples/2026-11-23-r3/guderley/references/citations.json",
    "/code/validated-examples/2026-11-23-r3/guderley/references/README.md",
    "/code/validated-examples/2026-11-23-r3/guderley/references/qualification.json",
    "/code/validated-examples/2026-11-23-r3/guderley/references/exactpack-source.json",
    "/code/validated-examples/2026-11-23-r3/guderley/references/eigenvalue-cache.json",
    "/code/validated-examples/2026-11-23-r3/guderley/references/cache-contract.json",
    "/code/validated-examples/2026-11-23-r3/guderley/references/cache-qualification.json",
    "/code/validated-examples/2026-11-23-r3/guderley/references/attempts/01-eigenvalue-recompute/qualification.json",
    "/code/validated-examples/2026-11-23-r3/guderley/attempts/02/failed-linux-report.json",
    "/code/validated-examples/2026-11-23-r3/guderley/attempts/02/failed-linux-workflow-context.json",
    "/code/validated-examples/2026-11-23-r3/guderley/attempts/02/published-release.json",
    "/code/validated-examples/2026-11-23-r3/guderley/attempts/02/pre-run-contract.json",
    "/code/validated-examples/2026-11-23-r3/guderley/attempts/02/cases.json"
  ]
}
```

## 移流・再構築・正値性

### Eulerの段階ごとの完全離散正値性

ID: advection-reconstruction-1 · P1 · 公開済み · 検証の拡充

調査時の範囲：検証範囲不足

調査時の現状：

27単体検査・3格子73判定と独立ZIP再実行、公開URLの517ファイル照合、公開配布物だけのLinux598検査/48ケース/19群が合格。ギャラリーの時空間図とコードへの経路を公開確認しました。

追加内容・最小の検証：

- 既存mean-preserving scalingの部品検査から、許容数値流束・SSP段階・CFLを含む一つの限定更新へ接続。
- 密度/圧力最小値とセル平均保存を全段階で測る。
- 強希薄波/near-vacuumで失敗・retry・floorを記録し、結果を理論の保証条件と対応付ける。

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

γ1.4の既存二重希薄波、128/256/512セル、保存量MUSCL・大域LF a4・SSPRK33に限定。CFL .4≤.5と全段波速上限を実測し、密度・圧力・保存収支・制限発動を記録。真空生成・一般のWENO/DG・2D正値性の検証ではありません。 公開内容commit 1c5302913560376997cfd3df06bb684bf71330df、Linux run 45142681101の実測成功を別記録に保持しています。

調査時の根拠：

- `code/numerical-methods-atlas/2026-11-21/numart/limiters.py` · positive_reconstruction
  部品は実装済み。
- `code/numerical-methods-atlas/2026-11-21/tests/test_limiters.py` · test_positive_scaling_conservation_and_pressure
  再構築テストあり。
- `numerical-methods-atlas/en/read/advanced-limiters/index.html` · advanced-limiters
  Euler MUSCL/FD WENOへの未接続を明記。

- [Zhang & Shu (2010), positivity-preserving Euler DG schemes](<https://www.math.purdue.edu/~zhan1966/research/paper/euler.pdf>)
  著者公開原稿をopenし題名・著者・密度圧力正値性の対象を確認。全文監査ではない。

完了の根拠：

```json
{
  "verification": "/numerical-methods-atlas/validation/verification/2026-11-23-euler-positivity-public.json",
  "inputs": [
    "/code/validated-examples/2026-11-23-r2/euler-positivity/inputs.json",
    "/code/validated-examples/2026-11-23-r2/euler-positivity/acceptance.json",
    "/code/validated-examples/2026-11-23-r2/euler-positivity/pre-run-contract.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-23-r2/euler-positivity/results/euler-double-rarefaction-positivity-preview.png",
    "/code/validated-examples/2026-11-23-r2/euler-positivity/results/euler-double-rarefaction-positivity.png"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#double-rarefaction-ja",
  "execution": "/numerical-methods-atlas/validation/euler-double-rarefaction-positivity/?lang=ja",
  "code": [
    "/code/validated-examples/2026-11-23-r2/euler-positivity/run.py",
    "/code/validated-examples/2026-11-23-r2/euler-positivity/euler_positivity.py",
    "/code/validated-examples/2026-11-23-r2/euler-positivity/references/double_rarefaction.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-23-r2/euler-positivity/references/citations.json",
    "/code/validated-examples/2026-11-23-r2/euler-positivity/references/README.md",
    "/code/validated-examples/2026-11-23-r2/euler-positivity/references/source-review.json",
    "/code/validated-examples/2026-11-23-r2/euler-positivity/source-provenance.json",
    "/code/validated-examples/2026-11-23-r2/euler-positivity/pre-run-review.json",
    "/code/validated-examples/2026-11-23-r2/euler-positivity/verification.json"
  ]
}
```

### Zalesak型2D回転輸送・形状保持

ID: advection-reconstruction-2 · P2 · 公開済み · 新規実装

調査時の範囲：未収録

調査時の現状：

26単体検査・8回転計算158判定、独立ZIP再実行、公開URLの図・コード照合と公開配布物のみのLinux全624検査が合格。途中の1/4周、回転中心とスロット角度の診断、ギャラリーからの導線も保存しています。

追加内容・最小の検証：

- 既存1D矩形波と2D滑らかentropy waveを残し、周期回転後の解析的returnを新たな問題として追加。
- 総量、min/max、形状誤差と回転中心/格子方向依存を比較。
- スロット形状・時刻・境界と点値/セル平均を原著または公式実装から固定する。

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

Firedrake公式例で形状・速度・周期を確認した単独0–1円盤の周期有限体積変種。真の2次元回転輸送を一次風上/保存量MUSCL minmod・SSPRK33で比較し、全段の保存・上下限、四分の一周と1周の形状誤差、位置/角度・境界帯の診断を保存。Zalesak FCT・Firedrake DG・LeVeque CTUの再現ではありません。初回32²/64²/128²の156/158判定と不合格を保持し、同一受入基準で細分化しています。 科学内容commit c1398c0eafe5511741cebc44d14ac324a6bf0429とLinux run 45154798151の公開実績を別記録に保存しています。

調査時の根拠：

- `catalog/atlas-test-problems.json` · advection-square/entropy-2d
  既存は1D不連続または2D滑らか。Zalesak固有IDなし。

- [Zalesak (1979), Fully multidimensional flux-corrected transport algorithms for fluids](<https://www.sciencedirect.com/science/article/pii/0021999179900512>)
  出版社書誌・抄録を確認。具体的スロット形状等は実装前に原文のテスト定義を照合する。

完了の根拠：

```json
{
  "verification": "/numerical-methods-atlas/validation/verification/2026-11-23-zalesak-public.json",
  "inputs": [
    "/code/validated-examples/2026-11-23/zalesak/inputs.json",
    "/code/validated-examples/2026-11-23/zalesak/acceptance.json",
    "/code/validated-examples/2026-11-23/zalesak/pre-run-contract.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-23/zalesak/results/zalesak-rotation-preview.png",
    "/code/validated-examples/2026-11-23/zalesak/results/zalesak-rotation.png"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#zalesak-ja",
  "execution": "/numerical-methods-atlas/validation/zalesak-rotation/?lang=ja",
  "code": [
    "/code/validated-examples/2026-11-23/zalesak/run.py",
    "/code/validated-examples/2026-11-23/zalesak/rotation.py",
    "/code/validated-examples/2026-11-23/zalesak/references/geometry.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-23/zalesak/references/citations.json",
    "/code/validated-examples/2026-11-23/zalesak/references/README.md",
    "/code/validated-examples/2026-11-23/zalesak/references/source-review.json",
    "/code/validated-examples/2026-11-23/zalesak/source-provenance.json",
    "/code/validated-examples/2026-11-23/zalesak/pre-run-review.json",
    "/code/validated-examples/2026-11-23/zalesak/attempts/01/attempt-summary.json",
    "/code/validated-examples/2026-11-23/zalesak/attempts/01/results/result.json",
    "/code/validated-examples/2026-11-23/zalesak/attempts/01/source/pre-run-contract.json",
    "/code/validated-examples/2026-11-23/zalesak/verification.json"
  ]
}
```

### WENO-Zの臨界点・epsilon依存の比較

ID: advection-reconstruction-3 · P2 · 公開済み · 検証の拡充

調査時の範囲：検証範囲不足

調査時の現状：

配布群weno-criticalの36単体検査と当該例の217判定、独立ZIPの全固定入力追試、公開URLの図・コード・配布物1048ファイル照合、公開配布物のみのLinux全735検査（24群56ケース）が合格。実際の科学内容commit a51543e8の成功を公開記録に保存しました。

追加内容・最小の検証：

- 既存p=2・epsilon=1e-6版を凍結し、比較版を追加して極値/高階臨界点の空間誤差を測る。
- 時間誤差を小さくした系列と固定格子の刻み系列を分離する。
- 原著最終版と前稿で異なる重み規約、特性/成分投影、FD点値を明記。

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

2026-11-23の候補13〜17を一括公開する限定検証。入力・受入基準・保存配列・失敗履歴は各不変配布版に保持。詳細な条件と適用範囲は実行入口を参照。 科学内容commit a51543e8b54129e70670e184290c9b50b5bc0645とLinux run 45167465669の実績を別記録に保持。後続の台帳更新コミットのCI成功は予告しません。

調査時の根拠：

- `catalog/atlas-methods.json` · weno-z
  variantとlimited review scope記録済み。
- `numerical-methods-atlas/references.json` · borges2008
  最終版はmetadata/abstract、以前の前稿と区別。
- `code/numerical-methods-atlas/2026-11-21/tests/test_reconstruction.py` · test_weno_constant_and_smooth_spatial_flux_derivative
  滑らか関数の既存検査を基準に拡張。


完了の根拠：

```json
{
  "verification": "/numerical-methods-atlas/validation/verification/2026-11-23-batch13-17-public.json",
  "inputs": [
    "/code/validated-examples/2026-11-23/weno-critical/inputs.json",
    "/code/validated-examples/2026-11-23/weno-critical/acceptance.json",
    "/code/validated-examples/2026-11-23/weno-critical/pre-run-contract.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-23/weno-critical/results/weno-critical-epsilon.png",
    "/code/validated-examples/2026-11-23/weno-critical/results/weno-critical-epsilon-preview.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-23/weno-critical/run.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-23/weno-critical/references/citations.json",
    "/code/validated-examples/2026-11-23/weno-critical/references/source-review.json",
    "/code/validated-examples/2026-11-23/weno-critical/README.md",
    "/code/validated-examples/2026-11-23/weno-critical/verification.json"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#advection-sine-ja",
  "execution": "/numerical-methods-atlas/validation/weno-critical-epsilon/?lang=ja"
}
```

## 浅水・地形・wet/dry

### SWASHESのlake at rest・地形上の定常解

ID: shallow-water-1 · P1 · 公開済み · 新規実装

調査時の範囲：未収録

調査時の現状：

配布群shallow-waterの31単体検査と当該例の62判定、独立ZIPの全固定入力追試、公開URLの図・コード・配布物1048ファイル照合、公開配布物のみのLinux全735検査（24群56ケース）が合格。実際の科学内容commit a51543e8の成功を公開記録に保存しました。

追加内容・最小の検証：

- 地形圧力ソースとfluxの釣合い、静止水面の保持、質量を測る。
- 一つのsmooth bump定常ケースから始め、境界条件と水頭/流量を固定。
- 平坦底ダム崩壊の成功をwell-balanced性の証拠にしない。

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

2026-11-23の候補13〜17を一括公開する限定検証。入力・受入基準・保存配列・失敗履歴は各不変配布版に保持。詳細な条件と適用範囲は実行入口を参照。 科学内容commit a51543e8b54129e70670e184290c9b50b5bc0645とLinux run 45167465669の実績を別記録に保持。後続の台帳更新コミットのCI成功は予告しません。

調査時の根拠：

- `code/numerical-methods-atlas/2026-11-21/numart/equations.py` · Barotropic(name='shallow-water')
  地形項を含まない基準。
- `catalog/atlas-test-problems.json` · dam-break
  現行問題との差。

- [Delestre et al., SWASHES](<https://arxiv.org/abs/1110.0288v7>)
  著者原稿の書誌・抄録を確認。2013出版、2016修正版v7で出版版の誤りを訂正と明示。参照版を固定すべき。

完了の根拠：

```json
{
  "verification": "/numerical-methods-atlas/validation/verification/2026-11-23-batch13-17-public.json",
  "inputs": [
    "/code/validated-examples/2026-11-23/shallow-water/inputs.json",
    "/code/validated-examples/2026-11-23/shallow-water/acceptance.json",
    "/code/validated-examples/2026-11-23/shallow-water/pre-run-contract.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-23/shallow-water/results/swashes-topography.png",
    "/code/validated-examples/2026-11-23/shallow-water/results/swashes-topography-preview.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-23/shallow-water/run.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-23/shallow-water/references/citations.json",
    "/code/validated-examples/2026-11-23/shallow-water/references/source-review.json",
    "/code/validated-examples/2026-11-23/shallow-water/README.md",
    "/code/validated-examples/2026-11-23/shallow-water/protocol-history.json",
    "/code/validated-examples/2026-11-23/shallow-water/verification.json"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#swashes-topography-ja",
  "execution": "/numerical-methods-atlas/validation/swashes-topography/?lang=ja"
}
```

### dry-bed参照を使うwetting/drying実行

ID: shallow-water-2 · P2 · 公開済み · 検証の拡充

調査時の範囲：検証範囲不足

調査時の現状：

配布群shallow-waterの31単体検査と当該例の47判定、独立ZIPの全固定入力追試、公開URLの図・コード・配布物1048ファイル照合、公開配布物のみのLinux全735検査（24群56ケース）が合格。実際の科学内容commit a51543e8の成功を公開記録に保存しました。

追加内容・最小の検証：

- 既存解析乾床解とfront位置、乾湿遷移、非負水深、質量を照合。
- dry toleranceと運動量処理、dry-cell速度の定義を公開。
- 既存の参照カードを実行済みと数えず、solver拡張後に新規固定入力を登録。

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

2026-11-23の候補13〜17を一括公開する限定検証。入力・受入基準・保存配列・失敗履歴は各不変配布版に保持。詳細な条件と適用範囲は実行入口を参照。 科学内容commit a51543e8b54129e70670e184290c9b50b5bc0645とLinux run 45167465669の実績を別記録に保持。後続の台帳更新コミットのCI成功は予告しません。

調査時の根拠：

- `numerical-methods-atlas/solutions/index.json` · swe-dry-bed/swe-vacuum
  参照は収録済み。
- `code/numerical-methods-atlas/2026-11-21/numart/equations.py` · Barotropic(name='shallow-water')
  現solverは非正水深を拒否。

- [Delestre et al., SWASHES](<https://arxiv.org/abs/1110.0288v7>)
  著者原稿の書誌・抄録を確認。2013出版、2016修正版v7で出版版の誤りを訂正と明示。参照版を固定すべき。

完了の根拠：

```json
{
  "verification": "/numerical-methods-atlas/validation/verification/2026-11-23-batch13-17-public.json",
  "inputs": [
    "/code/validated-examples/2026-11-23/shallow-water/inputs.json",
    "/code/validated-examples/2026-11-23/shallow-water/acceptance.json",
    "/code/validated-examples/2026-11-23/shallow-water/pre-run-contract.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-23/shallow-water/results/dry-bed-dam-break.png",
    "/code/validated-examples/2026-11-23/shallow-water/results/dry-bed-dam-break-preview.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-23/shallow-water/run.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-23/shallow-water/references/citations.json",
    "/code/validated-examples/2026-11-23/shallow-water/references/source-review.json",
    "/code/validated-examples/2026-11-23/shallow-water/README.md",
    "/code/validated-examples/2026-11-23/shallow-water/protocol-history.json",
    "/code/validated-examples/2026-11-23/shallow-water/verification.json"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#dry-bed-dam-break-ja",
  "execution": "/numerical-methods-atlas/validation/dry-bed-dam-break/?lang=ja"
}
```

## 非圧縮流・壁境界

### Ghiaのlid-driven cavity低Re比較

ID: incompressible-1 · P2 · 公開済み · 新規実装

調査時の範囲：未収録

調査時の現状：

配布群wall-flowの22単体検査と当該例の35判定、独立ZIPの全固定入力追試、公開URLの図・コード・配布物1048ファイル照合、公開配布物のみのLinux全735検査（24群56ケース）が合格。実際の科学内容commit a51543e8の成功を公開記録に保存しました。

追加内容・最小の検証：

- まずRe=100等の固定した少数条件で壁速度・角点処理・圧力基準を定義。
- 中心線u/v、渦中心、divergenceと定常残差を格子ごとに比較。
- Ghia表は高精度数値参照であり厳密解ではない。原表転記・出典ページと独立参照の差も保存。

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

2026-11-23の候補13〜17を一括公開する限定検証。入力・受入基準・保存配列・失敗履歴は各不変配布版に保持。詳細な条件と適用範囲は実行入口を参照。 科学内容commit a51543e8b54129e70670e184290c9b50b5bc0645とLinux run 45167465669の実績を別記録に保持。後続の台帳更新コミットのCI成功は予告しません。

調査時の根拠：

- `numerical-methods-atlas/en/read/incompressible/index.html` · incompressible
  周期基準のみ、wall boundary未実装を明記。
- `code/numerical-methods-atlas/2026-11-21/numart/incompressible.py` · poisson/project
  周期FFT演算子。

- [Ghia, Ghia & Shin (1982), High-Re solutions for incompressible flow](<https://www.sciencedirect.com/science/article/abs/pii/0021999182900584>)
  出版社検索結果の書誌・抄録で正方形cavityと数値参照を確認。直接openは403、表の値や全文は未照合。

完了の根拠：

```json
{
  "verification": "/numerical-methods-atlas/validation/verification/2026-11-23-batch13-17-public.json",
  "inputs": [
    "/code/validated-examples/2026-11-23-r2/wall-flow/inputs.json",
    "/code/validated-examples/2026-11-23-r2/wall-flow/acceptance.json",
    "/code/validated-examples/2026-11-23-r2/wall-flow/pre-run-contract.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-23-r2/wall-flow/results/cavity-ghia-re100.png",
    "/code/validated-examples/2026-11-23-r2/wall-flow/results/cavity-ghia-re100-preview.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-23-r2/wall-flow/run.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-23-r2/wall-flow/references/citations.json",
    "/code/validated-examples/2026-11-23-r2/wall-flow/references/source-review.json",
    "/code/validated-examples/2026-11-23-r2/wall-flow/README.md",
    "/code/validated-examples/2026-11-23-r2/wall-flow/protocol-history.json",
    "/code/validated-examples/2026-11-23-r2/wall-flow/verification.json"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#lid-driven-cavity-ja",
  "execution": "/numerical-methods-atlas/validation/cavity-ghia-re100/?lang=ja"
}
```

### Blasiusまたは非周期の製造解による壁面検査

ID: incompressible-2 · P2 · 公開済み · 新規実装

調査時の範囲：未収録

調査時の現状：

配布群wall-flowの22単体検査と当該例の59判定、独立ZIPの全固定入力追試、公開URLの図・コード・配布物1048ファイル照合、公開配布物のみのLinux全735検査（24群56ケース）が合格。実際の科学内容commit a51543e8の成功を公開記録に保存しました。

追加内容・最小の検証：

- 軽い非周期MMSで速度/圧力の境界と次数を先に検査。
- Blasius追加時は境界層近似の相似ODE解と、有限Re Navier–Stokes/有限計算領域の差を区別。
- 壁面せん断・排除厚さ・領域依存を測り、全NSの厳密解と表示しない。

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

2026-11-23の候補13〜17を一括公開する限定検証。入力・受入基準・保存配列・失敗履歴は各不変配布版に保持。詳細な条件と適用範囲は実行入口を参照。 科学内容commit a51543e8b54129e70670e184290c9b50b5bc0645とLinux run 45167465669の実績を別記録に保持。後続の台帳更新コミットのCI成功は予告しません。

調査時の根拠：

- `numerical-methods-atlas/en/read/reference-solutions/index.html` · reference-solutions
  Blasiusは将来項目。
- `code/numerical-methods-atlas/2026-11-21/numart/incompressible.py` · taylor_green
  現有は周期解析場。

- [Salari & Knupp, Code Verification by the Method of Manufactured Solutions, SAND2000-1444](<https://www.sandia.gov/research/publications/details/code-verification-by-the-method-of-manufactured-solutions-2000-06-01/>)
  Sandia公式報告の書誌・概要・DOI10.2172/759450を確認。製造解の検証方法の出典で、個別の初等解の発見原著として扱わない。

完了の根拠：

```json
{
  "verification": "/numerical-methods-atlas/validation/verification/2026-11-23-batch13-17-public.json",
  "inputs": [
    "/code/validated-examples/2026-11-23-r2/wall-flow/inputs.json",
    "/code/validated-examples/2026-11-23-r2/wall-flow/acceptance.json",
    "/code/validated-examples/2026-11-23-r2/wall-flow/pre-run-contract.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-23-r2/wall-flow/results/wall-manufactured.png",
    "/code/validated-examples/2026-11-23-r2/wall-flow/results/wall-manufactured-preview.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-23-r2/wall-flow/run.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-23-r2/wall-flow/references/citations.json",
    "/code/validated-examples/2026-11-23-r2/wall-flow/references/source-review.json",
    "/code/validated-examples/2026-11-23-r2/wall-flow/README.md",
    "/code/validated-examples/2026-11-23-r2/wall-flow/protocol-history.json",
    "/code/validated-examples/2026-11-23-r2/wall-flow/verification.json"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#wall-manufactured-ja",
  "execution": "/numerical-methods-atlas/validation/wall-manufactured/?lang=ja"
}
```

### Kelvin–Helmholtz／Rayleigh–Taylorの初期成長と独立参照

ID: incompressible-additional · P2 · 公開済み · 新規実装

調査時の範囲：未収録

調査時の現状：

固定した軽量段階をHRで公開。公開ファイル照合と全30補助版・71ケース・893pytestの公開ZIP Linux追試が合格。Saltzman／Williamsonを含む残る適用範囲はscope_noteと実行入口で区別します。

追加内容・最小の検証：

- 滑らかなせん断層・明示した摂動・境界・物理散逸を固定し、KHの初期成長率を比較する。
- RTは重力・密度配置・界面厚さと理論の仮定を別に定義する。非線形後期の図を厳密解と扱わず独立数値参照と比較する。

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

固定した軽量ケースの実装・検証・保存図を追加。各不変配布版に入力・判定・保存配列・改訂と失敗の履歴を保持し、条件と対象外は各実行入口に明記します。

調査時の根拠：

- `catalog/atlas-methods.json` · projection
  educational-example。
- `catalog/atlas-execution-examples.json` · taylor-green
  共通実行あり。
- `code/numerical-methods-atlas/2026-11-21/tests/test_new_models.py` · test_taylor_green_refinement_energy_and_pressure
  既存2次収束・圧力検査。

- [McNally–Lyra–Passy: A Well-Posed Kelvin-Helmholtz Instability Test and Comparison](<https://arxiv.org/abs/1111.1764>)
  著者稿の書誌・抄録で初期成長と滑らかな設定の検証目的を確認。この論文はKHの出典でありRT原典ではない。

完了の根拠：

```json
{
  "verification": "/code/validated-examples/2026-11-23-r2/instability-growth/verification.json",
  "inputs": [
    "/code/validated-examples/2026-11-23-r2/instability-growth/inputs.json",
    "/code/validated-examples/2026-11-23-r2/instability-growth/acceptance.json",
    "/code/validated-examples/2026-11-23-r2/instability-growth/pre-run-contract.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-23-r2/instability-growth/results/kh-initial-growth-preview.png",
    "/code/validated-examples/2026-11-23-r2/instability-growth/results/rt-initial-growth-preview.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-23-r2/instability-growth/run.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-23-r2/instability-growth/README.md",
    "/code/validated-examples/2026-11-23-r2/instability-growth/references/citations.json",
    "/numerical-methods-atlas/validation/verification/2026-11-23-batch18-27-public.json"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#kh-initial-growth-ja",
  "execution": "/numerical-methods-atlas/validation/kh-initial-growth/?lang=ja"
}
```

## 非相対論的MHD・CT/GLM/HLLD

### 円偏波Alfvén波・磁場ループの独立比較と収束

ID: mhd-1 · P1 · 公開済み · 検証の拡充

調査時の範囲：検証範囲不足

調査時の現状：

固定した軽量段階をHRで公開。公開ファイル照合と全30補助版・71ケース・893pytestの公開ZIP Linux追試が合格。Saltzman／Williamsonを含む残る適用範囲はscope_noteと実行入口で区別します。

追加内容・最小の検証：

- 既存保存結果を基準に空間/時間系列を分離し、Alfvén位相誤差・偏波・保存量を解析波で測る。
- loopは独立コードと比較し、磁気エネルギー・ループ形状・divergence演算子を揃える。
- 他のOT追補の独立照合を旧loopの検証に流用しない。

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

固定した軽量ケースの実装・検証・保存図を追加。各不変配布版に入力・判定・保存配列・改訂と失敗の履歴を保持し、条件と対象外は各実行入口に明記します。

調査時の根拠：

- `catalog/atlas-test-problems.json` · circular-alfven/magnetic-loop
  問題・計算結果は収録済み、固定入力runner結び付けなし。
- `catalog/atlas-mhd-supplements.json` · historical_replacements
  旧loopの独立照合、強磁場、UCT-HLLDは未検証と明記。

- [Gardiner & Stone (2005), An Unsplit Godunov Method for Ideal MHD via CT](<https://arxiv.org/abs/astro-ph/0501557>)
  著者原稿の抄録・書誌で面平均B、共有corner EMF、CTU/PPM結合を確認。現在の算術flux-CTと同一実装とは呼ばない。

完了の根拠：

```json
{
  "verification": "/code/validated-examples/2026-11-23/mhd-transport/verification.json",
  "inputs": [
    "/code/validated-examples/2026-11-23/mhd-transport/inputs.json",
    "/code/validated-examples/2026-11-23/mhd-transport/acceptance.json",
    "/code/validated-examples/2026-11-23/mhd-transport/pre-run-contract.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-23/mhd-transport/results/circular-alfven-refinement-preview.png",
    "/code/validated-examples/2026-11-23/mhd-transport/results/magnetic-loop-independent-preview.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-23/mhd-transport/run.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-23/mhd-transport/README.md",
    "/code/validated-examples/2026-11-23/mhd-transport/references/citations.json",
    "/numerical-methods-atlas/validation/verification/2026-11-23-batch18-27-public.json"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#circular-alfven-ja",
  "execution": "/numerical-methods-atlas/validation/circular-alfven-refinement/?lang=ja"
}
```

### 衝撃波後OTまたは標準rotorの限定検証

ID: mhd-2 · P2 · 公開済み · 検証の拡充

調査時の範囲：検証範囲不足

調査時の現状：

固定した軽量段階をHRで公開。公開ファイル照合と全30補助版・71ケース・893pytestの公開ZIP Linux追試が合格。Saltzman／Williamsonを含む残る適用範囲はscope_noteと実行入口で区別します。

追加内容・最小の検証：

- 現行short smooth OTを残し、衝撃波を伴う別時刻/別入力を区別して追加。
- 熱圧正値性・総エネルギー・native face/common cell divB・参照格子増分を測る。
- rotorを採るなら新規問題として初期回転/磁場/境界を固定し、既存CTU/UCT実装の再現とは呼ばない。

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

固定した軽量ケースの実装・検証・保存図を追加。各不変配布版に入力・判定・保存配列・改訂と失敗の履歴を保持し、条件と対象外は各実行入口に明記します。

調査時の根拠：

- `numerical-methods-atlas/validation/index.json` · ct-glm-ot-convergence
  衝撃波後・3D・一般cleaning認証ではないと明記。
- `catalog/atlas-test-problems.json` · orszag-tang
  現行独立実行はある。rotor固有IDは未登録。

- [Gardiner & Stone (2005), An Unsplit Godunov Method for Ideal MHD via CT](<https://arxiv.org/abs/astro-ph/0501557>)
  著者原稿の抄録・書誌で面平均B、共有corner EMF、CTU/PPM結合を確認。現在の算術flux-CTと同一実装とは呼ばない。

完了の根拠：

```json
{
  "verification": "/code/validated-examples/2026-11-23/mhd-transport/verification.json",
  "inputs": [
    "/code/validated-examples/2026-11-23/mhd-transport/inputs.json",
    "/code/validated-examples/2026-11-23/mhd-transport/acceptance.json",
    "/code/validated-examples/2026-11-23/mhd-transport/pre-run-contract.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-23/mhd-transport/results/postshock-orszag-tang-preview.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-23/mhd-transport/run.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-23/mhd-transport/README.md",
    "/code/validated-examples/2026-11-23/mhd-transport/references/citations.json",
    "/numerical-methods-atlas/validation/verification/2026-11-23-batch18-27-public.json"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#orszag-tang-ja",
  "execution": "/numerical-methods-atlas/validation/postshock-orszag-tang/?lang=ja"
}
```

## 格子・座標・非構造FEM

### L字領域Poisson特異解と歪んだ三角形FEM

ID: mesh-coordinate-1 · P2 · 公開済み · 新規実装

調査時の範囲：未収録

調査時の現状：

固定した軽量段階をHRで公開。公開ファイル照合と全30補助版・71ケース・893pytestの公開ZIP Linux追試が合格。Saltzman／Williamsonを含む残る適用範囲はscope_noteと実行入口で区別します。

追加内容・最小の検証：

- r^(2/3)sin(2theta/3)型のreentrant corner解などを境界条件とともに自前定義し、L2/H1誤差を要素積分。
- 一様/局所細分化、要素角度・aspect ratio・条件数の影響を分ける。
- 単位正方形の滑らかな2次L2収束を特異解や不規則格子に一般化しない。

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

固定した軽量ケースの実装・検証・保存図を追加。各不変配布版に入力・判定・保存配列・改訂と失敗の履歴を保持し、条件と対象外は各実行入口に明記します。

調査時の根拠：

- `catalog/atlas-test-problems.json` · poisson-2d-sine
  現基準は滑らかな正弦。
- `numerical-methods-atlas/en/read/meshes/index.html` · meshes
  Matplotlib三角形分割と幾何展示で、Triangle/一般非構造flow solverではない。

- [Shewchuk (1996), Triangle: Engineering a 2D Quality Mesh Generator](<https://www.cs.cmu.edu/~quake/tripaper/triangle0.html>)
  著者公開原著の書誌と算法/品質/robust predicatesの節構成を確認。現コードはMatplotlib triangulationでありTriangle利用ではない。
- [Salari & Knupp, Code Verification by the Method of Manufactured Solutions, SAND2000-1444](<https://www.sandia.gov/research/publications/details/code-verification-by-the-method-of-manufactured-solutions-2000-06-01/>)
  Sandia公式報告の書誌・概要・DOI10.2172/759450を確認。製造解の検証方法の出典で、個別の初等解の発見原著として扱わない。

完了の根拠：

```json
{
  "verification": "/code/validated-examples/2026-11-23/mesh-boundary/verification.json",
  "inputs": [
    "/code/validated-examples/2026-11-23/mesh-boundary/inputs.json",
    "/code/validated-examples/2026-11-23/mesh-boundary/acceptance.json",
    "/code/validated-examples/2026-11-23/mesh-boundary/pre-run-contract.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-23/mesh-boundary/results/lshape-fem-preview.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-23/mesh-boundary/run.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-23/mesh-boundary/README.md",
    "/code/validated-examples/2026-11-23/mesh-boundary/references/citations.json",
    "/numerical-methods-atlas/validation/verification/2026-11-23-batch18-27-public.json"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#lshape-fem-ja",
  "execution": "/numerical-methods-atlas/validation/lshape-fem/?lang=ja"
}
```

### 円筒・曲線座標の環状領域PDE製造解

ID: mesh-coordinate-2 · P2 · 公開済み · 検証の拡充

調査時の範囲：検証範囲不足

調査時の現状：

固定した軽量段階をHRで公開。公開ファイル照合と全30補助版・71ケース・893pytestの公開ZIP Linux追試が合格。Saltzman／Williamsonを含む残る適用範囲はscope_noteと実行入口で区別します。

追加内容・最小の検証：

- まずr>0のannulusで粘性応力発散・可変粘性・境界fluxを一組の製造解で離散化検査。
- 座標の物理/共変/反変成分と体積/面積重みを固定し、格子収束を測る。
- 軸を含む場合は正則性とaxis stencilを別テストにする。平面Poiseuille/Couetteを円筒問題の同一参照にしない。

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

固定した軽量ケースの実装・検証・保存図を追加。各不変配布版に入力・判定・保存配列・改訂と失敗の履歴を保持し、条件と対象外は各実行入口に明記します。

調査時の根拠：

- `code/numerical-methods-atlas/2026-11-21/numart/coordinates.py` · cylindrical_velocity_gradient/cylindrical_stress_divergence
  r=0を拒否する点演算子。
- `catalog/atlas-chapter-links.json` · coordinates-viscosity
  現対応はソース/恒等式検査のみ。

- [Salari & Knupp, Code Verification by the Method of Manufactured Solutions, SAND2000-1444](<https://www.sandia.gov/research/publications/details/code-verification-by-the-method-of-manufactured-solutions-2000-06-01/>)
  Sandia公式報告の書誌・概要・DOI10.2172/759450を確認。製造解の検証方法の出典で、個別の初等解の発見原著として扱わない。

完了の根拠：

```json
{
  "verification": "/code/validated-examples/2026-11-23/mesh-boundary/verification.json",
  "inputs": [
    "/code/validated-examples/2026-11-23/mesh-boundary/inputs.json",
    "/code/validated-examples/2026-11-23/mesh-boundary/acceptance.json",
    "/code/validated-examples/2026-11-23/mesh-boundary/pre-run-contract.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-23/mesh-boundary/results/annular-viscous-mms-preview.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-23/mesh-boundary/run.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-23/mesh-boundary/README.md",
    "/code/validated-examples/2026-11-23/mesh-boundary/references/citations.json",
    "/numerical-methods-atlas/validation/verification/2026-11-23-batch18-27-public.json"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#annular-viscous-mms-ja",
  "execution": "/numerical-methods-atlas/validation/annular-viscous-mms/?lang=ja"
}
```

## ALE・地球流体・球面格子

### 非一様移動格子輸送、その後Saltzman歪み格子ピストン

ID: ale-geophysical-1 · P2 · 検証済み · 検証の拡充

調査時の範囲：検証範囲不足

調査時の現状：

固定した軽量段階をHRで公開。公開ファイル照合と全30補助版・71ケース・893pytestの公開ZIP Linux追試が合格。Saltzman／Williamsonを含む残る適用範囲はscope_noteと実行入口で区別します。

追加内容・最小の検証：

- 最初は既存GCLと同じ移動に非一様scalarの解析輸送を載せ、幾何誤差と輸送誤差を分離。
- Lagrange/remapまで拡張する段階でSaltzmanを新規問題として考慮し、格子反転・歪み・保存・衝撃位置を検査。
- 現在のALE一様状態チェックを完全Euler/remap実装と呼ばない。Saltzman原典/入力は別途照合が必要。

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

既存の非一様ALEスカラー輸送・GCL検証に追加。今回の限定範囲：Tan–Lv–Zhu(2023) Example8の有限初期圧力e0=1e-4に対応する所与アフィンALEの2D Eulerピストン。変形セル体積平均のRH参照、GCL、境界仕事と保存を固定2格子で検査。物質追従Lagrange/WENO/remapではありません。

調査時の根拠：

- `code/numerical-methods-atlas/2026-11-21/numart/geometry.py` · moving_volume_uniform_test
  一様状態のみ。
- `catalog/atlas-test-problems.json`
  Saltzman登録なし。

- [Salari & Knupp, Code Verification by the Method of Manufactured Solutions, SAND2000-1444](<https://www.sandia.gov/research/publications/details/code-verification-by-the-method-of-manufactured-solutions-2000-06-01/>)
  Sandia公式報告の書誌・概要・DOI10.2172/759450を確認。製造解の検証方法の出典で、個別の初等解の発見原著として扱わない。

完了の根拠：

```json
{
  "verification": "/code/validated-examples/2026-11-25/continuum-particle-controls/verification.json",
  "inputs": [
    "/code/validated-examples/2026-11-25/continuum-particle-controls/inputs.json",
    "/code/validated-examples/2026-11-25/continuum-particle-controls/acceptance.json",
    "/code/validated-examples/2026-11-25/continuum-particle-controls/freeze.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-25/continuum-particle-controls/results/saltzman-ale-piston-preview.png",
    "/code/validated-examples/2026-11-25/continuum-particle-controls/results/saltzman-ale-piston.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-25/continuum-particle-controls/run.py",
    "/code/validated-examples/2026-11-25/continuum-particle-controls/ale_piston.py",
    "/code/validated-examples/2026-11-25/continuum-particle-controls/failure_support.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-25/continuum-particle-controls/source-reading.json",
    "/numerical-methods-atlas/solutions/?lang=ja#solution-saltzman-ale-piston-ja"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#saltzman-ale-piston-ja",
  "execution": "/numerical-methods-atlas/validation/saltzman-ale-piston/?lang=ja",
  "case_ids": [
    "saltzman-ale-piston"
  ],
  "primary_diagnostics": [
    {
      "path": "/code/validated-examples/2026-11-25/continuum-particle-controls/results/result.json",
      "case_id": "saltzman-ale-piston",
      "json_pointer": "/cases/0",
      "source_sha256": "cab002c93e01d997562f3c145e1aaddd6a2a8ce59a087d44e8bddc4679081bbf",
      "input_sha256": "5f49881f37b07c47f674979a4886e6da0421be06ddb6bb213ab7dfea6bf6e0f5"
    }
  ]
}
```

### 回転浅水波の時間積分→Williamsonの限定した球面ケース

ID: ale-geophysical-2 · P2 · 検証済み · 検証の拡充

調査時の範囲：検証範囲不足

調査時の現状：

固定した軽量段階をHRで公開。公開ファイル照合と全30補助版・71ケース・893pytestの公開ZIP Linux追試が合格。Saltzman／Williamsonを含む残る適用範囲はscope_noteと実行入口で区別します。

追加内容・最小の検証：

- まず既存f-planeの一つの固有modeを実際に時間積分し位相・振幅・geostrophic balanceを解析行列指数と比較。
- 球面拡張時はWilliamsonの固体回転輸送/定常釣合いから段階的に選び、質量/エネルギー/位相と格子向きを比較。
- A/B/C配置だけで時間精度・PV保存・全球dynamical coreの完成を主張しない。

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

既存の平面C格子・線形回転浅水波の検証に追加。今回の限定範囲：単位球の剛体回転スカラー輸送を2傾斜・2格子・各11remapで検査し、別に無次元軸対称SWEの定常釣合いを時間積分。非保存SLの質量ずれを保存し、原W92式の閲読や標準地球条件・全球dynamical core/PV保存を主張しません。

調査時の根拠：

- `code/numerical-methods-atlas/2026-11-21/numart/geophysical_grids.py` · symbol/gravity_frequency
  半離散記号。
- `code/numerical-methods-atlas/2026-11-21/tests/test_geophysical_grids.py` · test_fourier_symbol_matches_independent_physical_grid_stencils
  現有の独立空間演算子照合を保持。

- [MITgcm official documentation, C grid staggering of variables](<https://mitgcm.readthedocs.io/en/latest/algorithm/c-grid.html>)
  公式現行ドキュメントのC-grid配置を確認。MITgcm全体の再現ではない。
- [Williamson et al. (1992), A standard test set for spherical shallow water](<https://www.sciencedirect.com/science/article/pii/S0021999105800166>)
  出版社書誌・抄録で七つの段階的テストを確認。全球SWEの実装を現在の球面格子幾何テストから推定しない。

完了の根拠：

```json
{
  "verification": "/code/validated-examples/2026-11-25/continuum-particle-controls/verification.json",
  "inputs": [
    "/code/validated-examples/2026-11-25/continuum-particle-controls/inputs.json",
    "/code/validated-examples/2026-11-25/continuum-particle-controls/acceptance.json",
    "/code/validated-examples/2026-11-25/continuum-particle-controls/freeze.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-25/continuum-particle-controls/results/williamson-sphere-transport-preview.png",
    "/code/validated-examples/2026-11-25/continuum-particle-controls/results/williamson-sphere-transport.png",
    "/code/validated-examples/2026-11-25/continuum-particle-controls/results/sphere-zonal-balance-preview.png",
    "/code/validated-examples/2026-11-25/continuum-particle-controls/results/sphere-zonal-balance.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-25/continuum-particle-controls/run.py",
    "/code/validated-examples/2026-11-25/continuum-particle-controls/sphere.py",
    "/code/validated-examples/2026-11-25/continuum-particle-controls/failure_support.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-25/continuum-particle-controls/source-reading.json",
    "/numerical-methods-atlas/solutions/?lang=ja#solution-williamson-sphere-transport-ja",
    "/numerical-methods-atlas/solutions/?lang=ja#solution-sphere-zonal-balance-ja"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#williamson-sphere-transport-ja",
  "execution": "/numerical-methods-atlas/validation/williamson-sphere-transport/?lang=ja",
  "case_ids": [
    "williamson-sphere-transport",
    "sphere-zonal-balance"
  ],
  "primary_diagnostics": [
    {
      "path": "/code/validated-examples/2026-11-25/continuum-particle-controls/results/result.json",
      "case_id": "williamson-sphere-transport",
      "json_pointer": "/cases/1",
      "source_sha256": "cab002c93e01d997562f3c145e1aaddd6a2a8ce59a087d44e8bddc4679081bbf",
      "input_sha256": "5f49881f37b07c47f674979a4886e6da0421be06ddb6bb213ab7dfea6bf6e0f5"
    },
    {
      "path": "/code/validated-examples/2026-11-25/continuum-particle-controls/results/result.json",
      "case_id": "sphere-zonal-balance",
      "json_pointer": "/cases/2",
      "source_sha256": "cab002c93e01d997562f3c145e1aaddd6a2a8ce59a087d44e8bddc4679081bbf",
      "input_sha256": "5f49881f37b07c47f674979a4886e6da0421be06ddb6bb213ab7dfea6bf6e0f5"
    }
  ],
  "additional_executions": [
    "/numerical-methods-atlas/validation/sphere-zonal-balance/?lang=ja"
  ],
  "additional_galleries": [
    "/numerical-methods-atlas/gallery/?lang=ja#sphere-zonal-balance-ja"
  ]
}
```

## 相対論的流体・SRMHD

### Martí–Müller型1D相対論衝撃管

ID: relativistic-fluid-1 · P2 · 公開済み · 新規実装

調査時の範囲：解説のみ

調査時の現状：

固定した軽量段階をHRで公開。公開ファイル照合と全30補助版・71ケース・893pytestの公開ZIP Linux追試が合格。Saltzman／Williamsonを含む残る適用範囲はscope_noteと実行入口で区別します。

追加内容・最小の検証：

- まずMinkowski・理想気体EOS・法線速度のみの少数固定入力。
- 原始変数回復の残差、rho/p正値、|v|<1、波位置、中間状態をexact Riemann参照と比較。
- 物理/保存変数とセル平均/点値を明示し、GR時空や任意EOSの検証へ拡張解釈しない。

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

固定した軽量ケースの実装・検証・保存図を追加。各不変配布版に入力・判定・保存配列・改訂と失敗の履歴を保持し、条件と対象外は各実行入口に明記します。

調査時の根拠：

- `numerical-methods-atlas/equations/index.json` · srhd
  代表式はあるが実行なし。

- [Martí & Müller (1994), The analytical solution of the Riemann problem in relativistic hydrodynamics](<https://www.cambridge.org/core/journals/journal-of-fluid-mechanics/article/abs/analytical-solution-of-the-riemann-problem-in-relativistic-hydrodynamics/ACFB60CD3557DF2AF8AFF6B72D8B03A4>)
  出版社書誌・抄録でMinkowski時空・polytropic gas・中間圧力の暗黙代数方程式を確認。1994出版と2006電子公開日を区別。

完了の根拠：

```json
{
  "verification": "/code/validated-examples/2026-11-23/relativistic/verification.json",
  "inputs": [
    "/code/validated-examples/2026-11-23/relativistic/inputs.json",
    "/code/validated-examples/2026-11-23/relativistic/acceptance.json",
    "/code/validated-examples/2026-11-23/relativistic/pre-run-contract.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-23/relativistic/results/srhd-collision-preview.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-23/relativistic/run.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-23/relativistic/README.md",
    "/code/validated-examples/2026-11-23/relativistic/references/citations.json",
    "/numerical-methods-atlas/validation/verification/2026-11-23-batch18-27-public.json"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#srhd-collision-ja",
  "execution": "/numerical-methods-atlas/validation/srhd-collision/?lang=ja"
}
```

### SRMHDの固定Riemann/Alfvénケース

ID: relativistic-fluid-2 · P3 · 公開済み · 新規実装

調査時の範囲：未収録

調査時の現状：

固定した軽量段階をHRで公開。公開ファイル照合と全30補助版・71ケース・893pytestの公開ZIP Linux追試が合格。Saltzman／Williamsonを含む残る適用範囲はscope_noteと実行入口で区別します。

追加内容・最小の検証：

- SRHDの保存・回復が通った後、固定EOSで簡単な磁場配置から開始。
- Bx一定、物理的状態、波位置、磁場/流体相互作用を独立exact RMHD参照と照合。
- B→0極限はSRHDと整合を検査し、非相対論HLLD実装の名前をそのままSRMHD実装扱いしない。

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

固定した軽量ケースの実装・検証・保存図を追加。各不変配布版に入力・判定・保存配列・改訂と失敗の履歴を保持し、条件と対象外は各実行入口に明記します。

調査時の根拠：

- `numerical-methods-atlas/equations/index.json` · grmhd
  文献説明のみ、SRMHD固有カード/runnerなし。
- `catalog/atlas-methods.json` · hlld
  既存はideal nonrelativistic MHD。

- [Giacomazzo & Rezzolla (2006), Exact Riemann solution in relativistic MHD](<https://www.cambridge.org/core/journals/journal-of-fluid-mechanics/article/exact-solution-of-the-riemann-problem-in-relativistic-magnetohydrodynamics/96301C50DDB8E673859CF715B0813F3B>)
  出版社書誌・抄録で三波と一般七波の場合を確認。DOI10.1017/S0022112006001145。著者公式配布ページも確認できるが数値参照は未生成。

完了の根拠：

```json
{
  "verification": "/code/validated-examples/2026-11-23/relativistic/verification.json",
  "inputs": [
    "/code/validated-examples/2026-11-23/relativistic/inputs.json",
    "/code/validated-examples/2026-11-23/relativistic/acceptance.json",
    "/code/validated-examples/2026-11-23/relativistic/pre-run-contract.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-23/relativistic/results/srmhd-alfven-preview.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-23/relativistic/run.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-23/relativistic/README.md",
    "/code/validated-examples/2026-11-23/relativistic/references/citations.json",
    "/numerical-methods-atlas/validation/verification/2026-11-23-batch18-27-public.json"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#srmhd-alfven-ja",
  "execution": "/numerical-methods-atlas/validation/srmhd-alfven/?lang=ja"
}
```

## 楕円型・Poisson

### 2Dの純Neumann・混合Robin製造解を、互換条件と平均値ゲージ込みで固定入力化

ID: elliptic-poisson-1 · P1 · 公開済み · 検証の拡充

調査時の範囲：検証範囲不足

調査時の現状：

固定した軽量段階をHRで公開。公開ファイル照合と全30補助版・71ケース・893pytestの公開ZIP Linux追試が合格。Saltzman／Williamsonを含む残る適用範囲はscope_noteと実行入口で区別します。

追加内容・最小の検証：

- 既存1D境界実装と区別し、2Dの零空間・不適合右辺の拒否・平均値指定を検査
- 2D CG/MGの現状は零Dirichlet。cos型参照解で境界誤差と残差を分ける

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

固定した軽量ケースの実装・検証・保存図を追加。各不変配布版に入力・判定・保存配列・改訂と失敗の履歴を保持し、条件と対象外は各実行入口に明記します。

調査時の根拠：

- `catalog/atlas-methods.json` · cg.limitations,multigrid.limitations
- `code/numerical-methods-atlas/2026-11-21/numart/linear.py` · poisson_boundary_1d

- [PETSc公式: Singular systems / Neumann nullspace](<https://petsc.org/release/manual/ksp/>)
  一次論文の出版社ページまたは公式資料を検索・確認。全文監査や数値再現ではない。
- [MFEM公式: Example 27 Laplace boundary conditions](<https://mfem.org/examples/>)
  一次論文の出版社ページまたは公式資料を検索・確認。全文監査や数値再現ではない。

完了の根拠：

```json
{
  "verification": "/code/validated-examples/2026-11-23/mesh-boundary/verification.json",
  "inputs": [
    "/code/validated-examples/2026-11-23/mesh-boundary/inputs.json",
    "/code/validated-examples/2026-11-23/mesh-boundary/acceptance.json",
    "/code/validated-examples/2026-11-23/mesh-boundary/pre-run-contract.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-23/mesh-boundary/results/poisson-neumann-preview.png",
    "/code/validated-examples/2026-11-23/mesh-boundary/results/poisson-robin-preview.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-23/mesh-boundary/run.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-23/mesh-boundary/README.md",
    "/code/validated-examples/2026-11-23/mesh-boundary/references/citations.json",
    "/numerical-methods-atlas/validation/verification/2026-11-23-batch18-27-public.json"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#poisson-neumann-ja",
  "execution": "/numerical-methods-atlas/validation/poisson-neumann/?lang=ja"
}
```

### checkerboard係数ジャンプ／回転異方性拡散のMG・AMG比較

ID: elliptic-poisson-3 · P2 · 公開済み · 検証の拡充

調査時の範囲：検証範囲不足

調査時の現状：

固定範囲をHRで公開。最終SHAの全38群83ケース1047pytest、サイト543件が合格。初期公開の画面確認と新版HTTP差分確認、Linux失敗2件、DSMC性能修正版を区別して保持。Thomas1949原報は未読の文献整理で数値例なし。

追加内容・最小の検証：

- 既存amg-conditioningの定係数異方性を再追加しない
- 不連続係数の流束整合、真の残差・前進誤差・収束不達を固定ケースで比較

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

各例の前提・参照の独立範囲と未達版の履歴を、入力・受入基準・契約・検証記録で区別します。一般条件への認証や厳密解でない数値参照の厳密性は主張しません。

調査時の根拠：

- `code/validated-examples/2026-11-22/foundations-conditioning/cases.json` · amg-conditioning.limits
- `catalog/atlas-methods.json` · multigrid.limitations

- [PETSc公式: Singular systems / Neumann nullspace](<https://petsc.org/release/manual/ksp/>)
  一次論文の出版社ページまたは公式資料を検索・確認。全文監査や数値再現ではない。

完了の根拠：

```json
{
  "verification": "/numerical-methods-atlas/validation/verification/2026-11-24-batch28-37-public.json",
  "inputs": [
    "/code/validated-examples/2026-11-23/coefficient-diffusion/inputs.json",
    "/code/validated-examples/2026-11-23/coefficient-diffusion/acceptance.json",
    "/code/validated-examples/2026-11-23/coefficient-diffusion/pre-run-contract.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-23/coefficient-diffusion/results/checkerboard-diffusion-preview.png",
    "/code/validated-examples/2026-11-23/coefficient-diffusion/results/rotated-anisotropic-diffusion-preview.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-23/coefficient-diffusion/run.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-23/coefficient-diffusion/README.md",
    "/code/validated-examples/2026-11-23/coefficient-diffusion/verification.json",
    "/numerical-methods-atlas/validation/verification/2026-11-24-batch28-37-public.json"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#checkerboard-diffusion-ja",
  "execution": "/numerical-methods-atlas/validation/checkerboard-diffusion/?lang=ja"
}
```

### Thomas法の原報と再録・関連章文献の役割整理

ID: elliptic-poisson-4 · P2 · 公開済み · 参照・出典の整備

調査時の範囲：出典整備不足

調査時の現状：

固定範囲をHRで公開。最終SHAの全38群83ケース1047pytest、サイト543件が合格。初期公開の画面確認と新版HTTP差分確認、Linux失敗2件、DSMC性能修正版を区別して保持。Thomas1949原報は未読の文献整理で数値例なし。

追加内容・最小の検証：

- 台帳のThomasリンクはCrank–Nicolson/多重格子文献が中心
- 既存実行記録の『Thomas原報は未確認』を維持し、原報確認ができたときだけアクセス深度を更新

完了条件：

- 対象の本文・台帳と修正した箇所が確認できる。
- 出典・書誌・適用範囲の修正根拠と確認記録を残す。
- 実在する対象と根拠を照合してから完了にする。

目録の確認を原報本文の確認と扱わず、不明なDOI・報告番号・頁はnullのまま。原報未読を維持した文献役割の整理です。

調査時の根拠：

- `catalog/atlas-methods.json` · thomas.references
- `catalog/atlas-execution-examples.json` · poisson-1d-dirichlet.reference_notes


完了の根拠：

```json
{
  "targets": [
    "/numerical-methods-atlas/methods/thomas/?lang=ja",
    "/catalog/atlas-methods.json"
  ],
  "proof": [
    "/numerical-methods-atlas/reading/thomas-provenance.json"
  ],
  "note": {
    "ja": "目録の確認を原報本文の確認と扱わず、不明なDOI・報告番号・頁はnullのまま。原報未読を維持した文献役割の整理です。",
    "en": "Curation of bibliographic roles only; original1949 full text unread,unknown DOI/report/pages remain null. No new scientific case."
  },
  "publication_verification": "/numerical-methods-atlas/validation/verification/2026-11-24-batch28-37-public.json"
}
```

## 重力・周期静電場・多重極

### 中性スラブのYeh–Berkowitz補正／2D周期境界ベンチマーク

ID: gravity-electrostatics-multipole-1 · P2 · 公開済み · 新規実装

調査時の範囲：解説のみ

調査時の現状：

固定範囲をHRで公開。最終SHAの全38群83ケース1047pytest、サイト543件が合格。初期公開の画面確認と新版HTTP差分確認、Linux失敗2件、DSMC性能修正版を区別して保持。Thomas1949原報は未読の文献整理で数値例なし。

追加内容・最小の検証：

- slab-ewaldはplannedで詳細解説あり、通常の中性立方Ewald実装とは区別
- 真空層厚依存・双極子補正・力の有限差分・独立2D参照を小ケースで検査

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

各例の前提・参照の独立範囲と未達版の履歴を、入力・受入基準・契約・検証記録で区別します。一般条件への認証や厳密解でない数値参照の厳密性は主張しません。

調査時の根拠：

- `catalog/atlas-methods.json` · slab-ewald
- `code/validated-examples/2026-11-22/particle-transport/cases.json` · ewald-convergence.limits

- [Yeh & Berkowitz (1999), Ewald summation for systems with slab geometry](<https://pubs.aip.org/jcp/article/111/7/3155/294442/Ewald-summation-for-systems-with-slab-geometry>)
  DOI 10.1063/1.479595と出版社への解決先を確認。本文取得はツールで失敗。既存原著台帳yeh1999にも書誌情報あり。

完了の根拠：

```json
{
  "verification": "/numerical-methods-atlas/validation/verification/2026-11-24-batch28-37-public.json",
  "inputs": [
    "/code/validated-examples/2026-11-23/slab-ewald/inputs.json",
    "/code/validated-examples/2026-11-23/slab-ewald/acceptance.json",
    "/code/validated-examples/2026-11-23/slab-ewald/pre-run-contract.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-23/slab-ewald/results/neutral-slab-yb-preview.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-23/slab-ewald/run.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-23/slab-ewald/README.md",
    "/code/validated-examples/2026-11-23/slab-ewald/verification.json",
    "/numerical-methods-atlas/validation/verification/2026-11-24-batch28-37-public.json"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#neutral-slab-yb-ja",
  "execution": "/numerical-methods-atlas/validation/neutral-slab-yb/?lang=ja"
}
```

### 3D 1/r核／適応木のFMM

ID: gravity-electrostatics-multipole-2 · P3 · 公開済み · 検証の拡充

調査時の範囲：検証範囲不足

調査時の現状：

固定範囲をHRで公開。最終SHAの全38群83ケース1047pytest、サイト543件が合格。初期公開の画面確認と新版HTTP差分確認、Linux失敗2件、DSMC性能修正版を区別して保持。Thomas1949原報は未読の文献整理で数値例なし。

追加内容・最小の検証：

- 既存FMMは2D自由空間log核で、3D重力用FMMではない
- 一様球など解析配置・直接和・次数/木深さを分け、必要用途が出た時に範囲拡張

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

各例の前提・参照の独立範囲と未達版の履歴を、入力・受入基準・契約・検証記録で区別します。一般条件への認証や厳密解でない数値参照の厳密性は主張しません。

調査時の根拠：

- `catalog/atlas-methods.json` · fmm.limitations
- `code/validated-examples/2026-11-22/particle-transport/cases.json` · fmm-convergence


完了の根拠：

```json
{
  "verification": "/numerical-methods-atlas/validation/verification/2026-11-24-batch28-37-public.json",
  "inputs": [
    "/code/validated-examples/2026-11-23/fmm3d/inputs.json",
    "/code/validated-examples/2026-11-23/fmm3d/acceptance.json",
    "/code/validated-examples/2026-11-23/fmm3d/pre-run-contract.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-23/fmm3d/results/fmm3d-inverse-r-preview.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-23/fmm3d/run.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-23/fmm3d/README.md",
    "/code/validated-examples/2026-11-23/fmm3d/verification.json",
    "/numerical-methods-atlas/validation/verification/2026-11-24-batch28-37-public.json"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#fmm3d-inverse-r-ja",
  "execution": "/numerical-methods-atlas/validation/fmm3d-inverse-r/?lang=ja"
}
```

### Plummer球の短時間力学／2体軌道の重力時間積分

ID: gravity-electrostatics-multipole-3 · P2 · 公開済み · 検証の拡充

調査時の範囲：検証範囲不足

調査時の現状：

固定範囲をHRで公開。最終SHAの全38群83ケース1047pytest、サイト543件が合格。初期公開の画面確認と新版HTTP差分確認、Linux失敗2件、DSMC性能修正版を区別して保持。Thomas1949原報は未読の文献整理で数値例なし。

追加内容・最小の検証：

- 現Barnes–Hut固定例は静的力のみ
- 同一軟化核で軌道・エネルギー/運動量の時間誤差と木近似誤差を分ける。長時間・大粒子数走査は後段

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

各例の前提・参照の独立範囲と未達版の履歴を、入力・受入基準・契約・検証記録で区別します。一般条件への認証や厳密解でない数値参照の厳密性は主張しません。

調査時の根拠：

- `catalog/atlas-execution-examples.json` · barnes-hut.scope
- `catalog/atlas-methods.json` · barnes-hut.limitations

- [Barnes & Hut (1986), A hierarchical O(N log N) force-calculation algorithm](<https://www.nature.com/articles/324446a0>)
  出版社の検索結果・抄録を確認。直接openは認証リダイレクトのため失敗。

完了の根拠：

```json
{
  "verification": "/numerical-methods-atlas/validation/verification/2026-11-24-batch28-37-public.json",
  "inputs": [
    "/code/validated-examples/2026-11-23/gravity-dynamics/inputs.json",
    "/code/validated-examples/2026-11-23/gravity-dynamics/acceptance.json",
    "/code/validated-examples/2026-11-23/gravity-dynamics/pre-run-contract.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-23/gravity-dynamics/results/gravity-kepler-preview.png",
    "/code/validated-examples/2026-11-23/gravity-dynamics/results/gravity-plummer-short-preview.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-23/gravity-dynamics/run.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-23/gravity-dynamics/README.md",
    "/code/validated-examples/2026-11-23/gravity-dynamics/verification.json",
    "/numerical-methods-atlas/validation/verification/2026-11-24-batch28-37-public.json"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#gravity-kepler-ja",
  "execution": "/numerical-methods-atlas/validation/gravity-kepler/?lang=ja"
}
```

## PIC・プラズマ

### 線形Landau減衰

ID: pic-1 · P1 · 公開済み · 新規実装

調査時の範囲：未収録

調査時の現状：

固定範囲をHRで公開。最終SHAの全38群83ケース1047pytest、サイト543件が合格。初期公開の画面確認と新版HTTP差分確認、Linux失敗2件、DSMC性能修正版を区別して保持。Thomas1949原報は未読の文献整理で数値例なし。

追加内容・最小の検証：

- 1D1Vの弱い摂動で電場振幅の減衰率・周波数を解析分散関係と照合
- 粒子雑音・速度分布標本化・格子/刻みの誤差を分離

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

各例の前提・参照の独立範囲と未達版の履歴を、入力・受入基準・契約・検証記録で区別します。一般条件への認証や厳密解でない数値参照の厳密性は主張しません。

調査時の根拠：

- `catalog/atlas-methods.json` · pic.limitations
- `code/validated-examples/2026-11-22/particle-transport/cases.json` · pic-conservation.limits

- [Kraus et al. (2017), GEMPIC: geometric electromagnetic particle-in-cell methods](<https://www.cambridge.org/core/journals/journal-of-plasma-physics/article/gempic-geometric-electromagnetic-particleincell-methods/C32D97F1B5281878F094B7E5075D291A>)
  出版社本文のLandau damping・Weibel検証節を確認。掲載された大規模設定の再現を推奨する意味ではない。

完了の根拠：

```json
{
  "verification": "/numerical-methods-atlas/validation/verification/2026-11-24-batch28-37-public.json",
  "inputs": [
    "/code/validated-examples/2026-11-23/warm-pic/inputs.json",
    "/code/validated-examples/2026-11-23/warm-pic/acceptance.json",
    "/code/validated-examples/2026-11-23/warm-pic/pre-run-contract.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-23/warm-pic/results/thermal-landau-damping-preview.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-23/warm-pic/run.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-23/warm-pic/README.md",
    "/code/validated-examples/2026-11-23/warm-pic/verification.json",
    "/numerical-methods-atlas/validation/verification/2026-11-24-batch28-37-public.json"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#thermal-landau-damping-ja",
  "execution": "/numerical-methods-atlas/validation/thermal-landau-damping/?lang=ja"
}
```

### two-stream不安定性

ID: pic-2 · P2 · 公開済み · 新規実装

調査時の範囲：未収録

調査時の現状：

固定範囲をHRで公開。最終SHAの全38群83ケース1047pytest、サイト543件が合格。初期公開の画面確認と新版HTTP差分確認、Linux失敗2件、DSMC性能修正版を区別して保持。Thomas1949原報は未読の文献整理で数値例なし。

追加内容・最小の検証：

- 線形成長率と非線形飽和を別指標にし、速度分布・粒子数依存を固定入力化
- 冷たいcos(t)振動への合格を成長問題の検証に流用しない

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

各例の前提・参照の独立範囲と未達版の履歴を、入力・受入基準・契約・検証記録で区別します。一般条件への認証や厳密解でない数値参照の厳密性は主張しません。

調査時の根拠：

- `code/validated-examples/2026-11-22/particles/cases.json` · pic.limits

- [Kraus et al. (2017), GEMPIC: geometric electromagnetic particle-in-cell methods](<https://www.cambridge.org/core/journals/journal-of-plasma-physics/article/gempic-geometric-electromagnetic-particleincell-methods/C32D97F1B5281878F094B7E5075D291A>)
  出版社本文のLandau damping・Weibel検証節を確認。掲載された大規模設定の再現を推奨する意味ではない。

完了の根拠：

```json
{
  "verification": "/numerical-methods-atlas/validation/verification/2026-11-24-batch28-37-public.json",
  "inputs": [
    "/code/validated-examples/2026-11-23/warm-pic/inputs.json",
    "/code/validated-examples/2026-11-23/warm-pic/acceptance.json",
    "/code/validated-examples/2026-11-23/warm-pic/pre-run-contract.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-23/warm-pic/results/thermal-two-stream-preview.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-23/warm-pic/run.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-23/warm-pic/README.md",
    "/code/validated-examples/2026-11-23/warm-pic/verification.json",
    "/numerical-methods-atlas/validation/verification/2026-11-24-batch28-37-public.json"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#thermal-two-stream-ja",
  "execution": "/numerical-methods-atlas/validation/thermal-two-stream/?lang=ja"
}
```

### PIC空間離散そのものの独立実装照合

ID: pic-3 · P2 · 公開済み · 検証の拡充

調査時の範囲：検証範囲不足

調査時の現状：

固定範囲をHRで公開。最終SHAの全38群83ケース1047pytest、サイト543件が合格。初期公開の画面確認と新版HTTP差分確認、Linux失敗2件、DSMC性能修正版を区別して保持。Thomas1949原報は未読の文献整理で数値例なし。

追加内容・最小の検証：

- 現DOP853は時間参照であり、独立PIC空間実装ではない
- 同じ初期粒子・電荷割当・離散Poisson規約をそろえた小ケースを第三者実装または別実装で照合

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

既存cold-plasma-picに結び付く空間演算の独立実装検査です。小さい温速度を含む固定入力で、冷たい振動の解析解や連続極限の再検証とは区別します。

調査時の根拠：

- `code/validated-examples/2026-11-22/particle-transport/cases.json` · pic-conservation.limits

- [Kraus et al. (2017), GEMPIC: geometric electromagnetic particle-in-cell methods](<https://www.cambridge.org/core/journals/journal-of-plasma-physics/article/gempic-geometric-electromagnetic-particleincell-methods/C32D97F1B5281878F094B7E5075D291A>)
  出版社本文のLandau damping・Weibel検証節を確認。掲載された大規模設定の再現を推奨する意味ではない。

完了の根拠：

```json
{
  "verification": "/numerical-methods-atlas/validation/verification/2026-11-24-batch28-37-public.json",
  "inputs": [
    "/code/validated-examples/2026-11-23/pic-spatial/inputs.json",
    "/code/validated-examples/2026-11-23/pic-spatial/acceptance.json",
    "/code/validated-examples/2026-11-23/pic-spatial/pre-run-contract.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-23/pic-spatial/results/pic-independent-spatial-preview.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-23/pic-spatial/run.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-23/pic-spatial/README.md",
    "/code/validated-examples/2026-11-23/pic-spatial/verification.json",
    "/numerical-methods-atlas/validation/verification/2026-11-24-batch28-37-public.json"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#cold-plasma-pic-ja",
  "execution": "/numerical-methods-atlas/validation/pic-independent-spatial/?lang=ja"
}
```

## DSMC・希薄気体

### 平板Couette流／Fourier熱伝導の希薄気体ベンチマーク

ID: dsmc-1 · P1 · 公開済み · 新規実装

調査時の範囲：未収録

調査時の現状：

固定範囲をHRで公開。最終SHAの全38群83ケース1047pytest、サイト543件が合格。初期公開の画面確認と新版HTTP差分確認、Linux失敗2件、DSMC性能修正版を区別して保持。Thomas1949原報は未読の文献整理で数値例なし。

追加内容・最小の検証：

- まず小さい1D空間・3D速度系で壁散乱、Knudsen層、せん断応力/熱流束を確認
- セル幅/平均自由行程、刻み/衝突時間、粒子数と独立seed誤差を分ける

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

各例の前提・参照の独立範囲と未達版の履歴を、入力・受入基準・契約・検証記録で区別します。一般条件への認証や厳密解でない数値参照の厳密性は主張しません。

調査時の根拠：

- `code/validated-examples/2026-11-22/particle-transport/cases.json` · dsmc-statistics.limits
- `catalog/atlas-detailed-reading.json` · dsmc.verification

- [SPARTA公式: Validation and Verification](<https://sparta.github.io/pdf/sparta_2015_validation_verification.pdf>)
  Sandia開発者の公式講習資料。Fourier/Couette流による熱流束・せん断応力検証の説明を確認。

完了の根拠：

```json
{
  "verification": "/numerical-methods-atlas/validation/verification/2026-11-24-batch28-37-public.json",
  "inputs": [
    "/code/validated-examples/2026-11-23/dsmc-wall/inputs.json",
    "/code/validated-examples/2026-11-23/dsmc-wall/acceptance.json",
    "/code/validated-examples/2026-11-23/dsmc-wall/pre-run-contract.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-23/dsmc-wall/results/dsmc-couette-preview.png",
    "/code/validated-examples/2026-11-23/dsmc-wall/results/dsmc-fourier-preview.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-23/dsmc-wall/run.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-23/dsmc-wall/README.md",
    "/code/validated-examples/2026-11-23/dsmc-wall/verification.json",
    "/numerical-methods-atlas/validation/verification/2026-11-24-batch28-37-public.json"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#dsmc-couette-ja",
  "execution": "/numerical-methods-atlas/validation/dsmc-couette/?lang=ja"
}
```

### 平面定常衝撃波の構造（hard-sphere/VHS）

ID: dsmc-2 · P2 · 公開済み · 新規実装

調査時の範囲：未収録

調査時の現状：

固定範囲をHRで公開。最終SHAの全38群83ケース1047pytest、サイト543件が合格。初期公開の画面確認と新版HTTP差分確認、Linux失敗2件、DSMC性能修正版を区別して保持。Thomas1949原報は未読の文献整理で数値例なし。

追加内容・最小の検証：

- 現collision roundsを物理時間と読み替えず、速度依存衝突・streaming・流入出を実装してから検証
- 密度/温度/応力のプロファイルと外部参照を固定し、Maxwell緩和とは別ケースにする

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

各例の前提・参照の独立範囲と未達版の履歴を、入力・受入基準・契約・検証記録で区別します。一般条件への認証や厳密解でない数値参照の厳密性は主張しません。

調査時の根拠：

- `catalog/atlas-methods.json` · dsmc.limitations
- `code/validated-examples/2026-11-22/particles/cases.json` · dsmc.assumptions

- [SPARTA公式: Validation and Verification](<https://sparta.github.io/pdf/sparta_2015_validation_verification.pdf>)
  Sandia開発者の公式講習資料。Fourier/Couette流による熱流束・せん断応力検証の説明を確認。

完了の根拠：

```json
{
  "verification": "/numerical-methods-atlas/validation/verification/2026-11-24-batch28-37-public.json",
  "inputs": [
    "/code/validated-examples/2026-11-24/dsmc-shock/inputs.json",
    "/code/validated-examples/2026-11-24/dsmc-shock/acceptance.json",
    "/code/validated-examples/2026-11-24/dsmc-shock/pre-run-contract.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-24/dsmc-shock/results/dsmc-planar-shock-preview.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-24/dsmc-shock/run.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-24/dsmc-shock/README.md",
    "/code/validated-examples/2026-11-23/dsmc-shock/README.md",
    "/code/validated-examples/2026-11-23/dsmc-shock/verification.json",
    "/code/validated-examples/2026-11-24/dsmc-shock/verification.json",
    "/numerical-methods-atlas/validation/verification/2026-11-24-batch28-37-public.json"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#dsmc-planar-shock-ja",
  "execution": "/numerical-methods-atlas/validation/dsmc-planar-shock/?lang=ja"
}
```

## LBM・格子Boltzmann

### Ghia lid-driven cavity（まずRe=100）

ID: lbm-1 · P1 · 公開済み · 新規実装

調査時の範囲：未収録

調査時の現状：

Re100の実2D LBMを3格子で計算し、Ghiaの丸めた中心線表・主渦・定常性・壁運動量収支を照合。角と有限Machの制約を残します。

追加内容・最小の検証：

- 移動壁条件・中心線速度・主渦位置と格子細分化を追加
- 壁端の特異性やMach数圧縮性誤差を記録し、既存静止壁Poiseuilleと区別

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

固定入力・参照・受入条件・失敗履歴を保持し、独立に展開したZIPの全固定入力を再実行しました。HR上の実配信と公開ZIP Linux追試は、このローカル検証と別の記録で確認します。

調査時の根拠：

- `code/numerical-methods-atlas/2026-11-21/numart/lattice_boltzmann.py` · step(walls=True)は静止壁
- `code/numerical-methods-atlas/2026-11-21/tests/test_new_models.py` · 既存3件のLBMテスト

- [Ghia, Ghia & Shin (1982), High-Re solutions for incompressible flow ...](<https://www.sciencedirect.com/science/article/abs/pii/0021999182900584>)
  原著出版社の書誌と抄録を確認。cavityベンチマークの原著であり、LBM原著ではない。
- [On pressure and velocity flow boundary conditions and bounceback for the lattice Boltzmann BGK model](<https://arxiv.org/abs/comp-gas/9611001>)
  Selected original preprint pp2-7: standard equilibrium, moment-based flat velocity/density boundaries and corner/finite-Mach limitations. No full-paper audit; special d2q9i accuracy is not credited to this standard BGK.
- [Lattice Boltzmann method for moving boundaries](<https://doi.org/10.1016/S0021-9991(02)00022-0>)
  Original article sec3 printed410-414 via author-content mirror; quadratic interpolation paths, q=.5, wall correction, momentum exchange and compromised mass conservation. Our two-point linear implementation is separately derived and qualified; original2001BFL full text was inaccessible.
- [High-Re solutions for incompressible flow using the Navier-Stokes equations and a multigrid method](<https://www.sciencedirect.com/science/article/pii/0021999182900584>)
  Exact-byte existing17-point Re100columns and prior original-PDF/rendered-page provenance rechecked. Current session did not reacquire the original PDF. Printed398-399TablesI/II and408TableV provenance retained.

完了の根拠：

```json
{
  "verification": "/code/validated-examples/2026-11-24/lbm-cavity/verification.json",
  "inputs": [
    "/code/validated-examples/2026-11-24/lbm-cavity/inputs.json",
    "/code/validated-examples/2026-11-24/lbm-cavity/acceptance.json",
    "/code/validated-examples/2026-11-24/lbm-cavity/pre-run-contract.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-24/lbm-cavity/results/lbm-cavity-re100-preview.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-24/lbm-cavity/run.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-24/lbm-cavity/README.md",
    "/code/validated-examples/2026-11-24/lbm-cavity/verification.json"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#lid-driven-cavity-ja",
  "execution": "/numerical-methods-atlas/validation/lbm-cavity-re100/?lang=ja"
}
```

### LBM版2D Taylor–Green渦の時間・空間・Mach数誤差

ID: lbm-2 · P1 · 公開済み · 検証の拡充

調査時の範囲：検証範囲不足

調査時の現状：

解析Taylor–Green渦で速度・圧力・エネルギーを比較。格子・時間刻み・Mach数の結び付いた細分化と振幅・刻みの比較で、純粋な時間次数やMach次数とは区別します。

追加内容・最小の検証：

- せん断単一モードに加え、非線形移流と粘性を含む低Mach渦で速度/圧力誤差を分離
- 別系統の既存Taylor–Green投影法をLBMの検証とみなさない

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

固定入力・参照・受入条件・失敗履歴を保持し、独立に展開したZIPの全固定入力を再実行しました。HR上の実配信と公開ZIP Linux追試は、このローカル検証と別の記録で確認します。

調査時の根拠：

- `code/numerical-methods-atlas/2026-11-21/numart/lattice_boltzmann.py` · shear_wave
- `catalog/atlas-execution-examples.json` · taylor-greenはprojection法

- [On pressure and velocity flow boundary conditions and bounceback for the lattice Boltzmann BGK model](<https://arxiv.org/abs/comp-gas/9611001>)
  Selected original preprint pp2-7: standard equilibrium, moment-based flat velocity/density boundaries and corner/finite-Mach limitations. No full-paper audit; special d2q9i accuracy is not credited to this standard BGK.
- [Lattice Boltzmann method for moving boundaries](<https://doi.org/10.1016/S0021-9991(02)00022-0>)
  Original article sec3 printed410-414 via author-content mirror; quadratic interpolation paths, q=.5, wall correction, momentum exchange and compromised mass conservation. Our two-point linear implementation is separately derived and qualified; original2001BFL full text was inaccessible.

完了の根拠：

```json
{
  "verification": "/code/validated-examples/2026-11-24/lbm-taylor-green/verification.json",
  "inputs": [
    "/code/validated-examples/2026-11-24/lbm-taylor-green/inputs.json",
    "/code/validated-examples/2026-11-24/lbm-taylor-green/acceptance.json",
    "/code/validated-examples/2026-11-24/lbm-taylor-green/pre-run-contract.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-24/lbm-taylor-green/results/lbm-taylor-green-preview.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-24/lbm-taylor-green/run.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-24/lbm-taylor-green/README.md",
    "/code/validated-examples/2026-11-24/lbm-taylor-green/verification.json"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#taylor-green-ja",
  "execution": "/numerical-methods-atlas/validation/lbm-taylor-green/?lang=ja"
}
```

### 円柱後流／曲面境界のSchäfer–Turek型基準問題

ID: lbm-3 · P2 · 公開済み · 新規実装

調査時の範囲：未収録

調査時の現状：

二次曲面補間の環状Couette制御と、実際のRe20円柱流を別配布。点ごとの圧力・トルク、抗力・圧力差・後流を比較し、旧未達・流出不安定化の結果も保持。原著の推定区間を厳密解とはしません。

追加内容・最小の検証：

- まず定常低Reで抗力・圧力差を比較し、曲面壁の配置誤差を検査
- 既存half-way平板壁のみの検査から任意曲面精度を主張しない

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

固定入力・参照・受入条件・失敗履歴を保持し、独立に展開したZIPの全固定入力を再実行しました。HR上の実配信と公開ZIP Linux追試は、このローカル検証と別の記録で確認します。

調査時の根拠：

- `code/numerical-methods-atlas/2026-11-21/numart/lattice_boltzmann.py` · step,poiseuille

- [On pressure and velocity flow boundary conditions and bounceback for the lattice Boltzmann BGK model](<https://arxiv.org/abs/comp-gas/9611001>)
  Selected original preprint pp2-7: standard equilibrium, moment-based flat velocity/density boundaries and corner/finite-Mach limitations. No full-paper audit; special d2q9i accuracy is not credited to this standard BGK.
- [Lattice Boltzmann method for moving boundaries](<https://doi.org/10.1016/S0021-9991(02)00022-0>)
  Selected original sec3 printed410-414 via disclosed author-content mirror: Eq12/13/14 quadratic reflected-characteristic interpolation,moving-wall coefficient,Eq15 momentum exchange and compromised mass conservation. Generic Lagrange scalar oracle independently qualifies weights andsigns. No localPDF/rendered-symbol audit;2001BFLfulloriginal remains unread.
- [Benchmark Computations of Laminar Flow Around a Cylinder](<https://kent-and.github.io/mek4250/2021/SchaeferTurek1996.pdf>)
  Original chapter delivered by course mirror after official links404: printed3-4geometry/2D-1/force definitions,7protocol user-selected outlet,11-12Table3 estimated ranges. Not a full-paper or separate local rendered-symbol audit.
- [DFG flow around cylinder benchmark2D-1, Re20](<https://wwwold.mathematik.tu-dortmund.de/~featflow/en/benchmarks/cfdbenchmarking/flow/dfg_benchmark1_re20.html>)
  Actual geometry,do-nothingBC,mean-speed normalization,force/probe definitions and Nabh1998attribution read. Nabh original report not read; its precise values are contextual,not the adopted outlet truth.
- [Non-equilibrium extrapolation method for velocity and pressure boundary conditions in the lattice Boltzmann method](<https://cpb.iphy.ac.cn/en/article/doi/10.1088/1009-1963/11/4/310>)
  Official primary abstract actually read: equilibrium/nonequilibrium split and adjacent-fluid extrapolation. Full primary equations unavailable; the adopted all-nine poststream density reservoir is independently derived and qualified,not labelled the exact author implementation.

完了の根拠：

```json
{
  "verification": "/code/validated-examples/2026-11-24/lbm-annulus/verification.json",
  "inputs": [
    "/code/validated-examples/2026-11-24/lbm-annulus/inputs.json",
    "/code/validated-examples/2026-11-24/lbm-annulus/acceptance.json",
    "/code/validated-examples/2026-11-24/lbm-annulus/pre-run-contract.json",
    "/code/validated-examples/2026-11-24/lbm-curved-boundary/inputs.json",
    "/code/validated-examples/2026-11-24/lbm-curved-boundary/acceptance.json",
    "/code/validated-examples/2026-11-24/lbm-curved-boundary/pre-run-contract.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-24/lbm-annulus/results/lbm-annular-couette-control-preview.png",
    "/code/validated-examples/2026-11-24/lbm-curved-boundary/results/lbm-cylinder-re20-preview.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-24/lbm-annulus/run.py",
    "/code/validated-examples/2026-11-24/lbm-curved-boundary/run.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-24/lbm-annulus/README.md",
    "/code/validated-examples/2026-11-24/lbm-annulus/verification.json",
    "/code/validated-examples/2026-11-24/lbm-curved-boundary/README.md",
    "/code/validated-examples/2026-11-24/lbm-curved-boundary/verification.json"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#lbm-annular-couette-control-ja",
  "execution": "/numerical-methods-atlas/validation/lbm-annular-couette-control/?lang=ja"
}
```

## 放射輸送

### 等方散乱平板の多重散乱ベンチマーク

ID: radiation-1 · P1 · 公開済み · 検証の拡充

調査時の範囲：検証範囲不足

調査時の現状：

光学的厚さと散乱アルベドを固定した定常平板。角度離散法を、連続角度のFredholm積分方程式・異なるスカラー基底の参照と比較。有限な参照差を厳密誤差上界とはしません。

追加内容・最小の検証：

- 単一散乱アルベドと光学的厚さを変え、透過・反射・吸収収支を独立輸送解と比較
- 純吸収E3の合格を散乱やDISORT全機能の検証へ広げない

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

固定入力・参照・受入条件・失敗履歴を保持し、独立に展開したZIPの全固定入力を再実行しました。HR上の実配信と公開ZIP Linux追試は、このローカル検証と別の記録で確認します。

調査時の根拠：

- `code/validated-examples/2026-11-22/particles/cases.json` · radiation-transport.limits

- [Su & Olson (1997), An analytical benchmark for non-equilibrium radiative transfer ...](<https://www.sciencedirect.com/science/article/abs/pii/S0306454996001004>)
  原著出版社抄録で等方散乱・非平衡輸送の解析ベンチマークを確認。1996拡散問題と1997輸送問題を区別する。
- [Pharr,Jakob and Humphreys, Physically Based Rendering4e: The Equation of Transfer](<https://www.pbr-book.org/4ed/Light_Transport_II_Volume_Rendering/The_Equation_of_Transfer>)
  Read selected transfer/source/finite-ray boundary section. The isotropic Fredholm normalization,independent exact-cell E1weights and flux derivations are documented in this packet; no DISORT reproduction or Monte Carlo claim.

完了の根拠：

```json
{
  "verification": "/code/validated-examples/2026-11-24/radiation-scattering/verification.json",
  "inputs": [
    "/code/validated-examples/2026-11-24/radiation-scattering/inputs.json",
    "/code/validated-examples/2026-11-24/radiation-scattering/acceptance.json",
    "/code/validated-examples/2026-11-24/radiation-scattering/pre-run-contract.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-24/radiation-scattering/results/isotropic-scattering-slab-preview.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-24/radiation-scattering/run.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-24/radiation-scattering/README.md",
    "/code/validated-examples/2026-11-24/radiation-scattering/verification.json"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#isotropic-scattering-slab-ja",
  "execution": "/numerical-methods-atlas/validation/isotropic-scattering-slab/?lang=ja"
}
```

### Su–Olson非平衡放射輸送／Marshak波

ID: radiation-2 · P2 · 公開済み · 新規実装

調査時の範囲：未収録

調査時の現状：

1996拡散と1997輸送の規格化・境界・参照を分離。固定ExactPack版と著者提供の2023輸送表を照合し、物質交換・重み付き収支を確認。追加の同条件Fourierモードで平均自由行程を解像した拡散極限を調べ、固定格子AP・SSPRK2の硬い極限とは区別。1996/1997原著全文は未読です。

追加内容・最小の検証：

- Su–Olsonの1997輸送解と拡散近似版を区別し、時間依存・物質エネルギー交換を検証
- 熱平衡接近、全エネルギー収支、光学的厚い極限を別指標にする

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

固定入力・参照・受入条件・失敗履歴を保持し、独立に展開したZIPの全固定入力を再実行しました。HR上の実配信と公開ZIP Linux追試は、このローカル検証と別の記録で確認します。

調査時の根拠：

- `catalog/atlas-depth.json` · transport.next
- `catalog/atlas-methods.json` · radiation-transport.limitations

- [Su & Olson (1997), An analytical benchmark for non-equilibrium radiative transfer ...](<https://www.sciencedirect.com/science/article/abs/pii/S0306454996001004>)
  原著出版社抄録で等方散乱・非平衡輸送の解析ベンチマークを確認。1996拡散問題と1997輸送問題を区別する。
- [B. Su and G. L. Olson (1996), Benchmark results for the non-equilibrium Marshak diffusion problem, JQSRT56(3),337–351](<https://doi.org/10.1016/0022-4073(96)84524-9>)
  Publisher abstract and bibliographic metadata read; original full text/equations/tables unavailable and not directly checked. Diffusion is distinct from the1997transport problem.
- [J. Thrussell and J. M. Ferguson (2023), ExactPack: A python library of exact analytic solutions, SoftwareX24,101560](<https://doi.org/10.1016/j.softx.2023.101560>)
  Bibliographic software credit,recorded separately from Su–Olson1996 and the pinned executed source. Full software paper is not claimed read.
- [LANL ExactPack1.7.5, pinned SuOlson/Timmes evaluator](<https://github.com/lanl/ExactPack/tree/8718b61f281a9744ea7a3820c51800915e4636e9/exactpack/solvers/suolson>)
  All55documentation,41wrapper and348Timmes module lines read. Execute nondimensional usolution/vsolution serially; qualify selected original/tight integrals against sensitivity,PDE and Robin checks. No primary solver shares this evaluator. Full ExactPack/base/library audit is not claimed.
- [LANL ExactPack pinned BSD-3-Clause license](<https://github.com/lanl/ExactPack/blob/8718b61f281a9744ea7a3820c51800915e4636e9/LICENSE.txt>)
  Actual license text read and retained as exactpack-LICENSE.txt with redistributed inert source snapshots.
- [B. Su and G. L. Olson (1997), An analytical benchmark for non-equilibrium radiative transfer in an isotropically scattering medium, Annals of Nuclear Energy24(13),1035–1055](<https://doi.org/10.1016/S0306-4549(96)00100-4>)
  Publisher abstract/metadata read only. Original full text,integral normalization and original numerical tables were not directly read or transcribed. The actual comparison is independently attributed to the selected2023author repository below.
- [A. Crilly (2023), Learning closure relations using differentiable programming: an example in radiation transport](<https://raw.githubusercontent.com/ml4physicalsciences/ml4physicalsciences.github.io/master/2023/files/NeurIPS_ML4PS_2023_16.pdf>)
  Actually read and visually verified PDFpage6 Appendix4.1 equations7–10: epsilon*d_tau U+mu*d_x U+U=V/2+Q/2,V_tau=W−V. With I=2U, E=W. epsilon1,x0=.5,source duration10; no direct original1997-table verification.
- [A. Crilly RTClosureJAX pinned SuOlsonData analytical benchmark tables](<https://github.com/aidancrilly/RTClosureJAX/tree/3e4f636299d62bc03f7118cfc884230c756f9d87/SuOlsonData>)
  Pinned W/Vtransport data,coordinates,times and README actually read. Repository calls them analytical Su–Olson data; transcription versus regeneration is undocumented. They are not trained-closure/model predictions. Retain full15×7raw table; compare13points at tau.1,1,3.16228 with matching source/epsilon/units. Rounded five-decimal finite data,not a rigorous exact reference.
- [RTClosureJAX pinned MIT license](<https://github.com/aidancrilly/RTClosureJAX/blob/3e4f636299d62bc03f7118cfc884230c756f9d87/LICENSE>)
  Actual MIT license read and retained with the bundled raw table. No redistribution of the2023paper PDF is required by this packet.
- [SciPy1.14.1 expm_multiply: matrix exponential action and trace preconditioning](<https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.sparse.linalg.expm_multiply.html>)
  Actually inspected installed1.14.1 source/API docstring and the versioned official API action/traceA section. Shared by the new FV-mode and continuum-reference propagators; mathematical action equivalence is not bit equivalence or independent-engine evidence. The linked algorithm papers were not read as part of this update.
- [SciPy1.14.1 solve_ivp: DOP853 and complex initial states](<https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.integrate.solve_ivp.html>)
  Read selected official API sections for complex initial states,DOP853 and fixed tolerances. Two separately written continuum derivatives are compared to the shared exponential action under frozen141checks. This is finite reference qualification,not a primary SSPRK2 order test or a rigorous bound; original DOP853 papers were not reviewed here.

完了の根拠：

```json
{
  "verification": "/code/validated-examples/2026-11-24-r2/radiation-matter/verification.json",
  "inputs": [
    "/code/validated-examples/2026-11-24-r2/radiation-matter/inputs.json",
    "/code/validated-examples/2026-11-24-r2/radiation-matter/acceptance.json",
    "/code/validated-examples/2026-11-24-r2/radiation-matter/pre-run-contract.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-24-r2/radiation-matter/results/su-olson-diffusion1996-preview.png",
    "/code/validated-examples/2026-11-24-r2/radiation-matter/results/su-olson-transport1997-preview.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-24-r2/radiation-matter/run.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-24-r2/radiation-matter/README.md",
    "/code/validated-examples/2026-11-24-r2/radiation-matter/verification.json"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#su-olson-diffusion1996-ja",
  "execution": "/numerical-methods-atlas/validation/su-olson-diffusion1996/?lang=ja"
}
```

### 影形成・交差ビームの多次元輸送（M1の限界も表示）

ID: radiation-3 · P2 · 公開済み · 新規実装

調査時の範囲：未収録

調査時の現状：

実2D空間の角度輸送と非線形静止M1で影・対向ビームを比較。x/y交差制御とM1製造解、方向別流束の円錐分割を別に検査。角度輸送の厳密参照をM1全体の厳密解とはしません。

追加内容・最小の検証：

- 純吸収平板以外の角度構造を持つ2D固定入力を設ける
- 離散角解とmoment closureを混同せず、影の漏れ・交差後の角度情報を比較

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

固定入力・参照・受入条件・失敗履歴を保持し、独立に展開したZIPの全固定入力を再実行しました。HR上の実配信と公開ZIP Linux追試は、このローカル検証と別の記録で確認します。

調査時の根拠：

- `catalog/atlas-methods.json` · radiation-transport
- `catalog/atlas-depth.json` · transport.next

- [J. Rosdahl etal. (2013), RAMSES-RT: Radiation hydrodynamics in the cosmological context](<https://arxiv.org/html/1304.7126v2>)
  Read selectedSection2 equations12–14 and opposing-beam limitation text. The static grey equations here are neither GR nor reproductions of RAMSES astrophysical calculations. Original Levermore1984 full text was not read.
- [A Two-moment Radiation Hydrodynamics Module in Athena Using a Time-Explicit Godunov Method](<https://arxiv.org/pdf/1306.0010>)
  Independent reviewer actually read selected extracted Section3.3equations37–41and eigenvalue limits;not a whole-paper/rendered-symbol audit. Directional LF cone root/weighted-CFL algebra is separately authored and independently crosschecked,not a transplanted HLL solver or claimed general Riemann-fan bound. Actual generalized directional LF core passed762component checks,then all166fixed geometry gates. The authored LFcone proof is separate from the paper;no general nonlinearRiemannfan bound is claimed.

完了の根拠：

```json
{
  "verification": "/code/validated-examples/2026-11-24/radiation-geometry/verification.json",
  "inputs": [
    "/code/validated-examples/2026-11-24/radiation-geometry/inputs.json",
    "/code/validated-examples/2026-11-24/radiation-geometry/acceptance.json",
    "/code/validated-examples/2026-11-24/radiation-geometry/pre-run-contract.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-24/radiation-geometry/results/shadow-absorber2d-preview.png",
    "/code/validated-examples/2026-11-24/radiation-geometry/results/opposing-beams2d-preview.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-24/radiation-geometry/run.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-24/radiation-geometry/README.md",
    "/code/validated-examples/2026-11-24/radiation-geometry/verification.json"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#shadow-absorber2d-ja",
  "execution": "/numerical-methods-atlas/validation/shadow-absorber2d/?lang=ja"
}
```

## 確率MC・MCMC・SDE

### GBM/OUのweak誤差と信頼区間を分けた固定入力

ID: stochastic-1 · P1 · 公開済み · 検証の拡充

調査時の範囲：検証範囲不足

調査時の現状：

GBMとスカラーOUで解析モーメント・離散弱誤差・共有Brown運動・独立seed・MCSEを比較。既存GBM強収束や調和Langevin全体の検証とは区別します。

追加内容・最小の検証：

- GBM strong収束の既存経路比較とは別に、期待値・分散等のweak収束を反復seedで測る
- OU/Langevinの別章既存例を未実装扱いせず、一般SDE章のweak次数の主張を独立に検査

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

固定入力・参照・受入条件・失敗履歴を保持し、独立に展開したZIPの全固定入力を再実行しました。HR上の実配信と公開ZIP Linux追試は、このローカル検証と別の記録で確認します。

調査時の根拠：

- `catalog/atlas-methods.json` · sde.limitations
- `catalog/atlas-detailed-reading.json` · sde.verification

- [Higham (2001), An Algorithmic Introduction to Numerical Simulation of SDEs](<https://epubs.siam.org/doi/10.1137/S0036144500378302>)
  SIAMの原論文ページでEM・Milstein・strong/weak convergenceの扱いを確認。

完了の根拠：

```json
{
  "verification": "/code/validated-examples/2026-11-24/stochastic-accuracy/verification.json",
  "inputs": [
    "/code/validated-examples/2026-11-24/stochastic-accuracy/inputs.json",
    "/code/validated-examples/2026-11-24/stochastic-accuracy/acceptance.json",
    "/code/validated-examples/2026-11-24/stochastic-accuracy/pre-run-contract.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-24/stochastic-accuracy/results/gbm-weak-moments-preview.png",
    "/code/validated-examples/2026-11-24/stochastic-accuracy/results/ou-weak-moments-preview.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-24/stochastic-accuracy/run.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-24/stochastic-accuracy/README.md",
    "/code/validated-examples/2026-11-24/stochastic-accuracy/verification.json"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#gbm-sde-ja",
  "execution": "/numerical-methods-atlas/validation/gbm-weak-moments/?lang=ja"
}
```

### 正規尾確率などのimportance sampling／分散削減

ID: stochastic-2 · P1 · 公開済み · 新規実装

調査時の範囲：未収録

調査時の現状：

正規尾確率a=3,6で通常の重要度重み・既知分散・64独立seedの有限な区間被覆を比較。直接MCのゼロヒットをゼロ確率や幅ゼロ区間とはしません。一般の95%被覆保証ではありません。

追加内容・最小の検証：

- 既知erfc参照を持つ稀な事象で、推定量の不偏性と重み・実測分散・区間被覆を確認
- 単なる一様x²積分やMCMC診断と区別

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

固定入力・参照・受入条件・失敗履歴を保持し、独立に展開したZIPの全固定入力を再実行しました。HR上の実配信と公開ZIP Linux追試は、このローカル検証と別の記録で確認します。

調査時の根拠：

- `catalog/atlas-execution-examples.json` · mc-integral.scope
- `catalog/atlas-detailed-reading.json` · monte-carlo.verificationは提案、全て実行済みではない

- [Monte Carlo theory,methods and examples,Chapter9: importance sampling](<https://artowen.su.domains/mc/Ch-var-is.pdf>)
  Selected author-chapter support,ordinary estimator,second moments and diagnostics were read during preparation. Current refetch returned403. No full-book or PERT experiment reproduction.

完了の根拠：

```json
{
  "verification": "/code/validated-examples/2026-11-24/stochastic-estimation/verification.json",
  "inputs": [
    "/code/validated-examples/2026-11-24/stochastic-estimation/inputs.json",
    "/code/validated-examples/2026-11-24/stochastic-estimation/acceptance.json",
    "/code/validated-examples/2026-11-24/stochastic-estimation/pre-run-contract.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-24/stochastic-estimation/results/normal-tail-importance-preview.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-24/stochastic-estimation/run.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-24/stochastic-estimation/README.md",
    "/code/validated-examples/2026-11-24/stochastic-estimation/verification.json"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#normal-tail-importance-ja",
  "execution": "/numerical-methods-atlas/validation/normal-tail-importance/?lang=ja"
}
```

### 相関多変量Gaussian／banana・funnel型標的

ID: stochastic-3 · P2 · 公開済み · 検証の拡充

調査時の範囲：検証範囲不足

調査時の現状：

相関0.95の2D Gaussianを等方・前処理付き提案で比較。解析の同時モーメントと量別MCSE、保存同一データのArviZ診断640照合を分離。有限演算の分位点互換を明記し、banana・funnel・HMC/NUTSや一般の収束保証は未実装です。

追加内容・最小の検証：

- 既存1D対称二峰とは異なる相関・次元・局所スケールで診断の限界を示す
- 標的の既知モーメント/変数変換・量別MCSEを確認。HMC/NUTSの導入そのものを必須にはしない

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

固定入力・参照・受入条件・失敗履歴を保持し、独立に展開したZIPの全固定入力を再実行しました。HR上の実配信と公開ZIP Linux追試は、このローカル検証と別の記録で確認します。

調査時の根拠：

- `catalog/atlas-depth.json` · probability.next
- `code/validated-examples/2026-11-22/mcmc/cases.json` · mcmc-multimodal-mixing.limits

- [Hoffman & Gelman (2014), The No-U-Turn Sampler](<https://www.jmlr.org/papers/v15/hoffman14a.html>)
  JMLR原著ページで高次元・相関のある標的に対する比較の動機を確認。NUTS実装を今回必須とするものではない。
- [Rank-normalization,folding,and localization: An improved R-hat for assessing convergence of MCMC](<https://arxiv.org/pdf/1903.08008>)
  Read selected original rank/foldedRhat,ESS and corrected Blom equation. No multivariate global-convergence certificate.
- [ArviZ0.20.0 public diagnostics API and selected implementation](<https://python.arviz.org/en/v0.20.0/api/generated/arviz.mcse.html>)
  Read official0.20.0 ESS/MCSE source and API. Cache640values from128same-data observable/prefix arrays of8fixed chainsets in a separate process. Independence is the diagnostic engine,not an independent sampler.

完了の根拠：

```json
{
  "verification": "/code/validated-examples/2026-11-24/stochastic-estimation/verification.json",
  "inputs": [
    "/code/validated-examples/2026-11-24/stochastic-estimation/inputs.json",
    "/code/validated-examples/2026-11-24/stochastic-estimation/acceptance.json",
    "/code/validated-examples/2026-11-24/stochastic-estimation/pre-run-contract.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-24/stochastic-estimation/results/correlated-gaussian-mcmc-preview.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-24/stochastic-estimation/run.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-24/stochastic-estimation/README.md",
    "/code/validated-examples/2026-11-24/stochastic-estimation/verification.json"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#correlated-gaussian-mcmc-ja",
  "execution": "/numerical-methods-atlas/validation/correlated-gaussian-mcmc/?lang=ja"
}
```

### Milstein法のGBM strong次数比較

ID: stochastic-4 · P2 · 公開済み · 新規実装

調査時の範囲：未収録

調査時の現状：

同じBrown運動でEMとMilsteinのGBM強誤差を比較し、解析RMSと有限標本区間を照合。非Lipschitz系や一般の正値性へは広げません。

追加内容・最小の検証：

- 既存EMと同じBrown経路でstrong 1/2と1を比較
- 正値性や非Lipschitz系へ一般化せず、まず解析解を持つ小例に限定

完了条件：

- 固定入力と適用範囲、参照解または独立参照とその出典を保存する。
- 実コード・検査とpassed=trueの検証記録を揃える。
- 誤差・収束と制約が分かる図を保存する。
- 実在する問題ギャラリー・実行入口・入力・図への対応を確認する。

固定入力・参照・受入条件・失敗履歴を保持し、独立に展開したZIPの全固定入力を再実行しました。HR上の実配信と公開ZIP Linux追試は、このローカル検証と別の記録で確認します。

調査時の根拠：

- `catalog/atlas-methods.json` · sde.example_scope
- `catalog/atlas-execution-examples.json` · gbm-sde

- [Higham (2001), An Algorithmic Introduction to Numerical Simulation of SDEs](<https://epubs.siam.org/doi/10.1137/S0036144500378302>)
  SIAMの原論文ページでEM・Milstein・strong/weak convergenceの扱いを確認。

完了の根拠：

```json
{
  "verification": "/code/validated-examples/2026-11-24/stochastic-accuracy/verification.json",
  "inputs": [
    "/code/validated-examples/2026-11-24/stochastic-accuracy/inputs.json",
    "/code/validated-examples/2026-11-24/stochastic-accuracy/acceptance.json",
    "/code/validated-examples/2026-11-24/stochastic-accuracy/pre-run-contract.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-24/stochastic-accuracy/results/gbm-milstein-strong-preview.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-24/stochastic-accuracy/run.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-24/stochastic-accuracy/README.md",
    "/code/validated-examples/2026-11-24/stochastic-accuracy/verification.json"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#gbm-sde-ja",
  "execution": "/numerical-methods-atlas/validation/gbm-milstein-strong/?lang=ja"
}
```

## Maxwell・FDTD

### Mie散乱（まず2D円柱、用途があれば3D球）

ID: maxwell-fdtd-1 · P2 · 公開済み · 新規実装

調査時の範囲：未収録

調査時の現状：

固定入力のコード・保存図をHRで公開。匿名公開ファイル照合、実HR日英画面、全52群106例1352pytestの公開ZIP Linux/JUnit検査が合格。条件と履歴は各配布記録を参照。

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
- [Mie scattering 2D](<https://optics.ansys.com/hc/en-us/articles/360042703373-Mie-scattering-2D>)
  Read the complete substantive benchmark description: two-dimensional dielectric cylinder, TFSF, angular far field and lossless cross sections. Did not read the associated simulation files, theory table or cited book; no external numerical data imported. Publication and revision dates have not been verified. Accessed on 2026-11-24; this is a consultation date, not a publication year.
- [Bessel and Hankel Wronskians, section10.5](<https://dlmf.nist.gov/10.5>)
  Read section 10.5, especially equation 10.5.3 for the ordinary J/Hankel1 Wronskian; version 1.2.8. Cylinder boundary algebra is independently derived here. The year 2026 denotes DLMF version 1.2.8, released on 2026-09-15, not its initial publication year. Accessed on 2026-11-24.

完了の根拠：

```json
{
  "verification": "/code/validated-examples/2026-11-24-r2/maxwell-cylinder/verification.json",
  "inputs": [
    "/code/validated-examples/2026-11-24-r2/maxwell-cylinder/inputs.json",
    "/code/validated-examples/2026-11-24-r2/maxwell-cylinder/acceptance.json",
    "/code/validated-examples/2026-11-24-r2/maxwell-cylinder/pre-run-contract.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-24-r2/maxwell-cylinder/results/cylinder-mie2d-preview.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-24-r2/maxwell-cylinder/run.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-24-r2/maxwell-cylinder/README.md",
    "/code/validated-examples/2026-11-24-r2/maxwell-cylinder/cases.json",
    "/numerical-methods-atlas/validation/verification/2026-11-24-batch48-57-public.json"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#cylinder-mie2d-ja",
  "execution": "/numerical-methods-atlas/validation/cylinder-mie2d/?lang=ja"
}
```

### 損失・Lorentz分散板への斜め入射Fresnel

ID: maxwell-fdtd-2 · P2 · 公開済み · 検証の拡充

調査時の範囲：検証範囲不足

調査時の現状：

固定入力のコード・保存図をHRで公開。匿名公開ファイル照合、実HR日英画面、全52群106例1352pytestの公開ZIP Linux/JUnit検査が合格。条件と履歴は各配布記録を参照。

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
  Read Material Dispersion, Numerical Stability, Loss and Gain, and Conductivity. Confirmed the exp(-i omega t) convention, Lorentz polarization and dispersive-PML warning. Our sigma E conductivity and midpoint update differ from Meep. Unversioned latest documentation; no original Yee or Roden-Gedney paper claim. Publication and revision dates have not been verified. Accessed on 2026-11-24; this is a consultation date, not a publication year.

完了の根拠：

```json
{
  "verification": "/code/validated-examples/2026-11-24-r2/maxwell-lorentz/verification.json",
  "inputs": [
    "/code/validated-examples/2026-11-24-r2/maxwell-lorentz/inputs.json",
    "/code/validated-examples/2026-11-24-r2/maxwell-lorentz/acceptance.json",
    "/code/validated-examples/2026-11-24-r2/maxwell-lorentz/pre-run-contract.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-24-r2/maxwell-lorentz/results/lorentz-oblique-sp-preview.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-24-r2/maxwell-lorentz/run.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-24-r2/maxwell-lorentz/README.md",
    "/code/validated-examples/2026-11-24-r2/maxwell-lorentz/cases.json",
    "/numerical-methods-atlas/validation/verification/2026-11-24-batch48-57-public.json"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#lorentz-oblique-sp-ja",
  "execution": "/numerical-methods-atlas/validation/lorentz-oblique-sp/?lang=ja"
}
```

### PMLの浅い入射角・長時間・分散媒質との併用

ID: maxwell-fdtd-3 · P2 · 公開済み · 検証の拡充

調査時の範囲：検証範囲不足

調査時の現状：

固定入力のコード・保存図をHRで公開。匿名公開ファイル照合、実HR日英画面、全52群106例1352pytestの公開ZIP Linux/JUnit検査が合格。条件と履歴は各配布記録を参照。

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
  Read Material Dispersion, Numerical Stability, Loss and Gain, and Conductivity. Confirmed the exp(-i omega t) convention, Lorentz polarization and dispersive-PML warning. Our sigma E conductivity and midpoint update differ from Meep. Unversioned latest documentation; no original Yee or Roden-Gedney paper claim. Publication and revision dates have not been verified. Accessed on 2026-11-24; this is a consultation date, not a publication year.
- [Notes on Perfectly Matched Layers](<https://arxiv.org/html/2108.05348v1>)
  Read sections 3.2–4.2, equations 7–8 and the time-domain ADE discussion, plus sections 5–7.2 on homogeneity, evanescent fields and grazing/discretization limitations. The served text is updated 2026-08-24. The trapezoidal filter is our derivation; no full original Berenger/Roden-Gedney paper review is claimed.

完了の根拠：

```json
{
  "verification": "/code/validated-examples/2026-11-24-r2/maxwell-grazing/verification.json",
  "inputs": [
    "/code/validated-examples/2026-11-24-r2/maxwell-grazing/inputs.json",
    "/code/validated-examples/2026-11-24-r2/maxwell-grazing/acceptance.json",
    "/code/validated-examples/2026-11-24-r2/maxwell-grazing/pre-run-contract.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-24-r2/maxwell-grazing/results/dispersive-grazing-pml-preview.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-24-r2/maxwell-grazing/run.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-24-r2/maxwell-grazing/README.md",
    "/code/validated-examples/2026-11-24-r2/maxwell-grazing/cases.json",
    "/numerical-methods-atlas/validation/verification/2026-11-24-batch48-57-public.json"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#dispersive-grazing-pml-ja",
  "execution": "/numerical-methods-atlas/validation/dispersive-grazing-pml/?lang=ja"
}
```

## 線形代数・連立一次方程式

### 一般直接法の独立教材：部分ピボット LU・Cholesky と反復改良

ID: linear-algebra-1 · P1 · 公開済み · 新規実装

調査時の範囲：未収録

調査時の現状：

固定入力のコード・保存図をHRで公開。匿名公開ファイル照合、実HR日英画面、全52群106例1352pytestの公開ZIP Linux/JUnit検査が合格。条件と履歴は各配布記録を参照。

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

完了の根拠：

```json
{
  "verification": "/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/verification.json",
  "inputs": [
    "/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/inputs.json",
    "/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/acceptance.json",
    "/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/pre-run-contract.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/pivoted-direct-refinement-preview.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/run.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/README.md",
    "/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/cases.json",
    "/numerical-methods-atlas/validation/verification/2026-11-24-batch48-57-public.json"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#pivoted-direct-refinement-ja",
  "execution": "/numerical-methods-atlas/validation/pivoted-direct-refinement/?lang=ja"
}
```

### 鞍点系・対称不定値系：MINRES とブロック前処理

ID: linear-algebra-2 · P2 · 公開済み · 新規実装

調査時の範囲：未収録

調査時の現状：

固定入力のコード・保存図をHRで公開。匿名公開ファイル照合、実HR日英画面、全52群106例1352pytestの公開ZIP Linux/JUnit検査が合格。条件と履歴は各配布記録を参照。

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
- [Paige and Saunders: Stanford SOL MINRES](<https://web.stanford.edu/group/SOL/software/minres/>)
  Selected discussion of symmetric indefinite systems, SPD preconditioners and the original residual was read. The original 1975 paper was not read. This stored-basis Lanczos least-squares variant is not a copy of the production short recurrence.

完了の根拠：

```json
{
  "verification": "/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/verification.json",
  "inputs": [
    "/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/inputs.json",
    "/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/acceptance.json",
    "/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/pre-run-contract.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/symmetric-saddle-minres-preview.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/run.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/README.md",
    "/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/cases.json",
    "/numerical-methods-atlas/validation/verification/2026-11-24-batch48-57-public.json"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#symmetric-saddle-minres-ja",
  "execution": "/numerical-methods-atlas/validation/symmetric-saddle-minres/?lang=ja"
}
```

## 固有値・特異値問題

### 再始動 Krylov と shift-invert による内部固有値

ID: eigenvalues-1 · P1 · 公開済み · 検証の拡充

調査時の範囲：検証範囲不足

調査時の現状：

固定入力のコード・保存図をHRで公開。匿名公開ファイル照合、実HR日英画面、全52群106例1352pytestの公開ZIP Linux/JUnit検査が合格。条件と履歴は各配布記録を参照。

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

完了の根拠：

```json
{
  "verification": "/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/verification.json",
  "inputs": [
    "/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/inputs.json",
    "/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/acceptance.json",
    "/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/pre-run-contract.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/restarted-shift-invert-preview.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/run.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/README.md",
    "/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/cases.json",
    "/numerical-methods-atlas/validation/verification/2026-11-24-batch48-57-public.json"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#restarted-shift-invert-ja",
  "execution": "/numerical-methods-atlas/validation/restarted-shift-invert/?lang=ja"
}
```

### 質量行列付き一般化固有値の独立検証例

ID: eigenvalues-2 · P2 · 公開済み · 検証の拡充

調査時の範囲：検証範囲不足

調査時の現状：

固定入力のコード・保存図をHRで公開。匿名公開ファイル照合、実HR日英画面、全52群106例1352pytestの公開ZIP Linux/JUnit検査が合格。条件と履歴は各配布記録を参照。

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
- [SciPy 1.14.1 LOBPCG API](<https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.sparse.linalg.lobpcg.html>)
  Selected discussion of SPD B, preconditioner M, the history tuple, the 3k eigensolve, the 5k > n fallback and the rod example was read. This maintained-library comparison shares reduced LAPACK primitives; LOBPCG is not independently authored here.
- [SciPy 1.14.1 LOBPCG adapter and initial B-orthonormalization](<https://raw.githubusercontent.com/scipy/scipy/v1.14.1/scipy/sparse/linalg/_eigen/lobpcg/lobpcg.py>)
  Selected _makeMatMat, _b_orthonormalize and API lines were read. The installed pinned file is bound separately. No full reading of the original LOBPCG paper or byte equality between wheel and Web source formatting is claimed.

完了の根拠：

```json
{
  "verification": "/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/verification.json",
  "inputs": [
    "/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/inputs.json",
    "/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/acceptance.json",
    "/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/pre-run-contract.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/fem-mass-eigen-preview.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/run.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/README.md",
    "/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/cases.json",
    "/numerical-methods-atlas/validation/verification/2026-11-24-batch48-57-public.json"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#fem-mass-eigen-ja",
  "execution": "/numerical-methods-atlas/validation/fem-mass-eigen/?lang=ja"
}
```

### Arnoldi/Lanczos 原著の参照箇所を明示

ID: eigenvalues-3 · P3 · 公開済み · 参照・出典の整備

調査時の範囲：出典整備不足

調査時の現状：

選択した原典の読解範囲を公開。Lanczosの原文選択頁とArnoldiの公開OCR本文を区別し、未確認の原本画像・式記号とAMS403を明示。新しい数値例ではありません。

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

完了の根拠：

```json
{
  "targets": [
    "/catalog/atlas-method-primary-references.json",
    "/catalog/atlas-detailed-reading.json"
  ],
  "proof": [
    "/catalog/atlas-method-primary-references.json",
    "/catalog/atlas-detailed-reading.json"
  ],
  "note": "Selected Lanczos original NIST pages266–267/271 were visually checked. Selected Arnoldi original-paper prose was read from a disclosed public OCR copy; the original scan/equation symbols remain unverified and AMS requests returned403. This is source curation, not another numerical implementation.",
  "references": [
    "/numerical-methods-atlas/validation/verification/2026-11-24-batch48-57-public.json"
  ]
}
```

## 非線形方程式・大域化

### Bratu の折り返し点・上下枝をたどる擬似弧長継続

ID: nonlinear-1 · P1 · 公開済み · 新規実装

調査時の範囲：未収録

調査時の現状：

固定入力のコード・保存図をHRで公開。匿名公開ファイル照合、実HR日英画面、全52群106例1352pytestの公開ZIP Linux/JUnit検査が合格。条件と履歴は各配布記録を参照。

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
- [Condition Estimates for Pseudo-Arclength Continuation](<https://ipsen.math.ncsu.edu/ps/sinum65438.pdf>)
  Section2.2, printedpp265–266, Eqs2.2–2.5; tangent null equation, unit Euclidean tangent, augmented system and tangent hyperplane. Weighted h-sum metric is the implementation’s stated discrete variation. No full condition-number proof or original paper numerical benchmark is borrowed.
- [Finite differences for the1D Bratu problem,Problem8](<https://hplgit.github.io/INF5620/doc/pub/._main_nonlin005.html>)
  Problem8/Eq52: boundary-value equation, analytic cosh family, branch count and printed rounded critical value. The author’s parameter equals2 times our theta. Independent Decimal80 exact-family qualification remains the numerical reference; the printed rounded anchor is a separate coarse check.

完了の根拠：

```json
{
  "verification": "/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/verification.json",
  "inputs": [
    "/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/inputs.json",
    "/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/acceptance.json",
    "/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/pre-run-contract.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/results/bratu-fold-continuation-preview.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/run.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/README.md",
    "/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/cases.json",
    "/numerical-methods-atlas/validation/verification/2026-11-24-batch48-57-public.json"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#bratu-fold-continuation-ja",
  "execution": "/numerical-methods-atlas/validation/bratu-fold-continuation/?lang=ja"
}
```

### 真の matrix-free JFNK と inexact Newton forcing

ID: nonlinear-2 · P2 · 公開済み · 新規実装

調査時の範囲：未収録

調査時の現状：

固定入力のコード・保存図をHRで公開。匿名公開ファイル照合、実HR日英画面、全52群106例1352pytestの公開ZIP Linux/JUnit検査が合格。条件と履歴は各配布記録を参照。

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
- [Jacobian-free Newton-Krylov methods: a survey of approaches and applications](<https://inf.ufes.br/~luciac/comcie/JFNK-Knoll.pdf>)
  Selectedsec2.3,2.3.1,2.3.2 and2.4.1, printedpp361–363: matrix-free Jv action, perturbation scaling, inexact forcing Eq16 and line-search globalization. Actual central difference denominator2h and eps_machine^(1/3) scaling are independently specified/qualified, not an attribution to a PETSc default. No whole41-page audit or paper solver result reuse.
- [Choosing the Forcing Terms in an Inexact Newton Method](<https://users.wpi.edu/~walker/Papers/forcing_terms,SISC_17,1996,16-32.pdf>)
  Section1 AlgorithmIN/Eq1.2; selectedsec2 Choice2/Eq2.6; practical-safeguard paragraphssec2.1, printedpp16,20,22–23. Core eta=gamma*(||F_k||/||F_{k-1}||)^alpha is Choice2-style. Our gamma.9/alpha1.5 with eta_initial.3 and fixed[.001,.5] clamp omits the paper’s previous-eta safeguard. This is a declared variant, not its complete safeguarded algorithm or an asymptotic convergence certification.
- [Finite differences for the1D Bratu problem,Problem8](<https://hplgit.github.io/INF5620/doc/pub/._main_nonlin005.html>)
  Problem8/Eq52: boundary-value equation, analytic cosh family, branch count and printed rounded critical value. The author’s parameter equals2 times our theta. Independent Decimal80 exact-family qualification remains the numerical reference; the printed rounded anchor is a separate coarse check.

完了の根拠：

```json
{
  "verification": "/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/verification.json",
  "inputs": [
    "/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/inputs.json",
    "/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/acceptance.json",
    "/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/pre-run-contract.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/results/bratu-matrix-free-jfnk-preview.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/run.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/README.md",
    "/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/cases.json",
    "/numerical-methods-atlas/validation/verification/2026-11-24-batch48-57-public.json"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#bratu-matrix-free-jfnk-ja",
  "execution": "/numerical-methods-atlas/validation/bratu-matrix-free-jfnk/?lang=ja"
}
```

### 信頼領域と線探索の難しい初期値比較

ID: nonlinear-3 · P2 · 公開済み · 新規実装

調査時の範囲：未収録

調査時の現状：

固定入力のコード・保存図をHRで公開。匿名公開ファイル照合、実HR日英画面、公開ZIP Linux全56群116例1456pytestと全56JUnitの検査が合格。公開時点の条件・参照の読解範囲・失敗履歴は各配布記録を参照。

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

完了の根拠：

```json
{
  "verification": "/numerical-methods-atlas/validation/verification/2026-11-24-batch58-67-public.json",
  "inputs": [
    "/code/validated-examples/2026-11-24/globalization-controls/inputs.json",
    "/code/validated-examples/2026-11-24/globalization-controls/acceptance.json",
    "/code/validated-examples/2026-11-24/globalization-controls/pre-run-contract.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-24/globalization-controls/results/globalization-difficult-starts.png",
    "/code/validated-examples/2026-11-24/globalization-controls/results/globalization-difficult-starts-preview.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-24/globalization-controls/run.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-24/globalization-controls/README.md",
    "/code/validated-examples/2026-11-24/globalization-controls/cases.json",
    "/numerical-methods-atlas/validation/verification/2026-11-24-batch58-67-public.json",
    "/code/validated-examples/2026-11-24/globalization-controls/verification.json"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#globalization-difficult-starts-ja",
  "execution": "/numerical-methods-atlas/validation/globalization-difficult-starts/?lang=ja#globalization-difficult-starts-ja-measurements",
  "note": {
    "ja": "固定入力の正規source実行と独立展開ZIPのpytest/全入力再実行が合格。これは保存した局所科学検証で、同一SHAのHR公開後HTTP/UI/外部Linux確認の完了を意味しません。",
    "en": "Canonical source execution and independently extracted ZIP pytest/all-input reruns passed. This is saved local scientific verification, not a claim that same-SHA post-publication HR HTTP/UI/external Linux checks are complete."
  }
}
```

## 自動微分

### 逆モード VJP の実装と JVP/VJP 双対性検査

ID: automatic-differentiation-1 · P1 · 公開済み · 新規実装

調査時の範囲：解説のみ

調査時の現状：

固定入力のコード・保存図をHRで公開。匿名公開ファイル照合、実HR日英画面、公開ZIP Linux全56群116例1456pytestと全56JUnitの検査が合格。公開時点の条件・参照の読解範囲・失敗履歴は各配布記録を参照。

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
- [The Autodiff Cookbook](<https://docs.jax.dev/en/latest/notebooks/autodiff_cookbook.html>)
  Selected definitions and composition formulas only. A new educational tape will implement the stated finite subset. No JAX installation, execution, timing replication or implementation-source audit. Unread: Original reverse-mode/HVP papers, JAX transformation implementation, Unselected cookbook sections. Publication year not established (n.d.).
- [Frequently asked questions: undefined branches and ordering](<https://docs.jax.dev/en/latest/faq.html>)
  Read invalid inactive-branch and ordering discussions. We use an explicitly different strict nondifferentiability policy, not a universal JAX tie rule. Unread: Linked issue threads, Generalized derivative original papers. Publication year not established (n.d.).

完了の根拠：

```json
{
  "verification": "/numerical-methods-atlas/validation/verification/2026-11-24-batch58-67-public.json",
  "inputs": [
    "/code/validated-examples/2026-11-24/reverse-higher-ad/inputs.json",
    "/code/validated-examples/2026-11-24/reverse-higher-ad/acceptance.json",
    "/code/validated-examples/2026-11-24/reverse-higher-ad/pre-run-contract.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-24/reverse-higher-ad/results/reverse-vjp-duality.png",
    "/code/validated-examples/2026-11-24/reverse-higher-ad/results/reverse-vjp-duality-preview.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-24/reverse-higher-ad/run.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-24/reverse-higher-ad/README.md",
    "/code/validated-examples/2026-11-24/reverse-higher-ad/cases.json",
    "/numerical-methods-atlas/validation/verification/2026-11-24-batch58-67-public.json",
    "/code/validated-examples/2026-11-24/reverse-higher-ad/verification.json"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#reverse-vjp-duality-ja",
  "execution": "/numerical-methods-atlas/validation/reverse-vjp-duality/?lang=ja#reverse-vjp-duality-ja-measurements",
  "note": {
    "ja": "固定入力の正規source実行と独立展開ZIPのpytest/全入力再実行が合格。これは保存した局所科学検証で、同一SHAのHR公開後HTTP/UI/外部Linux確認の完了を意味しません。",
    "en": "Canonical source execution and independently extracted ZIP pytest/all-input reruns passed. This is saved local scientific verification, not a claim that same-SHA post-publication HR HTTP/UI/external Linux checks are complete."
  }
}
```

### Hessian-vector 積・二階微分の検証

ID: automatic-differentiation-2 · P2 · 公開済み · 新規実装

調査時の範囲：解説のみ

調査時の現状：

固定入力のコード・保存図をHRで公開。匿名公開ファイル照合、実HR日英画面、公開ZIP Linux全56群116例1456pytestと全56JUnitの検査が合格。公開時点の条件・参照の読解範囲・失敗履歴は各配布記録を参照。

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
- [The Autodiff Cookbook](<https://docs.jax.dev/en/latest/notebooks/autodiff_cookbook.html>)
  Selected definitions and composition formulas only. A new educational tape will implement the stated finite subset. No JAX installation, execution, timing replication or implementation-source audit. Unread: Original reverse-mode/HVP papers, JAX transformation implementation, Unselected cookbook sections. Publication year not established (n.d.).
- [Frequently asked questions: undefined branches and ordering](<https://docs.jax.dev/en/latest/faq.html>)
  Read invalid inactive-branch and ordering discussions. We use an explicitly different strict nondifferentiability policy, not a universal JAX tie rule. Unread: Linked issue threads, Generalized derivative original papers. Publication year not established (n.d.).

完了の根拠：

```json
{
  "verification": "/numerical-methods-atlas/validation/verification/2026-11-24-batch58-67-public.json",
  "inputs": [
    "/code/validated-examples/2026-11-24/reverse-higher-ad/inputs.json",
    "/code/validated-examples/2026-11-24/reverse-higher-ad/acceptance.json",
    "/code/validated-examples/2026-11-24/reverse-higher-ad/pre-run-contract.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-24/reverse-higher-ad/results/hessian-vector-products.png",
    "/code/validated-examples/2026-11-24/reverse-higher-ad/results/hessian-vector-products-preview.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-24/reverse-higher-ad/run.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-24/reverse-higher-ad/README.md",
    "/code/validated-examples/2026-11-24/reverse-higher-ad/cases.json",
    "/numerical-methods-atlas/validation/verification/2026-11-24-batch58-67-public.json",
    "/code/validated-examples/2026-11-24/reverse-higher-ad/verification.json"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#hessian-vector-products-ja",
  "execution": "/numerical-methods-atlas/validation/hessian-vector-products/?lang=ja#hessian-vector-products-ja-measurements",
  "note": {
    "ja": "固定入力の正規source実行と独立展開ZIPのpytest/全入力再実行が合格。これは保存した局所科学検証で、同一SHAのHR公開後HTTP/UI/外部Linux確認の完了を意味しません。",
    "en": "Canonical source execution and independently extracted ZIP pytest/all-input reruns passed. This is saved local scientific verification, not a claim that same-SHA post-publication HR HTTP/UI/external Linux checks are complete."
  }
}
```

### 分岐・非滑らか演算と微分の適用範囲

ID: automatic-differentiation-3 · P2 · 公開済み · 検証の拡充

調査時の範囲：検証範囲不足

調査時の現状：

固定入力のコード・保存図をHRで公開。匿名公開ファイル照合、実HR日英画面、公開ZIP Linux全56群116例1456pytestと全56JUnitの検査が合格。公開時点の条件・参照の読解範囲・失敗履歴は各配布記録を参照。

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
- [The Autodiff Cookbook](<https://docs.jax.dev/en/latest/notebooks/autodiff_cookbook.html>)
  Selected definitions and composition formulas only. A new educational tape will implement the stated finite subset. No JAX installation, execution, timing replication or implementation-source audit. Unread: Original reverse-mode/HVP papers, JAX transformation implementation, Unselected cookbook sections. Publication year not established (n.d.).
- [Frequently asked questions: undefined branches and ordering](<https://docs.jax.dev/en/latest/faq.html>)
  Read invalid inactive-branch and ordering discussions. We use an explicitly different strict nondifferentiability policy, not a universal JAX tie rule. Unread: Linked issue threads, Generalized derivative original papers. Publication year not established (n.d.).

完了の根拠：

```json
{
  "verification": "/numerical-methods-atlas/validation/verification/2026-11-24-batch58-67-public.json",
  "inputs": [
    "/code/validated-examples/2026-11-24/reverse-higher-ad/inputs.json",
    "/code/validated-examples/2026-11-24/reverse-higher-ad/acceptance.json",
    "/code/validated-examples/2026-11-24/reverse-higher-ad/pre-run-contract.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-24/reverse-higher-ad/results/kink-branch-derivatives.png",
    "/code/validated-examples/2026-11-24/reverse-higher-ad/results/kink-branch-derivatives-preview.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-24/reverse-higher-ad/run.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-24/reverse-higher-ad/README.md",
    "/code/validated-examples/2026-11-24/reverse-higher-ad/cases.json",
    "/numerical-methods-atlas/validation/verification/2026-11-24-batch58-67-public.json",
    "/code/validated-examples/2026-11-24/reverse-higher-ad/verification.json"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#kink-branch-derivatives-ja",
  "execution": "/numerical-methods-atlas/validation/kink-branch-derivatives/?lang=ja#kink-branch-derivatives-ja-measurements",
  "note": {
    "ja": "固定入力の正規source実行と独立展開ZIPのpytest/全入力再実行が合格。これは保存した局所科学検証で、同一SHAのHR公開後HTTP/UI/外部Linux確認の完了を意味しません。",
    "en": "Canonical source execution and independently extracted ZIP pytest/all-input reruns passed. This is saved local scientific verification, not a claim that same-SHA post-publication HR HTTP/UI/external Linux checks are complete."
  }
}
```

## 陰関数微分・感度・随伴法

### 時間依存問題の離散随伴と checkpointing

ID: sensitivity-adjoint-1 · P2 · 公開済み · 新規実装

調査時の範囲：未収録

調査時の現状：

固定入力のコード・保存図をHRで公開。匿名公開ファイル照合、実HR日英画面、公開ZIP Linux全56群116例1456pytestと全56JUnitの検査が合格。公開時点の条件・参照の読解範囲・失敗履歴は各配布記録を参照。

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
- [JAX vjp API](<https://docs.jax.dev/en/latest/_autosummary/jax.vjp.html>)
  Reverse-mode cotangent map definition and input/output shapes. Terminology only; no JAX implementation, library-equivalence or framework execution claim.
- [Python3.12.16 decimal documentation](<https://docs.python.org/3.12/library/decimal.html>)
  Decimal.exp correctly rounded half-even and from_float exact binary-float conversion. This supports arithmetic choices, not an already qualified numerical oracle.
- [Dickson,Kelley,Ipsen,Kevrekidis:Condition Estimates for Pseudo-Arclength Continuation](<https://ipsen.math.ncsu.edu/ps/sinum65438.pdf>)
  Section2.1 implicit sensitivity and2.2 simple-fold definition/arclength equations, printed265–267. Full proofs/experiments not audited; no reference table copied. Continuation already exists in56.
- [Author-hosted INF5620 nonlinear exercises,Problem8,Eq52](<https://hplgit.github.io/INF5620/doc/pub/._main_nonlin005.html>)
  Bratu BVP/cosh family/critical value and FD exercise. Source theta=2*the alpha in old sensitivity module. Continuum family only, never the exact discrete fold/state.

完了の根拠：

```json
{
  "verification": "/numerical-methods-atlas/validation/verification/2026-11-24-batch58-67-public.json",
  "inputs": [
    "/code/validated-examples/2026-11-24/adjoint/inputs.json",
    "/code/validated-examples/2026-11-24/adjoint/acceptance.json",
    "/code/validated-examples/2026-11-24/adjoint/pre-run-contract.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-24/adjoint/results/diffusion-discrete-adjoint.png",
    "/code/validated-examples/2026-11-24/adjoint/results/diffusion-discrete-adjoint-preview.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-24/adjoint/run.py",
    "/code/validated-examples/2026-11-24/adjoint/operators.py",
    "/code/validated-examples/2026-11-24/adjoint/krylov.py",
    "/code/validated-examples/2026-11-24/adjoint/newton.py",
    "/code/validated-examples/2026-11-24/adjoint/time_adjoint.py",
    "/code/validated-examples/2026-11-24/adjoint/references/modal_decimal.py",
    "/code/validated-examples/2026-11-24/adjoint/references/shooting_decimal.py",
    "/code/validated-examples/2026-11-24/adjoint/references/linear_oracle.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-24/adjoint/README.md",
    "/code/validated-examples/2026-11-24/adjoint/cases.json",
    "/numerical-methods-atlas/validation/verification/2026-11-24-batch58-67-public.json",
    "/code/validated-examples/2026-11-24/adjoint/verification.json"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#diffusion-discrete-adjoint-ja",
  "execution": "/numerical-methods-atlas/validation/diffusion-discrete-adjoint/?lang=ja#diffusion-discrete-adjoint-ja-measurements",
  "note": {
    "ja": "固定入力の正規source実行と独立展開ZIPのpytest/全入力再実行が合格。これは保存した局所科学検証で、同一SHAのHR公開後HTTP/UI/外部Linux確認の完了を意味しません。",
    "en": "Canonical source execution and independently extracted ZIP pytest/all-input reruns passed. This is saved local scientific verification, not a claim that same-SHA post-publication HR HTTP/UI/external Linux checks are complete."
  }
}
```

### 折り返し・悪条件下での感度と解法許容誤差

ID: sensitivity-adjoint-2 · P1 · 公開済み · 検証の拡充

調査時の範囲：検証範囲不足

調査時の現状：

固定入力のコード・保存図をHRで公開。匿名公開ファイル照合、実HR日英画面、公開ZIP Linux全56群116例1456pytestと全56JUnitの検査が合格。公開時点の条件・参照の読解範囲・失敗履歴は各配布記録を参照。

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
- [JAX vjp API](<https://docs.jax.dev/en/latest/_autosummary/jax.vjp.html>)
  Reverse-mode cotangent map definition and input/output shapes. Terminology only; no JAX implementation, library-equivalence or framework execution claim.
- [Python3.12.16 decimal documentation](<https://docs.python.org/3.12/library/decimal.html>)
  Decimal.exp correctly rounded half-even and from_float exact binary-float conversion. This supports arithmetic choices, not an already qualified numerical oracle.
- [Dickson,Kelley,Ipsen,Kevrekidis:Condition Estimates for Pseudo-Arclength Continuation](<https://ipsen.math.ncsu.edu/ps/sinum65438.pdf>)
  Section2.1 implicit sensitivity and2.2 simple-fold definition/arclength equations, printed265–267. Full proofs/experiments not audited; no reference table copied. Continuation already exists in56.
- [Author-hosted INF5620 nonlinear exercises,Problem8,Eq52](<https://hplgit.github.io/INF5620/doc/pub/._main_nonlin005.html>)
  Bratu BVP/cosh family/critical value and FD exercise. Source theta=2*the alpha in old sensitivity module. Continuum family only, never the exact discrete fold/state.
- [Python3.12.16 math documentation,math.sumprod](<https://docs.python.org/3.12/library/math.html#math.sumprod>)
  Selected math.sumprod definition,matching-length error,added-in3.12 and builtinfloat/mixedfloat intermediate arithmetic semantics only. No full CPython C implementation audit by this author. Documented extended intermediate precision; no wholeCPython audit or universal correctrounding claim.

完了の根拠：

```json
{
  "verification": "/numerical-methods-atlas/validation/verification/2026-11-24-batch58-67-public.json",
  "inputs": [
    "/code/validated-examples/2026-11-24/adjoint/inputs.json",
    "/code/validated-examples/2026-11-24/adjoint/acceptance.json",
    "/code/validated-examples/2026-11-24/adjoint/pre-run-contract.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-24/adjoint/results/bratu-fold-sensitivity.png",
    "/code/validated-examples/2026-11-24/adjoint/results/bratu-fold-sensitivity-preview.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-24/adjoint/run.py",
    "/code/validated-examples/2026-11-24/adjoint/operators.py",
    "/code/validated-examples/2026-11-24/adjoint/krylov.py",
    "/code/validated-examples/2026-11-24/adjoint/newton.py",
    "/code/validated-examples/2026-11-24/adjoint/fold_study.py",
    "/code/validated-examples/2026-11-24/adjoint/references/modal_decimal.py",
    "/code/validated-examples/2026-11-24/adjoint/references/shooting_decimal.py",
    "/code/validated-examples/2026-11-24/adjoint/references/linear_oracle.py",
    "/code/validated-examples/2026-11-24/adjoint/balanced_operator.py",
    "/code/validated-examples/2026-11-24/adjoint/state_linear.py",
    "/code/validated-examples/2026-11-24/adjoint/state_expansion.py",
    "/code/validated-examples/2026-11-24/adjoint/state_krylov.py",
    "/code/validated-examples/2026-11-24/adjoint/state_jacobian.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-24/adjoint/README.md",
    "/code/validated-examples/2026-11-24/adjoint/cases.json",
    "/numerical-methods-atlas/validation/verification/2026-11-24-batch58-67-public.json",
    "/code/validated-examples/2026-11-24/adjoint/verification.json"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#bratu-fold-sensitivity-ja",
  "execution": "/numerical-methods-atlas/validation/bratu-fold-sensitivity/?lang=ja#bratu-fold-sensitivity-ja-measurements",
  "note": {
    "ja": "固定入力の正規source実行と独立展開ZIPのpytest/全入力再実行が合格。これは保存した局所科学検証で、同一SHAのHR公開後HTTP/UI/外部Linux確認の完了を意味しません。",
    "en": "Canonical source execution and independently extracted ZIP pytest/all-input reruns passed. This is saved local scientific verification, not a claim that same-SHA post-publication HR HTTP/UI/external Linux checks are complete."
  }
}
```

### 多数の空間パラメータへの行列非形成 VJP 展開

ID: sensitivity-adjoint-3 · P2 · 公開済み · 検証の拡充

調査時の範囲：検証範囲不足

調査時の現状：

固定入力のコード・保存図をHRで公開。匿名公開ファイル照合、実HR日英画面、公開ZIP Linux全56群116例1456pytestと全56JUnitの検査が合格。公開時点の条件・参照の読解範囲・失敗履歴は各配布記録を参照。

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
- [JAX vjp API](<https://docs.jax.dev/en/latest/_autosummary/jax.vjp.html>)
  Reverse-mode cotangent map definition and input/output shapes. Terminology only; no JAX implementation, library-equivalence or framework execution claim.
- [Python3.12.16 decimal documentation](<https://docs.python.org/3.12/library/decimal.html>)
  Decimal.exp correctly rounded half-even and from_float exact binary-float conversion. This supports arithmetic choices, not an already qualified numerical oracle.
- [Dickson,Kelley,Ipsen,Kevrekidis:Condition Estimates for Pseudo-Arclength Continuation](<https://ipsen.math.ncsu.edu/ps/sinum65438.pdf>)
  Section2.1 implicit sensitivity and2.2 simple-fold definition/arclength equations, printed265–267. Full proofs/experiments not audited; no reference table copied. Continuation already exists in56.
- [Author-hosted INF5620 nonlinear exercises,Problem8,Eq52](<https://hplgit.github.io/INF5620/doc/pub/._main_nonlin005.html>)
  Bratu BVP/cosh family/critical value and FD exercise. Source theta=2*the alpha in old sensitivity module. Continuum family only, never the exact discrete fold/state.
- [Python3.12.16 math documentation,math.sumprod](<https://docs.python.org/3.12/library/math.html#math.sumprod>)
  Selected math.sumprod definition,matching-length error,added-in3.12 and builtinfloat/mixedfloat intermediate arithmetic semantics only. No full CPython C implementation audit by this author. Documented extended intermediate precision; no wholeCPython audit or universal correctrounding claim.

完了の根拠：

```json
{
  "verification": "/numerical-methods-atlas/validation/verification/2026-11-24-batch58-67-public.json",
  "inputs": [
    "/code/validated-examples/2026-11-24/adjoint/inputs.json",
    "/code/validated-examples/2026-11-24/adjoint/acceptance.json",
    "/code/validated-examples/2026-11-24/adjoint/pre-run-contract.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-24/adjoint/results/bratu-distributed-vjp.png",
    "/code/validated-examples/2026-11-24/adjoint/results/bratu-distributed-vjp-preview.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-24/adjoint/run.py",
    "/code/validated-examples/2026-11-24/adjoint/operators.py",
    "/code/validated-examples/2026-11-24/adjoint/krylov.py",
    "/code/validated-examples/2026-11-24/adjoint/newton.py",
    "/code/validated-examples/2026-11-24/adjoint/distributed.py",
    "/code/validated-examples/2026-11-24/adjoint/references/modal_decimal.py",
    "/code/validated-examples/2026-11-24/adjoint/references/shooting_decimal.py",
    "/code/validated-examples/2026-11-24/adjoint/references/linear_oracle.py",
    "/code/validated-examples/2026-11-24/adjoint/balanced_operator.py",
    "/code/validated-examples/2026-11-24/adjoint/state_linear.py",
    "/code/validated-examples/2026-11-24/adjoint/state_expansion.py",
    "/code/validated-examples/2026-11-24/adjoint/state_krylov.py",
    "/code/validated-examples/2026-11-24/adjoint/state_jacobian.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-24/adjoint/README.md",
    "/code/validated-examples/2026-11-24/adjoint/cases.json",
    "/numerical-methods-atlas/validation/verification/2026-11-24-batch58-67-public.json",
    "/code/validated-examples/2026-11-24/adjoint/verification.json"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#bratu-distributed-vjp-ja",
  "execution": "/numerical-methods-atlas/validation/bratu-distributed-vjp/?lang=ja#bratu-distributed-vjp-ja-measurements",
  "note": {
    "ja": "固定入力の正規source実行と独立展開ZIPのpytest/全入力再実行が合格。これは保存した局所科学検証で、同一SHAのHR公開後HTTP/UI/外部Linux確認の完了を意味しません。",
    "en": "Canonical source execution and independently extracted ZIP pytest/all-input reruns passed. This is saved local scientific verification, not a claim that same-SHA post-publication HR HTTP/UI/external Linux checks are complete."
  }
}
```

## 逆問題・最適化・正則化

### Gauss–Newton/Levenberg–Marquardt と境界付き最小二乗

ID: inverse-optimization-1 · P1 · 公開済み · 新規実装

調査時の範囲：未収録

調査時の現状：

固定入力のコード・保存図をHRで公開。匿名公開ファイル照合、実HR日英画面、公開ZIP Linux全56群116例1456pytestと全56JUnitの検査が合格。公開時点の条件・参照の読解範囲・失敗履歴は各配布記録を参照。

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
- [SciPy 1.14.1 least_squares documentation](<https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.optimize.least_squares.html>)
  Parameters, bounds, callable Jacobian, method-specific ftol/xtol/gtol and x_scale, max_nfev, returned status and Notes on LM and TRF. LM does not handle bounds and requires at least as many residual rows as variables; TRF supports bounds. MINPACK/STIR original papers were not read in this preparation.

完了の根拠：

```json
{
  "verification": "/numerical-methods-atlas/validation/verification/2026-11-24-batch58-67-public.json",
  "inputs": [
    "/code/validated-examples/2026-11-24/inverse-optimization/inputs.json",
    "/code/validated-examples/2026-11-24/inverse-optimization/acceptance.json",
    "/code/validated-examples/2026-11-24/inverse-optimization/pre-run-contract.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-24/inverse-optimization/results/bratu-gn-lm-bounds.png",
    "/code/validated-examples/2026-11-24/inverse-optimization/results/bratu-gn-lm-bounds-preview.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-24/inverse-optimization/run.py",
    "/code/validated-examples/2026-11-24/inverse-optimization/least_squares.py",
    "/code/validated-examples/2026-11-24/inverse-optimization/model.py",
    "/code/validated-examples/2026-11-24/inverse-optimization/references/thomas.py",
    "/code/validated-examples/2026-11-24/inverse-optimization/references/oracles.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-24/inverse-optimization/README.md",
    "/code/validated-examples/2026-11-24/inverse-optimization/cases.json",
    "/numerical-methods-atlas/validation/verification/2026-11-24-batch58-67-public.json",
    "/code/validated-examples/2026-11-24/inverse-optimization/verification.json"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#bratu-gn-lm-bounds-ja",
  "execution": "/numerical-methods-atlas/validation/bratu-gn-lm-bounds/?lang=ja#bratu-gn-lm-bounds-ja-measurements",
  "note": {
    "ja": "固定入力の正規source実行と独立展開ZIPのpytest/全入力再実行が合格。これは保存した局所科学検証で、同一SHAのHR公開後HTTP/UI/外部Linux確認の完了を意味しません。",
    "en": "Canonical source execution and independently extracted ZIP pytest/all-input reruns passed. This is saved local scientific verification, not a claim that same-SHA post-publication HR HTTP/UI/external Linux checks are complete."
  }
}
```

### BFGS/L-BFGS と標準 Rosenbrock 問題の固定検証

ID: inverse-optimization-2 · P2 · 公開済み · 新規実装

調査時の範囲：解説のみ

調査時の現状：

固定入力のコード・保存図をHRで公開。匿名公開ファイル照合、実HR日英画面、公開ZIP Linux全56群116例1456pytestと全56JUnitの検査が合格。公開時点の条件・参照の読解範囲・失敗履歴は各配布記録を参照。

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
- [On the limited memory BFGS method for large scale optimization](<https://users.iems.northwestern.edu/~nocedal/PDFfiles/limited-memory.pdf>)
  Author-hosted PDF selected physical pages 3–5 (printed 2–4), rendered locally and visually inspected: limited storage, deletion of oldest correction, Eq. (2.1) inverse-BFGS, Algorithm 2.1 and Eq. (2.6) retained-update construction. No full-paper/proof/experiment or Section 4 scaling review. The selected original uses weak Wolfe; this study deliberately uses a separately specified strong-Wolfe line search. Current-gamma least-squares scaling is independently derived here, not attributed to unread text.
- [SciPy 1.14.1 line_search documentation](<https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.optimize.line_search.html>)
  Signature, c1/c2, descent-direction requirement, returned failure None and evaluation counts. Cited textbook pages were not read.
- [SciPy 1.14.1 BFGS documentation](<https://docs.scipy.org/doc/scipy-1.14.1/reference/optimize.minimize-bfgs.html>)
  Options gtol, norm, c1/c2, hess_inv0 and precision-loss notes; no claim of reading a BFGS original paper.
- [SciPy 1.14.1 L-BFGS-B documentation](<https://docs.scipy.org/doc/scipy-1.14.1/reference/optimize.minimize-lbfgsb.html>)
  Options maxcor, ftol, gtol/projected-gradient convention, maxfun, maxiter and maxls.
- [A new approach to variable metric algorithms](<https://academic.oup.com/comjnl/article-abstract/13/3/317/345520?login=false>)
  Prior saved publisher metadata/abstract-search record only. Original article full text remains unavailable/unread; no new request was made and no derivation is claimed to have been checked against it.

完了の根拠：

```json
{
  "verification": "/numerical-methods-atlas/validation/verification/2026-11-24-batch58-67-public.json",
  "inputs": [
    "/code/validated-examples/2026-11-24/inverse-optimization/inputs.json",
    "/code/validated-examples/2026-11-24/inverse-optimization/acceptance.json",
    "/code/validated-examples/2026-11-24/inverse-optimization/pre-run-contract.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-24/inverse-optimization/results/bfgs-lbfgs-controls.png",
    "/code/validated-examples/2026-11-24/inverse-optimization/results/bfgs-lbfgs-controls-preview.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-24/inverse-optimization/run.py",
    "/code/validated-examples/2026-11-24/inverse-optimization/quasi_newton.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-24/inverse-optimization/README.md",
    "/code/validated-examples/2026-11-24/inverse-optimization/cases.json",
    "/numerical-methods-atlas/validation/verification/2026-11-24-batch58-67-public.json",
    "/code/validated-examples/2026-11-24/inverse-optimization/verification.json"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#bfgs-lbfgs-controls-ja",
  "execution": "/numerical-methods-atlas/validation/bfgs-lbfgs-controls/?lang=ja#bfgs-lbfgs-controls-ja-measurements",
  "note": {
    "ja": "固定入力の正規source実行と独立展開ZIPのpytest/全入力再実行が合格。これは保存した局所科学検証で、同一SHAのHR公開後HTTP/UI/外部Linux確認の完了を意味しません。",
    "en": "Canonical source execution and independently extracted ZIP pytest/all-input reruns passed. This is saved local scientific verification, not a claim that same-SHA post-publication HR HTTP/UI/external Linux checks are complete."
  }
}
```

### ノイズ・離散化不一致下の正則化選択と推定不確かさ

ID: inverse-optimization-3 · P1 · 公開済み · 検証の拡充

調査時の範囲：検証範囲不足

調査時の現状：

固定入力のコード・保存図をHRで公開。匿名公開ファイル照合、実HR日英画面、公開ZIP Linux全56群116例1456pytestと全56JUnitの検査が合格。公開時点の条件・参照の読解範囲・失敗履歴は各配布記録を参照。

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
- [Regularization Tools, Version 4.1 for Matlab 7.3](<https://www2.compute.dtu.dk/~pcha/Regutools/RTv4manual.pdf>)
  Official author manual: selected text around Section 2.5 and Section 2.9; physical pages 20 and 37 (printed 18 and 35) rendered locally and visually inspected. L-curve residual/solution norm tradeoff and discrepancy equation (2.61) were read. Four-point chord curvature here is a finite-list diagnostic, not the manual spline/corner algorithm, a theorem of optimal regularization or coverage. Original software (1994) and later article (2007) are separate bibliographic works and were not read.
- [SciPy 1.14.1 curve_fit documentation](<https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.optimize.curve_fit.html>)
  sigma/absolute_sigma and covariance interpretation sections. The penalized sandwich covariance in this study is derived independently; it is not presented as curve_fit output.
- [SciPy 1.14.1 least_squares documentation](<https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.optimize.least_squares.html>)
  Parameters, bounds, callable Jacobian, method-specific ftol/xtol/gtol and x_scale, max_nfev, returned status and Notes on LM and TRF. LM does not handle bounds and requires at least as many residual rows as variables; TRF supports bounds. MINPACK/STIR original papers were not read in this preparation.

完了の根拠：

```json
{
  "verification": "/numerical-methods-atlas/validation/verification/2026-11-24-batch58-67-public.json",
  "inputs": [
    "/code/validated-examples/2026-11-24/inverse-optimization/inputs.json",
    "/code/validated-examples/2026-11-24/inverse-optimization/acceptance.json",
    "/code/validated-examples/2026-11-24/inverse-optimization/pre-run-contract.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-24/inverse-optimization/results/bratu-noise-regularization.png",
    "/code/validated-examples/2026-11-24/inverse-optimization/results/bratu-noise-regularization-preview.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-24/inverse-optimization/run.py",
    "/code/validated-examples/2026-11-24/inverse-optimization/regularization.py",
    "/code/validated-examples/2026-11-24/inverse-optimization/least_squares.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-24/inverse-optimization/README.md",
    "/code/validated-examples/2026-11-24/inverse-optimization/cases.json",
    "/numerical-methods-atlas/validation/verification/2026-11-24-batch58-67-public.json",
    "/code/validated-examples/2026-11-24/inverse-optimization/verification.json"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#bratu-noise-regularization-ja",
  "execution": "/numerical-methods-atlas/validation/bratu-noise-regularization/?lang=ja#bratu-noise-regularization-ja-measurements",
  "note": {
    "ja": "固定入力の正規source実行と独立展開ZIPのpytest/全入力再実行が合格。これは保存した局所科学検証で、同一SHAのHR公開後HTTP/UI/外部Linux確認の完了を意味しません。",
    "en": "Canonical source execution and independently extracted ZIP pytest/all-input reruns passed. This is saved local scientific verification, not a claim that same-SHA post-publication HR HTTP/UI/external Linux checks are complete."
  }
}
```

## ODE・時間積分

### 標準 stiff ベンチマーク：Robertson 反応系と van der Pol

ID: ode-time-1 · P1 · 公開済み · 新規実装

調査時の範囲：未収録

調査時の現状：

固定入力と図をHRで公開。公開Linux全60群127例1572pytest・全60JUnitと同一SHAの公開確認が合格。元の未達精度目標は検証PASSと分けて表示・保持する。

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
- [Official SUNDIALS cvRoberts_dns model definition](<https://raw.githubusercontent.com/LLNL/sundials/main/examples/cvode/serial/cvRoberts_dns.c>)
  Read the model, initial values and Jacobian in selected official source sections. The observed main URL is not an immutable release pin. Our T = 0.4 scope does not reproduce the original paper, the long 4e10 benchmark or its numerical tables.
- [SciPy1.14.1 solve_ivp and selected official source](<https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.integrate.solve_ivp.html>)
  Read selected fixed-version method, API, local-tolerance and termination sections. This is not a full audit of the original research papers.
- [scikit-sundae official van der Pol example](<https://scikit-sundae.readthedocs.io/en/stable/examples/van_der_pol.html>)
  Read the equations and initial state in the official binding example. Our mu = 1 and 100, T = 2 inputs are an authored early-transient scope, not an original-paper or full mu = 1000 cycle reproduction.

完了の根拠：

```json
{
  "verification": "/numerical-methods-atlas/validation/verification/2026-11-24-batch68-77-public.json",
  "inputs": [
    "/code/validated-examples/2026-11-24-r2/ode-adaptivity/inputs.json",
    "/code/validated-examples/2026-11-24-r2/ode-adaptivity/acceptance.json",
    "/code/validated-examples/2026-11-24-r2/ode-adaptivity/pre-run-contract.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/robertson-stiff-kinetics.png",
    "/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/robertson-stiff-kinetics-preview.png",
    "/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/van-der-pol-stiff-transition.png",
    "/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/van-der-pol-stiff-transition-preview.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-24-r2/ode-adaptivity/run.py",
    "/code/validated-examples/2026-11-24-r2/ode-adaptivity/experiments.py",
    "/code/validated-examples/2026-11-24-r2/ode-adaptivity/io_contract.py",
    "/code/validated-examples/2026-11-24-r2/ode-adaptivity/reference_eval.py",
    "/code/validated-examples/2026-11-24-r2/ode-adaptivity/models.py",
    "/code/validated-examples/2026-11-24-r2/ode-adaptivity/stiff.py",
    "/code/validated-examples/2026-11-24-r2/ode-adaptivity/reporting_policy.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-24-r2/ode-adaptivity/README.md",
    "/code/validated-examples/2026-11-24-r2/ode-adaptivity/cases.json",
    "/code/validated-examples/2026-11-24-r2/ode-adaptivity/verification.json",
    "/numerical-methods-atlas/validation/verification/2026-11-24-batch68-77-public.json"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#robertson-stiff-kinetics-ja",
  "execution": "/numerical-methods-atlas/validation/robertson-stiff-kinetics/?lang=ja#robertson-stiff-kinetics-ja-measurements",
  "note": {
    "ja": "固定入力の正規実行と独立展開ZIPのpytest・全入力再実行が合格しました。公開後の同一SHAによるHTTP・UI・Linuxの確認は別に記録します。",
    "en": "Canonical execution and independently extracted ZIP pytest/all-input reruns passed. Same-SHA post-publication HTTP, UI and Linux checks are recorded separately."
  },
  "case_ids": [
    "robertson-stiff-kinetics",
    "van-der-pol-stiff-transition"
  ]
}
```

### 埋込み RK45・dense output・イベント位置決め

ID: ode-time-2 · P1 · 公開済み · 新規実装

調査時の範囲：未収録

調査時の現状：

固定入力と図をHRで公開。公開Linux全60群127例1572pytest・全60JUnitと同一SHAの公開確認が合格。元の未達精度目標は検証PASSと分けて表示・保持する。

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
- [SciPy1.14.1 RK45 coefficient and dense-output source](<https://github.com/scipy/scipy/blob/v1.14.1/scipy/integrate/_ivp/rk.py>)
  Read C, A, B, E, P, stage evaluation, accepted/rejected FSAL updates and quartic evaluation. The original Dormand–Prince 1980 and Shampine 1986 papers remain unread beyond bibliography. The adapted coefficient BSD notice is retained.

完了の根拠：

```json
{
  "verification": "/numerical-methods-atlas/validation/verification/2026-11-24-batch68-77-public.json",
  "inputs": [
    "/code/validated-examples/2026-11-24-r2/ode-adaptivity/inputs.json",
    "/code/validated-examples/2026-11-24-r2/ode-adaptivity/acceptance.json",
    "/code/validated-examples/2026-11-24-r2/ode-adaptivity/pre-run-contract.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/rk45-dense-events.png",
    "/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/rk45-dense-events-preview.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-24-r2/ode-adaptivity/run.py",
    "/code/validated-examples/2026-11-24-r2/ode-adaptivity/experiments.py",
    "/code/validated-examples/2026-11-24-r2/ode-adaptivity/io_contract.py",
    "/code/validated-examples/2026-11-24-r2/ode-adaptivity/reference_eval.py",
    "/code/validated-examples/2026-11-24-r2/ode-adaptivity/dopri.py",
    "/code/validated-examples/2026-11-24-r2/ode-adaptivity/tableau.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-24-r2/ode-adaptivity/README.md",
    "/code/validated-examples/2026-11-24-r2/ode-adaptivity/cases.json",
    "/code/validated-examples/2026-11-24-r2/ode-adaptivity/verification.json",
    "/numerical-methods-atlas/validation/verification/2026-11-24-batch68-77-public.json"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#rk45-dense-events-ja",
  "execution": "/numerical-methods-atlas/validation/rk45-dense-events/?lang=ja#rk45-dense-events-ja-measurements",
  "note": {
    "ja": "固定入力の正規実行と独立展開ZIPのpytest・全入力再実行が合格しました。公開後の同一SHAによるHTTP・UI・Linuxの確認は別に記録します。",
    "en": "Canonical execution and independently extracted ZIP pytest/all-input reruns passed. Same-SHA post-publication HTTP, UI and Linux checks are recorded separately."
  }
}
```

### 分割法の境界・時間依存と order reduction

ID: ode-time-3 · P2 · 公開済み · 検証の拡充

調査時の範囲：検証範囲不足

調査時の現状：

固定入力と図をHRで公開。公開Linux全60群127例1572pytest・全60JUnitと同一SHAの公開確認が合格。元の未達精度目標は検証PASSと分けて表示・保持する。

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
- [Overcoming order reduction in diffusion-reaction splitting. Part1: Dirichlet boundary conditions](<https://arxiv.org/abs/1411.0465>)
  Read selected extracted text from the 2014 v1 preprint: section 2, Algorithm 2, the constant-boundary example, section 3.2 assumptions and result, and the one-dimensional example. This was not a full-proof or whole-PDF visual audit; the present linear specialization does not reproduce the nonlinear tables.

完了の根拠：

```json
{
  "verification": "/numerical-methods-atlas/validation/verification/2026-11-24-batch68-77-public.json",
  "inputs": [
    "/code/validated-examples/2026-11-24-r2/ode-adaptivity/inputs.json",
    "/code/validated-examples/2026-11-24-r2/ode-adaptivity/acceptance.json",
    "/code/validated-examples/2026-11-24-r2/ode-adaptivity/pre-run-contract.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/strang-boundary-order-reduction.png",
    "/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/strang-boundary-order-reduction-preview.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-24-r2/ode-adaptivity/run.py",
    "/code/validated-examples/2026-11-24-r2/ode-adaptivity/experiments.py",
    "/code/validated-examples/2026-11-24-r2/ode-adaptivity/io_contract.py",
    "/code/validated-examples/2026-11-24-r2/ode-adaptivity/reference_eval.py",
    "/code/validated-examples/2026-11-24-r2/ode-adaptivity/boundary.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-24-r2/ode-adaptivity/README.md",
    "/code/validated-examples/2026-11-24-r2/ode-adaptivity/cases.json",
    "/code/validated-examples/2026-11-24-r2/ode-adaptivity/verification.json",
    "/numerical-methods-atlas/validation/verification/2026-11-24-batch68-77-public.json"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#strang-boundary-order-reduction-ja",
  "execution": "/numerical-methods-atlas/validation/strang-boundary-order-reduction/?lang=ja#strang-boundary-order-reduction-ja-measurements",
  "note": {
    "ja": "固定入力の正規実行と独立展開ZIPのpytest・全入力再実行が合格しました。公開後の同一SHAによるHTTP・UI・Linuxの確認は別に記録します。",
    "en": "Canonical execution and independently extracted ZIP pytest/all-input reruns passed. Same-SHA post-publication HTTP, UI and Linux checks are recorded separately."
  }
}
```

### Jameson系の定常多段RKによる線形モード減衰

ID: ode-time-additional · P2 · 公開済み · 新規実装

調査時の範囲：解説のみ

調査時の現状：

固定入力と図をHRで公開。公開Linux全60群127例1572pytest・全60JUnitと同一SHAの公開確認が合格。元の未達精度目標は検証PASSと分けて表示・保持する。

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

- [PERFORM time integration schemes](<https://perform.readthedocs.io/en/latest/solver/timeschemes.html>)
  Selected four-stage base-state recurrence. No full JST 1981 paper reading or compressible-flow implementation claim.

完了の根拠：

```json
{
  "verification": "/numerical-methods-atlas/validation/verification/2026-11-24-batch68-77-public.json",
  "inputs": [
    "/code/validated-examples/2026-11-24/steady-rk/inputs.json",
    "/code/validated-examples/2026-11-24/steady-rk/acceptance.json",
    "/code/validated-examples/2026-11-24/steady-rk/pre-run-contract.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-24/steady-rk/results/jameson-steady-linear-modes.png",
    "/code/validated-examples/2026-11-24/steady-rk/results/jameson-steady-linear-modes-preview.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-24/steady-rk/run.py",
    "/code/validated-examples/2026-11-24/steady-rk/steady.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-24/steady-rk/README.md",
    "/code/validated-examples/2026-11-24/steady-rk/cases.json",
    "/code/validated-examples/2026-11-24/steady-rk/verification.json",
    "/numerical-methods-atlas/validation/verification/2026-11-24-batch68-77-public.json"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#jameson-steady-linear-modes-ja",
  "execution": "/numerical-methods-atlas/validation/jameson-steady-linear-modes/?lang=ja#jameson-steady-linear-modes-ja-measurements",
  "note": {
    "ja": "固定入力の正規実行と独立展開ZIPのpytest・全入力再実行が合格しました。公開後の同一SHAによるHTTP・UI・Linuxの確認は別に記録します。",
    "en": "Canonical execution and independently extracted ZIP pytest/all-input reruns passed. Same-SHA post-publication HTTP, UI and Linux checks are recorded separately."
  }
}
```

## 微分代数方程式 DAE

### index-1 DAE：整合初期化込みの最小実装

ID: dae-1 · P1 · 公開済み · 新規実装

調査時の範囲：解説のみ

調査時の現状：

固定入力と図をHRで公開。公開Linux全60群127例1572pytest・全60JUnitと同一SHAの公開確認が合格。元の未達精度目標は検証PASSと分けて表示・保持する。

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
- [SUNDIALS v7.1.1 IDA mathematics, section 5.2](<https://sundials.readthedocs.io/en/v7.1.1/ida/Mathematics_link.html>)
  Residual form, BDF/Newton and consistent initialization sections selected. Section5.2 is not an IDA version. This authored MMS/BE solver is not IDA.

完了の根拠：

```json
{
  "verification": "/numerical-methods-atlas/validation/verification/2026-11-24-batch68-77-public.json",
  "inputs": [
    "/code/validated-examples/2026-11-24/dae-controls/inputs.json",
    "/code/validated-examples/2026-11-24/dae-controls/acceptance.json",
    "/code/validated-examples/2026-11-24/dae-controls/pre-run-contract.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-24/dae-controls/results/index1-dae-consistent-initialization.png",
    "/code/validated-examples/2026-11-24/dae-controls/results/index1-dae-consistent-initialization-preview.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-24/dae-controls/run.py",
    "/code/validated-examples/2026-11-24/dae-controls/models.py",
    "/code/validated-examples/2026-11-24/dae-controls/newton.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-24/dae-controls/README.md",
    "/code/validated-examples/2026-11-24/dae-controls/cases.json",
    "/code/validated-examples/2026-11-24/dae-controls/verification.json",
    "/numerical-methods-atlas/validation/verification/2026-11-24-batch68-77-public.json"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#index1-dae-consistent-initialization-ja",
  "execution": "/numerical-methods-atlas/validation/index1-dae-consistent-initialization/?lang=ja#index1-dae-consistent-initialization-ja-measurements",
  "note": {
    "ja": "固定入力の正規実行と独立展開ZIPのpytest・全入力再実行が合格しました。公開後の同一SHAによるHTTP・UI・Linuxの確認は別に記録します。",
    "en": "Canonical execution and independently extracted ZIP pytest/all-input reruns passed. Same-SHA post-publication HTTP, UI and Linux checks are recorded separately."
  }
}
```

### 名前付き DAE ベンチマーク：Robertson の保存則 DAE 形式

ID: dae-2 · P2 · 公開済み · 新規実装

調査時の範囲：未収録

調査時の現状：

固定入力と図をHRで公開。公開Linux全60群127例1572pytest・全60JUnitと同一SHAの公開確認が合格。元の未達精度目標は検証PASSと分けて表示・保持する。

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
- [SUNDIALS v7.1.1 idaRoberts_dns example](<https://github.com/LLNL/sundials/blob/v7.1.1/examples/ida/serial/idaRoberts_dns.c>)
  Read residual/Jacobian, initialization, tolerances and print format. Own first two residual rows have opposite sign and the same zero set.
- [Stored official v7.1.1 IDA Robertson output](<https://github.com/LLNL/sundials/blob/v7.1.1/examples/ida/serial/idaRoberts_dns.out>)
  Selected printed t=0.4 and4 values only, with Decimal rounding intervals. These approximate IDA values are not exact truth; no IDA run is performed here.

完了の根拠：

```json
{
  "verification": "/numerical-methods-atlas/validation/verification/2026-11-24-batch68-77-public.json",
  "inputs": [
    "/code/validated-examples/2026-11-24/dae-controls/inputs.json",
    "/code/validated-examples/2026-11-24/dae-controls/acceptance.json",
    "/code/validated-examples/2026-11-24/dae-controls/pre-run-contract.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-24/dae-controls/results/robertson-conservation-dae.png",
    "/code/validated-examples/2026-11-24/dae-controls/results/robertson-conservation-dae-preview.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-24/dae-controls/run.py",
    "/code/validated-examples/2026-11-24/dae-controls/models.py",
    "/code/validated-examples/2026-11-24/dae-controls/newton.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-24/dae-controls/README.md",
    "/code/validated-examples/2026-11-24/dae-controls/cases.json",
    "/code/validated-examples/2026-11-24/dae-controls/verification.json",
    "/numerical-methods-atlas/validation/verification/2026-11-24-batch68-77-public.json"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#robertson-stiff-kinetics-ja",
  "execution": "/numerical-methods-atlas/validation/robertson-conservation-dae/?lang=ja#robertson-conservation-dae-ja-measurements",
  "note": {
    "ja": "固定入力の正規実行と独立展開ZIPのpytest・全入力再実行が合格しました。公開後の同一SHAによるHTTP・UI・Linuxの確認は別に記録します。",
    "en": "Canonical execution and independently extracted ZIP pytest/all-input reruns passed. Same-SHA post-publication HTTP, UI and Linux checks are recorded separately."
  }
}
```

### 高 index 系の index reduction と拘束ドリフト

ID: dae-3 · P2 · 公開済み · 新規実装

調査時の範囲：解説のみ

調査時の現状：

固定入力と図をHRで公開。公開Linux全60群127例1572pytest・全60JUnitと同一SHAの公開確認が合格。元の未達精度目標は検証PASSと分けて表示・保持する。

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
- [NIST DLMF section22.19(i), pendulum](<https://dlmf.nist.gov/22.19>)
  Selected pendulum formulas, phase and modulus convention. Authored Cartesian conversion uses K-t; SciPy takes parameter m=k². No full chapter reading claimed.
- [NIST DLMF section19.8(i), arithmetic-geometric mean](<https://dlmf.nist.gov/19.8>)
  Selected AGM/K identity; independent Decimal Machin pi and sine with explicit finite remainders qualify a single fixed modulus.

完了の根拠：

```json
{
  "verification": "/numerical-methods-atlas/validation/verification/2026-11-24-batch68-77-public.json",
  "inputs": [
    "/code/validated-examples/2026-11-24/dae-controls/inputs.json",
    "/code/validated-examples/2026-11-24/dae-controls/acceptance.json",
    "/code/validated-examples/2026-11-24/dae-controls/pre-run-contract.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-24/dae-controls/results/high-index-pendulum.png",
    "/code/validated-examples/2026-11-24/dae-controls/results/high-index-pendulum-preview.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-24/dae-controls/run.py",
    "/code/validated-examples/2026-11-24/dae-controls/models.py",
    "/code/validated-examples/2026-11-24/dae-controls/newton.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-24/dae-controls/README.md",
    "/code/validated-examples/2026-11-24/dae-controls/cases.json",
    "/code/validated-examples/2026-11-24/dae-controls/verification.json",
    "/numerical-methods-atlas/validation/verification/2026-11-24-batch68-77-public.json"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#high-index-pendulum-ja",
  "execution": "/numerical-methods-atlas/validation/high-index-pendulum/?lang=ja#high-index-pendulum-ja-measurements",
  "note": {
    "ja": "固定入力の正規実行と独立展開ZIPのpytest・全入力再実行が合格しました。公開後の同一SHAによるHTTP・UI・Linuxの確認は別に記録します。",
    "en": "Canonical execution and independently extracted ZIP pytest/all-input reruns passed. Same-SHA post-publication HTTP, UI and Linux checks are recorded separately."
  }
}
```

## 幾何積分・Hamilton 系

### SHAKE/RATTLE：拘束付き振り子の固定入力比較

ID: geometric-1 · P2 · 公開済み · 新規実装

調査時の範囲：未収録

調査時の現状：

固定入力と図をHRで公開。公開Linux全60群127例1572pytest・全60JUnitと同一SHAの公開確認が合格。元の未達精度目標は検証PASSと分けて表示・保持する。

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
- [Solving Differential Equations on Manifolds](<https://www.unige.ch/~hairer/poly-sde-mani.pdf>)
  Author-hosted lecture notes, selected printed page50, SectionV.5, equations5.1–5.3 and Theorem5.1 statement, rendered and visually read. Centered SHAKE momentum and RATTLE final tangency are explicit. The original1977 SHAKE and1983 RATTLE articles remain full-text unread; no full proof review is claimed. Source date: 2011 (date displayed on lecture notes); this is not asserted as the publication year.
- [Lecture2: Symplectic integrators](<https://www.unige.ch/~hairer/poly_geoint/week2.pdf>)
  Author-hosted course notes, selected rendered printed pages2,12–13: Verlet kick/drift form, symplectic statement, Lie and symmetric Strang compositions. This does not qualify every state-dependent step rule or the authored coupled resonance experiment. Source date: 2010 (displayed course date); this is not asserted as the publication year.
- [DLMF22.4: Periods, Poles, and Zeros](<https://dlmf.nist.gov/22.4>)
  Official Table22.4.1 selected real periods: sn and cn have4K, dn has2K. Version date is not an initial publication date. Common-period reduction and direct-library periodicity qualification are separate from the independent angular DOP853 state comparison. Source date: 2026 (version); this is not asserted as the publication year.

完了の根拠：

```json
{
  "verification": "/numerical-methods-atlas/validation/verification/2026-11-24-batch68-77-public.json",
  "inputs": [
    "/code/validated-examples/2026-11-24/geometric-controls/inputs.json",
    "/code/validated-examples/2026-11-24/geometric-controls/acceptance.json",
    "/code/validated-examples/2026-11-24/geometric-controls/pre-run-contract.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-24/geometric-controls/results/shake-rattle-pendulum.png",
    "/code/validated-examples/2026-11-24/geometric-controls/results/shake-rattle-pendulum-preview.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-24/geometric-controls/run.py",
    "/code/validated-examples/2026-11-24/geometric-controls/physics.py",
    "/code/validated-examples/2026-11-24/geometric-controls/diagnostics.py",
    "/code/validated-examples/2026-11-24/geometric-controls/references/analytic.py",
    "/code/validated-examples/2026-11-24/geometric-controls/references/discrete.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-24/geometric-controls/README.md",
    "/code/validated-examples/2026-11-24/geometric-controls/cases.json",
    "/code/validated-examples/2026-11-24/geometric-controls/verification.json",
    "/numerical-methods-atlas/validation/verification/2026-11-24-batch68-77-public.json"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#high-index-pendulum-ja",
  "execution": "/numerical-methods-atlas/validation/shake-rattle-pendulum/?lang=ja#shake-rattle-pendulum-ja-measurements",
  "note": {
    "ja": "固定入力の正規実行と独立展開ZIPのpytest・全入力再実行が合格しました。公開後の同一SHAによるHTTP・UI・Linuxの確認は別に記録します。",
    "en": "Canonical execution and independently extracted ZIP pytest/all-input reruns passed. Same-SHA post-publication HTTP, UI and Linux checks are recorded separately."
  }
}
```

### Kepler 問題の離心率依存と近日点誤差

ID: geometric-2 · P2 · 公開済み · 検証の拡充

調査時の範囲：検証範囲不足

調査時の現状：

固定入力と図をHRで公開。公開Linux全60群127例1572pytest・全60JUnitと同一SHAの公開確認が合格。元の未達精度目標は検証PASSと分けて表示・保持する。

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
- [Lecture2: Symplectic integrators](<https://www.unige.ch/~hairer/poly_geoint/week2.pdf>)
  Author-hosted course notes, selected rendered printed pages2,12–13: Verlet kick/drift form, symplectic statement, Lie and symmetric Strang compositions. This does not qualify every state-dependent step rule or the authored coupled resonance experiment. Source date: 2010 (displayed course date); this is not asserted as the publication year.
- [Approximate Positions of the Planets](<https://ssd.jpl.nasa.gov/planets/approx_pos.html>)
  Official JPL page, selected steps3–4 and Kepler equation. Only the eccentric-anomaly equation and elliptic coordinate transformation are used; no planetary coefficient tables, fitted ephemeris accuracy or Horizons calculation is claimed. Publication date was not verified.

完了の根拠：

```json
{
  "verification": "/numerical-methods-atlas/validation/verification/2026-11-24-batch68-77-public.json",
  "inputs": [
    "/code/validated-examples/2026-11-24/geometric-controls/inputs.json",
    "/code/validated-examples/2026-11-24/geometric-controls/acceptance.json",
    "/code/validated-examples/2026-11-24/geometric-controls/pre-run-contract.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-24/geometric-controls/results/kepler-eccentricity.png",
    "/code/validated-examples/2026-11-24/geometric-controls/results/kepler-eccentricity-preview.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-24/geometric-controls/run.py",
    "/code/validated-examples/2026-11-24/geometric-controls/physics.py",
    "/code/validated-examples/2026-11-24/geometric-controls/diagnostics.py",
    "/code/validated-examples/2026-11-24/geometric-controls/references/analytic.py",
    "/code/validated-examples/2026-11-24/geometric-controls/references/discrete.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-24/geometric-controls/README.md",
    "/code/validated-examples/2026-11-24/geometric-controls/cases.json",
    "/code/validated-examples/2026-11-24/geometric-controls/verification.json",
    "/numerical-methods-atlas/validation/verification/2026-11-24-batch68-77-public.json"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#gravity-kepler-ja",
  "execution": "/numerical-methods-atlas/validation/kepler-eccentricity/?lang=ja#kepler-eccentricity-ja-measurements",
  "note": {
    "ja": "固定入力の正規実行と独立展開ZIPのpytest・全入力再実行が合格しました。公開後の同一SHAによるHTTP・UI・Linuxの確認は別に記録します。",
    "en": "Canonical execution and independently extracted ZIP pytest/all-input reruns passed. Same-SHA post-publication HTTP, UI and Linux checks are recorded separately."
  }
}
```

### 多周波数・高振動系での共鳴と安定性限界

ID: geometric-3 · P3 · 公開済み · 検証の拡充

調査時の範囲：検証範囲不足

調査時の現状：

固定入力と図をHRで公開。公開Linux全60群127例1572pytest・全60JUnitと同一SHAの公開確認が合格。元の未達精度目標は検証PASSと分けて表示・保持する。

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
- [Lecture2: Symplectic integrators](<https://www.unige.ch/~hairer/poly_geoint/week2.pdf>)
  Author-hosted course notes, selected rendered printed pages2,12–13: Verlet kick/drift form, symplectic statement, Lie and symmetric Strang compositions. This does not qualify every state-dependent step rule or the authored coupled resonance experiment. Source date: 2010 (displayed course date); this is not asserted as the publication year.

完了の根拠：

```json
{
  "verification": "/numerical-methods-atlas/validation/verification/2026-11-24-batch68-77-public.json",
  "inputs": [
    "/code/validated-examples/2026-11-24/geometric-controls/inputs.json",
    "/code/validated-examples/2026-11-24/geometric-controls/acceptance.json",
    "/code/validated-examples/2026-11-24/geometric-controls/pre-run-contract.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-24/geometric-controls/results/multifrequency-resonance.png",
    "/code/validated-examples/2026-11-24/geometric-controls/results/multifrequency-resonance-preview.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-24/geometric-controls/run.py",
    "/code/validated-examples/2026-11-24/geometric-controls/physics.py",
    "/code/validated-examples/2026-11-24/geometric-controls/diagnostics.py",
    "/code/validated-examples/2026-11-24/geometric-controls/references/analytic.py",
    "/code/validated-examples/2026-11-24/geometric-controls/references/discrete.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-24/geometric-controls/README.md",
    "/code/validated-examples/2026-11-24/geometric-controls/cases.json",
    "/code/validated-examples/2026-11-24/geometric-controls/verification.json",
    "/numerical-methods-atlas/validation/verification/2026-11-24-batch68-77-public.json"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#multifrequency-resonance-ja",
  "execution": "/numerical-methods-atlas/validation/multifrequency-resonance/?lang=ja#multifrequency-resonance-ja-measurements",
  "note": {
    "ja": "固定入力の正規実行と独立展開ZIPのpytest・全入力再実行が合格しました。公開後の同一SHAによるHTTP・UI・Linuxの確認は別に記録します。",
    "en": "Canonical execution and independently extracted ZIP pytest/all-input reruns passed. Same-SHA post-publication HTTP, UI and Linux checks are recorded separately."
  }
}
```

## 数値求積

### 無限区間・振動重み・既知特異点に応じた求積選択

ID: quadrature-1 · P2 · 公開済み · 検証の拡充

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
- [quad: adaptive integration and QUADPACK dispatch](<https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.integrate.quad.html>)
  Selected parameters/full_output and routine dispatch; no complete QUADPACK book/proof audit.

完了の根拠：

```json
{
  "verification": "/numerical-methods-atlas/validation/verification/2026-11-25-batch78-87-public.json",
  "inputs": [
    "/code/validated-examples/2026-11-25/quadrature-controls/inputs.json",
    "/code/validated-examples/2026-11-25/quadrature-controls/acceptance.json",
    "/code/validated-examples/2026-11-25/quadrature-controls/pre-run-contract.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-25/quadrature-controls/results/quadpack-domain-selection.png",
    "/code/validated-examples/2026-11-25/quadrature-controls/results/quadpack-domain-selection-preview.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-25/quadrature-controls/run.py",
    "/code/validated-examples/2026-11-25/quadrature-controls/quadpack_adapter.py",
    "/code/validated-examples/2026-11-25/quadrature-controls/simpson_baseline.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-25/quadrature-controls/README.md",
    "/code/validated-examples/2026-11-25/quadrature-controls/cases.json",
    "/code/validated-examples/2026-11-25/quadrature-controls/source-reading.json",
    "/code/validated-examples/2026-11-25/quadrature-controls/verification.json"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#quadpack-domain-selection-ja",
  "execution": "/numerical-methods-atlas/validation/quadpack-domain-selection/?lang=ja#quadpack-domain-selection-ja-measurements",
  "note": {
    "ja": "正規sourceと独立展開ZIPの固定再現検査を確認しました。元の精度/学習目標は別に保持し、全達成とはみなしません。公開後の同一SHAのCI・Linux・HTTP・画面確認は別です。",
    "en": "Canonical source and independently extracted ZIP reproduction checks passed. Original accuracy and learning goals remain separate; this does not mean every goal was met. Same-SHA post-publication CI, Linux, HTTP and browser checks are separate."
  }
}
```

### Gauss–Kronrod と二重指数変換の教材実装比較

ID: quadrature-2 · P2 · 公開済み · 新規実装

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
- [Pinned SciPy1.14.1 bundled dqk15](<https://raw.githubusercontent.com/scipy/scipy/v1.14.1/scipy/integrate/quadpack/dqk15.f>)
  Displayed table and nesting/resasc safeguards; coefficients are shared-origin, not independently regenerated.
- [Double Exponential Formulas for Numerical Integration](<https://ems.press/doi/pdf/10.2977/prims/1195192451>)
  Selected extracted pp722/724/730 equations; rendered equation screenshots failed. No whole-paper proof/optimality audit.

完了の根拠：

```json
{
  "verification": "/numerical-methods-atlas/validation/verification/2026-11-25-batch78-87-public.json",
  "inputs": [
    "/code/validated-examples/2026-11-25/quadrature-controls/inputs.json",
    "/code/validated-examples/2026-11-25/quadrature-controls/acceptance.json",
    "/code/validated-examples/2026-11-25/quadrature-controls/pre-run-contract.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-25/quadrature-controls/results/gk15-double-exponential.png",
    "/code/validated-examples/2026-11-25/quadrature-controls/results/gk15-double-exponential-preview.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-25/quadrature-controls/run.py",
    "/code/validated-examples/2026-11-25/quadrature-controls/gk15.py",
    "/code/validated-examples/2026-11-25/quadrature-controls/double_exponential.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-25/quadrature-controls/README.md",
    "/code/validated-examples/2026-11-25/quadrature-controls/cases.json",
    "/code/validated-examples/2026-11-25/quadrature-controls/source-reading.json",
    "/code/validated-examples/2026-11-25/quadrature-controls/verification.json"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#gk15-double-exponential-ja",
  "execution": "/numerical-methods-atlas/validation/gk15-double-exponential/?lang=ja#gk15-double-exponential-ja-measurements",
  "note": {
    "ja": "正規sourceと独立展開ZIPの固定再現検査を確認しました。元の精度/学習目標は別に保持し、全達成とはみなしません。公開後の同一SHAのCI・Linux・HTTP・画面確認は別です。",
    "en": "Canonical source and independently extracted ZIP reproduction checks passed. Original accuracy and learning goals remain separate; this does not mean every goal was met. Same-SHA post-publication CI, Linux, HTTP and browser checks are separate."
  }
}
```

### 多次元求積の次元依存：テンソル積と疎格子

ID: quadrature-3 · P3 · 公開済み · 新規実装

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
- [Fast Construction of the Fejer and Clenshaw-Curtis Quadrature Rules](<https://www.sam.math.ethz.ch/sam_reports/reports_final/reports2008/2008-07.pdf>)
  Selected cover/introduction/sec2 extracted equations2.1–2.6; not the entire DFT proof or performance study. This report supports the Clenshaw-Curtis rule only. The Smolyak Delta/combination assembly is independently derived here; the Smolyak1963 and Gerstner-Griebel1998 original bodies remain unread.

完了の根拠：

```json
{
  "verification": "/numerical-methods-atlas/validation/verification/2026-11-25-batch78-87-public.json",
  "inputs": [
    "/code/validated-examples/2026-11-25/quadrature-controls/inputs.json",
    "/code/validated-examples/2026-11-25/quadrature-controls/acceptance.json",
    "/code/validated-examples/2026-11-25/quadrature-controls/pre-run-contract.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-25/quadrature-controls/results/tensor-smolyak-dimensions.png",
    "/code/validated-examples/2026-11-25/quadrature-controls/results/tensor-smolyak-dimensions-preview.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-25/quadrature-controls/run.py",
    "/code/validated-examples/2026-11-25/quadrature-controls/cubature.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-25/quadrature-controls/README.md",
    "/code/validated-examples/2026-11-25/quadrature-controls/cases.json",
    "/code/validated-examples/2026-11-25/quadrature-controls/source-reading.json",
    "/code/validated-examples/2026-11-25/quadrature-controls/verification.json"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#tensor-smolyak-dimensions-ja",
  "execution": "/numerical-methods-atlas/validation/tensor-smolyak-dimensions/?lang=ja#tensor-smolyak-dimensions-ja-measurements",
  "note": {
    "ja": "正規sourceと独立展開ZIPの固定再現検査を確認しました。元の精度/学習目標は別に保持し、全達成とはみなしません。公開後の同一SHAのCI・Linux・HTTP・画面確認は別です。",
    "en": "Canonical source and independently extracted ZIP reproduction checks passed. Original accuracy and learning goals remain separate; this does not mean every goal was met. Same-SHA post-publication CI, Linux, HTTP and browser checks are separate."
  }
}
```

## 補間・近似・ウェーブレット

### Runge 関数：等間隔・Chebyshev 節点と barycentric/Clenshaw 評価

ID: interpolation-approximation-1 · P1 · 公開済み · 新規実装

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
- [NIST DLMF §3.11(ii): Chebyshev series and Clenshaw summation](<https://dlmf.nist.gov/3.11>)
  Selected E7, E9, E11 and E15 with endpoint-halving conventions; no original Clenshaw paper reading. The implementation uses full coefficients, so its final combination is derived explicitly.
- [SciPy 1.14.1 BarycentricInterpolator documentation](<https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.interpolate.BarycentricInterpolator.html>)
  Selected barycentric formula and interpolation-conditioning notes read during the preceding preparation. The Berrut–Trefethen paper is a bibliographic lead, not a full-text reading.

完了の根拠：

```json
{
  "verification": "/numerical-methods-atlas/validation/verification/2026-11-25-batch78-87-public.json",
  "inputs": [
    "/code/validated-examples/2026-11-25/approximation-controls/inputs.json",
    "/code/validated-examples/2026-11-25/approximation-controls/acceptance.json",
    "/code/validated-examples/2026-11-25/approximation-controls/pre-run-contract.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-25/approximation-controls/results/runge-barycentric-clenshaw.png",
    "/code/validated-examples/2026-11-25/approximation-controls/results/runge-barycentric-clenshaw-preview.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-25/approximation-controls/run.py",
    "/code/validated-examples/2026-11-25/approximation-controls/interpolation.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-25/approximation-controls/README.md",
    "/code/validated-examples/2026-11-25/approximation-controls/cases.json",
    "/code/validated-examples/2026-11-25/approximation-controls/source-reading.json",
    "/code/validated-examples/2026-11-25/approximation-controls/verification.json"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#runge-barycentric-clenshaw-ja",
  "execution": "/numerical-methods-atlas/validation/runge-barycentric-clenshaw/?lang=ja#runge-barycentric-clenshaw-ja-measurements",
  "note": {
    "ja": "正規sourceと独立展開ZIPの固定再現検査を確認しました。元の精度/学習目標は別に保持し、全達成とはみなしません。公開後の同一SHAのCI・Linux・HTTP・画面確認は別です。",
    "en": "Canonical source and independently extracted ZIP reproduction checks passed. Original accuracy and learning goals remain separate; this does not mean every goal was met. Same-SHA post-publication CI, Linux, HTTP and browser checks are separate."
  }
}
```

### de Boor スプラインと PCHIP の単調データ比較

ID: interpolation-approximation-2 · P1 · 公開済み · 新規実装

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
- [SciPy 1.14.1 PCHIP documentation and selected source](<https://raw.githubusercontent.com/scipy/scipy/v1.14.1/scipy/interpolate/_cubic.py>)
  Selected lines 202–225, 243–254, 275–298: harmonic interior derivatives, endpoint sign and 3-slope limiter, two-point case. The original Fritsch–Butland paper has not been read in full. Own formulas are independently expressed as scalar Hermite polynomials.
- [SciPy 1.14.1 BSpline and CubicSpline documentation](<https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.interpolate.CubicSpline.html>)
  Natural and clamped boundary conditions and the BSpline recurrence were read during preparation. No de Boor original full-text claim. SciPy is a secondary numerical companion; the rational second-derivative system is the independent reference.

完了の根拠：

```json
{
  "verification": "/numerical-methods-atlas/validation/verification/2026-11-25-batch78-87-public.json",
  "inputs": [
    "/code/validated-examples/2026-11-25/approximation-controls/inputs.json",
    "/code/validated-examples/2026-11-25/approximation-controls/acceptance.json",
    "/code/validated-examples/2026-11-25/approximation-controls/pre-run-contract.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-25/approximation-controls/results/spline-shape-controls.png",
    "/code/validated-examples/2026-11-25/approximation-controls/results/spline-shape-controls-preview.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-25/approximation-controls/run.py",
    "/code/validated-examples/2026-11-25/approximation-controls/splines.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-25/approximation-controls/README.md",
    "/code/validated-examples/2026-11-25/approximation-controls/cases.json",
    "/code/validated-examples/2026-11-25/approximation-controls/source-reading.json",
    "/code/validated-examples/2026-11-25/approximation-controls/verification.json"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#spline-shape-controls-ja",
  "execution": "/numerical-methods-atlas/validation/spline-shape-controls/?lang=ja#spline-shape-controls-ja-measurements",
  "note": {
    "ja": "正規sourceと独立展開ZIPの固定再現検査を確認しました。元の精度/学習目標は別に保持し、全達成とはみなしません。公開後の同一SHAのCI・Linux・HTTP・画面確認は別です。",
    "en": "Canonical source and independently extracted ZIP reproduction checks passed. Original accuracy and learning goals remain separate; this does not mean every goal was met. Same-SHA post-publication CI, Linux, HTTP and browser checks are separate."
  }
}
```

### Mallat 変換・閾値化と境界拡張の実行検証

ID: interpolation-approximation-3 · P3 · 公開済み · 新規実装

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
- [S. Mallat, A Theory for Multiresolution Signal Decomposition: The Wavelet Representation](<https://www.di.ens.fr/~mallat/papiers/MallatTheory89.pdf>)
  During preparation: title/abstract, Haar example on printed p. 679, selected §III-B/C filter/downsample/inverse-pyramid and border-symmetry prose on p. 681. Extracted formula glyphs were imperfect; no complete proof or numerical-table audit is claimed.
- [PyWavelets documentation: Signal extension modes](<https://pywavelets.readthedocs.io/en/latest/ref/signal-extension-modes.html>)
  Periodic and half-sample symmetric extension and the redundancy caveat. This example defines its own append-at-each-odd-level/crop convention; it does not claim PyWavelets coefficient-layout equivalence or require PyWavelets.

完了の根拠：

```json
{
  "verification": "/numerical-methods-atlas/validation/verification/2026-11-25-batch78-87-public.json",
  "inputs": [
    "/code/validated-examples/2026-11-25/approximation-controls/inputs.json",
    "/code/validated-examples/2026-11-25/approximation-controls/acceptance.json",
    "/code/validated-examples/2026-11-25/approximation-controls/pre-run-contract.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-25/approximation-controls/results/haar-mallat-boundary-threshold.png",
    "/code/validated-examples/2026-11-25/approximation-controls/results/haar-mallat-boundary-threshold-preview.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-25/approximation-controls/run.py",
    "/code/validated-examples/2026-11-25/approximation-controls/haar.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-25/approximation-controls/README.md",
    "/code/validated-examples/2026-11-25/approximation-controls/cases.json",
    "/code/validated-examples/2026-11-25/approximation-controls/source-reading.json",
    "/code/validated-examples/2026-11-25/approximation-controls/verification.json"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#haar-mallat-boundary-threshold-ja",
  "execution": "/numerical-methods-atlas/validation/haar-mallat-boundary-threshold/?lang=ja#haar-mallat-boundary-threshold-ja-measurements",
  "note": {
    "ja": "正規sourceと独立展開ZIPの固定再現検査を確認しました。元の精度/学習目標は別に保持し、全達成とはみなしません。公開後の同一SHAのCI・Linux・HTTP・画面確認は別です。",
    "en": "Canonical source and independently extracted ZIP reproduction checks passed. Original accuracy and learning goals remain separate; this does not mean every goal was met. Same-SHA post-publication CI, Linux, HTTP and browser checks are separate."
  }
}
```

## PINN・ニューラル演算子

### 製造解 Poisson PINN と従来法の最小比較

ID: pinn-neural-operators-1 · P2 · 公開済み · 新規実装

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
- [Physics Informed Deep Learning (Part I): Data-driven Solutions of Nonlinear Partial Differential Equations](<https://arxiv.org/pdf/1711.10561>)
  Extracted PDF text selected pp.4–6, §2 continuous-time residual, Eq(2)–(4), Burgers setup and loss/optimizer discussion; not all 22 pages and not visual PDF audit.

完了の根拠：

```json
{
  "verification": "/numerical-methods-atlas/validation/verification/2026-11-25-batch78-87-public.json",
  "inputs": [
    "/code/validated-examples/2026-11-25/small-models/inputs.json",
    "/code/validated-examples/2026-11-25/small-models/acceptance.json",
    "/code/validated-examples/2026-11-25/small-models/pre-run-contract.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-25/small-models/results/pinn-poisson.png",
    "/code/validated-examples/2026-11-25/small-models/results/pinn-poisson-preview.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-25/small-models/run.py",
    "/code/validated-examples/2026-11-25/small-models/experiments.py",
    "/code/validated-examples/2026-11-25/small-models/io_utils.py",
    "/code/validated-examples/2026-11-25/small-models/pinn.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-25/small-models/README.md",
    "/code/validated-examples/2026-11-25/small-models/cases.json",
    "/code/validated-examples/2026-11-25/small-models/source-reading.json",
    "/code/validated-examples/2026-11-25/small-models/verification.json"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#poisson-1d-dirichlet-ja",
  "execution": "/numerical-methods-atlas/validation/pinn-poisson/?lang=ja#pinn-poisson-ja-measurements",
  "note": {
    "ja": "正規sourceと独立展開ZIPの固定再現検査を確認しました。元の精度/学習目標は別に保持し、全達成とはみなしません。公開後の同一SHAのCI・Linux・HTTP・画面確認は別です。",
    "en": "Canonical source and independently extracted ZIP reproduction checks passed. Original accuracy and learning goals remain separate; this does not mean every goal was met. Same-SHA post-publication CI, Linux, HTTP and browser checks are separate."
  },
  "original_goal_summary": {
    "met": 12,
    "total": 15,
    "all_met": false
  }
}
```

### FNO の問題単位 train/test・解像度/OOD 検証

ID: pinn-neural-operators-2 · P3 · 公開済み · 新規実装

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
- [Fourier Neural Operator for Parametric Partial Differential Equations](<https://arxiv.org/html/2010.08895v3>)
  Selected HTML §2 learning operators; §3 Eq(2); §4 Eq(4)–(5), FFT/truncation/reality; §5 setup and §5.1 Burgers. PDF header/edition only; not full paper or appendix audit.

完了の根拠：

```json
{
  "verification": "/numerical-methods-atlas/validation/verification/2026-11-25-batch78-87-public.json",
  "inputs": [
    "/code/validated-examples/2026-11-25/small-models/inputs.json",
    "/code/validated-examples/2026-11-25/small-models/acceptance.json",
    "/code/validated-examples/2026-11-25/small-models/pre-run-contract.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-25/small-models/results/fno-periodic-heat.png",
    "/code/validated-examples/2026-11-25/small-models/results/fno-periodic-heat-preview.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-25/small-models/run.py",
    "/code/validated-examples/2026-11-25/small-models/experiments.py",
    "/code/validated-examples/2026-11-25/small-models/io_utils.py",
    "/code/validated-examples/2026-11-25/small-models/fno.py",
    "/code/validated-examples/2026-11-25/small-models/data_family.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-25/small-models/README.md",
    "/code/validated-examples/2026-11-25/small-models/cases.json",
    "/code/validated-examples/2026-11-25/small-models/source-reading.json",
    "/code/validated-examples/2026-11-25/small-models/verification.json"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#heat-periodic-ja",
  "execution": "/numerical-methods-atlas/validation/fno-periodic-heat/?lang=ja#fno-periodic-heat-ja-measurements",
  "note": {
    "ja": "正規sourceと独立展開ZIPの固定再現検査を確認しました。元の精度/学習目標は別に保持し、全達成とはみなしません。公開後の同一SHAのCI・Linux・HTTP・画面確認は別です。",
    "en": "Canonical source and independently extracted ZIP reproduction checks passed. Original accuracy and learning goals remain separate; this does not mean every goal was met. Same-SHA post-publication CI, Linux, HTTP and browser checks are separate."
  },
  "original_goal_summary": {
    "met": 6,
    "total": 8,
    "all_met": false
  }
}
```

### PINN/FNO の原著本文で損失・分割・適用条件の出典を補足

ID: pinn-neural-operators-3 · P3 · 公開済み · 参照・出典の整備

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
- [Physics Informed Deep Learning (Part I): Data-driven Solutions of Nonlinear Partial Differential Equations](<https://arxiv.org/pdf/1711.10561>)
  Extracted PDF text selected pp.4–6, §2 continuous-time residual, Eq(2)–(4), Burgers setup and loss/optimizer discussion; not all 22 pages and not visual PDF audit.
- [Fourier Neural Operator for Parametric Partial Differential Equations](<https://arxiv.org/html/2010.08895v3>)
  Selected HTML §2 learning operators; §3 Eq(2); §4 Eq(4)–(5), FFT/truncation/reality; §5 setup and §5.1 Burgers. PDF header/edition only; not full paper or appendix audit.

完了の根拠：

```json
{
  "kind": "reference-curation",
  "numerical_case_delta": 0,
  "shared_case_ids": [
    "pinn-poisson",
    "fno-periodic-heat"
  ],
  "verification": "/numerical-methods-atlas/validation/verification/2026-11-25-batch78-87-public.json",
  "inputs": [
    "/code/validated-examples/2026-11-25/small-models/source-reading.json"
  ],
  "references": [
    "https://arxiv.org/pdf/1711.10561",
    "https://arxiv.org/html/2010.08895v3",
    "/code/validated-examples/2026-11-25/small-models/verification.json"
  ],
  "reading": {
    "ja": "/numerical-methods-atlas/ja/read/pinn-operators/#selected-original-source-roles",
    "en": "/numerical-methods-atlas/en/read/pinn-operators/#selected-original-source-roles"
  },
  "note": {
    "ja": "選択閲読の役割を追記します。既存2019論文の抄録/書誌記録を保持し、別の数値例を加算しません。",
    "en": "Append the roles of selected original passages. Preserve the existing 2019 abstract/bibliographic record and add no numerical case."
  },
  "targets": [
    "/numerical-methods-atlas/ja/read/pinn-operators/#selected-original-source-roles",
    "/numerical-methods-atlas/en/read/pinn-operators/#selected-original-source-roles"
  ],
  "proof": [
    "/code/validated-examples/2026-11-25/small-models/source-reading.json",
    "/catalog/atlas-detailed-reading.json"
  ]
}
```

## 生物・化学反応のODE／確率反応

### Michaelis–Menten反応・Lotka–Volterra・SEIRの小規模基準計算

ID: biology-ode-1 · P2 · 公開済み · 新規実装

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

- [Rigorous estimates for the quasi-steady state approximation of the Michaelis–Menten reaction mechanism at low enzyme concentrations](<https://arxiv.org/html/2305.12602v2>)
  Selected §1 Eq(1)–(8) and selected discussion around transient-time estimates Eq(32); proofs and complete quantitative bounds unread.
- [Experiments in MATLAB, Chapter16: Predator-Prey Model](<https://www.mathworks.com/content/dam/mathworks/mathworks-dot-com/moler/exm/chapters/predprey.pdf>)
  Selected extracted text pp3–6: normalized LV equations, equilibrium, periodic-orbit discussion and numerical illustration. No original Lotka/Volterra paper read.
- [The Mathematics of Infectious Diseases](<https://math.uchicago.edu/~shmuel/Modeling/hethcote2000%20Mathematics%20of%20Infectious%20diseases.pdf>)
  Header, selected introduction compartment definitions and §3.1 printedpp618–619, displayed mass-action numbers and Eq(3.1); search around3.2/SEIR limit. Not whole55pages or visual diagram audit.

完了の根拠：

```json
{
  "verification": "/numerical-methods-atlas/validation/verification/2026-11-25-batch78-87-public.json",
  "inputs": [
    "/code/validated-examples/2026-11-25/small-models/inputs.json",
    "/code/validated-examples/2026-11-25/small-models/acceptance.json",
    "/code/validated-examples/2026-11-25/small-models/pre-run-contract.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-25/small-models/results/enzyme-qssa.png",
    "/code/validated-examples/2026-11-25/small-models/results/enzyme-qssa-preview.png",
    "/code/validated-examples/2026-11-25/small-models/results/lotka-volterra.png",
    "/code/validated-examples/2026-11-25/small-models/results/lotka-volterra-preview.png",
    "/code/validated-examples/2026-11-25/small-models/results/seir-linearization.png",
    "/code/validated-examples/2026-11-25/small-models/results/seir-linearization-preview.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-25/small-models/run.py",
    "/code/validated-examples/2026-11-25/small-models/experiments.py",
    "/code/validated-examples/2026-11-25/small-models/io_utils.py",
    "/code/validated-examples/2026-11-25/small-models/biology.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-25/small-models/README.md",
    "/code/validated-examples/2026-11-25/small-models/cases.json",
    "/code/validated-examples/2026-11-25/small-models/source-reading.json",
    "/code/validated-examples/2026-11-25/small-models/verification.json"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#enzyme-qssa-ja",
  "execution": "/numerical-methods-atlas/validation/enzyme-qssa/?lang=ja#enzyme-qssa-ja-measurements",
  "note": {
    "ja": "正規sourceと独立展開ZIPの固定再現検査を確認しました。元の精度/学習目標は別に保持し、全達成とはみなしません。公開後の同一SHAのCI・Linux・HTTP・画面確認は別です。",
    "en": "Canonical source and independently extracted ZIP reproduction checks passed. Original accuracy and learning goals remain separate; this does not mean every goal was met. Same-SHA post-publication CI, Linux, HTTP and browser checks are separate."
  },
  "case_ids": [
    "enzyme-qssa",
    "lotka-volterra",
    "seir-linearization"
  ],
  "original_goal_summary": {
    "met": 42,
    "total": 42,
    "all_met": true
  }
}
```

### Hodgkin–Huxleyの電位固定・静止平衡・発火時刻の検証

ID: biology-ode-2 · P2 · 検証済み · 新規実装

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

2026-11-25に追加した限定範囲：固定Hodgkin–Huxley入力の独立ODE参照・段階所有・パルス区間とHermite発火診断。補間多項式の根の資格確認は一般のODEイベント完全性証明ではありません。

調査時の根拠：

- `catalog/atlas-depth.json` · biology
- `numerical-methods-atlas/assets/biological-models.json`

- [Hodgkin–Huxley (1952), A quantitative description of membrane current…](<https://pmc.ncbi.nlm.nih.gov/articles/PMC1392413/>)
  書誌・抄録または公式文書の範囲を確認。新しい数値再現・全式の監査は未実施。

完了の根拠：

```json
{
  "verification": "/code/validated-examples/2026-11-25/biology-ode-controls/verification.json",
  "inputs": [
    "/code/validated-examples/2026-11-25/biology-ode-controls/inputs.json",
    "/code/validated-examples/2026-11-25/biology-ode-controls/acceptance.json",
    "/code/validated-examples/2026-11-25/biology-ode-controls/freeze.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-25/biology-ode-controls/results/hodgkin-huxley-controls-diagnostics.png",
    "/code/validated-examples/2026-11-25/biology-ode-controls/results/hodgkin-huxley-controls.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-25/biology-ode-controls/run.py",
    "/code/validated-examples/2026-11-25/biology-ode-controls/hh.py",
    "/code/validated-examples/2026-11-25/biology-ode-controls/common.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-25/biology-ode-controls/source-reading.json",
    "/numerical-methods-atlas/solutions/?lang=ja#solution-hodgkin-huxley-controls-ja"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#hodgkin-huxley-controls-ja",
  "execution": "/numerical-methods-atlas/validation/hodgkin-huxley-controls/?lang=ja",
  "case_ids": [
    "hodgkin-huxley-controls"
  ],
  "primary_diagnostics": [
    {
      "path": "/code/validated-examples/2026-11-25/biology-ode-controls/results/result.json",
      "case_id": "hodgkin-huxley-controls",
      "json_pointer": "/cases/0",
      "source_sha256": "104875b041a43542ec5d1500003da8f5986983816e27ce3b88971d11d7b63149",
      "input_sha256": "f15bd046bb65798a49c2e1f5ef75e7aedfb23a7aec0c09f2d11cec5a3a6b58a8"
    }
  ]
}
```

### Gillespie SSAの移入–死亡反応

ID: biology-ode-3 · P2 · 検証済み · 新規実装

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

2026-11-25に追加した限定範囲：移入死亡過程の固定SSAを、区間付きPoisson/binomial法則・実PCG初期状態の識別・独立レプリカの有限標本診断で検査。PRNG一般の被覆保証や任意反応網の保証ではありません。

調査時の根拠：

- `catalog/atlas-depth.json` · biology
- `numerical-methods-atlas/assets/biological-models.json`


完了の根拠：

```json
{
  "verification": "/code/validated-examples/2026-11-25/biology-ode-controls/verification.json",
  "inputs": [
    "/code/validated-examples/2026-11-25/biology-ode-controls/inputs.json",
    "/code/validated-examples/2026-11-25/biology-ode-controls/acceptance.json",
    "/code/validated-examples/2026-11-25/biology-ode-controls/freeze.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-25/biology-ode-controls/results/immigration-death-ssa-diagnostics.png",
    "/code/validated-examples/2026-11-25/biology-ode-controls/results/immigration-death-ssa.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-25/biology-ode-controls/run.py",
    "/code/validated-examples/2026-11-25/biology-ode-controls/ssa.py",
    "/code/validated-examples/2026-11-25/biology-ode-controls/common.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-25/biology-ode-controls/source-reading.json",
    "/numerical-methods-atlas/solutions/?lang=ja#solution-immigration-death-ssa-ja"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#immigration-death-ssa-ja",
  "execution": "/numerical-methods-atlas/validation/immigration-death-ssa/?lang=ja",
  "case_ids": [
    "immigration-death-ssa"
  ],
  "primary_diagnostics": [
    {
      "path": "/code/validated-examples/2026-11-25/biology-ode-controls/results/result.json",
      "case_id": "immigration-death-ssa",
      "json_pointer": "/cases/1",
      "source_sha256": "104875b041a43542ec5d1500003da8f5986983816e27ce3b88971d11d7b63149",
      "input_sha256": "f15bd046bb65798a49c2e1f5ef75e7aedfb23a7aec0c09f2d11cec5a3a6b58a8"
    }
  ]
}
```

## 反応拡散・生物の空間モデル

### Fisher–KPPのAblowitz–Zeppetella厳密進行前線

ID: biology-space-1 · P1 · 検証済み · 新規実装

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

2026-11-25に追加した限定範囲：Fisher–KPPの特定の閉形式進行波と独立MOL参照に対する固定入力の輸送・反応計算。任意初期値の波速選択や一般的なpositivity定理には拡張しません。

調査時の根拠：

- `catalog/atlas-depth.json` · biology
- `numerical-methods-atlas/assets/biological-models.json` · fisher-kpp

- [Ablowitz–Zeppetella (1979), Explicit solutions of Fisher's equation for a special wave speed](<https://doi.org/10.1007/BF02462380>)
  出版社検索結果の書誌と既存生物台帳の特殊前線条件を確認。全文の導出は今回未精査。

完了の根拠：

```json
{
  "verification": "/code/validated-examples/2026-11-25/biology-space-controls/verification.json",
  "inputs": [
    "/code/validated-examples/2026-11-25/biology-space-controls/inputs.json",
    "/code/validated-examples/2026-11-25/biology-space-controls/acceptance.json",
    "/code/validated-examples/2026-11-25/biology-space-controls/freeze.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-25/biology-space-controls/results/fisher-kpp-special-front-diagnostics.png",
    "/code/validated-examples/2026-11-25/biology-space-controls/results/fisher-kpp-special-front.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-25/biology-space-controls/run.py",
    "/code/validated-examples/2026-11-25/biology-space-controls/fisher.py",
    "/code/validated-examples/2026-11-25/biology-space-controls/common.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-25/biology-space-controls/source-reading.json",
    "/numerical-methods-atlas/solutions/?lang=ja#solution-fisher-kpp-special-front-ja"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#fisher-kpp-special-front-ja",
  "execution": "/numerical-methods-atlas/validation/fisher-kpp-special-front/?lang=ja",
  "case_ids": [
    "fisher-kpp-special-front"
  ],
  "primary_diagnostics": [
    {
      "path": "/code/validated-examples/2026-11-25/biology-space-controls/results/result.json",
      "case_id": "fisher-kpp-special-front",
      "json_pointer": "/cases/0",
      "source_sha256": "090c187f89db9d05a2eb437eaf5e73b2dcf1e7600ef0163efd94bae4119cb6eb",
      "input_sha256": "96095517a632f1706713360c82ce01c6d4b68682faa96fecae11e46cb87a1b80"
    }
  ]
}
```

### Schnakenberg等の2D・非周期境界と模様選択

ID: biology-space-2 · P2 · 検証済み · 検証の拡充

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

2026-11-25に追加した限定範囲：Schnakenbergの固定Neumann/Dirichlet条件とFV/Galerkin参照。旧D参照行と失敗履歴を保持し、独立参照のK/Q/許容値の資格確認を別に扱います。

調査時の根拠：

- `catalog/atlas-depth.json` · biology.supplemental_examples
- `numerical-methods-atlas/assets/biological-models.json` · schnakenberg

- [Schnakenberg (1979), Simple chemical reaction systems with limit cycle behaviour](<https://pubmed.ncbi.nlm.nih.gov/537379/>)
  原著書誌を確認。既存の1D実行と原著反応則を混同しない。

完了の根拠：

```json
{
  "verification": "/code/validated-examples/2026-11-25/biology-space-controls/verification.json",
  "inputs": [
    "/code/validated-examples/2026-11-25/biology-space-controls/inputs.json",
    "/code/validated-examples/2026-11-25/biology-space-controls/acceptance.json",
    "/code/validated-examples/2026-11-25/biology-space-controls/freeze.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-25/biology-space-controls/results/schnakenberg-2d-boundary-modes-diagnostics.png",
    "/code/validated-examples/2026-11-25/biology-space-controls/results/schnakenberg-2d-boundary-modes.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-25/biology-space-controls/run.py",
    "/code/validated-examples/2026-11-25/biology-space-controls/schnakenberg.py",
    "/code/validated-examples/2026-11-25/biology-space-controls/common.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-25/biology-space-controls/source-reading.json",
    "/numerical-methods-atlas/solutions/?lang=ja#solution-schnakenberg-2d-boundary-modes-ja"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#schnakenberg-2d-boundary-modes-ja",
  "execution": "/numerical-methods-atlas/validation/schnakenberg-2d-boundary-modes/?lang=ja",
  "case_ids": [
    "schnakenberg-2d-boundary-modes"
  ],
  "primary_diagnostics": [
    {
      "path": "/code/validated-examples/2026-11-25/biology-space-controls/results/result.json",
      "case_id": "schnakenberg-2d-boundary-modes",
      "json_pointer": "/cases/1",
      "source_sha256": "090c187f89db9d05a2eb437eaf5e73b2dcf1e7600ef0163efd94bae4119cb6eb",
      "input_sha256": "96095517a632f1706713360c82ce01c6d4b68682faa96fecae11e46cb87a1b80"
    }
  ]
}
```

### Keller–Segel／移流反応拡散の滑らかな製造解

ID: biology-space-3 · P2 · 検証済み · 新規実装

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

2026-11-25に追加した限定範囲：製造したKeller–Segel場の物理面流束・境界予算・SSP段階を独立空間参照と比較する限定例。一般の走化性blow-upや生物学的推定は未検証です。

調査時の根拠：

- `numerical-methods-atlas/assets/biological-models.json` · keller-segel
- `catalog/atlas-crossovers.json` · reaction-transport


完了の根拠：

```json
{
  "verification": "/code/validated-examples/2026-11-25/biology-space-controls/verification.json",
  "inputs": [
    "/code/validated-examples/2026-11-25/biology-space-controls/inputs.json",
    "/code/validated-examples/2026-11-25/biology-space-controls/acceptance.json",
    "/code/validated-examples/2026-11-25/biology-space-controls/freeze.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-25/biology-space-controls/results/keller-segel-forced-flux-diagnostics.png",
    "/code/validated-examples/2026-11-25/biology-space-controls/results/keller-segel-forced-flux.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-25/biology-space-controls/run.py",
    "/code/validated-examples/2026-11-25/biology-space-controls/keller_segel.py",
    "/code/validated-examples/2026-11-25/biology-space-controls/common.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-25/biology-space-controls/source-reading.json",
    "/numerical-methods-atlas/solutions/?lang=ja#solution-keller-segel-forced-flux-ja"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#keller-segel-forced-flux-ja",
  "execution": "/numerical-methods-atlas/validation/keller-segel-forced-flux/?lang=ja",
  "case_ids": [
    "keller-segel-forced-flux"
  ],
  "primary_diagnostics": [
    {
      "path": "/code/validated-examples/2026-11-25/biology-space-controls/results/result.json",
      "case_id": "keller-segel-forced-flux",
      "json_pointer": "/cases/2",
      "source_sha256": "090c187f89db9d05a2eb437eaf5e73b2dcf1e7600ef0163efd94bae4119cb6eb",
      "input_sha256": "96095517a632f1706713360c82ce01c6d4b68682faa96fecae11e46cb87a1b80"
    }
  ]
}
```

## 古典分子動力学・温度制御

### Nosé–Hoover／chainとBerendsen・速度スケーリングの対照

ID: thermostats-md-1 · P2 · 検証済み · 新規実装

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

2026-11-25に追加した限定範囲：NH/NHCの実サブフロー、物理的反転、eta所有、Berendsen局所逆写像と再スケールの違いを固定例で検査。短い決定論軌道の統計をエルゴード性証明としません。

調査時の根拠：

- `catalog/atlas-depth.json` · temperature
- `catalog/atlas-methods.json` · nose-hoover

- [LAMMPS公式: Nosé–Hoover nvt/npt](<https://docs.lammps.org/fix_nh.html>)
  書誌・抄録または公式文書の範囲を確認。新しい数値再現・全式の監査は未実施。
- [Bussi–Donadio–Parrinello (2007), Canonical sampling through velocity rescaling](<https://arxiv.org/abs/0803.4060>)
  書誌・抄録または公式文書の範囲を確認。新しい数値再現・全式の監査は未実施。

完了の根拠：

```json
{
  "verification": "/code/validated-examples/2026-11-25/thermostat-constraint-controls/verification.json",
  "inputs": [
    "/code/validated-examples/2026-11-25/thermostat-constraint-controls/inputs.json",
    "/code/validated-examples/2026-11-25/thermostat-constraint-controls/acceptance.json",
    "/code/validated-examples/2026-11-25/thermostat-constraint-controls/freeze.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-25/thermostat-constraint-controls/results/deterministic-thermostat-contrasts-diagnostics.png",
    "/code/validated-examples/2026-11-25/thermostat-constraint-controls/results/deterministic-thermostat-contrasts.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-25/thermostat-constraint-controls/run.py",
    "/code/validated-examples/2026-11-25/thermostat-constraint-controls/deterministic.py",
    "/code/validated-examples/2026-11-25/thermostat-constraint-controls/common.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-25/thermostat-constraint-controls/source-reading.json",
    "/numerical-methods-atlas/solutions/?lang=ja#solution-deterministic-thermostat-contrasts-ja"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#thermostatted-quartic-ja",
  "execution": "/numerical-methods-atlas/validation/deterministic-thermostat-contrasts/?lang=ja",
  "case_ids": [
    "deterministic-thermostat-contrasts"
  ],
  "primary_diagnostics": [
    {
      "path": "/code/validated-examples/2026-11-25/thermostat-constraint-controls/results/result.json",
      "case_id": "deterministic-thermostat-contrasts",
      "json_pointer": "/cases/0",
      "source_sha256": "45e4101f6676b2b971b144f5df45c1b28d3bff564d3896eeb309ee6c667d9351",
      "input_sha256": "31c649cecb7a69704ac44dbabeb86ef2fa4f79f941b9902fbe602f402571247d"
    }
  ]
}
```

### 重心除去・拘束・多自由度での正準統計

ID: thermostats-md-2 · P2 · 検証済み · 検証の拡充

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

2026-11-25に追加した限定範囲：線形拘束の実自由度と質量重み付き射影、Langevin過渡共分散と離散定常共分散、CSVRの符号付き統計と誤DOF負例を区別した限定例。

調査時の根拠：

- `catalog/atlas-depth.json` · temperature
- `catalog/atlas-methods.json` · nose-hoover

- [LAMMPS公式: Nosé–Hoover nvt/npt](<https://docs.lammps.org/fix_nh.html>)
  書誌・抄録または公式文書の範囲を確認。新しい数値再現・全式の監査は未実施。

完了の根拠：

```json
{
  "verification": "/code/validated-examples/2026-11-25/thermostat-constraint-controls/verification.json",
  "inputs": [
    "/code/validated-examples/2026-11-25/thermostat-constraint-controls/inputs.json",
    "/code/validated-examples/2026-11-25/thermostat-constraint-controls/acceptance.json",
    "/code/validated-examples/2026-11-25/thermostat-constraint-controls/freeze.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-25/thermostat-constraint-controls/results/projected-canonical-dof-diagnostics.png",
    "/code/validated-examples/2026-11-25/thermostat-constraint-controls/results/projected-canonical-dof.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-25/thermostat-constraint-controls/run.py",
    "/code/validated-examples/2026-11-25/thermostat-constraint-controls/constrained.py",
    "/code/validated-examples/2026-11-25/thermostat-constraint-controls/common.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-25/thermostat-constraint-controls/source-reading.json",
    "/numerical-methods-atlas/solutions/?lang=ja#solution-projected-canonical-dof-ja"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#projected-canonical-dof-ja",
  "execution": "/numerical-methods-atlas/validation/projected-canonical-dof/?lang=ja",
  "case_ids": [
    "projected-canonical-dof"
  ],
  "primary_diagnostics": [
    {
      "path": "/code/validated-examples/2026-11-25/thermostat-constraint-controls/results/result.json",
      "case_id": "projected-canonical-dof",
      "json_pointer": "/cases/1",
      "source_sha256": "45e4101f6676b2b971b144f5df45c1b28d3bff564d3896eeb309ee6c667d9351",
      "input_sha256": "31c649cecb7a69704ac44dbabeb86ef2fa4f79f941b9902fbe602f402571247d"
    }
  ]
}
```

### BOMD／CPMDと熱浴の連成・長いNVE

ID: thermostats-md-3 · P3 · 検証済み · 検証の拡充

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

2026-11-25に追加した限定範囲：規格化した2準位電子角と1核座標の自作BO/CP型模型、短いNVEと1核OU熱浴。M=20、架空角質量μ=.04/.01で、cp.xのemassや第一原理CPMDではありません。 残る未検証：長時間の第一原理NVE、一般の多軌道直交拘束・SCF/力誤差・断熱分離、電子/核の一般熱浴、正準平衡・エルゴード性、実物質。

調査時の根拠：

- `catalog/atlas-depth.json` · temperature
- `catalog/atlas-methods.json` · nose-hoover


完了の根拠：

```json
{
  "verification": "/code/validated-examples/2026-11-25/quantum-small/verification.json",
  "inputs": [
    "/code/validated-examples/2026-11-25/quantum-small/inputs.json",
    "/code/validated-examples/2026-11-25/quantum-small/acceptance.json",
    "/code/validated-examples/2026-11-25/quantum-small/freeze.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-25/quantum-small/results/two-state-bo-cp-ou.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-25/quantum-small/run.py",
    "/code/validated-examples/2026-11-25/quantum-small/coupled_md.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-25/quantum-small/provenance.json",
    "/numerical-methods-atlas/solutions/?lang=ja#solution-two-state-bo-cp-ou-ja"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#two-state-bo-cp-model-ja",
  "execution": "/numerical-methods-atlas/validation/two-state-bo-cp-ou/?lang=ja",
  "case_ids": [
    "two-state-bo-cp-ou"
  ],
  "primary_diagnostics": [
    {
      "path": "/code/validated-examples/2026-11-25/quantum-small/results/result.json",
      "case_id": "two-state-bo-cp-ou",
      "json_pointer": "/cases/0",
      "source_sha256": "750fa3e7f3fe79a96aaacd46039bf00f18b7623d7c4b09035b3c850bfd5d2c20",
      "input_sha256": "36f9b4b9293e5b34d554014134fbce6c31ec11a09a50d1bb5179e9dcb1cee21a"
    }
  ]
}
```

## Schrödinger・孤立原子

### 既存H/Heの式・規格化・出典を独立参照解カードへ収録

ID: quantum-atomic-1 · P1 · 検証済み · 参照・出典の整備

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

2026-11-25に追加した限定範囲：既存H/Heの式、u/p/nの測度、単位と保存した3行の有限基底参照を再照合するカード。新しいSCF/電子状態計算・外部参照の再生成は0回です。

調査時の根拠：

- `catalog/atlas-depth.json` · quantum-atoms
- `catalog/atlas-quantum.json` · hydrogen

- [PySCF公式: Self-consistent field methods](<https://pyscf.org/user/scf.html>)
  書誌・抄録または公式文書の範囲を確認。新しい数値再現・全式の監査は未実施。

完了の根拠：

```json
{
  "targets": [
    "/code/validated-examples/2026-11-25/quantum-small/saved-data/atom-reference.json",
    "/code/validated-examples/2026-11-25/quantum-small/provenance.json",
    "/numerical-methods-atlas/solutions/?lang=ja#solution-atomic-reference-cards-ja"
  ],
  "proof": [
    "/code/validated-examples/2026-11-25/quantum-small/verification.json",
    "/code/validated-examples/2026-11-25/quantum-small/source-manifest.json",
    "/code/validated-examples/2026-11-25/quantum-small/results/result.json"
  ],
  "note": "保存済み参照の再照合であり、新SCF/電子状態計算は0回。既存H/Heの式、u/p/nの測度、単位と保存した3行の有限基底参照を再照合するカード。新しいSCF/電子状態計算・外部参照の再生成は0回です。",
  "verification": "/code/validated-examples/2026-11-25/quantum-small/verification.json",
  "inputs": [
    "/code/validated-examples/2026-11-25/quantum-small/inputs.json",
    "/code/validated-examples/2026-11-25/quantum-small/acceptance.json",
    "/code/validated-examples/2026-11-25/quantum-small/freeze.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-25/quantum-small/results/atomic-reference-cards.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-25/quantum-small/run.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-25/quantum-small/provenance.json",
    "/numerical-methods-atlas/solutions/?lang=ja#solution-atomic-reference-cards-ja"
  ],
  "case_ids": [
    "atomic-reference-cards"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#helium-ground-state-ja",
  "execution": "/numerical-methods-atlas/validation/atomic-reference-cards/?lang=ja",
  "primary_diagnostics": [
    {
      "path": "/code/validated-examples/2026-11-25/quantum-small/results/result.json",
      "case_id": "atomic-reference-cards",
      "json_pointer": "/cases/1",
      "source_sha256": "750fa3e7f3fe79a96aaacd46039bf00f18b7623d7c4b09035b3c850bfd5d2c20",
      "input_sha256": "36f9b4b9293e5b34d554014134fbce6c31ec11a09a50d1bb5179e9dcb1cee21a"
    }
  ]
}
```

### 箱型井戸・調和振動子等の軽量固有値ベンチマーク

ID: quantum-atomic-2 · P2 · 検証済み · 新規実装

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
2026-11-25に追加した限定範囲：1D箱型井戸と有限箱HOの固定8行列から得た固有対を、native規格化・残差・閉形式参照と照合。HOの壁と格子の個別誤差保証や節数の厳密証明ではありません。

調査時の根拠：

- `catalog/atlas-depth.json` · quantum-atoms
- `catalog/atlas-quantum.json` · hydrogen


完了の根拠：

```json
{
  "verification": "/code/validated-examples/2026-11-25/quantum-small/verification.json",
  "inputs": [
    "/code/validated-examples/2026-11-25/quantum-small/inputs.json",
    "/code/validated-examples/2026-11-25/quantum-small/acceptance.json",
    "/code/validated-examples/2026-11-25/quantum-small/freeze.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-25/quantum-small/results/quantum-box-ho.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-25/quantum-small/run.py",
    "/code/validated-examples/2026-11-25/quantum-small/eigenpairs.py",
    "/code/validated-examples/2026-11-25/quantum-small/io_utils.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-25/quantum-small/provenance.json",
    "/numerical-methods-atlas/solutions/?lang=ja#solution-quantum-box-ho-ja"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#quantum-box-ho-ja",
  "execution": "/numerical-methods-atlas/validation/quantum-box-ho/?lang=ja",
  "case_ids": [
    "quantum-box-ho"
  ],
  "primary_diagnostics": [
    {
      "path": "/code/validated-examples/2026-11-25/quantum-small/results/result.json",
      "case_id": "quantum-box-ho",
      "json_pointer": "/cases/2",
      "source_sha256": "750fa3e7f3fe79a96aaacd46039bf00f18b7623d7c4b09035b3c850bfd5d2c20",
      "input_sha256": "36f9b4b9293e5b34d554014134fbce6c31ec11a09a50d1bb5179e9dcb1cee21a"
    }
  ]
}
```

## 分子HF・電子相関

### 最小基底H₂のRHF／UHF／FCI比較

ID: quantum-molecule-1 · P2 · 検証済み · 新規実装

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

2026-11-25に追加した限定範囲：同じ明示STO-3G 2AOのH2を2固定距離でRHF/UHF/有限基底FCI比較。αβスピン混入を保存し、FCIを連続空間の厳密化学や一般解離曲線と呼びません。

調査時の根拠：

- `catalog/atlas-depth.json` · quantum-molecular
- `catalog/atlas-quantum.json` · h2-hf-dft

- [PySCF公式: Self-consistent field methods](<https://pyscf.org/user/scf.html>)
  書誌・抄録または公式文書の範囲を確認。新しい数値再現・全式の監査は未実施。

完了の根拠：

```json
{
  "verification": "/code/validated-examples/2026-11-25/quantum-small/verification.json",
  "inputs": [
    "/code/validated-examples/2026-11-25/quantum-small/inputs.json",
    "/code/validated-examples/2026-11-25/quantum-small/acceptance.json",
    "/code/validated-examples/2026-11-25/quantum-small/freeze.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-25/quantum-small/results/h2-rhf-uhf-fci.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-25/quantum-small/run.py",
    "/code/validated-examples/2026-11-25/quantum-small/molecules.py",
    "/code/validated-examples/2026-11-25/quantum-small/io_utils.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-25/quantum-small/provenance.json",
    "/numerical-methods-atlas/solutions/?lang=ja#solution-h2-rhf-uhf-fci-ja"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#h2-rhf-ja",
  "execution": "/numerical-methods-atlas/validation/h2-rhf-uhf-fci/?lang=ja",
  "case_ids": [
    "h2-rhf-uhf-fci"
  ],
  "primary_diagnostics": [
    {
      "path": "/code/validated-examples/2026-11-25/quantum-small/results/result.json",
      "case_id": "h2-rhf-uhf-fci",
      "json_pointer": "/cases/3",
      "source_sha256": "750fa3e7f3fe79a96aaacd46039bf00f18b7623d7c4b09035b3c850bfd5d2c20",
      "input_sha256": "36f9b4b9293e5b34d554014134fbce6c31ec11a09a50d1bb5179e9dcb1cee21a"
    }
  ]
}
```

### 一般分子・分子DFT・MP2/CC/多参照の実証

ID: quantum-molecule-2 · P3 · 検証済み · 新規実装

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

2026-11-25に追加した限定範囲：1つの非対称3中心H3+・2電子/3s軌道のRHF/MP2/有限基底FCI。独立な演算子組立・2電子RS2恒等式は、外部化学エンジンの独立スカラー参照と区別します。 残る未実装/未検証：一般分子DFT、CC、一般多参照法、大基底・広い分子群、化学精度・精密エネルギー、構造最適化。MP2は変分上界ではありません。

調査時の根拠：

- `catalog/atlas-depth.json` · quantum-molecular
- `catalog/atlas-quantum.json` · h2-hf-dft

- [PySCF公式: Self-consistent field methods](<https://pyscf.org/user/scf.html>)
  書誌・抄録または公式文書の範囲を確認。新しい数値再現・全式の監査は未実施。

完了の根拠：

```json
{
  "verification": "/code/validated-examples/2026-11-25/quantum-small/verification.json",
  "inputs": [
    "/code/validated-examples/2026-11-25/quantum-small/inputs.json",
    "/code/validated-examples/2026-11-25/quantum-small/acceptance.json",
    "/code/validated-examples/2026-11-25/quantum-small/freeze.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-25/quantum-small/results/h3plus-mp2-fci.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-25/quantum-small/run.py",
    "/code/validated-examples/2026-11-25/quantum-small/molecules.py",
    "/code/validated-examples/2026-11-25/quantum-small/io_utils.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-25/quantum-small/provenance.json",
    "/numerical-methods-atlas/solutions/?lang=ja#solution-h3plus-mp2-fci-ja"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#h3plus-minimal-ja",
  "execution": "/numerical-methods-atlas/validation/h3plus-mp2-fci/?lang=ja",
  "case_ids": [
    "h3plus-mp2-fci"
  ],
  "primary_diagnostics": [
    {
      "path": "/code/validated-examples/2026-11-25/quantum-small/results/result.json",
      "case_id": "h3plus-mp2-fci",
      "json_pointer": "/cases/4",
      "source_sha256": "750fa3e7f3fe79a96aaacd46039bf00f18b7623d7c4b09035b3c850bfd5d2c20",
      "input_sha256": "36f9b4b9293e5b34d554014134fbce6c31ec11a09a50d1bb5179e9dcb1cee21a"
    }
  ]
}
```

## 周期DFT・力・第一原理MD

### 既存Heのエネルギー／力の参照値と出典の集約

ID: quantum-periodic-1 · P1 · 検証済み · 参照・出典の整備

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

2026-11-25に追加した限定範囲：人工2He・4電子・5bohrセル、局所GTH・LDA_X+VWN・旧コード版の保存エネルギー/6座標力を再照合する参照監査。新SCF/DFTK/PySCF計算やk点/基底/cutoff走査は0回です。

調査時の根拠：

- `catalog/atlas-depth.json` · quantum-periodic
- `catalog/atlas-forces-reading.json`

- [DFTK公式: Pseudopotentials](<https://docs.dftk.org/stable/examples/pseudopotentials/>)
  書誌・抄録または公式文書の範囲を確認。新しい数値再現・全式の監査は未実施。

完了の根拠：

```json
{
  "targets": [
    "/code/validated-examples/2026-11-25/quantum-small/saved-data/periodic-he-reference.json",
    "/code/validated-examples/2026-11-25/quantum-small/provenance.json",
    "/numerical-methods-atlas/solutions/?lang=ja#solution-periodic-he-reference-cards-ja"
  ],
  "proof": [
    "/code/validated-examples/2026-11-25/quantum-small/verification.json",
    "/code/validated-examples/2026-11-25/quantum-small/source-manifest.json",
    "/code/validated-examples/2026-11-25/quantum-small/results/result.json"
  ],
  "note": "保存済み参照の再照合であり、新SCF/電子状態計算は0回。人工2He・4電子・5bohrセル、局所GTH・LDA_X+VWN・旧コード版の保存エネルギー/6座標力を再照合する参照監査。新SCF/DFTK/PySCF計算やk点/基底/cutoff走査は0回です。",
  "verification": "/code/validated-examples/2026-11-25/quantum-small/verification.json",
  "inputs": [
    "/code/validated-examples/2026-11-25/quantum-small/inputs.json",
    "/code/validated-examples/2026-11-25/quantum-small/acceptance.json",
    "/code/validated-examples/2026-11-25/quantum-small/freeze.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-25/quantum-small/results/periodic-he-reference-cards.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-25/quantum-small/run.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-25/quantum-small/provenance.json",
    "/numerical-methods-atlas/solutions/?lang=ja#solution-periodic-he-reference-cards-ja"
  ],
  "case_ids": [
    "periodic-he-reference-cards"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#periodic-he-forces-ja",
  "execution": "/numerical-methods-atlas/validation/periodic-he-reference-cards/?lang=ja",
  "primary_diagnostics": [
    {
      "path": "/code/validated-examples/2026-11-25/quantum-small/results/result.json",
      "case_id": "periodic-he-reference-cards",
      "json_pointer": "/cases/5",
      "source_sha256": "750fa3e7f3fe79a96aaacd46039bf00f18b7623d7c4b09035b3c850bfd5d2c20",
      "input_sha256": "36f9b4b9293e5b34d554014134fbce6c31ec11a09a50d1bb5179e9dcb1cee21a"
    }
  ]
}
```

### 一般物質・金属・非局所擬ポテンシャル・長時間MD

ID: quantum-periodic-2 · P3 · 検証済み · 検証の拡充

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

2026-11-25に追加した限定範囲：G=-1,0,1と2固定k点の自作rank-one非局所核・平均Fermi占有N=1.5・固定NのHelmholtz自由エネルギー力。整数粒子の正準多体系や実金属・元素適合ノルム保存PSPではありません。 残る未実装/未検証：実在材料・一般金属、元素適合ノルム保存擬ポテンシャル、自己無撞着Hartree/XC、基底/k点/cutoff収束、長時間第一原理MD。

調査時の根拠：

- `catalog/atlas-depth.json` · quantum-periodic
- `catalog/atlas-forces-reading.json`

- [DFTK公式: Pseudopotentials](<https://docs.dftk.org/stable/examples/pseudopotentials/>)
  書誌・抄録または公式文書の範囲を確認。新しい数値再現・全式の監査は未実施。

完了の根拠：

```json
{
  "verification": "/code/validated-examples/2026-11-25/quantum-small/verification.json",
  "inputs": [
    "/code/validated-examples/2026-11-25/quantum-small/inputs.json",
    "/code/validated-examples/2026-11-25/quantum-small/acceptance.json",
    "/code/validated-examples/2026-11-25/quantum-small/freeze.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-25/quantum-small/results/periodic-projector-occupations.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-25/quantum-small/run.py",
    "/code/validated-examples/2026-11-25/quantum-small/periodic_projector.py",
    "/code/validated-examples/2026-11-25/quantum-small/io_utils.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-25/quantum-small/provenance.json",
    "/numerical-methods-atlas/solutions/?lang=ja#solution-periodic-projector-occupations-ja"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#finite-projector-fermi-ja",
  "execution": "/numerical-methods-atlas/validation/periodic-projector-occupations/?lang=ja",
  "case_ids": [
    "periodic-projector-occupations"
  ],
  "primary_diagnostics": [
    {
      "path": "/code/validated-examples/2026-11-25/quantum-small/results/result.json",
      "case_id": "periodic-projector-occupations",
      "json_pointer": "/cases/6",
      "source_sha256": "750fa3e7f3fe79a96aaacd46039bf00f18b7623d7c4b09035b3c850bfd5d2c20",
      "input_sha256": "36f9b4b9293e5b34d554014134fbce6c31ec11a09a50d1bb5179e9dcb1cee21a"
    }
  ]
}
```

## SPH・Godunov SPH

### GSPHの1D Sod衝撃管

ID: sph-gsph-1 · P2 · 検証済み · 新規実装

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

2026-11-25に追加した限定範囲：Gaussian線形比体積畳み込み・対称可変h・独立対Riemann解・反対称全エネルギー交換の実GSPHをSodで検査。通常SPHへp*を入れる代用や論文のcubic/MUSCL再現ではありません。

調査時の根拠：

- `catalog/atlas-methods.json` · sph/gsph
- `numerical-methods-atlas/references.json` · inutsuka2002

- [Inutsuka (2002), Reformulation of Smoothed Particle Hydrodynamics with Riemann Solver](<https://arxiv.org/abs/astro-ph/0206401>)
  出版社抄録と書誌を確認。既存アトラスには著者稿の節2–4の読書記録がある。今回新しい実装・原著数値再現はしていない。

完了の根拠：

```json
{
  "verification": "/code/validated-examples/2026-11-25/continuum-particle-controls/verification.json",
  "inputs": [
    "/code/validated-examples/2026-11-25/continuum-particle-controls/inputs.json",
    "/code/validated-examples/2026-11-25/continuum-particle-controls/acceptance.json",
    "/code/validated-examples/2026-11-25/continuum-particle-controls/freeze.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-25/continuum-particle-controls/results/gsph-sod-preview.png",
    "/code/validated-examples/2026-11-25/continuum-particle-controls/results/gsph-sod.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-25/continuum-particle-controls/run.py",
    "/code/validated-examples/2026-11-25/continuum-particle-controls/gsph.py",
    "/code/validated-examples/2026-11-25/continuum-particle-controls/reference_riemann.py",
    "/code/validated-examples/2026-11-25/continuum-particle-controls/failure_support.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-25/continuum-particle-controls/source-reading.json",
    "/numerical-methods-atlas/solutions/?lang=ja#solution-gsph-sod-ja"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#sod-ja",
  "execution": "/numerical-methods-atlas/validation/gsph-sod/?lang=ja",
  "case_ids": [
    "gsph-sod"
  ],
  "primary_diagnostics": [
    {
      "path": "/code/validated-examples/2026-11-25/continuum-particle-controls/results/result.json",
      "case_id": "gsph-sod",
      "json_pointer": "/cases/3",
      "source_sha256": "cab002c93e01d997562f3c145e1aaddd6a2a8ce59a087d44e8bddc4679081bbf",
      "input_sha256": "5f49881f37b07c47f674979a4886e6da0421be06ddb6bb213ab7dfea6bf6e0f5"
    }
  ]
}
```

### 静止一様圧力・線形音波の粒子配置依存

ID: sph-gsph-2 · P2 · 検証済み · 検証の拡充

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

2026-11-25に追加した限定範囲：規則/摂動粒子の一様圧力と小振幅音波をSPH/GSPHで比較。図の初期kernel誤差0.011834はA=.001より大きく、判定は基本Fourierモードの位相/振幅等の固定条件であり、点ごとの高精度を主張しません。

調査時の根拠：

- `catalog/atlas-methods.json` · sph/gsph
- `numerical-methods-atlas/references.json` · inutsuka2002


完了の根拠：

```json
{
  "verification": "/code/validated-examples/2026-11-25/continuum-particle-controls/verification.json",
  "inputs": [
    "/code/validated-examples/2026-11-25/continuum-particle-controls/inputs.json",
    "/code/validated-examples/2026-11-25/continuum-particle-controls/acceptance.json",
    "/code/validated-examples/2026-11-25/continuum-particle-controls/freeze.json"
  ],
  "plots": [
    "/code/validated-examples/2026-11-25/continuum-particle-controls/results/sph-pressure-acoustics-preview.png",
    "/code/validated-examples/2026-11-25/continuum-particle-controls/results/sph-pressure-acoustics.png"
  ],
  "code": [
    "/code/validated-examples/2026-11-25/continuum-particle-controls/run.py",
    "/code/validated-examples/2026-11-25/continuum-particle-controls/gsph.py",
    "/code/validated-examples/2026-11-25/continuum-particle-controls/failure_support.py"
  ],
  "references": [
    "/code/validated-examples/2026-11-25/continuum-particle-controls/source-reading.json",
    "/numerical-methods-atlas/solutions/?lang=ja#solution-sph-pressure-acoustics-ja"
  ],
  "gallery": "/numerical-methods-atlas/gallery/?lang=ja#sph-pressure-acoustics-ja",
  "execution": "/numerical-methods-atlas/validation/sph-pressure-acoustics/?lang=ja",
  "case_ids": [
    "sph-pressure-acoustics"
  ],
  "primary_diagnostics": [
    {
      "path": "/code/validated-examples/2026-11-25/continuum-particle-controls/results/result.json",
      "case_id": "sph-pressure-acoustics",
      "json_pointer": "/cases/4",
      "source_sha256": "cab002c93e01d997562f3c145e1aaddd6a2a8ce59a087d44e8bddc4679081bbf",
      "input_sha256": "5f49881f37b07c47f674979a4886e6da0421be06ddb6bb213ab7dfea6bf6e0f5"
    }
  ]
}
```
