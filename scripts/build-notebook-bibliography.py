#!/usr/bin/env python3
"""Build bibliography cards from public metadata; never opens scans or OCR."""
import argparse
import json
import re
from html import escape
from pathlib import Path


def build(directory):
    bibliography = json.loads((directory / 'bibliography.json').read_text())
    relations = json.loads((directory / 'material-links.json').read_text())
    raw = (directory / 'catalog.js').read_text()
    books = {book['id']: book for book in json.loads(raw.split('=', 1)[1].strip().removesuffix(';'))['notebooks']}
    cards = []
    for entry in bibliography['entries']:
        links = entry.get('related_notebooks', [])
        search = ' '.join([entry['id'], entry['title'], entry.get('creator') or '', entry.get('note') or ''] +
                          [books[link['notebook_id']].get('lecturer') or '' for link in links] +
                          [books[link['notebook_id']].get('lecture_title') or books[link['notebook_id']]['display_title'] for link in links] +
                          [link['notebook_id'] for link in links])
        parts = [f'<article id="{escape(entry["id"], quote=True)}" class="bibliographic-card" data-kind="{escape(entry["kind"], quote=True)}" data-search="{escape(search, quote=True)}">',
                 f'<div class="item-top"><span>{escape(entry["kind"])}</span><span>{escape(entry["id"].upper())} · 本文非公開</span></div>',
                 f'<h2>{escape(entry["title"])}</h2><p class="creator">{escape(entry.get("creator") or "著者・講師名：未確認")}</p>']
        if entry.get('note'):
            parts.append(f'<p class="catalogue-note">{escape(entry["note"])}</p>')
        if links:
            parts.append('<div class="related-notebooks"><h3>対応する自筆ノート</h3><ul>')
            for link in links:
                book = books[link['notebook_id']]
                title = book.get('lecture_title') or book['display_title']
                parts.append(f'<li><a href="notebook.html?id={escape(book["id"], quote=True)}">{escape(book["id"].upper()+" · "+title)}</a><span>{escape(relations["relation_labels"][link["relation"]])}</span></li>')
            parts.append('</ul></div>')
        if entry.get('reference_url'):
            parts.append(f'<a href="{escape(entry["reference_url"], quote=True)}" target="_blank" rel="noopener noreferrer">出版社・機関の書誌情報 ↗</a>')
        parts.append('</article>')
        cards.append(''.join(parts))
    path = directory / 'bibliography.html'
    html = path.read_text()
    html, count = re.subn(r'(<div class="bibliography-grid">).*?(</div><p class="zero")',
                          lambda match: match[1] + '\n' + '\n'.join(cards) + match[2], html, count=1, flags=re.S)
    assert count == 1, 'Bibliography card container missing'
    html, count = re.subn(r'(<p\b[^>]*\bid="result-count"[^>]*>)\d+項目(</p>)',
                          lambda match: match[1] + str(len(cards)) + '項目' + match[2], html, count=1)
    assert count == 1, 'Bibliography result count missing'
    path.write_text(html)
    for name in ['index.html', 'notebook.html', 'bibliography.html']:
        path = directory / name
        html = re.sub(r'関連資料 \d+項目の目録', f'関連資料 {len(cards)}項目の目録', path.read_text())
        path.write_text(html)
    print(f'Built {len(cards)} public bibliography cards and notebook backlinks.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--site-dir', type=Path, default=Path(__file__).resolve().parents[1] / 'notebooks')
    build(parser.parse_args().site_dir.resolve())
