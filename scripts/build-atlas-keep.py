#!/usr/bin/env python3
"""Render the bilingual KEEP explanation from its editable HTML/LaTeX catalog.

This builds documentation only. The dated solver packages and measurements are
not regenerated. Static pages and the SPA share the same mathematical content.
"""
import html
import hashlib
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
ATLAS = ROOT / 'numerical-methods-atlas'
SOURCE = '/catalog/atlas-keep-explanation.json'
data = json.loads((ROOT / SOURCE.lstrip('/')).read_text())
formulas = data['formulas']
rendered = json.loads(subprocess.check_output(
    ['node', 'scripts/render-atlas-math.cjs'], cwd=ROOT,
    input=json.dumps([{'id': key, 'formula': [value]} for key, value in formulas.items()]).encode(),
))['rendered']
anchors = {}
for lang in ['ja', 'en']:
    chapter = data['chapters'][lang]
    def equation(match):
        key = match[1]
        return '<div class="math-block">' + rendered[key][0] + '</div>'
    body = re.sub(r'<math-placeholder id="([a-z0-9-]+)"></math-placeholder>', equation, chapter['html'])
    assert 'math-placeholder' not in body, 'Unresolved equation placeholder'
    headings = [
        {'level': 2, 'id': key, 'title': html.unescape(re.sub('<[^>]+>', '', title))}
        for key, title in re.findall(r'<h2 id="([a-z0-9-]+)">(.*?)<a class="heading-anchor"', body, re.S)
    ]
    assert len(headings) == len(re.findall(r'<h2\b', body)), 'Every section needs a stable anchor'
    anchors[lang] = [item['id'] for item in headings]
    assert len(anchors[lang]) == len(set(anchors[lang]))
    entry = {'title': chapter['title'], 'html': body, 'headings': headings, 'locale': lang,
             'source_url': SOURCE, 'updated_on': data['updated_on']}
    if lang == 'ja':
        # This is a synchronized bilingual expansion; no longer the older translation.
        entry['translation_status'] = 'draft'
    for name in [f'content.{lang}.json'] + (['content.json'] if lang == 'en' else []):
        path = ATLAS / name
        content = json.loads(path.read_text())
        content['keep'] = entry
        path.write_text(json.dumps(content, ensure_ascii=False, indent=2) + '\n')

    path = ATLAS / lang / 'read/keep/index.html'
    text = path.read_text()
    static = body.replace('href="#/', f'href="/numerical-methods-atlas/?lang={lang}#/')
    static = re.sub(r'(src|href)="assets/', r'\1="/numerical-methods-atlas/assets/', static)
    text, count = re.subn(r'(<article class="prose" lang="' + lang + r'">).*?(</article>)',
                         lambda m: m[1] + static + m[2], text, count=1, flags=re.S)
    assert count == 1
    toc = ''.join('<a href="#' + item['id'] + '">' + html.escape(item['title']) + '</a>' for item in headings)
    text, count = re.subn(r'(<aside class="chapter-toc">.*?<nav\b[^>]*>).*?(</nav>)',
                         lambda m: m[1] + toc + m[2], text, count=1, flags=re.S)
    assert count == 1
    text = re.sub(r'(<div class="chapter-topline">.*?<a )href="[^"]+"',
                  lambda m: m[1] + 'href="' + SOURCE + '"', text, count=1, flags=re.S)
    if lang == 'ja':
        text = re.sub(r'<p class="translation-notice[^\"]*">.*?</p>',
                      '<p class="translation-notice">日本語・英語の本文と数式を同時更新：' + data['updated_on'] + '。翻訳は草稿です。</p>',
                      text, count=1, flags=re.S)
    path.write_text(text)
assert anchors['ja'] == anchors['en'], 'Bilingual section anchors must agree'
path = ATLAS / 'translation-status.json'
translations = json.loads(path.read_text())
translations['chapters']['keep'] = {
    'status': 'draft', 'source_url': SOURCE,
    'source_sha256': hashlib.sha256((ROOT / SOURCE.lstrip('/')).read_bytes()).hexdigest(),
    'checked_on': data['updated_on'],
}
path.write_text(json.dumps(translations, ensure_ascii=False, separators=(',', ':')) + '\n')
print('Built bilingual KEEP derivation, dispersion and RK4 explanation:', len(anchors['en']), 'sections,', len(formulas), 'equations.')
