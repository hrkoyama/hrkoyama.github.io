// Generated from frontend/search/compact-index.mjs by scripts/search_assets.py. Edit the source template.
/** Decode a fixed public vocabulary; fetch only fixed same-site detail assets. */
const decoded=new WeakMap(),pending=new Map();
export function unpackSearchIndex(data){
 if(data?.format!=='compact-search-v1')return data;
 if(decoded.has(data))return decoded.get(data);
 if(!Array.isArray(data.terms)||data.terms.length>500000||data.terms.some(word=>typeof word!=='string'))throw Error('Invalid search vocabulary');
 const expand=indices=>{
  if(!Array.isArray(indices))throw Error('Invalid search terms');
  let previous=0;
  return indices.map(delta=>{
   if(!Number.isInteger(delta)||delta<0)throw Error('Invalid search terms');
   const index=data.term_encoding==='sorted-delta'?previous+delta:delta;previous=index;
   if(index>=data.terms.length)throw Error('Invalid search terms');
   return data.terms[index];
  }).join(' ');
 };
 const field=data.kind==='atlas'?'entries':'documents';
 if(!Array.isArray(data[field])||data[field].length>2000)throw Error('Invalid search records');
 const rows=data[field].map(row=>{
  const terms=row.search_terms;
  const searchText=Array.isArray(terms)?expand(terms):Object.fromEntries(Object.entries(terms||{}).map(([language,ids])=>[language,expand(ids)]));
  const {search_terms,...record}=row;return {...record,search_text:searchText};
 });
 const {terms,...rest}=data,result={...rest,format:'unpacked-search-v1',[field]:rows};decoded.set(data,result);return result;
}
export function searchDetailURL(key){
 if(typeof key!=='string'||! /^[a-f0-9]{64}$/.test(key))throw Error('Invalid search detail key');
 return new URL('./details/'+key+'.json',import.meta.url);
}
export function loadSearchDetail(key){
 const url=searchDetailURL(key);
 if(!pending.has(key))pending.set(key,fetch(url,{credentials:'omit'}).then(response=>{
  if(!response.ok)throw Error('Search detail unavailable');return response.json();
 }).then(data=>{if(!data||typeof data!=='object'||Array.isArray(data))throw Error('Invalid search detail');return data;}).catch(error=>{pending.delete(key);throw error;}));
 return pending.get(key);
}
