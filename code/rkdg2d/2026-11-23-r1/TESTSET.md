# 2D Euler RKDG：AIエージェント向けコードと固定テスト

公開版 **2026-11-23-r1**。入口：[数値計算法アトラス](https://hrkoyama.github.io/numerical-methods-atlas/agent-kits/rkdg2d/)。[English](https://hrkoyama.github.io/numerical-methods-atlas/agent-kits/rkdg2d/TESTSET-en.md)／[機械可読の公開manifest](https://hrkoyama.github.io/numerical-methods-atlas/agent-kits/rkdg2d/manifest.json)。

「2次元圧縮性流体をDG法で解きたい」とき、このMDを利用者のAIに渡す。アトラスから完成コード・固定入力・独立参照・評価器を取得し、別コピーで改修した候補を同じ試験へ渡せる。任意のAI生成コードの成功を保証するものではない。

## 取得して最初の実計算を行う

Python 3.9以上、NumPyが必要。実際の確認環境はPython 3.9.6／NumPy 2.0.2。全対応版の検証ではない。`curl`、`unzip`とSHA256ツールも使う。未使用の作業ディレクトリで実行する。

```bash
mkdir rkdg-atlas-2026-11-23-r1
cd rkdg-atlas-2026-11-23-r1
curl -fL https://hrkoyama.github.io/code/rkdg2d/2026-11-23-r1/atlas-rkdg-agent-kit.zip -o atlas-rkdg-agent-kit.zip
curl -fL https://hrkoyama.github.io/code/rkdg2d/2026-11-23-r1/atlas-rkdg-agent-kit.zip.sha256 -o atlas-rkdg-agent-kit.zip.sha256
sha256sum -c atlas-rkdg-agent-kit.zip.sha256
# macOSでsha256sumがなければ、直前の1行を次に置き換える。
# shasum -a 256 -c atlas-rkdg-agent-kit.zip.sha256
unzip -q atlas-rkdg-agent-kit.zip
cd atlas-rkdg-agent-kit
sha256sum -c SHA256SUMS.txt
# macOSでは shasum -a 256 -c SHA256SUMS.txt
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-verified.txt
.venv/bin/python scripts/run_rkdg_smoke.py --output outputs/fresh-smoke.json
```

SHA不一致なら実行を中止して取得した版を確認する。内部`SHA256SUMS.txt`は自身を除く配布全ファイルを照合する。以後の`python`は`.venv/bin/python`へ読み替える。Windowsでは対応する仮想環境のPythonを使う。

smokeは**新しい6本のPDE計算**（p1/p2/p3、6²→12²、t=0.02）で、xとyの両方向に変化する斜めエントロピー波を解く。候補のsample関数を使わず、モードから独立に再構成した密度と厳密解を比較し、粗い格子でのL₂次数・保存・指定点の正値性を確認する。終了コード0と`outputs/fresh-smoke.json`の`passed=true`が合格。**元48ケースの合格を意味しない。** 実時間はJSONの`wall_seconds`に記録する。速度の保証はない。

## 提供する計算と固定した版

- 2D理想気体Euler、γ=1.4、直交一様格子、テンソル積Legendre Q1/Q2/Q3（p=1/2/3）。HLL、特性TVB/minmod（M=100）、セル平均を保持する正値性制限、SSPRK(5,4)。
- 現行完成候補：`agent-kits/rkdg2d/generated/rkdg2d.py`。SHA256：`4ed984a01c42fe9bb657c09c61361b086682d6aa611e9f478bf996c0b29b81d4`。
- 元48ケース基準：`validation/rkdg/acceptance.json`、SHA256：`7219904b7460efa32f1f1ea03b6cd729e9e3b200e7c60643d0cfa08ec866d4af`。
- 波形4診断基準：`validation/rkdg/resolution-acceptance.json`、SHA256：`275c7ffc386bc4cc791148b498e3872e9a67398f2a175bd3ae9a418559cf63c3`。
- 追加反転6基準：`validation/rkdg/reflection-acceptance.json`、SHA256：`ab7986e1eaf768f63fb239bf5a8d766d4c4fc5778389bdc42b5eb294594bf18a`。

現行結果は`outputs/rkdg-2026-11-23/accepted-v3/`。**元48ケースと波形4診断は合格、後から追加した反転x試験は5/6合格で全体不合格**。Shu–Osher p3の規格化最大差1.4833×10⁻¹⁰が固定上限10⁻¹⁰を超える。上限を緩めず、失敗記録も同梱する。元48＋4の成功を、この反転試験まで成功した意味で使わない。

`accepted/`、`manifest-v2.json`、`generated/assembly-notes.txt`などは過去の候補・失敗・修正の履歴。現在の候補は上記4ed984…で識別する。未完成の`starter/rkdg2d.py`は組み立て課題用であり、初回実行には完成候補を使う。`RELEASE.json`と`BUILD-STATE.json`に版と検証範囲を記録している。

## 保存結果だけを再判定する（PDE再実行なし）

展開先ルートで次を実行する。最初のSHA照合も済ませる。

```bash
python scripts/package_rkdg_agent_release.py --verify-only
python validation/rkdg/evaluate.py outputs/rkdg-2026-11-23/accepted-v3/metrics.json --solver agent-kits/rkdg2d/generated/rkdg2d.py --output outputs/saved-verdict.json
python validation/rkdg/resolution.py --campaign outputs/rkdg-2026-11-23/accepted-v3 --solver agent-kits/rkdg2d/generated/rkdg2d.py --output outputs/saved-resolution-verdict.json
```

`--verify-only`は全記録の結合と反転の12配列も検査する。終了コード0／`integrity_passed=true`は記録の整合を示し、`reflection_supplement.qualification_passed=false`（5/6合格）はそのまま残る。科学的な全項目合格と混同しない。その後の両評価器が終了コード0、`passed=true`、`failures=[]`であることを確認する。元判定は保存指標とソースの照合、波形判定は保存配列からの再評価。これだけで新規PDE計算をしたと報告しない。構造・評価器・出力契約の検査は、`python -m pip install -r requirements-tests-verified.txt`の後、`python -m pytest -q tests/test_rkdg*.py`で実行できる。これも全科学ケースの新規実行の代用ではない。

## 自分の候補を作り、元48＋波形4を新しく計算する

既存ファイルを上書きせずコピーする。基準・評価器・独立参照・過去記録を編集しない。

```bash
mkdir candidate
cp agent-kits/rkdg2d/generated/rkdg2d.py candidate/rkdg2d.py
python scripts/run_rkdg_smoke.py --solver candidate/rkdg2d.py --output outputs/candidate-smoke.json
# ここで候補を改修した場合、smokeも未使用の出力先で再実行する。
python scripts/run_rkdg_campaign.py --solver candidate/rkdg2d.py --output outputs/candidate-full
python scripts/run_rkdg_negative_control.py --solver candidate/rkdg2d.py --campaign outputs/candidate-full --output outputs/candidate-negative
python validation/rkdg/evaluate.py outputs/candidate-full/metrics.json --solver candidate/rkdg2d.py --output outputs/candidate-full/verdict.json
python validation/rkdg/resolution.py --campaign outputs/candidate-full --solver candidate/rkdg2d.py --output outputs/candidate-full/resolution-verdict.json
```

fullは初回の既定操作ではなく、**新しい科学計算を実行する明示的な選択**。細かい参照用の時間計算と故障版も走るため、smokeより重い。所要時間は環境依存で、全工程一括の所要時間は未測定。新しい候補の全4コマンドへ同じ`--solver`を渡す。全出力先はZIP展開ルート内の未使用パスにする。中断・失敗の記録も保持する。

campaignの終了コード0は計算完了を示し、その後の評価器で合否を決める。元判定の`case_counts`はsmooth=12、directional=24、double_mach=9、temporal=3、negative_controls=1（科学48ケース＋故障検査）。追加の`diagnostic_checks=4`は既存のShu–Osher配列を評価する4診断で、4本の新PDEではない。両評価器の終了コード0／`passed=true`に加え、負例の`outputs/candidate-negative/control-row.json`の`rejected=true`と`evidence.json`を確認する。

故障注入は提供候補のy流束行を識別する。改修で構造が変わり注入できなければ未実施と記録し、同等のy流束故障を作るadapterを用意する。結果JSONや評価器を書き換えて合格にしない。不足ケース・SHA不一致・非有限値・固定上限超過を受け入れない。

## 反転xの追加6本（歴史v3候補専用）

記録は`outputs/rkdg-2026-11-23/x-reflection/verdict.json`、元配列は同じ場所の`arrays/`。実際に全初期状態を反転し、x運動量の符号とLegendre xモードの偶奇を変換する。単に図を左右反転した結果ではない。

```bash
python scripts/run_rkdg_reflection.py --solver agent-kits/rkdg2d/generated/rkdg2d.py --forward outputs/rkdg-2026-11-23/accepted-v3 --output outputs/fresh-reflection --workers 2
```

このコマンドは新規PDEを6本実行する。**記録された環境の期待判定は終了コード1、`passed=false`、5/6合格**。別環境での丸めにより判定が変わる可能性も含め、実測を記録する。期待された失敗でも終了コードを成功に書き換えない。これはソースSHAを4ed984…に固定した歴史比較runnerで、改修候補には使えない。新しい候補の反転試験には、同じ不変基準を使う別のrunner・forward計算・来歴の整備が必要。`--output`と`--forward`は展開ルート内に置く。

## 多言語移植・MPI並列化へ渡す

`agent-kits/rkdg2d/PORT-AND-MPI-TASK.txt`が依頼テンプレート。日本語の`docs/rkdg-interchange.md`／英語の`docs/rkdg-interchange-en.md`が共通出力契約。JSON manifest＋所有セルのmodal CSVを用い、保存量は`rho,rho_u,rho_v,energy`、Legendreは`P_m(1)=1`、モード00はセル平均。全Qpモードを1回だけ出力し、ghost/haloセルを含めない。

```text
global_i,global_j,mode_i,mode_j,rho,rho_u,rho_v,energy
```

実際の移植側出力がある場合の照合例（`port/`は同梱しない）：

```bash
python validation/rkdg/interchange.py check-reference outputs/rkdg-2026-11-23/accepted-v3/arrays/smooth-p2-n8.npz port/smooth-p2-n8/manifest.json --output port/reference-comparison.json
python validation/rkdg/interchange.py compare port/serial/manifest.json port/mpi4/manifest.json --output port/mpi4-comparison.json
```

合格は終了コード0と`passed=true`。係数の既定公差`atol=1e-11, rtol=1e-9`はI/O等価性の基準で、物理精度の上限を緩めない。境界流束診断を提供し、`conservation_checked=true`も確認する。省略時の`false`は保存則確認済みを意味しない。

Python campaignは`DG2D`を持つPythonモジュールを読み、他言語実行ファイルを直接受け取らない。移植側は実行・出力読込・全固定ケースの独立指標を`metrics.json`形式へまとめるadapterを作る。1出力の一致だけで全48ケース合格とはしない。MPIは実際に1/2/4ランクを起動し、x/y分割・不均等分割、global CFL、各RK段のhalo・境界時刻、物理境界だけの流束・所有セルだけの総和を確認する。真にPDEを解いた出力だけに`execution_kind="solver-output"`を付ける。

同梱の実施済み例はC++17解析多項式のI/Oと1/2/4分割fixtureの照合。**他言語のPDEソルバー実行・実MPIでのPDE実行は未実施。** fixtureをMPI実行と報告しない。

## 制約・参照・報告

x/yの厳密1D入力には解析的縮約を使い、斜め波・Double Mach・smokeが完全2D結合を通る。衝撃波を含む全領域に2/3/4次収束を要求しない。Double Machは独立FV参照との広域構造比較で、微細渦の収束を主張しない。正値性は指定した求積点・面・頂点に限る。波形4診断のROIは[1.2,2.2]、p2/p3のx/y、256セルで、相対L₁≤0.08・平均除去標準偏差比≥0.5・相関≥0.8を同時に要求する。

固定参照は`validation/rkdg/references/`の来歴・入力・配列SHAとともに配布する。Shu–Osherの参照格子差は全域密度相対L₁の不確かさであり、点ごとの厳密誤差上限ではない。参照の再生成は通常不要。

報告には「新規PDE」「保存結果の再判定」「I/O fixture」「未実施」を分け、実ソースSHA、実行コマンド・終了コード・環境、入出力SHA、誤差・次数・保存残差・正値性・失敗理由を残す。方法と一次文献9報はZIP内`docs/rkdg.md`／`docs/rkdg-en.md`。Sod (1978)、HLL (1983)、Woodward–Colella (1984)、Shu–Osher (1989)、Toroほか (1994)、Jiang–Shu (1996)、Cockburn–Shu (1998)、Spiteri–Ruuth (2002)、Zhang–Shu (2010)を引用する。

提供する原著コードと付属文書はZIP内`LICENSE`のMIT。著作権・許諾文を保持する。アルゴリズムの論文引用とコードの利用許諾は別であり、引用論文の本文・私的ポスター・非公開草稿は同梱しない。
