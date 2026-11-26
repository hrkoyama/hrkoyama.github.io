# 公開ZIPのLinux追試を実行する条件

`Atlas lightweight public Linux verification` は、全追試の実行と、既存の全追試証拠の再利用を区別します。
公開用の `Public site checks`、ID台帳の検査、索引鮮度・リンク・日英ブラウザー検査は従来どおり実行します。

## 自動実行の基準

mainの `Public site checks` が成功した後、最後に**実際の全追試が成功したrun**から現在の対象SHAまでを比較します。
直前コミットだけの差分や、workflow全体のsuccess表示を基準にはしません。
科学job `public-supplements` と、その公開ZIP実行stepが実際に成功したrunを基準にします。
再利用だけで終了したrunは、次の全追試基準にはなりません。

次の場合は全追試を行います。

- 科学コード、固定入力、参照値、数値公差、受入条件、ZIP、manifest、配信registry、依存・実行環境が変わった。
- 公開検証器、検証器template、判定器、このworkflowや関連する実行設定が変わった。
- 直近の全追試が失敗・取消・時間切れになった。古い成功を使ってその失敗を隠しません。
- 信頼できる基準がない、API失敗、差分の欠落・切詰め、未分類の変更など、再利用を証明できない。

既存の手動実行と週次実行は、変更内容にかかわらず全追試です。
この条件変更そのものも全追試対象となるため、初回導入時には1回の全追試で確認します。

## 全追試を省く変更

明示的に許可したID対応台帳・凍結履歴・問題snapshot、公開配布外のMarkdown、表示用の索引・メタデータなどだけの変更なら、
以前の全追試証拠を再利用します。`code/` 内は配布物として扱い、READMEも含めて全追試対象です。
検証に関わるschemaやPython/JavaScriptなどのソースは、文言に見える変更でも安全側に全追試とします。

catalogの文言はJSONの構造・キー・ID・パス・数値等を保持した言語別テキストの変更を比較します。
文中の数値リテラルが変わる場合も全追試側に倒します。科学配布の登録・入力・受入条件に関係するcatalogやschemaは常に全追試対象です。

HTMLは一律には除外しません。既知の生成資料ページについて要素構造・属性、scriptの内容、入力値、文中の数値などの実行に関わる部分が
変わっていないことを確認したうえで、表示テキストだけの変更を許可します。
未知のHTML、JavaScriptや数値データを、文言として省略しません。
許可するパスの正本と比較実装は `scripts/atlas_depth_scope.py` です。
HTMLで許可する表示専用scriptは内容のGitハッシュも固定します。未知のscriptやinline実行コードがある章は、文言変更でも全追試側になります。
検索索引等の表示専用派生JSONは、先に成功した `Public site checks` の全生成鮮度検査を前提に、明示した出力だけを許可します。
新しい検索detailsは内容ハッシュのファイル名とテキスト専用schemaも照合します。

比較は[GitHubのCompare API](https://docs.github.com/en/rest/commits/commits#compare-two-commits)を使います。
同APIの変更ファイル一覧には上限があるため、300件以上の一覧は切詰めの可能性があるものとして全追試にします。
大きい変更を無理に省略するために、判定条件を緩めません。

## 再利用の記録

小さい `atlas-depth-scope-RUN-ATTEMPT` artifactに、対象SHA、判定理由、比較した変更、基準となる全追試run/SHA/日時を保存します。
再利用時のmodeは `reuse`、科学実行の表示は `not-rerun-reused-proof` です。
これは「今回のSHAで全数値計算を新たに実行して合格した」という記録ではありません。

全追試を行うときは、これまでどおり科学jobを別のfresh runnerで動かします。
科学jobはcheckoutせず、公開サイト上の同じハッシュの検証器・registry・ZIPから全登録群・全固定ケースを実行します。
群ごとの入力、数値公差、時間制限、pytest条件、全JUnit確認は変えません。
全追試用の大きいartifactは全追試時だけ作られ、再利用時はscopeの小さい証拠だけが残ります。

## 確認

```sh
node --test scripts/atlas-depth-scope.test.mjs
node --test scripts/atlas-depth-ci.test.mjs
```

テストでは、科学変更の後に文言変更が続く場合、失敗の後に文言変更が続く場合、skipを新たな基準にしないこと、
入力・参照・公差・ZIP・検証器の変更、HTML内scriptや入力属性、差分不足、手動・週次の強制全追試などを確認します。
科学計算のソース・入力・参照・基準・旧版ZIPのバイト列は変更しません。
