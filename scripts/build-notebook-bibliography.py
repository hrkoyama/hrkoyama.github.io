#!/usr/bin/env python3
"""Build bibliography cards from public metadata; never opens scans or OCR."""
import argparse
import hashlib
import json
import re
from html import escape
from pathlib import Path


def localized(tag, value, class_name=''):
    style = f' class="{class_name}"' if class_name else ''
    return f'<{tag}{style} data-ui-ja="{escape(value["ja"], quote=True)}" data-ui-en="{escape(value["en"], quote=True)}">{escape(value["ja"])}</{tag}>'


def preview_markup(entry):
    preview = entry['preview']
    content = localized('span', preview['label'], 'material-preview-label')
    content += localized('p', preview['caption'], 'material-preview-caption')
    if preview.get('year_label'):
        content += localized('p', preview['year_label'], 'material-preview-date')
    if not preview['image']:
        return '<div class="material-preview-empty"><div class="material-preview-description">' + content + '</div></div>'
    variant = 'cover' if preview['mode'] == 'cover' else 'title'
    return (f'<figure class="material-preview material-preview-{variant}">'
            f'<button type="button" class="material-preview-button" data-material-preview="{escape(entry["id"], quote=True)}" aria-label="{escape(entry["title"]+"の表紙・表題画像を拡大", quote=True)}">'
            f'<img src="{escape(preview["image"], quote=True)}" alt="{escape(preview["alt"]["ja"], quote=True)}" width="{preview["width"]}" height="{preview["height"]}" loading="lazy">'
            + localized('span', {'ja':'画像を拡大','en':'Enlarge preview'}, 'material-preview-action')
            + '</button><figcaption class="material-preview-description">' + content + '</figcaption></figure>')


def version(directory, name):
    return name + '?v=' + hashlib.sha256((directory / name).read_bytes()).hexdigest()[:12]


def preview_assets(directory, html, notebook=False):
    html = re.sub(r'<!-- material-previews -->.*?<!-- /material-previews -->\s*', '', html, flags=re.S)
    block = ('<!-- material-previews -->\n'
             f'<link rel="stylesheet" href="{version(directory, "material-previews.css")}">\n'
             f'<script src="{version(directory, "material-preview-data.js")}" defer></script>\n'
             f'<script src="{version(directory, "material-previews.js")}" defer></script>\n')
    if not notebook:
        block += f'<script src="{version(directory, "bibliography.js")}" defer></script>\n'
    block += '<!-- /material-previews -->\n'
    if notebook:
        html, count = re.subn(r'<script src="notebook\.js(?:\?v=[^"]+)?" defer></script>', lambda m: block + m[0], html, count=1)
        assert count == 1
    else:
        html = html.replace('</head>', block + '</head>', 1)
    return html


def build(directory):
    bibliography = json.loads((directory / 'bibliography.json').read_text())
    relations = json.loads((directory / 'material-links.json').read_text())
    raw = (directory / 'catalog.js').read_text()
    books = {book['id']: book for book in json.loads(raw.split('=', 1)[1].strip().removesuffix(';'))['notebooks']}
    # This generated browser payload contains public metadata only. Scans, OCR,
    # private review ledgers and source locations are never inputs to this tool.
    preview_data = {entry['id']: {key: entry[key] for key in ['title', 'creator', 'preview']} for entry in bibliography['entries']}
    (directory / 'material-preview-data.js').write_text('window.NOTEBOOK_MATERIAL_PREVIEWS = ' + json.dumps(preview_data, ensure_ascii=False, indent=2) + ';\n')
    cards = []
    for entry in bibliography['entries']:
        links = entry.get('related_notebooks', [])
        search = ' '.join([entry['id'], entry['title'], entry.get('creator') or '', entry.get('note') or ''] +
                          [books[link['notebook_id']].get('lecturer') or '' for link in links] +
                          [books[link['notebook_id']].get('lecture_title') or books[link['notebook_id']]['display_title'] for link in links] +
                          [link['notebook_id'] for link in links])
        availability = 'image' if entry['preview']['image'] else 'metadata'
        parts = [f'<article id="{escape(entry["id"], quote=True)}" class="bibliographic-card" data-kind="{escape(entry["kind"], quote=True)}" data-preview="{availability}" data-search="{escape(search, quote=True)}">',
                 f'<div class="item-top"><span>{escape(entry["kind"])}</span><span>{escape(entry["id"].upper())} · 本文非公開</span></div>',
                 f'<h2>{escape(entry["title"])}</h2><p class="creator">{escape(entry.get("creator") or "著者・講師名：未確認")}</p>']
        parts.append(preview_markup(entry))
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
        summary = {'ja':f'関連資料{len(cards)}件。確認済みの表紙・表題画像と書誌情報を紹介しています。資料の本文・問題・原本PDFは非公開です。',
                   'en':f'{len(cards)} related material records, with reviewed cover / title previews and bibliographic information. Document bodies, questions and full original PDFs remain private.'}
        html = re.sub(r'<p data-material-summary\b[^>]*>.*?</p>', lambda m: localized('p', summary).replace('<p ', '<p data-material-summary ', 1), html, flags=re.S)
        if name in ['notebook.html', 'bibliography.html']:
            html = preview_assets(directory, html, notebook=name == 'notebook.html')
        for script in ['library.js', 'notebook.js']:
            html = re.sub(rf'{re.escape(script)}(?:\?v=[^"\s]+)?', lambda m: version(directory, script), html)
        path.write_text(html)
    print(f'Built {len(cards)} public bibliography cards and notebook backlinks.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--site-dir', type=Path, default=Path(__file__).resolve().parents[1] / 'notebooks')
    build(parser.parse_args().site_dir.resolve())
