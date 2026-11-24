#!/usr/bin/env python3
"""Render one complete bilingual reading directory after all chapter builders."""
from html import escape, unescape
from html.parser import HTMLParser
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
BASE = '/numerical-methods-atlas/'
ORIGIN = 'https://hrkoyama.github.io'


class ChapterHeading(HTMLParser):
    def __init__(self):
        super().__init__()
        self.active = False
        self.parts = []

    def handle_starttag(self, tag, attrs):
        if tag == 'h1' and not self.parts:
            self.active = True

    def handle_endtag(self, tag):
        if tag == 'h1':
            self.active = False

    def handle_data(self, data):
        if self.active:
            self.parts.append(data)


def edition_for(requested, available):
    if requested in available:
        return requested
    if 'en' in available:
        return 'en'
    if available:
        return sorted(available)[0]
    raise ValueError('A reading entry must have a published edition')


def plain(value):
    return re.sub(r'\s+', ' ', unescape(re.sub(r'<[^>]*>', '', value))).strip()


def chapter_title(atlas, ident, language, documents):
    directory = atlas / language / 'read' / ident
    parser = ChapterHeading()
    parser.feed((directory / 'index.html').read_text())
    title = plain(''.join(parser.parts))
    if title:
        return title
    metadata = directory / 'index.json'
    if metadata.is_file():
        title = json.loads(metadata.read_text()).get('title')
        if isinstance(title, dict):
            title = title.get(language)
        if isinstance(title, str) and plain(title):
            return plain(title)
    title = documents[language].get(ident, {}).get('title')
    if isinstance(title, str) and plain(title):
        return plain(title)
    raise ValueError('Missing chapter title: '+language+'/'+ident)


def build(root=ROOT):
    atlas = root / 'numerical-methods-atlas'
    source_path = root / 'catalog/atlas-reading-index.json'
    catalog = json.loads(source_path.read_text())
    documents = {lang:json.loads((atlas / ('content.'+lang+'.json')).read_text()) for lang in ['ja','en']}
    available = {}
    for language in ['ja','en']:
        for page in (atlas / language / 'read').glob('*/index.html'):
            available.setdefault(page.parent.name, []).append(language)
    ordered = [ident for group in catalog['groups'] for ident in group['chapters']]
    if len(ordered) != len(set(ordered)):
        raise ValueError('A chapter appears in more than one reading-index group')
    if set(ordered) != set(available):
        raise ValueError('Update catalog/atlas-reading-index.json: missing='+str(sorted(set(available)-set(ordered)))+'; extra='+str(sorted(set(ordered)-set(available))))
    titles = {ident:{lang:chapter_title(atlas,ident,lang,documents) for lang in languages} for ident,languages in available.items()}
    digest = lambda path:hashlib.sha256(path.read_bytes()).hexdigest()[:12]
    source_sha = hashlib.sha256(source_path.read_bytes()).hexdigest()
    for language in ['ja','en']:
        ja = language == 'ja'
        title = catalog['title'][language]
        groups = []
        for group in catalog['groups']:
            entries = []
            for ident in group['chapters']:
                edition = edition_for(language, available[ident])
                text = titles[ident][edition]
                search = ' '.join([ident,*titles[ident].values(),*group['title'].values()])
                entries.append(dict(id=ident,title=text,url=BASE+edition+'/read/'+ident+'/',
                                    language=edition,available_languages=available[ident],search_text=search))
            groups.append(dict(id=group['id'],title=group['title'][language],description=group['description'][language],chapters=entries))
        jump = '<nav class="reading-jump" aria-label="'+('目次の分類' if ja else 'Reading categories')+'">'+''.join(
            '<a data-reading-group-link="'+g['id']+'" href="#reading-'+g['id']+'">'+escape(g['title'])+'</a>' for g in groups)+'</nav>'
        body = []
        for group in groups:
            rows = []
            for chapter in group['chapters']:
                note = ('英語の章' if ja else 'Japanese edition') if chapter['language'] != language else ''
                rows.append('<li data-reading-chapter="'+chapter['id']+'" data-search="'+escape(chapter['search_text'],quote=True)+'"><a href="'+chapter['url']+'"><span>'+escape(chapter['title'])+'</span><span class="reading-arrow" aria-hidden="true">→</span></a>'+('<small class="reading-edition">'+note+'</small>' if note else '')+'</li>')
            body.append('<section class="reading-group" id="reading-'+group['id']+'" data-reading-group="'+group['id']+'" aria-labelledby="heading-'+group['id']+'"><header><h2 id="heading-'+group['id']+'">'+escape(group['title'])+'</h2><p>'+escape(group['description'])+'</p></header><ol class="reading-chapters">'+''.join(rows)+'</ol></section>')
        label = '章名で絞り込む' if ja else 'Filter chapters'
        controls = '<form class="reading-filter" data-reading-controls role="search" hidden><label for="reading-filter">'+label+'</label><div class="reading-filter-row"><input id="reading-filter" data-reading-input type="search" autocomplete="off" placeholder="'+('例：Bratu、衝撃波、FDTD' if ja else 'e.g. Bratu, shocks, FDTD')+'"><button type="button" data-reading-reset>'+('すべて表示' if ja else 'Show all')+'</button></div><p role="status" aria-live="polite" data-reading-count>'+str(len(ordered))+('章' if ja else ' chapters')+'</p></form><p class="reading-empty" data-reading-empty hidden>'+('一致する章がありません。別の語を試すか、「すべて表示」で戻れます。' if ja else 'No chapters match. Try another term or choose Show all.')+'</p>'
        head = '<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+escape(title)+' | '+('数値計算法アトラス' if ja else 'Numerical Methods Atlas')+'</title><meta name="description" content="'+escape(catalog['description'][language],quote=True)+'"><link rel="canonical" href="'+ORIGIN+BASE+language+'/read/">'
        head += ''.join('<link rel="alternate" hreflang="'+edition+'" href="'+ORIGIN+BASE+edition+'/read/">' for edition in ['ja','en'])
        head += '<link rel="stylesheet" href="/styles/atlas-reading-index.css?v='+digest(root/'styles/atlas-reading-index.css')+'"><script type="module" src="'+BASE+'reading-index.mjs?v='+digest(atlas/'reading-index.mjs')+'"></script>'
        related = '<p class="reading-related">'+('適用条件・コード・検証例を手法名から調べる：' if ja else 'Look up a method’s conditions, code and checks: ')+'<a href="'+BASE+'methods/?lang='+language+'">'+('手法・コードの対応表' if ja else 'Methods and code reference')+'</a></p>'
        intro = '<nav class="reading-breadcrumb" aria-label="'+('アトラスの案内' if ja else 'Atlas navigation')+'"><a href="'+BASE+'?lang='+language+'">'+('アトラス' if ja else 'Atlas home')+'</a><span aria-hidden="true">/</span><a href="'+BASE+'explore/?lang='+language+'">'+('体系的に読む' if ja else 'Read systematically')+'</a></nav><header class="reading-heading"><h1>'+escape(title)+'</h1><p>'+escape(catalog['description'][language])+'</p>'+related+'</header>'
        packages = [dict(p, url=p.get('localized_urls', {}).get(language, p['url']),
                         language=language if language in p.get('available_languages', []) else p['language'])
                    for p in catalog.get('learning_packages', [])]
        featured = ''.join('<section class="reading-group"><h2><a href="'+p['url']+'">'+escape(p['title'][language])+'</a></h2><p>'+escape(p['description'][language])+'</p></section>' for p in packages)
        tail = '<footer class="reading-footer"><a href="index.json">JSON</a><a href="index.md">Markdown</a><a href="'+BASE+'methods/?lang='+language+'">'+('手法・コードの対応表' if ja else 'Methods and code reference')+'</a></footer>'
        page = '<!doctype html><html lang="'+language+'"><head>'+head+'</head><body class="atlas-reading-index"><main class="reading-index" id="reading-index" data-language="'+language+'">'+intro+featured+controls+jump+''.join(body)+tail+'</main></body></html>\n'
        directory = atlas / language / 'read'
        (directory/'index.html').write_text(page)
        record = dict(schema_version=1,language=language,title=title,description=catalog['description'][language],
                      source='/catalog/atlas-reading-index.json',source_sha256=source_sha,chapter_count=len(ordered),groups=groups,learning_packages=packages)
        (directory/'index.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
        markdown = '# '+title+'\n\n'+catalog['description'][language]+'\n\n'
        for p in packages:
            markdown += '## ['+p['title'][language]+']('+ORIGIN+p['url']+')\n\n'+p['description'][language]+'\n\n'
        for group in groups:
            markdown += '## '+group['title']+'\n\n'+group['description']+'\n\n'
            markdown += '\n'.join('- ['+c['title']+']('+ORIGIN+c['url']+')'+((' (English)' if c['language']=='en' else ' (Japanese)') if c['language']!=language else '') for c in group['chapters'])+'\n\n'
        (directory/'index.md').write_text(markdown)
    print('Built unified reading directories:',len(ordered),'chapters in',len(catalog['groups']),'groups; existing chapter URLs retained.')


if __name__ == '__main__':
    build()
