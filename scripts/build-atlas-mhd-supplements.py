#!/usr/bin/env python3
"""Attach scoped, verified MHD releases while preserving the historical article.

This renderer reads saved results through the strict release resolver. It runs
no MHD solver or reference generator and does not rewrite an immutable release.
"""
from html import escape
from pathlib import Path
import hashlib
import json
import re

from atlas_goal_availability import load_supplemental_examples
from atlas_reading_presentation import original_reading_document, retain_reading_presentation

ROOT = Path(__file__).resolve().parents[1]
CATALOG = 'catalog/atlas-mhd-supplements.json'
START = '<!-- atlas-mhd-supplements:start -->'
END = '<!-- atlas-mhd-supplements:end -->'
TOC_START = '<!-- atlas-mhd-supplements:toc-start -->'
TOC_END = '<!-- atlas-mhd-supplements:toc-end -->'


def digest(text):
    return hashlib.sha256(text.encode()).hexdigest()


def dump(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False)+'\n')


def link(url, text):
    assert url.startswith(('/', '#', 'https://'))
    return '<a href="'+escape(url, quote=True)+'">'+escape(text)+'</a>'


def remove_marked(text, start, end):
    """Reject malformed/duplicated overlays instead of dropping article text."""
    assert text.count(start) == text.count(end) and text.count(start) <= 1
    if start not in text:
        return text
    pattern = re.escape(start)+'.*?'+re.escape(end)
    result, count = re.subn(pattern, '', text, flags=re.S)
    assert count == 1
    return result


def historical_body(body, config, language, kind):
    body = remove_marked(body, START, END)
    for replacement in config['historical_replacements'][language]:
        old, new = replacement['old'], replacement['new']
        assert body.count(old)+body.count(new) == 1, 'Historical MHD clause changed'
        body = body.replace(new, old)
    assert digest(body) == config['historical_sha256'][language][kind], 'Historical MHD body changed; review before updating its digest'
    return body


def render(config, cases, bindings, language):
    ja = language == 'ja'
    ident = config['section_id']
    body = START+'<section data-mhd-supplements><h2 id="'+ident+'">'+escape(config['title'][language])+'</h2>'
    body += '<p>'+escape(config['intro'][language])+'</p>'
    body += '<p>'+escape(config['comparison_note'][language])+'</p>'
    body += '<p>'+escape(config['cleaning_note'][language])+'</p>'
    for case in cases:
        physical = bindings[case['id']]
        role = ('診断対照・物理問題数へ非加算' if ja else 'Diagnostic control; no additional physical problem') if physical is None else ('固定した物理問題の検証' if ja else 'Validation of a fixed physical problem')
        body += '<div data-mhd-supplement="'+escape(case['id'], quote=True)+'"><h3>'+escape(case['title'][language])+'</h3><p>'+role+'</p>'
        body += '<p>'+escape(case['summary'][language])+'</p><p>'+escape(case['limits'][language])+'</p>'
        links = [link(case['url']+'?lang='+language, '入力・結果・判定' if ja else 'Inputs, results and checks'),
                 link(case['reading'][language], '解説・式・一次文献' if ja else 'Reading, equations and primary sources')]
        links += [link(url, ('コード：' if ja else 'Code: ')+url.rsplit('/', 1)[-1]) for url in case['code_urls']]
        links += [link(url, ('テスト：' if ja else 'Tests: ')+url.rsplit('/', 1)[-1]) for url in case['test_urls']]
        links += [link(case['download'], '配布ZIP' if ja else 'Release ZIP'), link(case['results'], '保存結果' if ja else 'Saved results'), link(case['verification'], '独立展開の追試記録' if ja else 'Independent-extraction receipt')]
        body += '<p>'+' · '.join(links)+'</p></div>'
    body += '<p>'+link('/numerical-methods-atlas/'+language+'/read/mhd/supplements.json', '追加検証のJSON' if ja else 'Supplement metadata / JSON')+' · '+link('/'+CATALOG, '編集用正本' if ja else 'Editable source')+'</p></section>'+END
    return body


def updated_body(body, overlay, config, language, kind):
    base = historical_body(body, config, language, kind)
    for replacement in config['historical_replacements'][language]:
        base = base.replace(replacement['old'], replacement['new'])
    return base+overlay


def build(root=ROOT):
    config = json.loads((root/CATALOG).read_text())
    cases = load_supplemental_examples(root, config['supplemental_examples'])
    bindings = json.loads((root/'catalog/atlas-depth-expansion.json').read_text())['case_problem_ids']
    source_sha256 = {CATALOG:hashlib.sha256((root/CATALOG).read_bytes()).hexdigest(),
                     'catalog/atlas-depth-expansion.json':hashlib.sha256((root/'catalog/atlas-depth-expansion.json').read_bytes()).hexdigest(),
                     **{path:value for case in cases for path, value in case['source_sha256'].items()}}
    for language in ['ja', 'en']:
        overlay = render(config, cases, bindings, language)
        # The SPA and its English compatibility copy retain every other chapter.
        for name in ['content.'+language+'.json']+(['content.json'] if language == 'en' else []):
            path = root/'numerical-methods-atlas'/name
            data = json.loads(path.read_text())
            chapter = data['mhd']
            chapter['html'] = updated_body(chapter['html'], overlay, config, language, 'content')
            chapter['headings'] = [heading for heading in chapter['headings'] if heading['id'] != config['section_id']]
            chapter['headings'].append({'level':2, 'id':config['section_id'], 'title':config['title'][language]})
            dump(path, data)
        page = root/'numerical-methods-atlas'/language/'read/mhd/index.html'
        # Remove the duplicate mobile TOC before globally checking the bounded
        # historical overlay/TOC markers, then restore the same presentation.
        document, opening_first = original_reading_document(page.read_text())
        article = re.compile(r'(<article class="prose" lang="'+language+r'">)(.*?)(</article>)', re.S)
        document, count = article.subn(lambda match:match[1]+updated_body(match[2], overlay, config, language, 'static_article')+match[3], document)
        assert count == 1
        document = remove_marked(document, TOC_START, TOC_END)
        toc = re.compile(r'(<aside class="chapter-toc">.*?<nav\b[^>]*>)(.*?)(</nav>)', re.S)
        toc_link = TOC_START+link('#'+config['section_id'], config['title'][language])+TOC_END
        document, count = toc.subn(lambda match:match[1]+match[2]+toc_link+match[3], document)
        assert count == 1
        document = retain_reading_presentation(document, opening_first)
        page.write_text(document)
        fields = ['id', 'group', 'title', 'summary', 'limits', 'url', 'reading', 'code_urls', 'test_urls', 'download', 'results', 'verification']
        dump(page.parent/'supplements.json', {'schema_version':1, 'locale':language, 'chapter':'mhd', 'title':config['title'][language],
                                            'supplements':[{**{field:case[field] for field in fields}, 'problem_id':bindings[case['id']]} for case in cases],
                                            'source_sha256':source_sha256})
    print('Built bounded bilingual MHD supplements:', len(cases), 'scoped entries; historical article preserved.')


if __name__ == '__main__':
    build()
