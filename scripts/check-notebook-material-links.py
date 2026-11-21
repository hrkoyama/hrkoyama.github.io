"""Validate public bibliographic relationships without reading private scans or OCR."""
import argparse
import json
import re
import subprocess
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path


def read_catalog(text):
    return json.loads(text.split('=', 1)[1].strip().removesuffix(';'))


class Cards(HTMLParser):
    def __init__(self):
        super().__init__()
        self.current = None
        self.cards = {}

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'article' and 'bibliographic-card' in attrs.get('class', '').split():
            self.current = attrs['id']
            assert self.current not in self.cards, 'Duplicate bibliography anchor'
            self.cards[self.current] = []
        if self.current:
            assert tag not in {'img', 'iframe', 'object', 'embed'}, 'Material body embedded in bibliography'
            if tag == 'a':
                self.cards[self.current].append(attrs['href'])

    def handle_endtag(self, tag):
        if tag == 'article':
            self.current = None


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--site-dir', type=Path, default=Path(__file__).resolve().parents[1] / 'notebooks')
    parser.add_argument('--baseline-ref', help='Compare page allowlist and assets with this Git revision')
    args = parser.parse_args()
    site = args.site_dir.resolve()
    links = json.loads((site / 'material-links.json').read_text())
    assert set(links) == {'schema_version', 'updated_on', 'scope', 'relation_labels', 'links'}
    assert set(links['relation_labels']) == {'exercise_solution', 'course_material', 'same_source', 'reference_article'}
    catalog = read_catalog((site / 'catalog.js').read_text())
    books = {n['id']: n for n in catalog['notebooks']}
    bibliography = json.loads((site / 'bibliography.json').read_text())
    materials = {e['id']: e for e in bibliography['entries']}
    assert len(books) == len(catalog['notebooks']) == 41
    assert len(materials) == len(bibliography['entries'])
    assert not ({'n082', 'n086'} & books.keys())
    assert sum(len(n['frames']) for n in books.values()) == 1170
    pairs = set()
    for link in links['links']:
        # Explicitly disallow private evidence, page images, OCR and storage paths.
        assert set(link) == {'id', 'notebook_id', 'material_id', 'relation', 'status', 'confirmed_on'}
        assert link['status'] == 'confirmed'
        assert link['relation'] in links['relation_labels']
        assert re.fullmatch(r'\d{4}-\d{2}-\d{2}', link['confirmed_on'])
        note_id, material_id = link['notebook_id'], link['material_id']
        assert note_id in books and material_id in materials
        assert link['id'] == f'{note_id}-{material_id}'
        assert (note_id, material_id) not in pairs
        pairs.add((note_id, material_id))
    for note_id, book in books.items():
        expected = {(l['material_id'], l['relation']) for l in links['links'] if l['notebook_id'] == note_id}
        actual = {(m['id'], m['relation']) for m in book.get('related_materials', [])}
        assert actual == expected and len(actual) == len(book.get('related_materials', [])), note_id
        for material in book.get('related_materials', []):
            assert set(material) == {'id', 'title', 'creator', 'relation', 'label'}
            source = materials[material['id']]
            assert material['title'] == source['title'] and material['creator'] == source['creator']
            assert material['label'] == links['relation_labels'][material['relation']]
    cards = Cards()
    cards.feed((site / 'bibliography.html').read_text())
    assert cards.cards.keys() == materials.keys()
    for material_id, material in materials.items():
        assert set(material) <= {'id','source_ids','title','creator','kind','note','title_status','reference_url','creator_source','related_notebooks'}
        assert all(re.fullmatch(r'n[0-9]{3}|hdd-inutsuka', source_id) for source_id in material.get('source_ids', []))
        assert len(material['title']) <= 300 and len(material.get('note', '')) <= 1000
        expected = {(l['notebook_id'], l['relation']) for l in links['links'] if l['material_id'] == material_id}
        actual = {(l['notebook_id'], l['relation']) for l in material.get('related_notebooks', [])}
        assert actual == expected, material_id
        urls = cards.cards[material_id]
        expected_urls = {f'notebook.html?id={note_id}' for note_id, _ in expected}
        assert {u for u in urls if u.startswith('notebook.html?')} == expected_urls
        assert all(u in expected_urls or u == material.get('reference_url') for u in urls)
    # Preserve owner-confirmed names when the private packet has a different instructor.
    assert books['n094']['lecturer'] == '杉本大一郎'
    assert books['n070']['lecturer'] == '佐藤文隆'
    assert not ({('n094', 'b092'), ('n070', 'b071')} & pairs)
    assert materials['b099']['creator'] is None, 'A matching course does not establish material authorship'
    assert materials['b076']['kind'] == '記事'
    assert books['n090']['lecture_year_status'] == 'provisional'
    if args.baseline_ref:
        repo = Path(subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], cwd=site, text=True).strip())
        rel = (site / 'catalog.js').relative_to(repo).as_posix()
        baseline = read_catalog(subprocess.check_output(['git', 'show', f'{args.baseline_ref}:{rel}'], cwd=repo, text=True))
        assert {n['id'] for n in baseline['notebooks']} == books.keys()
        for previous in baseline['notebooks']:
            current = books[previous['id']]
            for field in ['source', 'source_pages', 'pages', 'frames', 'pdf', 'redaction_policy_sha256']:
                assert previous.get(field) == current.get(field), (previous['id'], field, 'Viewing assets or redactions changed')
    print(json.dumps({'notebooks': len(books), 'bibliography_records': len(materials),
                      'confirmed_links': len(pairs), 'linked_notebooks': len({n for n, _ in pairs}),
                      'relations': dict(Counter(l['relation'] for l in links['links'])),
                      'public_page_allowlist_and_redactions_retained': bool(args.baseline_ref)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
