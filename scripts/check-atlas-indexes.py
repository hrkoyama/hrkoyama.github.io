#!/usr/bin/env python3
"""Check derived reading indexes against the actual published pages, offline."""
from collections import Counter
from html import unescape
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlsplit
import argparse
import json
import os
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
ORIGIN = 'https://hrkoyama.github.io'
BASE = '/numerical-methods-atlas/'
LANGUAGES = ('ja', 'en')
CHAPTER_ROUTE = re.compile(r'^/numerical-methods-atlas/(ja|en)/read/([^/]+)/$')
VOID_TAGS = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr'}


def plain(value):
    return ' '.join(unescape(value).split())


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.heading = []
        self.links = []
        self.canonicals = []
        self.noindex = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        parent = self.stack[-1] if self.stack else {}
        hidden = parent.get('hidden', False) or 'hidden' in attrs or attrs.get('aria-hidden') == 'true'
        anchor = parent.get('anchor')
        if tag == 'a' and attrs.get('href'):
            anchor = len(self.links)
            self.links.append({'href': attrs['href'], 'parts': []})
        if tag == 'link' and 'canonical' in attrs.get('rel', '').split():
            self.canonicals.append(attrs.get('href', ''))
        if tag == 'meta' and attrs.get('name', '').lower() == 'robots' and 'noindex' in attrs.get('content', '').lower():
            self.noindex = True
        if tag not in VOID_TAGS:
            self.stack.append({'tag': tag, 'hidden': hidden, 'heading': tag == 'h1' or parent.get('heading', False), 'anchor': anchor})

    def handle_endtag(self, tag):
        for index in range(len(self.stack) - 1, -1, -1):
            if self.stack[index]['tag'] == tag:
                del self.stack[index:]
                break

    def handle_data(self, value):
        if not self.stack or self.stack[-1]['hidden']:
            return
        current = self.stack[-1]
        if current['heading']:
            self.heading.append(value)
        if current['anchor'] is not None:
            self.links[current['anchor']]['parts'].append(value)

    @property
    def title(self):
        return plain(''.join(self.heading))


def parse(path):
    page = Page()
    page.feed(path.read_text())
    return page


def inventory(root):
    chapters = {}
    for language in LANGUAGES:
        for path in sorted((root / BASE.strip('/') / language / 'read').glob('*/index.html')):
            chapters.setdefault(path.parent.name, {})[language] = parse(path).title
    return chapters


def describe(values):
    values = sorted(values)
    return ', '.join(values[:8]) + (' … (' + str(len(values)) + ')' if len(values) > 8 else '')


def compare_sets(errors, label, actual, expected):
    actual, expected = set(actual), set(expected)
    if actual != expected:
        errors.append(label + ': inventory differs; missing=[' + describe(expected - actual) + ']; extra=[' + describe(actual - expected) + ']')


def route(href, base=ORIGIN + BASE):
    url = urlsplit(urljoin(base, href))
    if url.scheme != 'https' or url.netloc != 'hrkoyama.github.io':
        return None
    match = CHAPTER_ROUTE.fullmatch(url.path)
    return (match[1], match[2]) if match else None


def read_json(root, relative, errors):
    try:
        return json.loads((root / relative).read_text())
    except (OSError, ValueError) as exc:
        errors.append(relative + ': cannot read JSON: ' + str(exc))
        return {}


def check_toc(root, chapters, language, errors):
    prefix = 'numerical-methods-atlas/' + language + '/read/'
    expected = {}
    for chapter, editions in chapters.items():
        edition = language if language in editions else 'en' if 'en' in editions else sorted(editions)[0]
        expected[(edition, chapter)] = editions[edition]
    record = read_json(root, prefix + 'index.json', errors)
    rows = [chapter for group in record.get('groups', []) for chapter in group.get('chapters', [])]
    compare_sets(errors, prefix + 'index.json IDs', [row.get('id', '') for row in rows], chapters)
    if len(rows) != len(chapters) or record.get('chapter_count') != len(chapters):
        errors.append(prefix + 'index.json: chapter count or duplicates differ from published inventory')
    if record.get('language') != language:
        errors.append(prefix + 'index.json: incorrect index language')
    for row in rows:
        chapter = row.get('id')
        if chapter not in chapters:
            continue
        actual_route = route(row.get('url', ''), ORIGIN + '/' + prefix)
        wanted = next(key for key in expected if key[1] == chapter)
        if actual_route != wanted or row.get('language') != wanted[0]:
            errors.append(prefix + 'index.json: incorrect edition route for ' + chapter)
        if plain(row.get('title', '')) != expected[wanted]:
            errors.append(prefix + 'index.json: stale title for ' + chapter)
        if sorted(row.get('available_languages', [])) != sorted(chapters[chapter]):
            errors.append(prefix + 'index.json: stale available languages for ' + chapter)
    for suffix in ('html', 'md'):
        path = root / (prefix + 'index.' + suffix)
        try:
            if suffix == 'html':
                pairs = [(route(link['href'], ORIGIN + '/' + prefix), plain(''.join(link['parts']))) for link in parse(path).links]
            else:
                pairs = [(route(href, ORIGIN + '/' + prefix), plain(title)) for title, href in re.findall(r'^\s*-\s+\[(.*?)\]\(([^)]+)\)', path.read_text(), re.M)]
        except OSError as exc:
            errors.append(str(path.relative_to(root)) + ': cannot read index: ' + str(exc))
            continue
        pairs = [(key, title) for key, title in pairs if key is not None]
        label = prefix + 'index.' + suffix
        actual = Counter(key for key, _ in pairs)
        compare_sets(errors, label, [edition + '/' + chapter for edition, chapter in actual], [edition + '/' + chapter for edition, chapter in expected])
        if any(count != 1 for count in actual.values()):
            errors.append(label + ': duplicate chapter links')
        for key, title in pairs:
            if key in expected and title != expected[key]:
                errors.append(label + ': stale title for ' + key[1])


def check_language_mapping(root, chapters, errors):
    relative = 'numerical-methods-atlas/home-overview-data.js'
    try:
        source = (root / relative).read_text()
        match = re.search(r'export\s+const\s+homeReadingLanguages\s*=\s*(\{.*?\})\s*;', source, re.S)
        mapping = json.loads(match[1]) if match else None
        if not isinstance(mapping, dict):
            raise ValueError('missing JSON homeReadingLanguages assignment')
        expected = {chapter: sorted(editions) for chapter, editions in chapters.items()}
        compare_sets(errors, relative, mapping, expected)
        for chapter in set(mapping) & set(expected):
            if sorted(mapping[chapter]) != expected[chapter]:
                errors.append(relative + ': stale editions for ' + chapter)
    except (OSError, ValueError, TypeError) as exc:
        errors.append(relative + ': cannot read language mapping: ' + str(exc))


def check_chapter_search(root, chapters, errors):
    relative = 'numerical-methods-atlas/home-search-index.json'
    data = read_json(root, relative, errors)
    entries = [row for row in data.get('entries', []) if row.get('kind') == 'chapter']
    counts = Counter(row.get('chapter', '') for row in entries)
    compare_sets(errors, relative + ' chapter IDs', counts, chapters)
    if any(count != 1 for count in counts.values()):
        errors.append(relative + ': duplicate canonical chapter entries')
    for entry in entries:
        chapter = entry.get('chapter')
        if chapter not in chapters:
            continue
        routes = entry.get('routes', {})
        compare_sets(errors, relative + ' editions for ' + chapter, routes, chapters[chapter])
        for language in LANGUAGES:
            expected_title = chapters[chapter].get(language)
            actual_title = entry.get('title', {}).get(language)
            if (plain(actual_title) if actual_title is not None else None) != expected_title:
                errors.append(relative + ': stale ' + language + ' title for ' + chapter)
            if language in chapters[chapter] and route(routes.get(language, '')) != (language, chapter):
                errors.append(relative + ': incorrect ' + language + ' route for ' + chapter)


def check_sitemaps(root, errors):
    canonicals, atlas_canonicals = set(), set()
    for parent, directories, files in os.walk(root):
        directories[:] = [name for name in directories if not name.startswith('.') and name not in {'node_modules', 'scripts', 'docs'}]
        for name in files:
            if not name.endswith('.html') or name.startswith('google'):
                continue
            path = Path(parent) / name
            page = parse(path)
            if page.noindex:
                continue
            for canonical in page.canonicals:
                if not canonical.startswith(ORIGIN + '/'):
                    continue
                canonicals.add(canonical)
                if path.relative_to(root).parts[0] == 'numerical-methods-atlas':
                    atlas_canonicals.add(canonical)
    for relative, expected in [('sitemap.xml', canonicals), ('numerical-methods-atlas/sitemap.xml', atlas_canonicals)]:
        try:
            actual = [node.text or '' for node in ET.parse(root / relative).findall('.//{*}loc')]
            compare_sets(errors, relative, actual, expected)
            if len(actual) != len(set(actual)):
                errors.append(relative + ': duplicate canonical URLs')
        except (OSError, ET.ParseError) as exc:
            errors.append(relative + ': cannot read sitemap: ' + str(exc))


def audit(root=ROOT):
    root = Path(root).resolve()
    errors = []
    chapters = inventory(root)
    if not chapters:
        errors.append('No published reading chapters found')
    for chapter, editions in chapters.items():
        for language, title in editions.items():
            if not title:
                errors.append('Published chapter has no H1 title: ' + language + '/' + chapter)
    for language in LANGUAGES:
        check_toc(root, chapters, language, errors)
    check_language_mapping(root, chapters, errors)
    check_chapter_search(root, chapters, errors)
    check_sitemaps(root, errors)
    return {'chapters': len(chapters), 'chapter_editions': sum(map(len, chapters.values())), 'errors': errors}


def check(root=ROOT):
    return audit(root)['errors']


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    result = audit(parser.parse_args().root)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    raise SystemExit(bool(result['errors']))
