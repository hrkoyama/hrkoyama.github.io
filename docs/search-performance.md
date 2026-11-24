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

## 容量制約時の候補生成と取得

[運用追記前の文書（旧全文保存版）](search-performance-before-remote-generation-2026-11-24.md)を同じdocs階層に保持しています。以下は容量制約時の運用追記です。

[既存workflow](../.github/workflows/atlas-search-quality.yml)の `candidate-build` は、非main候補で標準の `prepare-indexes.py` を一回実行し、生成差分をstaged treeへ含めた状態で12標本を測る。`candidate` は生成せず候補を測り、`published` はmainの配信版を測る。ローカルの全snapshot作成を避けるための経路であり、科学計算・図・配布ZIPの再生成stageではない。

公開先・他作業のlease・固定source SHA/treeを確認し、検証対象のHR `codex/` 候補をpushした後、既存runとの重複がないことを確認して明示dispatchする。次は既に`gh`を使える環境での操作例で、refは実際の固定候補へ置き換える。認証情報をコマンド・ログ・ファイルへ書かない。

```sh
gh workflow run atlas-search-quality.yml \
  --repo hrkoyama/hrkoyama.github.io \
  --ref codex/reviewed-candidate \
  -f target=candidate-build
```

同じ操作のAPIは `POST /repos/hrkoyama/hrkoyama.github.io/actions/workflows/atlas-search-quality.yml/dispatches`、入力は `ref` と `inputs.target: candidate-build`。担当者がどちらか一方を一回だけ使う。容量確認やartifact取得のhelperからdispatchしない。

完了した同source SHA・ref・run attemptの `atlas-cold-search-…` artifactから、生成メンバーだけを選ぶ。格納名は通常 `search-quality-build/{generation.json,prepare.log,generated.patch}` で、先頭の `test-results/` が付く場合や単独名の場合もあるため、実際のZIP directoryを読み、候補が重複したら拒否する。全artifact ZIP、全trace、全画像は保存しない。

- `generation.json`：`passed`、`source_commit`、`input_tree`、`output_tree`、`changed_paths`、patch/logのSHA-256と実生成時刻を保存する。sourceのSHA/treeが手元のclean候補と一致しなければ適用しない。
- `prepare.log`：小さいログとして保存し、`log_sha256` と照合する。失敗runのログも成功に付け替えない。
- `generated.patch`：ZIPメンバーのCRCと、復号したpatchの `patch_sha256` を確認する。streamでgzipへ保存すれば、大きなZIP本体・raw patch・別checkoutを追加する必要はない。全artifactのSHAを取得済みとは主張せず、取得メンバーと転送量を記録する。

差分は既存の生成物だけかをreviewし、科学 `code/`・ZIP・科学ソース・私用記録を含めない。適用前に残り容量と追加量の予算を確認する。圧縮ファイルが小さくても、生成物・Git blob・一時indexの容量は別に要る。

圧縮patchは標準入力で二回読む。最初は `git apply --index --binary --check`、review後に `--check` を外して適用する。これは手動のGit変更であり、取得helperは実行しない。適用先は同じsource SHA/treeで、staged・unstaged・未保存ファイルを混ぜない。直後の `git write-tree` が生成receiptの `output_tree` と完全一致しなければ、別のsourceへ調整適用して成功扱いにしない。

生成差分をコミットした最終候補をpushし、その同SHAで標準の **Public site checks**（索引鮮度・全Node・日英4ブラウザー）を通す。遠隔生成runが成功しても、最終候補CIや公開後確認の代替にはならない。失敗・中断・部分取得は保持する。生成後に正本を変更したら古いpatchを使い回さず、必要性と理由を記録して再度reviewする。公開までの残りの確認は[保守手順](../MAINTENANCE.md#候補固定公開実配信の確認)に従う。

これらのcommit markerだけではworkflowのpush pathsフィルターを越えない。
