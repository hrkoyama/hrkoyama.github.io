#!/usr/bin/env python3
"""Connect every physical reading edition without altering its scientific body."""
from copy import deepcopy
from hashlib import sha256
from html.parser import HTMLParser
import json
from pathlib import Path
import re

from atlas_chapter_resource_cards import render_chapter_resources, render_chapter_resource_jump
from atlas_search_routes import load_search_routes

ROOT = Path(__file__).resolve().parents[1]
ORIGIN = 'https://hrkoyama.github.io'
BASE = '/numerical-methods-atlas/'
LANGUAGES = ('ja', 'en')
GROUPS = ('methods', 'equations', 'figures', 'references', 'code')
GENERATOR = 'atlas-chapter-resources'
MARKERS = ('chapter-resource-jump', 'chapter-resources', 'chapter-resource-assets')


def strip_resources(text):
    """Remove only this builder's bounded decorations, retaining original bytes."""
    for marker in MARKERS:
        text = re.sub(r'<!-- '+marker+r' -->.*?<!-- /'+marker+r' -->', '', text, flags=re.S)
    return text


class ReadingPage(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.source = text
        self.lines = [0]
        self.lines += [match.end() for match in re.finditer('\n', text)]
        self.articles = []
        self.heading = False
        self.title_parts = []
        self.title = ''
        self.jump = None
        self.main_end = None
        self.head_end = None
        self.feed(text)
        if not self.title or self.jump is None or self.main_end is None or self.head_end is None:
            raise ValueError('Reading edition needs a main H1, head and main boundaries')

    def absolute_position(self):
        line, column = self.getpos()
        return self.lines[line-1]+column

    def handle_starttag(self, tag, attrs):
        if tag == 'article':
            self.articles.append(self.absolute_position())
        if tag == 'h1' and not self.title and not self.heading:
            self.heading = True
            if self.articles:
                self.jump = self.articles[0]

    def handle_endtag(self, tag):
        if tag == 'h1' and self.heading:
            self.title = ' '.join(''.join(self.title_parts).split())
            self.heading = False
            if self.jump is None:
                self.jump = self.source.index('>', self.absolute_position())+1
        if tag == 'article' and self.articles:
            self.articles.pop()
        if tag == 'main':
            self.main_end = self.absolute_position()
        if tag == 'head':
            self.head_end = self.absolute_position()

    def handle_data(self, value):
        if self.heading:
            self.title_parts.append(value)


def directories():
    definitions = {
        'methods': ('手法・コードの対応表', 'Methods and code reference', 'methods/'),
        'equations': ('方程式', 'Equations', 'equations/'),
        'figures': ('テスト問題の名前と図', 'Test problems by name and figure', 'gallery/'),
        'references': ('厳密解・参照解', 'Exact and reference solutions', 'solutions/'),
        'code': ('コード・入力・検証', 'Code, inputs and validation', 'code-and-data/'),
    }
    return {key: {'name': {'ja': ja, 'en': en},
                  'url': {lang: ORIGIN+BASE+path+'?lang='+lang for lang in LANGUAGES}}
            for key, (ja, en, path) in definitions.items()}


def load_chapter_resources(root=ROOT, navigation=None):
    root = Path(root).resolve()
    if navigation is None:
        navigation = load_search_routes(root)
    pages = {}
    for language in LANGUAGES:
        for path in sorted((root/'numerical-methods-atlas'/language/'read').glob('*/index.html')):
            ident = path.parent.name
            if not re.fullmatch(r'[a-z0-9][a-z0-9.-]*', ident):
                raise ValueError('Unsafe reading identity: '+ident)
            page = ReadingPage(strip_resources(path.read_text()))
            pages.setdefault(ident, {})[language] = page
    records = {}
    for ident, editions in sorted(pages.items()):
        original = navigation['nodes'].get('chapter:'+ident)
        registered = original is not None and any(original['groups'][key] for key in GROUPS)
        graph = deepcopy(original) if registered else {
            'kind': 'chapter', 'id': ident,
            'note': {'ja': 'このページではアトラス全体の資料一覧へ案内します。章固有の対応は未登録です。',
                     'en': 'This page links to atlas-wide resource indexes; chapter-specific associations are not registered.'},
            'groups': {key: [] for key in GROUPS}}
        records[ident] = {
            'id': ident, 'title': {lang: page.title for lang, page in editions.items()},
            'routes': {lang: ORIGIN+BASE+lang+'/read/'+ident+'/' for lang in editions},
            'association_status': 'registered' if registered else 'directory-only',
            'resource_navigation': graph, 'directories': directories()}
    return {'schema_version': 1, 'generated_by': GENERATOR, 'chapters': records,
            'source_sha256': deepcopy(navigation['source_sha256'])}


def markdown(record, language):
    graph = record['resource_navigation']
    out = '# '+record['title'][language]+'\n\n'
    out += ('この章の関連資料\n\n' if language == 'ja' else 'Resources for this chapter\n\n')
    out += record['routes'][language]+'\n\n'+graph['note'][language]+'\n\n'
    labels = {'methods': ('手法', 'Methods'), 'equations': ('方程式', 'Equations'),
              'figures': ('問題の図', 'Problem figures'), 'references': ('厳密解・参照解', 'Exact / reference solutions'),
              'code': ('コード・検証', 'Code and validation')}
    for key in GROUPS:
        out += '## '+labels[key][language == 'en']+'\n\n'
        entries = graph['groups'][key]
        if key == 'code':
            entries = sorted(entries, key=lambda entry: entry.get('availability') != 'run')
        for entry in entries:
            # Names are plain text; angle brackets keep literal URL parentheses intact.
            name = entry['name'][language].replace('[', '\\[').replace(']', '\\]')
            out += '- ['+name+'](<'+entry['url'][language]+'>)\n'
            if entry.get('relation'):
                out += '  relation: '+entry['relation']+'\n'
            if entry.get('reference_kind'):
                out += '  reference_kind: '+entry['reference_kind']+'\n'
            if entry.get('availability'):
                out += '  availability: '+entry['availability']+'\n'
            if entry.get('note'):
                out += '\n  '+entry['note'][language]+'\n'
            if entry.get('image'):
                out += '\n  '+entry['image']['url']+'\n'
        if not entries:
            directory = record['directories'][key]
            out += ('章固有の対応は未登録です。全体一覧：' if language == 'ja' else 'No chapter-specific association is registered. Atlas-wide index: ')
            out += '['+directory['name'][language]+']('+directory['url'][language]+')\n'
        out += '\n'
    return out.rstrip()+'\n'


def dump(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False)+'\n')


def build(root=ROOT, navigation=None):
    root = Path(root).resolve()
    data = load_chapter_resources(root, navigation)
    css = root/'styles/atlas-chapter-resources.css'
    asset = '<link rel="stylesheet" href="/styles/atlas-chapter-resources.css?v='+sha256(css.read_bytes()).hexdigest()[:12]+'">'
    count = 0
    for ident, record in data['chapters'].items():
        for language in record['routes']:
            directory = root/'numerical-methods-atlas'/language/'read'/ident
            path = directory/'index.html'
            original = strip_resources(path.read_text())
            page = ReadingPage(original)
            footer = render_chapter_resources(record, language)
            downloads = '<p class="chapter-resource-downloads"><a href="resources.json">'+('この章の関連資料 / JSON' if language == 'ja' else 'Chapter resources / JSON')+'</a> · <a href="resources.md">Markdown</a></p>'
            footer = footer[:-len('</section>')]+downloads+'</section>'
            inserts = [
                (page.head_end, '<!-- chapter-resource-assets -->'+asset+'<!-- /chapter-resource-assets -->'),
                (page.jump, '<!-- chapter-resource-jump -->'+render_chapter_resource_jump(record, language)+'<!-- /chapter-resource-jump -->'),
                (page.main_end, '<!-- chapter-resources -->'+footer+'<!-- /chapter-resources -->'),
            ]
            text = original
            for position, insertion in sorted(inserts, reverse=True):
                text = text[:position]+insertion+text[position:]
            path.write_text(text)
            dump(directory/'resources.json', {'schema_version': 1, 'generated_by': GENERATOR, **record,
                                              'language': language, 'source_sha256': data['source_sha256']})
            (directory/'resources.md').write_text(markdown(record, language))
            count += 1
    # Remove only orphaned sidecars positively identified as this builder's work.
    for language in LANGUAGES:
        for sidecar in (root/'numerical-methods-atlas'/language/'read').glob('*/resources.json'):
            if (sidecar.parent/'index.html').exists():
                continue
            old = json.loads(sidecar.read_text())
            if old.get('generated_by') == GENERATOR:
                sidecar.unlink()
                sidecar.with_suffix('.md').unlink(missing_ok=True)
    destination = root/'numerical-methods-atlas/reading-resources.json'
    dump(destination, data)
    editions = {ident: {lang: url.removeprefix(ORIGIN) for lang, url in record['routes'].items()}
                for ident, record in data['chapters'].items()}
    module = root/'numerical-methods-atlas/chapter-resources.mjs'
    module.write_text('// Generated from physically published reading editions.\nexport const chapterEditions='+json.dumps(editions, ensure_ascii=False, separators=(',', ':'))+';\n')
    app = root/'numerical-methods-atlas/app.js'
    if app.is_file():
        digest = sha256(module.read_bytes()).hexdigest()[:12]
        app.write_text(re.sub(r"from './chapter-resources[.]mjs(?:\?v=[a-f0-9]+)?'",
                              "from './chapter-resources.mjs?v="+digest+"'", app.read_text()))
    llms = root/'llms.txt'
    if llms.is_file():
        marker = '- [Reading chapter resource routes]('
        lines = [line for line in llms.read_text().splitlines() if not line.startswith(marker)]
        lines.append(marker+ORIGIN+BASE+'reading-resources.json): all physical chapter editions, scoped methods/equations/problem figures/references/code, and per-edition resources.json/resources.md; global directories are labelled separately from registered chapter associations.')
        llms.write_text('\n'.join(lines)+'\n')
    print('Connected', len(data['chapters']), 'physical chapters across', count, 'editions; scientific article and legacy downloads preserved.')
    return data


if __name__ == '__main__':
    build()
