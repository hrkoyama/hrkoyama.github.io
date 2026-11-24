// Generated from frontend/search/compact-index.mjs by scripts/search_assets.py. Edit the source template.
/** Restore the optional lossless row-value and details.keys string pool. */
export const ROW_STRING_LIMITS=Object.freeze({pool:50000,poolUnits:8200000,stringUnits:1000000,expandedUnits:16400000,nodes:1000000,depth:64,rows:2000});
const ENCODING='shared-raw-strings-v1',PREFIX='~s:';
const own=(value,key)=>Object.prototype.hasOwnProperty.call(value,key);
const plain=value=>value!==null&&typeof value==='object'&&!Array.isArray(value)&&Object.getPrototypeOf(value)===Object.prototype;
const scalarString=value=>typeof value==='string'&&!/[\uD800-\uDFFF]/u.test(value);
const invalid=()=>{throw Error('Invalid pooled row strings');};
export function restoreRowStrings(data){
 if(!data||typeof data!=='object')return data;
 if(data.row_string_encoding===undefined){
  if(own(data,'row_strings'))invalid();
  return data; // Old compact and already-unpacked payloads retain their API.
 }
 if(!plain(data)||data.format!=='compact-search-v1'||data.row_string_encoding!==ENCODING||!['atlas','site'].includes(data.kind))invalid();
 const pool=data.row_strings;
 if(!Array.isArray(pool)||Object.getPrototypeOf(pool)!==Array.prototype||pool.length>ROW_STRING_LIMITS.pool)invalid();
 let poolUnits=0;
 const seen=new Set();
 for(const text of pool){
  if(!scalarString(text)||text.length>ROW_STRING_LIMITS.stringUnits||seen.has(text))invalid();
  seen.add(text);poolUnits+=text.length;if(poolUnits>ROW_STRING_LIMITS.poolUnits)invalid();
 }
 const field=data.kind==='atlas'?'entries':'documents';
 if(!Array.isArray(data[field])||Object.getPrototypeOf(data[field])!==Array.prototype||data[field].length>ROW_STRING_LIMITS.rows)invalid();
 for(let i=0;i<data[field].length;i++)if(!own(data[field],i)||!plain(data[field][i]))invalid();
 let nodes=0,units=0;
 const charge=text=>{units+=text.length;if(units>ROW_STRING_LIMITS.expandedUnits)invalid();return text;};
 const restore=(value,depth=0)=>{
  if(++nodes>ROW_STRING_LIMITS.nodes||depth>ROW_STRING_LIMITS.depth)invalid();
  if(typeof value==='string'){
   if(!scalarString(value))invalid();
   if(!value.startsWith(PREFIX))return charge(value);
   const suffix=value.slice(PREFIX.length);
   if(suffix.startsWith('~'))return charge(PREFIX+suffix.slice(1));
   if(!/^(?:0|[1-9a-z][0-9a-z]{0,3})$/.test(suffix))invalid();
   const index=parseInt(suffix,36);
   if(index>=pool.length||index.toString(36)!==suffix)invalid();
   // Pool entries are raw strings, never recursively interpreted as tokens.
   return charge(pool[index]);
  }
  if(Array.isArray(value)){
   if(Object.getPrototypeOf(value)!==Array.prototype||value.length>ROW_STRING_LIMITS.nodes-nodes)invalid();
   const result=[];
   for(let i=0;i<value.length;i++){if(!own(value,i))invalid();result.push(restore(value[i],depth+1));}
   return result;
  }
  if(value&&typeof value==='object'){
   if(!plain(value))invalid();
   // CreateDataProperty preserves an own '__proto__' key without invoking a setter.
   return Object.fromEntries(Object.entries(value).map(([key,item])=>{if(!scalarString(key))invalid();charge(key);return [key,restore(item,depth+1)];}));
  }
  if(value!==null&&typeof value!=='boolean'&&(typeof value!=='number'||!Number.isFinite(value)))invalid();
  return value;
 };
 const rows=data[field].map(row=>restore(row));
 const {row_string_encoding,row_strings,...header}=data;
 const result={...header,[field]:rows};
 if(own(data,'details')){
  if(!plain(data.details))invalid();
  if(own(data.details,'keys')){
   if(!Array.isArray(data.details.keys)||data.details.keys.some(key=>typeof key!=='string'))invalid();
   const keys=restore(data.details.keys);
   result.details={...data.details,keys};
  }
 }
 return result;
}

/** Decode a fixed public vocabulary; fetch only fixed same-site detail assets. */
const decoded=new WeakMap(),pending=new Map();
const MAX_TERMS=500000,MAX_VOCABULARY_UNITS=8200000;
function vocabulary(data){
 const packed=data.terms;
 if(!Array.isArray(packed))throw Error('Invalid search vocabulary');
 if(data.vocabulary_encoding===undefined){
  if(packed.length>MAX_TERMS||packed.some(word=>typeof word!=='string'))throw Error('Invalid search vocabulary');
  return packed;
 }
 if(data.vocabulary_encoding!=='unicode-prefix-flat-v1'||packed.length%2||packed.length>2*MAX_TERMS)throw Error('Invalid search vocabulary');
 const words=[];let previous=[],units=0;
 for(let i=0;i<packed.length;i+=2){
  const prefix=packed[i],suffix=packed[i+1];
  if(!Number.isInteger(prefix)||prefix<0||prefix>previous.length||typeof suffix!=='string'||/[\uD800-\uDFFF]/u.test(suffix))throw Error('Invalid search vocabulary');
  if(suffix.length>MAX_VOCABULARY_UNITS-units)throw Error('Invalid search vocabulary');
  // Python len/slicing count Unicode code points, unlike JS string offsets.
  const points=previous.slice(0,prefix).concat(Array.from(suffix)),word=points.join('');
  units+=word.length;if(units>MAX_VOCABULARY_UNITS)throw Error('Invalid search vocabulary');
  words.push(word);previous=points;
 }
 return words;
}
function varints(value,limit){
 if(typeof value!=='string'||value.length>4*MAX_TERMS||! /^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$/.test(value))throw Error('Invalid search terms');
 const raw=atob(value);
 if(btoa(raw)!==value)throw Error('Invalid search terms');
 const values=[];let number=0,factor=1,bytes=0;
 for(let i=0;i<raw.length;i++){
  const byte=raw.charCodeAt(i);number+=(byte%128)*factor;bytes++;
  if(number>=limit||bytes>3)throw Error('Invalid search terms');
  if(byte<128){
   if(bytes>1&&byte===0)throw Error('Invalid search terms');
   values.push(number);if(values.length>MAX_TERMS)throw Error('Invalid search terms');
   number=0;factor=1;bytes=0;
  }else factor*=128;
 }
 if(bytes)throw Error('Invalid search terms');
 return values;
}
export function unpackSearchIndex(data){
 if(data?.format!=='compact-search-v1'){
  if(data&&typeof data==='object'&&('row_string_encoding' in data||'row_strings' in data))throw Error('Invalid pooled row strings');
  return data;
 }
 if(decoded.has(data))return decoded.get(data);
 const source=data;data=restoreRowStrings(data);
 const words=vocabulary(data),binary=data.term_encoding==='sorted-delta-varint-base64';
 if(data.term_encoding!==undefined&&!['sorted-delta','sorted-delta-varint-base64'].includes(data.term_encoding))throw Error('Invalid search terms');
 const expand=indices=>{
  if(binary)indices=varints(indices,words.length);
  if(!Array.isArray(indices))throw Error('Invalid search terms');
  let previous=0;
  return indices.map((delta,position)=>{
   if(!Number.isInteger(delta)||delta<0)throw Error('Invalid search terms');
   if(binary&&position>0&&delta===0)throw Error('Invalid search terms');
   const index=binary||data.term_encoding==='sorted-delta'?previous+delta:delta;previous=index;
   if(index>=words.length)throw Error('Invalid search terms');
   return words[index];
  }).join(' ');
 };
 const field=data.kind==='atlas'?'entries':'documents';
 if(!Array.isArray(data[field])||data[field].length>2000)throw Error('Invalid search records');
 const rows=data[field].map(row=>{
  const terms=row.search_terms;
  const searchText=Array.isArray(terms)||typeof terms==='string'?expand(terms):Object.fromEntries(Object.entries(terms||{}).map(([language,ids])=>[language,expand(ids)]));
  const {search_terms,...record}=row;return {...record,search_text:searchText};
 });
 const {terms,vocabulary_encoding,...rest}=data;
 // Preserve the legacy unpacked record/header API; storage codecs are private
 // to this loader. Both old numeric arrays and the new byte strings decode here.
 if(binary)rest.term_encoding='sorted-delta';
 const result={...rest,format:'unpacked-search-v1',[field]:rows};decoded.set(source,result);return result;
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
