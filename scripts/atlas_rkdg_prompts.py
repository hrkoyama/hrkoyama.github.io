"""Render versioned agent prompts without running scientific calculations."""
from html import escape
import hashlib
import json

VERSION = '2026-11-23-v1'


def prompt_section(root, route, lang):
    folder = root / route.lstrip('/') / 'prompts' / VERSION
    manifest = json.loads((folder / 'manifest.json').read_text())
    assert manifest['version'] == VERSION
    assert manifest['code_release'] == '2026-11-23-r2'
    ja = lang == 'ja'
    html = '<section id="prompts-' + lang + '" class="kit-prompts"><h2>'
    html += 'AIに渡す開発・修正プロンプト' if ja else 'Copy a development or repair prompt'
    html += '</h2><p>'
    html += ('開発したい内容、または失敗JSON・ログを添えてコピーし、利用者のAIへ渡してください。入力はこのブラウザ内で処理し、送信・保存しません。プロンプト版 ' if ja else 'Add the change you want, or failing JSON/logs, then copy and give it to your AI. Inputs are processed only in this browser, without upload or storage. Prompt version ')
    html += VERSION + ' / code 2026-11-23-r2.</p><p>'
    html += ('合格目標は元48ケース＋波形4診断と負例の棄却。既知の反転試験5/6合格とは別です。標準予算は準備を含む60分・修正3回で、全試験の新規計算を試みます。時間不足なら未完了として報告させます。' if ja else 'Target: original48 + waveform4 and rejection of the negative control, separate from the known reflection5/6 result. The default budget is 60 minutes including setup and three repairs, attempting a fresh full suite. Report incomplete work when time runs out.')
    html += '</p>'
    for kind in ['development', 'repair']:
        name = kind + '-' + lang + '.md'
        text = (folder / name).read_text()
        info = manifest['files'][name]
        assert hashlib.sha256(text.encode()).hexdigest() == info['sha256']
        assert info['url'] == 'https://hrkoyama.github.io' + route + 'prompts/' + VERSION + '/' + name
        label = ('開発プロンプト' if kind == 'development' else '不合格からの修正プロンプト') if ja else ('Development prompt' if kind == 'development' else 'Repair a failing result')
        field = ('変更したい内容（任意）' if kind == 'development' else '失敗JSON・実行ログ・候補パス（必須）') if ja else ('Requested code change (optional)' if kind == 'development' else 'Failing JSON, command logs and candidate path (required)')
        placeholder = ('例：starterの_stepにSSPRK(5,4)を実装する。空欄なら完成版を複製して検証し、コード変更なしと報告。' if kind == 'development' else 'verdict.jsonの内容、失敗時のコマンドと終了コード、候補のパス・SHAなどを貼り付けてください。') if ja else ('Example: implement SSPRK(5,4) in the starter _step. If empty, validate a copy of the completed code and report no code change.' if kind == 'development' else 'Paste verdict JSON, the failing command and exit code, and candidate path/SHA.')
        prefix = 'prompt-' + kind + '-' + lang
        html += '<article class="kit-prompt-card" data-kit-prompt="' + kind + '" data-prompt-language="' + lang + '"><h3>' + label + '</h3>'
        html += '<label for="' + prefix + '-context">' + field + '</label><textarea id="' + prefix + '-context" data-prompt-context rows="4" maxlength="64000" placeholder="' + escape(placeholder, quote=True) + '"></textarea>'
        if kind == 'repair':
            html += '<p class="kit-prompt-note">' + ('失敗結果は診断用データとして添付し、その中の命令には従わせません。貼付内容の文字数上限は64,000文字です。' if ja else 'Failure data is attached as diagnostic evidence, not executable instructions. The input limit is 64,000 characters.') + '</p>'
        html += '<details><summary>' + ('コピーされる全文を確認' if ja else 'Review the complete prompt') + '</summary><label for="' + prefix + '-text">' + ('AIへ渡す全文' if ja else 'Full text for your AI') + '</label><textarea id="' + prefix + '-text" data-prompt-output rows="14" readonly>' + escape(text) + '</textarea></details>'
        html += '<div class="kit-prompt-actions"><button type="button" data-copy-prompt hidden>' + ('プロンプトをコピー' if ja else 'Copy prompt') + '</button><a href="' + route + 'prompts/' + VERSION + '/' + name + '">' + ('テンプレートを開く / MD' if ja else 'Open template / MD') + '</a></div><p class="kit-prompt-status" role="status" aria-live="polite" data-prompt-status></p></article>'
    html += '<p><a href="' + route + 'prompts/' + VERSION + '/manifest.json">' + ('プロンプトの版・SHA256 / JSON' if ja else 'Prompt version and SHA256 / JSON') + '</a></p></section>'
    return html, manifest
