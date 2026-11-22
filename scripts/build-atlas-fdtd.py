#!/usr/bin/env python3
"""Verify the dedicated FDTD edition and expose its saved scientific figures."""
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
for case in record['cases']:
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
    if 'p-polarization' in record['cases']:
        replacement += ('従来のs偏光界面・PMLに加え、光学のp偏光に対応するTEzの固定例を追加しました。'
                        'Brewster角の単色係数と有限帯域波束の反射率、全反射時のエバネッセント場と正味法線流束を区別し、'
                        'Fresnel解析解、エネルギー収支、格子収束を確認します。選定した無損失・非磁性の条件に範囲を限定します。</li>' if ja else
                        'The retained s-polarized interface and PML examples are joined by selected TEz cases for optical p polarization. '
                        'Monochromatic Brewster coefficients are distinguished from finite-band packet reflectance, and evanescent fields '
                        'under total internal reflection from net normal energy flux. Fresnel fields, energy budgets and refinement are '
                        'checked for the specified lossless, nonmagnetic cases.</li>')
    elif 'dielectric-oblique' in record['cases']:
        replacement += ('従来の媒質界面・四辺と角のPMLに加え、無損失誘電体界面への斜め入射を検証しました。'
                        '光学のs偏光に相当するTMzの有限帯域波束で、Fresnel解析解、反射・透過エネルギー、'
                        '独立したエネルギー・流束収支と格子収束を確認します。検証した条件と一般媒質・他偏光・3次元の範囲を区別します。</li>' if ja else
                        'Alongside the retained interface and four-side/corner PML cases, an oblique lossless-dielectric '
                        'interface packet is checked against s-polarized Fresnel solutions. Reflected/transmitted packet '
                        'energies, independent energy/flux balances and grid refinement are distinct checks. The reading '
                        'separates tested conditions from general matter, other polarization and three-dimensional cases.</li>')
    elif 'pml-corners' in record['cases']:
        replacement += ('媒質界面・左右x方向PMLに続き、四辺・角部を含む2次元PMLの固定入力例を追加しました。'
                        '反射誤差、独立したエネルギー・仕事・流束収支、格子細分化を別々に確認します。'
                        '実行した入射方向・時間窓と未検証の一般媒質・3次元は同じ章で区別します。</li>' if ja else
                        'Following the dielectric-interface and x-directed strip cases, a separate fixed input exercises '
                        'two-dimensional PML on all four sides and in corners. Reflection error, independent '
                        'energy/work/flux balances and grid refinement are checked separately. The reading distinguishes '
                        'tested directions and time windows from unvalidated general media and three-dimensional cases.</li>')
    elif 'dielectric-interface' in record['cases'] and 'pml-pulse' in record['cases']:
        replacement += ('媒質界面の反射・透過とPMLの固定入力例も、解析解・反射誤差・エネルギー収支・格子収束を別に確認しました。'
                        '検証した入射・境界の範囲と、未検証のPML角部・一般媒質は同じ章で区別します。</li>' if ja else
                        'Separate fixed-input dielectric-interface and PML examples check analytic references, reflection error, '
                        'energy balance and grid refinement. The reading distinguishes tested incidence and boundaries '
                        'from unvalidated PML corners and general media.</li>')
    else:
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
print('Verified FDTD supplement and copied',len(record['cases']),'saved result figures.')
