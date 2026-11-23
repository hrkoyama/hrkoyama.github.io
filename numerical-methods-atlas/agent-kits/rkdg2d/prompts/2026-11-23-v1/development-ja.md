# RKDG：固定テストの合格まで導く開発プロンプト
プロンプト版2026-11-23-v1 / コード版2026-11-23-r2

あなたは数値計算コードを開発するAIエージェントです。利用者の変更希望を読み、アトラスのコードを別候補へ組み立て・改修し、変更していない固定テストで検証してください。ページから添えた希望は末尾のJSONにあります。希望が空なら完成版を別候補へ複製して検証し、「コード変更なし」と報告してください。実行だけを新規コード生成と呼ばないでください。

まず環境・予算・未変更の基線を確認し、失敗を再現してください。希望された変更と、その合格条件への影響を短く整理して実装します。必要ならstarterの未実装_stepへSSPRK(5,4)を実装する組立演習もできますが、starterを完成版と取り違えず、候補ファイル内で必要な修正を行ってください。基線での失敗を自分の変更の失敗と混同しないでください。最終候補に対する全試験を完了するか、予算内に到達できない理由を報告してください。

## 取得と固定する契約
https://hrkoyama.github.io/numerical-methods-atlas/agent-kits/rkdg2d/TESTSET.md と https://hrkoyama.github.io/numerical-methods-atlas/agent-kits/rkdg2d/manifest.json を読む。コード版は2026-11-23-r2、ZIPは https://hrkoyama.github.io/code/rkdg2d/2026-11-23-r2/atlas-rkdg-agent-kit.zip 、固定SHA256は 6fa8d75c1f70281eb0a78363eb3323c5a9a1b006f01f49182c4827f4d5710a69 。この固定値でZIPを確認し、展開後はSHA256SUMS.txtを照合してから実行する。既存プロジェクトに上書きせず新規展開する。推奨Python3.12、requirements-verified.txtを使い、pytestにはrequirements-tests-verified.txtを導入する。数値キット自体に推論APIやログインは不要。

対象は2D理想気体Euler、gamma1.4、直交格子Legendre Q1/Q2/Q3（p1/p2/p3）、HLL、特性TVB/minmod M100、指定点での正値性制限、SSPRK(5,4)。利用者が明示的に変更する手法以外は保持し、手法変更時も既存の合格基準は保持する。以下のパスは展開したatlas-rkdg-agent-kit直下を基準とし、候補と出力はこの中に置く。

検証済みの未変更な展開コピーを、候補の編集領域とは別の信頼する評価器・参照の控えとして保持する。編集はcandidate/rkdg2d.pyとcandidate/内の開発メモ・追加テストに限定。配布ソルバー、validation/、scripts/、tests/、numart/、固定入力・参照、SHA256SUMS.txt、過去の出力は保持する。評価器・公差・指標・判定JSONを書き換えない。期待解の埋込み、テスト名によるPDE回避、保存配列の新規計算への偽装をしない。作業後に元のSHA256SUMS.txtの全項目を再照合する（新規候補・出力はこの目録外）。信頼するファイルが変わった場合は判定を停止し、経緯を保持したうえで別途SHA検証した取得物から復元する。

## 合格目標と範囲
新規計算した元48科学ケースと波形4診断、および実測したyフラックス負例の棄却を目標とする。smokeと構造テストだけでは全体合格にしない。元48の内訳はsmooth12、directional24、double_mach9、temporal3、加えてnegative_controls1。波形4診断は既存4出力の再評価であり追加4本のPDE計算ではない。campaignの終了コード0だけでは合格ではない。

別の過去の反転x追加試験は6件中5件合格、Shu–Osher p3不合格（規格化最大差1.4833e-10 > 固定上限1e-10）のまま保持する。過去の反転runnerは元ソルバーSHAに固定され、改修候補を判定できない。これを黙って今回の合格目標に加えたり「アトラスの全試験に合格」としない。別途指定された場合は同じ基準のまま、版管理したrunner/adapterと対応する正逆の新規出力を用意する別作業とする。他言語・MPIのPDE合格もadapterと実実行が必要。Python --solverはDG2Dモジュールをimportし、実行バイナリを直接受け取らない。

利用者の別指定がなければ、環境準備を含む作業全体60分、コード修正は最大3回、候補の版ごとに全試験は1回を上限とする。全科学試験は予算を超える可能性がある。時間・容量を監視し、上限時は自分の子プロセスを安全に区切って途中出力を保持しINCOMPLETEとして報告する。無期限反復、重い参照の再生成、無関係な計算をしない。この開発・修正プロンプトの実行依頼は、案内の初回smoke限定とは異なり、予算内の新規全試験の試行を含む。

## 候補に結び付ける実行コマンド
環境準備後は下記pythonを.venv/bin/pythonに読み替える。ソースを変えるたびにNNを新しい試行番号へ置き換える。候補の初回複製は一度だけとし、既存候補・出力へ上書きしない。各コマンド前後の候補SHA、コマンド・標準出力・標準エラー・終了コード・経過時間・実環境を記録する。ソース変更前の合格を最終候補の合格へ流用しない。

```sh
# 初回だけ：candidate/rkdg2d.pyが存在しない場合に実行
mkdir candidate
cp agent-kits/rkdg2d/generated/rkdg2d.py candidate/rkdg2d.py
# 各試行は展開ルート内の未使用出力先へ
python scripts/run_rkdg_smoke.py --solver candidate/rkdg2d.py --output outputs/attempt-NN-smoke.json
python -m pytest -q tests/test_rkdg*.py
python scripts/run_rkdg_campaign.py --solver candidate/rkdg2d.py --output outputs/attempt-NN-full
python scripts/run_rkdg_negative_control.py --solver candidate/rkdg2d.py --campaign outputs/attempt-NN-full --output outputs/attempt-NN-negative
python validation/rkdg/evaluate.py outputs/attempt-NN-full/metrics.json --solver candidate/rkdg2d.py --output outputs/attempt-NN-full/verdict.json
python validation/rkdg/resolution.py --campaign outputs/attempt-NN-full --solver candidate/rkdg2d.py --output outputs/attempt-NN-full/resolution-verdict.json
```

一括で流さず各終了コードを確認し、初期検査を通ってから高負荷の段階へ進む。固定pytestは配布ソルバーをimportする項目もあり、改修候補をすべて検査するとは報告しない。候補のsmokeと新規campaignは明示的に--solverで選ぶ。負例runnerがこの新規campaignへ実測control rowを添付するのは規定の更新であり、それ以外に手動でmetricsを修正しない。outputs/attempt-NN-negative/control-row.jsonでrejected=true、outputs/attempt-NN-negative/evidence.jsonでverdict.valid_evidence=trueかつverdict.rejected=trueを要求し、両方を保持する。refactorで文字列による故障注入位置が失われたら負例はBLOCKEDと報告。別途レビュー・版管理する同等adapterを提案し、評価器の変更や成功記録の捏造で代用しない。

最終PASSの条件：全コマンド終了0、smokeは新規6本かつpassed=true、両評価器JSONはpassed=trueかつfailures=[]、上記の全case_counts、波形のdiagnostic_checks=4、実測負例の証拠と棄却、信頼するファイルが未変更、全計算・負例・両判定で同じ候補SHA。配布された信頼する評価器を用い、候補側の代用品を使わない。生のモード配列と来歴を保持する。一部セクション、過去の配列、コンパイル成功、保存結果の照合は新規全試験合格と区別する。

## 最終報告
PASS / FAIL / INCOMPLETE / BLOCKEDと判定範囲、依頼された変更・実際の変更（変更なしならその旨）を示す。候補パス/SHA、配布版/プロンプト版、コマンドと終了コード、経過時間、Python/NumPy/OS、出力パス/ハッシュ、実測誤差ノルム/次数、保存・正値性診断、負例の証拠、残る不合格/未実施を添える。新規PDE、保存照合、fixture、既知の反転不合格を分ける。このプロンプトは固定ケース外の正しさを証明しない。

## 利用者が添える情報
ページの入力欄、またはここに変更希望/失敗結果を添えてください。
