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
    text=('流体は複数の問題に実装・検証があります。量子は孤立原子・限定したH₂ RHFと固定Heセルの周期LDAに実装。生物と確率計算は小さな代表例から検証を追加しています。一般分子DFT・他の周期物質、温度制御などの未実装範囲も確認できます。' if ja else
          'Fluid examples cover several problems. Quantum implementations cover isolated atoms, scoped H₂ RHF and fixed-He periodic LDA. Biology and stochastic computation now have small validated examples. See remaining gaps in general molecular DFT, other periodic materials, temperature control and other models.')
    return '<aside class="atlas-depth-teaser"><h2>'+e(data['title'][lang])+'</h2><p>'+text+'</p><p><a href="/numerical-methods-atlas/depth/?lang='+lang+'">'+('解説・コード・実行・参照・収束を分野別に見る' if ja else 'Compare reading, code, execution, references and refinement')+'</a></p></aside>'
