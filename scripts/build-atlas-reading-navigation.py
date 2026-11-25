#!/usr/bin/env python3
"""Give existing chapter sidebars their field context and separate resource routes."""
from html import escape
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
BASE = '/numerical-methods-atlas/'
SIDEBAR = re.compile(r'<aside\b(?=[^>]*\bclass="[^"]*\breading-nav\b)[^>]*>.*?</aside>', re.S)
ASSET = re.compile(r'<link\b[^>]*href="/styles/atlas-reading-navigation[.]css[^\"]*"[^>]*>\s*')


def navigation(language, chapter, record, resources):
    ja = language == 'ja'
    matches = [group for group in record['groups'] if any(row['id'] == chapter for row in group['chapters'])]
    if len(matches) != 1:
        raise ValueError('Expected exactly one reading field for '+chapter)
    field = matches[0]

    def link(url, title, ident=None, attributes=''):
        return '<a href="'+escape(url, quote=True)+'"'+(' aria-current="page"' if ident == chapter else '')+attributes+'>'+escape(title)+'</a>'

    def listing(entries):
        return '<ul>'+''.join('<li>'+entry+'</li>' for entry in entries)+'</ul>'

    label = ('この資料の分類' if chapter in resources else 'この章の分野') if ja else ('Resource category' if chapter in resources else 'This chapter’s field')
    peers = [row for row in field['chapters'] if row['id'] not in resources]
    field_url = BASE+language+'/read/#reading-'+field['id']
    body = '<h2>'+label+'</h2><p class="reading-field-title">'+link(field_url, field['title'])+'</p>'
    if chapter not in resources:
        body += '<details class="reading-field-list" open><summary>'+('この分野の章' if ja else 'Chapters in this field')+' ('+str(len(peers))+')</summary>'+listing(
            link(row['url'], row['title'], row['id'], ' data-reading-field-chapter="'+escape(row['id'], quote=True)+'"') for row in peers)+'</details>'
    body += '<details data-reading-other-fields><summary>'+('ほかの分野' if ja else 'Other fields')+'</summary>'+listing(
        link(BASE+language+'/read/#reading-'+group['id'], group['title'], attributes=' data-reading-other-field="'+escape(group['id'], quote=True)+'"')
        for group in record['groups'] if group['id'] != field['id'])+'</details>'
    parts = ['<nav data-reading-navigation-group="field" data-reading-current-field="'+escape(field['id'], quote=True)+'" aria-label="'+label+'">'+body+'</nav>']
    groups = [
        ('learn', '学ぶ・調べる' if ja else 'Learn and look up', [
            link(BASE+'explore/?lang='+language, '学習ガイド（おすすめ順）' if ja else 'Learning guide (suggested order)'),
            link(BASE+language+'/read/', '分野別の全章目次' if ja else 'Complete chapter index', attributes=' data-reading-all-chapters'),
            link(BASE+'methods/?lang='+language, '手法・コードの対応表' if ja else 'Methods and code reference'),
        ]),
        ('resources', '学習資料' if ja else 'Learning resources', [
            link(BASE+language+'/read/textbooks/', '教科書案内' if ja else 'Textbook guide', 'textbooks'),
            link(BASE+language+'/read/references/', '原著・参考文献' if ja else 'Papers and references', 'references'),
        ]),
    ]
    for key, label, entries in groups:
        parts.append('<nav data-reading-navigation-group="'+key+'" aria-label="'+label+'"><h2>'+label+'</h2>'+listing(entries)+'</nav>')
    return '<aside class="reading-nav atlas-reading-nav" aria-label="'+('アトラスの案内' if ja else 'Atlas navigation')+'">'+''.join(parts)+'</aside>'


def reading_records(root):
    source = root/'catalog/atlas-reading-index.json'
    catalog = json.loads(source.read_text())
    source_sha = hashlib.sha256(source.read_bytes()).hexdigest()
    expected = [(group['id'], group['chapters']) for group in catalog['groups']]
    resources = catalog.get('resource_chapters', [])
    records = {}
    for language in ['ja', 'en']:
        record = json.loads((root/'numerical-methods-atlas'/language/'read/index.json').read_text())
        actual = [(group['id'], [row['id'] for row in group['chapters']]) for group in record['groups']]
        if record['source_sha256'] != source_sha or record['language'] != language or actual != expected:
            raise ValueError('Rebuild the complete reading index before chapter navigation: '+language)
        for group in record['groups']:
            for row in group['chapters']:
                if row['language'] not in ['ja', 'en'] or row['url'] != BASE+row['language']+'/read/'+row['id']+'/':
                    raise ValueError('Use the actual published reading edition: '+row['id'])
                if not (root/row['url'].lstrip('/')/'index.html').is_file():
                    raise ValueError('Missing reading destination: '+row['url'])
        records[language] = record
    return records, resources


def build(root=ROOT):
    records, resources = reading_records(root)
    css = root/'styles/atlas-reading-navigation.css'
    stylesheet = '<link rel="stylesheet" href="/styles/atlas-reading-navigation.css?v='+hashlib.sha256(css.read_bytes()).hexdigest()[:12]+'">'
    count = 0
    for language in ['ja', 'en']:
        for page in (root/'numerical-methods-atlas'/language/'read').glob('*/index.html'):
            original = page.read_text()
            if not SIDEBAR.search(original):
                continue
            text, replaced = SIDEBAR.subn(navigation(language, page.parent.name, records[language], resources), original)
            if replaced != 1:
                raise ValueError('Expected one legacy reading sidebar: '+str(page))
            text = ASSET.sub('', text).replace('</head>', stylesheet+'</head>', 1)
            # The page title and article stay intact; only the surrounding category changes.
            if page.parent.name in resources:
                text = re.sub(r'(<body\b)(?![^>]*\bdata-reading-resource=)', r'\1 data-reading-resource="'+page.parent.name+'"', text, count=1)
                label = '学習資料' if language == 'ja' else 'LEARNING RESOURCES'
                text, changed = re.subn(r'(<div class="chapter-topline"><span>).*?(</span>)', lambda m:m[1]+label+m[2], text, count=1)
                if changed != 1:
                    raise ValueError('Missing resource category: '+str(page))
            old_labels = ['解説章の目次', '分野別に解説を読む'] if language == 'ja' else ['Reading chapters', 'Learn by field']
            new_label = '分野別の全章目次' if language == 'ja' else 'Complete chapter index'
            def header_labels(match):
                text = match[0]
                for old in old_labels:
                    text = text.replace('>'+old+'</a>', '>'+new_label+'</a>')
                return text
            text = re.sub(r'<header class="site-header">.*?</header>', header_labels, text, flags=re.S)
            if text != original:
                page.write_text(text)
            count += 1
    print('Built field-aware navigation:', count, 'existing sidebars; other page templates and chapter content retained.')


if __name__ == '__main__':
    build()
