# 更新と復元の手順

## 実装範囲の表示と軽量な共通検索（2026-11-23）

HF/KSのモデル説明は一般形と公開した原子・H₂・固定周期Heセルの範囲を区別する。catalog/atlas-equations.jsonのnoteだけを修正し、式・入力・参照・受入条件と配布版を保持する。モデルに結び付く実行例と各ケースの制約は既存の台帳から案内する。

ホームと共通検索のscope=atlasはsearch/engine.mjsのatlasSearchと、同じsearch/atlas-query-index.jsonを使う。実行意図語・英単語境界・手法名・目的の制限・順位付けを揃える。サイト全体はsearch/query-index.jsonを使い、空の検索画面では索引を取得しない。既存のsearch/index.jsonとnumerical-methods-atlas/home-search-index.jsonは詳細な互換用公開データとして同じURLに保持する。

軽量版はcompact_search.pyが公開本文の正規化済み空白トークン集合を共通辞書と昇順差分IDへ可逆にまとめる。日本語の語中一致・数値・句読点を含む語を保ち、表示用の原文と明示的な関連経路をsearch/details/<SHA-256>.jsonへ分ける。画面の関連資料を開くと元の範囲説明・リンク・保存図を取得し、全文検索結果の抜粋は公開原文から補う。取得先は固定した同一サイトのファイルだけで、検索語を送信・保存しない。公開済みの内容ハッシュ付きdetailsファイルは削除・上書きしない。

search/budgets.jsonで画面向け2索引のUTF-8とgzip level9の予算を管理する。全文トークンの同等性、詳細ファイルのSHA、両入口の代表検索・全手法名、遅延読み込みと目的別制限を検査する。通常のprepareで両索引・依存モジュールの版を一括更新する。新しい機能と索引形式の変更があるため今回の公開前集約は日次更新の例外として私用キューへ実ログ・対象treeとともに記録する。数値計算や独立参照を索引更新のために再生成しない。

このリポジトリの `main` 直下を GitHub Pages で公開する。公開先は https://hrkoyama.github.io/ 。作業開始時に `git status` とリモートの最新版を確認し、他の未完了変更を上書きしない。

## 公開先の固定ルール

2026年11月22日のユーザー指示により、今後の公開先は **https://hrkoyama.github.io/** 配下だけとする。公開用リポジトリは **`hrkoyama/hrkoyama.github.io`**、公開ブランチは **`main`**。数値計算アトラスは `/numerical-methods-atlas/` に公開する。

**`koyamarium` 配下へ変更を反映しない。** push、PR作成・マージ、リリース、アップロード、公開・デプロイ用ワークフローの起動を行わない。上流ソースのローカル編集・検証は可能だが、上流へ push してから公開する手順は使わない。`koyamarium.github.io` と旧 `koyamahr.github.io` は公開先にしない。過去のURL・履歴の参照と、現在の公開先を区別する。

公開直前に `git remote get-url --push origin` と配信URLを照合し、実際の push 先と公開URLがこの指定に一致することを確認する。不一致なら正しい公開用作業コピーへ切り替える。公開側の独自拡張と他作業の未コミット変更を保持し、今回の変更だけを統合する。上流ビルド全体で公開サイトを置き換えない。常時適用する指示は `AGENTS.md` にも記録する。

## 通常の更新

Python 3.10以上とNode.js 22以上を使う。以下はPython標準ライブラリとNode標準機能だけで実行でき、ChatGPTやEnterpriseへの接続、推論APIキーは不要。

1. 対象の本文・データを編集する。
2. 公開前は必要な修正をステージし、`python3 scripts/prepare-indexes.py` を明示的に一度実行する。隔離コピー内の通常refreshで、公開用の進捗と取得案内、共通ナビゲーション、サイトマップ、研究相談索引、サイト内検索を更新する。作業中の更新は1日1回程度にまとめ、通常コミットごとの全再生成は行わない。
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

「コード・入力・検証」の各実行例から手法・式・問題図・参照解へ進む対応は `scripts/atlas_execution_routes.py` が共通実行台帳、式の対応表、明示的な問題対応と不変な追加配布版から解決する。共通案内・専用ページ・追加検証・入口一覧の日英HTML/JSON/Markdownを通常のrefreshで更新する。実際の `method_ids` と直接対応する式を使い、関連モデル・代表図・関連する参照解を固定入力そのものと混同しない。物理問題に結び付かない検査例は自身の保存済み検証図と比較条件へ案内する。`scripts/atlas-execution-routes.test.mjs` が対応と生成物を確認する。数値入力・結果・受入条件・共通registry・配布版の検証記録をナビゲーション整備のために変更しない。

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

## Bratuの複数パラメータ推定・正則化・識別可能性

正本は `catalog/atlas-detailed-reading.json` の `bratu-multi-inverse` と `catalog/atlas-methods.json`。定数λから空間係数 `λ(x)=a+b(2x−1)` へのモデル拡張を明示する。固定した下側分枝と区間制約のもとで随伴ベクトル勾配を実際の推定更新へ使い、Tikhonov正則化の強度・事前値・パラメータ尺度を記録する。データだけの重み付き観測感度行列のSVDと、正則化を加えた系を区別する。中央1点観測は階数が最大1であり、反射対称な係数の符号も区別できない。正則化による事前値の選択を、観測情報の増加と表示しない。

専用の不変配布版は `/code/bratu-multinverse/2026-11-22/`、梱包と独立展開の検証は `scripts/package-bratu-multinverse.py`、配布整合性の照合は `scripts/atlas_multinverse_release.py`。同じ格子による回復の整合性検査、細かい参照格子で生成して固定した観測への格子依存、固定摂動と正則化の比較を分ける。高次元の関数同定、大域的一意性、実測データ、統計的な信頼区間、データに基づく自動的な正則化強度の選択は検証対象に含めない。

既存 `optimization` の実装状況だけを拡張し、手法数・固有テスト問題数・共通実行例数は追加しない（今回の統合時点では共通22実行例・固有67問題）。公開手法JSONの主配布先は新しい2係数版とし、従来の1係数版の検証済み取得情報を `scalar_inverse_release` に保持する。旧章URL・節IDと以前の不変コード配布版を保持し、通常のrefreshで図・検索・ホーム・日英本文を再生成する。公開先は引き続き `hrkoyama.github.io` 配下だけ。

## 6分野の軽量な補助検証（2026-11-22）

`catalog/atlas-depth-expansion.json` を正本として、基盤手法4例、生物・確率・温度制御5例、粒子・輸送6例、流体・MHD4例の計19例を案内する。共通22実行例の台帳とその過去の成功記録は変更しない。テスト問題の目録は新しい13問題を加えた80問題となる。同じ物理問題の別手法やGLMの診断用モードを重複加算しない。

編集用コードは `scripts/depth-{foundations,models,particles,mhd}/`、不変配布版は `code/validated-examples/2026-11-22/{group}/`。`scripts/package-depth-examples.py --group GROUP --edition YYYY-MM-DD[-rN]` は計算・図を保存した後、ZIPを別フォルダに展開して全pytestと全入力を実際に再実行する。4版で93テストを通過した。既存版は上書きしない。通常のページ再生成では計算せず、`atlas_depth_release.py` が入力・ソース・ZIP・成功記録を照合する。`build-atlas-depth-examples.py` が19個別ページと日英4章を生成し、`update-depth-ci-pins.py` が公開専用台帳とCIのハッシュ固定値を更新する。通常のrefreshとNodeの全検査を行う。

`.github/workflows/atlas-depth-linux.yml` は公開済みの4 ZIPを新しいLinux/Python環境で取得し、SHA-256照合、全pytest、全19例の実計算と数値条件を検査する。共通サイト検査成功後・週次・手動で実行する。コードをcheckoutせず、固定したnumpy/scipy/pytestのみを使用し、描画と量子化学の計算は行わない。失敗時もログと計算結果を保存する。`verify-depth-public.py` は保存済みresult.jsonの一致だけを成功条件にせず、実行の終了と全ケースの条件を確認する。

量子化学を含む従来の22例Linux CIはユーザーの軽量化方針に従い手動実行だけにした。過去の自動実行に関する記録は当時の構成であり、現行の通常CIの範囲を示さない。2026-11-22のrun 44998314368の全22例成功記録を保存している。

検証範囲は各ケースの条件を優先する。Langevinは調和振動子のBAOAB、FMMは2次元対数核、DSMCは一様なMaxwell分子の衝突緩和、PME系はEssmannのSPME変種である。独立Athena++参照とのMHD比較は元の一次精度CT/GLM実装を変更しない。同条件の物理設定と共通診断に加え、CT固有の面上divergenceとGLMの中心差分診断を区別する。BOMDとの結合、全温度制御方式、3次元一般核、一般境界・媒質の検証へ拡大解釈しない。
## FDTDの媒質界面・左右x方向PML（第2版、2026-11-22）

新しい不変配布版は `code/fdtd/2026-11-22-r2/`。初版 `2026-11-22/` のソース・図・入力・ZIP・記録は変更しない。編集用の追加コードは `scripts/fdtd/scattering.py`、実行は `run_scattering.py`、テストは `test_scattering.py`。新入力 `dielectric-interface.json` と `pml-pulse.json` を加え、パッケージ処理は旧2例も含む4例を独立展開・再実行する。旧版の真空ソルバー・runner・入力・テストの同一性をprovenanceとハッシュで確認する。

界面は非磁性・無損失・非分散のε₁=1/ε₂=4への垂直入射に限定する。振幅Fresnel係数r,tと、誘電率・波速を反映したパケットエネルギーR,Tを区別する。界面節点には算術平均のεを置き、左右のエネルギー積分で節点を重複計上しない。閉じた計算領域の保存量、R+T、解析解誤差と格子収束を別々に判定する。

PMLはy周期の2次元TMz帯領域の左右x方向だけ。Bérenger型の補助分割Ez=Ex+Eyで、ExとHyの減衰率を整合し、時間方向の減衰は台形則で扱う。Ex,Eyは物理的な電場のx,y成分ではない。層の物理厚さ・最大減衰率・次数を固定して格子を細分化する。有限厚PMLの外端PECからは解析的に予測される戻り波が残るので、反射振幅の絶対値と、その解析的な有限層戻り波に対する誤差・収束を分離する。入射波の中心波数角度と、有限帯域パルスの角度分布も区別する。

PMLの電場・磁場の仕事は場と係数から直接集計し、修正離散エネルギーとの収支を照合する。仕事をエネルギー差から逆算しない。局所的には符号を持つ計算上の仕事であり、物理媒質の正のOhm発熱とは呼ばない。物理領域のエネルギー・Poynting流束は別の近似収支として誤差と収束を調べる。広領域の同じYee更新は境界反射の切り分け用で、外部の独立したFDTDライブラリとの比較ではない。

日英正本は従来どおり `catalog/atlas-detailed-reading.json` のfdtd。旧節・旧配布版へのリンクを残し、interface/pml節と第2版の入力・図・結果へ接続する。`atlas_fdtd_release.py` のcases指定と `build-atlas-fdtd.py` が4例を照合する。共通実行台帳22例・全問題67件には加算せず、FDTD補助配布版として案内する。四辺・角PML、媒質界面への斜め入射、浅い入射、分散物質、3次元への拡張はこの版の検証範囲から外す。公開先・手順は冒頭の指定を厳守する。

## FDTDの四辺・角PML（第3版、2026-11-22）

不変配布版は `code/fdtd/2026-11-22-r3/`。初版とr2の配布物・図・入力・検証記録を変更しない。編集用の追加コードは `scripts/fdtd/corner.py`、実行は `run_corner.py`、テストは `test_corner.py`、新しい入力は `inputs/pml-corners.json`。梱包処理は旧4入力と新入力の全5例を実行し、ZIPを独立展開して全テスト・全入力の再実行と数値指標/CSVの一致を検査する。r2の数値ソース・テスト・旧4入力は同一バイト列で保持し、provenanceに記録する。

真空2次元TMzの四辺にBérenger型PML、外端すべてにPECを置く。補助電場Ex/Eyはそれぞれγx/γyで減衰し、磁場Hy/Hxも対応するγx/γyで減衰する。角では両方の係数が同時に非ゼロになる。各Yee位置で係数を評価し、電場x/yと磁場x/yの仕事を場と係数から直接集計する。修正離散エネルギーとの収支は仕事を逆算する方法で確認しない。符号付き補助場の仕事と物理的なOhm発熱を区別する。

辺へ向かう波と斜めに角へ向かう波を別の組として確認する。四辺それぞれの流束、角領域の寄与、初期PML内の微小な場、参照の周期/領域と観測窓を記録する。有限厚・有限時間・選んだ波束の検証であり、任意の角度/周波数で反射ゼロ、一般媒質、分散物質、媒質界面への斜め入射、3次元の実証とは表示しない。参照の構成とその検査範囲は日英解説・コード・結果JSONで明示する。

日英の正本は従来のfdtd章とし、`pml-corners` 節とr3の取得先を追加する。旧節ID・旧版ZIP・r2の取得先は保持する。共通22実行例・固有67問題へ加算せず、FDTD補助配布版の5入力として案内する。通常のrefresh・全Node検査・日英と狭い画面の確認後、指定されたhrkoyama/hrkoyama.github.ioのmainだけへ公開する。公開後に本文・図・ZIPを匿名取得し、検証済み版と照合する。

## アトラスの検索と3つの入口

各解説章の資料ナビゲーションは `scripts/build-atlas-chapter-resources.py` が実在する日英の章と共通の対応情報から生成する。冒頭の5つの短い入口と章末の詳細を本文のarticleの外に置き、既存の数式・節ID・目次・index.json/Markdownとcontent JSONを保持する。各章の `resources.json`・`resources.md` と全体の `numerical-methods-atlas/reading-resources.json` も同時に更新する。章固有の対応がない場合と一部の分類が空の場合は「全体一覧」と明記し、未登録の科学的な対応を補わない。

5つの基礎章の追加対応は `catalog/atlas-chapter-links.json`。既存の `related_methods` は関連する定義だけに使い、Jameson系の解説へ古典RK4などの実行例を継承しない。円筒座標・格子のソース検査とPDEの固定入力例も区別する。通常refreshの章生成・章目次・章ナビゲーションの後、検索の前に実行し、検索本文と研究相談の本文抽出から資料ナビゲーションを除外する。生成する実在章manifest `chapter-resources.mjs` により、旧 `#/read/...` も静的専用章を含めて正しい日英ページと節へ転送する。`scripts/atlas-chapter-resources.test.mjs` が全章、本文保持、再生成、転送と参照条件を確認する。

検索結果の5つの入口は `scripts/atlas_search_routes.py` が公開済みの手法・問題・式・参照解台帳と検証済み実行例、明示的な章の対応から生成する。アトラス内検索とサイト全体検索は `search/navigation.mjs` の表示を共用し、方程式・参照解の個別項目も言語に対応した節へ直接つなぐ。複数候補と図の確認は折りたたみ、問題ごとの参照条件を集約時にも保持する。目的別の検索にはその目的で許可された実行例だけを渡し、予定手法や診断例へ他の実装・物理問題を割り当てない。検索語は従来どおりブラウザ内だけで処理する。

対応JSONは `/search/atlas-navigation.json`。本文の検索語と関連資料の対応情報を分け、隣接するカードの案内文から科学的な対応や実装を推測しない。通常refresh・コミット前の生成・CIで両検索と対応JSONを更新し、`scripts/atlas-search-navigation.test.mjs` が元の対応、図の出典、目的の制限、日英のリンク、表示と検索語の非送信を検査する。

トップの文言と3入口は `catalog/atlas-home.json` が正本。「目的から探す」は `/numerical-methods-atlas/start/`、「まず計算を試す」は `/numerical-methods-atlas/code-and-data/examples/`、「体系的に読む」は `/numerical-methods-atlas/explore/` へ進む。トップに全目的・分野地図・収録件数・検証範囲を再び並べない。

`build-atlas-purpose.py` と `atlas_home_layout.py` が日英の静的トップと次の階層を生成する。ライブ表示は `home-overview.js` と `home-search.js`、静的表示は同じレンダラーの `render-atlas-landing.mjs` を使う。詳細な地図と読む順番はexplore、目的フィルターはstartに保持する。科学的な台帳、既存のJSON・Markdown、固定配布版はこの表示整理で変更しない。`home-navigation.mjs` は以前の地図・分野・絞り込みURLを適切な次ページへ案内する。全条件がallのトップURLはトップのままとする。

ホームの外枠は `body.atlas-home` と `atlas-home-shell.css` で簡素化し、他の展示のナビゲーションを保持する。検索語は従来どおりブラウザ内だけで処理する。JavaScriptなしでは3入口と専用検索ページへのリンクを使える。通常のrefreshと全サイト検査後、日英・390px・検索・3入口・既存ブックマークを確認して公開する。

## 表示同期とCSVR／Langevin比較（2026-11-22）

生物の実装状況は `atlas_equation_availability.py` で、共通例と補助例の実在・不変配布物・追試記録を照合する。ロジスティック、閉鎖SIR、Turing発現／Schnakenberg、空間なしFHNの限定範囲を方程式一覧へ接続し、方程式総数46を保って実例23・解説23とする。TuringとSchnakenbergの同一実行を物理問題へ二重加算しない。Ewald／SPMEの古い実装前注記は正本と統合スクリプトで修正し、量子の次課題は軽量保守と必要性指定時の重い検査に位置付ける。

新しい温度比較の編集用ソースは `scripts/depth-thermostats/`、不変配布版は `code/validated-examples/2026-11-22/thermostats/`。CSVRの浴単独、CSVR／Langevinの調和2自由度、弱い四次非調和2自由度の3固定ケースを持つ。浴単独は診断で物理問題数へ加算しない。調和比較は既存のLangevin調和問題へ補助リンクを追加し、非調和問題だけを新しい1問題として数える。旧4補助配布版、既存BAOAB例、共通22実行例の配布物・入力・公差・履歴は変更しない。

CSVRは2007年原著の厳密な運動エネルギー更新に、2008年の式8–9の同じGaussianを使う符号を採る。Gamma生成は著者公式訂正も参照する。局所Langevinとはτ=(2γ)⁻¹で浴の運動エネルギー緩和を合わせ、両者に同じOBABO分割を使う。旧BAOABと同じ積分法とは表示しない。正準分布、HOの有限刻みshadow Gaussian、非調和Boltzmann求積を区別し、相関の一致や一般のエルゴード性を合格条件にしない。固定点CDF差はKS全域距離ではなく、誤差帯は独立複製間の標準誤差である。軸上不変の反例、ゼロK拒否、刻みと結合時間の範囲も明示する。

`build-thermostat-reading.py` と `catalog/atlas-thermostat-comparison.json` は日英の本文・8式・出典・JSON/Markdownを同じ根拠から生成する。Langevinの旧主配布版は `depth_release` に保持し、新比較は `depth_additional_releases` へ追加する。`depth_release_records` は各版・選択ケースを個別に照合し、異用途の例や重複した根拠の流用を拒否する。CSVRとLangevin以外の10温度制御法は実装予定を維持する。

軽量公開CIの対象は5補助配布版・22補助ケース・135 pytestであり、量子を含む従来の共通22例とは別の台帳である。通常のrefreshでは保存物を照合して描画し、科学計算と重い量子参照再生成は行わない。数値ソース・入力を変更する場合は新しい不変版を作り、ZIPの独立展開と全固定入力の再実行を行う。受入基準を失敗隠しのために緩めない。

## FDTDの媒質界面への斜め入射（第4版、2026-11-22）

新しい不変配布版は `code/fdtd/2026-11-22-r4/`。初版・r2・r3は上書きしない。追加の編集用ソースは `scripts/fdtd/oblique.py`、runnerは `run_oblique.py`、テストは `test_oblique.py`、入力は `inputs/dielectric-oblique.json`。従来の数値ソース・テスト・5入力はr3と同一バイト列で保持する。梱包時に全6入力を実行し、ZIPの独立展開・全テスト・全入力再実行で数値指標とCSVの一致を確認する。

対象は平面・無損失・非磁性誘電体界面の2次元TMz。Ezは入射面xyに垂直で、光学のs/TE偏光に対応する。周波数と接線波数を連続にした各モードのFresnel振幅・エネルギー係数、Snell角を用い、有限帯域波束を参照する。搬送波1成分の係数と、スペクトルで重み付けした波束の反射・透過エネルギーを区別する。解析波形に対する振幅倍率の目標は1であり、それを搬送波のr/tと呼ばない。

界面を含む場の誤差と格子/時間収束、反射・透過エネルギー、全体の修正離散エネルギー、局所の物理エネルギー・Poynting流束収支を別に判定する。連続参照の有限スペクトル積分・初期場の裾・外端PECと観測窓を確認し、全反射・p偏光・Brewster角・損失分散媒質や3次元まで検証したと表示しない。PMLを使わずに界面の検証を切り分ける。

日英本文の正本は既存fdtd章。`interface-oblique` 節とr4の図・結果・取得先を追加し、以前の節IDと3版のZIPを保持する。FDTD専用の補助配布版であり、共通実行台帳や他分野の検証件数へ加算しない。通常refresh・全Node検査・日英と390px幅の確認後、指定のhrkoyama/hrkoyama.github.io mainへ公開する。公開後に日英ページ・全図・ZIPを匿名取得して同一性を照合し、公開ZIPのテストも再実行する。

## 非線形反応拡散・パターン形成の独立検証（2026-11-22）

編集用の正本は `scripts/depth-biology/`、新しい不変補助配布版は `code/validated-examples/2026-11-22/biology/`。`schnakenberg-nonlinear` と `schnakenberg-pattern` は、既存の `turing-schnakenberg` 物理問題の有限振幅過渡と成長後を調べる追加ケースであり、問題数を増やさない。共通22実行例、旧5補助配布版、既存の図・入力・公差・成功履歴を保持する。

対象は無次元Schnakenbergの1次元2π周期系。a=0.1,b=0.9,D=(0.01,1)、固定したcos2/cos4の初期場、t=8と100を用いる。反射対称かつπ周期の不変部分空間を選んでおり、ランダム擾乱からの一般的な波数選択、2次元の模様、生物データの較正へ外挿しない。主計算は二次中心差分の拡散半ステップを厳密な離散熱半群で進め、反応の陰的中点法とStrang分割で組み合わせる。反応Newtonの残差、計算中の正の濃度、反応によるsource/sinkの離散収支を調べ、無条件正値や総量保存とは呼ばない。

独立参照は実cos係数のFourier–Galerkin空間離散とSciPy Radauで構成する。cubicのu²vはM=4(K+1)>4K点で評価して射影し、quadratic用の3/2則を流用しない。K=32/64/96と公差の細分化で参照自身の感度を検査する。空間比較はこの異なる空間離散へのraw field誤差、時間比較は同じ差分半離散系を別のRadauで進めた参照への誤差とする。L1/L2/L∞の各定義・speciesの扱いは専用READMEに従い、位相合わせで誤差を隠さない。

最初の粗い時間刻みは、分割誤差が最細の空間誤差を覆い、次数・誤差分離の事前基準を満たさなかった。`inputs-initial.json` と `protocol-history.json` に初回の条件と失敗指標を残し、受入基準・物理モデル・格子・参照条件を変えず、空間比較用の時間刻みと時間収束系列だけを細分化した。判定基準の緩和で成功扱いにしない。理論二次の構成と、有限の刻み対で観測した次数を区別する。

近定常の確認は高精度Galerkin参照に対する有限時間の検査。有限刻みStrangの固定点とPDEの定常解は一致するとは限らず、主計算のfull RHS残差を別に示す。線形化との差は非線形性の指標であり、精度や定常性の証明には使わない。既存生物章のoverlay、方程式ギャラリー、目的・分野・接続・手法の入口から専用の日英章と2実行ページへつなぎ、FHNの0次元限定や未実装17モデル族の表示を保つ。反応と輸送の結合経路は未追試のままとする。

通常の軽量Linux CIは6補助配布版・24補助ケースを公開ZIPから検査し、量子を含む従来の共通22例CIは必要時の手動実行を維持する。通常refreshは保存物の照合と描画だけを行い、科学計算を起動しない。公開先は指定のhrkoyama/hrkoyama.github.io mainだけとし、公開後に本文・図・ZIPと実際のLinux追試を確認する。
## FDTDのp偏光・Brewster角・全反射（第5版、2026-11-22）

不変配布版は `code/fdtd/2026-11-22-r5/`。追加の正本は `scripts/fdtd/polarization.py`、`run_polarization.py`、`test_polarization.py` と `inputs/p-polarization.json`。旧TMzソース・テスト・6入力をr4と同一バイト列で保持し、初版〜r4の4配布版を上書きしない。全7入力を実行し、ZIPの独立展開・全テスト・全入力再実行で指標とCSVの一致を検査する。

新規TEzはHzを整数時刻のセル中心、Ex/Eyを半時刻の辺に置く。固定例では周期yの単一接線モードへ厳密に縮約した更新を用い、全2次元Yee更新との同値性を別に検査する。界面は無損失・非磁性で、PMLは使わない。振幅r_H/t_H、法線エネルギー比R/T、有限帯域Brewster残留反射と単色係数ゼロを区別する。同じYee法の一様媒質対照で入射波の伝播誤差を反射から分け、連続Fresnel参照で別に精度を判定する。

全反射は全スペクトルが臨界角を越えるコンパクトな帯域を使い、減衰する複素波数を選ぶ。透過側のエバネッセント場と有限時間の蓄積エネルギーを、法線の正味透過率と混同しない。位相・減衰率、直接計算した流束・全体の離散保存量、参照の求積・時間窓・外端と初期裾を確認する。正味Tの微小な相殺誤差の生データは保持し、TIRの収束判定には符号付き過渡流束波形の相対L2誤差を使う。一般媒質・多モード・損失分散・3次元まで検証したとは表示しない。

既存fdtd章へ `interface-p-polarization` 節と新版取得先を追加する。r4等の除外は歴史的な範囲と明示し、新版の実測範囲へつなぐ。共通実行台帳や他分野の件数へ加算しない。通常refresh・全Node検査・日英と390px幅の確認後、hrkoyama/hrkoyama.github.ioのmainだけへ公開し、公開後の日英ページ・全図・ZIPを匿名照合して公開ZIPのテストを行う。
## 解説章の統一目次

日英の `/numerical-methods-atlas/{ja,en}/read/` は `catalog/atlas-reading-index.json` を分類と並び順の正本にする。`scripts/build-atlas-reading-index.py` が、公開済みの全章のタイトルと実在する言語版を読み、同じ構成のHTML・JSON・Markdownを生成する。章本文・章名・章URL・実装状況は目次の表示整理で変更しない。新しい章を追加したらこの目次の分類にもIDを一度だけ追加する。未登録・重複・存在しないIDがあれば生成を失敗させ、追加章を黙って落とさない。

各分野の章ビルダーが目次へ足す旧ブロックは、通常refresh内の統一目次ビルダーで置き換える。実行順は全章の生成後、アトラス内検索・全体検索・共通ナビゲーションの生成前とする。目次を直接編集したり、後段に別形式の一覧を継ぎ足したりしない。

`reading-index.mjs` の章名絞り込みはブラウザ内だけで動作する。JavaScriptなしでも全章へのリンクを表示し、章名の切り詰めや実装済みと誤解する一括ラベルを使わない。日英の分類・章順、重複のない全章リンク、狭い画面、以前の章URL、JSON・Markdownを通常の検査と公開後に確認する。

人向けの入口は「分野別に解説を読む」（理論・導出・計算例を分野順に読む）と「手法・コードの対応表」（手法名から適用条件・コード・検証例・公開状況を調べる）を区別する。体系的に読むページでも両方の役割を短く説明し、同じ種類の一覧に見える名前だけのリンクを並べない。既存のread/methodsのURLと機械可読データの意味は保持する。

## 教科書・参考文献と章ナビゲーション

教科書案内と原著・参考文献は「教科書・文献」という学習資料の入口に分ける。解法の章と同じ名前順の長い一覧へ埋め込まない。トップの検索と3入口を保ちながら、その直後と「体系的に読む」の上部に日英の直接リンクを置く。書籍の本文・書誌・表紙・関連章と既存URLをこの表示変更で書き換えない。

`scripts/build-atlas-reading-navigation.py` は全章の生成と統一目次の後、検索の生成前に、旧 `.reading-nav` を「学ぶ・調べる」と「教科書・文献」の短いナビゲーションに揃える。教科書・参考文献ページの周囲の分類は「学習資料」にする。章本文とページ内目次を保持し、JavaScriptなし・狭い画面でも資料へのリンクを表示する。再取り込みで旧「各章へ」が戻っても通常refreshで整理し直す。

## 多峰性MCMCと診断の独立照合（2026-11-22）

編集用正本は `scripts/depth-mcmc/`、新しい不変配布版は `code/validated-examples/2026-11-22/mcmc/`。旧 `models/` のGaussian標的・古典split-Rhat・保守的ESSは変更しない。新しい `mcmc-multimodal-mixing` は等重みN(-6,1)/N(6,1)の1次元二峰性標的を1問題として追加し、`mcmc-diagnostic-reference` は診断用として物理問題数に加算しない。提案法・初期値・seed・標本予算の違いを別問題として数えない。

混合比較は同じ目標・局所提案幅・固定予算で、峰を分けた初期値の局所RW、全鎖を同じ峰に置いた局所RW、既知の対称性を利用する反射ジャンプ併用を比較する。意図的な混合不良を正しく示すことが検証の成功条件であり、全系列が収束したという意味ではない。pooledな分布が良く見えても各鎖が移動していない場合と、Rhatが良く見えても全鎖が同じ峰を見落とす場合を区別する。自己遷移を含む全drawを使い、受理標本だけを抜き出さない。

rank正規化split/folded Rhat、bulk ESS、5%/95% tail ESSと、x・峰指示関数という異なる観測量を区別する。定数や変動不足は状態と理由を表示し、非有限値を安心できる数値に置き換えない。負相関でESSが標本数を超える場合と、旧Gaussian例のτ>=1規約を分離する。rank正規化はVehtariらの原著訂正を含む式を使い、固定した有限計算の診断を一般的な収束保証や偽陽性率の較正とは呼ばない。

独立診断参照は、版を固定したArviZへ同じ鎖を実際に入力して得る。参照の生成手順・環境・入力と鎖のSHA・参照値を保存し、通常の公開CIはNumPy/SciPy/pytestだけで保存参照への一致と実際の固定入力を再実行する。ArviZ参照の再生成は別の任意手順とし、原著式からの独自実装を長い第三者コードの転載で置き換えない。FFT自己相関は別の直接lag和とも照合し、IID/AR(1)の解析的な参照と有限標本推定の違いを明記する。

既存MCMC章の節ID・式・URLを保ち、日英の理論・測定範囲・旧Gaussianと新配布版へのリンクを同じ正本から生成する。目的・分野・確率数理の読書リンク・統一目次・ギャラリーも同期する。既存81図を保ち、新しい物理目標1件だけで82問題・実行入口38とする。通常の軽量CIは7補助配布版・26補助ケース、共通22例と量子を含む詳細CIは必要時の手動実行を維持する。公開後にhrkoyama.github.ioの日英本文・図・ZIP・診断参照とLinux実追試を確認する。

## 索引のまとめ更新と公開前の鮮度確認

2026年11月23日の指示により、索引更新は作業のまとめとして1日1回程度に集約し、公開前には必要な変更をステージして `python3 scripts/prepare-indexes.py` を明示的に一度実行する。通常のコミットごとに全再生成しない。「1日1回」は作業のまとめ方であり、定時ジョブやMacの常駐・背景処理は新設しない。過去の節にある「コミット前の自動生成」は、この運用に置き換える。

任意のコミットフックを使う新しい公開作業コピーでは、Python 3.10以上（通常は3.12）で `python3 scripts/install-index-hooks.py` を実行する。Gitの `extensions.worktreeConfig` が未設定の新規クローンでは先に `git config extensions.worktreeConfig true` を設定する。インストーラは実際のoriginと全push先がhrkoyama/hrkoyama.github.ioであることを確認し、その作業コピーだけに `.githooks` とビルド用Pythonを設定する。既存の独自フックがある場合は上書きしない。

通常のpre-commitは短い案内だけを表示して終了する。`ATLAS_REFRESH_INDEXES_ON_COMMIT=1 git commit ...` と明示した場合に限り、従来どおりステージされた内容の隔離コピーで通常refreshを実行する。明示的な `prepare-indexes.py` も同じ処理で、目次、章ナビゲーション、手法・実行例の一覧、検索、サイトマップ、AI向けJSON・Markdownを再生成し、差分になった生成物だけを元の作業コピーとステージへ反映する。別の未ステージ修正を取り込まない。生成先に未ステージ修正や同名の未追跡ファイルがあれば自動上書きせず終了する。数値計算の全面再実行や自動pushは行わない。

`python3 scripts/prepare-indexes.py --check` は同じ隔離再生成で、ステージ済み索引の更新漏れを検査する。変更・追加・削除された生成物があれば失敗し、元のファイルやGitインデックスは変更しない。この検査も全再生成を伴うため通常コミットには付けず、Public site checksでは従来どおり毎回実行してから通常の参照検査とNode検査を行う。公開前の明示更新とCIの厳密な鮮度検査は省略しない。CIを通さずにPages配信設定だけで更新する手順を、鮮度検査の代わりにしない。

アトラス内検索は以前の索引へ追記せず、実在する日英の各章・公開資料の題名と節見出し・本文から再構築する。統一目次の題名は現在の公開H1を優先する。rootとアトラスのサイトマップも現在のcanonical HTMLから作り直し、削除されたページを残さない。`check-atlas-indexes.py` は実ページと目次HTML/JSON/Markdown・言語対応・章検索・サイトマップの章名と収録範囲を独立に照合する。新章は目次の正本にも一度だけ分類し、未登録や重複を黙って落とさない。

ローカルでの研究相談索引は、元ページのハッシュと抽出内容が同じなら取得日時も維持し、変更があれば新しくする。変更なしの再生成で差分が増えないことを保つ。保存済みの図や配布版の根拠が変わった場合は、通常の索引更新で数値結果を作り直したことにしない。既存の個別検証手順を用いる。

## 式・問題図・厳密解の補助索引

ホームの検索と3入口は保ち、その下と「体系的に読む」に、厳密解・参照解、テスト問題（名前と図）、方程式の補助入口を共通レンダラーで置く。入口だけを個別に継ぎ足さず、日英・静的表示・動的表示で同じ経路にする。

`scripts/build-atlas-solutions.py` は保存済み `assets/reference-solutions.json` の全ケースから `/numerical-methods-atlas/solutions/` のHTML・JSON・Markdownを生成する。解析解、非線形方程式の数値解を含む半解析参照、製造解を区別する。多次元問題の断面を全2次元場の保存データと呼ばない。問題の図は既存の検証済みギャラリー、方程式は正本の式一覧へ接続し、新しい数値結果や架空の図を作らない。

これらも通常refresh、作業のまとめ・公開前の明示生成、CIの鮮度確認に含める。図のない新問題や保存根拠の不一致は不足として検出し、既存の図示・検証手順で整えた後に索引へ反映する。

## 図から問題別の方程式・参照・コードへ進む

全テスト問題の図と問題名は `/numerical-methods-atlas/problems/{id}/` の問題別ページへ接続する。`catalog/atlas-problem-links.json` は、既存の問題IDと方程式・参照解・関連手法の対応および日英の条件説明の正本。`atlas_problem_links.py` が実在する公開資料と保存済みの成功記録を照合し、`build-atlas-problems.py` が四つの区画を持つHTML・JSON・Markdownと全件JSONを生成する。図・方程式・解の索引を生成した後、検索とサイトマップの生成前に実行する。通常refresh、公開前の明示更新、CIの鮮度確認に含め、生成物への手作業の追記を避ける。

同じ方程式でもパラメータ・初期値・次元・標本化が違えば、対応が分かる注記と「関連モデルの参照」の区別を保つ。図の断面を全多次元場と呼ばない。厳密解のライブラリにない参照も、実行例に保存された解析解・独立計算・統計診断の根拠へ直接つなぐ。未登録の解や実行例を作ったことにしない。

固定入力実行例は共通台帳の `problem_id`、補助配布版の `case_problem_ids` と実際の問題台帳の対応だけから結ぶ。対応がnullの診断ケースや、同じ章・モデルという理由だけのケースを借用しない。実行例で使った手法と関連解説の手法を分け、手法台帳の公開状態は維持する。ソース・テストが配布版全体の共有ファイルならその範囲を表示する。既存の問題専用テストへの経路も公開ソースと関数名を検査して別に示す。新しい問題を追加したら対応の正本にも一度だけ登録し、不足・重複・存在しないリンクを検査で検出する。

方程式・厳密解・参照解の一覧から問題図とコードへ戻る対応も、同じ編集用対応表から `atlas_problem_routes.py` で逆引きする。問題台帳、保存図のmanifest、元の方程式・参照解ID、実際の実行台帳と成功記録から解決し、生成済みの解一覧・ギャラリー・問題ページを入力にしない。方程式→図一覧→解一覧→問題ページの生成順に循環依存や一回遅れの更新を持ち込まない。

両一覧のHTML・JSON・Markdownへ関連問題を反映する。図と問題名は問題ページへ、「コード・検証状況」はその問題のコード区画へ接続し、実行案内・ZIPは実在する対応例だけを示す。参照解と図の条件差、関連モデルという関係、図・固定入力実行例が未登録であることを表示する。方程式への関連付けだけで、そのモデル全体のソルバーを実装・検証したことにしない。既存の式・参照値・状態・件数・配布版は保持し、対応が多い項目は先頭の図と残り件数を示す折りたたみで案内する。

## 手法から方程式・問題図・参照・コードへ進む

手法・コードの対応表には各手法の四つの短いリンクを置き、個別ページの方程式、問題図、厳密解・参照解、コード・検証の区画へ案内する。`atlas_method_routes.py` が編集用の問題対応表の `method_ids` と、実際の共通・補助実行例の `method_ids` を合わせて対応を解決する。同じ章・モデル・名称という理由だけで関連付けを増やさない。実行案内は選んだ手法のIDを含むケースだけに絞り、関連解説として結ぶ問題と実行例で使われた問題を区別する。図が共通でも、別の手法で解いたケースを選択手法の検証として表示しない。

図と結び付かない専用配布版や診断例も、手法台帳で確認済みの元のコード経路を維持する。Bratuの前進Newton、自動微分、感度・随伴、係数推定はそれぞれの配布版・入力・確認範囲で案内する。章単位の関連コードと、その手法の全変種に対する専用実装・保証を混同しない。既存の実装状態、ソース・テストの割り当て、一次文献、件数を導線の追加で変更しない。

方程式は関連する問題を経由した対応、参照解は問題ごとの関係と条件差を保持して案内する。18件の参照解一覧にない解析解・独立計算・統計参照なども、問題別の参照区画へ進める。対応がない項目は未登録と表示する。HTML・JSON・Markdownと `methods/navigation.json` を同じ情報から生成し、通常refresh、コミット前の再生成、CIの鮮度確認に含める。手法生成は問題ページより先に実行されるため、入力は元の問題台帳と保存図・成功記録に限り、生成済みの手法・方程式・解一覧・問題ページを読み戻さない。後から生成するページURLは検証済みIDで作り、最終のサイト検査で到達先を確認する。

## CT／GLMの同条件比較と格子・時間収束（2026-11-22）

新しい正本は `scripts/depth-mhd-convergence/`、不変配布版は `code/validated-examples/2026-11-22/mhd-convergence/`。旧 `mhd/` を含む7補助版・26ケース・202 pytest、共通22例とすべての過去入力・公差・結果を保持する。新しい物理2ケースは、構成した厳密な移流磁気静力学平衡1問題と、既存Orszag–Tang問題の追加検証であり、CT/GLMや格子・刻みの違いを別の物理問題として数えない。

対象は2次元周期・理想・平面MHD（vz=Bz=0）。CTは面磁場と算術平均による共有角電場、GLMはセル磁場とpsiを使う。どちらも同じ一次Rusanov流束族、同じ固定信号速度上限、同じ前進Eulerの時間刻み列を用いる。GLMの波速と物理減衰率は格子幅・刻みを変えても固定する。面とセルの配置、法線磁場の扱いなどは固有に異なるため、離散化全体の比較とし、差のすべてを発散制御だけへ帰属しない。旧版の格子依存減衰と異なる新しい固定条件であり、旧成功を新条件の結果へ書き換えない。

平衡のベクトルポテンシャルは A=a[cos k(x-ut)+cos k(y-vt)]、B=(Ay,-Ax)、p=p0+k²A²/2、密度・速度一定。Lorentz力と圧力勾配が釣り合い、そのまま一様移流する理想MHDの厳密解をアトラスで構成した。名前付き既存ベンチマークや引用論文からの実測データとは表示しない。保存量の厳密なセル平均を誤差の基準にし、primitive(qbar)の圧力と圧力の厳密な平均の差を区別する。

格子系列では全格子で共通の細かいdtを固定し、最細格子の刻み半減差がPDE誤差を覆わないことを確認する。時間系列は固定空間離散を別のDOP853で積分した参照と照合し、参照自身の公差・最大刻み感度を検査する。この参照は時間積分に対する独立アルゴリズムであり、独立PDE実装とは呼ばない。Orszag–Tangには固定された公式Athena++ソースのCT結果を別に使い、参照の格子と時間の細分化も比較する。

CT固有の面発散と、両方式に同じ演算子を適用するセル中心発散は別々に記録する。保存量・正の密度圧力・L1/L2/L∞・初期条件一致・参照誤差・実行上限を分け、丸めた表示で合否を変えない。平面・短時間・固定条件の範囲であり、一般3次元、長時間乱流、任意の衝撃波や全GLM/CT変種の検証とは表示しない。

通常refreshは保存済みデータ・ハッシュを検査して日英ページと索引を生成するだけで、科学計算や量子収束走査を起動しない。MHDの元の章への補足は `catalog/atlas-mhd-supplements.json` と `scripts/build-atlas-mhd-supplements.py` で一度だけ付け、既存の節ID・数式・過去版を保持する。通常の軽量CIは8補助版・29ケースとし、量子を含む共通22例の詳細CIは必要時の手動実行を維持する。指定のhrkoyama/hrkoyama.github.io mainへ公開後、日英本文・図・全ダウンロードの匿名照合と、Linuxによる公開ZIPの実追試を確認する。

固定した単一LLF速度を使う周期GLMでは、中心差分のcurlと発散および数値拡散が可換で、発散ゼロ・psiゼロの部分空間を代数的に保つ。したがって物理2ケースの小さい発散だけでは、清掃項が実際に働いた証拠にしない。追加の `ct-glm-constraint-control` は非ゼロ発散を意図的に入れた非物理の診断対照で、問題数へ加算しない。CTの既存制約誤差の保持とGLMの輸送・減衰を、同一初期セル磁場と独立Fourier行列で検査する。GLMの減衰率ゼロの対照も用い、Bとpsiの波エネルギーから位相変化・LLF数値拡散・前進Eulerの効果と物理減衰を区別する。既存2ケースの入力・基準を保持し、初回入力と診断追加の設計理由を配布版の履歴に残す。

## 基盤手法の条件数・残差・収束（2026-11-22）

正本は `scripts/depth-foundations-conditioning/`、不変配布版は `code/validated-examples/2026-11-22/foundations-conditioning/`。旧8版・29ケース・248 pytestと共通22例を保持する。新しい4ケースで通常の補助CIは9版・33ケースとなる。物理・代数問題の既存83件と実行入口39件は増やさず、AMG追加例は問題への対応がnullの代数診断とする。元のPoisson PDE例 `sa-amg` の精度検証を借用しない。

AMGは同じ正方Dirichlet行列で、格子サイズによる条件数の変化と、同じ条件数での異方性による収束の変化を分ける。真の残差・解誤差・DSTによる別解法・疎直接法と解析スペクトルを比較し、反復上限による未収束を成功へ読み替えない。QR／SVDは二進で正確に作れる行列と右辺摂動を使い、LAPACKおよび実際のbinary64入力を独立に80桁・120桁で計算した参照と照合する。再構成・直交性・後退誤差と、条件数で増幅される前進誤差を区別し、階数閾値を合わせる。高精度参照の再生成は別手順で、通常の3依存へ追加しない。

Krylov固有値解法は部分空間の次元・固有値の間隔・非正規性を分け、Ritz残差、固有値誤差、部分空間誤差と左右固有ベクトルの感度を測る。小残差でも固有値誤差が大きくなり得る構成対照は、解法の出力とは別に表示する。求積は次数・公差・評価回数・真の積分誤差を測り、相殺による条件数と丸め誤差、局所的な山を標本化できない誤収束を示す。既知の分割点・変数変換を使う対照の改善を、任意の未知関数に対する保証とは表示しない。

初回数値実行前に入力・判定基準を固定し、科学計算の参照・生成手順・出典・ハッシュを保存する。日英の既存4章・式・参照を保持して新旧の検証へ接続し、目次・分野別入口・問題・図・検索を同期する。通常refreshは保存結果の検査と索引生成だけを行い、量子の走査は起動しない。Linuxの公開ZIP追試成果物は、pytestの使い捨て一時コピーだけをuploadから除外し、全ての実行ログ・結果・判定・配布物を保持する。公開先の確認・匿名の全ファイル照合・実際のLinux結果取得までを公開完了の条件とする。

## FDTDの損失・分散媒質（第6版、2026-11-22）

不変配布版は `code/fdtd/2026-11-22-r6/`。追加の正本は `scripts/fdtd/dispersive.py`、`run_dispersive.py`、`test_dispersive.py` と `inputs/loss-dispersion.json`。r5の旧7入力・数値ソース・テストは同一バイト列で保持し、過去5配布版を変更しない。全8入力を実行し、ZIPを独立展開して全テスト・全入力を再実行し、指標・全CSVの一致を確認する。

追加範囲は真空に挟まれた有限厚の媒質板への一次元垂直入射。導電電流sigma Eと受動的な単一共鳴Lorentz分極を扱い、E/P/Jを局所陰的中点法、HをYee半時刻更新で進める。界面のE制御体積ではeps_inf・sigma・fを半体積で平均し、対応する密度P/Jと整合させる。遠方PEC外端を使い、分散媒質とPMLを組み合わせた一般例とは表示しない。

多重反射を含む複素板の解析解を用い、単色係数・帯域重み付きR/T/A・有限窓流束を分ける。吸収を1−R−Tだけから定義せず、sigma|E_mid|²とgamma|J_mid|²/fを直接積算する。場の修正離散エネルギー、振動子の蓄積、直接散逸の恒等式と、中心化した物理エネルギー・Poynting収支は別の基準として検査する。解析内部場の散逸積分、初期裾・外端・有限窓・参照求積、格子と時間の収束も確認する。Meepのsigma_D D規約や陽的ADEの共鳴安定条件を、このsigma E・中点更新へそのまま適用しない。

既存fdtd章へ `interface-loss-dispersion` 節と新版取得先を追加する。旧版の除外記述は当時の範囲と明示し、一般分散・斜め入射・多共鳴・異方性・3次元まで検証したと表示しない。日英解説・図・ソース・テスト・入力・収束データを同じ配布版へ結ぶ。通常refresh・全Node検査・日英と390px幅を確認してhrkoyama/hrkoyama.github.io mainだけへ公開し、公開後に日英ページ、全図、コードZIPを匿名照合して公開ZIPのテストを行う。

## Lie–Trotter／Strangの比較解説（2026-11-22）

`catalog/atlas-detailed-reading.json` の `operator-splitting` が日英本文・式・比較表の正本。`catalog/atlas-methods.json` に `lie-trotter` と `strang-splitting` を時間積分の `reading-only` として登録し、手法147項目（教育用例114・解説のみ17・予定16）とする。従来の件数は各追加時点の履歴として保持する。検索・目次・サイトマップは通常refreshで再生成する。

`python3 scripts/verify-operator-splitting.py --check numerical-methods-atlas/assets/operator-splitting.json` は、固定した無次元2成分振動子のN=8,16,32,64について、解析解との大域誤差・局所欠損、逆順のLie–Trotter、可換な減衰対照を標準ライブラリだけで再計算する。保存値の更新を伴わない。これは解説用の小例で、汎用ソルバー配布版・共通実行例・新しい独立テスト問題として加算しない。既存Strang反応拡散の入力・公差・保存結果・不変配布版は保持する。部分流の適用順序、局所欠損と大域誤差、近似部分ソルバーと時間対称性、境界による次数低下を区別する。

## 同条件のLie–Trotter／Strang反応拡散比較（2026-11-22）

正本は `scripts/depth-splitting/`、不変配布版は `code/validated-examples/2026-11-22/splitting/`。`reaction-diffusion-splitting` は既存のSchnakenberg問題の追加ケースであり、83物理問題と共通22例を維持する。手法147項目のうちLie–Trotter／Strangだけを限定した教育用実装へ変更し、教育用例116・解説のみ15・予定16とする。旧9補助版・33ケース・297 pytestは保持し、通常の軽量CIは10版・34ケース・313 pytestとなる。

32点の2次中心差分、2π周期、T=1、既存と同じa=.1,b=.9,D=(.01,1)と有限振幅cos2/cos4初期場を固定する。同じ拡散FD行列指数と反応の陰的中点則を用い、Lieの拡散全刻み→反応全刻みとStrangの半刻み→全刻み→半刻みを比較。16/32/64/128ステップ・共通5出力時刻で採用法全体の時間誤差を測り、反応中点則の離散誤差を純粋な分割誤差から分離できたとは主張しない。Newton誤差の感度は別に確認する。

参照は同じFD半離散系を実空間疎行列と別記述の反応RHSで組んだ非分割Radau。公差を細分化したRadauとDOP853を照合する。これは独立した時間積分法であり、連続PDEの厳密解や空間の独立検証ではない。成分ごとのL1/RMS L2/L∞の悪い方を、正の共通出力時刻について最大化する。反応source/sink収支、全副段階の正濃度、Newton残差・上限と停止理由を確認し、未収束・予算超過・既存出力への上書きを拒否する。初回固定プロトコルは入力・公差を変更せず合格し、その入力ハッシュと指標を保持する。

16検査と全入力をZIP独立展開から再実行する。通常refreshは保存済みソース・数値・図・成功記録を照合し、計算・参照生成を起動しない。追加した配布版だけが今回の新しい科学計算で、旧版と量子収束の再実行は区別する。日英の比較解説・実行入口、手法・検索・既存Schnakenberg問題・生物の入口と軽量CIを同期し、指定のhrkoyama mainだけに公開する。公開後の図・全配布ファイルの匿名照合と公開ZIPのLinux追試まで確認する。

## 粒子・輸送の独立参照・保存則・統計誤差（2026-11-22）

正本は `scripts/depth-particle-transport/`、不変配布版は `code/validated-examples/2026-11-22/particle-transport/`。旧9版・33補助例・297 pytestと共通22例を保持する。新6例で10補助版・39例となるが、既存5問題群への追加検証であり、物理問題83件・実行入口39件へ加算しない。EwaldとSPMEは同じ中性周期電荷の問題に結ぶ。入力と判定基準を初回実行前に固定し、初回結果と独立レビューを保存してから配布する。

Ewaldは非対称8電荷のエネルギー・全24力成分を、Gaussian/theta積分の別実装と照合する。参照の複数制御の精密化と有限上限の感度を測るが、厳密な全配置の裾評価とは呼ばない。SPMEはBスプラインのエネルギー勾配型であり、原法Lagrange PMEと区別する。実空間・自己項の共有を明示し、格子・次数・位相と電荷の保持、勾配、有限格子の非ゼロ合力を測る。2D対数核FMMは直接和と解析配置を参照に、展開次数・木・対称性を測り、木の深さで単調に改善するとは仮定しない。

PICは同じ粒子数の格子系列と、固定格子・粒子の時間系列を分離する。線形理論とDOP853を使い、後者は同じ粒子格子RHSを共有する時間積分の参照と明記する。Gauss則の解像モードとNyquist零モードを分け、電荷・運動量の保持とエネルギーの近似保存、quiet startと時刻0のCIC雑音を区別する。DSMCは等質Maxwell衝突成分のまま、有限Nの重心ゼロ球面・Beta周辺分布と独立Gaussian射影標本を比較する。保存量は全履歴の最大誤差、異方性・CDF・モーメントの不確実性は独立seed間で測り、相関粒子をIIDとしない。衝突roundを物理時刻へ換算しない。

純吸収放射輸送は空間と角度を別に精密化し、特性解・適応求積・指数積分と、入射フラックス重みmu=sqrt(U)の光子MCを比較する。収支・正値性と、seed間RMSE・二項分散・区間被覆を分離する。有限seedの実測被覆を全seedの保証としない。散乱・放射流体連成は追加しない。量子の重い計算は通常CIへ追加しない。

日英の既存6章とparticle-gravityの元本文・式・引用・図を保持する。FMMの追記正本は `catalog/atlas-particle-transport-supplements.json`、生成は `build-atlas-particle-transport-supplements.py` で、元本文のハッシュを確認してマーカー内だけへ追記する。通常refresh、目次・検索・目的・問題別入口を同期し、コミット前の自動生成が安定した後に指定mainへ公開する。公開後は日英・6図・配布全ファイルを匿名照合し、公開ZIPから実行するLinux CIの実レポートとスキップ0を確認する。

## 利用者のAIエージェント向け開発基盤の年末計画（2026-11-23）

現行計画の正本は `catalog/atlas-work-queue.json`。利用者のAIエージェントが、要求から対応する実装・前提条件を調べ、アトラス提供のコード・標準問題・参照・テストを取得し、組立・改修・実行・評価してコードと結果を利用者へ返す開発基盤を年末の中心成果とする。公開再現・保守・復元はその土台に位置付ける。現在は仕様策定段階で、提供キットや外部エージェントでの開発実証を完了済みと表示しない。

必達の試作は既存分野の小さな1次元移流・拡散2課題。11月30日に再利用する実装と言語・依存・機械可読仕様、12月12日に別エージェントの開発サイクル、12月18日に候補固定、12月23日に新規文脈の受入、12月31日に修正・引継ぎを目標とする。元実装の成功と改修後の実測、妥当な改修と意図的な不具合の対照を区別する。新キットの入力族・参照・合格基準を事前固定し、旧固定recipeや不変配布版を変更しない。利用者側の既存AIによる開発を、2027年以降の専門AI学習・モデル研究と区別する。量子化学は軽量のまま維持する。

同時期の作用素分割と粒子・輸送の追加を統合すると、補助版は11グループ・40ケース・388 pytestとなる。147手法は教育用例116・解説のみ15・予定16。共通22例、問題台帳83件・実行入口39件を増やさない。各追加時点の以前の件数は履歴として保持し、公開成功は匿名取得照合と実際のLinux公開ZIP追試の完了後に記録する。

12月16日のリトリートを最初のポスター発表目標に追加した。A0縦・日本語中心、専門用語を英語併記。12日に実証用版と結果を固定し、14日にPDF、15日に可読性・図式・引用・QRとオフライン説明を確認する。発表用の版と18日以降の年末候補を区別し、観測していない成功を記載しない。ポスターと開発実証は現時点で準備計画の状態。

## 全候補の逐次実装と図版化（2026-11-23）

ユーザーの「全部を候補に登録し、一つずつ実装してギャラリーに絵を加える」という指示の正本は `catalog/atlas-benchmark-backlog.json`。全分野調査の98候補と共通整備5項目を保持し、新規実装・既存検証の拡充・参照や出典整理を区別する。候補は手法台帳・物理問題・実行例の件数へ加算しない。Nohを最初とし、一単位の実装、参照と出典、数値検証、図、配布・公開の根拠を確認して状態を進める。既存の年末必達計画とは別の継続台帳で、全候補を年内完了とする期限や全候補の同時実行は設定していない。

`build-atlas-benchmark-backlog.py` は日英の状態ラベルと、日本語原文と明示した候補詳細を `/numerical-methods-atlas/backlog/` のHTML・JSON・Markdownへ生成する。完了した科学項目は実在する入力・ソース・図・実行入口・ギャラリー・成功した検証記録へ結ぶ。出典整理の完了には修正対象と根拠を記録し、架空の数値実行例を求めない。未着手を実装済みへ自動変更しない。

参照解の追加は旧 `assets/reference-solutions.json` の保存値を上書きせず、`catalog/atlas-reference-supplements.json` と `atlas_reference_catalog.py` で統合する。従来カードのID・式・表示先を保ち、追加カードには出典の役割と適用条件を明記する。Nohのカラー図は円筒対称の1次元半径方向計算を回転した表示であり、独立した2次元Cartesian計算とは表示しない。原点過熱・衝撃層を含む全域誤差と局所診断を分け、最大誤差が下がらない場合も保存する。

Nohの初回公開版は `code/validated-examples/2026-11-23-r3/noh/`。初回の未公開梱包では描画依存がruntime要件へ混入して公開verifierに拒否されたため、既存のnumpy/scipy/pytestの3固定版と任意の描画依存を分け、新しい版で12検査と全8格子計算を再実行した。数値入力・ソルバー・厳密解・受入基準は変更せず、依存修正前の記録と新しい実行前hashを保持する。通常のLinux公開ZIP検証は12補助版・41ケース・400 pytestとなる。共通22例と旧11版の数値成果物は維持する。最終図題はCONVERGING FLOWとし、収束するのは流れで衝撃波は外向きに進むことを明示する。図題訂正・SVGの行末整形を新しいr3版に分離し、数値内容と判定基準は保持した。

ExactPackを使う際は、元の問題・解の原著と別に Thrussell–Ferguson (2023), *ExactPack: A python library of exact analytic solutions*, SoftwareX24,101560, DOI `10.1016/j.softx.2023.101560` と公式 `lanl/ExactPack` を引用する。実際のcommit、モジュール、パラメータ、ソースハッシュ、実行した照合とライセンスを保存する。Nohの参照はcommit `9bacc477eb791e959c9621e771fc7a725db755fa` の `noh1.py` と、γ=5/3・密度1・内向き速度1の実行範囲に限定する。解析評価器との一致を、別の数値Eulerソルバーによる検証やExactPack全テスト実行と呼ばない。コードのBSD-3-Clauseとソフト論文の利用条件を混同しない。

教科書案内に併置する関連論文は `catalog/atlas-textbook-related-papers.json` と `build-atlas-textbook-papers.py` から生成する。DOI `10.1007/BF02462380` はAblowitz–Zeppetella (1979)のFisher特殊進行波の原著**論文**であり、書籍件数や表紙・ISBNを作らない。書誌は既存の `ablowitz1979` を再利用し、同じ論文を重複登録しない。

## 2D RKDGのAIエージェント向け開発キット（2026-11-23）

入口は `/numerical-methods-atlas/agent-kits/rkdg2d/`。日英の `TESTSET.md` / `TESTSET-en.md` をAIへ渡し、機械可読 `manifest.json` と現行の不変版 `/code/rkdg2d/2026-11-23-r2/atlas-rkdg-agent-kit.zip`、SHA256副ファイルからコード・固定入力・独立参照・評価器を取得する。`catalog/atlas-agent-kits.json` と `scripts/build-atlas-agent-kits.py` が案内HTML/JSONを生成し、通常refreshの索引とサイトマップに反映する。トップの入口は `catalog/atlas-home.json` と共通 `home-overview.js`、コード案内は `build-atlas-execution-guide.py`、AI用直リンクは `llms.txt` に接続する。共通22実行例や全体の手法・問題件数へキットを別問題として加算しない。

小さな新規PDEによるクイック検査、保存結果のハッシュ照合と再判定、全固定入力の新規再計算を区別する。元48科学ケースと波形4診断の合格を保持し、別の反転x追加試験は6件中5件合格・Shu–Osher p3不合格のまま公開する。固定閾値を緩めず、全モードの反転差と密度差を保持する。C++17解析I/O・1/2/4分割fixtureを、実MPI実行や他言語PDEの追試と呼ばない。完全2D結合は斜め波とDouble Mach、厳密1D入力は解析的縮約として範囲を明記する。

更新は旧ZIPや候補SHAを上書きせず、新しい版・manifest・MD・SHA目録を揃える。builderは保存物の存在・ハッシュ・既知の合否だけを確認し、PDE・独立参照生成は起動しない。公開後はMD・manifest・図・ZIPを匿名取得して照合し、その取得ZIPから軽量実計算と保存判定を行う。ポスター本体、非公開草稿やそのQRはこのキットへ含めない。

RKDG初版r1のLinux追試では、新規6本smokeは合格した一方、保存結果の照合で旧packagerが浮動小数点辞書の完全一致を要求し、プラットフォーム間の末尾桁差を失敗扱いにした。r2は記録照合の移植性を修正し、科学ソルバー・固定基準・独立参照・元の測定記録を同一バイト列で保持する。物理的な受入閾値の緩和ではない。r1 ZIP/SHAを上書きせず、そのMD日英とmanifestも同じr1フォルダへ原本のまま保存する。現行入口のMD/manifestとcatalogはr2へ揃える。r1がLinuxで全検証に成功したという記録は作らない。

## 球対称Nohの追加版

現行の不変配布版は `code/validated-examples/2026-11-23-r5/noh/`。初期圧力ゼロの球半径対称1D系列を追加し、平面・円筒の旧8プロファイルと59基準、旧r3配布物を保持する。球の受入基準は初回実行前に固定し、定数再構築2試行の各2条件不合格をソース・ログ・全配列とともに残す。第3試行は体積重心での保存量MUSCL/minmod、セル共通θによる両面傾き制限、線形面応力の球殻求積を用い、同じ105条件すべてに合格した。入力・格子・CFL・受入閾値は変更しない。セル平均修復、圧力floor、隠れた再試行は行わない。中心最大内部エネルギー誤差は悪化したため、その値も比較図に保持する。

球の離散質量・エネルギー収支と連続解析総量との差を分け、実時間刻みのΣdt³/6・Σdt³/12を照合する。全域r²重み誤差に加え、原点を含む固定coreと中心値も示す。図は1D半径解の中心断面であり、Cartesian多次元や角度方向対称性破れの計算とは扱わない。候補全体は引き続きin-progress、84問題・41補助ケース・12群・147手法の件数は増やさない。通常Linux公開ZIP検証は旧388検査を保持し、新Noh28を加え416 pytestとなる。MUSCLの既存MHD主配布版を保持し、Nohは追加配布先として対応付ける。

未公開r4の独立ZIP再検証は合格したが、既存READMEに初回失敗CSVを未保存とする誤記があった。8CSVが旧r3と同一で残っていることを確認し、説明だけを訂正したr5を公開する。数値revision03の事前契約にある目標r4は当時の記録として保持し、入力・ソルバー・テスト・基準を変更しない。

## 軽量2D Cartesian Noh（2026年11月23日）

追加配布は `code/validated-examples/2026-11-23-r2/noh-cartesian/`、編集用正本は `scripts/depth-noh-cartesian/`。既存Noh r3/r5や他の配布版・固定基準を上書きしない。1D平面/円筒/球を保持し、同じ物理問題nohに新実行例noh-cartesian-2dを対応付ける。全物理問題84・手法147・共通22例は維持し、追加検証は13群42ケース435pytest（旧416+新19）となる。

正方形[-.5,.5]²全域32²/64²/128²で、2成分運動量とx/y面流束を非分割更新する。区分定数Rusanov＋Heun、CFL=.35、初期p0=0。全4辺の流入物理流束は面内解析積分し、時間に一次の流入をHeunで積分する。幾何源・対称境界・半径還元・状態/圧力floor・隠れた再試行は使わない。初期状態はセル中心標本で初期運動量の厳密セル平均ではない。無効段は生の配列と履歴を保存して失敗にする。

19単体検査と49判定は実行前の入力・ソース・受入hashを固定して初回から合格。参照密度は円との交差で分割したCartesianセルの64点Gauss求積で、128点と解析総質量でも確認し、閉形式の厳密セル平均とは呼ばない。ExactPackの固定commit9bacc477eb791e959c9621e771fc7a725db755faによる既存d=2解析点値を再利用し、今回はソフトを再実行しておらず別2D PDEエンジンとの比較でもない。原著Noh(1987)とExactPackソフト論文(2023)・公式コードを別々に引用する。

新しいギャラリー図は実際の2D保存配列。D4偶奇性と連続回転対称性は別で、軸・対角方向の衝撃半径差は3格子で単調には減らず、中心過熱も残る。原点位置ずらし、一般摂動安定性、3D Cartesianや高次精度は未検証。公開前にまとめて索引を更新し、公開後は指定HR URLの図・ZIP・日英と実際の公開ZIPのLinux追試を確認する。

この作業では空き4GiB未満で容量の大きい処理を開始せず、実行中2.5GiB未満で起動したプロセス群だけを中断する。Git各コマンドのgc.auto=0/maintenance.auto=falseで自動圧縮を抑止し、他作業のGit packや一時packは削除しない。

## 軽量Sedov–Taylor爆発（2026年11月23日）

編集用正本は `scripts/depth-sedov/`、不変配布先は `code/validated-examples/2026-11-23/sedov/`。球対称1D有限体積のRusanov＋Heun、γ=5/3、ρ0=1、p0=0、総投入エネルギー1、T=.05。4πを含む体積と投入球のセル交差体積で正規化する。固定投入半径.03の128/256/512セルと、同じ512セルで半径.015の感度計算を区別する。点爆発との誤差には有限投入半径のモデル差が含まれ、傾きを純粋な空間精度次数と呼ばない。感度差も投入半径の連続極限を検証した意味ではない。

入力・受入基準・数値ソース・22 pytestを実行前にhash固定し、初回4計算48判定が合格。状態修復・圧力floor・隠れた再試行はない。質量・エネルギーと幾何源を含む半径運動量の収支を分け、原点・衝撃波を含む誤差と中心値を保持する。冷たい遠方の極小波速で局所CFL比がinfになる警告は記録に残す。全体の実時間刻みは有限で、物理状態を書き換える処理ではない。

参照は独立の自己相似ODE、エネルギー積分による正規化、小さい中心域の漸近接続、衝撃位置で分けた球殻求積による半解析参照。閉形式の厳密セル平均ではない。圧力は数値保存量平均からのp(qbar)と連続物理圧力の平均pbarを比較する。固定ExactPackの選択モジュールを独立実行し、衝撃・中心から離れた点値と半径定数を照合する。元問題・理論はTaylor(1950)、参照ソフトはThrussell–Ferguson(2023)と公式LANLコードを別々に引用し、既知の中心密度評価の限界を保持する。

図は保存済みの球対称1D配列の断面表示で、2D Cartesian計算とは表示しない。物理問題は85、手法147・共通22例は不変。追加配布は14群43ケース457 pytest（旧435＋新22）。旧13配布版・既存84図と固定閾値を保持する。公開成功は指定HR mainのPages/サイト検査、匿名取得ハッシュ、公開ZIPだけのLinux追試で確認する。索引は公開前の明示更新へ集約し、生成中はGit index操作を並行しない。空き4GiB未満で大きい処理を開始せず、実行中2.5GiB未満なら自分が起動した処理を区切って停止・記録する。既存Git packは削除しない。

### Sedov r2：警告をエラーとする公開追試への修正

上記初版はMacで22pytest・4計算48判定に合格したが、公開Linux追試（run45109504662）は22pytest合格後、固定計算の極小波速に対するwidth/speedのoverflowを `-W error` が例外として検出し失敗した。旧 `2026-11-23/sedov/` はそのまま保持する。現行は `2026-11-23-r2/sedov/`。同じCFL条件を逆時間刻みの最大値から評価し、残り時間との比較を先に行って無制限の比を作らない。警告を抑制したり、物理状態・入力・参照・48の受入基準を変更する修正ではない。

r1の契約・数値ソース・実際のLinux失敗JSONを保持し、新しい実行前契約を作る。極小波速・零波速を警告エラー設定で扱う回帰検査を1件加えて23pytestとし、同じ4計算を `-W error` で検証する。全追加配布は14群43ケース458pytest（旧435＋新23）。公開済みr1のライセンスを含むバイト列や失敗履歴を成功に書き換えない。ExactPackの照合は既存実行記録を継承し、今回再実行したと表示しない。

## Double Mach反射の軽量な多格子比較（2026年11月23日）

正本は `scripts/depth-double-mach/`、配布先は `code/validated-examples/2026-11-23/double-mach/`。既存Double Mach問題を拡充し、Mach10・γ1.4・[0,4]×[0,1]・T=.2、セル中心の初期不連続と各RK段の移動上端境界を保つ。64×16/128×32/256×64で両Cartesian流束をHLL＋Heun更新し、各段の密度・圧力、実際の境界流束による全4保存量の収支を確認する。状態floor・修復・隠れた再試行を行わず、不正段の配列・履歴を保存する。

入力・受入条件・初期ソースは20検査前に固定。読み取りレビューで衝撃位置診断の空窓・平坦場へのガードと回帰1件を追加し、初期契約・20成功の記録を保持して21検査の改訂契約を全3格子計算前に固定する。物理ソルバー・入力・数値閾値は変更しない。警告をエラーにする設定で21 pytest・3計算40判定が合格。参照との差は初期射影・境界・離散化と有限参照の差を含み、傾きを厳密な空間次数や細部までの収束と呼ばない。

独立参照は公開RKDGキット不変r2から選択した、別実装のMUSCL（一般化minmod θ1.5）/HLL/HeunによるNy64/128の保存済み実行。元コード・入力・実行記録・ライセンス・ZIPと各ファイルのSHAを保持する。主計算とHLL族/Heunを共有するが別実装であり、新しいAthena/LAVA実行や厳密2D解と表示しない。参照格子の密度/圧力増分と主計算最細との差の比を事前閾値.75と照合する。原著Woodward–Colella(1984)、NASAの設定解説、実際の参照コードの役割を分ける。

参照一覧の種別に numerical-reference（有限格子の数値参照）を追加し、解析解・半解析解・製造解と分ける。旧18件の式データとSPAは変更せず、新カードは専用検証ページへ進める。物理問題85・手法147・共通22例は不変、追加配布は15群44ケース479 pytest。既存14配布物・他84図は保持する。旧Double Mach章には従来基準計算と新検証の違い・追加先を案内し、元のURLを残す。前向きステップと細いwall jetの収束検証は未実施として候補の残りに置く。

新図は実際の2D保存配列。固定壁近傍ROI[1,2.75]×[0,.25]は高速ジェットを含むが、最細でも最大接線速度は主計算約12.64/制限した参照約16.13で未解像性が残る。詳細なジェット・渦の収束や厳密な誤差上界を主張しない。梱包時の独立展開と公開ZIPだけのLinux実行を科学計算/pytestとも-Werrorで確認する。空き4GiB未満で大きな処理を開始せず、実行中2.5GiB未満なら自分の処理を区切って記録・停止する。既存Git packは削除しない。

## 前向きステップの軽量な2D検証（2026年11月23日）

正本は `scripts/depth-forward-step/`、不変配布版は `code/validated-examples/2026-11-23/forward-step/`。既存の物理問題forward-stepを拡充し、[0,3]×[0,1]からx≥.6,y<.2を除く格子整合形状、γ1.4、ρ1.4,u3,v0,p1、T4を固定する。60×20/120×40/240×80の第一次数HLL＋Heunで入口・出口・上下壁・段差の鉛直/水平壁の実際の面流束を同じRK重みで積分し、全4保存量の収支と各段の正の密度・圧力を照合する。状態floor・修復・隠れた再試行・角のエントロピー/エンタルピー補正はない。原著の角補正付きPPM像と同条件とは表示しない。

参照は別のC++17実装によるprimitive MUSCL（一般化minmodθ1.5）/HLL/HeunのNy80/160を新規実行する。通常のPython公開CIは保存した参照配列を使い、C++参照を再生成しない。入力・ソース・参照実行契約は事前固定。初版参照Ny160は120秒上限で停止したため、元ソース・契約・実際の失敗記録・完了したNy80配列を保持する。診断メッセージ引数をconst char*にする性能修正だけを行い、時間上限・数値条件・判定基準は不変。新Ny80は旧配列とビット一致し、改訂Ny160は約65秒で完了。主計算前契約も旧版を残して参照ソースSHAの改訂を説明し、参照配列は別の事前資格確認で結ぶ。

主計算の24pytest・3格子45判定が-Werrorで合格。密度L1差は.14754/.12878/.10265、圧力は.19373/.16015/.12242。参照80/160差は.02636/.03063で、保存量を保守的に制限してから圧力を計算する。主計算の保存収支は最大約2.99e-13。有限格子の数値参照は厳密2D解や誤差上界ではない。全流体領域に角近傍も含め、固定ROIの密度/圧力/エントロピー診断を別に示す。角ROI最小log(p/ρ^γ)は−.0784/−.1224/−.3510と変化する。上流値は約−.4711であり、最小値の低下だけを誤差の悪化とは解釈しない。全流体の密度L∞差は約.5923/.6703/.6649と単調に減らず、角の数値層・すべり線・渦の収束は主張しない。

補助配布は16群45ケース503pytest（旧479＋新24）。物理問題85・手法147・共通22例は不変。旧15配布版・他84図・既存本文URLを保持し、ギャラリー・方程式・手法・数値参照・実行・日英解説と検索を接続する。新図は実2D保存配列で、固体部分を流体として補間しない。索引は公開前の明示更新へ集約し、生成中はGit index操作を並行しない。開始時4GiB、実行中2.5GiBの容量基準を維持し、下回れば自分の処理群を区切って停止・記録する。既存Git packは削除しない。公開完了は指定HR mainのPages/サイトCI、匿名取得SHA照合、公開ZIPだけのLinux再実行で確認する。

## 低Machの等エントロピー渦と空間流束前処理（2026年11月23日）

正本は `scripts/depth-low-mach/`、不変配布版は `code/validated-examples/2026-11-23/low-mach/`。既存isentropic-vortexを拡充する。β3、背景速度(1,.5)、γ1.4、[-10,10]²、背景Mach .1/.01、N16/32/64、T=.1を固定し、RoeとMiczekの12計算を比較する。遠方圧力は|U∞|²/(γM∞²)で、背景Machと局所最大Machを区別する。無制限中央傾きのprimitive MUSCLを両流束に同じように用い、MiczekのP⁻¹|PA|は空間散逸行列だけへ適用する。物理Euler時間はSSPRK33・音響CFL.2で進め、擬似時間反復や定常収束の加速を実装したとは表示しない。

初版は32pytestと12計算の142/143判定に合格し、M∞.01最細の全域圧力誤差.16537が事前基準.1を超えた。入力・受入基準・全配列・実際の不合格・元ソースをattempts/01に保持する。物理入力とacceptance.jsonのバイト列を変えず、両流束へ同じ無制限MUSCLを追加し、再構築面の有限・正の密度/圧力と生失敗状態を確認する。新しい実行前契約・35検査を改訂の実行前に固定する。MUSCLの実際のFourier記号sin(k)(1.5−.5cos k)と.5(1−cos k)²を用いて、SSPRK33の有限個モードと行列冪を調べる。前進Eulerはこの刻みでは通常Roeでも不安定であり、SSP定理・TVD・一般正値性・非線形安定性を主張しない。

改訂は35pytest・12計算143判定が-Werrorで合格。M∞.01/N64の速度L1はRoe.07411/Miczek.01847、渦摂動のセル平均運動エネルギー比は.94563/.99732。全域圧力誤差は.01194/.01260でMiczekの方がわずかに大きく、固定コアでは.04871/.0006325となる。M∞.1の最細速度改善は比.8958と小さく、圧力の一様な改善を保証しない。圧力は大きい熱力学背景値ではなくρ∞|U∞|²（1/2なし）で規格化する。4保存量の周期収支は最大約4.24e-14。主計算は元のMacで約4.4秒。音響/対流刻み比も記録し、物理刻み制限がなくなったと表示しない。

参照は全平面の解析的な等エントロピー渦。保存量のGauss8セル求積をGauss16と比較し、その保存量平均から圧力を求める。閉形式の厳密セル平均や厳密な周期解析解ではなく、有限L20・T.1での周期継ぎ目の微小Gaussian裾を明示する。解析Euler点残差、独立な密行列固有値分解による散逸行列の照合、有限17²モードと冪1/10/100の診断を分ける。Miczek2015の原著行列と滑らかな例の無制限再構築、Barsukow2017の時間安定性の注意、SSPRK原著、NASAの周期渦の注意を確認範囲付きで引用する。新しい参照PDEエンジンは実行していない。

補助版は17群46ケース538pytest（旧503＋新35）。物理問題85・手法147・共通22実行例は不変。低Mach前処理だけを限定した教育用実装に変更し、117教育用・14解説・16予定とする。旧16配布版・他84図・旧KEEP章を保持する。参照カードは23件（解析14・半解析6・製造1・有限格子数値参照2）。ギャラリーの渦度と背景流を引いた速度矢印は実際の2D保存配列の[-3,3]²表示で、全計算領域は[-10,10]²。全域の圧力誤差と初版不合格の図も同梱し、コア図で遠方誤差を隠さない。長時間・一周期、衝撃波、Mach→0極限、定常反復加速は検証外。

公開前の明示prepare-indexesと全Node検査、指定HR mainへの公開、日英・390px・図/ZIPの匿名SHA照合、公開ZIPだけのLinux再実行までを確認する。容量基準は開始時4GiB・実行中2.5GiBを維持し、下回れば自分の処理群を区切って停止・記録する。既存Git packは削除しない。

## Guderley収束衝撃波の軽量な球対称検証（2026年11月23日）

正本は `scripts/depth-guderley/`、不変配布版は `code/validated-examples/2026-11-23-r3/guderley/`。新しい物理問題guderleyを1件追加する。γ1.4、球半径r∈[0,.75]、Rs(−1)=.6、t∈[−1,−.85]、128/256/512球殻、CFL.4を固定する。衝撃波の内側は冷たい未衝撃気体ρ1・u=p0、外側には初めから衝撃後の相似場がある。球殻面積・体積による区分定数HLL流束とHeun更新を使い、実際の外側HLL流束と半径運動量の圧力幾何源を同じRK重みで積算する。

半解析参照はExactPackの固定commit `9bacc477eb791e959c9621e771fc7a725db755fa` のeexp・ramsey.g/stateを実際に使う。ソース・SHA・BSD3ライセンスとソフトウェア論文の引用を保存する。今回のdense評価器は同じ相似ODEの収束前分岐に限定した適応で、元のstate8点との照合、λ表値、臨界点の位相差、RH条件、衝撃位置で分割したGauss16/32球殻平均の8検査を別の事前契約・60秒上限で実行済み。λ=1.3943607844230872、α=1/λ≈.7171745012。物理Lazarus時間と公開wrapperの時間変換、半径.6の規格化、p(保存量平均)と圧力平均を区別する。Ramsey2012・Lazarus1981・Chisnell1998・ExactPack2023と固定ソース、歴史的Guderley1942の出典確認範囲を明記する。

主計算の入力・受入条件・19科学ファイルのハッシュ、33pytest・3入力55判定を実行前に固定。単体検査後に契約の説明文にあった語句だけを明確化し、旧契約を保持した。19科学ハッシュ・入力・公差・検査数・数値条件は不変で、現契約に単体検査後・PDE前の説明改訂であることを記録する。33検査と3格子55判定が-Werrorで合格し、参照固有値の新規構成を含む全3格子はMacで約45秒。密度L1は.023454/.013387/.007722、圧力L1は.032769/.017432/.009477。全3保存量の収支は最大約8.85e-16。状態floor・修復・再試行はなく、冷たい気体の音速平方根に関する丸め帯のガードも実測0回。一般の非線形正値性の証明とは区別する。

衝撃位置は固定窓内の圧力差分ピークによる有限格子診断。最終誤差は1.134/2.268/2.536セルで単調には減らず、物理長さでは約.00665/.00665/.00372。L∞と履歴も保存し、原点到達・反射後・一般EOSや2D摂動の収束へ結果を拡張しない。ギャラリーの2次元図は実際の1次元球対称保存データの中心断面表示。公開の軽量追試は18群47ケース571pytestとなり、旧17配布版・1998codeファイル・85図と共通22例を保持する。物理問題86・手法147を数える。空き4GiB未満で大きな処理を開始せず、実行中2.5GiB未満なら自分の処理を区切って停止・記録する。既存Git packは削除しない。

最初の非公開ZIPは科学検査に合格したが、解説用メタデータの`validation_limits`が公開側の必須項目`limits`に対応しておらず、公開前の読み込み検査で停止した。このZIP全体は作業フォルダの`outputs/atlas-guderley-2026-11-23/unpublished-package-01/`に保持する。初回公開版は`2026-11-23-r2`とし、説明用キー名を修正した。数値ソース19ファイル・入力・判定は不変。梱包処理に公開用メタデータの先行検査と回帰検査を追加し、科学計算の前にこの種の不整合を検出する。

r2の公開後Linux追試は33pytestが96.3396秒で全合格し、続く本計算がグループ共通120秒枠の残り23.3121秒で停止した。r2を不変のまま保持し、r3へ計算時間の修正を加える。元のeexp計算・8点の原評価器照合・ソース12件・契約をreferences/attempts/01-eigenvalue-recomputeへ保持し、既に計算したλをSHA付きで再利用する。生きた元ライブラリ10ファイルも旧ハッシュと照合する。相似ODE・Gauss求積・Euler残差は毎回新規に評価し、全固有値探索は`python -W error -m references.qualify_reference --recompute-eigenvalue --output new-full-reference-qualification.json`として分ける。

r3の新しい事前契約・参照再確認6項目・主計算44ファイルの契約を検査前に固定。参照の軽量照合は約.04秒、33pytestと全3格子55判定を同じ120秒枠で続けた実行はMacで約.912秒。入力・受入条件・Eulerソルバー・run.pyはr2とバイト一致し、全3格子の初期値・最終値・参照値・保存履歴の配列もr2とビット一致した。失敗したLinux記録・contextと旧契約はattempts/02に保持する。アーカイブされたPythonはmanifest/ZIPで保持し、references/attempts以下も現行コードの案内から除く。

## Euler二重膨張波の段階正値性（2026年11月23日）

正本は `scripts/depth-euler-positivity/`、不変配布版は `code/validated-examples/2026-11-23-r2/euler-positivity/`。既存の物理問題 `double-rarefaction` を拡充し、物理問題86・手法147・既存の参照カード24・共通22実行例と、従来86問題の主画像を保持する。新しい実行例は `euler-double-rarefaction-positivity`。γ1.4、左右(ρ,u,p)=(1,−2,.4)/(1,2,.4)、[0,1]、x₀=.5、t=.15、128/256/512セルを固定する。中心には小さい正の密度・圧力があり、真空を生成する別の初期値や強爆風を実行したとは表示しない。

保存量の無制限線形MUSCL再構成を、平均を保つ共通係数で密度・圧力の許容集合へ縮小する。共有する大域Lax–Friedrichs流束のa=4、CFL=.4、SSPRK(3,3)を接続する。P1端点の重み1/2による十分条件aΔt/Δx≤1/2と、全ての実際の再構成面の|u|+c≤aを区別して検査する。各前進Euler候補とSSP凸結合の平均・面状態・保存収支、実際の縮小回数、生の不許容再構成、floor・retry・棄却数を保存する。ε=1e−13は再構成の目標であり、セル平均への質量・エネルギーの注入ではない。固定検査は27pytestと3格子73判定。事前契約の入力・受入条件・科学コードを実行前に固定し、公差を緩めない。

参照は対称な非真空Riemann問題の閉じた星状態と希薄波ファンから別に実装した評価器で、ファン境界ごとに分割したGauss8/16保存量セル平均を比較する。元の不変Numartの対数根探索によるRiemann評価器との照合とEuler点残差も保存する。これは独立PDEエンジンの実行ではない。Zhang–Shu2010の正値性理論・SSP原著・固定入力と評価器の出典役割、実際に確認した節と未読部分を明記し、ExactPackを実行したという表示は付けない。

ギャラリーは従来の二重膨張波の主画像を残し、同じカードに追加の時空間密度・圧力図を表示する。2次元の絵は保存した1次元計算のx–t場で、2次元Euler計算ではない。`gallery_figure` は `additional_figures` に登録され、配布版manifestのSHAとPNG構造・日英キャプションを確認できた図だけを選べる。通常refreshは画像を再計算しない。新しい図から検証ページ・手法・Euler式・既存参照・コードへ接続し、旧図・参照値・旧配布版を置き換えない。

従来のadvanced-limiters章は元Numart配布版の部品検査という範囲を明示し、別配布の1次元Euler段階更新へ案内する。FD WENO、DG発展、MHD、CT／GLM、KEEP、一般EOSの完全離散正値性やTVD・エントロピー安定性は今回の保証に含めない。現在の補助版は19群48ケース、全pytestは旧571＋新27の598となる。公開前の明示prepare-indexes・全Node検査・匿名図/ZIP取得と公開ZIPだけのLinux追試を確認し、hrkoyama/hrkoyama.github.ioのmainだけへ反映する。容量は開始4GiB・実行中2.5GiBの基準を維持し、下回れば自分の処理を停止して記録する。

初回ローカル実行は27pytestと3格子73判定に合格し、共通120秒枠に対して合計約1.94秒。独立展開ZIPも27検査と全入力を再実行し、runnerは約1.21秒だった。密度L1は.05275/.02773/.01379、圧力L1は.04606/.02697/.01436。全記録のSSP平均の密度/圧力は正、再構築の正値性スケーリングは各格子6セル・段で発動、θ最小約.44949、全端点の最大|u|+cは約2.7712<固定a4。境界収支の最大相対残差は約4.79e-15。真空・TVD・一般の高次法の保証は主張しない。バックログはローカル検証済みと公開確認済みを分け、実際の公開URL・Linux追試成功後にpublishedへ進める。

初回の未公開ZIPは科学計算27テスト・73判定には合格したが、全サイト検査で公開verifierが要求する3依存pinのうちSciPyの指定が欠け、数式表示とギャラリー件数にも不整合を検出した。未公開版全体・検査ログ・元契約を作業記録とattempts/01へ保持し、r2に分離する。requirementsへ既定のSciPy1.14.1を明記し、説明用KaTeX式と件数を修正。入力・受入基準・ソルバー・参照・27テストは不変で、改訂前後の3格子の初期/最終/参照/時空間配列はビット一致。改訂の再実行前契約を固定し、27検査と73判定は合計約1.485秒で再合格した。梱包時にも3依存pinを科学実行前に検査する回帰ガードを追加した。

科学内容commit 1c5302913560376997cfd3df06bb684bf71330dfのPages・Public site checks・公開ZIPのみLinux run45142681101が成功。公開517ファイルを匿名SHA照合し、実際のギャラリー新図→実行入口と390px表示も確認した。公開成功記録は`numerical-methods-atlas/validation/verification/2026-11-23-euler-positivity-public.json`。この実績を確認してから候補sequence11をpublishedに進める。記録は当該科学内容commitの成功であり、後続の台帳更新commitの成功を予告したものではない。

## Zalesak型2D回転輸送（2026年11月23日）

正本は `scripts/depth-zalesak/`、不変配布版は `code/validated-examples/2026-11-23/zalesak/`。新しい物理問題 `zalesak` と実行例 `zalesak-rotation`、2次元スカラー保存則 `rotational-advection`、解析参照カードを追加する。従来86問題・19補助配布版・24参照カード・共通22例・全147手法の状態と古い図・入力・結果・受入基準を保持する。更新後は87問題・25参照・47方程式、補助20群49ケース、公開実行入口47問題となる。新しい手法を増やすのではなく、既存のupwind・MUSCL・minmod・SSPRK(3,3)へ専用の実行例を接続する。

原問題の文献はZalesak(1979)、具体的な正規化した形状・剛体回転の照合元は公式Firedrake DG advection demoを区別する。[0,1]²、速度(.5−y,x−.5)、角速度1、周期2π、中心(.5,.75)・半径.15の円盤から.475<x<.525かつy<.85のスロットを除く。内部1・外部0の切り欠き円盤だけを運び、公式例のbell・cone・背景1・DG・流入条件を再現したとは表示しない。Zalesak1979全文や元の数値実験の完全監査、Firedrake実行、Zalesak FCTアルゴリズムの実装とも区別する。

計算は与えた速度による真の2次元スカラー有限体積輸送で、Euler方程式ではない。一次風上とminmod MUSCLを同じSSPRK(3,3)で比較し、全段の範囲と共有面流束による保存収支を記録する。法線速度は対向周期面で一致するが、接線成分の継ぎ目は滑らかな周期速度とは扱わない。連続解のコンパクトな台は境界から離れ、数値的な裾の境界量を別に測る。解析的な逆剛体回転と円盤・多角形の面積積分による保存量セル平均を参照にし、点値画像や別のPDEの細格子解と混同しない。3格子の各2手法と、64²での半セル位置ずらし・π/4初期形状角の診断を固定してから実行する。

ギャラリーの新しい主画像は実際の2次元保存配列による初期・一回転後の比較とし、従来86枚の主画像を再描画しない。専用配布版のmanifest、入力・結果・検証記録とPNGのSHAを照合し、プレビューmanifestの変更した出典だけを実際の保存比較に基づいて更新する。図・方程式・手法・参照・コード・解説章・検索の日英HTML/JSON/Markdownは通常の公開前prepareで生成する。バックログは実装中→ローカル検証済み→実際の公開URL/ZIP/Linux成功確認後に公開済みと進める。容量基準は開始4GiB、実行中2.5GiB。既存Git packを削除せず、自分の大きな処理は容量監視の下で行う。

初回の32²/64²/128²・8計算は26pytestと156/158判定に合格し、全段の範囲・保存・四分の一回転の検査も合格した。しかし最細N128の相対L1は一次風上約1.11675（事前基準1.0）、MUSCL約.6023（事前基準.55）で不合格だった。初回ソース・全8保存配列・ログ・実際の不合格を`attempts/01`と作業記録へ保持する。公差・受入条件・流束ソルバー・26検査は変更せず、改訂を実行する前に基準系列を64²/128²/256²へ細分化した新しい入力と契約を固定する。64²の半セル位置ずらし・π/4初期角度診断は不変。図とdriverは入力・保存記録の最大Nを選び、最細128を固定しない。

改訂2は26pytest・8計算158判定がすべて合格し、テストと本計算の合計は同じ120秒枠に対し約19.583秒。N256の相対L1は一次風上.932255798、MUSCL.394271052（比約.423）、最大質量変化は約8.90e-15だった。流束・受入基準・26テスト・幾何学的評価器は初版と同一。全段の記録最小/最大は0/1だが初期状態も含み、状態のclip・retry・棄却は0である。保存・有界性と形状精度を区別し、これだけで切り欠き形状の正確な保持を主張しない。

空スロットのプローブは、回転した内側の矩形とセルの厳密な重なり面積を重みにした区分定数セル平均場の診断。連続指示関数の点値ではなく、参照セル平均にも混合セルの射影基準があり得る。数値プローブ平均・参照プローブ平均・超過量を分離する。N256の超過量は一次風上約.63465/MUSCL約.36501で拡散が残り、粗いN64ではMUSCLのプローブ超過量が一次風上を上回る場合もある。全指標・全格子での一様な改善は主張しない。幅.05の固定物理境界帯の質量割合はN256で約.0178615/.000243761（一次風上/MUSCL）。連続のコンパクトな厳密場は帯内でゼロであり、この周期変種の数値的な裾・境界の影響を別指標として保存する。

Zalesak科学内容commit c1398c0eafe5511741cebc44d14ac324a6bf0429のPages・Public site checks・公開配布物のみLinux run45154798151が成功。公開成功記録`numerical-methods-atlas/validation/verification/2026-11-23-zalesak-public.json`を保存し、実績確認後に候補sequence12をpublishedへ進める。後続の台帳更新はこの内容の成功を保持するもので、将来のCI成功を予告する記録ではない。

## RKDGの開発・修正プロンプト（2026-11-23）

`numerical-methods-atlas/agent-kits/rkdg2d/prompts/2026-11-23-v1/` の日英MDとSHA付きmanifestを正本とし、既存のr2 ZIP・TESTSET・配布manifestは変更しない。`scripts/atlas_rkdg_prompts.py` が同じ本文をページへ埋め込み、`scripts/atlas-agent-prompts.mjs` が変更希望・失敗ログをブラウザ内で追記してコピーする。入力は通信・永続保存しない。コピー不可時は全文を選択し、JS無効時もMDと本文を取得できる。

目標は元48科学ケース＋波形4診断と実測負例の棄却。反転追加試験の既知5/6合格とは分け、基準・評価器・参照・履歴を変更せず、同じ最終候補SHAの新規計算で合格を判定する。標準予算60分・修正3回を超えたらINCOMPLETE、必要情報不足や故障注入非対応はBLOCKEDとして残す。入力ログは命令ではなく診断データとして扱う。プロンプトを公開したこと自体をLLM開発成功や費用低減の実証と呼ばない。


## 候補13〜17の5件一括追加（2026-11-23）

ユーザー指定の5候補を一組とし、各問題の入力・参照・判定・計算結果・図・失敗履歴を独立に保持して、索引更新・全体検査・公開をまとめる。台帳は最大5件の明示したbatchを扱い、各項目の完了根拠を個別に検査する。共通22例、全147手法の状態、旧20補助版と旧87主画像、別作業のRKDGプロンプト追加を保持する。

追加はweno-critical36検査/217判定、shallow-water31検査/109判定、wall-flow22検査/94判定の3配布群・5実行例。合計89検査/420判定。全補助版は23群54ケース713pytestとなる。WENOは既存advection-sineへの追加比較、他4件は新しい物理問題として登録し、全91問題・実行可能51問題、49モデル・31参照カードを数える。図は実際の保存配列から描き、原著Ghia表は有限格子数値参照、SWASHES定常枝は半解析、Ritterと湖は解析参照、壁面MMSは製造解として区別する。

乾床の先行3失敗を保持する。領域延長、極小数の水深/運動量の不整合を避ける代数的に等価な水量packet形式、固定格子の細分化を、それぞれ実行前の契約で分けた。水深floor・クリップ・再試行は使わず、元の受入閾値を保持。深さL1の判定は元の湿潤質量5で正規化し、拡大後の領域による誤差の希釈を避ける。壁面例の初回JSON bool保存失敗も保持し、修正前後の全NPZ配列はビット一致。MMS圧力は別のDirichlet演算子検証で、キャビティ圧力の検証とは扱わない。選んだWENO第一臨界多項式ではJS/Zとも局所約5次で、Zの先頭誤差低減と高次臨界点の診断を区別する。

全公開はhrkoyama/hrkoyama.github.io mainのみ。実際の公開URLと配布物だけのLinux成功確認後に5項目をpublishedへ進める。

公開前の全体検査でwall-flow結果の終了理由・上位ケース判定の形式不足を検出。未公開2026-11-23版全体を作業記録へバイト照合して保持し、公開版を2026-11-23-r2へ分離した。出力形式と回帰検査だけを修正し、数値入力・受入基準・ソルバー・全NPZ配列・PNGは保持する。梱包処理も実際の公開verifierと同じ結果形式検査を使い、同じ欠落を梱包前に拒否する。

## レベルセット法とVOF比較・軽量2D円の移流（2026年11月23日）

基本解説の正本はcatalog/atlas-detailed-reading.jsonのlevel-set、編集用コードはscripts/depth-level-set/、不変配布版はcode/validated-examples/2026-11-23/level-set/。レベルセット法を限定した教育用例、VOFを比較解説のみとして追加する。149手法（教育用118・解説15・予定16）、48方程式、88物理問題、27参照カード。円の平行移動と偏心剛体回転は同じlevel-set-circle問題の2条件として数え、共通22実行例は不変。補助配布21群51ケース646pytest（旧624＋新22）。旧20配布物・87主画像・旧参照データ・成功履歴を保持する。

全変数無次元、単位正方形、r.15、T1、N32/64/128、ENO2片側差分＋Heun、max(|u|+|v|)dt/dx≤.35。解析値は各RK段の外側2層だけへ指定し、内部は数値更新する。移流単独と、物理.1ごとの5段Godunov再初期化（dtau=.3dx）を比較する。体積補正・ゼロ界面投影・clip・retryはない。0/.25/.5/.75/1の辺上ゼロ交差半径誤差、三角形区分線形phiの面積と初期偏り、距離勾配、各再初期化面積ジャンプ、N64のCFL半減を保存。辺の標本誤差をHausdorff距離、dxとdtの同時細分化を純粋な空間次数と表示しない。二相流・曲率流・VOF・合体分裂は実装検証の範囲外。VOFの保存と有界性も区別する。

入力・ソース・22検査の契約を初回数値実行前に固定。初回の全本計算は約7.22秒で全20判定に合格した。最初のpytestは21/22で、速度と半径の内積をゼロと比較する絶対2e-16が1ulpの残差2.220446e-16より小さかった。元テスト・契約・実ログをattempts/01-testsへ保持し、その単体検査だけを積の大きさに応じた4epsilonの丸め誤差上界へ修正する。数値ソース・入力・生産計算の受入条件は不変で、改訂22検査が合格。初回の成功指標・入力SHAと変更理由はprotocol-history.jsonに残す。

通常の再生成では保存ソース・結果・図・ZIPのSHAを照合するだけで、科学計算を起動しない。事前の明示索引更新、全Node検査、日英・狭幅の表示、実際のpush先と配信URLを確認してHR mainへ公開する。公開後は対象本文・図・全配布物の匿名照合、公開ZIPだけのLinux実追試と結果取得までを完了条件とする。容量基準は開始4GiB・実行中2.5GiBを維持し、既存Git packは削除しない。


## 同時期のLevel Set追加と5候補の統合

公開mainの`11ba7a20076f052a569091ef976217f07341c3ba`が持つLevel Setの2ケース・22検査と、候補13〜17の5ケース・89検査をともに保持する。統合後は補助24群・56ケース・735 pytest、物理92問題（実行入口52）、50モデル・33参照・149手法となる。今回5候補の固定数値判定は420項目。旧2328保護ファイル・87主画像に加え、同時期のLevel Set配布版と実装45ファイル・主画像のレコードも保持する。保存図は再計算せず、プレビューは92件・248出典ハッシュへ接続する。

ローカルの`8f069f5913a70d0b0222e58b4064ff262c4ebffc`は非fast-forwardでpushが拒否されており、公開成功の根拠にしない。統合後の科学内容commitに対し実際のPages・サイト検査・匿名HTTP・公開ZIPのLinux結果を確認してから候補13〜17を公開済みにする。統合による索引再生成は別の入力状態に対する公開前更新であり、同一状態の定期的な再生成とは区別する。

## スペクトル要素法とFR法の軽量な比較（2026年11月23日）

基本解説の正本はcatalog/atlas-detailed-reading.jsonのspectral-elementとflux-reconstruction。編集用コードはscripts/depth-sem-fr/、初公開の不変配布版はcode/validated-examples/2026-11-23/sem-fr/。SEMとFRを独立した教育用例の2手法として追加し、既存P1 FEM・modal DGの公開ソース7ファイルをバイト一致で同梱して実際に比較する。PyFR・Nek5000・nekRSは公式資料に基づく関連実装の紹介であり、本体の導入・実行・性能測定を行った表示にしない。

SEMは零Dirichletの単位正方形、u=sin(πx)sin(πy)、f=2π²u。アフィン正方形・C0のLegendre GLL求積SEMでp2の2/4/8要素を実行し、既存三角形P1 FEMの4/8/16分割と自由未知数9/49/225を揃える。別に2×2要素のp1〜6を実行。GLL節点の誤差画像と、別の高次Gauss点で積分する連続L2/H1半ノルムを区別する。L2観測次数はSEM約3.04、P1約1.97。225自由未知数でのL2は約2.49e-4と5.38e-3。要素・求積・代数ソルバーの違いを明記し、速度・汎用的優位性を主張しない。

FRは1D周期の0.4+sin(2πx)、a1、T.25、p1/2、8/16/32セル、Gauss解点・Radau補正・上流流束・SSPRK3。初期L2射影と時間刻みを既存DGと揃えた限定した同値設定を検証し、全FR/DG・非線形・衝撃波・多次元へ広げない。連続L2観測次数は約1.99/3.00、既存DGとの差は約4e-15、段階質量変化は約3.6e-15。同じ空間行列の指数作用とRK3を比べ、刻み半減の時間誤差比は約.125。指数作用は独立した空間PDEソルバーではない。

入力・受入基準・ソースを初回実行前に固定。最初は密行列指数が有限の行列に対してRuntimeWarningを発し、24検査中23が合格。全元ソース・途中SEM場・ログ・診断をattempts/01-dense-exponentialへ保持し、同じ空間行列の指数作用をexpm_multiplyで評価するよう修正した。続くJSON保存でNumPy boolの型を検出し、元ソース・両方の実計算配列・ログをattempts/02-json-boolへ保持。判定スカラーのPython bool化と、実際の全driver出力検査を追加。元の入力・全数値受入基準は不変で、修正前後のNPZ配列はビット一致。25検査・全20数値判定と、独立展開ZIPの全入力再実行が合格した。

151手法、50モデル、92物理問題、35参照カード、補助25群58ケース760pytest。2つの新しい実行例は既存poisson-2d-sineとadvection-sineへ結び、問題数・元の92主画像を増やさない。追加プレビューは新しい保存データのみから描く。旧24配布版・既存コード・参照値と成功履歴、共通22実行例は保持する。今回の新しい内容・一覧・検索を公開前例外として一括stage後に明示prepareし、成功日時・対象tree・ログは非公開キューへ記録する。通常の生成では科学計算せず保存SHAを照合する。HR mainへの公開後は本文・図・全配布物を匿名取得し、実際の公開ZIPだけを使ったLinux追試レポートを取得・確認する。公開後の状態ラベルだけの再生成・再公開は日次集約の方針に従い保留できる。

## RKDGの実測した組み立て・修正プロンプト試験（2026-11-23）

正本は `catalog/atlas-rkdg-pilot.json` と不変結果版 `/code/rkdg2d/2026-11-23-pilot1/`。既存r2キット・MD・プロンプトv1を変更しない。`scripts/atlas_rkdg_pilot.py` が実測結果の日英HTML/Markdown/JSONを生成し、既存キット入口から接続する。各課題1試行、日本語テンプレート、組立2修正・2949.834583秒、注入欠陥の修正1回・2866.545312秒。各候補が元48科学行・波形4・負例棄却に合格し、各49配列から240指標を再照合。所要時間は共有Macでの準備・実装/修正・新規計算・検証込みであり、料金やモデル速度比較ではない。金額・課金トークン・正確なモデルIDは未取得。低価格モデル・アトラスなしとの比較や成功確率の一般化はしない。

公開ZIPは候補コード・指標・配列・固定判定を同一バイトで保持し、作業パスを除いたJSON/ログは変換と元ハッシュを記録する。初回の監督側時刻ログ照合失敗と既存4eps終端仕様への修正、参照remap警告と別加算経路の一致も保持する。ポスターの非公開QRや原稿は公開物へ入れない。公開後CIはbaseキットと結果ZIPを匿名取得し、保存データだけを再判定する。新しいAI生成や49本のPDEの再実行と呼ばない。実MPI・他言語PDE・量子計算は追加しない。

Linuxの追加照合v2は相対64epsのみのため24指標を不一致としたが、元48・波形4の固定科学判定は合格していた。最大絶対差は2.3527187142935446e-16。初回run 45170855021 と公開 `evidence/linux-audit-v2-failure.json` を保持する。元pilot ZIPは変更せず、別版 `/code/rkdg2d/2026-11-23-pilot-audit3/verify_saved_portable.py` をSHA固定で追加する。v3は非ゼロの無次元指標の整合性照合だけに絶対64eps床を加え、記録ゼロは完全一致を維持。科学判定基準・ソルバー・配列・指標記録・参照値は変更しない。公開用verifierは両候補を最後まで確認し、不合格でもレポートを保存する。

候補13〜17の最初の科学内容commit a51543e8b54129e70670e184290c9b50b5bc0645について、同じSHAのPages・Public site checks・公開配布物のみLinux run45167465669（https://github.com/hrkoyama/hrkoyama.github.io/actions/runs/45167465669）が実際に成功。匿名HTTPで1048ファイルをSHA照合し、Linuxの24群56ケース735pytestを確認した。追加3群はweno-critical36検査/217判定、shallow-water31検査/109判定（静水・地形定常62、乾床47）、wall-flow22検査/94判定（キャビティ35、MMS59）、合計89検査/420判定。3ZIPのSHA・実際のLinux report SHA・run URL・HTTP件数を`numerical-methods-atlas/validation/verification/2026-11-23-batch13-17-public.json`に固定し、確認後にsequence13〜17だけをpublishedへ進めた。元の配布版verificationはreferencesに保持する。この記録は当該科学内容commitの実績であり、後続の台帳・索引更新コミットのCI成功を予告するものではない。現在の5件単位と次回10件の利用者指定を分け、progress.jsonのnext_batch_size=10を保持した。


## 候補18〜27の10項目をまとめる運用（2026-11-23）

今回の10項目は5配布群・13実行例。固定入力・参照・受入基準を実行前に記録し、問題ごとの検証と保存図を揃えてから索引・全体テスト・公開を一度にまとめる。共通の22実行例、旧24補助版の56ケース・735pytest、旧92主画像と全既存配布物を保持する。追加はinstability-growth22pytest/74判定、mhd-transport47/125、mesh-boundary20/174、moving-waves19/98、relativistic25/110。追加計133pytest/581判定、別作業で追加されたSEM/FRの1群2ケース25pytestも保持し、公開時の合計は全30群71ケース893pytestとなる。

非一様ALEスカラー輸送と平面C格子の回転浅水波は今回の公開段階。Saltzman圧縮性ピストンとWilliamson球面問題は未実装として台帳に残す。相対論は1Dで、保存場のx–t図を2D流れと呼ばない。初期成長率の独立線形参照を完全非線形厳密解と混同しない。MHDの独立Athena++参照は最終時刻で比較し、実際の途中出力時刻と資格判定の訂正履歴を保持する。macOSのBLAS警告による失敗は、警告抑制を使わない同値な演算経路の比較・改訂履歴として保持する。SRMHDの最粗格子不足は閾値を維持した格子細分化で区別する。

公開用の版・SHAを固定し、外部Linuxの公開ZIP追試中は次セットの設計・出典確認・準備を非公開キューと別作業場所で進める。Linux追試・公開URL検査が終わるまで次の公開と索引更新を重ねない。公開確認だけのラベル変更・取得証明の反映案は非公開に記録し、次回の集約更新へ繰り越す。進行中の実装・次回候補の記録を公開サイトへ同期しない。公開先は引き続きhrkoyama/hrkoyama.github.io mainだけ。

公開追試器の全経路テストで、KH/RT初版のCSV出力欠落を検出した。元の不変版を保持し、数式・入力・公差・22検査を変えずにCSV書出しだけを加えた2026-11-23-r2を有効版とした。10NPZ・110配列・74判定・全ケース指標は元の版とバイト／値一致。包装時にも実際の公開CSV検査を適用し、出力欠落を公開前に拒否する。


## 候補18〜27の実公開確認（2026-11-23）

科学内容eccf88dffa59ae96d7c037dab74a597845dbd055、最終408a2279cc6ed1f4b9325888a66c496e937cbde9をHRmainで公開し、1200公開ファイルの匿名SHA照合、日英・狭い画面・図からコードへの操作、公開ZIPだけのLinux893pytest/30群71ケースが合格した。サイト全530テストも合格。最初のCIの模擬検査ホスト30秒制限を、判定・科学予算を変えず120秒へ限定修正した。成功後の同一版の自動重複Linuxだけを停止した。詳細は /numerical-methods-atlas/validation/verification/2026-11-23-batch18-27-public.json 。

Linux実追試中に次28〜37の10候補を非公開で設計・独立レビューした。文献整理1候補と科学9候補を分け、数値実行0、実行時間未測定、入力・参照・基準の契約は未固定。実行前の修正点と続きは非公開キューが正本。この公開確認ラベル案は、次回の集約索引更新まで私用フォルダで保持する。
