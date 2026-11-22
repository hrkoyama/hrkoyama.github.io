"""Static chapter resource navigation, separate from scientific article HTML."""
from html import escape
from urllib.parse import unquote, urljoin, urlsplit


ORIGIN = 'https://hrkoyama.github.io'
GROUPS = ('methods', 'equations', 'figures', 'references', 'code')
LABELS = {
    'methods': {'ja': '手法', 'en': 'Methods'},
    'equations': {'ja': '方程式', 'en': 'Equations'},
    'figures': {'ja': '問題の図', 'en': 'Problem figures'},
    'references': {'ja': '厳密解・参照解', 'en': 'Exact / reference solutions'},
    'code': {'ja': '実行コード', 'en': 'Execution code'},
}


def _language(language):
    if language not in ('ja', 'en'):
        raise ValueError('Unsupported chapter-resource language')
    return language == 'ja'


def _text(value, language):
    text = value.get(language) or value.get('en') or value.get('ja') or '' if isinstance(value, dict) else (value or '')
    if not isinstance(text, str):
        raise ValueError('Invalid chapter-resource text')
    return text


def _url(value):
    if not isinstance(value, str) or not value or any(char.isspace() or char == '\\' for char in value):
        raise ValueError('Missing or invalid chapter-resource URL')
    supplied = urlsplit(value)
    for path in (supplied.path, unquote(supplied.path)):
        if any(part in {'.', '..'} or part.startswith('.') for part in path.split('/') if part):
            raise ValueError('Non-public chapter-resource path')
    parsed = urlsplit(urljoin(ORIGIN + '/', value))
    if parsed.scheme != 'https' or parsed.netloc != 'hrkoyama.github.io' or parsed.username or parsed.password:
        raise ValueError('Chapter resources must use the public same-site origin')
    if not value.startswith(('https://', '/')):
        raise ValueError('Chapter-resource URL must be absolute or site-relative')
    return value


def _link(url, label, attrs=''):
    return '<a href="' + escape(_url(url), quote=True) + '"' + attrs + '>' + escape(label) + '</a>'


def _state(record):
    status = record.get('association_status')
    if status not in {'registered', 'directory-only'}:
        raise ValueError('Unknown chapter-resource association status')
    graph = record['resource_navigation']
    original_groups = graph.get('groups', {})
    if any(not isinstance(original_groups.get(key, []), list) for key in GROUPS):
        raise ValueError('Chapter-resource groups must be lists')
    groups = {key: list(original_groups.get(key, [])) for key in GROUPS}
    groups['code'].sort(key=lambda entry: entry.get('availability') != 'run')
    return status, graph, groups


def _category_label(key, entries, language):
    if key == 'code' and entries and all(entry.get('availability') == 'source' for entry in entries):
        return 'コード・検証' if language == 'ja' else 'Code & checks'
    return LABELS[key][language]


def _scope(entry, key, language):
    ja = language == 'ja'
    notes = []
    relation = entry.get('relation')
    if relation:
        if relation not in {'same-problem', 'related-model'}:
            raise ValueError('Invalid chapter-resource relation')
        if key == 'references':
            label = ('同じ問題の参照' if relation == 'same-problem' else '関連モデルの参照') if ja else ('Same-problem reference' if relation == 'same-problem' else 'Related-model reference')
        else:
            label = ('同じ問題' if relation == 'same-problem' else '関連モデル') if ja else ('Same problem' if relation == 'same-problem' else 'Related model')
        notes.append('<p class="chapter-resource-relation">' + label + '</p>')
    kind = entry.get('reference_kind')
    if kind:
        kinds = {
            'analytic': {'ja': '解析参照', 'en': 'Analytic reference'},
            'semi-analytic': {'ja': '半解析参照', 'en': 'Semi-analytic reference'},
            'manufactured': {'ja': '製造解', 'en': 'Manufactured solution'},
        }
        if kind not in kinds:
            raise ValueError('Unknown chapter-resource reference kind')
        notes.append('<p class="chapter-resource-kind">' + kinds[kind][language] + '</p>')
    if key == 'code' and entry.get('availability') in {'run', 'source'}:
        label = ('固定入力の実行例' if entry['availability'] == 'run' else '関連ソース・検証') if ja else ('Fixed-input execution' if entry['availability'] == 'run' else 'Related source and checks')
        notes.append('<p class="chapter-resource-kind">' + label + '</p>')
    note = _text(entry.get('note'), language)
    if note:
        notes.append('<p class="chapter-resource-note">' + escape(note) + '</p>')
    return ''.join(notes)


def _entry(entry, key, language):
    name = _text(entry.get('name'), language)
    if not name:
        raise ValueError('Missing chapter-resource name')
    return '<li data-chapter-resource-id="' + escape(str(entry.get('id', '')), quote=True) + '"><p class="chapter-resource-name">' + _link(_text(entry['url'], language), name) + '</p>' + _scope(entry, key, language) + '</li>'


def _directory(record, key, language):
    directory = record['directories'][key]
    label = ('全体一覧：' if language == 'ja' else 'Atlas-wide index: ') + _text(directory['name'], language)
    return _link(_text(directory['url'], language), label, ' data-chapter-resource-directory="' + key + '"')


def _preview(groups, language):
    for key in ('figures', 'methods', 'equations', 'references', 'code'):
        for entry in groups.get(key, []):
            image = entry.get('image')
            if not image:
                continue
            if any(isinstance(image.get(axis), bool) or not isinstance(image.get(axis), int) or image[axis] <= 0 for axis in ['width', 'height']):
                raise ValueError('Invalid chapter-resource preview dimensions')
            name, caption = _text(entry['name'], language), _text(image.get('caption'), language)
            target = _url(_text(entry['url'], language))
            image_url = _url(image['url'])
            body = '<figure class="chapter-resource-preview" data-chapter-resource-preview="' + escape(str(entry.get('id', '')), quote=True) + '"><a href="' + escape(target, quote=True) + '"><img src="' + escape(image_url, quote=True) + '" alt="' + escape(caption or name, quote=True) + '" width="' + str(image['width']) + '" height="' + str(image['height']) + '" loading="lazy" decoding="async"></a><figcaption><p class="chapter-resource-name">' + _link(target, name) + '</p>'
            if caption:
                body += '<p class="chapter-resource-note">' + escape(caption) + '</p>'
            body += _scope(entry, key, language)
            body += '<p class="chapter-resource-note">' + ('この保存図の条件と対応範囲は、リンク先と上の注記で確認できます。' if language == 'ja' else 'The linked page and notes above document the saved figure’s conditions and association scope.') + '</p></figcaption></figure>'
            return body
    return ''


def render_chapter_resource_jump(record, language):
    """A short front door; detailed contexts and previews remain at the footer."""
    ja = _language(language)
    status, _, groups = _state(record)
    heading = 'この章からたどる' if ja else 'Explore this chapter'
    if status == 'directory-only':
        heading += ' · ' + ('全体一覧' if ja else 'Atlas-wide indexes')
    body = '<nav class="chapter-resource-jump" data-chapter-resource-jump="' + escape(str(record['id']), quote=True) + '" aria-label="' + heading + '"><p>' + heading + '</p><ul>'
    for key in GROUPS:
        entries = groups.get(key, []) if status == 'registered' else []
        body += '<li><a href="#chapter-resources-' + key + '" data-chapter-resource-jump-category="' + key + '">' + _category_label(key, entries, language) + '</a></li>'
    return body + '</ul></nav>'


def render_chapter_resources(record, language):
    """Render all five destinations outside the immutable scientific article."""
    ja = _language(language)
    status, graph, groups = _state(record)
    body = '<section class="chapter-resource-navigation search-navigation" id="chapter-resources" data-chapter-resources="' + escape(str(record['id']), quote=True) + '" data-chapter-association-status="' + status + '"><h2>' + ('この章からたどる' if ja else 'Explore this chapter') + '</h2>'
    if status == 'directory-only':
        body += '<p class="chapter-resource-intro">' + ('この章に専用の手法・問題・実行例の対応付けは未登録です。以下はアトラス全体の一覧への入口です。' if ja else 'No chapter-specific method, problem or execution association is registered. The links below open atlas-wide indexes.') + '</p>'
    else:
        note = _text(graph.get('note'), language)
        if note:
            body += '<p class="chapter-resource-intro">' + escape(note) + '</p>'
    body += '<div class="chapter-resource-grid">'
    for key in GROUPS:
        entries = groups.get(key, []) if status == 'registered' else []
        body += '<section class="chapter-resource-category" id="chapter-resources-' + key + '" data-chapter-resource-group="' + key + '"><h3>' + _category_label(key, entries, language) + '</h3>'
        if entries:
            body += '<ul class="chapter-resource-list">' + ''.join(_entry(entry, key, language) for entry in entries[:3]) + '</ul>'
            if len(entries) > 3:
                count = len(entries) - 3
                summary = '残り' + str(count) + '件を表示' if ja else 'Show ' + str(count) + ' more'
                body += '<details class="chapter-resource-more"><summary>' + summary + '</summary><ul class="chapter-resource-list">' + ''.join(_entry(entry, key, language) for entry in entries[3:]) + '</ul></details>'
        else:
            if status == 'registered':
                body += '<p class="chapter-resource-note">' + ('この章に専用の対応付けは未登録です。' if ja else 'No chapter-specific association is registered.') + '</p>'
            body += '<p class="chapter-resource-directory">' + _directory(record, key, language) + '</p>'
        body += '</section>'
    body += '</div>'
    if status == 'registered':
        body += _preview(groups, language)
    return body + '</section>'
