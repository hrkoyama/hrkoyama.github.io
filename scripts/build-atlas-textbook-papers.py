#!/usr/bin/env python3
"""Add cited related papers to the bookshelf without classifying them as books."""
from html import escape
import json
from pathlib import Path
import re
ROOT=Path(__file__).resolve().parents[1]
MARKER=r'<!-- textbook-related-papers -->.*?<!-- /textbook-related-papers -->'
def build(root=ROOT):
    atlas=root/'numerical-methods-atlas'
    catalog=json.loads((root/'catalog/atlas-textbook-related-papers.json').read_text())
    references={row['id']:row for row in json.loads((atlas/'references.json').read_text())}
    if len({row['reference_id'] for row in catalog['papers']})!=len(catalog['papers']):raise ValueError('Repeated related paper')
    for lang in ['ja','en']:
        ja=lang=='ja';heading='厳密解を学ぶ関連論文' if ja else 'Related papers on exact solutions'
        out='<section class="textbook-related-papers"><h2 id="exact-solution-papers">'+heading+'</h2>'
        for row in catalog['papers']:
            ref=references[row['reference_id']]
            if ref.get('type') in ['book','chapter'] or not ref.get('journal') or not ref.get('doi'):raise ValueError('A related article needs journal and DOI metadata')
            out+='<section aria-labelledby="'+ref['id']+'-paper"><p><strong>'+('原著論文' if ja else 'Original article')+'</strong></p><h3 id="'+ref['id']+'-paper">'+escape(row['title'][lang])+'</h3>'
            citation=ref['author']+' ('+str(ref['year'])+'). '+ref['title']+'. '+ref['journal']+' '+ref['volume']+', '+ref['pages'].replace('--','–')+'.'
            out+='<p lang="en">'+escape(citation)+'</p><p>'+escape(row['summary'][lang])+'</p><p class="book-links"><a href="https://doi.org/'+escape(ref['doi'],quote=True)+'">DOI / '+('出版社の書誌・抄録' if ja else 'Publisher record and abstract')+'</a>'
            for link in row['links']:out+='<a href="'+escape(link['url'][lang],quote=True)+'">'+escape(link['label'][lang])+'</a>'
            out+='</p></section>'
        out+='</section>'
        block='<!-- textbook-related-papers -->'+out+'<!-- /textbook-related-papers -->'
        for filename in ['content.'+lang+'.json']+(['content.json'] if lang=='en' else []):
            p=atlas/filename;data=json.loads(p.read_text());chapter=data['textbooks'];chapter['html']=re.sub(MARKER,'',chapter['html'],flags=re.S).rstrip()+'\n'+block
            chapter['headings']=[x for x in chapter['headings'] if x['id'] not in ['exact-solution-papers',*[row['reference_id']+'-paper' for row in catalog['papers']]]]
            chapter['headings'] += [{'level':2,'id':'exact-solution-papers','title':heading}]+[{'level':3,'id':row['reference_id']+'-paper','title':row['title'][lang]} for row in catalog['papers']]
            p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
        p=atlas/lang/'read/textbooks/index.html';text=re.sub(MARKER,'',p.read_text(),flags=re.S)
        if text.count('</article>')!=1:raise ValueError('Unexpected textbook article boundary')
        text=text.replace('</article>',block+'</article>',1)
        toc_links=''.join('<a href="#'+escape(row['id'],quote=True)+'">'+escape(row['title'])+'</a>' for row in chapter['headings'] if row['level']==2)
        text,count=re.subn(r'(<aside\b[^>]*class="chapter-toc"[^>]*>\s*<p\b[^>]*>.*?</p>\s*<nav\b[^>]*>).*?(</nav>\s*</aside>)',lambda match:match[1]+toc_links+match[2],text,flags=re.S)
        if count!=1:raise ValueError('Unexpected textbook local contents boundary')
        p.write_text(text)
    print('Updated related-paper shelf:',len(catalog['papers']),'article; book inventory unchanged.')
if __name__=='__main__':build()
