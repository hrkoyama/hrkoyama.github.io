#!/usr/bin/env python3
"""Bootstrap public atlas checks without a checkout or preinstalled science stack.

Only standard-library modules are imported here. Public registry and tool bytes
are SHA-256 pinned; science runs in a fresh venv using source from public ZIPs.
"""
from pathlib import Path, PurePosixPath
import argparse
import datetime
import hashlib
import json
import math
import os
import platform
import re
import subprocess
import sys
import tempfile
import time
import urllib.parse
import urllib.request

ORIGIN = 'https://hrkoyama.github.io'
REGISTRY_URL = ORIGIN+'/numerical-methods-atlas/code-and-data/examples.json'
VERIFIER_URL = ORIGIN+'/scripts/verify-atlas-execution-examples.py'
BUILDER_URL = ORIGIN+'/scripts/build-atlas-execution-examples.py'
REQUIRED_PINS = {'numpy':'2.0.2','scipy':'1.14.1','matplotlib':'3.9.4','pytest':'8.3.5'}


def digest(data):return hashlib.sha256(data).hexdigest()


def valid_hash(value):
    if not isinstance(value,str) or not re.fullmatch('[a-f0-9]{64}',value):
        raise ValueError('Expected a lowercase SHA-256 digest')
    return value


def allowed_public_url(url):
    if not isinstance(url,str) or any(char.isspace() for char in url):raise ValueError('Invalid public URL')
    parsed = urllib.parse.urlparse(url)
    if parsed.scheme!='https' or parsed.netloc!='hrkoyama.github.io' or parsed.query or parsed.fragment:
        raise ValueError('Only canonical public HTTPS URLs are allowed')
    path = urllib.parse.unquote(parsed.path)
    if '\\' in path or '%' in path or any(part in ['', '.', '..'] for part in path.lstrip('/').split('/')):
        raise ValueError('Unsafe public artifact path')
    if not (url in {REGISTRY_URL,VERIFIER_URL,BUILDER_URL} or path.startswith('/code/')):
        raise ValueError('Only the registry, two pinned scripts and code artifacts are allowed')
    return url


class PublicRedirectHandler(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        target = urllib.parse.urljoin(req.full_url,newurl)
        allowed_public_url(target)
        return super().redirect_request(req,fp,code,msg,headers,target)


PUBLIC_OPENER = urllib.request.build_opener(urllib.request.ProxyHandler({}),PublicRedirectHandler())


def download(url, expected=None, limit=20_000_000):
    allowed_public_url(url)
    if expected is not None:valid_hash(expected)
    request = urllib.request.Request(url,headers={'User-Agent':'Atlas-public-CI/1.0'})
    with PUBLIC_OPENER.open(request,timeout=60) as response:
        allowed_public_url(response.geturl())
        data=response.read(limit+1)
    if len(data)>limit:raise ValueError('Public artifact exceeds download budget')
    if expected is not None and digest(data)!=expected:raise ValueError('Public artifact SHA-256 mismatch')
    return data


def strict_json(raw):
    def reject(value):raise ValueError('Nonfinite JSON constant')
    document=json.loads(raw,parse_constant=reject)
    def finite(value):
        if isinstance(value,float) and not math.isfinite(value):raise ValueError('Nonfinite JSON number')
        if isinstance(value,dict):
            for item in value.values():finite(item)
        elif isinstance(value,list):
            for item in value:finite(item)
    finite(document)
    return document


def write_json(path, value):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    staged=path.with_name(path.name+'.writing')
    staged.write_text(json.dumps(value,ensure_ascii=False,indent=2,allow_nan=False)+'\n')
    staged.replace(path)


def child_environment(temporary, parent=None):
    parent=os.environ if parent is None else parent
    names=['PATH','LANG','LC_ALL','LC_CTYPE','SYSTEMROOT','WINDIR','COMSPEC','PATHEXT']
    env={name:parent[name] for name in names if name in parent}
    temporary=Path(temporary)
    home=temporary/'home';home.mkdir(parents=True,exist_ok=True)
    scratch=temporary/'tmp';scratch.mkdir(parents=True,exist_ok=True)
    env.update(PATH=env.get('PATH',os.defpath),HOME=str(home),USERPROFILE=str(home),
               TMPDIR=str(scratch),TMP=str(scratch),TEMP=str(scratch),
               PYTHONDONTWRITEBYTECODE='1',PYTHONNOUSERSITE='1',
               MPLBACKEND='Agg',MPLCONFIGDIR=str(temporary/'matplotlib'),
               OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1',
               PIP_CONFIG_FILE=os.devnull,PIP_DISABLE_PIP_VERSION_CHECK='1')
    return env


def github_metadata(parent=None):
    """Record only public run identity, never arbitrary environment variables."""
    parent=os.environ if parent is None else parent
    result={}
    run_id=parent.get('GITHUB_RUN_ID','');attempt=parent.get('GITHUB_RUN_ATTEMPT','')
    commit=parent.get('GITHUB_SHA','');repository=parent.get('GITHUB_REPOSITORY','')
    server=parent.get('GITHUB_SERVER_URL','https://github.com')
    if re.fullmatch('[0-9]+',run_id):result['run_id']=run_id
    if re.fullmatch('[0-9]+',attempt):result['run_attempt']=attempt
    if re.fullmatch('[a-fA-F0-9]{40}|[a-fA-F0-9]{64}',commit):result['sha']=commit.lower()
    parsed=urllib.parse.urlparse(server)
    if ('run_id' in result and re.fullmatch('[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+',repository)
            and parsed.scheme=='https' and parsed.hostname and not parsed.username and not parsed.password
            and not parsed.query and not parsed.fragment and parsed.path in ['', '/']):
        result['url']=server.rstrip('/')+'/'+repository+'/actions/runs/'+run_id
    return result


def parse_requirements(text):
    """Accept only the four approved exact pins, not pip options or URLs."""
    if not isinstance(text,str):raise ValueError('Requirements must be UTF-8 text')
    pins={}
    for number,line in enumerate(text.splitlines(),1):
        line=line.strip()
        if not line or line.startswith('#'):continue
        match=re.fullmatch(r'([A-Za-z0-9][A-Za-z0-9._-]*)==([0-9]+(?:\.[0-9]+){1,3})',line)
        if not match:raise ValueError('Unsupported requirement on line '+str(number))
        name=re.sub('[-_.]+','-',match[1]).lower();version=match[2]
        if REQUIRED_PINS.get(name)!=version:raise ValueError('Unapproved dependency name or version on line '+str(number))
        pins[name]=version
    if not pins:raise ValueError('Empty requirements are not an environment definition')
    return pins


def fetch_to(url, expected, destination, acquisitions, kind):
    try:
        payload=download(url,expected)
    except Exception as exc:
        acquisitions.append({'kind':kind,'url':url,'expected_sha256':expected,'passed':False,'error':type(exc).__name__+': '+str(exc)})
        raise
    destination=Path(destination);destination.parent.mkdir(parents=True,exist_ok=True)
    destination.write_bytes(payload)
    acquisitions.append({'kind':kind,'url':url,'expected_sha256':expected,'sha256':digest(payload),'bytes':len(payload),'passed':True})
    return payload


def collect_requirements(registry, downloads_dir, acquisitions):
    """Read only each edition's pinned core requirements; never forward -r lines."""
    editions={}
    for example in registry['examples']:
        release=example['release'];key=(release['family'],release['version'],release['manifest_sha256'])
        item=editions.setdefault(key,{'release':release,'core':example['dependencies']['core']})
        if item['core']!=example['dependencies']['core']:raise ValueError('One edition has inconsistent core requirements')
    if len(editions)!=4:raise ValueError('Expected the four public code editions')
    pins={};downloads_dir=Path(downloads_dir)
    for index,item in enumerate(editions.values()):
        release=item['release'];valid_hash(release['manifest_sha256'])
        raw=fetch_to(release['manifest'],release['manifest_sha256'],downloads_dir/f'manifest-{index}.json',acquisitions,'manifest')
        manifest=strict_json(raw)
        if manifest['edition']!=release['version']:raise ValueError('Requirements manifest edition mismatch')
        url=allowed_public_url(item['core'])
        base=PurePosixPath(urllib.parse.urlparse(release['manifest']).path).parent
        relative=PurePosixPath(urllib.parse.urlparse(url).path).relative_to(base).as_posix()
        if relative!='requirements.txt':raise ValueError('Core requirements must be the edition requirements.txt')
        expected=valid_hash(manifest['files'].get(relative))
        payload=fetch_to(url,expected,downloads_dir/f'requirements-{index}.txt',acquisitions,'core-requirements')
        for name,version in parse_requirements(payload.decode('utf-8')).items():
            if name in pins and pins[name]!=version:raise ValueError('Conflicting pinned requirements')
            pins[name]=version
    if pins!=REQUIRED_PINS:raise ValueError('The three core requirements do not define the approved four packages')
    return pins


def _bytes(value):
    if value is None:return b''
    return value if isinstance(value,bytes) else str(value).encode('utf-8',errors='replace')


def run_logged(argv, cwd, env, timeout, stdout_path, stderr_path):
    stdout_path,stderr_path=Path(stdout_path),Path(stderr_path)
    stdout_path.parent.mkdir(parents=True,exist_ok=True)
    stdout_path.write_bytes(b'');stderr_path.write_bytes(b'')
    before=time.monotonic();out=err=b''
    result={'exit_code':None,'timed_out':False}
    try:
        proc=subprocess.run(argv,cwd=cwd,env=env,text=True,encoding='utf-8',errors='replace',capture_output=True,timeout=timeout)
        result['exit_code']=proc.returncode;out,err=_bytes(proc.stdout),_bytes(proc.stderr)
    except subprocess.TimeoutExpired as exc:
        result.update(timed_out=True,error='process_timeout');out,err=_bytes(exc.stdout),_bytes(exc.stderr)
    except (OSError,subprocess.SubprocessError) as exc:
        result['error']=type(exc).__name__+': '+str(exc);err=_bytes(result['error'])
    finally:
        stdout_path.write_bytes(out);stderr_path.write_bytes(err)
    result['duration_seconds']=round(time.monotonic()-before,6)
    return result


def require_success(result, label):
    if result.get('exit_code')!=0 or result.get('timed_out'):
        raise RuntimeError(label+' failed; see the saved stdout/stderr logs')


def create_environment(work, env, output):
    work,output=Path(work),Path(output)
    directory=work/'venv'
    result=run_logged([sys.executable,'-m','venv',str(directory)],work,env,120,
                      output/'logs/venv.stdout.log',output/'logs/venv.stderr.log')
    require_success(result,'venv creation')
    return directory/('Scripts/python.exe' if os.name=='nt' else 'bin/python')


def validate_registry(registry):
    if (not isinstance(registry,dict) or type(registry.get('schema_version')) is not int
            or registry['schema_version']!=1 or registry.get('url')!=REGISTRY_URL
            or not isinstance(registry.get('catalog_source'),dict)):
        raise ValueError('Expected a canonical public registry')
    records=registry.get('examples')
    if not isinstance(records,list) or len(records)!=19:raise ValueError('Expected all nineteen public examples')
    ids=[row['id'] for row in records]
    if len(set(ids))!=19 or any(not re.fullmatch('[a-z0-9-]+',ident) for ident in ids):raise ValueError('Invalid example inventory')


def validate_scientific_report(report, registry, expected):
    if not isinstance(report,dict):return False
    if (report.get('schema_version')!=1 or report.get('passed') is not True
            or report.get('registry_url')!=REGISTRY_URL or report.get('registry_source_mode')!='public-registry'
            or report.get('registry_sha256')!=expected['registry']):return False
    tool=report.get('verification_tool',{})
    if not isinstance(tool,dict):return False
    if tool.get('verifier_sha256')!=expected['verifier'] or tool.get('registry_builder_sha256')!=expected['builder']:return False
    groups={example['execution_group'] for example in registry['examples']}
    releases=report.get('releases',[])
    if (len(groups)!=18 or type(report.get('unique_runner_executions')) is not int
            or report['unique_runner_executions']!=len(groups) or not isinstance(releases,list)
            or len(releases)!=len(groups)):
        return False
    if any(not isinstance(release,dict) or not isinstance(release.get('execution'),dict) for release in releases):return False
    if {release['execution'].get('group') for release in releases}!=groups:return False
    if any(release.get('execution',{}).get('started') is not True
           or release.get('execution',{}).get('completed') is not True
           or type(release.get('execution',{}).get('exit_code')) is not int
           or release['execution']['exit_code']!=0 for release in releases):return False
    rows=report.get('examples',[])
    if not isinstance(rows,list) or len(rows)!=len(registry['examples']):return False
    if any(not isinstance(row,dict) for row in rows):return False
    records={row.get('id'):row for row in rows}
    if len(records)!=len(rows) or set(records)!={row['id'] for row in registry['examples']}:return False
    runs={release['execution']['group']:release['execution'] for release in releases}
    for example in registry['examples']:
        row=records[example['id']];execution=row.get('execution',{});validation=row.get('validation',{})
        if not isinstance(execution,dict) or not isinstance(validation,dict):return False
        if row.get('passed') is not True or row.get('problem_id')!=example['problem_id']:return False
        if execution.get('completed') is not True or type(execution.get('exit_code')) is not int or execution['exit_code']!=0 or execution.get('timed_out'):return False
        if execution.get('group')!=example['execution_group'] or set(execution.get('shared_runner_cases',[]))!=set(example['shared_runner_cases']):return False
        if execution!=runs[example['execution_group']] or execution.get('command')!=example['commands']['run']:return False
        if validation.get('passed') is not True:return False
        checks=validation.get('checks',[]);failures=validation.get('expected_failures',[])
        if not isinstance(checks,list) or not isinstance(failures,list) or any(not isinstance(check,dict) for check in checks+failures):return False
        if not checks or any(check.get('passed') is not True for check in checks+failures):return False
        required={check['id'] for check in example['checks']}|{'output-'+asset['id'] for asset in example['outputs']}
        if not required<={check.get('id') for check in checks}:return False
    return True


def failure_report(registry, expected, phase, error):
    rows=[]
    candidates=registry.get('examples',[]) if isinstance(registry,dict) else []
    for example in candidates if isinstance(candidates,list) else []:
        if not isinstance(example,dict) or not isinstance(example.get('id'),str):continue
        ident=example['id'];commands=example.get('commands',{})
        rows.append({'id':ident,'problem_id':example.get('problem_id',ident),
                     'execution':{'group':example.get('execution_group',ident),'started':False,'completed':False,'exit_code':None,'timed_out':False,'duration_seconds':0.,'shared_runner_cases':example.get('shared_runner_cases',[ident]),'command':commands.get('run','') if isinstance(commands,dict) else ''},
                     'validation':{'passed':False,'checks':[],'expected_failures':[],'phase':phase,'error':'ci_verification_not_accepted' if phase=='verification' else 'not_run_after_ci_setup_failure'},'residuals':{},'passed':False})
    return {'schema_version':1,'verified_on':datetime.datetime.now(datetime.timezone.utc).isoformat(),
            'registry_url':REGISTRY_URL,'registry_sha256':expected.get('registry'),'registry_source_mode':'public-registry',
            'environment':{},'releases':[],'examples':rows,'unique_runner_executions':0,
            'passed':False,'status':'failed','error':{'phase':phase,'message':error},
            'scope':'CI setup or verification contract failed; no successful CI validation is claimed. Inspect saved verifier logs and any unaccepted raw report.'}


def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir',type=Path,required=True)
    parser.add_argument('--registry-sha256',required=True)
    parser.add_argument('--verifier-sha256',required=True)
    parser.add_argument('--builder-sha256',required=True)
    parser.add_argument('--timeout',type=int,default=120)
    args=parser.parse_args(argv)
    output=args.output_dir.resolve()
    if output.exists() and (not output.is_dir() or any(output.iterdir())):
        print('Output directory must be new or empty; previous results are preserved',file=sys.stderr);return 2
    output.mkdir(parents=True,exist_ok=True)
    expected={};registry=None;acquisitions=[];phase='preflight'
    summary={'schema_version':1,'started_on':datetime.datetime.now(datetime.timezone.utc).isoformat(),
             'passed':False,'setup_passed':False,'scientific_passed':False,'phase':phase,
             'github':github_metadata(),'expected_sha256':expected,'acquisitions':acquisitions,
             'bootstrap':{'url':ORIGIN+'/scripts/run-atlas-public-ci.py','sha256':digest(Path(__file__).read_bytes())},
             'host':{'python':platform.python_version(),'operating_system':platform.system(),'machine':platform.machine()},
             'dependency_policy':{'core_requirements_only':True,'wheel_only':True,'cache':False,'index':'https://pypi.org/simple','direct_pins':REQUIRED_PINS,'transitive_dependencies':'Fresh PyPI wheel resolution, recorded by pip freeze and install report; not a complete lock file.'}}
    write_json(output/'ci-summary.json',summary)
    try:
        for name,value in [('registry',args.registry_sha256),('verifier',args.verifier_sha256),('builder',args.builder_sha256)]:expected[name]=valid_hash(value)
        if args.timeout<=0:raise ValueError('--timeout must be positive')
        with tempfile.TemporaryDirectory(prefix='atlas-public-ci-') as temporary:
            work=Path(temporary);env=child_environment(work)
            phase='public-downloads'
            raw=fetch_to(REGISTRY_URL,expected['registry'],output/'downloads/registry.json',acquisitions,'registry')
            registry=strict_json(raw);validate_registry(registry)
            for name,url in [('verifier',VERIFIER_URL),('builder',BUILDER_URL)]:
                payload=fetch_to(url,expected[name],output/'downloads/scripts'/url.rsplit('/',1)[1],acquisitions,name)
                target=work/'scripts'/url.rsplit('/',1)[1];target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(payload)
            phase='requirements'
            pins=collect_requirements(registry,output/'downloads/requirements',acquisitions)
            write_json(output/'requirements.json',{'direct_pins':pins,'requirements_scope':'Manifest-verified requirements.txt of all three code editions; optional PySCF reference regeneration is excluded.'})
            phase='venv'
            python=create_environment(work,env,output)
            phase='pip-install'
            install=[str(python),'-m','pip','--isolated','--disable-pip-version-check','--no-input','install','--no-cache-dir','--only-binary=:all:','--index-url','https://pypi.org/simple','--report',str(output/'pip-install.json'),*[name+'=='+version for name,version in sorted(pins.items())]]
            result=run_logged(install,work,env,600,output/'logs/pip-install.stdout.log',output/'logs/pip-install.stderr.log')
            summary['pip_install_process']=result;require_success(result,'wheel-only package installation')
            install_report=strict_json((output/'pip-install.json').read_bytes())
            installed=install_report.get('install')
            if not isinstance(installed,list) or not installed:raise ValueError('Installation report has no installed wheels')
            wheels=[]
            for package in installed:
                parsed=urllib.parse.urlparse(package['download_info']['url'])
                if (parsed.scheme!='https' or parsed.netloc not in {'files.pythonhosted.org','pypi.org'}
                        or parsed.query or parsed.fragment or not parsed.path.endswith('.whl')):
                    raise ValueError('Installation report contains a non-PyPI wheel source')
                archive=package['download_info']['archive_info']
                wheel_sha=archive.get('hashes',{}).get('sha256') or archive.get('hash','').removeprefix('sha256=')
                valid_hash(wheel_sha)
                wheels.append({'name':package['metadata']['name'],'version':package['metadata']['version'],
                               'url':package['download_info']['url'],'sha256':wheel_sha})
            summary['wheel_artifacts']=wheels
            phase='environment'
            result=run_logged([str(python),'-m','pip','freeze','--all'],work,env,60,output/'pip-freeze.txt',output/'logs/pip-freeze.stderr.log')
            require_success(result,'pip freeze')
            result=run_logged([str(python),'-m','pip','check'],work,env,60,output/'logs/pip-check.stdout.log',output/'logs/pip-check.stderr.log')
            require_success(result,'pip dependency check')
            probe='import json,platform,importlib.metadata as m;print(json.dumps({"python":platform.python_version(),"operating_system":platform.system(),"machine":platform.machine(),"packages":{k:m.version(k) for k in ["numpy","scipy","matplotlib","pytest"]}}))'
            result=run_logged([str(python),'-c',probe],work,env,30,output/'logs/environment.stdout.log',output/'logs/environment.stderr.log')
            require_success(result,'environment probe')
            environment=strict_json((output/'logs/environment.stdout.log').read_bytes())
            if environment.get('packages')!=REQUIRED_PINS:raise ValueError('Installed direct versions differ from the approved pins')
            write_json(output/'environment.json',environment)
            summary['environment']=environment;summary['setup_passed']=True
            phase='verification';summary['phase']=phase;write_json(output/'ci-summary.json',summary)
            command=[str(python),str(work/'scripts/verify-atlas-execution-examples.py'),'--registry',REGISTRY_URL,
                     '--expected-registry-sha256',expected['registry'],'--python',str(python),
                     '--output',str(output/'report.json'),'--artifacts-dir',str(output/'artifacts'),'--timeout',str(args.timeout)]
            result=run_logged(command,work,env,max(180,len(registry['examples'])*(args.timeout+180)),output/'logs/verifier.stdout.log',output/'logs/verifier.stderr.log')
            summary['verifier_process']=result
            report=strict_json((output/'report.json').read_bytes())
            good=result.get('exit_code')==0 and not result.get('timed_out') and validate_scientific_report(report,registry,expected)
            summary.update(scientific_passed=bool(good),passed=bool(good))
            if not good:
                if isinstance(report,dict) and report.get('passed') is True:
                    (output/'report.json').replace(output/'report-unaccepted.json')
                    summary['unaccepted_report']='report-unaccepted.json'
                raise RuntimeError('Public-file verification did not pass; inspect report.json and group logs')
            phase='complete'
    except Exception as exc:
        summary.update(passed=False,scientific_passed=False,error={'phase':phase,'type':type(exc).__name__,'message':str(exc)})
        report_path=output/'report.json'
        try:
            if report_path.exists():strict_json(report_path.read_bytes())
            else:write_json(report_path,failure_report(registry,expected,phase,str(exc)))
        except (OSError,ValueError):
            if report_path.exists():report_path.replace(output/'report-invalid.bin')
            write_json(report_path,failure_report(registry,expected,phase,str(exc)))
    finally:
        summary.update(phase=phase,finished_on=datetime.datetime.now(datetime.timezone.utc).isoformat())
        write_json(output/'acquisitions.json',acquisitions)
        write_json(output/'ci-summary.json',summary)
    print(json.dumps({'passed':summary['passed'],'setup_passed':summary['setup_passed'],'scientific_passed':summary['scientific_passed'],'phase':phase}))
    return 0 if summary['passed'] else 1


if __name__=='__main__':raise SystemExit(main())
