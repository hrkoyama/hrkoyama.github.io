#!/usr/bin/env python3
"""Give existing chapter sidebars their field context and separate resource routes."""
from html import escape
from html.parser import HTMLParser
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
BASE = '/numerical-methods-atlas/'
SIDEBAR = re.compile(r'<aside\b(?=[^>]*\bclass="[^"]*\breading-nav\b)[^>]*>.*?</aside>', re.S)
ASSET = re.compile(r'<link\b[^>]*href="/styles/atlas-reading-navigation[.]css[^\"]*"[^>]*>\s*')
WRAP = re.compile(r'<div class="chapter-wrap"(?: data-reading-layout="opening-first")?>')
JUMP = re.compile(r'<!-- chapter-resource-jump -->.*?<!-- /chapter-resource-jump -->', re.S)
POSITION = '<!-- chapter-resource-position -->'
RESOURCE_OPENINGS = frozenset(['textbooks', 'references'])


class ArticleSpan:
    """Byte-preserving string spans with the small match interface used below."""
    def __init__(self, text, start, opening_end, closing_start, end):
        self.text = text
        self.starts = (start, start, opening_end, closing_start)
        self.ends = (end, opening_end, closing_start, end)

    def __getitem__(self, group):
        return self.text[self.start(group):self.end(group)]

    def start(self, group=0):
        return self.starts[group]

    def end(self, group=0):
        return self.ends[group]


class ProseArticles:
    def finditer(self, text):
        class Boundaries(HTMLParser):
            def __init__(self):
                super().__init__(convert_charrefs=False)
                self.lines = [0]+[m.end() for m in re.finditer('\n', text)]
                self.depth = 0
                self.spans = []

            def position(self):
                line, column = self.getpos()
                return self.lines[line-1]+column

            def handle_starttag(self, tag, attrs):
                if tag != 'article':
                    return
                if self.depth:
                    self.depth += 1
                elif 'prose' in dict(attrs).get('class', '').split():
                    self.begin = self.position()
                    self.opening_end = self.begin+len(self.get_starttag_text())
                    self.depth = 1

            def handle_endtag(self, tag):
                if tag == 'article' and self.depth:
                    self.depth -= 1
                    if not self.depth:
                        closing = self.position()
                        self.spans.append(ArticleSpan(text, self.begin, self.opening_end,
                                                      closing, text.index('>', closing)+1))

        parser = Boundaries()
        parser.feed(text)
        parser.close()
        if parser.depth:
            raise ValueError('Unclosed legacy prose article')
        return iter(parser.spans)

    def search(self, text, position=0):
        return next((span for span in self.finditer(text) if span.start() >= position), None)


ARTICLE = ProseArticles()


def marked_part(text, name):
    pattern = re.compile(r'<!-- '+name+r' -->(.*?)<!-- /'+name+r' -->', re.S)
    matches = list(pattern.finditer(text))
    if len(matches) != 1:
        raise ValueError('Expected one '+name)
    return matches[0]


def restore_legacy_article(text):
    """Undo only our presentation wrappers, including after an upstream rebuild.

    Some earlier stages replace the complete article. In that case its current
    H1 is authoritative; an old extracted opening must not be added a second
    time. A leading scientific notice is stored separately so the inverse of
    an ordinary rerun retains its original position and exact bytes.
    """
    if 'data-reading-layout="opening-first"' not in text:
        return text
    wrap = WRAP.search(text)
    article = ARTICLE.search(text, wrap.end()) if wrap else None
    if not wrap or not article:
        raise ValueError('Missing legacy reading layout boundaries')
    prefix = text[wrap.end():article.start()]
    opening = marked_part(prefix, 'legacy-reading-opening')[1]
    opening_tag = '<div class="prose legacy-reading-opening" data-chapter-opening data-legacy-reading-opening>'
    if not opening.startswith(opening_tag) or not opening.endswith('</div>'):
        raise ValueError('Unexpected legacy opening wrapper')
    opening = opening[len(opening_tag):-len('</div>')]
    metadata = marked_part(prefix, 'legacy-reading-metadata')[1]
    metadata_tag = '<div class="legacy-reading-metadata">'
    if not metadata.startswith(metadata_tag) or not metadata.endswith('</div>'):
        raise ValueError('Unexpected legacy metadata wrapper')
    metadata = metadata[len(metadata_tag):-len('</div>')]
    marked_part(prefix, 'legacy-reading-mobile-toc')
    jumps = list(JUMP.finditer(prefix))
    if len(jumps) > 1 or prefix.count(POSITION) != 1:
        raise ValueError('Ambiguous legacy chapter resource position')
    body = article[2]
    headings = list(re.finditer(r'<h1\b[^>]*>.*?</h1>', body, re.S))
    if not headings:
        notice = marked_part(body, 'legacy-reading-leading-notice')
        body = body[:notice.start()]+notice[1]+opening+body[notice.end():]
    elif len(headings) != 1 or 'legacy-reading-leading-notice' in body:
        raise ValueError('Ambiguous upstream legacy article rebuild')
    jump = jumps[0][0] if jumps else ''
    return (text[:wrap.start()]+'<div class="chapter-wrap">'+metadata+jump+
            article[1]+body+article[3]+text[article.end():])


def legacy_reading_layout(text):
    """Move an existing H1/first paragraph; never synthesize scientific prose."""
    text = restore_legacy_article(text)
    wraps = list(WRAP.finditer(text))
    articles = list(ARTICLE.finditer(text))
    contents = list(re.finditer(r'<aside class="chapter-toc">(.*?)</aside>', text, re.S))
    if len(wraps) != 1 or len(articles) != 1 or len(contents) != 1:
        raise ValueError('Expected one legacy chapter, article and desktop contents')
    wrap, article = wraps[0], articles[0]
    if article.start() < wrap.end():
        raise ValueError('Legacy article must follow its chapter wrapper')
    before = text[wrap.end():article.start()]
    jumps = list(JUMP.finditer(before))
    if len(jumps) > 1:
        raise ValueError('Duplicate legacy chapter resource jumps')
    metadata = JUMP.sub('', before)
    if POSITION in metadata or 'legacy-reading-' in metadata:
        raise ValueError('Unrestored legacy presentation metadata')
    body = article[2]
    headings = list(re.finditer(r'<h1\b[^>]*>.*?</h1>', body, re.S))
    if len(headings) != 1:
        raise ValueError('Expected one existing legacy H1')
    heading = headings[0]
    # Only a paragraph directly following H1 is an existing lead. Do not lift
    # the first paragraph from a later section, callout, figure or equation.
    lead = re.match(r'\s*<p\b[^>]*>.*?</p>', body[heading.end():], re.S)
    end = heading.end()+(lead.end() if lead else 0)
    opening = body[heading.start():end]
    notice = body[:heading.start()]
    remainder = body[end:]
    toc = re.search(r'<nav\b[^>]*\baria-label="([^"]+)"[^>]*>(.*?)</nav>', contents[0][1], re.S)
    if not toc:
        raise ValueError('Missing existing labeled desktop contents')
    # Copy every existing contents link. The semantic nav also lets prose-only
    # exporters exclude this duplicate navigation and its summary label.
    mobile = ('<!-- legacy-reading-mobile-toc --><nav class="legacy-reading-mobile-toc" aria-label="'+toc[1]+'">'
              '<details class="reading-toc-details"><summary>'+toc[1]+'</summary><div class="reading-toc-links">'+
              toc[2]+'</div></details></nav>'
              '<!-- /legacy-reading-mobile-toc -->')
    front = ('<!-- legacy-reading-opening --><div class="prose legacy-reading-opening" data-chapter-opening data-legacy-reading-opening>'+
             opening+'</div><!-- /legacy-reading-opening -->'+POSITION+
             (jumps[0][0] if jumps else '')+mobile+
             '<!-- legacy-reading-metadata --><div class="legacy-reading-metadata">'+metadata+
             '</div><!-- /legacy-reading-metadata -->')
    science = '<!-- legacy-reading-leading-notice -->'+notice+'<!-- /legacy-reading-leading-notice -->'+remainder
    return (text[:wrap.start()]+'<div class="chapter-wrap" data-reading-layout="opening-first">'+front+
            article[1]+science+article[3]+text[article.end():])


def resource_breadcrumb(language):
    if language not in ['ja', 'en']:
        raise ValueError('Unknown reading resource language')
    label = '分野別の全章目次' if language == 'ja' else 'Complete chapter index'
    return ('<!-- resource-reading-breadcrumb --><nav class="reading-breadcrumb resource-reading-breadcrumb" aria-label="'+label+'">'
            '<a href="'+BASE+language+'/read/">'+label+'</a></nav><!-- /resource-reading-breadcrumb -->')


def restore_resource_article(text, language):
    """Remove the one declared resource breadcrumb, then undo the shared layout."""
    if 'resource-reading-breadcrumb' in text:
        breadcrumb = marked_part(text, 'resource-reading-breadcrumb')
        if breadcrumb[0] != resource_breadcrumb(language):
            raise ValueError('Unexpected reading resource breadcrumb')
        text = text[:breadcrumb.start()]+text[breadcrumb.end():]
    return restore_legacy_article(text)


def resource_reading_layout(text, language, chapter):
    """Give the two existing resource articles a title-first, reversible opening.

    Existing translation/draft notices remain visible directly after the lead;
    only their position changes. The desktop contents and full article retain
    the same bytes, while the shared mobile disclosure copies its exact links.
    """
    if chapter not in RESOURCE_OPENINGS:
        raise ValueError('Unknown reading resource opening')
    text = legacy_reading_layout(restore_resource_article(text, language))
    opening = marked_part(text, 'legacy-reading-opening')
    metadata = marked_part(text, 'legacy-reading-metadata')
    if metadata.start() < opening.end():
        raise ValueError('Unexpected reading resource metadata position')
    text = (text[:opening.end()]+metadata[0]+text[opening.end():metadata.start()]+
            text[metadata.end():])
    wrap = WRAP.search(text)
    return text[:wrap.end()]+resource_breadcrumb(language)+text[wrap.end():]


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
            link(BASE+'methods/?lang='+language, '全手法一覧' if ja else 'All methods'),
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


def build(root=ROOT, openings_only=False):
    records, resources = reading_records(root)
    documents = {language: json.loads((root/'numerical-methods-atlas'/('content.'+language+'.json')).read_text())
                 for language in ['ja', 'en']}
    css = root/'styles/atlas-reading-navigation.css'
    stylesheet = '<link rel="stylesheet" href="/styles/atlas-reading-navigation.css?v='+hashlib.sha256(css.read_bytes()).hexdigest()[:12]+'">'
    count = 0
    updates = []
    openings = {language: [] for language in ['ja', 'en']}
    resource_openings = {language: [] for language in ['ja', 'en']}
    for language in ['ja', 'en']:
        for page in (root/'numerical-methods-atlas'/language/'read').glob('*/index.html'):
            original = page.read_text()
            if not SIDEBAR.search(original):
                continue
            eligible = (page.parent.name in documents[language] and page.parent.name not in resources and
                        'class="reading-shell page-width"' in original)
            if openings_only and not eligible:
                continue
            text, replaced = SIDEBAR.subn(navigation(language, page.parent.name, records[language], resources), original)
            if replaced != 1:
                raise ValueError('Expected one legacy reading sidebar: '+str(page))
            text = ASSET.sub('', text).replace('</head>', stylesheet+'</head>', 1)
            # Keep the existing 44-chapter projection and its CLI scope intact.
            if eligible:
                text = legacy_reading_layout(text)
                openings[language].append(page.parent.name)
            if page.parent.name in resources:
                text = re.sub(r'(<body\b)(?![^>]*\bdata-reading-resource=)', r'\1 data-reading-resource="'+page.parent.name+'"', text, count=1)
                label = '学習資料' if language == 'ja' else 'LEARNING RESOURCES'
                text, changed = re.subn(r'(<div class="chapter-topline"><span>).*?(</span>)', lambda m:m[1]+label+m[2], text, count=1)
                if changed != 1:
                    raise ValueError('Missing resource category: '+str(page))
                if page.parent.name in RESOURCE_OPENINGS and 'class="reading-shell page-width"' in original:
                    text = resource_reading_layout(text, language, page.parent.name)
                    resource_openings[language].append(page.parent.name)
            old_labels = ['解説章の目次', '分野別に解説を読む'] if language == 'ja' else ['Reading chapters', 'Learn by field']
            new_label = '分野別の全章目次' if language == 'ja' else 'Complete chapter index'
            def header_labels(match):
                text = match[0]
                for old in old_labels:
                    text = text.replace('>'+old+'</a>', '>'+new_label+'</a>')
                # Role names follow these existing header destinations only.
                labels = {
                    BASE+'?lang='+language+'#/methods': '分野別ガイド' if language == 'ja' else 'Guides by field',
                    BASE+'?lang='+language+'#/equations': '計算例' if language == 'ja' else 'Calculation examples',
                    BASE+'methods/?lang='+language: '全手法一覧' if language == 'ja' else 'All methods',
                }
                for href, label in labels.items():
                    anchor = r'(<a\b[^>]*\bhref="'+re.escape(href)+r'"[^>]*>)[^<]*(</a>)'
                    text = re.sub(anchor, lambda item:item[1]+label+item[2], text)
                return text
            text = re.sub(r'<header class="site-header">.*?</header>', header_labels, text, flags=re.S)
            if text != original:
                updates.append((page, text))
            count += 1
    if set(openings['ja']) != set(openings['en']):
        raise ValueError('Legacy opening scope must match in Japanese and English')
    if set(resource_openings['ja']) != set(resource_openings['en']):
        raise ValueError('Resource opening scope must match in Japanese and English')
    for page, text in updates:
        page.write_text(text)
    print('Built field-aware navigation:', count, 'existing sidebars; other page templates and chapter content retained.')
    print('Opening-first legacy chapters:', len(openings['ja']), 'logical chapters;', sum(map(len, openings.values())), 'editions.')
    print('Opening-first learning resources:', len(resource_openings['ja']), 'logical resources;', sum(map(len, resource_openings.values())), 'editions.')


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--openings-only', action='store_true', help='Update only old reading-shell chapters, not learning resources.')
    build(openings_only=parser.parse_args().openings_only)
