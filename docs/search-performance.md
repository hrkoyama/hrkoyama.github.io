# 初回検索の性能検証

固定条件の合成負荷で初回操作を測る。実スマートフォンや実利用者の速度保証とは区別する。数値ソルバー・独立参照・配布ZIPは再実行・再包装しない。

- 対象：日英それぞれ、ホーム検索とアトラス範囲の全体検索。固定語は `Sod test`、各3回、計12標本。390×844px、1 worker、再試行なし。
- ブラウザー：既存lockfileのPlaywrightと対応Chromium。Linux runnerのCPU型・OS・Node・ブラウザー版・入力commit・測定treeを各標本へ保存する。
- 条件：新しいcontext、HTTP cache無効、service worker禁止。移動前から全要求へ下り1.6Mbps・上り0.75Mbps・最小ヘッダー遅延150msを適用し、CPU速度を4倍のslowdownへ設定する。これはCPU使用率4倍という意味ではない。
- 時間：移動開始→検索入力可能、DOMのinput/submit→先頭結果が操作可能、移動開始→結果まで。候補URLの正しさ・クリックのactionabilityと2描画frameを確認する。
- 内訳：実際のencoded/decoded body、索引転送時間、受信→JSON利用可能、JSON利用可能→結果、long taskを残す。後二者は複合区間で、解凍・解析・検索・描画それぞれの厳密なCPU profileではない。計測用fetch timingとobserverの小さな負荷も含む。
- 集計：全標本と最小・中央値・最大。3回から安定したp95や利用者全体の速度を主張しない。測定前の根拠のない速度合格値は設定しない。12標本・正しい結果・同一索引SHA・通信/ページエラーなし・スキップなしを確認する。

候補は `scripts/serve-atlas-gzip.py` のloopback fixture、公開後は **https://hrkoyama.github.io/** のCDNを使う。候補fixtureは主要HTML・索引・言語文書の圧縮cacheを先に用意するが、ブラウザーは毎回cold contextにする。OSのdisk cacheまでcoldにする試験ではない。公開側は測定前に、このcheckoutの主要6資産とのSHA一致を待つ。

`npm run test:search-performance` は通常の `test:browser` と別の設定。`ATLAS_PERF_TARGET=published` が公開側、それ以外の既定は候補fixture。結果は `test-results/search-performance/`、集計は `node scripts/summarize-search-performance.mjs`。失敗時の標本・traceもworkflow artifactへ保持する。

`Atlas cold-search performance verification` は定期実行しない。関連変更のmain pushでは公開版を測定する。候補ブランチでは明示dispatchかcommit中の `[atlas-search-measure]` で測定する。全索引生成まで必要な場合だけ `[atlas-search-build]` または `candidate-build` を明示指定し、生成ログ・入力tree・出力tree・patchを別に保持する。通常コミットごとの全再生成には使わない。ローカル容量不足時も、公開前に生成treeと取り込むpatchを照合する。

使用APIは [Playwright CDPSession](https://playwright.dev/docs/api/class-cdpsession)、[DevTools Network](https://chromedevtools.github.io/devtools-protocol/tot/Network/)、[DevTools Emulation](https://chromedevtools.github.io/devtools-protocol/tot/Emulation/) を参照する。計測は独立したテストcontextで行い、訪問者向けJSへの計測・送信機能は追加しない。
