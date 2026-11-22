#!/usr/bin/env python3
"""Replace the legacy alphabetical sidebar with separate learning/resource routes."""
from html import escape
from pathlib import Path
import hashlib
import re

ROOT = Path(__file__).resolve().parents[1]
BASE = '/numerical-methods-atlas/'
SIDEBAR = re.compile(r'<aside\b(?=[^>]*\bclass="[^"]*\breading-nav\b)[^>]*>.*?</aside>', re.S)
ASSET = re.compile(r'<link\b[^>]*href="/styles/atlas-reading-navigation[.]css[^\"]*"[^>]*>\s*')


def navigation(language, chapter):
    ja = language == 'ja'
    groups = [
        ('learn', '学ぶ・調べる' if ja else 'Learn and look up', [
            (BASE+language+'/read/', '分野別に解説を読む' if ja else 'Learn by field', None),
            (BASE+'methods/?lang='+language, '手法・コードの対応表' if ja else 'Methods and code reference', None),
        ]),
        ('resources', '教科書・文献' if ja else 'Books and references', [
            (BASE+language+'/read/textbooks/', '教科書案内' if ja else 'Textbook guide', 'textbooks'),
            (BASE+language+'/read/references/', '原著・参考文献' if ja else 'Papers and references', 'references'),
        ]),
    ]
    parts = []
    for key, label, entries in groups:
        links = ''.join('<li><a href="'+escape(url, quote=True)+'"'+(' aria-current="page"' if ident == chapter else '')+'>'+escape(title)+'</a></li>' for url, title, ident in entries)
        parts.append('<nav data-reading-navigation-group="'+key+'" aria-label="'+escape(label)+'"><h2>'+escape(label)+'</h2><ul>'+links+'</ul></nav>')
    return '<aside class="reading-nav atlas-reading-nav" aria-label="'+('アトラスの案内' if ja else 'Atlas navigation')+'">'+''.join(parts)+'</aside>'


def build(root=ROOT):
    css = root/'styles/atlas-reading-navigation.css'
    stylesheet = '<link rel="stylesheet" href="/styles/atlas-reading-navigation.css?v='+hashlib.sha256(css.read_bytes()).hexdigest()[:12]+'">'
    count = 0
    for language in ['ja', 'en']:
        for page in (root/'numerical-methods-atlas'/language/'read').glob('*/index.html'):
            original = page.read_text()
            if not SIDEBAR.search(original):
                continue
            text, replaced = SIDEBAR.subn(navigation(language, page.parent.name), original)
            if replaced != 1:
                raise ValueError('Expected one legacy reading sidebar: '+str(page))
            text = ASSET.sub('', text).replace('</head>', stylesheet+'</head>', 1)
            # The page title and article stay intact; only the surrounding category changes.
            if page.parent.name in {'textbooks', 'references'}:
                text = re.sub(r'(<body\b)(?![^>]*\bdata-reading-resource=)', r'\1 data-reading-resource="'+page.parent.name+'"', text, count=1)
                label = '学習資料' if language == 'ja' else 'LEARNING RESOURCES'
                text, changed = re.subn(r'(<div class="chapter-topline"><span>).*?(</span>)', lambda m:m[1]+label+m[2], text, count=1)
                if changed != 1:
                    raise ValueError('Missing resource category: '+str(page))
            text = re.sub(r'<header class="site-header">.*?</header>',
                          lambda m:m[0].replace('>解説章の目次</a>', '>分野別に解説を読む</a>').replace('>Reading chapters</a>', '>Learn by field</a>'), text, flags=re.S)
            if text != original:
                page.write_text(text)
            count += 1
    print('Built compact reading navigation:', count, 'pages; books and references separated from chapters.')


if __name__ == '__main__':
    build()
