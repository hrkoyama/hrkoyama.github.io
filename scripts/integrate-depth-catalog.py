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
        m=byid[ident]
        m.setdefault('depth_previous_status',m['status']);previous=m['depth_previous_status'];m['status']='educational-example'
        grouped=defaultdict(list)
        for group,case in rows:grouped[group].append(case['id'])
        primary=m.get('depth_release',{}).get('group',rows[0][0])
        assert primary in grouped, 'Never silently replace an existing primary release'
        configs=[{'group':group,'edition':config['edition'],'case_ids':grouped[group]}
                 for group in [primary,*[g for g in grouped if g!=primary]]]
        m['depth_release']=configs[0]
        if len(configs)>1:m['depth_additional_releases']=configs[1:]
        else:m.pop('depth_additional_releases',None)
        def description(key,lang):
            return ' '.join((case['title'][lang]+': ' if len(rows)>1 else '')+case[key][lang] for _,case in rows)
        m['depth_scope']={lang:description('summary',lang) for lang in ['ja','en']}
        if previous!='educational-example':
            m['summary']=m['depth_scope'].copy();m['limitations']={lang:description('limits',lang) for lang in ['ja','en']}
            m['next_deliverable']={'ja':'公開した固定入力の範囲を維持し、拡張時は条件・参照・公差を別に検証する。','en':'Preserve the published fixed-input scope; validate conditions, references and criteria separately for extensions.'}
        if ident in ['langevin-thermostat','stochastic-velocity-rescaling']:
            m['metadata_review']['level']='method-specific primary-source equations and scoped dedicated classical examples; independent ZIP rerun and explicit limits'
        if ident in ['ewald','pme','spme']:
            m['metadata_review']['level']='method-specific source curation plus independently extracted dedicated supplement; fixed inputs, numerical checks and scope verified'
            if ident=='ewald':
                m['method_review']['variant']={'ja':'公開例は中性3D点電荷・立方体・tin-foil境界の直接Ewald和です。実空間・逆空間・自己項を含み、打切り・分割パラメータ、エネルギー有限差分の力と独立theta積分を検査しています。','en':'The released example is direct Ewald summation for neutral 3D point charges in a cubic cell with tin-foil boundaries. It includes real/reciprocal/self terms and checks cutoffs, splitting, energy-difference forces and an independent theta integral.'}
        if m.get('method_review') and previous!='educational-example':
            v=m['method_review']['verification'];v['kind']='source-and-code-inspection'
            v['summary']={'ja':'原典・採用形の整理に加え、新しい専用補助配布版をZIP独立展開し、固定入力と数値判定を実行しました。採用変種と確認範囲は下の専用例・検証記録で確認できます。','en':'In addition to original-source and variant curation, independently extracted the new dedicated supplement ZIP and actually ran its fixed inputs and numerical checks. Dedicated examples and receipts state the adopted variant and scope.'}
            base='https://hrkoyama.github.io/code/validated-examples/'+config['edition']+'/'+rows[0][0]+'/'
            v['evidence']=[{'kind':'fixed-input-results','url':base+'results/result.json','label':'Fixed-input measured checks / 固定入力の実測判定'},{'kind':'independent-extraction-receipt','url':base+'verification.json','label':'Independent ZIP-extraction receipt / ZIP独立展開の記録'}]
            v['not_checked']={lang:[c['limits'][lang] for _,c in rows] for lang in ['ja','en']}
            if ident in ['pme','spme']:
                m['method_review']['variant']={'ja':'今回の実行例はcardinal B-splineによるEssmann型SPMEです。PME族の採用変種として示し、1993年のLagrange補間による原法を実装したとは呼びません。','en':'The executed example adopts Essmann-style SPME with cardinal B-splines. It is a PME-family variant, not an implementation of the original 1993 Lagrange-interpolation form.'}
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
