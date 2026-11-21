# 更新と復元の手順

このリポジトリの `main` 直下を GitHub Pages で公開する。公開先は https://hrkoyama.github.io/ 。作業開始時に `git status` とリモートの最新版を確認し、他の未完了変更を上書きしない。

## 通常の更新

Python 3.10以上とNode.js 22以上を使う。以下はPython標準ライブラリとNode標準機能だけで実行でき、ChatGPTやEnterpriseへの接続、推論APIキーは不要。

1. 対象の本文・データを編集する。
2. `python3 scripts/refresh-site.py` を実行する。公開用の進捗と取得案内、共通ナビゲーション、サイトマップ、研究相談索引、サイト内検索を順に更新する。
3. `node --test scripts/*.test.mjs` を実行する。`python3 scripts/check-site.py` は更新コマンド内でも実行される。
4. `python3 -m http.server 4180 --bind 127.0.0.1` で見本を開き、日本語・英語と狭い画面を確認する。終了時はサーバーを停止する。
5. `git diff --check` と差分を確認してコミットし、`git push origin main` で公開する。
6. GitHubのPages公開処理の成功後、変更したURLとダウンロード先をログアウトした状態で開き、本文・ファイル・版を確認する。

検索語や訪問者入力を集めるアクセス解析は追加しない。GitHubの通常の配信記録は別。Googleの反映・検索順位は公開完了と区別する。

## 編集する正本

- トップと共通案内：`index.html`、`using/index.html`、`using/citations.json`。
- 共通のナビゲーション・言語・方針表示：`scripts/site-chrome.mjs`、`site.js`、`site.css`。
- 熱的不安定性の公開作業記録の正本：`catalog/thermal-work-queue.json`。公開用の `the-art-of-thermal-instability/work-queue.json` も同じ正本から生成する。状態は実装・検証・公開を確認して変更する。`progress.html` と `code-and-data.html` は `scripts/build-public-resources.py` で生成する。
- 計算科学政策：`hpci-policy/` の各JSONと既存ビルダー。READMEの分野別手順を参照する。
- 検索と研究相談：生成済み索引を直接編集せず、公開本文を更新して再生成する。
- 取り込み元と対象版：`research-imports.json`、`astronomy-import.json`。元の教材ソースは非公開で保持する。READMEの取り込み手順の後にも `refresh-site.py` を実行する。

## 資料の見せ方・読みやすさ

ホームの正本は `index.html` の日英2区画と `styles/home.css`。教材・研究資料、資料・記録、調べる道具、研究者情報の順で案内する。リンク先、言語の注記、実物の図は公開済みのものを使う。

2026年11月22日の表示整理では、HPCI固有ページの構成・見出し・スタイルを保持した。教材本文は16px前後、重要な操作は14px以上・押しやすい大きさ、二次情報は12〜13px以上を目安とする。図の中の文字や数式は通常本文と分けて確認する。大学ノートの原本画像・PDF・公開対象・未確認情報を表示整理のために変更しない。

天文学教材の公開側の `app.js` とCSS、日英の発展編目次、熱的不安定性の `index.html` と `home.css` には公開先での表示改善がある。教材を再取り込みするときは、先にこれらの差分を上流へ取り込むか、Gitで保持した公開側の変更を再適用し、章URL・既存の節リンク・読了保存・文献を照合する。通常の `refresh-site.py` はこの表示変更を保持する。

各資料のCSS/JSを変更した後は通常のrefreshを実行する。`build-site-chrome.mjs` が閲覧用資産の内容ハッシュを参照URLへ付け、古い表示がブラウザに残るのを避ける。HPCI・アトラス本体・不変のコード配布版はこの追加処理の対象にしない。ノートの公開manifestはHTML/CSS/JSの変更だけを照合して更新する。

資料の追加時は、出典・単位・境界条件・実装状況・制約・利用条件を添える。大学ノートの非公開原本、マスク前画像、個人情報、第三者論文PDF、アカウント情報を取り込まない。ノートの画像・PDFの変更には既存の個別確認が必要。

## 大学ノートと非公開資料の対応

公開用の正本は `notebooks/material-links.json` と `notebooks/bibliography.json`。対応には講義・演習、同じ原本への添付、参考記事の区別を残し、確認済みの関係だけを掲載する。詳細な照合根拠と全文OCRは公開リポジトリへ含めない。`catalog.js` の `related_materials` と目録の戻りリンクは同じ対応に揃える。講師名と資料の著者・提出先の役割を区別し、姓のみや年の仮入力を保持する。

`scripts/build-notebook-bibliography.py` は公開済みの書誌JSON・対応JSON・catalogだけから目録カードと戻りリンクを再生成する。通常のrefreshにも含む。一つのスキャンに複数の課題・年度・著者の資料が含まれる場合は目録項目を分け、原本への添付と同じ講義での利用を区別する。資料の刊行年や試験年度だけでノートの受講年・講師を補わない。

`python3 scripts/check-notebook-material-links.py` が公開項目、対応の相互整合、既存の除外、講師表記を検査する。資料の本文・画像・PDFを追加せず、公開済みノート画像のマスクとページ選択を保持する。書誌JSONと新しい対応JSONのmanifestだけを確認して更新し、通常のrefreshでHTML・CSS・JSと全体検索の版を揃える。

## 公開前の自動確認

`.github/workflows/site-checks.yml` はpushとPRで、ローカル参照、サイトマップ、研究相談と検索索引の鮮度、代表ダウンロード、既存の動作検査を実行する。外部URLの一時的な障害やGoogle登録状況を成功扱いにする検査ではない。科学計算の全面再実行も行わない。

## バックアップと復元

公開Git履歴を含む控えは、作業コピーの外に `git bundle create ../hrkoyama-site.bundle --all` で保存し、`git bundle verify ../hrkoyama-site.bundle` で読み取り確認する。別の場所へ `git clone ../hrkoyama-site.bundle restored-site` で復元し、上記の静的検査を実行できる。バックアップには非公開の教材編集元を自動では含めない。教材元・書籍原稿はそれぞれの非公開リポジトリと保管先も保持する。

公開の取り消しは対象コミットの `git revert <commit>` で内容を確認し、検査後にpushする。共有した履歴を強制上書きしたり旧リポジトリを再公開したりしない。通常のGitとGitHubの権限があれば、このチャットやEnterprise環境なしで編集・復元・公開できる。

## 検索登録

Google Search Consoleの対象プロパティは `https://hrkoyama.github.io/`。`google0b2aef3d9ae4b856.html` は所有確認に必要なので保持する。サイトマップは `https://hrkoyama.github.io/sitemap.xml`。所有確認済み・サイトマップ送信済み・取得成功・ページのインデックス登録済みは別々に確認する。再送信だけで登録完了と記録しない。

## 数値計算アトラスの手法情報とコード版

手法情報の正本は `catalog/atlas-methods.json`。`scripts/build-atlas-resources.py` が手法一覧と個別のHTML・JSON・Markdown、取得案内を生成する。予定項目にコードや検証済み状態を付けない。関連コードの割当てが章単位か手法単位かを区別し、単位・境界等の未整理はnullと確認範囲で明示する。英語しかない解説は英語のURLへ案内する。

手法一覧の絞り込みは同じ生成処理が出す143項目に `atlas-methods.mjs` と一覧専用の `styles/atlas-methods.css` を適用する。状態は正本の教育用例91・解説のみ17・収録予定35を維持し、比較解説の有無で格上げしない。日英の名称・別名・分野・概要・状態ラベルを両言語で検索でき、空白区切りの全語と選択状態を組み合わせる。検索条件はタブ内のsessionStorageで引き継ぎ、URLや科学計算の台帳・検証記録を書き換えない。保存を拒否されても動作し、JavaScriptなしでは全項目を読める。`scripts/atlas-method-filters.test.mjs` が実生成HTMLと正本の一致、日英同期・日本語入力・件数・リセット等を確認する。

収録方針は同じ台帳の `editorial_policy` を正本とする。数理的な手法・定式化・適用条件・検証を中心に扱い、AMR・並列化・mixed precisionなどの計算効率化・実装上の技巧は独立した収録・開発の対象から外す。通常の丸め誤差と数値安定性は基礎に含む。除外したAMRを予定項目として復活させない。

アトラス冒頭の日英の目的説明は `catalog/atlas-purpose.json`。`build-atlas-purpose.py` が取り込み後の動的ホームと静的本文に適用し、収録方針をロードマップにも反映する。`build-atlas-search.py` は既存章に公開手法台帳を加え、アトラス内の検索も更新する。サーモスタット比較は台帳の `thermostats` 群から `build-thermostat-reading.py` で生成する。比較解説を公開済みでも、専用コードと検証結果が揃うまでは `planned` のままにする。これらはすべて `refresh-site.py` に含まれ、教材の再取り込み後にも再生成できる。

冒頭の8分野の地図は `numerical-methods-atlas/home-overview-data.js` と `locales/messages.json` を正本にする。`home-overview.js` の共通描画を `scripts/render-atlas-home-map.mjs` でも呼び、全分野を読める日英の静的本文を目的説明の生成処理へ渡す。量子化学は水素型・球対称Heの限定した実行例と一般の分子・周期系の解説を区別し、温度制御とEwald/PME/SPMEに未公開の実装を表示しない。ホーム用の文言・地図データ・CSSの変更時には生成処理で表示用ファイルの版も更新する。

紹介・共有用素材は `catalog/atlas-sharing.json` と `scripts/build-atlas-sharing.py` から生成する。`numerical-methods-atlas/share/` に日英の短文、説明文、SVG/PNGと取得案内を公開し、`share/ja/`・`share/en/` は言語ごとの共有プレビューを持つ。素材の生成方法・フォント・依存関係は同じフォルダの案内に残す。メインページの説明・OG/Twitter画像は `build-atlas-purpose.py` で更新する。外部投稿や送信は行わず、素材の公開とその利用条件の案内までを整備範囲にする。15実行例と全60問題、108既存項目と予定を含む143レコードを混同せず、AIの外部検索・学習への採用を保証する文言や新しい一括ライセンスを追加しない。

人向けの入口は文字・数式・絵の3つ。入口の文言も `catalog/atlas-purpose.json`、数式一覧の代表形と解説先は `catalog/atlas-equations.json` を編集する。数式一覧は `build-atlas-equations.py` で生成する。冒頭の数値は取り込み済み `coverage.json` の定義に従う。学術論文数を一次論文数と呼ばず、波形テスト数を全サイトのテスト問題総数や自動検査件数と混同しない。掲載する数式の行数と方程式・モデルの種類数も区別する。

量子化学・DFTの正本は `catalog/atlas-quantum.json`。`build-atlas-quantum.py` が日英の導入、式、一次文献、収録数・ロードマップを更新する。水素型原子・Heの2問題群は固定入力で実行し、原子計算版の23検査と独立したPySCF/Libxc参照で確認済み。6手法・3モデルの状態を、この限定した範囲で実行例ありにする。他の量子手法・時間依存KS・予定するH₂・周期系は未実装のまま、計画を実行例に加算しない。テスト台帳と画像一覧は全60問題。文献はDOIで重複を除き、既存の公開コード版と元の検証記録は変更しない。基底・格子・SCFの数値誤差と物理近似の誤差、交換のみLDAと相関を含むLDA、局所KSと一般化KS、有限基底FCIと連続空間の厳密解を区別する。

原子計算の正本は `catalog/atlas-quantum-examples.json` と別系列の `code/quantum-atoms/<edition>/`。同梱 `run.py` と `reference_pyscf.py` は別実装であり、参照側に教育用コードの関数を流用しない。PySCFの交換のみ汎関数は `LDA_X,` と明示する。有限格子値・h²外挿の推定・有限基底の独立参照値を別々に表示する。新しい原子計算版は必要な依存関係を用意したPythonで `scripts/package-quantum-atoms.py --edition YYYY-MM-DD` を実行する。このコマンドはZIPを別フォルダへ展開し、検査と固定入力全計算・画像生成を実行して、ハッシュと実際の結果を記録する。公開済みZIPは上書きできない。`build-quantum-examples.py` は通常の更新時にその記録と全ファイルのハッシュを確認して日英HTML/JSONを生成し、計算は再実行しない。関連する6手法の `quantum_examples` を別系列コードへ結び、旧版の `code_modules` に混ぜない。

公開済みの実行例を結ぶ正本は `catalog/atlas-execution-examples.json`。代表15問題（既存3例＋追加12例）について、例ID・対応する手法/問題・版・入力・実行場所・依存関係・コマンド・出力・数値検査・失敗判定・引用・既存の利用条件を記録する。`build-atlas-execution-examples.py` が不変な配布物と入力/参照結果のハッシュ、保存結果が受入条件を満たすことを確認し、`numerical-methods-atlas/code-and-data/examples.json` を生成する。`build-atlas-execution-guide.py` はこの情報から日英の取得・実行案内を生成する。方法/問題のJSONと原子計算の章も同じ実行例へリンクする。例を追加しても独立問題数や実装済み手法数を自動では増やさない。

共通手順の実行確認には、依存関係を導入済みのPythonを指定し、`python scripts/verify-atlas-execution-examples.py --python /path/to/python --output report.json` を使う。通常は公開registry、ZIP、入力、参照をHTTPSで取得し、安全に別の一時フォルダへ展開する。プログラム終了と数値条件の合格を別に記録し、新しいJSON/CSVのハッシュも残す。水素型原子とHeは同じrunnerの1回の実行を共有する。初公開前のみ `--registry catalog/atlas-execution-examples.json` を指定できる。この場合も科学計算のファイルは全て公開URLから取得し、どの入力経路かをレポートに記す。依存関係を自動でインストールしない。配布版の全自動検査や独立PySCF参照の再生成とは別の実行確認である。

追加12問題の固定入力は `code/numerical-methods-atlas/2026-11-22/recipes/*.json`、共通入口は同梱 `run_recipe.py`。同じフォルダの3モジュールが既存Numartを呼び、解析解・細格子の数値参照・保存則・独立に計算した残差などを評価する。Numart本体は2026-11-21版と同一のまま、旧配布版を上書きしない。各入力は刻み・境界・モデル規約・受入条件を含み、`result.json` に入力ハッシュ・実測値・各合否、`solution.csv` に解と参照を記録する。新規/空の出力先だけを許可し、終了コード0=数値条件合格、1=未達、2=入力/計算エラーとする。Shu–Osher/Brio–Wuの細格子比較を厳密解や別実装の独立参照と呼ばない。旧版411検査と新版432検査は重複を含む版別件数で、合算しない。

`verify-code-edition.py` はZIPを独立展開して自動検査を実行し、`run_recipe.py` があれば同梱全入力も実行して結果・CSV・入力ハッシュを検査する。公開用registryの再実行記録は段階を区別し、初回のローカル台帳＋公開配布物は `2026-11-22.json`、公開registryからの追試は `2026-11-22-public.json`。後者が存在すると案内ページは同じregistryハッシュを検証してそちらを表示する。過去の記録は書き換えない。

15問題を文字・数式・保存図から探す対応は `catalog/atlas-execution-discovery.json` が正本。`atlas_execution_discovery.py` が既存実行台帳とのID集合・問題ID・日英説明・数式・実装状態を照合する。検索語はその固定入力で実行するモデル/手法に限定し、Heの球対称閉殻HF・交換のみLDAをPBE/SCAN/UHF等の実行例として索引化しない。補間・硬いODE等の専用式を46モデルの追加として数えず、未実装モデルへ実行可能のラベルを付けない。

`build-atlas-execution-entries.py` が15専用ページと短い入口一覧を生成する。各専用ページには同じ実行条件・入力/ZIP・JSON/CSV・判定条件・公開再実行記録と、個別JSON/Markdownがある。Markdownの配列判定はpointerだけでなくwhereとfieldも必ず残す。元の共通実行台帳や公開済み検証記録のバイト列を入口整備のために変えず、対応表の方へ関連を追加する。検索は実行意図付きの具体例を優先し、ギャラリーは全60件を初期表示して15実行例に絞れる。画像が新入力の出力であるとの未確認の主張はしない。図の元説明・条件/根拠・解説への別リンクを保つ。

通常のrefreshは専用入口を生成してから、式・ギャラリー・検索・ホームを更新する。ルートサイトマップと全体検索にも専用ページを含める。一方、既存のLLM用読書パックは読書章と熱的不安定性の元の範囲を保持し、250件の上限は索引対象の読書資料に適用する。新しい非読書ルートの追加だけで読書パックの範囲を広げない。

公開用の追加実行記録は `numerical-methods-atlas/code-and-data/verification/` に保存し、台帳の `verification_receipt` を対応するURLにする。registryの内容と記録内のSHA-256が一致することを生成時に確認する。通常のrefreshは保存済み記録を参照し、ネット取得や科学計算を繰り返さない。レシピを変えた場合は記録を取り直し、古い記録を新しい条件の成功と表示しない。コードのMIT、入力・数値データ・図・本文の個別条件、第三者資料の条件は別のまま保持する。

公開15例のLinux継続検証は `.github/workflows/atlas-public-linux.yml`。Ubuntu 24.04 / Python 3.12の新しいジョブで、ソースcheckoutや依存キャッシュを使わず、公開URLから取得する `scripts/run-atlas-public-ci.py`・verifier・registry builder・実行台帳をSHA-256で固定する。`update-atlas-ci-pins.py` は通常refresh内でこの4つの期待値を更新するため、ツールや台帳を変更したらPagesの公開成功後にCIを実行する。公開manifestでrequirementsを照合し、新規venvへ固定依存を導入してから、公開ZIP・入力・参照だけで15例を14コマンド実行する。原子2例は同じrunnerを共有する。PySCF参照の再生成、全60問題、配布版pytest全件とは別の検証として記録する。

実行契機は手動・毎週月曜12:17（日本時間）・mainのPublic site checks成功後。公開ツールと台帳のSHA-256が揃うまで最大240秒待ってから実行する。CIの権限は読み取りだけで、サイトへの自動commitは行わない。通常の取得・依存導入・実行・数値判定の失敗でも、段階・環境・ハッシュ・ログ・生成JSON/CSVをActions成果物として90日保持する。`verify-atlas-execution-examples.py --artifacts-dir ... --expected-registry-sha256 ... --output ...` は途中の失敗も保存し、元の数値判定基準を変更しない。公開済み配布版と過去の検証記録は上書きしない。

CI案内の正本は `catalog/atlas-ci.json`、生成は `build-atlas-ci-page.py`。`numerical-methods-atlas/code-and-data/ci/` に最新状態への参照と、日付・run・registry SHAを持つ保存済み記録を分けて表示する。成功したrunのレポートを保存するときは、Actions成果物の `ci-summary.json` と `report.json` を確認し、新しい `ci/verification/` のJSONへrun URL等とともに収め、snapshotsへ追加して再生成する。古い成功記録を最新の成功と呼ばず、台帳SHAが変わった場合も履歴と現行条件を区別する。

AIの外部検索・公開情報の取得・実行・引用の実地観測は `numerical-methods-atlas/code-and-data/acceptance/YYYY-MM-DD.json` に日付付きで保存する。固定検索語・サービス・返却範囲・未発見、検索ツールのopenと通常HTTPの違い、URL提示あり試験、実行環境・生成出力・数値条件・文献の閲覧深度を別に記録する。ソースcheckoutや過去CI成功を独立AI実行の代用にせず、未発見からGoogle等の未登録を断定しない。保存記録を上書きせず、`catalog/atlas-ci.json` の `ai_acceptance_report` にURLとSHA-256を指定し、日英CI案内とllms.txtから接続する。

主要24手法の個別条件は `catalog/atlas-methods.json` の `priority_review` / `method_review` を正本とする。問題・実際の採用形・使う条件・避ける条件・単位・境界・制約を日英で記載し、`specified` / 理由付き `not-applicable` / `unknown` を区別する。原法・採用変種・定式化・参照解・背景の文献役割と、本文の該当箇所／抄録・書誌／書誌のみの確認範囲を保存する。この整理で数値検証済みの状態へ格上げしない。Ewald/PME/SPMEは実装前の比較仕様であり、重力PMの核・境界・符号と区別する。

一次文献の書誌は `catalog/atlas-method-primary-references.json` から `build-atlas-method-sources.py` が統合する。DOI・既存ID・同じ題名と年を照合し、URL別名や複数手法からの引用を重複加算しない。文献統合を量子章生成より先に実行し、全体の文献数・BibTeX・日英文献一覧を揃える。`atlas_method_review.py` は条件の欠落と状態・文献の確認範囲を検査し、HTML/Markdownと `/numerical-methods-atlas/methods/reviewed.json` へ同じ内容を出す。

現在の作業順序と専門AIを2027年以降に繰り延べる決定は `catalog/atlas-work-queue.json` が正本。専門AIや独立した基盤モデルが実装済みであると表示しない。数値検証例は実際に固定入力で計算し、独立参照・残差・収束・終了理由・コードと環境の版を記録してから台帳の状態を変更する。

数式一覧は `coverage.json` の全 `kind=equation` 項目とID・実装状態・章を完全照合する。一部だけの代表一覧へ戻さない。数式はLaTeXで保存し、同梱のKaTeXで静的HTML・MathMLにするため、新たなパッケージ取得は不要。モデル追加・章内の見出し変更時は全項目との件数一致だけでなくID集合と日英の節リンクも検査する。文献解説のみのモデルを計算例ありに変更せず、相対論や生物モデルの代表形・縮約・模式式の条件を残す。

全体のテスト問題の正本は `catalog/atlas-test-problems.json`。`build-atlas-test-problems.py` が根拠となるJSONの要素・検証関数・結果図を確認し、重複を除いた問題台帳、分野別集計、参照ファイルのハッシュを公開する。`coverage.json` と `assets/site-coverage.json` の `test_problems` はこの台帳から生成し、冒頭と収録一覧に表示する。`gallery_cases` は波形比較だけの従来の件数として残す。格子・手法・刻み・パラメータ・画像・動画の違いで同じ問題を加算しない。追加した計算例は既存問題との重複と根拠を確認して台帳に追記する。予定・参照評価のみ・局所の単体検査は別扱いとし、公開コード版の検証記録は書き換えない。

公開コードは `code/numerical-methods-atlas/<edition>/` にあり、編集可能なPython、検査、必要データ、依存関係、ライセンス、ハッシュ目録、ZIP、独立実行の検証記録を含む。公開済みの版のファイルは上書きしない。変更時は新しい版を用意し、目録・ZIP・独立実行結果を揃えてから台帳の `code_edition` と `code_base` を更新する。旧版のURLと配布物を保持する。Git履歴や未公開原稿を配布物へ含めない。

「絵から探す」は `catalog/atlas-gallery.json` を正本として、全テスト問題のIDと1対1で照合する。既存の共有図は対応するパネル・問題を説明に残す。`scripts/render-atlas-gallery.py` は保存済み数値データの図示と9問題の固定条件計算を行い、`numerical-methods-atlas/gallery/` に画像・入力値・数値検査・出典ハッシュを保存する。実行には公開コード版の依存関係（今回はNumPy 2.0.2、Matplotlib 3.9.4）が必要。追加検証の `verification.json` は実際に実行したpytestの選択項目・件数・参照ファイルのハッシュを記録する。新しい結果を元の公開コード版へ書き戻さない。通常の `refresh-site.py` は科学計算を再実行せず、保存画像と根拠のハッシュを検査して `build-atlas-gallery.py` から日英HTMLと機械可読一覧を生成する。旧 `#/gallery` は全件一覧へ案内し、従来の図版・比較ツールは `#/figures` に保持する。

新しい版のフォルダを前版から用意してコード・入力を編集し、Gitに追加する前に `python3 scripts/package-code-edition.py --edition YYYY-MM-DD` で目録とZIPを作る。必要な依存関係を一時環境に入れ、そのPythonで `scripts/verify-code-edition.py --edition YYYY-MM-DD` を実行する。これはZIPを別の一時フォルダに展開して検査し、実際の合否・環境を `verification.json` に保存する。検証スクリプトは依存関係の自動インストールや外部へのデータ送信を行わない。すでにGitに登録されたZIPは包装スクリプトで上書きできない。

研究用データを変更するときはコードMITと一括で扱わず、出典・利用条件・入力・検証範囲を確認する。`refresh-site.py` の後に全チェックを実行し、サイトマップと索引も同じ版に揃える。
