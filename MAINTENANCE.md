# 更新と復元の手順

このページは現行の保守ガイド。過去の検証・追加経緯は[保存履歴](docs/maintenance-history/README.md)に分離した。旧原文と各配布版の成功・失敗記録を保持し、過去の件数を現在の総数へ書き換えない。

## 公開先と保持するもの

公開用リポジトリは **`hrkoyama/hrkoyama.github.io`**、公開ブランチは **`main`**、Pagesの配信元はそのルート。公開先は **https://hrkoyama.github.io/** 配下だけで、アトラスは **https://hrkoyama.github.io/numerical-methods-atlas/**。常時適用する[AGENTS.md](AGENTS.md)と利用者の最新指示を併せて確認する。

**`koyamarium` 配下へはpush・PR作成/マージ・リリース・アップロード・公開ワークフロー起動を行わない。** `koyamarium.github.io` と旧 `koyamahr.github.io` も公開先にしない。過去の取り込み記録や旧remoteは公開の許可ではない。

既存の数値計算、固定入力、独立参照、数値公差、受入条件、golden、保存結果、図、配布ZIP、manifest、検証履歴、URL・節IDを保持する。公開済みの不変editionや内容ハッシュ付き検索detailsを上書き・削除しない。公開側独自の表示・資料・導線と他作業の未コミット変更も保持し、上流の `website/dist/` 全体では置き換えない。

## 現行件数と照合方法

次は **2026-11-24に公開コミット `9dde48159c568f985170506ef2eb0a7008f1c4ea` で確認したスナップショット**。将来の固定合格値ではない。更新後は下の読み取り専用コマンドと対象SHAを記録し、現行台帳で再確認する。

- 手法台帳：**152手法**。`educational-example` 122、`reading-only` 15、`planned` 15。
- 共通実行台帳：**22例**。補助配布の登録：**38群・83ケースID**。両者は別の集計で、物理問題の総数として足し合わせない。
- 補助配布台帳に記録されたテスト数：**1047 pytest**。これは保存された登録値であり、この件数確認コマンドが科学計算を再実行したことを意味しない。
- 問題台帳：**113問題**、ギャラリー：**113主図**、方程式・モデル台帳：**60項目**。問題と図はそれぞれの台帳で数える。

`coverage.json` などの集計には別の対象範囲がある。部分集合の件数を全手法数へ合わせたり、「解説あり」を「実装・検証済み」へ格上げしたりしない。現行総数は共通inventoryから検査し、旧editionの件数・SHA・数値基準はその版の固定値で検査する。

公開用作業コピーのルートで実行する（Python標準ライブラリのみ、数値実行なし）。

```sh
git rev-parse HEAD
python3 - <<'PY'
import json, sys
from pathlib import Path
sys.path.insert(0, 'scripts')
from atlas_registration import inventory
r = Path('.')
def load(path):
    return json.loads((r / path).read_text())
i = inventory(r)
releases = load('numerical-methods-atlas/validation/releases.json')['releases']
assert len(releases) == len(i['supplement_groups'])
assert {x['group'] for x in releases} == set(i['supplement_groups'])
assert {c for x in releases for c in x['case_ids']} == set(i['supplement_case_ids'])
print(json.dumps({
    'methods': len(i['method_ids']), 'statuses': i['method_status_counts'],
    'common_examples': len(load('numerical-methods-atlas/code-and-data/examples.json')['examples']),
    'supplement_groups': len(releases),
    'supplement_cases': len(i['supplement_case_ids']),
    'registered_pytest_tests': sum(x['tests'] for x in releases),
    'problems': len(load('catalog/atlas-test-problems.json')['problems']),
    'primary_figures': len(load('numerical-methods-atlas/gallery/preview-manifest.json')['items']),
    'equations_and_models': len(load('catalog/atlas-equations.json')['equations'])
}, ensure_ascii=False, indent=2))
PY
```

## 編集元と生成物の境界

- **登録と公開状態**：入口は `catalog/atlas-registration.json`、契約は `catalog/schemas/atlas-registration.schema.json`。手法は `catalog/atlas-methods.json`、補助群・現行editionは `catalog/atlas-depth-expansion.json` を編集する。`scripts/atlas_registration.py` と `scripts/fixtures/atlas-inventory.mjs` が共通のID・件数を読む。群ID・総数を各機能へ手で複製しない。手法一覧のHTML/JSON/Markdownは `scripts/build-atlas-resources.py` などの生成物。
- **本文と導線**：目的別入口は `catalog/atlas-goals.json` と `catalog/atlas-purpose.json`、詳説章は `catalog/atlas-detailed-reading.json` など該当分野のcatalog。式は `catalog/atlas-equations.json`、問題は `catalog/atlas-test-problems.json`。実行例への関係は `scripts/atlas_execution_routes.py` が公開台帳・直接対応から解決する。一般モデルの説明と実装した範囲、文献を読んだ範囲と未確認事項を分けて記す。
- **検索と共通画面**：編集用JSは `frontend/search/` と `frontend/atlas/app.js`。`scripts/search_assets.py` と `scripts/atlas_runtime_assets.py` が公開モジュールと資産manifestを生成する。可変文言は `atlas-runtime-data.mjs` へ生成される。生成済みJSや索引の直接編集、ビルダーによる意味的なJS文字列置換での補修を行わない。既存の手書き `numerical-methods-atlas/coverage.js` は編集元として扱う。
- **生成順**：`catalog/site-build-pipeline.json` が順序・依存・検索境界、`scripts/site_pipeline.py` が事前検査を定める。purposeの2回の生成は、検索前の本文確定と検索後の資産版伝播という別の役割を持つ。依存注記は差分生成の自動skip機構ではない。
- **科学配布と追試**：`code/` の版固有の入力・参照・結果・manifest・verificationと、対応するpackager/validatorを確認する。追加計算は各caseの入力・独立参照・受入条件をreview/freezeしてから行う。新規版と旧版を分け、失敗も保存し、全固定入力とZIP単体での再現性を確認する。公開独立verifierの編集元は `scripts/templates/verify-depth-public.py.tmpl`。群allowlist・配信registry・workflowのSHA pinは既存パイプラインで揃える。

ホームと共通案内は `index.html`・`using/`、共通chromeは `scripts/site-chrome.mjs`・`site.js`・`site.css`。HPCI等の公開側独自資料は[README](README.md)の分野別手順を使う。取り込み元・対象版は `research-imports.json` 等で確認し、公開側の追加内容を保持する。

## 開始からローカル確認まで

1. 利用者の最新指示と、教材元ルートにあるローカル専用の `LOCAL-WORK-QUEUE.md`、`outputs/atlas-private-work-queue.json`、指定された進捗を読む。実際のHEAD・公開/CIレシートで状態を照合する。準備・実装・実行・公開を区別する。これら私用ファイルをpublisher・サイト・ZIPへ取り込まない。
2. `atlas-search-publisher/` で `git status`、`git remote get-url --push origin`、`git fetch origin main` を確認する。他作業があれば、最新のHR `origin/main` から `codex/` ブランチの隔離worktreeを作り、今回の変更だけを編集する。既存作業コピーをresetしない。
3. 正本・本文を編集し、必要な変更をステージする。**索引に入る本文・catalog・frontend・生成器が変わるときだけ、まとめた対象で `python3 scripts/prepare-indexes.py` を明示実行する。** 原則1日1回程度に集約し、通常コミットや変更のない対象では全再生成しない。公開前の変更・修正・鮮度未確認は、理由・実際の成功時刻・対象tree・ログを私用キューへ記録する例外とする。
4. `prepare-indexes.py` はステージしたsnapshotから隔離生成し、生成差分をステージする。生成中の実質的なindex変更・生成先の未ステージ変更を拒否する。stat/cacheだけの更新は許す。生成中は元の内容・ステージを変更せず、終了後に `git diff --cached` を読む。
5. 現行の `MAINTENANCE.md`・ルート `README.md`・`docs/` のMarkdownだけの変更は、検索入力の公開HTML・明示metadataを変えない。全索引のローカル再生成を省く理由を記録し、同じ候補SHAのCIによる `--check` で鮮度を照合する。入力外という判断を将来の別のMarkdown生成元へ無条件で広げない。
6. 下の静的検査とNode検査、差分・保存物の照合を行う。画面変更時は日本語・英語、狭幅・標準幅の実画面と対象図を確認する。一時previewは自分のプロセスを特定して停止し、変更したviewportも戻す。

```sh
python3 scripts/check-site.py
node --test scripts/*.test.mjs
git diff --check
git diff --cached --check
git status --short
```

CIの基準環境は **Python 3.12、Node.js 22**。上の静的検査・Node検査は標準機能で実行できる。ブラウザー検査だけは `package-lock.json` の固定依存と対応Chromiumを使う（`npm ci --ignore-scripts`、`npx --no-install playwright install chromium`、`npm run test:browser`）。科学ZIPの追試は別の固定依存・受入条件を使う。

ローカルのブラウザー検査が残す自分のHTML reportは、次の直接のsite検査前に作業コピー外の一時領域へ保存する。Gitでignoreされていても静的walkerに見えるためで、他作業のファイルを消したり検査対象を緩めたりしない。

pre-commitは既定で全索引生成をskipする。`ATLAS_REFRESH_INDEXES_ON_COMMIT=1` は実際にprepareを起動するopt-in。日付で自動skipする機構や私用キューを読むガードはない。通常コミットごとの有効化はしない。CIの `prepare-indexes.py --check` は隔離再生成による鮮度照合で、日次のローカル更新とは別に毎回必要。

## 候補固定・公開・実配信の確認

1. 変更をコミットし、HRの `codex/` ブランチで **Public site checks** の成功を確認する。`check` jobは全生成の鮮度・参照・Node検査、`browser-smoke` jobは日英×390/1280pxの4profileを確認する。ブラウザー検査は数値計算の追試を代替しない。検証中のSHAと作業コピーはcleanに固定する。
2. 公開直前に最新の `origin/main` と私用キューの実公開中状態を再確認し、他作業の公開に重ねない。差があれば今回の変更だけを統合し、影響する検査を再実行する。実際のpush URLが `hrkoyama/hrkoyama.github.io`、Pages設定が `main` のルート・`https://hrkoyama.github.io/` であることを再確認する。
3. 固定候補を **`git push origin HEAD:refs/heads/main`** で公開する。隔離ブランチから古いローカル `main` を誤って送らない。force pushはしない。
4. 公開した同じSHAで **Pages build and deployment** と **Public site checks** の成功を確認する。匿名HTTPで変更したページ・文書・図・ダウンロードのURL、内容、版・ハッシュを照合する。保存物の照合と、新たな数値実行を区別して記録する。
5. mainのPublic site checks成功後に自動起動する **Atlas lightweight public Linux verification**（`.github/workflows/atlas-depth-linux.yml`）を待つ。同SHA、公開registryのSHA、ソースcheckoutなし、全登録群・全固定case、pytestの失敗・error・skipなしをreportと全JUnitで確認する。公開したZIPだけからの計算であり、旧版の詳細収束試験をすべて再生成したとは記さない。自動runと重なる手動dispatchを追加しない。再試行が必要なら失敗ログ・理由を保持する。
6. 実行・配信・CIの実レシート、実際の日時と対象SHA/treeをローカル専用の進捗へ保存して完了を記録する。未確認の日付や成功を補わない。公開確認後のpublishedラベル・公開記録・索引だけの変更は、最新の日次集約指示に従って根拠付きの私用提案へ残し、次の許可済み集約でHEAD/blobを再照合する。自動反映・二回目の索引更新/公開は行わない。

軽量Linuxの自動起動と週次設定は既存workflowにある。共通22例を対象とする手動の **Atlas public Linux verification**（`atlas-public-linux.yml`）やRKDG専用検査は対象が異なる。全体を同じ件数・同じ実行として記録しない。今回の変更に必要な検証範囲を確認し、重い科学実行を追加しない。

外部CI中は、別の隔離workspaceで次batchの調査・独立実装・軽量検査を進めてよい。数値実行前のreview/freezeは必要。現在のCI失敗修正を優先し、公開backlog登録・索引統合・次のpushは現在の必須公開確認後に直列化する。定期ジョブ・常駐処理・容量の定期監視を新設しない。

量子化学の追加開発は小さな教育用モデルと少数の固定入力を基本にする。大規模な基底/k点走査、重い独立参照の再生成、長時間の第一原理MD、実物質の精密計算は利用者の改めての指定範囲で扱う。保存結果の照合・代表固定caseの再実行・詳細収束検証を区別し、既存の成功履歴・配布版・公差を保持する。

## 他資料の保護と復元の入口

大学ノートの公開済み画像・PDF・ページ選択・マスクを保持する。非公開原本・全文OCR・マスク前画像・個人情報・アカウント情報を取り込まない。公開書誌と対応は `notebooks/bibliography.json`・`notebooks/material-links.json` を使い、未確認の講義・担当・年を補わない。変更時は既存の個別確認と `scripts/check-notebook-material-links.py` を用いる。詳細な既往判断は保存原文を参照する。

公開履歴の控えが必要なら、作業コピー外へ `git bundle create ../hrkoyama-site.bundle --all` で保存し、`git bundle verify ../hrkoyama-site.bundle` で確認する。既存の控えは上書きしない。復元先を分けてcloneし、静的検査・保存物の照合を行う。非公開の教材元・書籍原稿の保管も別途保持する。

公開の取り消しは対象コミットを `git revert` し、差分・保存物・検査を確認して同じHR公開手順を使う。共有履歴の強制上書きや旧サイトの再公開を行わない。`google0b2aef3d9ae4b856.html` と既存のSearch Console対象・`sitemap.xml` URLを保持し、配信成功とGoogleへの登録/順位を区別する。検索語・訪問者入力を収集する仕組みは追加しない。

## 旧見出しの互換案内

<details>
<summary>以前の見出しへのリンク（すべて保存原文の履歴）</summary>

以下の見出しは旧フラグメントURLを残すための案内。現行の件数・手順は上記を使い、当時の記述は保存原文で読む。

## 優先度2の保守境界と検査（2026-11-23）

[当時の記録を読む](docs/maintenance-history/through-9dde4815.md)。

## 候補28〜37の集約追加（2026-11-23）

[当時の記録を読む](docs/maintenance-history/through-9dde4815.md)。

## 実装範囲の表示と軽量な共通検索（2026-11-23）

[当時の記録を読む](docs/maintenance-history/through-9dde4815.md)。

## 公開先の固定ルール

[当時の記録を読む](docs/maintenance-history/through-9dde4815.md)。

## 通常の更新

[当時の記録を読む](docs/maintenance-history/through-9dde4815.md)。

## 編集する正本

[当時の記録を読む](docs/maintenance-history/through-9dde4815.md)。

## 資料の見せ方・読みやすさ

[当時の記録を読む](docs/maintenance-history/through-9dde4815.md)。

## 大学ノートと非公開資料の対応

[当時の記録を読む](docs/maintenance-history/through-9dde4815.md)。

## 公開前の自動確認

[当時の記録を読む](docs/maintenance-history/through-9dde4815.md)。

## バックアップと復元

[当時の記録を読む](docs/maintenance-history/through-9dde4815.md)。

## 検索登録

[当時の記録を読む](docs/maintenance-history/through-9dde4815.md)。

## 数値計算アトラスの手法情報とコード版

[当時の記録を読む](docs/maintenance-history/through-9dde4815.md)。

## 分野ごとの実装・検証の深さ（2026-11-22）

[当時の記録を読む](docs/maintenance-history/through-9dde4815.md)。

## H₂分子RHF（2026-11-22）

[当時の記録を読む](docs/maintenance-history/through-9dde4815.md)。

## 周期HeのKS-LDA（2026-11-22）

[当時の記録を読む](docs/maintenance-history/through-9dde4815.md)。

## 分野をつなぐ入口（2026-11-22）

[当時の記録を読む](docs/maintenance-history/through-9dde4815.md)。

## 自動微分の共通基盤とBratu検証

[当時の記録を読む](docs/maintenance-history/through-9dde4815.md)。

## 多原子DFTの原子間力（2026-11-22）

[当時の記録を読む](docs/maintenance-history/through-9dde4815.md)。

## Bratuの陰関数感度と離散随伴

[当時の記録を読む](docs/maintenance-history/through-9dde4815.md)。

## Bratuの合成観測による逆問題

[当時の記録を読む](docs/maintenance-history/through-9dde4815.md)。

## 2次元TMzのYee FDTD（2026-11-22）

[当時の記録を読む](docs/maintenance-history/through-9dde4815.md)。

## Bratuの複数パラメータ推定・正則化・識別可能性

[当時の記録を読む](docs/maintenance-history/through-9dde4815.md)。

## 6分野の軽量な補助検証（2026-11-22）

[当時の記録を読む](docs/maintenance-history/through-9dde4815.md)。

## FDTDの媒質界面・左右x方向PML（第2版、2026-11-22）

[当時の記録を読む](docs/maintenance-history/through-9dde4815.md)。

## FDTDの四辺・角PML（第3版、2026-11-22）

[当時の記録を読む](docs/maintenance-history/through-9dde4815.md)。

## アトラスの検索と3つの入口

[当時の記録を読む](docs/maintenance-history/through-9dde4815.md)。

## 表示同期とCSVR／Langevin比較（2026-11-22）

[当時の記録を読む](docs/maintenance-history/through-9dde4815.md)。

## FDTDの媒質界面への斜め入射（第4版、2026-11-22）

[当時の記録を読む](docs/maintenance-history/through-9dde4815.md)。

## 非線形反応拡散・パターン形成の独立検証（2026-11-22）

[当時の記録を読む](docs/maintenance-history/through-9dde4815.md)。

## FDTDのp偏光・Brewster角・全反射（第5版、2026-11-22）

[当時の記録を読む](docs/maintenance-history/through-9dde4815.md)。

## 解説章の統一目次

[当時の記録を読む](docs/maintenance-history/through-9dde4815.md)。

## 教科書・参考文献と章ナビゲーション

[当時の記録を読む](docs/maintenance-history/through-9dde4815.md)。

## 多峰性MCMCと診断の独立照合（2026-11-22）

[当時の記録を読む](docs/maintenance-history/through-9dde4815.md)。

## 索引のまとめ更新と公開前の鮮度確認

[当時の記録を読む](docs/maintenance-history/through-9dde4815.md)。

## 式・問題図・厳密解の補助索引

[当時の記録を読む](docs/maintenance-history/through-9dde4815.md)。

## 図から問題別の方程式・参照・コードへ進む

[当時の記録を読む](docs/maintenance-history/through-9dde4815.md)。

## 手法から方程式・問題図・参照・コードへ進む

[当時の記録を読む](docs/maintenance-history/through-9dde4815.md)。

## CT／GLMの同条件比較と格子・時間収束（2026-11-22）

[当時の記録を読む](docs/maintenance-history/through-9dde4815.md)。

## 基盤手法の条件数・残差・収束（2026-11-22）

[当時の記録を読む](docs/maintenance-history/through-9dde4815.md)。

## FDTDの損失・分散媒質（第6版、2026-11-22）

[当時の記録を読む](docs/maintenance-history/through-9dde4815.md)。

## Lie–Trotter／Strangの比較解説（2026-11-22）

[当時の記録を読む](docs/maintenance-history/through-9dde4815.md)。

## 同条件のLie–Trotter／Strang反応拡散比較（2026-11-22）

[当時の記録を読む](docs/maintenance-history/through-9dde4815.md)。

## 粒子・輸送の独立参照・保存則・統計誤差（2026-11-22）

[当時の記録を読む](docs/maintenance-history/through-9dde4815.md)。

## 利用者のAIエージェント向け開発基盤の年末計画（2026-11-23）

[当時の記録を読む](docs/maintenance-history/through-9dde4815.md)。

## 全候補の逐次実装と図版化（2026-11-23）

[当時の記録を読む](docs/maintenance-history/through-9dde4815.md)。

## 2D RKDGのAIエージェント向け開発キット（2026-11-23）

[当時の記録を読む](docs/maintenance-history/through-9dde4815.md)。

## 球対称Nohの追加版

[当時の記録を読む](docs/maintenance-history/through-9dde4815.md)。

## 軽量2D Cartesian Noh（2026年11月23日）

[当時の記録を読む](docs/maintenance-history/through-9dde4815.md)。

## 軽量Sedov–Taylor爆発（2026年11月23日）

[当時の記録を読む](docs/maintenance-history/through-9dde4815.md)。

### Sedov r2：警告をエラーとする公開追試への修正

[当時の記録を読む](docs/maintenance-history/through-9dde4815.md)。

## Double Mach反射の軽量な多格子比較（2026年11月23日）

[当時の記録を読む](docs/maintenance-history/through-9dde4815.md)。

## 前向きステップの軽量な2D検証（2026年11月23日）

[当時の記録を読む](docs/maintenance-history/through-9dde4815.md)。

## 低Machの等エントロピー渦と空間流束前処理（2026年11月23日）

[当時の記録を読む](docs/maintenance-history/through-9dde4815.md)。

## Guderley収束衝撃波の軽量な球対称検証（2026年11月23日）

[当時の記録を読む](docs/maintenance-history/through-9dde4815.md)。

## Euler二重膨張波の段階正値性（2026年11月23日）

[当時の記録を読む](docs/maintenance-history/through-9dde4815.md)。

## Zalesak型2D回転輸送（2026年11月23日）

[当時の記録を読む](docs/maintenance-history/through-9dde4815.md)。

## RKDGの開発・修正プロンプト（2026-11-23）

[当時の記録を読む](docs/maintenance-history/through-9dde4815.md)。

## 候補13〜17の5件一括追加（2026-11-23）

[当時の記録を読む](docs/maintenance-history/through-9dde4815.md)。

## レベルセット法とVOF比較・軽量2D円の移流（2026年11月23日）

[当時の記録を読む](docs/maintenance-history/through-9dde4815.md)。

## 同時期のLevel Set追加と5候補の統合

[当時の記録を読む](docs/maintenance-history/through-9dde4815.md)。

## スペクトル要素法とFR法の軽量な比較（2026年11月23日）

[当時の記録を読む](docs/maintenance-history/through-9dde4815.md)。

## RKDGの実測した組み立て・修正プロンプト試験（2026-11-23）

[当時の記録を読む](docs/maintenance-history/through-9dde4815.md)。

## 候補18〜27の10項目をまとめる運用（2026-11-23）

[当時の記録を読む](docs/maintenance-history/through-9dde4815.md)。

## 候補18〜27の実公開確認（2026-11-23）

[当時の記録を読む](docs/maintenance-history/through-9dde4815.md)。

## 候補28〜37とDSMC性能改訂（2026-11-24）

[当時の記録を読む](docs/maintenance-history/through-9dde4815.md)。

</details>

### 初学者向け19章教材（2026-11-24版）

`catalog/atlas-foundations-course.json` が本文・数式・例題・図の説明・38問の解答の共通原稿。公開入口は `/numerical-methods-atlas/learn/numerical-foundations/`。日本語のWeb/PDF教材であり、英語目次では言語を明記して案内する。既存の読み物章数や科学検証群数へ19章・19図を加算しない。

`build-atlas-foundations-course.py` は固定PDF/図/ZIPのSHAと原稿の一致を確認し、Webだけを生成する。通常の `refresh-site.py` は科学計算、MathJax、ReportLab、PDF生成を実行しない。公開版の原稿を変えるときは、先に小さな計算例の固定条件をレビューし、`scripts/foundations-course/` の実行・テスト・独立ZIP展開確認、共通数式SVG、PDFの再生成・全ページの目視確認、`verify-foundations-book.py` の抽出照合を行う。既刊PDFとZIPは保存し、公開済み版を黙って差し替えず版を追加する。

本教材の計算はPython 3.12標準ライブラリのみ。25計算テスト・2照合テスト・34固定判定・15CSVを `verify_release.py` で照合する。最初の風上法の粗い格子系列の失敗は履歴へ保存し、閾値を変えず系列を細かくした。意図的な不安定・低次対照の検出合格と、高精度法の合格を区別する。PDF制作時のみReportLab 4.4.9・svglib 1.6.0・MathJax 3.2.2・日本語TrueTypeフォントを使う。図は保存CSVから描き、WebとPDFで同じSVGを使う。公開前は `Foundations course candidate Linux verification` が候補ZIPをLinuxで実行する。公開ZIPだけのLinux追試は `Foundations course public Linux verification` に記録する。

初公開前R2では、丸めの影響を観察するderivative.csvのOS間等値照合を、80桁の独立Taylor参照とULP由来の境界へ修正した。初候補ZIPとLinux失敗を保持し、元の25計算テスト・34条件・他14CSVの公差・保存値・図を保持した。新しい2照合テストは両OSの記録値の検査と破損値の拒否を確認する。Pythonのlibm全般に1ULP精度を仮定せず、固定入力のsin/cosを参照式で検査する。
