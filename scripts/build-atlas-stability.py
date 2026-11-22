#!/usr/bin/env python3
"""Publish the bilingual stability foundations from editable prose and LaTeX.

Static reading pages and SPA documents use the same source. This documentation
build neither changes nor reruns the dated scientific-code distributions.
"""
import hashlib
import html
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
ATLAS = ROOT / 'numerical-methods-atlas'
SOURCE = '/catalog/atlas-stability-foundations.json'
source = ROOT / SOURCE.lstrip('/')
data = json.loads(source.read_text())
rendered = json.loads(subprocess.check_output(
    ['node', 'scripts/render-atlas-math.cjs'], cwd=ROOT,
    input=json.dumps([{'id': key, 'formula': [tex]} for key, tex in data['formulas'].items()]).encode(),
))['rendered']
documents = {lang: json.loads((ATLAS / f'content.{lang}.json').read_text()) for lang in ['ja', 'en']}
translations = json.loads((ATLAS / 'translation-status.json').read_text())
wave_enabled = any('data-wave-evolution' in item['html'] for item in data['chapters']['stability'].values())
if wave_enabled:
    wave_versions = {suffix: hashlib.sha256((ATLAS / ('wave-evolution.' + suffix)).read_bytes()).hexdigest()[:12]
                     for suffix in ['js', 'css']}

def wave_assets(text, module=False):
    """Version the small, chapter-scoped player without changing shared chrome."""
    text = re.sub(r'<!-- wave-evolution-assets -->.*?<!-- /wave-evolution-assets -->\n?', '', text, flags=re.S)
    block = '<!-- wave-evolution-assets --><link rel="stylesheet" href="/numerical-methods-atlas/wave-evolution.css?v=' + wave_versions['css'] + '">'
    if module:
        block += '<script type="module" src="/numerical-methods-atlas/wave-evolution.js?v=' + wave_versions['js'] + '"></script>'
    return text.replace('</head>', block + '<!-- /wave-evolution-assets -->\n</head>', 1)
for chapter, localized in data['chapters'].items():
    anchors = {}
    for lang in ['ja', 'en']:
        item = localized[lang]
        body = re.sub(r'<math-placeholder id="([a-z0-9-]+)"></math-placeholder>',
                      lambda m: '<div class="math-block">' + rendered[m[1]][0] + '</div>', item['html'])
        assert 'math-placeholder' not in body
        headings = [
            {'level': 2, 'id': ident, 'title': html.unescape(re.sub('<[^>]+>', '', title))}
            for ident, title in re.findall(r'<h2 id="([a-z0-9-]+)">(.*?)<a class="heading-anchor"', body, re.S)
        ]
        assert len(headings) == len(re.findall(r'<h2\b', body))
        anchors[lang] = [h['id'] for h in headings]
        assert len(anchors[lang]) == len(set(anchors[lang]))
        entry = {'title': item['title'], 'html': body, 'headings': headings, 'locale': lang,
                 'source_url': SOURCE, 'updated_on': data['updated_on']}
        if lang == 'ja':
            entry['translation_status'] = 'draft'
        documents[lang][chapter] = entry

        path = ATLAS / lang / 'read' / chapter / 'index.html'
        text = path.read_text()
        static = body.replace('href="#/', f'href="/numerical-methods-atlas/?lang={lang}#/')
        static = re.sub(r'(src|href)="assets/', r'\1="/numerical-methods-atlas/assets/', static)
        text, count = re.subn(r'(<article class="prose" lang="' + lang + r'">).*?(</article>)',
                             lambda m: m[1] + static + m[2], text, count=1, flags=re.S)
        assert count == 1
        toc = ''.join('<a href="#' + h['id'] + '">' + html.escape(h['title']) + '</a>' for h in headings)
        text, count = re.subn(r'(<aside class="chapter-toc">.*?<nav\b[^>]*>).*?(</nav>)',
                             lambda m: m[1] + toc + m[2], text, count=1, flags=re.S)
        assert count == 1
        text = re.sub(r'(<div class="chapter-topline">.*?<a )href="[^"]+"',
                      lambda m: m[1] + 'href="' + SOURCE + '"', text, count=1, flags=re.S)
        if lang == 'ja':
            text = re.sub(r'<p class="translation-notice[^\"]*">.*?</p>',
                          '<p class="translation-notice">日本語・英語の本文と数式を同時更新：' + data['updated_on'] + '。翻訳は草稿です。</p>',
                          text, count=1, flags=re.S)
        if chapter == 'stability' and wave_enabled:
            text = wave_assets(text, module=True)
        path.write_text(text)
    assert anchors['ja'] == anchors['en'], chapter + ': bilingual anchors differ'
    translations['chapters'][chapter] = {
        'status': 'draft', 'source_url': SOURCE,
        'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(), 'checked_on': data['updated_on'],
    }
for lang, content in documents.items():
    for name in [f'content.{lang}.json'] + (['content.json'] if lang == 'en' else []):
        (ATLAS / name).write_text(json.dumps(content, ensure_ascii=False, indent=2) + '\n')
(ATLAS / 'translation-status.json').write_text(json.dumps(translations, ensure_ascii=False, separators=(',', ':')) + '\n')
if wave_enabled:
    path = ATLAS / 'index.html'
    path.write_text(wave_assets(path.read_text()))
    path = ATLAS / 'app.js'
    text, count = re.subn(r"from './wave-evolution[.]js(?:[?]v=[a-f0-9]+)?'",
                          "from './wave-evolution.js?v=" + wave_versions['js'] + "'", path.read_text())
    assert count == 1, 'The SPA must initialize the waveform player after rendering'
    path.write_text(text)
print('Built bilingual stability foundations:', len(data['chapters']), 'chapters,', len(data['formulas']), 'equations.')
