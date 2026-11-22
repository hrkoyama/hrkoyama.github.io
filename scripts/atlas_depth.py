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
    count=len(json.loads((root/'catalog/atlas-depth-expansion.json').read_text())['case_problem_ids'])
    text=(f'共通22実行例を保持し、基盤・生物の非線形反応拡散・MCMC・Langevin／CSVR比較・粒子輸送・流体MHDの{count}補助例を接続。量子は孤立原子・限定H₂ RHF・小さなHeセルの範囲です。各例の分布・相関・独立参照・空間/時間収束と、完全HHや他の温度制御など残る差を確認できます。' if ja else
          f'Preserve 22 shared execution examples and explore {count} separate supplements in foundations, nonlinear biological reaction–diffusion, MCMC, Langevin/CSVR comparisons, particle transport and fluid/MHD. Quantum coverage remains scoped to atoms, H₂ RHF and small He cells. Compare distributions, correlations, independent references, space/time refinement and remaining gaps, including full HH and other thermostats.')
    return '<aside class="atlas-depth-teaser"><h2>'+e(data['title'][lang])+'</h2><p>'+text+'</p><p><a href="/numerical-methods-atlas/depth/?lang='+lang+'">'+('解説・コード・実行・参照・収束を分野別に見る' if ja else 'Compare reading, code, execution, references and refinement')+'</a></p></aside>'
