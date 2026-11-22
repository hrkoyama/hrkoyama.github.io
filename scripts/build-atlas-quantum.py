#!/usr/bin/env python3
"""Publish the curated quantum reading, bibliography and honest coverage counts.

This offline build integrates separately executed and verified atomic examples.
"""
from collections import Counter
import hashlib
import html
import json
from pathlib import Path
import re
import subprocess
from urllib.parse import urlparse
import xml.etree.ElementTree as ET
from atlas_execution_discovery import load_discovery
from atlas_equation_availability import equation_evidence

ROOT=Path(__file__).resolve().parents[1]
ATLAS=ROOT/'numerical-methods-atlas'
ORIGIN='https://hrkoyama.github.io'
load=lambda p:json.loads(p.read_text())
write=lambda p,d:p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
esc=html.escape
data=load(ROOT/'catalog/atlas-quantum.json')
queue=load(ROOT/'catalog/atlas-work-queue.json')
methods={x['id']:x for x in load(ROOT/'catalog/atlas-methods.json')['methods'] if x['group']['id']=='quantum'}
assert {x['id'] for x in data['sections']}==set(methods)
examples=load(ROOT/'catalog/atlas-quantum-examples.json')
case_ids={x['id'] for x in examples['cases']}
assert all(x['status'] in ['reading-only','educational-example'] and not x['code_modules'] and not x['test_files'] for x in methods.values())
assert all(set(x.get('quantum_examples',[]))<=case_ids and (x['status']!='educational-example' or x.get('quantum_examples') or x.get('molecular_examples') or x.get('periodic_examples')) for x in methods.values())
total_problems=len(load(ROOT/'catalog/atlas-test-problems.json')['problems'])
refs={x['id']:x for x in data['references']}
assert len(refs)==len(data['references'])
assert len({x['doi'].lower() for x in refs.values()})==len(refs)
assert all(x['references'] and all(r in refs for r in x['references']) for x in data['sections'])
math_records=data['sections']+[child for x in data['sections'] for child in x.get('subsections',[])]
math=json.loads(subprocess.run(['node','scripts/render-atlas-math.cjs'],cwd=ROOT,input=json.dumps(math_records),text=True,capture_output=True,check=True).stdout)['rendered']
def link(url,label):return '<a href="'+esc(url)+'">'+esc(label)+'</a>'
def paragraph(text):return '<p>'+esc(text)+'</p>'
def reference(r):return esc(r['author'].replace(' and ','; '))+f' ({r["year"]}). '+link(r['source'],r['title'])+'. '+esc(r['journal'])+'.'
bodies={}
for lang in ['ja','en']:
    ja=lang=='ja';route=f'/numerical-methods-atlas/{lang}/read/quantum-chemistry/'
    body='<p class="eyebrow">ELECTRONIC STRUCTURE · QUANTUM CHEMISTRY · DFT</p><h1>'+esc(data['title'][lang])+'</h1><p class="intro">'+esc(data['description'][lang])+'</p>'
    body+='<p class="resource-summary">'+(f'{len(methods)}項目の日英解説と{len(refs)}件の一次文献を公開。水素型原子・Heの2問題群と、H₂の限定した有限基底RHFに実行・検証例があります。周期He固定セルのLDA実行例も公開。一般の分子DFT・他の周期物質は未検証です。' if ja else f'Bilingual reading for {len(methods)} entries and {len(refs)} primary publications. Runnable validation covers two hydrogenic/He families and scoped finite-basis H₂ RHF. A fixed periodic-He LDA workflow is also available; general molecular DFT and other periodic materials remain unvalidated.')+'</p>'
    body+='<nav class="resource-nav">'+''.join(link(u,t) for u,t in [('/numerical-methods-atlas/?lang='+lang,'アトラス冒頭' if ja else 'Atlas home'),('/numerical-methods-atlas/methods/?lang='+lang+'#quantum-'+lang,'手法の見取り図' if ja else 'Method map'),('/numerical-methods-atlas/equations/?lang='+lang+'#quantum-'+lang,'数式から探す' if ja else 'Browse by equation'),(f'/numerical-methods-atlas/{lang}/read/quantum-atoms/','水素型原子・Heを実行する' if ja else 'Run hydrogenic / He examples'),('#verification','実行・検証と次の計画' if ja else 'Runnable examples and next plans'),('#sources','一次文献と公式資料' if ja else 'Primary sources and documentation')])+'</nav>'
    body+='<h2 id="how-to-read">'+('最初に分けて考える3つのこと' if ja else 'Three choices to keep separate')+'</h2><div class="quantum-terms">'
    choices=[('物理モデル・近似','Physical model and approximation','HF、KS-DFT、MP2、CI、CC等。どの多電子状態やエネルギーを近似するか。','HF, KS-DFT, MP2, CI or CC: which many-electron states and energies are approximated?'),('表現・離散化','Representation and discretization','基底、格子、擬ポテンシャル、k点。モデルを有限の計算問題にする方法。','Basis, grid, pseudopotential and k sampling: how is the model made finite?'),('方程式の解き方','Equation solver','固有値計算、SCF、混合、DIIS。選んだ離散問題をどこまで解いたか。','Eigensolvers, SCF, mixing and DIIS: how accurately is the chosen discrete problem solved?')]
    for jh,eh,jp,ep in choices:body+='<div><h3>'+esc(jh if ja else eh)+'</h3>'+paragraph(jp if ja else ep)+'</div>'
    body+='</div>'+paragraph('「SCFが収束した」「基底が収束した」「物理モデルが妥当」は別の確認です。代表式は原子単位系（ℏ = m_e = e = 4πε₀ = 1）を用います。有限の分子と周期的な固体は境界条件も違います。' if ja else 'SCF convergence, basis convergence and physical adequacy are distinct checks. Representative equations use atomic units (ℏ = m_e = e = 4πε₀ = 1). Finite molecules and periodic solids also require different boundaries.')
    body+='<nav class="quantum-map" aria-label="'+('分野の見取り図' if ja else 'Field map')+'">'
    for lane in data['lanes']:
        body+='<section><h2>'+esc(lane[lang])+'</h2><ul>'+''.join('<li>'+link('#'+x['id'],methods[x['id']]['name'][lang])+'</li>' for x in data['sections'] if x['lane']==lane['id'])+'</ul></section>'
    body+='</nav>'
    for x in data['sections']:
        body+='<section class="quantum-entry" data-quantum-id="'+x['id']+'"><h2 id="'+x['id']+'">'+esc(methods[x['id']]['name'][lang])+'</h2>'
        body+=''.join(paragraph(p) for p in x['paragraphs'][lang])
        if methods[x['id']].get('quantum_examples'):
            body+='<p class="resource-summary">'+esc(methods[x['id']]['example_scope'][lang])+' '+link(f'/numerical-methods-atlas/{lang}/read/quantum-atoms/','固定入力・コード・検証結果' if ja else 'Fixed inputs, code and measured checks')+'</p>'
        if methods[x['id']].get('molecular_examples'):
            body+='<p class="resource-summary">'+esc(methods[x['id']]['molecular_scope'][lang])+' '+link(f'/numerical-methods-atlas/{lang}/read/h2-hf/','H₂の入力・コード・独立参照・収束' if ja else 'H₂ inputs, code, independent references and refinement')+'</p>'
        if methods[x['id']].get('periodic_examples'):
            body+='<p class="resource-summary">'+esc(methods[x['id']]['periodic_scope'][lang])+' '+link(f'/numerical-methods-atlas/{lang}/read/periodic-dft/','周期DFTの条件・コード・収束・独立参照' if ja else 'Periodic DFT conditions, code, convergence and independent reference')+'</p>'
        if methods[x['id']].get('force_examples'):
            body+='<p class="resource-summary">'+esc(methods[x['id']]['force_scope'][lang])+' '+link(f'/numerical-methods-atlas/{lang}/read/periodic-forces/','原子間力・有限差分・独立参照・BOMD接続' if ja else 'Atomic forces, finite differences, independent reference and BOMD interface')+'</p>'
        if math[x['id']]:
            body+='<div class="quantum-math">'+''.join(math[x['id']])+'</div>'
            if any(len(f)>90 for f in x['formula']):body+='<p class="quantum-scroll-note">'+('長い式は横にスクロールできます。' if ja else 'Long equations scroll horizontally.')+'</p>'
        for child in x.get('subsections',[]):
            body+='<section class="quantum-subsection"><h3 id="'+child['id']+'">'+esc(child['title'][lang])+'</h3>'+''.join(paragraph(p) for p in child['paragraphs'][lang])
            if math[child['id']]:body+='<div class="quantum-math">'+''.join(math[child['id']])+'</div>'
            body+='</section>'
        body+='<p class="quantum-caution">'+esc(x['caution'][lang])+'</p><p>'+link('/numerical-methods-atlas/methods/'+x['id']+'/?lang='+lang,'条件・実装状況・JSON' if ja else 'Assumptions, implementation status and JSON')+'</p><ul>'
        body+=''.join('<li>'+link('#ref-'+r,refs[r]['author'].replace(' and ','; ')+f' ({refs[r]["year"]})')+'</li>' for r in x['references'])+'</ul></section>'
    body+='<section><h2 id="verification">'+('実行・検証例と次の計画' if ja else 'Runnable validation examples and next plans')+'</h2>'+paragraph(f'水素型原子・Heの2問題群を実行し、独立参照と比較して全{total_problems}問題の台帳へ加えました。さらにH₂の有限基底RHFを独立参照・SCFと基底の収束で検証しました。周期Heセルの限定DFTも追加。分子DFT・FCIや他の周期物質へ検証を拡張していません。' if ja else f'Two hydrogenic/He problem families were executed, independently compared and added to the {total_problems}-problem inventory. A scoped H₂ finite-basis RHF example now adds independent-reference, SCF and basis checks. A scoped periodic-He DFT workflow is now added; molecular DFT, FCI and other periodic materials are not validated.')
    for x in data['verification_plan']:
        state=('実行・検証例あり' if ja else 'Runnable and checked') if x['state']=='verified-educational-example' else 'Under construction'
        body+='<article class="quantum-plan"><p class="resource-status">'+state+'</p><h3>'+esc(x['title'][lang])+'</h3>'+paragraph(x['check'][lang])
        if x.get('url'):body+='<p>'+link(x['url'][lang],'結果・実行手順' if ja else 'Results and reproduction')+'</p>'
        body+='</article>'
    body+='</section><section><h2 id="further-topics">'+('今後広げる項目' if ja else 'Further topics to develop')+'</h2>'+paragraph('以下は追加候補です。この導入で専用解説・実装を提供しているという意味ではありません。AMR・並列化・mixed precisionは既存の収録方針どおり対象外です。' if ja else 'These are extension candidates, not dedicated readings or implementations already supplied here. AMR, parallelization and mixed precision remain outside the editorial scope.')+'<ul>'+''.join('<li>'+esc(x)+'</li>' for x in data['future_topics'][lang])+'</ul></section>'
    body+='<section><h2 id="sources">'+('一次文献と確認範囲' if ja else 'Primary publications and review scope')+'</h2>'+paragraph(data['source_policy'][lang])+'<ol class="quantum-references">'
    for r in sorted(refs.values(),key=lambda x:(x['year'],x['id'])):body+='<li id="ref-'+r['id']+'"><cite>'+reference(r)+'</cite></li>'
    body+='</ol><h3>'+('実装を調べるための公式資料' if ja else 'Official implementation documentation')+'</h3>'+paragraph('以下は外部ソフトウェアの資料です。このアトラスで実行・検証済みであることは意味しません。' if ja else 'These describe external software; linking them does not claim an atlas-verified run.')+'<ul>'+''.join('<li>'+link(x['url'],x['label'])+'</li>' for x in data['documentation'])+'</ul></section><p>'+link('/catalog/atlas-quantum.json','本文・式・出典 / JSON' if ja else 'Text, formulas and sources / JSON')+' · '+link('/using/?lang='+lang,'利用と引用' if ja else 'Use and citation')+'</p>'
    bodies[lang]=body
    other='en' if ja else 'ja'
    head='<!doctype html><html lang="'+lang+'"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+esc(data['title'][lang])+' | Numerical Methods Atlas</title><meta name="description" content="'+esc(data['description'][lang])+'"><link rel="canonical" href="'+ORIGIN+route+'"><link rel="alternate" hreflang="'+other+'" href="'+ORIGIN+f'/numerical-methods-atlas/{other}/read/quantum-chemistry/'+'"><link rel="stylesheet" href="/numerical-methods-atlas/vendor/katex.min.css">'
    for name in ['atlas-resources','atlas-quantum']:head+='<link rel="stylesheet" href="/styles/'+name+'.css?v='+sha(ROOT/'styles'/(name+'.css'))[:12]+'">'
    dest=ROOT/route.lstrip('/');dest.mkdir(parents=True,exist_ok=True)
    structured={'@context':'https://schema.org','@type':'LearningResource','name':data['title'][lang],'description':data['description'][lang],'inLanguage':lang,'url':ORIGIN+route,'dateModified':data['reviewed_on'],'educationalLevel':'Graduate','learningResourceType':'Introductory survey','citation':[r['source'] for r in refs.values()]}
    (dest/'index.html').write_text(head+'<script type="application/ld+json">'+json.dumps(structured,ensure_ascii=False).replace('<','\\u003c')+'</script></head><body class="profile-page"><main id="main" class="profile-main atlas-resource-main atlas-quantum-main">'+body+'</main></body></html>\n')
    path=ATLAS/lang/'read/index.html';text=re.sub(r'<!-- quantum-entry -->.*?<!-- /quantum-entry -->','',path.read_text(),flags=re.S)
    text=text.replace('</main>','<!-- quantum-entry --><section class="page-width"><h2>'+link(route,data['title'][lang])+'</h2>'+paragraph(data['description'][lang])+'</section><!-- /quantum-entry --></main>');path.write_text(text)

# The live reading router must know the chapter before redirecting to static HTML.
for name in ['content.en.json','content.ja.json','content.json']:
    path=ATLAS/name;content=load(path);lang='ja' if '.ja.' in name else 'en'
    content['quantum-chemistry']={'title':data['title'][lang],'html':bodies[lang],'headings':[{'level':2,'id':x['id'],'title':methods[x['id']]['name'][lang]} for x in data['sections']],'locale':lang}
    write(path,content)

# Extend the common reference library and downloadable BibTeX, deduplicating DOI.
path=ATLAS/'references.json';library=[x for x in load(path) if x.get('origin')!='curated-quantum-reading']
identities={x.get('doi','').lower() for x in library if x.get('doi')}
for r in refs.values():
    if r['doi'].lower() not in identities:
        assert r['id'] not in {x['id'] for x in library}
        library.append(r);identities.add(r['doi'].lower())
write(path,library)
path=ATLAS/'assets/references.bib';text=re.sub(r'\n% BEGIN QUANTUM READING\n.*?% END QUANTUM READING\n?','',path.read_text(),flags=re.S)
text+='\n% BEGIN QUANTUM READING\n'
for r in refs.values():text+='@article{'+r['id']+',\n'+''.join('  '+k+' = {'+str(r[k])+'},\n' for k in ['author','title','journal','year','doi'])+'}\n\n'
path.write_text(text+'% END QUANTUM READING\n')

all_equations=load(ROOT/'catalog/atlas-equations.json')['equations']
equation_by_id={x['id']:x for x in all_equations}
equation_examples=equation_evidence(ROOT,all_equations,load_discovery(ROOT))
equations=[x for x in all_equations if x['group']=='quantum']
for path in [ATLAS/'coverage.json',ATLAS/'assets/site-coverage.json']:
    coverage=load(path)
    coverage['items']=[x for x in coverage['items'] if x.get('origin')!='curated-quantum-reading']
    for x in methods.values():coverage['items'].append({'kind':'method','id':x['id'],'label':x['name']['en'],'chapter':'quantum-chemistry','status':'local-example' if x.get('quantum_examples') or x.get('molecular_examples') or x.get('periodic_examples') else 'reading','group':'Electronic structure & quantum chemistry','scope':' '.join(s['en'] for s in [x.get('example_scope',{}),x.get('molecular_scope',{}),x.get('periodic_scope',{})] if s.get('en')) if x.get('quantum_examples') or x.get('molecular_examples') or x.get('periodic_examples') else 'Introductory formulation only; no dedicated solver or numerical validation.','origin':'curated-quantum-reading'})
    for x in equations:coverage['items'].append({'kind':'equation','id':x['id'],'label':x['name']['en'],'chapter':x['chapter'],'status':x['status'],'group':'Electronic structure & quantum chemistry','scope':x['note']['en'],'origin':'curated-quantum-reading'})
    # Align previously imported biology labels with their verified scoped runs.
    # Counts refer to equation/model entries, never independent physical problems.
    for item in coverage['items']:
        if item['kind']=='equation':
            canonical=equation_by_id[item['id']]
            item['status']=canonical['status']
            item['scope']=canonical.get('coverage_scope',canonical['note']['en'])
    coverage['equation_execution_source_sha256']=equation_examples['source_sha256']
    coverage['items']=[x for x in coverage['items'] if x.get('origin')!='curated-model-example']
    for x in load(ROOT/'catalog/atlas-methods.json')['methods']:
        if x.get('model_examples'):
            assert x['status']=='educational-example'
            coverage['items'].append({'kind':'method','id':x['id'],'label':x['name']['en'],'chapter':x['id'],'status':'local-example','group':x['group']['en'],'scope':x['example_scope']['en'],'origin':'curated-model-example'})
    # Supplemental derivative code has its own immutable edition. Promote the
    # existing AD candidate once, without adding it to the original code ZIP.
    coverage['items']=[x for x in coverage['items'] if x.get('origin')!='curated-autodiff-example']
    for x in load(ROOT/'catalog/atlas-methods.json')['methods']:
        if x.get('autodiff_release'):
            assert x['status']=='educational-example'
            coverage['items'].append({'kind':'method','id':x['id'],'label':x['name']['en'],
                'chapter':'automatic-differentiation','status':'local-example',
                'group':x['group']['en'],'scope':x['limitations']['en'],
                'origin':'curated-autodiff-example'})
    coverage['items']=[x for x in coverage['items'] if x.get('origin')!='curated-sensitivity-example']
    for x in load(ROOT/'catalog/atlas-methods.json')['methods']:
        if x.get('sensitivity_release'):
            assert x['status']=='educational-example'
            coverage['items'].append({'kind':'method','id':x['id'],'label':x['name']['en'],
                'chapter':'adjoint','status':'local-example','group':x['group']['en'],
                'scope':x['limitations']['en'],'origin':'curated-sensitivity-example'})
    coverage['items']=[x for x in coverage['items'] if x.get('origin')!='curated-inverse-example']
    for x in load(ROOT/'catalog/atlas-methods.json')['methods']:
        if x.get('inverse_release'):
            assert x['status']=='educational-example'
            coverage['items'].append({'kind':'method','id':x['id'],'label':x['name']['en'],
                'chapter':'bratu-multi-inverse' if x.get('multi_inverse_release') else 'bratu-inverse','status':'local-example','group':x['group']['en'],
                'scope':x['limitations']['en'],'origin':'curated-inverse-example'})
    coverage['items']=[x for x in coverage['items'] if x.get('origin')!='curated-fdtd-example']
    for x in load(ROOT/'catalog/atlas-methods.json')['methods']:
        if x.get('fdtd_release'):
            assert x['status']=='educational-example'
            coverage['items'].append({'kind':'method','id':x['id'],'label':x['name']['en'],
                'chapter':'fdtd','status':'local-example','group':x['group']['en'],
                'scope':x['limitations']['en'],'origin':'curated-fdtd-example'})
    # New fixed-input supplements replace their existing method inventory row;
    # a second validation of a method never creates a second method count.
    depth_methods=[x for x in load(ROOT/'catalog/atlas-methods.json')['methods'] if x.get('depth_release')]
    depth_ids={x['id'] for x in depth_methods}
    coverage['items']=[x for x in coverage['items'] if x.get('origin')!='curated-depth-example' and not (x['kind']=='method' and x['id'] in depth_ids)]
    for x in depth_methods:
        assert x['status']=='educational-example'
        coverage['items'].append({'kind':'method','id':x['id'],'label':x['name']['en'],
            'chapter':'validation-'+x['depth_release']['group'],'status':'local-example',
            'group':x['group']['en'],'scope':x['depth_scope']['en'],'origin':'curated-depth-example'})
    # New splitting readings extend the method inventory, not the solver or
    # independent-problem inventory. Preserve all earlier example assignments.
    splitting_origin='curated-operator-splitting-reading'
    coverage['items']=[x for x in coverage['items'] if x.get('origin')!=splitting_origin]
    for x in load(ROOT/'catalog/atlas-methods.json')['methods']:
        if x.get('origin')==splitting_origin and not x.get('depth_release'):
            assert x['status']=='reading-only' and not x['code_modules'] and not x['test_files']
            coverage['items'].append({'kind':'method','id':x['id'],'label':x['name']['en'],
                'chapter':'operator-splitting','status':'reading','group':x['group']['en'],
                'scope':x['limitations']['en'],'origin':splitting_origin})
    coverage['publications']=[x for x in coverage['publications'] if x.get('origin')!='curated-quantum-reading']
    identities={x['identity'] for x in coverage['publications']}
    for r in refs.values():
        ident='doi:'+r['doi'].lower()
        if ident not in identities:
            coverage['publications'].append({'id':r['id'],'type':'article','identity':ident,'origin':'curated-quantum-reading'});identities.add(ident)
    c=coverage['counts'];pub=Counter(x['type'] for x in coverage['publications'])
    for kind in ['method','equation']:
        rows=[x for x in coverage['items'] if x['kind']==kind]
        c[kind+'s']=len(rows);c['local_'+kind+'s']=sum(x['status']=='local-example' for x in rows);c['reading_'+kind+'s']=sum(x['status']=='reading' for x in rows)
    c.update(references=len(coverage['publications']),journal_articles=pub['article'],conference_papers=pub['inproceedings'],papers=pub['article']+pub['inproceedings'],reading_chapters=len({p.parent for p in (ATLAS/'en/read').glob('*/index.html')}))
    coverage['counted_on']=max(coverage['counted_on'],data['reviewed_on'])
    coverage['public_extension_sha256']={f:sha(ROOT/f) for f in ['catalog/atlas-quantum.json','catalog/atlas-methods.json','catalog/atlas-equations.json','catalog/atlas-method-primary-references.json']}
    write(path,coverage)

# Public roadmap rendering is separate from imported development history.
def roadmap_history_titles(lang):
    titles={
        'current-priority-shock-methods':('過去の重点：衝撃波手法','Earlier priority: shock methods'),
        'next-verification-work':('従来の検証候補','Earlier validation candidates'),
        'suggested-order-for-nasa-cases':('従来のNASA問題の推奨順序','Earlier suggested order for NASA cases'),
        'authorized-next-work':('従来の実装候補と進捗記録','Earlier implementation candidates and progress'),
        'planned-machine-learning-numerics':('長期の改訂候補：機械学習に関連する数値計算','Longer-term candidates: machine-learning numerics'),
        'planned-quantum-chemistry-and-dft':('電子状態：公開済み例と残る課題','Electronic structure: published examples and remaining work'),
    }
    return {key:value[0 if lang=='ja' else 1] for key,value in titles.items()}


def build_public_roadmap(work,lang):
    ja=lang=='ja'
    title='現在の整備計画と公開済みの例' if ja else 'Current development plan and published examples'
    history='これまでの整備・分野別の検証候補' if ja else 'Development history and field-specific validation candidates'
    headings=[{'level':2,'id':'atlas-work-queue','title':title}]
    states={
        'in-progress':('実装中・公開確認待ち','In progress / publication check pending'),
        'planned':('予定','Planned'),
        'conditional-planned':('条件付きの候補','Conditional candidate'),
        'published-verified-example':('検証した限定例を公開済み','Scoped verified example published'),
        'reading-available':('解説公開済み','Reading published'),
        'hydrogenic-helium-verified':('検証した限定例を公開済み','Scoped verified examples published'),
        'deferred-until-2027':('2027年以降','2027 or later'),
        'published':('今回の範囲を公開確認済み','Current scope published and checked'),
    }
    tracks=[('current','まず揃える共通基盤・既存例（P0）','Shared foundation and existing examples first (P0)'),
            ('conditional','検証と進捗を見て追加する候補（P1）','Additions conditional on validation and progress (P1)'),
            ('published','既に利用できる代表例・解説','Representative examples and reading already available'),
            ('later','2027年以降の目標','Goals for 2027 or later')]
    body='<section id="atlas-work-queue"><h2>'+title+'</h2>'+paragraph(work['description'][lang])+paragraph(work['policy'][lang])
    if work.get('milestones'):
        label='整備の目安と確認の節目' if ja else 'Target milestones and review gates'
        headings.append({'level':3,'id':'atlas-queue-milestones','title':label})
        body+='<section><h3 id="atlas-queue-milestones">'+label+'</h3><ol>'
        for x in work['milestones']:body+='<li><strong>'+esc(x['title'][lang])+'</strong>'+paragraph(x['scope'][lang])+'</li>'
        body+='</ol></section>'
    for track,jtitle,etitle in tracks:
        rows=[x for x in work['items'] if x['track']==track]
        if not rows:continue
        ident='atlas-queue-'+track;label=jtitle if ja else etitle
        headings.append({'level':3,'id':ident,'title':label})
        body+='<section><h3 id="'+ident+'">'+esc(label)+'</h3>'
        for x in rows:
            state=states[x['state']][0 if ja else 1]
            body+='<article data-work-id="'+esc(x['id'])+'" data-work-state="'+esc(x['state'])+'"><h4>'+esc(x['title'][lang])+'</h4><p class="resource-status">'+esc(state)+'</p>'+paragraph(x['scope'][lang])
            if x.get('links'):body+='<p>'+' · '.join(link(y['url'].format(lang=lang),y['label'][lang]) for y in x['links'])+'</p>'
            body+='</article>'
        body+='</section>'
    body+='<p>'+link('/catalog/atlas-work-queue.json','現行作業台帳 / JSON' if ja else 'Current work queue / JSON')+'</p></section>'
    body+='<h2 id="atlas-roadmap-history">'+history+'</h2>'+paragraph('以下は過去の拡張記録と分野別の検証候補です。現行の優先順位や、すべてを年内に実装する約束ではありません。既存の節リンクを保持しています。' if ja else 'The sections below retain earlier development records and field-specific validation candidates. They are not the current priority order or a commitment to implement every item this year. Existing section links are preserved.')
    headings.append({'level':2,'id':'atlas-roadmap-history','title':history})
    return body,headings


def adapt_roadmap_history(text,headings,lang,current_headings):
    titles=roadmap_history_titles(lang)
    for ident,title in titles.items():
        def heading(match):
            anchor=re.search(r'<a\b[^>]*class="heading-anchor"[^>]*>.*?</a>',match[2],flags=re.S)
            return match[1]+esc(title)+(anchor[0] if anchor else '')+match[3]
        text=re.sub(r'(<h[23]\b[^>]*\bid="'+re.escape(ident)+r'"[^>]*>)(.*?)(</h[23]>)',heading,text,flags=re.S)
        # Imported static tables of contents must use the same titles as the body.
        def toc_label(match):
            return match[0] if 'class="heading-anchor"' in match[1] else match[1]+esc(title)+match[3]
        text=re.sub(r'(<a\b[^>]*href="#'+re.escape(ident)+r'"[^>]*>)(.*?)(</a>)',toc_label,text,flags=re.S)
    text=text.replace('相対論・新分野より、衝撃波手法の拡充を優先します。','当時は、相対論・新分野より衝撃波手法の拡充を優先しました。')
    text=text.replace('Shock-method expansion takes priority over relativity and new subject areas.','At that stage, shock-method expansion took priority over relativity and new subject areas.')
    text=text.replace('英語原文が更新されています。この日本語訳は旧版に対応します。','上部の現行計画は日英で更新しています。履歴部分の一部の日本語訳は英語の旧版に対応します。')
    ids={x['id'] for x in current_headings}
    def toc(match):
        old=match[2]
        for ident in ids:old=re.sub(r'<a\b[^>]*href="#'+re.escape(ident)+r'"[^>]*>.*?</a>','',old,flags=re.S)
        return match[1]+''.join(link('#'+x['id'],x['title']) for x in current_headings)+old+match[3]
    text=re.sub(r'(<aside\b[^>]*class="chapter-toc"[^>]*>.*?<nav\b[^>]*>)(.*?)(</nav>)',toc,text,flags=re.S)
    updated=None if headings is None else current_headings+[{**h,'title':titles.get(h['id'],h['title'])} for h in headings if h['id'] not in ids]
    return text,updated


# Keep imported prose inventories current without changing any original anchor.
counts=coverage['counts']
for lang in ['ja','en']:
    ja=lang=='ja';extension='<section id="quantum-extension"><h2>'+('電子状態・量子化学の追加項目' if ja else 'Added electronic-structure reading')+'</h2>'+paragraph('水素型原子・Heに限定した実行例を公開し、その他の実装予定と区別しています。' if ja else 'Scoped hydrogenic/He runs are available; other implementations remain planned.')+'<ul>'+''.join('<li>'+link(f'/numerical-methods-atlas/{lang}/read/quantum-chemistry/#{x["id"]}',x['name'][lang])+'</li>' for x in methods.values())+'</ul></section>'
    bib='<section id="quantum-references"><h2>'+('量子化学の追加一次文献' if ja else 'Added quantum-chemistry primary publications')+'</h2><ol>'+''.join('<li>'+reference(r)+'</li>' for r in refs.values())+'</ol></section>'
    roadmap,roadmap_headings=build_public_roadmap(queue,lang)
    for name,block,marker in [('site-coverage',extension,'quantum-inventory'),('references',bib,'quantum-bibliography'),('roadmap',roadmap,'atlas-work-queue')]:
        start='<!-- '+marker+' -->';end='<!-- /'+marker+' -->'
        for path,mode in [(ATLAS/lang/'read'/name/'index.html','static'),(ATLAS/('content.'+lang+'.json'),'content')]+([(ATLAS/'content.json','content')] if lang=='en' else []):
            doc=load(path) if mode=='content' else None
            text=doc[name]['html'] if doc is not None else path.read_text()
            text=re.sub(re.escape(start)+r'.*?'+re.escape(end),'',text,flags=re.S)
            if name=='roadmap':
                heading=roadmap_history_titles(lang)['planned-quantum-chemistry-and-dft']
                current='<h2 id="planned-quantum-chemistry-and-dft">'+heading+'</h2>'+paragraph(f'{len(methods)}項目の導入解説・代表式・一次文献を公開しました。水素型原子・Heには固定入力、コード、独立参照との比較があります。H₂の有限基底RHFを追加しました。周期HeセルのLDAを検証例へ追加。一般の分子DFT・他の周期系は別課題です。' if ja else f'Introductions, representative formulas and primary references are available for {len(methods)} entries. Hydrogenic/He examples supply fixed inputs, code and independent reference comparisons. Scoped finite-basis H₂ RHF is now included; periodic-He LDA validation is now added, while general molecular DFT and other periodic systems remain separate tasks.')
                current+='<p>'+link(f'/numerical-methods-atlas/{lang}/read/quantum-chemistry/','日英の解説・計算例と今後の計画' if ja else 'Bilingual overview, runnable examples and next plans')+'</p>'
                text=re.sub(r'<h2 id="planned-quantum-chemistry-and-dft"[^>]*>.*?(?=<h2|\Z)',lambda m:current,text,flags=re.S)
                text,updated_headings=adapt_roadmap_history(text,doc[name]['headings'] if doc is not None else None,lang,roadmap_headings)
                if doc is not None:doc[name]['headings']=updated_headings
            if name=='site-coverage':
                text=re.sub(r'(counted |集計日)\d{4}-\d\d-\d\d',lambda m:m[1]+coverage['counted_on'],text)
                if ja:
                    text=re.sub(r'方程式・モデル\d+項目・計算法と構成要素\d+項目・学術誌／会議論文\d+件・全参考資料\d+件。',f'方程式・モデル{counts["equations"]}項目・計算法と構成要素{counts["methods"]}項目・学術誌／会議論文{counts["papers"]}件・全参考資料{counts["references"]}件。',text)
                    text=re.sub(r'ローカル実験のある項目は\d+、文献解説のみは\d+で、',f'ローカル実験のある項目は{counts["local_equations"]}、文献解説のみは{counts["reading_equations"]}で、',text)
                    text=re.sub(r'ローカル実験のある項目は\d+、文献解説のみは\d+です',f'ローカル実験のある項目は{counts["local_methods"]}、文献解説のみは{counts["reading_methods"]}です',text)
                    text=re.sub(r'読書章はこの一覧を含め\d+章',f'読書章はこの一覧を含め{counts["reading_chapters"]}章',text)
                    text=re.sub(r'\d+件：学術誌論文',f'{counts["journal_articles"]}件：学術誌論文',text)
                else:
                    text=re.sub(r'\d+ equation/model entries · \d+ methods and building blocks · \d+ journal/conference papers · \d+ total sources[.]',f'{counts["equations"]} equation/model entries · {counts["methods"]} methods and building blocks · {counts["papers"]} journal/conference papers · {counts["references"]} total sources.',text)
                    text=re.sub(r'\d+ entries have scoped local examples; \d+ are reading-only,',f'{counts["local_equations"]} entries have scoped local examples; {counts["reading_equations"]} are reading-only,',text)
                    text=re.sub(r'\d+ entries have scoped local examples; \d+ are reading-only[.]',f'{counts["local_methods"]} entries have scoped local examples; {counts["reading_methods"]} are reading-only.',text)
                    text=re.sub(r'and \d+ reading chapters including this inventory',f'and {counts["reading_chapters"]} reading chapters including this inventory',text)
                    text=re.sub(r'\d+ journal-article records',f'{counts["journal_articles"]} journal-article records',text)
            addition=start+block+end
            if name=='roadmap':text=re.sub(r'(</h1>)',lambda m:m[1]+addition,text,count=1)
            else:text=text.replace('</main>',addition+'</main>') if doc is None else text+addition
            if doc is None:path.write_text(text)
            else:doc[name]['html']=text;write(path,doc)

# Register only real reading pages; examples and extended topics remain plans.
path=ATLAS/'sitemap.xml';xml=ET.parse(path);ns='{http://www.sitemaps.org/schemas/sitemap/0.9}';existing={x.text for x in xml.getroot().findall('.//{*}loc')}
for lang in ['ja','en']:
    url=ORIGIN+f'/numerical-methods-atlas/{lang}/read/quantum-chemistry/'
    if url not in existing:ET.SubElement(ET.SubElement(xml.getroot(),ns+'url'),ns+'loc').text=url
ET.register_namespace('',ns[1:-1]);xml.write(path,encoding='utf-8',xml_declaration=True)
messages=ATLAS/'locales/messages.json';translations=load(messages)
new_copy={
    'planned.quantum.eyebrow':{'ja':'導入解説 / 量子化学・DFT','en':'READING / QUANTUM CHEMISTRY + DFT'},
    'planned.quantum.title':{'ja':'基底関数から電子状態計算へ。','en':'From basis functions to electronic structure.'},
    'planned.quantum.scope':{'ja':f'Schrödinger、HF・DFT、基底・SCF、バンドの対称群、電子相関・励起まで{len(methods)}項目の導入を日英で公開しています。','en':f'Bilingual introductions to {len(methods)} entries cover Schrödinger, HF and DFT, bases, SCF, band symmetry, correlation and excitations.'},
    'planned.quantum.status':{'ja':'原子・H₂ RHF・小さな周期Heと力の限定例を維持します。大規模な基底・k点走査、重い参照再生成、長時間MDは必要性が指定された場合だけ扱います。','en':'Maintain scoped atoms, H₂ RHF, small periodic-He and force examples. Large basis/k-point sweeps, expensive reference regeneration and long MD are considered only on explicit need.'},
    'planned.quantum.link':{'ja':'量子化学・DFTの解説を読む','en':'Read the quantum chemistry and DFT overview'},
    'home-map.future':{'ja':'量子は原子・H₂ RHF・小さな周期Heセルと原子間力の検証例に範囲を限定します。各分野の小規模な参照比較と収束確認を優先します。','en':'Quantum examples stay limited to atoms, H₂ RHF, small periodic He cells and forces. Small reference comparisons and refinement checks take priority across fields.'},
}
old_copy={key:translations[key] for key in new_copy}
translations.update(new_copy);write(messages,translations)
# Also adapt the static shell retained for visitors without client rendering.
page=ATLAS/'index.html';static=page.read_text()
for key,old in old_copy.items():
    for lang,value in old.items():static=static.replace(esc(value),esc(new_copy[key][lang]))
page.write_text(static)
app=ATLAS/'app.js';text=app.read_text()
notice='const plannedQuantumNotice = () => `<aside class="callout page-width planned-extension" id="quantum-plan" aria-labelledby="quantum-plan-title"><p class="eyebrow">${escapeHTML(t("planned.quantum.eyebrow"))}</p><h2 id="quantum-plan-title">${escapeHTML(t("planned.quantum.title"))}</h2><p>${escapeHTML(t("planned.quantum.scope"))}</p><p class="planned-status">${escapeHTML(t("planned.quantum.status"))}</p><a class="text-link" href="#/read/quantum-chemistry">${escapeHTML(t("planned.quantum.link"))}</a></aside>`;'
text,n=re.subn(r'const plannedQuantumNotice = [^\n]+',lambda m:notice,text);assert n==1
for filename in ['references.json','locales/messages.json']:
    text=re.sub("'"+re.escape(filename)+r"(?:[?]v=[a-f0-9]+)?'","'"+filename+'?v='+sha(ATLAS/filename)[:12]+"'",text)
app.write_text(text)
print('Built bilingual quantum reading:',len(methods),'topics,',len(refs),'primary publications; counts:',counts['methods'],counts['equations'],counts['papers'])
