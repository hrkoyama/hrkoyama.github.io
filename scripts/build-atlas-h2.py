#!/usr/bin/env python3
"""Build bilingual H2-RHF reading from original prose and frozen measured data.

This build never executes scientific code or regenerates an independent reference.
It fails when the frozen package or its successful numerical records are absent.
"""
from pathlib import Path
from html import escape as e
import hashlib
import json
import re
import struct
import subprocess
import struct
import xml.etree.ElementTree as ET
from atlas_reading_presentation import specialized_reading_layout

ROOT=Path(__file__).resolve().parents[1]
ATLAS=ROOT/'numerical-methods-atlas'
SOURCE='/catalog/atlas-h2-reading.json'
ORIGIN='https://hrkoyama.github.io'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()


def read(path):return json.loads(path.read_text())
def dump(path,value):path.write_text(json.dumps(value,ensure_ascii=False,indent=2,allow_nan=False)+'\n')
def link(url,label):return '<a href="'+e(url,quote=True)+'">'+e(label)+'</a>'
def para(text):return '<p>'+e(text)+'</p>'
def heading(ident,title):return '<h2 id="'+ident+'">'+e(title)+'</h2>'
def route(lang):return '/numerical-methods-atlas/'+lang+'/read/h2-hf/'


def number(value):
    if isinstance(value,bool):return str(value).lower()
    if isinstance(value,(int,float)):return format(value,'.12g')
    return str(value)


def table(headers,rows,label):
    return '<div class="h2-table" tabindex="0" role="region" aria-label="'+e(label)+'"><table><thead><tr>'+''.join('<th scope="col">'+e(h)+'</th>' for h in headers)+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+e(number(v))+'</td>' for v in row)+'</tr>' for row in rows)+'</tbody></table></div>'


def measured(results,lang,base):
    ja=lang=='ja'
    body=heading('measured-results','保存した実測結果を読む' if ja else 'Reading the stored measurements')
    body+=para('次の値は公開版の固定入力から得た結果です。しきい値・停止条件・全反復履歴は入力とJSONに保存し、SCF反復、基底の変更、独立実装との差を別々に示します。表示の丸め値で再判定せず、機械判定は元のJSONの値で行います。' if ja else 'These values come from the release’s fixed inputs. Inputs and JSON retain thresholds, stopping rules and complete iteration histories. SCF iterations, basis changes and independent-implementation differences are shown separately. Numerical acceptance uses the original JSON values, not rounded display values.')
    metrics=results['metrics']
    names={
        'max_reference_energy_error':('独立参照との全エネルギー最大差 / hartree','Maximum total-energy difference from independent reference / hartree'),
        'max_scf_commutator':('最終SCF交換子ノルムの最大値','Maximum final SCF commutator norm'),
        'max_orthogonality_error':('軌道直交性の最大誤差','Maximum orbital orthogonality error'),
        'max_electron_count_error':('電子数の最大誤差','Maximum electron-count error'),
        'max_energy_consistency_error':('行列トレースと占有軌道の別式による最大エネルギー差 / hartree','Maximum trace/occupied-orbital energy difference / hartree'),
        'max_idempotency_error':('最終密度の冪等条件の最大残差','Maximum final-density idempotency residual'),
        'basis_energy_increase_max':('入れ子基底系列での最大エネルギー上昇 / hartree','Maximum energy increase in the nested basis sequence / hartree'),
        'last_basis_energy_change_max':('系列末尾の基底差の最大値 / hartree','Maximum last-basis energy change / hartree'),
        'last_two_basis_changes_max':('系列末尾2回の基底差の最大値 / hartree','Maximum energy change over the final two basis additions / hartree'),
        'scf_tolerance_energy_error_max':('SCF許容誤差走査と厳しい設定の最大差 / hartree','Maximum tolerance-sweep difference from the tight solution / hartree'),
    }
    assert all(k in metrics for k in names),'H2 metric schema changed; update reading explicitly'
    body+=table(['確認した量','実測値'] if ja else ['Measured quantity','Value'],[(names[k][0 if ja else 1],metrics[k]) for k in names],'数値検査の要約' if ja else 'Numerical check summary')
    rows=results['cases']
    assert rows and all(r['converged'] for r in rows),'Unconverged cases cannot be presented as successful reading evidence'
    body+=heading('geometry-and-basis-results','核間距離・基底ごとの比較' if ja else 'Comparisons by bond length and basis')
    body+=para('Rの単位はbohr、Eは核間反発を含む全エネルギー（hartree）です。基底IDは同梱入力の定義と対応します。重なり行列の最小固有値と条件数を併記し、基底を増やすことによる悪条件化も確認できます。' if ja else 'R is in bohr; E is total energy including nuclear repulsion, in hartree. Basis IDs refer to definitions in the packaged input. The minimum overlap eigenvalue and condition number expose conditioning changes during expansion.')
    body+=table(['R / bohr','基底' if ja else 'Basis','関数数' if ja else 'Functions','E / hartree','|E−E(PySCF)|','||R(SCF)||','λmin(S)','κ₂(S)','反復' if ja else 'Iterations'],[
        [r['bond_bohr'],r['basis_id'],r['nbf'],r['energy_total'],r['energy_error'],r['scf_commutator_norm'],r['overlap_min_eigenvalue'],r['overlap_condition_number'],r['iterations']] for r in rows
    ],'核間距離と基底の結果' if ja else 'Geometry and basis results')
    body+=heading('nested-basis-target','入れ子基底系列の停止目安' if ja else 'Stopping diagnostic for the nested basis sequence')
    body+=para('各核間距離について、系列末尾の2回の基底追加を調べます。最大エネルギー変化と入力の目標値を並べています。目標を満たしても、s型以外の関数や完全基底極限による誤差を評価したことにはなりません。' if ja else 'For each separation, inspect the final two additions in the nested sequence. The maximum energy increment is compared with the input target. Meeting this target does not assess missing angular functions or establish a complete-basis error.')
    refinement=results['basis_refinement'];assert refinement
    body+=table(['R / bohr','最終基底' if ja else 'Final basis','末尾2回の最大|ΔE| / hartree' if ja else 'Max |ΔE|, final two additions / hartree','入力の目標 / hartree' if ja else 'Input target / hartree','目標を満たす' if ja else 'Target met'],[
        [r['bond_bohr'],r['basis_ids'][-1],r['last_two_changes_max'],r['target'],r['target_reached']] for r in refinement
    ],'入れ子基底の指定公差' if ja else 'Stated nested-basis target')
    body+=heading('scf-tolerance-results','SCFの許容誤差だけを変える' if ja else 'Changing only SCF tolerances')
    body+=para('同じ幾何と基底で許容誤差を走査します。各点の終了理由、交換子残差、厳しいSCF設定とのエネルギー差を読みます。この走査を基底誤差や物理モデルの誤差と呼びません。' if ja else 'Tolerance sweeps keep geometry and basis fixed. Inspect termination, commutator residual and energy difference from the tight setting. This sweep does not measure basis error or physical-model error.')
    sweep=results['tolerance_sweep'];assert sweep
    body+=table(['R / bohr','基底' if ja else 'Basis','設定' if ja else 'Setting','反復' if ja else 'Iterations','E / hartree','|E−E(tight)|','||R(SCF)||','終了理由' if ja else 'Termination'],[
        [r['bond_bohr'],r['basis_id'],r['level'],r['iterations'],r['energy_total'],r['energy_error_to_tight'],r['scf_commutator_norm'],r['termination']] for r in sweep
    ],'SCF許容誤差走査' if ja else 'SCF tolerance sweep')
    image=ROOT/(base+'results/preview.png').lstrip('/')
    if image.is_file():
        png=image.read_bytes();assert png[:8]==b'\x89PNG\r\n\x1a\n';width,height=struct.unpack('>II',png[16:24])
        body+='<figure><img src="'+base+'results/preview.png" width="'+str(width)+'" height="'+str(height)+'" loading="lazy" alt="'+('固定入力のH₂ RHF基底・SCF収束の保存図' if ja else 'Stored fixed-input H2 RHF basis and SCF convergence plot')+'"><figcaption>'+('図は保存済み計算の可視化です。判定には入力と結果JSONの条件・数値を使います。' if ja else 'The figure visualizes stored calculations. Acceptance uses the criteria and values in the input/result JSON.')+'</figcaption></figure>'
    body+='<p>'+link(base+'results/result.json','全結果 / JSON' if ja else 'Full results / JSON')+' · '+link(base+'results/solution.csv','基底・幾何のCSV' if ja else 'Basis/geometry CSV')+' · '+link(base+'results/scf.csv','SCF履歴 / CSV' if ja else 'SCF histories / CSV')+'</p>'
    return body


def build():
    data=read(ROOT/SOURCE.lstrip('/'));package=data['package'];base=package['base'];release=ROOT/base.lstrip('/')
    result_path=release/package['results'];results=read(result_path)
    assert results['case']==data['example_id'] and results['passed'] is True and all(v is True for v in results['checks'].values())
    assert sha(release/package['input'])==results['input_sha256']
    assert sha(release/package['reference'])==results['reference_sha256']
    manifest=read(release/'source-manifest.json');verification=read(release/'verification.json')
    assert verification['failures']==verification['errors']==0
    for name,digest in manifest['files'].items():assert sha(release/name)==digest,name
    source_hash=sha(ROOT/SOURCE.lstrip('/'))
    sources={SOURCE.lstrip('/'):source_hash,(base+package['results']).lstrip('/'):sha(result_path),(base+'source-manifest.json').lstrip('/'):sha(release/'source-manifest.json'),(base+'verification.json').lstrip('/'):sha(release/'verification.json')}
    methods={m['id']:m for m in read(ROOT/'catalog/atlas-methods.json')['methods']};assert all(i in methods for i in data['methods'])
    rendered=json.loads(subprocess.check_output(['node','scripts/render-atlas-math.cjs'],cwd=ROOT,input=json.dumps([{'id':k,'formula':[v]} for k,v in data['formulas'].items()]).encode()))['rendered']
    references={r['id']:r for r in data['references']};documents={lang:read(ATLAS/f'content.{lang}.json') for lang in ['ja','en']}
    translations=read(ATLAS/'translation-status.json')
    for lang in ['ja','en']:
        ja=lang=='ja';title=data['title'][lang]
        body='<h1>'+e(title)+'</h1>'+para(data['intro'][lang])
        body+='<aside class="resource-summary">'+para('この実装は孤立した2電子H₂の有限s型基底RHFです。一般の分子HF、完全基底極限、相関を含む正しい解離曲線、分子・周期DFTの実装ではありません。' if ja else 'This implementation covers isolated two-electron H2 RHF in finite s-only bases. It does not implement general molecular HF, establish a complete-basis limit, recover the correlated dissociation curve, or supply molecular/periodic DFT.')+'</aside>'
        opening = body
        body+='<nav class="resource-nav">'+link('/numerical-methods-atlas/code-and-data/examples/h2-rhf/?lang='+lang,'固定入力・コード・テスト・判定条件' if ja else 'Fixed input, code, tests and acceptance')+' · '+link(base+'molecular-hf-2026-11-22.zip','ZIP')+' · '+link(base+'verification.json','独立展開の検証 / JSON' if ja else 'Independent-extraction verification / JSON')+'</nav>'
        markdown='# '+title+'\n\n'+data['intro'][lang]+'\n\n'
        for section in data['sections']:
            body+=heading(section['id'],section['title'][lang])+''.join(para(p) for p in section['paragraphs'][lang])
            body+=''.join('<div class="math-block">'+rendered[f][0]+'</div>' for f in section['formulas'])
            body+='<p class="h2-citations">'+('関連出典：' if ja else 'Sources: ')+', '.join(link('#source-'+i,references[i]['author']+' ('+str(references[i]['year'])+')') for i in section['references'])+'</p>'
            markdown+='## '+section['title'][lang]+'\n\n'+'\n\n'.join(section['paragraphs'][lang])+'\n\n'+''.join('$$\n'+data['formulas'][f]+'\n$$\n\n' for f in section['formulas'])
        body+=measured(results,lang,base)
        body+=heading('run-and-check','取得して結果を確かめる' if ja else 'Download and verify the result')
        body+=para('ZIP内の配布版フォルダで依存関係を導入し、同梱の固定入力を使います。結果の出力先は新規または空のディレクトリを指定します。独立参照の再生成はPySCFを用いる別工程で、通常のrunnerは保存済み参照を照合します。' if ja else 'Install dependencies in the extracted edition directory, then use its fixed input. Choose a new or empty output directory. Regenerating the independent reference with PySCF is a separate operation; the ordinary runner compares against the saved reference.')
        body+='<pre><code>python -m pip install -r requirements.txt\npython -m pytest -q\npython run.py --input inputs.json --output output</code></pre><p>'+link(base+package['input'],'固定入力 / JSON' if ja else 'Fixed input / JSON')+' · '+link(base+'run.py','Runner')+' · '+link(base+package['reference'],'PySCF独立参照 / JSON' if ja else 'Independent PySCF reference / JSON')+' · '+link('/numerical-methods-atlas/code-and-data/examples/h2-rhf/?lang='+lang,'版・受入条件・引用の共通手順' if ja else 'Edition, acceptance criteria and citation')+'</p>'
        body+=heading('sources','一次文献・関連資料と確認範囲' if ja else 'Primary publications, supporting sources and review scope')+para('書誌確認、抄録の参照、公式資料の該当箇所の確認を区別します。論文の全文や第三者のソースコードは配布していません。下の出典は方法の系譜と独立参照を示し、この教材による論文全体の再現を意味しません。' if ja else 'Bibliographic, abstract and relevant-documentation checks are distinguished below. Full papers and third-party source code are not redistributed. Sources identify method provenance and the independent reference, not full-paper reproductions by this tutorial.')+'<ol>'
        for r in data['references']:
            body+='<li id="source-'+r['id']+'">'+link(r['source'],r['author']+' ('+str(r['year'])+'). '+r['title'])+'. '+e(r['journal'])+para(r['review'][lang])+'</li>'
        body+='</ol>'
        headings=[{'level':2,'id':i,'title':re.sub('<[^>]+>','',t)} for i,t in re.findall(r'<h2 id="([a-z0-9-]+)">(.*?)</h2>',body,re.S)]
        entry={'title':title,'html':body,'headings':headings,'locale':lang,'source_url':SOURCE,'updated_on':data['updated_on']}
        if ja:entry['translation_status']='draft'
        documents[lang]['h2-hf']=entry
        directory=ROOT/route(lang).lstrip('/');directory.mkdir(parents=True,exist_ok=True)
        nav='<nav class="resource-nav">'+link(f'/numerical-methods-atlas/{lang}/read/','解説章の目次' if ja else 'Reading contents')+' · '+link(SOURCE,'編集用正本 / JSON' if ja else 'Editable source / JSON')+' · '+link(route(lang)+'index.json','JSON')+' · '+link(route(lang)+'index.md','Markdown')+'</nav>'
        toc='<nav aria-label="'+('この章の目次' if ja else 'On this page')+'">'+''.join(link('#'+h['id'],h['title']) for h in headings)+'</nav>'
        style='<style>.h2-reading{max-width:1100px;margin:auto;padding:1.2rem}.h2-reading .prose{max-width:84ch;margin:auto}.h2-reading .resource-nav,.h2-reading>nav{display:flex;flex-wrap:wrap;gap:.5rem}.h2-reading>nav a{padding:.3rem}.h2-reading .math-block,.h2-table{max-width:100%;overflow-x:auto}.h2-table{margin:1rem 0}.h2-table table{border-collapse:collapse;min-width:100%;font-size:.95rem}.h2-table td,.h2-table th{border-bottom:1px solid #becbc3;padding:.55rem;text-align:left}.h2-table td:not(:first-child){font-variant-numeric:tabular-nums;white-space:nowrap}.h2-reading img{width:100%;height:auto}.h2-reading pre{white-space:pre;overflow:auto;padding:1rem;background:#eef3ef}.h2-reading li{margin-bottom:1rem}.h2-reading h2{scroll-margin-top:1rem}.h2-citations{font-size:.95rem}.h2-reading .resource-summary{border-left:4px solid #386552;padding:.3rem 1rem;background:#eef3ef}.h2-reading{overflow-wrap:anywhere}</style>'
        style = style.replace('</style>', '.h2-reading .specialized-reading-toc{margin:1rem 0}.h2-reading .specialized-reading-toc>summary{min-height:44px;box-sizing:border-box;padding:.5rem 0;cursor:pointer}.h2-reading .specialized-reading-toc>nav{display:flex;flex-wrap:wrap;gap:.5rem 1rem;padding:.6rem 0}</style>', 1)
        document='<!doctype html><html lang="'+lang+'"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+e(title)+' | Numerical Methods Atlas</title><meta name="description" content="'+e(data['intro'][lang],quote=True)+'"><link rel="canonical" href="'+ORIGIN+route(lang)+'">'+''.join('<link rel="alternate" hreflang="'+l+'" href="'+ORIGIN+route(l)+'">' for l in ['ja','en'])+'<link rel="stylesheet" href="/numerical-methods-atlas/vendor/katex.min.css"><link rel="stylesheet" href="/numerical-methods-atlas/style.css"><link rel="stylesheet" href="/styles/atlas-resources.css">'+style+'</head><body class="profile-page" data-content-language="'+lang+'"><main id="main" class="h2-reading">'+specialized_reading_layout(nav, toc, body, opening, lang, plain_toc=True)+'</main></body></html>\n'
        (directory/'index.html').write_text(document)
        dump(directory/'index.json',{**entry,'url':ORIGIN+route(lang),'methods':data['methods'],'execution_example':'h2-rhf','references':data['references'],'source_sha256':sources,'measurements':results['metrics']})
        markdown+='## '+('保存した実測値' if ja else 'Stored measurements')+'\n\n'+'\n'.join('- '+k+': '+number(v) for k,v in results['metrics'].items())+'\n\n'+ORIGIN+base+package['results']+'\n\n'
        markdown+='## '+('実行' if ja else 'Execution')+'\n\n```sh\npython -m pip install -r requirements.txt\npython -m pytest -q\npython run.py --input inputs.json --output output\n```\n\n'+ORIGIN+'/numerical-methods-atlas/code-and-data/examples/h2-rhf/?lang='+lang+'\n\n'
        markdown+='## '+('文献' if ja else 'Sources')+'\n\n'+'\n'.join('- '+r['author']+' ('+str(r['year'])+'). '+r['title']+'. '+r['source']+' — '+r['review'][lang] for r in data['references'])+'\n'
        (directory/'index.md').write_text(markdown)
        path=ATLAS/lang/'read/index.html';text=re.sub(r'<!-- h2-reading -->.*?<!-- /h2-reading -->','',path.read_text(),flags=re.S)
        block='<!-- h2-reading --><section class="page-width"><h2>'+('H₂分子の実装と収束確認' if ja else 'H2 implementation and convergence checks')+'</h2><p>'+link(route(lang),title)+'</p></section><!-- /h2-reading -->'
        path.write_text(text.replace('</main>',block+'</main>'))
        translations['chapters']['h2-hf']={'status':'draft','source_url':SOURCE,'source_sha256':source_hash,'checked_on':data['updated_on']}
    for lang,docs in documents.items():
        dump(ATLAS/f'content.{lang}.json',docs)
        if lang=='en':dump(ATLAS/'content.json',docs)
    translations.update(total=len(documents['en']),translated=sum(k in documents['ja'] for k in documents['en']),reviewed=sum(r['status']=='reviewed' for r in translations['chapters'].values()));dump(ATLAS/'translation-status.json',translations)
    path=ATLAS/'home-search-index.json';index=read(path);index['entries']=[r for r in index['entries'] if r.get('origin')!='h2-reading']
    index['entries'].append({'id':'reading-h2-hf','title':data['title'],'headings':{lang:documents[lang]['h2-hf']['headings'] for lang in ['ja','en']},'keywords':data['keywords'],'routes':{lang:route(lang) for lang in ['ja','en']},'origin':'h2-reading','kind':'chapter'});dump(path,index)
    path=ATLAS/'sitemap.xml';tree=ET.parse(path);xml=tree.getroot();ns='{http://www.sitemaps.org/schemas/sitemap/0.9}';existing={r.text for r in xml.findall('.//{*}loc')}
    for lang in ['ja','en']:
        url=ORIGIN+route(lang)
        if url not in existing:ET.SubElement(ET.SubElement(xml,ns+'url'),ns+'loc').text=url
    ET.register_namespace('',ns[1:-1]);tree.write(path,encoding='utf-8',xml_declaration=True)
    print('Built bilingual H2 RHF reading from',len(results['cases']),'measured geometry/basis cases and',len(results['tolerance_sweep']),'SCF-tolerance cases.')


if __name__=='__main__':build()
