#!/usr/bin/env python3
"""Build bilingual detailed reading without changing solver status or code editions."""
from pathlib import Path
from html import escape, unescape
import hashlib
import json
import re
import subprocess
import xml.etree.ElementTree as ET
from atlas_goal_availability import load_supplemental_examples

ROOT=Path(__file__).resolve().parents[1]
ATLAS=ROOT/'numerical-methods-atlas'
SOURCE='/catalog/atlas-detailed-reading.json'
data=json.loads((ROOT/SOURCE.lstrip('/')).read_text())
methods={m['id']:m for m in json.loads((ROOT/'catalog/atlas-methods.json').read_text())['methods']}
refs={r['id']:r for r in data['references']}
assert len(refs)==len(data['references'])
assert len({c['id'] for c in data['chapters']})==len(data['chapters'])
assert all(i in methods for c in data['chapters'] for i in c['methods'])
rendered=json.loads(subprocess.check_output(['node','scripts/render-atlas-math.cjs'],cwd=ROOT,input=json.dumps([{'id':k,'formula':[v]} for k,v in data['formulas'].items()]).encode()))['rendered']
source_hash=hashlib.sha256((ROOT/SOURCE.lstrip('/')).read_bytes()).hexdigest()
documents={lang:json.loads((ATLAS/f'content.{lang}.json').read_text()) for lang in ['ja','en']}
translations=json.loads((ATLAS/'translation-status.json').read_text())

def write(path,obj):path.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
def link(url,label):return '<a href="'+escape(url,quote=True)+'">'+escape(label)+'</a>'
def heading(ident,title):return '<h2 id="'+ident+'">'+escape(title)+'</h2>'
def paragraph(text):return '<p>'+escape(text)+'</p>'
def url(chapter,lang):return f'/numerical-methods-atlas/{lang}/read/{chapter}/'

def reading_navigation(chapter, lang, headings):
    """Keep one parent link visible and disclose the existing auxiliary links."""
    ja=lang=='ja'
    label='この章の目次' if ja else 'On this page'
    breadcrumb='<nav class="reading-breadcrumb" aria-label="'+('現在地' if ja else 'Breadcrumb')+'">'+link(f'/numerical-methods-atlas/{lang}/read/','解説章の目次' if ja else 'Reading contents')+'</nav>'
    resources=' · '.join([link('/numerical-methods-atlas/methods/?lang='+lang,'手法一覧' if ja else 'Method map'),link(SOURCE,'編集用正本 / Source JSON' if ja else 'Editable source / JSON'),link(url(chapter,lang)+'index.md','Markdown'),link(url(chapter,lang)+'index.json','JSON')])
    toc='<nav class="reading-toc" aria-label="'+label+'"><details class="reading-toc-details"><summary>'+label+'</summary><div class="reading-toc-links">'+''.join(link('#'+h['id'],h['title']) for h in headings)+'</div><div class="reading-resource-links">'+resources+'</div></details></nav>'
    return breadcrumb,toc

def reading_layout(static, breadcrumb, toc, lang):
    """Move the existing title and first lead before auxiliary navigation.

    This template owns a known H1/paragraph prefix. Keep its original HTML,
    including authored comments, without changing the downloadable body.
    """
    opening=re.match(r'\s*<h1\b[^>]*>.*?</h1>(?:\s|<!--.*?-->)*<p\b[^>]*>.*?</p>',static,re.S)
    if not opening:
        raise ValueError('Detailed reading needs an existing H1 followed by its lead')
    end=opening.end()
    # The FDTD lead has an authored, paired intro marker around its quick links.
    # Keep such an existing block together rather than spanning new UI markup.
    for marker in re.findall(r'<!--\s*([a-z][a-z0-9-]+)\s*-->',static[:end]):
        closing=re.search(r'<!--\s*/'+re.escape(marker)+r'\s*-->',static[end:])
        if closing:
            end+=closing.end()
    return (breadcrumb+'<div class="reading-opening prose" data-chapter-opening lang="'+lang+'">'+
            static[:end]+'</div><!-- chapter-resource-position -->'+toc+
            '<article class="prose" lang="'+lang+'">'+static[end:]+'</article>')

def section_links(section,lang):
    """Optional current-reading links; keep labels bilingual and routes local."""
    rows=section.get('links',[])
    assert isinstance(rows,list)
    targets=[]
    for row in rows:
        assert isinstance(row,dict) and set(row)=={'url','label'}
        assert isinstance(row['url'],str) and re.fullmatch(r'/numerical-methods-atlas/validation/[a-z0-9]+(?:-[a-z0-9]+)*/',row['url'])
        assert isinstance(row['label'],dict) and set(row['label'])=={'ja','en'}
        assert all(isinstance(v,str) and v.strip() for v in row['label'].values())
        assert row['url'] not in [target.split('?')[0] for target,label in targets]
        targets.append((row['url']+'?lang='+lang,row['label'][lang]))
    return targets

def section_figures(section,lang):
    """Only immutable, hash-bound PNGs already shipped in validated editions."""
    figures=section.get('figures',[])
    assert isinstance(figures,list)
    for row in figures:
        source=row['source']
        assert re.fullmatch(r'/code/validated-examples/\d{4}-\d{2}-\d{2}(?:-r\d+)?/[a-z0-9-]+/results/[a-z0-9-]+[.]png',source)
        path=ROOT/source.lstrip('/')
        assert path.is_file() and not path.is_symlink() and path.resolve()==path
        payload=path.read_bytes()
        assert payload[:8]==b'\x89PNG\r\n\x1a\n' and payload[12:16]==b'IHDR'
        assert hashlib.sha256(payload).hexdigest()==row['sha256']
        assert tuple(int.from_bytes(payload[i:i+4],'big')for i in (16,20))==(row['width'],row['height'])
        assert all(isinstance(row['caption'][key],str) and row['caption'][key].strip()for key in ['ja','en'])
    return figures

def markdown_table(match):
    """Retain row/column boundaries in opted-in HTML reading chapters."""
    table=match[0]
    clean=lambda text:unescape(re.sub('<[^>]+>','',text)).strip().replace('|',r'\|')
    caption=re.search(r'<caption>(.*?)</caption>',table,re.S)
    rows=[[clean(cell) for cell in re.findall(r'<t[hd]\b[^>]*>(.*?)</t[hd]>',row,re.S)]
          for row in re.findall(r'<tr\b[^>]*>(.*?)</tr>',table,re.S)]
    assert rows and all(len(row)==len(rows[0]) for row in rows)
    lines=['| '+' | '.join(row)+' |' for row in rows]
    lines.insert(1,'| '+' | '.join(['---']*len(rows[0]))+' |')
    return '\n\n'+(clean(caption[1])+'\n\n' if caption else '')+'\n'.join(lines)+'\n\n'
def scoped_supplement_html(cases,lang):
    """Keep historical editions, target runs and diagnostic controls distinct."""
    if not cases:return ''
    ja=lang=='ja'
    body=heading('scoped-examples','固定入力で確かめる：別々の配布版' if ja else 'Check fixed inputs: separate scoped releases')
    body+=paragraph('各例の入力・観測量・診断の定義と適用範囲を確認します。検査の合格が示す内容は受入条件によって異なり、数学的な一般保証とは区別します。旧版の入力・測定・公差は保持します。' if ja else 'Check each example’s inputs, observables, diagnostic definitions and scope. What a passing check establishes depends on its acceptance criteria and differs from a general mathematical guarantee. Historical inputs, measurements and criteria are preserved.')
    for case in cases:
        role=('診断対照：物理問題数へ非加算' if ja else 'Diagnostic control: no additional physical problem') if case['problem_id'] is None else ('固定した標的の計算例' if ja else 'Computation for a fixed target')
        body+='<article class="resource-summary" id="supplement-'+case['id']+'"><h3>'+escape(case['title'][lang])+'</h3>'+paragraph(role)+paragraph(case['summary'][lang])+paragraph(case['limits'][lang])
        entries=[link(case['url']+'?lang='+lang,'入力・結果・受入条件' if ja else 'Input, results and acceptance'),link(case['reading'][lang],'手法・式・一次文献' if ja else 'Method, equations and sources')]
        entries+=[link(u,('コード：' if ja else 'Code: ')+u.rsplit('/',1)[-1]) for u in case['code_urls']]
        entries+=[link(u,('テスト：' if ja else 'Tests: ')+u.rsplit('/',1)[-1]) for u in case['test_urls']]
        entries+=[link(case['download'],'配布ZIP' if ja else 'Release ZIP'),link(case['results'],'保存結果' if ja else 'Saved results'),link(case['verification'],'独立展開からの追試記録' if ja else 'Independent-extraction rerun receipt')]
        body+='<p>'+' · '.join(entries)+'</p></article>'
    return body

def scoped_supplement_markdown(cases,lang):
    if not cases:return ''
    ja=lang=='ja'
    body='## '+('固定入力の実行例と診断対照' if ja else 'Fixed-input examples and diagnostic controls')+'\n\n'
    body+=('受入条件が示す検証範囲と数学的な一般保証を区別します。旧版の入力・測定・公差は保持します。' if ja else 'Distinguish the scope established by acceptance checks from a general mathematical guarantee; preserve historical inputs, measurements and criteria.')+'\n\n'
    for case in cases:
        role=('診断対照・物理問題数へ非加算' if ja else 'Diagnostic control; no physical-problem increment') if case['problem_id'] is None else ('固定標的の計算例' if ja else 'Fixed-target computation')
        body+='### '+case['title'][lang]+'\n\n'+role+'\n\n'+case['summary'][lang]+'\n\n'+case['limits'][lang]+'\n\n'
        entries=[(case['url']+'?lang='+lang,'入力・結果・受入条件' if ja else 'Input, results and acceptance'),(case['reading'][lang],'手法・一次文献' if ja else 'Method and sources')]
        entries+=[(u,('コード ' if ja else 'Code ')+u.rsplit('/',1)[-1]) for u in case['code_urls']]
        entries+=[(u,('テスト ' if ja else 'Tests ')+u.rsplit('/',1)[-1]) for u in case['test_urls']]
        entries+=[(case['download'],'ZIP'),(case['results'],'結果' if ja else 'Results'),(case['verification'],'追試記録' if ja else 'Rerun receipt')]
        body+=' · '.join('['+label+']('+target+')' for target,label in entries)+'\n\n'
    return body

def bibliography(chapter,lang):
    ja=lang=='ja'
    result=heading('sources','一次文献・関連資料と確認範囲' if ja else 'Primary publications, supporting sources and review scope')
    result+=paragraph('原著、後続の変種、著者による著書、概説、公式資料を区別して参照します。DOI・書誌の確認と原文の該当箇所の閲覧を区別し、論文全体の監査や数値再現を行ったという意味ではありません。確認範囲の注記は引用ごとに示します。' if ja else 'Distinguish original research, later variants, author monographs, pedagogical articles and official references. Bibliographic verification differs from consulting selected passages; neither implies a full-paper audit or numerical reproduction. Access-depth notes accompany each source.')
    result+='<ol class="reading-sources">'
    for ident in chapter['references']:
        r=refs[ident];review=r['source_review'];level=review['level']
        label={'metadata':('書誌確認','Bibliography checked'),'abstract-and-metadata':('抄録・書誌確認','Abstract and bibliography checked'),'full-text':('原文の該当箇所を参照','Selected source passages consulted')}[level][0 if ja else 1]
        target='https://doi.org/'+r['doi'] if r.get('doi') else r['source']
        kind={'book':('著者による著書・関連資料','Author monograph / supporting reference'),'misc':('公式の参照資料','Official reference documentation')}.get(r.get('type'),('研究論文・提案または関連する定式化','Research publication: proposal or related formulation'))[0 if ja else 1]
        if ident=='higham2001':kind='数値法の教育的解説（原提案とは別）' if ja else 'Pedagogical account, distinct from the original proposal'
        if r.get('source_role')=='research-preprint':kind='研究プレプリント（査読論文版とは区別）' if ja else 'Research preprint, distinct from the journal edition'
        result+='<li id="source-'+ident+'">'+link(target,r['author']+f' ({r["year"]}). '+r['title'])+'. '+escape(r.get('journal') or r.get('booktitle') or r.get('publisher',''))+'<p>'+escape(kind+' · '+label)+' · '+link(review['url'],'確認した資料' if ja else 'Consulted record')+'</p><p>'+escape(review['scope_ja'] if ja else (review.get('scope') or r.get('note') or 'Bibliographic identity checked; full-paper audit not claimed.'))+'</p></li>'
    return result+'</ol>'

for chapter in data['chapters']:
    ident=chapter['id'];assert all(i in methods for i in chapter['methods'])
    assert chapter['references'] and all(i in refs for i in chapter['references'])
    scoped=load_supplemental_examples(ROOT,chapter.get('scoped_supplements',[]))
    scoped_fields={}
    if scoped:
        bindings=json.loads((ROOT/'catalog/atlas-depth-expansion.json').read_text())['case_problem_ids']
        for case in scoped:case['problem_id']=bindings[case['id']]
        scoped_fields={'scoped_supplements':[{key:case[key] for key in ['id','title','group','problem_id','summary','limits','reading','url','code_urls','test_urls','download','results','verification']} for case in scoped],
                       'supplemental_source_sha256':{'catalog/atlas-depth-expansion.json':hashlib.sha256((ROOT/'catalog/atlas-depth-expansion.json').read_bytes()).hexdigest(),
                           **{path:digest for case in scoped for path,digest in case['source_sha256'].items()}}}
    anchors={}
    for lang in ['ja','en']:
        ja=lang=='ja';title=chapter['title'][lang];assert title.strip()
        if 'html' in chapter:body=chapter['html'][lang]
        else:
            assert chapter['intro'][lang].strip()
            body='<h1>'+escape(title)+'</h1>'+paragraph(chapter['intro'][lang])
            for section in chapter['sections']:
                body+=heading(section['id'],section['title'][lang])
                assert section['paragraphs'][lang] and all(p.strip() for p in section['paragraphs'][lang])
                for p in section['paragraphs'][lang]:body+=paragraph(p)
                body+=''.join('<math-placeholder id="'+f+'"></math-placeholder>' for f in section.get('formulas',[]))
                if section_links(section,lang):body+='<p>'+' · '.join(link(target,label) for target,label in section_links(section,lang))+'</p>'
                for figure in section_figures(section,lang):
                    caption=escape(figure['caption'][lang])
                    body+='<figure class="reading-saved-figure"><a href="'+escape(figure['source'],quote=True)+'"><img src="'+escape(figure['source'],quote=True)+'" alt="'+caption+'" width="'+str(figure['width'])+'" height="'+str(figure['height'])+'" style="max-width:100%;height:auto" loading="lazy" decoding="async"></a><figcaption>'+caption+'</figcaption></figure>'
        body+=scoped_supplement_html(scoped,lang)
        body+=heading('publication-scope','公開範囲と関連項目' if ja else 'Publication scope and related entries')
        if all(methods[i]['status']=='planned' for i in chapter['methods']):
            scope='解説・代表式・文献を公開しています。専用コードと数値検証結果は実装予定です。上記の検証案は未実施で、他の手法のコードや計算結果をこの手法の検証として流用しません。' if ja else 'Reading, representative equations and sources are published. Dedicated code and numerical verification remain planned. The suggested checks above are not measured results, and code/results of other methods are not presented as validation of this method.'
        else:scope='既存の教育用コードと版を固定した検証記録への案内です。今回の本文・翻訳の追加でコードや過去の測定結果を変更せず、原論文全体の再現を主張しません。' if ja else 'Links lead to existing educational code and dated verification records. This reading/translation update changes no scientific code or historical measurements and does not claim reproduction of an entire paper.'
        scope=chapter.get('publication_scope',{}).get(lang,scope)
        body+=paragraph(scope)+'<ul>'+''.join('<li>'+link('/numerical-methods-atlas/methods/'+i+'/?lang='+lang,methods[i]['name'][lang])+'</li>' for i in chapter['methods']+chapter.get('related_methods',[]))+'</ul>'
        body+=bibliography(chapter,lang)
        body=re.sub(r'<math-placeholder id="([a-z0-9-]+)"></math-placeholder>',lambda m:'<div class="math-block">'+rendered[m[1]][0]+'</div>',body)
        assert 'math-placeholder' not in body
        headings=[{'level':2,'id':key,'title':unescape(re.sub('<[^>]*>','',text))} for key,text in re.findall(r'<h2 id="([a-z0-9-]+)">(.*?)</h2>',body,re.S)]
        # Strip imported heading permalinks from TOC labels only.
        for h in headings:h['title']=h['title'].removesuffix('#').strip()
        anchors[lang]=[h['id'] for h in headings];assert len(anchors[lang])==len(set(anchors[lang]))
        entry={'title':title,'html':body,'headings':headings,'locale':lang,'source_url':SOURCE,'updated_on':data['updated_on']}
        if ja:entry['translation_status']='draft'
        documents[lang][ident]=entry
        directory=ROOT/url(ident,lang).lstrip('/');directory.mkdir(parents=True,exist_ok=True)
        static=body.replace('href="#/',f'href="/numerical-methods-atlas/?lang={lang}#/')
        static=re.sub(r'(src|href)="assets/',r'\1="/numerical-methods-atlas/assets/',static)
        navigation,toc=reading_navigation(ident,lang,headings)
        doc='<!doctype html><html lang="'+lang+'"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+escape(title)+' | Numerical Methods Atlas</title><meta name="description" content="'+escape(title+'：'+('代表式・計算手順・条件・検証案・一次文献' if ja else 'equations, algorithm, assumptions, proposed checks and primary sources'),quote=True)+'"><link rel="canonical" href="https://hrkoyama.github.io'+url(ident,lang)+'">'+''.join('<link rel="alternate" hreflang="'+l+'" href="https://hrkoyama.github.io'+url(ident,l)+'">' for l in ['ja','en'])+'<link rel="stylesheet" href="/numerical-methods-atlas/vendor/katex.min.css"><link rel="stylesheet" href="/numerical-methods-atlas/style.css"><link rel="stylesheet" href="/styles/atlas-resources.css"><style>.detailed-reading{max-width:1000px;margin:auto;padding:1.2rem}.detailed-reading .prose{max-width:78ch}.detailed-reading .math-block{max-width:100%;overflow-x:auto}.detailed-reading .resource-nav,.detailed-reading>nav{display:flex;flex-wrap:wrap;gap:.6rem}.detailed-reading>nav a{padding:.35rem}.reading-sources li{margin-bottom:1rem}.reading-sources p{font-size:.95rem;overflow-wrap:anywhere}h2{scroll-margin-top:1rem}</style></head><body class="profile-page" data-content-language="'+lang+'"><main id="main" class="detailed-reading">'+reading_layout(static,navigation,toc,lang)+'<p>'+link('/using/','引用と利用条件' if ja else 'Citation and reuse')+'</p></main></body></html>\n'
        (directory/'index.html').write_text(doc)
        write(directory/'index.json',{**entry,'url':'https://hrkoyama.github.io'+url(ident,lang),'methods':chapter['methods'],'implementation_status':{i:methods[i]['status'] for i in chapter['methods']},'references':[refs[i] for i in chapter['references']],'source_sha256':source_hash,**scoped_fields})
        # A simple readable extraction retains LaTeX source and citations.
        markdown='# '+title+'\n\n'
        if 'html' not in chapter:
            markdown+=chapter['intro'][lang]+'\n\n'
            for section in chapter['sections']:
                markdown+='## '+section['title'][lang]+'\n\n'+'\n\n'.join(section['paragraphs'][lang])+'\n\n'
                markdown+=''.join('$$\n'+data['formulas'][f]+'\n$$\n\n' for f in section.get('formulas',[]))
                if section_links(section,lang):markdown+=' · '.join('['+label+']('+target+')' for target,label in section_links(section,lang))+'\n\n'
                for figure in section_figures(section,lang):markdown+='!['+figure['caption'][lang]+']('+figure['source']+')\n\n'
        else:
            plain=chapter['html'][lang]
            if chapter.get('tables_in_markdown'):
                plain=re.sub(r'<table\b[^>]*>.*?</table>',markdown_table,plain,flags=re.S)
                plain=re.sub(r'<pre><code>(.*?)</code></pre>',lambda m:'\n\n```text\n'+unescape(m[1])+'\n```\n\n',plain,flags=re.S)
            plain=re.sub(r'<math-placeholder id="([a-z0-9-]+)"></math-placeholder>',lambda m:'\n$$\n'+data['formulas'][m[1]]+'\n$$\n',plain)
            plain=re.sub(r'<a [^>]*href="([^"]+)"[^>]*>(.*?)</a>',lambda m:'['+re.sub('<[^>]+>','',m[2])+']('+m[1]+')',plain,flags=re.S)
            plain=re.sub(r'</(?:p|h[1-6]|li|ul)>','\n\n',plain)
            markdown+=unescape(re.sub('<[^>]+>','',plain)).strip()+'\n\n'
        markdown+=scoped_supplement_markdown(scoped,lang)
        markdown+='## '+('公開範囲' if ja else 'Publication scope')+'\n\n'+scope+'\n\n'
        markdown+='## '+('文献' if ja else 'Sources')+'\n\n'+'\n'.join('- '+refs[i]['author']+' ('+str(refs[i]['year'])+'). '+refs[i]['title']+'. '+('https://doi.org/'+refs[i]['doi'] if refs[i].get('doi') else refs[i]['source']) for i in chapter['references'])+'\n'
        (directory/'index.md').write_text(markdown)
    assert anchors['ja']==anchors['en'],ident+': bilingual headings differ'
    translations['chapters'][ident]={'status':'draft','source_url':SOURCE,'source_sha256':source_hash,'checked_on':data['updated_on']}
# Follow-on reading belongs in both the static chapters and the SPA, once only.
for chapter in data['chapters']:
    for target in chapter.get('linked_from',[]):
        marker='<!-- detailed-followup-'+chapter['id']+' -->'
        end='<!-- /detailed-followup-'+chapter['id']+' -->'
        for lang in ['ja','en']:
            note=marker+paragraph(chapter['followup_note'][lang])+'<p>'+link(url(chapter['id'],lang),chapter['title'][lang])+'</p>'+end
            content=documents[lang][target]
            content['html']=re.sub(re.escape(marker)+'.*?'+re.escape(end),'',content['html'],flags=re.S)+note
            path=ATLAS/lang/'read'/target/'index.html'
            text=re.sub(re.escape(marker)+'.*?'+re.escape(end),'',path.read_text(),flags=re.S)
            assert '</article>' in text,target
            path.write_text(text.replace('</article>',note+'</article>',1))
# Add chapter routes to the actual reading contents and atlas search, idempotently.
for lang in ['ja','en']:
    path=ATLAS/lang/'read/index.html';text=path.read_text()
    text=re.sub(r'<!-- detailed-reading -->.*?<!-- /detailed-reading -->','',text,flags=re.S)
    block='<!-- detailed-reading --><section class="page-width"><h2>'+('追加の詳細解説・基底関数・回転Riemann法' if lang=='ja' else 'Detailed methods, basis functions and rotated Riemann solvers')+'</h2><ul>'+''.join('<li>'+link(url(c['id'],lang),c['title'][lang])+'</li>' for c in data['chapters'])+'</ul></section><!-- /detailed-reading -->'
    path.write_text(text.replace('</main>',block+'</main>'))
for lang,content in documents.items():
    write(ATLAS/f'content.{lang}.json',content)
    if lang=='en':write(ATLAS/'content.json',content)
translations.update(total=len(documents['en']),translated=sum(k in documents['ja'] for k in documents['en']),reviewed=sum(x['status']=='reviewed' for x in translations['chapters'].values()))
write(ATLAS/'translation-status.json',translations)
path=ATLAS/'home-search-index.json';index=json.loads(path.read_text());index['entries']=[x for x in index['entries'] if x.get('origin')!='detailed-reading']
for chapter in data['chapters']:
    index['entries'].append({'id':'reading-'+chapter['id'],'title':chapter['title'],'headings':{l:documents[l][chapter['id']]['headings'] for l in ['ja','en']},'keywords':list(chapter['title'].values())+chapter.get('keywords',[])+[a for i in chapter['methods'] for a in methods[i].get('aliases',[])],'routes':{l:url(chapter['id'],l) for l in ['ja','en']},'origin':'detailed-reading','kind':'chapter'})
write(path,index)
# Preserve the old chapter addresses and link the clarified historical attribution.
for lang in ['ja','en']:
    marker='<!-- rotated-source-note -->';end='<!-- /rotated-source-note -->'
    note=marker+'<p>'+link(url('rotated-hybrid',lang),'回転Riemann法の詳説：Ren（2003）、Roe・西川ら（2005）、西川・北村（2008）と公開実験の違い' if lang=='ja' else 'Rotated Riemann sources: Ren (2003), Roe–Nishikawa et al. (2005), Nishikawa–Kitamura (2008) and the atlas experiment')+'</p>'+end
    content=documents[lang]
    for ident in ['shock-expansion','carbuncle','history','advanced','references']:
        text=content[ident]['html'];text=text.replace('The 2D rotated solver and carbuncle tests are future work.','The atlas links an existing educational directional HLLE/Roe experiment; it is not the optimized Rotated-RHLL formula. Consult the dated verification record for tested scope.');text=re.sub(re.escape(marker)+'.*?'+re.escape(end),'',text,flags=re.S);content[ident]['html']=text+note
        path=ATLAS/lang/'read'/ident/'index.html';text=path.read_text();text=text.replace('The 2D rotated solver and carbuncle tests are future work.','The atlas links an existing educational directional HLLE/Roe experiment; it is not the optimized Rotated-RHLL formula. Consult the dated verification record for tested scope.');text=re.sub(re.escape(marker)+'.*?'+re.escape(end),'',text,flags=re.S);path.write_text(text.replace('</article>',note+'</article>',1))
    write(ATLAS/f'content.{lang}.json',content)
    if lang=='en':write(ATLAS/'content.json',content)
# Add targeted follow-on links without changing the original advanced chapter anchors.
for lang in ['ja','en']:
    marker='<!-- preconditioning-and-steady-rk -->';end='<!-- /preconditioning-and-steady-rk -->'
    note=marker+'<p>'+link(url('low-mach-preconditioning',lang),'前処理行列・音速点・エントロピー修正' if lang=='ja' else 'Preconditioning matrices, sonic points and entropy fixes')+' · '+link(url('steady-runge-kutta',lang),'定常解のためのダンピングRunge–Kutta反復' if lang=='ja' else 'Damping Runge–Kutta iterations for steady solutions')+'</p>'+end
    path=ATLAS/lang/'read/advanced/index.html';text=re.sub(re.escape(marker)+'.*?'+re.escape(end),'',path.read_text(),flags=re.S);path.write_text(text.replace('</article>',note+'</article>',1))
    content=documents[lang];text=re.sub(re.escape(marker)+'.*?'+re.escape(end),'',content['advanced']['html'],flags=re.S);content['advanced']['html']=text+note;write(ATLAS/f'content.{lang}.json',content)
    if lang=='en':write(ATLAS/'content.json',content)
# Keep the historical baseline chapter distinct from its newer measured follow-up.
for lang in ['ja','en']:
    marker='<!-- double-mach-validation-followup -->';end='<!-- /double-mach-validation-followup -->'
    message=('この章は以前のHLL基準計算の記録です。追加の軽量検証では、同じ初期条件・境界条件の3格子を、別実装による保存済み有限格子参照と比較します。参照の格子差と壁近傍の未解像性も示しています。' if lang=='ja' else 'This chapter records the earlier HLL baseline. A newer lightweight verification compares three grids at the same initial and boundary conditions with a stored finite-grid reference from a separate implementation, including reference-grid sensitivity and unresolved near-wall structure.')
    note=marker+'<aside class="callout" id="double-mach-validation-followup"><p>'+escape(message)+'</p><p>'+link('/numerical-methods-atlas/validation/double-mach-reflection/?lang='+lang,'追加の実行・検証へ' if lang=='ja' else 'Open the additional execution and verification')+'</p></aside>'+end
    path=ATLAS/lang/'read/double-mach/index.html';text=re.sub(re.escape(marker)+'.*?'+re.escape(end),'',path.read_text(),flags=re.S)
    path.write_text(re.sub(r'<article\b[^>]*>',lambda m:m[0]+note,text,count=1))
    content=documents[lang];text=re.sub(re.escape(marker)+'.*?'+re.escape(end),'',content['double-mach']['html'],flags=re.S);content['double-mach']['html']=note+text
    write(ATLAS/f'content.{lang}.json',content)
    if lang=='en':write(ATLAS/'content.json',content)
# Keep the existing wedge/step overview and point to the measured step follow-up.
for lang in ['ja','en']:
    marker='<!-- forward-step-validation-followup -->';end='<!-- /forward-step-validation-followup -->'
    message=('この章は楔と前向きステップの従来の計算例をまとめたものです。前向きステップには、段差面を含む境界の保存収支・正値性・格子依存性を調べる軽量な2次元検証を追加しています。段差角の処理と、未解像の細いすべり線・渦の限界も専用ページで確認できます。' if lang=='ja' else 'This chapter collects the earlier wedge and forward-step examples. A newer lightweight 2D forward-step verification checks conservation budgets including the step faces, admissibility and grid dependence. Its dedicated page also records the corner treatment and unresolved fine slip lines and vortices.')
    note=marker+'<aside class="callout" id="forward-step-validation-followup"><p>'+escape(message)+'</p><p>'+link('/numerical-methods-atlas/validation/forward-step-m3/?lang='+lang,'前向きステップの追加検証へ' if lang=='ja' else 'Open the additional forward-step verification')+'</p></aside>'+end
    path=ATLAS/lang/'read/nasa-2d/index.html';text=re.sub(re.escape(marker)+'.*?'+re.escape(end),'',path.read_text(),flags=re.S)
    path.write_text(re.sub(r'<article\b[^>]*>',lambda m:m[0]+note,text,count=1))
    content=documents[lang];text=re.sub(re.escape(marker)+'.*?'+re.escape(end),'',content['nasa-2d']['html'],flags=re.S);content['nasa-2d']['html']=note+text
    write(ATLAS/f'content.{lang}.json',content)
    if lang=='en':write(ATLAS/'content.json',content)
# Retain the historical KEEP case and distinguish spatial flux preconditioning
# from the pseudo-time and dual-time algorithms explained in the older chapter.
for lang in ['ja','en']:
    followups = [
        ('low-mach-preconditioning', 'low-mach-validation-followup',
         '数値散逸行列の前処理を扱う専用の軽量実行例を追加しました。背景Mach数.1/.01、3格子の移動等エントロピー渦を、元の物理時間と音響CFLで計算します。擬似時間・二重時間積分の定常加速、一般の非線形安定性や正値性は、この例の確認範囲に含みません。' if lang=='ja' else
         'A dedicated lightweight example implements numerical-dissipation matrix preconditioning. Moving isentropic vortices at background Mach numbers .1 and .01 are compared on three grids with unchanged physical time and an acoustic CFL. Pseudo-time or dual-time steady acceleration and general nonlinear stability or positivity guarantees remain outside its checked scope.'),

    ]
    for ident, anchor, message in followups:
        marker='<!-- '+anchor+' -->';end='<!-- /'+anchor+' -->'
        note=marker+'<aside class="callout" id="'+anchor+'"><p>'+escape(message)+'</p><p>'+link('/numerical-methods-atlas/validation/low-mach-vortex/?lang='+lang,'低Mach渦の追加検証へ' if lang=='ja' else 'Open the additional low-Mach vortex verification')+'</p></aside>'+end
        path=ATLAS/lang/'read'/ident/'index.html';text=re.sub(re.escape(marker)+'.*?'+re.escape(end),'',path.read_text(),flags=re.S)
        path.write_text(re.sub(r'<article\b[^>]*>',lambda m:m[0]+note,text,count=1))
        content=documents[lang];text=re.sub(re.escape(marker)+'.*?'+re.escape(end),'',content[ident]['html'],flags=re.S);content[ident]['html']=note+text
    write(ATLAS/f'content.{lang}.json',documents[lang])
    if lang=='en':write(ATLAS/'content.json',documents[lang])
# Keep the original standalone-limiter exposition and point to the fully
# discrete, separately scoped finite-volume update without rewriting history.
for lang in ['ja','en']:
    marker='<!-- euler-stage-positivity-followup -->';end='<!-- /euler-stage-positivity-followup -->'
    message=('従来の配布版は平均を保つスケーリングの部品検査です。追加版では同じ操作を1次元Eulerの保存量MUSCL・Lax–Friedrichs流束・SSPRK(3,3)の各段に接続し、強い二重膨張波の平均・面状態・保存収支を確認します。十分CFLと波速条件を明記し、DG・WENO・MHD全体の正値性保証とは区別します。' if lang=='ja' else 'The original release checks mean-preserving scaling as a standalone helper. An additional release connects the operation to every stage of a one-dimensional conservative-MUSCL, Lax–Friedrichs, SSPRK(3,3) Euler update and checks means, faces and conservation in a strong double rarefaction. Its sufficient CFL and wave-speed conditions remain distinct from general DG, WENO or MHD positivity guarantees.')
    note=marker+'<aside class="callout" id="euler-stage-positivity-followup"><p>'+escape(message)+'</p><p>'+link('/numerical-methods-atlas/validation/euler-double-rarefaction-positivity/?lang='+lang,'段階ごとのEuler正値性を試す' if lang=='ja' else 'Run the Euler stage-positivity example')+'</p></aside>'+end
    old_scope=('この補助関数は<strong>既存のEuler MUSCL、差分WENO、CT／GLM、KEEPの時間更新へ接続していません</strong>。既存の限界はそのままです。今後は各段階の許容性・保存性、真空近傍の二重膨張波、強い爆風を確認してから、時間全体の正値性を主張すべきです。多次元・非理想状態方程式にも追加解析が必要です。' if lang=='ja' else
        'This helper is <strong>not wired into the existing Euler MUSCL, finite-difference\nWENO, CT/GLM, or KEEP time updates</strong>. Those solvers retain their documented\nlimitations. A future complete implementation should add stage-by-stage\nadmissibility and conservation checks, near-vacuum double rarefaction, and\nstrong blast-wave tests before claiming positivity preservation over time.\nMultidimensional and non-ideal-EOS extensions need additional analysis.')
    new_scope=('従来のNumart配布版では、この補助関数は<strong>既存のEuler MUSCL、差分WENO、CT／GLM、KEEPの時間更新へ接続されていません</strong>。その配布版と既存ソルバーの限界は保持します。別配布の追加例で1次元Euler MUSCLの段階更新を確認しますが、差分WENO・CT／GLM・KEEP・強い爆風・多次元・非理想状態方程式は今回の確認範囲に含みません。' if lang=='ja' else
        'In the original Numart release, this helper is <strong>not wired into the existing Euler MUSCL, finite-difference WENO, CT/GLM, or KEEP time updates</strong>. That immutable release and the existing solvers retain their documented limitations. A separately distributed example now checks one-dimensional Euler MUSCL stage updates. Finite-difference WENO, CT/GLM, KEEP, strong blasts, multidimensional flow and non-ideal equations of state remain outside this verification.')
    path=ATLAS/lang/'read/advanced-limiters/index.html';text=re.sub(re.escape(marker)+'.*?'+re.escape(end),'',path.read_text(),flags=re.S).replace(old_scope,new_scope)
    path.write_text(re.sub(r'<article\b[^>]*>',lambda m:m[0]+note,text,count=1))
    content=documents[lang];text=re.sub(re.escape(marker)+'.*?'+re.escape(end),'',content['advanced-limiters']['html'],flags=re.S).replace(old_scope,new_scope);content['advanced-limiters']['html']=note+text
    write(ATLAS/f'content.{lang}.json',content)
    if lang=='en':write(ATLAS/'content.json',content)
# The imported atlas sitemap is additive; root sitemap is rebuilt later.
path=ATLAS/'sitemap.xml';xml=ET.parse(path);root=xml.getroot();existing={x.text for x in root.findall('.//{*}loc')};ns='{http://www.sitemaps.org/schemas/sitemap/0.9}'
for c in data['chapters']:
    for lang in ['ja','en']:
        target='https://hrkoyama.github.io'+url(c['id'],lang)
        if target not in existing:ET.SubElement(ET.SubElement(root,ns+'url'),ns+'loc').text=target
ET.register_namespace('',ns[1:-1]);xml.write(path,encoding='utf-8',xml_declaration=True)
print('Built',len(data['chapters']),'bilingual detailed chapters;',len(data['formulas']),'formula blocks;',len(refs),'distinct cited sources.')
