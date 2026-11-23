"""Build a bounded bilingual report from reviewed, immutable RKDG pilot records."""
from pathlib import Path
from html import escape as esc
import hashlib,json
ORIGIN='https://hrkoyama.github.io'

def build_pilot(root):
 cfg=json.loads((root/'catalog/atlas-rkdg-pilot.json').read_text());dest=root/cfg['route'].lstrip('/');data=json.loads((dest/'summary.json').read_text());archive=root/cfg['archive'].lstrip('/')
 assert hashlib.sha256(archive.read_bytes()).hexdigest()==cfg['archive_sha256']
 assert archive.stat().st_size==cfg['archive_bytes']
 assert hashlib.sha256((dest/'summary.json').read_bytes()).hexdigest()==cfg['summary_sha256']
 assert data['numerical_status']=='PASS' and data['cost']['amount'] is None
 for t in data['trials']:
  assert t['counts']==dict(smooth=12,directional=24,double_mach=9,temporal=3,negative_controls=1)
  assert t['status']=='PASS' and t['waveform_diagnostics']==4 and t['negative_control_rejected']
  assert t['fresh_full_campaign_pde_arrays']==49 and t['raw_scalar_comparisons']==240 and t['protected_files_changed']==0
  for fn in ['original-verdict.json','waveform-verdict.json']:
   v=json.loads((dest/'evidence'/t['trial']/fn).read_text());assert v['passed'] and v['failures']==[]
 sections=[]
 for lang in ['ja','en']:
  ja=lang=='ja';link=lambda href,text:'<a href="'+esc(href,quote=True)+'">'+esc(text)+'</a>'
  title='RKDGプロンプトの実測結果' if ja else 'Measured RKDG development and repair prompts'
  lead='日本語版テンプレートで、組み立てと不合格からの修正を各1試行。両候補が元48科学ケース＋波形4診断に合格し、実測した故障負例も棄却しました。' if ja else 'One assembly trial and one repair trial used the Japanese templates. Both candidates passed the original 48 scientific cases and four waveform diagnostics, and rejected an actually executed faulty control.'
  html='<section data-site-language="'+lang+'" lang="'+lang+'"><p class="eyebrow">RKDG AGENT PILOT · 2026-11-23</p><h1>'+title+'</h1><p class="kit-lead">'+lead+'</p>'
  html+='<nav class="kit-actions">'+link('/numerical-methods-atlas/agent-kits/rkdg2d/?lang='+lang+'#prompts-'+lang,'開発・修正プロンプトをコピー' if ja else 'Copy the development / repair prompts')+link(cfg['archive'],'コード・生配列・判定記録 / ZIP' if ja else 'Code, raw arrays and verdicts / ZIP')+link(cfg['route']+'summary.json','実測値 / JSON' if ja else 'Measurements / JSON')+link(cfg['route']+('index.md' if ja else 'index-en.md'),'解説 / Markdown' if ja else 'Report / Markdown')+'</nav>'
  html+='<h2>'+('実測した2試行' if ja else 'Two measured trials')+'</h2><div class="pilot-table"><table><thead><tr>'+''.join('<th>'+x+'</th>' for x in (['課題','結果','ソルバー修正','全所要時間'] if ja else ['Task','Result','Solver repairs','Total elapsed']))+'</tr></thead><tbody>'
  md='# '+title+'\n\n'+lead+'\n\n'
  for t in data['trials']:
   assembly=t['trial']=='assembly';task=('starterから組み立て' if assembly else '欠陥を入れた候補を修正') if ja else ('Assemble from the starter' if assembly else 'Repair an injected defect')
   seconds=t['subject_reported_elapsed_seconds'];minutes=t['subject_reported_elapsed_minutes'];approx=49 if assembly else 48
   elapsed=('約'+str(approx)+'分' if ja else 'About '+str(approx)+' min')+' ('+format(seconds,'.3f')+' s)'
   result='元48＋波形4 合格・負例棄却' if ja else 'Original 48 + waveform 4 PASS; fault rejected'
   html+='<tr><th scope="row">'+task+'</th><td>'+result+'</td><td>'+str(t['solver_repairs'])+('回' if ja else '')+'</td><td>'+elapsed+'</td></tr>'
   md+='- '+task+': '+result+'; '+str(t['solver_repairs'])+('回修正、' if ja else ' repairs; ')+elapsed+'; SHA256 `'+t['candidate_sha256']+'`.\n'
  html+='</tbody></table></div>'
  paragraphs=[
   ('修正回数は数値ソルバーへの変更を数え、初回実装を除きます。環境設定や補助スクリプトの修正は別に記録しました。所要時間は準備・実装/修正・新規計算・検証を含む報告値です。2試行は同じMacで並行しており、モデル速度の比較には使いません。','Repair counts cover numerical-solver revisions after initial implementation. Environment and auxiliary-script corrections are recorded separately. Reported elapsed time includes setup, development/repair, fresh computation and validation. Trials overlapped on one Mac and are not a model-speed comparison.'),
   ('費用金額・課金トークン・詳細なモデルIDは取得できませんでした。金額は未取得であり、0円ではありません。安価なモデルとの比較、アトラスなしとの比較、費用削減の実証は今回の範囲外です。','Monetary charges, billable tokens and the precise inherited model ID were unavailable. Unavailable cost is not zero. Lower-cost-model comparisons, Atlas-free controls and measured cost savings are outside this pilot.'),
  ]
  for jp,en in paragraphs:html+='<p>'+esc(jp if ja else en)+'</p>';md+='\n'+(jp if ja else en)+'\n'
  html+='<h2>'+('何を新しく計算し、どう確認したか' if ja else 'What was computed and checked')+'</h2>'
  scope=[
   ('各候補を--solverで選び、斜めエントロピー波12、x/yのSod・Shu–Osher24、Double Mach9、時間収束3の元48判定行を新規計算しました。時間比較の追加参照1本を含む実PDE出力は各49配列です。','Each candidate was selected explicitly with --solver for fresh computation of 12 oblique-wave, 24 x/y Sod/Shu–Osher, 9 Double Mach and 3 temporal-refinement rows. Each campaign produced 49 PDE arrays, including an additional temporal reference.'),
   ('波形4診断はp2/p3・x/yの保存出力から局所誤差、標準偏差比、相関を判定します。追加の4本のPDE計算ではありません。','Four waveform diagnostics evaluate local error, standard-deviation ratio and correlation from stored p2/p3 x/y outputs; they are not four additional PDE evolutions.'),
   ('別に保持した配布物の固定評価器で元48・波形4を再判定し、各49配列から240指標を再計算して一致を確認しました。元の配布295項目・判定基準・参照値は変更していません。故障版のyフラックスを実際に計算し、固定精度基準で棄却しました。','An independently held distribution supplied the frozen evaluators. The supervisor re-evaluated original 48/waveform 4 and matched 240 reconstructed metrics from each set of 49 arrays. All 295 distributed files, scientific criteria and references remained unchanged. A real faulty-y-flux computation was rejected by the fixed accuracy criteria.'),
   ('斜め波の最細格子間L₂次数は両候補とも2.0013 / 2.9747 / 4.0088。衝撃波のある全領域に2・3・4次収束を主張せず、Double Machは独立FV参照との広域構造比較です。正値性は指定した求積点・面・頂点の範囲です。','Both candidates gave finest-pair L2 orders 2.0013 / 2.9747 / 4.0088. No global high-order convergence across shocks is claimed. Double Mach checks broad structure against an independent FV reference; positivity covers the declared quadrature, face and corner points.'),
  ]
  html+='<ul>'
  for jp,en in scope:html+='<li>'+esc(jp if ja else en)+'</li>';md+='\n- '+(jp if ja else en)+'\n'
  html+='</ul><h2>'+('実験の条件と限界' if ja else 'Conditions and limits')+'</h2>'
  limits=[
   ('公開した日本語MD本文に固定の課題文を添え、会話履歴を引き継がない別エージェントで各1回実行しました。取得と環境準備は監督側が担当し、AIが実装・修正・実行を担当しました。','The unchanged published Japanese Markdown templates received fixed task context and were run once each by separate agents without inherited conversation history. The supervisor acquired inputs and prepared the environment; subjects implemented/repaired and executed the code.'),
   ('組み立ては未実装starterからSSPRK(5,4)・特性TVB・厳密1D入力の縮約を実装。短時間の方向差を見つけ、2回の修正後に全試験へ進みました。修正試験は事前に入れたSSPRK係数誤り1件で、原因を伏せて失敗JSONを渡しました。定数ODEの増分0.99dtから係数整合性を診断し、1回で修正しました。','Assembly started with the unfinished starter and implemented SSPRK(5,4), characteristic TVB and an invariant 1D restriction. A short directional diagnostic prompted two repairs before the full suite. The repair task used one pre-injected SSPRK coefficient defect with its cause withheld. The agent diagnosed a 0.99dt constant-ODE increment and repaired it once.'),
   ('完成ソースの参照は禁止しましたが、OSによる読取隔離ではありません。各1試行であり、一般的な成功率や任意のバグ修正能力は測っていません。','Reading completed implementations was prohibited by instructions, without OS-enforced read isolation. One trial per task does not measure a general success rate or arbitrary bug-repair ability.'),
   ('x/yの厳密1D入力は解析的縮約を使います。完全2D結合は斜め波とDouble Machで確認。既知の反転x追加試験は5/6合格のまま、今回の対象外です。MPI実行・他言語PDE・量子化学の追加計算は行っていません。','Exactly 1D x/y inputs use an analytic restriction; oblique waves and Double Mach exercise full 2D coupling. The historical reversed-x result remains 5/6, outside this qualification. No MPI, foreign-language PDE or new quantum-chemistry computation was performed.'),
  ]
  for jp,en in limits:html+='<p>'+esc(jp if ja else en)+'</p>';md+='\n'+(jp if ja else en)+'\n'
  html+='<details><summary>'+('検証中に見つかった事項' if ja else 'Issues observed during verification')+'</summary>'
  observations=[
   ('配布版をimportするpytest162件は未実装候補でも通ったため、候補そのものの合格には--solver指定の新規計算と固定評価器を使いました。','The 162 distribution-oriented pytest checks passed even with the unfinished candidate; candidate acceptance therefore used explicit --solver fresh runs and frozen evaluators.'),
   ('NumPy2.0.2の参照remap行列積で警告を保存。別プロセスでも再現しましたが、入力・出力は有限で、einsum経路との差は0でした。','NumPy2.0.2 reference-remap matmul warnings were retained and reproduced separately. Inputs/outputs were finite and matched an einsum contraction with zero maximum difference.'),
   ('監督側の追加照合v1はcallback時刻を完全一致とし、修正候補で失敗しました。配布ソルバー既存の終端処理（4eps×max(1,|T|)以内を最終時刻へ丸める）に合わせたv2で両候補を再照合。初回失敗を保持し、科学計算の基準や出力は変えていません。','Supervisor audit v1 incorrectly required bitwise callback-endpoint equality and failed on the repair data. Audit v2 follows the existing solver closure rule of 4eps×max(1,|T|). Both data sets were rechecked, preserving the first audit failure. Scientific criteria and outputs were unchanged.'),
  ]
  for jp,en in observations:html+='<p>'+esc(jp if ja else en)+'</p>';md+='\n'+(jp if ja else en)+'\n'
  linux_note=('Linuxの追加照合v2は、ほぼゼロの誤差ノルムを相対64epsだけで比較して24指標が不一致となりました（最大絶対差2.36×10⁻¹⁶未満）。元48・波形4の科学判定は合格です。別配布のv3は非ゼロの無次元指標に絶対64epsの丸め誤差床を加え、ゼロは完全一致を維持します。元ZIP・配列・記録値・科学判定基準は変更せず、初回失敗を保存しています。' if ja else 'Linux integrity audit v2 flagged 24 cancellation-dominated, near-zero metrics under a relative-only 64eps comparison (maximum absolute difference below 2.36e-16). Original 48 and waveform 4 scientific evaluators passed. Separate audit v3 adds an absolute 64eps rounding floor for nonzero dimensionless metrics and keeps zeros exact. The original ZIP, arrays, recorded values and scientific thresholds are unchanged; the first failure is retained.')
  html+='<p>'+esc(linux_note)+'</p>';md+='\n'+linux_note+'\n'
  html+='</details><h2>'+('保存データを追試する' if ja else 'Reassess the saved evidence')+'</h2>'
  how='baseキットr2と結果ZIPをそれぞれSHA256確認後に展開し、結果フォルダで次を実行します。NumPy2.0.2を使い、出力先は未使用フォルダにします。これは保存配列の再判定で、新しい全PDE計算ではありません。' if ja else 'SHA-verify and extract base kit r2 and the result ZIP separately. Run these commands from the result folder with NumPy2.0.2 and unused output paths. This reassesses saved arrays, not a fresh full PDE campaign.'
  command='python verify_saved_portable.py --bundle /path/to/atlas-rkdg-agent-pilot --trial assembly --base /path/to/atlas-rkdg-agent-kit --output /path/to/new-audit\npython verify_saved_portable.py --bundle /path/to/atlas-rkdg-agent-pilot --trial repair --base /path/to/atlas-rkdg-agent-kit --output /path/to/new-audit'
  portable=('別配布の照合v3を取得しSHA256を確認してください。元ZIPのv2は変更せず保持しています。' if ja else 'Download and SHA-verify the separate audit v3; the original ZIP and its audit v2 remain unchanged.')
  how+=' '+portable
  audit_links=link(cfg['portable_audit'],'Portable audit v3 / Python')+' · '+link(cfg['portable_audit']+'.sha256','SHA256')+' · '+link(cfg['route']+'evidence/linux-audit-v2-failure.json','Linux audit v2 failure / JSON')
  html+='<p>'+how+'</p><nav class="kit-actions">'+audit_links+'</nav><pre tabindex="0"><code>'+esc(command)+'</code></pre>'
  html+='<p class="kit-hash">SHA256 <code>'+cfg['archive_sha256']+'</code> · '+format(cfg['archive_bytes']/1e6,'.1f')+' MB · '+link(cfg['archive']+'.sha256','SHA256 file')+'</p>'
  for t in data['trials']:
   html+='<nav class="resource-nav">'+link(cfg['route']+'evidence/'+t['trial']+'/original-verdict.json',t['trial']+' original 48 / JSON')+link(cfg['route']+'evidence/'+t['trial']+'/waveform-verdict.json',t['trial']+' waveform 4 / JSON')+'</nav>'
  html+='<p>'+('実装コードは同梱MIT。論文・手法の一次文献と元の数式は' if ja else 'Code uses the bundled MIT license. Primary numerical-method references and equations are linked from the ')+link('/numerical-methods-atlas/agent-kits/rkdg2d/?lang='+lang,'RKDG開発キット' if ja else 'RKDG code kit')+('を参照してください。' if ja else '.')+'</p></section>'
  sections.append(html)
  md+='\n[Portable audit v3]('+ORIGIN+cfg['portable_audit']+') / [SHA256]('+ORIGIN+cfg['portable_audit']+'.sha256) / [Linux audit v2 failure]('+ORIGIN+cfg['route']+'evidence/linux-audit-v2-failure.json)\n'
  md+='\n## '+('保存データの再判定' if ja else 'Saved-data reassessment')+'\n\n'+how+'\n\n```sh\n'+command+'\n```\n\n[ZIP]('+ORIGIN+cfg['archive']+') / [SHA256]('+ORIGIN+cfg['archive']+'.sha256)\n\n[Source kit / primary references]('+ORIGIN+'/numerical-methods-atlas/agent-kits/rkdg2d/?lang='+lang+')\n'
  (dest/('index.md' if ja else 'index-en.md')).write_text(md)
 css='/styles/atlas-agent-kits.css';version=hashlib.sha256((root/css.lstrip('/')).read_bytes()).hexdigest()[:12]
 (dest/'index.html').write_text('<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title data-page-title-ja="RKDGプロンプト実測 | 数値計算法アトラス" data-page-title-en="RKDG agent pilot | Numerical Methods Atlas">RKDGプロンプト実測 | 数値計算法アトラス</title><meta name="description" content="AIエージェントによるRKDG組み立てと修正の実測。元48ケース・波形4診断、修正2/1回、約49/48分と検証範囲。"><link rel="canonical" href="'+ORIGIN+cfg['route']+'"><link rel="stylesheet" href="/styles/atlas-resources.css"><link rel="stylesheet" href="'+css+'?v='+version+'"></head><body class="profile-page"><main class="profile-main atlas-resource-main agent-kit" id="main">'+''.join(sections)+'</main></body></html>\n')
 (dest/'index.json').write_text(json.dumps({**cfg,'summary':ORIGIN+cfg['route']+'summary.json','languages':['ja','en'],'fresh_pde_rerun_by_page_builder':False},indent=2)+'\n')
 return cfg

def highlight(cfg,lang):
 ja=lang=='ja'
 return '<section class="kit-pilot-highlight"><h2>'+('AIエージェントで実際に試しました' if ja else 'Tested with actual AI agents')+'</h2><p>'+('2試行とも元48ケース＋波形4診断に合格。組み立ては修正2回・約49分、欠陥修正は1回・約48分。時間は共有Macでの準備・計算・検証込み、費用は未取得です。' if ja else 'Both trials passed original 48 + waveform 4. Assembly: 2 repairs, about 49 min. Defect repair: 1 repair, about 48 min. Times include setup, computation and verification on a shared Mac. Monetary cost is unavailable.')+'</p><a href="'+cfg['route']+'?lang='+lang+'">'+('実測結果・検証範囲・生配列を見る' if ja else 'View measurements, scope and raw evidence')+'</a></section>'
