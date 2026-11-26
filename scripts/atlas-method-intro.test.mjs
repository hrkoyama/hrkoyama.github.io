import test from 'node:test';
import assert from 'node:assert/strict';
import {execFileSync} from 'node:child_process';
import {fileURLToPath} from 'node:url';

const root=fileURLToPath(new URL('../',import.meta.url));
// Extract the pure HTML helpers without running the asset-generating builder.
const probe=String.raw`
import ast,copy,html,json,pathlib,sys
root=pathlib.Path(sys.argv[1])
tree=ast.parse((root/'scripts/build-atlas-resources.py').read_text())
names={'method_intro_parts','render_method_summary_examples'}
functions=[node for node in tree.body if isinstance(node,ast.FunctionDef) and node.name in names]
assert {node.name for node in functions}==names
namespace={'esc':html.escape}
exec(compile(ast.Module(body=functions,type_ignores=[]),'<method-intro-helpers>','exec'),namespace)
parts=namespace['method_intro_parts'];render=namespace['render_method_summary_examples']
catalog=json.loads((root/'catalog/atlas-methods.json').read_text())['methods']
before=copy.deepcopy(catalog)
outer=next(node for node in tree.body if isinstance(node,ast.For) and isinstance(node.target,ast.Name) and node.target.id=='x' and isinstance(node.iter,ast.Name) and node.iter.id=='METHODS')
inner=next(node for node in outer.body if isinstance(node,ast.For) and isinstance(node.target,ast.Name) and node.target.id=='lang')
end=next(i for i,node in enumerate(inner.body) if isinstance(node,ast.AugAssign) and isinstance(node.value,ast.Call) and getattr(node.value.func,'id',None)=='render_method_summary_examples')
opening=compile(ast.Module(body=inner.body[:end+1],type_ignores=[]),'<actual-method-opening-template>','exec')
def opening_html(method,language):
    env={**namespace,'x':method,'lang':language,'summary_parts':parts(method),
         'record':{'problem_navigation':{}},'status':lambda *args:'STATUS',
         'nav':lambda *args:'<nav data-general>GENERAL</nav>',
         'render_method_route_links':lambda *args:'<nav data-main-actions>MAIN</nav>',
         'render_method_routes':lambda *args:'<div data-full-routes>FULL</div>',
         'method_route_view_record':lambda value:value}
    exec(opening,env)
    return env['body']
rows=[{'id':method['id'],'parts':parts(method),'summary':method['summary'],
       'aliases':method.get('aliases',[]),
       'opening':{lang:opening_html(method,lang) for lang in ('ja','en')},
       'html':{lang:render(parts(method)[lang],lang) for lang in ('ja','en')}} for method in catalog]
release={'group':'fixture','edition':'fixture','case_ids':['fixed']}
scope={'ja':'scope JA <tag> & data','en':'scope EN <tag> & data'}
method={'id':'fixture','summary':{lang:'Definition '+lang+' '+scope[lang] for lang in ('ja','en')},
        'depth_release':release,'supplemental_scope_profiles':[{'release':release,'scope':scope}]}
def rejects(value):
    try:parts(value)
    except ValueError:return True
    return False
bad={}
value=copy.deepcopy(method);value['summary']['en']='Definition en';bad['asymmetric_language']=rejects(value)
value=copy.deepcopy(method);value['summary']['ja']+=' extra';bad['non_suffix']=rejects(value)
value=copy.deepcopy(method);value['summary']['ja']+=' '+scope['ja'];bad['repeated_scope']=rejects(value)
value=copy.deepcopy(method);value['depth_release']={**release,'edition':'other'};bad['unbound_release']=rejects(value)
value=copy.deepcopy(method);value['summary']={lang:' '+scope[lang] for lang in ('ja','en')};bad['missing_definition']=rejects(value)
plain={'id':'plain','summary':{'ja':'Definition: 追加固定例：is ordinary text.',
                             'en':'Definition: Additional fixed examples: is ordinary text.'}}
print(json.dumps({'rows':rows,'input_unchanged':catalog==before,'bad':bad,'plain':parts(plain),
                  'plain_summary':plain['summary'],'escaped':render(parts(method)['en'],'en')}))
`;
const result=JSON.parse(execFileSync(process.env.ATLAS_INDEX_PYTHON||'python3',
  ['-B','-c',probe,root],{encoding:'utf8',maxBuffer:4*1024*1024}));

test('method HTML keeps every original bilingual summary exactly reconstructible',()=>{
  assert.ok(result.input_unchanged,'presentation helpers must not mutate the catalog');
  for(const row of result.rows){
    for(const language of ['ja','en']){
      const [definition,examples]=row.parts[language];
      assert.equal(definition+(examples.length?' '+examples.join(' '):''),row.summary[language],row.id+'/'+language);
      if(!examples.length){
        assert.equal(definition,row.summary[language]);
        assert.equal(row.html[language],'');
      }else{
        assert.ok(definition.length>0);
        assert.ok(row.html[language].startsWith('<details class="method-summary-examples"><summary>'));
        assert.equal((row.html[language].match(/<li>/g)||[]).length,examples.length);
        assert.ok(!row.html[language].includes(' open'),'examples are an optional native disclosure');
      }
    }
    assert.equal(row.parts.ja[1].length,row.parts.en[1].length,row.id+': bilingual scope groups stay paired');
  }
});

test('Newton opens with its method definition while retaining all fixed-example prose',()=>{
  const row=result.rows.find(row=>row.id==='newton');
  assert.equal(row.parts.en[0],'Solve F(x)=0 using a Jacobian-based Newton direction and damping that requires sufficient decrease of the residual norm. The example supports a dense or preconditioned GMRES inner solve.');
  assert.ok(row.parts.ja[0].startsWith('非線形方程式 F(x)=0'));
  assert.ok(row.parts.en[1].some(scope=>scope.includes('Crossing the Bratu fold')));
  assert.ok(row.parts.en[1].some(scope=>scope.includes('Enzyme conservation and QSSA')));
  assert.ok(row.html.ja.includes('追加の固定入力例'));
  assert.ok(row.html.en.includes('Additional fixed-input examples'));
});

test('the actual page template places primary actions before aliases only for split introductions',()=>{
  const escape=value=>value.replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;').replaceAll('"','&quot;').replaceAll("'",'&#x27;');
  for(const row of result.rows)for(const language of ['ja','en']){
    const body=row.opening[language],actions=body.indexOf('<nav data-main-actions>'),routes=body.indexOf('<div data-full-routes>');
    assert.ok(body.indexOf('<p class="intro">')<body.indexOf('<nav data-general>'));
    assert.ok(actions<routes);
    if(row.aliases.length){
      const aliases='<p>'+(language==='ja'?'別名・表記：':'Other names: ')+escape(row.aliases.join(' / '))+'</p>';
      assert.ok(body.includes(aliases),row.id+': alias bytes retained');
      assert.equal(actions<body.indexOf(aliases),row.parts[language][1].length>0,row.id+'/'+language);
    }
    if(row.parts[language][1].length)assert.ok(routes<body.indexOf('<details class="method-summary-examples">'));
    else assert.ok(!body.includes('method-summary-examples'));
  }
});

test('ambiguous, asymmetric or unbound scope text cannot silently become a definition',()=>{
  for(const [reason,rejected] of Object.entries(result.bad))assert.ok(rejected,reason);
  for(const language of ['ja','en'])assert.deepEqual(result.plain[language],[result.plain_summary[language],[]]);
  assert.ok(result.escaped.includes('scope EN &lt;tag&gt; &amp; data'));
  assert.ok(!result.escaped.includes('<tag>'));
});
