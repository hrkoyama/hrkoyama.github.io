"""Validate public bibliographic relationships without reading private scans or OCR."""
import argparse
import json
import re
import subprocess
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from notebook_previews import validate_previews


def read_catalog(text):
    return json.loads(text.split('=', 1)[1].strip().removesuffix(';'))


class Cards(HTMLParser):
    def __init__(self, materials):
        super().__init__()
        self.current = None
        self.cards = {}
        self.materials = materials
        self.images = {}
        self.creators = {}
        self.in_creator = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'article' and 'bibliographic-card' in attrs.get('class', '').split():
            self.current = attrs['id']
            assert self.current not in self.cards, 'Duplicate bibliography anchor'
            self.cards[self.current] = []
            self.images[self.current] = []
            self.creators[self.current] = []
        if self.current:
            assert tag not in {'iframe', 'object', 'embed'}, 'Material body embedded in bibliography'
            if tag == 'img':
                approved = self.materials[self.current]['preview']
                assert approved['image'] and attrs.get('src') == approved['image'], 'Unapproved material image'
                assert 'srcset' not in attrs, 'Alternative image sources are not allowlisted'
                assert attrs.get('width') == str(approved['width']) and attrs.get('height') == str(approved['height'])
                self.images[self.current].append(attrs['src'])
            if tag == 'p' and 'creator' in attrs.get('class','').split():
                assert 'hidden' not in attrs and 'style' not in attrs
                self.in_creator = True
            if tag == 'a':
                self.cards[self.current].append(attrs['href'])

    def handle_endtag(self, tag):
        if tag == 'p':
            self.in_creator = False
        if tag == 'article':
            self.current = None

    def handle_data(self, data):
        if self.current and self.in_creator:
            self.creators[self.current].append(data)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--site-dir', type=Path, default=Path(__file__).resolve().parents[1] / 'notebooks')
    parser.add_argument('--baseline-ref', help='Compare page allowlist and assets with this Git revision')
    args = parser.parse_args()
    site = args.site_dir.resolve()
    links = json.loads((site / 'material-links.json').read_text())
    assert set(links) == {'schema_version', 'updated_on', 'scope', 'relation_labels', 'links'}
    assert set(links['relation_labels']) == {'exercise_solution', 'course_material', 'same_source', 'reference_article', 'reference_book', 'content_correspondence'}
    catalog = read_catalog((site / 'catalog.js').read_text())
    books = {n['id']: n for n in catalog['notebooks']}
    bibliography = json.loads((site / 'bibliography.json').read_text())
    materials = {e['id']: e for e in bibliography['entries']}
    preview_images = validate_previews(site, bibliography['entries'])
    browser_data = (site / 'material-preview-data.js').read_text()
    assert browser_data.startswith('window.NOTEBOOK_MATERIAL_PREVIEWS = ') and browser_data.endswith(';\n')
    browser_data = json.loads(browser_data.split('=',1)[1].strip().removesuffix(';'))
    assert browser_data == {entry['id']:{key:entry[key] for key in ['title','creator','preview']} for entry in bibliography['entries']}
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
    cards = Cards(materials)
    cards.feed((site / 'bibliography.html').read_text())
    assert cards.cards.keys() == materials.keys()
    for material_id, material in materials.items():
        assert set(material) <= {'id','source_ids','title','creator','kind','note','title_status','reference_url','creator_source','related_notebooks','preview','holding_status'}
        expected_image = [material['preview']['image']] if material['preview']['image'] else []
        assert cards.images[material_id] == expected_image, 'Exactly one approved preview image is permitted'
        assert ''.join(cards.creators[material_id]).strip() == (material.get('creator') or '著者・講師名：未確認'), 'Instructor / author name removed'
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
    assert ('n070', 'b071') not in pairs
    # Textual alignment is confirmed independently of the unresolved course identity.
    assert {(l['material_id'], l['relation']) for l in links['links'] if l['notebook_id'] == 'n094'} == {('b092', 'content_correspondence')}
    assert '同一講義は未確認' in links['relation_labels']['content_correspondence']
    assert materials['b092']['creator'] == '中村卓史'
    assert '杉本大一郎' in materials['b092']['note'] and '同一講義かは未確認' in materials['b092']['note']
    assert materials['b099']['creator'] is None, 'A matching course does not establish material authorship'
    assert materials['b076']['kind'] == '記事'
    assert materials['b109']['title'] == '分子雲の収縮・分裂過程'
    assert materials['b109']['creator'] == '犬塚修一郎' and materials['b109']['title_status'] == 'identified'
    assert materials['b109']['preview']['year_label'] is None
    assert materials['b078']['preview']['image'] is None and materials['b078']['creator'] == 'S. I. Blinnikov'
    assert books['n090']['lecture_year_status'] == 'provisional'
    assert books['n063']['lecture_year'] == 1993 and books['n063']['lecture_year_status'] == 'confirmed'
    assert books['n064']['lecture_year'] == 1992 and books['n064']['lecture_year_status'] == 'provisional'
    assert books['n056']['lecturer'] == '九後汰一郎・政池明'
    assert {(n, m) for n, m in pairs if m == 'b014'} == {('n063', 'b014'), ('n074', 'b014')}
    assert books['n074']['lecturer'] is None, 'A confirmed reference-book editor is not a course instructor'
    assert {(n, m) for n, m in pairs if m == 'b009'} == {('n060', 'b009')}
    assert next(l for l in links['links'] if l['id'] == 'n060-b009')['relation'] == 'reference_book'
    assert books['n060']['lecturer'] is None, 'A named reference-book author is not the course instructor'
    assert all(books[n].get('lecture_year') is None for n in ['n062', 'n066', 'n094', 'n104', 'n105']), 'Date/career constraints do not establish a lecture year'
    assert '東京大学大学院で受講' in books['n104']['notes']
    assert '東京大学大学院で受講' in books['n105']['notes']
    assert any(s.get('source') == 'user' and s.get('field') == 'notes'
               and s.get('value') == '東京大学大学院で受講'
               for s in books['n105']['metadata_sources'])
    for note_id in ['n057', 'n067', 'n070']:
        assert '該当書のスキャンを未確認' in books[note_id]['notes'], note_id
    if args.baseline_ref:
        repo = Path(subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], cwd=site, text=True).strip())
        rel = (site / 'catalog.js').relative_to(repo).as_posix()
        baseline = read_catalog(subprocess.check_output(['git', 'show', f'{args.baseline_ref}:{rel}'], cwd=repo, text=True))
        assert {n['id'] for n in baseline['notebooks']} == books.keys()
        for previous in baseline['notebooks']:
            current = books[previous['id']]
            assert previous.get('lecturer') == current.get('lecturer'), 'Notebook instructor changed'
            for field in ['source', 'source_pages', 'pages', 'frames', 'pdf', 'redaction_policy_sha256']:
                assert previous.get(field) == current.get(field), (previous['id'], field, 'Viewing assets or redactions changed')
    print(json.dumps({'notebooks': len(books), 'bibliography_records': len(materials),
                      'approved_preview_images':len(preview_images),'metadata_only':len(materials)-len(preview_images),
                      'confirmed_links': len(pairs), 'linked_notebooks': len({n for n, _ in pairs}),
                      'relations': dict(Counter(l['relation'] for l in links['links'])),
                      'public_page_allowlist_and_redactions_retained': bool(args.baseline_ref)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
