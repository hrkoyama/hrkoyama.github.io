#!/usr/bin/env python3
"""Render CI discovery separately from saved Linux verification snapshots.

No network or scientific code is executed. A saved success is validated against
its report, and its relationship to the current public registry is explicit.
"""
from collections import defaultdict
from datetime import datetime,timezone,timedelta
import hashlib
import html
import importlib.util
import json
from pathlib import Path
import re
from urllib.parse import urlparse,unquote

ROOT=Path(__file__).resolve().parents[1]
ORIGIN='https://hrkoyama.github.io'
ROUTE='/numerical-methods-atlas/code-and-data/ci/'
CATALOG='catalog/atlas-ci.json'
REGISTRY='numerical-methods-atlas/code-and-data/examples.json'


def encode(value):return json.dumps(value,ensure_ascii=False,indent=2,allow_nan=False)+'\n'
def digest(value):return hashlib.sha256(value).hexdigest()
def esc(value):return html.escape(str(value),quote=True)
def link(url,label):return '<a href="'+esc(url)+'">'+esc(label)+'</a>'
def paragraph(text,cls=''):return '<p'+(' class="'+cls+'"' if cls else '')+'>'+esc(text)+'</p>'


def sha_field(value):
    if not isinstance(value,str) or not re.fullmatch('[0-9a-f]{64}',value):raise ValueError('Invalid registry SHA-256')


def snapshot_path(url,root):
    parsed=urlparse(url)
    prefix=ROUTE+'verification/'
    decoded=unquote(parsed.path);parts=decoded.split('/')
    if parsed.scheme!='https' or parsed.netloc!='hrkoyama.github.io' or parsed.query or parsed.fragment or not decoded.startswith(prefix) or any(part in ['.','..'] for part in parts) or '\\' in decoded:
        raise ValueError('A snapshot must be a canonical public file under ci/verification/')
    path=root/decoded.lstrip('/')
    if path.suffix!='.json':raise ValueError('A snapshot must be JSON')
    return path


def github_run(url,repository,run_id,artifact=False):
    parsed=urlparse(url)
    prefix='/'+repository+'/actions/runs/'+str(run_id)
    if parsed.scheme!='https' or parsed.netloc!='github.com' or not (parsed.path==prefix or parsed.path.startswith(prefix+'/')):
        raise ValueError('Snapshot run/artifact link must belong to the recorded repository run')
    if not artifact and not re.fullmatch(re.escape(prefix)+r'(?:/attempts/[1-9][0-9]*)?',parsed.path):
        raise ValueError('Invalid workflow run URL')


def check_observed(module,actual,spec):
    if actual.get('passed') is not True:raise ValueError('A saved successful snapshot contains a failed check')
    for key in ['pointer','comparison','expected','tolerance','where','field']:
        if actual.get(key)!=spec.get(key):raise ValueError('Snapshot criterion differs from its registry')
    if 'observed' not in actual:raise ValueError('Missing observed numerical/check value')
    selected={k:v for k,v in spec.items() if k not in ['where','field','description']}
    selected['pointer']='/value'
    if not module.evaluate_check({'value':actual['observed']},selected)['passed']:
        raise ValueError('Saved observed value does not satisfy its criterion')


def validate_snapshot(url,envelope,registry,registry_sha,config,module):
    if type(envelope.get('schema_version')) is not int or envelope['schema_version']!=1:raise ValueError('Unsupported CI snapshot envelope')
    ci=envelope['ci'];report=envelope['verification']
    if any(ci.get(key) is not True for key in ['setup_passed','scientific_passed','passed']):raise ValueError('Only a fully successful CI run can be a saved success')
    if ci.get('error') not in [None,'']:raise ValueError('A successful CI snapshot cannot contain an error')
    if report.get('schema_version')!=1 or report.get('passed') is not True:raise ValueError('Missing successful verification report')
    if report.get('registry_source_mode')!='public-registry' or report.get('registry_url')!=ORIGIN+'/'+REGISTRY:
        raise ValueError('CI snapshots must verify the public registry')
    if report.get('environment',{}).get('operating_system')!='Linux':raise ValueError('A Linux CI snapshot must record Linux')
    sha_field(report['registry_sha256'])
    matches_registry=report['registry_sha256']==registry_sha
    current={row['id']:row for row in registry['examples']}
    cases=report['examples'];ids=[row['id'] for row in cases]
    if not cases or len(set(ids))!=len(ids):raise ValueError('Invalid saved example inventory')
    groups=defaultdict(list)
    for row in cases:groups[row['execution']['group']].append(row)
    if report.get('unique_runner_executions')!=len(groups) or len(report.get('releases',[]))!=len(groups):
        raise ValueError('Saved runner count does not match its examples/releases')
    if matches_registry and set(ids)!=set(current):raise ValueError('Current-registry snapshot has a different example inventory')
    for group,rows in groups.items():
        member_ids={row['id'] for row in rows}
        for row in rows:
            execution=row['execution'];validation=row['validation']
            if row.get('passed') is not True or execution.get('completed') is not True or execution.get('exit_code')!=0 or execution.get('timed_out') is not False or validation.get('passed') is not True:
                raise ValueError('Saved success contains failed/uncompleted execution')
            if set(execution['shared_runner_cases'])!=member_ids or execution!=rows[0]['execution']:
                raise ValueError('Shared-runner records are inconsistent')
            checks=validation.get('checks',[]);failures=validation.get('expected_failures',[])
            if not checks or any(check.get('passed') is not True for check in checks+failures):
                raise ValueError('Saved success contains an unpassed numerical/output check')
            if matches_registry:
                original=current[row['id']]
                if original['execution_group']!=group or original['problem_id']!=row['problem_id'] or set(original['shared_runner_cases'])!=member_ids:
                    raise ValueError('Snapshot execution mapping differs from current registry')
                for expected,actual_rows in [(original['checks'],checks),(original.get('expected_failures',[]),failures)]:
                    actual={check['id']:check for check in actual_rows}
                    if len(actual)!=len(actual_rows):raise ValueError('Duplicate saved criterion ID')
                    for spec in expected:
                        if spec['id'] not in actual:raise ValueError('Missing advertised numerical criterion')
                        check_observed(module,actual[spec['id']],spec)
            else:
                # An old registry is not silently treated as the current one.
                # Re-evaluate the recorded observations against its saved rules.
                for actual in checks+failures:
                    if actual.get('comparison') in module.CHECK_TYPES:
                        spec={k:actual[k] for k in ['id','pointer','comparison','expected','tolerance','where','field'] if k in actual}
                        check_observed(module,actual,spec)
    run_id=envelope['run_id']
    if isinstance(run_id,bool) or not re.fullmatch('[1-9][0-9]*',str(run_id)):raise ValueError('Invalid Actions run ID')
    attempt=envelope['attempt']
    if type(attempt) is not int or attempt<1:raise ValueError('Invalid Actions attempt')
    if not re.fullmatch('[0-9a-f]{40}',envelope['workflow_commit']):raise ValueError('Invalid workflow commit')
    repository=config['workflow']['repository']
    github_run(envelope['run_url'],repository,run_id)
    github_run(envelope['artifact_url'],repository,run_id,artifact=True)
    stamp=datetime.fromisoformat(report['verified_on'].replace('Z','+00:00'))
    if stamp.tzinfo is None:raise ValueError('Snapshot timestamp needs a timezone')
    return {'url':url,'verified_on':report['verified_on'],
            'verified_utc':stamp.astimezone(timezone.utc).strftime('%Y-%m-%d %H:%M UTC'),
            'verified_jst':stamp.astimezone(timezone(timedelta(hours=9))).strftime('%Y-%m-%d %H:%M JST'),
            'run_url':envelope['run_url'],'artifact_url':envelope['artifact_url'],'run_id':str(run_id),
            'attempt':attempt,'workflow_commit':envelope['workflow_commit'],
            'environment':report['environment'],'registry_sha256':report['registry_sha256'],
            'registry_matches_current':matches_registry,'example_count':len(cases),'runner_count':len(groups),
            'example_ids_match_current':set(ids)==set(current),'recorded_success':True,
            'scope':report.get('scope','')}


def load(root):
    source=(root/CATALOG).read_bytes();config=json.loads(source)
    if config.get('schema_version')!=1 or config.get('route')!=ROUTE:raise ValueError('Unsupported CI page configuration')
    raw=(root/REGISTRY).read_bytes();registry=json.loads(raw);registry_sha=digest(raw)
    spec=importlib.util.spec_from_file_location('ci_registry',root/'scripts/build-atlas-execution-examples.py')
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    module.validate_registry(registry)
    examples=registry['examples'];groups={row['execution_group'] for row in examples}
    releases={(row['release']['family'],row['release']['version']) for row in examples}
    current={'url':ORIGIN+'/'+REGISTRY,'sha256':registry_sha,'example_count':len(examples),'runner_count':len(groups),'release_count':len(releases)}
    snapshots=[]
    for item in config['snapshots']:
        url=item if isinstance(item,str) else item['url']
        path=snapshot_path(url,root)
        record=validate_snapshot(url,json.loads(path.read_bytes()),registry,registry_sha,config,module)
        record['sha256']=digest(path.read_bytes());snapshots.append(record)
    return config,current,snapshots,digest(source)


def snapshot_html(record,config,lang):
    ja=lang=='ja';matched=record['registry_matches_current']
    label=('保存された成功記録・現行台帳と一致' if matched else '過去の台帳に対する成功記録') if ja else ('Saved success · matches current registry' if matched else 'Historical success · earlier registry')
    body='<article class="ci-snapshot"><h3>'+label+'</h3>'
    body+=paragraph((record['verified_jst']+' / '+record['verified_utc']) if ja else record['verified_utc'])
    if not matched:body+=paragraph('この成功記録の台帳ハッシュは現在の台帳とは異なります。現在の15例がこの実行で確認されたとは表示しません。' if ja else 'This receipt has a different registry hash; it is not shown as verification of the current examples.','ci-note')
    body+=paragraph((f'{record["example_count"]}問題の数値条件が合格。共有を除いた実行は{record["runner_count"]}回。' if ja else f'Numerical conditions passed for {record["example_count"]} problems in {record["runner_count"]} distinct executions.'))
    body+='<nav class="ci-links">'+link(record['url'],'保存済み成功記録 / JSON' if ja else 'Saved successful receipt / JSON')+link(record['run_url'],'この実行のログ' if ja else 'Logs for this run')+link(record['artifact_url'],'この実行のartifact' if ja else 'Artifacts for this run')+'</nav>'
    body+='<details><summary>'+('環境・版・ハッシュ' if ja else 'Environment, editions and hashes')+'</summary><dl>'
    environment=record['environment']
    for key,value in [('Run',record['run_id']+' / attempt '+str(record['attempt'])),('CI commit',record['workflow_commit']),('Registry SHA-256',record['registry_sha256']),('OS',environment['operating_system']),('Python',environment.get('python','')),('NumPy',environment.get('numpy','')),('SciPy',environment.get('scipy','')),('Matplotlib',environment.get('matplotlib',''))]:
        body+='<dt>'+esc(key)+'</dt><dd><code>'+esc(value)+'</code></dd>'
    body+='</dl>'+paragraph('CIの検査プログラムのcommitと、計算に使うZIPの版は別です。ZIPの版・入力・取得ハッシュは保存JSONに記録しています。' if ja else 'The CI harness commit is distinct from scientific ZIP editions. ZIP versions, inputs and download hashes are recorded in the saved JSON.','ci-note')+'</details></article>'
    return body


def render(config,current,snapshots,lang):
    ja=lang=='ja';workflow=config['workflow'];environment=config['environment'];definitions=config['definitions']
    title='公開配布物のLinux再実行' if ja else 'Public-distribution checks on Linux'
    body='<section data-site-language="'+lang+'" lang="'+lang+'"><p class="eyebrow">PUBLIC DISTRIBUTIONS · FRESH LINUX CI</p><h1>'+title+'</h1>'+paragraph(config['scope'][lang],'intro')
    body+='<nav class="ci-links">'+link('/numerical-methods-atlas/code-and-data/?lang='+lang,'取得・実行の案内' if ja else 'Download and execution guide')+link('/numerical-methods-atlas/code-and-data/examples.json','実行例台帳 / JSON' if ja else 'Execution registry / JSON')+link('#latest-'+lang,'最新のCI状態' if ja else 'Current CI status')+link('#saved-'+lang,'保存された成功記録' if ja else 'Saved successful runs')+'</nav>'
    body+='<section id="latest-'+lang+'" class="ci-panel"><h2>'+('最新のCI状態' if ja else 'Current CI status')+'</h2>'
    body+='<a class="ci-badge" href="'+esc(workflow['runs_url'])+'"><img src="'+esc(workflow['badge_url'])+'" alt="'+('GitHub Actions：公開ブランチのワークフロー状態' if ja else 'GitHub Actions workflow status for the public branch')+'"></a>'
    body+=paragraph(definitions['latest'][lang])
    body+='<nav class="ci-links">'+link(workflow['runs_url'],'最近の実行・ログ・artifactを開く' if ja else 'Recent runs, logs and artifacts')+link(workflow['runs_api'],'最新runの公開API / JSON' if ja else 'Latest-run public API / JSON')+link(workflow['source_url'],'CIの設定を見る' if ja else 'View the workflow configuration')+'</nav>'
    body+=paragraph(definitions['artifact'][lang],'ci-note')
    body+='</section><section id="saved-'+lang+'" class="ci-panel"><h2>'+('保存されたLinux成功記録' if ja else 'Saved successful Linux runs')+'</h2>'+paragraph(definitions['saved'][lang])
    if snapshots:
        body+=''.join(snapshot_html(record,config,lang) for record in snapshots)
    else:
        body+='<div class="ci-pending">'+paragraph('保存済みのLinux成功記録はまだありません。初回の成功記録を確認してから、日時・環境・ハッシュ付きのJSONを追加します。最新の実行結果は上のActionsリンクで確認できます。' if ja else 'There is no saved successful Linux receipt yet. A dated JSON record with environment and hashes will be added after the first success is checked. Use the Actions link above for current run results.')+'</div>'
    body+='</section><section class="ci-panel" id="scope-'+lang+'"><h2>'+('何を確認するか・運用の条件' if ja else 'Verification scope and operation')+'</h2>'
    body+=paragraph((f'現在の対象は{current["example_count"]}問題、共有を除く{current["runner_count"]}コマンド、{current["release_count"]}つの配布ZIPです。' if ja else f'The current scope is {current["example_count"]} problems, {current["runner_count"]} distinct commands and {current["release_count"]} distribution ZIPs.'))
    body+=paragraph(definitions['atomic'][lang])
    body+='<ol class="ci-phases">'+''.join('<li>'+esc(row['label'][lang])+'</li>' for row in definitions['phases'])+'</ol>'
    body+=paragraph('取得・導入・実行・数値判定のどこで止まったかを記録します。計算が未実行の場合は、数値条件の不合格と区別します。失敗時のログとJSONもActionsのartifactに残します。' if ja else 'The record distinguishes download, setup, execution and numerical-validation failures. An unrun calculation is separate from failed numerical acceptance. Failure logs and JSON are also retained as Actions artifacts.')
    body+=paragraph(definitions['limits'][lang],'ci-note')
    body+='<dl class="ci-operations">'
    operations=[('実行環境' if ja else 'Environment',environment['runner']+' / Python '+environment['python']),
                ('実行の契機' if ja else 'Triggers',('手動、'+config['cadence']['weekly'][lang]+'、サイト検査成功後（公開URLの版照合を待つ）' if ja else 'Manual, '+config['cadence']['weekly'][lang]+', and after successful site checks (waiting for matching public versions)')),
                ('公開版の確認' if ja else 'Publication gate',config['cadence']['publication_gate'][lang]),
                ('依存関係' if ja else 'Dependencies',environment['dependency_policy'][lang]),
                ('時間上限' if ja else 'Timeouts',(f'各コマンド{environment["runner_timeout_seconds"]}秒、CI全体{environment["workflow_timeout_minutes"]}分' if ja else f'{environment["runner_timeout_seconds"]} seconds per command; {environment["workflow_timeout_minutes"]} minutes overall')),
                ('台帳のSHA-256' if ja else 'Current registry SHA-256',current['sha256'])]
    body+=''.join('<dt>'+esc(label)+'</dt><dd>'+esc(value)+'</dd>' for label,value in operations)+'</dl>'
    body+='<p>'+link('index.json','CI案内の台帳 / JSON' if ja else 'CI page metadata / JSON')+' · '+link('/rights/?lang='+lang,'利用条件・AI方針' if ja else 'Rights and AI policy')+'</p></section></section>'
    return body


def build(root=ROOT):
    config,current,snapshots,source_sha=load(root)
    css=digest((root/'styles/atlas-ci.css').read_bytes())[:12]
    document='<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
    document+='<title data-page-title-ja="公開配布物のLinux再実行 | 数値計算法アトラス" data-page-title-en="Public Linux verification | Numerical Methods Atlas">公開配布物のLinux再実行 | 数値計算法アトラス</title>'
    document+='<meta name="description" content="公開配布物15問題のfresh Linux CI。最新のActions状態と保存された成功記録を分け、取得・導入・実行・数値判定を確認。" data-description-ja="公開配布物15問題のfresh Linux CI。最新状態と保存された成功記録を分けて確認。" data-description-en="Fresh Linux checks for 15 public-distribution examples, separating current Actions status from saved successful receipts."><link rel="canonical" href="'+ORIGIN+ROUTE+'">'
    document+='<!-- site-head --><link rel="stylesheet" href="/site.css"><script src="/site.js" defer></script><!-- /site-head -->'
    document+='<link rel="stylesheet" href="/styles/atlas-ci.css?v='+css+'"></head><body class="profile-page" data-site-language-anchors="suffix"><main id="main" class="profile-main atlas-ci-main">'
    document+=''.join(render(config,current,snapshots,lang) for lang in ['ja','en'])+'</main></body></html>\n'
    public={**config,'url':ORIGIN+ROUTE,'catalog_source':{'url':ORIGIN+'/'+CATALOG,'sha256':source_sha},
            'current_registry':current,'latest_status':{'source':'external-github-actions-badge','recorded_conclusion':None},
            'workflow_runs_api':config['workflow']['runs_api'],
            'snapshots':snapshots}
    return document,public


def main():
    document,public=build()
    destination=ROOT/ROUTE.lstrip('/');destination.mkdir(parents=True,exist_ok=True)
    (destination/'index.html').write_text(document)
    (destination/'index.json').write_text(encode(public))
    guide=ROOT/'llms.txt';text=guide.read_text()
    text=re.sub(r'^- \[Public Linux verification CI\].*\n?','',text,flags=re.M)
    line=f'- [Public Linux verification CI]({ORIGIN}{ROUTE}): {public["current_registry"]["example_count"]} fixed-input public-distribution examples; latest workflow status and runs via GitHub Actions, separately from dated saved Linux success snapshots. The JSON page metadata links to the latest-run public API; no scientific data or code is changed by this page.\n'
    guide.write_text(text.rstrip()+'\n'+line)
    print('Built bilingual Linux CI guide:',public['current_registry']['example_count'],'problems;',len(public['snapshots']),'saved successes.')


if __name__=='__main__':main()
