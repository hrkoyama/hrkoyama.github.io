#!/usr/bin/env python3
"""Verify the dedicated FDTD edition and expose its two saved scientific figures."""
import json
from pathlib import Path
import re
import shutil
from atlas_fdtd_release import fdtd_release_record

ROOT = Path(__file__).resolve().parents[1]
method = next(m for m in json.loads((ROOT/'catalog/atlas-methods.json').read_text())['methods']
              if m['id'] == 'fdtd')
record = fdtd_release_record(ROOT, method)
release = ROOT/method['fdtd_release']['base'].lstrip('/')
for case in ['periodic-wave', 'pec-cavity']:
    shutil.copyfile(release/'results'/case/'summary.png',
                    ROOT/'numerical-methods-atlas/assets'/('fdtd-'+case+'.png'))

# Retain the historical roadmap location but describe the implemented subset.
for lang in ['ja', 'en']:
    ja = lang == 'ja'
    replacement = ('<li id="fdtd-verified-scope"><strong>限定実装・検証済み — Yee FDTD</strong>：'
        '2次元TMz・一様真空の周期平面波と長方形PEC空洞を実装。解析解、格子・時間細分化、'
        '数値分散、12周期の離散エネルギー保存を専用コードと固定入力で確認しました。'
        if ja else '<li id="fdtd-verified-scope"><strong>Scoped implementation and validation — Yee FDTD</strong>: '
        '2D TMz vacuum periodic plane waves and a rectangular PEC cavity now have original code, '
        'fixed inputs, analytic comparisons, grid/time refinement, dispersion and twelve-period discrete-energy checks. ')
    replacement += '<a href="/numerical-methods-atlas/'+lang+'/read/fdtd/">'+(
        '日英解説・コード・結果' if ja else 'Reading, code and results')+'</a>。' if ja else '<a href="/numerical-methods-atlas/'+lang+'/read/fdtd/">Reading, code and results</a>. '
    replacement += ('媒質界面の反射・透過と吸収境界/PMLは次の段階です。</li>' if ja else
                    'Interface reflection/transmission and absorbing boundaries/PML remain future work.</li>')
    pattern = r'<li(?: id="fdtd-verified-scope")?><strong>(?:予定 — 電磁場のFDTD|Planned — electromagnetic FDTD|限定実装・検証済み — Yee FDTD|Scoped implementation and validation — Yee FDTD).*?</li>'
    def update(text):
        text, count = re.subn(pattern, lambda m: replacement, text, flags=re.S)
        assert count == 1, 'Expected one FDTD roadmap entry in '+lang
        return text
    content_path = ROOT/'numerical-methods-atlas'/('content.'+lang+'.json')
    documents = json.loads(content_path.read_text())
    documents['roadmap']['html'] = update(documents['roadmap']['html'])
    content_path.write_text(json.dumps(documents, ensure_ascii=False, indent=2)+'\n')
    if lang == 'en':
        (content_path.parent/'content.json').write_text(content_path.read_text())
    static = ROOT/'numerical-methods-atlas'/lang/'read/roadmap/index.html'
    static.write_text(update(static.read_text()))
print('Verified FDTD supplement and copied both saved result figures.')
