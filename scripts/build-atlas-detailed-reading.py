#!/usr/bin/env python3
"""Build bilingual detailed reading without changing solver status or code editions."""
from pathlib import Path
from html import escape, unescape
import hashlib
import json
import re
import subprocess
import xml.etree.ElementTree as ET

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
        result+='<li id="source-'+ident+'">'+link(target,r['author']+f' ({r["year"]}). '+r['title'])+'. '+escape(r.get('journal') or r.get('booktitle') or r.get('publisher',''))+'<p>'+escape(kind+' · '+label)+' · '+link(review['url'],'確認した資料' if ja else 'Consulted record')+'</p><p>'+escape(review['scope_ja'] if ja else (review.get('scope') or r.get('note') or 'Bibliographic identity checked; full-paper audit not claimed.'))+'</p></li>'
    return result+'</ol>'

for chapter in data['chapters']:
    ident=chapter['id'];assert all(i in methods for i in chapter['methods'])
    assert chapter['references'] and all(i in refs for i in chapter['references'])
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
        toc='<nav aria-label="'+('この章の目次' if ja else 'On this page')+'">'+''.join(link('#'+h['id'],h['title']) for h in headings)+'</nav>'
        navigation='<nav class="resource-nav">'+link(f'/numerical-methods-atlas/{lang}/read/','解説章の目次' if ja else 'Reading contents')+' · '+link('/numerical-methods-atlas/methods/?lang='+lang,'手法一覧' if ja else 'Method map')+' · '+link(SOURCE,'編集用正本 / Source JSON' if ja else 'Editable source / JSON')+' · '+link(url(ident,lang)+'index.md','Markdown')+' · '+link(url(ident,lang)+'index.json','JSON')+'</nav>'
        doc='<!doctype html><html lang="'+lang+'"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+escape(title)+' | Numerical Methods Atlas</title><meta name="description" content="'+escape(title+'：'+('代表式・計算手順・条件・検証案・一次文献' if ja else 'equations, algorithm, assumptions, proposed checks and primary sources'),quote=True)+'"><link rel="canonical" href="https://hrkoyama.github.io'+url(ident,lang)+'">'+''.join('<link rel="alternate" hreflang="'+l+'" href="https://hrkoyama.github.io'+url(ident,l)+'">' for l in ['ja','en'])+'<link rel="stylesheet" href="/numerical-methods-atlas/vendor/katex.min.css"><link rel="stylesheet" href="/numerical-methods-atlas/style.css"><link rel="stylesheet" href="/styles/atlas-resources.css"><style>.detailed-reading{max-width:1000px;margin:auto;padding:1.2rem}.detailed-reading .prose{max-width:78ch}.detailed-reading .math-block{max-width:100%;overflow-x:auto}.detailed-reading .resource-nav,.detailed-reading>nav{display:flex;flex-wrap:wrap;gap:.6rem}.detailed-reading>nav a{padding:.35rem}.reading-sources li{margin-bottom:1rem}.reading-sources p{font-size:.95rem;overflow-wrap:anywhere}h2{scroll-margin-top:1rem}</style></head><body class="profile-page" data-content-language="'+lang+'"><main id="main" class="detailed-reading">'+navigation+toc+'<article class="prose" lang="'+lang+'">'+static+'</article><p>'+link('/using/','引用と利用条件' if ja else 'Citation and reuse')+'</p></main></body></html>\n'
        (directory/'index.html').write_text(doc)
        write(directory/'index.json',{**entry,'url':'https://hrkoyama.github.io'+url(ident,lang),'methods':chapter['methods'],'implementation_status':{i:methods[i]['status'] for i in chapter['methods']},'references':[refs[i] for i in chapter['references']],'source_sha256':source_hash})
        # A simple readable extraction retains LaTeX source and citations.
        markdown='# '+title+'\n\n'
        if 'html' not in chapter:
            markdown+=chapter['intro'][lang]+'\n\n'
            for section in chapter['sections']:
                markdown+='## '+section['title'][lang]+'\n\n'+'\n\n'.join(section['paragraphs'][lang])+'\n\n'
                markdown+=''.join('$$\n'+data['formulas'][f]+'\n$$\n\n' for f in section.get('formulas',[]))
        else:
            plain=chapter['html'][lang]
            plain=re.sub(r'<math-placeholder id="([a-z0-9-]+)"></math-placeholder>',lambda m:'\n$$\n'+data['formulas'][m[1]]+'\n$$\n',plain)
            plain=re.sub(r'<a [^>]*href="([^"]+)"[^>]*>(.*?)</a>',lambda m:'['+re.sub('<[^>]+>','',m[2])+']('+m[1]+')',plain,flags=re.S)
            plain=re.sub(r'</(?:p|h[1-6]|li|ul)>','\n\n',plain)
            markdown+=unescape(re.sub('<[^>]+>','',plain)).strip()+'\n\n'
        markdown+='## '+('公開範囲' if ja else 'Publication scope')+'\n\n'+scope+'\n\n'
        markdown+='## '+('文献' if ja else 'Sources')+'\n\n'+'\n'.join('- '+refs[i]['author']+' ('+str(refs[i]['year'])+'). '+refs[i]['title']+'. '+('https://doi.org/'+refs[i]['doi'] if refs[i].get('doi') else refs[i]['source']) for i in chapter['references'])+'\n'
        (directory/'index.md').write_text(markdown)
    assert anchors['ja']==anchors['en'],ident+': bilingual headings differ'
    translations['chapters'][ident]={'status':'draft','source_url':SOURCE,'source_sha256':source_hash,'checked_on':data['updated_on']}
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
# The imported atlas sitemap is additive; root sitemap is rebuilt later.
path=ATLAS/'sitemap.xml';xml=ET.parse(path);root=xml.getroot();existing={x.text for x in root.findall('.//{*}loc')};ns='{http://www.sitemaps.org/schemas/sitemap/0.9}'
for c in data['chapters']:
    for lang in ['ja','en']:
        target='https://hrkoyama.github.io'+url(c['id'],lang)
        if target not in existing:ET.SubElement(ET.SubElement(root,ns+'url'),ns+'loc').text=target
ET.register_namespace('',ns[1:-1]);xml.write(path,encoding='utf-8',xml_declaration=True)
print('Built',len(data['chapters']),'bilingual detailed chapters;',len(data['formulas']),'formula blocks;',len(refs),'distinct cited sources.')
