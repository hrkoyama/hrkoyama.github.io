#!/usr/bin/env python3
"""Attach only actually verified small supplements to existing method records."""
from pathlib import Path
from collections import defaultdict
import json,re,unicodedata
from atlas_depth_release import load_depth_group
ROOT=Path(__file__).resolve().parents[1]
def read(p):return json.loads(p.read_text())
def write(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
def doi(r):return re.sub(r'^https?://(?:dx\.)?doi.org/','',(r.get('doi') or '').strip(),flags=re.I).lower()
def title(r):return (''.join(c for c in unicodedata.normalize('NFKC',r['title']).lower() if c.isalnum()),int(r['year']))
def main():
    config=read(ROOT/'catalog/atlas-depth-expansion.json');catalog=read(ROOT/'catalog/atlas-methods.json');byid={m['id']:m for m in catalog['methods']};bindings=defaultdict(list);refs=[]
    for group in config['groups']:
        data=load_depth_group(ROOT,group['id'],group.get('edition',config['edition']))
        for c in data['metadata']:
            for method in c['method_ids']:
                assert method in byid,(c['id'],method)
                bindings[method].append((group['id'],c))
            refs.extend(c['references'])
    for ident,rows in bindings.items():
        m=byid[ident];groups={g for g,c in rows};assert len(groups)==1
        m.setdefault('depth_previous_status',m['status']);previous=m['depth_previous_status'];m['status']='educational-example'
        m['depth_release']={'group':rows[0][0],'edition':config['edition'],'case_ids':[c['id'] for _,c in rows]}
        m['depth_scope']={lang:' '.join(c['summary'][lang] for _,c in rows) for lang in ['ja','en']}
        if previous!='educational-example':
            m['summary']=m['depth_scope'].copy();m['limitations']={lang:' '.join(c['limits'][lang] for _,c in rows) for lang in ['ja','en']}
            m['next_deliverable']={'ja':'公開した固定入力の範囲を維持し、拡張時は条件・参照・公差を別に検証する。','en':'Preserve the published fixed-input scope; validate conditions, references and criteria separately for extensions.'}
        if m.get('method_review') and previous!='educational-example':
            v=m['method_review']['verification'];v['kind']='source-and-code-inspection'
            v['summary']={'ja':'原典・採用形の整理に加え、新しい専用補助配布版をZIP独立展開し、固定入力と数値判定を実行しました。採用変種と確認範囲は下の専用例・検証記録で確認できます。','en':'In addition to original-source and variant curation, independently extracted the new dedicated supplement ZIP and actually ran its fixed inputs and numerical checks. Dedicated examples and receipts state the adopted variant and scope.'}
            base='https://hrkoyama.github.io/code/validated-examples/'+config['edition']+'/'+rows[0][0]+'/'
            v['evidence']=[{'kind':'fixed-input-results','url':base+'results/result.json','label':'Fixed-input measured checks / 固定入力の実測判定'},{'kind':'independent-extraction-receipt','url':base+'verification.json','label':'Independent ZIP-extraction receipt / ZIP独立展開の記録'}]
            v['not_checked']={lang:[c['limits'][lang] for _,c in rows] for lang in ['ja','en']}
            if ident in ['pme','spme']:
                m['method_review']['variant']={'ja':'今回の実行例はcardinal B-splineによるEssmann型SPMEです。PME族の採用変種として示し、1993年のLagrange補間による原法を実装したとは呼びません。','en':'The executed example adopts Essmann-style SPME with cardinal B-splines. It is a PME-family variant, not an implementation of the original1993 Lagrange-interpolation form.'}
    write(ROOT/'catalog/atlas-methods.json',catalog)
    source=read(ROOT/'catalog/atlas-method-primary-references.json');existing=source['references']+read(ROOT/'numerical-methods-atlas/references.json');added=0
    for r in refs:
        matches=[p for p in existing if (doi(r) and doi(r)==doi(p)) or title(r)==title(p)]
        if matches:continue
        if any(p['id']==r['id'] for p in existing):raise ValueError('Reference ID collision: '+r['id'])
        x={**r,'source':r['url'],'type':('misc' if r.get('type')=='documentation' else r.get('type','article' if doi(r) else 'misc'))}
        if not x.get('doi'):x.pop('doi',None)
        source['references'].append(x);existing.append(x);added+=1
    write(ROOT/'catalog/atlas-method-primary-references.json',source)
    print('Attached',len(bindings),'method records; added',added,'deduplicated references.')
if __name__=='__main__':main()
