// A small DOM for exercising both search entry points without HTML insertion.
export class SearchElement {
  constructor(tag){this.tag=tag;this.children=[];this.parentElement=null;this.dataset={};this.attributes={};this.events=new Map();this.ownText='';this.hidden=false;this.open=false;this.isConnected=true;}
  set innerHTML(_){throw Error('Search content must be constructed as text and safe DOM nodes');}
  get classList(){return {add:(...names)=>{this.className=[...new Set([...(this.className||'').split(/\s+/).filter(Boolean),...names])].join(' ');},contains:name=>(this.className||'').split(/\s+/).includes(name)};}
  set textContent(value){this.ownText=String(value);for(const child of this.children)child.parentElement=null;this.children=[];}
  get textContent(){return this.ownText+this.children.map(child=>child.textContent).join('');}
  setAttribute(name,value){this.attributes[name]=String(value);if(name.startsWith('data-'))this.dataset[name.slice(5).replace(/-([a-z])/g,(_,letter)=>letter.toUpperCase())]=String(value);else this[name==='class'?'className':name]=String(value);}
  getAttribute(name){return this.attributes[name]??(name.startsWith('data-')?this.dataset[name.slice(5).replace(/-([a-z])/g,(_,letter)=>letter.toUpperCase())]:this[name==='class'?'className':name])??null;}
  removeAttribute(name){delete this.attributes[name];if(name==='hidden')this.hidden=false;}
  append(...children){for(let child of children){if(typeof child==='string'){const text=new SearchElement('#text');text.textContent=child;child=text;}if(child.tag==='#fragment'){this.append(...[...child.children]);continue;}child.remove();child.parentElement=this;this.children.push(child);}}
  prepend(...children){const previous=[...this.children];this.replaceChildren(...children,...previous);}
  insertBefore(child,before){if(!before){this.append(child);return child;}child.remove();const index=this.children.indexOf(before);if(index<0)throw Error('insertBefore target is not a child');child.parentElement=this;this.children.splice(index,0,child);return child;}
  replaceChildren(...children){for(const child of this.children)child.parentElement=null;this.children=[];this.ownText='';this.append(...children);}
  remove(){if(this.parentElement){const index=this.parentElement.children.indexOf(this);if(index>=0)this.parentElement.children.splice(index,1);this.parentElement=null;}}
  addEventListener(type,listener){if(!this.events.has(type))this.events.set(type,[]);this.events.get(type).push(listener);}
  dispatchEvent(event){for(const listener of this.events.get(event.type)||[])listener(event);return true;}
  fire(type,properties={}){this.dispatchEvent({type,target:this,preventDefault(){},...properties});}
  querySelectorAll(selector){return descendants(this).slice(1).filter(node=>matches(node,selector));}
  querySelector(selector){return this.querySelectorAll(selector)[0]||null;}
  focus(){this.focused=true;}
  scrollIntoView(){}
}
export const descendants=node=>[node,...node.children.flatMap(descendants)];
function matches(node,selector){
  if(selector.includes(','))return selector.split(',').some(part=>matches(node,part.trim()));
  if(selector.includes(' ')){const parts=selector.trim().split(/\s+/),last=parts.pop();if(!matches(node,last))return false;let parent=node.parentElement;while(parent){if(matches(parent,parts.join(' ')))return true;parent=parent.parentElement;}return false;}
  const tag=selector.match(/^[a-z][\w-]*/i)?.[0];if(tag&&tag!==node.tag)return false;
  const id=selector.match(/#([\w-]+)/)?.[1];if(id&&node.id!==id)return false;
  for(const match of selector.matchAll(/\.([\w-]+)/g))if(!node.classList.contains(match[1]))return false;
  for(const match of selector.matchAll(/\[([\w-]+)(?:=["']?([^\]"']+)["']?)?\]/g)){
    const value=node.getAttribute(match[1]);if(value===null||value===undefined)return false;if(match[2]!==undefined&&value!==match[2])return false;
  }
  return true;
}
export function searchDOM({kind='home',language='en',query='',index,fetch:fetchOverride}={}){
  const created=[],document=new SearchElement('#document'),head=new SearchElement('head'),body=new SearchElement('body');document.head=head;document.body=body;document.documentElement={lang:language};document.append(head,body);
  document.createElement=tag=>{const node=new SearchElement(tag);created.push(node);return node;};
  document.createTextNode=value=>{const node=new SearchElement('#text');node.textContent=value;return node;};
  document.createDocumentFragment=()=>new SearchElement('#fragment');document.getElementById=id=>descendants(document).find(node=>node.id===id)||null;
  const add=(tag,id,parent=body)=>{const node=document.createElement(tag);node.id=id;parent.append(node);return node;};
  let input,form;
  if(kind==='home'){
    form=add('form','home-search-form');input=add('input','home-search-input',form);input.value=query;
    for(const [tag,id]of [['p','status'],['ol','results'],['details','related'],['ol','related-results'],['summary','related-label'],['a','all']])add(tag,'home-search-'+id);
  }else{
    const main=add('main','search-main');main.setAttribute('data-search-index','/search/index.json?v=fixture');
    input=add('input','search-query',main);input.value=query;
    for(const [tag,id]of [['p','status'],['ol','results'],['button','more'],['div','examples'],['select','scope'],['details','related'],['summary','related-title'],['ol','related-results']])add(tag,'search-'+id,main);
  }
  const location=new URL('https://hrkoyama.github.io/'+(kind==='home'?'numerical-methods-atlas/':'search/')+'?scope=atlas&lang='+language+(query?'#q='+encodeURIComponent(query):''));
  const fetches=[],historyWrites=[],windowEvents=new SearchElement('#window');
  const history={pushState(_state,_title,url){historyWrites.push(String(url));location.href=new URL(url,location).href;},replaceState(_state,_title,url){historyWrites.push(String(url));location.href=new URL(url,location).href;}};
  const values={document,location,history,addEventListener:(...args)=>windowEvents.addEventListener(...args),fetch:async(url,options)=>{fetches.push({url:String(url),options});return fetchOverride?fetchOverride(url,options):{ok:true,json:async()=>index};},localStorage:new Proxy({},{get(){throw Error('Search must not access persistent query storage');}}),sessionStorage:new Proxy({},{get(){throw Error('Search must not access query storage');}}),navigator:{sendBeacon(){throw Error('Search must not transmit queries');}}};
  const previous=new Map(Object.keys(values).map(key=>[key,Object.getOwnPropertyDescriptor(globalThis,key)]));
  for(const [key,value]of Object.entries(values))Object.defineProperty(globalThis,key,{value,writable:true,configurable:true});
  return {document,input,form,created,fetches,historyWrites,location,nodes:document.getElementById,fireWindow:(...args)=>windowEvents.fire(...args),restore(){for(const [key,descriptor]of previous){if(descriptor)Object.defineProperty(globalThis,key,descriptor);else delete globalThis[key];}}};
}
export const flushSearch=async()=>{await new Promise(resolve=>setImmediate(resolve));await new Promise(resolve=>setImmediate(resolve));};
