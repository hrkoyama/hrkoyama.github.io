# 更新と復元の手順

このリポジトリの `main` 直下を GitHub Pages で公開する。公開先は https://hrkoyama.github.io/ 。作業開始時に `git status` とリモートの最新版を確認し、他の未完了変更を上書きしない。

## 公開先の固定ルール

2026年11月22日のユーザー指示により、今後の公開先は **https://hrkoyama.github.io/** 配下だけとする。公開用リポジトリは **`hrkoyama/hrkoyama.github.io`**、公開ブランチは **`main`**。数値計算アトラスは `/numerical-methods-atlas/` に公開する。

**`koyamarium` 配下へ変更を反映しない。** push、PR作成・マージ、リリース、アップロード、公開・デプロイ用ワークフローの起動を行わない。上流ソースのローカル編集・検証は可能だが、上流へ push してから公開する手順は使わない。`koyamarium.github.io` と旧 `koyamahr.github.io` は公開先にしない。過去のURL・履歴の参照と、現在の公開先を区別する。

公開直前に `git remote get-url --push origin` と配信URLを照合し、実際の push 先と公開URLがこの指定に一致することを確認する。不一致なら正しい公開用作業コピーへ切り替える。公開側の独自拡張と他作業の未コミット変更を保持し、今回の変更だけを統合する。上流ビルド全体で公開サイトを置き換えない。常時適用する指示は `AGENTS.md` にも記録する。

## 通常の更新

Python 3.10以上とNode.js 22以上を使う。以下はPython標準ライブラリとNode標準機能だけで実行でき、ChatGPTやEnterpriseへの接続、推論APIキーは不要。

1. 対象の本文・データを編集する。
2. `python3 scripts/refresh-site.py` を実行する。公開用の進捗と取得案内、共通ナビゲーション、サイトマップ、研究相談索引、サイト内検索を順に更新する。
3. `node --test scripts/*.test.mjs` を実行する。`python3 scripts/check-site.py` は更新コマンド内でも実行される。
4. `python3 -m http.server 4180 --bind 127.0.0.1` で見本を開き、日本語・英語と狭い画面を確認する。終了時はサーバーを停止する。
5. `git diff --check` と差分を確認してコミットする。`git remote get-url --push origin` が `hrkoyama/hrkoyama.github.io` を指すことを確認してから、`git push origin main` で公開する。
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

公開用の正本は `notebooks/material-links.json` と `notebooks/bibliography.json`。対応には講義・演習、同じ原本への添付、参考記事、ノートに明記された参考書の区別を残し、確認済みの関係だけを掲載する。詳細な照合根拠と全文OCRは公開リポジトリへ含めない。`catalog.js` の `related_materials` と目録の戻りリンクは同じ対応に揃える。講師名と資料の著者・提出先の役割を区別し、姓のみや年の仮入力を保持する。

章立て・連続する記述の対応を確認しても、講義の同一性や担当が未解決なら `content_correspondence` として区別し、表示に「同一講義は未確認」を残す。この関係だけで講師名・受講年を補わない。N094とB092はこの区別を用い、ノート作成者が確認した杉本大一郎と、資料表記の中村卓史を併記する。

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

目的別の入口は `catalog/atlas-goals.json` が正本。`build-atlas-goals.py` が日英の静的な `/numerical-methods-atlas/start/` と共通検索用の照合データを生成する。目的は適用モデル・制約・候補手法ID・公開実行例IDを伴い、未検証の万能推奨や未公開コードのリンクを作らない。検索で認識できる代表表現を追加するときも、衝撃波と滑らかな低散逸流、相対論/MHDとEulerの範囲を混同しない。`scripts/atlas-goals.test.mjs` が両検索入口と実在するリンクを確認する。

ホーム冒頭も同じ台帳の `home` と目的の台帳から `build-atlas-purpose.py` で生成する。目的のリンクは適用条件の節へ直接進める。収録数と資料一覧はその後に置き、日英の静的本文と動的ホームの両方でこの順番を保持する。

目的の公開状況フィルターは `atlas_goal_availability.py` の `goal_flags` を共通の分類とし、`goal-filters.mjs` をホームと目的別ページで共用する。実行例ありはコードとテストありにも含める。選択値だけをタブ内のsessionStorageへ保存し、日英とページ間で引き継ぐ。直接指定された節が隠れる場合は「すべて」に戻し、一覧と詳細を同時に絞り込む。JavaScriptなしでは全目的を表示する。`scripts/goal-filters.test.mjs` が件数・分類・リセット・保存拒否・直接リンクを検査する。

目的別の公開状況は `atlas_goal_availability.py` で算出する。原子の実装を分子・周期DFTへ転用して実装済みと表示しない。温度制御の比較解説は公開済みでも実装はplannedのまま、生物モデルの読書用resourcesは手法台帳や実装数へ加算しない。生物の検証案と実行済みテストを区別する。

安定性・散逸・分散とA/L安定性の解説の正本は `catalog/atlas-stability-foundations.json`、KEEP詳説は `catalog/atlas-keep-explanation.json`。`build-atlas-stability.py` と `build-atlas-keep.py` が通常のrefresh内で同梱KaTeXを使い、日英の静的ページ・SPA本文・目次を同じ正本から生成する。追加・修正は生成HTMLだけでなく正本へ反映し、既存の節IDと章間リンクを保持する。

手法情報の正本は `catalog/atlas-methods.json`。`scripts/build-atlas-resources.py` が手法一覧と個別のHTML・JSON・Markdown、取得案内を生成する。予定項目にコードや検証済み状態を付けない。関連コードの割当てが章単位か手法単位かを区別し、単位・境界等の未整理はnullと確認範囲で明示する。英語しかない解説は英語のURLへ案内する。

手法検索の名称・別名も同じ台帳の `name`・`aliases` を正本にする。`scripts/atlas_search_methods.py` が公開済みの解説・コード・テスト・個別実行例だけを検索へ渡し、`search/method-search.mjs` を全体検索とアトラス内検索で共用する。手法名の一致を一つのカードへまとめ、本文中の言及は関連資料へ折りたたむ。具体的な問題名に実行・コード等を添えた検索では、対応する公開実行例を展開して先頭に置く。アトラスからの共通検索は `scope=atlas` を初期範囲とし、検索語はURLフラグメントとブラウザ内だけで扱う。全143手法のID・日英名・別名、略語の誤一致、公開状況と直接リンクは `scripts/method-search.test.mjs` と `scripts/atlas-search-methods.test.mjs` で確認する。

手法一覧の絞り込みは同じ生成処理が出す143項目に `atlas-methods.mjs` と一覧専用の `styles/atlas-methods.css` を適用する。状態は正本の教育用例93・解説のみ17・収録予定33を維持し、比較解説の有無で格上げしない。日英の名称・別名・分野・概要・状態ラベルを両言語で検索でき、空白区切りの全語と選択状態を組み合わせる。検索条件はタブ内のsessionStorageで引き継ぎ、URLや科学計算の台帳・検証記録を書き換えない。保存を拒否されても動作し、JavaScriptなしでは全項目を読める。`scripts/atlas-method-filters.test.mjs` が実生成HTMLと正本の一致、日英同期・日本語入力・件数・リセット等を確認する。

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

「目的から探す」の分野は `catalog/atlas-goals.json` の `domains` と各目的の `domains` を正本とする。MHDのように分野が重なる目的は複数に分類し、目的の適用範囲を越えて汎用手法の分野を借用しない。ホームと目的一覧は同じ `goal-filters.mjs` で分野・公開状況の両条件を適用する。選択はタブ内で日英・ページ間に引き継ぎ、リセットと非表示の目的への直接リンクでは両条件を解除する。分野追加時は日英名・所属先・組み合わせ結果・重複しない件数を `goal-filters.test.mjs` で確認する。

目的フィルターの共有条件はURLクエリ `goal-domain` / `goal-availability` に保存する。どちらかがあればURLを優先し、省略側・不正値は `all` にする。両方なければ従来のタブ内選択を読み、`all` も含めた両条件をURLへ明示する。選択・リセットは履歴へ追加し、戻る／進む・BFCache復元ではそのURLの状態を復元する。日英・ホーム・目的一覧へのリンクにだけ同じ条件を渡し、既存のlang・他のクエリ・適用可能なアンカーを保持する。検索語などの入力をクエリへ追加しない。

目的フィルターの「共有リンクをコピー」は現在のURL・正規化した両条件・表示言語をクリック時に組み立て、Clipboard APIへ書き込む。成功・失敗は日英のライブ領域へ表示し、API非対応／拒否時は読取専用の共有URLを表示して手動コピーできるようにする。条件変更や履歴復元後に古い成功表示を残さず、コピー待機中の変更から古い結果を表示しない。クリップボードの既存内容は読み取らない。

23件の予定手法の詳細解説、基底関数の日英本文、回転Riemann法の出典整理は `catalog/atlas-detailed-reading.json` が正本。`build-atlas-detailed-reading.py` を文献統合の後・量子章の収録数再集計の前に実行し、静的日英HTML・JSON/Markdown・SPA本文・翻訳状況・章目次・検索入口を生成する。解説だけの追加で143手法の実装状態、公開配布版、過去の数値検証記録を変更しない。本文中の検証案と測定結果を区別する。引用はDOI・題名/年で重複を除き、原著・著者の著書・概説・公式参照資料と実際の閲覧範囲を明示する。回転法のRen（2003）、Roe・西川ら（2005）の関連研究、西川・北村（2008）のrotated-hybrid、アトラスの明示的HLLE/Roe教育用実験を同じものとしない。

同じ詳細解説の正本に、Weiss–Smith型の理想気体Γ、低Machの線形固有値モデル、淀み点カットオフと遷音速エントロピー修正、および定常Jameson系多段RKの解説を収める。可逆な前処理で物理的な零固有値が消えると説明せず、特異値条件数と固有値速度比を区別する。基準状態型4段式の線形安定性多項式と、一般非線形の次数を混同しない。これらの章の追加で新しい専用ソルバーや手法件数を計上しない。

## 分野ごとの実装・検証の深さ（2026-11-22）

項目拡張より、既存分野の検証差を埋める。正本は `catalog/atlas-depth.json`、生成は `scripts/build-atlas-depth.py`、ホームの共通導入は `scripts/atlas_depth.py`。日英で解説・専用コード・固定入力の追試・参照種別・収束確認と未実装範囲を示す。百分率や分野全体の認証を付けず、細格子の同じ実装を独立参照と呼ばない。

生物・確率の初回追加段階では手法143レコード（教育用例93・解説のみ17・実装予定33）、計算例または解説あり110項目、全64問題、共通19実行例。上の15例／60問題は先行公開時点の履歴として読む。原子と分子・周期DFT、閉鎖SIRとSEIR、IID積分とMCMCを混同しない。原子の数値検証は維持し、一般量子化学は未実装のまま。

生物・確率の4例は別系列 `code/model-benchmarks/2026-11-22/`。編集用の正本は `scripts/domain-benchmarks/`。`package-domain-benchmarks.py --edition YYYY-MM-DD[-rN]` を固定依存を導入したPythonで実行すると、新版を作り、SIRの独立DOP853参照・全入力・結果図を生成し、ZIPを独立展開して11検査と全入力を再実行する。既存版は上書きしない。Monte Carloは固定した256 seedの標本誤差・区間被覆、SDEは同じBrown経路を共有した強誤差と4段階の刻みを測る。統計的な許容条件は入力で事前固定し、全seedでの保証や弱収束次数の実測を主張しない。

共通台帳に4例を統合し、`2026-11-22-domains.json` はローカル台帳＋公開ZIP、`2026-11-22-domains-public.json` は公開レジストリから19例／18 runnerを実行した別記録。旧記録は保持する。Linux CIも4配布版・19例／18 runnerへ更新するが、旧15例の保存済みLinux成功を現行条件の成功と表示しない。`model_examples` は専用配布版からコード・テストを解決し、旧Numartへ架空のモジュールを割り当てない。

## H₂分子RHF（2026-11-22）

H₂の編集用コードは `scripts/h2-hf/`、不変配布版は `code/molecular-hf/2026-11-22/`。`scripts/package-molecular-hf.py --edition YYYY-MM-DD[-rN]` は独立PySCF参照の生成・全入力・図を作り、ZIPを独立展開して20検査と全入力を再実行する。公開版は上書きしない。PySCFは参照側だけで使い、教育用の積分・SCFをPySCFへ委譲しない。固定条件は核間距離0.8/1.4/3 bohr、STO-3Gと2〜8個/Hの入れ子s型Gaussian。24点とSCF公差3点を、独立した問題数24/27として加算しない。H₂は1問題・1実行例であり手法143レコードは増やさない。

日英本文の正本は `catalog/atlas-h2-reading.json`、生成は `scripts/build-atlas-h2.py`。独立参照差、直交化した交換子のFrobeniusノルム、SCF反復履歴、公差走査と基底の隣接エネルギー差を実測JSONから表示する。末尾2回のdiffuse/tight追加がともに1 mEh以下という有限s型部分空間の条件を示す。単調低下だけを収束とせず、完全基底極限・角運動量収束・正しい解離極限・相関の検証を主張しない。STO-3G係数はBSE v1の数値規約を出典とし、1969年論文の印刷値の転記と呼ばない。

`molecular_examples` をHF・SCF・電子基底に付け、原子の `quantum_examples` と既存のコード・入力・参照を保持する。分子RHFの専用目的を追加しても、分子DFT・周期DFTのreading-only状態へコードを貸さない。実行台帳は20例、全問題65、量子3問題群、手法状態94教育用例・16解説のみ・33予定。旧19例の検証記録はそのまま保持する。`2026-11-22-h2.json` は公開レジストリ由来の20例/19runnerの記録。専用入口ビルダーは-public版があれば優先し、なければ指定記録を使うが、どちらもpublic-registryかつ成功という条件を必須にする。

H₂の次の量子計算の優先は周期KS-DFT。小さな中性絶縁体セルから、Bloch条件・逆格子・k点和とメッシュ、基底/補助格子、SCFを別に収束させる。擬ポテンシャル・XC・単位と独立参照をそろえる。金属・smearingは後続とし、周期DFTを実装前に実行例ありへ変更しない。

## 周期HeのKS-LDA（2026-11-22）

現行は21実行例・全66問題・量子4問題群、手法145レコード（教育用例96・解説のみ16・予定33）。CPMDとBOMDの2項目は原著と日英比較解説のみで、MDのコード・力・軌道の検証を加算しない。上記の15／19／20例は各公開段階の記録として保持する。新しい周期例の正本は `scripts/periodic-dft/`、不変配布版は `code/periodic-dft/2026-11-22/`、日英本文は `catalog/atlas-periodic-reading.json` と `scripts/build-atlas-periodic.py`。既存の原子・H₂版は上書きしない。

周期例は格子定数4 bohrの固定1原子単純立方Heセル・価電子2・非偏極LDA_X＋LDA_C_VWN（VWN5）・局所GTH。自作部分はPySCFによる実行・検証ワークフローであり、自作DFTエンジンとは表示しない。Γ／2³／3³／4³メッシュ、Gaussian軌道基底、FFT補助格子、SCF公差を11個の設定で別々に調べる。同じモデル・GTH係数・汎関数のDFTK平面波計算を別に実行し、Γ／2³の全エネルギーを比較する。60／90／120／180／240 Haの打切り走査とJulia環境・入力・出典・ハッシュを配布する。参照側の再生成は通常のPython CIとは別操作。

`python scripts/package-periodic-dft.py --edition YYYY-MM-DD[-rN]` は正本に用意した固定入力の計算結果・図を新しい版へ取り込み、ZIPの独立展開・テストと全入力の再実行を検査する。Python依存はNumPy／SciPy／Matplotlib／pytest／PySCFの固定5版。共通Linux検証は6配布版・21例／20 runner、各runnerの上限900秒。公開レジストリから再実行した記録は `2026-11-22-periodic.json`。過去の検証記録を新しい台帳の成功として扱わない。

Gaussian軌道基底とFFT補助格子、DFTKの平面波打切りを同じ「基底」として混同しない。有限差分の経験的な目安は完全基底極限の厳密誤差上界ではない。独立照合はセル当たり全エネルギーに対するもので、仮想バンド全体の一致や大域的・基本ギャップを保証しない。標本k点で正のKSギャップを示す教育用の固定モデルであり、平衡He結晶、他元素、金属、一般分子DFTを検証済みにしない。自作コードMITと外部ライブラリ・基底／擬ポテンシャルデータの個別条件を保持する。

## 分野をつなぐ入口（2026-11-22）

正本は `catalog/atlas-crossovers.json`、生成は `scripts/build-atlas-crossovers.py` と共通ヘルパー `scripts/atlas_crossovers.py`。`/numerical-methods-atlas/connections/` に日英の経路・段階・接続ごとの受け渡す量、共通数理、異なる条件、追加の検証、既存の要素例を示す。ホームの目的選択直後に3つの経路を置き、目的ページ・検証範囲ページと検索にも接続する。

DFTから力・第一原理MD・温度制御、反応拡散から生物・流体、Poissonから圧力・Hartree・重力をたどる。汎用手法の実装状態を、その用途全体へ自動適用しない。段階の明示した実行例と `example_role`、手法台帳の状態、接続全体の `coupled_validation` を区別する。今回はすべての分野間接続が未実行であり、固定Heの全エネルギー、0次元反応ODE、移流、Poisson、Taylor–Green等の既存例で連成全体を検証済みにしない。MDの力・軌道、温度制御の分布、空間反応拡散を新しく実装したとは表示しない。

共通数理の絞り込みは `crossovers.mjs` の追加機能で、JavaScriptなしでもすべて読める。`math` クエリで条件を共有し、不正値・リセット・戻る／進むと直接節リンクを扱う。言語切替で経路の節と条件を保ち、読者の検索語や選択を外部へ送信しない。引用は既存の一次文献と確認範囲を掲載し、新しい手法・方程式・問題・論文数の加算にしない。通常refreshとNode検査、日英・390px表示を確認して公開する。コード配布版・入力・参照・数値判定・公開21例の実行台帳は変更せず、案内の変更だけで科学計算を再実行しない。

接続の意味は `connection_kind` で、量の受け渡し・モデル適用・要素例の参照・共通演算子の対応を区別する。Poissonの対応図は圧力・Hartree・重力を一つのソルバーへ連成する計画ではない。既存の圧力投影や周期DFT等の成功は各固定例の範囲で保持し、境界・符号・物理量を越えた精度保証として移さない。接続図は正本のfrom/toを使い、反応拡散とPoissonの分岐を架空の逐次計算へ変更しない。

## 自動微分の共通基盤とBratu検証

`automatic-differentiation` の正本は既存の `catalog/atlas-detailed-reading.json` と `catalog/atlas-methods.json`。前進モードの教育用実装だけを実装済みとし、逆モード・陰関数感度・随伴法の説明と実行検証を区別する。既存の章URLと節IDを保持する。

専用の不変配布版は `/code/autodiff/2026-11-22/`。旧コード版は上書きしない。`scripts/package-autodiff.py` が明示した公開ソースだけを梱包し、8件のテスト、manifest、ZIPとBratuの測定記録を残す。`build-atlas-autodiff.py` が専用版の図・JSONをアトラスへ配置し、疎行列・陰的積分・ロードマップへつなぐ。通常の `refresh-site.py` で本文・手法台帳・検索・ホームへの導線を再生成する。この補助比較を共通実行台帳・テスト問題の件数へ加算しない。

## 多原子DFTの原子間力（2026-11-22）

原子間力は `scripts/periodic-forces/` と新しい不変配布版 `code/periodic-forces/2026-11-22/` に分離する。既存の1原子周期DFT版・参照値・配布ZIPは上書きしない。正本本文は `catalog/atlas-forces-reading.json`、生成は `scripts/build-atlas-forces.py`。非対称なHe₂・5 bohr立方セル・4価電子・局所GTH・LDA交換＋VWN5を固定し、PySCF解析力（原子中心Gaussian基底の微分・イオン項を含む）を全6座標の中心エネルギー有限差分とDFTKの独立平面波力で照合する。変位幅、Gaussian軌道基底、k点、FFT補助格子、SCF公差、参照側の平面波打切りを別系列で記録する。各末尾差は経験的な停止目安で、真の誤差上界ではない。

BOMDの力供給APIとvelocity-Verletの1ステップ対2半ステップは局所的な接続の確認に限定する。原子間力を実装したことを、長時間NVE軌道、温度制御、一般物質・非局所擬ポテンシャル・応力・金属・CPMDの検証へ移さない。BOMD/CPMDの手法状態はreading-onlyのまま保持し、`force_examples` と `force_scope` は力を実際に用いたKS/基底/SCF/XC/擬ポテンシャル/k点の6手法へだけ付ける。

共通実行台帳は22例・7配布版・21 runner、全問題は67。別のAD・Bratu感度・Bratu逆問題の補助配布版をこの共通台帳へ加算しない。現行の手法145レコード（教育用99・解説のみ16・予定30）はAD・随伴法・限定した逆問題実装の追加後の状態を引き継ぎ、力例で手法数・状態件数を増やさない。再実行時間を確保するため、共通runnerの上限は3600秒、Linuxジョブは90分。過去の21例・66問題等は当時の版の記録として保持する。公開前の検証は、コードと最終台帳と同一バイト列の候補を `code/periodic-forces/verification-candidates/` に先に公開して実行できる。候補取得URL・SHAを追試記録へ明示し、最終の正規台帳と完全一致する場合だけ同じ成功記録を使う。これにより既存の公開台帳・件数を、未検証の候補へ途中で切り替えない。

クロスオーバーの力段階は専用固定例に限って実行済みとする。DFT→力はfixed-input、力→MDはinterface-onlyで、各接続に成功した力例の公開追試記録を必須とする。経路全体・長時間MD・温度制御のnot-executed状態は保持する。Feynmanの力の原論文、Pulayの解析微分、BOMDのSCFと保存性に関する一次論文を、抄録・書誌／公式実装の確認範囲とともに日英で引用する。

公開ファイル追試の初回は保存領域のENOSPCで20例の完了後に停止した。未公開だった失敗記録は内容を変更せず `2026-11-22-forces-enospc.json` へ名前を付けて保持し、保存先の書き込み確認後、同じ公開台帳・配布物で全22例を新規実行し直す。途中の成功を未実行の周期2例へ流用しない。

再起動後は空き容量16 GiBを確認し、同じ公開候補台帳から全22例／21 runnerを新規実行して成功した。成功記録は `2026-11-22-forces.json`。候補台帳と正規台帳のバイト列・SHA-256が一致することも確認した。再起動準備で止めた2回目の記録は `2026-11-22-forces-interrupted-reboot.json` として保持し、成功記録とは区別する。

## Bratuの陰関数感度と離散随伴

`catalog/atlas-detailed-reading.json` の `adjoint` 章と `catalog/atlas-methods.json` が正本。既存の章URL・節IDを保持し、一般の逆問題最適化や時間依存随伴を実装済みと表示しない。新しい不変配布版 `/code/bratu-sensitivity/2026-11-22/` は、解析的な連続感度、陰関数感度、離散随伴勾配、パラメータを変えて解き直した有限差分を照合する。Bratuの対称性だけに頼らず、非対称・複数パラメータの独立した転置検査を含める。

`atlas_sensitivity_release.py` が配布ファイル・ZIP・検証記録のハッシュを照合し、`build-atlas-autodiff.py` が図・JSONと章間リンクを配置する。古い自動微分配布版は上書きしない。通常の `refresh-site.py` で本文・手法台帳・検索・ホームを再生成する。この補助比較を共通実行台帳・テスト問題の件数へ加算しない。

## Bratuの合成観測による逆問題

`catalog/atlas-detailed-reading.json` の `bratu-inverse` が日英解説の正本。既存の `optimization` 手法項目を、区間制約付きの1パラメータ推定だけの教育用実装へ昇格する。従来の `/read/optimization/` と節IDは残す。準Newton法全般を実装済みとしない。感度解析の既存章・不変配布版も保持する。

新しい不変配布版は `/code/bratu-inverse/2026-11-22/`。観測位置・重み・真値・固定ノイズを保存し、離散随伴勾配を使った射影勾配法とArmijo線探索でλを推定する。同じ離散モデルの合成データによる回復はコード整合性の検査に限定し、連続解析解の固定観測を用いた格子細分化と固定ノイズによる推定値のずれを別々に示す。目的関数だけを使う独立した区間探索、解き直した有限差分、接線感度で照合する。収束判定、パラメータ誤差、主問題・随伴残差を区別し、実測データや統計的信頼区間の検証を主張しない。

`scripts/package-bratu-inverse.py` はZIPを独立展開して検査・結果再生成を行い、目録と検証記録を作る。`scripts/atlas_inverse_release.py` が配布ファイル・ZIP・記録のハッシュを照合する。図とJSONの配置は `build-atlas-autodiff.py`、本文・手法・検索・ホームの再生成は通常の `refresh-site.py` に従う。共通実行例22件・固有テスト問題67件には加算しない。公開は本書冒頭と `AGENTS.md` のとおり `hrkoyama/hrkoyama.github.io` の `main` だけへ行う。

## 2次元TMzのYee FDTD（2026-11-22）

編集用コードは `scripts/fdtd/`、不変配布版は `code/fdtd/2026-11-22/`。`scripts/package-fdtd.py --edition YYYY-MM-DD[-rN]` は2入力の計算・図・CSVを保存し、ZIPを別フォルダへ独立展開して全テストと両入力を再実行する。数値指標・CSVの一致、入力・ソース・配布物のSHA-256を検査し、既存版は上書きしない。Python 3.12と同梱requirementsの固定版を使う。

日英の本文・数式・実測値は既存の `catalog/atlas-detailed-reading.json` の `fdtd` が正本。旧章URLとmodel/algorithm/conditions/verification節を保持する。`atlas_fdtd_release.py` が配布物と成功記録を照合し、`build-atlas-fdtd.py` が保存図を配置する。通常のrefreshで解説・手法・検索・索引を更新する。FDTDは専用配布版を持つ教育用例へ変更するが、旧コード版のcode_modules/test_filesへ架空の実装を割り当てない。

対象は無次元・一様真空・源なしの2次元TMz（Ez,Hx,Hy）。斜めの周期波と長方形PEC空洞を、格子16×24、32×48、64×96、Courant数0.7で検証する。連続解析解との誤差と格子/時間の同時細分化、離散分散関係との一致、12周期の修正離散エネルギー保存と同時刻へ補間した物理エネルギーの誤差を区別する。連続場を格子へサンプルした際の初期磁場発散が厳密にゼロとは限らないため、発散の初期値からの保存を測る。

この2例は既存の共通実行台帳22例・全問題67件とは別の補助配布版として案内し、それらの公開成功記録へ加算しない。既存手法数145、状態は教育用100・解説のみ16・予定29。PML、媒質界面の反射/透過、電荷/電流、分散媒質、3次元一般形状の実装・検証は今後の範囲。独立参照は連続解析解と別に導いた離散恒等式であり、他ライブラリのFDTDコードとの比較を行ったとは表示しない。
