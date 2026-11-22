"""Shared field-depth introduction, independent of homepage rendering mode."""
import json
import hashlib
from html import escape as e


def depth_assets(root):
    version=hashlib.sha256((root/'styles/atlas-depth.css').read_bytes()).hexdigest()[:12]
    return '<link rel="stylesheet" href="/styles/atlas-depth.css?v='+version+'">'


def depth_teaser(root,lang):
    data=json.loads((root/'catalog/atlas-depth.json').read_text())
    ja=lang=='ja'
    text=('流体は複数の問題に実装・検証があります。量子は孤立原子と限定したH₂のRHFに実装。生物と確率計算は小さな代表例から検証を追加しています。分子DFT・周期系、温度制御などの未実装範囲も確認できます。' if ja else
          'Fluid examples cover several problems. Quantum implementations cover isolated atoms and scoped H₂ RHF. Biology and stochastic computation now have small validated examples. See remaining gaps in molecular/periodic DFT, temperature control and other models.')
    return '<aside class="atlas-depth-teaser"><h2>'+e(data['title'][lang])+'</h2><p>'+text+'</p><p><a href="/numerical-methods-atlas/depth/?lang='+lang+'">'+('解説・コード・実行・参照・収束を分野別に見る' if ja else 'Compare reading, code, execution, references and refinement')+'</a></p></aside>'
