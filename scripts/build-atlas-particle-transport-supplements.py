#!/usr/bin/env python3
"""Attach scoped logarithmic-FMM evidence without rewriting the gravity article.

Only hash-checked saved releases are read. This builder runs no scientific
solver, reference generator or quantum calculation.
"""
from html import escape
from pathlib import Path
import hashlib
import json
import re

from atlas_goal_availability import load_supplemental_examples


ROOT = Path(__file__).resolve().parents[1]
CATALOG = 'catalog/atlas-particle-transport-supplements.json'
START = '<!-- atlas-particle-transport-supplements:start -->'
END = '<!-- atlas-particle-transport-supplements:end -->'
TOC_START = '<!-- atlas-particle-transport-supplements:toc-start -->'
TOC_END = '<!-- atlas-particle-transport-supplements:toc-end -->'


def digest(text):
    return hashlib.sha256(text.encode()).hexdigest()


def dump(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False)+'\n')


def link(url, label):
    assert url.startswith(('/', '#', 'https://'))
    return '<a href="'+escape(url, quote=True)+'">'+escape(label)+'</a>'


def remove_marked(text, start, end):
    """Reject duplicate or malformed overlays before touching article content."""
    assert text.count(start) == text.count(end) and text.count(start) <= 1
    if start not in text:
        return text
    result, count = re.subn(re.escape(start)+'.*?'+re.escape(end), '', text, flags=re.S)
    assert count == 1
    return result


def historical_body(body, config, language, kind):
    body = remove_marked(body, START, END)
    assert digest(body) == config['historical_sha256'][language][kind], 'Historical gravity article changed; review its content before updating a digest'
    return body


def render(config, cases, language):
    ja = language == 'ja'
    body = START+'<section data-particle-transport-supplements><h2 id="'+config['section_id']+'">'+escape(config['title'][language])+'</h2>'
    body += '<p>'+escape(config['intro'][language])+'</p><p>'+escape(config['comparison_note'][language])+'</p>'
    for case in cases:
        body += '<div data-particle-transport-supplement="'+case['id']+'"><h3>'+escape(case['title'][language])+'</h3>'
        body += '<p>'+escape(case['summary'][language])+'</p><p>'+escape(case['limits'][language])+'</p>'
        entries = [link(case['url']+'?lang='+language, '入力・結果・判定' if ja else 'Inputs, results and checks'),
                   link(case['reading'][language], '解説・式・一次文献' if ja else 'Reading, equations and primary sources')]
        entries += [link(url, ('コード：' if ja else 'Code: ')+url.rsplit('/', 1)[-1]) for url in case['code_urls']]
        entries += [link(url, ('テスト：' if ja else 'Tests: ')+url.rsplit('/', 1)[-1]) for url in case['test_urls']]
        entries += [link(case['download'], '配布ZIP' if ja else 'Release ZIP'),
                    link(case['results'], '保存結果' if ja else 'Saved results'),
                    link(case['verification'], '独立展開の追試記録' if ja else 'Independent-extraction receipt')]
        body += '<p>'+' · '.join(entries)+'</p></div>'
    base = '/numerical-methods-atlas/'+language+'/read/'+config['chapter']+'/'
    body += '<p>'+link(base+'supplements.json', '追加検証のJSON' if ja else 'Supplement metadata / JSON')+' · '+link(base+'supplements.md', '追加検証のMarkdown' if ja else 'Supplement metadata / Markdown')+' · '+link('/'+CATALOG, '編集用正本' if ja else 'Editable source')+'</p></section>'+END
    return body


def markdown(config, cases, language):
    ja = language == 'ja'
    lines = ['# '+config['title'][language], '', config['intro'][language], '', config['comparison_note'][language], '']
    for case in cases:
        lines += ['## '+case['title'][language], '', case['summary'][language], '', case['limits'][language], '']
        entries = [(case['url']+'?lang='+language, '入力・結果・判定' if ja else 'Inputs, results and checks'),
                   (case['reading'][language], '解説・式・一次文献' if ja else 'Reading, equations and primary sources')]
        entries += [(url, ('コード：' if ja else 'Code: ')+url.rsplit('/', 1)[-1]) for url in case['code_urls']]
        entries += [(url, ('テスト：' if ja else 'Tests: ')+url.rsplit('/', 1)[-1]) for url in case['test_urls']]
        entries += [(case['download'], '配布ZIP' if ja else 'Release ZIP'), (case['results'], '保存結果' if ja else 'Saved results'), (case['verification'], '独立展開の追試記録' if ja else 'Independent-extraction receipt')]
        lines += ['- ['+label+']('+url+')' for url, label in entries]+['']
    return '\n'.join(lines)


def build(root=ROOT):
    config = json.loads((root/CATALOG).read_text())
    assert config['schema_version'] == 1 and config['chapter'] == 'particle-gravity'
    assert config['supplemental_examples'] == ['fmm', 'fmm-convergence']
    cases = load_supplemental_examples(root, config['supplemental_examples'])
    bindings = json.loads((root/'catalog/atlas-depth-expansion.json').read_text())['case_problem_ids']
    assert {bindings[case['id']] for case in cases} == {'logarithmic-particles'}
    sources = {CATALOG:hashlib.sha256((root/CATALOG).read_bytes()).hexdigest(),
               'catalog/atlas-depth-expansion.json':hashlib.sha256((root/'catalog/atlas-depth-expansion.json').read_bytes()).hexdigest(),
               **{path:value for case in cases for path, value in case['source_sha256'].items()}}
    # Check all historical bodies before writing any output.
    planned = []
    for language in ['ja', 'en']:
        overlay = render(config, cases, language)
        for name in ['content.'+language+'.json']+(['content.json'] if language == 'en' else []):
            path = root/'numerical-methods-atlas'/name
            data = json.loads(path.read_text())
            chapter = data[config['chapter']]
            chapter['html'] = historical_body(chapter['html'], config, language, 'content')+overlay
            chapter['headings'] = [heading for heading in chapter['headings'] if heading['id'] != config['section_id']]
            chapter['headings'].append({'level':2, 'id':config['section_id'], 'title':config['title'][language]})
            planned.append((path, data, True))
        path = root/'numerical-methods-atlas'/language/'read'/config['chapter']/'index.html'
        document = path.read_text()
        article = re.compile(r'(<article class="prose" lang="'+language+r'">)(.*?)(</article>)', re.S)
        document, count = article.subn(lambda match:match[1]+historical_body(match[2], config, language, 'static_article')+overlay+match[3], document)
        assert count == 1
        document = remove_marked(document, TOC_START, TOC_END)
        toc = re.compile(r'(<aside class="chapter-toc">.*?<nav\b[^>]*>)(.*?)(</nav>)', re.S)
        toc_link = TOC_START+link('#'+config['section_id'], config['title'][language])+TOC_END
        document, count = toc.subn(lambda match:match[1]+match[2]+toc_link+match[3], document)
        assert count == 1
        planned.append((path, document, False))
        fields = ['id', 'group', 'title', 'summary', 'limits', 'url', 'reading', 'code_urls', 'test_urls', 'download', 'results', 'verification']
        metadata = {'schema_version':1, 'locale':language, 'chapter':config['chapter'], 'title':config['title'][language],
                    'supplements':[{**{field:case[field] for field in fields}, 'problem_id':bindings[case['id']]} for case in cases],
                    'source_sha256':sources}
        planned.append((path.parent/'supplements.json', metadata, True))
        planned.append((path.parent/'supplements.md', markdown(config, cases, language), False))
    for path, value, structured in planned:
        if structured:
            dump(path, value)
        else:
            path.write_text(value)
    print('Built bilingual logarithmic-FMM supplements; historical gravity article preserved.')


if __name__ == '__main__':
    build()
